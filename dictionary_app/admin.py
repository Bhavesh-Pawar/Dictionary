from django.contrib import admin

# Register your models here.

from dictionary_app.models import *

class WordCountAdmin(admin.ModelAdmin):
    list_display = ['word','count']

admin.site.register(WordCount,WordCountAdmin)