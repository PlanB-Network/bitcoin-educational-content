---
name: LineageOS
description: Gratis, losgekoppeld Android-besturingssysteem voor smartphones
---

![cover](assets/cover.webp)



Conventionele Android-systemen die vooraf op onze smartphones zijn geïnstalleerd, brengen een aantal bekende problemen met zich mee: intensieve integratie van Google-services die leidt tot voortdurende datatracking, ongewenste gesponsorde toepassingen (bloatware) die door fabrikanten worden opgelegd en het niet meer volgen van updates na een paar jaar, waardoor nog functionerende apparaten worden veroordeeld tot geprogrammeerde veroudering.



LineageOS presenteert zichzelf als een elegant antwoord op deze problemen. LineageOS is een product van de opensourcegemeenschap en een directe opvolger van CyanogenMod (dat eind 2016 werd stopgezet). Het is een gratis, op Android gebaseerd mobiel besturingssysteem dat gebruikers de controle over hun smartphones teruggeeft. Het project werd officieel gelanceerd in december 2016, heeft nu wereldwijd meer dan 4,4 miljoen actieve installaties en ondersteunt honderden telefoonmodellen van meer dan 20 verschillende merken.



![lineageos-homepage](assets/fr/01.webp)



*Officiële LineageOS-website waarop het project en de doelstellingen worden gepresenteerd*



## Wat is LineageOS?



### Filosofie en doelstellingen



LineageOS is een open source mobiel besturingssysteem gebaseerd op het Android Open Source Project (AOSP), ontwikkeld door een grote gemeenschap van vrijwillige bijdragers wereldwijd. Het onofficiële motto zou "Jouw apparaat, jouw regels" kunnen zijn: het project wil de levensduur van smartphones verlengen en tegelijkertijd een gestroomlijnde, privacy-vriendelijke Android-ervaring bieden.



Het project ontstond uit de as van CyanogenMod, een van de populairste alternatieve Android ROM's in de geschiedenis. Toen CyanogenMod Inc. zijn deuren sloot in december 2016, mobiliseerde de gemeenschap om LineageOS te creëren, met behoud van de geest van innovatie en open-source filosofie die zijn voorganger kenmerkte.



In tegenstelling tot OEM Android-distributies, installeert LineageOS standaard geen Google-toepassingen en wordt bloatware volledig geëlimineerd. Gebruikers beginnen met een minimalistisch systeem met alleen essentiële applicaties (telefoon, berichten, camera, browser) en zijn vrij om te kiezen wat ze later willen toevoegen.



### Impact en gemeenschap



Officiële statistieken onthullen de omvang van het project: met meer dan 4,4 miljoen actieve installaties in 224 landen is LineageOS een van de meest gebruikte Android-alternatieven ter wereld. Brazilië leidt de weg met meer dan 2 miljoen gebruikers, gevolgd door China en de VS, wat de universele aantrekkingskracht van een gratis, aanpasbaar Android aantoont.




## Belangrijkste kenmerken



### Interface en gebruikerservaring



**Puur Android**: LineageOS biedt een authentieke Android-ervaring dicht bij AOSP, zonder overlays van de fabrikant of overbodige applicaties. De Interface blijft vertrouwd voor Android-gebruikers en biedt optimale vloeiendheid dankzij de afwezigheid van bloatware.



*standaard *Google-vrij**: Om juridische en ethische redenen zijn er geen Google-services vooraf geïnstalleerd. Deze "Google-vrije" benadering garandeert volledige controle over je persoonlijke gegevens en verbetert de prestaties door te voorkomen dat services op de achtergrond worden uitgevoerd.



### Aanpassing en veiligheid



**Geavanceerde aanpassingen**: LineageOS ontgrendelt vele opties die niet beschikbaar zijn op standaard Android: navigatieknop herconfiguratie, aanpasbare systeemthema's, gebruiksprofielen aangepast aan verschillende contexten (werk, privé, gaming).



**Outil Trust**: Geïntegreerde functionaliteit die de beveiligingsstatus van je apparaat bewaakt en je waarschuwt voor potentiële bedreigingen, zodat je in realtime inzicht hebt in de beveiliging van je systeem.



