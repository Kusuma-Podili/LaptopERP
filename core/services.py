"""
Enterprise Business Services for Identity, RBAC, and Audit Logging.
"""

import json
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import transaction
from .models import Role, AuditLog, Notification, SystemSetting, CompanyProfile

User = get_user_model()


class AuthService:
    """Handles user authentication, lockout security, and credential rotation."""
    
    @staticmethod
    def record_login_success(user, ip_address, user_agent):
        user.failed_login_attempts = 0
        user.account_locked_until = None
        user.last_login = timezone.now()
        user.save(update_fields=['failed_login_attempts', 'account_locked_until', 'last_login'])
        
        AuditLog.objects.create(
            user=user,
            action='LOGIN',
            module='CORE',
            entity_name='User Auth',
            entity_id=str(user.id),
            ip_address=ip_address,
            user_agent=user_agent,
            details=f"Successful login from IP {ip_address}"
        )

    @staticmethod
    def record_login_failure(user, ip_address):
        user.failed_login_attempts += 1
        if user.failed_login_attempts >= 5:
            user.account_locked_until = timezone.now() + timezone.timedelta(minutes=30)
        user.save(update_fields=['failed_login_attempts', 'account_locked_until'])


class RBACService:
    """Manages role provisioning, permission checks, and user assignment."""

    @staticmethod
    def assign_role_to_user(user, role_code, assigned_by=None):
        try:
            role = Role.objects.get(code=role_code)
            user.role = role
            user.save(update_fields=['role'])
            if assigned_by:
                AuditLog.objects.create(
                    user=assigned_by,
                    action='STATUS_CHANGE',
                    module='RBAC',
                    entity_name='User Role Assignment',
                    entity_id=str(user.id),
                    details=f"Assigned role {role.name} to {user.username}"
                )
            return True
        except Role.DoesNotExist:
            return False


class NotificationService:
    """Creates and dispatches system notifications to users."""

    @staticmethod
    def notify_user(user, title, message, severity='INFO', link=''):
        return Notification.objects.create(
            recipient=user,
            title=title,
            message=message,
            severity=severity,
            link_url=link
        )

    @staticmethod
    def notify_role(role_code, title, message, severity='INFO', link=''):
        users = User.objects.filter(role__code=role_code, is_active=True)
        notifications = [
            Notification(
                recipient=u,
                title=title,
                message=message,
                severity=severity,
                link_url=link
            ) for u in users
        ]
        return Notification.objects.bulk_create(notifications)


class SecuritySessionMonitor:
    """Enterprise Session Security & Geo-Anomaly Monitor."""
    @staticmethod
    def inspect_session_fingerprint(user_id: str, current_ip: str, previous_ip: str = None, user_agent: str = ""):
        is_ip_changed = bool(previous_ip and previous_ip != current_ip)
        is_suspicious = is_ip_changed and not current_ip.startswith("192.168.") and not current_ip.startswith("10.") and current_ip != "127.0.0.1"
        
        return {
            "user_id": user_id,
            "current_ip": current_ip,
            "ip_changed": is_ip_changed,
            "risk_level": "HIGH" if is_suspicious else "LOW",
            "require_2fa_prompt": is_suspicious,
            "security_action": "CHALLENGE_2FA" if is_suspicious else "ALLOW",
        }

