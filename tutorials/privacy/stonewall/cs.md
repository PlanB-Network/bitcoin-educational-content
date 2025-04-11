---
name: Stonewall
description: Porozumění a používání transakcí Stonewall
---
![cover stonewall](assets/cover.webp)

***VAROVÁNÍ:** Po zatčení zakladatelů Samourai Wallet a zabavení jejich serverů 24. dubna nyní používání aplikace Samourai Wallet vyžaduje připojení k vlastnímu Dojo, aby fungovalo správně. Kromě toho na transakce Stonewall to nemá žádný vliv a mohou být stále prováděny bez jakýchkoli problémů. Tyto typy transakcí jsou prováděny autonomně, bez potřeby vnější spolupráce nebo připojení přes Soroban.*

_Pozorně sledujeme vývoj této kauzy i vývoj souvisejících nástrojů. Ujistěte se, že tento tutoriál aktualizujeme, jakmile budou k dispozici nové informace._

_Tento tutoriál je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je zodpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

> *"Překonejte předpoklady analýzy blockchainu matematicky dokazatelnými pochybnostmi mezi odesílatelem a příjemcem vašich transakcí."*

## Co je transakce Stonewall?
Stonewall je specifický druh Bitcoinové transakce zaměřený na zvýšení soukromí uživatele během transakce napodobením coinjoin mezi dvěma stranami, aniž by to ve skutečnosti byl. Ve skutečnosti tato transakce není kolaborativní. Uživatel ji může sestavit sám, pouze s použitím vlastních UTXO jako vstupů. Proto můžete vytvořit transakci Stonewall pro jakoukoli příležitost, aniž byste potřebovali koordinovat s dalším uživatelem.

Fungování transakce Stonewall je následující: jako vstup použije odesílatel 2 UTXO, které mu patří. Jako výstup transakce produkuje 4 výstupy, včetně 2, které budou přesně stejné částky. Ostatní 2 budou změny. Mezi 2 výstupy stejné částky jde skutečně jen jeden příjemci platby.

V transakci Stonewall jsou pouze 2 role:
- Odesílatel, který provede skutečnou platbu;
- Příjemce, který nemusí být vědom si specifické povahy transakce a jednoduše očekává platbu od odesílatele.

Pojďme si vzít příklad, abychom pochopili strukturu této transakce. Alice je v pekárně, aby si koupila svou bagetu, která stojí `4,000 sats`. Chce platit v bitcoinech, přičemž si chce udržet určitou úroveň soukromí své platby. Proto se rozhodne vytvořit pro platbu transakci Stonewall.
![transaction stonewall bakery](assets/en/1.webp)
Analýzou této transakce vidíme, že pekař skutečně obdržel `4,000 sats` jako platbu za bagetu. Alice použila jako vstupy 2 UTXO: jedno o `10,000 sats` a jedno o `15,000 sats`. Jako výstup obdržela 3 UTXO: jedno o `4,000 sats`, jedno o `6,000 sats` a jedno o `11,000 sats`. Alice má v této transakci čistý zůstatek `-4,000 sats`, což odpovídá ceně bagety.

V tomto příkladu jsem úmyslně vynechal poplatky za těžbu, aby bylo snazší pochopení. Ve skutečnosti jsou transakční poplatky plně hrazeny odesílatelem.

## Jaký je rozdíl mezi Stonewall a Stonewall x2?
Transakce Stonewall funguje stejně jako transakce StonewallX2, s jediným rozdílem, že ta druhá vyžaduje spolupráci, na rozdíl od klasické transakce Stonewall, odtud označení "x2". Skutečně, transakci Stonewall lze provést bez potřeby vnější spolupráce: odesílatel ji může provést bez pomoci jiné osoby. Avšak pro transakci Stonewall x2 se do procesu přidává další účastník, nazývaný "spolupracovník". Spolupracovník přispívá vlastními bitcoiny jako vstup, vedle těch od odesílatele, a obdrží celou částku jako výstup (minus těžební poplatky).

