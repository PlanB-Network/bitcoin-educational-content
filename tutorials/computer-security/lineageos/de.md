---
name: LineageOS
description: Kostenloses, ungebundenes Android-Betriebssystem für Smartphones
---

![cover](assets/cover.webp)



Herkömmliche Android-Systeme, die auf unseren Smartphones vorinstalliert sind, bringen eine Reihe bekannter Probleme mit sich: die intensive Integration von Google-Diensten, die zu einer ständigen Datenüberwachung führt, unerwünschte gesponserte Anwendungen (Bloatware), die von den Herstellern aufgedrängt werden, und die Einstellung der Update-Verfolgung nach einigen Jahren, wodurch noch funktionierende Geräte zur programmierten Obsoleszenz verurteilt werden.



LineageOS präsentiert sich als eine elegante Antwort auf diese Probleme. Als Produkt der Open-Source-Community und direkter Nachfolger von CyanogenMod (das Ende 2016 eingestellt wurde) ist LineageOS ein kostenloses Android-basiertes mobiles Betriebssystem, das den Nutzern wieder die Kontrolle über ihre Smartphones gibt. Das im Dezember 2016 offiziell gestartete Projekt hat mittlerweile über 4,4 Millionen aktive Installationen weltweit und unterstützt Hunderte von Telefonmodellen von über 20 verschiedenen Marken.



![lineageos-homepage](assets/fr/01.webp)



*Offizielle LineageOS-Website zur Vorstellung des Projekts und seiner Ziele*



## Was ist LineageOS?



### Philosophie und Ziele



LineageOS ist ein quelloffenes mobiles Betriebssystem, das auf dem Android Open Source Project (AOSP) basiert und von einer großen Gemeinschaft freiwilliger Mitwirkender weltweit entwickelt wird. Sein inoffizielles Motto könnte lauten: "Dein Gerät, deine Regeln": Das Projekt zielt darauf ab, die Lebensdauer von Smartphones zu verlängern und gleichzeitig eine optimierte, datenschutzfreundliche Android-Erfahrung zu bieten.



Das Projekt entstand aus der Asche von CyanogenMod, einer der beliebtesten alternativen Android-ROMs der Geschichte. Als CyanogenMod Inc. im Dezember 2016 seine Pforten schloss, mobilisierte sich die Community, um LineageOS zu gründen, das den Innovationsgeist und die Open-Source-Philosophie seines Vorgängers beibehält.



Im Gegensatz zu OEM-Android-Distributionen werden bei LineageOS standardmäßig keine Google-Anwendungen vorinstalliert, und Bloatware wird vollständig vermieden. Die Benutzer beginnen mit einem minimalistischen System, das nur die wichtigsten Anwendungen enthält (Telefon, Nachrichten, Kamera, Browser) und können selbst entscheiden, was sie später hinzufügen möchten.



### Auswirkungen und Gemeinschaft



Offizielle Statistiken zeigen das Ausmaß des Projekts: Mit über 4,4 Millionen aktiven Installationen in 224 Ländern ist LineageOS eine der am weitesten verbreiteten Android-Alternativen der Welt. Brasilien liegt mit über 2 Millionen Nutzern an der Spitze, gefolgt von China und den USA, was die universelle Anziehungskraft eines freien, anpassbaren Androids zeigt.




## Hauptmerkmale



### Interface und Benutzererfahrung



**Pures Android**: LineageOS bietet ein authentisches, AOSP-nahes Android-Erlebnis, ohne Hersteller-Overlays oder überflüssige Anwendungen. Das Interface bleibt Android-Nutzern vertraut und bietet dank des Fehlens von Bloatware eine optimale Benutzerfreundlichkeit.



**Standardmäßig Google-frei**: Aus rechtlichen und ethischen Gründen sind keine Google-Dienste vorinstalliert. Dieser "Google-frei"-Ansatz garantiert die vollständige Kontrolle über Ihre persönlichen Daten und verbessert die Leistung durch die Vermeidung von Diensten, die im Hintergrund laufen.



