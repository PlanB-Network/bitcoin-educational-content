---
name: Deltaschwätzer
description: Praktischer Leitfaden für ein dezentrales Messaging-Tool
---

![image](assets/cover.webp)




## Einführung - Chat-Kontrolle und Datenschutz



In den letzten Jahren wurde zunehmend über Chat Control gesprochen, einen Regulierungsvorschlag, der darauf abzielt, das automatische Scannen privater Nachrichten auf großen Kommunikationsplattformen einzuführen. Das erklärte Ziel ist die Bekämpfung illegaler Inhalte. Das Problem ist, dass dieser Mechanismus in Wirklichkeit eine Massenüberwachung bedeuten würde, die die Ende-zu-Ende-Verschlüsselung und damit die Privatsphäre aller Nutzer, nicht nur der Straftäter, aushöhlen würde.



Die wirkliche Gefahr besteht darin, dass Chats zu kontrollierten Umgebungen werden, in denen jede Nachricht, jedes Bild und jeder Anhang geprüft werden könnte, bevor sie den Empfänger überhaupt erreichen. Und hier kommt eine mögliche Lösung ins Spiel: weg von zentralisierten Plattformen und hin zu dezentralen Messaging-Systemen, die nicht von einem einzigen Anbieter abhängig sind und nicht so leicht einer solchen Kontrolle unterworfen werden können.



Eine solche Lösung wird in diesem Lernprogramm vorgestellt: Delta Chat. Ein ausgereiftes und bereits brauchbares Tool.




## Warum Delta Chat und wie es funktioniert



Delta Chat ist bereits eine sehr gute Messaging-Lösung für den täglichen Gebrauch: sehr nützlich für Gespräche mit Freunden, Familie und anderen Menschen, wie ein echtes Äquivalent zu WhatsApp.



Es ist ein dezentralisiertes Nachrichtensystem, das vollständig auf E-Mail basiert. Es nutzt im Grunde die Infrastruktur der traditionellen E-Mail, baut aber darauf eine moderne Instant-Messenger-Schnittstelle und -Erfahrung auf. Auf den ersten Blick mag dies ein wenig improvisiert erscheinen, aber es funktioniert tatsächlich sehr gut und ist überraschend robust. Sie können spezielle E-Mail-Server namens ChatMail verwenden, aber es kann auch nahtlos mit normalen E-Mail-Servern zusammenarbeiten. Das bedeutet, dass Sie sich mit einem bestehenden Konto anmelden können, wenn Sie wollen, ohne etwas Neues erstellen zu müssen.



Ein weiteres Highlight ist die Unterstützung für WebXDCs, das sind kleine Webanwendungen, die direkt in Chats verwendet werden können, ähnlich den Mini-Apps in Telegram. Der wichtige Unterschied besteht darin, dass diese Anwendungen keinen Internetzugang haben, so dass sie den Benutzer nicht verfolgen oder Daten nach außen senden können.



Aus der Sicherheitsperspektive verwendet Delta Chat eine geprüfte Ende-zu-Ende-Verschlüsselung, die auf PGP basiert, aber mit modernen Erweiterungen versehen ist, die das Schutzniveau mit Signal vergleichbar machen. Der einzige derzeitige Mangel ist Perfect Forward Secrecy, aber das ist ein sich entwickelnder Aspekt.



Da Delta Chat ausschließlich auf E-Mail basiert, wird dies gänzlich vermieden:




- pflichtrufnummern
- Zentralisierte IDs
- registrierungen in Verbindung mit einer einzigen Dienstleistung



Und genau das macht dieses Tool sehr resistent gegen invasive Regelungen wie Chat Control.




## Einrichtung



