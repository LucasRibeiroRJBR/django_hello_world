# django_hello_world
 Primeira aplicação Python+Django
 
 ## MANAGE
 * É um wrapper(embrulho) em volta do ```django-admin.py```
 * Ele delega tarefas pro django_```admin.py```
 * Responsável por colocar o pacote do projeto no ```sys.path```
 * Ele define a variável de ambiente **DJANGO_SETTINGS_MODULE** que então aponta para o arquivo ```settings.py```
 * Por isso, o ```manage.py``` é gerado automaticamente junto ao projeto, para facilitar o uso de comandos do ```django_admin.py``` (comandos administrativos)
 
 ## WSGI
 * Web Server Gateway Interface - Interface de porta de entrada do servidor web
 * Plataforma padrão para aplicações web em Python
 * Serve de interface do Servidor Web e a Aplicação Web
 * O Django com o comando ```startproject``` inicia uma configuração WSGI padrão para que se possa executar sua aplicação web
 * Quando se inicia a aplicação Django com o comando ```runserver```, é iniciado um servidor de aplicação web leve. Esse servidor é especificado pela condiguração WSGI_APPLICATION
 
 ## SETTINGS
 * É o responsável pelas condigurações do Django
 * Nele é possível configurar por exemplo apps, conexão com banco de dados, templades, time zone, cache, segurança, arquivos estáticos, etc.
 
 ## URLS
 * É um ```Schema``` de URL
 * Responsável por gerenciar as rotas das URLs, onde é possível configurar pra onde cada rota será executada
 * É uma forma limpa e elegante de gerenciar URLs
 
 ## VIEWS
 * Responsável por processar e retornar uma resposta para o cliente que fez a requisição
 
```python
def soma(request, numero_a, numero_b):
    total = numero_a + numero_b
    return HttpResponse(f'<h1>A soma é: {total}.</h1>')
```
 
