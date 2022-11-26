from datetime import date, timedelta
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser, Appointment

class DateInput(forms.DateInput):
    input_type = 'date'

class MyRegForm(UserCreationForm):
    username=forms.CharField(label="Enter user name*", widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your user name',
            'style': 'height: 55px'
        }))
    first_name = forms.CharField(label="Enter first name*", widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your first name',
            'style': 'height: 55px'
        }))
    last_name = forms.CharField(label="Enter last name*", widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your last name',
            'style': 'height: 55px'
        }))
    email = forms.CharField(label="Enter email-id*", widget=forms.EmailInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your email-id',
            'style': 'height: 55px'
        }))
    mobile = forms.CharField(label="Enter first name*", widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your contact number',
            'style': 'height: 55px'
        }))
    age = forms.CharField(label="Enter your age*", widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your age',
            'style': 'height: 55px'
        }))
    gender = forms.CharField(label="Enter your age*", widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your gender',
            'style': 'height: 55px'
        }))
    password1 = forms.CharField(label="Enter your password*", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your password',
            'style': 'height: 55px'
        }))
    password2 = forms.CharField(label="Enter your confirm password*", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your confirm password',
            'style': 'height: 55px'
        }))
    class Meta:
        model = CustomUser
        fields=['username', 'first_name', 'last_name', 'email', 'mobile', 'age', 'gender']


class MyLoginFrm(AuthenticationForm):
    username=forms.CharField(label="Enter user name*", widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your user name',
            'style': 'height: 55px'
        }))
    password = forms.CharField(label="Enter your confirm password*", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your confirm password',
            'style': 'height: 55px'
        }))

class ChangeProfileFrm(UserChangeForm):
    password=None
    username=None
    first_name = forms.CharField(label="Enter first name*", widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your first name',
            'style': 'height: 55px'
        }))
    last_name = forms.CharField(label="Enter last name*", widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your last name',
            'style': 'height: 55px'
        }))
    email = forms.CharField(label="Enter email-id*", widget=forms.EmailInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your email-id',
            'style': 'height: 55px'
        }))
    mobile = forms.CharField(label="Enter first name*", widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your contact number',
            'style': 'height: 55px'
        }))
    age = forms.CharField(label="Enter your age*", widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your age',
            'style': 'height: 55px'
        }))
    gender = forms.CharField(label="Enter your age*", widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Enter your gender',
            'style': 'height: 55px'
        }))
    class Meta:
        model = CustomUser
        fields=['first_name', 'last_name', 'email', 'mobile', 'age', 'gender']

class AppointmentForm(forms.ModelForm):
    appdate=forms.DateField(label="Select Appointment date*",
            widget=DateInput(attrs={
            'class': 'form-control bg-light border-0',
            'placeholder': 'Select Appointment date',
            'style': 'height: 55px'
        }))
    def clean_appdate(self):
        ad = self.cleaned_data['appdate']
        td=date.today()
        fd=date.today() + timedelta(days=30)
        if ad==td:
            raise forms.ValidationError('Selected date may not be today')
        elif ad < td:
            raise forms.ValidationError('Selected date may not be previous date')
        elif ad > fd:
            raise forms.ValidationError('Selected date must be within 30 days from current date')
        return ad
    class Meta:
        model = Appointment
        fields = ['appdate']
    

