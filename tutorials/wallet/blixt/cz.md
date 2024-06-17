---
name: Blixt

description: Mobilní LN Node Peněženka
---

![prezentace](assets/blixt_intro_en.webp)

## Výkonný BTC/Lightning node ve vaší kapse, kdekoliv jste

Rád bych vám představil zajímavý a výkonný nový BTC/LN mobilní node a peněženku – Blixt. Název pochází ze švédštiny a znamená "blesk".
Pokud jste nikdy nepoužívali Bitcoin Lightning Network, před začátkem si prosím přečtěte [tuto jednoduchou analogii vysvětlující Lightning Network (LN)](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport).

## DŮLEŽITÉ ASPEKTY:

### 1. Blixt je soukromý node, NENÍ to směrovací node! Mějte to na paměti.

To znamená, že všechny LN kanály v Blixtu budou neohlášené do LN grafu (tzv. soukromé kanály). To znamená, TENTO NODE NEBUDE SMĚROVAT platby ostatních přes Blixt node. [Zde si přečtěte více o soukromých a veřejných kanálech](https://voltage.cloud/blog/lightning-network-faq/what-are-the-differences-between-public-and-private-channels/).

Mobilní node Blixt NENÍ pro směrování, opakuji. Je hlavně pro to, abyste mohli spravovat vlastní LN kanály a provádět vaše LN platby soukromě, kdykoliv potřebujete.

Mobilní node Blixt, je nutné mít online a synchronizovaný JEN PŘED tím, než budete provádět vaše transakce. Proto uvidíte ikonu nahoře, která indikuje stav synchronizace. Trvá to jen chvíli, v závislosti na tom, jak dlouho jste ho měli offline a znovu synchronizujete LN graf.

### 2. Blixt používá LND (aezeed) jako backend peněženky, takže se nepokoušejte importovat jiné typy bitcoinových peněženek do něj.

[Zde máte vysvětlené typy peněženek](https://coldbit.com/what-types-of-mnemonic-seeds-are-used-in-bitcoin/). Takže pokud jste měli dříve LND node, můžete importovat seed a backup.channels do Blixtu, [jak je vysvětleno v tomto průvodci](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario).

### 3. Důležité odkazy Blixt (prosím, přidejte si je do záložek):

- [Blixt Github repository](https://github.com/hsjoberg/blixt-wallet) | [Github Releases](https://github.com/hsjoberg/blixt-wallet/releases) (přímé stažení apk souboru)
- [Stránka s funkcemi Blixt](https://blixtwallet.github.io/features) - vysvětlení jednotlivých funkcí a možností.
- [FAQ stránka Blixt](https://blixtwallet.github.io/faq) - Seznam otázek a odpovědí a řešení problémů s Blixt
- [Průvodci Blixt](https://blixtwallet.github.io/guides) - demo, video tutoriály, další průvodci a případové studie pro Blixt
- [Tisknutelný A4 leták](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer) s prvními kroky používání Blixtu, v různých jazycích.
- Blixt také nabízí plně funkční demo přímo na [svých webových stránkách](https://blixtwallet.com) nebo na věnované [webové verzi](https://blixt-wallet-git-master-hsjoberg.vercel.app/), abyste měli plný zážitek z testování, předtím než začnete Blixt používat ve skutečném světě.
- [Stránka pro crowdfunding Geyser](https://geyser.fund/project/blixt) - darujte sats, jak chcete, na podporu projektu
- [Skupina pro podporu na Telegramu](https://t.me/blixtwallet)
# Dostupné klíčové funkce

## Neutrino Node

Blixt se standardně připojuje k serveru Blixt pro synchronizaci bloků a indexaci pomocí Neutrino (SPV režim pro zjednodušené ověření plateb), ale uživatel se může také připojit ke svému vlastnímu uzlu. Je překvapivé, že synchronizace SPV uzlu trvá méně než 5 minut, v mém případě na Androidu 11, než je možné plně využívat peněženku s plným uzlem (on-chain a LN).

## Kompletně Nespravovaný Uzel

Uživatel může spravovat vlastní kanály prostřednictvím snadno použitelného rozhraní a s dostatečným množstvím zobrazených informací pro dobrý uživatelský zážitek. V menu v levém horním rohu můžete přejít na Lightning kanály a začít je otevírat s jinými uzly, jak si přejete. Nezapomeňte v nastaveních povolit Tor. Je to mnohem lepší pro soukromí a také proto, že jako mobilní uzel, pokud často měníte internetové připojení / IP adresu v clearnetu, vaši partneři mohou být narušeni. S URI uzlu Tor budete mít vždy stejný soukromý identifikátor bez ohledu na vaši polohu / IP.

## Zálohování/Obnovení LND Uzlu

Silná, snadno spravovatelná a užitečná funkce je obnovení jiných mrtvých LND uzlů, pouze s 24-slovným seznamem seed a souborem channels.backup.

> [Zde je návod, jak obnovit mrtvé Umbrel uzly v Blixt v případě SHTF.](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario)

Uživatel má také možnost uložit zálohu kanálů Blixt na Google Drive a/nebo na lokální úložiště svého mobilního zařízení (a později ji přesunout na bezpečné místo, daleko od vašeho telefonu).

Proces obnovy je poměrně jednoduchý: vložte 24-slovný seed, přidejte záložní soubor (předtím zkopírovaný do paměti mobilu) a klikněte na obnovit. Synchronizace a skenování všech bloků pro vaše minulé transakce zabere nějaký čas. Kanály budou automaticky uzavřeny a prostředky vráceny do vaší on-chain peněženky (viz menu v levém horním rohu - on-chain).

> Pokud jste měli předtím otevřené kanály se svým starým uzlem za Tor, musíte nejprve povolit možnost Tor (a restartovat aplikaci) v nastavení menu. Tímto způsobem nebude procedura uzavírání selhat a/nebo nebude použita možnost vynuceného uzavření.

Nezapomeňte zálohovat své LN kanály po jejich otevření a/nebo uzavření. Stačí pár sekund, abyste byli v bezpečí. Později můžete záložní soubor přesunout na bezpečné místo daleko od vašeho mobilního zařízení.
Pokud chcete otestovat svůj seed v scénáři obnovy, před přidáním prostředků, jednoduše použijte stejný 24-slovný seed (aezeed) v BlueWallet. Pokud je generovaná BTC adresa stejná jako v Blixt, můžete pokračovat. Po tomto testu již není potřeba používat BlueWallet, testovanou peněženku pro obnovu můžete jednoduše smazat.

## Vestavěný Tor

Jakmile jej aktivujete, aplikace se restartuje v síti Tor. Od tohoto okamžiku můžete v nastavení menu vidět ID vašeho uzlu s onion adresou, takže jiné uzly mohůou otevírat kanály k vašemu malému mobilnímu uzlu Blixt. Nebo řekněme, že máte vlastní uzel doma a chcete mít malé kanály se svým mobilním uzlem Blixt. Perfektní kombinace.

## Dunder LSP - Poskytovatel Likvidity

Jednoduchá a fantastická funkce, která novým uživatelům nabízí možnost okamžitě začít přijímat BTC na Lightning Network, bez nutnosti vkládat prostředky on-chain a poté otevírat LN kanály.
Pro nové uživatele je to skvělá zpráva, protože by měli být schopni začít od nuly, přímo na LN. K tomu jednoduše vytvořte LN fakturu z hlavní obrazovky na tlačítku "přijmout", zadejte částku, popis atd. a zaplaťte z jiné peněženky. Blixt otevře kanál až do 400k sats za každou přijatou transakci. Pokud je to nutné, můžete otevřít více kanálů.

Zajímavý a užitečný případ je následující: řekněme, že vaše první přijatá částka je 200k. Blixt otevře kanál s 400k sats, kde už na vaší straně bude 200k (minus poplatky za otevření), ale protože stále máte 200k "místa" dostupného, můžete přijmout více. Takže další platba, řekněme 100k, přijde přímo tímto kanálem, bez dalších poplatků, a stále máte 100k místa pro přijetí dalších.

Ale pokud se rozhodnete přijmout, řekněme, 300k za třetí platbu, vytvoří se další nový kanál s 400k a tyto 300k budou přesunuty na vaši stranu.

Pokud je příliš mnoho požadavků, uzel Blixt může upravit kapacitu kanálu během otevírání.

## Automatické otevírání kanálů

V nastavení může uživatel aktivovat tuto možnost a mít automatizovanou službu, která otevírá kanály s nejlepšími uzly a trasami na základě dostupného zůstatku v on-chain peněžence aplikace Blixt. Tato funkce je velmi výhodná pro nové uživatele, kteří nevědí, s kterým uzlem otevřít kanál a/nebo jak otevřít LN kanál. Je to jako autopilot pro LN.

> Pamatujte: tato možnost se používá pouze jednou, když vytváříte svou novou peněženku Blixt, a je ve výchozím nastavení povolena. Takže pokud nový uživatel naskenuje on-chain QR kód na hlavní obrazovce a vloží své první sats na tuto adresu, Blixt automaticky otevře kanál s těmito sats, s veřejným uzlem Blixt.

## Služby příchozí likvidity

Funkce určená pro obchodníky, kteří potřebují více PŘÍCHOZÍ likvidity, snadno použitelná. K tomu jednoduše vyberte jednoho z poskytovatelů likvidity ze seznamu, zaplaťte částku, kterou chcete za kanál, a poskytněte své ID uzlu, a odtud se otevře kanál do vašeho uzlu Blixt.

## Seznamy kontaktů

Užitečná funkce, pokud chcete mít trvalý seznam příjemců, se kterými obchodujete většinou času. Tento seznam může obsahovat LNURL, Lightning adresy nebo budoucí statické platební informace/faktury. Zatím tento seznam nelze uložit mimo aplikaci, ale plánuje se možnost jeho exportu.

## LNURL a Lightning adresa

Plná podpora LNURL. Můžete platit na LNURL, LN-auth, LN-chan požadavek s LNURL.
Můžete posílat na jakoukoli Lightning adresu a také ji přidat do svého seznamu kontaktů.
Také od verze 0.6.9 je možné přijímat na vaši vlastní Lightning adresu *@blixtwallet.com* typu, prostřednictvím funkce [Blixt Lightning Box](https://github.com/hsjoberg/lightning-box).

## Keysend

Velmi silná funkce, kterou má málo mobilních peněženek. Můžete posílat/tlačit finanční prostředky přímo přes kanál nebo směřovat na jiný uzel, přidat zprávu, pokud je to nutné. Je to jako tajný chat přes LN. Tato funkce je velmi užitečná pro zobrazování zpráv na billboardu Amboss.space ([zde je průvodce k tomuto billboardu Amboss](https://darthcoin.substack.com/p/amboss-billboard-amazing-tool)).

## Podpis zpráv
Velmi užitečný nástroj pro podepisování zpráv vaším soukromým klíčem uzlu Blixt, ověřování zpráv a tak dále. Velmi málo mobilních peněženek má tuto funkci, skoro žádná.
## Multi-Channel Payments - Multi-Path Payments (MPP)

Užitečná funkce pro platby přes LN, která umožňuje rozdělit LN platbu na několik částí přes více kanálů. Je to dobrý způsob, jak vyvážit likviditu v síti a zlepšit soukromí.

## Lightning Browser

Série služeb třetích stran s LN, organizovaných v jednoduchém, přístupném a uživatelsky přívětivém prohlížeči. Je to také dobrý způsob, jak propagovat podniky, které přijímají BTC na LN. Tato funkce bude v budoucnu dále vyvíjena. Zatím nefunguje za Tor, takže prohlížení těchto aplikací bude na clearnetu (otevřeném internetu).

## Log Explorers

Toto je mocný nástroj pro kontrolu LND logů a obecného stavu vašeho uzlu. Existuje možnost uložit logovací soubor. Je velmi užitečné mít tyto logy po ruce v případě, že potřebujete pomoc vývojáře při identifikaci určitých problémů.

## Bezpečnost

V nastavení aplikace můžete pro větší bezpečnost vaší peněženky/uzlu nastavit možnost spustit aplikaci s PIN kódem a/nebo otiskem prstu.

## On-chain Wallet

Tato funkce je trochu skrytá, v zásuvném menu vlevo nahoře. Jelikož není často používána uživatelem LN, není viditelná na hlavní obrazovce. Ale to nevadí, můžete ji mít na samostatné peněžence, kde můžete spravovat adresy a zobrazit log transakcí, například importem vašeho seedu do Sparrow. Možná v budoucnu bude peněženka Blixt také zahrnovat funkci pro správu UTxO. Ale prozatím POUŽÍVEJTE tuto on-chain peněženku POUZE pro otevírání nebo zavírání kanálů na LN.

## Speciální funkce

- S verzí 0.6.9 byl představen "persistent mode", který umožňuje uživatelům provozovat Blixt jako vždy online LN uzel, udržující služby LND aktivní a LN peněženku připravenou k přijímání/odesílání kdykoliv.
- Jednoduché Taproot kanály - umožňují otevírání Taproot kanálů pro větší soukromí a pokročilé funkce
- Kanály bez potvrzení s Blixt Dunder LSP
- Speedloader ("synchronizace LN kanálů") - To znamená, že všechny kanály budou rychle synchronizovány při spuštění, pro lepší hledání cest. I když je trochu otravné vidět na začátku obrazovku synchronizace, zajistí to, že peněženka bude vědět o všech kanálech a platby budou rychlejší a spolehlivější.
- Přeloženo do 25+ jazyků!

## "Velikonoční vajíčka"

Ano, v aplikaci Blixt jsou některé skryté funkce, malé věci, které činí aplikaci půvabnou, aktivují zábavné/zajímavé akce a reakce.
Tip: zkuste kliknout dvakrát na logo Blixt v zásuvném menu 🙂 Nechám na vás, abyste zbytek objevili.

# Průvodce prvními kroky s Blixt

> Jako nový uživatel LN, pokud začnete používat Blixt LN Node, budete nejprve potřebovat vědět, co je Lightning Network a jak funguje, alespoň na základní úrovni. [Zde jsme dali dohromady jednoduchý seznam zdrojů o Lightning Network](https://blixtwallet.github.io/faq#what-is-ln). Prosím, nejprve je přečtěte.”

Provozování plnohodnotného LN uzlu na mobilním zařízení není snadný úkol a může zabrat nějaké místo (min 600MB) a paměť. Doporučujeme mít dobré mobilní zařízení, aktualizované a používající alespoň Android 11 jako OS.

Jakmile otevřete Blixt, obrazovka „Vítejte“ vám nabídne několik možností:

![Demo Blixt 01](assets/blixt_t01.webp)
V pravém horním rohu uvidíte 3 tečky, které aktivují menu s:
- "enable Tor" - uživatel může začít používat síť Tor, zejména pokud chce obnovit starý LND uzel, který běžel pouze s Tor peers.

- "Set Bitcoin node" - pokud uživatel chce připojit k vlastnímu uzlu přímo, aby synchronizoval bloky prostřednictvím Neutrino, může tak učinit přímo z úvodní obrazovky. Tato možnost je také dobrá v případě, že vaše internetové připojení nebo Tor není dostatečně stabilní pro připojení k výchozímu bitcoinovému uzlu (node.blixtwallet.com).

## První krok - Vytvoření nové peněženky

Pokud se rozhodnete "vytvořit novou peněženku", budete přesměrováni přímo na hlavní obrazovku Blixt Wallet.

To je váš "kokpit" a také je to "Hlavní LN peněženka", takže buďte pozorní, zobrazí se vám zde pouze zůstatek vaší LN peněženky. Onchain peněženka je zobrazena samostatně (viz C).

![Demo Blixt 02](assets/blixt_t02.webp)

A - Ikona indikátoru synchronizace Blixt bloků. To je nejdůležitější věc pro LN uzel: být synchronizován se sítí. Pokud je tato ikona stále aktivní, znamená to, že váš uzel NENÍ PŘIPRAVEN! Takže mějte trpělivost, zejména při první počáteční synchronizaci. Může to trvat až 6-8 minut, v závislosti na vašem zařízení a internetovém připojení.

Můžete na ni kliknout a vidět stav synchronizace:

![Demo Blixt 03](assets/blixt_t03.webp)

Také můžete kliknout na tlačítko "Show LND Log" (A), pokud chcete vidět a číst více technických detailů z LND logu v reálném čase. Je to velmi užitečné pro ladění a učení se více o tom, jak LN funguje.

B - Zde máte přístup ke všem nastavením Blixt, a je jich hodně! Blixt nabízí mnoho bohatých funkcí a možností, jak spravovat váš LN uzel jako profesionál. Všechny tyto možnosti jsou podrobně vysvětleny na [“Stránce s funkcemi Blixt - Menu možností”](https://blixtwallet.github.io/features#blixt-options).

C - Zde máte menu "Magic Drawer", také podrobně vysvětlené zde. Zde je "Onchain Wallet" (B), Lightning Channels (C), Kontakty, ikona stavu kanálů (A), Keysend (D).

![Demo Blixt 04](assets/blixt_t04.webp)

D - Je to pomocné menu s odkazy na stránku FAQ / Průvodce, kontaktování vývojáře, Github stránku a skupinu podpory na Telegramu.

E - Ukazuje vaši první BTC adresu, kam můžete vložit vaše první testovací satoshi. TO JE VOLITELNÉ! Pokud vložíte přímo na tuto adresu, otevře se LN kanál směrem k Blixt uzlu. To znamená, že uvidíte vaše vložené satoshi, jak jdou do další onchain transakce (tx), pro otevření tohoto LN kanálu. Můžete to zkontrolovat v onchain peněžence Blixt (viz bod C), kliknutím na horní pravé menu TX.

![Demo Blixt 05](assets/blixt_t05.webp)

Jak můžete vidět v Logu onchain transakcí, kroky jsou velmi podrobně indikovány, kam satoshi jdou (vklad, otevření, uzavření kanálu)

> DOPORUČENÍ: Po testování několika situací jsme dospěli k závěru, že je mnohem efektivnější otevírat kanály mezi 1 a 5 M satoshi. Menší kanály mají tendenci rychle se vyčerpat a platit vyšší % poplatků ve srovnání s většími kanály.
F - Uveďte zůstatek vaší hlavní peněženky Lightning. To NENÍ celkový zůstatek vaší peněženky Blixt, reprezentuje pouze sats, které máte v Lightning kanálech, dostupné k odeslání. Jak bylo uvedeno dříve, peněženka Onchain je oddělená. Mějte na paměti tento aspekt. Peněženka Onchain je oddělena z důležitého důvodu: používá se hlavně pro otevírání/zavírání LN kanálů.
Takže teď jste vložili nějaké sats na tu onchain adresu zobrazenou na hlavní obrazovce. Doporučuje se, když to uděláte, nechat vaši aplikaci Blixt online a aktivní po nějakou dobu, dokud BTC transakce není přijata těžaři do prvního bloku.

Poté může trvat až 20-30 minut, než je plně potvrzena a kanál je otevřen a uvidíte ho v Magic Drawer - Lightning Channels jako aktivní. Také malá barevná tečka na vrchu zásuvky, pokud je zelená, bude indikovat, že váš LN kanál je online a připraven k použití pro odesílání sats přes LN.

Adresa a uvítací zpráva zobrazená zmizí. Není již nutné nyní otevírat automatický kanál. Tuto možnost můžete také deaktivovat v menu Nastavení.

Je čas pokračovat, testovat další funkce a možnosti otevření LN kanálů.

Nyní, otevřeme další kanál s dalším uzlovým peerem. Komunita Blixt dala dohromady [seznam dobrých uzlů pro začátek používání s Blixt.](https://github.com/hsjoberg/blixt-wallet/issues/1033)

### Postup otevření normálního neohlášeného (soukromého) LN kanálu ve vašem mobilním uzlu Blixt

Je to velmi jednoduché, stačí jen několik kroků a trochu trpělivosti:
- Přejděte na [seznam komunity Blixt](https://github.com/hsjoberg/blixt-wallet/issues/1033) dobrých peerů
- Vyberte uzl a klikněte na jeho název, otevře se jeho stránka Amboss
- Klikněte pro zobrazení QR kódu pro adresu URI uzlu

![Demo Blixt 06](assets/blixt_t06.webp)

Nyní otevřete Blixt a přejděte na horní zásuvku - Lightning Channels a klikněte na tlačítko “+”

![Demo Blixt 07](assets/blixt_t07.webp)

Nyní klikněte na (A) kameru pro skenování QR kódu ze stránky Amboss a detaily uzlu budou vyplněny. Přidejte množství sats pro kanál, který chcete, a poté vyberte sazbu poplatku za tx. Můžete nechat auto (B) pro rychlejší potvrzení nebo ji upravit ručně posunutím tlačítka. Můžete také dlouze stisknout číslo a upravit ho, jak chcete.

Nedávejte méně než 1 sat/vbyte! Obvykle je lepší [konzultovat poplatky mempoolu](https://mempool.space/) před otevřením kanálu a vybrat vhodný poplatek.

Hotovo, nyní stačí jen kliknout na tlačítko “otevřít kanál” a počkat na 3 potvrzení, což obvykle trvá 30 minut (1 blok přibližně každých 10min).

Jakmile je potvrzeno, uvidíte kanál aktivní ve vaší sekci “Lightning Channels”.

## Druhý krok - Získání více příchozí likvidity

Takže teď máme LN kanál pouze s ODCHOZÍ likviditou. To znamená, že můžeme pouze ODESÍLAT, stále nemůžeme PŘIJÍMAT sats přes LN. Proč? Četli jste průvodce uvedené na začátku? Ne? Vraťte se a přečtěte je. Je velmi důležité pochopit, jak LN kanály fungují.

![Demo Blixt 08](assets/blixt_t08.webp)
Jak můžete vidět na tomto příkladu, kanál otevřený s prvním vkladem nemá příliš mnoho vstupní likvidity ("Může přijímat"), ale má hodně výstupní likvidity ("Může posílat").
Jaké tedy máte možnosti, pokud chcete přes LN přijímat více satoshi?
- Utratit nějaké satoshi z existujícího kanálu. Ano, LN je platební síť Bitcoinu, používaná hlavně k rychlejšímu, levnějšímu, soukromému a snadnému utrácení vašich satoshi. LN NENÍ způsob, jak držet satoshi, pro to máte onchain peněženku.
- Vyměnit nějaké satoshi zpět do vaší onchain peněženky pomocí služby submarine swap. Tímto způsobem neutrácíte své satoshi, ale vracíte je zpět do vaší vlastní onchain peněženky. Zde můžete vidět podrobně některé metody na [stránce Blixt Guides](https://blixtwallet.github.io/guides).
- Otevřít vstupní kanál od jakéhokoli poskytovatele LSP. Zde je video demo o [tom, jak používat LNBig LSP pro otevření vstupního kanálu](https://blixtwallet.github.io/assets/images/blixt-lnbig.mp4). To znamená, že zaplatíte malý poplatek za prázdný kanál (na vaší straně) a budete moci do tohoto kanálu přijímat více satoshi. Pokud jste obchodník, který přijímá více než utrácí, je to dobrá možnost. Také pokud kupujete satoshi přes LN, používáte Robosats nebo jakoukoli jinou LN burzu.
- Otevřít Dunder kanál, s Blixt nodem nebo jakýmkoli jiným poskytovatelem Dunder LSP. Dunder kanál je jednoduchý způsob, jak získat nějakou vstupní likviditu, ale zároveň do tohoto kanálu vložíte nějaké satoshi. Je to také dobré, protože kanál otevře s [UTXO](https://en.bitcoin.it/wiki/UTXO), které není z vaší Blixt peněženky. To přidává určitou míru soukromí.
Je to také dobré, protože pokud nemáte satoshi v onchain peněžence, abyste mohli otevřít normální LN kanál, ale máte je v jiné LN peněžence, můžete jednoduše zaplatit z této jiné peněženky přes LN otevření a vklad (na vaší straně) tohoto Dunder kanálu. [Zde jsou podrobnosti o tom, jak Dunder funguje a jak spustit vlastní server.](https://github.com/hsjoberg/dunder-lsp)

![Demo Blixt 09](assets/blixt_t09.webp)

Zde jsou kroky, jak aktivovat otevření Dunder kanálu:
- Přejděte do Nastavení, v sekci "Experiments" aktivujte políčko pro "Enable Dunder LSP".
- Jakmile to uděláte, vraťte se zpět do sekce "Lightning Network" a uvidíte, že se objevila možnost "Set Dunder LSP Server". Tam je standardně nastaveno "https://dunder.blixtwallet.com", ale můžete to změnit na jakoukoli jinou adresu poskytovatele Dunder LSP. [Zde je seznam komunity Blixt](https://github.com/hsjoberg/blixt-wallet/issues/1033) s uzly, které mohou poskytovat kanály Dudner LSP pro vaši Blixt.
- Nyní můžete jít na hlavní obrazovku a kliknout na tlačítko "Přijmout". Poté postupujte podle tohoto postupu vysvětleného [v tomto průvodci](https://blixtwallet.github.io/guides#guide-lsp).

Takže po potvrzení Dunder kanálu (což zabere několik minut) skončíte s tím, že máte 2 LN kanály: jeden otevřený původně s autopilotem (kanál A) a jeden s větší vstupní likviditou, otevřený s Dunder (kanál B).
![Demo Blixt 10](assets/blixt_t10.webp)
Dobře, nyní jste připraveni posílat a přijímat dostatečné množství satoshi přes LN!

## Třetí krok - Procedura obnovení uzlu

Nyní se podíváme na to, jak obnovit peněženku Blixt nebo jakýkoliv jiný havarovaný uzel LND. Je to trochu techničtější, ale prosím, věnujte pozornost. Není to tak těžké.

> PŘIPOMÍNKA: V minulosti jsem napsal speciální příručku s několika možnostmi [jak obnovit havarovaný uzel LND](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario), kde jsem také zmínil metodu použití Blixtu jako rychlého procesu obnovy, použitím seedu + souboru channel.backup z vašeho mrtvého uzlu LND. Také jsem napsal příručku, jak obnovit váš uzel Blixt nebo přemigrovat váš Blixt na jiné zařízení, [zde](https://blixtwallet.github.io/faq#blixt-restore).

![Demo Blixt 11](assets/blixt_t11.webp)

Ale pojďme tento proces vysvětlit jednoduchými kroky. Jak můžete vidět na obrázku výše, jsou zde 2 věci, které musíte udělat pro obnovení vašeho předchozího uzlu Blixt/LND:
- horní pole, kam musíte vložit všech 24 slov z vašeho seedu (starý / mrtvý uzel)
- dole jsou dvě možnosti tlačítek pro vložení / nahrání souboru channel.backup, který jste dříve uložili z vašeho starého uzlu Blixt/LND. Může to být z lokálního souboru (dříve jste ho nahráli do vašeho zařízení) nebo může být z vzdálené lokace Google Drive / iCloud. Blixt má možnost uložit zálohu vašich kanálů přímo na Google / iCloud Drive. Více detailů najdete na [stránce s funkcemi Blixt](https://blixtwallet.github.io/features#blixt-options).

Není třeba zmiňovat, že pokud jste předtím neměli žádné otevřené LN kanály, není třeba nahrávat žádný soubor channel.backup. Jednoduše vložte 24 slovní seed a stiskněte tlačítko obnovit.

Nezapomeňte aktivovat Tor z horního menu se třemi tečkami, jak jsme vysvětlili v kapitole "První krok" tohoto průvodce. To je případ, kdy jste měli pouze Tor peers a nemohli být kontaktováni přes clearnet (doména/IP). V opačném případě to není nutné.

Další užitečnou funkcí je nastavit konkrétní Bitcoin uzel z tohoto horního menu. Ve výchozím nastavení synchronizuje bloky z node.blixtwallet.com (režim neutrino), ale můžete nastavit jakýkoliv jiný Bitcoin uzel, který poskytuje synchronizaci neutrino.

Jakmile vyplníte tyto možnosti a stisknete tlačítko obnovit, Blixt začne nejprve synchronizovat bloky prostřednictvím Neutrino, jak jsme vysvětlili v kapitole "První krok" tohoto průvodce. Buďte tedy trpěliví a sledujte proces obnovy na hlavní obrazovce kliknutím na ikonu synchronizace.

![Demo Blixt 12](assets/blixt_t12.webp)

Jak můžete vidět na tomto příkladu, ukazuje, že bitcoinové bloky jsou synchronizovány na 100% (A) a proces obnovy probíhá (B). To znamená, že LN kanály, které jste dříve měli, budou uzavřeny a prostředky obnoveny do vaší onchain peněženky Blixt.

Tento proces trvá čas! Buďte prosím trpěliví a snažte se udržet váš Blixt aktivní a online. Počáteční synchronizace může trvat až 6-8 minut a uzavírání kanálů až 10-15 minut. Takže je lepší mít zařízení dobře nabité.
Jakmile tento proces začne, můžete zkontrolovat ve "Magic Drawer - Lightning Channels" stav každého z vašich předchozích kanálů, které ukazují, že jsou ve stavu "pending to close". Jakmile se každý kanál uzavře, můžete vidět uzavírací transakci v onchain peněžence (viz "Magic Drawer - Onchain") a otevřít log menu transakce.
![Demo Blixt 13](assets/blixt_t13.webp)

Také bude dobré zkontrolovat a přidat, pokud tam nejsou, vaše dřívější protějšky, které jste měli ve vašem starém LN uzlu. Takže jděte do menu Nastavení, dolů na "Lightning Network" a vstupte do možnosti "Show Lightning Peers".

![Demo Blixt 14](assets/blixt_t14.webp)

V této sekci uvidíte protějšky, se kterými jste v daném okamžiku spojeni, a můžete přidat další, lépe ty, se kterými jste měli dříve kanály. Stačí jít na stránku Amboss, vyhledat aliasy vašich protějšků nebo nodeID a naskenovat jejich node URI.

![Demo Blixt 15](assets/blixt_t15.webp)

Jak můžete vidět na obrázku výše, jsou zde 3 aspekty:

A - představuje URI adresu uzlu v clearnetu (doména/IP)

B - představuje URI adresu uzlu v Tor onion (.onion)

C - je QR kód pro skenování vaší Blixt kamerou nebo tlačítko pro kopírování.

Tuto URI adresu uzlu musíte přidat do seznamu vašich protějšků. Takže si uvědomte, že nestačí jen alias uzlu nebo nodeID.

Nyní můžete jít do "Magic Drawer" (menu vlevo nahoře) - Lightning Channels, a můžete vidět, při které výšce bloku maturita budou prostředky vráceny na vaši onchain adresu.

![Demo Blixt 16](assets/blixt_t16.webp)

Tento blokový číslo 764272 je, kdy budou prostředky použitelné na vaší bitcoinové onchain adrese. A může to trvat až 144 bloků od prvního potvrzovacího bloku, než budou uvolněny. Takže to zkontrolujte na [the mempool](https://mempool.space/).

A to je vše. Jen trpělivě čekejte, dokud nebudou všechny kanály uzavřeny a prostředky zpět ve vaší onchain peněžence.

## Čtvrtý krok - Přizpůsobení

Tato kapitola je o přizpůsobení a lepším poznání vašeho Blixt uzlu. Nebudu popisovat všechny dostupné funkce, jsou jich příliš mnoho a již byly vysvětleny na [stránce s funkcemi Blixt](https://blixtwallet.github.io/features).

Ale poukážu na některé z nich, které jsou nezbytné pro další používání vašeho Blixtu a pro zajištění skvělého zážitku.

### A - Jméno (NameDesc)

![Demo Blixt 17](assets/blixt_t17.webp)

[The NameDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) je standard pro předávání "jména příjemce" v BOLT11 fakturách.

To může být jakékoli jméno a lze ho kdykoli změnit.

Tato možnost je velmi užitečná v různých případech, kdy chcete poslat jméno společně s popisem faktury, aby příjemce měl nápovědu, od koho ty sats obdržel. Toto je zcela volitelné a také na obrazovce platby musí uživatel zaškrtnout políčko, které indikuje odeslání aliasu jména.

Zde je příklad, jak by to vypadalo, když použijete [chat.blixtwallet.com](https://chat.blixtwallet.com/)

![Demo Blixt 18](assets/blixt_t18.webp)

Toto je další příklad odesílání do jiné peněženkové aplikace, která podporuje NameDesc:

![Demo Blixt 19](assets/blixt_t19.webp)

### B - Zálohování LN kanálů a seed slov

Toto je velmi důležitá funkce!
Po otevření nebo uzavření LN kanálu byste měli provést zálohu. Lze to udělat ručně uložením malého souboru na lokálním zařízení (obvykle ve složce ke stažení) nebo použitím účtu Google Drive nebo iCloud.
![Demo Blixt 20](assets/blixt_t20.webp)

Přejděte do nastavení Blixt - sekce Peněženka. Zde máte možnosti uložit všechna důležitá data pro vaši peněženku Blixt:
- “Zobrazit mnemoniku” - zobrazí 24 slov semínka, abyste si je mohli zapsat
- “Odstranit mnemoniku ze zařízení” - toto je volitelné a použijte to pouze, pokud opravdu chcete odstranit slova semínka ze svého zařízení. To NEsmaže vaši peněženku, pouze semínko. Ale buďte opatrní! Pokud jste si je nezapsali, není možné je obnovit.
- “Exportovat zálohu kanálu” - tato možnost uloží malý soubor na vaše lokální zařízení, obvykle do složky “stažené soubory”, odkud si jej můžete vzít a přesunout mimo vaše zařízení pro bezpečné uchování.
- “Ověřit zálohu kanálu” - to je dobrá možnost, pokud používáte Google Drive nebo iCloud, abyste zkontrolovali integritu vzdáleně provedené zálohy.
- “Záloha kanálu na Google Drive” - uloží záložní soubor do vašeho osobního Google Drive. Soubor je šifrován a je uložen v samostatném úložišti než vaše obvyklé google soubory. Takže nejsou žádné obavy, že by mohl být čten kýmkoli. Každopádně bez slov semínka je tento soubor zcela k ničemu, takže nikdo nemůže vzít vaše prostředky pouze z tohoto souboru.

Pro tuto sekci bych doporučil následující:
- použijte správce hesel pro bezpečné uložení vašeho semínka a záložního souboru. [KeePass](https://keepass.info/) nebo Bitwarden jsou pro to velmi dobré a mohou být použity na více platformách a self-hosted nebo offline.
- DĚLEJTE ZÁLOHU VŽDY, když otevřete nebo zavřete kanál. Ten soubor je aktualizován s informacemi o kanálech. Není potřeba to dělat po každé transakci, kterou jste na LN provedli. Záloha kanálu neukládá tyto informace, ukládá pouze stav kanálu.

![Demo Blixt 21](assets/blixt_t21.webp)

## Závěr

OK, Blixt nabízí mnoho dalších úžasných funkcí, nechám na vás, abyste je objevovali jeden po druhém a bavili se.

Tato aplikace je opravdu podceňovaná, hlavně proto, že není podporována žádným financováním od VC, je řízena komunitou, vytvořena s láskou a vášní pro Bitcoin a Lightning Network.

Tento mobilní LN uzel, Blixt, je velmi mocným nástrojem v rukou mnoha uživatelů, pokud vědí, jak ho správně používat. Jen si představte, že se pohybujete po světě s LN uzlem ve vlastní kapse a nikdo o tom nebude vědět.

A nemluvě o všech ostatních bohatých funkcích, které s sebou přináší, které velmi málo nebo žádné jiné aplikace peněženky nemohou nabídnout.

Doufám, že si její používání užijete. Osobně ji miluji a je pro mě velmi užitečná (viz zde případ použití, kde je tato peněženka skvělým nástrojem).

ŠŤASTNÉ BITCOINOVÉ BLESKOVÁNÍ!

Ať je s vámi ₿ITCOIN!

> UPOZORNĚNÍ: Za psaní tohoto průvodce nejsem nijak placen ani podporován vývojáři této aplikace. Napsal jsem tento průvodce, protože jsem viděl, že zájem o tuto aplikaci peněženky roste a noví uživatelé stále nerozumí, jak s ní začít. Také pomoci Hampusovi (hlavnímu vývojáři) s dokumentací o používání této peněženky uzlu. Nemám žádný jiný zájem na propagaci této LN aplikace, než posunout vpřed adopci Bitcoinu a LN. To je jediná cesta!