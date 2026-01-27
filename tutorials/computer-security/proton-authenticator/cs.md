---
name: Proton Authenticator
description: Jak mohu použít Proton Authenticator k zabezpečení svých účtů pomocí 2FA?
---
![cover](assets/cover.webp)



Dvoufaktorové ověřování (2FA) přidává k vašim účtům další bezpečnostní bariéru tím, že kromě hesla vyžaduje další důkaz, že ho máte pouze vy. Zapnutí 2FA výrazně snižuje riziko hackerského útoku, a to i v případě, že je vaše heslo prozrazeno phishingem nebo únikem dat. Bez 2FA by útočník potřeboval k přístupu k vašim účtům pouze vaše heslo; s 2FA by potřeboval i váš druhý faktor, což by zmařilo většinu pokusů o krádež účtu.



Existují různé typy 2FA. SMS kódy jsou lepší než nic, ale zůstávají zranitelné vůči útokům na výměnu SIM karet a odposlechu. SMS jako primární 2FA nedoporučujeme. Autentizační aplikace (TOTP) generate dočasné kódy lokálně v zařízení, takže je mnohem obtížnější je zachytit. Fyzické bezpečnostní klíče nabízejí nejlepší zabezpečení, ale vyžadují vyhrazený hardware.



Proton Authenticator je autentizátor TOTP. Je to reakce společnosti Proton na omezení stávajících aplikací: mnohé z nich jsou proprietární, obsahují sledovače reklam a nenabízejí šifrované zálohování. Proton Authenticator se odlišuje tím, že poskytuje aplikaci s otevřeným zdrojovým kódem, bez reklam a sledovacích zařízení, s end-to-end šifrovaným zálohováním.



## Představujeme Proton Authenticator



Proton Authenticator je mobilní a desktopová autentizační aplikace TOTP vyvinutá společností Proton, která je známá svými službami zaměřenými na ochranu soukromí. Stejně jako všechny ostatní produkty společnosti Proton je i tato aplikace open source a prošla nezávislými bezpečnostními audity. Je k dispozici zdarma na všech platformách (Android, iOS, Windows, macOS, Linux).



Proton Authenticator nabízí následující klíčové funkce:





- Generování kódů **TOTP** pro vaše účty 2FA, kompatibilní s většinou webů používajících Google Authenticator, Authy atd.





- **Volitelné šifrované cloudové zálohování**: aplikaci můžete propojit se svým účtem Proton a zálohovat a synchronizovat své kódy s end-to-end šifrováním. Pokud ztratíte své zařízení, jednoduše znovu připojte nové a obnovte všechny své kódy.





- **Synchronizace s více zařízeními**: po přihlášení do Protonu v aplikaci se vaše kódy 2FA automaticky synchronizují mezi více zařízeními prostřednictvím šifrování end-to-end. V systému iOS je alternativou synchronizace přes iCloud.





- **Místní zamykání pomocí hesla nebo biometrie**: aplikace nabízí zamykání pomocí kódu PIN a/nebo otisku prstu/identifikace obličeje. Takže i když se někdo fyzicky dostane do vašeho odemčeného telefonu, nebude moci otevřít aplikaci Proton Authenticator.





- **Žádný sběr dat ani sledování**: Proton se zavazuje, že prostřednictvím aplikace nebude shromažďovat žádné osobní údaje. Neexistuje žádná skrytá reklama ani analýza chování.





- **Snadný import/export**: jednou ze silných stránek aplikace Proton Authenticator je průvodce importem stávajících účtů, který je kompatibilní s jinými aplikacemi (Google Authenticator, Authy, Aegis atd.). V případě potřeby můžete své kódy také exportovat do souboru.



Proton Authenticator je zkrátka nekompromisní řešení 2FA: bezpečné, soukromé a flexibilní.



## Instalace



Proton Authenticator je k dispozici zdarma na všech platformách. Chcete-li si aplikaci stáhnout, přejděte na oficiální stránku: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Oficiální stránka aplikace Proton Authenticator zobrazující hlavní funkce aplikace a Interface*



Na této stránce najdete odkazy ke stažení pro všechny operační systémy: Android, iOS, Windows, macOS a Linux. Jednoduše klikněte na vybraný operační systém a postupujte podle standardních instalačních kroků.



V tomto návodu si ukážeme, jak ji nainstalovat a nakonfigurovat v systému macOS, a poté se podíváme, jak aplikaci nainstalovat v systému iOS a synchronizovat kódy mezi oběma zařízeními.



### Instalace v systému macOS



Po stažení a instalaci aplikace spusťte aplikaci Proton Authenticator. Při prvním spuštění vás aplikace provede několika úvodními konfiguračními obrazovkami:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Uvítací obrazovka Proton Authenticator se zprávou "Bezpečnost v každém kódu" a tlačítkem "Začít "*



