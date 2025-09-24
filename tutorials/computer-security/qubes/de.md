---
name: Qubes
description: Ein einigermaßen sicheres Betriebssystem.
---

![cover](assets/cover.webp)



Qubes OS ist ein freies, quelloffenes Betriebssystem, das für Benutzer entwickelt wurde, die Sicherheit an die erste Stelle ihrer Prioritäten setzen. Seine Besonderheit beruht auf einer einfachen, aber radikalen Idee: Anstatt den Computer als Ganzes zu betrachten, unterteilt es seine Nutzung in unabhängige Abteilungen, die **_qubes_** genannt werden.



Jede qube funktioniert wie eine **isolierte virtuelle Umgebung** mit einer bestimmten Vertrauensstufe und Funktion. Selbst wenn also eine Anwendung kompromittiert wird, bleibt der Angriff auf ihre qube beschränkt, ohne den Rest des Systems zu beeinträchtigen.



> Wenn Sie es mit der Sicherheit ernst meinen, ist Qubes OS das beste derzeit verfügbare Betriebssystem. - **Edward Snowden**.

Die Installation von Qubes OS erfordert jedoch mehr Vorbereitung als die Installation eines herkömmlichen Betriebssystems. Es erfordert die Überprüfung bestimmter Hardware-Voraussetzungen, das Verständnis der Grundlagen der Virtualisierung und die Akzeptanz einer anderen Erfahrung, bei der jede alltägliche Aufgabe in Form einer Trennung betrachtet wird. Sobald es jedoch installiert ist, bietet Qubes OS ein robustes Framework, das die Art und Weise, wie Sie täglich mit Ihrem Computer interagieren, neu definiert. In diesem Tutorial erklären wir Ihnen, wie Qubes OS funktioniert und wie Sie es einfach auf Ihrem System installieren können.



## Wie funktioniert Qubes OS?



Qubes OS basiert auf dem Prinzip der Kompartimentierung. Anstatt ein einziges System zu verwenden, stützt es sich auf den **Xen**-Hypervisor, um isolierte virtuelle Maschinen, sogenannte qubes, zu erstellen. Jede qube ist für eine bestimmte Aufgabe oder Vertrauensstufe (Arbeit, persönliches Surfen, Bankgeschäfte usw.) bestimmt. Durch diese Trennung wird sichergestellt, dass eine Kompromittierung in einer qube nicht auf die anderen übergreifen kann, so dass sie wie mehrere unabhängige Computer innerhalb eines einzigen Rechners funktionieren.



Der Benutzer Interface wird von einer zentralen, sicheren Domäne namens **dom0** verwaltet. Diese Domäne ist völlig vom Internet isoliert und damit das Herzstück des Systems. Obwohl Fenster und Menüs von dom0 angezeigt werden, findet die eigentliche Ausführung von Anwendungen in den jeweiligen Qubes statt.



## Die verschiedenen Arten von Qubes



Um dom0 drehen sich verschiedene Arten von Qubes, die jeweils eine ganz bestimmte Rolle spielen.





- Die **AppVM** werden für die Ausführung alltäglicher Anwendungen verwendet: Der Benutzer kann so seine beruflichen E-Mails von seinen Internet- oder Bankaktivitäten trennen, wobei jede Umgebung völlig unabhängig von der anderen bleibt.





- Diese AppVMs basieren ihrerseits auf **TemplateVMs**, die als zentralisierte Vorlagen für die Installation und Aktualisierung von Software dienen, wodurch die Notwendigkeit entfällt, jede qube separat zu verwalten.



Qubes OS integriert auch virtuelle Maschinen, die auf **Systemdienste** spezialisiert sind.





- Die **NetVM** verwaltet direkt die **Netzwerkgeräte** und stellt die Verbindung zum Internet sicher. Sie sind oft mit **FirewallVMs** verbunden, die eingreifen, um den **Verkehr zu filtern** und die Exposition anderer Qubes zu begrenzen.





- ServiceVMs spielen eine ähnliche Rolle, zum Beispiel bei der Verwaltung von USB-Geräten, immer mit der gleichen Logik: Isolierung der risikoreichsten Komponenten, um die Angriffsfläche zu verringern.



Für gelegentliche oder riskante Aufgaben bietet Qubes OS schließlich **DisposableVM**. Diese ephemeren VMs werden spontan erstellt, um **ein verdächtiges Dokument** zu öffnen oder **eine zweifelhafte Website** zu besuchen, und verschwinden dann vollständig, wenn sie geschlossen werden, um alle Spuren zu löschen und einen anhaltenden Angriff zu verhindern.



