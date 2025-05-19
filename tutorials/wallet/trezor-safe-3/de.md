---
name: Trezor Safe 3
description: Konfigurieren und Verwenden von Hardware Wallet Safe 3
---
![cover](assets/cover.webp)



*Bildnachweis: [Trezor.io](https://trezor.io/)*



Der Trezor Safe 3 ist ein Hardware Wallet, der von SatoshiLabs entworfen und im Jahr 2023 entwickelt wurde. Es ist ein sehr kompaktes, leichtes Modell (14 Gramm), das sowohl für Anfänger als auch für fortgeschrittene Nutzer entwickelt wurde. Er ist der Nachfolger des berühmten Model One mit bedeutenden Ergänzungen, wobei der Open-Source-Ansatz der Marke beibehalten wurde, der ihn von seinem Hauptkonkurrenten, dem Ledger, unterscheidet. Der Preis des Safe 3 liegt bei 79 €. Er ist damit im mittleren Hardware Wallet-Segment angesiedelt und steht in direktem Wettbewerb mit dem Ledger Nano S Plus.



Der Safe 3 hat keinen Akku und wird ausschließlich über einen USB-C-Anschluss betrieben, der sowohl für die Stromversorgung als auch für die Kommunikation genutzt wird. Er verfügt über ein kleines 0,96 Zoll großes monochromes OLED-Display und zwei physische Tasten.



![Image](assets/fr/01.webp)



Der Safe 3 bietet alle wesentlichen Funktionen, die man von einem guten Hardware Wallet erwartet, einschließlich der hervorragenden Integration des passphrase BIP39. Allerdings unterstützt er noch kein Miniscript.



Dieses Modell ist besonders für Anfänger geeignet und ist vielleicht sogar das Hardware Wallet, das ich einem neuen Benutzer empfehlen würde. Es ist auch für fortgeschrittene Benutzer gut geeignet. Andererseits erfüllt es vielleicht nicht alle Erwartungen von fortgeschrittenen Nutzern, die nach spezielleren Funktionen suchen, die bei Geräten wie der Coldcard verfügbar sind. Wenn Sie diese fortgeschrittenen Optionen nicht benötigen, kann das Trezor Safe 3 eine ausgezeichnete Wahl sein.



## Das Sicherheitsmodell Trezor Safe 3



Der Trezor Safe 3 ist jetzt mit einem EAL6+-zertifizierten **Secure Element** ausgestattet, einem bedeutenden Fortschritt gegenüber früheren Modellen wie dem Model One und dem Model T. Dabei handelt es sich um den OPTIGA Trust M V3-Chip, der das seed nicht direkt speichert, sondern als kryptografische Komponente fungiert, um den Zugriff darauf zu sichern. Das Secure Element speichert ein Geheimnis, auf das nur zugegriffen werden kann, wenn der Benutzer die PIN korrekt eingegeben hat. Dieses Geheimnis wird dann zur Entschlüsselung des seed verwendet, das verschlüsselt im Hauptspeicher des Geräts gespeichert ist.



Dieses hybride Sicherheitssystem bietet einen verbesserten physischen Schutz, insbesondere gegen Extraktionsangriffe oder invasive Analysen, Probleme, für die das Model One anfällig war, insbesondere bei der PIN-Verwaltung. Diese Schwachstellen werden nun dank der Verwendung des Secure Elements umgangen. Dieses Modell verfügt außerdem über eine Open-Source-Softwarearchitektur: Der Code, der die Erzeugung und Verwendung der privaten Schlüssel verwaltet, bleibt vollständig zugänglich und überprüfbar. Der OPTIGA-Chip verwaltet nur den PIN-Code, ein Element außerhalb der Bitcoin Wallet Schlüsselverwaltung. Er gibt nur ein Geheimnis frei, das zur Entschlüsselung des seed verwendet werden kann. Außerdem profitiert der OPTIGA Trust M V3 Chip von einer relativ freien Lizenz, die es SatoshiLabs erlaubt, potenzielle Sicherheitslücken frei zu veröffentlichen.



Dieses Sicherheitsmodell stellt meiner Meinung nach einen der besten Kompromisse dar, die es derzeit auf dem Markt gibt. Es kombiniert die Vorteile eines Secure Elements mit Open-Source-Softwaremanagement. Bisher mussten sich die Nutzer zwischen der verbesserten physischen Sicherheit eines Chips und der Transparenz von Open-Source-Software entscheiden; mit Trezor Safe 3 ist es möglich, von beidem zu profitieren.



In diesem Tutorial zeigen wir Ihnen, wie Sie Ihren Trezor Safe 3 sicher einrichten und verwenden können.



## Auspacken des Trezor Safe 3



Wenn Sie Ihr Safe 3 erhalten, vergewissern Sie sich, dass die Verpackung und der Seal unversehrt sind, um sicherzustellen, dass das Paket nicht geöffnet wurde. Eine Softwareüberprüfung der Authentizität und Integrität des Geräts wird auch bei der späteren Einrichtung durchgeführt.



Inhalt der Box: :




- Trezor Safe 3;
- Ein Beutel, der Kartenmaterial zum Aufzeichnen Ihres Mnemonic-Spruchs, Aufkleber und eine Anleitung enthält;
- USB-C-auf-USB-C-Kabel.



![Image](assets/fr/02.webp)



Wenn du dein Trezor Safe 3 öffnest, sollte es durch eine Schutzfolie geschützt sein und der USB-C-Anschluss sollte durch ein holografisches Seal gesichert sein. Stellen Sie sicher, dass es da ist.



![Image](assets/fr/03.webp)



Die Navigation auf dem Gerät ist einfach: Verwenden Sie die rechte Taste, um nach rechts zu blättern, und die linke Taste, um nach links zu blättern. Drücken Sie beide Tasten gleichzeitig, um eine Aktion zu bestätigen.



![Image](assets/fr/04.webp)



## Voraussetzungen



In diesem Tutorial zeige ich Ihnen, wie Sie den Trezor Safe 3 mit der [Sparrow Wallet Portfolio Management Software] (https://sparrowwallet.com/download/) verwenden können. Wenn Sie diese Software noch nicht installiert haben, sollten Sie dies jetzt tun. Falls Sie Hilfe benötigen, haben wir auch eine ausführliche Anleitung zur Konfiguration von Sparrow Wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Außerdem benötigen Sie die Trezor Suite Software, um den Safe 3 zu konfigurieren, seine Authentizität zu überprüfen und die Firmware zu installieren. Wir werden diese Software nur zu diesem Zweck verwenden, und danach wird sie nur noch für Firmware-Updates benötigt. Für die tägliche Verwaltung des Wallet werden wir ausschließlich Sparrow Wallet verwenden, da es für Bitcoin optimiert und auch für Anfänger leicht zu bedienen ist (Sparrow unterstützt nur Bitcoin, keine Altcoins).



[Trezor Suite von der offiziellen Website herunterladen](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



Bei diesen beiden Programmen empfehle ich Ihnen dringend, sowohl ihre Authentizität (mit GnuPG) als auch ihre Integrität (über Hash) zu überprüfen, bevor Sie sie auf Ihrem Rechner installieren. Wenn Sie nicht wissen, wie man das macht, können Sie diese andere Anleitung befolgen:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Trezor Safe 3 starten



Schließen Sie Ihren Safe 3 an Ihren Computer an, auf dem die Trezor Suite und Sparrow Wallet bereits installiert sind.



![Image](assets/fr/06.webp)



Öffnen Sie die Trezor Suite und klicken Sie auf "*Meinen Trezor einrichten*".



![Image](assets/fr/07.webp)



Wählen Sie "*Bitcoin-only-Firmware*" und klicken Sie dann auf "*Install Bitcoin-only*".



![Image](assets/fr/08.webp)



Die Trezor Suite installiert dann die Firmware auf Ihrem Safe 3. Bitte warten Sie während der Installation.



![Image](assets/fr/09.webp)



Klicken Sie auf "*Fortfahren*".



![Image](assets/fr/10.webp)



Fahren Sie dann mit der Echtheitsprüfung fort, um sicherzustellen, dass Ihr Hardware Wallet nicht gefälscht oder kompromittiert ist.



![Image](assets/fr/11.webp)



Drücken Sie auf Ihrem Safe 3 die rechte Taste zur Bestätigung.



![Image](assets/fr/12.webp)



Wenn Ihr Trezor echt ist, wird eine Bestätigungsmeldung in der Trezor Suite angezeigt.



![Image](assets/fr/13.webp)



Sie können dann die Fenster mit den grundlegenden Bedienungsanweisungen überspringen.



![Image](assets/fr/14.webp)



## Erstellung eines Bitcoin-Portfolios



Klicken Sie in der Trezor Suite auf die Schaltfläche "*Neues Wallet erstellen*".



![Image](assets/fr/15.webp)



Für ein Standardportfolio können Sie sich für den Standard-Sicherungstyp entscheiden. Damit wird ein klassisches Single-Sig-Portfolio mit einer Mnemonic-Phrase mit 12 Wörtern erstellt. Klicken Sie auf "*Wallet* erstellen".



Wenn Sie mehr über die anderen in Trezor verfügbaren Backup-Optionen erfahren möchten, einschließlich *Multi-Share Backup*, empfehle ich Ihnen, auch dieses Tutorial zu lesen:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



Akzeptieren Sie die Nutzungsbedingungen von Hardware Wallet.



![Image](assets/fr/17.webp)



Drücken Sie erneut die rechte Taste, um ein neues Portfolio zu erstellen.



![Image](assets/fr/18.webp)



Klicken Sie in Trezor Suite auf "*Sicherung fortsetzen*".



![Image](assets/fr/19.webp)



Die Software enthält Anweisungen für die Verwaltung des Mnemonic-Satzes.



Mit diesem Mnemonic haben Sie vollen, uneingeschränkten Zugriff auf alle Ihre Bitcoins. Jeder, der im Besitz dieses Satzes ist, kann Ihr Geld stehlen, auch ohne physischen Zugang zu Ihrem Trezor Safe 3.



Die 12-Wort-Phrase stellt den Zugang zu Ihren Bitcoins wieder her, falls Ihr Hardware Wallet verloren geht, gestohlen wird oder kaputt geht. Es ist daher sehr wichtig, sie sorgfältig zu speichern und an einem sicheren Ort aufzubewahren.



Sie können die Gravur auf dem mitgelieferten Karton anbringen. Für zusätzliche Sicherheit empfehle ich, die Gravur auf einem Edelstahlsockel anzubringen, um sie vor Feuer, Überschwemmung oder Einsturz zu schützen.



Bestätigen Sie die Anweisungen und klicken Sie dann auf die Schaltfläche "*Wallet-Sicherung erstellen*".



![Image](assets/fr/20.webp)



Safe 3 erstellt Ihren Mnemonic-Satz mithilfe seines Zufallszahlengenerators. Vergewissern Sie sich, dass Sie während dieses Vorgangs nicht beobachtet werden. Schreiben Sie die auf dem Bildschirm angezeigten Wörter auf ein physisches Medium Ihrer Wahl. Je nach Ihrer Sicherheitsstrategie können Sie mehrere vollständige physische Kopien des Satzes anfertigen (aber vor allem dürfen Sie ihn nicht teilen). Achten Sie darauf, dass die Wörter nummeriert sind und in der richtigen Reihenfolge stehen.



***Natürlich dürfen Sie diese Wörter niemals im Internet weitergeben, wie ich es in diesem Tutorial tue. Dieses Beispiel Wallet wird nur auf dem Testnet verwendet und wird am Ende des Tutorials gelöscht werden



Für weitere Informationen über die richtige Art und Weise, Ihren Mnemonic-Satz zu speichern und zu verwalten, empfehle ich Ihnen dringend, diesen anderen Lehrgang zu besuchen, besonders wenn Sie ein Anfänger sind:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



Um zu den nächsten Wörtern zu gelangen, klicken Sie mit der rechten Maustaste. Sie können rückwärts gehen, indem Sie auf die linke Taste klicken. Wenn Sie alle Wörter aufgeschrieben haben, halten Sie die rechte Taste gedrückt, um zum nächsten Schritt zu gelangen.



![Image](assets/fr/22.webp)



Wählen Sie die Wörter in Ihrem Mnemonic-Satz entsprechend ihrer Reihenfolge aus, um zu bestätigen, dass Sie sie richtig aufgeschrieben haben. Verwenden Sie die linke und rechte Taste, um zwischen den Vorschlägen zu navigieren, und wählen Sie dann das richtige Wort aus, indem Sie gleichzeitig auf die beiden Tasten klicken.



![Image](assets/fr/23.webp)



Sobald diese Überprüfung abgeschlossen ist, klicken Sie auf die Schaltfläche auf der rechten Seite.



![Image](assets/fr/24.webp)



## Einstellen des PIN-Codes



Als Nächstes kommt der Schritt des PIN-Codes. Mit dem PIN-Code wird Ihr Trezor entsperrt. Er bietet also Schutz vor unbefugtem physischen Zugriff. Dieser PIN-Code ist nicht an der Ableitung der kryptografischen Schlüssel Ihres Wallet beteiligt. Selbst wenn Sie keinen Zugang zum PIN-Code haben, können Sie mit Ihrem 12-Wörter-Mnemonic-Satz wieder Zugang zu Ihren Bitcoins erhalten.



Klicken Sie in der Trezor Suite auf "*Weiter zur PIN*" und dann auf die Schaltfläche "*PIN festlegen*".



![Image](assets/fr/25.webp)



Bestätigen Sie mit Safe 3.



![Image](assets/fr/26.webp)



Wir empfehlen, einen möglichst zufälligen PIN-Code zu wählen. Speichern Sie diesen Code an einem anderen Ort als den, an dem Ihr Trezor gespeichert ist (z. B. in einem Passwortmanager). Sie können einen PIN-Code mit einer Länge zwischen 8 und 50 Ziffern festlegen. Ich empfehle Ihnen, den PIN-Code so lang wie möglich zu wählen, um die Sicherheit zu erhöhen.



Verwenden Sie die linke und rechte Taste, um die einzelnen Ziffern auszuwählen. Um Ihre Wahl zu bestätigen und zur nächsten Ziffer zu gelangen, drücken Sie beide Tasten gleichzeitig.



![Image](assets/fr/27.webp)



Wenn Sie fertig sind, klicken Sie auf das Häkchen "*ENTER*" am Anfang der Ziffern und bestätigen Sie Ihre PIN ein zweites Mal.



![Image](assets/fr/28.webp)



Ihr PIN-Code ist registriert worden.



![Image](assets/fr/29.webp)



Klicken Sie in Trezor Suite auf die Schaltfläche "*Einrichtung abschließen*".



![Image](assets/fr/30.webp)



Die Konfiguration Ihres Safe 3 ist nun abgeschlossen. Wenn Sie möchten, können Sie den Namen und die Startseite Ihres Hardware Wallet ändern.



![Image](assets/fr/31.webp)



Wir werden die Trezor Suite Software nicht mehr benötigen, außer um regelmäßige Firmware-Updates auf Ihrem Hardware Wallet durchzuführen, oder wenn Sie einen Wiederherstellungstest durchführen möchten. Wir werden nun Sparrow zur Verwaltung des Portfolios verwenden, da diese Software perfekt für die ausschließliche Verwendung des Bitcoin geeignet ist.



## Einrichten des Portfolios auf Sparrow Wallet



Beginnen Sie mit dem Herunterladen und Installieren von Sparrow Wallet [von der offiziellen Website] (https://sparrowwallet.com/) auf Ihrem Computer, falls Sie dies noch nicht getan haben.



Sobald Sie Sparrow Wallet geöffnet haben, stellen Sie sicher, dass die Software mit einem Bitcoin-Knoten verbunden ist, was durch das Häkchen in der unteren rechten Ecke des Interface angezeigt wird. Wenn Sie Probleme mit der Verbindung von Sparrow haben, empfehle ich Ihnen, den Anfang dieses Tutorials zu lesen:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klicken Sie auf die Registerkarte "*Datei*" und dann auf "*Neues Wallet*".



![Image](assets/fr/32.webp)



Geben Sie Ihrem Portfolio einen Namen und klicken Sie dann auf "*Wallet* erstellen".



![Image](assets/fr/33.webp)



Wählen Sie im Dropdown-Menü "*Skripttyp*" den Skripttyp aus, der zur Sicherung Ihrer Bitcoins verwendet werden soll. Ich empfehle "*Taproot*" oder, falls dies nicht möglich ist, "*Native SegWit*".



![Image](assets/fr/34.webp)



Klicken Sie auf die Schaltfläche "*Connected Hardware Wallet*". Ihr Safe 3 muss natürlich mit dem Computer verbunden und entsperrt sein.



![Image](assets/fr/35.webp)



Klicken Sie auf die Schaltfläche "*Scan*". Ihr Safe 3 sollte erscheinen. Klicken Sie auf "*Import Keystore*".



![Image](assets/fr/36.webp)



Sie können nun die Details Ihres Wallet sehen, einschließlich des erweiterten öffentlichen Schlüssels Ihres ersten Kontos. Klicken Sie auf die Schaltfläche "*Apply*", um die Erstellung des Wallet abzuschließen.



![Image](assets/fr/37.webp)



Wählen Sie ein sicheres Passwort, um den Zugang zum Sparrow Wallet zu schützen. Dieses Passwort gewährleistet einen sicheren Zugriff auf Ihre Sparrow Wallet-Daten und schützt Ihre öffentlichen Schlüssel, Adressen, Etiketten und Transaktionshistorie vor unbefugtem Zugriff.



Ich empfehle Ihnen, dieses Passwort in einem Passwort-Manager zu speichern, damit Sie es nicht vergessen.



![Image](assets/fr/38.webp)



Und jetzt ist Ihr Portfolio in Sparrow Wallet importiert worden!



![Image](assets/fr/39.webp)



Bevor Sie Ihre ersten Bitcoins in Ihrem Wallet erhalten, **empfehle ich Ihnen dringend, einen Test zur Wiederherstellung des leeren Geräts** durchzuführen. Schreiben Sie einige Referenzinformationen auf, z. B. Ihr xpub, und setzen Sie dann Ihren Trezor Safe 3 zurück, während der Wallet noch leer ist. Versuchen Sie dann, Ihr Wallet auf dem Trezor mit Hilfe Ihrer Papier-Backups wiederherzustellen. Überprüfen Sie, ob das nach der Wiederherstellung erzeugte xpub mit dem ursprünglich notierten übereinstimmt. Wenn dies der Fall ist, können Sie sicher sein, dass Ihre Sicherungskopien auf Papier zuverlässig sind.



Um mehr darüber zu erfahren, wie man einen Wiederherstellungstest durchführt, empfehle ich Ihnen, diesen anderen Lehrgang zu lesen:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Wie kann ich mit Trezor Safe 3 Bitcoins empfangen?



Klicken Sie auf Sparrow auf die Registerkarte "*Empfangen*".



![Image](assets/fr/40.webp)



Bevor Sie den von Sparrow Wallet vorgeschlagenen Address verwenden, überprüfen Sie ihn auf dem Bildschirm Ihres Trezor. Auf diese Weise können Sie sich vergewissern, dass der auf Sparrow angezeigte Address nicht gefälscht ist und dass der Hardware Wallet tatsächlich den privaten Schlüssel enthält, der benötigt wird, um die mit diesem Address gesicherten Bitcoins anschließend auszugeben. Dies hilft Ihnen, verschiedene Arten von Angriffen zu vermeiden.



Um diese Prüfung durchzuführen, klicken Sie auf die Schaltfläche "*Address anzeigen*".



![Image](assets/fr/41.webp)



Überprüfen Sie, ob der auf Ihrem Trezor angezeigte Address mit dem auf dem Sparrow Wallet übereinstimmt. Es ist auch ratsam, diese Überprüfung kurz vor der Übermittlung Ihres Address an den Absender durchzuführen, um sicher zu sein, dass er gültig ist. Sie können die Tasten zur Bestätigung verwenden.



![Image](assets/fr/42.webp)



Sie können dann ein "*Label*" hinzufügen, um die Quelle der Bitcoins zu beschreiben, die mit diesem Address gesichert werden sollen. Dies ist eine gute Praxis, die es Ihnen ermöglicht, Ihre UTXOs besser zu verwalten.



![Image](assets/fr/43.webp)



Sie können dann diesen Address verwenden, um Bitcoins zu erhalten.



![Image](assets/fr/44.webp)



## Wie kann ich mit Trezor Safe 3 Bitcoins versenden?



Jetzt, wo Sie Ihre ersten Satss auf Ihrem Safe-3-gesicherten Wallet erhalten haben, können Sie sie auch ausgeben! Schließen Sie Ihren Trezor an Ihren Computer an, entsperren Sie ihn mit dem PIN-Code, starten Sie den Sparrow Wallet und gehen Sie dann auf die Registerkarte "*Senden*", um eine neue Transaktion zu erstellen.



![Image](assets/fr/45.webp)



Wenn Sie *Münzkontrolle* wünschen, d.h. gezielt auswählen möchten, welche UTXOs in der Transaktion verbraucht werden sollen, gehen Sie auf die Registerkarte "*UTXOs*". Wählen Sie die UTXOs aus, die Sie ausgeben möchten, und klicken Sie dann auf "*Ausgewählte senden*". Sie werden zum gleichen Bildschirm auf der Registerkarte "*Senden*" zurückgeleitet, aber mit den bereits für die Transaktion ausgewählten UTXOs.



![Image](assets/fr/46.webp)



Geben Sie den Ziel-Address ein. Sie können auch mehrere Adressen eingeben, indem Sie auf die Schaltfläche "*+ Hinzufügen*" klicken.



![Image](assets/fr/47.webp)



Notieren Sie ein "*Etikett*", um sich den Zweck dieser Ausgabe zu merken.



![Image](assets/fr/48.webp)



Wählen Sie den Betrag, der an diesen Address gesendet werden soll.



![Image](assets/fr/49.webp)



Passen Sie den Gebührensatz für Ihre Transaktion an den aktuellen Markt an. Sie können zum Beispiel [Mempool.space](https://Mempool.space/) verwenden, um einen geeigneten Gebührensatz zu wählen.



Vergewissern Sie sich, dass alle Ihre Transaktionsparameter korrekt sind, und klicken Sie dann auf "*Transaktion erstellen*".



![Image](assets/fr/50.webp)



Wenn alles zu Ihrer Zufriedenheit ist, klicken Sie auf "*Transaktion zur Unterzeichnung abschließen*".



![Image](assets/fr/51.webp)



Klicken Sie auf "*Unterschreiben*".



![Image](assets/fr/52.webp)



Klicken Sie auf "*Unterschreiben*" neben Ihrem Trezor Safe 3.



![Image](assets/fr/53.webp)



Überprüfen Sie die Transaktionsparameter auf dem Bildschirm Ihres Hardware Wallet, einschließlich des empfangenden Address des Empfängers, des gesendeten Betrags und der Gebühr. Sobald die Transaktion auf dem Trezor überprüft wurde, klicken Sie auf beide Tasten gleichzeitig, um sie zu unterzeichnen.



![Image](assets/fr/54.webp)



Ihre Transaktion ist nun signiert. Prüfen Sie ein letztes Mal, ob alles in Ordnung ist, und klicken Sie dann auf "*Transaktion senden*", um sie im Bitcoin-Netzwerk zu übertragen.



![Image](assets/fr/55.webp)



Sie finden es auf der Registerkarte "*Transaktionen*" des Sparrow Wallet.



![Image](assets/fr/56.webp)



Herzlichen Glückwunsch, Sie sind nun mit der grundlegenden Verwendung des Trezor Safe 3 mit Sparrow Wallet vertraut! Um noch einen Schritt weiter zu gehen, empfehle ich Ihnen diese umfassende Anleitung zur Verwendung eines Hardware Wallet Trezor mit einem passphrase BIP39, um Ihre Sicherheit zu erhöhen:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Wenn Sie diese Anleitung nützlich fanden, wäre ich Ihnen dankbar, wenn Sie unten einen Green-Daumen hinterlassen würden. Sie können diesen Artikel auch gerne in Ihren sozialen Netzwerken teilen. Ich danke Ihnen sehr!