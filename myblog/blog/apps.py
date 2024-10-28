from django.apps import AppConfig


class BlogConfig(AppConfig):
    '''
    Configuration class for the Blog application.

    Attributes:
        default_auto_field (str): The default field type for auto-generated primary keys.
        name (str): The name of the application.
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
