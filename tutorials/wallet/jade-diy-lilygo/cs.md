---
name: Jade DIY
description: Přeměna vývojové desky za 15 dolarů na plně funkční hardware Bitcoin wallet
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - začátečnická konstrukce


**Posluchači:** Zvídaví stavitelé s malými nebo žádnými zkušenostmi s embedded.


**Trvání:** 2 hodiny (flexibilní)


**Výstupy:** Na konci kurzu studenti:



- Rozpoznejte bezpečnostní model hardwarových peněženek typu "udělej si sám" ve srovnání s komerčními zařízeními.
- Sestavte podpisové zařízení založené na mikrokontroléru.
- Flashujte firmware s otevřeným zdrojovým kódem a ověřte kontrolní součet sestavení.
- Podepište a odvysílejte transakci mainnet pomocí svého nového zařízení.


---

## Abstrakt


Tento dvouhodinový workshop naučí začátečníky sestavit funkční hardware Bitcoin wallet pomocí flashování open-source firmwaru Jade na desku LilyGO T-Display za 15 dolarů. Studenti přemění obecný vývojový hardware na podpisové zařízení srovnatelné s komerčními peněženkami za 150 dolarů a naučí se základy zabezpečení spíše praktickými zkušenostmi než pouhou teorií.


### Filozofie


Sestavení vlastního podepisovacího zařízení není jen o úspoře peněz - je to o pochopení technologie, která chrání váš Bitcoin. Tento seminář podporuje "bezpečnost prostřednictvím porozumění" a ne důvěryhodnost černé skříňky. Tím, že si studenti obstarají komponenty, flashují open-source firmware a sami generují entropii, snižují riziko dodavatelského řetězce a zároveň se učí kriticky hodnotit bezpečnostní nároky. Cílem je informovaná samostatnost: studenti by měli pochopit jak sílu, tak omezení svého DIY zařízení ve srovnání se zabezpečenými komerčními alternativami.


---

## Základní koncepce (15 min)


### Co je to vlastní opatrovnictví a proč na něm záleží?


Bitcoin byla vytvořena s cílem odstranit z našeho peněžního systému potřebu důvěryhodných třetích stran, jako jsou banky a korporace. Místo důvěryhodnosti využívá bitcoin matematiku, fyziku a kryptografii, aby umožnil komukoli vlastnit a ovládat své peníze, aniž by k tomu potřeboval něčí svolení.


Funguje to tak, že bitcoin existuje v globální digitální účetní knize zvané blockchain alias bitcoin timechain, což je veřejná a transparentní účetní kniha vedená počítači namísto centralizované účetní knihy, jako je bankovní účet.


Důležité je pochopit, že pro přesun bitcoinů z jednoho místa na druhé musíte transakci podepsat takzvaným soukromým klíčem. Představte si to jako odemknutí trezoru pomocí hesla a přesun bitcoinů do trezoru někoho jiného. Bitcoin vám dává moc držet klíče od tohoto trezoru sami, místo abyste se spoléhali na banku, že za vás vaše peníze přesune.


S velkou mocí přichází i velká zodpovědnost, ztratíte-li klíče, jsou vaše prostředky navždy pryč. Klíče od trezoru si tak můžete představit jako samotné peníze. Klíče sice nejsou totéž co bitcoiny, ale představují mechanismus pro přesun vašich finančních prostředků, a proto je nesmírně důležité je chránit. Proto říkáme "ne vaše klíče, ne vaše mince".


Termín self-custody může znít matoucím způsobem, ale znamená pouze to, že vlastníte vlastní soukromé klíče a máte kontrolu nad vlastními bitcoiny. Pokud tento klíč nedržíte, svěřujete ho někomu jinému, aby ho držel za vás. Pokud jsou vaše bitcoiny v ETF nebo na burze (Mt. Gox, FTX, Coinbase, Binance atd.), nevlastníte bitcoin, ale nárok na bitcoin. To s sebou přináší nejrůznější rizika, jako je hacknutí burzy a ztráta vašich bitcoinů nebo společnosti, které vaše peníze půjčují a dávají vám jen zlomek do rezervy. Důvěryhodné třetí strany by navíc měly plnou kontrolu nad vašimi penězi a mohly by omezit nebo zmrazit výběry.