### Počáteční dovoz



Pokud Proton Authenticator zjistí, že jste dříve používali jinou aplikaci 2FA, může se zobrazit průvodce importem. Podporuje přímý import z některých aplikací (Google Authenticator, 2FAS, Authy, Aegis atd.). Případně můžete tento krok přeskočit a přidat účty ručně později.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*Průvodce importem pro přenos kódů z jiných ověřovacích aplikací*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*Kompatibilní importní aplikace: 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth a Google Authenticator*



### Ochrana místní aplikace



Nastavte kód PIN pro odemknutí nebo povolte biometrické odemykání (Touch ID), pokud je k dispozici. Tento krok je zásadní, aby nikdo, kdo používá váš Mac, nezískal volný přístup k vašim kódům 2FA.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*Konfigurační obrazovka Touch ID se zprávou "Chraňte svá data" a tlačítkem "Aktivovat Touch ID "*



### Možnosti synchronizace



Aplikace také umožňuje aktivovat synchronizaci iCloud a bezpečně zálohovat data mezi zařízeními Apple.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*Možnost synchronizace přes ICloud se zprávou "Zálohujte svá data bezpečně pomocí šifrované synchronizace přes iCloud "*



Po dokončení těchto kroků je Proton Authenticator připraven k použití.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface hlavní prázdný Proton Authenticator s možnostmi "Vytvořit nový kód" a "Importovat kódy "*



## Přidání účtu 2FA pomocí služby ProtonMail



Nyní se podíváme na to, jak přidat první kód 2FA na příkladu služby ProtonMail. Tento způsob funguje stejně u všech služeb, které podporují dvoufaktorové ověřování.



### Povolení 2FA na ProtonMailu



Nejprve si můžete přečíst našeho průvodce službou ProtonMail, kde najdete další informace:



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Přihlaste se ke svému účtu ProtonMail a přejděte do nastavení zabezpečení. Vyhledejte možnost "Dvoufaktorové ověřování" a aktivujte ji.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*Stránka nastavení ProtonMailu s možností "Authenticator app" v sekci "Dvoufaktorové ověřování "*



Kliknutím na tlačítko aktivujete autentizátor a ProtonMail vás vyzve k výběru autentizační aplikace.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*Konfigurační okno ProtonMail 2FA s tlačítky "Storno" a "Další "*



ProtonMail poté zobrazí QR kód, který můžete naskenovat pomocí autentizační aplikace.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*ProtonMail QR kód pro skenování pomocí autentizační aplikace, s možností "Zadejte klíč ručně" *



Pokud dáváte přednost ručnímu zadání klíče, klikněte na možnost "Zadat klíč ručně" a zobrazí se tajný klíč.



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*Ruční zadání informací 2FA: Klíč, interval (30) a číslice (6)*



### Naskenujte kód QR pomocí nástroje Proton Authenticator



V aplikaci Proton Authenticator v systému macOS klikněte na možnost "Vytvořit nový kód". Aplikace vám nabídne několik možností: **Skenovat QR kód** nebo **Zadat klíč ručně**.



Pomocí fotoaparátu Macu naskenujte QR kód zobrazený na obrazovce ProtonMailu. Po naskenování QR kódu budete přesměrováni na obrazovku konfigurace nového kódu.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*Okno pro vytvoření nového záznamu s poli Název (ProtonMail), Tajemství, Odesílatel (Proton), parametry číslic a interval*



Proton Authenticator automaticky vyplní informace. Pokud si přejete, můžete název upravit a poté kliknout na tlačítko "Uložit".



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*Vygenerování TOTP kódu pro ProtonMail (848 812) se zobrazením zbývajícího času*



### Ověření konfigurace



ProtonMail vás požádá o zadání šestimístného kódu vygenerovaného nástrojem Proton Authenticator, abyste potvrdili, že 2FA funguje správně.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*Ověřovací obrazovka ProtonMailu s žádostí o zadání šestimístného kódu (848812)*



Zkopírujte kód z aplikace (kliknutím na něj) a vložte jej do aplikace ProtonMail, čímž aktivaci dokončíte.



Po ověření vás ProtonMail požádá o stažení kódů pro obnovení. Je nezbytné je pečlivě uložit.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*Obrazovka kódů pro obnovení ProtonMail se seznamem záchranných kódů a tlačítkem "Stáhnout "*



### Nouzové kódy



Při přidávání účtu dodržujte kódy pro obnovení poskytnuté službou. Většina webů nabízí statické kódy pro obnovení na jedno použití, které můžete uložit na bezpečném místě. Tyto záložní kódy uchovávejte mimo aplikaci Proton Authenticator, abyste měli přístup k účtu, pokud ztratíte přístup k aplikaci 2FA.



