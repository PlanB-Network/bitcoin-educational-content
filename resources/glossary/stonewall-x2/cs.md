---
term: STONEWALL X2

---
Specifická forma bitcoinové transakce, jejímž cílem je zvýšit soukromí uživatele během výdaje tím, že spolupracuje s třetí stranou, která se na výdaji nepodílí. Tato metoda simuluje minipřipojení mezi dvěma účastníky a zároveň provádí platbu třetí straně. Transakce Stonewall x2 jsou k dispozici jak v aplikaci Samourai Wallet, tak v softwaru Sparrow Wallet (obě aplikace jsou interoperabilní).

Jeho fungování je poměrně jednoduché: k provedení platby využívá UTXO v našem vlastnictví a požádá o pomoc třetí stranu, která rovněž přispěje UTXO, které vlastní. Transakce končí čtyřmi výstupy: dva ze stejných částek, z nichž jeden je určen na adresu příjemce platby, druhý na adresu patřící spolupracovníkovi. Třetí UTXO je odesláno zpět na jinou adresu spolupracovníka, což mu umožní získat zpět původní částku (pro něj neutrální akce, po odečtení poplatků za těžbu), a poslední UTXO se vrací na adresu, kterou vlastníme, což představuje změnu z platby. V transakcích Stonewall x2 jsou tedy definovány tři různé role:


- Odesílatel, který provádí platbu;
- Spolupracovník, který poskytne bitcoiny, aby zvýšil celkovou anonymitu transakce, přičemž na konci plně získá zpět své prostředky;
- Příjemce, který si nemusí být vědom konkrétní povahy transakce a jednoduše čeká na platbu od odesílatele.

![](../../dictionnaire/assets/3.webp)

Struktura Stonewall x2 přidává do transakce mnoho entropie a zamotává stopy řetězové analýzy. Zvenčí lze takovou transakci interpretovat jako malé spojení mincí mezi dvěma lidmi. Ve skutečnosti se však jedná o platbu. Tato metoda tak vytváří nejistoty v analýze řetězce, nebo dokonce vede k falešným stopám. I když se vnějšímu pozorovateli podaří identifikovat vzorec transakce Stonewall x2, nebude mít k dispozici všechny informace. Nebude schopen určit, který ze dvou UTXO stejných částek odpovídá platbě. Navíc nebude schopen zjistit, kdo platbu provedl. A konečně nebudou schopni určit, zda obě vstupní UTXO pocházejí od dvou různých osob, nebo zda patří jedné osobě, která je sloučila. Tento poslední bod je způsoben skutečností, že klasické transakce Stonewall se řídí přesně stejným vzorem jako transakce Stonewall x2. Zvenčí a bez dalších informací o kontextu není možné odlišit transakci Stonewall od transakce Stonewall x2. První z nich však nejsou transakcemi spolupráce, zatímco druhé ano. To ještě více zvyšuje pochybnosti o výdajích.