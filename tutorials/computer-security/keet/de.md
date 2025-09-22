---
name: Keet
description: Peer-to-Peer-Chat
---
![cover](assets/cover.webp)



Keet ist eine Instant-Messaging-Anwendung, die ohne Server funktioniert. Die 2022 von Holepunch (einem von Tether und Bitfinex finanzierten Unternehmen) lancierte Anwendung basiert vollständig auf einem Peer-to-Peer-Netzwerk und zeichnet sich durch einen radikal dezentralen Ansatz aus: Nachrichten, Anrufe und Dateien werden direkt zwischen den Nutzern ausgetauscht, ohne Zwischenhändler.



Keet verschlüsselt die gesamte Kommunikation von Anfang bis Ende und fragt keine persönlichen Daten ab. Die Registrierung ist anonym, es ist keine Telefonnummer oder E-Mail erforderlich. Neben dem Austausch von Textnachrichten bietet Keet auch Videoanrufe in sehr hoher Qualität sowie unbegrenzten Dateiaustausch. Die Anwendung kann daher sowohl für den privaten als auch für den beruflichen Gebrauch genutzt werden.



![Image](assets/fr/01.webp)



Im Moment (April 2025) ist Keet nicht vollständig quelloffen. Ein Teil des Quellcodes ist auf [Holepunch's GitHub repository](https://github.com/holepunchto) verfügbar, insbesondere die kryptographischen und Netzwerkkomponenten, aber der Client Interface ist es noch nicht. Holepunch hat jedoch angekündigt, dass es beabsichtigt, die gesamte Anwendung irgendwann als Open-Source zu veröffentlichen. Je nachdem, wann Sie dieses Tutorial entdecken, könnte dies bereits geschehen sein.




| Anwendung            | E2EE 1:1       | E2EE Gruppen   | Anonyme Registrierung | Client-Lizenz open-source | Server-Lizenz open-source | Dezentraler Server   | Entstehungsjahr   |
| -------------------- | -------------- | -------------- | --------------------- | ------------------------- | ------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                     | ❌                         | ❌                         | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                     | ❌                         | ❌                         | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optional) | ❌                     | ❌                         | ❌                         | ❌                    | 2011              |
| Telegram             | 🟡 (optional) | ❌              | 🟡                    | ✅                         | ❌                         | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                     | ❌                         | ❌                         | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                     | ✅                         | ✅                         | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                     | ✅                         | ❌                         | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                     | ✅                         | ✅                         | 🟡 (föderiert)      | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                     | ✅                         | N/A                       | 🟡 (über E-Mail)    | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                     | ✅                         | ✅                         | 🟡 (föderiert)      | 2014              |
| Session              | ✅              | ✅              | ✅                     | ✅                         | ✅                         | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                     | ✅                         | ✅                         | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                     | ✅                         | ❌                         | 🟡(kein Verzeichnis) | 2019              |
| Keet                 | ✅              | ✅              | ✅                     | ❌                         | N/A                       | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                     | ✅                         | N/A                       | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                     | ✅                         | N/A                       | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                     | ✅                         | N/A                       | ✅                    | 2013              |

*E2EE = Ende-zu-Ende-Verschlüsselung*



## Keet installieren



Keet ist auf allen Plattformen verfügbar. Sie können die Anwendung direkt aus dem App Store Ihres Telefons herunterladen:




- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store] (https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);



