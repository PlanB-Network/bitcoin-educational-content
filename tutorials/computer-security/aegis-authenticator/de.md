---
name: Aegis Authenticator
description: Wie können Sie Aegis Authenticator verwenden, um Ihre Konten mit doppelter Authentifizierung zu sichern?
---

![cover](assets/cover.webp)



Heutzutage ist die Zwei-Faktor-Authentifizierung (2FA) für die Sicherung von Online-Konten unerlässlich. Sie fügt dem Passwort einen zweiten Faktor hinzu (oft einen 6-stelligen Code), der nach 30 Sekunden abläuft, was es für Hacker erheblich schwieriger macht. Die Verwendung einer speziellen TOTP-Anwendung (*Time-based One-Time Password*) ist sicherer als SMS, die durch SIM-Swapping-Angriffe missbraucht werden können.



Allerdings sind nicht alle Authentifizierungsanwendungen gleich. Viele proprietäre Lösungen (Google Authenticator, Authy usw.) sind problematisch: Sie sind proprietär und quelloffen (es ist unmöglich, ihre Sicherheit zu überprüfen), integrieren manchmal Werbetracker, bieten kein verschlüsseltes Backup Ihrer Codes und können sogar verhindern, dass Sie Ihre Konten exportieren, um Sie in ihrem Ökosystem zu halten.



Aegis Authenticator hingegen präsentiert sich als eine kostenlose und ethische Alternative zu diesen Anwendungen. Aegis ist eine kostenlose, sichere Open-Source-Anwendung für die Verwaltung Ihrer Zwei-Schritt-Verifizierungs-Tokens auf Android. Seine Entwicklung konzentriert sich auf wesentliche Funktionen, die andere Apps nicht bieten, darunter eine robuste Verschlüsselung lokaler Daten und die Möglichkeit sicherer Backups. Alles in allem bietet Aegis eine lokale, überprüfbare Lösung zur doppelten Authentifizierung, ideal für alle, die die volle Kontrolle über ihre 2FA-Codes behalten möchten.



## Einführung von Aegis Authenticator



Aegis Authenticator ist eine Open-Source-2FA-Anwendung für Android, die unter der GPL v3-Lizenz veröffentlicht wurde. Sie zeichnet sich durch ihre "Privacy by Design"-Philosophie aus: Die Anwendung arbeitet vollständig offline und erfordert keine Verbindung zu einem Remote-Dienst. Folglich bleiben Ihre Token lokal auf Ihrem Gerät gespeichert, in einem sicheren Safe, zu dem nur Sie den Schlüssel besitzen.



### Wesentliche Merkmale



**Verschlüsselter Tresor:** Alle Ihre OTP-Codes werden in einem AES-256-verschlüsselten Tresor (GCM-Modus) gespeichert, der durch ein benutzerdefiniertes Hauptpasswort geschützt ist. Sie können diesen Tresor mit einem Passwort oder biometrischen Daten (Fingerabdruck, Gesichtserkennung) entsperren, um den Komfort zu erhöhen. Ohne ein Passwort wären die Daten unverschlüsselt - wir empfehlen daher dringend, ein Passwort festzulegen.



**Erweiterte Organisation:** Aegis hält Ihre vielen 2FA-Konten gut organisiert. Sie können Ihre Einträge alphabetisch oder in der Reihenfolge Ihrer Wahl sortieren, sie nach Kategorien gruppieren (z. B. Persönlich, Arbeit, Soziales), um sie leichter wiederzufinden, und jedem Eintrag ein persönliches Symbol zuweisen. Eine Suchleiste ermöglicht das sofortige Auffinden eines Dienstes oder Kontos anhand des Namens.



**Verschlüsselte lokale Backups:** Um sicherzustellen, dass Sie nie den Zugang zu Ihren Konten verlieren, bietet Aegis automatische Backups Ihres Safes. Diese sind verschlüsselt (über ein Passwort) und können an einem Ort Ihrer Wahl gespeichert werden (interner Speicher, Cloud-Ordner, etc.). Die Anwendung kann Ihre Kontodatenbank auch manuell exportieren, je nach Bedarf in verschlüsseltem oder unverschlüsseltem Format. Der Import von Konten aus anderen 2FA-Anwendungen ist ebenso einfach (Aegis unterstützt den Import von Authy, Google Authenticator, FreeOTP, andOTP usw.).



