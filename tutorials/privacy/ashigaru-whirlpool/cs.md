---
name: Ashigaru - Whirlpool Coinjoin
description: Jak v aplikaci Ashigaru vytvořím coinjoiny?
---

![cover](assets/cover.webp)



"*Bitcoin wallet pro ulice*"



V tomto tutoriálu se dozvíte, co je to coinjoin a jak ho vytvořit pomocí aplikace Ashigaru Terminal a implementace Whirlpool, protokolu coinjoin zděděného z protokolu Samourai Wallet.



## Jak fungují klouby Whirlpool



V tomto tutoriálu se nebudu vracet k pojmu coinjoin, jeho užitečnosti ani k teoretickému fungování Whirlpool, protože tato témata jsou již podrobně vysvětlena v 5. díle vzdělávacího kurzu BTC 204 na Plan ₿ Academy. Pokud jste ještě nezvládli fungování Whirlpool nebo princip coinjoinu, důrazně doporučuji, abyste se před pokračováním seznámili s touto 5. částí :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Zde je však několik stručných faktů a čísel, které se vám mohou hodit.



Portfolio kompatibilní s Whirlpool využívá 4 samostatné účty, které vyhovují potřebám procesu coinjoin:




- Účet **Deposit** označený indexem `0'` ;
- Účet **Špatná banka** (nebo *doxxická směna*), označený indexem `2 147 483 644'` ;
- Účet **Premix** označený indexem `2 147 483 645'` ;
- Účet **Postmix** označený indexem `2 147 483 646`.



Na Ashigaru jsou v listopadu 2025 k dispozici dva bazény (tento seznam se bude v následujících měsících pravděpodobně vyvíjet: nezapomeňte si proto při čtení zkontrolovat hodnoty):




