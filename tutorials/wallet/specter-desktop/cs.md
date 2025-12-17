---
name: Specter Desktop
description: Spravujte svá portfolia Bitcoin s více podpisy zcela suverénně pomocí vlastního uzlu
---

![cover](assets/cover.webp)



Specter Desktop je open source aplikace (licence MIT) vyvíjená společností Cryptoadvance od roku 2019, která usnadňuje správu peněženek Bitcoin s vašimi hardwarovými peněženkami (Ledger, Trezor, Coldcard, BitBox02, Passport atd.) a vaší vlastní infrastrukturou Bitcoin (Bitcoin Core node nebo Electrum server). Aplikace vyniká zejména v konfiguracích s více podpisy, které umožňují zabezpečit velké částky rozdělením podpisového výkonu mezi několik nezávislých hardwarových peněženek.



**V tomto kurzu se dozvíte, jak:**




- Instalace a konfigurace aplikace Specter Desktop v počítači (Windows, macOS nebo Linux)
- Připojte program Specter k serveru Electrum (v tomto příkladu použijeme Umbrel)
- Vytvoření jednoduchého wallet s hardwarem wallet (Coldcard)
- Přijímání a odesílání bitcoinů s naprostou suverenitou
- Nastavení vícepodpisového systému wallet 2 na 3 s několika hardwarovými peněženkami
- Instalace programu Spectre na server Umbrel (bonus pro pokročilé)



Všechny vaše transakce budou ověřovány lokálně prostřednictvím vaší vlastní infrastruktury, bez přenosu informací na externí servery, což zaručuje důvěrnost a finanční suverenitu. Před podpisem vždy zkontrolujte transakce na obrazovce hardwaru wallet.



## Stažení a instalace



Navštivte oficiální webové stránky aplikace Specter Desktop a stáhněte si ji.



