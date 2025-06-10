---
name: SimpleX Chat
description: Die erste Mailbox ohne Benutzer-ID
---
![cover](assets/cover.webp)



SimpleX wurde 2021 eingeführt und ist eine kostenlose Instant-Messaging-Anwendung mit einem radikal anderen Ansatz für den Datenschutz. Im Gegensatz zu WhatsApp, Signal und anderen zentralisierten Messaging-Diensten zeichnet sich SimpleX durch seine Benutzerverwaltung aus: Es gibt keine Benutzerkennungen, Pseudonyme, Nummern oder sichtbare öffentliche Schlüssel. Diese völlige Abwesenheit von Identifikatoren macht es praktisch unmöglich, Benutzer zuzuordnen und garantiert ein hohes Maß an Privatsphäre.



Im Gegensatz zu den meisten Anwendungen, die ein Konto oder eine Telefonnummer erfordern, können Sie mit SimpleX Unterhaltungen durch das Teilen eines Links oder eines flüchtigen QR-Codes einleiten. Jeder Link erzeugt einen eindeutigen verschlüsselten Kanal, und die Kontakte können den Absender nicht ohne eine ausdrückliche Exchange finden oder erneut kontaktieren. Die Nachrichten werden von Anfang bis Ende verschlüsselt und durchlaufen Relay-Server, die sie nach dem Versand löschen und weder den Absender noch den Empfänger oder ihre Schlüssel sehen.



![Image](assets/fr/01.webp)



Die Netzarchitektur ist vollständig dezentralisiert und unverbunden: Die Server kennen einander nicht, sie führen kein globales Verzeichnis und sie hosten keine Benutzerprofile. Noch besser ist, dass jeder Benutzer seinen eigenen Relay-Server einrichten und verwenden kann, während er mit den Servern im öffentlichen Netz interoperabel bleibt.



SimpleX ist vollständig quelloffen (Clients, Protokolle und Server) und auf Android, iOS, Linux, Windows und macOS verfügbar. Der lokale Speicher ist verschlüsselt und portabel, sodass Sie ein Profil von einem Gerät auf ein anderes übertragen können, ohne auf einen zentralen Server angewiesen zu sein.



SimpleX verfügt über alle klassischen Funktionen von Messaging-Anwendungen. Seine Ergonomie ist jedoch weniger flüssig als die von WhatsApp oder Signal. Außerdem kann die Nutzung restriktiver sein, insbesondere beim Hinzufügen von Kontakten. Meiner Meinung nach ist SimpleX eine interessante Alternative zu WhatsApp oder Signal für Nutzer, die Vertraulichkeit zu ihren Prioritäten zählen und deshalb bereit sind, einige Zugeständnisse in Bezug auf den alltäglichen Nutzungskomfort zu machen.



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



## Installieren Sie die SimpleX Chat-Anwendung



SimpleX Chat ist auf allen Plattformen verfügbar. Sie können die Anwendung direkt aus dem App Store Ihres Telefons herunterladen:




- [Google Play](https://play.google.com/store/apps/details?id=chat.simplex.app);
- [App Store] (https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084);
- [F-Droid](https://simplex.chat/fdroid/).



Unter Android ist auch eine [Installation über APK] möglich (https://github.com/simplex-chat/simplex-chat/releases).



In diesem Tutorial konzentrieren wir uns auf die mobile Version, aber beachten Sie bitte, dass auch [Desktop-Versionen verfügbar sind](https://simplex.chat/downloads/) (MacOS, Linux und Windows). Es ist möglich, die Desktop-Version mit einem bestehenden mobilen Benutzerprofil zu verknüpfen, aber damit diese Synchronisierung funktioniert, müssen beide Geräte mit demselben lokalen Netzwerk verbunden sein.



![Image](assets/fr/02.webp)



## Erstellen Sie ein Konto bei SimpleX Chat



Wenn Sie die Anwendung zum ersten Mal starten, klicken Sie auf die Schaltfläche "*Erstellen Sie Ihr Profil*".



![Image](assets/fr/03.webp)



Wählen Sie einen Benutzernamen, der Ihr richtiger Name oder ein Pseudonym sein kann, und klicken Sie dann auf "*Erstellen*".



![Image](assets/fr/04.webp)



Legen Sie dann die Häufigkeit fest, mit der die Anwendung nach neuen Nachrichten sucht. Wenn die Akkulaufzeit Ihres Telefons kein Problem darstellt, wählen Sie "*Instant*", um Nachrichten in Echtzeit zu erhalten. Wenn Sie Ihren Akku schonen und verhindern möchten, dass die Anwendung im Hintergrund läuft, wählen Sie "*Wenn die Anwendung läuft*": Sie erhalten dann nur Nachrichten, wenn die Anwendung geöffnet ist. Ein möglicher Kompromiss besteht darin, sich für eine regelmäßige Überprüfung alle 10 Minuten zu entscheiden.



Sobald Sie Ihre Wahl getroffen haben, klicken Sie auf "*Chat benutzen*".



![Image](assets/fr/05.webp)



Sie sind nun mit SimpleX Chat verbunden und können mit dem Chatten beginnen.



![Image](assets/fr/06.webp)



## SimpleX Chat einrichten



Um zu den Einstellungen zu gelangen, klicken Sie zunächst auf Ihr Profilfoto in der rechten unteren Ecke und dann auf "*Einstellungen*".



![Image](assets/fr/07.webp)



Die Standardeinstellungen sind im Allgemeinen für die meisten Benutzer geeignet. Ich empfehle Ihnen jedoch, das Menü "*Datenbank passphrase & Export*" aufzurufen. Hier können Sie Ihre SimpleX-Kontodatenbank zu Sicherungszwecken exportieren.



Sie können auch das zur Verschlüsselung dieser Datenbank verwendete passphrase ändern. Standardmäßig wird es zufällig generiert und lokal auf Ihrem Gerät gespeichert. Wenn Sie es vorziehen, können Sie Ihr eigenes passphrase definieren und die lokale passphrase-Sicherung löschen: Sie müssen es dann jedes Mal manuell eingeben, wenn Sie die Anwendung öffnen, und auch, wenn Sie auf ein anderes Gerät migrieren.



**Bitte beachten Sie**: Wenn Sie diese Option wählen, führt der Verlust des passphrase zum dauerhaften Verlust aller Ihrer SimpleX-Profile und Nachrichten.



![Image](assets/fr/08.webp)



Ich empfehle Ihnen auch, das Menü "*Datenschutz & Sicherheit*" aufzurufen, wo Sie die Option "*SimpleX Lock*" aktivieren können. Damit wird der Zugriff auf die Anwendung mit einem Sperrcode geschützt.



![Image](assets/fr/09.webp)



Mit den Menüs "*Benachrichtigungen*" und "*Erscheinungsbild*" können Sie SimpleX Chat Ihren Wünschen entsprechend anpassen.



![Image](assets/fr/10.webp)



## Nachrichten senden mit SimpleX Chat



Um sich mit einer anderen Person auf SimpleX zu verbinden, haben Sie zwei Möglichkeiten:




- Verwenden Sie einen Link zur einmaligen Verwendung;
- Verwenden Sie ein wiederverwendbares statisches Address.



Ein statischer Address ermöglicht es jedem, der ihn kennt, Sie auf SimpleX zu kontaktieren. Es handelt sich um einen persistenten Address, der ohne zeitliche Begrenzung mehrmals von verschiedenen Personen verwendet werden kann. Diese Beständigkeit macht sie anfälliger für Spam. Im Gegensatz zu anderen Messaging-Anwendungen reicht es jedoch aus, den SimpleX Address zu löschen, um alle Spam-Mails zu stoppen, ohne dass bestehende Unterhaltungen beeinträchtigt werden. Dieser Address wird nur für den Aufbau der ersten Verbindung verwendet und wird nicht mehr benötigt, sobald der Exchange begonnen hat.



Einmalige Links hingegen können von jedem Nutzer nur einmal verwendet werden. Sobald ein Kontakt ihn verwendet, wird der Link ungültig. Sie müssen für jede neue Verbindung einen neuen generate-Link erstellen.



### Mit statischem Address



Wenn Sie den Address verwenden möchten, klicken Sie auf Ihr Profilbild unten links im Interface und wählen dann "*Create SimpleX Address*". Klicken Sie dann erneut auf "*Create SimpleX Address*".



![Image](assets/fr/11.webp)



Ihr wiederverwendbarer Address wurde nun erstellt. Sie können ihn mit Personen teilen, die mit Ihnen in Kontakt treten möchten, indem Sie ihnen den QR-Code zeigen oder den Link schicken.



![Image](assets/fr/12.webp)



Klicken Sie auf die Schaltfläche "*Address Einstellungen*". Hier können Sie die mit Ihrem Address verbundenen Berechtigungen konfigurieren. Die Option "*Mit Kontakten teilen*" macht Ihren Address in Ihrem SimpleX-Profil sichtbar. Ihre Kontakte können es dann einsehen und an andere Personen weiterleiten, die Sie kontaktieren möchten.



Die Option "*Auto-akzeptieren*" nimmt automatisch eingehende Verbindungen über Ihren Address an. Das bedeutet, dass jeder, der Ihren Address besitzt, Ihr Profil sehen und Ihnen eine Nachricht senden kann, es sei denn, Sie aktivieren die Option "*Inkognito akzeptieren*". Diese Option verbirgt Ihren Namen und Ihr Profilfoto, wenn eine neue Verbindung hergestellt wird, und ersetzt sie durch ein zufälliges Pseudonym, das sich für jeden Gesprächspartner unterscheidet.



![Image](assets/fr/13.webp)



### Mit wiederverwendbarem Link



Die zweite Möglichkeit, mit einer Person in Verbindung zu treten, besteht darin, einen einmaligen Link zu erstellen. Klicken Sie dazu auf das Bleistiftsymbol in der unteren rechten Ecke von Interface und wählen Sie dann "*Einmalige Verknüpfung erstellen*".



Wenn Ihr Kontakt Ihnen einen Link geschickt hat, klicken Sie auf "*Link scannen / einfügen*", um ihn zu scannen oder einzufügen.



![Image](assets/fr/14.webp)



SimpleX generiert dann einen Link zur einmaligen Verwendung. Sie können ihn auf beliebige Weise an Ihren Kontakt weiterleiten: per Exchange, über andere Nachrichten usw.



![Image](assets/fr/15.webp)



Sie können auch wählen, welches Profil mit diesem Einladungslink verknüpft werden soll. Klicken Sie dazu auf Ihr Profil direkt unter dem QR-Code. Sie werden dann in der Lage sein, :




- wählen Sie eines Ihrer vorhandenen Profile aus (wie Sie mehrere Profile erstellen können, erfahren Sie im nächsten Abschnitt);
- oder wählen Sie den "*Incognito*"-Modus, der Ihren Namen und Ihr Profilfoto mit einem zufällig generierten Pseudonym für Ihren Korrespondenten verbirgt.



Hier wähle ich den Modus "*Incognito*".



![Image](assets/fr/16.webp)



Mein Kontakt hat den Link benutzt. Er seinerseits hat den "*Incognito*"-Modus nicht aktiviert, weshalb ich seinen Profilnamen "*Bob*" sehe. Andererseits sieht Bob nicht meinen richtigen Namen "*Loïc Morel*", sondern ein zufälliges Pseudonym, in diesem Fall "*RealSynergy*".



![Image](assets/fr/17.webp)



Ich könnte sofort mit dem Chat beginnen, aber zuerst möchte ich sicherstellen, dass ich mit Bob spreche und nicht mit einer böswilligen Person, die die Verbindung abgefangen oder einen MITM-Angriff durchgeführt hat.



Zu diesem Zweck werden wir unsere Sicherheitsverbindung **außerhalb der Anwendung** überprüfen. Dies ist wichtig, denn im Falle eines MITM-Angriffs wäre die interne Überprüfung gefährdet. Verwenden Sie also ein anderes sicheres Nachrichtensystem, oder noch besser, überprüfen Sie die Codes persönlich.



Klicken Sie im Chat auf Bobs Foto und dann auf "*Sicherheitscode überprüfen*". Bob muss dasselbe auf seiner Seite tun.



![Image](assets/fr/18.webp)



Wenn Sie aus der Ferne arbeiten, vergleichen Sie die Codes in einem anderen sicheren Nachrichtensystem (sie müssen identisch sein). Oder noch besser, wenn Sie sich persönlich treffen können, scannen Sie den QR-Code Ihres Kontakts, indem Sie auf "*Scan code*" klicken.



![Image](assets/fr/19.webp)



Wenn die Überprüfung erfolgreich war, erscheint ein Schildsymbol mit einem Häkchen neben dem Namen Ihres Kontakts. Dies ist Ihre Versicherung, dass Sie mit Bob austauschen. Wenn die Überprüfung nicht erfolgreich ist, erscheint die Meldung "*Fehlerhafter Sicherheitscode!*".



![Image](assets/fr/20.webp)



Sie können nun frei Exchange Nachrichten, Anrufe und Dateien mit Bob austauschen, je nach den Berechtigungen, die Sie für diese Unterhaltung festgelegt haben.



## Passen Sie Ihre SimpleX Chat-Profile an



Eine der leistungsfähigsten Funktionen von SimpleX ist die Möglichkeit, mehrere völlig getrennte Benutzerprofile zu verwalten, die alle über dasselbe lokale Konto zugänglich sind. So können Sie Ihre verschiedenen Identitäten sauber trennen, ohne das Nachrichtenmanagement zu verkomplizieren.



Sie könnten zum Beispiel eine :




- Ein Profil mit Ihrem echten Namen und einem echten Foto für Ihren beruflichen Austausch;
- Ein Profil mit Ihrem echten Namen und einem lustigen Foto für den Austausch mit Ihrer Familie;
- Ein Profil mit einem gefälschten Foto und einem Pseudonym für Ihre persönlichen Unterhaltungen;
- Ein weiteres pseudonymes Profil zum Chatten mit Fremden.



Genau das werden wir hier tun. Ich beginne mit der Konfiguration meines Hauptprofils, das mit meiner echten Identität verknüpft ist. Dazu klicke ich auf mein Profilfoto in der unteren rechten Ecke und dann auf meinen Benutzernamen.



![Image](assets/fr/21.webp)



Ich klicke dann auf mein Profilfoto, um es zu ändern und ein neues hinzuzufügen.



![Image](assets/fr/22.webp)



Um weitere Profile hinzuzufügen, klicken Sie auf das Menü "*Ihre Chat-Profile*".



![Image](assets/fr/23.webp)



Hier sehen Sie alle Ihre Profile. Klicken Sie auf "*Profil hinzufügen*", um ein neues Profil zu erstellen.



![Image](assets/fr/24.webp)



Wählen Sie dann die Informationen für Ihr neues Profil aus: Name, Foto usw. Hier verwende ich ein Pseudonym und ein anderes Bild, um meine wirkliche Identität bei bestimmten Kontakten zu verbergen.



![Image](assets/fr/25.webp)



Wenn Sie den Finger auf ein Profil halten, können Sie es ausblenden. Dadurch wird es in der Anwendung unsichtbar, zusammen mit allen zugehörigen Unterhaltungen. Sie können es auch "*stumm*" schalten, um keine Benachrichtigungen mehr zu erhalten.



![Image](assets/fr/26.webp)



Sobald Sie Ihre Profile erstellt haben, können Sie sie unabhängig voneinander verwalten. Wählen Sie auf der Startseite einfach das aktive Profil aus, das angezeigt werden soll.



![Image](assets/fr/27.webp)



Wenn Sie einen Einladungslink oder einen statischen Address erstellen, können Sie jetzt wählen, welches Profil damit verknüpft werden soll. Wenn ich z. B. das Profil "*Satoshi Nakamoto*" auswähle, um einen generate-Link zu erstellen und ihn an Alice zu senden, wird sie nur meine pseudonyme Identität "*Satoshi Nakamoto*" sehen, ohne jemals meine echte Identität "*Loïc Morel*" zu kennen. Wenn ich ihr dagegen einen Link von meinem echten Profil schicke, hat sie keine Möglichkeit, sich mit meinem pseudonymen Profil zu verbinden.



![Image](assets/fr/28.webp)



Herzlichen Glückwunsch, Sie sind jetzt auf dem neuesten Stand in Sachen SimpleX Messaging, einer hervorragenden Alternative zu WathsApp!



Ich empfehle auch dieses andere Tutorial, in dem ich Threema vorstelle, eine weitere interessante Alternative für Ihre Messaging-Anwendung:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74