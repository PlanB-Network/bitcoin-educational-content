---
name: Misty Breez
description: Der bogenlose Lightning Wallet.
---

![misty-breez-cover](assets/cover.webp)



Misty Breez ist ein selbsthaltender Lightning Wallet, der von Breez auf der Grundlage ihres Software Development Kit und des von BlockStream entwickelten **Liquid**-Netzwerks entwickelt wurde.


Es bietet einen völlig neuen Ansatz für den Betrieb ohne einen Lightning-Knoten: ein potenzieller **GAME CHANGER** für Bitcoin-Übertragungen zwischen Netzwerken.


In diesem Tutorial beschreiben wir, wie dieses Portfolio funktioniert und geben Ihnen einen vollständigen Überblick.



## Wie funktioniert Misty Breez?



Misty Breez ist eine Implementierung ohne einen Lightning-Knoten als Backend. Sie wurde auf der Grundlage von Breez SDK und Liquid entwickelt.



Liquid ist ein paralleles Layer zum Bitcoin-Netz, das erhebliche Verbesserungen bei Geschwindigkeit und Transaktionskosten bietet. Mit diesem Layer kann Misty Breez auf einen Lightning-Knoten verzichten und stattdessen Exchange-Dienste von Drittanbietern wie **Boltz** nutzen, um die Interoperabilität zwischen dem Liquid Network und dem Lightning Network sicherzustellen. Keine Eile, wir werden darauf zurückkommen.



Beginnen wir also unser Abenteuer mit dem Misty Breez Wallet.



## Erste Schritte mit Misty Breez



Die Misty Breez Mobile App ist auf offiziellen Download-Plattformen wie Google Play Store (für Android) und Apple Store (für iOS) verfügbar. Sie können auch über die offizielle [Misty Breez]-Website (https://breez.technology/misty/) zur richtigen App weitergeleitet werden.



⚠️ Achten Sie darauf, dass Sie Misty Breez nicht mit dem Breez Wallet verwechseln.



⚠️ **WICHTIG**: Für die Sicherheit Ihrer Bitcoins ist es wichtig, die Anwendung von offiziellen Plattformen herunterzuladen, um ihre Authentizität zu gewährleisten.



![download-misty-breez](assets/fr/01.webp)



In diesem Lernprogramm beginnen wir mit einem Android-Gerät. Dennoch gelten alle Schritte und spezifischen Funktionen, die in diesem Abschnitt beschrieben werden, auch für iOS.



Nach der Installation bietet Misty Breez Ihnen die Möglichkeit, einen neuen Wallet zu erstellen oder einen alten Lightning Wallet wiederherzustellen, für den Sie die Wiederherstellungswörter haben.


In diesem Tutorial entscheiden wir uns für die Erstellung eines neuen Portfolios.



⚠️Misty Breez befindet sich derzeit in der Entwicklungsphase, daher raten wir Ihnen, mit angemessenen Beträgen zu beginnen.



![create-wallet](assets/fr/02.webp)


### Speichern Sie Ihre Genesungswünsche:


Eines der ersten Dinge, die Sie bei der Erstellung eines neuen Portfolios tun sollten, ist, Ihre 12 Wiederherstellungswörter zu sichern.


Hier sind einige Tipps, wie Sie Ihren Sicherungssatz sichern können.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Um Ihre Phrasen zu sichern, wählen Sie das Menü **Einstellungen > Sicherheit** und dann die Option **Sicherungsphrase prüfen**.



![backup](assets/fr/03.webp)


Für zusätzliche Sicherheit können Sie auch **einen PIN-Code** erstellen, um den Zugang zu Ihrem Wallet zu authentifizieren.




Finden Sie Ihre lokale Währung in der Vielzahl der von Misty Breez akzeptierten Währungen. Konfigurieren Sie Ihre Währung über das Menü **Einstellungen > Fiat-Währungen** und wählen Sie dann die gewünschte(n) Währung(en) aus.



![devises](assets/fr/04.webp)



### Erste Transaktionen durchführen


Wenn Sie bereits mit dem Breez-Portfolio vertraut sind, wird Sie der intuitive Interface von Misty Breez nicht im Geringsten abschrecken.



Klicken Sie im Interface-Menü **Bilanz** auf die Option **Empfangen**, um Rechnungen zu erstellen und Ihre Bitcoins auf Ihrem Wallet zu empfangen.



⚠️ Misty Breez bittet Sie, in den Einstellungen Ihres Telefons Benachrichtigungen für die Anwendung zu aktivieren, damit Sie Anspruch auf einen Lightning Address haben.



Mit Misty Breez können Sie :




- Erhalten Sie Bitcoins auf dem Lightning Network von **100 Satoshis** bis zu **25.000.000 Satoshis**.
- Erhalten Sie Bitcoins im Bitcoin Hauptnetzwerk ab **25.000 Satoshis**.



![transactions](assets/fr/05.webp)



Hier beginnt der Zauber von Misty Breez.


Im Gegensatz zu Breez Wallet, das Ihnen einen Blitzknoten zur Verfügung stellt und Sie auffordert, die Kosten für das Öffnen und Schließen von Zahlungskanälen selbst zu tragen, verlangt Misty Breez nichts von Ihnen. Wie bereits erwähnt, funktioniert Misty Breez nicht einmal auf der Grundlage eines Lightning-Knotens.



Werfen wir einen genaueren Blick hinter die Kulissen.



In Wirklichkeit besitzen Sie ein Liquid-Portfolio, das mit Ihrem Misty Breez-Portfolio verbunden ist. Logischerweise handhaben Sie L-BTC (Liquid Bitcoin) zu festen Kursen, die mit U-Boot-Satoshis-Umwandlungsdiensten von Drittanbietern verbunden sind, die Ihnen die Interoperabilität mit dem Lightning Network ermöglichen.



Wenn Sie eine Zahlung auf Ihrem Misty Breez Wallet erhalten, sendet Ihnen Ihr Absender Satoshis, die durch einen Konvertierungsdienst wie Boltz (derzeit von Misty Breez verwendet) gehen, um die gesendeten Satoshis in L-BTC umzuwandeln, die auf Ihrem Misty Breez Wallet (verbunden Liquid Wallet) empfangen werden.


Hier ist ein vereinfachtes Diagramm des Prozesses hinter den Kulissen.



![lnswap-in](assets/fr/06.webp)



Klicken Sie auf die Interface im Menü **Saldo**, klicken Sie auf die Option **Senden**, um eine Blitz-Invoice zu bezahlen.


Stecken Sie das Lightning Invoice, das Lightning Address Ihres Empfängers ein oder scannen Sie einfach den QR-Code auf dem Invoice, um Ihre Zahlung durchzuführen.



![send-bitcoins](assets/fr/07.webp)



Hinter den Kulissen aktivieren Sie den Liquid Wallet, der mit Ihrem Misty Breez Wallet verbunden ist, um den Gegenwert von L-BTC über Boltz in Satoshis umzuwandeln, und übertragen diese Satoshis dann auf den Lightning Wallet des Empfängers (der sich auf dem Lightning Network befindet).



![send-bitcoin-bts](assets/fr/08.webp)



Diese Funktion der Infrastruktur von Misty Breez ermöglicht es den Benutzern, Transaktionen durchzuführen, auch wenn Misty Breez offline ist.



Für die Erfahreneren gibt es auch ein Menü **Einstellungen > Entwickler**, das Ihnen ein wenig mehr Details über :




- Die Version des Breez Software Development Kit.
- Der öffentliche Schlüssel Ihres Misty Breez Wallet.
- Der Kreditnehmer, die eindeutige Kennung, die aus dem primären öffentlichen Schlüssel abgeleitet wird.
- Ihr Portfoliosaldo.
- Tipp Liquid, für das Versenden von kleinen Beträgen von L-BTC.
- Die Bitcoin-Spitze, um kleine Mengen von Bitcoin zu versenden.



Sie können auch bestimmte Aktionen durchführen, wie z. B. die Synchronisierung mit dem Liquid Network, die Sicherung Ihrer Schlüssel, die Freigabe Ihres Aktivitätsprotokolls und die Auswahl eines neuen Scans des Liquid Network.



![dev-mode](assets/fr/09.webp)


Herzlichen Glückwunsch! Sie haben nun ein gutes Verständnis für das Misty Breez-Portfolio und seinen Beitrag zu Bitcoin netzübergreifenden Transaktionen. Wenn Sie dieses Tutorial nützlich fanden, geben Sie uns bitte einen Green-Daumen. Wir würden uns freuen, von Ihnen zu hören.



Um weiter zu gehen, empfehle ich auch, dass Sie unser Tutorial über die Aqua Wallet, die in ähnlicher Weise wie Misty Breez funktioniert entdecken:



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125