<h1>Algortimo de pesquisa binária</h1>

<h3>Então o que seria uma pesquisa binária?</h3>
<p>
Imagina que eu peça para você pensar em um número de 1 até 100 e somente me falar se o chute que eu estou falando é alto ou baixo. Eu poderia chutar todos os números de 1 até 100 sendo assim, se começarmos a chutar com o número 1 e o número pensado por você for o 100 nós teríamos que percorrer essa lista de números inteira para achar o seu número pensado.
</p>
<p>
O algoritmo de pesquisa binária soluciona exatamente esse entrave. Mas o que seria de fato? nada mais é do que estarmos sempre dividindo o número de posições de uma lista por 2.
</p>
<p>
"Você escreveu e eu continuei sem entender". Então vamos pensar no seguinte, ao invés de começar chutando qualquer número vamos começar na metade da faixa, ou seja o número 50 considerando o número 99 esse chute seria baixo demais, então assim faríamos de novo o mesmo processo só que descartando todos os números antes do 50 pois se o 50 é baixo, eles são mais baixos ainda. Assim diminuímos as tentativas (chutes), até encontrarmos o número pensado por você.
</p>

<h3>Mas e como isso funciona na forma de algoritmos?</h3>
<p>
Todo algoritmo é um conjunto de instruções que realizam uma tarefa determinada, no nosso caso aqui é a pesquisa binária.
</p>
<p>
Sendo assim eu descrevi os passos para explicar melhor, através da linguagem python, o exemplo de um algortimo de pesquisa binária. Os passos estão descritos na forma de anotação do lado do código.
</p>
<p>
Passo #1:
    Criamos as variáveis baixo e alto para acompanhar a parte da faixa que estamos procurando
</p>
<p>
Passo #2:
    Entraremos nesse loop enquanto baixo é menor ou igual a alto
</p>
<p>
Passo #3:
    Verificaremos o elemento central (lembre-se do 50)
</p>
<p>
Passo #4:
    Se o chute for igual ao item (que seria o número pensado por você) retornamos a variavel meio que apontará para o endereço dentro dessa lista onde está o número pensado por você
</p>
<p>
Passo #5:
    Se o chute for maior que o item, atualizaremos a variável alto com o valor da variável meio menos 1 (alto = meio - 1)
</p>
<p>
Passo #6:
    Se o chute não satisfizer as condições impostas nos outros passos atualizaremos a variável baixo somando a variável meio mais 1 (baixo = meio + 1)
</p>
<p>
Passo #7:
    Caso o item não esteja dentro da lista (faixa) nós retornaremos None. Um exemplo disso seria eu pedir pra você pensar de 1 à 100 e você pensar em 1387482.
</p>
<p>
Passo #8:
    Aqui eu criei uma lista de números inteiros ordenados.
</p>
<p>
Passo #9:
    Imprime na tela a posição do número 9 na minha lista, no caso o número natural 4
</p>
<p>
Passo #10:
    Imprime na tela a posição do número -1 ou seja, será retornado o valor None pois não temos o número inteiro -1
</p>