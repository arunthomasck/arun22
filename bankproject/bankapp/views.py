from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def demo1(request):
    return render(request, "index.html")
def demo2(request):
    return render(request, "single.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('demo2')  # Redirect to the desired URL after login
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')  # Redirect back to the login page with an error message

    return render(request, "login.html")  # Update the template name

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return redirect("register")  # Redirect back to the registration page with an error message
            else:
                # Create a new user
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "User created successfully")
                return redirect('login')  # Redirect to the login page after successful registration
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')  # Redirect back to the registration page with an error message

    return render(request,'register.html')  # Update the template name

def logout(request):
    auth.logout(request)
    return redirect('/')  # Redirect to the desired URL after logout

def details(request):
    if request.method == 'POST':
        full_name = request.POST['Name']
        date_of_birth = request.POST['DateOfBirth']
        age = request.POST['Age']
        gender = request.POST['Gender']
        phone_number = request.POST['PhoneNumber']
        email_id = request.POST['EmailID']

        # Process the data and save it as needed

        messages.success(request, "User details saved successfully")
        return redirect('/')  # Redirect to the desired URL after form submission

    return render(request, 'details.html')  # Update the template name
