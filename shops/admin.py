from django.contrib import admin
from django.utils.safestring import mark_safe

from shops.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_show', 'price', 'availability', 'created', 'uploaded']
    list_filter = ['availability', 'created', 'uploaded']
    list_editable = ['price', 'availability']

    def image_show(self, obj):
        if obj.img:
            return mark_safe("<img src='{}' width='60' />".format(obj.img.url))
        return "None"

    image_show.__name__ = "Картинка"
