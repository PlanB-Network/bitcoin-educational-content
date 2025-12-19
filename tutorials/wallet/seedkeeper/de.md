---
name: Seedkeeper
description: Wie erstelle ich eine Sicherungskopie meines wallet Bitcoin mit der Seedkeeper-Chipkarte?
---

![cover](assets/cover.webp)



Der Seedkeeper ist eine Smartcard, die von Satochip entwickelt wurde, einem belgischen Unternehmen, das auf Hardwarelösungen für die Verwaltung und den Schutz digitaler Geheimnisse spezialisiert ist. Satochip, das für seine Smartcards für das Bitcoin-Ökosystem bekannt ist, hat den Seedkeeper als Alternative zu herkömmlichen Methoden zur Speicherung von mnemonischen Phrasen entwickelt.



Konkret handelt es sich bei dem Seedkeeper um eine multifunktionale, EAL6-zertifizierte Chipkarte mit einem sicheren Prozessor und einem manipulationssicheren Speicher (einem so genannten "Secure Element"). Wie der Name schon sagt, besteht seine Aufgabe darin, Bitcoin wallet Mnemonics und Passwörter verschlüsselt und geschützt zu speichern. Mit Seedkeeper können Sie Ihre Geheimnisse direkt in der sicheren Komponente der Karte generate importieren, organisieren und speichern.



Meiner Meinung nach hat Seedkeeper zwei Hauptverwendungszwecke, die wir in zwei separaten Tutorials untersuchen werden:




- Bitcoin** Gedächtnisspeicher: Anstatt Ihre 12 oder 24 Wörter auf Papier aufzuschreiben, können Sie sie auf die Smartcard importieren und mit einem PIN-Code schützen.
- Passwortverwaltung**: Sie können generate starke Passwörter über die Seedkeeper-Anwendung erstellen und direkt auf der Smartcard speichern, so dass Sie einen bequemen, einfach zu bedienenden Offline-Passwortmanager haben.



