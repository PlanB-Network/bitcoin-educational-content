---
name: BitBanana
description: Mobiler Manager für Ihren Lightning-Knoten
---

![cover](assets/cover.webp)



In diesem Tutorial lernen Sie, wie Sie BitBanana auf Android installieren und konfigurieren, um Ihren Lightning-Knoten über Ihr Smartphone zu steuern. Wir werden sehen, wie Sie die App mit Ihrer bestehenden Infrastruktur (Umbrel, RaspiBlitz, myNode oder einem LND/Core Lightning-Knoten) verbinden, Lightning-Zahlungen durchführen, Ihre Kanäle aus der Ferne verwalten, Ihre Routing-Einnahmen einsehen und Ihre Konfigurationen sichern. Außerdem erfahren Sie mehr über die besten Sicherheitspraktiken, um den Zugriff auf Ihren Knoten zu schützen, und wie es im Vergleich zu Zeus, einer beliebten Alternative, aussieht.



## Einführung von BitBanana



BitBanana ist eine quelloffene mobile Android-Anwendung, die Ihr Smartphone in ein komplettes Dashboard zur Fernsteuerung Ihres Lightning-Knotens verwandelt. Im Gegensatz zu Lightning-Wallets, die einen lokalen Knoten auf dem Telefon einbetten, verfolgt BitBanana eine 100%ige Fernsteuerungsphilosophie: Die App enthält kein satoshi und verbindet sich nur mit Ihrer bestehenden Infrastruktur.



Entwickelt von Michael Wünsch unter MIT-Lizenz, garantiert die Anwendung totale Transparenz ohne Sammlung persönlicher Daten und verifizierte, reproduzierbare Builds. BitBanana unterstützt von Haus aus LND und Core Lightning über Standard-URIs (`lndconnect://` und `clngrpc://`), was die Erstkonfiguration drastisch vereinfacht. Die Anwendung erkennt auch LndHub und Nostr Wallet Connect für Benutzer ohne eigenen Knoten, obwohl diese Modi nur mit eingeschränkter Funktionalität arbeiten.



Die Schnittstelle bietet vollen Zugriff auf alle wichtigen Funktionen Ihres Knotens: Senden und Empfangen von Zahlungen (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), Lightning-Kanalverwaltung (Öffnen, Schließen, Gebührenanpassung, Rebalancing), erweiterte Münzkontrolle und Wachturmverwaltung. BitBanana implementiert auch mehrere robuste Sicherheitsebenen: biometrische Sperre, Stealth-Modus, Notfall-PIN und native Tor-Unterstützung zur Anonymisierung von Verbindungen.



## Unterstützte Plattformen und Installation



### Einrichtung



BitBanana ist ausschließlich für Android 8.0 oder höher verfügbar. Die Anwendung gibt es nicht für iOS, und es ist auch keine Version geplant. Diese Einschränkung erklärt sich durch die Geschichte des Projekts: BitBanana ist der direkte Nachfolger von Zap Android, das ursprünglich von Michael Wünsch entwickelt wurde, der beschloss, seine Arbeit unter seiner eigenen Marke fortzusetzen. Zap war eine Familie von separaten Anwendungen (Zap Android, Zap iOS, Zap Desktop), die von verschiedenen Entwicklern mit separaten Codebasen entwickelt wurden. BitBanana verfolgt nur den Android-Zweig.



Darüber hinaus unterliegt das iOS-Ökosystem erheblichen regulatorischen und technischen Beschränkungen für Lightning-Anwendungen, die nicht der Sorgfaltspflicht unterliegen. Im Jahr 2023 lehnte Apple ein Zeus-Update wegen "Lizenzverstößen" ab, und im Jahr 2024 verließ Phoenix Wallet den US-amerikanischen App Store angesichts der regulatorischen Unsicherheiten in Bezug auf Lightning-Dienstanbieter. Diese Hindernisse erklären, warum viele Lightning-Entwickler Android bevorzugen, das eine offenere Politik für nicht verpfändete Anwendungen bietet.



Für Android sind drei Installationsmethoden verfügbar: Google Play Store (5000+ Installationen, automatische Updates), F-Droid (reproduzierbare Builds, Quellcode-Verifizierung) oder manuelle APK von GitHub.



![BitBanana](assets/fr/01.webp)



Die offizielle bitbanana.app-Website (links) rühmt sich mit "100% Selbstkontrolle mit NULL Datenerfassung". Der zentrale Bildschirm zeigt die drei Download-Optionen an: F-Droid (empfohlen), Google Play und APK. Der Bildschirm auf der rechten Seite zeigt die Benachrichtigungserlaubnis für Zahlungswarnungen.



