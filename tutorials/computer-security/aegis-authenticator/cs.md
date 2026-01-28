---
name: Aegis Authenticator
description: Jak můžete pomocí nástroje Aegis Authenticator zabezpečit své účty pomocí duálního ověřování?
---

![cover](assets/cover.webp)



Dvoufaktorové ověřování (2FA) je dnes pro zabezpečení online účtů nezbytné. Kromě hesla přidává druhý faktor (často šestimístný kód), jehož platnost vyprší po 30 sekundách, což hackerům značně ztěžuje práci. Používání speciální aplikace TOTP (*Time-based One-Time Password*) je bezpečnější než SMS, které mohou být zneužity útoky typu SIM swapping.



Ne všechny aplikace pro ověřování jsou však stejné. Mnohá proprietární řešení (Google Authenticator, Authy atd.) přinášejí problémy: jsou proprietární a uzavřené (není možné kontrolovat jejich zabezpečení), někdy integrují reklamní trackery, nenabízejí šifrované zálohování vašich kódů a mohou dokonce bránit exportu vašich účtů a uzamknout vás v jejich ekosystému.



Aegis Authenticator se naproti tomu prezentuje jako bezplatná a etická alternativa k těmto aplikacím. Aegis je bezplatná, bezpečná aplikace s otevřeným zdrojovým kódem pro správu dvoufázových ověřovacích tokenů v systému Android. Její vývoj se zaměřuje na základní funkce, které jiné aplikace nenabízejí, včetně robustního šifrování místních dat a možnosti bezpečného zálohování. Celkově Aegis nabízí lokální, kontrolovatelné řešení dvojího ověřování, které je ideální pro všechny, kdo si chtějí zachovat úplnou kontrolu nad svými kódy 2FA.



## Představujeme Aegis Authenticator



Aegis Authenticator je aplikace 2FA s otevřeným zdrojovým kódem pro Android, vydaná pod licencí GPL v3. Vyznačuje se filozofií "privacy by design": aplikace funguje zcela offline a nevyžaduje připojení ke vzdálené službě. Vaše tokeny tak zůstávají uloženy lokálně ve vašem zařízení v bezpečném sejfu, od kterého máte klíč pouze vy.



### Klíčové vlastnosti



**Šifrovaný trezor:** všechny vaše kódy OTP jsou uloženy v šifrovaném trezoru AES-256 (režim GCM), chráněném hlavním heslem definovaným uživatelem. Pro větší pohodlí můžete tento trezor odemknout pomocí hesla nebo biometrických údajů (otisk prstu, rozpoznání obličeje). V případě absence hesla by data byla nezašifrovaná - proto důrazně doporučujeme, abyste si jej nastavili.



**Pokročilá organizace:** Systém Aegis udržuje vaše četné účty 2FA přehledně uspořádané. Záznamy můžete seřadit podle abecedy nebo podle vlastního výběru, seskupit je podle kategorií (např. osobní, pracovní, sociální) pro snadné vyhledávání a každému záznamu přiřadit osobní ikonu. Součástí je vyhledávací panel pro okamžité vyhledání služby nebo účtu podle názvu.



**Šifrované místní zálohy:** Abyste nikdy neztratili přístup ke svým účtům, nabízí Aegis automatické zálohování vašeho sejfu. Ty jsou šifrované (pomocí hesla) a lze je ukládat na vámi zvolené místo (interní úložiště, cloudová složka atd.). Aplikace může také ručně exportovat databázi účtů, a to podle potřeby v šifrovaném nebo nešifrovaném formátu. Import účtů z jiných aplikací 2FA je stejně snadný (Aegis podporuje import z Authy, Google Authenticator, FreeOTP aOTP atd.).



**Bezpečnost a soukromí:** aplikace je ve výchozím nastavení zcela offline. Nevyžaduje žádná síťová oprávnění - což znamená, že nepřenáší žádná data do vnějšího světa a neobsahuje žádné moduly pro sledování reklam ani analýzu chování. Aegis nezobrazuje reklamy a nevyžaduje uživatelský účet: jakmile je nainstalován, je spuštěn bez registrace. Jelikož je jeho zdrojový kód veřejný na GitHubu, komunita jej může volně kontrolovat, což zaručuje absenci škodlivých nebo skrytých funkcí.



