---
name: Bitcoin a BTCPay Server
goal: Nainstalovat BTCPay Server pro vaše podnikání
objectives:
  - Porozumět, co je btcpayserver.
  - Samostatně hostovat a konfigurovat BTCPay Server.
  - Používat btcpayserver ve vašem každodenním podnikání.
---

# Bitcoin a BTCPay Server

Toto je úvodní kurz o provozování BTCPay Serveru, který napsali Alekos a Bas a byl přizpůsoben ve formátu kurzu Plan ₿ melontwist a asi0.

NEDOKONČENÝ PŘÍBĚH

"To jsou lži, moje důvěra v tebe je zlomena, udělám tě zastaralým".

Produkováno nadací BTCPay Server

+++

# Úvod

<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>

## Kritické uznání pro autora Bitcoinu a BTCPay Serveru

<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>

Začněme tím, co je BTCPay Server a odkud přišel. Vážíme si transparentnosti a určitých standardů pro vytvoření důvěry v prostoru Bitcoinu.
Projekt v tomto prostoru tyto hodnoty porušil. Vedoucí vývojář BTCPay Serveru, Nicolas Dorier, to vzal osobně a slíbil, že je učiní zastaralými. Tady jsme mnoho let později a každý den pracujeme na tomto budoucím, plně otevřeném zdroji.

> To jsou lži, moje důvěra v tebe je zlomena, udělám tě zastaralým.
> Nicolas Dorier

Po slovech Nicolase byl čas začít budovat. Do toho, co nyní nazýváme BTCPay Server, bylo vloženo mnoho práce. Více lidí chtělo s tímto úsilím pomoci. Nejznámější jsou r0ckstardev, MrKukks, Pavlenex a první obchodník, který software použil, astupidmoose.

Co znamená open source a co do takového projektu vstupuje?

FOSS znamená Free & Open-Source Software. První část se vztahuje na podmínky, které umožňují komukoli kopírovat, upravovat a dokonce distribuovat verze (i za účelem zisku) softwaru. Druhá část se vztahuje na otevřené sdílení zdrojového kódu, povzbuzuje veřejnost, aby přispívala a zlepšovala ho.
To přitahuje zkušené uživatele nadšené pro příspěvek k softwaru, který již používají a získávají z něj hodnotu, což se časem ukázalo jako vítězné v adopci nad proprietárním softwarem. Je to v souladu s etosem Bitcoinu, že "informace touží být volné". Sjednocuje vášnivé lidi, kteří tvoří komunitu, a je prostě zábavnější. Jako Bitcoin, FOSS je nevyhnutelný.

### Předtím, než začneme

Tento kurz se skládá z několika částí. Mnoho z nich bude zajištěno vaším učitelem ve třídě, demo prostředími, ke kterým získáte přístup, hostovaným serverem pro vás a možná doménovým jménem. Pokud tento kurz absolvujete samostatně, mějte na paměti, že prostředí označená jako DEMO pro vás nebudou k dispozici.
NB. Pokud budete tento kurz sledovat ve třídě, názvy serverů se mohou lišit v závislosti na vašem nastavení ve třídě. Proměnné v názvech serverů se mohou lišit kvůli tomu.

### Struktura kurzu

Každá kapitola má cíle a hodnocení znalostí. V tomto kurzu se budeme věnovat každému z nich a na konci každého bloku lekcí (tj. kapitoly) shrneme klíčové funkce. Ilustrace jsou použity k poskytnutí vizuální zpětné vazby a posílení klíčových konceptů vizuálním způsobem. Cíle jsou stanoveny na začátku každého bloku lekcí. Tyto cíle přesahují seznam úkolů. Poskytují vám průvodce k získání nové sady dovedností. Hodnocení znalostí postupně zvyšuje náročnost nastavení vašeho BTCPay Serveru.

### Co studenti získají s kurzem?

S kurzem BTCPay Server se student může seznámit se základními principy Bitcoinu, jak technickými, tak netechnickými. Rozsáhlý výcvik v používání Bitcoinu prostřednictvím BTCPay Serveru umožní studentům provozovat vlastní Bitcoinovou infrastrukturu.

### Důležité webové adresy nebo možnosti kontaktu

Nadace BTCPay Server, která umožnila Alekosovi a Basovi napsat tento kurz, se nachází v Tokiu, Japonsko. Nadace BTCPay Server je dostupná prostřednictvím uvedeného webu;

- https://foundation.btcpayserver.org
- připojte se k oficiálním chatovacím kanálům: https://chat.btcpayserver.org

## Úvod do Bitcoinu

<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>

### Porozumění Bitcoinu prostřednictvím třídního cvičení

Jedná se o třídní cvičení, takže pokud absolvujete tento kurz sami, nemůžete ho provést, ale stále můžete projít tímto cvičením. Pro dokončení tohoto úkolu je minimální počet lidí mezi 9 a 11.

Cvičení začíná po zhlédnutí úvodu "Jak funguje Bitcoin a blockchain" od BBC.

