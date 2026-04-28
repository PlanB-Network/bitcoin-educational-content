---
name: Silentium
description: Progresivní web wallet s podporou tichých plateb (BIP-352)
---

![cover](assets/cover.webp)



Opakované použití adres Bitcoin je jednou z nejpřímějších hrozeb pro důvěrnost uživatelů. Pokud příjemce sdílí jednu adresu pro příjem více plateb, může jakýkoli pozorovatel vysledovat všechny související transakce a rekonstruovat jejich finanční historii. Tento problém se týká zejména tvůrců obsahu, charitativních organizací nebo aktivistů, kteří chtějí veřejně zobrazit adresu pro dary, aniž by ohrozili své soukromí.



Společnost Silentium na tento problém reaguje elegantním řešením přístupným přímo z prohlížeče. Tato open-source progresivní webová aplikace (PWA), kterou v květnu 2024 spustil Louis Singer, implementuje Silentium Payments (BIP-352): opakovaně použitelnou statickou adresu, kde každá platba končí na samostatné adrese blockchainu, bez předchozí interakce nebo pozorovatelné vazby mezi transakcemi.



**Důležité upozornění**: Silentium je experimentální projekt sloužící jako *důkaz konceptu* pro lehké peněženky společnosti Silent Payments. Neměl by být používán jako každodenní wallet nebo pro ukládání významných částek. Vývojáři to výslovně uvádějí:



> Používání na vlastní nebezpečí.

Všimněte si, že tento wallet lze použít jako testnet nebo regtest.



## Co je Silentium?



### Filozofie a cíle



Silentium slouží jako technická ukázka implementace tichých plateb v lehkém prohlížeči wallet. Přestože podporuje i běžné adresy Bitcoin, důraz je kladen na Tiché platby, aby uživatelé mohli s touto technologií ochrany soukromí jednoduše experimentovat.



### Jak fungují tiché platby?



Tiché platby (BIP-352) používají eliptickou křivku Diffie-Hellmanova klíče Exchange (ECDH). Příjemce vygeneruje statickou adresu (`sp1...` v mainnet, `tsp1...` v testnetu), která se skládá ze dvou veřejných klíčů: skenovacího klíče pro detekci plateb a výdajového klíče pro jejich použití.



Odesílatel zkombinuje své soukromé vstupní klíče se skenovacím klíčem příjemce a vypočítá sdílené tajemství, čímž vytvoří kryptografický "tweak". Tento tweak přidaný k výdajovému klíči vytvoří pro každou transakci jedinečnou adresu Taproot. Příjemce reprodukuje tento výpočet pomocí svého soukromého skenovacího klíče, aby zjistil a utratil prostředky bez předchozí interakce.



Výhody: zvýšená důvěrnost pro odesílatele i příjemce, není nutný server třetí strany, transakce jsou k nerozeznání od běžných plateb Taproot. Hlavní nevýhoda: intenzivní skenování blockchainu za účelem detekce plateb.



Chcete-li se dozvědět více o teoretickém fungování tichých plateb, podívejte se na poslední část kurzu BTC,204 na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Podporované platformy



Silentium je progresivní webová aplikace (PWA) přístupná z jakéhokoli moderního prohlížeče (mobilního nebo desktopového). Můžete ji používat přímo na `app.silentium.dev`, nainstalovat ji jako nativní aplikaci přes prohlížeč nebo ji nasadit lokálně. Instalace se provádí přímo z prohlížeče, bez nutnosti procházet oficiálními obchody.



## Používání webové aplikace



### Přístup a instalace