**Moderní Interface:** Aegis používá elegantní Material Design s podporou tmavých motivů (včetně režimu AMOLED) a dokonce i volitelného zobrazení dlaždic, které zobrazuje kódy jako mřížky. Interface je nenáročný, bez zbytečností a v rámci bezpečnostních opatření zabraňuje snímání kódů z obrazovky.



## Instalace



Protože je Aegis Authenticator open source, jeho vývojáři upřednostňují distribuční kanály šetrné k soukromí. Existují dva hlavní způsoby instalace:



### Přes F-Droid (doporučeno)



Nejbezpečnější a nejjednodušší způsob je prostřednictvím bezplatného alternativního obchodu F-Droid. Pokud F-Droid ještě nemáte v telefonu nainstalovaný, začněte stažením z oficiálních webových stránek [F-Droid.org](https://f-droid.org). Poté :





- Otevřete aplikaci F-Droid a zkontrolujte, zda jste aktualizovali úložiště, abyste získali nejnovější seznam aplikací
- V aplikaci F-Droid vyhledejte položku "Aegis Authenticator". Měla by se objevit oficiální aplikace (vydavatel: Beem Development)
- Instalaci zahájíte stisknutím tlačítka Instalovat. Protože je Aegis jednou z aplikací ověřených společností F-Droid, můžete využít spolehlivého a bezpečného stahování



Výhodou instalace přes F-Droid je možnost přijímat automatické aktualizace aplikací ihned po jejich vydání. F-Droid navíc zaručuje, že aplikace neobsahuje nežádoucí proprietární komponenty.



### Přes GitHub (podepsaný APK)



Pokud dáváte přednost instalaci aplikace bez použití obchodu, můžete si stáhnout oficiální APK přímo ze stránky projektu GitHub. V úložišti Aegis ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)) přejděte do sekce Releases, kde jsou zveřejněny stabilní verze.





- Stáhnout nejnovější verzi APK
- Před instalací APK se ujistěte, že jste v zařízení povolili instalaci aplikací z neznámých zdrojů (v nastavení systému Android)
- APK poskytnutý na GitHubu je podepsán vývojářem se stejným klíčem jako na F-Droidu



Po ruční instalaci bude aplikace fungovat stejně. Upozorňujeme, že aktualizace nebudou automatické: budete muset pravidelně kontrolovat GitHub, zda se neobjeví nová verze.



### Obchod Google Play vs F-Droid



Aplikace Aegis Authenticator je k dispozici v obchodě Google Play i F-Droid, takže si můžete vybrat způsob instalace:



**Obchod Google Play:**




- ✅ Automatické aktualizace integrované do systému Android
- ✅ Jednoduchá a známá instalace
- ✅ Stejné podepsané APK jako na jiných kanálech



**F-Droid (doporučeno) :**




- ✅ Bezplatný obchod s otevřeným zdrojovým kódem
- ✅ Reprodukovatelná a ověřitelná konstrukce
- ✅ Služba Google není vyžadována
- ✅ Respekt k filozofii svobodného softwaru



Volba mezi těmito dvěma možnostmi závisí na vašich preferencích týkajících se ekosystému Google. Pokud dáváte přednost jednoduchosti, je ideální Obchod Play. Pokud chcete mít více soukromí a být nezávislí na službách Google, je lepší volbou F-Droid.



## První konfigurace



Při prvním spuštění systému Aegis je navržen úvodní postup konfigurace, který zajistí bezpečný kód 2FA:



![Configuration initiale Aegis](assets/fr/01.webp)



*Počáteční proces konfigurace systému Aegis: uvítací obrazovka, volba zabezpečení, definice hlavního hesla a finalizace*



### Nastavení hlavního hesla



Systém Aegis vás nejprve požádá o výběr hlavního hesla. Toto heslo bude použito k zašifrování všech vašich ověřovacích tokenů uložených v trezoru. Důrazně doporučujeme nastavit silné a jedinečné heslo, které budete znát pouze vy.