Technisch gesehen verfügt Seedkeeper über eine Kapazität von 8192 Byte, so dass mindestens 50 einzelne Geheimnisse gespeichert werden können (die genaue Anzahl hängt von ihrer Größe und den mit jedem Geheimnis verbundenen Metadaten ab). Der Zugriff auf Seedkeeper kann entweder [über ein Smartcard-Lesegerät, das](https://satochip.io/accessories/) an einen Computer angeschlossen ist, oder über die mobile Anwendung mit NFC-Verbindung erfolgen. Das gesamte System arbeitet im Offline-Modus, ohne Internetverbindung, was eine begrenzte Angriffsfläche garantiert.



![Image](assets/fr/001.webp)



Eine besonders interessante Funktion ist die Möglichkeit, den Inhalt eines Seedkeepers in einen anderen zu duplizieren, um ein Backup zu erstellen. In diesem Tutorial zeigen wir Ihnen, wie Sie genau das tun können.



Seedkeeper ist auch sehr interessant, wenn er mit wallet zustandsloser Hardware wie SeedSigner oder Specter DIY kombiniert wird. In diesem Fall ist es nicht notwendig, den Satochip-Client auf dem Computer oder Handy zu verwenden. Der Seedkeeper bewahrt den seed in seinem secure element auf und kann direkt mit dem Signiergerät verwendet werden, wodurch die Notwendigkeit eines QR-Codes auf Papier entfällt. Ich werde diesen speziellen Anwendungsfall in diesem Tutorial nicht weiter ausführen, da er Gegenstand eines anderen Tutorials ist:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Welcher Anwendungsfall für Seedkeeper?



In diesem Tutorial werde ich mich nur mit Anwendungsfällen im Zusammenhang mit Bitcoin befassen, da dies das Thema dieses Tutorials ist. Wir werden nicht auf die Passwortverwaltungsfunktionen eingehen, die Gegenstand eines anderen Tutorials sein werden.



Die Verwendung eines Seedkeepers hat im Vergleich zu einer einfachen Sicherung des Merksatzes auf Papier mehrere Vorteile:





- Diebstahlsicher:** Der seed in Ihrem wallet ist nicht im Klartext zugänglich. Um ihn zu extrahieren, müssen Sie die Seedkeeper-PIN kennen. Ein Dieb, der in den Besitz des Geräts gelangt, kann ohne diesen Code nichts damit anfangen.





- Verteilung des Risikos auf zwei Faktoren:** Sie können die Sicherheit zwischen einem digitalen und einem physischen Faktor aufteilen. Wenn Sie beispielsweise die Seedkeeper-PIN in Ihrem Passwort-Manager speichern, benötigen Sie sowohl Zugang zu diesem Manager als auch den physischen Besitz der Smartcard, um die seed zu erhalten (eine deutlich geringere Angriffswahrscheinlichkeit).





- Zentralisierte Verwaltung:** Seedkeeper erleichtert die Verwaltung mehrerer Samen aus verschiedenen Portfolios.





- Einfache Backups:** Duplizieren Sie einfach verschlüsselte Backups auf andere SeedKeeper.



Es gibt jedoch eine Reihe von Nachteilen im Vergleich zu einer einfachen Papierkopie Ihrer seed:





- Der Preis:** ist zwar bescheiden (etwa 25 €), aber immer noch höher als der eines Blattes Papier.





- Abhängigkeit von einem Allzweck-Computer:** Die Eingabe und Verwaltung von seed erfordert einen Computer oder ein Smartphone, was bedeutet, dass Ihre Mnemonik einen Rechner mit einer viel größeren Angriffsfläche als wallet-Hardware durchläuft. Dies kann ein Risiko darstellen, wenn das Gerät kompromittiert wird. Aus diesem Grund empfehle ich nicht, Seedkeeper zu verwenden, um das seed einer wallet-Hardware zu speichern (außer bei zustandsloser Verwendung ohne Computer, wie bei SeedSigner). Die Rolle der wallet-Hardware besteht genau darin, die seed in einer minimalistischen, hochsicheren Umgebung zu speichern. Wenn Sie Ihren seed manuell auf Ihrem normalen Computer eingeben, ist er nicht mehr auf die wallet-Hardware beschränkt: Er landet auch auf einem Allzweckrechner, der mehreren Angriffsvektoren ausgesetzt ist. Es ist also besser, Seedkeeper für einen heißen wallet zu verwenden als für einen kalten (außer SeedSigner / zustandslose wallet Hardware).





- Das mit der PIN verbundene Verlustrisiko:** Die direkte Unzugänglichkeit der seed bietet im Gegensatz zu einem Papier-Backup tatsächlich Schutz vor physischem Diebstahl. Aber wie immer ist Sicherheit eine Abwägung zwischen dem Diebstahl- und dem Verlustrisiko. Wenn Ihr Backup eine PIN erfordert, macht es der Verlust dieses Codes unmöglich, Ihre mnemonische Phrase wiederzuerlangen und somit auf Ihre Bitcoins zuzugreifen.



In Anbetracht dieser Vor- und Nachteile bin ich der Meinung, dass Seedkeeper (abgesehen von seiner Passwortverwaltungsfunktion) am besten geeignet ist, um einerseits Seeds aus Ihrem **Softwareportfolio** zu speichern, da sie sich bereits auf Ihrem Telefon oder Computer befinden, oder von Ihrer bildschirmlosen wallet-Hardware wie dem Satochip, und andererseits in Kombination mit zustandsloser wallet-Hardware wie dem SeedSigner, wo er seine Stärken voll ausspielt.



Ein weiterer besonders interessanter Anwendungsfall für Seedkeeper ist die Möglichkeit, die *Deskriptoren* Ihrer Portfolios sicher und zuverlässig zu sichern.



## 2. Wie bekomme ich einen Seedkeeper?



Es gibt zwei Möglichkeiten, Ihren Seedkeeper zu erhalten. Du kannst ihn [direkt im offiziellen Satochip-Shop](https://satochip.io/product/seedkeeper/) oder bei einem autorisierten Händler kaufen. Aber da [das Seedkeeper-Applet quelloffen ist](https://github.com/Toporin/Seedkeeper-Applet), können Sie es auch selbst auf [einer leeren Smartcard](https://satochip.io/product/blank-javacard-for-diy-project/) installieren.



Wenn Sie die Backup-Funktion von Seedkeeper nutzen möchten, müssen Sie natürlich zwei Smartcards kaufen.



## 3. Installieren des Seedkeeper-Clients



In diesem Tutorial werden wir unser seed-Portfolio auf unserem Seedkeeper sichern. Der erste Schritt besteht darin, die Software auf Ihrem Computer oder Smartphone zu installieren. Auf einem PC müssen Sie [die neueste Version von Satochip-Utils herunterladen](https://github.com/Toporin/Satochip-Utils/releases). Auf dem Handy ist die Seedkeeper-Anwendung im [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) sowie im [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060) erhältlich.



![Image](assets/fr/002.webp)



## 4. Initialisierung des Seedkeepers



Starten Sie die Anwendung und klicken Sie auf die Schaltfläche "*Klick & Scan*".



![Image](assets/fr/003.webp)



Sie werden nach einem PIN-Code für Ihren Seedkeeper gefragt. Da es sich um eine neue Karte handelt, wurde noch keine PIN festgelegt. Geben Sie einen beliebigen Code ein, um diesen Schritt zu überspringen, und klicken Sie dann auf "*Weiter*".



![Image](assets/fr/004.webp)



Legen Sie die Karte dann auf die Rückseite Ihres Smartphones. Die Anwendung erkennt, dass Seedkeeper noch nicht initialisiert wurde, und fordert Sie auf, den PIN-Code für Ihre Smartcard festzulegen, der zwischen 4 und 16 Zeichen lang sein kann. Um optimale Sicherheit zu gewährleisten, wählen Sie ein starkes Passwort, das so lang wie möglich ist, zufällig ist und aus einer Vielzahl von Zeichen besteht. Dieser PIN-Code ist die einzige Barriere gegen den physischen Zugriff auf Ihre Wiederherstellungsphrase.



**Denken Sie auch daran, diese PIN jetzt zu speichern**, zum Beispiel in einem Passwortmanager oder auf einem separaten physischen Medium. Im letzteren Fall sollten Sie den Datenträger mit der PIN niemals am gleichen Ort wie Ihren Seedkeeper aufbewahren, da diese Sicherheit sonst nutzlos wird. Es ist wichtig, ein zuverlässiges Backup zu haben: Ohne die PIN können Sie die auf Ihrem Seedkeeper gespeicherten Geheimnisse nicht wiederherstellen.



![Image](assets/fr/005.webp)



Bestätigen Sie Ihren PIN-Code ein zweites Mal.



![Image](assets/fr/006.webp)



Ihr Seedkeeper ist nun initialisiert. Sie können ihn entsperren, indem Sie den soeben eingestellten PIN-Code eingeben.



![Image](assets/fr/007.webp)



Sie werden nun auf die Seite zur Verwaltung Ihrer Smartcard weitergeleitet.



![Image](assets/fr/008.webp)



## 5. Eine seed bei Seedkeeper registrieren



Sobald Ihr Seedkeeper freigeschaltet ist, klicken Sie auf die Schaltfläche "*+*".



![Image](assets/fr/009.webp)



Wählen Sie "Geheimnis importieren*". Mit der Option "*Geheimnis generieren*" können Sie direkt in der Anwendung eine neue mnemonische Phrase erstellen.



![Image](assets/fr/010.webp)



In unserem Fall wollen wir den seed in unserem Portfolio speichern. Klicken Sie auf "*Mnemonic*".



![Image](assets/fr/011.webp)



Weisen Sie diesem Geheimnis einen "*Label*" zu, damit es leicht identifiziert werden kann, wenn Sie mehrere Informationen in Ihrem Seedkeeper speichern.



![Image](assets/fr/012.webp)



Geben Sie dann Ihre Wiederherstellungsphrase in das vorgesehene Feld ein. Wenn Sie möchten, können Sie auch ein passphrase BIP39 oder Ihre *Deskriptoren* hinzufügen. Klicken Sie dann auf "Importieren*".



![Image](assets/fr/013.webp)



*Die in diesem Bild dargestellte Mnemonik ist fiktiv und gehört niemandem. Sie ist nur ein Beispiel. Geben Sie niemals Ihre eigene Eselsbrücke preis, sonst werden Ihre Bitcoins gestohlen



Legen Sie Ihren Seedkeeper auf die Rückseite Ihres Smartphones.



![Image](assets/fr/014.webp)



Ihr seed wurde registriert.



![Image](assets/fr/015.webp)



## 6. Zugang zu Ihrem seed auf Seedkeeper



Wenn Sie Ihren Merksatz überprüfen möchten, nehmen Sie Ihren Seedkeeper und klicken Sie auf die Schaltfläche "*Klick & Scan*".



![Image](assets/fr/016.webp)



Geben Sie Ihren PIN-Code ein und drücken Sie dann "*Weiter*".



![Image](assets/fr/017.webp)



Legen Sie Ihren Seedkeeper auf die Rückseite Ihres Smartphones.



![Image](assets/fr/018.webp)



Dies führt Sie zu einer Liste aller Ihrer registrierten Geheimnisse. In diesem Beispiel möchte ich die seed meines Portfolios "*Blockstream App*" anzeigen, also klicke ich darauf.



![Image](assets/fr/019.webp)



Drücken Sie die Taste "*Aufdecken*".



![Image](assets/fr/020.webp)



Scannen Sie Ihren Seedkeeper erneut.



![Image](assets/fr/021.webp)



Ihre zuvor aufgezeichnete mnemonische Phrase wird nun auf dem Bildschirm angezeigt.



![Image](assets/fr/022.webp)



## 7. Sichern von Seedkeeper



Wir werden nun ein Backup meines Seedkeepers auf einem zweiten Seedkeeper erstellen, um zwei Kopien zu haben. Diese Redundanz kann Teil einer Strategie sein, um Ihre Bitcoins zu sichern: zum Beispiel, indem Sie Ihre Phrase an zwei verschiedenen Orten aufbewahren, um physische Risiken zu begrenzen, oder indem Sie eine Kopie einem vertrauenswürdigen Verwandten als Teil eines Erbschaftsplans anvertrauen.



Nehmen Sie dazu Ihren zweiten Seedkeeper mit (denken Sie daran, einen der beiden mit einer Markierung zu versehen, um Verwechslungen zu vermeiden). Beginnen Sie damit, ihn zu initialisieren, wie in Schritt 4 dieses Tutorials beschrieben. Wählen Sie erneut ein sicheres Passwort. Je nach Ihrer Strategie können Sie sich für ein anderes Passwort entscheiden oder dasselbe beibehalten.



![Image](assets/fr/023.webp)



Öffnen Sie die Anwendung, klicken Sie auf "*Klick & Scan*", geben Sie das Passwort Ihres Seedkeepers Nr. 1 (Quelle) ein und scannen Sie ihn.



![Image](assets/fr/024.webp)



Dadurch gelangen Sie zur Startseite mit einer Liste Ihrer Geheimnisse. Klicken Sie auf die drei kleinen Punkte oben rechts auf der Oberfläche.



![Image](assets/fr/025.webp)



Wählen Sie "*Sicherung erstellen*" und drücken Sie dann "*Start*".



![Image](assets/fr/026.webp)



Geben Sie den PIN-Code Ihrer Backup-Karte (Seedkeeper Nr. 2) ein.



![Image](assets/fr/027.webp)



Scannen Sie dann die Karte.



![Image](assets/fr/028.webp)



Machen Sie dasselbe mit der Hauptkarte (Seedkeeper Nr. 1) und klicken Sie dann auf "*Sicherung erstellen*".



![Image](assets/fr/029.webp)



Ihr Seedkeeper Nr. 2 enthält nun alle Geheimnisse, die auf Seedkeeper Nr. 1 gespeichert sind.



![Image](assets/fr/030.webp)



Sie können Ihren Seedkeeper n°2 scannen, um zu überprüfen, ob die Geheimnisse kopiert wurden.



![Image](assets/fr/031.webp)



Das war's schon! Jetzt wissen Sie, wie Sie Seedkeeper verwenden können, um die mnemonische Phrase eines Bitcoin wallet zu speichern. In einem der nächsten Tutorials werden wir uns ansehen, wie Sie Seedkeeper zum Speichern Ihrer Passwörter verwenden können. Ich lade Sie auch dazu ein, seine kombinierte Verwendung mit SeedSigner zu entdecken:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

In diesem Lernprogramm haben wir mehrmals die ***Deskriptoren*** in Ihrem Bitcoin-Portfolio erwähnt. Sie wissen nicht, was sie sind? Dann empfehle ich Ihnen unsere kostenlose CYP 201-Schulung, in der alle Mechanismen, die mit dem Betrieb von HD-Portfolios zusammenhängen, im Detail behandelt werden!



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f