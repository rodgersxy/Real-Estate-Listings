from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Contact model
    args:
        admin.ModelAdmin
    display fields:
        id, name, listing, email, contact_date   
    """
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)