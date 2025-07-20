from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'email', 'phone', 'created_date',
    ordering = '-id',
    #list_filter = 'first_name', 'last_name', 'email',
    search_fields = 'first_name', 'last_name', 'email', 'phone',
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'email', 'phone'
    list_display_links = 'id', 'first_name', 'last_name'
    
 

