---
name: Manjaro
description: Zpřístupnění výkonu systému Arch Linux
---
![cover](assets/cover.webp)



Arch Linux je díky své robustnosti a stabilitě oblíbeným operačním systémem v mnoha oblastech. Jeho ovládání však může být pro začínající uživatele obtížné. Právě pro řešení tohoto problému byl vytvořen systém **Manjaro**: nabízí výkon systému Arch Linux, ale s jednodušším a přístupnějším prostředím, založeným na intuitivním a snadno naučitelném systému Interface.



## Začínáme s Manjaro



Jednou z největších předností systému Manjaro je jeho **jednoduchý a efektivní systém aktualizací**. Není třeba je spravovat ručně: Manjaro se o ně postará za vás! Na dostupnost aktualizace vás upozorní ikona v oznamovací oblasti (umístění se liší podle edice). Stačí jen postupovat podle pokynů a proces je rychlý a bezproblémový.



Manjaro také nabízí **rozsáhlý katalog aplikací**. Jelikož je Manjaro založeno na Arch Linuxu, těží z přímého přístupu k jeho oficiálním repozitářům, které jsou bohaté na nejrůznější software, včetně proprietárních aplikací. Manjaro mírně zpožďuje některé aktualizace Arch Linuxu kvůli dodatečnému testování; to zvyšuje stabilitu za cenu mírného zpoždění nových verzí. A pokud vám tato možnost volby nestačí, máte také přístup k **AUR (*Arch User Repository*)**, obrovské knihovně spravované komunitou. Pokud nějaký program neexistuje v oficiálních repozitářích, je pravděpodobné, že je k dispozici v AUR.



Další výhodou systému Manjaro je, že je **mnohem méně náročný na zdroje** než systémy jako Windows nebo macOS. Spotřebovává méně paměti RAM a výpočetního výkonu, takže je ideální volbou pro starší nebo méně výkonné počítače: váš počítač získá na plynulosti a rychlosti a znovu získá druhé mládí.



Navíc je Manjaro **úplně zdarma**. Na rozdíl od Windows nebo macOS nemusíte za jeho instalaci a maximální využití nic platit. V neposlední řadě nabízí **zvýšené zabezpečení** díky pravidelným a rychlým aktualizacím, které omezují vystavení zranitelnostem. Jeho aktivní komunita také zajišťuje, že případné problémy jsou rychle opraveny a jsou navržena účinná řešení.



## Objevte operační systém Manjaro



Než začnete instalovat Manjaro, je důležité vědět, že tato distribuce je k dispozici v několika edicích. Každá z těchto edic nabízí jedinečné pracovní prostředí, které ovlivňuje práci i spotřebu systémových prostředků. Existují tři hlavní oficiální edice distribuce Manjaro.



![0_01](assets/fr/01.webp)





- Nejvíce přizpůsobitelná je edice **KDE Plasma**. Pokud hledáte systém, který je vizuálně elegantní a zároveň vysoce výkonný, je KDE Plasma vynikající volbou. Toto stabilní desktopové prostředí je ideální pro uživatele, kteří chtějí mít naprostou kontrolu a přizpůsobené prostředí.





- Pro počítače s omezenějšími prostředky je ideálním řešením edice **Xfce**. Její Interface je lehká a intuitivní a zaručuje bezproblémový provoz i na starších počítačích. Navíc svým rozvržením připomíná systém Windows, což novým uživatelům usnadňuje přechod na Linux.





- A konečně edice **GNOME** nabízí zcela odlišný přístup. Její zjednodušený design klade důraz na produktivitu a organizaci prostřednictvím virtuálních pracovních prostorů. Toto pracovní prostředí zaměřené na činnosti je obzvláště atraktivní pro uživatele, kteří již znají Linux a hledají minimalistické, vysoce efektivní prostředí.



### Další vydání Manjaro



![0_02](assets/fr/02.webp)



Kromě oficiálních vydání nabízí komunita Manjaro i další verze. Tyto alternativní edice jsou navrženy tak, aby vyhovovaly specifickým potřebám, a nabízejí různá desktopová prostředí.



Edice **Cinnamon** je vynikající volbou, pokud právě začínáte a hledáte známou verzi Interface. Byla navržena tak, aby se snadno používala a zároveň zachovávala klasické konvence tradičních kancelářských prostředí.



