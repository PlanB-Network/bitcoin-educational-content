---
name: Sparrow Wallet - Stonewall
description: Porozumění a používání transakcí Stonewall v systému Sparrow
---

![cover](assets/cover.webp)




> *Prolomte předpoklady blockchainové analýzy pomocí matematicky prokazatelných pochybností mezi odesílatelem a příjemcem vašich transakcí.*

## Co je to transakce Stonewall?



Stonewall je specifická forma transakce Bitcoin, která má zvýšit důvěrnost uživatelů při utrácení tím, že imituje spojení dvou osob mincemi, aniž by se ve skutečnosti jednalo o spojení dvou osob. Ve skutečnosti tato transakce není kooperativní. Uživatel si ji může sestavit sám, přičemž jako vstupní údaje použije pouze UTXO, které mu patří. Můžete tedy vytvořit transakci Stonewall pro jakoukoli příležitost, aniž byste se museli synchronizovat s jiným uživatelem.



Transakce Stonewall funguje následovně: emitent jako vstup do transakce použije 2 UTXO, které mu patří. Na straně výstupu transakce vytváří 4 výstupy, z nichž 2 mají přesně stejnou hodnotu. Zbylé 2 budou devizové. Ze dvou výstupů o stejné částce pouze jeden skutečně obdrží příjemce platby.



V transakci Stonewall jsou tedy pouze 2 role:




- Vydavatel, který provádí skutečnou platbu ;
- Příjemce, který si nemusí být vědom specifické povahy transakce a jednoduše očekává platbu od odesílatele.



Podívejme se na příklad, abychom tuto strukturu transakce pochopili. Alice je u pekaře, aby si koupila bagetu, která stojí `4 000 sats`. Chce zaplatit v bitcoinech, přičemž chce zachovat určitou formu důvěrnosti o své platbě. Rozhodne se tedy pro tuto platbu sestavit transakci Stonewall.



![image](assets/fr/01.webp)



Analýzou této transakce zjistíme, že pekař skutečně obdržel za bagetu 4 000 sats. Alice použil jako vstupy 2 UTXO: jeden ve výši `10 000 sats` a druhý ve výši `15 000 sats`. Na výstupu získala 3 UTXO: jeden ve výši `4 000 sats`, jeden ve výši `6 000 sats` a jeden ve výši `11 000 sats`. Alice má tedy z této transakce čistý zůstatek `- 4 000 sats`, což dobře odpovídá ceně bagety.



V tomto příkladu jsem záměrně zanedbal poplatky mining, aby byl příklad srozumitelnější. Ve skutečnosti nese transakční náklady výhradně emitent.



## Jaký je rozdíl mezi Stonewall a Stonewall x2?



Transakce Stonewall funguje stejně jako transakce StonewallX2 s tím rozdílem, že na rozdíl od klasické transakce Stonewall vyžaduje spolupráci, a proto se jmenuje "x2". Je to proto, že transakce Stonewall se provádí bez nutnosti vnější spolupráce: odesílatel ji může provést bez pomoci jiné osoby. Naproti tomu u transakce Stonewall x2 se k procesu připojuje další účastník, známý jako "spolupracovník". Ten do transakce přispívá vedle odesílatele i vlastními bitcoiny a na konci převezme celou částku (po odečtení nákladů mining).



Vraťme se k našemu příkladu s Alice v pekárně. Pokud by chtěla provést transakci Stonewall x2, musela by Alice při jejím zadávání spolupracovat s Bob (třetí stranou). Každý z nich by si přivedl UTXO. Bob by pak při odchodu obdržel plnou výši svého příspěvku. Pekař by obdržel platbu za svou bagetu stejným způsobem jako v transakci Stonewall, zatímco Alice by získala zpět svůj počáteční zůstatek snížený o náklady na bagetu.



![image](assets/fr/02.webp)



Z pohledu nezúčastněné strany by transakce zůstala naprosto stejná.



![image](assets/fr/03.webp)



Stručně řečeno, transakce Stonewall a Stonewall x2 mají stejnou strukturu. Rozdíl mezi nimi spočívá v jejich kolaborativní či nekolaborativní povaze. Transakce Stonewall je vyvíjena individuálně, bez nutnosti spolupráce. Naproti tomu transakce Stonewall x2 se při jejím vytváření spoléhá na spolupráci dvou jednotlivců.



