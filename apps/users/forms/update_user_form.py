from django import forms
from ..models import User, Group
from django.core import validators
from graphene_file_upload.scalars import Upload


class UpdateUserForm(forms.ModelForm):
    password = forms.CharField(required=True)
    email = forms.CharField(required=True, validators=[
                            validators.validate_email])
    first_name = forms.CharField()
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all())
    country = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    lenguage = forms.CharField(required=True)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('password', 'email', 'first_name',
                  'groups', 'country', 'lenguage', 'phone')

    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user
