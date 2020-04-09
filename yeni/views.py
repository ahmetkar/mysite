from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Tablo1
def index(request):
  latest_list = Tablo1.objects.order_by('-date')
  output = [str(it.sayi) for it in latest_list]
  return HttpResponse("Tablo1 deki sayılar : <br> "+str(output)) 
  