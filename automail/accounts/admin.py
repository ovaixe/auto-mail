from django.contrib import admin
from .models import Receiver


@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'city', 'created']