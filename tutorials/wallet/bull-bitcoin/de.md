---
name: Bull Bitcoin Wallet
description: Finden Sie heraus, wie Sie den Wallet Bull Bitcoin verwenden
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Dieses Video-Tutorial von BTC Sessions führt Sie durch den Prozess der Einrichtung und Verwendung von Bull Bitcoin Wallet!*


Dieser Leitfaden führt Sie durch die Installation, Konfiguration und Verwendung von Bull Bitcoin Wallet. Sie erfahren, wie Sie Gelder in den Netzwerken Bitcoin, On-Chain, Liquid und Lightning senden und empfangen und wie Sie Bitcoin zwischen diesen Netzwerken verschieben können. Die umfangreichen Funktionen des wallet machen es zu einem leistungsstarken All-in-One-Tool für die Verwaltung Ihres Bitcoin. Lassen Sie uns beginnen.


## Einführung


Bull Bitcoin Wallet, entwickelt von [Bull Bitcoin] (https://www.bullbitcoin.com/), ist ein **selbstverwaltetes** Bitcoin wallet, was bedeutet, dass Sie die volle Kontrolle über Ihre privaten Schlüssel und damit über Ihr Geld haben, ohne von einer dritten Partei abhängig zu sein. Open-Source und verwurzelt in einer Cypherpunk-Philosophie, kombiniert dieser Wallet Einfachheit, Vertraulichkeit und fortgeschrittene Funktionen wie netzwerkübergreifende Swaps und PayJoin-Unterstützung. Es ermöglicht Ihnen, Ihre Bitcoins in drei Netzwerken zu verwalten: **Bitcoin onchain**, **Liquid** und **Lightning**, die jeweils auf bestimmte Anwendungen zugeschnitten sind. Auf dem [BullBitcoin GitHub] (https://github.com/orgs/SatoshiPortal/projects/49) können Sie sich über aktuelle Themen und kommende Entwicklungen informieren. Da das Projekt zu 100 % quelloffen und "öffentlich gebaut" ist, können Sie auch Ihre Vorschläge und Fehler, auf die Sie stoßen, einsenden. Während einige Wallets mittlerweile mehrere Netzwerke unterstützen, zeichnet sich der Bull Bitcoin Wallet dadurch aus, dass er Datenschutzfunktionen in alle Netzwerke integriert, was ihn zu einem leistungsstarken Tool für die Verwaltung Ihres Bitcoin in allen wichtigen Netzwerken macht


## 1️⃣ Voraussetzungen


Bevor Sie den **Bull Bitcoin Wallet** in Betrieb nehmen, vergewissern Sie sich, dass Sie die folgenden Gegenstände besitzen:



- Kompatibles Smartphone**: Ein **iOS** (iPhone oder iPad) oder **Android** Gerät
- Internetverbindung
- Sichere Sicherungsmedien**: Schreiben Sie Ihre **Wiederherstellungsphrase** (12 Wörter) auf Papier oder Metall und bewahren Sie sie an einem sicheren Ort auf.
- Grundkenntnisse**: Ein Mindestmaß an Verständnis der Bitcoin-Konzepte (Adressen, Transaktionen, Gebühren) ist nützlich, auch wenn dieses Tutorial jeden Schritt für Anfänger erklärt.


## 2️⃣ Installation


Sie können die Anwendung über installieren:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(für iOS-Geräte)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (für Android-Geräte)


Android-Nutzer haben auch andere Möglichkeiten:



- Lade die APK direkt von der [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) Seite herunter oder
- Installation über den Nostr-kompatiblen [Zapstore] (https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)


Nach der Installation der Anwendung folgen Sie dem Willkommensbildschirm, um Ihr Konto zu konfigurieren.


## 3️⃣ Erstmalige Konfiguration


Beim Öffnen werden Sie mit den folgenden Optionen konfrontiert:



- neues Wallet erstellen"
- gW-20 wiederherstellen" und
- erweiterte Optionen"


Beginnen wir mit dem Tippen auf "Erweiterte Optionen".


Hier können wir die erweiterten Einstellungen konfigurieren, bevor wir eine wallet erstellen oder wiederherstellen:


1. Aktiviere den "Tor-Proxy", um den Verkehr über das Tor-Netzwerk zu leiten.

1. die [Orbot-App] (https://orbot.app/en/) muss installiert sein und laufen, bevor sie aktiviert werden kann

2. Tor Proxy gilt nur für Bitcoin (nicht Liquid) und kann zu einer langsameren Verbindung führen.

2. Einrichten eines "benutzerdefinierten Electrum Server", oder

3. Passen Sie die Einstellungen von "Recover Bull" an. Wir werden später mehr über [Recover Bull] (https://recoverbull.com/) erfahren.


Nachdem Sie alle optionalen Einstellungen vorgenommen haben, tippen Sie auf "Fertig". Wenn Sie ein vorhandenes Wallet wiederverwenden möchten, klicken Sie auf "Wallet wiederherstellen" und geben Sie die 12 Wörter Ihrer Wiederherstellungsphrase ein.


Andernfalls klicken Sie auf "Create a New Wallet" (Neues Wallet erstellen).


![image](assets/en/01.webp)


## 4️⃣ Startbildschirm


Bevor wir tiefer eintauchen, werfen wir einen Blick auf den "Startbildschirm", um uns zu orientieren:



- die "Transaktionsübersicht" und das "Einstellungsmenü" befinden sich ganz oben.
- Der "Verfügbare Saldo" hat eine Datenschutzoption, die ein- oder ausgeschaltet werden kann.
- Greifen Sie auf den "Bitcoin Bull Exchange" zu, um zu kaufen, zu verkaufen oder zu bezahlen (dies hängt von der Gerichtsbarkeit ab und kann KYC erfordern).
- übertragung von Geldbeträgen zwischen Geldbörsen
- sicherheit Bitcoin" ist gleich Onchain Bitcoin Wallet
- sofortige Zahlungen" über Lightning / Liquid Network *(Hinweis: Bull Bitcoin Wallet ermöglicht es, Zahlungen über Lightning zu tätigen und zu empfangen. Über Lightning empfangene Gelder werden dank eines automatischen Austauschs über [*Boltz exchange](https://boltz.exchange/) im [*Liquid network](https://liquid.net/) (im Wallet Instant Payments) gespeichert. Dies gibt Ihnen die Möglichkeit, mit Lightning zu interagieren, ohne Liquiditätskanäle verwalten zu müssen, während Sie selbst in der Verwahrung bleiben.)
- senden und Empfangen von Geldern


![image](assets/en/02.webp)


Lassen Sie uns zunächst einige wichtige Konfigurationen vornehmen und mit dem `Backup` beginnen.


## 5️⃣ Sicherung


Um den Sicherungsvorgang zu starten, tippen Sie auf das "Zahnradsymbol (⚙)" in der oberen rechten Ecke der App und wählen Sie "Wallet Backup". Es werden Ihnen zwei Methoden zur Sicherung Ihres wallet angeboten: "Verschlüsselter Tresor" und "Physikalische Sicherung". Schauen wir uns beide an.


![image](assets/en/03.webp)


### Physikalische Sicherung


Tippen Sie auf "Physikalische Sicherung", um eine Liste von 12 Wörtern zu sehen, die Ihre Wiederherstellung oder seed-Phrase darstellen. Bitte beachten Sie die folgenden Punkte:



- Schreiben Sie Ihren "Wiederherstellungssatz" mit größter Sorgfalt auf. Schreiben Sie ihn auf Papier oder Metall und bewahren Sie ihn an einem sicheren Ort auf (Bankschließfach, Offline-Ort). Diese Phrase ist Ihr einziges Mittel, um auf Ihre Bitcoins zuzugreifen, falls Sie Ihr Gerät verlieren oder die Anwendung gelöscht wird.
- Es ist auch wichtig zu wissen, dass jeder, der diesen Satz kennt, alle Ihre Bitcoins stehlen kann. Bewahren Sie sie niemals digital auf:
- Kein Bildschirmfoto
- Keine Cloud-, E-Mail- oder Messaging-Backups
- Kein Kopieren/Einfügen (Gefahr des Speicherns in der Zwischenablage)


![image](assets/en/25.webp)


Auf dem nächsten Bildschirm müssen Sie die Wörter in die richtige Reihenfolge bringen, um sicherzustellen, dass Sie den seed-Satz richtig geschrieben haben. Sie erhalten eine Bestätigung, wenn der Test erfolgreich abgeschlossen ist.


! **Dieser Punkt ist kritisch**. Für weitere Hilfe:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Verschlüsselter Tresor


Es gibt auch die Möglichkeit eines verschlüsselten, anonymen Backups in der Cloud. Aber haben wir nicht im letzten Absatz erwähnt, dass Cloud-Backups riskant sind und vermieden werden sollten? Das Bull Bitcoin-Team hat jedoch eine clevere Methode entwickelt, um das Verfahren sicher zu machen. Und so funktioniert es:


recoverbull" ist ein Sicherungsprotokoll, das die Sicherung Ihres Bitcoin wallet vereinfacht, indem es die Sicherung in zwei Teile aufteilt. Zunächst wird die Sicherungsdatei Ihres wallet auf Ihrem Gerät mit einem starken Verschlüsselungsschlüssel verschlüsselt. Sie können diese verschlüsselte Datei speichern, wo immer Sie wollen, z. B. auf Google Drive oder Ihrem Gerät. Zweitens wird der Verschlüsselungsschlüssel, der zum Entsperren der Datei benötigt wird, auf dem Recoverbull Key Server gespeichert. Um Ihr wallet wiederherzustellen, benötigen Sie sowohl die verschlüsselte Sicherungsdatei als auch den Schlüssel, auf den Sie mit Ihrer PIN oder Ihrem Passwort zugreifen. Dieses Design stellt sicher, dass Ihr Cloud-Backup allein unbrauchbar ist und dass der Schlüsselserver allein ohne Ihre spezielle Backup-Datei unbrauchbar ist. So sind Ihre Gelder auch dann sicher, wenn ein Teil davon kompromittiert wird.


Stellen Sie es sich wie ein Bankschließfach vor. Die verschlüsselte Sicherungsdatei ist die *Box*, die Sie überall (z.B. Google Drive) speichern können. Ihre Wiederherstellungs-PIN ist der *Schlüssel*, der separat auf dem Recoverbull Key Server gespeichert ist. Ein Dieb müsste sowohl Ihre spezielle Box als auch Ihren speziellen Schlüssel bekommen, um sie zu öffnen. Dieses Design stellt sicher, dass selbst wenn jemand Ihre Sicherungsdatei erhält, diese ohne den Schlüssel vom Server nutzlos ist, und der Schlüssel des Servers ist ohne Ihre einzigartige Sicherungsdatei nutzlos.


Erfahren Sie mehr über das wallet-Sicherungsprotokoll "Recoverbull" [hier] (https://recoverbull.com/).


Tippen Sie auf "Verschlüsselter Tresor" und dann auf "Fortfahren", um die Verwendung des Standardservers zu bestätigen. Die Verbindung wird über das "Tor"-Netzwerk geleitet, um den Datenschutz und die Anonymität zu gewährleisten.


**Verstehen Sie Ihre PINs**



- pIN zum Entsperren der App**:** Die optionale PIN, die Sie unter "Einstellungen > Sicherheits-PIN" festlegen, um die App auf Ihrem Telefon zu sperren.
- wiederherstellungs-PIN**:** Die obligatorische PIN, die während des Sicherungsprozesses des "verschlüsselten Tresors" erstellt wurde und zur Entschlüsselung Ihrer Sicherungsdatei während der Wiederherstellung verwendet wird.


Es handelt sich um zwei separate PINs. Vergessen Sie Ihre Wiederherstellungs-PIN nicht, da sie für die Wiederherstellung Ihres wallet unerlässlich ist."


**Wiederherstellungs-PIN-Einrichtung:**



- Sie müssen eine PIN oder ein Passwort erstellen, um den Zugang zu Ihrem wallet wiederherzustellen.
- Die PIN / das Passwort muss mindestens 6 Ziffern lang sein (vermeiden Sie z. B. einfache Sequenzen wie 123456, die nicht akzeptiert werden).
- Ohne diese PIN ist die Wiederherstellung von wallet unmöglich.


Wählen Sie dann einen Tresoranbieter aus:



- "Google Drive" oder
- einen "benutzerdefinierten Ort" (z. B. Ihr Gerät)


![image](assets/en/04.webp)


Speichern Sie nun die "Sicherungsdatei". Tippen Sie anschließend auf "Wiederherstellung testen", wählen Sie Ihre gespeicherte Sicherungsdatei oder Ihren Tresor aus und tippen Sie dann auf "Tresor entschlüsseln". Geben Sie Ihre "PIN" oder Ihr "Passwort" ein. Wenn alles funktioniert hat, wird der Bildschirm "Test erfolgreich abgeschlossen" angezeigt.


### Import/Export-Etiketten


Nachdem wir nun unser Backup erstellt haben, lassen Sie uns einen Blick auf "Etiketten" werfen.  Das Bull Bitcoin wallet verbessert den Datenschutz und die Organisation, indem es den Benutzern ermöglicht, benutzerdefinierte Etiketten für ihre Empfangsadressen und Transaktionen zu erstellen. Diese Kennzeichnungen helfen Ihnen bei der Kategorisierung Ihrer Gelder, da Transaktionen, die an eine gekennzeichnete Adresse gesendet werden, diese Kennzeichnung übernehmen, und Sie können auch ausgehende Transaktionen kennzeichnen, um deren Änderungen zu verfolgen. Das wallet unterstützt den [BIP-329](https://bip329.org/)-Standard vollständig, d. h. Sie können alle Ihre Etiketten in eine Datei exportieren und in ein anderes wallet importieren. Diese Funktion stellt sicher, dass Sie Ihre Transaktionshistorie und Kategorisierungen nahtlos sichern oder zwischen verschiedenen Instanzen des wallet migrieren können, ohne Ihre personalisierte Organisation zu verlieren.


![image](assets/en/05.webp)


## 6️⃣ Einstellungen


Nachdem Ihr primäres Backup gesichert ist, können wir nun die anderen in den Einstellungen verfügbaren Funktionen erkunden.


### A - Sicherung des Zugangs


Um die App zu sichern, navigieren Sie zu "Einstellungen" und wählen Sie "Sicherheits-PIN", um den PIN-Code auszuwählen. Erstellen Sie eine starke PIN, um den Zugriff auf Ihr wallet zu sperren. Dieser Schritt ist zwar optional, wird aber dringend empfohlen, um unbefugten Zugriff zu verhindern, wenn jemand anderes Ihr Telefon verwendet.


![image](assets/en/06.webp)


### B - Verbindung zu einem persönlichen Knoten (optional)


Der Wallet BullBitcoin verbindet sich standardmäßig mit Electrum-Servern: dem ersten, der von Bull Bitcoin verwaltet wird, und einem sekundären Server von Blockstream, von dem man annimmt, dass er keine Protokolle aufbewahrt, was das Risiko des Trackings verringert.


Um die Vertraulichkeit zu erhöhen, können Sie die Anwendung über einen Electrum-Server mit Ihrem eigenen Bitcoin-Knoten verbinden. Tippen Sie dazu auf "Einstellungen" > "Bitcoin-Einstellungen" > "Electrum Server-Einstellungen" und dann auf "+ Benutzerdefinierten Server hinzufügen", um die Adresse und die Anmeldedaten Ihres Servers einzugeben.


![image](assets/en/07.webp)


### C - Währung


Das verfügbare Guthaben wird auf dem Hauptbildschirm sowohl in "sats" als auch in "USD" angezeigt. Um dies zu ändern, navigieren Sie zu "Einstellungen" > "Währung". Dort können Sie zwischen "sats/BTC" umschalten und Ihre "Standardwährung" auswählen.


![image](assets/en/08.webp)


### D - Bitcoin Einstellungen


Das Menü "Bitcoin Einstellungen" bietet tiefen Zugriff auf die wichtigsten Konfigurationen und Daten Ihres wallet. Hier können Sie die grundlegenden Details Ihres `Secure Bitcoin` und Ihrer `Instant Payments Wallets` einsehen, was Ihnen volle Transparenz und Kontrolle bietet. Zu den wichtigsten Funktionen in diesem Menü gehören:



- Wallet Details:** Navigieren Sie zu Ihrem Secure Bitcoin oder Instant payments wallet, um spezifische Informationen anzuzeigen.
- Wallet Fingerprint:** Eine eindeutige Kennung für Ihr wallet.
- Öffentlicher Schlüssel (Pubkey):** Der Schlüssel, der verwendet wird, um generate Ihre Bitcoin-Empfangsadressen.
- Descriptor:** Eine technische Zusammenfassung der Struktur Ihres wallet.
- Ableitungspfad:** Der spezifische Pfad, der verwendet wird, um generate alle Adressen von Ihrem privaten Hauptschlüssel abzuleiten.
- Address View:** Rufen Sie eine Liste Ihrer nicht verwendeten Empfangsadressen auf und ändern Sie Adressen (in Kürze)


Außerdem haben Sie die Möglichkeit,:



- aktivieren Sie die Einstellung "Automatischer Transfer", um ein maximales sofortiges wallet-Guthaben festzulegen, das dann automatisch auf den sicheren bitcoin wallet übertragen wird.
- Generische Geldbörsen über die Phrase "Mnemonic" importieren oder "watch-only" importieren
- Verbinden von "Hardware-Geldbörsen": Derzeit werden folgende Geräte unterstützt: ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade und Foundation Passport


## 7️⃣ Bull Bitcoin Exchange


Direkt vom wallet aus haben Sie Zugriff auf die [Bull Bitcoin-Börse] (https://www.bullbitcoin.com/), so dass Sie Bitcoin kaufen, verkaufen und bezahlen können, ohne die App zu verlassen. Diese Integration bietet eine bequeme Lösung für die Verwaltung Ihrer Bitcoin Bedürfnisse. Bitte beachten Sie, dass der Zugang zur Börse und ihren Diensten je nach Gerichtsbarkeit eingeschränkt sein kann und dass eine Überprüfung der Kundenidentität (Know Your Customer, KYC) erforderlich sein kann, um die regulatorischen Standards einzuhalten und alle Funktionen der Plattform zu nutzen.


Um loszulegen, tippen Sie auf "Exchange" in der rechten unteren Ecke und dann auf "Anmelden" oder "Login" für Ihr Konto.


Die Börse bietet die folgenden [Funktionen](https://www.bullbitcoin.com/):



- Kaufen Sie Bitcoin mit Selbstverwahrung von Ihrem Bankkonto
- Ohne Freiheitsentzug
- Einzelpersonen oder Körperschaften
- Sofortige Rücknahme
- Keine versteckten Gebühren
- Lightning Network verfügbar
- Keine Transaktionslimits
- Wiederkehrende Kaufoptionen


![image](assets/en/09.webp)


Weitere Informationen finden Sie in diesem Tutorial:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Empfang von Geldern


Der Empfang von Geldern mit **Bull Bitcoin Wallet** ist einfach und flexibel und unterstützt drei verschiedene Netzwerke, die für unterschiedliche Anwendungsfälle zugeschnitten sind:



- Das Netz "Bitcoin (onchain)" für die sichere Langzeitspeicherung.
- Das "Liquid"-Netz für schnelle, vertrauliche Transaktionen.
- Das "Lightning"-Netz für sofortige, preisgünstige Zahlungen.


Die App generiert automatisch die entsprechende Adresse oder Rechnung, je nach dem von Ihnen gewählten Netz. Hier erfahren Sie, wie Sie für jedes Netz vorgehen.


### Empfang über Onchain (Bitcoin-Netzwerk)


Um on-chain-Gelder zu empfangen, können Sie entweder "Secure Bitcoin Wallet" auf dem Startbildschirm auswählen und auf "Empfangen" tippen oder auf die Haupttaste "Empfangen" tippen und dann das "Bitcoin-Netz" auswählen.


Es gibt zwei primäre Modi für die Generierung einer Empfangsadresse:


**Standardmodus (URI mit zusätzlichen Eingabeparametern)


Standardmäßig erzeugt der wallet eine [BIP21 URI] (https://bips.dev/21/). Dabei handelt es sich um ein standardisiertes Format, das mehr Informationen als eine einfache Adresse enthält, darunter einen Betrag, eine persönliche Notiz und PayJoin-Parameter zur Verbesserung des Datenschutzes. Diese umfassende URI wird in einen QR-Code kodiert und zum Kopieren zur Verfügung gestellt. Das Format sieht wie folgt aus: bitcoin:<Adresse>?<Parameter1>=<Wert1>&<Parameter2>=<Wert2>`.



- Zusätzliche Eingabeparameter:**
    - Betrag:** Geben Sie den gewünschten Betrag in BTC, sats oder einer Fiat-Währung an.
    - Nachricht:** Fügen Sie eine persönliche Notiz hinzu, die für den Absender sichtbar ist.
    - PayJoin:** Aktivieren Sie diese Option, um den Datenschutz zu verbessern, indem Sie die Eingaben von Sender und Empfänger in der Transaktion kombinieren.


Beispiel URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Wichtiger Hinweis: Bitte senden Sie kein Geld an die Adressen in diesem Tutorial, der wallet wird gelöscht


![image](assets/en/10.webp)


**Nur Address kopieren oder scannen Option aktiviert


Wenn die Option "Nur Address kopieren oder scannen" aktiviert ist, erzeugt die Anwendung eine einfache Bitcoin-Adresse im SegWit-Format (bech32).


Beispiel:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Auch wenn Sie einen Betrag oder eine Notiz eingeben, werden diese nicht in den QR-Code oder die kopierte Adresse übernommen.


![image](assets/en/11.webp)


### Empfangen über den Liquid Network


Sie können eine Zahlung auf dem Liquid Network empfangen. Auf dem Bildschirm "Empfangen" haben Sie dieselben zwei Optionen, um eine Zahlungsanforderung zu erstellen:


**1. Einfacher Address:** Kopieren Sie die standardmäßige "Liquid-Adresse". Dies ist eine eindeutige Kennung für Ihren wallet im Liquid-Netz und enthält keine spezifischen Beträge oder Nachrichten.


Beispiel Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Detaillierte Zahlungsanforderung (URI):** Für eine strukturiertere Anforderung können Sie einen Betrag und eine persönliche Notiz angeben. Diese Informationen werden automatisch in einen teilbaren URI und den entsprechenden QR-Code kodiert.



- Betrag:** Sie können den Betrag in Bitcoin (BTC), Satoshis (Sats) oder einer Fiat-Währung festlegen.
- Hinweis:** Fügen Sie eine persönliche Nachricht hinzu, um die Transaktion zu identifizieren.


**Beispiel URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


Um die Transaktion abzuschließen, übermitteln Sie dem Absender die "Adresse" oder "URL". Dazu können Sie sie in die Zwischenablage kopieren oder den QR-Code direkt von Ihrem Bildschirm scannen lassen.


![image](assets/en/12.webp)


### Empfangen über Lightning



Mit dem Bull Bitcoin Wallet können Sie auch Zahlungen über das Lightning Network senden und empfangen. Eine wichtige Funktion ist, dass über Lightning empfangene Gelder automatisch ausgetauscht und auf dem Liquid Network in Ihrem Instant Payments Wallet gespeichert werden. Dieser Dienst wird vom Boltz unterstützt. Dank dieses Konzepts können Sie von der Geschwindigkeit und den niedrigen Kosten von Lightning profitieren, ohne die Komplexität der Verwaltung von Liquiditätskanälen in Kauf nehmen zu müssen, während Sie Ihre Gelder vollständig selbst verwahren. Während dieser hybride Ansatz selbstverwahrend ist und die Komplexität der Verwaltung von Kanälen vermeidet, führt er einen Drittanbieter-Service (Boltz), eine geringe Swap-Gebühr und die Abhängigkeit von der Liquid Network-Föderation von Funktionären als Schlüsselinhaber ein, was sich von einem traditionellen, nicht-verwahrenden Lightning wallet unterscheidet, bei dem Sie Ihre eigenen Kanäle verwalten. Mehr über Liquid und sein Verwaltungsmodell erfahren Sie hier:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Grenzwerte:**
    - Mindestbetrag:** Ein Mindestrechnungsbetrag ist erforderlich. Bitte überprüfen Sie die App auf das aktuelle Limit
    - Gebühren:** Sie, der Empfänger, sind für eine kleine Swap-Gebühr verantwortlich. Diese Gebühr wird von dem Betrag, den der Absender überweist, abgezogen und kann sich ändern
- Vorteile:**
    - Selbstverwahrung:** Ihr Geld ist immer unter Ihrer Kontrolle, gesichert im Liquid-Netzwerk.
    - Vermeiden Sie hohe On-Chain-Gebühren:** Indem Sie Lightning verwenden und auf Liquid speichern, umgehen Sie die on-chain-Gebühren, die mit der Eröffnung eines herkömmlichen Lightning-Kanals verbunden sind. Sie können sich dafür entscheiden, Gelder später in einen on-chain-Kanal zu verschieben, wenn der angesammelte Betrag die Kosten rechtfertigt.
    - Tipp:** Für die kostengünstigste Transaktion zwischen zwei Bull Bitcoin-Nutzern sollten Sie das **Liquid-Netzwerk direkt** nutzen, um die Lightning-Swap-Gebühren vollständig zu vermeiden.


Um eine Zahlung zu erhalten, müssen Sie generate eine "Blitzrechnung" ausstellen:


1. geben Sie einen Betrag ein**:** Geben Sie den Betrag an, den Sie in Bitcoin (BTC), Satoshis (Sats) oder einer Fiat-Währung erhalten möchten.

2. anmerkung hinzufügen" **(Optional):** Fügen Sie ein Memo oder eine Anmerkung ein. Diese wird in die Rechnung eingebettet und in Ihrem Transaktionsverlauf angezeigt, sobald die Zahlung abgeschlossen ist, damit sie leichter identifiziert werden kann.

3. gW-124 Gültigkeit "**:** Die Blitzrechnung ist zeitabhängig und läuft nach **12 Stunden** ab. Wenn sie nicht innerhalb dieses Zeitraums bezahlt wird, wird sie ungültig und Sie müssen eine neue Rechnung erstellen (generate).


Geben Sie dem Absender die Rechnung, indem Sie sie in die Zwischenablage kopieren oder den auf Ihrem Bildschirm angezeigten QR-Code scannen lassen.


![image](assets/en/13.webp)


## 9️⃣ Übermittlung von Geldern


Sie können den Sendebildschirm direkt von der Startseite oder von einer Ihrer Geldbörsen aus aufrufen. Bull Bitcoin Wallet vereinfacht den Prozess, indem es automatisch das Zielnetzwerk - "Bitcoin", "Liquid" oder "Lightning" - anhand der von Ihnen eingegebenen Adresse oder Rechnung erkennt, unabhängig davon, ob diese eingefügt oder per QR-Code gescannt wurde.


### On-Chain Übertragung über das Bitcoin-Netz


Wenn Sie Geld mit on-chain überweisen, wird Ihre Transaktion direkt in der Bitcoin-Blockchain aufgezeichnet. Diese Methode eignet sich am besten für größere Überweisungen oder nicht zeitkritische Überweisungen. Um zu beginnen, können Sie auf die Schaltfläche "Senden" unten rechts tippen und eine "Standard-Bitcoin-Adresse" scannen oder eingeben.


Wenn die von Ihnen angegebene Adresse keinen bestimmten Betrag enthält, werden Sie auf dem Sendebildschirm aufgefordert, die Details einzugeben. Sie können den Betrag in der von Ihnen bevorzugten Einheit angeben, z. B. in BTC, Satoshis oder einem Fiat-Äquivalent. Sie haben auch die Möglichkeit, eine persönliche Notiz hinzuzufügen, die Ihnen dabei hilft, die Transaktion später zu identifizieren. Diese Notiz wird nicht an den Empfänger weitergegeben.


Umgekehrt, wenn die Zahlungsanforderung, die Sie scannen oder einfügen, bereits alle notwendigen Details enthält, wie z. B. eine BIP21 URI mit einem vordefinierten Betrag, umgeht das wallet den Dateneingabebildschirm und führt Sie direkt zum Bestätigungsbildschirm, um die Zahlung zu autorisieren.


![image](assets/en/14.webp)


Bevor Ihre Transaktion gesendet wird, erhalten Sie einen Bestätigungsbildschirm. Es ist wichtig, dass Sie sich einen Moment Zeit nehmen und alle Parameter sorgfältig überprüfen, wobei Sie besonders auf die Empfängeradresse, den zu sendenden Betrag und die Netzwerkgebühren achten sollten. Dieser Bildschirm bietet auch leistungsstarke Werkzeuge zur Anpassung Ihrer Transaktion.


Sie können die Gebühren auf zwei Arten steuern. Die erste Methode besteht darin, eine gewünschte Transaktionsgeschwindigkeit auszuwählen, z. B. niedrig, mittel oder hoch, und das wallet berechnet automatisch die entsprechende Gebühr für Sie. Die zweite Methode ermöglicht eine genauere Steuerung, indem Sie eine bestimmte Gebühr festlegen, entweder als absoluten Gesamtbetrag in Satoshis oder als relativen Satz pro Byte, der dann eine geschätzte Bestätigungszeit ergibt.


Für fortgeschrittene Benutzer bietet das wallet mehrere Einstellungen zur Feinabstimmung der Transaktion. standardmäßig ist "Replace-by-Fee" (RBF) aktiviert, eine wertvolle Funktion, die es Ihnen ermöglicht, eine Transaktion zu beschleunigen, wenn sie im Mempool stecken bleibt, indem sie mit einer höheren Gebühr erneut gesendet wird. Sie können auch manuell auswählen, welche "Unspent Transaction Outputs" (UTXOs) Sie ausgeben wollen. Dies ist ein leistungsfähiges Werkzeug für die UTXO-Konsolidierung, eine Strategie, bei der Sie mehrere kleine Eingänge zu einem einzigen größeren zusammenfassen. Dies kann zwar zu höheren Gebühren für die aktuelle Transaktion führen, kann aber die Gebühren für künftige Transaktionen erheblich senken, insbesondere wenn ein Anstieg der Netzgebühren zu erwarten ist.


![image](assets/en/15.webp)


PayJoin wird automatisch versucht, wenn Sie die Zahlungsanforderung eines Empfängers (eine BIP21-URI) scannen, die einen "pj="-Parameter enthält. Wenn Sie einfach eine einfache Adresse ohne zusätzliche Parameter einfügen, wird diese Funktion nicht aktiviert. Diese kollaborative Methode verbessert den Schutz der Privatsphäre, indem sie die Eingaben von Sender und Empfänger kombiniert und so die Heuristik des gemeinsamen Besitzes von Eingaben durchbricht und unter bestimmten Umständen eine bessere Skalierung und Gebühreneinsparungen ermöglicht.


### Senden an den Liquid Network


Das Liquid Network ist für schnelle, vertrauliche Transaktionen mit minimalen Gebühren konzipiert. Wenn Sie Geld über Liquid senden, wird es von Ihrem "Instant Payments Wallet" abgehoben. Das Verfahren ist unkompliziert: Sie geben einfach die Liquid-Adresse des Empfängers ein oder scannen sie.


Wenn in der Adresse kein Betrag angegeben ist, werden Sie auf dem Sendebildschirm aufgefordert, einen Betrag anzugeben. Sie können den Betrag in BTC, Satoshis oder Fiat eingeben. Ein wesentlicher Vorteil von Liquid ist die niedrige Mindestschwelle. Wie bei on-chain-Transaktionen können Sie optional eine persönliche Notiz für Ihre eigenen Unterlagen hinzufügen. Wenn die Zahlungsanforderung bereits einen Betrag enthält, wird der wallet direkt zum Bestätigungsbildschirm weitergeleitet.


Auf dem Bestätigungsbildschirm für eine Liquid-Transaktion können Sie die Details überprüfen. Die Gebühren sind bemerkenswert niedrig und werden auf der Grundlage der Komplexität der Transaktion berechnet. Sie liegen in der Regel bei 0,1 sat/vB, was bei einer einfachen Transaktion nur 20-40 satoshis ausmacht (zum Beispiel 26 satoshis zum 21. Dezember 2025).


![image](assets/en/16.webp)


### Senden an den Lightning Network


Sie können entweder einen Lightning Address (z. B. "runningbitcoin@rizful.com") scannen, der es Ihnen ermöglicht, den Betrag und eine optionale Notiz für den Empfänger festzulegen, oder Sie scannen eine Rechnung mit einem vordefinierten Betrag, die Sie direkt zum Bestätigungsbildschirm führt.


*Beachten Sie, dass Mindestbeträge und Gebühren anfallen.*


Das Bull Bitcoin Wallet sendet Lightning-Zahlungen, indem es Gelder von Ihrem "Instant Payments Wallet" (auf Liquid) abhebt und sie über "Boltz" austauscht. Dieser hybride Ansatz ist vollständig selbstverwaltend und vermeidet die hohen on-chain-Gebühren für die Verwaltung eines dedizierten Lightning-Kanals, erfordert jedoch die Zahlung einer "Swap-Gebühr". Am günstigsten ist es, direkt an die Liquid-Adresse des Empfängers zu senden, wenn dieser auch einen Bull Bitcoin wallet verwendet.


## 🔟 Übertragen von Geldern zwischen Ihren Geldbörsen


Mit Bull Bitcoin können Sie Ihr Bitcoin zwischen Ihrem "Secure Bitcoin" wallet und Ihrem "Instant Payments Wallet" auf dem Liquid Network oder einem "externen Wallet" verschieben. Um eine Übertragung durchzuführen, navigieren Sie einfach zum Abschnitt "Übertragung", wählen Sie die Quell- und Ziel-Geldbörse aus, geben Sie den Betrag ein, den Sie übertragen möchten, und bestätigen Sie die Transaktion.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Wiederherstellung Ihres Bull Bitcoin Wallet


In diesem Abschnitt wird erklärt, wie Sie wieder Zugriff auf Ihre Bull Bitcoin Wallet-Gelder erhalten, wenn Sie Ihr Gerät verlieren, die App deinstallieren oder einfach zu einem neuen Gerät wechseln müssen. Wie bereits erläutert, gibt es zwei primäre Methoden für die Wiederherstellung: die Verwendung der einzigartigen "Recoverbull"-Methode und die Verwendung eines standardmäßigen "BIP39 seed-Satzes".


### Methode 1: Recoverbull


Wiederholung: Wallet-Backups werden lokal verschlüsselt. Die verschlüsselte Datei kann im Cloud-Speicher oder auf einem anderen Gerät gespeichert werden. Der Verschlüsselungsschlüssel wird auf dem Recoverbull Key Server gespeichert. Beide werden getrennt gehalten und müssen kombiniert werden, um ein wallet wiederherzustellen.


Zunächst werde ich den Wallet mit allen darauf befindlichen Geldern löschen und den wallet neu installieren. Wir landen wieder auf dem "Willkommensbildschirm". Diesmal wählen Sie die Option "Wallet wiederherstellen". Navigieren Sie dann zur Methode "Verschlüsselter Tresor", bestätigen Sie die Verwendung des "Standard-Schlüsselservers" und wählen Sie den Ort oder den "Tresoranbieter", an dem Sie die Sicherungsdatei gespeichert haben.


![image](assets/en/18.webp)


Es wird angezeigt, dass der Tresor erfolgreich importiert wurde. Tippen Sie auf die Schaltfläche "Tresor entschlüsseln" und geben Sie die "PIN" ein. Der nächste Bildschirm zeigt Ihre "Salden" und die "Anzahl der Transaktionen", die wiederhergestellt wurden.


![image](assets/en/19.webp)


### Methode 2: Seed Phrase


Bei dieser Methode wird die Master-Wiederherstellungsphrase Ihres wallet verwendet, eine Standardliste mit 12 Wörtern, die als ultimatives Backup für Ihr Geld dient. Es ist die universellste Methode zur Wiederherstellung eines Bitcoin wallet, da sie nicht an einen bestimmten Dienst oder Server gebunden ist. Solange Sie diese Phrase haben, können Sie Ihren wallet auf jedem kompatiblen Gerät wiederherstellen, auch ohne Zugriff auf den Bull Bitcoin Key Server.


Wählen Sie auf dem Willkommensbildschirm "Wallet wiederherstellen". Wählen Sie dieses Mal die Methode "Physikalische Sicherung". Die App zeigt ein Raster von Wörtern an. Wählen Sie sorgfältig jedes Wort Ihres 12-Wort-seed-Satzes in der richtigen Reihenfolge aus. Seien Sie akribisch, denn ein einziger Fehler führt zu einem falschen wallet.


## 1️⃣2️⃣ Anschließen eines Hardware Wallet


Um ein Höchstmaß an Sicherheit zu gewährleisten, entscheiden sich viele Bitcoin-Benutzer dafür, ihr Guthaben in einem "kalten Speicher" aufzubewahren. Das bedeutet, dass die "privaten Schlüssel", die Ihr Bitcoin steuern, auf einem Gerät aufbewahrt werden, das niemals mit dem Internet verbunden ist. Ein "Hardware-wallet" (oder Signiergerät) ist ein spezielles physisches Gerät, das genau für diesen Zweck entwickelt wurde. Es fungiert wie ein digitaler Tresor für Ihre Schlüssel und stellt sicher, dass sie niemals den potenziellen Bedrohungen eines Online-Computers oder Smartphones ausgesetzt sind.


Wenn Sie ein Hardware-wallet an die Bull Bitcoin-App anschließen, erhalten Sie das Beste aus beiden Welten: die kompromisslose Sicherheit des Kältespeichers für Ihre privaten Schlüssel, kombiniert mit den leistungsstarken Funktionen und der benutzerfreundlichen Oberfläche des Bull Bitcoin wallet zur Anzeige von Salden und zur Verwaltung von Transaktionen. In diesem letzten Kapitel zeigen wir Ihnen, wie Sie ein Hardware-wallet, wie z. B. eine [Coldcard Q](https://coldcard.com/q), an Ihr Bull Bitcoin wallet anschließen. Die Einrichtung einer Coldcard Q wird in diesem Lernprogramm nicht ausführlich behandelt; darüber können Sie sich hier informieren:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Importieren eines Wallet


![image](assets/en/26.webp)


Wählen Sie zunächst im Hauptmenü Ihrer Coldcard Q "Wallet exportieren" und dann "Bull Wallet". Ihre Coldcard wird generate einen QR-Code.


![image](assets/en/20.webp)


Öffnen Sie das Bull Bitcoin Wallet und navigieren Sie zu "Einstellungen" > "Bitcoin-Einstellungen" > "wallet importieren". Wählen Sie auf Ihrem Telefon "Coldcard Q" und tippen Sie auf "Kamera öffnen", um diesen QR-Code zu scannen und die öffentlichen Schlüssel Ihres wallet zu importieren.


![image](assets/en/21.webp)


### Empfangen mit Coldcard Q


Um Bitcoin mit Ihrer angeschlossenen Coldcard Q zu empfangen, muss das Gerät nicht physisch mit Ihrem Telefon verbunden sein. Das Bull Bitcoin Wallet hat die erforderlichen öffentlichen Schlüssel bereits importiert, so dass es selbständig generate-Adressen empfangen kann.


1. Tippen Sie auf Ihr importiertes Coldcard Q-Signiergerät und wählen Sie `Empfangen`.

2. Die App zeigt automatisch eine neue Bitcoin-Adresse aus dem wallet Ihrer Coldcard an.

3. Verwenden Sie diese Adresse, um Geldmittel zu erhalten. Das Bitcoin wird direkt mit den Schlüsseln des wallet gesichert, auch wenn das Gerät während des Vorgangs offline war.


![image](assets/en/22.webp)


### Versenden mit Coldcard Q


Das Senden von Bitcoin mit Ihrer Coldcard Q erfordert Ihre physische Bestätigung, um jede Transaktion zu autorisieren. Während die Bull Wallet App verwendet wird, um die Transaktion zu erstellen, kann die endgültige Signatur nur auf der Hardware wallet selbst erstellt werden.


Öffnen Sie zunächst Ihre "Coldcard Q" wallet und tippen Sie auf "Senden". Öffnen Sie dann "die Kamera", um den QR-Code der Empfängeradresse zu scannen. Geben Sie nach dem Scannen den "Betrag" ein, den Sie senden möchten, und passen Sie die "Gebührenpriorität" nach Bedarf an.


Weitere Optionen finden Sie unter "Erweiterte Einstellungen". Hier finden Sie die Option "Ersetzen durch Gebühr" (RBF), die standardmäßig aktiviert ist und es Ihnen ermöglicht, eine festgefahrene Transaktion später zu beschleunigen. Außerdem steht Ihnen die Option "Coin Control" zur Verfügung, mit der Sie die spezifischen UTXOs, die Sie ausgeben möchten, manuell auswählen können.


Sobald Sie alle Details überprüft haben, tippen Sie auf "PSBT anzeigen", um die Transaktion vorzubereiten.


![image](assets/en/23.webp)


Tippen Sie auf die Schaltfläche "Scannen" auf Ihrer Coldcard Q und verwenden Sie die Kamera, um den auf Ihrem Telefon angezeigten QR-Code zu scannen. Auf dem Coldcard-Bildschirm werden Ihnen dann alle Transaktionsdetails angezeigt. Überprüfen Sie sorgfältig den Betrag, die Empfängeradresse und Ihre Änderungsadresse. Wenn alles korrekt ist, drücken Sie die "Enter"-Taste auf der Coldcard Q, um die Transaktion zu unterschreiben. Anschließend erscheint ein QR-Code der signierten Transaktion auf dem Bildschirm.


![image](assets/en/24.webp)


Tippen Sie auf dem Bull wallet auf "Ich bin fertig" und dann auf die Schaltfläche "Kamera", um den QR-Code der "signierten Transaktion" von Ihrer Coldcard Q zu scannen. Überprüfen Sie diese ein letztes Mal und tippen Sie dann auf "Transaktion senden". Damit wird der Vorgang abgeschlossen, indem die Transaktion an das Bitcoin-Netzwerk gesendet wird, und Ihr Geld ist auf dem Weg.


## 🎯 Schlussfolgerung


Sie haben nun Ihre Reise durch die Bull Bitcoin Wallet abgeschlossen. Die App stellt Ihnen leistungsstarke Datenschutz- und Sicherheitstools zur Verfügung und macht fortschrittliche Funktionen einfach zu nutzen. Mit Funktionen wie "PayJoin", das Ihre Transaktionen auf der Blockchain verbirgt, und "Tor-Integration", die Ihre Netzwerkaktivitäten vor neugierigen Blicken verbirgt, können Sie Ihre Privatsphäre wahren. Wer die ultimative Kontrolle haben möchte, kann sich mit seinem "eigenen persönlichen Bitcoin-Knoten" verbinden, um sich nicht mehr auf die Server von Drittanbietern verlassen zu müssen, und einen "Hardware-wallet" verwenden, um seine privaten Schlüssel vollständig offline und sicher zu halten. Mit intelligenten Backup-Optionen und nahtloser Unterstützung für Bitcoin, Liquid und Lightning ist der Bull Bitcoin Wallet eine starke, allumfassende Wahl für alle, denen es ernst damit ist, ihre Gelder privat, sicher und vollständig unter ihrer eigenen Kontrolle zu halten.


## 📚 Bull Wallet Ressourcen


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Website ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)