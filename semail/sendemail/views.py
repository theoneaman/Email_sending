from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,template_name="home.html")


def send(request):
    x=request.GET["fn"]
    y=request.GET["ln"]
    z=request.GET["em"]
    subject='welcome to world of wonders'
    message=f"hi {x}.{y} thank you for wisiting our wow site"
    emil_from=settings.EMAIL_HOST_USER
    recipient_list=[z]
    send_mail(subject,message,emil_from,recipient_list,fail_silently=False)
    return HttpResponse('request send')