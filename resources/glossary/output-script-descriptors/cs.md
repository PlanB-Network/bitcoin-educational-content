---
term: DESKRIPTORY VÝSTUPNÍHO SKRIPTU

---
Deskriptory výstupních skriptů nebo jednoduše deskriptory jsou strukturované výrazy, které plně popisují výstupní skript (`scriptPubKey`) a poskytují všechny potřebné informace pro sledování transakcí do nebo z konkrétního skriptu. Tyto deskriptory usnadňují správu klíčů v peněženkách HD prostřednictvím standardního popisu struktury a typů použitých adres.

Hlavní zajímavost deskriptorů spočívá v jejich schopnosti zahrnout všechny podstatné informace pro obnovení peněženky do jediného řetězce (kromě fráze pro obnovení). Uložením deskriptoru s příslušnými mnemotechnickými frázemi lze obnovit nejen soukromé klíče, ale také přesnou strukturu peněženky a související parametry skriptu. Obnovení peněženky totiž vyžaduje nejen znalost počátečního seedu, ale také specifických indexů pro odvození párů podřízených klíčů a také `xpub` každého faktoru v případě vícesignátové peněženky. Dříve se předpokládalo, že tyto informace jsou implicitně známy všem. S diverzifikací skriptů a vznikem složitějších konfigurací by se však tyto informace mohly stát obtížně extrapolovatelnými, čímž by se z těchto údajů staly soukromé a těžko vymahatelné informace. Použití deskriptorů tento proces výrazně zjednodušuje: stačí znát frázi (fráze) pro obnovu a odpovídající deskriptor, aby bylo vše spolehlivě a bezpečně obnoveno.

Deskriptor se skládá z několika prvků:


- Skriptovací funkce jako `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature) a `sortedmulti` (Multisignature s tříděnými klíči);
- Odvozené cesty, například `[d34db33f/44h/0h/0h]` označující odvozenou cestu a konkrétní otisk hlavního klíče;
- Klíče v různých formátech, například hexadecimální veřejné klíče nebo rozšířené veřejné klíče (`xpub`);
- Kontrolní součet, kterému předchází hash, pro ověření integrity deskriptoru.

Deskriptor pro peněženku P2WPKH může vypadat například takto:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

V tomto deskriptoru označuje odvozovací funkce `wpkh` typ skriptu Pay-to-Witness-Public-Key-Hash. Za ní následuje odvozovací cesta, která obsahuje:


- `cdeab12f`: otisk hlavního klíče;
- `84h`: znamená použití účelu BIP84, určeného pro adresy SegWit v0;
- `0h`: což znamená, že se jedná o měnu BTC v hlavní síti;
- `0h`: odkazuje na konkrétní číslo účtu používané v peněžence.

Deskriptor obsahuje také rozšířený veřejný klíč použitý v této peněžence:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Dále zápis `/<0;1>/*` určuje, že deskriptor může generovat adresy z vnějšího (`0`) a vnitřního (`1`) řetězce, přičemž zástupný znak (`*`) umožňuje postupné odvození více adres konfigurovatelným způsobem, podobně jako při řízení "limitu mezer" v tradičním softwaru peněženek.

A konečně `#jy0l7nr4` představuje kontrolní součet pro ověření integrity deskriptoru.