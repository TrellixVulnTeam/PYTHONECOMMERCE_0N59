from django.contrib import admin

# Register your models here.

from accounts.models import GuestEmail

admin.site.register(GuestEmail)