**Sicherheit und Datenschutz:** Die Anwendung ist standardmäßig vollständig offline. Sie benötigt keine Netzwerkberechtigungen - das heißt, sie überträgt keine Daten nach außen und verfügt über keine Ad-Tracker oder Module zur Verhaltensanalyse. Aegis zeigt keine Werbung an und benötigt kein Benutzerkonto: Sobald die Anwendung installiert ist, kann sie ohne Registrierung genutzt werden. Da der Quellcode auf GitHub öffentlich zugänglich ist, kann die Community ihn frei überprüfen, was garantiert, dass keine bösartigen oder versteckten Funktionen vorhanden sind.



**Modernes Interface:** Aegis verwendet ein ordentliches Material Design, mit Unterstützung für dunkle Themen (einschließlich eines AMOLED-Modus) und sogar einer optionalen Kachelansicht, um Ihre Codes als Raster anzuzeigen. Interface ist übersichtlich, ohne Schnickschnack und verhindert als Sicherheitsmaßnahme die Bildschirmaufnahme von Codes.



## Einrichtung



Da Aegis Authenticator Open Source ist, bevorzugen die Entwickler datenschutzfreundliche Vertriebskanäle. Es gibt zwei Hauptwege, ihn zu installieren:



### Über F-Droid (empfohlen)



Der sicherste und einfachste Weg ist über F-Droid, den kostenlosen alternativen Store. Wenn F-Droid noch nicht auf Ihrem Telefon installiert ist, laden Sie es zunächst von der offiziellen Website [F-Droid.org] (https://f-droid.org) herunter. Dann :





- Öffnen Sie F-Droid und vergewissern Sie sich, dass Sie Ihre Repositories aktualisiert haben, um die neueste Liste von Anwendungen zu erhalten
- Suchen Sie in F-Droid nach "Aegis Authenticator". Die offizielle Anwendung sollte erscheinen (Herausgeber: Beem Development)
- Starten Sie die Installation durch Drücken von Installieren. Da Aegis eine der von F-Droid verifizierten Anwendungen ist, profitieren Sie von einem zuverlässigen und sicheren Download



Die Installation über F-Droid bietet den Vorteil, dass Sie automatische Anwendungsaktualisierungen erhalten, sobald diese veröffentlicht werden. Darüber hinaus garantiert F-Droid, dass die Anwendung frei von unerwünschten proprietären Komponenten ist.



### Über GitHub (signierte APK)



Wenn Sie die Anwendung lieber ohne den Umweg über einen Store installieren möchten, können Sie die offizielle APK direkt von der GitHub-Seite des Projekts herunterladen. Gehen Sie im Aegis-Repository ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)) zum Abschnitt Releases, wo stabile Versionen veröffentlicht werden.





- Laden Sie die neueste APK-Version herunter
- Stellen Sie vor der Installation der APK sicher, dass Sie die Installation von Anwendungen aus unbekannten Quellen auf Ihrem Gerät zugelassen haben (in den Android-Einstellungen)
- Die auf GitHub zur Verfügung gestellte APK ist vom Entwickler mit demselben Schlüssel signiert wie auf F-Droid



Nach der manuellen Installation wird die Anwendung identisch funktionieren. Bitte beachten Sie, dass Aktualisierungen nicht automatisch erfolgen: Sie müssen regelmäßig auf GitHub nach neuen Versionen suchen.



### Google Play Store vs. F-Droid



Aegis Authenticator ist sowohl im Google Play Store als auch auf F-Droid erhältlich, so dass Sie die Wahl haben, wie Sie es installieren möchten:



**Google Play Store:**




- ✅ In das Android-System integrierte automatische Updates
- ✅ Einfache, vertraute Installation
- ✅ Gleiche signierte APK wie auf anderen Kanälen



**F-Droid (empfohlen) :**




