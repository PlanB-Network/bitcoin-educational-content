---
term: Blocks/rev*.dat

definition: Soubory uchovávající data pro zrušení změn (undo data), která umožňují návrat k předchozímu stavu sady UTXO.
---
Název souborů v jádře bitcoinu, které uchovávají informace potřebné k potenciálnímu zvrácení změn provedených v sadě UTXO dříve přidanými bloky. Každý soubor je identifikován jedinečným číslem, které je stejné jako číslo souboru blk*.dat, kterému odpovídá. Soubory rev*.dat obsahují reverzní data odpovídající blokům uloženým v souborech blk*.dat. Tato data jsou v podstatě seznamem všech UTXO použitých jako vstupy v bloku. Tyto reverzní soubory umožňují uzlu vrátit se do předchozího stavu v případě reorganizace blockchainu, která způsobí vyřazení dříve validovaných bloků.