---
name: Orion Browser
description: Wie verwendet man Orion Browser zum Schutz der Privatsphäre auf Mac und iPhone?
---

![cover](assets/cover.webp)



## Einführung



In einem Kontext, in dem die meisten Browser massiv unsere persönlichen Daten sammeln, wird die Wahl eines datenschutzfreundlichen Browsers entscheidend. Chrome dominiert mit 65 % des Weltmarkts, aber sein Geschäftsmodell basiert auf der Ausbeutung Ihrer Browsing-Daten. Safari ist zwar in das Apple-Ökosystem integriert, verfügt aber nicht über fortschrittliche Schutzfunktionen und unterstützt keine flexiblen Erweiterungen von Drittanbietern.



![Répartition du marché des navigateurs](assets/fr/01.webp)


*Aufschlüsselung des Webbrowser-Marktes: Chrome dominiert mit über 65 % Marktanteil, gefolgt von Safari, Edge und Firefox*



**Orion Browser** präsentiert sich als innovative Alternative für Apple-Nutzer. Dieser von Kagi entwickelte Browser kombiniert die Geschwindigkeit der WebKit-Engine mit einer Null-Telemetrie-Philosophie. Im Gegensatz zu seinen Mitbewerbern sendet Orion keine Daten an entfernte Server und blockiert von Haus aus 99,9 % der Werbung und Tracker, einschließlich YouTube.



Seine einzigartige Eigenschaft? Orion ist der **einzige WebKit**-Browser, der Chrome- **und** Firefox-Erweiterungen nativ installiert und damit das Beste aus beiden Welten bietet. Diese Kompatibilität, kombiniert mit einem 2 bis 3 Mal geringeren Speicherverbrauch als bei anderen Browsern und einer nahtlosen Integration in das Apple-Ökosystem (iCloud, Schlüsselbund), macht ihn zur idealen Wahl für datenschutzbewusste Mac- und iPhone-Nutzer.



## Warum sollten Sie sich für Orion Browser entscheiden?



### Wichtigste Vorteile



**Maximaler Schutz direkt nach dem Auspacken**: Orion blockiert standardmäßig 99,9 % der Werbung (einschließlich YouTube) und alle Tracker von Erstanbietern und Dritten. Seine Technologie kombiniert die intelligente Tracking-Prävention von WebKit mit EasyPrivacy-Listen für maximale Effizienz. Einzigartige Funktion: Orion blockiert Fingerprinting-Skripte **bevor sie ausgeführt werden**, was Tracking buchstäblich unmöglich macht - ein radikalerer Ansatz als bei anderen Browsern, die nur versuchen, Daten zu "maskieren".



**Null überprüfbare Telemetrie**: Orion verfolgt einen radikalen Ansatz in Bezug auf den Datenschutz und verzichtet von vornherein auf Telemetrie. Im Gegensatz zu anderen Browsern, die beim Start Hunderte von Netzwerkanfragen stellen (IP-Exponent, Browser-Fingerabdruck, persönliche Informationen), ruft Orion niemals "nach Hause". Dieser grundlegende Unterschied schließt das Risiko eines unbeabsichtigten Datenverlusts vollständig aus.



**Ausgezeichnete Leistung**: Basierend auf einer optimierten Version von WebKit ist Orion auf dem Mac genauso schnell wie Safari oder übertrifft es sogar. In Speedometer 2.0/2.1-Tests belegt Orion auf Apple Silicon Prozessoren durchweg den ersten Platz. Native Werbeblocker beschleunigen den Seitenaufbau zusätzlich um 20 bis 40 %.



**Universelle Unterstützung von Erweiterungen**: Eine wichtige Neuerung: Orion ermöglicht die Installation von Erweiterungen aus dem Chrome Web Store **und** Mozilla Add-ons. Die Unterstützung von WebExtensions ist derzeit experimentell, mit dem Ziel einer 100%igen Kompatibilität bei der Beta-Version. Sie können viele beliebte Erweiterungen wie uBlock Origin, Bitwarden, sogar auf dem iPhone verwenden - eine Weltneuheit auf iOS, obwohl einige möglicherweise nicht perfekt funktionieren.



### Zu beachtende Beschränkungen





- **Begrenzte Verfügbarkeit**: Derzeit reserviert für macOS und iOS/iPadOS. Eine Linux-Version erreicht Entwicklungsmeilensteine (Meilenstein 2 im Jahr 2025), aber es ist kein öffentlicher Build verfügbar. Windows und Android befinden sich mangels Ressourcen nicht in der Entwicklung.
- **Geschlossener Quellcode**: Obwohl einige Komponenten quelloffen sind, bleibt Orion überwiegend proprietär, ein Punkt, der in der Datenschutzgemeinschaft diskutiert wird.
- **Experimentelle Erweiterungen**: Die Unterstützung von Erweiterungen befindet sich noch in der Beta-Phase, mit häufigen Inkompatibilitäten. Erweiterungen können die Leistung beeinträchtigen, und einige funktionieren überhaupt nicht.
- **WebKit-Sicherheit**: Im Gegensatz zu Chromium bietet WebKit keine so robuste standortbezogene Prozessisolierung, was in bestimmten Szenarien zu Sicherheitsrisiken führen kann.
- **Blockierungstests**: Orion schneidet in Online-Werbetests absichtlich schlecht ab (26-35%), da Kagi diese Tests für "grundsätzlich fehlerhaft" hält. Die tatsächliche Wirksamkeit im täglichen Gebrauch ist weitaus besser.



## Orion-Browser-Installation



### Unter macOS



![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)


*Die Kagi-Homepage präsentiert Orion Browser als "werbefreien Browser mit umfassendem Schutz der Privatsphäre und universeller Unterstützung von Erweiterungen "*





