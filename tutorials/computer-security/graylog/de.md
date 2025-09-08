---
name: Graylog
description: Zentralisieren und analysieren Sie Ihre Protokolle einfach
---
![cover](assets/cover.webp)



___



*Dieses Tutorial basiert auf Originalinhalten von Florian BURNEL, veröffentlicht auf [IT-Connect](https://www.it-connect.fr/). Lizenz [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Am Originaltext können Änderungen vorgenommen worden sein.*



___



## Einsatz von Graylog unter Debian 12



### I. Präsentation



Graylog ist eine quelloffene "Log Sink"-Lösung, die entwickelt wurde, um Protokolle von Ihren Maschinen und Netzwerkgeräten zu zentralisieren, zu speichern und in Echtzeit zu analysieren. In diesem Tutorial lernen wir, wie man die kostenlose Version von Graylog auf einem Debian 12 Rechner installiert!



Innerhalb eines Informationssystems erzeugt jeder **Server**, unabhängig davon, ob er unter **Linux** oder **Windows** läuft, und jedes **Netzwerkgerät** (Switch, Router, Firewall usw...) **seine eigenen Protokolle**, die lokal gespeichert werden. Mit Protokollen, die lokal auf jeder Maschine gespeichert werden, ist eine Ereignisanalyse und Korrelation sehr schwierig... An dieser Stelle kommt **Graylog** ins Spiel. Es fungiert als **Protokollsenke**, was bedeutet, dass **alle Ihre Rechner ihre Protokolle** an Graylog senden (z.B. über Syslog). Graylog **speichert und indiziert diese Protokolle** und ermöglicht Ihnen gleichzeitig die Durchführung globaler Suchen und die Erstellung von Warnmeldungen.



Graylog ist ein Analyse- und Überwachungstool, mit dem sich verdächtiges Verhalten und verschiedene Probleme (Stabilität, Leistung usw.) leichter erkennen lassen.




![Image](assets/fr/034.webp)



**Hinweis: Die kostenlose Version, **Graylog Open**, ist kein SIEM wie Wazuh, zumal ihr echte Funktionen zur Erkennung von Eindringlingen fehlen.



### II. Voraussetzungen



Der **Stack Graylog** basiert auf **mehreren Komponenten**, die wir installieren und konfigurieren müssen. Hier werden wir alle Komponenten auf demselben Server installieren, aber es ist möglich, Cluster auf Basis mehrerer Knoten zu erstellen und die Rollen auf mehrere Server zu verteilen. Für die Zwecke dieses Tutorials installieren wir **Graylog 6.1**, die bisher aktuellste Version.





- MongoDB 7**, die aktuell empfohlene Version für Graylog (mindestens 5.0.7, höchstens 7.x)
- OpenSearch**, eine von Amazon entwickelte quelloffene Fork von Elasticsearch (mindestens 1.1.x, höchstens 2.15.x)
- OpenJDK 17**



Der **Graylog-Server** läuft auf **Debian 12**, die Installation ist aber auch auf anderen Distributionen möglich, auch über Docker. Die virtuelle Maschine ist mit **8 GB RAM** und **256 GB Festplattenspeicher** ausgestattet, um genügend Ressourcen für alle Komponenten zu haben (andernfalls kann dies einen erheblichen Einfluss auf die Leistung haben). Dies ist jedoch nur ein grober Richtwert, denn **die Größe der Graylog-Architektur hängt von der Menge der zu verarbeitenden Informationen ab**. Graylog kann 30 MB oder 300 MB an Daten pro Tag verarbeiten, aber auch 300 GB an Daten pro Tag... Es handelt sich um eine **skalierbare Lösung**, die **Terabytes an Protokollen** verarbeiten kann (siehe [diese Seite] (https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Quelle: Graylog



Bevor Sie mit der Konfiguration beginnen, weisen Sie dem Graylog-Rechner eine statische IP Address zu und installieren Sie die neuesten Updates. Stellen Sie sicher, dass Sie die Zeitzone des lokalen Rechners einstellen und einen NTP-Server für die Synchronisierung von Datum und Uhrzeit definieren. Hier ist der auszuführende Befehl:



```
sudo timedatectl set-timezone Europe/Paris
```



**Hinweis: **Die Installation von OpenSearch ist optional**, wenn Sie stattdessen **Graylog Data Node** verwenden.



### III Schritt-für-Schritt-Installation von Graylog



Beginnen wir damit, den Paket-Cache zu aktualisieren und die Werkzeuge zu installieren, die wir für das Kommende benötigen.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. Installation von MongoDB



Sobald das erledigt ist, beginnen wir mit der Installation von MongoDB. Laden Sie den GPG-Schlüssel herunter, der dem MongoDB-Repository entspricht:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Fügen Sie dann das MongoDB 6-Repository auf dem Debian 12-Rechner hinzu:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Als nächstes aktualisieren wir den Paket-Cache und versuchen, MongoDB zu installieren:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



MongoDB kann nicht installiert werden, da eine Abhängigkeit fehlt: **libssl1.1**. Wir müssen dieses Paket manuell installieren, bevor wir fortfahren können, da Debian 12 es nicht in seinen Repositories hat.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Wir laden das DEB-Paket mit dem Namen "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (neueste Version) mit dem Befehl **wget** herunter und installieren es dann mit dem Befehl **dpkg**. Dies führt zu den folgenden zwei Befehlen:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Starten Sie die MongoDB-Installation neu:



```
sudo apt-get install -y mongodb-org
```



Starten Sie dann den MongoDB-Dienst neu und aktivieren Sie ihn so, dass er automatisch startet, wenn der Debian-Server gestartet wird.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



Nachdem MongoDB installiert ist, können wir mit der Installation der nächsten Komponente fortfahren.



#### B. Installation von OpenSearch



Lassen Sie uns nun mit der Installation von OpenSearch auf dem Server fortfahren. Der folgende Befehl fügt den Signaturschlüssel für OpenSearch-Pakete hinzu:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Fügen Sie dann das OpenSearch-Repository hinzu, damit wir das Paket anschließend mit **apt** herunterladen können:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Aktualisieren Sie Ihren Paket-Cache:



```
sudo apt-get update
```



Dann **installieren Sie OpenSearch** und achten Sie darauf, **das Standardpasswort für das Admin**-Konto Ihrer Instanz festzulegen. Hier lautet das Passwort "**IT-Connect2024!**", aber ersetzen Sie diesen Wert durch ein sicheres Passwort. **Vermeiden Sie schwache Passwörter** wie "**P@ssword123**" und verwenden Sie mindestens **8 Zeichen** mit mindestens einem Zeichen jedes Typs (Kleinbuchstaben, Großbuchstaben, Zahlen und Sonderzeichen), sonst wird am Ende der Installation ein Fehler angezeigt. **Dies ist eine Voraussetzung seit OpenSearch 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Bitte haben Sie während der Installation Geduld...



Wenn Sie fertig sind, nehmen Sie sich einen Moment Zeit, um die Mindestkonfiguration durchzuführen. Öffnen Sie die Konfigurationsdatei im YAML-Format:



```
sudo nano /etc/opensearch/opensearch.yml
```



Wenn die Datei geöffnet ist, stellen Sie die folgenden Optionen ein:



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



Diese OpenSearch-Konfiguration ist für die Einrichtung eines einzelnen Knotens gedacht. Hier sind einige Erläuterungen zu den verschiedenen Parametern, die wir verwenden:





- cluster.name: graylog**: dieser Parameter benennt den OpenSearch-Cluster mit dem Namen "**graylog**".
- node.name: ${HOSTNAME}**: Der Name des Knotens wird dynamisch auf den Namen des lokalen Linux-Rechners gesetzt. Auch wenn wir nur einen Knoten haben, ist es wichtig, ihn richtig zu benennen.
- pfad.Daten: /var/lib/opensearch**: Dieser Pfad gibt an, wo OpenSearch seine Daten auf dem lokalen Rechner speichert, in diesem Fall in "**/var/lib/opensearch**".
- path.logs: /var/log/opensearch**: Dieser Pfad definiert, wo OpenSearch-Protokolldateien gespeichert werden, hier in "**/var/log/opensearch**".
- discovery.type: single-node**: Dieser Parameter konfiguriert OpenSearch so, dass es mit einem einzelnen Knoten arbeitet, daher die Wahl der Option "**single-node**".
- network.host: 127.0.0.1**: Diese Konfiguration stellt sicher, dass OpenSearch nur auf seiner lokalen Interface-Schleife lauscht, was ausreichend ist, da es sich auf demselben Server wie Graylog befindet.
- action.auto_create_index: false**: Wenn Sie die automatische Indexerstellung deaktivieren, erstellt OpenSearch nicht automatisch einen Index, wenn ein Dokument ohne bestehenden Index gesendet wird.
- plugins.security.disabled: true**: Diese Option deaktiviert das OpenSearch-Sicherheits-Plugin, was bedeutet, dass es keine Authentifizierung, Zugangsverwaltung oder Kommunikationsverschlüsselung gibt. Diese Einstellung spart Zeit beim Einrichten von Graylog, sollte aber in der Produktion vermieden werden (siehe [diese Seite](https://opensearch.org/docs/1.0/security-plugin/index/)).



Einige Optionen sind bereits vorhanden, so dass Sie nur das "#" entfernen müssen, um sie zu aktivieren, und dann Ihren Wert angeben. Wenn Sie eine Option nicht finden können, können Sie sie direkt am Ende der Datei deklarieren.



![Image](assets/fr/023.webp)



Speichern und schließen Sie diese Datei.



#### C. Java (JVM) konfigurieren



Sie müssen die Java Virtual Machine, die von OpenSearch verwendet wird, konfigurieren, um die Menge an Speicher, die dieser Dienst verwenden kann, anzupassen. Bearbeiten Sie die folgende Konfigurationsdatei:



```
sudo nano /etc/opensearch/jvm.options
```



Mit der hier eingesetzten Konfiguration startet **OpenSearch mit 4 GB zugewiesenem Speicher und kann auf bis zu 4 GB** anwachsen, so dass es während des Betriebs keine Speicherschwankungen gibt. Hier berücksichtigt die Konfiguration die Tatsache, dass die virtuelle Maschine insgesamt **8 GB RAM** hat. Beide Parameter müssen den gleichen Wert haben. Das bedeutet, dass Sie die Zeilen:



```
-Xms1g
-Xmx1g
```



Mit diesen Zeilen:



```
-Xms4g
-Xmx4g
```



Hier sehen Sie ein Bild der vorzunehmenden Änderung:



![Image](assets/fr/022.webp)



Schließen Sie diese Datei, nachdem Sie sie gespeichert haben.



Darüber hinaus müssen wir die Konfiguration des Parameters "**max_map_count**" im Linux-Kernel überprüfen. Er definiert die Grenze der pro Prozess abgebildeten Speicherbereiche, um den Anforderungen unserer Anwendung gerecht zu werden. **OpenSearch** empfiehlt wie Elasticsearch**, diesen Wert auf "262144" zu setzen, um Fehler bei der Speicherverwaltung zu vermeiden.



Im Prinzip ist der Wert auf einem frisch installierten Debian 12-Rechner bereits korrekt. Aber lassen Sie uns das überprüfen. Führen Sie diesen Befehl aus:



```
cat /proc/sys/vm/max_map_count
```



Wenn Sie einen anderen Wert als "**262144**" erhalten, führen Sie den folgenden Befehl aus, andernfalls ist dies nicht erforderlich.



```
sudo sysctl -w vm.max_map_count=262144
```



Aktivieren Sie schließlich den OpenSearch-Autostart und starten Sie den zugehörigen Dienst.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Wenn Sie Ihren Systemstatus anzeigen, sollten Sie einen Java-Prozess mit 4 GB RAM sehen.



```
top
```



![Image](assets/fr/029.webp)



Nächster Schritt: die lang ersehnte Installation von Graylog!



#### D. Installation von Graylog



Um **Graylog 6.1** in seiner neuesten Version zu installieren, führen Sie die folgenden 4 Befehle aus, um **Graylog Server** herunterzuladen und zu installieren:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Danach müssen wir noch einige Änderungen an der Konfiguration von Graylog vornehmen, bevor wir versuchen, es zu starten.



Beginnen wir damit, diese beiden Optionen zu konfigurieren:





- password_secret**: Dieser Parameter wird verwendet, um einen Schlüssel zu definieren, der von Graylog verwendet wird, um die Speicherung von Benutzerpasswörtern zu sichern (im Sinne eines Salting Key). Dieser Schlüssel muss **einzigartig** und **zufällig** sein.
- root_password_sha2**: Dieser Parameter entspricht dem Standard-Administrator-Passwort in Graylog. Es wird als Hash SHA-256 gespeichert.



Wir beginnen mit der Generierung eines 96-Zeichen-Schlüssels für den Parameter **password_secret**:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Kopieren Sie den zurückgegebenen Wert und öffnen Sie dann die Graylog-Konfigurationsdatei:



```
sudo nano /etc/graylog/server/server.conf
```



Fügen Sie den Schlüssel in den Parameter **password_secret** ein, etwa so:



![Image](assets/fr/027.webp)



Speichern und schließen Sie die Datei.



Als Nächstes müssen Sie das Passwort für das standardmäßig angelegte Konto "**admin**" festlegen. In der Konfigurationsdatei muss der Hash des Passworts gespeichert werden, das heißt, er muss berechnet werden. Das folgende Beispiel gibt den Hash des Passworts "**LogsWells@**" an: Passen Sie den Wert an Ihr Passwort an.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Kopieren Sie den erhaltenen Wert als Ausgabe (ohne den Bindestrich am Ende der Zeile).



Öffnen Sie die Graylog-Konfigurationsdatei erneut:



```
sudo nano /etc/graylog/server/server.conf
```



Fügen Sie den Wert in die Option **root_password_sha2** wie folgt ein:



![Image](assets/fr/026.webp)



Setzen Sie in der Konfigurationsdatei die Option "**http_bind_address**". Geben Sie "**0.0.0.0:9000**" an, damit das Graylog-Web von Interface über Port **9000** über einen beliebigen Server IP Address erreicht werden kann.



![Image](assets/fr/024.webp)



Setzen Sie dann die Option "**elasticsearch_hosts**" auf "http://127.0.0.1:9200", um unsere lokale OpenSearch-Instanz zu deklarieren. Dies ist notwendig, da wir keinen **Graylog Data Node** verwenden. Und ohne diese Option ist es nicht möglich, weiterzumachen...



![Image](assets/fr/025.webp)



Speichern und schließen Sie die Datei.



Dieser Befehl aktiviert Graylog, so dass es beim nächsten Booten automatisch gestartet wird, und startet sofort den Graylog-Server.



```
sudo systemctl enable --now graylog-server
```



Versuchen Sie anschließend, über einen Browser eine Verbindung zu Graylog herzustellen. Geben Sie die IP Address (oder den Namen) des Servers und Port 9000 ein.



**Zu Ihrer Information:**



Vor nicht allzu langer Zeit erschien bei der ersten Anmeldung bei Graylog ein Authentifizierungsfenster ähnlich dem unten abgebildeten. Sie mussten Ihr Login "**admin**" und Ihr Passwort eingeben. Und dann waren Sie unangenehm überrascht, dass die Verbindung nicht funktionierte.



![Image](assets/fr/031.webp)



Es war notwendig, die Befehlszeile des Graylog-Servers aufzurufen und die Protokolle einzusehen. Wir konnten dann sehen, dass **für die erste Verbindung** ein **vorläufiges Passwort** verwendet werden muss, das in den Protokollen angegeben ist.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Sie mussten dann eine erneute Verbindung mit dem Benutzer "**admin**" und dem vorläufigen Kennwort versuchen, und schon konnten Sie sich anmelden!



**Dies ist nicht mehr der Fall. Sie müssen sich nur noch mit Ihrem Admin-Konto und dem in der Befehlszeile konfigurierten Passwort anmelden



![Image](assets/fr/033.webp)



**Willkommen bei Graylogs Interface!



![Image](assets/fr/019.webp)



#### E. Graylog: Erstellen eines neuen Administratorkontos



Anstatt das von Graylog nativ erstellte Administratorkonto zu verwenden, können Sie Ihr eigenes persönliches Administratorkonto erstellen. Klicken Sie auf das Menü "**System**", dann auf "**Benutzer und Teams**" und klicken Sie auf die Schaltfläche "**Benutzer erstellen**". Füllen Sie dann das Formular aus und weisen Sie Ihrem Konto die Administratorrolle zu.



![Image](assets/fr/020.webp)



Ein personalisiertes Konto kann, anders als ein natives Administratorkonto, zusätzliche Informationen wie Vor- und Nachname und E-Mail Address enthalten. Außerdem wird dadurch eine bessere Nachvollziehbarkeit gewährleistet, wenn jede Person mit einem benannten Konto arbeitet.



## Protokolle mit rsyslog an Graylog senden



### I. Präsentation



In diesem zweiten Teil werden wir lernen, wie man einen Linux-Rechner so konfiguriert, dass er seine Protokolle an einen Graylog-Server sendet. Zu diesem Zweck installieren und konfigurieren wir Rsyslog auf dem System.



### II. Konfigurieren von Graylog für den Empfang von Linux-Protokollen



Wir beginnen mit der Konfiguration von Graylog. Es sind drei Schritte zu erledigen:





- Die Erstellung eines **Eingangs**, um einen Einstiegspunkt zu schaffen, der es Linux-Rechnern ermöglicht, **Syslog-Protokolle über UDP** zu senden.
- Die Erstellung eines neuen **Index** zum Speichern und **Indizieren aller Linux-Protokolle**.
- Erstellung eines **Streams**, um die von Graylog empfangenen Protokolle in den neuen Linux-Index **zu leiten**.



#### A. Einen Eingang für Syslog erstellen



Melden Sie sich bei Graylog Interface an, klicken Sie im Menü auf "**System**" und dann auf "**Eingänge**". Wählen Sie in der Dropdown-Liste "**Syslog UDP**" und klicken Sie dann auf die Schaltfläche "**Neuen Eingang starten**". Es ist auch möglich, einen TCP-Syslog-Eingang zu erstellen, aber dies erfordert die Verwendung eines TLS-Zertifikats: ein Plus für die Sicherheit, aber in diesem Artikel nicht behandelt.



![Image](assets/fr/001.webp)



Ein Assistent wird auf dem Bildschirm erscheinen. Geben Sie diesem Eingang zunächst einen Namen, z. B. "**Graylog_UDP_Rsyslog_Linux**", und wählen Sie einen Port. Standardmäßig ist der Port "**514**", aber Sie können ihn anpassen. Hier ist der Port "**12514**" ausgewählt.



![Image](assets/fr/016.webp)



Sie können auch die Option "**Vollständige Meldung speichern**" ankreuzen, um die vollständige Protokollmeldung in Graylog zu speichern. Klicken Sie auf "**Eingabe starten**".



![Image](assets/fr/017.webp)



Der neue Eingang wurde erstellt und ist jetzt aktiv. Graylog kann jetzt Syslog-Protokolle auf Port 12514/UDP empfangen, aber wir haben die Konfiguration der Anwendung noch nicht abgeschlossen.



![Image](assets/fr/018.webp)


**Hinweis: Ein einziger Input kann zum Speichern von Protokollen von mehreren Linux-Rechnern verwendet werden.



#### B. Erstellen Sie einen neuen Linux-Index



Wir müssen einen Index in Graylog erstellen, um Protokolle von Linux-Rechnern zu speichern. Ein **Index** in Graylog ist eine Speicherstruktur, die die empfangenen Protokolle, d.h. die empfangenen Nachrichten, enthält. Graylog verwendet OpenSearch als Speichermaschine, und die Nachrichten werden indiziert, um eine schnelle und effiziente Suche zu ermöglichen.



Klicken Sie in Graylog im Menü auf "**System**" und dann auf "**Indizes**". Auf der neu erscheinenden Seite klicken Sie auf "**Indexsatz erstellen**".



![Image](assets/fr/005.webp)



Benennen Sie diesen Index, zum Beispiel "**Linux Index**", fügen Sie eine Beschreibung und ein Präfix hinzu, bevor Sie bestätigen. Hier werden wir **alle Linux-Protokolle in diesem Index** speichern. Es ist auch möglich, spezifische Indizes zu erstellen, um nur bestimmte Protokolle zu speichern (nur [SSH]-Protokolle (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), Webservice-Protokolle, usw.).



![Image](assets/fr/006.webp)



Nun müssen wir einen neuen Stream erstellen, um Nachrichten an diesen Index weiterzuleiten.



#### C. Einen Stream erstellen



Um einen neuen Stream zu erstellen, klicken Sie im Hauptmenü von Graylog auf "**Streams**". Klicken Sie dann auf die Schaltfläche "**Stream erstellen**" auf der rechten Seite. In dem nun erscheinenden Fenster geben Sie dem Stream einen Namen, z.B. "**Linux Stream**" und wählen den Index "**Linux Index**" für das Feld "**Index Set**". Bestätigen Sie Ihre Wahl.



**Hinweis: Nachrichten, die diesem Stream entsprechen, werden auch in den "**Standard-Stream**" aufgenommen, es sei denn, Sie aktivieren die Option "**Treffer aus 'Standard-Stream'** entfernen".



![Image](assets/fr/002.webp)



Klicken Sie dann in Ihren Steam-Einstellungen auf die Schaltfläche "**Stream-Regel hinzufügen**", um eine neue Regel für die Nachrichtenweiterleitung hinzuzufügen. Wenn Sie dieses Fenster nicht finden können, klicken Sie im Menü auf "**Streams**", dann in der Zeile, die Ihrem Stream entspricht, auf "**Mehr**" und dann auf "**Regeln verwalten**".



Wählen Sie den Typ "**Match input**" und wählen Sie den zuvor erstellten **Rsyslog input in UDP**. Bestätigen Sie mit der Schaltfläche "**Regel erstellen**". Alle Nachrichten an unseren neuen Eingang werden nun an den Index für Linux gesendet.



![Image](assets/fr/003.webp)



Ihr neuer Stream sollte in der Liste erscheinen und sich im Status "**Running**" befinden. Die Nachrichtenbandbreite zeigt "**0 msg/s**" an, da wir derzeit keine Protokolle an den Rsyslog UDP-Eingang senden. Um die Protokolle eines Streams anzuzeigen, klicken Sie einfach auf seinen Namen.



![Image](assets/fr/004.webp)



**Auf der Graylog-Seite ist alles bereit**. Der nächste Schritt ist die Konfiguration des Linux-Rechners.



### III. Installieren und Konfigurieren von Rsyslog unter Linux



Melden Sie sich auf dem Linux-Rechner an, entweder lokal oder per Fernzugriff, und verwenden Sie ein Benutzerkonto mit der Berechtigung, seine Rechte zu erweitern (über sudo). Andernfalls verwenden Sie direkt das "root"-Konto.



#### A. Installieren des Rsyslog-Pakets



Aktualisieren Sie zunächst den Paket-Cache und installieren Sie das Paket mit dem Namen "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



Prüfen Sie dann den Status des Dienstes. In den meisten Fällen wird er bereits ausgeführt.



```
sudo systemctl status rsyslog
```



#### B. Rsyslog konfigurieren



Rsyslog hat eine Hauptkonfigurationsdatei, die sich hier befindet:



```
/etc/rsyslog.conf
```



Darüber hinaus werden im Verzeichnis "**/etc/rsyslog.d/**" zusätzliche Konfigurationsdateien für Rsyslog gespeichert. In der Hauptkonfigurationsdatei gibt es eine Include-Anweisung, um alle "**.conf**"-Dateien zu importieren, die sich in diesem Verzeichnis befinden. Damit ist es möglich, zusätzliche Dateien zur Konfiguration von Rsyslog zu haben, ohne die Hauptdatei zu verändern.



In diesem Verzeichnis müssen Sie Zahlen verwenden, um die Reihenfolge des Ladens festzulegen, da die Dateien in alphabetischer Reihenfolge geladen werden. Durch Hinzufügen eines numerischen Präfixes können Sie die Priorität zwischen mehreren Konfigurationsdateien verwalten. Da wir hier nur eine zusätzliche Datei haben, stellt dies kein Problem dar.



In diesem Verzeichnis erstellen wir eine Datei mit dem Namen "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



Fügen Sie in diese Datei die folgende Zeile ein:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Diese Zeile ist folgendermaßen zu interpretieren:





- `*.*`: bedeutet, dass alle Syslog-Protokolle des Linux-Rechners an Graylog gesendet werden.
- @": gibt an, dass der Transport in UDP erfolgt. Sie müssen "**@@**" angeben, um zu TCP zu wechseln.
- 192.168.10.220:12514": gibt den Address des Graylog-Servers und den Port an, über den die Protokolle gesendet werden (entspricht dem Input).
- rSYSLOG_SyslogProtocol23Format": entspricht dem Format der an Graylog zu sendenden Nachrichten.



Wenn Sie fertig sind, speichern Sie die Datei und starten Sie Rsyslog neu.



```
sudo systemctl restart rsyslog.service
```



Nach dieser Aktion sollten die ersten Nachrichten auf Ihrem Graylog-Server eintreffen!



### IV. Anzeige von Linux-Protokollen in Graylog



In Graylog können Sie auf "**Streams**" klicken und Ihren neuen Stream auswählen, um zugehörige Nachrichten anzuzeigen. Alternativ können Sie auch auf "**Suchen**" klicken, Ihren Steam auswählen und eine Suche starten.



Hier sind einige der wichtigsten Merkmale des Interface:



**1** - Wählen Sie den Zeitraum, für den die Nachrichten angezeigt werden sollen. Standardmäßig werden die Nachrichten der letzten 5 Minuten angezeigt.



**2** - Wählen Sie den/die anzuzeigenden Stream(s).



**3** - Aktivieren Sie die automatische Aktualisierung der Nachrichtenliste (z. B. alle 5 Sekunden). Andernfalls ist sie statisch und Sie müssen sie manuell aktualisieren.



**4** - Klicken Sie auf die Lupe, um die Suche zu starten, nachdem Sie den Zeitraum, den Stream oder den Filter geändert haben.



**5** - Eingabeleiste zur Angabe Ihrer Suchfilter. Hier gebe ich "**Quelle:srv\-docker**" an, um nur die Protokolle des neuen Rechners anzuzeigen, auf dem ich gerade Rsyslog eingerichtet habe.



Die Protokolle werden vom Linux-Rechner gesendet:



![Image](assets/fr/015.webp)



### V. Erkennen eines SSH-Verbindungsfehlers



Die Stärke von Graylog liegt in seiner Fähigkeit, Protokolle zu indizieren und die Suche nach verschiedenen Kriterien zu ermöglichen: Quellcomputer, Timestamp, Nachrichteninhalt usw... Wir könnten versuchen, fehlgeschlagene SSH-Verbindungen zu identifizieren.



Versuchen Sie, von einem entfernten Rechner aus (z. B. dem Graylog-Server) eine Verbindung zu Ihrem Linux-Server herzustellen, auf dem Sie gerade Rsyslog konfiguriert haben. Zum Beispiel:



```
ssh [email protected]
```



Geben Sie dann absichtlich einen falschen **Benutzernamen** und **Passwort** ein, um **generate-Verbindungsfehler** zu verursachen. In der Datei "**/var/log/auth.log**" werden dann generate-Protokollmeldungen ähnlich der folgenden angezeigt:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Sie sollten diese Meldungen auf Graylog finden.



Verwenden Sie bei Graylog den folgenden Suchfilter, um nur übereinstimmende Meldungen anzuzeigen:



```
message:Failed password AND application_name:sshd
```



Wenn Sie mehrere Server haben und die Protokolle eines bestimmten Servers analysieren möchten, geben Sie zusätzlich dessen Namen an:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Hier ist ein Überblick über das Ergebnis auf einem Rechner, auf dem ich mehrere Verbindungsfehler zu verschiedenen Tageszeiten erzeugt habe:



![Image](assets/fr/009.webp)



Erfolglose Verbindungsversuche werden von dem Rechner mit der IP Address "**192.168.10.199**" unternommen. Wenn Sie mehr über die Aktivität dieses Rechners wissen wollen, können Sie nach dieser IP Address** suchen. Graylog wird alle Protokolle ausgeben, in denen auf diese IP Address verwiesen wird, und zwar auf allen Hosts (für die das Senden von Protokollen konfiguriert ist).



In diesem Fall kann der zu verwendende Filter sein:



```
message:"192.168.10.199"
```



Wir erhalten zusätzliche Ergebnisse (nicht überraschend, da wir die SSH-Anwendung nicht filtern):



![Image](assets/fr/008.webp)



### VI. Schlussfolgerung



Wenn Sie diese Anleitung befolgen, sollten Sie in der Lage sein, einen Linux-Rechner so zu konfigurieren, dass er seine Logs an einen Graylog-Server sendet. Auf diese Weise können Sie die Logs Ihrer Linux-Hosts in Ihrer Log-Senke zentralisieren!



Wenn Sie noch weiter gehen wollen, können Sie Dashboards und Warnmeldungen erstellen, um eine Benachrichtigung zu erhalten, wenn eine Anomalie entdeckt wird.



![Image](assets/fr/007.webp)