**⚠️ Upozornění:** nezapomeňte toto heslo - pokud ho ztratíte, vaše šifrované kódy 2FA se stanou nedostupnými (neexistují žádná zadní vrátka). Systém Aegis vás požádá o dvojí zadání hesla pro potvrzení.



### Povolení biometrického odemykání (volitelné)



Pokud je vaše zařízení se systémem Android vybaveno čtečkou otisků prstů nebo jiným biometrickým snímačem, systém Aegis vás vyzve k aktivaci biometrického odemykání. Tato možnost je volitelná, ale velmi praktická: umožňuje rychlé odemknutí aplikace pomocí otisku prstu nebo obličeje, místo abyste pokaždé zadávali heslo.



Všimněte si, že biometrické údaje představují další pohodlí: hlavní heslo je vyžadováno i v případě změny biometrických údajů nebo restartování zařízení.



### Zjištění nastavení aplikace



Jakmile se dostanete do aplikace (hlavní okno Interface je zpočátku prázdné), seznamte se s dostupnými možnostmi konfigurace. Přístup k nastavení získáte prostřednictvím rozbalovací nabídky v pravém horním rohu obrazovky (tři svislé tečky) a poté vyberte možnost "Settings" (Nastavení).



![Interface principale et paramètres](assets/fr/02.webp)



*Interface hlavní Aegis prázdný při spuštění, přístup do nabídky parametrů a přehled dostupných možností*



Nabídka nastavení systému Aegis sdružuje několik důležitých částí:





- **Vzhled**: Přizpůsobte si motiv (světlý, tmavý, AMOLED), jazyk a další vizuální nastavení
- **Chování**: Konfigurace chování aplikace při interakci se seznamem položek
- **Balíčky ikon**: správa a import balíčků ikon pro přizpůsobení vzhledu účtů
- **Bezpečnost**: Nastavení šifrování, biometrického odemykání, automatického zamykání a dalších bezpečnostních parametrů
- **Zálohování**: Konfigurace automatického zálohování do vybraného umístění
- **Import a export**: Import záloh z jiných ověřovacích aplikací a ruční export trezoru Aegis
- **Protokol auditu**: Podrobný protokol všech významných událostí v aplikaci



Tato přehledná organizace vám umožní nakonfigurovat systém Aegis podle vašich preferencí a potřeb zabezpečení.



## Přidání účtu 2FA



Po konfiguraci systému Aegis přejděme k tomu nejdůležitějšímu: přidání dvoufaktorových účtů. Tento proces je jednoduchý a systém Aegis nabízí několik metod integrace ověřovacích kódů.



### Tři dostupné metody sčítání



V hlavním okně aplikace Aegis Interface stiskněte tlačítko **+** vpravo dole, čímž se dostanete k možnostem přidání. K dispozici máte tři možnosti:





- **Naskenujte kód QR**: Naskenujte přímo kód QR zobrazený webovou službou
- **Skenování obrázku**: Naskenujte QR kód z obrázku uloženého v zařízení
- **Zadejte ručně**: Zadejte informace o účtu 2FA ručně



### Praktický příklad: konfigurace systému Bitwarden



Pro ilustraci si uveďme konkrétní příklad aktivace 2FA v systému Bitwarden:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Příklad aktivace 2FA v systému Bitwarden: Web Interface s možnostmi ověřování a doporučením Aegis*





- **Přihlášení a přístup k nastavení**: Přihlaste se ke svému účtu Bitwarden a přejděte do nastavení na záložku "Zabezpečení"
- **Sekce poskytovatelů**: Přejděte do sekce "Providers" a klikněte na "Manage" v sekci "Authenticator app"



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Dokončení procesu přidání účtu: QR kód zobrazený službou, viditelný tajný klíč a zadaný ověřovací kód*





- **Naskenujte QR kód**: Otevře se vyskakovací okno s QR kódem a tajným klíčem
- V systému **Aegis**: Použijte "Skenování QR kódu" k automatickému zachycení informací
- **Ověřování**: Do pole "Ověřovací kód" zadejte šestimístný kód vygenerovaný společností Aegis
- **Aktivace**: Kliknutím na "Zapnout" dokončíte aktivaci



### Ruční přidání podrobností



