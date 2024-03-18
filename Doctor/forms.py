from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import DoctorProfile

class DoctorSignUpForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=10)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        profile = DoctorProfile.objects.create(user=user, address_line1=self.cleaned_data['address_line1'], city=self.cleaned_data['city'], state=self.cleaned_data['state'], pincode=self.cleaned_data['pincode'])
        if self.cleaned_data['profile_picture']:
            profile.profile_picture = self.cleaned_data['profile_picture']
        profile.save()
        return user