![image](assets/fr/01.webp)


S péčí o vlastní osobu se zbavíte důvěry. Nikdo vám nemůže zmrazit peníze nebo odmítnout transakci, můžete posílat peníze přes hranice, komukoli a kdykoli a nepotřebujete bankovní účet, průkaz totožnosti ani ničí souhlas. Nikdo vás nemůže zastavit, cenzurovat ani okrást, což odemyká plnou sílu bitcoinu jako svobodných peněz. Proto říkáme, že s bitcoinem můžete být svou vlastní bankou.


Bitcoin byla vytvořena jako řešení problému manipulace s důvěrou a penězi, jako východisko z našeho současného systému, ale východisko funguje pouze tehdy, když si vezmete klíče. Proto je tak důležitá vlastní úschova.


### Co je Wallet?


Termín wallet je poněkud zavádějící, a proto může být matoucí. Ano, je pravda, že bitcoin wallet, stejně jako fyzický wallet, uchovává hodnotu. Hlavní rozdíl však spočívá v tom, že bitcoinové peněženky ve skutečnosti žádné bitcoiny neukládají.


Bitcoin existuje pouze jako záznam v účetní knize ve veřejném blockchainu nebo v metaforických trezorech v kyberprostoru. Nezapomeňte, že k přesunu bitcoinů musíte použít své klíče k odemknutí trezoru a přesunout mince někam jinam, soukromé klíče jsou to, co se používá k utrácení bitcoinů. Když provádíte transakci pomocí wallet, ve skutečnosti používáte své klíče pouze k podpisu transakce. Tímto způsobem prokazujete, že jste vlastníkem peněz a máte právo tyto mince utratit.


Peněženky Bitcoin ve skutečnosti pouze uchovávají vaše soukromé klíče, takže by bylo přesnější říkat jim klíčenky.


### Peněženky Hot vs Cold


Hot wallet je softwarová aplikace v telefonu nebo počítači. Je připojena k internetu, takže se snadněji používá a rychleji podepisuje transakce, ale to také znamená, že je více vystavena hackerům, malwaru a phishingu. Nazývá se "horký", protože je připojen k internetu, je zapojen a zapnut. Příkladem může být telefon wallet nebo prohlížeč wallet.


Naproti tomu studený klíč wallet neboli hardwarový klíč wallet je zařízení, které vytváří a ukládá klíč offline. Tím se odstraní možnost, aby se někdo naboural do vašich prostředků, a je mnohem bezpečnější pro dlouhodobé spoření, nicméně jde o zařízení, které je potřeba podepsat při každé transakci, a může být méně pohodlné.


### Model ohrožení Hardware Wallet


Hardwarové peněženky řeší zásadní problém: jak podepisovat transakce Bitcoin, aniž byste vystavili své soukromé klíče počítači připojenému k internetu, který by mohl být napaden malwarem nebo vzdálenými útočníky? Základní model hrozeb předpokládá, že váš každodenní notebook nebo telefon je potenciálně nepřátelský. Hardwarový wallet vytváří izolované prostředí, kde soukromé klíče nikdy neopustí zařízení a podepisování transakcí probíhá v secure element nebo mikrokontroléru, který zpět do hostitelského počítače předává pouze podpis, nikoliv samotný klíč. I když je váš počítač zcela kompromitován, útočník nemůže ukrást váš Bitcoin bez fyzického přístupu k zařízení a kódu PIN.


