---
name: Ashigaru - Stonewall x2
description: Porozumění a používání transakcí Stonewall x2 na Ashigaru
---
![cover stonewall x2](assets/cover.webp)



> *Udělejte z každé útraty coinjoin

## Co je to transakce Stonewall x2?



Stonewall x2 je specifická forma transakce Bitcoin, jejímž cílem je zvýšit důvěrnost uživatelů při utrácení, a to díky spolupráci s třetí stranou, která se na výdaji nepodílí. Tato metoda simuluje minipřipojení mezi dvěma účastníky a zároveň provádí platbu třetí straně. Transakce Stonewall x2 jsou k dispozici v aplikaci Ashigaru, fork od Samourai Wallet (tým, který stojí za vytvořením tohoto typu transakce).



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Funguje to poměrně jednoduše: k platbě použijete kartu UTXO, kterou vlastníte, a požádáte o pomoc třetí stranu, která rovněž přispěje svou vlastní kartou UTXO. Transakce končí čtyřmi výstupy: dva z nich jsou ve stejné výši, jeden je určen pro adresu příjemce platby, druhý pro adresu patřící spolupracovníkovi. Třetí UTXO se vrací na jinou adresu patřící spolupracovníkovi, což mu umožňuje získat zpět původní částku (pro něj neutrální akce, modulovaná náklady na mining), a poslední UTXO se vrací na adresu patřící nám, což představuje výměnu plateb.



V transakcích Stonewall x2 jsou tak definovány tři různé role:




- Vydavatel, který provádí skutečnou platbu ;
- Spolupracovník, který dává k dispozici bitcoiny, aby zvýšil anonymitu transakce, přičemž na konci získá zpět své prostředky v plné výši (což je pro něj neutrální akce, modulovaná náklady mining);
- Příjemce, který si nemusí být vědom specifické povahy transakce a jednoduše očekává platbu od odesílatele.



Uveďme si příklad. Alice je u pekaře, aby si koupila bagetu, která stojí `4 000 sats`. Chce zaplatit v bitcoinech, přičemž si chce zachovat určitou důvěrnost ohledně své platby. Zavolá si tedy svého přítele Bob, který jí s tím pomůže.



![image](assets/fr/01.webp)



Při analýze této transakce zjistíme, že pekař ve skutečnosti obdržel za bagetu 4 000 haléřů-10 haléřů. Alice použil na vstupu `10 000 sats` a na výstupu získal zpět `6 000 sats`, což dává čistý zůstatek `4 000 sats`, který odpovídá ceně bagety. Bob dodal na vstupu 15 000 sats` a obdržel dva výstupy: jeden ve výši 4 000 sats` a druhý ve výši 11 000 sats`, takže zůstatek činil 0`.



V tomto příkladu jsem záměrně zanedbal poplatky mining, aby byl příklad srozumitelnější. Ve skutečnosti se poplatky za transakce dělí rovným dílem mezi vydavatele platby a spolupracující osobu.



## Jaký je rozdíl mezi Stonewall a Stonewall x2?



Transakce StonewallX2 funguje úplně stejně jako transakce Stonewall s tím rozdílem, že první z nich je kolaborativní, zatímco druhá nikoli. Jak jsme viděli, transakce Stonewall x2 zahrnuje účast třetí strany, která je vůči platbě externí a která dá k dispozici své bitcoiny, aby zvýšila důvěrnost transakce. V klasické Stonewall transakci přebírá roli spolupracující osoby odesílatel.



Vraťme se k našemu příkladu Alice v pekárně. Kdyby se jí nepodařilo najít někoho, jako je Bob, kdo by ji doprovázel při jejím utrácení, mohla by udělat Stonewall sama. Takto by dvě UTXO na cestě dovnitř byly její a cestou ven by sebrala tři.



![image](assets/fr/02.webp)




Z vnějšího pohledu by transakce zůstala stejná.



![image](assets/fr/05.webp)



Když chcete použít nástroj na utrácení Ashigaru, měla by být logika následující:




- Pokud obchodník nepodporuje službu Payjoin Stowaway, můžete provést společnou transakci s jinou osobou mimo platbu díky službě Stonewall x2 ;
- Pokud nemůžete najít nikoho, kdo by provedl transakci Stonewall x2, můžete provést pouze transakci Stonewall, která bude napodobovat chování transakce Stonewall x2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Jaký smysl má transakce Stonewall x2?



