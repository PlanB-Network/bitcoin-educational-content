---
name: Robosats

description: Jak používat Robosats
---

![cover](assets/cover.webp)

RoboSats (https://learn.robosats.com/) je jednoduchý způsob, jak soukromě směňovat Bitcoin za národní měny. Zjednodušuje zkušenost s peer-to-peer obchodováním a využívá lightning hold faktury k minimalizaci potřeby držení a důvěry.

![video](https://youtu.be/XW_wzRz_BDI)

## Průvodce

> Tento průvodce je od Bitocin Q&A (https://bitcoiner.guide/robosats/). Veškerá zásluha patří jemu, podpořte ho tam (https://bitcoiner.guide/contribute); BitcoinQ&A je také bitcoinový mentor. Kontaktujte ho pro mentoring!

![image](assets/0.webp)

RoboSats - Jednoduchá a soukromá Lightning založená P2P směnárna

## Před začátkem

### Věci, které potřebujete vědět

| Pojem        | Definice                                                                                                                                                                                     |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | Vaše automaticky generovaná soukromá obchodní identita. Nepoužívejte stejného robota více než jednou, protože to může snížit vaše soukromí.                                                   |
| Token        | Řetězec náhodných znaků použitý k vygenerování vašeho jedinečného robota.                                                                                                                     |
| Maker        | Uživatel, který vytvoří nabídku na koupi nebo prodej Bitcoinu.                                                                                                                                |
| Taker        | Uživatel, který přijme nabídku jiného uživatele na koupi nebo prodej Bitcoinu.                                                                                                                |
| Bond         | Částka Bitcoinu uzamčená oběma stranami jako záruka férové hry a dokončení jejich části obchodu. Bondy jsou typicky 3% z celkové částky obchodu a jsou zajištěny Hodl fakturami.              |
| Trade Escrow | Používá se prodávajícím jako způsob držení obchodní částky Bitcoinu, opět s použitím Hodl faktur.                                                                                              |
| Poplatky     | RoboSats účtuje 0,2% z obchodní částky, která je rozdělena mezi oba, maker a taker. Taker platí 0,175% a maker platí 0,025%.                                                                  |

## Věci, které potřebujete mít

### Lightning peněženka

RoboSats je nativně Lightning, takže budete potřebovat Lightning peněženku k financování bond a přijetí zakoupených sats jako kupující. Při výběru vaší peněženky byste měli být opatrní, kvůli technologii použité k fungování RoboSats nejsou všechny kompatibilní.

Pokud provozujete vlastní uzel, Zeus je zdaleka nejlepší volba. Pokud nemáte vlastní uzel, doporučuji Phoenix, mobilní peněženku pro různé platformy s jednoduchým nastavením a přístupem k Lightning. Phoenix byl použit při tvorbě tohoto průvodce.

### Nějaké Bitcoiny

Kupující i prodávající musí financovat bond před jakýmkoli obchodem. Obvykle se jedná o velmi malou částku (~3% z obchodní částky), ale je to předpoklad.

Používáte RoboSats k nákupu vašich prvních sats? Proč si od přítele nepůjčit malou potřebnou částku, abyste mohli začít!? Pokud jste na to sami, zde jsou některé další skvělé možnosti, jak získat nějaké noKYC sats a začít.

### Přístup k RoboSats

Samozřejmě budete potřebovat přístup k RoboSats! Existují čtyři hlavní způsoby, jak toho dosáhnout:

1. Přes Tor Browser (Doporučeno!)
2. Přes běžný webový prohlížeč (Nedoporučeno!)
3. Přes Android APK
4. Váš vlastní klient

Pokud jste noví v používání Tor prohlížeče, dozvíte se více a stáhněte si ho [zde](https://www.torproject.org/download/).
Rychlá poznámka pro uživatele iOS, kteří chtějí přistupovat k RoboSats přes Tor z jejich telefonů. 'Onion Browser' není Tor Browser. Místo toho použijte Orbot + Safari a Orbot + DuckDuckGo.
## Nákup Bitcoinu

Následující kroky byly provedeny v květnu 2023 s použitím verze 0.5.0, přistupováno přes Tor prohlížeč. Kroky by měly být identické pro uživatele přistupující k RoboSats přes Android APK.

V době psaní RoboSats stále prochází aktivním vývojem, takže rozhraní se může v budoucnu trochu změnit, ale základní kroky potřebné k dokončení obchodu by měly zůstat v podstatě nezměněné.

> Když poprvé načtete RoboSats, objeví se tato úvodní stránka. Klikněte na Start.

![obrázek](assets/2.webp)

Vygenerujte svůj token a uložte ho na bezpečné místo, jako je aplikace pro šifrované poznámky nebo správce hesel. Tento token lze použít k obnovení vaší dočasné Robot ID v případě, že váš prohlížeč nebo aplikace se vypne uprostřed obchodu.

![obrázek](assets/3.webp)

Seznamte se se svou novou Robot identitou, poté klikněte na Pokračovat.

![obrázek](assets/4.webp)

Klikněte na Nabídky pro prohlížení knihy objednávek. Na vrchu stránky poté můžete filtrovat podle svých preferencí. Nezapomeňte si všímat procent záruk a prémie nad průměrným směnným kurzem.

- Vyberte Koupit
- Vyberte svou měnu
- Vyberte svou platební metodu(y)

![obrázek](assets/5.webp)

> Klikněte na nabídku, kterou byste chtěli přijmout. Zadejte částku (ve vaší vybrané fiat měně), kterou byste chtěli koupit od prodejce, poté si ještě jednou zkontrolujte detaily a klikněte na Přijmout objednávku.

Pokud prodejce není online (označeno červeným bodem na jeho profilovém obrázku), uvidíte varování, že obchod může trvat déle než obvykle. Pokud pokračujete a prodejce nepostupuje včas, budete kompenzováni 50% z jeho záruční částky za váš promarněný čas.

![obrázek](assets/6.webp)

Dále musíte uzamknout svou obchodní záruku zaplacením faktury na obrazovce. Jedná se o držící fakturu, která zamrzne ve vaší peněžence. Bude účtována pouze v případě, že nedokončíte svou část obchodu.

![obrázek](assets/7.webp)

Ve vaší Lightning peněžence naskenujte QR kód a zaplaťte fakturu.

![obrázek](assets/8.webp)

Dále ve vaší Lightning peněžence vygenerujte fakturu na zobrazenou částku a vložte ji do poskytnutého prostoru.

![obrázek](assets/9.webp)

Počkejte, až prodejce uzamkne svou obchodní částku. Když k tomu dojde, RoboSats automaticky přejde k dalšímu kroku, kde se otevře okno chatu. Pozdravte a požádejte prodejce o jeho informace pro fiat platbu. Jakmile je poskytnou, odešlete platbu vybranou metodou a potvrďte to v RoboSats. Veškerý chat v RoboSats je šifrován PGP, což znamená, že zprávy mohou číst pouze vy a váš obchodní partner.

![obrázek](assets/10.webp)

Jakmile prodejce potvrdí přijetí platby, RoboSats automaticky uvolní platbu pomocí dříve poskytnuté faktury.

![obrázek](assets/11.webp)

Když je faktura zaplacena, obchod je dokončen a vaše záruka je odemčena. Poté uvidíte shrnutí obchodu.

![obrázek](assets/12.webp)

Zkontrolujte svou Lightning peněženku pro potvrzení, že sats dorazily.

![obrázek](assets/13.webp)

## Další funkce

Kromě zjevného nákupu a prodeje Bitcoinu má RoboSats několik dalších funkcí, o kterých byste měli vědět.
Robot Garage
Chcete mít současně otevřené více obchodů, ale nechcete sdílet stejnou identitu napříč nimi? Žádný problém! Klikněte na záložku Robot, vygenerujte dalšího Robota a vytvořte nebo přijměte další objednávku.
![image](assets/14.webp)

### Vytváření objednávek

Kromě přijetí nabídky od někoho jiného můžete vytvořit vlastní a čekat, až k vám přijde další Robot.

- Otevřete stránku Vytvořit.
- Určete, zda je vaše objednávka na nákup nebo prodej Bitcoinu.
- Zadejte množství a měnu, ve které chcete Nakupovat/Prodávat.
- Zadejte platební metody, které jste ochotni použít.
- Zadejte % 'Přirážky nad tržní cenu', kterou jste ochotni přijmout. Poznamenejte, že to může být záporné číslo, pokud chcete nabídnout slevu oproti aktuální tržní ceně.
- Klikněte na Vytvořit objednávku.
- Zaplaťte fakturu Lightning, abyste uzamkli váš Maker Bond.
- Vaše objednávka je nyní aktivní. Sedněte si a čekejte, až ji někdo přijme.

![image](assets/15.webp)

### Výplaty na-chain

RoboSats je zaměřen na Lightning, ale kupující mají možnost přijmout své satoshi na Bitcoinovou adresu na-chain. Kupující mohou tuto možnost vybrat po uzamčení svého záručního vkladu. Po výběru možnosti na-chain uvidí kupující přehled poplatků. Dodatečné poplatky za tuto službu zahrnují:

- Poplatek za swap, který vybírá RoboSats - Tento poplatek je dynamický a mění se v závislosti na vytíženosti Bitcoinové sítě.
- Těžební poplatek za transakci výplaty - Tento je konfigurovatelný kupujícím.

![image](assets/16.webp)

### P2P Swapy

RoboSats umožňuje uživatelům vyměňovat satoshi do nebo ze své Lightning peněženky. Jednoduše klikněte na tlačítko swap na vrchu stránky s nabídkami, abyste viděli aktuální nabídky swapů.

Jako kupující nabídky ‘Swap In’ pošlete Bitcoin na-chain peerovi a obdržíte satoshi zpět, mínus inzerované poplatky a/nebo přirážky, do vaší Lightning peněženky. Jako kupující nabídky ‘Swap Out’ pošlete satoshi přes Lightning a obdržíte Bitcoin, mínus jakékoliv poplatky a/nebo přirážky, na vaši adresu na-chain. Uživatelé peněženek Samourai nebo Sparrow mohou také využít funkci Stowaway pro dokončení swapu.

Nabídky swapů RoboSats mohou také zahrnovat alternativy k Bitcoinu vázané na jiné měny, včetně RBTC, LBTC a WBTC. Měli byste být velmi opatrní při interakci s těmito tokeny, protože všechny přinášejí různé kompromisy. Vázaný Bitcoin není Bitcoin!

![image](assets/17.webp)

### Spusťte svůj vlastní klient RoboSats

Běžci uzlů Umbrel, Citadel a Start9 mohou nainstalovat svůj vlastní klient RoboSats přímo na svůj uzel. Výhody toho jsou:

- Dramaticky rychlejší načítací časy.
- Bezpečnější: kontrolujete, kterou aplikaci klienta RoboSats spouštíte.
- Bezpečný přístup k RoboSats z jakéhokoli prohlížeče / zařízení. Není potřeba používat TOR, pokud jste ve své lokální síti nebo používáte VPN: váš uzlový backend zajišťuje potřebnou torifikaci pro anonymizaci.
- Umožňuje kontrolu nad tím, ke kterému koordinátoru P2P trhu se připojíte (výchozí je robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)

![image](assets/18.webp)

## FAQ

### Mohu být podveden?
Jako kupující, pokud jste poslali fiat měnu potřebnou pro vaši část obchodu, ale prodávající nepřevede vám sats, pak můžete otevřít spor. Pokud během tohoto procesu sporu dokážete arbitrům RoboSats, že jste skutečně poslali fiat, zajištěné prostředky prodávajícího a jeho obchodní záruka budou převedeny na vás. Jak mohu zrušit obchod?

Obchod můžete zrušit po zveřejnění vaší záruky kliknutím na tlačítko Collaborative Cancel v menu obchodu. Pokud váš obchodní partner souhlasí se zrušením, nebudou vám účtovány žádné poplatky. Ale pokud váš obchodní partner chce obchod dokončit a vy ho přesto zrušíte, ztratíte vaši obchodní záruku.

### Funguje RoboSats s platební metodou ‘X’?

V RoboSats nejsou žádná omezení ohledně platebních metod. Pokud nevidíte žádné nabídky ve vaší preferované metodě, vytvořte si vlastní nabídku s použitím této metody!

![obrázek](assets/19.webp)

### Co se RoboSats dozví o mně, když jej používám?

Pokud používáte RoboSats přes Tor nebo Android aplikaci, nic vůbec! Dozvědět se více zde.

- Tor chrání vaše síťové soukromí.
- PGP šifrování udržuje váš obchodní chat v soukromí.
- Žádné účty znamenají jednoho robota na obchod. To znamená, že RoboSats nemůže korelovat více obchodů k jedné entitě.

Existují však některé výhrady! Lightning je poměrně soukromý jako odesílatel, ale ne jako příjemce. Pokud přijímáte na svůj vlastní Lightning uzel, vaše ID uzlu je sdíleno ve vašich fakturách. Toto ID uzlu dává každému, kdo o něm ví, výchozí bod pro pokusy o propojení vaší aktivity na řetězci. To platí i v případě, že uživatel si zvolí přijetí obchodu prostřednictvím výplaty na řetězci.

Aby se tomu předešlo, uživatelé mohou zvolit řešení, jako je Proxy Wallet pro Lightning nebo Coinjoin pro transakce na řetězci.

### Federace

V současné době je jediný koordinátor RoboSats provozován týmem vývojářů RoboSats. V Bitcoinu jakákoli forma centralizace usnadňuje cíl pro vlády nebo regulátory, kteří nemusí na konkrétní službu pohlížet příznivě.

Jelikož je RoboSats Open Source projekt, kdokoli by mohl vzít kód a začít provozovat vlastního koordinátora. I když to do jisté míry decentralizuje riziko od jediného cíle, také to fragmentuje již tak řídký trh s likviditou.

Tým RoboSats si toho je vědom a začal pracovat na federativním modelu. Pro koncového uživatele by se to nemělo obchodní tok demonstrovaný výše příliš změnit, ale objeví se další pohledy nebo obrazovky, na kterých budete moci přidávat nebo odebírat různé koordinátory, které vzniknou.

KONEC průvodce
https://bitcoiner.guide/robosats/