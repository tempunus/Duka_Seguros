from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Cliente, Seguradora, Produto, Apolice, Pagamento, Consorcio
from .forms import ClienteForm, SeguradoraForm, ProdutoForm, ApoliceForm, PagamentoForm, ConsorcioForm, AdministradoraConsorcioForm, AdministradoraConsorcio
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Atividade

def dashboard(request):
    atividades = Atividade.objects.filter(usuario=request.user).order_by('-data_hora')[:5]
    print("Atividades no contexto:", atividades)  # Só para debug
    return render(request, 'dashboard.html', {'atividades': atividades})


def home(request):
    """Página inicial do site"""
    return render(request, 'core/home.html')

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
            Q(documento__icontains=query) |
            Q(email__icontains=query)
        ).order_by('nome')
    else:
        clientes_list = Cliente.objects.all().order_by('nome')
    
    paginator = Paginator(clientes_list, 10)  # 10 clientes por página
    page = request.GET.get('page')
    clientes = paginator.get_page(page)
    
    return render(request, 'core/cliente_lista.html', {'clientes': clientes})


@login_required
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
    """Edição de cliente existente"""
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
    """Exclusão de cliente"""
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente excluído com sucesso!')
        return redirect('cliente_lista')
    
    return render(request, 'core/cliente_confirmar_exclusao.html', {'cliente': cliente})

# Views para Apólice
@login_required
def apolice_lista(request):
    """Lista de apólices"""
    query = request.GET.get('q', '')
    if query:
        apolices_list = Apolice.objects.filter(
            Q(numero__icontains=query) | 
            Q(cliente__nome__icontains=query) |
            Q(produto__nome__icontains=query)
        ).order_by('-data_inicio')
    else:
        apolices_list = Apolice.objects.all().order_by('-data_inicio')
    
    paginator = Paginator(apolices_list, 10)  # 10 apólices por página
    page = request.GET.get('page')
    apolices = paginator.get_page(page)
    
    return render(request, 'core/apolice_lista.html', {'apolices': apolices})

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
def apolice_editar(request, pk):
    """Edição de apólice existente"""
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
    """Exclusão de apólice"""
    apolice = get_object_or_404(Apolice, pk=pk)
    
    if request.method == 'POST':
        apolice.delete()
        messages.success(request, 'Apólice excluída com sucesso!')
        return redirect('apolice_lista')
    
    return render(request, 'core/apolice_confirmar_exclusao.html', {'apolice': apolice})

@login_required
def apolices_pendentes(request):
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
            Q(cnpj__icontains=query) |
            Q(codigo__icontains=query)
        ).order_by('nome')
    else:
        seguradoras_list = Seguradora.objects.all().order_by('nome')
    
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
    """Edição de seguradora existente"""
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
    """Exclusão de seguradora"""
    seguradora = get_object_or_404(Seguradora, pk=pk)
    
    if request.method == 'POST':
        seguradora.delete()
        messages.success(request, 'Seguradora excluída com sucesso!')
        return redirect('seguradora_lista')
    
    return render(request, 'core/seguradora_confirmar_exclusao.html', {'seguradora': seguradora})


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
            consorcio = form.save()
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


@login_required
class ConsorcioCreateView(CreateView):
    model = Consorcio
    form_class = ConsorcioForm
    template_name = 'core/consorcio_form.html'  
    success_url = reverse_lazy('consorcio_lista')  

    def get_initial(self):
        initial = super().get_initial()
        cliente_id = self.request.GET.get('cliente')
        if cliente_id:
            cliente = get_object_or_404(Cliente, pk=cliente_id)
            initial['cliente'] = cliente
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Se quiser deixar o campo cliente desabilitado para não alterar
        if self.request.GET.get('cliente'):
            form.fields['cliente'].disabled = True
        return form


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

def administradora_lista(request):
    from .models import AdministradoraConsorcio
    administradoras = AdministradoraConsorcio.objects.all()
    return render(request, 'core/administradora_lista.html', {'administradoras': administradoras})

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


def administradora_excluir(request, pk):
    adm = get_object_or_404(AdministradoraConsorcio, pk=pk)
    if request.method == 'POST':
        adm.delete()
        messages.success(request, 'Administradora excluída com sucesso!')
        return redirect('administradora_lista')
    return render(request, 'core/administradora_confirm_delete.html', {'adm': adm})