### Personalisierung und Sicherheit



**Erweiterte Anpassungsmöglichkeiten**: LineageOS schaltet viele Optionen frei, die bei Standard-Android nicht verfügbar sind: Neukonfiguration der Navigationstasten, anpassbare Systemthemen, Nutzungsprofile für verschiedene Kontexte (Arbeit, Privat, Spiele).



**Outil Trust**: Integrierte Funktionen, die den Sicherheitsstatus Ihres Geräts überwachen und Sie vor potenziellen Bedrohungen warnen, so dass Sie die Sicherheit Ihres Systems in Echtzeit verfolgen können.



**Erweiterte Updates**: Die LineageOS-Community ist bestrebt, monatliche Sicherheitspatches bereitzustellen, so dass Geräte, die von ihren Herstellern eingestellt werden, weiterhin die neuesten Android-Sicherheitspatches erhalten.



## Kompatible Geräte



LineageOS unterstützt Hunderte von Geräten von über 20 Herstellern: Samsung, Xiaomi, OnePlus, Motorola, Sony, Google Pixel, Fairphone und viele andere. Diese breite Kompatibilität ist einer der größten Vorteile des Projekts gegenüber Alternativen wie GrapheneOS, die auf Pixel-Geräte beschränkt sind.



![devices-compatibility](assets/fr/02.webp)



*LineageOS-kompatible Geräte-Seite mit Filter nach Hersteller*



![google-devices](assets/fr/03.webp)



*Unterstützte Google-Geräte, einschließlich des Pixel 4 (Codename "flame")*



### Beliebte Geräte



Laut offizieller Statistik gehören zu den meistgenutzten Modellen eine Vielzahl von Geräten unterschiedlicher Preis- und Altersklassen, was zeigt, dass LineageOS sowohl älteren Smartphones neues Leben einhauchen als auch neuere Geräte optimieren kann.



### Entscheidende Punkte vor der Installation



**Entsperrbarer Bootloader**: Prüfen Sie, ob Ihr Hersteller/Betreiber die Entsperrung zulässt. Einige Marken, wie Huawei, haben diese Möglichkeit bei neueren Modellen abgeschafft, während andere spezielle Verfahren vorschreiben.



**Exaktes Modell**: Es ist wichtig, die ROM herunterzuladen, die genau zu Ihrem Gerät passt. Zwei Modelle mit ähnlichen Markennamen können sich technisch unterscheiden (z. B. Galaxy S10 vs. S10 5G) und erfordern unterschiedliche Images.



**Skalierbare Unterstützung**: Neuere Geräte werden möglicherweise nicht sofort unterstützt, da die Portierung einen freiwilligen Entwickler erfordert, der sich um sie kümmert. Umgekehrt kann die Unterstützung aufhören, wenn sich der Betreuer eines Geräts aus dem Projekt zurückzieht.



## Einrichtung



### Wesentliche Voraussetzungen



⚠️ **Lesen Sie diese Anleitung vollständig durch, bevor Sie beginnen**, um Probleme zu vermeiden!



**Zurückkehren zur Standard-Firmware (falls erforderlich) :**




