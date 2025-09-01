---
name: Debian
description: Distribuce Linuxu proslulá svou stabilitou, robustností a kompatibilitou.
---

![cover](assets/cover.webp)



Debian je svobodná distribuce GNU/Linuxu, která je známá svou robustností a spolehlivostí. Její linuxové jádro a všechny balíčky jsou důkladně testovány, aby byla zajištěna stabilita a vysoká úroveň zabezpečení. Debian je vhodný pro servery i pracovní stanice a nabízí snadné používání a rozsáhlý katalog softwaru. Ať už hledáte bezpečný systém pro každodenní použití nebo produkční prostředí, Debian je tou správnou volbou.



## Proč si vybrat Debian?





- Zdarma a otevřeně**: Debian je zcela otevřený, což zaručuje transparentnost a žádné licenční poplatky.
- Stabilita a bezpečnost**: Každé vydání prochází důkladným testováním, díky čemuž je Debian jednou z nejspolehlivějších a nejbezpečnějších distribucí na trhu.
- Aktivní komunita**: rozsáhlá komunita a rozsáhlá dokumentace jsou vám k dispozici, kdykoli je třeba.
- Lehký a škálovatelný**: Debian můžete nainstalovat na počítače se skromnými zdroji při zachování dobrého výkonu.
- Rozsáhlý katalog softwaru**: v repozitářích je k dispozici více než 50 000 oficiálních balíčků.



## Výběr grafiky Interface



Debian nabízí několik desktopových prostředí, která vyhovují vašim potřebám:





- GNOME**: moderní, intuitivní prostředí Interface, ideální pro začátečníky. Nabízí plynulé a snadno použitelné grafické menu pro přístup k aplikacím.
- XFCE**: lehký a rychlý, ideální pro méně výkonné počítače.
- KDE Plasma**: vysoce přizpůsobitelné prostředí se vzhledem podobným systému Windows.
- Cinnamon**: jednoduchý a elegantní systém Interface inspirovaný systémem Windows.
- LXDE / LXQt**: velmi lehký, vhodný pro starší počítače.
- MATE**: jednoduchý a klasický, blízký starému GNOME.



💡 Pro pohodlné a snadné uchopení doporučujeme **GNOME**.



## Instalace a konfigurace Debianu


### Požadavky na hardware



Před zahájením instalace se ujistěte, že máte následující vybavení:





- Klíč USB**: pro uložení spouštěcího obrazu ISO je třeba mít k dispozici minimálně 8 GB.
- Paměť RAM (Random Access Memory)**: 4 GB pro bezproblémovou instalaci a provoz.
- Místo na disku**: alespoň 15 GB volného místa pro systém a aktualizace.



### Stáhnout



Výběr obrazu Debianu závisí na architektuře procesoru:





