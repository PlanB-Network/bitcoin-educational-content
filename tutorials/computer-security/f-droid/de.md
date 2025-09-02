---
name: F-Cold
description: Der Katalog der freien und Open-Source-Anwendungen.
---

![cover](assets/cover.webp)



Im digitalen Zeitalter arbeiten große Unternehmen und Institutionen daran, das Internet stärker zu zentralisieren, seine Kontrolle in ihre eigenen Hände zu legen und damit die Privatsphäre und Freiheit aller Nutzer zu behindern. Das ist keine Utopie, sondern findet bereits statt. Als Bitcoiner sind Dezentralisierung, Respekt für die Privatsphäre und individuelle Freiheiten Prinzipien, die Ihnen wichtig sind, insbesondere bei den Tools, die Sie täglich benutzen. Im Gegensatz zu iOS erlaubt Android seit Jahren die Koexistenz mehrerer App-Stores innerhalb seines Ökosystems, was Ihnen die Freiheit gibt, Apps aus Ihren bevorzugten Quellen zu finden und zu installieren.



In diesem Tutorial werfen wir einen Blick auf F-droid, ein Anwendungsverzeichnis, das eine Alternative zu Anwendungsstores wie dem Google Play Store und dem Microsoft Store darstellt.



## Erste Schritte mit F-Droid



F-Droid ist ein Anwendungs- und Toolstore, mit dem Sie kostenlose Open-Source-Anwendungen auf der Android-Plattform installieren können. F-Droid selbst ist ein Open-Source-Projekt, das 2010 von Ciaran Gultnieks und einigen anderen Mitwirkenden gestartet wurde. Das Hauptziel des Projekts ist es, Open-Source-Anwendungen zugänglich zu machen und Initiatoren von Open-Source-Projekten eine Plattform zu bieten, auf der sie ihre Tools veröffentlichen können, ohne auf den Google Play Store zurückgreifen zu müssen.



Leider ist F-Droid keine Anwendung, die für iOS verfügbar ist, und enthält viele Tools, die für Android-Systeme entwickelt wurden.



