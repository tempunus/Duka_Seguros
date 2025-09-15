from django.shortcuts import render, redirect, get_object_or_404
<<<<<<< HEAD
from django.shortcuts import get_object_or_404
=======
>>>>>>> b372def (Alterações_Duka)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
<<<<<<< HEAD
from .models import Cliente, Seguradora, Produto, Apolice, Pagamento, Consorcio
from .forms import ClienteForm, SeguradoraForm, ProdutoForm, ApoliceForm, PagamentoForm, ConsorcioForm, AdministradoraConsorcioForm, AdministradoraConsorcio
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Atividade
from .models import Apolice
from .filters import ApoliceFilter


def dashboard(request):
    atividades = Atividade.objects.filter(usuario=request.user).order_by('-data_hora')[:5]
    print("Atividades no contexto:", atividades)  # Só para debug
    return render(request, 'dashboard.html', {'atividades': atividades})

=======
from django.utils import timezone
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import (
    Cliente, Seguradora, Produto, Apolice, Pagamento,
    Consorcio, Atividade, AdministradoraConsorcio
)
from .forms import (
    ClienteForm, SeguradoraForm, ProdutoForm, ApoliceForm,
    PagamentoForm, ConsorcioForm, AdministradoraConsorcioForm
)
from .filters import ApoliceFilter


# ================= DASHBOARD =====================

@login_required
def dashboard(request):
    """Dashboard principal do sistema"""

    # Datas de referência
    hoje = timezone.now().date()
    daqui_15_dias = hoje + timezone.timedelta(days=15)

    # Contadores principais
    total_clientes = Cliente.objects.filter(ativo=True).count()
    total_apolices = Apolice.objects.count()
    total_consorcio = Consorcio.objects.count()
    apolices_ativas = Apolice.objects.filter(status='ATIVA').count()
    apolices_pendentes = Apolice.objects.filter(status='PENDENTE').count()

    # Vencimentos futuros (pagamentos com data >= hoje)
    total_vencimentos = Pagamento.objects.filter(
        data_vencimento__gte=hoje
    ).count()

    # Renovações → apólices que vencem nos próximos 15 dias
    apolices_renovacoes = Apolice.objects.filter(
        data_fim__gte=hoje,
        data_fim__lte=daqui_15_dias
    ).count()

    # Listas de referência
    apolices_recentes = Apolice.objects.order_by('-data_cadastro')[:5]
    atividades = Atividade.objects.filter(
        usuario=request.user
    ).order_by('-data_hora')[:5]
    pagamentos_vencidos = Pagamento.objects.filter(
        data_vencimento__lt=hoje
    )

    context = {
        'total_clientes': total_clientes,
        'total_apolices': total_apolices,
        'total_consorcio': total_consorcio,
        'apolices_ativas': apolices_ativas,
        'apolices_pendentes': apolices_pendentes,
        'total_vencimentos': total_vencimentos,
        'apolices_renovacoes': apolices_renovacoes,  # 👈 novo campo para dashboard
        'apolices_recentes': apolices_recentes,
        'atividades': atividades,
        'pagamentos_vencidos': pagamentos_vencidos,
    }

    return render(request, 'core/dashboard.html', context)


# ================= HOME =====================
>>>>>>> b372def (Alterações_Duka)

def home(request):
    """Página inicial do site"""
    return render(request, 'core/home.html')

<<<<<<< HEAD
@login_required
def dashboard(request):
    """Dashboard principal do sistema"""
    # Contadores para o dashboard
    total_clientes = Cliente.objects.filter(ativo=True).count()
    total_apolices = Apolice.objects.all().count()
    apolices_ativas = Apolice.objects.filter(status='ATIVA').count()
    apolices_pendentes = Apolice.objects.filter(status='PENDENTE').count()
    
    # Apólices recentes
    apolices_recentes = Apolice.objects.all().order_by('-data_cadastro')[:5]
    
    context = {
        'total_clientes': total_clientes,
        'total_apolices': total_apolices,
        'apolices_ativas': apolices_ativas,
        'apolices_pendentes': apolices_pendentes,
        'apolices_recentes': apolices_recentes,
    }
    return render(request, 'core/dashboard.html', context)

