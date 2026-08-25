from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import WorkshopJobCard, DiagnosticChecklistMaster, DiagnosticResult, JobCardPartRequisition


class JobCardListView(LoginRequiredMixin, ListView):
    model = WorkshopJobCard
    template_name = 'repairs/job_card_list.html'
    context_object_name = 'job_cards'
    paginate_by = 25

    def get_queryset(self):
        qs = WorkshopJobCard.objects.select_related('unit', 'unit__laptop_model', 'assigned_technician').all()
        status = self.request.GET.get('status')
        if status:
            qs = qs.filter(status=status)
        return qs


class JobCardDetailView(LoginRequiredMixin, DetailView):
    model = WorkshopJobCard
    template_name = 'repairs/job_card_detail.html'
    context_object_name = 'job'


class TechnicianBoardView(LoginRequiredMixin, TemplateView):
    template_name = 'repairs/technician_board.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['queued'] = WorkshopJobCard.objects.filter(status='QUEUED')[:10]
        ctx['in_progress'] = WorkshopJobCard.objects.filter(status__in=['IN_DIAGNOSTICS', 'REPAIR_IN_PROGRESS'])[:10]
        ctx['qa_testing'] = WorkshopJobCard.objects.filter(status='QA_TESTING')[:10]
        ctx['completed'] = WorkshopJobCard.objects.filter(status='COMPLETED')[:10]
        return ctx
