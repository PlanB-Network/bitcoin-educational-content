---
name: Bitcoin Keeper
description: Bitcoin mobilní wallet pro zabezpečení a multi-sig
---

![cover](assets/cover.webp)



Bezpečná správa bitcoinů představuje velkou výzvu pro každého držitele, který si je vědom toho, že jde o finanční suverenitu. Mezi jednoduchostí mobilního řešení wallet a robustností řešení multi-sig se může zdát, že technický rozdíl je pro mnoho uživatelů skličující. Bitcoin Keeper se nachází přesně na tomto průsečíku a nabízí progresivní přístup k zabezpečení, který uživatele doprovází v průběhu jejich vývoje.



Bitcoin Keeper je open source mobilní aplikace určená výhradně pro Bitcoin, kterou vyvinul tým BitHyve. Její ambicí je zpřístupnit pokročilou správu portfolia, zejména konfigurace s více podpisy, při zachování intuitivního rozhraní pro začátečníky. Aplikace přijala slogan "Secure today, Plan for tomorrow" (Zabezpečte se dnes, plánujte na zítřek), který odráží její filozofii dlouhodobé podpory.



Na rozdíl od univerzálních peněženek, které spravují více kryptoměn, se Bitcoin Keeper striktně zaměřuje na Bitcoin. Tento přístup zaměřený pouze na bitcoiny snižuje potenciální plochu pro útoky a výrazně zjednodušuje uživatelské prostředí. Aplikace také vyniká nativní integrací nejrozšířenějších hardwarových peněženek a pokročilými funkcemi správy UTXO.



## Co je Bitcoin Keeper?



### Filozofie a cíle



Bitcoin Keeper byl navržen tak, aby vyhovoval specifickým potřebám uživatelů bitcoinů, kteří si chtějí zachovat plnou kontrolu nad svými soukromými klíči. Projekt plně přijímá základní principy Bitcoin: otevřený a kontrolovatelný zdrojový kód, respektování soukromí a suverenitu uživatele. K používání aplikace není vyžadována žádná registrace ani osobní údaje a pro podpisové operace může běžet i offline.



Hlavním cílem je nabídnout flexibilní nástroj odolný vůči budoucnosti pro ukládání BTC po dobu několika let, a dokonce i několika generací, díky funkcím dědictví. Aplikace umožňuje uživatelům začít jednoduše s mobilním wallet a postupně se vyvíjet směrem k bezpečnějším řešením s více podpisy.



### Architektura aplikace



Společnost Bitcoin Keeper organizuje správu fondů na základě dvou odlišných koncepcí. **Hot Wallet** je jednoduchý jednotlačítkový wallet, uložený v telefonu, určený pro každodenní výdaje a skromné částky. Trezory** jsou trezory s více podpisy (Multi-Key), které vyžadují několik klíčů pro autorizaci výdaje a jsou určeny pro dlouhodobé bezpečné uložení.



### Hlavní funkce



Bitcoin Keeper podporuje téměř všechny hardwarové peněženky na trhu: Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport a Tapsigner společnosti Coinkite. Integrace probíhá různými metodami v závislosti na zařízení: QR kód, připojení NFC nebo import souboru.



Aplikace také nabízí pokročilou správu UTXO s označováním transakcí, ovládání mincí pro ruční výběr vstupů při odesílání a podporu formátu PSBT pro částečně podepsané transakce.



## Instalace a počáteční konfigurace



Bitcoin Keeper je k dispozici zdarma pro Android v obchodě Google Play a pro iOS v App Store. Uvedeným vydavatelem je BitHyve. Před instalací se ujistěte, že vaše zařízení neobsahuje malware, je aktualizované a není rootnuté nebo jailbreaknuté.



Při prvním spuštění vás aplikace vyzve k vytvoření bezpečnostního kódu PIN. Tento kód chrání přístup k vašemu zařízení wallet a lokálně šifruje citlivá data. Zvolte si silný kód a zapamatujte si jej. Poté můžete aktivovat biometrické ověřování (otisk prstu nebo Face ID) pro rychlejší odemknutí.



![Installation et configuration du PIN](assets/fr/01.webp)



Aplikace poté zobrazí několik úvodních obrazovek s vysvětlením svých tří pilířů: A plánování dědictví pro předávání bitcoinů. Stiskněte tlačítko "Začít" a poté zvolte "Začít nový" pro vytvoření nové konfigurace.



