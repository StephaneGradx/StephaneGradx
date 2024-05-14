from django.contrib import admin

from accounts.models import Login, Signup

# Register your models here.
admin.site.register(Signup)
admin.site.register(Login)