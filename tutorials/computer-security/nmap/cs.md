---
name: Nmap
description: Master Nmap pro mapování sítě a skenování zranitelností
---

![cover](assets/cover.webp)



*Tento návod vychází z původního obsahu Mickaela Dorignyho zveřejněného na stránkách [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). V původním textu byly provedeny změny.*



___



Vítejte v úvodním kurzu o nástroji Nmap, který je určen všem, kdo chtějí zvládnout tento výkonný nástroj pro skenování sítě. Cílem je poskytnout vám základní znalosti, které potřebujete k efektivnímu každodennímu používání Nmapu.



Nmap je všestranný nástroj, který profesionálové v oblasti IT, sítí a kybernetické bezpečnosti hojně využívají k diagnostice, zjišťování sítě a auditu zabezpečení. Tento výukový kurz je určen těm, kteří v těchto oblastech začínají a chtějí se seznámit se základy nástroje Nmap. Doporučujeme základní znalosti správy systému a sítě.



Dozvíte se základy programu Nmap, jak provádět skenování portů, identifikovat aktivní hostitele v síti, zjišťovat verze služeb a operačních systémů, provádět skenování zranitelností a mnoho dalšího. Každá část obsahuje podrobná vysvětlení a praktické příklady, které vám pomohou zvládnout používání Nmapu v různých kontextech.



Na konci tohoto výukového kurzu budete dobře rozumět nástroji Nmap a budete jej moci efektivně používat ke zlepšení zabezpečení a správy svých sítí. Příjemné čtení.



## 1 - Úvod do Nmap: Co je Nmap?



### I. Prezentace



V této první části se podíváme na nástroj Nmap pro skenování sítě. Podíváme se na klíčové Elements, které je třeba o tomto nástroji vědět, a na to, jak obecně funguje. To nám pomůže lépe pochopit zbytek výukového kurzu.



### II. Představení nástroje Nmap



Nmap, zkratka pro _Network Mapper_, je bezplatný nástroj s otevřeným zdrojovým kódem, který slouží k **zjišťování, mapování a auditu zabezpečení sítě**. Lze jej použít i pro další úlohy, jako je **inventarizace sítě, diagnostika nebo dohled**.



Dokáže zjistit, zda jsou hostitelé v cílové síti aktivní a dosažitelní, které síťové služby jsou vystaveny, které verze a technologie se používají a další užitečné analytické informace. Nmap lze použít ke skenování jedné služby na konkrétním počítači nebo v rozsáhlých částech sítě až po celý internet.



Silných stránek Nmapu je mnoho:





- Výkonný a flexibilní**: Nmap dokáže skenovat rozsáhlé sítě a používat pokročilé detekční techniky. Podporuje protokoly UDP, TCP, ICMP, IPv4 a IPv6 a může provádět detekci verzí, skenování zranitelností nebo interakce specifických protokolů. Jeho architektura je modulární, zejména díky skriptům NSE (Nmap Scripting Engine), kterým se budeme věnovat později v tomto kurzu.
- Snadné používání**: oficiální dokumentace je bohatá a kvalitní. K dispozici jsou také četné komunitní zdroje, které vám pomohou začít.
- Oblíbenost a dlouhá životnost**: Nmap je referencí ve svém oboru již od roku 1998. Aktuální verze v době této aktualizace je 7.95. Ačkoli pro specifické úlohy existují i jiné nástroje, Nmap zůstává pro mapování a analýzu sítí nepostradatelným nástrojem.



**Nmap v kině**



Nmap je jedním z mála bezpečnostních nástrojů, které si získaly určitou pověst mezi širokou veřejností. Objevil se ve filmu _Matrix Reloaded_ v příznačné scéně, kdy jej Trinity používá k nabourání se do systému:



![nmap-image](assets/fr/01.webp)



matrice: Reloaded scéna s Nmap



Objevuje se i v dalších filmových dílech.



**Zpětná vazba



Jako správce systému a poté auditor a pentester kybernetické bezpečnosti **používám Nmap téměř denně** a **pravidelně jej doporučuji** správcům systému, kteří chtějí posílit své znalosti sítí a zlepšit své diagnostické schopnosti.



### III. Provoz na vysoké úrovni



Nmap je k dispozici pro systémy Linux, Windows a macOS. Je napsán především v jazycích C, C++ a Lua (pro skripty NSE). Používá se hlavně v příkazovém řádku, i když jsou k dispozici i grafická rozhraní, například Zenmap. Důrazně však doporučujeme začít s příkazovým řádkem, abyste lépe pochopili, jak funguje.



Jednoduchý příklad:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Tento příkaz bude podrobně vysvětlen později. V tomto návodu budeme používat Nmap v Linuxu, ale jeho použití je podobné i v jiných systémech. V systému Windows se Nmap spoléhá na knihovnu **Npcap** (nahrazující dnes již zastaralou knihovnu WinPcap), která zachycuje a vkládá síťové pakety.



Nmap se používá stejně jako běžné binární soubory, například `ls` nebo `ip`. Některé pokročilé funkce mohou vyžadovat zvýšená práva, protože nástroj někdy manipuluje s pakety netradičními způsoby, aby vyvolal specifické reakce v cílových systémech (zejména pro detekci služeb nebo zranitelností).



### IV. Dopady používání Nmap



Před použitím nástroje Nmap je nutné si uvědomit jeho potenciální dopad na sítě a systémy:





- Může odeslat **tisíce nebo dokonce miliony paketů** v krátkém časovém úseku, což může zahltit některé síťové infrastruktury.
- Může generate **zdeformované nebo nestandardní** pakety, které mohou narušit některá zařízení (zejména průmyslové systémy).
- Může vyvolat chování podobné útoku**, které může vyvolat výstrahy v bezpečnostních systémech (firewally, IDS/IPS atd.).



Obecně lze říci, že **Nmap je velmi upovídaný nástroj**, protože generuje velké množství provozu, aby získal co nejvíce informací. Před použitím v citlivých nebo produkčních prostředích je proto vhodné plně porozumět jeho fungování.



### V. Závěr



V této části se seznámíte s mapou Nmap a jejími hlavními funkcemi. Viděli jsme, že se jedná o základní, výkonný a flexibilní nástroj pro mapování sítě. Probrali jsme také, jak funguje a jaká opatření je třeba při jeho používání dodržovat, abychom připravili půdu pro následující části výuky.



## 2 - Proč používat Nmap?



### I. Prezentace



V této části se podíváme na hlavní způsoby použití nástroje Nmap pro skenování sítě. Uvidíme, že se jedná o nástroj, který je široce používán v mnoha kontextech a profesích a že mít jej ve své sadě nástrojů a umět jej ovládat je rozhodně užitečná dovednost.



### II. Použití Nmap pro diagnostiku a dohled



