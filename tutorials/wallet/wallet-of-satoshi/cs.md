---
name: Wallet z Satoshi (WoS)
description: Nejjednodušší Wallet (opatrovnictví) pro začátek
---
![cover](assets/cover.webp)

_Tento návod napsal_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

# Stažení, konfigurace a používání Wallet z Satoshi

Wallet z Satoshi je Wallet Lightning Network, opatrovnický, velmi jednoduchý na použití.

Pro účely kurzu [BTC105 - Finding Yourself Now](https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5) se používá na poukazy Redeem Lightning Network.

**vždy pamatujte**: _ne klíče, ne mince_

Wallet custodial, neumožňují uživatelům plně disponovat svými prostředky. Obvykle se nedoporučují, s výjimkou těch, kteří začínají od nuly. WoS by měly sloužit jako vstupní brána Wallet nebo k ukládání kapesného, nikoliv k dlouhodobému hromadění prostředků.

---
Wallet z Satoshi (WoS) je opatrovnický produkt, ale má určitou pověst. Můžeme se rozumně obrátit na nástroj, jako je WoS, abychom například zvýšili svou schopnost získat likviditu. Na WoS dočasně delegujeme "špinavou práci", kterou je správa likvidity kanálů za nás. Jakmile dosáhneme určitého množství, vyprázdníme WoS On-Chain na našem neúředním Wallet.

**ATTENZIONE⚠️: Před pokračováním doporučujeme přečíst si celý návod**

## Stahování Wallet z Satoshi

Přejděme do obchodu playstore a stáhněme si WoS

![image](assets/it/01.webp)

**Poznámka:** WoS lze stáhnout pouze z oficiálních obchodů. Pokud je operační systém zařízení naprogramován, proběhne před otevřením WoS ověřovací část samotným operačním systémem. Jakmile proběhne ověřovací fáze, zvolte možnost _Otevřít_.

![image](assets/it/02.webp)

Wallet z Satoshi se otevře s následující obrazovkou a je třeba kliknout na _Start_

![image](assets/it/03.webp)

## Registrace účtu WoS

V tomto okamžiku je služba Wallet spuštěna, ale pro větší bezpečnost nastavíme přihlašovací jméno: to bude sloužit k obnovení prostředků v případě poruchy nebo ztráty zařízení. Poté vyberte nabídku v levém horním rohu.

![image](assets/it/04.webp)

Otevře se celé okno nabídky, ve kterém stačí nastavit měnu (Wallet z Satoshi ve výchozím nastavení představuje americký dolar jako referenční měnu) a barvu motivu (světlá/tmavá) podle vašeho vkusu. Ostatní ovládací prvky nepoužívejte.

Vzhledem k tomu, že WoS je správcovský nástroj, nemůžeme zálohovat Wallet pomocí věty Mnemonic. Můžeme však umožnit WoS získat naše prostředky v případě ztráty nebo nepoužívání mobilního zařízení kliknutím na _Přihlášení/Registrace_

![image](assets/it/07.webp)

Zobrazí se okno, ve kterém jsme vyzváni k zadání e-mailu Address. Může to být **protonový e-mail** (doporučujeme), nicméně funguje, protože právě ten nám umožní získat zpět prostředky Wallet v případě ztráty/odcizení nebo rozbití mobilního telefonu

![image](assets/it/08.webp)

Wallet z Satoshi odeslal zprávu do nahlášené e-mailové schránky

![image](assets/it/09.webp)

Ve schránce nalezneme dvě slova, která musíme zadat a přepsat do prostoru, který nám aplikace nabídne


- neaktivujte překladač: slova jsou a měla by zůstat v angličtině**
- přepsat obě slova a dávat pozor na velká/malá písmena**

![image](assets/it/10.webp)

Po přepsání dvou slov klikněte na tlačítko _OK_

![image](assets/it/11.webp)

Výsledkem je, že se nahoře objeví obrázek se symbolem zaškrtnutí pro ověření

![image](assets/it/12.webp)

zatímco v sekci nastavení se nyní v červeném pruhu _Přihlášení/Registrace_ zobrazuje e-mail uživatele Address.

![image](assets/it/13.webp)

## Přijímání plateb

