---
name: Session
description: Senden Sie verschlüsselte Nachrichten, keine Metadaten
---
![cover](assets/cover.webp)



Session ist eine verschlüsselte Nachrichtenanwendung aus dem Jahr 2020, die ein höheres Maß an Vertraulichkeit bieten soll als herkömmliche Nachrichtenübermittlung. Sie wurde zunächst von der *Oxen Privacy Tech Foundation* und dann von der *Session Technology Foundation* entwickelt.



Session verfügt über einige interessante technische Merkmale: eine Ende-zu-Ende-Verschlüsselung von Nachrichten, ein dezentralisiertes Netzwerk, das Verfügbarkeit und Redundanz garantiert, und ein von Tor inspiriertes Onion-Routing. Im Gegensatz zu WathsApp oder Signal, die eine Telefonnummer für die Registrierung benötigen, verlangt Session keine persönlichen Daten (keine Nummer, keine E-Mail, nur ein Paar kryptographische Schlüssel).



Mit Session können Sie Nachrichten, Dateien, Sprachnachrichten, Audioanrufe sowie Gruppen mit bis zu 100 Mitgliedern (und darüber hinausgehende Gemeinschaften) versenden, wobei die Gefahr von Metadatenlecks minimiert wird.



![Image](assets/fr/01.webp)



Session richtet sich vor allem an Nutzer, für die Vertraulichkeit im Mittelpunkt ihrer Prioritäten steht. Dieser Messaging-Dienst ist eine ernstzunehmende Alternative zu WhatsApp und verfügt über eine Architektur, die modernen Überwachungsmodellen standhält.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Ende-zu-Ende-Verschlüsselung*



## Installieren Sie die Anwendung Session



Session ist auf allen Plattformen verfügbar. Sie können die Anwendung direkt aus dem Anwendungsspeicher Ihres Telefons herunterladen:




- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store] (https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).



