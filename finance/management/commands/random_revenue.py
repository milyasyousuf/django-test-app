import logging
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from  finance.models import *
import random
import time


logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "This command will help us to create the fortnight in the database"

    def handle(self, *args, **options):
        try:
            qs = DailyPerformance.objects.filter_by_min_roi(min_roi=0.5)
            # print the length of the queryset 50 * 100
            print(qs.count()*50*100)
            # print the length of the queryset multiplied by 2
            print(qs.count()*50*100*2)

            for i in range(qs.count()):
                print("{}/{}: {}".format(i,qs.count(),qs[i].__dict__))
                DailyPerformance.objects.filter(id=qs[i].id).update(
                    revenue=qs[i].revenue * random.uniform(0.5, 2)
                )
        except Exception as exc:
            print("Something went wrong while rando_revenue, {}".format(exc))

