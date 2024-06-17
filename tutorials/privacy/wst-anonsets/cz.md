---
name: Whirlpool Stats Tools - Anonsets
description: Porozumění konceptu anonset a jak jej vypočítat s WST
---
![cover](assets/cover.webp)

***VAROVÁNÍ:** Po zatčení zakladatelů Samourai Wallet a zabavení jejich serverů 24. dubna již není nástroj Whirlpool Stats Tool dostupný ke stažení, jelikož byl hostován na Gitlabu Samourai. I když jste si tento nástroj dříve stáhli lokálně na svůj počítač, nebo byl nainstalován na vašem uzlu RoninDojo, WST v tuto chvíli nefunguje. Jeho provoz byl závislý na datech poskytovaných webem OXT.me, který již není přístupný. V současné době není WST zvlášť užitečný, protože protokol Whirlpool je neaktivní. Nicméně je možné, že tyto softwary budou v nadcházejících týdnech obnoveny. Navíc teoretická část tohoto článku zůstává relevantní pro pochopení principů a cílů coinjoinů obecně (nejen Whirlpool), stejně jako pro pochopení efektivity modelu Whirlpool. Můžete se také naučit, jak kvantifikovat soukromí poskytované cykly coinjoin.*

_Pozorně sledujeme vývoj této kauzy i vývoj souvisejících nástrojů. Ujistěte se, že tento tutoriál aktualizujeme, jakmile budou k dispozici nové informace._

_Tento tutoriál je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je zodpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

*"Přerušte stopu, kterou za sebou zanechávají vaše mince"*

V tomto tutoriálu se budeme zabývat konceptem anonsetů, ukazatelů, které nám umožňují odhadnout kvalitu procesu coinjoin na Whirlpool. Probereme metodu výpočtu a interpretaci těchto ukazatelů. Po teoretické části přejdeme k praxi tím, že se naučíme vypočítat anonsety konkrétní transakce pomocí Python nástroje *Whirlpool Stats Tools* (WST).

## Co je coinjoin na Bitcoinu?
**Coinjoin je technika, která narušuje sledovatelnost bitcoinů na blockchainu**. Spoléhá na spolupracující transakci se specifickou strukturou stejného názvu: transakci coinjoin.

Transakce coinjoin zvyšují soukromí uživatelů Bitcoinu tím, že komplikují analýzu řetězce pro vnější pozorovatele. Jejich struktura umožňuje sloučení více mincí od různých uživatelů do jediné transakce, čímž se zaměňují stopy a stává se obtížné určit vazby mezi vstupními a výstupními adresami.

Princip coinjoinu je založen na spolupracujícím přístupu: několik uživatelů, kteří si přejí smíchat své bitcoiny, vloží identické částky jako vstupy téže transakce. Tyto částky jsou poté redistribuovány ve výstupech ekvivalentní hodnoty. Na konci transakce se stává nemožným spojit konkrétní výstup s daným uživatelem. Mezi vstupy a výstupy neexistuje přímá vazba, čímž se přerušuje spojení mezi uživateli a jejich UTXO, stejně jako historie každé mince.

![coinjoin](assets/notext/1.webp)

Příklad transakce coinjoin:
[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)
Provedení coinjoinu při zajištění, že každý uživatel má neustále kontrolu nad svými prostředky, začíná konstrukcí transakce koordinátorem, který ji poté přenese každému účastníkovi. Každý uživatel poté transakci podepíše po ověření, že jim vyhovuje. Všechny shromážděné podpisy jsou nakonec integrovány do transakce. Pokud uživatel nebo koordinátor pokusí o přesměrování prostředků úpravou výstupů coinjoin transakce, podpisy se stanou neplatnými, což povede k zamítnutí transakce uzly.
Existuje několik implementací coinjoinu, jako jsou Whirlpool, JoinMarket nebo Wabisabi, každá s cílem řídit koordinaci mezi účastníky a zvýšit efektivitu transakcí coinjoin.
V tomto tutoriálu se zaměříme na mou oblíbenou implementaci: Whirlpool, která je dostupná na Samourai Wallet a Sparrow Wallet. Podle mého názoru je to nejefektivnější implementace pro coinjoins na Bitcoinu.
## Jaká je užitečnost coinjoinu na Bitcoinu?
Užitečnost coinjoinu spočívá v jeho schopnosti vytvářet pravděpodobnou zapření, tím že vaši minci "utopí" ve skupině nerozlišitelných mincí. Cílem této akce je přerušit sledovatelnost spojení, jak z minulosti do současnosti, tak z současnosti do minulosti.

