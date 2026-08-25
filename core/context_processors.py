from .models import CompanyProfile, Notification, SystemAlert
from django.utils import timezone

def erp_global_context(request):
    company = CompanyProfile.objects.first()
    unread_notifications_count = 0
    active_alerts = []
    
    if request.user.is_authenticated:
        unread_notifications_count = Notification.objects.filter(recipient=request.user, is_read=False).count()
        active_alerts = SystemAlert.objects.filter(is_active=True, valid_from__lte=timezone.now())
        
    return {
        'ERP_COMPANY': company,
        'UNREAD_NOTIFICATIONS_COUNT': unread_notifications_count,
        'SYSTEM_ALERTS': active_alerts,
        'CURRENT_YEAR': timezone.now().year,
    }
