---
name: Minibits Wallet
description: Příručka pro minibity Wallet
---

![cover](assets/cover.webp)


V tomto návodu vás provedu nastavením Minibits Wallet na používání ecash. Výkonná platební technologie zaměřená na ochranu soukromí, která funguje společně s Bitcoin. Minibits je ecash a Lightning Wallet, který umožňuje okamžité, levné a soukromé převody hodnot, takže je ideální pro každodenní transakce, u kterých záleží na soukromí.


Než se ponoříme do Minibits, ujasněme si, co ecash je a co není. Mnoho lidí si plete ecash s technologií Bitcoin nebo Blockchain, ale jde o zásadně odlišné koncepty.


Ecash NENÍ Bitcoin. Nenahrazuje váš samospasitelný Bitcoin Wallet, ale spíše jej doplňuje. Ecash NENÍ Blockchain a nežije na žádném veřejném Ledger. Zajímavé je, že ecash NENÍ nová technologie - ve skutečnosti předchází celosvětové síti, jejíž koncepty byly vyvinuty v 80. a 90. letech 20. století.


Co ecash JE: neuvěřitelně soukromý (transakce nezanechávají žádnou sledovatelnou historii), peer-to-peer (přímé převody bez prostředníků) a funguje jako digitální nástroj na doručitele (pokud jej vlastníte, máte jej pod kontrolou). Klíčovou výhodou je, že ecash lze používat offline - odesílatel nebo příjemce mohou být během transakcí odpojeni od internetu. Ecash MŮŽE být ražen jednou stranou nebo federací důvěryhodných subjektů a JE dokonalou doplňkovou technologií ke Bitcoin, která zvládá malé, časté transakce, zatímco Bitcoin slouží jako zúčtovací Layer.


Vezměte prosím na vědomí, že toto nastavení Minibits představuje "custodial řešení", což znamená, že správu svých prostředků svěřujete provozovateli Mincovny. To s sebou přináší specifická rizika, kterým musíte před pokračováním porozumět.


V projektu je uvedeno toto důležité prohlášení o vyloučení odpovědnosti:


- Tento Wallet by měl být používán pouze pro výzkumné účely.
- Wallet je beta verze s neúplnou funkčností a známými i neznámými chybami.
- Nepoužívejte ji s velkými částkami v hotovosti.
- Mincovna vydává hotovostní peníze uložené v Wallet
- důvěřujete mincovně, že ji podpoří Bitcoin, dokud nepřevedete svůj majetek na jiný Bitcoin blesk Wallet.
- Protokol Cashu, který Wallet implementuje, nebyl dosud podroben rozsáhlé revizi ani testování.


S Minibity zacházejte jako s každodenním účtem Wallet, nikoli jako se spořicím účtem, a nikdy zde neukládejte významnou hodnotu.


## 1️⃣ Nastavení Wallet


