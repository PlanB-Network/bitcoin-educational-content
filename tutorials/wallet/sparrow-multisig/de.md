---
name: Sparrow Wallet - Multisig
description: Erstellen einer Multisig-Wallet mit Sparrow
---
![cover](assets/cover.webp)


Eine Multisignatur-Wallet (oft "*Multisig*" genannt) ist eine Bitcoin-Wallet-Struktur, die mehrere kryptografische Signaturen von verschiedenen Schlüsseln erfordert, um eine Ausgabe zu autorisieren. Anders als bei einer herkömmlichen ("*Singlesig*") Wallet, bei der ein einzelner privater Schlüssel ausreicht, um ein UTXO freizugeben, basiert die Multisig auf einem **m-von-n**-Modell: von den _n_ Schlüsseln der Wallet müssen zwingend _m_ jede Transaktion gemeinsam signieren.


Dieser Mechanismus ermöglicht es, die Kontrolle über eine Wallet auf mehrere Einheiten oder Geräte zu verteilen. In einer 2-von-3-Konfiguration werden beispielsweise drei unabhängige Schlüsselsätze erzeugt, aber nur zwei davon werden benötigt, um Gelder freizugeben. Diese Architektur verringert die mit Kompromittierung oder Verlust eines Schlüssels verbundenen Risiken drastisch: Ein Dieb mit Zugriff auf nur einen Schlüssel kann die Wallet nicht leeren, und ein Benutzer, der einen Schlüssel verliert, hat mit den verbleibenden zwei weiterhin Zugriff auf seine Gelder.


![Image](assets/fr/01.webp)


Diese höhere Sicherheit geht jedoch mit größerer Komplexität einher. Die Einrichtung einer Multisig-Wallet erfordert die Sicherung mehrerer Mnemonic-Phrasen (eine pro Signaturfaktor) sowie erweiterter öffentlicher Schlüssel ("*xpub*"). Wenn Sie nämlich eine Multisig-2-von-3-Wallet verwenden, benötigen Sie zur Wiederherstellung der Wallet entweder alle drei Mnemonic-Phrasen oder mindestens zwei der drei Phrasen. Wenn Sie jedoch nur zwei der drei Phrasen besitzen, benötigen Sie zusätzlich Zugriff auf die drei *xpubs*, ohne die es unmöglich ist, die öffentlichen Schlüssel wiederzuerlangen, die zum Zugriff auf die damit geschützten Bitcoins nötig sind.


Zusammengefasst benötigen Sie zur Wiederherstellung einer Multisig-Wallet Folgendes:


- Entweder Zugriff auf alle Mnemonic-Phrasen der einzelnen Signaturfaktoren;
- Oder die vom Schwellenwert geforderte Mindestanzahl an Mnemonic-Phrasen, um signieren zu können, zusätzlich zum Zugriff auf die xpubs aller Faktoren, um die benötigten öffentlichen Schlüssel wiederherzustellen.


![Image](assets/fr/02.webp)


Diese Verwaltung von Multisig-Wallet-Backups wird durch *Output Script Descriptors* erleichtert, die alle für den Zugriff auf die Gelder erforderlichen öffentlichen Daten bündeln. Diese Funktion ist jedoch noch nicht in jeder Wallet-Software implementiert.


Multisig eignet sich besonders für Bitcoiner, die erhöhte Sicherheit oder eine gemeinsame Verwaltung ihrer Gelder suchen: Unternehmen, Vereine, Familien oder einzelne Nutzer mit erheblichen Bitcoin-Beständen. Es lässt sich nutzen, um dezentrale Governance-Modelle aufzubauen, zum Beispiel um die Signaturbefugnis auf mehrere Verantwortliche oder Teammitglieder zu verteilen.


In diesem Tutorial lernen wir, wie man eine klassische Multisignatur-Wallet mit **Sparrow Wallet** erstellt und nutzt. Wenn Sie eine individualisierte Multisignatur-Wallet mit Timelocks erstellen möchten, empfehle ich Ihnen stattdessen Liana:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Voraussetzungen