## Instalace systému IOS a import kódu



Když už jste si Proton Authenticator nastavili v systému macOS, můžete ho používat také v iPhonu nebo iPadu. Zde najdete návod, jak získat kódy 2FA na více zařízeních.



### Stažení aplikace v systému iOS



Přejděte do obchodu App Store a vyhledejte položku "Proton Authenticator". Stáhněte a nainstalujte aplikaci do svého zařízení se systémem iOS.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*Instalační proces v systému iOS: uvítací obrazovka, průvodce importem, výběr kompatibilních aplikací a závěrečná obrazovka "Importovat kódy z Proton Authenticator "*



### Metoda 1: Export/import prostřednictvím souboru JSON



Pokud nepoužíváte automatickou synchronizaci (iCloud nebo účet Proton), musíte kódy z Macu do iPhonu přenést ručně:



**Krok 1 - Export ze systému macOS** :



V počítači Mac otevřete aplikaci Proton Authenticator a přejděte do Nastavení (ikona ozubeného kola). V nabídce klikněte na položku "Export".



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*Nabídka nastavení aplikace Proton Authenticator v systému macOS s viditelnou možností "Exportovat "*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*Okno exportu s názvem souboru "Proton_Authenticator_backup_2025" a tlačítkem "Uložit "*



Uložte soubor JSON do počítače Mac. Můžete ho poslat zabezpečeným e-mailem nebo uložit na iCloud Drive, abyste k němu měli přístup z iPhonu.



**Krok 2 - Import v systému iOS** :



V iPhonu si nainstalujte aplikaci Proton Authenticator a během konfigurace zvolte import kódů. Ze seznamu vyberte "Proton Authenticator" a importujte soubor JSON.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*Proces importu v systému iOS: Lokalizace souboru JSON, potvrzení importu a konfigurační obrazovky s možnostmi Face ID a iCloud*



### Metoda 2: Automatická synchronizace



**Přes účet Proton (pro synchronizaci více platforem)** :



Pokud jste si ještě nenastavili účet Proton a chcete synchronizovat mezi různými operačními systémy, aplikace vás vyzve k vytvoření nebo připojení účtu Proton.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*Obrazovka synchronizace zařízení s výzvou k vytvoření bezplatného účtu Proton nebo k připojení k existujícímu účtu*



**Přes iCloud (pouze pro ekosystém Apple)** :


Pokud používáte pouze zařízení Apple, můžete v nastavení aplikace zvolit synchronizaci přes iCloud. Tato metoda automaticky a bezpečně synchronizuje vaše kódy mezi všemi vašimi zařízeními Apple, aniž byste potřebovali účet Proton.



## Šifrované zálohování a obnovení



Jednou z klíčových funkcí Proton Authenticator je end-to-end zálohování kódů 2FA, které zajišťuje, že při ztrátě nebo změně zařízení nemusíte začínat znovu.



### Koncové šifrování



Pokud jde o šifrované cloudové zálohování pomocí služby Proton Authenticator, vaše tajemství TOTP jsou před odesláním na server Proton šifrována lokálně ve vašem zařízení. Dešifrování můžete provést pouze vy na svých zařízeních připojených k účtu Proton. Společnost Proton AG nemá klíč k přečtení vašich registrovaných kódů.



Pokud se v systému iOS rozhodnete pro iCloud, a ne pro účet Proton, budou vaše data šifrována podle standardů společnosti Apple. Místní zálohování v systému Android umožňuje zašifrovat záložní soubor heslem, které si sami zvolíte.



### Obnova v případě ztráty



Pokud telefon ztratíte, odcizíte nebo vyměníte sluchátko :



**S povoleným zálohováním Protonu**: Nainstalujte Proton Authenticator do nového zařízení. Během počátečního nastavení se přihlaste ke stejnému účtu Proton. Aplikace okamžitě synchronizuje a stáhne všechny vaše kódy 2FA ze zašifrované zálohy.



**S iCloud zálohou (iOS)**: Připojte nový iPhone/iPad pomocí stejného Apple ID a nezapomeňte aktivovat iCloud Keychain. Po instalaci aplikace Proton Authenticator se připojte ke službě iCloud. Vaše kódy by se měly synchronizovat přes iCloud a zobrazit se.



**Žádné zálohování do cloudu**: Účty musíte importovat ručně. Pokud jste exportovali záložní soubor, použijte funkci Import v aplikaci Proton Authenticator. V nejhorším případě, pokud jste neměli žádnou zálohu, budete muset použít záložní kódy pro jednotlivé služby nebo kontaktovat podporu.



Proton Authenticator umožňuje kdykoli exportovat účty buď jako šifrovaný soubor, nebo jako QR kód pro více účtů. Tyto možnosti vám poskytnou větší jistotu.