**Uitgebreide updates**: De LineageOS-gemeenschap is toegewijd aan het leveren van maandelijkse beveiligingspatches, zodat apparaten die door hun fabrikanten worden stopgezet de nieuwste Android-beveiligingspatches blijven ontvangen.



## Compatibele apparaten



LineageOS ondersteunt honderden toestellen van meer dan 20 fabrikanten: Samsung, Xiaomi, OnePlus, Motorola, Sony, Google Pixel, Fairphone en vele anderen. Deze brede compatibiliteit is een van de grote voordelen van het project ten opzichte van alternatieven zoals GrapheneOS, die beperkt zijn tot Pixel-apparaten.



![devices-compatibility](assets/fr/02.webp)



*Pagina met LineageOS-compatibele apparaten met filters per fabrikant*



![google-devices](assets/fr/03.webp)



*Ondersteunde Google-apparaten, inclusief de Pixel 4 (codenaam "flame")*



### Populaire apparaten



Volgens officiële statistieken omvatten de meest gebruikte modellen een verscheidenheid aan toestellen in verschillende prijs- en leeftijdscategorieën, wat aantoont dat LineageOS in staat is om oudere smartphones nieuw leven in te blazen en nieuwere smartphones te optimaliseren.



### Cruciale punten voor installatie



**Ontsluitbare bootloader**: Controleer of je fabrikant/operator unlocken toestaat. Sommige merken, zoals Huawei, hebben deze mogelijkheid afgeschaft op recente modellen, terwijl andere merken specifieke procedures opleggen.



**Exact model**: Het is cruciaal om de ROM te downloaden die precies overeenkomt met je toestel. Twee modellen met vergelijkbare handelsnamen kunnen technisch verschillen (Galaxy S10 vs S10 5G bijvoorbeeld) en verschillende afbeeldingen vereisen.



**Schaalbare ondersteuning**: Nieuwere apparaten worden mogelijk niet meteen ondersteund, omdat voor het porten een vrijwillige ontwikkelaar nodig is. Omgekeerd kan de ondersteuning stoppen als de beheerder van een apparaat zich terugtrekt uit het project.



## Installatie



### Essentiële voorwaarden



⚠️ **Lees deze instructies helemaal door voordat je begint** om problemen te voorkomen!



**Return to stock firmware (indien nodig) :**




- Android Flash-tool**: Gebruik de officiële tool van Google [flash.android.com](https://flash.android.com) om je Pixel-apparaat eenvoudig te herstellen naar stock-Android vanuit je webbrowser (Chrome/Edge vereist)
- Alternatief**: Fabrieksafbeeldingen handmatig van [developers.google.com/android/images](https://developers.google.com/android/images)



**Verplichte vooropleidingstests:**




- Start het apparaat ten minste één keer** op met het originele standaardsysteem
- Test alle functies**: SMS, gesprekken, Wi-Fi, mobiele data
- Belangrijk**: Controleer of je sms'jes kunt versturen/ontvangen en gesprekken kunt voeren/ontvangen (ook via wifi en 4G/5G). Als het niet werkt op het standaardsysteem, zal het ook niet werken op LineageOS!
- Recente toestellen**: Sommige vereisen dat VoLTE/VoWiFi ten minste één keer wordt gebruikt op het standaardsysteem om IMS te leveren



**Systeemvoorbereiding:**




- Verwijder alle Google**-accounts van je apparaat om te voorkomen dat de fabrieksresetbeveiliging de activering blokkeert
- Volledige back-up** : Het proces wist je telefoon volledig. Maak een back-up van foto's, contacten, applicaties en belangrijke bestanden



**ADB- en Fastboot-tools:** Volg de [officiële LineageOS-gids](https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot) om de Android SDK-platformtools te installeren. Controleer de installatie met `adb version` en `fastboot --version`.



**Telefoonconfiguratie:**




- Activeer **Ontwikkelopties**: Instellingen > Over > tik 7 keer op "Build number"



![android-version](assets/fr/06.webp)



*Ga naar Instellingen > Over telefoon om de ontwikkelaarsmodus te activeren*





- Schakel **USB debugging** in bij Opties voor ontwikkelaars
- Activeer **OEM Unlock** (essentieel voor het ontgrendelen van de bootloader)



![developer-options](assets/fr/07.webp)



*Opties voor ontwikkelaar, USB-foutopsporing en OEM-ontgrendeling inschakelen*



### Gedetailleerde installatie



⚠️ **Deze instructies zijn specifiek voor LineageOS 22.2. Volg elke stap nauwkeurig. Ga niet verder als er iets mislukt!



#### Stap 1: Firmware controleren



**Firmware vereist**: Op je apparaat moet Android 13 geïnstalleerd zijn voordat je verder kunt gaan (voor Pixel 4). Firmware verwijst naar de apparaatspecifieke afbeeldingen in het voorraadsysteem.



![pixel4-info](assets/fr/04.webp)



*Officiële Pixel 4-pagina met downloadlinks en installatiegidsen*



![downloads-page](assets/fr/05.webp)



*LineageOS build downloadpagina en bestanden*



**Pixel 4 specifieke downloads:**




- LineageOS bouwen**: [download.lineageos.org/devices/flame/builds](https://download.lineageos.org/devices/flame/builds)
- Vereiste bestanden**: Download de 3 vereiste bestanden van deze pagina (ze worden in de volgende stappen gebruikt):
  - `lineage-22.2-YYYMMDD-nightly-flame-signed.zip` (hoofd-ROM)
  - dtbo.img` (blob met partitieapparaatstructuur)
  - `boot.img` (herstel LineageOS)



⚠️ **Belangrijk**: Controleer de Android-versie, niet de OS-versie van de fabrikant. Een aangepaste ROM (zelfs LineageOS) is geen garantie dat aan deze eis is voldaan.



**Tip**: Als je twijfelt over je firmware, keer dan terug naar het standaardsysteem voordat je verder gaat!



#### Stap 2: De bootloader ontgrendelen



⚠️ **Deze stap verwijdert al je gegevens!





- Test de ADB-verbinding**: Sluit je apparaat aan via USB en test het met de opdracht `adb devices` vanaf de computerterminal



![adb-devices](assets/fr/08.webp)



*Controleer ADB-verbinding met `adb devices`* commando





- Autoriseer verbinding** op uw telefoon



![usb-debugging-auth](assets/fr/09.webp)



*USB-debugging ingeschakeld met RSA-vingerafdruk van computer*





- Opstarten in bootloadermodus** :


```
adb -d reboot bootloader
```


Of houd **Volume omlaag + Aan/uit** apparaat uit





- Controleer de fastboot** verbinding:


```
fastboot devices
```



![fastboot-mode](assets/fr/10.webp)



*Fastboot commando's in terminal om verbinding te controleren*



![bootloader-screen](assets/fr/11.webp)



*Het fastbootscherm van de Pixel 4 met systeeminformatie*





- Ontgrendel de bootloader** :


```
fastboot flashing unlock
```


Gebruik op het apparaat de volumetoetsen om te navigeren en druk op de **Power** knop om "Unlock the bootloader" te selecteren en bevestig de bewerking



![unlock-bootloader](assets/fr/12.webp)



*Bevestiging van ontgrendeling bootloader op apparaat*



⚠️ **De telefoon wordt automatisch opnieuw opgestart** na bevestiging van ontgrendeling





- Schakel na automatisch opnieuw opstarten** USB-foutopsporing opnieuw in de ontwikkelaarsopties in




#### Stap 3: Extra partities flashen



⚠️ **Verplicht om herstel goed te laten werken**





- Bootloader opnieuw opstarten**: Volume omlaag + Aan/uit
- Flash** (vervang `/path/to/` door de map waar je het bestand hebt gedownload) :


```
fastboot flash dtbo /chemin/vers/dtbo.img
```



![flash-partitions](assets/fr/13.webp)



*Flash van dtbo en boot.img partities via fastboot*



#### Stap 4: LineageOS-herstel installeren





- Flashherstel** (vervang `/path/to/` door de map waar je het bestand hebt gedownload) :


```
fastboot flash boot /chemin/vers/boot.img
```




- Herstart in herstel** om te controleren



#### Stap 5: LineageOS installeren





- Opnieuw opstarten in herstel**: Volume omlaag + Power → Herstelmodus



![recovery-mode](assets/fr/14.webp)



*Interface vanuit LineageOS herstel met hoofdmenu*





- Fabrieksreset** : Type "Fabrieksreset" → "Gegevens formatteren / fabrieksreset"



![factory-reset](assets/fr/15.webp)



*Proces voor fabrieksreset in LineageOS*-herstel





- Terug naar hoofdmenu**
- Laad LineageOS** :
   - Op het apparaat: "Update toepassen" → "Toepassen vanaf ADB"
   - Op PC: `adb -d sideload /path/to/lineageos.zip`



![apply-update](assets/fr/16.webp)



*Selecteer "Update toepassen" en vervolgens "Toepassen vanaf ADB" in herstel*



![sideload-process](assets/fr/17.webp)



*LineageOS installatie bezig via sideload*



![sideload-terminal](assets/fr/18.webp)



*Opdracht Sideload in terminal met voortgang installatie*



normaal**: Het proces kan stoppen bij 47% of "Succes"-fouten weergeven - dit is normaal!



#### Stap 6: De eerste keer opstarten





- Opnieuw opstarten**: "Systeem nu opnieuw opstarten"
- Eerste keer opstarten**: Kan tot 15 minuten duren



**Installatie voltooid!



### Aandachtspunten



⚠️ **Waarschuwing**: LineageOS wordt geleverd "zoals het is" zonder garantie. Hoewel we er alles aan doen om ervoor te zorgen dat alles werkt, installeert u dit op eigen risico!



**Kritische controles:**




- Compatibiliteit firmware**: Controleer de vereiste firmwareversie op de downloadpagina van uw model
- Nooit de bootloader opnieuw vergrendelen** na installatie van LineageOS
- Volg de specifieke instructies** voor uw apparaat



## Configuratie en toepassingen



### Eerste opstart


Gestroomlijnd Interface, dicht bij stock-Android, zonder Google. Eenvoudige configuratie: taal, Wi-Fi, geen account nodig.



### Alternatieve toepassingen



**Bronnen van toepassingen beveiligen:**



**F-Droid** : De open source applicatiewinkel van de benchmark, vooraf geïnstalleerd met LineageOS voor microG of direct te downloaden. F-Droid biedt alleen open-source software die transparant is geverifieerd en gecompileerd, waardoor de afwezigheid van trackers of schadelijke componenten wordt gegarandeerd.



**Aurora Store**: Anonieme client voor toegang tot de Google Play Store zonder Google-account. Aurora leent gedeelde anonieme accounts, waardoor je mainstream apps kunt downloaden terwijl je je privacy behoudt.



**Essentiële alternatieve toepassingen:**





- Navigatie**: Organic Maps (offline kaarten gebaseerd op OpenStreetMap)
- Communicatie**: Signal (end-to-end versleutelde berichten), K-9 Mail (gratis e-mailclient)
- Media**: NewPipe (reclamevrije, trackingvrije YouTube), VLC (universele mediaspeler)
- Productiviteit**: Nextcloud (zelf-hostende cloud), Simple Calendar (CalDAV-synchronisatie)
- Beveiliging**: Bitwarden (wachtwoordbeheerder), Aegis Authenticator (2FA-codes)



Deze applicaties, waarvan de meeste beschikbaar zijn via F-Droid, vormen een samenhangend ecosysteem dat Google-services volledig kan vervangen en tegelijkertijd een moderne, functionele gebruikerservaring biedt.



## Gebruik en onderhoud



### Dagelijkse ervaring



LineageOS transformeert de Android-ervaring en geeft prioriteit aan vloeiendheid en reactiesnelheid. Het gestroomlijnde Interface is vooral effectief op oudere apparaten, die een nieuw leven krijgen, met prestaties die over het algemeen superieur zijn aan ROM's van fabrikanten dankzij de afwezigheid van zware overlays en overbodige processen.



Basisfunctionaliteiten (bellen, sms'en, foto's, browsen) werken naadloos, terwijl aanpassingshulpmiddelen het mogelijk maken het systeem nauwkeurig af te stemmen op individuele voorkeuren zonder de stabiliteit in gevaar te brengen.



### OTA-updatesysteem



LineageOS heeft een bijzonder gebruiksvriendelijk Over-The-Air updatesysteem. Nieuwe versies worden automatisch voorgesteld via meldingen en de installatie neemt slechts een paar klikken in beslag, zonder dat er complexe technische interventie nodig is. Uw geïnstalleerde gegevens en toepassingen blijven volledig behouden.



Deze regelmatige updates zijn een grote aanwinst, vooral voor apparaten die door hun fabrikanten uit productie zijn genomen, die kunnen blijven profiteren van de nieuwste Android-beveiligingspatches.



### Aanbevolen best practices



**Post-installatie beveiliging:**




- Stel een sterke PIN-code of wachtwoord in om te ontgrendelen
- Controleer of opslagcodering is ingeschakeld (meestal standaard)
- Installeer een wachtwoordmanager zoals Bitwarden via F-Droid



**Preventief onderhoud:**




- Regelmatige OTA-updates voor beveiliging
- Installatie van applicaties beperken tot vertrouwde bronnen (F-Droid, Aurora Store)
- Controleer periodiek de toestemmingen voor applicaties
- Af en toe opnieuw opstarten optimaliseert de prestaties en maakt geheugen vrij



## Voordelen en beperkingen



✅ **Voordelen:**




- Standaardprivacy (geen Google-tracking)
- Brede compatibiliteit (300+ modellen)
- Superieure prestaties (geen bloatware)
- Uitgebreide updates op oudere apparaten



❌ **Beperkingen:**




- Technische installatie
- Geen Android Auto/Google Pay
- Bankieren met apps kan problematisch zijn



## GrapheneOS vs LineageOS: wat is het verschil?



### Verschillende benaderingen



**GrapheneOS** richt zich uitsluitend op maximale beveiliging en draait alleen op Google Pixels om gebruik te maken van hun speciale beveiligingschips. Het systeem bevat talrijke geavanceerde maatregelen tegen exploits en versterkt de sandboxing van toepassingen aanzienlijk.



**LineageOS** balanceert beveiliging, privacy en gemak op zoveel mogelijk apparaten. De aanpak is pragmatischer, gericht op uitgebreide compatibiliteit in plaats van absolute veiligheid.



### Google-services beheren



**GrapheneOS**: Biedt een optioneel sandboxed Google Play-systeem. Google Play kan worden geïnstalleerd maar draait in een strikte sandbox, zonder speciale systeemrechten. Deze unieke aanpak maakt het mogelijk om het Google ecosysteem te gebruiken met behoud van strikte beveiligingscontrole.



**LineageOS**: Laat de gebruiker kiezen of hij Google-services (GApps), microG (gratis alternatief) of Google-vrij wil installeren. Maximale flexibiliteit om aan uw behoeften te voldoen.



### Technische vergelijking



| **Aspect** | **GrapheneOS** | **LineageOS** |
|------------|----------------|---------------|
| **Compatibilité** | Pixels uniquement | Centaines d'appareils |
| **Sécurité** | Mitigations avancées | Sécurité AOSP standard |
| **Google Play** | Sandboxé optionnel | Installation classique possible |
| **Installation** | Interface web + USB | Procédure manuelle technique |
| **Philosophie** | Sécurité avant tout | Équilibre et liberté de choix |

### Aanbevelingen voor gebruik



**Kies GrapheneOS** als je een Pixel hebt, als maximale beveiliging je hoogste prioriteit is en als je beperkingen voor betere bescherming accepteert.



**Ga voor LineageOS** als je een niet-Pixel toestel hebt, op zoek bent naar een goede privacy/praktische balans, of de vrijheid wilt om je niveau van compromis met het Google ecosysteem te kiezen.



## Conclusie



LineageOS biedt een volwassen alternatief om de controle over je Android-smartphone terug te krijgen. Ongehinderde ervaring, optimale prestaties, uitgebreide compatibiliteit: de ideale keuze voor het combineren van privacy en alledaags gebruiksgemak.



## Bronnen



### Officiële documentatie




- [Officiële website van LineageOS](https://lineageos.org)
- [LineageOS Wiki](https://wiki.lineageos.org) - Installatiegidsen per model
- [LineageOS voor microG](https://lineage.microg.org) - Versie met geïntegreerde microG



### Gemeenschap




- [Subreddit r/LineageOS](https://reddit.com/r/LineageOS)
- [Mastodon account @LineageOS](https://fosstodon.org/@LineageOS)



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1