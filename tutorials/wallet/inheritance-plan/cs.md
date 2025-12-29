---
name: Plán dědictví Bitcoin
description: Jak převést bitcoiny svým blízkým
---

![cover](assets/cover.webp)



Přenos bitcoinů představuje velkou technickou výzvu, kterou mnoho držitelů přehlíží. Na rozdíl od tradičních bankovních aktiv, kde finanční instituce může převést prostředky oprávněným vlastníkům, funguje Bitcoin bez prostředníků. Vaši blízcí se bez potřebných technických informací k vašim prostředkům nikdy nedostanou, a to bez ohledu na jejich právní legitimitu.



Tento výukový program vás provede vytvořením technického plánu dědictví. Dozvíte se, jak fungují mechanismy automatického přenosu on-chain, jak dokumentovat konfigurace a jak zvolit správná řešení, abyste zajistili, že vaše dědictví Bitcoin zůstane přístupné vašim blízkým.



## Proč je plán technického dědictví nezbytný



Bitcoin je založen na základním kryptografickém principu: kdo má soukromé klíče, ten kontroluje finanční prostředky. Tato svrchovanost se stává velkou zranitelností, když držitel zmizí, aniž by předal potřebné informace.



Dědický plán Bitcoin musí splňovat dva zdánlivě protichůdné cíle: umožnit vašim blízkým přístup k vašim finančním prostředkům, až přijde čas, a zároveň zabránit tomu, aby se k nim předčasně dostal někdo jiný. Tato křehká rovnováha se opírá o nativní programovací schopnosti systému Bitcoin.



Technická složitost přidává další úroveň obtížnosti. Vaši dědicové budou muset manipulovat s pojmy, jako jsou fráze pro obnovu, deskriptory portfolia nebo cesty odvození. Bez odpovídající přípravy hrozí, že i dědic s dobrými úmysly udělá nevratné chyby.



## Jak funguje dědičnost on-chain



Bitcoin používá svůj skriptovací jazyk k zakódování podmínek výdajů přímo v transakcích. Dědičnost on-chain využívá této programovatelnosti k vytváření alternativních cest obnovy, které se aktivují automaticky.



### Časové zámky



Časové zámky jsou základním mechanismem dědičnosti Bitcoin. Umožňují uzamknout prostředky, dokud není splněna časová podmínka.



**CLTV (CheckLockTimeVerify)**: Tento absolutní časový zámek kontroluje, zda bylo dosaženo určitého času (datum nebo výška bloku) před schválením výdaje. Například "tyto prostředky lze utratit až po bloku 900000" nebo "po 1. lednu 2026". Výhodou CLTV je, že umožňuje dlouhé zpoždění (několik let), ale datum je pevné a platí shodně pro všechny UTXO v portfoliu. Chcete-li si zachovat kontrolu nad svými prostředky, musíte pravidelně vytvářet nové portfolio s prodlouženým datem platnosti a převádět do něj své prostředky.



**CSV (CheckSequenceVerify)**: Tento relativní časový zámek ověřuje, zda od vytvoření UTXO uplynul určitý počet bloků. Například "tyto prostředky lze utratit až 52560 bloků (~1 rok) po přijetí". Výhodou CSV je, že každý UTXO má své vlastní nezávislé počítadlo. Při každém provedení transakce si nově vytvořené UTXO vynulují svůj vlastní časový limit. Technický limit 65535 bloků (maximálně ~15 měsíců) však omezuje možné časové rámce. Tento přístup je pro každodenní používání přirozenější, protože vaše běžná činnost automaticky posouvá termíny.



### Více způsobů utrácení



Dědičné portfolio kombinuje na každé adrese několik cest výdajů:





- Hlavní cesta** : Majitel může kdykoli utratit své prostředky pomocí hlavního klíče bez časového omezení.
- Cesta (cesty) obnovy**: Jeden nebo více alternativních klíčů může vynakládat prostředky až po uplynutí stanovené doby.



Každá transakce provedená vlastníkem "obnoví" UTXO a vytvoří nové výstupy s vynulovanými časovými zámky. Tento mechanismus zajišťuje, že dokud je vlastník aktivní, cesty obnovy se nikdy neaktivují.



### Miniscript a Taproot



**Miniscript** je strukturovaný jazyk vyvinutý Andrewem Poelstrou, Pieterem Wuillem a Sanketem Kanjalkarem, který usnadňuje psaní a analýzu složitých skriptů Bitcoin. Umožňuje sestavovat čitelné a ověřitelné podmínky pro utrácení, což je nezbytné pro konfigurace dědičnosti zahrnující více klíčů a časových zámků.



