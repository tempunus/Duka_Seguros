from django.urls import path
from . import views
from . import views_produto_pagamento

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # URLs para Cliente
    path('clientes/', views.cliente_lista, name='cliente_lista'),
    path('clientes/novo/', views.cliente_novo, name='cliente_novo'),
    path('clientes/<int:pk>/', views.cliente_detalhe, name='cliente_detalhe'),
    path('clientes/<int:pk>/editar/', views.cliente_editar, name='cliente_editar'),
    path('clientes/<int:pk>/excluir/', views.cliente_excluir, name='cliente_excluir'),
    
    # URLs para Apólice
    path('apolices/', views.apolice_lista, name='apolice_lista'),
    path('apolices/nova/', views.apolice_nova, name='apolice_nova'),
    path('apolices/<int:pk>/', views.apolice_detalhe, name='apolice_detalhe'),
    path('apolices/<int:pk>/editar/', views.apolice_editar, name='apolice_editar'),
    path('apolices/<int:pk>/excluir/', views.apolice_excluir, name='apolice_excluir'),
    path('apolices/pendentes/', views.apolices_pendentes, name='apolices_pendentes'),
    path('apolices-renovacao/', views.apolices_renovacao, name='apolices_renovacao'),

    
    # URLs para Seguradora
    path('seguradoras/', views.seguradora_lista, name='seguradora_lista'),
    path('seguradoras/nova/', views.seguradora_nova, name='seguradora_nova'),
    path('seguradoras/<int:pk>/', views.seguradora_detalhe, name='seguradora_detalhe'),
    path('seguradoras/<int:pk>/editar/', views.seguradora_editar, name='seguradora_editar'),
    path('seguradoras/<int:pk>/excluir/', views.seguradora_excluir, name='seguradora_excluir'),
    
    
    # URLs para Produto
    path('produtos/', views_produto_pagamento.produto_lista, name='produto_lista'),
    path('produtos/novo/', views_produto_pagamento.produto_novo, name='produto_novo'),
    path('produtos/<int:pk>/', views_produto_pagamento.produto_detalhe, name='produto_detalhe'),
    path('produtos/<int:pk>/editar/', views_produto_pagamento.produto_editar, name='produto_editar'),
    path('produtos/<int:pk>/excluir/', views_produto_pagamento.produto_excluir, name='produto_excluir'),
    
    # URLs para Pagamento
    path('pagamentos/', views_produto_pagamento.pagamento_lista, name='pagamento_lista'),
    path('pagamentos/novo/', views_produto_pagamento.pagamento_novo, name='pagamento_novo'),
    path('pagamentos/<int:pk>/', views_produto_pagamento.pagamento_detalhe, name='pagamento_detalhe'),
    path('pagamentos/<int:pk>/editar/', views_produto_pagamento.pagamento_editar, name='pagamento_editar'),
    path('pagamentos/<int:pk>/excluir/', views_produto_pagamento.pagamento_excluir, name='pagamento_excluir'),
    
    
    # URLs para Consorcio
    path('consorcios/', views.consorcio_lista, name='consorcio_lista'),
    path('consorcios/novo/', views.consorcio_novo, name='consorcio_novo'),
    path('consorcios/<int:pk>/', views.consorcio_detalhe, name='consorcio_detalhe'),
    path('consorcios/<int:pk>/editar/', views.consorcio_editar, name='consorcio_editar'),
    path('consorcios/<int:pk>/excluir/', views.consorcio_excluir, name='consorcio_excluir'),
    path('administradora/nova/', views.administradora_nova, name='administradora_nova'),
    path('administradora/lista/', views.administradora_lista, name='administradora_lista'),
    path('administradora/<int:pk>/editar/', views.administradora_editar, name='administradora_editar'),
    path('administradora/<int:pk>/excluir/', views.administradora_excluir, name='administradora_excluir'),

]



