---
name: Macadamia Wallet
description: Cashu mobile wallet pro anonymní a okamžité platby BTC
---

![cover](assets/cover.webp)



Macadamia Wallet je mobilní wallet pro iOS, který implementuje protokol Cashu, chaumský systém ecash umožňující zcela anonymní platby Bitcoin. Díky slepým podpisům nemůže žádný pozorovatel spojit vaše vklady s vašimi výdaji, což nabízí důvěrnost podobnou fyzické hotovosti.



V tomto tutoriálu se podíváme na to, jak nainstalovat a nakonfigurovat Macadamia, provést první transakce Cashu (Mint, Send, Receive, Melt) a spravovat více mincoven pro zabezpečení vašich prostředků.



## Co je to makadamiový olej Wallet?



### Protokol Cashu



Cashu používá slepé podpisy, které vynalezl David Chaum: bitcoiny uložíte na serveru "mincovny", který vydá ekvivalentní tokeny v satoších. Mincovna tyto tokeny podepisuje, aniž by viděla jejich obsah, což znemožňuje spojení token s uživatelem. Výměny jsou off-chain, peer-to-peer a naprosto neprůhledné - ani mincovna nemůže sledovat, kdo komu platí.



Macadamia je open source wallet iOS vyvinutý v Swift/SwiftUI. Funguje bez účtu nebo KYC, vaše tokeny jsou uloženy lokálně a chráněny frází seed. Kód je auditovatelný na GitHubu a tokeny jsou interoperabilní s ostatními peněženkami Cashu (Minibits, Cashu.me).



### Model opatrovnictví a kompromis



**Důležité**: Cashu funguje na základě opatrovnického modelu. Tokeny jsou příslibem platby (IOU), který je krytý rezervami mincovny Bitcoin. Pokud mincovna zanikne, vaše žetony ztratí svou hodnotu. Jedná se o kompromis pro dosažení maximální důvěrnosti.



Makadamii používejte jako fyzikální přípravek wallet: pouze v malém množství. Rozložte své prostředky na více mincoven, abyste rozředili riziko.



## Hlavní funkce



Macadamia implementuje čtyři základní operace protokolu Cashu. **Mint** převede vaše satoši na tokeny prostřednictvím faktury Lightning. **Send** umožňuje posílat tokeny zdarma prostřednictvím QR kódu nebo odkazu, a to zcela off-chain. **Příjem** umožňuje přijímat tokeny nebo generate fakturu Lightning. **Tavit** zaplatí fakturu Lightning zničením vašich žetonů.



wallet podporuje správu více mincoven současně. Žetony můžete mezi různými mincovnami vyměňovat prostřednictvím Lightning.



## Podporované platformy



Macadamia je k dispozici pouze v systému iOS 17 nebo vyšším pro iPhone a iPad. Nativní aplikace Swift/SwiftUI nabízí optimální integraci s ekosystémem Apple.



Protokol Cashu zaručuje interoperabilitu mezi peněženkami. Frázi seed můžete obnovit v jiných aplikacích, například v Minibits na Androidu nebo Nutstash na počítači.



Aktuální verze je distribuována prostřednictvím služby TestFlight. Tuto beta verzi používejte pouze v malém množství.



## Instalace



Macadamia je v současné době k dispozici prostřednictvím TestFlight, beta testovacího programu společnosti Apple. Zde je návod, jak ji nainstalovat:



### Instalace pomocí TestFlight



**Krok 1: Stáhněte si TestFlight**



Pokud aplikaci TestFlight ve svém zařízení ještě nemáte, vyhledejte v App Store položku "TestFlight" a nainstalujte ji. TestFlight je oficiální aplikace společnosti Apple pro testování beta verzí aplikací iOS.



**Krok 2: Zapojte se do beta programu Macadamia** (ve francouzštině)



Po instalaci aplikace TestFlight následujte tento odkaz s pozvánkou ze svého iPhonu nebo iPadu: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



Odkaz automaticky otevře TestFlight a nabídne vám instalaci programu Macadamia Wallet. Stiskněte tlačítko "Accept" a poté "Install", čímž zahájíte stahování. Aplikace váží přibližně deset megabajtů a její instalace trvá jen několik sekund.



