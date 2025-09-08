---
name: Lynis
description: Durchführung einer Sicherheitsüberprüfung eines Linux-Rechners mit Lynis
---
![cover](assets/cover.webp)



___



*Dieses Tutorial basiert auf Originalinhalten von Fares CHELLOUG, veröffentlicht auf [IT-Connect](https://www.it-connect.fr/). Lizenz [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Am Originaltext können Änderungen vorgenommen worden sein.*



___



## I. Präsentation



**In diesem Tutorial werden wir lernen, wie man mit Lynis eine Sicherheitsüberprüfung auf einem Linux-Rechner durchführt! Für diejenigen unter Ihnen, die **Lynis,** nicht kennen, ist es ein kleines Kommandozeilenprogramm, das die Konfiguration Ihres Servers analysiert und Empfehlungen zur **Verbesserung der Sicherheit Ihres Rechners** gibt



Lynis ist ein Open-Source-Tool von CISOFY, einem Unternehmen, das sich auf **System-Auditing und -Hardening** spezialisiert hat. Wenn Sie Fortschritte bei der Absicherung von Linux und beliebten Diensten (SSH, Apache2 usw.) machen wollen, ist Lynis Ihr Verbündeter! Lynis sagt Ihnen nicht nur, was schief läuft, sondern gibt auch Empfehlungen, die Sie in die richtige Richtung lenken (und Ihnen Zeit sparen).



**Lynis** funktioniert mit den meisten Linux-Distributionen, darunter: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis richtet sich an Linux-/UNIX-Anwender, ist aber auch **macOS**-kompatibel. Sehr schnell zu installieren, es gibt kein Abhängigkeitsmanagement auf Paketebene.



Es wird für eine Vielzahl von Zwecken verwendet:





- Sicherheitsaudits
- Konformitätsprüfung (PCI, HIPAA und SOX)
- Stärkere Systemkonfigurationen
- Erkennung von Schwachstellen



Das Tool wird von einer Vielzahl von Nutzern verwendet, darunter Systemadministratoren, IT-Prüfer und Pentester. Für Analysen basiert das Tool auf Standards wie **CIS Benchmark, NIST, NSA, OpenSCAP** und auf offiziellen Empfehlungen von **Debian, Gentoo, Red Hat**.



Das Projekt ist unter dieser Address auf **Github** verfügbar:





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Lynis von CISOFY herunterladen](https://cisofy.com/lynis/#download)



In diesem Schritt-für-Schritt-Tutorial werde ich **einen VPS mit Debian 12** verwenden und mich auf den SSH-Teil konzentrieren, da ich seine Konfiguration überprüfen und verbessern möchte.



## II. Download und Installation



Es gibt mehrere Möglichkeiten, Lynis herunterzuladen und zu installieren. Wählen Sie die von Ihnen bevorzugte Methode aus der folgenden Liste.



### A. Installation aus den Debian-Repositorien



Dieser Installationsmodus ermöglicht es Ihnen, den Befehl **lynis** von überall auf dem System aus zu verwenden, im Gegensatz zur Installation aus dem Quellcode, bei der Sie sich in dem Verzeichnis befinden müssen.



Verbinden Sie sich über SSH mit Ihrem Server und geben Sie die folgenden Befehle ein, um Lynis zu installieren:



```
sudo apt-get update
sudo apt-get install lynis -y
```



Das ist das Ergebnis:



![Image](assets/fr/024.webp)



### B. Herunterladen von der offiziellen Website



Sie können es auch von der Cisofy-Website herunterladen:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



Das ist das Ergebnis:



![Image](assets/fr/032.webp)



Als nächstes entpacken wir das Archiv mit dem folgenden Befehl:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



Das ist das Ergebnis:



![Image](assets/fr/020.webp)



Wechseln wir in den Ordner **lynis**:



```
cd lynis
```



Mit dem folgenden Befehl können wir nach Aktualisierungen suchen:



```
./lynis update info
```



Das ist das Ergebnis:



![Image](assets/fr/023.webp)



### C. Herunterladen von GitHub



Wir laden **Lynis** aus dem offiziellen GitHub-Repository herunter, indem wir den folgenden Befehl verwenden (*git* muss auf Ihrem Rechner vorhanden sein):



```
git clone https://github.com/CISOfy/lynis.git
```



Das ist das Ergebnis:



![Image](assets/fr/060.webp)



## III. Verwendung von Lynis



Lynis ist auf unserem Rechner vorhanden, also lasst uns lernen, wie man es benutzt!



### A. Wichtigste Bedienelemente und Optionen



Um die verfügbaren Befehle anzuzeigen, geben Sie einfach den folgenden Befehl ein:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe:
./lynis
```



Das ist das Ergebnis:



![Image](assets/fr/039.webp)



Außerdem haben Sie die folgenden Möglichkeiten:



![Image](assets/fr/040.webp)



Um alle verfügbaren Befehle anzuzeigen, geben Sie den folgenden Befehl ein:



```
sudo lynis show
```



Das ist das Ergebnis:



![Image](assets/fr/022.webp)



Wenn Sie alle Optionen anzeigen möchten, müssen Sie eingeben:



```
sudo lynis show options
```



Das ist das Ergebnis:



![Image](assets/fr/021.webp)



Im weiteren Verlauf dieses Artikels erfahren Sie, wie Sie bestimmte Optionen nutzen können.



### B. Durchführung der Systemprüfung



Wir werden **Lynis** bitten, unser System zu überprüfen und dabei aufzuzeigen, was korrekt konfiguriert ist und was verbessert werden könnte. Geben Sie dazu den folgenden Befehl ein:



```
sudo lynis audit system
# ou
./lynis audit system
```



Wenn Sie beim Ausführen dieses Befehls nicht als root angemeldet sind, wird das Tool standardmäßig mit den Rechten des angemeldeten Benutzers ausgeführt. Einige Tests werden in diesem Kontext nicht ausgeführt:



![Image](assets/fr/052.webp)



Im Folgenden sind die Tests aufgeführt, die in diesem Modus nicht durchgeführt werden:



![Image](assets/fr/051.webp)



Sobald der Befehl ausgeführt wurde, beginnt die Analyse. Warten Sie einfach einen Moment.



Am Ende des Audits erhalten Sie folgendes Ergebnis (wir sehen, dass **Lynis** das System **Debian 12** korrekt identifiziert hat und das **Debian-Plugin** für die Analyse verwenden wird):



![Image](assets/fr/017.webp)



Als Nächstes wird Lynis eine Reihe von Punkten auflisten, die allem entsprechen, was er in unserem System überprüft hat. Diese sind nach Kategorien geordnet, wie wir gleich sehen werden. Es ist auch erwähnenswert, dass ein Farbcode verwendet wird, um Empfehlungen hervorzuheben:





- Rot** für kritische Elements oder nicht eingehaltene bewährte Praktiken (z. B. ein fehlendes Paket), d. h. Ihr Server hält diesen Punkt nicht ein
- Gelb** für Vorschläge oder teilweise Erfüllung der Empfehlung (z. B. ist es von Vorteil, einen mit dieser Farbe hervorgehobenen Punkt zu erfüllen (nicht prioritär))
- Green** für Punkte, bei denen Ihre Serverkonfiguration konform ist
- Weiß**, wenn neutral



Hier können wir sehen, dass Lynis die Installation von **fail2ban** empfiehlt:



![Image](assets/fr/057.webp)



Im Abschnitt "**Boot und Dienste**" sehen wir, dass der Schutz der Dienste über *systemd* verbessert werden könnte. Positiv zu vermerken ist, dass Grub2 vorhanden ist und es keine Probleme mit Berechtigungen auf:



![Image](assets/fr/029.webp)



Dann gibt es die Abschnitte "**Kernel**" und "**Speicher und Prozesse**":



![Image](assets/fr/037.webp)



Als nächstes folgt der Abschnitt "**Benutzer, Gruppen und Authentifizierung**". Das Tool informiert uns über eine Warnung zu den Berechtigungen des Verzeichnisses "**/etc/sudoers.d**". Im Moment wissen wir nicht mehr, aber wir werden am Ende der Analyse sehen können, was die Empfehlung ist.



![Image](assets/fr/049.webp)



Hier sehen Sie, was Sie in den Abschnitten "**Shells", "Dateisysteme" und "USB-Geräte "** finden können. Unter anderem können wir sehen, dass es Vorschläge für Einhängepunkte gibt und dass USB-Geräte auf diesem Rechner derzeit erlaubt sind.



![Image](assets/fr/048.webp)



Danach folgen die Abschnitte: "**Dienste benennen", "Ports und Pakete", "Netzwerke".** Hier wird darauf hingewiesen, dass nicht mehr verwendete Pakete gelöscht werden können und dass es kein Dienstprogramm gibt, das automatische Aktualisierungen verwalten kann.



![Image](assets/fr/058.webp)



Wir können sehen, dass eine Firewall aktiviert ist (und ja, es gibt iptables!). Außerdem können wir sehen, dass sie ungenutzte Regeln gefunden hat und dass ein Apache-Webserver installiert ist.



![Image](assets/fr/055.webp)



Es folgt eine Analyse des Webservers selbst, da der Dienst identifiziert wurde.



Wir können sehen, dass es **Nginx**-Konfigurationsdateien gefunden hat und dass für den SSL/TLS-Teil die **Ciphers** mit der Verwendung eines Protokolls konfiguriert sind, das unsicher wäre. Andererseits ist laut Lynis die Protokollverwaltung korrekt.



![Image](assets/fr/038.webp)



Der SSH-Dienst ist auf meinem VPS-Server vorhanden. Seine Konfiguration wird von Lynis analysiert. Es muss gesagt werden, dass die SSH-Sicherheit leicht verbessert werden kann! Wir werden auf diesen Bereich im Detail zurückkommen, sobald wir die Empfehlungen erhalten haben.



![Image](assets/fr/026.webp)



Hier sind die Abschnitte **"SNMP-Unterstützung", "Datenbanken", "PHP", "Squid-Unterstützung", "LDAP-Dienste", "Protokollierung und Dateien "**.



Es gibt einen wirklich wichtigen Vorschlag zur Protokollverwaltung: Es wird dringend empfohlen, die Protokolle nicht nur lokal auf dem Rechner zu speichern. Wenn der Rechner von einem Angreifer beschädigt würde, würde er wahrscheinlich versuchen, seine Spuren zu verwischen... Wir müssen also die Protokolle auslagern.



![Image](assets/fr/050.webp)



Hier haben wir die Prüfung von gefährdeten Diensten, Kontoverwaltung, geplanten Aufgaben und NTP-Synchronisation.es wird angezeigt, dass das Niveau auf dem Banner und Identifikationsteil niedrig ist: das ist verständlich, wenn Sie die Systemversion anzeigen, gibt es einen Hinweis auf einen potenziellen Angreifer. Dies ist die Standardeinstellung.



Es wäre interessant, **auditd** zu aktivieren, um im Falle einer **forensischen** Analyse über Protokolle zu verfügen. Das **NTP** wird ebenfalls überprüft, denn für eine effiziente Suche in den Protokollen ist es besser, wenn die Systeme pünktlich sind, was die Suche vereinfacht.



![Image](assets/fr/036.webp)



Anschließend befasst sich Lynis mit kryptografischen Elements, Virtualisierung, Containern und Sicherheits-Frameworks. Einige Abschnitte sind leer, weil es keine Übereinstimmung mit dem analysierten Rechner gibt. Wir können jedoch sehen, dass ich zwei abgelaufene SSL-Zertifikate habe und **SELinux** nicht aktiviert habe.



![Image](assets/fr/027.webp)



Auch hier gibt es Verbesserungsmöglichkeiten: Es gibt keinen Anti-Virus- oder Anti-Malware-Scanner, und wir haben Vorschläge für Dateiberechtigungen.



![Image](assets/fr/028.webp)



Als Nächstes konzentriert sich Lynis auf die Straffung der Linux-Kernelkonfiguration (einschließlich der Regeln für den IPv4-Stack) sowie auf die Verwaltung der "Home"-Verzeichnisse des Linux-Rechners.



![Image](assets/fr/035.webp)



Wir sind am Ende der Analyse angelangt... Dieser letzte Punkt zeigt, dass wir von der Installation von ClamAV auf diesem Rechner nur profitieren können.



![Image](assets/fr/030.webp)



## IV. Empfehlungen



Nach dem Audit ist es an der Zeit, die Empfehlungen zu lesen und zu analysieren. Hier erhalten wir die Empfehlungen und Erklärungen für jeden der von Lynis durchgeführten Tests.



Nehmen Sie zum Beispiel die SSH-Empfehlungen. **Zu jedem Vorschlag finden Sie den empfohlenen Parameter und einen Link, der den Sicherheitspunkt erläutert ** Es liegt an Ihnen, je nach Kontext und Verwendung zu entscheiden.



Werfen wir einen Blick auf einige Beispiele von Empfehlungen, die sich direkt auf die in der Prüfung hervorgehobenen Punkte beziehen...



### A. Beispiele für Empfehlungen





- Wie wir bereits gesehen haben, ist NTP wichtig für die Zeitstempelung von Protokollen:



![Image](assets/fr/043.webp)





- Lynis schlägt außerdem vor, das Paket **apt-listbugs** zu installieren, um Informationen über kritische Fehler bei Paketinstallationen über **apt.** zu erhalten



![Image](assets/fr/041.webp)





- Das Tool schlägt vor, **needrestart zu installieren, um** zu sehen, welche Prozesse eine alte Version der Bibliothek verwenden und neu gestartet werden müssen.



![Image](assets/fr/054.webp)





- Dieser Vorschlag sieht die Installation von **fail2ban** vor, um automatisch Hosts zu blockieren, die sich nicht authentifizieren können (insbesondere durch Brute Force).



![Image](assets/fr/044.webp)





- Um die Systemdienste abzusichern, empfiehlt er, den blauen Befehl für jeden Dienst auf unserem Rechner auszuführen.



![Image](assets/fr/056.webp)





- Er schlägt vor, ein Verfallsdatum für alle geschützten Kontenpasswörter festzulegen.



![Image](assets/fr/031.webp)





- In diesem Vorschlag wird vorgeschlagen, Mindest- und Höchstwerte für das Alter eines Kennworts festzulegen. Dadurch wird u. a. sichergestellt, dass die Passwörter regelmäßig geändert werden.



![Image](assets/fr/042.webp)





- Wir empfehlen die Verwendung getrennter Partitionen, um die Auswirkungen von Speicherplatzproblemen auf einer Partition zu begrenzen.



![Image](assets/fr/047.webp)





- In dieser Empfehlung wird empfohlen, USB-Speicher und Firewire zu deaktivieren, um Datenverluste zu verhindern



![Image](assets/fr/033.webp)





- Um diese Empfehlung zu erfüllen, installieren und konfigurieren Sie einfach **unnatended-upgrade**, zum Beispiel.



![Image](assets/fr/053.webp)



### B. Installation der empfohlenen Pakete



Um die Systemkonfiguration zu verbessern, werden wir einige Pakete auf dem Rechner installieren: einige, die von Lynis empfohlen werden, einige, die ich persönlich empfehle.



Sie verfügen über eine gute Arbeitsgrundlage, wenn Sie sich ein wenig Zeit für die Konfiguration nehmen. Ziehen Sie dazu die IT-Connect-Website, andere Artikel im Internet und die Dokumentation der Tools zu Rate.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Einige Informationen über die installierten Pakete:





- Clamav** ist ein Antivirusprogramm.
- unattend-upgrades** ermöglicht es Ihnen, Ihre Aktualisierungen automatisch zu verwalten und sogar den Rechner neu zu starten oder alte Pakete automatisch zu entfernen, es ist vollständig konfigurierbar.
- rkhunter** ist ein Anti-Rootkit, das Ihr Dateisystem durchsucht.
- Fail2ban** stützt sich auf Ihre Logdateien, je nachdem, was Sie ihm zu lesen geben, und arbeitet mit **iptables**, um z.B. IP-Adressen zu sperren, die versuchen, Ihren Server per SSH zu "brute force".



### C. Empfehlungen für SSH



Werfen wir einen Blick auf die SSH-Empfehlungen. Sie sind unten aufgeführt. Keine Sorge, wir werden gleich erklären, wie man die Konfiguration verbessern kann.



![Image](assets/fr/034.webp)



Werfen wir einen genaueren Blick auf meine aktuelle **SSH**-Konfiguration in:**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



Die unten vorgeschlagene Konfiguration kann noch optimiert werden, bietet aber eine gute Grundlage. *Bitte beachten Sie, dass ich eine Reihe von Kommentaren zur besseren Lesbarkeit entfernt habe*.



Wir werden:





- Ändern Sie den SSH-Verbindungsport (vergessen Sie den Standardwert 22)
- Erhöhen Sie die Ausführlichkeitsstufe der Protokolle von **INFO auf VERBOSE**
- Setzen Sie **LoginGraceTime** auf **2 Minuten**



Wenn innerhalb von zwei Minuten keine Verbindungsinformationen eingegeben werden, wird die Verbindung getrennt.





- Aktivieren Sie **strictModes**



Legt fest, ob "sshd" die Modi und den Besitzer der Dateien des Benutzers sowie dessen Heimatverzeichnis überprüfen soll, bevor eine Verbindung bestätigt wird. Dies ist normalerweise wünschenswert, da Neulinge manchmal versehentlich ihr Verzeichnis oder ihre Dateien für alle zugänglich lassen. Die Voreinstellung ist "yes".





- Setzen Sie **MaxAuthtries** auf 3



Dies ist die Anzahl der fehlgeschlagenen Authentifizierungsversuche, bevor die Kommunikation beendet wird.





- **MaxSessions** auf 2 setzen



Dies ist die maximale Anzahl von gleichzeitigen Sitzungen.





- Aktivieren der Authentifizierung mit öffentlichem Schlüssel



```
PubkeyAuthentication yes
```





- Passwort-Authentifizierung beibehalten:



```
PasswordAuthentication yes
```



Leere Passwörter und **Kerberos**-Authentifizierung sowie **direkte Root-Authentifizierung** verbieten



```
PermitEmptyPasswords no
PermitRootLogin no
```



Stellen Sie sicher, dass Sie "**PermitRootLogin no" haben, wenn es gleich "yes" ist, ist es "absolut böse "**.





- TCP-Verbindungsumleitung verbieten



```
AllowTcpForwarding no
```



Gibt an, ob TCP-Umleitungen erlaubt sind, wobei "ja" die Standardeinstellung ist. Bitte beachten Sie: Die Deaktivierung von TCP-Umleitungen erhöht nicht die Sicherheit, wenn Benutzer Zugriff auf eine Shell haben, da sie immer noch ihre eigenen Umleitungswerkzeuge einrichten können.





- X11-Umleitung verbieten



```
X11Forwarding no
```



Gibt an, ob X11-Umleitungen akzeptiert werden, wobei "no" die Standardeinstellung ist. Bitte beachten Sie: Auch wenn X11-Umleitungen deaktiviert sind, erhöht dies nicht die Sicherheit, da Benutzer immer noch ihre eigenen Umleitungen einrichten können. Die X11-Umleitung wird automatisch deaktiviert, wenn **UseLogin** ausgewählt ist.





- Legen Sie das Zeitlimit für die Kommunikation zwischen dem Client und sshd fest



```
ClientAliveInterval  300
```



Legt eine Zeitüberschreitung in Sekunden fest, nach der der sshd-Dienst eine Nachricht sendet, um eine Antwort vom Client anzufordern, wenn keine Daten vom Client empfangen werden. Standardmäßig ist diese Option auf "0" gesetzt, was bedeutet, dass diese Nachrichten nicht an den Client gesendet werden. Nur die Version 2 des SSH-Protokolls unterstützt diese Option.



```
ClientAliveCountMax 0
```



Laut der [Dokumentation (*man page*) für sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html) bedeutet diese Option folgendes: "Legt die Anzahl der Hold-Nachrichten (siehe oben) fest, die an **sshd** gesendet werden, ohne dass eine Antwort vom Client erfolgt. Wenn dieser Schwellenwert erreicht wird, während die Hold-Nachrichten gesendet wurden, trennt **sshd** die Verbindung zum Client und beendet die Sitzung. Es ist wichtig zu beachten, dass sich diese Halte-Nachrichten von der Option **KeepAlive** (siehe unten) unterscheiden. Verbindungshaltemeldungen werden durch den verschlüsselten Tunnel gesendet und sind daher nicht fälschbar. Der durch **KeepAlive** aktivierte Verbindungserhalt auf TCP-Ebene ist fälschbar. Der Mechanismus zum Halten der Verbindung ist von Interesse, wenn der Client oder Server wissen muss, ob die Verbindung im Leerlauf ist."





- Verhinderung der Offenlegung von Informationen durch Deaktivierung von **motd, banner, lastlog**



```
PrintMotd no
```



Gibt an, ob sshd den Inhalt der Datei "/etc/motd" anzeigen soll, wenn sich ein Benutzer im interaktiven Modus anmeldet. Auf einigen Systemen kann dieser Inhalt auch von der Shell angezeigt werden, und zwar über /etc/profile oder eine ähnliche Datei. Der Standardwert ist "yes".



```
Banner none
```



Es sei darauf hingewiesen, dass in einigen Rechtsordnungen das Senden einer Nachricht vor der Authentifizierung eine Voraussetzung für den Rechtsschutz sein kann. Der Inhalt der angegebenen Datei wird an den entfernten Benutzer übermittelt, bevor die Verbindung autorisiert wird. Diese Option muss konfiguriert werden, da standardmäßig keine Nachricht angezeigt wird.



In Bildern ergibt dies:



![Image](assets/fr/019.webp)



### D. Audit-Punktzahl



Vergessen wir nicht, den **Lynis-Audit-Score** zu überprüfen! Wir sehen, dass **meine Härtungsbewertung 63** ist und dass die Berichtsdatei in "**/var/log/lynis-report.dat**" eingesehen werden kann. Außerdem gibt es die Datei "**/var/log/lynis.log**".



**Mit anderen Worten: je höher die Punktzahl, desto besser! Sie müssen also an Ihrer Konfiguration arbeiten, um die höchstmögliche Punktzahl zu erreichen, und gleichzeitig dafür sorgen, dass Ihr Rechner und die gehosteten Dienste normal funktionieren (was bedeutet, dass Sie Funktionstests durchführen müssen).



![Image](assets/fr/046.webp)



Schauen wir uns die Ergebnisse auf meinem zweiten Server an, auf dem ich etwas mehr Zeit mit dem Härten verbracht habe! Es ist also normal, dass die Punktzahl höher ist (**76**).



![Image](assets/fr/045.webp)



## V. Lynis automatisierte Planung



**Lynis** bietet auch die Möglichkeit, seine Prüfungen über eine geplante Aufgabe auszuführen. Es gibt nämlich die Option **"--cronjob "**, die alle Lynis-Tests ohne Validierung oder Benutzeraktion ausführt. Sie können dann ganz einfach ein Skript erstellen, das **Lynis** ausführt und die Ausgabe in einer Datei mit Zeitstempel und dem Namen des betreffenden Servers ablegt. Hier ist eine solche Datei, die Sie im Ordner */etc/cron.daily* ablegen können:



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



Die Variable **"AUDITOR_NAME "** ist einfach eine Variable, die wir in der Option **"--auditor "** von **Lynis** setzen, damit dieser Name im Bericht angezeigt wird:



![Image](assets/fr/059.webp)



Wir werden auch einige Kontextvariablen erstellen, die uns helfen werden, uns besser zu organisieren, wie z. B. den Hostnamen und das Datum, um den Bericht zu benennen und mit einem Zeitstempel zu versehen, und den Pfad zu dem Ordner, in dem wir unsere Berichte ablegen wollen.



## VI. Schlussfolgerung



Lynis ist ein sehr praktisches Tool, das Ihnen hilft, Zeit zu sparen und effizienter zu arbeiten, wenn Sie mehr über den Zustand der Konfiguration eines Linux-Servers wissen wollen, insbesondere im Hinblick auf die Sicherheit. Vergessen Sie jedoch nicht, dass jede Änderung getestet werden muss, bevor sie in der Produktion angewendet wird, und zwar unter Berücksichtigung Ihrer eigenen Nutzung und Ihres Kontexts.



Sie werden wahrscheinlich nicht dieselbe Konfiguration für einen VPS anwenden, der dem Netz ausgesetzt ist, wo Sie nur eine SSH-Verbindung benötigen (weil Sie die einzige Person sind, die sich verbindet), im Gegensatz zu einer **Bastion** oder einem **Scheduler**, die mehrere **SSH.**-Verbindungen benötigen



Sobald Sie eine Konfiguration gefunden haben, die Ihnen in Bezug auf die Härtung zusagt, ist es ratsam, ein Automatisierungstool zu verwenden, damit Sie die Aufgaben nicht manuell wiederholen müssen, da dies zeitaufwändig und fehleranfällig wäre. Sie können zum Beispiel ** verwenden: Puppet, Chef, Ansible, etc...**



Vergessen Sie nicht, vor der Umsetzung mit Ihren Teams zu kommunizieren: Sie müssen ihnen verständlich machen, warum Sie diese Änderungen vornehmen, und ihnen nicht nur sagen, dass Sie sie vornehmen. Letztendlich geht es darum, bewährte Verfahren weiterzugeben, und das erhöht Ihre Erfolgschancen.



Schließlich können Sie **Lynis** auch mit anderen Tools vergleichen, von denen es mehrere gibt. Wenn Sie eine zentralisierte Verwaltung anstreben und dabei Open Source bleiben wollen, empfehle ich das Tool [Wazuh] (https://wazuh.com/).



**Dieses Tutorial ist vorbei, viel Spaß mit Lynis!