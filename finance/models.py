
from django.db import models
from django.db.models.signals import post_save

class Perfomance(models.Model):
    cost = models.FloatField(default=0.0)
    revenue = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True


class HourlyPerformanceManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def filter_by_min_roi(self, min_roi=0.5):
        return super().get_queryset()


class HourlyPerformance(Perfomance):
    profit = models.FloatField(default=0.0)
    created_at = models.DateTimeField(null=True,blank=True)

    objects = HourlyPerformanceManger()

    def __str__(self):
        return str(self.id)

class DailyPerformanceManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def filter_by_min_roi(self, min_roi=0.5):
        return super().get_queryset()

class DailyPerformance(Perfomance):
    profit = models.FloatField(default=0.0)
    created_at = models.DateField()

    objects = DailyPerformanceManger()


    def __str__(self):
        return str(self.id)
