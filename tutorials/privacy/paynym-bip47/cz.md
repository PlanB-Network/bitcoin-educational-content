---
name: BIP47 - PayNym

description: Jak fungují PayNymy
---
***VAROVÁNÍ:** Po zatčení zakladatelů peněženky Samourai a zabavení jejich serverů dne 24. dubna již aplikaci nemohou používat uživatelé, kteří nemají vlastní Dojo. BIP47 zůstává použitelný ve peněžence Sparrow Wallet pro všechny uživatele a **v peněžence Samourai pouze pro uživatele, kteří mají Dojo**.*

_Sledujeme vývoj této kauzy stejně jako vývoj souvisejících nástrojů. Ujistěte se, že tento tutoriál aktualizujeme, jakmile budou k dispozici nové informace._

_Tento tutoriál je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je odpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

> "Je příliš velký," řekli všichni, a krocan, který se narodil se ostruhami a myslel si, že je císař, se nafoukl jako loď s napnutými plachtami a s velkou vzteky se rovnou vypravil k němu, jeho oči byly červené jako oheň. Chudý malý kachňátko nevědělo, zda stát na místě nebo utéct, a bylo velmi nešťastné, protože ho všechny kachny na dvoře pohrdaly.

![BIP47, ilustrace ošklivého kachňátka](assets/1.webp)

Jedním z největších problémů protokolu Bitcoin je opětovné používání adres. Transparentnost a distribuce sítě činí tuto praxi nebezpečnou pro soukromí uživatelů. Aby se předešlo problémům spojeným s tím, doporučuje se pro každou novou příchozí platbu do peněženky použít novou prázdnou přijímací adresu, což může být v některých případech složité dosáhnout.

Tento kompromis je starý jako White Paper. Satoshi nás již v roce 2008 ve své publikované práci varoval před tímto rizikem:

> "Jako další ochranný prostředek by pro každou transakci měl být použit nový pár klíčů, aby nebyly spojeny s jedním majitelem."

Existuje mnoho řešení, jak přijímat více plateb bez opětovného používání adresy. Každé z nich má své kompromisy a nevýhody. Mezi všemi těmito řešeními je [BIP47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki), návrh vyvinutý Justusem Ranvierem a publikovaný v roce 2015, který umožňuje generování opakovaně použitelných platebních kódů. Jeho cílem je umožnit provádění více transakcí téže osobě bez opětovného používání adresy.

