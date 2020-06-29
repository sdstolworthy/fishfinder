from django.contrib import admin

from planes.models import Airplane

# Register your models here.


@admin.register(Airplane)
class PlaneAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "url", "created_at"]
