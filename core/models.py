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


<<<<<<< HEAD

class Cliente(models.Model):
    """Modelo para armazenar informações de clientes da corretora"""
=======
class Cliente(models.Model):
>>>>>>> b372def (Alterações_Duka)
    TIPO_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]
<<<<<<< HEAD
    
=======

>>>>>>> b372def (Alterações_Duka)
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
<<<<<<< HEAD
    
    # Campos de controle
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    
    # Relacionamento com usuário que cadastrou
    cadastrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='clientes_cadastrados')
    
    def __str__(self):
        return self.nome
    
=======

    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='clientes_cadastrados')

    def __str__(self):
        return self.nome

>>>>>>> b372def (Alterações_Duka)
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']


class Seguradora(models.Model):
<<<<<<< HEAD
    """Modelo para armazenar informações das seguradoras parceiras"""
=======
>>>>>>> b372def (Alterações_Duka)
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20, unique=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)
<<<<<<< HEAD
    
    # Campos de controle
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    
=======

    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

>>>>>>> b372def (Alterações_Duka)
    class Meta:
        verbose_name = 'Seguradora'
        verbose_name_plural = 'Seguradoras'
        ordering = ['nome']


class Produto(models.Model):
<<<<<<< HEAD
    """Modelo para armazenar tipos de seguros/produtos oferecidos"""
=======
>>>>>>> b372def (Alterações_Duka)
    CATEGORIA_CHOICES = [
        ('AUTO', 'Automóvel'),
        ('VIDA', 'Vida'),
        ('SAUDE', 'Saúde'),
        ('RESIDENCIAL', 'Residencial'),
        ('EMPRESARIAL', 'Empresarial'),
        ('OUTROS', 'Outros'),
    ]
<<<<<<< HEAD
    
=======

>>>>>>> b372def (Alterações_Duka)
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    descricao = models.TextField(blank=True, null=True)
    seguradora = models.ForeignKey(Seguradora, on_delete=models.CASCADE, related_name='produtos')
<<<<<<< HEAD
    
    # Campos de controle
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nome} - {self.seguradora.nome}"
    
=======

    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.seguradora.nome}"

>>>>>>> b372def (Alterações_Duka)
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['categoria', 'nome']


class Apolice(models.Model):
<<<<<<< HEAD
    """Modelo para armazenar informações das apólices de seguro"""
    STATUS_CHOICES = [
    ('PROPOSTA', 'Proposta'),
    ('APROVADA', 'Proposta Aprovada'),
    ('ATIVA', 'Ativa'),
    ('PENDENTE', 'Pendente'),
    ('CANCELADA', 'Cancelada'),
    ('VENCIDA', 'Vencida'),
    ('RENOVADA', 'Renovada'),
]

    
    numero = models.CharField(max_length=50, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='apolices')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='apolices')
=======
    STATUS_CHOICES = [
        ('ATIVO', 'Ativo'),
        ('NAO_ATIVO', 'Não Ativo'),
        ('PENDENTE', 'Pendente'),
        ('ENDOSSO', 'Endosso'),
    ]

    PRODUTOS_CHOICES = [
        ('AUTO', 'AUTO'),
        ('MOTO', 'MOTO'),
        ('RESIDENCIAL', 'RESIDENCIAL'),
        ('CONDOMINIO', 'CONDOMÍNIO'),
        ('EMPRESARIAL', 'EMPRESARIAL'),
        ('VIDA', 'VIDA'),
        ('FIANCA', 'FIANÇA'),
        ('FROTA', 'FROTA'),
        ('PORTATEIS', 'PORTÁTEIS'),
        ('VIAGEM', 'VIAGEM'),
        ('IMOBILIARIA', 'IMOBILIÁRIA'),
        ('BIKE', 'BIKE'),
        ('RESP_CIVIL', 'RESPONSABILIDADE CIVIL'),
    ]

    numero = models.CharField(max_length=50, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='apolices')
    produto = models.CharField(max_length=30, choices=PRODUTOS_CHOICES)
    seguradora = models.ForeignKey(Seguradora, on_delete=models.CASCADE, related_name='apolices') 
    protocolo = models.CharField(max_length=100, blank=True, null=True) 
>>>>>>> b372def (Alterações_Duka)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_premio = models.DecimalField(max_digits=10, decimal_places=2)
    valor_comissao = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    percentual_comissao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
