from django.db import models

class Lead(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('ignored', 'Ignored'),
    ]

    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    tech_stack = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255)
    source_url = models.URLField()
    company_website = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    # email
    email_sent = models.BooleanField(default=False)
    email_template_used = models.ForeignKey('EmailTemplate', on_delete=models.SET_NULL, null=True, blank=True)
    email_sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.company_name
    

class EmailTemplate(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.name