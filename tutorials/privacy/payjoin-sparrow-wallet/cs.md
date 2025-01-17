---
name: Payjoin - Sparrow Wallet
description: Jak provést Payjoin transakci na Sparrow Wallet?
---
![tutorial cover image sparrow payjoin](assets/cover.webp)

***POZOR:** V důsledku zatčení zakladatelů Samourai Wallet a zabavení jejich serverů dne 24. dubna, Payjoins Stowaway na Samourai Wallet nyní fungují pouze při ruční výměně PSBT mezi zúčastněnými stranami, za předpokladu, že oba uživatelé jsou připojeni k vlastnímu Dojo. Co se týče Sparrow, Payjoins přes BIP78 stále fungují. Je však možné, že tyto nástroje budou v nadcházejících týdnech znovu spuštěny. Mezitím si můžete přečíst tento článek, abyste pochopili teoretické fungování payjoins.*

_Sledujeme vývoj této kauzy i vývoj souvisejících nástrojů. Ujistěte se, že tento tutoriál aktualizujeme, jakmile budou k dispozici nové informace._

_Tento tutoriál je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je odpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

> *"Nechte blockchainové špiony přehodnotit vše, co si myslí, že vědí."*

Payjoin je specifická struktura Bitcoinové transakce, která zvyšuje soukromí uživatele při utrácení prostřednictvím spolupráce s příjemcem platby. Existuje několik implementací, které usnadňují nastavení a automatizaci PayJoinu. Mezi tyto implementace patří zejména Stowaway vyvinutý týmem Samourai Wallet. Tento tutoriál má za cíl provést vás procesem provádění Stowaway Payjoin transakce pomocí softwaru Sparrow Wallet.

## Jak funguje Stowaway?

Jak bylo zmíněno dříve, Samourai Wallet nabízí nástroj PayJoin nazvaný "Stowaway." Je přístupný prostřednictvím softwaru Sparrow Wallet na PC nebo aplikace Samourai Wallet na Androidu. Pro provedení Payjoinu musí příjemce, který také vystupuje jako spolupracovník, používat software kompatibilní se Stowaway, konkrétně Sparrow nebo Samourai Wallet. Tyto dva softwary jsou interoperabilní, což umožňuje provádění transakcí Stowaway mezi peněženkou Sparrow a peněženkou Samourai a naopak.

Stowaway využívá kategorii transakcí, které Samourai označuje jako "Cahoots." Cahoot je v podstatě spolupracující transakce mezi více uživateli, která vyžaduje výměnu informací mimo řetězec. Samourai aktuálně nabízí dva nástroje Cahoots: Stowaway (Payjoins) a StonewallX2 (který prozkoumáme v budoucím článku).

Transakce Cahoots zahrnují výměnu částečně podepsaných transakcí mezi uživateli. Tento proces může být dlouhý a zdlouhavý, zejména když se provádí na dálku. Přesto je možné jej provést ručně s dalším uživatelem, což může být pohodlné, pokud jsou spolupracovníci fyzicky blízko. V praxi to zahrnuje ruční výměnu pěti QR kódů, které je třeba postupně naskenovat.

Když se tento proces provádí na dálku, stává se příliš složitým. Aby Samourai tento problém řešil, vyvinul šifrovaný komunikační protokol založený na Toru, nazvaný "Soroban." S Sorobanem jsou nutné výměny pro Payjoin automatizovány za uživatelsky přívětivým rozhraním. To je druhá metoda, kterou v tomto článku prozkoumáme.

Tyto šifrované výměny vyžadují navázání spojení a autentizaci mezi účastníky Cahoots. Komunikace Sorobanu spoléhá na Paynyms uživatelů. Pokud nejste obeznámeni s Paynyms, doporučuji se odkázat na tento článek pro více detailů: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)
Abych to řekl jednoduše, Paynym je unikátní identifikátor spojený s vaší peněženkou, který umožňuje různé funkce, včetně šifrovaného zasílání zpráv. Paynym je prezentován ve formě identifikátoru a ilustrace představující robota. Zde je příklad mého na Testnetu: ![Paynym Sparrow](assets/en/1.webp)
**Shrnutí:**
- *Payjoin* = Specifická struktura kolaborativní transakce;
- *Stowaway* = Implementace Payjoin dostupná na Samourai a Sparrow Wallet;
- *Cahoots* = Název, který Samourai dává všem svým typům kolaborativních transakcí, včetně Payjoin Stowaway;
- *Soroban* = Protokol šifrované komunikace založený na Toru, umožňující spolupráci s dalšími uživateli v kontextu transakce Cahoots.
- *Paynym* = Unikátní identifikátor peněženky umožňující komunikaci s dalším uživatelem na Sorobanu za účelem provedení transakce Cahoots.

[**-> Zjistěte více o transakcích Payjoin a jejich užitečnosti**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)

## Jak navázat spojení mezi Paynyms?

Pro provedení vzdálené transakce Cahoots, konkrétně PayJoin (Stowaway) prostřednictvím Samourai nebo Sparrow, je nutné "sledovat" uživatele, se kterým máte v úmyslu spolupracovat, pomocí jejich Paynym. V případě Stowaway to znamená sledovat osobu, které chcete poslat bitcoiny.

**Zde je postup, jak toto spojení navázat:**

Nejprve potřebujete získat identifikátor Paynym příjemce. To lze udělat pomocí jejich přezdívky nebo platebního kódu. K tomu, z peněženky Sparrow příjemce, vyberte záložku `Tools`, poté klikněte na `Show PayNym`.
![Show Paynym](assets/notext/2.webp)
![Paynym Sparrow](assets/en/1.webp)
Na vaší straně otevřete vaši Sparrow Wallet a přistupte k stejnému menu `Show PayNym`. Pokud používáte svůj Paynym poprvé, budete potřebovat získat identifikátor kliknutím na `Retrieve PayNym`.
![Retrieve paynym](assets/notext/3.webp)
Dále zadejte identifikátor Paynym vašeho spolupracovníka (buď jejich přezdívku `+...` nebo jejich platební kód `PM...`) do pole `Find Contact`, poté klikněte na tlačítko `Add Contact`.
![add contact](assets/notext/4.webp)
Software vám poté nabídne tlačítko `Link Contact`. Kliknutí na toto tlačítko není pro náš tutoriál nutné. Tento krok je nutný pouze pokud plánujete provádět platby na Paynym uvedený v kontextu BIP47, což není součástí našeho tutoriálu.

Jakmile Paynym příjemce sleduje váš Paynym, opakujte tuto operaci v opačném směru, aby vás příjemce také sledoval. Poté můžete provést Payjoin.

## Jak provést Payjoin na Sparrow Wallet?
Pokud jste dokončili tyto předběžné kroky, jste konečně připraveni provést transakci Payjoin! Postupujte podle našeho video tutoriálu:
![Payjoin Tutorial - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)

**Externí zdroje:**
- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.