![jak funguje bitcoin a blockchain](https://youtu.be/mhE_vvwAiRc)

Toto cvičení vyžaduje účast alespoň devíti lidí. Cílem tohoto cvičení je fyzicky pochopit, jak Bitcoin funguje. Hraním jednotlivých rolí v síti se naučíte interaktivním a zábavným způsobem. Toto cvičení nezahrnuje Lightning Network.

### Příklad; Vyžaduje 9 / 11 lidí

Role jsou:

- 1 Zákazník
- 1 Obchodník
- 7 až 9 Bitcoinových uzlů

**Nastavení je následující:**

Zákazník kupuje produkt v obchodě za Bitcoin.

**Scénář 1 - Tradiční bankovní systém**

- Nastavení:
  - Viz diagramy/vysvětlení v přiloženém Figjam - [Schéma aktivity](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Získejte tři dobrovolníky ze studentů, aby hráli role Zákazníka (Alice), Obchodníka (Bob) a Banky.
- Provedení sekvence událostí:
  - Zákazník- prohlíží obchod online a najde položku za 25 dolarů, kterou chce, a informuje Obchodníka, že by ji rád zakoupil
  - Obchodník- žádá o platbu.
  - Zákazník- posílá informace o kartě Obchodníkovi
  - Obchodník- předává informace Bance (identifikuje jak sebe, tak identitu/informace) s žádostí o platbu
  - Banka shromažďuje informace o Zákazníkovi a Obchodníkovi (Alice a Bob) a kontroluje, zda má zákazník dostatečný zůstatek.
  - Odečte 25 dolarů z účtu Alice, přidá 24 dolarů na účet Boba, vezme si 1 dolar za službu
  - Obchodník dostane od Banky zelenou a pošle zboží zákazníkovi.
- Komentáře:
  - Bob a Alice musí mít vztah s bankou.
  - Banka shromažďuje identifikační informace o obou, Bobovi a Alici.
  - Banka si vezme poplatek.
  - Banka musí být důvěryhodná, aby měla stále v péči peníze každého účastníka.

**Scénář 2 - Bitcoinový systém**

- Nastavení:
  - Viz diagramy/vysvětlení v přiloženém Figjam - [Schéma aktivity](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
- Nahraďte Banku devíti studenty, kteří budou hrát roli Počítače (Bitcoinové uzly/Těžaři) v síti, aby nahradili Banku. - Každý z 9 Počítačů má kompletní historický záznam všech minulých transakcí, které kdy byly provedeny (a tedy přesné zůstatky bez falzifikátů), stejně jako sadu pravidel:
  - Ověřit, že transakce je řádně podepsána (klíčpasujezámek)
  - Vysílat a přijímat platné transakce od vrstevníků v síti, odmítnout neplatné (včetně jakýchkoli, které se pokusí utratit stejné prostředky dvakrát)
- Pravidelně aktualizovat/přidávat záznamy s novými transakcemi přijatými od "náhodného" počítače, pokud jsou všechny obsahy platné (poznámka: prozatím ignorujeme komponentu Důkaz práce (Proof of Work) ve všem tomto, pro jednoduchost), jinak tyto odmítnout a pokračovat jako dříve až do příštího "náhodného" počítače, který pošle aktualizaci
  - Byla odměněna správná částka, pokud byly obsahy platné.
- Zahrát si sekvenci událostí:
  - Zákazník- prohlíží obchod online a najde položku za 25 $, kterou chce, a informuje Obchodníka, že by ji rád zakoupil
  - Obchodník- požádá o platbu zasláním faktury/adresy ze své peněženky zákazníkovi.
  - Zákazník- sestaví transakci (odešle BTC v hodnotě 25 $ na adresu poskytnutou Obchodníkem) a vysílá ji do Bitcoinové sítě.
- Počítače- přijmou transakci a ověří:
  - Na odesílané adrese je alespoň 25 $ v BTC
  - Transakce je řádně podepsána ("odemčena" zákazníkem)
  - Pokud tomu tak není, transakce nebude šířena sítí, a pokud ano, pak se šíří a čeká na vyřízení.
  - Obchodníci mohou zkontrolovat, že transakce čeká na vyřízení.
- Jeden počítač je "náhodně" vybrán, aby navrhl finalizaci navrhované transakce vysíláním "bloku" obsahujícího ji; pokud to vyjde, obdrží odměnu v BTC.
  - VOLITELNÉ/POKROČILÉ - místo náhodného výběru Počítače simulujte těžbu tak, že Počítače hází kostkami, dokud nedojde k předem určenému výsledku (např. první, kdo hodí dvojitou šestku, je vybrán)
  - Může se také zahrát, co by se stalo, kdyby dva Počítače vyhrály přibližně současně, což by vedlo k rozdělení řetězce.
  - Počítače ověří platnost, aktualizují/přidají záznamy do svých účetních knih, pokud jsou pravidla splněna, a vysílají blok vrstevníkům.
  - Náhodně vybraný počítač obdrží odměnu za navržení platného bloku.
  - Obchodník zkontroluje, že transakce byla finalizována; tedy prostředky byly přijaty a položka byla zaslána zákazníkovi.
- Komentáře:
  - Všimněte si, že nebylo potřeba předchozího bankovního vztahu.
  - Není potřeba třetí strana k zprostředkování; nahrazeno kódem/incentivy.
  - Žádné sběr dat nikým mimo přímou výměnu a mezi účastníky musí být vyměněno pouze nezbytné množství (např. dodací adresa).
  - Mezi lidmi není vyžadována důvěra (kromě Obchodníka, který zasílá položku), podobně jako nákup za hotové peníze v mnoha ohledech.
  - Peníze přímo vlastní jednotlivci.
  - Bitcoinový účetní deník je zjednodušeně vyjádřen v dolarech, ale ve skutečnosti jde o BTC.
  - Simulujeme vysílání jedné transakce, ale ve skutečnosti je v síti čekajících více transakcí a bloky obsahují najednou tisíce transakcí. Uzly také kontrolují, zda nejsou čekající transakce dvojitého utrácení (v takovém případě bych všechny kromě jedné odmítl).
- Scénáře podvodu:
  - Co kdyby zákazník neměl 25 $ v BTC?
    - Nemohl by transakci vytvořit, protože "odemknutí" a "vlastnictví" jsou totéž a počítače kontrolují, zda je transakce řádně podepsána; v opačném případě ji odmítnou.
- Co když náhodně vybraný počítač se pokusí "změnit účetní knihu"? - Blok by byl odmítnut, protože každý další počítač má kompletní historii a všiml by si změny, což by porušilo jedno z jejich pravidel.
  - Náhodný počítač by nedostal odměnu a žádné transakce z jeho bloku by nebyly finalizovány.

## Hodnocení znalostí

<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>

### Diskuse v KA třídě

Diskutujte o některých zjednodušeních provedených při cvičení ve třídě pod druhým scénářem a popište, co skutečný systém Bitcoinu dělá podrobněji.

### Přezkum slovní zásoby KA

Definujte následující klíčové termíny představené v předchozí sekci:

- Uzel
- Mempool
- Cílová obtížnost
- Blok

**Diskutujte o významu některých dalších termínů jako skupina:**

Blockchain, Transakce, Dvojí utrácení, Byzantský generálův problém, Těžba, Důkaz práce (PoW), Hashovací funkce, Odměna za blok, Blockchain, Nejdelší řetězec, Útok 51%, Výstup, Zámek výstupu, Změna, Satoshi, Veřejný/Privátní klíč, Adresa, Kryptografie s veřejným klíčem, Digitální podpis, Peněženka

# Představení BTCPay Serveru

<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>

## Porozumění přihlašovací obrazovce BTCPay Serveru

<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>

### Práce s BTCPay Serverem

Cílem tohoto bloku kurzu bude mít obecné porozumění softwaru BTCPay Server. V sdíleném prostředí se doporučuje sledovat demonstraci instruktora a postupovat podle učebnice BTCPay Serveru, aby bylo možné následovat učitele. Naučíte se, jak vytvořit peněženku prostřednictvím několika metod. Příklady zahrnují nastavení Hot wallet a hardware peněženky připojené prostřednictvím BTCPay Server Vault. Tyto cíle se odehrávají v demo prostředí, které je zobrazeno a k němuž je poskytnut přístup vaším kursovým instruktorem.

Pokud budete tento kurz sledovat sami, najdete seznam hostitelů třetích stran pro účely demo na https://directory.btcpayserver.org/filter/hosts. Silně doporučujeme nepoužívat tyto možnosti třetích stran jako produkční prostředí, ale slouží správným účelům pro úvod do používání Bitcoinu a BTCPay Serveru.

Jako začínající hvězda BTCPay Serveru možná máte předchozí zkušenosti s nastavením Bitcoinového uzlu. Tento kurz bude konkrétně zaměřen na softwarový stack BTCPay Serveru.

Mnoho možností v BTCPay Serveru existuje v nějaké formě i v dalším softwaru souvisejícím s Bitcoinovými peněženkami.

### Přihlašovací obrazovka BTCPay Serveru

Jakmile vstoupíte do demo prostředí, budete vyzváni k „Přihlášení“ nebo „Vytvoření účtu“. Administrátoři serveru mohou z bezpečnostních důvodů vypnout možnost vytváření nových účtů. Loga a barvy tlačítek BTCPay Serveru lze změnit, protože BTCPay Server je Open Source Software. Hostitel třetí strany může software White-label a změnit celý vzhled.

![obrázek](assets/en/0.webp)

### Okno pro vytvoření účtu

Vytváření účtů na BTCPay Serveru vyžaduje platné řetězce e-mailových adres; example@email.com by byl platný řetězec pro e-mail.

Heslo musí být dlouhé alespoň 8 znaků, včetně písmen, čísel a znaků. Po nastavení hesla jednou budete muset ověřit zadané heslo, abyste se ujistili, že je správné ve srovnání s tím, co bylo zadáno v prvním poli pro heslo.
Když jsou pole Email a Heslo správně vyplněna, klikněte na tlačítko „Vytvořit účet“. Tím se uloží Email a heslo na instanci BTCPay Serveru instruktora.
![image](assets/en/1.webp)

**!Poznámka!**

Pokud tento kurz sledujete samostatně, vytvoření tohoto účtu by bylo něco, co byste mohli dělat na hostingu třetí strany; proto znovu zdůrazňujeme, abyste tyto prostředí nikdy nepoužívali jako produkční, ale pouze pro účely školení.

### Vytvoření účtu administrátorem BTCPay Serveru

Administrátor instance BTCPay Serveru může také vytvářet účty pro BTCPay Server. Administrátor instance BTCPay Serveru může kliknout na „Nastavení serveru“ (1), kliknout na záložku „Uživatelé“ (2) a kliknout na tlačítko „+ Přidat uživatele“ (3) v pravém horním rohu záložky Uživatelé. V Cíli (4.3) se dozvíte více o kontrolě účtů administrátorem.

![image](assets/en/2.webp)

Jako administrátor budete potřebovat emailovou adresu uživatele a nastavit standardní heslo. Doporučuje se, aby administrátor informoval uživatele, že by měl toto heslo změnit před použitím účtu z bezpečnostních důvodů. Pokud administrátor nenastaví heslo a na serveru je nastaven SMTP, uživatel obdrží email s odkazem na vytvoření svého účtu a nastavení hesla.

### Příklad

Pokud kurz sledujete pod vedením instruktora, postupujte podle odkazu poskytnutého instruktorem a vytvořte svůj účet v demo prostředí. Ujistěte se, že vaše emailová adresa a heslo jsou bezpečně uloženy; tyto přihlašovací údaje budete potřebovat pro zbytek demo cílů v tomto kurzu.

Váš instruktor mohl shromáždit emailové adresy předem a poslat odkaz na pozvánku před tímto cvičením. Pokud bylo instruováno, zkontrolujte svůj email.

Pokud kurz absolvujete bez instruktora, vytvořte svůj účet pomocí demo prostředí BTCPay Serveru; přejděte na

https://mainnet.demo.btcpayserver.org/login.

Tento účet by měl být používán pouze pro demonstrační/školicí účely a nikdy pro podnikání.

### Shrnutí dovedností

V této sekci jste se naučili následující:

- Jak vytvořit účet na hostovaném serveru prostřednictvím rozhraní.
- Jak může administrátor serveru ručně přidávat uživatele v nastavení serveru.

### Hodnocení znalostí

#### KA Konceptuální přezkum

Uveďte důvody, proč je špatný nápad používat Demo Server pro produkční účely.

## Správa uživatelského účtu

<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>

### Správa účtu na BTCPay Serveru

Po vytvoření účtu majitelem obchodu může tento svůj účet spravovat v levém dolním rohu uživatelského rozhraní BTCPay Serveru. Pod tlačítkem Účet se nachází několik nastavení vyšší úrovně.

- Tmavý/Světlý režim.
- Přepínač Skrýt citlivé informace.
- Správa účtu.

![image](assets/en/3.webp)

### Tmavý a světlý režim

Uživatelé BTCPay Serveru si mohou vybrat mezi světlou nebo tmavou verzí uživatelského rozhraní. Stránky zaměřené na zákazníky se nezmění. Používají nastavení zákazníka týkající se tmavého nebo světlého režimu.

### Přepínač Skrýt citlivé informace

Tlačítko Skrýt citlivé informace přináší rychlou a jednoduchou vrstvu bezpečnosti. Kdykoli potřebujete pracovat s vaším BTCPay Serverem, ale mohou být lidé, kteří na vás koukají přes rameno ve veřejném prostoru, zapněte Skrýt citlivé informace a všechny hodnoty v BTCPay Serveru budou skryty. Někdo se může dívat přes vaše rameno, ale už nebude vidět hodnoty, se kterými pracujete.

### Správa účtu

Jakmile byl uživatelský účet vytvořen, zde můžete spravovat hesla, 2fa nebo API klíče.

### Správa účtu - Účet

Volitelně aktualizujte váš účet s jinou e-mailovou adresou. Aby bylo zajištěno, že vaše e-mailová adresa je správná, BTCPay Server umožňuje poslat ověřovací e-mail. Klikněte na uložit, pokud uživatel nastaví novou e-mailovou adresu a potvrdí, že ověření proběhlo úspěšně. Uživatelské jméno zůstává stejné jako předchozí e-mail.

Uživatel se může rozhodnout smazat celý svůj účet. To lze provést kliknutím na tlačítko smazat na kartě Účet.

![obrázek](assets/en/4.webp)

**!Poznámka!**

Po změně e-mailu se uživatelské jméno účtu nezmění. Předchozí zadaná e-mailová adresa zůstane jako přihlašovací jméno.

### Správa účtu - Heslo

Student si může přát změnit své heslo. Může tak učinit přechodem na kartu Heslo. Zde musí zadat své staré heslo a může ho změnit na nové.

![obrázek](assets/en/5.webp)

### Dvoufaktorové ověření (2fa)

Aby se omezily důsledky ukradeného hesla, můžete použít dvoufaktorové ověření (2fa), relativně novou bezpečnostní metodu. Dvoufaktorové ověření můžete aktivovat přes Správu účtu a kartu pro dvoufaktorové ověření. Po přihlášení pomocí uživatelského jména a hesla musíte dokončit druhý krok.

BTCPay Server umožňuje dvě způsoby aktivace 2FA, App-based 2FA (Authy, Google, Microsoft autentizátory) nebo prostřednictvím Bezpečnostních zařízení (FIDO2 nebo LNURL Auth).

### Dvoufaktorové ověření - Založené na aplikaci

Na základě operačního systému vašeho mobilního telefonu (Android nebo iOS) si uživatelé mohou vybrat mezi následujícími aplikacemi;

1. Stáhněte si dvoufaktorový autentizátor;
   - Authy pro [Android](https://play.google.com/store/apps/details?id=com.authy.authy) nebo [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator pro [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) nebo [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator pro [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) nebo [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)
2. Po stažení a instalaci aplikace Authenticator.
   - Naskenujte QR kód poskytnutý BTCPay Serverem
   - Nebo ručně zadejte vygenerovaný klíč od BTCPay Serveru do vaší aplikace Authenticator.
3. Aplikace Authenticator vám poskytne jedinečný kód. Zadejte jedinečný kód do BTCPay Serveru k ověření nastavení a klikněte na ověřit pro dokončení procesu.

![obrázek](assets/en/6.webp)

### Shrnutí dovedností

V této sekci jste se naučili následující:

- Možnosti správy účtu a různé způsoby, jak spravovat účet na instanci BTCPay Serveru.
- Jak nastavit app-based 2FA.

### Hodnocení znalostí

#### KA Konceptuální přezkum

Popište, jak app-based 2FA pomáhá zabezpečit váš účet

## Vytvoření nového obchodu

<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>

### Průvodce vytvořením vašeho obchodu

Když se nový uživatel přihlásí do BTCPay Serveru, prostředí je prázdné a je potřeba vytvořit první obchod. Úvodní průvodce BTCPay Serveru uživateli nabídne možnost „Vytvořit váš obchod“ (1). Obchod lze chápat jako Domov pro vaše potřeby s Bitcoinem. Nový uzel BTCPay Serveru začne se synchronizací Bitcoin Blockchainu (2). V závislosti na infrastruktuře, na které BTCPay Server běží, může toto trvat od několika hodin po několik dní. Aktuální verze instance je zobrazena v pravém dolním rohu uživatelského rozhraní BTCPay Serveru. To je užitečné pro referenci při řešení problémů.
![obrázek](assets/en/7.webp)

### Průvodce vytvořením obchodu

Následování tohoto kurzu začne mírně odlišnou obrazovkou než předchozí stránka. Jelikož váš instruktor připravil Demo prostředí, Bitcoin blockchain byl synchronizován předem, a proto neuvidíte stav synchronizace uzlů.

Uživatel se může rozhodnout smazat celý svůj účet. To lze provést kliknutím na tlačítko smazat na kartě Účet.

![obrázek](assets/en/8.webp)

**!Poznámka!**

Účty BTCPay Serveru mohou vytvářet neomezené množství obchodů. Každý obchod je peněženka nebo „domov“.

### Příklad

Začněte kliknutím na "Vytvořit váš obchod".

![obrázek](assets/en/9.webp)

Tím vytvoříte svůj první Domov a řídicí panel pro používání BTCPay serveru.

(1) Po kliknutí na "Vytvořit váš obchod" bude BTCPay Server vyžadovat, abyste obchodu dali název; to může být cokoli, co je pro vás užitečné.

![obrázek](assets/en/10.webp)

(2) Dále je nutné nastavit výchozí měnu obchodu, buď fiat měnu nebo denominovanou v Bitcoinu / Sats standardu. Pro demo prostředí to nastavíme na USD.

![obrázek](assets/en/11.webp)

(3) Jako poslední parametr nastavení obchodu vyžaduje BTCPay Server, abyste nastavili "Preferovaný zdroj ceny" pro porovnání ceny Bitcoinu s aktuální fiat cenou, aby váš obchod zobrazoval správný směnný kurz mezi Bitcoinem a měnou nastavenou pro obchod. V demo příkladu se držíme výchozího nastavení a zvolíme burzu Kraken. BTCPay Server používá API Kraken k ověření směnných kurzů.

![obrázek](assets/en/12.webp)

(4) Nyní, když byly tyto parametry obchodu nastaveny, klikněte na tlačítko Vytvořit a BTCPay Server vytvoří řídicí panel vašeho prvního obchodu, kde průvodce pokračuje.

![obrázek](assets/en/13.webp)

Gratulujeme, vytvořili jste svůj první obchod, a tím je toto cvičení ukončeno.

![obrázek](assets/en/14.webp)

### Shrnutí dovedností

V této sekci jste se naučili:

- Vytvoření obchodu a konfigurace výchozí měny kombinované s preferencemi zdroje ceny.
- Každý "Obchod" je nový domov oddělený od ostatních obchodů na této instalaci BTCPay Serveru.

# Úvod do zabezpečení Bitcoin klíčů

<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>

## Porozumění generování Bitcoin klíčů

<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>

### Co zahrnuje generování bitcoinových klíčů?

Bitcoinové peněženky při vytváření generují takzvané "semeno". V posledním cíli jste vytvořili "semeno", Série slov generovaných předtím jsou také známé jako mnemonické fráze. Semeno se používá k odvození jednotlivých Bitcoin klíčů a k odesílání nebo přijímání Bitcoinu. Semenné fráze by nikdy neměly být sdíleny s třetími stranami nebo nedůvěryhodnými vrstevníky.
Generování seedu probíhá podle průmyslového standardu známého jako "Hierarchical Deterministic" (HD) framework.
![image](assets/en/15.webp)

### Adresy

BTCPay Server je navržen tak, aby generoval novou Adresu. To řeší problém s opakovaným používáním veřejného klíče nebo Adresy. Používání stejného veřejného klíče usnadňuje sledování celé historie vašich plateb. Považování klíčů za poukázky na jedno použití by výrazně zlepšilo vaše soukromí. Používáme také Bitcoinové Adresy, nepleťte si je s veřejnými klíči.

Adresa je odvozena z veřejného klíče pomocí "hashovacího algoritmu". Většina peněženek a transakcí však zobrazuje Adresy místo těchto veřejných klíčů. Adresy jsou obecně kratší než veřejné klíče a obvykle začínají `1`, `3`, nebo `bc1`, zatímco veřejné klíče začínají `02`, `03`, nebo `04`.

- Adresy začínající na `1.....` jsou stále velmi běžné adresy. Jak je zmíněno v kapitole Vytvoření nového obchodu, jedná se o legacy adresy. Tento typ adresy je určen pro P2PKH transakce. P2Pkh používá kódování Base58, což znamená, že adresa je citlivá na velikost písmen. Její struktura je založena na veřejném klíči s přidanou jednou číslicí jako identifikátorem.

- Adresy začínající na `bc1...` se pomalu stávají velmi běžnými adresami. Jsou známé jako (nativní) SegWit Adresy. Tyto nabízejí lepší strukturu poplatků než ostatní zmíněné Adresy. Nativní SegWit Adresy používají kódování Bech32 a umožňují pouze malá písmena.

- Adresy začínající na `3...` jsou běžně stále používány burzami pro vkladové adresy. Tyto adresy jsou zmíněny v kapitole Vytvoření nového obchodu, jako obalené nebo vnořené SegWit adresy. Mohou však také fungovat jako "Multisig Adresa". Když jsou použity jako SegWit adresa, opět dochází k úsporám na transakčních poplatcích, i když méně než u Nativního SegWit. P2SH Adresy používají kódování Base58. To znamená, že jsou citlivé na velikost písmen, stejně jako legacy adresa.

- Adresy začínající na `2...` jsou Testnet adresy. Jsou určeny pro příjem testnet bitcoinů (tBTC). Nikdy byste je neměli zaměňovat a posílat na tyto adresy Bitcoin. Pro vývojové účely můžete vygenerovat testnet peněženku. Online existuje několik zdrojů pro získání testnet Bitcoinu. Nikdy nekupujte Testnet Bitcoin. Testnet Bitcoin se těží. To může být důvod, proč by vývojář místo toho mohl použít Regtest. Jedná se o vývojové prostředí pro vývojáře, kterému chybí určité síťové komponenty. Bitcoin je však pro vývojové účely velmi užitečný.

### Veřejné klíče

Veřejné klíče se v praxi dnes používají méně. S postupem času je uživatelé bitcoinu nahrazují Adresami. Stále však existují a občas se používají. Veřejné klíče jsou obecně mnohem delší řetězce než adresy. Stejně jako u adres, začínají specifickým identifikátorem.

- Nejprve, `02...` a `03...` jsou velmi standardní identifikátory veřejných klíčů zakódované ve formátu SEC. Tyto lze zpracovat a převést na adresy pro příjem, použít pro vytváření multi-sig adres nebo ověřit podpis. Transakce Bitcoinu z raných dnů používaly veřejné klíče jako součást P2PK transakcí.

- HD peněženky však používají odlišnou strukturu. `xpub...`, `ypub...` nebo `zpub...` jsou nazývány rozšířené veřejné klíče, často označované jako xpubs. Tyto klíče slouží k odvození mnoha veřejných klíčů, protože jsou součástí HD peněženky. Jelikož váš xpub obsahuje záznamy o celé vaší historii, tedy o minulých i budoucích transakcích, nikdy je nesdílejte s nedůvěryhodnými stranami.

### Shrnutí dovedností

V této sekci jste se naučili následující:

- Rozdíly mezi adresami a datovými typy veřejných klíčů a výhody používání adres oproti veřejným klíčům.

### Hodnocení znalostí

Popište výhodu používání nových adres pro každou transakci ve srovnání s opakovaným používáním adres nebo metodami veřejných klíčů.

## Zabezpečení klíčů pomocí hardwarové peněženky

<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>

### Ukládání klíčů Bitcoinu

Po vygenerování seed phrase, seznamu 12 - 24 slov vygenerovaných v této knize, je vyžadováno řádné zálohování a zabezpečení, protože tyto slova jsou jediným způsobem, jak obnovit přístup k peněžence. Struktura HD peněženek a způsob, jakým deterministicky generuje adresy pomocí jednoho seedu, všechny vaše vytvořené adresy budou zálohovány pomocí tohoto jednoho seznamu mnemonických slov reprezentujících váš seed nebo obnovovací frázi.

Uchovávejte svou obnovovací frázi v bezpečí. Pokud k ní získá přístup někdo, zejména s škodlivými úmysly, může přesunout vaše prostředky. Uchování seedu v bezpečí a zároveň si jej pamatovat je vzájemně propojené. Existuje několik metod, jak ukládat soukromé klíče Bitcoinu, každá s výhodami a nevýhodami, ať už z hlediska bezpečnosti, soukromí, pohodlí nebo fyzických prostředků. Kvůli důležitosti soukromých klíčů mají uživatelé bitcoinů tendenci ukládat a bezpečně chránit tyto klíče v „vlastní správě“ místo používání „opatrovnických“ služeb, jako jsou banky. V závislosti na uživateli musí použít buď řešení pro studené ukládání nebo teplou peněženku.

### Teplé a studené ukládání klíčů bitcoinu

Obvykle jsou bitcoinové peněženky označovány jako Teplá peněženka nebo Studená peněženka. Většina kompromisů spočívá v pohodlí, snadnosti použití a bezpečnostních rizicích. Každá z těchto metod může být také viděna v opatrovnickém řešení. Avšak kompromisy zde jsou většinou založeny na bezpečnosti a soukromí a přesahují rámec tohoto kurzu.

### Teplá peněženka

Teplé peněženky jsou nejpohodlnějším způsobem interakce s Bitcoinem prostřednictvím mobilních, webových nebo desktopových softwarů. Peněženka je vždy připojena k internetu, což uživatelům umožňuje posílat nebo přijímat Bitcoin. To je však také její slabina, peněženka, jelikož je vždy online, je nyní více zranitelná vůči útokům hackerů nebo malwaru na vašem zařízení. V BTCPay Serveru teplé peněženky ukládají soukromé klíče na instanci. Každý, kdo získá přístup k vašemu obchodu BTCPay Server, by mohl v případě škodlivých úmyslů ukrást prostředky z této adresy. Když BTCPay Server běží v hostovaném prostředí, měli byste to vždy zvážit ve vašem bezpečnostním profilu a v takovém případě raději nepoužívat Teplou peněženku. Když je BTCPay Server nainstalován na vlastním hardwaru, který je zabezpečený a důvěryhodný pro vás, rizikový profil se výrazně snižuje, ale nikdy nezmizí!

### Studená peněženka

Jednotlivci přesouvají své Bitcoiny do studené peněženky, protože může izolovat soukromé klíče od internetu. Odstranění internetového připojení ze rovnice snižuje riziko malwaru, spywaru a SIM swapů. Studené ukládání se považuje za bezpečnější než teplé ukládání z hlediska bezpečnosti a autonomie, pokud jsou přijata adekvátní opatření k zabránění ztrátě soukromých klíčů Bitcoinu. Studené ukládání je nejvhodnější pro velké množství Bitcoinů, které nejsou určeny k častému utrácení kvůli složitosti nastavení peněženky.

Existuje několik metod, jak ukládat klíče Bitcoinu v studeném ukládání, od papírových peněženek po brain peněženky, hardwarové peněženky nebo, od začátku, soubor peněženky. Většina peněženek používá BIP 39 pro generování seed phrase. Avšak uvnitř softwaru Bitcoin Core dosud nebyl dosažen konsenzus o jeho používání. Software Bitcoin Core stále generuje soubor Wallet.dat, který potřebujete uložit na bezpečném offline místě.

### Shrnutí dovedností

V této sekci jste se naučili:

- Rozdíly mezi teplými a studenými peněženkami z hlediska funkčnosti a jejich kompromisů.

### Hodnocení znalostí Konceptuální přehled

- Co je peněženka?
- Jaký je rozdíl mezi hot a cold peněženkami?

- Popište, co se myslí "generováním peněženky"?

## Používání vašich Bitcoin klíčů

<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>

### BTCPay Server Peněženka

BTCPay Server obsahuje následující standardní funkce peněženky:

- Transakce
- Odeslat
- Přijmout
- Rescan
- Pull Platby
- Výplaty
- PSBT
- Obecná nastavení

### Transakce

Administrátoři mohou vidět příchozí a odchozí transakce pro on-chain peněženku připojenou k tomuto konkrétnímu obchodu v zobrazení transakcí. Každá transakce má rozlišení mezi přijatými a odeslanými. Přijaté budou zelené a odchozí transakce budou červené. V zobrazení transakcí BTCPay Serveru uvidí administrátoři také sadu standardních štítků.

| Typ transakce   | Popis                                                          |
| --------------- | -------------------------------------------------------------- |
| App             | Platba byla přijata prostřednictvím faktury vytvořené aplikací |
| invoice         | Platba byla přijata prostřednictvím faktury                    |
| payjoin         | Nebylo zaplaceno, časovač faktury ještě nevypršel              |
| payjoin-exposed | UTXO bylo odhaleno prostřednictvím návrhu payjoin faktury      |
| payment-request | Platba byla přijata prostřednictvím žádosti o platbu           |
| payout          | Platba byla odeslána prostřednictvím výplaty nebo refundace    |

### Jak odeslat

Funkce odeslání BTCPay serveru odesílá transakce z vaší on-chain peněženky BTCPay Serveru. BTCPay Server umožňuje několik způsobů podepisování vašich transakcí pro vynaložení prostředků. Transakce může být podepsána pomocí;

- Hardware Peněženka
- Peněženky podporující PSBT
- HD soukromý klíč nebo obnovovací semena.
- Hot Peněženka

#### Hardware peněženka

BTCPay Server má vestavěnou podporu hardware peněženek, která vám umožňuje používat vaši hardware peněženku s BTCPay Vault bez úniku informací do aplikací nebo serverů třetích stran. Integrace hardware peněženky v BTCPay Serveru vám umožňuje importovat vaši hardware peněženku a utrácet příchozí prostředky s jednoduchým potvrzením na vašem zařízení. Vaše soukromé klíče nikdy neopustí zařízení a všechny prostředky jsou ověřovány proti vašemu full node, takže nedochází k úniku dat.

#### Podepisování peněženkou podporující PSBT

PSBT (Partially Signed Bitcoin Transactions) je výměnný formát pro Bitcoin transakce, které ještě musí být plně podepsány. PSBT je podporován v BTCPay Serveru a může být podepsán kompatibilními hardware a software peněženkami.

Konstrukce plně podepsané Bitcoin transakce probíhá následujícími kroky:

- PSBT je sestaven s konkrétními vstupy a výstupy, ale bez podpisů
- Exportovaný PSBT může být importován peněženkou, která podporuje tento formát
- Data transakce mohou být prohlédnuta a podepsána pomocí peněženky
- Podepsaný soubor PSBT je exportován z peněženky a importován do BTCPay Serveru
- BTCPay Server vytvoří konečnou Bitcoin transakci
- Ověříte výsledek a vysíláte jej do sítě

#### Podepisování pomocí HD soukromého klíče nebo mnemonického semínka

Pokud jste předtím vytvořili peněženku pomocí BTCPay Serveru, můžete prostředky utratit zadáním vašeho soukromého klíče do příslušného pole. Nastavte správnou "AccountKeyPath" v nastavení peněženky; jinak nemůžete utrácet.

#### Podepisování pomocí hot peněženky

Pokud jste při nastavování vašeho obchodu vytvořili novou peněženku a povolili ji jako hot peněženku, bude automaticky používat semínko uložené na serveru pro podepisování.

### RBF (Replace-By-Fee)

Replace-By-Fee (RBF) je funkce protokolu Bitcoin, která vám umožňuje nahradit dříve odeslanou transakci (která ještě nebyla potvrzena). To umožňuje náhodně měnit otisk transakce vaší peněženky nebo ji nahradit transakcí s vyšším poplatkem, aby se transakce posunula výše ve frontě na potvrzení (priorita těžby). To efektivně nahradí původní transakci, protože transakce s vyšším poplatkem bude mít prioritu, a jakmile bude potvrzena, původní transakce bude neplatná (nedojde k dvojímu utracení).
Stiskněte tlačítko "Pokročilé nastavení", abyste zobrazili možnosti RBF;

![image](assets/en/16.webp)

- Náhodně pro vyšší soukromí, umožňuje transakci být automaticky nahrazena pro náhodnou změnu otisku transakce.
- Ano, Označit transakci pro RBF a být explicitně nahrazena (Není nahrazena automaticky, pouze na základě vstupu)
- Ne, Neumožnit nahrazení transakce.

### Výběr mincí

Výběr mincí je pokročilá funkce zvyšující soukromí, která vám umožňuje vybrat mince, které chcete utratit při vytváření transakce. Například platba mincemi, které jsou čerstvé z mixu spojení.

Výběr mincí funguje přímo s funkcí štítků peněženky. To vám umožňuje označit příchozí prostředky pro hladší správu a utrácení UTXO.

BTCPay Server také podporuje BIP-329 pro správu štítků. BIP-329 umožňuje štítky na; pokud převádíte z peněženky podporující tento konkrétní BIP a nastavíte štítky, BTCPay Server je rozpozná a importuje je. Při migraci serverů lze tyto informace také exportovat a importovat do nového prostředí.

### Jak přijímat

Když kliknete na tlačítko přijmout v BTCPay Serveru, vygeneruje se nepoužitá adresa, která může být použita k přijímání plateb. Administrátoři mohou také vygenerovat novou adresu vytvořením nové "Faktury".

BTCPay Server vždy požádá o vygenerování další dostupné adresy, aby se zabránilo opětovnému použití adresy. Po kliknutí na "Vygenerovat další dostupnou BTC adresu" BTCPay Server vygeneroval novou adresu a QR. Umožňuje také přímo nastavit Štítek k adrese pro lepší správu vašich adres.

![image](assets/en/17.webp)

![image](assets/en/18.webp)

#### Nové skenování

Funkce Nové skenování využívá "Scantxoutset" z Bitcoin Core 0.17.0 pro skenování aktuálního stavu blockchainu (nazývaného UTXO Set) pro mince patřící do konfigurovaného schématu derivace. Nové skenování peněženky řeší dva problémy, které uživatelé BTCPay Serveru zažívají.

1. Problém s limitem mezery - Většina peněženek třetích stran jsou lehké peněženky, které sdílejí uzel mezi mnoha uživateli. Lehké a na uzlech závislé peněženky omezují množství (typicky 20) adres bez zůstatku, které sledují na blockchainu, aby předešly problémům s výkonem. BTCPay Server generuje novou adresu pro každou fakturu. S výše uvedeným na mysli, po vygenerování 20 po sobě jdoucích nezaplacených faktur, externí peněženka přestane načítat transakce, předpokládajíc, že nedošlo k žádným novým transakcím. Vaše externí peněženka je nezobrazí, jakmile budou faktury zaplaceny na 21., 22. atd. Na druhou stranu, interně peněženka BTCPay Serveru sleduje jakoukoli adresu, kterou generuje, spolu s mnohem větším limitem mezery. Nezávisí na třetí straně a vždy může ukázat správný zůstatek.
2. Řešení s limitem mezery - Pokud váš [externí/stávající peněženka](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-wallet) umožňuje konfiguraci limitu mezery, snadným řešením je jeho zvýšení. Většina peněženek to však neumožňuje. Jediné peněženky, o kterých víme, že umožňují nastavení limitu mezery, jsou Electrum, Wasabi a Sparrow Wallet. Bohužel u mnoha dalších peněženek pravděpodobně narazíte na problém. Pro nejlepší uživatelský zážitek a soukromí zvažte opuštění externích peněženek a použití interní peněženky BTCPay Serveru.

#### BTCPay Server používá “mempoolfullrbf=1”

BTCPay Server používá “mempoolfullrbf=1”; toto nastavení jsme přidali jako výchozí do vaší konfigurace BTCPay Serveru. Nicméně jsme to také udělali fragmentem, který si můžete sami vypnout. Bez “mempoolfullrbf=1”, pokud zákazník provede dvojí utrácení platby s transakcí, která neoznačuje RBF, obchodník by se dozvěděl až po potvrzení.

Administrátor se může rozhodnout toto nastavení vypnout. Následujícím řetězcem můžete změnit výchozí nastavení.

```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCLUDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i**
```

### Nastavení peněženky BTCPay Serveru

Nastavení peněženky v BTCPay Serveru poskytuje jasný a rychlý přehled o obecných nastaveních vaší peněženky. Všechna tato nastavení jsou předvyplněna, pokud byla peněženka vytvořena s BTCPay Serverem.

![image](assets/en/19.webp)

Nastavení peněženky v BTCPay Serveru poskytuje jasný a rychlý přehled o obecných nastaveních vaší peněženky. Všechna tato nastavení jsou předvyplněna, pokud byla peněženka vytvořena s BTCPay Serverem. Nastavení peněženky BTCPay Serveru začíná stavem peněženky. Je to Watch-only nebo Hot peněženka? V závislosti na typu peněženky se mohou akce lišit od opětovného skenování peněženky pro chybějící transakce, prořezávání starých transakcí z historie, registrace peněženky pro platební odkazy, nebo nahrazení a smazání aktuální peněženky připojené k obchodu. V nastavení peněženky BTCPay Serveru mohou administrátoři nastavit Štítek pro lepší správu peněženky. Zde Administrátor také uvidí Schéma derivace, klíč účtu (xpub), Otisk prstu a Cestu klíče. Platby v nastavení peněženky mají pouze 2 hlavní nastavení. Platba je neplatná, pokud transakce nebyla potvrzena (nastavené minuty) po vypršení faktury. Faktura se považuje za potvrzenou, když má transakce platby X počet potvrzení. Administrátoři mohou také nastavit přepínač pro zobrazení doporučených poplatků u plateb nebo nastavit ruční cíl potvrzení v počtu bloků.

![image](assets/en/20.webp)

**!Poznámka!**

Pokud budete tento kurz sledovat sami, vytvoření tohoto účtu by bylo něco, co byste mohli udělat na hostingu třetí strany, proto znovu zdůrazňujeme, abyste tyto nikdy nepoužívali jako produkční prostředí, ale pouze pro účely školení.

### Příklad

#### Nastavení Bitcoinové peněženky v BTCPay Serveru

BTCPay Server umožňuje dva způsoby nastavení peněženky. Jedním způsobem je import již existující Bitcoinové peněženky. Import lze provést připojením hardwarové peněženky, importem souboru peněženky, zadáním Rozšířeného veřejného klíče, skenováním QR kódu peněženky, nebo nejméně vhodným způsobem, ručním zadáním dříve vytvořeného obnovovacího seedu peněženky. V BTCPay Serveru je také možné vytvořit novou peněženku. Existují dva možné způsoby konfigurace BTCPay Serveru při generování nové peněženky.
Možnost "hot wallet" v BTCPay Serveru umožňuje funkce jako 'Payjoin' nebo 'Liquid'. Má to však nevýhodu, že obnovovací seed generovaný pro tuto peněženku bude uložen na serveru, kde může kdokoli, kdo má kontrolu Admina, získat obnovovací seed. Jelikož je váš soukromý klíč odvozen od vašeho obnovovacího seedu, zlý aktér by mohl získat přístup k vašim současným i budoucím prostředkům!
Aby se takové riziko v BTCPay Serveru zmírnilo, může Admin nastavit v Nastavení serveru > Zásady > "Povolit ne-adminům vytvářet hot wallets pro jejich obchody" na ne, jak je to ve výchozím nastavení. Pro zvýšení bezpečnosti těchto Hot wallets by měl správce serveru povolit 2FA autentizaci na účtech, kterým je dovoleno mít Hot wallets. Ukládání soukromých klíčů na veřejném serveru je nebezpečné a nese rizika. Některá jsou podobná rizikům Lightning Network (viz další kapitola o rizicích Lightning Network).

Druhou možností, kterou BTCPay Server nabízí při generování nové peněženky, je vytvoření peněženky pouze pro sledování (Watch-Only wallet). BTCPay Server jednou vygeneruje vaše soukromé klíče. Poté, co uživatel potvrdí, že si zapsal svou Seed Phrase, BTCPay Server smaže soukromé klíče ze serveru. Výsledkem je, že váš obchod nyní má peněženku pouze pro sledování připojenou k němu. Pro utrácení prostředků přijatých na vaší peněžence pouze pro sledování, viz kapitola Jak poslat, buď pomocí BTCPay Server Vault, PSBT (částečně podepsaná bitcoinová transakce), nebo, což se doporučuje nejméně, ručním poskytnutím vaší seed phrase.

V poslední části jste vytvořili nový 'Obchod'. Instalační průvodce bude pokračovat dotazem na "Nastavit peněženku" nebo "Nastavit Lightning node". V tomto příkladu budete postupovat podle procesu průvodce "Nastavit peněženku" (1).

![obrázek](assets/en/21.webp)

Po kliknutí na "Nastavit peněženku" bude průvodce pokračovat dotazem, jak chcete pokračovat; BTCPay Server nyní nabízí možnost připojit existující Bitcoinovou peněženku k vašemu novému obchodu. Pokud nemáte peněženku, BTCPay Server navrhuje vytvoření nové. Tento příklad bude postupovat podle kroků pro "vytvoření nové peněženky" (2). Postupujte podle kroků, abyste se naučili, jak "Připojit existující peněženku" (1).

![obrázek](assets/en/22.webp)

**!Poznámka!**

Pokud tento kurz absolvujete ve třídě, současný příklad a vygenerovaný seed jsou pouze pro vzdělávací účely. Na těchto adresách by nikdy nemělo být žádné významné množství jiné než požadované během cvičení.

(1) Pokračujte v průvodci "Nová peněženka" kliknutím na tlačítko "Vytvořit novou peněženku".

![obrázek](assets/en/23.webp)

(2) Po kliknutí na „Vytvořit novou peněženku“ vám další okno průvodce nabídne možnosti „Hot wallet“ a „Watch-only wallet“. Pokud postupujete podle instruktora, vaše prostředí je sdílená Demo verze, a můžete vytvořit pouze peněženku pouze pro sledování. Všimněte si rozdílu mezi oběma níže uvedenými obrázky. Jelikož jste v Demo prostředí a postupujete podle instruktora, vytvořte "Watch-only wallet" a pokračujte v průvodci "Nová peněženka".

![obrázek](assets/en/24.webp)

![obrázek](assets/en/25.webp)

(3) Pokračujete v průvodci novou peněženkou, nyní jste v sekci Vytvoření BTC peněženky pouze pro sledování. Zde máme možnost nastavit typ adresy peněženky "Address type", BTCPay Server vám umožňuje vybrat váš preferovaný typ adresy; v době psaní tohoto kurzu se stále doporučuje používat adresy bech32. Dozvíte se více o adresách v první kapitole této části.

- Segwit (bech32)
- Native SegWit jsou adresy, které začínají na `bc1q`. - Příklad: `bc1qXXXXXXXXXXXXXXXXXXXXXX`
- Legacy
  - Legacy adresy jsou adresy, které začínají číslem `1`.
  - Příklad: `15e15hXXXXXXXXXXXXXXXXXXXX`
- Taproot (Pro pokročilé uživatele)
  - Adresy Taproot začínají na `bc1p`.
  - Příklad: `bc1pXXXXXXXXXXXXXXXXXXXXXXXX`
- Segwit wrapped
  - Adresy Segwit wrapped začínají na `3`.
  - Příklad: `37BBXXXXXXXXXXXXXXX`

Vyberte segwit (doporučeno) jako preferovaný typ adresy vaší peněženky.

![obrázek](assets/en/26.webp)

(4) Při nastavování parametrů pro Peněženku umožňuje BTCPay Server uživatelům nastavit volitelnou heslovou frázi prostřednictvím BIP39, nezapomeňte potvrdit své heslo.

![obrázek](assets/en/27.webp)

(5) Po nastavení typu adresy Peněženky a možném nastavení některých pokročilých možností klikněte na Vytvořit, a BTCPay Server vygeneruje vaši novou Peněženku. Všimněte si, že toto je poslední krok před generováním vaší Seed fráze. Ujistěte se, že toto děláte v prostředí, kde vám nikdo nemůže ukrást seed frázi tím, že se podívá na váš obrazovku.

![obrázek](assets/en/28.webp)

(6) Na následující obrazovce průvodce BTCPay Server ukazuje Recovery seed frázi pro vaši nově vygenerovanou Peněženku; to jsou klíče k obnovení vaší Peněženky a podepisování transakcí. BTCPay Server generuje seed frázi o 12 slovech. Tato slova budou ze serveru odstraněna po této nastavovací obrazovce. Tato Peněženka je specificky Peněženka pouze pro sledování. Doporučuje se neukládat tuto seed frázi digitálně ani fotograficky. Uživatelé mohou v průvodci pokračovat pouze pokud aktivně potvrdí, že si svou seed frázi zapsali.

![obrázek](assets/en/29.webp)

(7) Po kliknutí na Hotovo a zabezpečení nově vygenerované Bitcoinové seed fráze, BTCPay Server aktualizuje váš obchod s připojenou novou Peněženkou a je připraven přijímat platby. V uživatelském rozhraní, v levém navigačním menu, si všimněte, jak je nyní Bitcoin zvýrazněn a aktivován pod Peněženkou.

![obrázek](assets/en/30.webp)

### Příklad: Zápis seed fráze

To je velmi specifický a bezpečný okamžik pro používání Bitcoinu. Jak bylo řečeno dříve, pouze vy byste měli mít přístup nebo vědomosti o vaší seed frázi. Jak budete postupovat společně s instruktorem a třídou, vygenerovaná seed by měla být použita pouze v tomto kurzu. Příliš mnoho faktorů, jako jsou zvědavé oči spolužáků, nezabezpečené systémy a mnoho dalších, dělá tyto klíče pouze vzdělávacími a nedůvěryhodnými. Klíče by však měly být stále uloženy pro příklady v kurzu.

První metoda, kterou v současné situaci použijeme, také ta nejméně bezpečná, je zapsání seed fráze ve správném pořadí. Karta Seed fráze je součástí kursových materiálů poskytnutých studentovi nebo nalezených na GitHubu BTCPay Serveru. Tuto kartu použijeme k zapsání slov vygenerovaných v předchozím kroku. Ujistěte se, že je zapisujete ve správném pořadí. Po jejich zapsání je zkontrolujte proti tomu, co bylo poskytnuto softwarem, abyste se ujistili, že jste je zapsali ve správném pořadí. Jakmile je máte zapsané, zaškrtněte políčko, které uvádí, že jste svou seed frázi správně zapsali.

### Příklad: Ukládání seed fráze na Hardware Wallet

V tomto kurzu se dotýkáme ukládání seed fráze na hardware peněženku. Následování tohoto kurzu instruktorem nemusí vždy zahrnovat takové zařízení. V materiálech kurzu je napsán seznam hardware peněženek, které by se hodily pro toto cvičení.
V tomto příkladu použijeme BTCPay Server vault a hardware peněženku Blockstream Jade.
Můžete také sledovat video pro návod, jak připojit hardware peněženku.
![BTCPay Server - Jak připojit vaši hardware peněženku k BTCPay Vault.](https://youtu.be/s4qbGxef43A)

Stáhněte si BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases

Ujistěte se, že stahujete správné soubory pro váš systém. Uživatelé Windows by měli stáhnout balíček [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), uživatelé Mac stáhnou [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg) a uživatelé Linuxu by měli stáhnout [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)

Po instalaci BTCPay Server Vault spusťte software kliknutím na ikonu na vaší ploše. Když je BTCPay Server Vault správně nainstalován a spuštěn poprvé, požádá o povolení k použití s webovými aplikacemi. Bude požadovat udělení přístupu k určitému BTCPay Serveru, se kterým pracujete. Přijměte tyto podmínky. BTCPay Server Vault nyní vyhledá hardware zařízení. Jakmile je zařízení nalezeno, BTCPay Server rozpozná, že Vault běží a načetl vaše zařízení.

**!Poznámka!**

Neposkytujte vaše SSH klíče nebo účet správce serveru nikomu jinému kromě správců, pokud používáte hot peněženku. Každý, kdo má přístup k těmto účtům, bude mít přístup k prostředkům v Hot Wallet.

### Shrnutí dovedností

V této sekci jste se naučili následující:

- Pohled na transakce Bitcoin peněženky a její různé kategorizace.
- Různé možnosti, které jsou k dispozici při odesílání z Bitcoin peněženky, od hardware po hot peněženky.
- Problém s gap limitem, který nastává při používání většiny peněženek, a jak tento problém napravit.
- Jak vygenerovat novou Bitcoin peněženku v BTCPay Serveru, včetně uložení klíčů v hardware peněžence a zálohování obnovovací fráze.

V tomto cíli jste se naučili, jak vygenerovat novou Bitcoin peněženku v BTCPay Serveru. Zatím jsme neprobrali, jak tyto klíče zabezpečit nebo používat. V rychlém přehledu tohoto cíle jste se naučili, jak nastavit první obchod. Naučili jste se, jak vygenerovat Bitcoin obnovovací frázi.

### Praktické hodnocení znalostí

Popište metodu pro generování klíčů a schéma pro jejich zabezpečení, spolu s kompromisy/riziky bezpečnostního schématu.

## BTCPay Server Lightning Wallet

<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>

Když správce serveru provádí novou instalaci BTCPay Serveru, může nastavit implementaci lightning network, LND, Core Lightning nebo Eclair; viz část Konfigurace BTCPay Serveru pro podrobnější instalační pokyny.
Pokud se toto provede ve třídě, připojení Lightning node k vašemu BTCPay Serveru probíhá prostřednictvím vlastního uzlu (Custom node). Uživatel, který není správcem serveru na BTCPay Serveru, nebude moci výchozím nastavením používat interní Lightning node. To slouží k ochraně majitele serveru před ztrátou jeho prostředků. Správci serverů mohou nainstalovat Plugin, který umožní přístup k jejich Lightning node prostřednictvím LNBank; to je mimo rozsah této knihy; více informací o LNBank najdete na oficiální stránce pluginu.

### Připojení interního uzlu (správce serveru)

Správce serveru může používat interní Lightning Node BTCPay Serveru. Bez ohledu na implementaci Lightningu je připojení k internímu Lightning node stejné.

Přejděte na předchozí nastavený obchod a klikněte v levém menu na "Lightning" peněženku. BTCPay Server nabízí dvě možnosti nastavení, použití interního uzlu (výchozí pouze pro správce serveru) nebo vlastního uzlu (externí připojení). Správci serverů mohou kliknout na možnost "Použít interní uzel". Další konfigurace není vyžadována. Klikněte na tlačítko "uložit" a všimněte si oznámení, které uvádí, "BTC Lightning node aktualizován". Obchod má nyní úspěšně získal schopnosti Lightning sítě.

### Připojení externího uzlu (uživatel/server vlastník obchodu)

Vlastníci obchodů nejsou výchozím nastavením oprávněni používat Lightning Node správce serveru. Je nutné se připojit k externímu uzlu, buď k uzlu vlastněnému majitelem obchodu před nastavením BTCPay Serveru, k pluginu LNBank, pokud jej správce serveru zpřístupní, nebo k řešení správce jako je Alby.

Přejděte na předchozí nastavený obchod a klikněte v levém menu pod peněženkami na "Lightning". Jelikož vlastníci obchodů nejsou výchozím nastavením oprávněni používat interní uzel, tato možnost je neaktivní. Použití vlastního uzlu je jedinou možností, která je výchozím nastavením dostupná pro majitele obchodů.

BTCPay Server vyžaduje informace o připojení; předem nastavený uzel (nebo řešení správce) poskytne tyto informace specifické pro implementaci Lightningu. V rámci BTCPay Serveru mohou majitelé obchodů používat následující připojení;

- C-lightning přes TCP nebo Unix domain socket connection.
- Lightning Charge přes HTTPS
- Eclair přes HTTPS
- LND přes REST proxy
- LNDhub přes REST API

![obrázek](assets/en/31.webp)

Klikněte na "testovat připojení", abyste se ujistili, že jste správně zadali údaje o připojení. Po potvrzení, že připojení je v pořádku, klikněte na uložit a BTCPay Server zobrazí, že obchod je aktualizován s Lightning Node.

### Správa interního Lightning node LND (Správce serveru)

Po připojení interního Lightning Node si správci serverů všimnou na Dashboardu nových dlaždic specificky pro informace o Lightningu.

- Lightning Balance
- BTC v kanálech
  - BTC otevírající kanály
  - BTC lokální zůstatek
  - BTC vzdálený zůstatek
  - BTC uzavírající kanály
- BTC On-chain
  - BTC potvrzené
  - BTC nepotvrzené
  - BTC rezervované
- Lightning Služby
  - Ride the Lightning (RTL).

Kliknutím buď na logo Ride the Lightning v dlaždici "Lightning služby" nebo na "Lightning" pod peněženkami v levém menu se správci serverů dostanou do RTL pro správu Lightning node.

**Poznámka!**

Pokud připojení interního Lightning Node selže - Pokud interní připojení selže, potvrďte:

1. Že Bitcoin on-chain uzel je plně synchronizován
2. Že interní lightning uzel je "Povolen" pod "Lightning" > "Nastavení" > "BTC Lightning Nastavení"
   Pokud se nemůžete připojit k vašemu Lightning uzlu, zkuste restartovat váš server nebo si pro více detailů přečtěte oficiální dokumentaci BTCPay Serveru; https://docs.btcpayserver.org/Troubleshooting/ . Nemůžete přijímat lightning platby ve vašem obchodě, dokud váš Lightning uzel nezobrazuje stav "Online". Zkuste otestovat vaše Lightning připojení kliknutím na odkaz "Public Node Info".

### Lightning peněženka

V možnosti Lightning peněženky v levém menu najdou správci serverů snadný přístup k RTL, jejich veřejné informace o uzlu a specifická nastavení Lightning pro jejich obchod na BTCPay Serveru.

#### Interní informace o uzlu

Správci serverů mohou kliknout na interní informace o uzlu a podívat se na stav svého serveru (Online/ Offline) a řetězec pro připojení pro Clearnet nebo Tor.

![obrázek](assets/en/32.webp)

#### Změna připojení

Pokud se majitel obchodu rozhodne použít změny v nastavení Lightning - Změna připojení.
Vedle informací o veřejném uzlu najdou majitelé obchodů tuto možnost. Vrátí je to k počátečnímu nastavení pro externí připojení lightning uzlu, vyplní nové informace o Lightning uzlu, kliknou na uložit a aktualizují obchod s novými informacemi o uzlu.

![obrázek](assets/en/33.webp)

#### Služby

Pokud se správce serveru rozhodne nainstalovat více služeb pro implementaci Lightning, budou zde uvedeny. S standardní implementací LND budou mít správci jako standardní nástroj pro správu uzlu Ride The Lightning (RTL).

#### Nastavení BTC Lightning peněženky

Po přidání Lightning uzlu do obchodu v předchozím kroku mohou majitelé obchodů v nastavení Lightning peněženky stále zvolit deaktivaci pro svůj obchod pomocí přepínače na vrcholu nastavení Lightning.

![obrázek](assets/en/34.webp)

#### Možnosti platby Lightning

Majitelé obchodů mohou nastavit parametry pro následující, aby vylepšili zážitek Lightning pro své zákazníky.

- Zobrazit částky plateb Lightning v Satoshis.
- Přidat hop hints pro soukromé kanály do Lightning faktury.
- Unifikovat on-chain a Lightning platby URL/QR kódy při placení.
- Nastavit šablonu popisu pro lightning faktury.

#### LNURL

Majitelé obchodů mohou zvolit, zda použít LNURL nebo ne. Lightning Network URL, nebo LNURL, je navrhovaný standard pro interakce mezi Lightning platícím a příjemcem. Stručně řečeno, LNURL je bech32 zakódovaná url s předponou lnurl. Očekává se, že Lightning peněženka dekóduje URL, kontaktuje URL a čeká na JSON objekt s dalšími instrukcemi, zejména s tagem definujícím chování lnurl.

- Povolit LNURL
- LNURL Classic Mode
  - Pro kompatibilitu peněženek, Bech32 zakódované (klasické) vs čistý text URL (nadcházející)
- Povolit příjemci předat komentář.

### Příklad 1

#### Připojení k Lightning s interním uzlem (Administrátor)

Tato možnost je k dispozici pouze pokud jste Administrátor této instance nebo pokud Administrátor změnil výchozí nastavení, kde uživatelé mohou používat interní lightning uzel.

Jako administrátor klikněte na Lightning Peněženku v levém menu. BTCPay Server požádá o použití jedné ze dvou možností pro připojení Lightning Uzlu, interní uzel nebo vlastní externí uzel. Klikněte na Použít interní uzel a klikněte na uložit.

#### Správa vašeho Lightning uzlu (RTL)

Po připojení k internímu lightning uzlu, BTCPay Server aktualizuje a zobrazí oznámení "BTC Lightning uzel aktualizován", potvrzující, že jste nyní připojili Lightning k vašemu obchodu.

Správa lightning uzlu je úkolem pro Administrátora serveru. To zahrnuje.

- Správa transakcí
- Správa likvidity
  - Příchozí likvidita
  - Odchozí likvidita
- Správa peerů a kanálů
  - Připojení peerů
  - Poplatky za kanál
  - Stav kanálu
- Pravidelné zálohování stavů kanálů.
- Kontrola zpráv o směrování.
- Alternativně použijte služby jako je Loop.

Správa všech lightning uzlů je standardně prováděna pomocí RTL (předpokládá se, že používáte implementaci LND). Administrátoři mohou kliknout na svou Lightning peněženku v BTCPay Serveru a najít tlačítko pro otevření RTL. Hlavní panel BTCPay Serveru je nyní aktualizován o dlaždice Lightning Network, včetně rychlého přístupu k RTL.

### Příklad 2

#### Připojení k lightning s Alby

Při připojení s úschovnou jako je Alby by měli majitelé obchodů nejprve vytvořit účet, navštívit: https://getalby.com/

![obrázek](assets/en/35.webp)

Po vytvoření účtu Alby jděte do svého obchodu BTCPay Server.

Krok 1: Klikněte na 'Nastavit Lightning uzel' na panelu nebo na 'Lightning' pod peněženkami.

![obrázek](assets/en/36.webp)

Krok 2: Vložte přihlašovací údaje vaší peněženky poskytnuté Alby. Na panelu Alby klikněte na Peněženka. Zde najdete "Přihlašovací údaje k peněžence". Zkopírujte tyto údaje. Vložte přihlašovací údaje od Alby do pole pro konfiguraci připojení v BTCPay Serveru.

![obrázek](assets/en/37.webp)

Krok 3: Po poskytnutí detailů připojení BTCPay Serveru klikněte na tlačítko "Testovat připojení", abyste ověřili, že připojení funguje správně. Všimněte si zprávy "Připojení k lightning uzlu úspěšné" na vrchu vaší obrazovky. To potvrzuje, že vše funguje jak má.

![obrázek](assets/en/38.webp)

Krok 4: Klikněte na uložit, a váš obchod je nyní připojen k lightning uzlu od Alby.

![obrázek](assets/en/39.webp)

**!Poznámka!**

Nikdy nedůvěřujte úschovné řešení Lightning pro více hodnot, než jste ochotni ztratit.

### Shrnutí dovedností

V této sekci jste se naučili:

- Jak připojit interní nebo externí Lightning uzel
- Obsah a funkce různých dlaždic souvisejících s Lightning na panelu
- Jak konfigurovat Lightning peněženku pomocí Voltage Surge nebo Alby

### Hodnocení znalostí Praktický přehled

Popište některé z různých možností pro připojení Lightning peněženky k vašemu obchodu.

# Rozhraní BTCPay Serveru

<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>

## Přehled panelu

<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>

BTCPay Server je modulární softwarový balíček. Existují však standardy, které každý BTCPay Server bude mít a s kterými bude administrátor/uživatelé interagovat. Začínáme panelem. Hlavní vstupní bod každého BTCPay Serveru po přihlášení. Panel poskytuje přehled o tom, jak váš obchod funguje, aktuální zůstatek peněženky a poslední transakce za posledních 7 dní. Jelikož je to modulární pohled, pluginy mohou využívat tento pohled pro svůj prospěch a vytvářet na panelu své dlaždice. V tomto učebním textu budeme mluvit pouze o standardních pluginech/aplikacích a jejich příslušných pohledech v rámci BTCPay Serveru.

### Dlaždice panelu

V hlavním pohledu na panel BTCPay Serveru jsou k dispozici několik standardních dlaždic. Tyto dlaždice jsou určeny majiteli obchodu nebo administrátorovi, aby rychle spravoval svůj obchod v jednom přehledu.

- Zůstatek peněženky
- Aktivita transakcí
- Zůstatek Lightning (pokud je Lightning povolen v obchodě)
- Služby Lightning (pokud je Lightning povolen v obchodě)
- Nedávné transakce.
- Nedávné faktury
- Aktuální aktivní crowdfundingové kampaně
- Výkon obchodu / nejprodávanější položky.
  Dlaždice Zůstatek peněženky poskytuje rychlý přehled o prostředcích a výkonnosti vaší peněženky. Lze ji zobrazit buď v BTC nebo ve fiat měně v týdenním, měsíčním nebo ročním grafu.
  ![image](assets/en/40.webp)

### Aktivita transakcí

Vedle dlaždice Zůstatek peněženky BTCPay Server zobrazuje rychlý přehled o čekajících výplatech, počtu transakcí za posledních 7 dní a zda váš obchod vydal nějaké refundace. Kliknutím na tlačítko Spravovat se dostanete do správy čekajících výplat (dozvíte se více o výplatách v kapitole BTCPay Server - Platby).

![image](assets/en/41.webp)

### Zůstatek Lightning

Toto je viditelné pouze, když je aktivován Lightning.

Když administrátor povolil přístup k síti Lightning, dashboard BTCPay Serveru nyní obsahuje novou dlaždici s informacemi o vašem Lightning uzlu. Kolik BTC je v kanálech, jak je toto vyvážené lokálně nebo vzdáleně (příchozí nebo odchozí likvidita), jestli se kanály zavírají nebo otevírají a kolik bitcoinů je drženo on-chain na lightning uzlu.

![image](assets/en/42.webp)

### Služby Lightning

Toto je viditelné pouze, když je lightning aktivní.

Vedle zobrazení vašeho zůstatku Lightning na dashboardu BTCPay Serveru uvidí administrátoři také dlaždici pro Služby Lightning. Zde administrátoři najdou rychlá tlačítka pro nástroje, které používají ke správě svého Lightning uzlu; například Ride the Lightning je jedním ze standardních nástrojů s BTCPay Serverem pro správu Lightning uzlu.

![image](assets/en/43.webp)

### Nedávné transakce

Dlaždice nedávných transakcí ukáže nejnovější transakce vašeho obchodu. Administrátor instance BTCPay Serveru může nyní jedním kliknutím vidět nejnovější transakci a zjistit, zda je potřeba k ní věnovat pozornost.

![image](assets/en/44.webp)

### Nedávné faktury

Dlaždice nedávných faktur ukazuje 6 nejnovějších faktur generovaných vaším BTCPay Serverem, včetně stavu a částky faktury. Dlaždice také obsahuje tlačítko "Zobrazit vše" pro snadný přístup k úplnému přehledu faktur.

![image](assets/en/45.webp)

### Bod prodeje a Crowdfundy

Jelikož BTCPay Server nabízí sadu standardních pluginů nebo aplikací, Bod prodeje a Crowdfund jsou dvě hlavní pluginy BTCPay Serveru. S každým obchodem a peněženkou může uživatel BTCPay Serveru generovat tolik Bodů prodeje nebo Crowdfundů, kolik uzná za vhodné. Každý z nich vytvoří novou dlaždici na dashboardu zobrazující výkon daných pluginů.

![image](assets/en/46.webp)

Všimněte si mírného rozdílu mezi dlaždicí Bodu prodeje a Crowdfundu. Administrátor vidí v dlaždici Bodu prodeje nejprodávanější položky. V dlaždici Crowdfundu se toto stává Nejlepšími výhodami. Obě dlaždice mají rychlá tlačítka pro správu příslušné aplikace a zobrazení nedávných faktur vytvořených nejlepšími položkami nebo výhodami.

![image](assets/en/47.webp)

**!?Poznámka!?**

Grafy zůstatků a nedávné transakce jsou k dispozici pouze pro on-chain platební metody. Informace o zůstatcích a transakcích v síti Lightning jsou na seznamu úkolů. Od verze BTCPay Serveru 1.6.0 jsou k dispozici základní informace o zůstatcích v síti Lightning.

### Shrnutí dovedností

V této sekci jste se naučili následující:

- Základní rozložení dlaždic na hlavní úvodní stránce je známé jako Dashboard.
- Základní pochopení obsahu každé dlaždice.

### Přezkoumání hodnocení znalostí

Z paměti vyjmenujte co nejvíce dlaždic z Dashboardu.

## BTCPay Server - Nastavení obchodu

<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>
V rámci softwaru BTCPay Server známe 2 typy nastavení. Specifická nastavení obchodu BTCPay Server, tlačítko nastavení, které najdete v levém menu pod Dashboardem, a nastavení BTCPay Server, která najdete na spodku menu hned nad účtem. Specifická nastavení serveru BTCPay Server mohou být zobrazena pouze administrátory serveru.
Nastavení obchodu obsahuje mnoho záložek pro kategorizaci jednotlivých sad nastavení.

- Obecné
- Kurzy
- Vzhled pokladny
- Přístupové tokeny
- Uživatelé
- Role
- Webhooks
- Procesory výplat
- E-maily
- Formuláře

### Obecné

V záložce Obecné nastavení majitelé obchodů nastavují svou značku a výchozí nastavení plateb. Při počátečním nastavení obchodu byl zadán název obchodu; toto bude odráženo v Obecných nastaveních pod Názvem obchodu. Zde může majitel obchodu také nastavit svůj web tak, aby odpovídal značce, a ID obchodu pro rozpoznání administrátorem v databázi.

#### Branding

Jelikož je BTCPay Server FOSS, majitel obchodu může provést vlastní branding, aby odpovídal jeho obchodu. Nastavte barvu značky, uložte loga vaší značky a přidejte vlastní CSS pro veřejné/stránky zákazníků (Faktury, Žádosti o platbu, Pull platby)

#### Platba

V nastavení plateb mají majitelé obchodů možnost nastavit výchozí měnu obchodu (buď v Bitcoinu nebo v jakékoli fiat měně).

#### Povolit komukoli vytvářet faktury

Toto nastavení je určeno pro vývojáře nebo tvůrce pracující na platformě BTCPay Server. S tímto nastavením zapnutým pro váš obchod umožňuje vnějšímu světu vytvářet faktury na vaší instanci BTCPay Server.

#### Přidat dodatečný poplatek (síťový poplatek) k fakturám

Funkce v rámci BTCPay chrání obchodníky před útoky prachu nebo klienty, kteří by později způsobili vysoké náklady na poplatky, když obchodník potřebuje najednou přesunout velké množství bitcoinů. Například zákazník vytvořil fakturu na 20$ a zaplatil ji částečně, platil 1$ 20krát, dokud nebyla faktura plně zaplacena. Obchodník má nyní větší transakci, což zvyšuje náklady na těžbu v případě, že se obchodník rozhodne později tyto prostředky přesunout. Ve výchozím nastavení BTCPay přidává k celkové částce faktury dodatečný síťový poplatek, aby pokryl tento výdaj pro obchodníka, když je faktura zaplacena v několika transakcích. BTCPay nabízí několik možností, jak přizpůsobit tuto ochrannou funkci. Můžete aplikovat síťový poplatek:

- Pouze pokud zákazník provede více než jednu platbu za fakturu (V příkladu výše, pokud zákazník vytvořil fakturu na 20\$ a zaplatil 1\$, celková částka k zaplacení je nyní 19\$ + síťový poplatek. Síťový poplatek je aplikován po první platbě)
- Na každou platbu (včetně první platby, v našem příkladu bude celková částka 20\$ + síťový poplatek hned, i při první platbě)
- Nikdy nepřidávat síťový poplatek (úplně vypne síťový poplatek)

I když chrání před transakcemi prachu, může to také negativně odrážet na podnikání, pokud není řádně komunikováno. Zákazníci mohou mít další otázky a myslet si, že je přeplácíte.

#### Faktura vyprší, pokud nebyla zaplacena celá částka po?

Časovač faktury je ve výchozím nastavení nastaven na 15 minut. Časovač je ochranným mechanismem proti volatilitě, protože uzamkne množství Bitcoinu podle kurzů Bitcoinu k fiat měnám. Pokud zákazník nezaplatí fakturu ve stanoveném období, faktura je považována za vypršenou. Faktura je považována za "zaplatěnou" hned, jakmile je transakce viditelná na blockchainu (0-potvrzení), ale považována za "dokončenou", když dosáhne počtu potvrzení, který obchodník definoval (obvykle 1-6). Časovač je přizpůsobitelný po minutách.

#### Považovat fakturu za zaplacenou i když zaplacená částka je o X% nižší než očekávaná?

Když zákazník použije peněženku na burze k přímé platbě za fakturu, burza si účtuje malý poplatek. To znamená, že taková faktura není považována za plně zaplacenou. Faktura dostává status "částečně zaplaceno". Zde můžete nastavit procentní sazbu, pokud obchodník chce přijímat nedoplatky na fakturách.

### Sazby

V BTCPay Serveru, když je faktura vygenerována, vždy potřebuje nejaktuálnější a přesnou cenu Bitcoinu vůči fiat měně. Při vytváření nového obchodu v BTCPay Serveru jsou administrátoři požádáni, aby nastavili svůj preferovaný zdroj ceny; po nastavení obchodu mohou majitelé obchodů kdykoli změnit svůj zdroj ceny v této záložce.

#### Pokročilé skriptování pravidel sazeb

Hlavně používáno pokročilými uživateli. Pokud je zapnuto, majitelé obchodů mohou vytvářet skripty týkající se chování cen a jak účtovat svým zákazníkům.

#### Testování

Rychlé testovací místo pro vaše preferované měnové páry. Zahrnuje také funkci pro kontrolu výchozích měnových párů prostřednictvím REST dotazu.

### Vzhled pokladny

Záložka vzhled pokladny začíná nastaveními specifickými pro fakturu a výchozí platební metodou a umožňuje specifické platební metody, když jsou splněny stanovené požadavky.

#### Nastavení faktury

Výchozí platební metody. BTCPay Server ve standardní konfiguraci má tři možnosti.

- BTC (on-chain)
- BTC (LNURL-pay)
- BTC (Off-chain & Lightning)

Můžeme nastavit parametry pro náš obchod, kde se zákazník setká s Lightningem pouze když je cena nižší než X částka a naopak pro On-chain transakce, když X je větší než Y vždy prezentovat možnost On-chain platby.

![image](assets/en/48.webp)

#### Pokladna

Od vydání BTCPay Serveru 1.7 bylo představeno nové rozhraní pokladny, nazývané Checkout V2. Od vydání 1.9 bylo standardizováno, administrátoři a majitelé obchodů mohou stále nastavit pokladnu na předchozí vydání. Použitím přepínače "Použít klasickou pokladnu" může majitel obchodu nastavit obchod zpět na předchozí zážitek z pokladny. BTCPay Server také má vybranou sadu přednastavení pro online obchodování nebo zážitek v obchodě.

![image](assets/en/49.webp)

Když zákazník interaguje s obchodem a generuje fakturu, je nastaven čas vypršení platnosti faktury. Ve výchozím nastavení BTCPay Server nastavuje toto na 5 minut, a administrátor může nastavit toto na jakoukoli hodnotu, kterou považuje za vhodnou. Stránku pokladny lze dále přizpůsobit kontrolou následujících parametrů:

- Oslavit platbu zobrazením konfet
- Zobrazit záhlaví obchodu (název a logo)
- Zobrazit tlačítko "Zaplatit v peněžence"
- Unifikovat URL/QR kódy pro on-chain a off-chain platby
- Zobrazit částky Lightning platby v Satoshi
- Automatická detekce jazyka na pokladně

![image](assets/en/50.webp)

Pokud není nastavena automatická detekce jazyka, BTCPay Server ve výchozím nastavení zobrazí angličtinu. Majitel obchodu může změnit toto výchozí nastavení na svůj preferovaný jazyk.

![image](assets/en/51.webp)

Kliknutím na rozevírací seznam mohou majitelé obchodů nastavit vlastní HTML titulek, který se zobrazí na stránce pokladny.

![image](assets/en/52.webp)

Aby zákazník věděl, kterou platební metodu používá, může majitel obchodu výslovně nastavit, že jeho pokladna vždy vyžaduje, aby uživatelé vybrali svou preferovanou platební metodu. Když je faktura zaplacena, BTCPay Server umožňuje zákazníkovi vrátit se na webovou stránku obchodu. Majitelé obchodů mohou nastavit toto přesměrování po zaplacení zákazníkem automaticky.

![image](assets/en/53.webp)

#### Veřejný účet

V nastaveních veřejného účtu může majitel obchodu nastavit stránky účtu jako veřejné a zobrazit seznam plateb na stránce účtu a QR kód účtu, aby zákazník mohl snadno získat přístup k němu digitálně.

### Přístupové tokeny

Přístupové tokeny se používají pro spárování s určitými integracemi e-commerce nebo vlastními integracemi.

### Uživatelé

Uživatelé obchodu jsou místo, kde majitel obchodu může spravovat své zaměstnance, jejich účty a přístup k obchodu. Po vytvoření účtů zaměstnanci může majitel obchodu přidat konkrétní uživatele do obchodu jako hosty nebo majitele. Pro další definici role zaměstnance se odkazujte na další sekci "Nastavení obchodu BTCPay Server - Role".

### Role

Majitel obchodu nemusí považovat standardní role uživatele za dostatečně významné. V nastavení vlastních rolí může majitel obchodu definovat přesné potřeby pro každou roli ve svém podnikání.

(1) Pro vytvoření nové role klikněte na tlačítko "+ Přidat roli".

(2) Zadejte název role, například "Pokladní".

(3) Nakonfigurujte jednotlivá oprávnění pro roli.

- Upravit vaše obchody.
- Spravovat směnárenské účty spojené s vašimi obchody.
  - Zobrazit směnárenské účty spojené s vašimi obchody.
- Spravovat vaše pull platby.
- Vytvořit pull platby.
  - Vytvořit nepotvrzené pull platby.
- Upravit faktury.
  - Zobrazit faktury.
  - Vytvořit fakturu.
  - Vytvořit faktury z lightning uzlů spojených s vašimi obchody.
- Zobrazit vaše obchody.
  - Zobrazit faktury.
  - Zobrazit vaše platební požadavky.
  - Upravit webové háčky obchodů.
- Upravit vaše platební požadavky.
  - Zobrazit vaše platební požadavky.
- Používat lightning uzly spojené s vašimi obchody.
  - Zobrazit lightning faktury spojené s vašimi obchody.
  - Vytvořit faktury z lightning uzlů spojených s vašimi obchody.
- Vložit prostředky na směnárenské účty spojené s vašimi obchody.
- Vybrat prostředky ze směnárenských účtů do vašeho obchodu.
- Obchodovat prostředky na směnárenských účtech vašeho obchodu.

Když je role vytvořena, její název je pevně stanoven a po přejití do režimu úprav nemůže být změněn.

### Webhooks

V BTCPay Serveru je poměrně snadné vytvořit nový "Webhook". V záložce Nastavení obchodu BTCPay Server - Webhooks může majitel obchodu snadno vytvořit nový webhook kliknutím na "+ Vytvořit Webhook". Webhooks umožňují BTCPay Serveru posílat HTTP události související s vaším obchodem na jiné servery nebo e-commerce integrace.

Nyní se nacházíte v zobrazení pro vytvoření Webhooku. Ujistěte se, že znáte vaši URL adresu Payload a vložte ji do vašeho BTCPay Serveru. Zatímco jste vložili URL adresu Payload, pod tím se zobrazuje tajemství webhooku. Zkopírujte tajemství webhooku a poskytněte jej na koncovém bodu. Když je vše nastaveno, můžete v BTCPay Serveru přepnout na Automatické opětovné doručení. Pokusíme se opětovně doručit jakékoli selhané doručení po 10 sekundách, 1 minutě a až 6krát po 10 minutách. Můžete přepínat mezi každou událostí nebo specifikovat události podle vašich potřeb. Nezapomeňte webhook povolit a kliknout na Přidat webhook pro uložení.

Webhooks nejsou určeny k tomu, aby byly kompatibilní s Bitpay API. V BTCPay Serveru existují dvě samostatné IPN (v termínech BitPay: "Okamžité platební oznámení").

- Webhook
- Oznámení

Použijte URL oznámení pouze tehdy, když vytváříte faktury prostřednictvím Bitpay API.

### Procesory výplat

Procesory výplat spolupracují s konceptem Výplaty v BTCPay Serveru. Agregátor výplat umožňuje seskupit více transakcí a odeslat je najednou. Díky procesorům výplat může majitel obchodu automatizovat hromadné výplaty. BTCPay Server nabízí dva způsoby automatizovaných výplat, On-chain a Off-chain (LN).
Majitel obchodu může kliknout a nakonfigurovat oba procesory výplat zvlášť. Majitel obchodu může chtít spustit on-chain procesor jednou každých X hodin, zatímco off-chain může jít každých několik minut. Pro On-chain můžete také nastavit cíl, do kterého bloku by měla být transakce zahrnuta. Ve výchozím nastavení je to nastaveno na 1 (nebo na další dostupný blok). Všimněte si, že nastavení procesoru Off-chain výplat má pouze časovač intervalu a žádný cílový blok. Platby přes Lightning network jsou okamžité.

![obrázek](assets/en/62.webp)
![obrázek](assets/en/63.webp)

Majitelé obchodů mohou nakonfigurovat on-chain procesor pouze pokud mají k obchodu připojenou Hot-wallet.

![obrázek](assets/en/64.webp)

Po nastavení procesoru výplat můžete jej rychle odstranit nebo upravit návratem na kartu Procesor výplat v nastaveních obchodu BTCPay Serveru.

**!?Poznámka!?**

Procesor výplat on-chain - Procesor výplat on-chain může fungovat pouze v obchodě nakonfigurovaném s připojenou Hot wallet. Pokud není hot wallet připojena, BTCPay Server nevlastní klíče k peněžence a nebude schopen automaticky zpracovávat výplaty.

### Emaily

BTCPay Server může používat emaily pro oznámení nebo, pokud jsou správně nastaveny, pro obnovu účtů, které byly na instanci vytvořeny, jelikož standardně BTCPay Server neposílá email při ztrátě hesla, například.

![obrázek](assets/en/65.webp)

Předtím, než majitel obchodu může nastavit pravidla emailů pro spuštění při konkrétních událostech jeho obchodu, musíme nastavit některá základní nastavení emailu. BTCPay Server potřebuje tato nastavení k odesílání emailů pro události založené na vašem obchodu nebo pro resetování hesla.

BTCPay Server usnadnil vyplnění těchto informací pomocí možnosti "Rychlé vyplnění":

- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid

Použitím možnosti rychlého vyplnění BTCPay Server předvyplní pole pro SMTP server a port; nyní majitel obchodu musí pouze vyplnit své údaje v Emailové adrese, Přihlášení (které je obvykle stejné jako vaše emailová adresa) a vaše heslo. Pokročilá možnost, kterou BTCPay Server nabízí v nastaveních emailu, je zakázat kontrolu bezpečnostních certifikátů TLS; ve výchozím nastavení je toto povoleno.

![obrázek](assets/en/66.webp)

S pravidly emailů může majitel obchodu nastavit konkrétní události, které spustí emaily na konkrétní emailové adresy.

- Faktura vytvořena
- Faktura obdržela platbu
- Faktura zpracovávána
- Faktura vypršela
- Faktura vyrovnána
- Faktura neplatná
- Platba faktury vyrovnána

Pokud zákazník poskytl emailovou adresu, tyto spouštěče mohou také poslat informace zákazníkovi. Majitelé obchodů mohou předvyplnit předmět emailu, aby bylo jasné, proč k tomuto emailu došlo a co spouštěč způsobil.

![obrázek](assets/en/67.webp)

### Formuláře

Jelikož BTCPay Server neshromažďuje žádná data, majitel obchodu by mohl chtít přidat vlastní formulář do svého nákupního procesu; tímto způsobem může majitel obchodu shromažďovat další informace od svého zákazníka. Stavitel formulářů BTCPay Serveru se skládá ze dvou částí, vizuální a pokročilejší kódový pohled na formuláře.
Při vytváření nového formuláře BTCPay Server otevře nové okno, které vyžaduje základní informace o tom, co chcete, aby váš nový formulář požadoval. Nejprve musí majitel obchodu dát svému novému formuláři jasný název, tento název NELZE změnit po jeho nastavení.
![image](assets/en/68.webp)

Po pojmenování formuláře majitelem obchodu můžete také přepnout přepínač "Povolit formulář pro veřejné použití" na ON, a ten se stane zeleným. To umožňuje použití formuláře na všech místech, která jsou viditelná zákazníkům. Například, pokud majitel obchodu vytvoří 1 samostatnou fakturu mimo svůj Bod prodeje, může stále chtít shromažďovat informace od zákazníka; přepnutí na ON umožňuje shromažďování těchto informací.

![image](assets/en/69.webp)

Každý formulář začíná alespoň 1 novým polem formuláře. Majitel obchodu si může vybrat, jaký typ pole by to mělo být;

- Text
- Číslo
- Heslo
- Email
- URL
- Telefonní čísla
- Datum
- Skrytá pole
- Skupina polí
- Textová oblast pro otevřené komentáře.
- Výběr možností

Každý typ přichází s jeho parametry k vyplnění. Majitel obchodu si je může nastavit podle svého přání. Pod prvním vytvořeným polem mohou majitelé obchodů přidávat další pole do tohoto jednoho formuláře.

![image](assets/en/70.webp)

#### Pokročilé vlastní formuláře

BTCPay Server také umožňuje vytvářet formuláře v kódu. Konkrétně v JSON. Místo pohledu na editor mohou majitelé obchodů kliknout na tlačítko KÓD vedle editoru a dostat se do kódu svých formulářů. V definici pole mohou být nastaveny pouze následující pole; hodnoty polí jsou uloženy v metadatech faktury:

| Pole                  | Popis                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| .fields.constant      | Pokud je true, .value musí být nastaveno v definici formuláře a uživatel nebude moci změnit hodnotu pole. (příklad: verze definice formuláře)                                                                                                                                                                                                                                                                                                                        |
| .fields.type          | Typ HTML vstupu text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel                                                                                                                                                                                                                                                                                                      |
| .fields.options       | Pokud je .fields.type select, seznam vybíratelných hodnot                                                                                                                                                                                                                                                                                                                                                                                                            |
| .fields.options.text  | Text zobrazený pro tuto možnost                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| .fields.options.value | Hodnota pole, pokud je tato možnost vybrána                                                                                                                                                                                                                                                                                                                                                                                                                          |
| .fields.type=fieldset | Vytvoří HTML skupinu polí kolem dětských .fields.fields (viz níže)                                                                                                                                                                                                                                                                                                                                                                                                   |
| .fields.name          | Název vlastnosti JSON pole, jak se objeví v metadatech faktury                                                                                                                                                                                                                                                                                                                                                                                                       |
| .fields.value         | Výchozí hodnota pole                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.required      | Pokud je true, pole bude vyžadováno                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.label         | Popisek pole                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| .fields.helpText      | Doplňující text poskytující vysvětlení k poli.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| .fields.fields        | Můžete organizovat vaše pole do hierarchie, což umožňuje vnoření dílčích polí do metadat faktury. Tato struktura vám může pomoci lépe organizovat a spravovat shromážděné informace, čímž je jejich přístup a interpretace jednodušší. Například, pokud máte formulář, který sbírá informace o zákaznících, můžete skupinu polí seskupit pod nadřazené pole nazvané zákazník. V rámci tohoto nadřazeného pole byste mohli mít dílčí pole jako jméno, Email a adresa. |

Název pole reprezentuje název vlastnosti JSON, který ukládá hodnotu poskytnutou uživatelem do metadat faktury. Některé známé názvy mohou být interpretovány a upravit nastavení faktury.

| Název pole       | Popis          |
| ---------------- | -------------- |
| invoice_amount   | Částka faktury |
| invoice_currency | Měna faktury   |

Pole faktury můžete automaticky předvyplnit přidáním řetězců dotazů do URL formuláře, jako je "?your_field=hodnota".

Zde jsou některé případové použití této funkce:

- Pomoc s vstupem uživatele: Předvyplněte pole známými informacemi o zákazníkovi, aby bylo pro ně snazší formulář dokončit. Například, pokud již znáte emailovou adresu zákazníka, můžete předvyplnit pole emailu, aby ušetřili čas.
- Personalizace: Přizpůsobte formulář na základě preferencí zákazníka nebo segmentace. Například, pokud máte různé úrovně zákazníků, můžete formulář předvyplnit relevantními daty, jako je jejich úroveň členství nebo konkrétní nabídky.
- Sledování: Sledujte zdroj návštěv zákazníků pomocí skrytých polí a předvyplněných hodnot. Například, můžete vytvořit odkazy s předvyplněnými hodnotami utm_media pro každý marketingový kanál (např. Twitter, Facebook, Email). To vám pomůže analyzovat účinnost vašich marketingových snah.
- A/B testování: Předvyplňte pole různými hodnotami pro testování různých verzí formuláře, což vám umožní optimalizovat uživatelskou zkušenost a míru konverze.

### Shrnutí dovedností

V této sekci jste se dozvěděli následující:

- Rozložení a funkce záložek v Nastavení obchodu
- Široké možnosti pro jemné ladění zpracování podkladových směnných kurzů, částečných plateb, mírných nedoplatků a dalšího.
- Přizpůsobení vzhledu pokladny, včetně závislosti hlavního řetězce oproti povolení Lightning na faktuře.
- Správa úrovní přístupu do obchodu a oprávnění napříč rolími.
- Konfigurace automatizovaných emailů a jejich spouštěčů
- Vytvoření vlastních formulářů pro shromažďování dalších informací o zákaznících při pokladně.

### Hodnocení znalostí

#### KA Review

Jaký je rozdíl mezi Nastavením obchodu a Nastavením serveru?

#### KA Hypothetický

Popište některé možnosti, které byste mohli vybrat v Vzhled pokladny > Nastavení faktury, a proč.

## BTCPay Server - Nastavení serveru

<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>

BTCPay Server se skládá ze dvou různých pohledů na nastavení. Jeden je věnován Nastavení obchodu a druhý Nastavení serveru. Posledně jmenovaný je dostupný pouze pokud jste administrátorem serveru a není pro majitele obchodů. Administrátoři serveru mohou přidávat uživatele, vytvářet vlastní role, konfigurovat emailový server, nastavovat politiky, provádět údržbové úkoly, kontrolovat všechny služby připojené k BTCPay Serveru, nahrávat soubory na server nebo kontrolovat Logy.

### Uživatelé

Jak bylo zmíněno v předchozí části, Administrátoři serveru mohou zvát uživatele na svůj server přidáním do záložky Uživatelé.

### Serverově specifické vlastní Role

BTCPay Server rozlišuje dva druhy vlastních rolí, specifické pro obchod a serverově specifické vlastní role v nastavení BTCPay Serveru. Obě mají podobnou sadu oprávnění; nicméně, pokud jsou nastaveny prostřednictvím záložky Nastavení BTCPay Serveru - Role, aplikovaná role bude platit serverově a vztahuje se na více obchodů. Všimněte si značky "Serverově specifické" u vlastních rolí v nastavení serveru.
![image](assets/en/71.webp)

### Serverově široké vlastní role

Sada oprávnění pro serverově široké vlastní role:

- Upravit vaše obchody.
- Spravovat směnárenské účty propojené s vašimi obchody.
  - Zobrazit směnárenské účty propojené s vašimi obchody.
- Spravovat vaše výběrové platby.
  - Vytvořit výběrové platby.
  - Vytvořit neověřené výběrové platby.
- Upravit faktury.
  - Zobrazit faktury.
  - Vytvořit fakturu.
  - Vytvořit faktury z lightning uzlů spojených s vašimi obchody.
- Zobrazit vaše obchody.
  - Zobrazit faktury.
  - Zobrazit vaše platební požadavky.
  - Upravit webové háčky obchodů.
- Upravit vaše platební požadavky.
  - Zobrazit vaše platební požadavky.
- Používat lightning uzly spojené s vašimi obchody.
  - Zobrazit lightning faktury spojené s vašimi obchody.
  - Vytvořit faktury z lightning uzlů spojených s vašimi obchody.
- Vložit prostředky na směnárenské účty propojené s vašimi obchody.
- Vybrat prostředky ze směnárenských účtů do vašeho obchodu.
- Obchodovat prostředky na směnárenských účtech vašeho obchodu.

**!?Poznámka!?**

Když je role vytvořena, její název je pevně stanoven a po editaci nemůže být změněn.

### Email

Nastavení emailu pro celý server vypadá podobně jako nastavení emailu specifické pro obchod. Toto nastavení ovšem zahrnuje nejen spouštěče pro obchody nebo logy administrátora. Toto nastavení emailu také umožňuje obnovu hesla na BTCPay Serveru při přihlášení. Funguje podobně jako nastavení specifické pro obchod; administrátoři mohou rychle vyplnit své emailové parametry, zadat své emailové přihlašovací údaje a server nyní může posílat emaily.

![image](assets/en/72.webp)

### Politiky

Administrátoři politik BTCPay Serveru mohou nastavit některá nastavení na témata jako Nastavení stávajících uživatelů, Nastavení nových uživatelů, Nastavení oznámení a Nastavení údržby. Tato jsou určena pro registraci nových uživatelů jako admin nebo normální uživatelé nebo dokonce skrytí BTCPay Serveru před vyhledávači přidáním do hlavičky vašeho serveru.

![image](assets/en/73.webp)

#### Nastavení stávajících uživatelů

Možnosti dostupné zde jsou oddělené od vlastních rolí. Tyto extra oprávnění mohou obchod nebo majitele obchodu vystavit útokům. Politiky, které mohou být přidány stávajícím uživatelům:

- Povolit ne-adminům používat interní Lightning uzel v jejich obchodech.
  - To by umožnilo majitelům obchodů používat Lightning uzel serverového administrátora a tedy jeho prostředky! Pozor, toto není řešení pro poskytnutí přístupu k Lightning.
- Povolit ne-adminům vytvářet hot peněženky pro jejich obchody.
  - To by umožnilo komukoli s účtem na vaší instanci BTCPay Serveru vytvářet hot peněženky a ukládat jejich obnovovací seed na serveru administrátora. To by mohlo administrátora zatížit odpovědností za držení prostředků třetích stran!
- Povolit ne-adminům importovat hot peněženky pro jejich obchody.
  - Podobně jako předchozí téma vytváření hot peněženek, tato politika umožňuje import hot peněženky, s těmi samými nebezpečími zmíněnými v sekci vytváření hot peněženek.

![image](assets/en/74.webp)

#### Nastavení nových uživatelů

Můžeme nastavit některá důležitá nastavení pro správu nových uživatelů přicházejících na server. Můžeme nastavit potvrzovací email pro nové registrace, zakázat vytváření nových uživatelů přes přihlašovací obrazovku a omezit přístup ne-adminů k vytváření uživatelů přes API.

- Vyžadovat potvrzovací email pro registraci.
  - Administrátor serveru musí mít nastavený Email server!
- Zakázat registraci nových uživatelů na serveru
- Zakázat ne-adminům přístup k API endpointu pro vytváření uživatelů.

Ve výchozím nastavení má BTCPay Server zapnuté Zakázání registrace nových uživatelů a vypnutý přístup ne-adminů k API endpointu pro vytváření uživatelů. To je z bezpečnostního hlediska, kde žádná náhodná osoba, která by mohla najít BTCPay přihlášení vašeho serveru, nemůže začít vytvářet účty.

![image](assets/en/75.webp)

#### Nastavení upozornění

![image](assets/en/76.webp)

#### Nastavení údržby

BTCPay Server je Open Source projekt, který je hostován na GitHubu. Kdykoliv BTCPay Server vydá novou verzi softwaru, administrátoři mohou být upozorněni, že je dostupná nová verze. Administrátoři také mohou chtít zabránit vyhledávačům (google, yahoo, duckduckgo) v indexaci domény BTCPay Serveru. Jelikož je BTCPay Server FOSS, vývojáři z celého světa mohou chtít vytvářet nové funkce; BTCPay Server má experimentální funkci, která když je aktivována, umožní administrátorovi používat funkce ještě nevhodné pro produkční použití, čistě pro účely testování.

- Kontrolovat vydání na GitHubu a upozornit, když je dostupná nová verze BTCPay Serveru.
- Zabránit vyhledávačům v indexaci tohoto webu
- Povolit experimentální funkce.

![image](assets/en/77.webp)

#### Pluginy

BTCPay Server může přidávat pluginy a rozšiřovat tak svou sadu funkcí. Pluginy jsou ve výchozím nastavení načítány z repozitáře plugin-builder BTCPay Serveru. Administrátor však může zvolit zobrazení pluginů ve stavu před vydáním a pokud to vývojář pluginu dovolí, může nyní administrátor serveru instalovat beta verze pluginů.

![image](assets/en/78.webp)

##### Nastavení přizpůsobení

Standardní nasazení BTCPay Serveru bude přístupné prostřednictvím domény nastavené při instalaci. Administrátor serveru však může přemapovat kořenovou doménu a zobrazit jednu z vytvořených aplikací z konkrétního obchodu. Administrátor serveru může také mapovat konkrétní domény na konkrétní aplikace.

- Zobrazit aplikaci na kořenové adrese webu
  - Zobrazí seznam možných aplikací, které se mají zobrazit na kořenové doméně.

![image](assets/en/79.webp)

- Přiřadit konkrétní domény k určitým aplikacím.
  - Když kliknete na nastavení konkrétní domény pro určité aplikace, může Administrátor nastavit tolik domén ukazujících na určité aplikace, kolik je potřeba.

![image](assets/en/80.webp)

#### Prohlížeče bloků

BTCPay Server standardně používá mempool.space jako svůj prohlížeč bloků pro transakce. Když BTCPay Server vygeneruje novou fakturu a je k ní přiřazena transakce, majitel obchodu může kliknout a otevřít transakci; BTCPay Server standardně ukazuje na mempool.space jako na prohlížeč bloků; administrátor serveru může toto změnit podle svého předvolení.

![image](assets/en/81.webp)

### Služby

Nastavení BTCPay Serveru: Záložka Služby je přehledem komponent, které váš BTCPay Server používá. Služby, které váš BTCPay Server nabízí, se mohou lišit v závislosti na způsobu nasazení.

Administrátor BTCPay Serveru může kliknout na "Zobrazit informace" u každé služby, otevřít ji a nastavit specifická nastavení.

![image](assets/en/82.webp)

#### LND (gRPC)

BTCPay zpřístupňuje službu LND gRPC pro vnější použití; informace pro připojení najdete v tomto konkrétním nastavení; zde jsou uvedeny kompatibilní peněženky. BTCPay Server také poskytuje QR kód pro připojení, který lze naskenovat a použít v mobilní peněžence.

Administrátoři serveru mohou otevřít více detailů, aby viděli;

- Detaily hostitele
- Použití SSL
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- GRPC SSL Cipher suite (GRPC_SSL_CIPHER_SUITES)

#### LND (REST)

BTCPay zpřístupňuje službu LND REST pro vnější použití; informace pro připojení najdete zde; zde jsou uvedeny kompatibilní peněženky. Mezi kompatibilní peněženky patří Joule, Alby a ZeusLN. BTCPay Server poskytuje QR kód pro připojení, stačí naskenovat a použít v kompatibilní peněžence.

- REST Uri
- Macaroon
- AdminMacaroon - InvoiceMacaroon
- ReadonlyMacaroon

#### Záloha LND Seed

Záloha LND Seed je užitečná pro obnovu prostředků z vaší LND peněženky v případě poškození vašeho serveru. Jelikož je Lightning node Hot-wallet, můžete najít důvěrné informace o seedu na této stránce.

LND dokumentuje proces obnovy. Viz https://github.com/lightningnetwork/lnd/blob/master/docs/recovery.md pro dokumentaci.

#### Ride The Lightning

Ride the Lightning je nástroj pro správu Lightning node, který je vyvinut jako Open Source software. BTCPay Server používá RTL jako komponentu pro správu Lightning node ve svém stacku. Administrátoři BTCPay Serveru mohou přistupovat k RTL prostřednictvím nastavení serveru - záložka Služby nebo kliknutím na Lightning peněženku.

#### Full node P2P

Administrátoři serveru mohou chtít připojit svůj Bitcoin node k mobilní peněžence. Tato stránka poskytuje informace pro vzdálené připojení k vašemu full node prostřednictvím protokolu P2P. V době psaní této knihy BTCPay Server uvádí Blockstream Green a Wasabi peněženku jako kompatibilní peněženky. BTCPay Server poskytuje QR kód pro připojení, naskenujte a použijte v kompatibilní peněžence.

#### Full node RPC

Tato stránka poskytuje informace pro vzdálené připojení k vašemu full node prostřednictvím protokolu RPC.

#### SSH

SSH se používá pro účely údržby. BTCPay Server zobrazuje počáteční příkaz pro připojení k vašemu serveru a veřejné klíče SSH oprávněné k připojení k vašemu serveru. Administrátoři serveru by mohli chtít vypnout změny SSH prostřednictvím uživatelského rozhraní BTCPay Serveru.

#### Dynamické DNS

Dynamické DNS umožňuje mít stabilní DNS jméno směřující na váš server, i když se vaše IP adresa pravidelně mění. Doporučuje se, pokud hostujete BTCPay Server doma a přejete si mít clearnet doménu pro přístup k vašemu serveru.

Všimněte si, že je potřeba správně nakonfigurovat vaše NAT a instalaci BTCPay Serveru, abyste získali HTTPS certifikát.

### Téma

BTCPay Server standardně nabízí dva motivy: Světlý a Tmavý režim. Mezi nimi můžete přepínat kliknutím na Účet v levém dolním rohu a přepínáním mezi Tmavým tématem nebo Světlým tématem. Administrátoři BTCPay Serveru mohou přidat své vlastní téma poskytnutím vlastního CSS tématu.

Administrátoři mohou rozšířit Světlý/Tmavý motiv přidáním vlastního CSS nebo nastavením svého vlastního tématu jako úplně vlastního.

![obrázek](assets/en/83.webp)

#### Branding serveru

Administrátoři serveru mohou změnit branding BTCPay Serveru nastavením branding serveru vaší společnosti. Jelikož je BTCPay Server FOSS, administrátoři serveru mohou software označit vlastní značkou a změnit vzhled tak, aby vyhovoval jejich podnikání.

![obrázek](assets/en/84.webp)

### Údržba

Jako administrátor serveru se od vás očekává, že se o server dobře postaráte. V záložce Údržba BTCPay Serveru může admin provádět některé základní údržbové práce. Nastavit název domény pro instanci BTCPay Serveru, restartovat nebo vyčistit server. Možná nejdůležitější je provádění aktualizací.

BTCPay Server je Open Source projekt a často se aktualizuje. Každé nové vydání je oznámeno buď vašimi notifikacemi BTCPay Serveru nebo na oficiálních kanálech, kterými BTCPay Server komunikuje.

![obrázek](assets/en/85.webp)

#### Název domény

Po nastavení BTCPay Serveru může administrátor chtít změnit původní doménu. V záložce Údržba může administrátor změnit doménu. Po kliknutí na potvrzení a nastavení správných DNS záznamů na doméně se BTCPay Server aktualizuje a restartuje, aby se vrátil na novou doménu.

![obrázek](assets/en/86.webp)

#### Restart

Restartujte BTCPay Server a související služby.

![obrázek](assets/en/87.webp)

#### Čištění

BTCPay Server běží s komponentami Dockeru; s aktualizacemi mohou zůstat zbytky Docker obrazů, dočasných souborů atd. Správci serverů mohou tyto zbytky vyčistit a uvolnit místo ve svém prostředí spuštěním skriptu pro čištění.
![image](assets/en/88.webp)

#### Aktualizace

Možná nejdůležitější možnost v záložce Údržba. BTCPay Server je vytvořen komunitou, a proto jsou jeho aktualizační cykly častější než u většiny softwarových produktů. Když má BTCPay Server novou verzi, správci budou o tom informováni ve svém centru oznámení. Kliknutím na tlačítko aktualizace BTCPay Server zkontroluje GitHub pro nejnovější verzi, aktualizuje Server a restartuje ho. Před aktualizací se správcům serverů vždy doporučuje číst poznámky k vydání distribuované prostřednictvím oficiálních kanálů BTCPay Serveru.

![image](assets/en/89.webp)

### Logy

Čelit problému nikdy není zábava. Tento dokument vysvětluje nejčastější postup a kroky pro efektivní identifikaci vašeho problému a jeho vyřešení sami nebo s pomocí komunity.

Identifikace problému je klíčová.

#### Replikace problému

Především se pokuste určit, kdy k problému dochází. Pokuste se problém replikovat. Zkuste aktualizovat a restartovat váš Server, abyste ověřili, že můžete svůj problém reprodukovat. Pokud to lépe popisuje váš problém, pořiďte snímek obrazovky.

##### Aktualizace serveru

Zkontrolujte vaši verzi BTCPay Serveru, jestli není mnohem starší než [nejnovější verze](https://github.com/btcpayserver/btcpayserver/releases) BTCPay Serveru. Aktualizace vašeho Serveru může problém vyřešit.

##### Restartování serveru

Restartování vašeho Serveru je jednoduchý způsob, jak vyřešit mnoho nejčastějších problémů BTCPay Serveru. Možná budete potřebovat SSH připojení k vašemu Serveru, abyste ho mohli restartovat.

##### Restartování služby

Pro některé problémy může být potřeba restartovat pouze určitou službu ve vaší nasazení BTCPay Serveru. Například restartování kontejneru lets encrypt pro obnovení SSL certifikátu.

```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```

Použijte docker ps pro nalezení názvu jiné služby, kterou byste chtěli restartovat.

#### Prohlížení logů

Logy mohou poskytnout zásadní kus informací. V následujících odstavcích popíšeme, jak získat informace z logů pro různé části BTCPay.

##### Logy BTCPay

Od verze v1.0.3.8 můžete snadno přistupovat k logům BTCPay Serveru z front endu. Pokud jste správcem serveru, přejděte do Nastavení serveru > Logy a otevřete soubor s logy. Pokud nevíte, co znamená konkrétní chyba v logu, zmíňte to při řešení problémů.

Pokud chcete podrobnější logy a používáte nasazení Dockeru, můžete zobrazit logy konkrétních Docker kontejnerů pomocí příkazové řádky. Viz tyto [instrukce pro ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) do instance BTCPay běžící na VPS.

Na další stránce je obecný seznam názvů kontejnerů používaných pro BTCPay Server.

Spusťte níže uvedené příkazy pro vypsání logů podle názvu kontejneru. Nahraďte název kontejneru pro zobrazení logů jiných kontejnerů.

```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```

| Logy pro     | Název kontejneru                  |
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

Existuje několik způsobů, jak přistupovat k vašim LND logům při použití Dockeru. Nejprve se přihlaste jako root:

```bash
sudo su -
Přejděte do správného adresáře:
cd btcpayserver-docker
# Najděte název kontejneru:
docker ps
Vytiskněte logy podle názvu kontejneru:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```

Alternativně můžete rychle vytisknout logy použitím ID kontejneru (stačí pouze první jedinečné znaky ID, jako jsou dvě nejlevější znaky):

```bash
docker logs 'vložte vaše ID kontejneru'
```

Pokud z nějakého důvodu potřebujete více logů

```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/_data/logs/bitcoin/mainnet/
ls
```

Uvidíte něco jako

```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```

Pro přístup k nerozbaleným logům těchto logů použijte `cat lnd.log` nebo pokud chcete jiný, použijte `cat lnd.log.15`.

Pro přístup k komprimovaným logům ve formátu `.gzip` použijte `gzip -d lnd.log.16.gz` (v tomto případě přistupujeme k `lnd.log.16.gz`). To by vám mělo dát nový soubor, kde můžete použít `cat lnd.log.16`. V případě, že výše uvedené nefunguje, možná budete muset nejprve nainstalovat gzip pomocí `sudo apt-get install gzip`.

###### Lightning Network c-lightning - Docker

```bash
sudo su -
docker ps
# Najděte ID kontejneru c-lightning.
docker logs 'vložte zde vaše ID kontejneru'
```

alternativně použijte toto

```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```

Informace o logu můžete také získat pomocí příkazu c-lightning cli.

```bash
bitcoin-lightning-cli.sh getlog
```

#### Logy Bitcoin Node

Kromě [prohlížení logů](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) vašeho kontejneru Bitcoind můžete také použít kterýkoliv z [příkazů bitcoin-cli](https://developer.bitcoin.org/reference/rpc/index.html)

[(otevře nové okno)](https://developer.bitcoin.org/reference/rpc/index.html) pro získání informací z vašeho bitcoinového uzlu. BTCPay zahrnuje skript, který vám umožní snadno komunikovat s vaším Bitcoinovým uzlem.

Uvnitř složky btcpayserver-docker získejte informace o blockchainu pomocí vašeho uzlu:

```bash
bitcoin-cli.sh getblockchaininfo
```

BTCPay Server má lokální souborový systém a umožňuje nahrávat majetek obchodu (produkty), loga a branding přímo na server. Souborový systém serveru je přístupný pouze správcům serveru; majitelé obchodů mohou nahrávat svá loga/branding na úrovni obchodu.
Když je správce serveru na záložce Úložiště souborů, je možné přímo nahrávat na váš server nebo změnit poskytovatele úložiště souborů na Lokální souborový systém nebo Azure Blob Storage.

![obrázek](assets/en/90.webp)

![obrázek](assets/en/91.webp)

### Shrnutí dovedností

V této sekci jste se naučili následující:

- Rozdíl mezi nastavením Obchodu a Serveru, zejména pokud jde o Uživatele, Role a Emaily
- Nastavit politiky pro celý server pro používání a vytváření Lightning nebo Bitcoin hot wallet, registraci nových uživatelů a emailové notifikace.
- Jak přidat vlastní témata (namísto jednoduchých možností světlé/tmavé) stejně jako vytvořit vlastní loga
- Provádět jednoduché údržbové úkoly serveru prostřednictvím poskytnutého GUI
- Řešení problémů, včetně získání podrobností pro kterýkoliv z Docker kontejnerů nebo vašeho uzlu
- Správa úložiště souborů

### Hodnocení znalostí

#### KA Konceptuální přezkum

Jaký je rozdíl v rolích přiřazených prostřednictvím nastavení Serveru oproti nastavení Obchodu a popište potenciální využití jednoho oproti druhému?

#### KA Praktický přezkum

Popište některé možné případy použití povolené na záložce Politiky.

#### KA Praktický přezkum

Popište některé akce, které by správce mohl pravidelně provádět na záložce Údržba.

## BTCPay Server - Platby

<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>

Faktura je dokument, který prodávající vystavuje kupujícímu za účelem vybrání platby.

V BTCPay Serveru faktura představuje dokument, který musí být zaplacen v určeném časovém intervalu za pevný směnný kurz. Faktury mají expiraci, protože uzamknou směnný kurz v určeném časovém rámci, aby chránily příjemce před cenovými kolísáními.

Jádrem BTCPay Serveru je schopnost fungovat jako systém pro správu faktur Bitcoinu. Faktura je zásadní nástroj pro sledování a správu přijaté platby.

Pokud nepoužíváte vestavěnou [Peněženku](https://docs.btcpayserver.org/Wallet/) pro ruční příjem plateb, všechny platby v obchodě budou zobrazeny na stránce Faktury. Tato stránka kumulativně řadí platby podle data a je klíčovým prvkem pro správu faktur a řešení problémů s platbami.

![obrázek](assets/en/92.webp)

### Obecné

#### Stavy faktur

V následující tabulce jsou uvedeny a popsány standardní stavy faktur v BTCPay a doporučené akce. Akce jsou pouze doporučení. Je na uživatelích, aby definovali nejlepší postup pro svůj případ použití a podnikání.

| Stav faktury                       | Popis                                                                                                                | Akce                                                                                                                                                        |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nová                               | Nezaplaceno, časovač faktury ještě nevypršel                                                                         | Žádná                                                                                                                                                       |
| Nová (částečně zaplaceno)          | Zaplaceno, ne v plné výši, časovač faktury ještě nevypršel                                                           | Žádná                                                                                                                                                       |
| Vypršela                           | Nezaplaceno, časovač faktury vypršel                                                                                 | Žádná                                                                                                                                                       |
| Vypršela (částečně zaplaceno) \*\* | Zaplaceno, ne v plné částce, a vypršelo                                                                              | Kontaktujte kupujícího, aby se domluvili na vrácení peněz nebo požádejte o doplacení dlužné částky. Volitelně označte fakturu jako vyrovnánu nebo neplatnou |
| Vypršela (zaplaceno pozdě)         | Zaplaceno, v plné výši, po vypršení časovače faktury                                                                 | Kontaktujte kupujícího, aby se domluvili na vrácení peněz nebo zpracujte objednávku, pokud jsou pozdní potvrzení přijatelná.                                |
| Vyrovnané (zaplaceno navíc)        | Zaplaceno více než částka faktury, vyrovnáno, přijat dostatečný počet potvrzení                                      | Kontaktujte kupujícího, abyste domluvili vrácení přeplatku, nebo volitelně počkejte, až vás kupující kontaktuje                                             |
| Zpracovává se                      | Zaplaceno v plné výši, ale nebyl přijat dostatečný počet potvrzení specifikovaných v nastavení obchodu               | Kontaktujte kupujícího, abyste domluvili vrácení přeplatku, nebo volitelně počkejte, až vás kupující kontaktuje                                             |
| Zpracovává se (zaplaceno navíc)    | Zaplaceno více než částka faktury, nedostatečný počet potvrzení                                                      | Počkejte na vyrovnání, poté kontaktujte kupujícího, abyste domluvili vrácení přeplatku, nebo volitelně počkejte, až vás kupující kontaktuje                 |
| Vyrovnané                          | Zaplaceno, v plné výši, přijat dostatečný počet potvrzení v obchodě                                                  | Vyřiďte objednávku                                                                                                                                          |
| Vyrovnané (označeno)               | Stav byl ručně změněn na vyrovnané ze stavu zpracovává se nebo neplatné                                              | Správce obchodu označil platbu jako vyrovnanou                                                                                                              |
| Neplatné\*                         | Zaplaceno, ale nepřijat dostatečný počet potvrzení v čase specifikovaném v nastavení obchodu                         | Zkontrolujte transakci na blockchain exploreru, pokud přijala dostatečný počet potvrzení, označte jako vyrovnané                                            |
| Neplatné (označeno)                | Stav byl ručně změněn na neplatné ze stavu vyrovnané nebo vypršelé                                                   | Správce obchodu označil platbu jako neplatnou                                                                                                               |
| Neplatné (zaplaceno navíc)         | Zaplaceno více než částka faktury, ale nepřijat dostatečný počet potvrzení v čase specifikovaném v nastavení obchodu | Zkontrolujte transakci na blockchain exploreru, pokud přijala dostatečný počet potvrzení, označte jako vyrovnané                                            |

#### Detaily faktury

Stránka s detaily faktury obsahuje veškeré informace související s fakturou.

Informace o faktuře jsou automaticky vytvořeny na základě stavu faktury, směnného kurzu atd. Informace o produktu jsou automaticky vytvořeny, pokud byla faktura vytvořena s informacemi o produktu, například v aplikaci Point of Sale.

#### Filtrace faktur

Faktury lze filtrovat pomocí rychlých filtrů umístěných vedle tlačítka hledání nebo pokročilých filtrů, které lze aktivovat kliknutím na odkaz (Pomoc) nahoře. Uživatelé mohou filtrovat faktury podle obchodu, ID objednávky, ID položky, stavu nebo data.

#### Export faktur

Faktury BTCPay Server lze exportovat ve formátech CSV nebo JSON. Pro více informací o exportu faktur a účetnictví.

#### Vrácení peněz za fakturu

Pokud byste z jakéhokoli důvodu chtěli provést vrácení peněz, můžete snadno vytvořit vrácení peněz z pohledu faktury.

#### Archivace faktur

V důsledku funkce nepoužívání stejné adresy BTCPay Serveru je běžné vidět na stránce faktur obchodu mnoho vypršelých faktur. Aby se tyto faktury nezobrazovaly ve vašem přehledu, vyberte je v seznamu a označte je jako archivované. Faktury, které byly označeny jako archivované, nejsou smazány. Platba na archivovanou fakturu bude stále detekována vaším BTCPay Serverem (stav zaplaceno pozdě). Archivované faktury obchodu si můžete kdykoli prohlédnout výběrem archivovaných faktur z rozevíracího seznamu filtru vyhledávání.

#### Výchozí měna

Výchozí měna obchodu, která byla nastavena při vytváření obchodu

#### Povolit komukoli vytvořit fakturu

Tuto možnost byste měli povolit, pokud chcete umožnit vnějšímu světu vytvářet faktury ve vašem obchodě. Tato možnost je užitečná pouze pokud používáte tlačítko platby nebo pokud vystavujete faktury prostřednictvím API nebo webových stránek třetích stran. Aplikace PoS je předem autorizována a pro náhodného návštěvníka, který otevře váš obchod PoS a vytvoří fakturu, není tato možnost nutná.

#### Přidat dodatečný poplatek (poplatek za síť) k faktuře

- Pouze pokud zákazník provede více než jednu platbu za fakturu
- Při každé platbě
- Nikdy nepřidávat poplatek za síť

#### Faktura vyprší, pokud celá částka nebyla zaplacena po .. minutách.

Časovač faktury je standardně nastaven na 15 minut. Časovač je ochranným mechanismem proti volatilitě, protože uzamkne množství kryptoměny podle aktuálního směnného kurzu krypto na fiat. Pokud zákazník nezaplatí fakturu v definovaném období, faktura se považuje za vypršenou. Faktura je považována za "zaplatěnou" jakmile je transakce viditelná na blockchainu (o-potvrzení), ale za "dokončenou" se považuje, když dosáhne počtu potvrzení, který obchodník definoval (obvykle 1-6). Časovač je přizpůsobitelný.

#### Považujte fakturu za zaplacenou i když zaplacená částka je ..% nižší než očekávaná.

V situaci, kdy zákazník používá k platbě za fakturu přímo peněženku z burzy, burza si vezme malý poplatek. To znamená, že taková faktura není považována za plně dokončenou. Faktura získá status "částečně zaplaceno". Pokud obchodník chce akceptovat nedoplatky na fakturech, můžete zde nastavit procentní sazbu.

### Požadavky

Platební požadavky jsou funkcí, která umožňuje majitelům obchodů BTCPay vytvářet dlouhodobé faktury. Platby za platební požadavek se provádějí podle směnného kurzu v době platby. To umožňuje uživatelům platit podle svého pohodlí bez nutnosti dohody nebo ověřování směnných kurzů s majitelem obchodu v době platby.

Uživatelé mohou platit požadavky částečnými platbami. Platební požadavek zůstává platný, dokud není zaplacen v plné výši nebo pokud majitel obchodu vyžaduje čas vypršení platnosti. Adresy se nikdy nepoužívají znovu. Při každém kliknutí na platbu pro vytvoření faktury pro platební požadavek se generuje nová adresa.

Majitelé obchodů mohou tisknout platební požadavky (nebo exportovat data faktur) pro účely vedení záznamů a účetnictví. BTCPay automaticky označuje faktury jako Platební Požadavky ve vašem seznamu faktur obchodu.

#### Přizpůsobte si své Platební Požadavky

- Částka Faktury - Nastavte Požadovanou Částku Platby
- Měna - Zobrazte Požadovanou Částku ve Fiatu nebo Kryptoměně
- Množství Plateb - Povolte pouze jednorázové platby nebo částečné platby
- Čas Vypršení - Povolte platby do určitého data nebo bez vypršení
- Popis - Textový Editor, Datové Tabulky, Vložení Fotografií & Videí
- Vzhled - Barva a Styl s CSS Tématy

![image](assets/en/93.webp)

#### Vytvořte Platební Požadavek

V levém menu přejděte na Platební Požadavek a klikněte na "Vytvořit Platební Požadavek".

![image](assets/en/94.webp)

Zadejte Název Požadavku, Částku, Zobrazovanou Měnu, Přiřazený Obchod, Čas Vypršení & Popis (Volitelně)

Vyberte možnost Povolit plátci vytvářet faktury ve své měně, pokud chcete umožnit částečné platby.

Klikněte na Uložit & Zobrazit pro kontrolu vašeho platebního požadavku.

BTCPay vytvoří URL pro platební požadavek. Sdílejte tuto URL pro zobrazení vašeho platebního požadavku. Potřebujete více stejných požadavků? Můžete duplikovat platební požadavky pomocí možnosti Klonovat v hlavním menu.

![image](assets/en/95.webp)

**VAROVÁNÍ**

Platební požadavky jsou závislé na obchodu, což znamená, že každý platební požadavek je při vytváření spojen s obchodem. Ujistěte se, že máte k obchodu, ke kterému platební požadavek patří, připojenou peněženku.

#### Zaplacený Požadavek

Plátce i žadatel mohou po odeslání platby zobrazit stav platebního požadavku. Stav se zobrazí jako Vyrovnaný, pokud byla platba přijata v plné výši. Pokud byly provedeny pouze částečné platby, Zbývající Částka ukáže zbývající dluh.

![image](assets/en/96.webp)

#### Přizpůsobení Platebních Požadavků

Obsah popisu lze upravit pomocí textového editoru platebního požadavku. Obě možnosti jsou k dispozici, pokud chcete použít další barevná témata nebo vlastní CSS stylování.
Ne-techničtí uživatelé mohou použít [bootstrap téma](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Další přizpůsobení je možné provést poskytnutím dodatečného CSS kódu, jak je ukázáno níže.

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
  background: lineární gradient(#59316b, #331840);
}

#mainNav .btn-link {
  color: white;
}
```

### Pull platby

Tradičně příjemce sdílí svou Bitcoin adresu pro provedení Bitcoin platby a odesílatel později pošle peníze na tuto adresu. Takový systém se nazývá Push platba, protože odesílatel iniciuje platbu, zatímco příjemce může být nedostupný, tlačí platbu příjemci.

Co když ale role obrátíme?

Co když místo toho, aby odesílatel tlačil platbu, odesílatel umožní příjemci vytáhnout platbu v okamžiku, který příjemce považuje za vhodný? To je koncept Pull platby. To umožňuje několik nových aplikací, jako jsou:

- Služba předplatného (kde předplatitel umožní službě pravidelně vytahovat peníze každou určitou dobu)
- Vrácení peněz (kde obchodník umožní zákazníkovi vytáhnout peníze na vrácení do jeho peněženky, když to uzná za vhodné)
- Časově založené fakturování pro freelancery (kde osoba najímající umožní freelancerovi vytáhnout peníze do jeho peněženky podle nahlášeného času)
- Patronát (kde patron umožní příjemci vytahovat peníze každý měsíc pro pokračování podpory jejich práce)
- Automatický prodej (kde zákazník burzy by umožnil burze pravidelně každý měsíc vytahovat peníze z jeho peněženky na prodej)
- Systém výběru zůstatku (kde služba s vysokým objemem umožní uživatelům požádat o výběry ze svého zůstatku, služba pak může snadno zpracovat všechny platby pro mnoho uživatelů ve fixních intervalech)

### Výplaty

Funkcionalita výplat je spojena s [Pull Platbami](https://docs.btcpayserver.org/PullPayments/). Tato funkce vám umožňuje vytvářet výplaty ve vašem BTCPay. Tato funkce umožňuje zpracování pull platby (vrácení peněz, výplaty platu nebo výběry).

#### Příklad 1: Vrácení peněz

Začněme s příkladem vrácení peněz. Zákazník si koupil položku ve vašem obchodě, ale bohužel ji musí vrátit. Chce vrácení peněz. V BTCPay můžete vytvořit [Vrácení peněz](https://docs.btcpayserver.org/Refund/) a poskytnout zákazníkovi odkaz pro nárok na jejich prostředky. Jakmile zákazník poskytne svou adresu a nárokuje prostředky, bude to zobrazeno ve Výplatách.

První stav, který má, je Čekání na schválení. Pracovníci obchodu mohou zkontrolovat, jestli na schválení čeká více výplat, a po výběru použijí tlačítko Akce.

Možnosti na tlačítku akce

- Schválit vybrané výplaty
- Schválit a poslat vybrané výplaty
- Zrušit vybrané výplaty

Dalším krokem je Schválit a poslat vybrané výplaty, protože chceme zákazníkovi vrátit peníze. Zkontrolujte Adresu zákazníka, zobrazí se částka a rozhodněte, zda chcete, aby byly poplatky odečteny z vrácení peněz nebo ne. Jakmile provedete kontroly, zbývá už jen podepsat transakci.
Zákazník je nyní informován na stránce s nároky. Může sledovat transakci, protože má k dispozici odkaz na block explorer a jeho transakci. Jakmile je transakce potvrzena a stav se změní na Dokončeno.

#### Příklad 2: Plat

Nyní se podívejme na výplatu platu, jelikož je řízena zevnitř obchodu a ne na žádost zákazníka. Základ je stejný; používá se Pull platby. Ale místo vytvoření vrácení peněz, vytvoříme [Pull Platbu](https://docs.btcpayserver.org/PullPayments/).

Přejděte na kartu Pull Platby ve vašem BTCPay serveru. V pravém horním rohu klikněte na tlačítko Vytvořit Pull Platbu.

Nyní jsme v procesu vytváření Výplaty, dejte jí název a požadovanou částku ve vybrané měně, vyplňte Popis, aby zaměstnanec věděl, o co jde. Další část je podobná vrácení peněz. Zaměstnanec vyplní Cílovou adresu a částku, kterou chce z této Výplaty nárokovat. Může se rozhodnout pro 2 samostatné nároky na různé adresy, nebo dokonce částečně nárokovat přes lightning.

Pokud čeká více Výplat, můžete je dávkově podepsat a odeslat. Jakmile jsou podepsány, výplaty přejdou na kartu Ve zpracování a zobrazí se Transakce. Když je přijata sítí, výplata přejde na kartu Dokončeno. Karta Dokončeno slouží čistě pro historické účely. Obsahuje zpracované Výplaty a transakci, která k ní patří.

### Pull platby

#### Koncept

Když odesílatel nastaví Pull platbu, může konfigurovat několik vlastností:

- Název Pull požadavku
- Limitní částka
- Jednotka (jako BTC, SAT, USD)
- Metody platby
  - BTC On-chain
  - BTC Off-chain
- Popis
- Vlastní CSS
- Datum ukončení (volitelné pro Lightning Network BOLT11)

Po tomto může odesílatel sdílet pull platbu pomocí odkazu s příjemcem, což umožní příjemci vytvořit výplatu. Příjemce si vybere:

- Kterou platební metodu použít
- Kam poslat peníze

Jakmile je výplata vytvořena, bude započítána do limitu pull platby pro aktuální období. Odesílatel poté schválí výplatu nastavením sazby, ve které bude výplata odeslána, a pokračuje v platbě.

Pro odesílatele poskytujeme snadno použitelný způsob, jak dávkově platit několik výplat z [BTCPay Interní Peněženky](https://docs.btcpayserver.org/Wallet/).

#### Greenfield API

BTCPay Server poskytuje plné API jak pro odesílatele, tak pro příjemce, které je dokumentováno na stránce `/docs` vaší instance. (nebo na webové stránce dokumentace https://docs.btcpayserver.org)

Protože naše API vystavuje plnou schopnost pull plateb, může odesílatel automatizovat platby podle svých potřeb.

### Shrnutí dovedností

V této sekci jste se naučili následující:

- Hluboké porozumění stavům faktur BTCPay Serveru a akcím, které lze na nich provádět
- Přizpůsobení a správa mechanismů faktur s prodlouženou platností známých jako Požadavky.
- Další flexibilní možnosti platby, které otevírá jedinečná funkce Pull Platby BTCPay Serveru, zejména jak zvládat vrácení peněz a platby platu.

### Hodnocení znalostí

#### KA Konceptuální přezkum

Jaké jsou některé rozdíly mezi fakturami a platebními požadavky a jaký by mohl být dobrý důvod pro použití těch druhých?

#### KA Konceptuální přezkum

Jak pull platby rozšiřují to, co obvykle lze dělat on-chain? Popište některé případy použití, které umožňují.

## Výchozí pluginy BTCPay Serveru

<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>

### Standardní pluginy a aplikace

BTCPay server přichází se standardní sadou pluginů (aplikací), které mohou BTCPay Server proměnit v platební bránu pro e-commerce. S přídavky bodu prodeje (Point Of Sale), platformy pro crowdfunding a jednoduchým tlačítkem pro platbu se BTCPay Server stává snadno nasaditelným řešením.

### Bod prodeje

Jedním ze standardních pluginů BTCPay Serveru je Bod prodeje (PoS). S pluginem PoS může majitel obchodu vytvořit Webshop přímo z BTCPay Serveru, majitel obchodu nepotřebuje třetí strany pro e-commerce řešení k provozování Webshopu. Webová aplikace PoS umožňuje uživatelům s kamennými obchody snadno přijímat Bitcoin, bez poplatků nebo třetí strany, přímo do jejich peněženky. PoS lze snadno zobrazit na tabletech nebo jiných zařízeních podporujících webové prohlížení. Uživatelé mohou snadno vytvořit zástupce na domovské obrazovce pro rychlý přístup k webové aplikaci.

#### Jak vytvořit nový Bod prodeje

BTCPay Server umožňuje majitelům obchodů rychle vytvořit Bod prodeje v několika rozvrženích. BTCPay Server si uvědomuje, že ne každý obchod je e-commerce, a ne každý obchod je bar nebo restaurace, a přichází s několika standardními nastaveními pro váš PoS.

Když majitel obchodu klikne na "Bod prodeje" ve svém levém menu, BTCPay Server nyní požádá o název; tento název bude viditelný v levém menu. Klikněte na Vytvořit pro vytvoření PoS.

![image](assets/en/97.webp)

#### Aktualizace nově vytvořeného Bodu prodeje

Po vytvoření nového PoS následuje obrazovka pro aktualizaci vašeho Bodu prodeje a přidání položek pro váš obchod.

##### Název aplikace

Název, který zde dáte vašemu Bodu prodeje, bude viditelný v hlavním menu BTCPay Serveru.

##### Zobrazovaný název

Veřejnost uvidí veřejný titul nebo název při návštěvě vašeho obchodu. BTCPay Server jako standard pojmenuje váš obchod „Čajovna“. Nahraďte to názvem vašeho obchodu.

![image](assets/en/98.webp)

#### Vyberte styl Bodu prodeje

BTCPay Server je schopen zobrazit svůj Bod prodeje několika způsoby.

- Seznam produktů
  - Zobrazení obchodu, kde zákazníci mohou koupit pouze 1 produkt najednou.
- Seznam produktů s košíkem.
  - Zobrazení obchodu, kde zákazníci mohou koupit několik položek najednou a získat přehled o nákupním košíku vpravo na obrazovce.
- Pouze klávesnice
  - Žádný seznam produktů, pouze klávesnice pro přímé fakturování.
- Zobrazení pro tisk (Tisknutelný seznam produktů s QR)
  - Pokud nemůžete vždy zobrazit svůj seznam produktů digitálně, potřebujete "offline" řešení pro produkty; BTCPay Server má funkci zobrazení pro tisk jako Offline obchod.

![image](assets/en/99.webp)

#### Styl Bodu prodeje - Seznam produktů

![image](assets/en/100.webp)

#### Styl Bodu prodeje - Seznam produktů + Košík

![image](assets/en/101.webp)

#### Styl Bodu prodeje - Pouze klávesnice

![image](assets/en/102.webp)

#### Styl Bodu prodeje - Zobrazení pro tisk

![image](assets/en/103.webp)

#### Měna

Majitel obchodu může nastavit pro svůj Bod prodeje jinou měnu než je jeho celkově nastavená výchozí měna. Výchozí měna obchodu se automaticky vyplní do tohoto pole.

#### Popis

Povězte světu o svém obchodu; co prodáváte a za kolik? Vše, co vysvětluje váš obchod, sem patří.

#### Produkty

Když je vytvořen Bod prodeje, standardní BTCPay Server přidá do obchodu několik položek pro referenci. Klikněte na tlačítko Upravit u kterékoli ze standardních položek, abyste lépe pochopili každou možnou volbu pro položku.

Vytvoření nového produktu ve vašem obchodě zahrnuje následující pole;

- Název
- Cena (pevná, minimální nebo vlastní)
- URL obrázku
- Popis
- Inventář
- ID
- Text tlačítka Koupit.
- Povolit/Zakázat

Jakmile majitel obchodu vyplní všechna pole nového produktu, klikne na uložit a všimne si, že sekce Produkty v Bodu prodeje se nyní naplňuje. Vždy se ujistěte, že uložíte v pravém horním rohu obrazovky, aby majitelé obchodů nepřišli o svůj pokrok při přidávání produktů.

Majitelé obchodů mohou také použít "Raw Editor" pro konfiguraci svých produktů. Raw editor vyžaduje základní porozumění strukturám JSON.

#### Pokladna

BTCPay Server umožňuje malé specifické úpravy pokladny pro PoS. Majitel obchodu může nastavit text "Koupit za x" nebo požadovat konkrétní údaje od zákazníka přidáním formulářů.

#### Spropitné

Ne všechny obchody potřebují možnost spropitného u svých prodejů. Majitelé obchodů mohou tuto možnost zapnout nebo vypnout, jak uznají za vhodné pro svůj obchod. Pokud obchod používá spropitné, majitel obchodu může nastavit text v poli pro spropitné, který se mu líbí. Spropitné v BTCPay Serveru funguje na základě procentuální částky. Majitelé obchodů mohou přidat více procent s oddělením čárkou.

#### Slevy

Jako majitel obchodu možná budete chtít zákazníkovi poskytnout vlastní slevu při pokladně; přepínač pro Slevy se stává dostupným ve vaší pokladně obchodu. Toto je ovšem velmi nedoporučováno u systémů samoobslužné pokladny.

#### Vlastní platby

Když je možnost Vlastní platby zapnutá, zákazník může zadat svou stanovenou cenu rovnou nebo vyšší než původní faktura vygenerovaná obchodem.

#### Další možnosti

Po nastavení všeho pro váš Bod prodeje zůstává několik dalších možností. Majitelé obchodů mohou snadno vložit svůj PoS prostřednictvím Iframe nebo vložit tlačítko platby odkazující na konkrétní položku obchodu. Pro stylizaci právě vytvořeného obchodu PoS mohou majitelé obchodů přidat vlastní CSS na konec dalších možností.

#### Odstranit tuto aplikaci

Pokud majitel obchodu chce zcela odstranit Bod prodeje ze svého BTCPay Serveru, na konci aktualizace PoS mohou majitelé obchodů kliknout na tlačítko Odstranit tuto aplikaci, aby úplně zničili svou aplikaci PoS. Když kliknete na "Odstranit tuto aplikaci", BTCPay Server požádá o potvrzení zadáním `DELETE` a potvrzením kliknutím na tlačítko Odstranit. Po odstranění se majitel obchodu vrátí na dashboard BTCPay Serveru.

### BTCPay Server - Crowdfund

Vedle pluginu Bod prodeje má BTCPay Server možnost vytvořit crowdfund. Stejně jako jakákoli jiná platforma pro crowdfund, majitelé obchodů mohou stanovit cíl, vytvořit výhody pro příspěvky a přizpůsobit je podle svých potřeb.

#### Jak nastavit nový crowdfund

Klikněte na plugin Crowdfund prostřednictvím hlavního menu vlevo od vašeho BTCPay Serveru, pod sekci Plugin. BTCPay Server nyní požádá o název pro Crowdfund; tento název bude také zobrazen v levém menu.

#### Aktualizace nově vytvořeného Bodu prodeje

Jakmile je aplikaci dán název, další obrazovka bude k aktualizaci aplikace, aby měla kontext.

#### Název aplikace

Název daný vašemu Crowdfundu bude viditelný v hlavním menu BTCPay Serveru.

#### Zobrazit název

Název je dán pro Crowdfund veřejnosti.

#### Slogan

Dejte Crowdfundu jednoduchý slogan, aby bylo poznat, o co ve sbírce jde.

![obrázek](assets/en/107.webp)

#### URL hlavního obrázku

Každý Crowdfund má svůj hlavní obrázek, ten banner, který rozeznáte ihned. Tento obrázek může být uložen na vašem serveru, pokud máte administrátorská práva, Admini mohou nahrávat pod nastaveními serveru BTCPay Server - Soubory. Když jste majitelem obchodu, obrázek musí být nahrán na web prostřednictvím hostingu třetí strany (například imgur)

#### Zveřejnit Crowdfund

Toto přepínač zpřístupní váš Crowdfund veřejnosti a tím bude viditelný pro vnější svět. Pro účely testování nebo pro ověření správné aplikace vašeho tématu, můžete chtít toto nastavení nechat na OFF po dobu vytváření Crowdfundu.

#### Popis

Povězte světu o vašem Crowdfundu, na co sbíráte? Vše, co vysvětluje váš Crowdfund, patří sem.

![obrázek](assets/en/108.webp)

#### Cíl Crowdfundu

Nastavte cílovou částku, kterou by sbírka měla pro projekt vydělat a v jaké měně má být cíl vyjádřen. Ujistěte se, že pokud jsou vaše cíle stanoveny mezi daty, zahrněte tyto cílové a koncové termíny pod Cíle v Crowdfundu.

![obrázek](assets/en/109.webp)

#### Výhody

Výhody hodně pomáhají vašemu crowdfunding. To je proto, že výhody dávají lidem způsob, jak se zapojit do vaší kampaně. Oslovují jak sobecké motivace, tak i altruistické motivace. A umožňují vám přístup k výdajům vašich podporovatelů, nikoli jen k jejich filantropické peněžence - můžete si domyslet, které je významnější.

Vytvoření nové výhody zahrnuje následující pole;

- Název
- Cena (pevná, minimální nebo vlastní)
- URL obrázku
- Popis
- Inventář
- ID
- Text tlačítka Koupit.
- Povolit/Zakázat

Jakmile majitel obchodu vyplní všechna pole nové výhody, klikne na uložit a všimne si, že sekce Výhody v Crowdfundu je nyní naplněna.

![obrázek](assets/en/110.webp)

### BTCPay Server - Bod prodeje

#### Příspěvky

Majitelé obchodů mohou vybírat, jak zobrazit Výhody, jak jsou řazeny nebo dokonce hodnoceny oproti ostatním výhodám. Jakmile jsou však cíle Crowdfundu dosaženy, majitelé obchodů mohou chtít zastavit příliv darů k této sbírce. Proto může přepnout "Nepovolovat další příspěvky po dosažení cíle". To zastaví přijímání darů pro Crowdfund.

##### Chování Crowdfundu

Standard Crowdfundu počítá pouze faktury vytvořené s Crowdfundem směrem k cíli. Mohou však nastat případy, kdy majitel obchodu chce, aby všechny faktury vytvořené v tomto obchodě byly počítány směrem k Crowdfundu.

#### Další možnosti přizpůsobení

BTCpay Server nabízí několik dalších přizpůsobení. Přidejte zvuky, animace nebo dokonce diskusní vlákna k Crowdfundu. Majitelé obchodů mohou také změnit vzhled a pocit Crowdfundu zadáním vlastního CSS.

#### Smazat tuto aplikaci

Pokud chce majitel obchodu zcela odstranit Crowdfund ze svého BTCPay Serveru, na konci aktualizace Crowdfundu může majitel obchodu kliknout na tlačítko „Smazat tuto aplikaci“ a tím zcela zničit svou aplikaci Crowdfund. Při kliknutí na "Smazat tuto aplikaci" BTCPay Server požádá o potvrzení zadáním `DELETE` a potvrzením kliknutím na tlačítko Smazat. Po smazání se majitel obchodu vrátí na dashboard BTCPay Serveru.

### BTCPay Server - Tlačítko platby

Snadno vkládatelná HTML a vysoce přizpůsobitelná tlačítka pro platby umožňují majitelům obchodů přijímat spropitné a dary. V levém menu BTCPay Serveru, pod sekci Plugins, majitelé obchodů mohou kliknout na „Pay Button“ a kliknout na Enable, aby vytvořili tlačítko pro platbu.

#### Obecná nastavení

V Obecných nastaveních pro tlačítko Platby mohou majitelé obchodů nastavit

- Standardní cenu
- Výchozí měnu
- Výchozí způsob platby
  - Použít výchozí nastavení obchodu
  - BTC on-chain
  - BTC Off-chain (Lightning)
  - BTC Off-chain (LNURL-pay)
- Popis při placení
- ID objednávky

#### Možnosti zobrazení

Tlačítko Platby na BTCPay Serveru lze konfigurovat tak, aby vyhovovalo různým stylům. Tlačítka mohou mít pevnou nebo vlastní částku, buď zobrazenou pomocí posuvníku nebo pomocí tlačítek plus a mínus.

#### Použití modálního okna

Při vytváření tlačítka pro platbu mohou majitelé obchodů zvolit jeho chování, když na něj zákazník klikne, a zobrazit ho v modálním okně nebo na nové stránce.

**!?Poznámka!?**

Upozornění: Tlačítko pro platbu by mělo být používáno pouze pro spropitné a dary

Používání tlačítka pro platbu pro integrace e-commerce není doporučeno, protože informace relevantní pro objednávku mohou být uživatelem upraveny. Pro e-commerce byste měli použít naše Greenfield API. Pokud tento obchod zpracovává komerční transakce, doporučujeme vytvořit před použitím tlačítka pro platbu samostatný obchod.

#### Přizpůsobení textu tlačítka Platby

Ve výchozím nastavení tlačítko pro platbu BTCPay Serveru uvádí "Platit s BTCPay". Majitelé obchodů mohou tento text upravit podle svého přání a změnit logo BTCPay Serveru za své vlastní. Text nastavíte pomocí "Pay Button Text" a URL obrázku vložíte pod "Pay Button Image URL".

##### Velikost obrázku

Velikost obrázku na tlačítku lze nastavit pouze na tři výchozí hodnoty.

- 146x40px
- 168x46px
- 209x57px

#### Typ tlačítka

BTCPay Server zná tři stavy pro tlačítko Platby.

- Pevná částka
  - Předem nastavená cena je v obecných nastaveních tlačítka.
- Vlastní částka
  - Tlačítko Platby na BTCPay Serveru má tlačítka + a - pro nastavení vlastní ceny.
  - Při použití vlastní částky BTCPay Server požádá o Min, Max a jak postupně by měla částka narůstat.
  - Tlačítka mohou být nastavena na „Použít jednoduchý styl vstupu“. To odstraní tlačítka +/-.
  - Tlačítko se vejde do řádku, kde tlačítko a přepínače se zobrazují v řadě.
- Posuvník
  - Podobně jako u vlastní částky, ale vizuálně se liší tím, že má posuvník místo tlačítek +/-.
  - Při použití posuvníku BTCPay Server požádá o Min, Max a jak postupně by měla částka narůstat.

**!?Poznámka!?**

Odstranění tlačítka Platby lze provést nahoře v popisu upozornění.

#### Oznámení o platbě

Server IPN (Okamžité oznámení o platbě) je určen pro webhooks a může být vyplněn URL pro odeslání dat po nákupu.

#### Oznámení e-mailem

Kdykoli dojde k platbě, BTCPay Server může informovat majitele obchodu.

#### Přesměrování prohlížeče

Když zákazník dokončí nákup, bude přesměrován na tento odkaz, pokud jej majitel obchodu nastavil.

#### Pokročilé možnosti tlačítka Platby

Určete další parametry řetězce dotazu, které by měly být připojeny k stránce pro placení po vytvoření faktury. Například, `lang=da-DK` by načetlo stránku pro placení ve výchozím jazyce dánsky.

#### Použití aplikace jako koncového bodu

Přímo propojte tlačítko pro platbu s položkou v jedné z aplikací PoS nebo Crowdfund předtím.
Majitelé obchodů mohou kliknout na rozbalovací menu a vybrat požadovanou Aplikaci; jakmile je Aplikace vybrána, majitel obchodu může přidat položku, která má být propojena.

#### Generovaný kód

Jelikož je tlačítko pro platbu od BTCPay Server snadno vkládatelné HTML, BTCPay Server zobrazuje na konci po nastavení tlačítka pro platbu generovaný kód pro kopírování na webovou stránku.

Majitelé obchodů mohou zkopírovat generovaný kód na svou webovou stránku a tlačítko pro platbu od BTCPay Server je přímo aktivní na jejich webové stránce.

#### Oznámení o platbě

Serverové IPN (Okamžité oznámení o platbě) je určeno pro webhooks a může být vyplněno URL adresou pro odeslání dat o nákupu.

#### Emailová oznámení

Kdykoliv dojde k platbě, BTCPay Server může informovat majitele obchodu.

#### Přesměrování prohlížeče

Když zákazník dokončí nákup, bude přesměrován na tento odkaz, pokud jej nastavil majitel obchodu.

#### Pokročilé možnosti tlačítka pro platbu

Určete další parametry řetězce dotazu, které by měly být připojeny k stránce pro placení, jakmile je vytvořena faktura. Například, `lang=da-DK` by načetlo stránku pro placení ve výchozím jazyce dánsky.

#### Použití aplikace jako koncového bodu

Přímo propojte tlačítko pro platbu s položkou v jedné z aplikací PoS nebo Crowdfund předtím. Majitelé obchodů mohou kliknout na rozbalovací menu a vybrat požadovanou aplikaci, jakmile je aplikace vybrána, majitel obchodu může přidat položku, která má být propojena.

#### Generovaný kód

Jelikož je tlačítko pro platbu od BTCPay Server snadno vkládatelné HTML, BTCPay Server zobrazuje na konci po nastavení tlačítka pro platbu generovaný kód pro kopírování na webovou stránku. Majitelé obchodů mohou zkopírovat generovaný kód na svou webovou stránku a tlačítko pro platbu od BTCPay Server je přímo aktivní na jejich webové stránce.

### Shrnutí dovedností

V této sekci jste se naučili:

- Jak používat integrovaný plugin PoS od BTCPay Server pro snadné vytvoření vlastního obchodu
- Jak používat integrovaný plugin Crowdfund od BTCPay Server pro snadné vytvoření vlastní crowdfund aplikace
- Generování kódu pro vlastní tlačítko pro platbu pomocí pluginu Pay Button

### Hodnocení znalostí

#### KA Review

Jaké jsou tři vestavěné pluginy, které jsou standardně součástí BTCPay Server? Popište několika slovy, jak lze každý použít.

# Konfigurace BTCPay Server

<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>

## Základní pochopení instalace BTCPay Server v prostředí LunaNode

<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>

### Instalace BTCPay Server na Hostovaném Prostředí (LunaNode)

Tyto kroky poskytnou veškeré informace potřebné k začátku používání BTCPay Server na LunaNode. Existuje mnoho možností, jak software nasadit.
Všechny detaily o BTCPay Server najdete na https://docs.btcpayserver.org.

#### Kde začít?

V této části se seznámíte s LunaNode jako poskytovatelem hostingu, naučíte se první kroky používání vašeho BTCPay Server a jak postupovat s Lightning Network. Po projití všemi kroky budete moci provozovat webshop nebo crowdfund platformu přijímající Bitcoin!

To je jedna z mnoha cest, jak nasadit BTCPay Server. Pro více detailů čtěte naši dokumentaci,

https://docs.btcpayserver.org.

### Nasazení BTCPay Server - LunaNode

Nejprve jděte na webovou stránku LunaNode.com, kde si vytvoříme nový účet. Klikněte vpravo nahoře na Sign Up nebo použijte průvodce Get Started na jejich domovské stránce.
![image](assets/en/111.webp)

Po vytvoření nového účtu LunaNode pošle ověřovací email. Jakmile účet ověříte, oproti Voltage, ihned se vám nabídne možnost doplnit zůstatek na účtu. Tento zůstatek je potřebný k zaplacení prostoru na serveru a nákladů na hosting.

![image](assets/en/112.webp)

#### Přidejte kredit na váš účet u LunaNode

Jakmile kliknete na "Deposit credit", můžete nastavit, kolik chcete na účet doplnit a jakým způsobem za to zaplatíte. LunaNode a BTCPay Server budou stát mezi 10$USD a 20$USD za měsíc.
Oproti Voltage.cloud, získáte plný přístup k vašemu Virtual Private Server (VPS odteď) a tím pádem máte větší kontrolu nad vaším serverem. Po vytvoření nového účtu LunaNode pošle ověřovací email.
Jakmile účet ověříte, oproti Voltage, nyní ihned dostanete možnost doplnit zůstatek na účtu. Tento zůstatek je potřebný k zaplacení prostoru na serveru a nákladů na hosting.

#### Jak nasadit nový server?

V tomto průvodci projdeme nastavením vytvořením sady API klíčů a použitím spouštěče BTCPay Server od LunaNode.

Ve vašem dashboardu LunaNode klikněte vpravo nahoře na API. To otevře novou stránku. Musíme jen nastavit jméno pro API klíč. Zbytek zařídí LunaNode a nebude pokryto v tomto průvodci. Klikněte na tlačítko Create API Credential.
Po vytvoření API přihlašovacích údajů získáte dlouhý řetězec písmen a znaků. To je váš API klíč.

![image](assets/en/113.webp)

#### Jak nasadit nový server?

Tyto přihlašovací údaje mají 2 části, API klíč a API ID; budeme potřebovat obojí. Než přejdeme k dalšímu kroku, otevřeme si druhou záložku v prohlížeči a jdeme na https://launchbtcpay.lunanode.com/

Zde budete požádáni o poskytnutí vašeho API klíče a API ID. To slouží k ověření, že jste to vy, kdo provádí nasazení nového serveru. API klíč by měl být stále otevřený ve vaší předchozí záložce; pokud se posunete dolů v tabulce, najdete API ID.

Vraťte se na stránku s Launcherem, vyplňte pole s vaším API klíčem a ID a klikněte na pokračovat.

![image](assets/en/114.webp)

V dalším kroku můžete poskytnout název domény. Pokud již vlastníte doménu a chcete ji použít pro BTCPay Server, ujistěte se, že také přidáte DNS záznam (nazývaný `A` záznam) na vaší doméně. Pokud doménu nevlastníte, použijte doménu poskytnutou LunaNode (to můžete později změnit v nastavení BTCPay Serveru) a klikněte na Pokračovat.

Přečtěte si více o nastavení nebo změně DNS záznamu pro BTCPay Server; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name

#### Spuštění BTCPay Serveru na LunaNode

Po provedení předchozích kroků můžeme nastavit všechny možnosti pro náš nový server. Zde vybereme Bitcoin (BTC) jako naši podporovanou měnu; můžeme nastavit email pro oznámení o obnově šifrovacích certifikátů; to není povinné.
Tento průvodce má za cíl nastavit prostředí Mainnet (reálný svět Bitcoinu); nicméně, LunaNode také umožňuje nastavit toto na Testnet nebo Regtest pro účely vývoje. V tomto průvodci necháme nastavení na možnost Mainnet.
Vyberte si vaši implementaci Lightning. LunaNode nabízí dvě různé implementace, LND a Core Lightning. Pro tento průvodce si vybereme LND. Existují malé, ale skutečné rozdíly mezi oběma implementacemi; pro více informací doporučujeme číst rozsáhlou dokumentaci; https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln

![image](assets/en/115.webp)

LunaNode nabízí několik plánů Virtuálního Stroje (VM). Ty se liší cenovými relacemi a specifikacemi serveru. Pro tento průvodce postačí plán m2; nicméně, pokud jste zaškrtli více než jen Bitcoin jako měnu, zvažte použití alespoň m4.

Zrychlení počáteční synchronizace blockchainu; toto je volitelné a závisí na vašich potřebách. Existují pokročilé možnosti jako nastavení Lightning Alias, ukázání na konkrétní vydání na GitHubu, nebo nastavení SSH klíčů; žádné z těchto nebudou v tomto průvodci zmíněny.

Po vyplnění formuláře musíte kliknout na Launch VM, a LunaNode začne vytvářet váš nový VM, včetně nainstalovaného BTCPay Serveru. Tento proces trvá několik minut; jakmile je váš server připraven, LunaNode vám poskytne odkaz na váš nový BTCPay Server.

Po procesu vytvoření klikněte na odkaz na váš BTCPay Server; zde budete požádáni o vytvoření účtu Administrátora.

![image](assets/en/116.webp)

### Shrnutí dovedností

V této sekci jste se naučili:

- Vytvoření a financování účtu na LunaNode
- Použití BTCPay Server Launcheru k vytvoření vlastního serveru

### Hodnocení znalostí

#### KA Konceptuální přehled

Popište některé rozdíly mezi provozováním instance BTCPay Serveru na VPS oproti vytvoření účtu na hostované instanci.

## Instalace BTCPay Serveru na prostředí Voltage

<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>

Seznámíte se s Voltage.cloud jako poskytovatelem hostingu, naučíte se o prvních krocích používání vašeho BTCPay Serveru a dozvíte se, jak postupovat s Lightning Network. Po projití všemi kroky budete moci provozovat webshop nebo platformu pro crowdfunding přijímající Bitcoin!

To je jedna z mnoha cest, jak nasadit BTCPay Server. Pro více detailů čtěte naši dokumentaci,
https://docs.btcpayserver.org.

### Nasazení BTCPay Serveru - Voltage.cloud

Nejprve jděte na webovou stránku Voltage.cloud a zaregistrujte nový účet. Při vytváření účtu se můžete přihlásit na 7denní bezplatnou zkušební verzi. Buď klikněte na Sign Up vpravo nahoře nebo použijte "Try a free 7 day trial" na jejich domovské stránce.

![image](assets/en/117.webp)

Po vytvoření účtu klikněte na tlačítko `NODES` na vašem řídicím panelu. Jakmile jsme vybrali Nodes a vytvořili nový uzel, jsou nám prezentovány možné uzly, které Voltage nabízí. Jelikož tento průvodce také pojednává o LightningNetwork, musíme na Voltage nejprve vybrat naši implementaci Lightningu, než vytvoříme BTCPay Server. Klikněte na LightningNode.

![image](assets/en/118.webp)
Zde si budete muset vybrat, jaký typ Lightning uzlu chcete. Voltage nabízí různé možnosti pro vaše osvětlení. To se liší od nasazení například s LunaNode. Pro účely tohoto průvodce postačí Lite Node. Přečtěte si více o rozdílech na Voltage.cloud.
![image](assets/en/119.webp)

Dejte svému uzlu Název, nastavte heslo a toto heslo si zabezpečte. Pokud toto heslo ztratíte, ztratíte přístup k zálohám a Voltage je nemůže obnovit. Vytvořte uzel a Voltage vám ukáže průběh. Voltage vytvořil váš Lightning uzel. Nyní můžeme vytvořit instanci BTCPay Serveru a přímo přistupovat k Lightning Network.

Klikněte na Uzly v levém horním rohu vašeho řídicího panelu. Zde můžete nastavit další část vaší instance BTCPay Serveru. Klikněte na "vytvořit nový", jakmile se ocitnete v přehledu uzlů. Objeví se vám podobná obrazovka jako předtím. Nyní místo Lightning uzlu vybereme BTCPay Server.

Voltage vám ukáže geolokaci vašeho BTCPay Serveru, Voltage hostuje v regionu západního pobřeží USA. Zde uvidíte také cenu hostingu serveru. Klikněte na Vytvořit a dejte svému BTCPay Serveru název. Povolte Lightning a Voltage vám ukáže Lightning uzel vytvořený v předchozím kroku. Klikněte na Vytvořit a Voltage vytvoří instanci BTCPay Serveru.

![image](assets/en/120.webp)

Po kliknutí na vytvořit vám Voltage představí výchozí uživatelské jméno a heslo. Tyto údaje jsou podobné vašemu dříve nastavenému heslu ve Voltage. Klikněte na tlačítko Přihlásit se k účtu, abyste byli přesměrováni na váš BTCPay Server.

Vítejte ve vaší nové instanci BTCPay Serveru. Jelikož jsme již nastavili Lightning v procesu vytváření, ukazuje vám, že Lightning je již povolen!

### Shrnutí dovedností

V této kapitole jste se naučili:

- Vytvoření účtu na Voltage.cloud
- Kroky k získání BTCPay Serveru společně s Lightning uzlem na účtu

### Hodnocení znalostí

#### KA Konceptuální přezkum

Jaké jsou některé klíčové rozdíly mezi nastavením Voltage a LunaNode?

## Instalace BTCPay Serveru na Umbrel uzlu

<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>

Na konci těchto kroků budete moci přijímat lightning platby do vašeho obchodu BTCPay na vaší lokální síti. Tento proces se také vztahuje, pokud provozujete umbrel uzel v restauraci nebo podniku. Pokud chcete tento obchod připojit k veřejnému webu, postupujte podle pokročilého cvičení, abyste svůj umbrel uzel zpřístupnili veřejnosti.

https://umbrel.com/

![image](assets/en/121.webp)

### Nasazení BTCPay Serveru - Umbrel

Po úplné synchronizaci vašeho Umbrel uzlu s Bitcoin blockchainem přejděte do Umbrel App Store a vyhledejte BTCPay Server v sekci Aplikace.

![image](assets/en/122.webp)

Klikněte na BTCPay Server, abyste viděli detaily aplikace. Když jsou detaily pro BTCPay Server otevřené, v pravém dolním rohu se zobrazují požadavky pro správný běh aplikace. Ukazuje, že vyžaduje Bitcoin a Lightning uzel. Pokud jste na svém Umbrelu ještě nenainstalovali Lightning uzel, klikněte na Instalovat. Tento proces může trvat několik minut.

![image](assets/en/123.webp)

Po instalaci vašeho Lightning uzlu:

1. Klikněte na otevřít v detailu aplikace nebo na aplikaci v řídicím panelu Umbrel.
2. Klikněte na nastavit nový uzel; ukáže se vám 24 slov pro obnovu vašeho Lightning uzlu.
3. Tyto si poznamenejte.

![image](assets/en/124.webp)
Umbrel po vás bude chtít ověření slov, která jste právě zapsali. Po nastavení Lightning uzlu se vraťte do Umbrel App Store a najděte BTCPay Server. Klikněte na tlačítko instalovat a Umbrel zobrazí, zda jsou nainstalovány požadované komponenty a že BTCPay Server vyžaduje přístup k těmto komponentám. Po instalaci klikněte v pravém horním rohu na detaily aplikace na Otevřít nebo otevřete BTCPay Server přes dashboard vašeho Umbrelu.

Umbrel po vás bude chtít ověření slov, která jste právě zapsali.

![obrázek](assets/en/125.webp)

**!?Poznámka!?**

Ujistěte se, že je uložíte na vhodné místo, podobně jako jste se naučili ukládat klíče.

Po nastavení Lightning uzlu se vraťte do Umbrel App Store a najděte BTCPay Server. Klikněte na tlačítko instalovat a Umbrel zobrazí, zda jsou nainstalovány požadované komponenty a že BTCPay Server vyžaduje přístup k těmto komponentám.

![obrázek](assets/en/126.webp)

Po instalaci klikněte v pravém horním rohu na detaily aplikace na Otevřít nebo otevřete BTCPay Server přes dashboard vašeho Umbrelu.

![obrázek](assets/en/127.webp)

### Shrnutí dovedností

V této sekci jste se naučili:

- Kroky k instalaci BTCPay Serveru s funkcionalitou Lightning na uzlu Umbrel

### Hodnocení znalostí

#### KA Konceptuální přezkum

Jak se nastavení na Umbrelu liší od předchozích dvou hostovaných možností?

# Závěr

<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>



## Ohodnoťte kurz
<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>
<isCourseReview>true</isCourseReview>

## Závěr kurzu

<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

![obrázek](assets/en/128.webp)

Měli byste také mít obecné porozumění tomu, co je Bitcoin, jak funguje a jak může být škálovatelný díky druhým vrstvám jako je Lightning Network. V tomto kurzu jsme podrobně pokryli, jak může kdokoli používat BTCPay Server, od počáteční instalace po vytvoření obchodu a složité správě faktur, aby se stal finančně suverénní osobou nebo obchodníkem.

Gratulujeme k dokončení tohoto kurzu. Doufáme, že se vám obsah líbil a že budete pokračovat v používání a prozkoumávání BTCPay Serveru a že se těšíte na slibnou budoucnost Bitcoinu a na rostoucí komunitu tvůrců a účastníků, kterou přinese.

> **FOSS je nevyhnutelný.**

### Slovníček

| Termín                                         | Definice                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 51% útok                                       | Akt úmyslného vytváření nového nejdelšího řetězce bloků, který nahradí bloky v blockchainu. To vám umožňuje nahradit transakce, které byly začleněny do blockchainu. Tento druh útoku je nejsnadnější provést, když máte většinu těžební síly, proto se mu říká „Útok většiny“ nebo „51% útok“.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| AccountKey                                     | Klíč účtu pro rebasování                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| AccountKeyPath                                 | Cesta od kořene k klíči účtu je předponou otisku hlavního veřejného klíče.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Adresa                                         | Bitcoinové adresy kompaktně kódují informace potřebné k platbě příjemci. Moderní adresa se skládá z řetězce písmen a čísel, který začíná na bc1 a vypadá jako bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4. Adresa je zkratkou pro uzamykací skript příjemce, který může odesílatel použít k převedení prostředků příjemci. Většina adres buď reprezentuje veřejný klíč příjemce nebo nějakou formu skriptu, který definuje složitější podmínky výdaje. Předchozí příklad je bech32 adresa kódující svědka programu uzamčení prostředků na hash veřejného klíče (viz Pay-to-Witness-Public-Key-Hash). Existují také starší formáty adres, které začínají na 1 nebo 3 a používají kódování adres Base58Check pro reprezentaci hashů veřejných klíčů nebo hashů skriptů.                                         |
| Typ Adresy                                     | Adresa může reprezentovat několik různých skriptů. Adresy jsou kódovány a předponovány, aby vyjádřily jejich typ skriptu. Starší adresy používají Base58, a když je starší adresa hashem veřejného klíče, takzvaná P2PKH adresa, začíná na ‘1’. Méně často je starší adresa hashem skriptu, v takovém případě začne na ‘3’. Aktuálně jsou všechny SegWit adresy kódovány v Bech32 a začínají předponou ‘bc1’.                                                                                                                                                                                                                                                                                                                                                                                                |
| Aplikace                                       | BTCPay Server má pluginy, které mohou fungovat jako samostatná aplikace.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| BIP 329                                        | Export/import popisků peněženky                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| BIP49                                          | Definuje schéma derivace pro HD peněženky používající serializační formát P2WPKH-vnořený-v-P2SH (BIP 141) pro transakce se segregovaným svědkem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Bitcoinová Adresa                              | Alfanumerický řetězec, kam posíláte své bitcoiny, takže tam nyní "žijí" Je to identifikátor, který se skládá z řetězce asi 33 písmen a čísel kombinovaně. V současné verzi protokolu začíná adresa na 1, 3 nebo b. Mít adresu příjemce je nezbytnou součástí k iniciaci bitcoinové transakce. Bitcoinové adresy jsou generovány z veřejných klíčů a z jedné sady veřejných klíčů lze generovat několik adres, aby se zlepšilo soukromí. Bitcoinové adresy fungují stejně jako emailové adresy, pokud chcete poslat zprávu, potřebujete vědět, kam to jde, stejně je to s bitcoiny. Před odesláním bitcoinové transakce musíte zajistit, že adresa příjemce je přesná, protože bitcoinové transakce jsou nevratné a můžete posílat bitcoiny na adresu, která nepatří příjemci.                                |
| bitcoin versus Bitcoin                         | Bitcoin je měnová síť a bitcoin (s malým b) je měnová jednotka na síti Bitcoin. Používáte měnu bitcoin nebo token k transakci na síti Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Blok                                           | Blok je datová struktura v blockchainu Bitcoinu, která se skládá z hlavičky a těla bitcoinových transakcí. Blok je označen časovým razítkem a zavazuje se k určitému předchůdci (rodičovskému) bloku. Po zahashování poskytuje hlavička bloku důkaz práce, který činí blockchain pravděpodobnostně neměnným. Bloky musí dodržovat pravidla vynucovaná konsensem sítě, aby rozšířily blockchain. Když je blok připojen k blockchainu, zahrnuté transakce jsou považovány za první potvrzení.                                                                                                                                                                                                                                                                                                                  |
| Prohlížeč Bloků                                | Online nástroj, který umožňuje vyhledávat v reálném čase i historické informace o blockchainu, včetně dat souvisejících s bloky, transakcemi, adresami a dalším.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Block Hash                                     | Block hash je SHA-256 hash dat bloku a obvykle se reprezentuje v hexadecimálním formátu. Block hash lze interpretovat jako velmi velké číslo. Aby bylo splněno požadavky Proof-of-Work, musí být hash bloku nižší než určitý práh. Proto všechny hashe bloků začínají řadou nul následovaných alfanumerickým řetězcem. Některé bloky mají až dvacet vedoucích nul, zatímco starší bloky mají jen osm. Počet požadovaných nul přibližně ukazuje obtížnost těžby v době, kdy byl blok publikován.                                                                                                                                                                                                                                                                                                              |
| Block Height                                   | Každý blok je číslován vzestupně, začínaje nulou.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Block Reward                                   | Skládá se z dotace bloku (nově vytvořeného bitcoinu) a součtu všech transakčních poplatků z transakcí zahrnutých v bloku.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Block Size                                     | Každý blok má omezené množství dat, které do něj může být vloženo. Data, která se do určitého bloku nevešla, budou zaznamenána v jednom z následujících bloků. Pokud jde o bloky bitcoinu, dříve měly velikost bloku 1 MB, avšak po soft forku může velikost bloku technicky obsahovat až 4 MB dat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Block Subsidy                                  | Množství nově vytěženého bitcoinu v každém bloku. Každý vyrobený blok a přidaný do blockchainu umožňuje tvůrci bloku vytěžit určité množství nového bitcoinu. Dotace začala na 50 BTC za blok a každých 210 000 bloků, nebo přibližně každé 4 roky, se snižuje na polovinu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Blockchain                                     | Distribuovaný záznam, nebo databáze, všech transakcí Bitcoinu. Transakce jsou seskupeny do diskrétních aktualizací nazývaných bloky, omezené až na 4 miliony váhových jednotek. Bloky jsou produkované přibližně každých 10 minut prostřednictvím stochastického procesu nazývaného těžba. Každý blok zahrnuje výpočetně náročný "důkaz práce". Požadavek na důkaz práce slouží k regulaci intervalů bloků a ochraně blockchainu před útoky na přepisování historie: útočník by musel překonat stávající důkaz práce, aby nahradil již publikované bloky, čímž se každý blok stává s pravděpodobností neměnným, protože je pohřben pod následujícími bloky.                                                                                                                                                  |
| BTCPAY Server Vault                            | Pro optimální rovnováhu mezi jednoduchostí použití, bezpečností a soukromím se doporučuje používat BTCPay Server Wallet s hardware peněženkou. BTCPay Vault je postaven tak, aby propojil Hardware Wallet a BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Byzantine Generals' Problem                    | Problém teorie her, který popisuje obtíže decentralizovaných stran dosáhnout konsenzu bez spoléhání na důvěryhodnou centrální stranu. Název pochází ze scénáře několika generálů obléhajících Byzanc. Obklíčili město, ale musí kolektivně rozhodnout, kdy zaútočit. Pokud všichni generálové zaútočí současně, vyhrají, ale pokud zaútočí v různých časech, prohrají. Generálové nemají mezi sebou bezpečné komunikační kanály, protože jakékoli zprávy, které posílají nebo přijímají, mohly být zachyceny nebo podvodně odeslány obránci Byzance. Jak se mohou generálové organizovat, aby zaútočili ve stejný čas?                                                                                                                                                                                       |
| Censorship                                     | Kontrola nad tím, jaké informace mohou být přenášeny masám. Pokud jde o bitcoin, cenzura je o schopnosti zastavit transakci třetími stranami.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Change                                         | Část UTXOs vrácená do peněženky odesílatele, obvykle prostřednictvím jiné adresy. Činí součet vstupů mínus částka utracená a transakční poplatek.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Child Pays For Parent (CPFP)                   | Technika zvyšování poplatku, při které uživatel utratí výstup z nepotvrzené transakce s nízkým poplatkem ve dceřiné transakci s vysokým poplatkem, aby podnítil těžaře k zahrnutí obou transakcí do bloku.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Coinbase Transaction                           | První transakce v každém bloku, která rozděluje odměnu za blok a transakční poplatky tomu, kdo blok vytěžil.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Coincidence of Wants                           | Ekonomický jev, kdy obě strany drží předmět, který druhá strana chce, takže tyto předměty vymění přímo bez použití peněžního prostředku.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Cold Storage                                   | Způsob správy dat bez připojení k internetu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Cold Wallet                                    | Typ bitcoinové peněženky, která bezpečně ukládá vaše soukromé klíče offline, obvykle na fyzickém zařízení. Také známá jako hardware peněženka, chrání vaše digitální bitcoiny před online hackery pomocí zařízení podobného flash disku, které není připojeno k internetu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Command Line Interface (CLI)                   | Interakce s zařízením nebo počítačovým programem pomocí příkazů od uživatele nebo klienta a odpovědí od zařízení nebo programu ve formě řádků textu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Commitment Transaction                         | Commitment transakce je Bitcoinová transakce, podepsaná oběma partnery kanálu, která kóduje nejnovější zůstatek kanálu. Při každé nové platbě provedené nebo přeposlané pomocí kanálu se zůstatek kanálu aktualizuje a nová commitment transakce je podepsána oběma stranami. Důležité je, že v kanálu mezi Alicí a Bobem si oba Alice a Bob udržují vlastní verzi commitment transakce, která je také podepsána druhou stranou. Kanál může kdykoli uzavřít buď Alice nebo Bob, pokud předloží svou commitment transakci na Bitcoinový blockchain. Předložení starší (zastaralé) commitment transakce je považováno za podvod (tj. porušení protokolu) v Lightning Network a může být penalizováno druhou stranou, která si nárokuje všechny prostředky v kanálu pro sebe prostřednictvím penalty transakce. |
| Confirmation                                   | Jakmile je transakce zahrnuta do bloku, má jedno potvrzení. Jakmile je na blockchainu vytěžen další blok, transakce má dvě potvrzení, a tak dále. Šest nebo více potvrzení je považováno za dostatečný důkaz, že transakce nemůže být vrácena.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Crowdfund (CF)                                 | Výchozí plugin BTCPay Serveru, který majitelům obchodů umožňuje snadno vytvořit typickou crowdfundovou webovou stránku. Mohou snadno stanovit cíl, vytvořit odměny za příspěvky a přizpůsobit ji svým potřebám.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Cryptography                                   | Speciální systém, kde je původní zpráva změněna tak, aby ji mohli přijímat pouze zamýšlení příjemci.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Dashboard                                      | Centrální úvodní stránka BTCPay Serveru. Poskytuje přehled o veškeré aktivitě obchodu, zobrazený přes řadu shrnujících dlaždic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Demo                                           | Odkazuje na virtuální prostředí, ve kterém probíhají ukázky softwaru.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Deployment                                     | Nasazení softwaru zahrnuje veškeré aktivity, které software zpřístupňují pro použití. Obecný proces nasazení se skládá z několika vzájemně souvisejících aktivit s možnými přechody mezi nimi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Derivation Path                                | Kus dat, který říká Hierarchical Deterministic (HD) peněžence, jak odvodit konkrétní klíč v rámci stromu klíčů. Derivation paths se používají jako Bitcoinový standard a byly zavedeny s HD peněženkami jako součást BIP 32.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Difficulty Adjustment                          | Úprava obtížnosti cíle, každých 2016 bloků (přibližně každé dva týdny), aby se pokusila zajistit, že bloky jsou těženy jednou každých 10 minut v průměru. Tímto způsobem vytváří konzistentní čas mezi bloky a konzistentní vydávání nových bitcoinů do sítě (prostřednictvím odměny za blok).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Difficulty Target                              | Používá se při těžbě, je to číslo, které musí hash bloku být nižší, aby byl blok přidán do blockchainu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Digital Signature                              | Digitální podpis je matematický systém pro ověřování pravosti a integrity digitálních zpráv nebo dokumentů. Dá se považovat za kryptografické závazky, ve kterých zpráva není skryta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Divisible                                      | Vlastnost zboží, které lze rozdělit na menší části bez ztráty hodnoty. Protože ekonomické transakce často probíhají v různých částkách, musí být měna dělitelná, aby byla široce použitelná v ekonomice.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Docker                                         | Software, který balíčkuje software do standardizovaných jednotek nazývaných kontejnery, které obsahují vše, co software potřebuje k běhu, včetně knihoven, systémových nástrojů, kódu a runtime.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Double-Spend                                   | Výsledek úspěšného utracení nějakých peněz více než jednou. Bitcoin chrání proti dvojímu utrácení ověřením, že každá transakce přidaná do blockchainu dodržuje pravidla konsensu; to znamená kontrolu, že vstupy pro transakci nebyly dříve utraceny.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Durable                                        | Vlastnost peněz, při které měna může udržet svůj původní stav v průběhu času a vydržet opakované použití. Odolná měna musí být schopna přežít potenciální poškození.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Electrum                                       | Electrum je jedna z nejpopulárnějších Bitcoinových peněženek, vytvořená v roce 2011.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Extended public key (Xpub)                     | Rozšířený veřejný klíč, známý také jako Xpub, veřejný klíč, který funguje jako rodič pro klíče odvozené od xpub jako funkce HD peněženky. Tento Xpub je standard zavedený v BIP 32. Peněženky ho používají v zákulisí k odvození veřejných klíčů. Sdílení Xpub se nedoporučuje proti, vaše prostředky nebudou přímo vystaveny riziku pohybu, xpub nemůže odvodit soukromé klíče. Výhodou sdílení xpub může být pro účely crowdfundingu v BTCPay Server. Xpub je sdílen prostřednictvím online prostředků, zatímco soukromé klíče zůstávají offline na HWW.                                                                                                                                                                                                                                                   |
| F.U.D.                                         | Zkratka pro Fear, uncertainty and doubt (Strach, nejistota a pochybnosti); Obvykle vyvoláno úmyslně, aby se konkurent dostal do nevýhody.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Fee                                            | V kontextu Lightning Network budou uzly účtovat poplatky za směrování plateb ostatních uživatelů. Jednotlivé uzly mohou stanovit vlastní politiky poplatků, které budou vypočítány jako součet pevného base_fee a fee_rate, která závisí na výši platby. V kontextu Bitcoinu platí odesílatel transakce transakční poplatek těžařům za zařazení transakce do bloku. Bitcoinové transakční poplatky nezahrnují základní poplatek a závisí lineárně na váze transakce, ale ne na částce.                                                                                                                                                                                                                                                                                                                       |
| Fiat                                           | Měna vydaná vládou, která není kryta komoditou, jako je zlato.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Finite                                         | Odkazuje na omezené množství Bitcoinu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Fork                                           | Změna protokolu nebo kódu. Forky jsou obvykle zaváděny za účelem vylepšení projektu. Ve světě open source existují forky proto, že mnoho jednotlivců si stáhne a spustí stejný software v různých časech a ne vždy jej aktualizují. Pokud si dva uživatelé stáhnou a spustí verzi 1 softwaru a pouze jeden uživatel provede aktualizaci, když je vydána verze 2, uživatel, který aktualizoval, používá fork verze 1.                                                                                                                                                                                                                                                                                                                                                                                         |
| Funding Transaction                            | Transakce použitá k otevření platebního kanálu. Hodnota (v bitcoinech) funding transakce přesně odpovídá kapacitě platebního kanálu. Výstup z funding transakce je 2-of-2 multisignature skript (multisig), kde každý partner kanálu kontroluje jeden klíč. Díky své multisig povaze může být utracen pouze vzájemnou dohodou mezi partnery kanálu. Nakonec bude utracen jednou z commitment transakcí nebo závěrečnou transakcí.                                                                                                                                                                                                                                                                                                                                                                            |
| Fungible                                       | Být něčím (jako peníze nebo komodita) takové povahy, že jedna část nebo množství může být nahrazeno jinou rovnocennou částí nebo množstvím při placení dluhu nebo vyrovnání účtu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Gap Limit                                      | Odkazuje na standardní počet veřejných adres, které jsou kontrolovány pro transakce v blockchainu za účelem výpočtu zůstatku účtu. Transakce přijaté na adrese za limitem mezery nejsou detekovány.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Genesis Block                                  | První blok v Bitcoin blockchainu. Satoshi Nakamoto, tvůrce Bitcoinu, vytěžil Genesis blok 3. ledna 2009 a zahrnul do něj titulek z Financial Times toho dne, „Chancellor on brink of second bailout for banks.“ (Kancléř na pokraji druhého záchranného balíčku pro banky.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Github                                         | Platforma a cloudová služba pro vývoj softwaru a správu verzí pomocí Gitu, která umožňuje vývojářům ukládat a spravovat jejich kód.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Gossip Protocol                                | Uzly LN posílají a přijímají informace o topologii Lightning Network prostřednictvím gossip zpráv, které si vyměňují se svými partnery. Gossip protokol je hlavně definován v BOLT #7 a definuje formát zpráv node_announcement, channel_announcement a channel_update. Aby se zabránilo spamu, zprávy o oznámení uzlu budou přeposílány pouze v případě, že uzel již má kanál, a zprávy o oznámení kanálu budou přeposílány pouze v případě, že funding transakce kanálu byla potvrzena Bitcoinovou sítí. Obvykle se Lightning uzly spojují se svými partnery kanálu, ale je v pořádku spojit se s jakýmkoli jiným Lightning uzlem pro zpracování gossip zpráv.                                                                                                                                             |
| Gresham's Law                                  | Zákon, který říká, že „špatné peníze vytlačují dobré“. Jinými slovy, v ekonomice, kde jsou používány dvě měny, jednotlivci utratí špatné peníze, které se neustále znehodnocují, a budou držet dobré peníze, které si udržují svou hodnotu. Takto špatné peníze budou dominovat z hlediska oběhu a používání v každodenních transakcích, zatímco dobré peníze budou dominovat z hlediska úspor a dlouhodobých investic.                                                                                                                                                                                                                                                                                                                                                                                      |
| Halving                                        | Událost, která snižuje míru vydávání bitcoinu na polovinu každých 210 000 bloků (přibližně každé čtyři roky).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Hard Fork                                      | Změna konsensu, která není zpětně kompatibilní. Zpětná nekompatibilita nastává, když je dříve neplatné chování uznáno za platné. Aby bylo možné udržet konsensus přes hard fork, všechny uzly musí být aktualizovány. V opačném případě staré uzly odmítnou transakce nebo bloky jako neplatné podle starých pravidel, zatímco aktualizované uzly je přijmou jako platné. Z tohoto důvodu se v Bitcoinu vyhýbají hard forku za všech okolností.                                                                                                                                                                                                                                                                                                                                                              |
| Hardware Wallet (HWW)                          | Speciální typ Bitcoin peněženky, která uchovává soukromé klíče uživatele v bezpečném hardwarovém zařízení.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Hash Function                                  | Kryptografická hash funkce je matematický algoritmus, který mapuje data libovolné velikosti na bitový řetězec pevné velikosti (hash) a je navržen jako jednosměrná funkce, tj. funkce, kterou je nepraktické invertovat. Jediný způsob, jak získat vstupní data z výstupu ideální kryptografické hash funkce, je pokusit se o hrubou sílu hledání možných vstupů, aby se zjistilo, zda produkují shodu.                                                                                                                                                                                                                                                                                                                                                                                                      |
| Hash Rate                                      | Míra, jakou těžaři na síti Bitcoinu kumulativně produkují hashe za sekundu. Jeden hash je pokus o vytvoření Důkazu práce pro blok.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Hot Wallet                                     | Zařízení s vnějšími připojeními, zejména k internetu. Hot wallet je Bitcoin peněženka, která se připojuje k internetu. Tyto peněženky jsou pohodlnější pro každodenní výdaje, ale nejsou tak bezpečné jako možnosti studeného uložení, protože interagují s internetem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Initial Block Download (IBD)                   | Proces sestavování celého blockchainu Bitcoinu od začátku. Když je nový uzel nastaven a připojí se k síti, spojí se s ostatními uzly a žádá je o bloky. Nový uzel zpracovává tyto bloky a buduje blockchain, dokud není aktuální a synchronizovaný se sítí.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Invoice                                        | Obchodní dokument vystavený prodávajícím kupujícímu v souvislosti s prodejní transakcí a označující produkty, množství a dohodnuté ceny za produkty nebo služby, které prodávající poskytl kupujícímu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Know Your Customer (KYC)                       | Zákony zaměřené na prevenci používání finančních institucí pro nelegální převody peněz tím, že požadují, aby všechny finanční účty byly identifikovatelné k jednotlivcům nebo organizacím.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Layer 2                                        | Síť postavená na vrcholu blockchainu, např., Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Legacy Address                                 | Legacy adresy používají Base58 a když je legacy adresa hashem veřejného klíče, tzv. P2PKH adresa, začíná ‘1’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Lightning Network                              | Protokol na vrcholu Bitcoinu. Vytváří síť platebních kanálů, které umožňují bezdůvěrné předávání plateb sítí s pomocí HTLC a onion routing. Dalšími komponentami Lightning Network jsou gossip protokol, transportní vrstva a platební požadavky.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Liquidity                                      | Míra několika vlastností objednávkové knihy konkrétního aktiva na daném trhu. Likvidita je indikátorem toho, jak velký dopad na cenu aktiva bude mít velká objednávka. Aktivum s vyšší likviditou má hlubší hloubku objednávkové knihy. To znamená, že bude schopno absorbovat více objednávek s menšími cenovými pohyby.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Nejdelší řetězec                               | Řetězec bloků, jehož vytvoření vyžadovalo nejvíce úsilí. Je tak pojmenován, protože intuitivně blockchain obsahující více bloků vyžadoval k jeho vytvoření více energie než řetězec s menším počtem bloků, ale přesněji jde o řetězec, jehož vytvoření vyžadovalo více práce, takže přesnější název by mohl být "nejtěžší řetězec".                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Hlavní řetězec                                 | V kontextu Lightning Network se tímto myslí Bitcoinová síť.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Prostředek směny                               | Typ zboží, které usnadňuje výměnu jiných zboží a služeb v ekonomice. Historicky byly jako prostředek směny používány předměty jako mušle, korálky a zlato.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Mempool                                        | Zkratka pro "memory pool", jedná se o dočasné úložiště pro transakce, které byly přijaty uzlem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Těžař                                          | Uzel zapojený do procesu budování blockchainu přidáváním nových bloků prostřednictvím hašování.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Těžba                                          | Proces konstrukce bloku z nedávných Bitcoinových transakcí a poté řešení výpočetního problému vyžadovaného jako důkaz práce. Je to proces, kterým se aktualizuje sdílený bitcoinový záznam (tj. Bitcoinový blockchain) a jsou do něj začleněny nové transakce. Je to také proces, při kterém je vydáván nový bitcoin. Pokaždé, když je vytvořen nový blok, těžební uzel obdrží nový bitcoin vytvořený v rámci coinbase transakce tohoto bloku.                                                                                                                                                                                                                                                                                                                                                               |
| Vícepodepisová adresa (multisig)               | Skript, který vyžaduje více než jeden podpis k autorizaci výdaje. Platební kanály jsou vždy zakódovány jako multisig adresy vyžadující jeden podpis od každého partnera platebního kanálu. Ve standardním případě dvoustranného platebního kanálu se používá multisig adresa 2 z 2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Uzel                                           | Počítač účastnící se sítě. Konkrétně Bitcoinové nebo Lightning sítě.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Výstup                                         | Balíček bitcoinů vytvořený v bitcoinové transakci.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Zámek výstupu                                  | Sada požadavků kladených na výstup. Tyto požadavky musí být splněny, aby bylo možné výstup použít v transakci. Nejběžnějším příkladem je jednoduchý požadavek mít soukromý klíč.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| P2SH adresa                                    | P2SH adresy jsou Base58Check kódování 20bytového hash skriptu. P2SH adresy začínají "3". P2SH adresy skrývají veškerou složitost, takže odesílatel platby nevidí skript.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| P2WPKH adresa                                  | Formát adresy "native SegWit v0", P2WPKH adresy jsou zakódovány bech32 a začínají "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| P2WSH adresa                                   | Formát adresy skriptu "native SegWit v0", P2WSH adresy jsou zakódovány bech32 a začínají "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Částečně podepsaná Bitcoinová transakce (PSBT) | Bitcoinový standard, který usnadňuje přenositelnost nepodepsaných transakcí, což umožňuje více stranám snadno podepsat stejnou transakci. Je to nejužitečnější, když více stran chce přidat vstupy do stejné transakce. PSBT byl představen BIP 174 a umožňuje uživatelům snadněji podepisovat transakce na zařízení pro studené uchovávání a poté vysílat podepsanou transakci z zařízení připojeného k internetu.                                                                                                                                                                                                                                                                                                                                                                                          |
| Hledání cesty                                  | Proces nalezení cesty pro platbu od zdroje k cíli v Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Pay-to-Public-Key-Hash (P2PKH)                 | P2PKH je typ výstupu, který uzamkne bitcoin na hash veřejného klíče. Výstup uzamčený skriptem P2PKH lze odemknout (utratit) předložením veřejného klíče odpovídajícího hashi a digitálního podpisu vytvořeného odpovídajícím soukromým klíčem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Pay-to-Script-Hash (P2SH)                      | P2SH je univerzální typ výstupu, který umožňuje použití složitých Bitcoin skriptů. U P2SH složitý skript, který detailně určuje podmínky pro utracení výstupu (redeem script), není prezentován v uzamykacím skriptu. Místo toho je hodnota uzamčena na hash skriptu, který musí být prezentován a splněn, aby bylo možné výstup utratit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Pay-to-Taproot (P2TR)                          | Aktivovaný v listopadu 2021, Taproot je nový typ výstupu, který uzamkne bitcoin na strom podmínek utracení, nebo na jednu kořenovou podmínku.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Pay-to-Witness-Public-Key-Hash (P2WPKH)        | P2WPKH je ekvivalent P2PKH v SegWit, používající odděleného svědka (segregated witness). Podpis pro utracení výstupu P2WPKH je umístěn ve stromu svědků místo pole ScriptSig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Pay-to-Witness-Script-Hash (P2WSH)             | P2WSH je ekvivalent P2SH v SegWit, používající odděleného svědka. Podpis a skript pro utracení výstupu P2WSH je umístěn ve stromu svědků místo pole ScriptSig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Payjoin                                        | Speciální typ Bitcoin transakce, kde jak odesílatel, tak příjemce přispívají vstupy za účelem narušení heuristiky společného vlastnictví vstupů, předpokladu používaného k odhalení soukromí uživatelů bitcoinu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Platební kanál                                 | Finanční vztah mezi dvěma uzly na Lightning Network, vytvořený pomocí bitcoinové transakce platící na multisignaturní adresu. Partneři kanálu mohou kanál používat k posílání bitcoinů tam a zpět mezi sebou bez nutnosti zaznamenávat všechny transakce do blockchainu Bitcoinu. V typickém platebním kanálu jsou do blockchainu přidány pouze dvě transakce, finanční transakce a transakce závazku. Platby poslané přes kanál nejsou zaznamenány v blockchainu a říká se, že probíhají "mimo řetězec".                                                                                                                                                                                                                                                                                                    |
| Požadavek na platbu                            | Funkce, která umožňuje majitelům obchodů BTCPay vytvářet dlouhodobé faktury. Fondy zaplacené na požadavek na platbu používají směnný kurz v době platby. To umožňuje uživatelům provádět platby podle svého výběru bez nutnosti dohadovat nebo ověřovat směnné kurzy s majitelem obchodu v době platby.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Výplata                                        | Funkcionalita výplaty je spojena s Pull Payments. Tato funkce umožňuje zpracování pull platby (refundace, výplaty platu nebo výběry).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Plugin                                         | Softwarový doplněk, který je nainstalován do programu, rozšiřující jeho možnosti.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Bod prodeje (PoS)                              | Výchozí plugin BTCPay Serveru umožňující majiteli obchodu vytvořit webshop přímo z BTCPay Serveru. Majitel obchodu nepotřebuje žádná třetí strana e-commerce řešení k provozování webshopu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Přenosný                                       | Schopnost zboží být snadno přepravováno napříč prostorem. Přenosnost je důležitou vlastností zvukových peněz; aby mohla být měna široce přijata a tedy použitelná, musí být schopna snadno překračovat hranice, přecházet mezi jednotlivci a na dlouhé vzdálenosti.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Proof Of Work (PoW)                            | Data, která vyžadují významný výpočetní výkon k nalezení, a která může kdokoli snadno ověřit, aby prokázal množství práce, které bylo potřebné k jejich vytvoření. V Bitcoinu musí těžaři najít číselné řešení algoritmu SHA-256, které splňuje celosíťový cíl, nazývaný cíl obtížnosti.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Pseudonym                                      | Falešné jméno používané jednotlivci k ochraně jejich identity nebo k budování reputace oddělené od jejich skutečné identity. Veřejné klíče se používají, aby uživatelé Bitcoinu mohli přijímat bitcoiny, zatímco zůstávají pseudonymní vůči blockchainu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Public-Key Cryptography                        | Zahrnuje dvojici klíčů známých jako veřejný klíč a soukromý klíč, které jsou spojeny s entitou, která potřebuje elektronicky ověřit svou identitu nebo podepsat či šifrovat data. Veřejný klíč je zveřejněn a odpovídající soukromý klíč je udržován v tajnosti. Data, která jsou šifrována veřejným klíčem, lze dešifrovat pouze odpovídajícím soukromým klíčem.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Veřejný/Soukromý Klíč                          | Pár klíčů používaný v kryptografii s veřejným klíčem. Veřejný klíč je sdílen s ostatními veřejně a lze jej chápat jako číslo účtu, zatímco soukromý klíč je udržován v tajnosti a lze jej chápat jako heslo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Pull Payment                                   | Tradičně, aby byla provedena platba v Bitcoinu, příjemce sdílí svou bitcoinovou adresu a odesílatel později pošle peníze na tuto adresu. Takový systém se nazývá push platba, protože platbu iniciuje odesílatel, zatímco příjemce může být nedostupný, čímž efektivně "tlačí" platbu příjemci. Na rozdíl od typického scénáře, kdy odesílatel "tlačí" platbu, odesílatel umožní příjemci vytáhnout platbu ve chvíli, kterou považuje za vhodnou.                                                                                                                                                                                                                                                                                                                                                            |
| Králičí Nora                                   | Odkaz na Alenku v říši divů, kde hrdina začíná dobrodružství vstupem do králičí nory. V Bitcoinu se tím myslí zdánlivě nekonečná témata, která člověk prozkoumává a vidí v novém světle, jakmile začne Bitcoinu rozumět.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Přijmout                                       | Proces, kdy jsou bitcoiny poslány na poskytnutou adresu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Registrace                                     | Proces vytvoření účtu nebo přihlášení k službě, obvykle výběrem uživatelského jména a hesla.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Replace By Fee (RBF)                           | Bitcoinová transakce může být označena jako RBF, aby odesílatel mohl tuto transakci nahradit jinou podobnou transakcí, která platí vyšší poplatek. Tento mechanismus existuje, aby uživatelé mohli reagovat, pokud se síť stane přetíženou a poplatky neočekávaně vzrostou.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Repository                                     | Ve verzovacích systémech je repozitář datová struktura, která ukládá metadata pro sadu souborů nebo strukturu adresářů.[1] V závislosti na tom, zda je použitý verzovací systém distribuovaný, jako je Git nebo Mercurial, nebo centralizovaný, jako je Subversion, CVS nebo Perforce, může být celá sada informací v repozitáři duplikována na systému každého uživatele nebo udržována na jednom serveru.[2] Mezi metadata, která repozitář obsahuje, patří mimo jiné historický záznam změn v repozitáři, sada objektů commitu a sada odkazů na objekty commitu, nazývaných hlavy.                                                                                                                                                                                                                        |
| Rescan                                         | Proces skenování aktuálního stavu sady UTXO pro mince patřící k dříve nakonfigurovanému schématu derivace.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Revokation Key                                 | Každá Revocable Sequence Maturity Contract (RSMC) obsahuje dva klíče pro zrušení. Každý partner kanálu zná jeden klíč pro zrušení. Znát oba klíče pro zrušení umožňuje utratit výstup RSMC v rámci předem definovaného časového zámku. Při vyjednávání nového stavu kanálu jsou sdíleny staré klíče pro zrušení, čímž dochází k "zrušení" starého stavu. Klíče pro zrušení se používají k odrazení partnerů kanálu od vysílání starého stavu kanálu.                                                                                                                                                                                                                                                                                                                                                         |
| Routing                                        | Proces použití cesty Lightning Network k provedení platby.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Routing Fees                                   | V Lightning Network poplatky účtované za přeposílání plateb ostatních uživatelů. Jednotlivé uzly si mohou stanovit vlastní politiky poplatků, které budou vypočítány jako součet pevného base_fee a fee_rate, který závisí na částce platby.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Salability                                     | Snadnost, s jakou lze zboží prodat na trhu kdykoli to jeho držitel požaduje, s nejmenší ztrátou jeho ceny.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Satoshi (sat)                                  | Satoshi je nejmenší jednotka (nominální hodnota) bitcoinu, která může být zaznamenána na blockchainu. Jedno satoshi je 1/100 miliontina (0,00000001) bitcoinu a je pojmenováno po tvůrci Bitcoinu, Satoshi Nakamotovi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Satoshi Nakamoto                               | Jméno používané osobou nebo skupinou lidí, kteří navrhli Bitcoin a vytvořili jeho původní referenční implementaci. Jako součást implementace také navrhli první blockchainovou databázi. V procesu byli první, kdo vyřešil problém dvojitého utrácení u digitální měny. Jejich skutečná identita zůstává neznámá.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Satoshi Per Byte                               | Jednotka pro měření priority transakce, definovaná jako poplatek za transakci v satoshi dělený velikostí transakce v bytech.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Satoshi Per Verabyte                           | Podobný koncept jako Satoshi Per Byte, ale pro novější adresy používající Segwit. Rovná se velikosti transakce ve váhových jednotkách dělené čtyřmi. Váhové jednotky se vypočítávají vynásobením velikosti transakce (bez svědka) třikrát, přičemž se přidá velikost transakce včetně svědka.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Scarcity                                       | Vlastnost zboží, které nelze bez nákladů replikovat. Nedostatek není závislý na počtu existujících jednotek zboží, ale spíše na nákladnosti výroby dalších jednotek.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Script                                         | Bitcoin používá pro transakce skriptovací systém nazvaný Bitcoin Script. Podobá se programovacímu jazyku Forth, je jednoduchý, založený na zásobníku a zpracovává se zleva doprava. Je záměrně Turing-neúplný, bez smyček nebo rekurze.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Seed Phrase                                    | Seznam slov, který uchovává veškeré informace potřebné k obnovení bitcoinových prostředků na řetězci. Softwarové peněženky obvykle generují frázi seed a instruují uživatele, aby si ji napsal na papír. Pokud uživatelův počítač selže nebo se poškodí jeho pevný disk, může si znovu stáhnout stejný softwarový peněženku a pomocí papírové zálohy získat své bitcoiny zpět.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Segregated Witness (SegWit)                    | Segregated Witness (SegWit) je aktualizace protokolu Bitcoinu zavedená v roce 2017, která přidává nové svědectví pro podpisy a další důkazy o autorizaci transakce. Toto nové pole svědka je vyjmuté z výpočtu ID transakce, což řeší většinu tříd manipulace s transakcemi třetími stranami. Segregated Witness byl nasazen jako soft fork a je to změna, která technicky činí pravidla protokolu Bitcoinu restriktivnějšími.                                                                                                                                                                                                                                                                                                                                                                               |
| Self-Sovereignty                               | Model pro správu digitálních identit, ve kterém jednotlivci nebo firmy mají jedinou vlastnictví nad schopností kontrolovat své účty a osobní data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Send                                           | Proces přesunutí bitcoinu na adresu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Sensitivity Mode                               | Aktivováno přepínačem v nastavení obchodu, aktivace způsobí, že číselné hodnoty (např. množství bitcoinu) budou všude zakryty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Server Settings                                | Nastavení v BTCPay Serveru, které se vztahuje na celý server (na rozdíl od nastavení obchodu, které je omezeno na jednotlivý obchod).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SHA-256                                        | Kryptografická hašovací funkce. Člen rodiny hašovacích funkcí nazývaných Secure Hashing Algorithm (SHA) funkce.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Shopify                                        | Kanadská nadnárodní e-commerce společnost se sídlem v Ottawě, Ontario. Shopify je název její vlastní e-commerce platformy pro online obchody a maloobchodní prodejní systémy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SMTP                                           | Simple Mail Transfer Protocol je internetový standardní komunikační protokol pro přenos elektronické pošty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Soft Fork                                      | Aktualizace protokolu, která je kompatibilní jak vpřed, tak vzad, takže umožňuje pokračovat v používání stejného řetězce jak starým, tak novým uzlům.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Software Stack                                 | V informatice je sada softwarových subsystémů nebo komponent potřebných k vytvoření kompletní platformy tak, aby nebyl k podpoře aplikací potřeba žádný další software.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Store                                          | Obchod v rámci BTCPay Serveru lze chápat jako "Domov" pro konkrétní bitcoinovou peněženku, rozšířený o všechny funkce BTCPay Serveru.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Store Settings                                 | Nastavení v BTCPay Serveru specifické pro obchod.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Taproot                                        | Aktualizace Bitcoinu, která by představila několik nových funkcí. Aktualizace je popsána v BIPs 340, 341 a 342 a zavádí schéma podpisu Schnorr, Taproot a Tapscript. Společně tyto aktualizace představují nové, efektivnější, flexibilnější a soukromější způsoby převodu bitcoinu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Thier's Law                                    | Zákon, který tvrdí, že dobré peníze vytlačí špatné peníze.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Third-Party Host                               | Když je webová stránka jednotlivce nebo společnosti provozována na serverech vlastněných a spravovaných jinou firmou. Alternativou je mít vaši webovou stránku hostovanou na vašich serverech ve vašem vlastním datovém centru.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Timelock                                       | Timelock je typ závazku, který omezuje možnost utrácení některých bitcoinů do určeného budoucího času nebo výšky bloku. Timelocky se výrazně objevují v mnoha Bitcoinových smlouvách, včetně platebních kanálů a HTLCs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Topologie                                      | Topologie Lightning Network popisuje tvar Lightning Network jako matematický graf. Uzly grafu jsá uzly Lightning (účastníci sítě/peers). Hrany grafu jsou platební kanály. Topologie Lightning Network je veřejně vysílána s pomocí gossip protokolu, s výjimkou neohlášených kanálů. To znamená, že Lightning Network může být výrazně větší než je ohlášený počet kanálů a uzlů. Znát topologii je zvláště zajímavé v procesu směrování plateb založeném na zdroji, kdy odesílatel objevuje trasu.                                                                                                                                                                                                                                                                                                         |
| Transakce                                      | Transakce jsou datové struktury používané Bitcoinem pro převod bitcoinů z jedné adresy na druhou. Několik tisíc transakcí je agregováno do bloku, který je poté zaznamenán (těžen) na blockchainu. První transakce v každém bloku, nazývaná coinbase transakce, generuje nové bitcoiny.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ID transakce                                   | Řetězec písmen a čísel, který identifikuje konkrétní transakci na blockchainu. Řetězec je jednoduše dvojitý SHA-256 hash transakce. Tento hash lze použít k vyhledání transakce na uzlu nebo block exploreru.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Dvoufaktorové ověření (2FA)                    | Metoda zabezpečení správy identity a přístupu, která vyžaduje dvě formy identifikace pro přístup k prostředkům a datům, často s použitím sekundárního zařízení kromě standardního přihlašovacího hesla.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Necenzurovatelnost                             | Vlastnost, že žádná entita nemá schopnost vrátit zpět Bitcoin transakci nebo zařadit na černou listinu peněženku nebo adresu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Nezabavitelnost                                | Vlastnost, že žádná entita nemůže vzít bitcoiny od entity proti její vůli.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Nevyužité výstupy transakcí (UTXO)             | Výstupy ještě nevyužité, tedy dostupné k použití v nových transakcích.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Uživatelská zkušenost (UX)                     | Jak uživatel interaguje a prožívá produkt, systém nebo službu. Zahrnuje vnímání uživatele o užitečnosti, jednoduchosti použití a efektivitě.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Uživatelské rozhraní (UI)                      | Bod interakce a komunikace mezi člověkem a počítačem v zařízení.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Ověřitelnost                                   | Vlastnost zboží, které lze snadno odlišit od napodobenin a padělků.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Virtuální                                      | Existující na počítači nebo počítačové síti nebo simulované na nich.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Virtuální stroj (VM)                           | V informatice je virtuální stroj virtualizace nebo emulace počítačového systému. Virtuální stroje jsou založeny na počítačových architekturách a poskytují funkčnost fyzického počítače. Jejich implementace může zahrnovat specializovaný hardware, software, nebo kombinaci obou.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Virtuální soukromý server                      | Virtuální soukromý server je virtuální stroj prodávaný jako služba internetovým hostingovým službám. Termín "virtuální dedikovaný server" má podobný význam. Virtuální soukromý server běží na vlastní kopii operačního systému a zákazníci mohou mít úroveň přístupu superuživatele k této instanci operačního systému, takže mohou instalovat téměř jakýkoliv software, který na tomto OS běží.                                                                                                                                                                                                                                                                                                                                                                                                            |
| Volatilita                                     | Míra stupně variace ceny aktiva v čase. Aktiva, která pravidelně zažívají velké změny ceny, jsou volatilnější, zatímco aktiva s stabilnější cenou jsou méně volatilní.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Peněženka                                      | Bitcoinové peněženky uchovávají klíče uživatele, což umožňuje uživatelům přijímat bitcoiny, podepisovat transakce a kontrolovat zůstatek na účtu. Soukromé a veřejné klíče v bitcoinové peněžence plní dvě odlišné funkce, ale jsou spolu spojeny již při vytváření. Bitcoinové peněženky obsahují klíče uživatele, nikoli jejich skutečné bitcoiny. Konceptuálně je peněženka podobná klíčence v tom smyslu, že obsahuje mnoho párů soukromých a veřejných klíčů. Tyto klíče se používají k podepisování transakcí, což umožňuje uživateli prokázat, že vlastní výstupy transakcí na blockchainu, tj. jejich bitcoiny. Všechny bitcoiny jsou zaznamenány na blockchainu ve formě výstupů transakcí.                                                                                                         |
| Wasabi Peněženka                               | Otevřený zdrojový, nevlastnický, soukromí zaměřený Bitcoinový software pro Desktop, který implementuje CoinJoin bez důvěry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Pouze pro sledování Peněženka                  | Bitcoinové peněženky, které vám umožňují sledovat vaše bitcoiny v chladném úložišti, zatímco zakazují možnost utrácet prostředky. To je proto, že peněženky pouze pro sledování neuchovávají ani nepoužívají soukromé klíče a proto nemohou autorizovat žádné výdaje jménem uživatele.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Velryba                                        | V kontextu Bitcoinu je velryba někdo, kdo drží velké množství bitcoinů.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| White-Label                                    | Produkt White-Label je produkt nebo služba vyrobená jednou společností, kterou ostatní společnosti přeznačují, aby to vypadalo, jako by ji vyrobily ony.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Whitepaper                                     | Představuje nový nápad nebo téma k diskusi. Bitcoinový whitepaper představil Bitcoin jako „Peer-to-peer elektronický platební systém“, který „nevyžaduje důvěryhodné třetí strany“. Satoshi Nakamoto vydal whitepaper 31. října 2008 na emailovou listu kryptografů a cypherpunků.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Wrapped Segwit                                 | Implementace designu zahrnutá v aktualizaci SegWit, která měla umožnit peněženkám a dalšímu softwaru pro Bitcoin snadněji podporovat SegWit. Aby se toho dosáhlo, dvě původní skripty SegWit, P2WPKH a P2WSH, se používají jako „redeemScript“ transakce P2SH, což vede k obaleným typům skriptů SegWit P2SH-P2WPKH a P2SH-P2WSH.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

![obrázek](assets/en/129.webp)
