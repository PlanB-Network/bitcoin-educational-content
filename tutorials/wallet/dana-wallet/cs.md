---
name: Dana Wallet
description: Minimalistické portfolio pro tiché platby (BIP-352)
---

![cover](assets/cover.webp)



Opakované použití adres Bitcoin je jednou z nejpřímějších hrozeb pro důvěrnost uživatelů. Pokud příjemce sdílí jednu adresu pro příjem více plateb, může jakýkoli pozorovatel vysledovat všechny související transakce a rekonstruovat jejich finanční historii. Tento problém se týká zejména tvůrců obsahu, charitativních organizací nebo aktivistů, kteří chtějí veřejně zobrazit darovací adresu, aniž by ohrozili soukromí své nebo svých dárců.



Dana Wallet na tento problém reaguje elegantním řešením: Tiché platby. Tento minimalistický open-source wallet, spuštěný v roce 2024, generuje opakovaně použitelnou statickou adresu a zároveň zaručuje, že každá přijatá platba skončí na samostatné adrese v blockchainu. Odesílatel nepotřebuje žádnou předchozí interakci s příjemcem a žádný vnější pozorovatel nemůže jednotlivé transakce propojit. V blockchainu tyto platby vypadají jako zcela běžné transakce Taproot.



Dana Wallet je k dispozici v Mainnet a Signet, ale vývojáři ji stále považují za experimentální a doporučují nevkládat prostředky, které nejste připraveni prohrát. V tomto návodu použijeme verzi pro Signet, abychom objevili Tiché platby, aniž bychom riskovali skutečné prostředky.



## Co je Dana Wallet?



### Filozofie a cíle



Dana Wallet používá přístup "SP-first": wallet generuje výhradně adresy tichých plateb a přijímá pouze tento typ plateb. Pomocí této aplikace nebude možné vytvořit klasickou adresu Bitcoin (starší, standardní SegWit nebo Taproot). Toto záměrné omezení vám umožní plně se soustředit na studium protokolu BIP-352, aniž byste byli rozptylováni jinými funkcemi. Nepřehledné rozhraní záměrně upřednostňuje snadné používání před množstvím možností, takže nástroj je přístupný i uživatelům, kteří s koncepcí důvěrnosti on-chain teprve začínají.



Projekt je kompletně open-source, vyvinutý s využitím Flutteru pro mobilní rozhraní a Rust pro vnitřní kryptografickou logiku. Tato architektura kombinuje plynulé uživatelské prostředí s optimálním výkonem pro intenzivní operace skenování.



### Jak fungují tiché platby?



Tiché platby (BIP-352) jsou založeny na sofistikovaném kryptografickém mechanismu využívajícím eliptickou křivku Diffie-Hellmanova klíče Exchange (ECDH). Příjemce generuje statickou adresu (začínající `sp1...` v mainnet nebo `tsp1...` v Signetu), která se skládá ze dvou různých veřejných klíčů: skenovacího klíče ($B_{scan}$) pro detekci příchozích plateb a výdajového klíče ($B_{spend}$) pro utrácení přijatých prostředků. Toto oddělení umožňuje uchovávat výdajový klíč na hardwaru wallet a zároveň používat skenovací klíč na připojeném zařízení.



Když chce odesílatel provést platbu, jeho wallet zkombinuje součet soukromých klíčů svých vstupů s veřejným skenovacím klíčem příjemce a vypočítá sdílený tajný klíč ECDH. Toto tajemství generuje kryptografický "tweak", který po přidání k výdajovému klíči příjemce vytvoří jedinečnou adresu Taproot pro danou transakci.



Příjemce může tento výpočet reprodukovat pomocí svého soukromého skenovacího klíče a veřejných klíčů viditelných v transakci (Diffie-Hellmanova matematická vlastnost). To mu umožňuje zjistit a utratit finanční prostředky bez předchozí interakce s odesílatelem.



Tento přístup nabízí několik výhod:




- Důvěrnost příjemce**: každá platba končí na jiné adrese
- Důvěrnost odesílatele**: žádný trvalý identifikátor spojující platby
- Žádný server třetí strany**: protokol funguje samostatně
- Nerozlišitelné transakce**: Tiché platby vypadají jako běžné transakce Taproot