Jinými slovy, analytik, který zná vaši počáteční transakci na vstupu do cyklů coinjoinu, by neměl být schopen s jistotou identifikovat vaše UTXO na výstupu z remixovacích cyklů (analýza od vstupu do cyklu po výstup z cyklu).

![coinjoin](assets/en/2.webp)

Naopak, analytik, který zná vaše UTXO na výstupu z cyklů coinjoinu, by neměl být schopen určit původní transakci na vstupu do cyklů (analýza od výstupu z cyklu po vstup do cyklu).

![coinjoin](assets/en/3.webp)

Pro posouzení obtížnosti analytika spojit minulost se současností a naopak je nutné kvantifikovat velikost skupin, ve kterých je vaše mince skryta. Toto měření nám říká počet analýz s identickou pravděpodobností. Takže pokud je správná analýza utopena mezi 3 dalšími analýzami stejné pravděpodobnosti, vaše úroveň skrytí je velmi nízká. Na druhou stranu, pokud je správná analýza v souboru 20 000 analýz, všechny stejně pravděpodobné, vaše mince je velmi dobře skryta.

A přesně velikost těchto skupin představuje ukazatele, které se nazývají "anonsety".

## Porozumění anonsetům
Anonsety slouží jako ukazatele pro hodnocení stupně soukromí konkrétního UTXO. Konkrétněji měří počet nerozlišitelných UTXO v souboru, který zahrnuje studovanou minci. Požadavek na homogenní soubor UTXO znamená, že anonsety jsou obvykle počítány přes cykly coinjoinu. Použití těchto ukazatelů je zvláště relevantní pro coinjoins Whirlpool kvůli jejich uniformitě.

Anonsety umožňují, je-li to vhodné, posoudit kvalitu coinjoinů. Velká velikost anonsetu znamená zvýšenou úroveň anonymity, protože se stává obtížnějším rozlišit konkrétní UTXO v souboru.

Existují dva typy anonsetů:
- **Prospective anonymity set;**
- **Retrospective anonymity set.**
První ukazatel ukazuje velikost skupiny, mezi kterou je studované UTXO skryto na konci cyklu, známe-li UTXO na vstupu, tj. počet nerozlišitelných mincí přítomných v této skupině. Tento ukazatel umožňuje měřit odolnost soukromí mince proti analýze z minulosti do současnosti (od vstupu po výstup). V angličtině se název tohoto ukazatele nazývá "forward anonset" nebo "forward-looking metrics".
![coinjoin](assets/en/4.webp)
Tento ukazatel odhaduje míru, do jaké je váš UTXO chráněn proti pokusům o rekonstrukci jeho historie od vstupního bodu po výstupní bod v procesu coinjoin.

Například, pokud vaše transakce participovala v jejím prvním cyklu coinjoin a byly dokončeny další dva následné cykly, očekávaný anonset vaší mince by byl `13`:

![coinjoin](assets/en/5.webp)

Druhý ukazatel ukazuje počet možných zdrojů pro danou minci, známe-li UTXO na konci cyklu. Tento ukazatel měří odolnost důvěrnosti mince proti analýze od současnosti do minulosti (od výstupu k vstupu), tedy jak obtížné je pro analytika vystopovat původ vaší mince před cykly coinjoin. V angličtině se název tohoto ukazatele nazývá "*backward anonset*", nebo "*backward-looking metrics*".

![coinjoin](assets/en/6.webp)

Znáte-li vaše UTXO na výstupu z cyklů, retrospektivní anonset určuje počet potenciálních transakcí Tx0, které by mohly tvořit váš vstup do cyklů coinjoin. Na níže uvedeném diagramu to odpovídá součtu všech oranžových bublin.

![coinjoin](assets/en/7.webp)

## Výpočet anonsetů s nástroji Whirlpool Stats Tools (WST)
Pro výpočet těchto ukazatelů na vašich vlastních mincích, které prošly cykly coinjoin, můžete použít nástroj speciálně vyvinutý společností Samourai Wallet: *Whirlpool Stats Tools*.

