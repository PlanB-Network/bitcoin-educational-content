---
name: Zeus Swap
description: Služba Exchange bez úschovy mezi bitcoiny On-Chain a Lightning Network
---

![cover](assets/cover.webp)



Ekosystém Bitcoin představuje dualitu: hlavní síť (On-Chain) nabízí maximální zabezpečení, zatímco Lightning Network umožňuje okamžité transakce. Tato architektura dvou Layer vytváří praktickou výzvu: jak lze efektivně převádět finanční prostředky mezi těmito dvěma vrstvami bez centralizovaných prostředníků?



Problém je konkrétní: obdržíte platbu Lightning, ale chcete ji mít v úložišti Cold, nebo naopak máte bitcoiny On-Chain, ale potřebujete likviditu Lightning. Tradiční řešení zahrnují ruční otevírání/zavírání kanálů Lightning (nákladné a technické) nebo centralizované platformy vyžadující KYC.



Zeus Swap tento problém řeší pomocí automatizované služby Exchange, která není určena k zadržování. Vyvinula ji společnost Zeus LSP a umožňuje vám obousměrně převádět bitcoiny On-Chain na satoši Lightning, aniž byste své prostředky svěřili zprostředkovateli. Proces využívá atomické kontrakty (HTLC), které zaručují, že Exchange bude buď dokončen, nebo zrušen.



Inovace spočívá v jednoduchosti: stačí jen několik kliknutí pro Exchange, který zachovává vaši finanční suverenitu, bez nutnosti registrace nebo KYC.



## Co je Zeus Swap?



Zeus Swap je služba likvidity Exchange vyvinutá společností Zeus LSP, která umožňuje atomické výměny mezi hlavní sítí Bitcoin a Lightning Network. Jedná se o technickou infrastrukturu, která využívá podmořské swapy a reverzní swapy k usnadnění obousměrné konverze mezi On-Chain BTC a bleskovými satoši, přičemž je zachována nekustodiální povaha operace.



### Technická architektura



Zeus Swap využívá Boltzovu open-source technologii Bitcoin/Lightning atomic swap. Protokol používá časově uzamčené kontrakty Hash (HTLC): kontrakty uzamykající finanční prostředky se dvěma podmínkami uvolnění (odhalení kryptografického tajemství nebo uplynutí času).



Při podmořské výměně (On-Chain → Lightning) uživatel pošle bitcoiny do Address, který obsahuje Hash z Invoice Lightning. Zeus LSP tyto prostředky odemkne pouze zaplacením odpovídajícího Invoice, čímž odhalí předobraz, který bitcoiny automaticky odemkne. Tento mechanismus zaručuje atomicitu.



Při zpětné výměně (Lightning → On-Chain) uživatel zaplatí Lightning Invoice z Zeus LSP, čímž odhalí předběžný obraz umožňující uvolnění připravené transakce Bitcoin do cílového Address.



Podrobnější informace o tom, jak Lightning Network funguje, naleznete v našem specializovaném kurzu :



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Obchodní model



Zeus LSP působí jako tvůrce trhu, udržuje likviditu On-Chain a Lightning, aby mohl plnit swapy. U swapů Zeus uplatňuje variabilní poplatek (obvykle 0,1 % až 0,5 % v závislosti na směru a podmínkách) plus poplatek Bitcoin Mining, transparentně zobrazený před validací.



Jako poskytovatel bleskových služeb Zeus optimalizuje náklady díky svým odborným znalostem v oblasti otevírání kanálů na vyžádání, efektivního směrování a řešení likvidity na míru.



### Integrace



Zeus Wallet nativně integruje tuto službu a umožňuje výměnu bez nutnosti opustit Interface Bitcoin/Lightning. Tím se eliminuje tření při kopírování a vkládání mezi aplikacemi.



Nezávislý web Interface zůstává přístupný všem peněženkám, což zaručuje maximální flexibilitu použití.



