
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import EmailForm

def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                send_mail(
                    form.cleaned_data['subject'],  # The subject of the email
                    form.cleaned_data['message'],  # The message body of the email
                    'lasya1220@zohomail.in',  # Your email address (sender)
                    [form.cleaned_data['recipient_email']],  # The recipient's email address
                    fail_silently=False,
                )
                # If email is successfully sent, render the success page
                return render(request, 'email_sent.html')
            except Exception as e:
                # In case of an error, return a message
                return render(request, 'email_sent.html', {'error': str(e)})
    else:
        form = EmailForm()  # Instantiate an empty form
    return render(request, 'send_email.html', {'form': form})



# Create your views here.