- ✅ Kostenloser und quelloffener Speicher
- ✅ Reproduzierbare und überprüfbare Konstruktion
- ✅ Kein Google-Dienst erforderlich
- ✅ Respekt für die Philosophie der freien Software



Die Wahl zwischen diesen beiden Optionen hängt von Ihren Vorlieben in Bezug auf das Google-Ökosystem ab. Wenn Sie Einfachheit bevorzugen, ist der Play Store ideal. Wenn Sie einen datenschutzfreundlicheren Ansatz wünschen, der unabhängig von Google-Diensten ist, ist F-Droid die bessere Wahl.



## Erste Konfiguration



Wenn Aegis zum ersten Mal gestartet wird, wird ein anfängliches Konfigurationsverfahren vorgeschlagen, um Ihren 2FA-Code sicher zu machen:



![Configuration initiale Aegis](assets/fr/01.webp)



*Anfänglicher Aegis-Konfigurationsprozess: Begrüßungsbildschirm, Sicherheitsauswahl, Festlegung des Master-Passworts und Fertigstellung*



### Festlegen eines Master-Passworts



Aegis fordert Sie zunächst auf, ein Master-Passwort zu wählen. Dieses Kennwort wird zur Verschlüsselung all Ihrer im Tresor gespeicherten Authentifizierungs-Token verwendet. Wir empfehlen Ihnen dringend, ein starkes, eindeutiges Passwort festzulegen, das nur Sie kennen.



**⚠️ Warnung:** Vergessen Sie dieses Passwort nicht - wenn Sie es verlieren, werden Ihre verschlüsselten 2FA-Codes unzugänglich (es gibt keine Hintertür). Aegis fordert Sie auf, das Passwort zweimal zur Bestätigung einzugeben.



### Biometrische Entsperrung aktivieren (optional)



Wenn Ihr Android-Gerät mit einem Fingerabdruckleser oder einem anderen biometrischen Sensor ausgestattet ist, wird Aegis Sie auffordern, die biometrische Entsperrung zu aktivieren. Diese Option ist optional, aber sehr praktisch: Sie ermöglicht es Ihnen, die Anwendung schnell mit Ihrem Fingerabdruck oder Gesicht zu entsperren, anstatt jedes Mal das Passwort einzugeben.



Beachten Sie, dass die Biometrie nur ein zusätzlicher Komfort ist: Ihr Hauptkennwort ist auch dann erforderlich, wenn die biometrischen Daten geändert oder das Gerät neu gestartet wird.



### Anwendungseinstellungen entdecken



Sobald Sie sich in der Anwendung befinden (das Haupt-Interface ist zunächst leer), machen Sie sich mit den verfügbaren Konfigurationsoptionen vertraut. Rufen Sie die Einstellungen über das Dropdown-Menü oben rechts auf dem Bildschirm auf (drei vertikale Punkte) und wählen Sie dann "Einstellungen".



![Interface principale et paramètres](assets/fr/02.webp)



*Interface main Aegis leer beim Start, Zugang zum Parametermenü und Übersicht der verfügbaren Optionen*



Im Aegis-Einstellungsmenü sind mehrere wichtige Bereiche zusammengefasst:





- **Erscheinungsbild**: Anpassen des Themas (hell, dunkel, AMOLED), der Sprache und anderer visueller Einstellungen
- **Verhalten**: Konfigurieren Sie das Verhalten der Anwendung bei der Interaktion mit der Liste der Einträge
- **Icon Packs**: Verwalten und importieren Sie Icon Packs, um das Aussehen Ihrer Konten anzupassen
- **Sicherheit**: Einstellungen für Verschlüsselung, biometrische Entsperrung, automatische Verriegelung und andere Sicherheitsparameter
- **Backups**: Konfigurieren Sie automatische Backups an einem Ort Ihrer Wahl
- **Importieren und Exportieren**: Importieren Sie Backups aus anderen Authentifizierungsanwendungen und exportieren Sie Ihren Aegis-Datenspeicher manuell
- **Audit-Protokoll**: Detailliertes Protokoll aller wichtigen Ereignisse in der Anwendung



