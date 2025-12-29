---
name: Matrice
description: Průvodce porozuměním, konfigurací a používáním Matrixu, bezpečné, otevřené a decentralizované komunikační platformy.
---

![cover](assets/cover.webp)



## Co je Matrix?



Matrix je **decentralizovaný komunikační protokol** navržený tak, aby umožňoval výměnu zpráv, souborů a audio/video hovorů mezi uživateli a aplikacemi bez závislosti na centrálním podniku. Na rozdíl od tradičních platforem pro zasílání zpráv je Matrix **otevřenou infrastrukturou**, srovnatelnou s elektronickou poštou: každý si může vybrat server nebo jej sám provozovat, přičemž si zachovává možnost výměny se zbytkem sítě.



Matrix se vyznačuje třemi základními principy:



### Protokol, ne aplikace



Matrix není aplikace jako WhatsApp nebo Telegram.


Jedná se o standardizovaný jazyk, který může používat mnoho aplikací.


Jinými slovy, široká škála softwaru Element, FluffyChat, Cinny, Nheko a další poskytují přístup ke stejné síti Matrix.



To zaručuje naprostou svobodu: změna aplikace bez ztráty kontaktů, rozmanitost rozhraní, nezávislost na jediném dodavateli.



![capture](assets/fr/03.webp)



### Decentralizovaná, sdružená síť



Struktura Matrixu je založena na **federaci**, modelu, ve kterém spolupracuje několik nezávislých serverů.


Každý server (nazývaný _homeserver_) může hostit uživatele, chatovací místnosti a synchronizovat zprávy s ostatními servery v síti.


Tedy :





- celý systém neřídí jediný subjekt;
- server může zmizet, aniž by to mělo vliv na zbytek sítě;
- každá organizace nebo jednotlivec může spravovat svůj vlastní prostor.



Tento model zajišťuje **vysokou odolnost** a odráží hodnoty technologické suverenity.



![capture](assets/fr/03.webp)



### Bezpečný, šifrovaný systém



Matrix podporuje **konečné šifrování (E2EE)** pro soukromé výměny a šifrované skupiny.


Zprávy mohou číst pouze účastníci, nikoli zprostředkující servery.


Tento přístup umožňuje komunikovat, aniž by byl obsah výměn vystaven třetí straně, a zároveň zachovává transparentnost protokolu a možnost hostování vlastního serveru.



![capture](assets/fr/05.webp)



### Jedinečná interoperabilita



Jednou z hlavních předností systému Matrix je jeho schopnost fungovat jako **most mezi různými komunikačními systémy**. Díky _mostům_ je možné propojit :





- Telegram
- WhatsApp
- Signal
- Messenger
- Slack
- Discord
- IRC, XMPP atd.



To umožňuje sjednotit komunity rozptýlené na několika platformách a zároveň si zachovat kontrolu nad infrastrukturou.



![capture](assets/fr/06.webp)



## Jak Matrix funguje?



Tato část představuje vnitřní strukturu sítě Matrix, aby bylo možné pochopit, jak uživatelé, servery a aplikace v tomto decentralizovaném ekosystému interagují. Matrix je založen na třech základních prvcích: _homeservery_, identity a _klienti_ sloužící ke komunikaci.



### Servery: homeservery



Matrix běží na nezávislých serverech zvaných _homeservery_.


Každý homeserver spravuje :





- uživatelské účty, které hostí,
- soukromé konverzace a salonky, kterých se tito uživatelé účastní,
- synchronizace s ostatními síťovými servery.



Všechny domácí servery připojené k síti Matrix si automaticky vyměňují zprávy a události ze sdílených obytných místností. Například:





- uživatel registrovaný na serveru A může chatovat s uživatelem na serveru B,
- salon může být rozprostřen na desítky serverů,
- nikdo nemá kontrolu nad salonem nebo komunitou jako celkem.



Tento model je vysoce odolný a umožňuje každé organizaci nebo jednotlivci spravovat vlastní infrastrukturu.



### Identifikátory matic



Každý uživatel má jedinečný identifikátor, který se nazývá **MXID** (_Matrix ID_) a vypadá jako adresa:



```bash
@nomdutilisateur:serveur.xyz
```



Skládá se z :





- uživatelské jméno, před kterým je **@**
- název serveru, na kterém byl účet vytvořen, před kterým je uveden znak **:**



Příklady:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



Tento identifikátor umožňuje komunikaci s jakýmkoli jiným uživatelem služby Matrix bez ohledu na server, ze kterého pochází.



### Klienti Matrix (aplikace)



Chcete-li používat Matrix, musíte se připojit k aplikaci nazvané **klient Matrix**.



