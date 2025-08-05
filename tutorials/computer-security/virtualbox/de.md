---
name: VirtualBox
description: Installieren Sie VirtualBox unter Windows 11 und erstellen Sie Ihre erste VM
---
![cover](assets/cover.webp)



___



*Dieses Tutorial basiert auf Originalinhalten von Florian Burnel, veröffentlicht auf [IT-Connect](https://www.it-connect.fr/). Lizenz [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Am Originaltext können Änderungen vorgenommen worden sein.*



___




## I. Präsentation



In diesem Tutorial lernen wir, wie man VirtualBox unter Windows 11 installiert, um virtuelle Maschinen zu erstellen, sei es für Windows 10, Windows 11, Windows Server oder eine Linux-Distribution (Debian, Ubuntu, Kali Linux, etc.).



Dieses Einführungs-Tutorial zu VirtualBox soll Ihnen den Einstieg in diese von Oracle entwickelte Open-Source-Virtualisierungslösung erleichtern, die völlig kostenlos ist. Später werden weitere Tutorials online gestellt, die Sie tiefer in das Thema einführen.



Wenn es um die Virtualisierung eines Arbeitsplatzes geht, sei es zu Testzwecken im Rahmen eines Projekts oder während Ihres IT-Studiums, ist VirtualBox eindeutig eine gute Lösung. Es ist auch eine Alternative zu anderen Lösungen wie Hyper-V, das in Windows 10 und Windows 11 (sowie in Windows Server) integriert ist, und VMware Workstation (kostenpflichtig) / VMware Workstation Player (kostenlos für den privaten Gebrauch).



Meine Konfiguration: **ein Windows 11-Arbeitsplatz, auf dem ich VirtualBox installieren werde**, aber Sie können VirtualBox sowohl auf Windows 10 (oder einer älteren Version) als auch auf Linux installieren. Was virtuelle Maschinen betrifft, so unterstützt VirtualBox eine breite Palette von Systemen, darunter Windows (z.B. Windows 10, Windows 11, Windows Server 2022, etc.), Linux (Debian, Rocky Linux, Ubuntu, Fedora, etc.), BSD (PfSense) und macOS.



## II. VirtualBox für Windows 11 herunterladen



Um VirtualBox für die Installation auf einem Windows-Rechner herunterzuladen, gibt es nur einen guten Address: die [offizielle VirtualBox-Website] (https://www.virtualbox.org/wiki/Downloads) im Abschnitt "**Downloads**". Klicken Sie einfach auf "Windows-Hosts", um den Download dieser ausführbaren Datei zu starten, die etwas über 100 MB groß ist.



![Image](assets/fr/025.webp)



## III. Installation von VirtualBox unter Windows 11



### A. Installation von VirtualBox



Die Installation von VirtualBox** ist ganz einfach und für alle Windows-Versionen gleich. Starten Sie zunächst die ausführbare VirtualBox-Datei, die Sie gerade heruntergeladen haben, und klicken Sie dann auf "**Weiter**".



![Image](assets/fr/026.webp)



Diese Installation ist anpassbar, aber ich empfehle Ihnen, alle Funktionen zu installieren: das ist der Fall bei der Standardauswahl. Auf dem Bild unten sehen Sie verschiedene Elements, darunter :





- VirtualBox USB-Unterstützung**, damit VirtualBox USB-Geräte unterstützen kann
- VirtualBox Bridged Network** zur Integration der Netzwerkunterstützung im "Bridge"-Modus (die virtuelle Maschine kann sich direkt mit Ihrem lokalen Netzwerk verbinden)
- VirtualBox Host-Only Network** zur Integration der Netzwerkunterstützung im "Host-Only"-Modus (die virtuelle Maschine kann in diesem Modus nur mit Ihrem physischen Windows 11-Host und anderen virtuellen Maschinen kommunizieren)



Klicken Sie auf "**Weiter**", um fortzufahren.



![Image](assets/fr/001.webp)



Klicken Sie auf "**Ja**" und bedenken Sie, dass **das Netzwerk auf Ihrem Windows 11-Rechner** für einen Moment unterbrochen wird, während VirtualBox Netzwerkänderungen vornimmt, um verschiedene Netzwerktypen zu unterstützen, einschließlich des Bridge-Modus.



![Image](assets/fr/002.webp)



Sobald Sie dies bestätigt haben, beginnt die Installation... Und es erscheint eine Meldung "**Möchten Sie diese Gerätesoftware installieren?**". Aktivieren Sie die Option "**Vertraue immer Software von Oracle Corporation**" und klicken Sie auf "**Installieren**". VirtualBox muss tatsächlich mehrere Treiber auf Ihrem Computer installieren.



![Image](assets/fr/003.webp)



Die Installation ist nun abgeschlossen! Aktivieren Sie die Option "**Nach der Installation Oracle VM VirtualBox 6.1.34 starten**" und klicken Sie auf "**Klicken**", um die Software zu starten.



![Image](assets/fr/004.webp)



### B. Hinzufügen des Erweiterungspakets



Auf der offiziellen VirtualBox-Website (siehe vorheriger Link) können Sie ein offizielles Erweiterungspaket herunterladen, das Sie unter dem Abschnitt "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" finden, indem Sie auf den Link "**Alle unterstützten Plattformen**" klicken. Mit diesem Paket können Sie VirtualBox zusätzliche Funktionen hinzufügen: Es ist nicht zwingend erforderlich, aber es kann nützlich sein! Es enthält zum Beispiel Unterstützung für USB 3.0 in VMs, Webcam-Unterstützung und Festplattenverschlüsselung.



Öffnen Sie VirtualBox, klicken Sie auf "**Datei**" und dann im Menü auf "**Einstellungen**".



![Image](assets/fr/005.webp)



Klicken Sie auf "**Erweiterungen**" auf der linken Seite (1), dann auf die Schaltfläche "**+**" auf der rechten Seite (2), um das soeben heruntergeladene VirtualBox**-Erweiterungspaket zu **laden** (3).



![Image](assets/fr/006.webp)



Bestätigen Sie mit einem Klick auf die Schaltfläche "**Installation**".



![Image](assets/fr/007.webp)



Klicken Sie auf "**OK**": Das offizielle Erweiterungspaket ist nun auf Ihrer VirtualBox-Instanz installiert!



![Image](assets/fr/008.webp)



Fahren wir nun mit der Erstellung unserer ersten virtuellen Maschine fort.



## IV. Erstellen Ihrer ersten VirtualBox-VM



Um eine neue virtuelle Maschine in VirtualBox zu erstellen, klicken Sie einfach auf die Schaltfläche "**Neu**", um den Assistenten zur Erstellung einer VM zu starten. Da Sie VirtualBox zum ersten Mal starten, möchte ich Ihnen ein paar weitere Details über Interface und die anderen Schaltflächen geben.





- Einstellungen**: allgemeine VirtualBox-Konfiguration (Standard-VM-Ordner, Update-Verwaltung, Sprache, NAT-Netzwerke, Erweiterungen usw.)
- Import**: Importieren einer virtuellen Anwendung im OVF-Format
- Export**: Exportieren Sie eine vorhandene virtuelle Maschine im OVF-Format, um eine virtuelle Appliance zu erstellen
- Hinzufügen**: Hinzufügen einer vorhandenen virtuellen Maschine zu Ihrem VirtualBox-Inventar, im Standard-VirtualBox-Format (.vbox) oder im XML-Format



Auf der linken Seite bietet der Bereich "**Tools**" Zugang zu **erweiterten Funktionen, insbesondere zur Verwaltung des virtuellen Netzwerks, aber auch zur Verwaltung des VM-Speichers**. Unter dem Eintrag "**Tools**" werden später Ihre virtuellen Maschinen hinzugefügt.



![Image](assets/fr/009.webp)



### A. Prozess der VM-Erstellung



**Zur Erinnerung: VirtualBox unterstützt eine Vielzahl von Betriebssystemen, darunter Windows, Linux und BSD. In diesem Beispiel werde ich eine virtuelle Maschine für Windows 11 erstellen. Es müssen mehrere Felder ausgefüllt werden:





- Name**: Name der virtuellen Maschine (dies ist der Name, der in VirtualBox angezeigt wird)
- Maschinenordner**: Speicherort der virtuellen Maschine, wobei ein Unterordner mit dem Namen der VM an diesem Ort erstellt wird
- Typ**: der Typ des Betriebssystems, je nachdem, welches Betriebssystem Sie installieren möchten
- Version**: die Version des Systems, das Sie installieren möchten, in diesem Fall Windows 11, also "**Windows11_64**"



Klicken Sie auf "**Weiter**", um fortzufahren.



![Image](assets/fr/010.webp)



Je nach dem Betriebssystem, das Sie im vorherigen Schritt ausgewählt haben, gibt **VirtualBox Empfehlungen zu den Ressourcen, die der virtuellen Maschine zugewiesen werden sollen**. Hier geht es um den Arbeitsspeicher, den Sie der VM zuweisen möchten. Nehmen wir 4 GB an, da dies für Windows 11 empfohlen wird, aber wenn Sie nicht genügend Ressourcen haben, können Sie stattdessen 2 GB angeben. **Fortfahren



**Hinweis**: Die der virtuellen Maschine zugewiesenen Ressourcen können später geändert werden.



![Image](assets/fr/011.webp)



Was die virtuelle Hard-Platte angeht, so fangen wir bei Null an, also müssen wir "**Jetzt virtuelle Hard-Platte erstellen**" wählen, damit die VM über Speicherplatz für die Installation des Betriebssystems und die Speicherung von Daten verfügt. Klicken Sie auf "**Erstellen**".



![Image](assets/fr/012.webp)



VirtualBox unterstützt drei verschiedene Formate für virtuelle Hard-Festplatten, was einen großen Unterschied zu anderen Lösungen wie VMware und Hyper-V darstellt. Es gibt drei Formate zur Auswahl:





- VDI**, das offizielle VirtualBox-Format
- VHD**, das offizielle Hyper-V-Format, obwohl das neue VHDX-Format heutzutage immer häufiger verwendet wird
- VMDX** ist das offizielle VMware-Format sowohl für VMware Workstation als auch für VMware ESXi



Um eine virtuelle Maschine zu erstellen, die nur auf dieser VirtualBox-Instanz verwendet werden soll, wählen Sie "**VDI**". Wenn die virtuelle Hard-Platte jedoch später an einen Hyper-V-Host angeschlossen werden soll, kann es sinnvoll sein, mit dem VHD-Format zu beginnen, um eine Konvertierung zu vermeiden. Klicken Sie auf "**Weiter**".



![Image](assets/fr/013.webp)



**Die virtuelle Festplatte kann entweder dynamisch oder in ihrer Größe festgelegt sein**. Wenn sie dynamisch ist, wächst die Datei, die **die virtuelle Festplatte repräsentiert (hier eine .vdi-Datei), wenn Daten auf die Festplatte geschrieben werden**, bis sie ihre maximale Größe erreicht hat, aber sie schrumpft nicht, wenn Daten gelöscht werden. Wenn sie dagegen eine feste Größe hat, wird **der gesamte Speicherplatz sofort zugewiesen (und somit reserviert)**, was eine etwas höhere Leistung ermöglicht, aber bei der ersten Erstellung des virtuellen Datenträgers länger dauert.



Für virtuelle Testmaschinen mit VirtualBox halte ich persönlich den Modus **dynamisch zugewiesen**" für ausreichend.



![Image](assets/fr/014.webp)



**Der nächste Schritt ist die Angabe der Größe der virtuellen Festplatte**, wobei zu beachten ist, dass die Festplatte standardmäßig im VM-Verzeichnis gespeichert wird (dies kann in diesem Stadium geändert werden). Ich habe eine Größe von 64 GB angegeben, um die Anforderungen von Windows 11 zu erfüllen, aber auch hier kann eine kleinere Größe zugewiesen werden. Klicken Sie auf "**Erstellen**", um die VM zu erstellen!



![Image](assets/fr/015.webp)



Zu diesem Zeitpunkt befindet sich die VM in unserem Inventar, sie ist konfiguriert, aber das Betriebssystem ist noch nicht installiert. Wir müssen die Konfiguration der VM abschließen, bevor wir sie in Betrieb nehmen.



### B. Zuweisung eines ISO-Images zu einer VirtualBox-VM



Um Windows 11 oder ein anderes System zu installieren, benötigen wir Installationsquellen. In den meisten Fällen verwenden wir zur Installation eines Betriebssystems ein Disk-Image im ISO-Format. **Es ist notwendig, das ISO-Image von Windows 11 in das virtuelle DVD-Laufwerk unserer VM zu laden



Klicken Sie auf die VM im VirtualBox-Inventar (1) und dann auf die Schaltfläche "**Konfiguration**" (2), die Zugang zur allgemeinen Konfiguration dieser virtuellen Maschine bietet. Dieses Menü dient zur Verwaltung der Ressourcen (z.B. RAM erhöhen, CPU konfigurieren, etc.). Klicken Sie auf "**Speicher**" auf der linken Seite (3), auf das DVD-Laufwerk, auf dem "**Leer**" steht (4), dann auf das DVD-Symbol (5) und "**Wählen Sie eine Datenträgerdatei**".



![Image](assets/fr/016.webp)



Wählen Sie das ISO-Image des Betriebssystems aus, das Sie installieren möchten, und klicken Sie auf OK. Ich erhalte die folgende Meldung:



![Image](assets/fr/017.webp)



Bleiben Sie im Abschnitt "**Konfiguration**" der VM, ich muss noch ein paar Dinge erklären.



### C. VM-Netzwerkverbindung



Gehen Sie zum Abschnitt "**Netzwerk**" auf der linken Seite. In diesem Bereich können Sie das Netzwerk der virtuellen Maschine verwalten: Anzahl der virtuellen Netzwerkschnittstellen (bis zu 4 pro VM), MAC Address und Netzwerkzugriffsmodus (NAT, Bridge Access, internes Netzwerk usw.). **Wenn Sie möchten, dass Ihre virtuelle Maschine Zugang zum Internet hat, wählen Sie "NAT" oder "Bridge Access "**, aber dieser zweite Modus erfordert, dass ein DHCP-Server in Ihrem Netzwerk aktiv ist, oder Sie müssen eine IP Address manuell konfigurieren.



Hinweis: Ich werde in einem eigenen Artikel ausführlicher auf den Netzwerkteil zurückkommen.



![Image](assets/fr/018.webp)



### D. Die Anzahl der virtuellen Prozessoren



Wie ein physischer Computer benötigt auch eine virtuelle Maschine Arbeitsspeicher, eine Hard-Festplatte und einen Prozessor, um zu funktionieren. Bei der Erstellung der VM haben Sie vielleicht bemerkt, dass der Assistent die Konfiguration des Prozessors nicht berücksichtigt hat. Dies kann jedoch jederzeit über die Registerkarte "**System**" und dann "**Prozessor**" konfiguriert werden, wo Sie die Anzahl der virtuellen Prozessoren auswählen können.



Hinweis: Die Option "**VT-x/AMD-v verschachtelt aktivieren**" ist für verschachtelte Virtualisierung erforderlich.



In meinem Fall hat die virtuelle Maschine 2 virtuelle Prozessoren:



![Image](assets/fr/019.webp)



**Zögern Sie nicht, sich auch die anderen Abschnitte des Konfigurationsmenüs anzuschauen.



### E. Erster Start und Betriebssysteminstallation



Um eine virtuelle Maschine zu starten, wählen Sie sie einfach im Inventar aus und klicken Sie auf die Schaltfläche "**Start**". Es öffnet sich ein zweites Fenster, das einen visuellen Überblick über die VM bietet.



![Image](assets/fr/020.webp)



Autsch, ich bekomme eine böse Fehlermeldung und meine virtuelle Maschine lässt sich nicht starten! Die Fehlermeldung lautet "Login failed for virtual machine..." mit den folgenden Details:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



Das ist ganz normal, denn **die Virtualisierungsfunktion ist auf meinem Computer nicht aktiviert**! Um dieses Problem zu beheben, müssen Sie Ihren Computer neu starten, um auf das BIOS zuzugreifen und die Virtualisierung zu aktivieren.



![Image](assets/fr/021.webp)



Ohne zu warten, starte ich meinen Computer neu und **drücke die Taste "SUPPR", um auf das BIOS** (die Taste kann je nach Rechner variieren und könnte z. B. F2 sein) meines ASUS-Motherboards zuzugreifen. Um die Virtualisierung zu aktivieren, muss in meinem Fall der "SVM-Modus" aktiviert werden. Auch hier kann sich der Name von einem Motherboard zum anderen und von einem Hersteller zum anderen ändern. Suchen Sie nach einer Funktion, die **AMD-V** (für eine AMD-CPU) oder **Intel VT-x** (für eine Intel-CPU) heißt.



![Image](assets/fr/022.webp)



Sobald dies geschehen ist, speichern Sie die Änderung und starten Sie die physische Maschine neu... Diesmal kann **VirtualBox die virtuelle Maschine** starten und das Windows-ISO-Image laden, um das Betriebssystem zu installieren! 🙂



![Image](assets/fr/023.webp)



Auf unserem physischen Windows 11-Host, auf dem VirtualBox installiert ist, können wir sehen, dass der Ordner der virtuellen Windows 11-Maschine verschiedene Dateien enthält.





- Die VBOX**-Datei (im XML-Format), die der VM-Konfiguration entspricht (RAM, CPU, usw.)
- Die Datei VBOX-PREV** ist eine Sicherungskopie der vorherigen Konfiguration
- Die VDI**-Datei entspricht der virtuellen Hard-Platte im dynamischen Modus und ist daher derzeit nur 13 GB groß, während ihre maximale Größe 64 GB beträgt
- Die NVRAM**-Datei enthält den BIOS-Status der virtuellen Maschine, der dem nichtflüchtigen Speicher einer physischen Maschine entspricht



![Image](assets/fr/024.webp)



## V. Schlussfolgerung



**VirtualBox ist jetzt auf unserem physischen Windows 11-Rechner eingerichtet und läuft! Jetzt müssen wir nur noch die Vorteile nutzen und virtuelle Maschinen erstellen!** Auf die Installation von Windows 11 in einer VirtualBox-VM werde ich in einem anderen Artikel zurückkommen. Für Windows 10, Windows Server oder eine Linux-Distribution (Ubuntu, Debian, etc.), lassen Sie sich einfach von uns führen!