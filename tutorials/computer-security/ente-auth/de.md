---
name: Ente Auth
description: Ein quelloffener, Ende-zu-Ende-verschlüsselter 2FA-Authentifikator
---
![cover](assets/cover.webp)



Die Zwei-Faktor-Authentifizierung (2FA) ist für die Sicherung unserer Online-Konten unverzichtbar geworden. Sie erfordert zusätzlich zu Ihrem üblichen Passwort einen temporären Code, der in der Regel von einer speziellen Anwendung generiert wird. Dieser Mechanismus, der als TOTP (Time-Based One-Time Password) bekannt ist, garantiert, dass ein Angreifer, selbst wenn Ihr Passwort kompromittiert wird, nicht in der Lage ist, auf Ihr Konto zuzugreifen, ohne diesen zweiten Faktor zu besitzen, der alle 30 Sekunden erneuert wird.



Die Wahl der richtigen Authentifizierungsanwendung ist jedoch nicht trivial. Google Authenticator ist zwar sehr beliebt, hat aber erhebliche Einschränkungen: proprietärer Code, der nicht überprüft werden kann, Synchronisierung ohne Ende-zu-Ende-Verschlüsselung und das Risiko eines Totalverlusts der Codes im Falle eines Problems mit Ihrem Telefon. Andere Lösungen, wie Authy, erfordern eine Telefonnummer und garantieren keine vollständige Vertraulichkeit.



