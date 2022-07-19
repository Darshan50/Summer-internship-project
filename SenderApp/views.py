import email
from re import sub
from django.shortcuts import render,redirect
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
from django.contrib import messages
from pdf_mail import sendpdf
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,'index.html')

def send(request):
    if request.method == 'POST':
        emailto = request.POST['emailto']
        subject = request.POST['subject']
        msg = request.POST['msg']
        

        try:
            email = EmailMessage(subject,msg,settings.EMAIL_HOST_USER,[emailto])
            email.content_subtype = 'html'
            try:
                item = request.FILES['item']
                email.attach(item.name,item.read(),item.content_type)
            except:
                pass
            finally:
                email.send()
            messages.success(request, 'Email Sent Successfully')
            return redirect('/')
        except:
            messages.success(request,'Error occured in sending Email, try again!!')