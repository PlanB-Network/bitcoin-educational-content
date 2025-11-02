---
name: SwapMarket
description: Agregátor výměnných služeb Bitcoin a Lightning
---

![cover](assets/cover.webp)



Převod finančních prostředků mezi Bitcoin On-Chain a Lightning Network obecně vyžaduje buď manuální otevření bleskových kanálů (technické a nákladné), nebo použití centralizovaných swapových platforem s KYC. SwapMarket nabízí alternativu: Trustless atomové swapy prostřednictvím konkurenčních poskytovatelů bez KYC.



Inovace: Ačkoli jsou poskytovatelé zprostředkovateli, HTLC (*Hash Time Locked Contracts*) matematicky zaručují, že vaše prostředky zůstanou pod vaší kontrolou. Agregace několika poskytovatelů (Boltz, ZEUS Swaps, Eldamar, Middle Way) vytváří cenovou konkurenci. Interface webový open-source selfhosting.



## Co je SwapMarket?



SwapMarket, agregátor s otevřeným zdrojovým kódem spuštěný v roce 2024, funguje jako srovnávač poskytovatelů swapů Bitcoin/Lightning. Uživatel okamžitě porovná podmínky (poplatky, likviditu, limity) a vybere optimálního poskytovatele.



### Technická architektura



**Frontend na straně klienta**: na straně klienta (Fork Boltz Web App) umístěné na GitHub Pages. Kód běží v prohlížeči bez backendového serveru. Historie ukládána lokálně (cookies/cache). Veřejný a auditovatelný zdrojový kód.



**Zjištění poskytovatele** : Seznam kódovaný podle Hard v souboru `src/configs/Mainnet.ts`. Noví poskytovatelé se přidávají prostřednictvím žádosti o stažení nebo e-mailu.



**Nezávislé backendy**: Každý poskytovatel provozuje svůj vlastní backend Boltz. Interface se dotazuje na rozhraní API v reálném čase a okamžitě porovnává nabídky.



**HTLC Atomic Swaps**: Hash Smlouvy s časovým zámkem zaručují atomicitu: buď se swap uskuteční, nebo každá strana získá zpět své prostředky. Riziko protistrany je matematicky eliminováno.



### Filozofie



SwapMarket omezuje centralizaci tím, že vytváří konkurenci mezi poskytovateli poplatků a likvidity. Žádné KYC, open-source samohostitelný kód, multiplikace nezávislých operátorů, aby se zabránilo selhání jednoho bodu.



## Hlavní funkce



### Tržiště poskytovatelů



Interface zobrazuje všechny aktivní poskytovatele: název poskytovatele, uplatňované poplatky (procentní a/nebo pevné), minimální/maximální dostupné částky a podporované typy swapů. Aplikace se přímo dotazuje na rozhraní API každého poskytovatele, na které je odkazováno v konfiguračním souboru, a získává nabídky v reálném čase. Konkurence mezi poskytovateli zaručuje optimální sazby, které se u standardních swapů obvykle pohybují kolem 0,5 %.



### Obousměrné výměny



**Výměna (On-Chain → Lightning)**: Převod BTC On-Chain na satoshi Lightning. Případ použití: napájení mobilního Wallet Lightning, získání příchozí kapacity na uzlu nebo okamžitá likvidita.



**Výměna (Lightning → On-Chain)**: Převod bleskových satošů na On-Chain BTC. Případ použití: vyhození Wallet Lightning do úložiště Cold nebo vyrovnání likvidity mezi vrstvami.



### Bezpečnost a zotavení



**Trustless Atomové výměny: HTLC zaručuje, že buď bude Exchange dokončen v plné výši, nebo každá strana získá zpět svůj podíl. Riziko protistrany je matematicky eliminováno.



**Výkupní mechanismus**: Každý swap má datum vypršení platnosti (TIMELOCK). Pokud swap selže, jsou prostředky po vypršení platnosti automaticky vráceny. Uživatel si vždy ponechává možnost získat své bitcoiny zpět.



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



Aplikace bude přístupná na adrese `http://localhost:3000`. Self-hosting zaručuje úplnou kontrolu nad Interface, eliminuje riziko cenzury oficiální domény a umožňuje kontrolu zdrojového kódu před spuštěním.



### Počáteční konfigurace



**Wallet Lightning**: (Phoenix, Zeus, BlueWallet atd.). Pro výměnu budete mít k dispozici generate Lightning Invoice. Za výměnu-vyřazení zaplatíte blesk Invoice.



