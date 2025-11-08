---
name: SwapMarket
description: Agregátor výměnných služeb Bitcoin a Lightning
---

![cover](assets/cover.webp)



Převod finančních prostředků mezi Bitcoin on-chain a Lightning Network obecně vyžaduje buď manuální otevření bleskových kanálů (technické a nákladné), nebo použití centralizovaných swapových platforem s KYC. SwapMarket nabízí alternativu: nedůvěryhodné atomické swapy prostřednictvím konkurenčních poskytovatelů bez KYC.



Inovace: Ačkoli jsou poskytovatelé zprostředkovateli, HTLC (*Smlouvy Hash s časovým zámkem*) matematicky zaručují, že vaše prostředky zůstanou pod vaší kontrolou. Agregace několika poskytovatelů (Boltz, ZEUS Swaps, Eldamar, Middle Way) vytváří cenovou konkurenci. Interface webový open-source selfhosting.



## Co je SwapMarket?



SwapMarket, agregátor s otevřeným zdrojovým kódem spuštěný v roce 2024, funguje jako srovnávač poskytovatelů swapů Bitcoin/Lightning. Uživatel okamžitě porovná podmínky (poplatky, likviditu, limity) a vybere optimálního poskytovatele.



### Technická architektura



**Frontend na straně klienta**: na straně klienta (fork Boltz Web App) umístěné na GitHub Pages. Kód běží v prohlížeči bez backendového serveru. Historie ukládána lokálně (cookies/cache). Veřejný a auditovatelný zdrojový kód.



**Zjištění poskytovatele** : Hardcoded seznam v souboru `src/configs/mainnet.ts`. Noví poskytovatelé se přidávají prostřednictvím žádosti o stažení nebo e-mailu.



**Nezávislé backendy**: Každý poskytovatel provozuje svůj vlastní backend Boltz. Rozhraní se dotazuje na API v reálném čase a okamžitě porovnává nabídky.



**HTLC Atomic Swaps**: Hash Smlouvy s časovým zámkem zaručují atomicitu: buď se swap uskuteční, nebo každá strana získá zpět své prostředky. Riziko protistrany je matematicky eliminováno.



### Filozofie



SwapMarket omezuje centralizaci tím, že vytváří konkurenci mezi poskytovateli poplatků a likvidity. Žádné KYC, open-source samohostitelný kód, multiplikace nezávislých operátorů, aby se zabránilo selhání jednoho bodu.



## Hlavní funkce



### Tržiště poskytovatelů



Rozhraní zobrazuje všechny aktivní poskytovatele: název poskytovatele, uplatňované poplatky (procentní a/nebo pevné), minimální/maximální dostupné částky a podporované typy swapů. Aplikace se přímo dotazuje na rozhraní API jednotlivých poskytovatelů, na které je odkazováno v konfiguračním souboru, a získává nabídky v reálném čase. Konkurence mezi poskytovateli zaručuje optimální sazby, které se u standardních swapů obvykle pohybují kolem 0,5 %.



### Obousměrné výměny



**Výměna (on-chain → Lightning)**: Převod on-chain BTC na Lightning satoshis. Případ použití: napájení mobilního wallet Lightning, získání příchozí kapacity na uzlu nebo okamžitá likvidita.



**Výměna (Lightning → on-chain)**: Převést bleskové satoši na on-chain BTC. Případ použití: Vyprázdněte wallet Lightning do chladicího skladu nebo vyvažte likviditu mezi vrstvami.



### Bezpečnost a zotavení



**Trustless atomové výměny**: HTLC zaručují, že buď bude výměna dokončena v plné výši, nebo každá strana získá zpět svůj podíl. Riziko protistrany je matematicky eliminováno.



**Mezinformace o splácení**: Každý swap má časový zámek. Pokud swap selže, jsou prostředky po vypršení platnosti automaticky vráceny. Uživatel si vždy ponechává možnost získat své bitcoiny zpět.



**Klíče pro obnovu**: SwapMarket umožňuje exportovat obnovovací klíče pro probíhající swapy. V případě problému lze tyto klíče použít k dokončení nebo zrušení výměny z libovolného zařízení.



