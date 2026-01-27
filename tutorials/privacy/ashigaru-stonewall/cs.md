---
name: Ashigaru - Stonewall
description: Pochopení a používání transakcí Stonewall na Ashigaru
---
![cover stonewall](assets/cover.webp)



> *Prolomte předpoklady blockchainové analýzy pomocí matematicky prokazatelných pochybností mezi odesílatelem a příjemcem vašich transakcí.*

## Co je to transakce Stonewall?



Stonewall je specifická forma transakce Bitcoin, která má zvýšit důvěrnost uživatelů při utrácení tím, že napodobuje spojení dvou osob mincemi, aniž by jimi ve skutečnosti byla. Ve skutečnosti tato transakce není kooperativní. Uživatel si ji může sestavit sám, přičemž jako vstupní údaje použije pouze UTXO, které vlastní. Můžete tedy vytvořit transakci Stonewall pro jakoukoli příležitost, aniž byste se museli synchronizovat s jiným uživatelem.



Transakce Stonewall funguje následovně: emitent jako vstup do transakce použije 2 UTXO, které mu patří. Na straně výstupu transakce vytváří 4 výstupy, z nichž 2 mají přesně stejnou hodnotu. Zbylé 2 budou devizové. Ze dvou výstupů o stejné částce pouze jeden skutečně obdrží příjemce platby.



V transakci Stonewall jsou tedy pouze 2 role:




- Vydavatel, který provádí skutečnou platbu ;
- Příjemce, který si nemusí být vědom specifické povahy transakce a jednoduše očekává platbu od odesílatele.



Podívejme se na příklad, abychom tuto strukturu transakce pochopili. Alice je u pekaře, aby si koupila bagetu, která stojí `4 000 sats`. Chce zaplatit v bitcoinech, přičemž chce zachovat určitou formu důvěrnosti o své platbě. Rozhodne se tedy pro tuto platbu sestavit transakci Stonewall.



![image](assets/fr/01.webp)



Analýzou této transakce zjistíme, že pekař skutečně obdržel za bagetu 4 000 haléřů 6 haléřů. Alice použil jako vstupy 2 UTXO: jeden ve výši `10 000 sats` a druhý ve výši `15 000 sats`. Na straně výstupu získal zpět 3 UTXO: jeden ve výši `4 000 sats`, jeden ve výši `6 000 sats` a jeden ve výši `11 000 sats`. Alice má tedy z této transakce čistý zůstatek `- 4 000 sats`, což dobře odpovídá ceně bagety.



V tomto příkladu jsem záměrně zanedbal poplatky mining, aby byl příklad srozumitelnější. Ve skutečnosti nese transakční náklady výhradně emitent.



## Jaký je rozdíl mezi Stonewall a Stonewall x2?



Transakce Stonewall funguje stejně jako transakce StonewallX2 s tím rozdílem, že na rozdíl od klasické transakce Stonewall vyžaduje spolupráci, a proto se jmenuje "x2". Je to proto, že transakce Stonewall se provádí bez nutnosti vnější spolupráce: odesílatel ji může provést bez pomoci jiné osoby. Naproti tomu u transakce Stonewall x2 se k procesu připojuje další účastník, známý jako "spolupracovník". Ten do transakce přispívá vedle odesílatele i svými bitcoiny a na konci převezme celou částku (modulo mining náklady).



Vraťme se k našemu příkladu s Alice v pekárně. Pokud by chtěla provést transakci Stonewall x2, musela by Alice při jejím zadávání spolupracovat s Bob (třetí stranou). Každý z nich by si přivedl UTXO. Bob by pak dostala zpět celý svůj příspěvek. Pekař by obdržel platbu za svou bagetu stejným způsobem jako v případě transakce Stonewall, zatímco Alice by získala zpět svůj původní zůstatek snížený o cenu bagety.



![image](assets/fr/02.webp)



Z vnějšího pohledu by transakce zůstala naprosto stejná.



![image](assets/fr/03.webp)



Stručně řečeno, transakce Stonewall a Stonewall x2 mají stejnou strukturu. Rozdíl mezi nimi spočívá v jejich kolaborativní či nekolaborativní povaze. Transakce Stonewall je vyvíjena individuálně, bez nutnosti spolupráce. Naproti tomu transakce Stonewall x2 se při jejím vytváření spoléhá na spolupráci dvou jednotlivců.



