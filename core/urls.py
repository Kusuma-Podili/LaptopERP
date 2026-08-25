from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('login/', views.EnterpriseLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/create/', views.UserCreateView.as_view(), name='user_create'),
    path('audit-logs/', views.AuditLogListView.as_view(), name='audit_logs'),
    path('settings/', views.SystemSettingsView.as_view(), name='settings'),
]
