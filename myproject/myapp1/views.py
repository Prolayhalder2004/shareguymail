# file_mailer/views.py
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import FileEmailForm

def send_email(request):
    if request.method == 'POST':
        form = FileEmailForm(request.POST, request.FILES)
        if form.is_valid():
            recipient_email = form.cleaned_data['email']
            uploaded_file = request.FILES['file']
            
            email = EmailMessage(
                'Hi USER',
                'Here is the File From ShareGUY',
                settings.EMAIL_HOST_USER,
                [recipient_email],
            )
            email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
            email.send(fail_silently=False)
            
            return render(request, 'file_mailer/success.html', {'recipient_email': recipient_email})
    else:
        form = FileEmailForm()
    return render(request, 'file_mailer/send_email.html', {'form': form})
