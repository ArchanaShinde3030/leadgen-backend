
from django.contrib import admin
from .models import Lead, EmailTemplate, Tag



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',) 
    search_fields = ('name',)

# Lead admin
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'job_title', 'location', 'status', 'source_url', 'tech_stack')
    search_fields = ('company_name', 'job_title', 'location', 'tech_stack') 
    list_filter = ('status', 'location')
    ordering = ('company_name',)
    list_per_page = 25 
    filter_horizontal = ('tags',) 
    
# EmailTemplate admin
@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject')
    search_fields = ('name', 'subject')