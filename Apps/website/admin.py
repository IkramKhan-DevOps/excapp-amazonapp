from django.contrib import admin
from .models import (
    ProductImage, ProductBrand, ProductCategory, Product, ProductTag
)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'product', 'is_active', 'created_on']
    list_filter = ['is_active']


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'retail_price', 'sale_price', 'category', 'brand', 'is_active', 'created_on']
    list_filter = ['is_active', 'category', 'brand']
    fieldsets = (
        (None, {'fields': ('image', 'name', 'description')}),
        ('Details', {'fields': ('retail_price', 'sale_price', 'category', 'brand')}),
        ('Detailed Description', {'fields': ('detailed_description',)}),
        ('Status', {
            'fields': ('is_active',),
        }),
    )


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductBrand, ProductBrandAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductTag, ProductTagAdmin)