Durch diese übersichtliche Organisation können Sie Aegis nach Ihren Wünschen und Sicherheitsanforderungen konfigurieren.



## Ein 2FA-Konto hinzufügen



Nachdem Sie Aegis konfiguriert haben, kommen wir nun zum Wesentlichen: dem Hinzufügen Ihrer Zwei-Faktor-Konten. Der Prozess ist einfach, und Aegis bietet mehrere Methoden zur Integration Ihrer Authentifizierungscodes.



### Die drei verfügbaren Additionsmethoden



Drücken Sie auf dem Hauptbildschirm von Aegis Interface die Taste **+** unten rechts, um die Hinzufügungsoptionen aufzurufen. Sie haben drei Optionen:





- **QR-Code scannen**: Scannen Sie direkt den vom Webservice angezeigten QR-Code
- **Bild scannen**: Scannen Sie einen QR-Code von einem auf Ihrem Gerät gespeicherten Bild
- **Manuell eingeben**: 2FA-Kontoinformationen manuell eingeben



### Praktisches Beispiel: Konfiguration von Bitwarden



Nehmen wir das konkrete Beispiel der 2FA-Aktivierung auf Bitwarden, um den Prozess zu veranschaulichen:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Beispiel einer 2FA-Aktivierung auf Bitwarden: Interface Web mit Authentifizierungsoptionen und Aegis-Empfehlung*





- **Einloggen und Zugriff auf die Einstellungen**: Loggen Sie sich in Ihr Bitwarden-Konto ein und öffnen Sie die Einstellungen, Registerkarte "Sicherheit"
- **Abschnitt Anbieter**: Gehen Sie zum Abschnitt "Anbieter" und klicken Sie auf "Verwalten" im Abschnitt "Authenticator-App"



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Vollständiger Prozess zum Hinzufügen eines Kontos: QR-Code, der vom Dienst angezeigt wird, geheimer Schlüssel sichtbar und Verifizierungscode eingegeben*





- **QR-Code scannen**: Es öffnet sich ein Popup-Fenster mit dem QR-Code und dem geheimen Schlüssel
- In **Aegis**: Verwenden Sie "QR-Code scannen", um Informationen automatisch zu erfassen
- **Verifizierung**: Geben Sie den von Aegis generierten 6-stelligen Code in das Feld "Verifizierungscode" ein
- **Aktivierung**: Klicken Sie auf "Einschalten", um die Aktivierung abzuschließen



### Details manuell hinzufügen



Wenn Sie es vorziehen oder nicht in der Lage sind, den QR-Code zu scannen, verwenden Sie die Option "Manuelle Eingabe". Das Formular ermöglicht Ihnen die Eingabe von :



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Verfahren zum Hinzufügen eines neuen 2FA-Kontos: leeres Interface, Optionen hinzufügen, manuelles Eingabeformular und Konto erfolgreich hinzugefügt*





- **Name**: Name des Dienstes (z. B. Bitwarden, GitHub...)
- **Emittent**: Der Emittent (oft identisch mit dem Namen)
- **Gruppe**: Optional, um Ihre Konten nach Kategorien zu organisieren
- **Anmerkung**: Persönliche Bemerkungen zu diesem Konto
- **Geheim**: Der vom Dienst bereitgestellte geheime Schlüssel (standardmäßig maskiert)
- **Erweitert**: Erweiterte Parameter (Algorithmus, Periode, Anzahl der Ziffern)



Sobald das Konto hinzugefügt wurde, erscheint es in Ihrer Liste mit seinem aktuellen Code und einer Zeitanzeige, die die verbleibende Zeit bis zur Erneuerung angibt.



### Universelle Kompatibilität



Aegis ist mit allen Diensten kompatibel, die die TOTP- und HOTP-Standards verwenden, einschließlich praktisch aller Websites, die 2FA anbieten: soziale Netzwerke, Banken, Passwortmanager, Krypto-Plattformen usw.



### Eingangsorganisation



Sobald Sie mehrere Konten hinzugefügt haben, werden Sie die Organisationstools von Aegis zu schätzen wissen:





- **Benutzerdefinierte Sortierung:** Standardmäßig werden die Konten in alphabetischer Reihenfolge aufgelistet, aber Sie können die Reihenfolge manuell ändern
- **Gruppen und Kategorien:** Erstellen Sie Gruppen, um Ihre persönlichen Konten von Ihren Geschäftskonten zu trennen, oder gruppieren Sie sie nach Art des Dienstes (Bankgeschäfte, E-Mail, soziale Netzwerke usw.)
- **Benutzerdefinierte Icons:** Aegis versucht, automatisch ein passendes Icon zuzuweisen, wenn es verfügbar ist, andernfalls können Sie aus vielen allgemeinen Icons wählen oder ein Bild importieren
- **Schnellsuche:** Mit der Suchleiste am oberen Rand können Sie einige Buchstaben eingeben, um sofort passende Einträge herauszufiltern



Wenn Sie einen Eintrag berühren, wird der OTP-Code in voller Größe angezeigt (falls er ausgeblendet war), und Sie können ihn mit einem langen Druck in die Zwischenablage kopieren - praktisch, um ihn in die Anwendung einzufügen, mit der Sie sich verbinden möchten.



## Sicherheit und Backups



Da die Sicherheit das Herzstück von Aegis ist, ist es wichtig zu verstehen, wie Ihre 2FA-Codes geschützt sind und wie man ihre Beständigkeit im Falle eines Problems sicherstellt.



### Sicherheitsarchitektur



**Robuste Verschlüsselung**: Alle Ihre Codes werden in einem verschlüsselten Tresor unter Verwendung des **AES-256-Algorithmus im GCM-Modus** gespeichert, kombiniert mit Ihrem Master-Passwort. Die Schlüsselableitung basiert auf **scrypt** und bietet einen verbesserten Schutz gegen Brute-Force-Angriffe.



**Sichere Entsperrung** : Das Master-Passwort ist erforderlich, um Ihre Daten zu entschlüsseln. Biometrie (optional) verwendet den **Android Secure Keystore** und TEE (Trusted Execution Environment) zum Schutz des Verschlüsselungsschlüssels.



**Minimale Berechtigungen**: Aegis arbeitet standardmäßig offline und benötigt nur Zugriff auf die Kamera (QR-Scan), die biometrischen Daten und den Vibrator. Es werden keine Daten gesammelt oder weitergegeben.



### Sicherungsoptionen



Aegis bietet verschiedene Backup-Strategien für unterschiedliche Sicherheits- und Komfortbedürfnisse:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface komplett mit zusätzlichem Konto, Sicherungswarnung, automatischen Sicherungseinstellungen und Sicherungsstrategien*



**1. Automatische lokale Backups**




- Konfigurieren Sie einen Zielordner Ihrer Wahl
- Anpassbare Häufigkeit (nach jeder Änderung, täglich, usw.)
- Passwort-geschützte verschlüsselte Dateien (.aesvault)
- Kompatibel mit synchronisierten Ordnern (Nextcloud, Dropbox, etc.)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Auswahl des Sicherungsordners: Datei-Explorer, Zielordner und Zugriffsberechtigung*



**2. Android** Cloud-Backups




- Optionale Integration mit Android-Backup-System
- Nur für verschlüsselte Tresore verfügbar (Sicherheit erhalten)
- Transparentes Backup mit anderen Android-Daten
- Automatische Wiederherstellung bei Geräteumstellung



**3. Manuelle** Ausfuhren




- Export bei Bedarf über **Einstellungen > Import & Export**
- Wahl zwischen verschlüsseltem (empfohlen) und unverschlüsseltem Format
- Nützlich für Migrationen oder gelegentliche Backups



### Gute Sicherheitspraktiken





