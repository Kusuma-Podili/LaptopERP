from django.contrib import admin
from .models import DiagnosticChecklistMaster, WorkshopJobCard, DiagnosticResult, JobCardPartRequisition, RepairLaborLog

admin.site.register(DiagnosticChecklistMaster)
admin.site.register(WorkshopJobCard)
admin.site.register(DiagnosticResult)
admin.site.register(JobCardPartRequisition)
admin.site.register(RepairLaborLog)
