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

def multi(request):
    option = []# Initialize an empty list
    ml = []
    num=0
    choose = None
    selected_posi=None
    n=0
    a=0
    
    if request.method == 'GET':
        # Check if 'options' is in the GET parameters
        if 'options' in request.GET:
            num=1
            options = request.GET['options']
            numoptions = int(request.GET['numoptions'])
            
            option = options.split(",")  # Here, the entered names are turned into a list
            length = len(option)
            
            while n == 0:
                if numoptions > length:
                    print("Sorry, the chosen number of possibilities is higher than the total possibilities.")
                    n = 1
                else:
                    choose = random.randint(0, length - 1)
                    if option[choose] not in ml:
                        ml.append(option[choose])
                        a = a + 1
                    if a == numoptions:
                        n = 1

            selected_posi = [ml[i] for i in range(numoptions)]
            
    return render(request, 'multi_selection.html', {'option': option, 'num':num, 'multiple_option':selected_posi,})
    


def user_login(request):
    return render(request,'login.html')

def user_signup(request):
    return render(request,'signup.html')