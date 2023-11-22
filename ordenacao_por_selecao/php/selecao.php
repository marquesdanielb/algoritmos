<?php declare(strict_types=1);

function busca_menor(array $arr): int {
    $menor = $arr[0];
    $menorIndice = 0;

    for ($i=0; $i < count($arr); $i++) { 
        if ($arr[$i] < $menor) {
            $menor = $arr[$i];
            $menorIndice = $i;
        }
    }

    return $menorIndice;
}

function ordenar_por_selecao(array $arr): array {
    $novoArr = [];
    for ($i=0; $i < count($arr); $i++) { 
        $menor = busca_menor($arr);
        array_push($novoArr, array_splice($arr, $menor, 1)[0]);
    }

    return $novoArr;
}

$selecao = ordenar_por_selecao([5, 3, 6, 13, 10]);
