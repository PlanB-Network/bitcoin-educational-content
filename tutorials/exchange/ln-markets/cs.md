---
name: LN Markets
description: Obchodní platforma Bitcoin na Lightning Network
---

![cover](assets/cover.webp)



LN Markets je první skutečně Lightning-nativní obchodní platforma Bitcoin, která umožňuje obchodovat s pákovými deriváty Bitcoin přímo z vašeho wallet Lightning, bez KYC, s okamžitým vypořádáním a minimální úschovou. Byla spuštěna v roce 2020 a odstraňuje třecí plochy tradičních burz: žádné ověřování totožnosti, žádné blokované vklady, žádné čekání na potvrzení blockchainu. Váš wallet Lightning se stane vaším obchodním účtem.



## Co je LN Markets?



LN Markets nabízí **Futures** (trvalé kontrakty s pákovým efektem až 100×) a **Options** (Call/Put s rizikem omezeným na zaplacené pojistné). Platforma funguje jako vrstva pro agregaci likvidity konsolidující více obchodních míst pro optimální provádění obchodů s nulovým skluzem. Vaše finanční prostředky jsou uzamčeny pouze přesně na dobu trvání aktivních pozic, nikoliv na dny nebo týdny jako u tradičního depozitního účtu.



### Dostupné obchodní produkty



**Futures (trvalé smlouvy)**



Trvalé kontrakty jsou futures bez data vypršení platnosti, které umožňují spekulovat na vývoj ceny Bitcoin s pákovým efektem. LN Markets nabízí dva režimy řízení marže:



**Izolovaný režim**: Každá pozice má vlastní vyhrazené rozpětí. Ohroženy jsou pouze prostředky přidělené této konkrétní pozici. Pokud pozice dosáhne likvidační ceny, **zlikviduje se pouze tato pozice**, vaše ostatní pozice a zbývající zůstatek nejsou ovlivněny. Ideální pro striktní omezení rizika na obchod.



**Křížový režim (Cross Margin)** : Marže je sdílena mezi všemi vašimi otevřenými pozicemi. Váš celkový zůstatek na účtu slouží jako zajištění pro všechny vaše pozice. Pokud se pozice pokazí, systém čerpá celý váš dostupný zůstatek, aby se zabránilo její likvidaci. **Riziko**: Pokud váš celkový zůstatek dojde, mohou být všechny vaše pozice současně zlikvidovány. Doporučujeme pouze zkušeným obchodníkům, kteří se snaží maximalizovat kapitálovou efektivitu.



**Řízení pozic** :





- Dlouhá pozice**: sázíte na růst kurzu BTC/USD. Pokud cena vzroste, vyhráváte, pokud klesne, prohráváte. **Příklad**: Bitcoin za 100 000 USD, otevřete dlouhou pozici s 10 000 sats a 10× pákovým efektem. Pokud Bitcoin vzroste na 105 000 USD (+5 %), vaše pozice získá 50 % (5 % × 10), tj. ~5 000 sats zisk. Pokud Bitcoin klesne na 95 000 USD (-5 %), ztratíte 50 %, tj. ztrátu ~5 000 sats.





- Krátká pozice**: sázíte na pokles BTC/USD. Pokud cena klesne, vyhráváte, pokud stoupne, prohráváte. **Příklad**: Bitcoin za 100 000 USD, otevřete krátkou pozici s 10 000 sats a 10× pákovým efektem. Pokud Bitcoin klesne na 95 000 USD (-5 %), vyhráváte 50 %, tj. ~5 000 sats. Pokud Bitcoin vzroste na 105 000 USD (+5 %), ztratíte 50 %.



Pákový efekt (až 100×) úměrně zesiluje zisky a ztráty. Mechanismus **funding rate** (pravidelné poplatky každých 8 hodin) vyrovnává dlouhé a krátké pozice. Současně můžete spravovat až 100 futures pozic.



**Možnosti**



Opce je jako **losovací lístek s platností**. Platíte prémii za sázku na směr vývoje ceny Bitcoin. **Hlavní výhoda**: nikdy nemůžete ztratit více než zaplacenou prémii, není možná likvidace.





- Kupní opce (býčí sázka)**: Sázíte na to, že Bitcoin vzroste nad realizační hodnotu před vypršením platnosti. Pokud cena vzroste, vyhráváte, pokud cena klesne, ztráta je omezena na prémii.





- Prodejní opce (medvědí sázka)**: Sázíte na to, že Bitcoin klesne pod realizační hodnotu. Vyhrajete, pokud cena klesne, ztráta je omezena na prémii, pokud cena vzroste.





- Straddle (sázka na volatilitu)**: Koupíte si současně kupní a prodejní sázku. Vyhrajete, pokud Bitcoin udělá velký pohyb jakýmkoli směrem, obě prémie ztratíte, pokud cena zůstane stabilní.



Limit: 50 souběžných pozic. Ideální pro začátky obchodování s pákovým efektem bez obav z likvidace.



**sats ↔ sUSD**: USD, abyste se ochránili před volatilitou, nebo naopak, abyste znovu získali expozici vůči Bitcoin.



## Přístup k platformě a vytvoření účtu



### Přejít na stránku LN Markets



Přejděte na stránku [lnmarkets.com](https://lnmarkets.com) a klikněte na "Open App".



![Page d'accueil LN Markets](assets/fr/01.webp)



### Vytvoření účtu



Uvítací obrazovka nabízí několik způsobů připojení:



![Méthodes de connexion](assets/fr/02.webp)



**Dostupné možnosti** :


1. **Registrace pomocí blesku wallet** (doporučeno) : LNURL-auth s Phoenix, Breez, Zeus nebo BlueWallet


2. **Registrace pomocí e-mailu**: klasický účet (omezuje zkušenosti s Lightning)


3. **Alby** nebo **Ledger**: rozšíření prohlížeče



### Připojení přes Lightning (LNURL-auth)



Klikněte na možnost "Zaregistrovat se pomocí blesku wallet". Naskenujte QR kód pomocí blesku wallet :



![QR code LNURL-auth](assets/fr/03.webp)



Váš wallet automaticky podepíše kryptografickou žádost a váš účet je vytvořen okamžitě, bez e-mailu nebo hesla. Silné zabezpečení a naprostá anonymita.



### Počáteční konfigurace



![Configuration post-connexion](assets/fr/04.webp)



**Dostupné parametry** :




- Uživatelské jméno**: přizpůsobte si své uživatelské jméno
- Automatické výběry**: aktivujte automatické výběry na wallet po uzavření obchodu
- Dvoufaktorové ověřování**: vylepšené zabezpečení pomocí 2FA
- Dokumentace**: přístup k oficiálním zdrojům



## Prohlídka Interface



Rozhraní LN Markets je rozděleno do několika sekcí přístupných z postranní nabídky:



### Přístrojová deska



![Dashboard](assets/fr/06.webp)



Zobrazuje vaši výkonnost podle typu produktu (křížové futures, izolované futures, opce) s P&L, zobchodovanými objemy a vaším osobním Address Lightning (např. `pivi@lnmarkets.com`).



### Profil



![Profil trader](assets/fr/07.webp)



Podrobné statistiky: počet obchodů, typ obchodníka (SCALPER atd.), medián trvání pozice, rozdělení Long/Short, míra výher, průměry (množství, marže, pákový efekt) a progresivní struktura poplatků podle objemu.



### Obchodování



![Historique des trades](assets/fr/08.webp)



Na kartě Obchody se zobrazuje kompletní historie vašich pozic se všemi důležitými ukazateli: datum vytvoření, směr (Long/Short), velikost pozice (množství), vázaná marže, vstupní a výstupní cena, realizovaný zisk/ztráta (P&L) a obchodní poplatky. Můžete filtrovat podle typu produktu (futures/opce) a exportovat data pro externí analýzu nebo účetnictví.



### Nastavení



![Paramètres de la plateforme](assets/fr/05.webp)



Karta Nastavení nabízí dvě karty: **Účet** a **Interface**.



*karta *Účet**:



Správa účtů s upravitelnými poli :




- Uživatelské jméno**: změňte své uživatelské jméno (např. "pivi") pomocí tlačítka "Aktualizovat"
- E-mail**: přidejte/upravte svou e-mailovou adresu
- Vkladová bitcoinová adresa**: bitcoinová adresa, kterou můžete použít pro vklad prostředků on-chain.



**Tři přepínače konfigurace** :




- Zobrazení v žebříčcích**: zvolte, zda se chcete zobrazit ve veřejných žebříčcích, nebo ne
- Použití adres Taproot**: pro vklady/výběry on-chain použijte adresy Bitcoin Taproot
- Povolit automatické výběry**: aktivujte automatické výběry do wallet Lightning po uzavření obchodu



**Migrace účtu**: Sekce umožňující migraci účtu Lightning na klasické ověřování e-mailem/heslem.



**Session management**: tlačítko "Vymazat relaci a místní data" pro odpojení a vyčištění místních dat prohlížeče.



*karta *Interface**:



Přizpůsobte si uživatelské prostředí pomocí sedmi přepínačů:




- Přeskočit potvrzení příkazu**: deaktivovat potvrzovací modal před provedením obchodu (rychlé obchodování)
- Zobrazit popisky**: zobrazení popisek při najetí na prvky
- Soukromý režim (maskuje citlivé údaje)**: maskuje částky a citlivé údaje v rozhraní (režim soukromí)
- Zobrazit čistý PL v profilu**: zobrazení čistého zisku/ztráty ve veřejném profilu
- Použít ikony jednotek**: zobrazení ikon pro měnové jednotky (sats, $)
- Povolit zvuková oznámení**: aktivace zvukových oznámení pro obchodní události
- Povolit oznámení na ploše**: aktivace oznámení na ploše operačního systému



### Wallet



![Wallet](assets/fr/09.webp)



Bitcoin a syntetické zůstatky v USD s historií vkladů, výběrů, křížových převodů, swapů, financování a správy adres on chain.



### API



![API V3](assets/fr/10.webp)



LN Markets nabízí kompletní API REST (V2 a V3) pro plnou automatizaci obchodování prostřednictvím skriptů nebo botů. Přímo z rozhraní můžete vytvářet klíče API s přizpůsobitelnými oprávněními (pouze pro čtení, obchodování, výběry). Pro snadnou integraci jsou k dispozici oficiální SDK pro TypeScript a Python. Úplná dokumentace ke API V3 je k dispozici na adrese [api.lnmarkets.com/v3](https://api.lnmarkets.com/v3).



## První vklad finančních prostředků



Klikněte na možnost "Deposit". K dispozici jsou tři metody:



![Modal de dépôt](assets/fr/11.webp)



1. **LNURL**: naskenujte kód QR pomocí wallet Lightning


2. **Invoice**: zadejte částku a naskenujte fakturu Lightning


3. **On-Chain**: depo Bitcoin on chain



## Obchodování v praxi



### Obchodování s dlouhými futures: sázka na růst



Na ovládacím panelu klikněte na položku "Futures" a poté na "Isolated". Kliknutím na **"Buy "** otevřete dlouhou pozici.



![Interface Futures Long](assets/fr/12.webp)



Kliknutím na ikonu **kalkulačky** vedle tlačítka "Koupit" zobrazíte kalkulačku pozic:



![Calculateur de position Long](assets/fr/13.webp)



**Konkrétní příklad** :




- Množství**: $100 (velikost pozice)
- Obchodní marže**: 12.(vázaná marže): 336 sats
- Pákový efekt**: 7.(každé 1% BTC = 7,73% z vašeho kapitálu)
- Vstupní cena** : $104,863.5
- Likvidace**: (kritická automatická likvidační cena)
- Výstupní cena**: 110 000 USD (pro výpočet zisku)
- PL** : 4,492 sats (zisk při odchodu za 110 000 USD)



**Scénáře** :




- Nárůst +4,9 %** (110 000 USD) : +4 492 sats zisk (+36,4 %)
- Neutrální** (104 863 USD) : -185 sats (pouze poplatky)
- Pokles o -11,5 %** (92 852 USD): celková likvidace (-100 %)



Obchod potvrdíte kliknutím na tlačítko "Buy". **Dva možné případy** :





- Pokud máte na účtu dostatek likvidity**: zobrazí se přímo potvrzovací modal (obrázek níže). Kliknutím na "Ano" obchod okamžitě provedete.



![Confirmation trade Long](assets/fr/14.webp)





- Pokud nemáte dostatek hotovosti**: místo toho se zobrazí bleskový QR kód. Naskenujte jej pomocí wallet Lightning a zaplaťte požadovanou marži. Obchod se otevře automaticky po přijetí platby



### Obchodování s krátkými futures: sázka na pokles



Kliknutím na **"Sell "** otevřete krátkou pozici (pokud cena klesne, vyhráváte). Otevřete kalkulačku pomocí ikony kalkulačky a nastavte pozici:



![Calculateur de position Short](assets/fr/15.webp)



Kliknutím na tlačítko "Sell" potvrďte. Pokud jde o Long, **dva možné případy**:





- Pokud máte dostatek hotovosti**: režim přímého potvrzení, klikněte na "Ano"
- Pokud nemáte dostatek hotovosti**: zobrazí se bleskový QR kód (obrázek níže). Naskenujte jej pomocí blesku wallet a zaplaťte požadovanou marži:



![Paiement Lightning pour Short](assets/fr/16.webp)



Po přijetí platby Lightning se vaše krátká pozice automaticky otevře. Poté ji můžete spravovat z obchodního rozhraní.



#### Uzavření pozice



Chcete-li uzavřít pozici (dlouhou nebo krátkou), klikněte na **malý křížek v pravém dolním rohu** rozhraní pro správu:



![Interface de clôture](assets/fr/17.webp)



Zobrazí se dialogové okno pro potvrzení uzavření obchodu:



![Confirmation clôture](assets/fr/18.webp)



V modálním okně se zobrazí aktuální P&L (zisk nebo ztráta). Klepnutím na tlačítko "Ano" jej zavřete. Zůstatek se okamžitě přičte (zisk) nebo odečte (ztráta) z vašeho účtu Wallet prostřednictvím aplikace Lightning.



### Obchodní opce Call: podmíněné právo na nákup



Opce nabízejí **riziko omezené** na zaplacené pojistné, bez možnosti likvidace. Call opce vám dává právo (nikoli povinnost) koupit Bitcoin za realizační cenu před vypršením platnosti. Na rozdíl od futures nemůžete nikdy ztratit více než investované prémium.



Na hlavním panelu klikněte na možnost "Možnosti" a poté vyberte kartu "Volání".



![Interface Options Call](assets/fr/19.webp)



Nakonfigurujte svůj obchod s následujícími parametry:




- Množství**: $100 (velikost vaší smlouvy)
- Platnost** : 2025-11-15 (datum vypršení platnosti)
- Stávka**: uSD (cílová cena)



Ostatní pole se vypočítají automaticky:




- Marže**: 1.(splatné pojistné, vaše investice)
- Zlomová hodnota**: (cena, za kterou získáte zpět svůj podíl)
- Delta**: 40 (citlivost na cenu Bitcoin)



**Jak vypočítat svou výhru?**



Váš zisk závisí na ceně Bitcoin v době expirace. Vzorec: **(cena BTC - strike) × velikost Contract - zaplacené pojistné**.



**Konkrétní příklady** :





- Bitcoin za 96 000 USD** (aktuální cena) : Vnitřní hodnota = 0 USD. **Ztráta: -1,045 sats** (ztrácíte prémii)





- Bitcoin za 97 000 dolarů**: Vnitřní hodnota = (97 000 - 96 000) × 0,00105 BTC = 1,05 USD. Převedeno na sats ≈ 2 175 sats. **Zisk: 2,175 - 1,045 = +1,130 sats** (+108% zisk)





- Bitcoin za 98 000 USD**: vnitřní hodnota = 2 000 USD ≈ 3 224 sats. **Zisk: +2 179 sats** (zisk +208 %)





- Bitcoin za 100 000 USD**: vnitřní hodnota = 4 000 USD ≈ 5 263 sats. **Zisk: +sats** (+403% zisk)





- Bitcoin do 96 000 USD**: Opce je bezcenná. **Omezená ztráta: -1,045 sats**, likvidace není možná



Klikněte na "Buy Call". Zobrazí se dialogové okno s potvrzením:



![Confirmation Call option](assets/fr/20.webp)



Potvrďte opětovným kliknutím na tlačítko "Buy Call". Tato možnost se zobrazí v nabídce "Running Options". Při vypršení platnosti opce LN Markets automaticky vypočítá vnitřní hodnotu a upraví váš zisk/ztrátu.



**Poznámka k prodejním opcím** : Operace je stejná jako u kupní opce, ale v opačném pořadí. U prodejní opce sázíte na to, že cena Bitcoin **poklesne**. Pokud Bitcoin klesne pod vaši realizační hodnotu, vyhráváte; pokud zůstane nad ní, ztrácíte pouze zaplacené pojistné. Výpočet zisků se řídí stejnou logikou: **(Strike - cena BTC) × velikost Contract - zaplacené pojistné**.



### Výběr z fondu Lightning



Klikněte na "Odstoupit":



![Modal de retrait](assets/fr/21.webp)



**Metody** : LNURL, Invoice, Lightning Address, On-Chain.



**Postup Invoice** :


1. Vytvoření faktury Lightning ze zařízení wallet


2. Kopírování faktury (začíná `lnbc...`)


3. Vložte ji do pole LN Markets


4. Potvrďte stažení


5. wallet je připsán za 1-3 sekundy



Žádné poplatky za bleskový výběr, pouze minimální náklady na směrování (v praxi <0,1 %).



## Rizika a osvědčené postupy



**Hlavní rizika** :




- Úplná likvidace**: vysoká páka může během několika minut zničit 100 % marže
- Experimentální služba**: alfa fáze, technologické nejistoty
- Riziko protistrany**: platforma zůstává jedinou protistranou



**Nejlepší postupy** :



1. **Řízení kapitálu**: přijměte strategii řízení rizik přizpůsobenou vašemu profilu. Například: vyčleňte 5 % svých celkových aktiv na obchodování s pákovým efektem, pak riskujte maximálně 1 % tohoto kapitálu na obchod (např.: 1 BTC aktivum → 5 milionů sats na obchod → 50 tisíc sats max. riziko na pozici)



2. **Systematický stop-loss**: nastavte si stop-lossy tak, abyste omezili ztráty na obchod. Například s pravidlem 1 % rizika představuje i 10 po sobě jdoucích ztrátových obchodů pouze 10 % vašeho obchodního kapitálu



3. **Začněte v malém**: nejprve otestujte několik tisíc sátů, abyste pochopili mechanismy, než začnete používat strategii řízení kapitálu



4. **Regulérní výběr zisků**: zajistěte si své zisky na hlavní wallet a ponechte na platformě pouze aktivní obchodní kapitál



5. **Dejte si pozor na pákový efekt**: vyhněte se pákovému efektu >20×, pokud si nejste plně vědomi rizika likvidace



**Náklady**: žádné poplatky za bleskový vklad/výběr, spread ~0,1 % na obchod (klesá na 0,06 % v závislosti na objemu).



## Výhody a omezení



**Výhody** :




- Nepověřené osoby (celková kontrola bez období obchodování)
- Bez KYC (anonymita prostřednictvím Lightning/Nostr)
- Okamžité zúčtování (vklady/výběry během několika sekund)
- Realizace s nulovým skluzem s agregací likvidity
- Veřejná podpora API a Nostr



**Omezení** :




- Služba alfa (možné evoluce)
- Nižší likvidita než u Binance/Deribit
- Zakázáno pro obyvatele USA



## Závěr



LN Markets představuje zásadní vývoj obchodování Bitcoin tím, že nativně integruje Lightning Network a vrací kontrolu zpět uživatelům. Pro zdatné bitcoináře, kteří chtějí spekulovat, aniž by ohrozili svou suverenitu, je to jedinečná alternativa k tradičním centralizovaným burzám.



Platforma se nadále vyvíjí a v současné době probíhá vývoj lineárních futures kontraktů USDT a obchodování bez custodialu prostřednictvím Discreet Log Contracts (DLC). Uplatňováním správných postupů řízení rizik (malé částky, stop-loss, pravidelné výběry) se LN Markets stává mocným nástrojem pro zodpovědné zkoumání pákového efektu Bitcoin.



Začněte v malém, vyzkoušejte několik tisíc dat a postupně prozkoumejte tuto novou hranici Lightning Network. Šťastné suverénní obchodování ⚡️!



## Zdroje





- [oficiální stránky LN Markets](https://lnmarkets.com)
- [Dokumentace](https://docs.lnmarkets.com)