- Weiter zu [kagi.com/orion](https://kagi.com/orion/)
- Klicken Sie auf "**Orion für macOS herunterladen**"



![Page de téléchargement d'Orion Browser](assets/fr/03.webp)


*Die Orion Browser Download-Seite zeigt die Verfügbarkeit für macOS und iOS, mit Links zum App Store*





- Öffnen Sie die heruntergeladene `.dmg`-Datei
- Ziehen Sie die Orion-Anwendung in den Anwendungsordner
- Beim ersten Start fordert macOS Sie auf, das Öffnen zu bestätigen



**Alternative Homebrew**:


```bash
brew install --cask orion
```



### Auf iPhone/iPad





- Öffnen Sie den **App Store**
- Suche nach "**Orion Browser by Kagi**"
- Installieren Sie die kostenlose App (kompatibel mit iOS 15+)



### Erstmalige Konfiguration



Beim ersten Start führt Orion Sie durch mehrere Schritte:



**1. Willkommensbildschirm**


![Écran de bienvenue d'Orion](assets/fr/04.webp)


*Der Willkommensbildschirm von Orion Browser hebt die wichtigsten Funktionen hervor: schnelleres Surfen, keine Telemetrie, Werbeblocker und Unterstützung von Erweiterungen*



**2. Interface**-Anpassung


![Options de personnalisation](assets/fr/05.webp)


*Über den Anpassungsbildschirm können Sie das Aussehen der Registerkarten und des Interface nach Ihren Wünschen konfigurieren*





- **Datenimport**: Übertragen Sie ganz einfach Favoriten und Passwörter aus Safari, Chrome oder Firefox
- **iCloud-Synchronisierung**: Aktivieren Sie diese Funktion, um Ihre Favoriten und Tabs auf allen Ihren Apple-Geräten zu finden



**3. Installation auf mobilen Geräten**


![Installation sur iOS](assets/fr/06.webp)


*Installationsbildschirm auf iOS mit dem QR-Code zum schnellen Herunterladen von Orion Browser aus dem App Store*



**4. Interface - Willkommen und wichtige Werkzeuge**



![Page d'accueil Orion](assets/fr/07.webp)


*Orion Browser Interface-Startseite: Der Pfeil zeigt die drei wichtigsten Werkzeuge an, die direkt über die Address-Leiste* zugänglich sind



Sobald die Konfiguration abgeschlossen ist, finden Sie das optimierte Interface von Orion mit seinen **drei wesentlichen Werkzeugen** (durch den Pfeil gekennzeichnet):





- **Schutzschild 🛡️**: Zeigt den Datenschutzbericht mit der Anzahl der blockierten Elemente auf der aktuellen Seite an
- **Pinsel 🖌️**: Anpassen der Seitenanzeige (Thema, Schriftart, Entfernen störender Elemente)
- **Gang ⚙️**: Konfigurieren Sie website-spezifische Parameter (Berechtigungen, Sperren usw.)



Diese Tools sind immer verfügbar und ermöglichen es Ihnen, Ihr Surferlebnis auf jeder einzelnen Website zu kontrollieren.



**Wichtig**: Orion ist kostenlos und erfordert keine Registrierung oder Erstellung eines Kontos, um zu funktionieren.



![Orion+ dans les préférences](assets/fr/08.webp)


*Orion+ Abonnement-Bildschirm in den Einstellungen, der ein optionales Abonnement zur Unterstützung der Entwicklung anbietet*



**Orion+ (optional)**: Um die Projektentwicklung zu unterstützen, bietet Kagi Orion+ ($5/Monat, $50/Jahr oder $150 auf Lebenszeit). Dieses freiwillige Abonnement ermöglicht:




- Direkte Kommunikation mit dem Entwicklungsteam
- Beeinflussen Sie die Entwicklung des Browsers nach Ihren Bedürfnissen
- Zugriff auf Nightly-Versionen mit den neuesten experimentellen Funktionen
- Profitieren Sie von der neuesten WebKit-Engine
- Erhalten Sie ein unverwechselbares Abzeichen im Feedback-Forum



Orion+ garantiert die Unabhängigkeit des Projekts: "Ihr finanzieller Beitrag hilft uns, unabhängig zu bleiben und unser Versprechen zu halten, der beste Browser für unsere Nutzer zu werden". Es ist dieses Modell der Nutzerfinanzierung, das Orion werbe- und telemetriefrei hält.



## Konfiguration für maximale Vertraulichkeit



### Wesentliche Parameter



Rufen Sie die Einstellungen über **Orion → Einstellungen** (oder ⌘,) auf:



**1. Suche - Private Suchmaschine**



![Configuration du moteur de recherche](assets/fr/09.webp)


*Standardkonfiguration der Suchmaschine: DuckDuckGo ist für maximalen Datenschutz ausgewählt*





- **Standard-Engine**: Wählen Sie **DuckDuckGo**, **Startpage** oder **Kagi** für optimalen Datenschutz (vermeiden Sie Google/Bing)
- **Suchvorschläge**: Deaktivieren Sie sie, um zu verhindern, dass Tastatureingaben an die Server der Suchmaschine gelangen



**2. Privatsphäre - Allgemein** Schutz



![Content Blocker dans les préférences](assets/fr/12.webp)


*Die Orion-Datenschutzeinstellungen zeigen den Content Blocker mit 119.156 aktiven Regeln, Optionen zum Entfernen von Trackern und einen benutzerdefinierten Benutzeragenten*



**Inhaltsblocker standardmäßig aktiv**:




- **EasyList**: 119k+ Werbeblocker-Regeln
- **EasyPrivacy**: Schutz vor Tracking
- **Filter-Listen verwalten**: Zusätzliche Listen hinzufügen (Hagezi empfohlen)



**Datenschutzoptionen**:




- Entfernen Sie Tracker aus URLs: **"For Private Browsing only"** bereinigt kopierte Links
- Teilen Sie Unfallberichte: **"Nach Anfrage" respektiert Ihr Einverständnis**
- **Benutzerdefinierter Agent**: Kann geändert werden, um bestimmte Blockierungen zu umgehen



![YouTube avec Privacy Report](assets/fr/10.webp)


*Beispiel für YouTube mit Orion: keine Werbung sichtbar und Datenschutzbericht zeigt die vielen Elements blockiert*



**3. Website-Einstellungen - Steuerung nach Standort**



![Website Settings pour YouTube](assets/fr/11.webp)


*Website-Einstellungen für YouTube mit Kompatibilitätsoptionen, Inhaltssperrung und standortspezifischen Berechtigungen*



**Schnellzugriff**: Klicken Sie auf das Zahnrad ⚙️ in der Address-Leiste, um es einzustellen:




- **Kompatibilitätsmodus**: Behebt Anzeigeprobleme durch Aussetzen von Erweiterungen
- **Inhaltsblocker**: Deaktivieren Sie die Blockierung für eine bestimmte Website, falls erforderlich
- **JavaScript/Cookies**: Granulare Kontrolle nach Standort
- **Berechtigungen**: Kamera, Mikrofon, Standort individuell konfigurierbar



**4. Erweiterte benutzerdefinierte Filter** (siehe unten)



**Eigene Filter erstellen** (Datenschutz → Filterlisten verwalten → Eigene Filter):



**Vereinfachte Syntax** (kompatibel mit Adblock Plus):




- `reddit.com##.promotedlink`: Blendet gesponserte Reddit-Beiträge aus
- ||ads.beispiel.com^`: Blockiert eine Werbedomain vollständig
- @@||site-utile.com^`: Erzeugt eine Ausnahme für eine Website



**Tipp: Auf [FilterLists.com](https://filterlists.com) finden Sie Tausende von gebrauchsfertigen Speziallisten.**



### Empfohlene Erweiterungen



Orion unterstützt von Haus aus Erweiterungen für Chrome und Firefox. Installieren Sie sie direkt aus den offiziellen Stores:



**Essentials**:




- **uBlock Origin**: Erweitert den nativen Blocker um granulare Kontrolle
- **Bitwarden**: Open-Source-Passwort-Manager
- **ClearURLs**: Löscht URL-Tracking-Parameter



**Optional**:




- **LocalCDN**: Serviert gemeinsam genutzte Bibliotheken lokal
- **Cookie AutoLöschen**: Automatisches Löschen von Cookies nach dem Schließen von Tabs
- **NoScript**: Vollständige Kontrolle über die Ausführung von JavaScript (fortgeschrittene Benutzer)



Zur Installation einer:




- Besuchen Sie [chrome.google.com/webstore](https://chrome.google.com/webstore) oder [addons.mozilla.org](https://addons.mozilla.org)
- Klicken Sie auf "Zu Chrome/Firefox hinzufügen"
- Orion wird die Erweiterung automatisch abfangen und installieren



**Vorsicht**: Da die Unterstützung von Erweiterungen noch experimentell ist, können viele Erweiterungen nicht richtig funktionieren oder die Leistung beeinträchtigen. Sollte ein Problem auftreten (Website funktioniert nicht mehr, Langsamkeit), deaktivieren Sie die Erweiterungen eine nach der anderen, um die Ursache zu ermitteln.



## Täglicher Gebrauch



### Interface und einzigartige Merkmale




![Outil de personnalisation pinceau](assets/fr/13.webp)


*Orion-Pinselmenü zum Anpassen der Anzeige: Schriftgröße, Thema (hell/dunkel), Deaktivierung von klebrigen Überschriften und Entfernen von störenden Elements*



**Pinselwerkzeug: Erweiterte Anpassung**



Das **Pinsel**-Tool von Orion ist eine einzigartige Funktion, mit der Sie die Anzeige jeder Website individuell gestalten können:



**Themenoptionen**:




- Umschalten zwischen hellen und dunklen Themen für jede Website
- Automatische Anpassung an Ihre Systempräferenzen



**Typografische Kontrolle**:




- **Schriftgröße**: Lesbarkeit mit den Schaltflächen A- und A+ einstellen
- **Schriftart**: Schriftfamilie ändern (Standard oder benutzerdefiniert)



**Interface Reinigung**:




- **Klebrige Kopfzeilen deaktivieren**: Entfernt Kopfzeilen, die beim Scrollen am oberen Rand hängen bleiben
- **Elements** löschen: Lästige Elements (Werbung, Pop-ups, Cookie-Banner) dauerhaft entfernen
  - Klicken Sie auf "+ Löschen" und wählen Sie das auszublendende Element aus
  - Sehr nützlich für Websites mit permanenter Werbung oder visuellem Tracking Elements



**Persistenz**: Alle diese Einstellungen werden pro Domain gespeichert und bei Ihrem nächsten Besuch automatisch wieder angewendet.



**Erweiterte Registerkartenverwaltung**:




- **Vertikale Registerkarten**: Aktivieren über die Menüleiste (Funktion "Tabs on the Side")
- **Kompakte Registerkarten**: In Voreinstellungen → Registerkarten → Layout "Kompakt", um Platz zu sparen
- **Registerkartengruppen**: Organisieren Sie Ihre Sitzungen nach Thema
- **Mehrere Profile**: Erstellen Sie über die Menüleiste (Funktion "Profile") separate Identitäten mit vollständig isolierten Daten



**Low Power Mode**: Dieser vom iPhone inspirierte Modus unterbricht inaktive Tabs automatisch nach 5 Minuten und kann den Energieverbrauch um bis zu 90 % senken. Aktivieren Sie ihn über die Menüleiste von Orion auf dem Mac oder in den Einstellungen auf iOS.



**Eingebaute Werkzeuge** (Menü Bearbeiten und andere):




- **Text auf Seite bearbeiten**: Vorübergehende Änderung eines beliebigen Textes (Menü Bearbeiten)
- **Kopieren und Einfügen zulassen**: Umgeht die Kopierbeschränkungen (Menü Bearbeiten)
- **Sauberen Link kopieren**: Rechtsklick auf einen Link, um Tracking-Parameter zu entfernen
- **Focus Mode**: ablenkungsfreie Navigation über den gesamten Bildschirm
- **Bild-im-Bild**: Videos in einem schwebenden Fenster ansehen
- **Im Internet-Archiv öffnen**: Direkter Zugang zu archivierten Versionen
- **Datenschutzbericht**: Klicken Sie auf das Schild 🛡️, um die gesperrten Elemente pro Seite anzuzeigen



### Verwaltung des privaten Browsing



Die private Navigation von Orion (⌘⇧N) bietet:




- Vollständige Isolierung von Cookies und Sitzungen
- Automatische Löschung beim Schließen
- Verlauf und Cache-Deaktivierung
- Verbesserter Schutz gegen Fingerabdrücke



**Tipp**: Für eine erweiterte Abschottung erstellen Sie **getrennte Profile** über die Menüleiste (Funktion Profile). Jedes Profil erscheint als separate App im Dock, mit eigenen Einstellungen, Erweiterungen und Daten, die vollständig isoliert sind.



### Leistungsoptimierung und Datenschutz



Um Orion schnell und privat zu halten:




- **Erweiterungen**: Auf das absolute Minimum beschränken (kann die Leistung verringern)
- **Energiesparmodus**: Aktivieren Sie diesen Modus für lange Sitzungen (90% Einsparung möglich)
- **Datenschutzbericht**: Klicken Sie auf das Schild 🛡️, um Blockierungen in Echtzeit zu sehen
- **Visuelle Anpassung**: Verwenden Sie den 🖌️ Pinsel, um die Anzeige anzupassen und ablenkende Elemente zu entfernen
- **Sauberen Link kopieren**: Rechtsklick zum Kopieren von Links ohne Tracker
- **Getrennte Profile**: Verwenden Sie spezielle Profile, um Ihre Aktivitäten aufzuteilen
- **Website-Einstellungen**: Klicken Sie auf das Zahnrad ⚙️, um die Berechtigungen je nach Website anzupassen
- **Regelmäßige Reinigung**: Cache über Orion löschen → Browsing-Daten löschen



## Vergleich mit Alternativen



| Critère | Orion | Safari | Chrome | Firefox | Brave |
|---------|-------|--------|---------|----------|--------|
| **Télémétrie** | Aucune | Minimale | Extensive | Modérée | Minimale |
| **Bloqueur natif** | 99,9% efficace | Basique | Absent | Partiel | Complet |
| **Extensions** | Chrome + Firefox | Limitées | Chrome uniquement | Firefox uniquement | Chrome uniquement |
| **Performance Mac** | Excellente | Excellente | Bonne | Moyenne | Bonne |
| **Consommation RAM** | Très faible | Faible | Élevée | Moyenne | Moyenne |
| **Open Source** | Partiel | Partiel (WebKit) | Partiel | Complet | Complet |
| **Plateformes** | Mac/iOS | Mac/iOS | Toutes | Toutes | Toutes |

**Vergleich zu Safari**: Orion bietet mit seinem fortschrittlichen Blocker und der Unterstützung von Erweiterungen einen hervorragenden Schutz, während die WebKit-Leistung erhalten bleibt.



**Versus Chrome**: unübertroffener Datenschutz ohne Kompromisse bei der Kompatibilität, dank der Unterstützung von Chrome-Erweiterungen.



**Vergleich zu Firefox**: Schneller auf dem Mac, Interface intuitiver, aber weniger granulare Kontrolle und nicht Open-Source.



**Vergleich zu Brave**: Ähnliche Philosophie, aber Orion vermeidet Krypto/BAT-Kontroversen und bietet eine bessere Apple-Integration.



## Empfohlene Anwendungsfälle



**Ideal für**:




- Apple-Nutzer suchen mehr Privatsphäre als Safari
- Personen, die alle Anzeigen (einschließlich YouTube) ohne Erweiterungen blockieren möchten
- Entwickler, die WebKit-Entwicklungswerkzeuge mit integriertem Schutz der Privatsphäre benötigen
- IPhone-Nutzer wollen Desktop-Erweiterungen auf dem Handy (einzigartige Innovation)
- Fachleute, die ihre Tätigkeiten aufteilen müssen (mehrere Profile)
- Mobile Nutzer, die ein besseres Akkumanagement wünschen (Low Power Mode)



**Vermeiden, wenn**:




- Sie verwenden hauptsächlich Windows/Linux (keine Version verfügbar)
- Vollständig offene Quellen sind für Ihr Bedrohungsmodell unerlässlich
- Sie sind von bestimmten Erweiterungen abhängig, die möglicherweise nicht funktionieren
- Sie benötigen eine plattformübergreifende Synchronisierung über das Apple-Ökosystem hinaus
- Sie bevorzugen eine bewährte, stabile Lösung (permanenter Betastatus seit 2021)



## Aufmerksamkeit und Sicherheit



### Einzigartige Sicherheitsmerkmale



**Revolutionärer Anti-Fingerprinting-Schutz**: Orion ist der einzige Browser, der die Ausführung von Fingerprinting-Skripten vollständig blockiert, bevor diese Ihr System scannen können. Dieser Ansatz "kein laufendes Skript = kein Fingerprinting möglich" übertrifft die traditionellen Maskierungsmethoden anderer Browser.



**Transparente Whitelist**: Orion unterhält eine kleine öffentliche Liste von Websites (browserbench.org, wizzair.com), auf denen die Sperrung automatisch aufgehoben wird, um Störungen zu vermeiden. Diese Transparenz ermöglicht es den Benutzern, genau zu verstehen, wann und warum die Blockierung aufgehoben wird.



**Ungeprüfte Erweiterungen**: Die Unterstützung von Chrome/Firefox-Erweiterungen birgt zusätzliche Risiken, da diese Erweiterungen nicht für WebKit entwickelt wurden und nicht speziell für diese Umgebung geprüft werden.



### Wartung und Aktualisierung





- **Automatische Updates**: Orion aktualisiert sich unter macOS automatisch über Sparkle
- **Verfolgung von Schwachstellen**: Regelmäßige Überprüfung der Versionshinweise auf Sicherheitspatches
- **Fehler melden**: Verwenden Sie [orionfeedback.org](https://orionfeedback.org), um Probleme zu melden




## Schlussfolgerung



Orion Browser stellt einen bedeutenden Schritt nach vorne für den Datenschutz unter macOS und iOS dar. Sein Null-Telemetrie-Ansatz, kombiniert mit einem ultra-effizienten nativen Blocker und einer einzigartigen Unterstützung für universelle Erweiterungen, macht ihn zu einer hervorragenden Wahl für datenschutzbewusste Apple-Nutzer.



**Wichtig**: Orion befindet sich seit 2021 in der permanenten Beta-Phase, mit Einschränkungen bei der Kompatibilität von Erweiterungen und inhärenten WebKit-Risiken. Bewerten Sie diese Kompromisse je nach Ihrem Bedrohungsmodell.



Für den täglichen Gebrauch auf einem Mac oder iPhone ist es wahrscheinlich der beste Kompromiss zwischen Vertraulichkeit, Leistung und Benutzerfreundlichkeit, den das Apple-Ökosystem zu bieten hat, vorausgesetzt, man akzeptiert seine Einschränkungen.



Denken Sie daran: Der Schutz Ihrer Privatsphäre hängt nicht nur von Ihrem Browser ab. Kombinieren Sie Orion mit bewährten Praktiken (starke Passwörter, 2FA, VPN, falls erforderlich) für optimale Online-Sicherheit.



## Ressourcen und Unterstützung



### Offizielle Dokumentation




- **Offizielle Website**: [kagi.com/orion](https://kagi.com/orion/)
- **Vollständige FAQ**: [browser.kagi.com/faq](https://browser.kagi.com/faq)
- **Gemeinschaftsforum**: [community.kagi.com](https://community.kagi.com)
- **Fehlerverfolgung**: [orionfeedback.org](https://orionfeedback.org)
- **GitHub Orion**: [github.com/OrionBrowser](https://github.com/OrionBrowser) - Open-Source-Komponenten
- **Blog Kagi**: [blog.kagi.com](https://blog.kagi.com) - Nachrichten und Aktualisierungen



### Empfohlene Überprüfungstests



Testen Sie nach der Konfiguration Ihre Einrichtung:




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/) - Fingerabdrucktest
- [DNS Leak Test](https://www.dnsleaktest.com/) - Überprüfung auf DNS-Lecks
- [BrowserLeaks](https://browserleaks.com/) - Vollständige Suite von Datenschutztests



### Alternativen zu Plan ₿ Network


Für maximalen Schutz sollten Sie unsere anderen Leitfäden konsultieren:




- [Firefox gehärtet](https://planb.network/tutorials/computer-security/communication/firefox-11814cec-3415-4ed9-a06e-f6fda5c9510f) - Erweiterte Multiplattform-Konfiguration
- [Tor Browser](https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb) - Vollständige Anonymität im Netz
- [Mullvad Browser](https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e) - Maximaler Schutz durch Fingerabdrücke



Wenn Sie mehr über die Geschichte und die Funktionsweise von Browsern sowie über die wichtigsten digitalen Objekte in Ihrem täglichen Leben erfahren möchten, lade ich Sie ein, unseren neuen kostenlosen Schulungskurs SCU 202 zu entdecken, der auf Plan ₿ Network verfügbar ist:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1