"""
Core Enterprise Middlewares for LaptopERP:
- Audit Log Recording for all write and state change actions
- Security Header Enforcement
- Maintenance Mode Checker
"""

import json
from django.utils import timezone
from django.conf import settings
from .models import AuditLog, SystemSetting


class AuditLogMiddleware:
    """Middleware to automatically record API / View actions to AuditLog."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Skip recording static, media and safe GET requests without state changes
        if request.path.startswith(('/static/', '/media/', '/favicon.ico')):
            return response

        if request.method in ('POST', 'PUT', 'PATCH', 'DELETE') and request.user.is_authenticated:
            try:
                ip = self.get_client_ip(request)
                module_name = request.path.strip('/').split('/')[0] or 'root'
                
                # Determine action type
                action_map = {'POST': 'CREATE', 'PUT': 'UPDATE', 'PATCH': 'UPDATE', 'DELETE': 'DELETE'}
                action = action_map.get(request.method, 'UPDATE')
                
                details_dict = {
                    'path': request.path,
                    'status_code': response.status_code,
                    'query_params': dict(request.GET),
                }

                AuditLog.objects.create(
                    user=request.user,
                    action=action,
                    module=module_name.upper(),
                    entity_name=request.path[:128],
                    ip_address=ip,
                    user_agent=request.META.get('HTTP_USER_AGENT', '')[:255],
                    details=json.dumps(details_dict),
                )
            except Exception as e:
                # Middleware must never crash the request flow
                pass

        return response

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class EnterpriseSecurityHeaderMiddleware:
    """Enforces strict security headers across all web and API responses."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        return response
