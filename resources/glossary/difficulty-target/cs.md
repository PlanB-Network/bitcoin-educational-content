---
term: CÍLOVÁ OBTÍŽNOST
---

Faktor obtížnosti, známý také jako cílová obtížnost, je parametr používaný v konsenzuálním mechanismu proof of work (Důkaz práce, PoW) u Bitcoinu. Tento cíl představuje číselnou hodnotu, která určuje obtížnost pro těžaře vyřešit specifický kryptografický problém, nazývaný důkaz práce, při vytváření nového bloku na blockchainu.

Cílová obtížnost je nastavitelné 256bitové (64 bajtů) číslo určující limit přijatelnosti pro hashování hlaviček bloků. Jinými slovy, aby byl blok platný, hash jeho hlavičky s `SHA256d` (dvojitý `SHA256`) musí být číselně nižší nebo roven cílové obtížnosti. Důkaz práce spočívá v modifikaci pole `nonce` v hlavičce bloku nebo transakce coinbase, dokud výsledný hash není nižší než cílová hodnota.

Tento cíl se upravuje každých 2016 bloků (přibližně každé dva týdny) během události nazývané "úprava". Faktor obtížnosti se přepočítává na základě času, který trvalo vytěžit předchozích 2016 bloků. Pokud je celkový čas kratší než dva týdny, obtížnost se zvyšuje úpravou cíle směrem dolů. Pokud je celkový čas delší než dva týdny, obtížnost se snižuje úpravou cíle směrem nahoru. Cílem je udržet průměrný čas těžby 10 minut na blok. Tento čas mezi jednotlivými bloky pomáhá zabránit rozdělení sítě Bitcoin, což by vedlo k plýtvání výpočetním výkonem. Cílová obtížnost se nachází v každé hlavičce bloku, v poli `nBits`. Jelikož je toto pole redukováno na 32 bitů a cíl je ve skutečnosti 256 bitů, cíl je zkomprimován do méně přesného vědeckého formátu.

![](../../dictionnaire/assets/34.png)

> ► *Cílová obtížnost je někdy také nazývána "faktor obtížnosti". Rozšířeně se může odkazovat na její kódování v hlavičkách bloků termínem "nBits".*