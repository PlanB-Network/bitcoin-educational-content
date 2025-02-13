---
name: Peach
description: Kompletní průvodce používáním Peach a výměnou bitcoinů P2P
---
![cover](assets/cover.webp)

![peach](https://youtu.be/ziwhv9KqVkM)

## Úvod

Pro zachování důvěrnosti a finanční nezávislosti uživatelů jsou zásadní výměnné burzy P2P (peer-to-peer) bez nutnosti KYC. Umožňují přímé transakce mezi jednotlivci bez nutnosti ověřování totožnosti, což je zásadní pro ty, kteří si cení soukromí. Chcete-li teoretickým konceptům porozumět hlouběji, podívejte se na kurz BTC204:

https://planb.network/courses/btc204
### 1. Co je to broskev?

Peach je výměnná platforma P2P, která uživatelům umožňuje nakupovat a prodávat bitcoiny bez nutnosti KYC. Nabízí intuitivní rozhraní a pokročilé bezpečnostní funkce. Ve srovnání s jinými řešeními, jako jsou Bisq, HodlHodl a Robosat, Peach vyniká snadným používáním a nízkými poplatky.

### 2. Ochrana soukromí a shromažďování údajů

**Jaké informace Peach shromažďuje?

Společnost Peach se snaží ukládat naprosté minimum údajů o svých uživatelích. Zde je přehled údajů uložených na jejích serverech:


- Hash vašeho jedinečného identifikátoru aplikace (AdID)
- Hash vašich platebních údajů
- Vaše šifrované konverzace
- Údaje o transakcích, aby se zajistilo, že anonymní uživatelé nepřekročí obchodní limit (typy použitých platebních metod, částky nákupu a prodeje)
- Adresy používané k odesílání a přijímání z účtu úschovy
- Údaje o používání (Firebase a Google Analytics), pouze s vaším souhlasem

Připomínáme, že hash je podobně jako šifrování nerozpoznatelný údaj. Stejná data vždy vytvoří stejný hash, což umožňuje odhalit duplicity bez znalosti původních dat.

*Další informace o hashování naleznete v tomto kurzu:*

https://planb.network/courses/cyp201
**Kdo může vidět mé platební údaje?


- Vaše platební údaje vidí pouze vaše protistrana
- Data jsou přenášena přes servery Peach, ale jsou plně šifrována od konce ke konci
- V případě sporu budou vaše platební údaje a historie konverzace viditelné přidělenému zprostředkovateli Peach

## Instalace a konfigurace

### 1. Instalace aplikace Peach

![Installation de Peach](assets/fr/01.webp)


- Aplikaci si stáhněte ze stránek [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/).
- Postupujte podle pokynů k instalaci v zařízení.
- Během instalace budete vyzváni, abyste si zvolili, zda si přejete sdílet určité údaje za účelem vylepšení aplikace Peach (obrázek 1)
- Na další obrazovce (obrázek 2) máte dvě možnosti:
 - Pokud jste nový uživatel, klikněte na "Nový uživatel" a vytvořte si nový profil
 - Pokud již účet máte, obnovte svůj stávající profil pomocí funkce "Obnovit"
- Pokud máte doporučující kód, můžete ho zadat zde.
- Chcete-li obnovit existující účet (obrázek 3), budete potřebovat :
 - Váš záložní soubor
 - Heslo pro dešifrování tohoto souboru

### 2. Přehled hlavních obrazovek

Aplikace Peach je uspořádána do čtyř hlavních obrazovek přístupných ze spodního navigačního panelu:

![Navigation dans l'application](assets/fr/02.webp)


- Domů** : Hlavní obrazovka pro nákup a prodej bitcoinů. Zde můžete vytvářet nové transakce a přistupovat k dostupným nabídkám.
- Peněženka**: Vaše integrovaná bitcoinová peněženka, která vám umožní :
 - Zkontrolujte si zůstatek
 - Přijímání bitcoinů
 - Odeslat bitcoiny
 - Zobrazení historie transakcí
- Živnosti** : Vaše centrum pro správu obchodu, kde najdete :
 - Vaše aktuální transakce
 - Kompletní historie vašich výměn
 - Stav každé transakce
- Nastavení** : Konfigurační centrum vašeho účtu pro :
 - Správa platebních metod
 - Konfigurace zálohování
 - Přizpůsobení předvoleb
 - Přístup k pomoci a podpoře

### 3. Konfigurace platebních metod

![Accès aux paramètres de paiement](assets/fr/03.webp)

Přístup k platebním metodám přes kartu Nastavení (obrázek 8)

**Online platby

![Configuration des paiements en ligne](assets/fr/04.webp)


- Kliknutím na tlačítko přidáte nový způsob platby
- Zvolte si měnu
- Vyberte preferovaný způsob platby

*Dostupné typy platebních metod:*

***Bankovní převody jsou k dispozici: ***


- SEPA (standardní nebo okamžitá)
- Vyplňte své bankovní údaje SEPA

***Přijímáme online peněženky :***


- V závislosti na zemi máte k dispozici několik možností (Revolut, Paypal, Wise, Strike atd.)
- Podle pokynů přidejte své přihlašovací údaje

***Dárková karta, kterou lze použít :***


- Amazon
- Zadejte zemi vydání karty a další potřebné informace

***Národní možnosti platby:***

Platební systémy specifické pro jednotlivé země :


- Satispay (Itálie)
- MB Way (Portugalsko)
- Bizum (Španělsko)
- Rychlejší platby (Velká Británie)

***Osobní platby:***

![Configuration des paiements en personne](assets/fr/05.webp)


- Vyberte možnost "Meetup
- Pak si ze seznamu vyberte schůzku

### Návod k použití


- Můžete nastavit několik platebních metod současně
- Čím více metod přidáte, tím širší nabídku budete mít k dispozici
- Před registrací zkontrolujte, zda jsou vaše údaje správné
- Způsoby platby můžete kdykoli změnit nebo odstranit

**Bezpečnostní poznámka**: Vaše platební údaje jsou šifrovány a sdíleny pouze s vaším směnným partnerem během transakce.

### 4. Jak zabezpečit své portfolio

**Pochopení účtu Peach

Účet Peach není tradiční účet s přihlašovacím jménem a heslem. Jedná se o soubor uložený lokálně v telefonu, což znamená, že Peach nepotřebuje ukládat vaše údaje ani znát vaši identitu: vy máte vše pod kontrolou. Tento soubor obsahuje všechny vaše údaje, od klíčů k bitcoinové peněžence až po platební údaje.

Tento přístup zaručuje větší důvěrnost, ale znamená také větší odpovědnost. Ztráta telefonu bez zálohy znamená ztrátu přístupu k účtu Peach a finančním prostředkům. Proto je velmi důležité tento soubor zálohovat a chránit silným heslem.

**Vytvoření záloh**

![Accéder aux sauvegardes](assets/fr/13.webp)


- Přístup k nastavení z karty v pravém dolním rohu domovské obrazovky
- V nabídce nastavení vyberte možnost "zálohování"

![Processus de sauvegarde](assets/fr/06.webp)

K dispozici jsou dva typy zálohování:

**Uložení souboru účtu (obrázek 14)**


- Klikněte na "Vytvořit novou zálohu"
- Vytvoření silného hesla pro zašifrování záložního souboru
- Uložte tento soubor na bezpečném místě

Záloha souborů obnoví celý účet Peach včetně :


- Vaše portfolio
- Vaše platební metody
- Historie konverzace
- Platební údaje
- Historie transakcí s údaji o protistraně

**Uložení fráze pro obnovení (obrázek 15)**


- Podle pokynů zobrazte frázi pro obnovení
- Pečlivě zapište slova ve správném pořadí
- Tuto zálohu uložte na bezpečném místě, ideálně jinde než soubor s účtem

Fráze pro obnovení obnovuje pouze :


- Přístup k vašemu účtu
- Vaše bitcoinové fondy

Ztratíte :


- Historie konverzace
- Platební údaje
- Informace o protistraně v historii transakcí

Pro optimální zabezpečení doporučujeme provádět oba typy zálohování.

## Nákup a prodej bitcoinů

### 1. Jak koupit Bitcoiny

![Création et vue des offres](assets/fr/07.webp)


- Na domovské obrazovce klikněte na tlačítko "Koupit" (obrázek 16)
- Konfigurace nákupu podle vašich preferencí (obrázek 17)
- Prohlédněte si seznam dostupných nabídek (obrázek 18)

![Sélection et confirmation d'achat](assets/fr/08.webp)


- Vyberte si nabídku, která vám vyhovuje (obrázek 19)
- Proveďte platbu dohodnutým způsobem
- Potvrzení platby v aplikaci a vyhodnocení transakce (obrázek 20)

![Réception des bitcoins](assets/fr/09.webp)


- Sledování stavu transakce
- Kontrola potvrzení o přijetí bitcoinů
- Prostředky budou k dispozici ve vašem portfoliu Peach

### 2. Jak prodávat Bitcoiny

![Création d'un ordre de vente](assets/fr/10.webp)


- Konfigurace prodejní nabídky (obrázek 24)
- Transakci financujte odesláním bitcoinů na zadanou adresu (obrázek 25)
- Počkejte na potvrzení transakce (obrázek 26)
- Vaše nabídka je nyní viditelná pro kupující (obrázek 27)

![Attente du paiement](assets/fr/11.webp)


- Sledování stavu nabídky
- Čekání na potvrzení platby od kupujícího
- Zkontrolujte podrobnosti transakce

![Finalisation de la vente](assets/fr/12.webp)


- Kontrola stavu platby
- Potvrzení přijetí platby
- Vyhodnocení transakce
- Bitcoiny jsou automaticky uvolněny kupujícímu

**Tipy pro úspěšnou transakci**


- Rychle reagujte na zprávy od protistrany
- Pečlivě zkontrolujte platební údaje
- Pokud máte problém, neváhejte využít mediační službu

**Bezpečnostní upozornění**: Nikdy nepotvrzujte přijetí platby, dokud si neověříte, že byla přijata na váš účet.

## Výhody a nevýhody

### Výhody broskví


- KYC není vyžadováno**: Zachovává důvěrnost informací o uživateli.
- Žádný přístup k bankovním údajům**: Peach nemá přístup k vašim bankovním údajům ani k vaší identitě.
- Intuitivní rozhraní**: Snadné použití pro středně pokročilé uživatele.
- Open Source** : Zdrojový kód je veřejný a ověřitelný komunitou.

### Nevýhody broskví


- Omezená likvidita**: Menší objem obchodů než u zavedenějších platforem.
- Regulační riziko** : Aplikaci spravuje švýcarská společnost. Podléhá proto švýcarským předpisům, které se mohou vyvíjet a případně aplikaci cenzurovat.

## Užitečné zdroje


- Francouzské vysvětlující video: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Stručný průvodce: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)