from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Cliente, Seguradora, Produto, Apolice, Pagamento, Consorcio, AdministradoraConsorcio, Atividade
from .forms import ClienteForm, SeguradoraForm, ProdutoForm, ApoliceForm, PagamentoForm, ConsorcioForm, AdministradoraConsorcioForm
from .filters import ApoliceFilter

# -------------------- DASHBOARD --------------------
@login_required
def dashboard(request):
    """Dashboard principal do sistema"""

    # Contadores gerais
    total_clientes = Cliente.objects.filter(ativo=True).count()
    total_apolices = Apolice.objects.count()
    total_consorcios = Consorcio.objects.count()
    apolices_ativas = Apolice.objects.filter(status='ATIVA').count()
    apolices_pendentes = Apolice.objects.filter(status='PENDENTE').count()

    # Apólices que vencem ou precisam ser renovadas nos próximos 15 dias
    hoje = timezone.now().date()
    limite = hoje + timedelta(days=15)
    total_vencimentos = Apolice.objects.filter(data_fim__range=(hoje, limite)).count()

    # Atividades recentes
    atividades = Atividade.objects.filter(usuario=request.user).order_by('-data_hora')[:5]

    context = {
        'total_clientes': total_clientes,
        'total_apolices': total_apolices,
        'total_consorcios': total_consorcios,
        'apolices_ativas': apolices_ativas,
        'apolices_pendentes': apolices_pendentes,
        'total_vencimentos': total_vencimentos,
        'atividades': atividades,
    }

    return render(request, 'core/dashboard.html', context)


# -------------------- HOME --------------------
def home(request):
    """Página inicial do site"""
    return render(request, 'core/home.html')


# -------------------- CLIENTES --------------------
@login_required
def cliente_lista(request):
    query = request.GET.get('q', '')
    if query:
        clientes_list = Cliente.objects.filter(
            Q(nome__icontains=query) |
            Q(documento__icontains=query) |
            Q(email__icontains=query)
        ).order_by('nome')
    else:
        clientes_list = Cliente.objects.all().order_by('nome')

    paginator = Paginator(clientes_list, 10)
    page = request.GET.get('page')
    clientes = paginator.get_page(page)

    return render(request, 'core/cliente_lista.html', {'clientes': clientes})


@login_required
def cliente_detalhe(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'core/cliente_detalhe.html', {'cliente': cliente})


