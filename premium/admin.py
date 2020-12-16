from django.contrib import admin
from .models import Premium, user_subscription

# Register your models here.
admin.site.register(Premium)
admin.site.register(user_subscription)
