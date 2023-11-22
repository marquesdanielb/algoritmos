<?php declare(strict_types=1);

function quicksort(array $arr) : array {
    if (count($arr) < 2) {
        return $arr;
    } else {
        $pivo = $arr[array_key_first($arr)];
        var_dump($arr);
        $menores = array_filter(array_slice($arr, 1), function($el) use ($pivo) { return $el <= $pivo; });
        $maiores = array_filter(array_slice($arr, 1), function($el) use ($pivo) { return $el > $pivo; });

        return array_merge(quicksort($menores), [$pivo], quicksort($maiores));
    }
}

var_dump(quicksort([10, 2, 5, 3]));
