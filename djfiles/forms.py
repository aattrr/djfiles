from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import Profile, News
from django.contrib.auth.forms import UserChangeForm


class RegisterForm(UserCreationForm):
    tel = forms.CharField(required=False)
    town = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    second_name = forms.CharField(required=False)
    about_me = forms.CharField(widget=forms.Textarea, required=False)
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'second_name', 'about_me', 'tel', 'town', 'avatar', 'password1', 'password2')


class ChangeUserForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangeUserForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'second_name', 'about_me', 'tel', 'town')


class UploadFileForm(forms.Form):
    file = forms.FileField()