Mezi nejznámější patří :





- Element (web, mobil, desktop)
- FluffyChat (mobilní telefon)
- Cinny (minimalistický web/desktop)
- Nheko (stolní počítač)



Tyto aplikace jsou pouze rozhraním pro :





- pro zobrazení zpráv,
- posílat text, obrázky nebo soubory,
- připojit se k veletrhům nebo je vytvořit,
- uskutečňovat audio/video hovory.



Všechny aplikace komunikují se servery prostřednictvím stejného standardizovaného protokolu.



### Pokoje a soukromé zprávy (DM)



V systému Matrix probíhají výměny v **pokojích** :





- místnost může být veřejná nebo soukromá
- pojme dvě osoby nebo tisíce lidí
- může být sdílena mezi několika servery
- má jedinečný identifikátor začínající na **!**



Soukromé zprávy jsou jednoduše chatovací místnosti se dvěma účastníky, často označované jako **DM (Direct Messages)**.



Synchronizace salonu probíhá v reálném čase mezi zúčastněnými servery, což zajišťuje bezproblémový provoz při zachování decentralizace.



## Proč používat Matrix?



Matrix není jen alternativou k centralizovaným systémům zasílání zpráv: je to technologie, která splňuje skutečné potřeby v oblasti digitální suverenity, bezpečnosti a interoperability. Existuje mnoho důvodů, proč si tento protokol ke komunikaci vybírá stále více lidí, firem a institucí.



### Získejte zpět kontrolu nad svou komunikací



Většina platforem pro zasílání zpráv funguje na základě centralizovaného modelu: jediný hráč řídí servery, přístup, data a pravidla používání. Tento model znamená naprostou závislost na dodavateli.


Společnost Matrix k tomu přistupuje jinak.


Každý si může zvolit, kde bude hostovat svůj účet, nebo dokonce umístit svůj vlastní server. Žádný subjekt není v pozici, kdy by mohl uživatele zablokovat, požadovat rušivou identifikaci nebo nařídit změnu zásad.


Tato architektura vrací autonomii jednotlivcům i organizacím. Komunikace již není založena na důvěře ve společnost, ale na otevřeném, zdokumentovaném a ověřitelném protokolu.



### Zabezpečená, šifrovaná komunikace



Matrix podporuje koncové šifrování pro soukromé konverzace a skupiny. Tento mechanismus zajišťuje, že zprávy mohou číst pouze účastníci, i když procházejí přes servery třetích stran ve federaci.



Protokol používá algoritmus Megolm/Olm, který byl navržen speciálně pro zajištění silného zabezpečení v distribuovaném prostředí s více zařízeními.



To umožňuje :





- chránit citlivé rozhovory,
- zabránit neoprávněnému přístupu (i z hostitelského serveru),
- dlouhodobě zachovávat důvěrnost.



Šifrování není volitelná možnost: je to základní součást protokolu.



### Již nejste závislí na jediné aplikaci



Matrix není aplikace, ale protokol.



Tato rozmanitost zákazníků zaručuje :





- výběr přizpůsobený individuálním potřebám,
- možnost používat Matrix na jakémkoli typu zařízení,
- žádná závislost na jediném softwaru.



Pokud je zákazník nevhodný nebo přestane být veden, stačí vybrat jiného: účet bude nadále normálně fungovat.



### Sdružování a propojování různých komunit



Federace umožňuje, aby různé servery pracovaly společně a zároveň byly spravovány nezávisle.


Tedy :





- organizace může spravovat vlastní homeserver,
- jednotlivci se mohou připojit k veřejným serverům,
- všichni mohou vzájemně komunikovat, jako by byli na stejné platformě.



Tato flexibilita umožňuje vytvářet komunikační prostory přizpůsobené všem potřebám: týmům, sdružením, komunitám, institucím nebo projektům s otevřeným zdrojovým kódem.



Matrix je oblíbený zejména v technických kruzích, aktivistických kolektivech, výzkumných pracovištích, vládách a stále častěji i v komunitách Bitcoin.



### Jedinečná interoperabilita v oblasti zasílání zpráv



Jednou z hlavních předností systému Matrix je jeho schopnost **rozšiřovat** výměny díky můstkům schopným propojit :





- WhatsApp
- Telegram
- Signal
- Slack
- Discord
- IRC
- XMPP
- a mnoho dalších platforem



Matrix se tak stává jednotící vrstvou pro komunikaci, která spojuje několik komunit rozptýlených v různých aplikacích.



Tato interoperabilita snižuje roztříštěnost a zjednodušuje spolupráci.



### Svobodný, otevřený a udržitelný protokol



