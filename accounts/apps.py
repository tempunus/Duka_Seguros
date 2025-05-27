from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Ou AutoField se for necessário
    name = 'accounts'

    def ready(self):
        import accounts.signals
