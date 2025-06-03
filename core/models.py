from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms


class Atividade(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.descricao} ({self.data_hora})"



class Cliente(models.Model):
    """Modelo para armazenar informações de clientes da corretora"""
    TIPO_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]
    
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, default='PF')
    nome = models.CharField(max_length=200)
    documento = models.CharField(max_length=20, unique=True, help_text="CPF ou CNPJ")
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    
    # Campos de controle
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    
    # Relacionamento com usuário que cadastrou
    cadastrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='clientes_cadastrados')
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']


class Seguradora(models.Model):
    """Modelo para armazenar informações das seguradoras parceiras"""
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20, unique=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)
    
    # Campos de controle
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Seguradora'
        verbose_name_plural = 'Seguradoras'
        ordering = ['nome']


class Produto(models.Model):
    """Modelo para armazenar tipos de seguros/produtos oferecidos"""
    CATEGORIA_CHOICES = [
        ('AUTO', 'Automóvel'),
        ('VIDA', 'Vida'),
        ('SAUDE', 'Saúde'),
        ('RESIDENCIAL', 'Residencial'),
        ('EMPRESARIAL', 'Empresarial'),
        ('OUTROS', 'Outros'),
    ]
    
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    descricao = models.TextField(blank=True, null=True)
    seguradora = models.ForeignKey(Seguradora, on_delete=models.CASCADE, related_name='produtos')
    
    # Campos de controle
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nome} - {self.seguradora.nome}"
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['categoria', 'nome']


class Apolice(models.Model):
    """Modelo para armazenar informações das apólices de seguro"""
    STATUS_CHOICES = [
        ('ATIVA', 'Ativa'),
        ('PENDENTE', 'Pendente'),
        ('CANCELADA', 'Cancelada'),
        ('VENCIDA', 'Vencida'),
        ('RENOVADA', 'Renovada'),
    ]
    
    numero = models.CharField(max_length=50, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='apolices')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='apolices')
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_premio = models.DecimalField(max_digits=10, decimal_places=2)
    valor_comissao = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    percentual_comissao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ATIVA')
    observacoes = models.TextField(blank=True, null=True)
    
    # Campos de controle
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    # Relacionamento com usuário que cadastrou
    cadastrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='apolices_cadastradas')
    
    def __str__(self):
        return f"Apólice {self.numero} - {self.cliente.nome}"
    
    def dias_para_vencimento(self):
        """Retorna o número de dias até o vencimento da apólice"""
        if self.data_fim:
            delta = self.data_fim - timezone.now().date()
            return delta.days
        return None
    
    class Meta:
        verbose_name = 'Apólice'
        verbose_name_plural = 'Apólices'
        ordering = ['-data_inicio']


class Pagamento(models.Model):
    """Modelo para armazenar informações de pagamentos das apólices"""
    FORMA_PAGAMENTO_CHOICES = [
        ('BOLETO', 'Boleto'),
        ('CARTAO', 'Cartão de Crédito'),
        ('DEBITO', 'Débito Automático'),
        ('PIX', 'PIX'),
        ('TRANSFERENCIA', 'Transferência Bancária'),
        ('DINHEIRO', 'Dinheiro'),
    ]
    
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('PAGO', 'Pago'),
        ('ATRASADO', 'Atrasado'),
        ('CANCELADO', 'Cancelado'),
    ]
    
    apolice = models.ForeignKey(Apolice, on_delete=models.CASCADE, related_name='pagamentos')
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=15, choices=FORMA_PAGAMENTO_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDENTE')
    parcela = models.PositiveSmallIntegerField(default=1)
    total_parcelas = models.PositiveSmallIntegerField(default=1)
    observacoes = models.TextField(blank=True, null=True)
    
    # Campos de controle
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Pagamento {self.parcela}/{self.total_parcelas} - Apólice {self.apolice.numero}"
    
    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['apolice', 'data_vencimento']





    
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
    administradora = models.ForeignKey('AdministradoraConsorcio', on_delete=models.CASCADE)
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


class AdministradoraConsorcio(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome

