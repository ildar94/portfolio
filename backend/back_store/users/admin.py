from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    fieldsets = (
        (None, {'fields': (
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
            'phone_number'
        )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'first_name',
                'last_name',
                #'password',
                'password1',
                'password2',
                'email',
                'city',
                'street',
                'house_number',
                'building',
                'apartment',
                'index',
                'phone_number',
                'is_staff',
                'is_active')}
         ),
    )
    list_display = ('username', 'email', 'first_name', 'last_name',)
    list_filter = ('email',)
    search_fields = ('email', 'first_name', 'last_name',)


admin.site.register(User, UserAdmin)