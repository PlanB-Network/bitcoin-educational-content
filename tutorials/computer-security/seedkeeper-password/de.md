---
name: Seedkeeper - Passwortmanager
description: Wie können Sie Ihre Passwörter mit der Seedkeeper Smartcard speichern?
---

![cover](assets/cover.webp)



Der Seedkeeper ist eine Smartcard, die von Satochip entwickelt wurde, einem belgischen Unternehmen, das auf Hardwarelösungen für die Verwaltung und den Schutz digitaler Geheimnisse spezialisiert ist. Satochip, das für seine Smartcards für das Bitcoin-Ökosystem bekannt ist, hat den Seedkeeper als Alternative zu herkömmlichen Methoden zur Speicherung von mnemonischen Phrasen und anderen digitalen Geheimnissen konzipiert.



Konkret handelt es sich bei dem Seedkeeper um eine multifunktionale, EAL6-zertifizierte Chipkarte mit einem sicheren Prozessor und einem manipulationssicheren Speicher (einem so genannten "Secure Element"). Wie der Name schon sagt, besteht seine Aufgabe darin, Bitcoin-Portfoliomnemonics und Passwörter verschlüsselt und geschützt zu speichern. Mit Seedkeeper können Sie generate, importieren, organisieren und Ihre Geheimnisse direkt in der sicheren Komponente der Karte speichern.



Meiner Meinung nach hat Seedkeeper zwei Hauptverwendungszwecke, die wir in zwei separaten Tutorials untersuchen werden:




- Bitcoin** Gedächtnisspeicher: Anstatt Ihre 12 oder 24 Wörter auf Papier aufzuschreiben, können Sie sie auf die Smartcard importieren und mit einem PIN-Code schützen.
- Passwortverwaltung**: Sie können generate starke Passwörter über die Seedkeeper-Anwendung erstellen und direkt auf der Smartcard speichern, so dass Sie einen bequemen, einfach zu bedienenden Offline-Passwortmanager haben.