Nmap lze použít k diagnostice sítě a obecněji k monitorování. Stejně jako lze pomocí příkazu ping zjistit, zda spolu komunikují dva hostitelé, lze pomocí Nmap rychle zjistit, zda je hostitel aktivní nebo zda je v provozu určitá služba. Díky [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap") můžeme získat přesné údaje týkající se doby odezvy hostitele, trasy, kterou pakety procházejí, odezvy konkrétní služby atd.



Následující příkaz a výsledek lze například použít k rychlému zjištění, zda je webový server na hostiteli **192.168.1.18** aktivní a správně reaguje:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Použití mapy Nmap k získání stavu webové služby ze vzdáleného serveru.*



Použití Nmapu jde tedy dále než známý "ping test" během ladění nebo diagnostických fází. Později uvidíme, že existuje několik metod, které Nmap používá k určení, která služba naslouchá na daném portu, včetně její verze.



### III. Použití Nmap pro mapování sítě



Hlavním cílem tohoto nástroje jako _Network Mapper_ je mapování sítě. Lze jej použít v rámci místní sítě nebo v rámci více sítí, podsítí a VLAN a vypsat všechny dosažitelné hostitele a služby. Nmap umožňuje tuto úlohu provádět mnohem rychleji a efektivněji než jakákoli ruční metoda.



K rychlé identifikaci aktivních hostitelů v síti **192.168.1.0/24** lze použít například následující příkaz:



```
nmap -sn 192.168.1.0/24
```



*Poznámka: volba `-sP` je zastaralá a byla nahrazena volbou `-sn`.*



![nmap-image](assets/fr/03.webp)



*Použití mapy Nmap ke zjištění dosažitelných hostitelů v síti*



Později uvidíme, že existuje několik metod, které Nmap používá k určení, zda lze hostitele považovat za "aktivního", i když a priori nevystavuje žádné služby.



### IV. Použití mapy Nmap k vyhodnocení zásad filtrování



Nmap má tu výhodu, že je věcný: jeho výsledky umožňují stanovit konkrétní zjištění, na rozdíl od jakéhokoli dokumentu o architektuře nebo zásad filtrování. Je to klíčový nástroj pro hodnocení účinnosti rozdělení informačního systému, protože umožňuje **ověřit, zda je politika filtrování skutečně uplatňována**.



V podnikové síti je podle osvědčených postupů nutné systémy segmentovat podle jejich role, kritičnosti nebo umístění. Pravidla filtrování (často implementovaná prostřednictvím firewallů) musí omezovat komunikaci mezi zónami. Tyto konfigurace jsou však často složité a náchylné k chybám.



Pro ověření, zda byly zásady dodrženy, není nic lepšího než konkrétní test. Můžete například zkontrolovat, zda citlivé služby správy (SSH, WinRM, MSSQL, MySQL atd.) nejsou přístupné z uživatelské zóny.



Použití **Nmap k testování zásad filtrování** by mělo být systematické předtím, než se takové zásady zavedou do výroby. Bohužel je tato kontrola často zanedbávána.



Podle mých zkušeností zůstává mnoho chyb konfigurace bez povšimnutí, pokud nejsou provedeny validační testy. Jednoduchá chyba v rozsahu IP adres nebo přehlédnutí pravidla může způsobit, že údajně izolovaná zóna je zranitelná.



### V. Použití Nmapu pro bezpečnostní audit a penetrační testování



Nmap má **mnoho užitečných funkcí pro hodnocení bezpečnosti**, penetrační testy (pentesty) a bohužel také pro útočníky.



Funkce zjišťování sítě jsou pro útočníka, který po počátečním napadení potřebuje pochopit topologii sítě, klíčové. Nmap však nabízí mnohem víc: integruje skriptovací engine, z nichž **mnoho je určeno pro detekci zranitelností**.



Tento příkaz lze například použít ke kontrole, zda služba FTP umožňuje anonymní připojení, aniž by bylo nutné se připojovat ručně:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Použití skriptu NSE ke kontrole anonymního ověřování FTP pomocí Nmap.*



Detekce zranitelností pomocí nástroje Nmap je jedním z prvních kroků při auditu nebo penetračním testu. Umožňuje rychle identifikovat určitá slabá místa a optimalizovat analytické úsilí.



Ale pozor: **Nástroje pro skenování zranitelnosti mají své limity**. Nmap pokrývá pouze zlomek hrozeb a nezaručuje, že je systém bezpečný, pokud nejsou zjištěny žádné problémy. Je proto nezbytné **pochopit, jak použité skripty fungují**, a nespoléhat se pouze na jejich verdikt.



### VI. Závěr



Viděli jsme, že zvládnutí Nmapu může pokrýt širokou škálu případů použití, od diagnostiky a monitorování až po mapování, vyhodnocování bezpečnostních politik a skenování zranitelností. V příští části se pustíme do detailů a nainstalujeme Nmap.




## 3 - Instalace a konfigurace aplikace Nmap



### I. Prezentace



V této části se dozvíte, jak nainstalovat nástroj Nmap pro skenování sítě v operačních systémech Linux a Windows. Na konci této části budeme mít vše, co potřebujeme, abychom mohli začít používat Nmap pro budoucí moduly. Nakonec se dozvíme, jaká oprávnění může při svém použití vyžadovat a proč.



### II. Instalace Nmapu pod Linuxem



Nmap byl původně navržen pro operační systémy GNU/Linux. Díky jeho dlouhé životnosti a popularitě jej proto najdete ve všech oficiálních repozitářích hlavních unixových distribucí. V tomto návodu budu používat operační systém založený na Debianu [Kali Linux](https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Ale úplně stejně jej můžete používat i z klasického Debianu, CentOS, Red Hatu nebo čehokoli jiného!



V Debianu můžete zkontrolovat, zda je Nmap přítomen v aktuálních repozitářích, pomocí následujícího příkazu:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



Odpověď zde jasně naznačuje, že balíček "nmap" v repozitářích (zde v repozitářích Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")) existuje. Od této chvíle můžete Nmap instalovat pomocí obvyklých instalačních příkazů, nic odzbrojujícího zatím 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



Abychom zkontrolovali, zda je Nmap správně nainstalován, zobrazíme jeho verzi:



```
nmap --version
```



Zde je očekávaný výsledek:



![nmap-image](assets/fr/05.webp)



výsledek zobrazení aktuální verze Nmap._



Všimněte si, že je v tomto zobrazení přítomna knihovna "libpcap" (_Packet Capture Library_) a její verze. Knihovnu "libpcap" používá také program Wireshark a Nmap ji používá k vytváření a manipulaci s pakety a k poslechu síťového provozu.



### III Instalace aplikace Nmap v systému Windows



Chcete-li instalovat do operačního systému Windows, začněte stažením binárního souboru z oficiálních stránek (a žádných jiných!):





- Stránka Nmap ke stažení na oficiálních webových stránkách: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




Poté je třeba stáhnout binární soubor s názvem `nmap-<VERSION>-setup.exe`:



![nmap-image](assets/fr/06.webp)



instalační binární stránka nmap pro Windows ke stažení



Jakmile budete mít tuto binárku v systému, jednoduše ji spusťte a nainstalujte Nmap. Instalace je jednoduchá a všechny možnosti můžete ponechat jako výchozí.



Můj reflex je zrušit zaškrtnutí políčka "zenmap (GUI Frontend)". Jedná se o grafický Interface pro Nmap, který nepoužívám a v tomto tutoriálu se jím nebudu zabývat, ale neváhejte jej vyzkoušet, jakmile zvládnete nástroj Nmap pro příkazový řádek!



![nmap-image](assets/fr/07.webp)



volitelné zrušení volby Zenmap při instalaci Nmap v systému Windows



Na konci instalace programu Nmap je navržena druhá instalace: instalace knihovny "Npcap":



![nmap-image](assets/fr/08.webp)



instalace knihovny "Npcap" při instalaci Nmap pod Windows



Jedná se o knihovnu, na kterou se Nmap spoléhá při správě síťové komunikace, tj. při vytváření, odesílání a přijímání síťových paketů. S touto knihovnou jste se již pravděpodobně setkali, pokud používáte Wireshark v systému Windows, protože ji také používá a vyžaduje instalaci.



Stejně jako v Linuxu můžete ověřit, zda je Nmap nainstalován, otevřením příkazového řádku nebo terminálu [Powershell] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") a zadáním následujícího příkazu:



```
nmap --version
```



Zde je očekávaný výsledek:



![nmap-image](assets/fr/09.webp)



výsledek zobrazení aktuální verze Nmap._



Nmap je nyní nainstalován v systému Windows. Podle tohoto návodu jej můžete používat stejným způsobem jako v Linuxu.



### IV. Místní oprávnění potřebná k použití Nmap



Ale mimochodem, **je při použití Nmapu nutné mít v systému zvýšená místní práva?** Odpověď zní: **Záleží na tom**.



Ve své základní podobě, tj. aniž byste zašli příliš daleko v používání jeho možností, Nmap nutně nevyžaduje privilegovaná práva. Brzy však zjistíte, že je lepší používat Nmap v privilegovaném kontextu ("root" pod Linuxem, "administrator" nebo ekvivalent pod Windows), abyste mohli využít jeho plný potenciál, i když riskujete, že dostanete chybové hlášení, jako je toto:



![nmap-image](assets/fr/10.webp)



chybová zpráva pod Linuxem, když možnosti Nmap vyžadují práva roota._



Ať už v systému Linux nebo Windows, existuje mnoho případů, kdy vás Nmap požádá o privilegovaný přístup. Hlavní důvody jsou následující (neúplný seznam):





- Konstrukce "surových" síťových paketů**: Nmap umí širokou škálu metod skenování, včetně pokročilé manipulace s pakety a jejich konstrukce. To je například případ, kdy chceme provádět skenování TCP SYN, které nerespektuje klasický _Three-way handshake_ výměny TCP. K tomu Nmap potřebuje použít jiné funkce než ty, které jsou nativní pro operační systémy, které jediné umí respektovat správné postupy v síťové komunikaci (volá knihovny "Npcap" a "libcap", které jsme viděli výše). Právě proto, že Nmap nedělá věci "standardním" způsobem, je schopen odvodit určité informace o operačních systémech, službách a některých zranitelnostech.





- Naslouchat síťovému provozu**: některé možnosti Nmapu vyžadují, aby naslouchal síti za účelem získání určitých informací. Tato činnost je v operačních systémech považována za citlivou, protože umožňuje odposlouchávat i komunikaci jiných aplikací v systému. Stejně jako Wireshark potřebuje Nmap k této činnosti specifická oprávnění, která lze snáze získat, pokud se nacházíte přímo v privilegované relaci.





- Naslouchání na privilegovaných portech**: v operačních systémech jsou porty od 0 do 1024 (TCP i UDP) považovány za privilegované, tj. jsou nějakým způsobem vyhrazeny pro velmi specifické použití, a proto jsou chráněny. Ačkoli je to dnes již poněkud zastaralý důvod, pro naslouchání na těchto portech je stále nutné mít určitá oprávnění, což Nmap může mít v závislosti na způsobu použití.





- Odesílání paketů UDP:** Podobně naslouchání síťové aplikaci na portech UDP (bezstavový protokol) vyžaduje v operačních systémech privilegovaná práva. Pokud tedy chcete provést skenování UDP, při kterém bude muset Nmap naslouchat na odpověď, aby mohl analyzovat odpovědi na své skenování, bude vyžadována relace s privilegiem.




Přesněji řečeno, alespoň v Linuxu je možné spustit Nmap se všemi jeho funkcemi a možnostmi, aniž byste byli root. Toho se dosáhne přidělením správných _schopností_ binárnímu souboru. To však vyžaduje pokročilou manipulaci a nemusí to být tak praktické jako přímé spuštění Nmapu s právy. Tento přístup je také méně obvyklý a při nesprávné konfiguraci může způsobit bezpečnostní problémy.



To je však trochu odklon od našeho výukového programu Nmap, takže se od toho prozatím oprostíme.



Ve zbytku tohoto návodu předpokládejte, že Nmap je vždy spuštěn jako "root" (z shellu jako "root" nebo pomocí příkazu "sudo") nebo v terminálu správce pod Windows, i když to není uvedeno. V opačném případě se můžete setkat s jemnými, ale znatelnými rozdíly oproti tomuto návodu.



### V. Závěr



A je to! Nmap je nyní nainstalován v našem operačním systému a připraven k použití, nevyžaduje žádnou další konfiguraci. Tímto oddílem končíme úvod a představení systému Nmap. Doufám, že se vám při něm zalíbilo a že máte chuť začít s praxí.



Nyní už máme lepší představu o tom, co je to mapovací nástroj Nmap, jaké jsou jeho nejčastější možnosti použití a jaká jsou jeho omezení. Pojďme dál!




## 4 - Skenování portů TCP a UDP pomocí aplikace Nmap



### I. Prezentace



V této části se naučíme provádět první skenování portů pomocí nástroje Nmap pro skenování sítě. Uvidíme, jak jej použít k sestavení seznamu síťových služeb vystavených na hostiteli, ať už pomocí protokolů TCP nebo UDP.



Od této chvíle nezapomeňte skenovat pouze hostitele v kontrolovaném prostředí, ke kterým máte výslovné oprávnění.





- Pro připomenutí: [Trestní zákoník: Kapitola III: Útoky na systémy automatizovaného zpracování dat](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Pokud nemáte po ruce**, doporučuji následující bezplatné řešení, které je přesně to pravé!





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")**: Hack The Box je tréninková platforma pro hackery, která vám neustále poskytuje zranitelné systémy, na které můžete útočit, jak uznáte za vhodné. K dispozici je několik stovek systémů, ale celoročně je zdarma nabízen obnovený fond 20 strojů s přístupem přes OpenVPN VPN.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")**: Tato platforma nabízí ke stažení množství záměrně zranitelných systémů, které lze použít prostřednictvím VirtualBoxu (rovněž bezplatné řešení) nebo jiným způsobem. Po stažení není třeba používat VPN - vše je lokální.




Můžete si také **vytvořit virtuální počítač** ve svém oblíbeném operačním systému a nainstalovat do něj různé služby jako testovací cíle. Výhodou zde bude, že budete moci také vidět, co se děje na straně serveru během skenování, zejména pomocí Wiresharku, a budete mít k dispozici místní firewall, když budeme provádět pokročilejší testy.



Buďme praktičtí!



### II. Skenování portů TCP hostitele pomocí nástroje Nmap



#### A. První skenování portů TCP pomocí Nmap



Nyní provedeme první skenování pomocí nástroje Nmap. Náš cíl je jednoduchý: chceme zjistit, jaké služby jsou vystaveny webovým serverem, který jsme právě nasadili, abychom zjistili, zda se neobjevilo něco neočekávaného, například služba správy, která by neměla být přístupná, nebo vystavení portu aplikace, o které jsme si mysleli, že byla zrušena.



V mém příkladu má skenovaný hostitel adresu IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



Zde je možný výsledek. Vidíme klasický návrat Nmapu se spoustou informací:



![nmap-image](assets/fr/11.webp)



výsledky jednoduchého skenování TCP provedeného pomocí nástroje Nmap._



Při rychlém pohledu na tento výsledek zjistíme, že porty TCP/22 a TCP/80 jsou na tomto hostiteli přístupné.



Ve výchozím nastavení, a pokud mu to neřeknete, bude Nmap skenovat pouze porty TCP.



#### B. Porozumění výsledkům jednoduchého skenování Nmap



Pojďme však ještě o krok dál, abychom tomuto výstupu porozuměli: každý řádek je důležitý jednak proto, abychom věděli, co bylo právě provedeno, a jednak proto, abychom správně interpretovali samotné výsledky skenování.



První řádek je v podstatě připomínkou verze a data skenování (užitečné pro protokolování a archivaci!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



Na druhém řádku je zobrazen začátek výsledků skenování pro hostitele "debian.home (192.168.1.19)". Tato informace bude užitečná, až začneme skenovat několik hostitelů najednou:



```
Nmap scan report for debian.home (192.168.1.19)
```



Třetí řádek nám říká, že daný hostitel je "Up", tj. aktivní:



```
Host is up (0.00022s latency).
```



Nakonec nás Nmap informuje, že 998 portů TCP identifikovaných jako uzavřené není zobrazeno v:



```
Not shown: 998 closed tcp ports (conn-refused)
```



To nám ušetří téměř 1 000 řádků výstupu, který vypadá jako:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Děkujeme mu, že nás toho ušetřil!



Proč 998 "uzavřených" portů? Když sečtete 2 otevřené porty, je to 1000 portů, a to je počet portů, které bude Nmap skenovat ve výchozí konfiguraci, nikoli 65535 existujících portů TCP! Později uvidíme, že je to zcela a snadno přizpůsobitelné. Pokud však má cílový hostitel službu naslouchající na poněkud exotickém portu, toto "výchozí" skenování ji neodhalí.



Po těchto informacích najdeme to nejzajímavější: tabulku uspořádanou podle tří sloupců "PORT - STATE - SERVICE":





- První sloupec "PORT" jednoduše označuje cílový port/protokol a je důležité se podívat, zda se jedná o port TCP (`<port>/tcp`) nebo UDP (`<port>/udp`).





- Sloupec "STATE" označuje stav síťové služby zjištěný na tomto portu a určený mapou Nmap na základě získané odpovědi. Může to být "open", "closed", "filtered" nebo "unknown". Později uvidíme, jak Nmap tyto různé stavy rozlišuje.





- Sloupec "SERVICE" označuje službu vystavenou na daném portu. Všimněte si však, že jsme zde nepoužili aktivní možnosti zjišťování služeb. Nmap se spoléhá na místní odkaz mezi portem/protokolem a údajně přiřazenou službou: soubor "/etc/services"




Pokud se podíváte do souboru /etc/services v systému Linux, najdete odkaz "port/protokol - služba" podobný tomu, který zobrazuje Nmap:



![nmap-image](assets/fr/12.webp)



vyextrahuje obsah souboru "/etc/services" pod Linuxem._



Je důležité si uvědomit, že Nmap prozatím neprovádí žádné aktivní zjišťování služeb. V takovém případě by například nebyl schopen identifikovat službu SSH za portem TCP/80. Proto je důležité vědět, jak používat správné možnosti - to se brzy stane!



Znalost interpretace výstupů nástroje Nmap je důležitou součástí zvládnutí tohoto nástroje. Dobrou zprávou je, že tento výstup bude z velké části stejný, ať už použijete jakékoli možnosti.



#### C. Pod kapotou: analýza sítě pomocí programu Wireshark



Pokud se pozorně podíváte na to, co se děje v síti Interface hostitele, který skenuje server, nebo v síti samotného serveru, bude vám činnost Nmapu mnohem jasnější. Přesně to zde uděláme.



To, co vám zde mohu ukázat, je jen část toho, co je viditelné v programu Wireshark. Pokud chcete jít ještě dál, neváhejte sami provést zachycení sítě během skenování a pak procházet to, co bylo zachyceno.



V tomto testu jsou můj skenovací hostitel (192.168.1.18) a cílový hostitel (192.168.1.19) ve stejné místní síti.



Nmap nejprve zjistí, zda je cílový hostitel v místní síti aktivní, a to odesláním požadavku ARP. Pokud obdrží odpověď, ví, že je hostitel aktivní, a zahájí skenování sítě:



![nmap-image](assets/fr/13.webp)



_ARP požadavek vydaný mapou Nmap ke zjištění, zda se v místní síti nachází cílový hostitel._



Pokud se skenovaný hostitel nachází ve vzdálené síti, zahájí Nmap odesláním požadavku ping a pokusí se dosáhnout některých nejčastěji exponovaných portů (TCP/80, TCP/443):



![nmap-image](assets/fr/14.webp)



požadavek ping vydaný mapou Nmap ke zjištění, zda je cílový hostitel dosažitelný ve vzdálené síti



Pokud na některý z těchto testů získá odpověď, považuje cíl za aktivní.



Jakmile Nmap zjistí, že je cíl aktivní, pokusí se přeložit jeho název domény pomocí serveru DNS nakonfigurovaného na síťové kartě:



![nmap-image](assets/fr/15.webp)



rozlišení dNS na cíli skenování Nmap



Nyní, když Nmap identifikoval svůj cíl a ví, že je aktivní, zahájí skenování portů TCP:



![nmap-image](assets/fr/16.webp)



tCP Přenos paketu SYN a příjem RST/ACK během skenování Nmap



Za tímto účelem bude na každém portu TCP ve svém výchozím rozsahu **odesílat pakety TCP SYN a čekat na odpověď**. Na výše uvedeném snímku obrazovky přijímá od skenovaného serveru pakety TCP RST/ACK, což znamená "jděte dál, tady není nic k vidění" - jinými slovy, tyto porty jsou zavřené. Jak jsme viděli ve výsledku, bude tomu tak u většiny skenovaných portů. Až na dvě výjimky:



![nmap-image](assets/fr/17.webp)



odpověď na paket TCP SYN odeslaný na port 22, aktivní v cíli skenování



Na obrázku výše vidíme paket TCP SYN/ACK odeslaný cílovým hostitelem**. Port je aktivní a vystavuje službu. Nmap potvrdí přijetí odpovědi a poté ukončí spojení (TCP RST/ACK). **Takto zjistil, že port TCP/22 je aktivní**.



Viděli jsme, že Nmap při skenování sítě TCP respektuje "třícestný handshake". Z výkonnostních důvodů je možné jej požádat, aby na návrat serveru neodpovídal, čímž se při skenování velké sítě ušetří několik tisíc paketů. Těmto možnostem a optimalizacím se však budeme věnovat později v tomto tutoriálu.



Nyní máme lepší představu o tom, jak provádět skenování TCP a co se při něm vlastně děje. Viděli jsme také, že ve výchozím nastavení provádí Nmap skenování portů TCP na omezeném počtu portů.



### III. Skenování portů UDP pomocí Nmap



#### A. První skenování portů UDP pomocí Nmap



Nyní se podíváme, jak skenovat porty UDP hostitele. Jak jsme viděli, ve výchozím nastavení Nmap vždy skenuje porty TCP. To může znamenat, že nám unikne mnoho informací, pokud o nich nevíme.



Připomínám, že pro účely tohoto testu jsou můj skenovací hostitel (192.168.1.18) a cílový hostitel (192.168.1.19) ve stejné místní síti.



```
nmap -sU 192.168.1.19
```



Zde má vrácená zpráva stejný formát jako při skenování TCP, ale zobrazené aktivní služby jsou ve formátu `<port>/UDP`, jak je požadováno!



![nmap-image](assets/fr/18.webp)



výsledek jednoduchého skenování UDP pomocí programu Nmap._



Volba "-sU" slouží k tomu, abyste Nmapu sdělili, že chcete pracovat s protokolem UDP, a nikoli s protokolem TCP, jak je výchozí.



Mimochodem, pravděpodobně jste si všimli, že Nmap vyžaduje pro skenování UDP práva "root", jak bylo zmíněno dříve v tutoriálu.



poznámka: Od nejnovějších verzí programu Nmap se pro zajištění spolehlivých výsledků vždy doporučuje provádět skenování UDP s právy správce, protože některé funkce vyžadují neošetřený přístup k síťovým soketům._



Skenování UDP může trvat velmi dlouho (v mém případě 1100 sekund na skenování 1000 portů), protože v UDP neexistuje "Three Way Handshake", což znamená, že Nmap čeká na návrat každého odeslaného paketu UDP a určí port jako "uzavřený" pouze tehdy, pokud po určité době (timeout) nedojde k návratu. Tato odpověď skenovaných hostitelů není systematická a často je omezena počtem odpovědí za sekundu, aby se zabránilo určitým útokům typu amplification. To je rozdíl od protokolu TCP, kde dochází k okamžité odpovědi ze strany skenovaného hostitele, ať už je port otevřený, nebo zavřený. Později si ukážeme, jak tuto funkci optimalizovat.



Druhým problémem protokolu UDP je **to, že služby ne vždy odpovídají na příchozí pakety**, jednoduše proto, že to není vždy nutné a je to princip protokolu UDP. V takovém případě, kdy není přijat žádný ICMP "port unreachable", je služba označena Nmapem jako "open|filtered", jak ukazuje obrázek výše.



#### B. Pod kapotou: analýza sítě pomocí programu Wireshark



Stejně jako v případě skenování TCP se podívejme blíže na to, co se děje na úrovni sítě během skenování UDP pomocí analýzy Wireshark. Chování programu Nmap při určování, zda je hostitel aktivní, je stejné.



Jediný skutečný rozdíl při skenování protokolu UDP spočívá v tom, že Nmap nebude čekat na "Three Way Handshake", protože tento mechanismus v protokolu UDP (bezstavový protokol) neexistuje:



![nmap-image](assets/fr/19.webp)



přenos paketů uDP a příjem ICMP (nedostupný port) během skenování Nmap



Na výše uvedeném obrázku vidíme, že Nmap odešle velké množství paketů UDP a na většinu z nich obdrží jako odpověď paket ICMP "Destination unreachable (Port unreachable)". To je normální, protože se jedná o vhodnou odpověď definovanou v [RFC 1122](https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122"), když je port UDP nedostupný:



![nmap-image](assets/fr/20.webp)



výtah z RFC 1122._



Podívejme se blíže na tento snímek Wireshark, který ukazuje **tři možné scénáře** v protokolu UDP:



![nmap-image](assets/fr/21.webp)



zachycení sítě během skenování UDP na různých portech pomocí Nmap._



Jedná se o tyto tři případy:





- První Exchange se skládá z paketů č. 3, 4 a 8, 9. Nmap odesílá pakety UDP na klasickém portu SNMP, a proto **sestavuje pakety odpovídající protokolu předem**. Poté získá odpověď od serveru (pakety č. 8 a 9). Výsledek: Nmap obdržel odpověď, služba je "otevřená".





- Druhý paket Exchange se skládá z paketů 6 a 7. Nmap odešle "prázdný" paket UDP (bez struktury protokolu) na port UDP/165 a jako odpověď obdrží paket ICMP: "Destination unreachable (Port unreachable)". Výsledek: Nmap obdržel (negativní) odpověď, hostitel je v provozu, ale služba, kterou se snažil dosáhnout, na tomto portu nefunguje a bude označena jako "uzavřená".





- Poslední Exchange tvoří paket č. 12: Nmap odešle "prázdný" UDP paket na port UDP/1235. Nedojde k žádné odpovědi, dokonce ani k výslovnému odmítnutí ze strany skenovaného hostitele. Výsledek: Nmap označí port jako "open|filtered", protože není schopen určit, zda je to způsobeno přítomností firewallu nakonfigurovaného tak, aby neodpovídal, nebo aktivní službou UDP, která stejně nevrací žádnou odpověď (v UDP není povinná).




Zde je výsledek zobrazený programem Nmap po těchto třech případech:



![nmap-image](assets/fr/22.webp)



možné výsledky skenování UDP provedeného pomocí Nmap._



Nyní máme lepší představu o tom, jak provádět skenování UDP a co se při něm vlastně děje. Zatím jsme Nmap používali jen velmi jednoduše, aniž bychom se rozhodovali, které porty skenovat, ale to se brzy změní!



### IV. Jemné doladění skenování portů pomocí nástroje Nmap



#### A. Připomenutí výchozího chování Nmapu



Jak jsme viděli, pokud nezadáte žádné možnosti, Nmap sám vybere počet a porty, které bude skenovat. Jedná se o "výchozí" konfiguraci, kterou Nmap používá, pokud mu přesně neřeknete, co má dělat. Tyto výchozí volby jsou navrženy tak, aby poskytly představu o hlavních exponovaných portech, přičemž tyto porty jsou vybírány spíše podle četnosti exponování (nejběžnější nebo nejčastější porty) než podle číselného pořadí (port 1, 2, 3 atd.), a také proto, aby se zabránilo zahájení skenování 65535 možných portů, pokud nezadáte příslušné volby, což by bylo pro "výchozí" případ použití příliš dlouhé a heslovité.



**Jak se tyto porty vybírají?



1000 portů skenovaných ve výchozím režimu je vybráno podle četnosti jejich výskytu. Tyto statistiky udržuje Nmap a aktualizuje je stejným způsobem jako samotnou binární knihovnu a její skripty (moduly). Tyto statistiky si můžete sami prohlédnout v souboru "/usr/shares/nmap/nmap-services":



![nmap-image](assets/fr/23.webp)



extrahované ze souboru "/usr/shares/nmap/nmap-services"._



Ve třetím sloupci vidíme něco, co vypadá jako pravděpodobnost (mezi 0 a 1) nebo procentuální rozdělení. Jedná se o četnost výskytu jednotlivých dvojic port/protokol. Vidíme, že nejznámější porty (v tomto výpisu FTP, SSH, TELNET a SMTP) mají mnohem vyšší hodnotu než ostatní.



#### B. Přesné zadání cílových portů pro skenování Nmapem



V reálném světě však můžeme potřebovat skenovat pouze určitý port, několik portů nebo určitý rozsah portů. Aplikace Nmap to umožňuje snadno a jednotně pro skenování UDP i TCP.



**Skenování konkrétního portu pomocí Nmap**



Pokud si přejeme skenovat pouze jeden port, a ne 1000, můžeme tento port zadat pomocí volby "-p" nebo "--port":



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Výsledkem je, že skenování bude přirozeně mnohem rychlejší a Nmap bude vysílat pouze pakety potřebné ke zjištění, zda je hostitel aktivní a zda je zadaný port dosažitelný. To šetří čas, pokud chcete pouze provést rychlý test, zda je webová služba na vašem prezentačním webu stále funkční.



**Skenování více portů pomocí Nmap**



Stejným způsobem můžeme Nmapu zadat několik portů, přičemž použijeme stejnou volbu a zadané porty spojíme čárkou:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Bez ohledu na pořadí bude Nmap kontrolovat všechny tyto porty a pouze ty, které jsou na cílovém hostiteli. Ve výstupu Nmapu si všimněte, že nám **výslovně sdělí všechny porty a jejich stav**, i když jsou "zavřené". Na rozdíl od výchozího chování, kde by tento kompletní výstup zabíral příliš mnoho místa:



![nmap-image](assets/fr/24.webp)



*Výsledek skenování TCP pomocí Nmap na uvedených portech.*



**Skenování řady portů



Pokud je počet portů, které chcete skenovat, příliš velký, můžete je zadat podle rozsahu, například:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Samozřejmě je můžete kombinovat podle vlastního uvážení, například:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**Skenování portů TCP a UDP



Můžete také provádět skenování UDP a TCP na vybraných portech současně:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



V posledním příkladu si všimněte přítomnosti písmen "U:", která označují port UDP, a písmen "T:", která označují port TCP. Zde je možný výstup tohoto typu skenování:



![nmap-image](assets/fr/25.webp)



*Výsledek skenování portů TCP a UDP pomocí nástroje Nmap.*



To je zajímavý způsob, jak si přizpůsobit skenování!



**Skenování všech portů



Nakonec je možné zadat Nmapu mnohem větší nebo menší rozsahy. Viděli jsme, že výchozí seznam vybraný mapou Nmap obsahuje 1000 portů. Můžeme si také vyžádat 100 nejčastějších portů nebo 200 nejčastějších portů pomocí volby "--top-ports":



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Nakonec jej můžeme požádat, aby prohledal všechny možné porty (všech 65535) pomocí zápisu "-p-":



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



Druhý způsob bude trvat déle, zejména v případě UDP, ale budete mít jistotu, že nevynecháte žádné otevřené porty.



*Poznámka: Možnost "-p-" je doporučená metoda pro skenování všech portů TCP. Pro skenování UDP je vhodné omezit počet portů z výkonnostních důvodů, protože kompletní skenování všech portů UDP může trvat velmi dlouho.*



Později v tomto kurzu se podíváme, jak optimalizovat rychlost skenování Nmapu podle našich potřeb, což bude užitečné zejména pro skenování všech portů TCP a UDP.



### V. Závěr



V této části jsme si konečně vyzkoušeli praktické postupy, takže nyní víme, **jak používat Nmap k základnímu skenování portů TCP a UDP hostitele**. Podrobně jsme se také podívali na to, co se děje na úrovni sítě a **jak Nmap určuje, zda je port TCP nebo UDP aktivní, či nikoli**. Nakonec víme, jak jemně vybrat porty, které chceme skenovat, a **co vlastně dělají výchozí možnosti Nmapu**. V následujícím textu tyto znalosti zopakujeme a použijeme je na skenování celé sítě, včetně globálního mapování a zjišťování sítě.




## 5 - Mapování a zjišťování sítě pomocí nástroje Nmap



### I. Prezentace



V této části se naučíme používat nástroj Nmap pro skenování sítě k mapování sítě. Uvidíme, jak efektivní může být při tomto úkolu, a to prostřednictvím jeho různých možností. Nakonec se podíváme na různé způsoby zadávání cílů našeho skenování do nástroje Nmap.



Využijeme zejména to, co jsme se naučili v předchozí části o tom, jak Nmap určuje, zda je hostitel aktivní a dosažitelný.



Jak bylo uvedeno v úvodu k nástroji Nmap, jedná se o mapovač sítě. Jako takový je ideálním nástrojem pro sestavení seznamu přístupných hostitelů v síti, ať už místní nebo vzdálené.



**Návrat autora:**



Jako auditor kybernetické bezpečnosti a pentester používám Nmap systematicky při provádění interních penetračních testů, abych zjistil, kde se nacházím, kdo jsou moji sousedé v místní síti a jaké další sítě jsou přístupné, stejně jako systémy, které se v nich nacházejí. Můj cíl je jednoduchý: zmapovat síť, určit velikost informačního systému a zejména načrtnout jeho útočnou plochu.



Mapování sítě může být užitečné také v kontextu diagnostiky sítě, dohledu, mapování aktiv (jste si opravdu jisti, že váš IS je tvořen pouze tím, co je v adresáři Active Directory nebo v inventáři GLPI/OCS? Lze jej také využít k odhalení přítomnosti stínového IT ve vašem informačním systému.



### II. Použití mapy Nmap ke skenování rozsahu sítě



#### A. Objevení sítě pomocí skenování Nmap



Nyní bychom rádi postoupili o stupeň výš a analyzovali celou naši místní síť. Nic nemůže být jednodušší: stačí použít příkazy, které jsme viděli v předchozí části, ale místo prosté IP adresy Address zadat CIDR.



CIDR (**Classless Inter Domain Routing**) je "klasický" zápis pro určení rozsahu sítě a jejího rozsahu (pomocí masky). Například "192.168.0.0/24" je "překlad" zápisu desítkové masky "255.255.255.0".



Chcete-li použít Nmap se zadáním CIDR, můžete jej použít takto:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



Stejně jako u portů v předchozí části je možné zadat více hostitelů, více sítí nebo rozsah:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



Zde je příklad výsledků, které můžeme získat při spuštění skenování v síti:



![nmap-image](assets/fr/26.webp)



výsledky skenování Nmap pro mapování několika sítí



Konkrétně vidíme několik aktivních hostitelů a každá část hostitele začíná tímto řádkem:



```
Nmap scan report for <name> (<IP>)
```



To nám umožňuje jasně zjistit, ke kterému hostiteli se vztahují následující výsledky. Důležitý je také úplně poslední řádek:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Víme, že v proskenovaných sítích objevil Nmap 5 aktivních hostitelů.



#### B. Pod kapotou: analýza sítě pomocí programu Wireshark



Nyní se blíže podíváme na to, co se děje na úrovni sítě během zjišťování sítě pomocí nástroje Nmap.



Jak jsme viděli v předchozí části, ve výchozím nastavení používá Nmap ke zjištění přítomnosti hostitelů v místní síti protokol ARP:



![nmap-image](assets/fr/27.webp)



aRP pakety zachycené při skenování místní sítě pomocí Nmap a jeho výchozích možností



Je tak schopen odhalit prakticky všechny hostitele v místní síti, protože odpověď na požadavek ARP obvykle poskytují všichni hostitelé aktivní v síti a nevypadá nijak podezřele.



Pro vzdálené sítě používá Nmap kombinaci technik:



![nmap-image](assets/fr/28.webp)



pakety iCMP a TCP zachycené při skenování vzdálené sítě pomocí mapy Nmap a jejích výchozích možností



Přesněji řečeno, Nmap používá paket ICMP echo (klasický případ pingu) a paket ICMP Timestamp, který se obvykle používá k výpočtu doby přenosu paketů. Doufá, že získá odpověď od hostitelů ve vzdálených sítích.



Je v tom ale něco víc. Na výše uvedeném snímku Wiresharku můžete vidět, že pakety **TCP SYN** jsou systematicky odesílány na porty TCP/443 všech potenciálních hostitelů v sítích, které mají být skenovány, stejně jako pakety **TCP ACK** na portu TCP/80.



**Proč posílat pakety TCP na porty v rámci zjišťování sítě?



Odesláním paketu SYN na daný port může Nmap **určit, zda služba naslouchá na daném portu**. Pokud hostitel odpoví na paket SYN paketem SYN/ACK, znamená to, že je aktivní a že služba na daném portu naslouchá. Nmap proto zkusí štěstí u této služby, **i když na ping neodpoví**.



Odesláním paketu ACK na daný port může Nmap **určit, zda je na daném hostiteli přítomna brána firewall**. Pokud hostitel odpoví na paket ACK paketem RST (Reset), znamená to, že na daném hostiteli je pravděpodobně přítomna brána firewall, která blokuje nevyžádaný provoz. Hostitel tak prozradí svou přítomnost v síti, i když neodpověděl na jiné požadavky.



Je však důležité poznamenat, že detekce brány firewall pomocí této techniky nemusí být ve všech případech zcela spolehlivá. Někteří hostitelé mohou odpovídat generate RST z jiných důvodů, než je přítomnost brány firewall, například kvůli specifické konfiguraci služby nebo operačního systému. Kromě toho mohou být moderní brány firewall nakonfigurovány tak, aby na pokusy o zjišťování tohoto typu neodpovídaly.



Nyní jsme ušli dlouhou cestu a můžeme provádět základní zjišťování sítě. Nyní se podíváme na několik dalších možností, které nám umožní větší kontrolu nad chováním Nmapu.



### III. Zjištění sítě bez skenování portů pomocí Nmapu



Jak jste si možná všimli, ve výchozím nastavení Nmap **provádí skenování portů po objevení aktivního hostitele**, což při skenování přidává obrovské množství paketů a čekání na odpověď. Pokud máte v síti 5 hostitelů, Nmap se pokusí zkontrolovat stav přibližně 5 000 portů, což bude trvat déle.



Je však možné použít možnosti Nmapu k **pouhému zjišťování aktivních hostitelů** v síti, aniž by byly zjišťovány jejich služby.



Pokud chceme pouze zjistit, kteří hostitelé jsou dosažitelní, bez jakýchkoli informací o službách a portech, které vystavují, můžeme použít volbu "-sn" a provést **pouze skenování pomocí ICMP Echo (ping) a ARP požadavků**. Jinými slovy, skenování portů zcela zakážeme:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Zde je výsledek zjišťování sítě Nmap bez skenování portů:



![nmap-image](assets/fr/29.webp)



Výsledek zjišťování sítě bez skenování portů pomocí Nmap.



Již jsme se zmínili o možných omezeních při použití samotného protokolu ICMP pro zjišťování hostitelů (pro vzdálené sítě). Proto Nmap používá také několik triků, které mohou prozradit přítomnost firewallu nebo konkrétní služby na hostitelích. Pomocí voleb můžeme tyto triky znovu použít a dokonce je rozšířit, aniž bychom museli znovu začínat s kompletním skenováním portů každého objeveného hostitele.



K tomu použijeme volby "-PS" (TCP SYN) a "-PA" (TCP ACK), které nám umožní zadat porty, k nimž se chceme připojit v rámci zjišťování hostitele, a také volbu "-PP":



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Tato kontrola již zajišťuje, že zjišťování hostitelů je o něco úplnější než při použití výchozích možností.



Začínáme dostávat poměrně rozsáhlé příkazy, které využívají více možností. Je to proto, že víme, jak Nmap funguje, a známe omezení jeho "výchozích" možností, kvůli kterým můžeme někdy ztrácet čas nebo vynechat důležité Elements. A to je právě ten důvod, proč věnovat čas jeho zvládnutí!



Podrobné informace o možnostech naší poslední objednávky:





- "`-sn`: zakáže skenování portů pro každého aktivního hostitele objeveného mapou Nmap.





- "`-PP`: povoluje ICMP echo (ping scan) pro zjišťování hostitele.





- "`-PS <PORT>`": odešle paket TCP SYN na uvedený port (porty), aby zjistil aktivní službu prozrazující přítomnost hostitele, který neodpověděl na ping.





- "`-PA <PORT>`": odešle paket TCP ACK na uvedeném portu (uvedených portech), aby zjistil aktivní firewall prozrazující přítomnost hostitele, který neodpověděl na ping.




Ve výše uvedeném příkladu jsem pro volbu "-PS" zadal porty, které považuji za nejčastěji exponované v kontextech Nmap. Tyto různé porty pak budou testovány na každém hostiteli, nikoliv proto, abychom zjistili, zda je služba, kterou hostí, skutečně aktivní, ale proto, abychom zjistili, zda nám to umožní objevit hostitele, který neodpověděl na naše ICMP Echo, a přitom je stále aktivní (prostřednictvím odpovědi od služby nebo firewallu hostitele).



Zde je vidět, co lze vidět na snímku sítě pořízeném v době takového skenování, v tomto případě výpisu na jediném cílovém hostiteli:



![nmap-image](assets/fr/30.webp)



pakety odeslané mapou Nmap při pokročilém zjišťování sítě bez skenování portů



Najdeme pakety TCP SYN, TCP ACK na portu TCP/80 a ICMP echo. Nmap provede všechny tyto testy pro každého hostitele, na kterého se zaměřuje naše kontrola zjišťování sítě.



### IV. Použití souboru prostředků k zaměření pomocí Nmapu



V reálných informačních systémech, které se někdy skládají z desítek či stovek sítí, podsítí a VLAN, se může zadávání cílů rychle ukázat jako složité. Proto je jednodušší použít soubor jako zdroj pro Nmap než je zadávat jeden po druhém na příkazovém řádku.



Na začátku vytvořte jednoduchý soubor, který bude obsahovat jeden záznam na řádek:



![nmap-image](assets/fr/31.webp)



soubor obsahující na každém řádku jeden cíl (hostitel nebo síť)



Dále můžeme použít všechny dosud známé možnosti Nmap a zadat možnost "-iL <cesta/soubor>":



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Nmap pak zahrne do skenování všechny cíle obsažené v našem souboru.



Pokud chcete mít jistotu, že budou zohledněny všechny cíle, můžete použít volbu "-sL -n". Nmap pak bude interpretovat pouze CIDRy a hostitele v souboru a zobrazí vám je, aniž by odesílal pakety po síti:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Tím je zajištěno, že seznam hostitelů, kteří mají být prohledáni, je přesný.



Poslední důležitý tip, o který bych se s vámi rád podělil, se týká **vyloučení hostitele nebo sítě v rámci skenování**. Tato potřeba vyloučit hostitele může být v řadě případů nezbytná, zejména pokud chceme mít jistotu, že **citlivá součást informačního systému nebude naším skenováním narušena nebo narušena**.



Častým příkladem takových potřeb je situace, kdy společnost vlastní průmyslové (PLC) nebo zdravotnické zařízení. Takové zařízení je někdy špatně navrženo a vůbec není určeno pro příjem špatně formátovaných paketů nebo jejich příliš velkého množství. Ze zřejmých důvodů dostupnosti nebo obchodního/lidského rizika je vhodnější je z testování vyloučit.



Chceme-li ze skenování vyloučit IP adresy nebo sítě, můžeme použít například volbu "--exclude" programu Nmap:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



V tomto příkladu prohledávám síť "192.168.1.0/24", ale vylučuji hostitele "192.168.1.140", který se v ní nachází. Na tohoto hostitele nebude Nmap posílat žádné pakety. Další příklad s vyloučením podsítě:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



Podobně proskenuji velkou síť "10.0.0.0/16", ale síť "10.0.100.0/24" se neprovede. Opět doporučuji použít volbu "-sL -n", abyste získali zcela jasný přehled o tom, kteří hostitelé budou skenováni a kteří budou ze skenování vyloučeni, zejména pokud pracujete v citlivém prostředí.



### V. Zjišťování sítě a skenování portů



Nyní můžeme zkombinovat to, co jsme se naučili v této části, s tím, co jsme se dozvěděli v předchozí části o možnostech skenování portů. Ve výchozím nastavení jsme viděli, že Nmap bude skenovat 1000 nejčastějších portů na každém aktivním hostiteli, kterého objeví. Viděli jsme, jak tomuto chování zabránit, pokud ho nechceme, ale můžeme ho plně ovládat, a dokonce i rozšířit, pokud to vyhovuje našim potřebám.



Například následující příkaz zkontroluje přítomnost naslouchající služby na portu TCP/22 na každém skenovaném hostiteli:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap nejprve provede zjišťování sítě, zobrazí seznam aktivních hostitelů a u každého z nich zkontroluje, zda je na portu TCP/22 přítomna služba.



Stejným způsobem můžeme provést úplnou kontrolu všech portů TCP u každého hostitele objeveného v síti "192.168.0.0/24", například s výjimkou hostitele "192.168.0.4":



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Všechny možnosti, které jsme se dosud naučili, můžete libovolně kombinovat podle vlastních potřeb.



### VI. Závěr



V této části jsme si ukázali, jak pomocí Nmapu mapovat síť pomocí různých možností. Nyní jsme se seznámili s cíli našeho skenování a také s chováním programu Nmap při skenování portů a metodou zjišťování hostitelů. A co je nejdůležitější, víme, jaké je výchozí chování a omezení Nmapu a jak používat jeho hlavní možnosti, abychom se dostali dále.



V další části se podíváme na mechanismy a možnosti zjišťování verzí služeb a operačních systémů skenovaných nástrojem Nmap.




## 6 - Zjišťování verzí služeb a operačního systému pomocí nástroje Nmap



### I. Prezentace



V této části se dozvíte, jak pomocí nástroje Nmap zjistit a přesně detekovat verze služeb a operačních systémů používaných skenovanými hostiteli. Podrobně se podíváme na to, jak Nmap tento úkol plní, a také na omezení tohoto nástroje, abychom lépe pochopili a interpretovali jeho výsledky.



Jak jsme viděli v předchozích částech tohoto návodu, ve výchozím nastavení se Nmap nedívá na to, jaké služby jsou vystaveny na portech, které skenuje a považuje za otevřené. Pokud tedy nasloucháte webové službě na portu TCP/22, Nmap ji bude nadále hlásit jako otevřenou, ale jako službu `SSH`. Je to proto, že k hledání vztahu mezi portem/protokolem a názvem služby (soubor `/etc/services/`) používá [databázi](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) místní ve vašem systému.



Ve většině případů vám [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) poskytne správné informace, protože v produkčním prostředí se takové případy vyskytují zřídka. Ve zbývajících případech se však bude jednat o situace, kdy je klasická služba ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP atd.) vystavena na neklasickém portu (např. 2022 pro službu SSH), v takovém případě Nmap nenajde ve své místní databázi shodu nebo shodu, která neodpovídá skutečnosti, a vy přijdete o důležité informace.



Nmap naštěstí nabízí velmi přesné možnosti a mechanismy, jak zjistit, jaká služba se za otevřeným portem skrývá. Má dokonce databázi dotazů a signatur pro přesnou identifikaci technologií a verzí. Kromě služeb dokáže Nmap identifikovat také použitou technologii a její verzi.



Právě tomu se budeme věnovat v této části.



### II. Jak zjistit technologii nebo verzi



#### A. Připomenutí způsobu identifikace technologie nebo verze



Identifikace technologie a verze zahrnuje vyhledání názvu služby, CMS, aplikace nebo softwaru naslouchajícího na cílovém portu. Například webová stránka je spravována systémem CMS (`WordPress`), provozována webovou službou (`Apache`, IIS, Nginx) a hostována serverem (Linux nebo Windows). Jak ale zjistíte, která webová služba je spuštěna?



Klasickou metodou pro zjištění těchto informací je _banner grabbing_, který spočívá v tom, že se jednoduše vyhledá místo, kde daná služba tyto informace zobrazuje, a údaje se přečtou. Velmi často služby ve své výchozí konfiguraci nebo zpracování zobrazují svůj název a dokonce i svou verzi jako první odpověď po připojení.



![nmap-image](assets/fr/32.webp)



zobrazit verzi, jakmile je navázáno spojení TCP službou FTP



Zde vidíme, že jednoduché připojení TCP k této službě prostřednictvím `telnetu` vede k paketu TCP obsahujícímu její technologii a verzi.



Jakmile zjistíte, s jakým typem služby máte co do činění, můžete této službě také posílat konkrétní příkazy nebo požadavky a získávat z ní informace. Tyto požadavky/příkazy lze posílat i naslepo (aniž byste si byli jisti, že se jedná o správný typ služby) v naději, že některý z nich vyvolá odpověď dané služby.



V jiných, pokročilejších případech je nutné odeslat specifické pakety, které vyvolají reakci, například chybu, která poskytne podrobné informace o použité verzi nebo technologii.



Jak si můžete představit, Nmap se pomocí všech těchto technik pokusí identifikovat přesný typ služby hostované na portu a také název její technologie a verze.



#### B. Porozumění sondám a shodám Nmap



K provádění všech těchto kontrol na každém skenovaném portu používá Nmap místní databázi, která je často aktualizována (stejně jako binární soubor nebo jeho moduly). Jedná se o textový soubor o několika tisících řádcích: `/usr/share/nmap/nmap-service-probes`.



Tento soubor se skládá z mnoha položek, které jsou uspořádány podle dvou hlavních zásad:





- `Sonda`: jedná se o definici paketu, který Nmap odešle ve snaze vyvolat reakci identifikované služby. Představte si to jako pokus o zaslepení, jako je _Hello? Guten Tag? Hello? Um... Buenos Dias perhaps?_. Jakmile cílová služba obdrží sondu, které rozumí (tj. mluví správným protokolem), odpoví Nmapu, který tak získá potvrzení, o jaký typ služby se jedná.





- Match": jedná se o regulární výrazy, které Nmap aplikuje na získanou odpověď. Pokud odeslání požadavku HTTP GET vyvolalo odpověď od služby, použije na tuto odpověď desítky regulárních výrazů, aby identifikoval přítomnost například slova `Apache`, `Nginx`, `Microsoft IIS` atd.




Existuje několik dalších směrnic pro specifické případy, ale hlavní pro pochopení fungování Nmapu a přizpůsobení jeho použití jsou tyto. Abychom si tuto teoretickou část přiblížili, uvedeme příklad:



![nmap-image](assets/fr/33.webp)



příklad sondy v souboru Nmap `/usr/share/nmap/nmap-service-probes`



V prvním řádku tohoto příkladu vidíme snadno pochopitelnou sondu s názvem `GetRequest`. Jedná se o paket TCP obsahující prázdný požadavek HTTP GET na kořenovou adresu webové služby pomocí protokolu HTTP/1.0, po kterém následuje řádkový posuv a prázdný řádek.



Řádek `ports` říká Nmapu, na který port má tuto sondu odeslat. To vám umožní stanovit priority testů a ušetřit čas.



Nakonec máme dva příklady `match`. První z nich například zařadí skenovanou webovou službu do kategorie `ajp13`, pokud regulární výraz obsažený v tomto řádku odpovídá přijaté odpovědi služby.



Abyste lépe pochopili, jak mohou sondy vypadat, uvádíme seznam některých sond, které najdete v tomto souboru (v době psaní tohoto návodu jich bylo celkem 188).



![nmap-image](assets/fr/34.webp)



příklad několika sond, které Nmap používá a které jsou v souboru `/usr/share/nmap/nmap-service-probes`._



První dva (nazvané `NULL` a `GenericLines`) jsou zde obzvláště zajímavé, protože jednoduše posílají prázdný paket TCP nebo paket obsahující zalomení řádku. Služby serveru se často ohlásí právě v okamžiku přijetí spojení, aniž by klient provedl nějakou konkrétní akci, příkaz nebo požadavek.



Zde je případ poněkud složitější _shody_:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



Přesný regulární výraz je zde obsažen mezi znaky `m|` a `|`, které ohraničují jakýkoli regulární výraz v tomto souboru. Věnujte prosím čas přečtení celého příkladu. V regulárním výrazu si všimněte výběru: `([\d.]+)`, který slouží k oddělení verze. Tento příklad také definuje další Elements, například název produktu `p/nginx/`, načtenou verzi `v/$1/` a CPE s verzí `cpe:/a:igor_sysoev:nginx:$1/`.



CPE (Common Platform Enumeration) je standardizovaný systém zápisu používaný k identifikaci a popisu softwaru a hardwaru. Tento formát umožňuje efektivnější správu zranitelností a bezpečnostních konfigurací a především jednotný způsob jejich reprezentace bez ohledu na to, o jaký produkt se jedná. Zde jsou dva příklady CPE: `cpe:/o:microsoft:windows_8.1:r1` a `cpe:/a:apache:http_server:2.4.35`



Zde jasně identifikujeme jejich typy `o` pro operační systém, `a` pro aplikaci, dodavatele, produkt a verze.



V případě _shody_ s jedním z těchto regulárních výrazů tedy získáme nejen název služby, ale také její verzi a přesný CPE, což usnadní vyhledávání CVE s dopadem na tuto verzi. Tyto informace najdete ve standardním výstupu Nmapu a uvidíte, že jsou velmi užitečné i pro další účely, kterým se budeme věnovat v několika dalších částech.



Přesná syntaxe _matches_ a obecněji direktiv v souboru `/usr/share/nmap/nmap-service-probes` tím nekončí a může se zdát poměrně složitá, pokud nejste zvyklí manipulovat s Nmapem a jeho výsledky. Měli byste však mít alespoň na paměti jeho existenci a obecné fungování, což se vám bude hodit později, až budete chtít pochopit nebo ladit výsledek, přizpůsobit skenování nebo dokonce přispět k vývoji Nmapu.



### III. Použití mapy Nmap k detekci verzí



Nyní budeme používat celou tuto složitou mechaniku _Probe_ a _Match_ pomocí jednoduché volby: `-sV`. Ta jednoduše řekne Nmapu: zkuste přesně zjistit, které služby a verze portů jste nastavili jako otevřené.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



Zde je úplný příklad výsledku takového příkazu:



![nmap-image](assets/fr/35.webp)



výsledky detekce verzí aplikací vystavených v síti pomocí nástroje Nmap



Zde vidíme, že se programu Nmap podařilo identifikovat všechny verze síťových služeb vystavených tímto cílem a zobrazit tyto informace v novém sloupci `VERSION`. Je možné zobrazit poměrně přesné informace, dokonce až na úroveň operačního systému, pokud jsou tyto informace součástí obnovené signatury.



Chceme-li podrobně porozumět tomu, co se děje během kontroly zranitelnosti, můžeme použít volbu `--version-trace`. Ta poskytne zobrazení v režimu ladění a zobrazí _Sondu_, která vedla k detekci:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



V důsledku toho budeme muset třídit velké množství informací. Pokuste se identifikovat řádky začínající slovy `Service scan Hard match`. Pak uvidíte řádky, jako jsou tyto:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Můžeme jasně vidět, které _Sondy_ byly použity ke zjištění technologie a verze (v tomto případě _Sondy_ `NULL` a `GetRequest`), stejně jako získané informace.



### IV. Zvládnutí testů a přesnost detekce



Nyní se vrátíme k direktivě v souboru `/usr/share/nmap/nmap-service-probes`, které jsme se dříve nevěnovali:



![nmap-image](assets/fr/36.webp)



direktiva `rarity` v souboru `/usr/share/nmap/nmap-service-probes`._



Tato direktiva se používá k označení vzácnosti (tj. priority/pravděpodobnosti) spojené s _Sondou_. Tento zápis od 1 do 9 umožňuje řídit úplnost analýzy prováděné Nmapem při odesílání _Sond_. V systému "notace" Nmapu poskytuje rarita 1 informace v naprosté většině případů, zatímco rarita 8 nebo 9 představuje velmi zvláštní případ, specifický pro konfiguraci nebo službu, která se vyskytuje zřídka.



Pro upřesnění, ve výchozím případě Nmap odešle každé identifikované službě _Sondy_, které mají vzácnost od 1 do 7. Pro lepší představu o rozložení _Sond_ podle _vzácnosti_ uvádíme jejich počet:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Může se to zdát protichůdné, ale 8 a 9 jsou vzácnější než ostatní. Je to právě proto, že sondy rarity 1 jsou obecné a fungují ve většině případů bez ohledu na službu (vzpomeňte si na sondu `NULL`, která jednoduše odešle prázdný paket TCP). Zatímco složitější sondy jsou pro každou službu téměř jedinečné.



Pokud chceme ručně spravovat sondy, které chceme použít při skenování verzí, můžeme použít volbu `--version-intensity`. Zde jsou dva příklady:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Na závěr tohoto tématu uvádíme příklad _Sondy_ 9 a 8:



![nmap-image](assets/fr/37.webp)



příklady sond s raritou 8 a 9 v souboru `/usr/share/nmap/nmap-service-probes`._



Tyto dvě _Sondy_ detekují servery Quake1 a Quake2 (videohra). Zajímavé z nostalgického hlediska, ale v běžném životě pravděpodobně nebudou příliš užitečné.



V závislosti na vašich požadavcích na přesnost nebo rychlost nezapomeňte, že tento princip "vzácnosti" existuje a může ovlivnit výsledek.



### V. Použití Nmap k detekci operačních systémů



Nyní se podíváme na to, jak nám Nmap může pomoci zjistit operační systémy hostitelů skenovaných a detekovaných v síti. K tomu použijeme volbu `-O` (pro `OS Scan`) programu Nmap.



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



Zde je příklad výsledků. Zde nám Nmap říká, že se pravděpodobně jedná o operační systém Linux, a nabízí nám různé statistiky týkající se jeho přesné verze.



![nmap-image](assets/fr/38.webp)



zjišťování pravděpodobnosti identifikace operačního systému pomocí nástroje Nmap



K dosažení tohoto cíle bude Nmap používat řadu technik, které fungují velmi podobně jako _Probes_ a _Matches_ pro detekci technologií a verzí. Hlavní rozdíl spočívá v tom, že Nmap bude používat poměrně "nízkoúrovňové" parametry protokolů ICMP, TCP, UDP a dalších. Zde jsou dva testovací příklady pro detekci operačního systému Microsoft Windows 11:



![nmap-image](assets/fr/39.webp)



příklady testů provedených nástrojem Nmap k detekci operačního systému Windows 11



Přiznejme si, že tyto testy jsou velmi obtížné na interpretaci a nebudeme se je snažit pochopit do hloubky v rámci úvodního kurzu Nmap. Pokud byste se chtěli do této problematiky ponořit hlouběji, soubor obsahující tyto informace se nachází v adresáři `/usr/share/nmap/nmap-os-db`.



Je však třeba si uvědomit, že detekce operačního systému je spíše pravděpodobná, než jistá.



### VI. Závěr



V této části jsme se naučili používat možnosti nástroje Nmap pro zjišťování technologií, verzí a operačních systémů skenovaných hostitelů a služeb. Nyní již dobře rozumíme tomu, jak Nmap tyto informace získává na dálku. Prošli jsme si také možnosti správy hovorovosti a přesnosti testů a také omezení nástroje v těchto oblastech.



V další části se dozvíme, jak pomocí skriptů Nmap NSE provést bezpečnostní analýzu našeho informačního systému. Pokud budete potřebovat, věnujte čas opětovnému přečtení posledních částí a neváhejte si sami procvičit a ponořit se do útrob nástroje, abyste lépe zvládli to, co jsme se dosud naučili.




## 7 - Bezpečnostní analýza: odhalování zranitelností



### I. Prezentace



V této části se naučíme používat nástroj Nmap pro skenování sítě k detekci a analýze zranitelností v cílech našeho skenování. Zejména se podíváme na různé možnosti, které jsou k dispozici pro splnění tohoto úkolu, a prozkoumáme hranice možností nástroje, abychom lépe pochopili a interpretovali jeho výsledky.



V této první části se podíváme na skener zranitelností Nmap a zjistíme, jak používat základní možnosti detekce zranitelností. V následujících částech se blíže podíváme na to, jak tato funkce funguje a jak ji lze přizpůsobit.



### II. Použití Nmap k detekci zranitelností



Nyní chceme pomocí síťového skeneru Nmap odhalit zranitelnosti služeb a systémů našeho informačního systému. To znamená, že kromě zjišťování aktivních hostitelů, výčtu vystavených služeb a zjišťování verzí a technologií bude Nmap hledat zranitelnosti.



Za tímto účelem se Nmap spoléhá na skripty NSE (_Nmap Scripting Engine_), které lze považovat za moduly umožňující granulární přístup k testování.



Pomocí správných voleb požádáme Nmap, aby použil své různé skripty NSE na každou objevenou službu, což nám umožní zjistit:





- Poruchy konfigurace ;





- Další a pokročilejší verze a objevy OS ;





- Známé zranitelnosti (CVE) ;





- Slabé identifikátory ;





- Charakteristické znaky Elements infekce malwarem ;





- Možnosti odepření služby ;





- Atd.




Jak vidíte, skripty NSE významně rozšiřují možnosti Nmapu, pokud jde o síťové operace, které může provádět. A to k provádění mnohem pokročilejších úloh než kdykoli předtím. Dobrou zprávou je, že jako obvykle lze tyto funkce používat jednoduše prostřednictvím volby a ve výchozím kontextu. Právě to si ukážeme příště.



### III. Příklad kontroly zranitelnosti



Skripty NSE lze použít při použití nástroje Nmap ke skenování jednoho portu na hostiteli, všech služeb na tomto hostiteli nebo všech služeb zjištěných v několika sítích. Možnosti, které si ukážeme, tedy můžeme použít ve všech souvislostech, které jsme dosud studovali.



Chceme-li povolit skenování zranitelností pomocí programu Nmap, musíme použít volbu `-sC`:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Nezapomeňte, že ve výchozím nastavení, pokud nic nezadáte, bude Nmap skenovat pouze 1000 nejběžnějších portů. Nezjistí zranitelnosti na exotičtějších portech, které mohou vaše cíle vystavovat.



Před použitím této funkce v produkčním informačním systému vás vyzývám, abyste pokračovali ve čtení tohoto návodu. V následujících částech se podíváme na to, jak lépe kontrolovat dopad a typy testů, které budou spuštěny.



Díky opakovanému použití toho, co jsme se naučili dříve, můžeme být například komplexnější a prohledat všechny porty TCP cíle:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Zde je výsledek skenování Nmap pomocí skriptů NSE:



![nmap-image](assets/fr/40.webp)



příklad výsledků skenování zranitelností hostitele pomocí nástroje Nmap._



Zde vidíme zobrazení dalších informací, které nás zajímají v souvislosti s analýzou zranitelnosti:





- Ke službě FTP lze přistupovat anonymně a není chráněna ověřováním. Skript NSE, který má toto ověření na starosti, nám to sdělí a dokonce zobrazí část stromové struktury služby FTP. Zde vidíme, že máme přístup do adresáře `C` systému Windows!





- Skript NSE, který má na starosti pokročilé vyhledávání webových služeb, zobrazuje název stránky, což nám dává lepší představu o tom, co webová služba hostuje.





- Provedeme také mini analýzu konfigurace služby SMB (skripty `smb2-time`, `smb-security-mode` a `smb2-security-mode`). Informace jsou zobrazeny trochu jinak, za výsledkem kontroly sítě, aby byly lépe čitelné. Tyto informace označují zejména nepřítomnost signatur SMB Exchange. Tato slabina konfigurace umožňuje použít cíl při útoku SMB Relay, což je pozoruhodná bezpečnostní chyba často využívaná při testech vniknutí/kybernetických útoků.




To je samozřejmě jen jeden příklad. Nmap má skripty NSE pro mnoho služeb zaměřených na širokou škálu zranitelností. Na tyto možnosti se blíže podíváme v následující části.



Na závěr tohoto úvodu do skenování zranitelností uvádíme kompletní příkaz pro zjišťování sítě, skenování portů TCP a detekci verzí a zranitelností:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



Zde je příkaz, který začíná vypadat jako reálnější případy použití Nmapu!



### IV. Pochopení omezení Nmapu při skenování zranitelností



Aby bylo jasno: Nmap není schopen provést kompletní penetrační test vašeho informačního systému nebo simulovat operaci Red Teamu. Má několik omezení, kterých si musíte být vědomi, pokud nechcete mít falešný pocit bezpečí:





- Omezené pokrytí**: Přestože jsou skripty NSE Nmapu výkonné, jejich pokrytí testů může být ve srovnání s jinými specializovanými nástroji pro odhalování zranitelností omezené. Některé zranitelnosti nemusí být dostupnými skripty NSE pokryty, například zranitelnosti služby Active Directory, odhalení citlivých dat nebo pokročilejší případy zranitelných webových aplikací.





- Složitost zranitelnosti**: některé typy zranitelností může být obtížné odhalit pomocí skriptů NSE kvůli jejich složitosti. Například zranitelnosti vyžadující složitou interakci se vzdálenou službou nemusí být pomocí Nmap efektivně odhaleny (jako v případě nadměrných oprávnění ve sdíleném souboru nebo chyby v řízení oprávnění ve webové aplikaci).





- Pasivní detekce**: Nmap se při detekci zranitelností zaměřuje především na aktivní skenování, což znamená, že bez navázání aktivního spojení s cílovými hostiteli nemusí efektivně odhalit potenciální zranitelnosti. Zranitelnosti, které se během aktivního skenování neprojeví, proto mohou být přehlédnuty (jako v případě injektáže kódu ve webové aplikaci).





- Závislost na aktualizacích**: [databáze](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) skriptů NSE se neustále vyvíjí, ale mezi objevením nové zranitelnosti a přidáním odpovídajícího skriptu do Nmapu může dojít ke zpoždění. V důsledku toho nemusí být Nmap vždy aktuální s nejnovějšími zranitelnostmi.





- Falešně pozitivní a falešně negativní výsledky**: Stejně jako u jiných bezpečnostních nástrojů mohou skripty NSE Nmapu vytvářet falešně pozitivní (falešná upozornění na zranitelnosti) nebo falešně negativní výsledky (skutečné zranitelnosti nebyly odhaleny). To je třeba mít na paměti při analýze výsledků aplikace Nmap.




Proto je důležité pochopit, co Nmap dělá a nedělá, a stejně tak vědět, jak interpretovat jeho výsledky. Zejména jsme si v tomto návodu ukázali, že výchozí volby mohou vést k tomu, že nám unikne důležitá funkce Elements, kterou lze při pečlivém používání odhalit.



Ať už jste správce síťového systému, bezpečnostní inženýr nebo dokonce CISO, pomocí nástroje Nmap získáte přehled o stavu zabezpečení informačního systému. Jedná se o důležitý první krok k zabezpečení systému, který může tým IT provádět pravidelně. Neměl by však nahradit zásah a rady odborníků [na kybernetickou bezpečnost] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), kteří budou schopni odhalit slabá místa mnohem komplexněji než Nmap.



### V. Závěr



V této první části modulu 3 jsme se seznámili se skenováním zranitelností pomocí nástroje Nmap. Nyní již víme, jak používat hlavní volbu k provedení tohoto úkolu, ale známe také limity tohoto cvičení. V další části se na tuto funkci podíváme blíže a pomocí skriptů NSE rozšíříme možnosti Nmapu desetinásobně.



## 8 - Použití skriptů NSE Nmapu



### I. Prezentace



V této části se podrobně podíváme na skripty NSE (_Nmap Scripting Engine_). Zejména se podíváme na to, proč jsou jednou z velkých předností tohoto nástroje, jak fungují a jak procházet a používat mnoho existujících skriptů.



Tato část navazuje na předchozí výukový kurz, ve kterém jsme se naučili používat základní funkce skenování zranitelností Nmapu. Nyní se blíže podíváme na to, jak v tomto ohledu funguje [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/), abychom mohli opět provádět přesnější a kontrolovanější skenování.



### II. Koncepce skriptů Nmap NSE



Skripty Nmap NSE umožňují velmi flexibilně rozšiřovat jeho možnosti. Jsou napsány v jazyce LUA, což je skriptovací jazyk, který je snadněji ovladatelný a přístupný než jazyk C nebo C#, který používá Nmap. Výhodou použití skriptů LUA s nástrojem Nmap namísto samostatného nástroje je, že nám umožňuje využít rychlost provádění a standardní funkce nástroje Nmap (zjišťování hostitele, portu a verze atd.).



Tyto skripty jsou uspořádány podle kategorií a jeden skript může patřit do více než jedné kategorie:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Technicky jsou kategorie, do kterých skript patří, uvedeny přímo v jeho kódu.



![nmap-image](assets/fr/41.webp)



kategorie skriptů nSE `ftp-anon`._



Tento příklad ukazuje část kódu skriptu NSE `ftp-anon.nse`, jehož spuštění jsme viděli v předchozí části.



### III. Seznam stávajících skriptů NSE



Ve výchozím nastavení jsou skripty Nmap NSE umístěny v adresáři `/usr/share/nmap/scripts/` bez specifické stromové struktury nebo hierarchie. Zde je přehled obsahu tohoto adresáře:



![nmap-image](assets/fr/42.webp)



rozbalí obsah adresáře `/usr/share/nmap/scripts/` obsahujícího skripty NSE._



Tento adresář obsahuje více než 5 000 skriptů NSE. Ve většině případů obsahuje první část názvu skriptu protokol nebo kategorii, do které patří. To nám umožňuje seznam seřadit, například pokud chceme vypsat všechny skripty zaměřené na službu FTP:



![nmap-image](assets/fr/43.webp)



seznam skriptů NSE Nmap s názvy začínajícími na `ftp-`._



Nmap ve skutečnosti nenabízí možnost procházení a výpis skriptů NSE; můžete použít příkaz `--script-help` následovaný názvem kategorie nebo slovem:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



Výstupem však bude název každého skriptu a jeho popis, což není optimální, pokud vyhledávání přinese několik desítek skriptů:



![nmap-image](assets/fr/44.webp)



výsledek použití příkazu `--script-help` programu Nmap



Podle mého názoru je nejefektivnější metodou použití klasických linuxových příkazů v adresáři `/usr/share/nmap/scripts/`:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Neváhejte si prohlédnout kód modulů, které vás osloví, abyste lépe pochopili, jak skript NSE funguje.



### IV. Použití skriptů Nmap NSE



Nyní se naučíme provádět skenování zranitelností pečlivým výběrem skriptů NSE, které nás zajímají.



#### A. Výběr skriptů podle kategorie



Pro začátek můžeme zvolit spuštění všech skriptů patřících do určité kategorie. Tuto kategorii nebo tyto kategorie musíme Nmapu označit argumentem `--script <category>`:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Tento první příkaz je ekvivalentem příkazu `nmap -sC`. Ve výchozím nastavení Nmap vybere skripty v kategorii `default`, ale to jen pro představu. Další příkaz například použije všechny skripty v kategorii `discovery`:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Jak jsme viděli, některé kategorie nám umožňují rychle identifikovat, co příslušné skripty NSE dělají (`discovery`, `vuln`, `exploit`), zatímco jiné definují úroveň rizika, detekce nebo stability provedeného testu. Pokud se nacházíme v citlivém kontextu a nemáme dobrou představu o různých činnostech prováděných naším výběrem skriptů, můžeme se rozhodnout kombinovat výběry a vybrat pouze ty skripty, které patří do kategorií `discovery` a `safe`:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Pokud chcete bezpodmínečně a výslovně vyloučit skripty z kategorií `dos` a `intruzivní`, můžete použít následující zápis:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Vezměte prosím na vědomí, že zadání výše uvedených podmínek vyloučení bude mít za následek použití všech ostatních kategorií, které nejsou výslovně vyloučeny. Abychom byli spravedlivější, mohli bychom zadat např:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Zde je několik příkladů, jak zacházet se skripty NSE podle kategorií, zejména při použití Nmapu pro analýzu zranitelností v reálném prostředí.



#### B. Výběr skriptů jako celku



Můžeme také zvolit provedení jednoho konkrétního testu během analýzy, testu odpovídajícího skriptu NSE. K tomu je třeba zadat název skriptu v parametru `-script <name>`. Vezměme si příklad skriptu `ftp-anon.nse`:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



Pak získáme velmi přesný výsledek:



![nmap-image](assets/fr/45.webp)



výsledek použití skriptu NSE `ftp-anon` na portu FTP prostřednictvím Nmap._



Vidíme výsledek spuštění skriptu `ftp-anon` na portu 21 a na žádném jiném portu, protože jsme zadali volbu `-p 21`. Mohli jsme také provést základní kontrolu portů a spustit skript `ftp-anon` NSE pouze na nalezených službách FTP:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Nmap by tedy tento test anonymního připojení provedl i v případě, že by našel službu FTP na jiném portu.



Pro stručný popis toho, co skript NSE dělá, můžete použít výše uvedenou volbu `--script-help`:



![nmap-image](assets/fr/46.webp)



help zobrazení výsledku pro NSE skript `sshv1`._



Stručně řečeno, opět můžeme znovu použít všechny možnosti, služby, verze a technologie pro zjišťování sítě, které jsme dosud používali!



#### C. Správa argumentů skriptu



Při používání Nmapu se setkáte s některými skripty NSE, které pro správnou funkci vyžadují vstupní argumenty. Nyní se podíváme na to, jak těmto skriptům předávat argumenty prostřednictvím možností Nmapu.



Jako příklad uveďme skript `ssh-brute`, který umožňuje provést útok hrubou silou na službu SSH.



Klasický útok hrubou silou spočívá v otestování několika hesel (někdy i milionů) při pokusu o autentizaci k určitému účtu. Tím, že útočník vyzkouší tolik hesel, sází na pravděpodobnost, že uživatel použil slabé heslo ze slovníku hesel použitého pro útok.



Tento skript má "výchozí" možnosti, které bychom mohli upravit tak, aby vyhovovaly našemu kontextu. V kontextu tohoto útoku můžeme například poskytnout Nmapu seznam uživatelů a slovník hesel, který se má použít. Pokud vím, není možné jednoduše vypsat argumenty požadované pro skript, takže nejspolehlivějším způsobem je navštívit oficiální webové stránky Nmap. Přímý odkaz na dokumentaci ke skriptu NSE lze získat jako odpověď na volbu `--script-help`:



![nmap-image](assets/fr/47.webp)



výsledek zobrazení nápovědy pro skript NSE `ssh-brute` s odkazem na nmap.org._



Kliknutím na uvedený odkaz se dostaneme na tuto webovou stránku webu [https://nmap.org](https://nmap.org/):



![nmap-image](assets/fr/48.webp)



seznam argumentů, které lze předat skriptu Nmap `ssh-brute` NSE



Zde máme jasný přehled o argumentech, které lze použít, z nichž hlavní jsou v našem kontextu `passdb` (soubor obsahující seznam hesel) a `userdb` (soubor obsahující seznam uživatelů). Dokumentace zde odkazuje na interní knihovny Nmapu, protože tyto mechanismy hrubé síly a související volby jsou vzájemně propojeny, aby se daly jednotně používat v několika skriptech (`ssh-brute`, `mysql-brute`, `mssql-brute` atd.), a proto budou mít víceméně stejné argumenty:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Jak vidíte v tomto posledním příkazu, můžeme zadat potřebné argumenty skriptu Nmap pomocí volby `--scripts-args key=value,key=value`. Zde je možný výsledek výstupu Nmapu při provádění SSH brute force pomocí skriptu `ssh-brute` NSE:



![nmap-image](assets/fr/49.webp)



výsledek provedení SSH bruteforce pomocí Nmap._



Jak vidíte, informace generované skripty NSE jsou v interaktivním výstupu (terminálovém výstupu) opatřeny předponou `NSE: [název skriptu]`, což usnadňuje jejich vyhledávání. V rámci obvyklého zobrazení výsledků Nmapu máme jednoduše k dispozici shrnutí, které uvádí, zda byly nebo nebyly objeveny slabé identifikátory (včetně hesel, nezapomeňte).



Abychom se posunuli ještě o krok dál a připomněli vám, že to vše lze použít jako doplněk ke všem možnostem, které jsme si již představili, uvádíme příkaz, který zjistí síť `10.10.10.0/24`, prohledá 2000 nejčastějších portů TCP a spustí anonymní vyhledávání přístupu ke službám FTP a kampaň hrubé síly ke službám SSH:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Toto je jen jeden příklad z mnoha dostupných skriptů a jejich možností. Nyní však máme lepší představu o tom, jak se se skripty NSE vypořádat, zda vyžadují argumenty a jak tyto argumenty Nmapu předat.



### V. Závěr



V této části jsme se naučili používat skripty Nmap NSE k provádění různých úloh. Zvu vás, abyste věnovali čas objevování různých kategorií skriptů a samotných skriptů a zjistili, kolik testů mohou automatizovat.



Již několik sekcí se nám hromadí více či méně pokročilé možnosti zjišťování, skenování a výčtu. Nyní byste si již měli být vědomi toho, že výstup a zobrazení výsledků Nmapu začíná být poměrně rozsáhlé, někdy až příliš mnohomluvné pro náš terminál. V příští části se naučíme, jak tento výstup zvládnout, zejména jeho ukládáním do souborů v různých formátech.






## 9 - Správa výstupních dat Nmap




### I. Prezentace



V této části se podíváme na výstup vytvořený nástrojem Nmap, a zejména na různé možnosti formátování tohoto výstupu. Uvidíme, že Nmap může vytvářet několik výstupních formátů, které vyhovují různým potřebám, a že i to je jedna z velkých předností tohoto nástroje.



Ve výchozím nastavení nabízí Nmap podrobné zobrazení výsledků provedených skenování a testů. Zahrnuje skenované hostitele a služby, ty, které byly zjištěny jako přístupné, specifika otevřených portů, jejich stav a verzi. Kromě toho jsou ve výstupu terminálu k dispozici také podrobnosti o skriptech NSE. Tento výstup však může být i při přehledném formátování informací rychle obsáhlý, což může ztěžovat hledání přesných informací ve výsledcích.



### II. Zvládnutí výstupních formátů Nmap



#### A. Uložení výsledků skenování do textového souboru



Pro usnadnění práce umožňuje [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) velmi snadno uložit výstup do textového souboru. To může být užitečné pro archivaci, porovnání s jinými testy, ale také pro prohlížení tohoto výstupu pomocí specializovaných nástrojů pro zpracování textu nebo skriptovacích jazyků, jako je Sublime text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed atd. Pro uložení standardního výstupu Nmapu do textového souboru můžeme použít volbu `-oN <jméno souboru>` (písmeno "N" ve slově "normal"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Žádné překvapení, protože Nmap zobrazí svůj obvyklý standardní výstup v našem terminálu, ale také v zadaném souboru.



#### B. Výstup generate Nmap ve zkráceném formátu



Existuje také druhý výstupní formát ve stylu "text", který lze snadno interpretovat člověkem: formát "greppable".



Tento formát byl vytvořen pro "zhuštěný" pohled na výstup Nmapu, strukturovaný tak, aby usnadnil jeho zpracování nástroji, jako je `grep`. Podívejme se na příklad tohoto typu výstupu:



![nmap-image](assets/fr/50.webp)



nmap skenování sítě a výstup ve formátu "greppable"._



Zde jsem provedl zjišťování sítě a skenování portů a analýzu technologií a verzí v síti /24 a poté jsem výstup uložil do souboru ve formátu "greppable". Nakonec jsem získal soubor obsahující 2 řádky pro každého aktivního hostitele:





- První řádek mi říká, že takový a takový hostitel je _Up_;





- Druhý řádek mi sdělí, které porty byly skenovány, jejich stav a informace o technologii a verzi, které byly získány ve velmi specifickém formátu: `<port>/<stav/<protokol>//<služba>//<verze>/,`




Toto formátování s pevným oddělovačem umožňuje rychlé zpracování pomocí nástrojů pro zpracování textu, jako je `grep`, nebo skriptovacích a programovacích jazyků. Následující příkaz mi například umožňuje snadno získat informace o hostiteli `10.10.10.5` v případě rozsáhlého skenování provedeného programem Nmap, jehož výstup by bylo obtížné procházet:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



Naopak mohu také snadno vypsat všechny hostitele, kteří mají otevřený port 21, protože porty a IP jsou na stejném řádku:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



Chceme-li získat takový výstup, musíme použít volbu `-oG <jméno souboru>.gnmap` (písmeno "G" ve slově "grep"). Ze zvyku zde pro takový soubor používám příponu `.gnmap`, ale klidně použijte jakoukoli:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Tento formát lze použít k různým účelům a je obzvláště užitečný pro rychlé skriptování/třídění. Nicméně se od něj spíše upouští ve prospěch formátu, kterému se budeme věnovat příště.



poznámka: formát `-oG` greppable je od verze Nmap 7.90 oficiálně zastaralý. Kvůli kompatibilitě jej lze stále používat. Pro účely kompatibility jej lze stále používat, ale pro jakýkoli vývoj nebo automatizované analyzování se doporučuje používat XML nebo normální formát._



#### C. Formát XML pro výstup Nmap



Posledním formátem, který stojí za zmínku v tomto tutoriálu, je XML. Na rozdíl od předchozích dvou formátů není tento určen ke čtení lidmi, ale jinými nástroji nebo skripty.



XML (_eXtensible Markup Language_) je značkovací jazyk používaný k ukládání a přenosu dat, který nabízí hierarchickou strukturu pomocí vlastních značek.



Formát XML se v rámci aplikace Nmap používá k podrobným zprávám generate o provedených skenováních, včetně informací o hostitelích, portech a zjištěných zranitelnostech, jakož i dalších informací, které se ve standardním výstupu aplikace Nmap nezobrazují.



Chceme-li výstupní soubor generate ve formátu XML, musíme použít volbu `-oX` ("O" od "XML"):



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



Výsledkem je standardní výstup Nmapu v terminálu a soubor ve formátu XML v aktuálním adresáři.



Formát XML samozřejmě není určen ke čtení a interpretaci lidmi. Nicméně pokud chcete provádět skriptování nebo automatizovanou analýzu tohoto formátu výstupu Nmap, musíte mít představu o použitých značkách a struktuře. Zde je například část obsahu souboru XML vytvořeného programem Nmap, který zobrazuje výsledky skenování pro 1 hostitele:



![nmap-image](assets/fr/51.webp)



příklad záznamu XML pro 1 hostitele během skenování Nmapem



Je zde mnoho informací a nás zajímají zejména dva otevřené porty:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Chápeme, že tento formát usnadní automatické analyzování výsledků, protože každá informace je přehledně uspořádána ve vyhrazeném pojmenovaném tagu nebo atributu. Zejména zde najdeme informaci, se kterou jsme se dosud nesetkali: CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



O CPE jsme se krátce zmínili v části 2 modulu 2 a tato informace se zjišťuje při shodách během detekce verze. Nmap používá své mechanismy detekce služeb, technologií a verzí k nalezení přidruženého CPE.



Díky tomu můžeme tyto informace opakovaně používat v databázích a aplikacích, které je používají. Mám na mysli zejména databázi NVD, která odkazuje na CVE. U každé CVE obsahuje CPE, kterých se zranitelnost týká. Zde je příklad CVE týkající se `a:microsoft:internet_information_services:7.5` z databáze NVD:



![nmap-image](assets/fr/52.webp)



přítomnost CPE v údajích o CVE v databázi NVD



Nyní již lépe chápeme výhody tohoto formátu, který nabízí velmi přehlednou strukturu informací a obsahuje všechna data shromážděná nebo zpracovaná systémem Nmap.



Reflexivně systematicky ukládám skenování Nmapu ve všech třech formátech najednou. Umožňuje to volba `-oA <název>` ("A" jako "All"), která vytvoří soubor `<název>.nmap`, soubor `<název>.xml` a soubor `<název>.gnmap`. Tímto způsobem mám jistotu, že mi nic nedojde, až se budu potřebovat vrátit k výsledkům.



S těmito třemi formáty byste měli mít vše, co potřebujete k ukládání a případnému automatizovanému zpracování výsledků Nmap. Formát XML budeme opět používat v příští části, kdy se budeme zabývat používáním Nmapu s dalšími bezpečnostními nástroji.



#### III. Generování HTML zprávy ze skenování Nmap



Formát XML nabízí mnoho možností, v neposlední řadě slouží jako základ pro generování zprávy ve formátu HTML, který je vizuálně příjemnější pro prohlížení.



K transformaci souboru Nmap ve formátu XML na webovou stránku použijeme nástroj `xsltproc`, který si musíme nejprve nainstalovat:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Po instalaci tohoto nástroje mu jednoduše zadejte soubor XML, který má být převeden, a název sestavy HTML, která má být vygenerována:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Díky tomu budeme mít celý sken pěkně strukturovaný, dokonce s několika barvami a klikacími odkazy v obsahu!



![nmap-image](assets/fr/53.webp)



výpis ze zprávy o skenování Nmap ve formátu HTML vygenerované pomocí xsltproc._



Obecně řečeno, soubor XML uložený aplikací Nmap obsahuje odkaz na jiný soubor ve formátu XSL:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



Převod do HTML je tedy funkce, kterou poskytuje a usnadňuje Nmap, přičemž `xsltproc` je běžný a uznávaný nástroj pro provádění tohoto úkolu (který nepochází ze sady nástrojů Nmap).



XSLT (_Extensible Stylesheet Language Transformations_) je podmnožinou jazyka XSL, která umožňuje zobrazit data XML na webové stránce a "transformovat" je souběžně se styly XSL na čitelné a formátované informace ve formátu HTML.



zdroj: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



Úroveň informací v hlášení je stejná jako ve formátu XML programu Nmap a vyšší než ve standardním terminálovém výstupu (_interaktivní výstup_).



### IV. Správa úrovně hovorovosti Nmapu



Nyní se podíváme na několik možností pro Debugger Nmap nebo pro sledování jeho průběhu.



První volbou, kterou bychom měli zmínit, je volba `-v`, která zvyšuje slovní rozsah Nmapu. Zde je příklad:



![nmap-image](assets/fr/54.webp)



slovní výstup nmapu pomocí volby `-v`._



Při skenování zaměřeném na mnoho hostitelů a portů bude výstup terminálu obtížně zneužitelný kvůli množství zobrazených informací. Z tohoto důvodu by se tato možnost měla používat v kombinaci s dříve uvedenými možnostmi, které umožňují ukládat standardní výstup Nmapu do souboru. Informace související s použitím verbosity nebudou do tohoto výstupního souboru zahrnuty. Jak je vidět z výše uvedeného příkladu, tato slovní zásoba umožňuje přehledně a přímo sledovat akce a objevy programu Nmap. U delších skenů, kde může být zobrazování dat pomalé, se tak vyhnete tomu, abyste byli slepí k aktuální činnosti Nmapu a věděli, že věci postupují a jakým tempem. Chcete-li zvýšit hovorovost o další úroveň, můžete použít volbu `-vv`.



Chcete-li dále sledovat činnost programu Nmap během skenování, můžete použít volbu `--packet-trace`. S volbou `-v` získáme živý protokol všech otevřených portů, které Nmap objevil, zatímco s touto volbou získáme řádek protokolu pro každý paket odeslaný na port. To přirozeně vytváří velmi mnohomluvný výstup, ale umožňuje podrobné sledování činnosti Nmapu, zde je příklad:



![nmap-image](assets/fr/55.webp)



podrobné sledování aktivity Nmap pomocí `--packet-trace`._



Pokud jsou použity volby `-oN`, `-oG`, `-oX` nebo `-oA`, tyto informace se opět nezaznamenají do výstupního souboru vytvořeného nástrojem Nmap.



Nmap nabízí také dvě možnosti ladění: `-d` a `-dd`. Tyto volby se chovají podobně jako volba `-v` verbosity, ale přidávají další technické informace, například souhrn technických parametrů na začátku skenování:



![nmap-image](assets/fr/56.webp)



možnosti časování se zobrazují v zobrazení ladění Nmapu



V několika následujících částech se podíváme na to, jaké jsou možnosti "Timing" a proč se vyplatí je znát.



Pokud chcete mít pouze základní syntetický přehled o průběhu skenování Nmap, můžete použít volbu `--stats-every 5s`. Hodnota "5s" zde znamená 5 sekund a lze ji upravit podle vašich potřeb. Jedná se o frekvenci, s jakou budeme od Nmapu dostávat zpětnou vazbu o jeho průběhu:



![nmap-image](assets/fr/57.webp)



informace zobrazené volbou `--stats-every` programu Nmap



Zejména můžeme získat procento pokroku a také údaj o fázi, ve které se nachází: fáze zjišťování hostitele pomocí [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/), fáze zjišťování exponovaných portů TCP atd. Tyto informace lze také získat ve výstupu terminálu stisknutím klávesy "Enter" během skenování.



Nmap však neumí příliš dobře odhadnout, jak dlouho bude úloha trvat, a to i proto, že předem neví, kolik hostitelů a služeb bude muset prohledat.



### V. Závěr



V této části jsme se zabývali několika možnostmi ukládání výsledků skenování Nmap do různých formátů souborů. To se bude velmi hodit, protože v reálném kontextu mohou výsledky skenování zabírat stovky nebo dokonce tisíce řádků! Také jsme se podívali, jak zvýšit úroveň slovního rozsahu Nmapu pro účely ladění nebo pro získání zprávy o průběhu skenování.



Formát XML bude užitečný zejména v následující části, kde se podíváme na několik nástrojů, které mohou pracovat s výsledky Nmap.




## 10 - Použití Nmapu s dalšími bezpečnostními nástroji



### I. Prezentace



V této části se podíváme na některá klasická použití Nmapu s dalšími bezplatnými a open source bezpečnostními nástroji. Zejména využijeme to, co jsme se naučili v předchozích částech, k dalšímu zvýšení výkonu a efektivity Nmapu.



Díky možnosti ukládat výsledky skenování Nmap ve formátu XML jsou data kompatibilní s řadou dalších nástrojů. Vzhledem k tomu, že téměř všechny programovací a skriptovací jazyky dnes mají knihovny schopné zpracovávat XML, je zpracování těchto dat mnohem snazší. Řada nástrojů, zejména těch zaměřených na útočnou bezpečnost, má funkce pro zpracování formátu XML generovaného nástrojem Nmap. Podívejme se na ně blíže.



Zmíním se o několika útočných nástrojích, aniž bych podrobně popsal, jak se používají a jak fungují. Budu předpokládat, že čtenář je seznámen s jejich základním použitím a že jsou již funkční. Tato část bude zajímavá zejména pro profesionály [v oblasti kybernetické bezpečnosti] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), lidi ve výcviku nebo pro ty, kteří se rozhodli do této problematiky hlouběji ponořit.



### II. Import výsledků Nmap do Metasploitu



Prvním nástrojem, na který se podíváme a který umožňuje opakovaně používat data Nmapu při výzkumu útočné bezpečnosti a zranitelností, je Metasploit.



Metasploit je framework pro zneužití a útoky. Jedná se o bezplatné řešení a uznávaný nástroj, který obsahuje velké množství modulů napsaných v jazyce Ruby nebo Python. Ty umožňují využívat zranitelnosti, provádět útoky, generovat zadní vrátka, spravovat zpětná volání (C&C neboli Communication and Control functions) a vše jednotně používat.



Tento známý a široce používaný operační systém může pracovat zejména s [databází] postgreSQL(https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/), ve které jsou uloženy informace o hostitelích, portech, službách, ověřování a další.





- Oficiální dokumentace Metasploitu: [https://docs.metasploit.com/](https://docs.metasploit.com/)




Zde přichází ke slovu Nmap a jeho výstup, protože formát XML výstupu Nmap lze snadno importovat do databáze Metasploitu a naplnit tak jeho databázi hostitelů a služeb, které lze následně rychle označit jako cíle toho či onoho útoku.



Jakmile se dostanu do interaktivního prostředí Metasploitu, začnu tím, že si vytvořím pracovní prostor, jakýsi prostor specifický pro mé aktuální prostředí:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Po vytvoření pracovního prostoru je třeba ověřit, zda je komunikace s databází funkční:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Nakonec můžeme použít příkaz Metasploitu `db_import` k importu našeho skenování Nmap ve formátu XML:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Zde je výsledek provedení všech těchto příkazů:



![nmap-image](assets/fr/58.webp)



importovat skenování Nmap ve formátu XML do databáze Metasploitu



Zde vidíte, že každý hostitel je importován spolu se svými službami. Tato data lze pak zobrazit příkazem `services` nebo `services -p <port>` pro konkrétní službu:



![nmap-image](assets/fr/59.webp)



seznam služeb importovaných ze souboru XML do databáze Metasploitu



Nakonec můžeme tato data snadno a rychle znovu použít v modulu díky volbě `-R`, která "převede" seznam služeb získaný jako vstup pro direktivu `RHOSTS`, která slouží k určení cílů prováděného útoku. Zde je příklad s modulem `ssh_login`, který umožňuje provést útok hrubou silou na služby [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



použít volbu `services -R` pro import služeb zadaných jako cíl útoku



Toto je jen malý příklad toho, co lze s daty Nmap v Metasploitu dělat, ale dává vám malou představu o tom, jak rychle a snadno lze tyto informace znovu použít v rámci penetračního testu, skenování zranitelností nebo kybernetického útoku. Za zmínku také stojí, že Nmap lze spustit přímo z Metasploitu a importovat výsledky do databáze (příkaz `db_nmap`), což je další zajímavé téma, kterému se budeme věnovat!



### III. Použití Nmap s webovým skenerem Aquatone



Druhým nástrojem, který bych rád představil v této části věnované opětovnému využití výsledků Nmapu pro ofenzivní analýzu zabezpečení a zranitelností, je Aquatone.



Aquatone je webový skener určený k efektivnímu prozkoumávání webových aplikací v síti. Nabízí pokročilé funkce pro zjišťování webových služeb, identifikaci subdomén, analýzu portů a fingerprinting webových aplikací. Vše je přehledně a stručně prezentováno v HTML, JSON a textových zprávách pro snadnou analýzu zabezpečení webu.



Stejně jako Metasploit dokáže Aquatone přímo zpracovat formát XML aplikace Nmap a použít jej jako cíl pro skenování. Ze všech dat, která může zpráva Nmap obsahovat, dokáže extrahovat pouze hostitele a služby, které jsou předmětem zájmu (webové služby).





- Odkaz na nástroj: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




Chcete-li použít výstup XML aplikace Nmap s aplikací Aquatone, jednoduše odešlete soubor XML v rouře, kterou bude aplikace Aquatone využívat. Zde je příklad:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Pokud Aquatone běžně provádí zjišťování portů na hostitelích za účelem nalezení webových služeb, v tomto kontextu se bude spoléhat pouze na výsledky Nmapu, který tuto operaci již provedl, čímž ušetří čas:



![nmap-image](assets/fr/61.webp)



použití výsledků Nmap ve formátu XML s `aquatone`._



Pro informaci uvádíme výtah ze zprávy společnosti Aquatone:



![nmap-image](assets/fr/62.webp)



příklad zprávy `aquatone`



Osobně často používám Aquatone k získání rychlého přehledu o typech webových stránek v síti, zejména díky funkci snímků obrazovky.



I zde platí, že kompletní zpráva Nmap ve formátu XML šetří čas a usnadňuje její opakované použití v jiném nástroji.



### IV. Závěr



Tyto dva příklady jasně ukazují, že formát XML aplikace Nmap usnadňuje použití jejích výsledků jinými nástroji, protože se jedná o strukturovaný a snadno použitelný datový formát. Existuje mnoho dalších nástrojů, které jsou schopny tyto výsledky zpracovat, například nástroje pro automatické vytváření zpráv, grafické reprezentace nebo složitější proprietární skenery zranitelností.



Samozřejmě můžete také vyvíjet vlastní skripty a nástroje v jazyce Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) nebo v jakémkoli jiném jazyce s knihovnou pro zpracování XML, abyste mohli manipulovat s daty výsledků Nmap a znovu je používat podle vlastního uvážení.



Touto částí končí výukový modul o pokročilejším použití Nmapu, zejména o skenování zranitelností pomocí skriptů NSE.



V další části výukového kurzu se mimo jiné zaměříme na některé další, více technické osvědčené postupy a tipy týkající se konkrétních skenů, které může Nmap provádět. Podíváme se také na možnosti optimalizace výkonu skenování, které jsou užitečné zejména při skenování velkých sítí.




## 11 - Zlepšení výkonu skenování sítě



### I. Prezentace



V této kapitole se dozvíte, jak optimalizovat rychlost skenování sítě pomocí nástroje Nmap pomocí různých specifických možností. Zejména se dozvíme více o vnitřním fungování nástroje Nmap, od správy _timeout_ až po předem uložené konfigurace nástroje.



Nyní, když jsme se dobře seznámili s funkcemi Nmapu, pojďme se seznámit s touto bestií a její silou. Pokud jste někdy nástroj používali ve velkých sítích, pravděpodobně jste si všimli, že některé skenování může trvat dlouho, a to navzdory výkonu nástroje. A to z dobrého důvodu: jednoduchý příkaz `nmap` s několika možnostmi může generate miliony paketů zaměřených na stovky tisíc potenciálních systémů a služeb.



Navíc některé konfigurace síťových zařízení mohou záměrně nastavit nižší rychlost (počet paketů za sekundu) s rizikem odmítnutí vašich paketů nebo zákazu vaší IP adresy Address z bezpečnostních důvodů.



V závislosti na kontextu se může vyplatit pokusit se to vše optimalizovat, jak uvidíme v této kapitole.



V každém případě můžete zkontrolovat výchozí hodnoty parametrů, na které se budeme dívat, a také to, zda byly správně zohledněny volby, které se chystáte použít, pomocí Nmap debug (volba `-d`, kterou jsme viděli v předchozí kapitole):



![nmap-image](assets/fr/63.webp)



zobrazit možnosti časování pomocí volby `-d` Nmap._



### II. Řízení rychlosti skenování Nmap



#### A. Řízení paralelizace



Ve výchozím nastavení používá Nmap pro optimalizaci skenování paralelizaci a všechny parametry, které používá, lze upravit pomocí různých voleb. Případy, kdy je skutečně nutné tyto parametry upravit, jsou však poměrně vzácné, takže se jimi v tomto návodu nebudeme podrobně zabývat:





- `--min-hostgroup/max-hostgroup <size>`: velikost paralelních skupin pro skenování hostitelů.





- `--min-parallelism/max-parallelism <numprobes>`: paralelizace sond.





- `--scan-delay/--max-scan-delay <time>`: nastavuje prodlevu mezi sondami.




Stačí vědět, že existují a lze je použít.



#### B. Řízení počtu paketů za sekundu



Ve výchozím nastavení Nmap sám upravuje počet odesílaných paketů za sekundu podle odezvy sítě. Toto nastavení je však možné vynutit definováním nejvyšší a/nebo minimální hodnoty, kterou se má počet paketů za sekundu řídit. Toto nastavení se provádí pomocí voleb `--min-rate <číslo>` a `--max-rate <číslo>`, kde `číslo` představuje počet paketů za sekundu. Příklad:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Tyto možnosti umožňují upravit rychlost skenování podle vašich konkrétních potřeb, a to buď za účelem urychlení procesu, nebo omezení využívané šířky pásma. Právě druhý případ (omezení rychlosti skenování) vás k těmto možnostem nejspíše přivede, zejména pokud se při používání Nmapu setkáváte s latencí sítě (což je poměrně vzácné).



### III. Správa selhání připojení a časových limitů



Další parametr, se kterým si můžeme pohrát a optimalizovat tak rychlost skenování Nmap (nebo zaručit větší přesnost), se týká _timeout_ a _retry_.



Pro _timeouts_ je to **časový limit bez odpovědi**, po jehož uplynutí Nmap přestane čekat na odpověď a bude považovat službu nebo hostitele za nedostupné. Pro _retry_ je to **počet po sobě jdoucích pokusů o operaci**, které Nmap provede, než bude pokračovat.



Stejně jako v případě paralelizace lze i ve fázi vyhledávání hostitele nebo služby použít správu _timeout_ a _retry_:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: určuje dobu kruhového přenosu Exchange. Tento parametr je opět ve skutečnosti vypočítáván a upravován za běhu během skenování. Je nepravděpodobné, že jej budete potřebovat použít, protože Nmap tuto dobu počítá za běhu podle reakce sítě.





- `--max-retries <číslo>`: omezuje počet opakovaných přenosů paketu během skenování portu. Ve výchozím nastavení může Nmap provést až 10 opakování pro jednu službu, zejména pokud zjistí latence nebo ztráty na úrovni sítě, ale ve většině případů se provádí pouze jedno.





- `--host-timeout <time>`: určuje maximální dobu, kterou Nmap stráví na hostiteli při všech svých operacích, včetně skenování portů, detekce služeb a dalších operací souvisejících s tímto hostitelem. Pokud je tento časový interval překročen bez jakékoliv odezvy nebo **ukončení operací**, Nmap tohoto hostitele opustí bez zobrazení jakýchkoliv výsledků týkajících se tohoto hostitele a přejde na dalšího v seznamu. To vám umožňuje kontrolovat maximální dobu, kterou Nmap stráví na daném hostiteli, čímž se vyhnete zaseknutí na nepoddajných hostitelích a optimalizujete celkovou dobu skenování.




Při každodenní práci používám k optimalizaci skenování volby `--max-retries` a `--host-timeout`:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Tyto parametry nabízejí další flexibilitu pro přizpůsobení chování skenování konkrétním potřebám a podmínkám sítě. Je však třeba si uvědomit jejich důsledky z hlediska zatížení skenovaných hostitelů a možné ztráty přesnosti.



### IV. Použití připravených konfigurací



Různé možnosti, se kterými jsme se seznámili v této kapitole, lze použít samostatně nebo jako součást hotových konfigurací, které nabízí Nmap. Volba, která umožňuje použití těchto _šablon_ (šablon konfigurace), je `-T <číslo>` nebo `-T <název>`. Existuje 5 použitelných úrovní _šablon_:



```
-T<0-5>: Set timing template (higher is faster)
```



Ve výchozím nastavení používá Nmap _šablonu_ 3 (_normální_), která je obecně dostačující.



Pokud jde o mě, většinou se pohybuji v situacích, kdy potřebuji být poměrně rychlý (a zároveň co nejúplnější), a často používám možnost `-T4`.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Zde jsou informace o ladění tohoto skenování:



![nmap-image](assets/fr/64.webp)



použití nastavení `-T4` během skenování Nmap



### V. Závěr



V této kapitole jsme se zabývali různými technikami a možnostmi, které můžete použít ke správě výkonu, agresivity a výkonnosti Nmapu. Tyto možnosti jsou užitečné zejména při skenování rozsáhlých sítí a vzácněji i pro účely utajení.



V příští kapitole se podíváme na několik osvědčených postupů pro používání Nmapu a zajištění jeho bezpečnosti.




## 12 - Bezpečnost a důvěrnost dat při používání mapy Nmap



### I. Prezentace



V této kapitole se podíváme na řadu osvědčených postupů, které je třeba přijmout s ohledem na bezpečnost a především důvěrnost dat vytvářených, zpracovávaných a ukládaných v systému Nmap.



Použití Nmap v rámci informačního systému lze rychle zařadit do kategorie útočných akcí. V důsledku toho je třeba přijmout řadu opatření, aby bylo možné jednat v právním rámci a zároveň zaručit bezpečnost zamýšlených cílů, shromážděných dat a systému použitého pro skenování.



### II. Získání příslušných povolení



Před skenováním sítě nebo systému se ujistěte, že jste získali příslušná oprávnění. Skenování systémů na zranitelnosti (skripty NSE) bez oprávnění může být nezákonné a může mít právní důsledky, zejména pokud bezpečnost informačních systémů není součástí vaší oficiální kompetence.





- Pro připomenutí: [Trestní zákoník: Kapitola III: Útoky na systémy automatizovaného zpracování dat](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Ochrana citlivých údajů



Výsledky vytvořené nástrojem Nmap lze považovat za citlivé, zejména pokud obsahují informace o slabých místech informačního systému, které by mohl útočník zneužít. Ale také tehdy, pokud se týkají systémů, které nejsou přístupné každému (např. citlivé, průmyslové, zdravotnické nebo [záložní] informační systémy (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



Viděli jsme také, že v závislosti na použitých skriptech NSE mohou výsledky skenování NSE [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) obsahovat také identifikátory.



Záškodník, kterému se podaří získat přístup k těmto výsledkům skenování, tak bude mít k dispozici mapu informačního systému a množství technických informací, aniž by tyto činnosti sám provedl a riskoval, že bude odhalen.



Proto je důležité dbát na to, abyste při používání aplikace Nmap nevhodně neshromažďovali nebo neukládali citlivé informace, mimo jiné:





- Šifrování výstupních dat: Pokud potřebujete ukládat nebo přenášet výsledky skenování Nmap, nezapomeňte je zašifrovat, abyste ochránili důvěrnost dat. Zabráníte tak neoprávněnému zachycení citlivých informací. V ideálním případě by data měla být zašifrována ihned po opuštění systému použitého k provedení skenování (archiv ZIP zašifrovaný silným heslem je velmi dobrý začátek).





- Nastavte řízení přístupu: zajistěte, aby k výsledkům skenování Nmap, které budou uloženy, měly přístup pouze oprávněné osoby. Nastavte vhodné kontroly přístupu, abyste ochránili citlivé informace před neoprávněným přístupem.





- Ostražitost při manipulaci s daty: při přenosu, kopírování nebo zpracování naskenovaných dat dbejte na přísnou kontrolu zabezpečení dat. To znamená: nenechávejte je ležet v adresáři `Download` na pracovní stanici připojené k internetu, nenechávejte je procházet interní aplikací HTTP file Exchange, nenechávejte otevřený Poznámkový blok bez uzamčení pracovní stanice během polední přestávky atd.




### IV. Zvládání agresivních skenů



Jak jsme viděli v tomto návodu, Nmap může být na síťové úrovni velmi obsáhlý. Může také odesílat pakety, které nejsou správně formátovány a které striktně nerespektují strukturu protokolu v síťových rámcích a paketech, které generuje. Všechny tyto činnosti mohou mít dopad na určité systémy a služby, někdy až do té míry, že způsobí nefunkčnost nebo nasycení systémových a síťových prostředků.



Abyste se vyhnuli jakýmkoli incidentům, musíte ovládat chování Nmapu a vědět, jak jej přizpůsobit kontextu, ve kterém je používán, pomocí různých možností popsaných v tomto tutoriálu. Nmap nebudeme nutně používat stejným způsobem v informačním systému obsahujícím průmyslový [hardware](https://www.it-connect.fr/actualites/actu-materiel/) jako v uživatelské síti tvořené systémy Windows chráněnými místní bránou firewall nebo v jádru sítě.



Doufejme, že vás jednotlivé lekce v tomto tutoriálu naučily ovládat a analyzovat chování Nmapu, ale nejlépe se to naučíte praxí. Proto se ujistěte, že jste obeznámeni s možnostmi Nmap, které budete používat.



### V. Ochrana skenovacího systému



V první kapitole jsme viděli, že ve většině případů je třeba spustit Nmap jako `kořenový` nebo místní správce. Je to proto, že provádí síťové operace, někdy na poměrně nízké úrovni, prostřednictvím síťových knihoven, které vyžadují vysoká a riziková oprávnění z hlediska stability systému nebo důvěrnosti jiných aplikací.



Nmap lze proto považovat za citlivou součást systému, na kterém je nainstalován. Ujistěte se, že používáte nejnovější verzi programu Nmap, protože starší verze mohou obsahovat známé bezpečnostní chyby. Používáním aktuální verze můžete minimalizovat rizika spojená s používáním nástroje.



Pokud jste se rozhodli používat Nmap nikoli prostřednictvím relace jako `root`, ale udělením specifických oprávnění privilegovanému uživateli, takže má vše, co potřebuje k používání Nmap (`sudo` nebo _capabilities_), mějte na paměti, že Nmap lze použít jako součást kompletního zvýšení oprávnění:



![nmap-image](assets/fr/65.webp)



povýšení práv Nmapu pomocí `sudo`._



Zde používám příkaz Nmap přes `sudo`, ale to mi umožňuje získat interaktivní shell jako `root` v systému, což nebylo původním cílem.



Je také velmi nevhodné instalovat Nmap do systémů, které nejsou určeny k provádění skenování sítě. Mám na mysli zejména servery nebo pracovní stanice. Jednak by to přidalo potenciální vektor pro zvýšení oprávnění, ale především by to útočníkovi poskytlo bezproblémový přístup k útočnému nástroji.



V neposlední řadě je třeba zajistit širší bezpečnost systému používaného pro skenování, aby se sám nestal vektorem pro vniknutí nebo únik informací. Jako správce systému je lepší používat vyhrazený systém, ideálně s omezenou životností, než vlastní pracovní stanici.



### VI. Závěr



Závěrem bych chtěl říci, že před použitím nástroje Nmap v reálných nebo produkčních podmínkách se ujistěte, že jste jej řádně zvládli, a buďte ostražití při zpracování a správě jeho výsledků. Byla by škoda způsobit škodu, únik dat nebo usnadnit kompromitaci, když je původní přístup zaměřen na zlepšení bezpečnosti vaší společnosti.



## 13 - Skenování portů prostřednictvím protokolu TCP: SYN, Connect a FIN



### I. Prezentace



V této a následující kapitole se blíže podíváme na různé typy skenování TCP, které jsou v Nmapu k dispozici, a začneme těmi nejčastěji používanými: SYN, Connect a FIN.



Jak jste si možná všimli, Nmap nabízí několik možností pro skenování TCP:



![nmap-image](assets/fr/66.webp)



skenovací techniky dostupné v aplikaci Nmap._



Cílem tohoto článku je vysvětlit některé z těchto metod a pomoci vám pochopit jejich rozdíly, výhody a omezení. Uvidíte, že v závislosti na kontextu nebo na tom, co chcete zjistit, je lepší zvolit tu či onu možnost.



### II. Skenování TCP SYN nebo "Half Open scan



Prvním typem skenování TCP, kterému se budeme věnovat, je `TCP SYN Scan`, známý také jako `Half Open Scan`. Pokud si vzpomínáte na skenování sítě, které jsme prováděli po našich prvních skenováních portů, jedná se o typ skenování, který [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) používá ve výchozím nastavení, pokud je spuštěn s právy roota.



Překlad vám pomůže pochopit, jak toto skenování funguje. Ve skutečnosti skenování TCP SYN odešle na každý cílový port paket TCP SYN, což je první paket odeslaný klientem (který žádá o navázání spojení) v rámci známého _Three way handshake_ TCP. Za normálních okolností, pokud je port na cílovém serveru otevřený a běží za ním služba, odešle server zpět paket TCP SYN/ACK, aby potvrdil klientův SYN a inicializoval spojení TCP. Tato odpověď má podobu paketu TCP s příznaky SYN a ACK nastavenými na 1, což nám umožňuje potvrdit, že port je otevřený a vede ke službě.



Na druhou stranu, pokud je port uzavřen, server nám pošle paket `TCP` s příznaky RST a ACK nastavenými na 1, aby ukončil požadavek na připojení, takže budeme vědět, že za tímto portem není aktivní žádná služba:



![nmap-image](assets/fr/67.webp)



tCP SYN Scan diagram chování pro otevřené a uzavřené porty



Abych získal konkrétnější představu o `TCP SYN Scan`, provedl jsem skenování portu TCP/80 na hostiteli, který měl na tomto portu aktivní webový server. Při skenování sítě pomocí programu Wireshark můžeme vidět následující tok (zdroj skenování: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



zachycení sítě během skenování TCP SYN pro otevřený port



Na prvním řádku vidíme, že zdroj skenování odesílá paket TCP hostiteli `10.10.10.203` na portu TCP/80. V tomto paketu TCP je příznak SYN nastaven na hodnotu 1, což znamená, že se jedná o požadavek na inicializaci spojení TCP.



Na druhém řádku pak vidíme, že cíl odpovídá zprávou `TCP SYN/ACK`, což znamená, že souhlasí s inicializací spojení, a tedy s příjmem datových toků na portu TCP/80. Můžeme tedy usoudit, že port TCP/80 je otevřený a že na skenovaném serveru je přítomen webový server.



Náš hostitel pak odešle zpět paket RST, který spojení uzavře, a umožní tak skenovanému hostiteli neudržovat otevřené spojení TCP a nečekat na odpověď. V případě skenování na mnoha portech by neuzavření spojení TCP mohlo vést k odepření služby, protože by se nasytil počet spojení čekajících na odpověď, která může server udržovat (viz [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



V programu Wireshark budete moci zobrazit stav příznaků TCP pro každý provedený test. Ukáže se, zda se jedná o paket SYN, SYN/ACK, ACK atd:



![nmap-image](assets/fr/69.webp)



zobrazit příznaky TCP paketu v programu Wireshark (zde TCP SYN)



Naopak jsem provedl stejný test mezi oběma počítači, ale tentokrát jsem skenoval port TCP/81, na kterém není aktivní žádná služba (zdroj skenování: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



zachycení sítě během skenování TCP SYN pro uzavřený port



Skenovaný hostitel vrátí `TCP RST/ACK` jako odpověď na můj `TCP SYN`, pokud port není otevřený.



Jak již bylo zmíněno, při spuštění Nmapu z privilegovaného terminálu je výchozím režimem TCP SYN Scan, který lze vynutit pomocí volby `-sS` (`scan SYN`):



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




Z důvodu rychlosti se nejčastěji používá kontrola `TCP SYN Scan`. Na druhou stranu se může zdát podezřelé, že klient nedokončí _Three Way Handshake_ (tj. neodešle ACK po SYN/ACK serveru), pokud je pozorován příliš často na serveru nebo ze stejného zdroje v síti. Normální chování klienta po obdržení paketu TCP SYN/ACK v reakci na TCP SYN je totiž odeslání `potvrzení` (ACK) a následné spuštění Exchange. V případě, že klient obdrží paket TCP SYN/ACK, může se stát, že se mu nepodaří odeslat potvrzení (ACK).



Nicméně poskytuje o něco rychlejší skenování, protože se neobtěžuje odesílat ACK pro každou pozitivní odpověď. Výhodou SYN Scan je jeho rychlost, protože na každý skenovaný port je odeslán pouze jeden paket, ovšem za cenu větší šance na detekci.



Kromě toho dokáže skenování TCP SYN zjistit, zda je port filtrován (chráněn) bránou firewall. Ve skutečnosti lze firewall před cílovým hostitelem zjistit podle toho, jak se chová, když obdrží paket TCP SYN na portu, který má chránit. Jednoduše neodpoví. Jak jsme však viděli, v obou případech (otevřený nebo zavřený port) dojde k odpovědi ze strany hostitele. Toto třetí chování odhalí přítomnost brány firewall mezi skenovaným hostitelem a počítačem, na kterém probíhá skenování. Zde je výsledek, který může Nmap vrátit, když je skenovaný port filtrován firewallem:



![nmap-image](assets/fr/71.webp)



zobrazení nmap při skenování filtrovaného portu



Když provedeme zachycení sítě v době skenování, můžeme skutečně vidět, že není poskytnuta žádná odezva:



![nmap-image](assets/fr/72.webp)



zachycení sítě během skenování TCP SYN pro port filtrovaný bránou firewall



Rozdíl mezi uzavřeným a filtrovaným portem je následující: filtrovaný port je port chráněný bránou firewall, zatímco uzavřený port je port, na kterém neběží žádná služba, a který proto nemůže zpracovávat naše pakety TCP. Některé typy skenování TCP, například skenování TCP SYN, jsou schopny zjistit, zda je port filtrován, zatímco jiné typy skenování to nedokážou.



### III. Kontrola připojení TCP nebo úplná kontrola



Druhým typem kontroly TCP je `TCP Connect scan`, známý také jako _Full Open Scan_. Funguje stejně jako skenování TCP SYN, ale tentokrát po kladné odpovědi ze serveru (SYN/ACK) vrací `TCP ACK`. Proto se nazývá `Full Open`, protože spojení je plně otevřeno a iniciováno na každém portu otevřeném během skenování, čímž je respektován protokol TCP _Three Way Handshake_:



![nmap-image](assets/fr/73.webp)



tCP Connect Scan diagram chování pro otevřené a uzavřené porty



Zde je vidět, co se děje v síti během kontroly `TCP Connect` zaměřené na otevřený port:



![nmap-image](assets/fr/74.webp)



sniffing sítě během skenování TCP Connect na otevřený port



Vidíme, že první odeslaný paket TCP je `TCP SYN` odeslaný klientem a server poté odpoví zprávou `TCP SYN/ACK`, což znamená, že port je otevřený a je na něm aktivní služba. Aby Nmap simuloval legitimního klienta po celé délce, pošle poté serveru zpět `TCP ACK`. Naopak při skenování uzavřeného portu:



![nmap-image](assets/fr/75.webp)



zachycení sítě během skenování TCP Connect pro uzavřený port



Všimněte si, že odpovědí serveru na náš paket `SYN` je opět paket `TCP RST/ACK`, takže můžeme usoudit, že port je uzavřen a nejsou na něm spuštěny žádné služby.



Při použití nástroje Nmap se k provedení kontroly připojení TCP používá volba `-sT` (`skenovat připojení`). Vezměte prosím na vědomí, že pokud je Nmap používán z neprivilegované relace, jedná se o výchozí režim skenování TCP:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



Funkce `TCP Connect Scan` simuluje legitimnější požadavek na připojení, jehož chování se nejvíce podobá chování klienta lambda, takže je obtížnější odhalit skenování na sníženém počtu portů. Je však pomalejší, protože kompletně inicializuje každé TCP spojení na otevřených portech skenovaného počítače.



Pokud jsou nainstalovány služby detekce a ochrany proti narušení sítě (IDS, IPS, EDR), lze snadno odhalit i skenování 10 000 portů pomocí Nmap. Pokud chce útočník zůstat nenápadný, zaměří se spíše na malý počet strategicky vybraných portů, například 445 (SMB) nebo 80 (HTTP), které jsou na serverech často otevřené a představují běžnou zranitelnost.



Vzhledem k tomu, že funkce TCP Connect Scan v obou případech očekává odpověď, může také zjistit přítomnost brány firewall, která může filtrovat porty na cílovém hostiteli.



### IV. Skenování TCP FIN nebo "Stealth Scan



Funkce `TCP FIN Scan`, známá také jako _Stealth Scan_, využívá chování klienta ukončujícího připojení TCP k detekci otevřeného portu.



V protokolu TCP znamená ukončení relace odeslání paketu TCP s příznakem FIN nastaveným na hodnotu 1. V normálním případě Exchange server ukončí veškerou komunikaci s klientem (žádná odpověď). Pokud server nemá aktivní spojení TCP s klientem, odešle `RST/ACK`. Můžeme tedy rozlišovat mezi otevřenými a uzavřenými porty zasíláním paketů `TCP FIN` na sadu portů:



![nmap-image](assets/fr/76.webp)



diagram chování skenování tCP FIN pro otevřené a zavřené porty



Znovu jsem zachytil síť během _Stealth scan_ a toto je to, co vidíte, když je skenovaný port otevřený:



![nmap-image](assets/fr/77.webp)



zachycení sítě během skenování TCP FIN pro otevřený port



Vidíme, že klient odešle jeden nebo dva pakety pro ukončení spojení TCP a server neodpoví. Jednoduše přijme ukončení spojení a přestane komunikovat.



Při skenování uzavřeného portu se nyní zobrazí následující informace:



![nmap-image](assets/fr/78.webp)



zachycení sítě během skenování TCP FIN pro uzavřený port



Vidíme, že server odesílá zpět paket `TCP RST/ACK`, takže existuje rozdíl v chování mezi otevřeným a uzavřeným portem, a jsme schopni vypsat otevřené porty na serveru odesláním paketu TCP FIN. Pomocí nástroje Nmap se k provedení skenování TCP FIN používá volba `-sF` (`scan FIN`):



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



Funkce TCP FIN Scan nefunguje na hostitelích se systémem Windows, protože operační systém má tendenci ignorovat pakety TCP FIN, pokud jsou odesílány na porty, které nejsou otevřené. Pokud tedy spustíte TCP FIN Scan na hostiteli se systémem Windows, budete mít dojem, že jsou všechny porty zavřené.



Proto je důležité znát několik metod skenování a pochopit rozdíly mezi nimi.



Protože v obou případech nebude protokol TCP FIN čekat na odpověď, nebude schopen zjistit přítomnost brány firewall mezi cílovým hostitelem a zdrojem skenování.



Zde je příklad výsledku skenování TCP FIN v programu Nmap:



![nmap-image](assets/fr/79.webp)



výsledky skenování TCP FIN pomocí Nmap._



Neodpověď hostitele na daném portu může znamenat, že je port filtrován, ale také, že je otevřený a aktivní.



Toto skenování se označuje jako "stealth", protože neprovádí generate velký provoz a zpravidla nezpůsobuje přihlašování v cílových systémech. Lze jej použít k diskrétnímu zjišťování portů v síti, aniž by vyvolal poplach. Jak však bylo uvedeno výše, jeho účinnost se může lišit v závislosti na cílovém systému, stejně jako jeho diskrétnost v závislosti na konfiguraci bezpečnostního zařízení.



### V. Závěr



Tolik k první ze dvou kapitol o různých typech skenování TCP, které nabízí Nmap! V příští kapitole se podíváme na typy skenování TCP XMAS, Null a ACK, které fungují různými způsoby při zjišťování otevřených portů na hostiteli.





## 14 - Skenování portů přes TCP: XMAS, Null a ACK



### I. Prezentace



V této části budeme pokračovat ve zkoumání různých metod skenování TCP, které nabízí Nmap. Zde se podíváme na metody `XMAS`, `Null` a `ACK`, které využívají specifické funkce TCP k získání informací o portech a službách otevřených na daném cíli.



### II. Skenování TCP XMAS



XMAS Scan TCP je trochu neobvyklý v tom, že vůbec nesimuluje běžné chování uživatele nebo počítače v síti. Ve skutečnosti XMAS Scan odesílá pakety TCP s příznaky `URG` (Urgent), `PSH` (Push) a `FIN` (Finish) nastavenými na 1, aby obešel některé firewally nebo filtrační mechanismy.



Název XMAS vychází ze skutečnosti, že vidět tyto vlajky je neobvyklé. Když jsou v paketu TCP nastaveny všechny tři příznaky současně, vypadá to jako rozsvícený vánoční stromek:



![nmap-image](assets/fr/80.webp)



příznaky tCP používané při skenování XMAS



Aniž bychom se zde podrobně zabývali úlohou těchto příznaků, je důležité vědět, že při odeslání paketu s těmito třemi příznaky aktivní služba za cílovým portem nevrátí žádné pakety. Naopak pokud je port uzavřen, obdržíme paket TCP RST/ACK. Nyní budeme schopni rozlišit chování otevřeného a uzavřeného portu při výpisu portů na počítači:



![nmap-image](assets/fr/81.webp)



tCP XMAS Scan diagram chování pro otevřené a uzavřené porty



Při skenování sítě na portu TCP/80 hostitele s aktivním webovým serverem se při zjištění otevřeného portu (zdroj skenování `10.10.14.84`) stále postupuje podle stejné logiky:



![nmap-image](assets/fr/82.webp)



zachycení sítě během skenování TCP XMAS pro otevřený port



Vidíme, že zdroj skenování odešle dva pakety TCP XMAS (s příznaky `FIN`, `PSH` a `URG` nastavenými na 1) na hostitele `10.10.10.203` a že cíl se nevrátí, což znamená, že port je otevřený. Naopak při provedení `TCP XMAS Scan` na uzavřeném portu je pozorován následující výsledek:



![nmap-image](assets/fr/83.webp)



zachycení sítě během skenování protokolu TCP XMAS pro uzavřený port



Odpovědí na náš paket TCP je pak `TCP RST/ACK`, což znamená, že port je uzavřen. Chcete-li tuto techniku použít v programu Nmap, můžete pomocí volby `-sX` (`scan XMAS`) provést skenování TCP XMAS:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



Je důležité poznamenat, že skenování TCP XMAS není schopno detekovat firewally, které mohou být mezi cílem a skenovaným počítačem, na rozdíl od některých jiných typů skenování, jako je TCP SYN nebo Connect. Aktivní brána firewall mezi oběma hostiteli totiž zajistí, že nedojde k návratu protokolu TCP, pokud je cílový port filtrován (tj. chráněn bránou firewall). V případě neodpovědi proto nelze zjistit, zda je port chráněn bránou firewall, nebo zda je otevřený a aktivní. Měli byste si také uvědomit, že podobně jako u kontroly TCP FIN mohou některé aplikace nebo operační systémy, například Windows, zkreslit výsledky tohoto typu kontroly.



poznámka: podpora skenování XMAS/FIN/NULL v posledních verzích systému Windows je stále omezená a výsledky mohou být u tohoto typu cíle nekonzistentní. (Aktualizace 2025)_



### III. Skenování TCP Null



Na rozdíl od skenování TCP XMAS bude skenování TCP Null odesílat pakety TCP se všemi příznaky nastavenými na 0. I toto chování se nikdy nevyskytuje v běžném protokolu Exchange mezi počítači, protože odesílání paketů TCP bez příznaku není specifikováno v RFC popisujícím protokol TCP. Proto jej lze snadněji odhalit.



Stejně jako skenování TCP XMAS může toto skenování narušit některé brány firewall nebo filtrovací moduly a umožnit průchod paketů:



![nmap-image](assets/fr/84.webp)



tCP Null Scan diagram chování pro otevřené a uzavřené porty



Zde je zobrazeno, co lze vidět v síti během skenování TCP Null na otevřeném portu:



![nmap-image](assets/fr/85.webp)



zachycení sítě během skenování TCP Null pro otevřený port



Skenovací zařízení odešle bezpříznakový paket (`[<None>]` v programu Wireshark) bez odpovědi ze serveru. Naopak, když je cílový port uzavřen:



![nmap-image](assets/fr/86.webp)



zachycení sítě během skenování TCP Null pro uzavřený port



Chcete-li provést skenování protokolu TCP Null pomocí nástroje Nmap, jednoduše použijte volbu `-sN` (`scan Null`):



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Vzhledem k tomu, že odezva při otevřeném portu a při aktivní bráně firewall (v obou případech není na serveru žádná zpětná vazba) je totožná, není skenování TCP Null schopno zjistit přítomnost brány firewall. A co víc, brána firewall může dokonce zfalšovat výsledek tím, že naznačuje, že port je otevřený, protože neodpovídá na pakety TCP bez příznaků, přestože je port filtrován. To je důležitá informace, kterou je třeba si uvědomit při používání skenů, které nejsou schopny rozlišit mezi otevřeným a filtrovaným (firewallem chráněným) portem, jako jsou například skeny `TCP Null`, `XMAS` nebo `FIN`, aby interpretace získaných výsledků zůstala konzistentní.



### IV. Skenování TCP ACK



Kontrola TCP ACK se používá ke zjištění přítomnosti brány firewall na cílovém hostiteli nebo mezi cílem a zdrojem kontroly.



Na rozdíl od jiných skenů se skenování TCP ACK nesnaží zjistit, které porty jsou na hostiteli otevřené, ale spíše to, zda je aktivní systém filtrování, a pro každý port odpovídá slovy `filtered` nebo `unfiltered`. Některé skeny TCP, jako například `TCP SYN` nebo `TCP Connect`, mohou provádět obojí současně, zatímco jiné, jako například `TCP FIN` nebo `TCP XMAS`, nedokáží určit přítomnost filtrování vůbec. Proto může být užitečná kontrola TCP ACK:



![nmap-image](assets/fr/87.webp)



tCP ACK Scan diagram chování pro filtrované a nefiltrované porty



Pro tento typ skenování použijeme volbu `-sA` programu Nmap. Zde je výsledek skenování TCP ACK, pokud je port filtrován, tj. blokován a chráněn firewallem:



![nmap-image](assets/fr/88.webp)



zobrazení nmap během TCP ACK Scan._



Příklad výsledku pro hostitele s bránou firewall a bez ní. Nmap vrátí `filtered` na portech TCP/80 a TCP/81 hostitele `10.10.10.203`. Při analýze sítě pomocí programu Wireshark je chování následující:



![nmap-image](assets/fr/89.webp)



zachycení sítě během skenování TCP ACK pro port, který není filtrován bránou firewall



Cílový počítač nevrátí nic, pokud je přítomna brána firewall.



Chcete-li spustit toto skenování pomocí Nmap, použijte volbu `-sA` (`scan ACK`):



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Závěr



Kromě již představených metod skenování prostřednictvím protokolu TCP jsme se zabývali třemi různými metodami. Tyto různé metody se mají používat za velmi specifických podmínek a v určitých souvislostech, zejména v rámci penetračních testů nebo operací červených týmů, při nichž se uplatňuje pojem diskrétnosti.



## 15 - Nmap CheatSheet - Souhrn výukových příkazů



### I. Prezentace



Zde je stručný přehled mnoha příkazů a případů použití Nmapu, abyste je mohli rychle najít a znovu použít při každodenním používání.



### II. Nmap: Nmap: CheatSheet IT-Connect



Zde je přehled příkazů, které jsou zde uvedeny. Tato stránka usnadňuje nalezení nejčastějších způsobů použití Nmap.





- Skenování přístavu




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Zjištění aktivních hostitelů




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



poznámka: Volba `-sP` je již několik let zastaralá a měla by být nahrazena volbou `-sn`. (Aktualizace 2025)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Detekce verze




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- Skripty NSE: hledání zranitelností




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Správa výstupu Nmap




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Optimalizace výkonu




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- Typy skenování TCP




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Doufám, že pro vás budou tyto příkazy užitečné. Nezapomeňte přizpůsobit cíl skenování svému kontextu a nahlédnout do oficiální dokumentace, abyste si plně osvojili prováděné testy.



### III. Závěr



Výukový kurz Nmap je nyní dokončen. Nyní máte k dispozici základy, které potřebujete k používání tohoto komplexního a výkonného nástroje. Před použitím v produkčním prostředí vám důrazně doporučujeme procvičit se v kontrolovaných prostředích (Hack The Box, VulnHub, virtuální počítače).



Vnitřní fungování nástroje a jeho pokročilé funkce je třeba ještě hodně prozkoumat. Zvládnutí zde uvedených příkazů a konceptů vám však umožní používat Nmap s jistotou a relevantně.