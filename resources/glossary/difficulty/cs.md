---
term: OBTÍŽNOST
---

Nastavitelný parametr, který určuje složitost důkazu práce potřebného pro přidání nového bloku do blockchainu a získání přidružené odměny. Tato obtížnost je reprezentována cílem obtížnosti, 256bitovou hodnotou, která stanovuje horní limit, kterého musí hash hlavičky bloku dosáhnout, aby byl považován za platný. Cílem je, aby hash, dosažený dvojitým provedením SHA256 (SHA256d), byl menší nebo roven tomuto cíli. Aby těžaři dosáhli tohoto hash, manipulují s `nonce` v hlavičce bloku. Obtížnost se upravuje každých 2016 bloků, nebo přibližně každé dva týdny, aby se udržel průměrný čas vytváření bloku na přibližně 10 minut.