Hlavní nevýhodou jsou náklady na skenování: příjemce musí analyzovat každou novou transakci Taproot, aby odhalil ty, které jsou určeny jemu.



Pokud se chcete dozvědět více o technickém fungování tichých plateb, doporučujeme kurz BTC204 o důvěrnosti v Bitcoin, který obsahuje kapitolu věnovanou tichým platbám:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Podporované platformy



Dana Wallet je k dispozici jako aplikace pro Android. APK lze stáhnout prostřednictvím specializovaného úložiště F-Droid, které poskytli vývojáři, prostřednictvím Obtainium nebo přímo z GitHubu. Pro uživatele Linuxu je technicky možné zkompilovat aplikaci Flutter pro desktop.



Aplikace není dostupná v systému iOS ani v oficiálních obchodech (Google Play, App Store), což odráží její experimentální status a zaměření na technické publikum.



## Instalace



### Základní předpoklady



Chcete-li nainstalovat Danu Wallet do systému Android, potřebujete zařízení se systémem Android, které má v nastavení zabezpečení povolenou možnost "Neznámé zdroje". Není vyžadován žádný účet ani registrace.



### Přidat zálohu F-Cold



Doporučenou metodou je přidání specializovaného úložiště F-Droid Dana Wallet. Přejděte na stránku `fdroid.silentpayments.dev`, kde najdete odkaz na úložiště a QR kód, který můžete naskenovat. Úložiště v současné době nabízí 3 aplikace: verzi Mainnet, vývojovou verzi a Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Instalace přes F-Droid



Otevřete aplikaci F-Droid v zařízení se systémem Android a poté vstupte do Nastavení pomocí ikony vpravo dole. Chcete-li spravovat zdroje aplikací, vyberte možnost "Úložiště". Stisknutím tlačítka "+" přidejte nové úložiště a poté naskenujte QR kód nebo vložte odkaz `https://fdroid.silentpayments.dev/fdroid/repo`. Po přidání úložiště se zobrazí tři dostupné verze aplikace Dana Wallet. Vyberte možnost "Dana Wallet - záložka" a stiskněte tlačítko "Instalovat".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Počáteční konfigurace



### Vytvoření portfolia



Při prvním spuštění se na obrazovce Dana Wallet zobrazí uvítací obrazovka s informacemi o jejím poslání: "Posílejte a přijímejte dary bez prostředníků". Pro pokračování stiskněte tlačítko "Begin". Další obrazovka představuje tři hlavní výhody aplikace:




- Darování bez námahy**: začněte přijímat dary během několika sekund
- Ochrana soukromí ve výchozím nastavení**: není potřeba serverů ani složité infrastruktury
- Zkušenosti podobné e-mailu**: posílejte a přijímejte bitcoiny stejně jednoduše jako e-mailem



Můžete si vybrat mezi možnostmi "Obnovit" pro obnovení stávajícího portfolia nebo "Vytvořit nové portfolio wallet" pro vytvoření nového portfolia. Stiskněte tlačítko "Create new wallet".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



Aplikace poté vygeneruje frázi pro obnovení, kterou je třeba pečlivě zaznamenat na fyzický nosič. I v případě testovacích prostředků bez skutečné hodnoty si osvojte správné postupy zálohování.



### Interface a parametry



Po vytvoření portfolia se zobrazí hlavní rozhraní rozdělené do dvou karet: "Transakce" a "Nastavení".



Na kartě **Transakce** se zobrazuje zůstatek bitcoinů (a jeho převod na dolary), seznam posledních transakcí a dvě akční tlačítka: "Zaplatit" pro odeslání peněz a tlačítko pro příjem (ikona pro stažení).



Karta **Nastavení** nabízí čtyři možnosti:




- Zobrazit frázi seed**: zobrazí vaši frázi pro obnovení pro úschovu
- Změna fiat měny**: změna měny zobrazení (ve výchozím nastavení USD)
- Nastavení backend url**: konfigurace URL serveru Blindbit (viz další část)
- Wipe wallet**: úplně vymaže wallet ze zařízení



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Server Blindbit



