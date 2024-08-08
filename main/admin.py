from django.contrib import admin
from .models import Image, House

# Register House.
class ImageInline(admin.TabularInline):
    model = Image
    extra = 3

class HouseAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(House, HouseAdmin)