@login_required
def cliente_novo(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.cadastrado_por = request.user
            cliente.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('cliente_detalhe', pk=cliente.pk)
    else:
        form = ClienteForm()

    total_clientes = Cliente.objects.count()
    return render(request, 'core/cliente_form.html', {'form': form, 'total_clientes': total_clientes})


@login_required
def cliente_editar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('cliente_detalhe', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)

    total_clientes = Cliente.objects.count()
    return render(request, 'core/cliente_form.html', {'form': form, 'total_clientes': total_clientes})


@login_required
def cliente_excluir(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente excluído com sucesso!')
        return redirect('cliente_lista')
    return render(request, 'core/cliente_confirmar_exclusao.html', {'cliente': cliente})


# -------------------- APÓLICES --------------------
@login_required
def apolice_lista(request):
    query = request.GET.get('q', '')
    apolices = Apolice.objects.all().order_by('-data_inicio')

    if query:
        apolices = apolices.filter(
            Q(numero__icontains=query) |
            Q(cliente__nome__icontains=query) |
            Q(produto__nome__icontains=query)
        )

    filtro = ApoliceFilter(request.GET, queryset=apolices)

    paginador = Paginator(filtro.qs, 10)
    page = request.GET.get('page')
    page_obj = paginador.get_page(page)

    return render(request, 'core/apolice_lista.html', {
        'apolices': page_obj,
        'filter': filtro,
    })


@login_required
def apolice_detalhe(request, pk):
    apolice = get_object_or_404(Apolice, pk=pk)
    return render(request, 'core/apolice_detalhe.html', {'apolice': apolice})


@login_required
def apolice_nova(request):
    cliente_id = request.GET.get('cliente')
    if request.method == 'POST':
        form = ApoliceForm(request.POST)
        if form.is_valid():
            apolice = form.save(commit=False)
            apolice.cadastrado_por = request.user
            apolice.save()
            messages.success(request, 'Apólice cadastrada com sucesso!')
            return redirect('apolice_detalhe', pk=apolice.pk)
    else:
        initial = {}
        if cliente_id:
            try:
                cliente = Cliente.objects.get(pk=cliente_id)
                initial['cliente'] = cliente
            except Cliente.DoesNotExist:
                pass
        form = ApoliceForm(initial=initial)

    total_apolices = Apolice.objects.count()
    return render(request, 'core/apolice_form.html', {'form': form, 'total_apolices': total_apolices})

@login_required
def apolices_renovacao(request):
    """Lista de apólices que precisam ser renovadas nos próximos 15 dias"""
    hoje = timezone.now().date()
    limite = hoje + timedelta(days=15)
    
    apolices = Apolice.objects.filter(data_fim__range=(hoje, limite)).order_by('data_fim')

    return render(request, 'core/apolices_renovacao.html', {'apolices': apolices})

@login_required
def apolice_editar(request, pk):
    apolice = get_object_or_404(Apolice, pk=pk)
    if request.method == 'POST':
        form = ApoliceForm(request.POST, instance=apolice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Apólice atualizada com sucesso!')
            return redirect('apolice_detalhe', pk=apolice.pk)
    else:
        form = ApoliceForm(instance=apolice)

    total_apolices = Apolice.objects.count()
    return render(request, 'core/apolice_form.html', {'form': form, 'total_apolices': total_apolices})


@login_required
def apolice_excluir(request, pk):
    apolice = get_object_or_404(Apolice, pk=pk)
    if request.method == 'POST':
        apolice.delete()
        messages.success(request, 'Apólice excluída com sucesso!')
        return redirect('apolice_lista')
    return render(request, 'core/apolice_confirmar_exclusao.html', {'apolice': apolice})


@login_required
def apolices_pendentes(request):
    pendentes = Apolice.objects.filter(status='PENDENTE')
    return render(request, 'core/apolices_pendentes.html', {'pendentes': pendentes})


# -------------------- SEGURADORAS --------------------
@login_required
def seguradora_lista(request):
    query = request.GET.get('q', '')
    if query:
        seguradoras_list = Seguradora.objects.filter(
            Q(nome__icontains=query) |
            Q(cnpj__icontains=query) |
            Q(codigo__icontains=query)
        ).order_by('nome')
    else:
        seguradoras_list = Seguradora.objects.all().order_by('nome')

    paginator = Paginator(seguradoras_list, 10)
    page = request.GET.get('page')
    seguradoras = paginator.get_page(page)

    return render(request, 'core/seguradora_lista.html', {'seguradoras': seguradoras})


@login_required
def seguradora_detalhe(request, pk):
    seguradora = get_object_or_404(Seguradora, pk=pk)
    return render(request, 'core/seguradora_detalhe.html', {'seguradora': seguradora})


@login_required
def seguradora_nova(request):
    if request.method == 'POST':
        form = SeguradoraForm(request.POST)
        if form.is_valid():
            seguradora = form.save()
            messages.success(request, 'Seguradora cadastrada com sucesso!')
            return redirect('seguradora_detalhe', pk=seguradora.pk)
    else:
        form = SeguradoraForm()
    return render(request, 'core/seguradora_form.html', {'form': form})


@login_required
def seguradora_editar(request, pk):
    seguradora = get_object_or_404(Seguradora, pk=pk)
    if request.method == 'POST':
        form = SeguradoraForm(request.POST, instance=seguradora)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seguradora atualizada com sucesso!')
            return redirect('seguradora_detalhe', pk=seguradora.pk)
    else:
        form = SeguradoraForm(instance=seguradora)
    return render(request, 'core/seguradora_form.html', {'form': form})


@login_required
def seguradora_excluir(request, pk):
    seguradora = get_object_or_404(Seguradora, pk=pk)
    if request.method == 'POST':
        seguradora.delete()
        messages.success(request, 'Seguradora excluída com sucesso!')
        return redirect('seguradora_lista')
    return render(request, 'core/seguradora_confirmar_exclusao.html', {'seguradora': seguradora})


# -------------------- CONSÓRCIOS --------------------
@login_required
def consorcio_lista(request):
    consorcios = Consorcio.objects.all()
    return render(request, 'core/consorcio_lista.html', {'consorcios': consorcios})


@login_required
def consorcio_detalhe(request, pk):
    consorcio = get_object_or_404(Consorcio, pk=pk)
    return render(request, 'core/consorcio_detalhe.html', {'consorcio': consorcio})


@login_required
def consorcio_novo(request):
    if request.method == "POST":
        form = ConsorcioForm(request.POST)
        if form.is_valid():
            consorcio = form.save(commit=False)
            consorcio.cadastrado_por = request.user
            consorcio.save()
            messages.success(request, 'Consórcio cadastrado com sucesso!')
            return redirect('consorcio_detalhe', pk=consorcio.pk)
    else:
        form = ConsorcioForm()
    return render(request, 'core/consorcio_form.html', {'form': form})


@login_required
def consorcio_editar(request, pk):
    consorcio = get_object_or_404(Consorcio, pk=pk)
    if request.method == "POST":
        form = ConsorcioForm(request.POST, instance=consorcio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consórcio atualizado com sucesso!')
            return redirect('consorcio_detalhe', pk=consorcio.pk)
    else:
        form = ConsorcioForm(instance=consorcio)
    return render(request, 'core/consorcio_form.html', {'form': form})


@login_required
def consorcio_excluir(request, pk):
    consorcio = get_object_or_404(Consorcio, pk=pk)
    if request.method == "POST":
        consorcio.delete()
        messages.success(request, 'Consórcio excluído com sucesso!')
        return redirect('consorcio_lista')
    return render(request, 'core/consorcio_confirmar_exclusao.html', {'consorcio': consorcio})


# -------------------- ADMINISTRADORAS --------------------
@login_required
def administradora_nova(request):
    if request.method == 'POST':
        form = AdministradoraConsorcioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Administradora de consórcio cadastrada com sucesso!')
            return redirect('administradora_lista')
    else:
        form = AdministradoraConsorcioForm()
    return render(request, 'core/administradora_form.html', {'form': form})


@login_required
def administradora_lista(request):
    administradoras = AdministradoraConsorcio.objects.all()
    return render(request, 'core/administradora_lista.html', {'administradoras': administradoras})


@login_required
def administradora_editar(request, pk):
    adm = get_object_or_404(AdministradoraConsorcio, pk=pk)
    if request.method == 'POST':
        form = AdministradoraConsorcioForm(request.POST, instance=adm)
        if form.is_valid():
            form.save()
            messages.success(request, 'Administradora atualizada com sucesso!')
            return redirect('administradora_lista')
    else:
        form = AdministradoraConsorcioForm(instance=adm)
    return render(request, 'core/administradora_form.html', {'form': form, 'editar': True})


@login_required
def administradora_excluir(request, pk):
    adm = get_object_or_404(AdministradoraConsorcio, pk=pk)
    if request.method == 'POST':
        adm.delete()
        messages.success(request, 'Administradora excluída com sucesso!')
        return redirect('administradora_lista')
    return render(request, 'core/administradora_confirm_delete.html', {'adm': adm})


# -------------------- PRODUTOS --------------------
@login_required
def produto_lista(request):
    query = request.GET.get('q', '')
    if query:
        produtos_list = Produto.objects.filter(
            Q(nome__icontains=query) |
            Q(codigo__icontains=query) |
            Q(categoria__icontains=query),
            ativo=True
        ).order_by('nome')
    else:
        produtos_list = Produto.objects.filter(ativo=True).order_by('nome')

    paginator = Paginator(produtos_list, 10)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'core/produto_lista.html', {'produtos': produtos, 'query': query})


@login_required
def produto_detalhe(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'core/produto_detalhe.html', {'produto': produto})


@login_required
def produto_novo(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('produto_lista')
    else:
        form = ProdutoForm()
    return render(request, 'core/produto_form.html', {'form': form})


@login_required
def produto_editar(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('produto_lista')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'core/produto_form.html', {'form': form})


@login_required
def produto_excluir(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect('produto_lista')
    return render(request, 'core/produto_confirmar_exclusao.html', {'produto': produto})
