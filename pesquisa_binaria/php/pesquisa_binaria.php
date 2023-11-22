<?php declare(strict_types=1);

function pesquisa_binaria(array $lista, int $item): int|null 
{
    $baixo = 0;
    $alto = count($lista) - 1;

    while ($baixo <= $alto) {
        $meio = (int) (($baixo + $alto) / 2);
        $chute = $lista[$meio];
        
        if ($chute == $item) {
            return $meio;
        }

        if ($chute > $item) {
            $alto = $meio - 1;
        } else {
            $baixo = $meio + 1;
        }
    }

    return null;
}

$minha_lista = [2, 4, 6, 23, 55];
$resultado_pesquisa = pesquisa_binaria($minha_lista, 6);

var_dump($resultado_pesquisa);
