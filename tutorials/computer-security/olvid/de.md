---
name: Olvid
description: Private Nachrichten für alle
---
![cover](assets/cover.webp)



Olvid ist eine französische Instant-Messaging-Anwendung, die 2019 auf den Markt gebracht wurde und ein hohes Maß an Sicherheit bieten soll, ohne dabei Kompromisse bei der Privatsphäre einzugehen. Im Gegensatz zu WhatsApp oder Signal fragt Olvid bei der Registrierung keine persönlichen Daten ab: keine Telefonnummer, keine E-Mail, nichts. Die Identifizierung zwischen den Nutzern basiert auf einem Exchange von Schlüsseln, ohne Verzeichnisserver oder gemeinsames Address-Buch.



Alle Nachrichten werden Ende-zu-Ende mit einem originellen kryptografischen Protokoll verschlüsselt, das auch die Metadaten schützt: Niemand weiß, mit wem Sie sprechen und wann. Der Client-Code ist Open Source, aber der zentrale Server, der verschlüsselte Nachrichten weiterleitet, bleibt proprietär und wird auf AWS gehostet.

Das Sicherheitsmodell von Olvid basiert auf einem zentralen Prinzip: dem vollständigen Verzicht auf eine vertrauenswürdige dritte Partei bei der Einrichtung digitaler Identitäten. Im Gegensatz zu den meisten verschlüsselten Messengern, die ein zentrales Verzeichnis zur Verwaltung der Benutzeridentitäten verwenden, verlässt sich Olvid auf keine zentrale Infrastruktur, um die Integrität der Kommunikation zu gewährleisten. Diese Architektur beseitigt somit die Risiken im Zusammenhang mit einer Kompromittierung des Verzeichnisses.

Olvid verwendet dennoch einen zentralen Nachrichtenverteilungsserver, der jedoch ausschließlich eine logistische Funktion erfüllt: die asynchrone Übertragung verschlüsselter Nachrichten. Dieser Server ist an keinem Schritt der Verschlüsselung beteiligt, kennt weder die wahre Identität der Benutzer noch den Inhalt oder die Metadaten der Nachrichten (mit Ausnahme des öffentlichen Schlüssels des Empfängers, der für das Routing erforderlich ist). Er kann daher standardmäßig als feindlich angesehen werden, ohne die Gesamtsicherheit zu gefährden. Selbst wenn er kompromittiert würde, könnte er keinen Zugriff auf die Inhalte der Kommunikation ermöglichen. Olvid setzt also auf eine zentrale Nachrichtenverteilung (aus Gründen der Effizienz und Dienstqualität), garantiert aber gleichzeitig eine von dieser Infrastruktur unabhängige Sicherheit.


Olvid bietet eine kostenlose Version und eine Abo-Version für 4,99 € pro Monat. Die kostenlose Version bietet den vollen Funktionsumfang, mit Ausnahme von Audio- und Videoanrufen (obwohl es möglich ist, diese zu empfangen), und ermöglicht keine Synchronisierung von Konten über mehrere Geräte hinweg. Wenn Sie also vorhaben, Ihr Smartphone ausschließlich zu verwenden und keine Anrufe tätigen müssen, ist Olvid eine ausgezeichnete Lösung.



Olvid ist von ANSSI (der französischen Behörde für Cybersicherheit) zertifiziert. Diese Anwendung ist eine hervorragende Alternative zu den herkömmlichen Messaging-Diensten (WhatsApp, Facebook Messenger, WeChat...) für alle, die ihre Privatsphäre schützen wollen und gleichzeitig Wert auf eine einfache Nutzung legen.


