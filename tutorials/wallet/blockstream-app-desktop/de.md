---
name: Blockstream App - Desktop
description: Wie verwende ich mein Hardware Wallet mit der Blockstream App auf einem Computer?
---
![cover](assets/cover.webp)



## 1. Einführung



### 1.1 Ziel des Lehrgangs





- In dieser Anleitung wird erklärt, wie man die **Blockstream App** auf einem Computer verwendet, um einen Bitcoin **onchain** Wallet mit einem **Hardware Wallet** zu verwalten und so sichere Transaktionen zu ermöglichen, die auf dem Haupt-Blockchain Bitcoin aufgezeichnet werden.
- Es behandelt die Installation, die Erstkonfiguration, den Anschluss eines Hardware Wallet und den Empfang und Versand von Onchain-Bitcoins.
- Hinweis: Weitere Anleitungen in den Anhängen behandeln Liquid, Nur-Überwachung und die mobile Anwendung.



### 1.2 Zielpublikum





- **Einsteiger**: Benutzer, die ihre Bitcoins mit einer sicheren Desktop-Software und einem Hardware Wallet verwalten möchten.
- **Fortgeschrittene Nutzer**: Personen, die verstehen möchten, wie man einen Hardware Wallet für Onchain-Transaktionen und Datenschutzoptionen wie Tor oder SPV verwendet.



### 1.3. Hintergrund zu Hardware-Geldbörsen





- **Hardware Wallet**, **Cold Wallet**: Ein physisches Gerät, das private Schlüssel offline speichert und im Gegensatz zu **Hot-Geldbörsen** (Software-Geldbörsen auf angeschlossenen Geräten) ein hohes Maß an Sicherheit vor Cyberangriffen bietet.
- **Empfohlene Verwendung**:
    - Ideal für die Sicherung großer Beträge oder langfristiger Ersparnisse.
    - Geeignet für sicherheitsbewusste Nutzer, die ihr Geld vor den Risiken schützen wollen, die mit vernetzten Geräten verbunden sind.
- **Beschränkungen**: Erfordert Software wie die Blockstream App, um Salden, generate-Adressen anzuzeigen und Hardware Wallet-signierte Transaktionen zu übertragen.



## 2. Einführung der Blockstream App





- **Blockstream App** ist eine mobile (iOS, Android) und Desktop-Anwendung für die Verwaltung von Bitcoin-Geldbörsen und Assets auf dem Liquid Network. Sie wurde 2016 von Blockstream übernommen und hieß zunächst *GreenAddress*, wurde dann in *Blockstream Green* (2019) umbenannt und heißt jetzt *Blockstream app* (2025).
- **Hauptmerkmale**:
- **Onchain-Transaktionen** auf Blockchain Bitcoin.
    - Transaktionen über das **Liquid**-Netz (Sidechain für schnellen, vertraulichen Austausch).
- **Watch-only**-Portfolios zur Überwachung von Fonds ohne Zugang zu Schlüsseln.
    - Datenschutzoptionen: Verbindung über **Tor**, Verbindung zu einem **persönlichen Knoten** über Electrum oder **SPV**-Verifizierung, um die Abhängigkeit von Drittanbieter-Knoten zu verringern.
    - Funktionen **Replace-by-fee (RBF)** zur Beschleunigung unbestätigter Transaktionen.
- **Kompatibilität**: Integriert Hardware-Wallets wie z. B. **Blockstream Jade**.
- **Interface**: Intuitiv für Anfänger, mit erweiterten Optionen für Experten.
- **Anmerkung**: Dieser Leitfaden konzentriert sich auf die Verwendung von onchain mit einem Hardware Wallet in der Desktop-Version. Andere Anleitungen, die als Anhänge zur Verfügung gestellt werden, behandeln die Verwendung auf mobilen Anwendungen, für onchain, Liquid und Watch-Only-Funktionen.



## 3. Installieren und Einrichten von Blockstream App Desktop



### 3.1. Herunterladen





- Gehen Sie auf die [offizielle Website](https://blockstream.com/app/) und klicken Sie auf "_Jetzt herunterladen_". Laden Sie die Version herunter, die Ihrem Betriebssystem entspricht (Windows, macOS, Linux).
- **Hinweis**: Achten Sie darauf, von der offiziellen Quelle herunterzuladen, um betrügerische Software zu vermeiden.



### 3.2. Erstkonfiguration





- **Startbildschirm**: Beim ersten Öffnen zeigt die Anwendung einen Bildschirm ohne konfigurierte Wallet. Erstellte oder importierte Portfolios werden später hier angezeigt.



![image](assets/fr/02.webp)





- **Anpassen der Einstellungen**: Klicken Sie auf das Einstellungssymbol unten links, passen Sie die Optionen unten an und verlassen Sie Interface, um fortzufahren.



![image](assets/fr/03.webp)



#### 3.2.1. Allgemeine Parameter





- Klicken Sie im Menü "Einstellungen" auf "**Allgemein**".
- **Funktion**: Ändern Sie die Sprache der Software und aktivieren Sie bei Bedarf experimentelle Funktionen.



![image](assets/fr/04.webp)



#### 3.2.2. Verbindung über Tor





- Klicken Sie im Menü "Einstellungen" auf "**Netzwerk**".
- **Funktion**: Leiten Sie den Netzwerkverkehr über **Tor**, ein anonymes Netzwerk, das Ihre Verbindungen verschlüsselt.
- **Warum?**: Verbergen Sie Ihre IP Address und schützen Sie Ihre Privatsphäre, ideal, wenn Sie Ihrem Netzwerk nicht vertrauen (z. B. öffentliches WLAN).
- **Nachteil**: Kann die Anwendung aufgrund der Verschlüsselung verlangsamen.
- **Empfehlung**: Aktiviere Tor, wenn Vertraulichkeit eine Priorität ist, aber teste die Verbindungsgeschwindigkeit.



![image](assets/fr/05.webp)



#### 3.2.3. Verbinden mit einem persönlichen Knoten





- Klicken Sie im Menü Einstellungen auf "**Benutzerdefinierte Server und Validierung**".
- **Funktion**: Verbindet die Anwendung mit Ihrem eigenen **kompletten Bitcoin-Knoten** über einen **Electrum-Server**.
- **Warum?**: Ermöglicht die vollständige Kontrolle über Blockchain-Daten und beseitigt die Abhängigkeit von Blockstream-Servern.
- **Voraussetzung**: Ein konfigurierter Bitcoin-Knoten.
- **Empfehlung**: Fortgeschrittene Benutzer, die maximale Souveränität wünschen.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. SPV-Überprüfung





- Klicken Sie im Menü Einstellungen auf "**Benutzerdefinierte Server und Validierung**".
- **Funktion**: Verwendet **Simplified Payment Verification (SPV)**, die Block-Header herunterlädt und Ihre Transaktionen durch einen Einschlussnachweis (Merkle) verifiziert, ohne die vollständige Blockchain zu speichern.
- **Warum?**: Verringert die Abhängigkeit vom Blockstream-Standardknoten und bleibt gleichzeitig leichtgewichtig für Geräte.
- **Nachteil**: Weniger sicher als ein Full node, da es für einige Informationen auf Knotenpunkte von Drittanbietern angewiesen ist.
- **Empfehlung**: Aktivieren Sie SPV, wenn Sie keinen persönlichen Knoten verwenden können, aber einen Full node für optimale Sicherheit bevorzugen.



![image](assets/fr/07.webp)



## 4. Verbinden eines Hardware Wallet mit der Blockstream App



### 4.1. Vorüberlegungen



#### 4.1.1. Für Ledger-Benutzer





- Blockstream Green unterstützt nur die **Bitcoin Legacy** Anwendung auf Ledger Geräten (Nano S, Nano X).
- Befolgen Sie die Schritte in **Ledger Live**, bevor Sie Ihr Gerät anschließen:


1. Gehen Sie zu **"Einstellungen "** → **"Experimentelle Funktionen "** und aktivieren Sie den **Entwicklermodus**.


2. Gehen Sie zu **"Mein Ledger"** → **"App-Katalog "**, und installieren Sie die Anwendung **Bitcoin Legacy**


3. Öffnen Sie die Anwendung **Bitcoin Legacy** auf Ihrem Ledger, bevor Sie Blockstream Green starten, um die Verbindung herzustellen.




- **Hinweis**: Stellen Sie sicher, dass Ihr Ledger mit Ihrem PIN-Code freigeschaltet ist und dass die Bitcoin Legacy-Anwendung aktiv ist, wenn Sie eine Verbindung herstellen.



#### 4.1.2 Initialisierung eines Hardware Wallet





- Wenn Ihr Hardware Wallet (Ledger, Trezor oder Blockstream Jade) noch nie benutzt wurde (entweder mit Blockstream Green oder mit einer anderen Software wie Ledger Live), müssen Sie es zunächst initialisieren. Dieser Schritt erfolgt in einer sicheren Umgebung, ohne Kameras oder Beobachter:


1. **seed phrase generation / Mnemonic phrase** (12, 18 oder 24 Wörter): Schreiben Sie sie sorgfältig auf ein Blatt Papier.


2. **seed Phrasenüberprüfung**: Testen Sie den Wallet-Import aus den notierten Wörtern, z. B. durch Verifizierung des erweiterten öffentlichen Schlüssels. Durchzuführen, bevor Mittel an Wallet gesendet werden und der seed-Satz dauerhaft gesichert wird.


3. **Sicherung des seed-Satzes**: Bewahren Sie den Satz auf einem physischen Medium (Papier oder Metall) und an einem sicheren Ort auf. Speichern Sie ihn niemals digital (keine Screenshots, Cloud oder E-Mail).




- **Wichtig**: Der seed-Satz ist Ihre einzige Möglichkeit, Ihr Geld wiederzuerlangen, wenn das Gerät verloren geht oder eine Fehlfunktion hat. Jeder, der Zugang hat, kann Ihre Bitcoins stehlen.
- **Ressourcen** zum Sichern und Überprüfen des seed-Satzes:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Konfiguration für dieses Lernprogramm :





- Wir gehen davon aus, dass das Hardware Wallet bereits mit einer seed-Phrase und einem Sperr-PIN-Code initialisiert worden ist.
- Wir gehen davon aus, dass das Hardware Wallet noch nie mit der Blockstream App verbunden war, was die Erstellung eines neuen Kontos erfordert. Wenn das Hardware Wallet bereits mit der Blockstream App verwendet wurde, wird das Konto automatisch angezeigt, wenn die Anwendung geöffnet wird.



### 4.2. Verbindung starten





- Klicken Sie auf dem Startbildschirm auf "**Neues Wallet einrichten**", bestätigen Sie dann die Geschäftsbedingungen und klicken Sie auf "**Starten**":



![image](assets/fr/08.webp)





- Wählen Sie die Option "**Auf Hardware Wallet**":



![image](assets/fr/09.webp)





- Wenn Sie einen **Blockstream Jade** verwenden, klicken Sie auf die entsprechende Schaltfläche. Ansonsten wählen Sie "**Ein anderes Hardware-Gerät anschließen**":



![image](assets/fr/10.webp)





- Schließen Sie Ihr Hardware Wallet über USB an den Computer an und wählen Sie es in der Blockstream-App aus:



![image](assets/fr/22.webp)





- Bitte warten Sie, während die Blockstream App Ihre Portfoliodaten importiert:



![image](assets/fr/23.webp)



### 4.3. Ein Konto erstellen





- Wenn Ihr Hardware Wallet bereits mit der Blockstream App verwendet wurde, wird Ihr Konto nach dem Import automatisch im Interface angezeigt. Andernfalls müssen Sie ein Konto erstellen, indem Sie auf "**Konto erstellen**" klicken:



![image](assets/fr/24.webp)





- Wählen Sie "**Standard**", um ein klassisches Bitcoin-Portfolio zu konfigurieren:



![image](assets/fr/25.webp)





- Sobald Ihr Konto eingerichtet ist, können Sie auf Ihr Interface-Hauptportfolio zugreifen:



![image](assets/fr/26.webp)





## 5. Verwendung des onchain Wallet mit einem Hardware Wallet



### 5.1. Bitcoins erhalten





- Klicken Sie auf dem Hauptbildschirm des Portfolios auf "**Empfangen**":



![image](assets/fr/27.webp)





- Die Anwendung zeigt eine **leere Empfangs-Address** an. Die Verwendung einer neuen Address für jeden Empfang verbessert Ihre Vertraulichkeit. Klicken Sie auf "**Address kopieren**", um die Address zu kopieren, oder lassen Sie den Absender den angezeigten QR-Code scannen:



![image](assets/fr/12.webp)



**Optionen** :




- (1) Klicken Sie auf die Pfeile, um generate ein neues Address mit Ihrem Portfolio zu verknüpfen.
- (2) Um einen bestimmten Betrag anzufordern, klicken Sie auf "**Mehr Optionen**" und dann auf "**Betrag anfordern**". Der QR wird aktualisiert, und der Address wird durch einen Bitcoin-Zahlungs-URI ersetzt, wie z. B.: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Um einen früheren Address wieder zu verwenden, klicken Sie auf "**Weitere Optionen**" und dann auf "**Adressliste**":



![image](assets/fr/14.webp)





- **Überprüfung**: Überprüfen Sie die freigegebene Address sorgfältig, um Fehler oder Angriffe (z. B. Malware, die die Zwischenablage verändert) zu vermeiden.
- Sobald die Transaktion im Netz übertragen wurde, wird sie in Ihrem Wallet angezeigt. Warten Sie 1 bis 6 Bestätigungen ab, um die Transaktion als unveränderbar zu betrachten.



![image](assets/fr/28.webp)



### 5.2. Bitcoins senden





- Klicken Sie auf dem Hauptbildschirm des Portfolios auf "**Senden**".



![image](assets/fr/29.webp)





- **Details eingeben**:
    - (1) Vergewissern Sie sich, dass die ausgewählte Anlage **Bitcoin** (onchain) ist.
    - (2) Geben Sie die **Address des Empfängers** ein, indem Sie sie einfügen oder einen QR-Code mit Ihrer Webcam scannen.
    - (3) Geben Sie den zu sendenden **Betrag** an (in BTC, Satoshis oder anderen Einheiten).




![image](assets/fr/16.webp)





- Wählen Sie **Transaktionsgebühren** (optional) :
 - Wählen Sie je nach Dringlichkeit aus den vorgeschlagenen Optionen (schnell, mittel, langsam) und geben Sie die voraussichtliche Bestätigungszeit an.
 - Für individuelle Gebühren passen Sie die Anzahl der Satoshis pro Vbyte manuell an. Diese werden auf dem Startbildschirm angezeigt. Siehe auch [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- **Manuelle Auswahl von UTXOs** (optional): Klicken Sie auf "**Manuelle Coin-Auswahl**", um die spezifischen UTXOs auszuwählen, die in der Transaktion verwendet werden sollen.



![image](assets/fr/18.webp)





- **Vorläufige Überprüfung**: Überprüfen Sie den Address, den Betrag und die Gebühren auf dem Übersichtsbildschirm und klicken Sie dann auf "**Transaktion bestätigen**". In Wirklichkeit wird die Transaktion erst dann für das Netz freigegeben, wenn Sie sie mit Ihrem Hardware Wallet signiert haben. Nur dieser verfügt über die geheimen Schlüssel, die mit den Adressen verbunden sind, von denen die UTXOs (Satoshis) abgebucht werden.



![image](assets/fr/19.webp)





- **Endkontrolle und Unterschrift**: Vergewissern Sie sich, dass alle Transaktionsparameter **auf Ihrem Hardware Wallet**-Bildschirm korrekt sind, und unterzeichnen Sie die Transaktion dann damit. Ein Address-Fehler kann zu einem unwiderruflichen Verlust von Mitteln führen.





- **Übertragung**: Nach der Unterzeichnung sendet die Blockstream App die Transaktion automatisch an das Bitcoin Netzwerk.



![image](assets/fr/20.webp)





- **Nachbereitung**:
 - Die Transaktion wird auf dem Wallet-Startbildschirm als "ausstehend" angezeigt, bis sie bestätigt wird.
 - Solange die Transaktion noch nicht bestätigt wurde, kann die Funktion **Replace-by-fee (RBF)** verwendet werden, um die Bestätigung durch Erhöhung der Gebühr zu beschleunigen (siehe Anhang).



![image](assets/fr/21.webp)



## Anhänge



### A1. Andere Blockstream-Tutorials





- Verwendung des Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Importieren und verfolgen Sie ein Portfolio im "Watch-Only"-Modus:



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- Verwendung der Blockstream-App auf Handys (Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Erläuterung von Replace-by-fee (RBF)





- **Definition**: Replace-by-fee (RBF) ist eine Funktion des Bitcoin-Netzwerks, die es dem Absender ermöglicht, die Bestätigung einer **onchain**-Transaktion zu beschleunigen, indem er die Gebühr erhöht.
- **Grenzwerte**:
    - RBF ist nicht für Liquid oder Lightning-Transaktionen verfügbar.
    - Die erste Transaktion muss als RBF-kompatibel gekennzeichnet werden, was Blockstream App automatisch tut.
- Weitere Informationen finden Sie unter [unser Glossar] (https://planb.network/resources/glossary/rbf-replacebyfee).



### A3. Bewährte Praktiken





- **Sichern Sie Ihre Wiederherstellungsphrase**:
    - Bewahren Sie Ihren Hardware Wallet- und Mnemonic-Satz auf einem physischen Medium (Papier, Metall) an einem sicheren Ort auf.
    - Speichern Sie sie niemals digital (Cloud, E-Mail, Screenshot).
    - Tutorial: Speichern Sie Ihren Mnemonic-Satz:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Schützen Sie Ihre Privatsphäre** :





    - generate einen neuen Address für jeden Onchain-Empfang.
    - Aktivieren Sie **Tor** oder **SPV**, um die Verfolgung einzuschränken.
    - Verbinden Sie sich mit Ihrem eigenen Bitcoin-Knoten über Electrum für maximale Souveränität.
- **Überprüfen Sie immer die Lieferadressen**:





    - Prüfen Sie den Address auf Ihrem Hardware Wallet-Bildschirm, bevor Sie unterschreiben.
    - Verwenden Sie Kopieren/Einfügen oder einen QR-Code, um manuelle Fehler zu vermeiden.
- **Kosten optimieren**:





    - Anpassung der Gebühren je nach Dringlichkeit und Netzüberlastung (siehe [Mempool.space](https://Mempool.space/)).
    - Verwenden Sie Liquid oder Lightning für schnelle, kostengünstige Transaktionen, die keine Onchain-Sicherheit erfordern.
- **Aktualisieren Sie die Software**:





    - Halten Sie Ihre Blockstream-App und Hardware Wallet-Firmware mit den neuesten Funktionen und Sicherheitspatches auf dem neuesten Stand.



### A4. Zusätzliche Ressourcen





- **Offizielle Links**:
    - [Offizielle Website](https://blockstream.com/)
    - [Unterstützung für Blockstream App](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): Dokumentation und Chat
    - [GitHub](https://github.com/Blockstream/green_qt)





- **Block Explorers**:
    - Onchain : [Mempool.space](https://Mempool.space/)
    - Liquid : [Blockstream Info](https://blockstream.info/Liquid)
    - Blitz : [1ML (Lightning Network)](https://1ml.com/)





- **Sicherung des Wiederherstellungssatzes:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network** :



[Glossar](https://planb.network/fr/resources/glossary/liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Glossar](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb