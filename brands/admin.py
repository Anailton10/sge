from django.contrib import admin

from brands.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )
    search_fields = ('name', )
