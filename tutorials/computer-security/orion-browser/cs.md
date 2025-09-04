---
name: Prohlížeč Orion
description: Jak používat Orion Browser k ochraně soukromí na Macu a iPhonu?
---

![cover](assets/cover.webp)



## Úvod



V situaci, kdy většina prohlížečů masivně shromažďuje naše osobní údaje, se výběr prohlížeče šetrného k soukromí stává klíčovým. Chrome dominuje s 65% podílem na celosvětovém trhu, ale jeho obchodní model je založen na využívání údajů o prohlížení. Prohlížeč Safari, ačkoli je integrován do ekosystému společnosti Apple, postrádá pokročilé ochranné funkce a pružně nepodporuje rozšíření třetích stran.



![Répartition du marché des navigateurs](assets/fr/01.webp)


*Rozdělení trhu webových prohlížečů: Chrome dominuje s více než 65% podílem na trhu, následují Safari, Edge a Firefox*



**Orion Browser** se představuje jako inovativní alternativa pro uživatele Apple. Tento prohlížeč, vyvinutý společností Kagi, kombinuje rychlost jádra WebKit s filozofií nulové telemetrie. Na rozdíl od svých konkurentů Orion neodesílá žádná data na vzdálené servery a nativně blokuje 99,9 % reklam a sledovacích zařízení, včetně YouTube.



Jeho jedinečná vlastnost? Orion je **jediným prohlížečem WebKit**, který nativně instaluje rozšíření pro Chrome **a** Firefox, a nabízí tak to nejlepší z obou světů. Tato kompatibilita v kombinaci s 2 až 3krát nižší spotřebou paměti než u jiných prohlížečů a bezproblémovou integrací s ekosystémem Apple (iCloud, Keychain) z něj činí ideální volbu pro uživatele Maců a iPhonů, kteří dbají na své soukromí.



## Proč si vybrat Orion Browser?



### Hlavní výhody



**Maximální ochrana hned po vybalení z krabice**: Orion ve výchozím nastavení blokuje 99,9 % reklam (včetně YouTube) a všechny sledovací služby první strany i třetích stran. Jeho technologie kombinuje inteligentní prevenci sledování WebKit se seznamy EasyPrivacy pro dosažení maximální účinnosti. Jedinečná funkce: Orion blokuje fingerprintingové skripty **před jejich spuštěním**, čímž doslova znemožňuje sledování - jedná se o radikálnější přístup než u jiných prohlížečů, které se pouze snaží data "maskovat".



**Nulová ověřitelná telemetrie**: Orion zaujímá radikální přístup k ochraně soukromí, protože jeho konstrukce je nulová. Na rozdíl od jiných prohlížečů, které při spuštění provádějí stovky síťových požadavků (exponent IP, otisk prstu prohlížeče, osobní údaje), Orion nikdy "nevolá domů". Tento zásadní rozdíl zcela eliminuje riziko neúmyslného úniku dat.



**Výjimečný výkon**: Orion je založen na optimalizované verzi WebKitu a svou rychlostí se na Macu vyrovná Safari nebo ho dokonce předčí. V testech Speedometer 2.0/2.1 se na křemíkových procesorech Apple trvale umisťuje na prvním místě. Nativní blokování reklam dále zrychluje načítání stránek o 20 až 40 %.



**Univerzální podpora rozšíření**: Orion umožňuje instalovat rozšíření z webového obchodu Chrome **a** Mozilla Add-ons. Podpora webových rozšíření je v současné době experimentální, cílem je 100% kompatibilita při vydání beta verze. Můžete používat mnoho populárních rozšíření, jako je uBlock Origin, Bitwarden, a to i na iPhonu - v systému iOS je to světová novinka, i když některá nemusí fungovat dokonale.



### Omezení, která je třeba si uvědomit