Pokud chcete nebo nemůžete naskenovat kód QR, použijte možnost "Zadat ručně". Formulář umožňuje zadat :



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Postup přidání nového účtu 2FA: prázdný účet Interface, přidání možností, formulář pro ruční zadání a úspěšně přidaný účet*





- **Jméno**: Název služby (např. Bitwarden, GitHub...)
- **Emitent**: Emitent (často totožný s názvem)
- **Skupina**: Nepovinné, pro uspořádání účtů podle kategorií
- **Poznámka**: Osobní poznámky k tomuto účtu
- **Tajemství**: Tajný klíč poskytnutý službou (ve výchozím nastavení maskovaný)
- **Pokročilý**: Pokročilé parametry (algoritmus, perioda, počet číslic)



Po přidání účtu se účet zobrazí v seznamu s aktuálním kódem a ukazatelem času, který zbývá do obnovení.



### Univerzální kompatibilita



Systém Aegis je kompatibilní se všemi službami používajícími standardy TOTP a HOTP, včetně prakticky všech stránek nabízejících 2FA: sociální sítě, banky, správci hesel, kryptografické platformy atd.



### Organizace vstupu



Jakmile si přidáte několik účtů, oceníte organizační nástroje systému Aegis:





- **Vlastní řazení:** Ve výchozím nastavení se účty zobrazují v abecedním pořadí, ale pořadí můžete změnit ručně
- **Skupiny a kategorie:** Vytvářejte skupiny, abyste oddělili osobní účty od firemních, nebo je seskupte podle typu služby (bankovnictví, e-mail, sociální sítě atd.)
- **Vlastní ikony:** Aegis se snaží automaticky přiřadit vhodnou ikonu, pokud je k dispozici, jinak si můžete vybrat z mnoha obecných ikon nebo importovat obrázek
- **Rychlé vyhledávání:** Vyhledávací panel v horní části umožňuje zadat několik písmen a okamžitě vyfiltrovat odpovídající položky



Dotykem na položku se OTP kód zobrazí v plné velikosti (pokud byl skrytý) a dlouhým stisknutím jej můžete zkopírovat do schránky - to se hodí pro vložení do aplikace, ke které se chcete připojit.



## Zabezpečení a zálohování



Vzhledem k tomu, že základem systému Aegis je bezpečnost, je důležité pochopit, jak jsou vaše kódy 2FA chráněny a jak zajistit jejich trvalost v případě problému.



### Bezpečnostní architektura



**Robustní šifrování**: Všechny vaše kódy jsou uloženy v šifrovaném trezoru pomocí algoritmu **AES-256 v režimu GCM** v kombinaci s vaším hlavním heslem. Odvozování klíčů je založeno na technologii **scrypt**, která nabízí zvýšenou ochranu proti útokům hrubou silou.



**Zabezpečené odemykání** : K dešifrování dat je nutné hlavní heslo. Biometrické údaje (volitelné) používají k ochraně šifrovacího klíče **Android Secure Keystore** a TEE (Trusted Execution Environment).



**Minimální oprávnění**: Aegis ve výchozím nastavení funguje offline a vyžaduje pouze přístup ke kameře (QR sken), biometrii a vibrátoru. Žádná data nejsou shromažďována ani sdílena.



### Možnosti zálohování



Společnost Aegis nabízí několik strategií zálohování, které vyhovují různým potřebám zabezpečení a pohodlí:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface s přidaným účtem, upozorněním na zálohování, nastavením automatického zálohování a strategiemi zálohování*



**1. Automatické místní zálohování**




- Konfigurace cílové složky podle vlastního výběru
- Přizpůsobitelná frekvence (po každé změně, denně atd.)
- Šifrované soubory chráněné heslem (.aesvault)
- Kompatibilita se synchronizovanými složkami (Nextcloud, Dropbox atd.)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Proces výběru záložní složky: průzkumník souborů, cílová složka a oprávnění k přístupu*



**2. Cloudové zálohování pro Android**




- Volitelná integrace se zálohovacím systémem Android
- K dispozici pouze pro zašifrované trezory (zabezpečení zachováno)
- Transparentní zálohování s ostatními daty systému Android
- Automatické obnovení při výměně zařízení



**3. Ruční** export




