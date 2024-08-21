---
term: STONEWALL
---

Specifický typ Bitcoinové transakce zaměřený na zvýšení soukromí uživatele při platbě tím, že napodobuje coinjoin mezi dvěma lidmi, aniž by to ve skutečnosti byl. Tato transakce není kolaborativní. Uživatel ji může sestavit sám, zapojuje do ní pouze své vlastní UTXO jako vstupy. Tedy, Stonewall transakci můžete vytvořit pro jakoukoliv příležitost, bez nutnosti synchronizace s jiným uživatelem.

Funkce Stonewall transakce je následující: na vstupu transakce odesílatel použije 2 UTXO, které mu patří. Transakce poté vyprodukuje 4 výstupy, z nichž 2 budou přesně stejné částky. Ostatní 2 budou tvořit zbytek. Mezi 2 výstupy stejné částky, pouze jeden skutečně půjde příjemci platby.

Takže existují pouze 2 role ve Stonewall transakci:
* Odesílatel, který provede skutečnou platbu;
* Příjemce, který nemusí být vědom specifické povahy transakce a jednoduše očekává platbu od odesílatele.

![](../../dictionnaire/assets/33.png)
Stonewall transakce jsou dostupné jak v aplikaci Samourai Wallet, tak v softwaru Sparrow Wallet.

Struktura Stonewall přidává do transakce hodně entropie a ztěžuje sledování pro analýzu blockchainu. Zvenčí může být taková transakce interpretována jako malý coinjoin mezi dvěma lidmi. Ale ve skutečnosti, stejně jako transakce Stonewall x2, jde o platbu. Tato metoda tedy generuje nejistoty v analýze blockchainu, nebo dokonce vede k falešným stopám. I když externí pozorovatel dokáže identifikovat vzor Stonewall transakce, nebudou mít veškeré informace. Nejsou schopni určit, které z dvou UTXO stejných částek odpovídá platbě. Navíc nebudou schopni určit, zda dvě UTXO na vstupu pocházejí od dvou různých lidí, nebo zda patří jediné osobě, která je sloučila. Tento poslední bod je způsoben tím, že transakce Stonewall x2 následují přesně stejný vzor jako Stonewall transakce. Zvenčí a bez dodatečných kontextových informací je nemožné rozlišit Stonewall transakci od transakce Stonewall x2. Nicméně, prvně jmenované nejsou kolaborativní transakce, zatímco ty druhé ano. To přidává ještě více pochybností o této výdaji.