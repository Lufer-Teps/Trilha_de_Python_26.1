# Trilha_de_Python_26.1
DESAFIO 1

#explicação do código:

O código visa auxiliar o usuário a prepara uma viagem para o exterior com o custo em Euros.
O programa coletará informações do usuário como custo da passagem, diária e orçamento do mesmo em reais. fará as converções necessárias e no final informará se a sua viagem é possivel ou não.

#Informações de uso:

Na primeira interação o usuario precisa digitar o valor do seu orçamento em reais.
Na segunda interação deverá infroma o lugar de destino.
Na terceira o valor da passagem.
Na quarta devera informa o valor da diária em euros.
E na ultima interação final o seu tempo de estadia.

Após essas informações sera informado se a viagem é válida ou não, além do restante do dinheiro no final em caso de viagem válida, caso contrário informara o quanto de dinheiro ainda é necessario.

OBS: Não digitar valores negativos, ou então o código será encerrado com uma mensagem informando do problema.



#Perguntas teóricas finais do desafio

1) git add . inclui todas as mudanças no programa para a staging area para assim o usuario poder salva las depois. git commit -m ""salva as alterações no historico, pra informar oq foi modificado.

2) porque o comando "input" sempre vai entender que oq foi digitado pelo usuário é uma string, logo para a realização de algumas contas é necessario transformar o valor em int ou float.

3) da erro no código. A linguagem python não sabe somar uma string com um valor decimal automaticamente.


DESAFIO 2)

#explicação do código:

O código funciona com uma batalha simulado entre 2 cartas de um mesmo jogador.

o usuario precisa inserir o monstro assim como seu ataque e vida.
O primeiro sera considerado monstro 1 e todos os seus atributos serao marcados depois como 1.
o segundo sera considerado monstro 2 e todos os parametros serao marcados como 2.
o código nao funcionara se os valores forem negativos, onde o mesmo ira parar e exibir mensagem justificando o motivo da não continuação.

1) o laço de loop for consiste em um loop de variaveis onde o loop ja foi listado anteriormente pelo usuario enquanto o while consite em um loop infinito onde o mesmo continuara enquanto uma condição for considerada verdadeira no caso desse desafio a vida de um monstro for maior que 0.

2) o return como o nome ja diz returna a função quando ela for exigida. Se um calculo for feito e a função não for retornada a função vai calcular e vai deixar esse valor guardado, esperando ele ser chamado.

3) loops infinitos acontecem com maior frequencia na estrutura while pois a mesma roda infinitamente por natureza, onde a mesma só ira parar quando uma condicional for colocada ou a condicional for falsa.