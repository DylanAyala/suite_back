from django import forms
from ..models_all.user import User
from django.core import validators


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    email = forms.CharField(required=True, validators=[validators.validate_email])
    phone = forms.CharField(required=False)
    is_active = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'phone', 'is_active')

    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user