- 0.25 BTC`, přičemž vstupní poplatek činí `0,0125 BTC`;
- 0.025 BTC, přičemž vstupní poplatek činí 0,00125 BTC.



Každý směšovací cyklus může zahrnovat 5 až 10 UTXO na vstupu a výstupu.



![Image](assets/fr/01.webp)



## Požadavky na software



Pro vytváření spojů s mincemi pomocí programu Whirlpool budete potřebovat tři samostatné programy:





- Ashigaru Terminal**, který vám umožní spravovat vaše coinjoiny přímo z počítače;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, aplikace ve vašem chytrém telefonu, pomocí které můžete utrácet bitcoiny v *postmixu* odkudkoli;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, implementace uzlu Bitcoin zaručující suverénní připojení k síti bez závislosti na serveru třetí strany.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Nainstalujte si každý z těchto nástrojů podle příslušných návodů a pak můžete začít vytvářet první spojení mincí.



## Přijímání bitcoinů



Po vytvoření portfolia začnete s jediným účtem označeným indexem `0`. Jedná se o účet `Deposit`. Právě na tento účet budete posílat bitcoiny určené pro coinjoins. Můžete je přijímat buď prostřednictvím aplikace Ashigaru (viz 5. část specializovaného tutoriálu), nebo prostřednictvím terminálu Ashigaru (rovněž podrobně popsáno v 5. části specializovaného tutoriálu).



Jakmile na vašem vkladovém účtu bude alespoň částka potřebná k účasti v nejmenším poolu (plus poplatky za služby a minimum potřebné k pokrytí nákladů na mining), budete připraveni zahájit první spojení s mincemi.



![Image](assets/fr/02.webp)



## Vytvořte Tx0



Po připsání peněz na váš vkladový účet a potvrzení transakce můžete zahájit proces připojení mince. To provedete tak, že v terminálu Ashigaru otevřete nabídku `Peněženky` a vyberete svůj wallet. Pokud je váš wallet uzamčen, software vás požádá o zadání hesla a passphrase.



![Image](assets/fr/03.webp)



Poté vyberte účet `Vklad`.



![Image](assets/fr/04.webp)



Přejděte do nabídky `UTXOs`.



![Image](assets/fr/05.webp)



Zde uvidíte seznam všech UTXO na svém vkladovém účtu. Vyberte ty, které chcete odeslat v cyklech coinjoin.



Pro větší důvěrnost a pro zamezení *Common Input Ownership Heuristic (CIOH)* se doporučuje používat pouze jeden UTXO na jeden vstup v Whirlpool (podrobné vysvětlení této zásady naleznete v BTC 204).



Stisknutím klávesy `ENTER` na klávesnici vyberte položku UTXO: vedle ní se zobrazí hvězdička `(*)`, která označuje, že je vybrána.



![Image](assets/fr/06.webp)



Poté klikněte na tlačítko `Mix Selected`.



![Image](assets/fr/07.webp)



Pokud máte zařízení UTXO dostatečně velké, abyste se mohli zapojit do jednoho ze dvou dostupných fondů, můžete cílový fond vybrat pomocí šipek. Na této stránce se zobrazí podrobnosti o vašem Tx0 :




- počet UTXO, které vstoupí do fondu;
- různé uplatňované poplatky (poplatky za služby a poplatky mining) ;
- výši *doxické změny*.



Pečlivě zkontrolujte informace a kliknutím na `Broadcast` začněte vysílat Tx0.



![Image](assets/fr/08.webp)



Ashigaru poté zobrazí TXID vašeho Tx0 a potvrdí, že transakce byla v síti odvysílána.



![Image](assets/fr/09.webp)



## Vytváření spojů coinjoins



Po odvysílání Tx0 se vraťte na domovskou stránku svého vkladového účtu, klikněte na `Účty` a vyberte účet `Premix`.



![Image](assets/fr/10.webp)



V nabídce `UTXOs` uvidíte různé vyrovnané části, které jsou připraveny ke vstupu do cyklů coinjoin. Jakmile potvrdíte Tx0, terminál Ashigaru automaticky zahájí svůj první cyklus míchání.



![Image](assets/fr/11.webp)



Po potvrzení Tx0 bude terminálem Ashigaru automaticky vytvořena a odeslána první transakce coinjoin. Přejdete-li na `Účty > Postmix > UTXO`, můžete si prohlédnout své vyrovnané UTXO, které čekají na potvrzení svého prvního cyklu.



![Image](assets/fr/12.webp)



Nyní můžete nechat Ashigaru Terminal běžet na pozadí: bude pokračovat v automatickém mixování a remixování vašich skladeb.



## Dokončování spojů mincí



Nyní můžete nechat své mince automaticky remixovat. Model Whirlpool znamená, že za remixování neplatíte žádné další poplatky: žádné servisní poplatky, žádné poplatky mining. Nechat své mince účastnit se více cyklů míchání tak může vaší důvěrnosti jen prospět.



Pro lepší pochopení tohoto mechanismu a toho, na kolik cyklů se vyplatí čekat, doporučuji přečíst si tento článek:



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Chcete-li zobrazit počet remixů provedených jednotlivými skladbami, otevřete nabídku `UTXOs` v účtu `Postmix`.



![Image](assets/fr/13.webp)



Chcete-li utratit smíšené mince, přejděte do aplikace Ashigaru, která používá stejný software wallet jako software Ashigaru Terminal. Číslo wallet zobrazené při otevření odpovídá vašemu účtu `Vklad`. Pro přístup k účtu `Postmix`, který obsahuje vaše smíšené UTXO, klikněte na symbol Whirlpool v pravém horním rohu.



![Image](assets/fr/14.webp)



Na tomto účtu uvidíte všechny své mince, které jsou aktuálně smíšené. Chcete-li je utratit, stiskněte symbol `+` v pravém dolním rohu obrazovky a poté vyberte možnost `Poslat`.



![Image](assets/fr/15.webp)



Vyplňte podrobnosti o transakci: adresu příjemce, částku, která má být odeslána, a pokud chcete, zvolte si specifickou strukturu transakce, abyste ještě více zvýšili důvěrnost (viz příslušné výukové programy).



![Image](assets/fr/16.webp)



Pečlivě zkontrolujte podrobnosti transakce a poté přetažením šipky v dolní části obrazovky potvrďte odeslání.



![Image](assets/fr/17.webp)



Vaše transakce byla podepsána a odvysílána v síti Bitcoin.



![Image](assets/fr/18.webp)



## Utratit Doxxic Change



Nezapomeňte: Model Whirlpool je založen na vyrovnání vašich dílků na Tx0, před jejich vstupem do bazénů. Právě tento mechanismus narušuje sledování UTXO. Podle mého názoru je to nejefektivnější model spojování mincí, ale má jednu nevýhodu: generuje *změnu*, která neprochází procesem spojování mincí.



Tato změna odpovídá vytvoření UTXO pro každý Tx0. Je izolována ve zvláštním účtu s názvem `Doxická změna` nebo `Špatná banka`, v závislosti na softwaru, aby se zabránilo jejímu použití s ostatními UTXO. To je velmi důležité, protože tyto UTXO nebyly smíchány: jejich sledovací vazby zůstávají neporušené a mohou ohrozit vaši důvěrnost tím, že vytvoří spojení mezi vámi a vaší aktivitou coinjoin. Zacházejte s nimi proto opatrně a **nikdy je nepoužívejte s jinými UTXO**, ať už smíšenými, nebo ne. Kombinace toxického UTXO-25 se smíšeným UTXO-25 vymaže všechny výhody v oblasti ochrany soukromí, které jste získali díky coinjoinu.



Ashigaru prozatím nenabízí přímý přístup k tomuto účtu `Doxxic Change` (alespoň já jsem ho nenašel). Tato funkce bude pravděpodobně přidána v některé z budoucích aktualizací. Do té doby je jediným způsobem, jak tyto prostředky získat, importovat svůj seed do Sparrow Wallet. Ten obvykle automaticky zjistí, že se jedná o wallet používaný s Whirlpool, a umožní vám přístup ke všem čtyřem účtům, včetně účtu `Doxxic Change`. Tyto UTXO pak můžete utratit jako běžné bitcoiny z Sparrow.



Zde je několik možných strategií, jak spravovat své devizové UTXO z coinjoins, aniž byste ohrozili své soukromí:





- Míchání do menších bazénů:** Pokud je váš toxický UTXO dostatečně velký, aby se mohl připojit k menšímu bazénu, je to obecně nejlepší možnost. Dávejte si však pozor, abyste za tímto účelem nikdy neslučovali několik toxických UTXO, protože tím vznikne spojení mezi vašimi různými záznamy v Whirlpool.





- Označte je jako neutratitelné:** Dalším rozumným přístupem je jednoduše je ponechat tak, jak jsou, na jejich samostatném účtu a ponechat je nedotčené. Tím zabráníte jejich náhodnému utracení. Pokud se hodnota bitcoinů zvýší, mohly by být otevřeny nové pooly přizpůsobené jejich velikosti.





- Poskytování darů:** Tyto toxické UTXO můžete proměnit v dary vývojářům Bitcoin, open-source projektům nebo asociacím, které přijímají BTC. To vám umožní se jich užitečně zbavit a zároveň podpořit ekosystém.





- Koupit předplacené dárkové karty nebo karty Visa:** Platformy jako [Bitrefill](https://www.bitrefill.com/) umožňují vyměnit bitcoiny za dárkové karty nebo dobíjecí karty Visa, které lze použít v obchodech. To může být jednoduchý a diskrétní způsob, jak utratit toxické UTXO.





- Vyměňte je za Monero:** Samourai Wallet nabízela dnes již nefunkční službu výměny BTC/XMR. Pokud podobná služba existuje (osobně o žádné nevím), je to výborné řešení pro izolaci těchto UTXO, jejich konverzi na Monero a následné odeslání zpět na Bitcoin. Tato metoda však byla drahá a závislá na dostupné likviditě.





- Převést je na Lightning Network:** Převod těchto UTXO na Lightning Network, abyste mohli využívat snížené transakční poplatky, je potenciálně zajímavou možností. Tato metoda však může odhalit určité informace v závislosti na používání Lightningu, a proto by měla být používána s opatrností.



## Jak se mohu informovat o kvalitě našich cyklů coinjoin?



Má-li být coinjoin skutečně účinný, musí vykazovat vysoký stupeň jednotnosti mezi vstupními a výstupními částkami. Tato jednotnost zvyšuje počet možných interpretací pro vnějšího pozorovatele, což zase zvyšuje nejistotu ohledně transakce. K měření této nejistoty používáme koncept entropie aplikovaný na transakci. Model Whirlpool je v tomto ohledu uznáván jako jeden z nejefektivnějších, neboť zaručuje vynikající homogenitu mezi účastníky. Pro podrobnější seznámení s tímto principem doporučuji nahlédnout do poslední kapitoly 5. části vzdělávacího kurzu BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Výkonnost několika cyklů coinjoin se měří podle velikosti množin, v nichž je mince ukryta. Tyto množiny definují takzvané *anonsety*. Existují dva typy: první měří důvěrnost vůči retrospektivní analýze (ze současnosti do minulosti) a druhý měří odolnost vůči prospektivní analýze (z minulosti do současnosti). Úplné vysvětlení těchto dvou ukazatelů naleznete v následujícím tutoriálu (nebo opět ve školení BTC 204):



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Jak spravovat postmix?



Po provedení několika cyklů spojování mincí je nejlepší strategií ponechat si UTXO na účtu `Postmix` a nechat je remixovat neomezeně dlouho, dokud je opravdu nebudete potřebovat utratit.



Někteří uživatelé dávají přednost převodu svých smíšených bitcoinů na wallet, který je zabezpečen hardwarem wallet. Tato možnost je možná, ale vyžaduje určitou přísnost, aby nebyla ohrožena důvěrnost získaná pomocí coinjoins.



Nejčastější chybou je slučování UTXO. Je důležité nikdy neslučovat smíšené UTXO s nesmíšenými UTXO ve stejné transakci, jinak hrozí spuštění *Common Input Ownership Heuristic (CIOH)*. To předpokládá důslednou správu UTXO, zejména prostřednictvím jasného a přesného označování. Obecně řečeno, slučování UTXO je špatná praxe, která při špatné správě často vede ke ztrátě důvěrnosti.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Opatrní byste měli být také při konsolidaci smíšených UTXO. Omezené konsolidace lze zvážit, pokud mají UTXO významné anonce, ale nevyhnutelně snižují úroveň vaší důvěrnosti. Vyhněte se masivním nebo uspěchaným konsolidacím, prováděným před dostatečným počtem remixů, protože by mohly vytvořit inferenční vazby mezi vašimi kusy před a po mixu. V případě pochybností je nejlepší nekonsolidovat postmixové UTXO a přenášet je po jednom do hardwaru wallet a pokaždé generovat novou prázdnou adresu příjmu. Nezapomeňte označit každý přenášený modul UTXO.



Důrazně nedoporučujeme přesouvat postmixové UTXO do portfolií pomocí minoritních skriptů. Pokud jste se například účastnili Whirlpool z portfolia multi-sig v `P2WSH`, bude vás málo, kteří sdílíte tento typ skriptu. Odesláním svých postmixových UTXO do stejného typu skriptu výrazně snížíte svou anonymitu. Kromě typu skriptu mohou vaši důvěrnost ohrozit i další specifické otisky wallet, takže nejlepší je utratit je z aplikace Ashigaru.



A konečně, stejně jako u všech transakcí Bitcoin, nikdy nepoužívejte adresu příjemce opakovaně. Každá platba musí být zaslána na novou, jedinečnou, prázdnou adresu.



Nejjednodušší a nejbezpečnější metodou je nechat smíchané UTXO odpočívat na účtu `Postmix`, nechat je přirozeně remixovat a utrácet je pouze v případě potřeby z Ashigaru.



Peněženky Ashigaru a Sparrow obsahují dodatečná ochranná opatření proti nejčastějším chybám spojeným s analýzou blockchainu, která vám pomohou zachovat důvěrnost vašich transakcí.