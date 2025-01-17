---
name: Payjoin - Samourai Wallet
description: Jak provést transakci Payjoin v peněžence Samourai Wallet?
---
![samourai payjoin cover](assets/cover.webp)

***POZOR:** V důsledku zatčení zakladatelů Samourai Wallet a zabavení jejich serverů dne 24. dubna, Payjoins Stowaway na Samourai Wallet nyní fungují pouze při ruční výměně PSBT mezi zúčastněnými stranami, za předpokladu, že oba uživatelé jsou připojeni k vlastnímu Dojo. Co se týče Sparrow, Payjoins přes BIP78 stále fungují. Je však možné, že tyto nástroje budou v nadcházejících týdnech znovu spuštěny. Mezitím si můžete přečíst tento článek, abyste pochopili teoretické fungování Stowaway.*

_Pokud plánujete provést Stowaway ručně, postup je velmi podobný tomu, který je popsán v tomto tutoriálu. Hlavní rozdíl spočívá ve výběru typu transakce Stowaway: místo výběru `Online` klikněte na `Osobně / Ručně`. Poté bude nutné ručně vyměnit PSBT pro sestavení transakce Stowaway. Pokud jste fyzicky blízko svému spolupracovníkovi, můžete postupně skenovat QR kódy. Pokud jste na dálku, JSON soubory lze vyměňovat prostřednictvím bezpečného komunikačního kanálu. Zbytek tutoriálu zůstává nezměněn._

_Pozorně sledujeme vývoj této kauzy i vývoj souvisejících nástrojů. Ujistěte se, že tento tutoriál aktualizujeme, jakmile budou k dispozici nové informace._

_Tento tutoriál je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je odpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

> *"Přinutit špiony blockchainu, aby přehodnotili vše, co si myslí, že vědí."*

Payjoin je specifická struktura Bitcoinové transakce, která zvyšuje soukromí uživatele během platby spoluprací s příjemcem platby. Existuje několik implementací, které usnadňují nastavení a automatizaci PayJoin. Mezi tyto implementace patří nejznámější Stowaway, vyvinutý týmy v Samourai Wallet. Tento tutoriál vysvětluje, jak provést transakci Stowaway Payjoin pomocí aplikace Samourai Wallet.

## Jak funguje Stowaway?

Jak bylo zmíněno dříve, Samourai Wallet nabízí nástroj PayJoin nazvaný "Stowaway." Je přístupný prostřednictvím softwaru Sparrow Wallet na PC nebo aplikace Samourai Wallet na Androidu. Pro provedení Payjoinu musí příjemce, který také vystupuje jako spolupracovník, používat software kompatibilní se Stowaway, konkrétně Sparrow nebo Samourai. Tyto dva softwary jsou interoperabilní, což umožňuje transakci Stowaway mezi peněženkou Sparrow a peněženkou Samourai a naopak.

Stowaway se opírá o kategorii transakcí, které Samourai označuje jako "Cahoots." Cahoot je v podstatě kolaborativní transakce mezi více uživateli, vyžadující výměnu informací mimo řetězec. Samourai k dnešnímu dni nabízí dva nástroje Cahoots: Stowaway (Payjoins) a StonewallX2 (který prozkoumáme v budoucím článku).

Transakce Cahoots zahrnují výměny částečně podepsaných transakcí mezi uživateli. Tento proces může být dlouhý a zdlouhavý, zejména když se provádí na dálku. Přesto lze stále ručně provést s dalším uživatelem, což může být pohodlné, pokud jsou spolupracovníci fyzicky blízko. V praxi to zahrnuje ruční výměnu pěti QR kódů, které se postupně skenují.

Když se tento proces provádí na dálku, stává se příliš složitým. Aby se tento problém vyřešil, Samourai vyvinul šifrovaný komunikační protokol založený na Toru, nazvaný "Soroban." S Sorobanem jsou výměny potřebné pro Payjoin automatizovány za uživatelsky přívětivým rozhraním. To je druhá metoda, kterou v tomto článku prozkoumáme.
Tyto šifrované výměny vyžadují navázání spojení a ověření mezi účastníky Cahoots. Komunikace Soroban je proto založena na Paynyme uživatelů. Pokud nejste obeznámeni s Paynymy, doporučuji vám pro více detailů navštívit tento článek: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)

 Jednoduše řečeno, Paynym je unikátní identifikátor spojený s vaší peněženkou, který umožňuje různé funkce, včetně šifrovaného zasílání zpráv. Paynym je prezentován ve formě identifikátoru a ilustrace reprezentující robota. Zde je příklad mého na Testnetu: ![paynym samourai wallet](assets/en/1.webp)

