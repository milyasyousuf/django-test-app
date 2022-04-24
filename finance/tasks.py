

from celery import shared_task
from finance.models import *
import time
@shared_task(bind=True)
def iterator_data(self, ids):


    # create another script called slow_iteration.py
    # in this script filter DailyPerformance where revenue > 2*cost or revenue > 1000, excluding records with cost=0 .Limit the queryset to 50 records.
    # Iter over this queryset, and add a time.sleep(60) inside the loop. Implement this with a celery task
    data = DailyPerformance.objects.filter(id__in=ids)
    print("==============================")
    for d in data.iterator():
        print(d.__dict__)
    time.sleep(6)
    print("==============================")

#celery -A app flower  --address=0.0.0.0 --port=5566 --basic_auth=agflower:Test@1234