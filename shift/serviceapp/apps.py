from django.apps import AppConfig


class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'serviceapp'
    verbose_name = "Работники"

    def ready(self):
        import serviceapp.signals
