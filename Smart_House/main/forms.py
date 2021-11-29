from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Textarea
from .models import Controls, Items


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ControlForm(ModelForm):
    class Meta:
        model = Controls
        fields = ['name_controller', 'has_item']

        widgets = {
            "name_controller": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип предмету керування'
            }),
            "has_item": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кількість предметів'
            })
        }


class ItemsForm(ModelForm):
    class Meta:
        model = Items
        fields = ["name", "title", "controller"]

        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Засіб використання"
            }),
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Короткий опис"
            }),
            "controller": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Виберіть пристрій керування"
            })
        }