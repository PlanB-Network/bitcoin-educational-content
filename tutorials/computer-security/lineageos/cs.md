---
name: LineageOS
description: Bezplatný operační systém Android pro chytré telefony bez lepidla
---

![cover](assets/cover.webp)



Konvenční systémy Android předinstalované v našich chytrých telefonech představují řadu známých problémů: intenzivní integrace služeb Google vedoucí k neustálému sledování dat, nežádoucí sponzorované aplikace (bloatware) vnucované výrobci a opuštění sledování aktualizací po několika letech, což odsoudí stále funkční zařízení k programovému zastarání.



LineageOS se prezentuje jako elegantní odpověď na tyto problémy. LineageOS, produkt komunity open source a přímý nástupce CyanogenModu (ukončeného na konci roku 2016), je bezplatný mobilní operační systém založený na Androidu, který uživatelům vrací kontrolu nad jejich smartphony. Projekt byl oficiálně spuštěn v prosinci 2016 a nyní se může pochlubit více než 4,4 milionu aktivních instalací po celém světě a podporuje stovky modelů telefonů více než 20 různých značek.



![lineageos-homepage](assets/fr/01.webp)



*Oficiální webové stránky LineageOS představující projekt a jeho cíle*



## Co je LineageOS?



### Filozofie a cíle



LineageOS je mobilní operační systém s otevřeným zdrojovým kódem založený na projektu Android Open Source Project (AOSP), který vyvíjí rozsáhlá komunita dobrovolných přispěvatelů z celého světa. Jeho neoficiálním mottem by mohlo být "Vaše zařízení, vaše pravidla": cílem projektu je prodloužit životnost chytrých telefonů a zároveň nabídnout zjednodušené prostředí systému Android, které je šetrné k soukromí.



Projekt vznikl z popela CyanogenModu, jedné z nejpopulárnějších alternativních ROM pro Android v historii. Když společnost CyanogenMod Inc. v prosinci 2016 ukončila svou činnost, komunita se zmobilizovala a vytvořila LineageOS, který si zachoval ducha inovací a filozofii open source, jež charakterizovaly jeho předchůdce.



Na rozdíl od OEM distribucí Androidu nemá LineageOS ve výchozím nastavení předinstalované žádné aplikace Google a zcela eliminuje bloatware. Uživatelé začínají s minimalistickým systémem obsahujícím pouze základní aplikace (telefon, zprávy, fotoaparát, prohlížeč) a mohou si svobodně vybrat, co přidají později.



### Dopad a komunita



Oficiální statistiky ukazují rozsah projektu: s více než 4,4 milionu aktivních instalací ve 224 zemích představuje LineageOS jednu z nejrozšířenějších alternativ Androidu na světě. Vede Brazílie s více než 2 miliony uživatelů, následuje Čína a USA, což dokazuje univerzální přitažlivost svobodného a přizpůsobitelného systému Android.




## Hlavní funkce



### Interface a zkušenosti uživatelů



**Čistý Android**: LineageOS nabízí autentické prostředí Androidu blízké AOSP, bez překryvných prvků výrobce a zbytečných aplikací. Interface zůstává uživatelům Androidu známý a zároveň nabízí optimální plynulost díky absenci bloatwaru.



**Ve výchozím nastavení bez služby Google**: Z právních a etických důvodů nejsou předinstalovány žádné služby Google. Tento přístup "bez Googlu" zaručuje úplnou kontrolu nad vašimi osobními údaji a zvyšuje výkon, protože se vyhýbá službám běžícím na pozadí.



### Přizpůsobení a bezpečnost



**Pokročilé přizpůsobení**: LineageOS zpřístupňuje mnoho možností, které nejsou dostupné v základním Androidu: změna konfigurace navigačních tlačítek, přizpůsobitelné motivy systému, profily používání přizpůsobené různým kontextům (práce, osobní, hraní her).



**Outil Trust**: Integrovaná funkce, která monitoruje stav zabezpečení zařízení a upozorňuje na potenciální hrozby, poskytuje přehled o zabezpečení systému v reálném čase.



**Rozšířené aktualizace**: Komunita LineageOS se zavázala poskytovat měsíční bezpečnostní záplaty, což umožňuje, aby zařízení, jejichž výrobu výrobci ukončili, nadále dostávala nejnovější bezpečnostní záplaty systému Android.



## Kompatibilní zařízení



LineageOS podporuje stovky zařízení od více než 20 výrobců: Samsung, Xiaomi, OnePlus, Motorola, Sony, Google Pixel, Fairphone a mnoho dalších. Tato široká kompatibilita je jednou z hlavních výhod projektu oproti alternativám, jako je GrapheneOS, které jsou omezeny na zařízení Pixel.



![devices-compatibility](assets/fr/02.webp)



*Stránka zařízení kompatibilních s LineageOS s filtry podle výrobce*



![google-devices](assets/fr/03.webp)



*Podporovaná zařízení Google včetně Pixelu 4 (kódové označení "flame")*



### Oblíbená zařízení



Podle oficiálních statistik patří mezi nejpoužívanější modely celá řada zařízení různých cenových a věkových kategorií, což dokazuje schopnost systému LineageOS vdechnout nový život starším smartphonům i optimalizovat ty novější.



### Zásadní body před instalací



**Odemykatelný zavaděč**: Zkontrolujte, zda výrobce/operátor umožňuje odemknutí. Některé značky, jako například Huawei, tuto možnost u posledních modelů zrušily, zatímco jiné stanovují zvláštní postupy.



**Přesný model**: Je důležité stáhnout ROM, která přesně odpovídá vašemu zařízení. Dva modely s podobnými obchodními názvy se mohou technicky lišit (například Galaxy S10 vs. S10 5G) a vyžadovat odlišné obrazy.



**Škálovatelná podpora**: Novější zařízení nemusí být podporována okamžitě, protože jejich portování vyžaduje dobrovolného vývojáře, který se o ně postará. Naopak podpora může být ukončena, pokud správce zařízení od projektu odstoupí.



## Instalace



### Základní předpoklady



⚠️ **Před zahájením si kompletně přečtěte tyto pokyny**, abyste předešli případným problémům!



**Obnovení výchozího firmwaru (v případě potřeby) :**




