---
name: Zvládnutí BTC Pay Server
goal: Nakonfigurovat instanci BTC Pay Server pro místní podnik
objectives:
- Porozumět základům role BTCPay Serveru při zpracování plateb
- Zvládnout vnitřní fungování procesu konfigurace BTCPay Serveru
- Nasadit BTCPay Server v cloudových a uzlových prostředích
- Stát se operátorem BTC Pay Serveru
---
# Cesta k finanční suverenitě

Důvěra je křehká, zejména když jde o peníze. Tento úvodní kurz vás provede BTCPay Serverem, výkonným nástrojem, který vám umožňuje přijímat platby v Bitcoinu bez spoléhání se na třetí strany. Naučíte se základy toho, jak se stát operátorem BTCPay Serveru

Tento kurz vytvořili Alekos a Bas a upravili melontwist a asi0. Odhaluje, jak jednotlivci a podniky budují alternativy k tradičním platebním systémům. Ať už vás Bitcoin zajímá, nebo jste připraveni provozovat platební infrastrukturu pro podniky, objevíte praktické dovednosti, které zpochybňují status quo. Jste připraveni prozkoumat, jak ve skutečnosti vypadá finanční nezávislost?
+++
# Úvod


<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>


## Přehled kurzů


<chapterId>785ed2bc-94ae-4962-a26a-edf5742a3c72</chapterId>


Vítejte v kurzu POS 305 na serveru BTCPay!


Cílem tohoto školení je naučit vás instalovat, konfigurovat a používat BTCPay Server ve vaší firmě nebo organizaci. BTCPay Server je řešení s otevřeným zdrojovým kódem, které vám umožní zpracovávat platby Bitcoin autonomně, bezpečně a s nízkými náklady. Tento kurz je určen především pokročilým uživatelům, kteří chtějí zvládnout samostatnou integraci BTCPay Serveru do svého každodenního provozu.


**Část 1: Úvod do serveru BTCPay**

Začneme obecným představením serveru BTCPay, včetně přihlašovací obrazovky, správy uživatelských účtů a vytvoření nového obchodu. Tento úvod vám pomůže pochopit BTCPay Server Interface a porozumět základním funkcím potřebným k zahájení používání tohoto nástroje.


**Díl 2: Úvod do zabezpečení klíčů Bitcoin**

Bezpečnost vašich prostředků Bitcoin je velmi důležitá. V této části se budeme zabývat generováním kryptografických klíčů, používáním hardwarových peněženek k zabezpečení těchto klíčů a způsobem interakce s klíči prostřednictvím serveru BTCPay. Dozvíte se také, jak nakonfigurovat BTCPay Server Lightning Wallet, abyste optimalizovali své transakce.


**Část 3: Server BTCPay Interface**

Tato část vás provede uživatelským rozhraním Interface serveru BTCPay. Dozvíte se, jak se pohybovat na ovládacím panelu, konfigurovat nastavení obchodu a serveru, spravovat platby a využívat integrované pluginy. Cílem je poskytnout vám nástroje potřebné k přizpůsobení instalace podle vašich konkrétních potřeb.


**Část 4: Konfigurace serveru BTCPay**

Nakonec se zaměříme na praktickou instalaci BTCPay Serveru v různých prostředích. Ať už používáte LunaNode, Voltage nebo uzel Umbrel, naučíte se základní kroky pro nasazení a konfiguraci BTCPay Serveru s ohledem na specifika jednotlivých prostředí.


Jste připraveni ovládnout server BTCPay a rozvíjet své podnikání? Jdeme na to!


## Kritika ocenila Author's Bitcoin a BTCPay Server


<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>


Začněme tím, co je server BTCPay a jaký je jeho původ. Vážíme si transparentnosti a určitých standardů, které vytvářejí důvěru v prostoru Bitcoin.

Projekt v tomto prostoru tyto hodnoty porušil. Hlavní vývojář serveru BTCPay, Nicolas Dorier, to vzal osobně a slíbil, že je zastará. A jsme tady, o mnoho let později, a na této budoucnosti, plně open-source, pracujeme každý den.


> Tohle je lež, moje důvěra v tebe je narušena, nechám tě zastarat.
> Nicolas Dorier

Po Nicolasových slovech nastal čas začít stavět. Na tom, čemu nyní říkáme BTCPay Server, bylo odvedeno značné množství práce. K tomuto úsilí chtělo přispět více lidí. Mezi nejznámější patří r0ckstardev, MrKukks, Pavlenex a první obchodník, který software používal, astupidmoose.


Co znamená open source a co je součástí takového projektu?


FOSS je zkratka pro Free & Open-Source Software. První z nich označuje podmínky, které umožňují komukoli kopírovat, upravovat a dokonce šířit verze softwaru (i za účelem zisku). Druhý termín označuje otevřené sdílení zdrojového kódu a podporuje veřejnost v jeho přispívání a vylepšování.

To přitahuje zkušené uživatele, kteří s nadšením přispívají k softwaru, který již používají a z něhož mají užitek, což se v konečném důsledku ukazuje jako úspěšnější způsob přijetí než u proprietárního softwaru. Je to v souladu s étosem Bitcoin, který říká, že "informace touží být zdarma" Sdružuje nadšené lidi, kteří tvoří komunitu, a je jednoduše zábavnější. Stejně jako Bitcoin je FOSS nevyhnutelný.


### Než začneme


Tento kurz se skládá z několika částí. O mnohé z nich se postará váš třídní učitel, prostředí Demo, ke kterému získáte přístup, hostovaný server pro vás a případně i název domény. Pokud tento kurz absolvujete samostatně, počítejte s tím, že prostředí označená jako DEMO nebudete mít k dispozici.

POZN. Pokud tento kurz absolvujete v učebně, mohou se názvy serverů lišit v závislosti na nastavení učebny. Proměnné v názvech serverů se proto mohou lišit.


### Struktura kurzu


Každá kapitola obsahuje cíle a hodnocení znalostí. V tomto kurzu se budeme věnovat každému z nich a na konci každého bloku lekcí (tj. kapitoly) uvedeme shrnutí klíčových prvků. Ilustrace jsou uváděny za účelem poskytnutí vizuální zpětné vazby a posílení klíčových pojmů po vizuální stránce. Na začátku každého bloku lekcí jsou stanoveny cíle. Tyto cíle přesahují rámec kontrolního seznamu. Poskytují návod k osvojení nového souboru dovedností. Hodnocení znalostí jsou postupně náročnější, protože nastavení serveru BTCPay je kompletní.


### Co studenti v rámci kurzu obdrží?


V kurzu BTCPay Server může student pochopit základní technické i netechnické principy Bitcoin. Rozsáhlé školení v používání Bitcoin prostřednictvím BTCPay Serveru umožní studentům provozovat vlastní infrastrukturu Bitcoin.


### Důležité webové adresy nebo možnosti kontaktu


Nadace BTCPay Server Foundation, která Alekosovi a Basovi umožnila tento kurz napsat, sídlí v japonském Tokiu. Nadaci BTCPay Server lze kontaktovat prostřednictvím uvedených webových stránek.



- https://foundation.btcpayserver.org
- Připojte se k oficiálním chatovacím kanálům: https://chat.btcpayserver.org


## Úvod do Bitcoin


<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>


### Porozumění Bitcoin prostřednictvím cvičení ve třídě


Jedná se o cvičení ve třídě, takže pokud tento kurz absolvujete sami, nemůžete ho provést, ale přesto si můžete toto cvičení projít. K provedení tohoto úkolu je zapotřebí minimálně 9 až 11 osob.


Cvičení začíná po zhlédnutí úvodního filmu "Jak funguje Bitcoin a Blockchain" od BBC.


:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::


Toto cvičení vyžaduje minimálně devět účastníků. Cílem tohoto cvičení je fyzicky pochopit, jak funguje Bitcoin. Tím, že budete hrát jednotlivé role v síti, získáte interaktivní a hravý způsob učení. Toto cvičení se netýká sítě Lightning Network.


### Příklad: Vyžaduje 9 / 11 osob


Role jsou následující:



- 1 zákazník
- 1 Obchodník
- 7 až 9 uzlů Bitcoin


**Nastavení je následující:**


Zákazníci si v obchodě zakoupí produkt s kódem Bitcoin.


**Scénář 1 - tradiční bankovní systém**



