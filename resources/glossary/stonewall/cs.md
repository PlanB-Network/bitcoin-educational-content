---
term: STONEWALL

---
Specifická forma bitcoinové transakce, jejímž cílem je zvýšit soukromí uživatele během útraty tím, že napodobuje spojení mincí mezi dvěma lidmi, aniž by se ve skutečnosti jednalo o spojení. Tato transakce ve skutečnosti není kolaborativní. Uživatel ji může sestavit sám a jako vstupy do ní zapojit pouze své vlastní UTXO. Proto si můžete vytvořit transakci Stonewall pro jakoukoli příležitost, aniž byste se museli synchronizovat s jiným uživatelem.

Fungování transakce Stonewall je následující: na vstupu transakce odesílatel použije 2 UTXO, které mu patří. Transakce pak vytvoří 4 výstupy, z nichž 2 budou mít přesně stejnou hodnotu. Zbývající 2 budou tvořit změnu. Ze 2 výstupů o stejné částce půjde příjemci platby skutečně pouze jeden.

V transakci Stonewall tedy existují pouze 2 role:


- Odesílatel, který provádí skutečnou platbu;
- Příjemce, který si nemusí být vědom konkrétní povahy transakce a jednoduše čeká na platbu od odesílatele.

![](../../dictionnaire/assets/33.webp)

Transakce Stonewall jsou dostupné v aplikaci Samourai Wallet i v softwaru Sparrow Wallet.

Struktura Stonewall přidává do transakce mnoho entropie a znejasňuje stopu pro analýzu řetězce. Zvenčí lze takovou transakci interpretovat jako malé spojení mincí mezi dvěma lidmi. Ve skutečnosti se však stejně jako u transakce Stonewall x2 jedná o platbu. Tato metoda tak vytváří nejistoty při analýze řetězce, nebo dokonce vede k falešným stopám. I když se externímu pozorovateli podaří identifikovat vzorec Stonewallské transakce, nebude mít k dispozici všechny informace. Nebude schopen určit, který ze dvou UTXO stejných částek odpovídá platbě. Navíc nebude schopen určit, zda oba UTXO na vstupu pocházejí od dvou různých osob, nebo zda patří jedné osobě, která je sloučila. Tento poslední bod je způsoben skutečností, že transakce Stonewall x2 se řídí přesně stejným vzorem jako transakce Stonewall. Zvenčí a bez dalších kontextových informací není možné odlišit transakci Stonewall od transakce Stonewall x2. První z nich však nejsou transakcemi spolupráce, zatímco druhé ano. To ještě více zpochybňuje tento výdaj.