- Export na vyžádání prostřednictvím **Nastavení > Import a export**
- Volba šifrovaného (doporučeno) nebo čistého formátu
- Užitečné pro migraci nebo příležitostné zálohování



### Správné bezpečnostní postupy





- Uchovávejte několik záložních verzí, abyste zabránili poškození
- Pravidelně testujte **své zálohy** pokusem o obnovení
- Kódy pro obnovení poskytnuté službou uchovávejte odděleně
- **Hlavní heslo** je vyžadováno i při zálohování do cloudu
- **Zabezpečení hlavního hesla**: používejte jedinečné a silné heslo uložené ve správci hesel
- Udržujte svou aplikaci **aktuální** s nejnovějšími bezpečnostními záplatami
- **Aktivace automatického zámku** v nastavení pro zabezpečení přístupu k aplikaci
- **Zakázat snímky obrazovky** (výchozí možnost), abyste zabránili zachycení vašich kódů
- **Biometrické údaje používejte střídmě**: pro kritické přístupy preferujte hesla



## Srovnání s jinými aplikacemi



Jak si Aegis stojí v porovnání s jinými populárními ověřovacími aplikacemi?



### Aegis vs. Google Authenticator



**Aegis :**




- ✅ Otevřený zdrojový kód a možnost auditu
- ✅ Místní šifrované zálohování
- ✅ Pokročilá organizace (skupiny, ikony, vyhledávání)
- ✅ Žádný sběr dat
- ❌ Pouze Android



**Autentikátor Google :**




- ✅ K dispozici pro Android a iOS
- ✅ Cloudová synchronizace (od roku 2023)
- ❌ Uzavřený zdrojový kód
- ❌ Omezená funkčnost
- ❌ Potenciální sběr dat Google



### Aegis vs. Authy



**Aegis :**




- ✅ Otevřený zdroj
- ✅ Není vyžadován účet
- ✅ Možnost exportu kódu
- ✅ Celková kontrola dat
- ❌ Žádná nativní synchronizace více zařízení



**Authy :**




- ✅ Synchronizace více zařízení
- ✅ K dispozici pro Android a iOS
- ❌ Uzavřený zdrojový kód
- ❌ Vyžaduje telefonní číslo
- ❌ Nelze exportovat kódy
- ❌ Aplikace pro stolní počítače odstraněny v březnu 2024



Aegis je vynikající pro uživatele systému Android, kteří si cení transparentnosti, místního zabezpečení a úplné kontroly nad svými daty. Alternativy jako Authy jsou vhodnější, pokud nezbytně potřebujete automatickou synchronizaci více zařízení.




## Závěr



Aegis Authenticator je vynikajícím řešením pro ty, kteří hledají bezpečnou a transparentní aplikaci 2FA šetrnou k soukromí. Jeho přístup založený na otevřeném zdrojovém kódu v kombinaci s robustním šifrováním a přehledným Interface z něj činí prvotřídní volbu pro zabezpečení vašich online účtů.



Aegis je sice omezen na systém Android a postrádá nativní cloudovou synchronizaci, ale tato omezení více než vynahrazuje svou filozofií "privacy by design" a úplnou kontrolou dat. Uživatelům, kteří se zajímají o své digitální soukromí, nabízí Aegis důvěryhodnou a výkonnou alternativu k dominantním proprietárním řešením na trhu.



Bezpečnost vašich online účtů nemusí záviset na dobré vůli komerčních společností. Se službou Aegis máte kontrolu nad svými ověřovacími kódy v digitálním trezoru, od kterého máte klíč pouze vy.



## Zdroje



### Oficiální webové stránky




- **Oficiální webové stránky**: [getaegis.app](https://getaegis.app/) - Prezentace aplikace a její stažení
- **Zdrojový kód**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Oficiální repozitář GitHubu
- **F-Droid** : [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Instalace přes free store



### Technická dokumentace




- **Dokumentace k trezoru**: [Návrh trezoru](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Technický popis šifrování a bezpečné architektury
- **Oficiální FAQ**: [getaegis.app/#faq](https://getaegis.app/#faq) - Odpovědi na často kladené otázky
- **Projekt wiki**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Úplná uživatelská dokumentace