- AMD64**: stáhněte si "live hybrid" edici ze seznamu [download] (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- ARM64**: získejte obraz DVD z oficiálních stránek [Debianu] (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- Ostatní architektury**: najděte ISO odpovídající vaší architektuře [zde](https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Vytvoření spouštěcího klíče USB



Po stažení příslušného obrazu ISO přejděte k vytvoření instalačního média:




- Stáhněte si Balena Etcher** z [oficiální webové stránky](https://etcher.balena.io/), poté získejte binární soubor pro svůj systém a nainstalujte jej.



![etcher](assets/fr/02.webp)





- Spusťte Etcher**: otevřete software a vyberte dříve stažený obraz ISO Debianu.
- Zvolte klíč USB**: jako cíl zadejte svůj klíč (8 GB+).
- Spustit flash**: klikněte na **Flash!** a počkejte, až se proces dokončí.



![flash](assets/fr/03.webp)



Nyní je váš USB klíč připraven k zahájení instalace Debianu.



## Instalace Debianu do systému



### Zavedení systému z klíče USB



Spuštění instalace z klíče USB:




- Úplně vypněte** počítač.
- Restartujte počítač** a poté přejděte do systému BIOS/UEFI okamžitým stisknutím kláves `ESC`, `F2`, `F11` (nebo vyhrazené klávesy v závislosti na značce).
- Ve spouštěcí nabídce vyberte jako spouštěcí zařízení **klíč USB**.
- Potvrzením** klávesou Enter spustíte obraz Debianu: dostanete se na uvítací obrazovku instalátoru.



### Spuštění instalace



Úvodní obrazovka:



![starting](assets/fr/04.webp)



Při zavádění systému z paměti USB nabízí uvítací obrazovka Debianu několik možností:




- Live System**: spustí Debian bez instalace, ideální pro testování prostředí.
- Spustit instalátor**: spustí instalaci přímo na disku Hard.
- Rozšířené možnosti instalace**: umožňuje přístup k přizpůsobeným režimům instalace.



Chcete-li prozkoumat Debian v živém režimu, vyberte možnost **Živý systém** a potvrďte ji tlačítkem **Enter**. Instalaci pak spustíte kliknutím na **Install Debian** v živém prostředí.



![system](assets/fr/05.webp)





- Volba jazyka** (volitelné)



Ze seznamu vyberte hlavní jazyk systému Debian a klikněte na tlačítko OK.



![language](assets/fr/06.webp)





- Časové pásmo** (GMT)



Pro automatické nastavení data a času zvolte zeměpisnou zónu.



![timezone](assets/fr/07.webp)





- Rozložení klávesnice



Vyberte jazyk a rozložení klávesnice. Pomocí vestavěného testovacího pole zkontrolujte, zda každá klávesa vytváří očekávaný znak.



![keyboard](assets/fr/08.webp)



### Rozdělení disku





- Vymazat disk**: pokud máte vyhrazený oddíl, tato možnost odstraní veškerý jeho obsah.
- Ruční vytváření oddílů**: zvolte tuto možnost a vytvářejte, měňte velikost nebo odstraňujte oddíly podle potřeby.



![disk](assets/fr/09.webp)





- Vytvoření uživatelského účtu



Zadejte své celé jméno, název účtu a silné heslo, abyste zajistili bezpečnost své relace.



![user](assets/fr/10.webp)





- Shrnutí parametrů**



Zobrazí se přehled vašich voleb: zaškrtněte každou položku a v případě potřeby se vraťte k úpravě.



![settings](assets/fr/11.webp)





- Spuštění instalace



Klepnutím na **Install** zahájíte kopírování souborů a konfiguraci systému a počkáte na dokončení procesu.



![install](assets/fr/12.webp)





- Restart**



Po dokončení instalace restartujte počítač, abyste použili všechny konfigurace a získali přístup k novému systému Debian.



![restart](assets/fr/13.webp)



Při spuštění zadejte uživatelské jméno a heslo pro přístup do systému.



![login](assets/fr/14.webp)



## Aktualizace systému



Než začnete systém používat, je nutné jej aktualizovat. Můžete tak využívat nejnovější softwarové záplaty, aktuální úložiště a v některých případech i bezpečnostní záplaty pro samotný operační systém.



### Možnost 1: Aktualizace pomocí grafického prostředí Interface (GNOME)



Pokud máte nainstalovaný Debian s prostředím GNOME, můžete aktualizace provádět graficky. Za tímto účelem otevřete aplikaci **Software** a přejděte na kartu **Aktualizace**. Poté klikněte na možnost **Znovu spustit a aktualizovat** a spusťte proces.



### Možnost 2: Aktualizace přes terminál (doporučeno)



Tato metoda nabízí dokonalejší kontrolu. Umožňuje aktualizovat repozitáře, softwarové balíčky a v případě potřeby i jádro.




- Otevřete terminál pomocí klávesové zkratky `Ctrl + Alt + T`.
- Aktualizujte seznam dostupných balíčků pomocí následujícího příkazu:



```shell
sudo apt update
```



Po výzvě zadejte heslo (všimněte si, že se při psaní nezobrazují žádné znaky - to je normální).





- Instalace dostupných aktualizací:



```shell
sudo apt full-upgrade
```



## Objevte základní úkoly



### Procházení internetu



Výchozím webovým prohlížečem v Debianu je **Firefox**. Pokud dáváte přednost jinému prohlížeči, můžete si nainstalovat jiný, pokud je k dispozici v repozitářích Debianu (například Chromium, Brave...).



### Zpracování textu



V Debianu je ve výchozím nastavení nainstalován kancelářský balík **LibreOffice**.





- K psaní dokumentů použijte **LibreOffice Writer**, obdobu aplikace Microsoft Word.
- Pro tabulky slouží **LibreOffice Calc** jako alternativa k aplikaci Excel.
- A konečně **LibreOffice Impress** umožňuje vytvářet prezentace stejně jako PowerPoint.



## Instalace aplikací



V Debianu lze aplikace instalovat dvěma způsoby:



### Grafická metoda:



Ke snadnému vyhledávání a instalaci aplikací můžete použít **správce softwaru** (přístupný prostřednictvím grafického rozhraní Interface).



### Metoda příkazového řádku:



Pokud se hledaná aplikace nezobrazuje v grafickém okně Interface nebo pokud dáváte přednost terminálu, použijte následující příkaz:



```shell
sudo apt install <name>
```



Nahraďte `<název>` názvem balíčku. Například pro instalaci `curl`:



```shell
sudo apt install curl
```



### Instalace ručně staženého balíčku:



Pokud jste si stáhli soubor `.deb` (balíček Debianu), můžete jej nainstalovat pomocí následujícího příkazu:



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

Váš systém Debian je nyní nainstalován a připraven k používání pro každodenní úkoly.


Díky pracovnímu prostředí **GNOME** máte přístup k široké škále aplikací prostřednictvím uživatelsky přívětivého grafického prostředí Interface, které je ideální pro začátečníky i pokročilé uživatele.



Je také možné změnit desktopové prostředí (např. na XFCE, KDE atd.), aniž byste museli Debian přeinstalovat. K tomu stačí použít terminál a nainstalovat nové prostředí podle vlastního výběru.



Chcete-li se dozvědět více o Debianu a obecněji o distribucích GNU/Linuxu, doporučuji vám tento kurz:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1