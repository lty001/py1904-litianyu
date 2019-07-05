from django.contrib import admin
from .models import *

# Register your models here.


# class ChoiceInlines(admin.StackedInline):
#     model = Question
#     extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('desc',)
    list_filter = ('desc',)
    list_per_page = 10
    # inlines = [ChoiceInlines]


admin.site.register(Question,QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):


    list_display = ['desc','votes']
    search_fields = ['desc','votes']

admin.site.register(Choice,ChoiceAdmin)