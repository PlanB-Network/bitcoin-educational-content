---
name: Minibits Wallet
description: Anleitung für Minibits Wallet
---

![cover](assets/cover.webp)


In diesem Tutorial zeige ich dir Schritt für Schritt, wie du die Minibits Wallet für Ecash einrichtest. Eine leistungsfähige, auf Datenschutz ausgerichtete Zahlungstechnologie, die mit Bitcoin kompatibel ist. Minibits ist eine Ecash- und Lightning-Wallet, die sofortige, kostengünstige und private Werttransfers ermöglicht und sich somit ideal für alltägliche Transaktionen eignet, bei denen die Privatsphäre eine wichtige Rolle spielt.

Bevor wir loslegen, sollten wir uns zunächst einmal damit auseinandersetzen, was Ecash ist und was nicht. Viele Menschen verwechseln Ecash mit Bitcoin oder der Blockchain-Technologie, dabei handelt es sich jedoch um grundlegend unterschiedliche Konzepte.

Ecash ist KEIN Bitcoin. Es ersetzt nicht deine selbstverwahrte Bitcoin-Wallet, sondern ergänzt sie. Ecash ist KEINE Blockchain und NICHT auf einem öffentlichen Ledger gespeichert. Interessanterweise ist Ecash KEINE neue Technologie – die Idee stammt aus den 1980ern/90ern, also vor dem World Wide Web!

Was Ecash IST: extrem privat (keine nachvollziehbare Transaktionshistorie), peer-to-peer (direkter Transfer ohne Vermittler) und digitales Eigentum (wer es hat, kontrolliert es). Ein riesiger Vorteil: Ecash kann offline genutzt werden – Sender oder Empfänger müssen nicht im Internet sein. Ecash kann von einer Einzelperson oder einem Föderation vertrauenswürdiger Entitäten geprägt werden. Und es IST die ideale Ergänzung zu Bitcoin: kleine Alltagstransaktionen laufen über Ecash, Bitcoin dient als Abrechnungsebene.

Beachte, dass dieses Minibits-Setup eine `custodial Lösung` darstellt. Das bedeutet, du vertraust dem Mint-Betreiber damit, deine Gelder zu verwalten. Dies birgt spezifische Risiken, die du verstehen solltest, bevor du fortfährst.

Das Projekt zeigt diesen wichtigen Hinweis an:

- Diese Wallet sollte ausschließlich zu Forschungszwecken genutzt werden.
- Die Wallet ist eine Beta-Version mit unvollständiger Funktionalität sowie bekannten und unbekannten Fehlern.
- Verwende sie nicht mit großen Ecash-Beträgen.
- Das in der Wallet gespeicherte Ecash wird vom Mint ausgegeben.
- Du vertraust dem Mint, dass es durch Bitcoin gedeckt ist, bis du deine Guthaben in eine andere Bitcoin-Lightning-Wallet überträgst.
- Das Cashu-Protokoll der Wallet wurde bisher nicht ausführlich geprüft oder getestet.

Behandle Minibits wie ein alltägliches Portemonnaie, nicht wie ein Sparkonto, und speichere hier niemals größere Summen.


## 1️⃣ Wallet einrichten


Besuche zuerst die [Minibits Webseite](https://www.minibits.cash/) Dort findest du Downloads für alle Plattformen. iOS-Nutzer laden die App im [App Store](https://testflight.apple.com/join/defJQgTD),EU-iOS-Nutzer zusätzlich im [Freedom Store](https://freedomstore.io/) . Android-Nutzer holen sie im [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) oder direkt als APK von der  [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases) Seite.

Beim Installieren siehst du Einführungsbildschirme zur Technologie – lies sie durch oder skippe sie, wenn du schon Bescheid weißt. Danach wählst du zwischen:

- `Verstanden, zur Wallet` (neuer Nutzer)
- `Verlorene Wallet wiederherstellen` (Backup nutzen).

![image](assets/en/01.webp)

Nach der Einrichtung landest du auf dem Startbildschirm mit diesen Elementen:  
① Profil-Icon (oben): Geht zu deinem Profil, um deine Minibits-Adresse zu sehen oder `Batch-Receive`-Optionen zu wählen.  
② Mitte: Zeigt die verfügbaren Mints – Minibits Mint ist standardmäßig aktiv.  
③ Aktionsleiste: Hier schickst du Ecash/Lightning-Zahlungen, scannst QR-Codes oder empfängst Geld.  
④ Navigationsleiste unten: Schnellzugriff auf Startseite, Transaktionsverlauf, Kontakte und Einstellungen.


![image](assets/en/02.webp)


## 2️⃣ Mints verwalten


Standardmäßig ist der Minibits Mint aktiv. Ein Vorteil von Ecash: Du kannst mehrere Mints nutzen, um Sicherheit und Dezentralisierung zu erhöhen. Um einen neuen Mint hinzuzufügen, geh zu `Einstellungen` → `Mints verwalten` → `Mint hinzufügen`.

Auf [Bitcoinmints.com](Bitcoinmints.com) findest du eine Liste aller Mints mit Bewertungen – such dir vertrauenswürdige aus. Mit mehreren Mints reduzierst du Risiken: Wenn ein Mint Probleme hat, sind deine Gelder auf anderen Mints trotzdem sicher.


![image](assets/en/04.webp)


## 3️⃣ Backup erstellen


Das Backup ist der wichtigste Schritt! Geh zu `Einstellungen` → `Backup`. Dort hast du zwei Optionen:

1. `Deine Seed-Phrase`: 12 Wörter, mit denen du dein Ecash auf allen Mints wiederherstellen kannst. Schreib sie physisch auf (Papier/Metall) und lagere sie an mehreren sicheren Orten. Nie digital speichern! Schau dir [dieses Tutorial](https://planb.academy/en/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) an, um die besten Praktiken zu lernen.
2. Das `Wallet-Backup`: welches aus einen langen Backup-String besteht.

**Achtung**: Für die Wiederherstellung brauchst du immer noch deine Seed-Phrase – der Backup-String allein reicht nicht!


![image](assets/en/05.webp)


## 4️⃣ Minibits-Wallet-Adresse erstellen


Geh unten zu `Kontakte` und pass deine persönliche `Minibits-Wallet-Adresse` an: Tippe `Ändern` → `Wallet-Adresse ändern`. Gib deinen Wunsch-Namen ein und prüfe die Verfügbarkeit.


![image](assets/en/07.webp)


Nach der Erstellung wirst du um eine kleine `Spende` gebeten, um das Projekt zu unterstützen. Das ist freiwillig, aber sinnvoll, wenn du die App regelmäßig nutzt. Open-Source-Projekte wie Minibits leben von der Community – selbst kleine Beträge sichern die Weiterentwicklung.


![image](assets/en/08.webp)


## 5️⃣ Nostr Setup


Möchtest du Leute, denen du auf Nostr folgst, zappen? Dann füge deinen `npub-Schlüssel` hinzu: Geh zu `Kontakte` → `Öffentlich`. So verknüpfst du deine Minibits-Wallet mit Nostr für einfaches Tipping.

Du kannst auch dein eigenes Profil nutzen: Gehe zu `Einstellungen` → `Datenschutz`, um deine eigene Nostr-Adresse und Schlüssel zu importieren. Aber Vorsicht: Dann funktioniert die Kommunikation mit minibits.cash-Nostr und LNURL-Adresse-Servern nicht mehr – Zap-Empfang per Lightning-Adresse ist dann deaktiviert.


![image](assets/en/09.webp)


## 6️⃣ Geld erhalten


Zum Start musst du die Wallet per Lightning-Invoice aufladen. Tippe `Aufladen`, gib den Betrag ein, füge optional eine Notiz hinzu und bestätige mit `Invoice erstellen`. Zahle diese Invoice dann mit einer anderen Lightning-Wallet – so wandelst du Bitcoin in Ecash-Token um.

![image](assets/en/10.webp)


## 7️⃣ Geld senden


Jetzt kannst du Geld auf zwei Arten versenden:

### Ecash senden

Tippe `Senden` → `Ecash senden`, gib den Betrag ein und bestätige mit `Token erstellen`. Ein QR-Code erscheint – teile ihn mit dem Empfänger oder lass ihn scannen. Die Ecash-Tokens landen sofort in seiner Wallet, ohne Gebühren oder Bestätigungsverzögerung.


![image](assets/en/11.webp)


### Mit Lightning zahlen

Tippe `Senden` → `Mit Lightning zahlen`. Wähle aus deinen Nostr-Kontakten (wenn du npub verbunden hast) oder füge eine Lightning-Adresse-, Invoice- oder LNURL-Pay-Code via `Einfügen`/`Scannen` ein. Bestätige den Empfänger, gib den Zu zahlenden Betrag ein, füge optional eine Notiz hinzu und tippe `Bestätigen` → `Jetzt zahlen`.


![image](assets/en/12.webp)


## 8️⃣ NWC-Verbindung erstellen


Minibits kann `Nostr Wallet Connect (NWC)`-Verbindungen erstellen – andere Apps können damit Zahlungen von deiner Wallet anfordern, ohne deine privaten Schlüssel zu sehen.

Um die Funktion einzurichten, gehe zu: `Einstellungen` → `Nostr Wallet Connect` → `Verbindung hinzufügen`. Gib der Verbindung einen klaren Namen (App + Nutzerkonto), setze ein tägliches Maximal-Limit und bestätige mit `Speichern`.

Dies ist praktisch für Nostr-Clients, bei denen du automatisches Tippen aktivieren willst – ohne jede Transaktion manuell zu bestätigen.


![image](assets/en/12.webp)


## 🎯 Fazit

Minibits ist dein Einstieg ins Ecash-Universum: Private Zahlungen, die deine Bitcoin Guthaben ergänzen. Denk immer an sichere Backups, nutze zur Sicherheit mehrere Mints und speichere nie große Summen in dieser custodial Lösung.

Mehr Infos findest du auf GitHub, auf der Website und im Telegram-Channel – dort tauscht sich die Community über Updates und Problemlösungen aus:
- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Website](https://www.minibits.cash/)
- [Telegram](https://t.me/MinibitsWallet)

Das Ecash-Ökosystem ist immer noch in der Entwicklung, aber Tools wie Minibits machen diese starke Datenschutz-Technologie immer zugänglicher für alle.
