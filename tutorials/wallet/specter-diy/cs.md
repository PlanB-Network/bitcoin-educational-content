---
name: Spectre DIY
description: Průvodce nastavením Spectre DIY
---

![cover](assets/cover.webp)


## Specter-DIY


> Cypherpunkové píší kód. Víme, že někdo musí napsat software na obranu soukromí, a protože soukromí nezískáme, pokud ho nezískáme všichni, napíšeme ho my.

*Manifest Cypherpunk - Eric Hughes - 9. března 1993*


Myšlenkou projektu je sestavit hardwarový wallet z hotových komponent.

Přestože máme rozšiřující desku, která vše dává do pěkného tvaru a pomáhá vám vyhnout se pájení, budeme i nadále podporovat a udržovat kompatibilitu se standardními součástkami.


![image](assets/fr/01.webp)


Chceme také zachovat flexibilitu projektu, aby mohl s minimálními změnami fungovat na jakékoli jiné sadě komponent. Možná chcete vytvořit hardwarový wallet na jiné architektuře (RISC-V?) a jako komunikační kanál použít zvukový modem - mělo by to jít. Mělo by být snadné přidávat nebo měnit funkce Spectra a my se snažíme co nejvíce abstrahovat logické moduly.


Kódy QR jsou výchozím způsobem komunikace programu Spectre s hostitelem. Kódy QR jsou docela pohodlné a umožňují uživateli mít kontrolu nad přenosem dat - každý kód QR má velmi omezenou kapacitu a komunikace probíhá jednosměrně. Navíc je připojena vzduchem - zařízení wallet nemusíte v žádném okamžiku připojovat k počítači.


Pro ukládání tajemství podporujeme agnostický režim (wallet po vypnutí zapomene všechna tajemství), bezstarostný režim (ukládá tajemství do paměti flash mikrokontroléru aplikace) a brzy se chystá integrace secure element.


