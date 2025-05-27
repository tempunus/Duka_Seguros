from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import PerfilUsuario

@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        # Evita criar duplicado
        if not PerfilUsuario.objects.filter(user=instance).exists():
            PerfilUsuario.objects.create(user=instance)