In diesem Tutorial zeige ich Ihnen, wie Sie eine Multisig mit der [Sparrow-Wallet-Verwaltungssoftware](https://sparrowwallet.com/download/) erstellen. Falls Sie diese Software noch nicht installiert haben, tun Sie dies bitte jetzt. Wenn Sie dabei Hilfe benötigen, haben wir auch ein ausführliches Tutorial zur Konfiguration von Sparrow Wallet:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Um eine Multisignatur-Wallet einzurichten, benötigen Sie verschiedene Hardware-Wallets. Für eine Multisig 2-von-3 könnten Sie beispielsweise Folgendes verwenden:


- Ein Trezor Model One;
- Ledger Flex;
- Ein Passport Core.


![Image](assets/fr/03.webp)


Es empfiehlt sich, in Ihrer Multisig-Konfiguration Hardware-Wallets unterschiedlicher Hersteller zu verwenden. So wird sichergestellt, dass ein schwerwiegendes Problem bei einem bestimmten Modell die Gesamtsicherheit Ihrer Multisig nicht beeinträchtigt. Zudem profitieren Sie so von den spezifischen Vorteilen jedes Geräts. In meiner Konfiguration zum Beispiel:



- Der Trezor Model One ist vollständig quelloffen, wodurch sich die Seed-Generierung überprüfen lässt. Da er jedoch nicht mit einem Secure Element ausgestattet ist, bleibt er anfällig für physische Angriffe;



- Der Ledger Flex hingegen profitiert von nicht überprüfbarer proprietärer Firmware, verfügt aber über ein Secure Element, das einen ausgezeichneten physischen Schutz bietet;



- Der Passport Core kombiniert vollständig quelloffene Firmware, ein Secure Element und air-gapped QR-Code-Austausch. Er ist ein unabhängiger dritter Signierer, der Adressen verifizieren und PSBTs ohne USB-Datenverbindung signieren kann.


Bevor Sie Ihre Multisig-Wallet konfigurieren, stellen Sie sicher, dass jede Hardware-Wallet korrekt eingerichtet ist (Mnemonic-Erzeugung und -Sicherung, PIN-Festlegung). Genaue Anleitungen finden Sie in unseren Tutorials zu den jeweiligen Hardware-Wallets, zum Beispiel:


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Wie wir später in diesem Tutorial sehen werden, ist es auch möglich, in Ihre Multisig-Konfiguration einen Faktor einzubinden, der nicht an eine Hardware-Wallet gebunden ist, dessen private Schlüssel aber auf Ihrem PC gespeichert sind. Diese Methode ist naturgemäß weniger sicher als die ausschließliche Nutzung von Hardware-Wallets, kann aber in bestimmten Fällen sinnvoll sein. Für eine Multisig 2-von-3 könnten Sie sich beispielsweise für zwei Hardware-Wallets und eine Software-Wallet entscheiden.

> ⚠️ **Sicherheitshinweis Coldcard MK3:** Erstellen Sie keinen neuen Seed auf einem MK3 mit einer Firmware älter als 4.2.0. Auf älteren Firmware-Versionen erzeugte Seeds müssen ersetzt und die Gelder verschoben werden. Dieses Tutorial verwendet daher Passport Core als air-gapped Referenz-Signierer.


## Erstellen einer Multisig-Wallet


Öffnen Sie Sparrow Wallet, klicken Sie auf den Tab "*File*" und wählen Sie dann "*New Wallet*".


![Image](assets/fr/04.webp)


Vergeben Sie einen Namen für Ihre Multisignatur-Wallet und klicken Sie dann zur Bestätigung auf "*Create Wallet*".


![Image](assets/fr/05.webp)


Wählen Sie im Dropdown-Menü "*Policy Type*" die Option "*Multi Signature*".


![Image](assets/fr/06.webp)


Oben rechts können Sie nun die Gesamtzahl der Schlüssel Ihrer Multisig sowie die Anzahl der für eine Ausgabe erforderlichen Mitunterzeichner festlegen. In meinem Beispiel handelt es sich um ein 2-von-3-Schema.


![Image](assets/fr/07.webp)


Am unteren Rand des Fensters zeigt Sparrow Wallet drei "*Keystore*" an. Jeder steht für einen Schlüsselsatz. Da ich hier drei Hardware-Wallets verwende, entspricht jeder "*Keystore*" einer davon. Wir konfigurieren sie nun.


Ich beginne mit dem Passport Core. Im Tab "*Keystore 1*" wähle ich die Option "*Airgapped Hardware Wallet*".


![Image](assets/fr/08.webp)


Öffnen Sie auf dem Passport das gewünschte Konto und wählen Sie dann "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". Das Passport zeigt einen animierten QR-Code mit seinen Informationen zum öffentlichen Schlüssel an.

Wählen Sie in Sparrow "*Scan...*" neben "*Passport*" und scannen Sie diesen animierten QR-Code mit der Webcam Ihres Computers. Vergleichen Sie den von Sparrow angezeigten Master-Key-Fingerabdruck mit dem auf dem Passport angezeigten und importieren Sie anschließend den Keystore.

Ihr Passport-xpub wurde nun importiert. Wiederholen Sie das entsprechende Vorgehen für den Ledger Flex und den Trezor Model One.


Für den Ledger Flex wähle ich "*Keystore 2*" und klicke dann auf "*Connected Hardware Wallet*". Stellen Sie sicher, dass der Ledger mit dem Computer verbunden, entsperrt und die Bitcoin-Anwendung geöffnet ist.


![Image](assets/fr/15.webp)


Klicken Sie dann auf die Schaltfläche "*Scan...*".


![Image](assets/fr/16.webp)


Klicken Sie neben dem Namen Ihrer Hardware-Wallet auf "*Import Keystore*".


![Image](assets/fr/17.webp)


Der zweite Unterzeichner ist nun korrekt in Sparrow Wallet registriert.


![Image](assets/fr/18.webp)


Ich wiederhole exakt denselben Vorgang mit dem Trezor One, um die Multisig-Konfiguration abzuschließen.


![Image](assets/fr/19.webp)


In meiner Konfiguration decken wir diesen Fall nicht ab, aber wenn Sie eine Signatur über eine Software-Wallet in Sparrow (Hot Wallet) in Ihre Multisig einbinden möchten, klicken Sie einfach auf die Schaltfläche "*New or Imported Software Wallet*".


Nachdem nun alle Ihre Signaturgeräte in Sparrow Wallet importiert sind, können Sie die Erstellung der Multisig durch Klicken auf "*Apply*" abschließen.


![Image](assets/fr/20.webp)


Wählen Sie ein starkes Passwort, um den Zugriff auf Ihre Sparrow-Wallet zu sichern. Dieses Passwort schützt Ihre öffentlichen Schlüssel, Adressen, Labels und den Transaktionsverlauf vor unbefugtem Zugriff.


Denken Sie daran, dieses Passwort an einem sicheren Ort, etwa in einem Passwort-Manager, zu speichern, damit Sie es nicht verlieren.


![Image](assets/fr/21.webp)


## Sichern einer Multisig-Wallet


Wir speichern nun den *Output Script Descriptor* auf einem unabhängigen Datenträger und bewahren mehrere Kopien davon auf.


Der *Descriptor* enthält alle xpubs Ihrer Multisig-Wallet sowie die zur Schlüsselerzeugung verwendeten Ableitungspfade. Erinnern Sie sich an Teil 1: Um eine Multisig-Wallet wiederherzustellen, benötigen Sie entweder **alle** Mnemonic-Phrasen oder nur die zum Erreichen des Signaturschwellenwerts erforderliche Mindestanzahl. Im letzteren Fall ist es jedoch ebenfalls unerlässlich, **die xpubs** der fehlenden Unterzeichner zu besitzen. Der *Descriptor* enthält alle xpubs Ihrer Multisig.


Falls dies nicht klar ist, merken Sie sich einfach Folgendes: Um eine Multisig wiederherzustellen, benötigen Sie je nach Schwellenwert die Mindestanzahl an Mnemonic-Phrasen für jede verwendete Hardware-Wallet (in meinem Fall: 2 Phrasen) sowie den *Descriptor*.


Dieser *Descriptor* enthält keine privaten Schlüssel, sondern nur öffentliche. Das bedeutet, er gewährt keinen Zugriff auf die Gelder. Er ist daher nicht so kritisch wie Mnemonic-Phrasen, die vollen Zugriff auf Ihre Bitcoins gewähren. Das Risiko beim *Descriptor* betrifft ausschließlich die Vertraulichkeit: Im Falle einer Kompromittierung könnte ein Dritter alle Ihre Transaktionen beobachten, aber nicht über Ihre Gelder verfügen.


Ich empfehle dringend, mehrere Kopien dieses *Descriptors* zu erstellen und sie zusammen mit jedem Signaturgerät Ihrer Multisig aufzubewahren. In meinem Fall beispielsweise drucke ich den *Descriptor* auf Papier aus und bewahre eine Kopie beim Passport, eine weitere beim Trezor und eine beim Ledger auf. Zusätzlich speichere ich diesen *Descriptor* als PDF-Datei auf drei USB-Sticks, die jeweils zusammen mit einer der Hardware-Wallets aufbewahrt werden. So maximiere ich meine Chancen, diesen *Descriptor* niemals zu verlieren, und stelle sicher, dass bei jedem Gerät zwei Kopien (eine physische und eine digitale) vorhanden sind.


Sobald Ihre Multisig-Wallet erstellt wurde, stellt Sparrow diesen *Descriptor* automatisch bereit. Klicken Sie auf die Schaltfläche "*Save PDF...*", um ihn sowohl als Text als auch als QR-Code zu speichern.


![Image](assets/fr/22.webp)


Sie können dieses PDF anschließend ausdrucken und auf Ihre USB-Sticks kopieren.


![Image](assets/fr/23.webp)


Das Passport nutzt die von Sparrow importierte Multisig-Konfiguration, um während des QR-Pairing- und Signaturvorgangs die relevanten Schlüsselinformationen anzuzeigen und zu überprüfen. Bewahren Sie den *Descriptor* unabhängig davon auf: Er bleibt unverzichtbar, um die Wallet wiederherzustellen, falls ein Unterzeichner nicht verfügbar ist.


Achten Sie neben der Speicherung des *Descriptors* auch besonders darauf, die Mnemonic-Phrasen jedes Ihrer Signaturgeräte zu sichern. Wenn Sie gerade erst anfangen, empfehle ich Ihnen sehr, dieses weitere Tutorial zu lesen, um zu erfahren, wie man sie richtig sichert und verwaltet:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Bevor Sie Ihre ersten Bitcoins auf Ihre Multisig empfangen, **rate ich Ihnen dringend, einen Wiederherstellungstest mit leerer Wallet durchzuführen**. Notieren Sie sich einige Referenzinformationen, etwa die erste Empfangsadresse, und setzen Sie dann Ihre Hardware-Wallets zurück, solange die Wallet noch leer ist. Versuchen Sie anschließend, Ihre Multisig-Wallet auf den Hardware-Wallets mithilfe Ihrer papierbasierten Mnemonic-Phrasen-Backups wiederherzustellen und danach in Sparrow mithilfe des *Descriptors*. Prüfen Sie, ob die nach der Wiederherstellung erzeugte erste Adresse mit der ursprünglich notierten übereinstimmt. Ist dies der Fall, können Sie sicher sein, dass Ihre Papier-Backups zuverlässig sind.


Um mehr darüber zu erfahren, wie man einen Wiederherstellungstest durchführt, empfehle ich Ihnen, dieses weitere Tutorial zu lesen:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bitcoins auf Ihrer Multisig empfangen


Ihre Wallet ist nun bereit, Bitcoins zu empfangen. Klicken Sie in Sparrow auf den Tab "*Receive*".


![Image](assets/fr/30.webp)


Bevor Sie die von Sparrow Wallet erzeugte Adresse verwenden, nehmen Sie sich die Zeit, sie direkt auf dem Bildschirm Ihrer Hardware-Wallets zu überprüfen. So stellen Sie sicher, dass die Adresse nicht verändert wurde und dass Ihre Geräte über die privaten Schlüssel verfügen, die zum Ausgeben der zugehörigen Gelder erforderlich sind. Dies schützt Sie vor einer Reihe von Angriffsvektoren.


Klicken Sie dazu auf "*Display Address*", um die Adresse bei einer Kabelverbindung auf Ihrem Trezor oder Ledger anzuzeigen.


![Image](assets/fr/31.webp)


Wählen Sie beim Passport das Multisig-Konto aus und wählen Sie "*Verify Address*". Scannen Sie den QR-Code der von Sparrow angezeigten Empfangsadresse. Das Passport bestätigt auf seinem Bildschirm, ob die Adresse zur Multisig-Wallet gehört.


Prüfen Sie, ob die auf jeder Hardware-Wallet angezeigte Adresse genau mit der in Sparrow Wallet übereinstimmt. Es empfiehlt sich, dies unmittelbar vor der Weitergabe der Adresse an den Zahler zu tun, um sich ihrer Integrität sicher zu sein.


Sie können dieser Adresse dann ein "*Label*" zuweisen, um die Herkunft der empfangenen Bitcoins zu kennzeichnen. Das ist eine gute Möglichkeit, die Verwaltung Ihrer UTXOs zu organisieren.


![Image](assets/fr/34.webp)


Sobald dies überprüft ist, können Sie die Adresse zum Empfangen von Bitcoins verwenden.


![Image](assets/fr/35.webp)


## Bitcoins mit Ihrer Multisig senden


Nachdem Sie nun Ihre ersten Sats auf Ihrer Multisig-Wallet empfangen haben, können Sie sie auch ausgeben! Gehen Sie in Sparrow zum Tab "*Send*", um eine neue Transaktion zu erstellen.


![Image](assets/fr/36.webp)


Wenn Sie *Coin Control* nutzen möchten, also die UTXOs, die Sie ausgeben möchten, manuell auswählen, gehen Sie zum Tab "*UTXOs*". Wählen Sie die UTXOs aus, die Sie ausgeben möchten, und klicken Sie dann auf "*Send Selected*". Sie werden automatisch zum Tab "*Send*" weitergeleitet, wobei die UTXOs bereits vorausgefüllt sind.


![Image](assets/fr/37.webp)


Geben Sie die Zieladresse ein. Durch Klicken auf "*+ Add*" können mehrere Adressen hinzugefügt werden.


![Image](assets/fr/38.webp)


Fügen Sie ein "*Label*" hinzu, um den Zweck dieser Ausgabe zu beschreiben und Ihre Transaktionen leichter nachverfolgen zu können.


![Image](assets/fr/39.webp)


Geben Sie den an die ausgewählte Adresse zu sendenden Betrag ein.


![Image](assets/fr/40.webp)


Passen Sie die Gebührenrate an die aktuellen Netzwerkbedingungen an. Konsultieren Sie zum Beispiel [Mempool.space](https://Mempool.space/), um ein geeignetes Gebührenniveau auszuwählen.


Klicken Sie nach der Überprüfung aller Transaktionsparameter auf "*Create Transaction*".


![Image](assets/fr/41.webp)


Wenn Sie mit allem zufrieden sind, klicken Sie auf "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


Am unteren Bildschirmrand sehen Sie, dass Sparrow auf 2 Signaturen wartet. Das ist normal: Die hier verwendete Wallet ist eine Multisig 2-von-3.


![Image](assets/fr/43.webp)


Ich beginne mit dem Signieren über mein Passport. Klicken Sie in Sparrow auf "*Show QR*", um die PSBT (*Partially Signed Bitcoin Transaction*) als animierte QR-Codes anzuzeigen. Wählen Sie auf dem Passport das Multisig-Konto und dann "*Sign with QR Code*" und scannen Sie den von Sparrow angezeigten QR-Code.


Prüfen Sie auf dem Bildschirm Ihrer Hardware-Wallet sorgfältig die Transaktionsparameter: die Adresse des Empfängers, den gesendeten Betrag und die Gebühren. Sobald die Transaktion bestätigt wurde, bestätigen Sie, um mit der Signatur fortzufahren.


Nachdem Sie die Transaktion genehmigt haben, zeigt das Passport die signierte PSBT als animierte QR-Codes an. Klicken Sie in Sparrow auf "*Scan QR*" und scannen Sie diese Codes mit Ihrer Webcam. Die Signatur des Passports wird daraufhin hinzugefügt. Für die zweite erforderliche Signatur verwende ich nun den Ledger: Ich verbinde und entsperre ihn und klicke dann in Sparrow auf "*Sign*".


![Image](assets/fr/48.webp)


Klicken Sie neben dem Namen Ihrer Hardware-Wallet auf "*Sign*".


![Image](assets/fr/49.webp)


Wenn Sie Ihren Ledger zum ersten Mal mit dieser Multisig verwenden, fordert Sparrow Sie auf, die erweiterten öffentlichen Schlüssel (xpubs) der Mitunterzeichner zu überprüfen. Wie beim Passport verhindert dieser Schritt, dass Sie später blind signieren. Vergleichen Sie zur Überprüfung dieser Informationen den auf dem Ledger-Bildschirm angezeigten xpub mit den direkt von Ihren anderen Hardware-Wallets bereitgestellten.


![Image](assets/fr/50.webp)


Überprüfen Sie die Adresse des Empfängers, den übertragenen Betrag und die Transaktionsgebühr, und signieren Sie dann die Transaktion.


![Image](assets/fr/51.webp)


Drücken Sie auf den Bildschirm, um zu signieren.


![Image](assets/fr/52.webp)


Sparrow verfügt nun über die beiden zur Freigabe der Gelder aus der Multisig-Wallet erforderlichen Signaturen. Überprüfen Sie die Transaktion ein letztes Mal, und klicken Sie, wenn alles in Ordnung ist, auf "*Broadcast Transaction*", um sie im Netzwerk zu verbreiten.


![Image](assets/fr/53.webp)


Sie finden diese Transaktion im Tab "*Transactions*" von Sparrow Wallet.


![Image](assets/fr/54.webp)


Herzlichen Glückwunsch, Sie wissen jetzt, wie man eine Multisignatur-Wallet auf Sparrow einrichtet und nutzt. Wenn Sie dieses Tutorial hilfreich fanden, würde ich mich über einen grünen Daumen unten freuen. Teilen Sie diesen Artikel gerne in Ihren sozialen Netzwerken. Danke fürs Teilen!


Um noch weiterzugehen, empfehle ich Ihnen, dieses Tutorial über eine weitere Methode zur Erhöhung der Sicherheit Ihrer Bitcoin-Wallet zu lesen, die BIP39-Passphrase:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
