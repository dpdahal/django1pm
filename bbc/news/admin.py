from django.contrib import admin

from .models import *


# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['cat_name']


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug', 'description', 'cat_id']
    search_fields = ['title', 'cat_id']


@admin.register(CompanySetting)
class AdminSetting(admin.ModelAdmin):
    pass


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['email','subject','message']