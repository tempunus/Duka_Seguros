from django.contrib import admin
from .models import Cliente, Seguradora, Produto, Apolice, Pagamento, Consorcio, AdministradoraConsorcio


# ----------------------------
# Cliente
# ----------------------------
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'documento', 'email', 'telefone', 'ativo')
    list_filter = ('tipo', 'ativo')
    search_fields = ('nome', 'documento', 'email', 'telefone')
    readonly_fields = ('data_cadastro', 'data_atualizacao')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('tipo', 'nome', 'documento', 'email', 'telefone')
        }),
        ('Endereço', {
            'fields': ('endereco', 'cidade', 'estado', 'cep')
        }),
        ('Outras Informações', {
            'fields': ('data_nascimento', 'observacoes', 'ativo', 'cadastrado_por')
        }),
        ('Controle', {
            'fields': ('data_cadastro', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cadastrado_por = request.user
        super().save_model(request, obj, form, change)


# ----------------------------
# Seguradora
# ----------------------------
@admin.register(Seguradora)
class SeguradoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'codigo', 'ativo')
    search_fields = ('nome', 'cnpj', 'codigo')
    readonly_fields = ('data_cadastro', 'data_atualizacao')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'cnpj', 'codigo', 'telefone', 'email', 'site', 'ativo')
        }),
        ('Controle', {
            'fields': ('data_cadastro', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )


# ----------------------------
# Produto
# ----------------------------
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'seguradora', 'ativo')
    list_filter = ('categoria', 'ativo', 'seguradora')
    search_fields = ('nome', 'codigo', 'seguradora__nome')
    readonly_fields = ('data_cadastro', 'data_atualizacao')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'codigo', 'categoria', 'descricao', 'seguradora', 'ativo')
        }),
        ('Controle', {
            'fields': ('data_cadastro', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )


# ----------------------------
# Apólice
# ----------------------------
@admin.register(Apolice)
class ApoliceAdmin(admin.ModelAdmin):
    list_display = ('numero', 'cliente', 'produto', 'seguradora', 'status', 'data_inicio', 'data_fim')
    list_filter = ('status', 'produto', 'seguradora')
    search_fields = ('numero', 'cliente__nome', 'protocolo', 'codigo_ci')
    readonly_fields = ('data_cadastro', 'data_atualizacao')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('numero', 'cliente', 'produto', 'seguradora', 'protocolo', 'codigo_ci', 'classificacao_bonus', 'status')
        }),
        ('Valores', {
            'fields': ('valor_premio', 'valor_comissao', 'percentual_comissao')
        }),
        ('Período', {
            'fields': ('data_inicio', 'data_fim')
        }),
        ('Observações', {
            'fields': ('observacoes',)
        }),
        ('Controle', {
            'fields': ('cadastrado_por', 'data_cadastro', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cadastrado_por = request.user
        super().save_model(request, obj, form, change)


# ----------------------------
# Pagamento
# ----------------------------
@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('apolice', 'parcela', 'total_parcelas', 'valor', 'status', 'data_vencimento', 'data_pagamento')
    list_filter = ('status', 'forma_pagamento')
    search_fields = ('apolice__numero',)
    readonly_fields = ('data_cadastro', 'data_atualizacao')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('apolice', 'parcela', 'total_parcelas', 'valor', 'forma_pagamento', 'status')
        }),
        ('Datas', {
            'fields': ('data_vencimento', 'data_pagamento')
        }),
        ('Observações', {
            'fields': ('observacoes',)
        }),
        ('Controle', {
            'fields': ('data_cadastro', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )


# ----------------------------
# Consórcio
# ----------------------------
@admin.register(Consorcio)
class ConsorcioAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'administradora', 'tipo', 'valor_credito', 'status', 'data_adesao')
    list_filter = ('tipo', 'status', 'administradora')
    search_fields = ('cliente__nome', 'administradora__nome', 'grupo', 'cota')
    date_hierarchy = 'data_adesao'
    readonly_fields = ('data_cadastro', 'data_atualizacao')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('cliente', 'administradora', 'tipo', 'status')
        }),
        ('Detalhes do Consórcio', {
            'fields': ('grupo', 'cota', 'valor_credito', 'valor_parcela', 'total_parcelas', 'parcelas_pagas')
        }),
        ('Datas', {
            'fields': ('data_adesao', 'data_contemplacao')
        }),
        ('Informações Adicionais', {
            'fields': ('taxa_administracao', 'observacoes', 'cadastrado_por')
        }),
        ('Controle', {
            'fields': ('data_cadastro', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cadastrado_por = request.user
        super().save_model(request, obj, form, change)


# ----------------------------
# Administradora de Consórcio
# ----------------------------
@admin.register(AdministradoraConsorcio)
class AdministradoraConsorcioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone', 'email')
    search_fields = ('nome', 'cnpj')
    readonly_fields = ()
