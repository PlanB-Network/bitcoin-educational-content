---
name: Tox
description: Eröffnen Sie Gespräche ohne Vermittler über das dezentrale Tox-Protokoll
---
![cover](assets/cover.webp)



Die Ende-zu-Ende-Verschlüsselung ist ein Dienst, der von vielen Messaging-Apps wie WhatsApp und Telegram angeboten wird. Verschlüsselung bedeutet hier, dass die Nachricht, bevor sie vom Absender gesendet wird, durch ein kryptografisches Schloss gesichert wird, zu dem nur der Empfänger den Schlüssel hat. Heute wollen wir eine völlig dezentralisierte, Ende-zu-Ende-verschlüsselte Messaging-Anwendung entdecken, die auf ähnlichen Prinzipien wie Blockchain basiert und eine sichere, Ende-zu-Ende-verschlüsselte Kommunikation ohne Vermittler bietet: Tox Chat.



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
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Ende-zu-Ende-Verschlüsselung*



## Was ist Tox?



Tox ist ein kostenloses (quelloffenes), dezentralisiertes Kommunikationsprotokoll, das die *Networking and Cryptography Library* (NaCl)-Technologie sowie Kombinationen von Verschlüsselungsalgorithmen verwendet, um die Sicherheit und Vertraulichkeit seiner Nutzer zu gewährleisten. Mit Tox können Sie Exchange-Textnachrichten versenden, Audio- und Videoanrufe tätigen, Dateien austauschen und Ihren Bildschirm mit Freunden teilen - sicher, dezentral und ohne Vermittler.



Die Technologie, die das Tox-Protokoll verwendet, ähnelt Peer-to-Peer-Netzwerken wie Blockchains, was die Dezentralisierung der Infrastruktur des Protokolls begünstigt. Im Gegensatz zu sozialen Netzwerken und verschlüsselten End-to-End-Nachrichtenanwendungen basiert die Tox-Chat-Anwendung auf einem dezentralen Protokoll, das keinen zentralen Server hat. Alle Benutzer kommunizieren in einem vermittlungsfreien, zensurresistenten Peer-to-Peer-Netzwerk. Um zu kommunizieren, wird jeder Benutzer durch eine eindeutige ID (ToxID) identifiziert, die von seinem öffentlichen Schlüssel abgeleitet ist, der in einer verteilten Hash-Tabelle gespeichert ist.



## Tox verbinden



