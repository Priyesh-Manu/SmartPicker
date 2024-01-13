from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
import random
# Create your views here.

from django.http import HttpResponse

# Problem 1: SmartPicker Functionality

def home(request):
    option = []  # Initialize an empty list to store options
    num = 0  # Flag to check if options are present and to control template rendering
    choose = None  # Randomly chosen index from the options list
    pick = None  # The selected option

    # Check if the request method is GET
    if request.method == 'GET':
        # Check if 'options' is in the GET parameters
        if 'options' in request.GET:
            num = 1  # Set to 1 to indicate that options are present and template rendering is needed
            options = request.GET['options']
            option = options.split(",")  # Convert entered names into a list
            length = len(option)
            choose = random.randint(0, length - 1)
            pick = option[choose]  # Select a random option from the list
            
            
    # Render the 'index.html' template with the data
    return render(request, 'index.html',  {'option': option, 'num': num, 'ch': pick,})


# Problem 2: Multi-Selection Functionality

def multi(request):
    option = []  # Initialize an empty list
    ml = []  # List to store selected options
    num = 0  # Flag to check if options are present and to control template rendering
    choose = None
    selected_posi = None
    n = 0  # Flag to control the while loop
    a = 0  # Counter for the number of selected options
    msg = None  # Message for error handling
    # Check if the request method is GET
    if request.method == 'GET':
        # Check if 'options' and 'numoptions' are in the GET parameters
        if 'options' in request.GET:
            num = 1  # Set to 1 to indicate that options are present and template rendering is needed
            options = request.GET['options']
            numoptions = int(request.GET['numoptions'])

            option = options.split(",")  # Convert entered names into a list
            length = len(option)

            while n == 0:
                # Check if the chosen number of possibilities is higher than the total possibilities
                if numoptions > length:
                    msg = "Invalid selection: Too many options chosen."
                    n = 1
                else:
                    choose = random.randint(0, length - 1)
                    # Check if the selected option is not already in the list
                    if option[choose] not in ml:
                        ml.append(option[choose])
                        a = a + 1
                    if a == numoptions:
                        n = 1  # Exit the while loop when the required number of options are selected
            if numoptions < length:
                selected_posi = [ml[i] for i in range(numoptions)]

    # Render the 'multi_selection.html' template with the data
    return render(request, 'multi_selection.html', {'option': option, 'num': num, 'multiple_option': selected_posi, 'message': msg,})
    

# Function for user signup
def user_signup(request):
    if request.method == 'POST':
        # Get user input from the form
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        create_password = request.POST['crpassword']
        conform_password = request.POST['cnpassword']
        
        # Check if passwords match
        if create_password == conform_password:
            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            else:
                # Create a new user and save to the database
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=create_password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords didn\'t match')
            return redirect('signup')
    return render(request, 'signup.html')

# Function for user login
def user_login(request):
    if request.method == 'POST':
        # Get user input from the login form
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is authenticated, log them in and redirect to home
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')

# Function for user logout
def user_logout(request):
    # Logout the user and redirect to home
    logout(request)
    return redirect('home')

# Function for contact

def contact(request):
    return render(request,'contact.html')
