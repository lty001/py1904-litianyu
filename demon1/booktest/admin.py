from django.contrib import admin
from .models import *

# Register your models here.

class HeroInfoInlines(admin.StackedInline):
    model = HeroInfo
    extra = 1

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')
    list_filter = ('title','pub_date')
    list_per_page = 10
    inlines = [HeroInfoInlines]


admin.site.register(BookInfo,BookInfoAdmin)

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['name','content']
    search_fields = ['name','content']

admin.site.register(HeroInfo,HeroInfoAdmin)