| Anwendung            | E2EE 1:1      | E2EE Gruppen  | Anonyme Registrierung | Client-Lizenz open-source | Server-Lizenz open-source | Dezentraler Server   | Entstehungsjahr |
| -------------------- | ------------- | ------------- | --------------------- | ------------------------- | ------------------------- | -------------------- | --------------- |
| WhatsApp             | ✅             | ✅             | ❌                     | ❌                         | ❌                         | ❌                    | 2009            |
| WeChat               | ❌             | ❌             | ❌                     | ❌                         | ❌                         | ❌                    | 2011            |
| Facebook Messenger   | ✅             | 🟡 (optional) | ❌                     | ❌                         | ❌                         | ❌                    | 2011            |
| Telegram             | 🟡 (optional) | ❌             | 🟡                    | ✅                         | ❌                         | ❌                    | 2013            |
| LINE                 | ✅             | ✅             | ❌                     | ❌                         | ❌                         | ❌                    | 2011            |
| Signal               | ✅             | ✅             | ❌                     | ✅                         | ✅                         | ❌                    | 2014            |
| Threema              | ✅             | ✅             | ✅                     | ✅                         | ❌                         | ❌                    | 2012            |
| Element (Matrix)     | ✅             | ✅             | ✅                     | ✅                         | ✅                         | 🟡 (föderiert)       | 2016            |
| Delta Chat           | ✅             | ✅             | ✅                     | ✅                         | N/A                       | 🟡 (über E-Mail)     | 2017            |
| Conversations (XMPP) | ✅             | ✅             | ✅                     | ✅                         | ✅                         | 🟡 (föderiert)       | 2014            |
| Session              | ✅             | ✅             | ✅                     | ✅                         | ✅                         | ✅                    | 2020            |
| SimpleX              | ✅             | ✅             | ✅                     | ✅                         | ✅                         | ✅                    | 2021            |
| **Olvid**            | **✅**         | **✅**         | **✅**                 | **✅**                     | **❌**                     | 🟡(kein Verzeichnis) | **2019**        |
| Keet                 | ✅             | ✅             | ✅                     | ❌                         | N/A                       | ✅                    | 2022            |
| Jami                 | ✅             | ✅             | ✅                     | ✅                         | N/A                       | ✅                    | 2005            |
| Briar                | ✅             | ✅             | ✅                     | ✅                         | N/A                       | ✅                    | 2018            |
| Tox                  | ✅             | ✅             | ✅                     | ✅                         | N/A                       | ✅                    | 2013            |

*E2EE = Ende-zu-Ende-Verschlüsselung*



## Installieren Sie die Olvid-Anwendung



Olvid ist auf allen Plattformen verfügbar. Sie können die Anwendung direkt aus dem App Store Ihres Telefons herunterladen:




- [Google Play](https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store] (https://apps.apple.com/app/olvid/id1414865219);



Unter Android ist auch eine [Installation über APK] möglich (https://www.olvid.io/download/).



In diesem Tutorial konzentrieren wir uns auf die mobile Version, aber beachten Sie bitte, dass auch [Computer-Versionen verfügbar sind](https://www.olvid.io/download/) (MacOS, Linux und Windows). Wenn Sie die kostenpflichtige Version wählen, können Sie Ihr Konto auf mehreren Geräten synchronisieren.



![Image](assets/fr/01.webp)



## Ein Konto bei Olvid erstellen



Wenn Sie die Anwendung zum ersten Mal starten, klicken Sie auf die Schaltfläche "*Ich bin ein neuer Benutzer*".



![Image](assets/fr/02.webp)



Wählen Sie einen Spitznamen oder geben Sie Ihren Vor- und Nachnamen ein.



![Image](assets/fr/03.webp)



Fügen Sie ein Profilfoto hinzu.



![Image](assets/fr/04.webp)



Ihr Konto ist nun erstellt.



![Image](assets/fr/05.webp)



Um den Verlust des Zugriffs auf Ihr Olvid-Konto zu verhindern, empfehlen wir Ihnen, automatische Sicherungen einzurichten. Öffnen Sie dazu die Einstellungen, indem Sie auf die drei Punkte oben rechts im Interface klicken und dann "*Einstellungen*" wählen.

⚠️ **Achtung**: Seit Version 3.7 von Olvid wurde das Verfahren zum Sichern Ihrer Profile und Kontakte durch ein neues ersetzt. Dieses Tutorial zeigt noch die alte Version. Sie können die neue Version in deren FAQ entdecken: [💾 Sichern Ihrer Profile](https://www.olvid.io/faq/sauvegarder-vos-profils/)

![Image](assets/fr/06.webp)



Rufen Sie das Menü "*Tasten und Kontakte speichern*" auf.



![Image](assets/fr/07.webp)



Klicken Sie dann auf "*generate ein Sicherungsschlüssel*". Mit diesem Schlüssel werden Ihre Backups verschlüsselt. Wenn Sie Ihr Konto auf einem anderen Gerät wiederherstellen müssen und keinen Zugriff mehr darauf haben, benötigen Sie sowohl ein Backup als auch diesen Schlüssel, um es zu entschlüsseln.



![Image](assets/fr/08.webp)



Bewahren Sie diesen Schlüssel an einem sicheren Ort auf. Sie können auch eine Kopie auf Papier anfertigen.



![Image](assets/fr/09.webp)



Sie können dann wählen, ob Sie ein lokales Backup oder ein automatisches Backup in einem Cloud-Dienst erstellen möchten. Die zweite Option wird dringend empfohlen, um den Zugang zu Ihrem Olvid-Konto unter allen Umständen zu gewährleisten, auch wenn Sie Ihr Telefon verlieren.



![Image](assets/fr/10.webp)



Vergewissern Sie sich, dass die Option "*Automatische Sicherung aktivieren*" aktiviert ist.



![Image](assets/fr/11.webp)



Sie können auch die anderen verfügbaren Einstellungen erkunden, um die Anwendung an Ihre Bedürfnisse anzupassen.



![Image](assets/fr/12.webp)



## Versenden von Nachrichten mit Olvid



Um Nachrichten senden zu können, müssen Sie zunächst Kontakte hinzufügen. Klicken Sie auf der Startseite auf die blaue Schaltfläche "*+*".



![Image](assets/fr/13.webp)



Olvid zeigt dann Ihre Benutzer-ID an. Sie können diese dann an die Personen weitergeben, mit denen Sie kommunizieren möchten, damit diese Sie als Kontakt hinzufügen können.



Um eine Person hinzuzufügen, scannen Sie ihren Ausweis mit Ihrer Kamera oder fügen Sie ihn manuell ein, indem Sie auf die drei kleinen Punkte in der oberen rechten Ecke klicken.



![Image](assets/fr/14.webp)



Sobald die ID gescannt wurde, können Sie entweder Ihren Kontakt den angezeigten QR-Code scannen lassen oder ihm eine Fernverbindungsanfrage senden, indem Sie auf "*Fernkontakt*" klicken.



![Image](assets/fr/15.webp)



Die Verbindung ist nun hergestellt.



![Image](assets/fr/16.webp)



Sie können nun Nachrichten und andere Inhalte mit Ihrem Korrespondenten austauschen!



![Image](assets/fr/17.webp)



Auf der Startseite finden Sie alle Ihre Unterhaltungen.



![Image](assets/fr/18.webp)



Die zweite Registerkarte enthält alle Ihre Kontakte.



![Image](assets/fr/19.webp)



Sie können auch Gruppendiskussionen erstellen.



![Image](assets/fr/20.webp)



Herzlichen Glückwunsch, Sie sind jetzt auf dem Laufenden, was die Verwendung von Olvid Messaging angeht, einer großartigen Alternative zu WathsApp! Wenn Sie dieses Tutorial nützlich fanden, wäre ich Ihnen sehr dankbar, wenn Sie unten einen Green-Daumen hinterlassen würden. Sie können dieses Tutorial auch gerne in Ihren sozialen Netzwerken teilen. Herzlichen Dank!



Ich empfehle auch dieses andere Tutorial, in dem ich Ihnen Proton Mail vorstelle, eine viel datenschutzfreundlichere Alternative zu Gmail :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2