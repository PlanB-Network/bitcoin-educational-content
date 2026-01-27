---
name: LineageOS
description: Gratis, okonstlat Android-operativsystem för smartphones
---

![cover](assets/cover.webp)



Konventionella Android-system som är förinstallerade på våra smartphones innebär ett antal välkända problem: intensiv integration av Google-tjänster som leder till ständig dataspårning, oönskade sponsrade applikationer (bloatware) som införs av tillverkarna och övergivande av uppdateringsspårning efter några år, vilket dömer fortfarande fungerande enheter till programmerad föråldring.



LineageOS presenterar sig som ett elegant svar på dessa problem. LineageOS är en produkt av open source-communityn och en direkt efterföljare till CyanogenMod (som lades ner i slutet av 2016), och är ett gratis Android-baserat mobilt operativsystem som ger användarna tillbaka kontrollen över sina smartphones. Projektet lanserades officiellt i december 2016 och har nu över 4,4 miljoner aktiva installationer över hela världen och stödjer hundratals telefonmodeller från över 20 olika märken.



![lineageos-homepage](assets/fr/01.webp)



*Officiell LineageOS-webbplats som presenterar projektet och dess mål*



## Vad är LineageOS?



### Filosofi och mål



LineageOS är ett mobilt operativsystem med öppen källkod baserat på Android Open Source Project (AOSP), utvecklat av ett stort antal frivilliga bidragsgivare över hela världen. Dess inofficiella motto skulle kunna vara "Din enhet, dina regler": projektet syftar till att förlänga livslängden för smartphones samtidigt som det erbjuder en strömlinjeformad, integritetsvänlig Android-upplevelse.



Projektet uppstod ur askan av CyanogenMod, en av de mest populära alternativa Android ROM:arna i historien. När CyanogenMod Inc. stängde sina dörrar i december 2016 mobiliserades samhället för att skapa LineageOS, med bibehållen innovationsanda och öppen källkodsfilosofi som kännetecknade sin föregångare.



Till skillnad från OEM Android-distributioner förinstallerar LineageOS inte några Google-applikationer som standard och eliminerar helt bloatware. Användarna börjar med ett minimalistiskt system som endast innehåller viktiga applikationer (telefon, meddelanden, kamera, webbläsare) och kan fritt välja vad de vill lägga till senare.



### Påverkan och samhälle



Officiell statistik avslöjar projektets omfattning: med över 4,4 miljoner aktiva installationer i 224 länder är LineageOS ett av de Android-alternativ som har störst spridning i världen. Brasilien ligger i topp med över 2 miljoner användare, följt av Kina och USA, vilket visar på den universella dragningskraften hos en gratis, anpassningsbar Android.




## Huvudsakliga egenskaper



### Interface och användarupplevelse



**Ren Android**: LineageOS erbjuder en autentisk Android-upplevelse som ligger nära AOSP, utan överlägg från tillverkare eller överflödiga applikationer. Interface förblir bekant för Android-användare samtidigt som den erbjuder optimal flyt tack vare avsaknaden av bloatware.



**Google-fri som standard**: Inga Google-tjänster är förinstallerade, av juridiska och etiska skäl. Detta "Google-fria" tillvägagångssätt garanterar total kontroll över dina personuppgifter och förbättrar prestandan genom att undvika tjänster som körs i bakgrunden.



### Anpassning och säkerhet



**Avancerad anpassning**: LineageOS låser upp många alternativ som inte är tillgängliga på Android: omkonfiguration av navigeringsknappar, anpassningsbara systemteman, användningsprofiler anpassade till olika sammanhang (arbete, privat, spel).



**Outil Trust**: Integrerad funktionalitet som övervakar enhetens säkerhetsstatus och varnar dig för potentiella hot, vilket ger realtidsöversikt över systemets säkerhet.



**Förlängda uppdateringar**: LineageOS-communityn har åtagit sig att tillhandahålla månatliga säkerhetsuppdateringar, vilket gör att enheter som avvecklats av sina tillverkare kan fortsätta att få de senaste Android-säkerhetsuppdateringarna.



