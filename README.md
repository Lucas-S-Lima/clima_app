# Clima App 🌥️
##### Sistema de consulta, registro e notificação de temperatura de cidades.

###### Este sistema foi desenvolvido em Python + Django + Celery
<br>

### Como rodar o projeto: 

* Clonar repositório

> `git clone https://github.com/Lucas-S-Lima/clima_app.git`

* Acessando

> `cd clima_app`

* Instalando as dependências

> `pip install -r requirements.txt`

* Aplicando as migrações

> `python manage.py migrate`

* Criar superusuário
>`python manage.py createsuperuser`

* Subindo a aplicação

> `python manage.py runserver`

### Configurando o alerta de notificações

* Diretamente no painel administrativo do Django:

Acessando o localhost http://127.0.0.1:8000/admin:

> Em `PERIODIC TASKS > Periodic Tasks` criar tasks no intervalo desejado

Passar como parâmetro a cidade desejada em `Arguments > Positional Arguments` e salvar

### Configurando o SMTP para envio de e-mails:

* Em settings.py, configurar:

>`EMAIL_HOST_USER = ['your@email.com']`

>`EMAIL_HOST_PASSWORD = ['GmailPasswordApp']`

Que pode ser obtido nas configurações de segurança da conta do Gmail: `Segurança > Senhas de Apps`

### Subindo o gerenciador de tarefas (Celery):

*Pré-requisito: ter o Docker instalado na máquina*

* Criando o container do broker RabbitMQ:

> `docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management`

* Subindo o worker do celery + celery beat:

> `celery -A clima_app -l INFO -B`

* Os logs poderão ser visualizados no terminal ou no painel administrativo em `CELERY RESULTS > Task results`

### Aplicando os testes:

* Para testar a aplicação com os testes criados:

> `python manage.py test`

###### Por fim, caso a temperatura de uma cidade ultrapasse o limite estabelecido, o usuário será notificado por email.



