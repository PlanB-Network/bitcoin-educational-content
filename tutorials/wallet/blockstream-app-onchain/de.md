---
name: Blockstream App - Onchain
description: Blockstream App auf dem Handy einrichten und Onchain-Transaktionen verwalten
---
![cover](assets/cover.webp)


## 1. Einführung


### 1.1 Ziel des Lehrgangs





- In diesem Tutorial wird erklärt, wie die **Blockstream App** mobile Anwendung verwendet wird, um einen Bitcoin **onchain** Wallet zu verwalten, d. h. Transaktionen, die direkt auf dem Haupt-Blockchain Bitcoin aufgezeichnet werden.
- Es umfasst die Installation, die Erstkonfiguration, die Erstellung eines Software Wallet und die Vorgänge zum Empfangen und Senden von Bitcoins.
- Hinweis: Weitere Anleitungen in den Anhängen behandeln Liquid, Nur-Überwachung und die Desktop-Version.



![image](assets/fr/01.webp)



### 1.2 Zielpublikum





- Einsteiger**: Benutzer, die ihre Bitcoins mit einer intuitiven mobilen Anwendung verwalten möchten.
- Fortgeschrittene Nutzer**: Personen, die die Onchain-Funktionen und Datenschutzoptionen wie Tor oder SPV verstehen wollen.



### 1.3. Erinnerungen an Hot-Geldbörsen





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: alles Bezeichnungen für eine Anwendung, die auf einem Smartphone, einem Computer oder einem beliebigen Gerät mit Internetanschluss installiert ist und die Verwaltung und Sicherung privater Schlüssel von einem Bitcoin Wallet ermöglicht.
- Im Gegensatz zu **Hardware-Geldbörsen**, auch bekannt als **Cold-Geldbörsen**, die Schlüssel offline isolieren, arbeiten Software-Geldbörsen in einer vernetzten Umgebung, was sie anfälliger für Cyberangriffe macht.





- Empfohlene Verwendung** :
    - Ideal für die Verwaltung moderater Mengen von Bitcoin, insbesondere für tägliche Transaktionen.
    - Geeignet für Anfänger oder Nutzer mit begrenztem Vermögen, denen ein Hardware Wallet überflüssig erscheint.





- Beschränkungen**: Weniger sicher für die Aufbewahrung großer Geldbeträge oder langfristiger Ersparnisse. Wählen Sie in diesem Fall eine Hardware Wallet.




## 2. Einführung der Blockstream App





- Blockstream App** ist eine mobile (iOS, Android) und Desktop-Anwendung für die Verwaltung von Bitcoin-Portfolios und Assets auf dem Liquid Network. Sie wurde 2016 von [Blockstream] (https://blockstream.com/) übernommen und hieß zuvor *Green Address* und dann *Blockstream Green*.
- Hauptmerkmale** :
    - Onchain**-Transaktionen auf Blockchain Bitcoin.
    - Netzwerktransaktionen **Liquid** (Sidechain für schnellen, vertraulichen Datenaustausch).
    - Watch-only**-Portfolios zur Überwachung von Fonds ohne Zugang zu Schlüsseln.
    - Datenschutzoptionen: Verbindung über **Tor**, Verbindung zu einem **persönlichen Knoten** über Electrum oder **SPV**-Verifizierung, um die Abhängigkeit von Drittanbieter-Knoten zu verringern.
    - Funktionen **Replace-by-fee (RBF)** zur Beschleunigung unbestätigter Transaktionen.
- Kompatibilität**: Integriert Hardware-Wallets wie z. B. **Blockstream Jade**.
- Interface**: Intuitiv für Anfänger, mit erweiterten Optionen für Experten.
- Anmerkung**: Dieser Leitfaden konzentriert sich auf die Verwendung der Onchain. Andere Anleitungen in den Anhängen behandeln Liquid, Watch-Only und die Desktop-Version.



## 3. Installieren und Konfigurieren der Blockstream App



### 3.1. Herunterladen





- Für Android** :
    - Laden Sie [Blockstream App] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) aus dem Google Play Store herunter.
    - Alternativ: Installieren Sie über die APK-Datei, die auf [Blockstreams offiziellem GitHub](https://github.com/Blockstream/green_android) verfügbar ist.
- Für iOS** :
    - Laden Sie [Blockstream App] (https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) aus dem App Store herunter.
- Hinweis**: Achten Sie darauf, von offiziellen Quellen herunterzuladen, um betrügerische Anwendungen zu vermeiden.



### 3.2. Erstkonfiguration





- Startbildschirm**: Beim ersten Öffnen zeigt die Anwendung einen Bildschirm ohne konfigurierte Wallet. Erstellte oder importierte Portfolios werden später hier angezeigt.



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





- Funktion**: Verbindet die Anwendung mit Ihrem eigenen **kompletten Bitcoin-Knoten** über einen **Electrum**-Server.
- Warum?**: Ermöglicht die vollständige Kontrolle über Blockchain-Daten und beseitigt die Abhängigkeit von Blockstream-Servern.
- Voraussetzung**: Ein konfigurierter Bitcoin-Knoten.
- Empfehlung**: Fortgeschrittene Benutzer, die maximale Souveränität anstreben.


#### 3.2.4. SPV-Überprüfung





- Funktion**: Verwendet **Simplified Payment Verification (SPV)**, um bestimmte Blockchain-Daten direkt zu überprüfen, ohne die gesamte Kette herunterzuladen.
- Warum?**: Verringert die Abhängigkeit vom Standardknoten von Blockstream und bleibt gleichzeitig leichtgewichtig für mobile Geräte.
- Nachteil**: Weniger sicher als ein Full node, da es für einige Informationen auf Knotenpunkte Dritter angewiesen ist.
- Empfehlung**: Aktivieren Sie SPV, wenn Sie keinen persönlichen Knoten verwenden können, aber einen Full node für optimale Sicherheit bevorzugen.





## 4. Erstellung eines Bitcoin-Onchain-Portfolios



### 4.1. Erstellung starten





- Vorsicht**: Legen Sie Ihr Portfolio in einer privaten Umgebung an, ohne Kameras oder Beobachter.
- Klicken Sie auf dem Startbildschirm auf "Erste Schritte":



![image](assets/fr/04.webp)





- Wenn Sie einen **Cold Wallet** (offline Wallet) verwalten möchten: Klicken Sie auf **"Connect Jade "**, um den Hardware Wallet Blockstream Jade oder andere kompatible Cold Wallets zu verwenden.



![image](assets/fr/05.webp)





- Der nächste Bildschirm erscheint:



![image](assets/fr/06.webp)





- (1) **"Mobile Wallet einrichten "** : Erstellen Sie einen neuen Hot Wallet (Hot Wallet).
- (2) **"Wiederherstellen aus Backup "**: Importieren Sie ein bestehendes Portfolio mit einer Mnemonic Phrase (12 oder 24 Wörter). Achtung! Importieren Sie keinen Cold Wallet-Satz, da er auf einem angeschlossenen Gerät offengelegt wird und damit seine Sicherheit nicht mehr gewährleistet ist.
- (3) **"Nur beobachten "**: Importieren Sie ein bestehendes schreibgeschütztes Portfolio, um den Saldo (z. B. Ihres Cold Wallet) anzuzeigen, ohne den Mnemonic-Satz freizugeben. Siehe das Tutorial "Nur beobachten" im Anhang.



**In diesem Tutorial**: Klicken Sie auf **"Setup Mobile Wallet"**, um einen Hot Wallet zu erstellen.


Ihr Wallet wird automatisch erstellt und die Wallet-Startseite, hier "Mein Wallet 5" genannt, wird angezeigt:



![image](assets/fr/07.webp)



**Wichtig**: Die Blockstream App hat die Erstellung eines Wallet vereinfacht, indem sie den 12-Wort-seed-Satz nicht mehr automatisch anzeigt. *Auch wenn das Portfolio jetzt mit einem Klick erstellt wird, riskieren Sie, den Zugang zu Ihren Fonds zu verlieren, wenn Sie Ihre seed-Phrase* nicht speichern.



### 4.2. seed-Satz speichern





- Klicken Sie auf dem Wallet-Startbildschirm auf die Registerkarte "Sicherheit" und dann auf die Eingabeaufforderung "Sichern" oder das Menü "Wiederherstellungsphrase":



![image](assets/fr/08.webp)



Die seed 12-Wort-Phrase wird angezeigt und Sie können sie speichern.





- Schreiben Sie Ihren Wiederherstellungssatz mit äußerster Sorgfalt auf. Schreiben Sie ihn auf Papier oder Metall und bewahren Sie ihn an einem sicheren Ort auf (sicherer Offline-Ort). Diese Phrase ist Ihr einziges Mittel, um auf Ihre Bitcoins zuzugreifen, falls Sie Ihr Gerät verlieren oder die Anwendung gelöscht wird.
- Es ist auch wichtig zu wissen, dass jeder, der diesen Satz kennt, alle Ihre Bitcoins stehlen kann. Bewahren Sie sie niemals digital auf:
 - Kein Bildschirmfoto
 - Keine Cloud-, E-Mail- oder Messaging-Backups
 - Kein Kopieren/Einfügen (Gefahr des Speicherns in der Zwischenablage)



**! Dieser Punkt ist kritisch**. Weitere Informationen zur Datensicherung :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Bestätigen Sie den Satz seed



Bevor Sie Geld an einen Address senden, der mit diesem seed-Satz verbunden ist, müssen Sie die Sicherung Ihrer 12 Wörter testen.



Dazu schreiben wir eine Referenz auf, löschen den Wallet, stellen ihn mit der Sicherung wieder her und prüfen, ob die Referenz unverändert ist.





- Klicken Sie auf dem Wallet-Startbildschirm auf die Registerkarte "Einstellungen" und dann auf "Wallet-Details", und kopieren Sie den zPub ([erweiterter öffentlicher Schlüssel](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602):



![image](assets/fr/09.webp)



Hinweis: Ein zpub Address kann in Ihre Blockstream-Anwendung für die Funktion "Nur beobachten" importiert werden (siehe Anhang).





- Löschen Sie die Anwendung, stellen Sie dann den Wallet über **"Restore from Backup "** wieder her, indem Sie den Mnemonic-Satz eingeben, und prüfen Sie, ob der zpub unverändert ist. Wenn ja, ist Ihre Sicherung korrekt, und Sie können Mittel an den Wallet senden.





- Wenn Sie mehr darüber erfahren möchten, wie Sie einen Wiederherstellungstest durchführen, finden Sie hier eine entsprechende Anleitung:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.5. Sicherung des Zugangs zur Anwendung



Sperren Sie den Zugriff auf die Anwendung mit einem starken PIN-Code:




- Gehen Sie auf dem Wallet-Startbildschirm auf **"Sicherheit "** und klicken Sie dann auf **"PIN "**
- Geben Sie **einen zufälligen 6-stelligen PIN-Code** ein und bestätigen Sie ihn.



**Biometrische Option**: Erhältlich für zusätzlichen Komfort, aber weniger sicher als ein robuster PIN-Code (Risiko des unbefugten Zugriffs, z. B. Fingerabdruck oder Gesichtsscan im Schlaf).



**Hinweis**: Die PIN sichert das Gerät, aber nur der seed-Satz kann zum Abrufen von Geldern verwendet werden.





## 5. Verwendung des onchain Wallet



### 5.1. Bitcoins erhalten





- Klicken Sie auf der Startseite des Portfolios auf **Transact**" und dann auf **"Receive "**.



![image](assets/fr/10.webp)





- Die Anwendung zeigt einen **leeren Empfangs-Address** an (SegWit v0-Format, beginnend mit `bc1q...`). Die Verwendung eines neuen Address bei jedem Bitcoin-Empfang verbessert Ihre Vertraulichkeit.





- Optionen** :
    - (1) "Bitcoin": Klicken Sie auf , um eine Onchain- oder Liquid-Sendung auszuwählen, und wählen Sie die Anlage.
    - (2) Klicken Sie auf die Pfeile, um einen weiteren neuen Address auszuwählen, der mit diesem seed-Satz verbunden ist.
    - (3) Sie können auch einen Address aus den bereits verwendeten/angezeigten Adressen auswählen, indem Sie auf die drei Punkte oben rechts und dann auf "Liste der Adressen" klicken
    - (4) Um einen bestimmten Betrag anzufordern, klicken Sie auf die drei Punkte oben rechts, wählen "Betrag anfordern" und geben den gewünschten Betrag ein. Der QR wird aktualisiert, und die Address wird durch eine Bitcoin-Zahlungs-URI ersetzt.




![image](assets/fr/11.webp)





- Teilen Sie den Address/URI, indem Sie auf "**Teilen**" klicken, den Text kopieren oder den QR-Code scannen.
- Verifizierung**: Überprüfen Sie die mit dem Empfänger geteilten Address so weit wie möglich, um Fehler oder Angriffe zu vermeiden (z. B. Malware, die die Zwischenablage verändert).



### 5.2. Bitcoins senden





- Klicken Sie auf der Startseite des Portfolios auf "**Transaktion**" und dann auf **"Senden "**:



![image](assets/fr/12.webp)





- Details eingeben** :
    - (1) Geben Sie den **Address des Empfängers** ein, indem Sie ihn aufkleben oder einen QR-Code scannen.
    - (2) Überprüfen Sie die Vermögenswerte und das Konto, von dem die Gelder überwiesen werden.
    - (3) Geben Sie den zu überweisenden **Betrag** an. Sie können die Einheit wählen: BTC, Satoshis, USD, ...


Der Mindestbetrag (Dush-Limit) am 03/08/2025 beträgt 546 Sats.




    - (4) Wählen Sie **Transaktionsgebühren** :
        - Wählen Sie je nach Dringlichkeit aus den vorgeschlagenen Optionen (z. B. schnell, mittel, langsam), und es wird eine ungefähre Übertragungszeit angezeigt.
        - Für kundenspezifische Gebühren passen Sie die Anzahl der Satoshi pro Vbyte manuell an (siehe [Mempool.space](https://Mempool.space/) für marktübliche Tarife).




![image](assets/fr/13.webp)





- Prüfen** :
    - Überprüfen Sie die Address, den Betrag und die Gebühren auf dem Übersichtsbildschirm.
    - Ein Address-Fehler kann zu einem unwiderruflichen Verlust von Geldern führen. Hüten Sie sich vor Malware, die die Zwischenablage modifiziert.



![image](assets/fr/14.webp)





- Bestätigen**: Klicken Sie auf die Schaltfläche "Senden", um die Transaktion zu unterzeichnen und zu verteilen.
- Folgemaßnahmen**: Auf der Registerkarte Wallet "Transaktion" wird die Transaktion bis zur Bestätigung (1 bis 6 Bestätigungen) als "ausstehend" angezeigt:



![image](assets/fr/15.webp)





- Solange die Transaktion noch nicht bestätigt ist, können Sie mit der Funktion "Replace by fee" (siehe Anhang) die Abwicklung durch Erhöhung der Transaktionsgebühren beschleunigen:



![image](assets/fr/16.webp)




## Anhänge



### A1. Andere Blockstream-Tutorials



Verwendung des Liquid Network



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Importieren und Verfolgen eines Wallet im "Nur beobachten"-Modus



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Desktop-Version



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Erläuterung von Replace-by-fee (RBF)



**Definition**: Replace-by-fee (RBF) ist eine Funktion des Bitcoin-Netzwerks, die es dem Absender ermöglicht, die Bestätigung einer **onchain**-Transaktion zu beschleunigen, indem er sich bereit erklärt, eine höhere Gebühr zu zahlen.



**Grenzen** :




- RBF ist nicht für Liquid oder Lightning-Transaktionen verfügbar.
- Die erste Transaktion muss bei ihrer Erstellung als RBF-kompatibel gekennzeichnet werden, was Blockstream App automatisch tut.



**Weitere Informationen:**




- [Glossar](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Bewährte Praktiken



Um **Blockstream App** sicher und effizient zu nutzen, befolgen Sie diese Empfehlungen. Sie werden Ihnen helfen, Ihr Geld zu schützen, Ihre Transaktionen zu optimieren und Ihre Vertraulichkeit in den **Bitcoin (onchain)**, **Liquid** und **Lightning** Netzwerken zu wahren.





- Sichern Sie Ihre Wiederherstellungsphrase** :
 - Anleitung: Speichern des Mnemonic-Satzes



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Verwenden Sie eine sichere Authentifizierung** :
 - Aktivieren Sie eine **starke PIN** oder **biometrische Authentifizierung** (Fingerabdruck oder Gesichtserkennung), um den Zugang zur Anwendung zu schützen.
 - Geben Sie niemals Ihre PIN oder biometrischen Daten weiter.





- Schützen Sie Ihre Privatsphäre** :
 - generate ein neues Address für jeden Onchain- oder Liquid-Empfang, um die Rückverfolgung auf dem Blockchain zu begrenzen.
 - Aktivieren Sie die Funktionen "Verbesserter Datenschutz", "Tor" und "SPV".
 - Für maximale Vertraulichkeit sollten Sie Ihren Wallet über einen Electrum-Server mit Ihrem eigenen Bitcoin-Knoten verbinden, anstatt den öffentlichen Knoten zu verwenden





- Wählen Sie das für Ihre Bedürfnisse am besten geeignete Netz**:
 - Onchain**: Bevorzugt für langfristige Verwahrung oder Transaktionen mit hohem Wert (Gebühren im Verhältnis zum Betrag vernachlässigbar).
 - Liquid**: Für schnelle, kostengünstige Übertragungen mit erhöhter Vertraulichkeit.
 - Lightning**: Wählen Sie sofortige, kostengünstige Überweisungen für kleine Beträge.





- Überprüfen Sie immer die Lieferadressen** :
 - Überprüfen Sie das Address sorgfältig, bevor Sie Geldmittel senden. Gelder, die an einen falschen Address gesendet werden, sind für immer verloren. Verwenden Sie Kopieren/Einfügen oder QR-Code-Scannen, kopieren/verändern Sie niemals einen Address von Hand.





- Kosten optimieren** :
 - Wählen Sie für Onchain-Transaktionen je nach Dringlichkeit und Netzüberlastung geeignete Gebühren (langsam, mittel, schnell).
 - Verwenden Sie Liquid oder Lightning für kleine Mengen.





- Halten Sie die Anwendung auf dem neuesten Stand




### A4. Zusätzliche Ressourcen





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