Technisch gesehen verfügt Seedkeeper über eine Kapazität von 8192 Byte, so dass mindestens 50 einzelne Geheimnisse gespeichert werden können (die genaue Anzahl hängt von ihrer Größe und den mit jedem Geheimnis verbundenen Metadaten ab). Der Zugriff auf Seedkeeper kann entweder [über ein Smartcard-Lesegerät, das](https://satochip.io/accessories/) an einen Computer angeschlossen ist, oder über die mobile Anwendung mit NFC-Verbindung erfolgen. Das gesamte System arbeitet im Offline-Modus, ohne Internetverbindung, was eine begrenzte Angriffsfläche garantiert.



![Image](assets/fr/001.webp)



Eine besonders interessante Funktion ist die Möglichkeit, den Inhalt eines Seedkeepers in einen anderen zu duplizieren, um ein Backup zu erstellen. In diesem Tutorial zeigen wir Ihnen, wie Sie genau das tun können.



In dieser Anleitung wird nur die Verwendung von SeedKeeper für herkömmliche Passwörter im Sinne eines Passwortmanagers behandelt. Wenn Sie SeedKeeper zum Speichern von Bitcoin wallet-Gedächtnisstützen verwenden möchten, lesen Sie bitte dieses andere Tutorial:



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. Wie bekomme ich einen Seedkeeper?



Es gibt zwei Möglichkeiten, Ihren Seedkeeper zu erhalten. Du kannst ihn [direkt im offiziellen Satochip-Shop](https://satochip.io/product/seedkeeper/) oder bei einem autorisierten Händler kaufen. Aber da [das Seedkeeper-Applet quelloffen ist](https://github.com/Toporin/Seedkeeper-Applet), können Sie es auch selbst auf [einer leeren Smartcard](https://satochip.io/product/blank-javacard-for-diy-project/) installieren.



Wenn Sie die Backup-Funktion von Seedkeeper nutzen möchten, müssen Sie natürlich zwei Smartcards kaufen.



## 2. Installieren des Seedkeeper-Clients



Der erste Schritt besteht darin, die Software auf Ihrem Computer oder Smartphone zu installieren. Auf einem PC müssen Sie [die neueste Version von Satochip-Utils herunterladen](https://github.com/Toporin/Satochip-Utils/releases). Für Mobiltelefone ist die Seedkeeper-Anwendung im [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) und im [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060) erhältlich.



![Image](assets/fr/002.webp)



## 3. Initialisierung des Seedkeepers



Starten Sie die Anwendung und klicken Sie auf die Schaltfläche "*Klick & Scan*".



![Image](assets/fr/003.webp)



Sie werden nach einem PIN-Code für Ihren Seedkeeper gefragt. Da es sich um eine neue Karte handelt, wurde noch keine PIN festgelegt. Geben Sie einen beliebigen Code ein, um diesen Schritt zu überspringen, und klicken Sie dann auf "*Weiter*".



![Image](assets/fr/004.webp)



Legen Sie die Karte dann auf die Rückseite Ihres Smartphones. Die Anwendung erkennt, dass Seedkeeper noch nicht initialisiert wurde, und fordert Sie auf, den PIN-Code für Ihre Smartcard festzulegen, der zwischen 4 und 16 Zeichen lang ist. Um optimale Sicherheit zu gewährleisten, wählen Sie einen robusten PIN-Code, der so lang wie möglich ist, zufällig ist und aus einer Vielzahl von Zeichen besteht. Dieser PIN-Code ist die einzige Barriere gegen den physischen Zugriff auf Ihre Passwörter.



**Denken Sie auch daran, diese PIN jetzt zu speichern**, zum Beispiel in einem Passwortmanager oder auf einem separaten physischen Medium. Im letzteren Fall sollten Sie den Datenträger mit der PIN niemals am gleichen Ort wie Ihren Seedkeeper aufbewahren, da diese Sicherheit sonst nutzlos wird. Es ist wichtig, ein zuverlässiges Backup zu haben: Ohne die PIN können Sie die auf Ihrem Seedkeeper gespeicherten Geheimnisse nicht wiederherstellen.



![Image](assets/fr/005.webp)



Bestätigen Sie Ihren PIN-Code ein zweites Mal.



![Image](assets/fr/006.webp)



Ihr Seedkeeper ist nun initialisiert. Sie können ihn entsperren, indem Sie den soeben eingestellten PIN-Code eingeben.



![Image](assets/fr/007.webp)



Sie werden nun auf die Seite zur Verwaltung Ihrer Smartcard weitergeleitet.



![Image](assets/fr/008.webp)



## 4. Passwörter auf Seedkeeper speichern



Sobald Ihr Seedkeeper freigeschaltet ist, klicken Sie auf die Schaltfläche "*+*".



![Image](assets/fr/009.webp)



Wählen Sie "Geheimnis generieren*". Mit der Option "*Geheimnis importieren*" können Sie ein bestehendes Geheimnis speichern (z. B. ein Passwort, das Sie in der Vergangenheit erstellt haben).



![Image](assets/fr/010.webp)



In unserem Fall wollen wir ein Passwort speichern. Klicken Sie auf "*Passwort*".



![Image](assets/fr/011.webp)



Weisen Sie diesem Geheimnis einen "*Label*" zu, damit es leicht identifiziert werden kann, wenn Sie mehrere Informationen in Ihrem Seedkeeper speichern. Sie können auch einen Identifikator hinzufügen, der mit dem Passwort und der URL der Website verbunden ist.



![Image](assets/fr/012.webp)



Wählen Sie die Länge und die Parameter Ihres Passworts und klicken Sie auf "*Erzeugen*" und dann auf "*Importieren*".



![Image](assets/fr/013.webp)



Legen Sie Ihren Seedkeeper auf die Rückseite Ihres Smartphones.



![Image](assets/fr/014.webp)



Ihr Passwort wurde registriert.



![Image](assets/fr/015.webp)



## 5. Zugang zu Ihrem Seedkeeper-Passwort



Wenn Sie Ihr Passwort überprüfen möchten, nehmen Sie Ihren Seedkeeper und klicken Sie auf die Schaltfläche "*Klick & Scan*".



![Image](assets/fr/016.webp)



Geben Sie Ihren PIN-Code ein und drücken Sie dann "*Weiter*".



![Image](assets/fr/017.webp)



Legen Sie Ihren Seedkeeper auf die Rückseite Ihres Smartphones.



![Image](assets/fr/018.webp)



Dies führt Sie zu einer Liste aller Ihrer registrierten Geheimnisse. In diesem Beispiel möchte ich das Kennwort für mein Plan ₿ Academy-Konto anzeigen, also klicke ich es an.



![Image](assets/fr/019.webp)



Drücken Sie die Taste "*Aufdecken*".



![Image](assets/fr/020.webp)



Scannen Sie Ihren Seedkeeper erneut.



![Image](assets/fr/021.webp)



Ihr zuvor gespeichertes Passwort erscheint nun auf dem Bildschirm. Sie können es kopieren und auf der betreffenden Website verwenden.



![Image](assets/fr/022.webp)



## 6. Sichern von Seedkeeper



Wir werden nun ein Backup meines Seedkeepers auf einem zweiten Seedkeeper erstellen, so dass wir zwei Kopien haben. Diese Redundanz kann Teil einer Strategie zur Sicherung Ihrer wichtigsten Passwörter sein: Sie können beispielsweise Ihre Seedkeeper an zwei verschiedenen Orten aufbewahren, um die physischen Risiken zu begrenzen, oder einer vertrauenswürdigen Person eine Kopie anvertrauen.



Nehmen Sie dazu Ihren zweiten Seedkeeper mit (denken Sie daran, einen der beiden mit einer Markierung zu versehen, um Verwechslungen zu vermeiden). Beginnen Sie damit, ihn zu initialisieren, wie in Schritt 3 dieses Tutorials beschrieben. Wählen Sie auch hier einen starken PIN-Code. Je nach Ihrer Strategie können Sie sich für eine andere PIN entscheiden oder dieselbe beibehalten.



![Image](assets/fr/023.webp)



Öffnen Sie die Anwendung, klicken Sie auf "*Klick & Scan*", geben Sie die PIN Ihres Seedkeepers Nr. 1 (Quelle) ein und scannen Sie ihn.



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



Das ist alles, was Sie wissen müssen! Jetzt wissen Sie, wie Sie Seedkeeper zum Speichern Ihrer Passwörter verwenden können. In einem zukünftigen Tutorial werden wir uns ansehen, wie man Seedkeeper zum Sichern eines Bitcoin wallet verwendet. Ich lade Sie auch dazu ein, die kombinierte Verwendung mit SeedSigner zu entdecken:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356