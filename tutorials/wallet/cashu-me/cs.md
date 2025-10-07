---
name: Cashu.me
description: Cashu.me průvodce používáním ecash
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*Zde je videonávod od BTC Sessions, videonávod, který vás provede nastavením a používáním Cashu.me Bitcoin Wallet, který vám umožní přístup k jednoduchým, levným a soukromým transakcím Bitcoin - bez potřeby obchodu s aplikacemi!*


V tomto tutoriálu prozkoumáme Cashu.me, prohlížečovou aplikaci Wallet pro soukromé platby Bitcoin pomocí Chaumian ecash. Než se do toho ponoříme, pojďme si stručně představit ecash a jeho fungování.


## Úvod do systému ecash


Představte si, že byste měli digitální hotovost, která by fungovala stejně jako fyzické bankovky v kapse - soukromá, okamžitá a použitelná mezi partnery bez prostředníků. To je to, co umožňuje ecash: digitální platební přístup, který vrací soukromí fyzické hotovosti do digitálního světa. Na rozdíl od onchain-Bitcoin, který zaznamenává každou transakci na veřejném Ledger viditelném pro kohokoli, ecash vytváří soukromé tokeny, které představují skutečnou hodnotu Bitcoin a zároveň zachovávají důvěrnost vašich výdajových zvyklostí.


Představte si ekopeníze jako digitální nástroje na doručitele uložené ve vašem zařízení - pokud je držíte, vlastníte je stejně jako fyzickou hotovost. Tyto tokeny vydávají důvěryhodné služby zvané `Mints`, které drží podkladové rezervy Bitcoin. Když používáte ecash, nevysíláte své transakce do celé sítě. Místo toho si vyměňujete soukromé tokeny přímo s ostatními, čímž vytváříte platební zkušenost, která se více podobá předání hotovosti než tradiční digitální platbě.


Cashu je svobodný a open-source protokol Chaumian ecash vytvořený pro Bitcoin. Tato technologie vychází z průkopnického kryptografického výzkumu Davida Chauma z 80. let 20. století, který k zajištění soukromí používá "slepé podpisy". Když obdržíte žetony ecash, mincovna je podepíše, aniž by věděla, kde budou utraceny příště - což je klíčová vlastnost, která zabraňuje sledování transakcí. Důležité je, že ecash nenahrazuje Bitcoin; doplňuje jej tím, že řeší některé kritické problémy, které vyplývají z požadavků na architekturu Bitcoin. Poskytuje soukromí, které nabízí fyzická hotovost (což transparentní Bitcoin Ledger postrádá), a umožňuje okamžité mikrotransakce bez poplatků Blockchain nebo zpoždění potvrzení.


Systém Ecash se bez problémů integruje se systémem Lightning Network. Pomocí Lightningu vkládáte Bitcoin do mincovny (převádíte hodnotu Bitcoin na žetony ecash) a později vybíráte (převádíte žetony zpět na utratitelný zůstatek Lightningu). Dohromady tvoří výkonnou kombinaci: Bitcoin poskytuje bezpečné vypořádání Layer, Lightning umožňuje rychlé transakce a interoperabilitu sítě a ecash přidává soukromí Layer, díky němuž se digitální platby opět stávají skutečně soukromými.


## Cashu.me


Cashu.me je `Progresivní webová aplikace (PWA)`, která implementuje protokol Cashu - specifickou implementaci Chaumian ecash určenou pro Bitcoin. Jako PWA funguje přímo v prohlížeči, aniž by vyžadovala instalaci z obchodů s aplikacemi, ačkoli si ji můžete `nainstalovat` do svého zařízení pro snadnější přístup. Tento webový přístup zajišťuje širokou kompatibilitu napříč operačními systémy a zároveň zachovává bezpečnost prostřednictvím kryptografických protokolů, nikoliv platformových omezení.


## 🎉 Klíčové funkce


Pojďme se ponořit do funkcí a prozkoumat, co Cashu.me nabízí:



- Chaumian ecash na Lightning**: Používá slepé podpisy, takže mincovny nemohou sledovat zůstatky uživatelů ani historii transakcí
- Vlastní úschova žetonů**: Tokeny ecash ovládáte lokálně pomocí své věty seed
- Zálohy frází seed**: 12 slov pro obnovení fráze Wallet
- Mátová nezávislost**: Pracuje s více nezávislými mincovnami - nejste vázáni na jednoho poskytovatele
- Okamžité bezplatné transakce**: V rámci stejné mincovny jsou platby dokončeny během několika sekund s nulovými poplatky
- Architektura zachovávající soukromí**: Mincovny nevidí, kdo s kým obchoduje
- Offline ecash**: Odesílání/přijímání žetonů prostřednictvím místního přenosového protokolu, jako je NFC, QR kód, Bluetooth atd., bez připojení k internetu
- Objevte mincovníky ecash prostřednictvím Nostr**: Najděte a ověřte důvěryhodné mincovny prostřednictvím protokolu Nostr
- Vyměňte si ecash mezi mincovnami**: Všechny mincovny mluví jazykem Lightning, což znamená, že mezi nimi můžete převádět hodnotu.
- Dálkově ovládejte svůj Wallet pomocí aplikace Nostr Wallet Connect (NWC)**: Připojte se k dalším aplikacím, jako je Nostr Client, a začněte zapping přes NWC


Rozhodujícím kompromisem je "důvěra": zatímco samotné tokeny máte pod kontrolou, mincovnám musíte důvěřovat, že budou opatrovat podkladové rezervy Bitcoin. Jak uvádí dokumentace Cashu:


> ...mincovna provozuje infrastrukturu Lightning a spravuje satoši pro uživatele mincovny ecash. Uživatelé musí důvěřovat mincovně, že Redeem jejich ecash, jakmile chtějí přejít na Lightning.

- Dokumentace Cashu, [Obecné otázky bezpečnosti a ochrany osobních údajů](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


Díky tomu je ecash řešením pro úschovu samotného Bitcoin, i když si zachováváte plnou kontrolu nad tokeny.


## úvodní nastavení 1️⃣


① Začněte návštěvou [Wallet.cashu.me](https://Wallet.cashu.me) ve svém prohlížeči. Vzhledem k tomu, že Cashu.me je `PWA`, nemusíte ji stahovat z obchodů s aplikacemi, ale jednoduše otevřete stránku přímo v prohlížeči. Pro snadnější přístup si ji můžete volitelně nainstalovat na domovskou obrazovku svého zařízení.


② Chcete-li nainstalovat PWA, klepněte v prohlížeči na tlačítko nabídky ⋮ a vyberte možnost `Přidat na domovskou obrazovku`. Po instalaci zavřete kartu prohlížeče a spusťte Cashu.me z domovské obrazovky zařízení. Na úvodní obrazovce klepněte na `Další` a pokračujte.


③ Bezpečnost je zásadní. Frázi seed bezpečně uložte do správce hesel nebo si ji ještě lépe zapište na papír. Tato 12slovná obnovovací fráze je jediným způsobem, jak získat zpět finanční prostředky, pokud ztratíte přístup k tomuto zařízení. Klepnutím na ikonu 👁️ zobrazte svou frázi seed, pečlivě zapište všech 12 slov v pořadí a poté zaškrtněte políčko označené `Zapsal jsem si ji`. Klepnutím na `Další` pokračujte a na následující obrazovce zaškrtnutím políčka potvrďte, že souhlasíte s `podmínkami`.


![image](assets/en/01.webp)


Po dokončení nastavení se budete muset připojit ke službě `Mint`. Klepnutím na `ADD MINT` a následně na `DISCOVER MINTS` zobrazíte mincovny doporučené komunitou Nostr. Pro další ověření si můžete prohlédnout hodnocení mincoven na adrese [bitcoinmints.com](bitcoinmints.com).


Poté klepněte na `Klepnutím na procházet mincovníky` a zobrazte si úplný seznam. Vyberte mincovnu zkopírováním její adresy URL, vložením do pole URL a zadáním rozpoznatelného názvu. Pro tento příklad použijeme např:


URL: `https://mint.minibits.cash/Bitcoin`

Jméno: `Minibits`


![image](assets/en/02.webp)


Klepnutím na `ADD MINT` proces dokončíte. Na potvrzovací obrazovce ověřte, že důvěřujete provozovateli této mincovny, a poté znovu klepněte na `ADD MINT`. Mincovník Minibits se nyní objeví na domovské obrazovce. Jakmile je mincovník Wallet nastaven, musíte jej před prováděním transakcí financovat.


![image](assets/en/03.webp)


## 2️⃣ Financování vašeho Wallet


Cashu.me nabízí dva různé způsoby financování Wallet. Když na úvodní obrazovce klepnete na `Přijmout`, zobrazí se možnosti přijetí peněz prostřednictvím `PENĚŽNÍCH PROSTŘEDKŮ` nebo `PŘÍJMU`.


![image](assets/en/04.webp)


### Financování prostřednictvím LIGHTNING


První možností je financovat Wallet prostřednictvím blesku Invoice. `Zvolte mincovnu`, pokud jste přidali různé mincovny, a určete `částku (Sats)`, kterou chcete obdržet. Poté klepněte na `Vytvořit Invoice.` Nyní se vám zobrazí QR-kód, který můžete naskenovat pomocí jiného bleskového Wallet nebo můžete jednoduše `Kopírovat` Invoice a vložit do jiného Wallet, abyste zaplatili a financovali svůj cashu.me Wallet.


![image](assets/en/05.webp)


### Příjem hotovosti ecash


Metoda ecash umožňuje přijímat tokeny přímo od jiné společnosti ecash Wallet. Začněte klepnutím na tlačítko `Přijmout` a vyberte možnost `ECASH`. Budete moci `Vložit` nebo `Skenovat` nebo použít `NFC` pro odeslání Cashu token z jiného Wallet. Pokud se rozhodnete pro vložení, zadejte řetězec token, který jste zkopírovali z jiného Wallet, automaticky se zobrazí `Částka` a `Mincovník`. Klepnutím na `PŘEVZÍT` transakci dokončíte a ve vašem Wallet se objeví Sats. Všimněte si, že váš zůstatek je nyní rozdělen mezi více mincovníků. Například můžete mít 1 000 Sats v `Mincovně` Minibits a dalších 1 000 Sats v `Mincovně` Coinos. Toto rozdělení mezi různé mincovny je důležitým aspektem architektury Cashu.


![image](assets/en/06.webp)


### Výměna mezi mincovníky


Pokud již nedůvěřujete konkrétní mincovně, kterou jste si přidali, cashu.me nabízí funkci `Vyměnit` prostředky z jedné mincovny do druhé. Přejděte na záložku mincovny a sjeďte dolů, dokud neuvidíte položku `Výměna mincoven`. V rozbalovacích nabídkách vyberte mincovnu `Z` a `Do` a zadejte částku, kterou chcete převést. Klepnutím na `SWAP` přesunete žetony mezi mincovnami. Tento úkon bude proveden prostřednictvím transakce Lightning, takže si musíte ponechat prostor pro případné poplatky Lightning. V mém příkladu stačil 1 sat.


![image](assets/en/07.webp)


## 3️⃣ Zasílání finančních prostředků


Cashu.me nabízí dvě možnosti, jak odeslat Sats. Poslat prostřednictvím `ecash` nebo `lightning`. Podívejme se na obě možnosti.


### Odesílání přes Lightning


Chcete-li odeslat prostřednictvím aplikace Lightning, postupujte podle následujících kroků:


1. Na domovské obrazovce klepněte na tlačítko `Odeslat` a vyberte možnost `Blesk`

2. Aplikace vás vyzve k zadání `Lightning Invoice` nebo `-Address`. Můžete vložit přímo Invoice/Address nebo použít možnost naskenovat QR kód pro jeho vizuální zachycení a poté potvrdit tlačítkem `ENTER`

3. Pomocí rozevíracího pole vyberte mincovnu, ze které chcete platit, a klepnutím na tlačítko `Platit` potvrďte výběr. **Poznámka**: v části `Nastavení` -> `Experimentální` je také možnost použít `Multinut`, který umožňuje platit faktury z více mincoven najednou.

4. Po úspěšném dokončení se zobrazí potvrzení o platbě a částka odečtená z vašeho zůstatku.


![image](assets/en/08.webp)


### Odesílání přes ecash


Odesílání hotovosti je podobně jednoduché.


1. Klepněte na tlačítko `Odeslat` a tentokrát vyberte možnost `PENĚŽNÍ POPLATKY`.

2. `Vyberte mincovník` a zadejte částku, kterou chcete odeslat v Sats, a klepnutím na `Odeslat` potvrďte

3. Tím se vytvoří `Animovaný QR kód`, který můžete přizpůsobit nastavením parametrů Rychlost a Velikost. Kdokoli může tento QR kód naskenovat a okamžitě odeslat Redeem Sats, nebo můžete klepnout na možnost KOPÍROVAT a odeslat řetězec token někomu jinému prostřednictvím alternativních kanálů, jako je Bluetooth, NFC nebo standardní zasílání zpráv.

4. Otevírám další Wallet. Vložte ze schránky a v druhém Wallet vyberte `Přijmout ecash`.


![image](assets/en/09.webp)


## 4️⃣ Další funkce


Kromě základních funkcí pro odesílání a přijímání nabízí Cashu.me další výkonné funkce, které rozšiřují možnosti Bitcoin v rámci ekosystému Nostr.


### Nostr Wallet Connect


Nostr Wallet Connect (`NWC`) mění způsob interakce s aplikacemi Nostr tím, že vytváří bezproblémové spojení mezi vaším Wallet a aplikacemi sociálních sítí. Tento protokol umožňuje aplikacím, jako je [Damus](https://damus.io/) nebo [Primal](https://primal.net/home), požadovat platby přímo prostřednictvím relé Nostr, aniž byste museli aplikaci opustit.


Nastavení `NWC` v Cashu.me:


1. Přejděte na `Nastavení` v levém horním menu Hamburgeru

2. Přejděte na část `NOSTR Wallet CONNECT` a klepněte na tlačítko `Povolit`

3. Poté si nastavíte příspěvek, abyste určili maximální částku, kterou mohou aplikace utratit ze svého účtu Wallet.

4. Po konfiguraci můžete zkopírovat připojovací řetězec a vložit jej do libovolného klienta Nostr, který podporuje funkci `NWC`, čímž umožníte okamžité zapping a tipping.


![image](assets/en/10.webp)


### Lightning Address prostřednictvím npub.cash


Cashu.me se integruje s [npub.cash](https://npub.cash/) a poskytuje vám Lightning Address, který bez problémů funguje s protokolem Nostr. Zde se můžete zaregistrovat a požádat o své uživatelské jméno poskytnutím svého Nostr `nsec`, který stojí 5 000 Sats a podporuje projekt npub.cash, nebo můžete použít jakýkoli veřejný klíč Nostr (`npub`) bez registrace.


Nejprve přejděte do `Nastavení` a klepněte na `Povolit` Blesk Address s npub.cash. Tím se generate vytvoří npub.cash Address pomocí řetězce `npub` odvozeného z vaší Wallet seed fráze ve výchozím nastavení.


Můžete také navštívit [tuto webovou stránku](https://npub.cash/username) a požádat o vlastní uživatelské jméno pomocí svého vlastního Nostr `nsec`, čímž získáte osobní Lightning Address jako username@npub.cash.


![image](assets/en/11.webp)


## 🎯 Závěr


Cashu.me poskytuje soukromé platby Bitcoin, které fungují jako fyzická hotovost - okamžitě a peer-to-peer, aniž by byla odhalena vaše transakční historie. Osobně oceňuji jeho architekturu PWA, protože funguje bez omezení obchodu s aplikacemi. Spojením bezpečnosti Bitcoin, rychlosti Lightning a soukromí ecash nabízí Wallet případy použití, které by mohly zvýšit každodenní přijetí Bitcoin.


I když máte nad svými žetony ecash plnou kontrolu díky vlastní úschově, nezapomeňte, že mincovny fungují jako důvěryhodné třetí strany, které drží podkladové rezervy Bitcoin. Možnost používat více mincoven a vyměňovat si je mezi sebou poskytuje flexibilitu při zachování soukromí.


Díky funkcím, jako jsou adresy NWC a npub.cash, je Cashu.me atraktivní možností Wallet pro klienty sociálních sítí, kteří si cení soukromí a suverenity více než omezení velkých technologických politik.


## 📚 Zdroje


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)