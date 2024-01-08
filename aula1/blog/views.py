from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    print('Blog')
    return HttpResponse('Blog')
