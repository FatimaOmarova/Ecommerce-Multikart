from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserModelAdmin(UserAdmin):
    list_display = ("first_name","last_name","username","last_login",)


# Register your models here.
admin.site.register(User , UserModelAdmin)