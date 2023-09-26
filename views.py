# sms_service/views.py

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import SMSMessage
from .models import SMSMessage


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('sms_history')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')



from twilio.rest import Client
from django.http import JsonResponse

def send_sms(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        message_body = request.POST['message_body']

        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        try:
            # Send the SMS using Twilio
            message = client.messages.create(
                body=message_body,
                from_=TWILIO_PHONE_NUMBER,
                to=phone_number
            )

            response = {
                'message': 'SMS sent successfully',
                'sms_sid': message.sid
            }
            return JsonResponse(response, status=200)

        except Exception as e:
            response = {
                'message': 'Failed to send SMS',
                'error': str(e)
            }
            return JsonResponse(response, status=500)

        def get_sms_messages(request):
            if request.method == 'GET':
                # Retrieve sent SMS messages from the database
                sms_messages = SMSMessage.objects.all().order_by('-timestamp')

                # Create a list of dictionaries representing SMS messages
                sms_list = [
                    {
                        'phone_number': msg.phone_number,
                        'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                        'message_body': msg.message_body
                    }
                    for msg in sms_messages
                ]

                return JsonResponse(sms_list, safe=False, status=200)



            def send_sms(request):
                # ...
                sms_message = SMSMessage.objects.create(
                    phone_number=phone_number,
                    message_body=message_body
                )
                # ...

            def get_sms_messages(request):
                # Retrieve sent SMS messages from the database
                sms_messages = SMSMessage.objects.all().order_by('-timestamp')
                # ...




