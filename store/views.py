from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import items

# Create your views here.
def index(request):

    try:
        deals1 = items.objects.all()[:3]
        deals2 = items.objects.all()[3:6]
    except items.DoesNotExist:
        deals1 = None
        deals2 = None

    context = {
        'deals1' : deals1,
        'deals2' : deals2
    }

    print(context)

    return render(request, 'store/landing.html', context)