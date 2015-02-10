from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

admin.site.register(UserProfile)

# Register your models here.

from django.contrib import admin
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)

