---
name: Macadamia Wallet
description: Cashu mobile wallet für anonyme und sofortige BTC-Zahlungen
---

![cover](assets/cover.webp)



Macadamia Wallet ist ein mobiler wallet für iOS, der das Cashu-Protokoll implementiert, ein chaumianisches Ecash-System, das völlig anonyme Bitcoin-Zahlungen ermöglicht. Dank der blinden Unterschrift kann kein Beobachter Ihre Einzahlungen mit Ihren Ausgaben in Verbindung bringen, was eine ähnliche Vertraulichkeit wie bei physischem Bargeld bietet.



In diesem Tutorial erfahren Sie, wie Sie Macadamia installieren und konfigurieren, Ihre ersten Cashu-Transaktionen durchführen (Mint, Send, Receive, Melt) und mehrere Mints verwalten, um Ihr Geld zu sichern.



## Was ist Macadamia Wallet?



### Das Cashu-Protokoll



Cashu verwendet Blindsignaturen, die von David Chaum erfunden wurden: Sie zahlen Bitcoins bei einem "Mint"-Server ein, der entsprechende Token in Satoshis ausgibt. Die Münzanstalt signiert diese Token, ohne deren Inhalt zu sehen, was es unmöglich macht, einen token mit einem Nutzer zu verbinden. Der Austausch ist off-chain, Peer-to-Peer und völlig undurchsichtig - selbst die Münzanstalt kann nicht nachvollziehen, wer wen bezahlt.



Macadamia ist ein quelloffenes wallet iOS, das in Swift/SwiftUI entwickelt wurde. Es funktioniert ohne Konto oder KYC, Ihre Token werden lokal gespeichert und durch eine seed Phrase geschützt. Der Code ist auf GitHub überprüfbar und die Token sind mit anderen Cashu-Geldbörsen (Minibits, Cashu.me) interoperabel.



### Verwahrungsmodell und Kompromiss



**Wichtig**: Cashu arbeitet nach einem Verwahrungsmodell. Münzen sind Zahlungsversprechen (IOUs), die durch die Bitcoin-Reserven der Münzanstalt gedeckt sind. Wenn die Münzanstalt verschwindet, verlieren Ihre Münzen ihren Wert. Dies ist der Kompromiss für maximale Vertraulichkeit.



Verwenden Sie Macadamia als physisches wallet: nur kleine Mengen. Verteilen Sie Ihre Mittel auf mehrere Prägeanstalten, um das Risiko zu streuen.



## Hauptmerkmale



Macadamia implementiert die vier grundlegenden Operationen des Cashu-Protokolls. **Mint** wandelt Ihre Satoshis in Token über eine Lightning-Rechnung um. *mit *Senden** können Sie kostenlos Token per QR-Code oder Link versenden, komplett off-chain. *mit *Empfangen** können Sie Token oder generate eine Lightning-Rechnung empfangen. *mit *Schmelzen** bezahlen Sie eine Blitzrechnung, indem Sie Ihre Token zerstören.



wallet unterstützt die Verwaltung mehrerer Münzstätten gleichzeitig. Sie können Token zwischen verschiedenen Münzstätten über Lightning austauschen.



## Unterstützte Plattformen



Macadamia ist nur unter iOS 17 oder höher für iPhone und iPad verfügbar. Die native Swift/SwiftUI-Anwendung bietet eine optimale Integration in das Apple-Ökosystem.



Das Cashu-Protokoll garantiert die Interoperabilität zwischen den Geldbörsen. Sie können Ihre seed-Phrase in anderen Anwendungen wie Minibits auf Android oder Nutstash auf dem Desktop wiederherstellen.



Die aktuelle Version wird über TestFlight verteilt. Verwenden Sie nur kleine Mengen mit dieser Beta-Version.



## Einrichtung



Macadamia ist derzeit über TestFlight, das Beta-Testprogramm von Apple, verfügbar. Hier erfahren Sie, wie Sie es installieren können:



### Installation über TestFlight



**Schritt 1: TestFlight herunterladen**



Wenn Sie die TestFlight-App noch nicht auf Ihrem Gerät haben, suchen Sie im App Store nach "TestFlight" und installieren Sie sie. TestFlight ist die offizielle Anwendung von Apple zum Testen von Beta-Versionen von iOS-Anwendungen.



**Schritt 2: Nehmen Sie am Macadamia-Beta-Programm teil** (auf Französisch)



Sobald TestFlight installiert ist, folgen Sie diesem Einladungslink von Ihrem iPhone oder iPad aus: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



Der Link öffnet automatisch TestFlight und bietet Ihnen an, Macadamia Wallet zu installieren. Tippen Sie auf "Akzeptieren" und dann auf "Installieren", um den Download zu starten. Die Anwendung wiegt etwa zehn Megabyte und die Installation dauert nur wenige Sekunden.



![Installation TestFlight](assets/fr/01.webp)



### Wichtige Informationen über Beta-Versionen



Macadamia befindet sich noch in der aktiven Entwicklungsphase. TestFlight-Versionen werden häufig aktualisiert und können neue Funktionen einführen oder Fehler beheben. Wie bei jeder Betaversion kann es jedoch zu Fehlfunktionen kommen. **Wir empfehlen Ihnen dringend, nur kleine Mengen** zu verwenden, deren Verlust Sie im Falle eines technischen Problems in Kauf nehmen.



Macadamia sammelt keine Nutzerdaten gemäß der angezeigten Datenschutzrichtlinie. Achten Sie bei der Installation darauf, dass der Entwickler cypherbase UG ist.



## Erstmalige Konfiguration



Beim ersten Start erzeugt Macadamia einen BIP-39-Satz mit 12 Wörtern. Schreiben Sie sie an einem sicheren Ort auf - niemals als Screenshot. Mit diesen Wörtern können Sie Ihr wallet neu erstellen und Ihre Token ausgeben.



![Configuration initiale](assets/fr/02.webp)



Folgen Sie den vier Schritten: Willkommen, Bedingungen akzeptieren, seed-Satz speichern und abschließende Bestätigung.



![Interface principale](assets/fr/03.webp)



Sobald die Konfiguration abgeschlossen ist, präsentiert Macadamia drei Hauptregisterkarten. **Wallet** zeigt Ihren Kontostand und die Transaktionshistorie an. *mit *Mints** können Sie Ihre Cashu-Server verwalten. **Einstellungen** ermöglicht den Zugriff auf die Einstellungen und Ihre seed-Phrase.



![Ajout d'un mint](assets/fr/04.webp)



Nun müssen Sie eine Münzprägeanstalt konfigurieren, d. h. einen Cashu-Server, der Ihre Token ausgeben wird. Gehen Sie auf die Registerkarte "Mints", tippen Sie auf "Add new Mint URL" und geben Sie die Adresse der von Ihnen gewählten Münzprägeanstalt ein (z. B. mint.cubabitcoin.org). Informieren Sie sich auf bitcoinmints.com oder cashu.space über seriöse öffentliche Münzprägeanstalten. Bestätigen Sie nur Münzprägeanstalten, deren Reputation Sie überprüft haben, da diese über Ihre Satoshis verfügen.



## Täglicher Gebrauch



### Erstellung neuer Münzmarken (Mint)



Um Ihr wallet Macadamia mit Ecash zu füttern, müssen Sie eine "Mint"-Operation durchführen (um Token zu erstellen). Tippen Sie auf "Empfangen" und wählen Sie dann die Option "Blitz". Geben Sie den gewünschten Betrag ein (z. B. 1000 sats), wählen Sie die zu verwendende Münzsorte und generate dann die Lightning-Rechnung.



![Opération Mint](assets/fr/05.webp)



Bezahlen Sie die erstellte Lightning-Rechnung mit Ihrem üblichen wallet (Phoenix, Zeus, BlueWallet).



![Confirmation Mint](assets/fr/06.webp)



Cashu-Token erscheinen sofort nach der Zahlung in Ihrem Guthaben.



### Token senden



Um Cashu-Token an einen anderen Benutzer zu senden, berühren Sie die Schaltfläche "Senden" auf dem Hauptbildschirm und wählen Sie dann "Ecash". Geben Sie den zu versendenden Betrag ein (z. B. 50 sats) und fügen Sie bei Bedarf eine beschreibende Notiz hinzu.



![Envoi Ecash](assets/fr/07.webp)



Teilen Sie den QR-Code oder den generierten Text über iMessage, Signal oder Telegram. Der Empfänger fordert das Geld sofort und kostenlos an.



### Token erhalten



Um von einem anderen Benutzer gesendete Cashu-Token zu erhalten, berühren Sie "Empfangen" und wählen Sie dann "Ecash". Scannen Sie den token QR-Code oder fügen Sie den token Link ein, den Sie erhalten haben.



![Réception Ecash](assets/fr/08.webp)



Berühren Sie "Redeem", um token zu beanspruchen.



### Zahlungen bei Blitzschlag (Schmelzen)



Um eine Lightning-Rechnung mit Ihren Cashu-Tokens zu bezahlen, tippen Sie auf "Senden" und wählen Sie dann "Lightning". Fügen Sie eine BOLT11-Rechnung ein, die Sie bezahlen möchten.



![Paiement Lightning](assets/fr/11.webp)



Die Münzanstalt vernichtet Ihre Token und führt die Lightning-Zahlung aus. So können Sie für jeden Lightning-Dienst bezahlen und gleichzeitig Ihre Anonymität bewahren.



### Tauschen Sie zwischen Minzbonbons



Wenn Sie Wertmarken von einer Münzanstalt erhalten, die Sie nicht konfiguriert haben, bietet Ihnen Macadamia mehrere Optionen zur Verwaltung dieser Wertmarken.



![Swap inter-mints](assets/fr/09.webp)



Fügen Sie die neue Münzstätte hinzu oder tauschen Sie die Token mit einer bestehenden Münzstätte. Der Tausch nutzt Lightning als Brücke, um Ihr Geld anonym zu übertragen.



### Erweiterte Verwaltung mehrerer Münzstätten



Macadamia bietet ausgefeilte Tools für die gleichzeitige Verwaltung mehrerer Mints und die strategische Zuweisung Ihrer Mittel.



![Gestion multi-mints](assets/fr/10.webp)



mit "Geld verteilen" wird Ihr Guthaben automatisch prozentual aufgeteilt (z.B. 50/50). "Transfer" ermöglicht manuelle Transfers zwischen Münzstätten, um Ihre Risiken zu diversifizieren.



## Vorteile und Grenzen



**Highlights** :





- Höchste Vertraulichkeit**: Nicht zurückverfolgbare Transaktionen, selbst für die Münzanstalt. Keine Blockchain-Metadaten, spurloser Peer-to-Peer-Austausch.
- Schnell und kostenlos**: Kostenlose Sofortüberweisungen innerhalb einer Münze, ideal für Kleinstbeträge.
- Interoperabilität**: standardisierte Cashu-Tokens zur Verwendung mit anderen kompatiblen Wallets (Minibits, Nutstash).
- Einfachheit**: Interface iOS Native ist auch für Anfänger zugänglich und gleichzeitig überprüfbar (Open Source).



**Einschränkungen** :





- Verwahrungsmodell**: Vertrauen in die Münze erforderlich. Wenn eine Münzanstalt verschwindet, verlieren Ihre Münzen ihren Wert.
- nur iOS**: Keine Android-/Desktop-Version. Die Interoperabilität von Cashu ermöglicht den Zugriff über andere Geldbörsen, aber das optimale Erlebnis bleibt iOS.
- Mint-Abhängigkeit**: Mint offline = nicht in der Lage, Transaktionen auszuführen, die sein Eingreifen erfordern (Mint, Melt).
- Aufstrebende Technologie** : Aktive Entwicklung, mögliche Bugs, sich entwickelnde Standards.



## Bewährte Praktiken





- Diversifizieren Sie Ihre Münzen**: Verteilen Sie Ihre Chips auf mehrere seriöse Münzstätten, um das Risiko zu streuen.
- Beträge begrenzen**: Verwenden Sie Macadamia als physisches wallet für tägliche Zahlungen, nicht als Safe.
- Sichern Sie Ihr seed**: Bewahren Sie Ihren 12-Wörter-Satz auf Papier an einem sicheren Ort auf. Testen Sie die Wiederherstellung gelegentlich.
- Prüfen Sie Münzen**: Informieren Sie sich auf cashu.space und in den Community-Foren, bevor Sie eine Münzanstalt hinzufügen. Wählen Sie solche mit guter Betriebszeit und einem guten Ruf.
- VPN oder Tor**: Verbergen Sie Ihre IP-Adresse mit VPN/Tor, um die Privatsphäre im Netzwerk zu maximieren.
- Treten Sie der Gemeinschaft bei**: Telegram/Discord Cashu-Gruppen für Updates, Mint-Empfehlungen und Best Practices.



## Schlussfolgerung



Macadamia Wallet bringt die Eigenschaften von physischem Bargeld zum digitalen Bitcoin. Durch die Kombination von Chaum- und Lightning-Blindsignaturen bietet es eine elegante Lösung für die Vertraulichkeit von Transaktionen. Seine native iOS-Schnittstelle macht hochentwickelte kryptografische Technologie zugänglich und bleibt gleichzeitig Open Source und interoperabel mit dem Cashu-Ökosystem.



Das Verwahrungsmodell erfordert Wachsamkeit und gute Sicherheitspraktiken. Richtig eingesetzt, wird Macadamia zu einem unschätzbaren Werkzeug für alltägliche Zahlungen, die Anonymität erfordern, und ergänzt die nicht-verwahrenden Geldbörsen für Ersparnisse.



## Ressourcen



### Offizielle Dokumentation




- Offizielle Website: [macadamia.cash](https://macadamia.cash)
- Macadamia FAQ: [macadamia.cash/faq](https://macadamia.cash/faq)
- GitHub-Quellcode: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Cashu Dokumentation




- Technische Dokumentation: [docs.cashu.space](https://docs.cashu.space)
- Liste der öffentlichen Münzstätten: [bitcoinmints.com](https://bitcoinmints.com)
- Offizielle Website des Protokolls: [cashu.space](https://cashu.space)



### Gemeinschaft




- Telegramm Cashu Gruppe: [t.me/cashu_ecash](https://t.me/cashu_ecash)