from django.contrib import admin
from .models import Gallery,Contact
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

admin.site.site_header="Chef's Burger Samakhusi Admin Panel"

# Register your models here.
admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.unregister(Group)