- Omezená dostupnost**: V současné době vyhrazeno pro macOS a iOS/iPadOS. Verze pro Linux dosahuje milníků vývoje (milník 2 v roce 2025), ale není k dispozici žádné veřejné sestavení. Verze pro Windows a Android nejsou ve vývoji z důvodu nedostatku zdrojů.
- Uzavřený zdrojový kód**: Přestože některé komponenty jsou open-source, Orion zůstává převážně proprietární, což je předmětem diskusí v komunitě zabývající se ochranou soukromí.
- Experimentální rozšíření**: Podpora rozšíření zůstává ve fázi beta s častými nekompatibilitami. Rozšíření mohou mít vliv na výkon a některá nefungují vůbec.
- Zabezpečení WebKit**: Na rozdíl od Chromu WebKit nenabízí tak robustní izolaci procesů na webu, což může v určitých scénářích představovat bezpečnostní riziko.
- Blokovací testy**: Kagi považuje tyto testy za "zásadně chybné". Skutečná účinnost při každodenním používání je mnohem lepší.



## Instalace prohlížeče Orion Browser



### V systému macOS



![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)


*Domovská stránka Kagi představuje Orion Browser jako "prohlížeč bez reklam s úplnou ochranou soukromí a univerzální podporou rozšíření "*