## Kompatibla enheter



LineageOS stöder hundratals enheter från över 20 tillverkare: Samsung, Xiaomi, OnePlus, Motorola, Sony, Google Pixel, Fairphone och många andra. Denna breda kompatibilitet är en av projektets stora fördelar jämfört med alternativ som GrapheneOS, som är begränsade till Pixel-enheter.



![devices-compatibility](assets/fr/02.webp)



*Sidan med LineageOS-kompatibla enheter med filter efter tillverkare*



![google-devices](assets/fr/03.webp)



*Google-enheter stöds, inklusive Pixel 4 (kodnamn "flame")*



### Populära enheter



Enligt officiell statistik omfattar de mest använda modellerna en mängd olika enheter som täcker olika pris- och åldersintervall, vilket visar LineageOS förmåga att blåsa nytt liv i äldre smartphones samt optimera nyare.



### Viktiga punkter före installationen



**Opplåsbar startladdare**: Kontrollera att din tillverkare/operatör tillåter upplåsning. Vissa märken, t.ex. Huawei, har tagit bort denna möjlighet på de senaste modellerna, medan andra kräver särskilda förfaranden.



**Exakt modell**: Det är viktigt att ladda ner den ROM som exakt motsvarar din enhet. Två modeller med liknande handelsnamn kan skilja sig åt tekniskt (Galaxy S10 vs S10 5G till exempel) och kräver olika bilder.



**Skalbart stöd**: Nyare enheter kanske inte stöds omedelbart, eftersom portering kräver att en frivillig utvecklare tar hand om dem. Omvänt kan stödet upphöra om den som underhåller en enhet drar sig ur projektet.



## Installation



### Viktiga förutsättningar



⚠️ **Läs igenom denna bruksanvisning helt och hållet innan du börjar** för att undvika problem!



**Återgå till standardprogramvaran (om nödvändigt) :**




