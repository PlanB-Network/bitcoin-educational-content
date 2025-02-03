---
term: COINJOIN

---
Coinjoin je technika používaná k narušení sledovatelnosti bitcoinů. Spoléhá na kolaborativní transakce se specifickou strukturou stejného jména: coinjoin transakce. Transakce coinjoin pomáhají zlepšit ochranu soukromí uživatelů bitcoinu tím, že ztěžují analýzu transakcí vnějšími pozorovateli. Tato struktura umožňuje smíchat více mincí v jedné transakci, což ztěžuje určení vazeb mezi vstupními a výstupními adresami.

Obecná operace coinjoin je následující: různí uživatelé, kteří chtějí mixovat, vloží jako vstup transakce určitou částku. Tyto vstupy vyjdou jako různé výstupy ve stejné výši. Na konci transakce není možné určit, který výstup patří kterému uživateli. Mezi vstupy a výstupy transakce coinjoin není technicky žádná vazba. Vazba mezi každým uživatelem a každým UTXO je přerušena, stejně jako je přerušena historie každé mince.

![](../../dictionnaire/assets/4.webp)

Aby bylo možné provést coinjoin, aniž by kterýkoli uživatel kdykoli ztratil kontrolu nad svými prostředky, je transakce nejprve sestavena koordinátorem a poté předána každému uživateli. Každý z nich pak transakci podepíše na své straně poté, co ověří, že mu vyhovuje, a následně jsou všechny podpisy přidány k transakci. Pokud se některý uživatel nebo koordinátor pokusí ukrást prostředky ostatních tím, že upraví výstupy transakce coinjoin, budou podpisy neplatné a transakce bude uzly odmítnuta. Pokud je záznam výstupů účastníků prováděn pomocí Chaumových slepých podpisů, aby se zabránilo propojení se vstupem, označuje se jako "Chaumův coinjoin".

Tento mechanismus zvyšuje důvěrnost transakcí, aniž by vyžadoval úpravy protokolu Bitcoin. Specifické implementace coinjoinu, jako jsou Whirlpool, JoinMarket nebo Wabisabi, nabízejí řešení, která usnadňují proces koordinace mezi účastníky a zvyšují efektivitu transakcí coinjoinu. Zde je příklad transakce coinjoin:

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

Je obtížné s jistotou určit, kdo jako první představil myšlenku coinjoin u Bitcoinu a kdo měl nápad použít v této souvislosti slepé podpisy Davida Chauma. Často se má za to, že jako první o ní hovořil Gregory Maxwell v [zprávě na BitcoinTalku v roce 2013](https://bitcointalk.org/index.php?topic=279249.0):

Použití Chaumových slepých podpisů: Uživatelé se připojují a poskytují vstupy (a mění adresy), jakož i kryptograficky zaslepenou verzi adresy, na kterou chtějí poslat své soukromé mince; server tokeny podepíše a vrátí je. Uživatelé se znovu anonymně připojí, odmaskují své výstupní adresy a pošlou je zpět serveru. Server vidí, že všechny výstupy byly jím podepsány a že tedy všechny výstupy pocházejí od platných účastníků. Později se lidé znovu připojí a podepíší.

Maxwell, G. (2013, 22. srpna). *CoinJoin: Bitcoin privacy for the real world* (Soukromí bitcoinů pro reálný svět). Fórum BitcoinTalk. https://bitcointalk.org/index.php?topic=279249.0

Existují však i dřívější zmínky, a to jak o Chaumových signaturách v kontextu míchání, tak o koincidencích. [V červnu 2011 představuje Duncan Townsend na BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) mixér, který používá Chaumovy signatury způsobem dosti podobným moderním chaumovským coinjoinům. Ve stejném vlákně je [zpráva od hashcoinu v reakci na Duncana Townsenda](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) k vylepšení jeho mixeru. Tato zpráva představuje to, co se nejvíce podobá coinjoins. Zmínka o podobném systému je také ve [zprávě od Alexe Mizrahiho z roku 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), když radil tvůrcům Tenebrixu. Samotný termín "coinjoin" nevymyslel Greg Maxwell, ale pochází z nápadu Petera Todda.

> *Termín "coinjoin" nemá francouzský překlad. Někteří bitcoináři používají pro transakci coinjoin také termíny "mix", "mixování" nebo "mixage". Mixování je spíše proces používaný v jádru coinjoinu. Je také důležité nezaměňovat mixování prostřednictvím coinjoinů s mixováním prostřednictvím centrálního aktéra, který během procesu přebírá bitcoiny do svého vlastnictví. To nemá nic společného s coinjoinem, kde uživatel během procesu neztrácí kontrolu nad svými bitcoiny*