### Der Mechanismus für sichere Kopien (qrexec)



Der Austausch zwischen qubes basiert auf **qrexec**, einem auf Sicherheit ausgelegten Inter-VM-Kommunikationssystem. Anstatt qubes frei kommunizieren zu lassen, schreibt qrexec **spezifische Richtlinien** vor: eine Datei, die von einer AppVM in eine andere kopiert wird, oder Text, der über die Zwischenablage übertragen wird, durchläuft immer einen Kanal, der vom System überwacht und validiert wird. Auf diese Weise wird selbst der einfache Akt des Kopierens und Einfügens kontrolliert, um die Verbreitung von Malware zu verhindern.



### Festplattenverwaltung



Qubes OS verwendet ein ausgeklügeltes System für die Speicherverwaltung. TemplateVMs enthalten die gemeinsame Softwarebasis, während AppVMs nur ihre persönlichen Daten und spezifischen Dateien hinzufügen. Dies reduziert den Speicherplatzbedarf und erleichtert globale Aktualisierungen. DisposableVMs hingegen verwenden temporäre Volumes, die beim Schließen vollständig verschwinden. Dieses Modell garantiert nicht nur mehr Sicherheit, sondern auch eine effiziente Ressourcenverwaltung.



## Warum Qubes OS wählen?



Die Vorteile von Qubes OS liegen vor allem in seinem einzigartigen Sicherheitsmodell. Das Herzstück dieses Ansatzes ist die Kompartimentierung, die den Benutzer schützt, indem jede Aufgabe in separaten virtuellen Maschinen isoliert wird. In der Praxis bedeutet dies, dass eine infizierte E-Mail oder eine bösartige Website nur eine einzige Qubes kompromittieren kann, während der Rest des Systems und Ihre persönlichen Daten vollständig geschützt bleiben. Diese Architektur schränkt komplexe Angriffe, die sich auf einem herkömmlichen System ungehindert ausbreiten könnten, erheblich ein.



Qubes OS bietet außerdem vollständige Transparenz und Kontrolle über Ihre digitale Umgebung. Sie wissen genau, welche Software Zugriff auf welche Ressource hat, ob es sich um das Netzwerk, ein USB-Gerät oder andere sensible Komponenten handelt. Das System integriert standardmäßig fortschrittliche Sicherheitsfunktionen, wie die vollständige Festplattenverschlüsselung, und erleichtert die Nutzung von Anonymisierungsdiensten wie dem Whonix-Betriebssystem.



https://planb.network/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

Anstatt ein undurchdringliches System zu schaffen, konzentriert sich Qubes OS auf die Widerstandsfähigkeit: Es kapselt den Schaden im Falle einer Kompromittierung ein und reduziert so das Risiko für den Rest des Systems. Dieser pragmatische Ansatz macht Qubes OS zu einer bevorzugten Wahl für Benutzer mit hohen Sicherheitsanforderungen oder die ein Maximum an Kontrolle über ihr digitales Leben behalten wollen.



## Installation von Qubes OS



Bevor Sie Qubes OS installieren, müssen Sie sicherstellen, dass Ihre Hardware die Mindestanforderungen erfüllt, da das System auf Virtualisierung basiert, um Qubes zu isolieren. Die wichtigsten zu prüfenden Komponenten sind:




- Der **Prozessor**: Ein 64-Bit-Prozessor, der mit Hardware-Virtualisierung (Intel VT-x oder AMD-V) kompatibel ist.
- RAM: Mindestens 8 GB sind erforderlich, aber wir empfehlen einen RAM von 16 GB oder mehr, um mehrere Qubes gleichzeitig laufen zu lassen.
- **Speicherplatz**: mindestens 36 GB, idealerweise 128 GB auf einer SSD für optimale Leistung.