![Page d'accueil Specter](assets/fr/01.webp)



Na stránce pro stažení vyberte verzi odpovídající vašemu operačnímu systému: MacOS, Windows nebo Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Po stažení nainstalujte aplikaci podle obvyklých pokynů operačního systému. V případě systému macOS přetáhněte ikonu do složky Aplikace. V případě systému Windows spusťte instalační program. V případě Linuxu postupujte podle pokynů v balíčku.



## Počáteční konfigurace



Při prvním spuštění vás aplikace Specter Desktop vyzve k výběru typu připojení. Můžete se připojit k serveru Electrum nebo k vlastnímu uzlu Bitcoin Core.



![Choix du type de connexion](assets/fr/03.webp)



V tomto příkladu použijeme připojení k serveru Electrum spuštěnému v systému Umbrel.



Další informace naleznete v našem výukovém programu Umbrel:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Tato možnost nabízí rychlejší synchronizaci než jádro Bitcoin. Pokud dáváte přednost, můžete zvolit "Bitcoin Core" a nakonfigurovat připojení k místnímu uzlu. Následující kroky zůstávají stejné bez ohledu na vaši volbu.



Chcete-li nakonfigurovat vlastní server Electrum, vyberte možnost "Electrum Connection" a poté "Enter my own".



![Configuration Electrum](assets/fr/04.webp)



Zadejte adresu serveru Electrum. V našem případě s Umbrel bude adresa `umbrel.local` s portem `50001`. Klepnutím na tlačítko "Connect" (Připojit) navažte spojení.



Po připojení se zobrazí uvítací obrazovka s kontrolním seznamem, který vám pomůže začít. Nyní je třeba přidat hardwarové peněženky.



![Écran d'accueil](assets/fr/05.webp)



## Přidání hardwaru wallet



V levé nabídce klikněte na "Add device" a přidejte hardware wallet.



Spectre Desktop podporuje řadu hardwarových peněženek: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault a mnoho dalších.



Pokud se chcete dozvědět více, podívejte se na naše výukové materiály o hardwaru wallet.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Vyberte hardware wallet. V tomto příkladu používáme kartu Coldcard MK4.



Níže najdete náš návod pro tento hardware wallet:



https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

V případě karty Coldcard je třeba exportovat veřejné klíče z hardwaru wallet prostřednictvím připojení USB nebo karty microSD.



![Import des clés du Coldcard](assets/fr/07.webp)



Při exportu klíčů z karty Coldcard postupujte podle zobrazených pokynů. Pojmenujte svůj hardware wallet (zde "MK4 Tuto"). Po importu klíčů můžete vytvořit wallet s jediným klíčem nebo přidat další hardwarové peněženky pro wallet s více podpisy.



![Dispositif ajouté](assets/fr/08.webp)



## Vytvoření portfolia



Po přidání hardwaru wallet klikněte na "Create single key wallet" a vytvořte wallet s jedním podpisem.



Pojmenujte své portfolio (např. "Wallet pro tuto") a vyberte typ adresy. Chcete-li používat nativní adresy bech32, které optimalizují transakční náklady, vyberte možnost "Segwit".



![Configuration du portefeuille](assets/fr/09.webp)



Po vytvoření portfolia vám společnost Specter nabídne uložení záložního souboru PDF obsahujícího všechny veřejné informace potřebné k obnovení portfolia (deskriptory, rozšířené veřejné klíče). Tento soubor neobsahuje vaše soukromé klíče.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Přijímání bitcoinů



Chcete-li přijímat bitcoiny, vyberte v levém menu svůj účet wallet a klikněte na kartu "Přijmout".



Spectre automaticky vygeneruje novou adresu příjmu s QR kódem.



![Génération d'une adresse de réception](assets/fr/11.webp)



Adresu můžete zkopírovat nebo naskenovat QR kód. Než někomu předáte adresu, vždy ji zkontrolujte na obrazovce hardwaru wallet.



## Zobrazení historie a adres



Jakmile obdržíte bitcoiny, můžete si své transakce prohlédnout na kartě "Transakce".



![Historique des transactions](assets/fr/12.webp)



Na kartě "Adresy" si můžete prohlédnout všechny adresy vygenerované vaším portfoliem, jejich stav využití a související částky.



![Liste des adresses](assets/fr/13.webp)



## Odeslat bitcoiny



Chcete-li poslat bitcoiny, klikněte na kartu "Odeslat". Zadejte adresu příjemce, částku, která má být odeslána, a zaškrtněte rozšířené možnosti, pokud chcete ručně vybrat UTXO (kontrolu mincí).



![Création d'une transaction](assets/fr/14.webp)



Kliknutím na tlačítko "Vytvořit nepodepsanou transakci" vytvoříte transakci. Spectre vás poté požádá o podepsání transakce pomocí hardwaru wallet.



![Signature de la transaction](assets/fr/15.webp)



Pokud používáte kartu Coldcard, máte na výběr mezi podpisem přes USB a kartou microSD (s air-gapped). Potvrďte transakci na obrazovce hardwaru wallet a pečlivě zkontrolujte cílovou adresu a částku.



Jakmile je transakce podepsána, můžete ji vysílat v síti Bitcoin.



![Options de diffusion](assets/fr/16.webp)



Kliknutím na "Odeslat transakci" transakci odešlete. Spectre potvrdí, že transakce byla odeslána, a její stav můžete sledovat na kartě Transakce.



![Diffusion de la transaction](assets/fr/17.webp)



## Vytvoření a používání portfolia s více podpisy



Jednou z hlavních předností aplikace Specter Desktop je její schopnost zjednodušit správu portfolií s více podpisy. Vícepodpisový systém wallet vyžaduje k autorizaci transakce několik podpisů, čímž se eliminuje jediný bod selhání. Například konfigurace 2 na 3 vyžaduje k potvrzení jakéhokoli výdaje dva podpisy ze tří samostatných hardwarových peněženek.



Chcete-li vytvořit multisig wallet, začněte přidáním všech podepisovacích hardwarových peněženek prostřednictvím "Přidat zařízení". V tomto příkladu budeme používat tři různé hardwarové peněženky: Coldcard MK4 (již přidaná dříve), Passport a Ledger. Tato diverzifikace výrobců posiluje bezpečnost tím, že zabraňuje závislosti na jediném dodavatelském řetězci nebo firmwaru.



Zde jsou odkazy na výukové programy Ledger a Passport:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Přidání zařízení Passport pojmenováním hardwaru wallet (např. "Passport multi") a importem jeho klíčů prostřednictvím karty microSD nebo kódu QR. Poté pokračujte kliknutím na tlačítko "Continue" (Pokračovat).



![Ajout du Passport](assets/fr/23.webp)



Poté přidejte Ledger připojením přes USB a otevřením aplikace Bitcoin na hardwaru wallet. Pojmenujte jej (např. "ledger multi") a kliknutím na "Get via USB" a poté na "Continue" importujte jeho veřejné klíče.



![Ajout du Ledger](assets/fr/24.webp)



Po registraci tří hardwarových peněženek ve Spectru klikněte na "Add wallet" a výběrem možnosti "Multiple Signature" vytvořte wallet s více podpisy.



![Choix du type de wallet](assets/fr/25.webp)



Vyberte tři hardwarové peněženky, které chcete zahrnout do svého multipodpisového kvora: Vyberte MK4 Tuto, Passport multi a ledger multi. Kliknutím na tlačítko "Pokračovat" přejděte k dalšímu kroku.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Zvolte konfiguraci více podpisů. Vyberte "Segwit" jako typ adresy, abyste mohli využívat optimalizované poplatky. Parametr "Požadované podpisy pro autorizaci transakcí (m ze 3)" umožňuje definovat prahovou hodnotu: pro konfiguraci 2 na 3 jsou vyžadovány 2 podpisy. Každý hardware wallet zobrazí svůj odpovídající multisig klíč. Kliknutím na "Create wallet" (Vytvořit wallet) dokončíte vytváření.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Vaše portfolio s více podpisy "Multi tuto" je nyní vytvořeno. Společnost Specter okamžitě doporučuje uložit záložní soubor PDF obsahující popis portfolia. Kliknutím na "Save Backup PDF" (Uložit záložní soubor PDF) si tento kritický soubor stáhněte.



![Wallet multisig créé](assets/fr/28.webp)



Spectre také umožňuje exportovat informace wallet do každé z vašich hardwarových peněženek prostřednictvím QR kódu nebo souboru. To umožňuje některým hardwarovým peněženkám (například Coldcard nebo Passport) ukládat konfiguraci multisig přímo do jejich paměti.



V případě aplikace Passport odemkněte zařízení a poté přejděte na "Správa účtu" > "Připojit Wallet" > "Specter" > "Multisig" > "QR kód" a naskenujte QR kód vygenerovaný aplikací Specter. Passport vás poté požádá o naskenování přijímací adresy z vašeho wallet, abyste potvrdili konfiguraci multisig.



Pokud jde o MK4, připojte jej k počítači a odemkněte jej. Poté klikněte na "Save MK4 Tuto file" a uložte soubor do MK4. Až budete příště podepisovat hardware wallet, MK4 použije tento soubor k dokončení konfigurace multisig.



![Export vers les hardware wallets](assets/fr/29.webp)



Pro vaši informaci můžete kdykoli přistupovat k zálohám na kartě "Nastavení" svého portfolia a poté "Exportovat":



![Accès au backup PDF](assets/fr/30.webp)



Každodenní používání zůstává podobné jako u jednoduchého wallet: normálně přijímáte adresy generate. Chcete-li poslat bitcoiny, přejděte na kartu "Odeslat", zadejte adresu příjemce a částku a klikněte na "Vytvořit nepodepsanou transakci".



![Création d'une transaction multisig](assets/fr/31.webp)



Spectre sestaví PSBT (Partially Signed Bitcoin Transaction) a zobrazí "Acquired 0 of 2 signatures". Nyní musíte podepsat alespoň dvě ze tří hardwarových peněženek. Klikněte na první hardwarovou peněženku wallet (např. "MK4 Tuto"), abyste získali podpis pomocí karty Coldcard, a poté na druhou (např. "Passport multi"), abyste získali druhý požadovaný podpis.



![Signature de la transaction](assets/fr/32.webp)



Jakmile získáte 2 požadované podpisy (v rozhraní se zobrazí "Acquired 2 of 2 signatures" a "Transaction is ready to send"), klikněte na "Send Transaction" (Odeslat transakci), čímž transakci odvysíláte v síti Bitcoin.



![Transaction prête à être diffusée](assets/fr/33.webp)



Tento přístup s více podpisy je vhodný zejména pro firmy (výdaje musí schvalovat několik manažerů), rodiny (ochrana vícegeneračního dědictví) nebo jednotlivce spravující velké částky (geografické rozložení hardwarových peněženek, aby odolaly lokálním katastrofám).



### Zásadní význam zálohování více podpisů



**Upozornění**: zálohování portfolia složeného z více značek se zásadně liší od zálohování jednotlivého portfolia. K obnově multisigového portfolia nestačí pouze vaše fráze pro obnovu (fráze seed). Musíte také zálohovat **output descriptor** (output descriptor), který obsahuje konfigurační informace pro vaše multisig portfolio.



output descriptor obsahuje základní údaje: rozšířené veřejné klíče (xpubs) každého spolupodepisovatele, podpisový práh (v našem příkladu 2 na 3), typ použitého skriptu (nativní, vnořený nebo starší Segwit) a cesty obcházení pro každý hardware wallet. Bez tohoto deskriptoru, i když máte dvě ze tří frází pro obnovení, nebudete moci obnovit svůj wallet ani získat přístup ke svým bitcoinům. Deskriptor umožňuje vašemu softwaru zjistit, jak kombinovat veřejné klíče k generate adresám Bitcoin odpovídajícím vašim prostředkům.



Aplikace Specter Desktop automaticky generuje záložní soubor PDF při vytváření portfolia více značek. Tento soubor PDF obsahuje kompletní deskriptor, otisky prstů každého hardwaru wallet a všechny veřejné informace potřebné pro obnovu. **Tento soubor neobsahuje vaše soukromé klíče**, a proto sám o sobě neumožňuje utrácet vaše bitcoiny, ale umožňuje každému, kdo k němu získá přístup, vidět vaši kompletní transakční historii a zůstatek.



Chcete-li správně zálohovat konfiguraci více podpisů, postupujte takto: Po vytvoření portfolia klikněte na kartu "Nastavení", poté na "Exportovat" a vyberte "Uložit zálohu PDF". Vytvořte několik kopií tohoto PDF: vytiskněte alespoň dvě kopie na papír a ponechte si také šifrovanou digitální kopii. Jednu kopii PDF uložte s každou z vašich frází pro obnovu na geograficky oddělených místech.



Vyryjte své fráze o obnově na ohnivzdorné a vodotěsné kovové desky, abyste zaručili jejich dlouhou životnost. Nikdy nepodceňujte důležitost těchto záloh: pokud ztratíte složku `~/.specter` v počítači A ztratíte jednu z hardwarových peněženek bez zálohy deskriptorů, budou všechny vaše prostředky nenávratně ztraceny, a to i při konfiguraci 2 na 3. Redundance více podpisů chrání před ztrátou hardwaru wallet, ale pouze v případě, že jste správně zálohovali deskriptor wallet.



## Výhody a omezení aplikace Specter Desktop



**Výhody**: Optimální důvěrnost s kompletním místním ověřením bez serverů třetích stran. Flexibilita více podpisů pro pokročilé konfigurace (firemní, rodinné, individuální). Rozsáhlá podpora hardwaru wallet s plnou interoperabilitou (USB a vzduchem).



**Omezení**: Značná křivka učení pokročilých konceptů Bitcoin (UTXO, deskriptory, cesty derivace).



## Osvědčené postupy



Před ověřením vždy zkontrolujte adresy a částky na obrazovce hardwaru wallet, abyste se ochránili před malwarem.



Zálohy PDF uchovávejte odděleně od semen. Tyto veřejné deskriptory mohou být uloženy v bankovním trezoru nebo šifrovaném cloudu, což usnadní obnovu, aniž byste odhalili své soukromé klíče.



Před použitím portfolia s velkými finančními prostředky otestujte obnovu na částkách token. Vytvářejte, testujte, odstraňujte a obnovujte, abyste ověřili své postupy.



Udržujte program Specter a firmware v aktuálním stavu. Rozdělte své spolupodepisující osoby podle zeměpisné polohy (doma/kancelář/blízko), abyste odolali lokálním katastrofám. Používejte popisné štítky pro usnadnění účetnictví a daňových přiznání.



## Bonus: Instalace na server Bitcoin (Umbrel, RaspiBlitz, Start9)



Pokud již vlastníte server Bitcoin, například Umbrel, RaspiBlitz, MyNode nebo Start9, můžete si nainstalovat Spectre Desktop přímo z jejich obchodu s aplikacemi. Tento přístup nabízí několik významných výhod: aplikace se automaticky nakonfiguruje s vaším místním uzlem Bitcoin Core, zůstává nepřetržitě přístupná prostřednictvím webového rozhraní z libovolného zařízení ve vaší síti a můžete k ní dokonce bezpečně přistupovat na dálku prostřednictvím sítě Tor. Celá vaše infrastruktura Bitcoin je centralizována na jediném vyhrazeném serveru, což zjednodušuje správu a posiluje vaši suverenitu.



### Instalace z obchodu s aplikacemi Umbrel



V rozhraní Umbrel přejděte do obchodu App Store a vyhledejte aplikaci Specter Desktop. Klepnutím na "Install" (Instalovat) spusťte instalaci.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Po dokončení instalace spusťte aplikaci Spectre Desktop v počítači Umbrel. Na uvítací obrazovce budete vyzváni k výběru typu připojení. Pokud používáte program Specter na zařízení Umbrel, klikněte na "Aktualizovat nastavení" a nakonfigurujte připojení.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Výběrem možnosti "Vzdálené připojení USB Spectre" povolíte používání hardwarových peněženek USB připojených k místnímu počítači při používání programu Spectre na vzdáleném serveru Umbrel.



![Configuration Remote Specter USB](assets/fr/20.webp)



Podle zobrazených pokynů nakonfigurujte můstek HWI. Je třeba vstoupit do nastavení zařízení bridge a přidat doménu `http://umbrel.local:25441` na whitelist. Klepnutím na tlačítko "Update" (Aktualizovat) uložte konfiguraci.



![HWI Bridge Settings](assets/fr/21.webp)



Pokud chcete hardwarové peněženky USB používat i z místního počítače, stáhněte si do počítače aplikaci Specter Desktop a nastavte ji na "Ano, Spouštím Spectre vzdáleně". Kliknutím na "Uložit" dokončete konfiguraci.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Závěr



Aplikace Specter Desktop demokratizuje pokročilé konfigurace Bitcoin a zpřístupňuje více podpisů, aniž by byla obětována vaše suverenita nebo důvěrnost. Pro uživatele spravující značné finanční částky transformuje institucionální postupy do řešení, které mohou nasadit i soukromé osoby.



Přestože aplikace vyžaduje počáteční investice do infrastruktury a učení, nabízí naprostou suverenitu: kontrolu nad validační infrastrukturou, fyzické vlastnictví klíčů a transakce bez dohledu třetích stran. Ať už jste jednotlivec zajišťující své úspory, rodina vytvářející vícegenerační bezpečnostní schránku, nebo společnost spravující peněžní toky, Spectre Desktop je referenční nástroj pro sladění maximálního zabezpečení a absolutní suverenity.



## Zdroje



### Oficiální dokumentace




- [Oficiální webové stránky Spectre Desktop](https://specter.solutions/desktop/)
- [zdrojový kód GitHub](https://github.com/cryptoadvance/specter-desktop)
- [Kompletní dokumentace](https://docs.specter.solutions/)



### Společenství a podpora




- [Telegram Specter Community Group](https://t.me/spectersupport)
- [Diskusní fórum Reddit](https://reddit.com/r/specterdesktop/)
- [Hlášení chyb na GitHubu](https://github.com/cryptoadvance/specter-desktop/issues)