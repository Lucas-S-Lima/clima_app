# Clima App 
##### Sistema de consulta, registro e notificação de temperatura de cidades.

###### Este sistema foi desenvolvido em Python + Django + Celery

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

Acessando o localhost https://127.0.0.1:8000/admin:

![Localhost](./media/Captura%20de%20tela%20de%202025-06-15%2015-30-49.png)

Em `PERIODIC TASKS > Periodic Tasks`:

![PeriodicTask](./media/Captura%20de%20tela%20de%202025-06-15%2015-33-12.png)

Criar tasks no intervalo desejado

![PeriodicTask](./media/Captura%20de%20tela%20de%202025-06-15%2015-40-30.png)

Passar como parâmetro a cidade desejada em `Arguments > Positional Arguments` e salvar:

![PositionalArg](./media/Captura%20de%20tela%20de%202025-06-15%2016-05-47.png)


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

###### Por fim, caso a temperatura de uma cidade ultrapasse o limite estabelecido, o usuário será notificado por email.


