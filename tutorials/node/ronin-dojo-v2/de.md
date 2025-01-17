---
name: RoninDojo v2
description: Installation deines RoninDojo v2 Bitcoin-Knotens auf einem Raspberry Pi
---
![cover RoninDojo v2](assets/cover.webp)

***WARNUNG:** Nach der Verhaftung der Gründer von Samourai Wallet und der Beschlagnahme ihrer Server am 24. April sind bestimmte Funktionen von RoninDojo, wie Whirlpool, nicht mehr funktionsfähig. Es besteht jedoch die Möglichkeit, dass diese Werkzeuge in den kommenden Wochen wieder in Betrieb genommen oder anders neu gestartet werden. Da der Code von RoninDojo auf dem GitLab von Samourai gehostet wurde, das ebenfalls beschlagnahmt wurde, ist es derzeit nicht möglich, den Code aus der Ferne herunterzuladen. Die Teams von RoninDojo arbeiten wahrscheinlich an einer erneuten Veröffentlichung des Codes.*

_Wir verfolgen die Entwicklungen in diesem Fall sowie die Entwicklungen bezüglich der zugehörigen Tools genau. Seien Sie versichert, dass wir dieses Tutorial aktualisieren werden, sobald neue Informationen verfügbar sind._

_Dieses Tutorial wird nur zu Bildungs- und Informationszwecken bereitgestellt. Wir befürworten oder ermutigen die Verwendung dieser Tools zu kriminellen Zwecken nicht. Es liegt in der Verantwortung jedes Benutzers, die Gesetze in seiner Gerichtsbarkeit zu beachten._

---

> "*Nutze Bitcoin mit Privatsphäre.*"

In einem vorherigen Tutorial hatten wir bereits das Verfahren zur Installation und Nutzung von RoninDojo v1 erklärt. Im letzten Jahr jedoch haben die RoninDojo-Teams Version 2 ihrer Implementierung herausgebracht, was einen signifikanten Wendepunkt in der Softwarearchitektur markierte. Tatsächlich wechselten sie von der Linux Manjaro-Distribution zu Debian. Folglich bieten sie kein vorkonfiguriertes Image mehr für die automatische Installation auf dem Raspberry Pi an. Es gibt jedoch immer noch eine Methode für die manuelle Installation. Diese habe ich für meinen eigenen Knoten verwendet, und seitdem funktioniert RoninDojo v2 wunderbar auf meinem Raspberry Pi 4. Daher biete ich ein neues Tutorial an, wie man RoninDojo v2 manuell auf einem Raspberry Pi installiert.

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0



## Inhaltsverzeichnis:
- Was ist RoninDojo?
- Welche Hardware sollte man für die Installation von RoninDojo v2 wählen?
- Wie montiert man den Raspberry Pi 4?
- Wie installiert man RoninDojo v2 auf einem Raspberry Pi 4?
- Wie nutzt man seinen RoninDojo v2 Knoten?

## Was ist RoninDojo?
Dojo ist ursprünglich eine vollständige Bitcoin-Knoten-Implementierung, basierend auf Bitcoin Core, und entwickelt von den Teams des Samourai Wallets. Diese Lösung kann auf jeder Ausrüstung installiert werden. Im Gegensatz zu anderen Core-Implementierungen wurde Dojo speziell optimiert, um sich in die Android-Anwendungsumgebung von Samourai Wallet zu integrieren. RoninDojo ist ein Hilfsprogramm, das die Installation und Verwaltung eines Dojo sowie verschiedener anderer ergänzender Tools erleichtert. Kurz gesagt, RoninDojo bereichert die Basisimplementierung von Dojo durch die Integration einer Vielzahl zusätzlicher Tools, während es dessen Installation und Verwaltung vereinfacht.

