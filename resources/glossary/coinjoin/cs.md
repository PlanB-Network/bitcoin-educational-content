---
term: COINJOIN
---

Coinjoin je technika používaná k narušení sledovatelnosti bitcoinů. Spoléhá na kolaborativní transakci se specifickou strukturou stejného názvu: transakce coinjoin. Transakce coinjoin pomáhají zlepšit ochranu soukromí uživatelů Bitcoinu tím, že ztěžují externím pozorovatelům analýzu transakcí. Tato struktura umožňuje míchání více mincí v jediné transakci, což ztěžuje určení vazeb mezi vstupními a výstupními adresami.

Obecný postup coinjoinu je následující: různí uživatelé, kteří si přejí míchat, vloží určitou částku jako vstup transakce. Tyto vstupy pak vyjdou jako různé výstupy stejné částky. Na konci transakce je nemožné určit, který výstup patří kterému uživateli. Technicky neexistuje žádná vazba mezi vstupy a výstupy transakce coinjoin. Vazba mezi každým uživatelem a každým UTXO je přerušena, stejně jako historie každé mince.

![](../../dictionnaire/assets/4.png)

Aby bylo možné provádět coinjoin bez toho, aby kterýkoli uživatel kdy ztratil kontrolu nad svými prostředky, transakce je nejprve sestavena koordinátorem a poté předána každému uživateli. Každý poté transakci na své straně podepíše po ověření, že mu vyhovuje, a poté jsou všechny podpisy přidány do transakce. Pokud uživatel nebo koordinátor pokusí ukrást prostředky ostatních účastníků úpravou výstupů transakce coinjoin, pak budou podpisy neplatné a transakce bude uzly zamítnuta. Když je záznam výstupů účastníků prováděn pomocí Chaumových slepých podpisů, aby se zabránilo spojení s vstupem, hovoří se o "Chaumian coinjoin".

Tento mechanismus zvyšuje důvěrnost transakcí bez nutnosti úprav protokolu Bitcoinu. Specifické implementace coinjoinu, jako jsou Whirlpool, JoinMarket nebo Wabisabi, nabízejí řešení usnadňující koordinační proces mezi účastníky a zvyšující efektivitu transakce coinjoin. Zde je příklad transakce coinjoin:

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

Je obtížné určit s jistotou, kdo jako první představil myšlenku coinjoinu na Bitcoinu a kdo měl nápad použít Davidovy Chaumovy slepé podpisy v tomto kontextu. Často se soudí, že první o tom diskutoval Gregory Maxwell v [zprávě na BitcoinTalk v roce 2013](https://bitcointalk.org/index.php?topic=279249.0):
Použití Chaumových slepých podpisů: Uživatelé se spojí a poskytnou vstupy (a adresy pro změnu) spolu s kryptograficky zaslepenou verzí adresy, na kterou chtějí poslat své soukromé mince; server tokeny podepíše a vrátí je. Uživatelé se znovu spojí anonymně, odmaskují své výstupní adresy a pošlou je zpět serveru. Server může vidět, že všechny výstupy byly jím podepsány a že tudíž všechny výstupy pocházejí od platných účastníků. Později se lidé znovu spojí a podepíší.
Maxwell, G. (2013, 22. srpna). *CoinJoin: Soukromí Bitcoinu pro skutečný svět*. Fórum BitcoinTalk. https://bitcointalk.org/index.php?topic=279249.0
Nicméně existují i dřívější zmínky, jak o Chaumových podpisech v kontextu míchání, tak i o coinjoinech. [V červnu 2011 Duncan Townsend představil na BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) mixer, který využívá Chaumovy podpisy způsobem velmi podobným moderním Chaumian coinjoinům. Ve stejném vlákně je [zpráva od uživatele hashcoin jako reakce na Duncana Townsenda](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) s návrhem na vylepšení jeho mixéru. Tato zpráva představuje něco, co se nejvíce podobá coinjoinům. Zmínka o podobném systému je také v [zprávě od Alexa Mizrahiho v roce 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), kdy radil tvůrcům Tenebrixu. Termín "coinjoin" sám nevymyslel Greg Maxwell, ale pochází z nápadu Petera Todda.
> ► *Termín "coinjoin" nemá český překlad. Někteří bitcoinisté také používají termíny "mix", "míchání" nebo "mixage" pro odkaz na transakci coinjoin. Míchání je spíše proces používaný v jádru coinjoinu. Je také důležité neplést míchání prostřednictvím coinjoinů s mícháním prostřednictvím centrálního aktéra, který během procesu přebírá držbu bitcoinů. To nesouvisí s coinjoinem, kde uživatel během procesu neztrácí kontrolu nad svými bitcoiny.*