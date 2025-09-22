---
name: Blockstream App - Watch-Only
description: Wie konfiguriere ich einen Watch-only wallet in der Blockstream App?
---

![cover](assets/cover.webp)


## 1. Einführung


### 1.1 Zielsetzung des Tutorials





- In diesem Tutorial wird erklärt, wie man die **Watch-Only**-Funktion der **Blockstream App** einrichtet und verwendet, um einen Bitcoin Wallet zu überwachen, ohne auf seine privaten Schlüssel zuzugreifen.
- Er behandelt die Installation, die Erstkonfiguration, den Import eines erweiterten öffentlichen Schlüssels und dessen Verwendung zur Verfolgung von Salden und generate-Empfangsadressen.
- Hinweis: Weitere Tutorials, die im Anhang zu finden sind, behandeln Onchain, Liquid und die Desktop-Version.



### 1.2. Zielpublikum





- **Einsteiger**: Benutzer, die ein Bitcoin-Portfolio (oft in Verbindung mit einem Hardware Wallet) über eine intuitive mobile Anwendung überwachen möchten.
- **Fortgeschrittene Nutzer**: Personen, die schreibgeschützte Portfolios verwalten und dabei Datenschutzoptionen wie Tor oder SPV nutzen möchten.
- **Hardware Wallet-Besitzer**: Sie können ihren Kontostand und ihre generate-Adressen überprüfen, ohne ihr Gerät anzuschließen.
- **Unternehmen und Geschäfte**:
 - Verfolgen Sie Ihre Transaktionen zu Buchhaltungszwecken, ohne Ihre privaten Schlüssel preiszugeben.
 - Überprüfung von Transaktionen, die ohne Eingabe der privaten Schlüssel in Online-Zahlungssystemen eingehen.
 - Ermöglichen Sie es Mitarbeitern, neue generate-Empfangsadressen zu nutzen, ohne Zugang zu privaten Schlüsseln zu haben.
- **Organisationen und Crowdfunding**: Zeigen Sie den Spendern den Saldo transparent an, ohne den Zugriff auf die Mittel zu ermöglichen.



### 1.3. Einführung von "Watch-Only



Mit einem **Watch-Only** Wallet können Sie die Transaktionen und den Kontostand eines Bitcoin Wallet überwachen, ohne Zugriff auf die privaten Schlüssel zu haben. Anders als ein herkömmlicher Wallet speichert er nur öffentliche Daten, wie den **erweiterten öffentlichen Schlüssel** (aus dem **xpub**, dann **zpub**, **ypub** usw. hervorgingen), der es ihm ermöglicht, Empfängeradressen zu erhalten und den Transaktionsverlauf auf dem Blockchain Bitcoin zu verfolgen. Da es keine privaten Schlüssel gibt, ist es unmöglich, Gelder aus der Anwendung auszuzahlen, was eine erhöhte Sicherheit garantiert.



![image](assets/fr/10.webp)



**Warum einen Watch-only wallet verwenden?**





- **Sicherheit**: Ideal für die Überwachung eines durch einen **Hardware Wallet** gesicherten Portfolios, ohne dass private Schlüssel auf einem angeschlossenen Gerät preisgegeben werden.
- **Bequemlichkeit**: Sie können den Kontostand und die neuen Empfängeradressen des generate überprüfen, ohne das Hardware Wallet anschließen zu müssen.
- **Vertraulichkeit**: Kompatibel mit Optionen wie **Tor** oder **SPV** zur Begrenzung der Abhängigkeit von Servern Dritter.
- **Anwendungsfälle**: Nachverfolgung von Geldern unterwegs, Generierung von Adressen für den Empfang von Zahlungen oder Verifizierung von Transaktionen, ohne private Schlüssel zu riskieren.



![image](assets/fr/01.webp)



### 1.4. Erweiterte öffentliche Schlüssel



Ein **erweiterter öffentlicher Schlüssel** (xpub, ypub, zpub usw.) ist ein von einem Bitcoin Wallet abgeleiteter Datensatz, der alle untergeordneten öffentlichen Schlüssel und die zugehörigen Empfangsadressen erzeugt, ohne Zugriff auf die privaten Schlüssel zu gewähren.





