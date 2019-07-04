from django.contrib import admin
from .models import *

# Register your models here.


# class VoteAnswerInlines(admin.StackedInline):
#     model = VoteTitle
#     extra = 1

class VoteTitleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 10
    # inlines = [VoteAnswerInlines]


admin.site.register(VoteTitle,VoteTitleAdmin)

class VoteAnswerAdmin(admin.ModelAdmin):


    list_display = ['answer','num']
    search_fields = ['answer','num']

admin.site.register(VoteAnswer,VoteAnswerAdmin)