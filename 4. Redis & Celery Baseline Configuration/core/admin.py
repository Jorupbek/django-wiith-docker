from django.contrib import admin
from core.models import Test

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
