---
term: POPISY SKRIPTŮ VÝSTUPU
---

Popisy skriptů výstupu, nebo jednoduše popisy, jsou strukturované výrazy, které plně popisují výstupní skript (`scriptPubKey`) a poskytují veškeré nezbytné informace pro sledování transakcí do nebo z konkrétního skriptu. Tyto popisy usnadňují správu klíčů v HD peněženkách prostřednictvím standardního popisu struktury a typů použitých adres.

Hlavní výhoda popisů spočívá v jejich schopnosti zahrnout veškeré zásadní informace pro obnovení peněženky do jediného řetězce (kromě obnovovací fráze). Uložením popisu spolu s odpovídajícími mnemonickými frázemi je možné obnovit nejen soukromé klíče, ale také přesnou strukturu peněženky a přidružené parametry skriptu. Skutečně, obnovení peněženky vyžaduje nejen znalost počátečního seedu, ale také specifické indexy pro derivaci dětských párů klíčů, stejně jako `xpub` každého faktoru v případě multisig peněženky. Dříve se předpokládalo, že tyto informace jsou implicitně známy všem. Nicméně, s diverzifikací skriptů a vznikem složitějších konfigurací, mohou se tyto informace stát obtížně extrapolovatelnými, čímž se tyto údaje promění v soukromé a těžko prolomitelné informace. Použití popisů výrazně zjednodušuje proces: stačí znát obnovovací frázi(e) a odpovídající popis pro spolehlivé a bezpečné obnovení všeho.

Popis se skládá z několika prvků:
* Funkce skriptu jako `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignatura) a `sortedmulti` (Multisignatura se seřazenými klíči);
* Cesty derivace, například `[d34db33f/44h/0h/0h]` označující odvozenou cestu a specifický otisk hlavního klíče;
* Klíče v různých formátech, jako jsou hexadecimální veřejné klíče nebo rozšířené veřejné klíče (`xpub`);
* Kontrolní součet, předcházený hashem, pro ověření integrity popisu.

Například popis pro peněženku P2WPKH by mohl vypadat takto:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```
V tomto popisu funkce derivace `wpkh` označuje typ skriptu Pay-to-Witness-Public-Key-Hash. Následuje cesta derivace, která obsahuje:
* `cdeab12f`: otisk hlavního klíče;
* `84h`: což značí použití účelu BIP84, určeného pro adresy SegWit v0;
* `0h`: což označuje, že se jedná o měnu BTC na hlavní síti;
* `0h`: což odkazuje na konkrétní číslo účtu použitého v peněžence.

Popis také zahrnuje rozšířený veřejný klíč použitý v této peněžence:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U

Dále, notace `/<0;1>/*` specifikuje, že deskriptor může generovat adresy z vnější (`0`) a vnitřní (`1`) řady, s použitím zástupného symbolu (`*`), což umožňuje sekvenční derivaci více adres v konfigurovatelným způsobem, podobně jako správa "mezery limitu" v tradičním softwaru peněženky.

Nakonec, `#jy0l7nr4` představuje kontrolní součet pro ověření integrity deskriptoru.