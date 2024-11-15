---
name: Peer-to-Peer řešení pro nákup a prodej Bitcoinů
goal: Prozkoumat řešení pro nákup a prodej Bitcoinů bez KYC
objectives:
  - Porozumět různým typům KYC, jejich rizikům a výhodám
  - Porozumět výhodám peer-to-peer nákupu
  - Implementovat řešení, které vyhovuje vašim potřebám
  - Zlepšit správu vašich UTXO (KYC a non-KYC)
---

# Cesta do světa Non-KYC

Pierre nám nabízí tento kurz, který se zabývá různými existujícími řešeními pro nákup a prodej bitcoinů peer-to-peer. Peer-to-peer nákup je zcela legální a umožňuje větší anonymitu, skutečně tato řešení nejsou KYC. KYC (Know Your Customer - Poznej svého zákazníka) je pravidlo tržního regulátora (AMF), které zahrnuje požadavek na identifikaci zákazníků, kteří si přejí koupit nebo prodat bitcoin. Tato pravidla mají za cíl zabránit praní peněz, financování terorismu a daňovým únikům. Přestože má KYC pro uživatele významné důsledky, jeho cílem je bránit a chránit uživatele, ačkoli se často pozoruje opačný efekt.

Proto prozkoumáme různé typy KYC (plný typ KYC jako ve Francii, typ KYC Light jako ve Švýcarsku a typ non-KYC jako peer-to-peer). Pierre představí více než 6 řešení, takže budete mít veškeré informace potřebné k objevení toho, které vám vyhovuje. Pokud hledáte řešení KYC, vězte, že jsou zahrnuta v kurzu BTC 102.

+++

# Úvod
<partId>9aa6ddfd-a257-549f-bb23-f77f1ca5d330</partId>

## Vysvětlení & Typy KYC
<chapterId>13d18e82-0c50-5a7f-97d8-39cf5b4ef085</chapterId>

### Úvod

