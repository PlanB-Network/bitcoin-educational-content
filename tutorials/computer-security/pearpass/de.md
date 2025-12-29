---
name: PearPass
description: Gewinnen Sie die Kontrolle über Ihre Passwörter mit einem lokalen, Peer-to-Peer- und Cloud-freien Passwortmanager zurück
---

![cover](assets/cover.webp)



In einer Zeit, in der jeder Einzelne Dutzende, ja Hunderte von Online-Konten verwaltet, ist die Sicherheit von Logins zu einem zentralen Thema der IT-Sicherheit geworden. Soziale Netzwerke, Nachrichtensysteme, professionelle Dienste, Finanzplattformen: Jeder dieser Zugänge beruht auf einem Geheimnis, dessen Preisgabe schwerwiegende Folgen für Ihr Leben haben kann.



Doch trotz der wachsenden Zahl von Angriffen sind schlechte Praktiken in der Bevölkerung nach wie vor weit verbreitet: schwache Passwörter, wiederverwendete Passwörter, im Klartext gespeicherte Passwörter oder etwa auswendig gelernte Passwörter. Um diese Probleme zu lösen, ohne das tägliche Leben komplizierter zu machen, besteht die Lösung in der Verwendung eines Passwortmanagers.



Es gibt bereits Dutzende von Passwortmanagern, und Plan ₿ Academy bietet für die meisten von ihnen eine Anleitung. In diesem Tutorial möchte ich Ihnen jedoch einen vorstellen, der sich in Bezug auf seine Funktionsweise deutlich von den anderen abhebt: **PearPass**.



**PearPass ist ein quelloffener, lokaler Peer-to-Peer-Passwortmanager, der den Benutzern die vollständige Kontrolle über ihre Daten gibt



![Image](assets/fr/01.webp)



## Warum PearPass wählen?



Ein Passwort-Manager ist eine Software, die alle Ihre Passwörter generiert, speichert und auf sichere Art und Weise organisiert. Anstatt sich Passwörter zu merken oder wiederzuverwenden, müssen Sie nur ein einziges Geheimnis schützen: das Master-Passwort, das Ihren gesamten Safe verschlüsselt. Dieser Ansatz ermöglicht die Verwendung eindeutiger, langer, zufälliger Passwörter für jeden Dienst, wodurch das Risiko des Vergessens und der Kompromittierung verringert und gleichzeitig die Auswirkungen eines möglichen Lecks begrenzt werden. Heute ist es ein grundlegendes IT-Tool, das jeder verwenden sollte.



Es gibt zwei Hauptkategorien von Passwortmanagern. Auf der einen Seite gibt es Software, die nur lokal genutzt wird. Diese ist sehr sicher, da die Daten nie auf einem zentralen Server gespeichert werden, aber nicht sehr praktisch, da Sie Ihre Anmeldedaten nicht einfach zwischen verschiedenen Geräten (Computer, Smartphone, Tablet...) synchronisieren können. Cloud-basierte Passwort-Manager hingegen speichern Ihre Anmeldedaten auf ihren Servern und synchronisieren sie mit allen Ihren Geräten. Ihr Hauptvorteil ist die Bequemlichkeit, aber sie bedeuten einen Kompromiss bei der Sicherheit, da Ihre Passwörter auf Infrastrukturen gespeichert werden, über die Sie keine Kontrolle haben.



PearPass bricht absichtlich mit beiden Modellen. Es positioniert sich zwischen lokalen Managern und Cloud-Lösungen: Es ermöglicht die Synchronisierung Ihrer Passwörter, während es garantiert, dass diese niemals auf entfernten Servern gespeichert werden. Infolgedessen werden alle Ihre Anmeldeinformationen lokal auf Ihren Geräten gespeichert, und die Synchronisierung zwischen mehreren Rechnern erfolgt ausschließlich über Peer-to-Peer. Diese Architektur eliminiert die mit zentralisierten Datenbanken verbundenen Schwachstellen: Es gibt keine Server, die kompromittiert werden könnten, und keine Infrastruktur von Dritten, die auf Ihre Anmeldedaten zugreifen könnte. Die Kommunikation zwischen Ihren Geräten ist Ende-zu-Ende verschlüsselt, so dass nur die Schlüssel, die Sie besitzen, den Zugriff auf die Daten ermöglichen.



