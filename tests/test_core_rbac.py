from django.test import TestCase
from core.models import User, Role, AuditLog, CompanyProfile
from core.services import AuthService, RBACService


class RBACAndSecurityTestCase(TestCase):
    def setUp(self):
        self.admin_role = Role.objects.create(code='ADMIN', name='Admin', can_manage_users=True)
        self.tech_role = Role.objects.create(code='TECH', name='Technician', can_perform_repairs=True)
        self.user = User.objects.create_user(
            username='johndoe',
            email='john@test.com',
            password='TestPass123!'
        )

    def test_role_assignment(self):
        result = RBACService.assign_role_to_user(self.user, 'TECH')
        self.assertTrue(result)
        self.user.refresh_from_db()
        self.assertEqual(self.user.role.code, 'TECH')
        self.assertTrue(self.user.has_role_permission('can_perform_repairs'))
        self.assertFalse(self.user.has_role_permission('can_manage_users'))

    def test_login_audit_recording(self):
        AuthService.record_login_success(self.user, '192.168.1.50', 'TestAgent/1.0')
        log = AuditLog.objects.filter(user=self.user, action='LOGIN').first()
        self.assertIsNotNone(log)
        self.assertEqual(log.ip_address, '192.168.1.50')