<<<<<<< HEAD
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PROPOSTA')
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
=======
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDENTE')

    # 🔹 Novos campos
    codigo_ci = models.CharField("Código C.I", max_length=50, blank=True, null=True)
    classificacao_bonus = models.CharField("Classificação de Bônus", max_length=50, blank=True, null=True)

    observacoes = models.TextField(blank=True, null=True)
    
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='apolices_cadastradas')

    def __str__(self):
        return f"Apólice {self.numero} - {self.cliente.nome}"

    def dias_para_vencimento(self):
>>>>>>> b372def (Alterações_Duka)
        if self.data_fim:
            delta = self.data_fim - timezone.now().date()
            return delta.days
        return None
<<<<<<< HEAD
    
=======

>>>>>>> b372def (Alterações_Duka)
    class Meta:
        verbose_name = 'Apólice'
        verbose_name_plural = 'Apólices'
        ordering = ['-data_inicio']


class Pagamento(models.Model):
<<<<<<< HEAD
    """Modelo para armazenar informações de pagamentos das apólices"""
=======
>>>>>>> b372def (Alterações_Duka)
    FORMA_PAGAMENTO_CHOICES = [
        ('BOLETO', 'Boleto'),
        ('CARTAO', 'Cartão de Crédito'),
        ('DEBITO', 'Débito Automático'),
        ('PIX', 'PIX'),
        ('TRANSFERENCIA', 'Transferência Bancária'),
        ('DINHEIRO', 'Dinheiro'),
    ]
<<<<<<< HEAD
    
=======

>>>>>>> b372def (Alterações_Duka)
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('PAGO', 'Pago'),
        ('ATRASADO', 'Atrasado'),
        ('CANCELADO', 'Cancelado'),
    ]
<<<<<<< HEAD
    
=======

>>>>>>> b372def (Alterações_Duka)
    apolice = models.ForeignKey(Apolice, on_delete=models.CASCADE, related_name='pagamentos')
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=15, choices=FORMA_PAGAMENTO_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDENTE')
    parcela = models.PositiveSmallIntegerField(default=1)
    total_parcelas = models.PositiveSmallIntegerField(default=1)
    observacoes = models.TextField(blank=True, null=True)
<<<<<<< HEAD
    
    # Campos de controle
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Pagamento {self.parcela}/{self.total_parcelas} - Apólice {self.apolice.numero}"
    
=======

    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pagamento {self.parcela}/{self.total_parcelas} - Apólice {self.apolice.numero}"

>>>>>>> b372def (Alterações_Duka)
    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['apolice', 'data_vencimento']

<<<<<<< HEAD
    
class Consorcio(models.Model):
    """Modelo para armazenar informações de consórcios"""
=======

class Consorcio(models.Model):
>>>>>>> b372def (Alterações_Duka)
    TIPO_CHOICES = [
        ('IMOVEL', 'Imóvel'),
        ('AUTOMOVEL', 'Automóvel'),
        ('MOTO', 'Motocicleta'),
        ('CAMINHAO', 'Caminhão'),
        ('MAQUINAS', 'Máquinas e Equipamentos'),
        ('OUTROS', 'Outros'),
    ]
<<<<<<< HEAD
    
    STATUS_CHOICES = [
        ('ATIVO', 'Ativo'),
        ('CONTEMPLADO', 'Contemplado'),
        ('CANCELADO', 'Cancelado'),
        ('ENCERRADO', 'Encerrado'),
        ('TRANSFERIDO', 'Transferido'),
    ]
    
=======

    STATUS_CHOICES = [
        ('ATIVO', 'Ativo'),
        ('NAO_ATIVO', 'Não Ativo'),
        ('PENDENTE', 'Pendente'),
        ('ENDOSSO', 'Endosso'),
    ]

>>>>>>> b372def (Alterações_Duka)
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
<<<<<<< HEAD
    
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
    
=======

    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='consorcios_cadastrados')

    def __str__(self):
        return f"Consórcio {self.tipo} - {self.cliente.nome} - {self.administradora}"

    def percentual_quitado(self):
        if self.total_parcelas > 0:
            return (self.parcelas_pagas / self.total_parcelas) * 100
        return 0

>>>>>>> b372def (Alterações_Duka)
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

<<<<<<< HEAD
=======
    class Meta:
        verbose_name = 'Administradora de Consórcio'
        verbose_name_plural = 'Administradoras de Consórcios'
        ordering = ['nome']
>>>>>>> b372def (Alterações_Duka)