**Shrnutí:**
- _Payjoin_ = Specifická struktura kolaborativních transakcí;
- _Stowaway_ = Implementace Payjoin dostupná na Samourai a Sparrow Wallet;
- _Cahoots_ = Název, který Samourai dává všem typům svých kolaborativních transakcí, včetně Payjoin Stowaway;
- _Soroban_ = Protokol šifrované komunikace založený na Toru, umožňující spolupráci s dalšími uživateli v kontextu transakce Cahoots;
- _Paynym_ = Unikátní identifikátor peněženky umožňující komunikaci s dalším uživatelem na Sorobanu za účelem provedení transakce Cahoots.

[**-> Dozvědět se více o transakcích Payjoin a jejich užitečnosti**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)

## Jak navázat spojení mezi Paynymy?

Pro provedení vzdálené transakce Cahoots, konkrétně PayJoin (Stowaway) přes Samourai, je nutné "sledovat" uživatele, se kterým máte v úmyslu spolupracovat, pomocí jejich Paynymu. V případě Stowaway to znamená sledovat osobu, které chcete poslat bitcoiny.

**Zde je postup, jak toto spojení navázat:**

Nejprve potřebujete získat platební kód Paynymu příjemce pro Payjoin. V aplikaci Samourai Wallet musí příjemce klepnout na ikonu svého Paynymu (malý robot) umístěnou v levém horním rohu obrazovky a poté kliknout na přezdívku svého Paynymu, začínající na `+...`. Například můj je `+namelessmode0aF`. Pokud váš spolupracovník používá Sparrow Wallet, doporučuji vám navštívit náš věnovaný tutoriál kliknutím zde.

![connexion paynym samourai](assets/notext/2.webp)

Váš spolupracovník bude poté přesměrován na stránku svého Paynymu. Odtud může buď sdílet své údaje Paynymu s vámi, nebo sdílet svůj QR kód, abyste ho mohli naskenovat. K tomu musí kliknout na malou ikonu "sdílet" umístěnou v pravém horním rohu jejich obrazovky.
![partager paynym samourai](assets/en/1.webp)

Na vaší straně spusťte aplikaci Samourai Wallet a přistupte k menu "PayNyms" stejným způsobem. Pokud používáte svůj Paynym poprvé, budete potřebovat získat identifikátor.

![demander un paynym](assets/notext/3.webp)

Poté klikněte na modré "+" v pravém dolním rohu obrazovky.
![ajouter paynym collaborateur](assets/notext/4.webp)
Poté můžete vložit platební kód svého spolupracovníka vybráním `VLOŽIT KÓD PLATBY`, nebo otevřít kameru pro skenování jejich QR kódu stisknutím `SKENOVAT QR KÓD`.![paste paynym identifier](assets/notext/5.webp)

Klikněte na tlačítko `SLEDOVAT`.
![follow paynym](assets/notext/6.webp)Potvrďte kliknutím na `ANO`.
![confirm follow paynym](assets/notext/7.webp)
Software vám poté nabídne tlačítko `SE CONNECTER`. Pro účely našeho návodu není nutné na toto tlačítko klikat. Tento krok je vyžadován pouze v případě, že plánujete provádět platby na jiný Paynym jako součást BIP47, což není součástí našeho návodu.
![connect paynym](assets/notext/8.webp)
Jakmile váš Paynym sleduje Paynym příjemce, opakujte tuto operaci v opačném směru, aby vás také příjemce sledoval. Poté můžete provést Payjoin.

## Jak provést Payjoin na Samourai Wallet?

Pokud jste dokončili tyto předběžné kroky, jste konečně připraveni provést transakci Payjoin! Postupujte podle našeho video návodu:

![Payjoin Video Tutorial - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)

**Externí zdroje:**
- https://docs.samourai.io/en/spend-tools#stowaway.