---
name: Cashu.me
description: Cashu.me Anleitung für Ecash
---

![cover](assets/cover.webp)

![video](https://www.youtube.com/watch?v=LIPw1c74LBU)

Hier ist ein Video-Tutorial von BTC Sessions, eine Videoanleitung, die dir Schritt für Schritt zeigt, wie du die Cashu.me Bitcoin Wallet einrichtest und verwendest. Diese Wallet ermöglicht dir einfache, günstige und private Bitcoin-Transaktionen - ohne die Notwendigkeit eines App Stores!

In diesem Tutorial beschäftigen wir uns mit Cashu.me, einer browserbasierten Wallet für private Bitcoin-Zahlungen mit Chaumian Ecash. Bevor wir damit beginnen, wollen wir zunächst kurz auf Ecash und dessen Funktionsweise eingehen.

## Einführung in Ecash

Stell dir vor, du hättest digitales Bargeld, das genauso funktioniert wie physische Geldscheine – also privat, von Person zu Person nutzbar. Genau das macht Ecash möglich: ein digitales Zahlungssystem, das die Privatsphäre von physischem Bargeld in die digitale Welt zurückbringt. Im Gegensatz zu Onchain-Bitcoin, wo jede Transaktion in einem öffentlichen Kassenbuch aufgeführt wird, erstellt Ecash private Token, die den tatsächlichen Bitcoin-Wert repräsentieren. Das Gute daran ist, dass dabei gleichzeitig deine Ausgabegewohnheiten vertraulich behandelt werden.

Stell dir Ecash wie digitale Inhaberpapiere vor, die auf deinem Gerät gespeichert sind – wenn du sie hältst, gehören sie dir, genau wie physisches Bargeld. Diese Token werden von Diensten ausgegeben denen man vertrauen muss, welche als `Mints` bezeichnet werden und die darunterliegenden Bitcoin-Reserven halten. Wenn du Ecash verwendest, übermittelst du keine Transaktionen an das gesamte Netzwerk. Stattdessen tauschst du private Token direkt mit anderen aus, wodurch ein Zahlungserlebnis entsteht, das sich eher wie die Übergabe von Bargeld an jemanden anfühlt als wie eine herkömmliche digitale Zahlung.

Cashu ist ein kostenloses und Open-Source-Protokoll für Chaumian Ecash, das für Bitcoin entwickelt wurde. Die Technologie baut auf der bahnbrechenden kryptografischen Forschung von David Chaum aus den 1980er Jahren auf und verwendet `Blind signatures`, um die Privatsphäre zu gewährleisten. Wenn du Ecash-Token erhältst, signiert der Mint sie, ohne zu wissen, wo sie als Nächstes ausgegeben werden. Dies ist ein entscheidendes Merkmal, da es die Transaktionsverfolgung verhindert. Wichtig ist, dass Ecash Bitcoin nicht ersetzt; es ergänzt es, indem es einige kritische Probleme löst, die mit den Architekturanforderungen von Bitcoin verbunden sind. Es bietet die Privatsphäre, die physisches Bargeld bietet (die Bitcoin durch seinen transparentes Ledger fehlt) und ermöglicht sofortige Mikrotransaktionen ohne Blockchain-Gebühren oder Bestätigungsverzögerungen.

Ecash lässt sich nahtlos in das Lightning-Netzwerk integrieren. Du verwendest Lightning, um Bitcoin in einen Mint einzuzahlen (deinen Bitcoin-Wert in Ecash-Token umzuwandeln) und später wieder auszuheben (Token werden wieder in ausgabefähiges Lightning-Guthaben umgewandelt). Zusammen bilden sie eine leistungsstarke Kombination: Bitcoin bietet eine sichere Abrechnungsebene, Lightning ermöglicht schnelle Transaktionen und Netzwerk-Interoperabilität und Ecash fügt eine Ebene für den Privatsphäre hinzu, die digitale Zahlungen wieder wirklich privat macht.

## Cashu.me

Cashu.me ist eine `Progressive Web App (PWA)`, die das Cashu-Protokoll implementiert – eine spezifische Implementierung von Chaumian Ecash, die für Bitcoin entwickelt wurde. Als PWA funktioniert sie direkt in deinem Browser, ohne dass eine Installation aus App Stores erforderlich ist. Du kannst sie jedoch auf deinem Gerät `installieren`, um den Zugriff zu vereinfachen. Dieser webbasierte Ansatz gewährleistet eine breite Kompatibilität über Betriebssysteme hinweg und sorgt gleichzeitig durch kryptografische Protokolle für Sicherheit, anstatt sich auf Plattformbeschränkungen zu verlassen.

## 🎉 Wichtige Funktionen

Werfen wir einen Blick auf die Funktionen und erkunden wir, was Cashu.me zu bieten hat:

- **Chaumian Ecash auf Lightning:** Es werden Blind Signaturen verwendet, sodass Mints die Kontostände oder Transaktionshistorien der Benutzer nicht nachverfolgen können.
- **Selbstverwahrung von Token:** Du kontrollierst Ecash-Token lokal mit deiner Seed-Phrase
- **Seed-Phrase-Backups**: 12-Wort-Wiederherstellungsphrase für die Wallet-Wiederherstellung
- **Unabhängigkeit der Mints**: Funktioniert mit mehreren unabhängigen Mints – du bist nicht an einen Anbieter gebunden
- **Sofortige, kostenlose Transaktionen**: Innerhalb desselben Mints werden Zahlungen in Sekunden finalisiert, ohne Gebühren
- **Architektur zum Schutz der Privatsphäre**: Mints können nicht sehen, wer mit wem Transaktionen durchführt.
- **Offline Ecash**: Sende/Empfange Token über ein lokales Übertragungsprotokoll wie NFC, QR-Code, Bluetooth usw., auch ohne Internetverbindung zu benötigen
- **Ecash Mints über Nostr entdecken**: Finde und verifiziere vertrauenswürdige Mints durch das Nostr-Protokoll
- **Ecash zwischen Mints tauschen**: Alle Mints sprechen Lightning, was bedeutet, dass du Guthaben zwischen ihnen tauschen kannst
- **Wallet-Freigabe mit Nostr Wallet Connect (NWC)**: Verbinde dich mit anderen Apps wie Nostr Clients und beginne per NWC zu zappen

Der entscheidende Kompromiss ist `Vertrauen`: Zwar kontrollierst du die Token selbst, musst aber darauf vertrauen, dass die Mints die zugrunde liegenden Bitcoin-Reserven verwahren. Wie in der Dokumentation von Cashu angegeben: :

> ...der Mint betreibt die Lightning-Infrastruktur und verwahrt die Satoshis für die Ecash-Nutzer des Mints. Die Nutzer müssen dem Mint vertrauen, dass er ihre Ecash einlöst, wenn sie diese gegen Lightning austauschen wollen.

— Cashu Dokumentation, [General Safety and Privacy Questions](https://docs.cashu.space/faq#general-safety-and-privacy-questions) 

Dadurch wird Ecash zu einer Custodial Lösung für Bitcoin selbst, wobei du jedoch die volle Kontrolle über die Token behälst.

## 1️⃣ Erste Einrichtung

① Beginne damit, [wallet.cashu.me](wallet.cashu.me) mit deinem Browser aufzurufen. Da die Cashu.me Wallet eine `PWA` ist, musst du sie nicht aus App Stores herunterladen, sondern kannst die Seite einfach direkt in deinem Browser öffnen. Für leichteren Zugriff kannst du die PWA optional auf deinem Gerät zur Startseite hinzufügen.

② Um die PWA zu installieren, tippe auf die ⋮ in deinem Browser und wähle `Add to Home Screen`. Nach der Installation schließe die Browser-Registerkarte und starte Cashu.me von deinem Startbildschirm neu. Auf dem Willkommensbildschirm tippe auf `Next`, um fortzufahren.

③ Sicherheit ist entscheidend. Bewahre deine Seed-Phrase sicher in einem Passwortmanager auf. Noch besser ist es, sie auf Papier zu schreiben. Diese 12-Wort-Wiederherstellungsphrase ist deine einzige Möglichkeit, dein Guthaben wiederherzustellen, wenn du den Zugriff auf dieses Gerät verlierst. Tippe auf das 👁️-Symbol, um deine Seed-Phrase anzuzeigen. Notiere anschließend sorgfältig alle zwölf Wörter in der richtigen Reihenfolge und aktiviere dann das Kästchen mit der Bezeichnung `I have written it down`. Tippe auf `Next` um fortzufahren, und aktiviere das Kästchen, um zu bestätigen, dass du die `terms` akzeptierst.

![image](assets/en/01.webp)

Nach Abschluss der Einrichtung musst du dich mit einem `Mint` verbinden. Tippe auf `ADD MINT` gefolgt von `DISCOVER MINTS` um Mints anzuzeigen, die von der Nostr-Community empfohlen werden. Für zusätzliche Verifizierung kannst du die Mint-Bewertungen auf [bitcoinmints.com](bitcoinmints.com) überprüfen.

Tippe dann auf `Click to browse mints`, um die vollständige Liste zu sehen. Wähle einen Mint, indem du seine URL kopierst, sie in das URL-Feld einfügst und ihm einen eindeutigen Namen gibst. Für dieses Beispiel verwenden wir:

URL: `https://mint.minibits.cash/Bitcoin`  
Name: `Minibits`

![image](assets/en/02.webp)

Tippe auf `ADD MINT` um den Vorgang abzuschließen. Auf dem Bestätigungsbildschirm überprüfe, ob du dem Mint-Betreiber vertraust, und tippe erneut auf `ADD MINT`. Der Minibits-Mint wird nun auf deinem Startbildschirm angezeigt. Sobald deine Wallet eingerichtet ist, musst du sie vor Transaktionen aufladen.

![image](assets/en/03.webp)

## 2️⃣ Wallet aufladen

Cashu.me bietet zwei verschiedene Methoden, um deine Wallet aufzuladen. Wenn du auf `Receive` auf dem Startbildschirm tippst, siehst du Optionen, um Guthaben über `ECASH` oder über `LIGHTNING` zu empfangen. Lass uns beide Optionen erkunden.

![image](assets/en/04.webp)

### Aufladen über LIGHTNING

Die erste Option besteht darin, die Wallet über eine Lightning-Invoice aufzuladen. `Select a mint` wenn du verschiedene Mints hinzugefügt hast, und definiere den `amount (sats)` den du empfangen möchtest. Tippe dann auf `CREATE INVOICE`. Jetzt wird ein QR-Code angezeigt, den du mit einer anderen Lightning-Wallet scannen kannst, oder du kannst die Invoice einfach über `Copy` in eine andere Wallet einfügen, um zu zahlen und deine Cashu.me-Wallet aufzuladen.

![image](assets/en/05.webp)

### Ecash empfangen

Die Ecash-Option ermöglicht es dir, Token direkt von einer anderen Ecash-Wallet zu empfangen. Beginne, indem du auf die `Receive` tippst und die `ECASH` Option wählst. Du kannst `Paste` oder `Scan` oder `NFC` verwenden, um einen Cashu-Token von einer anderen Wallet zu senden. Wenn du einfügen wählst, gib die Token-Zeichenfolge ein, die du von einer anderen Wallet kopiert hast, der `Amount` und der `Mint` werden automatisch angezeigt. Tippe auf `RECEIVE` um die Transaktion abzuschließen, und die Sats werden in deiner Wallet angezeigt. Beachte, dass dein Guthaben jetzt über mehrere Mints verteilt ist. Zum Beispiel könntest du 1,000 Sats in deinem Minibits `Mint` und zusätzliche 1,000 Sats in einem Coinos `Mint` haben. Diese Trennung über verschiedene Mints ist ein wichtiger Aspekt der Cashu-Architektur.

![image](assets/en/06.webp)

### Zwischen Mints tauschen

Wenn du einem bestimmten Mint, den du hinzugefügt hast, nicht mehr vertraust, bietet cashu.me eine Funktion zum `Swap` um Guthaben von einem Mint zu einem anderen zu übertragen. Navigiere zum Mint-Tab und scrolle nach unten, bis du `Multimint Swaps` siehst. Wähle den Mint `FROM` und `TO` aus den Dropdown-Menüs aus und gib den Betrag ein, den du übertragen möchtest. Tippe auf `SWAP` um die Token zwischen den Mints zu tauschen. Dies wird über eine Lightning-Transaktion ausgeführt, daher musst du Platz für mögliche Lightning-Gebühren lassen. In meinem Beispiel war 1 Sat ausreichend.

![image](assets/en/07.webp)

## 3️⃣ Guthaben senden

Um Sats zu senden, bietet Cashu.me zwei Optionen. Du kannst entweder über `Ecash` oder über `Lightning` senden. Lass uns beide Optionen betrachten.

### Senden über Lightning

Um über Lightning zu senden, folge diesen Schritten:

1. Tippe auf `SEND` auf dem Startbildschirm und wähle `Lightning`
2. Die App fordert dich auf, eine `Lightning invoice` oder `-address` einzugeben. Du kannst die Rechnung/Adresse direkt einfügen oder die Option zum Scannen des QR-Codes verwenden, um sie visuell zu erfassen, und bestätige dann mit `ENTER`
3. Wähle den Mint aus, von dem du zahlen möchtest, indem du das Dropdown-Feld verwendest, und tippe auf `PAY` um zu bestätigen. **Hinweis**: es gibt auch eine Option, `Multinut` unter `Settings` -> `Experimental` zu verwenden, die es ermöglicht, Rechnungen von mehreren Mints gleichzeitig zu zahlen.
4. Nach erfolgreichem Abschluss siehst du die Zahlungsbestätigung und den Betrag, der von deinem Guthaben abgezogen wurde.

![image](assets/en/08.webp)

### Senden über Ecash

Das Senden von Ecash ist ähnlich einfach.

1. Tippe auf `SEND` und diesmal wähle die `ECASH` Option.
2. `Select a mint` und gib den `Amount` ein, den du in Sats senden möchtest, und tippe auf `SEND` um zu bestätigen
3. Dies erstellt einen `Animated QR Code` den du anpassen kannst, indem du die Geschwindigkeit und Größe anpasst. Jeder kann diesen QR-Code scannen, um die Sats sofort einzulösen, oder du kannst auf `COPY` tippen, um die Token-Zeichenfolge an jemanden anders über alternative Kanäle wie Bluetooth, NFC oder Nachrichten zu senden.
4. Ich öffne eine andere Wallet. Füge aus der Zwischenablage ein und wähle `Receive ecash` in der anderen Wallet.

![image](assets/en/09.webp)

## 4️⃣ Zusätzliche Funktionen

Neben den Hauptfunktionen zum Senden und Empfangen bietet Cashu.me leistungsstarke Zusatzfunktionen, die dein Bitcoin-Erlebnis im Nostr-Ökosystem verbessern.

### Nostr Wallet Connect

Nostr Wallet Connect (`NWC`) verändert, wie du mit Nostr-Anwendungen interagierst, indem es eine nahtlose Verbindung zwischen deiner Wallet und sozialen Apps herstellt. Dieses Protokoll ermöglicht es Anwendungen wie [Damus](https://damus.io/) oder [Primal](https://primal.net/home), Zahlungen direkt über Nostr-Relays anzufordern, ohne dass du die App verlassen musst.

Um `NWC` in Cashu.me einzurichten:

1. Gehe zu `Settings` auf dem Hamburger-Menü oben links
2. Scrolle zum `NOSTR WALLET CONNECT` Abschnitt und tippe auf die `Enable` Taste
3. Dann richtest du eine Erlaubnis ein, um den maximalen Betrag festzulegen, den Anwendungen von deiner Wallet ausgeben dürfen.
4. Sobald konfiguriert, kannst du die Verbindungszeichenfolge kopieren und in jeden Nostr-Client einfügen, der `NWC` unterstützt, was sofortige Zapping- und Trinkgeldfunktionen ermöglicht.

![image](assets/en/10.webp)

### Lightning-Adresse über npub.cash

Cashu.me integriert [npub.cash](https://npub.cash/), um eine Lightning-Adresse bereitzustellen, die nahtlos mit dem Nostr-Protokoll zusammenarbeitet. Hier kannst du dich anmelden und deinen Benutzernamen beanspruchen, indem du deinen Nostr `nsec` bereitstellst, was 5,000 Sats kostet und das npub.cash-Projekt unterstützt. Oder du kannst jeden öffentlichen Nostr-Schlüssel (`npub`) ohne Registrierung verwenden.

Zuerst gehe zu `Settings` und tippe `Enable` Lightning address with npub.cash. Dies generiert eine npub.cash-Adresse unter Verwendung einer `npub`-Zeichenfolge, die standardmäßig von deiner Wallet-Seed-Phrase abgeleitet wird.

Alternativ besuche [diese Website](https://npub.cash/username) um einen benutzerdefinierten Benutzernamen unter Verwendung deines eigenen Nostr `nsec` zu beanspruchen, was dir eine personalisierte Lightning-Adresse wie `Benutzername@npub.cash` gibt.
 
![image](assets/en/11.webp)

## 🎯 Fazit

Cashu.me bietet private Bitcoin-Zahlungen, die wie physisches Bargeld funktionieren – sofort und peer-to-peer, ohne deine Transaktionshistorie preiszugeben. Ich schätze persönlich die PWA-Architektur, weil sie frei von App-Store-Beschränkungen ist. Durch die Kombination der Sicherheit von Bitcoin, der Geschwindigkeit von Lightning und der Privatsphäre von Ecash bietet die Wallet Funktionen, die die alltägliche Bitcoin-Adoption fördern könnten.

Obwohl du die volle Kontrolle über deine Ecash-Token durch Selbstverwaltung hast, denke daran, dass Mints als zu vertrauende Dienste agieren, die die darunterliegenden Bitcoin-Reserven halten. Die Möglichkeit, mehrere Mints zu verwenden und zwischen ihnen zu tauschen, bietet Flexibilität, während die Privatsphäre gewahrt bleibt.

Dank Funktionen wie NWC und npub.cash-Adressen ist Cashu.me eine ansprechende Wallet-Option für Nostr-Clients, die Privatsphäre und Souveränität Big-Tech-Politikbeschränkungen vorziehen.

## 📚 Ressourcen

[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)

[https://github.com/cashubtc](https://github.com/cashubtc)

[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)

[https://cashu.space/](https://cashu.space/)