- Nastavení:
  - Viz schémata/vysvětlivky v přiloženém Obrázku - [Schéma činnosti](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Sežeňte tři dobrovolníky z řad studentů, kteří budou hrát role zákazníka (Alice), obchodníka (Bob) a banky.
- Přehrajte sled událostí:
  - Zákazník - prohlíží si obchod online a najde položku za 25 dolarů, kterou chce, a informuje obchodníka, že by si ji rád koupil
  - Obchodník - žádá o platbu.
  - Zákazník - odešle informace o kartě obchodníkovi
  - Obchodník - předá bance informace (identifikující jak jeho vlastní, tak i totožnost/informace) a požádá o úhradu platby
  - Banka shromáždí informace o zákazníkovi a obchodníkovi (Alice a Bob) a zkontroluje, zda je zůstatek zákazníka dostatečný.
  - Odečte z účtu Alice 25 USD, připíše na účet Bob 24 USD, vezme si 1 USD za službu
  - Obchodník obdrží od banky palec nahoru a odešle zboží zákazníkovi.
- Komentáře:
  - Bob a Alice musí mít vztah s bankou.
  - Banka shromažďuje identifikační údaje o Bob i Alice.
  - Banka si bere podíl.
  - Banka musí být vždy pověřena úschovou peněz každého účastníka.


**Scénář 2 - systém Bitcoin**



- Nastavení:
  - Viz schémata/vysvětlivky v přiloženém Obrázku - [Schéma činnosti](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Nahraďte banku devíti studenty, kteří budou hrát roli počítačů (Bitcoin uzlů/minerů) v síti, která nahradí banku.
- Každý z 9 počítačů má kompletní historický záznam všech transakcí, které kdy byly provedeny (tedy přesné zůstatky bez falšování), a také soubor pravidel:
  - Ověření správného podpisu transakce (thekeyfitsthelock)
  - Vysílání a přijímání platných transakcí partnerům v síti, zahazování neplatných transakcí (včetně těch, které se pokoušejí utratit stejné prostředky dvakrát)
- Pravidelně aktualizujte/přidávejte záznamy s novými transakcemi přijatými z "náhodného" počítače, pokud jsou všechny obsahy platné (poznámka: pro zjednodušení prozatím ignorujeme komponentu Proof of Work), jinak je odmítněte a pokračujte jako dříve, dokud další "náhodný" počítač nepošle aktualizaci
  - Správná částka byla odměněna, pokud byl obsah platný.
- Přehrajte sled událostí:
  - Zákazník - prohlíží si obchod online a najde položku za 25 dolarů, kterou chce, a informuje obchodníka, že by si ji rád koupil
  - Obchodník - požádá zákazníka o platbu zasláním Invoice/Address ze svého Wallet.
  - Zákazník vytvoří transakci (odeslání BTC v hodnotě 25 USD na účet Address poskytnutý obchodníkem) a odvysílá ji do sítě Bitcoin.
- Počítače - přijmou transakci a ověří ji:
  - V Address je nejméně 25 dolarů BTC odeslaných z
  - Transakce je řádně podepsána ("odemčena" zákazníkem)
  - Pokud tomu tak není, transakce se po síti nerozšíří, a pokud ano, pak se rozšíří a čeká.
  - Obchodníci mohou zkontrolovat, že transakce čeká na vyřízení.
- Jeden počítač je "náhodně" vybrán, aby navrhl dokončení navrhované transakce odvysíláním "bloku", který ji obsahuje; pokud se potvrdí, obdrží odměnu BTC.
  - VOLITELNĚ/VYLEPŠENO - namísto náhodného výběru počítače simulujte Mining tak, že počítače budou házet kostkami, dokud nedojde k nějakému předem určenému výsledku (např. bude vybrán ten, který jako první hodí dvě šestky)
  - Může také přehrát, co by se stalo, kdyby dva počítače vyhrály přibližně současně, což by vedlo k řetězovému rozdělení.
  - Počítače zkontrolují platnost, aktualizují/přidají záznamy do svých účetních knih, pokud jsou splněna pravidla, a odvysílají blok transakcí rovnocenným partnerům.
  - Náhodně vybraný počítač obdrží odměnu za navržení platného bloku.
  - Transakce s kontrolou obchodníka byla dokončena, tedy byly přijaty finanční prostředky a položka byla odeslána zákazníkovi.
- Komentáře:
  - Všimněte si, že nebylo nutné mít předchozí bankovní vztah.
  - K usnadnění není zapotřebí žádná třetí strana; nahrazuje se kodexem/podněty.
  - Nikdo mimo přímý Exchange nesmí shromažďovat údaje a mezi účastníky musí být vyměněno pouze nezbytné množství (např. přepravní Address).
  - Mezi lidmi (kromě obchodníka, který zboží posílá) není vyžadována žádná důvěra, podobně jako při nákupu v hotovosti.
  - Peníze vlastní přímo fyzické osoby.
  - Bitcoin Ledger je pro zjednodušení zobrazen v dolarech, ale ve skutečnosti se jedná o BTC.
  - Simulujeme vysílání jedné transakce, ale ve skutečnosti v síti probíhá více transakcí a bloky obsahují tisíce transakcí najednou. Uzly také ověřují, zda nejsou v očekávání žádné transakce s dvojím utracením (v tomto případě bych všechny kromě jedné vyřadil).
- Scénáře podvádění:
  - Co kdyby zákazník neměl 25 BTC?
    - Nebyly by schopny transakci vytvořit, protože "odemknutí" a "Ownership" je totéž a počítače kontrolují, zda je transakce řádně podepsaná; jinak ji odmítnou
  - Co když se náhodně vybraný počítač pokusí "změnit Ledger"?
    - Blokování by bylo odmítnuto, protože každý jiný počítač má kompletní historii a všiml by si změny, čímž by porušil jedno ze svých pravidel.
    - Náhodný počítač by nedostal odměnu a žádné transakce z jeho bloku by nebyly dokončeny.


## Hodnocení znalostí


<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>


### KA Diskuse ve třídě


Proberte některá zjednodušení provedená v rámci druhého scénáře ve třídě a podrobněji popište, co dělá skutečný systém Bitcoin.


### KA Přehled slovní zásoby


Definujte následující klíčové pojmy uvedené v předchozí části:



- Uzel
- Mempool
- Obtížnost Cíl
- Blok


**Diskutujte ve skupině o významu některých dalších pojmů:**


Blockchain, Transakce, Dvojité výdaje, Byzantský generálský problém, Mining, Proof of Work (PoW), Hash Funkce, Block reward, Blockchain, Nejdelší řetězec, 51% útok, Výstup, Výstupní zámek, Změna, Satoshis, Veřejný/soukromý klíč, Address, Kryptografie veřejného klíče, Digitální podpis, Wallet


# Představujeme server BTCPay


<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>


## Pochopení přihlašovací obrazovky serveru BTCPay


<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>


### Práce se serverem BTCPay


Cílem tohoto bloku kurzu je získat obecné znalosti o softwaru BTCPay Server. Ve sdíleném prostředí se doporučuje sledovat ukázku instruktora a při sledování postupu spolu s učitelem nahlédnout do učebnice BTCPay Server Coursebook. Naučíte se, jak vytvořit Wallet pomocí několika metod. Příklady zahrnují nastavení Hot Wallet a hardwarové peněženky připojené prostřednictvím trezoru BTCPay Server. Tyto cíle se vyskytují v ukázkovém prostředí, které zobrazuje a ke kterému má přístup váš instruktor kurzu.


Pokud tento kurz sledujete sami, seznam hostitelů třetích stran pro účely ukázky najdete na adrese https://directory.btcpayserver.org/filter/hosts. Důrazně nedoporučujeme používat tyto možnosti třetích stran jako produkční prostředí; slouží však správnému účelu pro seznámení s používáním Bitcoin a BTCPay Serveru.


Jako stážista BTCPay Server Rockstar můžete mít předchozí zkušenosti s nastavením uzlu Bitcoin. Tento kurz je speciálně přizpůsoben softwarovému zásobníku BTCPay Server.


Mnohé z možností BTCPay Serveru existují v té či oné podobě i v jiných programech souvisejících s Bitcoin Wallet.


### Přihlašovací obrazovka serveru BTCPay


Po přivítání v ukázkovém prostředí budete vyzváni k přihlášení nebo vytvoření účtu Správci serveru mohou z bezpečnostních důvodů funkci vytváření nových účtů zakázat. Loga a barvy tlačítek BTCPay Serveru lze měnit, protože BTCPay Server je software s otevřeným zdrojovým kódem. Hostitel třetí strany může software označit bílým štítkem a změnit celý vzhled.


![image](assets/en/001.webp)


### Okno Vytvořit účet


Vytváření účtů na serveru BTCPay vyžaduje platný řetězec Email Address; example@email.com je platný řetězec pro Email.


Heslo musí mít alespoň 8 znaků, včetně písmen, číslic a znaků. Po jednorázovém nastavení hesla je třeba ověřit, zda je heslo stejné jako to, které bylo zadáno do prvního pole pro zadání hesla.


Po správném vyplnění polí E-mail a Heslo klikněte na tlačítko Vytvořit účet. Tím se E-mail a heslo uloží na instanci serveru BTCPay instruktora.


![image](assets/en/002.webp)


**!Poznámka!**


Pokud budete tento kurz absolvovat samostatně, bude vytvoření tohoto účtu pravděpodobně provedeno na hostiteli třetí strany; proto znovu zdůrazňujeme, že by se neměly používat jako produkční prostředí, ale pouze pro účely školení.


### Vytvoření účtu správcem serveru BTCPay


Správce instance serveru BTCPay může také vytvářet účty pro server BTCPay. Správce instance serveru BTCPay může kliknout na "Nastavení serveru" (1), kliknout na záložku "Uživatelé" (2) a kliknout na tlačítko "+ Přidat uživatele" (3) v pravém horním rohu záložky Uživatelé. V cíli (4.3) se dozvíte více o správcovském ovládání účtů.


![image](assets/en/003.webp)


Jako správce budete potřebovat e-mail uživatele Address a nastavíte standardní heslo. Doporučujeme, aby správce informoval uživatele, aby si toto heslo před použitím účtu z bezpečnostních důvodů změnil. Pokud správce heslo nenastaví a na serveru byl nakonfigurován protokol SMTP, uživatel obdrží e-mail s odkazem na pozvánku, aby si vytvořil účet a nastavil heslo sám.


### Příklad


Při sledování kurzu s instruktorem následujte odkaz poskytnutý instruktorem a vytvořte si účet v ukázkovém prostředí. Ujistěte se, že je váš e-mail Address a heslo bezpečně uloženo; tyto přihlašovací údaje budete potřebovat pro zbytek demonstračních cílů v tomto kurzu.


Váš instruktor mohl před tímto cvičením shromáždit e-mail Address a zaslat odkaz s pozvánkou. Pokud jste byli instruováni, zkontrolujte svůj e-mail.


Pokud se kurzu účastníte bez instruktora, vytvořte si účet pomocí demo prostředí serveru BTCPay; přejděte na stránku


https://Mainnet.demo.btcpayserver.org/login.


Tento účet by měl být používán pouze pro demonstrační/školící účely a nikdy ne pro obchodní účely.


### Shrnutí dovedností


V této části jste se dozvěděli následující:



- Jak vytvořit účet na hostovaném serveru prostřednictvím Interface.
- Jak může správce serveru ručně přidávat uživatele v nastavení serveru.


### Hodnocení znalostí


#### Koncepční přezkum KA


Uveďte důvody, proč je použití ukázkového serveru pro produkční účely špatný nápad.


## Správa uživatelských účtů


<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>


### Správa účtu na serveru BTCPay


Poté, co si majitel obchodu vytvoří účet, může jej spravovat v levém dolním rohu uživatelského rozhraní serveru BTCPay. Pod tlačítkem Účet se nachází několik nastavení vyšší úrovně.



- Tmavý/světlý režim.
- Přepínač Skrýt citlivé informace.
- Správa účtu.


![image](assets/en/004.webp)


### Tmavý a světlý režim


Uživatelé serveru BTCPay si mohou vybrat mezi světlou a tmavou verzí uživatelského rozhraní. Stránky určené pro zákazníky se nezmění. Využívají nastavení preferované zákazníkem, pokud jde o tmavý nebo světlý režim.


### Přepínač Skrýt citlivé informace


Tlačítko Skrýt citlivé informace poskytuje rychlé a jednoduché zabezpečení Layer. Kdykoli potřebujete ovládat svůj BTCPay Server, ale přes rameno vám mohou číhat lidé na veřejném prostranství, zapněte funkci Skrýt citlivé informace a všechny hodnoty v BTCPay Serveru budou skryty. Někdo vám může nahlížet přes rameno, ale už neuvidí hodnoty, se kterými pracujete.


### Správa účtu


Po vytvoření uživatelského účtu zde můžete spravovat hesla, 2FA nebo klíče API.


### Správa účtu - Účet


Volitelně můžete svůj účet aktualizovat pomocí jiného e-mailu Address. Abyste se ujistili, že váš e-mail Address je správný, server BTCPay umožňuje zaslat ověřovací e-mail. Pokud uživatel nastaví nový e-mail Address a potvrdí, že ověření proběhlo, klikněte na tlačítko uložit. Uživatelské jméno zůstává stejné jako u předchozího e-mailu.


Uživatel se může rozhodnout odstranit celý svůj účet. To lze provést kliknutím na tlačítko smazat na kartě Účet.


![image](assets/en/005.webp)


**!Poznámka!**


Po změně e-mailu se uživatelské jméno účtu nezmění. Dříve zadaný e-mail Address zůstane přihlašovacím jménem.


### Správa účtu - Heslo


Student si může chtít změnit heslo. Může tak učinit na kartě Heslo. Zde musí zadat své staré heslo a může ho změnit na nové.


![image](assets/en/006.webp)


### Dvoufaktorové ověřování (2fa)


Chcete-li omezit následky odcizení hesla, můžete použít dvoufaktorové ověřování (2FA), což je poměrně nová metoda zabezpečení. Dvoufaktorové ověřování můžete aktivovat prostřednictvím aplikace Správa účtu a karty pro dvoufaktorové ověřování. Po přihlášení pomocí uživatelského jména a hesla musíte provést druhý krok.


Server BTCPay podporuje dva způsoby zapnutí 2FA: 2FA prostřednictvím aplikace (Authy, Google, Microsoft Authenticators) nebo prostřednictvím bezpečnostních zařízení (FIDO2 nebo LNURL Auth).


### Dvoufaktorové ověřování - na bázi aplikace


Podle operačního systému mobilního telefonu (Android nebo iOS) si uživatelé mohou vybrat z následujících aplikací;


1. Stáhněte si dvoufaktorový ověřovač.


   - Authy pro [Android](https://play.google.com/store/apps/details?id=com.authy.authy) nebo [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator pro [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) nebo [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator pro [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) nebo [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)

2. Po stažení a instalaci aplikace Authenticator.


   - Naskenujte QR kód poskytnutý serverem BTCPay
   - Nebo zadejte klíč vygenerovaný serverem BTCPay ručně do aplikace Authenticator.

3. Aplikace Authenticator vám poskytne jedinečný kód. Zadejte jedinečný kód na serveru BTCPay, abyste ověřili nastavení, a kliknutím na tlačítko ověřit proces dokončete.


![image](assets/en/007.webp)


### Shrnutí dovedností


V této části jste se dozvěděli následující:



- Možnosti správy účtu a různé způsoby správy účtu na instanci serveru BTCPay.
- Jak nastavit 2FA v aplikaci.


### Hodnocení znalostí


#### Koncepční přezkum KA


Popište, jak aplikace 2FA pomáhá zabezpečit váš účet.


## Vytvoření nového obchodu


<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>


### Vytvoření průvodce obchodem


Když se nový uživatel přihlásí k serveru BTCPay, je prostředí prázdné a potřebuje první úložiště. Průvodce zavedením BTCPay Serveru nabídne uživateli možnost "Vytvořit svůj obchod" (1). Obchod lze považovat za domov pro potřeby Bitcoin. Nový uzel BTCPay Serveru se spustí synchronizací Bitcoin Blockchain (2). V závislosti na tom, na jaké infrastruktuře BTCPay Server provozujete, to může trvat od několika hodin až po několik dní. Aktuální verze instance je zobrazena v pravém dolním rohu uživatelského rozhraní BTCPay Serveru. To je užitečné pro referenci při řešení problémů.


![image](assets/en/008.webp)


### Vytvoření průvodce obchodem


Po absolvování tohoto kurzu se zobrazí trochu jiná obrazovka než na předchozí stránce. Protože váš instruktor připravil ukázkové prostředí, byl již předtím synchronizován Bitcoin Blockchain, a proto se vám nezobrazí stav synchronizace uzlů.


Uživatel se může rozhodnout odstranit celý svůj účet. To lze provést kliknutím na tlačítko smazat na kartě Účet.


![image](assets/en/009.webp)


**!Poznámka!**


Účty na serveru BTCPay mohou vytvářet neomezený počet obchodů. Každý obchod je Wallet nebo "domovský".


### Příklad


Začněte kliknutím na "Vytvořit obchod".


![image](assets/en/010.webp)


Tím se vytvoří vaše první domovská stránka a ovládací panel pro používání serveru BTCPay.


(1) Po kliknutí na tlačítko "Vytvořit obchod" vás server BTCPay požádá o pojmenování obchodu; může to být cokoli, co se vám hodí.


![image](assets/en/011.webp)


(2) Dále musí být nastavena výchozí měna úložiště, a to buď fiat měna, nebo měna denominovaná v Bitcoin nebo Sats. Pro demonstrační prostředí ji nastavíme na USD.


![image](assets/en/012.webp)


(3) Jako poslední parametr v nastavení obchodu vyžaduje server BTCPay nastavení "Preferovaného zdroje cen" pro porovnání ceny Bitcoin s aktuální fiat cenou, aby váš obchod zobrazoval správný kurz Exchange mezi Bitcoin a fiat měnou nastavenou v obchodě. V ukázkovém příkladu se budeme držet výchozího nastavení a nastavíme jej na Kraken Exchange. Server BTCPay používá ke kontrole kurzů Exchange rozhraní Kraken API.


![image](assets/en/013.webp)


(4) Po nastavení těchto parametrů obchodu klikněte na tlačítko Vytvořit a server BTCPay vytvoří ovládací panel vašeho prvního obchodu, kde bude pokračovat průvodce.


![image](assets/en/014.webp)


Gratulujeme, vytvořili jste svůj první obchod a tím toto cvičení končí.


![image](assets/en/015.webp)


### Shrnutí dovedností


V této části jste se dozvěděli:



- Vytvoření obchodu a konfigurace výchozí měny v kombinaci s předvolbami zdroje cen.
- Každý "Store" je nový domov oddělený od ostatních obchodů na této instalaci BTCPay Serveru.


# Úvod do zabezpečení klíčů Bitcoin


<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>


## Porozumění generování klíčů Bitcoin


<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>


### Co se děje při generování klíčů Bitcoin?


Peněženky Bitcoin při vytvoření vytvářejí tzv. V posledním cíli jste vytvořili "seed", Řada slov vytvořených předtím je také známa jako fráze Mnemonic. Ze slovíčka seed se odvozují jednotlivé klíče Bitcoin a používají se k odesílání nebo přijímání slovíček Bitcoin. Fráze seed by nikdy neměly být sdíleny s třetími stranami nebo nedůvěryhodnými partnery.


Generování seed se provádí podle průmyslového standardu známého jako "hierarchický deterministický" (HD) rámec.


![image](assets/en/016.webp)


### Adresy


BTCPay Server je postaven na generate a novém Address. Tím se zmírňuje problém opakovaného použití veřejného klíče nebo Address. Použití stejného veřejného klíče velmi usnadňuje sledování celé historie plateb. Přemýšlení o klíčích jako o jednorázových poukázkách by výrazně zlepšilo vaše soukromí. Používáme také adresy Bitcoin, nezaměňujte je s veřejnými klíči.


Klíč Address se odvozuje z veřejného klíče pomocí "hashovacího algoritmu" Většina peněženek a transakcí však zobrazuje spíše Adresy než tyto veřejné klíče. Adresy jsou obecně kratší než veřejné klíče a obvykle začínají znakem `1`, `3` nebo `bc1`, zatímco veřejné klíče začínají znakem `02`, `03` nebo `04`.



- Adresy začínající na `1.....` jsou stále velmi časté. Jak bylo uvedeno v kapitole "Vytvoření nového úložiště", jedná se o starší adresy. Tento typ Address je určen pro transakce P2PKH. P2Pkh používá kódování Base58, díky čemuž se u Address rozlišují malá a velká písmena. Jeho struktura je založena na veřejném klíči s další číslicí jako identifikátorem.



- Adresy začínající `bc1...` se pomalu přesouvají mezi velmi běžné adresy. Tyto adresy se nazývají (nativní) adresy SegWit. Ty nabízejí lepší strukturu poplatků než ostatní zmíněné Adresy. Nativní adresy SegWit používají kódování Bech32 a umožňují psát pouze malá písmena.



- Adresy začínající na `3...` se na burzách stále běžně používají pro vkladové adresy. Tyto adresy jsou zmíněny v kapitole "Vytvoření nového úložiště", zabalené nebo vnořené adresy SegWit. Mohou však fungovat také jako "Multisig Address". Při použití jako SegWit Address dochází k určité úspoře transakčních poplatků, opět však menší než u nativních SegWit. Adresy P2SH používají kódování Base58. Díky tomu jsou stejně jako starší Address citlivé na velikost písmen.



- Adresy začínající `2...` jsou adresy Testnet. Jsou určeny pro příjem Testnet Bitcoin (tBTC). Nikdy byste to neměli zaměňovat a posílat na tyto adresy Bitcoin. Pro účely vývoje můžete generate a Testnet Wallet. Na internetu existuje více kohoutků pro získání Testnet Bitcoin. Nikdy nekupujte Testnet Bitcoin. Testnet Bitcoin se těží. To může být pro vývojáře důvodem, aby místo toho použil Regtest. Jedná se o prostředí hřiště pro vývojáře, kde chybí určité síťové komponenty. Bitcoin je však pro vývojové účely velmi užitečný.


### Veřejné klíče


Veřejné klíče se dnes v praxi používají méně často. Postupem času je uživatelé Bitcoin nahrazují adresami. Stále však existují a občas se ještě používají. Veřejné klíče jsou obecně mnohem delší řetězce než adresy. Stejně jako adresy začínají specifickým identifikátorem.



- Za prvé, `02...` a `03...` jsou velmi standardní identifikátory veřejných klíčů zakódované ve formátu SEC. Lze je zpracovat a přeměnit na adresy pro příjem, použít pro vytvoření adres multi-sig nebo pro ověření podpisu. V dřívějších transakcích Bitcoin se veřejné klíče používaly jako součást transakcí P2PK.



- Peněženky HD však mají jinou strukturu. `xpub...`, `ypub...` nebo `zpub...` se nazývají rozšířené veřejné klíče neboli xpub. Tyto klíče se používají k odvození mnoha veřejných klíčů jako součást HD Wallet. Protože váš xpub obsahuje záznamy o celé vaší historii, tedy o minulých i budoucích transakcích, nikdy je nesdílejte s nedůvěryhodnými stranami.


### Shrnutí dovedností


V této části jste se dozvěděli následující:



- Rozdíly mezi adresami a typy dat veřejných klíčů a výhody používání adres oproti veřejným klíčům.


### Hodnocení znalostí


Popište výhody používání nových adres pro každou transakci ve srovnání s metodami opakovaného použití Address nebo veřejného klíče.


## Zabezpečení klíčů pomocí Hardware Wallet


<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>


### Uložení klíčů Bitcoin


Po vygenerování fráze seed vyžaduje seznam 12-24 slov vygenerovaný v této knize řádné zálohování a zabezpečení, protože tato slova jsou jediným způsobem, jak obnovit přístup k Wallet. Struktura peněženek HD a způsob deterministického generování adres pomocí jediné fráze seed znamená, že všechny vaše vytvořené adresy budou zálohovány pomocí tohoto jediného seznamu slov Mnemonic, který představuje vaši frázi seed nebo frázi pro obnovení.


Udržujte frázi pro obnovení v bezpečí. Pokud se k němu někdo dostane, konkrétně se zlým úmyslem, může vaše finanční prostředky přesunout. Udržujte seed v bezpečí a zároveň nezapomínejte, že je mezi nimi vzájemná. Existuje několik způsobů ukládání soukromých klíčů Bitcoin. Každý z nich má své výhody a nevýhody, pokud jde o bezpečnost, soukromí, pohodlí a fyzické uložení. Vzhledem k důležitosti soukromých klíčů mají uživatelé systému Bitcoin tendenci tyto klíče uchovávat a bezpečně uchovávat spíše ve "vlastní úschově", než aby využívali "úschovných" služeb, jako jsou banky. V závislosti na uživateli musí používat buď řešení pro ukládání klíčů Cold, nebo Hot Wallet.


### Hot a Cold uložení klíčů Bitcoin


Obvykle se peněženky Bitcoin označují jako Hot Wallet nebo Cold Wallet. Většina kompromisů spočívá v pohodlí, snadnosti použití a bezpečnostních rizicích. Každý z těchto způsobů lze také vidět v řešení pro správce. Kompromisy jsou zde však většinou založeny na bezpečnosti a ochraně soukromí a přesahují rámec tohoto kurzu.


### Hot Wallet


Peněženky Hot představují nejpohodlnější způsob interakce s Bitcoin prostřednictvím mobilního, webového nebo desktopového softwaru. Peněženka Wallet je vždy připojena k internetu, což uživatelům umožňuje odesílat nebo přijímat peněženky Bitcoin. To je však také jeho slabinou; protože je Wallet stále online, je nyní zranitelnější vůči útokům hackerů nebo malwaru na vaše zařízení. V serveru BTCPay ukládají peněženky Hot soukromé klíče v instanci. Kdokoli, kdo získá přístup k vašemu úložišti na serveru BTCPay Server, může potenciálně ukrást finanční prostředky z tohoto Address, pokud je zlovolný. Pokud BTCPay Server běží v hostovaném prostředí, měli byste tuto skutečnost vždy zohlednit ve svém bezpečnostním profilu a v takovém případě Hot Wallet raději nepoužívat. Pokud je BTCPay Server nainstalován na vámi vlastněném a zabezpečeném hardwaru, rizikový profil se výrazně snižuje, ale nikdy zcela nezmizí.


### Cold Wallet


Jednotlivci přesunou svůj klíč Bitcoin do Cold Wallet, protože ten dokáže izolovat soukromé klíče od internetu, a tím je chránit před potenciálními online hrozbami. Odstranění internetového připojení z rovnice snižuje riziko malwaru, spywaru a výměny SIM karet. Má se za to, že úložiště Cold je z hlediska bezpečnosti a autonomie lepší než úložiště Hot, pokud jsou přijata odpovídající opatření, aby se zabránilo ztrátě soukromých klíčů Bitcoin. Úložiště Cold je nejvhodnější pro velké množství klíčů Bitcoin, které se vzhledem ke složitosti nastavení Wallet nemají často utrácet.


Existují různé způsoby ukládání klíčů Bitcoin do úložiště Cold, od papírových peněženek přes mozkové peněženky, hardwarové peněženky nebo od počátku soubor Wallet. Většina peněženek používá k zápisu BIP 39 do generate frázi seed. V rámci softwaru Bitcoin core však zatím nebylo dosaženo konsenzu o jeho používání. Software Bitcoin core bude stále generate soubor Wallet.dat, který je třeba uložit na bezpečné offline místo.


### Shrnutí dovedností


V této části jste se dozvěděli:



- Rozdíly mezi peněženkami Hot a Cold z hlediska funkčnosti a jejich kompromisů.


### Hodnocení znalostí Koncepční přehled



- Co je Wallet?



- Jaký je rozdíl mezi peněženkami Hot a Cold?



- Popište, co znamená "generování Wallet"?


## Používání kláves Bitcoin


<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>


### Server BTCPay Wallet


BTCPay Server obsahuje následující standardní funkce Wallet:



- Transakce
- Odeslat
- Příjem
- Rescan
- Tažení plateb
- Výplaty
- PSBT
- Obecná nastavení


### Transakce


Správci mohou v zobrazení transakcí zobrazit příchozí a odchozí transakce pro On-Chain Wallet připojené k tomuto konkrétnímu úložišti. U každé transakce jsou rozlišeny přijaté a odeslané částky. Přijaté budou mít barvu Green a odeslané transakce budou mít červenou barvu. V rámci zobrazení transakcí serveru BTCPay uvidí správci také sadu standardních štítků.


| Transaction Type | Description                                          |
| ---------------- | ---------------------------------------------------- |
| App              | Payment was received through an app-created invoice  |
| invoice          | Payment was received through an invoice              |
| payjoin          | Not paid, invoice timer still has not expired        |
| payjoin-exposed  | UTXO was exposed through an invoice payjoin proposal |
| payment-request  | Payment was received through a payment request       |
| payout           | Payment was sent through a payout or refund          |

### Jak odeslat


Funkce odesílání serveru BTCPay odesílá transakce z vašeho serveru BTCPay On-Chain Wallet. Server BTCPay umožňuje více způsobů podepisování transakcí za účelem utrácení finančních prostředků. Transakci lze podepsat pomocí;



- Hardware Wallet
- Peněženky podporující PSBT
- Soukromý klíč HD nebo semena pro obnovení.
- Hot Wallet


#### Hardware Wallet


BTCPay Server má vestavěnou podporu Hardware Wallet, která vám umožní používat váš Hardware Wallet s BTCPay Vault bez úniku informací do aplikací nebo serverů třetích stran. Integrace Hardware Wallet v rámci BTCPay Serveru umožňuje importovat váš Hardware Wallet a utrácet příchozí prostředky jednoduchým potvrzením na vašem zařízení. Vaše soukromé klíče nikdy neopustí zařízení a všechny finanční prostředky jsou ověřovány proti vašemu Full node, což zajišťuje, že nedojde k úniku dat.


#### Podepisování pomocí Wallet podporujícího PSBT


PSBT (částečně podepsané transakce Bitcoin) je výměnný formát pro transakce Bitcoin, které ještě musí být plně podepsány. PSBT je podporován na serveru BTCPay a lze jej podepisovat pomocí kompatibilních hardwarových a softwarových peněženek.


Konstrukce plně podepsané transakce Bitcoin probíhá v následujících krocích:



- PSBT je zkonstruován se specifickými vstupy a výstupy, ale bez signatur
- Exportovaný PSBT lze importovat pomocí Wallet, který tento formát podporuje
- Data transakce lze zkontrolovat a podepsat pomocí Wallet
- Podepsaný soubor PSBT se exportuje z Wallet a importuje se do serveru BTCPay
- Server BTCPay vytvoří konečnou transakci Bitcoin
- Ověříte výsledek a odešlete jej do sítě


#### Podepisování pomocí soukromého klíče HD nebo Mnemonic seed


Pokud jste si před použitím serveru BTCPay vytvořili účet Wallet, můžete peníze utratit zadáním svého soukromého klíče do příslušného pole. Nastavte správnou "AccountKeyPath" v Wallet> Settings; jinak nemůžete utrácet.


#### Podepisování pomocí Hot Wallet


Pokud jste při nastavování úložiště vytvořili nový účet Wallet a povolili jej jako Hot Wallet, automaticky se k podpisu použije účet seed uložený na serveru.


### RBF (Replace-by-fee)


Replace-by-fee (RBF) je funkce protokolu Bitcoin, která umožňuje nahradit dříve vysílanou transakci (dokud není potvrzena). To umožňuje náhodně změnit otisk transakce Wallet nebo ji nahradit vyšší sazbou poplatku a posunout tak transakci výše ve frontě potvrzení (Mining) s vyšší prioritou. Tím bude původní transakce účinně nahrazena, protože vyšší sazba poplatku bude mít prioritu, a po potvrzení bude původní transakce zneplatněna (nedojde k dvojímu utracení).


Stisknutím tlačítka "Advanced Settings" zobrazíte možnosti RBF.


![image](assets/en/017.webp)



- Randomizace pro vyšší soukromí umožňuje automatické nahrazení transakce za účelem randomizace otisku prstu transakce.
- Ano, označit transakci pro RBF a explicitně ji nahradit (není nahrazena ve výchozím nastavení, pouze zadáním)
- Ne, nepovolte nahrazení transakce.


### Výběr Coin


Výběr Coin je pokročilá funkce pro zvýšení ochrany soukromí, která vám umožňuje vybrat mince, které chcete utratit při vytváření transakce. Například platbu mincemi, které jsou čerstvě pořízené z mixu conjoinů.


Výběr Coin funguje nativně s funkcí štítků Wallet. Díky tomu můžete příchozí prostředky označovat štítky pro hladší správu a utrácení UTXO.


BTCPay Server podporuje BIP-329 pro správu štítků. Pokud převádíte z Wallet, který podporuje BIP-329, a máte nastavené štítky, BTCPay Server je automaticky rozpozná a importuje. Při migraci serverů lze tyto informace také exportovat a importovat do nového prostředí.


### Jak přijímat


Po kliknutí na tlačítko pro příjem na serveru BTCPay se vygeneruje nepoužitý účet Address, který lze použít pro příjem plateb. Správci mohou také vytvořit nový generate vytvořením nového "Invoice"


Server BTCPay vás vždy vyzve, abyste generate následující dostupné Address, aby se zabránilo opakovanému použití Address. Po kliknutí na "generate další dostupný BTC Address" vygeneruje BTCPay Server nový Address a QR. Umožňuje vám také přímo nastavit štítek k Address pro lepší správu vašich adres.


![image](assets/en/018.webp)


![image](assets/en/019.webp)


#### Opětovné skenování


Funkce Rescan se spoléhá na funkci "Scantxoutset" ve verzi Bitcoin core 0.17.0, která skenuje aktuální stav sady Blockchain (nazývané UTXO Set) a hledá mince patřící do nakonfigurovaného derivačního schématu. Opětovné skenování Wallet řeší dva běžné problémy, se kterými se uživatelé serveru BTCPay často setkávají.


1. Problém s limitem mezery - Většina peněženek třetích stran jsou lehké peněženky, které sdílejí uzel mezi mnoha uživateli. Lehké peněženky a peněženky závislé na Full node omezují počet (obvykle 20) adres bez zůstatku, které sledují na Blockchain, aby se předešlo problémům s výkonem. Server BTCPay generuje nový Address pro každý Invoice. S ohledem na výše uvedené platí, že poté, co BTCPay Server vygeneruje 20 po sobě jdoucích nezaplacených faktur, externí Wallet přestane transakce načítat za předpokladu, že nedošlo k žádným novým transakcím. Váš externí Wallet je nebude zobrazovat, jakmile budou faktury uhrazeny 21., 22. atd. Na druhou stranu interní server BTCPay Wallet sleduje všechny vygenerované Address spolu s výrazně vyšším limitem mezer. Nespoléhá se na třetí stranu a dokáže vždy zobrazit správný zůstatek.

2. Řešení limitu mezery - Pokud váš [externí/existující Wallet](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet) umožňuje konfiguraci limitu mezery, je snadné jej zvýšit. Většina peněženek to však neumožňuje. Jediné peněženky, které v současné době podporují konfiguraci gap-limit, o kterých víme, jsou Electrum, Wasabi a Sparrow wallet. Bohužel je pravděpodobné, že na problém narazíte i u mnoha dalších peněženek. Pro nejlepší uživatelský zážitek a ochranu soukromí zvažte použití interní peněženky Wallet serveru BTCPay namísto externích peněženek.


#### Server BTCPay používá "mempoolfullrbf=1"


BTCPay Server používá "mempoolfullrbf=1"; přidali jsme ji jako výchozí do nastavení BTCPay Serveru. Nicméně jsme také vytvořili funkci, kterou můžete sami vypnout. Bez funkce "mempoolfullrbf=1" by se obchodník v případě, že by zákazník dvakrát utratil platbu s transakcí, která nesignalizuje RBF, dozvěděl až po potvrzení.


Správce může chtít toto nastavení zrušit. Pomocí následujícího řetězce můžete výchozí nastavení změnit.


```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i
```


### Nastavení serveru BTCPay Wallet


Nastavení Wallet na serveru BTCPay Server poskytují jasný a stručný přehled obecných nastavení vašeho Wallet. Všechna tato nastavení jsou předvyplněna, pokud byl Wallet vytvořen pomocí BTCPay Serveru.


![image](assets/en/020.webp)


Nastavení Wallet na serveru BTCPay Server poskytují jasný a stručný přehled obecných nastavení vašeho Wallet. Všechna tato nastavení jsou předvyplněna, pokud byl Wallet vytvořen pomocí BTCPay Serveru. Nastavení Wallet na serveru BTCPay Server začínají stavem Wallet. Jedná se o Wallet, který je určen pouze pro sledování, nebo o Hot? V závislosti na typu Wallet se mohou lišit akce, včetně opětovného skenování Wallet kvůli chybějícím transakcím, ořezání starých transakcí z historie, registrace Wallet pro platební odkazy nebo nahrazení a odstranění stávajícího Wallet připojeného k obchodu. V nastavení Wallet serveru BTCPay mohou správci nastavit štítek pro Wallet pro lepší správu Wallet. Správce zde také uvidí Schéma odvození, klíč k účtu (xpub), Otisk prstu a Cestu klíče. Platby v nastavení Wallet mají pouze dvě hlavní nastavení. Platba je neplatná, pokud se nepodaří potvrdit transakci do (nastavených minut) po vypršení platnosti Invoice. Považujte Invoice za potvrzenou, pokud má platební transakce X potvrzení. Správci mohou také nastavit přepínač pro zobrazení doporučených poplatků na obrazovce platby nebo nastavit ruční cíl potvrzení v počtu bloků.


![image](assets/en/021.webp)


**!Poznámka!**


Pokud tento kurz sledujete samostatně, vytvoření tohoto účtu by pravděpodobně proběhlo na hostiteli třetí strany. Proto opět doporučujeme, abyste je nepoužívali jako produkční prostředí, ale spíše pouze pro účely školení.


### Příklad


#### Nastavení Bitcoin Wallet na serveru BTCPay


Server BTCPay nabízí dva způsoby nastavení účtu Wallet. Jedním ze způsobů je import stávajícího Bitcoin Wallet. Import lze provést připojením Hardware Wallet, importem souboru Wallet, zadáním rozšířeného veřejného klíče, naskenováním QR kódu Wallet nebo, což je nejméně výhodné, ručním zadáním dříve vytvořeného Wallet recovery seed. V BTCPay Serveru je také možné vytvořit nový Wallet. Při vytváření nového Wallet lze BTCPay Server nakonfigurovat dvěma možnými způsoby.


Možnost Hot Wallet v serveru BTCPay umožňuje funkce jako "PayJoin" nebo "Liquid". Má to však jednu nevýhodu: obnovení seed vygenerované pro tento Wallet bude uloženo na serveru, odkud si ho může kdokoli s administrátorskými právy stáhnout. Vzhledem k tomu, že váš soukromý klíč je odvozen od vašeho obnovovacího klíče seed, mohl by záškodník získat přístup k vašim současným i budoucím prostředkům!


Pro zmírnění tohoto rizika na serveru BTCPay může správce nastavit hodnotu v Nastavení serveru > Zásady > "Povolit neadminům vytvářet peněženky Hot pro jejich obchody" na "ne", protože se jedná o výchozí hodnotu. Pro zvýšení bezpečnosti těchto peněženek Hot by měl správce serveru povolit ověřování 2FA na účtech, které mají povoleno mít peněženky Hot. Ukládání soukromých klíčů na veřejném serveru je nebezpečná praxe a nese s sebou značná rizika. Některá z nich jsou podobná rizikům Lightning Network (viz další kapitola o rizicích Lightning Network).


Druhou možností, kterou server BTCPay nabízí při generování nového účtu Wallet, je vytvoření účtu Watch-only wallet. BTCPay Server vytvoří generate vaše soukromé klíče jednou. Poté, co uživatel potvrdí, že si zapsal svou frázi seed, BTCPay Server vymaže soukromé klíče ze serveru. Výsledkem je, že váš obchod má nyní připojený Watch-only wallet. Chcete-li přijaté prostředky utratit na svém účtu Watch-only wallet, podívejte se do kapitoly Jak odeslat, a to buď pomocí trezoru BTCPay Serveru, PSBT (Partially Signed Bitcoin Transaction), nebo, což se doporučuje nejméně, ručním zadáním své fráze seed.


V poslední části jste vytvořili nový "Store". Průvodce instalací bude pokračovat výzvou "Set up a Wallet" nebo "Set up a Lightning node". V tomto příkladu budete postupovat podle postupu průvodce "Set up a Wallet" (1).


![image](assets/en/022.webp)


Po kliknutí na tlačítko "Nastavit Wallet" bude průvodce pokračovat dotazem, jak chcete pokračovat; BTCPay Server nyní nabízí možnost připojit stávající Bitcoin Wallet k vašemu novému obchodu. Pokud Wallet nemáte, BTCPay Server vám navrhne vytvoření nového. Tento příklad bude postupovat podle kroků pro "vytvoření nového Wallet" (2). Postupujte podle kroků, abyste se dozvěděli, jak "připojit existující Wallet (1).


![image](assets/en/023.webp)


**!Poznámka!**


Pokud tento kurz absolvujete ve třídě, vezměte prosím na vědomí, že aktuální příklad a seed, které jsme vygenerovali, slouží pouze pro vzdělávací účely. Na těchto adresách by nikdy nemělo být žádné podstatné množství jiné, než je požadováno v průběhu cvičení.


(1) Pokračujte v průvodci "New Wallet" kliknutím na tlačítko "Create a new Wallet".


![image](assets/en/024.webp)


(2) Po kliknutí na tlačítko "Create a new Wallet" se v dalším okně průvodce zobrazí možnosti "Hot Wallet" a "Watch-only wallet" Pokud postupujete společně s instruktorem, vaše prostředí je sdílená ukázka a můžete vytvořit pouze Watch-only wallet. Všimněte si rozdílu mezi oběma obrázky níže. Protože jste v prostředí Demo a sledujete instruktora, vytvořte "Watch-only wallet" a pokračujte průvodcem "New Wallet".


![image](assets/en/025.webp)


![image](assets/en/026.webp)


(3) Pokračujte v novém průvodci Wallet a nyní se nacházíte v části Vytvořit BTC Watch-only wallet. Zde se dostaneme k nastavení "typu Wallet" Server BTCPay umožňuje zvolit preferovaný typ Address; v době psaní tohoto kurzu se stále doporučuje používat adresy bech32. Podrobněji se o adresách dozvíte v první kapitole tohoto dílu.



- SegWit (bech32)
  - Nativní adresy SegWit začínají na `bc1q`.
  - Příklad: `bc1qXXXXXXXXXXXXXXXXXXXXXX`
- Odkaz
  - Starší adresy jsou adresy začínající číslem `1`.
  - Příklad: `15e15hXXXXXXXXXXXXXXXXXXXX`
- Taproot (pro pokročilé uživatele)
  - Adresy Taproot začínají na `bc1p`.
  - Příklad: `bc1pXXXXXXXXXXXXXXXXXXXXXXXX`
- SegWit v obalu
  - Adresy zabalené v SegWit začínají na `3`.
  - Příklad: `37BBXXXXXXXXXXXXXXX`


Jako preferovaný typ Wallet Address zvolte SegWit (doporučený).


![image](assets/en/027.webp)


(4) Při nastavování parametru pro Wallet umožňuje server BTCPay uživatelům nastavit volitelný passphrase prostřednictvím BIP39; nezapomeňte potvrdit heslo.


![image](assets/en/028.webp)


(5) Po nastavení typu Wallet Address a případném nastavení některých pokročilých možností klikněte na tlačítko Vytvořit a server BTCPay generate vytvoří váš nový Wallet. Všimněte si, že toto je poslední krok před vygenerováním vaší fráze seed. Ujistěte se, že to děláte pouze v prostředí, kde by někdo nemohl ukrást frázi seed pohledem na vaši obrazovku.


![image](assets/en/029.webp)


(6) Na následující obrazovce průvodce vám server BTCPay zobrazí frázi Recovery seed pro váš nově vygenerovaný Wallet; jedná se o klíče pro obnovení vašeho Wallet a podepisování transakcí. Server BTCPay vygeneruje frázi seed o 12 slovech. Tato slova budou po této obrazovce nastavení ze serveru vymazána. Tato fráze Wallet je konkrétně frází Watch-only wallet. Doporučujeme neukládat tuto frázi seed digitálně nebo pomocí fotografie. Uživatelé mohou v průvodci pokračovat dále, pouze pokud aktivně potvrdí, že si frázi seed zapsali.


![image](assets/en/030.webp)


(7) Po kliknutí na tlačítko Hotovo a zajištění nově vygenerované fráze Bitcoin seed server BTCPay aktualizuje váš obchod s přiloženou novou frází Wallet a je připraven přijímat platby. V uživatelském okně Interface si v levém navigačním menu všimněte, jak je nyní Bitcoin zvýrazněn a aktivován pod Wallet.


![image](assets/en/031.webp)


### Příklad: Zápis věty seed


Toto je obzvláště bezpečný okamžik pro použití Bitcoin. Jak již bylo zmíněno, přístup k frázi seed nebo její znalost byste měli mít pouze vy. Vzhledem k tomu, že sledujete instruktora a učebnu, měla by být vygenerovaná hláška seed používána pouze v tomto kurzu. Příliš mnoho faktorů, včetně zvědavých pohledů spolužáků, nezabezpečených systémů a dalších, činí tyto klíče pouze výukovými a nedůvěryhodnými. Vygenerované klíče by však přesto měly být uloženy pro příklady z kurzu.


První metodou, kterou v této situaci použijeme a která je zároveň nejméně bezpečná, je zapsání věty seed ve správném pořadí. Karta s frází seed je součástí studijních materiálů poskytnutých studentovi nebo ji lze nalézt na serveru BTCPay GitHub. Tuto kartu použijeme k zápisu slov vygenerovaných v předchozím kroku. Dbejte na to, abyste je zapisovali ve správném pořadí. Po jejich zapsání je porovnejte s tím, co vám poskytl software, abyste se ujistili, že jste je zapsali ve správném pořadí. Jakmile je zapíšete, klikněte na zaškrtávací políčko s prohlášením, že jste frázi seed zapsali správně.


### Příklad: Uložení fráze seed na Hardware Wallet


V tomto kurzu se zabýváme ukládáním fráze seed do zařízení Hardware Wallet. Následování tohoto kurzu s instruktorem může někdy zahrnovat takové zařízení. V materiálech pro průvodce kurzem je sestaven seznam hardwarových peněženek, které by byly pro toto cvičení vhodné.


V tomto příkladu použijeme trezor BTCPay Server a Blockstream Jade Hardware Wallet.


Můžete se také podívat na videoprůvodce připojením Hardware Wallet.

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::


Stáhnout BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases


Ujistěte se, že jste stáhli správné soubory pro váš konkrétní systém. Uživatelé systému Windows by si měli stáhnout balíček [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), uživatelé systému Mac balíček [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg) a uživatelé systému Linux balíček [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)


Po instalaci BTCPay Server Vault spusťte software kliknutím na ikonu na ploše. Po správné instalaci a prvním spuštění se BTCPay Server Vault zeptá na povolení k použití s webovými aplikacemi. Požádá o udělení přístupu ke konkrétnímu serveru BTCPay Server, se kterým pracujete. Přijměte tyto podmínky. BTCPay Server Vault nyní vyhledá Hardwarové zařízení. Jakmile je zařízení nalezeno, BTCPay Server rozpozná, že je Trezor spuštěn, a vyhledá vaše zařízení.


**!Poznámka!**


Při používání Hot Wallet nedávejte klíče SSH ani účet správce serveru nikomu jinému než správcům. Kdokoli s přístupem k těmto účtům bude mít přístup k prostředkům v Hot Wallet.


### Shrnutí dovedností


V této části jste se dozvěděli následující:



- Transakční pohled na Bitcoin Wallet a jeho různé kategorizace.
- Při odesílání z Bitcoin Wallet jsou k dispozici různé možnosti, od hardwaru až po peněženky Hot.
- Problém s mezerou, se kterým se setkáváme při používání většiny peněženek, a jak jej odstranit.
- Jak vytvořit nový generate Bitcoin Wallet v rámci serveru BTCPay, včetně uložení klíčů v Hardware Wallet a zálohování fráze pro obnovení.


V tomto cíli jste se naučili, jak v rámci serveru BTCPay vytvořit nový generate Bitcoin Wallet. Zatím jsme se nezabývali tím, jak tyto klíče zabezpečit nebo používat. V rychlém přehledu tohoto cíle jste se naučili, jak nastavit první úložiště. Naučili jste se, jak vytvořit generate frázi Bitcoin Recovery seed.


### Hodnocení znalostí Praktický přehled


Popište metodu generování klíčů a schéma jejich zabezpečení spolu s kompromisy/riziky bezpečnostního schématu.


## BTCPay Server Lightning Wallet


<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>


Když správce serveru vytváří novou instanci BTCPay Serveru, může nastavit implementaci Lightning Network, například LND, Core Lightning nebo Eclair; podrobnější pokyny k instalaci najdete v části Konfigurace BTCPay Serveru.


Pokud budete následovat učebnu, připojení uzlu Lightning k serveru BTCPay funguje prostřednictvím uzlu Custom. Uživatel, který není správcem serveru BTCPay Server, nebude moci ve výchozím nastavení používat interní uzel Lightning. Je to z důvodu ochrany vlastníka serveru před ztrátou jeho prostředků. Správci serverů mohou nainstalovat zásuvný modul, který jim umožní přístup k uzlu Lightning prostřednictvím LNBank; to je však mimo rozsah této knihy. Další informace o LNBank naleznete na oficiální stránce zásuvného modulu.


### Připojení interního uzlu (správce serveru)


Správce serveru může používat interní Lightning Node BTCPay Serveru. Bez ohledu na implementaci Lightning je připojení k internímu uzlu Lightning stejné.


Přejděte do předchozího úložiště nastavení a v levé nabídce klikněte na položku "Lightning" Wallet. Server BTCPay nabízí dvě možnosti nastavení: použití interního uzlu (ve výchozím nastavení pouze správce serveru) nebo vlastního uzlu (externí připojení). Správci serveru mohou kliknout na možnost "Použít interní uzel". Není třeba provádět žádnou další konfiguraci. Klikněte na tlačítko "uložit" a všimněte si oznámení s textem: "BTC Lightning node updated". Úložiště nyní úspěšně získalo schopnosti Lightning Network.


### Připojení externího uzlu (uživatel serveru/vlastník úložiště)


Ve výchozím nastavení nemají majitelé obchodů povoleno používat správce serveru Lightning Node. Připojení musí být navázáno na externí uzel, a to buď na uzel vlastněný majitelem obchodu před nastavením serveru BTCPay, nebo na zásuvný modul LNBank, pokud jej správce serveru zpřístupní, nebo na řešení správce, jako je Alby.


Přejděte do obchodu s předchozím nastavením a v levém menu klikněte na položku Blesk pod peněženkami. Vzhledem k tomu, že majitelé obchodů nemají ve výchozím nastavení povoleno používat interní uzel, je tato možnost zašedlá. Použití vlastního uzlu je jedinou možností, která je ve výchozím nastavení pro majitele obchodů k dispozici.


Server BTCPay vyžaduje informace o připojení; předem připravené (nebo správcovské) řešení dodá tyto informace speciálně přizpůsobené implementaci Lightning. V rámci serveru BTCPay Server mohou majitelé obchodů používat následující připojení;



- C-lightning přes TCPneboUnixdomainsocketconnection.
- Nabíjení bleskem přes HTTPS
- Eclair přes HTTPS
- LND prostřednictvím proxy serveru REST
- LNDhub prostřednictvím rozhraní REST API


![image](assets/en/032.webp)


Kliknutím na tlačítko "otestovat připojení" se ujistěte, že jste správně zadali údaje o připojení. Po potvrzení správnosti připojení klikněte na "Uložit" a server BTCPay zobrazí, že obchod je aktualizován pomocí uzlu Lightning.


### Správa interního uzlu Lightning LND (správce serveru)


Po připojení interního uzlu Lightning si správci serveru všimnou nových dlaždic na panelu Dashboard určených speciálně pro informace Lightning.



- Vyvážení blesků
- BTC v kanálech
  - Otevírací kanály BTC
  - Místní zůstatek BTC
  - Vzdálený zůstatek BTC
  - Uzavírání kanálů BTC
- BTC On-Chain
  - Společnost BTC potvrdila
  - BTC nepotvrzeno
  - BTC vyhrazeno
- Služby Lightning
  - Ride the Lightning (RTL).


Správci serverů se mohou dostat do RTL pro správu uzlů Lightning kliknutím na logo Ride the Lightning v dlaždici "Lightning services" nebo na položku "Lightning" pod peněženkami v levém menu.


**Poznámka!**


Připojení interního uzlu Lightning selhalo - Pokud interní připojení selže, potvrďte:


1. Uzel Bitcoin On-Chain je plně synchronizován

2. Vnitřní uzel blesku je "Enabled" v části "Lightning" > "Settings" > "BTC Lightning Settings"


Pokud se nemůžete připojit k uzlu Lightning, můžete zkusit restartovat server nebo si přečíst další podrobnosti v oficiální dokumentaci serveru BTCPay; https://docs.btcpayserver.org/Troubleshooting/. Dokud se váš uzel Lightning nezobrazí jako "Online", nemůžete ve svém obchodě přijímat platby Lightning. Zkuste otestovat své připojení k Lightning kliknutím na odkaz "Public Node Info".


### Blesk Wallet


V možnosti Lightning Wallet v levém panelu nabídek najdou správci serverů snadný přístup k RTL, informacím o svém veřejném uzlu a nastavení Lightning specifickému pro jejich obchod BTCPay Server.


#### Informace o interním uzlu


Správci serverů mohou kliknutím na informace o interním uzlu zobrazit stav serveru (Online/Offline) a řetězec připojení pro Clearnet nebo Tor.


![image](assets/en/033.webp)


#### Změna připojení


Chcete-li změnit externí uzel Lightning, přejděte do "Nastavení Lightning" a klikněte na "Změnit připojení" (vedle "Informace o veřejném uzlu"). Tím obnovíte stávající nastavení. Zadejte nové údaje o uzlu, klikněte na tlačítko Uložit a obchod se odpovídajícím způsobem aktualizuje.


![image](assets/en/034.webp)


#### Služby


Pokud se správce serveru rozhodne nainstalovat více služeb pro implementaci Lightning, budou zde uvedeny. Při standardní implementaci LND budou mít správci k dispozici standardní nástroj Ride The Lightning (RTL) pro správu uzlů.


#### Nastavení BTC Lightning Wallet


Po přidání uzlu Lightning do obchodu v předchozím kroku se mohou majitelé obchodů rozhodnout, že jej pro svůj obchod deaktivují pomocí přepínače v horní části nastavení Lightning.


![image](assets/en/035.webp)


#### Možnosti platby Lightning


Majitelé obchodů mohou nastavit následující parametry, aby zlepšili zážitek svých zákazníků ze služby Lightning.



- Zobrazení částek platby blesku v satoshi.
- Přidání nápovědy hop pro soukromé kanály do zařízení Lightning Invoice.
- Sjednocení URL/QR kódů plateb On-Chain a Lightning při placení.
- Nastavení šablony popisu pro bleskové faktury.


#### LNURL


Majitelé obchodů se mohou rozhodnout, zda budou LNURL používat, nebo ne. Adresa URL Lightning Network neboli LNURL je navrhovaný standard pro interakci mezi Lightning Payer a příjemcem platby. Stručně řečeno, LNURL je adresa URL kódovaná v jazyce bech32 s předponou LNURL. Od Lightning Wallet se očekává, že dekóduje adresu URL, kontaktuje ji a očekává objekt JSON s dalšími instrukcemi, především se značkou, která definuje chování LNURL.



- Povolit LNURL
- LNURL Klasický režim
  - Pro kompatibilitu s Wallet, kódování Bech32 (klasické) vs. cleartextová adresa URL (připravované)
- Umožnit příjemci platby předat komentář.


### Příklad 1


#### Připojení k aplikaci Lightning pomocí interního uzlu (správce)


Tato možnost je k dispozici pouze v případě, že jste správcem této instance nebo pokud správce změnil výchozí nastavení tak, aby uživatelé mohli používat interní uzel blesku.


Jako správce klikněte na Lightning Wallet v levém panelu nabídek. Server BTCPay vás vyzve k výběru jedné ze dvou možností připojení uzlu Lightning: Interní uzel nebo vlastní externí uzel. Klikněte na možnost "Použít interní uzel" a poté klikněte na tlačítko "Uložit"


#### Správa uzlu Lightning (RTL)


Po připojení k internímu uzlu Lightning se server BTCPay aktualizuje a zobrazí oznámení "BTC Lightning node updated", které potvrzuje, že jste nyní připojili Lightning k vašemu obchodu.


Správa uzlu blesku je úkolem správce serveru. Jedná se o následující činnosti:


- Správa transakce
- Řízení likvidity
  - Příchozí likvidita
  - Odchozí likvidita
- Správa kolegů a kanálů
  - Připojení kolegové
  - Poplatky za kanály
  - Stav kanálu
- Časté zálohování stavů kanálů.
- Kontrola zpráv o směrování
- Můžete také využít služeb, jako je Loop.


Veškerá správa bleskových uzlů probíhá standardně s RTL (za předpokladu, že používáte implementaci LND). Správci mohou kliknout na svůj Lightning Wallet v BTCPay Serveru a najít tlačítko pro otevření RTL. Na hlavním panelu BTCPay Serveru jsou nyní aktualizovány dlaždice Lightning Network, včetně rychlého přístupu k RTL.


### Příklad 2


#### Připojení k blesku s Alby


Majitelé obchodů by si při propojení s úschovnou, jako je Alby, měli nejprve vytvořit účet a navštívit stránku https://getalby.com/


![image](assets/en/036.webp)


Po vytvoření účtu Alby přejděte do obchodu serveru BTCPay.


Krok 1: Klikněte na "Nastavit uzel Lightning" na ovládacím panelu nebo na "Lightning" pod peněženkami.


![image](assets/en/037.webp)


Krok 2: Vložte pověření k připojení Wallet, které vám poskytla společnost Alby. Na ovládacím panelu Alby klikněte na Wallet. Zde najdete položku "Wallet Connection Credentials" (Pověření k připojení Wallet). Zkopírujte tato pověření. Pověření z Alby vložte do pole Konfigurace připojení na serveru BTCPay.


![image](assets/en/038.webp)


Krok 3: Po zadání údajů o připojení serveru BTCPay klikněte na tlačítko "Otestovat připojení", abyste se ujistili, že připojení funguje správně. Všimněte si zprávy "Připojení k bleskovému uzlu proběhlo úspěšně" v horní části obrazovky. To potvrzuje, že vše funguje podle očekávání.


![image](assets/en/039.webp)


Krok 4: Klikněte na tlačítko "Uložit" a váš obchod je nyní připojen k uzlu Lightning od společnosti Alby.


![image](assets/en/040.webp)


**!Poznámka!**


Nikdy nesvěřujte správci řešení Lightning větší hodnotu, než jste ochotni ztratit.


### Shrnutí dovedností


V této části jste se dozvěděli:



- Jak připojit interní nebo externí uzel Lightning
- Obsah a funkce různých dlaždic souvisejících s bleskem na panelu nástrojů
- Jak nakonfigurovat Lightning Wallet pomocí přepětí nebo Alby


### Hodnocení znalostí Praktický přehled


Popište některé z různých možností připojení zařízení Lightning Wallet k vašemu obchodu.


# Server BTCPay Interface


<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>


## Přehled přístrojového panelu


<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>


BTCPay Server je modulární softwarový balíček. Existují však standardy, které musí každý BTCPay Server dodržovat, a tyto standardy řídí interakci mezi správcem a uživateli. Začněme u ovládacího panelu. Hlavní vstupní bod každého serveru BTCPay Server po přihlášení. Dashboard poskytuje přehled o výkonu vašeho obchodu, aktuálním zůstatku Wallet a transakcích za posledních 7 dní. Jelikož se jedná o modulární zobrazení, mohou Pluginy toto zobrazení využít ve svůj prospěch a vytvořit si na Dashboardu vlastní dlaždice. V tomto kurzu se budeme zabývat pouze standardními zásuvnými moduly a aplikacemi spolu s jejich příslušnými zobrazeními v rámci celého serveru BTCPay.


### Dlaždice na přístrojové desce


V hlavním zobrazení ovládacího panelu serveru BTCPay je k dispozici několik standardních dlaždic. Tyto dlaždice jsou určeny pro majitele obchodu nebo správce, aby mohli rychle spravovat svůj obchod v jednom přehledu.



- Bilance Wallet
- Transakční činnost
- Lightning Balance (pokud je Lightning v obchodě povolen)
- Služby Lightning (pokud je služba Lightning v obchodě povolena)
- Nedávné transakce.
- Nedávné faktury
- Aktuální aktivní crowdfundingové fondy
- Výkonnost obchodu / nejprodávanější položky.


### Bilance Wallet


Dlaždice Bilance Wallet poskytuje rychlý přehled o prostředcích a výkonnosti vašeho Wallet. Lze ji zobrazit v měně BTC nebo Fiat v týdenním, měsíčním nebo ročním grafu.


![image](assets/en/041.webp)


### Transakční činnost


Vedle dlaždice Zůstatek Wallet zobrazuje server BTCPay rychlý přehled čekajících výplat, počet transakcí za posledních 7 dní a zda váš obchod vydal nějaké náhrady. Kliknutím na tlačítko Spravovat se dostanete do správy čekajících výplat (více o výplatách se dozvíte v kapitole BTCPay Server - Platby).


![image](assets/en/042.webp)


### Vyvážení blesků


Tato funkce je viditelná pouze tehdy, když je aktivován blesk.


Když správce povolí přístup ke Lightning Network, na panelu BTCPay Server se nyní zobrazí nová dlaždice s informacemi o vašem uzlu Lightning. Kolik BTC je v kanálech, jak je to vyváženo lokálně nebo vzdáleně (příchozí nebo odchozí likvidita), zda se kanály zavírají nebo otevírají a kolik Bitcoin drží On-Chain na uzlu Lightning.


![image](assets/en/043.webp)


### Služby Lightning


Tato funkce je viditelná pouze při aktivním blesku.


Vedle zobrazení zůstatku na účtu Lightning na ovládacím panelu serveru BTCPay uvidí správci také dlaždici pro služby Lightning. Zde správci najdou rychlá tlačítka pro nástroje, které používají ke správě svého uzlu Lightning; například Ride the Lightning je jedním ze standardních nástrojů se serverem BTCPay Server pro správu uzlů Lightning.


![image](assets/en/044.webp)


### Nedávné transakce


Dlaždice Poslední transakce zobrazuje nejnovější transakce vašeho obchodu. Správce instance serveru BTCPay nyní může jedním kliknutím zobrazit poslední transakci a zjistit, zda je třeba jí věnovat pozornost.


![image](assets/en/045.webp)


### Nedávné faktury


Dlaždice Poslední faktury zobrazuje 6 posledních faktur vygenerovaných vaším serverem BTCPay, včetně stavu a částky Invoice. Součástí dlaždice je také tlačítko "Zobrazit vše" pro snadný přístup k úplnému přehledu Invoice.


![image](assets/en/046.webp)


### Prodejní místa a crowdfunding


BTCPay Server poskytuje sadu standardních pluginů nebo aplikací, Point Of Sale a Crowdfund jsou dva hlavní pluginy BTCPay Serveru. S každým obchodem a Wallet může uživatel BTCPay Serveru generate tolik Point Of Sales nebo Crowdfundů, kolik uzná za vhodné. U každého z nich se vytvoří nová dlaždice ovládacího panelu zobrazující výkonnost zásuvných modulů.


![image](assets/en/047.webp)


Všimněte si drobného rozdílu mezi prodejním místem a dlaždicí crowdfundingu. Správce vidí v dlaždici Prodejní místo nejprodávanější položky. V dlaždici Crowdfund se z nich stanou Top výhody. Obě dlaždice mají rychlá tlačítka pro správu příslušné aplikace a zobrazení posledních faktur vytvořených podle nejlepších položek nebo nejlepších perků.


![image](assets/en/048.webp)


**!?Poznámka!?**


Grafy zůstatků a posledních transakcí jsou k dispozici pouze pro platební metody On-Chain. Informace o zůstatcích a transakcích Lightning Network jsou na seznamu úkolů. Od verze 1.6.0 serveru BTCPay jsou k dispozici základní zůstatky Lightning Network.


### Shrnutí dovedností


V této části jste se dozvěděli následující:



- Základní rozvržení dlaždic na hlavní vstupní stránce se nazývá Dashboard.
- Základní znalost obsahu jednotlivých dlaždic.


### Přehled hodnocení znalostí


Vypište z paměti co nejvíce dlaždic z ovládacího panelu.


## BTCPay Server - Nastavení obchodu


<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>


V rámci softwaru BTCPay Server známe dva typy nastavení. Nastavení specifické pro BTCPay Server Store, tlačítko nastavení, které se nachází v levé liště menu pod Dashboardem, a nastavení BTCPay Serveru, které se nachází v dolní části lišty menu, přímo nad Účtem. Nastavení specifická pro server BTCPay Server mohou zobrazit pouze správci serveru.


Nastavení úložiště se skládá z mnoha karet pro kategorizaci jednotlivých sad nastavení.



- Obecné
- Sazby
- Vzhled pokladny
- Přístupové tokeny
- Uživatelé
- Role
- Webové háčky
- Zpracovatelé výplat
- E-maily
- Formuláře


### Obecné


Na kartě Obecná nastavení mohou majitelé obchodů nastavit výchozí nastavení značky a plateb. Při počátečním nastavení obchodu byl zadán název obchodu; ten se promítne do Obecných nastavení v části Název obchodu. Zde může majitel obchodu také nastavit své webové stránky tak, aby odpovídaly brandingu, a ID obchodu, které správce rozpozná v databázi.


#### Branding


Vzhledem k tomu, že BTCPay Server je FOSS, může si majitel obchodu vytvořit vlastní značku, která bude odpovídat jeho obchodu. Nastavte barvu značky, uložte loga své značky a přidejte vlastní CSS pro veřejné/zákaznické stránky (faktury, žádosti o platbu, tahové platby)


#### Platba


V nastavení plateb mohou majitelé obchodů nastavit výchozí měnu svého obchodu (buď Bitcoin, nebo libovolnou fiat měnu).


#### Umožnit komukoli vytvářet faktury


Toto nastavení je určeno pro vývojáře nebo stavitele nad serverem BTCPay. Pokud je toto nastavení pro váš obchod povoleno, umožňuje vnějšímu světu vytvářet faktury na vaší instanci BTCPay Serveru.


#### Přidání dalšího poplatku (síťový poplatek) k fakturám


Funkce v rámci BTCPay, která chrání obchodníky před útoky Dust nebo klienty před pozdějšími vysokými náklady na poplatky, když obchodník potřebuje přesunout velké množství Bitcoin najednou. Například zákazník vytvořil Invoice za 20 USD a zaplatil ji částečně, přičemž 20krát zaplatil 1 USD, dokud nebyla Invoice zcela zaplacena. Obchodník má nyní větší transakci, což zvyšuje náklady na Mining, pokud se obchodník rozhodne přesunout tyto prostředky později. Ve výchozím nastavení BTCPay uplatňuje dodatečné síťové náklady na celkovou částku Invoice, aby pokryla tyto náklady pro obchodníka, pokud je Invoice zaplacena ve více transakcích. BTCPay nabízí několik možností přizpůsobení této ochranné funkce. Můžete použít síťový poplatek:



- Pouze v případě, že zákazník provede více než jednu platbu za Invoice (Ve výše uvedeném příkladu, pokud zákazník vytvořil Invoice za 20\$ a zaplatil 1\$, je nyní celková dlužná částka za Invoice 19\$ + síťový poplatek. Síťový poplatek se uplatní po první platbě)
- Při každé platbě (včetně první platby, v našem případě bude celková částka 20\$ + síťový poplatek hned při první platbě)
- Nikdy nepřidávat síťový poplatek (úplně vypne síťový poplatek)


Chrání sice před transakcemi Dust, ale může se také negativně odrazit na podnikání, pokud není správně komunikováno. Zákazníci mohou mít další otázky a myslet si, že jim účtujete příliš vysoké částky.


#### Invoice pozbývá platnosti, pokud nebyla uhrazena celá částka po?


Časovač Invoice je ve výchozím nastavení nastaven na 15 minut. Časovač slouží jako ochranný mechanismus proti nestálosti, protože blokuje množství Bitcoin podle sazeb Bitcoin-fiat Exchange. Pokud zákazník nezaplatí Invoice ve stanovené lhůtě, považuje se Invoice za prošlý. Invoice je považován za "zaplacený", jakmile je transakce viditelná na Blockchain (s nulovým počtem potvrzení), a je "dokončen", jakmile dosáhne počtu potvrzení, který obchodník definoval (obvykle 1-6). Časovač je nastavitelný po minutách.


#### Považujte Invoice za zaplacený, i když je zaplacená částka o X % nižší, než se očekávalo?


Pokud zákazník použije Exchange Wallet k přímé platbě za Invoice, strhne si Exchange malý poplatek. To znamená, že takový Invoice není považován za zcela dokončený. Invoice je označen jako "částečně zaplacený". Zde můžete nastavit procentní sazbu, pokud chce obchodník přijímat nedoplacené faktury.


### Sazby


Když se na serveru BTCPay vygeneruje Invoice, je vždy potřeba nejaktuálnější a nejpřesnější cena Bitcoin-tofiat. Při vytváření nového obchodu v BTCPay Serveru jsou správci vyzváni k nastavení preferovaného zdroje cen. Po založení obchodu mohou majitelé obchodu na této kartě zdroj cen kdykoli změnit.


#### Pokročilé skriptování pravidel sazby


Používají ji hlavně výkonní uživatelé. Pokud je zapnuto, mohou majitelé obchodů vytvářet skripty týkající se chování cen a způsobu účtování zákazníkům.


#### Testování


Rychlé testovací místo pro vaše preferované měnové páry. Tato funkce zahrnuje také možnost kontroly výchozích měnových párů prostřednictvím dotazu REST.


### Vzhled pokladny


Karta Vzhled pokladny začíná nastavením specifickým pro Invoice a výchozím způsobem platby a po splnění stanovených požadavků povoluje konkrétní způsoby platby.


#### Nastavení Invoice


Výchozí způsoby platby. Server BTCPay ve své standardní konfiguraci nabízí tři možnosti.



- BTC (On-Chain)
- BTC (LNURL-pay)
- BTC (off-chain a Lightning)


Pro náš obchod můžeme nastavit parametry, podle kterých bude zákazník komunikovat se službou Lightning pouze tehdy, když je cena nižší než částka X, a naopak pro transakce On-Chain, když je X větší než Y, vždy se zobrazí možnost platby On-Chain.


![image](assets/en/049.webp)


#### Pokladna


Od verze 1.7 serveru BTCPay byla zavedena nová pokladna Interface, Checkout V2. Vzhledem k tomu, že verze 1.9 byla standardizována, mohou správci a majitelé obchodů stále nastavit pokladnu na předchozí verzi. Pomocí přepínače "Použít klasickou pokladnu" může majitel obchodu vrátit pokladnu do předchozího stavu. Server BTCPay má také vybranou sadu předvoleb pro online obchod nebo pro zkušenost v obchodě.


![image](assets/en/050.webp)


Když zákazník komunikuje s obchodem a vygeneruje Invoice, je pro něj stanovena doba platnosti. Ve výchozím nastavení ji server BTCPay nastavuje na 5 minut a správci ji mohou upravit podle svých preferencí. Stránku pokladny lze dále přizpůsobit zaškrtnutím následujících parametrů:



- Oslavte platbu ukázáním konfet
- Zobrazit záhlaví obchodu (název a logo)
- Zobrazení tlačítka "Zaplatit v Wallet"
- Sjednocení URL/QR plateb On-Chain a off-chain
- Zobrazení částek platby blesku v satoshi
- Automatická detekce jazyka při placení


![image](assets/en/051.webp)


Pokud není nastavena automatická detekce jazyka, server BTCPay ve výchozím nastavení zobrazuje angličtinu. Majitel obchodu může toto výchozí nastavení změnit na svůj preferovaný jazyk.


![image](assets/en/052.webp)


Klikněte na rozevírací seznam a majitelé obchodů mohou nastavit vlastní název HTML, který se zobrazí na stránce pokladny.


![image](assets/en/053.webp)


Aby zákazníci znali svůj způsob platby, může majitel obchodu výslovně nastavit, že u pokladny musí uživatelé vždy zvolit preferovaný způsob platby. Po zaplacení částky Invoice umožní server BTCPay zákazníkovi návrat do internetového obchodu. Majitelé obchodů mohou nastavit, aby se toto přesměrování po zaplacení zákazníkem použilo automaticky.


![image](assets/en/054.webp)


#### Veřejný příjem


V rámci nastavení veřejných účtenek může majitel obchodu nastavit, aby byly stránky účtenek veřejné, a zobrazit tak seznam plateb na stránce účtenky a QR kód, aby se k němu zákazník mohl snadno dostat.


![image](assets/en/055.webp)


### Přístupové tokeny


Přístupové tokeny se používají pro spárování s určitými integracemi elektronického obchodu nebo integracemi vytvořenými na zakázku.


![image](assets/en/056.webp)


### Uživatelé


Uživatelé obchodu jsou místem, kde může majitel obchodu spravovat své zaměstnance, jejich účty a přístup do obchodu. Poté, co si zaměstnanci vytvoří své účty, může majitel obchodu přidat konkrétní uživatele do obchodu jako uživatele hosty nebo vlastníky. Chcete-li blíže definovat roli zaměstnance, přečtěte si další část "Nastavení obchodu na serveru BTCPay - Role"


![image](assets/en/057.webp)


### Role


Majitel obchodu nemusí považovat standardní role uživatele za dostatečně významné. V nastavení vlastních rolí může majitel obchodu přesně definovat potřeby jednotlivých rolí ve svém podniku.


(1) Chcete-li vytvořit novou roli, klikněte na tlačítko "+ Přidat roli".


![image](assets/en/058.webp)


(2) Zadejte název role, například "Cashier".


![image](assets/en/059.webp)


(3) Nakonfigurujte jednotlivá oprávnění role.



- Upravte své obchody.
- Správa účtů Exchange propojených s vašimi obchody.
  - Zobrazení účtů Exchange propojených s vašimi obchody.
- Spravujte platby za tahání.
- Vytvoření tahových plateb.
  - Vytvoření neschválených plateb čerpání.
- Úprava faktur.
  - Zobrazení faktur.
  - Vytvořte položku Invoice.
  - Vytvářejte faktury z bleskových uzlů přidružených k vašim obchodům.
- Prohlédněte si své obchody.
  - Zobrazení faktur.
  - Zobrazení žádostí o platbu.
  - Úprava webových háčků obchodů.
- Upravte své žádosti o platbu.
  - Zobrazení žádostí o platbu.
- Použijte bleskové uzly spojené s vašimi obchody.
  - Zobrazení bleskových faktur spojených s vašimi obchody.
  - Vytvářejte faktury z bleskových uzlů přidružených k vašim obchodům.
- Vkládání prostředků na účty Exchange propojené s vašimi obchody.
- Výběr prostředků z účtů Exchange do vašeho obchodu.
- Obchodování s prostředky na účtech Exchange vašeho obchodu.


Když je role vytvořena, je její název pevně nastaven a nelze jej měnit poté, co je v režimu úprav.


![image](assets/en/060.webp)


### Webové háčky


V rámci serveru BTCPay je poměrně snadné vytvořit nový "Webhook". V nastavení obchodu BTCPay Server - záložka Webhook může majitel obchodu snadno vytvořit nový webhook kliknutím na "+ Vytvořit webhook". Webhooky umožňují serveru BTCPay Server odesílat události HTTP související s vaším obchodem na jiné servery nebo integrace elektronických obchodů.


![image](assets/en/061.webp)


Nyní jste v zobrazení pro vytvoření webového háčku. Ujistěte se, že znáte adresu URL Payloadu, a vložte ji do serveru BTCPay. Zatímco jste vložili adresu URL payloadu, pod ní se zobrazuje tajemství webhooku. Zkopírujte tajemství webhooku a zadejte ho na koncovém bodě. Když je vše nastaveno, můžete v BTCPay Serveru přepnout na "Automatické opětovné doručení" BTCPay Server se pokusí znovu doručit jakékoli neúspěšné doručení po 10 sekundách, 1 minutě a až 6krát po 10 minutách. Můžete přepínat mezi každou událostí nebo určit události podle svých potřeb. Nezapomeňte webový háček povolit a stisknutím tlačítka "Add webhook" jej uložit.


![image](assets/en/062.webp)


Webhooks nejsou kompatibilní s rozhraním API služby Bitpay. V BTCPay Serveru existují dvě samostatná IPN (v terminologii BitPay: "Oznámení o okamžité platbě").



- Webhookp
- Oznámení


Při vytváření faktur prostřednictvím rozhraní API služby Bitpay používejte pouze adresu URL oznámení.


### Zpracovatelé výplat


Zpracovatelé výplat spolupracují s konceptem výplat na serveru BTCPay. Agregátor výplat, který umožňuje dávkovat více transakcí a odesílat je najednou. Pomocí procesorů výplat může majitel obchodu automatizovat dávkové výplaty. BTCPay Server nabízí dva způsoby automatizovaných výplat: On-Chain a off-chain (LN).


Majitel obchodu může kliknout a nakonfigurovat oba výplatní procesory samostatně. Majitel obchodu může chtít spustit procesor On-Chain pouze jednou za X hodin, zatímco procesor off-chain se může spouštět každých několik minut. Pro procesor On-Chain lze také nastavit cíl, do kterého bloku má být zařazen. Ve výchozím nastavení je tato hodnota nastavena na 1 (nebo na nejbližší dostupný blok). Všimněte si, že nastavení procesoru výplaty off-chain má pouze časovač intervalu a žádný cíl bloku. Výplaty Lightning Network jsou okamžité.


![image](assets/en/063.webp)

![image](assets/en/064.webp)


Majitelé prodejen mohou konfigurovat procesor On-Chain pouze v případě, že mají k prodejně připojený procesor Hot Wallet.


![image](assets/en/065.webp)


Po nastavení procesoru výplaty jej můžete rychle odebrat nebo upravit, když se vrátíte na kartu Procesor výplaty v nastavení obchodu BTCPay Server.


**Poznámka**


Procesor výplat On-Chain - Procesor výplat On-Chain může pracovat pouze v obchodě nakonfigurovaném s připojeným Hot Wallet. Pokud není připojen žádný Hot Wallet, server BTCPay nemá klíče Wallet a nebude moci automaticky zpracovávat výplaty.


### E-maily


Server BTCPay může používat e-maily pro oznámení nebo, pokud jsou správně nastaveny, pro obnovení účtů vytvořených v instanci. Standardně BTCPay Server neodesílá e-mail například při ztrátě hesla.


![image](assets/en/066.webp)


Než může majitel obchodu nastavit pravidla e-mailu pro spouštění konkrétních událostí ve svém obchodě, musí nejprve nastavit základní nastavení e-mailu. Server BTCPay vyžaduje tato nastavení k odesílání e-mailů pro události související s vaším obchodem nebo pro obnovení hesla.


Server BTCPay usnadnil vyplnění těchto informací pomocí možnosti "Rychlé vyplnění":



- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid


Při použití možnosti rychlého vyplnění BTCPay Server předvyplní pole pro server SMTP a port. Nyní musí majitel obchodu vyplnit pouze své přihlašovací údaje, včetně e-mailu Address, přihlašovacího jména (které se obvykle rovná vašemu e-mailu Address) a hesla. Pokročilou možností v nastavení e-mailu serveru BTCPay je možnost Zakázat bezpečnostní kontroly certifikátu TLS; ve výchozím nastavení je tato možnost povolena.


![image](assets/en/067.webp)


Pomocí pravidel pro e-maily může majitel obchodu nastavit konkrétní události, které spustí zasílání e-mailů na konkrétní e-mailové adresy.



- Invoice Vytvořeno
- Invoice Přijatá platba
- Zpracování Invoice
- Invoice Vypršela platnost
- Invoice Vypořádáno
- Invoice Neplatný
- Invoice Vyrovnaná platba


Pokud zákazník zadal e-mailovou adresu Address, mohou tyto spouštěče odeslat informace také zákazníkovi. Majitelé obchodů mohou předvyplnit řádek Předmětu, aby bylo jasné, proč k tomuto E-mailu došlo a co jej spustilo.


![image](assets/en/068.webp)


### Formuláře


Vzhledem k tomu, že server BTCPay neshromažďuje žádné údaje, může majitel obchodu chtít přidat do pokladny vlastní formulář; tímto způsobem může majitel obchodu shromažďovat další informace od svých zákazníků. Nástroj pro tvorbu formulářů BTCPay Serveru se skládá ze dvou částí: vizuálního a pokročilejšího zobrazení kódu formulářů.


Při vytváření nového formuláře otevře server BTCPay nové okno, ve kterém si vyžádá základní informace o tom, na co se má nový formulář ptát. Nejprve musí majitel obchodu zadat jasný název svého nového formuláře; tento název nelze po jeho nastavení měnit.


![image](assets/en/069.webp)


Poté, co majitel obchodu zadá formuláři název, můžete také přepnout přepínač "Povolit formulář pro veřejné použití" do polohy ON, čímž se změní na Green. Tím zajistíte, že se formulář bude používat na všech místech, kde se setkávají se zákazníky. Pokud například majitel obchodu vytvoří samostatný formulář Invoice nikoli prostřednictvím prodejního místa, může chtít i přesto shromažďovat informace od zákazníka. Tento přepínač umožňuje tyto informace shromažďovat.


![image](assets/en/070.webp)


Každý formulář začíná alespoň 1 novým formulářovým polem. Majitel obchodu si může vybrat, jaký typ pole to má být.



- Text
- Číslo
- Heslo
- E-mail
- ADRESA URL
- Telefonní čísla
- Datum
- Skrytá pole
- Sada polí
- Textová oblast pro otevřené komentáře.
- Výběr možností


Každý typ má své parametry, které je třeba vyplnit. Majitel obchodu si je může nastavit podle svých představ. Pod prvním vytvořeným polem mohou majitelé obchodů do tohoto formuláře přidávat nová pole.


![image](assets/en/071.webp)


#### Pokročilé vlastní formuláře


BTCPay Server také umožňuje vytvářet formuláře v kódu. Zejména JSON. Místo toho, aby se majitelé obchodů dívali do editoru, mohou kliknout na tlačítko CODE hned vedle editoru a dostat se do kódu svých Formulářů. V definici pole lze nastavit pouze následující pole; hodnoty polí jsou uloženy v metadatech Invoice:


| Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant      | If true, the .value must be set in the form definition, and the user will not be able to change the field's value. ( example: the form definition's version)                                                                                                                                                                                                                                                                                                       |
| .fields.type          | The HTML input type text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel                                                                                                                                                                                                                                                                                                |
| .fields.options       | If .fields.type is select, the list of selectable values                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.options.text  | The text displayed for this option                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.options.value | The value of the field if this option is selected                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.type=fieldset | Create a HTML fieldset around the children .fields.fields (see below)                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.name          | The JSON property name of the field as it will appear in the invoice's metadata                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.value         | The default value of the field                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.required      | if true, the field will be required                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .fields.label         | The label of the field                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| .fields.helpText      | Additional text to provide an explanation for the field.                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.fields        | You can organize your fields in a hierarchy, allowing child fields to be nested within the invoice’s metadata. This structure can help you better organize and manage the collected information, making it easier to access and interpret. For example, if you have a form that collects customer information, you can group the fields under a parent field called customer. Within this parent field, you might have child fields like name, Email, and address. |

Název pole představuje název vlastnosti JSON, která ukládá hodnotu zadanou uživatelem do metadat modulu Invoice. Některé dobře známé názvy lze interpretovat a upravit tak, aby bylo možné upravit nastavení zařízení Invoice.


| Field name       | Description            |
| ---------------- | ---------------------- |
| invoice_amount   | The invoice's amount   |
| invoice_currency | The invoice's currency |

Pole formuláře Invoice můžete předvyplnit automaticky přidáním řetězců dotazů do adresy URL formuláře, například "?your_field=value".


Zde je několik případů použití této funkce:



- Asistence při zadávání údajů uživatelem: Předvyplňte pole známými informacemi o zákazníkovi, abyste mu usnadnili vyplnění formuláře. Například pokud již znáte e-mail zákazníka Address, můžete předvyplnit pole e-mailu a ušetřit mu tak čas.
- Personalizace: Přizpůsobení formuláře na základě preferencí nebo segmentace zákazníků. Máte-li například různé úrovně zákazníků, můžete formulář předvyplnit relevantními údaji, jako je úroveň jejich členství nebo konkrétní nabídky.
- Sledování: Sledování zdroje návštěv zákazníků pomocí skrytých polí a předvyplněných hodnot. Můžete například vytvořit odkazy s předvyplněnými hodnotami utm_media pro každý marketingový kanál (např. Twitter, Facebook, E-mail). To vám pomůže analyzovat účinnost marketingového úsilí.
- A/B testování: Předvyplňte pole různými hodnotami a otestujte různé verze formuláře, což vám umožní optimalizovat uživatelskou zkušenost a míru konverze.


### Shrnutí dovedností


V této části jste se dozvěděli následující:



- Rozložení a funkce karet v Nastavení obchodu
- Množství možností pro jemné doladění zpracování podkladových sazeb Exchange, částečných plateb, mírných nedoplatků a dalších.
- Přizpůsobení vzhledu pokladny, včetně závislosti na ceně hlavního řetězce vs. povolení Lightning na fakturách.
- Správa úrovní přístupu k úložišti a oprávnění napříč rolemi.
- Konfigurace automatických e-mailů a jejich spouštěčů
- Vytvářejte vlastní formuláře pro shromažďování dalších informací o zákaznících při placení.


### Hodnocení znalostí


#### KA Review


Jaký je rozdíl mezi Nastavením úložiště a Nastavením serveru?


#### Hypotetické KA


Popište některé možnosti, které můžete vybrat v nabídce Vzhled pokladny > Nastavení Invoice, a proč.


## BTCPay Server - Nastavení serveru


<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>


Server BTCPay se skládá ze dvou různých zobrazení nastavení. Jeden je věnován nastavení obchodu a druhý nastavení serveru. Druhé z nich je dostupné pouze správcům serveru, nikoliv majitelům obchodů. Správci serveru mohou přidávat uživatele, vytvářet vlastní role, konfigurovat e-mailový server, nastavovat zásady, spouštět úlohy údržby, kontrolovat všechny služby připojené k serveru BTCPay Server, nahrávat na server soubory nebo kontrolovat protokoly.


### Uživatelé


Jak bylo uvedeno v předchozí části, správci serveru mohou pozvat uživatele na svůj server tak, že je přidají na kartu Uživatelé.


### Vlastní role pro celý server


Server BTCPay má dva typy vlastních rolí: vlastní role pro konkrétní obchod a vlastní role pro celý server v nastavení serveru BTCPay. Obě obsahují podobnou sadu oprávnění; pokud je však nastavíte prostřednictvím záložky Nastavení serveru BTCpay - Role, bude použitá role platit pro celý server a bude se vztahovat na více obchodů. Všimněte si příznaku "Server-wide" u vlastních rolí v nastavení serveru.


![image](assets/en/072.webp)


### Vlastní role pro celý server


Nastavení oprávnění vlastních rolí pro celý server;



- Upravte své obchody.
- Správa účtů Exchange propojených s vašimi obchody.
  - Zobrazení účtů Exchange propojených s vašimi obchody.
- Spravujte platby za tahání.
- Vytvoření tahových plateb.
  - Vytvoření neschválených plateb čerpání.
- Úprava faktur.
  - Zobrazení faktur.
  - Vytvořit Invoice.
  - Vytvářejte faktury z bleskových uzlů přidružených k vašim obchodům.
- Prohlédněte si své obchody.
  - Zobrazení faktur.
  - Zobrazení žádostí o platbu.
  - Úprava webových háčků obchodů.
- Upravte své žádosti o platbu.
  - Zobrazení žádostí o platbu.
- Použijte bleskové uzly spojené s vašimi obchody.
  - Zobrazení bleskových faktur spojených s vašimi obchody.
  - Vytvářejte faktury z bleskových uzlů přidružených k vašim obchodům.
- Vkládání prostředků na účty Exchange propojené s vašimi obchody.
- Výběr prostředků z účtů Exchange do vašeho obchodu.
- Obchodování s prostředky na účtech Exchange vašeho obchodu.


**!?Poznámka!?**


Když je role vytvořena, je její název pevně nastaven a nelze jej měnit poté, co je v režimu úprav.


### E-mail


Nastavení e-mailu pro celý server vypadá podobně jako nastavení e-mailu pro konkrétní obchod. Toto nastavení však zpracovává nejen spouštěče pro obchody nebo protokoly správce, ale také spouštěče pro jiné události. Toto nastavení E-mailu také zpřístupňuje obnovu hesla na serveru BTCPay při přihlášení. Funguje podobně jako nastavení specifické pro Store; správci mohou rychle vyplnit parametry E-mailu a zadat své e-mailové přihlašovací údaje, čímž serveru umožní odesílat e-maily.


![image](assets/en/073.webp)


### Zásady


Správci zásad serveru BTCPay mohou nastavit různá nastavení v tématech, jako jsou nastavení stávajících uživatelů, nastavení nových uživatelů, nastavení oznámení a nastavení údržby. Ta jsou určena pro registraci nových uživatelů jako správců nebo běžných uživatelů nebo pro skrytí serveru BTCPay před vyhledávači přidáním do hlavičky serveru.


![image](assets/en/074.webp)


#### Nastavení stávajícího uživatele


Možnosti, které jsou zde k dispozici, jsou oddělené od vlastních rolí. Tato dodatečná oprávnění mohou způsobit, že úložiště nebo jeho vlastník budou zranitelní vůči útokům. Zásady, které lze přidat stávajícím uživatelům:



- Povolit neadminům používat interní uzel Lightning v jejich úložištích.
  - To by umožnilo majitelům obchodů používat uzel Lightning správce serveru, a tedy i jeho finanční prostředky! Pozor, nejedná se o řešení, které by umožňovalo přístup k Lightningu.
- Umožnit neadministrátorům vytvářet peněženky Hot pro své sklady.
  - To by umožnilo komukoli s účtem na vaší instanci serveru BTCPay vytvářet peněženky Hot a ukládat jejich obnovení seed na serveru správce. Tím by mohl Správce nést odpovědnost za držení prostředků třetích stran!
- Umožnit neadministrátorům importovat peněženky Hot do svých obchodů.
  - Podobně jako v předchozím tématu vytváření peněženek Hot umožňuje tato zásada importovat peněženku Hot Wallet se stejnými nebezpečími, která byla zmíněna v části o vytváření peněženek Hot.


![image](assets/en/075.webp)


#### Nastavení nového uživatele


Můžeme nastavit některá důležitá nastavení pro správu nových uživatelů přicházejících na server. Můžeme nastavit potvrzovací e-mail pro nové registrace, zakázat vytváření nových uživatelů prostřednictvím přihlašovací obrazovky a omezit přístup neadminů k vytváření uživatelů přes rozhraní API.



- Vyžadujte potvrzovací e-mail pro registraci.
  - Správce serveru musí mít nastaven e-mailový server.
- Zakázat registraci nových uživatelů na serveru
- Zakázat přístup neadminů ke koncovému bodu API pro vytváření uživatelů.


Ve výchozím nastavení má server BTCPay přepínač "Zakázat registraci nových uživatelů na serveru" a vypíná přístup neadminů ke koncovému bodu API pro vytváření uživatelů. Je to z důvodu bezpečnosti, aby náhodní lidé, kteří narazí na vaše přihlášení k BTCPay, nemohli vytvářet účty.


![image](assets/en/076.webp)


#### Nastavení oznámení


![image](assets/en/077.webp)


#### Nastavení údržby


BTCPay Server je open source projekt na GitHubu. Kdykoli BTCPay Server vydá novou verzi softwaru, mohou být administrátoři upozorněni, že je k dispozici nová verze. Správci mohou také chtít zabránit vyhledávačům (jako je Google, Yahoo a DuckDuckGo) v indexování domény BTCPay Server. Vzhledem k tomu, že BTCPay Server je FOSS, mohou vývojáři po celém světě chtít vytvářet nové funkce. BTCPay Server má experimentální funkci, která po zapnutí umožňuje správcům používat funkce, které nejsou určeny pro produkční, ale spíše pro testovací účely.



- Kontrolujte vydání na GitHubu a upozorněte na dostupnost nové verze BTCPay Serveru.
- Odradit vyhledávače od indexování tohoto webu
- Povolení experimentálních funkcí.


![image](assets/en/078.webp)


#### Zásuvné moduly


Server BTCPay může přidávat zásuvné moduly a rozšiřovat svou sadu funkcí. Zásuvné moduly se ve výchozím nastavení načítají z repozitáře BTCPay Server plugin-builder. Správce se však může rozhodnout, že chce vidět zásuvné moduly ve stavu Pre-release, a pokud to vývojář zásuvného modulu povolí, může nyní správce serveru instalovat beta verze zásuvných modulů.


![image](assets/en/079.webp)


##### Nastavení přizpůsobení


Standardní nasazení serveru BTCPay bude přístupné prostřednictvím domény nastavené během instalace. Správce serveru však může přemapovat kořenovou doménu a zobrazit jednu z vytvořených aplikací z konkrétního obchodu. Správce serveru může také namapovat konkrétní domény na konkrétní aplikace.



- Zobrazení aplikace v kořenovém adresáři webu
  - Zobrazí seznam možných aplikací, které se mají zobrazit v kořenové doméně.


![image](assets/en/080.webp)



- Mapování konkrétních domén na konkrétní aplikace.
  - Po kliknutí na možnost nastavit konkrétní doménu pro konkrétní aplikace může správce nastavit libovolný počet domén, které ukazují na konkrétní aplikace.


![image](assets/en/081.webp)


#### Průzkumníci bloků


Server BTCPay je standardně dodáván s Mempool.space jako jeho Block explorer pro transakce. Když BTCPay Server vygeneruje nový Invoice a je k němu vázána transakce, může majitel obchodu kliknutím otevřít transakci. BTCPay Server bude ve výchozím nastavení směřovat na Mempool.space jako na Block explorer; správce serveru však může tuto možnost změnit na jím preferovanou.


![image](assets/en/082.webp)


### Služby


"Nastavení serveru BTCPay: Na kartě "Služby" je přehled komponent, které váš BTCPay Server používá. Služby, které váš BTCPay Server vystavuje, se mohou lišit v závislosti na způsobu nasazení.


Správce serveru BTCPay může kliknout na "Zobrazit informace" za každou službou, aby ji otevřel a nastavil konkrétní nastavení.


![image](assets/en/083.webp)


#### LND (gRPC)


BTCPay zpřístupňuje službu GRPC LND pro externí spotřebu; informace o připojení najdete v tomto specifickém menu nastavení; kompatibilní peněženky jsou uvedeny zde. Server BTCPay také poskytuje QR kód pro připojení, který lze naskenovat a použít v mobilním zařízení Wallet.


Správci serverů mohou otevřít další podrobnosti a zobrazit je.



- Podrobnosti o hostiteli
- Použití protokolu SSL
- Makronky
- AdminMacaroon
- FakturaMacaroon
- ReadonlyMacaroon
- Sada šifrátorů GRPC SSL (GRPC_SSL_CIPHER_SUITES)


#### LND (REST)


BTCPay vystavuje službu REST LND pro externí použití; informace o připojení najdete zde; kompatibilní peněženky jsou uvedeny zde. Mezi kompatibilní peněženky patří Joule, Alby a ZeusLN. Server BTCPay poskytuje pro připojení QR kód, který lze naskenovat a použít v kompatibilní peněžence Wallet.



- REST URI
- Makronky
- AdminMacaroon
- FakturaMacaroon
- ReadonlyMacaroon


#### LND seed Záloha


Záloha LND seed je užitečná pro obnovení prostředků z vašeho LND Wallet v případě poškození serveru. Vzhledem k tomu, že uzel Lightning je Hot-Wallet, najdete důvěrné informace o seed na této stránce.


LND dokumentuje proces obnovy. Dokumentaci naleznete na adrese https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md.


#### Jízda na blesku


Ride the Lightning je nástroj pro správu uzlů Lightning vytvořený jako software s otevřeným zdrojovým kódem. BTCPay Server používá RTL jako komponentu pro správu uzlů Lightning ve svém zásobníku. Správci serveru BTCPay Server se k RTL dostanou prostřednictvím nastavení serveru - záložka Služby nebo kliknutím na Lightning Wallet.


#### Full node P2P


Správci serverů mohou chtít připojit svůj uzel Bitcoin k mobilnímu uzlu Wallet. Na této stránce naleznete informace o tom, jak se vzdáleně připojit ke Full node prostřednictvím protokolu P2P. V době psaní tohoto kurzu uvádí BTCPay Server jako kompatibilní peněženky Blockstream Green a Wasabi. BTCPay Server poskytuje QR kód pro připojení, který lze naskenovat a použít v kompatibilní peněžence Wallet.


#### Full node RPC


Na této stránce jsou k dispozici informace pro vzdálené připojení k zařízení Full node prostřednictvím protokolu RPC.


#### SSH


SSH se používá pro účely údržby. Server BTCPay zobrazuje počáteční příkaz pro připojení k vašemu serveru a veřejné klíče SSH oprávněné k připojení k vašemu serveru. Správci serveru mohou chtít zakázat změny SSH prostřednictvím uživatelského rozhraní BTCPay Serveru.


#### Dynamický systém DNS


Dynamický systém DNS umožňuje mít stabilní název DNS směřující na váš server, i když se vaše IP adresa Address pravidelně mění. To se doporučuje, pokud hostujete BTCPay Server doma a chcete mít pro přístup na svůj Server doménu clearnet.


Upozorňujeme, že pro získání certifikátu HTTPS je třeba správně nakonfigurovat NAT a instalaci serveru BTCPay.


### Téma


BTCPay Server je standardně dodáván se dvěma motivy: Světlý a tmavý režim. Ty lze přepínat kliknutím na Účet v levém dolním rohu a přepínáním mezi Tmavým a Světlým tématem. Správci serveru BTCPay Server mohou přidat vlastní téma zadáním vlastního tématu CSS.


Správci mohou téma Light/Dark rozšířit přidáním vlastního CSS nebo nastavením vlastního tématu jako plně vlastního.


![image](assets/en/084.webp)


#### Značení serveru


Správci serveru mohou změnit značku serveru BTCPay nastavením značky vaší společnosti pro celý server. Vzhledem k tomu, že BTCPay Server je FOSS, mohou správci serverů software označit bílým štítkem a přizpůsobit jeho vzhled tak, aby vyhovoval jejich podnikání.


![image](assets/en/085.webp)


### Údržba


Uživatelé od vás jako správce serveru očekávají, že se o server budete dobře starat. V záložce Údržba serveru BTCPay může správce provádět základní údržbu. Nastavit název domény na instanci BTCPay Serveru, Restartovat nebo vyčistit Server. Pravděpodobně nejdůležitější je spustit aktualizace.


BTCPay Server je open source projekt a často se aktualizuje. Každá nová verze je oznámena buď prostřednictvím oznámení BTCPay Serveru, nebo na oficiálních kanálech, přes které BTCPay Server komunikuje.


![image](assets/en/086.webp)


#### Název domény


Po nastavení serveru BTCPay může správce chtít změnit původní doménu. Na kartě Údržba může správce změnit Doménu. Po kliknutí na tlačítko potvrdit a nastavení správných záznamů DNS na Doméně se BTCPay Server aktualizuje a restartuje, aby se vrátil na novou Doménu.


![image](assets/en/087.webp)


#### Restartování


Restartujte server BTCPay a související služby.


![image](assets/en/088.webp)


#### Clean


BTCPay Server běží s komponentami Docker; při aktualizacích se mohou objevit zbytky obrazů Docker, dočasné soubory atd. Správci serveru mohou uvolnit místo spuštěním skriptu Clean.


![image](assets/en/089.webp)


#### Aktualizace


Je to nejdůležitější možnost na kartě Údržba. BTCPay Server je vytvořen komunitou, a proto jsou jeho aktualizační cykly častější než u většiny softwarových produktů. Jakmile se na BTCPay Serveru objeví nová verze, správci o tom budou informováni ve svém centru oznámení. Kliknutím na tlačítko aktualizace BTCPay Server zkontroluje GitHub, zda neobsahuje nejnovější verzi, aktualizuje Server a restartuje se. Správcům serveru vždy doporučujeme, aby si před aktualizací přečetli poznámky k vydání distribuované prostřednictvím oficiálních kanálů BTCPay Serveru.


![image](assets/en/090.webp)


### Protokoly


Čelit problému není nikdy zábava. Tento dokument popisuje nejběžnější pracovní postupy a kroky, které vám pomohou efektivně identifikovat a vyřešit problém, ať už samostatně, nebo s pomocí komunity.


Zásadní je identifikace problému.


#### Replikace problému


Především se snažte zjistit, kdy k problému dochází. Pokuste se problém zopakovat. Zkuste aktualizovat a restartovat server, abyste ověřili, zda můžete problém reprodukovat. Pokud to lépe popisuje váš problém, pořiďte snímek obrazovky.


##### Aktualizace serveru


Zkontrolujte svou verzi BTCPay Serveru, pokud je mnohem starší než [nejnovější verze](https://github.com/btcpayserver/btcpayserver/releases) BTCPay Serveru. Aktualizace vašeho Serveru může problém vyřešit.


##### Restartování serveru


Restartování serveru je snadný způsob, jak vyřešit mnoho nejčastějších problémů se serverem BTCPay. Možná budete muset do svého Serveru vstoupit přes SSH, abyste jej mohli restartovat.


##### Restartování služby


V některých případech může být nutné restartovat pouze určitou službu v nasazení BTCPay Serveru, například restartovat kontejner letsencrypt kvůli obnovení certifikátu SSL.


```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```


Pomocí nástroje docker ps zjistěte název jiné služby, kterou chcete restartovat.


#### Prohlížení protokolů


Protokoly mohou poskytnout zásadní informace. V následujících odstavcích popíšeme, jak získat informace z logů pro různé části BTCPay.


##### Záznamy BTCPay


Od verze 1.0.3.8 můžete snadno přistupovat k protokolům serveru BTCPay z předního panelu. Jste-li správcem serveru, přejděte do Nastavení serveru > Protokoly a otevřete soubor s protokoly. Pokud nevíte, co konkrétní chyba v protokolech znamená, uveďte ji při řešení problémů.


Pokud chcete podrobnější protokoly a používáte nasazení Docker, můžete si zobrazit protokoly konkrétních kontejnerů Docker pomocí příkazového řádku. Viz tyto [pokyny pro ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) do instance BTCPay běžící na VPS.


Na další stránce je obecný seznam názvů kontejnerů používaných pro server BTCPay.


Chcete-li vytisknout protokoly podle názvu kontejneru, spusťte níže uvedené příkazy. Chcete-li zobrazit protokoly ostatních kontejnerů, nahraďte název kontejneru.


```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```


| Logs for     | Container Name                    |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker


Při použití nástroje Docker můžete k protokolům LND přistupovat několika způsoby. Nejprve se přihlaste jako root:


```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```


Alternativně můžete rychle vytisknout protokoly pomocí ID kontejneru (jsou potřeba pouze první jedinečné znaky ID, například dva nejvzdálenější znaky vlevo):


```bash
docker logs 'add your container ID'
```


Pokud z jakéhokoli důvodu potřebujete více protokolů


```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```


Zobrazí se něco jako


```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```


Chcete-li získat přístup k nekomprimovaným protokolům těchto protokolů, proveďte `cat LND.log`, nebo chcete-li jiný protokol, použijte `cat LND.log.15`.


Pro přístup ke komprimovaným protokolům ve formátu `.gzip` použijte příkaz `gzip -d LND.log.16.gz` (v tomto případě přistupujeme k souboru `LND.log.16.gz`). Tím byste měli získat nový soubor, ve kterém můžete provést `cat LND.log.16`. V případě, že výše uvedený postup nefunguje, může být nutné nejprve nainstalovat gzip pomocí `sudo apt-get install gzip`.


###### Lightning Network c-lightning - Docker


```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```


Případně použijte tuto možnost:


```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```


Informace o protokolu můžete získat také pomocí příkazu c-lightning CLI.


```bash
bitcoin-lightning-cli.sh getlog
```


#### Protokoly uzlu Bitcoin


Kromě [prohlížení protokolů](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) kontejneru bitcoind můžete také použít některý z příkazů [bitcoin-cli](https://developer.Bitcoin.org/reference/RPC/index.html)


[(otevře se nové okno)](https://developer.Bitcoin.org/reference/RPC/index.html) a získáte informace z uzlu Bitcoin. BTCPay obsahuje skript, který vám umožní snadno komunikovat s vaším uzlem Bitcoin.


Ve složce btcpayserver-docker získejte informace o Blockchain pomocí svého uzlu:


```bash
bitcoin-cli.sh getblockchaininfo
```


### Soubory


Server BTCPay je vybaven místním souborovým systémem, který umožňuje nahrávat aktiva obchodu (produktu), loga a značky přímo na server. Souborový systém serveru je přístupný pouze správcům serveru; majitelé obchodů mohou nahrávat svá loga nebo branding na úrovni obchodu.


Když se správce serveru nachází na kartě Úložiště souborů, je možné nahrávat přímo na server nebo změnit poskytovatele úložiště souborů na místní souborový systém nebo Azure Blob Storage.


![image](assets/en/091.webp)


![image](assets/en/092.webp)


### Shrnutí dovedností


V této části jste se dozvěděli následující:



- Rozdíl mezi nastavením úložiště a serveru, zejména pokud jde o uživatele, role a e-maily
- Nastavení zásad pro celý server pro používání a vytváření blesků nebo Bitcoin Hot Wallet, registraci nových uživatelů a e-mailová oznámení.
- Jak přidat vlastní motivy (namísto jednoduchých světlých/tmavých možností) a vytvořit vlastní loga
- Provádění jednoduchých úkolů údržby serveru prostřednictvím poskytnutého grafického uživatelského rozhraní
- Řešení problémů, včetně načítání podrobností o kontejnerech Docker nebo uzlu
- Správa ukládání souborů


### Hodnocení znalostí


#### Koncepční přezkum KA


Jaký je rozdíl v rolích přiřazených prostřednictvím nastavení serveru a nastavení úložiště a jaké je potenciální použití jedné z nich oproti druhé?


#### KA Praktický přehled


Popište některé možné případy použití povolené na kartě Zásady.


#### KA Praktický přehled


Popište některé akce, které může správce běžně provádět na kartě Údržba.


## Server BTCPay - Platby


<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>


Invoice je doklad, který prodávající vystavuje kupujícímu za účelem inkasa platby.


V BTCPay Serveru představuje Invoice doklad, který musí být uhrazen v definovaném časovém intervalu za pevnou sazbu Exchange. Faktury mají datum expirace, protože fixují kurz Exchange ve stanoveném časovém rámci, čímž chrání příjemce před kolísáním ceny.


Základem BTCPay Serveru je schopnost fungovat jako systém správy Bitcoin Invoice. Systém Invoice je základním nástrojem pro sledování a správu přijatých plateb.


Pokud nepoužíváte vestavěný [Wallet](https://docs.btcpayserver.org/Wallet/) pro ruční příjem plateb, budou všechny platby v rámci obchodu zobrazeny na stránce Faktury. Tato stránka kumulativně třídí platby podle data a slouží jako centrální zdroj pro správu Invoice a řešení problémů s platbami.


![image](assets/en/093.webp)


### Obecné


#### Stavy Invoice


V následující tabulce jsou uvedeny a popsány standardní stavy Invoice v BTCPay spolu s navrhovanými běžnými kroky. Akce jsou pouze doporučení. Je na uživatelích, aby definovali nejlepší postup pro svůj případ použití a podnikání.


| Invoice Status             | Description                                                                                                                             | Action                                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| New                        | Not paid, invoice timer still has not expired                                                                                           | None                                                                                                                        |
| New (paidPartial)          | Paid, not in full, invoice timer still has not expired                                                                                  | None                                                                                                                        |
| Expired                    | Not paid, invoice timer expired                                                                                                         | None                                                                                                                        |
| Expired (paidPartial) \*\* | Paid, not in full amount, and expired                                                                                                   | Contact buyer to arrange a refund or ask for them to pay their due. Optionally mark the invoice as settled or invalid           |
| Expired (paidLate)         | Paid, in full amount, after the invoice timer has expired                                                                               | Contact buyer to arrange a refund or process order if late confirmations are acceptable.                                    |
| Settled (paidOver)         | Paid more than the invoice amount, settled, received sufficient amount of confirmations                                                 | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing                 | Paid in full, but has not received sufficient amount of confirmations specified in the store settings                                   | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing (paidOver)      | Paid more than the invoice amount, not received sufficient amount of confirmations                                                      | Wait to be settled, then contact the  buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you |
| Settled                    | Paid, in full, received sufficient amount of confirmations in store                                                                     | Fulfil the order                                                                                                            |
| Settled (marked)           | Status was manually changed to settled from a processing or invalid status                                                             | Store admin has marked the payment as settled                                                                               |
| Invalid\*                  | Paid, but failed to receive sufficient amount of confirmations within the time specified in store settings                              | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |
| Invalid (marked)           | Status was manually changed to invalid from a settled or expired status                                                                 | Store admin has marked the payment as invalid                                                                               |
| Invalid (paidOver)         | Paid more than the invoice amount, but failed to receive sufficient amount of confirmations within the time specified in store settings | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |

#### Podrobnosti o Invoice


Stránka s podrobnostmi o Invoice obsahuje všechny informace týkající se Invoice.


Informace o Invoice se vytvářejí automaticky na základě stavu Invoice, rychlosti Exchange atd. Informace o produktu se vytvoří automaticky, pokud byl Invoice vytvořen s informacemi o produktu, například v aplikaci Prodejní místo.


#### Filtrace Invoice


Faktury lze filtrovat pomocí rychlých filtrů umístěných vedle tlačítka pro vyhledávání nebo pomocí pokročilých filtrů, které lze přepínat kliknutím na odkaz (Nápověda) v horní části. Uživatelé mohou filtrovat faktury podle obchodu, ID objednávky, ID položky, stavu nebo data.


#### Invoice export


Faktury serveru BTCPay lze exportovat ve formátu CSV nebo JSON. Další informace o exportu a účtování Invoice.


#### Vrácení peněz na účet Invoice


Pokud chcete z jakéhokoli důvodu vystavit vratku, můžete ji snadno vytvořit v zobrazení Invoice.


#### Archivace faktur


V důsledku toho, že server BTCPay nemá funkci opakovaného použití Address, je běžné, že se na stránce Invoice vašeho obchodu zobrazuje mnoho faktur, jejichž platnost vypršela. Chcete-li je skrýt ze svého pohledu, vyberte je v seznamu a označte je jako archivované. Faktury, které byly označeny jako archivované, se neodstraní. Platba na archivovanou Invoice bude stále detekována vaším serverem BTCPay (stav paidLate). Archivované faktury obchodu můžete kdykoli zobrazit výběrem archivovaných faktur z rozbalovacího seznamu filtru vyhledávání.


#### Výchozí měna


Výchozí měna obchodu, která byla nastavena v průvodci vytvořením obchodu.


#### Umožnit komukoli vytvořit Invoice


Tuto možnost byste měli povolit, pokud chcete umožnit vytváření faktur ve vašem obchodě zvenčí. Tato možnost je užitečná pouze v případě, že používáte platební tlačítko nebo pokud vystavujete faktury prostřednictvím rozhraní API nebo webové stránky HTML třetí strany. Aplikace PoS je předautorizovaná a nevyžaduje povolení tohoto nastavení, aby náhodný návštěvník mohl otevřít váš obchod POS a vytvořit Invoice.


#### Přidání dalšího poplatku (síťový poplatek) k účtu Invoice



- Pouze v případě, že zákazník provede více než jednu platbu za Invoice
- Při každé platbě
- Nikdy nepřidávejte síťový poplatek


#### Invoice pozbývá platnosti, pokud není uhrazena celá částka po ... minutách.


Časovač Invoice je ve výchozím nastavení nastaven na 15 minut. Časovač slouží jako ochranný mechanismus proti volatilitě, protože blokuje množství kryptoměn na základě kurzů kryptoměn vůči fiatu. Pokud zákazník nezaplatí částku Invoice ve stanovené lhůtě, považuje se Invoice za prošlou. Invoice je považován za "zaplacený", jakmile je transakce viditelná na Blockchain (s nulovým počtem potvrzení), a je považován za "dokončený", jakmile dosáhne počtu potvrzení, který obchodník definoval (obvykle 1-6). Časovač lze přizpůsobit.


#### Považujte Invoice za zaplacený, i když je zaplacená částka o ..% nižší, než se očekávalo.


V situaci, kdy zákazník použije Exchange Wallet k přímé platbě za Invoice, si Exchange vezme malý poplatek. To znamená, že takový Invoice není považován za zcela dokončený. Invoice je označen jako "částečně zaplacený" Pokud chce obchodník přijímat nedoplacené faktury, můžete zde nastavit procentní sazbu


### Žádosti


Žádosti o platbu jsou funkcí, která umožňuje majitelům obchodů BTCPay vytvářet dlouhodobé faktury. Prostředky jsou vypláceny podle žádosti o platbu s použitím kurzu Exchange platného v době platby. Uživatelé tak mohou provádět platby podle svého uvážení, aniž by museli v době platby vyjednávat nebo ověřovat sazby Exchange s majitelem obchodu.


Uživatelé mohou za žádosti platit po částech. Požadavek na platbu zůstane platný, dokud není uhrazen v plné výši nebo pokud majitel obchodu požaduje dobu platnosti. Adresy se nikdy nepoužívají opakovaně. Pokaždé, když uživatel klikne na tlačítko zaplatit, je vygenerován nový kód Address, který vytvoří kód Invoice pro daný požadavek na platbu.


Majitelé obchodů mohou tisknout žádosti o platbu (nebo exportovat data Invoice) pro evidenci a účetnictví. BTCPay automaticky označuje faktury jako žádosti o platbu v seznamu Invoice vašeho obchodu.


#### Přizpůsobení žádostí o platbu



- Invoice Částka - Nastavení požadované částky platby
- Denominace - Zobrazte požadovanou částku v nominální hodnotě nebo v kryptoměně
- Množství plateb - Povolit pouze jednotlivé platby nebo částečné platby
- Doba vypršení platnosti - Povolení plateb do určitého data nebo bez vypršení platnosti
- Popis - Textový editor, datové tabulky, vkládání fotografií a videí
- Vzhled - Barva a styl pomocí motivů CSS


![image](assets/en/094.webp)


#### Vytvoření žádosti o platbu


V levém menu přejděte na položku Žádost o platbu a klikněte na tlačítko "Vytvořit žádost o platbu".


![image](assets/en/095.webp)


Zadejte název požadavku, částku, nominální hodnotu, přidružený obchod, dobu platnosti a popis (nepovinné)


Pokud chcete povolit částečné platby, vyberte možnost Povolit příjemci vytvářet faktury v jeho nominální hodnotě.


Kliknutím na tlačítko Uložit a zobrazit zkontrolujte svou žádost o platbu.


BTCPay vytvoří adresu URL pro požadavek na platbu. Tuto adresu URL můžete sdílet a zobrazit si žádost o platbu. Potřebujete více stejných požadavků? Platební žádosti můžete duplikovat pomocí možnosti Klonovat v hlavní nabídce.


![image](assets/en/096.webp)


**UPOZORNĚNÍ**


Platební požadavky jsou závislé na úložišti, což znamená, že každý platební požadavek je při vytváření přiřazen k úložišti. Ujistěte se, že je k vašemu obchodu připojen účet Wallet, ke kterému platební požadavek patří.


#### Placená žádost


Příjemce a žadatel mohou po odeslání platby zobrazit stav žádosti o platbu. Pokud byla platba přijata v plné výši, zobrazí se stav jako Vyřízeno. Pokud byly provedeny pouze částečné platby, zobrazí se v poli Dlužná částka zbývající zůstatek.


![image](assets/en/097.webp)


#### Přizpůsobení žádostí o platbu


Obsah popisu lze upravit pomocí textového editoru žádosti o platbu. Obě možnosti jsou k dispozici, pokud chcete použít další barevné motivy nebo vlastní stylování CSS.


Netechničtí uživatelé mohou použít [bootstrap theme](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Další přizpůsobení lze provést zadáním dalšího kódu CSS, jak je uvedeno níže.


```css
:root {
--btcpay-font-family-base: "Source Sans Pro", -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--btcpay-primary: #7d4698;
--btcpay-primary-accent: #59316b;
--btcpay-body-text: #333a41;
--btcpay-body-bg: #fff;
--btcpay-bg-tile: #f8f9fa;
}

#mainNav {
color: white;
background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
color: white;
}
```


### Stažení plateb


Tradičně příjemce sdílí svůj Bitcoin Address, aby provedl platbu Bitcoin, a odesílatel později pošle peníze na tento Address. Takový systém se nazývá Push payment, protože odesílatel iniciuje platbu v době, kdy příjemce může být nedostupný, a tlačí platbu k příjemci.


Co když se ale role obrátí?


Co kdyby místo toho, aby odesílatel platbu tlačil, umožnil příjemci platbu stáhnout v době, kterou příjemce uzná za vhodnou? To je koncept tahové platby. To umožňuje několik nových aplikací, jako např:



- Předplacená služba (kdy předplatitel umožňuje službě čerpat peníze po x časech)
- Vrácení peněz (pokud obchodník umožní zákazníkovi stáhnout si vrácené peníze na svůj účet Wallet, kdy uzná za vhodné)
- Vyúčtování na základě času pro osoby na volné noze (kdy najímající osoba umožní osobě na volné noze čerpat peníze do svého účtu Wallet podle vykázaného času)
- Patronát (mecenáš umožňuje příjemci každý měsíc čerpat peníze na další podporu jeho práce)
- Automatický prodej (kdy zákazník Exchange umožní, aby Exchange každý měsíc automaticky stahoval peníze ze svého Wallet a prodával je)
- Systém výběru zůstatku (služba s velkým objemem výplat umožňuje uživatelům požádat o výběr z jejich zůstatku, služba pak může snadno dávkovat všechny výplaty mnoha uživatelům v pevně stanovených intervalech)


### Výplaty


Funkce výplaty je spojena s funkcí [Pull Payments](https://docs.btcpayserver.org/PullPayments/). Tato funkce umožňuje vytvářet výplaty v rámci BTCPay. Tato funkce umožňuje zpracovávat pull platby (náhrady, výplaty mezd nebo výběry).


#### Příklad 1: Vrácení peněz


Začněme příkladem vrácení peněz. Zákazník si ve vašem obchodě zakoupil zboží, ale bohužel ho musí vrátit. Chce vrátit peníze. V rámci služby BTCPay můžete vytvořit položku [Refund](https://docs.btcpayserver.org/Refund/) a poskytnout zákazníkovi odkaz, aby si vyzvedl své prostředky. Jakmile zákazník zadá svůj kód Address a požádá o vyplacení prostředků, zobrazí se v sekci Výplaty.


První stav, který má, je Čeká na schválení. Prodavači mohou zkontrolovat, zda jich čeká více, a po provedení výběru použijete tlačítko Akce.


Možnosti na tlačítku akce



- Schválení vybraných výplat
- Schválení a odeslání vybraných výplat
- Zrušení vybraných výplat


Dalším krokem je schválení a odeslání vybraných výplat, protože chceme zákazníkovi vrátit peníze. Zkontrolujeme zákaznickou kartu Address, kde je uvedena částka a zda si přejeme, aby byly poplatky od vrácené částky odečteny, či nikoliv. Po dokončení kontroly zbývá už jen podepsat transakci.


Zákazník se nyní aktualizuje na stránce Reklamace. Může sledovat transakci, protože je mu poskytnut odkaz na Block explorer a jeho transakci. Po potvrzení transakce se její stav změní na "Dokončeno".


#### Příklad 2: Plat


Nyní se věnujme výplatě mezd, protože ta se řídí zevnitř obchodu, a nikoli podle požadavku zákazníka. Základní koncept je stejný; využívá tahové platby. Ale místo vytvoření refundace provedeme [Tažnou platbu](https://docs.btcpayserver.org/PullPayments/).


Přejděte na kartu Pull Payments na serveru BTCPay. V pravém horním rohu klikněte na tlačítko Vytvořit pull platbu.


Nyní se nacházíme ve fázi vytváření výplaty, pojmenujte ji a zadejte požadovanou částku ve zvolené měně. Vyplňte Popis, aby zaměstnanec věděl, o co se jedná. Další část je podobná jako u náhrad. Zaměstnanec vyplní Cíl Address a částku, kterou chce z této Výplaty požadovat. Může se rozhodnout, že půjde o 2 samostatné žádosti, na různé adresy, nebo dokonce o částečnou žádost přes blesk.


Pokud čekáte na více výplat, můžete je podepsat a odeslat v dávkách. Po podepsání se Výplaty přesunou na kartu Probíhá a zobrazí se na ní Transakce. Po přijetí sítí se výplata přesune na kartu Dokončeno. Záložka Dokončeno slouží čistě pro historické účely. Jsou v ní uloženy zpracované Výplaty a transakce, které k nim patří


### Stažení plateb


#### Koncept


Při konfiguraci platby Pull může odesílatel nastavit řadu vlastností:



- Název požadavku na stažení
- Limitní částka
- Jednotka (například BTC, SAT, USD)
- Způsoby platby
  - BTC On-Chain
  - BTC off-chain
- Popis
- Vlastní CSS
- Datum ukončení (nepovinné pro Lightning Network BOLT11)


Poté může odesílatel pomocí odkazu sdílet s příjemcem vytaženou platbu a umožnit mu vytvořit výplatu. Příjemce si vybere svou výplatu:



- Jaký způsob platby použít
- Kam poslat peníze


Jakmile je výplata vytvořena, započítává se do limitu pro výplatu tahu v aktuálním období. Odesílatel poté schválí výplatu nastavením sazby, za kterou bude výplata odeslána, a přistoupí k platbě.


Pro odesílatele poskytujeme snadno použitelnou metodu dávkování více výplat z [BTCPay Internal Wallet](https://docs.btcpayserver.org/Wallet/).


#### Rozhraní API Greenfield


Server BTCPay poskytuje odesílateli i příjemci úplné rozhraní API, které je zdokumentováno na stránce `/docs` vaší instance. (nebo na webové stránce s dokumentací https://docs.btcpayserver.org)


Vzhledem k tomu, že naše rozhraní API zpřístupňuje všechny možnosti tahových plateb, může odesílatel automatizovat platby podle svých potřeb.


### Shrnutí dovedností


V této části jste se dozvěděli následující:



- Důkladná znalost stavů Invoice serveru BTCPay a akcí, které lze na nich provádět
- Přizpůsobení a správa mechanismů Invoice s prodlouženou životností známých jako Požadavky.
- Další flexibilní možnosti plateb se otevírají díky jedinečné funkci Pull Payment na serveru BTCPay, zejména při zpracování refundací a výplat mezd.


### Hodnocení znalostí


#### Koncepční přezkum KA


Jaké jsou rozdíly mezi fakturami a žádostmi o platbu a co může být dobrým důvodem pro jejich použití?


#### Koncepční přezkum KA


Jak se platby za stažení rozšiřují o to, co lze obvykle provést On-Chain? Popište některé případy použití, které umožňují.


## Výchozí pluginy serveru BTCPay


<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>


### Výchozí zásuvné moduly a aplikace


Server BTCPay je dodáván se standardní sadou pluginů (aplikací), které mohou server BTCPay proměnit v platební bránu pro elektronické obchodování. Po přidání prodejního místa, platformy Crowdfund a tlačítka pro snadnou platbu se BTCPay Server stává snadno nasaditelným řešením.


### Prodejní místa


Jedním ze standardních pluginů serveru BTCPay je Point of Sale (PoS). Pomocí pluginu PoS může majitel obchodu vytvořit webový obchod přímo ze serveru BTCPay Server; majitel obchodu nepotřebuje k provozování webového obchodu řešení e-commerce třetích stran. Webová aplikace PoS umožňuje uživatelům s kamennými prodejnami snadno přijímat platby Bitcoin bez poplatků a bez třetí strany přímo do jejich Wallet. Aplikaci PoS lze snadno zobrazit na tabletech nebo jiných zařízeních, která podporují prohlížení webových stránek. Uživatelé si mohou snadno vytvořit zástupce na domovské obrazovce pro rychlý přístup k webové aplikaci.


#### Jak vytvořit nové prodejní místo


BTCPay Server umožňuje majitelům obchodů rychle vytvořit prodejní místo v několika rozvrženích. BTCPay Server si uvědomuje, že ne každý obchod je e-shop a ne každý obchod je bar nebo restaurace, a přichází s několika standardními nastaveními pro vaše PoS.


Když majitel obchodu klikne na "Prodejní místo" v levém řádku nabídky, server BTCPay se nyní zeptá na jméno; toto jméno bude viditelné v levém řádku nabídky. Kliknutím na tlačítko Vytvořit vytvoříte PoS.


![image](assets/en/098.webp)


#### Aktualizace nově vytvořeného prodejního místa


Po vytvoření nového PoS můžete na následující obrazovce aktualizovat prodejní místo a přidat položky pro svůj obchod.


##### Název aplikace


Zde uvedený název vašeho prodejního místa bude viditelný v hlavní nabídce serveru BTCPay.


##### Zobrazení názvu


Veřejnost při návštěvě uvidí název nebo jméno vašeho obchodu. Server BTCPay ve výchozím nastavení pojmenuje váš obchod "Tea shop" Nahraďte jej názvem svého obchodu.


![image](assets/en/099.webp)


#### Zvolte styl prodejního místa


Server BTCPay dokáže zobrazit své prodejní místo několika způsoby.



- Seznam produktů
  - Zobrazení obchodu, ve kterém mohou zákazníci najednou zakoupit pouze 1 produkt.
- Seznam produktů s košíkem.
  - Zobrazení obchodu, ve kterém mohou zákazníci nakoupit více položek najednou a získat přehled o nákupním košíku v pravé části obrazovky.
- Pouze klávesnice
  - Žádný seznam produktů, pouze klávesnice pro přímou fakturaci.
- Zobrazení pro tisk (tisknutelný seznam produktů s QR)
  - Pokud nemůžete vždy zobrazovat seznam produktů digitálně, potřebujete "offline" řešení pro produkty; BTCPay Server má tiskový displej, který funguje jako offline obchod.


![image](assets/en/100.webp)


#### Point Of Sale Style - Seznam produktů


![image](assets/en/101.webp)


#### Styl prodejního místa - Seznam produktů + Košík


![image](assets/en/102.webp)


#### Styl prodejního místa - pouze klávesnice


![image](assets/en/103.webp)


#### Styl prodejního místa - Tiskový displej


![image](assets/en/104.webp)


#### Měna


Majitel obchodu může pro své prodejní místo nastavit jinou měnu, než je jeho celková nastavená výchozí měna. Toto pole se automaticky vyplní výchozí měnou obchodu.


#### Popis


Řekněte světu o svém obchodě; co prodáváte a za kolik? Vše, co vysvětluje váš obchod, patří sem.


![image](assets/en/105.webp)


#### Produkty


Když se vytvoří prodejní místo, standardní server BTCPay přidá do obchodu několik položek pro referenci. Klikněte na tlačítko Upravit u některé ze standardních položek, abyste lépe porozuměli jednotlivým možným volbám pro danou položku.


Vytvoření nového produktu v obchodě se skládá z následujících polí;



- Název
- Cena (pevná, minimální nebo vlastní)
- Adresa URL obrázku
- Popis
- Inventura
- ID
- Koupit text tlačítka.
- Povolit/vypnout


Jakmile majitel obchodu vyplní všechna nová pole produktu, klikněte na tlačítko uložit a všimněte si, že se sekce Produkty v prodejním místě nyní vyplní. Vždy ukládejte v pravém horním rohu obrazovky, abyste předešli možnosti, že majitelé obchodu ztratí svůj postup při přidávání produktů.


Majitelé obchodů mohou ke konfiguraci svých produktů používat také "Raw Editor". Editor raw vyžaduje základní znalosti struktur JSON.


![image](assets/en/106.webp)


#### Pokladna


Server BTCPay umožňuje malé přizpůsobení pokladen specifické pro PoS. Majitel obchodu může nastavit text "Koupit za x" nebo si vyžádat konkrétní údaje o zákazníkovi přidáním do formulářů.


#### Tipy


Pouze některé obchody potřebují možnost Tipy na prodej. Majitelé obchodů ji mohou zapnout nebo vypnout podle toho, jak uznají za vhodné pro svůj obchod. Pokud obchod používá zapnuté tipy, může majitel obchodu nastavit text v poli pro tipy, který se mu líbí. Spropitné na serveru BTCPay funguje na základě procentuální částky. Majitelé obchodu mohou přidat více procentních podílů oddělených čárkami.


#### Slevy


Jako majitel obchodu můžete chtít zákazníkovi při placení poskytnout vlastní slevu; přepínač Slevy je k dispozici v pokladně vašeho obchodu. Důrazně však nedoporučujeme používat samoobslužné pokladní systémy.


#### Vlastní platby


Je-li zapnuta možnost Vlastní platby, může zákazník zadat nastavenou cenu rovnou nebo vyšší než původní cena Invoice vygenerovaná obchodem.


#### Další možnosti


Po nastavení všeho pro vaše prodejní místo zbývá několik dalších možností. Majitelé obchodů mohou snadno vložit svůj PoS prostřednictvím rámce Iframe nebo vložit platební tlačítko odkazující na konkrétní položku obchodu. Pro stylizaci právě vytvořeného obchodu PoS mohou majitelé přidat vlastní CSS ve spodní části dalších možností.


#### Odstranit tuto aplikaci


Pokud chce majitel obchodu zcela odstranit prodejní místo ze svého serveru BTCPay, může v dolní části aktualizace PoS kliknout na tlačítko Odstranit tuto aplikaci a zcela tak zničit svou aplikaci PoS. Po kliknutí na tlačítko "Smazat tuto aplikaci" si server BTCPay vyžádá potvrzení zadáním `DELETE` a potvrzením kliknutím na tlačítko Smazat. Po odstranění se majitel obchodu vrátí na ovládací panel serveru BTCPay Server.


### Server BTCPay - Crowdfund


Server BTCPay má vedle pluginu Point of Sale možnost vytvořit crowdfunding. Stejně jako u jiných platforem crowdfundingu mohou majitelé obchodů nastavit cíl, vytvořit výhody pro příspěvky a přizpůsobit je svým potřebám.


#### Jak založit nový crowdfundingový fond


Klikněte na plugin Crowdfund v hlavním menu vlevo na serveru BTCPay pod sekcí Plugin. BTCPay Server si nyní vyžádá název pro Crowdfund; tento název se také zobrazí v levém panelu nabídky.


![image](assets/en/107.webp)


#### Aktualizace nově vytvořeného prodejního místa


Jakmile je aplikaci přidělen název, na další obrazovce se aktualizuje kontext aplikace.


#### Název aplikace


Název vašeho crowdfundingu bude viditelný v hlavní nabídce serveru BTCPay.


#### Zobrazení názvu


Tento titul je určen pro veřejnost.


#### Tagline


Dejte crowdfundingu jednu větu, abyste poznali, čeho se sbírka týká.


![image](assets/en/108.webp)


#### Adresa URL doporučeného obrázku


Každý crowdfunding má svůj hlavní obrázek, jeden banner, který přímo poznáte. Tento obrázek může být uložen na vašem serveru, pokud máte práva pro správu. Administrátoři jej mohou nahrát v nastavení serveru BTCPay - Soubory. Jste-li majitelem obchodu, je třeba obrázek nahrát na web prostřednictvím hostitele třetí strany (například Imgur).


#### Zveřejnění crowdfundingu


Tímto přepínačem se váš crowdfunding stane veřejným, a tedy viditelným pro okolní svět. Pro účely testování nebo zjištění, zda je téma správně použito, ponechte toto nastavení po dobu vytváření crowdfundingu na hodnotě OFF.


#### Popis


Řekněte světu o svém crowdfundingu. Na co vybíráte peníze? Vše, co vysvětluje váš crowdfunding, najdete zde.


![image](assets/en/109.webp)


#### Cíl crowdfundingu


Stanovte cílovou částku, kterou by měl fundraiser na projekt vydělat, a měnu, ve které by měla být tato částka vyjádřena. Ujistěte se, že pokud jsou vaše cíle stanoveny mezi daty, uveďte tato cílová a koncová data pod položkou Cíle v crowdfundingu.


![image](assets/en/110.webp)


#### Výhody


Výhody mohou výrazně posílit vaše úsilí o crowdfunding. Výhody totiž lidem umožňují účastnit se vaší kampaně. Využívají jak sobecké, tak dobročinné motivace. A umožňují vám přístup k výdajům vašich podporovatelů, nejen k jejich dobročinným peněženkám - můžete hádat, co je významnější.


Vytvoření nové výhody se skládá z následujících polí.



- Název
- Cena (pevná, minimální nebo vlastní)
- Adresa URL obrázku
- Popis
- Inventura
- ID
- Koupit text tlačítka.
- Povolit/vypnout


Jakmile majitel obchodu vyplní všechna pole nové výhody, klikněte na tlačítko uložit a všimněte si, že se sekce Výhody v sekci Crowdfunds nyní vyplní.


![image](assets/en/111.webp)


### Server BTCPay - prodejní místo


#### Příspěvky


Majitelé obchodů si mohou zvolit způsob zobrazení výhod, jejich řazení nebo dokonce jejich porovnání s ostatními výhodami. Po dosažení cílů crowdfundingu však mohou majitelé obchodů chtít zastavit přísun darů na tuto sbírku. Proto může přepnout na možnost "Nepovolit další příspěvky po dosažení cíle". Tím se zabrání tomu, aby Crowdfund přijímal dary.


##### Chování crowdfundingu


Standard Crowdfund započítává do cíle pouze faktury vytvořené pomocí Crowdfund. Mohou však nastat případy, kdy majitel obchodu chce, aby se do crowdfundingu započítávaly všechny faktury vytvořené v tomto obchodě.


#### Další možnosti přizpůsobení


Server BTCpay nabízí několik dalších možností přizpůsobení. Přidejte do crowdfundingu zvuky, animace nebo dokonce diskusní vlákna. Majitelé obchodu mohou také upravit vzhled Crowdfund zadáním vlastního CSS.


#### Odstranit tuto aplikaci


Pokud chce majitel obchodu zcela odstranit crowdfund ze svého serveru BTCPay, může v dolní části aktualizace crowdfund kliknout na tlačítko "Odstranit tuto aplikaci" a zcela tak odstranit svou aplikaci crowdfund. Po kliknutí na tlačítko "Odstranit tuto aplikaci" si server BTCPay vyžádá potvrzení zadáním `DELETE` a potvrzením kliknutím na tlačítko Odstranit. Po odstranění se majitel obchodu vrátí na ovládací panel serveru BTCPay Server.


### Server BTCPay - Tlačítko pro platbu


Snadno vložitelné HTML a vysoce přizpůsobitelná platební tlačítka umožňují majitelům obchodů přijímat spropitné a dary. V levém panelu nabídky serveru BTCPay, pod sekcí Pluginy, mohou majitelé obchodů kliknout na "Platební tlačítko" a kliknutím na tlačítko Povolit vytvořit platební tlačítko.


#### Obecná nastavení


V obecných nastaveních platebního tlačítka mohou majitelé obchodů nastavit



- Standardní cena
- Výchozí měna
- Výchozí způsob platby
  - Použít výchozí nastavení obchodu
  - BTC On-Chain
  - BTC off-chain (Lightning)
  - BTC off-chain (LNURL-pay)
- Popis pokladny
- ID objednávky


#### Možnosti zobrazení


Tlačítko Pay na serveru BTCPay lze nakonfigurovat tak, aby vyhovovalo různým stylům. Tlačítka mohou mít pevnou nebo vlastní částku, která se zobrazuje pomocí posuvníku nebo přepínačů plus a minus.


#### Použití Modal


Při vytváření platebního tlačítka mohou majitelé obchodů zvolit jeho chování, když na něj zákazník klikne, a zobrazit ho v modálním okně nebo jako novou stránku.


**!?Poznámka!?**


Varování: Tlačítko Platba by se mělo používat pouze pro spropitné a dary


Použití platebního tlačítka pro integraci s elektronickým obchodem se nedoporučuje, protože uživatel může měnit informace související s objednávkou. Pro e-commerce byste měli používat naše rozhraní API Greenfield. Pokud tento obchod zpracovává komerční transakce, doporučujeme před použitím platebního tlačítka vytvořit samostatný obchod.


#### Přizpůsobení textu tlačítka Pay


Ve výchozím nastavení je na platebním tlačítku serveru BTCPay uvedeno "Zaplatit pomocí BTCPay". Majitelé obchodů si mohou tento text nastavit podle svého přání a změnit logo BTCPay Serveru na své vlastní. Text nastavíte pomocí pole "Pay Button Text" a URL adresu obrázku vložíte pod pole "Pay Button Image URL".


##### Velikost obrázku


Velikost obrázku v tlačítku lze nastavit pouze na tři výchozí hodnoty.



- 146x40px
- 168x46px
- 209x57px


#### Typ tlačítka


Server BTCPay zná tři stavy platebního tlačítka.



- Pevná částka
  - Předchozí nastavená cena je uvedena v obecných nastaveních tlačítka.
- Vlastní částka
  - Tlačítko Pay na serveru BTCPay má přepínače + a - pro nastavení vlastní ceny.
  - Při použití vlastní částky si server BTCPay vyžádá Min, Max a jak postupně se má zvyšovat.
  - Tlačítka lze nastavit na "Použít jednoduchý styl zadávání".Tím se odstraní přepínače +/-.
  - Fit tlačítko inline, kde se tlačítko a přepínače zobrazují inline.
- Posuvník
  - Podobně jako vlastní částka se však vizuálně liší, protože místo přepínačů +/- má posuvník.
  - Při použití posuvníku si server BTCPay vyžádá Min, Max a způsob postupného zvyšování.


**!?Poznámka!?**


Tlačítko Platba lze v horní části popisu varování odstranit.


#### Oznámení o platbách


Server IPN (oznámení o okamžité platbě) je určen pro webové háčky a lze jej nakonfigurovat pomocí adresy URL pro údaje po nákupu.


#### E-mailová oznámení


Kdykoli byla provedena platba, může server BTCPay informovat majitele obchodu.


#### Přesměrování prohlížeče


Když zákazník dokončí nákup, bude přesměrován na tento odkaz, pokud jej majitel obchodu nastavil.


#### Rozšířené možnosti platebního tlačítka


Zadejte další parametry řetězce dotazů, které by měly být připojeny ke stránce pokladny po vytvoření Invoice. Například `lang=da-DK` by ve výchozím nastavení načetl stránku pokladny v dánštině.


#### Použití aplikace jako koncového bodu


Platební tlačítko můžete přímo propojit s položkou v některé z aplikací PoS nebo Crowdfund, které jste již dříve používali.


Majitelé obchodů mohou kliknout na rozbalovací nabídku a vybrat požadovanou aplikaci; po výběru aplikace může majitel obchodu přidat položku, kterou je třeba propojit.


#### Generovaný kód


Vzhledem k tomu, že platební tlačítko BTCPay Serveru je snadno vložitelný HTML, BTCPay Server po konfiguraci platebního tlačítka zobrazí ve spodní části vygenerovaný kód, který lze zkopírovat do webové stránky.


Majitelé obchodů mohou zkopírovat vygenerovaný kód na své webové stránky a platební tlačítko ze serveru BTCPay je aktivní přímo na jejich webových stránkách.


#### Oznámení o platbách


Server IPN (oznámení o okamžité platbě) je určen pro webové háčky a lze jej nakonfigurovat pomocí adresy URL pro odesílání údajů o nákupu.


#### E-mailová oznámení


Kdykoli je provedena platba, server BTCPay může upozornit majitele obchodu.


#### Přesměrování prohlížeče


Když zákazník dokončí nákup, bude přesměrován na tento odkaz, pokud jej majitel obchodu nastavil.


#### Rozšířené možnosti platebního tlačítka


Zadejte další parametry dotazovacího řetězce, které by měly být připojeny ke stránce pokladny po vytvoření Invoice. Například `lang=da-DK` by ve výchozím nastavení načetl stránku pokladny v dánštině.


#### Použití aplikace jako koncového bodu


Platební tlačítko můžete přímo propojit s položkou v některé z aplikací PoS nebo Crowdfund, které jste již dříve používali. Majitelé obchodů mohou kliknout na rozbalovací nabídku a vybrat požadovanou aplikaci. Po výběru aplikace může majitel obchodu přidat položku, kterou je třeba propojit.


#### Generovaný kód


Vzhledem k tomu, že platební tlačítko BTCPay Serveru je snadno vložitelný HTML, BTCPay Server po konfiguraci platebního tlačítka zobrazí ve spodní části vygenerovaný kód, který lze zkopírovat do webové stránky. Majitelé obchodů mohou vygenerovaný kód zkopírovat na své webové stránky a Platební tlačítko od BTCPay Serveru je na jejich webových stránkách přímo aktivní.


### Shrnutí dovedností


V této části jste se dozvěděli:



- Jak snadno vytvořit vlastní obchod pomocí integrovaného pluginu PoS serveru BTCPay?
- Jak snadno vytvořit vlastní crowdfundingovou aplikaci pomocí integrovaného pluginu BTCPay Serveru?
- Generování kódu pro vlastní platební tlačítko pomocí pluginu Pay Button


### Hodnocení znalostí


#### KA Review


Jaké tři integrované pluginy jsou standardní součástí BTCPay Serveru? Popište několika slovy, jak lze každý z nich použít.


# Konfigurace serveru BTCPay


<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>


## Základní znalosti instalace BTCPay Serveru v prostředí LunaNode


<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>


### Instalace serveru BTCPay na hostovaném prostředí (LunaNode)


Tyto kroky vám poskytnou všechny potřebné informace pro zahájení používání serveru BTCPay na LunaNode. Existuje mnoho možností nasazení softwaru.

Všechny podrobnosti o serveru BTCPay najdete na adrese https://docs.btcpayserver.org.


#### Kde začít?


V této části se seznámíte s poskytovatelem hostingu LunaNode, dozvíte se o prvních krocích při používání serveru BTCPay a naučíte se pracovat s Lightning Network. Poté, co projdeme všechny kroky, můžete provozovat webový obchod nebo crowdfundingovou platformu přijímající Bitcoin!


Jedná se o jeden z mnoha způsobů nasazení serveru BTCPay. Další podrobnosti najdete v naší dokumentaci.


https://docs.btcpayserver.org.


### Server BTCPay - nasazení LunaNode


#### Nasazení uzlu LunaNode


Nejprve přejděte na webové stránky LunaNode.com, kde si vytvoříme nový účet. Klikněte na tlačítko Zaregistrovat se vpravo nahoře nebo použijte průvodce Začít na jejich domovské stránce.


![image](assets/en/112.webp)


Po vytvoření nového účtu vám LunaNode zašle ověřovací e-mail. Jakmile účet ověříte, ve srovnání s Napětím se vám okamžitě zobrazí možnost doplnit zůstatek na účtu. Tento zůstatek je nutný k pokrytí nákladů na serverový prostor a hosting.


![image](assets/en/113.webp)


#### Přidejte si kredit na svůj účet LunaNode


Po kliknutí na tlačítko "Vložit kredit" si můžete nastavit, jakou částkou chcete účet dobít a jakým způsobem za něj chcete zaplatit. LunaNode a BTCPay Server budou stát od 10 do 20 dolarů měsíčně.

Ve srovnání s Voltage.cloud získáte plný přístup ke svému virtuálnímu privátnímu serveru (VPS), což vám umožní mít nad svým serverem větší kontrolu. Po vytvoření nového účtu vám LunaNode zašle ověřovací e-mail.

Po ověření účtu se vám ve srovnání s Voltage okamžitě zobrazí možnost doplnit zůstatek na účtu. Tento zůstatek je nutný k pokrytí nákladů na serverový prostor a hosting.


#### Jak nasadit nový server?


V tomto průvodci vás provedeme procesem nastavení vytvořením sady klíčů API a použitím spouštěče serveru BTCPay vyvinutého společností LunaNode.


Na ovládacím panelu LunaNode klikněte vpravo nahoře na API. Tím se otevře nová stránka. Musíme pouze nastavit Jméno pro klíč API. O zbytek se postará LunaNode a v tomto návodu se jím nebudeme zabývat. Klikněte na tlačítko Vytvořit pověření API.

Po vytvoření pověření API se zobrazí dlouhý řetězec písmen a znaků. To je váš klíč API.


![image](assets/en/114.webp)


#### Jak nasadit nový server?


Tyto pověření mají dvě části: klíč API a ID API; budeme potřebovat obě. Než přejdeme k dalšímu kroku, otevřeme v prohlížeči druhou kartu a přejdeme na adresu https://launchbtcpay.lunanode.com/


Zde budete požádáni o zadání klíče API a ID API. To slouží k tomu, abyste věděli, že jste tento nový server poskytli vy. Klíč API by měl být stále otevřen na předchozí kartě; pokud v tabulce níže sjedete dolů, najdete ID API.


Můžete se vrátit na stránku se spouštěčem, vyplnit pole s klíčem API a ID a kliknout na pokračovat.


![image](assets/en/115.webp)


V dalším kroku můžete zadat název domény. Pokud již vlastníte doménu a chcete ji použít pro server BTCPay, nezapomeňte na své doméně přidat také záznam DNS (tzv. `A` záznam). Pokud doménu nevlastníte, použijte místo ní doménu poskytnutou společností LunaNode (můžete ji později změnit v nastavení BTCPay Serveru) a klikněte na tlačítko Pokračovat.


Další informace o nastavení nebo změně záznamu DNS pro server BTCPay; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name


#### Spuštění serveru BTCPay na LunaNode


Po provedení předchozích kroků můžeme nastavit všechny možnosti pro náš nový server. Zde vybereme jako podporovanou měnu Bitcoin (BTC). Můžeme také nastavit e-mail, na který budeme dostávat oznámení o šifrovacích certifikátech pro účely obnovení, což je volitelné.


Tento návod je zaměřen na nastavení prostředí Mainnet (v reálném světě Bitcoin); LunaNode však umožňuje pro vývojové účely nastavit také prostředí Testnet nebo Regtest. V tomto průvodci ponecháme možnost Mainnet.


Můžete si vybrat implementaci Lightning. LunaNode nabízí dvě různé implementace, LND a Core Lightning. V tomto průvodci se budeme zabývat implementací LND. V obou implementacích je jen málo, ale zato skutečných rozdílů; pro více informací o nich doporučujeme přečíst si rozsáhlou dokumentaci: https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln


![image](assets/en/116.webp)


LunaNode nabízí několik plánů virtuálních počítačů. Ty se liší cenovým rozpětím a specifikacemi serverů. Pro účely tohoto průvodce postačí plán m2; pokud jste však jako měnu zvolili více než jen Bitcoin, zvažte použití alespoň plánu m4.


Zrychlete počáteční synchronizaci Blockchain; tato možnost je volitelná a závisí na vašich potřebách. Existují i pokročilé možnosti, jako je nastavení aliasu Lightning, odkazování na konkrétní verzi GitHubu nebo nastavení klíčů SSH; žádnou z nich se tento průvodce nebude zabývat.


Po vyplnění formuláře klikněte na tlačítko Launch VM a Lunanode začne vytvářet váš nový virtuální počítač včetně nainstalovaného serveru BTCPay. Tento proces trvá několik minut; jakmile je váš server připraven, LunaNode vám poskytne odkaz na váš nový BTCPay Server.


Po vytvoření klikněte na odkaz na server BTCPay a budete vyzváni k vytvoření účtu správce.


![image](assets/en/117.webp)


### Shrnutí dovedností


V této části jste se dozvěděli:



- Vytvoření a financování účtu na platformě LunaNode
- Použití nástroje BTCPay Server Launcher k vytvoření vlastního serveru


### Hodnocení znalostí


#### Koncepční přezkum KA


Popište některé rozdíly mezi provozem instance BTCPay Serveru na VPS a vytvořením účtu na hostované instanci.


## Instalace serveru BTCPay v prostředí Voltage


<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>


Seznámíte se s Voltage.cloud jako poskytovatelem hostingu, dozvíte se o prvních krocích při používání serveru BTCPay a naučíte se používat Lightning Network. Poté, co projdeme všechny kroky, můžete provozovat webový obchod nebo crowdfundingovou platformu přijímající Bitcoin!


Jedná se o jeden z mnoha způsobů nasazení serveru BTCPay. Další podrobnosti najdete v naší dokumentaci.

https://docs.btcpayserver.org.


### Server BTCPay - nasazení Voltage.cloud


Nejprve přejděte na webovou stránku Voltage.cloud a zaregistrujte si nový účet. Při vytváření účtu se můžete přihlásit k sedmidenní bezplatné zkušební verzi. Buď klikněte na tlačítko Sign Up vpravo nahoře, nebo použijte možnost "Vyzkoušet 7denní zkušební verzi zdarma" na jejich domovské stránce.


![image](assets/en/118.webp)


Po vytvoření účtu klikněte na tlačítko `NODES` na hlavním panelu. Jakmile vybereme možnost Uzly a vytvoříme nový uzel, zobrazí se nám možné nabídky napětí uzlu. Protože se tento průvodce bude zabývat také Lightning Network, u Voltage musíme nejprve zvolit naši implementaci Lightning a teprve poté vytvořit server BTCPay. Klikněte na možnost LightningNode.


![image](assets/en/119.webp)


Zde musíte vybrat, jaký typ uzlu Lightning chcete. Napětí má řadu možností pro vaše nastavení osvětlení. To se liší například při nasazení s uzlem LunaNode. Pro záměr tohoto návodu bude stačit uzel Lite. Více informací o rozdílech najdete v části Voltage.cloud.


![image](assets/en/120.webp)


Zadejte uzlu název, nastavte heslo a zabezpečte je. Pokud toto heslo ztratíte, ztratíte přístup ke svým zálohám a Voltage je nebude moci obnovit. Vytvořte uzel a Voltage vám zobrazí průběh. Voltage vytvořilo váš uzel Lightning. Nyní můžeme vytvořit instanci serveru BTCPay a přímo přistupovat k serveru Lightning Network.


Klikněte na Uzly v levém horním rohu ovládacího panelu. Zde můžete nastavit další část své instance serveru BTCPay. Jakmile se ocitnete v přehledu uzlů, klikněte na tlačítko "vytvořit nový". Zobrazí se vám podobná obrazovka jako předtím. Nyní místo Lightning Node zvolíme BTCPay Server.


Napětí zobrazuje zeměpisnou polohu vašeho serveru BTCPay, který je umístěn v západní oblasti USA. Zde také uvidíte náklady na hostování serveru. Klikněte na tlačítko Vytvořit a zadejte serveru BTCPay název. Povolte Lightning a Voltage vám zobrazí uzel Lightning vytvořený v předchozím kroku. Klikněte na Create a Voltage vytvoří instanci serveru BTCPay.


![image](assets/en/121.webp)


Po stisknutí tlačítka vytvořit vám Voltage nabídne výchozí uživatelské jméno a heslo. Ta jsou podobná vašemu předchozímu nastavenému heslu v aplikaci Voltage. Kliknutím na tlačítko Přihlásit se k účtu budete přesměrováni na svůj server BTCPay.


Vítejte ve své nové instanci serveru BTCPay. Protože jsme Lightning nastavili již v procesu vytváření, ukazuje se, že Lightning je již povolen!


### Shrnutí dovedností


V této kapitole jste se naučili:



- Vytvoření účtu na Voltage.cloud
- Kroky ke zprovoznění serveru BTCPay spolu s uzlem Lightning na účtu


### Hodnocení znalostí


#### Koncepční přezkum KA


Jaké jsou hlavní rozdíly mezi nastaveními Voltage a LunaNode?


## Instalace serveru BTCPay na uzel Umbrel


<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>


Na konci těchto kroků můžete přijímat bleskové platby do svého obchodu BTCPay v místní síti. Tento postup se uplatní i v případě, že provozujete uzel umbrel v restauraci nebo podniku. Pokud chcete tento obchod připojit k veřejným webovým stránkám, postupujte podle postupu pro pokročilé, abyste svůj uzel umbrel vystavili veřejnosti.


https://umbrel.com/


![image](assets/en/122.webp)


### Server BTCPay - nasazení Umbrel


Po úplné synchronizaci uzlu Umbrel s Bitcoin Blockchain přejděte do obchodu s aplikacemi Umbrel a pod položkou Aplikace vyhledejte BTCPay Server.


![image](assets/en/123.webp)


Kliknutím na server BTCPay zobrazíte podrobnosti o aplikaci. Po otevření podrobností o BTCPay Serveru se v pravém dolním rohu zobrazí požadavky na správný běh aplikace. Ukazuje se, že vyžaduje uzel Bitcoin a Lightning. Pokud nemáte na svém Umbrelu nainstalovaný uzel Lightning, klikněte na tlačítko Instalovat. Tento proces může trvat několik minut.


![image](assets/en/124.webp)


Po instalaci bleskového uzlu:


1. Klikněte na tlačítko otevřít v podrobnostech aplikace nebo na aplikaci na ovládacím panelu Umbrels.

2. Klepněte na tlačítko Nastavit nový uzel; zobrazí se 24 slov pro obnovení vašeho bleskového uzlu.

3. Zapište si je.


![image](assets/en/125.webp)


Umbrel požádá o ověření právě zapsaných slov. Po nastavení uzlu Lightning se vraťte do obchodu s aplikacemi Umbrel a najděte server BTCPay. Klikněte na tlačítko instalovat a Umbrel zobrazí, zda jsou nainstalovány požadované komponenty a zda BTCPay Server vyžaduje přístup k těmto komponentám. Po instalaci klikněte na tlačítko Otevřít v pravém horním rohu podrobností o aplikaci nebo otevřete BTCPay Server prostřednictvím ovládacího panelu Umbrellu.


Umbrel požádá o ověření právě zapsaných slov.


![image](assets/en/126.webp)


**!?Poznámka!?**


Ujistěte se, že je ukládáte na bezpečném místě, jak jste se již dříve naučili při ukládání klíčů.


Po nastavení uzlu Lightning se vraťte do obchodu s aplikacemi Umbrel a najděte BTCPay Server. Klikněte na tlačítko instalovat a aplikace Umbrel zobrazí, zda jsou nainstalovány požadované komponenty a zda BTCPay Server vyžaduje přístup k těmto komponentám.


![image](assets/en/127.webp)


Po instalaci klikněte na tlačítko Otevřít v pravém horním rohu informací o aplikaci nebo otevřete BTCPay Server prostřednictvím ovládacího panelu Umbrels.


![image](assets/en/128.webp)


### Shrnutí dovedností


V této části jste se dozvěděli:



- Kroky pro instalaci serveru BTCPay s funkcí Lightning na uzel Umbrel


### Hodnocení znalostí


#### Koncepční přezkum KA


Jak se nastavení služby Umbrel liší od předchozích dvou hostovaných možností?


# Závěrečná část


<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>




## Recenze a hodnocení

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>

## Závěr kurzu


<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>