Hardwarové peněženky však přinášejí vlastní hrozby. Musíte věřit, že výrobce nezavedl zadní vrátka, že dodavatelský řetězec nebyl narušen a že generování náhodných čísel je skutečně náhodné. Fyzičtí útočníci mohou získat klíče pomocí útoků postranními kanály nebo manipulací s čipem a někdo s dočasným přístupem může vaše zařízení upravit. Sestavení vlastního hardwaru wallet vám pomůže pochopit tyto kompromisy - budete se rozhodovat o bezpečných prvcích oproti univerzálním mikrokontrolérům, o tom, jak ověřovat transakce na displeji a jak se chránit před vzdálenými i fyzickými hrozbami. Cílem není dokonalé zabezpečení, ale pochopení, proti kterým hrozbám se chráníte a které zůstávají.


### Klíčové pojmy



- Entropie a věty seed:** Váš wallet je tak bezpečný, jak bezpečná je náhoda, která ho zrodila. Smícháme generátor náhodných čísel zařízení s lidsky přívětivými triky, jako jsou hody kostkou, převedeme tuto entropii na 12- nebo 24-slovnou [BIP39 frázi](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) a opustíme místnost s písemnou nebo kovovou zálohou, které důvěřujete.
- Hygiena slovního spojení:** S číslem seed zacházejte jako s hlavními klíči od svých úspor. Nikdy je nezadávejte do telefonu nebo počítače - keyloggery, screenshoty a cloudové zálohy je mohou navždy vyzradit. Frázi mějte offline, uložte ji na místo, ke kterému máte přístup jen vy, a před odchodem si ji nacvičte přečíst nahlas.
- Zabezpečený prvek + mikrokontrolér:** Představte si secure element jako trezor a mikrokontrolér jako mozek. Prvek secure element střeží soukromé klíče s odolností proti neoprávněné manipulaci, zatímco mikrokontrolér se stará o obrazovku, tlačítka a logiku firmwaru. Všimněte si, že hardwarové peněženky, které dnes stavíme, nemají secure element. To neznamená, že jsou nezabezpečené, jen mají o jednu úroveň ochrany méně.
- Důvěra ve firmware:** Firmware je neviditelný operační systém wallet. Vždy stahujte z označených verzí, zkontrolujte zveřejněný hash a uvědomte si, že reprodukovatelná sestavení umožňují více lidem zkompilovat stejný kód a dojít k naprosto stejné binární kopii. Pokud se kontrolní součet neshoduje, nepodepisujete.


---

## Co stavíme?


Používáme obecný hardware, LilyGo T-Display, a flashujeme na něm firmware Jade SDK. Jade Plus](https://blockstream.com/jade/jade-plus/) je open-source wallet, který obvykle stojí 150 dolarů:


![image](assets/fr/02.webp)


Dnes budeme místo toho flashovat jejich firmware na hardware za 15 dolarů.


### Co koupit


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB s pláštěm, model K164)** - [Objednat přímo u LilyGO](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) za cca 15 USD. Tato deska ESP32 poskytuje displej, tlačítka a rozhraní USB, které zrcadlí Jade Plus od společnosti Blockstream. Vestavěná deska ESP32 obsahuje také rádia Wi-Fi a Bluetooth; dodáme firmware, který je ponechá vypnuté, ale utváří váš model ohrožení, protože škodlivý kód by je mohl opět zapnout.
- Kabel USB-C** - Vezměte si kabel, který umožňuje přenos dat, abyste mohli flashovat firmware a napájet desku přímo z notebooku (pro použití ve třídě je naprosto v pořádku).


### Proč si postavit vlastní Hardware Wallet?



- Ušetříte zhruba 135 dolarů oproti nákupu komerčního zařízení.
- Vytvořte si pohodlí pomocí flashování firmwaru, bezpečných prvků a hygieny wallet.
- Roztočte další podepisovací zařízení a rozložte úspory do více peněženek.
- Snižte riziko dodavatelského řetězce tím, že si každý komponent obstaráte a sestavíte sami.
- Mějte na paměti Loppovu mantru: suverenita a pohodlí jsou vždy v rozporu.


