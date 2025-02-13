---
name: RGB CLI
description: Jak mohu v systému RGB vytvářet a vyměňovat chytré smlouvy?
---
![cover](assets/cover.webp)

V tomto tutoriálu budeme postupovat krok za krokem při psaní smlouvy pomocí nástroje příkazového řádku `rgb` vytvořeného sdružením LNP/BP. Cílem je ukázat, jak nainstalovat a manipulovat s CLI, zkompilovat schéma, importovat rozhraní a implementaci rozhraní a poté vystavit aktivum RGB. Podíváme se také na základní logiku, včetně kompilace a ověřování stavu. Na konci tohoto tutoriálu byste měli být schopni reprodukovat tento proces a vytvořit vlastní smlouvy RGB.

## Připomenutí protokolu RGB

RGB je protokol, který běží nad Bitcoinem a napodobuje funkce chytrých smluv a správu digitálních aktiv, aniž by přetěžoval blockchain, na kterém je založen. Na rozdíl od běžných on-chain chytrých smluv (jako například na Ethereu) se RGB spoléhá na systém "*Client-side validation*": většinu dat a historie stavů si vyměňují a ukládají výhradně zúčastnění účastníci, zatímco v blockchainu Bitcoinu se nacházejí pouze malé kryptografické závazky (prostřednictvím mechanismů jako *Tapret* nebo *Opret*). V protokolu RGB tedy bitcoinový blockchain slouží pouze jako server pro časové razítkování a systém ochrany proti dvojímu utrácení.

Smlouva RGB je strukturována jako evoluční stavový stroj. Začíná Genesis, která definuje počáteční stav (popisující například nabídku, ticker nebo jiná metadata) podle striktně typovaného a sestaveného Schema. Poté se použijí stavové přechody a v případě potřeby stavová rozšíření, aby se tento stav upravil nebo rozšířil. Každá operace, ať už jde o převod zastupitelných aktiv (RGB20), nebo o vytvoření jedinečných aktiv (RGB21), zahrnuje *Jednorázové pečetě*. Ty propojují bitcoinové UTXO se stavy mimo řetězec a zabraňují dvojímu utrácení, přičemž zajišťují důvěrnost a škálovatelnost.

Chcete-li se dozvědět více o tom, jak protokol RGB funguje, doporučuji vám absolvovat toto komplexní školení:

https://planb.network/courses/csv402
Vnitřní logika RGB je založena na knihovnách Rust, které můžete jako vývojáři importovat do svých projektů a spravovat tak část *Ověřování na straně klienta*. Kromě toho tým LNP/BP pracuje na vazbách pro další jazyky, ale to ještě není dokončeno. Kromě toho další subjekty, jako například Bitfinex, vyvíjejí své vlastní integrační balíčky, ale o těch si povíme v jiném tutoriálu. Prozatím je oficiálním odkazem `rgb` CLI, i když zůstává relativně nedoladěný.

## Instalace a prezentace nástroje rgb CLI

Hlavní příkaz se nazývá jednoduše `rgb`. Je navržen tak, aby připomínal `git`, se sadou dílčích příkazů pro manipulaci se smlouvami, jejich vyvolávání, vydávání aktiv atd. Bitcoinová peněženka není v současné době integrována, ale bude v nejbližší verzi (0.11). Tato příští verze umožní uživatelům vytvářet a spravovat peněženky (prostřednictvím deskriptorů) přímo z `rgb`, včetně generování PSBT, kompatibility s externím hardwarem (např. hardwarovou peněženkou) pro podepisování a interoperability se softwarem, jako je Sparrow. Tím se zjednoduší celý scénář vydávání a převodu aktiv.

### Instalace prostřednictvím služby Cargo

Nástroj nainstalujeme v jazyce Rust pomocí :

```bash
cargo install rgb-contracts --all-features
```

(Poznámka: bedna se jmenuje `rgb-contracts` a nainstalovaný příkaz se bude jmenovat `rgb`. Pokud by bedna s názvem `rgb` již existovala, mohlo by dojít ke kolizi, proto ten název)

Instalace kompiluje velké množství závislostí (např. parsování příkazů, integrace Electrum, správa důkazů nulové znalosti atd.).

Po dokončení instalace se spustí :

```bash
rgb
```

Při spuštění příkazu `rgb` (bez argumentů) se zobrazí seznam dostupných dílčích příkazů, například `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer` atd. Můžete změnit adresář místního úložiště (skrýš, která obsahuje všechny protokoly, schémata a implementace), vybrat síť (testnet, mainnet) nebo nakonfigurovat server Electrum.

![RGB-CLI](assets/fr/01.webp)

### První přehled kontrol

Když spustíte následující příkaz, uvidíte, že rozhraní `RGB20` je již ve výchozím nastavení integrováno:

```bash
rgb interfaces
```

Pokud toto rozhraní není integrováno, klonujte :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Zkompilujte ji:

```bash
cargo run
```

Poté importujte vybrané rozhraní:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-CLI](assets/fr/02.webp)

Bylo nám však řečeno, že do softwaru zatím nebylo importováno žádné schéma. V úložišti není ani žádná smlouva. Chcete-li si ji prohlédnout, spusťte příkaz :

```bash
rgb schemata
```

Poté můžete úložiště klonovat a získat určitá schémata:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-CLI](assets/fr/03.webp)

Toto úložiště obsahuje v adresáři `src/` několik souborů Rust (například `nia.rs`), které definují schémata (NIA pro "*Non Inflatable Asset*", UDA pro "*Unique Digital Asset*" atd.). Pro kompilaci pak můžete spustit příkaz :

```bash
cd rgb-schemata
cargo run
```

Tím se vygeneruje několik souborů `.rgb` a `.rgba` odpovídajících sestaveným schématům. Najdete zde například soubor `NonInflatableAsset.rgb`.

### Import schématu a implementace rozhraní

Nyní můžete schéma importovat do `rgb` :

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-CLI](assets/fr/04.webp)

Tím se přidá do místní zásoby. Pokud spustíme následující příkaz, uvidíme, že se schéma nyní zobrazí:

```bash
rgb schemata
```

## Vytvoření smlouvy (vystavení)

Existují dva přístupy k vytvoření nového aktiva:


- Buď použijeme skript, nebo kód v jazyce Rust, který sestaví smlouvu vyplněním polí schématu (globální stav, Vlastní stavy atd.) a vytvoří soubor `.rgb` nebo `.rgba`;
- Nebo použijte přímo dílčí příkaz `issue` se souborem YAML (nebo TOML) popisujícím vlastnosti tokenu.

Ve složce `examples` najdete příklady v jazyce Rust, které ukazují, jak sestavit `ContractBuilder`, vyplnit `globální stav` (název aktiva, ticker, dodávku, datum atd.), definovat Vlastní stav (ke kterému UTXO je přiřazen), a pak to vše zkompilovat do *kontraktní zásilky*, kterou můžete exportovat, validovat a importovat do skrýše.

Druhým způsobem je ruční úprava souboru YAML pro přizpůsobení `tickeru`, `jména`, `dodávky` atd. Předpokládejme, že se soubor jmenuje `RGB20-demo.yaml`. Můžete zadat :


- `spec`: ticker, name, precision ;
- `terms`: pole pro právní upozornění ;
- `issuedSupply` : množství vydaných tokenů ;
- `assignments`: označuje jednorázovou plombu (*definice plomby*) a odemčené množství.

Zde je příklad souboru YAML, který je třeba vytvořit:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-CLI](assets/fr/05.webp)

Pak jednoduše spusťte příkaz :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-CLI](assets/fr/06.webp)

V mém případě je jedinečný identifikátor schématu (uzavřený v jednoduchých uvozovkách) `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` a neuvedl jsem žádného vydavatele. Takže moje objednávka je :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Pokud ID schématu neznáte, spusťte příkaz :

```bash
rgb schemata
```

CLI odpoví, že byla vydána nová smlouva a přidána do zásoby. Pokud zadáme následující příkaz, uvidíme, že nyní existuje další smlouva, která odpovídá právě vydané smlouvě:

```bash
rgb contracts
```

![RGB-CLI](assets/fr/07.webp)

Další příkaz pak zobrazí globální stavy (jméno, ticker, nabídka...) a seznam vlastněných stavů, tj. alokací (například 1 milion tokenů `PBN` definovaných v UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-CLI](assets/fr/08.webp)

## Export, import a validace

Chcete-li tuto smlouvu sdílet s ostatními uživateli, můžete ji exportovat ze skrýše do souboru :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-CLI](assets/fr/09.webp)

Soubor `myContractPBN.rgb` lze předat jinému uživateli, který jej může přidat do své skrýše příkazem :

```bash
rgb import myContractPBN.rgb
```

Pokud se jedná o jednoduchou *smluvní zásilku*, zobrazí se při importu zpráva "`Importuji zásilku rgb`". Pokud se jedná o větší *přechodovou zásilku*, bude příkaz jiný (`rgb accept`).

K zajištění platnosti můžete také použít funkci místní validace. Můžete například spustit funkci :

```bash
rgb validate myContract.rgb
```

### Používání, ověřování a zobrazování zásob

Připomínáme, že úložiště je lokální inventář schémat, rozhraní, implementací a kontraktů (Genesis + přechody). Pokaždé, když spustíte příkaz "import", přidáte do zásobníku prvek. Tuto skrýš si můžete podrobně prohlédnout příkazem :