Protokol Matrix je zcela otevřený a transparentně vyvinutý.


To zaručuje několik výhod:





- průběžný vývoj normy,
- možnost kontroly kódu kýmkoli,
- nezávislost na obchodních nebo politických změnách,
- dlouhodobou odolnost.



Na rozdíl od proprietárních systémů pro zasílání zpráv nezávisí budoucnost Matrixu na jediné společnosti, ale na globální komunitě a otevřeném standardu.



## Jak si mohu vytvořit účet Matrix?



Vytvoření účtu Matrix je jednoduché a nevyžaduje žádné technické dovednosti. Uživatelé se mohou připojit k existujícímu serveru, vytvořit si přihlašovací jméno a okamžitě začít chatovat. V této části jsou popsány základní kroky.



### Výběr serveru (veřejného nebo soukromého)



Matrix je federativní síť: existuje mnoho serverů (homeserverů) spravovaných různými organizacemi, komunitami nebo jednotlivci. Výběr serveru určuje pouze to, kde je účet hostován, ale nebrání komunikaci s celou sítí.


**K dispozici jsou dvě možnosti:**



### - Použití veřejného serveru



To je nejjednodušší řešení.


Příklady oblíbených serverů:





- _matrix.org_ (nejznámější)
- _envs.net_
- tematické komunitní servery (technika, soukromí, open-source...)



Tyto servery jsou vhodné pro začínající uživatele, kteří se chtějí rychle zaregistrovat.



### - Použití soukromého serveru



Ideální pro :





- organizace,
- rodinu,
- projekt s otevřeným zdrojovým kódem,
- pracovní tým,
- nebo pro suverénní, samostatné použití.



V tomto případě musí někdo spravovat server (Synapse, Dendrite, Conduit...).


Bez ohledu na to, který server si vyberete, mohou uživatelé díky federaci komunikovat mezi sebou.



### Vytvoření účtu krok za krokem



Protože je Matrix otevřený protokol, může k němu přistupovat několik aplikací.


Jak bylo popsáno výše, nabízejí různá rozhraní a funkce v závislosti na požadavcích:





- Element**: nejkomplexnější klient dostupný na všech platformách.
- FluffyChat**: jednoduchý, moderní a ideální pro mobilní telefony.
- Nheko**: lehký, ergonomický klient pro PC.
- SchildiChat**: Varianta Element s ergonomickými vylepšeními.
- NeoChat**: integrován do ekosystému KDE.



Volba klienta nemá na účet žádný vliv: všechny fungují s libovolným serverem Matrix.



### Klasické kroky :





- Otevřete vybranou aplikaci. V našem případě to uděláme pomocí [Element](app.element.io).
- Vyberte možnost "Vytvořit účet".



![cover-kali](assets/fr/10.webp)



Pro zjednodušení si můžete vytvořit účet Matrix pomocí **Google, Facebook, Apple, GitHub nebo GitLab**. Tyto služby budou vědět pouze to, že jejich účet byl použit k přístupu do Matrixu: jedná se o tzv. sociální připojení**.



Pro větší důvěrnost se můžete zaregistrovat také ručně výběrem **jména**, **hesla** a **e-mailové adresy**.



V závislosti na zvoleném serveru může být vyžadován **captcha** a souhlas s **podmínkami používání**.



Po ověření registrace je odeslán potvrzovací e-mail.


Stačí kliknout na odkaz pro aktivaci účtu a přístup k webové aplikaci (Element), abyste se mohli zapojit do prvních konverzací Matrixu.



![cover-kali](assets/fr/11.webp)



Nyní máte účet a používáte webovou verzi aplikace Element.



## Přidejte svůj první kontakt



Chcete-li s někým komunikovat v systému Matrix, potřebujete znát pouze jeho úplný identifikátor, který se nazývá **Matrix ID**.



Příklad:



`@alice:matrix.org @bened:monserveur.bj`



### Přidání kontaktu



Chcete-li pozvat přátele do skupinového chatu, klikněte na kolečko `i` v pravém horním rohu. Tím se otevře pravý panel. Klepnutím na "Lidé" zobrazíte seznam členů této místnosti: v tuto chvíli byste měli být přítomni pouze vy.



![cover-kali](assets/fr/12.webp)



Klikněte na "Pozvat do této místnosti" v horní části seznamu lidí a otevře se výzva, abyste mohli pozvat své přátele do Matrixu. Pokud jsou již v Matrixu přihlášeni, zadejte jejich Matrix ID. Pokud nejsou, zadejte jejich e-mailovou adresu a budou pozváni, aby se k nám připojili.



Neexistuje žádný systém "přátel": kontakt je jednoduše osoba, se kterou byla zahájena konverzace.



