---
term: CÍL OBTÍŽNOSTI

---
Faktor obtížnosti, známý také jako cíl obtížnosti, je parametr používaný v mechanismu konsensu pomocí důkazu práce (Proof of Work, PoW) v Bitcoinu. Cíl představuje číselnou hodnotu, která určuje obtížnost řešení konkrétního kryptografického problému, tzv. důkazu práce, pro těžaře při vytváření nového bloku v blockchainu.

Cílová hodnota obtížnosti je nastavitelné 256bitové číslo (64 bajtů), které určuje hranici přijatelnosti pro hašování hlaviček bloků. Jinými slovy, aby byl blok platný, musí být hash jeho hlavičky pomocí `SHA256d` (double `SHA256`) číselně nižší nebo roven cíli obtížnosti. Důkaz práce spočívá v úpravě pole `nonce` v hlavičce bloku nebo transakce coinbase, dokud výsledný hash není nižší než cílová hodnota.

Tento cíl se upravuje každých 2016 bloků (přibližně každé dva týdny) během akce zvané "úprava" Koeficient obtížnosti se přepočítává na základě doby, kterou trvalo vytěžit předchozí bloky roku 2016. Pokud je celkový čas kratší než dva týdny, obtížnost se zvýší úpravou cíle směrem dolů. Pokud je celkový čas delší než dva týdny, obtížnost se sníží úpravou cíle směrem nahoru. Cílem je udržet průměrnou dobu těžby 10 minut na blok. Tato doba mezi jednotlivými bloky pomáhá zabránit rozdělení bitcoinové sítě, což vede k plýtvání výpočetním výkonem. Cílová hodnota obtížnosti se nachází v záhlaví každého bloku v poli `nBits`. Protože je toto pole zmenšeno na 32 bitů a cíl je ve skutečnosti 256 bitů, je cíl zhuštěn do méně přesného vědeckého formátu.

![](../../dictionnaire/assets/34.webp)

> ► Cílová obtížnost se někdy nazývá také "faktor obtížnosti" V záhlaví bloků se může označovat termínem "nBits".*