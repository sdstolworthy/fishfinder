from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from planes.models import Airplane

# Register your models here.


class PriceFilter(SimpleListFilter):
    title = "Max Price"
    parameter_name = "price"

    def lookups(self, request, model_admin):
        base_price = 20000
        interval = 5000

        def get_price(price):
            return base_price + price * interval

        return [(get_price(x), "${}".format(get_price(x))) for x in range(6)]

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.distinct().filter(price__lte=self.value())


@admin.register(Airplane)
class PlaneAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "url", "created_at"]
    search_fields = (
        "title",
        "description",
    )
    list_filter = [PriceFilter]