![cover-kali](assets/fr/13.webp)



Pozvaná osoba může pozvání přijmout nebo odmítnout. Pokud pozvání přijme, měla by se připojit k místnosti. Čím více, tím lépe!



![cover-kali](assets/fr/14.webp)



### Nastavení vlastního serveru



Matrix se skutečně uplatní ve spojení s osobním serverem.


Nasazení vlastního homeserveru vám umožní :





- zachovat úplnou kontrolu nad daty,
- definovat vlastní pravidla používání,
- hostovat více účtů (přátelé, tým, komunita),
- a zajistit maximální odolnost v případě omezení nebo cenzury.



**Dostupná řešení:**





- Synapse**: historicky nejúplnější implementace.
- Dendrite**: lehčí, výkonnější a navržený pro budoucnost protokolu.
- Conduit**: minimalistická varianta, kterou lze snadno nasadit.



**Předpoklady:**





- název domény,
- počítač nebo VPS,
- minimální znalosti správy systému.



I když to vyžaduje trochu konfigurace, správa vlastního serveru dělá z Matrixu suverénní a odolný nástroj.



### Účast na prvních veletrzích



Matrix si velmi zakládá na _pokojích_ (obývacích pokojích).


Konají se zde veřejné, soukromé, komunitní, technické, místní a mezinárodní veletrhy.



**Tři způsoby, jak se připojit k salonu:**



1. **Pomocí odkazu na pozvánku** (často ve formě adresy URL `matrix.to`).


2. **Vyhledání názvu salonu** v aplikaci.


3. **Zadáním celého ID pořadu**, např. :


`#bitcoin:matrix.org`


`#communauté-bénin:monsrv.bj`



Po připojení se chatovací místnost chová jako klasická diskusní skupina, s historií, šifrováním, soubory, reakcemi a audio/video hovory, v závislosti na použitém klientovi.



![capture](assets/fr/09.webp)



## Jak dál



Po zvládnutí základů nabízí Matrix řadu pokročilých možností. Ať už chcete připojit jiné systémy pro zasílání zpráv, hostovat vlastní server nebo organizovat komunitu, ekosystém je velmi bohatý.



### Mosty (WhatsApp, Telegram, Signal atd.)



Most spojuje systém Matrix s jinými systémy pro zasílání zpráv.


Pomocí něj můžete odesílat a přijímat zprávy z :





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Discord
- Slack**
- IRC** (IRC)
- a mnoho dalších



### Co mohou mosty udělat





- Centralizujte všechny své konverzace v systému Matrix
- Poskytnout otevřené rozhraní pro interakci s proprietárními službami
- Správa multiplatformní komunity z jediného místa



Některé mosty jsou oficiální, jiné komunitní.


V závislosti na oddělení mohou vyžadovat :





- osobní server,
- další konfigurace,
- nebo použití stávajícího veřejného mostu.



### Použití Matrixu pro organizaci, komunitu nebo projekt Bitcoin



Matrix není jen osobní nástroj.


Lze jej použít ke strukturování pracovních skupin, organizaci místních komunit nebo řízení projektové komunikace.



**Příklady použití:**





- Komunity s otevřeným zdrojovým kódem
- Projekty Bitcoin a Lightning ecosystem
- Skupiny studentů nebo vývojářů
- Občanské organizace
- Nezávislá média
- Místní skupiny a sdružení



**Proč je to zajímavé?





- 100% open-source** nástroj
- Suverénní a decentralizovaná** komunikace
- Prostory rozdělené do **salónků**, **podskupin**, **soukromých salónků** atd.
- Integrace s Nextcloudem, GitLabem, Mattermostem nebo vlastními roboty
- Vyladěná správa oprávnění a moderování



Matrix se pak stává komunikačním pilířem pro všechny struktury, které chtějí zůstat nezávislé na velkých centralizovaných platformách.



## Závěr



Matrix představuje moderní, otevřené a bezpečné řešení pro komunikaci v reálném čase, které nabízí decentralizovanou alternativu k tradičním platformám. Díky federativní architektuře a pokročilým šifrovacím protokolům umožňuje uživatelům zachovat si kontrolu nad svými daty a zároveň využívat plynulé a interoperabilní prostředí. Ať už pro osobní, profesionální nebo komunitní použití, Matrix nabízí robustní a škálovatelný rámec pro budování komunikačních prostředí přizpůsobených dnešním potřebám.



Chcete-li se dozvědět více a zjistit všechny funkce, které Matrix nabízí, můžete nahlédnout do oficiální dokumentace, která je k dispozici zde :


[https://matrix.org/docs/](https://matrix.org/docs/)