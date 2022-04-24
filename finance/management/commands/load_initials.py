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


    def randomDate(self, start, end):
        stime = int(start.strftime("%s"))
        etime = int(end.strftime("%s"))
        ptime = stime + random.random() * (etime - stime)
        dt = datetime.fromtimestamp(time.mktime(time.localtime(ptime)))
        return dt

    def generate_daily_data(self):
        start_date = timezone.now() - timedelta(days=7)
        end_date = timezone.now()
        dates = [start_date+timedelta(days=x) for x in range((end_date-start_date).days)]
        obj_list = []
        for date in dates:
            cost=random.randint(50,120)
            revenue=random.randint(50,100)
            obj_list.append(
                DailyPerformance(
                    cost=cost,
                    revenue=revenue,
                    created_at=date,
                    profit = revenue - cost
                )
            )
        DailyPerformance.objects.bulk_create(obj_list)


    def generate_hourly_data(self):
        start_date = timezone.now() - timedelta(days=1)
        end_date = timezone.now()
        obj_list = []
        for i in range(0 , 10):
            cost=random.randint(50,120)
            revenue=random.randint(50,100)
            obj_list.append(
                HourlyPerformance(
                    cost=cost,
                    revenue=revenue,
                    created_at=self.randomDate(start_date, end_date),
                    profit = revenue - cost
                )
            )
        HourlyPerformance.objects.bulk_create(obj_list)

    def handle(self, *args, **options):
        logger.info("Loading Initial Data: {}".format(timezone.now()))
        try:
            logger.info("Loading end now: {}".format(timezone.now()))
            self.generate_daily_data()
            self.generate_hourly_data()
        except Exception as exc:
            logger.error("Something went wrong while fortnight creation, {}".format(exc))

