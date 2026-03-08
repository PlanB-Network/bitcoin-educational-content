---
name: Valet Bitcoin
description: Valet vám přináší uzel Lightning, který není opatrovnickým uzlem, do kapsy
---

![cover_valet](assets/cover.webp)



## Úvod


Valet je lehký, samostatně použitelný systém Bitcoin a Lightning wallet, který nabízí snadný a pohodlný proces nástupu pro začátečníky. Byl speciálně přizpůsoben pro obsluhu komunit Bitcoin a oběhových hospodářství, zejména v odlehlých oblastech.


Jedná se o fork z **Simple Bitcoin Wallet (SBW)** s pokročilou funkcí hostovaného kanálu Lightning nazvanou **Fiat Channels**, která je navržena tak, aby umožnila komukoli přijímat platby Lightning bez rizika volatility.


Valet je v současné době k dispozici pouze pro zařízení se systémem Android a lze jej stáhnout a nainstalovat z několika otevřených obchodů s aplikacemi. Valet však není **hostován** v **obchodě Google Play** z důvodu ochrany osobních údajů vývojářů a obav o jejich důvěryhodnost.



## Stažení a instalace aplikace Valet


Valet si můžete stáhnout jako soubor APK ze stránky Standard Sats' GitHub. společnost [Standard Sats](https://standardsats.github.io/) vyvinula aplikaci Valet.


