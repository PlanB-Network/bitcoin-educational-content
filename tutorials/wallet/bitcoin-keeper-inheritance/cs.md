---
name: Bitcoin Keeper - Plán dědictví
description: Naplánujte si přenos bitcoinů pomocí Bitcoin Keeper
---

![cover](assets/cover.webp)



Převod aktiv Bitcoin je jedním z problémů, které držitelé nejvíce podceňují. Na rozdíl od bankovního účtu, kde může finanční instituce předat prostředky právoplatným dědicům, je Bitcoin zcela závislý na vlastnictví soukromých klíčů. Zcela legitimní zákonný dědic se bez těchto klíčů k prostředkům nikdy nedostane, zatímco zlomyslný jedinec, který má tajemství v držení, je bude moci utratit bez jakýchkoli formalit.



V tomto druhém výukovém kurzu Bitcoin Keeper se seznámíme s prémiovými funkcemi věnovanými plánování pozůstalosti. Aplikace nabízí pokročilé nástroje pro vytváření vylepšených trezorů s časovými ochrannými mechanismy díky Miniscriptu a také doprovodné dokumenty, kterými se mohou vaši blízcí řídit.



Tato příručka předpokládá, že jste již zvládli základy systému Bitcoin Keeper (vytváření portfolia, klasický multisig, přidávání hardwarových kláves), jak je vysvětleno v našem prvním výukovém kurzu :



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