Die Anwendung fordert Berechtigungen an: Netzwerk (Knotenverbindung), Kamera (QR-Codes), NFC (LNURL), Hintergrunddienste (Benachrichtigungen), Biometrie (Sicherheit) und WireGuard VPN. Keine Tracker, keine Datenerfassung. Aktivieren Sie ein Passwort oder eine biometrische Sperre, um den Zugang zu sichern.



## Erstmalige Konfiguration



### Anschließen an einen LND-Knoten



Um BitBanana mit Ihrem LND-Knoten (Umbrel, RaspiBlitz, myNode) zu verbinden, erhalten Sie eine "ndconnect"-URI oder einen QR-Code, der die Adresse, das TLS-Zertifikat und den Authentifizierungsmakaron enthält.



In diesem Tutorial verwenden wir einen LND-Knoten über Umbrella. Weitere Einzelheiten finden Sie in unserem speziellen Tutorial:



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



Rufen Sie in der Lightning Node-Anwendung das Menü oben rechts auf und wählen Sie "wallet verbinden".



![BitBanana](assets/fr/04.webp)



Wählen Sie **gRPC (Tor)**, um sich über Tor zu verbinden (empfohlen). Der QR-Code und die Details (Host .onion, Port 10009, Macaroon) werden angezeigt.



![BitBanana](assets/fr/02.webp)



Drücken Sie in BitBanana auf "CONNECT NODE", scannen Sie den QR-Code oder fügen Sie die URI ein. Autorisieren Sie den Zugriff auf die Kamera und überprüfen Sie die angezeigte .onion-Adresse, bevor Sie bestätigen.



**Core Lightning** Anschluss



Wenn Sie Core Lightning (CLN) anstelle von LND verwenden, bleibt der Prozess identisch, wobei der URI "clngrpc://" die gegenseitigen TLS-Zertifikate enthält. Core Lightning unterstützt nativ BOLT12 (Angebote) und ermöglicht wiederverwendbare Rechnungen und wiederkehrende Zahlungen, die in LND nicht verfügbar sind.



**Verbindung ohne eigenen Knoten (LNbits/hosted)**



Wenn Sie keinen Lightning-Knoten haben, kann sich BitBanana über LndHub (das von BlueWallet und LNbits verwendete Protokoll) oder Nostr Wallet Connect (NWC) mit gehosteten Diensten verbinden. Bitte beachten Sie: Diese Modi arbeiten im Verwahrungsmodus (der Dienst hostet Ihre Gelder) mit eingeschränkter Funktionalität. Sie können keine Kanäle verwalten oder Routing-Gebühren konfigurieren und können nur Lightning-Zahlungen senden und empfangen.



Weitere Einzelheiten zu LNbits oder Nostr Wallet Connect finden Sie in unseren verschiedenen Tutorials:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Täglicher Gebrauch



### Interface Haupt



Auf dem Startbildschirm wird Ihr Lightning-Kontostand angezeigt. Über das Menü oben links haben Sie Zugriff auf die folgenden Bereiche: Kanäle, Routing, Signieren/Bestätigen, Knoten, Kontakte, Einstellungen, Backup. Das Uhrensymbol (oben rechts) öffnet die Transaktionshistorie. Mit den Schaltflächen "Senden" und "Empfangen" am unteren Rand können Sie Ihre Satoshis senden und empfangen.



![BitBanana](assets/fr/05.webp)



### Zahlungen für Blitzschlag und on-chain



![BitBanana](assets/fr/10.webp)



**Senden Sie eine Zahlung:** Drücken Sie auf dem Startbildschirm die Schaltfläche "Senden". Der Zahlungsbildschirm (links) bietet Ihnen die Möglichkeit, eine Adresse oder Zahlungsdaten in das Feld "Address oder Zahlungsdaten" einzufügen, mit einem QR-Scanner oben rechts zum Scannen von Codes. Sie können auch einen in der Rubrik "Kontakte" gespeicherten Kontakt auswählen, um nicht jedes Mal scannen zu müssen.



BitBanana erkennt auf intelligente Weise alle Zahlungsformate: klassische Lightning-Rechnungen (Zeichenketten, die mit `lnbc` beginnen), Lightning Address (E-Mail-Format wie `utilisateur@domaine.com`), LNURL-Pay-Codes für dynamische Zahlungen, LNURL-Withdraw für Geldabhebungen und sogar Keysend-Zahlungen direkt an einen öffentlichen Lightning-Schlüssel ohne vorherige Rechnung. Die Anwendung führt die erforderlichen LNURL-Auflösungen automatisch im Hintergrund durch.



