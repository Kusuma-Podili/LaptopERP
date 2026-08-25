from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('dashboard/', views.ExecutiveDashboardView.as_view(), name='executive_dashboard'),
]
