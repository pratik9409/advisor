from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import advisor


def add_advisor(request):
    try:
        advisor_name = request.POST['name']
        advisor_photo_url = request.POST['url']
        here = Advisor(name=advisor_name, url=advisor_photo_url)
        here.save()
        # print(Advisor.objects.all().count())
        # Advisor.objects.all().delete()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=400)

def truncate_tables(request):
    try:
        User.objects.all().delete()
        Advisor.objects.all().delete()
        Booking.objects.all().delete()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=400)


