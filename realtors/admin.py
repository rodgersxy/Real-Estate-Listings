# Import necessary modules from Django
from django.contrib import admin

# Import the 'Realtor' model from the same directory  models.py file)
from .models import Realtor

# Create a custom admin class for the 'Realtor' model
class RealtorAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the list view of the admin panel
    list_display = ('id', 'name', 'email', 'hire_date')

    # Make the 'id' and 'name' fields clickable to view the individual record
    list_display_links = ('id', 'name')

    # Enable searching by the 'name' field in the admin panel
    search_fields = ('name',)

    # Set the number of items displayed per page in the admin panel list view
    list_per_page = 25

# Register the 'Realtor' model with the custom admin class
admin.site.register(Realtor, RealtorAdmin)
