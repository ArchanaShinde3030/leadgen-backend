from django.contrib import admin
from .models import Lead, EmailTemplate


class LeadAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'job_title', 'location', 'status', 'source_url', 'tech_stack')
    search_fields = ('company_name', 'job_title', 'location', 'tech_stack') 
    list_filter = ('status', 'location')
    ordering = ('company_name',)
    list_per_page = 25 


admin.site.register(Lead, LeadAdmin)
admin.site.register(EmailTemplate)