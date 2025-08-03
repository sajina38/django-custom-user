from django.contrib import admin
from .models import Product
from unfold.admin import ModelAdmin
# Register your models here.

class ProductAdmin(ModelAdmin):
    list_display = ("id", "name", "price", "created_at", "release_date")
    search_fields = ("name", "description")
    list_filter = ("created_at", "updated_at", "price")
    date_hierarchy = "release_date"
    ordering = ("-created_at",)
    list_editable = (
        "name",
        "price",
    )
    list_per_page = 2
    # fields = ('name', 'description', 'price', 'release_date', 'created_at', 'updated_at')
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("name", "description", "price")}),
        ("Release Information", {"fields": ("release_date",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

admin.site.register(Product, ProductAdmin)