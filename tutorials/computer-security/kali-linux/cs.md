---
name: Kali
description: Instalace Kali Linuxu do VirtualBoxu, na bootovací USB disk nebo jako dual boot, krok za krokem.
---

![cover-kali](assets/cover.webp)



## Úvod



### Proč Kali Linux?



**Kali Linux** je linuxová distribuce specializovaná na bezpečnost IT.


Zde je důvod, proč používáme Kali Linux:





- Je předkonfigurován s širokou škálou pentestovacích nástrojů (testy zabezpečení systému a sítě).
- Je **otevřený a svobodný**, takže jej můžete volně používat a upravovat.
- Je **spolehlivý a bezpečný**, ideální pro výuku kybernetické bezpečnosti.
- Umožňuje naučit se používat Linux v prostředí připraveném k testování.
- Lze jej instalovat různými způsoby: **VirtualBox**, **spouštěcí klíč USB** nebo **duální spouštění**.



## Instalace a konfigurace



### 1. Předpoklady



**Potřebné vybavení:**





- 64bitový procesor** (Intel nebo AMD).
- minimálně 8 GB RAM** (pro nenáročnou instalaci nebo virtuální počítač může stačit 4 GB).
- 50 GB volného místa na disku** pro instalaci systému Kali Linux.
- Připojení k internetu** pro stažení obrazu ISO a aktualizací.
- Minimálně 8 GB USB klíč** pro vytvoření bootovacího média (pokud chcete Kali nainstalovat na počítač nebo otestovat na Live USB).



Před instalací do stávajícího počítače je důležité zálohovat data.



### 2. Stáhnout