![Installation TestFlight](assets/fr/01.webp)



### Důležité informace o beta verzích



Macadamia je stále ve fázi aktivního vývoje. Verze TestFlight jsou často aktualizovány a mohou přinášet nové funkce nebo opravovat chyby. Jako u každé beta verze se však mohou vyskytnout závady. **Důrazně doporučujeme používat pouze malé množství**, které akceptujete, že by mohlo být v případě technického problému ztraceno.



Společnost Macadamia neshromažďuje žádné údaje o uživatelích v souladu se zobrazenými zásadami ochrany osobních údajů. Při instalaci nezapomeňte zkontrolovat, že vývojářem je cypherbase UG.



## Počáteční konfigurace



Při prvním spuštění vygeneruje Macadamia větu BIP-39 o 12 slovech. Zapište si je na bezpečné místo - nikdy ne jako snímek obrazovky. Tato slova vám umožní znovu vytvořit wallet a utratit žetony.



![Configuration initiale](assets/fr/02.webp)



Postupujte podle čtyř kroků: uvítání, přijetí podmínek, uložení věty seed a závěrečné potvrzení.



![Interface principale](assets/fr/03.webp)



Po dokončení konfigurace Macadamia zobrazí tři hlavní karty. **Wallet** zobrazuje zůstatek a historii transakcí. **Mints** umožňuje spravovat servery Cashu. *položka *Nastavení** umožňuje přístup k nastavení a vaší frázi seed.



