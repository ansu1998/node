from django import forms
from .models import Booking, Musician

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['p_name', 'p_phone', 'p_email', 'booked_on']
        labels = {
            'p_name':'Patient Name',
            'p_phone':'Phone Number',
            'p_email':'Email',
        }

        widgets ={
            'p_name':forms.TextInput(
                attrs = {'class':'form-control',
                    'placeholder': 'Enter your First Name'}
            ),
            'p_email':forms.TextInput(
                attrs = {'class':'form-control',
                    'placeholder': 'Enter your email'}
            ),
            'booked_on':forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type':'date'}
            ),
        }

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name','last_name','instrument']

        widgets ={
            'first_name':forms.TextInput(
                attrs = {'class':'form-control',
                    'placeholder': 'Enter your First Name'}
            ),
            'last_name':forms.TextInput(
                attrs = {'class':'form-control',
                    'placeholder': 'Enter your Second Name'}
            ),
            'instrument':forms.Textarea(
                attrs = {'class':'form-control',
                    'placeholder': 'Enter your todo title'}
            ),
        }
