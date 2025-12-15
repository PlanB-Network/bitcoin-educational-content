---
name: Angry IP Scanner
description: Eine einfache Möglichkeit, Ihr Netzwerk zu scannen
---
![cover](assets/cover.webp)



___



*Dieses Tutorial basiert auf Originalinhalten von Florian BURNEL, veröffentlicht auf [IT-Connect](https://www.it-connect.fr/). Lizenz [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Am Originaltext können Änderungen vorgenommen worden sein.*



___



## I. Präsentation



Wie scannt man ein Windows-Netzwerk schnell und einfach nach angeschlossenen Rechnern? Die Antwort ist Angry IP Scanner. Mit diesem Open-Source-Projekt können Sie ein Netzwerk mithilfe eines benutzerfreundlichen grafischen Interface einfach scannen.



Dieses Tool kann von Einzelpersonen zum **Scannen ihres lokalen Netzwerks** verwendet werden, aber auch von IT-Fachleuten für den gleichen Zweck. Ein Beweis dafür, dass **dieses Tool sehr praktisch ist**, ist, dass es bereits von **einigen cyberkriminellen Gruppen** verwendet wurde, um Unternehmensnetzwerke zu scannen (auf dieselbe Weise wie Nmap). Ein gutes Beispiel ist die [Ransomware-Gruppe RansomHub] (https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Es ist immer noch ein solides Stück Software, aber wie bei anderen netzwerk- und sicherheitsorientierten Tools kann es missbraucht werden.



Wir verwenden es hier unter **Windows 11**, aber es ist durchaus möglich, es auch unter anderen Versionen von **Windows**, **Linux** und **macOS** zu verwenden.



Der **Angry IP** Scanner ist zwar weniger umfangreich als Nmap, aber immer noch interessant für eine schnelle, grundlegende Netzwerkanalyse, auch weil er für jedermann zugänglich ist. Er **ermittelt mit dem Netzwerk verbundene Hosts** und identifiziert **Hostnamen** und **offene Ports**.



Wenn Sie weiter gehen wollen, sehen Sie sich das Tutorial zu Nmap an:



https://planb.academy/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Erste Schritte mit Angry IP Scanner



### A. Angry IP Scanner herunterladen und installieren



Sie können die neueste Version von Angry IP Scanner von der offiziellen Website der Anwendung oder von GitHub herunterladen. Wir werden die letztere Option verwenden. Klicken Sie auf den unten stehenden Link und laden Sie die EXE-Version herunter: "**ipscan-3.9.1-setup.exe**".





- [Angry IP Scanner GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Führen Sie die ausführbare Datei aus, um mit der Installation fortzufahren. Während der Installation gibt es nichts Besonderes zu tun.



![Image](assets/fr/013.webp)



### B. Führen Sie einen ersten Netzwerk-Scan durch



Nehmen Sie sich beim ersten Start die Zeit, die Anweisungen im Fenster "**Einstieg**" zu lesen, um mehr über die Funktionsweise des Tools zu erfahren. Übrigens gibt es einige Begriffe zu beachten:





- **Feeder**: Modul zur Erstellung von Listen der zu überprüfenden IP-Adressen aus einem zufälligen IP-Bereich oder einer Datei mit einer Liste von IP-Adressen.
- **Fetcher**: eine Reihe von Modulen zum Abrufen von Informationen über Hosts im Netz. Es gibt z. B. Fetchers zum Erkennen von MAC-Adressen, zum Scannen von Ports, zum Erkennen von Hostnamen oder zum Senden von HTTP-Anfragen.



![Image](assets/fr/018.webp)



Um ein IP-Subnetz zu scannen, geben Sie einfach die **Start-IP Address** und die **Ende-IP Address** in das Feld "**IP-Bereich**" ein (andernfalls ändern Sie den Typ auf der rechten Seite). Klicken Sie dann auf die Schaltfläche "**Start**".



![Image](assets/fr/019.webp)



Einige Dutzend Sekunden später wird das Ergebnis im Interface der Software sichtbar sein. **Für jede IP Address im analysierten Bereich sehen Sie, ob Angry IP Scanner einen Host erkannt hat oder nicht.** Außerdem wird eine Zusammenfassung auf dem Bildschirm angezeigt, die die Anzahl der aktiven Hosts (in diesem Fall 6) und die Anzahl der Hosts mit offenen Ports angibt.



![Image](assets/fr/020.webp)



Hier sehen wir das Vorhandensein eines Hosts mit dem Namen "**OPNsense.local.domain**", der mit dem IP Address "**192.168.10.1**" verbunden und über die **Ports 80** und **443** (HTTP und HTTPS) erreichbar ist. Wenn Sie mit der rechten Maustaste auf den Host klicken, erhalten Sie Zugriff auf zusätzliche Befehle wie Ping, Trace Route und Öffnen des Browsers über diese IP Address.



![Image](assets/fr/012.webp)



### C. Scan-Ports hinzufügen



Standardmäßig wird **Angry IP Scanner** 3 Ports scannen: **80** (HTTP), **443** (HTTPS) und **8080**. Sie können in den Anwendungseinstellungen weitere Ports hinzufügen, die gescannt werden sollen. Klicken Sie auf das Menü "**Tools**" und dann auf die Registerkarte "**Ports**".



Hier können Sie die Portliste über die Option "**Portauswahl**" ändern. Sie können **einzelne, durch ein Komma getrennte Portnummern oder Portbereiche** angeben. Im folgenden Beispiel werden zwei Ports hinzugefügt: **445** (SMB) und **389** (LDAP). Um Ports von 1 bis 1000 zu scannen, geben Sie "**1-1000**" ein. Es wird nicht angegeben, ob die Port-Scans in TCP, UDP oder beidem durchgeführt werden.



![Image](assets/fr/021.webp)



Wenn Sie den Scan erneut ausführen, werden Sie wahrscheinlich neue Informationen erhalten. Im Beispiel unten sagt mir Angry IP Scanner, dass die Ports 389 und 445 auf den Hosts "**SRV-ADDS-01**" und "**SRV-ADDS-02**" offen sind, dank der neuen Konfiguration der zu scannenden Ports.



![Image](assets/fr/022.webp)



**Hinweis**: Über das Menü "**Scanner**" können Sie die Scanergebnisse in eine Textdatei exportieren.



Wenn Sie den Scan weiter ausbauen möchten, klicken Sie auf das Menü "**Tools**" und dann auf "**Fetchers**". Dies fügt dem Scan "Fähigkeiten" hinzu. Wählen Sie einfach einen Abrufer aus und schieben Sie ihn nach links, um ihn zu aktivieren. Dadurch wird dem Scan-Ergebnis eine zusätzliche Spalte hinzugefügt.



![Image](assets/fr/014.webp)



Das folgende Beispiel zeigt die Funktionen "**NetBIOS-Info**" und "**Web-Erkennung**". Erstere liefert zusätzliche Informationen wie den MAC Address und den Domänennamen des Rechners, während letztere den Titel der Webseite anzeigt (der einen Hinweis auf den Typ des Webservers oder der Anwendung geben kann).



![Image](assets/fr/011.webp)



Schließlich können Sie in den Einstellungen auch die Methode ändern, die für "**ping**" verwendet wird, d. h. um zu prüfen, ob ein Host aktiv ist oder nicht. Da einige Hosts nicht auf Pings reagieren, können Sie hier andere Methoden ausprobieren (UDP-Paket, TCP-Port-Sonde, ARP, UDP + TCP-Kombination usw.).



## III. Schlussfolgerung



Einfach und effektiv: Angry IP Scanner erkennt Hosts, die mit einem Netzwerk verbunden sind, und lässt Sie Port-Scans konfigurieren. Was die Optionen angeht, ist er nicht so flexibel wie Nmap und geht nicht so weit, aber er ist ein guter Anfang für schnelle Scans.



Wenn Sie **Nmap** mit einem grafischen Interface nutzen möchten, können Sie **die Zenmap-Anwendung** verwenden (siehe Übersicht unten).



![Image](assets/fr/015.webp)



https://planb.academy/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d