![Ajout d'un mint](assets/fr/04.webp)



Nyní je třeba nakonfigurovat mincovnu, tj. server Cashu, který bude vydávat tokeny. Přejděte na kartu "Mincovny", klepněte na "Přidat novou adresu URL mincovny" a zadejte adresu vybrané mincovny (např. mint.cubabitcoin.org). Podívejte se na stránky bitcoinmints.com nebo cashu.space, kde najdete renomované veřejné mincovny. Ověřujte pouze mincovny, jejichž pověst jste si ověřili, protože budou mít v péči vaše satoši.



## Denní použití



### Vytváření nových žetonů (mincovna)



Chcete-li svůj účet wallet Macadamia nakrmit hotovostí ecash, musíte provést operaci "Mint" (vytvořit žetony). Dotkněte se možnosti "Receive" (Přijmout) a poté vyberte možnost "Lightning" (Blesk). Zadejte požadovanou částku (např. 1000 sats), vyberte mincovník, který chcete použít, a poté generate fakturu Blesk.



![Opération Mint](assets/fr/05.webp)



Uhraďte vygenerovanou fakturu Lightning pomocí obvyklého účtu wallet (Phoenix, Zeus, BlueWallet).



![Confirmation Mint](assets/fr/06.webp)



Žetony Cashu se po zaplacení okamžitě objeví na vašem účtu.



### Odesílání žetonů



Chcete-li poslat žetony Cashu jinému uživateli, dotkněte se tlačítka "Send" na hlavní obrazovce a poté vyberte možnost "Ecash". Zadejte částku, která má být odeslána (např. 50 sats), a v případě potřeby přidejte popisnou poznámku.



![Envoi Ecash](assets/fr/07.webp)



Sdílejte QR kód nebo vygenerovaný text prostřednictvím iMessage, Signal nebo Telegram. Příjemce si okamžitě a bezplatně vyzvedne peníze.



### Přijímání žetonů



Chcete-li přijmout žetony Cashu zaslané jiným uživatelem, dotkněte se tlačítka "Receive" a poté vyberte možnost "Ecash". Naskenujte QR kód token nebo vložte odkaz token, který jste obdrželi.



![Réception Ecash](assets/fr/08.webp)



Dotykem na položku "Redeem" si nárokujte položku token.



### Platby za blesk (tání)



Chcete-li zaplatit fakturu Lightning pomocí žetonů Cashu, dotkněte se tlačítka "Odeslat" a poté vyberte možnost "Lightning". Vložte fakturu BOLT11, kterou chcete zaplatit.



![Paiement Lightning](assets/fr/11.webp)



Mincovna zničí vaše žetony a provede bleskovou platbu. Můžete tak zaplatit za jakoukoli službu Lightning a zároveň si zachovat anonymitu.



### Výměna mezi mincovnami



Pokud obdržíte žetony z mincovny, kterou jste nenakonfigurovali, nabízí vám Macadamia několik možností, jak tyto žetony spravovat.



![Swap inter-mints](assets/fr/09.webp)



Přidejte novou mincovnu nebo vyměňte žetony za stávající mincovnu. Výměna využívá Lightning jako most k anonymnímu převodu vašich prostředků.



### Pokročilá správa více mincoven



Macadamia nabízí sofistikované nástroje pro správu více mincoven najednou a strategické rozdělení finančních prostředků.



![Gestion multi-mints](assets/fr/10.webp)



"Rozdělit prostředky" automaticky rozdělí váš zůstatek podle procent (např. 50/50). "Převod" umožňuje ruční převody mezi mincovnami pro diverzifikaci vašich rizik.



## Výhody a omezení



**Highlights** :





- Maximální důvěrnost**: Transakce jsou nevystopovatelné, a to i ze strany mincovny. Žádná metadata blockchainu, nesledovatelné peer-to-peer výměny.
- Rychle a zdarma**: Bezplatné okamžité převody v rámci mincovníku, ideální pro mikroplatby.
- Interoperabilita**: standardizované tokeny Cashu pro použití s jinými kompatibilními peněženkami (Minibits, Nutstash).
- Jednoduchost**: Interface iOS native je přístupný i začátečníkům a přitom zůstává kontrolovatelný (open source).



**Omezení** :





- Opatrovnický model**: vyžadován mincovní trust. Pokud mincovna zanikne, vaše žetony ztratí svou hodnotu.
- pouze pro iOS**: Žádná verze pro Android/desktop. Interoperabilita Cashu umožňuje přístup přes jiné peněženky, ale optimální je stále iOS.
- Závislost na mátě**: Mint offline = není schopen provádět transakce, které vyžadují jeho zásah (Mint, Melt).
- Nové technologie** : Aktivní vývoj, možné chyby, vyvíjející se standardy.



## Osvědčené postupy





- Rozmanitost mincoven**: Rozložte své žetony mezi několik renomovaných mincoven, abyste rozmělnili riziko.
- Limitní částky**: Používejte Macadamia jako fyzickou kartu wallet pro denní platby, nikoli jako trezor.
- Zajistěte své zařízení seed**: Uložte si 12 slov na papíře na bezpečném místě. Občas otestujte obnovení.
- Zkontrolujte mincovníky**: Před přidáním mincovny se poraďte s cashu.space a komunitními fóry. Vybírejte ty, které mají dobrou dobu provozu a dobrou pověst.
- VPN nebo Tor**: Skryjte svou IP adresu pomocí VPN/Tor, abyste maximalizovali soukromí v síti.
- Připojte se ke komunitě**: Pro aktualizace, mincovní doporučení a osvědčené postupy se obracejte na skupiny Telegram/Discord Cashu.



## Závěr



Macadamia Wallet přináší vlastnosti fyzické hotovosti do digitálního Bitcoin. Kombinací slepých podpisů Chaum a Lightning nabízí elegantní řešení pro utajení transakcí. Jeho nativní rozhraní pro iOS zpřístupňuje sofistikované kryptografické technologie a zároveň zůstává open source a interoperabilní s ekosystémem Cashu.



Model opatrovnictví vyžaduje ostražitost a správné bezpečnostní postupy. Při správném používání se Macadamia stává neocenitelným nástrojem pro každodenní platby vyžadující anonymitu a doplňuje neúschovné peněženky pro spoření.



## Zdroje



### Oficiální dokumentace




- Oficiální webové stránky: [macadamia.cash](https://macadamia.cash)
- Nejčastější dotazy k makadamii: [macadamia.cash/faq](https://macadamia.cash/faq)
- Zdrojový kód GitHub: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Dokumentace Cashu




- Technická dokumentace: [docs.cashu.space](https://docs.cashu.space)
- Seznam veřejných mincoven: [bitcoinmints.com](https://bitcoinmints.com)
- Oficiální webové stránky protokolu: [cashu.space](https://cashu.space)



### Společenství




- Skupina Telegram Cashu: [t.me/cashu_ecash](https://t.me/cashu_ecash)