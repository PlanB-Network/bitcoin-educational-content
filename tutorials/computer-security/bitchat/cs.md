---
name: Bitchat
description: Decentralizované zasílání zpráv bez internetu pro svobodnou komunikaci
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*Tento videonávod od společnosti BTC Sessions vás provede procesem nastavení a používání aplikace Bitchat!*


Bitchat vznikl na základě rychlého prototypování, kdy [@jack](https://primal.net/jack) během víkendového kódování vyvinul původní koncept. krátce poté se k projektu připojil [@calle](https://primal.net/calle), aby se podílel na vývoji implementace pro Android. Jack v současné době vede vývoj verze pro iOS, zatímco calle dohlíží na verzi pro Android s podporou mnoha dalších přispěvatelů.


## Úvod: Chatujte svobodně, bez sítě


Představte si posílání zpráv při výpadku internetu, během přírodní katastrofy nebo v místech, kde je komunikace omezena. Bitchat to umožňuje. Jedná se o decentralizovanou aplikaci pro zasílání zpráv typu peer-to-peer, která vynechává centrální servery a umožňuje zařízením komunikovat přímo mezi sebou, zcela offline pomocí Bluetooth a mesh sítí. Aplikace Bitchat byla navržena s ohledem na soukromí a odolnost a je ideální pro použití v oblastech, kde je tradiční připojení nespolehlivé nebo nedostupné - například při katastrofách, na odlehlých místech nebo pro ty, kteří se chtějí vyhnout sledování. Bitchat ve své podstatě využívá kryptografii, která zajišťuje, že každá zpráva je od konce do konce zašifrovaná, ověřená a odolná proti manipulaci.


V tomto návodu si ukážeme, jak Bitchat funguje a jak jej můžete používat pro skutečně soukromou komunikaci připravenou pro offline komunikaci.


## 🚀 Klíčové funkce


Bitchat umožňuje offline zasílání zpráv prostřednictvím těchto [funkcí](https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features):



- Kompatibilní s více platformami**: Plná kompatibilita protokolu mezi iOS a Androidem.
- Decentralizovaná síť Mesh**: Automatické zjišťování partnerů a přenos zpráv přes Bluetooth Low Energy (BLE)
- Šifrování od konce ke konci**: Výměna klíčů X25519 + AES-256-GCM pro soukromé zprávy
- Chaty založené na kanálech**: Skupinové zprávy založené na tématech s volitelnou ochranou heslem
- Uložení a předání**: Zprávy se ukládají do mezipaměti pro offline partnery a doručují se při jejich opětovném připojení
- Ochrana osobních údajů na prvním místě**: Žádné účty, žádná telefonní čísla, žádné trvalé identifikátory
- Příkazy ve stylu IRC: Známé rozhraní ve stylu `/join, /msg, /who`.
- Uchovávání zpráv**: Volitelné ukládání zpráv v rámci celého kanálu řízené vlastníky kanálu
- Nouzové utírání**: Trojím klepnutím na logo okamžitě vymažete všechna data
- Moderní uživatelské rozhraní systému Android**: Jetpack Compose s Material Designem 3
- Tmavá/světlá témata**: Estetika inspirovaná terminálem odpovídá verzi pro iOS
- Optimalizace baterie**: Adaptivní skenování a správa napájení


## 1️⃣ Jak funguje Bitchat - jednoduše


Bitchat umožňuje posílat zprávy na okolní telefony přímo přes Bluetooth (`BLE`, jak je uvedeno níže), bez nutnosti připojení k internetu nebo mobilního signálu. Při zahájení konverzace provedou telefony zabezpečený handshake a vytvoří jedinečný, dočasný šifrovací klíč pro vaši konverzaci. Každá zpráva je chráněna koncovým šifrováním a pro každou zprávu je použit nový klíč, aby bylo zajištěno, že minulé zprávy zůstanou v bezpečí i v případě pozdějšího napadení telefonu. Nakonec aplikace rozdělí zprávy na malé kousky a smíchá je s náhodnými fiktivními daty, aby skryla vaši aktivitu v oblasti zpráv. Pro přímé konverzace mezi zařízeními funguje pouze v dosahu do ~100 m. Je to jako předávání zašifrovaných poznámek v přeplněné místnosti - zařízení si šeptají přímo mezi sebou a po každé zprávě skartují klíče.


Bitchat vám také umožňuje připojit se k chatovacím místnostem založeným na poloze pomocí protokolu Nostr a `#geohashes`. Geohash je krátký kód, jako například `#u33d`, který představuje určitou zeměpisnou oblast, od jedné čtvrti až po celé město nebo region. Můžete se `teleportovat` do kterékoli chatovací místnosti s geohash po celém světě jednoduše zadáním její značky. Vaše zprávy jsou odesílány prostřednictvím decentralizované sítě relé, která chrání vaši přesnou polohu. Navíc pokaždé, když se připojíte k místnosti geohash, je vám přidělena nová, dočasná identita, která přidává další vrstvu soukromí do vašich konverzací založených na poloze.


Přesnější technické údaje naleznete v [oficiální bílé knize](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).


## instalace a nastavení 2️⃣


### Kde získat Bitchat


Aplikaci Bitchat můžete nainstalovat prostřednictvím:



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (pro zařízení iOS)
- [Obchod Google Play](https://play.google.com/store/apps/details?id=com.bitchat.droid) (pro zařízení se systémem Android)


Uživatelé systému Android mají také alternativní možnosti:



- Stáhněte si APK přímo ze stránky [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) nebo
- Instalace prostřednictvím kompatibilního obchodu Nostr [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr)


![image](assets/en/01.webp)


**Poznámka**: _Tento tutoriál se zaměřuje především na implementaci pro Android. Verze pro iOS se může lišit._


### Proces nastavení


Po instalaci otevřete aplikaci Bitchat a zobrazí se úvodní obrazovka s oprávněními. Zde je uvedeno, co musíte udělat:


1. **Přidělte tato požadovaná oprávnění:**


   - Přístup přes Bluetooth** (pro zjištění uživatelů Bitchat v okolí)
   - Přesná poloha** (systém Android ji vyžaduje pro funkci Bluetooth)
   - Oznámení** (pro příjem upozornění na soukromé zprávy)

2. **Zakázat optimalizaci baterie**:


   - To umožňuje, aby Bitchat běžel na pozadí
   - Nepřetržitě udržuje síťová připojení


Klepněte na možnost `Udělit oprávnění` , postupujte podle pokynů a klepnutím na možnost `Zakázat optimalizaci baterie` přejděte na další obrazovku.


![image](assets/en/02.webp)


Vítejte na hlavní obrazovce aplikace Bitchat. Pojďme se zorientovat:


### Nastavení


Nejdříve k věci. Nabídku nastavení otevřete klepnutím na logo `Bitchat`.  K dispozici jsou následující možnosti:



- Nastavení vzhledu (systém/světlo/tma).
- povolit `Proof of work` pro geohash pro odradení spamu (volitelné)
- Zapnutím funkce `Tor` zvýšíte soukromí.


![image](assets/en/16.webp)


### Nastavení identity


Klepněte na pole `bitchat/anonXXXX` v horní části a vyberte své uživatelské jméno. Takto vás ostatní uvidí v režimu Bluetooth i internetu. Můžete například změnit "anon2022" na uživatelské jméno podle vlastního výběru.


![image](assets/en/03.webp)


### Výběr síťových kanálů


K přepínání mezi typy připojení použijte nabídku `#lokační kanály` (vpravo od uživatelského jména):



- BLE Mesh***: Výchozí režim Bluetooth (bez internetu, dosah 10 až 50 metrů)
- #geohashes**: Geografické komunity s podporou internetu využívající [protokol Nostr](https://nostr.com/)


Pokud zvolíte režim `#geohashes`, Bitchat se integruje s protokolem Nostr a umožní tak vytváření geografických komunit. Vaše zprávy jsou zveřejňovány na `decentralizovaných relays Nostr` namísto peer-to-peer sítě Bitchat, což umožňuje širší, ale místně filtrované konverzace. Důležité je, že vaše identifikační klíče Bitchat kryptograficky podepisují všechny události Nostr, aby byla zachována autentizace, zatímco značky geohash (jako `#u4pruyd` pro sousedství) filtrují zprávy na vámi zvolenou úroveň přesnosti. To znamená, že se můžete účastnit místních diskusí, aniž byste museli odhalovat přesné souřadnice, ačkoli je vyžadován přístup k internetu.


![image](assets/en/04.webp)


### Sledování vrstevníků

license: CC-BY-SA-V4

Počítadlo uživatelů zobrazuje uživatele:



- Blízko (BLE Mesh) nebo
- Ve vaší zóně geohash (#geohashes)


![image](assets/en/05.webp)


## 3️⃣ Globální chat a soukromé zprávy


Bitchat nabízí dva různé režimy komunikace, které vyhovují různým potřebám:



- Veřejné kanály:** Pro otevřenou konverzaci s ostatními. Můžete se připojit buď prostřednictvím místní sítě BLE mesh pro blízké uživatele, nebo prostřednictvím globálního #geohash pro internetové komunity založené na poloze.
- Soukromé zprávy:** Pro bezpečné rozhovory mezi čtyřma očima. Ty navazují přímé, šifrované spojení, aby vaše výměny zůstaly důvěrné.


Znalost obou režimů vám pomůže při vedení konverzace.


### Veřejné kanály: Komunitní centrum


Nabídka `#lokační kanály` (vpravo nahoře) řídí vaši veřejnou viditelnost. Výběrem možnosti `mesh` se připojíte ke všem uživatelům v okolí prostřednictvím sítě BLE, typicky k zařízením v okruhu 10-50 metrů. Tím se vytvoří otevřené fórum, kde se zprávy vysílají všem v dosahu, což je ideální pro oznámení událostí nebo místní upozornění.


Chcete-li získat širší geografický dosah, zvolte libovolnou značku `#geohash` a připojte se ke komunitám na internetu filtrovaným podle místa. Tyto kanály využívají přenosové kanály protokolu Nostr, které umožňují komunikaci napříč městy nebo regiony při zachování relevance podle polohy. Vaše zprávy se ostatním účastníkům stejného kanálu zobrazují živě a noví účastníci po připojení automaticky vidí historii posledních zpráv.


![image](assets/en/06.webp)


### Soukromé rozhovory: Zabezpečené a šifrované


Chcete-li zahájit soukromou konverzaci, klepněte přímo na libovolné `jméno uživatele` zobrazené v `Přehledu přátel`.Můžete také klepnout na ikonu `hvězdičky` a označit si tohoto uživatele jako oblíbeného, díky čemuž zůstane viditelný ve vašem seznamu kontaktů, i když je offline.


![image](assets/en/07.webp)


Při zahájení soukromého chatu Bitchat automaticky spustí `bezpečnostní handshake`. Zařízení si vymění efemérní klíče a vytvoří šifrovaný tunel speciálně pro vaši konverzaci. Tento proces zajišťuje, že všechny vaše zprávy a sdílené soubory zůstanou důvěrné díky nepřetržitému end-to-end šifrování. Soukromé zprávy podporují sdílení textu a souborů.


![image](assets/en/08.webp)


## 4️⃣ Další funkce


K panelu akcí se dostanete okamžitě zadáním `/` kdekoli v aplikaci Bitchat. Tím se zobrazí nabídka příkazů pro rychlé akce.



- Správa připojení**: `Blokovat uživatele` nebo `Unblock peers`
- Ovládání kanálů**: `Zobrazit kanály` nebo `Připojit/vytvořit kanál`
- Sociální interakce**: 🎣
- Údržba chatu**: `Vymazat zprávy z chatu`
- Nástroje pro ochranu soukromí**: `Zjistit, kdo je online` nebo `Poslat soukromou zprávu`


Příkazy se provádějí okamžitě - jako `/block Satoshi` pro umlčení kritiků nebo `/hug Hal` pro šíření pozitivity 🫂.


![image](assets/en/09.webp)


## 5️⃣ Vytvoření kanálu


Kanály v Bitchatu umožňují organizovanou komunikaci na základě témat, míst nebo komunit. Chcete-li si vytvořit vlastní, postupujte podle tohoto postupu:


### Krok 1: Vytvoření kanálu


Chcete-li vytvořit kanál, napište do libovolného chatu `/j` nebo `/join` následované `názvem kanálu` (např. `/j <název kanálu>`). Po vytvoření se zobrazí nová `ikona ⧉` označující nový kanál. Ostatní uživatelé se mohou připojit zadáním stejného příkazu (např. `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Krok 2: Konfigurace nastavení


Kromě výchozích příkazů jsou v rámci kanálu k dispozici následující nastavení:



- `/save` pro lokální ukládání zpráv
- `/transfer` pro přenos vlastnictví kanálu a
- `/pass` pro změnu hesla kanálu.


U soukromých komunit tento příkaz povoluje ochranu heslem a vyžaduje, aby schválení členové před připojením zadali vlastní heslo.


## 6️⃣ Panický režim


Nyní si povíme něco o tomto `panickém režimu`: trojité klepnutí na logo `Bitchat` spustí kompletní vymazání všech místních zpráv a dat v aplikaci. Jedná se o maximální ochranu soukromí, ideální pro situace vyžadující okamžitou diskrétnost.


**Důležitá připomínka:** _Panický režim je trvalý. Po jeho aktivaci nelze data obnovit. Používejte jej s opatrností._


![image](assets/en/11.webp)


## 7️⃣ Geohashes


Kanály Geohash umožňují cílené konverzace na základě `geografické polohy` namísto tradičních síťových spojení. Díky této funkci se bitchat stává komunikačním nástrojem, který si uvědomuje svou polohu a je ideální pro místní koordinaci, budování komunit a diskuse zaměřené na konkrétní místo.


### Jak funguje `#geohashes`


Systém rozděluje svět na čtverce mřížky pomocí systému [Geohash](https://en.wikipedia.org/wiki/Geohash), kde každý znak v hashi představuje větší přesnost:



- Úroveň 4** (např. `u33d`): Pokrývá přibližně 25 km × 25 km - ideální pro celoměstské diskuse
- Úroveň 6** (např. `u33d8z`): 1,2 km × 1,2 km - přesnost v sousedství
- Úroveň 8** (např. `u33d8z1k`): Pokrývá zhruba 150 m × 150 m - přesnost uličního segmentu


Přesná volba vyvažuje soukromí a užitečnost: vyšší úrovně vytvářejí exkluzivnější zóny, ale přesněji odhalují vaši polohu.


### Připojení ke kanálům `#geohash`


1. Vstupte do nabídky `#lokační kanály`.

2. Vyberte požadovanou úroveň přesnosti a zadejte `#geohash` (např. #u33d)

3. Klepnutím na tlačítko `Teleport` se připojíte ke kanálu `#lokace`.


![image](assets/en/12.webp)


Případně můžete klepnutím na ikonu `mapa` použít zobrazení mapy k určení úrovně přesnosti a klepnutím na `vybrat` se připojit ke kanálu `#lokalizace`.


![image](assets/en/13.webp)


**Důležitá připomínka**: _#geohash vyžaduje aktivní připojení k internetu - na rozdíl od BLE mesh, který funguje offline přes Bluetooth._


## 8️⃣ Heatmaps


Heatmaps jsou skvělým způsobem, jak objevovat události a kanály Bitchat po celém světě. [Bitmapa](https://bitmap.lat/) vizualizuje a sleduje anonymní zprávy založené na poloze v síti Nostr a zobrazuje efemérní události Nostr. Podívejte se a připojte se ke kanálům a chatům specifickým pro danou lokalitu.


![image](assets/en/15.webp)


## 🎯 Závěr


Bitchat umožňuje bezpečnou, decentralizovanou komunikaci v případech, kdy tradiční zasílání zpráv selhává. Je schopen fungovat bez internetové infrastruktury pomocí sítě BLE mesh, takže je vhodný pro protesty, zóny postižené katastrofou a odlehlé oblasti, kde je připojení omezené nebo cenzurované. Aplikace zajišťuje soukromí díky šifrování efemérním klíčem, lokalizačním kanálům založeným na geohash a vymazání dat v režimu paniky.


Aplikace je zatím v počáteční fázi vývoje, ale již nyní se ukazuje jako slibná. Uživatelé by měli počítat s občasnými chybami a problémy hlásit prostřednictvím [GitHub](https://github.com/permissionlesstech/bitchat-android/issues). Plánují se vylepšení, včetně integrace `ecash` pro soukromé transakce v aplikaci pomocí protokolu Cashu.


![image](assets/en/14.webp)


## 📚 Zdroje Bitchat


[Github](https://github.com/permissionlesstech) | [Webové stránky ](https://bitchat.free/)| [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)