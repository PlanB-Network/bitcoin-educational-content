---
name: Ashigaru
description: fork od společnosti Samourai Wallet pro zabezpečení, správu a mixování bitcoinů
---

![cover](assets/cover.webp)



Ashigaru je mobilní aplikace Bitcoin wallet, která navazuje na projekt Samourai Wallet, ale v nové podobě. Tento software se zrodil ve zvláštním kontextu: v dubnu 2024 byli zakladatelé projektu Samourai Wallet zatčeni americkými úřady a jejich servery byly zabaveny. Ačkoli samotná aplikace Samurai zůstala použitelná, v současné době již není udržována. Ashigaru je svobodná verze Samuraje Wallet pro fork, kterou udržuje anonymní tým, aby byla zaručena kontinuita funkčnosti Samuraje a zachována jeho původní filozofie: bránit soukromí a suverenitu uživatelů Bitcoin.



Ashigaru přebírá většinu DNA Samourai: podobné rozhraní, zjevně samospasitelný přístup, otevřený zdrojový kód a důraz na soukromí. Kód je šířen pod licencí GNU GPLv3, která zaručuje, že kdokoli může software auditovat, upravovat nebo dále šířit.



Aplikace Ashigaru integruje sadu pokročilých nástrojů pro důvěrnost a správu vašich UTXO:




- Whirlpool**, protokol pro spojování mincí založený na Zerolinku, který umožňuje přerušit deterministické vazby mezi vstupy a výstupy transakcí, aniž byste ztratili suverenitu nad svými prostředky.
- PayNym**, který implementuje opakovaně použitelné platební kódy (BIP47), nyní reprezentované systémem avatarů "*Pepehash*".
- Ricochet**, funkce, která do transakcí přidává mezilehlé skoky, aby bylo obtížnější je vystopovat.
- A samozřejmě ***Coin Control*** pro přesný výběr, zmrazení a označení UTXO.
- Dávkové odesílání*** pro snížení nákladů seskupením několika plateb do jedné transakce.
- Režim **Stealth**, který skryje aplikaci v mobilním telefonu za falešný spouštěč, aby si jí při fyzické kontrole telefonu nikdo nevšiml.
- Pokročilé nástroje pro optimalizaci výdajů (payjoin, stonewall...).
- Optimalizovaný systém obnovy pomocí fráze Passphrase BIP39.
- Systém pro automatickou optimalizaci výběru transakčních poplatků.



![Image](assets/fr/01.webp)



Ashigaru je proto určena uživatelům, kteří jsou si vědomi problémů spojených s dohledatelností transakcí v systému Bitcoin. Ať už jste uživatel, který dbá na ochranu soukromí, zkušený bitcoiner, který se zavázal k vlastnímu dohledu, nebo jednotlivec vystavený rizikům zvýšeného dohledu, tato aplikace wallet vám poskytne nástroje, které potřebujete k tomu, abyste získali zpět kontrolu nad svou aktivitou na Bitcoin.



Ashigaru je k dispozici v mobilní verzi prostřednictvím aplikace, kterou si v tomto návodu prozkoumáme. Lze ji však používat i na počítači pomocí aplikace ***Ashigaru Terminal***, kterou si představíme v některém z příštích tutoriálů.



![Image](assets/fr/02.webp)



V tomto návodu bych vás rád seznámil se základním používáním Ashigaru: instalací, připojením k Dojo, zálohováním, přijímáním a odesíláním bitcoinů. Pokročilé nástroje budou představeny v dalších specializovaných tutoriálech.



## 1. Předpoklady pro Ashigaru



Aplikace vyžaduje několik předpokladů pro správnou funkci. Především se nejedná o aplikaci dostupnou v klasických obchodech, jako je Google Play Store nebo App Store. Do telefonu se instaluje ručně pouze ze svého souboru `.apk`, který lze stáhnout prostřednictvím sítě Tor. Pokud tedy používáte iPhone, tato metoda nebude fungovat: budete potřebovat zařízení se systémem Android.



