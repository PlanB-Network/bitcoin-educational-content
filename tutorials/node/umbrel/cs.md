---
name: Deštník
description: Objevte a nainstalujte Umbrel - Váš uzel Bitcoin a domovský server
---

![cover](assets/cover.webp)



## Úvod



### Co je to uzel Bitcoin?



Uzel Bitcoin je počítač, který se účastní sítě Bitcoin tím, že na něm běží software Bitcoin Core nebo alternativní klient. Jeho úloha je zásadní pro provoz a bezpečnost sítě:





- Úložiště Blockchain**: Udržuje úplnou a aktuální kopii Blockchain Bitcoin
- Ověřování transakcí**: ověřuje každou transakci a blok podle pravidel protokolu
- Šíření informací**: Sdílí nové transakce a bloky s ostatními uzly
- Budování konsensu**: Přispívá k uplatňování pravidel sítě



Provozování vlastního uzlu Bitcoin je zásadním krokem k finanční nezávislosti a nabízí několik klíčových výhod:





- Důvěrnost**: Sdílejte své transakce, aniž byste své údaje prozradili třetím stranám
- Odpor proti cenzuře**: Nikdo vám nemůže zabránit v používání Bitcoin
- Nezávislé ověření**: Při ověřování vašich transakcí není třeba důvěřovat cizím uzlům
- Vytváření konsensu**: Přispívejte k uplatňování pravidel sítě Bitcoin
- Síťová podpora**: Staňte se aktivním účastníkem distribuce a decentralizace sítě



### Deštník: Jednoduché řešení pro provoz uzlu Bitcoin



Umbrel je operační systém s otevřeným zdrojovým kódem, který zjednodušuje instalaci a správu uzlu Bitcoin. Zároveň promění váš počítač v osobní a soukromý domácí server, který usnadňuje hostování :





- Kompletní uzel Bitcoin
- Bitcoin základní aplikace (Electrs, Mempool.space)
- Další osobní služby (cloudové úložiště, streamování, VPN atd.)



Díky elegantnímu a intuitivnímu uživatelskému rozhraní Interface zpřístupňuje společnost Umbrel samoobslužné služby všem, přičemž si zachovává plnou kontrolu nad svými daty.



## Možnosti instalace deštníku



Společnost Umbrel nabízí dva hlavní způsoby použití svého řešení: možnost na klíč (Umbrel Home) a bezplatnou verzi s otevřeným zdrojovým kódem (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: Řešení na klíč



Umbrel Home je předkonfigurovaný domácí server, speciálně navržený pro optimální zážitek. Toto hardwarové řešení "vše v jednom" obsahuje:



**Funkce hardwaru**




- Vysoce výkonný procesor optimalizovaný pro selfhosting
- Předinstalované vysokorychlostní úložiště SSD
- Tichý chladicí systém
- Kompaktní, elegantní design
- Integrované porty USB a Ethernet



**Exkluzivní výhody**




- Instalace Plug-and-play: zapojte a jeďte
- Prémiová podpora se specializovanou asistencí
- Zaručené automatické aktualizace
- Integrovaný průvodce migrací
- Plná záruka na hardware
- Plná podpora všech funkcí



**Cena**: 399 € (cena se může lišit podle sezóny)



### UmbrelOS: Verze s otevřeným zdrojovým kódem



UmbrelOS je svobodná verze operačního systému Umbrel s otevřeným zdrojovým kódem. Toto flexibilní řešení vám umožní používat vlastní hardware a zároveň využívat základní funkce systému Umbrel.



**Výhody**




- Zcela zdarma
- Otevřený a ověřitelný zdrojový kód
- Svoboda volby
- Pokročilé možnosti přizpůsobení



**Podporované platformy**




- Raspberry Pi 5: oblíbené a cenově dostupné řešení
- Systémy X86: Pro standardní počítače nebo servery
- Virtuální počítač: Pro testování nebo použití na stávající infrastruktuře



**Omezení




- Pouze podpora Společenství
- Některé pokročilé funkce vyhrazené pro Umbrel Home
- Další technická počáteční konfigurace
- Výkon závisí na zvoleném hardwaru



Tato verze je ideální pro :




- Techničtí uživatelé
- Ti, kteří již vlastní kompatibilní zařízení
- Lidé, kteří se chtějí učit a experimentovat
- Vývojáři, kteří chtějí přispět k projektu



Oficiální instalační odkazy :




- [Instalace na Raspberry Pi 5](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Instalace na systémech x86 (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Instalace virtuálního počítače](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



V tomto návodu se zaměříme na instalaci systému UmbrelOS na Raspberry Pi 5, ale základní principy zůstávají podobné i pro jiné platformy.



## Instalace operačního systému Umbrel na Raspberry Pi 5



### Požadované součásti



Pro tuto instalaci budete potřebovat :





- Raspberry Pi 5 (4 GB nebo 8 GB RAM)
- Oficiální napájení Raspberry Pi Supply (zásadní pro stabilitu!)
- Karta MicroSD (minimálně 32 GB)
- Čtečka karet microSD
- Externí disk SSD pro ukládání dat
- Ethernetový kabel
- Kabel USB pro připojení disku SSD



### Instalační kroky



**Stáhnout UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Navštivte [oficiální webové stránky](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Stáhněte si nejnovější verzi UmbrelOS pro Raspberry Pi 5



**Balena Etcher** instalace



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Stáhněte si a nainstalujte [Balena Etcher](https://www.balena.io/etcher/) do počítače



**Příprava karty microSD**



![Insertion carte microSD](assets/fr/03.webp)




- Vložte kartu microSD do čtečky karet v počítači



**Obrázek bliká**



![Flashage UmbrelOS](assets/fr/04.webp)




- Spuštění Balena Etcher
- Vyberte staženou bitovou kopii systému UmbrelOS
- Zvolte kartu microSD jako cíl
- Klikněte na "Flash!" a počkejte na dokončení procesu
- Bezpečné vysunutí karty



**Instalace karty microSD



![Installation microSD](assets/fr/05.webp)




- Vložení karty microSD do počítače Raspberry Pi 5



**Připojení periferie**



![Connexion périphériques](assets/fr/06.webp)




- Připojení externího disku SSD k dostupnému portu USB
- Připojení ethernetového kabelu mezi počítačem Pi a směrovačem



**Zapnutí napájení



![Démarrage du Pi](assets/fr/07.webp)




- Připojení oficiálního napájení Raspberry Pi Supply
- Počkejte několik minut, než se systém spustí



**První přístup**



![Accès interface web](assets/fr/08.webp)




- Na zařízení připojeném ke stejné síti otevřete prohlížeč
- Přístup na webovou stránku Interface společnosti Umbrel na adrese: `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Pokud soubor `umbrel.local` nefunguje, je třeba zjistit IP adresu Address počítače Raspberry Pi v místní síti. Můžete :




- Podívejte se do příručky Interface vašeho směrovače
- Použití síťového skeneru, jako je nmap
- V terminálu počítače použijte příkaz `arp -a`



## První krok na Umbrel



Jakmile je aplikace Umbrel spuštěna a přístupná prostřednictvím prohlížeče, postupujte podle následujících kroků:



### Počáteční konfigurace



**Vytvořte si účet**



![Création compte](assets/fr/10.webp)




- Výběr uživatelského jména
- Nastavení bezpečného hesla
- Pro přístup ke službě Umbrel budete potřebovat tyto přihlašovací údaje



**Potvrzení účtu



![Confirmation compte](assets/fr/11.webp)




- Kliknutím na "Další" získáte přístup k ovládacímu panelu



**Objevení Interface**



![Interface Umbrel](assets/fr/12.webp)




- Přístup do obchodu s aplikacemi Umbrel
- Objevte mnoho dostupných aplikací
- Začněme instalací základních aplikací pro Bitcoin



### Instalace aplikací Bitcoin



**Bitcoin Node**



![Bitcoin Node](assets/fr/13.webp)




- První aplikace k instalaci
- Stáhněte si a zkontrolujte celou knihu Blockchain Bitcoin



**Volitelé**



![Installation Electrs](assets/fr/14.webp)




- Server Electrum pro připojení peněženek Bitcoin
- Synchronizuje se s uzlem Bitcoin



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Displej Interface pro Blockchain
- Sleduje transakce a bloky v reálném čase



## Sledování transakce pomocí Mempool.space



Mempool.space je open-source průzkumník Blockchain, který poskytuje vizualizaci sítě Bitcoin v reálném čase. Umožňuje sledovat transakce a pochopit, jak se transakce v síti šíří.



### Porozumění Mempool a potvrzením



"Mempool" (paměťový fond) je jako virtuální čekárna, kde jsou uloženy všechny nepotvrzené transakce Bitcoin před jejich zařazením do bloku. Zde je uveden způsob zpracování transakce:



1. **Vysílání**: Při odesílání transakce je tato transakce nejprve vysílána v síti Bitcoin


2. **Čekání v Mempool**: Čeká na výběr v Miner na základě nákladů


3. **První potvrzení**: Nezletilý ji zahrne do bloku (1. potvrzení)


4. **Další potvrzení**: Každý nový blok vytěžený po bloku obsahujícím vaši transakci přidává potvrzení



Doporučený počet potvrzení závisí na množství :




- Pro malá množství: stačí 1-2 potvrzení
- Pro velké množství: 6 potvrzení se obecně považuje za velmi bezpečné



### Prozkoumejte Interface z Mempool.space



1. **Na domovské stránce** najdete přehled sítě Bitcoin:




   - Nedávno vytěžené bloky
   - Odhady nákladů pro různé priority
   - Současný stav Mempool



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Vyhledat transakci**: Chcete-li sledovat konkrétní transakci, vložte její identifikátor (txid) do vyhledávacího řádku v horní části stránky.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### Analýza podrobností o transakci



Po nalezení transakce vám Mempool.space nabídne kompletní analýzu:



1. **Důležité informace** :




   - Stav (potvrzený nebo nepotvrzený)
   - Vyplacené výdaje (v Sats/vB)
   - Odhadovaná doba potvrzení



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **Struktura transakce** :




   - Vizuální zobrazení vstupů a výstupů
   - Podrobný seznam dotčených adres
   - Převedené částky



3. **Technické údaje** :




   - Transakční hmotnost
   - Virtuální velikost
   - Použitý formát a verze
   - Další specifická metadata



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Výhody používání Mempool.space v systému Umbrel



1. **Důvěrnost**: Vaše požadavky procházejí přes váš vlastní uzel


2. **Nezávislost**: Není třeba spoléhat na služby třetích stran


3. **Spolehlivost**: Přístup k datům i při výpadku veřejných prohlížečů



Pomocí této aplikace můžete efektivně sledovat své transakce, pochopit, jak poplatky ovlivňují rychlost potvrzení, a lépe porozumět fungování sítě Bitcoin.



## Připojení zařízení Wallet Bitcoin k uzlu



### Konfigurace Electrs



**Místní připojení



![Connexion locale](assets/fr/18.webp)




- Pro použití v místní síti
- Rychlejší a snadnější nastavení



**Vzdálené připojení přes Tor**



![Connexion Tor](assets/fr/19.webp)




- Přístup k uzlu odkudkoli
- Bezpečnější a soukromější



### Propojení se Sparrow Wallet



**Přístup k parametrům



![Paramètres Sparrow](assets/fr/20.webp)




- Otevřený vrabec Wallet
- Přejděte do nabídky Předvolby > Server
- Klikněte na "Upravit existující připojení"



**Výběr typu připojení



Sparrow nabízí tři režimy připojení:



***Veřejný server***




- Připojení k veřejným serverům (např. blockstream.info, Mempool.space)
- Jednoduché, ale méně soukromé



***Bitcoin Core***




- Přímé připojení k uzlu Bitcoin
- Soukromé, ale pomalejší



***Soukromé elektrum***




- Připojení k serveru Electrs
- Spojení důvěrnosti a výkonu



**Konfigurace voličů**



Typ připojení zvolte podle informací zobrazených v aplikaci Electrs, kterou jsme viděli dříve:



V obou případech ponechte možnosti "Použít SSL" a "Použít proxy" nezaškrtnuté.



**Místní připojení


Hostitel: umbrel.local


Číslo portu: 50001



**Vzdálené připojení (Tor)**


Hostitel : [your-Address-onion]


Číslo portu: 50001



Připojení Tor je nutné, pokud chcete k uzlu přistupovat mimo místní síť.



![Configuration connexion](assets/fr/21.webp)


Další informace o softwaru Sparrow Wallet naleznete v obsáhlém výukovém programu :


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Závěr



Deštník je nyní připraven k použití. Aktivně se zapojíte do sítě Bitcoin a zároveň si zachováte plnou kontrolu nad svými daty. Neváhejte a prozkoumejte mnoho dalších aplikací, které jsou k dispozici v obchodě s aplikacemi Umbrel a rozšiřují možnosti vašeho domácího serveru.



## Užitečné zdroje



### Oficiální dokumentace




- [Oficiální webové stránky Umbrel](https://umbrel.com)
- [Dokumentace k deštníku](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)



### Aplikace Bitcoin




- [Bitcoin Core](https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Sparrow Wallet](https://sparrowwallet.com)



### Společenství




- [Fórum Deštník](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitter Umbrel](https://twitter.com/umbrel)