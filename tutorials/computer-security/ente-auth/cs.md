---
name: Ente Auth
description: Autentikátor 2FA s otevřeným zdrojovým kódem a šifrováním end-to-end
---
![cover](assets/cover.webp)



Dvoufaktorové ověřování (2FA) se stalo nepostradatelným pro zabezpečení našich online účtů. Kromě obvyklého hesla vyžaduje dočasný kód, který obvykle generuje speciální aplikace. Tento mechanismus, známý jako TOTP (Time-Based One-Time Password), zaručuje, že i v případě prozrazení hesla se útočník nedostane k vašemu účtu, pokud nebude mít k dispozici tento druhý faktor, který se obnovuje každých 30 sekund.



Výběr správné autentizační aplikace však není triviální. Authenticator Google je sice populární, ale má zásadní omezení: proprietární kód, který nelze zkontrolovat, synchronizace bez koncového šifrování a riziko úplné ztráty kódů v případě problémů s telefonem. Jiná řešení, například Authy, vyžadují telefonní číslo a nezaručují úplné utajení.



**Ente Auth** je moderní a bezpečnou alternativou. Tato bezplatná multiplatformní aplikace s otevřeným zdrojovým kódem, kterou vyvinul tým stojící za aplikací [Ente Photos](https://ente.io), nabízí end-to-end šifrované zálohování do cloudu a bezproblémovou synchronizaci mezi všemi vašimi zařízeními. Na rozdíl od proprietárních řešení vám Ente Auth poskytuje úplnou kontrolu nad vašimi ověřovacími kódy, aniž by bylo ohroženo vaše soukromí.



V tomto návodu vám krok za krokem ukážeme, jak nainstalovat a používat službu Ente Auth a čím se toto řešení liší od tradičních ověřovatelů.



## Představení služby Ente Auth



Službu Ente Auth vyvinul tým, který stojí za Ente Photos, službou pro ukládání fotografií s koncovým šifrováním a ochranou soukromí. V souladu s filozofií Ente ("Ente" znamená v malajalámštině "můj", což symbolizuje kontrolu nad vašimi daty) byla služba Ente Auth navržena tak, aby uživatelé měli zpět plnou kontrolu nad svými dvoufaktorovými ověřovacími kódy.



### Hlavní funkce



**Standardní kódy TOTP**: Ente Auth generuje dočasné kódy kompatibilní s většinou služeb (GitHub, Google, Binance, ProtonMail atd.). Můžete přidat tolik účtů 2FA, kolik potřebujete, a aplikace vypočítá kódy na základě zadaných tajemství.



**Koncové šifrované zálohování do cloudu**: Vaše kódy jsou bezpečně uloženy online. Dešifrovat je můžete pouze vy - šifrovací klíč je odvozen od vašeho hesla a je znám pouze vám. Ente (server) nezná vaše tajemství, ani názvy vašich účtů, protože vše je šifrováno na straně klienta pomocí architektury zero-knowledge.



**Synchronizace více zařízení**: Můžete si nainstalovat Ente Auth na několik zařízení (chytrý telefon, tablet, počítač) a přistupovat ke svým kódům na všech z nich. Veškeré změny se automaticky a okamžitě přenášejí do ostatních zařízení prostřednictvím šifrovaného cloudu, což vám poskytuje velkou flexibilitu při každodenní práci.



**Minimalistický, intuitivní Interface**: Aplikace nabízí zjednodušenou verzi Interface, kterou se snadno naučí i netechničtí uživatelé. u účtů 2FA se zobrazuje název služby, vaše přihlašovací jméno a šestimístný kód, který se aktualizuje v reálném čase. Ente Auth také zobrazuje další kód s několikasekundovým předstihem, abyste se vyhnuli tomu, že vás zastihne vypršení platnosti.



**Otevřený zdroj a auditovaný**: Zdrojový kód Ente Auth je [veřejný na GitHubu](https://github.com/ente-io/auth) pod licencí AGPL v3.0. Každý vývojář jej může auditovat a zkontrolovat, zda neobsahuje chyby nebo nežádoucí chování. Implementovaná kryptografie byla předmětem [nezávislého externího auditu](https://ente.io/blog/cryptography-audit/), což je zárukou serióznosti zabezpečení aplikace.



### Výhody a omezení



**Výhody:**




- Ochrana soukromí již od návrhu s end-to-end šifrováním
- Bezpečná synchronizace mezi všemi zařízeními
- Auditovatelný otevřený zdrojový kód
- Interface přehledný, intuitivní uživatel Interface
- Automatické zálohování, které zabrání ztrátě kódů
- K dispozici na všech platformách (mobilní i stolní)



**Omezení:**




- Pro synchronizaci je nutné připojení k internetu
- Pokročilí uživatelé mohou dát přednost 100% offline řešením, jako je Aegis (pouze pro Android)
- Relativně nové ve srovnání se zavedenými řešeními



## Instalace



Služba Ente Auth je k dispozici na většině populárních platforem. Aplikaci si můžete stáhnout z [oficiálních webových stránek](https://ente.io/auth) nebo z oficiálních obchodů.



![Installation d'Ente Auth](assets/fr/01.webp)



*Stránka ke stažení Ente Auth se všemi dostupnými platformami*



### Android


Máte několik možností:




- Obchod Google Play**: Pro klasickou instalaci vyhledejte "Ente Auth"
- F-Droid**: Froid-Droid: k dispozici z katalogu aplikací s otevřeným zdrojovým kódem pro Android, se zárukou ověřené konstrukce a bez proprietárního obsahu
- Ruční instalace** : Soubory APK lze stáhnout ze [stránky projektu na GitHubu](https://github.com/ente-io/auth/releases) s integrovaným upozorněním na nové verze



### iOS (iPhone/iPad)


Nainstalujte si aplikaci Ente Auth přímo z obchodu Apple App Store vyhledáním jejího názvu. Aplikaci pro iOS lze spustit také na počítačích Mac vybavených křemíkovými čipy Apple (M1/M2) prostřednictvím obchodu Mac App Store.



### Počítače (Windows, macOS, Linux)


Ente Auth nabízí nativní desktopové aplikace. Navštivte [ente.io/download](https://ente.io/download) nebo [Releases section of GitHub](https://github.com/ente-io/auth/releases) :





- Windows**: Dodává se instalační program EXE
- macOS**: Přetažení obrazu disku DMG v aplikacích
- Linux** : K dispozici je několik formátů (AppImage portable, .deb pro Debian/Ubuntu, .rpm pro Fedoru/Red Hat)



**Poznámka:** Tento návod je založen na verzi Ente Auth 4.4.4 a novější. Starší verze mohou mít drobné rozdíly v Interface.



### Interface Web


Ke svým kódům můžete bez instalace přistupovat prostřednictvím [auth.ente.io](https://auth.ente.io) z libovolného prohlížeče. Web Interface je omezen na prohlížení kódů (užitečné pro řešení problémů), protože přidávání účtů vyžaduje z bezpečnostních důvodů mobilní nebo desktopovou aplikaci.



## První konfigurace



### Vytvoření účtu



Při prvním spuštění služby Ente Auth máte dvě možnosti:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Domovská obrazovka Ente Auth s možnostmi vytvoření účtu*



**S účtem (doporučeno)**: Zvolte "Vytvořit účet" a zadejte svůj e-mail Address a heslo. **Důležité**: toto heslo slouží jako hlavní heslo pro šifrování vašich dat. Zvolte silné, jedinečné heslo, protože neexistuje běžný postup obnovení bez ztráty dat. Pokud ho špatně zadáte, vaše zašifrovaná data budou neobnovitelná.



**Offline režim**: Pokud chcete aplikaci používat lokálně bez cloudu, vyberte možnost "Použít bez záloh". V tomto režimu zůstanou vaše kódy v zařízení, ale budete je muset ručně exportovat, abyste o ně nepřišli.



![Vérification email et récupération de clé](assets/fr/03.webp)



*Proces ověření e-mailu a vygenerování klíče pro obnovení o 24 slovech*



Pro ověření vytvoření účtu a umožnění obnovy na novém zařízení může být vyžadováno ověření e-mailem. Služba Ente Auth vám také poskytne klíč pro obnovení o 24 slovech (na základě metody BIP39). **Tento klíč** si bezpodmínečně uložte na bezpečné místo: je to jediný prostředek pro obnovení dat, pokud zapomenete heslo.



### Místní zabezpečení



Důrazně doporučuji povolit místní ochranu pomocí kódu nebo biometrie. Přejděte do **Nastavení → Zabezpečení → Zamykací obrazovka** a nakonfigurujte :





- Biometrické odemykání**: V závislosti na možnostech vašeho zařízení: ID obličeje, otisk prstu
- Kód PIN/heslo specifické pro danou aplikaci**
- Zpoždění automatického zamykání**: např. "Ihned" nebo po 30 sekundách nečinnosti



Tato ochrana zabraňuje neoprávněnému přístupu ke kódům, pokud někdo získá přístup k odemčenému telefonu. Všimněte si, že tento zámek je dodatečnou překážkou: vaše data zůstanou end-to-end zašifrována i bez této ochrany.



## Přidání účtů 2FA



### Standardní postup



Pro přidání nového účtu 2FA si uveďme konkrétní příklad aktivace 2FA v zařízení Bull Bitcoin :



![Configuration du premier compte](assets/fr/04.webp)



*Hlavní zařízení Interface společnosti Ente Auth je připraveno k přidání prvního účtu 2FA*



**Služební strana (Bull Bitcoin)**: Přihlaste se ke svému účtu Bull Bitcoin, přejděte do nastavení zabezpečení a povolte dvoufaktorové ověřování.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Nabídka bezpečnostních nastavení Interface Bull Bitcoin*



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Možnost zapnutí dvoufaktorového ověřování v zařízení Bull Bitcoin*



Služba poté zobrazí kód QR, který můžete naskenovat pomocí ověřovací aplikace:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*QR kód vygenerovaný aplikací Bull Bitcoin, který lze naskenovat pomocí autentizátoru*



**In Ente Auth**: Klepněte na "Enter a setup key" a poté naskenujte QR kód zobrazený společností Bull Bitcoin. Ente Auth automaticky rozpozná účet a vyplní pole.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Konfigurace údajů o účtu Bull Bitcoin v aplikaci Ente Auth*



Název služby a přihlašovací jméno si můžete přizpůsobit, abyste ji snáze našli. Pokročilá nastavení (algoritmus SHA1, 30s perioda, 6 číslic) jsou ve výchozím nastavení obecně správná.



**Ověření na straně služby**: Pro dokončení aktivace se vraťte do Bull Bitcoin a zadejte šestimístný kód vygenerovaný službou Ente Auth.



![Saisie du code 2FA](assets/fr/09.webp)



*Zadejte kód vygenerovaný službou Ente Auth pro ověření aktivace 2FA*



![2FA activée](assets/fr/10.webp)



*Potvrzení úspěšné aktivace 2FA v zařízení Bull Bitcoin*



**Záložní kódy**: Bull Bitcoin vám poskytne kódy pro obnovení. **Ulož je na bezpečné místo, odděleně od autentizátoru.



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Možnost nouzových záložních kódů generate na Bull Bitcoin*



![Codes de récupération](assets/fr/12.webp)



*Seznam kódů pro obnovení, které si můžete uložit na bezpečné místo*



### Organizace a řízení



Ente Auth nabízí několik praktických funkcí:



**Rychlá kopie**: Stisknutím kódu se kód automaticky zkopíruje do schránky.



**Akce citlivé na kontext**: Stisknutím a podržením (nebo kliknutím pravým tlačítkem myši na ploše) můžete položku upravit, odstranit, sdílet nebo připnout.



**Tagy a vyhledávání**: Pro rychlé filtrování použijte vyhledávací panel.



![Création d'un tag](assets/fr/17.webp)



*Proces vytváření značek: kontextová nabídka a dialogové okno pro vytváření*



![Tag appliqué](assets/fr/18.webp)



*Značka "Bitcoin" byla úspěšně použita na účtu Bull Bitcoin*



**Automatické ikony**: Díky integraci balíčku ikon [Simple Icons] (https://simpleicons.org/) může být každá položka ilustrována logem služby.



**Dočasné bezpečné sdílení**: Bezpečné sdílení, jedinečná funkce Ente Auth, umožňuje předat kód 2FA kolegovi, aniž by bylo odhaleno základní tajemství. generate šifrovaný odkaz platný maximálně 2, 5 nebo 10 minut - příjemce kód vidí v reálném čase, ale nemůže jej exportovat ani přistupovat k datům účtu. Tato metoda je ideální pro technickou pomoc nebo dočasnou spolupráci a nabízí úroveň zabezpečení, kterou nelze dosáhnout pouhým snímkem obrazovky nebo textovou zprávou.



![Partage sécurisé](assets/fr/19.webp)



*Interface dočasné bezpečné sdílení: zvolte dobu trvání (5 min)*



**Zabezpečený export/import**: Ente Auth umožňuje exportovat kódy do jiných aplikací nebo je importovat z Google Authenticator a dalších řešení. Export probíhá prostřednictvím zašifrovaného souboru nebo QR kódu, což zaručuje přenositelnost vašich dat bez ohrožení bezpečnosti.



**Klíč pro obnovení BIP39**: Aplikace automaticky generuje 24slovnou frázi pro obnovení podle standardu BIP39 (Bitcoin Improvement Proposal), která je shodná s peněženkami pro kryptoměny. Tato fráze je vaším konečným obnovovacím klíčem, který vám umožní obnovit všechny vaše kódy, i když zapomenete hlavní heslo.



## Konfigurace a nastavení



Ente Auth nabízí řadu možností přizpůsobení, které jsou dostupné v nastavení aplikace:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Přehled parametrů dostupných v nástroji Ente Auth*



### Správa účtů a dat



![Paramètres de sécurité](assets/fr/14.webp)



*Rozšířené možnosti zabezpečení: ověření e-mailu, kód PIN, aktivní relace*



Nastavení zabezpečení umožňuje :




- Povolení ověřování e-mailu pro nová připojení
- Aktivace klíče Passkey
- Zobrazení aktivních relací na různých zařízeních
- Nastavení kódu PIN nebo biometrických údajů



### Interface a možnosti použití



![Paramètres généraux](assets/fr/15.webp)



*Parametry Interface a přizpůsobení aplikace*



Obecná nastavení zahrnují :




- Jazyk**: Interface vícejazyčný
- Displej**: Velké ikony, kompaktní režim
- Soukromí**: Skrýt kódy, rychlé vyhledávání
- Telemetrie**: Hlášení chyb (lze vypnout)



## Zálohování a synchronizace



### Jak funguje šifrování



Když přidáte účet s připojeným účtem Ente, aplikace tato citlivá data okamžitě lokálně zašifruje pomocí hlavního klíče (odvozeného z vašeho hesla). Zašifrovaná data jsou poté odeslána na server Ente k uložení.



Díky tomuto mechanismu je vždy k dispozici end-to-end šifrovaná cloudová záloha vašich kódů. Pokud zařízení ztratíte, jednoduše znovu nainstalujte aplikaci Ente Auth a znovu se připojte: aplikace automaticky stáhne a dešifruje všechny vaše kódy.



### Synchronizace více zařízení



Pokud používáte službu Ente Auth v chytrém telefonu i v počítači, jakékoli doplnění nebo změny na jednom zařízení se během několika sekund objeví i na druhém. Tato synchronizace probíhá prostřednictvím cloudu Ente, ale protože jsou data šifrována end-to-end, server vidí pouze nečitelný šifrovaný obsah.



![Synchronisation mobile](assets/fr/16.webp)



*Ukázka synchronizace: stejný účet Bull Bitcoin dostupný na mobilním telefonu i počítači*



Synchronizace je bezproblémová: nainstalujte si Ente Auth do chytrého telefonu, přihlaste se pomocí přihlašovacích údajů a všechny vaše kódy 2FA (zde Bull Bitcoin) se zobrazí automaticky. Výše uvedený příklad ukazuje dokonalou synchronizaci mezi počítačem a mobilním telefonem - stejný kód Bull Bitcoin je dostupný na obou zařízeních.



Pokud jde o důvěrnost, společnost Ente ani žádná třetí strana nemá přístup k vašim tajemstvím 2FA. Dokonce i metadata (značky, poznámky, názvy služeb) jsou před odesláním zašifrována. Tato architektura s nulovou znalostí zajišťuje, že vaše kódy můžete rozluštit pouze vy.



### Použití offline



Synchronizace vyžaduje připojení k internetu, ale služba Ente Auth funguje dokonale offline na každém zařízení, protože všechna data jsou uložena lokálně. Offline změny jsou zařazeny do fronty a synchronizovány, jakmile je připojení obnoveno.



## Bezpečnost a ochrana soukromí



### Kryptografické záruky



Služba Ente Auth je založena na robustním end-to-end šifrování s architekturou nulové znalosti. Vaše kódy jsou šifrovány klíčem, který máte pouze vy a který je odvozen z vašeho hlavního hesla pomocí pokročilých funkcí pro odvozování klíčů.



**Nulová znalostní architektura: Ente nemá fyzický přístup k vašim datům. Dokonce i metadata (názvy služeb, značky, poznámky) jsou před přenosem šifrována na straně klienta. Tento přístup zajišťuje, že v případě útoku na vaše servery nebo žádosti vlády může Ente zveřejnit pouze zašifrovaná data, která nelze přečíst bez vašeho hesla.



**Místní šifrování**: Šifrování probíhá výhradně ve vašem zařízení před odesláním do cloudu. Servery společnosti Ente přijímají a ukládají pouze zašifrovaná data, což znemožňuje neoprávněný přístup i správcům služby.



### Transparentnost a audity



Vzhledem k tomu, že kód je [open source](https://github.com/ente-io/auth), může komunita ověřit, zda neobsahuje zadní vrátka. Ente si nechal provést [několik externích auditů](https://ente.io/blog/cryptography-audit/), aby ověřil bezpečnost své implementace:





- Cure53** (Německo): Audit aplikací a kryptografické bezpečnosti
- Symbolic Software** (Francie): Specializované kryptografické znalosti
- Fallible** (Indie): Penetrační testování a analýza zranitelností



Tyto nezávislé audity prováděné uznávanými firmami zaručují, že kryptografická implementace společnosti Ente Auth je v souladu s osvědčenými bezpečnostními postupy a nemá žádné kritické nedostatky.



### Zásady ochrany osobních údajů



Společnost Ente Auth uplatňuje [vzorové zásady ochrany osobních údajů](https://ente.io/privacy/) založené na minimálním shromažďování údajů. Uchovávány jsou pouze informace nezbytně nutné pro provoz služby: váš e-mail Address pro ověření a obnovení účtu.



**Žádné sledování ani telemetrie**: Na rozdíl od většiny aplikací Ente Auth neshromažďuje žádné metriky používání, žádné identifikační údaje o haváriích ani žádné informace o chování. Aplikace funguje bez rušivé reklamy nebo analytických sledovacích zařízení.



**Soulad s GDPR**: Ente plně dodržuje evropské obecné nařízení o ochraně osobních údajů. Máte právo kdykoli získat přístup ke svým údajům, opravit je nebo vymazat. Export dat](https://ente.io/take-control/) je vzdálen pouhé kliknutí a trvalé vymazání vašeho účtu odstraní všechna vaše data ze serverů.



**Decentralizované, zabezpečené úložiště**: Vaše šifrovaná data jsou replikována u 3 různých poskytovatelů ve 3 různých zemích, což zaručuje optimální dostupnost a zároveň zabraňuje závislosti na jediném poskytovateli cloudu.



Obchodní model společnosti Ente je založen na placené službě Ente Photos, což nám umožňuje nabízet službu Ente Auth **zdarma a bez omezení**, aniž by bylo ohroženo vaše soukromí zpeněžením vašich údajů. Tento přístup zaručuje udržitelnost služby, aniž by se spoléhala na reklamu nebo další prodej osobních údajů.



## Srovnání s jinými řešeními



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth vyniká jako jedno z mála řešení, které kombinuje všechny výhody: transparentnost zdrojového kódu, šifrované cloudové zálohování a synchronizaci napříč platformami.



## Doporučené případy použití



### Individuální uživatelé



Služba Ente Auth je ideální pro osoby, které dbají na bezpečnost a systematicky aktivují 2FA. Už se nebudete muset obávat ztráty kódů při změně telefonu nebo volby mezi pohodlím a bezpečností.



### Používání v rodině a na více zařízeních



Aplikace se hodí, pokud používáte více zařízení. Kódy můžete ukládat do chytrých telefonů a tabletů nebo synchronně a bezpečně sdílet určité rodinné kódy (Netflix, rodinný cloud).



### Profesionální použití



Týmům spravujícím citlivé účty usnadňuje Ente Auth spolupráci a zároveň zachovává bezpečnost díky pokročilým funkcím sdílení integrovaným do části "Organizace a správa".



## Osvědčené postupy





- Uložte si nouzové kódy**: Kódy pro obnovení poskytované jednotlivými službami uchovávejte mimo svůj telefon.





- Používejte silné hlavní heslo**: Hlavní heslo Ente Auth musí být jedinečné a silné, protože chrání všechny vaše kódy.





- Aktivace místní ochrany**: Nastavte PIN nebo biometrické údaje, abyste zabránili neoprávněnému fyzickému přístupu.





- Nepřizpůsobujte se příliš**: Vyhněte se pokročilým úpravám, které by mohly ohrozit synchronizaci.





- Udržujte aplikaci aktuální**: Aktualizace opravují bezpečnostní chyby a zlepšují funkčnost.





- Obnovení testu**: Příležitostně zkontrolujte, zda můžete kódy obnovit na jiném zařízení.



## Závěr



Ente Auth představuje moderní komplexní řešení dvoufaktorového ověřování. Tato open source aplikace kombinuje bezpečnost, transparentnost a snadné používání a splňuje tak potřeby náročných uživatelů, aniž by se vzdala pohodlí.



Na rozdíl od proprietárních řešení, která vás uzavírají do nepřehledného ekosystému, vám Ente Auth vrací kontrolu nad vašimi autentizačními daty a zároveň vás díky šifrovaným zálohám chrání před náhodnou ztrátou.



Ať už jste jednotlivec, který chce zabezpečit své osobní účty, nebo tým spravující firemní přístupy, Ente Auth je chytrá volba pro modernizaci přístupu k digitálnímu zabezpečení bez ohrožení soukromí.



## Zdroje a podpora



### Oficiální dokumentace




- Oficiální webové stránky**: [ente.io/auth](https://ente.io/auth)
- Centrum nápovědy**: [help.ente.io/auth](https://help.ente.io/auth)
- Technický blog**: [ente.io/blog](https://ente.io/blog)



### Zdrojový kód a transparentnost




- GitHub**: [github.com/ente-io/auth](https://github.com/ente-io/auth)
- Kryptografický audit**: [ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)



### Společenství




- Discord**: [discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- Reddit**: [r/enteio](https://reddit.com/r/enteio)