- Přejít na [kagi.com/orion](https://kagi.com/orion/)
- Klikněte na "**Stáhnout Orion pro macOS**"



![Page de téléchargement d'Orion Browser](assets/fr/03.webp)


*Stránka Orion Browser ke stažení s dostupností pro macOS a iOS a odkazy na App Store*





- Otevření staženého souboru `.dmg`
- Přetáhněte aplikaci Orion do složky Aplikace
- Při prvním spuštění vás systém macOS požádá o potvrzení otevření



**Alternativní Homebrew**:


```bash
brew install --cask orion
```



### V zařízení iPhone/iPad





- Otevřete **App Store**
- Hledat "**Orion Browser by Kagi**"
- Nainstalujte si bezplatnou aplikaci (kompatibilní s iOS 15+)



### Počáteční konfigurace



Při prvním spuštění vás Orion provede několika kroky:



**1. Uvítací obrazovka


![Écran de bienvenue d'Orion](assets/fr/04.webp)


*Uvítací obrazovka prohlížeče Orion Browser s upozorněním na klíčové funkce: rychlejší prohlížení, nulová telemetrie, blokování reklam a podpora rozšíření*



**2. Přizpůsobení Interface**


![Options de personnalisation](assets/fr/05.webp)


*Na obrazovce přizpůsobení můžete nakonfigurovat vzhled karet a Interface podle svých preferencí*





- Import dat**: Snadný přenos oblíbených položek a hesel ze Safari, Chrome nebo Firefoxu
- Synchronizace přes ICloud**: Aktivujte, abyste našli své oblíbené položky a karty na všech svých zařízeních Apple



**3. Instalace na mobilní zařízení**


![Installation sur iOS](assets/fr/06.webp)


*Instalační obrazovka v systému iOS zobrazující QR kód pro rychlé stažení Orion Browseru z App Store*



**4. Interface vítané a nezbytné nástroje



![Page d'accueil Orion](assets/fr/07.webp)


*Domovská stránka Orion Browseru Interface: šipka označuje tři klíčové nástroje přístupné přímo z panelu Address*



Po dokončení konfigurace objevíte zjednodušenou aplikaci Interface Orion s jejími **třemi základními nástroji** (označeno šipkou):





- Štít 🛡️**: Zobrazí zprávu o ochraně osobních údajů s počtem blokovaných položek na aktuální stránce
- Kartáč 🖌️**: Přizpůsobení zobrazení stránky (téma, písmo, odstranění rušivých prvků Elements)
- Převodovka ⚙️**: Konfigurace parametrů specifických pro web (oprávnění, blokování atd.)



Tyto nástroje jsou vždy k dispozici a umožňují vám kontrolovat prohlížení na jednotlivých stránkách.



**Důležité**: Orion je zdarma a nevyžaduje registraci ani vytvoření účtu.



![Orion+ dans les préférences](assets/fr/08.webp)


*Obrazovka předplatného Orion+ v předvolbách, která nabízí volitelné předplatné na podporu vývoje*



**Orion+ (volitelně)**: Pro podporu vývoje projektů nabízí Kagi Orion+ (5 USD/měsíc, 50 USD/rok nebo 150 USD doživotně). Toto dobrovolné předplatné umožňuje:




- Komunikovat přímo s vývojovým týmem
- Ovlivnění vývoje prohlížeče podle vašich potřeb
- Přístup k nočním verzím s nejnovějšími experimentálními funkcemi
- Využijte nejnovější engine WebKit
- Získejte výrazný odznak na fóru zpětné vazby



Orion+ zaručuje nezávislost projektu: "Váš finanční příspěvek nám pomáhá zůstat nezávislými a dodržet náš slib, že se staneme nejlepším prohlížečem pro naše uživatele." Právě díky tomuto modelu financování uživateli je Orion bez reklam a telemetrie.



## Konfigurace pro maximální důvěrnost



### Základní parametry



Přístup k předvolbám získáte prostřednictvím **Orion → Předvolby** (nebo ⌘,):



**1. Vyhledávání - Soukromý vyhledávač**



![Configuration du moteur de recherche](assets/fr/09.webp)


*Výchozí konfigurace vyhledávače: DuckDuckGo je vybrán pro maximální ochranu soukromí*





- Výchozí motor**: Pro optimální ochranu soukromí vyberte **DuckDuckGo**, **Startpage** nebo **Kagi** (vyhněte se Google/Bing)
- Návrhy na vyhledávání**: Zakázat je, abyste zabránili úniku stisknutých kláves na servery vyhledávačů



**2. Ochrana soukromí - obecná** ochrana



![Content Blocker dans les préférences](assets/fr/12.webp)


*Nastavení ochrany osobních údajů Orion zobrazující blokování obsahu s 119 156 aktivními pravidly, možnostmi odstranění sledovacích zařízení a vlastním uživatelským agentem*



**Blokátor obsahu je ve výchozím nastavení aktivní**:




- EasyList**: 119k+ pravidel pro blokování reklam
- EasyPrivacy**: Ochrana proti sledování
- Správa seznamů filtrů**: Přidejte další seznamy (doporučujeme Hagezi)



**Možnosti ochrany osobních údajů**:




- Odstranění sledovacích zařízení z adres URL**: "Pouze pro soukromé prohlížení" vyčistí zkopírované odkazy
- Sdílejte hlášení o nehodách**: "Po vyžádání souhlasu" respektuje váš souhlas
- Vlastní uživatelský agent**: Může být upraven tak, aby obcházel určitá blokování



![YouTube avec Privacy Report](assets/fr/10.webp)


*Příklad YouTube prohlíženého pomocí Orionu: žádná viditelná reklama a zpráva o ochraně osobních údajů zobrazující mnoho blokovaných Elements*



**3. Nastavení webových stránek - ovládání podle stránek**



![Website Settings pour YouTube](assets/fr/11.webp)


*Nastavení webu pro YouTube zobrazující možnosti kompatibility, blokování obsahu a oprávnění specifická pro daný web*



**Rychlý přístup**: Kliknutím na ozubené kolečko ⚙️ v liště Address nastavíte:




- Režim kompatibility**: Řeší problémy se zobrazením pozastavením rozšíření
- Blokátory obsahu**: V případě potřeby deaktivujte blokování konkrétního webu
- JavaScript/Cookies**: Granulární kontrola podle webu
- Oprávnění**: Nastavení: kamera, mikrofon, poloha individuálně konfigurovaná



**4. Pokročilé vlastní filtry** (viz níže)



**Vytvoření vlastních filtrů** (Soukromí → Správa seznamů filtrů → Vlastní filtry):



**Zjednodušená syntaxe** (kompatibilní s Adblock Plus):




- `reddit.com##.promotedlink`: Skryje sponzorované příspěvky na Redditu
- `||ads.example.com^`: Úplně zablokuje reklamní doménu
- `@@||site-utile.com^`: Vytvoří výjimku pro web



**Tip: Navštivte [FilterLists.com](https://filterlists.com), kde najdete tisíce specializovaných seznamů připravených k použití.



### Doporučená rozšíření



Orion nativně podporuje rozšíření pro Chrome a Firefox. Nainstalujte si je přímo z oficiálních obchodů:



**Podstatné**:




- uBlock Origin**: Přidává granulární ovládání k nativnímu blokátoru
- Bitwarden**: Správce hesel s otevřeným zdrojovým kódem
- ClearURLs**: Odstraní parametry sledování URL



**Volitelné**:




- LocalCDN**: Slouží lokálně pro sdílené knihovny
- Cookie AutoDelete**: Automaticky odstraní soubory cookie po zavření karet
- NoScript**: Úplná kontrola nad prováděním JavaScriptu (pro pokročilé uživatele)



Instalace zařízení:




- Navštivte [chrome.google.com/webstore](https://chrome.google.com/webstore) nebo [addons.mozilla.org](https://addons.mozilla.org)
- Klikněte na "Přidat do prohlížeče Chrome/Firefox"
- Orion toto rozšíření zachytí a nainstaluje automaticky



**Upozornění**: Vzhledem k tomu, že podpora rozšíření je experimentální, mnohá rozšíření nemusí fungovat správně nebo mohou mít vliv na výkon. V případě problému (nefunkčnost webu, pomalost) vypněte rozšíření jedno po druhém, abyste zjistili zdroj.



## Denní použití



### Interface a jedinečné vlastnosti




![Outil de personnalisation pinceau](assets/fr/13.webp)


*Orion brush menu pro přizpůsobení zobrazení: velikost písma, téma (světlé/tmavé), deaktivace samolepicích záhlaví a odstranění rušivých Elements*



**Nástroj Štětec: pokročilé přizpůsobení**



Nástroj **brush** společnosti Orion je jedinečná funkce, která umožňuje přizpůsobit zobrazení každé webové stránky:



**Možnosti tématu**:




- Přepínání mezi světlými a tmavými motivy pro každý web
- Automatické přizpůsobení systémovým preferencím



**Typografická kontrola**:




- Velikost písma**: Tlačítky A- a A+ upravte čitelnost
- Styl písma**: Změňte rodinu písma (výchozí nebo vlastní)



**Čištění Interface**:




- Zakázat lepivé záhlaví**: Odstraní záhlaví, která při rolování zůstávají přilepená nahoře
- Vymazat Elements**: (reklamy, vyskakovací okna, bannery se soubory cookie)
  - Klikněte na "+ Vymazat" a poté vyberte položku, která má být skryta
  - Velmi užitečné pro weby s trvalými reklamami nebo vizuálním sledováním Elements



**Vytrvalost**: Všechna tato nastavení se ukládají pro každou doménu a automaticky se znovu použijí při příští návštěvě.



**Pokročilá správa karet**:




- Svislé záložky**: Aktivace přes panel nabídek (funkce Karty na boku)
- Kompaktní karty**: V Předvolbách → Karty → Rozložení "Kompaktní" pro úsporu místa
- Skupiny karet**: Uspořádejte si relace podle témat
- Více profilů**: Vytvářejte samostatné identity prostřednictvím panelu nabídek (funkce Profily) se zcela izolovanými údaji



**Režim nízké spotřeby**: Tento režim, inspirovaný iPhonem, automaticky pozastaví neaktivní karty po 5 minutách a může snížit spotřebu energie až o 90 %. Aktivujte ho v nabídkovém panelu Orionu na Macu nebo v nastavení na iOS.



**Vestavěné nástroje** (nabídka Úpravy a další):




- Upravit text na stránce**: dočasná úprava libovolného textu (nabídka Upravit)
- Povolit kopírování a vkládání**: Obejde omezení kopírování (nabídka Úpravy)
- Kopírovat čistý odkaz**: Kliknutím pravým tlačítkem myši na odkaz odstraníte parametry sledování
- Režim Focus**: navigace přes celou obrazovku bez rozptylování
- Obraz v obraze**: Sledujte videa v plovoucím okně
- Otevřít v internetovém archivu**: Přímý přístup k archivovaným verzím
- Zpráva o ochraně osobních údajů**: Kliknutím na štít 🛡️ zobrazíte položky blokované podle stránek



### Správa soukromého procházení



Privátní navigace Orion (⌘⇧N) nabízí:




- Úplná izolace souborů cookie a relací
- Automatické odstranění při uzavření
- Historie a deaktivace mezipaměti
- Zvýšená ochrana proti snímání otisků prstů



**Tip**: Pro pokročilé rozdělení vytvořte **oddělené profily** pomocí panelu nabídek (funkce Profily). Každý profil se v Docku zobrazí jako samostatná aplikace s vlastním nastavením, rozšířeními a zcela izolovanými daty.



### Optimalizace výkonu a ochrana soukromí



Aby byl Orion rychlý a soukromý:




- Rozšíření**: Omezte na nezbytné minimum (může snížit výkon)
- Režim nízké spotřeby**: Aktivujte při dlouhých sezeních (možná úspora 90 %)
- Zpráva o ochraně osobních údajů**: Kliknutím na štít 🛡️ zobrazíte blokování v reálném čase
- Vizuální přizpůsobení**: Pomocí štětce 🖌️ můžete přizpůsobit zobrazení a odstranit rušivý prvek Elements
- Kopírovat čistý odkaz**: Klepnutím pravým tlačítkem myši zkopírujete odkazy bez sledovačů
- Samostatné profily**: Pomocí vyhrazených profilů můžete své aktivity rozdělit na části
- Nastavení webových stránek**: Kliknutím na ozubené kolečko ⚙️ upravíte oprávnění podle webu
- Pravidelné čištění**: Vymazat mezipaměť přes Orion → Vymazat data o prohlížení



## Srovnání s alternativami



| Critère | Orion | Safari | Chrome | Firefox | Brave |
|---------|-------|--------|---------|----------|--------|
| **Télémétrie** | Aucune | Minimale | Extensive | Modérée | Minimale |
| **Bloqueur natif** | 99,9% efficace | Basique | Absent | Partiel | Complet |
| **Extensions** | Chrome + Firefox | Limitées | Chrome uniquement | Firefox uniquement | Chrome uniquement |
| **Performance Mac** | Excellente | Excellente | Bonne | Moyenne | Bonne |
| **Consommation RAM** | Très faible | Faible | Élevée | Moyenne | Moyenne |
| **Open Source** | Partiel | Partiel (WebKit) | Partiel | Complet | Complet |
| **Plateformes** | Mac/iOS | Mac/iOS | Toutes | Toutes | Toutes |

**Oproti Safari**: Orion nabízí vynikající ochranu díky pokročilému blokování a podpoře rozšíření, přičemž zachovává výkon WebKitu.



**Oproti Chrome**: bezkonkurenční soukromí bez omezení kompatibility díky podpoře rozšíření pro Chrome.



**Oproti Firefoxu**: Rychlejší na Macu, Interface intuitivnější, ale méně podrobné ovládání a ne open-source.



**Versus Brave**: Orion se však vyhýbá kontroverzím ohledně kryptografického systému/BAT a nabízí lepší integraci se systémem Apple.



## Doporučené případy použití



**Ideální pro**:




- Uživatelé Apple hledají více soukromí než Safari
- Lidé, kteří chtějí blokovat všechny reklamy (včetně YouTube) bez rozšíření
- Vývojáři vyžadující devtools WebKit s integrovanou ochranou soukromí
- Uživatelé IPhone, kteří chtějí rozšíření pro stolní počítače v mobilu (jedinečná inovace)
- Profesionálové, kteří potřebují rozdělit své činnosti (více profilů)
- Mobilní uživatelé, kteří hledají lepší správu baterie (režim nízké spotřeby)



**Vyhněte se, pokud**:




- Používáte hlavně Windows/Linux (není k dispozici žádná verze)
- Plně otevřený zdrojový kód je pro váš model hrozeb nezbytný
- Jste závislí na konkrétních rozšířeních, která nemusí fungovat
- Potřebujete synchronizaci napříč platformami mimo ekosystém Apple
- Dáváte přednost osvědčenému, stabilnímu řešení (trvalý status beta od roku 2021)



## Pozornost a bezpečnost



### Jedinečné bezpečnostní prvky



**Revoluční ochrana proti otiskům prstů**: Orion je jediným prohlížečem, který zcela blokuje spuštění skriptů fingerprintingu dříve, než mohou skenovat váš systém. Tento přístup "žádný spuštěný skript = žádný možný fingerprinting" překonává tradiční maskovací metody používané jinými prohlížeči.



**Transparentní bílá listina**: Orion udržuje malý veřejný seznam stránek (browserbench.org, wizzair.com), na kterých je blokování automaticky vypnuto, aby se předešlo poruchám. Tato transparentnost umožňuje uživatelům přesně pochopit, kdy a proč je blokování zmírněno.



**Neauditovaná rozšíření**: Podpora rozšíření pro Chrome/Firefox přináší další rizika, protože tato rozšíření nebyla navržena pro WebKit a nejsou pro toto prostředí speciálně auditována.



### Údržba a aktualizace





- Automatické aktualizace**: Orion se v systému macOS aktualizuje automaticky prostřednictvím Sparkle
- Sledování zranitelnosti**: Pravidelně kontrolujte poznámky k vydání, zda neobsahují bezpečnostní záplaty
- Hlášení chyb**: Pro hlášení problémů použijte [orionfeedback.org](https://orionfeedback.org)




## Závěr



Prohlížeč Orion představuje významný krok vpřed v oblasti ochrany soukromí v systémech macOS a iOS. Jeho přístup s nulovou telemetrií v kombinaci s mimořádně účinným nativním blokováním a jedinečnou podporou univerzálních rozšíření z něj dělá vynikající volbu pro uživatele Apple, kteří dbají na své soukromí.



**Důležité**: Orion zůstává od roku 2021 v trvalé beta verzi s omezeními kompatibility rozšíření a riziky spojenými s WebKitem. Posuďte tyto kompromisy podle svého modelu hrozeb.



Pro každodenní použití na Macu nebo iPhonu je to pravděpodobně nejlepší kompromis mezi důvěrností, výkonem a snadným používáním, který je v ekosystému Apple k dispozici, pokud ovšem akceptujete jeho omezení.



Nezapomeňte, že ochrana vašeho soukromí nezávisí jen na prohlížeči. Pro optimální zabezpečení online kombinujte Orion s osvědčenými postupy (silná hesla, 2FA, případně VPN).



## Zdroje a podpora



### Oficiální dokumentace




- Oficiální webové stránky**: [kagi.com/orion](https://kagi.com/orion/)
- Úplné znění často kladených otázek**: [browser.kagi.com/faq](https://browser.kagi.com/faq)
- Fórum Společenství**: [community.kagi.com](https://community.kagi.com)
- Sledování chyb**: [orionfeedback.org](https://orionfeedback.org)
- GitHub Orion**: [github.com/OrionBrowser](https://github.com/OrionBrowser) - Open-source komponenty
- Blog Kagi**: [blog.kagi.com](https://blog.kagi.com) - Novinky a aktualizace



### Doporučené ověřovací testy



Po konfiguraci otestujte nastavení:




- [Zakryj své stopy (EFF)](https://coveryourtracks.eff.org/) - Test otisků prstů
- [Test úniku DNS](https://www.dnsleaktest.com/) - Kontrola úniků DNS
- [BrowserLeaks](https://browserleaks.com/) - Kompletní sada testů soukromí



### Alternativy k Plan ₿ Network


Pro maximální ochranu si přečtěte naše další průvodce:




- [Firefox hardened](https://planb.network/tutorials/computer-security/communication/firefox-11814cec-3415-4ed9-a06e-f6fda5c9510f) - Pokročilá konfigurace pro více platforem
- [Tor Browser](https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb) - Úplná síťová anonymita
- [Mullvad Browser](https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e) - Maximální ochrana otisků prstů



Pokud se chcete dozvědět více o historii a fungování prohlížečů a také o hlavních digitálních objektech ve vašem každodenním životě, zvu vás k návštěvě našeho nového bezplatného školení SCU 202, které je k dispozici na Plan ₿ Network:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
