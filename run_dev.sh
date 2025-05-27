#!/bin/bash

# Script para iniciar a aplicação Duka Seguradora em modo de desenvolvimento

echo "Iniciando a aplicação Duka Seguradora em modo de desenvolvimento..."

# Verificar se o diretório do projeto existe
if [ ! -d "/home/ubuntu/duka_seguradora" ]; then
    echo "Erro: Diretório do projeto não encontrado!"
    exit 1
fi

# Entrar no diretório do projeto
cd /home/ubuntu/duka_seguradora

# Ativar ambiente virtual
echo "Ativando ambiente virtual..."
source venv/bin/activate

# Criar superusuário se não existir
echo "Verificando superusuário..."
python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duka_project.settings')
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@dukaseguradora.com', 'admin123')
    print('Superusuário criado com sucesso!')
else:
    print('Superusuário já existe.')
"

# Iniciar servidor de desenvolvimento
echo "Iniciando servidor de desenvolvimento..."
python manage.py runserver 0.0.0.0:8000

echo "Servidor encerrado."
