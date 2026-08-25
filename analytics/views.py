from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .services.engine import AnalyticsCalculationEngine


class ExecutiveDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/executive_dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['kpi'] = AnalyticsCalculationEngine.get_executive_summary()
        return ctx
