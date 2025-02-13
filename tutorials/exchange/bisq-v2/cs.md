---
name: Bisq 2
description: Kompletní průvodce používáním Bisq 2 a výměnou bitcoinů P2P
---
![cover](assets/cover.webp)

## Úvod

Pro zachování důvěrnosti a finanční nezávislosti uživatelů jsou zásadní výměnné burzy P2P (peer-to-peer) bez nutnosti KYC. Umožňují přímé transakce mezi jednotlivci bez nutnosti ověřování totožnosti, což je zásadní pro ty, kteří si cení soukromí. Chcete-li teoretickým konceptům porozumět hlouběji, podívejte se na kurz BTC204:

https://planb.network/courses/btc204
### Co je Bisq 2?

Bisq 2 je nová verze populární decentralizované burzy Bisq, která byla spuštěna v roce 2024. Na rozdíl od svého předchůdce byl Bisq 2 vyvinut tak, aby podporoval více směnných protokolů a nabízel uživatelům větší flexibilitu.

**Klíčové nové funkce:**


- Podpora více sítí pro ochranu soukromí (Tor, I2P)
- Více identit pro větší důvěrnost
- REST API pro obchodní boty
- Podpora více typů portfolia
- Systém rolí s povinným vkladem v BSQ

Tato příručka se zaměřuje výhradně na protokol "Bisq Easy", který je v současné době jediný dostupný. Protokol Bisq Easy byl navržen speciálně pro nové uživatele Bitcoinu. Tento protokol umožňuje uživatelům nakupovat a prodávat Bitcoiny za fiat měny na decentralizované platformě peer-to-peer. Transakce jsou omezeny na ekvivalent 600 USD (s minimem 6 USD) a bezpečnost výměny závisí na pověsti prodejců BTC. Bisq Easy nemá žádné obchodní poplatky ani požadavky na bezpečnostní vklad. Očekává se, že Bisq Easy nahradí Bisq 1 pro hotovostní směny pod 600 USD (nebo jejich ekvivalent).

**Hlavní funkce:**


- Aplikace pro stolní počítače napříč platformami
- K dispozici je několik výměnných protokolů
- Decentralizovaná síť P2P
- Zaměření na důvěrnost (žádné KYC, používání Tor)
- Bez svěřenectví (zachováte si kontrolu nad svými prostředky)
- Open source (AGPL)

### Rozdíly s produktem Bisq 1

**Pro kupující:**


- Nevyžaduje se žádná bezpečnostní záloha
- Žádné poplatky za obchodování
- Žádné poplatky za těžbu
- Zabezpečení na základě pověsti dodavatele
- Nižší obchodní limity (ekvivalent 600 USD)

**Pro prodejce:**


- Nevyžaduje se žádná bezpečnostní záloha
- Budování pověsti
- Možnost spalování BSQ nebo vytváření vazeb BSQ
- Potenciálně vyšší prodejní prémie (10-15 % nad tržní)

**Důležitá poznámka:** Jakmile bude protokol Bisq Multisig implementován v systému Bisq 2, bude možné starou verzi systému Bisq postupně ukončit. Bisq 1 se však bude nadále používat jako nástroj pro správu CAD Bisq a pro výměnu BSQ-BTC.

### Proces výměny


- Tvůrce nabídky definuje podmínky výměny
- Jakmile se obchodníci dohodnou na podmínkách (způsob platby a cena), začíná výměna
- Prodávající zašle kupujícímu své bankovní údaje a kupující zašle prodávajícímu svou adresu bitcoinu
- Kupující provede platbu v hotovosti a oznámí to prodávajícímu
- Po obdržení platby odešle prodávající bitcoiny na adresu kupujícího
- Výměna je dokončena, když kupující obdrží bitcoiny

### Důležitá pravidla


- Před výměnou platebních údajů lze výměnu zrušit bez udání důvodu
- Po výměně podrobností může mít neplnění povinností za následek vykázání
- U bankovních převodů **nikdy nepoužívejte v důvodu platby termíny "Bisq" nebo "Bitcoin "** (mohlo by to vést ke zmrazení prostředků nebo dokonce k zablokování bankovního účtu příjemce nebo plátce)
- Obchodníci se musí přihlásit alespoň jednou denně, aby mohli sledovat proces
- V případě problému mohou obchodníci využít služeb zprostředkovatele

## Instalace a konfigurace

### 1. Stáhněte si a ověřte Bisq 2

![Téléchargement de Bisq 2](assets/fr/01.webp)


- Přejít na [bisq.network](https://bisq.network/downloads/)
- Stáhněte si verzi aplikace Bisq 2 odpovídající vašemu operačnímu systému (posuňte stránku dolů)
- Ověřte pravost staženého souboru (důrazně doporučujeme). Podrobného průvodce ověřením podpisu naleznete v následujícím návodu:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
### 2. Instalace podle vašeho systému

Při instalaci postupujte podle pokynů příslušných pro váš operační systém. Pokud se během instalace setkáte s jakýmikoli obtížemi, můžete se podívat do podrobného průvodce na [oficiální wiki Bisq](https://bisq.wiki/Downloading_and_installing).

### 3. První spuštění


- Spusťte Bisq 2 a přijměte podmínky používání

![Conditions d'utilisation](assets/fr/01.webp)


- Vytvoření nového profilu výběrem jména a avatara

![Création du profil](assets/fr/02.webp)


- Poté se dostanete na hlavní panel aplikace, kde můžete spustit službu Bisq Easy a koupit nebo prodat své první bitcoiny

![Page d'accueil de Bisq 2](assets/fr/03.webp)

### 4. Nastavení platebních metod


- Přístup do sekce platebních účtů z hlavní nabídky

![Liste des comptes de paiement](assets/fr/04.webp)


- Přidání nového způsobu platby vyplněním požadovaných údajů

![Création d'un nouveau compte de paiement](assets/fr/05.webp)

Předkonfigurace platebních metod není povinná, ale doporučuje se, abyste ušetřili čas při obchodování. Platební metody můžete také nakonfigurovat přímo během obchodování, a to tak, že kontaktujete svého burzovního partnera.

### 5. Zabezpečení účtu

**Zálohování dat:**

Na rozdíl od Bisq 1 Bisq 2 v současné době neintegruje peněženku Bitcoin: transakce se proto provádějí prostřednictvím vašich vlastních externích peněženek. Přesto doporučujeme pravidelně zálohovat datovou složku Bisq 2. Chcete-li najít svou datovou složku, podívejte se na [oficiální wiki Bisq](https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory).

**Správa identity:**

Bisq 2 umožňuje vytvořit více identit. Každá identita může být použita pro různé typy transakcí. Vaše identity jsou uloženy ve složce dat.

## Nákup a prodej bitcoinů

### Jak koupit Bitcoiny

**Možnost 1: Využijte stávající nabídku**


- Na hlavní obrazovce vyberte "Bisq Easy", záložku "Začínáme" a klikněte na "Spustit průvodce obchodem"

![Lancer trade wizard](assets/fr/06.webp)


- Vyberte možnost "Koupit Bitcoin" a vyberte měnu

![Sélection achat Bitcoin](assets/fr/07.webp)

![Choix de la devise](assets/fr/08.webp)


- Nastavení preferovaných platebních metod (SEPA, Revolut atd.)

![Configuration méthodes de paiement](assets/fr/09.webp)


- V tuto chvíli máte buď seznam nabídek odpovídajících vašim předchozím kritériím, nebo musíte přejít do "Knihy nabídek"

![Liste des offres](assets/fr/10.webp)


- V druhém případě můžete nabídky zobrazovat a filtrovat pomocí tlačítek v pravém horním rohu rozhraní

![Filtres des offres](assets/fr/11.webp)


- Jakmile si vyberete nabídku, stačí zvolit způsob platby a poté potvrdit přehled obchodů

![Choix modalités de paiement](assets/fr/12.webp)

![Configuration du trade](assets/fr/13.webp)

![Récapitulatif du trade](assets/fr/14.webp)

**Možnost 2: Vytvořte si vlastní nabídku**


- Vyberte "Bisq Easy" a poté "Offerbook"
- Vyberte si obchodní pár (např. BTC/EUR)
- Klikněte na "Vytvořit nabídku
- Postupujte podle průvodce vytvořením nabídky: Definujte částku (pevnou nebo v rozmezí)

![Configuration du montant](assets/fr/20.webp)


- Vyberte přijímané způsoby platby

![Sélection méthodes de paiement](assets/fr/21.webp)


  - Zkontrolujte shrnutí a zveřejněte nabídku

![Récapitulatif et publication](assets/fr/22.webp)

Po zahájení výměny :


- Pošlete prodávajícímu svou adresu Bitcoin nebo fakturu Lightning

![Envoi adresse Bitcoin](assets/fr/15.webp)


- Získat bankovní údaje prodávajícího

![Réception coordonnées bancaires](assets/fr/16.webp)

![Détails coordonnées bancaires](assets/fr/17.webp)


- Proveďte platbu (bez uvedení "Bisq" nebo "Bitcoin")
- Oznámení prodávajícímu o vaší platbě

![Notification paiement](assets/fr/18.webp)


- Čekání na bitcoiny

![Attente réception](assets/fr/19.webp)

### Jak prodat bitcoiny?

Proces prodeje na serveru Bisq 2 se řídí podobnou logikou jako proces nákupu, přičemž hlavní kroky jsou stejné, ale v opačném pořadí. Můžete buď vytvořit vlastní nabídku k prodeji, nebo reagovat na existující nabídku ke koupi. Zde je rozpis jednotlivých možností a fází procesu:

**Možnost 1: Vytvoření nabídky k prodeji**


- Vyberte "Bisq Easy" a poté "Offerbook"
- Klikněte na "Vytvořit nabídku" a vyberte "Prodej bitcoinů"
- Konfigurace nabídky :
 - Zvolte měnu (EUR, USD atd.)
 - Výběr přijímaných způsobů platby
 - Nastavte částku (v rozmezí od 6 do 600 USD)
 - Nastavení ceny (pevná nebo % z trhu)
- Zkontrolujte podrobnosti a zveřejněte nabídku

**Možnost 2: Využijte stávající nabídku**


- Procházení nabídek na kartě "Kniha nabídek"
- Filtrování podle měny a způsobu platby
- Vyberte si nabídku, která vám vyhovuje
- Zkontrolujte podrobnosti a přijměte nabídku

**Proces prodeje:**

Po zahájení výměny :


   - Odeslání bankovních údajů kupujícímu
   - Čekání na adresu Bitcoin kupujícího
   - Zkontrolujte, zda je adresa platná

Po oznámení platby :


   - Zkontrolujte, zda byla na váš účet přijata platba
   - Zkontrolujte, zda částka a údaje souhlasí
   - Odeslat bitcoiny na zadanou adresu
   - Označit transakci jako dokončenou

Finalizace :


   - Počkejte na potvrzení od kupujícího
   - Zanechte zpětnou vazbu k transakci
   - Vybudujte si dobrou pověst pro budoucí prodej

**Důležité upozornění:** Jako prodejce musíte být obzvláště ostražití, pokud jde o riziko zpětných plateb. Dávejte přednost bezpečným platebním metodám a před odesláním bitcoinů vždy zkontrolujte, zda byla platba přijata.

## Správné postupy a bezpečnost

### Bezpečnostní tipy

**Pro kupující:**


- Začněte s malým množstvím
- Zkontrolujte reputaci prodejců (minimální skóre 30 000)
- Používejte pouze navrhované způsoby platby
- Před odesláním platby zkontrolujte, zda je prodávající aktivní
- Používejte pouze bankovní údaje uvedené v chatu o výměně
- Nikdy nekomunikujte mimo platformu Bisq 2
- Uchovávejte doklady o platbě
- Nikdy neposílejte citlivé informace

**Pro prodejce:**


- Buďte opatrní u nových účtů
- Vyhněte se platebním metodám citlivým na zpětné platby (PayPal, Venmo)
- Zkontrolujte, zda údaje o účtu odpovídají kupujícímu
- Omezení komunikace na chat Bisq 2
- Zahájení mediace v případě pochybností

### Budování reputace (pro prodejce)

Chcete-li zlepšit svou reputaci na portálu Bisq jako prodávající, provádějte pravidelné transakce a udržujte profesionální komunikaci s kupujícími. Rychle reagujte na požadavky kupujících, abyste zajistili pozitivní zkušenosti. Můžete si také vytvořit dluhopis BSQ, abyste prokázali svůj závazek vůči platformě. Tyto činnosti vybudují důvěru a přilákají více kupujících.

### Řešení sporů


- Kontaktujte svůj protějšek prostřednictvím chatu
- V případě potřeby otevřete spor
- Poskytněte všechny požadované důkazy
- Postupujte podle pokynů zprostředkovatele

### Zásady ochrany osobních údajů :


- Není nutná registrace ani centralizované ověřování totožnosti
- Všechna připojení probíhají přes síť Tor (a brzy i přes I2P)
- Žádný centrální server pro ukládání dat
- Údaje o transakci jsou přístupné pouze zúčastněným stranám

### Ochrana před cenzurou :


- Plně distribuovaná síť P2P
- Využití sítě Tor (a brzy i I2P) k boji proti cenzuře
- Projekt s otevřeným zdrojovým kódem spravovaný DAO bez centralizované právnické osoby

## Výhody a nevýhody

### Výhody produktu Bisq 2


- Maximální důvěrnost**: Žádné KYC, použití Tor
- Decentralizace**: Žádný centrální server
- Bezpečnost**: Otevřený zdrojový kód, který není předmětem úschovy
- Intuitivní rozhraní**: jednodušší než Bisq 1
- Flexibilita**: Více výměnných protokolů

### Bisq 2 nevýhody


- Omezená likvidita** (prozatím) :
 - Nový protokol v počáteční fázi
 - Několik dostupných prodejních nabídek
 - Potenciálně dlouhé čekací doby na nalezení kupce
- Obchodní limity**: USD na transakci (s Bisq easy)
- Pouze pro stolní počítače**: Žádná mobilní aplikace

## Budoucí protokoly

Ačkoli je v současné době k dispozici pouze protokol Bisq Easy, pro Bisq 2 se vyvíjí několik dalších protokolů:


- Bisq Lightning**: Výměnný protokol založený na systému úschovy využívajícím kryptografii s výpočtem více stran v síti Lightning.
- Bisq MuSig**: Migrace hlavního protokolu z Bisq 1 na Bisq 2 pomocí multisig 2 na 2 s bezpečnostními zálohami.
- Výměny BSQ**: Okamžité atomové swapy mezi BSQ a BTC.
- Likvidní swapy**: Výměna aktiv v síti Liquid (USDT, BTC-L) prostřednictvím atomických swapů.
- Monero Swaps**: Výměny mezi bitcoinem a Monerem.
- Liquid MuSig**: Pro nižší náklady a vyšší důvěrnost je použita verze protokolu multisig využívající L-BTC.
- Výměny ponorek**: Výměny mezi Bitcoinem v síti Lightning a Bitcoinem v řetězci.
- Stablecoin Swapy**: Výměny mezi bitcoinem a stablecoiny v USD.
- Možnosti Multisig**: Vytvoření P2P prodejních a kupních opcí s blokováním BTC v rámci on-chain multisig transakce.
- Otevřené smlouvy Multisig**: Umožňuje vytvářet vlastní podmíněné kontrakty pomocí multisigového systému 2 na 3 s arbitráží.

Tyto protokoly se v současné době vyvíjejí a budou postupně integrovány do systému Bisq 2, což uživatelům nabídne větší flexibilitu podle jejich specifických potřeb.

## Užitečné zdroje


- Oficiální webové stránky: [bisq.network](https://bisq.network)
- Dokumentace: [Bisq Wiki](https://bisq.wiki)
- Podpora: [Fórum Bisq](https://bisq.community)
- Zdrojový kód : [GitHub](https://github.com/bisq-network)