Původně byl tento návrh částí komunity přijat s pohrdáním a nikdy nebyl přidán do Bitcoin Core. Nicméně některé softwary se rozhodly jej implementovat samostatně. Například Samourai Wallet vyvinula vlastní implementaci BIP47: PayNym. Dnes je tato implementace dostupná v peněžence Samourai pro smartphony, stejně jako na [Sparrow Wallet](https://sparrowwallet.com/) pro PC.

Časem Samourai naprogramoval nové funkce přímo související s PayNym. Nyní je k dispozici celý ekosystém nástrojů optimalizujících soukromí uživatele na základě PayNym a BIP47.
V tomto článku objevíte princip BIP47 a PayNym, mechanismy těchto protokolů a praktické aplikace, které z nich vyplývají. Budu se věnovat pouze první verzi BIP47, která je aktuálně používána pro PayNym, ale verze 2, 3 a 4 fungují prakticky stejným způsobem.
Jediným významným rozdílem je nalezen v transakci oznámení. Verze 1 používá jednoduchou adresu s OP_RETURN pro oznámení, verze 2 používá multisig skript (bloom-multisig) s OP_RETURN, a verze 3 a 4 jednoduše používají multisig skript (cfilter-multisig). Mechanismy diskutované v tomto článku, včetně studovaných kryptografických metod, jsou tedy aplikovatelné na všechny čtyři verze. K dnešnímu dni implementace PayNym na Samourai Wallet a Sparrow používá první verzi BIP47.

## Shrnutí:

1- Problém opakovaného použití adresy.

2- Principy BIP47 a PayNym.

3- Tutoriály: Používání PayNym.

- Sestavení BIP47 transakce s Samourai Wallet.
- Sestavení BIP47 transakce s Sparrow Wallet.

4- Funkce BIP47.

- Opakovaně použitelný platební kód.
- Kryptografická metoda: Výměna klíčů Diffie-Hellman založená na eliptických křivkách (ECDH).
- Transakce oznámení.
- Sestavení transakce oznámení.
- Přijetí transakce oznámení.
- BIP47 platební transakce.
- Přijetí BIP47 platby a odvození soukromého klíče.
- Vrácení BIP47 platby.

5- Odvozené použití PayNym.

6- Můj osobní názor na BIP47.

## Problém opakovaného použití adresy.

Přijímací adresa slouží k přijímání bitcoinů. Je generována z veřejného klíče hashováním a aplikací specifického formátu. Umožňuje tedy vytvoření nové podmínky pro výdaj mince za účelem změny jejího majitele.

> Chcete-li se dozvědět více o generování přijímací adresy, doporučuji přečíst poslední část tohoto článku: Bitcoinová peněženka - úryvek z [ebooku Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).

Pravděpodobně jste již slyšeli od znalého bitcoinového uživatele, že přijímací adresy jsou určeny k jednorázovému použití a že byste měli pro každou novou příchozí platbu do vaší peněženky generovat novou. Dobře, ale proč?
Základně opakované použití adresy přímo neohrožuje vaše prostředky. Použití kryptografie na eliptických křivkách vám umožňuje prokázat síti, že jste v držení soukromého klíče, aniž byste tento klíč odhalili. Proto můžete na stejné adrese uzamknout více různých UTXO (Unspent Transaction Outputs) a utratit je v různých časech. Pokud neodhalíte soukromý klíč spojený s touto adresou, nikdo nemůže přistupovat k vašim prostředkům. Problém s opakovaným použitím adresy je více spojen s ochranou soukromí.

Jak bylo zmíněno v úvodu, transparentnost a distribuce Bitcoinové sítě znamená, že jakýkoliv uživatel s přístupem k uzlu může pozorovat transakce platebního systému. V důsledku toho mohou vidět různé zůstatky adres. Satoshi Nakamoto pak zmínil možnost generování nových párů klíčů, a tedy nových adres, pro každou novou příchozí platbu do peněženky. Cílem by bylo mít další ochrannou bariéru v případě spojení identity uživatele s jedním z jejich párů klíčů.

Dnes, s přítomností společností provádějících analýzu řetězců a rozvojem KYC (Know Your Customer), již používání prázdných adres není další ochrannou bariérou, ale povinností pro každého, kdo si i jen trochu cení svého soukromí.

Usilování o soukromí není pohodlí nebo fantazie maximalistů Bitcoinu. Je to konkrétní parametr, který přímo ovlivňuje vaši osobní bezpečnost a bezpečnost vašich prostředků. Abych vám to pomohl lépe pochopit, zde je velmi konkrétní příklad:
- Bob kupuje Bitcoin prostřednictvím průměrování nákladů na dolar (DCA), což znamená, že pravidelnými intervaly získává malé množství Bitcoinu, aby vyrovnal svoji vstupní cenu. Bob systematicky posílá zakoupené prostředky na stejnou přijímací adresu. Každý týden kupuje 0,01 Bitcoinu a posílá jej na tuto stejnou adresu. Po dvou letech Bob na této adrese nahromadil celý Bitcoin.
- Pekař na rohu přijímá platby v Bitcoinech. Bob, nadšený možností utrácet Bitcoiny, jde koupit svou bagetu v satoshi. K platbě používá prostředky uzamčené na jeho adrese. Jeho pekař teď ví, že vlastní Bitcoin. Tato významná částka by mohla vzbudit závist a Bob by v budoucnu mohl čelit fyzickému útoku.

Opakované používání adresy umožňuje pozorovateli udělat nesporné spojení mezi vašimi různými UTXO a někdy mezi vaší identitou a celou vaší peněženkou.
To je důvod, proč většina softwaru pro Bitcoin peněženky automaticky generuje novou přijímací adresu, když kliknete na tlačítko "Přijmout". Pro pravidelné uživatele není zvykání si na používání nových adres velkou nepříjemností. Nicméně pro online podniky, burzy nebo charitativní kampaně může být toto omezení rychle nezvladatelné.
Existuje mnoho řešení pro tyto organizace. Každé z nich má své výhody a nevýhody, ale k dnešnímu dni, a jak uvidíme později, BIP47 se opravdu vymyká ostatním.

Tento problém opakovaného používání adresy není v Bitcoinu zanedbatelný. Jak můžete vidět na níže uvedeném grafu z webu oxt.me, celková míra opakovaného používání adresy uživateli Bitcoinu je v současnosti 52%:
Graf z OXT.me ukazující vývoj celkové míry opakovaného používání adresy v síti Bitcoin.

![image](assets/2.webp)

Kredit: OXT

Většina těchto opakovaných použití pochází z burz, které z důvodů efektivity a pohodlí používají stejnou adresu mnohokrát. K dnešnímu dni by BIP47 bylo nejlepším řešením, jak tomuto jevu mezi burzami zabránit. Pomohlo by to snížit celkovou míru opakovaného používání adresy bez způsobení příliš velkého tření pro tyto subjekty.

Toto globální opatření napříč celou sítí je v tomto případě zvláště relevantní. Skutečně, opakované používání adresy není problémem pouze pro osobu, která se tohoto chování dopouští, ale také pro každého, kdo s ní transakci provádí. Ztráta soukromí v Bitcoinu funguje jako virus, šířící se z uživatele na uživatele. Studium globálního opatření na všech transakcích v síti nám umožňuje pochopit rozsah tohoto jevu.

## Principy BIP47 a PayNym.

BIP47 má za cíl poskytnout jednoduchý způsob, jak přijímat více plateb bez opakovaného používání adresy. Jeho provoz je založen na použití opakovaně použitelného platebního kódu.

Takto může více odesílatelů posílat více plateb na jediný opakovaně použitelný platební kód jiného uživatele, aniž by příjemce musel pro každou novou transakci poskytovat novou prázdnou adresu.

Uživatel může svůj platební kód volně sdílet (na sociálních sítích, na svém webu...) bez rizika ztráty soukromí, na rozdíl od běžné přijímací adresy nebo veřejného klíče.
Pro provedení výměny musí oba uživatelé mít Bitcoin peněženku s implementací BIP47, jako je PayNym na Samourai Wallet nebo Sparrow Wallet. Asociace platebních kódů obou uživatelů vytvoří mezi nimi tajný kanál. Pro správné vytvoření tohoto kanálu musí odesílatel provést transakci na blockchainu Bitcoinu: notifikační transakci (o tomto později více).

Asociace platebních kódů obou uživatelů generuje sdílená tajemství, která sama generují velké množství jedinečných přijímacích adres Bitcoinu (přesně 2^32). Takže ve skutečnosti není platba pomocí BIP47 poslána na platební kód, ale na zcela normální adresy, odvozené z platebních kódů zúčastněných stran.
Platební kód funguje jako virtuální identifikátor, odvozený ze seedu peněženky. Ve struktuře derivace HD peněženky se platební kód nachází na úrovni 3, na úrovni účtu peněženky.
![image](assets/3.webp)

Jeho účel derivace je označen jako 47' (0x8000002F) s odkazem na BIP47. Například cesta derivace pro opakovaně použitelný platební kód by byla:

> m/47'/0'/0'/

Abych vám dal představu, jak platební kód vypadá, zde je ten můj:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Může být také zakódován jako QR kód, aby se usnadnila komunikace:

![image](assets/4.webp)

Co se týče PayNym Botů, těch robotů, které vidíte na Twitteru, jedná se pouze o vizuální reprezentace vašeho platebního kódu, vytvořené peněženkou Samourai. Jsou generovány pomocí hash funkce, což je činí téměř jedinečnými. Zde je ten můj s jeho identifikátorem:

> +throbbingpond8B1

![image](assets/5.webp)

Tyto Boty nemají žádnou skutečnou technickou užitečnost. Místo toho usnadňují interakce mezi uživateli tím, že vytvářejí virtuální vizuální identitu.

Pro uživatele je proces provedení platby BIP47 s implementací PayNym extrémně jednoduchý. Představme si, že Alice chce poslat platby Bobovi:

1. Bob sdílí svůj QR kód nebo přímo svůj opakovaně použitelný platební kód. Může jej umístit na svůj web, na své různé veřejné sociální sítě, nebo jej poslat Alici jiným komunikačním prostředkem.
2. Alice otevře svůj software Samourai nebo Sparrow a naskenuje nebo vloží Bobův platební kód.
3. Alice propojí svůj PayNym s Bobovým ("Follow" v angličtině). Tato operace se provádí mimo řetězec a je zcela zdarma.

4. Alice propojí svůj PayNym s Bobovým ("Connect" v angličtině). Tato operace se provádí "na řetězci". Alice musí zaplatit poplatky za těžbu transakce a také pevný poplatek 15 000 sats za službu na Samourai. Na Sparrow jsou poplatky za službu prominuty. Tento krok nazýváme notifikační transakce.

5. Jakmile je notifikační transakce potvrzena, Alice může vytvořit BIP47 platební transakci pro Boba. Její peněženka automaticky vygeneruje novou prázdnou přijímací adresu, pro kterou má klíč pouze Bob.

Provedení notifikační transakce, tj. propojení jejího PayNym, je povinným předpokladem pro provádění BIP47 plateb. Jakmile je toto provedeno, může odesílatel provést více plateb příjemci (přesně 2^32) bez nutnosti provádět novou notifikační transakci.

Možná jste si všimli, že existují dvě různé operace pro propojení PayNymů: "follow" a "connect". Operace propojení ("connect") odpovídá notifikační transakci BIP47, která je prostě Bitcoinová transakce s určitými informacemi přenášenými prostřednictvím výstupu OP_RETURN. Tím pomáhá zřídit šifrovanou komunikaci mezi oběma uživateli pro vytvoření sdílených tajemství potřebných pro generování nových prázdných přijímacích adres.

Na druhou stranu, operace propojení ("follow" nebo "relier") umožňuje propojení na Soroban, šifrovaný komunikační protokol založený na Toru, speciálně vyvinutý týmy Samourai.

Shrnutí:
- Propojení dvou PayNymů ("sledování") je zcela zdarma. Umožňuje navázat šifrovanou komunikaci mimo blockchain, zejména pro použití kolaborativních transakčních nástrojů Samourai (Stowaway nebo StonewallX2). Tato operace je specifická pro PayNym a není popsána v BIP47.
- Propojení dvou PayNymů má svou cenu. Zahrnuje provedení notifikační transakce pro iniciaci spojení. Cena se skládá z jakýchkoli poplatků za služby, poplatků za těžbu transakce a 546 sats poslaných na notifikační adresu příjemce, aby byl informován o otevření tunelu. Tato operace souvisí s BIP47. Po dokončení může odesílatel provádět více plateb BIP47 příjemci.

Pro propojení dvou PayNymů musí být již předtím propojeny.

## Tutoriály: Používání PayNym.

Nyní, když jsme probrali teorii, pojďme se společně podívat na praxi. Cílem níže uvedených tutoriálů je propojit můj PayNym v mém Sparrow peněžence s mým PayNym v mém Samourai peněžence. První tutoriál vás naučí, jak provést transakci s použitím opakovaně použitelného platebního kódu z Samourai do Sparrow, a druhý tutoriál popisuje stejný mechanismus ze Sparrow do Samourai.

> Tyto tutoriály jsem provedl na Testnetu. Nejedná se o skutečné bitcoiny.

### Vytvoření BIP47 transakce s peněženkou Samourai.

Začít musíte samozřejmě s aplikací Samourai Wallet. Můžete ji přímo stáhnout z Google Play Store nebo s APK souborem dostupným na oficiálních stránkách Samourai.

Jakmile je peněženka inicializována, pokud jste tak již neučinili, vyžádejte si svůj PayNym kliknutím na plus (+) v pravém dolním rohu, poté na "PayNym".

Prvním krokem k provedení platby BIP47 je získání opakovaně použitelného platebního kódu od našeho příjemce. Poté budeme moci navázat spojení a následně propojit:

![video](assets/6.mp4)

Jakmile je notifikační transakce potvrzena, mohu poslat více plateb mému příjemci. Každá transakce bude automaticky provedena s novou prázdnou adresou, pro kterou má příjemce klíče. Příjemce nemusí podnikat žádné kroky, vše je vypočítáno na mé straně.

Zde je návod, jak provést BIP47 transakci s peněženkou Samourai:

![video](assets/7.mp4)

### Vytvoření BIP47 transakce s peněženkou Sparrow.

Stejně jako u Samourai, samozřejmě potřebujete mít software Sparrow. Je dostupný na vašem počítači. Můžete si jej stáhnout z jejich [oficiálních stránek](https://sparrowwallet.com/).

Před instalací softwaru na vaše zařízení se ujistěte, že ověříte podpis vývojáře a integritu staženého softwaru.

Vytvořte peněženku a vyžádejte si svůj PayNym kliknutím na "Zobrazit PayNym" v menu "Nástroje" v horní liště:

![image](assets/8.webp)

Poté budete muset propojit a spojit svůj PayNym s PayNym vašeho příjemce. K tomu zadejte jejich opakovaně použitelný platební kód do okna "Najít kontakt", sledujte je a poté proveďte notifikační transakci kliknutím na "Propojit kontakt":

![image](assets/9.webp)

Jakmile je notifikační transakce potvrzena, můžete posílat platby na opakovaně použitelný platební kód. Zde je návod, jak na to:

![video](assets/10.mp4)

Nyní, když jsme byli schopni prozkoumat praktický aspekt implementace PayNym BIP47, pojďme se podívat, jak všechny tyto mechanismy fungují a jaké kryptografické metody jsou používány.
Pro studium mechanismů BIP47 je nezbytné porozumět struktuře hierarchické deterministické (HD) peněženky, mechanismům pro odvozování dětských klíčových párů, stejně jako principům eliptické křivkové kryptografie. Naštěstí, veškeré potřebné informace k pochopení této části můžete najít na mém blogu:
- [Porozumění odvozovacím cestám Bitcoinové peněženky](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-bitcoin)

- [Bitcoinová peněženka - úryvek z e-knihy Bitcoin Democratized 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2)

### Opakovaně použitelný platební kód.

Jak je vysvětleno ve druhé části tohoto dokumentu, opakovaně použitelný platební kód se nachází na třetí úrovni hierarchie HD peněženky. Je do jisté míry srovnatelný s xpub, jak svým umístěním, tak strukturou, stejně jako svou rolí.

Zde jsou různé části, které tvoří 80-bajtový platební kód:

- Byte 0: Verze. Pokud používáte první verzi BIP47, tento byte bude roven 0x01.

- Byte 1: Bitové pole. Tento prostor je vyhrazen pro poskytování dodatečných indikací v případě specifického použití. Pokud jednoduše používáte PayNym, tento byte bude roven 0x00.

- Byte 2: Parita y. Tento byte udává 0x02 nebo 0x03 v závislosti na paritě (sudé nebo liché číslo) hodnoty y-ové souřadnice našeho veřejného klíče. Pro více informací o této praxi si prosím přečtěte krok 1 sekce "odvození adresy" tohoto článku.

- Od bytu 3 do bytu 34: Hodnota x. Tyto byty udávají x-ovou souřadnici našeho veřejného klíče. Konkatenace x a parity y nám dává náš komprimovaný veřejný klíč.

- Od bytu 35 do bytu 66: Řetězový kód. Tento prostor je vyhrazen pro řetězový kód spojený s výše zmíněným veřejným klíčem.

- Od bytu 67 do bytu 79: Výplň. Tento prostor je vyhrazen pro možný budoucí vývoj. Pro verzi 1 jej jednoduše vyplníme nulami, abychom dosáhli 80 bajtů, což je velikost dat pro výstup OP_RETURN.

Zde je šestnáctková reprezentace mého opakovaně použitelného platebního kódu, prezentovaná v předchozí sekci, s barvami odpovídajícími výše uvedeným bytům:
Dále je také potřeba přidat předponový byte "P", aby bylo rychle zřejmé, že se jedná o platební kód. Tento byte je 0x47.

> 0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000

Nakonec vypočítáme kontrolní součet tohoto platebního kódu pomocí HASH256, což znamená dvojité hašování funkcí SHA256. Získáme první čtyři byty tohoto digestu a konkatenujeme je na konec (v růžové).
Platební kód je připraven, nyní jej musíme pouze převést do Base 58:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Jak vidíte, tato konstrukce úzce připomíná strukturu rozšířeného veřejného klíče typu "xpub".

Během tohoto procesu získání našeho platebního kódu jsme použili komprimovaný veřejný klíč a řetězový kód. Tyto dva prvky jsou výsledkem deterministické a hierarchické derivace ze semínka peněženky, následující cestu derivace: m/47'/0'/0'/
Konkrétně, abychom získali veřejný klíč a řetězový kód opakovaně použitelného platebního kódu, vypočítáme hlavní soukromý klíč ze semínka, poté odvodíme dvojici dětských klíčů s indexem 47 + 2^31 (pevná derivace). Poté odvodíme další dvě dvojice dětských klíčů s indexem 2^31 (pevná derivace).

> Pokud se chcete dozvědět více o odvozování dětských klíčových párů v hierarchické deterministické Bitcoinové peněžence, doporučuji absolvovat CRYPTO301.

### Kryptografická metoda: Výměna klíčů Elliptic Curve Diffie-Hellman (ECDH).

Kryptografická metoda použitá v jádru BIP47 je ECDH (Elliptic-Curve Diffie-Hellman). Tento protokol je variantou klasické výměny klíčů Diffie-Hellman.

Diffie-Hellman, ve své první verzi, je protokol dohody o klíči představený v roce 1976, který umožňuje oběma stranám, každá s párem veřejných a soukromých klíčů, určit sdílené tajemství výměnou informací přes nezabezpečený komunikační kanál.

![obrázek](assets/11.webp)

Toto sdílené tajemství (červený klíč) pak lze použít pro další úkoly. Typicky lze toto sdílené tajemství použít k šifrování a dešifrování komunikace přes nezabezpečenou síť:

![obrázek](assets/12.webp)

Pro dosažení této výměny používá Diffie-Hellman modulární aritmetiku pro výpočet sdíleného tajemství. Zde je zjednodušené vysvětlení, jak to funguje:

- Alice a Bob se dohodnou na společné barvě, v tomto případě žluté. Tato barva je známá všem. Je to veřejná informace.

- Alice si vybere tajnou barvu, v tomto případě červenou. Smíchá obě barvy, výsledkem je oranžová.

- Bob si vybere tajnou barvu, v tomto případě tyrkysově modrou. Smíchá obě barvy, výsledkem je nebesky modrá.

- Alice a Bob mohou vyměnit barvy, které získali: oranžovou a nebesky modrou. Tato výměna může proběhnout přes nezabezpečenou síť a může být pozorována útočníky.

- Alice smíchá nebesky modrou barvu, kterou obdržela od Boba, se svou tajnou barvou (červenou). Získá hnědou.

- Bob smíchá oranžovou barvu, kterou obdržel od Alice, se svou tajnou barvou (tyrkysově modrou). Také získá hnědou.

![obrázek](assets/13.webp)
> Credit: Původní nápad: A.J. Han VinckVektorová verze: FlugaalPřeklad: Dereckson, Volné dílo, prostřednictvím Wikimedia Commons. https://commons.wikimedia.org/wiki/File:Diffie-Hellman_Key_Exchange_(fr).svg
V této zjednodušené verzi hnědá barva představuje tajemství sdílené mezi Alicí a Bobem. Mělo by být pochopeno, že ve skutečnosti je pro útočníka nemožné oddělit oranžovou a nebesky modrou barvu, aby získal Alicino nebo Bobovo tajné barvy.

Nyní se podívejme na jeho skutečné fungování. Na první pohled se může zdát Diffie-Hellman složitý na pochopení. Ve skutečnosti je princip fungování téměř dětsky jednoduchý. Než se pustíme do detailů jeho mechanismů, rychle vám připomenu dva matematické koncepty, které budeme potřebovat (a mimochodem, jsou také používány v mnoha dalších kryptografických metodách).

1. Prvočíslo je přirozené číslo, které má pouze dva dělitele: 1 a samo sebe. Například číslo 7 je prvočíslo, protože je dělitelné pouze 1 a 7 (samo sebou). Na druhou stranu, číslo 8 prvočíslem není, protože je dělitelné 1, 2, 4 a 8. Má tedy nejen dva dělitele, ale čtyři celé a kladné dělitele.

2. "Modulo" (označované "mod" nebo "%") je matematická operace, která umožňuje dvěma celým číslům vrátit zbytek z euklidovského dělení prvního čísla druhým číslem. Například 16 mod 5 je rovno 1.

Výměna klíčů Diffie-Hellman mezi Alicí a Bobem probíhá takto:

- Alice a Bob určí dvě společná čísla: p a g. p je prvočíslo. Čím větší je toto číslo p, tím bezpečnější Diffie-Hellman bude. g je primitivní kořen p. Tyto dvě čísla mohou být komunikována v prostém textu přes nezabezpečenou síť, jsou ekvivalenty žluté barvy ve zjednodušení výše. Alice a Bob potřebují mít přesně stejné hodnoty pro p a g.

- Jakmile jsou parametry zvoleny, Alice a Bob každý určí vlastní tajné náhodné číslo. Náhodné číslo získané Alicí se nazývá a (ekvivalent červené barvy) a náhodné číslo získané Bobem se nazývá b (ekvivalent tyrkysové barvy). Tyto dvě čísla musí zůstat tajné.

- Místo výměny těchto čísel a a b, každá strana vypočítá A (velké písmeno) a B (velké písmeno) tak, že:

> A je rovno g umocněnému na a modulo p:
> A = g^a % p

> B je rovno g umocněnému na b modulo p:
> B = g^b % p

- Tyto čísla A (ekvivalent oranžové barvy) a B (ekvivalent nebesky modré barvy) budou mezi oběma stranami vyměněny. Výměna může proběhnout v prostém textu přes nezabezpečenou síť.

- Alice, která nyní zná B, vypočítá hodnotu z tak, že:

> z je rovno B umocněnému na a modulo p:
> z = B^a % p

- Jako připomínka, B = g^b % p. Tedy:

  > z = B^a % p
  > z = (g^b)^a % p
  >
  > Podle pravidel umocňování:
  >
  > (x^n)^m = x^nm
  >
  > Tedy:
  >
  > z = g^ba % p

- Bob, který nyní zná A, také vypočítá hodnotu z následovně:
> z je rovno A umocněného na b modulo p:
> z = A^b % p
>
> Proto:
>
> z = (g^a)^b % p
> z = g^ab % p
> z = g^ba % p

Díky distributivitě operátoru modulo najdou Alice a Bob přesně stejnou hodnotu pro z. Toto číslo představuje jejich sdílené tajemství, které je ekvivalentem barvy hnědé v předchozím vysvětlení. Toto sdílené tajemství mohou použít k šifrování komunikace mezi nimi na nezabezpečené síti.

![Diagram technické operace Diffie-Hellman](assets/14.webp)

Útočník, který má k dispozici p, g, A a B, nebude schopen vypočítat a, b ani z. Provedení této operace by vyžadovalo reverzní umocňování, což je nemožné udělat jinak než zkoušením všech možností jednu po druhé, protože pracujeme s konečným polem. To by bylo ekvivalentní výpočtu diskrétního logaritmu, který je reciproční k umocňování v cyklické konečné skupině.

Proto, pokud zvolíme dostatečně velké hodnoty pro a, b a p, je Diffie-Hellman bezpečný. Typicky, s parametry o velikosti 2,048 bitů (číslo se 600 číslicemi v desítkové soustavě), by zkoušení všech možností pro a a b bylo nepraktické. Doposud, s čísly této velikosti, je algoritmus považován za bezpečný.

Právě zde leží hlavní nevýhoda protokolu Diffie-Hellman. Pro zajištění bezpečnosti musí algoritmus používat velká čísla. V důsledku toho je nyní preferován algoritmus ECDH, což je varianta Diffie-Hellmana, která používá algebraickou křivku, konkrétně eliptickou křivku. To nám umožňuje pracovat s mnohem menšími čísly při zachování ekvivalentní bezpečnosti, čímž se snižují požadavky na výpočetní a úložné zdroje.

Obecný princip algoritmu zůstává stejný. Nicméně, místo použití náhodného čísla a a čísla A vypočítaného z a pomocí modulárního umocňování, budeme používat dvojici klíčů založených na eliptické křivce. Místo spoléhání na distributivitu operátoru modulo, budeme používat zákon skupiny na eliptických křivkách, konkrétně asociativitu tohoto zákona.
Pokud nemáte znalosti o tom, jak fungují soukromé a veřejné klíče na eliptické křivce, v prvních šesti částech tohoto článku vysvětlím základy této metody.

Stručně řečeno, soukromý klíč je náhodné číslo mezi 1 a n-1 (kde n je řád křivky), a veřejný klíč je jedinečný bod na křivce určený soukromým klíčem prostřednictvím sčítání bodů a zdvojení od generátorového bodu, jak následuje:

> K = k·G

Kde K je veřejný klíč, k je soukromý klíč a G je generátorový bod.

Jednou z vlastností této dvojice klíčů je, že je velmi snadné určit K, pokud znáte k a G, ale v současné době je nemožné určit k, pokud znáte K a G. Jedná se o jednosměrnou funkci.

Jinými slovy, snadno můžete vypočítat veřejný klíč, pokud znáte soukromý klíč, ale je nemožné vypočítat soukromý klíč, pokud znáte veřejný klíč. Tato bezpečnost je opět založena na nemožnosti výpočtu diskrétního logaritmu.

Tuto vlastnost využijeme k adaptaci našeho algoritmu Diffie-Hellman. Princip operace ECDH je tedy následující:

- Alice a Bob se dohodnou na kryptograficky bezpečné eliptické křivce a jejích parametrech. Tyto informace jsou veřejné.
- Alice vygeneruje náhodné číslo ka, které bude jejím soukromým klíčem. Tento soukromý klíč musí zůstat tajný. Svůj veřejný klíč Ka určí přičtením a zdvojením bodů na vybrané eliptické křivce.
> Ka = ka·G

- Bob také generuje náhodné číslo kb, které bude jeho soukromým klíčem. Spočítá přidružený veřejný klíč Kb.

> Kb = kb·G

- Alice a Bob si vymění své veřejné klíče Ka a Kb přes nezabezpečenou veřejnou síť.

- Alice vypočítá bod (x, y) na křivce použitím svého soukromého klíče ka na Bobův veřejný klíč Kb.

> (x, y) = ka·Kb

- Bob vypočítá bod (x, y) na křivce použitím svého soukromého klíče kb na Alicein veřejný klíč Ka.

> (x, y) = kb·Ka

- Alice a Bob získají stejný bod na eliptické křivce. Sdíleným tajemstvím bude x-ová souřadnice tohoto bodu.

Dostanou stejné sdílené tajemství, protože:

> (x, y) = ka·Kb = ka·kb·G = kb·ka·G = kb·Ka

Potenciální útočník sledující nezabezpečenou veřejnou síť může získat pouze veřejné klíče každé strany a parametry vybrané křivky. Jak bylo vysvětleno dříve, tyto dvě informace samy o sobě neumožňují určení soukromých klíčů, takže útočník nemůže přistupovat k tajemství.
ECDH je algoritmus, který umožňuje výměnu klíčů. Často se používá společně s dalšími kryptografickými metodami pro definici protokolu. Například ECDH se používá v jádru TLS (Transport Layer Security), protokolu pro šifrování a autentizaci používaném pro internetovou transportní vrstvu. TLS používá pro výměnu klíčů ECDHE, variantu ECDH, kde jsou klíče efemérní, aby poskytovaly trvalou důvěrnost. Kromě ECDHE TLS také používá autentizační algoritmus jako ECDSA, šifrovací algoritmus jako AES a hashovací funkci jako SHA256.

TLS definuje "s" v "https" a malou ikonu zámku, kterou vidíte ve svém internetovém prohlížeči v levém horním rohu, což zaručuje šifrovanou komunikaci. Takže právě teď používáte ECDH čtením tohoto článku a pravděpodobně ho používáte každý den, aniž byste si to uvědomovali.

### Transakce oznámení.

Jak jsme zjistili v předchozí části, ECDH je varianta výměny Diffie-Hellman, která zahrnuje páry klíčů založené na eliptické křivce. Naštěstí máme spoustu párů klíčů, které splňují tento standard v našich Bitcoinových peněženkách!

Nápad spočívá v použití párů klíčů z hierarchicky deterministických Bitcoinových peněženek obou stran pro vytvoření sdílených a efemérních tajemství mezi nimi. V rámci BIP47 se místo toho používá ECDHE (Eliptická křivka Diffie-Hellman Efemérní).

ECDHE se původně používá v BIP47 k přenosu platebního kódu odesílatele příjemci. To je slavná transakce oznámení. Aby bylo možné použít BIP47, obě strany (odesílatel, který posílá platby, a příjemce, který platby přijímá) musí znát platební kód druhé strany. To je nezbytné pro odvození efemérních veřejných klíčů a tedy i určených přijímacích adres.
Před touto výměnou logicky odesílatel již zná platební kód příjemce, protože jej mohl získat mimo blockchain, například z jejich webových stránek nebo sociálních médií. Příjemce ovšem nemusí nutně znát platební kód odesílatele. Je nutné, aby jim byl předán, jinak nebudou schopni odvodit své efemerní klíče a tudíž nebudou vědět, kde se jejich bitcoiny nacházejí, a nebudou moci odemknout své prostředky. Přenos může proběhnout mimo blockchain, pomocí jiného komunikačního systému, ale to by představovalo problém, pokud by se peněženka obnovovala z seedu. Skutečně, jak jsem již zmínil, adresy BIP47 nejsou odvozeny ze seedu příjemce (v opačném případě by bylo lepší použít přímo jeden z jejich xpubů), ale jsou výsledkem výpočtu zahrnujícího jak platební kód příjemce, tak platební kód odesílatele. Proto, pokud příjemce ztratí svou peněženku a pokusí se ji obnovit ze seedu, bude nutně potřebovat mít všechny platební kódy lidí, kteří jim poslali bitcoiny prostřednictvím BIP47.

Bylo by možné používat BIP47 bez této notifikační transakce, ale každý uživatel by musel zálohovat platební kódy svých protějšků. Tato situace zůstane neudržitelná, dokud nebude nalezen jednoduchý a odolný způsob, jak tyto zálohy vytvářet, ukládat a aktualizovat. Notifikační transakce je tedy v současném stavu věcí téměř povinná.

Kromě své role zálohování platebních kódů, jak již název napovídá, tato transakce slouží také jako notifikace pro příjemce. Informuje jejich klienta, že byl právě otevřen tunel.

Než vysvětlím technické fungování notifikační transakce podrobněji, rád bych trochu hovořil o modelu soukromí. Skutečně, model soukromí BIP47 odůvodňuje určitá opatření přijatá při konstrukci této počáteční transakce.

Platební kód sám o sobě nepředstavuje přímé riziko pro soukromí. Na rozdíl od klasického modelu Bitcoinu, který umožňuje přerušit tok informací mezi identitou uživatele a transakcemi, zejména udržením anonymních veřejných klíčů, může být platební kód přímo spojen s identitou. To není povinné, ale toto spojení není nebezpečné.

Skutečně, platební kód přímo neodvozuje adresy používané pro příjem plateb BIP47. Místo toho jsou adresy získány aplikací ECDHE mezi dětskými klíči platebních kódů obou stran.

Takže samotný platební kód nepředstavuje přímé riziko pro soukromí, protože pouze notifikační adresa je od něj odvozena. Z ní lze vyvodit určité informace, ale obvykle nemůžete vědět, s kým transakci provádíte.

Je tedy nezbytné udržovat přísné oddělení mezi platebními kódy uživatelů. V tomto ohledu je počáteční komunikační krok kódu kritickým okamžikem pro soukromí plateb, a přesto je povinný pro správné fungování protokolu. Pokud lze jeden z platebních kódů veřejně získat (například z webové stránky), druhý kód, tj. kód odesílatele, by neměl být spojen s prvním.

Představme si například, že chci poslat dar pomocí BIP47 mírovému protestnímu hnutí v Kanadě:

- Tato organizace zveřejnila svůj platební kód přímo na svých webových stránkách nebo platformách sociálních médií.
- Tento kód je tedy spojen s hnutím.

- Získám tento platební kód.

- Než jim mohu poslat transakci, musím se ujistit, že znají můj osobní platební kód, který je také spojen s mou identitou, protože jej používám pro příjem transakcí z mých sociálních sítí.

Jak jim ho mohu předat? Pokud jim jej pošlu pomocí běžného komunikačního prostředku, informace může uniknout a já mohu být identifikován jako osoba podporující mírová hnutí.
Notifikační transakce rozhodně není jediným řešením pro tajné přenosy platebního kódu odesílatele, ale v současné době tuto roli plní perfektně díky aplikaci několika vrstev bezpečnosti.
V níže uvedeném diagramu červené čáry představují okamžik, kdy musí být tok informací přerušen, a černé šipky představují nezpochybnitelné vazby, které může vytvořit vnější pozorovatel:

![Diagram modelu soukromí pro opakovaně použitelný platební kód](assets/15.webp)

Ve skutečnosti, pro klasický model soukromí Bitcoinu, je často obtížné úplně přerušit tok informací mezi párem klíčů a uživatelem, zejména při provádění vzdálených transakcí. Například v případě kampaně na podporu, bude od příjemce vyžadováno, aby na svém webu nebo na sociálních médiích zveřejnil adresu nebo veřejný klíč. Správné použití BIP47, tj. s notifikační transakcí, tento problém řeší prostřednictvím ECDHE a šifrovací vrstvy, kterou budeme studovat.

Zřejmě, klasický model soukromí Bitcoinu je stále dodržován na úrovni efemérních veřejných klíčů odvozených z asociace dvou platebních kódů. Tyto dva modely jsou vzájemně závislé. Chci zde pouze zdůraznit, že na rozdíl od klasického použití veřejného klíče pro přijímání bitcoinů, může být platební kód spojen s identitou, protože informace "Bob provádí transakci s Alicí" je přerušena v jiném okamžiku. Platební kód se používá k generování platebních adres, ale pouhým pozorováním blockchainu je nemožné spojit BIP47 platební transakci s použitými platebními kódy.

### Konstrukce notifikační transakce.

Nyní se podívejme, jak tato notifikační transakce funguje. Představme si, že Alice chce poslat prostředky Bobovi pomocí BIP47. V mém příkladu Alice vystupuje jako odesílatel a Bob jako příjemce. Bob již zveřejnil svůj platební kód na svém webu, takže Alice již zná Bobův platební kód.

1. Alice vypočítá sdílené tajemství pomocí ECDH:

- Vybere pár klíčů ze své HD peněženky umístěné na jiné větvi než její platební kód. Poznamenejme, že tento pár by neměl být snadno spojen s notifikační adresou Alice nebo s identitou Alice (viz předchozí sekce).
- Alice vybere soukromý klíč z tohoto páru. Budeme mu říkat "a" (malé písmeno).

> a

- Alice načte veřejný klíč spojený s notifikační adresou Boba. Tento klíč je první potomek odvozený z platebního kódu Boba (index 0). Tento veřejný klíč budeme nazývat "B" (velké písmeno). Soukromý klíč spojený s tímto veřejným klíčem se nazývá "b" (malé písmeno). "B" je určeno pomocí sčítání bodů a zdvojení na eliptické křivce z "G" (generující bod) s "b" (soukromý klíč).

> B = b·G

- Alice vypočítá tajný bod "S" (velké písmeno) na eliptické křivce pomocí sčítání bodů a zdvojení, aplikuje svůj soukromý klíč "a" na Bobův veřejný klíč "B".

> S = a·B

- Alice vypočítá slepící faktor "f", který bude použit k šifrování jejího platebního kódu. K tomu vygeneruje pseudonáhodné číslo pomocí funkce HMAC-SHA512. Jako druhý vstup do této funkce použije hodnotu, kterou bude moci načíst pouze Bob: (x), což je x-ová souřadnice dříve vypočítaného tajného bodu. První vstup je (o), což je UTXO spotřebované jako vstup do této transakce (outpoint).

> f = HMAC-SHA512(o, x)

2. Alice převede svůj osobní platební kód na základ 2 (binární).
3. Používá tento slepý faktor jako klíč k provedení symetrické šifrování na nákladu svého platebního kódu. Použitý šifrovací algoritmus je jednoduše XOR. Operace provedená je podobná šifře Vernam, známé také jako "jednorázový blok":
- Alice nejprve rozdělí svůj slepý faktor na dvě části: prvních 32 bajtů se nazývá "f1" a posledních 32 bajtů se nazývá "f2". Takže máme:

> f = f1 || f2

- Alice vypočítá šifrovaný text (x') x-ové souřadnice veřejného klíče (x) svého platebního kódu a zvlášť vypočítá šifrovaný text (c') svého řetězového kódu (c). "f1" a "f2" působí jako šifrovací klíče a používá se operace XOR.

> x' = x XOR f1
>
> c' = c XOR f2

- Alice nahradí skutečné hodnoty abscisy veřejného klíče (x) a řetězového kódu (c) ve svém platebním kódu šifrovanými hodnotami (x') a (c').

Než budeme pokračovat v technickém popisu této notifikační transakce, pojďme na chvíli diskutovat operaci XOR. XOR je bitový logický operátor založený na Booleově algebře. Pro dva bitové operandy vrací 1, pokud se odpovídající bity liší, a vrací 0, pokud jsou odpovídající bity stejné. Zde je pravdivostní tabulka pro XOR na základě hodnot operandů D a E:

| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Například:

> 0110 XOR 1110 = 1000

Nebo:

> 010011 XOR 110110 = 100101

S ECDH je použití XOR jako šifrovací vrstvy obzvláště koherentní. Nejprve, díky tomuto operátoru, je šifrování symetrické. To umožňuje příjemci dešifrovat platební kód stejným klíčem, který byl použit pro šifrování. Šifrovací a dešifrovací klíč je vypočítán z sdíleného tajemství pomocí ECDH.

Tato symetrie je umožněna komutativními a asociativními vlastnostmi operátoru XOR:

- Další vlastnosti:
  -> D ⊕ D = 0
  -> D ⊕ 0 = D

- Komutativita:
  D ⊕ E = E ⊕ D

- Asociativita:
  D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z

- Symetrie:
  Pokud: D ⊕ E = L
  Pak: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E
  -> D ⊕ L = E
Dále, tato metoda šifrování je velmi podobná Vernamově šifře (One-Time Pad), jedinému známému šifrovacímu algoritmu, který má k dnešnímu dni bezpodmínečnou (nebo absolutní) bezpečnost. Aby Vernamova šifra měla tuto charakteristiku, musí být šifrovací klíč dokonale náhodný, stejně velký jako zpráva a použit pouze jednou. V šifrovací metodě použité zde pro BIP47 je klíč skutečně stejně velký jako zpráva, slepý faktor je přesně stejně velký jako spojení x-koordinátu veřejného klíče s řetězcem kódu platebního kódu. Tento šifrovací klíč je skutečně použit pouze jednou. Tento klíč však není odvozen z dokonale náhodného zdroje, jelikož se jedná o HMAC. Je spíše pseudonáhodný. Proto to není Vernamova šifra, ale metoda je podobná.
Vraťme se k naší konstrukci notifikační transakce:

4. Alice nyní má svůj platební kód s šifrovaným obsahem. Sestaví a vysílá transakci, která zahrnuje její veřejný klíč "A" jako vstup, výstup na Bobovu notifikační adresu a výstup OP_RETURN obsahující její platební kód se šifrovaným obsahem. Tato transakce je notifikační transakce.

OP_RETURN je Opcode, což je skript, který označuje výstup Bitcoinové transakce jako neplatný. Dnes se používá k vysílání nebo ukotvení informací na Bitcoinovém blockchainu. Může uchovávat až 80 bajtů dat, která jsou zaznamenána na řetězci a tedy viditelná pro všechny ostatní uživatele.

Jak jsme viděli v předchozí části, Diffie-Hellman se používá k generování sdíleného tajemství mezi dvěma uživateli komunikujícími přes nezabezpečenou síť, kterou potenciálně sledují útočníci. V BIP47 se pro komunikaci na Bitcoinové síti, která je svou podstatou transparentní komunikační síť sledovaná mnoha útočníky, používá ECDH. Sdílené tajemství vypočítané prostřednictvím výměny klíčů Diffie-Hellman na eliptické křivce je poté použito k šifrování tajných informací k přenosu: platební kód odesílatele (Alice).

Zde je diagram extrahovaný z BIP47, který ilustruje to, co jsme právě popisovali:

![Diagram Alice posílá svůj maskovaný platební kód na Bobovu notifikační adresu](assets/16.webp)

Kredit: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Pokud porovnáme tento diagram s tím, co jsem popsal dříve:

- "Wallet Priv-Key" na straně Alice odpovídá: a.

- "Child Pub-Key 0" na straně Boba odpovídá: B.
- "Notification Shared Secret" odpovídá: f.
- "Masked Payment Code" odpovídá šifrovanému platebnímu kódu, tj. s šifrovaným obsahem: x' a c'.

- "Notification Transaction" je transakce, která obsahuje OP_RETURN.

Shrneme-li kroky, které jsme právě provedli pro provedení notifikační transakce:

- Alice získá Bobův platební kód a notifikační adresu.

- Alice vybere UTXO, které jí patří v její HD peněžence s odpovídajícím párem klíčů.

- Vypočítá tajný bod na eliptické křivce pomocí ECDH.

- Tento tajný bod použije k výpočtu HMAC, což je slepý faktor.

- Tento slepý faktor použije k šifrování obsahu svého osobního platebního kódu.

- Použije výstup transakce OP_RETURN k přenosu maskovaného platebního kódu Bobovi.

Abychom lépe pochopili jeho fungování, zejména použití OP_RETURN, pojďme společně prozkoumat skutečnou notifikační transakci. Provedl jsem takovou transakci na Testnetu, kterou můžete najít kliknutím zde:
Při pozorování této transakce můžeme již vidět, že má jediný vstup a 4 výstupy:

- První výstup je OP_RETURN, který obsahuje můj maskovaný platební kód.

- Druhý výstup 546 sats směřuje na notifikační adresu příjemce.

- Třetí výstup 15 000 sats představuje poplatek za službu, jelikož jsem použil Samourai Wallet pro sestavení této transakce.

- Čtvrtý výstup dvou milionů sats představuje zbytek, tj. zbývající rozdíl z mého vstupu, který se vrací na další mou adresu.

Nejzajímavější k prozkoumání je samozřejmě výstup 0 používající OP_RETURN. Podívejme se na něj podrobněji:

![OP_RETURN Výstup notifikační transakce BIP47](assets/18.webp)

Zdroj: https://blockstream.info/

Objevujeme hexadecimální skript výstupu:

> 6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000

V tomto skriptu můžeme rozlišit několik částí:
Mezi operátory můžeme rozpoznat 0x6a, který odkazuje na OP_RETURN a 0x4c, který odkazuje na OP_PUSHDATA1. Byte následující po tomto operátoru udává velikost následujícího payloadu. Udává 0x50, což je 80 bajtů.

Následuje platební kód s šifrovaným payloadem.

Zde je můj platební kód použitý v této transakci:

> V base 58:
>
> PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU
>
> V base 16 (HEX):
> 4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc000000000000000000000000008604e4db

Pokud porovnáme můj platební kód s OP_RETURN, můžeme vidět, že HRP (v hnědé) a kontrolní součet (v růžové) nejsou přenášeny. To je normální, jelikož tyto informace jsou určeny pro lidi.
Dále můžeme rozpoznat (zeleně) verzi (0x01), bitové pole (0x00) a paritu veřejného klíče (0x02). A na konci platebního kódu prázdné bajty černě (0x00), které umožňují doplnění do celkových 80 bajtů. Všechna tato metadata jsou přenášena v nešifrované podobě (plaintext). Nakonec můžeme pozorovat, že x-ová souřadnice veřejného klíče (modře) a řetězový kód (červeně) byly zašifrovány. To tvoří náklad platebního kódu.

### Přijetí transakce s oznámením.

Nyní, když Alice poslala Bobovi transakci s oznámením, pojďme se podívat, jak ji interpretuje.

Připomeňme si, že Bob musí být schopen přistupovat k platebnímu kódu Alice. Bez těchto informací, jak uvidíme v další části, nebude schopen odvodit páry klíčů vytvořené Alicí a tedy nebude mít přístup k jeho bitcoinům přijatým s BIP47. Zatím je náklad platebního kódu Alice zašifrován. Podívejme se společně, jak jej Bob dešifruje.

1. Bob sleduje transakce, které vytvářejí výstupy na jeho notifikační adresu.

2. Když má transakce výstup na jeho notifikační adresu, Bob ji analyzuje, zda obsahuje výstup OP_RETURN, který odpovídá standardu BIP47.

3. Pokud je první bajt nákladu OP_RETURN 0x01, Bob začne hledat možné sdílené tajemství s ECDH:

- Bob vybere veřejný klíč ve vstupu transakce. To znamená Alicin veřejný klíč pojmenovaný "A" s:

> A = a·G

- Bob vybere soukromý klíč "b" spojený s jeho osobní notifikační adresou:

> b

- Bob vypočítá tajný bod "S" (sdílené tajemství ECDH) na eliptické křivce přidáním a zdvojením bodů, aplikací svého soukromého klíče "b" na Alicin veřejný klíč "A":

> S = b·A

- Bob určí slepící faktor "f", který mu umožní dešifrovat náklad platebního kódu Alice. Stejným způsobem, jakým to Alice vypočítala dříve, Bob najde "f" aplikací HMAC-SHA512 na (x) hodnotu x-souřadnice tajného bodu "S" a na (o) UTXO spotřebované jako vstup v této notifikační transakci:

> f = HMAC-SHA512(o, x)

4. Bob interpretuje data v OP_RETURN notifikační transakce jako platební kód. Jednoduše dešifruje náklad tohoto potenciálního platebního kódu pomocí slepícího faktoru "f".

- Bob rozdělí slepící faktor "f" na dvě části: prvních 32 bajtů "f" bude "f1" a posledních 32 bajtů bude "f2".
- Bob dešifruje zašifrovanou x-souřadnici hodnotu (x') veřejného klíče platebního kódu Alice:

> x = x' XOR f1

- Bob dešifruje zašifrovanou hodnotu řetězového kódu (c') platebního kódu Alice:

> c = c' XOR f2

5. Bob kontroluje, zda je hodnota veřejného klíče platebního kódu Alice součástí skupiny secp256k1. Pokud ano, interpretuje ji jako platný platební kód. V opačném případě transakci ignoruje.

Nyní, když Bob zná platební kód Alice, může jí poslat až 2^32 plateb, aniž by kdy znovu potřeboval provést transakci s oznámením jako tato.

Proč to funguje? Jak může Bob určit stejný slepící faktor jako Alice a dešifrovat její platební kód? Podívejme se podrobněji na proces ECDH na základě toho, co jsme právě popisovali.
Za prvé se zabýváme symetrickým šifrováním. To znamená, že šifrovací klíč a dešifrovací klíč jsou stejné hodnoty. V tomto případě je klíč v transakci oznámení slepící faktor (f = f1 || f2). Alice a Bob musí získat stejnou hodnotu pro f bez přímého přenosu, protože útočník by ji mohl zachytit a dešifrovat tajné informace.
Tento slepící faktor je získán aplikací HMAC-SHA512 na dvě hodnoty: x-ovou souřadnici tajného bodu a spotřebovaný UTXO ve vstupu transakce. Bob tedy musí mít tyto dvě informace, aby mohl dešifrovat Alicein platobní kód.

Pro vstupní UTXO může Bob jednoduše získat sledováním transakce oznámení. Pro tajný bod bude muset Bob použít ECDH.

Jak je vidět v sekci o Diffie-Hellmanovi, výměnou svých veřejných klíčů a tajnou aplikací svých soukromých klíčů na veřejný klíč druhého, mohou Alice a Bob najít specifický a tajný bod na eliptické křivce. Transakce oznámení se spoléhá na tento mechanismus:

> Bobův pár klíčů:
>
> B = b·G
>
> Alicein pár klíčů:
>
> A = a·G
>
> Pro tajný bod S (x,y):
>
> S = a·B = a·b·G = b·a·G = b·A

![Diagram generování sdíleného tajemství s ECDHE](assets/19.webp)
Nyní, když Bob zná Alicein platobní kód, bude schopen detekovat její BIP47 platby a odvodit soukromé klíče blokující přijaté bitcoiny.
![Bob interpretuje Aliceinu transakci oznámení](assets/20.webp)

Zdroj: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Pokud porovnáme tento diagram s tím, co jsem vám dříve popsal:

- "Wallet Pub-Key" na straně Alice odpovídá: A.

- "Child Priv-Key 0" na straně Boba odpovídá: b.

- "Notification Shared Secret" odpovídá: f.

- "Masked Payment Code" odpovídá Aliceinu maskovanému platobnímu kódu, tj. s šifrovaným payloadem: x' a c'.

- "Notification Transaction" je transakce, která obsahuje OP_RETURN.

Dovolte mi shrnout kroky, které jsme právě společně viděli, pro přijetí a interpretaci transakce oznámení:

- Bob monitoruje výstupy transakcí na svou adresu oznámení.

- Když jednu detekuje, získá informace obsažené v OP_RETURN.

- Bob vybere veřejný klíč vstupu a vypočítá tajný bod pomocí ECDH.

- Tento tajný bod použije k výpočtu HMAC, což je slepící faktor.

- Tento slepící faktor použije k dešifrování Aliceina platobního kódu obsaženého v OP_RETURN.

### BIP47 platobní transakce.

Nyní se podívejme na platobní proces s BIP47. Připomínám vám současný stav situace:

- Alice zná Bobův platobní kód, který jednoduše získala z jeho webové stránky.

- Bob zná Alicein platobní kód díky transakci oznámení.

- Alice provede první platbu Bobovi. Může provést mnoho dalších stejným způsobem.

Než vám tento proces vysvětlím, myslím, že je důležité připomenout vám, na kterých indexech aktuálně pracujeme:

Popisujeme cestu derivace platobního kódu takto: m/47'/0'/0'/. 

Další hloubka distribuuje indexy následovně:
- První normální (nepevnější) dětský pár se používá k vygenerování notifikační adresy, o které jsme diskutovali v předchozí sekci: m/47'/0'/0'/0/.
- Normální dětské klíčové páry se používají v rámci ECDH k generování přijímacích adres plateb BIP47, jak uvidíme v této sekci: m/47'/0'/0'/ od 0 do 2,147,483,647/.

- Pevnější dětské klíčové páry jsou efemérní platební kódy: m/47'/0'/0'/ od 0' do 2,147,483,647'/.
  Pokaždé, když Alice chce poslat platbu Bobovi, odvodí novou jedinečnou prázdnou adresu, opět díky protokolu ECDH:
- Alice vybere první soukromý klíč odvozený z jejího osobního opakovaně použitelného platebního kódu:

> a

- Alice vybere první nepoužitý veřejný klíč odvozený z Bobova platebního kódu. Tento veřejný klíč, nazveme ho "B". Je spojen se soukromým klíčem "b", který zná pouze Bob.

> B = b·G

- Alice vypočítá tajný bod "S" na eliptické křivce přidáním a zdvojením bodů, aplikací svého soukromého klíče "a" na Bobův veřejný klíč "B":

> S = a·B

- Z tohoto tajného bodu Alice vypočítá sdílené tajemství "s" (malé písmeno). K tomu vybere x-ovou souřadnici tajného bodu "S" nazvanou "Sx", a tuto hodnotu předá do hashovací funkce SHA256.

> s = SHA256(Sx)

Nevěřte. Ověřte! Pokud chcete pochopit základní principy hashovací funkce, najdete, co potřebujete, v tomto článku. A pokud nedůvěřujete NIST (máte pravdu), a chcete být schopni podrobně pochopit, jak SHA256 funguje, vše vysvětluji v tomto článku ve francouzštině.

- Alice použije toto sdílené tajemství "s" k vypočítání přijímací adresy Bitcoinu. Nejprve zkontroluje, že "s" je v rámci řádu křivky secp256k1. Pokud ne, zvýší index Bobova veřejného klíče, aby odvodila další sdílené tajemství.

- Za druhé, vypočítá veřejný klíč "K0" přidáním bodů "B" a "s·G" na eliptické křivce. Jinými slovy, Alice přidá veřejný klíč odvozený z Bobova platebního kódu "B" s dalším bodem vypočítaným na eliptické křivce přidáním a zdvojením bodů se sdíleným tajemstvím "s" z generátorového bodu křivky secp256k1 "G". Tento nový bod představuje veřejný klíč, a nazýváme ho "K0":

> K0 = B + s·G

- S tímto veřejným klíčem "K0" může Alice odvodit prázdnou přijímací adresu standardním způsobem (například SegWit V0 v Bech32).

Jakmile má Alice tuto přijímací adresu "K0" patřící Bobovi, může sestavit standardní Bitcoinovou transakci výběrem UTXO, které jí patří na jiné větvi její HD peněženky, a utratit ji na Bobovu adresu "K0".

![Alice posílá bitcoiny s BIP47 Bobovi](assets/21.webp)

Kredit: Opakovaně použitelné platební kódy pro hierarchické deterministické peněženky, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
Pokud toto schéma porovnáme s tím, co jsem vám dříve popsal:

- "Child Priv-Key" na straně Alice odpovídá: a.
- "Child Pub-Key 0" na straně Boba odpovídá: B.
- "Payment Secret 0" odpovídá: s.
- "Platební veřejný klíč 0" odpovídá: K0.
Dovolte mi shrnout kroky, které jsme právě společně provedli pro odeslání platby BIP47:

- Alice vybere první odvozený soukromý klíč dítěte ze svého osobního platebního kódu.
- Pomocí ECDH vypočítá tajný bod na eliptické křivce z prvního nepoužitého odvozeného veřejného klíče dítěte z Bobova platebního kódu.
- Tento tajný bod použije k výpočtu sdíleného tajemství pomocí SHA256.
- Toto sdílené tajemství použije k výpočtu nového tajného bodu na eliptické křivce.
- Tento nový tajný bod přičte k Bobovu veřejnému klíči.
- Získá nový efemérní veřejný klíč, pro který má pouze Bob přidružený soukromý klíč.
- Alice může Bobovi poslat běžnou transakci na odvozenou efemérní přijímací adresu.

Pokud chce provést druhou platbu, opakuje výše uvedené kroky, s výjimkou toho, že vybere druhý odvozený veřejný klíč z Bobova platebního kódu. To znamená další nepoužitý klíč. Poté bude mít druhou přijímací adresu patřící Bobovi, "K1".

![Alice odvozuje tři BIP47 přijímací adresy pro Boba](assets/22.webp)

Kredit: Opakovaně použitelné platební kódy pro hierarchické deterministické peněženky, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Může takto pokračovat a odvodit až 2^32 prázdných adres patřících Bobovi.

Z externího pohledu, pozorováním Bitcoin blockchainu, je teoreticky nemožné odlišit platbu BIP47 od běžné platby. Zde je příklad transakce platby BIP47 na Testnetu:

https://blockstream.info/testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

TXID:

> 94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

Vypadá to jako běžná transakce se spotřebovaným vstupem, výstupem platby 210,000 sats a změnou.

![Bitcoinová platební transakce s BIP47](assets/23.webp)

Kredit: https://blockstream.info/

### Přijetí platby BIP47 a odvození soukromého klíče.

Alice právě provedla svou první platbu na prázdnou BIP47 adresu vlastněnou Bobem. Nyní se podívejme, jak Bob tuto platbu přijme. Uvidíme také, proč Alice nemá přístup k soukromému klíči adresy, kterou právě vygenerovala, a jak Bob tento klíč získá, aby utratil právě přijaté bitcoiny.

Jakmile Bob obdrží od Alice notifikační transakci, odvodí BIP47 veřejný klíč "K0" ještě předtím, než jí na něj pošle jakoukoliv platbu. Proto sleduje jakoukoliv platbu na přidruženou adresu. Ve skutečnosti okamžitě odvodí několik adres, které bude sledovat (K0, K1, K2, K3...). Zde je způsob, jakým odvodí tento veřejný klíč "K0":

- Bob vybere první odvozený soukromý klíč dítěte ze svého platebního kódu. Tento soukromý klíč se jmenuje "b". Je spojen s veřejným klíčem "B", který Alice použila v předchozím kroku:

> b

- Bob vybere první odvozený veřejný klíč Alice z jejího platebního kódu. Tento klíč se jmenuje "A". Je spojen s soukromým klíčem "a", který Alice použila ve svých výpočtech a o kterém ví pouze Alice. Bob může tento proces provést, protože zná Alicein platební kód, který mu byl předán s notifikační transakcí.

> A = a·G
- Bob vypočítá tajný bod "S" přidáním a zdvojením bodů na eliptické křivce, aplikuje svůj soukromý klíč "b" na veřejný klíč Alice "A". Zde používáme ECDH, což zaručuje, že tento bod "S" bude stejný jak pro Boba, tak pro Alici.
> S = b·A

- Stejně jako Alice, Bob izoluje x-souřadnici tohoto bodu "S". Tuto hodnotu jsme pojmenovali "Sx". Tuto hodnotu propustí funkcí SHA256, aby našel sdílené tajemství "s" (malé písmeno).

> s = SHA256(Sx)

- Stejným způsobem jako Alice, Bob vypočítá bod "s·G" na eliptické křivce. Poté přidá tento tajný bod ke svému veřejnému klíči "B". Poté získá nový bod na eliptické křivce, který interpretuje jako veřejný klíč "K0":

> K0 = B + s·G

Jakmile Bob má tento veřejný klíč "K0", může odvodit přidružený soukromý klíč, aby mohl utratit své bitcoiny. On je jediný, kdo může tento číslo vygenerovat.

- Bob přidá svůj odvozený dětský soukromý klíč "b" ze svého osobního platebního kódu. On je jediný, kdo může získat hodnotu "b". Poté přidá "b" k sdílenému tajemství "s", aby získal k0, soukromý klíč K0:

> k0 = b + s
> Díky zákonu skupiny eliptické křivky Bob získá přesně soukromý klíč odpovídající veřejnému klíči použitému Alicí. Takže máme:
> K0 = k0·G

![Bob generuje své přijímací adresy BIP47](assets/24.webp)

Kredit: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Pokud porovnáme tento diagram s tím, co jsem vám dříve popsal:

- "Child Priv-Key 0" na straně Boba odpovídá: b.

- "Child Pub-Key 0" na straně Alice odpovídá: A.

- "Payment Secret 0" odpovídá: s.

- "Payment Pub-Key 0" odpovídá: K0.

- "Payment Priv-Key 0" odpovídá: k0.

Shrneme-li kroky, které jsme právě společně viděli pro přijetí platby BIP47 a výpočet odpovídajícího soukromého klíče:

- Bob vybere první odvozený dětský soukromý klíč ze svého osobního platebního kódu.

- Vypočítá tajný bod na eliptické křivce pomocí ECDH z prvního odvozeného dětského veřejného klíče z řetězového kódu Alice.

- Tento tajný bod použije k výpočtu sdíleného tajemství pomocí SHA256.

- Toto sdílené tajemství použije k výpočtu nového tajného bodu na eliptické křivce.

- Přidá tento nový tajný bod ke svému osobnímu veřejnému klíči.

- Získá nový efemerní veřejný klíč, na který Alice pošle svou první platbu.

- Bob vypočítá soukromý klíč spojený s tímto efemerním veřejným klíčem přidáním svého odvozeného dětského soukromého klíče ze svého platebního kódu a sdíleného tajemství.

Protože Alice nemůže získat "b", Bobův soukromý klíč, není schopna určit k0, soukromý klíč spojený s Bobovou přijímací adresou BIP47.

Schématicky můžeme reprezentovat výpočet sdíleného tajemství "S" takto:

![Výpočet sdíleného tajemství s ECDHE](assets/25.webp)

Jakmile je sdílené tajemství nalezeno s ECDH, Alice a Bob vypočítají veřejný klíč platby BIP47 "K0" a Bob také vypočítá přidružený soukromý klíč "k0":
![Odvození přijímací adresy BIP47 ze sdíleného tajemství](assets/26.webp)
### Vrácení platby BIP47.

Jelikož Bob zná opakovaně použitelný platební kód Alice, má již veškeré potřebné informace k tomu, aby jí poslal vrácení peněz. Nebude potřebovat kontaktovat Alici, aby požádal o jakékoli informace. Jednoduše ji upozorní pomocí notifikační transakce, zejména aby mohla obnovit své adresy BIP47 pomocí svého seedu, a poté jí může také poslat až 2^32 plateb.
Bob může Alici vrátit peníze stejným způsobem, jakým jí posílal platby. Role jsou obrácené:

![Bob posílá vrácení peněz Alici s BIP47](assets/27.webp)

Kredit: Opakovaně použitelné platební kódy pro hierarchické deterministické peněženky, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Nyní znáte všechny klady a zápory této úžasné řešení, které BIP47 představuje.

## Odvozená použití PayNym.

Implementace tohoto BIP47 v peněžence Samourai vedla k vytvoření PayNyms, identifikátorů vypočítaných z platebních kódů uživatelů. Dnes jejich užitečnost daleko přesahuje použití BIP47.

Tým Samourai postupně vyvíjí celý ekosystém nástrojů a služeb založených na PayNym uživatele. Mezi tyto patří samozřejmě všechny nástroje pro utrácení, které umožňují optimalizovat soukromí uživatele přidáním entropie do transakce a tím i přidáním věrohodného popření.

Společné použití Sorobanu, šifrované komunikační sítě založené na Toru, a PayNyms výrazně optimalizovalo uživatelskou zkušenost při sestavování spolupracujících transakcí, přičemž udrželo dobrý stupeň bezpečnosti. Je tak snadné provádět transakce Stowaway (PayJoin) a StonewallX2 bez nutnosti ručně provádět mnoho výměn nepodepsaných transakcí potřebných k nastavení takové spolupracující transakce.

Na rozdíl od použití BIP47, protože tyto spolupracující transakce nevyžadují notifikační transakci, stačí propojit PayNyms k použití těchto nástrojů. Není potřeba je spojovat.

Pokud se chcete dozvědět více o spolupracujících transakcích a obecněji o všech nástrojích pro utrácení peněženky Samourai, můžete si přečíst sekci "Nástroje pro utrácení" v tomto článku. Najdete zde technické vysvětlení a podrobný tutoriál pro každý nástroj.

Kromě těchto spolupracujících transakcí bylo nedávno pozorováno, že tým Samourai pracuje na protokolu autentizace spojeném s PayNym: Auth47. Tento nástroj je již implementován a umožňuje například autentizaci s PayNym na webové stránce, která tuto metodu akceptuje. V budoucnu si myslím, že mimo tuto možnost autentizace na webu bude Auth47 součástí většího projektu kolem ekosystému BIP47/PayNym/Samourai. Možná tento protokol bude použit k další optimalizaci uživatelské zkušenosti s peněženkou Samourai, zejména při používání nástrojů pro utrácení. Uvidíme...

## Můj osobní názor na BIP47.

Zřejmě hlavní nevýhodou BIP47 je notifikační transakce. Nutí uživatele platit poplatky za její těžbu, což může být pro některé otravné. Avšak argument "spam" na blockchainu Bitcoinu je naprosto nepřijatelný. Každý, kdo platí poplatky za svou transakci, by měl mít možnost ji zaznamenat do účetní knihy, bez ohledu na její účel. Tvrdit opak je podporovat cenzuru.

Je možné, že v budoucnu budou nalezena méně nákladná řešení, jak komunikovat platební kód odesílatele příjemci a pro bezpečné uložení příjemcem. Ale zatím zůstává notifikační transakce řešením s nejméně kompromisy.
Tato nevýhoda zůstává zanedbatelná, když zvážíme všechny výhody BIP47. Ze všech existujících návrhů na řešení problému opakovaného používání adres se mi jeví jako nejlepší řešení.
Jak bylo vysvětleno dříve, většina opakovaného používání adres pochází od směnáren. BIP47 je jediné rozumné řešení, které tento problém řeší přímo u zdroje. Jakýkoliv návrh, který má za cíl snížit počet opakovaných použití adres, by se měl zaměřit na tento aspekt a přizpůsobit řešení hlavnímu zdroji problému.

Z hlediska použitelnosti, ačkoliv jsou jeho vnitřní mechanismy poměrně složité, je postup platby BIP47 přímý. Opakovaně použitelné platební kódy tak mohou být snadno přijaty i začínajícími uživateli.

Z hlediska soukromí je BIP47 velmi zajímavý. Jak jsem vysvětlil v sekci o transakci oznámení, platební kód neodhaluje žádné informace o odvozených efemérních adresách. Tím pádem přerušuje tok informací mezi bitcoinovou transakcí a identifikátorem příjemce, na rozdíl od tradičního používání přijímací adresy.

A především, implementace PayNym BIP47 funguje! Je dostupná v peněžence Samourai Wallet od roku 2016 a ve Sparrow Wallet od začátku tohoto roku. Nejedná se o vědecký projekt, ale o řešení, které bylo včera otestováno a dnes je plně funkční.

Doufejme, že v budoucnu budou tyto opakovaně použitelné platební kódy přijaty aktéry ekosystému, implementovány do softwaru peněženek a používány bitcoinisty.

Jakékoliv opravdu pozitivní řešení pro soukromí uživatelů musí být diskutováno, prosazováno a bráněno, aby se Bitcoin nestal hřištěm certifikačních autorit a nástrojem vládního dohledu.
Přemýšlel o tom, jak byl všude pronásledován a urážen, a nyní slyšel všechny říkat, že je nejkrásnější ze všech těchto krásných ptáků! A dokonce i bez černý skláněl své větve směrem k němu a slunce rozšířilo tak teplé a laskavé světlo! Poté mu peří nafouklo, jeho štíhlý krk se narovnal a z celého srdce zvolal: "Jak jsem si mohl snít o tolika štěstí, když jsem byl jen ošklivé malé káčátko."

## Pro další studium:

- Porozumění a používání CoinJoin na Bitcoinu.

- Porozumění odvozovacím cestám bitcoinové peněženky.

- Instalace a používání vašeho Bitcoinového uzlu RoninDojo.

### Externí zdroje a poděkování:

Děkuji LaurentMT a Théo Pantamis za mnoho konceptů, které mi vysvětlili a které jsem použil v tomto článku. Doufám, že jsem je přesně předal.

Děkuji Fanis Michalakis za korekturu tohoto textu a jeho odborné rady.

- https://bitcoiner.guide/paynym/
- https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%20points,a%20type%20of%20algebraic%20curve).
- https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060
- https://ee.stanford.edu/~hellman/publications/24.pdf
- https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols