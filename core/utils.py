from .models import Atividade

def registrar_atividade(usuario, descricao):
    """Cria um registro de atividade para o usuário logado."""
    if usuario.is_authenticated:
        Atividade.objects.create(usuario=usuario, descricao=descricao)