[**-> Více informací o Stonewallských transakcích x2**](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Jaký je smysl transakce Stonewall?



Struktura Stonewall přidává do transakce obrovské množství entropie a rozmazává linie řetězové analýzy. Při pohledu zvenčí lze takovou transakci interpretovat jako malý coinjoin mezi dvěma lidmi. Ve skutečnosti se však stejně jako u transakce Stonewall x2 jedná o platbu. Tato metoda proto vytváří nejistoty v analýze řetězce, nebo dokonce vede k falešným stopám.



Vezměme si příklad Alice u pekaře. Transakce v blockchainu by vypadala takto:



![image](assets/fr/04.webp)



Vnější pozorovatel, který se spoléhá na běžnou heuristiku řetězové analýzy, by mohl chybně dojít k závěru, že "**dva lidé vytvořili malý coinjoin, každý s jedním UTXO jako vstupem a dvěma UTXO jako výstupem**".



![image](assets/fr/05.webp)



Tato interpretace je nepřesná, protože, jak víte, jeden UTXO byl odeslán pekaři, 2 příchozí UTXO přišly od Alice a ta získala zpět 3 kurzovní výstupy.



![image](assets/fr/01.webp)



I kdyby se vnějšímu pozorovateli podařilo identifikovat paterna Stonewallské transakce, nebude mít k dispozici všechny informace. Nebude schopen určit, kterému ze dvou UTXO stejných částek odpovídá platba. Kromě toho nebude schopen určit, zda obě zadaná UTXO pocházejí od dvou různých osob, nebo zda patří jedné osobě, která je sloučila. Tento poslední bod vyplývá ze skutečnosti, že výše zmíněné transakce Stonewall x2 se řídí přesně stejným vzorem jako transakce Stonewall. Při pohledu zvenčí a bez dalších kontextových informací není možné rozlišit mezi transakcí Stonewall a transakcí Stonewall x2. První z nich nejsou transakcemi spolupráce, zatímco druhé ano. To přidává k výdajům ještě více pochybností.



![image](assets/fr/03.webp)



## Jak mohu provést transakci Stonewall na Ashigaru?



Transakce Stonewall, původně vyvinuté týmem Samourai Wallet, byly převzaty aplikací Ashigaru, fork původního wallet vytvořeného po zatčení vývojářů Samourai. Musíte si nainstalovat Ashigaru a vytvořit wallet:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Na rozdíl od transakcí Stowaway nebo Stonewall x2 (*cahoots*) nevyžadují transakce Stonewall použití Paynyms. Lze je provádět přímo, bez předchozí přípravy nebo spolupráce s jiným uživatelem.



Ve skutečnosti k provádění kamenných transakcí nepotřebujete žádný návod, protože Ashigaru je generuje automaticky při každém utrácení, jakmile vaše wallet obsahuje dostatek UTXO.



Klikněte na tlačítko `+` v pravém dolním rohu obrazovky a poté vyberte možnost `Odeslat`.



![Image](assets/fr/06.webp)



Vyberte účet, ze kterého chcete provést výdaj.



![Image](assets/fr/07.webp)



Poté zadejte údaje o transakci: adresu příjemce a částku, která má být odeslána, a stiskněte šipku pro potvrzení.



![Image](assets/fr/08.webp)



Zde můžete samozřejmě upravit výchozí transakční poplatky podle podmínek na trhu. Nejzajímavějším prvkem na této stránce je však typ transakce. Všimněte si, že Ashigaru automaticky vybral `STONEWALL`. Kliknutím na tlačítko `PŘEHLED` se dozvíte více.



![Image](assets/fr/09.webp)



Vidíte, že transakce je skutečně typu Stonewall: skládá se ze 2 vstupů o stejné částce, 2 výstupů o stejné částce, jakož i z výstupů směny a v mém případě z dalšího vstupu, který uspokojí částku platby.



![Image](assets/fr/10.webp)



Pokud si nepřejete provést transakci Stonewall, ale dáváte přednost běžné platbě, klikněte na ikonu tužky v pravém horním rohu obrazovky a místo možnosti `STONEWALL` vyberte možnost `Jednoduchá`.



![Image](assets/fr/11.webp)



Jakmile zkontrolujete všechny údaje, přetáhněte zelenou šipku v dolní části obrazovky, čímž transakci podepíšete a uvolníte.



![Image](assets/fr/12.webp)



Nyní víte, jak provést transakci Stonewall, a co je důležitější, jak funguje. Pokud se chcete dozvědět více, podívejte se na můj návod na terminálu Ashigaru, který vysvětluje, jak provádět coinjoiny prostřednictvím Whirlpool.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add