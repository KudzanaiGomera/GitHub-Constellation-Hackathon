from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

from django.forms.widgets import PasswordInput, TextInput

User = get_user_model()

class UserRegister(UserCreationForm):
	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name','email', 'account_type', 'password1','password2']


class UserLogin(AuthenticationForm):
	username = forms.CharField(widget=TextInput())
	password = forms.CharField(widget=PasswordInput())