[**-> Více informací o Stonewallských transakcích x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Jaký je smysl transakce Stonewall?



Struktura Stonewall přidává do transakce obrovské množství entropie a rozmazává linie řetězové analýzy. Při pohledu zvenčí lze takovou transakci interpretovat jako malý coinjoin mezi dvěma lidmi. Ve skutečnosti se však stejně jako u transakce Stonewall x2 jedná o platbu. Tato metoda proto vytváří nejistoty v analýze řetězce, nebo dokonce vede k falešným stopám.



Vezměme si příklad Alice u pekaře. Transakce v blockchainu by vypadala takto:



![image](assets/fr/04.webp)



Vnější pozorovatel, který se spoléhá na běžnou heuristiku řetězové analýzy, by mohl chybně dojít k závěru, že "*dva lidé vytvořili malý coinjoin, přičemž každý z nich má na vstupu jeden UTXO a na výstupu dva UTXO*".



![image](assets/fr/05.webp)



Tato interpretace je nepřesná, protože, jak víte, jeden UTXO byl poslán do pekárny, 2 příchozí UTXO přišly z Alice a ona získala 3 výměnné výstupy.



![image](assets/fr/01.webp)



I kdyby se vnějšímu pozorovateli podařilo identifikovat paterna Stonewallské transakce, nebude mít k dispozici všechny informace. Nebude schopen určit, kterému ze dvou UTXO stejných částek odpovídá platba. Kromě toho nebude schopen určit, zda oba záznamy UTXO pocházejí od dvou různých osob, nebo zda patří jedné osobě, která je sloučila. Tento poslední bod je způsoben skutečností, že výše zmíněné transakce Stonewall x2 se řídí přesně stejným vzorem jako transakce Stonewall. Při pohledu zvenčí a bez dalších kontextových informací není možné rozlišit mezi transakcí Stonewall a transakcí Stonewall x2. První z nich nejsou transakcemi spolupráce, zatímco druhé ano. To přidává k výdajům ještě více pochybností.



![image](assets/fr/03.webp)



## Jak mohu provést transakci Stonewall na Sparrow?



Původně vyvinutý týmem Samurai Wallet, transakce Stonewall byly převzaty aplikací Ashigaru, fork z původního portfolia vytvořeného po zatčení vývojářů Samurai, a také na Sparrow Wallet.



Je třeba nainstalovat Sparrow a vytvořit :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Na rozdíl od transakcí Stowaway nebo Stonewall x2 (*cahoots*) nevyžadují transakce Stonewall použití Paynyms. Lze je provádět přímo, bez zvláštní přípravy nebo spolupráce s jiným uživatelem.



Provedení transakce Stonewall na Sparrow je velmi jednoduché: začněte vytvořením transakce jako obvykle, a to buď prostřednictvím nabídky `Odeslat`, nebo z nabídky `UTXOs`, pokud chcete provést *Coin Control*.



![Image](assets/fr/06.webp)



Poté zadejte údaje o transakci: adresu příjemce, štítek, částku k odeslání a výši nebo sazbu poplatků v závislosti na tržních podmínkách.



![Image](assets/fr/07.webp)



Před potvrzením můžete vybrat strukturu Stonewall. V dolní části rozhraní nahraďte položku `Efektivita` položkou `Soukromí`. Pokud se tato možnost nezobrazí, znamená to, že vaše portfolio nemá dostatečný počet UTXO pro sestavení tohoto typu transakce.



![Image](assets/fr/08.webp)



Po výběru možnosti `Soukromí` si všimnete, že se struktura transakce zcela změní: stane se z ní Stonewallská transakce, která spotřebuje několik vašich UTXO jako vstupy a vytvoří dva výstupy o stejných částkách, z nichž jeden odpovídá skutečné platbě `100 000 sats`, navíc k výstupům směny.



![Image](assets/fr/09.webp)



Pokud je vše v pořádku, klikněte na `Vytvořit transakci`.



Poté můžete naposledy zkontrolovat údaje o transakci a kliknout na `Finalizovat transakci pro podpis`.



![Image](assets/fr/10.webp)



Poté podepište transakci podle metody specifické pro vaše portfolio a kliknutím na `Vysílat transakci` ji odvysílejte v síti Bitcoin a vyčkejte na potvrzení.



![Image](assets/fr/11.webp)



Nyní víte, jak transakce Stonewall v systému Sparrow Wallet funguje a jak ji vytvořit. Chcete-li prohloubit své mistrovství v těchto nástrojích určených k posílení důvěryhodnosti onchainu, zvu vás na mé školení BTC 204 na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c