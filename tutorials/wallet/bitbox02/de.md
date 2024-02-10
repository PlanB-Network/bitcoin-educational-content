---
name: BitBox02

description: Einrichtung und Verwendung einer BitBox02
---

![cover](assets/cover.jpeg)

Die BitBox02 (https://bitbox.swiss/) ist eine in der Schweiz hergestellte physische Geldbörse, die speziell für die Sicherung Ihrer Bitcoins entwickelt wurde. Zu ihren wichtigsten Merkmalen gehören einfache Sicherung und Wiederherstellung mit einer microSD-Karte, ein minimalistisches und diskretes Design sowie umfassende Unterstützung für Bitcoin.

![device](assets/1.png)

Sie bietet modernste Sicherheitstechnologie, die von Experten entwickelt wurde und einen sicheren Chip umfasst. Ihr Quellcode wurde von Sicherheitsforschern vollständig überprüft und ist vollständig Open Source. Die BitBox02 wird mit einer einfachen, aber leistungsstarken BitBoxApp geliefert, die eine sichere Verwaltung Ihrer Bitcoins ermöglicht. Sie unterstützt den Vollknoten für Bitcoin und gewährleistet eine Ende-zu-Ende-verschlüsselte Kommunikation zwischen der App und dem Gerät. Hergestellt in der Schweiz, hat die BitBox02 einen positiven Ruf bei ihren Benutzern erlangt.

![video](https://youtu.be/sB4b2PbYaj0)

> Spezifikationen
>
> - Konnektivität: USB-C
> - Kompatibilität: Windows 7 und höher, macOS 10.13 und höher, Linux, Android
> - Eingabe: Kapazitive Touch-Sensoren
> - Mikrocontroller: ATSAMD51J20A; 120 Mhz 32-Bit Cortex-M4F; Echter Zufallszahlengenerator
> - Sicherer Chip: ATECC608B; Echter Zufallszahlengenerator (NIST SP 800-90A/B/C)
> - Display: 128 x 64 px weißes OLED
> - Material: Polycarbonat
> - Größe: 54,5 x 25,4 x 9,6 mm inklusive USB-C-Stecker
> - Gewicht: Gerät 12 g; mit Verpackung und Zubehör 160 g

Laden Sie Datenblätter auf ihrer Website herunter https://bitbox.swiss/bitbox02/

## Verwendung der BitBox02-Hardware-Geldbörse

### Einrichten der BitBox02

Die BitBox02 verfügt über einen USB-C-Anschluss, der mit der Hülle verbunden ist. Wenn Ihr Computer den regulären USB-Anschluss verwendet, müssen Sie den mit dem Gerät gelieferten Adapter verwenden.

Schließen Sie es an Ihren Computer an und das Gerät wird eingeschaltet (noch nicht tun).

Es hat Sensoren oben und unten und fordert Sie auf, oben oder unten zu berühren, um den Bildschirm entsprechend auszurichten.

![image](assets/2.png)

### Laden Sie die BitBox02-App herunter

Besuchen Sie https://shiftcrypto.ch/ und klicken Sie oben auf den Link "App", um zur Download-Seite zu gelangen:

![image](assets/3.png)

Klicken Sie auf die blaue Schaltfläche "Herunterladen":

![image](assets/4.png)

Um den Download zu überprüfen (es erhöht die Komplexität, ist aber empfehlenswert, insbesondere wenn Sie viele Bitcoins speichern), siehe Anhang A.

Nach dem Download können Sie die Datei entpacken. Auf einem Mac doppelklicken Sie einfach auf die heruntergeladene Datei und ein BitBox App-Symbol wird in Ihrem Download-Verzeichnis angezeigt. Sie können es für einfachen Zugriff auf Ihren Desktop (oder an einen anderen Ort) ziehen.

Doppelklicken Sie auf die App, um sie auszuführen (sie wird nicht "installiert").

Auf dem Mac erhalten Sie eine Warnung von Ihrem Computer. Ignorieren Sie sie einfach und klicken Sie auf "Öffnen":

![image](assets/5.png)

Sie sehen dann Folgendes:

![image](assets/6.png)

Schließen Sie das Gerät nun an den Computer an.
Es wird Ihnen einen Pairing-Code anzeigen. Überprüfen Sie, ob sie übereinstimmen, und berühren Sie dann den Sensor, um das Häkchen auszuwählen. Dann zurück zum Bildschirm, wird der Weiter-Button für Sie verfügbar sein.

![image](assets/7.png)

Sie haben dann die Möglichkeit, einen neuen Seed zu erstellen oder einen Seed wiederherzustellen. Ich werde das Erstellen eines neuen Seeds demonstrieren (Es ist wichtig, auch den erstellten Seed zur Überprüfung der Qualität Ihres Backups wiederherzustellen, bevor Sie Bitcoin in die Brieftasche laden).

![image](assets/8.png)

Das Gerät wurde mit einer microSD-Karte geliefert. Legen Sie sie ein, wenn Sie sie noch nicht haben.

![image](assets/9.png)

Benennen Sie Ihr Gerät und klicken Sie auf "Weiter", dann bestätigen Sie auf dem Gerät.

![image](assets/10.png)

Sie werden dann aufgefordert, ein Passwort für das Gerät festzulegen. Dies ist kein Teil Ihres Seeds. Es ist auch keine Passphrase (das ist Teil Ihres Seeds). Es handelt sich einfach um ein Passwort, um das Gerät zu sperren. Wenn Sie das Gerät einschalten, werden Sie jedes Mal nach diesem Passwort gefragt. Sie haben 10 aufeinanderfolgende Fehlversuche, bevor das Gerät sich selbst von allen Speicherinhalten löscht, also seien Sie vorsichtig. Die Animation auf dem Bildschirm wird Ihnen zeigen, wie Sie die Bedienelemente des Geräts verwenden, um das Passwort festzulegen.

![image](assets/11.png)

Lesen Sie den nächsten Bildschirm und überprüfen Sie jedes Kästchen, dann fahren Sie fort.

![image](assets/12.png)
![image](assets/13.png)
![image](assets/14.png)

Und so sieht die Brieftasche aus, wenn sie bereit ist.

![image](assets/15.png)

### NICHT SO SCHNELL!!

Es ist ziemlich seltsam, aber der BitBox02 sagt uns, dass wir das Gerät verwenden können, hat uns aber nicht aufgefordert, die Seed-Wörter aufzuschreiben! Das EINZIGE Backup, das wir haben, ist die Datei, die auf der microSD-Karte gespeichert ist. Das ist unzureichend. Diese Speichergeräte halten nicht ewig (aufgrund von "Bit-Rot"). Wir brauchen ein Papier-Backup und Duplikate, die in Safes aufbewahrt werden (wie im allgemeinen Leitfaden zur Verwendung von Hardware-Wallets erklärt).

Um unseren Seed-Phrasen zu erhalten und sie aufzuschreiben, gehen Sie zum Tab "Gerät verwalten" auf der linken Seite und klicken Sie dann auf "Wiederherstellungswörter anzeigen".

![image](assets/16.png)

Sie können dann die Bestätigung durchgehen, und das Gerät wird Ihnen die Wörter präsentieren. Schreiben Sie sie ordentlich auf und lassen Sie niemanden die Wörter sehen.

![image](assets/17.png)

Danach können Sie auf den Bitcoin-Tab auf der linken Seite klicken, um Ihre Empfangsadressen zu erhalten.

![image](assets/18.png)

Es zeigt jeweils eine Adresse an, aber zumindest können Sie aus den ersten 20 Adressen auswählen:

![image](assets/19.png)

Durch Klicken auf die blaue Schaltfläche wird die vollständige Adresse angezeigt, und Sie werden aufgefordert, zu überprüfen, ob die Adresse mit der Anzeige auf dem Bildschirm übereinstimmt. Dies ist eine gute Praxis, um zu bestätigen, dass keine Malware auf Ihrem Computer Sie dazu verleitet, Bitcoin an die Adresse eines Angreifers zu senden.

![image](assets/20.png)

Um Bitcoin an diese Brieftasche zu senden, können Sie die Adresse kopieren und in die Auszahlungsseite der Börse einfügen, auf der sich Ihre Münzen befinden. Ich empfehle Ihnen, zuerst einen kleinen Testbetrag zu senden und ihn entweder zurück an die Börse oder an die zweite Adresse in Ihrer Brieftasche auszugeben.

Für größere Beträge empfehle ich Ihnen, eine Passphrase zu erstellen (siehe unten). Die ursprüngliche Brieftasche (ohne Passphrase) kann als Ihre Täuschungsbrieftasche verwendet werden (sie muss einen angemessenen Betrag enthalten, um glaubwürdig zu sein).

### Mit einem Knoten verbinden

Der BitBox02 wird automatisch mit einem Knotenpunkt verbunden. Schauen wir mal, mit welchem er verbunden ist. Klicken Sie auf den Einstellungen-Tab auf der linken Seite und dann auf "Verbinden Sie Ihren eigenen Full Node".

![image](assets/21.png)

Hier können wir sehen, dass er mit dem Knotenpunkt von shiftcrypto verbunden ist. Nicht gut. Wir haben ihnen alle unsere Bitcoin-Adressen verraten und unsere IP-Adresse (natürlich nicht den Seed; sie können unsere Adressen/Salden sehen, aber nicht ausgeben). Wir können unsere eigenen Knotenpunkt-Details auf dieser Seite eingeben (außerhalb des Umfangs dieses speziellen Leitfadens) oder bessere Software wie Sparrow Bitcoin Wallet, Electrum Desktop Wallet oder Specter Desktop verwenden. Ich werde später im Leitfaden das Sparrow Bitcoin Wallet demonstrieren.

![image](assets/22.png)

Fügen Sie eine Passphrase hinzu

Jetzt, da wir das Gerät mit der BitBox02-App eingerichtet haben (und unsere Adressen offengelegt haben, was bei dieser speziellen Hardware-Wallet unvermeidlich ist), können wir unserer Seed-Phrase eine Passphrase hinzufügen. Dadurch können wir eine neue Brieftasche mit demselben Seed erstellen, und ShiftCrypto wird unsere neuen Adressen niemals sehen. Wir werden diese Brieftasche nur mit unserer eigenen Software verbinden.

### Passphrase aktivieren

Gehen Sie jetzt voran und "aktivieren" Sie die Passphrase-Funktion (aber wir setzen noch keine Passphrase). Gehen Sie zum Tab "Gerät verwalten" und klicken Sie auf "Passphrase aktivieren" (roter Kreis unten).

![image](assets/23.png)

Lesen Sie die Schritte durch...

![image](assets/24.png)
![image](assets/25.png)
![image](assets/26.png)

Trennen Sie nun das Gerät und schließen Sie die BitBox02-App.

ENDE des BitBox02-Abschnitts von Parman.

Ihr Gerät ist jetzt vollständig einsatzbereit und kann mit jeder Desktop-Lösung wie Specter, Sparrow und der BitBox-Oberfläche verwendet werden.
