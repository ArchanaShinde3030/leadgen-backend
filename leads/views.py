
from rest_framework import viewsets
from .models import Lead
from .serializers import LeadSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.http import JsonResponse
import json
from rest_framework import viewsets, filters
from leads.models import Lead
from leads.serializers import LeadSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['location', 'job_title', 'tech_stack', 'company_name']

@csrf_exempt 
def admin_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid username or password'}, status=401)

# ----------------------------- SMTP ------------------------------------------
        
        
from django.core.mail import send_mail
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Lead, EmailTemplate

@api_view(['POST'])
def send_email_to_lead(request, lead_id):
    try:
        lead = Lead.objects.get(id=lead_id)

        if not lead.contact_email:
            return Response({"error": "No email available"}, status=400)

       
        template = EmailTemplate.objects.first()

        if not template:
            return Response({"error": "No template found"}, status=400)

        # Dynamic replace
        subject = template.subject
        message = template.body
        message = message.replace("{{company_name}}", lead.company_name or "")
        message = message.replace("{{job_title}}", lead.job_title or "")

        # Email send
        send_mail(
            subject,
            message,
            'yourgmail@gmail.com',
            [lead.contact_email],
            fail_silently=False,
        )

        # Lead update
        lead.email_sent = True
        lead.email_template_used = template
        lead.email_sent_at = timezone.now()
        lead.status = 'contacted'
        lead.save()

        return Response({"message": "Email sent successfully"})

    except Lead.DoesNotExist:
        return Response({"error": "Lead not found"}, status=404)


# -----------------both Use SMTP and OUTREACH----------------------------------

from django.core.mail import send_mail
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Lead, EmailTemplate

@api_view(['POST'])
def send_bulk_outreach(request):
    template = EmailTemplate.objects.first()

    if not template:
        return Response({"error": "No template found"}, status=400)

    leads = Lead.objects.filter(email_sent=False).exclude(contact_email__isnull=True)

    count = 0

    for lead in leads:
        message = template.body
        message = message.replace("{{company_name}}", lead.company_name or "")
        message = message.replace("{{job_title}}", lead.job_title or "")

        try:
            send_mail(
                template.subject,
                message,
                'yourgmail@gmail.com',
                [lead.contact_email],
                fail_silently=True,
            )

            lead.email_sent = True
            lead.email_template_used = template
            lead.email_sent_at = timezone.now()
            lead.status = 'contacted'
            lead.save()

            count += 1

        except Exception as e:
            print(f"Failed for {lead.contact_email}: {e}")

    return Response({"message": f"{count} outreach emails sent"})