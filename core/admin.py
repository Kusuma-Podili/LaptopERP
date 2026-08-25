from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role, Department, Branch, CompanyProfile, AuditLog, SystemSetting, Notification


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'department', 'branch', 'is_staff']
    list_filter = ['role', 'department', 'branch', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Enterprise Metadata', {'fields': ('employee_id', 'role', 'department', 'branch', 'phone_number', 'is_technician', 'hourly_rate')}),
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'can_manage_inventory', 'can_perform_repairs', 'can_manage_sales', 'can_view_analytics']
    search_fields = ['name', 'code']


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'user', 'action', 'module', 'entity_name', 'ip_address']
    list_filter = ['action', 'module', 'timestamp']
    readonly_fields = [f.name for f in AuditLog._meta.fields]


admin.site.register(CompanyProfile)
admin.site.register(Branch)
admin.site.register(Department)
admin.site.register(SystemSetting)
admin.site.register(Notification)
