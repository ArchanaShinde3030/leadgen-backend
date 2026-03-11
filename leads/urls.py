# leadgen/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, admin_login
from . import views
from .views import send_bulk_outreach

router = DefaultRouter()
router.register(r'leads', LeadViewSet, basename='leads')
lead_list = LeadViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('login/', admin_login, name='login'),
    path('', include(router.urls)),
    path('leads/', lead_list, name='lead-list'),
    path('send-email/<int:lead_id>/', views.send_email_to_lead, name='send_email'),
    path('send-bulk-outreach/', send_bulk_outreach),
]