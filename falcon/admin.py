from django.contrib import admin

# Register your models here.
import inspect

from falcon import models

for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj):
        admin.site.register(obj)


# TODO: Figure out why the Wordfilter is crashing so I can display it properly.
# from falcon.models import Wordfilter

# class WordfilterAdmin(admin.ModelAdmin):
#     list_display = Wordfilter._meta.fields
#
#
# admin.site.register(Wordfilter, WordfilterAdmin)

