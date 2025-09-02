---
name: LibreWolf
description: Jak používat prohlížeč soukromí LibreWolf
---

![cover](assets/cover.webp)



Každé kliknutí, každé vyhledávání, každá navštívená stránka: váš webový prohlížeč se stal důmyslným donašečem, který napájí globální komerční sledovací systém. Prohlížeč Google Chrome, který používají více než 3 miliardy lidí, mění vaše každodenní prohlížení na lukrativní data pro reklamní giganty. Dokonce i Firefox, navzdory své pověsti "etického" prohlížeče, ve výchozím nastavení aktivuje telemetrické mechanismy, které předávají vaše zvyky při prohlížení webu společnosti Mozilla.



Tato skutečnost vyvolává zásadní otázku: je ještě možné svobodně surfovat po internetu, aniž bychom byli neustále špehováni a profilováni? Naštěstí je odpověď kladná, a to díky komunitním projektům, které vracejí uživatele do centra svého zájmu.



Společnost LibreWolf ztělesňuje tuto filozofii digitálního odporu. Tento prohlížeč, který je dílem komunity nezávislých vývojářů, mění Firefox ve skutečný štít proti online dohledu. Tam, kde se komerční prohlížeče snaží zpeněžit vaši pozornost, LibreWolf dělá pravý opak: činí vás neviditelnými pro sledovací zařízení a zároveň zachovává plynulé a moderní prohlížení.



V tomto kurzu zjistíme, jak může LibreWolf změnit způsob, jakým surfujete na webu, a nabídne vám spolehlivou ochranu proti sledování, aniž by to bylo na úkor výkonu nebo kompatibility s webem.



![LIBREWOLF](assets/fr/01.webp)


*Podíl webových prohlížečů na trhu: Podíl prohlížeče Chrome na trhu je 65 %, následují Safari a Edge. Tato dominance vyvolává otázky týkající se rozmanitosti webu a ochrany soukromí*



## Představujeme LibreWolf



**FreeWolf** je webový prohlížeč s otevřeným zdrojovým kódem odvozený od prohlížeče Mozilla Firefox, který vyvíjí a spravuje nezávislá komunita nadšenců pro svobodný software. Jeho hlavním cílem je nabídnout prohlížení zaměřené na soukromí, bezpečnost a svobodu uživatele.



Konkrétně LibreWolf využívá engine Gecko z Firefoxu, ale s radikálně odlišnou filozofií: zatímco Firefox musí vyvažovat soukromí a snadnost používání, LibreWolf volí standardní soukromí. Projekt odstraňuje vše, co by mohlo narušit vaše soukromí (telemetrie, sběr dat, sponzorované moduly), a zároveň integruje rozšířená nastavení zabezpečení.



### Cíle: soukromí a svoboda



Cílem LibreWolf je maximalizovat ochranu proti sledování a snímání otisků prstů a zároveň zvýšit zabezpečení prohlížeče. Mezi jeho hlavní cíle patří:





- Odstranění veškeré telemetrie a shromažďování dat** v prohlížeči Firefox
- Zakázat funkce, které jsou v rozporu se svobodou uživatele**, například proprietární moduly DRM
- Použití nastavení ochrany soukromí/bezpečnosti** a specifických záplat od samého počátku
- Rozvoj Společenství zaručuje transparentnost a nezávislost** na komerčních zájmech



LibreWolf se zkrátka prezentuje jako "Firefox, jaký by byl, kdyby soukromí bylo nejvyšší prioritou" - prohlížeč, který vás respektuje ve výchozím nastavení, bez nutnosti další konfigurace.



### Hlavní funkce



LibreWolf od samého počátku nabízí řadu funkcí zaměřených na ochranu soukromí:



**Žádná telemetrie nebo sběr dat:** Na rozdíl od prohlížečů Chrome nebo Firefox, které odesílají určité statistiky o používání, LibreWolf neshromažďuje vůbec nic z vašeho prohlížení. Žádná hlášení o pádech, žádné uživatelské studie, žádné sponzorované návrhy.



**Společnost LibreWolf nativně integruje rozšíření uBlock Origin, jeden z nejlepších blokátorů reklam a sledovacích zařízení na trhu. Ve výchozím nastavení LibreWolf agresivně filtruje vše, co by vás mohlo sledovat online (rušivé reklamy, sledovací skripty, kryptoměna Mining).



**Soukromý vyhledávač ve výchozím nastavení:** LibreWolf ve výchozím nastavení používá jako výchozí vyhledávač DuckDuckGo, který nezachovává historii vašich dotazů. K dispozici jsou také další alternativy zaměřené na soukromí (Searx, Qwant, Whoogle).