Pro pokročilejší uživatele jsou k dispozici edice jako **i3 Window Manager** nebo **Sway**. Jsou mnohem lehčí a rychlejší, nicméně k jejich plné konfiguraci a využití je třeba dobře ovládat příkazový řádek. Tato prostředí jsou ideální pro ty, kteří chtějí mít nad svým systémem naprostou kontrolu a kterým je efektivita nade vše.



## Technické požadavky



Aby systém Manjaro fungoval optimálně, musí váš počítač splňovat několik minimálních požadavků. Doporučujeme, abyste měli alespoň :





- **64bitový (x86_64)** procesor
- doporučené 4 GB RAM (minimálně 2 GB) (viz níže)
- 30 GB místa na disku (více, pokud vytvoříte vyhrazený oddíl `/home`)



## Instalace systému Manjaro



Pro stažení přejděte na [oficiální webové stránky Manjaro](https://manjaro.org/) a vyberte si edici, která nejlépe vyhovuje vašim potřebám. Po stažení souboru je třeba vytvořit bootovací USB klíč s obrazem Manjaro ISO.



Pak přejděte na webovou stránku softwaru [Rufus] (https://rufus.ie/fr/) a stáhněte si ji. Spusťte program, připojte klíč USB, vyberte obraz ISO Manjaro a spusťte flashování. Před vyjmutím klíče počkejte na dokončení procesu. Poté můžete restartovat počítač.



![0_03](assets/fr/03.webp)



Chcete-li do počítače nainstalovat Manjaro, nejprve jej zcela vypněte. Poté připojte USB klíč, počítač znovu zapněte a vstupte do spouštěcí nabídky nebo do firmwaru UEFI/BIOS stisknutím **F2, F10, F12, Escape** nebo **Delete** (v závislosti na výrobci).



Poté vyberte klíč USB jako spouštěcí zařízení a spusťte proces instalace operačního systému.



### Spouštěcí obrazovka



Při prvním spuštění systému Manjaro z klíče USB se dostanete přímo do nabídky instalace. Před spuštěním instalace můžete změnit rozložení klávesnice nebo jazyk systému.



Poté vyberte možnost **Boot with open source drivers** a spusťte instalaci systému Manjaro. Tyto ovladače s otevřeným zdrojovým kódem jsou kompatibilní s většinou hardwaru a ve většině případů postačí. Pokud máte například grafickou kartu NVIDIA nebo požadujete vyšší grafický výkon, můžete zvolit možnost **Boot with proprietary drivers**, která používá proprietární ovladače.



![0_04](assets/fr/04.webp)



Systém se spustí ve **výchozím živém režimu**. To vám umožní otestovat funkčnost systému Manjaro a zjistit, zda vyhovuje vašim potřebám, než jej nainstalujete natrvalo. Jakmile budete připraveni, klikněte na možnost **Install Manjaro Linux**.



Vyberte požadovaný jazyk pro instalaci a klikněte na tlačítko **Další**.



![0_06](assets/fr/06.webp)



Poté vyberte svou polohu a nastavte správné časové pásmo. V této fázi můžete také změnit jazyk a formát data.



![0_07](assets/fr/07.webp)



Vyberte rozložení klávesnice. K dispozici je testovací pole pro kontrolu, zda zadané klávesy odpovídají očekávaným znakům.



![0_08](assets/fr/08.webp)



### Rozdělení disku


Máte dvě možnosti rozdělení disku.





- První a nejjednodušší možností je vymazat celý disk a nainstalovat na něj Manjaro.
- Druhá možnost umožňuje **ruční rozdělení**.



![0_09](assets/fr/09.webp)



Pro čistou instalaci doporučujeme vytvořit alespoň tři oddíly:





- První oddíl o velikosti **516 MB** (primární) pro **boot**.
- Druhý oddíl **2 GB** (logický) pro **swap**.
- Třetí oddíl pro vaše **osobní data**.



Pokud chcete souběžně instalovat další systém, musíte tento poslední oddíl rozdělit a přidělit pouze jednu část systému Manjaro (alespoň **15 GB**, aby byl zaručen správný chod systému).


### Vytvoření uživatelského účtu



Vytvoření uživatelského účtu v systému vyplněním požadovaných údajů. Nakonec nastavte heslo správce (**root**). Tento správce je **superuživatel** s plnými právy v systému a možností provádět pokročilé příkazy.



![0_10](assets/fr/10.webp)



### Výběr správného kancelářského balíku



Manjaro umožňuje vybrat si mezi **FreeOffice** a **LibreOffice**.





- Kancelářský balík **LibreOffice** je kompletnější, má širší nabídku softwaru a pokročilých funkcí.
- Naproti tomu **FreeOffice** je lehčí a obsahuje pouze to nejnutnější: **TextMaker**, **PlanMaker** a **Presentations**.



![0_11](assets/fr/11.webp)



### Shrnutí konfigurace



Na souhrnné obrazovce se zobrazí všechny nastavené parametry. V případě potřeby se můžete vrátit a provést změny, aniž by to mělo vliv na ostatní již provedená nastavení.



Poté klikněte na tlačítko **Install** a potvrďte, čímž zahájíte samotnou instalaci.



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



### Ukončení instalace



Na konci procesu zaškrtněte políčko **Restartovat nyní** a klikněte na tlačítko **Ukončit**. Systém se restartuje a **Manjaro bude připraveno k použití**.



![0_13](assets/fr/14.webp)



## První kroky s Manjaro



Instalace systému Manjaro je pouze prvním krokem. Abyste ze svého systému vytěžili co nejvíce, je zde několik užitečných informací.



### Aktualizace systému



Manjaro výrazně zjednodušuje aktualizace. Aktualizace balíčků :



```shell
sudo pacman -Syu
```



Tento příkaz stáhne a nainstaluje nejnovější dostupné verze. Doporučujeme jej spouštět pravidelně, abyste udrželi svůj systém **bezpečný a stabilní**.



### Konfigurace vývojového prostředí



Chcete-li v systému Manjaro vyvíjet webové aplikace, nainstalujte základní nástroje jediným příkazem:



```shell
sudo pacman -S nodejs npm git yarn
```



Tento příkaz nainstaluje Node.js a npm pro spouštění a správu projektů JavaScript a TypeScript, Git pro správu verzí a Yarn jako alternativního správce balíčků.



### Instalace Bitcoin Wallet



Chcete-li spravovat své bitcoiny v systému Manjaro, můžete si nainstalovat **Electrum**, lehký a bezpečný nástroj Wallet :



```shell
sudo pacman -S electrum  # Install Electrum
```



Electrum vám umožní **snadno přijímat a odesílat bitcoiny** a zároveň nabízí pokročilé funkce, jako je správa více Wallet a ochrana passphrase. Kompletního průvodce používáním služby Electrum najdete v našem specializovaném tutoriálu, který vysvětluje, jak vytvořit Wallet, zabezpečit své prostředky a provádět transakce.



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

## Zabezpečení systému Manjaro



Bezpečnost je klíčovým aspektem každé instalace systému Linux. Je důležité, abyste chránili důvěrnost a integritu svých dat.



### Konfigurace brány firewall



Manjaro obsahuje UFW (*Uncomplicated Firewall*), program pro správu firewallů se síťovými filtry, ale musíte jej aktivovat ručně:



```bash
# Installation if not present
sudo pacman -S ufw

# Firewall activation
sudo systemctl enable ufw.enable

sudo ufw enable

# Allow SSH connections (optional)
sudo ufw allow ssh

# Check the status
sudo ufw status verbose
```



![verbose](assets/fr/15.webp)



### Správa oprávnění uživatelů



1. **Vytvoření neprivilegovaného uživatele**



```shell
sudo useradd -m username
sudo passwd username
```



2. **Konfigurace souboru Sudoers**



```shell
sudo EDITOR=nano visudo
```



Nyní jste připraveni používat Manjaro Linux na svém počítači. Díky jeho **jednoduché instalaci**, **snadným aktualizacím** a **flexibilitě** získáte výkonný a vysoce výkonný systém vhodný pro vývoj, každodenní používání a správu bitcoinů pomocí nástrojů, jako je Electrum.



Manjaro kombinuje **stabilitu, rychlost a bezpečnost** a zároveň zůstává **výhradně zdarma**, takže je ideální volbou pro začátečníky i pokročilé uživatele. Věnujte čas prozkoumání jeho různých funkcí a přizpůsobte si prostředí podle svých potřeb. Pokud chcete získat více odborných znalostí a poznat systém Arch Linux, doporučujeme vám náš výukový kurz.



https://planb.academy/tutorials/computer-security/operating-system/arch-linux-7a3dc8a8-629b-4971-bb0d-4eab94f93973