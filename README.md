Situação Proposta

Obter alguns dados de um usuário do Github.

API utlizada, Github para a leitura dos dados.

Passo 1: Classe User
Criar um objeto/classe para representar os dados do usuário do Github.

Os dados mínimos esperados são:
Nome do usuário;
URL para o perfil do usuário;
Número de repositórios publicos do usuário;
Número de seguidores do usuário;
Número de pessoas que o usuário segue.

Passo 2: Leitura dos dados do usuário
Criar uma função que deve receber o nome de usuário, acessar a API do Github e retornar o objeto do usuário criado no primeiro passo do desafio.


Passo 3: Leitura dos repositórios
Criar uma função ou método que retorne um dicionário que contem o nome dos repositórios do usuário como chave e a URL do repositório como valor.

Exemplo para o usuário 'githubuser':
{
'empass': 'https://github.com/githubuser/empass',
'grit': 'https://github.com/githubuser/grit',
'mysuperproject': 'https://github.com/githubuser/mysuperproject',
'simplegit': 'https://github.com/githubuser/simplegit'
}


Passo 4: Gerar relatório do usuário
Criar uma função que receba os dados do usuário e seus repositórios e gere um arquivo de texto básico (txt) que contém os dados do usuário 
do primeiro passo e uma lista de repositórios com a URL deles.

Esse arquivo gerado deve apresentar em seu nome o "login" do usuário.

Relatório esperado para o usuário 'githubuser', esse relatório deve ter o nome 'githubuser.txt':
Nome: None
Perfil: https://github.com/githubuser
Número de repositórios publicos: 4
Número de seguidores: 5
Número de usuários seguidos: 0
Repositórios:
empass: https://github.com/githubuser/empass
grit: https://github.com/githubuser/grit
mysuperproject: https://github.com/githubuser/mysuperproject
simplegit: https://github.com/githubuser/simplegit

Critérios de avaliação
Funcionamento do código
Testes de unidade
Cobertura de testes
Complexidade ciclomática
