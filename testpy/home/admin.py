from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


# # # 정상작동 class 방식 # # #
# if문 사용을 위해 def방식(주석처리해둔 아래 코드)으로 진행했으나 error
class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
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

admin.site.register(CustomUser, MyUserAdmin)




# ================================================== #
# ================================================== #
# admin페이지에서 user 수정시
# 슈퍼유저가 아닐경우 아래 필드 권한차단 요청드립니다.
# 'is_active', 'is_staff', 'is_superuser', 'user_permissions'
# ================================================== #
# ================================================== #

# # # 에러 def 방식 # # #
# class MyUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'

# class MyUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'

# class MyUserAdmin(UserAdmin):
#     def get_fieldsets(self, request):
#         if request.user.is_superuser:
#             fieldsets = (
#             (None, {'fields': ('username', 'mychoicegroup', 'password')}),
#             (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#             )
#             add_fieldsets = (
#                 (None, {
#                     'classes': ('wide',),
#                     'fields': ('username', 'mychoicegroup', 'password1', 'password2'),
#                 }),
#             )
#             form = MyUserChangeForm
#             add_form = MyUserCreationForm
#             list_display = ('username', 'is_staff', 'mychoicegroup')
#             list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#             search_fields = ('username', 'mychoicegroup')
#             ordering = ('username',)
#         else:
#             fieldsets = (
#                 (None, {'fields': ('username', 'mychoicegroup', 'password')}),
#                 (_('Permissions'), {'fields': ('groups')}),
#             )
#             add_fieldsets = (
#                 (None, {
#                     'classes': ('wide',),
#                     'fields': ('username', 'mychoicegroup', 'password1', 'password2'),
#                 }),
#             )
#             form = MyUserChangeForm
#             add_form = MyUserCreationForm
#             list_display = ('username', 'is_staff', 'mychoicegroup')
#             list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#             search_fields = ('username', 'mychoicegroup')
#             ordering = ('username',)
#         return fieldsets, add_fieldsets, form, add_form, list_display, list_filter, search_fields, ordering

# admin.site.register(CustomUser, MyUserAdmin)
