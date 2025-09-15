from django import forms
from .models import Cliente, Seguradora, Produto, Apolice, Pagamento, Consorcio, AdministradoraConsorcio
import re
from django.core.exceptions import ValidationError


class ClienteForm(forms.ModelForm):
    """Formulário para cadastro e edição de clientes"""
    class Meta:
        model = Cliente
<<<<<<< HEAD
        fields = ['tipo', 'nome', 'documento', 'email', 'telefone', 'endereco', 
                  'cidade', 'estado', 'cep', 'data_nascimento', 'observacoes', 'ativo']
=======
        fields = [
            'tipo', 'nome', 'documento', 'email', 'telefone', 'endereco', 
            'cidade', 'estado', 'cep', 'data_nascimento', 'observacoes', 'ativo'
        ]
>>>>>>> b372def (Alterações_Duka)
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

<<<<<<< HEAD
=======

>>>>>>> b372def (Alterações_Duka)
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

<<<<<<< HEAD
=======

>>>>>>> b372def (Alterações_Duka)
class ProdutoForm(forms.ModelForm):
    """Formulário para cadastro e edição de produtos"""
    class Meta:
        model = Produto
        fields = ['nome', 'codigo', 'categoria', 'descricao', 'seguradora', 'ativo']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 6}),
<<<<<<< HEAD
=======
            'categoria': forms.Select(attrs={'class': 'form-select'}),
>>>>>>> b372def (Alterações_Duka)
        }
        labels = {
            'nome': 'Nome do Produto',
            'codigo': 'Código (opcional)',
            'categoria': 'Categoria',
            'descricao': 'Descrição',
            'seguradora': 'Seguradora',
            'ativo': 'Produto Ativo'
        }

<<<<<<< HEAD
=======

>>>>>>> b372def (Alterações_Duka)
class ApoliceForm(forms.ModelForm):
    """Formulário para cadastro e edição de apólices"""
    class Meta:
        model = Apolice
<<<<<<< HEAD
        fields = ['numero', 'cliente', 'produto', 'data_inicio', 'data_fim', 
                  'valor_premio', 'valor_comissao', 'percentual_comissao', 
                  'status', 'observacoes']
        widgets = {
=======
        fields = [
            'numero', 'cliente', 'produto', 'seguradora', 'protocolo',
            'data_inicio', 'data_fim', 'valor_premio', 'valor_comissao',
            'percentual_comissao', 'status', 'codigo_ci', 'classificacao_bonus', 'observacoes'
        ]
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-select'}),
>>>>>>> b372def (Alterações_Duka)
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 6}),
        }
        labels = {
            'numero': 'Número da Apólice',
            'cliente': 'Cliente',
            'produto': 'Produto',
<<<<<<< HEAD
=======
            'seguradora': 'Seguradora',
            'protocolo': 'Protocolo',
>>>>>>> b372def (Alterações_Duka)
            'data_inicio': 'Data de Início',
            'data_fim': 'Data de Término',
            'valor_premio': 'Valor do Prêmio (R$)',
            'valor_comissao': 'Valor da Comissão (R$)',
            'percentual_comissao': 'Percentual de Comissão (%)',
            'status': 'Status',
<<<<<<< HEAD
            'observacoes': 'Observações'
        }

=======
            'codigo_ci': 'Código C.I',
            'classificacao_bonus': 'Classificação de Bônus',
            'observacoes': 'Observações'
        }


>>>>>>> b372def (Alterações_Duka)
class PagamentoForm(forms.ModelForm):
    """Formulário para cadastro e edição de pagamentos"""
    class Meta:
        model = Pagamento
<<<<<<< HEAD
        fields = ['apolice', 'data_vencimento', 'data_pagamento', 'valor', 
                  'forma_pagamento', 'status', 'parcela', 'total_parcelas', 'observacoes']
=======
        fields = [
            'apolice', 'data_vencimento', 'data_pagamento', 'valor', 
            'forma_pagamento', 'status', 'parcela', 'total_parcelas', 'observacoes'
        ]
>>>>>>> b372def (Alterações_Duka)
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


<<<<<<< HEAD


=======
>>>>>>> b372def (Alterações_Duka)
class ConsorcioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['administradora'].empty_label = "Selecione uma administradora..."

    class Meta:
        model = Consorcio
        fields = [
            'cliente', 'administradora', 'tipo', 'grupo', 'cota',
            'valor_credito', 'valor_parcela', 'total_parcelas', 'parcelas_pagas',
            'data_adesao', 'data_contemplacao', 'taxa_administracao',
            'status', 'observacoes'
        ]
        widgets = {
            'administradora': forms.Select(attrs={'class': 'form-select'}),
            'data_adesao': forms.DateInput(attrs={'type': 'date'}),
            'data_contemplacao': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }


<<<<<<< HEAD

=======
>>>>>>> b372def (Alterações_Duka)
def validar_cnpj(cnpj):
    # Remove tudo que não for número
    cnpj = re.sub(r'\D', '', cnpj)

    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        raise ValidationError('CNPJ inválido.')

    # Validação oficial do CNPJ
    def calcular_digito(cnpj, posicoes):
        soma = sum(int(cnpj[i]) * pos for i, pos in enumerate(posicoes))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    primeiro = calcular_digito(cnpj, [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    segundo = calcular_digito(cnpj, [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])

    if cnpj[-2:] != primeiro + segundo:
        raise ValidationError('CNPJ inválido.')

<<<<<<< HEAD
=======

>>>>>>> b372def (Alterações_Duka)
class AdministradoraConsorcioForm(forms.ModelForm):
    class Meta:
        model = AdministradoraConsorcio
        fields = ['nome', 'cnpj', 'telefone', 'email', 'endereco']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs['class'] = 'form-control'

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        validar_cnpj(cnpj)
        return cnpj
