from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import SMSMessage
from django.utils import timezone
from datetime import timedelta

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('admin/', admin.site.urls),
    path('', include('sms_service.urls')),
    path('api/send-sms/', views.send_sms, name='send_sms'),
    path('api/get-sms-messages/', views.get_sms_messages, name='get_sms_messages'),
]


def send_sms(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        message_body = request.POST['message_body']

        # Check for duplicate SMS messages
        duplicate_messages = SMSMessage.objects.filter(
            phone_number=phone_number,
            message_body=message_body,
            timestamp__gte=timezone.now() - timedelta(minutes=5)  # Allow duplicates within the last 5 minutes
        )

        if duplicate_messages.exists():
            messages.warning(request, 'Duplicate message detected. Message not sent.')
            return JsonResponse({'message': 'Duplicate message detected.'}, status=400)

        # If not a duplicate, save the SMS message
        sms_message = SMSMessage.objects.create(
            phone_number=phone_number,
            message_body=message_body
        )

        # Implement Twilio integration to send the SMS
        # ...

        return JsonResponse({'message': 'SMS sent successfully'})