- Nástroj Android Flash Tool**: Pomocí oficiálního nástroje Google [flash.android.com](https://flash.android.com) můžete snadno obnovit zařízení Pixel do výchozího systému Android z webového prohlížeče (vyžaduje se Chrome/Edge)
- Alternativa**: Tovární obrázky ručně z [developers.google.com/android/images](https://developers.google.com/android/images)



**Povinné zkoušky:**




- Spusťte zařízení alespoň jednou** s původním výchozím systémem
- Otestujte všechny funkce**: Zkoušejte SMS, hovory, Wi-Fi, mobilní data
- Důležité**: Zkontrolujte, zda můžete odesílat/přijímat SMS a uskutečňovat/přijímat hovory (včetně hovorů přes WiFi a 4G/5G). Pokud to nefunguje ve stock systému, nebude to fungovat ani v LineageOS!
- Nedávná zařízení**: Některá vyžadují, aby bylo VoLTE/VoWiFi použito alespoň jednou v základním systému pro zajištění IMS



**Příprava systému:**




- Odstranění všech účtů Google** ze zařízení, abyste se vyhnuli ochraně před obnovením továrního nastavení, která může zablokovat aktivaci
- Úplné zálohování** : Tento proces zcela vymaže telefon. Zálohujte fotografie, kontakty, aplikace a důležité soubory



**Nástroje ADB a Fastboot:** Podle [oficiálního průvodce LineageOS](https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot) nainstalujte nástroje platformy Android SDK. Instalaci ověřte pomocí `adb version` a `fastboot --version`.



**Konfigurace telefonu:**




- Aktivujte **možnosti vývojáře**: Nastavení > O aplikaci > 7x klepněte na "Číslo sestavení"



![android-version](assets/fr/06.webp)



*Přejděte do Nastavení > Informace o telefonu a aktivujte režim pro vývojáře*





- Povolení **Ladění USB** v Možnostech pro vývojáře
- Aktivace **OEM Unlock** (nezbytné pro odemknutí zavaděče)



![developer-options](assets/fr/07.webp)



*Povolení možností pro vývojáře, ladění USB a odemykání OEM*



### Podrobná instalace



⚠️ **Tyto pokyny jsou specifické pro LineageOS 22.2. Postupujte přesně podle jednotlivých kroků. Pokud se něco nepodaří, nepokračujte dál!



#### Krok 1: Kontrola firmwaru



**Vyžaduje se firmware**: Před pokračováním musí být v zařízení nainstalován Android 13 (pro Pixel 4). Firmware označuje obrazy specifické pro zařízení, které jsou součástí základního systému.



![pixel4-info](assets/fr/04.webp)



*Oficiální stránka Pixel 4 s odkazy na stažení a průvodci instalací*



![downloads-page](assets/fr/05.webp)



*Stránka pro stažení sestavení systému LineageOS a soubory*



**Specifické soubory ke stažení pro Pixel 4:**




- Sestavte LineageOS**: [download.lineageos.org/devices/flame/builds](https://download.lineageos.org/devices/flame/builds)
- Požadované soubory**: Stáhněte si 3 požadované soubory z této stránky (budou použity v následujících krocích):
  - `lineage-22.2-YYYYMMDD-nightly-flame-signed.zip` (hlavní ROM)
  - dtbo.img` (blob stromu zařízení oddílu)
  - `boot.img` (recovery LineageOS)



⚠️ **Důležité**: Zkontrolujte verzi systému Android, nikoli verzi operačního systému výrobce. Používání vlastní ROM (ani LineageOS) nezaručuje, že je tento požadavek splněn.



💡 **Tip**: Pokud máte pochybnosti o svém firmwaru, vraťte se před pokračováním k výchozímu systému!



#### Krok 2: Odemknutí zavaděče



⚠️ **Tímto krokem odstraníte všechna data!





- Otestujte připojení ADB**: Připojte zařízení přes USB a otestujte ho pomocí příkazu `adb devices` z terminálu počítače



![adb-devices](assets/fr/08.webp)



*Kontrola připojení ADB pomocí příkazu `adb devices`*





- Autorizace připojení** v telefonu



![usb-debugging-auth](assets/fr/09.webp)



*Povolené ladění USB pomocí otisku prstu RSA počítače*





- Zavedení do režimu zavaděče** :


```
adb -d reboot bootloader
```


Nebo podržte tlačítko **Ztlumit hlasitost + Napájení** zařízení vypnuté





- Zkontrolujte připojení fastboot**:


```
fastboot devices
```



![fastboot-mode](assets/fr/10.webp)



*Příkazy Fastboot v terminálu pro kontrolu připojení*



![bootloader-screen](assets/fr/11.webp)



*Displej s informacemi o systému při rychlém spuštění systému Pixel 4*





- Odemknutí zavaděče** :


```
fastboot flashing unlock
```


V zařízení se pohybujte pomocí tlačítek hlasitosti a stisknutím tlačítka **Power** vyberte možnost "Unlock the bootloader" a potvrďte operaci



![unlock-bootloader](assets/fr/12.webp)



*Potvrzení odemčení zavaděče v zařízení*



⚠️ **Po potvrzení odemčení se telefon automaticky restartuje**





- Po automatickém restartu** znovu povolte ladění USB v možnostech pro vývojáře




#### Krok 3: Flashování dalších oddílů



⚠️ **Vyžadováno pro správnou funkci obnovení**





- Restartujte zavaděč**: Snížení hlasitosti + napájení
- Flash** (nahraďte `/path/to/` složkou, do které jste soubor stáhli) :


```
fastboot flash dtbo /chemin/vers/dtbo.img
```



![flash-partitions](assets/fr/13.webp)



*Flashování oddílů dtbo a boot.img pomocí fastboot*



#### Krok 4: Instalace obnovení systému LineageOS





- Flash recovery** (nahraďte `/path/to/` složkou, do které jste soubor stáhli) :


```
fastboot flash boot /chemin/vers/boot.img
```




- Restartujte obnovení** a zkontrolujte



#### Krok 5: Instalace systému LineageOS





- Restart v režimu obnovení**: Režim obnovení: Snížení hlasitosti + napájení → Režim obnovení



![recovery-mode](assets/fr/14.webp)



*Interface z obnovení systému LineageOS s hlavní nabídkou*





- Obnovení továrního nastavení** : Zadejte "Obnovení továrního nastavení" → "Formátovat data / obnovení továrního nastavení"



![factory-reset](assets/fr/15.webp)



*Proces obnovení továrního nastavení v obnovení systému LineageOS*





- Návrat do hlavní nabídky**
- Sideload LineageOS** :
   - V zařízení: "Použít aktualizaci" → "Použít z ADB"
   - Na PC: `adb -d sideload /path/to/lineageos.zip`



![apply-update](assets/fr/16.webp)



*V programu zotavení vyberte možnost "Použít aktualizaci" a poté "Použít z ADB "*



![sideload-process](assets/fr/17.webp)



*Probíhá instalace systému LineageOS pomocí sideload*



![sideload-terminal](assets/fr/18.webp)



*Příkaz Sideload v terminálu s průběhem instalace*



💡 **Normální**: Proces se může zastavit na 47 % nebo zobrazit chybu "Úspěch" - to je normální!



#### Krok 6: První spuštění





- Restart**: "Restartovat systém"
- První bota**: Může trvat až 15 minut



🎉 **Instalace dokončena!**



### Body pozornosti



⚠️ **Upozornění**: LineageOS je poskytován "tak jak je" bez záruky. Přestože se snažíme zajistit, aby vše fungovalo, instalujete jej na vlastní nebezpečí!



**Kritické kontroly:**




- Kompatibilita firmwaru**: Ujistěte se, že požadovaná verze firmwaru je uvedena na stránce ke stažení vašeho modelu
- Po instalaci systému LineageOS nikdy znovu nezamykejte** zavaděč
- Postupujte podle konkrétních pokynů** pro své zařízení



## Konfigurace a aplikace



### První spuštění


Zjednodušený systém Interface, který se blíží systému Android, bez společnosti Google. Jednoduchá konfigurace: jazyk, Wi-Fi, není nutný účet.



### Alternativní aplikace



**Zabezpečení zdrojů aplikací:**



**F-Droid** : Referenční obchod s aplikacemi s otevřeným zdrojovým kódem, předinstalovaný v systému LineageOS pro microG nebo ke stažení přímo. F-Droid nabízí pouze software s otevřeným zdrojovým kódem, který byl ověřen a zkompilován transparentně, což zaručuje absenci sledovacích programů nebo škodlivých komponent.



**Aurora Store**: Anonymní klient pro přístup do obchodu Google Play bez účtu Google. Aurora si půjčuje sdílené anonymní účty, což vám umožní stahovat běžné aplikace při zachování vašeho soukromí.



**Zásadní alternativní aplikace:**





- Navigace**: (offline mapy založené na OpenStreetMap)
- Komunikace**: Signal (šifrované zprávy end-to-end), K-9 Mail (bezplatný e-mailový klient)
- Média**: (YouTube bez reklam a sledování), VLC (univerzální přehrávač médií)
- Produktivita**: (selfhostingový cloud), Simple Calendar (synchronizace CalDAV)
- Bezpečnost**: Bitwarden (správce hesel), Aegis Authenticator (kódy 2FA)



Tyto aplikace, z nichž většina je k dispozici prostřednictvím služby F-Droid, tvoří ucelený ekosystém, který může plně nahradit služby Google a zároveň nabídnout moderní a funkční uživatelské prostředí.



## Použití a údržba



### Každodenní zkušenost



Systém LineageOS mění prostředí systému Android a upřednostňuje plynulost a rychlost odezvy. Zjednodušená verze Interface je obzvláště účinná na starších zařízeních, kterým vdechuje nový život, přičemž díky absenci těžkých překryvných vrstev a zbytečných procesů je výkon obecně vyšší než u ROM od výrobce.



Základní funkce (volání, SMS, fotografie, prohlížení) fungují bez problémů, zatímco nástroje pro přizpůsobení umožňují systém přesně přizpůsobit individuálním preferencím, aniž by byla ohrožena stabilita.



### Systém aktualizací OTA



Systém LineageOS nabízí mimořádně snadno použitelný systém aktualizací Over-The-Air. Nové verze jsou automaticky navrhovány prostřednictvím oznámení a instalace trvá jen několik kliknutí bez nutnosti složitých technických zásahů. Tento proces plně zachovává nainstalovaná data a aplikace.



Tyto pravidelné aktualizace jsou velkým přínosem zejména pro zařízení, jejichž výroba byla ukončena a která mohou nadále využívat nejnovější bezpečnostní záplaty systému Android.



### Doporučené osvědčené postupy



**Zabezpečení po instalaci:**




- Nastavení silného kódu PIN nebo hesla pro odemknutí
- Zkontrolujte, zda je povoleno šifrování úložiště (obvykle ve výchozím nastavení)
- Instalace správce hesel, jako je Bitwarden, přes F-Droid



**Preventivní údržba:**




- Pravidelné aktualizace OTA pro zabezpečení
- Omezení instalace aplikací na důvěryhodné zdroje (F-Droid, Aurora Store)
- Pravidelná kontrola oprávnění udělených aplikacím
- Občasné restarty optimalizují výkon a uvolňují paměť



## Výhody a omezení



✅ **Výhody:**




- Výchozí ochrana osobních údajů (bez sledování Google)
- Široká kompatibilita (více než 300 modelů)
- Vynikající výkon (žádný bloatware)
- Rozšířené aktualizace na starších zařízeních



❌ **Omezení:**




- Technická instalace
- Žádné Android Auto/Google Pay
- Bankovní aplikace mohou být problematické



## GrapheneOS vs. LineageOS: Jaký je mezi nimi rozdíl?



### Odlišné přístupy



**GrapheneOS** se zaměřuje výhradně na maximální zabezpečení a běží pouze na zařízeních Google Pixel, kde využívá jejich speciální bezpečnostní čipy. Systém obsahuje řadu pokročilých opatření proti zneužití a výrazně posiluje sandboxing aplikací.



**Systém LineageOS** vyvažuje zabezpečení, soukromí a pohodlí na co největším počtu zařízení. Tento přístup je pragmatičtější a usiluje spíše o rozšířenou kompatibilitu než o absolutní bezpečnost.



### Správa služeb Google



**GrapheneOS**: Nabízí volitelný systém Google Play se sandboxem. Google Play lze nainstalovat, ale běží v přísném sandboxu bez zvláštních systémových oprávnění. Tento jedinečný přístup umožňuje používat ekosystém Google při zachování přísné kontroly zabezpečení.



**LineageOS**: (GApps), microG (bezplatná alternativa) nebo zůstat zcela bez Google. Maximální flexibilita podle vašich potřeb.



### Technické srovnání



| **Aspect** | **GrapheneOS** | **LineageOS** |
|------------|----------------|---------------|
| **Compatibilité** | Pixels uniquement | Centaines d'appareils |
| **Sécurité** | Mitigations avancées | Sécurité AOSP standard |
| **Google Play** | Sandboxé optionnel | Installation classique possible |
| **Installation** | Interface web + USB | Procédure manuelle technique |
| **Philosophie** | Sécurité avant tout | Équilibre et liberté de choix |

### Doporučení pro použití



**Vyberte si systém GrapheneOS**, pokud vlastníte zařízení Pixel, pokud je pro vás nejvyšší prioritou maximální zabezpečení a pokud akceptujete omezení pro zvýšenou ochranu.



**Přejděte na LineageOS**, pokud máte jiné zařízení než Pixel, hledáte dobrou rovnováhu mezi soukromím a praktičností nebo si chcete svobodně zvolit úroveň kompromisu s ekosystémem Google.



## Závěr



Systém LineageOS nabízí vyspělou alternativu pro získání kontroly nad smartphonem se systémem Android. Nespoutaný zážitek, optimální výkon, rozsáhlá kompatibilita: ideální volba pro kombinaci soukromí a každodenní praktičnosti.



## Zdroje



### Oficiální dokumentace




- [Oficiální stránky LineageOS](https://lineageos.org)
- [LineageOS Wiki](https://wiki.lineageos.org) - Návody k instalaci podle modelu
- [LineageOS pro microG](https://lineage.microg.org) - Verze s integrovaným microG



### Společenství




- [Subreddit r/LineageOS](https://reddit.com/r/LineageOS)
- [Mastodon účet @LineageOS](https://fosstodon.org/@LineageOS)



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1