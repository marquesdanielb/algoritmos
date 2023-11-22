<?php declare(strict_types=1);

function regressiva(int $i) : int|null {
    echo $i.PHP_EOL;
    if ($i <= 1) {
        return null;
    } else {
        return regressiva($i-1);
    }
}

function fat(int $i) : int {
    if ($i === 1) {
        return 1;
    } else {
        return $i * fat($i-1);
    }
}

regressiva(10);
echo fat(3).PHP_EOL;