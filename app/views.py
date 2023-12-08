from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jyothi(request):
    return HttpResponse('<h1><marquee>hii naveen reddy</h1></marquee>')