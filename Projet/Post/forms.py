from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book




class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['pdf']

class UploadFileForm(forms.Form):
    #file = forms.FileField()
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
