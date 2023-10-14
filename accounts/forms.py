from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import BookModel


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    # email = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'last_name' , 'email')

class BookStoreForm(forms.ModelForm):
    class Meta:
        model=BookModel
        exclude = ['first_pub' , 'last_pub']
        
        