## Osvědčené postupy



Používání autentizátoru 2FA výrazně zvyšuje bezpečnost, je však třeba dodržovat určité osvědčené postupy:



### Uložení nouzových kódů



Při aktivaci služby 2FA se často zobrazí seznam kódů pro obnovení. Mějte je mimo telefon (na papíře, v zašifrovaném správci hesel apod.). V případě úplné ztráty ověřovacího zařízení vás tyto statické kódy zachrání.



### Nemíchejte hesla a kódy 2FA



Je lákavé používat správce hesel, který ukládá i TOTP. Uchovávání hesla a kódu 2FA na stejném místě však vytváří jediný bod selhání a oslabuje duální ověřování. Pro maximální zabezpečení mnoho odborníků doporučuje oba faktory oddělit: hesla v bezpečném správci a kódy 2FA v samostatné aplikaci, jako je například Proton Authenticator. Použití integrovaného správce je však stále lepší než nemít 2FA vůbec.



### Aktivace několika metod 2FA



V ideálním případě používejte na kritických účtech více než jeden druhý faktor. Pokud to služba umožňuje, neváhejte přidat fyzický bezpečnostní klíč. Více informací naleznete v našem návodu o fyzických klíčích Yubikey:



https://planb.academy/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Stejně tak mějte po ruce vytištěné nouzové kódy.



### Zůstaňte diskrétní a chraňte své zařízení



Nenechte nikoho prohledávat odemčený telefon. S nástrojem Proton Authenticator jsou vaše kódy chráněny kódem PIN/biometrickými údaji - tento kód PIN neprozrazujte. Stejně tak si dejte pozor na phishing: i když máte 2FA, pokud kód zadáte podvodné stránce v reálném čase, může ho použít útočník.



### Aktualizace a audity



Udržujte Proton Authenticator aktuální (aktualizace opravují případné chyby). Protože je kód otevřený, komunita provádí neformální audity a společnost Proton zveřejňuje výsledky formálních auditů.



## Srovnání s jinými aplikacemi



Jak si Proton Authenticator stojí v porovnání s ostatními autentizačními aplikacemi? Zde je srovnávací přehled:



**Protonový autentifikátor**: Synchronizace s více zařízeními, lokální zamykání, žádné sledování, k dispozici na mobilu i počítači.



**Autentikátor Google**: V roce 2023 byla přidána synchronizace více zařízení, ve výchozím nastavení není zámek aplikací, obsahuje sledovací zařízení Google: proprietární, zálohování přes účet Google od roku 2023, ale bez koncového šifrování (klíče jsou viditelné pro Google).



**Aegis Authenticator**: Pouze pro Android, pouze lokální zálohování, bez synchronizace s cloudem, kódový/biometrický zámek, bez sledování.



**Authy**: Synchronizace více zařízení, zámek PIN/otisk prstu, sbírá telefonní číslo, desktopová aplikace ukončena v březnu 2024.



Níže najdete našeho průvodce službou Authy:



https://planb.academy/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator je jedno z nejkomplexnějších a nejbezpečnějších řešení: open source, šifrovaná synchronizace pro více zařízení, žádné komerční návaznosti.



## Zdroje a podpora



### Oficiální dokumentace




- **Oficiální webové stránky**: [proton.me/authenticator](https://proton.me/authenticator) - Prezentace produktu a soubory ke stažení
- **Stránka ke stažení**: [proton.me/en/authenticator/download](https://proton.me/fr/authenticator/download) - Odkazy pro všechny operační systémy
- **Podpora protonů**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Oficiální průvodce aktivací 2FA
- **Proton blog**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Oznámení a podrobné funkce



### Zdrojový kód a transparentnost




- **GitHub Proton Authenticator**: [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Otevřený zdrojový kód
- **Bezpečnostní audity**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Nezávislé auditní zprávy



### Doporučené bezpečnostní testy


Po konfiguraci otestujte nastavení:




- [Have I Been Pwned](https://haveibeenpwned.com/) - Zkontrolujte, zda vaše účty byly napadeny
- [Adresář 2FA](https://2fa.directory/) - seznam služeb podporujících 2FA



### Společenství a diskuse




- Reddit r/Proton: [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Oficiální komunita Protonu
- **Fórum průvodců ochranou osobních údajů**: [discuss.privacyguides.net](https://discuss.privacyguides.net) - Technické diskuse o otázkách ochrany soukromí
- **Reddit r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Obecné tipy k ochraně soukromí



### Další




- [Have I Been Pwned](https://haveibeenpwned.com/) - Zkontrolujte, zda vaše účty byly napadeny
- [Adresář 2FA](https://2fa.directory/) - seznam služeb podporujících 2FA