# Views para Cliente
@login_required
def cliente_lista(request):
    """Lista de clientes"""
    query = request.GET.get('q', '')
    if query:
        clientes_list = Cliente.objects.filter(
            Q(nome__icontains=query) | 
=======

# ================= CLIENTE =====================

@login_required
def cliente_lista(request):
    query = request.GET.get('q', '')
    if query:
        clientes_list = Cliente.objects.filter(
            Q(nome__icontains=query) |
>>>>>>> b372def (Alterações_Duka)
            Q(documento__icontains=query) |
            Q(email__icontains=query)
        ).order_by('nome')
    else:
        clientes_list = Cliente.objects.all().order_by('nome')
<<<<<<< HEAD
    
    paginator = Paginator(clientes_list, 10)  # 10 clientes por página
    page = request.GET.get('page')
    clientes = paginator.get_page(page)
    
=======

    paginator = Paginator(clientes_list, 10)
    page = request.GET.get('page')
    clientes = paginator.get_page(page)

>>>>>>> b372def (Alterações_Duka)
    return render(request, 'core/cliente_lista.html', {'clientes': clientes})


@login_required
<<<<<<< HEAD
def total_clientes_view(request):
    """total de clientes"""
    total_clientes = Cliente.objects.count()
    return render(request, 'clientes/total_clientes.html', {
        'total_clientes': total_clientes
    })
    
@login_required
def cliente_detalhe(request, pk):
    """Detalhes do cliente"""
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'core/cliente_detalhe.html', {'cliente': cliente})

@login_required
def cliente_novo(request):
    """Cadastro de novo cliente"""
=======
def cliente_detalhe(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'core/cliente_detalhe.html', {'cliente': cliente})


@login_required
def cliente_novo(request):
>>>>>>> b372def (Alterações_Duka)
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
<<<<<<< HEAD
    
    total_clientes = Cliente.objects.count()
    return render(request, 'core/cliente_form.html', {'form': form, 'total_clientes': total_clientes})
    

@login_required
def cliente_editar(request, pk):
    """Edição de cliente existente"""
    cliente = get_object_or_404(Cliente, pk=pk)
    
=======

    return render(request, 'core/cliente_form.html', {'form': form})


