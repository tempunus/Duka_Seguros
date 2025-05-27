# Documentação da Aplicação Duka Seguradora

## Visão Geral

A aplicação Duka Seguradora é um sistema web desenvolvido em Django para gerenciamento de uma corretora de seguros. O sistema permite o cadastro e gerenciamento de clientes, apólices, seguradoras, produtos e pagamentos, com acesso protegido por senha.

## Tecnologias Utilizadas

- **Backend**: Python 3.10 com Django 5.2
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Banco de Dados**: SQLite (desenvolvimento)
- **Autenticação**: Sistema de autenticação do Django

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
duka_seguradora/
├── accounts/            # App para gerenciamento de usuários
├── core/                # App principal com funcionalidades de negócio
├── duka_project/        # Configurações do projeto Django
├── static/              # Arquivos estáticos (CSS, JS, imagens)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/           # Templates HTML
│   ├── accounts/
│   ├── core/
│   └── base.html
├── venv/                # Ambiente virtual Python
└── manage.py            # Script de gerenciamento Django
```

## Funcionalidades Principais

### Sistema de Autenticação
- Login e logout de usuários
- Registro de novos usuários
- Recuperação de senha
- Perfil de usuário

### Gerenciamento de Clientes
- Cadastro de clientes (pessoa física e jurídica)
- Listagem, edição e exclusão de clientes
- Visualização detalhada de clientes
- Busca e filtros

### Gerenciamento de Apólices
- Cadastro de apólices
- Listagem, edição e exclusão de apólices
- Visualização detalhada de apólices
- Controle de status (ativa, pendente, cancelada, vencida, renovada)
- Busca e filtros

### Gerenciamento de Seguradoras
- Cadastro de seguradoras
- Listagem, edição e exclusão de seguradoras
- Visualização detalhada de seguradoras

### Gerenciamento de Produtos
- Cadastro de produtos de seguros
- Listagem, edição e exclusão de produtos
- Categorização de produtos

### Gerenciamento de Pagamentos
- Registro de pagamentos de apólices
- Controle de parcelas
- Acompanhamento de status de pagamento

## Modelos de Dados

### Cliente
- Tipo (Pessoa Física/Jurídica)
- Nome/Razão Social
- CPF/CNPJ
- Dados de contato (email, telefone)
- Endereço completo
- Data de nascimento (para pessoa física)
- Status (ativo/inativo)
- Observações

### Apólice
- Número da apólice
- Cliente
- Produto
- Datas de início e fim de vigência
- Valor do prêmio
- Valor e percentual de comissão
- Status (ativa, pendente, cancelada, vencida, renovada)
- Observações

### Seguradora
- Nome
- CNPJ
- Código
- Dados de contato
- Site
- Status (ativa/inativa)

### Produto
- Nome
- Código
- Categoria
- Descrição
- Seguradora
- Status (ativo/inativo)

### Pagamento
- Apólice
- Data de vencimento
- Data de pagamento
- Valor
- Forma de pagamento
- Status (pago, pendente, atrasado, cancelado)
- Número da parcela e total de parcelas
- Observações

## Instruções de Uso

### Requisitos
- Python 3.10 ou superior
- Pip (gerenciador de pacotes Python)
- Virtualenv (recomendado)

### Instalação e Configuração

1. Clone o repositório ou extraia os arquivos do projeto
2. Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
4. Execute as migrações do banco de dados:
   ```
   python manage.py migrate
   ```
5. Crie um superusuário para acessar o sistema:
   ```
   python manage.py createsuperuser
   ```
6. Inicie o servidor de desenvolvimento:
   ```
   python manage.py runserver
   ```
7. Acesse o sistema em http://localhost:8000

### Acesso ao Sistema

- Use o email e senha cadastrados para fazer login
- O painel administrativo está disponível em http://localhost:8000/admin/

## Considerações de Segurança

- Todas as rotas do sistema (exceto a página inicial e login) estão protegidas por autenticação
- As senhas são armazenadas de forma segura usando o sistema de hash do Django
- Validações de formulários são realizadas tanto no frontend quanto no backend

## Manutenção e Suporte

Para manutenção e suporte da aplicação:

1. Mantenha o Django e as dependências atualizadas
2. Faça backup regular do banco de dados
3. Para ambientes de produção, considere usar PostgreSQL ou MySQL
4. Configure um servidor web como Nginx ou Apache para servir a aplicação em produção
5. Utilize HTTPS para garantir a segurança das comunicações

## Próximos Passos e Melhorias Futuras

- Implementação de relatórios e dashboards avançados
- Integração com APIs de seguradoras
- Sistema de notificações para apólices próximas do vencimento
- Aplicativo móvel para acesso em dispositivos Android e iOS
- Módulo de cotações online
