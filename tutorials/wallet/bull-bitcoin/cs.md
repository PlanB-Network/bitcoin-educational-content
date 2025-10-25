---
name: Bull Bitcoin Wallet
description: Zjistěte, jak používat Wallet Bull Bitcoin
---

![cover](assets/cover.webp)



Tato příručka vás seznámí s instalací, konfigurací a používáním zařízení Bull Bitcoin Mobile. Dozvíte se, jak přijímat a odesílat finanční prostředky ve třech sítích: Onchain, Liquid a Lightning a jak přenášet svůj Bitcoin z jedné sítě do druhé. Přílohy poskytují zdroje a kontakty, základní informace a stručná vysvětlení technických pojmů.



## Úvod



**Bull Bitcoin Mobile**, vyvinutý společností **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([create account](https://app.bullbitcoin.com/registration/orangepeel)), je **samostatný** Bitcoin Wallet, což znamená, že máte plnou kontrolu nad svými soukromými klíči, a tedy i nad svými prostředky, aniž byste byli závislí na třetí straně. Tento Wallet s otevřeným zdrojovým kódem a s kořeny ve filozofii Cypherpunk v sobě spojuje jednoduchost, důvěrnost a pokročilé funkce, jako je výměna mezi sítěmi a podpora PayJoin. Umožňuje spravovat vaše bitcoiny ve třech sítích: **Bitcoin onchain**, **Liquid** a **Lightning**, přičemž každá z nich je přizpůsobena specifickému použití.



### Kontext rozvoje



Wallet reaguje na velkou výzvu: Síťové poplatky Bitcoin jsou nevhodné pro malé platby nebo pro otevření malých samostatných kanálů Lightning. Wallet Bull Bitcoin Mobile nabízí samoobslužné řešení, přičemž se spoléhá na 3 hlavní sítě Bitcoin:





- **Síť Bitcoin (onchain)**: Ideální pro střednědobé až dlouhodobé ukládání UTXO a transakcí velké hodnoty, kde jsou poplatky poměrně zanedbatelné.
- **Liquid Network**: Navrženo pro rychlé (~2 minuty), důvěrnější (skryté částky) a levné transakce, ideální pro shromažďování malých částek nebo ochranu soukromí.
- **Síť Lightning**: Optimalizovaná pro okamžité a levné platby, vhodná pro každodenní transakce malé až střední hodnoty.



Například u mobilního telefonu Bull Bitcoin můžete v portfoliu **Liquid** nebo **Lightning** akumulovat malé částky a poté, jakmile dosáhnete významné částky, můžete :





- Převod do sítě onchain pro bezpečné střednědobé nebo dlouhodobé uložení s vyšší důvěrností díky Liquid a/nebo Lightning upstream a s poplatky onchain za jednu transakci



### Průběžný vývoj



Aplikace Wallet se neustále vyvíjí, takže se nedivte, pokud mezi tímto návodem a vaší aktuální aplikací najdete nesrovnalosti.




- Například od 19.7.2025 jsou tlačítka **"Koupit / Prodat / Zaplatit "** v aplikaci viditelná, ale šedá, protože tyto možnosti, které jsou k dispozici na Exchange [bullbitcoin.com](https://app.bullbitcoin.com/registration/orangepeel), budou brzy integrovány pro jednotné prostředí. Jejich použití zůstane zcela volitelné. Probíhá nebo se plánuje mnoho dalších změn: správa více Wallet, passphrase, kompatibilita s hardwarovými peněženkami...
- Na [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49) se můžete podívat na aktuální témata a nadcházející vývoj. Jelikož je projekt 100% open-source a "built in public", můžete nám také posílat své návrhy a případné chyby, na které narazíte.




## 1. Předpoklady



Než začnete používat **Bull Bitcoin Mobile**, ujistěte se, že máte následující položky:





- **Kompatibilní smartphone**: Zařízení se systémem **iOS** (iPhone nebo iPad) nebo **Android**
- Připojení k internetu
- **Zabezpečená zálohovací média**: Napište si **obnovovací frázi** (12 slov) na papír nebo kov a uložte ji na bezpečném místě.
- **Základní znalosti**: V tomto návodu jsou vysvětleny jednotlivé kroky pro začátečníky.



## 2. Instalace





- Stáhněte si **aplikaci**:
- [Obchod Google Play](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share) **Stáhněte si z obchodu s aplikacemi pro zařízení se systémem Android**
- [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) **Stáhněte si APK pro zařízení se systémem Android přímo**
- [iOS](https://testflight.apple.com/join/FJbE4JPN) **Stáhnout přes TestFlight pro zařízení Apple**
 - Zkontrolujte jméno vývojáře (Bull Bitcoin), abyste se vyhnuli podvodným aplikacím.
 - Ujistěte se, že stažená verze odpovídá nejnovější stabilní verzi uvedené na GitHubu.
 - Bull Bitcoin Mobile je **open-source**. Pro zobrazení kódu: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- Instalace aplikace




## 3. Počáteční konfigurace



### 3.1 Spusťte aplikaci :



Aplikace používá pro obě portfolia jedinečnou frázi pro obnovu o 12 slovech:




- **gW-26' Wallet**: Pro transakce v síti Bitcoin (onchain)
- **okamžité platby Wallet**: Pro okamžité transakce v sítích Liquid a Lightning



Po otevření se zobrazí výzva k importu existující fráze pro obnovení nebo k vytvoření nové fráze Wallet :



![image](assets/fr/02.webp)



### 3.2 Fráze pro obnovu :



Chcete-li znovu použít existující kód Wallet, klikněte na "**Recover Wallet**" a vyplňte 12 slov své fráze pro obnovení.



V opačném případě klikněte na "**Vytvořit nový Wallet**" :




- S maximální pečlivostí si zapište frázi o zotavení. Zapište si ji na papír nebo kov a uložte ji na bezpečném místě (bezpečnostní schránka, offline místo). Tato fráze je vaším jediným prostředkem pro přístup k bitcoinům v případě ztráty zařízení nebo vymazání aplikace.
- Je také důležité si uvědomit, že kdokoli s touto frází může ukrást všechny vaše bitcoiny. Nikdy je neukládejte digitálně:
 - Žádný snímek obrazovky
 - Žádné zálohování do cloudu, e-mailu nebo zpráv
 - Žádné kopírování/vkládání (riziko uložení do schránky)



**! Tento bod je rozhodující**. Další pomoc :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Zajištění přístupu :





- Přejděte do nastavení a klikněte na **PIN kód**.
- Nastavte robustní kód **PIN** pro ochranu přístupu k aplikaci.
- Tento krok je nepovinný, ale důrazně jej doporučujeme, abyste zabránili tomu, že se k vašemu telefonu Wallet dostane kdokoli, kdo k němu má přístup.



![image](assets/fr/03.webp)



### 3.4 Připojení k osobnímu uzlu (volitelné):



BullBitcoin Wallet se ve výchozím nastavení připojuje k serverům Electrum: prvnímu, který spravuje Bull Bitcoin, a sekundárnímu serveru od společnosti Blockstream, přičemž u obou se předpokládá, že nevedou žádné protokoly, což snižuje riziko sledování.



Pro větší důvěrnost můžete aplikaci připojit k vlastnímu uzlu Bitcoin prostřednictvím serveru Electrum (pokyny jsou k dispozici na [BullBitcoin's GitHub](https://github.com/orgs/SatoshiPortal/projects/49) ).




## 4. Přijímání finančních prostředků



Příjem peněz pomocí **Bull Bitcoin Mobile** je jednoduchý a přizpůsobený vašim potřebám, ať už používáte :




  - síť **Bitcoin (onchain)** pro dlouhodobé zachování,
  - síť **Liquid** pro rychlejší a rychlejší Confidential Transactions,
  - síť **Lightning** pro okamžité platby s nízkou hodnotou.



Aplikace automaticky generuje adresy Lightning reception nebo Invoice v závislosti na zvolené síti. Zde je uveden postup pro jednotlivé sítě.



### 4.1. onchain (síť Bitcoin)



Na domovské obrazovce můžete :




- nebo vyberte **Secure Bitcoin Wallet** a poté klikněte na "**Přijmout "** :



![image](assets/fr/04.webp)





- nebo klikněte na "**Příjem "** a poté vyberte síť **Bitcoin**:



![image](assets/fr/05.webp)



#### 4.1.1. Možnost "Pouze kopírování nebo skenování Address" je vypnutá (výchozí)



![image](assets/fr/06.webp)





- Tím získáte přístup k volitelným pokročilým parametrům. Můžete zadat :
 - **částku** v BTC, Sats nebo fiat.
 - **osobní poznámka**, která bude součástí kopie URI / QR kódu.
 - Aktivace funkce **PayJoin** (podrobnosti viz dodatek 3), která zvyšuje důvěrnost kombinací záznamů odesílatele a příjemce.





- Příklad automaticky generovaného **URI**:



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- **Použití**: Zkopírujte URI a sdílejte jej s odesílatelem nebo jej nechte naskenovat QR kód.



#### 4.1.2. Možnost "Kopírovat nebo skenovat pouze Address" je povolena



![image](assets/fr/07.webp)





- Pokud je povolena možnost **"Kopírovat nebo skenovat pouze Address"**, aplikace vygeneruje jednoduchý soubor Bitcoin Address ve formátu SegWit (bech32).





- Příklad:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



I když zadáte částku nebo poznámku, nebudou zahrnuty do QR kódu ani do kopie Address





- **Použití**: Zkopírujte kód Address a sdílejte jej s odesílatelem nebo jej nechte naskenovat kód QR.



#### 4.1.3. Generování nového Address





- Proč používat pro každou transakci nový modul Address? Tím **chráníte své soukromí**, protože zabráníte propojení více plateb se stejným Address a omezíte možnosti sledování na Blockchain.
- Ve výchozím nastavení Bull Bitcoin automaticky generuje nepoužívaný Address.
 - Vytvoření nové jednotky Address si můžete vynutit kliknutím na **"Nová jednotka Address"** v dolní části obrazovky.
 - Všechny vaše adresy jsou propojeny s vaší větou seed: bez ohledu na to, kolik adres používáte, vaše portfolio bude zobrazovat jediný zůstatek a může automaticky konsolidovat prostředky při odeslání zásilky.





- Tip: Vždy používejte nový **Address** poskytovaný společností Bull Bitcoin, pokud nemáte specifickou potřebu (např. veřejný Address pro příjem darů).



### 4.2. Liquid



Na domovské obrazovce můžete :




- nebo vyberte **Instantní platby Wallet** a poté klikněte na **"Přijmout "** a poté na **"Liquid"** :



![image](assets/fr/08.webp)





- nebo klikněte na "**Příjem "** a poté vyberte síť **Liquid**:



![image](assets/fr/09.webp)



Jakmile se ocitnete na obrazovce **"Příjem "**, zkopírujte Liquid Address:





- Žádná částka ani poznámka. Příklad:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- Nebo zadáním **částky** (v BTC, Sats nebo fiat) a/nebo **osobní poznámky**, která bude součástí kopie URI / QR kódu. Příklad:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Použití**: Zkopírujte kód Address/URI a sdílejte jej s odesílatelem nebo jej nechte naskenovat QR kód.



### 4.3. Blesk



Na domovské obrazovce můžete :




- nebo vyberte **Instantní platby Wallet** a poté klikněte na "**Přijmout "** :



![image](assets/fr/10.webp)





- nebo klikněte na možnost "**Příjem "** a poté vyberte síť **Lightning**:



![image](assets/fr/11.webp)



#### 4.3.1. Provoz, omezení a výhody





- **Mechanismus**: Wallet umožňuje provádět a přijímat platby prostřednictvím Lightning. Prostředky přijaté prostřednictvím Lightning jsou uloženy v síti **Liquid** (v Wallet Instant Payments) díky automatické výměně prostřednictvím **Boltz**. To vám dává možnost komunikovat s Lightning, aniž byste museli spravovat kanály likvidity, a přitom zůstat ve vlastní úschově.





- **Limity:**
- **Minimální částka** 100 satoši (k 19. 7. 2025) při použití generate a Invoice.
- **Náklady**, které se odečtou od odeslané částky, platíte vy, na rozdíl od přijímání pomocí Wallet Lightning native, kde náklady na převod hradí kromě odeslané částky pouze odesílatel. Ke dni 19. 7. 2025 se od odeslané částky odečítá 47 Sats.





- **Výhody**:
- **Samostatné opatrovnictví**: Vaše finanční prostředky zůstávají pod vaší kontrolou a jsou uloženy na Liquid Network.
- **Žádné vysoké poplatky za řetězec**: Úložiště Liquid umožňuje vyhnout se nákladným vkladům v řetězci, abyste mohli otevřít svůj kanál Lightning nebo přidat likviditu. Tyto operace lze provést později, až částka nahromaděná na Liquid ospravedlní poplatky.





- **Tip:** Pokud má odesílatel Wallet Bull Bitcoin, použijte přímo Liquid Network, abyste se vyhnuli poplatkům za výměnu



#### 4.3.2. generate Invoice





- Zadejte **částku** (v BTC, Sats nebo fiat)





- Přidejte **osobní poznámku**, která bude začleněna do Invoice. Pokud odesílatel uhradí částku Invoice, vaše Wallet ji rovněž zahrne do údajů o transakci.





- Platnost Invoice: Blesk Invoice je platný **12 hodin**. Po uplynutí této doby pozbývá platnosti a nelze ji již zaplatit. Je třeba vygenerovat nový Invoice.





- **Použití**: Zkopírujte kód Invoice a sdílejte ho s odesílatelem nebo ho nechte naskenovat kód QR.




## 5. Zasílání finančních prostředků



### 5.1. Základní princip



Buď z domovské stránky, nebo z peněženek :



![image](assets/fr/12.webp)



pro přístup k obrazovce odeslání:



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** usnadňuje posílání peněz tím, že automaticky detekuje síť (Bitcoin, Liquid nebo Lightning) na základě zadaného kódu Address nebo Invoice (zkopírovaného nebo naskenovaného pomocí QR kódu).



### 5.2. řetězový přenos (síť Bitcoin)



#### 5.2.1. Odesílací obrazovka



**Akce**: Zadejte nebo naskenujte řetězec Bitcoin onchain Address





- Pokud částka nebyla definována, například :



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- Poté můžete na obrazovce odeslání vybrat :
 - Částka v BTC, sat nebo fiat. Minimální částka: 546 satoshis k 22/07/2025.
 - Nepovinná poznámka k identifikaci transakce. Viditelná pouze pro vás v podrobnostech transakce.



![image](assets/fr/14.webp)





- Pokud již byla částka definována, například :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Poté budete přesměrováni přímo na níže uvedenou potvrzovací obrazovku.



#### 5.2.2 Potvrzovací obrazovka



Věnujte čas kontrole všech parametrů, zejména částky, destinace Address a poplatků.


Poté můžete upravit parametry:



![image](assets/fr/15.webp)




- **Poplatky**: Můžete si vybrat:
- Odhadne se buď **rychlost provedení** vaší transakce, nebo související poplatky
- Odhadne se buď výše **poplatků** v režimu absolutních poplatků (celkové poplatky v satoši), nebo relativních poplatků (poplatky za bajt) a rychlost transakce





- **Rozšířená nastavení**:





- **Replace-by-fee (RBF)**: Tato funkce je aktivována ve výchozím nastavení a urychluje transakci zaplacením vyššího poplatku (podrobnosti viz příloha 4).





- **Ruční výběr UTXO**: Pokud jsou vaše finanční prostředky uloženy na několika různých adresách Wallet, můžete si vybrat adresy, ze kterých chcete finanční prostředky odeslat. Proč byste to měli udělat? S rostoucím používáním systému Bitcoin se zvyšují poplatky za převody. Odesílání z několika adres s malými částkami je dražší než odesílání z jediné adresy Address, ale když to uděláte nyní, vyhnete se tomu, že to budete muset udělat později, kdy budou poplatky ještě vyšší. Tomuto postupu se říká **konsolidace UTXO**.



![image](assets/fr/16.webp)





- **Odesílání pomocí PayJoin**: Pokud byla funkce aktivována příjemcem, který zadal URI, např. :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Poté Bull Bitcoin Mobile nakonfiguruje odesílání kombinací vašich UTXO s UTXO příjemce jako vstup, čímž se zlepší důvěrnost (podrobnosti viz Příloha 3).



### 5.3. Odeslat do Liquid



#### 5.3.1 Obrazovka odeslání



Síť **Liquid** umožňuje rychlé transakce (~2 minuty díky jednomu bloku za minutu), důvěrnější (maskované částky) než v síti onchain a s velmi nízkými poplatky. Prostředky jsou vybírány z **Instant Payments Wallet**.



**Akce**: Zadejte nebo naskenujte Liquid Address





- Pokud částka nebyla definována, například :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



Poté můžete na obrazovce odeslání vybrat :




- Částka v BTC, sat nebo fiat. Žádné minimum, 1 Satoshi možné;
- Nepovinná poznámka k identifikaci transakce. Viditelná pouze pro vás v podrobnostech transakce.



![image](assets/fr/17.webp)





- Pokud již byla částka definována, například :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



Poté budete přesměrováni přímo na níže uvedenou potvrzovací obrazovku.



#### 5.3.2 Potvrzovací obrazovka



Věnujte čas kontrole všech parametrů, zejména množství a místa určení Address.



![image](assets/fr/18.webp)





- **Poplatky**: Proporcionálně podle složitosti transakce, obvykle na bázi 0,1 sat/vB, tj. 20-40 satoshis za jednoduchou transakci (33 Sats k 22.7.2025).



### 5.4. Odeslat do aplikace Lightning



#### 5.4.1 Obrazovka odeslání



Síť **Lightning** umožňuje okamžité a levné platby malých částek, což je ideální pro drobné každodenní transakce.



**Akce**: Zadejte nebo naskenujte blesk Invoice





- Pokud naskenujete LN-URL Address, který umožňuje nastavit množství


Příklad: `orangepeel@walletofsatoshi.com`.


pak můžete na obrazovce odeslání vybrat :




 - Částka v BTC, sat nebo fiat. Minimální částka 1000 satoshis k 23/07/2025
 - Nepovinná poznámka k identifikaci transakce. Bude zaslána příjemci.



![image](assets/fr/19.webp)





- Pokud naskenujete blesk Invoice, který obsahuje definované množství


Příklad:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



Poté budete přesměrováni přímo na níže uvedenou potvrzovací obrazovku.



Poznámka: částka musí být vyšší než 21 Sats ke dni 23.7.2025



#### 5.4.2 Provoz, omezení a výhody





- **Mechanismus**: Prostředky jsou čerpány z **Instant Payments Wallet** (Liquid) a převedeny prostřednictvím swapu **Liquid → Lightning** s **Boltz**.





- **Limity:**
- **Minimální množství** vyšší než u nativního blesku Wallet (viz výše)
- **Výdaje** plus Liquid → Výměna blesků přes Boltz





- **Výhody**:
- **Samostatné opatrovnictví**: Vaše finanční prostředky zůstávají pod vaší kontrolou, jsou uloženy na Liquid Network a v případě potřeby je lze převést prostřednictvím Lightningu
- **Žádné vysoké poplatky za řetězec**: Uložení na Liquid vám ušetřilo nákladné onchain vklady za otevření Lightning kanálu nebo přidání likvidity. Tyto operace můžete provést později, až částka nashromážděná na Liquid ospravedlní poplatky.





- **Tip:** Pokud má příjemce Wallet Bull Bitcoin, použijte přímo Liquid Network, abyste se vyhnuli nákladům na výměnu



#### 5.3.3 Potvrzovací obrazovka



Věnujte čas kontrole všech parametrů, zejména množství a místa určení Address.



![image](assets/fr/20.webp)




## 6. Zobrazit historii



**Bull Bitcoin Mobile** umožňuje snadno sledovat transakce v sítích **Bitcoin (onchain)**, **Liquid** a **Lightning**. Historie je přístupná dvěma způsoby a zobrazuje podrobné informace pro každý typ transakce. Své transakce můžete kontrolovat také pomocí externích prohlížečů bloků.



### 6.1. Historie přístupu





- **Přes domovskou obrazovku**:
 - Kliknutím na **Secure Bitcoin Wallet** zobrazíte transakce **v řetězci** nebo na **Instant Payments Wallet** pro transakce **Liquid** a **Lightning**.
 - Historie se zobrazuje přímo pod celkovým portfoliem, filtrovaná podle vybraného typu Wallet.



![image](assets/fr/21.webp)





- Prostřednictvím vyhrazené stránky:
 - Na domovské obrazovce klikněte na symbol **historie** (ikona hodin nebo podobný symbol).
 - Přístup na stránku se seznamem všech transakcí s filtry podle typu akce: **Odeslání**, **Příjem**, **Výměna**, **PayJoin**, **Prodej**, **Koupě** (poznámka: funkce Prodej a Koupě jsou ve fázi vývoje a v současné době, 20. července 2025, nejsou k dispozici).



![image](assets/fr/22.webp)



### 6.2. Údaje o transakci



Každá transakce zobrazuje specifické informace v závislosti na síti a typu akce (odeslání nebo přijetí). Zde jsou k dispozici podrobnosti o **transakci v řetězci** :



![image](assets/fr/23.webp)



### 6.3. Kontrola prostřednictvím Block explorer



Seznam průzkumníků pro sítě **Bitcoin onchain**, **Liquid** a **Lightning** je uveden v dodatku 4.



V případě služby **Lightning** nejsou transakce ve veřejných prohlížečích viditelné. Zkontrolujte podrobnosti (včetně Swap ID pro Boltz) v aplikaci.




## 7. Nastavení



Stránka "Nastavení" je přístupná přímo z domovské stránky aplikace Bull Bitcoin a slouží ke konfiguraci a správě různých aspektů portfolia a uživatelského prostředí.



![image](assets/fr/24.webp)





- **Wallet Záloha**: Zobrazuje frázi pro obnovu portfolia pro bezpečné zálohování. Nejlepší postupy pro správu a ukládání fráze pro obnovu naleznete v části 3. o vytváření portfolia.





- **Wallet Podrobnosti**:
- **Pubkey**: Veřejný klíč spojený s Wallet, který se používá k příjmu adres generate Bitcoin.
- **Cesta odvození**: generate Wallet adresy ze soukromého klíče.





- **Server Electrum (uzel Bitcoin)**: Nastavte připojení k přizpůsobenému uzlu Bitcoin pro transakce v řetězci.





- **Kód PIN**: PIN kód: Aktivujte a/nebo upravte bezpečnostní kód pro ochranu přístupu k aplikaci a funkcím Wallet.





- **Měna**: Vyberte, zda se mají částky zobrazovat v BTC nebo Sats, a výchozí fiat měnu (dolar, euro atd.).





- **Nastavení automatické výměny**: Funkce *Auto Swap* vám umožňuje automatizovat převod vašich BTC z **Instant Payments Wallet (Liquid)** do vašeho **Bitcoin On-Chain** Wallet, jakmile částka dosáhne prahové hodnoty, kterou považujete za dostatečně vysokou, aby ospravedlnila transakční poplatek.





- **Protokoly**: Záznamy o činnosti, které lze sdílet s technickou podporou a usnadnit tak řešení problémů.





- **Přístup k Telegramu pro podporu**: Přímý odkaz na oficiální kanál Telegramu pro pomoc uživatelům.





- **Přístup do Githubu**: Odkaz na [Bull Bitcoin Github repository](https://github.com/SatoshiPortal) pro zobrazení kódu s otevřeným zdrojovým kódem nebo nahlášení problémů.




## PŘÍLOHY



### A1. Vysvětlení PayJoin (P2EP)



![image](assets/fr/25.webp)



**Definice** :




- PayJoin neboli **Pay-to-EndPoint (P2EP)** je transakční technika Bitcoin, která zvyšuje důvěrnost v síti **onchain**. Spojuje záznamy odesílatele a příjemce do jediné transakce, což znesnadňuje dohledání částek a adres.



**Provoz:**




- Při transakci PayJoin spolupracují odesílatel a příjemce prostřednictvím kompatibilního serveru PayJoin na společné transakci generate.
- Místo toho, aby záznamy poskytoval pouze odesílatel (UTXO), přispívá také příjemce jedním ze svých UTXO. Tím se informace viditelné na Blockchain rozostří: místo jediné položky odpovídající skutečné částce jsou nyní položky dvě a výstupy přímo neodrážejí vyměněnou částku.
- Konečná transakce se podobá standardní transakci Bitcoin (multi-input/multi-output), ale díky steganografické struktuře skrývá skutečnou odeslanou částku a vazby mezi adresami.



**Pro použití v zařízení Bull Bitcoin Mobile**




- **Příjem** (Address Supply): PayJoin je ve výchozím nastavení povolen.
- **Odeslat**: Wallet automaticky rozpozná URI PayJoin a podle toho nakonfiguruje transakci, například:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Výhody**




- **Zvýšená důvěrnost**: PayJoin ruší předpoklad, že všechny záznamy v transakci patří jednomu subjektu. U PayJoin vstupy pocházejí od odesílatele i příjemce, což tento předpoklad porušuje.
- **Maskování částek**: Skutečná vyměněná částka se nezobrazuje přímo ve výstupech. Je vypočítána jako rozdíl mezi příchozí a odchozí částkou UTXO příjemce, což činí analýzu zavádějící.



**Omezení**




- PayJoin vyžaduje, aby odesílatel a příjemce používali kompatibilní peněženky, jinak se používá standardní onchain transakce.
- Transakce je o něco složitější (více vstupů a výstupů), což vede k mírně vyšším nákladům.
- Přestože je navržen tak, aby se podobal standardní transakci, pokročilé heuristické postupy (např. nejednoznačné výstupy, známé servery PayJoin) mohou vést k podezření na jeho použití, i když bez absolutní jistoty.



**Další informace:**




- [Slovníček pojmů](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Vysvětlení Replace-by-fee (RBF)



**Definice**: Replace-by-fee (RBF) je funkce sítě Bitcoin, která umožňuje odesílateli urychlit potvrzení **onchain** transakce tím, že souhlasí se zaplacením vyššího poplatku.



**Omezení** :




- RBF není k dispozici pro transakce Liquid nebo Lightning.
- Počáteční transakce musí být při vytvoření označena jako kompatibilní s RBF, což Bull Bitcoin Mobile dělá automaticky, pokud není zakázáno.



**Další informace:**




- [Slovníček pojmů](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Osvědčené postupy



Chcete-li používat **Bull Bitcoin Mobile** bezpečně a efektivně, dodržujte následující doporučení. Pomohou vám ochránit vaše finanční prostředky, optimalizovat transakce a zachovat důvěrnost informací v sítích **Bitcoin (onchain)**, **Liquid** a **Lightning**.





- Zajistěte si frázi pro **obnovení**:
 - Výukový program: [Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- Použijte **zabezpečené ověřování**:
 - Aktivujte **silný kód PIN** nebo **biometrické ověření** (otisk prstu nebo rozpoznání obličeje) pro ochranu přístupu k aplikaci.
 - Nikdy nesdělujte svůj PIN nebo biometrické údaje.





- **Chraňte své soukromí**:
 - generate nový Address pro každý příjem v řetězci nebo Liquid, aby se omezilo sledování na Blockchain.
 - Pro zvýšení důvěrnosti ohledně částky odeslané v řetězci použijte PayJoin, pokud je k dispozici
 - Chcete-li dosáhnout maximální důvěrnosti, připojte svůj Wallet k vlastnímu uzlu Bitcoin prostřednictvím serveru Electrum namísto použití veřejného uzlu





- Vyberte si síť, která nejlépe vyhovuje vašim potřebám:
- **Onchain**: V případě dlouhodobé úschovy nebo transakcí s velkou hodnotou (poplatky jsou v poměru k částce zanedbatelné).
- **Liquid**: Použijte pro rychlé a levné přenosy se zvýšenou důvěrností.
- **Blesk**: Vyberte si okamžité a levné převody malých částek. Pokud jste dva uživatelé Wallet Bull Bitcoin, zvolte Liquid, abyste se vyhnuli poplatkům za výměnu Lightning <> Liquid prostřednictvím Boltz.





- Vždy zkontrolujte dodací adresy:
 - Před odesláním finančních prostředků pečlivě zkontrolujte Address. Finanční prostředky zaslané na nesprávný účet Address jsou navždy ztraceny. Používejte kopírování/vkládání nebo skenování QR kódu, nikdy nekopírujte/neupravujte Address ručně.





- **Optimalizace nákladů**:
 - Pro transakce v řetězci zvolte vhodné poplatky (pomalé, střední, rychlé) podle naléhavosti a přetížení sítě.
 - Pro malá množství použijte Liquid nebo Lightning.
 - Pokud předpokládáte potřebu urychlit potvrzení, aktivujte pro zásilky v řetězci funkci Replace-by-fee (RBF) (viz dodatek 4).





- Aktualizujte aplikaci




### A4. Další zdroje





- **Oficiální odkazy a podpora:**
- [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com), **support@bullbitcoin.com** : e-mailová podpora
- [Oficiální webové stránky Bull Bitcoin](https://bullbitcoin.com/): **Informace o službách Bull Bitcoin, vytvoření účtu, přístup k aplikaci**
- [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile): **Prohlížejte si kód, vývoj a plán, přispívejte k vývoji...**
- [Účet X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)
- Skupina **Telegram** pro mobilní telefon Wallet: skupinový chat s podporou, viz stránka "Nastavení".





- **Block Explorers:**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Blesk: **[1ML (Lightning Network)](https://1ml.com/)**





- **Výuka a výukové programy:** **[Plan ₿ Network](https://planb.network/)**
 - Zajištění fráze pro obnovení



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Slovník pojmů](https://planb.network/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- **Lightning Network**:
- [Slovník pojmů](https://planb.network/resources/glossary/lightning-network)




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Bull Bitcoin



#### Přehled společnosti



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)** je nejstarší nedepozitní platforma Exchange zaměřená výhradně na Bitcoin, která byla založena v roce 2013 na velvyslanectví Bitcoin v kanadském Montrealu. Společnost, v jejímž čele stojí Francis Pouliot, uznávaný průkopník ekosystému Bitcoin, se staví do pozice klíčového hráče v prosazování finanční suverenity a autonomie uživatelů. Jejím posláním je umožnit jednotlivcům získat zpět kontrolu nad svými penězi tím, že budou používat Bitcoin jako nástroj svobody a platebního styku, a zároveň odmítat fiat měny a kryptoměny jiné než Bitcoin.



![image](assets/fr/26.webp)



[Vytvořte si účet](https://app.bullbitcoin.com/registration/orangepeel) se slevou 0,25 % na nákupy a prodeje Bitcoin.



#### Hodnoty a filozofie



Bull Bitcoin vyniká svými zásadami Commitment až Cypherpunk a etikou Bitcoin:





- **Exkluzivní zaměření na Bitcoin**: Platforma je věrná vizi decentralizované měny odolné vůči cenzuře.





- Osoby, které nejsou správci: Uživatelé si zachovávají plnou kontrolu nad svými bitcoiny tím, že si je posílají do vlastních portfolií.





- **Důvěrnost**: U transakcí do 999 USD je minimalizováno shromažďování osobních údajů a možnost nákupu bez KYC. Údaje jsou chráněny v souladu s předpisy (FINTRAC v Kanadě, AMF ve Francii).





- **Transparentnost**: Žádné skryté poplatky, náklady jsou zahrnuty v rozpětí (rozdíl mezi nákupní a prodejní cenou).





- **Finanční suverenita**: Bitcoin podporuje nezávislost na tradičních bankovních systémech a centralizovaných institucích.



#### Hlavní služby





- **Záloha Fiat**: Uživatelé mohou na svůj účet Bull Bitcoin vložit peníze ve fiat měně (CAD, EUR atd.) bankovním převodem nebo v hotovosti/debetní kartou na vybraných kanadských poštách.





- **Nákup Bitcoin**: Uživatelé si mohou zakoupit Bitcoin, který je zasílán přímo do jejich portfolia, které není depozitářem, což zaručuje úplnou kontrolu nad jejich finančními prostředky.





- **Plánovaný nákup Bitcoin**: Bull Bitcoin nabízí automatickou službu opakovaného nákupu (DCA - Dollar Cost Averaging) v pravidelných intervalech, čerpající z vašeho dostupného zůstatku, s přímým převodem bitcoinů na uživatelem řízený Wallet, což snižuje dopad kolísání cen.



Všimněte si, že možnost nazvaná "AutoBuy" vám umožní převést vaše fiaty, jakmile se dotknou vašeho zůstatku na Bull Bitcoin, a poslat vaše Bitcoiny na váš vlastní Wallet. Tuto možnost lze také zkombinovat s pravidelným bankovním převodem naplánovaným u vaší banky a provést tak DCA. Tato možnost zautomatizuje vaši akumulaci Bitcoin, aniž byste museli otevřít aplikaci.






- Nákup Bitcoin za pevnou cenu **"limitní příkaz"**: Umožňuje nakoupit Bitcoin za cenu předem určenou uživatelem, která se automaticky provede, jakmile cena indexu Bull Bitcoin dosáhne nebo klesne pod nastavený limit.





- **Prodej Bitcoin**: Uživatelé mohou prodat své Bitcoiny a obdržet peníze ve fiat měně přímo na svůj bankovní účet prostřednictvím bankovního nebo SEPA převodu.





- **Platby třetích stran**: Bull Bitcoin umožňuje uživatelům posílat fiat peníze na bankovní účty ze svých bitcoinů, a to zcela transparentně pro příjemce.





- **Bull Bitcoin Prime**: Bull Bitcoin Prime je prémiová služba pro bonitní a firemní zákazníky, která nabízí řešení na míru a prémiovou podporu. Zahrnuje přístup ke sníženým poplatkům, vyhrazeného správce účtu a na míru šité podnikové služby. Tato služba je určena institucím, profesionálním obchodníkům a firemním klientům, kteří hledají hluboké odborné znalosti a přednostní zacházení.





- **Mobilní zařízení Wallet**: Bull Bitcoin nabízí mobilní Wallet s otevřeným zdrojovým kódem, dostupný pro Android a iOS, který podporuje transakce onchain, Liquid a Lightning Network.





- **Podpora vzdělávání**: Bezplatné průvodce a osobní koučink, které uživatelům pomáhají vytvořit, zabezpečit a spravovat jejich portfolio Bitcoin a posilují jejich finanční samostatnost.



#### Dodržování předpisů a bezpečnost





- **Právní předpisy**: Bull Bitcoin splňuje požadavky KYC/AML.





- **Bezpečnost**: Používání zabezpečených portfolií a doporučení pro offline ukládání. Osobní údaje jsou umístěny na infrastruktuře Bitcoin společnosti Bull, která je 100% vlastní a nespoléhá se na žádnou třetí stranu.