# Site em django estilo discord

# Sobre
Site desenvolvido em python com o framework django, mas não estou conseguindo fazer o deploy dele.<br>
Postei mesmo assim pois foi uma grande experiencia.<br>
O projeto é uma "copia" pois foi feito acompanhando um tutorial. <br>

Link para ver o projeto completo:
https://youtu.be/_eh15Uq3zPw

https://user-images.githubusercontent.com/95443404/191163094-5befb747-1711-4e0c-be50-43b984bd4ca6.mp4

# O que eu aprendi com o projeto


- [X] Criar a home page, na views, criar uma função home que recebe request e devolve o HttpResponse, importar o HttpResponse: from django.http import HttpResponse, criar uma file urls local e adicionar o caminho ao urlpatterns path na file urls e colocar um nome em cada caminho. Serve para criar as paginas do app.
- [X] Voltar na file urls principal, importar o include, e criar um caminho para a file urls.base: path('', include('base.urls')).
- [X] Criando a pasta template no diretorio base, adicionando os templates de html.
    - [X] Fazendo o django saber que os templates existem: ir no arquivo principal, settings, TEMPLATES e adicionar'DIRS': [BASE_DIR / 'templates'].(BASE_DIR fala pra voltar pra root do arquivo.)
    - [X] Chamando o template html no views, dentro da func criada trocar o HttpResponse por render(request, ('nome do arquivo')).
- [X] Criando uma navbar que aparece em todos os templates, cria-se um arquivo Html e adiciona ele nas outras paginas usando o comando: {% include 'nome do arquivo' %}.
- [X] Melhorando a criação da nav bar, criar um arquivo html main, que vai ser o pai dos outros htmls, dentro do body adicionar: <br>
<body><br>
    {% include 'navbar.html' %} # criando a navbar<br>
    {% block content %}         # inicio do bloco de conteudo<br>
    {% endblock %}              # fim do bloco de conteudo<br>
</body><br>
Depois disso ir em cada pagina do template e adicionar: <br>
{% extends 'main.html' %}<br>
{% block content%}<br>
conteudo<br>
{% endblock content%}<br>

- [X] Limpando o codigo, pra isso é necessario criar uma pasta template dentro do app local, que nesse caso foi a pasta base, criamos um template e dentro da pasta template criamos outra pasta chamada base. (padrao do django), recorte os htmls que não são globais e coloque eles nessa pasta. Agora arrume o local dos novos arquivos dentro da file views.<br>
- [X] Criando links para redirecionamento, ir na file urls e adicionar: <str:pk>/ (string, primary key) ao elemento que vai ser clicavel, depois ir até o html do mesmo e cliar os links, adicionado a tag <'a href='caminho e id'/'> e adicionar o argumento novo a função da views.<br>
- [X] Melhorando o redirecionamento ao criar as tags com o href referenciando a url exemplo: <'a href="{% url 'room' room.id %}'">, Assim se precisarmos trocar a tag n precisamos trocar em todas as paginas.<br>
- [X] Utilizar o comando: python manage.py migrate. Para criar a data base.<br>
    - [X] Ao criar a database, liberamos o acesso ao painel de administrador.<br>
        - [X] Para acessar acessar o painel de administrador, precisamos criar a validação dentro do servidor usando o comando: python manage.py createsuperuser.<br>
    - [X] Para registrar no painel de administrador precisamos importar na base local o que vai ser registrado e usar o comando: admin.site.register("o que foi importado").<br>
    - [X] Para linkar a data base com o que é mostrado na tela,entrar na file views e excluir o que esta linkado com a room antiga, adicioanr a room nova, usando: Room.objects.all() para pegar todos os objetos do model Room. E na func do room, usar Room.objects.get(id=pk) para ter certeza que não temos numeros de paginas iguais.<br>
- [X] dentro do diretorio base local, entrar na file models.py para criar as classes da database.<br>
    - [X] Como nesse projeto teremos as rooms, vamos criar: <br>
    class Room que possui os elementos das nossas salas.<br>
- [X] Ao criar novas migrações usar o comando: python manage.py makemigrations, é praticamente criar um comit para prepagar o novo arquivo para ir para a database.
    - [X] Depois de criar o a migration nova, precisamos aplicar ela com o comando: python manage.py migrate.
- [X] Editando os modelos criados, adicionado uma classe de mensagens para dentro da classe room, sendo filho dela.
    - [X] Depois usar o comando: python manage.py makemigrations para colocar as atualizações em espera e usar o comando: python manage.py migrate para efetualas.
