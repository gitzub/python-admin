from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'mychoicegroup')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'mychoicegroup', 'password1', 'password2'),
            }),
        )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('username', 'mychoicegroup', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'mychoicegroup')
    search_fields = ('username', 'mychoicegroup')
    ordering = ('username',)

admin.site.register(User, MyUserAdmin)