- Přejděte na [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Vyberte obraz ISO pro vaši aplikaci:
  - Instalační obraz** : pro instalaci na PC.
  - Virtuální obraz**: pro instalaci Kali do VirtualBoxu nebo VMware.
- Stáhněte si obraz ISO.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Vytvoření spouštěcího klíče USB



Můžete použít několik nástrojů, například Balena Etcher :





- Stáhněte si a nainstalujte [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Otevřete Balena Etcher a vyberte obraz ISO Kali.
- Jako cílové médium vyberte klíč USB.
- Klikněte na tlačítko Flash a počkejte na dokončení procesu.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Instalace a zabezpečení systému Kali Linux



#### 4.1 Zavedení systému na klíči USB





- Vypněte počítač.
- Připojte USB klíč (obsahující Kali Linux).
- Zapněte počítač. Na nejnovějších počítačích by měl systém automaticky rozpoznat spouštěcí klíč USB. Pokud tomu tak není, restartujte počítač podržením přístupové klávesy systému BIOS/UEFI (obvykle F2, F12 nebo Delete, v závislosti na značce).
  - V nabídce BIOS/UEFI vyberte jako spouštěcí zařízení klíč USB.
  - Uložit a restartovat.



#### 4.2 Spuštění instalace



##### Spouštěcí obrazovka



Při zavádění z USB klíče by se měla zobrazit spouštěcí obrazovka systému Kali Linux. Vyberte si mezi **grafickou instalací** a **textovou instalací**. V tomto příkladu jsme se rozhodli pro grafickou instalaci.



![capture](assets/fr/06.webp)



Pokud použijete obrázek **Live**, zobrazí se další režim, **Live**, který je také výchozí možností spuštění.



![Mode Live](assets/fr/07.webp)



##### Výběr jazyka



Zvolte preferovaný jazyk instalace a systému.



![Sélection de la langue](assets/fr/08.webp)



Uveďte prosím svou zeměpisnou polohu.



![Options d'accessibilité](assets/fr/09.webp)



##### Konfigurace klávesnice



Vyberte rozložení klávesnice. Pro kontrolu, zda klávesy odpovídají vaší konfiguraci, je k dispozici testovací pole.



![Configuration du clavier](assets/fr/10.webp)



##### Připojení k síti



Instalace nyní prohledá síťová rozhraní, vyhledá službu DHCP a vyzve vás k zadání názvu hostitele pro váš systém. V příkladu níže jsme jako název hostitele zadali **"kali "**.



![Configuration réseau](assets/fr/11.webp)



Volitelně můžete zadat výchozí název domény, který bude tento systém používat (hodnoty lze získat z DHCP nebo pokud existuje již existující operační systém).



![Choix du type d'installation](assets/fr/12.webp)



##### Uživatelské účty



Dále vytvořte uživatelský účet pro systém (celé jméno, uživatelské jméno a silné heslo).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Časové pásmo



Pro nastavení systémového času vyberte zeměpisnou oblast.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Typ rozdělení



Instalační program poté prohledá disky a zobrazí několik možností v závislosti na konfiguraci.



V této příručce začínáme s **prázdným diskem**, což nám dává **čtyři možné volby**.


Vybereme možnost **Povedené - použít celý disk**, protože zde provádíme jednorázovou instalaci systému Kali Linux (single boot). To znamená, že nebude zachován žádný jiný operační systém a celý disk může být vymazán.



Pokud již disk obsahuje data, může se zobrazit další možnost **Povedené - použít největší souvislé volné místo**.



Tato alternativa umožňuje nainstalovat Kali Linux bez odstranění stávajících dat, což je ideální pro duální zavádění s jiným systémem.



V našem případě je disk prázdný, takže se tato možnost nezobrazí.



![Choix du partitionnement](assets/fr/17.webp)



Vyberte disk, který chcete rozdělit.



![capture](assets/fr/18.webp)



V závislosti na svých potřebách si můžete vybrat, zda chcete mít všechny soubory v jednom oddílu (výchozí chování), nebo zda chcete mít samostatné oddíly pro jeden nebo více adresářů nejvyšší úrovně.



Pokud si nejste jisti, co chcete, vyberte možnost **Všechny soubory v jednom oddíle**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Poté budete mít poslední možnost zkontrolovat konfiguraci disku, než instalační program provede nevratné změny. Po kliknutí na tlačítko _Continue_ se spustí instalační program a instalace bude téměř dokončena.



![capture](assets/fr/21.webp)



##### Šifrovaný LVM



Pokud byla tato možnost v předchozím kroku povolena, Kali Linux nyní provede bezpečné vymazání pevného disku předtím, než vás požádá o heslo LVM.



Použijte silné heslo, jinak se zobrazí upozornění na slabé heslo passphrase.



##### Informace o zmocněnci



Kali Linux používá k distribuci aplikací repozitáře. Pokud vaše prostředí používá proxy server, musíte zadat potřebné informace.



Pokud si nejste jisti**, zda chcete použít proxy server, **vynechte prázdné pole**. Zadání nepravdivých údajů zabrání připojení k úložištím.



![capture](assets/fr/22.webp)



##### Metapety



Pokud přístup k síti nebyl nakonfigurován, je třeba jej na výzvu **dále konfigurovat**.



Pokud používáte obrázek **Live**, další krok se nezobrazí.



Poté můžete vybrat [metabalíčky](https://www.kali.org/docs/general-use/metapackages/), které chcete nainstalovat. Výchozí možnosti nainstalují standardní systém Kali Linux, takže nebudete muset nic upravovat.



![capture](assets/fr/23.webp)



#### Informace o spuštění



Poté potvrďte instalaci zavaděče GRUB.



![capture](assets/fr/24.webp)



##### Restartování



Nakonec klikněte na tlačítko Pokračovat a restartujte novou instalaci Kali Linuxu.



![capture](assets/fr/25.webp)



#### 4.3 Aktualizace a konfigurace systému Kali Linux po instalaci



Důležitým krokem po nové instalaci je aktualizace systému. Máte dvě možnosti:



##### Možnost 1: Prostřednictvím grafického uživatelského rozhraní (GUI)



Kali, stejně jako Debian/Ubuntu, nabízí integrovaného grafického správce aktualizací.



1. Klikněte na **hlavní nabídku** (vlevo nahoře nebo dole v závislosti na ploše).


2. Otevřete **"Software Updater "**.


3. Nástroj bude :




    - Zkontrolujte balíčky, které mají být aktualizovány.
    - Zobrazí se seznam (s velikostmi a verzemi).
    - Umožňuje spustit aktualizaci jediným kliknutím.


4. Na výzvu zadejte heslo správce (`sudo`).


5. Nechte jej nainstalovat a v případě potřeby restartujte.



##### Možnost 2: Přes terminál



Otevřete terminál a spusťte :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Účet **root** není vhodné používat pro každodenní práci; vytvořte si raději uživatele, který není root.



V terminálu zadejte tyto příkazy:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Odhlaste se a znovu se přihlaste jako nový uživatel.



Shrňme si některé základní úlohy Kali Linuxu do tabulky.



### Základní úlohy pod Kali Linuxem




| **Kategorie** | **Základní úkol** | **Popis / Cíl** | **Hlavní metoda** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Navigace v systému** | Otevřít terminál | Přístup k hlavnímu příkazovému řádku Kali | Klikněte na ikonu terminálu nebo použijte `Ctrl + Alt + T` |
| | Procházet složky | Pohyb v adresářové struktuře systému | `cd /cesta/ke/slozce`, `ls` pro výpis souborů |
| | Vytvořit / smazat složku | Organizace souborů | `mkdir nazev_slozky`, `rm -r nazev_slozky` |
| **Správa souborů** | Kopírovat / přesunout soubor | Manipulace se soubory v terminálu | `cp soubor cil`, `mv soubor cil` |
| | Smazat soubor | Uvolnění místa na disku | `rm nazev_souboru` |
| | Zobrazit obsah textového souboru | Rychlé čtení souboru | `cat soubor.txt`, `less soubor.txt` |
| **Správa systému** | Aktualizovat Kali Linux | Instalace nejnovějších verzí a bezpečnostních oprav | `sudo apt update && sudo apt full-upgrade -y` |
| | Instalovat software | Přidání nového nástroje nebo utility | `sudo apt install nazev_balicku` |
| | Smazat software | Vyčištění systému | `sudo apt remove nazev_balicku` |
| | Vyčistit nepotřebné závislosti | Získání místa na disku | `sudo apt autoremove` |
| **Sítě a internet** | Ověřit síťové připojení | Testování přístupu k internetu | `ping google.com` |
| | Identifikovat IP adresu | Zjištění síťové konfigurace | `ip a` nebo `ifconfig` |
| | Změnit Wi-Fi síť | Připojení k jinému přístupovému bodu | Ikona sítě → Vybrat požadovanou Wi-Fi |
| **Účty a oprávnění** | Spustit příkaz jako správce | Dočasné získání root práv | `sudo prikaz` |
| | Vytvořit nového uživatele | Přidání lokálního účtu | `sudo adduser uzivatelske_jmeno` |
| | Změnit heslo | Zabezpečení účtu | `passwd` |
| **Vzhled a pohodlí** | Změnit tapetu | Přizpůsobení plochy | Pravé kliknutí na plochu → **Nastavení plochy** |
| | Změnit motiv / ikony | Zlepšení čitelnosti a estetiky | Nastavení → Vzhled / Motivy |
| **Nástroje Kali** | Otevřít nabídku nástrojů | Průzkum testovacích a bezpečnostních nástrojů | Nabídka **Aplikace → Kali Linux** |
| | Spustit nástroj (např. nmap, wireshark) | Praktické objevování bezpečnostních utilit | `sudo nmap`, `wireshark` atd. |
| **Nápověda a dokumentace** | Získat nápovědu k příkazu | Pochopení příkazu před jeho použitím | `man prikaz` nebo `prikaz --help` |

## Závěr



Instalace Kali Linuxu je jen prvním krokem k objevení tohoto výkonného prostředí určeného pro kybernetickou bezpečnost. Zvládnutím základních úloh a správy systému může každý začít zkoumat vestavěné nástroje a pochopit vnitřní fungování systému Linux. Systém Kali nabízí vynikající výukovou platformu jak pro upevnění technických dovedností, tak pro rozvoj skutečné kultury bezpečnosti IT.