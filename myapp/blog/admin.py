from django.contrib import admin
from .models import PyBlog

# Register your models here.

@admin.register(PyBlog)
class PyblogAdmin(admin.ModelAdmin):
    list_display = ('title', 'regist_dt', 'update_dt')