Chcete-li přijímat na WoS, klikněte na tlačítko _Přijmout_ a zobrazí se řada příkazů.

![image](assets/it/14.webp)

Můžete získat


- prostřednictvím LN-Address **a**
- prostřednictvím LN, nastavení Invoice **b**
- on chain (WoS podporuje síť Bitcoin, ale s podmořskými výměnami za poplatek) **c**
- zarámování QR kódu LNurl-p **d**

![image](assets/it/15.webp)

## Vytvoření Invoice

Klikněte na _Příjem_ a vyberte příkaz se symbolem Lightning Network

![image](assets/it/16.webp)

Zobrazí se pouze nabídka pro vytvoření Invoice, kde klikneme na tlačítko _Přidat částku_ a napíšeme přesnou částku a přidáme popis, v tomto příkladu "Můj první Invoice"

![image](assets/it/17.webp)

Pomocí klávesnice nastavíme částku

![image](assets/it/18.webp)

a pak si nechat zaplatit Invoice. Přijatá platba vypadá takto:

![image](assets/it/19.webp)

## Sběr z pokladny

Wallet z Satoshi má ve výchozím nastavení zajímavou funkci, díky které je vhodný zejména pro obchodníky: POS. Podívejme se, jak ji aktivovat.

Na hlavní obrazovce vyberte nabídku v pravém horním rohu

![image](assets/it/20.webp)

Poté vyberte možnost _Místo prodeje_

![image](assets/it/21.webp)

V nejnovější verzi WoS věnujte pozornost výběru _Keypad_

![image](assets/it/22.webp)

a poté na klávesnici zadejte částku, která se v následujícím příkladu rovná 18 centům / 118 Sats. Přidejte popis sbírky, v tomto případě "moje druhá s pokladnou" Rozsvítí se velké tlačítko Green, na které je třeba kliknout

![image](assets/it/23.webp)

gW-44 a ukázat ji například klientovi.

![image](assets/it/24.webp)

Tato platba se také vybírá!

![image](assets/it/25.webp)

## Odesílání plateb

Jednoduchost je silnou stránkou hlavní obrazovky WoS. Chcete-li zaplatit za službu Invoice, klikněte na tlačítko _Odeslat_

![image](assets/it/26.webp)

Při prvním použití požádá systém WoS o oprávnění k přístupu ke kameře

![image](assets/it/27.webp)

Od tohoto okamžiku je kamera aktivována

![image](assets/it/28.webp)

V rámci položky Invoice vidíme, že byla požadována platba ve výši 210 Sats. Také se načte popis, pokud jej žadatel zadal. Tato obrazovka je shrnutím a zároveň žádostí o potvrzení: WoS "žádá o povolení" k odeslání platby, které je uděleno kliknutím na tlačítko Green _Odeslat_

![image](assets/it/29.webp)

Když platba dorazí na místo určení, systém WoS zobrazí toto upozornění

![image](assets/it/30.webp)

Na hlavní obrazovce se po kliknutí na _Historie_ (hned pod zůstatkem) zobrazí seznam transakcí

![image](assets/it/31.webp)

### Obnovení účtu WoS

Nyní se podíváme, jak nainstalovat službu WoS do nového zařízení; to se bude hodit i v případě krádeže, ztráty nebo nemožnosti ovládat mobilní telefon, na kterém byla služba Wallet nainstalována dříve. Po opětovné instalaci je třeba zopakovat právě vysvětlený postup registrace účtu s jednou obměnou: na konci žádosti o přihlášení pomocí dříve nastaveného e-mailu se WoS zobrazí takto:

![image](assets/it/33.webp)

Zpráva nás upozorní, že postup pro reaktivaci účtu byl odeslán e-mailem. Je třeba otevřít poštovní schránku.

**DŮLEŽITÉ**: e-mail otevřete z počítače nebo v každém případě z jiného zařízení, než na kterém se chystáte načíst účet WoS. Ve složce doručené pošty najdeme zprávu, která nám ukáže QR kód, který je třeba zarámovat

![image](assets/it/34.webp)

Po zarámování QR kódu se načtený účet zobrazí na hlavní stránce WoS se zůstatkem a historií.