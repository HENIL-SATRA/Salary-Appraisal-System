from django.contrib import admin

# Register your models here.
from.models import userInfo
from.models import userProfile

admin.site.register(userInfo)
admin.site.register(userProfile)