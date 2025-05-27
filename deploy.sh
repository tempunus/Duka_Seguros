#!/bin/bash

# Script de implantação para a aplicação Duka Seguradora

echo "Iniciando implantação da aplicação Duka Seguradora..."

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

# Instalar dependências de produção
echo "Instalando dependências de produção..."
pip install gunicorn whitenoise

# Configurar settings para produção
echo "Configurando settings para produção..."
sed -i "s/DEBUG = True/DEBUG = False/" duka_project/settings.py
sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \['*'\]/" duka_project/settings.py

# Adicionar whitenoise para servir arquivos estáticos
if ! grep -q "whitenoise" duka_project/settings.py; then
    sed -i "/MIDDLEWARE = \[/a \    'whitenoise.middleware.WhiteNoiseMiddleware'," duka_project/settings.py
    echo "STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'" >> duka_project/settings.py
fi

# Coletar arquivos estáticos
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

# Aplicar migrações finais
echo "Aplicando migrações finais..."
python manage.py migrate

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

# Iniciar servidor com gunicorn
echo "Iniciando servidor com gunicorn..."
gunicorn duka_project.wsgi:application --bind 0.0.0.0:8000 --daemon

echo "Implantação concluída com sucesso!"
echo "A aplicação está disponível em: http://localhost:8000"
echo "Usuário admin: admin@dukaseguradora.com"
echo "Senha: admin123"