- [X] Adicionar os items para aparecer no html: colocar dentro da tag: @{{"nome do objeto a ser mostrado"}}
------------------------------------------------------------------
CRUD - CREATE READ UPDATE DELETE

- [X] {% csrf_token %} para verificação de token dentro da html.
- [X] O django ja tem uma funcao de form imbutida só precisamos criar o arquivo dos formularios importar o modulo ModelForm especificar os valores definindo a classe, com modelo e campos.
- [X] para salvar os valores do formulario, em views, na função createRoom, faz o request do form, e verifica se ele é valido, se sim salva na db.
- [X] usar o modulo redirect para ao final da criação enviar o usuario para a tela de home.
- [X] colocando ordem nos posts, dentro da file models.py, colocar dentro da classe Salas uma classe com o ordering escolhido.
    - [X] para fazer update da room, ir na file views.py e criar uma func de update.
    - [X] essa func chama o request e a primary key, inicia o formulario da room e renderiza no room_form.html.
- [X] criar um novo html para a parte de deletar o formulario.
- [X] adicionar esse html na views
- [X] adicionar na url
------------------------------------------------------------------
FORMATANDO A PAGINA USANDO CSS 
criar a tag style e o container da pagina html
------------------------------------------------------------------
CRIANDO A SEARCH BAR 
- [X] ir na file views func home e adicioanr o request de salas.
- [X] ir na file html search bar e criar o form.
- [X] criando buscas dinamicas na file views, func home, adicionar no filtro de rooms, primeiro importe, from django.db.models import Q, depois adicione exemplo: Q(topic__name__icontains=q). Topic é o parametro name fala o nome do parametro icontains para ver se contem e q sendo parametro digitado.
- [X] Usar no django para contar algo usar a variavel e no final colocar .count()
-----------------------------------------------------------------
CRIANDO O LOGUIN
- [X] criar uma pagina html nova para o login.
- [X] adicionando as funcionalidades de login.
- [X] depois ir na pagina views e criar a func do login.
- [X] adicionar a func de login na pagina views. 
    - [X] criar o metodo para pegar as informações digitadas, criar opções de erros caso tenha digitado errado e se estiver tudo certo o usuario consegue logar
--------------------------------------------------------------------
CRIANDO O LOGOUT
- [X] Ir na file navbar e criar um redirect para o logout
------------------------------------------------------------------
COLOCANDO SOMENTE PARA QUEM ESTIVER LOGADO CONSEGUIR CRIAR Salas
- [X] Na views importar uma fuc do django chamada login required.E adicioanr ela a func que cria as salas. Parametro para redirect.
-------------------------------------------------------------------
CRIANDO A PARTE DE CADASTRO
- [X] ir na pag views e criar a parte de registro, o django tem uma func especifica pra isso pode importar, UserCreationForm.
----------------------------------------------------------------------------
EDITANDO AS Salas
- [X] adicionando as mensagens nas salas
- [X] colocando o usuario que digitou a mensagem para aparecer, tudo É feito dentro do html da sala, usando as {{}} para chamar a interação.
Exemplo:  <p>{{message.body}}</p> coloca na tela a msg do usuario.
- [X] dentro da views na fuc da sala, criamos a variavel de mensagens e incluimos ela no contexto.
- [X] criando a parte para deletar a mensagem, pra isso criar uma def na views e adicionar o path na url, tendo a func na room.html .

--------------------------------------------------------------------------------
CRIANDO O FEED

- [ ] Na file home.html criar mais uma coluna para o FEED.
- [ ] Na coluna do feed adicionar a parte das ultimas mensagens.
    - [ ] para modificar essa coluna ir na views e trocar na fuc home o que a room_messages esta mostrando.
- [ ] na home coloquei a func de delete mas talvez seja melhor n ter.
- [ ] criar um html para todos os itens da home e usar o {% include %} para adicionar ele a pag principal.

---------------------------------------------------------------------------
CRIANDO O PERFIL

- [ ] na file views criar a func do perfil, adicionar ela na url.

---------------------------------------------------------------------------
STATIC FILES PARA CRIAR O CSS E AS Images

- [ ] criar um folder pra style e outro para img dentro da pasta static
- [ ] deixar o django saber q esta file existe na file settings, criar um caminho para ela.
- [ ] adicionar o css na file main.html chamando o {% load static %} 

---------------------------------------------------------------------
ADICIONANDO TEMPLATES
- [ ] configurar o template para o modo que o django reconhece
{É só substituir}