## Instalace a přístup



### Interface web



SwapMarket nevyžaduje žádnou instalaci. Přístup je možný přes prohlížeč na adrese https://swapmarket.github.io. Pro maximální důvěrnost použijte Brave, Firefox s rozšířeními proti sledování nebo LibreWolf. Pro síťovou anonymitu se doporučuje prohlížeč Tor.



Nevyžaduje se žádná registrace, e-mail ani ověření totožnosti.



### Vlastní hostování (volitelné)



Pro technické uživatele, kteří chtějí eliminovat závislost na oficiální doméně GitHub Pages, lze SwapMarket spustit lokálně :



**Přes npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Přes Docker** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



Aplikace bude přístupná na adrese `http://localhost:3000`. Vlastní hostování zaručuje úplnou kontrolu nad rozhraním, eliminuje riziko cenzury oficiální domény a umožňuje kontrolu zdrojového kódu před spuštěním.



### Počáteční konfigurace



**Wallet Lightning**: (Phoenix, Zeus, BlueWallet atd.). Pro výměnu budete mít fakturu generate Lightning. Za výměnu-outs zaplatíte fakturu Lightning.



**Wallet on-chain**: wallet Bitcoin on-chain pro zasílání finančních prostředků. Pro swap-outs si připravte přijímací adresu Bitcoin.



**Volitelná konfigurace**: SwapMarket ukládá swapovou historii a preference do souborů cookie prohlížeče. Není nutné vytvářet účet.



## Přístup k nastavení a záchrannému klíči



Před provedením prvních výměn důrazně doporučujeme stáhnout si **Záchranný klíč**. Tento nouzový klíč vám umožní obnovit vaše finanční prostředky v případě technického problému nebo ztráty přístupu k vašemu zařízení.



### Přístupové parametry



Na hlavní stránce SwapMarketu klikněte na ikonu ozubeného kola (⚙️) v pravém horním rohu rozhraní vedle formuláře swapu.



![Accès aux paramètres](assets/fr/01.webp)



### Nastavení stránky



Otevře se stránka Nastavení, kde se zobrazí několik možností konfigurace:





- Jmenovitá hodnota**: BTC nebo sats
- Oddělovač desetinných míst**: Oddělovač desetinných míst (, nebo .)
- Oznámení zvuku/prohlížeče**: Zvukové oznámení a oznámení prohlížeče
- Záchranný klíč** : Stáhněte si klíč pro obnovení
- Protokoly**: Zobrazit, stáhnout nebo odstranit protokoly



![Page Settings](assets/fr/02.webp)



### Stáhnout Rescue Key



Klikněte na tlačítko **Stáhnout** vedle položky "Rescue Key".



**Důležité body** :




- Záchranný klíč je **jediný nouzový klíč**, který funguje pro všechny vaše budoucí výměny
- Tento klíč uchovávejte na **bezpečném a trvalém** místě (správce hesel, digitální trezor)
- V případě problému s výměnou (timeout, technická porucha) vám tento klíč umožní obnovit vaše prostředky



## Vytvoření swapu krok za krokem



### Výměna: Blesk → Bitcoin



Tento první příklad ukazuje, jak převést bleskové satoši na bitcoiny on-chain.



**Krok 1: Výměna konfigurace



Na hlavní stránce vyberte formulář výměny :




- BLESK** (horní pole): Zadejte částku, kterou si přejete zaslat v sats Lightning (příklad: 30 000 sats)
- BITCOIN** (spodní pole): Částka, kterou obdržíte, se zobrazí automaticky po odečtení poplatků (příklad: 29 320 sats)



Do spodního pole vložte svou **přijímací adresu Bitcoin**, na kterou chcete peníze obdržet. Tuto adresu pečlivě zkontrolujte.



Výchozím poskytovatelem je obvykle Boltz Exchange. Síťové poplatky a poplatky poskytovatele jsou zřetelně zobrazeny.



![Configuration swap-out](assets/fr/03.webp)



**Krok 2: Výběr poskytovatele**



Kliknutím na rozbalovací nabídku poskytovatele (výchozí: "Boltz Exchange") zobrazíte všechny dostupné poskytovatele likvidity.



Otevře se modální okno se srovnávací tabulkou:




- Stav**: Green indikátor, zda je poskytovatel aktivní
- Alias**: (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Poplatek**: Poplatky účtované poskytovatelem (obvykle 0,49 % až 0,5 %)
- Maximální výměna**: Maximální částka přijímaná pro swap



Porovnejte poplatky a maximální částky a vyberte si poskytovatele podle svého výběru.



**Upozornění**: Rozhraní pro výběr poskytovatele nezobrazuje **minimální částky** pro jednotlivé poskytovatele. Tato informace se zobrazí pouze v rozhraní pro vytvoření swapu po výběru poskytovatele. Minimální a maximální částky se mohou u jednotlivých poskytovatelů lišit a v průběhu času se mohou měnit. **Vždy si tyto limity zkontrolujte v době swapu**: pokud částka, kterou chcete swapovat, přesahuje limity poskytovatele, můžete si vybrat jiného, vhodnějšího pro vaši transakci.



![Sélection du provider](assets/fr/04.webp)



**Krok 3: Vytvoření swapu a blesková platba**



Klikněte na žluté tlačítko **"CREATE ATOMIC SWAP "**. SwapMarket vám generate vystaví **Bleskovou fakturu** (BOLT11), kterou můžete zaplatit ze svého wallet Blesku.



Na stránce se zobrazí :




- Swap ID**: Jedinečný swapový identifikátor (příklad: J4ymFIMVR6Hm)
- Stav**: "(swap vytvořen, čeká na platbu)
- QR kód**: Naskenujte jej pomocí wallet Lightning
- Invoice Lightning**: (příklad: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Tuto fakturu uhraďte z blesku wallet (Phoenix, Zeus, BlueWallet atd.). Zobrazí se přesná částka k úhradě (příklad: 30 000 sats).



![Paiement Lightning](assets/fr/05.webp)



**Krok 4: Potvrzení a přijetí**



Jakmile je platba Lightning potvrzena, SwapMarket okamžitě obdrží vaši platbu a poskytovatel odvysílá transakci Bitcoin na vaši adresu.



Stav se změní na **"invoice.settled "** (faktura uhrazena) a zobrazí se potvrzovací zpráva.



Vaše bitcoiny on-chain budou k dispozici, jakmile bude transakce potvrzena (obvykle za několik minut až hodin, v závislosti na poplatcích mining zvolených poskytovatelem).



![Confirmation swap-out](assets/fr/06.webp)



Kliknutím na **"OPEN CLAIM TRANSACTION "** si můžete transakci Bitcoin prohlédnout v prohlížeči blockchainu.



### Výměna: Bitcoin → Lightning



Tento druhý příklad ukazuje, jak převést bitcoiny on-chain na bleskové satoši.



**Krok 1: Výměna konfigurace



Na hlavní stránce vyberte formulář výměny :




- BITCOIN** (horní pole): Zadejte částku, kterou si přejete odeslat v sats Bitcoin (příklad: 63 400 sats)
- BLESK** (spodní pole): Částka, kterou obdržíte, se zobrazí automaticky po odečtení poplatků (příklad: 62 884 sats)



Do spodního pole vložte fakturu Lightning** (BOLT11) vygenerovanou z blesku wallet nebo použijte adresu LNURL, pokud ji váš blesk wallet podporuje.



![Configuration swap-in](assets/fr/07.webp)



**Krok 2: Kontrola záchranného klíče**



Po kliknutí na **"CREATE ATOMIC SWAP "** se zobrazí modální okno s žádostí o ověření záchranného klíče.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rescue Key**: Klikněte na tlačítko **"OVĚŘIT EXISTUJÍCÍ KLÍČ "** a uložený klíč importujte.



Vyberte dříve stažený soubor Rescue Key. Po úspěšném ověření se rozhraní automaticky přepne na další krok.



**Krok 3: adresa vkladu Bitcoin**



SwapMarket nyní generuje **unikátní adresu Bitcoin** obsahující smlouvu HTLC spojenou s vaší fakturou Lightning.



Na stránce se zobrazí :




- Swap ID**: Jedinečný identifikátor (příklad: 1kGmB6JyGqU4)
- Stav**: "(faktura nastavena, čeká na platbu Bitcoin)
- QR kód**: Adresa depa Bitcoin
- Adresa Bitcoin**: Obvykle začíná "bc1p..." (příklad: bc1p5mvtwxapjkds...9d4n9f)
- Žluté varování** : "Ujistěte se, že se transakce potvrdí do ~24 hodin po vytvoření této výměny!"



Tato doba ~24 hodin je **časovým limitem** smlouvy HTLC. Pokud transakce Bitcoin nebude v tomto časovém rámci potvrzena, výměna se nezdaří a vy budete muset použít záchranný klíč, abyste získali své prostředky zpět.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Adresu můžete zkopírovat kliknutím na tlačítko **"ADRESA "** nebo naskenovat QR kód přímo z vašeho wallet on-chain.



**Krok 4: Odesílání bitcoinů**



Ze svého účtu wallet Bitcoin on-chain zašlete **přesně** uvedenou částku (např. 63 400 sats) na vygenerovanou adresu.



**Důležité**: Pro zaručení rychlého potvrzení použijte příslušné poplatky mining. Pokud je poplatek příliš nízký a transakce zůstane v mempoolu po uplynutí časového limitu (~24 h), výměna se nezdaří.



Jakmile je transakce odeslána, SwapMarket zjistí, že je v mempoolu, a zobrazí :




- Stav** : "transaction.mempool
- Zpráva**: "Transakce je v mempoolu - čekáme na potvrzení pro dokončení výměny"



![Transaction en mempool](assets/fr/10.webp)



**Krok 5: Potvrzení a přijetí blesku**



Jakmile transakce Bitcoin obdrží první potvrzení, poskytovatel automaticky uhradí vaši fakturu Lightning. Na svůj blesk wallet okamžitě obdržíte satoši.



Stav se změní na **"transaction.claim.pending "** a zobrazí se potvrzovací zpráva:



![Confirmation swap-in](assets/fr/11.webp)



Bleskové satelity jsou okamžitě k dispozici v wallet.



## Výhody a omezení



### Výhody



**Soutěž o ceny**: Sdružování poskytovatelů vytváří přirozenou konkurenci, která snižuje poplatky (0,49 % až 0,5 %).



**Důvěrnost**: Žádné KYC, 100% rozhraní na straně klienta (bez přenosu osobních údajů), kompatibilní s prohlížečem Tor Browser.



**Nezávislý**: HTLC matematicky zaručuje výlučnou kontrolu nad vašimi prostředky. Buď se výměna podaří, nebo dostanete své bitcoiny zpět.



**Open-source self-hostable**: auditovatelný veřejný kód, který lze nasadit lokálně pro maximální odolnost vůči cenzuře.



### Omezení



**Omezená likvidita**: Omezený počet aktivních poskytovatelů (Boltz, Eldamar, MiddleWay v závislosti na období). Maximální částky mohou být omezeny.



**Čas vypršení platnosti**: Časový limit od 24h do 48h. Pokud není transakce on-chain potvrzena před vypršením platnosti, je nutné ruční obnovení.



**Interface centralizace**: Oficiální rozhraní je umístěno na GitHub Pages. Pokud GitHub cenzuruje repozitář, přístup přes swapmarket.github.io bude zablokován (řešení: selfhosting).



**on-chain Traces**: HTLC jsou potenciálně identifikovatelné pokročilou analýzou blockchainu.



## Osvědčené postupy



### Zabezpečená konfigurace



**Stáhněte si záchranný klíč**: Před první výměnou si stáhněte záchranný klíč z Nastavení (viz výše). Tento jedinečný klíč bude fungovat pro všechny vaše budoucí swapy a umožní vám v případě problému obnovit vaše prostředky.



**Používejte prohlížeč Tor**: Pro maximální utajení přistupujte ke SwapMarketu přes Tor Browser, abyste skryli svou IP adresu.



**Zvažte možnost vlastního hostingu**: Pro technické uživatele je provozování vlastní instance SwapMarketu eliminací závislosti na oficiální doméně GitHub Pages.



### Optimalizace výměny



**Sledujte paměťový fond**: Před výměnou zkontrolujte mempool.space. Vybírejte si časy s nízkou aktivitou, abyste minimalizovali náklady na mining.



**Zkontrolujte adresy**: V případě výměny pečlivě zkontrolujte adresu příjemce. Použijte kopírování a vložení a zkontrolujte prvních 5 a posledních 5 znaků.



**Zkoušejte s malým množstvím**: Začněte s minimálním povoleným množstvím (25 000 až 50 000 sats). Po zvládnutí procesu postupně zvyšujte.



**Dokumentujte své výměny**: Zaznamenejte si ID každé výměny, adresu výkupu a datum ukončení platnosti. Tyto informace usnadňují sledování a obnovu v případě technického problému.



### Strategie používání



**Vyvážení peněžních toků**: (úspory, dlouhodobé zajištění) a Lightning (denní výdaje, okamžité platby) podle vašich skutečných potřeb.



**Vypočítejte ziskovost**: Pro trvalé potřeby likvidity Lightning porovnejte kumulativní náklady na opakované swapy oproti přímému otevření kanálu Lightning. SwapMarket vyniká pro jednorázové úpravy, ne nutně pro velké pravidelné toky.



## SwapMarket vs Boltz: Jaký je mezi nimi rozdíl?



### Boltz: Technologie vs. služby



**Boltz je technologie s otevřeným zdrojovým kódem** (`boltz-backend` na GitHubu), která implementuje atomické výměny prostřednictvím HTLC mezi Bitcoin, Lightning a Liquid.



**Kritický bod**: Všichni poskytovatelé SwapMarketu (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) nasazují vlastní instanci backendu Boltz. Základní technologie je tedy totožná. Zranitelnost v backendu Boltz by potenciálně ovlivnila všechny poskytovatele, ale open-source povaha systému umožňuje komunitní audit.



**Boltz Exchange** je jediná služba provozovaná týmem Boltz, zatímco **SwapMarket** sdružuje několik poskytovatelů, kteří využívají technologii Boltz, a vytváří tak konkurenční cenové prostředí.



Další podrobnosti naleznete v našich návodech Boltz a Zeus Swap:



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Hlavní rozdíly



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**Výhody SwapMarketu**: Cenová konkurence, diverzifikace backendových instancí, porovnávání v reálném čase.



**Technologické alternativy** (nekompatibilní se SwapMarketem): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Tato řešení používají vlastní implementace podmořských swapů.



**Doporučení**: Použijte Boltz Exchange pro zjednodušení nebo SwapMarket pro optimalizaci nákladů prostřednictvím konkurence. Obě varianty jsou z hlediska bezpečnosti rovnocenné (HTLC není omezující).



## Závěr



SwapMarket usnadňuje výměny Bitcoin/Lightning tím, že sdružuje více poskytovatelů do jediného rozhraní. Architektura HTLC zaručuje, že swapy nebudou podléhat prověřování, absence KYC zachovává důvěrnost a samostatně hostitelský kód s otevřeným zdrojovým kódem posiluje odolnost vůči cenzuře.



Konkurence mezi poskytovateli zvyšuje sazby a rozšiřuje zdroje likvidity. Pro optimalizaci dvouúrovňového řízení (úspory on-chain, výdaje Lightning) je SwapMarket praktickým nástrojem, který zachovává finanční suverenitu a důvěrnost.



## Zdroje



### Oficiální dokumentace




- [SwapMarket - webová aplikace](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Technická dokumentace](https://docs.boltz.exchange/)
- [Průvodce vlastním hostováním](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Související projekty




- [Boltz Exchange](https://boltz.exchange) - Původní služba výměny atomů
- [ZEUS Swaps](https://zeusln.com) - Poskytovatel bleskových swapů