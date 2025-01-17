---
term: DIFFICULTY

---
Nastavitelný parametr, který určuje složitost důkazu práce potřebného k přidání nového bloku do blockchainu a získání související odměny. Tato obtížnost je reprezentována cílovou hodnotou obtížnosti, což je 256bitová hodnota, která určuje horní hranici, kterou musí hash hlavičky bloku splňovat, aby byl považován za platný. Cílem je, aby hodnota hashe, dosažená dvojím provedením algoritmu SHA256 (SHA256d), byla menší nebo rovna této cílové hodnotě. Aby těžaři dosáhli této hodnoty, manipulují s hodnotou `nonce` v záhlaví bloku. Obtížnost se upravuje každých 2016 bloků, tedy přibližně každé dva týdny, aby se udržovala průměrná doba vytvoření bloku přibližně 10 minut.