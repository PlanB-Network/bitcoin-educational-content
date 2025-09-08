---
name: Blockstream-App - Liquid
description: So konfigurieren Sie die Blockstream-App und verwenden das Liquid Network
---
![cover](assets/cover.webp)


## 1. Einführung


### 1.1 Ziel des Lehrgangs





- In diesem Tutorial wird erklärt, wie die **Blockstream App** für die Verwaltung eines **Bitcoin Liquid** Portfolios verwendet wird, d.h. für Transaktionen, die direkt auf der Bitcoin "Liquid" Side Chain aufgezeichnet werden.
- Es behandelt die Installation, die Erstkonfiguration, die Erstellung eines Software Wallet und die Vorgänge zum Empfangen und Senden von Bitcoins auf Liquid.
- Hinweis: Weitere Anleitungen in den Anhängen behandeln Onchain, Watch-Only und die Desktop-Version.



### 1.2 Zielpublikum





- Einsteiger**: Benutzer, die ihre Bitcoins mit einer intuitiven mobilen Anwendung verwalten möchten, in die das Liquid Network integriert ist.
- Fortgeschrittene Nutzer**: Personen, die die Onchain-Funktionen und Datenschutzoptionen wie Tor oder SPV verstehen wollen.



### 1.3 Einführung in Liquid



**Liquid** ist eine **Sidechain** von Bitcoin, die von **[Blockstream](https://blockstream.com/Liquid/)** entwickelt wurde, um schnellere, mehr Confidential Transactions und erweiterte Funktionen zu bieten, während sie mit dem Haupt-Blockchain Bitcoin verbunden bleibt.



Ein Sidechain ist ein unabhängiger Blockchain, der parallel zu einem Bitcoin betrieben wird und einen Mechanismus verwendet, der als **Zwei-Wege-Peg** bekannt ist. Dieses System sperrt Bitcoins auf den Haupt-Blockchain, um **Liquid-Bitcoins (L-BTC)** zu erzeugen, Token, die auf dem Liquid Network zirkulieren und dabei die Wertgleichheit mit den ursprünglichen Bitcoins beibehalten. Die Gelder können jederzeit an Blockchain Bitcoin zurückgegeben werden.



![image](assets/fr/17.webp)






- (1) Peg-in**: Bitcoins (BTC) werden von der Liquid-Föderation auf dem Haupt-Blockchain gesperrt. Im Gegenzug wird ein entsprechender Betrag an Liquid-Bitcoins (L-BTC), der die Parität zwischen den beiden Ketten gewährleistet, auf dem Blockchain-Liquid ausgegeben und an den Nutzer gesendet.





- (2) Unabhängige Transaktionen** : Die Transaktionen können gleichzeitig und unabhängig voneinander auf dem Haupt-Blockchain (BTC) und dem Sidechain Liquid (L-BTC) ablaufen, je nach den Anforderungen der Benutzer.





- (3) Peg-out**: Der Nutzer schickt Liquid-Bitcoins (L-BTC) zurück an den Liquid-Verbund. Die Föderation schaltet daraufhin eine entsprechende Menge an Bitcoins (BTC) auf dem Haupt-Blockchain frei und überweist sie an den Nutzer.



Liquid stützt sich auf eine **Föderation** von vertrauenswürdigen Teilnehmern (Börsen, anerkannte Bitcoin-Unternehmen), die die Blockvalidierung und die bilaterale Verankerung verwalten. Im Gegensatz zu Blockchain und Bitcoin, die dezentralisiert sind und sich auf Miner stützen, ist Liquid ein **federated** Netzwerk, was bedeutet, dass seine Sicherheit und Verwaltung von diesen Teilnehmern abhängen. Dies bedeutet zwar einen Kompromiss bei der Dezentralisierung, ermöglicht aber eine optimierte Leistung und erweiterte Funktionen.



![image](assets/fr/18.webp)



##### Warum Liquid verwenden?





- Geschwindigkeit**: Transaktionen auf Liquid werden in etwa **1 Minute** bestätigt, im Vergleich zu 10 Minuten oder mehr für Onchain-Transaktionen, dank Blöcken, die jede Minute von einer Föderation von Validatoren generiert werden.
- Erhöhte Vertraulichkeit**: Liquid verwendet **Confidential Transactions**, das den Betrag und die Art der übertragenen Vermögenswerte verbirgt, wodurch die Transaktionen vertraulicher werden (obwohl die Adressen sichtbar bleiben).
- Niedrige Gebühren** : Transaktionen auf Liquid sind im Allgemeinen günstiger, was sie ideal für häufige Überweisungen oder kleine Beträge macht.
- Mehrere Vermögenswerte**: Zusätzlich zu L-BTCs unterstützt Liquid die Ausgabe anderer digitaler Vermögenswerte wie Stablecoins oder Tokens zur Verwendung in bestimmten Anwendungen.
- Anwendungsfälle**: Liquid eignet sich besonders für plattformübergreifende Börsen, schnelle Zahlungen oder Anwendungen, die intelligente Verträge erfordern und gleichzeitig mit der Sicherheit von Bitcoin verbunden bleiben.



**Hinweis: Dieses Tutorial konzentriert sich auf die Verwendung des Liquid über die Blockstream App. Für ein vertieftes Verständnis des Liquid Network finden Sie Ressourcen im Anhang.



### 1.4. Hot Wallet Erinnerung





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: alles Bezeichnungen für eine Anwendung, die auf einem Smartphone, einem Computer oder einem beliebigen mit dem Internet verbundenen Gerät installiert ist und die Verwaltung und Sicherung der privaten Schlüssel eines Bitcoin Wallet ermöglicht.
- Im Gegensatz zu **Hardware-Geldbörsen**, auch bekannt als **Cold-Geldbörsen**, die die Schlüssel offline isolieren, arbeiten Software-Geldbörsen in einer vernetzten Umgebung, was sie anfälliger für Cyberangriffe macht.





- Empfohlene Verwendung** :
    - Ideal für die Verwaltung moderater Mengen von Bitcoin, insbesondere für tägliche Transaktionen.
    - Geeignet für Anfänger oder Nutzer mit begrenztem Vermögen, für die ein Hardware Wallet überflüssig erscheint.





- Beschränkungen**: Weniger sicher für die Aufbewahrung großer Geldbeträge oder langfristiger Ersparnisse. In diesem Fall sollten Sie eine Hardware Wallet wählen.




## 2. Einführung der Blockstream App





- Blockstream App** ist eine mobile (iOS, Android) und Desktop-Anwendung zur Verwaltung von Bitcoin-Wallets und Assets auf dem Liquid Network. Sie wurde 2016 von [Blockstream] (https://blockstream.com/) übernommen und hieß zuvor *Green Address* und dann *Blockstream Green*.
- Hauptmerkmale** :
    - Onchain**-Transaktionen auf Blockchain Bitcoin.
    - Transaktionen über das **Liquid**-Netz (Sidechain für schnellen, vertraulichen Austausch).
    - Watch-only**-Portfolios zur Überwachung von Fonds ohne Zugang zu Schlüsseln.
    - Datenschutzoptionen: Verbindung über **Tor**, Verbindung zu einem **persönlichen Knoten** über Electrum oder **SPV**-Verifizierung, um die Abhängigkeit von Drittanbieter-Knoten zu verringern.
    - Funktionen **Replace-by-fee (RBF)** zur Beschleunigung unbestätigter Transaktionen.
- Kompatibilität**: Integriert Hardware-Wallets wie z. B. **Blockstream Jade**.
- Interface**: Intuitiv für Anfänger, mit erweiterten Optionen für Experten.
- Anmerkung**: Dieser Leitfaden konzentriert sich auf die Verwendung von Onchain. Andere Anleitungen in den Anhängen behandeln Onchain, Watch-Only und die Desktop-Version.




## 3. Installieren und Konfigurieren der Blockstream App



### 3.1. Herunterladen





- Für Android** :
    - Laden Sie [Blockstream App] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) aus dem Google Play Store herunter.
    - Alternativ: Installieren Sie über die APK-Datei, die auf [Blockstreams offiziellem GitHub](https://github.com/Blockstream/green_android) verfügbar ist.
- Für iOS** :
    - Laden Sie [Blockstream App] (https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) aus dem App Store herunter.
- Hinweis**: Achten Sie darauf, von offiziellen Quellen herunterzuladen, um betrügerische Anwendungen zu vermeiden.



### 3.2. Erstkonfiguration





- Startbildschirm**: Beim ersten Öffnen zeigt die Anwendung einen Bildschirm ohne konfiguriertes Wallet. Erstellte oder importierte Portfolios werden später hier angezeigt.



![image](assets/fr/02.webp)





- Einstellungen anpassen**: Klicken Sie auf "Anwendungseinstellungen", passen Sie die Optionen unten an, klicken Sie auf "Speichern", starten Sie die Anwendung neu und erstellen Sie Ihr Portfolio.



![image](assets/fr/03.webp)



#### 3.2.1. Verbesserter Datenschutz (nur Android)





- Funktion**: Deaktiviert Bildschirmfotos, blendet die Anwendungsvorschau im Task-Manager aus und sperrt den Zugriff, wenn das Telefon gesperrt ist.
- Warum?** : Schützt Ihre Daten vor unbefugtem physischen Zugriff oder Malware, die den Bildschirm abfängt.



#### 3.2.2. Verbindung über Tor





- Funktion**: Leiten Sie den Netzwerkverkehr über **Tor**, ein anonymes Netzwerk, das Ihre Verbindungen verschlüsselt.
- Warum?**: Verbergen Sie Ihre IP Address und schützen Sie Ihre Privatsphäre, ideal, wenn Sie Ihrem Netzwerk nicht vertrauen (z. B. öffentliches WLAN).
- Nachteil**: Kann die Anwendung aufgrund der Verschlüsselung verlangsamen.
- Empfehlung**: Aktiviere Tor, wenn Vertraulichkeit eine Priorität ist, aber teste die Verbindungsgeschwindigkeit.



#### 3.2.3. Verbinden mit einem persönlichen Knoten





- Funktion**: Verbindet die Anwendung mit Ihrem eigenen **kompletten Bitcoin-Knoten** über einen **Electrum-Server**.
- Warum?**: Ermöglicht die vollständige Kontrolle über Blockchain-Daten und beseitigt die Abhängigkeit von Blockstream-Servern.
- Voraussetzung**: Ein konfigurierter Bitcoin-Knoten.
- Empfehlung**: Fortgeschrittene Benutzer, die maximale Souveränität wünschen.



#### 3.2.4. SPV-Überprüfung





- Funktion**: Verwendet **Simplified Payment Verification (SPV)**, um bestimmte Blockchain-Daten direkt zu überprüfen, ohne die gesamte Kette herunterzuladen.
- Warum?**: Verringert die Abhängigkeit vom Standardknoten von Blockstream und bleibt gleichzeitig leichtgewichtig für mobile Geräte.
- Nachteil**: Weniger sicher als ein Full node, da er für einige Informationen auf Knotenpunkte von Dritten angewiesen ist.
- Empfehlung**: Aktivieren Sie SPV, wenn Sie keinen persönlichen Knoten verwenden können, sondern einen Full node für optimale Sicherheit bevorzugen.





## 4. Erstellung eines Bitcoin-Onchain-Portfolios



### 4.1. Erstellung starten





- Vorsicht**: Legen Sie Ihr Portfolio in einer privaten Umgebung an, ohne Kameras oder Beobachter.
- Klicken Sie auf dem Startbildschirm auf "Erste Schritte":



![image](assets/fr/04.webp)





- Wenn Sie einen **Cold Wallet** (offline Wallet) verwalten möchten: Klicken Sie auf **"Connect Jade "**, um den Hardware Wallet Blockstream Jade oder andere kompatible Cold Wallets zu verwenden.



![image](assets/fr/05.webp)






- Der nächste Bildschirm erscheint:



![image](assets/fr/06.webp)






- (1) **"Mobiles Wallet einrichten "** : Erstellen Sie einen neuen Hot Wallet (Hot Wallet).
- (2) **"Wiederherstellen aus Backup "**: Importieren Sie ein bestehendes Portfolio mit einer Mnemonic Phrase (12 oder 24 Wörter). Achtung! Importieren Sie die Phrase nicht von einem Cold Wallet, da sie auf einem angeschlossenen Gerät offengelegt wird, wodurch die Sicherheit beeinträchtigt wird.
- (3) **"Nur beobachten "**: Importieren Sie ein bestehendes schreibgeschütztes Portfolio, um den Saldo (z. B. Ihres Cold Wallet) zu sehen, ohne den Mnemonic-Satz anzuzeigen. Siehe das "Nur beobachten"-Tutorial im Anhang.



**In diesem Tutorial**: Klicken Sie auf **"Setup Mobile Wallet"**, um einen Hot zu erstellen.


Ihr Wallet wird automatisch erstellt und die Wallet-Startseite, hier "Mein Wallet 5" genannt, wird angezeigt:



![image](assets/fr/07.webp)



**Wichtig**: Die Blockstream App hat die Erstellung eines Wallet vereinfacht, indem sie den 12-Wort-seed-Satz nicht mehr automatisch anzeigt. *Auch wenn das Portfolio jetzt mit einem Klick erstellt wird, riskieren Sie, den Zugriff auf Ihre Fonds zu verlieren, wenn Sie Ihre seed-Phrase* nicht speichern.



### 4.2. seed-Satz speichern





- Klicken Sie auf dem Startbildschirm des Wallet auf die Registerkarte "Sicherheit" und dann auf die Eingabeaufforderung "Sichern" oder das Menü "Wiederherstellungsphrase":



![image](assets/fr/08.webp)



Der seed-Satz mit 12 Wörtern wird angezeigt, damit Sie ihn speichern können.





- Schreiben Sie Ihren Wiederherstellungssatz mit äußerster Sorgfalt auf. Schreiben Sie ihn auf Papier oder Metall und bewahren Sie ihn an einem sicheren Ort auf (sicherer Offline-Ort). Diese Phrase ist Ihr einziges Mittel, um auf Ihre Bitcoins zuzugreifen, falls Sie Ihr Gerät verlieren oder die Anwendung gelöscht wird.
- Es ist auch wichtig zu wissen, dass jeder, der diesen Satz kennt, alle Ihre Bitcoins stehlen kann. Bewahren Sie sie niemals digital auf:
 - Kein Bildschirmfoto
 - Keine Cloud-, E-Mail- oder Messaging-Backups
 - Kein Kopieren/Einfügen (Gefahr des Speicherns in der Zwischenablage)



**! Dieser Punkt ist kritisch**. Weitere Informationen zur Datensicherung :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. seed-Satz prüfen



Bevor Sie Mittel an einen Address senden, der mit diesem seed-Satz verbunden ist, müssen Sie die Sicherung Ihrer 12 Wörter testen.


Dazu schreiben wir einen Verweis auf, löschen Wallet, stellen es mit dem Backup wieder her und prüfen, ob der Verweis unverändert ist.





- Klicken Sie auf dem Wallet-Startbildschirm auf die Registerkarte "Einstellungen" und dann auf "Wallet-Details", und kopieren Sie den zPub ([erweiterter öffentlicher Schlüssel](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f):



![image](assets/fr/09.webp)



Hinweis: Ein zpub Address kann in Ihre Blockstream-Anwendung für die Funktion "Nur beobachten" importiert werden (siehe Anhang).





- Löschen Sie die Anwendung, stellen Sie dann den Wallet über **"Restore from Backup "** wieder her, indem Sie den Mnemonic-Satz eingeben, und prüfen Sie, ob der zpub unverändert ist. Wenn ja, ist Ihre Sicherung korrekt, und Sie können Mittel an den Wallet senden.





- Wenn Sie mehr darüber erfahren möchten, wie Sie einen Wiederherstellungstest durchführen, finden Sie hier eine entsprechende Anleitung:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Sicherung des Zugangs zur Anwendung



Sperren Sie den Zugriff auf die Anwendung mit einem starken PIN-Code:




- Gehen Sie auf dem Wallet-Startbildschirm auf **"Sicherheit "** und klicken Sie dann auf **"PIN "**
- Geben Sie **einen zufälligen 6-stelligen PIN-Code** ein und bestätigen Sie ihn.



**Biometrische Option**: Erhältlich für zusätzlichen Komfort, aber weniger sicher als ein robuster PIN-Code (Risiko des unbefugten Zugriffs, z. B. Fingerabdruck oder Gesichtsscan im Schlaf).



**Hinweis**: Die PIN sichert das Gerät, aber nur der seed-Satz kann verwendet werden, um Gelder wiederherzustellen.





## 5. Verwendung des Liquid Wallet



### 5.1. Erhalten Sie "L-BTC"-Bitcoins



Um Liquid-Bitcoins (L-BTC) zu erhalten, gibt es mehrere Möglichkeiten. Sie können jemanden bitten, Ihnen direkt welche zu schicken, indem Sie einen Liquid, der Address empfängt, teilen, wie unten beschrieben.



Alternativ Exchange Ihre Bitcoins onchain oder über die Lightning Network für L-BTC mit [eine Brücke wie Boltz] (https://boltz.Exchange/): Geben Sie Ihre Liquid erhalten Address, die Zahlung, wie Sie wollen, und erhalten Sie Ihre L-BTC.





- Klicken Sie auf der Startseite des Portfolios auf **Transact**" und dann auf **"Receive "**.



![image](assets/fr/19.webp)





- Standardmäßig zeigt die Anwendung eine leere **Quittung Address, onchain** (SegWit v0-Format, beginnend mit `bc1q...`). Klicken Sie auf "Bitcoin", um **Liquid Bitcoin** auszuwählen:



![image](assets/fr/20.webp)





- Optionen** :
 - (1) Klicken Sie auf die Pfeile, um einen anderen neuen Address auszuwählen, der mit diesem seed-Satz verknüpft ist.
    - (2) Sie können auch ein Address aus den bereits verwendeten/angezeigten Adressen auswählen, indem Sie auf die drei Punkte oben rechts und dann auf "Liste der Adressen" klicken
    - (3) Um einen bestimmten Betrag anzufordern, klicken Sie auf die drei Punkte oben rechts, wählen "Betrag anfordern" und geben den gewünschten Betrag ein. Der QR wird aktualisiert, und die Address wird durch eine Bitcoin-Zahlungs-URI ersetzt.



![image](assets/fr/21.webp)





- Teilen Sie den Address/URI, indem Sie auf "**Teilen**" klicken, den Text kopieren oder den QR-Code scannen.
- Verifizierung**: Überprüfen Sie den Address, der mit dem Empfänger geteilt wurde, so weit wie möglich, um Fehler oder Angriffe zu vermeiden (z. B. Malware, die die Zwischenablage verändert).



### 5.2. Bitcoins senden





- Klicken Sie auf der Startseite des Portfolios auf "**Transaktion**" und dann auf **"Senden "**:



![image](assets/fr/22.webp)





- Details eingeben** :
    - (1) Geben Sie den **Address des Empfängers** ein, indem Sie ihn aufkleben oder einen QR-Code scannen.
    - (2) Überprüfen Sie die Vermögenswerte und das Konto, von dem die Gelder überwiesen werden.
    - (3) Geben Sie den zu überweisenden **Betrag** an. Sie können die Einheit wählen: L-BTC, L-Satoshis, USD, ...



![image](assets/fr/23.webp)





- Prüfen** :
    - Überprüfen Sie die Address, den Betrag und die Gebühren auf dem Übersichtsbildschirm.
    - Ein Address-Fehler kann zu einem unwiderruflichen Verlust von Geldern führen. Hüten Sie sich vor Malware, die die Zwischenablage modifiziert.



![image](assets/fr/24.webp)





- Bestätigen**: Klicken Sie auf die Schaltfläche "Senden", um die Transaktion zu unterzeichnen und zu verteilen.
- Weiterverfolgung**: Auf der Registerkarte Wallet "Vorgang" erscheint die Transaktion als "Unbestätigt", dann "Bestätigt" und schließlich "Abgeschlossen":



![image](assets/fr/25.webp)





- Die Zeit zwischen 2 Blöcken beträgt bei Liquid 1 Minute, so dass die Transaktion schnell bestätigt und abgeschlossen wird.




## Anhänge



### A1. Andere Tutorials zur Blockstream App



Nutzung des Onchain-Netzwerks



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Importieren und Verfolgen eines Wallet im "Nur beobachten"-Modus



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Desktop-Version



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. Bewährte Praktiken



Um **Blockstream App** sicher und effizient zu nutzen, befolgen Sie diese Empfehlungen. Sie werden Ihnen helfen, Ihr Geld zu schützen, Ihre Transaktionen zu optimieren und Ihre Vertraulichkeit in den **Bitcoin (onchain)**, **Liquid** und **Lightning** Netzwerken zu wahren.





- Sichern Sie Ihre Wiederherstellungsphrase** :
 - Anleitung: Speichern des Mnemonic-Satzes



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Verwenden Sie eine sichere Authentifizierung** :
 - Aktivieren Sie eine **starke PIN** oder **biometrische Authentifizierung** (Fingerabdruck oder Gesichtserkennung), um den Zugang zur Anwendung zu schützen.
 - Geben Sie niemals Ihre PIN oder biometrischen Daten weiter.





- Schützen Sie Ihre Privatsphäre** :
 - generate ein neues Address für jeden Onchain-Empfang oder Liquid zur Begrenzung der Rückverfolgung auf dem Blockchain.
 - Aktivieren Sie die Funktionen "Verbesserter Datenschutz", "Tor" und "SPV".
 - Für maximale Vertraulichkeit sollten Sie Ihren Wallet über einen Electrum-Server mit Ihrem eigenen Bitcoin-Knoten verbinden, anstatt den öffentlichen Knoten zu verwenden





- Wählen Sie das für Ihre Bedürfnisse am besten geeignete Netz**:
 - Onchain**: Bevorzugt für langfristige Verwahrung oder Transaktionen mit hohem Wert (Gebühren im Verhältnis zum Betrag vernachlässigbar).
 - Liquid**: Für schnelle, kostengünstige Überweisungen mit erhöhter Vertraulichkeit.
 - Lightning**: Wählen Sie sofortige, kostengünstige Überweisungen für kleine Beträge.





- Überprüfen Sie immer die Lieferadressen** :
 - Überprüfen Sie das Address sorgfältig, bevor Sie Geldmittel senden. Gelder, die an einen falschen Address gesendet werden, sind für immer verloren. Verwenden Sie Kopieren/Einfügen oder QR-Code-Scannen, kopieren/verändern Sie niemals einen Address von Hand.





- Kosten optimieren** :
 - Wählen Sie für Onchain-Transaktionen je nach Dringlichkeit und Netzüberlastung geeignete Gebühren (langsam, mittel, schnell).
 - Verwenden Sie Liquid oder Lightning für kleine Mengen.





- Halten Sie die Anwendung auf dem neuesten Stand




### A3. Zusätzliche Ressourcen





- Offizielle Links:**
 - [Offizielle Website](https://blockstream.com/)**
 - [Support für die mobile Anwendung](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : Dokumentation und Chat
 - [GitHub](https://github.com/Blockstream/green_android)**





- Block Explorers :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Blitzschlag: **[1ML (Lightning Network)](https://1ml.com/)**





- Lernen und Tutorien:** **[Plan ₿ Network](https://planb.network/)** :
 - Sicherung des Wiederherstellungssatzes



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Glossar](https://planb.network/fr/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Glossar](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