[V prohlížeči přejděte na `https://app.silentium.dev/`](https://app.silentium.dev/). Aplikace se okamžitě načte a zobrazí domovskou obrazovku.



Chcete-li ji nainstalovat jako nativní aplikaci v systému iOS, stiskněte tlačítko sdílení (čtverec se šipkou nahoru) a vyberte možnost "Na domovské obrazovce". V systému Android prohlížeč obvykle přímo nabízí oznámení "Přidat na domovskou obrazovku". Po instalaci se aplikace Silentium zobrazí s vyhrazenou ikonou a funguje jako nativní aplikace, ale pro synchronizaci transakcí vyžaduje připojení k internetu.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Vytvoření portfolia



Při prvním spuštění vyberte možnost "Vytvořit Wallet" pro vytvoření nového portfolia generate nebo "Obnovit Wallet" pro obnovení z existující fráze pro obnovení.



Vyberte možnost "Vytvořit Wallet". Aplikace vygeneruje frázi o 12 slovech, kterou musíte pečlivě zapsat. Tato fráze je jediným způsobem, jak získat zpět své finanční prostředky. I na testnetu si osvojte správné postupy zálohování. Po uložení fráze stiskněte tlačítko "Pokračovat".



Aplikace vás poté vyzve k nastavení hesla pro zabezpečení přístupu do zařízení wallet. Zvolte silné heslo a potvrďte jej.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Po potvrzení fráze a nastavení hesla budete přesměrováni do hlavního rozhraní.



### Interface hlavní a parametry



Hlavní rozhraní zobrazuje váš zůstatek v satoši (zpočátku 0 sats) a ve spodní části jsou tři tlačítka:




- Sync**: synchronizuje wallet s blockchainem
- Receive**: přijímat finanční prostředky
- Odeslat**: odeslání bitcoinů



Přístup do Nastavení získáte přes ikonu vpravo nahoře (tři vodorovné pruhy). Nabídka Nastavení nabízí několik možností:





- O**: informace o aplikaci
- Záloha**: záloha fráze pro obnovení
- Průzkumník**: vyberte průzkumníka blockchainu (ve výchozím nastavení Mempool) a server Silentiumd
- Síť**: výběr sítě (mainnet/testnet)
- Heslo**: změna hesla
- Reload**: opětovné nabití wallet
- Obnovení**: úplné obnovení
- Téma**: změna tématu



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



Sekce **Explorer** je obzvláště důležitá: umožňuje zvolit použitý blockchain explorer (ve výchozím nastavení Mempool) a také zobrazuje URL adresu serveru Silentiumd (`https://bitcoin.silentium.dev/v1` pro mainnet). Pokud hostujete vlastní server Silentiumd nebo chcete používat testnet, je to místo, kde tyto parametry nastavujete.



### Přijímání finančních prostředků



V hlavním rozhraní stiskněte tlačítko "Receive". Ve výchozím nastavení Silentium zobrazí adresu tiché platby s jejím QR kódem. Adresa začíná `sp1...` na mainnet nebo `tsp1...` na testnetu.



Mezi tichou platbou a klasickou adresou Bitcoin můžete přepínat pomocí tlačítka "Přepnout na klasickou adresu" / "Přepnout na tichou adresu" ve spodní části obrazovky.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Po odvysílání transakce vyčkejte několik minut. V případě tichých plateb společnost Silentium automaticky skenuje blockchain a hledá transakce určené pro vás. Transakce se zobrazují se stavem "Nepotvrzeno" a poté jsou postupně potvrzovány.



### Odeslat platbu



V hlavním rozhraní stiskněte tlačítko "Odeslat". Na obrazovce odeslání se zobrazí dotaz :



1. **Address**: vložte adresu tiché platby (`sp1...` nebo `tsp1...`) nebo klasickou adresu Bitcoin. Ke skenování adresy můžete použít ikonu QR skenování.


2. **Částka**: zadejte částku v satoších, která má být odeslána. Pro snadné zadávání se zobrazí číselná klávesnice. Váš disponibilní zůstatek se pro informaci zobrazuje v horní části.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Po zadání adresy a částky pokračujte stisknutím tlačítka "Proceed". Před potvrzením transakce vás aplikace vyzve k výběru požadované výše poplatku.



## wallet self-hosting



### Proč hostovat na vlastní pěst?



Místní hosting společnosti Silentium nabízí naprostou suverenitu, ověřování kódu, vývojové prostředí a odolnost vůči výpadkům oficiálních stránek.



### Předpoklady



Node.js (verze 14+), npm nebo yarn, Git a přibližně 500 MB místa na disku.



### Místní instalace



Klonujte úložiště a nainstalujte :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Spuštění a použití



Spusťte aplikaci v režimu vývoje:



```bash
yarn start
```



V prohlížeči přejděte na adresu `http://localhost:3000`. Pro optimalizovanou produkční verzi :



```bash
yarn build
```



Soubory vygenerované v `build/` lze obsluhovat pomocí nginx, Apache nebo jiného webového serveru. Ve výchozím nastavení se Silentium připojuje k veřejnému serveru `bitcoin.silentium.dev`. Změňte toto nastavení v parametrech a použijte testnet nebo vlastní server.



## Server Silentiumd



### Úloha a fungování



Společnost Silentium používá indexovací server **Silentiumd** k optimalizaci detekce plateb. Skenování všech transakcí Taproot by bylo pro prohlížeč nebo mobilní telefon příliš těžkopádné.



Silentiumd pro každou transakci Taproot předem vypočítá mezidata (tweaky). Váš wallet stáhne tato vylepšení (několik bajtů na transakci) a provede konečný výpočet lokálně, čímž ověří vlastnictví platby. Na rozdíl od běžných serverů Electrum server nikdy nezná vaše klíče ani nemůže identifikovat vaše transakce.



Kompaktní filtry BIP158 umožňují vašemu zařízení wallet určit, které bloky mají být prohledány, aniž by byly odhaleny vaše adresy, čímž je zachována vaše důvěrnost.



### Veřejný server



Veřejný server `bitcoin.silentium.dev` (mainnet), sponzorovaný společností Vulpem Ventures, nabízí jednoduché a okamžité zkušenosti. Přestože je zachována důvěrnost, tento přístup předpokládá relativní důvěru v infrastrukturu třetí strany.



### Hostování vlastního serveru Silentiumd



Chcete-li získat naprostou suverenitu, hostujte vlastní server Silentiumd. Předpoklady: Jádro Bitcoin s neelagovaným uzlem s `txindex=1` a `blockfilterindex=1`, Go 1.21+, 10-20 GB místa na disku, znalost správy systému.



**Instalace:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Konfigurace pomocí proměnných prostředí (podrobnosti naleznete v souboru `config.md` úložiště). Server indexuje blockchain a vystavuje API, který může být dotazován vaším wallet.



V současné době neexistují žádná balíková řešení pro Umbrel nebo Start9, což omezuje přístupnost pro netechnické uživatele.



## Výhody a omezení



### Nejdůležitější informace





- Maximální dostupnost**: použití z libovolného prohlížeče, bez nutnosti náročné instalace
- Multiplatformní**: díky technologii PWA funguje na mobilních zařízeních (Android/iOS) i na stolních počítačích
- Jednoduchý selfhosting**: místní instalace pomocí několika příkazů
- Open-source**: plně auditovatelný kód na GitHubu
- Zaměření na ochranu soukromí**: žádné sledování, žádná analytika, místní kryptografické výpočty
- Oddělená architektura**: jasné oddělení mezi wallet (klientem) a indexovacím serverem
- Bez účtu**: není nutná registrace ani osobní údaje



### Omezení, která je třeba zvážit





- Experimentální projekt**: pouze ověření konceptu, není určen pro každodenní použití nebo výrobu
- Žádné záruky**: riziko chyb, zranitelností, možné ztráty finančních prostředků
- Omezená podpora**: málo uživatelské dokumentace, malá komunita, žádná oficiální podpora
- Závislost na serveru**: vyžaduje funkční server Silentiumd (veřejný nebo samostatně hostovaný)
- Intenzivní skenování**: Tichá detekce plateb spotřebovává šířku pásma
- Omezené funkce**: žádné ovládání mincí, žádný Lightning, žádné vícepodpisy



## Osvědčené postupy



### Bezpečnost seed



I na testnetu berte frázi o zotavení vážně. Zapište si ji a uschovejte na bezpečném místě. Mějte oddělené peněženky pro testnet a mainnet: nikdy nepoužívejte testovací seed na wallet určené pro skutečné prostředky.



### Ověření zdrojového kódu



Jednou z výhod vlastního hostingu je možnost zkontrolovat zdrojový kód před jeho spuštěním. Pokud plánujete používat Silentium se skutečnými prostředky, věnujte čas kontrole kódu nebo si k tomu přizvěte důvěryhodného vývojáře. Porovnejte také hash kódu nasazeného na `app.silentium.dev` s hashem repozitáře GitHub, abyste se ujistili o jeho pravosti.



### Zálohování a obnovení



Tiché vymáhání prostředků vyžaduje zařízení wallet kompatibilní s protokolem BIP-352. Standardní wallet nemůže skenovat blokový řetězec a získat tak vaše Tiché platby UTXO. Mějte nainstalovaný systém Silentium nebo se ujistěte, že máte přístup k jinému kompatibilnímu systému wallet (například Cake Wallet nebo jiné budoucí implementace), abyste mohli v případě potřeby obnovit své prostředky.



## Závěr



Silentium poskytuje přístupný testovací prostor pro pochopení tichých plateb bez technických potíží. Jako ukázka konceptu demonstruje, jak lze tuto technologii ochrany soukromí integrovat do prohlížeče wallet a zároveň zachovat vlastní úschovu. Experimentujte na testnetu a objevte tento slibný průlom v oblasti soukromí on-chain.



## Zdroje



### Oficiální dokumentace




- Úložiště Silentium GitHub (wallet): https://github.com/louisinger/silentium
- Úložiště Silentiumd GitHub (server): https://github.com/louisinger/silentiumd
- Webová aplikace: https://app.silentium.dev/
- Komunitní stránky Silent Payments: https://silentpayments.xyz
- Specifikace BIP-352: https://bips.dev/352



### Články a zdroje




- Oficiální oznámení (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Tiché platby: https://bitcoinops.org/en/topics/silent-payments/



### Nástroje Testnet




- Baterie Testnet: https://testnet-faucet.com/
- Mempool testnet explorer: https://mempool.space/testnet