Struktura Stonewall x2 přidává do transakce obrovské množství entropie, což zkresluje řetězovou analýzu. Při pohledu zvenčí by taková transakce mohla být interpretována jako malý Coinjoin mezi dvěma lidmi. Ve skutečnosti se však jedná o platbu. Tato metoda proto vytváří nejistotu v analýze řetězce, nebo dokonce vede k falešným stopám.



Vezměme si příklad Alice, Bob a Boulanger. Transakce v blockchainu by vypadala následovně:



![image](assets/fr/03.webp)



Vnější pozorovatel, který se spoléhá na běžnou heuristiku analýzy řetězce, by mohl chybně dojít k závěru, že "*Alice a Bob provedly malé spojení, přičemž každý z nich má jeden UTXO in a každý dva UTXO out*".



![image](assets/fr/04.webp)



Tento výklad je nesprávný, protože jak víte, do Boulangeru byl odeslán UTXO, Alice má pouze jeden výměnný výstup a Bob má dva.



![image](assets/fr/01.webp)



I kdyby se vnějšímu pozorovateli podařilo identifikovat paterna transakce Stonewall x2, nebude mít k dispozici všechny informace. Nebude schopen určit, kterému ze dvou UTXO stejných částek odpovídá platba. Stejně tak nebude schopen určit, zda platbu provedl Alice nebo Bob. A konečně nebude schopen určit, zda obě zadaná UTXO pocházejí od dvou různých osob, nebo zda patří jedné osobě, která je sloučila. Tento poslední bod je způsoben skutečností, že klasické Stonewall transakce, o nichž byla řeč výše, se řídí přesně stejným paternem jako Stonewall x2 transakce. Při pohledu zvenčí a bez dalších kontextových informací není možné odlišit transakci Stonewall od transakce Stonewall x2. Ty první nejsou transakcemi spolupráce, zatímco ty druhé ano. To přidává k výdajům ještě více pochybností.



![image](assets/fr/05.webp)




## Jak navážu spojení mezi službami Paynyms?



Stejně jako u jiných kolaborativních transakcí na Ashigaru (*Cahoots*), i u Stonewall x2 dochází k výměně částečně podepsaných transakcí mezi odesílatelem a spolupracovníkem. Tuto výměnu lze provést ručně, pokud jste se spolupracovníkem fyzicky přítomni, nebo automaticky pomocí komunikačního protokolu Soroban.



Pokud zvolíte druhou možnost, budete muset před provedením akce Stonewall x2 navázat spojení mezi systémy Paynyms. Za tímto účelem musí váš Paynym "*sledovat*" Paynym vašeho spolupracovníka a naopak. Chcete-li zjistit, jak to udělat, můžete postupovat podle začátku tohoto dalšího návodu:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Jak mohu provést transakci Stonewall x2 na Ashigaru?



Chcete-li provést transakci Stonewall x2, klikněte na obrázek svého Paynymu v levém horním rohu obrazovky a poté otevřete nabídku `Spolupracovat`. Osoba, která se s vámi účastní transakce, musí udělat totéž, pokud si QR kódy nevyměňujete osobně.



![Image](assets/fr/06.webp)



Máte dvě možnosti: vyberte `Iniciovat`, pokud jste odesílatelem platby, nebo `Zúčastnit se`, pokud jste osobou spolupracující na transakci, ale nejste ani plátcem, ani skutečným příjemcem.



![Image](assets/fr/07.webp)



Pokud máte roli spolupracovníka, je postup velmi jednoduchý. Pro vzdálenou spolupráci prostřednictvím sítě Soroban klikněte na `Podílet se`, vyberte účet, který chcete použít, a poté stiskněte `ČEKAT NA POŽADAVKY NA CAHOOTS` a vyčkejte na požadavek zaslaný plátcem.



![Image](assets/fr/08.webp)



Naopak při osobní spolupráci prostřednictvím skenování QR kódu přejděte na domovskou stránku wallet, stiskněte ikonu QR kódu v horní části obrazovky a poté naskenujte QR kód poskytnutý plátcem, který transakci iniciuje.



![Image](assets/fr/09.webp)