Ronin bietet auch [eine Node-in-Box-Lösung, genannt "*Tanto*"](https://ronindojo.io/en/products), ein Gerät mit bereits auf einem von ihrem Team zusammengestellten System installiertem RoninDojo. Der Tanto ist eine kostenpflichtige Option, die für diejenigen interessant sein könnte, die technische Komplikationen vermeiden möchten. Da der Quellcode von RoninDojo jedoch offen ist, ist es auch möglich, ihn auf eigener Hardware zu implementieren. Diese Alternative, die wirtschaftlicher ist, erfordert dennoch einige zusätzliche Handgriffe, die wir in diesem Tutorial behandeln werden.
RoninDojo ist ein Dojo, es ermöglicht also die einfache Integration von Whirlpool CLI in deinen Bitcoin-Knoten, um das bestmögliche Coinjoin-Erlebnis zu bieten. Mit Whirlpool CLI wird es möglich, deine Bitcoins kontinuierlich zu remixen, 24 Stunden am Tag, 7 Tage die Woche, ohne dass dein persönlicher Computer eingeschaltet bleiben muss.

Über Whirlpool CLI hinaus umfasst RoninDojo eine Vielzahl von Tools, um die Funktionalitäten deines Dojos zu erweitern. Unter diesen analysiert der Boltzmann-Rechner das Datenschutzniveau deiner Transaktionen, der Electrum-Server ermöglicht die Verbindung deiner Bitcoin-Wallets mit deinem Knoten, und der Mempool-Server ermöglicht es dir, deine Transaktionen lokal anzusehen, ohne Informationen preiszugeben.
Im Vergleich zu anderen Node-Lösungen wie Umbrel ist RoninDojo eindeutig auf On-Chain-Lösungen und Datenschutztools fokussiert. Anders als Umbrel unterstützt RoninDojo weder das Einrichten eines Lightning-Nodes noch die Integration von allgemeineren Serveranwendungen. Obwohl RoninDojo weniger vielseitige Tools als Umbrel bietet, verfügt es über alle wesentlichen Funktionen zur Verwaltung Ihrer On-Chain-Aktivitäten.
Wenn Sie keine allgemeinen Funktionen oder solche, die mit dem Lightning-Netzwerk in Verbindung stehen, wie sie von Umbrel angeboten werden, benötigen und nach einem einfachen, stabilen Node mit wesentlichen Tools wie Whirlpool oder Mempool suchen, könnte RoninDojo die ideale Lösung sein. Während Umbrel dazu tendiert, ein Mini-Multitasking-Server zu werden, der auf das Lightning-Netzwerk und Vielseitigkeit ausgerichtet ist, konzentriert sich RoninDojo, in Übereinstimmung mit der Philosophie von Samourai Wallet, auf grundlegende Tools für die Privatsphäre der Nutzer.

Nun, da wir RoninDojo umrissen haben, sehen wir uns gemeinsam an, wie man diesen Node einrichtet.

## Welche Hardware sollte man für die Installation von RoninDojo v2 wählen?
RoninDojo bietet ein Image für die automatische Installation seiner Software auf einem [RockPro64](https://ronindojo.io/en/download) an. Unser Tutorial konzentriert sich jedoch auf das manuelle Installationsverfahren auf einem Raspberry Pi 4. Obwohl der Raspberry Pi 5 kürzlich eingeführt wurde und dieses Tutorial theoretisch mit diesem neuen Modell kompatibel sein sollte, hatte ich noch nicht die Gelegenheit, es persönlich zu testen, und ich habe kein Feedback aus der Community gefunden. Sobald ich den Pi 5 und kompatible Komponenten erwerbe, werde ich dieses Tutorial aktualisieren, um Sie informiert zu halten. In der Zwischenzeit empfehle ich, den Pi 4 zu priorisieren, da er für meinen Node perfekt funktioniert.
Ich betreibe RoninDojo auf einem Raspberry Pi mit 8 GB RAM. Obwohl einige Mitglieder der Community es geschafft haben, es auf Geräten mit nur 4 GB RAM zum Laufen zu bringen, habe ich diese Konfiguration selbst nicht getestet. Angesichts des geringen Preisunterschieds scheint es klug, sich für die Version mit 8 GB RAM zu entscheiden. Dies könnte sich auch als nützlich erweisen, wenn Sie planen, Ihren Raspberry Pi in Zukunft für andere Zwecke zu verwenden.
Es ist wichtig zu beachten, dass die Teams von RoninDojo häufig Probleme im Zusammenhang mit dem Gehäuse und dem SSD-Adapter gemeldet haben. Ich habe diese Probleme selbst erlebt. **Daher wird dringend empfohlen, Gehäuse mit einem USB-Kabel für die SSD Ihres Nodes zu vermeiden.** Bevorzugen Sie stattdessen eine Speichererweiterungskarte, die speziell für Ihren Raspberry Pi entwickelt wurde:

![Speichererweiterungskarte RPI4](assets/notext/1.webp)

Um die Bitcoin-Blockchain zu speichern, benötigen Sie eine SSD, die mit der von Ihnen gewählten Speichererweiterungskarte kompatibel ist. Derzeit (Februar 2024) befinden wir uns in einer Übergangsphase. Es wird erwartet, dass in einigen Monaten 1 TB Festplatten nicht mehr ausreichen werden, um die wachsende Größe der Blockchain zu speichern, insbesondere unter Berücksichtigung der verschiedenen Anwendungen, die Sie in Ihren Node integrieren möchten. Einige empfehlen daher, in eine 2 TB SSD zu investieren, um langfristig Ruhe zu haben. Allerdings, mit dem jährlichen Abwärtstrend der SSD-Preise, schlagen andere vor, sich mit einer 1 TB Festplatte zu begnügen, die für ein oder zwei Jahre ausreichen sollte, mit dem Argument, dass bis zum Zeitpunkt ihrer Obsoleszenz die Kosten für 2 TB Modelle wahrscheinlich gesunken sein werden. Die Wahl hängt also von Ihren persönlichen Vorlieben ab. Wenn Sie planen, Ihren RoninDojo für eine signifikante Dauer zu behalten und jegliche technische Handhabung in den kommenden Jahren vermeiden möchten, scheint die Option einer 2 TB SSD die vorsichtigste zu sein, da sie Ihnen einen komfortablen Spielraum für die Zukunft bietet.

Zusätzlich benötigen Sie verschiedene kleine Komponenten:
- Ein Gehäuse mit einem Lüfter, um Ihren Raspberry Pi und Ihre Speichererweiterungskarte zu beherbergen. Kits, die sowohl die SSD-Erweiterungskarte als auch ein kompatibles Gehäuse enthalten, sind online verfügbar;
- Ein Stromkabel für Ihren Raspberry Pi;
- Eine micro SD-Karte mit mindestens 16 GB (obwohl technisch gesehen 8 GB ausreichen könnten, ist der Preisunterschied zwischen 8- und 16-GB-Karten oft vernachlässigbar);
- Ein RJ45-Ethernet-Kabel für die Netzwerkverbindung.

![node material](assets/notext/2.webp)

## Wie montiert man den Raspberry Pi 4?
Die Montage Ihres Knotens variiert je nach gewählter Hardware, insbesondere dem Typ des Gehäuses. Die allgemeine Vorgehensweise bei der Montage bleibt jedoch im Großen und Ganzen ähnlich.
Beginnen Sie damit, Ihre SSD auf der Speichererweiterungskarte zu installieren, wobei Sie darauf achten, die beiden Sicherungsschrauben hinten festzuziehen.

![assembly1](assets/notext/3.webp)

Befestigen Sie dann Ihren Raspberry Pi an der Erweiterungskarte.

![assembly2](assets/notext/4.webp)

Befestigen Sie auch den Lüfter am Raspberry Pi.

![assembly3](assets/notext/5.webp)

Verbinden Sie die verschiedenen Komponenten, achten Sie darauf, die richtigen Pins zu verwenden, indem Sie sich auf das Handbuch Ihres Gehäuses beziehen. Gehäusehersteller bieten oft Video-Tutorials an, um Sie bei der Montage zu unterstützen. In meinem Fall habe ich eine zusätzliche Erweiterungskarte mit einem Ein-/Ausschalter. Dies ist nicht wesentlich für die Erstellung eines Bitcoin-Knotens. Ich verwende es hauptsächlich, um einen Stromschalter zu haben.

Wenn Sie, wie ich, eine Erweiterungskarte mit einem Ein-/Ausschalter haben, vergessen Sie nicht, den kleinen "Auto Power On"-Jumper zu installieren. Dies ermöglicht es Ihrem Knoten, automatisch zu starten, sobald er mit Strom versorgt wird. Diese Funktion ist besonders nützlich im Falle eines Stromausfalls, da sie es Ihrem Knoten ermöglicht, von selbst neu zu starten, ohne dass Sie manuell eingreifen müssen.

![assembly4](assets/notext/6.webp)

Bevor Sie die gesamte Hardware in das Gehäuse einsetzen, ist es wichtig, die ordnungsgemäße Funktion Ihres Raspberry Pi, der Speichererweiterungskarte und des Lüfters durch Einschalten zu überprüfen.

![assembly5](assets/notext/7.webp)

Installieren Sie schließlich Ihren Raspberry Pi in seinem Gehäuse. Beachten Sie, dass ein späterer Schritt das Hinzufügen der micro SD-Karte in den entsprechenden Port am Raspberry Pi erfordert. Wenn Ihr Gehäuse mit einer Öffnung ausgestattet ist, die es Ihnen ermöglicht, die SD-Karte einzusetzen, ohne es öffnen zu müssen (wie es bei meinem der Fall ist, wie auf dem Foto dargestellt), können Sie das Gehäuse jetzt schließen. Wenn Ihr Gehäuse jedoch keinen direkten Zugang zum micro SD-Port hat, müssen Sie warten, bis Sie die micro SD-Karte vorbereitet haben, um sie einzusetzen, bevor Sie die Montage abschließen.

![assembly6](assets/notext/8.webp)

## Wie installiert man RoninDojo v2 auf einem Raspberry Pi 4?

### Schritt 1: Vorbereiten der bootfähigen micro SD
Nachdem Sie Ihre Hardware montiert haben, ist der nächste Schritt die Installation von RoninDojo. Dafür werden wir eine bootfähige micro SD-Karte von Ihrem Computer aus vorbereiten, indem wir das entsprechende Disk-Image darauf brennen.
Sie müssen die _**Raspberry Pi Imager**_-Software verwenden, die speziell dafür entwickelt wurde, das Herunterladen, Konfigurieren und Schreiben von Betriebssystemen auf einer micro SD-Karte für die Verwendung mit einem Raspberry Pi zu erleichtern. Beginnen Sie damit, diese Software auf Ihrem persönlichen PC zu installieren:
- Für Ubuntu/Debian: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- Für Windows: https://downloads.raspberrypi.org/imager/imager_latest.exe
- Für Mac: https://downloads.raspberrypi.org/imager/imager_latest.dmg
Sobald die Software installiert ist, öffnen Sie sie und stecken Sie Ihre Micro-SD-Karte in Ihren persönlichen Computer. Wählen Sie im Raspberry Pi Imager Interface `CHOOSE OS` aus:
![choose OS](assets/notext/9.webp)

Als Nächstes gehen Sie zum Menü `Raspberry Pi OS (other)`:

![choose OS others](assets/notext/10.webp)

Wählen Sie das Betriebssystem `Raspberry Pi OS (Legacy, 64-bit) Lite`, welches `0.3 GB` groß ist:

![choose OS Legacy Lite](assets/notext/11.webp)

Nachdem Sie das Betriebssystem ausgewählt haben, werden Sie zum Hauptmenü des Raspberry Pi Imagers weitergeleitet. Klicken Sie auf `CHOOSE STORAGE`:

![choose storage](assets/notext/12.webp)

Wählen Sie Ihre Micro-SD-Karte aus:

![choose micro sd](assets/notext/13.webp)

Nachdem Sie das Betriebssystem und die Micro-SD-Karte ausgewählt haben, klicken Sie auf `NEXT`:

![choose next](assets/notext/14.webp)

Ein neues Fenster wird erscheinen. Wählen Sie `EDIT CONFIGURATION`:

![edit settings](assets/notext/15.webp)

In diesem Fenster gehen Sie zum Reiter `GENERAL` und nehmen Sie die folgenden Einstellungen vor (die sehr wichtig sind, damit es funktioniert):
- Aktivieren Sie die Option und weisen Sie `RoninDojo` als Hostnamen zu;
- Aktivieren Sie `Set username and password`, geben Sie `pi` als Benutzernamen ein, wählen Sie ein Passwort und notieren Sie diese Informationen, da sie später benötigt werden. Diese Anmeldeinformationen sind temporär und werden danach gelöscht;
- Deaktivieren Sie `Configure Wi-Fi`;
- Aktivieren Sie `Set locale settings` und wählen Sie Ihre Zeitzone sowie den Tastaturtyp, der Ihrem Computer entspricht;

![general settings](assets/notext/16.webp)

Im Reiter SERVICES klicken Sie auf das Feld `Enable SSH` und wählen Sie `Use a password for authentication`:

![services settings](assets/notext/17.webp)

Stellen Sie außerdem sicher, dass im Reiter `OPTIONS` die Telemetrie deaktiviert ist:

![options settings](assets/notext/18.webp)

Klicken Sie auf `SAVE`:

![settings save](assets/notext/19.webp)
Bestätigen Sie mit `YES`, um die Erstellung der bootfähigen Micro-SD-Karte zu starten:
![settings yes](assets/notext/20.webp)

Eine Nachricht wird Sie informieren, dass alle Daten auf der Micro-SD-Karte gelöscht werden. Bestätigen Sie mit `YES`, um den Prozess zu starten:

![overwrite micro SD](assets/notext/21.webp)

Warten Sie, bis die Software die Vorbereitung Ihrer Micro-SD-Karte abgeschlossen hat:

![writing micro SD](assets/notext/22.webp)

Wenn die Nachricht erscheint, die das Ende des Prozesses anzeigt, können Sie die Micro-SD-Karte aus Ihrem Computer entfernen:

![writing micro SD completed](assets/notext/23.webp)

### Schritt 2: Vervollständigen Sie den Aufbau des Knotens
Sie können nun die Micro-SD-Karte in den entsprechenden Port Ihres Raspberry Pi einsetzen.

![micro SD](assets/notext/24.webp)

Verbinden Sie dann Ihren Raspberry Pi mit Ihrem Router, indem Sie das Ethernet-Kabel verwenden. Schließlich schalten Sie Ihren Knoten ein, indem Sie das Stromkabel anschließen und den Einschaltknopf drücken (falls Ihr Setup einen solchen enthält).

### Schritt 3: Eine SSH-Verbindung mit dem Knoten herstellen
Zuerst ist es notwendig, die IP-Adresse Ihres Knotens zu finden. Sie haben die Möglichkeit, ein Tool wie _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ oder _[Angry IP Scanner](https://angryip.org/)_ zu verwenden, oder die Administrations-Oberfläche Ihres Routers zu überprüfen. Die IP-Adresse sollte im Format `192.168.1.??` sein. **Ersetzen Sie für alle folgenden Befehle `[IP]` durch die tatsächliche IP-Adresse Ihres Knotens**, (entfernen Sie die Klammern).

Starten Sie ein Terminal.
Um einen möglichen Schlüssel zu entfernen, der bereits mit der IP-Adresse Ihres Knotens verknüpft ist, führen Sie den Befehl aus: `ssh-keygen -R [IP]`.

Ein Fehler nach diesem Befehl ist nicht schwerwiegend; es bedeutet einfach, dass der Schlüssel nicht in Ihrer Liste bekannter Hosts existiert (was ziemlich wahrscheinlich ist). Wenn beispielsweise die IP Ihres Knotens `192.168.1.40` ist, wird der Befehl zu: `ssh-keygen -R 192.168.1.40`.

Als Nächstes, stellen Sie eine SSH-Verbindung mit Ihrem Knoten her, indem Sie den Befehl ausführen:
`ssh pi@[IP]`.
Eine Nachricht wird bezüglich der Authentizität des Hosts erscheinen: `The authenticity of host '[IP]' can't be established.` Dies deutet darauf hin, dass die Authentizität des Geräts, zu dem Sie eine Verbindung herstellen möchten, aufgrund eines fehlenden bekannten öffentlichen Schlüssels nicht verifiziert werden kann. Wenn Sie zum ersten Mal über SSH eine Verbindung zu einem neuen Host herstellen, wird diese Nachricht immer erscheinen. Sie müssen `yes` antworten, um dessen öffentlichen Schlüssel zu Ihrem lokalen Verzeichnis hinzuzufügen, was diese Warnmeldung bei zukünftigen SSH-Verbindungen zu diesem Knoten verhindern wird. Geben Sie daher `yes` ein und drücken Sie `Enter`, um zu validieren.
Dann werden Sie aufgefordert, Ihr Passwort einzugeben, das zuvor in Schritt 1 als temporär festgelegt wurde. Validieren Sie mit `Enter`. Sie werden dann über SSH mit Ihrem Knoten verbunden sein.

Zusammenfassend sind hier die auszuführenden Befehle:
- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `yes`
- Geben Sie das temporäre Passwort ein und validieren Sie.

### Schritt 4: Aktualisierung und Vorbereitung
Sie sind jetzt über eine SSH-Sitzung mit Ihrem Knoten verbunden. In Ihrem Terminal sollte die Befehlsaufforderung lauten: `pi@RoninDojo:~ $`. Um zu beginnen, aktualisieren Sie die Liste der verfügbaren Pakete und installieren Sie Updates für bestehende Pakete mit dem folgenden Befehl:
`sudo apt update && sudo apt upgrade -y`

Sobald die Updates abgeschlossen sind, fahren Sie fort, *Git* und *Dialog* mit dem Befehl zu installieren:
`sudo apt install git dialog -y`

Klonen Sie als Nächstes den `master`-Zweig des _RoninOS_ Git-Repositorys, indem Sie ausführen:
`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`

Führen Sie das Skript `customize-image.sh` mit dem Befehl aus:
`cd /opt/RoninOS/ && sudo ./customize-image.sh`

**Es ist wichtig, das Skript ohne Unterbrechung laufen zu lassen und geduldig auf das Ende des Prozesses zu warten**, was etwa 10 Minuten dauert. Wenn die Nachricht `Setup is complete` erscheint, können Sie zum nächsten Schritt übergehen.

### Schritt 5: Starten von RoninOS
Starten Sie RoninOS mit dem Befehl:
`sudo systemctl start ronin-setup`

Zeigen Sie die Zeilen der Logdatei mit dem Befehl an:
`tail -f /home/ronindojo/.logs/setup.logs`

In diesem Stadium ist es **wichtig, RoninOS starten zu lassen und darauf zu warten**, dass es fertig läuft. Dies dauert etwa 40 Minuten. Wenn `All RoninDojo feature installations complete!` erscheint, können Sie mit Schritt 6 fortfahren.

### Schritt 6: Zugriff auf RoninUI und Ändern der Anmeldeinformationen
Nach Abschluss der Installation, um über einen Browser eine Verbindung zu Ihrem Knoten herzustellen, stellen Sie sicher, dass Ihr persönlicher Computer mit demselben lokalen Netzwerk wie Ihr Knoten verbunden ist. Wenn Sie auf Ihrem Gerät ein VPN verwenden, deaktivieren Sie es vorübergehend. Um auf die Knotenschnittstelle in Ihrem Browser zuzugreifen, geben Sie in die URL-Leiste ein:
- Direkt die IP-Adresse Ihres Knotens, zum Beispiel, `192.168.1.??`;
- Oder geben Sie `ronindojo.local` ein.
Sobald Sie auf der RoninUI-Startseite sind, werden Sie aufgefordert, die Einrichtung zu starten. Um dies zu tun, klicken Sie auf den `Let's start`-Button.

![lets start](assets/notext/25.webp)

In diesem Stadium präsentiert Ihnen RoninUI Ihr `root`-Passwort. Es ist wesentlich, dieses sicher aufzubewahren. Sie können sich für eine physische Sicherung auf Papier entscheiden oder es in einem [Passwort-Manager](https://planb.network/courses/secu101/4/2) speichern.

![root password](assets/notext/26.webp)

Nachdem Sie das `root`-Passwort gesichert haben, markieren Sie das Kästchen `I have backed up Root user credentials` und klicken auf `Continue`, um fortzufahren.

![confirm root password](assets/notext/27.webp)

Der nächste Schritt beinhaltet das Erstellen eines Benutzerpassworts, das sowohl für den Zugriff auf die RoninUI-Webinterface als auch für die Herstellung von SSH-Sitzungen mit Ihrem Knoten verwendet wird. Wählen Sie ein starkes Passwort und stellen Sie sicher, dass Sie es sicher speichern. Sie müssen dieses Passwort zweimal eingeben, bevor Sie auf `Finish` klicken, um zu validieren. Was den Benutzernamen betrifft, wird empfohlen, die Standardwahl, `ronindojo`, beizubehalten. Wenn Sie sich entscheiden, ihn zu ändern, denken Sie daran, die Befehle in den folgenden Schritten entsprechend anzupassen.

![user credentials](assets/notext/28.webp)

Sobald diese Aktionen abgeschlossen sind, warten Sie, bis Ihr Knoten initialisiert ist. Dann werden Sie auf das RoninUI-Webinterface zugreifen. Sie sind fast am Ende des Prozesses, nur noch ein paar kleine Schritte übrig!
![Ronin UI](assets/notext/29.webp)

### Schritt 7: Temporäre Anmeldeinformationen entfernen
Öffnen Sie ein neues Terminal auf Ihrem persönlichen Computer und stellen Sie eine SSH-Verbindung mit Ihrem Knoten her, indem Sie den folgenden Befehl verwenden:
`SSH ronindojo@[IP]`

Wenn beispielsweise die IP-Adresse Ihres Knotens `192.168.1.40` ist, wird der entsprechende Befehl sein:
`SSH ronindojo@192.168.1.40`

Wenn Sie Ihren Benutzernamen im vorherigen Schritt geändert haben, indem Sie den Standardbenutzernamen (`ronindojo`) durch einen anderen ersetzt haben, stellen Sie sicher, dass Sie diesen neuen Namen im Befehl verwenden. Wenn Sie beispielsweise `planb` als Benutzernamen gewählt haben und die IP-Adresse `192.168.1.40` ist, wird der einzugebende Befehl sein:
`SSH planb@192.168.1.40`
Sie werden aufgefordert, das Benutzerpasswort einzugeben. Geben Sie es ein und drücken Sie `enter`, um zu validieren. Dann gelangen Sie zur RoninCLI-Schnittstelle. Verwenden Sie die Pfeiltasten auf Ihrer Tastatur, um zur Option `Exit RoninDojo` zu navigieren und drücken Sie `enter`, um sie auszuwählen.
![RoninCLI](assets/notext/30.webp)

An diesem Punkt befinden Sie sich im Terminal Ihres Knotens, mit einer Befehlsaufforderung ähnlich wie: `ronindojo@RoninDojo:~ $`. Um den temporären Benutzer zu entfernen, der während der Konfiguration der bootfähigen Micro-SD-Karte erstellt wurde, geben Sie den folgenden Befehl ein und drücken Sie `enter`:
`sudo deluser --remove-home pi`

Sie werden aufgefordert, Ihr Benutzerpasswort zu bestätigen. Geben Sie es ein und validieren Sie mit `enter`. Warten Sie, bis der Vorgang abgeschlossen ist, und verwenden Sie dann den Befehl `exit`, um das Terminal zu verlassen.
Herzlichen Glückwunsch! Ihr RoninDojo v2 Node ist jetzt konfiguriert und einsatzbereit. Er wird mit dem IBD (*Initial Block Download*) beginnen, um die Bitcoin-Blockchain vom Genesis-Block an herunterzuladen und zu verifizieren. Dieser Schritt umfasst das Abrufen aller seit dem 3. Januar 2009 getätigten Bitcoin-Transaktionen und nimmt einige Zeit in Anspruch. Sobald die Blockchain vollständig heruntergeladen ist, wird der Indexer fortfahren, die Datenbank zu komprimieren. Die Dauer des IBD kann erheblich variieren. Ihr RoninDojo Node wird voll funktionsfähig sein, sobald dieser Prozess abgeschlossen ist.
**Wenn Sie von einem alten RoninDojo v1 Node** auf diese neue Version mit diesem Tutorial migrieren und dabei die gleiche SSD behalten, sollte Ihr Node automatisch die vorhandenen Daten auf der Festplatte erkennen und wiederverwenden, sodass Sie den IBD nicht erneut durchführen müssen. In diesem Fall müssen Sie nur darauf warten, dass Ihr Node mit den neuesten Blöcken resynchronisiert wird.

### Schritt 8: "veth* fix"
Wenn Sie auf Ihrem RoninDojo v2 auf Raspberry Pi auf einen Fehler stoßen, bei dem Ihr Knoten nach einer problemlosen Installation plötzlich über SSH nicht mehr erreichbar ist, sich aber nach einem einfachen Neustart wieder erholt, dann müssen Sie diesen Schritt 8 befolgen. Dieser häufige Fehler kann leicht mit einer von der Gemeinschaft entwickelten Lösung behoben werden: dem "_veth fix_". Diese kleine Korrektur behebt dauerhaft die plötzlichen Verbindungsabbrüche. Hier erfahren Sie, wie Sie sie anwenden.

Öffnen Sie ein neues Terminal auf Ihrem persönlichen Computer und stellen Sie eine SSH-Verbindung zu Ihrem Knoten her, indem Sie den folgenden Befehl verwenden: 
`SSH ronindojo@[IP]`

Wenn beispielsweise die IP-Adresse Ihres Knotens `192.168.1.40` ist, wäre der passende Befehl: 
`SSH ronindojo@192.168.1.40`

Es wird Sie aufgefordert, das Benutzerpasswort einzugeben. Geben Sie es ein und drücken Sie `Enter`, um zu bestätigen. Sie gelangen dann zur RoninCLI-Schnittstelle. Verwenden Sie die Pfeiltasten Ihrer Tastatur, um zur Option `Exit RoninDojo` zu navigieren und drücken Sie `Enter`, um sie auszuwählen.

An diesem Punkt befinden Sie sich im Terminal Ihres Knotens, mit einem Befehlsprompt ähnlich wie: `ronindojo@RoninDojo:~ $`. Um den veth* fix anzuwenden, geben Sie den folgenden Befehl ein und drücken Sie `Enter`: 
`sudo nano /etc/dhcpcd.conf`

Bestätigen Sie Ihr Passwort erneut und drücken Sie `Enter`.

Sie gelangen zur Datei `dhcpcd.conf`. Sie müssen den folgenden Text kopieren, dabei das Sternchen einschließen, und ihn am Ende der Datei hinzufügen: 
`denyinterfaces veth*`

Um dies zu tun, bewegen Sie sich mit der Abwärtspfeil-Taste Ihrer Tastatur zum Ende der Datei und verwenden Sie dann die rechte Maustaste Ihrer Maus, um den Text auf einer unabhängigen Zeile einzufügen.

Nachdem Sie den Text hinzugefügt haben, drücken Sie `ctrl X`, um den Vorgang zu starten, gefolgt von `ctrl Y`, um das Speichern der Änderungen zu bestätigen, und drücken Sie `Enter`, um den Vorgang abzuschließen und zum Befehlsprompt zurückzukehren. Um sicherzustellen, dass die Änderung korrekt angewendet wurde, öffnen Sie die Datei `dhcpcd.conf` erneut mit dem entsprechenden Befehl.

Um die Anwendung der Korrektur abzuschließen, starten Sie Ihren Knoten neu, indem Sie ausführen: 
`sudo reboot now`

An diesem Punkt können Sie Ihr Terminal schließen. Lassen Sie dem RoninDojo genügend Zeit zum Neustarten, nach dem Sie sich über die grafische Benutzeroberfläche Ihres Browsers erneut verbinden sollten. Dieser Prozess sollte den aufgetretenen Fehler beheben.

## Wie verwenden Sie Ihren RoninDojo v2 Node?

### Verbinden Ihrer Wallet-Software mit Electrs
Die erste Nutzung Ihres frisch installierten und synchronisierten Nodes wird sein, Ihre Transaktionen im Bitcoin-Netzwerk zu übertragen. Sie werden wahrscheinlich Ihre verschiedenen Wallets mit Ihrem Node verbinden wollen, um Ihre Transaktionen vertraulich zu übertragen. Dies können Sie über den Electrum Rust Server (electrs) tun. Diese Anwendung ist normalerweise auf Ihrem RoninDojo Node vorinstalliert. Falls nicht, könnten Sie sie manuell über die RoninCLI-Schnittstelle in `Anwendungen > Anwendungen verwalten > Electrum Server installieren` installieren.

Um die Tor-Adresse Ihres Electrum Servers zu erhalten, gehen Sie in der RoninUI-Web-Oberfläche zu:
`Pairing > Electrum Server > Jetzt verbinden`
![Pairing](assets/notext/31.webp)
![Electrs](assets/notext/32.webp)
Sie müssen dann die `Hostname`-Adresse, die auf `.onion` endet, in Ihrer Wallet-Software eingeben, begleitet von Port `50001`. ![hostname](assets/notext/33.webp)
Zum Beispiel in Sparrow Wallet, gehen Sie einfach zum Tab:
`Datei > Einstellungen > Server > Privater Electrum`

![Sparrow](assets/notext/34.webp)

### Verbinden Ihrer Wallet-Software mit Samourai Dojo
Als Alternative zur Nutzung von Electrs ermöglicht Dojo Ihnen, Ihre kompatible Software-Wallet direkt mit Ihrem RoninDojo Node zu verbinden. Wallets wie Samourai Wallet und Sentinel bieten diese Funktionalität.

Um die Verbindung herzustellen, müssen Sie lediglich den QR-Code Ihres Dojo scannen. Um diesen QR-Code über RoninUI zu erreichen, navigieren Sie zu:
`Pairing > Samourai Dojo > Jetzt verbinden`
![Samourai Dojo](assets/notext/35.webp)
Um Ihr Samourai Wallet mit Ihrem Dojo zu verbinden, scannen Sie einfach diesen QR-Code während der App-Installation:

![Samourai Wallet-Verbindung](assets/notext/36.webp)
Wenn Sie bereits vor der Einrichtung Ihres Ronin Dojo eine Samourai Wallet hatten, ist es notwendig, Ihre Wallet zu sichern, die Samourai Wallet App zu deinstallieren und dann neu zu installieren, bevor Sie Ihre Wallet wiederherstellen. Beim Starten der neu installierten App haben Sie die Möglichkeit, eine Verbindung zu einem neuen Dojo herzustellen. **Seien Sie vorsichtig, dieser Prozess birgt das Risiko, Ihre Bitcoins zu verlieren, wenn er nicht korrekt ausgeführt wird!** Stellen Sie sicher, dass Sie ein Backup Ihrer Samourai Wallet in Ihren Dateien haben und überprüfen Sie die Gültigkeit Ihrer Passphrase über `Einstellungen > Fehlerbehebung > Passphrase`. Es ist auch wichtig, ein lesbares Backup Ihrer Wiederherstellungsphrase und Ihrer Passphrase zu haben. Für mehr Präzision bei dieser Operation wird empfohlen, diesem detaillierten Tutorial zu folgen: [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).

### Ihren eigenen Mempool.space Block Explorer verwenden
Ein Block Explorer wandelt die rohen Informationen aus der Bitcoin-Blockchain in ein strukturiertes und leicht lesbares Format um. Mit Tools wie *Mempool.space* ist es möglich, Transaktionen zu analysieren, nach spezifischen Adressen zu suchen oder sogar die durchschnittlichen Gebührensätze der Mempools des Netzwerks in Echtzeit zu konsultieren.

Die Verwendung von Online-Block-Explorern birgt jedoch Risiken für Ihre Privatsphäre und erfordert Vertrauen in die von Dritten bereitgestellten Daten. Tatsächlich könnten Sie durch die Nutzung dieser Dienste, ohne Ihren eigenen Knoten zu durchlaufen, unbeabsichtigt Informationen über Ihre Transaktionen preisgeben und müssen sich auf die Genauigkeit der vom Seiteninhaber präsentierten Informationen verlassen.
Um diese Risiken zu mindern, wird empfohlen, Ihre eigene Instanz von *Mempool.space* über das Tor-Netzwerk zu verwenden, direkt auf Ihrem Knoten gehostet. Diese Lösung gewährleistet die Wahrung Ihrer Privatsphäre und die Autonomie Ihrer Daten.
Beginnen Sie dazu mit der Installation des *Mempool Space Visualizer* von RoninUI. Gehen Sie auf der Web-Oberfläche zum `Dashboard`-Tab und klicken Sie unter `Mempool Space` auf `Verwalten`:
`Dashboard > Mempool Space > Verwalten`
![Mempool verwalten](assets/notext/37.webp)
Klicken Sie dann auf den Button `Mempool Visualizer installieren`:
![Mempool installieren](assets/notext/38.webp)
Bestätigen Sie Ihr Benutzerpasswort:
![Passwort Mempool](assets/notext/39.webp)
Warten Sie, bis die Installation abgeschlossen ist, und klicken Sie erneut auf den Button `Verwalten`:
![Mempool Verwalten](assets/notext/40.webp)
Sie erhalten einen `.onion`-Link, um über das Tor-Netzwerk auf Ihre eigene Instanz von *Mempool.space* zuzugreifen.
![Mempool-Link](assets/notext/41.webp)
Ich rate Ihnen, diesen Link in Ihren Favoriten im Tor-Browser zu speichern oder ihn zur Tor-Browser-App auf Ihrem Smartphone hinzuzufügen, für einen einfachen und sicheren Zugriff von überall. Wenn Sie den Tor-Browser noch nicht haben, können Sie ihn hier herunterladen: [https://www.torproject.org/download/](https://www.torproject.org/download/)
![Mempool Tor](assets/notext/42.webp)

### Whirlpool verwenden, um Ihre Bitcoins zu mischen
Ihr RoninDojo-Knoten integriert auch _WhirlpoolCLI_, eine Befehlszeilenschnittstelle, die die Automatisierung von Whirlpool CoinJoins ermöglicht, und _WhirlpoolGUI_, eine grafische Oberfläche, die für die Interaktion mit _WhirlpoolCLI_ konzipiert wurde.
Das Durchführen eines Coinjoins über Whirlpool erfordert, dass die verwendete Anwendung aktiv ist, um Remixes durchzuführen. Diese Bedingung kann für diejenigen, die hohe Anonymitätsstufen erreichen möchten, einschränkend sein. Tatsächlich muss das Gerät, auf dem die Whirlpool integrierende Anwendung läuft, kontinuierlich eingeschaltet bleiben. Das bedeutet, dass Ihr Computer oder Smartphone, um 24 Stunden am Tag an Remixes teilnehmen zu können, durchgehend eingeschaltet bleiben muss, mit Samourai oder Sparrow kontinuierlich geöffnet. Eine Lösung für diese Einschränkung ist die Verwendung von _WhirlpoolCLI_ auf einem Gerät, das immer eingeschaltet ist, wie zum Beispiel einem Bitcoin-Node, was es Ihren Münzen ermöglicht, ohne Unterbrechung zu remixen, ohne dass ein weiteres Gerät eingeschaltet bleiben muss.
Ein detailliertes Tutorial wird vorbereitet, um Sie Schritt für Schritt durch den Prozess des Coinjoinings mit Samourai Wallet und RoninDojo v2, von A bis Z, zu führen.

Für ein tieferes Verständnis von Coinjoin und dessen Verwendung bei Bitcoin lade ich Sie auch ein, diesen anderen Artikel zu konsultieren: Verständnis und Nutzung von Coinjoin bei Bitcoin, wo ich alles, was Sie über diese Technik wissen müssen, im Detail erkläre.

https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2
### Verwendung des Whirlpool Stat Tool (WST)


Nachdem Sie Coinjoins mit Whirlpool durchgeführt haben, ist es nützlich, das erreichte Datenschutzniveau für Ihre gemischten UTXOs genau zu bewerten. Dazu können Sie das Python-Tool *Whirlpool Stat Tool* verwenden. Dieses Tool ermöglicht es Ihnen, sowohl die prospektiven als auch die retrospektiven Bewertungen Ihrer UTXOs zu messen, während deren Diffusionsrate im Pool analysiert wird.

Um Ihr Verständnis der Berechnungsmechanismen dieser Anonsets zu vertiefen, empfehle ich, den Artikel zu lesen: REMIX - WHIRLPOOL, der die Funktionsweise dieser Indizes detailliert beschreibt.

https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa



Um auf das WST-Tool zuzugreifen, gehen Sie zu RoninCLI. Öffnen Sie dazu ein Terminal auf Ihrem persönlichen Computer und stellen Sie eine SSH-Verbindung mit Ihrem Node her, indem Sie den folgenden Befehl verwenden:
`SSH ronindojo@[IP]`

Wenn beispielsweise die IP-Adresse Ihres Nodes `192.168.1.40` ist, wäre der entsprechende Befehl:
`SSH ronindojo@192.168.1.40`

Wenn Sie während Schritt 6 Ihren Benutzernamen geändert haben, indem Sie den Standardbenutzernamen (`ronindojo`) durch einen anderen ersetzt haben, stellen Sie sicher, dass Sie diesen neuen Namen im Befehl verwenden. Wenn Sie beispielsweise `planb` als Ihren Benutzernamen gewählt haben und die IP-Adresse `192.168.1.40` ist, wäre der einzugebende Befehl:
`SSH planb@192.168.1.40`

Sie werden aufgefordert, das Benutzerpasswort einzugeben. Geben Sie es ein und drücken Sie `Enter`, um zu bestätigen. Sie gelangen dann zur RoninCLI-Oberfläche. Verwenden Sie die Pfeiltasten auf Ihrer Tastatur, um zum Menü `Samourai Toolkit` zu navigieren und drücken Sie `Enter`, um es auszuwählen:

![Samourai Toolkit](assets/notext/43.webp)

Wählen Sie dann `Whirlpool Stat Tool`:

![WST](assets/notext/44.webp)

Beim Initialisieren von WST wird das Tool mit seiner automatischen Installation beginnen. Warten Sie während dieses Schritts. Die Gebrauchsanweisungen werden durchlaufen. Sobald die Installation abgeschlossen ist, drücken Sie eine beliebige Taste, um auf das WST-Terminal zuzugreifen:

![WST-Befehle](assets/notext/45.webp)

Das folgende Befehlsprompt wird angezeigt:
`wst#/tmp>`

Wenn Sie diese Schnittstelle verlassen und zum RoninCLI-Menü zurückkehren möchten, geben Sie einfach ein:
`quit`

Zuerst ist es notwendig, den Proxy so zu konfigurieren, dass Tor verwendet wird, um Vertraulichkeit beim Extrahieren von Daten aus OXT zu gewährleisten. Geben Sie den Befehl ein:
`socks5 127.0.0.1:9050`
Fahren Sie anschließend fort, die Pool-Informationen herunterzuladen, die Ihre Transaktion enthalten:
`download 0001`
Ersetzen Sie `0001` durch den Nennwertcode des Pools, an dem Sie interessiert sind. Die Nennwertcodes sind wie folgt auf WST:
- Pool 0,5 Bitcoins: `05`
- Pool 0,05 Bitcoins: `005`
- Pool 0,01 Bitcoins: `001`
- Pool 0,001 Bitcoins: `0001`

Nach dem Herunterladen laden Sie die Daten, indem Sie `0001` durch den Code Ihres Pools in diesem Befehl ersetzen: `load 0001`

![WST laden](assets/notext/46.webp)

Warten Sie, bis das Laden abgeschlossen ist, was einige Minuten dauern kann. Sobald die Daten geladen sind, um die Anonset-Werte Ihrer Münze zu erfahren, führen Sie den Befehl `score` gefolgt von Ihrer TXID (ohne die Klammern) aus:
`score [TXID]`

![WST Bewertung](assets/notext/47.webp)

WST zeigt dann den retrospektiven Wert (_Rückblickende Metriken_), gefolgt von dem prospektiven Wert (_Vorausschauende Metriken_). Neben den Anonset-Werten wird WST auch die Diffusionsrate Ihrer Transaktion innerhalb des Pools im Verhältnis zu ihrem Anonset angeben.

**Es ist wichtig zu beachten, dass der prospektive Wert Ihrer Münze aus der TXID Ihres anfänglichen Mixes berechnet werden sollte und nicht aus Ihrem neuesten Mix. Umgekehrt wird der retrospektive Wert eines UTXO aus der TXID des letzten Zyklus berechnet.**

### Verwendung des Boltzmann-Rechners
Der Boltzmann-Rechner ist ein Werkzeug zur Analyse einer Bitcoin-Transaktion, das die Möglichkeit bietet, ihr Entropieniveau unter anderen fortgeschrittenen Metriken zu messen. Diese Daten bieten eine quantifizierte Bewertung der Privatsphäre einer Transaktion und helfen, potenzielle Mängel zu identifizieren. Dieses Werkzeug ist bereits in Ihren RoninDojo-Knoten integriert, was den Zugang und die Nutzung erleichtert.

Bevor das Verfahren zur Verwendung des Boltzmann-Rechners im Detail erläutert wird, ist es wichtig, die Bedeutung dieser Indikatoren, ihre Berechnungsmethode und ihren Nutzen zu verstehen. Obwohl sie auf jede Bitcoin-Transaktion anwendbar sind, sind diese Indikatoren besonders nützlich, um die Qualität einer Coinjoin-Transaktion zu bewerten.

**Der erste Indikator**, den die Software berechnet, ist die Gesamtzahl der möglichen Kombinationen, angegeben unter `nb combinations` im Werkzeug. Basierend auf den Werten der beteiligten UTXOs quantifiziert dieser Indikator die Anzahl der Wege, auf denen Eingaben mit Ausgaben verbunden werden können. Mit anderen Worten, er bestimmt die Anzahl der plausiblen Interpretationen, die eine Transaktion generieren kann. Zum Beispiel präsentiert ein Coinjoin, der gemäß dem Whirlpool 5x5-Modell strukturiert ist, `1496` mögliche Kombinationen:
![Kombinationen](assets/notext/50.webp)
Quelle: KYCP

**Der zweite Indikator**, der berechnet wird, ist die Entropie einer Transaktion, bezeichnet durch `Entropy`. Wenn eine Transaktion eine hohe Anzahl möglicher Kombinationen hat, ist es oft relevanter, sich auf ihre Entropie zu beziehen. Diese wird als der binäre Logarithmus der Anzahl möglicher Kombinationen definiert. Hier ist die verwendete Formel:
- $E$: die Entropie der Transaktion;
- $C$: die Anzahl der möglichen Kombinationen für die Transaktion.
$$E = \log_2(C)$$
In der Mathematik entspricht der binäre Logarithmus (Logarithmus zur Basis 2) der inversen Operation des Potenzierens von 2. Mit anderen Worten, der binäre Logarithmus von $x$ ist der Exponent, zu dem 2 erhoben werden muss, um $x$ zu erhalten. Daher wird dieser Indikator in Bits ausgedrückt. Nehmen wir das Beispiel der Berechnung der Entropie für eine Coinjoin-Transaktion, die nach dem Whirlpool 5x5-Modell strukturiert ist, welches, wie zuvor erwähnt, eine Anzahl möglicher Kombinationen von `1496` bietet:$$ C = 1496 $$
$$ E = \log_2(1496) $$
$$ E \approx 10.5469 \text{ Bits}$$

Somit zeigt diese Coinjoin-Transaktion eine Entropie von 10.5469 Bits, was als sehr zufriedenstellend betrachtet wird. Je höher dieser Wert ist, desto mehr unterschiedliche Interpretationen lässt die Transaktion zu, wodurch ihr Datenschutzniveau erhöht wird.

Nehmen wir ein zusätzliches Beispiel mit einer konventionelleren Transaktion, die einen Input und zwei Outputs aufweist: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/de/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)
Im Fall dieser Transaktion ist die einzige mögliche Interpretation: `(inp 0) > (Outp 0 ; Outp 1)`. Folglich wird ihre Entropie auf `0` festgelegt:
$$ C = 1 $$
$$ E = \log_2(1) $$
$$ E \approx 0 \text{ Bits}$$
**Der dritte Indikator**, der vom Boltzmann-Rechner bereitgestellt wird, heißt `Wallet Efficiency` (Wallet-Effizienz). Dieser Indikator bewertet die Effizienz der Transaktion, indem er sie mit der optimalen Transaktion vergleicht, die in einem identischen Setup denkbar wäre. Dies führt uns zur Diskussion des Konzepts der maximalen Entropie, die der höchsten Entropie entspricht, die eine spezifische Transaktionsstruktur theoretisch erreichen kann. Somit ist für eine Whirlpool 5x5-Coinjoin-Struktur die maximale Entropie auf `10.5469` festgelegt. Die Effizienz der Transaktion wird dann berechnet, indem diese maximale Entropie mit der tatsächlichen Entropie der analysierten Transaktion konfrontiert wird. Die verwendete Formel lautet wie folgt:
- $ER$: die tatsächliche Entropie der Transaktion, ausgedrückt in Bits;
- $EM$: die maximal mögliche Entropie für eine gegebene Transaktionsstruktur, ebenfalls in Bits;
- $Ef$: die Effizienz der Transaktion, in Bits.
$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$
$$Ef = 0 \text{ Bits}$$

Dieser Indikator wird auch als Prozentsatz ausgedrückt, seine Formel lautet dann:
- $CR$: die Anzahl der tatsächlichen möglichen Kombinationen;
- $CM$: die maximale Anzahl möglicher Kombinationen mit derselben Struktur;
- $Ef$: die Effizienz ausgedrückt als Prozentsatz.
$$Ef = \frac{CR}{CM}$$
$$Ef = \frac{1496}{1496}$$
$$Ef = 100\%$$

Eine Effizienz von `100%` zeigt also an, dass die Transaktion ihr Potenzial für Datenschutz basierend auf ihrer Struktur maximiert.
**Der vierte Indikator**, die Entropiedichte oder `Entropy Density`, bietet eine Perspektive auf die Entropie in Bezug auf jeden Eingang oder Ausgang der Transaktion. Dieser Indikator erweist sich als nützlich für die Bewertung und den Vergleich der Effizienz von Transaktionen unterschiedlicher Größen. Um ihn zu berechnen, teilt man einfach die Gesamtentropie der Transaktion durch die Gesamtzahl der beteiligten Eingänge und Ausgänge. Am Beispiel eines Whirlpool 5x5 Coinjoin:
- $ED$: die Entropiedichte ausgedrückt in Bits;
- $E$: die Entropie der Transaktion ausgedrückt in Bits;
- $T$: die Gesamtzahl der Eingänge und Ausgänge in der Transaktion.
$$T = 5 + 5 = 10$$
$$ED = \frac{E}{T}$$
$$ED = \frac{10.5469}{10}$$
$$ED = 1.054 \text{ Bits}$$
**Das fünfte Informationsstück**, das vom Boltzmann-Rechner geliefert wird, ist die Tabelle der Übereinstimmungswahrscheinlichkeiten zwischen Eingängen und Ausgängen. Diese Tabelle zeigt durch den `Boltzmann-Score` die Wahrscheinlichkeit, dass ein bestimmter Eingang mit einem gegebenen Ausgang verbunden ist. Am Beispiel eines Whirlpool-Coinjoin würde die Wahrscheinlichkeitstabelle die Chancen der Verknüpfung zwischen jedem Eingang und Ausgang hervorheben und bietet ein quantitatives Maß für die Ambiguität oder Vorhersehbarkeit von Assoziationen in der Transaktion:

| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Hier ist klar, dass jeder Eingang eine gleiche Chance hat, mit jedem Ausgang verbunden zu sein, was die Ambiguität und Vertraulichkeit der Transaktion verstärkt. Jedoch ist die Situation bei einer einfachen Transaktion mit einem Eingang und zwei Ausgängen anders:

| %       | Ausgang 0 | Ausgang 1 |
|---------|-----------|-----------|
| Eingang 0 | 100%     | 100%     |

Hier sehen wir, dass die Wahrscheinlichkeit für jeden Ausgang, von Eingang 0 zu kommen, 100% beträgt. Eine niedrigere Wahrscheinlichkeit übersetzt sich somit in eine größere Vertraulichkeit, indem sie die direkten Verbindungen zwischen Eingängen und Ausgängen verdünnt.

**Das sechste Informationsstück**, das bereitgestellt wird, ist die Anzahl der deterministischen Verbindungen, ergänzt durch das Verhältnis dieser Verbindungen. Dieser Indikator offenbart, wie viele Verbindungen zwischen den Eingängen und Ausgängen in der analysierten Transaktion unbestreitbar sind, mit einer 100%igen Wahrscheinlichkeit. Das Verhältnis bietet wiederum eine Perspektive auf das Gewicht dieser deterministischen Verbindungen innerhalb der Gesamtverbindungen der Transaktion.

Zum Beispiel zeigt eine Whirlpool-Typ-Coinjoin-Transaktion keine deterministischen Verbindungen und weist daher einen Indikator und ein Verhältnis von 0% auf. Andererseits ist in unserer zweiten untersuchten Transaktion (mit einem Eingang und zwei Ausgängen) der Indikator auf 2 gesetzt und das Verhältnis erreicht 100%. Somit signalisiert ein Nullindikator eine ausgezeichnete Vertraulichkeit dank der Abwesenheit von direkten und unbestreitbaren Verbindungen zwischen Eingängen und Ausgängen.
**Wie man auf den Boltzmann-Rechner auf RoninDojo zugreift?** Um auf das Werkzeug *Boltzmann-Rechner* zuzugreifen, gehen Sie zu RoninCLI. Öffnen Sie dazu ein Terminal auf Ihrem persönlichen Computer und stellen Sie eine SSH-Verbindung mit Ihrem Knoten her, indem Sie den folgenden Befehl verwenden: `SSH ronindojo@[IP]`

Wenn beispielsweise die IP-Adresse Ihres Knotens `192.168.1.40` ist, wäre der entsprechende Befehl:
`SSH ronindojo@192.168.1.40`

Wenn Sie Ihren Benutzernamen während Schritt 6 geändert haben, indem Sie den Standardbenutzernamen (`ronindojo`) durch einen anderen ersetzt haben, stellen Sie sicher, dass Sie diesen neuen Namen im Befehl verwenden. Wenn Sie beispielsweise `planb` als Ihren Benutzernamen gewählt haben und die IP-Adresse `192.168.1.40` ist, wäre der einzugebende Befehl:
`SSH planb@192.168.1.40`

Sie werden aufgefordert, das Benutzerpasswort einzugeben. Geben Sie es ein und drücken Sie dann `Enter`, um zu bestätigen. Sie gelangen dann zur RoninCLI-Schnittstelle. Verwenden Sie die Pfeiltasten auf Ihrer Tastatur, um zum Menü `Samourai Toolkit` zu navigieren und drücken Sie `Enter`, um es auszuwählen:

![Samourai Toolkit](assets/notext/43.webp)

Wählen Sie dann `Boltzmann-Rechner`:

![boltzmann](assets/notext/49.webp)

Sie gelangen auf die Startseite der Software:

![boltzmann home](assets/notext/51.webp)

Geben Sie die TXID der Transaktion ein, die Sie untersuchen möchten, und drücken Sie die `Enter`-Taste:

![boltzmann txid](assets/notext/52.webp)

Der Rechner liefert Ihnen dann alle Indikatoren, die wir zuvor besprochen haben:

![boltzmann result](assets/notext/53.webp)

### Weitere Funktionen Ihres RoninDojo v2
Ihr RoninDojo-Knoten integriert verschiedene andere Funktionen. Insbesondere haben Sie die Möglichkeit, spezifische Informationen zu scannen, um sie zu berücksichtigen. Manchmal zeigt beispielsweise Ihre Samourai-Wallet, die mit RoninDojo verbunden ist, möglicherweise nicht die Bitcoins an, die Sie tatsächlich besitzen. Wenn der Saldo 0 anzeigt, während Sie sicher sind, Bitcoins in dieser Wallet zu haben, können mehrere Gründe diese Situation erklären, wie ein Fehler in den Ableitungspfaden. Aber eine der Ursachen kann auch sein, dass Ihr Knoten Ihre Adressen nicht ordnungsgemäß überwacht. Um dieses Problem zu lösen, können Sie sicherstellen, dass Ihr Knoten tatsächlich Ihrem `xpub` folgt, indem Sie das _xpub-Werkzeug_ verwenden. Um auf dieses Werkzeug über RoninUI zuzugreifen, folgen Sie dem Pfad:
`Wartung > XPUB-Werkzeug`

Geben Sie den `xpub` ein, der das Problem verursacht, und klicken Sie auf die Schaltfläche `Prüfen`, um diese Informationen zu überprüfen:
![xpub tool](assets/notext/54.webp)
Stellen Sie sicher, dass alle Transaktionen ordnungsgemäß aufgelistet sind. Es ist auch wichtig zu überprüfen, ob der verwendete Ableitungstyp dem Ihrer Wallet entspricht. Wenn dies nicht der Fall ist, klicken Sie auf `Neu eingeben`, und wählen Sie dann aus `BIP44`, `BIP49` oder `BIP84` nach Ihren Bedürfnissen.
Über dieses Werkzeug hinaus ist die Registerkarte `Wartung` von RoninUI voller anderer nützlicher Funktionen:
- *Transaktionswerkzeug*: Ermöglicht die Untersuchung der Details einer bestimmten Transaktion;
- *Adresswerkzeug*: Ermöglicht die Bestätigung der Verfolgung einer bestimmten Adresse durch Ihr Dojo;
- *Blöcke erneut scannen*: Zwingt Ihren Knoten, einen neuen Scan eines bestimmten Blockbereichs durchzuführen.

Die Registerkarte `Push Tx` ist eine weitere interessante Funktion von RoninUI, die das Senden einer signierten Transaktion im Bitcoin-Netzwerk ermöglicht. Die Transaktion muss in hexadezimaler Form eingegeben werden.

Bezüglich der anderen Registerkarten, die auf Ihrem RoninUI-Dashboard verfügbar sind:
- `Apps`: Beherbergt die Whirlpool-Anwendung und wird sicherlich in Zukunft zur Integration neuer Anwendungen verwendet werden;
- `Logs`: Bietet Echtzeitzugriff auf die Ereignisprotokolle Ihrer Software;
- `System Info`: Stellt allgemeine Informationen über Ihren Knoten bereit, wie z.B. CPU-Temperatur, Speicherplatznutzung oder RAM-Daten. Sie finden dort auch die Optionen `Reboot` und `Shut down`, um Ihren Knoten neu zu starten oder auszuschalten;
- `Settings`: Ermöglicht es Ihnen, Ihr Benutzerpasswort zu ändern.

Das war's! Vielen Dank, dass Sie diesem Tutorial bis zum Ende gefolgt sind. Wenn es Ihnen gefallen hat, ermutige ich Sie, es in den sozialen Medien zu teilen. Darüber hinaus, wenn Sie die Möglichkeit haben, erwägen Sie, die Entwickler, die diese freie und Open-Source-Software unserer Gemeinschaft zur Verfügung stellen, mit einer Spende zu unterstützen: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). Um Ihr Wissen über RoninDojo zu vertiefen und weitere Ressourcen zu entdecken, empfehle ich dringend, die unten genannten Links zu externen Ressourcen zu konsultieren.

**Externe Ressourcen:**
- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/introducing-boltzmann-85930984a159](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)
