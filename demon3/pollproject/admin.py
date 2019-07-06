from django.contrib import admin
from .models import *
# Register your models here.


class ChoiceInlines(admin.StackedInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    inlines = [ChoiceInlines]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['desc','votes']
    list_filter = ['desc','votes']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)