Pokud jste v roli plátce, tj. iniciátora transakce, přejděte do nabídky `Spolupracovat` a vyberte možnost `Iniciovat`.



![Image](assets/fr/10.webp)



Protože chceme provést transakci Stonewall x2, zvolte tuto možnost.



![Image](assets/fr/11.webp)



Poté si můžete vybrat mezi online spoluprací (*Cahoots* přes *Soroban*) nebo osobní spoluprací s výměnou QR kódů.



![Image](assets/fr/12.webp)



### Cahoots online



Pokud jste zvolili možnost `Online`, vyberte spolupracovníka ze sledovaných systémů Paynyms.



![Image](assets/fr/13.webp)



Klikněte na `Nastavit transakci` a poté vyberte účet, ze kterého chcete provést výdaj.



![Image](assets/fr/14.webp)



Na další stránce zadejte údaje o transakci: adresu skutečného příjemce platby, částku k odeslání a sazbu poplatku. Poté klikněte na `Přezkoumat nastavení transakce`.



![Image](assets/fr/15.webp)



Pečlivě zkontrolujte informace, ujistěte se, že váš spolupracovník poslouchá požadavky *Cahoots*, a poté klikněte na zelené tlačítko `Začít TRANSAKCI` pro zahájení výměny PSBT prostřednictvím Sorobanu.



![Image](assets/fr/16.webp)



Počkejte, dokud oba účastníci transakci nepodepíší, a pak ji odvysílejte v síti Bitcoin.



![Image](assets/fr/17.webp)



### Osobní diskuse



Pokud chcete výměnu provést osobně, vyberte typ transakce `STONEWALL X2` a poté možnost `Osobně / ručně`.



![Image](assets/fr/18.webp)



Klikněte na `Nastavit transakci` a poté vyberte účet, ze kterého chcete provést výdaj.



![Image](assets/fr/19.webp)



Na další stránce zadejte údaje o transakci: adresu skutečného příjemce platby, částku k odeslání a sazbu poplatku. Poté klikněte na `Přezkoumat nastavení transakce`.



![Image](assets/fr/20.webp)



Zkontrolujte údaje a poté stiskněte zelené tlačítko `Začít transakci` a začněte vyměňovat PSBT prostřednictvím skenování QR kódu.



![Image](assets/fr/21.webp)



Výměna se provádí střídavým skenováním se spolupracovníkem: kliknutím na `ZOBRAZIT QR KÓD` zobrazíte svůj QR kód spolupracovníkovi, který jej naskenuje. On pak kliknutím na `ZOBRAZIT QR KÓD` zobrazí svůj kód a vy jej naskenujete pomocí `ZAPOJIT QR skener`. Tento postup opakujte, dokud nebude dokončeno všech pět kroků výměny.



![Image](assets/fr/22.webp)



Po dokončení všech výměn zkontrolujte podrobnosti transakce a poté ji uvolněte přetažením zelené šipky v dolní části obrazovky.



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Její struktura je následující:



![Image](assets/fr/24.webp)



*Kredit: [mempool.space](https://mempool.space/)*



Můžeme pozorovat dva vstupy z mého portfolia, a to `91 869 sats` a `64 823 sats`, zatímco další dva vstupy pocházejí z portfolia wallet mého spolupracovníka. Na straně výstupu je jeden UTXO ve výši `100 000 sats` odeslán skutečnému příjemci platby a dva UTXO ve výši `100 000 sats` a `159 578 sats` se vracejí do portfolia mého spolupracovníka. Pro něj je operace neutrální, protože získá zpět celou částku prostředků, které investoval na vstupu (bez nákladů na mining, na které přispěl). Nakonec obdržím výměnný UTXO ve výši `56 270 sats`, což odpovídá rozdílu mezi mými celkovými vstupy a platbou ve výši `100 000 sats` zaslanou příjemci.



Tuto strukturu mohu samozřejmě popsat, protože jsem transakci sám vytvořil. Ale pro vnějšího pozorovatele je obecně nemožné určit, které UTXO patří kterému účastníkovi, ať už na vstupu nebo na výstupu.



Chcete-li prohloubit své znalosti o správě soukromí v onchainu na platformě Bitcoin, doporučuji vám absolvovat mé školení BTC 204 na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c