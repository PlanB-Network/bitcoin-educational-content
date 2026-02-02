---
name: Silentium
description: Progressives Web wallet mit Unterstützung von Silent Payments (BIP-352)
---

![cover](assets/cover.webp)



Die Wiederverwendung von Bitcoin-Adressen ist eine der direktesten Bedrohungen für die Vertraulichkeit der Nutzer. Wenn ein Empfänger eine einzige Adresse verwendet, um mehrere Zahlungen zu erhalten, kann jeder Beobachter alle damit verbundenen Transaktionen zurückverfolgen und seine finanzielle Geschichte rekonstruieren. Dieses Problem betrifft vor allem Urheber von Inhalten, Wohltätigkeitsorganisationen oder Aktivisten, die eine Spendenadresse öffentlich anzeigen möchten, ohne ihre Privatsphäre zu gefährden.



Silentium reagiert auf dieses Problem mit einer eleganten Lösung, die direkt über Ihren Browser zugänglich ist. Diese quelloffene progressive Webanwendung (PWA), die im Mai 2024 von Louis Singer ins Leben gerufen wurde, implementiert Silent Payments (BIP-352): eine wiederverwendbare statische Adresse, bei der jede Zahlung auf einer separaten Blockchain-Adresse landet, ohne vorherige Interaktion oder beobachtbare Verbindung zwischen Transaktionen.



**Wichtige Warnung**: Silentium ist ein experimentelles Projekt, das als *Konzeptnachweis* für die leichten Geldbörsen von Silent Payments dient. Es sollte nicht als tägliches wallet oder zum Speichern größerer Beträge verwendet werden. Die Entwickler weisen ausdrücklich darauf hin:



> Die Verwendung erfolgt auf eigene Gefahr.

Beachten Sie, dass dieser wallet als Testnetz oder Regtest verwendet werden kann.



## Was ist Silentium?



### Philosophie und Ziele



Silentium dient als technische Demonstration für die Implementierung von Silent Payments in einem leichtgewichtigen wallet-Browser. Obwohl auch herkömmliche Bitcoin-Adressen unterstützt werden, liegt der Schwerpunkt auf Silent Payments, um den Benutzern die Möglichkeit zu geben, auf unkomplizierte Weise mit dieser Datenschutztechnologie zu experimentieren.



### Wie funktionieren die stillen Zahlungen?



Silent Payments (BIP-352) verwenden den Elliptic Curve Diffie-Hellman Key Exchange (ECDH). Der Empfänger generiert eine statische Adresse (`sp1...` auf mainnet, `tsp1...` auf testnet), die aus zwei öffentlichen Schlüsseln besteht: einem Scan-Schlüssel, um Zahlungen zu erkennen, und einem Spend-Schlüssel, um sie zu verwenden.



Der Absender kombiniert seine privaten Eingabeschlüssel mit dem Scan-Schlüssel des Empfängers, um ein gemeinsames Geheimnis zu berechnen, das einen kryptografischen "Tweak" erzeugt. Dieser Tweak, der zum Ausgabenschlüssel hinzugefügt wird, erzeugt eine eindeutige Taproot-Adresse für jede Transaktion. Der Empfänger reproduziert diese Berechnung mit seinem privaten Scan-Schlüssel, um die Gelder ohne vorherige Interaktion zu erkennen und auszugeben.



Vorteile: erhöhte Vertraulichkeit für Sender und Empfänger, kein Server eines Dritten erforderlich, Transaktionen nicht von herkömmlichen Taproot-Zahlungen zu unterscheiden. Hauptnachteil: intensives Scannen der Blockchain zur Erkennung von Zahlungen.



Um mehr über die theoretische Funktionsweise von Silent Payments zu erfahren, lesen Sie den letzten Teil des BTC.204-Kurses auf Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Unterstützte Plattformen



Silentium ist eine Progressive Web App (PWA), die über jeden modernen Browser (mobil oder Desktop) zugänglich ist. Verwenden Sie sie direkt auf "app.silentium.dev", installieren Sie sie als native Anwendung über Ihren Browser oder stellen Sie sie lokal bereit. Die Installation erfolgt direkt über den Browser, ohne den Umweg über die offiziellen Stores.



## Verwendung der Webanwendung



### Zugang und Installation



[Rufen Sie `https://app.silentium.dev/` in Ihrem Browser auf](https://app.silentium.dev/). Die Anwendung wird sofort geladen und zeigt den Startbildschirm an.



Um ihn als native Anwendung auf iOS zu installieren, drücken Sie die Freigabetaste (Quadrat mit Pfeil nach oben) und wählen Sie "Auf dem Startbildschirm". Unter Android bietet der Browser in der Regel direkt eine Benachrichtigung "Zum Startbildschirm hinzufügen". Nach der Installation erscheint Silentium mit einem eigenen Symbol und funktioniert wie eine native Anwendung, erfordert aber eine Internetverbindung, um Transaktionen zu synchronisieren.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Erstellung eines Portfolios



Wählen Sie beim ersten Start "Wallet erstellen", um ein neues Portfolio zu erstellen, oder "Wallet wiederherstellen", um eine vorhandene Wiederherstellungsphrase wiederherzustellen.



Wählen Sie "Wallet erstellen". Die Anwendung generiert einen 12-Wörter-Satz, den Sie sorgfältig aufschreiben müssen. Nur mit dieser Phrase können Sie Ihr Guthaben wiederherstellen. Auch im Testnetz sollten Sie gute Sicherungsmethoden anwenden. Drücken Sie auf "Weiter", nachdem Sie Ihre Phrase gespeichert haben.



Die Anwendung fordert Sie dann auf, ein Passwort festzulegen, um den Zugang zum wallet zu sichern. Wählen Sie ein sicheres Passwort und bestätigen Sie es.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Nach der Bestätigung des Satzes und der Eingabe des Passworts gelangen Sie zur Hauptschnittstelle.



### Interface Haupt- und Parameter



Die Hauptschnittstelle zeigt Ihren Kontostand in Satoshis an (anfangs 0 sats), mit drei Schaltflächen am unteren Rand:




- Sync**: synchronisiert wallet mit der Blockchain
- Empfangen**: Geld erhalten
- Senden**: zum Senden von Bitcoins



Sie erreichen die Einstellungen über das Symbol oben rechts (drei horizontale Balken). Das Menü "Einstellungen" bietet mehrere Optionen:





- Über**: Informationen zur Bewerbung
- Backup**: Sicherung der Wiederherstellungsphrase
- Explorer**: Wählen Sie den Blockchain-Explorer (standardmäßig Mempool) und den Silentiumd-Server
- Netzwerk**: Auswahl des Netzwerks (mainnet/Testnet)
- Passwort**: Passwort ändern
- Nachladen**: Nachladen des wallet
- Zurücksetzen**: Vollständiges Zurücksetzen
- Thema**: Thema ändern



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



Der Abschnitt **Explorer** ist besonders wichtig: Hier können Sie den verwendeten Blockchain-Explorer auswählen (standardmäßig Mempool) und die URL des Silentiumd-Servers anzeigen (`https://bitcoin.silentium.dev/v1` für mainnet). Wenn Sie Ihren eigenen Silentiumd-Server hosten oder testnet verwenden möchten, können Sie diese Parameter hier konfigurieren.



### Empfang von Geldern



Drücken Sie auf der Hauptschnittstelle die Schaltfläche "Empfangen". Standardmäßig zeigt Silentium eine Silent Payment-Adresse mit ihrem QR-Code an. Die Adresse beginnt mit `sp1...` auf mainnet oder `tsp1...` auf testnet.



Mit der Schaltfläche "Zu klassischer Adresse wechseln" / "Zu stiller Adresse wechseln" am unteren Rand des Bildschirms können Sie zwischen stiller Zahlung und klassischer Bitcoin-Adresse wechseln.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Sobald die Transaktion übertragen wurde, warten Sie bitte ein paar Minuten. Bei Silent Payments durchsucht Silentium die Blockchain automatisch nach Transaktionen, die für Sie bestimmt sind. Die Transaktionen erscheinen mit dem Status "Unbestätigt", bevor sie nach und nach bestätigt werden.



### Eine Zahlung senden



Drücken Sie auf der Hauptschnittstelle die Taste "Senden". Der Sendebildschirm wird Sie fragen:



1. **Address**: Fügen Sie eine Silent-Payment-Adresse (`sp1...` oder `tsp1...`) oder eine klassische Bitcoin-Adresse ein. Sie können das QR-Scan-Symbol verwenden, um eine Adresse zu scannen.


2. **Betrag**: Geben Sie den zu sendenden Betrag in Satoshis ein. Zur einfachen Eingabe wird ein Ziffernblock angezeigt. Ihr verfügbares Guthaben wird oben als Referenz angezeigt.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Sobald Sie die Adresse und den Betrag eingegeben haben, klicken Sie auf "Weiter", um fortzufahren. In der Anwendung werden Sie aufgefordert, die gewünschte Gebührenhöhe auszuwählen, bevor Sie die Transaktion bestätigen.



## wallet selbst gehostet



### Warum selbst hosten?



Das lokale Hosting von Silentium bietet totale Souveränität, Code-Verifizierung, eine Entwicklungsumgebung und Ausfallsicherheit bei Ausfällen der offiziellen Website.



### Voraussetzungen



Node.js (Version 14+), npm oder yarn, Git und etwa 500 MB Speicherplatz.



### Lokale Installation



Klonen Sie das Repository und installieren Sie die :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Einführung und Nutzung



Starten Sie die Anwendung im Entwicklungsmodus:



```bash
yarn start
```



Rufen Sie `http://localhost:3000` in Ihrem Browser auf. Für eine optimierte Produktionsversion :



```bash
yarn build
```



Die in `build/` erzeugten Dateien können mit nginx, Apache oder einem beliebigen Webserver bereitgestellt werden. Standardmäßig verbindet sich Silentium mit dem öffentlichen Server "bitcoin.silentium.dev". Ändern Sie diese Einstellung in den Parametern, um testnet oder Ihren eigenen Server zu verwenden.



## Der Silentiumd-Server



### Rolle und Arbeitsweise



Silentium verwendet einen **Silentiumd**-Indexierungsserver, um die Zahlungserkennung zu optimieren. Das Scannen aller Taproot-Transaktionen wäre für einen Browser oder ein Mobiltelefon zu umständlich.



Silentiumd berechnet für jede Taproot-Transaktion Zwischendaten (Tweaks) vor. Ihr wallet lädt diese Tweaks (ein paar Bytes pro Transaktion) herunter und führt die endgültige Berechnung lokal durch, um die Eigentümerschaft der Zahlung zu verifizieren. Im Gegensatz zu herkömmlichen Electrum-Servern kennt der Server niemals Ihre Schlüssel oder kann Ihre Transaktionen identifizieren.



Mit den kompakten BIP158-Filtern kann Ihr wallet bestimmen, welche Blöcke gescannt werden sollen, ohne Ihre Adressen preiszugeben, so dass Ihre Vertraulichkeit gewahrt bleibt.



### Öffentlicher Server



Der öffentliche Server "bitcoin.silentium.dev" (mainnet), der von Vulpem Ventures gesponsert wird, bietet eine einfache und unmittelbare Erfahrung. Obwohl die Vertraulichkeit gewahrt bleibt, setzt dieser Ansatz ein relatives Vertrauen in die Infrastruktur Dritter voraus.



### Hosten Sie Ihren eigenen Silentiumd-Server



Für totale Souveränität, hosten Sie Ihren eigenen Silentiumd-Server. Voraussetzungen: Bitcoin Core nicht-elagged Knoten mit `txindex=1` und `blockfilterindex=1`, Go 1.21+, 10-20 GB Festplattenplatz, Systemadministrationskenntnisse.



**Installation:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Konfigurieren Sie über Umgebungsvariablen (siehe die `config.md` des Repositorys für Details). Der Server indiziert die Blockchain und stellt einen API zur Verfügung, der von Ihrem wallet abgefragt werden kann.



Derzeit gibt es keine Paketlösungen für Umbrel oder Start9, was die Zugänglichkeit für nichttechnische Benutzer einschränkt.



## Vorteile und Grenzen



### Höhepunkte





- Maximale Zugänglichkeit**: Nutzung von jedem Browser aus, keine umfangreiche Installation erforderlich
- Multiplattform**: funktioniert auf dem Handy (Android/iOS) und dem Desktop dank der PWA-Technologie
- Einfaches Self-Hosting**: lokale Installation mit wenigen Befehlen möglich
- Open-Source**: vollständig überprüfbarer Code auf GitHub
- Datenschutz**: kein Tracking, keine Analysen, lokale kryptografische Berechnungen
- Getrennte Architektur**: klare Trennung zwischen wallet (Client) und Indizierungsserver
- Ohne Konto**: keine Registrierung oder persönliche Daten erforderlich



### Zu berücksichtigende Zwänge





- Experimentelles Projekt**: nur Konzeptnachweis, nicht für den täglichen Gebrauch oder die Produktion bestimmt
- Keine Garantien**: Risiko von Bugs, Sicherheitslücken, möglicher Verlust von Geldern
- Begrenzter Support**: wenig Benutzerdokumentation, kleine Community, kein offizieller Support
- Server-Abhängigkeit**: erfordert einen funktionierenden Silentiumd-Server (öffentlich oder selbst gehostet)
- Intensives Scannen**: Stille Erkennung von Zahlungen verbraucht Bandbreite
- Eingeschränkte Funktionalität**: keine Münzkontrolle, kein Lightning, keine Mehrfachsignaturen



## Bewährte Praktiken



### seed Sicherheit



Auch im testnet sollten Sie Ihre Wiederherstellungsformel ernst nehmen. Schreiben Sie ihn auf und bewahren Sie ihn an einem sicheren Ort auf. Bewahren Sie getrennte Geldbörsen für Testnet und mainnet auf: Verwenden Sie niemals ein Test-seed auf einem wallet, der für echte Gelder bestimmt ist.



### Überprüfung des Quellcodes



Einer der Vorteile des Selbst-Hostings ist die Möglichkeit, den Quellcode zu prüfen, bevor Sie ihn ausführen. Wenn Sie Silentium mit echtem Geld einsetzen wollen, sollten Sie sich die Zeit nehmen, den Code zu prüfen oder einen vertrauenswürdigen Entwickler damit beauftragen. Vergleichen Sie auch den Hash des auf "app.silentium.dev" bereitgestellten Codes mit dem des GitHub-Repositorys, um die Authentizität sicherzustellen.



### Sicherung und Wiederherstellung



Für die Wiederherstellung von Silent Payments-Fonds ist ein wallet erforderlich, das mit dem BIP-352-Protokoll kompatibel ist. Ein Standard-wallet kann die Blockchain nicht scannen, um Ihre UTXO Silent Payments abzurufen. Lassen Sie Silentium installiert oder stellen Sie sicher, dass Sie Zugang zu einem anderen kompatiblen wallet haben (z. B. Cake Wallet oder andere zukünftige Implementierungen), um Ihre Gelder bei Bedarf wiederherzustellen.



## Schlussfolgerung



Silentium bietet ein zugängliches Testfeld für das Verständnis von Silent Payments ohne technische Reibungsverluste. Als Proof of Concept zeigt es, wie diese Datenschutztechnologie in einen wallet-Browser integriert werden kann, ohne dass die Selbstkontrolle beeinträchtigt wird. Experimentieren Sie auf testnet, um diesen vielversprechenden Durchbruch für den on-chain-Datenschutz zu entdecken.



## Ressourcen



### Offizielle Dokumentation




- Silentium GitHub-Repository (wallet): https://github.com/louisinger/silentium
- Silentiumd GitHub-Repository (Server): https://github.com/louisinger/silentiumd
- Webanwendung: https://app.silentium.dev/
- Website der Gemeinschaft für stille Zahlungen: https://silentpayments.xyz
- Spezifikation BIP-352: https://bips.dev/352



### Artikel und Ressourcen




- Offizielle Ankündigung (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Stille Zahlungen: https://bitcoinops.org/en/topics/silent-payments/



### Testnet Werkzeuge




- Testnet Wasserhahn: https://testnet-faucet.com/
- Mempool testnet explorer: https://mempool.space/testnet