![video](https://youtu.be/tCld_-n2d30)



## Plány předplatného Bitcoin Keeper



Bitcoin Keeper funguje na modelu freemium se třemi úrovněmi předplatného, které nabízejí postupně se rozšiřující funkce. Chcete-li získat přístup k plánům, přejděte na kartu **Další** a klepnutím na aktuální plán (výchozí je "Pleb") otevřete obrazovku **Správa předplatného**.



![Plans d'abonnement](assets/fr/01.webp)



Plán **Pleb** (zdarma) poskytuje přístup k základním funkcím: neomezené vytváření peněženek s jedním nebo více klíči, kompatibilitu se všemi hlavními hardwarovými peněženkami (Coldcard, Trezor, Ledger, Jade, Tapsigner...), kontrolu mincí, označování a připojení k osobnímu serveru Electrum. Tento plán je dostatečný pro standardní použití a dokonce i pro klasické konfigurace multi-sig.



Plán **Hodler** (9,99 €/měsíc, při ročním placení 1 měsíc zdarma) zahrnuje všechny funkce služby Pleb a přidává šifrované zálohy do cloudu (iCloud nebo Google Drive) pro obnovení vašich trezorů na libovolném zařízení, serverový klíč pro přidání automatických zásad utrácení a 2FA nad určitou hranici a peněženky Canary pro zjištění neoprávněného přístupu k vašim klíčům.



Plán **Diamond Hands** (29,99 €/měsíc, při roční platbě 1 měsíc zdarma) je kompletní balíček pro plánování majetku. Zahrnuje celý plán Hodler a odemyká Dědický klíč (odložená aktivace), Nouzový klíč (nouzový klíč pro obnovu v případě ztráty), nástroje a dokumenty pro plánování dědictví a hovor s podporou týmu Concierge pro ověření vaší konfigurace. Jedná se o nabídku pro bitcoinaře, kteří chtějí předat své dědictví několika generacím.



Důležitý bod: vytvořené trezory zůstanou přístupné, i když se vrátíte k bezplatnému tarifu. Vaše konfigurace jsou založeny na otevřených standardech (BSMS, Miniscript) a fungují nezávisle na vašem předplatném.



## Dědické dokumenty



Po aktivaci předplatného Diamantové ruce přejděte na kartě Více do sekce **Dědické dokumenty**. Bitcoin Keeper obsahuje pět vzorových dokumentů pro strukturování vašeho plánu dědictví a také sekci s tipy:



![Documents d'héritage](assets/fr/02.webp)





- Šablona slov pro zotavení**: šablona pro přehledné a uspořádané zapisování frází pro zotavení
- Důvěryhodné kontakty**: šablona pro uvedení kontaktních údajů důvěryhodných osob zapojených do vašeho plánu (notář, právník, dědicové, klíčníci)
- Doplňkový sdílený klíč**: dokument s podrobnými technickými informacemi ke každému klíči: Kód PIN, cesta odvození, fyzické umístění, typ zařízení a další informace užitečné pro identifikaci a použití klíče
- Pokyny k vymáhání**: pokyny krok za krokem pro dědice nebo příjemce k vymáhání finančních prostředků
- Dopis advokátovi**: předvyplněný dopis, který lze upravit pro vašeho advokáta nebo notáře



Sekce **Tipy pro dědictví** nabízí praktické rady, jak zajistit klíče pro dědice a optimalizovat plán dědictví.



Upravte tyto dokumenty podle své situace a uložte je na bezpečném místě, odděleně od samotných klíčů.



## Konfigurace zálohování do cloudu



Před vytvořením staršího trezoru aktivujte cloudové zálohování, abyste ochránili své konfigurační soubory. Na kartě Více stiskněte tlačítko **Osobní cloudové zálohování**.



![Configuration Cloud Backup](assets/fr/03.webp)



Pro šifrování záloh zvolte silné heslo. Toto heslo chrání pouze konfigurační soubory wallet (nikoli vaše soukromé klíče). Potvrďte heslo a stiskněte tlačítko **Potvrdit**. Vaše zálohy budou uloženy na iCloudu nebo Disku Google v závislosti na vašem zařízení. Stisknutím tlačítka **Backup Now** spustíte první zálohu.



## Import hardwarových klíčů



V našem příkladu vytvoříme trezor 2 ze 3 se dvěma dalšími klíči (Dědičnost a Nouzový stav). Začněme importem všech potřebných klíčů na kartu **Klíče**.



![Import des clés hardware](assets/fr/04.webp)



Stiskněte tlačítko **Přidat klíč** a poté vyberte možnost **Přidat klíč z hardwaru** pro připojení hardwaru wallet. Zařízení Bitcoin Keeper podporuje mnoho zařízení: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner a Specter Solutions.



V naší konfiguraci importujeme :




- 2 klíče **Coldcard** (MK4SP a MK4)
- 2 klíče **Tapsigner** (Metro a Genesis)



Chcete-li přidat kartu Coldcard, vyberte ji ze seznamu a podle pokynů na obrazovce exportujte veřejný klíč prostřednictvím kódu QR, souboru, USB nebo NFC. Další podrobnosti o používání karty Coldcard nebo Tapsigner naleznete v našich specializovaných návodech:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-mk4-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


Po importu všech klíčů je najdete na kartě Klíče s vlastními názvy.



## Vytvoření staršího modelu wallet



Přejděme k vytvoření kmene. Na kartě **Peníze** stiskněte tlačítko **Přidat Wallet**, vyberte možnost **Bitcoin Wallet** a poté **Vytvořit Wallet**.



![Création du wallet](assets/fr/05.webp)



Vyberte typ wallet. Pro náš starší plán vyberte možnost **2 ze 3 víceklíčových**. V dolní části obrazovky aktivujte možnost **Vylepšené možnosti zabezpečení** a stiskněte tlačítko **Pokračovat**.



![Options de sécurité avancées](assets/fr/06.webp)



Ve vyskakovacím okně Rozšířené možnosti zabezpečení zaškrtněte políčko :




- Dědičný klíč**: další klíč, který bude po uplynutí stanovené doby přidán do kvora
- Nouzový klíč**: klíč s odloženou úplnou kontrolou pro obnovení prostředků v případě ztráty klíče



Stiskněte tlačítko **Uložit změny**. Poté z importovaných klíčů vyberte 3 klíče, které budou tvořit váš wallet (např. Seed Key, Coldcard MK4SP a Tapsigner Metro).



## Stanovení zvláštních klíčových termínů



Na další obrazovce můžete nakonfigurovat nouzový klíč a dědičný klíč. Zde definujete prodlevy, kterými se řídí aktivace těchto speciálních klíčů.



![Configuration des délais](assets/fr/07.webp)



U položky **Emergency Key** vyberte hardwarový klíč, který bude sloužit jako konečná záloha (zde Coldcard MK4), a zvolte prodlevu aktivace (v našem příkladu: 2 roky). Na rozdíl od dědického klíče se nouzový klíč nepřidává ke kvoru: umožňuje **úplně obejít multisig** a dává vám úplnou kontrolu nad prostředky po uplynutí časového limitu. Je to vaše řešení poslední instance: pokud dojde ke ztrátě nebo zničení několika klíčů, tento jediný klíč vám umožní vše obnovit. Je proto třeba jej chránit s maximální přísností.



Pro **Dědičný klíč** vyberte klíč určený pro dědice (zde Coldcard MK4SP) a zvolte prodlevu (v našem příkladu: 1 rok). Po uplynutí jednoho roku bez pohybu bude tento klíč **přidán k podpisovému kvoru**. V praxi to znamená, že po uplynutí této doby se z vašeho klíče wallet 2-of-3 stane klíč wallet 2-of-4, což dědici umožní účastnit se podpisového kvora vedle stávajících klíčů.



### Jak fungují časové zámky?



Bitcoin Keeper používá **absolutní časové zámky** (CLTV - CheckLockTimeVerify), které umožňuje Miniscript. Na rozdíl od relativních časových zámků (CSV), které se spouštějí při přijetí každého UTXO, pracují absolutní časové zámky s **pevným datem vypršení** definovaným při vytvoření wallet.



Konkrétně, pokud dnes vytvoříte wallet s dědičným klíčem na 1 rok, bude datum aktivace "dnes + 1 rok". Všechny prostředky uložené na tomto účtu wallet, bez ohledu na datum jejich uložení, budou prostřednictvím klíče Inheritance Key přístupné k témuž datu.



Výhodou absolutních časových plánů je, že umožňují časy realizace delší než 15 měsíců (limit relativních časových plánů CSV), což vysvětluje, proč společnost Bitcoin Keeper může nabízet možnosti jako 2 roky.



### Mechanismus obnovení



Abyste zabránili aktivaci speciálních klíčů během svého života, musíte pravidelně "obnovovat" svůj klíč wallet. U absolutních časových zámků to znamená **znovuvytvoření wallet s novým datem vypršení platnosti** posunutým do budoucnosti a následný převod vašich prostředků na tento nový wallet.



Bitcoin Keeper tento proces zjednodušuje díky integrované funkci obnovení. Aplikace se o tuto složitost postará automaticky na pozadí: stačí postupovat podle návodu, aniž byste museli ručně vytvářet nový účet wallet nebo sami převádět finanční prostředky. Tuto operaci plánujte pravidelně, s dostatečným předstihem před uplynutím nejkratšího nastaveného časového rámce. Například při jednoletém dědickém klíči obnovujte každých 9-10 měsíců, abyste zachovali bezpečnostní rezervu.



## Uložení a export konfigurace



Po vytvoření souboru wallet vám aplikace připomene, abyste konfigurační soubor uložili. **Tento krok je velmi důležitý**: bez tohoto souboru nebudou vaši dědicové schopni obnovit multisignátor wallet.



![Export de la configuration](assets/fr/08.webp)



Stiskněte tlačítko **Zálohovat soubor pro obnovení Wallet**. K dispozici je několik možností exportu:




- Export do PDF**: generuje kompletní dokument se všemi informacemi wallet
- Zobrazit QR**: zobrazí QR kód pro import konfigurace do jiného zařízení
- Airdrop / Export souboru**: exportuje soubor prostřednictvím možností sdílení
- NFC**: sdílení prostřednictvím NFC s kompatibilním zařízením



Rozmnožte kopie: jednu u notáře, jednu v bankovním sejfu a jednu šifrovanou digitální verzi. Váš nový wallet se nyní objeví na kartě Peněženky s označením "Multiklíč", "2 ze 3", "Dědičný klíč" a "Nouzový klíč".



## Vytvoření kanárka Wallet



Kanár Wallet je systém včasného varování. Myšlenka: každý klíč použitý v multiklíči wallet lze použít i v samostatném klíči wallet. Uložením malé částky na tohoto "kanárka" wallet signalizuje jakýkoli neoprávněný pohyb ohrožení klíče.



![Canary Wallets](assets/fr/09.webp)



Existují dva způsoby konfigurace modulu Wallet Canary. Na kartě **Další** stiskněte v části "Klíče a peněženky" tlačítko **Peněženky kanárků**. Na obrazovce je vysvětlen princip: pokud někdo získá přístup k jednomu z vašich klíčů a najde prostředky v přidruženém jednoduchém klíči wallet, pokusí se je odstranit, na což vás upozorní.



![Configuration Canary depuis une clé](assets/fr/10.webp)



Kanárka můžete také konfigurovat přímo z klíče. Na kartě **Keys** vyberte klávesu (např. Tapsigner Genesis), stiskněte ikonu **Settings** (ozubené kolečko) a poté **Canary Wallet**. Otevře se přidružený kanárek wallet, který je připraven přijmout několik sledovacích satošů.



Na každém kanárském ostrově Wallet uložte malou částku (několik tisíc satošů). Pokud se tyto prostředky přesunou bez vašeho souhlasu, okamžitě odstraňte kompromitující klíč ze svých multisigových trezorů.



## Osvědčené postupy



**Před vložením velké částky otestujte konfiguraci** s malou částkou peněz. Pošlete do trezoru několik tisíc satošů a pak zkuste odchozí útratu, abyste si ověřili, že jste zvládli proces podepisování s každým zařízením. Vyzkoušejte také import konfiguračního souboru do jiného telefonu, abyste se ujistili, že záloha funguje.



**Distribuujte klíče inteligentně**. V případě odposlechů je předávejte v zapečetěné obálce s PIN kódem sděleným odděleně (např. v dopise s pokyny k obnově uloženém jinde). U klasických hardwarových peněženek si zařízení ponechte u důvěryhodné třetí strany a seed na papíře nebo kovu u sebe nebo jiné třetí strany. Poznamenejte si otisk každého klíče a jeho název v konfiguračním souboru, aby nedošlo k záměně.



**Plánujte pravidelné testy** (požární cvičení). Každoročně zkontrolujte, zda můžete trezor obnovit ze záloh na prázdném telefonu. Testujte výstrahy kanárků kontrolou zůstatků. Simulujte scénáře ztráty ("co když ztratím kartu Coldcard?"), abyste si ověřili, že zbývající kombinace klíčů jsou dostatečné.



**Nezapomeňte na obnovení**. Pokud jste si nastavili dědický klíč na 1 rok, obnovujte se každých 9-10 měsíců. To je cena, kterou platíte za automatický přenos bez zásahu třetí strany.



**Udržujte plán aktuální**. Jakákoli změna (výměna klíče, změna dědiců, změna termínu) se musí promítnout do všech záloh a dokumentů. Po každé změně přegenerujte soubory PDF a nové verze znovu rozešlete.



## Limity a úvahy



Navzdory síle těchto nástrojů je důležité si uvědomit jejich omezení, abyste je mohli spravovat co nejefektivněji.



**Složitost** multisigového trezoru s časovými zámky může být sama o sobě rizikem: chybná konfigurace, nepochopení ze strany dědiců, ztráta kritického prvku mezi mnoha komponentami. Bitcoin Keeper tuto zkušenost maximálně zjednodušuje, ale stále se jedná o technickou operaci. Tento plán nasazujte pouze tehdy, pokud to množství, které má být chráněno, ospravedlňuje. U malých částek může stačit jednodušší plán.



Za zamyšlení stojí **závislost na aplikaci**. Přestože je kód open source a je založen na otevřených standardech (Miniscript, BSMS), některé funkce jsou závislé na ekosystému Keeper. Uschovejte si kopii aplikace (APK pro Android nebo IPA pro iOS) a v dopisech dědicům zdokumentujte možnost použití jiných peněženek kompatibilních s Miniscriptem (např. Liana) k obnově prostředků.



Důvěryhodní zprostředkovatelé** představují lidské riziko. Co se stane, když zlý úmyslný příbuzný použije svěřený klíč před uplynutím lhůty? Nebo když právník špatně uloží vaše dokumenty? Pečlivě si tyto osoby vybírejte, jasně jim vysvětlete jejich povinnosti a mějte plán B. Nejlepší ochranou proti těmto nebezpečím zůstávají peněženky Canary, redundantní zálohy a samotná struktura multisig.



## Závěr



Společnost Bitcoin Keeper se svým plánem Diamantové ruce nabízí kompletní sadu nástrojů pro plánování majetku: Vylepšené trezory s časovými klíči, doprovodné dokumenty, peněženky Canary a individuální podporu.



Nejde jen o technickou záležitost: je to otázka návrhu architektury vašeho majetku, inteligentní distribuce klíčů a znalostí a pravidelného testování systému. Dobře navržený plán dědictví Bitcoin promění vaše satoše ve skutečné, přenosné dědictví.