@login_required
def cliente_editar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
>>>>>>> b372def (Alterações_Duka)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('cliente_detalhe', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
<<<<<<< HEAD
    
    total_clientes = Cliente.objects.count()
    return render(request, 'core/cliente_form.html', {'form': form, 'total_clientes': total_clientes})

@login_required
def cliente_excluir(request, pk):
    """Exclusão de cliente"""
    cliente = get_object_or_404(Cliente, pk=pk)
    
=======

    return render(request, 'core/cliente_form.html', {'form': form})


@login_required
def cliente_excluir(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
>>>>>>> b372def (Alterações_Duka)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente excluído com sucesso!')
        return redirect('cliente_lista')
<<<<<<< HEAD
    
    return render(request, 'core/cliente_confirmar_exclusao.html', {'cliente': cliente})

# Views para Apólice
@login_required
def apolice_lista(request):
    """Lista de apólices com busca e filtro por data"""
    query = request.GET.get('q', '')

    # Começa com todas as apólices
    apolices = Apolice.objects.all().order_by('-data_inicio')

    # Filtro de busca textual
=======
    return render(request, 'core/cliente_confirmar_exclusao.html', {'cliente': cliente})


# ================= APÓLICE =====================

@login_required
def apolice_lista(request):
    query = request.GET.get('q', '')
    apolices = Apolice.objects.all().order_by('-data_inicio')

>>>>>>> b372def (Alterações_Duka)
    if query:
        apolices = apolices.filter(
            Q(numero__icontains=query) |
            Q(cliente__nome__icontains=query) |
            Q(produto__nome__icontains=query)
        )

<<<<<<< HEAD
    # Filtro por data (usando django-filter)
    filtro = ApoliceFilter(request.GET, queryset=apolices)

    # Paginação
=======
    filtro = ApoliceFilter(request.GET, queryset=apolices)
>>>>>>> b372def (Alterações_Duka)
    paginador = Paginator(filtro.qs, 10)
    page = request.GET.get('page')
    page_obj = paginador.get_page(page)

<<<<<<< HEAD
    # Renderiza template com contexto
=======
>>>>>>> b372def (Alterações_Duka)
    return render(request, 'core/apolice_lista.html', {
        'apolices': page_obj,
        'filter': filtro,
    })
<<<<<<< HEAD
  

@login_required
def total_apolice_view(request):
    """total de apolices"""
    total_apolices = Apolice.objects.count()
    return render(request, 'apolices/total_apolices.html', {
        'total_apilices': total_apolices
    })

@login_required
def apolice_detalhe(request, pk):
    """Detalhes da apólice"""
    apolice = get_object_or_404(Apolice, pk=pk)
    return render(request, 'core/apolice_detalhe.html', {'apolice': apolice})

@login_required
def apolice_nova(request):
    """Cadastro de nova apólice"""
    cliente_id = request.GET.get('cliente')
    
=======


@login_required
def apolice_detalhe(request, pk):
    apolice = get_object_or_404(Apolice, pk=pk)

    # Registrar acesso do usuário
    Atividade.objects.create(
        usuario=request.user,
        descricao=f"Acessou a apólice {apolice.numero}",
        apolice=apolice
    )

    return render(request, 'core/apolice_detalhe.html', {'apolice': apolice})


@login_required
def apolice_nova(request):
    cliente_id = request.GET.get('cliente')
>>>>>>> b372def (Alterações_Duka)
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
<<<<<<< HEAD
        
        form = ApoliceForm(initial=initial)
    
    total_apolices = Apolice.objects.count()
    return render(request, 'core/apolice_form.html', {'form': form, 'total_apolices': total_apolices})
=======
        form = ApoliceForm(initial=initial)

    return render(request, 'core/apolice_form.html', {'form': form})
>>>>>>> b372def (Alterações_Duka)


@login_required
def apolice_editar(request, pk):
<<<<<<< HEAD
    """Edição de apólice existente"""
    apolice = get_object_or_404(Apolice, pk=pk)
    
=======
    apolice = get_object_or_404(Apolice, pk=pk)
>>>>>>> b372def (Alterações_Duka)
    if request.method == 'POST':
        form = ApoliceForm(request.POST, instance=apolice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Apólice atualizada com sucesso!')
            return redirect('apolice_detalhe', pk=apolice.pk)
    else:
        form = ApoliceForm(instance=apolice)
<<<<<<< HEAD
    
    total_apolices = Apolice.objects.count()
    return render(request, 'core/apolice_form.html', {'form': form, 'total_apolices': total_apolices})

@login_required
def apolice_excluir(request, pk):
    """Exclusão de apólice"""
    apolice = get_object_or_404(Apolice, pk=pk)

=======

    return render(request, 'core/apolice_form.html', {'form': form})


@login_required
def apolice_excluir(request, pk):
    apolice = get_object_or_404(Apolice, pk=pk)
>>>>>>> b372def (Alterações_Duka)
    if request.method == 'POST':
        apolice.delete()
        messages.success(request, 'Apólice excluída com sucesso!')
        return redirect('apolice_lista')
<<<<<<< HEAD

=======
>>>>>>> b372def (Alterações_Duka)
    return render(request, 'core/apolice_confirmar_exclusao.html', {'apolice': apolice})


@login_required
def apolices_pendentes(request):
<<<<<<< HEAD
    pendentes = Apolice.objects.filter(status='PENDENTE').exclude(id__isnull=True)
    return render(request, 'core/apolices_pendentes.html', {'pendentes': pendentes})

# Views para Seguradora
@login_required
def seguradora_lista(request):
    """Lista de seguradoras"""
    query = request.GET.get('q', '')
    if query:
        seguradoras_list = Seguradora.objects.filter(
            Q(nome__icontains=query) | 
=======
    pendentes = Apolice.objects.filter(status='PENDENTE')
    return render(request, 'core/apolices_pendentes.html', {'pendentes': pendentes})


# ================= SEGURADORA =====================

@login_required
def seguradora_lista(request):
    query = request.GET.get('q', '')
    if query:
        seguradoras_list = Seguradora.objects.filter(
            Q(nome__icontains=query) |
>>>>>>> b372def (Alterações_Duka)
            Q(cnpj__icontains=query) |
            Q(codigo__icontains=query)
        ).order_by('nome')
    else:
        seguradoras_list = Seguradora.objects.all().order_by('nome')
<<<<<<< HEAD
    
    paginator = Paginator(seguradoras_list, 10)  # 10 seguradoras por página
    page = request.GET.get('page')
    seguradoras = paginator.get_page(page)
    
    return render(request, 'core/seguradora_lista.html', {'seguradoras': seguradoras})

@login_required
def seguradora_detalhe(request, pk):
    """Detalhes da seguradora"""
    seguradora = get_object_or_404(Seguradora, pk=pk)
    return render(request, 'core/seguradora_detalhe.html', {'seguradora': seguradora})

@login_required
def seguradora_nova(request):
    """Cadastro de nova seguradora"""
=======

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
>>>>>>> b372def (Alterações_Duka)
    if request.method == 'POST':
        form = SeguradoraForm(request.POST)
        if form.is_valid():
            seguradora = form.save()
            messages.success(request, 'Seguradora cadastrada com sucesso!')
            return redirect('seguradora_detalhe', pk=seguradora.pk)
    else:
        form = SeguradoraForm()
<<<<<<< HEAD
    
    return render(request, 'core/seguradora_form.html', {'form': form})

@login_required
def seguradora_editar(request, pk):
    """Edição de seguradora existente"""
    seguradora = get_object_or_404(Seguradora, pk=pk)
    
=======
    return render(request, 'core/seguradora_form.html', {'form': form})


@login_required
def seguradora_editar(request, pk):
    seguradora = get_object_or_404(Seguradora, pk=pk)
>>>>>>> b372def (Alterações_Duka)
    if request.method == 'POST':
        form = SeguradoraForm(request.POST, instance=seguradora)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seguradora atualizada com sucesso!')
            return redirect('seguradora_detalhe', pk=seguradora.pk)
    else:
        form = SeguradoraForm(instance=seguradora)
<<<<<<< HEAD
    
    return render(request, 'core/seguradora_form.html', {'form': form})

@login_required
def seguradora_excluir(request, pk):
    """Exclusão de seguradora"""
    seguradora = get_object_or_404(Seguradora, pk=pk)
    
=======
    return render(request, 'core/seguradora_form.html', {'form': form})


@login_required
def seguradora_excluir(request, pk):
    seguradora = get_object_or_404(Seguradora, pk=pk)
>>>>>>> b372def (Alterações_Duka)
    if request.method == 'POST':
        seguradora.delete()
        messages.success(request, 'Seguradora excluída com sucesso!')
        return redirect('seguradora_lista')
<<<<<<< HEAD
    
    return render(request, 'core/seguradora_confirmar_exclusao.html', {'seguradora': seguradora})


=======
    return render(request, 'core/seguradora_confirmar_exclusao.html', {'seguradora': seguradora})


# ================= CONSÓRCIO =====================

>>>>>>> b372def (Alterações_Duka)
@login_required
def consorcio_lista(request):
    consorcios = Consorcio.objects.all()
    return render(request, 'core/consorcio_lista.html', {'consorcios': consorcios})

<<<<<<< HEAD
@login_required
def consorcio_detalhe(request, pk):
    consorcio = get_object_or_404(Consorcio, pk=pk)
    return render(request, 'core/consorcio_detalhe.html', {'consorcio': consorcio})

=======

@login_required
def consorcio_detalhe(request, pk):
    consorcio = get_object_or_404(Consorcio, pk=pk)

    # Registrar acesso do usuário
    Atividade.objects.create(
        usuario=request.user,
        descricao=f"Acessou o consórcio {consorcio.id}",
        consorcio=consorcio
    )

    return render(request, 'core/consorcio_detalhe.html', {'consorcio': consorcio})


>>>>>>> b372def (Alterações_Duka)
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

<<<<<<< HEAD
=======

>>>>>>> b372def (Alterações_Duka)
@login_required
def consorcio_editar(request, pk):
    consorcio = get_object_or_404(Consorcio, pk=pk)
    if request.method == "POST":
        form = ConsorcioForm(request.POST, instance=consorcio)
        if form.is_valid():
            consorcio = form.save()
            messages.success(request, 'Consórcio atualizado com sucesso!')
            return redirect('consorcio_detalhe', pk=consorcio.pk)
    else:
        form = ConsorcioForm(instance=consorcio)
    return render(request, 'core/consorcio_form.html', {'form': form})

<<<<<<< HEAD
=======

>>>>>>> b372def (Alterações_Duka)
@login_required
def consorcio_excluir(request, pk):
    consorcio = get_object_or_404(Consorcio, pk=pk)
    if request.method == "POST":
        consorcio.delete()
        messages.success(request, 'Consórcio excluído com sucesso!')
        return redirect('consorcio_lista')
    return render(request, 'core/consorcio_confirmar_exclusao.html', {'consorcio': consorcio})


<<<<<<< HEAD
@login_required
class ConsorcioCreateView(CreateView):
    model = Consorcio
    form_class = ConsorcioForm
    template_name = 'core/consorcio_form.html'  
    success_url = reverse_lazy('consorcio_lista')  
=======
class ConsorcioCreateView(CreateView):
    model = Consorcio
    form_class = ConsorcioForm
    template_name = 'core/consorcio_form.html'
    success_url = reverse_lazy('consorcio_lista')
>>>>>>> b372def (Alterações_Duka)

    def get_initial(self):
        initial = super().get_initial()
        cliente_id = self.request.GET.get('cliente')
        if cliente_id:
            cliente = get_object_or_404(Cliente, pk=cliente_id)
            initial['cliente'] = cliente
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
<<<<<<< HEAD
        # Se quiser deixar o campo cliente desabilitado para não alterar
=======
>>>>>>> b372def (Alterações_Duka)
        if self.request.GET.get('cliente'):
            form.fields['cliente'].disabled = True
        return form


<<<<<<< HEAD
=======
# ================= ADMINISTRADORA CONSÓRCIO =====================

>>>>>>> b372def (Alterações_Duka)
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

<<<<<<< HEAD
def administradora_lista(request):
    from .models import AdministradoraConsorcio
    administradoras = AdministradoraConsorcio.objects.all()
    return render(request, 'core/administradora_lista.html', {'administradoras': administradoras})

=======

@login_required
def administradora_lista(request):
    administradoras = AdministradoraConsorcio.objects.all()
    return render(request, 'core/administradora_lista.html', {'administradoras': administradoras})


@login_required
>>>>>>> b372def (Alterações_Duka)
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


<<<<<<< HEAD
=======
@login_required
>>>>>>> b372def (Alterações_Duka)
def administradora_excluir(request, pk):
    adm = get_object_or_404(AdministradoraConsorcio, pk=pk)
    if request.method == 'POST':
        adm.delete()
        messages.success(request, 'Administradora excluída com sucesso!')
        return redirect('administradora_lista')
    return render(request, 'core/administradora_confirm_delete.html', {'adm': adm})
