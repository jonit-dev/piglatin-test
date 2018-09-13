# set HTTP response

from django.http import HttpResponse
from django.shortcuts import render

from pigLatin.functions.translator import translatePhrase


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def translate(request):
    return render(request, 'translate.html', {'translated': translatePhrase(request.GET['keywords'])})
