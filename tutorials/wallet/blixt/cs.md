---
name: Blixt Wallet
description: Jak začít používat výkonný uzel LN v mobilním telefonu?
---
![cover](assets/cover.webp)


Tato příručka je věnována všem novým uživatelům, kteří chtějí začít používat Bitcoin Lightning Network (LN) ZDARMA OPEN SOURCE, ÚPLNĚ NEKUSTODIÁLNÍM způsobem.


Pomocí [Blixt Wallet](https://blixtwallet.com/), plnohodnotného uzlu LN na mobilním telefonu, ať jste kdekoli.


Pokud jste nikdy nepoužili Bitcoin Lightning Network, než začnete, [přečtěte si prosím tuto jednoduchou analogii vysvětlení o Lightning Network (LN)](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## DŮLEŽITÉ ASPEKTY:



- Blixt je privátní uzel, nikoliv směrovací uzel! Mějte to na paměti : To znamená, že všechny kanály LN v Blixt budou neohlášené do grafu LN (tzv. soukromé kanály). To znamená, že tento uzel NEBUDE provádět směrování ostatních plateb přes uzel Blixt. Tento uzel Blixt NENÍ určen ke směrování, opakuji. Je hlavně proto, abyste mohli spravovat své vlastní kanály LN a provádět své platby LN soukromě, kdykoli potřebujete. Tento uzel Blixt je nutné mít online a synchronizovaný POUZE PŘED tím, než se chystáte provádět transakce. Proto se nahoře zobrazí ikona, která indikuje stav synchronizace. Trvá to jen několik okamžiků v závislosti na tom, jak dlouho jste jej drželi offline.



- Blixt používá LND (aezeed) jako backend Wallet, takže se do něj nepokoušejte importovat jiné typy peněženek Bitcoin. [Zde jste vysvětlili typy semen Wallet Mnemonic] (https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). A zde je [rozsáhlejší seznam všech typů peněženek](https://walletsrecovery.org/). Pokud jste tedy dříve měli uzel LND, můžete do Blixt importovat seed a záložní.kanály, [jak je vysvětleno v této příručce](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- Na konci této příručky najdete speciální část s ["tipy a triky"](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Další důležité odkazy - najdete je na konci této příručky a přidejte si je do záložek.


---

## Blixt - První kontakt


Takže... Darthova máma se rozhodla začít používat LN s Blixtem. Rozhodnutí Hard, ale moudré. Blixt je jen pro chytré lidi a ty, kteří se chtějí opravdu naučit více, hlubší využití LN.


![blixt](assets/en/01.webp)


Darth varuje svou matku:


"*Maminko, pokud začnete používat uzel Blixt LN, musíte nejprve vědět, co je to Lightning Network a jak funguje, alespoň na základní úrovni. [Zde jsem sestavil jednoduchý seznam zdrojů o Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Nejprve si je prosím přečtěte.*"


Darthova máma si přečetla zdroje a udělala první krok: nainstalovala si Blixt do svého zbrusu nového zařízení se systémem Android. Blixt je k dispozici také pro iOS a macOS (desktop). Ty však nejsou pro Darthovu mámu... Nicméně pro lepší kompatibilitu a zážitek se doporučuje používat novější verzi systému Android, alespoň 9 nebo 10. Spuštění plného uzlu LN na mobilním zařízení není snadný úkol a mohlo by zabrat nějaké místo (min. 600 MB) a paměť.


Po otevření aplikace Blixt se na obrazovce "Vítejte" zobrazí několik možností:


![blixt](assets/en/02.webp)


V pravém horním rohu se zobrazí 3 tečky, které aktivují nabídku s:



- "enable Tor" - uživatel může začít se sítí Tor, zejména pokud chce obnovit starý uzel LND, který byl spuštěn pouze s Tor peery.
- "Nastavit uzel Bitcoin" - pokud se uživatel chce připojit přímo k vlastnímu uzlu, aby mohl synchronizovat bloky prostřednictvím Neutrina, může to udělat hned na úvodní obrazovce. Tato možnost je také vhodná v případě, že vaše internetové připojení nebo Tor není tak stabilní, aby se dalo připojit k výchozímu uzlu Bitcoin (node.blixtwallet.com).
- Brzy tam bude přidán jazyk, takže uživatel může začít rovnou s jazykem, který mu vyhovuje. Pokud chcete do tohoto open source projektu přispět překladem do dalších jazyků, [připojte se prosím zde](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### MOŽNOST A - Vytvoření nového Wallet


Pokud zvolíte možnost "vytvořit nový Wallet", budete přesměrováni přímo na hlavní obrazovku aplikace Blixt Wallet.


Toto je váš "kokpit" a také "hlavní LN Wallet", takže si uvědomte, že vám ukáže pouze rovnováhu vašeho LN Wallet. Zapnutý řetězec Wallet se zobrazuje samostatně (viz C).


![blixt](assets/en/03.webp)


A - Ikona indikátoru synchronizace bloků Blixt. To je pro uzel LN nejdůležitější: být synchronizován se sítí. Pokud je tato ikona stále funkční, znamená to, že váš uzel NENÍ PŘIPRAVEN! Mějte tedy trpělivost, speciálně pro první počáteční synchronizaci. Může to trvat až 6-8 minut, v závislosti na vašem zařízení a připojení k internetu.


Můžete na něj kliknout a zobrazit stav synchronizace:


![blixt](assets/en/04.webp)


Pokud si chcete prohlédnout a přečíst další technické podrobnosti protokolu LND v reálném čase, můžete také kliknout na tlačítko "Zobrazit protokol LND" (A). Je velmi užitečné pro ladění a další informace o tom, jak LN funguje.


B - Zde máte přístup ke všem Blixt nastavení, a jsou hodně! Blixt nabízí mnoho bohatých funkcí a možností, jak spravovat uzel LN jako profesionál. Všechny tyto možnosti jsou podrobně vysvětleny v části "[Blixt Features Page](https://blixtwallet.github.io/features#blixt-options) - Options Menu".


C - Zde je k dispozici nabídka "Kouzelná zásuvka" [podrobněji vysvětleno také zde](https://blixtwallet.github.io/features#blixt-drawer). Zde je "Onchain Wallet" (B), Kanály blesků (C), Kontakty, ikona stavu kanálů (A), Keysend (D).


![blixt](assets/en/05.webp)


D - je nabídka nápovědy s odkazy na stránku s nejčastějšími dotazy / návody, kontakt na vývojáře, stránku Github a skupinu podpory Telegramu.


E - Uveďte svůj první BTC Address, kam můžete vložit svůj první testovací Sats. TENTO ÚDAJ JE NEPOVINNÝ! Pokud vložíte přímo do tohoto Address, je otevření kanálu LN směrem k uzlu Blixt. To znamená, že uvidíte svůj vložený Sats, který jde do další onchain transakce (tx), pro otevření tohoto LN kanálu. To můžete zkontrolovat do onchainu Blixt Wallet (viz bod C), kliknutím na menu TX vpravo nahoře.


![blixt](assets/en/06.webp)


Jak vidíte v protokolu transakcí Onchain, kroky jsou velmi podrobné a je v nich uvedeno, kam Sats směřují (vklad, otevření, uzavření kanálu).


DOPORUČENÍ:


Po otestování několika situací jsme dospěli k závěru, že je mnohem účinnější otevřít kanály mezi 1 a 5 M Sats. Menší kanály mají tendenci být rychle vyčerpány a platit vyšší % poplatků ve srovnání s většími kanály.


F - Uveďte hlavní zůstatek blesku Wallet. NEJEDNÁ se o celkový zůstatek na účtu Blixt Wallet, ale pouze o zůstatek Sats, který máte v kanálech Lightning a který můžete odeslat. Jak bylo uvedeno dříve, Onchain Wallet je samostatný. Mějte na paměti tento aspekt. Onchain Wallet je oddělený z důležitého důvodu: používá se hlavně pro otevírání/uzavírání kanálů LN.


Dobře, takže Darthova máma teď uložila nějaký Sats do toho řetězce Address zobrazeného na hlavní obrazovce. Doporučuje se, abyste při tomto úkonu nechali aplikaci Blixt chvíli online a aktivní, dokud těžaři nepřijmou BTC tx do prvního bloku.


Poté může trvat až 20-30 minut, než se plně potvrdí a kanál bude otevřen a zobrazí se v Magické zásuvce - Kanály blesků jako aktivní. Také malá barevná tečka v horní části zásuvky, pokud je Green, bude indikovat, že váš kanál LN je online a je připraven k použití pro odeslání Sats přes LN.


Zobrazené okno Address a uvítací zpráva zmizí. Nyní již není nutné otevírat automatický kanál. Tuto možnost můžete také deaktivovat v nabídce Nastavení.


Je čas přejít na testování dalších funkcí a možností otevření kanálů LN.


Nyní otevřeme další kanál s jiným uzlem peer. Komunita Blixt sestavila [seznam dobrých uzlů, které lze začít používat s Blixtem](https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Postup pro otevření kanálu LN v aplikaci Blixt**


Je to velmi jednoduché, stačí jen několik kroků a trocha trpělivosti:



- Dostal jsem se do seznamu [Blixt Community](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- Vyberte uzel a klikněte na jeho název odkaz, otevře se jeho stránka Amboss
- Kliknutím zobrazíte QR kód pro uzel URI Address


![blixt](assets/en/07.webp)


Otevřete aplikaci Blixt, přejděte do horní zásuvky - Lightning Channels a klikněte na tlačítko "+"


![blixt](assets/en/08.webp)


Nyní klikněte na fotoaparát (A) a naskenujte QR kód ze stránky Amboss, čímž se vyplní údaje o uzlu. Přidejte částku Sats pro požadovaný kanál a poté vyberte sazbu poplatku za tx. Pro rychlejší potvrzení ji můžete ponechat automatickou (B) nebo ji nastavit ručně posunutím tlačítka. Číslo můžete také dlouze stisknout a upravit podle svých představ.


Nevkládejte méně než 1 sat/vbyte ! Obvykle je lepší se před otevřením kanálu podívat do [Mempool fees](https://Mempool.space/) a vybrat vhodný poplatek.


Hotovo, nyní stačí kliknout na tlačítko "otevřít kanál" a počkat na 3 potvrzení, což obvykle trvá 30 min (1 blok přibližně každých 10 min).


Po potvrzení se kanál zobrazí aktivní v sekci "Lightning Channels".


---

## Blixt - Druhý kontakt


Dobře, takže nyní máme kanál LN pouze s likviditou OUTBOUND. To znamená, že můžeme pouze ODESÍLAT, ale stále nemůžeme PŘIJÍMAT Sats přes LN.


![blixt](assets/en/09.webp)


Proč? Četli jste průvodce uvedené na začátku? Ne? Vraťte se k nim a přečtěte si je. Je velmi důležité pochopit, jak kanály LN fungují.


![blixt](assets/en/10.webp)


Jak vidíte v tomto příkladu, kanál otevřený prvním vkladem nemá příliš velkou likviditu INBOUND ("Can receive"), ale má velkou likviditu OUTBOUND ("Can send").


Jaké máte možnosti, pokud chcete získat více Sats než LN?



- Strávit nějaké Sats ze stávajícího kanálu. Ano, LN je platební síť Bitcoin, která slouží především k rychlejšímu, levnějšímu, soukromému a snadnému utrácení Sats. LN NENÍ způsob hodlingu, na to máte onchain Wallet.



- Vyměňte některé Sats zpět do řetězce Wallet pomocí služby výměny ponorek. Tímto způsobem neutrácíte své Sats, ale vracíte je zpět do svého vlastního onchainu Wallet. Některé metody si můžete podrobně prohlédnout zde, na stránce [Blixt Guides Page](https://blixtwallet.github.io/guides).



- Otevřete kanál INBOUND od libovolného poskytovatele LSP. Zde je video ukázka, jak používat LNBig LSP pro otevření příchozího kanálu. To znamená, že zaplatíte malý poplatek za EMPTY kanál (na vaší straně) a budete moci přijímat další Sats do tohoto kanálu. Pokud jste obchodník, který přijímá více než utrácí, je to dobrá možnost. Také pokud kupujete Sats přes LN, používáte Robosaty nebo jakýkoli jiný LN Exchange.



- Otevřete kanál Dunder s uzlem Blixt nebo jiným poskytovatelem LSP Dunder. Kanál Dunder je jednoduchý způsob, jak získat nějakou likviditu INBOUND, ale zároveň do tohoto kanálu vložíte nějaký Sats. Je také dobré, protože otevře kanál s [UTXO](https://en.Bitcoin.it/wiki/UTXO), který není z vašeho Blixt Wallet. To přidá trochu soukromí. Je také dobré, protože pokud nemáte Sats do onchainu Wallet, abyste otevřeli normální kanál LN, ale máte je do jiného LN Wallet, můžete prostě zaplatit z tohoto jiného Wallet prostřednictvím LN otevření a vklad (na vaší straně) tohoto dunderského kanálu. [Více informací o tom, jak Dunder funguje a jak provozovat vlastní server, najdete zde] (https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Zde jsou uvedeny kroky k aktivaci otevření kanálu Dunder:



- Přejděte do Nastavení a v části Experimenty aktivujte políčko "Povolit Dunder LSP".
- Jakmile tak učiníte, vraťte se do sekce "Lightning Network" a uvidíte, že se objevila možnost "Set Dunder LSP Server". Tam je ve výchozím nastavení nastaven "https://dunder.blixtwallet.com", ale můžete jej změnit pomocí libovolného jiného poskytovatele Dunder LSP Address. [Zde je seznam komunity Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033) s uzly, které mohou poskytovat kanály Dudner LSP pro váš Blixt.
- Nyní můžete přejít na hlavní obrazovku a kliknout na tlačítko "Receive". Poté postupujte podle tohoto postupu [vysvětleného v této příručce](https://blixtwallet.github.io/guides#guide-lsp).


OK, takže po potvrzení kanálu Dunder (bude trvat několik minut) budete mít 2 kanály LN: jeden otevřený původně s autopilotem (kanál A) a druhý s větší příchozí likviditou, otevřený s Dunderem (kanál B).


![blixt](assets/en/12.webp)


Dobře, nyní můžete odesílat a přijímat dostatečné množství Sats přes LN!


ŠŤASTNÝ BLESK Bitcoin!


---

## Blixt - Třetí kontakt


Pamatujte si, že v první kapitole "První kontakt" byly na uvítací obrazovce 2 možnosti:


- [Možnost A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Vytvoření nového Wallet
- Možnost B - Obnovení Wallet


Nyní si tedy řekneme, jak obnovit havarovaný uzel Blixt Wallet nebo jakýkoli jiný uzel LND. Je to trochu techničtější, ale věnujte tomu prosím pozornost. Není to Hard.


### MOŽNOST B - Obnovení Wallet


V minulosti jsem napsal speciální návod [jak obnovit havarovaný uzel Umbrel](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), kde jsem se zmínil také o metodě použití Blixtu jako rychlého procesu obnovy pomocí souboru seed + channel.backup z Umbrelu.


Napsal jsem také návod, jak obnovit uzel Blixt nebo migrovat uzel Blixt na jiné zařízení, [zde](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Vysvětleme si však tento proces v jednoduchých krocích. Jak vidíte na obrázku výše, pro obnovení předchozího uzlu Blixt/LND byste měli udělat dvě věci:



- v horním poli je třeba vyplnit všech 24 slov z vašeho seed (starý / mrtvý uzel)
- dole jsou dvě možnosti tlačítek pro vložení / nahrání souboru channel.backup, dříve uloženého ze starého uzlu Blixt/LND. Může být z místního souboru (nahrajete jej do zařízení dříve) nebo může být ze vzdáleného umístění na disku Google / iCloud. Blixt má tuto možnost uložit zálohu kanálů přímo na disk Google / iCloud. Další podrobnosti naleznete na stránce [Blixt Features Page](https://blixtwallet.github.io/features#blixt-options).


Nicméně pokud jste dříve neměli otevřené žádné kanály LN, není třeba nahrávat žádný soubor channels.backup. Stačí vložit 24 slov seed a stisknout tlačítko obnovit.


Nezapomeňte aktivovat Tor v horní nabídce se třemi tečkami, jak jsme vysvětlili v části Možnost A. To je případ, kdy jste měli POUZE Tor peery a nemohli jste být kontaktováni přes clearnet (doména/IP). V opačném případě není nutné.


Další užitečnou funkcí je nastavení konkrétního uzlu Bitcoin z této horní nabídky. Ve výchozím nastavení synchronizuje bloky z node.blixtwallet.com (režim neutrino), ale můžete nastavit jakýkoli jiný uzel Bitcoin, který poskytuje synchronizaci neutrino.


Jakmile tedy vyplníte tyto možnosti a stisknete tlačítko obnovit, Blixt začne nejprve synchronizovat bloky prostřednictvím Neutrina, jak jsme vysvětlili v kapitole První kontakt. Buďte tedy trpěliví a sledujte proces obnovy na hlavní obrazovce kliknutím na ikonu synchronizace.


![blixt](assets/en/14.webp)


Jak vidíte na tomto příkladu, bloky Bitcoin jsou 100% synchronizovány (A) a proces obnovy probíhá (B). To znamená, že kanály LN, které jste měli dříve, budou uzavřeny a prostředky obnoveny do vašeho Blixt onchainu Wallet.


Tento proces vyžaduje čas! Buďte prosím trpěliví a snažte se udržovat svůj Blixt aktivní a online. Počáteční synchronizace může trvat až 6-8 minut a uzavření kanálů může trvat až 10-15 minut. Proto raději mějte zařízení dobře nabité.


Po spuštění tohoto procesu můžete zkontrolovat stav všech svých předchozích kanálů v zásuvce Magic Drawer - Lightning Channels,kde se zobrazují kanály ve stavu "čekající na uzavření". Jakmile je každý kanál uzavřen, mohli byste v onchainu Wallet (viz Magická zásuvka - Onchain) zobrazit uzavírací tx a otevřít protokol nabídky tx.


![blixt](assets/en/15.webp)


Také bude dobré zkontrolovat a přidat, pokud tam nejsou, vaše dřívější vrstevníky, které jste měli ve starém uzlu LN. Přejděte tedy do nabídky Nastavení, dolů na "Lightning Network" a zadejte možnost "Zobrazit vrstevníky Lightning".


![blixt](assets/en/16.webp)


Uvnitř sekce uvidíte kolegy, které máte v danou chvíli připojené, a můžete přidat další, lépe přidat ty, které jste měli kanály předtím. Stačí přejít na stránku [Amboss page](https://amboss.space/), vyhledat aliasy uzlů vašich peerů nebo nodeID a naskenovat jejich URI uzlu.


![blixt](assets/en/17.webp)


Jak můžete vidět na obrázku výše, jsou 3 aspekty:


A - představuje URI uzlu clearnetu Address (doména/IP)


B - představuje uzel Tor onion Address URI (.onion)


C - je QR kód, který naskenujete pomocí fotoaparátu Blixt nebo tlačítka kopírování.


Tento uzel Address URI musíte přidat do seznamu partnerů. Proto si uvědomte, že nestačí jen název aliasu uzlu nebo nodeID.


Nyní můžete přejít do zásuvky Magic Drawer (menu vlevo nahoře) - Lightning Channels a uvidíte, při jaké výšce bloku splatnosti budou prostředky vráceny do vašeho onchainu Address.


![blixt](assets/en/18.webp)


Tento blok číslo 764272 je okamžik, kdy budou prostředky použitelné ve vašem řetězci Bitcoin onchain Address. A může to trvat až 144 bloků od 1. potvrzovacího bloku, než budou uvolněny. [Takže si to zkontrolujte v Mempool] (https://Mempool.space/).


A to je vše. Stačí trpělivě počkat, až se uzavřou všechny kanály a prostředky se vrátí zpět do řetězce Wallet.


👉 **Tajná metoda obnovy :**


Existuje ještě jedna metoda, jak obnovit uzel Blixt LND, aniž byste museli zavírat kanály. Je však skryta běžným uživatelům-noobům, protože tato metoda je určena POUZE pro ty, kteří vědí, co dělají.


V případě, že potřebujete migrovat stávající (funkční) uzel Blixt na jiné nové zařízení, aniž byste museli uzavřít stávající kanály LN, musíte provést tyto kroky:



- Předpokládáme, že jste již uložili Blixt Wallet seed (24 slov aezeed)
- Ve starém zařízení přejděte do části "Nastavení" - ladění - "Kompaktní databáze LND". Tento krok je nepovinný, ale doporučuje se, pokud chcete menší velikost souboru channel.db. Obvykle je poměrně velký, v závislosti na aktivitě vašeho uzlu. Tím se restartuje program Blixt a zkomprimuje se velikost souboru db.
- Po restartu přejděte do "Nastavení" a změňte svůj běžný alias na "Hampus". Tím aktivujete skryté možnosti, které jsou určeny pouze pro pokročilé uživatele.
- Přejděte dolů do sekce "Ladění" a uvidíte novou možnost "Exportovat soubor channel.db". POZOR! Jakmile provedete tento export, stávající uzel Blixt LN bude v tomto starém zařízení deaktivován a bude exportována celá databáze uzlů (channel.db) připravená k importu do nového zařízení.
- Tento soubor db bude uložen do určené složky ve starém zařízení (Dokumenty nebo Stažené soubory) a odtud jej budete muset v nezměněné podobě přesunout do nového zařízení. K přenosu souboru přímo mezi zařízeními můžete použít například aplikaci [LocalSend FOSS](https://github.com/localsend/localsend).
- V tuto chvíli MUSÍ váš starý Blixt zůstat vypnutý. NEOTEVÍREJTE JEJ ZNOVU!
- Po přenesení souboru channel.db do nového zařízení spusťte novou instalaci aplikace Blixt a na první obrazovce vyberte možnost "Obnovit Wallet".
- Na tlačítku, kde je napsáno "Vybrat soubor SCB", dlouze stiskněte (NE jednoduše klikněte!) a poté se zobrazí možnost vybrat soubor channel.db, který uložíte lokálně do nového zařízení. Pokud toto tlačítko pouze jednoduše stisknete, použije se ve výchozím nastavení soubor SCB (s uzavíracími kanály), nefunguje to pro plné zálohy živých kanálů.
- Vložte 24 slov seed a klikněte na tlačítko "Obnovit"
- Uvidíte, že se služba Blixt začne synchronizovat se službou Neutrino. Můžete také sledovat protokoly synchronizace.
- MĚJTE NA PAMĚTI! V této fázi se snažte mít neustále otevřený Blixt! Nenechávejte jej přejít do režimu spánku ani nezavírejte obrazovku aplikace. To by mohlo narušit počáteční synchronizaci a museli byste ji provést znovu. Trpělivě vyčkejte, netrvá to déle než několik minut.
- Po dokončení synchronizace počátečních bloků rychle prohledá vaše předchozí adresy Wallet a vaše kanály budou opět online, živé a zdravé.
- Bohužel předchozí historii plateb a kontaktů (zatím) není možné obnovit. Ale to stejně není tak důležité.


A hotovo! Nyní máte plně obnovený uzel Blixt LN. Mohlo by to fungovat i s jinými zálohami LND (Umbrel, Raspiblitz atd.), pokud jste předtím správně uložili soubor channel.db. Blixt tedy může doslova zachránit jakýkoli mrtvý uzel LND.


---

## Blixt - Čtvrtý kontakt


Tato kapitola se zabývá přizpůsobením a poznáním Blixt Node. Nebudu popisovat všechny dostupné funkce, je jich příliš mnoho a byly již vysvětleny v [Blixt Features Page](https://blixtwallet.github.io/features).


Upozorním však na některé z nich, které jsou nezbytné pro to, abyste mohli Blixt používat a mít s ním skvělé zkušenosti.


### A - Název (NameDesc)


![blixt](assets/en/19.webp)


[NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) je standard pro vyjádření "názvu příjemce" ve fakturách BOLT11.


Toto jméno může být libovolné a lze je kdykoli změnit.


Tato možnost je opravdu užitečná v různých případech, kdy chcete spolu s popisem Invoice odeslat i jméno, aby příjemce mohl mít nápovědu, kdo tyto Sats přijal. Tato možnost je plně volitelná a také na obrazovce platby musí uživatel zaškrtnout políčko označující odeslání jména přezdívky.


Zde je příklad, jak by se zobrazil, kdybyste použili [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


Toto je další příklad odeslání do jiné aplikace Wallet, která podporuje NameDesc:


![blixt](assets/en/21.webp)


### B - Lightning Box


Počínaje novou verzí v0.6.9-420 [nedávno oznámenou](https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420) zavedl Blixt novou výkonnou funkci pro Lightning Address v Blixt.


Tato nová funkce je volitelná, není ve výchozím nastavení zapnutá!


V současné době je výchozí LN Box provozován serverem Blixt a nabízí @blixtwallet.com LN Address. Ale KAŽDÝ, kdo má veřejný uzel LND, může provozovat server Lightning Box a nabízet LN Address pro svou vlastní doménu, self-custody.


V současné době server Blixt přeposílá platby zaslané na adresy LN @blixtwallet.com pouze uživatelům služby Blixt, kteří si nastavili LN Address. Uživatelé musí svůj uzel Blixt Wallet uvést do "trvalého režimu", aby mohli tyto platby přijímat na své adresy @blixtwallet.com LN.


V poznámkách k vydání naleznete videoukázku, jak nastavit LN Address v aplikaci Blixt.


Tento LN Address implementovaný do aplikace Blixt Wallet je jako chat přes LN, okamžitý a zábavný, také podporuje [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (přidání jména aliasu k platbě). Do seznamu kontaktů si můžete přidat všechny své běžné adresy LN, které volně používáte, a mít je po ruce pro chatování. Nyní lze Blixt považovat za plnohodnotnou chatovací aplikaci LN 😂😂.


Další užitečnou funkcí je plná podpora LUD-18 (kterou podporuje i [Stacker.News](https://stacker.news/r/DarthCoin) a další).


![blixt](assets/en/22.webp)


Jak vidíte na výše uvedeném snímku obrazovky, při odesílání z účtu Stacker News se pěkně zobrazilo logo + LN Address + zpráva. Stejně funguje i odesílání z Blixt, můžete připojit svůj Blixt LN Address nebo jednoduše přidat jméno aliasu (dříve nastavené v nastavení Blixt) nebo dokonce obojí.


Tato možnost z LUD-18 by mohla být užitečná také pro služby předplatného, kde uživatel může poslat určitý alias (NENÍ to alias vašeho uzlu nebo vaše skutečné jméno!) a na základě toho by mohl být zaregistrován nebo obdržet zpět určitou zprávu nebo cokoli jiného. Připojení jména aliasu ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+komentáře ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) k platbě LN může mít více případů použití!


Zde je kód pro [Lightning Box](https://github.com/hsjoberg/lightning-box), pokud jej spustíte pro sebe, pro svou rodinu a přátele, na svém vlastním uzlu.


Zde také můžete spustit [LSP Dunder server](https://github.com/hsjoberg/dunder-lsp) pro mobilní uzly Blixt a nabízet likviditu pro uživatele Blixt, pokud máte dobrý veřejný uzel LN (funguje pouze s LND).


### C - Záložní kanály LN a slova seed


To je velmi důležitá funkce!


Po otevření nebo uzavření kanálu LN byste měli provést zálohu. To lze provést ručně uložením malého souboru na místní zařízení (obvykle do složky ke stažení) nebo pomocí účtu Google Drive nebo iCloud.


![blixt](assets/en/23.webp)


Přejděte do části Nastavení Blixt - Wallet. Zde máte k dispozici možnosti uložení všech důležitých údajů pro váš Blixt Wallet:



- "Zobrazit Mnemonic" - zobrazí 24 slov seed pro jejich zapsání
- "Remove Mnemonic from device" - tato možnost je volitelná a použijte ji pouze v případě, že chcete slova seed ze zařízení skutečně odstranit. Tímto způsobem NEBUDE vymazáno slovo Wallet, ale pouze slovo seed. Dávejte však pozor ! Neexistuje způsob, jak je obnovit, pokud jste je předtím nezapsali.
- "Exportovat zálohu kanálu" - tato možnost uloží malý soubor do místního zařízení, obvykle do složky "Downloads", odkud jej můžete pro jistotu vzít a přesunout mimo zařízení.
- "Ověřit zálohu kanálu" - tato možnost je vhodná, pokud používáte Google drive nebo iCloud pro kontrolu integrity zálohy provedené na dálku.
- " Záloha kanálu Google drive" - uloží soubor zálohy na váš osobní disk Google. Soubor je zašifrován a je uložen v jiném úložišti než vaše běžné soubory Google. Nehrozí tedy žádné obavy, že by jej mohl kdokoli přečíst. Každopádně je tento soubor bez slov seed zcela nepoužitelný, takže nikdo nemůže vzít vaše prostředky pouze z tohoto souboru.


Pro tuto část bych doporučil následující:



- použijte správce hesel k bezpečnému uložení souboru seed a zálohy. KeePass nebo Bitwarden jsou k tomu velmi dobré a lze je používat na více platformách a na vlastním hostingu nebo offline.
- ZÁLOHUJTE VŽDY, když otevřete nebo zavřete kanál. Tento soubor se aktualizuje o informace o kanálech. Není nutné ji provádět po každé transakci, kterou jste provedli v LN. Záloha kanálu tyto informace neukládá, ukládá pouze stav kanálu.


![blixt](assets/en/24.webp)


---

## Blixt - Tipy a triky


### PŘÍPAD 1 - PROBLÉMY SE SYNCHRONIZACÍ


"_Můj Blixt se nesynchronizuje... Můj Blixt nezobrazuje zůstatek... Můj Blixt nemůže otevřít kanály... Zkoušel jsem ho obnovit v jiném zařízení... atd_"


Všechny tyto problémy začínají tím, že vaše zařízení není správně synchronizováno. Pochopte prosím tento důležitý aspekt: Blixt je mobilní uzel LND, který pro synchronizaci / čtení bloků používá Neutrino.



- Zde je méně technické vysvětlení z časopisu [Bitcoin](https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Zde jsou další technické zdroje z [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/)
- Zde je návod, jak můžete aktivovat Neutrino na svém domovském uzlu a servírovat filtry bloků pro svůj mobilní uzel, z [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


UPOZORNĚNÍ: Používání Neutrina přes clearnet je naprosto bezpečné, vaše IP nebo xpub nejsou prozrazeny. Pomocí neutrina pouze čtete bloky ze vzdáleného uzlu. To je vše. Vše ostatní se provádí na vašem lokálním zařízení.


Není tedy nutné jej používat s aplikací Tor. Tor přidá do procesu synchronizace obrovské zpoždění a způsobí, že váš Blixt bude velmi nestabilní. Pokud opravdu chcete používat přes Tor, ujistěte se, co děláte, a mějte dobré připojení a trpělivost. Stejný případ platí i pro používání VPN. Dávejte si pozor, jakou latenci vám tato VPN poskytuje.


Zpoždění neutrinového serveru můžete otestovat jednoduchým pingem z počítače nebo z mobilního telefonu.


![blixt](assets/en/25.webp)


Toto je obvyklý ping na server neutrino europe.blixtwallet.com, který ukazuje, že připojení je velmi dobré s dobou odezvy avg 50 ms a TTL 51. Doba odezvy se může lišit, ale ne příliš. TTL musí být stabilní.


Pokud jsou tyto hodnoty vyšší než 100-150 ms, váš synchronizační proces bude zastaralý, nebo ještě hůře, může to způsobit uzavření kanálů ze strany peerů! Neignorujte tento aspekt.


Bez správné synchronizace se také nezobrazí správné vyvážení nebo se kanály LN nedostanou online a nebudou funkční. Nezáleží na tom, kolik giga ultra terra mbps máte rychlost stahování NEMÁ význam. Záleží na časové odezvě a TTL (time to live).


To je jako obecný případ pro uživatele z LATAM. Nevím, co se tam dole děje, ale vy máte příšerné připojení s pingy přes 200 ms, které mohou narušit jakoukoli synchronizaci.


Jaké je tedy řešení pro tyto zoufalé uživatele?



- přestat používat Blixt s Tor. Je naprosto k ničemu
- můžete použít VPN, ale zvolte ji s rozmyslem a neustále sledujte ping. Použijte takovou, která je blíže vaší zeměpisné poloze. Vzdálenost znamená delší dobu odezvy ms, nezapomeňte.
- vyberte si moudře své neutrinové partnery, zde je seznam známých veřejných neutrinových serverů:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Dalším způsobem je vybrat jeden z tohoto seznamu uzlů oznamujících "kompaktní filtry" (BIP157 / neutrino) - [Bitnodes Page Neutrino filter](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Vyberte si ten, který je blíže vaší zeměpisné poloze.


Dalším způsobem (nejlepším) je připojení k místnímu komunitnímu uzlu, který provozuje váš přítel nebo skupina, kterou znáte a která nabízí neutrinové připojení. [Zde je návod, jak to udělat] (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Jejich uzel nebude nijak ovlivněn, potřebují jen stabilní a veřejné připojení.


V regionu LATAM je potřeba více neutrinových serverů pro lepší a rychlejší synchronizaci. Zorganizujte se proto, prosím, s místní komunitou Bitcoin a rozhodněte, kdo a kde provozuje jádro Bitcoin + neutrino pro vlastní potřebu. Stačí k tomu jen veřejná IP adresa. Pokud nemáte přístup k veřejné IP, můžete použít IP VPS a vytvořit wireguard tunel do svého domovského uzlu. Tímto způsobem přesměrujete veškerý provoz na místní IP adresu VPS, aniž byste odhalili jakékoli soukromé informace o svém domácím uzlu.


### PŘÍPAD 2 - NIKDY NEDOKONČIT SYNCHRONIZACI


"_Můj Blixt má dobré spojení s neutrinovým serverem, ale zasekla se synchronizace._"


#### Časový server


Někdy lidé používají různá stará zařízení nebo nejsou správně připojeni k časovému serveru. Neutrino synchronizuje v pořádku, dokud se nedostane k aktuálním blokům, které neodpovídají skutečnému místnímu času. V protokolech Blixt LND se objeví chyba, která říká, že "časové razítko bloku je daleko od budoucnosti" nebo něco souvisejícího s "hlavička neprošla kontrolou přípustnosti".


Rychlá oprava: nastavte správný čas a datum pro své zařízení a restartujte aplikaci Blixt.


#### Málo místa v zařízení


Někdy se může stát, že při použití starého zařízení s malým prostorem dosáhne prahové hodnoty a zasekne se. Skutečně pro více používáte tento mobilní uzel LND, neutrální soubory se zvětšují a také soubor channel.db.


Rychlá oprava: Přejděte na Blixt Options - Debug section - Vyberte "stop LND and delete neutrino files". Tím se aplikace restartuje a spustí se nová čerstvá synchronizace. Někdy tato rychlá oprava může opravit i poškozená data. Mějte na paměti, že úplná resynchronizace bude nějakou dobu trvat, 1 až 3 minuty. NEMÁ to za následek odstranění stávajících fondů nebo kanálů, ale ano, po obnovení synchronizace to může vyvolat opětovné skenování adres Bitcoin a to může trvat déle.


V dalším kroku zkontrolujte, kolik dat je ještě obsazeno. To můžete zjistit v informacích o aplikaci Android - data. Pokud je stále větší než 400-500 MB, můžete soubory LND zkomprimovat. Přejděte tedy do sekce Blixt Options - Debug - vyberte možnost "Compact DB LND". Pokud se tak neděje automaticky, restartujte aplikaci Blixt. Kompaktování probíhá při spuštění a je pouze jednorázové. Nyní uvidíte, že data Blixt jsou více méně obsazena.


#### Trvalý režim


Někdy lidé neotevřou Blixt po dlouhou dobu, takže je příliš stará synchronizace. Očekávají však, že po otevření bude synchronizován okamžitě.


Mějte prosím trpělivost a podívejte se na horní otočné kolo. Volitelně můžete přejít do nabídky Možnosti - Zobrazit informace o uzlu a podívat se, zda je synchronizace s řetězcem a synchronizace s grafem označena jako "true". Bez této zmínky "true" nemůžete správně používat Blixt, nevidíte správně zůstatek, nevidíte online kanály LN, nemůžete provádět platby.


Rychlá oprava: K dispozici je výkonná možnost "udržet při životě" uzel Blixt. Přejděte na Možnosti - Experimenty - Vyberte "Aktivovat trvalý režim". Tím restartujete svůj uzel Blixt a přepnete službu LND do trvalého režimu, tj. bude vždy aktivní a udrží online vaši synchronizaci, i když přepnete na jinou aplikaci nebo jednoduše zavřete uzel Blixt (nikoli násilně zavřít nebo zabít úlohu). Můžete to tak nechat celý den, pokud jste ve stabilním připojení a potřebujete Blixt použít několikrát. Nebude to příliš spotřebovávat baterii.


### PŘÍPAD 3 - CHCI PŘEJÍT NA JINÉ ZAŘÍZENÍ


OK o tomto scénáři jsem napsal rozsáhlý návod na [FAQ stránku](https://blixtwallet.github.io/faq#blixt-restore): s 2 možnostmi, rychlé (kooperativní uzavření kanálů před migrací) a pomalé (vynutit uzavření kanálů, protože staré zařízení je mrtvé).


Chci zde však zopakovat některé důležité aspekty a přidat nový "tajný" postup.


UPOZORNĚNÍ:



- Vždy po každém otevření nebo zavření kanálu proveďte zálohu jeho stavu (SCB). Zabere to jen několik sekund.
- Neuchovávejte staré soubory SCB, abyste je nezmátli a neobnovili. Jsou naprosto nepoužitelné a mohly by vyvolat sankční řízení, pokud je se. Pokud přistoupíte k obnově, vždy použijte poslední verzi souboru SCB.
- Uložte soubor SCB (jedná se o zašifrovaný text s příponou .bin) mimo zařízení na bezpečné místo. Pro přesun tohoto souboru do počítače nebo jiného zařízení můžete použít funkci [LocalSend](https://github.com/localsend/localsend).
- Uložte si také seed svého zařízení Blixt Wallet na bezpečné místo, například do offline správce hesel / šifrovaného USB.


Tajná metoda: Jak migrovat uzel Blixt bez uzavření stávajících kanálů. K tomu si musíte pozorně přečíst předchozí část "Třetí kontakt" v této příručce o "Obnovení Wallet".


Tento postup NENÍ PRO NOOBS, je určen pouze pro pokročilé uživatele! Proto není široce přístupný a doporučuji jej provádět pouze s pomocí vývojářů Blixt nebo mé podpory. Prosím, neignorujte tuto radu.


### PŘÍPAD 4 - JAKÉ PEERY POUŽÍT K OTEVŘENÍ KANÁLŮ?


Jak jsem napsal na stránce [Blixt guides page](https://blixtwallet.github.io/guides), existuje mnoho způsobů, jak otevřít kanály s tímto mobilním uzlem LND. Některé důležité aspekty bych zde ale rád připomněl:



- otevřené se známými uzly LSP a s rovnocennými uzly, za které ručí komunita. [Viz seznam zde](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- neotevírejte pouze s náhodnými uzly Tor. Ty jsou bezcenné a budete mít jen problémy s nemožností provádět platby. Bez ohledu na to, jak dobrý je váš kamarád "uzlový běžec" se shity Tor uzlem v džungli, nikdy vám nedá nejlepší trasy pro mobilní privátní uzel. Neotevíráte kanály s někým, protože je váš přítel. Tohle není Facebook! Kanál si otevíráte kvůli: dobrým trasám, malým poplatkům, dostupnosti.
- není třeba otevírat tunu malých kanálů, 2-3 nebo maximálně 4, ale s dobrým množstvím Sats. Neotvírejte malé kanály, jsou úplně k ničemu. Menší než 200k pro mobil nemají moc využití.
- mějte na paměti LSP, které nabízejí příchozí kanály a kanály JIT (just in time). Ty jsou velmi užitečné, protože nemusíte používat žádné své UTXO, otevírací kanál můžete zaplatit prostředky, které již máte v jiných peněženkách LN, střádat je a připravit na otevření většího kanálu. Tyto JIT kanály byste měli využívat ve svůj prospěch. [V této příručce jsem vysvětlil](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) více možností peerů pro privátní uzly, jako je Blixt. Také [zde v tomto průvodci zveřejněném na SN](https://stacker.news/items/679242/r/DarthCoin) jsem vysvětlil, jak spravovat likviditu soukromých mobilních uzlů.


---

## Závěr


OK, existuje mnoho dalších úžasných funkcí, které Blixt nabízí, nechám vás je objevovat jednu po druhé a bavte se.


Tato aplikace je opravdu podceňována, hlavně proto, že není podporována žádným financováním VCs, je řízena komunitou, budována s láskou a vášní pro Bitcoin a Lightning Network.


Tento mobilní uzel LN, Blixt je velmi mocným nástrojem v rukou mnoha uživatelů, pokud vědí, jak jej dobře používat. Jen si představte, že chodíte po světě s uzlem LN ve vlastní kapse a nikdo to nepozná.


A to nemluvím o všech dalších bohatých funkcích, které jsou součástí, a které může nabídnout jen velmi málo nebo žádná jiná aplikace Wallet.


Mezitím zde najdete všechny odkazy na tento úžasný bleskový uzel Bitcoin:



- [Oficiální webová stránka společnosti Blixt](https://blixtwallet.com/)
- [stránka Blixt Github](https://github.com/hsjoberg/blixt-Wallet/)
- [Blixt Features page](https://blixtwallet.github.io/features) - vysvětlení jednotlivých funkcí a vlastností.
- [Blixt FAQ page](https://blixtwallet.github.io/faq) - Seznam otázek a odpovědí a řešení problémů s Blixtem
- [Blixt Guides page](https://blixtwallet.github.io/guides) - demoverze, videonávody, další návody a případy použití pro Blixt
- Stáhnout: [Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [APK přímo ke stažení](https://github.com/hsjoberg/blixt-Wallet/releases)
- [Telegramová skupina pro přímou podporu](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [crowdfundingová stránka Gejzír](https://geyser.fund/project/blixt) - přispějte na projekt Sats podle svých možností
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - anonymní chat s LN
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - promo video (můžete si vyzkoušet 1. použití LN)
- [Leták formátu A4 k vytištění s prvními kroky při používání nástroje Blixt v různých jazycích](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt také nabízí plně funkční demo](https://blixt-Wallet-git-master-hsjoberg.vercel.app/) přímo na svých webových stránkách nebo na vyhrazené webové verzi, abyste si mohli vyzkoušet všechny zkušenosti, než začnete používat v reálném světě.


---
**DISCLAIMER:**


*Vývojáři této aplikace mě nijak neplatí ani nepodporují. Tuto příručku jsem napsal, protože jsem viděl, že zájem o tuto aplikaci Wallet roste a noví uživatelé stále nechápou, jak s ní začít pracovat. Také proto, abych pomohl Hampusovi (hlavnímu vývojáři) s dokumentací o používání tohoto uzlu Wallet.*


*Nemám žádný jiný zájem na propagaci této aplikace LN, než prosazovat přijetí Bitcoin a LN. To je jediná cesta!*


---