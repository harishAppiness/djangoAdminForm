from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html
from .models import ApplicationSettings


# Register your models here.
# admin.site.site_header = 'Admin Settings Dashboard'

# class ApplicationSettingsAdmin(admin.ModelAdmin):
#     list_display = ('id','module','setting_name','setting_value','edit_item','delete_item')
#     list_filter = ('created','modified')

#     def edit_item(self, obj):
#         return format_html(f'<form action="http://127.0.0.1:8000/admin/settings/applicationsettings/{obj.id}/change/"><input type="submit" value="edit" /></form>')
#     def delete_item(self, obj):
#         return format_html(f'<form action="http://127.0.0.1:8000/admin/settings/applicationsettings/{obj.id}/delete/"><input type="submit" value="delete" /></form>')

admin.site.register(ApplicationSettings)
# admin.site.register(ApplicationSettingsAdmin)
# admin.site.unregister(Group)


