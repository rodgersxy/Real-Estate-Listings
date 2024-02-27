from django.apps import AppConfig


class ContactsConfig(AppConfig):
    """
    Custom admin configuration for the Contact model
    args:
        AppConfig
    display fields:
        id, name, listing, email, contact_date
    """
    name = 'contacts'
