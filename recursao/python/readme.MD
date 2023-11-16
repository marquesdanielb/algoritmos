<h1>Então o que seria uma recursão?</h1>
<p>
Recursão é quando uma função chama a si mesma. Toda função recursiva tem dois casos: o caso-base e o caso-recursivo.
</p>
<p>
Um exemplo? Você conhece o  termo matemático <i>fatorial</i>? Se não conhece vou tentar dar uma rápida explicação sobre o que é: Imagine que queremos calcular todos os números anteriores ao número 3 com excessão do 0 ou seja o cálculo seria 3x2x1 que teria o resultado igual a 6. Calcular o fatorial de um número nada mais é do que a multiplicação desse número <b>n</n> (3) pelos seus antecessores (que vieram antes) maiores ou iguais a um.
</p>
<p>
É ai que entra o algoritmo de recursão. Quando calculamos o fatorial estamos sempre calculando o resultado de uma expressão com a outra. Nos exemplos de códigos tive a oportunidade de escrever duas funções com códigos distintos porém utilizando a recursão para o resultado esperado.
</p>
<p>
#1: Regressiva
Na primeira função, que eu dei o nome de regressiva, nós temos uma variável i que é impressa no console e conferida se o valor de i é menor ou igual a um, caso seja igual a um ou menor ele retorna o valor None. Caso não retornará a função regressiva com o valor de i - 1
</p>
<p>
#2: Fat
Assim como eu já tinha explicado, essa função exemplifica em código python o cálculo de um número fatorial x e confere se o x for igual a  1, a função retornará None caso não retornará a multiplicação entre x e chamará a função novamento com o valor de x - 1.
</p>