**Zesílená ochrana proti otiskům prstů:** Otisk prstu umožňuje jedinečnou identifikaci prohlížeče prostřednictvím jeho konfigurace, a to i bez souborů cookie. Proti tomu LibreWolf aktivuje technologii RFP (Resist Fingerprinting) z projektu Tor, aby byl váš prohlížeč co nejobecnější. Testy ukazují, že standardní Firefox je v nástrojích, jako je coveryourtracks.eff.org, jedinečný na ~90 %, zatímco v případě LibreWolf pouze na ~10-20 % (tato čísla jsou orientační a mohou se lišit v závislosti na konfiguraci softwaru a hardwaru a nainstalovaných rozšířeních).



![LIBREWOLF](assets/fr/07.webp)


*EFF testovací stránku [Cover Your Tracks](https://coveryourtracks.eff.org/) pomocí tlačítka TEST YOUR BROWSER. Tato stránka slouží k vyhodnocení ochrany proti sledovacím zařízením a snímání otisků prstů



![LIBREWOLF](assets/fr/08.webp)


*Výsledek testu Zakryj stopy. Zobrazí se zpráva "máte silnou ochranu proti sledování na webu", která ukazuje účinnost ochrany LibreWolf.*



**Společnost LibreWolf ve výchozím nastavení aktivuje přísná nastavení zabezpečení. Vylepšená ochrana sledování ve Firefoxu je nastavena na úroveň Strict, aby blokovala tisíce sledovacích zařízení, souborů cookie třetích stran a škodlivého obsahu. Aktivuje také izolaci stránek a souborů cookie (*Total Cookie Protection*) pro rozdělení dat pro každou doménu a omezuje WebRTC (omezuje *ICE kandidáty* a směrování přes proxy server, pokud je proxy server přítomen), aby se snížilo riziko úniku IP Address.



**Rychlé aktualizace enginu:** Projekt velmi pečlivě sleduje vývoj Firefoxu: LibreWolf je vždy založen na nejnovější stabilní verzi Firefoxu a správci se snaží vydat novou verzi do 24 až 72 hodin po každém oficiálním vydání Firefoxu.



## Výhody a nevýhody



### Výhody





- Žádná telemetrie ani nežádoucí připojení:** LibreWolf nepřenáší žádné údaje o používání, čímž je zajištěno naprosté respektování vašeho soukromí.





- Open-source a komunita:** Projekt je 100% open-source a je udržován dobrovolníky. Tato nezávislost zaručuje, že vývoj nebude ovlivňovat žádný reklamní model.





- Předkonfigurováno pro ochranu soukromí:** LibreWolf vám ušetří drahocenný čas: nemusíte trávit hodiny nastavováním Firefoxu, vše je již hotovo.





- Nativní blokování/sledování reklam:** uBlock Origin je integrován jako standard, takže pro ochranu před reklamami a chybami nemusíte dělat vůbec nic.





- Vynikající ochrana proti otiskům prstů:** Díky RFP a četným nastavením soukromí LibreWolf výrazně snižuje vaši jedinečnou digitální stopu na webu.





- Vyšší výkon a nižší hmotnost:** Díky odstranění telemetrie a některých nepodstatných funkcí může být LibreWolf o něco rychlejší a méně náročný na spotřebu energie než standardní Firefox.



### Nevýhody a omezení





- Žádné vestavěné automatické aktualizace:** LibreWolf se sám neaktualizuje. Je na vás, abyste si nainstalovali nové verze, jakmile jsou vydány, a zůstali tak v bezpečí.





- Snížená kompatibilita s některými službami:** Vzhledem k velmi přísnému nastavení může mít LibreWolf na některých webových stránkách problémy. Streamovací platformy Netflix a Disney+ nebudou fungovat, protože LibreWolf ve výchozím nastavení vypíná Widevine DRM.





- Žádná vestavěná anonymní síť:** Na rozdíl od prohlížeče Tor Browser nesměruje LibreWolf provoz přes Tor nebo VPN sám. Pokud potřebujete síťovou anonymitu, budete muset ručně nakonfigurovat proxy server/VPN.





- Neperzistentní soubory cookie a relace (výchozí nastavení):** Z důvodu zachování důvěrnosti LibreWolf odstraní soubory cookie, historii a data webu pokaždé, když zavřete prohlížeč. Při každém přihlášení se budete muset znovu přihlásit ke svým účtům.





- Žádná mobilní verze ani cloudová synchronizace:** LibreWolf je k dispozici pouze na počítači (Windows, Linux, macOS). Neexistuje žádná mobilní aplikace, a tedy ani synchronizace účtů nebo záložek prostřednictvím cloudu.



## Instalace aplikace LibreWolf



**Oficiální webové stránky:** [librewolf.net](https://librewolf.net)



LibreWolf je k dispozici pro všechny hlavní desktopové operační systémy: Linux, Windows a macOS. Chcete-li si LibreWolf stáhnout, navštivte oficiální webové stránky:



![LIBREWOLF](assets/fr/02.webp)


*Domovská stránka LibreWolf (librewolf.net) zobrazující logo prohlížeče, modré tlačítko Install a odkazy na zdrojový kód a dokumentaci. Velká modrá šipka ukazuje na tlačítko Instalovat*



Kliknutím na tlačítko "Instalace" získáte přístup k podrobným pokynům pro váš operační systém:



![LIBREWOLF](assets/fr/03.webp)


*Stránka pro výběr operačního systému pro stažení LibreWolf.*



Instalace se liší v závislosti na operačním systému:



### V systému Linux


LibreWolf nabízí sestavení pro mnoho distribucí. Pro Debian/Ubuntu a odvozené systémy je k dispozici oficiální repozitář APT. Alternativně je LibreWolf publikován ve formátu Flatpak na Flathubu:


```
flatpak install flathub io.gitlab.librewolf-community
```



### V systému Windows


Stáhněte si instalační program (.exe) z oficiálních webových stránek nebo použijte:




- Chocolatey:** `choco install librewolf`
- WinGet:** `winget install librewolf`



### V systému macOS


LibreWolf je k dispozici jako balíček .dmg pro Mac. Stáhněte si obraz disku z oficiálních webových stránek a přetáhněte aplikaci LibreWolf do složky Aplikace. Případně ji můžete nainstalovat pomocí nástroje Homebrew.




## Konfigurace a první použití



Při prvním spuštění si všimnete známého Firefoxu Interface, který je však více osekaný: domovská stránka obsahuje pouze vyhledávací panel a žádné sponzorované nabídky. Na panelu nástrojů uvidíte ikonu uBlock Origin - znamení, že je blokátor aktivní.



![LIBREWOLF](assets/fr/04.webp)


*Domovská stránka LibreWolf s rozšířeními a menu. Modrá šipka v pravém horním rohu označuje ikonu menu (tři vodorovné pruhy)



LibreWolf automaticky načte vaše stránky v režimu "strict" (proti sledování) a výchozím vyhledávačem bude DuckDuckGo. Můžete zkusit navštívit testovací stránku pro sledování (např. amiunique.org) a pozorovat vystavenou stopu - měla by být mnohem obecnější než u standardního prohlížeče.



### Nastavení ochrany osobních údajů



Systém LibreWolf je již optimálně nakonfigurován pro ochranu soukromí. V nabídce Menu → Možnosti → Soukromí a zabezpečení uvidíte, že LibreWolf je nastaven na režim Zvýšená ochrana sledování: Přísné. Tento režim blokuje:




- Sledování mezi lokalitami
- Soubory cookie třetích stran
- Známý obsah sledování
- Těžba kryptoměn
- Digitální detektory otisků prstů



![LIBREWOLF](assets/fr/05.webp)


*Stránka karty Zabezpečení a soukromí zobrazující nastavení zabezpečení LibreWolf.*



WebRTC je vypnuté (zabraňuje úniku IP) a je zavedena celková ochrana souborů cookie. Telemetrie a průzkumy Firefoxu jsou zcela zakázány.



### Správa souborů cookie a historie



Ve výchozím nastavení odstraňuje LibreWolf soubory cookie a místní úložiště při každém zavření. Pokud vám toto chování vadí, můžete jej upravit v části Soukromí a zabezpečení → Soubory cookie a data webu zrušením zaškrtnutí políčka "Smazat soubory cookie a data webu při ukončení aplikace LibreWolf".



![LIBREWOLF](assets/fr/06.webp)


*Stejná stránka o kousek níže, kde se zobrazuje možnost vymazání souborů cookie po zavření prohlížeče*



### Přidání užitečných rozšíření



LibreWolf zásadně nedoporučuje přidávat zbytečná rozšíření, protože každé rozšíření může být sledovacím vektorem. Nicméně některá renomovaná rozšíření mohou zlepšit vaše zkušenosti:




- Kontejnery pro více účtů ve Firefoxu** (od Mozilly) pro rozdělené prohlížení stránek
- Decentraleyes** nebo **LocalCDN** pro lokální obsluhu společných knihoven



Vyhněte se zejména "bezplatným VPN" rozšířením nebo pochybným proxy serverům - uBlock Origin již pokrývá 99 % vašich potřeb.



## Každodenní použití



### Každodenní prohlížení webu


Používejte LibreWolf pro každodenní internetové aktivity. Hlavní rozdíl oproti jiným prohlížečům spočívá v tom, že zanecháváte mnohem méně reklamních stop. Na mnoha webech zmizí bannery "Accept cookie" díky filtrovacím seznamům uBlocku.



### Použití soukromých karet k rozdělení


Přestože LibreWolf na konci relace vše smaže, může být užitečné otevřít soukromé okno prohlížeče (Ctrl+Shift+P) pro určité úkoly během relace, aby bylo možné oddělit určitou identitu.



### Využití kontejnerů s více účty


Instalace rozšíření Kontejnery pro více účtů vám může výrazně pomoci rozdělit vaše aktivity do nepropustných sil. Můžete například definovat kontejner "Bankovnictví" pro bankovní stránky, kontejner "Sociální sítě" pro Facebook/Twitter atd. Každý kontejner má své vlastní soubory cookie, relace a izolované úložiště. Každý kontejner má své vlastní soubory cookie, relace a izolované úložiště.



### Přesné vyladění správy oprávnění podle lokalit


LibreWolf umožňuje kontrolovat oprávnění, která udělujete webům (poloha, kamera, mikrofon, oznámení), případ od případu. Udělujte oprávnění pouze důvěryhodným webům a v případě potřeby.



## Osvědčené postupy s LibreWolf



1. **Udržujte LibreWolf v aktuálním stavu:** Pravidelně kontrolujte, zda na webu nejsou nové verze, zejména po vydání stabilní verze Firefoxu.



2. **Vyhněte se směšování osobní identity a soukromého procházení:** V ideálním případě byste se neměli přihlašovat pomocí osobních účtů ve stejné relaci, kdy provádíte citlivý výzkum.



3. **Nezatěžujte LibreWolf zbytečnými rozšířeními:** Každé nainstalované rozšíření může představovat bezpečnostní riziko nebo riziko otisků prstů.



4. **Používejte navíc VPN nebo Tor proxy:** LibreWolf vás neanonymizuje pro poskytovatele internetových služeb. Pro zajištění síťové anonymity můžete LibreWolf používat za důvěryhodnou VPN.



5. **Uložení důležitých dat:** Záložky, hesla, pokud jsou uložena lokálně. Zvažte použití externího správce hesel (KeePassXC, Bitwarden) namísto základního správce hesel v prohlížeči.



## Srovnání s ostatními prohlížeči



LibreWolf je součástí "sady nástrojů" prohlížečů zaměřených na ochranu soukromí:



**LibreWolf vs. Firefox:** LibreWolf přichází již zpevněný a bez telemetrie. Firefox si zachovává výhodu synchronizace s více zařízeními a velmi rozsáhlou uživatelskou základnu, ale k dosažení úrovně důvěrnosti LibreWolf vyžaduje ruční konfiguraci.



**Brave používá kód Chrome/Chromium a integruje obchodní model prostřednictvím volitelného reklamního programu. LibreWolf je komunitní Fork pro Firefox, zachovává svobodný ekosystém Mozilly a nemá vazby na Google.



**LibreWolf vs Tor Browser:** Tor Browser je nenahraditelný pro anonymitu tváří v tvář silnému dohledu, ale je pomalý a nepohodlný při každodenním používání. LibreWolf je pro každodenní prohlížení klasického webu mnohem rychlejší a praktičtější.



**LibreWolf vs. Mullvad Browser:** Mullvad Browser jde ve standardizaci ještě dál, ale za cenu snížení použitelnosti (nemožnost uchovávat přihlašovací cookie). LibreWolf dosahuje rovnováhy: je velmi soukromý, ale každodenně použitelný.



## Závěr



LibreWolf představuje vynikající řešení pro ty, kteří hledají mimořádně soukromý "každodenní" prohlížeč, aniž by museli jít až do extrémní anonymity Toru. Je ideální volbou pro aktivisty, novináře, vývojáře nebo náročné uživatele, kteří chtějí klasické prohlížení webu (rychlé, kompatibilní s moderními weby) a zároveň uniknout sledování reklam a velkým technologiím.



Přestože má určitá omezení (žádné automatické aktualizace, omezená kompatibilita s některými službami), je LibreWolf cenným nástrojem v arzenálu každého, kdo chce získat kontrolu nad svým digitálním soukromím. Díky snadnému použití a výchozí konfiguraci je moudrou volbou pro uživatele, kteří dbají na své soukromí.



## Zdroje



### Oficiální dokumentace




- [oficiální stránky LibreWolf](https://librewolf.net)
- [Zdrojový kód na Codeberg](https://codeberg.org/librewolf)
- [Oficiální FAQ](https://librewolf.net/docs/faq)



### Průvodci a srovnání




- [Průvodci ochranou osobních údajů](https://www.privacyguides.org/en/desktop-browsers/)
- [Srovnávací testy soukromí](https://privacytests.org)



### Podpora Společenství




- [Subreddit r/LibreWolf](https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf](https://matrix.to/#/#librewolf:matrix.org)