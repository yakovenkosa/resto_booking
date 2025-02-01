from django.contrib import admin

from restaurant.models import Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
    )
    search_fields = (
        "name",
        "description",
    )
