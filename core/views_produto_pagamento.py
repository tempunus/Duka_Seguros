from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Produto, Pagamento
from .forms import ProdutoForm, PagamentoForm

# Views para Produto
@login_required
def produto_lista(request):
    """Lista de produtos"""
    query = request.GET.get('q', '')
    if query:
        produtos_list = Produto.objects.filter(
            Q(nome__icontains=query) | 
            Q(codigo__icontains=query) |
            Q(seguradora__nome__icontains=query)
        ).order_by('nome')
    else:
        produtos_list = Produto.objects.all().order_by('nome')
    
    paginator = Paginator(produtos_list, 10)  # 10 produtos por página
    page = request.GET.get('page')
    produtos = paginator.get_page(page)
    
    return render(request, 'core/produto_lista.html', {'produtos': produtos})

@login_required
def produto_detalhe(request, pk):
    """Detalhes do produto"""
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'core/produto_detalhe.html', {'produto': produto})

@login_required
def produto_novo(request):
    """Cadastro de novo produto"""
    seguradora_id = request.GET.get('seguradora')
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('produto_lista')  # Corrigido aqui
    else:
        initial = {}
        if seguradora_id:
            try:
                from .models import Seguradora
                seguradora = Seguradora.objects.get(pk=seguradora_id)
                initial['seguradora'] = seguradora
            except Seguradora.DoesNotExist:
                pass
        
        form = ProdutoForm(initial=initial)
    
    return render(request, 'core/produto_form.html', {'form': form})


@login_required
def produto_editar(request, pk):
    """Edição de produto existente"""
    produto = get_object_or_404(Produto, pk=pk)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('produto_detalhe', pk=produto.pk)
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'core/produto_form.html', {'form': form})

@login_required
def produto_excluir(request, pk):
    """Exclusão de produto"""
    produto = get_object_or_404(Produto, pk=pk)
    
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect('produto_lista')
    
    return render(request, 'core/produto_confirmar_exclusao.html', {'produto': produto})

# Views para Pagamento
@login_required
def pagamento_lista(request):
    """Lista de pagamentos"""
    query = request.GET.get('q', '')
    if query:
        pagamentos_list = Pagamento.objects.filter(
            Q(apolice__numero__icontains=query) | 
            Q(apolice__cliente__nome__icontains=query)
        ).order_by('-data_vencimento')
    else:
        pagamentos_list = Pagamento.objects.all().order_by('-data_vencimento')
    
    paginator = Paginator(pagamentos_list, 10)  # 10 pagamentos por página
    page = request.GET.get('page')
    pagamentos = paginator.get_page(page)
    
    return render(request, 'core/pagamento_lista.html', {'pagamentos': pagamentos})

@login_required
def pagamento_detalhe(request, pk):
    """Detalhes do pagamento"""
    pagamento = get_object_or_404(Pagamento, pk=pk)
    return render(request, 'core/pagamento_detalhe.html', {'pagamento': pagamento})

@login_required
def pagamento_novo(request):
    """Cadastro de novo pagamento"""
    apolice_id = request.GET.get('apolice')
    
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            pagamento = form.save()
            messages.success(request, 'Pagamento cadastrado com sucesso!')
            return redirect('pagamento_detalhe', pk=pagamento.pk)
    else:
        initial = {}
        if apolice_id:
            try:
                from .models import Apolice
                apolice = Apolice.objects.get(pk=apolice_id)
                initial['apolice'] = apolice
            except Apolice.DoesNotExist:
                pass
        
        form = PagamentoForm(initial=initial)
    
    return render(request, 'core/pagamento_form.html', {'form': form})

@login_required
def pagamento_editar(request, pk):
    """Edição de pagamento existente"""
    pagamento = get_object_or_404(Pagamento, pk=pk)
    
    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pagamento atualizado com sucesso!')
            return redirect('pagamento_detalhe', pk=pagamento.pk)
    else:
        form = PagamentoForm(instance=pagamento)
    
    return render(request, 'core/pagamento_form.html', {'form': form})

@login_required
def pagamento_excluir(request, pk):
    """Exclusão de pagamento"""
    pagamento = get_object_or_404(Pagamento, pk=pk)
    
    if request.method == 'POST':
        pagamento.delete()
        messages.success(request, 'Pagamento excluído com sucesso!')
        return redirect('pagamento_lista')
    
    return render(request, 'core/pagamento_confirmar_exclusao.html', {'pagamento': pagamento})
