import logging
from re import L
from django.core.management.base import BaseCommand
from django.utils import timezone
from  finance.models import *
from finance.tasks import iterator_data
from django.core.paginator import Paginator

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Loading Initial Data: {}".format(timezone.now()))
        try:
            qs = DailyPerformance.objects.filter().exclude(cost=0)
            qs = qs.annotate(
                two_x_cost=ExpressionWrapper(
                    (F('revenue')*2),
                    output_field=models.IntegerField()
                )
            ).filter(Q(revenue__lt=F('two_x_cost')) | Q(revenue__gt=1000)).values('id')
            p = Paginator(qs, 50)
            for i in p.page_range:
                pg = []
                for q in p.page(i).object_list:
                    pg.append(q['id'])
                iterator_data.delay(pg)
        except Exception as exc:
            logger.error("Something went wrong while slow iteration: {}".format(exc))

