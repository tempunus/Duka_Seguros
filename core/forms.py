from django import forms
from .models import Cliente, Seguradora, Produto, Apolice, Pagamento, Consorcio


class ClienteForm(forms.ModelForm):
    """Formulário para cadastro e edição de clientes"""
    class Meta:
        model = Cliente
        fields = ['tipo', 'nome', 'documento', 'email', 'telefone', 'endereco', 
                  'cidade', 'estado', 'cep', 'data_nascimento', 'observacoes', 'ativo']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'tipo': 'Tipo de Cliente',
            'nome': 'Nome Completo / Razão Social',
            'documento': 'CPF / CNPJ',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'endereco': 'Endereço',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'cep': 'CEP',
            'data_nascimento': 'Data de Nascimento',
            'observacoes': 'Observações',
            'ativo': 'Cliente Ativo'
        }

class SeguradoraForm(forms.ModelForm):
    """Formulário para cadastro e edição de seguradoras"""
    class Meta:
        model = Seguradora
        fields = ['nome', 'cnpj', 'codigo', 'telefone', 'email', 'site', 'ativo']
        labels = {
            'nome': 'Nome da Seguradora',
            'cnpj': 'CNPJ',
            'codigo': 'Código (opcional)',
            'telefone': 'Telefone',
            'email': 'E-mail',
            'site': 'Site',
            'ativo': 'Seguradora Ativa'
        }

class ProdutoForm(forms.ModelForm):
    """Formulário para cadastro e edição de produtos"""
    class Meta:
        model = Produto
        fields = ['nome', 'codigo', 'categoria', 'descricao', 'seguradora', 'ativo']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 6}),
        }
        labels = {
            'nome': 'Nome do Produto',
            'codigo': 'Código (opcional)',
            'categoria': 'Categoria',
            'descricao': 'Descrição',
            'seguradora': 'Seguradora',
            'ativo': 'Produto Ativo'
        }

class ApoliceForm(forms.ModelForm):
    """Formulário para cadastro e edição de apólices"""
    class Meta:
        model = Apolice
        fields = ['numero', 'cliente', 'produto', 'data_inicio', 'data_fim', 
                  'valor_premio', 'valor_comissao', 'percentual_comissao', 
                  'status', 'observacoes']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 6}),
        }
        labels = {
            'numero': 'Número da Apólice',
            'cliente': 'Cliente',
            'produto': 'Produto',
            'data_inicio': 'Data de Início',
            'data_fim': 'Data de Término',
            'valor_premio': 'Valor do Prêmio (R$)',
            'valor_comissao': 'Valor da Comissão (R$)',
            'percentual_comissao': 'Percentual de Comissão (%)',
            'status': 'Status',
            'observacoes': 'Observações'
        }

class PagamentoForm(forms.ModelForm):
    """Formulário para cadastro e edição de pagamentos"""
    class Meta:
        model = Pagamento
        fields = ['apolice', 'data_vencimento', 'data_pagamento', 'valor', 
                  'forma_pagamento', 'status', 'parcela', 'total_parcelas', 'observacoes']
        widgets = {
            'data_vencimento': forms.DateInput(attrs={'type': 'date'}),
            'data_pagamento': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'apolice': 'Apólice',
            'data_vencimento': 'Data de Vencimento',
            'data_pagamento': 'Data de Pagamento',
            'valor': 'Valor (R$)',
            'forma_pagamento': 'Forma de Pagamento',
            'status': 'Status',
            'parcela': 'Parcela',
            'total_parcelas': 'Total de Parcelas',
            'observacoes': 'Observações'
        }




class ConsorcioForm(forms.ModelForm):
    class Meta:
        model = Consorcio
        fields = [
            'cliente', 'administradora', 'tipo', 'grupo', 'cota',
            'valor_credito', 'valor_parcela', 'total_parcelas', 'parcelas_pagas',
            'data_adesao', 'data_contemplacao', 'taxa_administracao',
            'status', 'observacoes'
        ]
        widgets = {
            'data_adesao': forms.DateInput(attrs={'type': 'date'}),
            'data_contemplacao': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