Pojďme se vrátit k našemu příkladu s Alicí v pekárně. Pokud by chtěla provést transakci Stonewall x2, musela by Alice spolupracovat s Bobem (třetí stranou) při vytváření transakce. Každý by poskytl jeden vstupní UTXO. Bob by poté obdržel celou částku svého vstupu jako výstup. Pekař by obdržel platbu za svou bagetu stejným způsobem jako u transakce Stonewall, zatímco Alice by obdržela zpět svůj počáteční zůstatek, mínus náklady na bagetu.
![transakce stonewall x2](assets/en/2.webp)

Z vnější perspektivy by vzor transakce zůstal přesně stejný.
![Stonewall nebo Stonewall x2 ?](assets/en/3.webp)

Shrnutí, transakce Stonewall a Stonewall x2 sdílejí identickou strukturu. Rozdíl mezi nimi spočívá v jejich kolaborativní povaze. Transakce Stonewall je vyvíjena individuálně, bez potřeby spolupráce. Na rozdíl od toho, transakce Stonewall x2 spoléhá na spolupráci mezi dvěma jednotlivci pro její provedení.

[**-> Dozvědět se více o transakcích Stonewall x2**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)

## Jaký je účel transakce Stonewall?
Struktura Stonewall přidává do transakce významné množství entropie a ztěžuje analýzu řetězce. Z vnější perspektivy může být taková transakce interpretována jako malý coinjoin mezi dvěma lidmi. Ale ve skutečnosti, stejně jako transakce Stonewall x2, jde o platbu. Tato metoda tedy vytváří nejistoty v analýze řetězce a může dokonce vést k falešným stopám.

Pojďme se znovu podívat na příklad Alice v pekárně. Transakce na blockchainu by vypadala takto:
![Stonewall nebo Stonewall x2 ?](assets/en/4.webp)
Vnější pozorovatel spoléhající na běžné heuristiky analýzy řetězce by mohl chybně usoudit, že "*dva lidé provedli malý coinjoin, každý s jedním UTXO jako vstupem a dvěma UTXO jako výstupem*".
![Stonewall nebo Stonewall x2 ?](assets/en/5.webp)
Tato interpretace je nesprávná, protože, jak víte, UTXO bylo posláno pekaři, 2 UTXO ve vstupu pochází od Alice, a ona obdržela 3 změnové výstupy.

![transakce stonewall pekař](assets/en/1.webp)
I když vnější pozorovatel dokáže identifikovat vzor transakce Stonewall, nebude mít veškeré informace. Nebude schopen určit, který ze dvou UTXO stejných částek odpovídá platbě. Navíc nebude schopen určit, zda dva UTXO ve vstupu pocházejí od dvou různých osob, nebo zda patří jedné osobě, která je sloučila. Tento poslední bod je způsoben tím, že transakce Stonewall x2, o kterých jsme výše hovořili, následují přesně stejný vzor jako transakce Stonewall. Zvenčí a bez dalších informací o kontextu je nemožné rozlišit transakci Stonewall od transakce Stonewall x2. Avšak prvně jmenované nejsou kolaborativní transakce, zatímco druhé ano. To přidává ještě více pochybností o tomto výdaji. ![Stonewall nebo Stonewall x2?](assets/en/3.webp)
## Jak provést transakci Stonewall na Samourai Wallet?
Na rozdíl od transakcí Stowaway nebo Stonewall x2 (cahoots) transakce Stonewall nevyžaduje použití Paynymů. Lze ji provést přímo, bez jakýchkoli přípravných kroků. K tomu postupujte podle našeho video návodu na Samourai Wallet: 
![Návod na Stonewall - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)

## Jak provést transakci Stonewall na Sparrow Wallet?
Na rozdíl od transakcí Stowaway nebo Stonewall x2 (cahoots) transakce Stonewall nevyžaduje použití Paynymů. Lze ji provést přímo, bez jakýchkoli přípravných kroků. K tomu postupujte podle našeho video návodu na Sparrow Wallet: 
![Návod na Stonewall - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)


**Externí zdroje:**
- https://docs.samourai.io/en/spend-tools#stonewall.