```bash
rgb dump
```

![RGB-CLI](assets/fr/10.webp)

Tím se vygeneruje složka s podrobnostmi o celé skrýši.

## Převod a PSBT

Chcete-li provést převod, musíte manipulovat s místní peněženkou Bitcoin, abyste mohli spravovat závazky `Tapret` nebo `Opret`.

### Vytvořit fakturu

Ve většině případů probíhá interakce mezi účastníky smlouvy (např. Alicí a Bobem) prostřednictvím vystavení faktury. Pokud Alice chce, aby Bob něco provedl (převod tokenu, reissue, akci v DAO atd.), Alice vytvoří fakturu s podrobnými instrukcemi pro Boba. Máme tedy :


- Alice** (vystavitel faktury) ;
- Bob** (který přijímá a provádí fakturaci).

Na rozdíl od jiných ekosystémů není faktura RGB omezena na pojem platby. Může obsahovat jakýkoli požadavek spojený se smlouvou: odvolání klíče, hlasování, vytvoření rytiny (*rytiny*) na NFT atd. Příslušnou operaci lze popsat v rozhraní smlouvy. Odpovídající operaci lze popsat v rozhraní smlouvy.

Následující příkaz vygeneruje fakturu RGB:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

S :


- `$CONTRACT`: Identifikátor smlouvy (*ContractId*) ;
- `$INTERFACE`: použité rozhraní (např. `RGB20`) ;
- `$ACTION`: název operace zadané v rozhraní (pro jednoduchý přenos tokenu to může být "Transfer"). Pokud rozhraní již poskytuje výchozí akci, nemusíte ji zde znovu zadávat;
- `$STATE`: stavové údaje, které se mají přenést (například množství tokenů, pokud se přenáší zastupitelný token);
- `$SEAL`: jednorázová pečeť příjemce (Alice), tj. explicitní odkaz na UTXO. Bob použije tuto informaci k sestavení svědecké transakce a odpovídající výstup pak bude patřit Alici (v *zaslepené UTXO* nebo nezašifrované podobě).

Například pomocí následujících příkazů

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

CLI vygeneruje fakturu jako :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Bobovi ji lze předat jakýmkoli kanálem (text, QR kód atd.).

### Provedení převodu

Převod z této faktury :


- Bob (který má žetony ve své skrýši) má peněženku Bitcoin. Potřebuje připravit bitcoinovou transakci (ve formě PSBT, např. `tx.psbt`), která utratí UTXO, v nichž se nacházejí požadované RGB tokeny, plus jedno UTXO pro měnu (směnu) ;
- Bob provede následující příkaz:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Tím se vygeneruje soubor `consignment.rgb`, který obsahuje :
 - Historie přechodu prokazuje Alici, že žetony jsou pravé;
 - Nový přechod, který přenáší žetony do Alenčiny jednorázové pečeti ;
 - Svědecká transakce (nepodepsaná).
- Bob odešle tento soubor `consignment.rgb` Alici (e-mailem, prostřednictvím serveru pro sdílení nebo protokolu RGB-RPC, Storm atd.);
- Alice obdrží soubor `consignment.rgb` a přijme jej do své vlastní zásoby:

```bash
alice$ rgb accept consignment.rgb
```


- CLI zkontroluje platnost přechodu a přidá jej do Aliciny zásoby. Pokud je neplatný, příkaz selže s podrobným chybovým hlášením. V opačném případě uspěje a oznámí, že vzorová transakce ještě nebyla vysílána do sítě Bitcoin (Bob čeká na Alicino zelené světlo);
- Jako potvrzení vrátí příkaz `přijmout` podpis (*výplatní pásku*), který může Alice odeslat Bobovi, aby mu ukázala, že potvrdila platnost *zaslání* ;
- Bob pak může podepsat a zveřejnit (`--publish`) svou transakci Bitcoin:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Jakmile je tato transakce potvrzena v řetězci, vlastnictví aktiva se považuje za převedené na Alici. Alicina peněženka, která sleduje těžbu transakce, vidí, že se v její skrýši objevil nový vlastněný stát.

Nyní víte, jak vystavit a převést smlouvu RGB. Pokud se vám tento návod zdál užitečný, budu vám velmi vděčný, když mi níže dáte zelený palec. Neváhejte tento článek sdílet na svých sociálních sítích. Moc vám děkuji!

Doporučuji také tento další tutoriál, ve kterém vysvětluji, jak spustit uzel Lightning kompatibilní s RGB a vyměňovat tokeny téměř okamžitě:

https://planb.network/tutorials/node/rgb/rln-ffc02528-329b-4e16-bd83-873d0299feea