Unter Android ist auch eine [Installation über APK] möglich (https://github.com/holepunchto/keet-mobile-releases/releases).



In diesem Tutorial konzentrieren wir uns auf die mobile Version, aber bitte beachten Sie, dass es auch [Computer-Versionen gibt](https://keet.io/) (MacOS, Linux und Windows). Es ist auch möglich, Ihr Konto auf mehreren Geräten zu synchronisieren.



## Ein Konto auf Keet erstellen



Beim ersten Start können Sie die Präsentationsbildschirme ignorieren.



![Image](assets/fr/02.webp)



Klicken Sie auf die Schaltfläche "*Ich bin ein neuer Benutzer*".



![Image](assets/fr/03.webp)



Akzeptieren Sie die Nutzungsbedingungen und klicken Sie dann auf "*Schnelleinrichtung*".



![Image](assets/fr/04.webp)



Wählen Sie einen Namen oder Spitznamen und klicken Sie dann auf "*Einrichtung abschließen*".



![Image](assets/fr/05.webp)



Ihr Profil ist nun erstellt. Klicken Sie erneut auf "*Einrichtung abschließen*", um den Vorgang abzuschließen.



![Image](assets/fr/06.webp)



Sie können Ihr Profil jederzeit auf der Registerkarte "*Profil*" anpassen.



## Speichern Sie Ihr Keet-Konto



Das erste, was Sie mit Ihrem neuen Keet-Konto tun müssen, ist, Ihre Wiederherstellungsphrase zu speichern. Dabei handelt es sich um eine Abfolge von 24 Wörtern, mit der du bei Verlust oder Wechsel des Geräts den Zugang zu deinem Konto wiederherstellen kannst. Mit dieser Phrase hat jeder, der sie kennt, vollen Zugriff auf Ihr Konto. Daher ist es wichtig, eine zuverlässige Sicherungskopie zu erstellen und sie niemals weiterzugeben.



Klicken Sie dazu auf die Registerkarte "*Profil*" unten rechts auf dem Interface.



![Image](assets/fr/07.webp)



Rufen Sie dann das Menü "*Einstellungen*" auf.



![Image](assets/fr/08.webp)



Wählen Sie "*Datenschutz und Sicherheit*".



![Image](assets/fr/09.webp)



Klicken Sie dann auf "*Wiederherstellungssatz*".



![Image](assets/fr/10.webp)



Drücken Sie die Schaltfläche "*Phrase anzeigen*", um Ihre Wiederherstellungsphrase anzuzeigen. Kopieren Sie sie sorgfältig und bewahren Sie sie an einem sicheren Ort auf.



![Image](assets/fr/11.webp)



## Versenden von Nachrichten mit Keet



Um auf Keet zu kommunizieren, müssen Sie "*Rooms*" erstellen. Klicken Sie dazu auf das Bleistiftsymbol oben rechts im Interface.



![Image](assets/fr/12.webp)



Wählen Sie "*Neuer Gruppenchat*".



![Image](assets/fr/13.webp)



Wählen Sie einen Namen und eine Beschreibung für Ihren "*Raum*" und klicken Sie dann auf "*Gruppenchat erstellen*".



![Image](assets/fr/14.webp)



Ihr "*Raum*" ist nun erstellt. Klicken Sie auf das Symbol "*+*" oben rechts, um Teilnehmer einzuladen.



![Image](assets/fr/15.webp)



Legen Sie die Rechte fest, die Sie neuen Mitgliedern über den Einladungslink gewähren, sowie die Dauer der Gültigkeit des Links. Klicken Sie dann auf "*generate einladen*".



![Image](assets/fr/16.webp)



Keet wird generate einen Link zum Beitritt zu Ihrem "*Raum*" senden. Sie können ihn entweder kopieren und weitergeben oder seinen QR-Code von den Personen scannen lassen, die Sie einladen möchten.



![Image](assets/fr/17.webp)



Sie können nun Nachrichten und Multimedia-Dateien austauschen. Um einen Anruf zu starten, klicken Sie auf das Telefonsymbol in der oberen rechten Ecke.



![Image](assets/fr/18.webp)



Von dieser Gruppe aus können Sie auch private Nachrichten an ein bestimmtes Mitglied senden. Klicken Sie auf das Profilbild der Gruppe und wählen Sie dann das gewünschte Mitglied im Bereich "*Mitglieder*" aus.



![Image](assets/fr/19.webp)



Klicken Sie auf die Schaltfläche "*DM-Anfrage senden*" und geben Sie Ihre Nachricht ein.



![Image](assets/fr/20.webp)



Sobald die DM-Anfrage akzeptiert wurde, finden Sie diesen Kontakt auf der Startseite, wo Sie mit ihm privat sprechen können.



![Image](assets/fr/21.webp)



## Synchronisieren Sie Ihr Konto auf mehreren Geräten



Da Sie nun wissen, wie Sie Keet verwenden können und ein Konto haben, können Sie es auch mit einem anderen Gerät, z. B. einem Computer, synchronisieren. Öffnen Sie dazu die Anwendung auf Ihrem Handy, klicken Sie auf "*Profil*" und rufen Sie "*Einstellungen*" auf.



![Image](assets/fr/22.webp)



Gehen Sie dann in das Menü "*Meine Geräte*".



![Image](assets/fr/23.webp)



Klicken Sie auf "*Gerät hinzufügen*". Keet wird generate einen Link zum Synchronisieren eines neuen Geräts anbieten. Kopieren Sie diesen Link.



![Image](assets/fr/24.webp)



Installieren Sie Keet auf Ihrem zweiten Gerät. Wählen Sie auf dem Startbildschirm die Option "*Ich bin ein aktueller Benutzer*".



![Image](assets/fr/25.webp)



Klicken Sie dann auf "*Gerät verbinden*".



![Image](assets/fr/26.webp)



Fügen Sie den Link ein, den Sie von Ihrem ersten Gerät erhalten haben, und klicken Sie dann auf "*Synchronisierung starten*".



![Image](assets/fr/27.webp)



Klicken Sie auf Ihrem ersten Gerät auf "*Verbindungsgeräte bestätigen*", um die Verbindung zu autorisieren.



![Image](assets/fr/28.webp)



Auf dem zweiten Gerät schließen Sie den Vorgang ab, indem Sie auf "*Geräte verbinden*" klicken.



![Image](assets/fr/29.webp)



Sie können nun von diesem neuen Gerät aus auf alle Ihre "*Raum*" und Gespräche zugreifen.



![Image](assets/fr/30.webp)



Herzlichen Glückwunsch, Sie sind jetzt auf dem Laufenden, was die Verwendung von Keet Messaging angeht, einer großartigen Alternative zu WathsApp! Wenn Sie dieses Tutorial nützlich fanden, wäre ich Ihnen sehr dankbar, wenn Sie unten einen Green-Daumen hinterlassen würden. Du kannst dieses Tutorial auch gerne in deinen sozialen Netzwerken teilen. Herzlichen Dank!



Ich empfehle auch dieses andere Tutorial, in dem ich Ihnen Proton Mail vorstelle, eine viel datenschutzfreundlichere Alternative zu Gmail:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2