Pokud máte RoninDojo, WST je předinstalován na vašem uzlu. Můžete tedy přeskočit kroky instalace a přímo přejít k krokům použití. Pro ty, kteří nemají uzel RoninDojo, pojďme se podívat, jak postupovat při instalaci tohoto nástroje na počítač.

Budete potřebovat: Tor Browser (nebo Tor), Python 3.4.4 nebo vyšší, git a pip. Otevřete terminál. Pro kontrolu přítomnosti a verze těchto softwarů ve vašem systému zadejte následující příkazy:
```bash
python --version
git --version
pip --version
```

Pokud je potřeba, můžete je stáhnout z jejich příslušných webových stránek:
- https://www.python.org/downloads/ (pip je přímo součástí Pythonu od verze 3.4);
- https://www.torproject.org/download/;
- https://git-scm.com/downloads.
Jakmile jsou všechny tyto softwary nainstalovány, z terminálu naklonujte repozitář WST:
```bash
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```

![WST](assets/notext/8.webp)

Přejděte do adresáře WST:
```bash
cd whirlpool_stats
```

Nainstalujte závislosti:
```bash
pip3 install -r ./requirements.txt
```

![WST](assets/notext/9.webp)

Můžete je také nainstalovat ručně (volitelně):
```bash
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```

Přejděte do podadresáře `/whirlpool_stats`:
```bash
cd whirlpool_stats
```

Spusťte WST:
```bash
python3 wst.py
```

![WST](assets/notext/10.webp)

Spusťte Tor nebo Tor Browser na pozadí.

**-> Pro uživatele RoninDojo můžete pokračovat v tutoriálu přímo zde.**

Nastavte proxy na Tor (RoninDojo),
```bash
socks5 127.0.0.1:9050
```
nebo do Tor Browseru v závislosti na tom, co používáte:```bash
socks5 127.0.0.1:9150
```

Tato manipulace vám umožní stahovat data na OXT přes Tor, aby nedošlo k úniku informací o vašich transakcích. Pokud jste začátečník a tento krok se vám zdá složitý, vězte, že jde jednoduše o směrování vašeho internetového provozu přes Tor. Nejjednodušší metoda spočívá v spuštění Tor Browseru na pozadí vašeho počítače, a poté pouze spuštění druhého příkazu pro připojení přes tento prohlížeč (`socks5 127.0.0.1:9150`).

![WST](assets/notext/11.webp)

Dále přejděte do pracovního adresáře, ze kterého hodláte stahovat data WST pomocí příkazu `workdir`. Tato složka bude sloužit k ukládání transakčních dat, která získáte z OXT ve formě `.csv` souborů. Tyto informace jsou nezbytné pro výpočet indikátorů, které hledáte. Můžete si volně vybrat umístění tohoto adresáře. Mohlo by být rozumné vytvořit složku speciálně pro data WST. Jako příklad si zvolme složku pro stahování. Pokud používáte RoninDojo, tento krok není nutný:
```bash
workdir path/to/your/directory
```

Výzva příkazového řádku by poté měla změnit na zobrazení vašeho pracovního adresáře.

![WST](assets/notext/12.webp)

Poté stáhněte data z poolu obsahujícího vaši transakci. Například, pokud jsem v poolu `100,000 sats`, příkaz je:
```bash
download 0001
```

![WST](assets/notext/13.webp)

Kódy denominací na WST jsou následující:
- Pool 0.5 bitcoinů: `05`
- Pool 0.05 bitcoinů: `005`
- Pool 0.01 bitcoinů: `001`
- Pool 0.001 bitcoinů: `0001`
Jakmile jsou data stažena, načtěte je. Například, pokud jsem v poolu `100,000 sats`, příkaz je:
```bash
load 0001
```

Tento krok trvá několik minut v závislosti na vašem počítači. Nyní je dobrý čas si udělat kávu! :)

![WST](assets/notext/14.webp)

Po načtení dat zadejte příkaz `score` následovaný vaším TXID (identifikátorem transakce) pro získání jeho anonsetů:
```bash
score TXID
```

**Pozor**, výběr TXID pro použití se liší v závislosti na anonsetu, který chcete vypočítat. Pro posouzení budoucího anonsetu mince je nutné zadat, prostřednictvím příkazu `score`, TXID odpovídající jejímu prvnímu coinjoinu, což je počáteční mix provedený s tímto UTXO. Na druhou stranu, pro určení retrospektivního anonsetu, musíte zadat TXID posledního provedeného coinjoinu. Shrnutí, budoucí anonset je vypočítán z TXID prvního mixu, zatímco retrospektivní anonset je vypočítán z TXID posledního mixu.

