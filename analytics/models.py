"""
Analytics Snapshots and Historical Metrics Models.
"""

import uuid
from django.db import models
from core.models import TimeStampedUUIDModel


class DailyKPIReport(TimeStampedUUIDModel):
    """Aggregated daily performance summary."""
    report_date = models.DateField(unique=True)
    total_sales_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    units_sold = models.PositiveIntegerField(default=0)
    units_received = models.PositiveIntegerField(default=0)
    repairs_completed = models.PositiveIntegerField(default=0)
    rma_opened = models.PositiveIntegerField(default=0)
    total_stock_value = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)

    class Meta:
        ordering = ['-report_date']

    def __str__(self):
        return f"Daily KPI: {self.report_date} (${self.total_sales_amount})"