Um Qubes OS zu installieren, laden Sie das offizielle ISO-Image von der Qubes OS [official site](https://www.qubes-os.org/downloads/) herunter. Es ist wichtig, die Integrität des ISO-Images anhand der mitgelieferten GPG-Signaturen zu überprüfen, um sicherzustellen, dass die Datei nicht manipuliert wurde und der Download sicher ist.



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



Sobald die ISO-Datei überprüft wurde, müssen Sie ein bootfähiges Installationsmedium erstellen, in der Regel einen USB-Stick. Laden Sie dazu Software wie **Rufus** unter Windows oder **Etcher** unter Windows, Linux oder macOS herunter und installieren Sie sie. Mit diesen Tools können Sie die ISO-Datei auf den USB-Stick kopieren, so dass dieser bootfähig ist.



Bevor Sie mit der Installation beginnen, müssen Sie das **BIOS oder UEFI** Ihres Computers so konfigurieren, dass die **Virtualisierung** aktiviert wird und das Booten von USB möglich ist. Abhängig von Ihrem Computermodell kann es notwendig sein, **Secure Boot** zu deaktivieren, da Qubes OS bei aktivierter Option möglicherweise nicht bootet.



![0_02](assets/fr/02.webp)



Sobald diese Bedingungen erfüllt sind, starten Sie Ihren Computer neu und rufen das BIOS/UEFI auf, indem Sie sofort **Esc**, **Del**, **F9**, **F10**, **F11** oder **F12** (je nach Hersteller) drücken. Wählen Sie im Boot-Menü den USB-Stick als Boot-Gerät, um die Installation von Qubes OS zu starten.



**Startbildschirm**


Wenn Sie vom USB-Stick booten, gelangen Sie direkt in das Menü **GRUB**, in dem Sie die auszuführende Aktion auswählen können. Wählen Sie mit den Pfeiltasten auf Ihrer Tastatur "Qubes OS installieren" und drücken Sie "Enter".



![0_03](assets/fr/03.webp)



**Sprachwahl** :



Wenn die Installation beginnt, müssen Sie zunächst die **Sprache** und die **regionale Variante** wählen, die für Ihre Konfiguration geeignet sind. Dadurch wird sichergestellt, dass das System und die Installationsoptionen korrekt in der von Ihnen bevorzugten Sprache angezeigt werden.



![0_04](assets/fr/04.webp)



**Parameterkonfiguration** :



In diesem Stadium müssen Sie eine Reihe von Elements konfigurieren, bevor Sie die Installation auf Ihrem Rechner starten können.



![0_05](assets/fr/05.webp)



**Tastaturlayout** :



Klicken Sie auf die Option **Tastatur** und wählen Sie dann das **geeignete Layout** für Ihren Computer. Wenn Sie Ihre Wahl getroffen haben, klicken Sie auf **Beendet**, um zum nächsten Schritt überzugehen.



**Wahl des Reiseziels** :



Wählen Sie die Option "Installationsziel", um die Festplatte auszuwählen, auf der Sie Qubes OS installieren möchten. Standardmäßig erfolgt die Partitionierung automatisch, so dass Sie alle Daten von der Festplatte entfernen und das System auf ihr installieren können. Sie können jedoch **Benutzerdefiniert** oder **Erweiterte Anpassung** wählen, um eine benutzerdefinierte Partitionierung durchzuführen. Klicken Sie dann auf "Fertig". Das System wird Sie auffordern, ein **Passwort** festzulegen, das als Sicherheits-Layer zur Verschlüsselung Ihrer Daten dient. Achten Sie darauf, dass Sie ein komplexes und eindeutiges Passwort wählen.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Wählen Sie das Format für Datum und Uhrzeit** :


Klicken Sie auf die Option Zeit und Datum und wählen Sie dann Ihre geografische Zone aus. Sie können auch Ihr bevorzugtes Zeitformat wählen: 24h oder 12h.



![0_08](assets/fr/08.webp)



**Anlegen eines Benutzerkontos** :


Klicken Sie auf **Benutzer anlegen**, um Ihr **Erstkonto** zu erstellen, mit dem Sie sich bei Qubes OS anmelden können.



![0_09](assets/fr/09.webp)



**Aktivieren Sie das Root-Konto** :


Sie können auch **das Root-Konto** aktivieren, indem Sie ein separates Passwort für die Verwaltung festlegen.



![0_10](assets/fr/10.webp)



Nachdem Sie diese Einstellungen vorgenommen haben, klicken Sie auf **Installation starten**, um den Vorgang zu starten.



![0_11](assets/fr/11.webp)



Warten Sie auf das **Ende der Installation** und klicken Sie dann auf **System neu starten**, um die Installation abzuschließen und Qubes OS zu starten.



![0_12](assets/fr/12.webp)



**Zusätzliche Konfiguration** :


Nach dem Neustart fordert Qubes OS Sie auf, die **Standardvorlagen und die Qubes-Konfiguration** abzuschließen. Geben Sie das für die Verschlüsselung der Festplatte festgelegte Passwort ein.



![0_13](assets/fr/13.webp)



Als nächstes wählen Sie die **TemplateVM** aus, die Sie installieren möchten. Übliche Optionen sind **Debian 12 Xfce**, **Fedora 41 Xfce** und **Whonix 17**, wobei letzteres für Anwendungen empfohlen wird, die **Anonymität und Netzwerksicherheit** erfordern. Sie können auch die **Standardvorlage** definieren, die als Grundlage für die Erstellung neuer **AppVMs** dienen wird.



![0_14](assets/fr/14.webp)



Im Abschnitt **Hauptkonfiguration** können Sie festlegen, dass wichtige Systemkomponenten wie **sys-net**, **sys-firewall** und **default DisposableVM** automatisch erstellt werden. Es ist ratsam, die Option **sys-firewall und sys-usb disposable** zu aktivieren, um die Gefährdung von Geräten und Netzwerken im Falle einer Kompromittierung zu begrenzen. Sie können auch **Standard-AppVMs** erstellen, z. B. **persönlich**, **Arbeit**, **nicht vertrauenswürdig** und **Vault**, um Ihre Aktivitäten je nach Vertrauensstufe zu organisieren.



![0_15](assets/fr/15.webp)



Mit Qubes OS können Sie auch einen **qube für USB-Geräte** (sys-usb) erstellen und **Whonix Gateway und Workstation qubes** konfigurieren, um Ihre Kommunikation über das Tor-Netzwerk zu sichern. Für fortgeschrittene Benutzer können Sie im Abschnitt **Erweiterte Konfiguration** einen **LVM Thin Pool** erstellen, um den Speicherplatz zwischen qubes effizient zu verwalten.



Wenn Sie alle Optionen konfiguriert haben, klicken Sie auf **Fertigstellen** und dann auf **Konfiguration abschließen**. Warten Sie, während das System diese Einstellungen übernimmt. Sie werden dann aufgefordert, sich **in Ihr Benutzerkonto einzuloggen**, und Ihre Qubes-OS-Umgebung ist einsatzbereit, sicher und ordnungsgemäß für Ihre verschiedenen Aktivitäten isoliert.



![0_17](assets/fr/17.webp)



Ihr Betriebssystem ist nun installiert und einsatzbereit.



![0_18](assets/fr/18.webp)



## Erstellen Sie eine Qube auf Ihrem System



Um eine qube zu erstellen, wird der Prozess durch das Tool **Qube Manager** gesteuert, das über das Startmenü zugänglich ist. Klicken Sie im Toolfenster einfach auf das Symbol **Qube erstellen**, um ein neues Konfigurationsfenster zu öffnen. Geben Sie zunächst einen Namen für Ihre qube ein, z. B. "perso-web" oder "work", um ihre Verwendung zu kennzeichnen.



Als nächstes wählen Sie den **Typ** aus, normalerweise **AppVM** für Routineaufgaben oder **DisposableVM** für den temporären Einsatz. Es ist wichtig, das **Template** zu wählen, auf dem Ihre qube basieren wird, wie z.B. "fedora-39" oder "debian-12", da dies das Betriebssystem und die Software bereitstellt. Außerdem bestimmen Sie die **NetVM**, die für den Internetzugang der qube zuständig ist, standardmäßig **sys-firewall**.



Nachdem Sie die Speichergröße und den Arbeitsspeicher (RAM) angepasst haben, klicken Sie einfach auf **OK**, um den Erstellungsprozess zu starten. Sobald der Vorgang abgeschlossen ist, ist Ihre neue qube in der Liste sichtbar und einsatzbereit.



Zusammenfassend lässt sich sagen, dass Qubes OS kein gewöhnliches Betriebssystem ist, sondern eine hochmoderne Sicherheitslösung, die die Architektur des Personal Computers neu überdenkt. Sein Ansatz, der auf Kompartimentierung und Isolierung durch Virtualisierung basiert, bietet einen konkurrenzlosen Schutz gegen die ausgefeiltesten Bedrohungen. Durch die Segmentierung der Arbeitsumgebung in spezialisierte Bereiche für jede Aufgabe wird sichergestellt, dass sich Malware nicht ausbreiten und das gesamte System gefährden kann.



Ganz gleich, ob Sie sicher im Internet surfen, vertrauliche Informationen schützen oder mit unterschiedlichen Vertrauensstufen arbeiten müssen, Qubes OS bietet einen stabilen, transparenten Rahmen. Wenn Sie gute Praktiken anwenden und die Funktionen voll ausschöpfen, verfügen Sie über eine **digitale Festung**, die an moderne Bedrohungen angepasst ist. Erfahren Sie mehr über den Schutz Ihrer Daten und Ihrer Privatsphäre.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1