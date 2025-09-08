---
name: Raspberry Pi Zero
description: Jak postavit minimální, odpojený a levný počítač pomocí Raspberry Pi Zero a sady příslušenství.
---
![cover](assets/cover.webp)



Pokud jste na stránkách Plan ₿ Network již nějakou dobu, zjistili jste, že jedním z nejvíce doporučovaných bezpečnostních nastavení, téměř nutností, **je správa finančních prostředků pomocí offline ukládání vašich soukromých klíčů**.



Pokud jste jej ještě neobjevili, v tomto návodu najdete odkazy na zdroje s otevřeným zdrojovým kódem, pomocí kterých se o něm dozvíte více.



K offline správě soukromých klíčů je tedy zapotřebí zařízení trvale odpojené od sítě, ať už se jedná o [hardware peněženku](https://planb.network/resources/glossary/hardware-wallet) nebo počítač s airgapem, určený k této specifické funkci.



Jak to udělat, pokud například nemáte možnost zakoupit hardware, který by plnil pouze tuto úlohu, ale nechcete se tohoto bezpečnostního kroku vzdát?



## Řešení


Co kdybych vám řekl, že si můžete vyrobit offline zařízení v podobě airgap počítače, který má velikost a hmotnost USB flash disku a stojí 35 eur? Nevěřili byste tomu?



Pokračovat ve čtení.



Řeknu vám víc: přečtěte si to celé. Navrhované řešení je levné, ale není právě nejjednodušší. Nejprve získáte obecnou představu, pak se rozhodnete investovat část svého času do osobního průzkumu a s co největším klidem se rozhodnete, zda a jak postupovat.



## Požadavky


**1** [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): PI Zero (bez jakéhokoli označení za názvem) je základem pro vytvoření počítače s minimálním výkonem, ale především postrádá Wi-Fi a Bluetooth karty, které jsou nezbytné pro účel tohoto cvičení.





- Cena**: v době psaní tohoto návodu (srpen 2025) přibližně 15,00.
- Kontinuita výroby**: Malina zaručuje výrobu do ledna 2030.



PI Zero bez Wi-Fi a Bluetooth jsou bohužel prakticky nedostupné. Alternativy PI Zero W a PI Zero 2W možná najdete snáze. V takovém případě můžete funkce připojení zakázat změnou konfiguračního souboru. Po instalaci operačního systému je třeba tyto položky přidat do konfiguračního souboru:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



v části této příručky se dozvíte, jak a kde to udělat. Pokud si však chcete být opravdu jisti, můžete na webu najít několik návodů na odstranění čipu Wi-Fi pomocí malé frézky, takové, která je vhodná pro práci na elektronických deskách.



**2** _startovací sada_ pro Raspberry PI Zero: jak je zvykem pro svět Malina, holé kosti, bez vnějšího pouzdra. Omezené prostředky tak malé desky navíc podmiňují možnosti spojení s vnějším světem.



Když jsem se rozhodl pokračovat, našel jsem [tuto sadu](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) plnou příslušenství, abych plně využil potenciál PI Zero. Sada totiž obsahuje napájecí adaptér USB A -> micro USB Supply, malý rozbočovač USB, adaptér mini-HDMI -> HDMI, měděný chladič a hliníkový vnější kryt. Součástí sady jsou také šroubky a imbusový klíč potřebné k umístění zařízení PI Zero do nového pouzdra.





- Náklady**: 19.99 eur.



**3** Tento návod nevyžaduje, abyste na počítač s airgapem vynakládali velké finanční prostředky. Měli byste však vědět, že budete potřebovat klávesnici a myš USB (výhradně drátovou, vyhněte se Bluetooth) a monitor. V závislosti na vstupu na monitoru budete možná potřebovat adaptér z mini-HDMI, což je jediný výstup dostupný na počítači PI Zero. Nakonec se podívejte na Hard na to, že všichni máme někde doma bezdrátovou klávesnici a myš - je čas je Dust vypnout.



## Mimořádný rozpočet



**4** Originální napájení Supply můžete získat od společnosti Raspberry, stojí asi 15,00 eur.



**5** Osobně jsem se rozhodl použít napájení Supply, které je součástí _starter kitu_, nicméně jsem ho kombinoval s kabelem USBA → miniUSB, tzv. `no data`, který stál 3,70 eur.



**6** Karta micro SD, která má mít minimálně 32 GB úložného prostoru; v případě průmyslové kvality/úrovně je lepší.



**7** Budete potřebovat systém, adaptér USB na micro SD, jako je ten, který vidíte na obrázku. Operační systém vašeho zařízení PI Zero a jeho paměť budou ve skutečnosti fungovat na tomto médiu.



![img](assets/it/06.webp)



## Instalace operačního systému


Před zavřením počítače PI Zero do kufříku doporučuji nainstalovat operační systém. Pak budete moci zkontrolovat LED diodu, která indikuje provoz, hned zpočátku.



Pro výběr a vypálení operačního systému jsem zvolil nejjednodušší způsob: pomocí nástroje Raspberry`s `PI Imager`.



![img](assets/it/01.webp)



Přejděte tedy na [Github Raspberry](https://github.com/raspberrypi/rpi-imager/releases), abyste si stáhli nejnovější verzi Imageru, a vyberte tu, která nejlépe odpovídá vašemu operačnímu systému (v. 1.9.6 v době psaní). Všimnete si, že vedle každého souboru je také hash odpovídajícího souboru. To se nám bude hodit pro ověření.



![img](assets/it/02.webp)



Doporučuji, abyste si pro svůj vlastní klid ověřili operační systém, který budete v počítači airgap používat. Získáte tak jistotu, že pracujete s legální (nikoli škodlivou) verzí Imageru a následně i Raspi OS.



Ověření proveďte ihned po stažení na počítači, který běžně používáte, připojeném k internetu



Poté otevřete terminál Linuxu a připravte stahování, přičemž vytvoříte adresář `raspios`, který bude užitečný pro práci s ním.



![img](assets/it/19.webp)



Stáhněte si Imager pro svou distribuci Linuxu pomocí `wget`.



![img](assets/it/20.webp)



Nakonec spusťte příkaz `sha256sum` a porovnejte soubor Hash s tím, který poskytuje Raspberry ve svém Githubu.



![img](assets/it/21.webp)



Pokud máte systém Windows, otevřete Power Shell a zadejte následující příkaz:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Získáte Hash, který musí odpovídat tomu, který je zveřejněn na Raspberry Github.



Po ověření stahování můžete Imager nainstalovat do svého počítače a otevřít jej. Imager je nástroj, který potřebujete k vypálení operačního systému na micro SD, což bude "systémový disk" PI Zero.



Postup je velmi jednoduchý: nejprve vyberte zařízení Raspberry, které budete používat (takže věnujte pozornost **svému modelu** Raspi Zero), poté verzi operačního systému a nakonec přípojný bod karty micro SD, na kterou chcete operační systém flashnout.



### První krok



![img](assets/it/03.webp)



### Druhý krok



![img](assets/it/07.webp)



**Dobrá poznámka**: vyberte `PI OS 32-bit`, který jako jediný funguje s PI Zero.



### Třetí krok



![img](assets/it/08.webp)



(Dávejte velký pozor, abyste ponechali zaškrtnutou možnost _Vyloučit systémovou jednotku_, abyste se vyhnuli výzvě k instalaci operačního systému Raspi do počítače.)



Když je vše nastaveno, zobrazovač se vás zeptá, zda chcete použít vlastní nastavení. Vyberte, co chcete, nebo klepněte na _No_ a pokračujte s výchozími možnostmi.



![img](assets/it/09.webp)



Potvrďte, že chcete odstranit obsah paměti micro SD



![img](assets/it/10.webp)



Imager začne flashovat operační systém na micro SD, na průběh vás upozorní posuvník.



![img](assets/it/11.webp)



Na konci je automatické ověření, doporučuji vám, abyste ho nezastavovali.



![img](assets/it/12.webp)



Nakonec se na obrazovce objeví zpráva, a pokud se vše podařilo, vypadá tak, jak čtete na obrázku.



![img](assets/it/13.webp)



Nyní můžete skutečně vyjmout micro SD z čtečky a vložit ji do slotu PI Zero. Zapněte malý Raspberry a sledujte LED: očekáváme, že bude zelený a bude blikat, což značí normální načítání operačního systému, poté by měl zůstat trvale svítit. Pokud máte jiné indikace, například pokud LED bliká pravidelně nebo je červený, podívejte se do FAQ nebo na [stránky fóra podpory](https://forums.raspberrypi.com/).



## První konfigurace


První spuštění systému Raspi OS je o něco pomalejší než obvykle, protože musí provést řadu aktuálních instalačních úloh. Pokud však vše proběhlo v pořádku, objeví se uvítací obrazovka.



![img](assets/it/14.webp)



Kliknutím na _Další_ nastavte zeměpisnou oblast, zejména pro načtení správné klávesnice. Té věnujte zvláštní pozornost.



![img](assets/it/15.webp)



Klikněte na _Další_ a budete vyzváni k vytvoření uživatele, zapište si přihlašovací údaje a dobře je uschovejte.



![img](assets/it/16.webp)



Průvodce vás požádá o výběr výchozího webového prohlížeče, mezi Chromem a Firefoxem; může se vás také zeptat na nastavení sítě Wi-Fi, pokud pracujete s PI Zero W nebo 2W. Pokračujte a klikněte na tlačítko _Skip_.



V určitém okamžiku budete vyzváni k aktualizaci palubního softwaru a operačního systému. Zvolte _Skip_: pro účely tohoto cvičení ve skutečnosti stavíme offline stroj, který musí od této chvíle zůstat offline.



Nakonec vás může požádat o povolení `ssh`, ale i tento krok odmítněte, protože se jedná o IP adresu s nulovou vzduchovou mezerou.



![img](assets/it/17.webp)



Více toho není třeba konfigurovat. Po dokončení restartujte Raspberry, aby se změny projevily.



![img](assets/it/18.webp)



## Nová počítačová vzduchová mezera


Po restartu je nový počítač airgap připraven. PI Zero vám zobrazí novou pracovní plochu, se kterou můžete pracovat buď prostřednictvím grafického rozhraní, nebo z příkazového řádku.



![img](assets/it/22.webp)



### První kroky pro PI Zero W nebo 2W


Pokud pracujete s řadou Raspberry PI Zero W nebo 2W, vaše deska má na sobě čipy pro Wi-Fi a Bluetooth. Při prvním nastavení jste přeskočili konfiguraci připojení, takže PI Zero není připojeno k internetu. Nyní můžete tyto dva čipy softwarově trvale zakázat.



Systém Raspi OS poskytuje soubor `config.txt`, který si můžete upravit podle svých představ. Soubor `config` se nachází v oddílu `boot` v adresáři `firmware` a můžete jej upravovat a ukládat s právy `root`.



Otevřete terminál z ikony vlevo nahoře a stane se z něj `kořenový`.(1)



![img](assets/it/23.webp)



(1) Pokud jste v předchozích krocích v systému Raspi OS nevytvořili heslo `root`, doporučuji vám, abyste tak učinili nyní pomocí příkazu `passwd`. Mít uživatele `root`, který se pohybuje nezávisle na vašem osobním uživateli, se může ukázat jako velmi výhodné v situacích obnovy.



V terminálu vyhledejte soubor `config.txt` a připravte se na jeho úpravu pomocí editoru `nano`.



![img](assets/it/24.webp)



Úprava by měla být provedena v dolní části celého `config`, za slovy `[All]`. V tomto okamžiku přidáte příkazy `dtoverlay` uvedené na začátku výukového programu.



![img](assets/it/25.webp)



Uložte, zavřete a restartujte. V následujícím kroku se pustíme do průzkumu malého Raspberry.



## Co od tohoto zařízení očekávat?


Podle [technických specifikací](https://www.raspberrypi.com/products/raspberry-pi-zero/) na webu Raspberry má PI Zero jednojádrový procesor BCM2835 a 512 MB RAM, takže se neočekává, že bude příliš výkonný.



Protože terminál je lehčí, budeme k prozkoumání konfigurace systému používat příkazový řádek.



Po zapnutí se zobrazí krátká obrazovka s duhovými barvami, po níž následuje uvítací zpráva od Raspberry a v levém dolním rohu zprávy jádra související se zaváděním systému.



Jakmile se zobrazí pracovní plocha systému PI OS, otevřete terminál a zadejte:



```bash
uname -a
```


Tento příkaz zobrazí na obrazovce aktuálně používanou verzi jádra a další informace.



![img](assets/it/26.webp)



Informace o procesoru a hardwaru můžete zobrazit také zadáním:



```bash
lscpu
```



![img](assets/it/27.webp)



A také viz `proc/mem/info`.



![img](assets/it/28.webp)



Zjištění verze Debianu a kódového označení verze:



``` bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



``` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Použijte


Ačkoli se výkon zdá být omezený (na papíře a ve srovnání s výkonem dnešních strojů), PI Zero je výkonný, zejména jako terminál.





- Nejprve můžete přejít do hlavní nabídky a inspirovat se panelem _Add/Remove software_, kde najdete řadu nástrojů pro programování a procvičování. Nezapomeňte, že to můžete udělat také z terminálu, ale vždy s právy `root`.



![img](assets/it/33.webp)





- Toto offline zařízení si můžete "adoptovat" pro ukládání různých důvěrných dokumentů, které zůstanou v případě potřeby přístupné, aniž by byly vystaveny internetu.
- Pomocí této konfigurace můžete bezpečně používat klíče GPG-12.
- Mohl bys dokonce využít tento nový „hračičku“ jako airgap podpisové zařízení, [podle rad Arman The Parman](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).



Z peněženek, které znám, je jediná, která poskytuje 32bitovou verzi, Electrum. No: Zero IP, jak jsme ji připravili v tomto návodu, by vám umožnila udržet soukromé klíče offline nastavení pro Wallet airgap, které jsme pokryli v tomto návodu:



https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Závěry


Nastavení má pravděpodobně jednu velkou slabinu: micro SD je médium, které by mohlo způsobit problémy. Je náchylná na intenzivní používání; možná s tím již máte zkušenosti z používání s telefonem. Po instalaci veškerého softwaru, který budete chtít na IP Zero airgap používat, proveďte dobrou zálohu drahocenné micro SD pomocí nástroje Raspi OS, který máte k dispozici.



![img](assets/it/34.webp)



S rostoucími potřebami a s nimi i rozpočtovými možnostmi můžete prozkoumat další řešení Raspberry nebo podobná řešení. Když už mluvíme o paměti, PI 5 například nabízí možnost sestavit disk M2 NVME, který je určitě robustnější než microSD.



Nezapomeňte si dělat poznámky a zdokumentovat každý krok instalace obslužného softwaru, který se chystáte používat v režimu offline. **Dříve nebo později vyjde aktualizovaný operační systém Raspi**, který určitě budete chtít využít. V tu chvíli budete muset všechno smazat a udělat to celé znovu (třeba s novou micro SD 😂).



Cvičení, které jsme právě provedli, si za předpokladu, že je to i váš první pokus, budete dlouho pamatovat. Ne vždy je možné věnovat se hardwarově `vloženým` operacím offline, aniž byste zanedbali pozornost airgappovanému stroji, který čas od času zapnete a zkontrolujete.



Přesto jste to zvládli, gratulujeme! A budete moci toto řešení doporučit všem, kteří potřebují snížit svůj rozpočet.