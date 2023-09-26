from django.db import models
from django.db import models

class SMSMessage(models.Model):
    phone_number = models.CharField(max_length=15)
    message_body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # sms_service/models.py

    class SMSMessage(models.Model):
        phone_number = models.CharField(max_length=15)
        message_body = models.TextField()
        timestamp = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f'{self.phone_number} ({self.timestamp})'

class SMSMessage(models.Model):
    message_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=15)
    message_body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message ID: {self.message_id}, Phone Number: {self.phone_number}, Timestamp: {self.timestamp}'