Chcete-li začít, navštivte [webové stránky Minibits](https://www.minibits.cash/), kde najdete možnosti stahování pro všechny hlavní platformy. Uživatelé iOS mohou stahovat z [App Store](https://testflight.apple.com/join/defJQgTD), zatímco uživatelé EU iOS mají další možnost instalace z [Freedom Store](https://freedomstore.io/). Uživatelé systému Android mohou aplikaci získat z [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) nebo stáhnout soubor APK přímo ze stránky [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases).


Při instalaci Minibits se zobrazí úvodní obrazovky, které vysvětlují základní pojmy - můžete si je přečíst, nebo je přeskočit, pokud jste s technologií již obeznámeni. Po dokončení těchto úvodních kroků budete vyzváni k výběru mezi:


- `Mám to, vezměte mě do Wallet` pro nové uživatele nebo
- `Obnovit ztracené Wallet`, pokud obnovujete ze zálohy.


![image](assets/en/01.webp)

Po dokončení počátečního nastavení se dostanete na domovskou obrazovku, na které je několik důležitých údajů Elements. ① Ikona profilu v horním rohu vás přenese na stránku vašeho profilu, kde můžete přistupovat ke svým Minibitům Wallet Address a vybrat možnosti `dávkového příjmu`. ② Uprostřed obrazovky uvidíte mincovníky, které můžete používat, přičemž ve výchozím nastavení je vybrán mincovník Minibits. ③ Řádek akcí níže nabízí možnosti odesílání plateb ecash nebo lightning, skenování QR kódu a přijímání plateb. ④ A konečně spodní navigační panel obsahuje zkratky na domovskou obrazovku, historii transakcí, kontakty a nastavení.


![image](assets/en/02.webp)


## 2️⃣ Spravujte mentolky


Ve výchozím nastavení je mincovník Minibits při spuštění aplikace povolen. Jednou ze silných stránek ecash je však možnost používat více mincoven pro zvýšení decentralizace a bezpečnosti. Chcete-li přidat další mincovnu, přejděte na `Nastavení`, poté vyberte `Správa mincoven` a nakonec klepněte na `Přidat mincovnu`.


[Bitcoinmints.com](Bitcoinmints.com) poskytuje komplexní seznam dostupných mincoven s uživatelskými hodnoceními, které vám pomohou vybrat seriózní možnosti. Používání více mincoven snižuje vaše riziko. Pokud se u jedné mincovny vyskytnou problémy, vaše prostředky v ostatních mincovnách zůstanou přístupné.


![image](assets/en/04.webp)


## 3️⃣ Vytvoření zálohy


Zálohování je pravděpodobně nejdůležitějším krokem celého procesu nastavení. Pro přístup k možnostem zálohování přejděte do `Nastavení`-> `Zálohování` Zde najdete dvě základní možnosti:

1. `Vaše fráze seed`, která obsahuje `12 slov` a umožňuje obnovit zůstatek hotovosti v případě ztráty zařízení. Tato fráze seed je vaším hlavním klíčem ke všem hotovostem ecash ve všech mincovnách, které jste přidali. Zapište si ji na fyzické médium (papír nebo kov) a bezpečně ji uložte na více místech. Frázi seed nikdy neukládejte na digitální médium, kde by mohla být ohrožena. Zvažte návštěvu tohoto [tutoriálu](https://planb.network/en/tutorials/Wallet/backup/backup-Mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270), kde najdete osvědčené postupy pro zabezpečení své fráze Wallet.

2. `Wallet backup`, který obsahuje dlouhý zálohovací řetězec.


**Upozornění**: Při použití této zálohy k obnově Wallet budete stále potřebovat frázi seed.


![image](assets/en/05.webp)


## 4️⃣ Vytvořit minibity Wallet Address


Dále přejděte na `Kontakty` v dolní části a přizpůsobte si vyhrazený `Minibits Wallet Address` klepnutím na `Změnit` -> `Změnit Wallet Address`. Zadejte preferovaný model Address a zkontrolujte dostupnost.


![image](assets/en/07.webp)


Po nastavení Address budete požádáni o malý `Donation` na podporu projektu. Ačkoli je to nepovinné, důrazně doporučuji to zvážit, pokud plánujete službu pravidelně využívat. Projekty s otevřeným zdrojovým kódem, jako je Minibits, spoléhají na podporu komunity, aby mohly pokračovat ve vývoji a údržbě. I malý příspěvek pomáhá zajistit projektu dlouhou životnost.


![image](assets/en/08.webp)


## nastavení 5️⃣ Nostr


Pokud chcete dát tip lidem, které sledujete na Nostru, můžete `Přidat svůj npub klíč` výběrem `Kontakty` a poté `Veřejné`. Tím se vaše Minibits Wallet propojí se sociální sítí Nostr a umožní bezproblémové dávání spropitného.


Máte také možnost `Použít svůj vlastní profil` tak, že přejdete do `Nastavení` a poté do `Soukromí` a importujete svůj vlastní Nostr Address a klíč. Mějte však na paměti, že tímto postupem přestane váš Wallet komunikovat se servery minibits.cash Nostr a LNURL Address, což znemožní bleskové funkce Address pro příjem zapsů a plateb.


![image](assets/en/09.webp)


## 6️⃣ Přijímání finančních prostředků


Chcete-li zpočátku získat finanční prostředky, musíte si dobít účet Wallet prostřednictvím bleskového účtu Invoice. Tento proces je jednoduchý: klepněte na `Doplnění` , zadejte `Částku`, kterou chcete přidat, volitelně přidejte `Paměť` a poté klepněte na `Vytvořit Invoice`. Tento Invoice pak budete muset zaplatit pomocí jiného bleskového Wallet. Tím se bleskové platby Bitcoin převedou na žetony ecash v rámci vašeho minibitového Wallet.


![image](assets/en/10.webp)


## 7️⃣ Odeslat finanční prostředky


Když už jste založili účet Wallet, můžete posílat prostředky dvěma různými způsoby.


### Odeslat ecash


První možností je poslat ecash přímo. Klepněte na `Odeslat` , poté vyberte `Odeslat ecash`, zadejte `Částku` a klepněte na `Vytvořit token.` Tím se vytvoří kód QR generate, který můžete sdílet s příjemcem nebo jej nechat přímo naskenovat jeho zařízením. Příjemci se žetony objeví v jeho Wallet téměř okamžitě, bez Blockchain poplatků nebo zpoždění při potvrzování.


![image](assets/en/11.webp)


### Platba pomocí Lightning


Druhou možností je platba prostřednictvím služby Lightning. Klepněte na `Odeslat` a poté vyberte `Platit pomocí Lightning`. Můžete si vybrat ze svých `kontaktů` Nostr (pokud jste připojili svůj npub) nebo zadat/vložit kód platby Lightning Address, Invoice nebo LNURL pomocí možnosti `Vložit` nebo `skenovat`. Po `potvrzení` příjemce budete vyzváni k zadání `částky k zaplacení`, případně přidejte poznámku a poté klepněte na `potvrdit` a poté na `zaplatit` pro dokončení transakce Lightning.


![image](assets/en/12.webp)


## 8️⃣ Vytvoření připojení NWC


Další výkonnou funkcí Minibits je možnost vytvářet připojení `Nostr Wallet Connect (NWC)`, která umožňují jiným aplikacím požadovat platby z vašeho Wallet, aniž by došlo k odhalení vašich soukromých klíčů.


Pro nastavení přejděte do `Nastavení`, vyberte `Nostr Wallet Connect` a klepněte na `Přidat připojení`. Připojení pojmenujte nějak popisně, abyste identifikovali jak aplikaci, tak přidružený uživatelský účet. Nastavte přiměřený maximální denní limit, abyste mohli kontrolovat, kolik lze prostřednictvím tohoto připojení utratit, a poté klepnutím na `Uložit` dokončete nastavení.


Tato funkce je užitečná zejména u služeb, jako je Nostr Clients, kde chcete povolit automatické spropitné bez nutnosti ručního schvalování každé transakce.


![image](assets/en/12.webp)


## 🎯 Závěr


Minibity představují dostupný vstupní bod do světa ecash a nabízejí platby zaměřené na ochranu soukromí, které doplňují vaše držení Bitcoin. Nezapomeňte vždy udržovat řádné zálohy, zvažte použití více mincí pro redundanci a ukládejte do tohoto úschovného řešení pouze přiměřené množství.


Další zdroje najdete v úložišti Minibits na GitHubu, na oficiálních webových stránkách a na kanálu Telegram, kde komunita aktivně diskutuje o vývoji a řeší problémy


- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Webové stránky](https://www.minibits.cash/)
- [Telegram](https://t.me/MinibitsWallet)


Ecosystem se stále vyvíjí, ale nástroje jako Minibits tuto výkonnou technologii ochrany soukromí stále více zpřístupňují běžným uživatelům.