- Bewahren Sie mehrere **Sicherungsversionen** auf, um Beschädigungen zu vermeiden
- **Testen** Sie regelmäßig Ihre Backups, indem Sie eine Wiederherstellung versuchen
- **Bewahren Sie die vom Dienst bereitgestellten Wiederherstellungscodes separat auf**
- Ihr **Hauptkennwort** ist auch bei Cloud-Backups erforderlich
- **Sichern Sie Ihr Hauptpasswort**: Verwenden Sie ein eindeutiges, sicheres Passwort, das in einem Passwortmanager gespeichert ist
- Halten Sie Ihre Anwendung mit den neuesten Sicherheitspatches auf dem neuesten Stand
- Aktivieren Sie die **automatische Sperre** in den Einstellungen, um den Zugriff auf die Anwendung zu sichern
- Deaktivieren Sie **Screenshots** (Standardoption), damit Ihre Codes nicht abgefangen werden können
- **Biometrische Daten sparsam einsetzen**: Passwörter für kritische Zugriffe bevorzugen



## Vergleich mit anderen Anwendungen



Wie schneidet Aegis im Vergleich zu anderen gängigen Authentifizierungsanwendungen ab?



### Aegis vs. Google Authenticator



**Aegis:**




- ✅ Quelloffen und prüfbar
- ✅ Lokale verschlüsselte Sicherung
- ✅ Erweiterte Organisation (Gruppen, Icons, Suche)
- ✅ Keine Datenerhebung
- ❌ Nur Android



**Google Authenticator :**




- ✅ Verfügbar für Android und iOS
- ✅ Synchronisierung über die Cloud (ab 2023)
- ❌ Geschlossener Quellcode
- ❌ Eingeschränkte Funktionalität
- ❌ Mögliche Datenerfassung durch Google



### Aegis vs. Authy



**Aegis:**




- ✅ Offene Quelle
- ✅ Kein Konto erforderlich
- ✅ Code-Export möglich
- ✅ Datenkontrolle insgesamt
- keine native Multigeräte-Synchronisierung



**Authy:**




- ✅ Synchronisierung mit mehreren Geräten
- ✅ Verfügbar für Android und iOS
- ❌ Geschlossener Quellcode
- ❌ Erfordert eine Telefonnummer
- ❌ Codes können nicht exportiert werden
- ❌ Desktop-Anwendungen werden im März 2024 entfernt



Aegis eignet sich hervorragend für Android-Nutzer, die Wert auf Transparenz, lokale Sicherheit und vollständige Kontrolle über ihre Daten legen. Alternativen wie Authy sind besser geeignet, wenn Sie unbedingt eine automatische Multi-Geräte-Synchronisation benötigen.




## Schlussfolgerung



Aegis Authenticator ist eine hervorragende Lösung für diejenigen, die eine datenschutzfreundliche, sichere und transparente 2FA-Anwendung suchen. Sein Open-Source-Ansatz, kombiniert mit robuster Verschlüsselung und einer übersichtlichen Interface, macht ihn zu einer erstklassigen Wahl für die Sicherung Ihrer Online-Konten.



Obwohl Aegis auf Android beschränkt ist und keine native Cloud-Synchronisation bietet, macht es diese Einschränkungen durch seine "Privacy by Design"-Philosophie und die vollständige Datenkontrolle mehr als wett. Für Nutzer, die sich Sorgen um ihre digitale Privatsphäre machen, bietet Aegis eine glaubwürdige und leistungsstarke Alternative zu den marktbeherrschenden proprietären Lösungen.



Die Sicherheit Ihrer Online-Konten muss nicht von der Kulanz kommerzieller Unternehmen abhängen. Mit Aegis behalten Sie die Kontrolle über Ihre Authentifizierungscodes in einem digitalen Tresor, zu dem nur Sie den Schlüssel besitzen.



## Ressourcen



### Offizielle Webseiten




- **Offizielle Website**: [getaegis.app](https://getaegis.app/) - Präsentation der Bewerbung und Download
- **Quellcode**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Offizielles GitHub-Repository
- **F-Droid**: [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Installation über den kostenlosen Store



### Technische Dokumentation




- **Vault-Dokumentation**: [Vault design](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Technische Beschreibung der Verschlüsselung und der sicheren Architektur
- **Offizielle FAQ**: [getaegis.app/#faq](https://getaegis.app/#faq) - Antworten auf häufig gestellte Fragen
- **Projekt-Wiki**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Vollständige Benutzerdokumentation