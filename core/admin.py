from django.contrib import admin
from .models import Consorcio, AdministradoraConsorcio



admin.site.register(AdministradoraConsorcio)

@admin.register(Consorcio)
class ConsorcioAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'administradora', 'tipo', 'valor_credito', 'status', 'data_adesao')
    list_filter = ('tipo', 'status', 'administradora')
    search_fields = ('cliente__nome', 'administradora', 'grupo', 'cota')
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
        if not change:  # Se for uma nova instância
            obj.cadastrado_por = request.user
        super().save_model(request, obj, form, change)



