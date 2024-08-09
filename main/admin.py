from django.contrib import admin
from .models import Image, House, Category

# Register House.
class ImageInline(admin.TabularInline):
    model = Image
    extra = 3

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'location', 'category']
    list_filter = ['category']
    inlines = [ImageInline]


# Register Category.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}