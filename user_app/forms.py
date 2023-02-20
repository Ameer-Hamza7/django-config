from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'password1', 'password2', 'email', 'groups'
        ]


class CreateGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        # fields = ['name']
