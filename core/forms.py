from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from registration.forms import RegistrationForm

from core.models import UserProfile


class CustomUserCreationForm(RegistrationForm):
    email = forms.EmailField(required=True)

    class Meta(RegistrationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"].lower()
        if commit:
            user.save()
        return user


class AccountProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'bio', 'birth_date']