**Wallet On-Chain**: Wallet Bitcoin On-Chain pro zasílání finančních prostředků. Pro výměnné operace si připravte Bitcoin přijímající Address.



**Volitelná konfigurace**: SwapMarket ukládá swapovou historii a preference do souborů cookie prohlížeče. Není nutné vytvářet účet.



## Přístup k nastavení a záchrannému klíči



Před provedením prvních výměn důrazně doporučujeme stáhnout si **Záchranný klíč**. Tento nouzový klíč vám umožní obnovit vaše finanční prostředky v případě technického problému nebo ztráty přístupu k vašemu zařízení.



### Přístupové parametry



Na hlavní stránce SwapMarketu klikněte na ikonu ozubeného kola (⚙️) v pravém horním rohu Interface vedle formuláře pro výměnu.



![Accès aux paramètres](assets/fr/01.webp)



### Nastavení stránky



Otevře se stránka Nastavení, kde se zobrazí několik možností konfigurace:





- Jmenovitá hodnota**: BTC nebo Sats
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



Tento první příklad ukazuje, jak převést bleskové satoši na bitcoiny On-Chain.



**Krok 1: Výměna konfigurace



Na hlavní stránce vyberte formulář výměny :




- BLESK** (horní pole): Zadejte částku, kterou si přejete zaslat v Sats Lightning (příklad: 30 000 Sats)
- Bitcoin** (spodní pole): Částka, kterou obdržíte, se zobrazí automaticky po odečtení poplatků (příklad: Sats 29 320)



Do spodního pole vložte svůj **příjem Bitcoin Address**, kam si přejete finanční prostředky obdržet. Tuto položku Address pečlivě zkontrolujte.



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



**Upozornění**: Výběr poskytovatele Interface nezobrazuje **minimální částky** pro jednotlivé poskytovatele. Tyto informace se zobrazí až v Interface pro vytvoření výměny po výběru poskytovatele. Minimální a maximální částky se mohou u jednotlivých poskytovatelů lišit a v průběhu času se mohou měnit. **Vždy si tyto limity zkontrolujte v okamžiku swapu**: pokud částka, kterou chcete swapovat, je mimo limity poskytovatele, můžete si vybrat jiného, vhodnějšího pro vaši transakci.



![Sélection du provider](assets/fr/04.webp)



**Krok 3: Vytvoření swapu a blesková platba**



Klikněte na žluté tlačítko **"CREATE ATOMIC SWAP "**. SwapMarket pro vás vytvoří **Lightning Invoice** (BOLT11), který zaplatíte ze svého Wallet Lightning.



Na stránce se zobrazí :




