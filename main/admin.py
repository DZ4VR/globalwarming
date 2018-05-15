from django.contrib import admin
from .models import rating
# Register your models here.

class ratingAdmin(admin.ModelAdmin):
    list_filter = ['id']

admin.site.register(rating,  ratingAdmin)