Auf der offiziellen Website von [Delta Chat] (https://delta.chat/download) können Sie den Download-Bereich aufrufen. Unter Linux ist es bequem über Flathub verfügbar, aber es gibt auch Pakete für Arch, NixOS, Snap und eigenständige Versionen.



![image](assets/it/01.webp)



Sie ist auch verfügbar für:




- [F-Droid] (https://f-droid.org/app/com.b44t.messenger)
- [Play Store](https://play.google.com/store/apps/details?id=chat.delta)
- [iOS] (https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS] (https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch](https://open-store.io/app/deltatouch.lotharketterer)
- und andere Geschäfte...



Wenn Sie nach einer Anleitung für die Installation von F-Droid suchen, könnte diese Anleitung Ihnen helfen:



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

Eine sehr wichtige Sache: Für die Desktop-Versionen ist kein Telefon erforderlich. Anders als bei WhatsApp oder SimpleX Chat müssen Sie sich nicht erst auf dem Handy registrieren. Sie können Ihr Profil direkt am PC erstellen oder es von einem anderen Gerät übertragen.




## Profil erstellen



Sobald die App geöffnet ist, fragt Delta Chat, ob Sie ein neues Profil erstellen oder ein bestehendes Profil verwenden möchten.



![image](assets/it/02.webp)



Wenn Sie ein neues Profil erstellen, können Sie es eingeben:




- ein Name
- ein Bild (optional)



Ein ChatMail-Server wird standardmäßig vorgeschlagen, aber es ist möglich:




- einen anderen ChatMail-Server wählen
- ein klassisches E-Mail-Konto verwenden
- iMAP und SMTP manuell konfigurieren
- sich mit dem Einladungscode eines anderen Nutzers registrieren



Nach ein paar Sekunden ist das Profil fertig und Sie können die App verwenden.



![image](assets/it/03.webp)




## Interface und Chat



Die Benutzeroberfläche ist sehr einfach und überschaubar:




- Gerätemeldungen, d.h. lokale Kommunikation
- Gespeicherte Nachrichten, ähnlich denen in Telegram und zwischen Geräten synchronisierbar



![image](assets/it/04.webp)



Fügen Sie einfach einen Kontakt hinzu:




- Zeigen Sie Ihren QR-Code
- Scannen Sie die Daten der anderen Person
- Per Link einladen (Einladungslink teilen).



![image](assets/it/05.webp)



Sobald die Verbindung hergestellt ist, wird automatisch eine Ende-zu-Ende-Verschlüsselung konfiguriert. Die Chat-Benutzeroberfläche ist der von WhatsApp sehr ähnlich:




- text- und Sprachnachrichten
- fotos, Videos und Dateien
- antworten auf Nachrichten
- reaktionen
- popup-Meldungen
- anpassbare Benachrichtigungen.



![image](assets/it/06.webp)



## WebXDC: Anwendungen in Chats:



Delta Chat ermöglicht die Verwendung von WebXDC, d. h. von kleinen Anwendungen, die in Unterhaltungen eingebettet sind. Hier ist eine kurze Liste der nützlichsten Anwendungen:




- umfragen
- reißbretter
- temporäre private Chats
- spiele mit gemeinsamen Chat-Ergebnissen



Es können auch komplexere Spiele gestartet werden, was die Flexibilität dieses Tools unterstreicht.



![image](assets/it/07.webp)



## Gruppen, Kanäle und erweiterte Funktionen



Sie können Gruppen erstellen, Sticker verwenden (vor allem auf Desktops) und, wenn Sie die experimentellen Optionen aktivieren, sogar Kanäle, ähnlich denen in Telegram.



In den erweiterten Einstellungen können Sie diese Funktion aktivieren:




- sprachanrufe (noch experimentell)
- erweiterte E-Mail-Profilverwaltung
- vollständige Backups.



![image](assets/it/08.webp)



## Multigeräte und Datensicherung



Delta Chat unterstützt mehrere Geräte vollständig:




- sie können ein zweites Gerät per QR-Code hinzufügen
- können Sie eine vollständige Übertragung per Backup durchführen.



In Sekundenschnelle finden Sie Ihre Chats, Gruppen und den kompletten Verlauf wieder, ohne von einem zentralen Server abhängig zu sein.



![image](assets/it/09.webp)




## Schlussfolgerung



In einer Zeit, in der immer häufiger über die Kontrolle privater Kommunikation gesprochen wird, stellt Delta Chat eine konkrete Antwort dar: dezentralisierte, verschlüsselte Nachrichten, die wirklich jeden Tag nutzbar sind.



Es ist die Lösung, die mich von allen, die ich ausprobiert habe, in Bezug auf Einfachheit, Privatsphäre und Freiheit am meisten überzeugt hat. Wenn Sie möchten, können Sie mich auch im Delta-Chat über den folgenden [Einladungslink](https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats) kontaktieren



Wenn Ihnen dieser Leitfaden gefallen hat, können Sie mich unterstützen, indem Sie spenden und einen Daumen hoch hinterlassen. Und denken Sie daran: Nur wenn Sie Delta Chat sowohl auf dem Handy als auch auf dem Desktop nutzen und erforschen, werden Sie seine volle Funktionalität entdecken.



Bis zum nächsten Mal.