Unter Android ist auch eine [Installation über APK] möglich (https://github.com/session-foundation/session-android/releases).



In diesem Tutorial konzentrieren wir uns auf die mobile Version, aber beachten Sie bitte, dass auch [Computer-Versionen verfügbar sind](https://getsession.org/download) (MacOS, Linux und Windows). Später werden wir uns ansehen, wie Sie ein Konto über mehrere Geräte hinweg synchronisieren können.



## Ein Konto auf Session erstellen



Beim ersten Start klicken Sie auf "*Konto erstellen*".



![Image](assets/fr/02.webp)



Wählen Sie einen Anzeigenamen für Ihr Profil. Dies kann ein Pseudonym oder Ihr richtiger Name sein.



![Image](assets/fr/03.webp)



Sie müssen dann zwischen zwei Modi der Benachrichtigungsverwaltung wählen:





- Schneller Modus (**Firebase Cloud Messaging/Apple Push Notification Service**): Ermöglicht es Ihnen, dank der von Google oder Apple (je nach System) bereitgestellten Benachrichtigungsdienste Nachrichtenbenachrichtigungen nahezu in Echtzeit zu erhalten. Damit dies funktioniert, werden Ihre IP Address und eine eindeutige Benachrichtigungs-ID an Google oder Apple übermittelt, und die ID des Sitzungskontos wird ebenfalls bei einem STF-Server (über Tor) registriert. Dieser Modus beinhaltet eine (zugegebenermaßen minimale) Offenlegung von Metadaten, gefährdet aber nicht den Inhalt von Nachrichten oder Kontakten und ermöglicht keine Rückverfolgung Ihrer tatsächlichen Aktivitäten. Dieser Modus ist daher effizienter in Bezug auf die Reaktionsfähigkeit, stützt sich aber auf eine zentralisierte Infrastruktur und ist etwas weniger effektiv in Bezug auf die Vertraulichkeit.





- Langsamer Modus (**Hintergrundabfrage**): Die Sitzungsanwendung bleibt im Hintergrund aktiv und fragt regelmäßig das Netz nach neuen Nachrichten ab. Dieser Ansatz garantiert eine größere Vertraulichkeit als der erste, da keine Daten an Server von Drittanbietern übertragen werden; weder Google, Apple noch die STF-Server erhalten irgendwelche Informationen. Andererseits hat dieser Modus zwei Nachteile: Benachrichtigungen können sich verzögern (bis zu mehreren Minuten), und der Energieverbrauch ist im Allgemeinen aufgrund der Anwendungsaktivität im Hintergrund höher.



![Image](assets/fr/04.webp)



Sie sind nun mit der Anwendung Sitzung verbunden und können Nachrichten austauschen.



![Image](assets/fr/05.webp)



## Speichern Sie Ihr Sitzungskonto



Bevor Sie mit der Nutzung von Session beginnen, müssen Sie zunächst Ihr Konto speichern, damit Sie es wiederherstellen können, wenn Sie Ihr Gerät verlieren. Klicken Sie dazu auf die Schaltfläche "*Fortfahren*" neben "*Speichern Sie Ihr Wiederherstellungspasswort*".



![Image](assets/fr/06.webp)



Die Sitzung zeigt dann einen Mnemonic-Satz an. Kopieren Sie ihn sorgfältig und bewahren Sie ihn an einem sicheren Ort auf. Mit dieser Phrase haben Sie vollen Zugriff auf Ihr Session-Konto, daher ist es wichtig, sie nicht preiszugeben. Sie benötigen sie, um mit einem anderen Gerät auf Ihr Konto zuzugreifen, insbesondere wenn Sie Ihr aktuelles Telefon verlieren oder ersetzen.



![Image](assets/fr/07.webp)



Dieser Satz funktioniert auf ähnliche Weise wie die Mnemonic-Sätze in Bitcoin-Portfolios. Ich empfehle Ihnen daher, dieses andere Lernprogramm zu konsultieren, in dem ich die besten Verfahren zum Speichern eines Mnemonic-Satzes erkläre:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Bitte beachten**: Im Gegensatz zu den Mnemonic-Sätzen, die in den Bitcoin-Portfolios verwendet werden, müssen Sie bei Session **jedes Wort unbedingt in seiner Gesamtheit speichern**. Die ersten 4 Buchstaben sind nicht ausreichend!



## Einrichten der Anwendung Session



Um auf die Anwendungseinstellungen zuzugreifen, klicken Sie auf Ihr Profilfoto oben links in Interface. Hier können Sie ein Profilfoto hinzufügen.



![Image](assets/fr/08.webp)



Im Menü "*Datenschutz*" können Sie verschiedene Funktionen aktivieren oder deaktivieren (Vorsicht, einige können Ihre IP Address preisgeben). Ich empfehle auch, die Option "*App sperren*" zu aktivieren, die eine Authentifizierung für den Zugriff auf die Anwendung erfordert.



![Image](assets/fr/09.webp)



Im Menü "*Benachrichtigung*" haben Sie die Wahl zwischen "*Schneller Modus*" und "*Langsamer Modus*" (siehe vorherige Teile des Tutorials). Sie können die Benachrichtigungen auch an Ihre Vorlieben anpassen.



![Image](assets/fr/10.webp)



Gehen Sie schließlich zum Menü "*Erscheinungsbild*", um Interface nach Ihrem Geschmack anzupassen. Im Menü "*Wiederherstellungskennwort*" können Sie Ihre Mnemonic-Phrase abrufen, wenn Sie eine neue Sicherung erstellen möchten.



![Image](assets/fr/11.webp)



## Versenden von Nachrichten mit Session



Um andere Personen zu kontaktieren, klicken Sie auf die Schaltfläche "*+*" auf der Startseite.



![Image](assets/fr/12.webp)



Es stehen mehrere Optionen zur Verfügung. Wenn Sie eine Gruppe erstellen oder einer Gruppe beitreten möchten, wählen Sie "*Gruppe erstellen*" oder "*Gemeinschaft beitreten*".



![Image](assets/fr/13.webp)



Wenn Sie möchten, dass jemand Sie als Kontakt hinzufügt, können Sie ihn Ihre Sitzungs-ID als QR-Code scannen lassen.



![Image](assets/fr/14.webp)



Um Ihr Login aus der Ferne zu versenden, klicken Sie auf "*Einen Freund einladen*". Sie können dann Ihre Sitzungs-ID kopieren und sie über einen anderen Kommunikationskanal versenden. Sie können diese Informationen auch abrufen, indem Sie auf Ihr Profilfoto auf der Startseite klicken.



![Image](assets/fr/15.webp)



Wenn Sie die Sitzungs-ID einer anderen Person haben und diese hinzufügen möchten, klicken Sie auf "*Neue Nachricht*".



![Image](assets/fr/16.webp)



Sie können die Kennung dann in einen Text einfügen oder sie direkt scannen, wenn Sie sie als QR-Code haben.



![Image](assets/fr/17.webp)



Senden Sie dann eine erste Nachricht an diese Person.



![Image](assets/fr/18.webp)



Sobald die Person Ihre Anfrage akzeptiert, wird ihr Benutzername angezeigt, und Sie können frei mit ihr chatten.



![Image](assets/fr/19.webp)



## Desktop-Software synchronisieren



Um Ihr Konto auf Ihrem Computer zu synchronisieren, müssen Sie die Software installieren. [Laden Sie sie von der offiziellen Website herunter] (https://getsession.org/download). Ich empfehle Ihnen, vor der Installation die Authentizität und Integrität der Software zu überprüfen.



![Image](assets/fr/20.webp)



Beim ersten Start klicken Sie auf "*Ich habe ein Konto*".



![Image](assets/fr/21.webp)



Geben Sie Ihren Mnemonic-Satz ein und achten Sie darauf, zwischen den einzelnen Wörtern ein Leerzeichen zu lassen.



![Image](assets/fr/22.webp)



Sie können nun von Ihrem Computer aus auf Ihre Unterhaltungen zugreifen.



![Image](assets/fr/23.webp)



Herzlichen Glückwunsch, Sie haben jetzt den Dreh raus, wie man Session Messaging benutzt, eine hervorragende Alternative zu WathsApp!



Ich empfehle auch dieses andere Tutorial, in dem ich Threema vorstelle, eine weitere interessante Alternative für Ihre Messaging-Anwendung:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74