## Fyzické nastavení


### Příprava případu


Pro umístění desky LilyGO T-Display máte dvě možnosti: pouzdro vytištěné na 3D tiskárně nebo oficiální kryt LilyGO. Tištěné pouzdro najdete a vytisknete na adrese [tento model](https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). Nabízí lehký a přizpůsobitelný obal pro vaše zařízení.


![image](assets/fr/04.webp)


Případně můžete použít oficiální pouzdro LilyGO, které má trochu jiný střih a povrchovou úpravu a nabízí robustnější ochranu a leštěný vzhled.


![image](assets/fr/05.webp)


Všimněte si, že tištěná a oficiální pouzdra se mírně liší konstrukcí a sestavením. Ať už zvolíte kteroukoli možnost, ujistěte se, že je deska v pouzdře správně usazena, aby nedošlo k uvolnění spojů nebo poškození.


### Kontrola desky


Než budete pokračovat, pečlivě zkontrolujte desku LilyGO T-Display, zda na ní nejsou viditelné závady nebo nečistoty. Zkontrolujte, zda jsou displej, tlačítka a port USB-C čisté a bez prachu nebo stříkanců pájky. S deskou zacházejte opatrně a dodržujte bezpečnost při elektrostatickém výboji (ESD) tím, že se uzemníte nebo použijete ESD pásek na zápěstí, abyste zabránili poškození citlivých součástek.


### Připojení k notebooku


Připojte desku LilyGO k notebooku pomocí kabelu USB-C podporujícího přenos dat. Toto připojení zajistí napájení a umožní flashování firmwaru.


Po spuštění se zobrazí následující obrazovka:


![image](assets/fr/06.webp)



Po zapnutí zobrazí zařízení LilyGO barevnou testovací obrazovku, na které se cyklicky střídají stálé barvy. Tím se před flashováním firmwaru potvrdí, že displej a deska fungují správně.


Po dokončení barevného testu se obrazovka nastaví do výchozího stavu, což znamená, že deska je připravena k dalším krokům v procesu sestavování.


![image](assets/fr/07.webp)


## Snadná cesta nebo cesta Hard


Existují dva hlavní přístupy k flashování firmwaru hardwaru wallet: jednoduchý a složitý způsob. Snadný způsob využívá předkonfigurované nástroje nebo webové flashery, které automaticky nahrají firmware do vašeho zařízení s minimálním vstupem. Tato metoda je ideální pro začátečníky, kteří chtějí mít rychle vyhráno nebo se raději vyhnou složitému ladění a interakcím s příkazovým řádkem. Zjednodušuje proces a umožňuje rychlejší zprovoznění, takže je přístupný i pro ty, kteří s vývojem vestavných zařízení nebo hardwarových peněženek začínají.


Naproti tomu složitější způsob zahrnuje ruční flashování firmwaru pomocí nástrojů příkazového řádku. Tento přístup vyžaduje ověření podpisů a kontrolních součtů firmwaru, aby byla zajištěna jeho pravost a integrita, což vám umožní lépe porozumět procesu flashování a interakci firmwaru s hardwarem. Vyžaduje sice větší úsilí a znalost terminálových příkazů, ale nabízí větší kontrolu, transparentnost a jistotu zabezpečení zařízení.


Každá z těchto metod má své kompromisy: snadný způsob obětoval určitou míru důvěry a porozumění ve prospěch rychlosti a pohodlí, zatímco složitý způsob vyžaduje více času a technických dovedností, ale odmění vás flexibilitou a lepším porozuměním základní technologii. Instruktoři by měli studenty povzbuzovat, aby si vybrali cestu, která nejlépe odpovídá jejich úrovni pohodlí a zvědavosti, a podporovat tak důvěru a zkoumání.


## Snadný způsob


Nejjednodušší způsob flashování ESP32



