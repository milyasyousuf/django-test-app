from django.contrib import admin

from .models import *


class DailyPerformanceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cost",
        "revenue",
        "profit",
        "created_at"
    )

class HourlyPerformanceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cost",
        "revenue",
        "profit",
        "created_at"
    )


admin.site.register(HourlyPerformance, HourlyPerformanceAdmin)
admin.site.register(DailyPerformance, DailyPerformanceAdmin)