Sobald die Rechnung geladen wurde, zeigt BitBanana alle Details an: den genauen Betrag, die geschätzten Weiterleitungsgebühren, die Zahlungsbeschreibung (falls vom Empfänger angegeben) und das Ablaufdatum der Rechnung. Nach der Bestätigung wird die Zahlung über Ihre Lightning-Kanäle weitergeleitet. In den Transaktionsdetails können Sie dann den zurückgelegten Weg Schritt für Schritt und die tatsächlich gezahlten Gebühren einsehen.



**Zahlung empfangen:** Drücken Sie die Schaltfläche "Empfangen". Über einen Selektor (rechter Bildschirm) können Sie zwischen Lightning (sofortige Zahlung über Ihre Kanäle) und On-Chain wählen. Für eine Lightning-Rechnung geben Sie den gewünschten Betrag in Satoshis ein (oder belassen Sie es bei 0, um eine Rechnung ohne festen Betrag zu erstellen, die der Zahler ausfüllen muss), und fügen Sie eine optionale Beschreibung hinzu, die auf der Rechnung erscheinen soll. BitBanana erstellt sofort eine Lightning-Rechnung mit QR-Code zum Scannen. Sie können die Rechnung auch als Text kopieren und per E-Mail verschicken. Sobald die Zahlung eingegangen ist, erhalten Sie eine Push-Benachrichtigung und die Transaktion erscheint sofort in der Historie mit all ihren Details.



### Kanäle und Routing



![BitBanana](assets/fr/06.webp)



Der Abschnitt "Kanäle" zeigt Ihre Sende-/Empfangsmöglichkeiten an und listet Ihre Kanäle mit eindeutigen Avataren auf. Bei jedem Kanal wird die Liquidität zwischen lokalem und entferntem Guthaben aufgeteilt. Tippen Sie auf einen Kanal, um alle Details und Aktionen (Schließen, Ändern von Weiterleitungsgebühren) anzuzeigen. Die drei Punkte oben rechts ermöglichen den Zugriff auf die Option "Rebalance", um die Liquidität Ihrer Kanäle neu zu verteilen. Die Schaltfläche "+" öffnet einen neuen Kanal.



Der Abschnitt "Routing" (zentraler Bildschirm) zeigt die Weiterleitungserträge nach Zeitraum (1D, 1W, 1M, 3M, 6M, 1Y) mit einer detaillierten Weiterleitungshistorie an, um Ihre Strategie zu optimieren.



Signieren/Verifizieren (rechter Bildschirm) ermöglicht es Ihnen, Nachrichten kryptografisch zu signieren/verifizieren, um die Kontrolle über den Knoten nachzuweisen.



### Multi-Knoten und Parameter



![BitBanana](assets/fr/07.webp)



**Knoten verwalten**: listet Ihre Knoten auf, mit Schaltflächen zum manuellen Hinzufügen, Scannen von QR oder Umschalten zwischen Knoten. Insbesondere können Sie verschiedene Arten von Verbindungen zum selben Knoten einrichten: LAN, VPN oder Tor.



**Kontakte verwalten**: speichert Ihre Lightning-Kontakte für schnelle Zahlungen.



**Einstellungen**: Anpassen von Währung, Sprache und Avataren. Bereich Sicherheit & Datenschutz: App-Sperre (PIN/Biometrie), Guthaben verbergen (Stealth-Modus), Tor (IP-Anonymisierung). Konfiguration von Preisorakeln, Block-Explorern, benutzerdefinierten Gebührenschätzern.



## Vorteile und Grenzen



**Highlights:**




- Absolute Mobilität: Steuern Sie Ihren Lightning-Knoten von überall aus
- Volle Funktionalität: Zahlungen (LNURL, Lightning Address, BOLT 12), Kanalmanagement, Münzkontrolle, Wachtürme, Multi-Knoten
- Sicherheit: PIN/Biometrie, Stealth-Modus, Notfall-PIN, natives Tor, Screenshot-Sperre
- Kostenlos, quelloffen (MIT), keine Provisionen, keine Datenerhebung



**Einschränkungen:**




- Erfordert einen aktiven Lightning-Knoten (oder LNbits im Verwahrungsmodus)
- Keine iOS-Version geplant
- Die Sicherung des Zugangs zum Telefon ist von entscheidender Bedeutung (macaroon admin = vollständiger Zugang zum Knoten)



## Bewährte Praktiken



**Sicherheit:**




- PIN/Biometrie-Sperre aktivieren (verhindert unbefugten Zugriff auf den Knoten)
- Einrichten einer Notfall-PIN (löscht sensible Daten im Notfall)
- Geben Sie niemals Ihre Anmelde-URI oder Ihren Makaron weiter
- Stealth-Modus in feindlichen Umgebungen



**Anmeldung:**




- VPN-Mesh (Tailscale, ZeroTier): bester Kompromiss zwischen Geschwindigkeit und Sicherheit
- Tor: maximale Vertraulichkeit, höhere Latenzzeit
- Clearnet: vermeiden, sofern nicht erforderlich (IP-Exposition, offene Ports)



