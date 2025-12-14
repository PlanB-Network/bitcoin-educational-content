---
name: Pop!_OS
description: Průvodce instalací linuxové distribuce Pop!_OS
---

![cover](assets/cover.webp)



## Úvod



Pop!OS je operační systém založený na Linuxu, který vyvinul **System76**, americký výrobce specializující se na stroje pro vývojáře, designéry a pokročilé uživatele.



Pop!OS je navržen tak, aby nabízel moderní, stabilní a vysoce výkonné prostředí, vyznačuje se jednoduchým ovládáním, výkonnými nástroji a silným zaměřením na produktivitu.



### Kdo je System76?



System76 je americká společnost založená v roce 2005 se sídlem v Denveru, která se specializuje na výrobu notebooků, stolních počítačů a serverů určených speciálně pro Linux.



Na rozdíl od tradičních výrobců vyvíjí System76 stroje, které jsou otevřené, opravitelné a orientované na svobodu softwaru.



Společnost System76 nevyrábí pouze počítače.



Společnost také vyvíjí :




- Pop!OS**, vlastní operační systém založený na Linuxu;
- COSMIC**, moderní, vysoce výkonné desktopové prostředí používané systémem Pop!OS ;
- Open Firmware**, firmware s otevřeným zdrojovým kódem založený na systému Coreboot ;
- nástroje pro vývojáře a návrháře.



Cílem je nabídnout vysoce kvalitní integraci hardwaru a softwaru srovnatelnou s ekosystémem společnosti Apple, ale zcela otevřenou a zaměřenou na Linux.



## Moderní, stabilní a dostupný systém



Pop!OS staví na základech systému Ubuntu a poskytuje mu vynikající stabilitu, širokou hardwarovou kompatibilitu a přístup k rozsáhlému softwarovému ekosystému.


Nabízí elegantní rozhraní, pracovní plochu COSMIC, která je navržena tak, aby byla plynulá, intuitivní a přizpůsobitelná i pro nové uživatele.



## Ideální volba pro vývojáře, designéry a náročné uživatele



Pop!OS ocení zejména :





- vývojáři (předinstalované nástroje, pokročilá správa dlaždic),
- uživatelé s grafickými kartami Nvidia nebo AMD,
- studenti a profesionálové, kteří hledají spolehlivý systém,
- uživatelé systému Windows, kteří chtějí jednoduše přejít na jiný systém.



Obsahuje automatické dlaždice, přehledné centrum softwaru a integrované nástroje produktivity, které usnadňují každodenní používání.



## Nejdůležitější informace o systému Pop!OS





- Optimalizovaný výkon** díky pravidelným aktualizacím.
- K dispozici jsou dvě verze ISO**: standardní a optimalizovaná pro Nvidii.
- Zvýšené zabezpečení** (při instalaci je k dispozici šifrování LUKS).
- Interface COSMIC** ergonomický a moderní.
- Vysoce kompatibilní** se softwarem Ubuntu a Flatpak.



## Stáhněte si POP!OS bezpečně



### 1. Předpoklady



Před stažením a instalací systému POP!OS je třeba provést několik úkonů, abyste správně připravili instalační prostředí.



### Požadované vybavení





- Kompatibilní počítač**: Procesor Intel nebo AMD, grafický procesor Intel / AMD / Nvidia.
- Alespoň 4 GB RAM** (pro pohodlné používání se doporučuje 8 GB).
- minimálně 20 GB volného místa** (doporučuje se 40 GB nebo více).
- Klíč USB** o velikosti minimálně 4 GB k vytvoření instalačního média.



### Připojení k internetu



Stabilní připojení je užitečné pro :





- stáhnout obraz ISO,
- instalovat aktualizace po instalaci.



Pop!OS lze spustit i bez připojení, ale instalace přes internet je mnohem plynulejší.



### Zálohování dat



Pokud má Pop!OS nahradit jiný systém (Windows, Ubuntu atd.) nebo s ním koexistovat, doporučujeme před zahájením práce zálohovat důležité soubory.



### Zkontrolujte přítomnost grafického procesoru Nvidia (pokud je k dispozici)



U počítačů vybavených grafickou kartou Nvidia je třeba stáhnout speciální obraz ISO, který obsahuje ovladače Nvidia.