Dana Wallet používá k detekci tichých plateb indexovací server **Blindbit**. Pochopení jeho fungování je důležité pro vyhodnocení modelu důvěryhodnosti aplikace.



**Proč potřebujeme server?



Aby bylo možné odhalit tichou platbu, musí váš wallet teoreticky prohledat všechny transakce Taproot v každém bloku a pro každou z nich provést kryptografický výpočet (ECDH). V mobilním telefonu by tato operace byla příliš náročná na výpočetní výkon a šířku pásma.



Server Blindbit řeší tento problém tím, že pro všechny transakce Taproot předem vypočítá meziprodukty (tzv. "tweaky"). Váš wallet pak tyto tweaky stáhne (33 bajtů na transakci) a provede konečný výpočet **místně**, aby zkontroloval, zda vám platba patří.



**Zachování důvěrnosti**



Na rozdíl od běžného serveru Electrum, kde odhalujete své adresy, server Blindbit neví, které platby vám patří. Všem uživatelům poskytuje stejné údaje a konečné ověření provádí váš telefon. Vaše důvěrnost je tedy vůči serveru zachována.



**Výchozí server



Dana Wallet používá veřejný server `silentpayments.dev/blindbit/signet` (pro Signet) nebo `silentpayments.dev/blindbit/mainnet` (pro Mainnet). Pokud hostujete vlastní server, můžete tuto adresu URL změnit v nastavení.



**Hostování vlastního serveru Blindbit**



Uživatelé, kteří si přejí naprostou suverenitu, mohou hostovat vlastní server Blindbit Oracle. To vyžaduje :




- Kompletní uzel jádra Bitcoin **bez orla** (jiný než pruned)
- Instalace Blindbit Oracle (k dispozici na GitHubu: `setavenger/blindbit-oracle`)
- Přibližně 10 GB dalšího místa na disku
- Technické dovednosti (kompilace Go, konfigurace serveru)



Pro aplikace Umbrel a Start9 zatím není k dispozici žádný balíček. Instalace zůstává prozatím manuální. Tato oblast se aktivně vyvíjí a v budoucnu se mohou objevit dostupnější řešení.



## Denní použití



### Přijímání finančních prostředků



Chcete-li přijmout bitcoiny, stiskněte na hlavní obrazovce tlačítko pro příjem (ikona stahování). Dana Wallet poté na záložce zobrazí vaši kompletní adresu tiché platby ve formátu `tsp1q...`. Rozhraní nabízí několik možností:




- Zobrazit kód QR**: zobrazí kód QR vaší adresy pro snadné skenování
- Sdílet**: sdílení adresy prostřednictvím aplikací v telefonu
- Kopírovat**: zkopíruje adresu do schránky



Jak je zobrazeno na obrazovce, můžete tuto adresu veřejně sdílet na sociálních sítích, aniž byste ohrozili své soukromí.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Chcete-li získat první zkušební prostředky na platformě Signet, použijte speciální kohoutek Silent Payments dostupný na adrese `silentpayments.dev/faucet/signet`. Zkopírujte svou adresu `tsp1...`, vložte ji do pole na faucet a poté žádost potvrďte. Počkejte, až bude vytěžen blok (v systému Signet asi 10 minut).



### Odeslat platbu



Chcete-li odeslat peníze, stiskněte na hlavní obrazovce tlačítko "Zaplatit". Zobrazí se obrazovka "Zvolte příjemce (příjemce)" se třemi možnostmi zadání příjemce:




- Ruční zadání platebních údajů
- Vložit ze schránky**: vložení adresy ze schránky
- Naskenovat QR kód**: naskenujte QR kód obsahující adresu



Po ověření adresy příjemce můžete na obrazovce "Zadat částku" zadat částku, která má být odeslána, v satoších. Pro informaci se zobrazí váš dostupný zůstatek. Pro pokračování stiskněte tlačítko "Pokračovat ve výběru poplatku".



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



Na další obrazovce se zobrazí tři úrovně poplatků v závislosti na požadované naléhavosti:




- Rychlé** (10-30 minut): vyšší poplatky za rychlé potvrzení
- Normální** (30-60 minut): mírné náklady
- Pomalé** (1+ hodina): minimální poplatek za neurgentní transakce



Po výběru výše poplatku se na potvrzovací obrazovce "Připraveno k odeslání?" shrnou všechny podrobnosti: cílová adresa, částka, odhadovaný čas a poplatek za transakci. Tyto informace pečlivě zkontrolujte a poté stisknutím tlačítka "Odeslat" transakci odešlete.



Po odeslání se transakce zobrazí v historii se stavem "Nepotvrzeno", dokud není zařazena do bloku. Váš zůstatek se odpovídajícím způsobem aktualizuje.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Výhody a omezení



### Nejdůležitější informace





- Pedagogické**: zjednodušené rozhraní zaměřené na výuku Tiché platby
- Obousměrné**: na rozdíl od jiných portfolií podporuje odesílání i příjem
- Open-source**: plně auditovatelný kód na GitHubu
- Vyhrazený Faucet**: usnadňuje získání finančních prostředků na testování
- Bez účtu**: není nutná registrace ani osobní údaje



### Omezení, která je třeba zvážit





- Experimentální**: neauditovaný software, u Mainnet používejte s opatrností
- Omezená platforma**: hlavně Android, žádná verze pro iOS
- Omezené funkce**: žádné ovládání mincí, žádné podúčty, žádný Lightning
- Intenzivní skenování**: detekce plateb spotřebovává značné množství prostředků



## Osvědčené postupy



### Bezpečnost seed



Dokonce i v případě testů Signet s bezcenným pozadím berte frázi o obnově vážně. Pomocí možnosti "Zobrazit frázi seed" v nastavení si ji pečlivě zapište. V rámci správné praxe udržujte zcela oddělené peněženky pro Signet a Mainnet: nikdy nepoužívejte seed vytvořený pro testování na wallet určený k přijímání skutečných prostředků.



### Upozornění na experimentální status



Dana Wallet je svými vývojáři stále považována za experimentální. Jak jasně uvádějí: "Nevyužívejte prostředky, o které nejste ochotni přijít". Pro účely učení se rozhodněte pro verzi Signet. Pokud používáte verzi Mainnet, omezte se na částky token.



### Zálohování a obnovení



Tiché vymáhání prostředků vyžaduje zařízení wallet kompatibilní s protokolem BIP-352. Standardní wallet nemůže skenovat blokový řetězec a získat tak vaše Tiché platby UTXO. Nechte si nainstalovanou Danu Wallet nebo při prvním spuštění použijte možnost "Obnovit" pro obnovení stávajícího wallet.



## Srovnání s BIP-47 a PayJoin



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Tiché platby eliminují oznamovací transakci BIP-47 za cenu dražšího skenování. PayJoin řeší jiný problém (korelace vstupů) a lze jej kombinovat s tichými platbami.



## Závěr



Dana Wallet je cenným vzdělávacím nástrojem pro výuku tichých plateb v prostředí bez rizika. Jeho minimalistický přístup umožňuje pochopit základní mechanismy protokolu BIP-352, aniž by vás rozptylovaly vedlejší funkce. Experimentováním se Signetem získáte praktické znalosti o této slibné technologii pro utajení transakcí Bitcoin.



Tiché platby jsou významným krokem vpřed při slaďování snadného používání a respektování soukromí. Nadšení komunity a první integrace do různých peněženek (Cake Wallet, BitBox02, BlueWallet pro odesílání) ukazují na budoucnost, kdy zveřejnění darovací adresy již nebude ohrožovat finanční soukromí jejího majitele.



## Zdroje



### Oficiální dokumentace




- Dana Wallet Úložiště GitHub: https://github.com/cygnet3/danawallet
- F-Cold záloha: https://fdroid.silentpayments.dev
- Komunitní stránky Silent Payments: https://silentpayments.xyz
- Specifikace BIP-352: https://bips.dev/352



### Testovací nástroje Signet




- Faucet Tiché platby: https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet



### Server Blindbit (na vlastním hostingu)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle