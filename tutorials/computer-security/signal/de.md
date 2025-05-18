---
name: Signal
description: Drücken Sie sich frei aus
---
![cover](assets/cover.webp)



Signal ist eine Ende-zu-Ende-verschlüsselte Messaging-Anwendung, die standardmäßig eine hohe Vertraulichkeit bietet. Jede Nachricht, jeder Anruf und jede Datei wird durch das Signal-Protokoll geschützt, das als eines der robustesten Messaging-Protokolle gilt. Es wird von vielen anderen Anwendungen wiederverwendet, darunter WathsApp, Facebook Messenger, Skype und Google Messages für RCS-Kommunikation.



Signal wurde 2014 von Moxie Marlinspike (Pseudonym) ins Leben gerufen und wird seit 2018 von der Signal Foundation entwickelt, einer gemeinnützigen Organisation, die mit Unterstützung von Brian Acton (Mitbegründer von WhatsApp) gegründet wurde.



![Image](assets/fr/01.webp)



Im Vergleich zu WhatsApp zeichnet sich Signal durch seine Transparenz aus: Der Code der Anwendung, sowohl client- als auch serverseitig, ist vollständig quelloffen. Dies ermöglicht es jedem, die Anwendung zu überprüfen und insbesondere zu kontrollieren, ob die Verschlüsselung wie angekündigt angewendet wird.



Allerdings ist Signal auf die Verwendung einer Telefonnummer angewiesen, was im Vergleich zu anderen Lösungen die größte Schwäche in Sachen Anonymität darstellt. Trotzdem ist die Anwendung meiner Meinung nach eine der zuverlässigsten in Bezug auf Sicherheit und Vertraulichkeit, dank ihrer völlig offenen Architektur und einem weit verbreiteten Verschlüsselungsprotokoll, und daher getestet und geprüft, im Gegensatz zu anderen, eher marginalen Anwendungen.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| **Signal**           | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Ende-zu-Ende-Verschlüsselung*




## Installieren Sie die Anwendung Signal



Signal ist auf allen Plattformen verfügbar. Sie können die Anwendung direkt aus dem Anwendungsspeicher Ihres Telefons herunterladen:




- [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms);
- [App Store] (https://apps.apple.com/us/app/signal-private-messenger/id874139669);



Unter Android ist auch eine [Installation über APK] möglich (https://github.com/signalapp/Signal-Android/releases).



In dieser Anleitung konzentrieren wir uns auf die mobile Version, aber beachten Sie bitte, dass auch [Desktop-Versionen verfügbar sind](https://signal.org/fr/download/) (MacOS, Linux und Windows). Sie müssen jedoch zunächst die mobile Anwendung einrichten, bevor Sie Ihr Konto mit der Desktop-Version synchronisieren können.



## Erstellen Sie ein Konto bei Signal



Wenn Sie die Anwendung zum ersten Mal starten, klicken Sie auf die Schaltfläche "*Fortfahren*".



![Image](assets/fr/02.webp)



Geben Sie Ihre Telefonnummer ein und klicken Sie dann auf "*Weiter*".



![Image](assets/fr/03.webp)



Ein Verifizierungscode wird Ihnen per SMS zugesandt. Geben Sie diesen Code in der Anwendung Signal ein.



![Image](assets/fr/04.webp)



Wählen Sie einen PIN-Code, um Ihr Signal-Konto zu sichern. Dieser Code verschlüsselt Ihre Daten und kann verwendet werden, um den Zugriff auf Ihr Konto wiederherzustellen, wenn Ihr Gerät verloren geht. Daher ist es wichtig, einen stabilen PIN-Code zu wählen, der möglichst lang und zufällig ist, und ihn zuverlässig aufzubewahren.



![Image](assets/fr/05.webp)



Bestätigen Sie diesen PIN-Code ein zweites Mal.



![Image](assets/fr/06.webp)



Sie können jetzt Ihr Benutzerprofil personalisieren. Wählen Sie ein Foto, geben Sie Ihren Namen oder einen Spitznamen ein. In diesem Stadium können Sie auch festlegen, wer Sie auf Signal über Ihre Nummer finden kann. Wählen Sie "*Jeder*", wenn Sie sichtbar sein wollen, oder "*Niemand*", um über die Telefonnummer nicht auffindbar zu sein (Sie können dann nur mit Ihrem "*Benutzername*" hinzugefügt werden). Sobald Sie Ihre Auswahl getroffen haben, klicken Sie auf "*Weiter*".



![Image](assets/fr/07.webp)



Sie sind jetzt mit Signal verbunden und können Exchange-Nachrichten versenden.



![Image](assets/fr/08.webp)



## Einrichten Ihres Signal-Kontos



Klicken Sie auf Ihr Profilfoto in der oberen linken Ecke, um zu den Anwendungseinstellungen zu gelangen.



![Image](assets/fr/09.webp)



Im Menü "*Konto*" können Sie Ihre Profileinstellungen verwalten. Ich empfehle Ihnen, die Standardeinstellungen beizubehalten. Sie können auch die Option "*Registrierungssperre*" aktivieren, die Ihr Konto gegen bestimmte Arten von Angriffen schützt. Dieses Menü enthält auch die Optionen, die Sie benötigen, um Ihr Konto auf ein neues Gerät zu übertragen.



![Image](assets/fr/10.webp)



Wenn Sie in den Einstellungen erneut auf Ihr Profilbild klicken, gelangen Sie zu den Optionen für die Personalisierung Ihres Profils. Ich empfehle Ihnen, einen "*Benutzernamen*" festzulegen: So können Sie mit anderen Personen in Kontakt treten, ohne Ihre Telefonnummer preiszugeben.



![Image](assets/fr/11.webp)



Wenn Sie "*QR-Code oder Link*" auswählen, erhalten Sie die Informationen, die Sie mit jemandem teilen müssen, der Sie zu Signal hinzufügen möchte.



![Image](assets/fr/12.webp)



Das Menü "*Privatsphäre*" ist besonders wichtig. Hier finden Sie Optionen für die Kontrolle der Sichtbarkeit Ihrer Nummer, die Verwaltung Ihrer Nachrichten mit Ihren Kontakten sowie verschiedene Berechtigungen, die in der Anwendung vergeben werden.



![Image](assets/fr/13.webp)



Und Sie können die Menüs "*Erscheinungsbild*", "*Chats*" und "*Benachrichtigungen*" erkunden, um Interface und die Bedienung der Anwendung an Ihre persönlichen Bedürfnisse anzupassen.



## Desktop-Anwendung verbinden



Um die Desktop-Anwendung zu verbinden, installieren Sie zunächst die Software auf Ihrem Computer (siehe den ersten Teil dieses Tutorials). Gehen Sie dann auf Ihrem Telefon zu Einstellungen und öffnen Sie den Abschnitt "*Verknüpfte Geräte*".



![Image](assets/fr/14.webp)



Klicken Sie auf die Schaltfläche "*Ein neues Gerät verbinden*".



![Image](assets/fr/15.webp)



Starten Sie die Software auf Ihrem Computer und scannen Sie dann den auf dem Bildschirm angezeigten QR-Code mit Ihrem Telefon. Wenn Sie Ihre Unterhaltungen importieren möchten, wählen Sie die Option "*Nachrichtenverlauf übertragen*".



![Image](assets/fr/16.webp)



Ihre Geräte sind nun vollständig synchronisiert.



![Image](assets/fr/17.webp)



## Versenden von Nachrichten mit Signal



Um mit jemandem auf Signal zu kommunizieren, müssen Sie ihn zunächst als Kontakt hinzufügen. Es gibt mehrere Möglichkeiten: Sie können sie über ihre Telefonnummer hinzufügen (wenn die Person die Option aktiviert hat, auf diese Weise gefunden zu werden), oder ihre Signal-ID verwenden.



Klicken Sie auf das Bleistiftsymbol in der unteren rechten Ecke des Interface.



![Image](assets/fr/18.webp)



In meinem Fall möchte ich die Person anhand ihres Benutzernamens hinzufügen. Also klicke ich auf "*Nach Benutzernamen suchen*".



![Image](assets/fr/19.webp)



Sie können dann entweder den Login einfügen oder den QR-Code scannen.



![Image](assets/fr/20.webp)



Senden Sie ihm eine Nachricht, um Kontakt aufzunehmen.



![Image](assets/fr/21.webp)



Das Gespräch wird dann auf der Startseite angezeigt. Wenn die Person Ihre Kontaktanfrage annimmt, sehen Sie ihren Namen und ihr Profilfoto.



![Image](assets/fr/22.webp)



Herzlichen Glückwunsch, Sie sind jetzt auf dem neuesten Stand bei der Verwendung von Signal Messaging, einer großartigen Alternative zu WathsApp! Wenn Sie dieses Tutorial nützlich fanden, wäre ich Ihnen sehr dankbar, wenn Sie unten einen Green-Daumen hinterlassen würden. Sie können dieses Tutorial auch gerne in Ihren sozialen Netzwerken teilen. Herzlichen Dank!



Ich empfehle auch dieses andere Tutorial, in dem ich Ihnen Proton Mail vorstelle, eine viel datenschutzfreundlichere Alternative zu Gmail :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2