**Ente Auth** zeichnet sich als moderne, sichere Alternative aus. Diese kostenlose, quelloffene, plattformübergreifende Anwendung, die vom Team hinter [Ente Photos] (https://ente.io) entwickelt wurde, bietet durchgängig verschlüsselte Cloud-Backups und eine nahtlose Synchronisation zwischen all Ihren Geräten. Im Gegensatz zu proprietären Lösungen haben Sie mit Ente Auth die volle Kontrolle über Ihre Authentifizierungscodes, ohne Ihre Privatsphäre zu gefährden.



In diesem Tutorial zeigen wir Ihnen Schritt für Schritt, wie Sie Ente Auth installieren und nutzen können und warum sich diese Lösung von herkömmlichen Authentifikatoren unterscheidet.



## Einführung von Ente Auth



Ente Auth wurde von dem Team entwickelt, das hinter Ente Photos steht, einem Ende-zu-Ende-verschlüsselten und datenschutzfreundlichen Fotospeicherdienst. Getreu der Ente-Philosophie ("Ente" bedeutet "mein" auf Malayalam und symbolisiert die Kontrolle über Ihre Daten) wurde Ente Auth so konzipiert, dass die Nutzer wieder die volle Kontrolle über ihre Zwei-Faktor-Authentifizierungscodes haben.



### Hauptmerkmale



**Standard TOTP-Codes**: Ente Auth generiert temporäre Codes, die mit den meisten Diensten kompatibel sind (GitHub, Google, Binance, ProtonMail, etc.). Sie können so viele 2FA-Konten hinzufügen, wie Sie benötigen, und die Anwendung berechnet die Codes auf der Grundlage der angegebenen Geheimnisse.



**End-to-End verschlüsselte Cloud-Sicherung**: Ihre Codes werden sicher online gespeichert. Nur Sie können sie entschlüsseln - der Verschlüsselungsschlüssel ist von Ihrem Passwort abgeleitet und nur Ihnen bekannt. Ente (der Server) hat keine Kenntnis von Ihren Geheimnissen oder sogar von Ihren Kontotiteln, da alles auf der Client-Seite mit einer Zero-Knowledge-Architektur verschlüsselt wird.



**Synchronisierung mit mehreren Geräten**: Sie können Ente Auth auf mehreren Geräten (Smartphone, Tablet, Computer) installieren und auf Ihre Codes auf allen Geräten zugreifen. Alle Änderungen werden automatisch und sofort über die verschlüsselte Cloud auf Ihre anderen Geräte übertragen, so dass Sie bei Ihrer täglichen Arbeit sehr flexibel sind.



**Minimalistisches, intuitives Interface**: Die Anwendung bietet ein schlankes Interface, das auch für technisch nicht versierte Benutzer leicht zu erlernen ist. 2FA-Konten werden mit dem Namen des Dienstes, Ihrem Login und dem 6-stelligen Code angezeigt und in Echtzeit aktualisiert. Ente Auth zeigt auch den nächsten Code ein paar Sekunden im Voraus an, um zu vermeiden, dass Sie durch den Ablauf des Codes überrumpelt werden.



**Open Source und geprüft**: Der Quellcode von Ente Auth ist [öffentlich auf GitHub](https://github.com/ente-io/auth) und steht unter der AGPL v3.0 Lizenz. Jeder Entwickler kann ihn überprüfen, um nach Fehlern oder unerwünschtem Verhalten zu suchen. Die implementierte Kryptographie war Gegenstand eines [unabhängigen externen Audits](https://ente.io/blog/cryptography-audit/), eine Garantie für die Seriosität der Sicherheit der Anwendung.



### Vorteile und Grenzen



**Vorteile:**




- Datenschutz durch Design mit End-to-End-Verschlüsselung
- Sichere Synchronisierung zwischen all Ihren Geräten
- Prüfbarer offener Quellcode
- Interface klare, intuitive Bedienung Interface
- Automatisches Backup, um den Verlust von Codes zu verhindern
- Verfügbar auf allen Plattformen (Mobil und Desktop)



**Grenzen:**




- Internetverbindung für die Synchronisierung erforderlich
- Fortgeschrittene Benutzer bevorzugen vielleicht 100%ige Offline-Lösungen wie Aegis (nur Android)
- Relativ neu im Vergleich zu etablierten Lösungen



## Einrichtung



Ente Auth ist auf den meisten gängigen Plattformen verfügbar. Sie können die Anwendung von [der offiziellen Website] (https://ente.io/auth) oder aus den offiziellen Stores herunterladen.



![Installation d'Ente Auth](assets/fr/01.webp)



*Ente Auth Download-Seite mit allen verfügbaren Plattformen*



### Android


Sie haben mehrere Möglichkeiten:




- **Google Play Store**: Suchen Sie nach "Ente Auth" für die klassische Installation
- **F-Droid**: Erhältlich aus dem Open-Source-Anwendungskatalog für Android, mit einer Garantie für geprüfte Konstruktion und ohne proprietäre Inhalte
- **Manuelle Installation**: APK-Dateien können von der [GitHub-Seite des Projekts](https://github.com/ente-io/auth/releases) heruntergeladen werden, mit integrierter Benachrichtigung über neue Versionen



### iOS (iPhone/iPad)


Installieren Sie Ente Auth direkt aus dem Apple App Store, indem Sie nach dem Namen der App suchen. Die iOS App kann auch auf Macs mit Apple Silicon Chip (M1/M2) über den Mac App Store ausgeführt werden.



### Computer (Windows, macOS, Linux)


Ente Auth bietet native Desktop-Anwendungen an. Besuchen Sie [ente.io/download](https://ente.io/download) oder den [Releases-Bereich von GitHub](https://github.com/ente-io/auth/releases) :





- **Windows**: Ein EXE-Installationsprogramm wird mitgeliefert
- **macOS**: DMG-Disk-Image in Anwendungen ziehen und ablegen
- **Linux**: Mehrere Formate verfügbar (AppImage portable, .deb für Debian/Ubuntu, .rpm für Fedora/Red Hat)



**Hinweis:** Dieses Tutorial basiert auf Ente Auth v4.4.4 und höher. Frühere Versionen können kleinere Interface-Unterschiede aufweisen.



### Interface Web


Ohne Installation können Sie über [auth.ente.io] (https://auth.ente.io) von jedem Browser aus auf Ihre Codes zugreifen. Interface Web ist auf die Anzeige von Codes beschränkt (nützlich für die Fehlersuche), da das Hinzufügen von Konten aus Sicherheitsgründen die mobile oder Desktop-Anwendung erfordert.



## Erste Konfiguration



### Erstellung eines Kontos



Wenn Sie Ente Auth zum ersten Mal starten, haben Sie zwei Möglichkeiten:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Startbildschirm von Ente Auth mit Optionen zur Kontoerstellung*



**Mit Konto (empfohlen)**: Wählen Sie "Konto erstellen" und geben Sie Ihre E-Mail Address und ein Passwort ein. **Wichtig**: Dieses Passwort dient als Master-Passwort für die Verschlüsselung Ihrer Daten. Wählen Sie ein starkes, eindeutiges Passwort, da es kein herkömmliches Rücksetzverfahren ohne Datenverlust gibt. Wenn Sie es verlegen, sind Ihre verschlüsselten Daten unwiederbringlich verloren.



**Offline-Modus**: Wählen Sie "Ohne Backups verwenden", um die Anwendung lokal ohne Cloud zu verwenden. In diesem Modus bleiben Ihre Codes auf dem Gerät, aber Sie müssen sie manuell exportieren, um sie nicht zu verlieren.



![Vérification email et récupération de clé](assets/fr/03.webp)



*E-Mail-Verifizierungsprozess und Generierung eines 24-Wörter-Wiederherstellungsschlüssels*



Eine E-Mail-Verifizierung kann angefordert werden, um die Kontoerstellung zu bestätigen und die Wiederherstellung auf einem neuen Gerät zu ermöglichen. Ente Auth stellt Ihnen auch einen Wiederherstellungsschlüssel mit 24 Wörtern zur Verfügung (basierend auf der BIP39-Methode). **Bewahren Sie diesen Schlüssel** unbedingt an einem sicheren Ort auf: Er ist die einzige Möglichkeit, Ihre Daten wiederherzustellen, wenn Sie Ihr Passwort vergessen haben.



### Lokale Sicherheit



Ich empfehle dringend, den lokalen Schutz durch einen Code oder biometrische Daten zu aktivieren. Gehen Sie zu **Einstellungen → Sicherheit → Sperrbildschirm** und konfigurieren Sie :





- **Biometrische Entsperrung**: Face ID, Fingerabdruck, abhängig von den Funktionen Ihres Geräts
- Anwendungsspezifische PIN/Passwort
- **Auto-Lock-Verzögerung**: z. B. "Sofort" oder nach 30 Sekunden Inaktivität



Dieser Schutz verhindert den unbefugten Zugriff auf Ihre Codes, falls sich jemand Zugang zu Ihrem entsperrten Telefon verschafft. Beachten Sie, dass diese Sperre eine zusätzliche Barriere ist: Ihre Daten bleiben auch ohne diesen Schutz Ende-zu-Ende-verschlüsselt.



## 2FA-Konten hinzufügen



### Standardverfahren



Um ein neues 2FA-Konto hinzuzufügen, nehmen wir das konkrete Beispiel der Aktivierung von 2FA auf Bull Bitcoin :



![Configuration du premier compte](assets/fr/04.webp)



*Der Haupt-Interface von Ente Auth ist bereit, das erste 2FA*-Konto hinzuzufügen



**Diensteseite (Bull Bitcoin)**: Melden Sie sich bei Ihrem Bull Bitcoin-Konto an, gehen Sie zu den Sicherheitseinstellungen und aktivieren Sie die Zwei-Faktor-Authentifizierung.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Interface Bull Bitcoin* Menü Sicherheitseinstellungen



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Option zur Aktivierung der Zwei-Faktor-Authentifizierung bei Bull Bitcoin*



Der Dienst zeigt dann einen QR-Code an, den Sie mit Ihrer Authentifizierungsanwendung scannen können:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*Vom Bull Bitcoin generierter QR-Code, der mit Ihrem Authentifikator* zu scannen ist



**In Ente Auth**: Klicken Sie auf "Enter a setup key" und scannen Sie den vom Bull Bitcoin angezeigten QR-Code. Ente Auth wird das Konto automatisch erkennen und die Felder ausfüllen.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Konfigurieren der Bull Bitcoin-Kontodetails in Ente Auth*



Sie können den Namen des Dienstes und Ihre Anmeldung anpassen, damit er leichter zu finden ist. Die erweiterten Einstellungen (SHA1-Algorithmus, 30er-Periode, 6 Ziffern) sind in der Regel standardmäßig korrekt.



**Service-seitige Validierung**: Kehren Sie zum Bull Bitcoin zurück und geben Sie den von Ente Auth generierten 6-stelligen Code ein, um die Aktivierung abzuschließen.



![Saisie du code 2FA](assets/fr/09.webp)



*Geben Sie den von Ente Auth generierten Code ein, um die 2FA*-Aktivierung zu bestätigen



![2FA activée](assets/fr/10.webp)



*Bestätigung der erfolgreichen 2FA-Aktivierung auf Bull Bitcoin*



**Backup-Codes**: Bull Bitcoin stellt Ihnen Wiederherstellungscodes zur Verfügung. **Speichern Sie sie an einem sicheren Ort, getrennt von Ihrem Authentifikator.**



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Option auf generate Notfallsicherungscodes auf Bull Bitcoin*



![Codes de récupération](assets/fr/12.webp)



*Liste der Wiederherstellungscodes, die Sie an einem sicheren Ort aufbewahren sollten*



### Organisation und Verwaltung



Ente Auth bietet mehrere praktische Funktionen:



**Schnellkopie**: Drücken Sie den Code, um ihn automatisch in die Zwischenablage zu kopieren.



**Kontextabhängige Aktionen**: Halten Sie die Taste gedrückt (oder klicken Sie mit der rechten Maustaste auf den Desktop), um einen Eintrag zu bearbeiten, zu löschen, zu teilen oder anzuheften.



**Tags und Suche**: Organisieren Sie Ihre Konten mit Tags (persönlich/beruflich, nach Dienstkategorie) und verwenden Sie die Suchleiste, um schnell zu filtern.



![Création d'un tag](assets/fr/17.webp)



*Tag-Erstellungsprozess: Kontextmenü und Erstellungsdialog*



![Tag appliqué](assets/fr/18.webp)



*Tag "Bitcoin" erfolgreich auf Bull Bitcoin*-Konto angewendet



**Automatische Icons**: Jeder Eintrag kann mit dem Logo des Dienstes illustriert werden, dank der Integration des Icon Packs [Simple Icons] (https://simpleicons.org/).



**Vorübergehende sichere Freigabe**: Eine einzigartige Funktion von Ente Auth: Mit der sicheren Freigabe können Sie einen 2FA-Code an einen Kollegen übermitteln, ohne das zugrunde liegende Geheimnis preiszugeben. generate einen verschlüsselten Link, der für maximal 2, 5 oder 10 Minuten gültig ist - der Empfänger sieht den Code in Echtzeit, kann ihn aber nicht exportieren oder auf Kontodaten zugreifen. Diese Methode ist ideal für technische Unterstützung oder vorübergehende Zusammenarbeit und bietet ein Maß an Sicherheit, das mit einem einfachen Screenshot oder einer Textnachricht nicht möglich ist.



![Partage sécurisé](assets/fr/19.webp)



*Interface vorübergehende sichere Freigabe: Dauer wählen (5 min)*



**Sicherer Export/Import**: Mit Ente Auth können Sie Ihre Codes in andere Anwendungen exportieren oder sie aus Google Authenticator und anderen Lösungen importieren. Der Export erfolgt über eine verschlüsselte Datei oder einen QR-Code, wodurch die Übertragbarkeit Ihrer Daten ohne Sicherheitseinbußen gewährleistet wird.



**BIP39-Wiederherstellungsschlüssel**: Die Anwendung generiert automatisch eine Wiederherstellungsphrase mit 24 Wörtern nach dem BIP39-Standard (Bitcoin Improvement Proposal), der mit den Geldbörsen für Kryptowährungen identisch ist. Diese Phrase ist Ihr ultimativer Wiederherstellungsschlüssel, mit dem Sie alle Ihre Codes wiederherstellen können, selbst wenn Sie Ihr Master-Passwort vergessen haben.



## Konfiguration und Einstellungen



Ente Auth bietet zahlreiche Anpassungsmöglichkeiten, die über die Anwendungseinstellungen zugänglich sind:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Übersicht der in Ente Auth* verfügbaren Parameter



### Konto- und Datenverwaltung



![Paramètres de sécurité](assets/fr/14.webp)



*Erweiterte Sicherheitsoptionen: E-Mail-Verifizierung, PIN-Code, aktive Sitzungen*



Die Sicherheitseinstellungen ermöglichen es Ihnen, :




- Aktivieren Sie die E-Mail-Überprüfung für neue Verbindungen
- Passkey aktivieren
- Aktive Sitzungen auf Ihren verschiedenen Geräten anzeigen
- Einrichten eines PIN-Codes oder biometrischer Daten



### Interface und Nutzungsmöglichkeiten



![Paramètres généraux](assets/fr/15.webp)



*Interface-Parameter und Anwendungsanpassung*



Allgemeine Einstellungen sind:




- **Sprache**: Interface mehrsprachig
- **Anzeige**: Große Icons, kompakter Modus
- **Datenschutz**: Codes verbergen, Schnellsuche
- **Telemetrie**: Fehlerberichterstattung (kann deaktiviert werden)



## Sicherung und Synchronisierung



### Wie die Verschlüsselung funktioniert



Wenn Sie ein Konto mit einem verbundenen Ente-Konto hinzufügen, verschlüsselt die Anwendung diese sensiblen Daten sofort lokal mit Ihrem Hauptschlüssel (abgeleitet von Ihrem Passwort). Die verschlüsselten Daten werden dann zur Speicherung an den Ente-Server gesendet.



Dank dieses Mechanismus ist ein Ende-zu-Ende-verschlüsseltes Cloud-Backup Ihrer Codes immer verfügbar. Wenn Sie Ihr Gerät verlieren, installieren Sie einfach Ente Auth neu und stellen Sie die Verbindung wieder her: Die Anwendung lädt automatisch alle Ihre Codes herunter und entschlüsselt sie.



### Multi-Geräte-Synchronisation



Wenn Sie Ente Auth sowohl auf dem Smartphone als auch auf dem Computer verwenden, erscheinen alle Ergänzungen oder Änderungen auf einem Gerät innerhalb von Sekunden auf dem anderen. Diese Synchronisierung läuft über die Cloud von Ente, aber da die Daten Ende-zu-Ende verschlüsselt sind, sieht der Server nur unlesbare verschlüsselte Inhalte.



![Synchronisation mobile](assets/fr/16.webp)



*Synchronisierungsdemo: Dasselbe Bull Bitcoin-Konto ist auf dem Handy und dem Desktop zugänglich*



Die Synchronisierung ist nahtlos: Installieren Sie Ente Auth auf Ihrem Smartphone, melden Sie sich mit Ihren Anmeldedaten an, und alle Ihre 2FA-Codes (hier Bull Bitcoin) erscheinen automatisch. Das obige Beispiel zeigt die perfekte Synchronisation zwischen Desktop und Mobile - der gleiche Bull Bitcoin Code ist auf beiden Geräten zugänglich.



Was die Vertraulichkeit betrifft, so hat weder Ente noch ein Dritter Zugang zu Ihren 2FA-Geheimnissen. Sogar Metadaten (Tags, Notizen, Dienstnamen) werden verschlüsselt, bevor sie gesendet werden. Diese Zero-Knowledge-Architektur stellt sicher, dass nur Sie Ihre Codes entschlüsseln können.



### Offline-Nutzung



Für die Synchronisierung ist das Internet erforderlich, aber Ente Auth funktioniert perfekt offline auf jedem Gerät, da alle Daten lokal gespeichert sind. Offline-Änderungen werden in eine Warteschlange gestellt und synchronisiert, sobald die Verbindung wiederhergestellt ist.



## Sicherheit und Datenschutz



### Kryptografische Garantien



Ente Auth basiert auf einer robusten Ende-zu-Ende-Verschlüsselung mit Zero-Knowledge-Architektur. Ihre Codes werden mit einem Schlüssel verschlüsselt, den nur Sie besitzen und der von Ihrem Master-Passwort mit Hilfe fortschrittlicher Schlüsselableitungsfunktionen abgeleitet wird.



**Zero-Knowledge-Architektur:** Ente hat keinen physischen Zugriff auf Ihre Daten. Selbst Metadaten (Dienstnamen, Tags, Notizen) werden vor der Übertragung auf der Client-Seite verschlüsselt. Dieser Ansatz gewährleistet, dass Ente im Falle eines Angriffs auf Ihre Server oder einer behördlichen Anfrage nur verschlüsselte Daten offenlegen kann, die ohne Ihr Passwort nicht gelesen werden können.



**Lokale Verschlüsselung**: Der Verschlüsselungsprozess findet vollständig auf Ihrem Gerät statt, bevor die Daten an die Cloud gesendet werden. Die Server von Ente empfangen und speichern nur verschlüsselte Daten, was einen unbefugten Zugriff unmöglich macht, selbst für Service-Administratoren.



### Transparenz und Audits



Da der Code [quelloffen](https://github.com/ente-io/auth) ist, kann die Gemeinschaft überprüfen, ob es keine Hintertüren gibt. Ente hat [mehrere externe Audits](https://ente.io/blog/cryptography-audit/) durchführen lassen, um die Sicherheit seiner Implementierung zu validieren:





- **Cure53** (Deutschland): Audit der Anwendungs- und Kryptosicherheit
- **Symbolic Software** (Frankreich): Spezialisiertes kryptographisches Fachwissen
- **Fallible** (Indien): Penetrationstests und Schwachstellenanalyse



Diese unabhängigen Audits, die von anerkannten Unternehmen durchgeführt werden, garantieren, dass die kryptografische Implementierung von Ente Auth den besten Sicherheitspraktiken entspricht und keine kritischen Schwachstellen aufweist.



### Datenschutzbestimmungen



Ente Auth wendet eine [beispielhafte Datenschutzpolitik](https://ente.io/privacy/) an, die auf einer minimalen Datenerfassung basiert. Es werden nur Informationen gespeichert, die für den Betrieb des Dienstes unbedingt erforderlich sind: Ihre E-Mail Address für die Authentifizierung und die Wiederherstellung des Kontos.



**Kein Tracking oder Telemetrie**: Im Gegensatz zu den meisten Anwendungen sammelt Ente Auth keine Nutzungsmetriken, keine identifizierenden Absturzdaten und keine verhaltensbezogenen Informationen. Die Anwendung arbeitet ohne aufdringliche Werbung oder analytische Tracker.



**GDPR-Konformität**: Ente hält sich vollständig an die europäische Datenschutzverordnung (General Data Protection Regulation). Sie haben jederzeit das Recht, Ihre Daten einzusehen, zu korrigieren oder zu löschen. Der Datenexport] (https://ente.io/take-control/) ist nur einen Klick entfernt, und durch das endgültige Löschen Ihres Kontos werden alle Ihre Daten von den Servern gelöscht.



**Dezentrale, sichere Speicherung**: Ihre verschlüsselten Daten werden bei 3 verschiedenen Anbietern in 3 verschiedenen Ländern repliziert, was eine optimale Verfügbarkeit garantiert und die Abhängigkeit von einem einzigen Cloud-Anbieter vermeidet.



Das Geschäftsmodell von Ente basiert auf dem kostenpflichtigen Dienst Ente Photos, der es uns ermöglicht, Ente Auth **kostenlos und ohne Einschränkungen** anzubieten, ohne Ihre Privatsphäre durch die Monetarisierung Ihrer Daten zu gefährden. Dieser Ansatz garantiert die Nachhaltigkeit des Dienstes, ohne auf Werbung oder den Weiterverkauf von persönlichen Daten angewiesen zu sein.



## Vergleich mit anderen Lösungen



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth ist eine der wenigen Lösungen, die alle Vorteile in sich vereint: Transparenz des Quellcodes, verschlüsseltes Cloud-Backup und plattformübergreifende Synchronisation.



## Empfohlene Anwendungsfälle



### Einzelne Benutzer



Ente Auth ist ideal für sicherheitsbewusste Personen, die systematisch 2FA aktivieren. Sie müssen sich keine Sorgen mehr machen, dass Sie Ihre Codes verlieren, wenn Sie das Telefon wechseln, oder dass Sie sich zwischen Komfort und Sicherheit entscheiden müssen.



### Familien- und geräteübergreifende Nutzung



Die App ist besonders nützlich, wenn Sie mehrere Geräte verwenden. Sie können Ihre Codes auf Smartphones und Tablets speichern oder bestimmte Familiencodes (Netflix, Familien-Cloud) synchron und sicher teilen.



### Professioneller Einsatz



Für Teams, die sensible Konten verwalten, erleichtert Ente Auth die Zusammenarbeit bei gleichzeitiger Wahrung der Sicherheit, dank seiner fortschrittlichen Freigabefunktionen, die in den Bereich "Organisation und Verwaltung" integriert sind.



## Bewährte Praktiken





- **Speichern Sie Ihre Notfallcodes**: Bewahren Sie die von den einzelnen Diensten bereitgestellten Wiederherstellungscodes nicht in Ihrem Telefon auf.





- **Verwenden Sie ein sicheres Master-Passwort**: Ihr Ente Auth Master-Passwort muss eindeutig und sicher sein, da es alle Ihre Codes schützt.





- **Aktivieren Sie den lokalen Schutz**: Konfigurieren Sie PIN oder Biometrie, um unbefugten physischen Zugriff zu verhindern.





- **Übertreiben Sie es nicht mit den Anpassungen**: Vermeiden Sie erweiterte Änderungen, die die Synchronisierung beeinträchtigen könnten.





- **Halten Sie die Anwendung auf dem neuesten Stand**: Updates beheben Sicherheitslücken und verbessern die Funktionalität.





- **Wiederherstellung testen**: Testen Sie gelegentlich, ob Sie Ihre Codes auf einem anderen Gerät wiederherstellen können.



## Schlussfolgerung



Ente Auth ist eine moderne, umfassende Lösung für die Zwei-Faktor-Authentifizierung. Durch die Kombination von Sicherheit, Transparenz und Benutzerfreundlichkeit erfüllt diese Open-Source-Anwendung die Bedürfnisse anspruchsvoller Nutzer, ohne auf Komfort zu verzichten.



Im Gegensatz zu proprietären Lösungen, die Sie in ein undurchsichtiges Ökosystem einbinden, gibt Ihnen Ente Auth die Kontrolle über Ihre Authentifizierungsdaten zurück und schützt Sie dank der verschlüsselten Backups vor versehentlichem Verlust.



Egal, ob Sie eine Einzelperson sind, die ihre persönlichen Konten schützen möchte, oder ein Team, das den Zugang für Unternehmen verwaltet, Ente Auth ist eine kluge Wahl, um Ihren Ansatz für digitale Sicherheit zu modernisieren, ohne die Privatsphäre zu gefährden.



## Ressourcen und Unterstützung



### Offizielle Dokumentation




- **Offizielle Website**: [ente.io/auth](https://ente.io/auth)
- **Hilfe-Center**: [help.ente.io/auth](https://help.ente.io/auth)
- **Technischer Blog**: [ente.io/blog](https://ente.io/blog)



### Quellcode und Transparenz




- **GitHub**: [github.com/ente-io/auth](https://github.com/ente-io/auth)
- **Kryptographie-Audit**: [ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)



### Gemeinschaft




- **Discord**: [discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- **Reddit**: [r/enteio](https://reddit.com/r/enteio)