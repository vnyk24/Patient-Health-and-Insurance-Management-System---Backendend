from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def health_check(request):
    return JsonResponse({'status':'healthy'})

def authentication(request):
    pass