👉 Chcete-li si Valet stáhnout, navštivte stránku Standard Sats [GitHub](https://github.com/standardsats/valet/releases) a najděte **nejnovější** verzi (často je to ta nejvyšší).


👉 Přejděte na **Assets** a klikněte na soubor s příponou pouze **.apk**. Stahování se spustí automaticky.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


👉 Po dokončení stahování přejděte do **Správce souborů** > **Stažené soubory** ve svém zařízení a vyberte soubor Valet apk.


![Select_valet_apk](assets/en/002.webp)


👉 Nainstalujte ji a za několik sekund bude aplikace připravena a objeví se na domovské obrazovce.


![valet_icon_on_homescreen](assets/en/003.webp)


Případně si můžete Valet stáhnout z obchodu s aplikacemi **F-Droid**. Pokud aplikaci F-Droid ve svém zařízení nemáte, můžete si ji stáhnout a nainstalovat [zde](https://f-droid.org/en/).


👉 Na domovské obrazovce otevřete aplikaci F-Droid a vyhledejte položku **Valet**. Ze dvou zobrazených možností vyberte první možnost s **fialovo-bílou ikonou** a klikněte na **Stáhnout**.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


👉 Po stažení klikněte na tlačítko **Install** a postupujte podle pokynů na obrazovce. Po dokončení instalace můžete aplikaci Valet spustit z F-Droid kliknutím na tlačítko **Otevřít** nebo ji spustit z domovské obrazovky zařízení.



## Vytvoření modelu Bitcoin Wallet


V systému Valet můžete nastavit zařízení Bitcoin wallet ve dvou jednoduchých krocích.


👉 Spusťte aplikaci Valet z domovské obrazovky zařízení nebo z aplikace F-Droid. Zobrazí se obrazovka nastavení wallet se dvěma možnostmi: **Vytvořit nový Wallet** a **Obnovit stávající Wallet**.


👉 Vyberte možnost **Vytvořit nový Wallet** a okamžitě se vytvoří nový wallet a budete přesměrováni na domovskou stránku.


![set_up_a\_new_wallet](assets/en/006.webp)



## Zálohování výchozí fráze


👉 Na domovské stránce wallet klikněte na kartu **Green** s nápisem **"Klepnutím uložíte frázi pro obnovení wallet pro případ, že byste zařízení někdy ztratili nebo vyměnili "**


![seed_phrase_green_card](assets/en/007.webp)


👉 Zobrazí se sada 12 anglických slov. Zapište si je na papír v pořadí od 1 do 12 a uschovejte je.


![the_seed_phrase](assets/en/008.webp)


### Věnujte pozornost ⚠️:


Věnujte pozornost následujícím prvkům:


- Jak již víte, Valet je samoobslužný systém wallet, takže vaše věta seed je jediným přístupem k obnovení vašeho systému Wallet.
- Pokud někdy ztratíte frázi seed, **nikdy** nezískáte přístup k frázi wallet.
- Pokud někdo získá vaši větu seed, může vám nenávratně ukrást všechny Bitcoin.


Musíte si tedy napsat 12 slov seed a uložit je na bezpečném místě. Nikdy byste si neměli pořizovat snímek obrazovky, ukládat ji jako koncept v e-mailu nebo ji ukládat do jakéhokoli elektronického zařízení, které bylo kdy připojeno k internetu.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Přijímání a odesílání Bitcoin v systému Valet


Valet je samoobslužný model wallet s možností použití on-chain i Lightning Bitcoin. To znamená, že můžete přijímat a odesílat Bitcoin ze systému Valet buď prostřednictvím **On-chain**, nebo prostřednictvím **Lightning Network**.


Abyste však mohli přijímat nebo odesílat Bitcoin prostřednictvím Lightning, musíte nastavit kanál Lightning pomocí on-chain Bitcoin jako Liquidity. Nebo si můžete od prodejců zakoupit nějakou likviditu kanálu Lightning.



## Generování řetězce Bitcoin Address


Chcete-li přijímat Bitcoin prostřednictvím on-chain, musíte si vygenerovat adresu Bitcoin.


👉 Na domovské stránce wallet se zobrazí **Oranžová** a **Fialová karta** s označením **Bitcoin** a **Lightning**.


👉 Klikněte na oranžovou kartu s označením **Bitcoin**. Budete přesměrováni na obrazovku se zobrazením adresy Bitcoin.


![click_on_Bitcoin_card](assets/en/009.webp)


👉 Adresu můžete **zkopírovat** a poslat ji osobě, která vám Bitcoin posílá, nebo kliknutím na tlačítko **sdílet** poslat QR kód osobě prostřednictvím sociálních médií nebo jiných komunikačních kanálů.


👉 Můžete také kliknout na tlačítko **Upravit** a nastavit množství Bitcoin, které má být na danou adresu odesláno.


**Upozornění:** Podobně jako u faktury se funkce úprav hodí ve scénářích, kdy můžete chtít na určitou adresu v určitém okamžiku obdržet určité množství Bitcoin. To však neznamená, že adresa nemůže obdržet vyšší nebo nižší množství.


👉Kliknutím na **Další čerstvé adresy** vygenerujete nové náhodné adresy.


![generating_a\_bitcoin_add](assets/en/010.webp)


👉 Adresu on-chain Bitcoin můžete také vygenerovat kliknutím na tlačítko **Přijmout** v dolní části domovské stránky wallet. Poté vyberte možnost **Přijmout na bitcoinovou adresu** a pokračujte stejným postupem jako výše.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Odesílání Bitcoin prostřednictvím řetězce On-chain


Vysílání Bitcoin ze zařízení Valet wallet prostřednictvím on-chain je jednoduchý úkol.


👉 V dolní části domovské stránky wallet klikněte na tlačítko **Odeslat**, zadejte adresu Bitcoin nebo klikněte na **Skenovat**, čímž naskenujete QR kód adresy, a poté klikněte na **Ok**.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


👉 Zadejte částku Bitcoin, kterou chcete odeslat. Částku můžete zadat ručně v měně Sats nebo v měně Fiat, případně můžete kliknout na **Max** a použít celý zůstatek on-chain.


👉 Můžete také upravit poplatky, které chcete za transakci zaplatit, kliknutím na malé zelené pole s nápisem **poplatek** a následným posunutím bílé tečky doprava nebo doleva poplatky zvýšíte, resp. snížíte. Kliknutím na tlačítko **Ok** transakci odešlete.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Nastavení kanálu Lightning Network


Jak bylo uvedeno výše, Valet je samospustitelný Bitcoin a Lightning wallet; abyste tedy mohli odesílat a přijímat Bitcoin prostřednictvím sítě Lightning, musíte nejprve nastavit kanál Lightning podle následujících kroků:


👉 Na domovské obrazovce klikněte na **fialovou kartu** s nápisem **Blesk**. Zobrazí se stránka s následujícími možnostmi:



- Skenování uzlu QR
- Nákup na LNBIG.COM
- Nákup na BITREFILL.COM
- Žádost o resynchronizaci grafu LN.


Když vyberete možnost **Nakoupit z lnbig.com** nebo **Nakoupit z bitrefill.com**, budete přesměrováni na webové stránky těchto společností, kde si můžete zakoupit příchozí likviditu několika kapacit. Poslední možnost **Požádat o resynchronizaci grafu LN** prozatím ignorujte.


Proto je naší volbou **Skenování uzlu QR**. V tomto okamžiku musíte mít rozhodnuto a získat **QR kód** uzlu, ke kterému chcete otevřít kanál. Kanály můžete otevřít do libovolného veřejného uzlu dle vlastního výběru. Podívejte se na [1ML](https://1ml.com/) nebo [Amboss](https://amboss.space/), vyberte libovolný veřejný uzel podle svého výběru a naskenujte příslušný QR kód vybraného uzlu.


![channel_opening_options](assets/en/016.webp)


👉 Budete automaticky přesměrováni na další stránku, kde nyní musíte financovat svůj kanál. I v tomto případě platí, že pro samopřenosné použití sítě Lightning je nutné, abyste k financování kanálu použili své karty Bitcoin. To znamená, že musíte mít ve svém zařízení on-chain wallet karty Bitcoin, kterými můžete financovat kanál Lightning. Více informací o síti Lightning naleznete v tomto článku od [Hacken](https://hacken.io/discover/lightning-network/).


![fund_channel](assets/en/017.webp)


👉 Zadejte **částku** Bitcoin, kterou chcete kanál financovat, nebo klikněte na **Max** a použijte celý zůstatek on-chain Bitcoin. Můžete upravit **poplatek** nebo ponechat výchozí nastavení poplatku a kliknout na **Ok**.


**Upozornění:** Částka, kterou kanál financujete, bude představovat kapacitu vašeho nového kanálu (tj. celkový objem Sats, který může být do tohoto kanálu a z tohoto kanálu převeden)


Je také důležité, abyste při otevírání kanálu použili jako částku financování více než **100 000 Sats**. Je to proto, že mnoho uzlů Lightning vyžaduje pro otevření kanálu k nim minimálně 100 000 Sats kapacity. Abyste se tedy vyhnuli pokusům a omylům, jednoduše používejte částky vyšší než toto rozmezí.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


👉 Když se v tuto chvíli podíváte na svou domovskou stránku wallet, uvidíte, že vaše finanční částka byla přesunuta z karty **Bitcoin** na kartu **Lightning**. V historii transakcí uvidíte, že se transakce financování zpracovává.


![channel_funding_processing](assets/en/020.webp)


👉 Pokud kliknete na kartu Lightning, zobrazí se informace o tom, že se váš kanál Lightning otevírá. V seznamu transakcí se také zobrazí transakce **financování kanálu**. Počkejte, až bude transakce financování potvrzena na blockchain, a váš kanál Lightning bude připraven.


![channel_opening](assets/en/021.webp)


👉 Jakmile je transakce financování potvrzena, klikněte na domovské stránce na kartu **Lightning** a zobrazí se vám následující informace o vašem kanálu Lightning:



- RANDOMNÍ SADA ČÍSEL ODDĚLENÝCH TEČKAMI:** Jedná se o IP adresy uzlů. (IPV4 a IPV6)
- KAPACITA:** Jedná se o celkový objem Sats, který lze tímto kanálem odeslat a přijmout
- CAN SEND:** Toto je množství Sats, které můžete v tuto chvíli odeslat. Všimněte si, že je to téměř stejný údaj jako **Kapacita**. Je to proto, že jste prostřednictvím kanálu neodeslali žádné platby.
- CAN RECEIVE:** Toto je počet Sats, které můžete v daném okamžiku přijímat na tomto kanálu. (V tuto chvíli to bude málo nebo nic, protože abyste mohli přijímat, musíte nejprve vyslat nějaké Sats, abyste vytvořili příchozí Liquidity)
- REFUNDABLE:** Zobrazuje částku, která se po uzavření kanálu vrátí na vaši adresu on-chain. Tato částka se také označuje jako **místní zůstatek vašeho kanálu**. Všimněte si, že je jen o něco menší než kapacita kanálu, a to proto, že při uzavření kanálu musíte zaplatit poplatek za zveřejnění uzavírací transakce na blockchain, stejně jako jste to udělali při financování kanálu. Systém tedy odečetl přibližnou nejnižší částku, kterou zaplatíte)
- VALUE IN FLIGHT:** Když někdo pošle na váš kanál nějaký sats nebo když se vy pokusíte někomu poslat nějaký sats a z nějakého důvodu se transakce zpozdí, často se to zobrazí v tomto poli.


![channel_info](assets/en/022.webp)


## Odesílání Sats prostřednictvím vašeho kanálu


Odesílání Sats prostřednictvím Lightning Network je jednoduchý úkol.


👉 V dolní části úvodní stránky klikněte na **Odeslat** a **vložte** fakturu Blesku (musíte ji mít zkopírovanou) do určeného pole nebo klikněte na **Skenovat** a naskenujte QR kód faktury Blesku.


![click_send_or_scan](assets/en/023.webp)


Většina faktur Lightning obsahuje předem zadanou částku k úhradě. V několika případech se však může jednat o otevřenou fakturu, kde je třeba částku vyplnit.


👉 Zadejte částku v **dolárech** nebo **Sats** nebo klikněte na **Max**, abyste využili celý zůstatek na kanálu Blesk, a klikněte na **Ok**. Jakmile bude nalezena vhodná cesta, bude vaše platba odeslána a dokončena během několika sekund. Sledujte na domovské stránce, zda byla platba dokončena. Po dokončení se označí zelenou fajfkou.


![enter_the_amount](assets/en/024.webp)


## Příjem Sats prostřednictvím vašeho kanálu


Přijímání plateb v kanálu Lightning do značné míry závisí na tom, zda máte příchozí Liquidity, nebo ne. Po otevření kanálu nebudete moci přijímat platby, dokud neodešlete alespoň nějaký Sats, abyste **vytvořili příchozí likviditu** na druhém konci spojení kanálu. Chcete-li si ověřit, zda můžete přijímat Sats a jaké množství Sats můžete přijímat, zaškrtněte v informacích o kanálu pole **Můžete přijímat**. To vám ukáže, kolik Sats přijímáte v každém okamžiku.


Nyní předpokládejme, že jste z kanálu odeslali několik zpráv Sats, nyní máte příchozí likviditu a můžete přijímat zprávy Sats.


Chcete-li přijímat prostřednictvím kanálu Lightning, musíte vygenerovat fakturu. Na rozdíl od Bitcoin on-chain, který používá adresy, síť Lightning používá faktury. Existují dvě cesty, jak vygenerovat fakturu v síti Valet.


#### MOŽNOST 1


👉 V dolní části domovské stránky klikněte na **Přijmout**, vyberte **Přijmout do Bleskové faktury**. Vyplňte částku, která má být na faktuře přijata, a klikněte na tlačítko **Ok**. Zkopírujte fakturu nebo sdílejte QR kód s plátcem.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### MOŽNOST 2


👉 Klikněte na fialovou kartu Blesk na domovské stránce wallet. Klepněte kamkoli na kanál a zobrazí se seznam možností. Vyberte možnost **Přijmout na kanál** a zadejte částku, kterou přijímáte (buď v Sats, nebo v dolarech). Při vyplňování faktury se také zobrazí, kolik Sats můžete přijmout (příchozí kapacita). Klikněte na tlačítko **Ok** a zkopírujte fakturu nebo sdílejte QR kód s plátcem.


![receive_to_channel](assets/en/028.webp)


**Pozor:** První možnost je univerzální volba, což znamená, že pokud máte více aktivních kanálů a použijete první možnost, systém automaticky vybere jeden z vašich kanálů pro příjem Sats.


V tomto případě je tedy nejlepší použít druhou možnost, pokud chcete přijímat Sats na určitý kanál.


### Vysvětlení možností vyskakovacího okna vašeho kanálu


Když klepnete na svůj kanál, zobrazí se následující pole možností:


![channel_pop_ups](assets/en/029.webp)


**SDÍLENÍ PODROBNOSTÍ O SVĚTELNÉM KANÁLU:** Umožňuje sdílet podrobnosti o kanálu, jako je ID vzdáleného partnera, ID místního kanálu, transakce financování, datum vytvoření atd.


**ZAVŘENÍ KANÁLU DO KABELKY:** Kanál blesku můžete zavřít, kdykoli budete chtít. Chcete-li kanál uzavřít, systém zkontroluje zůstatek Bitcoin, který máte na své vlastní straně kanálu (nezapomeňte na pole **"Can Send "**, známé také jako místní zůstatek), a pošle vám jej zpět. V systému Valet si můžete vybrat, kam chcete, aby byl tento zůstatek Bitcoin odeslán při uzavření kanálu. Takže **Zavřít kanál na wallet** je jedna z vašich dvou možností.


👉 Klikněte na tuto možnost a vyberte možnost **Bitcoin**. Bude zahájeno uzavírání kanálu a zůstatek vašeho kanálu Bitcoin bude odeslán zpět na adresu wallet on-chain.


![close_channel_to_wallet](assets/en/030.webp)


**ZAVŘÍT KANÁL NA ADDRESS:** Toto je druhá možnost uzavření kanálu. Po výběru této možnosti budete vyzváni k zadání adresy wallet, na kterou bude odeslán zůstatek Bitcoin na vašem kanálu. Upozorňujeme, že v této možnosti můžete naskenovat pouze QR kód adresy Bitcoin, na kterou chcete kanál uzavřít. V současné době není k dispozici možnost ručního vložení adresy.


👉 Klikněte na tuto možnost, naskenujte adresu Bitcoin a klikněte na **Ok**. Bude zahájeno uzavírání kanálu a na naskenovanou adresu bude odeslán váš zůstatek Lightning Bitcoin.


![scan_address_and_Ok](assets/en/031.webp)


**VYTVOŘENÍ KANÁLU:** Jedná se o stejnou věc jako při generování faktury, ale v některých případech můžete mít více než jeden kanál, včetně kanálů Fiat (jedinečný druh kanálu Lightning, který lze získat v zařízení Valet wallet). Pokud tedy máte otevřeno více kanálů, tato možnost zajistí, že můžete přijímat platby na konkrétní kanál.


**DOPLNIT Z JINÝCH KANÁLŮ:** Tato možnost je funkce, která umožňuje doplnit jeden kanál z jiných existujících kanálů. Například pokud máte 2 různé kanály Lightning (A a B) a zůstatek Bitcoin na kanálu A se vyčerpal, pomocí této možnosti můžete snadno a automaticky doplnit zůstatek kanálu A z kanálu B.


**PŘÍMÝ NEPŘÍJEMNÝ PŘÍJEM:** Jedná se také o možnost vygenerovat fakturu pro příjem platby, ale při použití této možnosti vám odesílatel platí přímo. To znamená, že platba nepřeskakuje přes různé uzly, než se k vám dostane, jako je tomu u běžné platby Lightning. Odesílatel tedy v podstatě ví, že platí právě vám, zná vaše ID kanálu atd. Tuto možnost lze často využít, pokud dostáváte platbu ze zdroje, kterému důvěřujete, a nepotřebujete zachovávat své soukromí.


## Hostované kanály a kanály Fiat


Stejně jako mnoho dalších modelů Bitcoin wallet je Valet jednoduchý, lehký model Bitcoin a Lightning wallet. Má však jedinečnou funkci Lightning, která jej odlišuje od většiny ostatních modelů Bitcoin wallet. Tato funkce se nazývá **Hosted and Fiat Channels**.


Kanály Fiat jsou typem implementace Lightning, která umožňuje snadné zapojení a používání sítě Lightning. Jedná se o správcovské řešení, které umožňuje plnou anonymitu, stejně jako u běžného kanálu Lightning. Technologie Fiat channels umožňuje také vytváření derivátů Bitcoin v síti Lightning. Příkladem může být to, že díky kanálům Fiat mohou obchodníci přijímat platby Bitcoin se stabilní hodnotou, aniž by se museli obávat volatility Bitcoin.


Současná implementace Fiat kanálů na Valet umožňuje vytvářet stabilní syntetické Fiat měny kryté Sats. Používá vztah hostitel-klient, kde hostitelem je jakýkoli uzel Lightning nabízející tuto službu a klientem je uživatel Valetu. Jedná se o custodial řešení, protože všechny Sats jsou na straně Hostitele; generování faktur, směrování torů a generování předobrazů však stále probíhá na straně klienta jako u běžného kanálu Lightning.


Otevření kanálu Fiat probíhá stejně jako otevření kanálu Lightning. Jediným podstatným rozdílem je, že v tomto případě nemusí klient (uživatel Valet) vázat žádnou likviditu on-chain pro vytvoření kapacity kanálu. Hostitel nastaví kapacitu kanálu a směruje všechny platby za klienta.


👉 Chcete-li otevřít kanál Fiat, klikněte na fialovou kartu **Blesk** na domovské stránce wallet. Vyberte možnost **Scan Node QR** (V tomto okamžiku musíte mít identifikovaného hostitele, ke kterému chcete otevřít kanál, a získat QR uzlu. Příkladem uzlu Hostitel, ke kterému můžete otevřít kanál Fiat, je uzel SATM u standardního Sats.)


**Upozornění:** Je důležité si uvědomit, že hostitelem se může stát kdokoli. Jediné, co potřebujete, je provozovat uzel Lightning se zásuvným modulem **Fiat channel** a službou **Hedging**. Fiat channels je open-source projekt společnosti *Standard Sats*. Přečtěte si o něm více [zde](https://github.com/standardsats/fiat-channels-rfc) a [zde](https://standardsats.github.io/).


SATM uzel QR níže:


![SATM_node_QR](assets/en/032.webp)


👉 Po naskenování QR uzlu klikněte na **Požádat o fiat kanál v USD** nebo **Požádat o fiat kanál v EUR** (v této nominální hodnotě budou vaše zůstatky ve Fiatu kótovány). Prozatím zvolte USD a klikněte na **OK**. Kanál se automaticky otevře a vy můžete ihned začít přijímat Sats. Vidíte, že je to tak jednoduché!!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉 Přejděte na domovskou stránku wallet a uvidíte **světle zelenou** kartu s označením **USD**, což je váš **Fiat kanál**.


![fiat_channel_card](assets/en/035.webp)


**Upozornění:** Když obdržíte Sats na kanálu Fiat, bude hodnota obdrženého Sats ve fiat uzamčena jako stabilní zůstatek, zatímco objem Sats se bude pohybovat podle ceny Bitcoin. Toto řešení bylo navrženo především pro obchodníky, kteří chtějí přijímat Sats k platbám, ale nechtějí čelit problémům s volatilitou Bitcoin. To jim pomáhá udržet stabilní hodnotu za všech okolností, a přitom mohou stále provádět transakce v síti Lightning a využívat globální dosah a rychlé vypořádání Bitcoin jako prostředku směny na Lightning Network.


Po vytvoření kanálu Fiat se zobrazí následující pole hodnot a jejich význam:


![fiat_channel_info](assets/en/036.webp)



- RANDOMNÍ SADA ČÍSEL ODDĚLENÝCH TEČKAMI:** Jedná se o IP adresy uzlů. (IPV4 a IPV6)
- CENA SERVERU:** Jedná se o tržní cenu Bitcoin, za kterou vám Hostitel nabízí služby. Tato cena se často mírně liší od převládající tržní ceny, protože Hostitel může přidat drobnou přirážku. O této sazbě rozhoduje výhradně Hostitel; proto se také bude u jednotlivých Hostitelů lišit.
- FIAT BALANCE:** Jedná se o uzamčenou stabilní hodnotu fiat každého satelitu, který na tomto kanálu obdržíte. Nezapomeňte, že jak bylo vysvětleno dříve, kdykoli na svém kanálu Fiat přijmete Sats, je v tomto poli okamžitě uzamčena fiat hodnota Sats v okamžiku příjmu jako syntetická stabilní fiat hodnota. Vaše hodnota **Fiat Balance** nekolísá s tržní cenou Bitcoin. Kdykoli chcete provést platbu z tohoto kanálu, můžete poslat pouze ekvivalent tohoto fiatového zůstatku Sats. Představte si to tedy jako digitální fiat měnu krytou měnou Sats.
- KAPACITA:** Jedná se o celkový objem Sats, který lze tímto kanálem odeslat a přijmout. (Tento údaj je rovněž nastaven Hostitelem. A na rozdíl od běžného kanálu Lightning může tuto kapacitu Hostitel případně upravit)
- MOŽNOST ODESLÁNÍ:** Jedná se o objem Sats, který můžete odeslat v každém bodě na základě vašeho zůstatku ve fiat. To je zcela odlišné od toho, co máte v běžném kanálu Lightning, protože tato hodnota se pohybuje s cenou Bitcoin. Proto to, co zde vidíte, je hodnota Sats vašeho fiatového zůstatku v každém okamžiku na základě **Serverového kurzu**.
- CAN RECEIVE:** Toto je počet Sats, které můžete v daném okamžiku na tomto kanálu přijímat. Po vytvoření kanálu by tato hodnota měla být stejná jako kapacita kanálu.
- VALUE IN FLIGHT:** Když někdo pošle na váš kanál nějaký sats nebo když se vy snažíte někomu poslat nějaký sats a z nějakého důvodu se transakce zpozdí, často se to zobrazí v tomto poli.


Zde jsou důležité informace o kanálech Fiat:



- Na rozdíl od běžného kanálu Lightning můžete po otevření kanálu fiat okamžitě začít přijímat zprávy Sats, ale nemůžete je odesílat. Odesílat Sats můžete až po přijetí Sats.
- Za všech okolností je aktivem odesílaným z a do Sats. Zůstatek *Fiat* je pouze syntetickou reprezentací IOU hodnoty Bitcoin přijaté v libovolném okamžiku. Nejedná se tedy o výtvor token ani o novou kryptoměnu.
- Kanál Fiat je užitečný především pro obchodníky/podniky, kteří jsou skeptičtí k přijímání plateb Bitcoin kvůli obavám z volatility. Může být také užitečný pro společnosti, které chtějí vyplácet mzdy svým zaměstnancům v Bitcoin, aniž by nesly důsledky volatility Bitcoin, která může způsobit nestabilitu jejich mzdového kapitálu. Může být užitečná i pro jednotlivce, kteří žijí v oblasti s převažujícím používáním Bitcoin, ale mají fixní životní náklady.
- Všimněte si, že zde není žádné pole označené jako **REFUNDABLE**. Je to proto, že technicky nelze kanál Fiat uzavřít. Kanál Fiat můžete přestat používat pouze tak, že jeho zůstatek odčerpáte do svého běžného kanálu Blesk.


### Vysvětlení možností vyskakovacího okna Fiat Channel


Po klepnutí na kanál Fiat Lightning se zobrazí následující pole:


![fiat_channel_pop_up](assets/en/037.webp)


**SDÍLENÍ PODROBNOSTÍ O HOSTOVANÉM KANÁLU:** Umožňuje sdílet podrobnosti o kanálu Fiat, jako je ID vzdáleného partnera, ID místního kanálu, datum vytvoření atd.


**EXPORTOVAT STAV KANÁLU:** Umožňuje exportovat stav kanálu v libovolném okamžiku. Obvykle je to užitečné při opravě chyb kanálu a Hostitel vás může požádat, abyste tento stav sdíleli, pokud je to potřeba.


**Vyčerpání zůstatku kanálu:** Jak již bylo zmíněno, kanál Fiat nelze technicky uzavřít, ale můžete vyčerpat zůstatek kanálu do stávajícího normálního kanálu Lightning. Tím se automaticky přesune ekvivalent zůstatku Fiatu do vašeho normálního kanálu Blesk.


**PŘIJMOUT DO KANÁLU:** Jedná se o stejnou věc jako při generování faktury, ale v některých případech může mít uživatel více než jeden kanál Fiat s různými Hostiteli, včetně běžných kanálů Lightning. Pokud má tedy uživatel otevřeno více kanálů, tato možnost zajistí, že může přijmout platbu na konkrétní kanál.


**DOPLNIT Z JINÝCH KANÁLŮ:** Tato možnost je funkce, která umožňuje uživateli doplnit jeden kanál z jiných existujících kanálů. Pomocí této možnosti tedy můžete doplnit svůj kanál Fiat z normálního kanálu nebo jiných kanálů Fiat, které máte, stejně jako byste mohli vypustit vodu.


**PŘÍMÝ NEPŘÍJEMNÝ PŘÍJEM:** Jedná se také o možnost vygenerovat fakturu pro příjem platby, ale při použití této možnosti vám odesílatel platí přímo. To znamená, že platba nepřeskakuje přes různé uzly, než se dostane k vám. Odesílatel tedy v podstatě ví, že platí právě vám, zná ID vašeho kanálu atd. Tuto možnost lze často použít, pokud přijímáte platbu ze zdroje, kterému důvěřujete, a nepotřebujete zachovávat své soukromí.


## Nastavení obsluhy:


Stejně jako každá jiná aplikace má i Valet nastavení aplikace, které si můžete upravit podle svého vkusu. Na stránku nastavení se dostanete z domovské obrazovky.


👉 Na domovské obrazovce klikněte na ikonu **Gear** v pravém horním rohu obrazovky a přejděte do nastavení. Níže jsou uvedeny součásti v sekci nastavení.


![settings_icon](assets/en/038.webp)


**MÍSTNÍ ZÁLOHOVÁNÍ KANÁLŮ JE ZAPNUTO:** Pokud je jinak **Zakázáno,** měli byste jej povolit, protože je to jediný způsob, jak můžete obnovit své normální kanály Lightning, pokud odinstalujete a znovu nainstalujete Valet. Vysvětlíme to později. Klikněte tedy na tuto možnost a dejte Valetu oprávnění k vašemu **úložiště médií**, protože právě tam je uložen soubor se zálohou.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**KAM ULOŽIT MÍSTNÍ ZÁLOHU:** Pokud jste Valetu udělili oprávnění k úložišti, bude toto pole automaticky nastaveno na ukládání místních záloh do složky **Stáhnuté soubory**. Můžete to však změnit kliknutím sem a výběrem libovolné složky podle vlastního výběru.


**Správa řetězových peněženek** Tohle je trochu technická záležitost a pokud nejste dostatečně zkušení, nemusíte se tím zabývat. Výchozí nastavení je zde v pořádku.


**PŘIDAT HARDWARE WALLET:** Tímto byste se také neměli zabývat, pokud nemáte hardwarové zařízení wallet, které chcete připojit a sledovat. Pomocí tohoto nastavení můžete skenovat a připojovat hardwarovou kartu wallet, například kartu Trezor nebo Cold, a sledovat její činnost. Jedná se o funkci pouze pro sledování, což znamená, že odtud nemůžete provádět transakce na hardwarové kartě wallet. Můžete pouze sledovat a monitorovat aktivity wallet, zůstatky atd.


**Nastavení vlastního uzlu ELECTRUM:** To je také technická záležitost a pokud nemáte dostatečné znalosti, neměli byste se tím zabývat. Výchozí nastavení je dostatečně dobré.


**BITCOIN UNITS:** Takto má být zobrazen zůstatek na účtu Bitcoin. První možnost zobrazí váš zůstatek v jednotkách Satoshi, např. 1 000 000 Sats, zatímco druhá možnost jej zobrazí v desetinných místech BTC. Např. 0,01BTC


**POUŽÍVAT AUTENTIZACI PINEM** Pokud toto políčko zaškrtnete, budete si muset nastavit PIN nebo otisk prstu, který musíte zadat pro přihlášení do wallet a ověřování transakcí.


**POUŽÍVAT PŘIPOJENÍ TOR:** Pokud toto políčko zaškrtnete, budou vaše transakce probíhat přes síť Tor. Přidává to další vrstvu soukromí, ale může to mít za následek zpoždění průchodnosti plateb, zejména u bleskových plateb.


**ZOBRAZIT Frázi pro obnovu BIP39:** Zde máte přístup ke své 12slovné frázi seed pro zálohování. Pokud jste si ji tedy předtím nezapsali nebo nemůžete najít, kam jste si ji zapsali, pokud máte stále přístup ke své hlášce Wallet, můžete si ji odsud zkopírovat.


**STATISTIKA POUŽITÍ:** Zobrazuje přehled všech vašich transakcí a aktivit od vytvoření wallet


![usage_stats](assets/en/041.webp)


## Obnova Wallet


Valet je neautorizovaná aplikace wallet, takže pokud zařízení ztratíte nebo aplikaci wallet odinstalujete, budete muset provést obnovení wallet, abyste získali zpět své kanály Bitcoin a Lightning. Na začátku tohoto návodu jsme se zmínili o důležitosti zapsání vaší **12slovné fráze seed**, protože ta je klíčem k obnovení vašeho zařízení wallet. Neexistují žádní zástupci zákaznické péče, kteří by vám pomohli dostat se zpět do vašeho zařízení wallet.


Pro obnovu zařízení Valet wallet jsou zapotřebí dva důležité nástroje v závislosti na tom, zda jste měli aktivní kanál Lightning, nebo ne. Uživatelům, kteří neměli aktivní běžný kanál Lightning, stačí jejich **12slovná fráze seed**, a to podle jednoduchých kroků uvedených níže:


👉 Nainstalujte novou aplikaci Valet a spusťte ji.


👉 Vyberte **Obnovit stávající Wallet**


![restore_existing_wallet](assets/en/042.webp)


👉 Vyberte **Pouze fráze pro obnovení**.


![select_recovery_phrase](assets/en/043.webp)


👉 Zadejte svou 12slovnou frázi pro obnovení a klikněte na **OK**.


![input_12_words](assets/en/044.webp)


Vaše zařízení wallet bude obnoveno. V tomto případě bude obnoven pouze váš zůstatek on-chain Bitcoin.


Pokud jste však měli aktivní normální kanál Blesk a obnovíte svůj kanál wallet pouze pomocí fráze pro obnovení, bude váš kanál Blesk násilně uzavřen a veškerý zůstatek Bitcoin, který na něm máte, bude automaticky odeslán na váš zůstatek on-chain.


Další možností, jak obnovit funkci Valet wallet, zejména pokud jste měli před odinstalováním funkce Valet otevřený normální kanál Lightning, je **použít místní záložní soubor uložený v zařízení spolu s frází seed o 12 slovech**. Pokud použijete tyto dvě položky, stav vašeho kanálu Lightning bude obnoven, a proto nebude váš kanál Lightning násilně uzavřen.


Zde jsou uvedeny následující kroky:


👉 Nainstalujte novou aplikaci Valet a spusťte ji.


👉 Vyberte možnost **Obnovit stávající Wallet**.


👉 Vyberte **Výraz pro zálohování + obnovení**.


![select_backup_and_recovery_seed](assets/en/045.webp)


👉 Ve správci souborů telefonu vyberte soubor Zálohování. (Ve výchozím nastavení je vždy uložen ve složce **Stažené soubory**.)


![local_backup_file_in_download_folder](assets/en/046.webp)


Po výběru správného záložního souboru se zobrazí výzva potvrzující, že je **"Záložní soubor přítomen "**, a poté budete vyzváni k zadání 12slovné fráze seed.


![enter_12_words](assets/en/047.webp)


👉 Zadejte 12slovnou frázi pro obnovení a klikněte na **OK**. Budete přesměrováni na domovskou stránku wallet.


👉 Počkejte, až se dokončí synchronizace sítě Bitcoin (**SYNC**) a synchronizace uzlů Lightning (**LN Sync**), a váš wallet bude plně obnoven, včetně kanálů Lightning.


![LN_sync](assets/en/048.webp)


## Závěr


Valet je zajímavé řešení wallet s funkcemi, které jsou vhodné pro zavádění nových uživatelů. Disponuje také Fiat kanálem, což je nepříliš nová technologie, která zajišťuje integraci podniků provozovaných fiatem na standardu Bitcoin.


Stáhněte si Valet ještě dnes a vyzkoušejte ho!!! 🧡