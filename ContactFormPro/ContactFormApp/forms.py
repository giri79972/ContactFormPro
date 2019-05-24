__author__ = 'Giri'
from django import forms

class ContactForm(forms.Form):
    first_name=forms.CharField(label="Enter First Name",widget=forms.TextInput(attrs={'class':'form_control','placeholder':'First Name'}))
    last_name=forms.CharField(label="Enter Last Name",widget=forms.TextInput(attrs={'class':'form_control','placeholder':'Last Name'}))
    email=forms.EmailField(label='Enter Your Email',widget=forms.EmailInput(attrs={'class':'form_control','placeholder':'Your Email'}))
    loc=forms.CharField(label="Enter Your Location",widget=forms.TextInput(attrs={'class':'form_control','placeholder':'Your Location'}))
    number=forms.IntegerField(label='Enter Your Number',widget=forms.NumberInput(attrs={'class':'form_control','placeholder':'Your Number'}))
    sal=forms.IntegerField(label='Enter Your Salary',widget=forms.NumberInput(attrs={'class':'form_control','placeholder':'Your Salary'}))
