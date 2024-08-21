---
term: STONEWALL X2
---

Specifická forma Bitcoinové transakce zaměřená na zvýšení soukromí uživatele při platbě, a to spoluprací s třetí stranou, která se na výdaji nepodílí. Tato metoda simuluje mini-coinjoin mezi dvěma účastníky, zatímco provádí platbu třetí straně. Transakce Stonewall x2 jsou dostupné jak v aplikaci Samourai Wallet, tak v softwaru Sparrow Wallet (oba jsou interoperabilní).

Její provoz je relativně jednoduchý: používá UTXO v našem vlastnictví k provedení platby a vyhledá pomoc třetí strany, která také přispěje UTXO, které vlastní. Transakce končí se čtyřmi výstupy: dva z nich jsou ve stejných částkách, jeden je určen pro adresu příjemce platby, druhý pro adresu spolupracovníka. Třetí UTXO je odesláno zpět na další adresu spolupracovníka, což jim umožňuje získat zpět původní částku (neutrální akce pro ně, minus poplatky za těžbu), a poslední UTXO se vrací na adresu, kterou vlastníme, což představuje zbytek z platby. Tak jsou v transakcích Stonewall x2 definovány tři různé role:
* Odesílatel, který provádí efektivní platbu;
* Spolupracovník, který poskytuje bitcoiny k zlepšení celkové anonymity transakce, přičemž na konci plně získává zpět své prostředky;
* Příjemce, který nemusí být vědom specifické povahy transakce a jednoduše očekává platbu od odesílatele.

![](../../dictionnaire/assets/3.png)

Struktura Stonewall x2 přidává do transakce hodně entropie a zamotává stopy pro analýzu řetězce. Zvenčí může být taková transakce interpretována jako malý coinjoin mezi dvěma lidmi. Ve skutečnosti je to ale platba. Tato metoda tedy generuje nejistoty v analýze řetězce, nebo dokonce vede k falešným stopám. I když externí pozorovatel dokáže identifikovat vzor transakce Stonewall x2, nebude mít veškeré informace. Nebude moci určit, které z dvou UTXO ve stejných částkách odpovídá platbě. Navíc nebude moci vědět, kdo platbu provedl. Nakonec nebude moci určit, zda dvě vstupní UTXO pocházejí od dvou různých lidí, nebo zda patří jedné osobě, která je sloučila. Tento poslední bod je způsoben tím, že klasické transakce Stonewall sledují přesně stejný vzor jako transakce Stonewall x2. Zvenčí a bez dodatečných informací o kontextu je nemožné rozlišit transakci Stonewall od transakce Stonewall x2. Nicméně prvně jmenované nejsou kolaborativní transakce, zatímco druhé ano. To přidává ještě více pochybností o výdaji.