from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Username",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username',
        })
    )
    password1 = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
        })
    )
    password2 = forms.CharField(
        required=True,
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password',
        })
    )
    bio = forms.CharField(
        required=False,
        label="Bio",
        widget=forms.Textarea(attrs={
            'placeholder': 'Tell us something about yourself (optional)',
        })
    )
    class Meta:
        model = Profile
        fields = ['username', 'password1', 'password2', 'bio']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Username",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username',
        })
    )
    password = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
        })
    )

class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Username",
        widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
        })
    )
    email = forms.EmailField(
        required=False,
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your email address',
        })
    )
    bio = forms.CharField(
        required=False,
        label="Bio",
        widget=forms.Textarea(attrs={
            'placeholder': 'Tell us something about yourself',
        })
    )

    class Meta:
        model = Profile
        fields = ['username', 'email', 'bio', 'avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled = True