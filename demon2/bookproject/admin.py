from django.contrib import admin
from .models import *

# Register your models here.


class HeroInlines(admin.StackedInline):
    model = Hero
    extra = 1

class CountryAdmin(admin.ModelAdmin):
    list_display = ['cname']
    list_filter = ['cname']
    inlines = [HeroInlines]

class HeroAdmin(admin.ModelAdmin):
    list_display = ['hname','gender','content']
    search_fields = ['hname','content']

admin.site.register(Country,CountryAdmin)
admin.site.register(Hero,HeroAdmin)