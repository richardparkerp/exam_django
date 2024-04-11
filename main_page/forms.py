from django import forms
from .models import Doctor, Appointment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields = ['username', 'email','first_name', 'last_name', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        }

        

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'specialization': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'experience': forms.TextInput(attrs={'class':'form-control'}),
        }
    


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

        widgets = {
            'doctor': forms.Select(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'time': forms.TimeInput(attrs={'class':'form-control'}),
        }
    