Sie können F-droid von [der offiziellen Website] (https://f-droid.org/) im APK-Format herunterladen und manuell auf Ihrem Android-Handy installieren.



![download](assets/fr/02.webp)



Stellen Sie unter Android sicher, dass Sie die Installationsrechte für den Browser gewähren, von dem Sie F-Droid heruntergeladen haben.



Nach Abschluss der Installation startet F-Droid eine Aktualisierung der Open-Source-Anwendungsverzeichnisse, um die Anwendungen im Store zu erweitern.



![repositories](assets/fr/03.webp)



Sie können jetzt Anwendungen auf Ihrem Telefon installieren, ohne den Google Play Store zu besuchen.



## Die F-Droid-Buchhandlung



Im Application Store finden Sie verschiedene Kategorien von Anwendungen, die Ihren Bedürfnissen entsprechen. Auf der Registerkarte **Kategorien** finden Sie über 20 Anwendungstypen, von Browsern bis hin zu kostenlosen Texteditoren, die alle nur wenige Informationen von Ihnen erfordern.



Möchten Sie eine bestimmte Anwendung installieren? Klicken Sie auf die Schaltfläche **Suchen** und geben Sie dann den Namen der gesuchten Anwendung ein.



![search](assets/fr/04.webp)



F-Droid bietet umfassende Informationen zu jeder Anwendung, die Sie installieren möchten.



Wenn Sie auf die Anwendung klicken, finden Sie u.a.:




- Neue Funktionen und Änderungen in der letzten verfügbaren Version
- Eine detaillierte Beschreibung der Anwendung, ihrer Funktionen, der Gründe für ihre Verwendung und der Open-Source-Gemeinschaft, die hinter dem Projekt steht.



![features](assets/fr/05.webp)





- Die vom Projekt verwendete Lizenz, Links zum Quellcode und zu Problemen, die bei der Nutzung der Anwendung aufgetreten sind
- Für die Anwendung erforderliche Genehmigungen



![permissions](assets/fr/06.webp)



Weitere Informationen finden Sie in unserem Thunderbird-Tutorial:



https://planb.network/tutorials/computer-security/communication/thunderbird-91d02325-0361-4641-b152-8975890284a8

F-Droid gibt Ihnen alle Informationen, die Sie benötigen, um zu entscheiden, ob die Verwendung einer Anwendung Ihre Daten schützt und Ihre Privatsphäre verbessert. Scannen Sie alle Anwendungen, die Sie verwenden möchten, und klicken Sie dann auf die Schaltfläche **Installieren**, um Ihre Anwendung herunterzuladen und zu installieren.


Erteilen Sie F-Droid Installationsrechte, indem Sie die Option in Ihren Einstellungen aktivieren.



![settings](assets/fr/07.webp)



## Exchange Ihre Anwendungen



F-Droid fördert die Praxis von Open Source und Community-Beiträgen, insbesondere durch die Option **Near By** Exchange. Verbinden Sie sich mit den Nutzern um Sie herum über:




- Bluetooth-Erkennung;
- Das gleiche Wi-Fi-Netzwerk;
- QR-Code oder IP:PORT Address in Ihrem Browser eingeben.



Mit dieser Option können Sie auf Ihrem Android-Telefon installierte Anwendungen in wenigen Schritten mit Freunden und Familie teilen und empfangen.



![swap](assets/fr/08.webp)



## Aktualisierungen



Lesen Sie auf der Registerkarte **Aktualisierung** die Liste der verfügbaren Aktualisierungen und vergewissern Sie sich, dass Sie auch die Informationen über neue Versionen der einzelnen Anwendungen lesen, um sich über alle wichtigen Änderungen der von Ihnen verwendeten Version zu informieren.



![updates](assets/fr/09.webp)



Sie können die Liste der verfügbaren Anwendungen auch aktualisieren, indem Sie die Seite aktualisieren (nach unten scrollen).



## Fügen Sie Ihre eigenen Anwendungen hinzu



F-Droid ist ein Open-Source-Projekt, das zu Beiträgen zu Anwendungen ermutigt, die die Privatsphäre der Nutzer in den Vordergrund stellen. Sie können Ihre eigene Android-Mobilanwendung durch Beiträge zum F-Droid GitLab-Quellcode in den Store aufnehmen.



Ihre Anwendung muss quelloffen sein, d. h. der Quellcode muss öffentlich zugänglich sein, z. B. auf GitHub oder GitLab.


Sie müssen dann eine YAML-Datei (die Metadaten) erstellen, die Ihre Anwendung beschreibt, einschließlich aller Informationen und Berechtigungen, die für ihre Nutzung erforderlich sind, und dabei der von F-Droid vorgeschlagenen [Metadaten-Vorlage] (https://f-droid.org/docs/Build_Metadata_Reference/) folgen.



Im Abschnitt **Entwickler** der [Dokumentation] (https://f-droid.org/en/docs/) finden Sie alle Ressourcen, die Sie benötigen, um Ihre Anwendungen auf F-Droid zu veröffentlichen und zu pflegen.



### Integrität und Sicherheit



Die Veröffentlichung einer Anwendung als Open Source ist oft gleichbedeutend mit erhöhter Sicherheit, aber auch mit einem erheblichen Risiko. Wie können Sie sicherstellen, dass der Quellcode einer auf F-Droid verfügbaren Anwendung nicht bösartig verändert wird?



F-Droid kompiliert Anwendungen auf seinen eigenen Servern auf der Grundlage des offiziellen Quellcodes und der Kompilierungsanweisungen. Jede veröffentlichte Anwendung wird neu erstellt und überprüft, um sicherzustellen, dass sie nicht kompromittiert wurde. Auf diese Weise wird sichergestellt, dass die angebotene APK dem von den Entwicklern veröffentlichten Quellcode treu bleibt. Darüber hinaus wird jede über F-Droid installierte Anwendung digital signiert und der Signatur-Fingerabdruck mit dem von den Entwicklern der Anwendung auf der offiziellen Website oder im Git-Repository veröffentlichten verglichen.



Wenn Ihnen dieses Tutorial gefallen hat, erfahren Sie mehr über unseren Kurs IT-Sicherheit und Datenmanagement:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1