- Swap ID**: Jedinečný swapový identifikátor (příklad: J4ymFIMVR6Hm)
- Stav**: "(swap vytvořen, čeká na platbu)
- QR kód**: Naskenujte jej pomocí Wallet Lightning
- Invoice Lightning**: (příklad: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Tento účet Invoice zaplaťte ze svého blesku Wallet (Phoenix, Zeus, BlueWallet atd.). Zobrazí se přesná částka, která má být zaplacena (příklad: 30 000 Sats).



![Paiement Lightning](assets/fr/05.webp)



**Krok 4: Potvrzení a přijetí**



Jakmile je platba Lightning potvrzena, SwapMarket okamžitě obdrží vaši platbu a poskytovatel odvysílá transakci Bitcoin do vašeho Address.



Stav se změní na **"Invoice.settled "** (Invoice zaplacen) a zobrazí se potvrzovací zpráva.



Vaše bitcoiny On-Chain budou k dispozici, jakmile bude transakce potvrzena (obvykle během několika minut až několika hodin, v závislosti na poplatcích Mining zvolených poskytovatelem).



![Confirmation swap-out](assets/fr/06.webp)



Kliknutím na **"OPEN CLAIM TRANSACTION "** můžete zobrazit transakci Bitcoin v průzkumníku Blockchain.



### Výměna: Bitcoin → Blesk



Tento druhý příklad ukazuje, jak převést bitcoiny On-Chain na bleskové satoši.



**Krok 1: Výměna konfigurace



Na hlavní stránce vyberte formulář výměny :




- Bitcoin** (horní pole): Bitcoin (příklad: 63 400 Sats)
- BLESK** (spodní pole): Částka, kterou obdržíte, se zobrazí automaticky po odečtení poplatků (příklad: 62 884 Sats)



Do spodního pole vložte blesk** Invoice (BOLT11) vygenerovaný z blesku Wallet nebo použijte LNURL Address, pokud jej váš blesk Wallet podporuje.



![Configuration swap-in](assets/fr/07.webp)



**Krok 2: Kontrola záchranného klíče**



Po kliknutí na **"CREATE ATOMIC SWAP "** se zobrazí modální okno s žádostí o ověření záchranného klíče.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rescue Key**: Klikněte na tlačítko **"OVĚŘIT EXISTUJÍCÍ KLÍČ "** a uložený klíč importujte.



Vyberte dříve stažený soubor Rescue Key. Po úspěšném ověření přejde Interface automaticky k dalšímu kroku.



**Krok 3: záloha Bitcoin** Address



SwapMarket nyní generuje **unikátní Bitcoin Address** obsahující HTLC Contract propojený s vaším bleskem Invoice.



Na stránce se zobrazí :




- Swap ID**: Jedinečný identifikátor (příklad: 1kGmB6JyGqU4)
- Stav** : "Invoice.set" (Invoice nastaven, čeká na platbu Bitcoin)
- QR kód**: Bitcoin depo Address
- Bitcoin** Address: Obvykle začíná slovy "bc1p..." (příklad: bc1p5mvtwxapjkds...9d4n9f)
- Žluté varování** : "Ujistěte se, že se transakce potvrdí do ~24 hodin po vytvoření této výměny!"



Tato doba ~24 hodin je **časový limit** HTLC Contract. Pokud transakce Bitcoin nebude v tomto časovém rámci potvrzena, výměna se nezdaří a vy budete muset použít záchranný klíč, abyste získali své prostředky zpět.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Kód Address můžete zkopírovat kliknutím na tlačítko **"Address"** nebo naskenováním QR kódu přímo z Wallet On-Chain.



**Krok 4: Odesílání bitcoinů**



Ze svého účtu Wallet Bitcoin On-Chain odešlete **přesně** uvedenou částku (např. 63 400 Sats) na vygenerovaný účet Address.



**Důležité**: Pro zaručení rychlého potvrzení použijte příslušné poplatky Mining. Pokud je poplatek příliš nízký a transakce zůstane v Mempool po uplynutí časového limitu (~24 h), výměna se nezdaří.



Jakmile je transakce odeslána, SwapMarket zjistí, že je v Mempool, a zobrazí :




- Stav** : "transaction.Mempool"
- Zpráva**: "Transakce je v Mempool - čekáme na potvrzení pro dokončení výměny"



![Transaction en mempool](assets/fr/10.webp)



**Krok 5: Potvrzení a přijetí blesku**



Jakmile transakce Bitcoin obdrží první potvrzení, poskytovatel automaticky vyplatí váš bleskový účet Invoice. Na váš blesk Wallet okamžitě obdržíte satoši.



Stav se změní na **"transaction.claim.pending "** a zobrazí se potvrzovací zpráva:



![Confirmation swap-in](assets/fr/11.webp)



Vaše bleskové satelity jsou ihned k dispozici ve vašem Wallet.



## Výhody a omezení



### Výhody



**Soutěž o ceny**: Sdružování poskytovatelů vytváří přirozenou konkurenci, která snižuje poplatky (0,49 % až 0,5 %).



**Důvěrnost**: Žádné KYC, Interface 100% na straně klienta (bez přenosu osobních údajů), kompatibilní s Tor Browserem.



**Nezávislý**: HTLC matematicky zaručuje výlučnou kontrolu nad vašimi prostředky. Buď se výměna podaří, nebo dostanete své bitcoiny zpět.



**Open-source self-hostable**: auditovatelný veřejný kód, který lze nasadit lokálně pro maximální odolnost vůči cenzuře.



### Omezení



**Omezená likvidita**: Omezený počet aktivních poskytovatelů (Boltz, Eldamar, MiddleWay v závislosti na období). Maximální částky mohou být omezeny.



**Čas vypršení platnosti**: Časový limit od 24h do 48h. Pokud není transakce On-Chain potvrzena před vypršením platnosti, je nutné ruční obnovení.



**Interface centralizace**: Oficiální Interface je sice umístěn na stránkách GitHubu, ale je možné jej hostovat na vlastním serveru. Pokud GitHub cenzuruje repozitář, přístup přes swapmarket.github.io bude zablokován (řešení: selfhosting).



**Stopy On-Chain**: Skripty HTLC jsou potenciálně identifikovatelné pomocí pokročilé analýzy Blockchain.



## Osvědčené postupy



### Zabezpečená konfigurace



**Stáhněte si záchranný klíč**: Před první výměnou si stáhněte záchranný klíč z Nastavení (viz výše). Tento jedinečný klíč bude fungovat pro všechny vaše budoucí swapy a umožní vám v případě problému obnovit vaše prostředky.



**Používejte prohlížeč Tor**: Pro maximální utajení přistupujte ke SwapMarketu přes Tor Browser, abyste skryli svou IP adresu Address.



**Zvažte možnost vlastního hostingu**: Pro technické uživatele je provozování vlastní instance SwapMarketu eliminací závislosti na oficiální doméně GitHub Pages.



### Optimalizace výměny



**Sledujte Mempool**: Před výměnou zkontrolujte prostor Mempool.space. Vyberte si časy s nízkou aktivitou, abyste minimalizovali náklady na Mining.



**Zkontrolujte adresy**: Při výměně pečlivě zkontrolujte přijímající Address. Použijte kopírování a vložení a zkontrolujte prvních 5 a posledních 5 znaků.



**Zkoušejte s malým množstvím**: Začněte s minimálním povoleným množstvím (25 000 až 50 000 Sats). Po zvládnutí procesu množství postupně zvyšujte.



**Dokumentujte své výměny**: Zaznamenejte si ID každé výměny, datum vyplacení Address a datum vypršení platnosti. Tyto informace usnadňují sledování a obnovu v případě technického problému.



### Strategie používání



**Vyvážení peněžních toků**: (úspory, dlouhodobé zajištění) a Lightning (denní výdaje, okamžité platby) podle vašich skutečných potřeb.



**Vypočítejte ziskovost**: Pro trvalé potřeby likvidity Lightning porovnejte kumulativní náklady na opakované swapy oproti přímému otevření kanálu Lightning. SwapMarket vyniká pro jednorázové úpravy, ne nutně pro velké pravidelné toky.



## SwapMarket vs Boltz: Jaký je mezi nimi rozdíl?



### Boltz: Technologie vs. služby



**Boltz je technologie s otevřeným zdrojovým kódem** (`boltz-backend` na GitHubu), která implementuje atomické výměny prostřednictvím HTLC mezi Bitcoin, Lightning a Liquid.



**Kritický bod**: Všichni poskytovatelé SwapMarketu (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) nasazují vlastní instanci backendu Boltz. Základní technologie je tedy totožná. Zranitelnost v backendu Boltz by potenciálně ovlivnila všechny poskytovatele, ale open-source povaha systému umožňuje komunitní audit.



**Boltz Exchange** je jediná služba provozovaná týmem Boltz, zatímco **SwapMarket** sdružuje několik poskytovatelů, kteří využívají technologii Boltz, a vytváří tak konkurenční cenové prostředí.



Další podrobnosti naleznete v našich návodech Boltz a Zeus Swap:



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.network/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

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



**Doporučení**: Pro zjednodušení použijte Boltz Exchange nebo SwapMarket pro optimalizaci nákladů prostřednictvím konkurence. Obě varianty jsou z hlediska bezpečnosti rovnocenné (HTLC není omezující).



## Závěr



SwapMarket usnadňuje výměny Bitcoin/Lightning tím, že sdružuje více poskytovatelů do jediného Interface. Architektura HTLC zaručuje, že swapy nebudou podléhat prověřování, absence KYC zachovává důvěrnost a samohostitelný kód s otevřeným zdrojovým kódem posiluje odolnost vůči cenzuře.



Konkurence mezi poskytovateli zvyšuje sazby a rozšiřuje zdroje likvidity. Pro optimalizaci řízení dvou Layer (úspory On-Chain, výdaje na Lightning) je SwapMarket praktickým nástrojem, který zachovává finanční suverenitu a důvěrnost.



## Zdroje



### Oficiální dokumentace




- [SwapMarket - webová aplikace](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Technická dokumentace](https://docs.boltz.Exchange/)
- [Průvodce vlastním hostováním](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Související projekty




- [Boltz Exchange](https://boltz.Exchange) - Původní služba výměny atomů
- [ZEUS Swaps](https://zeusln.com) - Poskytovatel bleskových swapů