## Hlavní funkce



### Obousměrné výměny



Zeus Swap nabízí dva typy Exchange:



**Výměna ponorek (On-Chain → Blesk)**: vstřikování bleskové likvidity ze zásob Bitcoin, užitečné pro napájení mobilního uzlu Wallet nebo Blesku bez ručního otevírání kanálů.



**Reverzní swapy (Lightning → On-Chain)**: přeměňte satoši Lightning na bitcoiny On-Chain pro dlouhodobé uložení, abyste se vyhnuli nákladnému uzavírání kanálů.



### Uživatelská rozhraní



**Interface web** (swaps.zeuslsp.com): zjednodušené prostředí bez registrace, průvodce procesem se zobrazením poplatků a stavu v reálném čase.



** Integrace se systémem Zeus Wallet**: přímé výměny z aplikace, automatická správa faktur a adres, eliminace chyb při zpracování.



### Bezpečnost a zotavení



Každá výměna generuje jedinečný kód Contract s neměnnými parametry: Hash Lightning, timeout, náhrada Address. V případě selhání probíhá automatická obnova prostřednictvím poskytovaného Address nezávisle na Zeus LSP.



**Zeus Swaps Rescue Key**: při výměně On-Chain → Lightning Zeus automaticky vygeneruje univerzální klíč pro obnovení, který nahradí staré jednotlivé soubory náhrady. Tento jedinečný klíč funguje na jakémkoli zařízení a pro všechny s ním vytvořené výměny. Tento klíč je nezbytné stáhnout a uložit na bezpečné místo, abyste mohli v případě selhání swapu obnovit své prostředky.



### Optimalizace sítě



Zeus Swap automaticky upravuje dobu platnosti a poplatky Mining podle podmínek v síti. Uživatelé služby Zeus mohou využívat pokročilé možnosti: výběr LSP, vlastní zpoždění, kompatibilitu s dalšími službami (Boltz).



## Instalace a použití



### Přístupové metody



**Interface web** (swaps.zeuslsp.com): univerzální řešení kompatibilní se všemi peněženkami, bez nutnosti instalace, ideální pro příležitostné použití.



**Aplikace Zeus** (iOS/Android): integrovaný zážitek kombinující Wallet a swapy, vhodný pro běžné uživatele.



Další informace o tomto kompletním systému Wallet naleznete v našem výukovém programu Zeus:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Webová konfigurace



**On-Chain → Blesk**: Proces začíná konfigurací swapu na webu Zeus Swap Interface. Uživatel může pomocí šipky mezi poli On-Chain a Lightning obrátit směr výměny.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: výběr částky (Sats 50 000 → Sats 49 648 po odečtení poplatků) s transparentním zobrazením síťových poplatků (Sats 302) a služby Zeus (Sats 50).*



Během procesu vám Zeus nabídne stažení univerzálního klíče pro obnovení:



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Dialogové okno pro stažení záchranného klíče Zeus Swaps - univerzálního klíče, který nahradí staré soubory s jednotlivými úhradami*



Pokud již klíč máte, Zeus vám umožní jej zkontrolovat:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface pro kontrolu platnosti existujícího záchranného klíče Zeus Swaps*



Po konfiguraci Zeus vygeneruje depot Bitcoin Address a zobrazí pokyny :



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Stránka pro dokončení výměny: QR kód a Bitcoin Address pro zaslání 50 000 Sats, s připomínkou 24hodinového data vypršení platnosti*



Výměna pak čeká na potvrzení Bitcoin:



![Attente de confirmation](assets/fr/05.webp)



*Stav "Transakce v Mempool" - čeká se na potvrzení Bitcoin pro dokončení výměny*



Po potvrzení se výměna automaticky dokončí:



![Swap réussi](assets/fr/06.webp)



*Potvrzení úspěchu: 49 648 Sats obdržených v Blesku po odečtení síťových a servisních poplatků*



### Používání aplikace Zeus



**Blesk → On-Chain**: Aplikace Zeus nabízí integrovanou zkušenost s reverzními výměnami (Lightning až Bitcoin).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Hlavní obrazovka Zeus zobrazující zůstatky Lightning (69 851 Sats) a On-Chain (38 018 Sats), přístup k výměnám přes boční menu*



![Configuration du swap reverse](assets/fr/08.webp)



*Vytvoření reverzní výměny Interface: gW-69, s jasně zobrazenými síťovými poplatky (530 Sats) a službami (250 Sats). Uživatelé mohou buď ručně zadat Bitcoin přijímající Address, nebo generate automaticky z Wallet Zeus prostřednictvím tlačítka "generate On-Chain Address"*



![Finalisation du swap mobile](assets/fr/09.webp)



*Finalizační obrazovky: Invoice s nápisem "PAY THIS Invoice", potvrzení o úspěšné platbě Lightning za 9,96 sekundy a výpis zůstatku, na kterém čeká 49 162 Sats*



### Dohled a zabezpečení



Každá výměna má jedinečný identifikátor se sledováním v reálném čase. Úplné zobrazení průběhu, automatická upozornění na data vypršení platnosti. Automatická doporučení pro nabíjení podle podmínek sítě.



## Výhody a omezení



### Výhody





- Jednoduchost**: Výměna na několik kliknutí oproti ruční manipulaci s kanály
- Bez úschovy**: žádné KYC, žádný účet, finanční prostředky nikdy nesvěřené třetí straně
- Transparentnost**: poplatky se explicitně zobrazují před validací (0,1 % až 0,5 % + minima v závislosti na uživatelských testech - aktuální poplatky si ověřte při každé výměně)
- Integrace mobilních zařízení**: nativní prostředí v Zeus Wallet



### Omezení





- Doba platnosti**: pokud Bitcoin není potvrzen včas, je možné jej zrušit
- Limity částek**: minimálně 25 000 Sats, likvidita Zeus LSP se mění podle podmínek
- Stopy On-Chain**: Skripty HTLC potenciálně identifikovatelné analýzou Blockchain
- Požadované potvrzení**: minimálně 10 minut pro ověření platnosti Bitcoin



## Osvědčené postupy



### Načasování a náklady





- Sledujte prostor Mempool.space v době nízkého přetížení
- Preferují víkendy a hodiny mimo špičku, aby se snížily náklady na Mining
- Výpočet ziskovosti: malé částky vs. přímé otevření kanálu



### Zabezpečení





- Pečlivě zkontrolujte adresy Bitcoin (doporučujeme kopírovat a vkládat)
- Zálohování záchranného klíče Zeus Swaps**: stáhněte a uložte klíč k obnovení na bezpečném místě
- Dokument: Contract ID, náhrada Address, datum ukončení platnosti
- Pro včasné potvrzení použijte příslušné poplatky Mining



### Strategie používání





- Vyvážení On-Chain/Lightning liquidity podle vašich potřeb
- Zeus Swap pro jednorázové úpravy, přímé kanály pro trvalé potřeby



## Srovnání s jinými swapovými službami



### Zeus Swap vs Boltz Exchange



Zeus Swap využívá technologii Boltzova backendu, ale přináší několik zásadních vylepšení:



**Zeus Swap výhody** :




- Interface unified**: nativní integrace v systému Zeus Wallet vs Interface webová technika Boltz
- WebSocket API**: aktualizace v reálném čase vs. ruční dotazování
- Automatizovaná správa**: automatická fakturace a správa Address
- Podpora mobilních zařízení**: optimalizace pouze pro chytré telefony a stolní počítače
- Dokumentace Swagger**: kompletní rozhraní REST API pro vývojáře



**Boltz zůstává výhodný** pro naprostou nezávislost a použití s jakoukoli sestavou Bitcoin/Lightning.



