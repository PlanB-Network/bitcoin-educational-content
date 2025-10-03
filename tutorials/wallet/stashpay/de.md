---
name: StashPay
description: Der minimalistische Bitcoin Wallet für alle
---

![cover](assets/cover.webp)



Die Benutzerfreundlichkeit ist ein Schlüsselfaktor für die Annahme von Bitcoin-Lösungen auf der ganzen Welt. Die Bereitstellung einer reibungslosen, einfachen und technisch unbelasteten Erfahrung ist die Priorität für viele Geldbörsen und Exchange-Plattformen. In dieser Hinsicht zeichnet sich StashPay durch seinen minimalistischen Ansatz aus, während es gleichzeitig die Leistungsfähigkeit von Lightning Network demonstriert.



In diesem Tutorial werden wir einen Blick auf dieses Portfolio werfen, um herauszufinden, wie es funktioniert und wie es ideal für kleine Unternehmen oder Solopreneure ist.



## Erste Schritte mit StashPay



StashPay ist ein selbstverwaltender Wallet, der vor allem für seine minimalistische, benutzerorientierte Benutzererfahrung bekannt ist.  Mit diesem Wallet brauchen Sie keine technischen Kenntnisse, um Ihre ersten Satoshis zu empfangen und zu senden.



StashPay ist ein Open-Source-Projekt, das in React Native entwickelt wurde und darauf abzielt, das Problem der hohen Transaktionsgebühren selbst bei Transaktionen auf der Hauptkette des Bitcoin-Protokolls zu lösen. Es ist als mobile App für Android- und iOS-Plattformen über Download-Links auf der [Website] (https://stashpay.me/) verfügbar.



![introduce](assets/fr/01.webp)



Es ist wichtig, dass Sie die Android-Anwendung von der Website herunterladen, da sie nicht im Google Play Store verfügbar ist.


Wenn der Download abgeschlossen ist, erteilen Sie bitte die erforderlichen Berechtigungen, damit Sie die Anwendung auf Ihrem Android-Telefon installieren können.



Nach der Installation der Anwendung erstellt StashPay beim ersten Öffnen der Anwendung einen Bitcoin Wallet für Sie. Vor jeder Transaktion empfehlen wir Ihnen, eine Sicherungskopie dieser Wallet zu erstellen. Im Folgenden finden Sie alle unsere Richtlinien, um sicherzustellen, dass Ihre Wiederherstellungsphrasen ordnungsgemäß gesichert sind.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Greifen Sie auf die StashPay-Einstellungen zu, indem Sie auf das Symbol "Einstellungen" und dann auf die Option **Sicherung erstellen** klicken. Genehmigen Sie dann die Anzeige der Wiederherstellungsphrasen. Kopieren Sie Ihre Wiederherstellungsphrasen nicht in die Zwischenablage Ihres Telefons, da sie für andere betrügerische Anwendungen, die auf Ihrem Mobiltelefon installiert sind, zugänglich sein könnten.



![backup](assets/fr/02.webp)



Sie können auch einen Bitcoin Wallet abrufen, den Sie bereits verwenden, indem Sie auf die Option **Wallet wiederherstellen** klicken und Ihre 12 oder 24 Wiederherstellungswörter einfügen.



### Erhalten Sie Ihre ersten Satoshis auf StashPay



Klicken Sie auf dem Startbildschirm auf die Schaltfläche **Empfangen** und geben Sie einen Betrag ein, der größer ist als der in Rot angegebene Betrag. In unserem Fall können wir nicht weniger als 0,11 USD mit dem StashPay Wallet erhalten.



![receive](assets/fr/03.webp)



Sobald Sie den Betrag festgelegt haben, können Sie auf die Schaltfläche **Invoice erstellen** klicken und dann den Invoice einscannen oder kopieren, um ihn an den Absender der Satoshis zu senden.



![receive_sats](assets/fr/04.webp)



Sie können Ihren Transaktionsverlauf einsehen, indem Sie auf das Symbol "Uhr" auf der Startseite klicken.



![network_fee](assets/fr/05.webp)



Sie werden bemerkt haben, dass Sie für den Erhalt von Satoshis eine Netzgebühr zahlen müssen. Diese Gebühren werden von den Satoshis, die Sie erhalten werden, abgezogen. Das liegt daran, dass StashPay ein Wallet ist, der auf dem Breez Development Kit basiert. Um Satoshis mit der Lightning-Knoten-freien Implementierung des Kits zu erhalten, berechnet Breez dem Kunden (in unserem Fall StashPay) `0,25% + 40 Satoshis`. Erfahren Sie mehr in unserem Misty Breez-Tutorial.



https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Bitcoins mit StashPay versenden



Das Senden von Bitcoins mit StashPay ist dank des minimalistischen Interface ziemlich intuitiv. Klicken Sie auf dem Startbildschirm auf die Schaltfläche **Senden**. Scannen Sie den QR-Code oder fügen Sie den Address ein, an den Sie Satoshis senden möchten. StashPay erkennt automatisch die Bitcoin-Protokollkette, an die Sie Bitcoins senden möchten.



![send](assets/fr/06.webp)



Da StashPay ein Wallet ist, das auf dem Breez Development Kit basiert, profitiert es von einem interessanten Vorteil: Es kann Bitcoins auf der Hauptkette zu geringen Kosten versenden. Breez nutzt den Boltz-Service, um Transaktionen zwischen den verschiedenen Chains des Bitcoin-Protokolls durchzuführen, so dass Kunden, die das Development Kit implementieren, von diesem Service direkt in ihrer Anwendung profitieren können.



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Das Breez SDK schreibt jedoch einen Mindestbetrag vor, ab dem Sie Bitcoins an einen Address auf der Hauptkette senden können.



![onchain](assets/fr/07.webp)



Sie können Bitcoins auch mit dem Lightning Address des Empfängers senden. Überprüfen Sie Ihre Transaktionsdetails und bestätigen Sie dann mit einem Klick auf die Schaltfläche **Senden**.



![confirm](assets/fr/08.webp)



## Mehr Konfigurationen



In den StashPay-Einstellungen können Sie Konfigurationen anpassen, um Ihre Nutzung des Wallet zu personalisieren.



Mit StashPay können Sie Exchange Satoshis in der lokalen Währung Ihrer Wahl kaufen. Klicken Sie auf die Option **Währungen** und suchen Sie dann nach Ihrer Währung in der Liste der +113 von StashPay angebotenen Währungen.



![currencies](assets/fr/09.webp)



Im Menü **Empfangsoptionen** finden Sie alle Einstellungen für den Empfang von Bitcoins mit StashPay. Wählen Sie zum Beispiel **Lightning oder Onchain**, um Ihren Wallet für den Empfang von Bitcoins von der Hauptkette zu aktivieren.



![receive-onchain](assets/fr/10.webp)



Mit der Option **OnChain-Adressen scannen** können Sie den Kontostand Ihres Wallet aktualisieren, indem Sie alle UTXOs (Bitcoins, die Sie noch nicht ausgegeben haben) überprüfen, die mit Ihren verschiedenen Adressen verbunden sind.



![rescan](assets/fr/11.webp)



Das Menü **Protokoll exportieren** listet alle Aktionen der Breez- und Boltz-Infrastruktur auf, die Ihre Transaktionen und den atomaren Austausch zwischen den verschiedenen Bitcoin-Protokollketten betreffen.



![export](assets/fr/12.webp)



Sie haben sich gerade mit dem minimalistischen Bitcoin Wallet von StashPay vertraut gemacht. Wenn Sie diese Anleitung nützlich fanden, empfehlen wir Ihnen unsere Anleitung, wie Sie mit Bitcoin beginnen und Ihre ersten Bitcoins verdienen.



https://planb.network/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f