![úvod od Rogzy](https://youtu.be/3AHeKLTK7Sg)

### Vysvětlení

![vysvětlení typů KYC](https://youtu.be/kDhXoPU1KtM)

KYC, neboli "Poznej svého zákazníka", je regulační standard, který vyžaduje shromažďování soukromých informací od klientů, jako je jejich fyzická adresa, identifikace nebo bankovní výpisy. Tato praxe je běžná na platformách pro zprostředkování, které mohou požadovat kompletní KYC, včetně podrobných informací, jako je občanský průkaz, fotografie, důkaz o bydlišti, výplatní pásky atd.
Hlavním cílem KYC (Poznej svého zákazníka) je boj proti praní peněz, financování terorismu a daňovým únikům. Jedná se o zákon implementovaný AMF (Autorité des marchés financiers), regulačním orgánem francouzského trhu. Nicméně aplikace KYC vede k centralizaci vysoce citlivých databází obsahujících osobní informace uživatelů. Tyto informace, mající určitou hodnotu, mohou být prodány zlomyslným subjektům.
Navíc platformy pro výměnu často požadují nadměrné množství osobních informací, čímž uživatele vystavují riziku a zvyšují náklady na dodržování předpisů. Tyto regulační náklady mohou odradit francouzské podniky a poškodit jejich mezinárodní konkurenceschopnost.

Existují tři typy KYC, včetně plného KYC, který vyžaduje kompletní a regulované shromažďování informací pro přístup ke službě. Ve Švýcarsku existuje alternativa nazvaná "KYC light", která umožňuje nákup a prodej bitcoinů bez poskytnutí občanského průkazu, pokud částka nákupu nepřesahuje 1000 eur za den. Řešení jako Relay umožňují využití této metody.
V tomto kontextu mohou švýcarské úřady získat přístup k bankovním informacím pro vyšetřování osob považovaných za rizikové. Dodací adresy bitcoinů jsou také vystopovatelné prostřednictvím bankovního systému. KYC light je obecně považován za jednodušší a méně nákladný než francouzský systém.
Ve Francii vyžaduje nákup bitcoinů online poslání peněz třetí straně, prostřednictvím SEPA převodu nebo Paypalu. Pro ty, kteří dávají přednost anonymitě, bezpečnosti a soukromí, jsou také k dispozici řešení pro nákup bitcoinů v hotovosti. Pro malé objemy je nákup bitcoinů v hotovosti jednoduchou a legální možností.
Aby bylo možné každému denně prodávat PLT v hodnotě 100 eur bitcoinů, je nutná regulace ze strany AMF (Autorité des Marchés Financiers). Ve Francii se tato regulace většinou týká jednotlivců, kteří provádějí významné objemy transakcí. Dalšími dvěma metodami nákupu bitcoinu jsou použití bankomatů a výměny mezi přáteli. Bankomaty jsou regulovány a pro transakce nad 500 eur vyžadují identifikaci. Výměna mezi přáteli na druhou stranu nabízí diskrétnější přístup k bitcoinu.

Tyto regulační opatření jsou na místě, aby se zabránilo financování terorismu, daňovým únikům a praní špinavých peněz. Bitcoin, jako plně sledovatelná databáze, činí praní peněz obzvláště obtížným. Použití Bitcoinu zločinci lze vystopovat, což z Bitcoinu činí neefektivní nástroj pro praní peněz.
Je důležité poznamenat, že toto školení představuje různé alternativy, stejně jako nástroje, které lze použít pro škodlivé i neškodlivé účely. Kromě toho nabízí vysvětlení, jak fungují knihy objednávek mezi tvůrci (poskytovateli objednávek) a příjemci (příjemci objednávek).

Je také důležité poznamenat, že informace prezentované zde neschvalují žádné konkrétní řešení. Jedná se pouze o prezentaci dostupných možností pro lepší pochopení tématu. Pro další otázky týkající se Bitcoinu neváhejte konzultovat online zdroje, jako je www.discoverbitcoin.com.

## Srovnání řešení pro nákup a prodej mezi rovnými (Peer-to-Peer)
<chapterId>aad2dccb-0d2c-5533-859b-372b0f10d1ca</chapterId>

![srovnání řešení pro nákup a prodej mezi rovnými](https://youtu.be/HiwSjN04Mz0)

P2P řešení pro nákup Bitcoinu: Bisq, RoboSat, LNP2PBot, Peach a HodlHodl

Nákup Bitcoinu na základě peer-to-peer (P2P) je preferovanou možností pro investory, kteří se chtějí vyhnout centralizovaným burzovním platformám. Tato část kurzu zkoumá různá dostupná P2P řešení, včetně Bisq, RoboSat, LNP2PBot, Peach a HodlHodl.
Srovnání výhod a nevýhod různých řešení

Každé P2P řešení má své vlastní výhody a nevýhody. Níže je přehled klíčových vlastností každého řešení.

### Bisq

[Bisq](https://bisq.network/) je neopatrované P2P řešení, které využívá systém DAO (Decentralizovaná Autonomní Organizace) a používá multisig pro řešení sporů. Jeho kód je otevřený, což přispívá k jeho robustnosti a ochraně soukromí uživatelů.

| Výhody                                      | Nevýhody                                                                                                       |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| - P2P, neopatrované, multisig, DAO řešení   | - Aplikace je poměrně těžkopádná a nepříliš uživatelsky přívětivá, dostupná pouze na počítačích                |
| - Robustní a bezpečné                       | - Omezení na nákup a prodej, stejně jako správa účtu s podpisy, mají dvousečný aspekt.                         |
| - Otevřený zdroj                            |                                                                                                                |

### RoboSat

[RoboSat](https://learn.robosats.com/) je snadno použitelné, rychlé řešení fungující pod TORem a nevyžaduje účet. Je otevřeného zdroje a využívá Lightning Network pro rychlé transakce.

| Výhody                                                     | Nevýhody                                                                  |
| - Snadné použití                                      | - Protokol je křehký s pouze jedním koordinátorem                           || - Nízké transakční poplatky                               | - Vyžaduje technické znalosti a porozumění soukromí |
| - Využívá Lightning Network pro rychlé transakce | - Aplikace Umbrell umožňuje spravovat vlastní instanci klienta           |
### LNP2PBot

[LNP2PBot](https://lnp2pbot.com/) je přístupný přes Telegram pro nákupy Bitcoinů bez KYC. Nabízí rychlé transakce prostřednictvím Lightning Network a nízké poplatky.

| Výhody                                                          | Nevýhody                                                         |
| -------------------------------------------------------------- | ----------------------------------------------------------------- |
| - Přístupný přes Telegram                                      | - Méně robustní a bezpečný než jiná řešení                        |
| - Rychlost prostřednictvím Lightning Network                    | - Pomalejší a méně uživatelsky přívětivý než Robosat             |
| - Nízké transakční poplatky                                     | - Může být spojen s identitou uživatele na Telegramu              |
| - Interní řešení sporů                                          | - Nedostatek likvidity a křehkost aplikace                        |
| - Nabízí komunity pro zmírnění problémů s důvěrou               | - Důvěra musí být vložena do LNP2Pbot pro řešení sporů            |

### Peach

[Peach](https://peachbitcoin.com/) je mobilní aplikace věnovaná obchodování s Bitcoinem. Vyniká svou jednoduchostí, nevyžaduje vytvoření účtu pro provoz. Obchody jsou rychlé, i bez použití Lightning Network. Navíc notifikace na telefonu urychlují proces transakce.

| Výhody                                                          | Nevýhody                                                                                                                  |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| - Zjednodušené použití: vytvoření účtu není nutné.              | - Bezpečnost a robustnost: Peach je spojen s firmou, což představuje potenciální slabiny z hlediska bezpečnosti.           |
| - Rychlost transakce: výměny jsou rychlé.                       | - Absence Lightning Network: tato technologie, která umožňuje rychlejší transakce s Bitcoinem, není Peachem využívána.      |
| - Notifikace: urychlují proces transakce.                       |                                                                                                                            |

### HodlHodl

[HodlHodl](https://hodlhodl.com/) je nezákonné řešení pro výměnu Bitcoinů. Nabízí mnoho výhod, jako je vysoká likvidita, možnost soukromých obchodů, systém doporučení, stejně jako účty s historií obchodů a hodnotícím systémem. Nicméně, obchody jsou spojeny s e-mailovou adresou uživatele a digitální identitou, uloženou v HodlHodl. Navíc zdrojový kód HodlHodl není veřejně přístupný a aplikace nemůže být použita s Tor.

| Výhody                                                                                                                     | Nevýhody                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| - Nezákonné: uživatel zůstává v držení svých privátních klíčů.                                                            | - Ukládání osobních informací: e-mailová adresa a digitální identita uživatele jsou uloženy HodlHodl.                       |
| - Likvidita: HodlHodl nabízí širokou škálu možností výměny.                                                              | - Zavřený zdrojový kód: kód HodlHodl není veřejně přístupný.                                                               |
| - Možnosti soukromého obchodu: uživatel si může vybrat, s kým obchodovat. | - Nezpůsobilost pro Tor: HodlHodl nemůže být použit s tímto soukromím zaměřeným sítí. |
| - Systém doporučení: HodlHodl odměňuje ústní propagaci. | - Možnost nuceného KYC: v určitých situacích může HodlHodl vyžadovat identifikační informace pro získání prostředků. |
| - Historie obchodů a hodnotící systém: tyto funkce umožňují posoudit spolehlivost ostatních uživatelů. | |

## Závěr o P2P řešeních
<chapterId>c904985a-78dd-593e-a9c4-bfd1208d10c3</chapterId>
Shrnutí, každé P2P řešení má své výhody a nevýhody. Bisq je považován za nejrobustnější a nejbezpečnější, ale méně přístupný. RoboSat je open source, ale méně robustní než Bisq. LNP2PBot je méně robustní a bezpečný než ostatní řešení, pomalejší a méně uživatelsky přívětivý než RoboSat, ale více než Bisq. Peach je nejjednodušší a nejrychlejší aplikace pro nákup Bitcoinu bez KYC, ale je podporována společností, a proto má slabiny z hlediska bezpečnosti a robustnosti. HodlHodl je protokol spravovaný společností a je uzavřený zdroj, proto má slabiny z hlediska bezpečnosti a robustnosti a je o něco složitější než Peach.
Dobrá stará hotovost tváří v tvář zůstává vždy řešením pro malé částky.
Kromě P2P řešení existují i další možnosti výměny kryptoměn. kycnot.me nabízí služby jako VPN, VPS, SMS atd. Bitrefil umožňuje nákup dárkových karet. Každé řešení na [kycnotme](https://kycnot.me/) je prezentováno s jeho klady a zápory.

# Tutoriály na P2P nákup/prodej řešení
<partId>582cee39-f6d0-5fb8-906f-b3e4c9f36fa5</partId>

## Robosats
<chapterId>1f1bd705-fcb3-5e32-8aa7-9ba184488326</chapterId>

![robosats](https://tube.nuagelibre.fr/videos/watch/1978a2e0-64a0-4437-9229-7614cdf5bf61?start=0s)

[RoboSat](https://learn.robosats.com/) je open-source projekt vyvinutý Reckless Satoshi pro soukromou výměnu Bitcoinů za národní měny. Zjednodušuje peer-to-peer zážitek a používá Lightning faktury k minimalizaci potřeby držení a důvěry. K jeho použití budeme potřebovat Tor, anonymní komunikační síť.

První věc, kterou musíte udělat, je stáhnout Tor. Najdete ho na GitHubu nebo přímo na oficiálních stránkách na následující adrese: tor.org/download.
Jakmile je Tor stažen a nainstalován:
- Stiskněte "Connect" pro navázání spojení.
- Přejděte na [Robosats onion adresu](http://robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion/).
- Zkopírujte token pro uložení vaší identity.

Zde jsou kroky pro nákup bitcoinů s Robosats:

- Zkontrolujte knihu objednávek, můžete filtrovat podle měny a způsobu platby - například koupit bitcoin v eurech s Revolut.
- Před nákupem zkontrolujte expiraci nabídky, cenu v eurech a prémii (nabídky můžete také filtrovat podle prémie).
- Preferujte nabídku s aktivním uživatelem a prémii nižší než průměr.
- Ověřte souhrn objednávky s množstvím, způsobem platby, prémii, ID objednávky a expirací.
- Můžete přijmout své satoshi na bitcoinovou adresu s poplatky za swap-out (z LN na BTC-onchain) okolo 1% (můžete upravit on-chain těžební poplatky).
- Alternativně vytvořte fakturu s LN peněženkou z tohoto [seznamu](https://learn.robosats.com/docs/wallets/) a zkopírujte fakturu na Robosats.
- Kontaktujte prodejce prostřednictvím šifrovaného chatu, abyste diskutovali o platbě fiat.

Nyní se podívejme na kroky pro prodej bitcoinů na Robosats:

- Přizpůsobte svou nabídku výběrem způsobu platby, prémie, doby expirace atd.
- Velikost záručního vkladu je ekvivalentní kauce na BISQ. Vložte 15% nebo 10% kauce, aby byla podpořena férová hra druhé strany.
- Zamkněte satoshi, aby bylo potvrzeno vytvoření objednávky a zabráněno spamu.
- Pokud někdo přijme vaši nabídku prodeje, domluvte se s protistranou na provedení platby ve fiat měně. Jakmile je platba provedena, obchod je dokončen a prodané satoshi jsou vaše!

## BISQ: Peer-to-peer řešení pro nákup
<chapterId>28b010ce-0e9b-5f20-a622-fa64629b2d88</chapterId>

[Bisq](https://bisq.network/) je decentralizovaná obchodní platforma pro digitální aktiva, primárně pro Bitcoin. Umožňuje přímé, bezpečné a soukromé transakce mezi uživateli po celém světě bez nutnosti zprostředkovatele.

🚨 Při používání Bisq buďte opatrní, jedná se o pokročilé řešení. Pro začátečníky nemusí být vhodné. Před zahájením se ujistěte, že máte nějaké zkušenosti a porozumění. 🚨

Podíváme se podrobně na toto řešení, zde jsou výuková videa:
Pro ty zkušenější je zde stručný průvodce, který rychle shrnuje základní kroky:

1. Stáhněte a nainstalujte: Navštivte webové stránky Bisq a stáhněte aplikaci. Nainstalujte ji na svůj systém.
2. Nastavte způsob platby: Otevřete aplikaci a přejděte na "Účet". Přidejte údaje o vašem způsobu platby.
3. Financujte svou peněženku Bisq: Klikněte na "Fondy" a poté na "Přijmout fondy" pro získání vaší adresy Bisq. Pošlete na tuto adresu Bitcoiny.
4. Proveďte transakci: Klikněte na "Koupit/Prodat" a vyberte požadovanou transakci. Postupujte podle pokynů k dokončení transakce.
5. Potvrďte příjem: Jakmile obdržíte platbu, potvrďte ji v aplikaci Bisq. To uvolní Bitcoin z escrow.

Vždy si pečlivě zkontrolujte všechny detaily vašich transakcí a obchodujte pouze s důvěryhodnými stranami.

Zde je nyní kompletní průvodce, který vás provede všemi kroky použití Bisq.

BISQ je decentralizovaná a bezpečná síť, která respektuje vaše soukromí. Skutečně, je to non-custodial, což znamená, že vždy vlastníte své fondy. Navíc BISQ používá token, BSQ, který vám umožňuje platit nižší transakční poplatky a podporuje vaši účast v DAO (Decentralizovaná Autonomní Organizace). Aby BISQ chránil prodejce v transakcích Bitcoin-fiat, implementoval systém podpisů a limitů účtů. Jako kupující budete potřebovat získat podepsaný účet, abyste zvýšili svůj nákupní limit. Podpis je také způsob, jak ověřit obchodní historii obchodníků, čímž se zajišťuje bezpečnost transakcí.

Pro instalaci Bisq a zálohování vašich dat postupujte podle těchto jednoduchých kroků:

- Přejděte na stránku bisc.network pro stažení softwaru (Screenshot stránky pro stažení)
- Ověřte integritu softwaru pomocí nástrojů, jako jsou ty, které nabízí Loïc Morel pro uživatele Windows.
- Jakmile je instalátor ověřen, spusťte BISQ, udělte potřebná oprávnění a přijměte podmínky použití. (Screenshot podmínek použití)
- BISQ se připojí k síti Bitcoin a k sobě přes Tor, což může chvíli trvat.
- Nastavte svůj platební účet a proveďte zálohy vašeho SID (Secure Identifier) vaší peněženky, aby se předešlo jakékoli ztrátě nebo krádeži. (Screenshot stránky nastavení účtu)
- Nastavte také heslo pro šifrování vašich informací.
V závislosti na vašem operačním systému budou data BISQ uložena na různých místech. Najdete je ve složce "Data Directory". Buďte opatrní, pokud tuto složku smažete, všechna vaše data BISQ budou ztracena. Pro obnovu vašich dat prostřednictvím zálohy:
- Zkopírujte záložní složku do umístění 'user/application support/BISQ'.
- Přejmenujte záložní složku na 'BISQ'.
- Restartujte BISQ a všechna vaše data by měla být obnovena.

Než začnete na BISQ kupovat nebo prodávat Bitcoin, je klíčové nastavit si platební účet. Například si můžete nastavit účet ve vaší národní měně, jako je účet SEPA, účet REVOLUT nebo účet PAYPAL. Pro nastavení vašeho účtu REVOLUT:

- Přidejte účet a vyberte REVOLUT ze seznamu možností. (Snímek obrazovky se seznamem možností účtů)
- Můžete si vybrat různé měny: euro, britská libra, americký dolar nebo švýcarský frank.
- Maximální doba transakce je jeden den a limit nákupu je 0,25 Bitcoinu.
- Použijte své osobní jméno účtu REVOLUT, abyste předešli jakékoli záměně.
- Nezapomeňte podepsat své účty a stanovit limity nákupu pro větší bezpečnost.

Pro nákup Bitcoinu na BISQ:

- Přejděte do sekce "Koupit", kde si můžete vybrat z různých trhů. (Snímek obrazovky sekce "Koupit")
- Pro využití snížených poplatků doporučujeme koupit BSQ, které můžete zakoupit za Bitcoin.
- Můžete si vybrat z různých nabídek na základě ceny, množství, způsobu platby atd.
- Pro nákup BSQ nejprve vložte Bitcoin do vaší peněženky.
- Vyberte nabídku s nízkou přirážkou a malým množstvím pro nákup BSQ.
- BISQ ověří platnost nabídky a peer spojení.
- Pokud prodávající není připojen, vyberte jiného.
- Zkontrolujte nabídku a přijměte 5% přirážku.
- Potvrďte poplatky a výměnu BSQ, poté čekejte na potvrzení transakce, abyste mohli koupit Bitcoiny za BSQ.

Prodej Bitcoinu na BISQ:

- Vytvořte novou nabídku v záložce "Prodat". (Snímek obrazovky záložky "Prodat")
- Můžete si vybrat, kolik Bitcoinů prodat nebo kolik eur chcete obdržet.
- Můžete nastavit přirážku jako procento nad tržní cenou.
- Můžete vytvořit rozsah prodeje nebo nechat výběr na kupujícím.
- Můžete také nastavit cenu pro zastavení nabídky.
- Vyberte minimální výši vkladu a transakční poplatky.
- Financujte objednávku vložením Bitcoinů na prodej, částky bezpečnostního vkladu a poplatků.
- Jakmile nabídku vytvoříte, počkejte, až se objeví kupující.
Jakmile kupující provede transakční vklad na BISQ, Bitcoiny jsou automaticky odeslány kupujícímu a vy obdržíte peníze. Účet je ověřen a podepsán po transakci s podepsaným účtem.
## LNP2PBOT
<chapterId>e3b61150-90e3-5ab4-bc12-4a05879321f5</chapterId>

![LNp2pbot tutorial](https://tube.nuagelibre.fr/videos/watch/57ed232d-6149-4267-be38-92b0f32800f7)

[Telegram](https://telegram.org/) je platforma pro zasílání zpráv, která s pomocí bota [Lnp2pbot](https://lnp2pbot.com/) umožňuje rychlý a snadný nákup a prodej bitcoinů. Jak na to:

Pro nákup Bitcoinů přes LNP2PBOT na Telegramu postupujte takto:
- Začněte tím, že navštívíte Twitter účet Lnp2pbot a klikněte na odkaz v bio. (Snímek obrazovky Twitter účtu bota a odkazu v bio)
- V Telegramu použijte příkazy "/buy" nebo "/sell" pro vytvoření nabídek koupě nebo prodeje. (Snímek obrazovky použití příkazů "/buy" nebo "/sell")
- Přejděte na kanál P2P Lightning, abyste našli nabídky koupě a prodeje podle vašich kritérií. (Snímek obrazovky kanálu P2P Lightning)
- Vytvořte nabídku koupě pomocí Lnp2pbot a příkazu "/buy".
- Vyberte měnu podle vašeho výběru, uveďte množství, cenu (s prémiovou sazbou, pokud si přejete) a vyberte způsob platby.
- Počkejte, až vás potenciální prodávající kontaktuje.

Pokud chcete prodat Bitcoiny přes Revolut, postupujte takto:

- Klikněte na 'prodat Satoshi', abyste otevřeli oznámení na LNP2PBot. (Snímek obrazovky možnosti 'prodat Satoshi')
- Obdržíte Lightning fakturu k zaplacení, aby bylo možné prodat Satoshi. (Snímek obrazovky Lightning faktury)
- Počkejte, až kupující pošle fakturu se satoshi k přijetí plateb.
- Navážte přímý kontakt s kupujícím přes Telegram, abyste se dohodli na způsobu platby a vyměnili potřebné informace.
- Potvrďte transakci s poznámkou.

Pokud chcete koupit Bitcoiny odesláním LN faktury, postupujte podle těchto kroků:

- Zkopírujte fakturu a pošlete ji botovi k nákupu Satoshi.
- Navážte kontakt s prodávajícím, abyste dokončili nákup bitcoinů.
- V případě problému navrhněte čekání nebo pokus o zrušení.
- Zrušte nabídku a hledejte novou, pokud je to nutné.
- Vyberte nabídku, která akceptuje okamžité CPAs pro nákup Satoshi.
- Pošlete fakturu a počkejte na potvrzení platby prodávajícím.
- Jakmile je platba provedena, pošlete potvrzení botovi.
- Počkejte na potvrzení přijetí eur a odeslání satoshi prodávajícím.
Použitím těchto metod můžete bezpečně kupovat a prodávat bitcoiny na Telegramu.

## Peach Bitcoin
<chapterId>05e328c4-1003-586e-85c3-65109e3486e1</chapterId>

site: https://peachbitcoin.com/

Podrobně se na toto řešení podíváme v kurzu BTC 205, který nabízí @pivi\_, zde jsou výuková videa:

![peach](https://youtu.be/ziwhv9KqVkM)

[Peach](https://peachbitcoin.com/) je švýcarská mobilní aplikace, která umožňuje peer-to-peer nákup a prodej bitcoinů. Toto snadno použitelné řešení nabízí intuitivní rozhraní, ideální pro transakce s kryptoměnami.

Rozhraní aplikace Peach se skládá ze čtyř záložek: koupit, prodat, historie a nastavení. (Snímek obrazovky rozhraní aplikace)
Nákup bitcoinů na Peach je zjednodušený. Pro začátek je potřeba vytvořit nabídku. To je možné přístupem na záložku "koupit". (Snímek obrazovky záložky "koupit")
Poté procházejte dostupné nabídky posouváním, dokud nenajdete tu, která vám vyhovuje. Přijímané způsoby platby jsou různé, včetně bankovního převodu, online peněženky, dárkové karty a místní možnosti. (Snímek obrazovky dostupných způsobů platby)
Jakmile si vyberete nabídku, můžete diskutovat s prodávajícím prostřednictvím chatu integrovaného do aplikace. (Snímek obrazovky chatu aplikace)
Po potvrzení platby prodávajícím je transakce dokončena. Bitcoiny jsou poté odeslány kupujícímu, který obdrží oznámení potvrzující přijetí finančních prostředků. (Snímek obrazovky oznámení o přijetí bitcoinů)
Peach je neopatrovnická aplikace, což znamená, že bitcoiny zůstávají po celou dobu procesu ve vašem vlastnictví. Nicméně, jakékoli potenciální spory jsou řízeny centrálně. Proto je zásadní zálohovat informace související s transakcemi a vaše osobní údaje pomocí funkce Zálohování. (Screenshot funkce Zálohování) Jelikož je Peach stále ve verzi beta, mohou se vyskytnout nějaké chyby. Doporučuje se ověřit všechny informace před uzavřením transakce.
Shrnutí, mobilní aplikace Peach nabízí přístupné řešení pro nákup a prodej bitcoinů peer-to-peer. Bezpečné a optimální využití Peach je klíčem k úspěšným transakcím.

## Hold Hodl
<chapterId>2c285751-ae9f-54af-8b28-c7c0beac7b43</chapterId>
[HodlHodl](https://hodlhodl.com/) je decentralizovaný trh s bitcoiny, který klade důraz na kontrolu uživatele a bezpečnost. Na rozdíl od tradičních burz funguje na modelu peer-to-peer, což umožňuje přímé výměny mezi uživateli. Díky svému systému escrow s více podpisy Hodl Hodl zajišťuje bezpečnost prostředků během transakcí. Platforma také podporuje různé platební metody a nabízí obchodní možnosti, jako jsou Kontrakty na rozdíl (CFD).
![hodlhodl tutorial](https://youtu.be/BDH9jE7kpD8)

V tomto tutoriálu vysvětlujeme, jak nakupovat a prodávat bitcoiny peer-to-peer na platformě HodlHodl.

Před začátkem používání platformy HodlHodl je nutné provést několik přípravných kroků:

- Otevřete webové stránky HodlHodl.
- Vytvořte účet pomocí e-mailové adresy, abyste si uchovali historii svých transakcí.
- Před zahájením obchodování pečlivě přečtěte průvodce bezpečností.
- Všimněte si, že platforma není open source a uchovává některé vaše osobní informace.

Postup pro provedení nákupu na platformě HodlHodl je následující:

- Použijte funkci filtru, abyste našli nabídky, které vám vyhovují.
- Klikněte na nabídku, která vás zajímá.
- Vyplňte potřebná pole pro přijetí smlouvy.
- V našem příkladu jsme jako platební metodu použili Revolut.

Nastavení multisig smlouvy pro transakci probíhá na HodlHodl následovně:

- Jakmile je nabídka přijata, proveďte platbu vybranou metodou (v našem případě Revolut).
- Vytvořte multisig smlouvu generováním hesla.
- Počkejte, až budou bitcoiny vloženy na multisig adresu.
- Vyberte počet potvrzení pro smlouvu.
- Proveďte platbu dohodnuté částky prodejci a potvrďte ji na HodlHodl.
- Buďte trpěliví, protože doba vkladu může být dlouhá v závislosti na použité bance.
- Počkejte na potvrzení prodejce před uvolněním bitcoinů po nákupu.

Vytvoření nabídky pro prodej nebo nákup bitcoinů na HodlHodl probíhá takto:

- Na stránkách HodlHodl uveďte výdejní adresu pro nabídky nákupu.
- Zadejte množství, cenu a platební metodu.
- Můžete také přidat volitelné funkce, jako jsou limity transakcí nebo název nabídky.
- Jakmile je nabídka vytvořena, můžete ji podle přání zobrazit, upravit, duplikovat nebo smazat.

## Bonus: Side Shift.AI
<chapterId>bd1f0844-af1e-53da-9518-b3b22f802276</chapterId>

![SideShift AI](https://youtu.be/xG8Wc1Ti5b8)
Zde je stručný návod na používání [SideShift AI](https://sideshift.ai/), velmi praktického nástroje pro převod shitcoinů na bitcoin. Je to ideální nástroj pro ty, kteří uzavřeli všechny své osobní burzy. Není potřeba žádný systém objednávek a likvidita je k dispozici. Všimněte si však, že za každou transakci se účtuje poplatek 2,5 %. Pokud jste kryptoměny zakoupili způsobem KYC, doporučuje se použít Monero pro jejich převod na bitcoin. Monero nabízí lepší soukromí ve srovnání s Bitcoinem. Pro zvýšení bezpečnosti se také doporučuje operace CoinJoin. CoinJoin míchá vaše transakce s transakcemi ostatních uživatelů, aby komplikoval sledovatelnost vašich transakcí.

Rád bych vám také představil open-source nástroj pro nákup a prodej bitcoinů. Tento nástroj vám umožňuje vybrat si z mnoha blockchainů. Stačí zadat vaši bitcoinovou adresu a vybrat částku, kterou chcete poslat. Není potřeba vytvářet účet ani připojovat vaši peněženku k nástroji. Můžete použít pevnou sazbu pro odeslání nebo přijetí určité částky. Navíc tento nástroj také umožňuje prodej bitcoinů výměnou za USDC.

### Podpořte nás

Tento kurz, stejně jako veškerý obsah na této univerzitě, vám byl nabídnut zdarma naší komunitou. Můžete nás podpořit tím, že jej sdílíte s ostatními, stane se členem univerzity a dokonce přispějete k jejímu vývoji prostřednictvím GitHubu. Jménem celého týmu vám děkujeme!

### Ohodnoťte školení

Systém hodnocení školení bude brzy integrován do této nové E-learningové platformy! Mezitím vám velmi děkujeme za sledování kurzu a pokud se vám líbil, zvažte jeho sdílení s lidmi ve vašem okolí.

# Pro další informace
<partId>28194543-78b5-5f98-852a-2fc76439ddde</partId>

## Rozhovor se Steph z Peach Bitcoin
<chapterId>76ed1f17-1d0b-5c0f-8726-91ab4e2e2955</chapterId>

![rozhovor se Steph](https://youtu.be/LRGKD8qNSXw)

Zde je shrnutí rozhovoru:

Peach Bitcoin je nevěřitelská mobilní aplikace, která umožňuje peer-to-peer nákup a prodej Bitcoinu. Současný tým Peach Bitcoin, který sídlí ve Švýcarsku, zahrnuje osm členů a snaží se aplikaci vyvíjet tak, aby sloužila také jako peněženka. Unikátní model Peach Bitcoin spočívá ve struktuře centralizované společnosti, přičemž si zachovává decentralizovaný nákupní a prodejní záznam. Aplikace navíc nabízí možnost hotovostních transakcí při osobních setkáních.
Jednou z hlavních výhod Peach Bitcoin je úroveň bezpečnosti, kterou nabízí uživatelům. Escrow systém s vícepodepisem a časovým zámkem je navržen tak, aby řešil konflikty a zajišťoval bezpečnost transakcí. Navíc má Peach Bitcoin prioritní přístup k vícepodepisovým fondům, což mu umožňuje převést bitcoiny kupujícímu v případě škodlivého chování ze strany prodejce. Společnost plánuje integrovat všechny evropské měny, stejně jako další platební metody, když spustí otevřenou betaverzi v lednu.

Nápad na Peach Bitcoin vznikl z osobní zkušenosti zakladatelky s průmyslem Bitcoinu. Po objevení Bitcoinu v roce 2017 a účasti na několika setkáních a konferencích se stala maximalistkou Bitcoinu a uviděla příležitost vytvořit platformu pro Bitcoinery, aby se setkávali a prováděli hotovostní transakce. Aplikace navíc zahrnuje šifrovaný chat pro komunikaci s ostatními uživateli, čímž zachovává anonymitu uživatele.
Aktuálně Pitch Bitcoin vyvíjí několik funkcí, které mají usnadnit práci prodejcům, včetně vytvoření API pro prodejce, platformy pro velké prodejce a integrace BTC Pay Serveru pro automatizaci převodů. Aplikace bude spuštěna v otevřené betaverzi v lednu 2023.
Zakladatelka Pitch Bitcoin zdůrazňuje význam konkurence v ekosystému Bitcoinu, protože to, co je dobré pro Bitcoin, je prospěšné pro všechny. Také podporuje diverzitu a inkluzi v průmyslu Bitcoinu a dále.

## Rozhovor s Pierrem
<chapterId>4e4ba218-01ec-5f3a-bc49-c148bb22ee61</chapterId>

![rozhovor s Pierrem](https://youtu.be/COoezuJncm8)

Zde je shrnutí rozhovoru:
Tento rozhovor uzavírá kurz Bitcoin 205, který se zabývá tématem řešení pro nákup Bitcoinu peer-to-peer. Kurz organizovaný Pierrem má za cíl vzdělávat frankofonní veřejnost o technických řešeních pro nákup Bitcoinu peer-to-peer, oblasti, která byla dosud opomíjena. Díky dosaženému pokroku je nyní možné nakupovat a používat Bitcoin s ochranou soukromí, i jen s telefonem a aplikací Telegram.

Jednou z vyzdvihnutých metod je použití CoinJoin s Samourai pro zvýšení bezpečnosti. Toto řešení minimalizuje rizika spojená s centralizovanými subjekty držícími osobní informace o uživatelích Bitcoinu. Doporučuje se nákup Bitcoinů non-KYC, metoda, která posiluje anonymitu. Navíc některé burzy, jako je Kraken, nabízejí nižší poplatky za výběr než jiné, což je v souladu s principy Bitcoinu.
Bisq, Robosat a Peach jsou prezentovány jako demokratická řešení pro obchodování s Bitcoinem. Peach je zvláště vyzdvihnut pro svou snadnou dostupnost jako mobilní aplikace. Existují však výzvy, které je třeba řešit, včetně regulace kryptoměn a potřeby respektovat určité limity, aby nedošlo k nadměrné regulaci.

Diskutováno je také používání Bitcoinových bankomatů; ty představují ekonomickou metodu pro získání Bitcoinů non-KYC. V závislosti na místních předpisech mohou být tyto bankomaty instalovány doma nebo na veřejných místech a mohou být použity k nabízení bitcoinů blízkým nebo pro platby v barech.

Vzdělávání zdůrazňuje důležitost role vzdělání ve chápání Bitcoinu. Naznačuje se, že Bitcoin může nabídnout řešení v případě recese nebo hyperinflace a že je důležité zvyšovat povědomí o jeho potenciálu, než bude příliš pozdě. Navíc je zdůrazněno, že oddělení státu a peněz je stejně zásadní jako oddělení státu a náboženství.

Závěrem je Bitcoin prezentován jako decentralizovaná měna, která vyžaduje veřejné vzdělávání a otevřenou mysl, aby byla plně pochopena a využita. Školení má pomoci účastníkům pochopit různá řešení pro nákup peer-to-peer a používat tyto nástroje k zvýšení jejich anonymity a bezpečnosti při používání Bitcoinu.

## Hodnocení tohoto kurzu
<chapterId>a6410a99-adfc-50fd-a004-8048be620c8a</chapterId>
<isCourseReview>true</isCourseReview>

## Závěrečná zkouška
<chapterId>38d03a01-ae5f-5c21-acd4-42f18b20c2b4</chapterId>
<isCourseExam>true</isCourseExam>

## Bonusový článek o soukromí
<chapterId>9f1aa75a-3031-58b2-9d4a-11a5c4197302</chapterId>

Skvělý [článek](https://decouvrebitcoin.fr/tribune-sur-le-kyc-et-lidentification-des-bitcoins-onchain/) od Loïca Morela o KYC a identifikaci
Tento podrobný článek zkoumá výzvy a řešení pro zachování soukromí při nákupu a používání bitcoinů. Loïc rozebírá některé běžné omyly týkající se identifikace KYC (Know Your Customer - Poznej svého zákazníka), podrobně popisuje rizika spojená s tímto procesem a nabízí techniky pro udržení anonymity transakcí. Je to povinné čtení pro ty, kteří chtějí porozumět nuancím soukromí ve světě Bitcoinu a naučit se, jak používat nástroje jako CoinJoin, Stonewall a PayJoin k zamaskování sledování transakcí a tím ochránit své soukromí.