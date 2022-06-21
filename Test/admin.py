from django.contrib import admin
from .models import Strings

class Admin(admin.ModelAdmin):
    list_display=('Master_String','String1','String2','String3','String4')

# Register your models here.

admin.site.register(Strings,Admin)