- **So funktioniert es**: Der erweiterte öffentliche Schlüssel wird durch ein deterministisches Verfahren (BIP-32) aus dem seed-Satz erzeugt. Es entsteht ein hierarchischer Baum von untergeordneten öffentlichen Schlüsseln, von denen jeder in einen Empfangs-Address umgewandelt werden kann. Unter Verwendung desselben Ableitungspfades (z. B. `m/44'/0'/0'`) wie der überwachte Wallet generiert der Watch-only wallet dieselben Adressen, so dass die Mittel verfolgt und neue Empfangsadressen erstellt werden können.



![image](assets/fr/11.webp)





- Erweiterte öffentliche Schlüsseltypen
- **xpub**: Wird für Legacy-Portfolios (Adressen, die mit "1" beginnen, BIP-44) und Taproot-Portfolios (Adressen, die mit "bc1p" beginnen, BIP-86) verwendet.
- **ypub**: Entwickelt für kompatible SegWit-Geldbörsen (Adressen, die mit "3" beginnen, BIP-49).
- **zpub**: Verbunden mit nativen SegWit-Portfolios (Adressen, die mit "bc1q" beginnen, BIP-84).
- **Andere (tpub, upub, vpub, usw.)**: Wird für alternative Netze (wie Testnet) oder spezielle Normen verwendet. Zum Beispiel steht tpub für das Testnet-Netz.





- **Unterscheidung**: Die Wahl zwischen xpub, ypub oder zpub hängt vom Address-Typ (legacy, SegWit, Taproot oder nested SegWit) und dem vom Wallet verwendeten BIP-Standard ab. Prüfen Sie das von Ihrem Quellportfolio geforderte Format, um die Kompatibilität mit der Blockstream App sicherzustellen.





- **Sicherheit und Vertraulichkeit**: Der erweiterte öffentliche Schlüssel ist nicht sicherheitsrelevant, da er die Ausgabe von Geldern nicht zulässt (kein Zugriff auf private Schlüssel). Er ist jedoch sensibel in Bezug auf die Vertraulichkeit, da er alle öffentlichen Adressen und die damit verbundene Transaktionshistorie offenlegt.



**Empfehlung**: Schützen Sie Ihren erweiterten öffentlichen Schlüssel als sensible Information.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Hot Wallet Erinnerung





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: alle Bezeichnungen für eine Anwendung, die auf einem Smartphone, einem Computer oder einem beliebigen mit dem Internet verbundenen Gerät installiert ist und die Verwaltung und Sicherung privater Schlüssel von einem Bitcoin Wallet ermöglicht.
- Im Gegensatz zu **Hardware-Geldbörsen**, auch bekannt als **Cold-Geldbörsen**, die die Schlüssel offline isolieren, arbeiten Software-Geldbörsen in einer vernetzten Umgebung, was sie anfälliger für Cyberangriffe macht.





- **Empfohlene Verwendung**:
    - Ideal für die Verwaltung moderater Mengen von Bitcoin, insbesondere für tägliche Transaktionen.
    - Geeignet für Anfänger oder Nutzer mit begrenztem Vermögen, für die ein Hardware Wallet überflüssig erscheint.





- **Beschränkungen**: Weniger sicher für die Aufbewahrung großer Geldbeträge oder langfristiger Ersparnisse. Wählen Sie in diesem Fall ein Hardware Wallet.




## 2. Einführung der Blockstream App





