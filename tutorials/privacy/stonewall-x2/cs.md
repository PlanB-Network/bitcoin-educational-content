---
name: Stonewall x2
description: Porozumění a používání transakcí Stonewall x2
---
![cover stonewall x2](assets/cover.webp)

***VAROVÁNÍ:** Po zatčení zakladatelů Samourai Wallet a zabavení jejich serverů 24. dubna fungují transakce Stonewallx2 pouze manuální výměnou PSBT mezi dotčenými stranami, za předpokladu, že oba uživatelé jsou připojeni ke svému vlastnímu Dojo. Je možné, že tyto nástroje budou znovu spuštěny v nadcházejících týdnech. Mezitím si můžete tento článek přečíst, abyste pochopili teoretické fungování Stonewallx2 a naučili se je provádět ručně.*

_Pokud zvažujete provést Stonewallx2 ručně, postup je velmi podobný tomu, který je popsaný v tomto návodu. Hlavní rozdíl spočívá ve výběru typu transakce Stonewallx2: místo výběru `Online` klikněte na `Osobně / Ručně`. Poté bude nutné ručně vyměnit PSBT pro sestavení transakce Stonewallx2. Pokud jste fyzicky blízko svému spolupracovníkovi, můžete postupně skenovat QR kódy. Pokud jste na dálku, JSON soubory lze vyměňovat prostřednictvím bezpečného komunikačního kanálu. Zbytek návodu zůstává nezměněn._

_Pečlivě sledujeme vývoj této kauzy i vývoj souvisejících nástrojů. Ujistěte se, že tento návod aktualizujeme, jakmile budou k dispozici nové informace._

_Tento návod je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je odpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

> *Učiňte z každé platby coinjoin.*

## Co je transakce Stonewall x2?

Stonewall x2 je specifický druh Bitcoinové transakce zaměřený na zvýšení soukromí uživatele při platbě, a to spoluprací s třetí stranou, která není v této platbě zapojena. Tato metoda simuluje mini-coinjoin mezi dvěma účastníky, zatímco se provádí platba třetí straně. Transakce Stonewall x2 jsou dostupné jak v aplikaci Samourai Wallet, tak v softwaru Sparrow Wallet. Oba jsou interoperabilní.

Její provoz je poměrně jednoduchý: používáme UTXO ve svém vlastnictví k provedení platby a hledáme pomoc třetí strany, která také přispěje vlastním UTXO. Transakce má čtyři výstupy: dva z nich ve stejných částkách, jeden určený pro adresu příjemce platby, druhý pro adresu spolupracovníka. Třetí UTXO je vráceno na další adresu spolupracovníka, což mu umožňuje získat zpět původní částku (pro něj neutrální akce, modulo těžební poplatky), a konečné UTXO se vrací na adresu nám, což představuje zbytek z platby.

Takto jsou definovány tři různé role v transakcích Stonewall x2:
- Odesílatel, který provádí skutečnou platbu;
- Spolupracovník, který poskytuje bitcoiny k zlepšení celkové anonymity transakce, přičemž na konci plně získává zpět své prostředky (pro něj neutrální akce, modulo těžební poplatky);
- Příjemce, který nemusí být vědom si specifické povahy transakce a jednoduše očekává platbu od odesílatele.

Pojďme si vzít příklad, abychom lépe pochopili. Alice je v pekárně, aby si koupila bagetu, která stojí `4,000 sats`. Chce platit bitcoiny, přičemž si přeje udržet určitou úroveň soukromí své platby. Proto vyzve svého přítele Boba, který jí v tomto procesu pomůže.
![schema stonewall x2](assets/en/1.webp)
Při analýze této transakce vidíme, že pekař skutečně obdržel `4,000 sats` jako platbu za bagetu. Alice použila `10,000 sats` jako vstup a obdržela `6,000 sats` jako výstup, což vede k čistému zůstatku `-4,000 sats`, což odpovídá ceně bagety. Co se týče Boba, poskytl `15,000 sats` jako vstup a obdržel dva výstupy: jeden `4,000 sats` a druhý `11,000 sats`, což vede k zůstatku `0`. V tomto příkladu jsem záměrně opomenul poplatky za těžbu, aby bylo pochopení jednodušší. Ve skutečnosti se transakční poplatky dělí rovným dílem mezi odesílatele platby a spolupracovníka.

## Jaký je rozdíl mezi Stonewall a Stonewall x2?

Transakce StonewallX2 funguje přesně jako transakce Stonewall, s tím rozdílem, že první je kolaborativní, zatímco druhá není. Jak jsme viděli, transakce Stonewall x2 zahrnuje účast třetí strany, která je externí vůči platbě, a která poskytne své bitcoiny k zvýšení soukromí transakce. V typické transakci Stonewall je role spolupracovníka převzata odesílatelem.

Pojďme se vrátit k našemu příkladu s Alicí v pekárně. Pokud by nenašla někoho jako Boba, kdo by ji doprovodil ve výdaji, mohla by provést transakci Stonewall sama. Takže oba vstupní UTXOs by byly její a na výstupu by obdržela 3.
![transakce stonewall](assets/en/2.webp)

Z externího pohledu by vzor transakce zůstal stejný.
![Stonewall nebo Stonewall x2?](assets/en/5.webp)
Logika by tedy měla být následující při použití nástroje Samourai pro výdaje:
- Pokud obchodník nepodporuje Payjoin Stowaway, kolaborativní transakce může být provedena s další osobou externí vůči platbě pomocí Stonewall x2.
- Pokud se nenajde nikdo pro provedení transakce Stonewall x2, může být provedena transakce Stonewall samostatně, napodobující chování transakce Stonewall x2.
- Nakonec poslední možností by bylo provést transakci s JoinBot, serverem udržovaným Samourai, který může na požádání působit jako spolupracovník v transakci Stonewall x2.

