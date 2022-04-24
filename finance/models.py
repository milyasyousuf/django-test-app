
from django.db import models
from django.db.models import ExpressionWrapper, F, Q

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

    @classmethod
    def create_model(cls, **data):
        return HourlyPerformance(**data)

class DailyPerformanceManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    # create a method called filter_by_min_roi(min_roi: float) so you can do
    # DailyPerformance.objects.filter_by_min_roi(min_roi=0.5)
    # -- ROI in economics is return on investment and it's the result from the profit/costs, usually expressed in % --
    def filter_by_min_roi(self, min_roi=0.5):
        qs =  super().get_queryset()
        return qs.annotate(
            roi=ExpressionWrapper(
                (F('profit') / F('cost')*100),
                output_field=models.IntegerField()
            )
        ).filter(roi__gt=int(min_roi*100))


class DailyPerformance(Perfomance):
    profit = models.FloatField(default=0.0)
    created_at = models.DateField()

    objects = DailyPerformanceManger()

    @classmethod
    def create_model(cls, **data):
        return DailyPerformance(**data)

    def __str__(self):
        return str(self.id)