Zeus Swap transformuje osvědčenou technologii Boltz do běžného uživatelského prostředí, srovnatelného s rozdílem mezi surovým protokolem a uživatelsky přívětivou aplikací.



### Zeus Swap vs Phoenix/Breez (integrované swapy)



Systémy Phoenix a Breez integrují transparentní funkce výměny, které před koncovým uživatelem skrývají technickou složitost. Phoenix používá automatický systém swap-in/swap-out, kdy uživatel explicitně nerozlišuje mezi vrstvami Bitcoin: "pošle do Bitcoin Address" a aplikace se o swap postará na pozadí.



Tento velmi zjednodušený přístup je dokonale vhodný pro začátečníky, ale omezuje pochopení a kontrolu operací. Zeus Swap uplatňuje více vzdělávací filozofii: uživatelé chápou, že vyměňují mezi dvěma různými vrstvami, a postupně rozvíjejí své chápání ekosystému dvou Layer Bitcoin.



## Podrobné srovnání poplatků a limitů (2024)



⚠️ **Upozornění**: Poplatky se mohou v průběhu času měnit v závislosti na tržních podmínkách a aktualizacích služeb. Před potvrzením výměny vždy zkontrolujte poplatky zobrazené v Interface.



| Service | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Montant minimum |
|---------|-------------------------|----------------------|-----------------|
| **Zeus Swap** | ~0.1% + frais minage | 0.5% + frais minage | 25 000 sats |
| **Boltz** | 0.2% + frais minage | 0.5% + frais minage | 50 000 sats |
| **Phoenix** | Frais minage uniquement | 0.4% fixe | 10 000 sats |
| **Breez** | 0.25% + frais réseau | 0.5% + frais minage | 50 000 sats |

Zeus Swap nabízí rovnováhu mezi snadným používáním a technickou kontrolou: je přístupnější než Boltz, flexibilnější než Phoenix/Breez, s přísným neomezujícím přístupem.



## Závěr



Zeus Swap představuje významnou inovaci v ekosystému Bitcoin, která elegantně řeší problém interoperability mezi hlavní sítí a Lightning Network. Kombinací kryptografické robustnosti atomických swapů s přístupným uživatelským prostředím tato služba demokratizuje správu duálních Bitcoin a Layer, aniž by byly ohroženy zásady finanční suverenity.



Architektura Zeus Swap, která není založena na svěřeneckém právu a která je dědictvím osvědčené technologie Boltz, zajišťuje, že vaše finanční prostředky zůstanou pod vaší výhradní kontrolou po celou dobu procesu swapu. Tento přístup respektuje ducha směrnice Bitcoin a zároveň nabízí uživatelský komfort potřebný pro běžné přijetí. Cenová transparentnost a absence procesů KYC posilují tuto jedinečnou nabídku hodnoty.



Pro moderního uživatele Bitcoin je Zeus Swap strategickým nástrojem pro optimalizaci rozdělování likvidity podle potřeb: On-Chain bezpečné úložiště pro dlouhodobé úspory, blesková dostupnost pro denní výdaje a mikrotransakce. Tato flexibilita mění správu Bitcoin z technického omezení v konkurenční výhodu.



Budoucí vývoj systému Zeus Swap, podporovaný zkušeným týmem Zeus LSP a komunitou open-source společnosti Boltz, slibuje další zlepšování nákladů, doby zpracování a uživatelského komfortu. Tato služba je součástí širšího trendu vyzrávání infrastruktury Bitcoin, kdy se technická vyspělost stává pro koncového uživatele transparentní.



## Zdroje



### Oficiální dokumentace




- [Zeus Swap - Webový portál](https://swaps.zeuslsp.com)
- [Zeus Wallet - Mobilní aplikace](https://zeusln.app)
- [Blog Zeus - Oznámení a návody](https://blog.zeusln.com)
- [Technická dokumentace k systému Zeus](https://docs.zeusln.app)



### Společenství a podpora




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegram Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)