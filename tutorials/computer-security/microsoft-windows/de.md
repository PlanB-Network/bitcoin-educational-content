---
name: Windows 11
description: Automatische Installation von Microsoft Windows 11 über eine Konfigurationsdatei
---
![cover](assets/cover.webp)


In diesem Lernprogramm lernen Sie, wie Sie Windows 11 automatisch installieren können, indem Sie eine andere Methode als die Standard-Windows-Installation verwenden.


## Herunterladen!


Als Erstes benötigen Sie eine Installationsdatei. Am sichersten und zuverlässigsten können Sie diese direkt von der offiziellen Website von Microsoft herunterladen.


Besuchen Sie einfach den unten angegebenen Link und folgen Sie den Anweisungen, um die [Windows 11 ISO-Datei] herunterzuladen (https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


Wenn Sie auf der Download-Seite sind, scrollen Sie nach unten zu dem Abschnitt, in dem Sie die ISO-Datei herunterladen können.


![Image](assets/en/01.webp)


َUnd wählen Sie die richtige Version.


![Image](assets/en/03.webp)


Nachdem Sie Windows 11 ausgewählt haben, klicken Sie auf die Schaltfläche Bestätigen.


Bei diesem Schritt kann es einige Sekunden dauern, bis die Anfrage bearbeitet ist. Danach wird die folgende Seite angezeigt:


![Image](assets/en/04.webp)


Nachdem Sie die Anfrage bestätigt haben, müssen Sie Ihre bevorzugte Sprache auswählen.


![Image](assets/en/05.webp)


Nachdem Sie die Sprache ausgewählt und auf die Schaltfläche Bestätigen geklickt haben, wird die Anfrage bearbeitet. Dieser Schritt kann ein paar Sekunden dauern.


Sobald die Anfrage erfolgreich bearbeitet wurde, wird eine Seite mit dem Download-Link für die .iso-Datei angezeigt. Klicken Sie auf die Schaltfläche 64-Bit-Download, um den Download zu starten.


Die Datei ist etwa 5,5 GB groß, und der erzeugte Link ist 24 Stunden lang gültig.


## Automatisierung!


In diesem Stadium müssen wir Änderungen an der Standard-Windows-Installation vornehmen. In dieser Phase wird mit der unbeaufsichtigten Installation festgelegt, welche Elemente installiert werden sollen, ohne dass der Benutzer nachträglich eingreifen muss. Bei dieser Methode wird nämlich eine XML-Datei verwendet, um die Installationsschritte und die in Windows installierten Dienste zu konfigurieren. Mit anderen Worten: Durch die Verwendung der Datei Unattended.xml wird ein Automatisierungsprozess während der Installation geschaffen, der die Auswahl mehrerer Optionen überflüssig macht und die langwierigen Schritte vermeidet, die normalerweise während der Einrichtung erforderlich sind. Bei dieser Methode handelt es sich um eine ungewöhnliche, aber standardmäßige Methode, die von Microsoft eingeführt wurde. Weitere Informationen finden Sie auf [Microsofts offizieller Website](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11).


Im Internet gibt es verschiedene Tools zur Erstellung unbeaufsichtigter Dateien. Einige davon sind online, während andere offline sind. Eines der Online-Tools zur Erstellung dieser Datei ist [diese Website](https://schneegans.de/windows/unattend-generator). Nach dem Öffnen dieser Website wird die folgende Seite angezeigt:


![Image](assets/en/06.webp)


Wie oben auf der Seite erwähnt, kann diese Methode für die Installation von Windows 10 und 11 verwendet werden. Im ersten Schritt wählen wir die Windows-Sprache aus. Wenn wir eine zweite oder sogar eine dritte Sprache zur Liste der Windows-Anzeige- und Tastatursprachen hinzufügen möchten, können wir das Feld unten verwenden:


![Image](assets/en/07.webp)


Im nächsten Schritt wählen wir den gewünschten Ort aus.


![Image](assets/en/08.webp)


In diesem Stadium können wir auch die Prozessorarchitektur für den Computer festlegen. In diesem Schritt können wir:

1. Entscheiden Sie, ob Sie Windows-Sicherheitsfunktionen wie TPM und Secure Boot ignorieren möchten. Die Secure-Boot-Funktion stellt sicher, dass die Manipulation von Windows-Kerndateien während des Startvorgangs erkannt und ihre Ausführung verhindert wird. Diese Funktion trägt auch dazu bei, das System vor der Installation bösartiger Updates für Windows zu schützen. Die Aktivierung der Option zur Umgehung dieser Funktionen ist auf bestimmten Computern, insbesondere älteren Modellen, manchmal unvermeidlich. Es wird jedoch allgemein empfohlen, Funktionen wie Secure Boot aktiviert zu lassen.

2. Ignorieren Sie die Anforderung einer Internetverbindung, um den Vorgang abzuschließen. Dies ist in Situationen nützlich, in denen keine kabelgebundene LAN-Verbindung verfügbar ist, da in den meisten Fällen die drahtlose Karte während der Windows-Installation noch nicht erkannt wird und ein Internetzugang über Kabel erforderlich ist. Wenn Sie diese Option aktivieren, werden Probleme im Zusammenhang mit diesem Schritt behoben.


Im nächsten Schritt können wir einen Namen für den Computer wählen.


![Image](assets/en/09.webp)


Wir können Windows auch erlauben, einen Namen für das System zu wählen. In diesem Schritt können wir den Windows-Typ auswählen, ob komprimiert oder unkomprimiert, oder Windows die geeignete Version auf der Grundlage der Computerspezifikationen bestimmen lassen. Auch die Zeitzone kann in dieser Phase festgelegt werden.


Der nächste Schritt betrifft die Partitionseinstellungen:


![Image](assets/en/10.webp)


In diesem Stadium können wir den Partitionstyp für die Installation von Windows sowie die erforderlichen Einstellungen für die Installation der Windows-Wiederherstellungsumgebung festlegen. Wenn Sie die erste Option wählen, werden die Auswahl der Partition und die Partitionierung auf den Zeitpunkt der Windows-Installation verschoben, und während des Setups werden diese Fragen genau wie bei der normalen Installationsmethode gestellt.


In diesem Schritt wählen wir die zu installierende Windows-Version aus:


![Image](assets/en/11.webp)


Wenn ein Produktschlüssel vorhanden ist, kann er ebenfalls in diesem Stadium eingegeben werden.


Im nächsten Schritt müssen Sie das Windows-Anmeldekonto konfigurieren:


![Image](assets/en/12.webp)


## Konto-Sitzungen


In diesem Stadium:


1. Wir können einen Namen und ein Passwort für das Administratorkonto festlegen. Es ist auch möglich, mehrere Benutzer- oder Administratorkonten zu erstellen.

2. Hier legen wir fest, welches Konto bei der ersten Anmeldung nach der Windows-Installation verwendet werden soll. Die verschiedenen Optionen für diesen Abschnitt sind in der Abbildung dargestellt.

3. Wenn Sie nicht möchten, dass irgendwelche Konten erstellt werden, löschen Sie alle Konten und wählen Sie diese Option. In diesem Fall werden Sie nach der Windows-Installation automatisch mit dem Windows-Administratorkonto angemeldet.


Der nächste Schritt besteht in der Konfiguration der Passwort- und Hostdateieinstellungen:


![Image](assets/en/13.webp)


In dieser Phase wird festgelegt, ob die Kennwörter eine Ablauffrist haben sollen. Außerdem enthält dieser Abschnitt Sicherheitseinstellungen in Bezug auf fehlgeschlagene Anmeldeversuche, die je nach Bedarf aktiviert oder deaktiviert werden können.


Im unteren Teil dieses Abschnitts finden Sie Einstellungen für die Dateianzeige. Keine dieser Optionen ist bei einer normalen Windows-Installation verfügbar und muss nach der Installation konfiguriert werden. Im Gegensatz dazu sind diese Einstellungen bei der unbeaufsichtigten Installationsmethode leicht zugänglich.


Der nächste Schritt ist die Konfiguration der Windows-Sicherheitseinstellungen:


![Image](assets/en/14.webp)


## Sicherheitseinstellungen


In diesem Stadium:


1. Windows Defender kann aktiviert oder deaktiviert werden. Diese Funktion funktioniert wie eine Sicherheitssoftware in Windows und hilft, die Ausführung bösartiger Dateien, bestimmte Netzwerkangriffe und mehr zu verhindern.

2. Automatische Windows-Updates können deaktiviert werden. Dies ist eine der häufigsten Herausforderungen für Windows-Benutzer!

3. In diesem Abschnitt können Sie die Benutzerkontensteuerung (UAC) aktivieren oder deaktivieren. Diese Funktion verhindert, dass verdächtige Anwendungen mit erhöhten Lese- und Schreibberechtigungen ausgeführt werden.

4. Diese Funktion wird von Windows verwendet, um potenziell schädliche Software zu erkennen.

5. Aktivieren oder deaktivieren Sie die Unterstützung für lange Pfade in Windows-Anwendungen, z. B. in PowerShell und anderen.

6. Aktivieren oder deaktivieren Sie Remote Desktop für den Fernzugriff auf das System.


Je nach verwendeter Windows-Version werden einige dieser Funktionen unterstützt oder nicht.


Der nächste Schritt besteht darin, die Symbole zu konfigurieren:


![Image](assets/en/15.webp)


In diesem Abschnitt:


1. Es werden Desktop-Symbole aufgelistet, die je nach Bedarf hinzugefügt oder entfernt werden können.

2. Es werden Symbole für das Startmenü aufgelistet, die je nach Bedarf hinzugefügt oder entfernt werden können.

3. In diesem Abschnitt können Sie konfigurieren, ob virtualisierungsbezogene Tools installiert werden sollen oder nicht. Diese Option ist spezifisch für Windows 11 und gilt nicht für Windows 10.


Im nächsten Schritt müssen Sie die Wi-Fi-Einstellungen konfigurieren:


![Image](assets/en/16.webp)


In diesem Abschnitt können die Wi-Fi-Netzwerkeinstellungen konfiguriert werden. Wie bereits erwähnt, wird die Wi-Fi-Karte in den meisten Fällen während der Windows-Installation nicht erkannt, so dass eine Verbindung während der Einrichtung normalerweise nicht möglich ist. Durch die Konfiguration dieses Abschnitts kann das System jedoch eine Verbindung mit dem Internet herstellen, wenn die WLAN-Karte erkannt wird.


Der nächste Schritt beinhaltet eine wichtige Einstellung:


![Image](assets/en/17.webp)


In diesem Abschnitt legen wir fest, ob Informationen über Systemprobleme an Microsoft gesendet werden sollen oder nicht.


Der nächste Schritt ist die Konfiguration von Standardanwendungen:


![Image](assets/en/18.webp)


## Standard-Software aktivieren/deaktivieren


In diesem Abschnitt können wir alle Anwendungen auswählen, die nicht standardmäßig installiert werden sollen. Zum Beispiel können wir entscheiden, Cortana oder Copilot nicht zu installieren.


Der nächste Schritt betrifft die Sicherheitseinstellungen in Bezug auf die Anwendungsausführung:


![Image](assets/en/19.webp)


Durch die Anwendung von WDAC-Einstellungen kann die Ausführung bestimmter Anwendungen verhindert werden.


Nachdem Sie die gewünschten Einstellungen vorgenommen haben, können Sie die generierte XML-Datei herunterladen:


![Image](assets/en/20.webp)


Wenn Sie auf XML-Datei herunterladen klicken, wird die Datei autounattend.xml heruntergeladen. Um diese Datei zu verwenden, binden Sie einfach die heruntergeladene ISO-Datei auf einem USB-Laufwerk ein, legen die Datei autounattend.xml im Stammverzeichnis ab und fahren dann mit der Windows-Installation fort.


Eines der verfügbaren Tools zur Erstellung eines bootfähigen USB-Laufwerks ist Rufus. Rufus kann ein bootfähiges Windows-Installations-Flash-Laufwerk mit einer bestimmten Windows-Installations-ISO-Datei erstellen. Es ist schnell und einfach, Sie können es [hier](https://rufus.ie/en/#download) herunterladen


![Image](assets/en/21.webp)


In dieser Software klicken wir nach Auswahl des gewünschten USB-Laufwerks und der entsprechenden ISO-Datei auf Start.


![Image](assets/en/22.webp)


In diesem Stadium deaktivieren wir alle Optionen, da deren Aktivierung zu Konflikten bei der Verwendung der generierten Unattend-Datei führen kann. Nachdem die Dateien auf das USB-Laufwerk kopiert wurden, legen wir die Datei autounattend.xml im Stammverzeichnis ab:


![Image](assets/en/23.webp)


Jetzt ist das USB-Laufwerk für die automatische Installation von Windows bereit, und die Installation kann über dieses Laufwerk gestartet werden.


## ISO-Bearbeitung


Wenn Sie Windows auf einer virtuellen Maschine installieren müssen, können Sie Software zum Erstellen und Bearbeiten von ISO-Dateien verwenden. Eine solche Software ist AnyBurn. Nachdem Sie den Inhalt der von der Microsoft-Website heruntergeladenen ISO-Datei extrahiert haben, legen Sie die Datei autounattend.xml in das Stammverzeichnis. Erstellen Sie dann mit AnyBurn eine neue ISO-Datei mit den aktualisierten Inhalten.


AnyBurn ist eine multifunktionale Software für die Arbeit mit ISO-Dateien. Sie bietet verschiedene Funktionen für den Umgang mit ISO-Dateien, eine davon ist die Erstellung bootfähiger ISO-Images; [hier](https://www.anyburn.com/download.php) ist die Original-Website.


Wählen Sie auf der Hauptseite der Software "Bild aus Datei/Ordner erstellen":


![Image](assets/en/24.webp)


Auf der nächsten Seite wählen Sie alle aus der ISO-Datei extrahierten Dateien sowie die Datei autounattend.xml aus.


![Image](assets/en/25.webp)


In diesem Schritt konfigurieren wir die Einstellungen, um die ISO-Datei bootfähig zu machen:


![Image](assets/en/26.webp)


In diesem Stadium muss der Pfad zur Datei bootfix.bin festgelegt werden, um das ISO bootfähig zu machen. Diese Datei befindet sich im Stammverzeichnis der ISO-Datei, im Boot-Ordner. Es wird auch empfohlen, die Optionen ISO9660 und UDF im Abschnitt Eigenschaften zu aktivieren.


![Image](assets/en/27.webp)


Wenn Sie nach diesem Schritt auf Weiter klicken, wird die ISO-Datei erstellt. Diese Datei kann in Virtualisierungssoftware wie Oracle VirtualBox verwendet werden. Nachstehend finden Sie eine Anleitung zu VirtualBox:


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65