**Taproot** (aktivován v listopadu 2021) výrazně zlepšuje dědičnost on-chain. Díky jeho stromové struktuře (MAST) je v blockchainu odhalena pouze použitá výdajová podmínka. Pokud vlastník utratí své prostředky normálně, podmínky dědictví zůstávají neviditelné. Tato důvěrnost také snižuje transakční náklady u složitých cest.



## Zásadní význam deskriptorů



V případě starších portfolií nestačí k obnovení přístupu k finančním prostředkům věta pro obnovu (seed). Rozhodujícím prvkem se stává **deskriptor**.



Deskriptor je řetězec, který vyčerpávajícím způsobem popisuje strukturu portfolia: zapojené veřejné klíče, podmínky výdajů, cesty odvození a nakonfigurované časové zámky. Zde je zjednodušený příklad:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Tento deskriptor říká: "buď může hlavní klíč utratit okamžitě, nebo může klíč obnovy utratit po 52560 blocích".



Rozbalme si tento příklad:




- `wsh()` : Svědecký skript Hash, označuje typ adresy (P2WSH)
- or_d()`: podmínka "nebo" s výchozí větví
- pk([otisk prstu/cesta]xpub...)`: Hlavní veřejný klíč s otiskem prstu a cestou odvození
- and_v()`: podmínka "a" kombinující klíč obnovy s časovým zámkem
- `starší(52560)`: Relativní časový zámek 52560 bloků



**Bez deskriptoru nebudou vaši dědicové schopni obnovit portfolio ani se všemi frázemi pro obnovu.** Standardní portfolio lze obnovit pouze z seed, protože se řídí standardizovanými odvozovacími cestami (BIP44, BIP84). Starší portfolio naproti tomu používá vlastní skripty, které nelze odhadnout. Záloha deskriptoru (nebo konfigurační soubor exportovaný vaším softwarem) musí doprovázet fráze pro obnovu v plánu dědictví.



## Dokumentární součásti dědického plánu



Kromě technických mechanismů se účinný plán dědictví opírá o tři pilíře dokumentace.



### Dědický list



Tento osobní dopis je vstupním bodem vašeho plánu. Je určen vašim dědicům a vysvětluje souvislosti a opatření, která je třeba přijmout.



Váš dopis musí obsahovat výslovná bezpečnostní pravidla:




- Nespěchejte, před přesunem finančních prostředků si dejte čas na učení
- Nikdy nesdělujte kompletní frázi o obnově jediné osobě
- Nikdy nezadávejte frázi pro obnovení do neověřeného softwaru nebo počítače
- Pozor na podvodníky a lidi nabízející nevyžádanou pomoc
- Než se rozhodnete, požádejte o radu alespoň dvě osoby, kterým důvěřujete



Tento dopis obsahuje také kontaktní údaje notáře a místo uložení závěti. Nikdy by neměl obsahovat fráze pro obnovu nebo hesla.



### Adresář důvěryhodných kontaktů



Žádný dědic by neměl čelit obnově bitcoinu sám. Tento adresář obsahuje seznam osob, které mohou poskytnout technickou nebo právní pomoc.



U každého kontaktu uveďte: celé jméno, vztah k vám, roli v plánu, úroveň důvěry, dovednosti Bitcoin a úplné kontaktní údaje. Základní pravidlo: vaši dědicové by se měli před přijetím jakéhokoli důležitého rozhodnutí vždy poradit alespoň se dvěma různými osobami.



### Inventarizace majetku Bitcoin



V této sekci jsou zmapovány všechny vaše bitcoiny s technickými informacemi potřebnými k jejich obnově.



Pro každé portfolio zdokumentujte :




- Typ portfolia**: hardware, software, konfigurace (single-sig, multisig, legacy)
- Umístění zařízení**: fyzické umístění hardwaru wallet
- Umístění souboru Descriptor/konfigurace**: kritické pro pokročilá portfolia
- Umístění výrazu pro vymáhání**: odděleně od deskriptoru
- Přístupové kódy**: kde jsou uloženy kódy PIN a přístupové fráze
- Konfigurované prodlevy**: při aktivaci cest obnovy



## Dostupná technická řešení



Několik softwarových balíků implementuje mechanismy dědičnosti on-chain. Každý z nich má své vlastní technické vlastnosti.



### Liana



Liana je desktopový software (Linux, macOS, Windows) používající Miniscript k vytváření portfolií s časovanými cestami obnovy. Projekt vyvíjí společnost Wizardsardine, jejímž spoluzakladatelem je Antoine Poinsot (hlavní přispěvatel Bitcoin).



**Technická architektura**: Liana vytváří ve výchozím nastavení portfolia P2WSH (nativní SegWit), přičemž podpora Taproot je k dispozici v závislosti na kompatibilitě vašeho hardwaru wallet. Architektura je založena na hlavní cestě a jedné nebo více cestách obnovy. Vytvořený deskriptor kóduje všechny podmínky a musí být uložen.



**Použité časové zámky**: Liana používá relativní časové bloky (CSV), omezené na 65535 bloků (~15 měsíců). Pro zachování kontroly je nutné provést transakci obnovení před vypršením časového zámku.



**Integrace hardwaru wallet**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY a další zařízení jsou kompatibilní pro podepisování transakcí.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper je mobilní aplikace (iOS, Android) kombinující multisig a časové zámky prostřednictvím "Enhanced Vaults". Mobilní přístup s integrovaným naváděním ji zpřístupňuje i méně technicky zdatným uživatelům.



**Technická architektura**: Vylepšené trezory využívají Miniscript k vytváření multisig konfigurací, kde se další klíče aktivují s definovaným zpožděním. Dědičný klíč přidává ke stávajícímu kvoru, zatímco nouzový klíč může multisig zcela obejít.



**Použité časové zámky**: Bitcoin Keeper používá absolutní časomíry (CLTV), které umožňují dodací lhůty delší než 15 měsíců. Datum aktivace je nastaveno při vytvoření wallet a platí pro všechny UTXO. Aplikace obsahuje funkci "revaulting", která automaticky řídí obnovu: uživatel jednoduše postupuje podle naváděcích kroků, aniž by musel ručně vytvářet nový wallet.



**Další funkce**: Funkce: Integrované dědické dokumenty, peněženky Canary pro detekci ohrožení klíčů a připomenutí obnovení.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Heritage



Heritage je desktopová aplikace, která používá skripty Taproot ke kódování podmínek dědičnosti. Použití Taproot nabízí zvýšenou důvěrnost, protože nepoužité cesty zůstávají v blockchainu neviditelné.



**Technická architektura**: Každá adresa dědictví zahrnuje hlavní cestu a alternativní cesty pro každého dědice s postupným časovým rozvrhem. Hierarchická struktura umožňuje definovat osobní zálohu po 6 měsících a rodinné dědice po 12-15 měsících.



**Způsoby použití**: Samostatná verze s vlastním uzlem (zdarma) nebo spravovaná služba přidávající upomínky a oznámení dědicům (0,05 %/rok).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Proces obnovy dědice



Pochopení procesu obnovy pomáhá připravit účinný plán. Zde jsou uvedeny technické kroky, které musí dědic dodržet.



### Požadavky na obnovu



Dědic potřebuje :


1. **Deskriptor nebo konfigurační soubor** původního portfolia (JSON nebo textový formát, v závislosti na softwaru)


2. **jeho fráze pro obnovení** (fráze spojená s klíčem dědictví, obvykle 12 nebo 24 slov)


3. **Kompatibilní software** (Liana, Bitcoin Keeper, Heritage nebo Sparrow/Specter pro standardní deskriptory)


4. **Připojení k uzlu Bitcoin** pro kontrolu stavu časového zámku a vysílání transakce



### Kroky k obnově



1. **Instalace softwaru** do zabezpečeného zařízení a konfigurace připojení k síti Bitcoin (osobní uzel nebo server Electrum)


2. **Importujte deskriptor** pro rekonstrukci struktury portfolia. Software automaticky generate všechny použité adresy


3. **Obnovit klíč dědictví** z fráze pro obnovení. Software zkontroluje, zda tento klíč odpovídá jednomu z klíčů autorizovaných v deskriptoru


4. **Synchronizace portfolia** pro zjištění všech UTXO a podmínek jejich výdajů


5. **Kontrola vypršení platnosti časového zámku**: software pro každý UTXO uvede, zda je cesta obnovy aktivní


6. **Vytvoření transakce obnovy** na adresu, kterou ovládá výhradně dědic (ideálně nový jediný wallet)


7. **Podepsání a vysílání** transakce v síti Bitcoin



Pokud časový zámek ještě nevypršel, musí dědic počkat. Software zobrazí datum nebo blok, od kterého je možné obnovení. Během této čekací doby zůstávají prostředky v blockchainu v bezpečí.



### Body, které je třeba sledovat u dědice



Dědic musí věnovat zvláštní pozornost :




- Kontrola pravosti staženého softwaru** (kontrolní součty, podpisy)
- Nikdy nesdělujte svou frázi o zotavení** nikomu, kdo vám nabízí pomoc
- Před provedením obnovy se poraďte alespoň se dvěma důvěryhodnými osobami**
- Převést finanční prostředky do jednoduchého portfolia**, které má po zotavení plně pod kontrolou



## Osvědčené postupy



### Oddělení informací



Nikdy neukládejte všechny informace na jednom místě. Deskriptor musí být oddělen od frází pro obnovení, které jsou zase odděleny od kódů PIN. Toto rozdělení komplikuje přístup útočníkovi a zároveň zůstává obnovitelné pro vaše legitimní dědice.



### Testy obnovy



Před vložením značných finančních prostředků si celý proces obnovy vyzkoušejte na malé částce. Ověřte si, že můžete obnovit portfolio z deskriptoru a frází pro obnovení na prázdném zařízení. Zdokumentujte jednotlivé kroky pro své dědice.



### Údržba časového zámku



Naplánujte si obnovení časových zámků v dostatečném předstihu před vypršením jejich platnosti. V případě 12měsíčního časového zámku proveďte transakci každých 9-10 měsíců. Software obvykle nabízí funkce připomenutí nebo automatické obnovení.



### Aktualizace plánu



Vaše konfigurace Bitcoin se vyvíjí. Každá významná změna (nové portfolio, úprava termínů, přidání dědice) musí být zohledněna ve vaší dokumentaci. Zavedete si každoroční rutinní revizi.



## Volba přístupu



Výběr mezi různými řešeními závisí na vašem technickém profilu a vašich konkrétních potřebách.



**Liana** je vhodný pro uživatele stolních počítačů, kteří dávají přednost softwaru s otevřeným zdrojovým kódem a plným ovládáním prostřednictvím vlastního uzlu. Konfigurace zůstává přístupná díky průvodcovskému rozhraní. Relativní časové plány (CSV) zjednodušují údržbu, protože vaše běžná činnost automaticky posouvá termíny. Omezení: maximální zpoždění přibližně 15 měsíců (65535 bloků).



**Bitcoin Keeper** se zaměřuje na mobilní uživatele, kteří hledají intuitivní rozhraní s integrovanými doprovodnými dokumenty. Aplikace nabízí dva typy speciálních klíčů: Dědičný klíč (který se přidává ke kvoru) a Nouzový klíč (který jej zcela obchází). Absolutní časové klíče (CLTV) umožňují dobu realizace přesahující 15 měsíců, přičemž integrovaná funkce revaultingu zjednodušuje obnovu. Plán Diamantové ruce odemyká pokročilé starší funkce.



**Dědičnost** je určena technickým uživatelům, kteří ocení důvěrnost Taproot a hierarchickou dědičnost s postupným zpožděním. Stromová struktura Taproot skrývá podmínky dědičnosti při běžných transakcích a odhaluje pouze podmínku použitou při obnově.



Všechna tři řešení mají jedno společné: vyžadují pravidelné obnovování, aby se zabránilo předčasné aktivaci cest obnovení. Toto omezení je cenou i zárukou nedůvěryhodného dědictví on-chain. Naplánujte si pravidelné upomínky a zařaďte tuto údržbu do rutiny správy systému Bitcoin.



## Závěr



Technický plán dědictví Bitcoin kombinuje kryptografické mechanismy (časové zámky, Miniscript, Taproot) s přísnou dokumentací. Pokročilé peněženky umožňují automatický přenos bitcoinů po určité době nečinnosti bez zásahu třetí strany.



Důležité prvky, které je třeba předat dědicům, jsou: deskriptor nebo konfigurační soubor, jejich fráze pro obnovení, podrobné pokyny pro obnovení a kontaktní údaje na kompetentní osoby, které jim mohou pomoci.



Začněte výběrem technického řešení vhodného pro váš profil, vyzkoušejte jej na malém množství a poté vše zdokumentujte ve strukturovaném plánu. Počáteční složitost zaručuje, že vaše aktiva Bitcoin budou předána s plnou důvěrou.



## Zdroje



### Šablona dědického plánu





- [Šablona dědického plánu Bitcoin (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Šablona dokumentace Plan ₿ Network



### Technické odkazy





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Specifikace absolutních časoměrů (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Specifikace relativních časových záznamů (CSV)
- [Miniscript Reference](https://bitcoin.sipa.be/miniscript/) - Oficiální dokumentace Miniscriptu od Pietera Wuilleho



### Oficiální webové stránky řešení





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Heritage Wallet](https://btc-heritage.com/) - Crypto7