- **Blockstream App** ist eine mobile (iOS, Android) und Desktop-Anwendung zur Verwaltung von Bitcoin-Portfolios und Assets auf dem Liquid Network. Sie wurde 2016 von [Blockstream] (https://blockstream.com/) übernommen und hieß zuvor *Green Address* und dann *Blockstream Green*.
- **Hauptmerkmale**:
- **Onchain-Transaktionen** auf Blockchain Bitcoin.
    - Transaktionen über das **Liquid**-Netz (Sidechain für schnellen, vertraulichen Austausch).
- **Watch-only-Portfolios** zur Überwachung von Fonds ohne Zugang zu Schlüsseln.
    - Datenschutzoptionen: Verbindung über **Tor**, Verbindung zu einem **persönlichen Knoten** über Electrum oder **SPV**-Verifizierung, um die Abhängigkeit von Drittanbieter-Knoten zu verringern.
    - Funktionen **Replace-by-fee (RBF)** zur Beschleunigung unbestätigter Transaktionen.
- **Kompatibilität**: Integriert Hardware-Wallets wie z. B. **Blockstream Jade**.
- **Interface**: Intuitiv für Anfänger, mit erweiterten Optionen für Experten.
- **Anmerkung**: Dieser Leitfaden konzentriert sich auf die Verwendung von Onchain. Andere Anleitungen in den Anhängen behandeln Onchain, Watch-Only und die Desktop-Version.




## 3. Installieren und Konfigurieren der Blockstream App



### 3.1. Herunterladen





- **Für Android**:
    - Laden Sie [Blockstream App] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) aus dem Google Play Store herunter.
    - Alternativ: Installieren Sie über die APK-Datei, die auf [Blockstreams offiziellem GitHub](https://github.com/Blockstream/green_android) verfügbar ist.
- Für **iOS**:
    - Laden Sie [Blockstream App] (https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) aus dem App Store herunter.
- **Hinweis**: Achten Sie darauf, von offiziellen Quellen herunterzuladen, um betrügerische Anwendungen zu vermeiden.



### 3.2. Erstkonfiguration





- **Startbildschirm**: Beim ersten Öffnen zeigt die Anwendung einen Bildschirm ohne konfigurierte Wallet. Erstellte oder importierte Portfolios werden später hier angezeigt.



![image](assets/fr/02.webp)





- **Einstellungen anpassen**: Klicken Sie auf "Anwendungseinstellungen", passen Sie die Optionen unten an, klicken Sie auf "Speichern", starten Sie die Anwendung neu und erstellen Sie Ihr Portfolio.



![image](assets/fr/03.webp)



#### 3.2.1. Verbesserter Datenschutz (nur Android)





- **Funktion**: Deaktiviert Bildschirmfotos, blendet die Anwendungsvorschau im Task-Manager aus und sperrt den Zugriff, wenn das Telefon gesperrt ist.
- **Warum?**: Schützt Ihre Daten vor unbefugtem physischen Zugriff oder Malware, die den Bildschirm abfängt.



#### 3.2.2. Verbindung über Tor





- **Funktion**: Leiten Sie den Netzwerkverkehr über **Tor**, ein anonymes Netzwerk, das Ihre Verbindungen verschlüsselt.
- **Warum?**: Verbergen Sie Ihre IP Address und schützen Sie Ihre Privatsphäre, ideal, wenn Sie Ihrem Netzwerk nicht vertrauen (z. B. öffentliches WLAN).
- **Nachteil**: Kann die Anwendung aufgrund der Verschlüsselung verlangsamen.
- **Empfehlung**: Aktiviere Tor, wenn Vertraulichkeit eine Priorität ist, aber teste die Verbindungsgeschwindigkeit.



#### 3.2.3. Verbinden mit einem persönlichen Knoten





- **Funktion**: Verbindet die Anwendung mit Ihrem eigenen **kompletten Bitcoin-Knoten** über einen **Electrum-Server**.
- **Warum?**: Ermöglicht die vollständige Kontrolle über Blockchain-Daten und beseitigt die Abhängigkeit von Blockstream-Servern.
- **Voraussetzung**: Ein konfigurierter Bitcoin-Knoten.
- **Empfehlung**: Fortgeschrittene Benutzer, die maximale Souveränität wünschen.



#### 3.2.4. SPV-Überprüfung





- **Funktion**: Verwendet **Simplified Payment Verification (SPV)**, um bestimmte Blockchain-Daten direkt zu überprüfen, ohne die gesamte Kette herunterzuladen.
- **Warum?**: Verringert die Abhängigkeit vom Standardknoten von Blockstream und bleibt gleichzeitig leichtgewichtig für mobile Geräte.
- **Nachteil**: Weniger sicher als ein Full node, da er für einige Informationen auf Knotenpunkte von Dritten angewiesen ist.
- **Empfehlung**: Aktivieren Sie SPV, wenn Sie keinen persönlichen Knoten verwenden können, sondern einen Full node für optimale Sicherheit bevorzugen.





## 4. Erstellung eines Bitcoin "Watch-only"-Portfolios



### 4.1. Wiederherstellung des erweiterten öffentlichen Schlüssels



Um einen Watch-only wallet einzurichten, müssen Sie zunächst den erweiterten öffentlichen Schlüssel (xpub, ypub, zpub usw.) des zu überwachenden Wallet erhalten. Diese Informationen finden Sie im Allgemeinen in den Einstellungen oder im Abschnitt "Wallet-Informationen" Ihrer Software oder Ihres Hardware Wallet.





- Beispiel mit Blockstream App: Gehen Sie auf dem Wallet-Startbildschirm zu "Einstellungen" und dann zu "Wallet-Details", und kopieren Sie die Datei zpub :



![image](assets/fr/09.webp)





- Alternative 1: generate einen QR-Code mit dem erweiterten öffentlichen Schlüssel zum Scannen im nächsten Schritt.
- Alternative 2: Verwenden Sie einen output descriptor, wenn Ihr Wallet dies ermöglicht.



### 4.2. importieren Sie Wallet Watch-only





- **Vorsicht**: Legen Sie Ihr Portfolio in einer privaten Umgebung an, ohne Kameras oder Beobachter.
- Klicken Sie auf dem Startbildschirm auf "Neues Portfolio einrichten" und dann auf "Erste Schritte":



![image](assets/fr/04.webp)





- Der nächste Bildschirm erscheint:



![image](assets/fr/06.webp)






- (1) **"Mobile Wallet einrichten "** : Erstellen Sie einen neuen Hot Wallet. Siehe das "Blockstream App - Onchain"-Tutorial im Anhang.
- (2) **"Wiederherstellen aus Backup "**: Importieren Sie ein bestehendes Portfolio mit einer Mnemonic Phrase (12 oder 24 Wörter). Achtung! Importieren Sie die Phrase nicht von einem Cold Wallet, da sie auf einem angeschlossenen Gerät offengelegt wird, was ihre Sicherheit beeinträchtigt.
- (3) **"Watch-Only "**: die Option, die uns in diesem Tutorial interessiert.





- Wählen Sie dann "**Einzelsignatur**" und das Netz "**Bitcoin**":



![image](assets/fr/12.webp)





- Fügen Sie den erweiterten öffentlichen Schlüssel (xpub, ypub, zpub usw.) ein, scannen Sie den entsprechenden QR-Code, oder geben Sie einen output descriptor ein. Auch wenn die Anwendung "xpub" angibt, sind die Schlüssel ypub, zpub usw. ebenfalls zugelassen. Klicken Sie dann auf "Verbinden":



![image](assets/fr/13.webp)




### 4.3. Verwendung des Wallet Watch-only



Nach dem Import zeigt der Watch-only wallet den Gesamtsaldo und die Transaktionshistorie der vom erweiterten öffentlichen Schlüssel abgeleiteten Adressen an. Nur Onchain-Transaktionen sind sichtbar (Liquid-Transaktionen werden ignoriert). Um einen Liquid Wallet zu überwachen, wiederholen Sie den Import, indem Sie im vorherigen Schritt "Liquid" auswählen.





- **Saldo und Verlauf**: Auf dem Startbildschirm können Sie den Gesamtsaldo und den Verlauf der Onchain-Transaktionen einsehen:



![image](assets/fr/14.webp)





- generate einen empfangenden **Address**: Klicken Sie auf "Transact", dann auf "Receive", um einen neuen onchain Address zu erstellen. Teilen Sie ihn per QR-Code oder kopieren Sie ihn, um Geld zu erhalten:



![image](assets/fr/15.webp)





- **Geld senden**: Klicken Sie auf **"Transact"**, dann **"Send"**. Sie können eingeben:
 - Der Address des Empfängers.
 - Der Betrag der Transaktion.
 - Transaktionsgebühren.



Da das Watch-only wallet jedoch nicht über die privaten Schlüssel verfügt, können Sie keine Gelder direkt senden. Um die Transaktion zu signieren, verbinden Sie Ihre Hardware Wallet- oder Exchange-PSBTs durch Scannen der QR-Codes (eine Option, die z. B. auf der Coldcard Q verfügbar ist).



![image](assets/fr/16.webp)





- **Hinweis**: Überprüfen Sie immer das empfangende Address und die Transaktionsdetails, um Fehler zu vermeiden. Gelder, die an den falschen Address gesendet wurden, können nicht zurückerstattet werden.




## Anhänge



### A1. Andere Tutorials zur Blockstream App





- Nutzung des Onchain-Netzwerks :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Verwendung des Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Desktop-Version :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Erweiterte öffentliche Schlüssel





- Glossar :
 - [Erweiterte öffentliche Schlüssel](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Kurs:
 - [Les clés publiques étendues](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




### A3. Bewährte Praktiken



Um **Blockstream App** sicher und effizient zu nutzen, befolgen Sie diese Empfehlungen. Sie werden Ihnen helfen, Ihr Geld zu schützen, Ihre Transaktionen zu optimieren und Ihre Vertraulichkeit in den **Bitcoin (onchain)**, **Liquid** und **Lightning** Netzwerken zu wahren.





- **Sichern Sie Ihre Wiederherstellungsphrase**:
 - Anleitung: Speichern des Mnemonic-Satzes



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Verwenden Sie eine sichere Authentifizierung**:
 - Aktivieren Sie eine **starke PIN** oder **biometrische Authentifizierung** (Fingerabdruck oder Gesichtserkennung), um den Zugang zur Anwendung zu schützen.
 - Geben Sie niemals Ihre PIN oder biometrischen Daten weiter.





- **Schützen Sie Ihre Privatsphäre** :
 - generate ein neuer Address für jeden Onchain- oder Liquid-Empfang, um die Verfolgung auf dem Blockchain zu begrenzen.
 - Aktivieren Sie die Funktionen "Verbesserter Datenschutz", "Tor" und "SPV".
 - Für maximale Vertraulichkeit sollten Sie Ihren Wallet über einen Electrum-Server mit Ihrem eigenen Bitcoin-Knoten verbinden, anstatt den öffentlichen Knoten zu verwenden





- Wählen Sie das für Ihre Bedürfnisse am besten geeignete **Netz**:
- **Onchain**: Bevorzugt für langfristige Verwahrung oder Transaktionen mit hohem Wert (Gebühren im Verhältnis zum Betrag vernachlässigbar).
- **Liquid**: Für schnelle, kostengünstige Übertragungen mit erhöhter Vertraulichkeit.
- **Lightning**: Wählen Sie sofortige, kostengünstige Überweisungen für kleine Beträge.





- **Überprüfen Sie immer die Lieferadressen**:
 - Überprüfen Sie den Address sorgfältig, bevor Sie Geldmittel senden. Gelder, die an einen falschen Address gesendet werden, sind für immer verloren. Verwenden Sie Kopieren/Einfügen oder QR-Code-Scannen, kopieren/verändern Sie einen Address niemals von Hand.





- **Kosten optimieren**:
 - Wählen Sie für Onchain-Transaktionen je nach Dringlichkeit und Netzüberlastung geeignete Gebühren (langsam, mittel, schnell).
 - Verwenden Sie Liquid oder Lightning für kleine Mengen.





- Halten Sie die Anwendung auf dem neuesten Stand




### A4. Zusätzliche Ressourcen





- **Offizielle Blockstream-Links:**
- [Offizielle Website](https://blockstream.com/)
- [Support für die mobile Anwendung](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): Dokumentation und Chat
- [GitHub](https://github.com/Blockstream/green_android)





- **Block Explorers:**
 - Onchain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Blitzschlag: **[1ML (Lightning Network)](https://1ml.com/)**





- Lernen und Tutorien: **[Plan ₿ Network](https://planb.network/)**
  - Sicherung des Wiederherstellungssatzes



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Glossar](https://planb.network/fr/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**:
- [Glossar](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb