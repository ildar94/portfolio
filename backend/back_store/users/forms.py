from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            # 'first_name',
            # 'last_name',
            'password',
            'email',
            # 'city',
            # 'street',
            # 'house_number',
            # 'building',
            # 'apartment',
            # 'index',
            # 'phone_number',
        )



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password',
            'email',
            'city',
            'street',
            'house_number',
            'building',
            'apartment',
            'index',
            'phone_number',
    )