### Sicherung und Wiederherstellung



Schließlich gibt es noch das Menü "Backup", mit dem Sie Ihre Konfigurationen für die Migration oder Neuinstallation von Telefonen speichern können.



![BitBanana](assets/fr/08.webp)



**Wichtig:** Das Backup enthält KEINE seed- oder Channel-Backups (die auf dem Knoten durchgeführt werden müssen). Sie enthält: Knotenkonfigurationen (Adressen, Zertifikate, Makronen), Etiketten, Kontakte, Parameter. Mit der Schaltfläche Wiederherstellen können Sie eine vorhandene Sicherung importieren. Vor dem Speichern ist eine Bestätigung erforderlich.



![BitBanana](assets/fr/09.webp)



Geben Sie ein Verschlüsselungspasswort ein (rechter Bildschirm). Das System öffnet die Dateiauswahl (linker Bildschirm) zum Speichern von `BitBananaBackup_2025-XX-XX.dat`. Bestätigung "Backup erstellt".



**Sicherheit:** Speichern Sie das Backup verschlüsselt (persönliche Cloud, USB, NAS). Geben Sie niemals Dateien oder Passwörter weiter. Testen Sie die Wiederherstellung regelmäßig. Das Backup stellt Verbindungen wieder her, nicht Gelder.



## BitBanana vs. Zeus: Was ist der Unterschied?



Wenn Sie sich mit mobilen Apps für die Verwaltung eines Lightning-Knotens befassen, werden Sie wahrscheinlich auf Zeus stoßen, eine beliebte Alternative zu BitBanana. Im Gegensatz zu BitBanana, das sich ausschließlich auf die Fernsteuerung eines bestehenden Knotens konzentriert, verfolgt Zeus einen umfassenderen Ansatz und bietet zwei Betriebsmodi: einen direkt in die Anwendung eingebetteten Lightning-Knoten (eingebetteter Modus mit integriertem LND) und die Fernverbindung zu einem externen Knoten, genau wie BitBanana.



Diese Doppelfunktionalität macht Zeus besonders attraktiv für Anfänger, die ohne vorherige Infrastruktur mit Lightning experimentieren möchten. Der eingebettete Modus ermöglicht die sofortige Inbetriebnahme mit einem vollständigen mobilen Knoten, während fortgeschrittene Benutzer auf eine Fernverbindung umschalten können, sobald ihr persönlicher Knoten konfiguriert ist. Zeus unterstützt auch LND und Core Lightning für die Fernverbindung, wie z. B. BitBanana.



Ein weiterer großer Vorteil von Zeus ist seine plattformübergreifende Verfügbarkeit (iOS und Android), während BitBanana ausschließlich Android-basiert bleibt. Zeus beinhaltet auch die LSP-Infrastruktur von Olympus, um den Empfang von Lightning-Zahlungen über Just-in-Time-Kanäle zu erleichtern, ein Point-of-Sale-System für Händler und eine integrierte Swap-Funktionalität zur Verwaltung der Liquidität.



BitBanana behält jedoch seine spezifischen Stärken bei: eine einfachere, schlankere Schnittstelle, eine bessere Benutzererfahrung (UX) dank der ausschließlichen Konzentration auf die Fernsteuerung und einen pädagogischen Ansatz mit kontextbezogenen Erklärungen. Zeus bietet mehr Funktionalität, allerdings auf Kosten einer komplexeren Schnittstelle. Die Anwendung eignet sich vor allem für Nutzer, die einen Knoten ausschließlich aus der Ferne steuern wollen, ohne dass sie ihn betreuen müssen.



Um mehr über Zeus zu erfahren, schauen Sie sich die folgenden Tutorials an:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Schlussfolgerung



BitBanana verwandelt Ihr Android-Smartphone in ein komplettes Lightning-Dashboard, das den Betreibern von Knotenpunkten eine noch nie dagewesene Mobilität bietet. Die Anwendung deckt alle Funktionalitäten ab: Zahlungen (alle Formate), Kanalmanagement, Münzkontrolle, Wachtürme, Multi-Knoten, mit erweiterter Sicherheit (PIN/Biometrie, Tor, Notfall-PIN).



Völlig souverän, BitBanana sammelt keine Daten und kompromittiert weder die Vertraulichkeit noch die Kontrolle über Ihr Geld. Offener Quellcode (MIT) garantiert Transparenz.



## Ressourcen



### Offizielle Dokumentation




- [BitBanana-Website](https://bitbanana.app)
- [Vollständige Dokumentation](https://docs.bitbanana.app)
- [GitHub-Quellcode](https://github.com/michaelWuensch/BitBanana)



### Einrichtung




- [Google Play Store](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)