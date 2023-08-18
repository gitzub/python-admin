from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('username을 입력해주세요.')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff=True일 필요가 있습니다.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser=True일 필요가 있습니다.')
        return self._create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(_("username"), max_length=50, validators=[username_validator], unique=True)

# ====================== 2번 =====================================
# ================================================================
# admin사이트에서 유저등록시 로그인한 id(username)에 따라 mychoicegroup 항목에 동일한 이름의 그룹 노출
# 로그인한 id(username)가 test1이면 test1그룹 / test2면 test2그룹
# id = test1 / id = test2   --->   pw = 8u8u8u8u
# ================================================================
# ========= 실패한 코드 ===========================================
    mychoicegroup = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='my choice group list', related_name='appliers_User_mychoicegroup')
# ========= 실패한 코드 ===========================================
    # mychoicegroup = models.ForeignKey(Group.objects.get(name=username), on_delete=models.SET_NULL, blank=False, null=True, verbose_name='my choice group list', related_name='appliers_User_mychoicegroup')



# ====================== 3번 ======================= #
# ================================================== #
# admin페이지에서 user등록이나 수정시 선택된 mychoicegroup가 그룹 에 함께 적용되도록 요청드립니다.
# ================================================== #
# =========== 실패한 코드 =========================== #
    # addgroup_user = User.objects.get(username="test1")
    # addgroup_group = Group.objects.get(name="test1")
    # addgroup_user.groups.add(addgroup_group)
# =========== 실패한 코드 =========================== #
    # addgroup_user = username
    # addgroup_group = Group.objects.get(name="test1")
    # addgroup_user.groups.add(addgroup_group)
# =========== 실패한 코드 =========================== #
    # mychoicegroup = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='my choice group list', related_name='appliers_User_mychoicegroup')
    # username.groups.add(mychoicegroup)







    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)
    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['mychoicegroup']

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
