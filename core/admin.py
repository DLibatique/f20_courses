from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from core.models import UserCourse

# Register your models here.
admin.site.register(UserCourse)

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = True
#     verbose_name_plural = "students"
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline,)
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
