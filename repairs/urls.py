from django.urls import path
from . import views

app_name = 'repairs'

urlpatterns = [
    path('jobs/', views.JobCardListView.as_view(), name='job_card_list'),
    path('jobs/<uuid:pk>/', views.JobCardDetailView.as_view(), name='job_card_detail'),
    path('board/', views.TechnicianBoardView.as_view(), name='technician_board'),
]