- Přejděte na oficiální Blockstream Github: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Zdrojový soubor si můžete stáhnout a spustit web lokálně, ale GitHub jej již hostuje na adrese [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub servíruje HTML, CSS, JavaScript atd. přímo do prohlížeče, takže můžete zařízení flashovat bez instalace vývojářských nástrojů.


![image](assets/fr/09.webp)



- Otevřete rozbalovací nabídku (pravděpodobně je výchozí hodnota `M5Stack Core2`) a vyberte vývojovou desku - pro tuto třídu vyberte `LILYGO T-Display`.


![image](assets/fr/10.webp)



- Po kliknutí na tlačítko flash se zobrazí toto. Abyste zjistili, které zařízení je LILYGO, odpojte zařízení lilygo a znovu jej zapojte. Objeví se com port, který lilygo a zmizí. Klikněte na port COM, ke kterému je připojeno zařízení Jade


![image](assets/fr/11.webp)



- To je vše, měl by se zobrazit ukazatel průběhu, a až bude dokončen, můžete jej nastavit


## Nastavení zařízení Jade Wallet


Po úspěšném flashnutí firmwaru je nyní váš LilyGO T-Display plně funkčním hardwarem Jade wallet. Tato část vás provede procesem počátečního nastavení, od vygenerování fráze seed až po připojení zařízení pomocí softwaru wallet, jako je Sparrow nebo mobilní aplikace Blockstream Green.


### Počáteční spuštění a nastavení zařízení



- Zapnutí zařízení:** Když je zařízení LilyGO stále připojeno k notebooku přes USB-C, měl by se automaticky spustit firmware Jade. Na displeji se zobrazí logo Jade.



- Vstup do režimu nastavení:** Zařízení zobrazí úvodní nabídku. K navigaci použijte dvě fyzická tlačítka na desce:
 - Levé tlačítko:** Posun nahoru/zpět
 - Pravé tlačítko:** Posun dolů/dopředu
 - Obě tlačítka současně:** Vybrat/potvrdit



- Vyberte možnost "Setup":** Přejděte na možnost Setup a potvrďte ji stisknutím obou tlačítek. Zařízení vás provede procesem počáteční konfigurace.


### Vytvoření Wallet



- Zvolte "Begin Setup" (Zahájit nastavení):** Zařízení vás vyzve k zahájení procesu vytváření wallet. Potvrďte svůj výběr.



- Vyberte možnost "Vytvořit nový Wallet":** Zobrazí se dvě možnosti:
 - Vytvořit novou větu Wallet:** Vygeneruje novou větu seed (zvolte ji pro workshop)
 - Obnovení Wallet:** Obnovení existujícího wallet z fráze seed (pro pokročilé uživatele)



- Vyberte možnost "Create New Wallet" a potvrďte ji.



- Generování entropie:** Zařízení použije svůj generátor náhodných čísel k vytvoření kryptografické entropie. Tento proces trvá několik sekund, protože zařízení shromažďuje náhodnost z více zdrojů.


### Nahrávání klíčové fráze



- Zapište si frázi seed:** Přístroj nyní zobrazí 12slovnou frázi BIP39 seed, vždy po jednom slově. Toto je nejdůležitější krok celého procesu.


**Důležité bezpečnostní postupy:**


- Napište každé slovo zřetelně na papír (použijte přiložené kartičky s frázemi seed, pokud jsou k dispozici)
- Každé slovo při psaní dvakrát zkontrolujte
- Nikdy nefotografujte větu seed telefonem
- Nikdy nezadávejte tato slova do počítače nebo telefonu
- Frázi seed si nechte pro sebe - nesdílejte obrazovku ani ji neukazujte ostatním



- Ověření fráze seed:** Po zapsání všech 12 slov vás přístroj požádá o potvrzení několika slov z fráze, aby se ujistil, že jste je zaznamenali správně. Pomocí tlačítek vyberte správné slovo pro každou výzvu.


**Profi tip:** Než přejdete k dalšímu postupu, procvičte si přečtení věty seed nahlas (potichu, aby ji ostatní neslyšeli). Pomůže to zachytit případné chyby v písmu nebo nejasnosti.


### Metoda připojení



- Výběr typu připojení:** Firmware Jade podporuje dva způsoby připojení:
 - USB:** Kabelové připojení přes kabel USB-C (doporučeno pro tento workshop)
 - Bluetooth:** Bezdrátové připojení k mobilním zařízením



- Prozatím vyberte možnost **USB**, protože je to nejjednodušší možnost pro software wallet pro stolní počítače a nezavádí vektory bezdrátových útoků.



- Pojmenování zařízení:** Zařízení Jade zobrazí jedinečný identifikátor, například "Connect Jade A7D924". Tento identifikátor vám pomůže rozlišit více hardwarových peněženek, pokud jich nakonec vytvoříte více než jednu. V případě potřeby si tento identifikátor poznamenejte.


### Připojení k softwaru Wallet


Nyní máte dvě hlavní možnosti propojení s nově vytvořeným hardwarem wallet: mobilní aplikaci Blockstream Green (pro použití na cestách) nebo Sparrow Wallet (pro použití na stolním počítači s pokročilejšími funkcemi). Pro tento seminář se zaměříme na Sparrow Wallet, protože nabízí lepší přehled o technických detailech transakcí Bitcoin.


#### Možnost 1: Mobilní aplikace Blockstream Green (rychlý start)


Pokud chcete zařízení rychle otestovat pomocí mobilního zařízení:



- Stáhněte si aplikaci **Blockstream Green** z App Store (iOS) nebo Google Play (Android)
- Otevřete aplikaci a vyberte možnost "Connect Hardware Wallet"
- V seznamu podporovaných zařízení vyberte možnost "Jade"
- Připojte zařízení Jade k telefonu pomocí kabelu USB-C na USB-C (nebo adaptéru USB-C na Lightning pro iPhone 15+)
- Podle pokynů na obrazovce se připojte a vytvořte svůj první účet wallet


**Poznámka ke Liquid:** Aplikace Blockstream Green podporuje jak Bitcoin, tak Liquid (postranní řetězec Bitcoin). Pokud používáte funkce Liquid, můžete být vyzváni k "Exportování hlavního zaslepovacího klíče" - to umožní aplikaci zobrazit částky transakcí v síti Liquid, které jsou jinak důvěrné. Pro tento workshop můžete funkce Liquid vynechat a zaměřit se na standardní transakce Bitcoin.


#### Možnost 2: Sparrow Wallet (doporučeno pro dílnu)


Sparrow Wallet je výkonná aplikace pro stolní počítače, která vám umožňuje detailní kontrolu nad transakcemi Bitcoin a bezproblémové propojení s hardwarem Jade wallet.


**Instalace:**



- Stáhněte si Sparrow Wallet z oficiálních webových stránek: [sparrowwallet.com](https://sparrowwallet.com)
- Ověřte podpis stahování (podrobnosti naleznete v dokumentaci Sparrow)
- Instalace a spuštění aplikace


**Připojení vašeho nefritu ke Sparrow:**



- V okně Sparrow přejděte na **Soubor → Nový Wallet**
- Pojmenujte svůj wallet (např. "My Jade Wallet")
- Klikněte na **Připojený Hardware Wallet**
- Sparrow by měl automaticky detekovat připojené zařízení Jade
- Pokud se zobrazí výzva, potvrďte připojení na displeji Jade stisknutím obou tlačítek
- Vyberte požadovaný typ skriptu:
 - Nativní Segwit (P2WPKH):** Doporučeno pro začátečníky - nejnižší poplatky, nejširší kompatibilita s moderními peněženkami
 - Vnořený Segwit (P2SH-P2WPKH):** Pro kompatibilitu se staršími službami
 - Taproot (P2TR):** Nejpokročilejší, nabízí nejlepší soukromí a nejnižší poplatky, ale vyžaduje špičkovou podporu wallet
- Kliknutím na tlačítko **Importovat úložiště klíčů** dokončíte připojení


**Konfigurace připojení k serveru Sparrow:**


Předtím, než si můžete prohlédnout svůj zůstatek nebo vysílat transakce, musí se Sparrow připojit k uzlu Bitcoin a načíst data blockchainu. Máte několik možností, z nichž každá přináší různé kompromisy mezi pohodlím, soukromím a důvěryhodností:



- Veřejný Electrum Server (nejjednodušší, nejméně soukromý):** Připojuje se k veřejnému serveru provozovanému třetí stranou. Rychle se nastavuje, ale server může vidět adresy vašeho wallet a případně je spojit s vaší IP adresou. Vhodné pro testování na testnetu.
 - V aplikaci Sparrow přejděte do nabídky **Nástroje → Předvolby → Server**
 - Vyberte možnost **Veřejný server** a vyberte server ze seznamu
 - Kliknutím na tlačítko **Test Connection** ověříte



- Uzel Bitcoin Core nebo Uzly (většina soukromých, většina pracovních):** Spusťte si vlastní plnohodnotný uzel Bitcoin. Jedná se o zlatý standard pro soukromí a ověřování, protože každou transakci ověřujete sami a nevěříte serveru nikoho jiného. Vyžaduje však stažení celého blockchainu (~600 GB) a udržování synchronizace vašeho uzlu.
 - Instalace a synchronizace jádra Bitcoin nebo uzlů
 - V programu Sparrow přejděte do nabídky **Nástroje → Předvolby → Server**
 - Vyberte možnost **Bitcoin Core nebo Knots** a zadejte údaje o připojení uzlu



- Soukromý Electrum Server (dobrá rovnováha):** Hostujte vlastní server Electrum (jako Fulcrum nebo Electrs) připojený k uzlu Bitcoin Core nebo Knots. Nabízí plné soukromí bez nutnosti provozovat Sparrow na stejném stroji jako váš uzel.
 - Nastavení serveru Electrum, který ukazuje na uzel Bitcoin Core nebo Knots
 - V systému Sparrow přejděte do nabídky **Nástroje → Předvolby → Server**
 - Vyberte možnost **Soukromý Electrum** a zadejte adresu URL svého serveru


Pro tento workshop je použití **veřejného Electrum Server** pro transakce testnetu naprosto v pořádku. V produkčním prostředí se skutečnými prostředky byste měli zvážit spuštění vlastního uzlu nebo použití důvěryhodného privátního serveru pro maximální soukromí.


#### Možnost 3: Aplikace Blockstream Green pro stolní počítače (rychlý start)


Blockstream Green je software pro dokončení nastavení JadeDIY a musí být ve verzi pro stolní počítače



- Pořiďte si oficiální aplikaci Blockstream - odkaz na ni najdete na jejich webových stránkách. Až tam budete, klikněte na [Download now] (https://blockstream.com/app/).


![image](assets/fr/12.webp)



- V závislosti na tom, kam stahujete soubory, bude soubor pravděpodobně ve složce Stažené soubory. Zkontrolujte ji a poklepáním na spustitelný soubor software nainstalujte.


![image](assets/fr/13.webp)



- Pro spuštění instalačního programu bude možná nutné udělit práva správce. Jakmile tak učiníte, zobrazí se okno, které by mělo vypadat jako na následujícím obrázku - klikněte na **Další**.


![image](assets/fr/14.webp)



- Zvolte místo, kam chcete nainstalovanou aplikaci umístit (umístění s ostatními programy nebo místo, které lze snadno najít), a klikněte na tlačítko **Další**.


![image](assets/fr/15.webp)



- Instalační program se zeptá na název zástupce. Zadejte jej nebo ponechte výchozí a klikněte na tlačítko **Další**.


![image](assets/fr/16.webp)



- Pokud chcete zástupce na ploše, zaškrtněte políčko; jinak klikněte na tlačítko **Další**.


![image](assets/fr/17.webp)



- Nakonec klikněte na tlačítko **Install** a počkejte několik minut na dokončení instalace.


![image](assets/fr/18.webp)



- Lišta průběhu by se měla vyplnit až do konce.


![image](assets/fr/19.webp)



- Po dokončení se zobrazí nová stránka - klikněte na tlačítko **Dokončit**.


![image](assets/fr/20.webp)



- Vyhledejte nově nainstalovanou aplikaci Blockstream (příklad je uveden v nabídce Start systému Windows 11).


![image](assets/fr/21.webp)



- Jakmile ji najdete, kliknutím ji spusťte - měla by se zobrazit úvodní obrazovka.


### Ověření nastavení


Po připojení ke Sparrow (nebo jiné aplikaci wallet):



- Kontrola adres:** Sparrow zobrazí přijímací adresy odvozené z vaší fráze seed. Adresu si můžete ověřit na zařízení Jade tak, že přejdete na kartu "Receive" (Příjem) v Sparrow a kliknete na "Display Address" (Zobrazit Address) - adresa by se měla zobrazit jak na obrazovce počítače, tak na displeji zařízení Jade.



- Vytvoření přijímací adresy:** Klikněte na kartu **Příjem** v aplikaci Sparrow a zkopírujte první přijímací adresu Bitcoin.



- Připraveno pro transakce:** Váš hardware wallet je nyní plně nakonfigurován a připraven přijímat a podepisovat transakce Bitcoin. Přejděte k další části a vyzkoušejte si podepisování transakcí testnetu.



---

### Kontrolní seznam rychlého nastavení



- Firmware Jade se úspěšně zavádí
- Vytvoření nové věty wallet s 12 slovy věty seed
- Jasně zapsaná a ověřená věta o semenech
- Vybraný režim připojení USB
- Nainstalovaný a připojený software Wallet (Sparrow)
- Konfigurace připojení k serveru (veřejné připojení Electrum pro mainnet)
- První přijímací adresa vygenerovaná a ověřená v zařízení



---

**Licence MIT**


**Copyright (c) 2025 The Bitcoin Network NYC**


Tímto se uděluje bezplatné povolení každé osobě, která získá kopii tohoto softwaru a souvisejících souborů dokumentace (dále jen "software"), k neomezenému nakládání se softwarem, včetně neomezeného práva používat, kopírovat, upravovat, slučovat, publikovat, distribuovat, poskytovat sublicence a/nebo prodávat kopie softwaru, a povolit osobám, kterým je software poskytnut, aby tak činily za následujících podmínek:


Výše uvedené oznámení o autorských právech a toto oznámení o povolení musí být obsaženo ve všech kopiích nebo podstatných částech softwaru.


SOFTWARE JE POSKYTOVÁN "TAK, JAK JE", BEZ JAKÝCHKOLI ZÁRUK, VÝSLOVNÝCH NEBO PŘEDPOKLÁDANÝCH, MIMO JINÉ VČETNĚ ZÁRUK PRODEJNOSTI, VHODNOSTI PRO URČITÝ ÚČEL A NEPORUŠOVÁNÍ PRÁV. AUTOŘI ANI DRŽITELÉ AUTORSKÝCH PRÁV V ŽÁDNÉM PŘÍPADĚ NENESOU ODPOVĚDNOST ZA JAKÉKOLI NÁROKY, ŠKODY NEBO JINOU ODPOVĚDNOST, AŤ UŽ SMLUVNÍ, DELIKTNÍ NEBO JINOU, VYPLÝVAJÍCÍ ZE SOFTWARU, Z NĚJ NEBO V SOUVISLOSTI S NÍM NEBO S JEHO POUŽÍVÁNÍM ČI JINÝM NAKLÁDÁNÍM S NÍM.


---