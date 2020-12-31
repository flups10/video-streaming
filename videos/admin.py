from django.contrib import admin
from .models import Serie, Episode, SerieComments

# Register your models here.
admin.site.register(Serie)
admin.site.register(Episode)
admin.site.register(SerieComments)
