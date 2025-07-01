# auth_app/admin.py

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Unregister the original
admin.site.unregister(User)

# Register again (optionally with your custom UserAdmin subclass)
admin.site.register(User, UserAdmin)
