from django.contrib import admin
from votingapp.models import User,Choice

# Register your models here.

admin.site.register(User)
admin.site.register(Choice)