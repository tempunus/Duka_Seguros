# filters.py
import django_filters
from django import forms
from .models import Apolice

class ApoliceFilter(django_filters.FilterSet):
    data_inicio__gte = django_filters.DateFilter(
        field_name='data_inicio',
        lookup_expr='gte',
        label='Início após',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    data_inicio__lte = django_filters.DateFilter(
        field_name='data_inicio',
        lookup_expr='lte',
        label='Início antes',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Apolice
        fields = []
