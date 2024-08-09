from django.contrib import admin
from .models import Image, House, Category

# Register House.
class ImageInline(admin.TabularInline):
    model = Image
    extra = 3

class HouseAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(House, HouseAdmin)

# Register Category.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

admin.site.register(Category, CategoryAdmin)