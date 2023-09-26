from django.contrib import admin
# sms_service/admin.py

from django.contrib import admin
from .models import SMSMessage

admin.site.register(SMSMessage)