Pokud chcete najít spolupracovníka, který je ochoten vám pomoci v transakci Stonewall X2, můžete také navštívit tuto Telegramovou skupinu (neoficiální) udržovanou uživateli Samourai pro spojení odesílatelů a spolupracovníků: [Make Every Spend a Coinjoin](https://t.me/EverySpendACoinjoin).

[**-> Dozvědět se více o transakcích Stonewall**](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

## Jaký je účel transakce Stonewall x2?

Struktura Stonewall x2 přidává do transakce významné množství entropie a mate analýzu řetězce. Z vnějšku může být taková transakce interpretována jako malý Coinjoin mezi dvěma jednotlivci. Ve skutečnosti je to ale platba. Tato metoda generuje nejistoty v analýze řetězce a dokonce vede k falešným stopám.

Vraťme se k příkladu Alice, Boba a pekaře. Transakce na blockchainu by vypadala takto:
![stonewall x2 veřejně](assets/en/3.webp)
Externí pozorovatel, spoléhající se na běžné heuristiky analýzy řetězce, by mohl chybně usoudit, že "Alice a Bob provedli malý coinjoin, každý s jedním vstupním UTXO a každý se dvěma výstupními UTXO."![misinterpretace stonewall x2](assets/en/4.webp)Tato interpretace je nesprávná, protože, jak víte, UTXO bylo odesláno Pekaři, Alice má pouze jeden výstup změny a Bob má dva.
![transakce stonewall x2](assets/en/1.webp)
I když externí pozorovatel dokáže identifikovat vzor transakce Stonewall x2, nebude mít veškeré informace. Nebude schopen určit, které ze dvou UTXO stejných částek odpovídá platbě. Dále nebude schopen vědět, zda platbu provedla Alice nebo Bob. Nakonec nebude schopen určit, zda dva vstupní UTXO pocházejí od dvou různých osob, nebo zda patří jedné osobě, která je sloučila. Tento poslední bod je způsoben tím, že klasické transakce Stonewall, o kterých jsme výše hovořili, následují přesně stejný vzor jako transakce Stonewall x2. Zvenčí a bez dalších informací o kontextu je nemožné odlišit transakci Stonewall od transakce Stonewall x2. Avšak prvně jmenované nejsou kolaborativní transakce, zatímco druhé ano. To přidává ještě více pochybností o tomto výdaji.
![Stonewall nebo Stonewall x2?](assets/en/5.webp)

## Jak navázat spojení mezi Paynyms, aby bylo možné spolupracovat prostřednictvím Soroban?

Stejně jako u jiných kolaborativních transakcí na Samourai (*Cahoots*), provádění Stonewall x2 zahrnuje výměnu částečně podepsaných transakcí mezi odesílatelem a spolupracovníkem. Tato výměna může být provedena ručně, pokud jste fyzicky se svým spolupracovníkem, nebo automaticky prostřednictvím komunikačního protokolu Soroban.

Pokud si vyberete druhou možnost, budete muset navázat spojení mezi Paynyms, než budete moci provést Stonewall x2. K tomu je nutné, aby váš Paynym "sledoval" Paynym vašeho spolupracovníka a naopak.

**Přístup k Paynymu spolupracovníka:**

Začít je nutné získáním platebního kódu Paynymu vašeho spolupracovníka. V aplikaci Samourai Wallet musí váš spolupracovník stisknout ikonu svého Paynymu (malý robot) umístěnou v levém horním rohu obrazovky, poté kliknout na přezdívku svého Paynymu, začínající na `+...`. Například moje je `+namelessmode0aF`.

![samourai paynym](assets/notext/6.webp)
Pokud váš spolupracovník používá Sparrow Wallet, měl by kliknout na záložku 'Nástroje', poté na 'Zobrazit PayNym'.![paynym sparrow](assets/notext/7.webp)
**Sledování PayNymu vašeho spolupracovníka z Samourai Wallet:**

Pokud používáte Samourai Wallet, spusťte aplikaci a stejným způsobem přistupte k menu 'PayNyms'. Pokud používáte svůj Paynym poprvé, budete potřebovat získat jeho identifikátor.

![požadavek paynym samourai](assets/notext/8.webp)

Poté klikněte na modré '+' v pravém dolním rohu obrazovky.
![přidat spolupracovníka paynym](assets/notext/9.webp)
Poté můžete vložit platební kód svého spolupracovníka výběrem 'VLOŽIT PLATEBNÍ KÓD', nebo otevřít kameru pro skenování jejich QR kódu stisknutím 'SKENOVAT QR KÓD'.
![paste paynym identifier](assets/notext/10.webp)
Klikněte na tlačítko 'FOLLOW'.
![follow paynym](assets/notext/11.webp)
Potvrďte kliknutím na 'YES'.
![confirm follow paynym](assets/notext/12.webp)
Software vám poté nabídne tlačítko 'CONNECT'. Pro náš tutoriál není nutné na toto tlačítko klikat. Tento krok je vyžadován pouze pokud plánujete provádět platby na jiný PayNym jako součást BIP47, což není součástí našeho tutoriálu.
![connect paynym](assets/notext/13.webp)
Jakmile váš PayNym sleduje PayNym vašeho spolupracovníka, opakujte tento proces v opačném směru, aby vás mohl sledovat i váš spolupracovník. Poté můžete provést transakci Stonewall x2.

**Sledování PayNym vašeho spolupracovníka z Sparrow Wallet:**

Pokud používáte Sparrow Wallet, otevřete svou peněženku a přistupte k menu 'Show PayNym'. Pokud používáte svůj PayNym poprvé, budete muset získat identifikátor kliknutím na 'Retrieve PayNym'.
![request paynym sparrow](assets/notext/14.webp)
Poté zadejte identifikátor PayNym vašeho spolupracovníka (buď jejich přezdívku '+...' nebo jejich platební kód 'PM...') do pole 'Find Contact' a klikněte na tlačítko 'Add Contact'.
![add contact paynym](assets/notext/15.webp)
Software vám poté nabídne tlačítko 'Link Contact'. Pro náš tutoriál není nutné na toto tlačítko klikat. Tento krok je vyžadován pouze pokud plánujete provádět platby na uvedený PayNym jako součást BIP47, což není součástí našeho tutoriálu.

Jakmile váš PayNym sleduje PayNym vašeho spolupracovníka, opakujte tento proces v opačném směru, aby vás mohl sledovat i váš spolupracovník. Poté můžete provést transakci Stonewall x2.
## Jak provést transakci Stonewall x2 na Samourai Wallet?

Pokud jste dokončili předchozí kroky spojení Paynymů, jste konečně připraveni provést transakci Stonewall x2! Postupujte podle našeho video tutoriálu na Samourai Wallet:
![Stonewall x2 Tutorial - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)

## Jak provést transakci Stonewall x2 na Sparrow Wallet?

Pokud jste dokončili předchozí kroky spojení Paynymů, jste konečně připraveni provést transakci Stonewall x2! Postupujte podle našeho video tutoriálu na Sparrow Wallet:
![Stonewall x2 Tutorial - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)

**Externí zdroje:**
- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.