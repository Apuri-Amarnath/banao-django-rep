from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Doctor.forms import DoctorSignUpForm
from Doctor.models import DoctorProfile


# Create your views here.
def doctor_login(request):
    template = 'users/doctor/doctor_login.html'
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('doctor_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, template, {'form': form})

@login_required
def doctor_dashboard(request):
    doctor_profile = DoctorProfile.objects.get(user=request.user)
    return render(request, 'users/doctor/doctor_dashboard.html', {'doctor_profile': doctor_profile})

def doctor_signup(request):
    template = 'users/doctor/doctor_signup.html'
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctor_dashboard')  # Redirect to doctor login
    else:
        form = DoctorSignUpForm()
    return render(request, template, {'form': form})

def doctor_logout(request):
    logout(request)
    return redirect('index')