- Android-Flash-Tool**: Verwenden Sie das offizielle Google-Tool [flash.android.com] (https://flash.android.com), um Ihr Pixel-Gerät ganz einfach über Ihren Webbrowser (Chrome/Edge erforderlich) auf das Standard-Android zurückzusetzen
- Alternative**: Werksbilder manuell von [developers.google.com/android/images](https://developers.google.com/android/images)



**Obligatorische Voraussetzungstests:**




- Starten Sie Ihr Gerät mindestens einmal** mit dem ursprünglichen Standardsystem
- Testen Sie alle Funktionen**: SMS, Anrufe, Wi-Fi, mobile Daten
- Wichtig**: Stellen Sie sicher, dass Sie SMS senden/empfangen und Anrufe tätigen/empfangen können (auch über WiFi und 4G/5G). Wenn es auf dem Stock-System nicht funktioniert, wird es auch auf LineageOS nicht funktionieren!
- Neuere Geräte**: Bei einigen muss VoLTE/VoWiFi mindestens einmal auf dem Standardsystem verwendet werden, um IMS bereitzustellen



**Systemvorbereitung:**




- Entfernen Sie alle Google**-Konten von Ihrem Gerät, um den Werksreset-Schutz zu umgehen, der die Aktivierung blockieren kann
- Vollständige Sicherung** : Bei diesem Vorgang wird Ihr Telefon vollständig gelöscht. Sichern Sie Fotos, Kontakte, Anwendungen und wichtige Dateien



**ADB und Fastboot Tools:** Folgen Sie der [offiziellen LineageOS-Anleitung] (https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot), um die Android SDK Platform Tools zu installieren. Überprüfen Sie die Installation mit `adb version` und `fastboot --version`.



**Telefonkonfiguration:**




- Aktivieren Sie **Entwickleroptionen**: Einstellungen > Über > 7 Mal auf "Build-Nummer" tippen



![android-version](assets/fr/06.webp)



*Navigieren Sie zu Einstellungen > Über das Telefon, um den Entwicklermodus zu aktivieren*





- Aktivieren Sie **USB-Debugging** in den Entwickleroptionen
- Aktivieren Sie **OEM Unlock** (unerlässlich für die Entsperrung des Bootloaders)



![developer-options](assets/fr/07.webp)



*Entwickleroptionen, USB-Debugging und OEM-Entsperrung aktivieren*



### Detaillierte Installation



⚠️ **Diese Anweisungen sind spezifisch für LineageOS 22.2. Befolgen Sie jeden Schritt genau. Machen Sie nicht weiter, wenn etwas fehlschlägt!



#### Schritt 1: Überprüfung der Firmware



**Firmware erforderlich**: Auf Ihrem Gerät muss Android 13 installiert sein, bevor Sie fortfahren können (für Pixel 4). Firmware bezieht sich auf die gerätespezifischen Bilder, die im Standardsystem enthalten sind.



![pixel4-info](assets/fr/04.webp)



*Offizielle Pixel 4-Seite mit Download-Links und Installationsanleitungen*



![downloads-page](assets/fr/05.webp)



*LineageOS Build Download-Seite und Dateien*



**Pixel 4 spezifische Downloads:**




- LineageOS** bauen: [download.lineageos.org/devices/flame/builds](https://download.lineageos.org/devices/flame/builds)
- Erforderliche Dateien**: Laden Sie die 3 erforderlichen Dateien von dieser Seite herunter (sie werden in den folgenden Schritten verwendet):
  - lineage-22.2-YYYYYMMDD-nightly-flame-signed.zip" (Haupt-ROM)
  - dtbo.img` (Partitions-Gerätebaum-Blob)
  - boot.img" (Wiederherstellung LineageOS)



⚠️ **Wichtig**: Überprüfen Sie die Android-Version, nicht die Betriebssystemversion des Herstellers. Eine benutzerdefinierte ROM (auch LineageOS) ist keine Garantie dafür, dass diese Anforderung erfüllt ist.



💡 **Tipp**: Wenn Sie Zweifel an Ihrer Firmware haben, kehren Sie zum Originalsystem zurück, bevor Sie fortfahren!



#### Schritt 2: Entriegeln des Bootloaders



⚠️ **Dieser Schritt löscht alle Ihre Daten!





- Testen Sie die ADB-Verbindung**: Schließen Sie Ihr Gerät über USB an und testen Sie es mit dem Befehl `adb devices` von Ihrem Computerterminal aus



![adb-devices](assets/fr/08.webp)



*Überprüfen Sie die ADB-Verbindung mit dem Befehl `adb devices`*





- Verbindung** auf Ihrem Telefon autorisieren



![usb-debugging-auth](assets/fr/09.webp)



*USB-Debugging mit dem RSA-Fingerabdruck des Computers aktiviert*





- Booten in den Bootloader-Modus** :


```
adb -d reboot bootloader
```


Oder halten Sie **Lautstärke runter + Power** Gerät aus





- Überprüfen Sie die fastboot**-Verbindung:


```
fastboot devices
```



![fastboot-mode](assets/fr/10.webp)



*Fastboot-Befehle im Terminal zur Überprüfung der Verbindung*



![bootloader-screen](assets/fr/11.webp)



*Das Fastboot-Display des Pixel 4 mit Systeminformationen*





- Entsperren Sie den Bootloader** :


```
fastboot flashing unlock
```


Verwenden Sie auf dem Gerät die Lautstärketasten zum Navigieren und drücken Sie die **Einschalttaste**, um "Bootloader entsperren" auszuwählen und den Vorgang zu bestätigen



![unlock-bootloader](assets/fr/12.webp)



*Bestätigung der Entsperrung des Bootloaders auf dem Gerät*



⚠️ **Das Telefon wird nach der Bestätigung der Entsperrung automatisch neu gestartet**





- Aktivieren Sie nach dem automatischen Neustart** das USB-Debugging in den Entwickleroptionen erneut




#### Schritt 3: Flashen zusätzlicher Partitionen



⚠️ **Erforderlich für die ordnungsgemäße Wiederherstellung**





- Bootloader neu starten**: Lautstärke runter + Power
- Flash** (ersetzen Sie `/path/to/` durch den Ordner, in den Sie die Datei heruntergeladen haben) :


```
fastboot flash dtbo /chemin/vers/dtbo.img
```



![flash-partitions](assets/fr/13.webp)



*Flashen von dtbo- und boot.img-Partitionen über fastboot*



#### Schritt 4: Installation der LineageOS-Wiederherstellung





- Flash Recovery** (ersetzen Sie `/path/to/` durch den Ordner, in den Sie die Datei heruntergeladen haben) :


```
fastboot flash boot /chemin/vers/boot.img
```




- Neustart in der Wiederherstellung** zur Überprüfung



#### Schritt 5: Installation von LineageOS





- Neustart im Wiederherstellungsmodus**: Leiser + Ein/Aus → Wiederherstellungsmodus



![recovery-mode](assets/fr/14.webp)



*Interface aus LineageOS-Wiederherstellung mit Hauptmenü*





- Werksrückstellung** : Tippen Sie "Werksreset" → "Daten formatieren / Werksreset"



![factory-reset](assets/fr/15.webp)



*Zurücksetzen auf die Werkseinstellungen in der LineageOS*-Wiederherstellung





- Zurück zum Hauptmenü**
- LineageOS** von der Seite laden:
   - Auf dem Gerät: "Update anwenden" → "Von ADB anwenden"
   - Auf dem PC: "adb -d sideload /path/to/lineageos.zip"



![apply-update](assets/fr/16.webp)



*Wählen Sie in der Wiederherstellung* "Update anwenden" und dann "Von ADB anwenden"



![sideload-process](assets/fr/17.webp)



*LineageOS-Installation läuft über sideload*



![sideload-terminal](assets/fr/18.webp)



*Sideload-Befehl im Terminal mit Installationsfortschritt*



💡 **Normal**: Es kann vorkommen, dass der Prozess bei 47% anhält oder "Success"-Fehler anzeigt - das ist normal!



#### Schritt 6: Erste Inbetriebnahme





- Neustart**: "System jetzt neu starten"
- Erster Start**: Kann bis zu 15 Minuten dauern



🎉 **Installation abgeschlossen!**



### Aufmerksamkeiten



⚠️ **Warnung**: LineageOS wird "wie besehen" ohne Garantie zur Verfügung gestellt. Während wir uns bemühen, sicherzustellen, dass alles funktioniert, installieren Sie dies auf eigene Gefahr!



**Kritische Prüfungen:**




- Firmware-Kompatibilität**: Stellen Sie sicher, dass Sie die erforderliche Firmware-Version auf der Download-Seite Ihres Modells überprüfen
- Den Bootloader nach der Installation von LineageOS nie wieder sperren**
- Befolgen Sie die spezifischen Anweisungen** für Ihr Gerät



## Konfiguration und Anwendungen



### Erste Inbetriebnahme


Schlankes Interface, nahe am Standard-Android, ohne Google. Einfache Konfiguration: Sprache, Wi-Fi, kein Konto erforderlich.



### Alternative Anwendungen



**Sichere Anwendungsquellen:**



**F-Droid** : Der Benchmark Open Source Application Store, vorinstalliert mit LineageOS für microG oder direkt herunterladbar. F-Droid bietet nur Open-Source-Software an, die verifiziert und transparent kompiliert wurde, was das Fehlen von Trackern oder bösartigen Komponenten garantiert.



**Aurora Store**: Anonymer Client für den Zugriff auf den Google Play Store ohne ein Google-Konto. Aurora leiht sich gemeinsam genutzte anonyme Konten und ermöglicht es Ihnen, Mainstream-Apps herunterzuladen und gleichzeitig Ihre Privatsphäre zu wahren.



**Wesentliche alternative Anwendungen:**





- Navigation**: Organische Karten (Offline-Karten auf Basis von OpenStreetMap)
- Kommunikation**: Signal (Ende-zu-Ende-verschlüsselte Nachrichten), K-9 Mail (kostenloser E-Mail-Client)
- Medien**: NewPipe (werbefreies, verfolgungsfreies YouTube), VLC (universeller Media-Player)
- Produktivität**: Nextcloud (selbst gehostete Cloud), Simple Calendar (CalDAV-Synchronisierung)
- Sicherheit**: Bitwarden (Passwortmanager), Aegis Authenticator (2FA-Codes)



Diese Anwendungen, von denen die meisten über F-Droid verfügbar sind, bilden ein kohärentes Ökosystem, das Google-Dienste vollständig ersetzen kann und gleichzeitig ein modernes, funktionales Benutzererlebnis bietet.



## Nutzung und Wartung



### Tägliche Erfahrung



LineageOS verändert das Android-Erlebnis und legt dabei den Schwerpunkt auf Flüssigkeit und Reaktionsfähigkeit. Das gestraffte Interface ist besonders effektiv auf älteren Geräten, die ein neues Leben erhalten, mit einer Leistung, die im Allgemeinen besser ist als die der Hersteller-ROMs, dank des Fehlens von schweren Overlays und überflüssigen Prozessen.



Die grundlegenden Funktionen (Anrufe, SMS, Fotos, Surfen) funktionieren nahtlos, während die Anpassungswerkzeuge eine Feinabstimmung des Systems auf die individuellen Vorlieben ermöglichen, ohne die Stabilität zu beeinträchtigen.



### OTA-Update-System



LineageOS verfügt über ein besonders einfach zu bedienendes Over-The-Air-Update-System. Neue Versionen werden automatisch über Benachrichtigungen vorgeschlagen, und die Installation erfolgt mit wenigen Klicks, ohne dass komplexe technische Eingriffe erforderlich sind. Dabei bleiben Ihre installierten Daten und Anwendungen vollständig erhalten.



Diese regelmäßigen Updates sind ein großer Vorteil, vor allem für Geräte, die von ihren Herstellern nicht mehr hergestellt werden, da sie weiterhin von den neuesten Android-Sicherheitspatches profitieren können.



### Empfohlene bewährte Verfahren



**Nach der Installation Sicherheit:**




- Legen Sie eine sichere PIN oder ein Passwort für die Entsperrung fest
- Prüfen Sie, ob die Speicherverschlüsselung aktiviert ist (normalerweise standardmäßig)
- Installieren Sie einen Passwort-Manager wie Bitwarden über F-Droid



**Vorbeugende Instandhaltung:**




- Regelmäßige OTA-Updates für die Sicherheit
- Begrenzung der Anwendungsinstallation auf vertrauenswürdige Quellen (F-Droid, Aurora Store)
- Regelmäßige Überprüfung der für Anwendungen erteilten Genehmigungen
- Gelegentliche Neustarts optimieren die Leistung und geben Speicher frei



## Vorteile und Grenzen



✅ **Vorteile:**




- Standard-Datenschutz (kein Google-Tracking)
- Breite Kompatibilität (über 300 Modelle)
- Überlegene Leistung (keine Bloatware)
- Erweiterte Updates für ältere Geräte



❌ **Einschränkungen:**




- Technische Installation
- Kein Android Auto/Google Pay
- Banking-Apps können problematisch sein



## GrapheneOS vs LineageOS: Was ist der Unterschied?



### Unterschiedliche Ansätze



**GrapheneOS** konzentriert sich ausschließlich auf maximale Sicherheit und läuft nur auf Google Pixels, um deren spezielle Sicherheitschips zu nutzen. Das System enthält zahlreiche fortschrittliche Schutzmaßnahmen gegen Exploits und stärkt das Sandboxing von Anwendungen erheblich.



**LineageOS** schafft ein Gleichgewicht zwischen Sicherheit, Datenschutz und Komfort auf so vielen Geräten wie möglich. Der Ansatz ist eher pragmatisch und zielt eher auf erweiterte Kompatibilität als auf absolute Sicherheit ab.



### Verwaltung von Google-Diensten



**GrapheneOS**: Bietet ein optionales Google Play-System mit Sandbox. Google Play kann installiert werden, läuft aber in einer strikten Sandbox, ohne spezielle Systemprivilegien. Dieser einzigartige Ansatz ermöglicht die Nutzung des Google-Ökosystems unter Beibehaltung einer strengen Sicherheitskontrolle.



**LineageOS**: Der Benutzer kann wählen, ob er Google-Dienste (GApps), microG (kostenlose Alternative) installieren möchte oder ganz auf Google verzichten will. Maximale Flexibilität, um Ihren Bedürfnissen gerecht zu werden.



### Technischer Vergleich



| **Aspect** | **GrapheneOS** | **LineageOS** |
|------------|----------------|---------------|
| **Compatibilité** | Pixels uniquement | Centaines d'appareils |
| **Sécurité** | Mitigations avancées | Sécurité AOSP standard |
| **Google Play** | Sandboxé optionnel | Installation classique possible |
| **Installation** | Interface web + USB | Procédure manuelle technique |
| **Philosophie** | Sécurité avant tout | Équilibre et liberté de choix |

### Empfehlungen für die Verwendung



**Entscheiden Sie sich für GrapheneOS**, wenn Sie ein Pixel besitzen, wenn maximale Sicherheit Ihre oberste Priorität ist und wenn Sie Einschränkungen für einen verbesserten Schutz akzeptieren.



**Entscheiden Sie sich für LineageOS**, wenn Sie ein Nicht-Pixel-Gerät besitzen, ein gutes Gleichgewicht zwischen Privatsphäre und Funktionalität suchen oder die Freiheit haben möchten, Ihre Kompromisse mit dem Google-Ökosystem zu wählen.



## Schlussfolgerung



LineageOS bietet eine ausgereifte Alternative, um die Kontrolle über Ihr Android-Smartphone wiederzuerlangen. Unverfälschtes Erlebnis, optimale Leistung, umfassende Kompatibilität: die ideale Wahl, um Privatsphäre und Alltagstauglichkeit zu verbinden.



## Ressourcen



### Offizielle Dokumentation




- [LineageOS offizielle Website](https://lineageos.org)
- [LineageOS Wiki](https://wiki.lineageos.org) - Installationsanleitungen nach Modell
- [LineageOS für microG](https://lineage.microg.org) - Version mit integriertem microG



### Gemeinschaft




- [Subreddit r/LineageOS](https://reddit.com/r/LineageOS)
- [Mastodon-Konto @LineageOS](https://fosstodon.org/@LineageOS)



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1