- Android Flash-verktyg**: Använd det officiella Google-verktyget [flash.android.com](https://flash.android.com) för att enkelt återställa din Pixel-enhet till standard-Android från din webbläsare (Chrome/Edge krävs)
- Alternativ**: Fabriksbilder manuellt från [developers.google.com/android/images](https://developers.google.com/android/images)



**Obligatoriska förkunskapstest: **




- Starta din enhet minst en gång** med det ursprungliga lagersystemet
- Testa alla funktioner**: SMS, samtal, Wi-Fi, mobildata
- Viktigt**: Kontrollera att du kan skicka/ta emot SMS och ringa/ta emot samtal (inklusive via WiFi och 4G/5G). Om det inte fungerar på standardsystemet kommer det inte att fungera på LineageOS heller!
- Nyare enheter**: Vissa kräver att VoLTE/VoWiFi används minst en gång på standardsystemet för att IMS ska kunna tillhandahållas



**Systemförberedelser:**




- Ta bort alla Google**-konton från din enhet för att undvika fabriksåterställningsskydd, som kan blockera aktivering
- Fullständig säkerhetskopiering** : Processen kommer att radera din telefon helt och hållet. Säkerhetskopiera foton, kontakter, applikationer och viktiga filer



**ADB- och Fastboot-verktyg:** Följ den [officiella LineageOS-guiden](https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot) för att installera Android SDK Platform Tools. Verifiera installationen med `adb version` och `fastboot --version`.



**Telefonkonfiguration:**




- Aktivera **Utvecklaralternativ**: Inställningar > Om > tryck på "Byggnummer" 7 gånger



![android-version](assets/fr/06.webp)



*Navigera till Inställningar > Om telefonen för att aktivera utvecklarläget*





- Aktivera **USB-felsökning** i utvecklaralternativ
- Aktivera **OEM Unlock** (nödvändigt för att låsa upp bootloader)



![developer-options](assets/fr/07.webp)



*Aktivera utvecklaralternativ, USB-felsökning och OEM-upplåsning*



### Detaljerad installation



⚠️ **Dessa instruktioner är specifika för LineageOS 22.2. Följ varje steg exakt. Gå inte vidare om något misslyckas!



#### Steg 1: Kontroll av inbyggd programvara



**Firmware krävs**: Din enhet måste ha Android 13 installerat innan du fortsätter (för Pixel 4). Firmware avser de enhetsspecifika bilder som ingår i standardsystemet.



![pixel4-info](assets/fr/04.webp)



*Officiell Pixel 4-sida med nedladdningslänkar och installationsguider*



![downloads-page](assets/fr/05.webp)



*LineageOS build nedladdningssida och filer*



**Pixel 4-specifika nedladdningar: **




- Bygga LineageOS**: [download.lineageos.org/devices/flame/builds](https://download.lineageos.org/devices/flame/builds)
- Obligatoriska filer**: Ladda ner de 3 nödvändiga filerna från den här sidan (de kommer att användas i följande steg):
  - `lineage-22.2-YYYYMMDD-nightly-flame-signed.zip` (huvud-ROM)
  - dtbo.img` (partition enhet träd blob)
  - `boot.img` (återställning LineageOS)



⚠️ **Viktigt**: Kontrollera Android-versionen, inte tillverkarens OS-version. Att använda en anpassad ROM (även LineageOS) garanterar inte att detta krav är uppfyllt.



💡 ** Tips **: Om du är osäker på din firmware, återgå till lagersystemet innan du fortsätter!



#### Steg 2: Låsa upp bootloader



⚠️ **I detta steg raderas alla dina data!





- Testa ADB-anslutningen**: Anslut din enhet via USB och testa med kommandot `adb devices` från din datorterminal



![adb-devices](assets/fr/08.webp)



*Kontrollera ADB-anslutningen med kommandot `adb devices`*





- Godkänn anslutning** på din telefon



![usb-debugging-auth](assets/fr/09.webp)



*USB-felsökning aktiverad med datorns RSA-fingeravtryck*





- Starta i bootloader-läge** :


```
adb -d reboot bootloader
```


Eller håll **Volym ned + Power** enheten avstängd





- Kontrollera anslutningen till fastboot**:


```
fastboot devices
```



![fastboot-mode](assets/fr/10.webp)



*Fastboot-kommandon i terminalen för att kontrollera anslutningen*



![bootloader-screen](assets/fr/11.webp)



*Pixel 4:s snabbstartsdisplay med systeminformation*





- Lås upp bootloader** :


```
fastboot flashing unlock
```


På enheten, använd volymknapparna för att navigera och tryck på **Power**-knappen för att välja "Lås upp bootloader" och bekräfta åtgärden



![unlock-bootloader](assets/fr/12.webp)



*Bekräftelse på upplåsning av bootloader på enheten*



⚠️ **Telefonen startar om automatiskt** efter bekräftelse av upplåsning





- Efter automatisk omstart**, återaktivera USB-felsökning i utvecklaralternativen




#### Steg 3: Flasha ytterligare partitioner



⚠️ **Krävs för att återställningen ska fungera korrekt**





- Starta om bootloader**: Volym ned + ström
- Flash** (ersätt `/path/to/` med den mapp där du hämtade filen) :


```
fastboot flash dtbo /chemin/vers/dtbo.img
```



![flash-partitions](assets/fr/13.webp)



*Flash av dtbo- och boot.img-partitioner via fastboot*



#### Steg 4: Installera LineageOS-återställning





- Flash recovery** (ersätt `/path/to/` med den mapp där du hämtade filen) :


```
fastboot flash boot /chemin/vers/boot.img
```




- Starta om i återställning** för att kontrollera



#### Steg 5: Installera LineageOS





- Starta om i återställningsläge**: Volym ned + Power → Återställningsläge



![recovery-mode](assets/fr/14.webp)



*Interface från LineageOS-återställning med huvudmeny *





- Fabriksåterställning** : Skriv "Fabriksåterställning" → "Formatera data / fabriksåterställning"



![factory-reset](assets/fr/15.webp)



*Process för fabriksåterställning i LineageOS*-återställning





- Återgå till huvudmenyn**
- Sideload LineageOS** :
   - På enheten: "Tillämpa uppdatering" → "Tillämpa från ADB"
   - På datorn: `adb -d sideload /path/to/lineageos.zip`



![apply-update](assets/fr/16.webp)



*Välj "Apply Update" och sedan "Apply from ADB" i återställningen*



![sideload-process](assets/fr/17.webp)



*LineageOS-installation pågår via sidoladdning*



![sideload-terminal](assets/fr/18.webp)



*Sideload-kommando i terminal med installationsförlopp*



💡 **Normal **: Processen kan stanna vid 47% eller visa "Success" -fel - det här är normalt!



#### Steg 6: Första uppstarten





- Starta om**: "Starta om systemet nu"
- Första uppstarten**: Kan ta upp till 15 minuter



🎉 **Installationen är klar!**



### Uppmärksamhetspunkter



⚠️ **Varning**: LineageOS tillhandahålls "i befintligt skick" utan garanti. Även om vi gör allt vi kan för att se till att allt fungerar, installerar du detta på egen risk!



**Kritiska kontroller:**




- Kompatibilitet med fast programvara**: Kontrollera vilken version av den inbyggda programvaran som krävs på nedladdningssidan för din modell
- Lås aldrig bootloader** igen efter installation av LineageOS
- Följ de specifika anvisningarna** för din enhet



## Konfiguration och tillämpningar



### Första uppstarten


Strömlinjeformad Interface, nära lager Android, utan Google. Enkel konfiguration: språk, Wi-Fi, inget konto krävs.



### Alternativa tillämpningar



**Säkra applikationskällor:**



**F-Droid** : Den främsta programbutiken med öppen källkod, förinstallerad med LineageOS för microG eller direkt nedladdningsbar. F-Droid erbjuder endast programvara med öppen källkod som har verifierats och sammanställts transparent, vilket garanterar frånvaron av spårare eller skadliga komponenter.



**Aurora Store**: Anonym klient för åtkomst till Google Play Store utan ett Google-konto. Aurora lånar delade anonyma konton, så att du kan ladda ner vanliga appar samtidigt som du bevarar din integritet.



**Viktiga alternativa tillämpningar:**





- Navigering**: Organic Maps (offline-kartor baserade på OpenStreetMap)
- Kommunikation**: Signal (krypterade meddelanden från början till slut), K-9 Mail (gratis e-postklient)
- Media**: NewPipe (reklamfritt, spårningsfritt YouTube), VLC (universell mediaspelare)
- Produktivitet**: Nextcloud (självhostande moln), Simple Calendar (CalDAV-synkronisering)
- Säkerhet**: Bitwarden (lösenordshanterare), Aegis Authenticator (2FA-koder)



Dessa applikationer, varav de flesta finns tillgängliga via F-Droid, bildar ett sammanhängande ekosystem som helt kan ersätta Googles tjänster och samtidigt erbjuda en modern och funktionell användarupplevelse.



## Användning och underhåll



### Daglig erfarenhet



LineageOS förändrar Android-upplevelsen och prioriterar fluiditet och responsivitet. Den strömlinjeformade Interface är särskilt effektiv på äldre enheter, som får ett nytt liv, med prestanda som i allmänhet är överlägsen tillverkarens ROM tack vare frånvaron av tunga överlägg och överflödiga processer.



Grundläggande funktioner (samtal, SMS, foton, surfning) fungerar sömlöst, medan anpassningsverktyg gör det möjligt att finjustera systemet efter individuella preferenser utan att kompromissa med stabiliteten.



### OTA-uppdateringssystem



LineageOS har ett särskilt lättanvänt Over-The-Air-uppdateringssystem. Nya versioner föreslås automatiskt via meddelanden, och installationen tar bara några klick, utan behov av komplexa tekniska ingrepp. Processen bevarar helt och hållet dina installerade data och applikationer.



Dessa regelbundna uppdateringar är en stor tillgång, särskilt för enheter som har utgått från tillverkarna, som kan fortsätta att dra nytta av de senaste Android-säkerhetsuppdateringarna.



### Rekommenderade bästa metoder



**Säkerhet efter installation:**




- Ange en stark PIN-kod eller ett lösenord för upplåsning
- Kontrollera att lagringskryptering är aktiverad (vanligtvis som standard)
- Installera en lösenordshanterare som Bitwarden via F-Droid



**Förebyggande underhåll:**




- Regelbundna OTA-uppdateringar för säkerhet
- Begränsa installationen av applikationer till betrodda källor (F-Droid, Aurora Store)
- Granska regelbundet de behörigheter som beviljats för applikationer
- Tillfälliga omstarter optimerar prestanda och frigör minne



## Fördelar och begränsningar



✅ **Förmåner:**




- Standardintegritet (ingen Google-spårning)
- Bred kompatibilitet (över 300 modeller)
- Överlägsen prestanda (utan bloatware)
- Utökade uppdateringar på äldre enheter



❌ **Begränsningar:**




- Teknisk installation
- Ingen Android Auto/Google Pay
- Bankappar kan vara problematiska



## GrapheneOS vs LineageOS: Vad är skillnaden?



### Olika tillvägagångssätt



**GrapheneOS** fokuserar uteslutande på maximal säkerhet och körs endast på Google Pixels för att utnyttja deras dedikerade säkerhetschip. Systemet innehåller många avancerade åtgärder mot exploateringar och stärker avsevärt sandboxningen av applikationer.



**LineageOS** balanserar säkerhet, integritet och bekvämlighet på så många enheter som möjligt. Tillvägagångssättet är mer pragmatiskt och siktar på utökad kompatibilitet snarare än absolut säkerhet.



### Hantera Google-tjänster



**GrapheneOS**: Erbjuder ett sandboxat Google Play-system som tillval. Google Play kan installeras men körs i en strikt sandlåda, utan några särskilda systemrättigheter. Detta unika tillvägagångssätt gör det möjligt att använda Googles ekosystem och samtidigt upprätthålla en strikt säkerhetskontroll.



**LineageOS**: Låter användaren välja att installera Google-tjänster (GApps), microG (gratis alternativ) eller vara helt Google-fri. Maximal flexibilitet för att passa dina behov.



### Teknisk jämförelse



| **Aspect** | **GrapheneOS** | **LineageOS** |
|------------|----------------|---------------|
| **Compatibilité** | Pixels uniquement | Centaines d'appareils |
| **Sécurité** | Mitigations avancées | Sécurité AOSP standard |
| **Google Play** | Sandboxé optionnel | Installation classique possible |
| **Installation** | Interface web + USB | Procédure manuelle technique |
| **Philosophie** | Sécurité avant tout | Équilibre et liberté de choix |

### Rekommendationer för användning



**Välj GrapheneOS** om du äger en Pixel, om maximal säkerhet är din högsta prioritet och om du accepterar begränsningar för förbättrat skydd.



**Välj LineageOS** om du har en icke-Pixel-enhet, letar efter en bra balans mellan integritet och praktik eller vill ha friheten att välja din kompromissnivå med Googles ekosystem.



## Slutsats



LineageOS erbjuder ett moget alternativ för att återfå kontrollen över din Android-smartphone. Oförglömlig upplevelse, optimal prestanda, omfattande kompatibilitet: det perfekta valet för att kombinera integritet och praktisk vardag.



## Resurser



### Officiell dokumentation




- [LineageOS officiella webbplats](https://lineageos.org)
- [LineageOS Wiki](https://wiki.lineageos.org) - Installationsguider efter modell
- [LineageOS för microG](https://lineage.microg.org) - Version med integrerad microG



### Gemenskap




- [Subreddit r/LineageOS](https://reddit.com/r/LineageOS)
- [Mastodon-konto @LineageOS](https://fosstodon.org/@LineageOS)



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1