![Image](assets/fr/02.webp)



Um dies zu ermöglichen, stützt sich PearPass, wie der Name schon sagt, auf **Pears**, ein Peer-to-Peer-Technologie-Ökosystem, das auf die Erstellung und Ausführung von serverlosen Anwendungen ausgerichtet ist. Pears stellt die Ausführungsumgebung, die Verteilungsmechanismen und die Netzwerkschichten bereit, die für die Ausführung vollständig dezentralisierter Anwendungen erforderlich sind, die in der Lage sind, sich direkt zwischen Peers zu synchronisieren, ohne dass eine zentrale Infrastruktur erforderlich ist. Im Fall von PearPass sorgt Pears für die Geräteerkennung, den verschlüsselten Verbindungsaufbau und die Synchronisierung des Passwort-Tresors zwischen Ihren Rechnern. Dieser Ansatz stellt sicher, dass PearPass funktionsfähig, widerstandsfähig und unabhängig von einer externen Behörde bleibt.



https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Abgesehen von dieser innovativen Architektur ist PearPass vollständig quelloffen, und alle Funktionen sind kostenlos. Die Software wurde außerdem von Secfault Security unabhängig geprüft. Neben seiner besonderen Architektur bietet PearPass natürlich alle klassischen Funktionen, die man von einem guten Passwort-Manager erwartet, die wir im Laufe dieses Tutorials entdecken werden.



Kurz gesagt, wo herkömmliche Passwortmanager Sie auffordern, einem Unternehmen und seinen Servern zu vertrauen, verfolgt PearPass eine Logik der Souveränität: keine Cloud, keine zentralisierten Konten, keine Vermittler. Sie behalten die alleinige Kontrolle über Ihre Anmeldedaten und profitieren gleichzeitig von der Synchronisierung zwischen Ihren Geräten.



## Wie kann ich PearPass installieren?



PearPass ist auf allen Plattformen verfügbar: Windows, Linux, macOS, Android, iOS und Browser-Erweiterungen. Es besteht keine Notwendigkeit, Pears auf Ihrem Rechner zu installieren: PearPass funktioniert eigenständig.



### Installation unter Windows



