from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Consorcio(models.Model):
    """Modelo para armazenar informações de consórcios"""
    TIPO_CHOICES = [
        ('IMOVEL', 'Imóvel'),
        ('AUTOMOVEL', 'Automóvel'),
        ('MOTO', 'Motocicleta'),
        ('CAMINHAO', 'Caminhão'),
        ('MAQUINAS', 'Máquinas e Equipamentos'),
        ('OUTROS', 'Outros'),
    ]
    
    STATUS_CHOICES = [
        ('ATIVO', 'Ativo'),
        ('CONTEMPLADO', 'Contemplado'),
        ('CANCELADO', 'Cancelado'),
        ('ENCERRADO', 'Encerrado'),
        ('TRANSFERIDO', 'Transferido'),
    ]
    
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='consorcios')
    administradora = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    grupo = models.CharField(max_length=50, blank=True, null=True)
    cota = models.CharField(max_length=50, blank=True, null=True)
    valor_credito = models.DecimalField(max_digits=12, decimal_places=2)
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2)
    total_parcelas = models.PositiveIntegerField()
    parcelas_pagas = models.PositiveIntegerField(default=0)
    data_adesao = models.DateField()
    data_contemplacao = models.DateField(blank=True, null=True)
    taxa_administracao = models.DecimalField(max_digits=5, decimal_places=2, help_text="Percentual")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='ATIVO')
    observacoes = models.TextField(blank=True, null=True)
    
    # Campos de controle
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    # Relacionamento com usuário que cadastrou
    cadastrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='consorcios_cadastrados')
    
    def __str__(self):
        return f"Consórcio {self.tipo} - {self.cliente.nome} - {self.administradora}"
    
    def percentual_quitado(self):
        """Retorna o percentual quitado do consórcio"""
        if self.total_parcelas > 0:
            return (self.parcelas_pagas / self.total_parcelas) * 100
        return 0
    
    class Meta:
        verbose_name = 'Consórcio'
        verbose_name_plural = 'Consórcios'
        ordering = ['-data_adesao']
