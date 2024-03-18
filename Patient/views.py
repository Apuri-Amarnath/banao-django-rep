from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from Patient.forms import PatientSignUpForm
from Patient.models import PatientProfile


# Create your views here.
def patient_signup(request):
    template = 'users/patient/patient_signup.html'
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patient_dashboard')
    else:
        form = PatientSignUpForm()
    return render(request, template, {'form': form})


@login_required
def patient_dashboard(request):
    patient_profile = PatientProfile.objects.get(user=request.user)
    return render(request, 'users/patient/patient_dashboard.html',{'patient_profile': patient_profile})


def patient_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('patient_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/patient/patient_login.html', {'form': form})
def patient_logout(request):
        logout(request)
        return redirect('index')