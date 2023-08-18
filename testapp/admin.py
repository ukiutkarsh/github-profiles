from testapp.models import Repository, UserProfile
from django.contrib import admin

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Repository)