![Écrans d'introduction](assets/fr/02.webp)



## Zjištění rozhraní



Rozhraní aplikace Bitcoin Keeper je uspořádáno do čtyř hlavních karet přístupných ze spodního navigačního panelu:



![Les quatre onglets de l'application](assets/fr/03.webp)



Na kartě **Peněženky** jsou zobrazeny vaše peněženky a jejich zůstatky. Zde máte přístup ke svým peněženkám a můžete odesílat a přijímat bitcoiny. Značky "Hot Wallet" a "Single-Key" nebo "Multi-Key" vám umožní rychle identifikovat typ každé z nich wallet.



Karta **Klíče** centralizuje správu podpisových klíčů. Najdete zde mobilní klíč vygenerovaný aplikací a také všechny klíče importované z hardwarových peněženek. Zde také přidáváte nová podpisová zařízení.



Karta **Concierge** nabízí služby podpory: můžete zadávat dotazy týmu podpory a spojit se s poradci společnosti Bitcoin, kteří vám poskytnou individuální pomoc.



Karta **Další** (Další možnosti) umožňuje přístup k nastavením, jako je připojení k osobnímu serveru, zálohování klíčů, dědictví dokumentů, předvolby zobrazení a správa wallet.



## Připojení k vlastnímu serveru



Pro posílení důvěrnosti umožňuje Bitcoin Keeper připojit aplikaci k vlastnímu serveru Electrum namísto použití výchozích veřejných serverů.



![Configuration du serveur Electrum](assets/fr/04.webp)



Na kartě Další přejděte dolů a najděte nastavení serveru. Stisknutím tlačítka "Přidat server" nakonfigurujte nové připojení. Můžete si vybrat mezi "Public Server" (předkonfigurované veřejné servery) a "Private Electrum" (váš vlastní server).



Pro soukromý server zadejte adresu URL (např. umbrel.local pro uzel Umbrel) a číslo portu (obvykle 50001). Aktivujte protokol SSL, pokud jej server podporuje. Můžete také naskenovat konfigurační QR kód. Po zadání parametrů stiskněte tlačítko "Připojit k serveru".



Pokud ještě nemáte svůj vlastní uzel Bitcoin, podívejte se na náš návod na Umbrel, jednoduchý a cenově dostupný způsob, jak si uplést vlastní uzel:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Přijímání bitcoinů



Na kartě Peněženky vyberte stisknutím tlačítka wallet, ze které chcete přijímat finanční prostředky. Na obrazovce wallet se zobrazí zůstatek a tři akční tlačítka: Odeslat Bitcoin, Přijmout Bitcoin a Zobrazit všechny mince.



![Réception de bitcoins](assets/fr/05.webp)



Stiskněte tlačítko "Receive Bitcoin". Bitcoin Keeper vygeneruje novou adresu příjmu ve formátu Bech32 (začínající bc1...) spolu s jejím QR kódem. K této adrese můžete přidat štítek pro identifikaci zdroje prostředků. Adresu můžete sdílet s odesílatelem zobrazením QR kódu nebo zkopírováním textové adresy.



Aplikace automaticky generuje novou adresu pro každý příjem, čímž zachovává vaše soukromí. V případě potřeby můžete použít funkci "Get New Address" a získat prázdnou adresu.



## Řízení UTXO



Bitcoin Keeper nabízí úplný přehled o UTXO (Nevyčerpané transakční výstupy), které tvoří váš zůstatek. Na obrazovce wallet stiskněte tlačítko "View All Coins" (Zobrazit všechny mince), čímž se dostanete do správce rohů.



![Gestion des UTXO](assets/fr/06.webp)



Na obrazovce "Správa mincí" jsou uvedeny jednotlivé mince UTXO, jejich množství a označení. Toto zobrazení umožňuje sledovat původ mincí a uspořádat je. Prostřednictvím položky "Vybrat k odeslání" můžete vybrat konkrétní UTXO, které se mají odeslat s kontrolou mincí, a zabránit tak míchání mincí různého původu.



## Odeslat bitcoiny



Chcete-li odeslat, vyberte zdrojové portfolio a stiskněte tlačítko "Odeslat Bitcoin". Zadejte cílovou adresu (vloženou nebo naskenovanou pomocí QR kódu) a volitelně přidejte štítek pro identifikaci příjemce.



![Envoi de bitcoins](assets/fr/07.webp)



Na další obrazovce můžete zadat částku, která má být odeslána. Rozhraní zobrazí váš dostupný zůstatek a přepočet na fiat měnu. Zvolte prioritu dobíjení: Nízká (úsporná, ~60 minut), Střední nebo Vysoká (prioritní). Odhadované poplatky v sats/vbyte se zobrazují v reálném čase. Stisknutím tlačítka "Odeslat" můžete pokračovat.



![Confirmation et envoi](assets/fr/08.webp)



Na souhrnné obrazovce se zobrazí všechny podrobnosti: wallet, cílová adresa, priorita transakce, síťové poplatky, odeslaná částka a celková částka. Tyto informace pečlivě zkontrolujte, protože transakce Bitcoin jsou nevratné. Transakci odešlete stisknutím tlačítka "Potvrdit a odeslat".



Zobrazí se potvrzení "Úspěšné odeslání" s úplným shrnutím. Transakce je viditelná v historii "Poslední transakce" se svým označením.



## Uložení klíčů



Zálohování klíče pro obnovení je důležitým krokem. Na kartě Více přejděte do sekce "Zálohování a obnovení" a klikněte na "Recovery Key".



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



Na obrazovce se zobrazí stav záloh. Pro ověření zálohy vás aplikace požádá o potvrzení určitého slova ve vaší větě (např. 7. slovo). Toto ověření zajistí, že jste frázi pro obnovu zapsali správně.



V části "Nastavení klíče pro obnovení" si můžete zobrazit celou frázi prostřednictvím položky "Zobrazit klíč pro obnovení" a zobrazit otisk prstu podepisující osoby vašeho klíče. Frázi o 12 slovech uchovávejte na papíře, na bezpečném místě, mimo dosah vlhkosti a ohně. Nikdy ji neukládejte do připojeného zařízení.



## Přidání externího klíče (hardware wallet)



Jednou z hlavních předností Bitcoin Keeper je integrace hardwarových peněženek. Na kartě Klíče stiskněte tlačítko "Přidat klíč" a přidejte nové podpisové zařízení.



![Ajout d'une clé hardware](assets/fr/10.webp)



Chcete-li připojit hardware wallet, vyberte možnost "Přidat klíč z hardwaru". Aplikace podporuje širokou škálu zařízení: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner a Specter Solutions.



### Konfigurace Tapsigner



Tapsigner je karta NFC od společnosti Coinkite, která je vhodná zejména pro mobilní použití. Pokud se chcete dozvědět více, máme pro vás speciální návod :



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

Chcete-li přidat zařízení Tapsigner, vyberte jej ze seznamu hardwarových peněženek.



![Configuration du Tapsigner](assets/fr/11.webp)



Nejprve zadejte 6-32místný kód PIN vytištěný na zadní straně karty (výchozí u nových karet) nebo svůj kód PIN, pokud je již nakonfigurován. Stiskněte tlačítko "Proceed" (Pokračovat) a po zobrazení nápisu "Ready to scan" (Připraveno ke skenování) přiložte kartu Tapsigner k zadní straně telefonu. Komunikace NFC automaticky importuje veřejný klíč. Poté můžete přidat popis (např. "Métro Card") k identifikaci tohoto klíče.



## Vytvoření portfolia více značek



Jakmile nastavíte klíče, můžete vytvořit multipodpis wallet kombinující několik zařízení. Na kartě Peněženky klikněte na možnost "Přidat Wallet".



![Création d'un nouveau wallet](assets/fr/12.webp)



Máte tři možnosti: "Vytvořit Wallet" pro nové portfolio, "Importovat Wallet" pro obnovení stávajícího wallet nebo "Spolupráce Wallet" pro sdílený trezor. Vyberte možnost "Vytvořit Wallet" a poté "Bitcoin Wallet".



![Sélection du type de wallet](assets/fr/13.webp)



Další obrazovka nabízí různé konfigurace: "Single-key", "2 of 3 multi-key" nebo "3 of 5 multi-key". Chcete-li si multi-sig přizpůsobit, stiskněte tlačítko "Select custom setup" (Zvolit vlastní nastavení). Zvolte například "1 ze 2": ze dvou možných klíčů je vyžadován jeden podpis.



Poté vyberte klíče, které budou tvořit váš trezor. V našem příkladu kombinujeme "Mobilní klíč" (softwarový klíč telefonu) s "TAPSIGNER" (Metro Card). Tato konfigurace nabízí redundanci: pokud se jeden z klíčů stane nedostupným, můžete vždy utratit své prostředky pomocí druhého klíče.



![Finalisation du wallet multisig](assets/fr/14.webp)



Pojmenujte wallet (např. "Testovací plánB"), přidejte volitelný popis a zaškrtněte vybrané klíče. Stiskněte tlačítko "Create Your Wallet". Zobrazí se potvrzovací zpráva "Wallet Created Successfully" (Soubor Wallet úspěšně vytvořen), která vám připomene, abyste soubor obnovy wallet uložili.



Váš nový multisig wallet se nyní objeví na kartě Peněženky s označením "Multi-key" a indikací "1 ze 2".



### Uložení konfiguračního souboru



**Na rozdíl od jednoduchého sejfu wallet, kde k obnovení přístupu stačí fráze pro obnovení, vyžaduje multisig wallet také konfigurační soubor, který popisuje strukturu sejfu (které klíče se účastní, kolik podpisů je požadováno). Bez tohoto souboru nebude možné ani se všemi frázemi pro obnovení obnovit systém wallet.



![Export du fichier de configuration](assets/fr/15.webp)



Chcete-li tento soubor exportovat, vyberte na kartě Peněženky multisignály wallet a poté stiskněte ikonu Nastavení (ozubené kolečko) v pravém horním rohu. V části "Wallet Settings" (Nastavení Wallet) klikněte na položku "Wallet configuration file" (Konfigurační soubor Wallet). K dispozici je několik možností exportu:





- Export PDF**: vytvoří dokument PDF obsahující všechny informace o wallet
- Zobrazit QR**: zobrazí skenovatelný QR kód pro import konfigurace do jiného zařízení
- Airdrop / Export souborů**: exportuje soubor prostřednictvím možností sdílení v telefonu
- NFC**: sdílení prostřednictvím NFC s kompatibilním zařízením



Tento konfigurační soubor uchovávejte odděleně od frází pro obnovení, nejlépe na šifrovaném nebo tištěném médiu. Pokud telefon ztratíte, tento soubor v kombinaci s frázemi pro obnovení pro každý zúčastněný klíč vám umožní obnovit multisig wallet v Bitcoin Keeper nebo v jiném kompatibilním softwaru.



## Osvědčené postupy



### Organizace fondu



Strukturovat bitcoiny podle jejich použití: horký wallet Single-Key pro běžné výdaje s omezeným množstvím a jeden nebo více trezorů Multi-Key pro dlouhodobé úspory. Systematické značení UTXO vám pomůže sledovat, odkud vaše prostředky pocházejí, což je užitečné zejména pro správu důvěrnosti a zamezení míchání mincí různého původu.



Udržujte telefon v bezpečí: aktivujte biometrický zámek, pravidelně provádějte aktualizace systému a dávejte pozor na nainstalované aplikace. A aktualizujte bezpečnostní záplaty pro Bitcoin Keeper.



### Záložní zabezpečení



Uchovávejte alespoň dvě kopie každé fráze pro obnovu na papíře, uložené na geograficky oddělených místech. V případě velkých částek zvažte gravírovaný kov odolný proti katastrofám. Nikdy tyto fráze neukládejte na zařízení připojené k internetu a nikdy je nefotografujte.



U trezorů multi-sig uložte také konfigurační soubor (soubor pro obnovení Wallet), který obsahuje zúčastněné veřejné klíče a strukturu trezoru. Tento soubor v kombinaci s frázemi pro obnovu klíčů umožňuje obnovu systému wallet v jakémkoli kompatibilním softwaru, jako je Sparrow nebo Specter.



## Výhody a omezení



### Nejdůležitější informace





- Aplikace pouze Bitcoin snižuje složitost a riziko
- Nativní integrace vícesignálových trezorů s návodem krok za krokem
- Rozšířená hardwarová podpora wallet (Tapsigner, Coldcard, Ledger, Jade atd.)
- Pokročilá správa UTXO a kontrola mincí
- Možnost připojení k osobnímu serveru Electrum
- Otevřený, kontrolovatelný zdrojový kód



### Omezení, která je třeba zvážit





- Interface převážně v angličtině
- Některé prémiové funkce (zálohování do cloudu, asistovaný server) vyžadují upgrade
- Konfigurace Multisig vyžaduje úvodní školení



## Závěr



Bitcoin Keeper je škálovatelné řešení pro správu bitcoinů. Jeho progresivní přístup, od jednoduchého horkého wallet až po trezory s více podpisy, znamená, že zabezpečení lze vylepšovat podle toho, jak se mění potřeby. Možnost snadné integrace hardwarových peněženek, jako je Tapsigner, otevírá cestu k robustním konfiguracím bez nadměrné složitosti.



Orientace pouze na bitcoiny, otevřený zdrojový kód a respektování soukromí z něj činí volbu, která je v souladu se základními hodnotami ekosystému Bitcoin.



Tento výukový program se zabývá základními funkcemi programu Bitcoin Keeper v jeho bezplatné verzi. Aplikace nabízí také prémiové funkce (zálohování do cloudu, asistované zálohování serveru, kanárkové peněženky), kterým bude věnován samostatný tutoriál. V některém z příštích průvodců se budeme zabývat také funkcí Plánování dědictví, která vám díky vylepšeným trezorům a doprovodným dokumentům integrovaným do aplikace umožní připravit předání vašich bitcoinů vašim blízkým.



## Zdroje





- Oficiální webové stránky: [bitcoinkeeper.app](https://bitcoinkeeper.app)
- Centrum nápovědy: [help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- Zdrojový kód: [github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)