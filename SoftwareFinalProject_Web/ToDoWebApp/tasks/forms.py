from django import forms
from .models import Assignment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['name', 'due_date', 'description', 'status']  # removed 'assigned_to'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
