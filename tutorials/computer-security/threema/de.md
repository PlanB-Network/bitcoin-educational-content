---
name: Threema
description: Sichere, anonyme Sofortnachrichten
---
![cover](assets/cover.webp)



Threema wurde 2012 in der Schweiz gegründet und ist eine Instant-Messaging-App, die Privatsphäre und Sicherheit garantieren soll. Im Gegensatz zu WhatsApp, Telegram oder Signal benötigt Threema keine Telefonnummer oder E-Mail Address, um ein Konto zu erstellen. Jeder Nutzer hat eine eindeutige Kennung, die eine völlig anonyme Registrierung ermöglicht.



Auf der technischen Seite ist die Kommunikation über Threema Ende-zu-Ende verschlüsselt. Der Code der mobilen Anwendung ist seit 2020 quelloffen, aber die Serverinfrastruktur bleibt proprietär und zentralisiert. Die Server werden ausschließlich in der Schweiz gehostet (einem Land, das für seinen rechtlichen Rahmen für den Datenschutz bekannt ist).



![Image](assets/fr/01.webp)



Threema hat Basis-Clients für Android und iOS. Es gibt auch eine Webanwendung sowie Software für Windows, Linux und macOS. Um sie zu nutzen, müssen Sie sich jedoch zunächst auf einem mobilen Gerät registrieren.



Die Threema-Anwendung ist nicht kostenlos. Sie funktioniert nach einem einmaligen Kaufmodell: 5,99 €, um die App lebenslang zu nutzen (oder 4,99 €, wenn Sie sie direkt kaufen). Um Threema wirklich anonym nutzen zu können, muss auch die Zahlung anonym sein. Aus diesem Grund können Sie im *Threema Shop*" einen Aktivierungsschlüssel in Bitcoins oder Bargeld kaufen, um die Android-Version zu aktivieren. Auf iOS hingegen muss der Kauf über den App Store erfolgen, da Apple die Monetarisierung von Apps einschränkt.



Es gibt auch eine spezielle Geschäftsversion namens "*Threema Work*". In diesem Tutorial konzentrieren wir uns auf die Heimversion.



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



## Installieren Sie die Threema-Anwendung



Threema ist auf allen Plattformen verfügbar. Sie können die Anwendung direkt aus dem App Store Ihres Telefons herunterladen:




- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold](https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829);
- [App Store] (https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



Unter Android ist auch eine [Installation über APK] möglich (https://shop.threema.ch/en/download).



Es gibt auch [Computerversionen](https://threema.ch/download) (MacOS, Linux und Windows). Dieses Tutorial zeigt Ihnen, wie Sie diese synchronisieren können.



## Threema-Lizenz kaufen



Wenn Sie die Anwendung direkt über einen App-Store installiert haben, haben Sie bereits für die Lizenz bezahlt und sollten sofort Zugriff darauf haben. Wenn Sie über F-Droid oder die APK gegangen sind, müssen Sie nun eine Lizenz auf der offiziellen Website erwerben.



[Gehen Sie zum "*Threema Shop*" (https://shop.threema.ch/) und klicken Sie auf die Schaltfläche "*Threema für Android kaufen*".



![Image](assets/fr/02.webp)



Wählen Sie die Anzahl der Lizenzen, die Sie erwerben möchten (nur eine, wenn es nur für Sie ist), wählen Sie die Währung und wählen Sie die Art der Lieferung der Lizenz. Sie können wählen, ob Sie die Lizenz per E-Mail erhalten möchten oder direkt auf der Website, wenn Sie anonym bleiben möchten. Klicken Sie dann auf "*Zur Zahlung übergehen*".



![Image](assets/fr/03.webp)



Wählen Sie Ihre Zahlungsmethode. In meinem Fall werde ich mit Bitcoins bezahlen, was ich Ihnen auch empfehle, da Sie damit anonym bleiben können (vorausgesetzt, Sie verwenden Bitcoin ordnungsgemäß) und es viel bequemer ist als eine Barzahlung aus der Ferne. Klicken Sie dann auf "*Weiter*".



![Image](assets/fr/04.webp)



Wenn Sie kein Invoice benötigen, klicken Sie erneut auf "*Weiter*", ohne persönliche Daten einzugeben.



Bestätigen Sie dann Ihren Kauf, indem Sie auf "*Zahlung bestätigen*" klicken.



![Image](assets/fr/05.webp)



Sie müssen dann den angegebenen Betrag an den Bitcoin Address senden (Lightning wird leider noch nicht unterstützt). Sobald die Transaktion auf dem Blockchain bestätigt wurde, klicken Sie auf "*Schließen*" neben dem Invoice.



Sie haben dann Zugang zu Ihrem Lizenzschlüssel. Bitte beachten Sie: Wenn Sie keine E-Mail Address eingegeben haben, wird dieser Schlüssel hier nur angezeigt. Denken Sie daran, die URL der Seite zu speichern, damit Sie sie bei Bedarf später wieder aufrufen können.



![Image](assets/fr/06.webp)



## Erstellen Sie ein Konto bei Threema



Nun, da Sie Ihren Lizenzschlüssel haben, können Sie die Anwendung endlich starten. Wenn Sie Threema nicht über einen Anwendungsspeicher erworben haben, werden Sie beim ersten Start aufgefordert, Ihren Lizenzschlüssel einzugeben, den Sie auf der Website erworben haben.



![Image](assets/fr/07.webp)



Klicken Sie dann auf die Schaltfläche "*Jetzt einrichten*".



![Image](assets/fr/08.webp)



Bewegen Sie Ihren Finger über den Bildschirm, um generate eine Entropiequelle zu erzeugen, die für die Erstellung Ihrer "*Threema ID*" benötigt wird.



![Image](assets/fr/09.webp)



Ihre "*Threema ID*" wird dann angezeigt. Sie ermöglicht es Ihnen, andere Benutzer zu kontaktieren. Klicken Sie auf "*Weiter*".



![Image](assets/fr/10.webp)



Wählen Sie ein Passwort. Damit können Sie im Bedarfsfall den Zugang zu Ihrem Konto wiederherstellen. Wählen Sie ein möglichst langes und zufälliges Passwort und bewahren Sie eine sichere Kopie davon auf, zum Beispiel in einem Passwortmanager.



![Image](assets/fr/11.webp)



Wählen Sie dann einen Benutzernamen, der entweder Ihr richtiger Name oder ein Pseudonym sein kann.



![Image](assets/fr/12.webp)



Sie können dann Ihre Threema-ID mit Ihrer Telefonnummer verknüpfen. Das erleichtert Ihnen die Suche in Ihren Kontakten, aber wenn Sie Threema benutzen, dient das auch dazu, Ihre Anonymität zu wahren: Es ist also besser, sie nicht zu verknüpfen. Klicken Sie auf "*Weiter*".



![Image](assets/fr/13.webp)



Sobald Sie diesen Schritt abgeschlossen haben, klicken Sie auf "*Finish*".



![Image](assets/fr/14.webp)



Sie sind nun mit Threema verbunden und können mit der Kommunikation beginnen.



![Image](assets/fr/15.webp)



## Threema einrichten



Rufen Sie zunächst die Einstellungen auf, indem Sie auf die drei kleinen Punkte in der oberen rechten Ecke klicken und dann "*Einstellungen*" wählen.



![Image](assets/fr/16.webp)



Auf der Registerkarte "*Datenschutz*" finden Sie mehrere Optionen, die Sie an Ihre Bedürfnisse anpassen können:




- Synchronisieren der Kontakte auf Ihrem Telefon ;
- Annahme von Nachrichten von unbekannten Personen;
- Schreibkennzeichen bei der Dateneingabe ;
- Benachrichtigung über den Erhalt von Nachrichten...



![Image](assets/fr/17.webp)



Auf der Registerkarte "*Sicherheit*" empfehle ich, die Option "*Sperrmechanismus*" zu aktivieren, um den Zugriff auf die Anwendung zu schützen. Es ist auch ratsam, passphrase zu aktivieren, um Ihre lokalen Backups zu sichern.



![Image](assets/fr/18.webp)



Sie können auch die anderen Bereiche der Einstellungen erkunden, um die Anwendung an Ihre Wünsche anzupassen.



![Image](assets/fr/19.webp)



## Sichern Sie Ihr Threema-Konto



Bevor Sie mit dem Austausch von Nachrichten beginnen, ist es wichtig, dass Sie eine Möglichkeit zur Wiederherstellung Ihres Kontos planen, insbesondere für den Fall, dass Ihr Telefon ausgetauscht wird oder verloren geht. Klicken Sie dazu auf die drei Punkte oben rechts im Interface und rufen Sie dann das Menü "*Backups*" auf.



![Image](assets/fr/20.webp)



Hier finden Sie zwei Möglichkeiten, Ihre Daten zu sichern:




- "*Threema Safe*";
- "*Datensicherung*".



"Threema Safe* speichert alle Ihre Kontoinformationen, mit Ausnahme Ihrer Gespräche, auf den Servern von Threema. Diese Daten werden mit dem Passwort verschlüsselt, das Sie bei der Erstellung Ihres Kontos gewählt haben, so dass Threema keinen Zugriff auf sie hat. Die Backups werden automatisch und regelmäßig erstellt.



Mit "*Threema Safe*" müssen Sie nur Ihre "*Threema ID*" und Ihr Passwort eingeben, um Ihr Konto auf einem neuen Gerät wiederherzustellen. Wenn eine dieser beiden Informationen fehlt, ist es unmöglich, Ihr Konto wiederherzustellen.



Mit dieser Option können Sie nur Ihre ID, Ihr Profil, Ihre Kontakte, Gruppen und bestimmte Einstellungen abrufen, aber **nicht Ihren Gesprächsverlauf**.



Um "*Threema Safe*" zu aktivieren, aktivieren Sie einfach die Option im Menü "*Backups*".



![Image](assets/fr/21.webp)



Wenn Sie auch Ihren Gesprächsverlauf sichern und wiederherstellen möchten, müssen Sie die Option "*Datensicherung*" verwenden. Dadurch wird eine vollständige Sicherung Ihres Kontos erstellt, die lokal auf Ihrem Telefon gespeichert wird. Sie müssen diese Sicherung auf Ihr neues Gerät übertragen und Ihr Passwort (und möglicherweise Ihr passphrase) verwenden, um Ihr gesamtes Konto wiederherzustellen.



Da diese Sicherung nur lokal ist, muss sie regelmäßig auf externe Medien kopiert werden. Andernfalls ist eine Wiederherstellung unmöglich, wenn Ihr Gerät verloren geht. Diese Methode eignet sich daher am besten für eine geplante Übertragung von einem Gerät auf ein anderes und nicht für Notfallsituationen.



Bitte beachten Sie: "*Datensicherung*" funktioniert nur, wenn Sie das gleiche Betriebssystem verwenden. Sie können damit z. B. nicht von einem Samsung auf ein iPhone umsteigen.



## Passen Sie Ihr Threema-Profil an



Klicken Sie in der linken oberen Ecke von Interface auf Ihr Profilbild und wählen Sie dann "*Mein Profil*".



![Image](assets/fr/22.webp)



Hier können Sie Ihr Profil anpassen: fügen Sie ein Foto hinzu, wählen Sie aus, wer es sehen kann, oder sehen Sie Ihr Threema-Login.



![Image](assets/fr/23.webp)



## PC-Software synchronisieren



Wenn Sie auf Ihre Unterhaltungen auf Ihrem PC zugreifen möchten, können Sie Ihr Threema-Konto mit der entsprechenden Software synchronisieren. Laden Sie die Software für Ihr Betriebssystem [von der offiziellen Website] herunter (https://threema.ch/en/download).



![Image](assets/fr/24.webp)



Klicken Sie auf Ihrem Handy auf die drei Punkte oben rechts und öffnen Sie dann das Menü "*Threema 2.0 for Desktop*".



![Image](assets/fr/25.webp)



Klicken Sie auf "*Gerät hinzufügen*" und scannen Sie dann mit Ihrem Telefon den QR-Code, der von der Software auf Ihrem Computer angezeigt wird.



![Image](assets/fr/26.webp)



Um die Synchronisierung zu bestätigen, klicken Sie auf die in der Software angezeigte Emoji-Gruppe.



![Image](assets/fr/27.webp)



Melden Sie sich an Ihrem Computer mit Ihrem Passwort an.



![Image](assets/fr/28.webp)



Zusätzlich zur mobilen Anwendung können Sie jetzt auch direkt von Ihrem Computer aus auf Ihr Threema-Konto zugreifen.



![Image](assets/fr/29.webp)



## Versenden von Nachrichten mit Threema



Nun, da alles korrekt eingerichtet ist, können Sie mit der Kommunikation beginnen. Klicken Sie auf die Schaltfläche "*Chat starten*".



![Image](assets/fr/30.webp)



Wählen Sie "*Neuer Kontakt*".



![Image](assets/fr/31.webp)



Geben Sie die "*Threema ID*" Ihres Ansprechpartners ein oder scannen Sie sie ein.



![Image](assets/fr/32.webp)



Klicken Sie auf das Nachrichtensymbol.



![Image](assets/fr/33.webp)



Senden Sie eine erste Nachricht an Ihren Korrespondenten.



![Image](assets/fr/34.webp)



Wenn Ihr Gesprächspartner antwortet, wird die Verbindung hergestellt, und Sie können seinen Namen und sein Profilfoto sehen. Sie können dann Exchange-Nachrichten und Multimedia-Dateien versenden und sogar Anrufe tätigen.



![Image](assets/fr/35.webp)



Herzlichen Glückwunsch, Sie sind jetzt auf dem Laufenden, was die Verwendung von Threema Messaging angeht, einer großartigen Alternative zu WathsApp! Wenn Sie dieses Tutorial nützlich fanden, wäre ich Ihnen sehr dankbar, wenn Sie unten einen Green-Daumen hinterlassen würden. Sie können dieses Tutorial auch gerne in Ihren sozialen Netzwerken teilen. Herzlichen Dank!



Ich empfehle auch dieses andere Tutorial, in dem ich Ihnen Proton Mail vorstelle, eine viel datenschutzfreundlichere Alternative zu Gmail:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2