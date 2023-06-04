from django.contrib import admin
from serviceapp.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'date_up', 'salary')
    list_display_links = ('login',)
    search_fields = ('login',)
    list_filter = ('date_up', 'salary')

admin.site.register(Person, PersonAdmin)