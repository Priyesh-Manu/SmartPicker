from django.shortcuts import render
import random
# Create your views here.

from django.http import HttpResponse

def home(request):
    option = []  # Initialize an empty list
    num=0
    choose = None
    pick = None
    if request.method == 'GET':
        # Check if 'options' is in the GET parameters
        if 'options' in request.GET:
            num=1
            options = request.GET['options']
            option = options.split(",")  # Here, the entered names are turned into a list
            length = len(option)
            choose = random.randint(0, length - 1)
            pick=option[choose]
    return render(request, 'index.html', {'option': option, 'num':num, 'ch':pick,})
