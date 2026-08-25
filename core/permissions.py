"""
RBAC Permissions for Django Views and DRF API Endpoints.
"""

from rest_framework import permissions
from django.contrib.auth.mixins import UserPassesTestMixin


class BaseRolePermissionMixin(UserPassesTestMixin):
    role_perm_attribute = None

    def test_func(self):
        user = self.request.user
        if not user.is_authenticated:
            return False
        if user.is_superuser:
            return True
        if not self.role_perm_attribute:
            return True
        return user.has_role_permission(self.role_perm_attribute)


class IsAdminUserOrSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (request.user.is_superuser or request.user.has_role_permission('can_manage_users')))


class HasModulePermission(permissions.BasePermission):
    module_perm = 'can_manage_inventory'

    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False
        if request.user.is_superuser:
            return True
        return request.user.has_role_permission(self.module_perm)
