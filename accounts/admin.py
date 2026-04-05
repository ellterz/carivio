from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Profile

# Register your models here.

@admin.register(Profile)
class CustomUserAdmin(UserAdmin):
    model = Profile
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'avatar')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio','avatar')}),
    )