WST poté zobrazí retrospektivní skóre (*Backward-looking metrics*) a budoucí skóre (*Forward-looking metrics*). Například, vzal jsem TXID náhodné mince na Whirlpool, která mi nepatří.

![WST](assets/notext/15.webp)
Transakce v otázce: [7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)
Pokud tuto transakci považujeme za první coinjoin provedený pro danou minci, pak má potenciální anonset `86,871`. To znamená, že je skryta mezi `86,871` nerozlišitelnými mincemi. Pro vnějšího pozorovatele, který tuto minci zná na začátku cyklů coinjoin a pokusí se sledovat její výstup, bude čelit `86,871` možným UTXO, každé s identickou pravděpodobností, že jde o hledanou minci.

Pokud tuto transakci považujeme za poslední coinjoin mince, pak má retrospektivní anonset `42,185`. To znamená, že existuje `42,185` potenciálních zdrojů pro toto UTXO. Pokud vnější pozorovatel identifikuje tuto minci na konci cyklů a snaží se vystopovat její původ, bude čelit `42,185` možným zdrojům, všechny s rovnou pravděpodobností, že jde o hledaný původ.
Kromě skóre anonsetu WST vám také poskytuje míru rozptýlení vašeho výstupu v rámci poolu na základě anonsetu. Tento další ukazatel jednoduše umožňuje posoudit potenciál pro zlepšení vaší mince. Tato míra je obzvláště užitečná pro potenciální anonset. Skutečně, pokud má vaše mince míru rozptýlení 15%, znamená to, že může být zaměněna s 15% mincí v poolu. To je dobré, ale stále máte velkou marži pro zlepšení pokračováním v remixování. Na druhou stranu, pokud má vaše mince míru rozptýlení 95%, pak se blížíte limitům poolu. Můžete pokračovat v remixování, ale váš anonset se už mnoho nezvýší.

Je důležité poznamenat, že anonsety vypočítané WST nejsou zcela přesné. Vzhledem k obrovskému objemu dat, která je třeba zpracovat, WST používá algoritmus *HyperLogLogPlusPlus* k výraznému snížení zátěže spojené s lokálním zpracováním dat a potřebnou pamětí. Jedná se o algoritmus, který umožňuje odhadovat počet rozlišitelných hodnot ve velmi velkých datech s vysokou přesností výsledku. Proto jsou poskytnutá skóre dostatečně dobrá pro použití ve vašich analýzách, jelikož jsou velmi blízká odhady reality, ale neměla by být interpretována jako přesné hodnoty do jednotky.

Závěrem mějte na paměti, že není nezbytné systematicky vypočítávat anonsety pro každou vaši minci v coinjoinech. Samotný design Whirlpoolu již poskytuje záruky. Skutečně, retrospektivní anonset je zřídka důvodem k obavám. Od vašeho počátečního míchání získáváte obzvláště vysoké retrospektivní skóre díky dědictví předchozích míchání od Genesis coinjoinu. Co se týče potenciálního anonsetu, stačí udržet vaši minci na účtu po míchání dostatečně dlouhou dobu.
To je důvod, proč považuji použití Whirlpool za zvláště relevantní v strategii *Hodl -> Mix -> Spend -> Replace* (Držet -> Míchat -> Utrácet -> Nahradit). Podle mého názoru je nejlogičtější přístup uchovávat většinu úspor v bitcoinech v studené peněžence, zatímco neustále udržovat určitý počet kusů v coinjoins na Samourai pro pokrytí denních výdajů. Jakmile jsou bitcoiny z coinjoins utraceny, jsou nahrazeny novými, aby se vrátily na definovanou hranici smíšených kusů. Tato metoda umožňuje osvobodit se od starostí o naše UTXO anonsety, zatímco činí čas potřebný pro účinnost coinjoins mnohem méně omezujícím.
**Externí zdroje:**

- [Podcast ve francouzštině o analýze řetězců](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [Wikipedie článek o HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog)
- Samouraiho repozitář pro statistiky Whirlpool
- Webová stránka Whirlpool od Samourai
- [Článek na Medium v angličtině o soukromí a Bitcoinu od Samourai](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [Článek na Medium v angličtině o konceptu anonymity set od Samourai](https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7)