Zaměřujeme se především na nastavení více podpisů s jinými hardwarovými peněženkami, ale wallet může fungovat i jako samostatný podepisovač. Snažíme se, aby byl kompatibilní s jádrem Bitcoin, kde to jde - PSBT pro nepodepsané transakce, deskriptory wallet pro import/export multisignačních peněženek. Pro snazší komunikaci s jádrem Bitcoin pracujeme také na [Specter Desktop app](https://github.com/cryptoadvance/specter-desktop) - malém pythonovském serveru flask, který komunikuje s vaším uzlem Bitcoin Core.


Většina firmwaru je napsána v jazyce MicroPython, což usnadňuje kontrolu a změnu kódu. Pro výpočty eliptických křivek používáme knihovnu [secp256k1](https://github.com/bitcoin-core/secp256k1) z Bitcoin Core a pro grafické uživatelské rozhraní knihovnu [LittlevGL](https://lvgl.io/).


## Odmítnutí odpovědnosti


Projekt významně dospěl do té míry, že úroveň zabezpečení Spectre-DIY je nyní srovnatelná s komerčními hardwarovými peněženkami na trhu. Implementovali jsme bezpečný zavaděč, který ověřuje aktualizace firmwaru, takže si můžete být jisti, že po počátečním nastavení lze do zařízení nahrát pouze podepsaný firmware. Na rozdíl od komerčních podepisovacích zařízení však musí zavaděč nainstalovat uživatel ručně a není nastaven v továrně výrobce zařízení. Proto věnujte při počáteční instalaci firmwaru zvýšenou pozornost a ujistěte se, že jste ověřili podpisy PGP a firmware flashujete ze zabezpečeného počítače.


Pokud něco nefunguje, napište nám sem nebo se zeptejte v naší skupině [Telegram](https://t.me/+VEinVSYkW5TUl5Ai).


## Nákupní seznam pro Specter-DIY


Zde popíšeme, co si koupit, a v další části sestavy vysvětlíme, jak ji sestavit, a uvedeme několik poznámek k desce - napájecí propojky, porty USB atd.


### Deska Discovery


Hlavní součástí zařízení je vývojová deska:



- Vývojová deska STM32F469I-DISCO (např. od [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) nebo [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Kabel Mini**USB
- Standardní kabel MicroUSB pro komunikaci přes USB


Nepovinné, ale doporučené:


- [Waveshare QR code scanner](https://www.waveshare.com/barcode-scanner-module.htm) s dlouhými kolíkovými hlavičkami, jako jsou [tyto](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) nebo [tyto](https://www.amazon.com/gp/product/B015KA0RRU/), pro připojení skeneru k desce (jsou potřeba 4 kolíkové hlavičky).


V současné době pracujeme na rozšiřující desce, která obsahuje slot pro čipovou kartu, snímač QR kódů, baterii a pouzdro vytištěné na 3D tiskárně, ale neobsahuje hlavní část - desku discovery, kterou je třeba objednat zvlášť. Tímto způsobem stále nehrozí útok na dodavatelský řetězec, protože komponenty důležité pro bezpečnost jsou zakoupeny v náhodném obchodě s elektronikou.


Spectre můžete začít používat i bez dalších komponent, ale budete s ním moci komunikovat přes USB nebo vestavěný slot na SD kartu. Používání Spectra přes USB znamená, že není připojeno vzduchem, takže ztrácíte důležitou bezpečnostní vlastnost.


### Skener QR


U skeneru QR kódů máte několik možností.


**Možnost 1. Doporučujeme.** Velmi dobrý skener od Waveshare (40$)


[Waveshare scanner](https://www.waveshare.com/barcode-scanner-module.htm) - budete muset najít způsob, jak jej pěkně připevnit, možná použít nějaký Arduino Prototype shield a nějakou lepicí pásku.


Pájení není potřeba, ale pokud máte pájecí schopnosti, můžete si wallet udělat hezčí ;)


**Varianta 2.** Velmi pěkný skener od Mikroe, ale dost drahý (150 USD):


[Kliknutí na čárový kód](https://www.mikroe.com/barcode-click) + [Adaptér](https://www.mikroe.com/arduino-uno-click-shield)


**Možnost 3.** Jakýkoli jiný skener QR


V Číně najdete levné skenery. Jejich kvalita často není tak dobrá, ale můžete to risknout. Možná by to zvládla i ESPcamera. Stačí připojit napájení, UART (piny D0 a D1) a spoušť na D5.


**Možnost 4.** Bez skeneru.


Pak můžete Spectre používat pouze s USB / SD kartou.


Ledaže byste si vytvořili vlastní komunikační modul, který by místo QR kódů používal něco jiného - audiomodem, bluetooth nebo cokoli jiného. Jakmile to půjde spouštět a posílat data po sériové lince, můžete si dělat, co chcete.


### Volitelné součásti


Pokud přidáte malou powerbanku nebo baterii a nabíječku/booster, stane se váš wallet zcela samostatným ;)



## Montáž systému Specter-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### Připojení skeneru čárových kódů Waveshare


Firmware wallet nakonfiguruje skener za vás při prvním spuštění, takže není nutná žádná ruční předkonfigurace.


Zde je uveden způsob připojení skeneru k desce:


![image](assets/fr/02.webp)


Pro větší pohodlí si můžete koupit stínění Arduino Protype a vše na něj připájet a namontovat (např. [toto](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Správa napájení


Na horní straně desky se nachází propojka, která určuje, odkud se bude napájet. Polohu jumperu můžete změnit a zvolit zdroj napájení, kterým bude jeden z portů USB nebo pin VIN a připojit k němu externí baterii (měla by být 5V).


### Skříň pro kutily


Podívejte se do složky [přílohy](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures).


### Buďte kreativní!


Sestavte si vlastní Specter-DIY a pošlete nám obrázky (pošlete nám žádost o stažení nebo nás kontaktujte).


Podívejte se na [Galerii](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) se Spectry sestavenými komunitou!




## Instalace zkompilovaného kódu


U zabezpečeného zavaděče je počáteční instalace firmwaru poněkud odlišná. Aktualizace je jednodušší a nevyžaduje připojení hardwaru wallet k počítači.


![video](https://youtu.be/eF4cgK_L6T4)


### Flashing počátečního firmwaru


**Poznámka** Pokud nechcete používat binární soubory z vydání, podívejte se na [dokumentaci zavaděče](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md), kde je vysvětleno, jak jej zkompilovat a nakonfigurovat tak, aby používal vaše veřejné klíče místo našich.



- Pokud aktualizujete z verze nižší než `1.4.0` nebo nahráváte firmware poprvé, použijte soubor `initial_firmware_<version>.bin` ze stránky [releases](https://github.com/cryptoadvance/specter-diy/releases).
 - Ověřte podpis souboru `sha256.signed.txt` podle [Štěpánova klíče PGP](https://stepansnigirev.com/ss-specter-release.asc)
 - Ověření hashe souboru `initial_firmware_<version>.bin` oproti hashi uloženému v souboru `sha256.signed.txt`
- Pokud aktualizujete z prázdného zavaděče nebo se zobrazí chybová zpráva zavaděče, že firmware není platný, podívejte se do další části - Flashing signed Specter firmware.
- Ujistěte se, že je napájecí propojka desky discovery v poloze STLK
- Připojte desku discovery k počítači pomocí kabelu **miniUSB** na horní straně desky.
    - Deska by se měla zobrazit jako vyměnitelný disk s názvem `DIS_F469NI`.
- Zkopírujte soubor `initial_firmware_<version>.bin` do kořenového adresáře souborového systému `DIS_F469NI`.
- Po dokončení flashování firmwaru se deska resetuje a restartuje do zavaděče. Bootloader zkontroluje firmware a zavede hlavní firmware. Pokud se zobrazí chybové hlášení, že nebyl nalezen žádný firmware - postupujte podle pokynů pro aktualizaci a nahrajte firmware prostřednictvím SD karty.
- Nyní můžete přepnout napájecí propojku tam, kde vám vyhovuje, a napájet desku z powerbanky nebo baterie.


Flashování počátečního firmwaru pomocí kopírování a vložení souboru `.bin` se někdy nezdaří - často kvůli kabelu nebo pokud zařízení připojíte přes rozbočovač USB. V takovém případě to můžete zkusit ještě několikrát (obvykle se to podaří na 2-3 pokusy).


Pokud se to stále nedaří, můžete použít open-source nástroj [stlink](https://github.com/stlink-org/stlink/releases/latest). Nainstalujte jej a zadejte do terminálu: v případě, že je to nutné, napište následující příkaz: `st-flash write <cesta/do/initial_firmare.bin> 0x8000000`. Obvykle to funguje mnohem spolehlivěji.


### Aktualizace firmwaru



- Stáhněte si soubor `specter_upgrade_<verze>.bin` ze stránky [releases](https://github.com/cryptoadvance/specter-diy/releases).
- Zkopírujte tento binární soubor do kořenového adresáře karty SD (formát FAT, max. 32 GB)
 - Ujistěte se, že v kořenovém adresáři je pouze jeden soubor `specter_upgrade***.bin`
- Vložte kartu SD do slotu SD na desce Discovery a zapněte desku
- Bootloader provede flash firmwaru a oznámí vám, kdy bude dokončen.
- Restartujte desku - nyní se zobrazí rozhraní Specter-DIY, které vám nabídne výběr kódu PIN


Kdykoli vyjde nová verze, stačí stáhnout soubor `specter_upgrade_<verze>.bin`, vložit jej na kartu SD a aktualizovat zařízení stejně jako v předchozím kroku. Bootloader zajistí, že na desku bude možné nahrát pouze podepsaný firmware.


### Jak zjistit verzi firmwaru


Přejděte do nabídky `Nastavení zařízení` - pod názvem obrazovky se zobrazí číslo verze.


## Použití Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Zabezpečení systému Specter-DIY


### Hardware


Displej je řízen aplikačním MCU.


Integrace zabezpečených prvků zatím chybí - v současné době jsou tajemství uložena také v hlavní jednotce MCU. Modul wallet však můžete používat i bez uložení tajemství - pokaždé však musíte zadat frázi pro obnovení. Proč si dlouze pamatovat passphrase, když si můžete pamatovat celou mnemotechniku?


Zařízení používá k ukládání některých souborů externí paměť flash (QSPI), ale všechny uživatelské soubory jsou podepsány modulem wallet a při načítání kontrolovány.


Funkce skenování QR je umístěna v samostatném mikrokontroléru, takže veškeré zpracování obrazu probíhá mimo bezpečnostní MCU. V současné době jsou USB a SD karta stále spravovány hlavním MCU, takže pokud chcete snížit plochu útoku, SD kartu a USB nepoužívejte.


### Ochrana PIN (ověření uživatele)


Při prvním spuštění je na hlavní jednotce MCU vygenerováno jedinečné tajemství. Tento tajný kód umožňuje ověřit, že zařízení nebylo nahrazeno škodlivým - při zadávání kódu PIN se zobrazí seznam slov, která zůstanou stejná, dokud je tam tajný kód.


Váš kód PIN spolu s tímto jedinečným tajemstvím slouží jako dešifrovací klíč pro vaše klíče generate (pokud je máte uloženy). Pokud by tedy útočník dokázal obejít obrazovku PIN, dešifrování se stejně nezdaří.


Pokud jste firmware uzamkli (TODO: přidejte sem odkaz na návod), účinně to uzamkne i tajný kód, takže pokud útočník na desku nahraje jiný firmware, tajný kód se vymaže a vy ho budete moci poznat, až začnete zadávat PIN kód - sekvence slov bude jiná.


### Generování věty pro obnovu


Jedná se o jednu z nejdůležitějších částí wallet - k generate klíč bezpečně. Abychom to dobře provedli, používáme více zdrojů entropie:



- TRNG mikrokontroléru. Proprietární, certifikovaný a pravděpodobně dobrý, ale nevěříme mu
- Dotykový displej. Při každém dotyku obrazovky měříme polohu a okamžik, kdy k dotyku došlo (v tikách mikrokontroléru na frekvenci 180 MHz).
- Vestavěné mikrofony - zatím ne. Deska má dva mikrofony, takže vás může poslouchat hardwarový wallet a přimíchávat tato data do fondu entropie.


Všechna tato entropie se spojí a převede na vaši frázi pro obnovení. Výsledná entropie je vždy lepší než u jednotlivých zdrojů.


### Vysokoúrovňová logika - peněženky


Spectre funguje jako úložiště klíčů. Uchovává soukromé klíče HD, které mohou být zapojeny do peněženek. Peněženky jsou definovány svými deskriptory. Podporujeme také miniskriptury.


Každá jednotka wallet patří do určité sítě. To znamená, že pokud jste importovali wallet do sítě `testnet`, nebude k dispozici v síti `mainnet` nebo `regtest` - musíte se přepnout do této sítě a importovat wallet samostatně.


### Ověřování transakcí


Pro transakce, které podepíše společnost wallet, platí následující pravidla:



- pokud jsou nalezeny smíšené vstupy z různých peněženek, je uživatel varován ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- výstupy změn zobrazují název wallet, do kterého jsou odesílány
- pro použití multisignu nebo miniscriptu musíte nejprve importovat wallet přidáním deskriptoru wallet (přes QR, USB nebo SD kartu)


## Podpora deskriptorů


Všechny běžné deskriptory Bitcoin fungují. Kromě toho máme několik rozšíření:


### Více větví v deskriptorech


Abychom ušetřili místo v QR kódech, umožňujeme přidávat deskriptory s více větvemi najednou. Pokud chcete použít `wpkh(xpub/0/*)` pro přijímací adresy a `wpkh(xpub/1/*)` pro změnové adresy, můžete je spojit do jednoho deskriptoru: `wpkh(xpub/{0,1}/*)` - wallet bude první index části sady `{}` považovat za větev pro přijímací adresy a druhý za změnové adresy.


Můžete také zadat více než dvě větve a indexy větví se mohou lišit pro různé signatáře, takže tento deskriptor je velmi zvláštní, ale zcela platný:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Zde pro příjem adresy číslo 17 použije wallet skript z `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))`.


Jediným požadavkem je, aby počet indexů ve všech sadách byl stejný (ve výše uvedeném případě 3).


### Výchozí derivace


Pokud deskriptor obsahuje hlavní veřejné klíče, ale neobsahuje odvození se zástupnými znaky, bude ke všem rozšířeným klíčům v deskriptoru přidáno výchozí odvození `/{0,1}/*`. Pokud alespoň jeden z xpubů obsahuje odvození se zástupným znakem, deskriptor se nezmění.


Deskriptor `wpkh(xpub)` bude převeden na `wpkh(xpub/{0,1}/*)`.


### Miniscript


Spectre podporuje miniskript, ale nepodporuje kompilaci z politiky do miniskriptu (protože je to příliš nákladné). Provádíme určité kontroly miniskriptů, takže na nejvyšší úrovni jsou povoleny pouze skripty `B` a všechny argumenty v dílčích miniskriptech musí mít vlastnosti podle [spec](http://bitcoin.sipa.be/miniscript/).


Pomocí [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) můžete ze zásady generate vytvořit deskriptor a poté jej importovat do zásady wallet.


Například pojistku "mohu utratit hned, nebo za 100 dní může utratit moje žena" lze převést do wallet takto:


Politika: (můj klíč je 9krát pravděpodobnější)


Miniscript: (pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`


Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))``


Protože zde nemáme žádné odvození se zástupnými znaky, budou k xpubs připojeny výchozí odvození `/{0,1}/*`.



---

Licence MIT


Copyright (c) 2019 cryptoadvance


---