Unter Windows wird PearPass als klassisches Installationsprogramm geliefert. Gehen Sie auf [die offizielle Download-Seite] (https://pass.pears.com/download), und klicken Sie dann auf die Schaltfläche "Windows-Installationsprogramm herunterladen".



Sobald die Datei heruntergeladen ist, öffnen Sie das Installationsprogramm und folgen Sie den Anweisungen des Assistenten. Die Anwendung kann dann über das "Startmenü" oder über eine Verknüpfung auf dem Desktop aufgerufen werden.



![Image](assets/fr/03.webp)



### Installation unter macOS



Unter macOS wird PearPass als Disk-Image (`.dmg`) verteilt. Gehen Sie auf [die offizielle Download-Seite] (https://pass.pears.com/download) und wählen Sie die Version, die der Architektur Ihres Macs entspricht (Intel oder Apple Silicon). Nach dem Herunterladen öffnen Sie die `.dmg`-Datei und starten Sie die Anwendung aus dem Ordner `Applications`.



Beim ersten Start zeigt macOS eine Sicherheitsmeldung an, die darauf hinweist, dass das Programm aus dem Internet kommt: Bestätigen Sie einfach, um fortzufahren.



### Installation unter Linux



Unter Linux ist PearPass im `.AppImage'-Format verfügbar, das eine breite Kompatibilität mit den meisten Distributionen ohne spezielle Abhängigkeiten garantiert. Laden Sie die "AppImage"-Datei von [der offiziellen Download-Seite] (https://pass.pears.com/download) herunter und starten Sie sie dann direkt durch Doppelklick.



Je nach Ihrer Umgebung müssen Sie die Datei möglicherweise über die Dateieigenschaften (Rechtsklick) oder mit dem Befehl "chmod +x" ausführbar machen. Sobald PearPass autorisiert ist, wird es als eigenständige Anwendung gestartet.



### Installation der Browser-Erweiterung



PearPass bietet eine Browser-Erweiterung für die automatische Anmeldung und den schnellen Zugriff auf Ihren Safe beim Surfen im Internet. Die Erweiterung ist derzeit für Google Chrome und kompatible Browser verfügbar. Um sie zu installieren, gehen Sie auf [die offizielle Download-Seite] (https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/04.webp)



Sobald sie hinzugefügt wurde, können Sie sie für einen schnellen Zugriff an die Symbolleiste anheften. Um die Erweiterung zu aktivieren, ist eine Verknüpfung mit der lokal auf Ihrem Computer installierten PearPass-Anwendung erforderlich (wir kommen später im Lernprogramm darauf zurück).



### Installation auf iOS und Android



Auf iPhone und Android laden Sie die Anwendung einfach aus Ihrem App Store herunter:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store] (https://apps.apple.com/us/app/pearpass/id6752954830).



![Image](assets/fr/05.webp)



Zusätzlich zu diesen klassischen Installationsmethoden ist es auch möglich, die Software direkt von den GitHub-Repositories herunterzuladen, für jede :




- [Desktop] (https://github.com/tetherto/pearpass-app-desktop);
- [Mobil] (https://github.com/tetherto/pearpass-app-mobile);
- [Browser-Erweiterung] (https://github.com/tetherto/pearpass-app-browser-extension).



Sobald PearPass auf einer oder mehreren Plattformen installiert ist, können Sie mit der Erstkonfiguration fortfahren. In diesem Tutorial beginnen wir mit der Konfiguration der Software auf dem Desktop und synchronisieren sie dann mit der Browser-Erweiterung und der mobilen Anwendung.



## Wie kann ich einen PearPass-Safe erstellen?



Wenn Sie PearPass zum ersten Mal auf Ihrem Computer starten, führt Sie die Anwendung durch zwei Schritte: das Festlegen Ihres Master-Passworts und das Erstellen Ihres ersten Safes.



### Master-Passwort festlegen



Wenn die Anwendung zum ersten Mal auf dem Desktop gestartet wird, klicken Sie auf die Schaltfläche "Überspringen" und dann auf "Fortfahren", um den Einführungsbildschirm zu durchlaufen und zur Konfiguration des Hauptkennworts zu gelangen.



![Image](assets/fr/06.webp)



Als Nächstes folgt der wichtige Schritt der Wahl Ihres Hauptkennworts. Wie wir in der Einleitung gesehen haben, ist dieses Passwort sehr wichtig, da es Ihnen Zugang zu allen anderen im Manager gespeicherten Passwörtern gibt. Technisch gesehen wird es verwendet, um die kryptografischen Schlüssel abzuleiten, mit denen Ihre Daten verschlüsselt werden.



Das Master-Kennwort birgt zwei Hauptrisiken: Verlust und Kompromittierung. Wenn Sie den Zugang zu diesem Passwort verlieren, können Sie nicht mehr auf Ihre Anmeldedaten zugreifen. PearPass speichert niemals Ihr Master-Passwort: **Wenn es verloren geht, sind Ihre Anmeldedaten dauerhaft verloren**. Es gibt keinen Wiederherstellungsmechanismus. Umgekehrt, wenn dieses Passwort kompromittiert wird und ein Angreifer Zugang zu einem Ihrer Geräte erhält, kann er oder sie auf alle Ihre Konten zugreifen.



Um das Verlustrisiko zu begrenzen, können Sie eine physische Sicherungskopie Ihres Master-Passworts anfertigen, z. B. auf Papier, und diese an einem sicheren Ort aufbewahren. Idealerweise versiegeln Sie diese Sicherungskopie in einem Umschlag, so dass Sie regelmäßig überprüfen können, dass kein Zugriff erfolgt ist. Erstellen Sie jedoch niemals eine digitale Sicherungskopie des Passworts.



Um das Risiko einer Kompromittierung zu verringern, muss Ihr Hauptpasswort sicher sein. Es sollte so lang wie möglich sein, eine Vielzahl von Zeichen enthalten und wirklich zufällig gewählt werden. Für das Jahr 2025 werden mindestens 13 Zeichen empfohlen, darunter Groß- und Kleinbuchstaben, Zahlen und Symbole, vorausgesetzt, das Passwort ist zufällig. Ich würde jedoch ein Passwort von mindestens 20 Zeichen, wenn nicht mehr, mit allen Arten von Zeichen empfehlen, um eine dauerhafte Sicherheit zu gewährleisten.



Geben Sie Ihr Master-Passwort in das vorgesehene Feld ein, bestätigen Sie es ein zweites Mal und klicken Sie dann auf die Schaltfläche "Weiter".



![Image](assets/fr/07.webp)



Sie werden dann zum Anmeldebildschirm weitergeleitet: Geben Sie Ihr Master-Passwort ein, um zu überprüfen, ob alles richtig funktioniert.



![Image](assets/fr/08.webp)



### Erstellen Sie Ihren ersten Safe



Sobald Sie sich angemeldet haben, fordert PearPass Sie auf, Ihren ersten Safe zu erstellen. Ein Safe ist ein verschlüsselter Behälter, in dem Ihre Passwörter, IDs, sichere Notizen und andere Informationen gespeichert werden. Jeder Safe ist isoliert und kann durch einen eindeutigen Namen identifiziert werden, so dass Sie Ihre Daten je nach Verwendungszweck organisieren können (persönlich, beruflich, bestimmte Projekte...).



Klicken Sie auf die Schaltfläche "Einen neuen Tresor erstellen".



![Image](assets/fr/09.webp)



Wählen Sie einen Namen für diesen Tresor und klicken Sie dann erneut auf "Neuen Tresor erstellen", um die Erstellung abzuschließen.



![Image](assets/fr/10.webp)



Ihr Safe ist sofort einsatzbereit. Sie können sofort mit dem Hinzufügen von Passwörtern, Logins oder sicheren Notizen beginnen.



![Image](assets/fr/11.webp)



## Wie füge ich ein Login zu PearPass hinzu?



Sobald Sie Ihren Safe erstellt haben, können Sie damit beginnen, Ihre Gegenstände darin zu speichern. PearPass unterstützt die Registrierung von vielen Arten von Gegenständen:




- anmeldung bei einer Website oder einem Dienst ;
- identität: Ihre persönlichen Daten zum schnellen Ausfüllen von Formularen, aber auch zum Speichern von Ausweisdokumenten direkt in PearPass ;
- kreditkarte: Ihre Kreditkartennummern für eine schnellere Bezahlung beim Online-Einkauf;
- Wi-Fi: Passwörter für Ihre Wi-Fi-Netzwerke ;
- PassPhrase: geheime Phrase, die aus mehreren Wörtern zusammengesetzt ist (Warnung: Ich rate dringend davon ab, sie für wallet Bitcoin mnemonische Phrasen zu verwenden);
- hinweis: Erstellen sicherer Notizen ;
- benutzerdefiniert: Mit dieser Funktion können Sie einen benutzerdefinierten Elementtyp erstellen, der an Ihre spezifischen Bedürfnisse angepasst ist.



Öffnen Sie zunächst PearPass und melden Sie sich mit Ihrem Master-Passwort an.



![Image](assets/fr/12.webp)



Wählen Sie den Tresor aus, in dem Sie diese Kennung speichern möchten.



![Image](assets/fr/13.webp)



Klicken Sie auf der Startseite auf die Schaltfläche, um ein neues Element hinzuzufügen, je nachdem, welche Art von Informationen Sie erfassen möchten. In meinem Fall möchte ich ein Login für mein Konto auf der Plan ₿ Academy-Website hinzufügen: Ich klicke also auf die Schaltfläche "Login erstellen".



![Image](assets/fr/14.webp)



Sobald Sie die Art des Elements, das Sie hinzufügen möchten, ausgewählt haben, erscheint ein Formular, in das Sie die mit dem betreffenden Dienst verbundenen Informationen eingeben können. Je nach Bedarf können Sie den Namen des Dienstes, das Login, das Passwort und, falls erforderlich, die Adresse der Website und zusätzliche Hinweise eingeben.



PearPass verfügt auch über einen Passwortgenerator, mit dem Sie direkt aus dem Formular heraus ein sicheres Passwort erstellen können. Um ihn zu verwenden, klicken Sie auf das Symbol, das drei kleine Punkte im Feld "Passwort" darstellt, wählen Sie die gewünschte Länge und klicken Sie dann auf "Passwort einfügen".



Wenn Sie alle Felder ausgefüllt haben, klicken Sie auf die Schaltfläche "Speichern", um die Kennung im Safe zu speichern.



![Image](assets/fr/15.webp)



Die Kennung ist nun gespeichert. Er erscheint in der Liste der Objekte im ausgewählten Safe und kann durch Anklicken angezeigt werden.



![Image](assets/fr/16.webp)



Sie können ein Element ganz einfach ändern, indem Sie es anklicken und dann auf die Schaltfläche "Bearbeiten" klicken. Sie können es auch löschen, indem Sie auf die drei kleinen Punkte oben rechts auf der Oberfläche und dann auf "Element löschen" klicken.



![Image](assets/fr/22.webp)



Auf dem Handy bleibt die Logik dieselbe, obwohl die Schnittstelle angepasst wurde. Nach dem Einloggen wählen Sie den gewünschten Tresor aus, tippen auf die Schaltfläche "+", wählen die Art des zu erstellenden Artikels und geben dann die erforderlichen Informationen ein.



![Image](assets/fr/17.webp)



## Wie organisiert man PearPass?



Wie wir in den vorherigen Abschnitten gesehen haben, können Sie mit PearPass mehrere verschiedene Tresore erstellen. Dies ermöglicht die Trennung verschiedener Verwendungen und stellt eine erste Organisationsebene für Ihren Passwortmanager dar. Von der Startseite aus können Sie leicht von einem Tresor zu einem anderen wechseln, indem Sie auf den Pfeil oben links auf der Oberfläche klicken.



![Image](assets/fr/18.webp)



Eine weitere Möglichkeit, Ihre Kennwörter auch innerhalb eines Tresors zu organisieren, ist die Erstellung von Ordnern. Klicken Sie dazu in der linken Spalte der Benutzeroberfläche auf das "+"-Symbol neben "Alle Ordner" und geben Sie dann den Namen des Ordners ein, den Sie erstellen möchten.



![Image](assets/fr/19.webp)



Sie können dann die Bezeichner Ihrer Wahl speichern, entweder direkt beim Anlegen eines Artikels oder später, indem Sie auf "Bearbeiten" klicken. Dazu müssen Sie nur den gewünschten Ordner in der oberen linken Ecke des Formulars auswählen.



![Image](assets/fr/20.webp)



Nach dem Öffnen eines Elements, z. B. einer Anmeldung, können Sie auf das Sternsymbol oben rechts auf der Benutzeroberfläche klicken, um es zu Ihren Favoriten hinzuzufügen. Favoriten können schnell in einem speziellen Ordner gefunden werden, zusätzlich zu ihrem Basisordner.



![Image](assets/fr/21.webp)



Und schließlich gibt es eine Suchleiste am oberen Rand der Benutzeroberfläche, mit der Sie schnell das gesuchte Element finden können, auch wenn Ihr Tresor viele Identifikatoren enthält.



## Wie synchronisiere ich PearPass auf meinem Handy?



Jetzt, wo Sie einen funktionierenden Tresor mit auf Ihrem Computer gespeicherten Elementen haben, möchten Sie wahrscheinlich auch von Ihrem Smartphone oder einem anderen Gerät aus auf Ihre Passwörter zugreifen. Mit PearPass können Sie Ihren Manager auf mehreren Geräten sicher mit Pears synchronisieren. Lassen Sie uns herausfinden, wie.



Melden Sie sich zunächst auf dem Quellcomputer (z. B. Ihrem Computer) mit Ihrem Master-Passwort bei Ihrem Tresor an. Klicken Sie auf der Startseite auf die Schaltfläche "Gerät hinzufügen" unten rechts auf der Benutzeroberfläche.



![Image](assets/fr/23.webp)



PearPass generiert dann einen Einladungslink, der auch als QR-Code verfügbar ist, um den ausgewählten Tresor auf dem Gerät Ihrer Wahl zu synchronisieren.



![Image](assets/fr/24.webp)



Wenn Sie auf Ihrem mobilen Gerät synchronisieren möchten, installieren Sie zunächst die Anwendung und starten Sie sie dann. Sie werden aufgefordert, ein Hauptpasswort für Ihren Mobile Manager zu erstellen. Sie können entweder das gleiche Passwort wie auf Ihrem Computer oder ein anderes verwenden. In jedem Fall sollten Sie die gleichen Empfehlungen befolgen: ein sicheres, zufälliges Passwort, das auf einem physischen Medium gespeichert ist.



![Image](assets/fr/25.webp)



Sie können dann auf Wunsch die biometrische Authentifizierung aktivieren, um zu vermeiden, dass Sie Ihr Hauptpasswort jedes Mal manuell eingeben müssen, wenn Sie Ihr Handy entsperren.



![Image](assets/fr/26.webp)



Geben Sie Ihr Hauptpasswort erneut ein und klicken Sie dann auf die Schaltfläche "Weiter".



![Image](assets/fr/27.webp)



Wählen Sie die Option "Tresor laden", klicken Sie dann auf "QR-Code scannen" und scannen Sie den von PearPass angezeigten Einladungs-QR-Code auf Ihrem Quellrechner (dem Computer).



![Image](assets/fr/28.webp)



Ihre Tresore auf Ihrem Computer und Ihrem Mobiltelefon sind jetzt synchronisiert. Jede auf einem Gerät hinzugefügte ID wird auf dem anderen Gerät sicher gespeichert und repliziert.



![Image](assets/fr/29.webp)



Auf Mobiltelefonen können Sie auch das automatische Ausfüllen von Feldern aktivieren. Gehen Sie dazu zu "Einstellungen > Erweitert" und klicken Sie auf die Schaltfläche "Als Standard festlegen" im Abschnitt "Automatisches Ausfüllen".



![Image](assets/fr/30.webp)



## Wie kann ich PearPass mit der Browsererweiterung synchronisieren?



Ein Passwortmanager, der zwischen Ihrem Computer und Ihrem Smartphone synchronisiert wird, ist bereits sehr praktisch, aber die direkte Integration in Ihren Browser ist noch praktischer. Beginnen Sie dazu mit [Hinzufügen der offiziellen PearPass-Erweiterung zu Ihrem Browser] (https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/31.webp)



Gehen Sie in der PearPass-Software, die auf Ihrem lokalen Rechner installiert ist, zu "Einstellungen > Erweitert" und aktivieren Sie die Option "Browsererweiterung aktivieren".



![Image](assets/fr/32.webp)



PearPass erzeugt eine token-Kopplungsdatei. Kopieren Sie sie.



![Image](assets/fr/33.webp)



Öffnen Sie dann die PearPass-Erweiterung in Ihrem Browser, fügen Sie die token-Kopplung ein, und klicken Sie auf die Schaltfläche "Überprüfen", gefolgt von "Fertigstellen".



![Image](assets/fr/34.webp)



Ihr Passwortmanager ist nun mit der Browsererweiterung synchronisiert.



![Image](assets/fr/35.webp)



Damit können Sie jetzt ganz einfach eine Verbindung zu Ihren verschiedenen Webkonten herstellen.



![Image](assets/fr/36.webp)



Jetzt wissen Sie, wie Sie den PearPass-Passwortmanager verwenden können. Über dieses Tool hinaus hängt die alltägliche digitale Sicherheit von der korrekten Verwendung geeigneter Lösungen ab. Wenn Sie lernen möchten, wie Sie ein sicheres, stabiles und effizientes persönliches digitales Umfeld einrichten können, lade ich Sie ein, unseren Schulungskurs zu diesem Thema zu entdecken:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1