Pro stažení souboru `.apk` přes Tor budete potřebovat prohlížeč, který umožňuje přístup k webům `.onion`. Nejjednodušší způsob je nainstalovat si do telefonu aplikaci Tor Browser, která je k dispozici v [Google Play Store](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) nebo přímo [prostřednictvím jejího souboru `.apk`](https://www.torproject.org/download/#android).



![Image](assets/fr/03.webp)



Většina nejnovějších smartphonů ve výchozím nastavení blokuje instalaci aplikací z neznámých zdrojů. Chcete-li povolit instalaci, musíte tuto možnost dočasně aktivovat v nastavení zařízení pro prohlížeč Tor Browser. Po instalaci aplikace nezapomeňte tuto funkci deaktivovat, abyste posílili zabezpečení telefonu.



Dalším nezbytným předpokladem pro používání Ashigaru je uzel Bitcoin Dojo. Z důvodu bezpečnosti a suverenity tým Ashigaru neudržuje centralizovaný server pro připojení vaší aplikace. Budete tedy muset provozovat vlastní instanci Dojo nebo se připojit k důvěryhodné instanci.



Dojo umožňuje vaší aplikaci Ashigaru konzultovat informace z blockchainu, zobrazovat zůstatky adres a vysílat vaše transakce v síti Bitcoin.



Chcete-li se dozvědět více o nástroji Dojo a naučit se jej nainstalovat, navrhuji vám sledovat tento specializovaný výukový program :



https://planb.network/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Pokud si opravdu nemůžete dovolit provozovat vlastní Dojo, můžete najít lidi, kteří jsou ochotni sdílet své instance zdarma na adrese [dojobay.pw](https://www.dojobay.pw/mainnet/). Může to být dočasné řešení, ale z dlouhodobého hlediska doporučuji používat vlastní Dojo, abyste si zaručili suverenitu a důvěrnost.



## 2. Zkontrolujte a nainstalujte aplikaci Ashigaru



### 2.1. Stáhněte si aplikaci Ashigaru



V telefonu otevřete prohlížeč Tor Browser a přejděte na [oficiální webové stránky Ashigaru](https://ashigaru.rs/download/) v sekci `Download`. Poté klikněte na tlačítko `Stáhnout pro Android` a stáhněte instalační soubor.



![Image](assets/fr/04.webp)



Před instalací aplikace do vašeho zařízení zkontrolujeme její pravost a integritu. To je velmi důležitý krok, zejména při instalaci aplikace přímo ze souboru `.apk'.



### 2.2. Zkontrolujte aplikaci Ashigaru



Vraťte se na [oficiální webové stránky Ashigaru](https://ashigaru.rs/download/) do sekce `Stáhnout` a zkopírujte zprávu zobrazenou pod názvem `SHA-256 Hash souboru APK`. Zkopírujte celý blok od `Začátek PGP PODPISANÉ ZPRÁVY` až po `Konec PGP PODPISU`.



![Image](assets/fr/05.webp)



V telefonu otevřete novou kartu v prohlížeči Tor Browser a přejděte na [nástroj pro ověření Keybase](https://keybase.io/verify). Vložte zprávu, kterou jste právě zkopírovali, do příslušného pole a klikněte na tlačítko `Ověřit`.



![Image](assets/fr/06.webp)



Pokud je podpis pravý, zobrazí Keybase zprávu potvrzující, že soubor byl podepsán vývojáři Ashigaru. Můžete také kliknout na profil `ashigarudev` uvedený databází Keybase a zkontrolovat, zda otisk jejich klíče přesně odpovídá : `A138 06B1 FA2A 676B`.



Pokud se však v této fázi objeví chyba, znamená to, že podpis je neplatný. V takovém případě soubor APK **neinstalujte**. Začněte znovu od začátku nebo před pokračováním požádejte komunitu o pomoc.



![Image](assets/fr/07.webp)



Keybase vám poskytla hash aplikace. Nyní zkontrolujeme, zda se hash staženého souboru `.apk` shoduje s hashem ověřeným na Keybase. Za tímto účelem přejděte na stránku [HASH FILE ONLINE](https://hash-file.online/).



![Image](assets/fr/08.webp)



Klikněte na tlačítko `PROHLÉDNOUT...` a vyberte soubor `.apk` stažený v kroku 2.1.


Poté vyberte hashovací funkci `SHA-256` a kliknutím na `CALCULATE HASH` vypočítejte hash vašeho souboru.



![Image](assets/fr/09.webp)



Na webu se zobrazí hash vašeho souboru `.apk`. Porovnejte ho s hashem, který jste ověřili na Keybase.io. Pokud jsou oba hashe shodné, kontrola pravosti a integrity proběhla úspěšně. Nyní můžete přistoupit k instalaci aplikace.



![Image](assets/fr/10.webp)



### 2.3. nainstalujte aplikaci Ashigaru



Chcete-li aplikaci nainstalovat, otevřete správce souborů v telefonu a přejděte do složky stažených souborů. Poté klikněte na soubor `.apk`, který jste právě zkontrolovali, a po výzvě potvrďte instalaci.



![Image](assets/fr/11.webp)



Ashigaru je nyní nainstalováno v telefonu.



## 3. Inicializace aplikace a vytvoření portfolia Bitcoin



Při prvním spuštění aplikace vyberte možnost `MAINNET`.



![Image](assets/fr/12.webp)



Poté klikněte na `Začítat`.



![Image](assets/fr/13.webp)



Nyní vytvoříme nové portfolio Bitcoin. Stiskněte tlačítko `Vytvořit nové portfolio wallet`.



![Image](assets/fr/14.webp)



### 3.1. vytvořit portfolio Bitcoin



Ashigaru vyžaduje passphrase BIP39. Vyberte si passphrase a zadejte jej do příslušných polí. Musí být co nejdelší a nejnáhodnější, aby odolal útoku hrubou silou.



Okamžitě proveďte fyzickou zálohu tohoto passphrase. Jedná se o velmi důležitý krok: pokud ztratíte telefon, **pokud již nebudete mít tento passphrase, nebudete mít přístup ke svým bitcoinům** uloženým ve vašem Ashigaru wallet. Tentýž passphrase se používá také k zašifrování obnovovacího souboru wallet.



Pokud nevíte, co je to passphrase, nebo plně nerozumíte tomu, jak funguje, důrazně doporučuji přečíst si tento doplňkový návod. Je to důležité, protože passphrase je kritickým prvkem vašeho zabezpečení: nepochopení jeho použití by mohlo vést k trvalé ztrátě vašich finančních prostředků.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Po zadání kódu passphrase klikněte na tlačítko `NEXT`.



![Image](assets/fr/15.webp)



Poté zvolte kód PIN. Tento kód bude sloužit k odemknutí vašeho zařízení Ashigaru wallet a ochrání jej před neoprávněným fyzickým přístupem. Neúčastní se kryptografického odvození klíčů vašeho zařízení wallet. To znamená, že i bez znalosti kódu PIN bude moci kdokoli s vaší mnemotechnickou frází a passphrase získat přístup k vašim bitcoinům.



Zvolte dlouhý, náhodný kód PIN. Nezapomeňte mít záložní kopii na jiném místě než telefon, abyste zabránili jejich současnému napadení.



![Image](assets/fr/16.webp)



Po vytvoření kódu PIN zobrazí Ashigaru mnemotechnickou frázi wallet. Varování: Tato fráze v kombinaci s vaším passphrase poskytuje plný přístup k vašim bitcoinům. Kdokoli, kdo ji má v držení, se může zmocnit vašich prostředků, i když nemá přístup k vašemu telefonu. Tuto sekvenci 12 slov lze použít k obnovení wallet v případě ztráty, krádeže nebo rozbití telefonu. Je proto důležité uložit ji s maximální opatrností na fyzický nosič (papír nebo kov).



Tuto frázi nikdy neukládejte v digitální podobě, jinak riskujete, že vaše finanční prostředky budou odcizeny. V závislosti na vaší bezpečnostní strategii si můžete vytvořit několik fyzických kopií, ale nikdy je nerozdělujte. Udržujte slova v přesném pořadí a ujistěte se, že jsou očíslována.



A konečně, nikdy neukládejte mnemotechnickou pomůcku a kód passphrase na stejné místo. Pokud by došlo k prozrazení obou současně, mohl by útočník získat přístup k vašemu wallet.



![Image](assets/fr/17.webp)



Chcete-li se dozvědět více o tom, jak zabezpečit mnemotechnickou frázi, přečtěte si tento doplňující návod :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru vás poté požádá, abyste znovu potvrdili svou passphrase. Využijte této příležitosti a zkontrolujte, zda je vaše fyzická záloha správná.



![Image](assets/fr/18.webp)



### 3.2. připojit dódžó



Poté následuje krok připojení k vašemu Dojo. Jak bylo vysvětleno v úvodu, Ashigaru musí být připojeno k Dojo, aby mohlo komunikovat se sítí Bitcoin.



Přihlaste se do nástroje "Maintenance Tool" v programu Dojo a otevřete nabídku `PAIRING`.



![Image](assets/fr/19.webp)



V aplikaci Ashigaru stiskněte tlačítko `Scan QR` a naskenujte připojovací QR kód zobrazený zařízením DMT. Poté klikněte na tlačítko `Pokračovat` pro potvrzení.



![Image](assets/fr/20.webp)



Zadejte kód PIN a odemkněte zařízení wallet. Tím se dostanete na stránku synchronizace. Je normální, že se v této fázi zobrazí chyby *PayNym*, protože zařízení wallet je nové. Jednoduše klikněte na tlačítko `Pokračovat`.



![Image](assets/fr/21.webp)



Poté budete přesměrováni na domovskou stránku svého portfolia.



![Image](assets/fr/22.webp)



Než budete pokračovat, doporučuji provést zkušební obnovení, dokud wallet ještě neobsahuje žádné bitcoiny. To vám umožní zkontrolovat, zda vaše papírové zálohy fungují správně. Chcete-li zjistit, jak na to, postupujte podle tohoto návodu:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Nastavení aplikace Ashigaru



Chcete-li se dostat do nastavení aplikace, klikněte na obrázek svého *PayNym* v levém horním rohu a poté vyberte možnost `Nastavení`.



![Image](assets/fr/23.webp)



Zde najdete několik možností, jak přizpůsobit provoz Ashigaru svým potřebám. Důrazně však doporučuji, abyste hned na začátku aktivovali 2 důležité parametry.



Nejprve otevřete nabídku `Zabezpečení > Skrytý režim` a poté tuto funkci aktivujte, pokud ji potřebujete. Skryje aplikaci Ashigaru za název, logo a rozhraní běžné aplikace nainstalované v telefonu. Cílem je zabránit tomu, aby někdo v případě fyzické kontroly vašeho telefonu identifikoval aplikaci Ashigaru.



![Image](assets/fr/24.webp)



Každá nabízená falešná aplikace má specifickou metodu pro odemknutí skutečného rozhraní Ashigaru. Pokud například zvolíte kalkulačku, aplikace Ashigaru zmizí z domovské obrazovky a nahradí ji falešná kalkulačka. Po jejím otevření se zobrazí klasické funkční rozhraní kalkulačky, ale pro přístup k Ashigaru stačí pětkrát rychle klepnout na symbol `=`.



Druhým důležitým parametrem, který je třeba aktivovat, je [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). Tato volba umožňuje zvýšit náklady na transakci, pokud se zasekne v mempoolech, protože náklady jsou příliš nízké. Můžete ji aktivovat prostřednictvím nabídky `Transakce > Utratit pomocí RBF`.



![Image](assets/fr/25.webp)



Tip: Zobrazovanou jednotku svého portfolia můžete změnit z `BTC` na `sat` jednoduše kliknutím na celkový zůstatek zobrazený na domovské stránce.



## 5. Příjem bitcoinů na Ashigaru



Nyní, když je vaše portfolio funkční, můžete přijímat satss. Za tímto účelem stiskněte tlačítko `+` v pravém dolním rohu rozhraní a poté zelené tlačítko `Přijímat`.



![Image](assets/fr/26.webp)



Ashigaru pak zobrazí první nepoužitou přijímací adresu v wallet, aby se zabránilo opakovanému použití adresy (opakované použití adresy je velmi špatný postup pro vaše soukromí). Tuto adresu pak můžete předat osobě nebo službě, která vám potřebuje poslat bitcoiny.



![Image](assets/fr/27.webp)



Po odvysílání transakce v síti se automaticky zobrazí na domovské stránce aplikace.



![Image](assets/fr/28.webp)



## 6. Odesílání bitcoinů pomocí Ashigaru



Nyní, když máte bitcoiny ve svém účtu Ashigaru wallet, je můžete také posílat. To provedete stisknutím tlačítka `+` vpravo dole a poté vyberte červené tlačítko `Odeslat`.



![Image](assets/fr/29.webp)



Poté vyberte účet, ze kterého chcete provést výdaj. Prozatím jsme se nezabývali účtem `Postmix`, který je vyhrazen pro coinjoiny a na který se podíváme v některém z dalších tutoriálů. Budeme tedy posílat prostředky z hlavního vkladového účtu.



![Image](assets/fr/30.webp)



Zadejte údaje o transakci: částku k odeslání a adresu příjemce Bitcoin.



![Image](assets/fr/31.webp)



Kliknutím na tři malé tečky v pravém horním rohu a poté na `Zobrazit nespotřebované výstupy` si můžete také přesně vybrat, které UTXO chcete utratit, abyste zvýšili své soukromí.



![Image](assets/fr/32.webp)



Po vyplnění všech údajů pokračujte kliknutím na bílou šipku v dolní části rozhraní.



Poté se zobrazí souhrnná stránka se všemi podrobnostmi o vaší transakci. Zobrazí se několik důležitých prvků:




- V bloku `Destination` naposledy zkontrolujte, zda jsou adresa příjemce a odeslaná částka správné;
- V bloku `Poplatky` si můžete prohlédnout sazbu poplatku automaticky vybranou Ashigaru a v případě potřeby ji upravit kliknutím na `Správce` ;
- Blok `Transakce` označuje typ transakce, kterou se chystáte provést. Zde hovoříme o jednoduché transakci, ale Ashigaru podporuje i další typy transakcí optimalizovaných pro ochranu soukromí, kterým se budeme podrobně věnovat v některém z příštích tutoriálů;
- Červený blok `Transaction Alert` vás varuje, pokud vaše transakce vykazuje vzorce, které mohou být rozpoznány nástroji pro analýzu řetězce a které by mohly ohrozit vaše soukromí. Kliknutím na něj si můžete zobrazit podrobnosti. V mém případě mi například Ashigaru říká, že odeslaná částka je zaokrouhlená (`3000 sats`), což mi umožňuje odvodit, který výstup odpovídá výdaji a který je směnou. Chcete-li se o těchto heuristických metodách analýzy řetězce dozvědět více, zvu vás na mé školení BTC 204 na stránkách Plan ₿ Academy ;
- Nakonec můžete k transakci přidat štítek, abyste měli záznam o jejím účelu.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Jakmile zkontrolujete všechny údaje, odešlete bitcoiny pomocí zelené šipky. Podržte šipku stisknutou a poté ji přetáhněte doprava, čímž odeslání potvrdíte.



![Image](assets/fr/33.webp)



Vaše transakce byla odvysílána v síti Bitcoin.



![Image](assets/fr/34.webp)



## 7. Obnovení vašeho Ashigaru wallet



Obnova Ashigaru wallet se mírně liší od obnovy klasického Bitcoin wallet, protože aplikace používá stejné metody jako Samurai Wallet. Pokud ztratíte přístup ke svému wallet (ať už proto, že jste zapomněli PIN, odinstalovali jej nebo ztratili telefon), existuje několik způsobů, jak bitcoiny obnovit.



Pokud máte stále přístup k telefonu nebo pokud jste si vytvořili zálohu tohoto souboru, nejjednodušší metodou je použít záložní soubor `ashigaru.txt`. Tento soubor obsahuje všechny informace, které potřebujete k obnovení svého portfolia v nové instanci Ashigaru (nebo v Sparrow Wallet), ale je zašifrován pomocí passphrase, který jste definovali v kroku 3.1 tohoto návodu. Pro použití této metody proto musíte mít k dispozici jak soubor `ashigaru.txt`, tak svůj passphrase.



Pomocí těchto dvou prvků můžete například obnovit své portfolio na Sparrow Wallet.



![Image](assets/fr/35.webp)



Pokud nemáte přístup k souboru `ashigaru.txt`, můžete i tak získat přístup ke svým prostředkům pomocí mnemotechnické fráze passphrase, stejně jako v případě jakéhokoli jiného portfolia Bitcoin. Doporučuji provést toto obnovení buď na nové instanci Ashigaru, nebo přímo na Sparrow Wallet, abyste snadno obnovili obchozí cesty z Whirlpool, pokud jste jej používali. Případně můžete tyto informace importovat do jakéhokoli jiného softwaru kompatibilního s BIP39 ručním zadáním odvozovacích cest.



Další informace o tomto postupu naleznete v kompletním návodu, který jsem napsal pro obnovu Wallet Samurai wallet. Jelikož Ashigaru je fork, postup je totožný:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Jak vidíte, ať už použijete jakoukoli metodu obnovy, je zařízení passphrase nepostradatelné. Nezapomeňte ji proto pečlivě zálohovat. V závislosti na vaší bezpečnostní strategii si můžete vytvořit i několik kopií.



## 8. Aktualizace aplikace



Chcete-li aplikaci Ashigaru aktualizovat, protože jste ji nainstalovali ze souboru `.apk`, a nikoli prostřednictvím Obchodu Play jako běžnou aplikaci, musíte stáhnout nový soubor `.apk` odpovídající aktualizované verzi a poté jej nainstalovat ručně.



Zopakujte kroky popsané v části 2 tohoto návodu s tím rozdílem, že když kliknete na soubor `.apk` pro spuštění instalace, **telefon se systémem Android by vám měl nabídnout možnost `Aktualizovat`, nikoli `Instalace`**.



![Image](assets/fr/41.webp)



Toto je velmi důležitý bod: pokud systém Android zobrazuje `Install` místo `Update`, pravděpodobně instalujete podvodnou verzi. V takovém případě okamžitě přerušte instalační postup.



Stejně jako při první instalaci zkontrolujte před aktualizací pravost a neporušenost souboru `.apk`.



Chcete-li zjistit, kdy bude k dispozici nová verze, občas se podívejte na oficiální webové stránky Ashigaru. Buďte si jisti, že Ashigaru je stabilní, vyzrálá aplikace, zděděná po Samourai Wallet, a aktualizace jsou ve srovnání s mladším softwarem poměrně vzácné.



## 9. Přispějte na projekt Ashigaru



Ashigaru je open-source projekt. Pokud chcete podpořit jeho vývoj, můžete přispět přímo z aplikace prostřednictvím služby PayNym.



Za tímto účelem klikněte na své PayNym v pravém horním rohu rozhraní a poté vyberte svůj platební kód začínající na `PM...`.



![Image](assets/fr/36.webp)



Poté stiskněte tlačítko `+` v pravém dolním rohu obrazovky.



![Image](assets/fr/37.webp)



Jako příjemce vyberte `Ashigaru Open Source Project`.



![Image](assets/fr/38.webp)



Kliknutím na tlačítko `CONNECT` navážete komunikační kanál BIP47 (více o tomto protokolu v následujícím návodu).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Po potvrzení transakce oznámení můžete odeslat svůj dar na projekt kliknutím na malou bílou šipku v pravém horním rohu rozhraní.



![Image](assets/fr/40.webp)



Nyní víte, jak používat základní funkce aplikace Ashigaru. V příštích tutoriálech se podíváme na to, jak využívat pokročilé výdajové transakce, a také na Whirlpool, implementaci coinjoin zděděnou ze Samuraje Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
