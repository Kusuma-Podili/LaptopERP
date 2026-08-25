"""
Core Web Views: Dashboard, Login, User Management, Audit Logs, and Company Settings.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone
from .models import User, Role, AuditLog, CompanyProfile, Department, Branch, SystemSetting, Notification
from .forms import CustomLoginForm, EnterpriseUserCreateForm, CompanyProfileForm
from .services import AuthService, RBACService


class EnterpriseLoginView(LoginView):
    template_name = 'core/login.html'
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.get_user()
        ip = self.request.META.get('REMOTE_ADDR')
        ua = self.request.META.get('HTTP_USER_AGENT', '')
        AuthService.record_login_success(user, ip, ua)
        return super().form_valid(form)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user
        ctx['total_users'] = User.objects.filter(is_active=True).count()
        ctx['recent_audit_logs'] = AuditLog.objects.select_related('user').all()[:10]
        ctx['notifications'] = Notification.objects.filter(recipient=user, is_read=False)[:5]
        return ctx


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'core/user_list.html'
    context_object_name = 'users'
    paginate_by = 25

    def get_queryset(self):
        return User.objects.select_related('role', 'department', 'branch').all()


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = EnterpriseUserCreateForm
    template_name = 'core/user_form.html'
    success_url = reverse_lazy('core:user_list')

    def form_valid(self, form):
        messages.success(self.request, "New enterprise user created successfully.")
        return super().form_valid(form)


class AuditLogListView(LoginRequiredMixin, ListView):
    model = AuditLog
    template_name = 'core/audit_logs.html'
    context_object_name = 'audit_logs'
    paginate_by = 50

    def get_queryset(self):
        qs = AuditLog.objects.select_related('user').all()
        module = self.request.GET.get('module')
        if module:
            qs = qs.filter(module__iexact=module)
        return qs


class SystemSettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'core/settings.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['company'] = CompanyProfile.objects.first()
        ctx['settings'] = SystemSetting.objects.all()
        return ctx