Sie können das Tox-Protokoll über einen Instant-Messaging-Client verwenden, den Sie von der [Tox-Chat-Website] (https://tox.chat) herunterladen können.



![download](assets/fr/01.webp)



Abhängig von Ihrem Betriebssystem können Sie einen Tox-Client herunterladen und installieren, der mit:





- aTox: [aTox](https://github.com/evilcorpltd/aTox), ein in Kotlin geschriebener Tox-Client, der nur auf Android verfügbar ist



![aTox](assets/fr/02.webp)





- qTox: Ein Tox-Client von [open source](https://github.com/TokTok/qTox), basierend auf dem Qt Framework (C++), verfügbar für Windows, Linux, MacOs.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic](https://github.com/JFreegman/toxic) ist ein in C geschriebener Tox-Client, der auf Systemen mit Befehlszeilenschnittstellen läuft.



![Toxic](assets/fr/04.webp)



In diesem Tutorial werden wir qTox-Clients unter Windows und aTox zur Kommunikation verwenden.



## Erste Schritte mit qTox



Nach dem Download installieren Sie Ihren Tox-Client und erstellen Ihr Profil.



![qTox-acount](assets/fr/05.webp)



Herzlichen Glückwunsch, Sie haben sich soeben dem Tox-Protokoll angeschlossen. In der qTox-Software finden Sie Ihre Profilinformationen, indem Sie auf Ihren Benutzernamen klicken.



![profil](assets/fr/06.webp)



Dort finden Sie insbesondere Ihre Tox-ID, die Sie als QR-Code speichern und an Personen weitergeben können, die mit Ihnen in Kontakt treten möchten.



Exportieren Sie Ihre Tox-Profildatei, damit Sie eine Sicherungskopie Ihres Profils und Ihrer Kontaktinformationen haben, die Sie zur Wiederherstellung verwenden können. Klicken Sie auf die Schaltfläche **Exportieren** und wählen Sie dann den Pfad zu Ihrer Sicherungsdatei.



![export](assets/fr/07.webp)



Über das Menü **Mehr** können Sie Freunde hinzufügen, Kontakte importieren und die Freundschaftsanfragen verwalten, die Sie erhalten.



![friends](assets/fr/08.webp)



Sie können mich zum Beispiel über diese Tox-ID erreichen: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



Sobald die Freundschaftsanfrage gesendet wurde, muss der Empfänger Ihre Anfrage annehmen oder ablehnen, bevor Sie ihn kontaktieren können.



![request](assets/fr/09.webp)



Ihr Tox-Client enthält alle Optionen, die Instant-Messaging-Anwendungen bieten:





- Videoanrufe





- Sprachanrufe





- Gemeinsame Nutzung von Dateien





- emojis



![chat](assets/fr/10.webp)



### Peer-to-Peer-Gruppen



Mit Ihren Tox-Clients können Sie auch völlig dezentral mit einer Gruppe von Personen kommunizieren: Diese Konferenzen werden als solche bezeichnet. Erstellen Sie im Menü **Gruppen** eine neue Konferenz oder konsultieren Sie die Liste der Einladungen zur Teilnahme an Konferenzen, die Sie erhalten haben.



![conferences](assets/fr/11.webp)



Sobald die Konferenz erstellt wurde, können Sie Ihre Freunde über Ihren Tox-Client zur Teilnahme an der Konferenz einladen. Klicken Sie in der Liste Ihrer Freunde mit der rechten Maustaste auf den Benutzernamen des Freundes, den Sie einladen möchten. Klicken Sie auf die Option **Zur Konferenz einladen**, und wählen Sie dann den von Ihnen erstellten Konferenznamen aus. Sie können einen Freund auch einladen, indem Sie mit der Option **Eine neue Konferenz erstellen** implizit eine Konferenz erstellen.



⚠️ Tox-Clients befinden sich noch in der Entwicklung, daher können bei der Interaktion mit der Software Fehler auftreten. Die Funktionen für Konferenzen und Videogespräche sind auf dem Tox Android-Client (aTox) noch nicht verfügbar.



![invite](assets/fr/12.webp)



### Dateiübertragungen



Im Menü **Dateitransfers** finden Sie eine Übersicht über die Dateien, die Sie gesendet und von Ihren Kontakten erhalten haben.



![files](assets/fr/13.webp)



Sie können auch die Konfigurationen für die Dateifreigabe für jede Diskussion, die Sie führen, anpassen. Klicken Sie mit der rechten Maustaste auf den Benutzernamen Ihres Empfängers und wählen Sie "Weitere Details anzeigen".



![details](assets/fr/14.webp)



In den Interface-Details können Sie die Berechtigungen verwalten, die Sie Ihrem Empfänger für:





- Automatische Annahme von Konferenzeinladungen.





- Automatische Dateiannahme.





- Sicherungspfade für Ihre Diskussionsdateien.



![permissions](assets/fr/15.webp)



### Weitere Parameter



Im Menü **Einstellungen** können Sie die Einstellungen für Ihren Tox-Client anpassen.





- Im Abschnitt **Allgemein** ändern Sie die Basissprache Ihres Tox-Clients, definieren die Pfade für die Dateisicherung und die maximale Dateigröße, die automatisch akzeptiert werden soll.



![general](assets/fr/16.webp)





- Im Abschnitt **Interface-Benutzer** können Sie die Schriftarten und -größen Ihrer Nachrichten ändern. Sie können auch das Thema Ihres Tox-Clients ändern.



![ui](assets/fr/17.webp)





- Auf der Registerkarte **Datenschutz** können Sie flüchtige Nachrichten festlegen, indem Sie das Kontrollkästchen "Chatverlauf behalten" deaktivieren. Sie können auch Ihren Nospam-Code ändern, wenn Sie feststellen, dass Sie mit Freundschaftsanfragen zugemüllt werden, indem Sie auf die Schaltfläche "generate zufälliger NoSpam-Code" klicken.



![privacy](assets/fr/18.webp)



### Was garantiert die Vertraulichkeit von Tox?



Das Tox-Protokoll verwendet die Distributed Hash Table, um ein Netz dezentraler Knoten zu schaffen. Jeder Tox-Client ist Teil des DHT-Netzwerks und speichert Informationen über andere Knoten. Im Falle von Tox speichert die DHT IP-Adressen als Werte, die mit öffentlichen Tox-Schlüsseln (Tox-ID) verbunden sind. Dies erleichtert die Suche nach einem Tox-Client-Gerät, ohne einen zentralen Server abfragen zu müssen.



Stellen Sie sich vor, Sie schreiben an unseren Benutzer "EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F", den wir **Benutzer B** nennen. Ihr Tox-Client findet diese Kennung in der Hash-Verteilungstabelle und ruft die zugehörige IP Address ab. Sobald die IP Address gefunden wurde, baut Ihr Tox-Client einen direkten, verschlüsselten Kommunikationskanal mit dem Rechner von **Benutzer B** auf oder verwendet andere Knoten als Relais, um **Benutzer B** zu erreichen. Verschlüsselungsalgorithmen stellen sicher, dass unabhängig vom Kommunikationskanal nur **Benutzer B** den Inhalt Ihrer Nachricht lesen kann.



Wenn Ihnen die Entdeckung von Tox gefallen hat und Sie verstehen konnten, wie Sie damit Ihre Privatsphäre schützen können, geben Sie diesem Tutorial bitte ein "Daumen hoch". Wir empfehlen auch unser Tutorial über Simple Login, ein Tool, mit dem Sie anonym E-Mails empfangen und versenden können.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41