Tato kontrola je velmi jednoduchá:





- nahlédnutím do specifikací počítače,
- nebo vyhledáním modelu grafické karty v nastavení systému.



### Stáhněte si z oficiálních stránek



Obraz ISO systému Pop!OS je třeba stáhnout přímo z oficiální stránky System76: [system76.com/pop](https://system76.com/pop/).



Na této stránce je vždy k dispozici nejnovější verze přizpůsobená vašemu hardwaru.



![capture](assets/fr/03.webp)



### Vyberte si verzi: Standardní nebo Nvidia, nebo Raspberry Pi (ARM64)



Pop!OS je k dispozici ve třech variantách:



### Standardní verze



Doporučeno pro počítače používající :





- procesor intel nebo AMD;
- integrovaným grafickým procesorem Intel nebo AMD;
- grafickou kartu AMD Radeon.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Verze Nvidia



Doporučeno pro počítače vybavené grafickými kartami Nvidia.


Tento obraz již obsahuje ovladače Nvidia, což usnadňuje instalaci a omezuje problémy s grafikou.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Verze Raspberry Pi (ARM64)



Pro Raspberry Pi 4 a 400 (procesor ARM).


Jedná se o specifickou verzi pro tyto minipočítače, která je přizpůsobena architektuře ARM.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## Vytvoření spouštěcího klíče USB



Můžete použít několik nástrojů, například Balena Etcher :





- Stáhněte si a nainstalujte [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Otevřete Balena Etcher a vyberte obraz ISO systému Pop!OS.
- Jako cílové médium vyberte klíč USB.
- Klikněte na tlačítko Flash a počkejte na dokončení procesu.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Instalace a zabezpečení systému Pop!OS



### Zavedení systému z klíče USB





- Vypněte počítač.
- Připojte USB klíč (obsahující Pop!OS).
- Zapněte počítač. Na nejnovějších počítačích by měl systém automaticky rozpoznat spouštěcí klíč USB. Pokud tomu tak není, restartujte počítač podržením přístupové klávesy systému BIOS/UEFI (obvykle F2, F12 nebo Delete, v závislosti na značce).
  - V nabídce BIOS/UEFI vyberte jako spouštěcí zařízení klíč USB.
  - Uložit a restartovat.



### Spuštění instalace



Jakmile vyberete spouštěcí USB klíč jako spouštěcí zařízení, počítač se spustí do prostředí Pop!OS Live.



Vyberte jazyk.



![Capture](assets/fr/10.webp)



Vyberte místo.



![Capture](assets/fr/11.webp)



Vyberte jazyk pro zadávání z klávesnice.



![Capture](assets/fr/12.webp)



Vyberte rozložení klávesnice.



![Capture](assets/fr/13.webp)



Pro standardní instalaci zvolte možnost `Čistá instalace`. Tato možnost je nejlepší pro nové uživatele Linuxu, ale mějte na paměti, že odstraní veškerý obsah cílové jednotky. Případně můžete zvolit možnost `Try Demo Mode` a pokračovat v testování Pop!OS v živém prostředí.



![Capture](assets/fr/14.webp)



Výběrem možnosti `Vlastní (Pokročilé)` získáte přístup k aplikaci GParted. Tento nástroj umožňuje nastavit pokročilé funkce, jako je duální spouštění systému, vytvoření samostatného oddílu `/home` nebo umístění oddílu `/tmp` na jinou jednotku.



Klepnutím na `Rozmazat a nainstalovat` nainstalujete Pop!OS na vybranou jednotku.



![Capture](assets/fr/15.webp)



### Konfigurace uživatelského účtu



Další část instalačního programu vás provede vytvořením uživatelského účtu, abyste se mohli přihlásit do nového operačního systému.



Zadejte celé jméno (může obsahovat libovolný text, velká nebo malá písmena) a uživatelské jméno (musí být psáno malými písmeny):



![Capture](assets/fr/16.webp)



Po vytvoření účtu budete vyzváni k nastavení nového hesla.



![Capture](assets/fr/17.webp)



### Šifrování celého disku



Šifrování systémového disku není nutné, ale zaručuje bezpečnost uživatelských dat v případě, že někdo získá neoprávněný fyzický přístup k zařízení.



Disk lze zašifrovat pomocí přihlašovacího hesla zaškrtnutím políčka `Heslo pro šifrování je stejné jako heslo k uživatelskému účtu`. Toto políčko můžete také zrušit a dole vybrat možnost `Nastavit heslo`. Chcete-li proces šifrování disku ignorovat, vyberte možnost `Nešifrovat`.



![Capture](assets/fr/18.webp)



Pokud jste zvolili tlačítko `Nastavit heslo`, zobrazí se další výzva k nastavení šifrovacího hesla.



Přejděte k dalšímu kroku instalačního programu. Pop!OS nyní zahájí instalaci na disk.



![Capture](assets/fr/19.webp)



Po dokončení instalace restartujte počítač a přihlaste se, abyste dokončili proces konfigurace uživatelského účtu.



Pokud jste změnili pořadí spouštění tak, abyste při spuštění upřednostnili Live USB klíč, vypněte počítač úplně a vyjměte instalační USB klíč. Pokud jste v režimu dual-boot, stiskněte příslušné klávesy pro přístup ke konfiguraci a vyberte jednotku obsahující instalaci Pop!OS.



![Capture](assets/fr/20.webp)



### Grafika NVIDIA



Pokud jste instalovali z ISO Intel/AMD a váš systém je vybaven samostatnou grafickou kartou NVIDIA nebo pokud jste ji přidali později, budete muset pro dosažení optimálního výkonu nainstalovat ovladače pro vaši kartu ručně. Pro instalaci ovladače spusťte v příkazovém terminálu následující příkaz:



```bash
sudo apt install system76-driver-nvidia
```



Grafické ovladače NVIDIA můžete také nainstalovat z obchodu Pop!_Shop.



![Capture](assets/fr/20.webp)



## Instalace základních nástrojů



Pop!OS nabízí širokou škálu softwaru prostřednictvím svého Pop!Shopu, ale mnoho základních nástrojů lze nainstalovat také přes terminál pomocí `apt` nebo `flatpak`. Zde se dozvíte, jak nainstalovat klíčové nástroje pro kompletní pracovní prostředí.



### Instalace terminálu



| Outil                        | Description                                | Commande d’installation                         |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox                      | Navigateur web libre et populaire          | `sudo apt install firefox`                      |
| Brave                        | Navigateur web axé sur la confidentialité  | Installation via Pop!_Shop ou site officiel     |
| Visual Studio Code (VS Code) | Éditeur de code puissant pour développeurs | `flatpak install flathub com.visualstudio.code` |
| Git                          | Gestionnaire de versions                   | `sudo apt install git`                          |
| Flatpak                      | Gestionnaire de paquets alternatif         | `sudo apt install flatpak`                      |
| VLC                          | Lecteur multimédia polyvalent              | `sudo apt install vlc`                          |
| GNOME Terminal               | Terminal par défaut                        | Préinstallé sur Pop!OS                          |
| Curl                         | Outil de transfert de données en ligne     | `sudo apt install curl`                         |
| Wget                         | Téléchargement de fichiers via HTTP/FTP    | `sudo apt install wget`                         |
| Docker                       | Conteneurisation d’applications            | Installation via script officiel ou `apt`       |
| Node.js                      | Environnement JavaScript côté serveur      | Installation via `apt` ou NodeSource            |
| Python3                      | Langage de programmation                   | `sudo apt install python3 python3-pip`          |
| GIMP                         | Éditeur d’image avancé                     | `sudo apt install gimp`                         |
| Thunderbird                  | Client mail                                | `sudo apt install thunderbird`                  |
| Transmission                 | Client BitTorrent léger                    | `sudo apt install transmission-gtk`             |
| Htop                         | Moniteur de système interactif             | `sudo apt install htop`                         |

### Instalace prostřednictvím služby Pop! Shop (grafické rozhraní)





- V hlavní nabídce otevřete **Pop!_Shop**.
- Pomocí vyhledávacího řádku vyhledejte požadované aplikace (například "Brave").
- U každé aplikace klikněte na tlačítko **Install**.
- Pop!_Shop automaticky spravuje závislosti a aktualizace.



## Aktualizace systému



### Možnost 1: Prostřednictvím grafického uživatelského rozhraní (GUI)



Pop!OS obsahuje jednoduchý a intuitivní grafický správce aktualizací.



1. Klikněte na **hlavní nabídku** (ikona vlevo dole).


2. Otevřete **"Pop!_Shop "**.


3. V aplikaci Pop!_Shop klikněte na kartu **"Aktualizace "**.


4. Systém automaticky vyhledá dostupné aktualizace.


5. Klepnutím na **"Aktualizovat vše "** zahájíte instalaci aktualizací.


6. Na požádání zadejte své heslo.


7. Nechte proces dokončit a v případě potřeby jej znovu spusťte.



### Možnost 2: Přes terminál



Otevřete terminál a zadejte příkaz :



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### Správa uživatelů



Pro běžné operace doporučujeme používat standardní uživatelský účet s právy sudo.



Vytvoření nového uživatele :



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



Odhlaste se a znovu se přihlaste pod tímto novým uživatelem.



### Správa grafického ovladače





- U karet Nvidia zkontrolujte, zda jsou nainstalovány proprietární ovladače:



```bash
sudo apt install system76-driver-nvidia
```





- U AMD/Intel jsou ovladače obvykle zahrnuty ve výchozím nastavení.



### Aktivace brány firewall (UFW)



Pop!OS ve výchozím nastavení neblokuje síťový provoz. Pro zvýšení bezpečnosti aktivujte UFW:



```bash
sudo ufw enable && sudo ufw status verbose
```



### Konfigurace automatických aktualizací



Udržování systému v aktuálním stavu bez nutnosti ručního zásahu:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### Přizpůsobení vzhledu a chování





- Otevřete **Nastavení systému** → **Vzhled** a vyberte světlý nebo tmavý motiv.
- Konfigurace aktivních rohů, animací a rozšíření prostřednictvím správce COSMIC.
- Upravte rozložení pracovní plochy tak, abyste optimalizovali pracovní postupy.



### Konfigurace automatického zálohování



Systém Pop!OS integruje nástroje, jako je Deja Dup pro zálohování:





- Spusťte **Zálohování** z nabídky.
- Vyberte externí disk nebo síťové umístění.
- Naplánujte pravidelné zálohování.



### Instalace užitečných rozšíření GNOME/COSMIC



Zde je několik doporučených rozšíření pro zlepšení uživatelského komfortu:





- Dash to Dock**: panel aplikací je vždy viditelný.
- GSConnect**: synchronizace se systémem Android.
- Indikátor schránky**: pokročilá správa schránky.



Nainstalujte je prostřednictvím :



```bash
sudo apt install gnome-shell-extensions
```



Poté je aktivujte v nastavení.



### Optimalizace správy paměti a swapu



Zkontrolujte stav výměny:



```bash
swapon --show
```



V případě potřeby zvětšete velikost odkládací paměti nebo nakonfigurujte odkládací soubor :



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



Přidejte jej do souboru `/etc/fstab` pro automatické připojení.



## Správa balíčků a úložišť



### Porozumění zdrojům balíčků



Pop!OS, založený na Ubuntu, využívá především :





- Oficiální repozitáře Ubuntu**: pro většinu stabilního softwaru.
- Úložiště System76**: pro ovladače, firmware a specifické nástroje.
- Flatpak**: přístup k široké škále aplikací se sandboxem.
- Snap** (nepovinné): další univerzální formát balíčku.



---

### Přidávání a správa repozitářů PPA



Pro instalaci často aktualizovaného softwaru lze přidat určité soubory PPA (Personal Package Archives):



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## Závěr



Pop!OS je moderní a stabilní linuxová distribuce vhodná pro začátečníky i pokročilé uživatele.



Díky intuitivnímu rozhraní COSMIC a integrovaným nástrojům nabízí plynulý a produktivní provoz, ať už jde o vývoj, tvorbu nebo každodenní používání.



Tento návod se zabývá hlavními fázemi: přípravou, stahováním, instalací, počátečním nastavením a základními nástroji.



Neváhejte dále zkoumat Pop!OS a přizpůsobit si prostředí tak, abyste z něj vytěžili co nejvíce.