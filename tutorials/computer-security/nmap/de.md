---
name: Nmap
description: Master-Nmap für Netzwerk-Mapping und Schwachstellen-Scans
---

![cover](assets/cover.webp)



*Dieses Tutorial basiert auf Originalinhalten von Mickael Dorigny, die auf [IT-Connect](https://www.it-connect.fr/) veröffentlicht wurden. Lizenz [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Es wurden Änderungen am Originaltext vorgenommen.*



___



Willkommen zu diesem Einführungs-Tutorial zu Nmap, das sich an alle richtet, die dieses leistungsstarke Netzwerk-Scanning-Tool beherrschen wollen. Das Ziel ist es, Ihnen die grundlegenden Kenntnisse zu vermitteln, die Sie benötigen, um Nmap im Alltag effektiv zu nutzen.



Nmap ist ein vielseitiges Tool, das von IT-, Netzwerk- und Cybersecurity-Fachleuten häufig zur Diagnose, Netzwerkerkennung und Sicherheitsüberprüfung eingesetzt wird. Dieses Tutorial richtet sich an diejenigen, die neu in diesen Bereichen sind und die Grundlagen von Nmap erlernen möchten. Grundkenntnisse in der System- und Netzwerkadministration werden empfohlen.



Sie lernen die Grundlagen von Nmap, wie man Port-Scans durchführt, aktive Hosts in einem Netzwerk identifiziert, Service-Versionen und Betriebssysteme erkennt, Schwachstellen-Scans durchführt und vieles mehr. Jeder Abschnitt enthält detaillierte Erklärungen und praktische Beispiele, die Ihnen helfen, die Verwendung von Nmap in einer Vielzahl von Kontexten zu meistern.



Am Ende dieses Tutorials werden Sie ein solides Verständnis von Nmap haben und in der Lage sein, es effektiv einzusetzen, um die Sicherheit und Verwaltung Ihrer Netzwerke zu verbessern. Viel Spaß beim Lesen.



## 1 - Einführung in Nmap: Was ist Nmap?



### I. Präsentation



In diesem ersten Abschnitt werfen wir einen Blick auf das Netzwerk-Scan-Tool Nmap. Wir werden uns die wichtigsten Elements ansehen, die Sie über dieses Tool wissen müssen, und wie es im Allgemeinen funktioniert. Dies wird uns helfen, den Rest des Tutorials besser zu verstehen.



### II. Einführung in das Nmap-Tool



Nmap, für _Network Mapper_, ist ein freies Open-Source-Tool, das zur **Netzwerkerkennung, -zuordnung und Sicherheitsüberprüfung** verwendet wird. Es kann auch für andere Aufgaben wie **Netzwerkinventarisierung, Diagnose oder Überwachung** verwendet werden.



Es kann feststellen, ob Hosts in einem anvisierten Netzwerk aktiv und erreichbar sind, welche Netzwerkdienste ausgesetzt sind, welche Versionen und Technologien verwendet werden und andere nützliche Analyseinformationen. Nmap kann zum Scannen eines einzelnen Dienstes auf einem bestimmten Rechner oder über große Bereiche des Netzwerks bis hin zum gesamten Internet verwendet werden.



Die Stärken von Nmap sind vielfältig:





- Leistungsstark und flexibel**: Nmap kann große Netzwerke scannen und fortschrittliche Erkennungstechniken verwenden. Es unterstützt UDP, TCP, ICMP, IPv4 und IPv6 und kann Versionserkennung, Schwachstellen-Scans oder protokollspezifische Interaktionen durchführen. Seine Architektur ist modular, vor allem dank der NSE-Skripte (Nmap Scripting Engine), auf die wir später in diesem Tutorial eingehen werden.
- Benutzerfreundlichkeit**: Die offizielle Dokumentation ist umfangreich und von höchster Qualität. Außerdem stehen zahlreiche Community-Ressourcen zur Verfügung, um Ihnen den Einstieg zu erleichtern.
- Beliebtheit und Langlebigkeit**: Nmap ist seit 1998 eine Referenz in seinem Bereich. Die aktuelle Version, zum Zeitpunkt dieser Aktualisierung, ist 7.95. Obwohl es andere Tools für bestimmte Aufgaben gibt, ist Nmap nach wie vor ein unverzichtbares Werkzeug für die Netzwerkabbildung und -analyse.



**Nmap im Kino**



Nmap ist eines der wenigen Sicherheitstools, die in der breiten Öffentlichkeit einen gewissen Bekanntheitsgrad erlangt haben. Es taucht in dem Film _Matrix Reloaded_ in einer symbolträchtigen Szene auf, in der Trinity es benutzt, um sich in ein System zu hacken:



![nmap-image](assets/fr/01.webp)



matrix: Reloaded-Szene mit Nmap



Er tritt auch in anderen Kinofilmen auf.



**Feedback



Als Systemadministrator und späterer Cybersecurity-Auditor und Pentester nutze **ich Nmap fast täglich**, und ich empfehle es **regelmäßig** Systemadministratoren, die ihre Netzwerkbeherrschung und ihre Diagnosefähigkeiten verbessern wollen.



### III. Betrieb auf hoher Ebene



Nmap ist für Linux, Windows und macOS verfügbar. Es ist hauptsächlich in C, C++ und Lua (für NSE-Skripte) geschrieben. Es wird hauptsächlich auf der Kommandozeile verwendet, obwohl es auch grafische Oberflächen wie Zenmap gibt. Wir raten Ihnen jedoch dringend, mit der Befehlszeile zu beginnen, um die Funktionsweise besser zu verstehen.



Ein einfaches Beispiel:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Dieser Befehl wird später im Detail erklärt. In diesem Tutorium verwenden wir Nmap unter Linux, aber seine Einsatzmöglichkeiten sind auf anderen Systemen ähnlich. Unter Windows stützt sich Nmap auf die **Npcap**-Bibliothek (die das inzwischen veraltete WinPcap ersetzt), um Netzwerkpakete zu erfassen und einzuspeisen.



Nmap wird wie ein herkömmliches Binärprogramm wie `ls` oder `ip` benutzt. Einige fortgeschrittene Funktionen können erhöhte Rechte erfordern, da das Tool manchmal Pakete auf unkonventionelle Weise manipuliert, um bestimmte Reaktionen auf den Zielsystemen hervorzurufen (insbesondere zur Erkennung von Diensten oder Sicherheitslücken).



### IV. Auswirkungen der Verwendung von Nmap



Bevor Sie Nmap verwenden, sollten Sie sich unbedingt über die möglichen Auswirkungen auf Netzwerke und Systeme im Klaren sein:





- Er kann **Tausende oder sogar Millionen von Paketen** in kurzer Zeit versenden, was bestimmte Netzinfrastrukturen sättigen kann.
- Es kann generate **geformte oder nicht standardisierte** Pakete, die bestimmte Geräte (insbesondere Industriesysteme) stören können.
- Er kann **angriffsähnliches Verhalten** hervorrufen, das in Sicherheitssystemen (Firewalls, IDS/IPS usw.) Warnungen auslösen kann.



Im Allgemeinen ist **Nmap ein sehr gesprächiges Tool**, da es eine Menge Datenverkehr erzeugt, um so viele Informationen wie möglich zu extrahieren. Es ist daher ratsam, seine Funktionsweise vollständig zu verstehen, bevor man es in sensiblen oder Produktionsumgebungen einsetzt.



### V. Schlussfolgerung



In diesem Abschnitt werden Nmap und seine wichtigsten Funktionen vorgestellt. Wir haben gesehen, dass es ein unverzichtbares, leistungsfähiges und flexibles Netzwerk-Mapping-Tool ist. Wir haben auch besprochen, wie es funktioniert und welche Vorsichtsmaßnahmen Sie treffen müssen, wenn Sie es benutzen, um den Rahmen für die folgenden Teile des Tutorials zu schaffen.



## 2 - Warum Nmap verwenden?



### I. Präsentation



In diesem Abschnitt werfen wir einen Blick auf die Hauptanwendungen des Netzwerk-Scanning-Tools Nmap. Wir werden sehen, dass es ein Tool ist, das in vielen Kontexten und Berufen weit verbreitet ist, und dass es definitiv eine nützliche Fähigkeit ist, es in Ihrem Werkzeugkasten zu haben und zu wissen, wie man es beherrscht.



### II. Verwendung von Nmap für Diagnose und Überwachung



Nmap kann für die Netzwerkdiagnose und - im weiteren Sinne - für die Überwachung verwendet werden. Genauso wie man mit einem Ping feststellen kann, ob zwei Hosts miteinander kommunizieren, kann man mit Nmap schnell feststellen, ob ein Host aktiv ist oder ob ein bestimmter Dienst in Betrieb ist. Dank [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap") kann man genaue Daten über die Antwortzeit eines Hosts, den Weg, den die Pakete nehmen, die Antwort eines bestimmten Dienstes usw. erhalten.



Der folgende Befehl und das folgende Ergebnis können zum Beispiel verwendet werden, um schnell herauszufinden, ob ein Webserver auf dem Host **192.168.1.18** aktiv ist und korrekt antwortet:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Verwenden Sie Nmap, um den Status eines Webdienstes von einem entfernten Server abzurufen



Die Verwendung von Nmap geht also weiter als der berühmte "Ping-Test" während der Debugging- oder Diagnosephasen. Wir werden später sehen, dass es mehrere Methoden gibt, mit denen Nmap herausfindet, welcher Dienst an einem bestimmten Port lauscht, einschließlich seiner Version.



### III. Verwendung von Nmap für das Netzwerk-Mapping



Als _Network Mapper_ ist die Netzwerkzuordnung das Hauptziel dieses Tools. Es kann innerhalb eines lokalen Netzwerks oder über mehrere Netzwerke, Subnetze und VLANs hinweg verwendet werden, um alle erreichbaren Hosts und Dienste aufzulisten. Nmap macht diese Aufgabe viel schneller und effizienter als jede manuelle Methode.



Der folgende Befehl kann zum Beispiel verwendet werden, um aktive Hosts im Netzwerk **192.168.1.0/24** schnell zu identifizieren:



```
nmap -sn 192.168.1.0/24
```



*Hinweis: Die Option "sP" ist veraltet und wurde durch "sn" ersetzt



![nmap-image](assets/fr/03.webp)



*Nmap verwenden, um erreichbare Hosts in einem Netzwerk zu finden*



Wir werden später sehen, dass es mehrere Methoden gibt, mit denen Nmap feststellt, ob ein Host als "aktiv" angesehen werden kann, auch wenn er a priori keine Dienste anbietet.



### IV. Verwendung von Nmap zur Bewertung einer Filterungsstrategie



Nmap hat den Vorteil, dass es faktisch ist: Seine Ergebnisse ermöglichen konkrete Feststellungen, im Gegensatz zu einem Architekturdokument oder einer Filterungspolitik. Es ist ein wichtiges Instrument zur Bewertung der Wirksamkeit der Abschottung von Informationssystemen, da es Ihnen ermöglicht, **zu überprüfen, ob die Filterrichtlinie tatsächlich angewendet wird**.



In einem Unternehmensnetz ist es nach bewährten Verfahren erforderlich, dass die Systeme je nach ihrer Rolle, ihrer Kritikalität oder ihrem Standort segmentiert werden. Filterregeln (oft über Firewalls implementiert) müssen die Kommunikation zwischen den Zonen einschränken. Diese Konfigurationen sind jedoch oft komplex und fehleranfällig.



Um also zu überprüfen, ob die Richtlinie eingehalten wurde, geht nichts über einen konkreten Test. So können Sie beispielsweise überprüfen, ob sensible Verwaltungsdienste (SSH, WinRM, MSSQL, MySQL usw.) von einer Benutzerzone aus nicht zugänglich sind.



Die Verwendung von **Nmap zum Testen der Filterrichtlinie** sollte systematisch erfolgen, bevor eine solche Richtlinie in Betrieb genommen wird. Leider wird diese Prüfung oft vernachlässigt.



Meiner Erfahrung nach bleiben viele Konfigurationsfehler unbemerkt, wenn es keine Validierungstests gibt. Ein einfacher Fehler in einem IP-Bereich oder ein Regelversehen kann eine vermeintlich isolierte Zone angreifbar machen.



### V. Verwendung von Nmap für Sicherheitsaudits und Penetrationstests



Nmap hat **viele nützliche Funktionen für die Sicherheitsbewertung**, Penetrationstests (Pentests) und leider auch für Angreifer.



Netzwerkerkennungsfunktionen sind für einen Angreifer, der die Netzwerktopologie nach einer ersten Kompromittierung verstehen muss, von entscheidender Bedeutung. Aber Nmap bietet viel mehr als das: Es integriert eine Skripting-Engine, **von denen viele der Erkennung von Sicherheitslücken gewidmet sind**.



Mit diesem Befehl kann beispielsweise überprüft werden, ob ein FTP-Dienst eine anonyme Verbindung zulässt, ohne dass eine manuelle Verbindung hergestellt werden muss:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Verwendung eines NSE-Skripts zur Überprüfung der anonymen FTP-Authentifizierung über Nmap.*



Die Schwachstellenerkennung mit Nmap ist einer der ersten Schritte bei einem Audit oder Penetrationstest. Sie ermöglicht es Ihnen, bestimmte Schwachstellen schnell zu identifizieren und Ihre Analysebemühungen zu optimieren.



Aber Vorsicht: **Werkzeuge zum Scannen von Schwachstellen haben ihre Grenzen**. Nmap deckt nur einen Bruchteil der Bedrohungen ab und garantiert nicht, dass ein System sicher ist, wenn keine Probleme entdeckt werden. Es ist daher wichtig, **die Funktionsweise der verwendeten Skripte zu verstehen** und sich nicht allein auf ihr Urteil zu verlassen.



### VI. Schlussfolgerung



Wir haben gesehen, dass die Beherrschung von Nmap eine breite Palette von Anwendungsfällen abdecken kann, von der Diagnose und Überwachung bis zum Mapping, der Bewertung von Sicherheitsrichtlinien und dem Scannen von Schwachstellen. Im nächsten Abschnitt gehen wir der Sache auf den Grund und installieren Nmap.




## 3 - Installieren und Konfigurieren von Nmap



### I. Präsentation



In diesem Abschnitt lernen wir, wie man das Netzwerk-Scan-Tool Nmap unter Linux und Windows installiert. Am Ende dieses Abschnitts haben wir alles, was wir brauchen, um Nmap für zukünftige Module zu verwenden. Schließlich werden wir sehen, welche Privilegien es bei der Verwendung benötigt und warum.



### II. Installation von Nmap unter Linux



Nmap wurde ursprünglich für den Einsatz auf GNU/Linux-Betriebssystemen entwickelt. Daher und dank seiner Langlebigkeit und Beliebtheit finden Sie es in allen offiziellen Repositories der großen Unix-Distributionen. In diesem Tutorial verwende ich ein Debian-basiertes Betriebssystem [Kali Linux] (https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Aber Sie können es auf genau die gleiche Weise von einem klassischen Debian, CentOS, Red Hat oder was auch immer verwenden!



Unter Debian können Sie mit folgendem Befehl überprüfen, ob Nmap in Ihren aktuellen Repositories vorhanden ist:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



Die Antwort hier zeigt eindeutig, dass das Paket "nmap" in den Repositories (hier die von Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")) existiert. Von nun an können Sie Nmap über die üblichen Installationsbefehle installieren, nichts Entwaffnendes für den Moment 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



Um zu überprüfen, ob Nmap korrekt installiert ist, zeigen wir seine Version an:



```
nmap --version
```



Hier ist das erwartete Ergebnis:



![nmap-image](assets/fr/05.webp)



ergebnis der Anzeige der aktuellen Version von Nmap._



Beachten Sie das Vorhandensein der Bibliothek "libpcap" (_Packet Capture Library_) und ihrer Version in dieser Anzeige. Die auch von Wireshark verwendete "libpcap" wird von Nmap benutzt, um Pakete zu erzeugen und zu manipulieren und den Netzwerkverkehr abzuhören.



### III Installation von Nmap unter Windows



Zur Installation auf einem Windows-Betriebssystem laden Sie zunächst die Binärdatei von der offiziellen Website (und keiner anderen!) herunter:





- Nmap-Download-Seite auf der offiziellen Website: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




Sie müssen dann die Binärdatei mit dem Namen "nmap-<VERSION>-setup.exe" herunterladen:



![nmap-image](assets/fr/06.webp)



nmap für Windows Installations-Binary Download-Seite



Sobald Sie diese Binärdatei auf Ihrem System haben, führen Sie sie einfach aus, um Nmap zu installieren. Die Installation ist unkompliziert, und Sie können alle Optionen als Standard belassen.



Mein Reflex ist es, das Häkchen bei "zenmap (GUI Frontend)" zu entfernen. Das ist ein grafisches Interface für Nmap, das ich nicht benutze und das in diesem Tutorial nicht behandelt wird, aber Sie können es gerne ausprobieren, sobald Sie das Nmap-Befehlszeilentool beherrschen!



![nmap-image](assets/fr/07.webp)



optionale Abwahl von Zenmap bei der Installation von Nmap unter Windows



Am Ende der Nmap-Installation wird eine zweite Installation vorgeschlagen: die der Bibliothek "Npcap":



![nmap-image](assets/fr/08.webp)



installation der "Npcap"-Bibliothek bei der Installation von Nmap unter Windows



Dies ist die Bibliothek, auf die sich Nmap stützt, um die Netzwerkkommunikation zu verwalten, d.h. um Netzwerkpakete zu erstellen, zu senden und zu empfangen. Wenn Sie Wireshark unter Windows benutzen, sind Sie wahrscheinlich schon auf diese Bibliothek gestoßen, da sie ebenfalls verwendet wird und installiert werden muss.



Wie bei Linux können Sie überprüfen, ob Nmap installiert ist, indem Sie eine Eingabeaufforderung oder ein [Powershell]-Terminal (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") öffnen und den folgenden Befehl eingeben:



```
nmap --version
```



Hier ist das erwartete Ergebnis:



![nmap-image](assets/fr/09.webp)



ergebnis der Anzeige der aktuellen Version von Nmap._



Nmap ist jetzt auf Windows installiert. Sie können es auf genau dieselbe Weise wie unter Linux verwenden, indem Sie dieser Anleitung folgen.



### IV. Für die Benutzung von Nmap benötigte lokale Privilegien



Übrigens, wenn man Nmap benutzt, **braucht man dann erhöhte lokale Rechte auf dem System?** Die Antwort ist: **Es kommt darauf an**.



In seiner grundlegenden Form, d.h. ohne sehr weit in der Nutzung seiner Optionen zu gehen, benötigt Nmap nicht unbedingt privilegierte Rechte. Sie werden jedoch bald feststellen, dass es besser ist, Nmap in einem privilegierten Kontext ("root" unter Linux, "Administrator" oder gleichwertig unter Windows) zu benutzen, um sein volles Potenzial ausschöpfen zu können, auch auf die Gefahr hin, eine Fehlermeldung wie diese zu erhalten:



![nmap-image](assets/fr/10.webp)



fehlermeldung unter Linux, wenn Nmap-Optionen Root-Rechte erfordern



Ob unter Linux oder Windows, es gibt viele Fälle, in denen Nmap Sie um privilegierten Zugriff bittet. Die Hauptgründe dafür sind die folgenden (die Liste ist nicht vollständig):





- Konstruieren von "rohen" Netzwerkpaketen**: Nmap ist in der Lage, eine breite Palette von Scan-Methoden anzuwenden, einschließlich fortgeschrittener Paketmanipulation und -konstruktion. Das ist z.B. der Fall, wenn wir TCP-SYN-Scans durchführen wollen, die das klassische _Three-way handshake_ des TCP-Austauschs nicht respektieren. Um das zu tun, muss Nmap andere Funktionen als die von Betriebssystemen benutzen, die nur wissen, wie man gute Praktiken in der Netzwerkkommunikation respektiert (es greift auf die oben genannten Bibliotheken "Npcap" und "libcap" zurück). Weil Nmap nicht auf die "normale" Weise vorgeht, kann es bestimmte Informationen über Betriebssysteme, Dienste und bestimmte Schwachstellen ableiten.





- Den Netzwerkverkehr abhören**: Einige der Optionen von Nmap erfordern, dass es das Netzwerk abhört, um bestimmte Informationen zu erhalten. Diese Aktion gilt auf Betriebssystemen als sensibel, da sie es Ihnen auch ermöglicht, die Kommunikation anderer Anwendungen auf dem System abzuhören. Genau wie Wireshark benötigt Nmap dazu bestimmte Rechte, die man leichter erhält, wenn man sich direkt in einer privilegierten Sitzung befindet.





- Lauschen auf privilegierten Ports**: Auf Betriebssystemen gelten die Ports von 0 bis 1024 (TCP und UDP) als privilegiert, d.h. sie sind irgendwie für ganz bestimmte Zwecke reserviert und daher geschützt. Obwohl dieser Grund heute etwas veraltet ist, ist es immer noch notwendig, bestimmte Privilegien zu haben, um auf diesen Ports zu lauschen, was Nmap je nach Verwendungszweck tun muss.





- Senden von UDP-Paketen:** Auch das Abhören einer Netzwerkanwendung auf UDP-Ports (ein zustandsloses Protokoll) erfordert privilegierte Rechte auf Betriebssystemen. Daher ist eine privilegierte Sitzung erforderlich, wenn Sie einen UDP-Scan durchführen wollen, bei dem Nmap auf eine Antwort warten muss, um die Antworten auf seine Scans zu analysieren.




Um genau zu sein, ist es zumindest unter Linux möglich, Nmap mit all seinen Funktionen und Optionen auszuführen, ohne root zu sein. Dies wird erreicht, indem man der Binärdatei die richtigen _Fähigkeiten_ zugesteht. Dies erfordert jedoch fortgeschrittene Manipulationen und ist vielleicht nicht so praktisch wie die direkte Ausführung von Nmap mit Privilegien. Außerdem ist dieser Ansatz weniger verbreitet und kann Sicherheitsprobleme aufwerfen, wenn er falsch konfiguriert ist.



Das weicht jedoch ein bisschen von unserem Nmap-Tutorial ab, also lassen wir es vorerst weg.



Für den Rest dieses Tutorials gehen Sie davon aus, dass Nmap immer als "root" (von einer Shell als "root" oder über den Befehl "sudo") oder in einem Administrator-Terminal unter Windows ausgeführt wird, auch wenn dies nicht angegeben ist. Andernfalls können Sie subtile, aber spürbare Unterschiede zum Tutorial feststellen.



### V. Schlussfolgerung



Das war's! Nmap ist jetzt auf unserem Betriebssystem installiert und einsatzbereit und muss nicht mehr konfiguriert werden. Mit diesem Abschnitt ist die Einführung und Vorstellung von Nmap abgeschlossen. Ich hoffe, es hat Ihnen den Mund wässrig gemacht und Sie sind begierig darauf, mit der Praxis zu beginnen.



Jetzt haben wir eine bessere Vorstellung davon, was das Nmap-Mapping-Tool ist und wofür es am häufigsten verwendet wird, aber auch von seinen Grenzen. Lassen Sie uns weitermachen!




## 4 - TCP- und UDP-Port-Scans mit Nmap



### I. Präsentation



In diesem Abschnitt lernen wir, wie wir unsere ersten Port-Scans mit dem Netzwerk-Scan-Tool Nmap durchführen. Wir werden sehen, wie man damit eine Liste der Netzwerkdienste erstellt, die auf einem Host verfügbar sind, egal ob sie TCP- oder UDP-Protokolle verwenden.



Denken Sie daran, von nun an nur noch Hosts in einer kontrollierten Umgebung zu scannen, für die Sie eine ausdrückliche Genehmigung haben.





- Zur Erinnerung: [Strafgesetzbuch: Kapitel III: Angriffe auf automatisierte Datenverarbeitungssysteme](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Wenn Sie keins zur Hand haben**, empfehle ich Ihnen die folgenden kostenlosen Lösungen, die genau das Richtige sind!





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")**: Die Hacking-Trainingsplattform "Hack The Box" stellt ständig verwundbare Systeme zur Verfügung, die Sie nach Belieben angreifen können. Es stehen mehrere hundert Systeme zur Verfügung, aber ein erneuter Pool von 20 Maschinen wird das ganze Jahr über kostenlos angeboten, mit Zugang über ein OpenVPN-VPN.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")**: Diese Plattform bietet zahlreiche absichtlich verwundbare Systeme zum Download an, die über VirtualBox (ebenfalls eine kostenlose Lösung) oder auf andere Weise genutzt werden können. Nach dem Download ist kein VPN erforderlich - alles ist lokal.




Es steht Ihnen auch frei, eine virtuelle Maschine** auf Ihrem bevorzugten Betriebssystem zu erstellen und dort verschiedene Dienste als Testziele zu installieren. Der Vorteil dabei ist, dass Sie auch sehen können, was auf der Serverseite während eines Scans passiert, insbesondere mit Wireshark, und dass Sie bei fortgeschritteneren Tests auch die lokale Firewall im Blick haben.



Lassen Sie uns praktisch werden!



### II. Scannen der TCP-Ports eines Hosts mit Nmap



#### A. Erster TCP-Port-Scan mit Nmap



Wir werden nun unsere ersten Scans mit Nmap durchführen. Unser Ziel ist einfach: Wir wollen herausfinden, welche Dienste von dem Webserver, den wir gerade eingerichtet haben, offengelegt werden, um zu sehen, ob es etwas Unerwartetes gibt, z. B. einen Verwaltungsdienst, der nicht zugänglich sein sollte, oder die Offenlegung eines Ports einer Anwendung, von der wir dachten, dass sie außer Betrieb genommen wurde.



In meinem Beispiel hat der zu überprüfende Host die IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



Hier ist ein mögliches Ergebnis. Wir sehen eine klassische Nmap-Rückgabe mit einer Menge Informationen:



![nmap-image](assets/fr/11.webp)



ergebnisse eines einfachen TCP-Scans mit Nmap._



Ein kurzer Blick auf dieses Ergebnis zeigt uns, dass die Ports TCP/22 und TCP/80 auf diesem Host zugänglich sind.



Standardmäßig scannt Nmap nur TCP-Ports, wenn Sie es nicht anders angeben.



#### B. Verstehen der Ergebnisse eines einfachen Nmap-Scans



Gehen wir jedoch einen Schritt weiter, um diese Ausgabe zu verstehen: Jede Zeile ist wichtig, erstens, um zu wissen, was gerade getan wurde, und zweitens, um die Scanergebnisse selbst richtig zu interpretieren.



Die erste Zeile ist im Wesentlichen eine Erinnerung an die Scan-Version und das Datum (nützlich für die Protokollierung und Archivierung!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



Die zweite Zeile zeigt die Ergebnisse des ersten Scans für den Host "debian.home (192.168.1.19)". Diese Information wird nützlich sein, wenn wir mehrere Hosts gleichzeitig scannen wollen:



```
Nmap scan report for debian.home (192.168.1.19)
```



In der dritten Zeile steht, dass der betreffende Host "Up", also aktiv ist:



```
Host is up (0.00022s latency).
```



Schließlich informiert uns Nmap, dass 998 TCP-Ports, die als geschlossen identifiziert wurden, nicht in der Datei:



```
Not shown: 998 closed tcp ports (conn-refused)
```



Dies erspart uns fast 1.000 Zeilen an Ausgaben, die wie:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Danke an ihn, dass er uns das erspart hat!



Warum 998 "geschlossene" Ports? Wenn man die 2 offenen Ports hinzufügt, ergibt das 1000, und das ist die Anzahl der Ports, die Nmap in seiner Standardkonfiguration scannt, nicht die 65535 vorhandenen TCP-Ports! Wir werden später sehen, dass dies vollständig und leicht anpassbar ist. Aber wenn der anvisierte Host einen Dienst hat, der auf einem eher exotischen Port lauscht, wird dieser "Standard"-Scan ihn nicht aufdecken.



Nach diesen Informationen finden wir das Interessanteste: eine Tabelle, die nach den drei Spalten "PORT - STATE - SERVICE" organisiert ist:





- Die erste Spalte "PORT" gibt einfach den Zielport/das Zielprotokoll an, und hier ist es wichtig zu sehen, ob es sich um einen TCP-Port (`<port>/tcp`) oder einen UDP-Port (`<port>/udp`) handelt.





- Die Spalte "STATE" gibt den Status des Netzwerkdienstes an, der an diesem Port entdeckt und von Nmap anhand der erhaltenen Antwort bestimmt wurde. Dieser kann "offen", "geschlossen", "gefiltert" oder "unbekannt" sein. Wir werden später sehen, wie Nmap zwischen diesen verschiedenen Zuständen unterscheidet.





- Die Spalte "SERVICE" gibt den Dienst an, der an dem betreffenden Anschluss angeboten wird. Bitte beachten Sie jedoch, dass wir hier keine aktiven Optionen zur Diensterkennung verwendet haben. Nmap verlässt sich auf eine lokale Referenz zwischen einem Port/Protokoll und dem vermeintlich zugewiesenen Dienst: die Datei "/etc/services"




Wenn Sie einen Blick in die Datei "/etc/services" auf einem Linux-System werfen, finden Sie einen Link "port/protocol - service", der dem von Nmap angezeigten Link ähnelt:



![nmap-image](assets/fr/12.webp)



extrahiert den Inhalt der Datei "/etc/services" unter Linux._



Es ist wichtig zu verstehen, dass Nmap bis auf weiteres keine aktive Service-Erkennung durchgeführt hat. Es wäre zum Beispiel nicht in der Lage gewesen, den SSH-Dienst hinter einem TCP/80-Port zu identifizieren, wenn dies der Fall gewesen wäre. Deshalb ist es wichtig zu wissen, wie man die richtigen Optionen benutzt - das kommt bald!



Zu wissen, wie man die Ausgabe von Nmap interpretiert, ist ein wichtiger Teil der Beherrschung des Tools. Die gute Nachricht ist, dass diese Ausgabe weitgehend dieselbe ist, egal welche Optionen Sie verwenden.



#### C. Unter der Haube: Netzwerkanalyse mit Wireshark



Wenn Sie sich genau ansehen, was auf dem Netzwerk Interface des Hosts, der den Server scannt, oder auf dem des Servers selbst passiert, werden die Aktionen von Nmap viel klarer. Genau das werden wir hier tun.



Was ich Ihnen hier zeigen kann, ist nur ein Teil dessen, was in Wireshark sichtbar ist. Wenn Sie mehr erfahren möchten, können Sie selbst eine Netzwerkerfassung während eines Scans durchführen und dann die erfassten Daten durchsuchen.



In diesem Test befinden sich mein Scan-Host (192.168.1.18) und mein Zielhost (192.168.1.19) im selben lokalen Netzwerk.



Nmap beginnt damit, herauszufinden, ob der Zielhost im lokalen Netzwerk aktiv ist, indem es eine ARP-Anfrage sendet. Wenn es eine Antwort erhält, weiß es, dass der Host aktiv ist, und beginnt mit seinem Netzwerk-Scan:



![nmap-image](assets/fr/13.webp)



aRP-Anfrage, die von Nmap ausgegeben wird, um festzustellen, ob ein Zielhost im lokalen Netzwerk vorhanden ist



Wenn sich der zu scannende Host in einem entfernten Netzwerk befindet, beginnt Nmap mit dem Senden einer Ping-Anfrage und versucht, einige der am häufigsten exponierten Ports (TCP/80, TCP/443) zu erreichen:



![nmap-image](assets/fr/14.webp)



ping-Anfrage von Nmap, um festzustellen, ob ein Zielhost in einem entfernten Netz erreichbar ist



Erhält es bei einem dieser Tests eine Antwort, so gilt das Ziel als aktiv.



Sobald Nmap festgestellt hat, dass sein Ziel aktiv ist, versucht es, seinen Domainnamen mit dem auf der Netzwerkkarte konfigurierten DNS-Server aufzulösen:



![nmap-image](assets/fr/15.webp)



dNS-Auflösung auf dem Nmap-Scan-Ziel



Jetzt, da Nmap sein Ziel identifiziert hat und weiß, dass es aktiv ist, beginnt es mit dem TCP-Port-Scan:



![nmap-image](assets/fr/16.webp)



tCP SYN-Paketübertragung und RST/ACK-Empfang während des Nmap-Scans



Dazu sendet er an jedem TCP-Port in seinem Standardbereich **TCP SYN-Pakete und wartet auf eine Antwort**. Im obigen Screenshot empfängt er TCP RST/ACK-Pakete von dem gescannten Server, was bedeutet: "Weitergehen, hier gibt es nichts zu sehen" - mit anderen Worten, diese Ports sind geschlossen. Wie wir im Ergebnis gesehen haben, ist dies bei den meisten gescannten Ports der Fall. Mit zwei Ausnahmen:



![nmap-image](assets/fr/17.webp)



antwort auf ein TCP SYN-Paket, das an Port 22 gesendet wird, aktiv auf dem Scan-Ziel



Im obigen Screenshot sehen wir ein TCP SYN/ACK-Paket, das vom Zielhost** gesendet wurde. Der Port ist aktiv und stellt einen Dienst zur Verfügung. Nmap bestätigt den Empfang der Antwort und trennt dann die Verbindung (TCP RST/ACK). **So wusste es, dass der Port TCP/22 aktiv war**.



Wir haben hier gesehen, dass Nmap beim Scannen eines TCP-Netzwerks den "Three Way Handshake" respektiert. Aus Leistungsgründen kann man es bitten, nicht auf die Antwort des Servers zu antworten, und so beim Scannen eines großen Netzwerks mehrere tausend Pakete einsparen. Aber wir werden uns diese Optionen und Optimierungen später im Tutorium ansehen.



Wir haben jetzt eine bessere Vorstellung davon, wie man einen TCP-Scan durchführt und was dabei eigentlich passiert. Wir haben auch gesehen, dass Nmap standardmäßig einen TCP-Port-Scan an einer begrenzten Anzahl von Ports durchführt.



### III. Scannen von UDP-Ports mit Nmap



#### A. Erster UDP-Port-Scan mit Nmap



Sehen wir uns nun an, wie man die UDP-Ports eines Hosts scannt. Wie wir gesehen haben, scannt Nmap standardmäßig immer TCP-Ports. Das kann bedeuten, dass uns eine Menge Informationen entgehen, wenn wir uns dessen nicht bewusst sind.



Zur Erinnerung: Für die Zwecke dieses Tests befinden sich mein Scan-Host (192.168.1.18) und mein Ziel-Host (192.168.1.19) im selben lokalen Netzwerk.



```
nmap -sU 192.168.1.19
```



Hier hat die Rückgabe das gleiche Format wie bei einem TCP-Scan, aber die angezeigten aktiven Dienste sind wie gewünscht in `<Port>/UDP`!



![nmap-image](assets/fr/18.webp)



ergebnis eines einfachen UDP-Scans mit Nmap._



Die Option "-sU" wird verwendet, um Nmap mitzuteilen, dass Sie mit UDP arbeiten wollen und nicht mit TCP, wie es der Standard ist.



Übrigens werden Sie wahrscheinlich feststellen, dass Nmap für UDP-Scans "Root"-Rechte benötigt, wie schon weiter oben im Tutorial erwähnt.



hinweis: Seit den neuesten Versionen von Nmap wird immer empfohlen, UDP-Scans mit Administratorrechten auszuführen, um zuverlässige Ergebnisse zu gewährleisten, da einige Funktionen Rohzugriff auf Netzwerk-Sockets erfordern



UDP-Scans können sehr lange dauern (in meinem Beispiel 1100 Sekunden für den Scan von 1000 Ports), weil es bei UDP kein "Three Way Handshake" gibt, d.h. Nmap wartet auf eine Antwort auf jedes gesendete UDP-Paket und stuft den Port nur dann als "geschlossen" ein, wenn nach einer bestimmten Zeit (Timeout) keine Antwort erfolgt. Diese Antwort von gescannten Hosts erfolgt nicht systematisch und ist oft in Bezug auf die Anzahl der Antworten pro Sekunde begrenzt, um bestimmte Verstärkungsangriffe zu vermeiden. Dies steht im Gegensatz zu TCP, wo eine sofortige Antwort des gescannten Hosts erfolgt, unabhängig davon, ob der Port offen oder geschlossen ist. Wir werden später sehen, wie man dies optimieren kann.



Eine zweite Schwierigkeit bei UDP besteht darin, **dass Dienste nicht immer auf eingehende Pakete antworten**, ganz einfach, weil dies nicht immer notwendig ist und es das Prinzip von UDP ist. Wenn dies der Fall ist und kein ICMP "port unreachable" empfangen wird, wird der Dienst von Nmap als "offen|gefiltert" markiert, wie im Screenshot oben gezeigt.



#### B. Unter der Haube: Netzwerkanalyse mit Wireshark



Wie bei unserem TCP-Scan sehen wir uns nun genauer an, was bei einem UDP-Scan auf Netzwerkebene passiert, indem wir eine Wireshark-Analyse durchführen. Das Verhalten von Nmap bei der Feststellung, ob ein Host aktiv ist, ist dasselbe.



Der einzige wirkliche Unterschied beim Scannen von UDP ist, dass Nmap nicht auf ein "Three Way Handshake" wartet, da dieser Mechanismus in UDP (zustandsloses Protokoll) nicht existiert:



![nmap-image](assets/fr/19.webp)



übertragung von uDP-Paketen und Empfang von ICMP (Port unerreichbar) während des Nmap-Scans



Auf dem obigen Screenshot ist zu sehen, dass Nmap eine große Anzahl von UDP-Paketen sendet und für die meisten von ihnen ein ICMP-Paket "Destination unreachable (Port unreachable)" als Antwort erhält. Das ist normal, denn es ist die angemessene Antwort, die in [RFC 1122] (https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") definiert ist, wenn ein UDP-Port unerreichbar ist:



![nmap-image](assets/fr/20.webp)



auszug aus RFC 1122._



Schauen wir uns diese Wireshark-Aufnahme genauer an, die **die drei möglichen Szenarien** in UDP zeigt:



![nmap-image](assets/fr/21.webp)



netzwerkaufzeichnung während eines UDP-Scans auf verschiedenen Ports mit Nmap._



Die drei Fälle sind wie folgt:





- Das erste Exchange besteht aus den Paketen Nr. 3, 4 und 8, 9. Nmap sendet UDP-Pakete über den klassischen SNMP-Port und **konstruiert daher im Voraus protokollkonforme Pakete**. Anschließend erhält es eine Antwort vom Server (Pakete Nr. 8 und 9). Ergebnis: Nmap hat eine Antwort erhalten, der Dienst ist "offen".





- Das zweite Exchange besteht aus den Paketen 6 und 7. Nmap sendet ein "leeres" UDP-Paket (ohne Protokollstruktur) an Port UDP/165 und erhält ein ICMP-Paket als Antwort: "Ziel unerreichbar (Port unerreichbar)". Ergebnis: Nmap hat eine (negative) Antwort erhalten, der Host ist erreichbar, aber der Dienst, den es zu erreichen versuchte, ist an diesem Port nicht funktionsfähig, der als "geschlossen" markiert wird.





- Das letzte Exchange besteht aus Paket Nr. 12: Nmap sendet ein "leeres" UDP-Paket an Port UDP/1235. Es gibt keine Antwort, nicht einmal eine ausdrückliche Ablehnung vom gescannten Host. Ergebnis: Nmap markiert den Port als "offen|gefiltert", da es nicht sagen kann, ob dies auf das Vorhandensein einer Firewall zurückzuführen ist, die so konfiguriert ist, dass sie nicht antwortet, oder auf einen aktiven UDP-Dienst, der ohnehin keine Antwort zurückgibt (bei UDP nicht zwingend erforderlich).




Hier ist das Ergebnis, das Nmap nach diesen drei Fällen anzeigt:



![nmap-image](assets/fr/22.webp)



mögliche Ergebnisse eines mit Nmap durchgeführten UDP-Scans._



Wir haben jetzt eine bessere Vorstellung davon, wie man einen UDP-Scan durchführt und was dabei eigentlich passiert. Bisher haben wir Nmap nur auf sehr einfache Weise benutzt, ohne wirklich zu entscheiden, welche Ports gescannt werden sollen, aber das wird sich jetzt ändern!



### IV. Feinabstimmung des Port-Scannens mit Nmap



#### A. Zur Erinnerung an das Standardverhalten von Nmap



Wie wir gesehen haben, wählt Nmap selbst die Anzahl und die Ports aus, die gescannt werden sollen, wenn Sie keine Optionen angeben. Das ist die "Standardkonfiguration", die Nmap benutzt, wenn Sie ihm nicht genau sagen, was es tun soll. Diese Standardoptionen sollen eine Vorstellung von den wichtigsten freiliegenden Ports vermitteln, wobei diese nach Häufigkeit der Exposition (häufigste oder häufigste Ports) und nicht in numerischer Reihenfolge (Port 1, 2, 3 usw.) ausgewählt werden, und auch um zu vermeiden, dass ein Scan der 65535 möglichen Ports gestartet wird, wenn Sie nicht die entsprechenden Optionen angeben, was für einen "Standard"-Anwendungsfall zu lang und wortreich wäre.



**Wie werden diese Häfen ausgewählt?



Die 1000 Ports, die im Standardmodus gescannt werden, werden nach der Häufigkeit ihres Auftretens ausgewählt. Diese Statistiken werden von Nmap gepflegt und auf dieselbe Weise aktualisiert wie das Binary selbst und seine Skripte (Module). Sie können diese Statistiken selbst in der Datei "/usr/shares/nmap/nmap-services" einsehen:



![nmap-image](assets/fr/23.webp)



entnommen aus der Datei "/usr/shares/nmap/nmap-services"._



Hier, in der dritten Spalte, sehen wir etwas, das wie Wahrscheinlichkeiten (zwischen 0 und 1) oder eine prozentuale Verteilung aussieht. Dies ist die Häufigkeit des Auftretens jedes Port/Protokoll-Paares. Wir können sehen, dass die bekanntesten Ports (FTP, SSH, TELNET und SMTP in diesem Auszug) einen viel höheren Wert haben als die anderen.



#### B. Genaue Angabe der Zielports für einen Nmap-Scan



In der realen Welt müssen wir aber vielleicht nur einen bestimmten Port scannen, oder mehrere Ports, oder einen bestimmten Bereich von Ports. Nmap macht es einfach, genau das zu tun, und zwar auf einheitliche Weise sowohl für UDP- als auch für TCP-Scans.



**Scannen eines bestimmten Ports über Nmap**



Wenn wir einen einzelnen Port und nicht 1000 scannen wollen, können wir diesen Port mit der Nmap-Option "-p" oder "--port" angeben:



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Dadurch wird der Scan natürlich viel schneller, und Nmap sendet nur die Pakete aus, die nötig sind, um festzustellen, ob der Host aktiv ist, und dann, ob der angegebene Port erreichbar ist. Das spart Zeit, wenn Sie nur einen schnellen Test durchführen wollen, um zu sehen, ob der Webdienst auf Ihrer Showcase-Site noch aktiv ist.



**Mehrere Ports über Nmap scannen**



Auf die gleiche Weise können wir Nmap mehrere Ports angeben, indem wir dieselbe Option verwenden und die angegebenen Ports mit einem Komma aneinanderhängen:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Unabhängig von der Reihenfolge prüft Nmap alle diese Ports, und nur die auf dem Zielhost. Sie werden in der Ausgabe von Nmap feststellen, dass es uns **explizit alle Ports und ihren Status** mitteilt, auch wenn sie "geschlossen" sind. Im Gegensatz zum Standardverhalten, bei dem diese vollständige Ausgabe viel zu viel Platz in Anspruch genommen hätte:



![nmap-image](assets/fr/24.webp)



*Ergebnis eines Nmap-TCP-Scans auf den angegebenen Ports.*



**Scannen einer Reihe von Ports



Wenn die Anzahl der zu überprüfenden Ports zu groß ist, können Sie sie in einem Bereich angeben, z. B.:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Natürlich können Sie nach eigenem Ermessen kombinieren, zum Beispiel:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**TCP- und UDP-Port-Scannen



Sie können auch gleichzeitig UDP- und TCP-Scans auf ausgewählten Ports durchführen:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



Sie werden in diesem letzten Beispiel das Vorhandensein von "U:" zur Kennzeichnung eines UDP-Ports und "T:" zur Kennzeichnung eines TCP-Ports bemerken. Hier ist eine mögliche Ausgabe dieser Art von Scan:



![nmap-image](assets/fr/25.webp)



*Ergebnis eines TCP- und UDP-Port-Scans mit Nmap.*



Das ist ein interessanter Weg, um Ihre Scans zu individualisieren!



**Scannen aller Ports



Schließlich ist es möglich, Nmap viel größere oder kleinere Bereiche anzugeben. Wir haben gesehen, dass die von Nmap ausgewählte Standardliste 1000 Ports enthält. Wir können auch die 100 häufigsten Ports oder die 200 häufigsten Ports mit der Option "--top-ports" abfragen:



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Schließlich können wir ihn bitten, alle möglichen Ports (alle 65535) zu scannen, indem wir die Schreibweise "-p-" verwenden:



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



Letzteres dauert zwar länger, vor allem bei UDP, aber Sie können sicher sein, dass Sie keinen offenen Port übersehen.



*Hinweis: Die Option "-p-" ist die empfohlene Methode zum Scannen aller TCP-Ports. Bei UDP-Scans ist es ratsam, die Anzahl der Ports aus Leistungsgründen zu begrenzen, da vollständige Scans aller UDP-Ports sehr viel Zeit in Anspruch nehmen können.*



Später im Tutorial werden wir sehen, wie wir die Geschwindigkeit von Nmap-Scans für unsere Bedürfnisse optimieren können, was besonders für Scans auf allen TCP- und UDP-Ports nützlich sein wird.



### V. Schlussfolgerung



In diesem Abschnitt haben wir endlich etwas praktische Erfahrung gesammelt, so dass wir jetzt wissen, **wie man Nmap auf grundlegende Weise benutzt, um die TCP- und UDP-Ports eines Hosts zu scannen**. Wir haben uns auch im Detail angesehen, was auf Netzwerkebene passiert und **wie Nmap feststellt, ob ein TCP- oder UDP-Port aktiv ist oder nicht**. Schließlich wissen wir, wie wir die Ports, die wir scannen wollen, fein säuberlich auswählen und **was Nmaps Standardoptionen eigentlich tun**. Im Folgenden werden wir dieses Wissen wiederverwenden und es auf das Scannen eines ganzen Netzwerks anwenden, einschließlich des globalen Mappings und der Netzwerkerkennung.




## 5 - Netzwerkabbildung und -erkennung mit Nmap



### I. Präsentation



In diesem Abschnitt lernen wir, wie Sie das Netzwerk-Scan-Tool Nmap verwenden, um Ihr Netzwerk abzubilden. Wir werden sehen, wie effektiv es bei dieser Aufgabe sein kann, indem wir seine verschiedenen Optionen nutzen. Zum Schluss sehen wir uns verschiedene Möglichkeiten an, Nmap die Ziele unserer Scans mitzuteilen.



Insbesondere werden wir das verwenden, was wir im vorherigen Abschnitt darüber gelernt haben, wie Nmap feststellt, ob ein Host aktiv und erreichbar ist.



Wie in der Einführung zu Nmap erwähnt, handelt es sich um einen Network Mapper. Als solches ist es das perfekte Tool, um eine Liste der erreichbaren Hosts in einem Netzwerk zu erstellen, egal ob lokal oder remote.



**Wiederkehr des Autors:**



Als Auditor und Pentester für Cybersicherheit verwende ich Nmap systematisch, wenn ich interne Penetrationstests durchführe, um herauszufinden, wo ich mich befinde, wer meine Nachbarn im lokalen Netz sind und welche anderen Netze zugänglich sind, sowie die Systeme, die sich dort befinden. Mein Ziel ist einfach: das Netzwerk abzubilden, die Größe des Informationssystems zu bestimmen und vor allem seine Angriffsfläche zu skizzieren.



Netzwerk-Mapping kann auch im Zusammenhang mit Netzwerkdiagnose, Überwachung und Asset-Mapping nützlich sein (sind Sie wirklich sicher, dass Ihr IS nur aus dem besteht, was im Active Directory oder in Ihrem GLPI/OCS Inventory steht? Es kann auch verwendet werden, um das Vorhandensein von Schatten-IT in Ihrem Informationssystem zu erkennen.



### II. Nmap zum Scannen eines Netzwerkbereichs verwenden



#### A. Entdeckung eines Netzwerks mit einem Nmap-Scan



Wir möchten nun einen Gang höher schalten und unser gesamtes lokales Netzwerk analysieren. Nichts könnte einfacher sein: Wir brauchen nur die Befehle aus dem vorigen Abschnitt zu wiederholen, aber anstelle einer einfachen IP Address eine CIDR anzugeben.



CIDR (**Classless Inter Domain Routing**) ist die "klassische" Notation zur Angabe eines Netzbereichs und seiner Ausdehnung (unter Verwendung der Maske). Zum Beispiel ist "192.168.0.0/24" eine "Übersetzung" der dezimalen Maskenschreibweise "255.255.255.0".



Um Nmap durch Angabe einer CIDR zu verwenden, können wir es wie folgt einsetzen:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



Es ist auch möglich, wie bei den Ports im vorherigen Abschnitt, mehrere Hosts, mehrere Netzwerke oder einen Bereich anzugeben:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



Hier ein Beispiel für die Ergebnisse, die bei einem Scan in einem Netzwerk erzielt werden können:



![nmap-image](assets/fr/26.webp)



ergebnisse eines Nmap-Scans zur Abbildung mehrerer Netzwerke



Insbesondere sehen wir mehrere aktive Hosts, und jeder Host-Abschnitt beginnt mit einer Zeile wie dieser:



```
Nmap scan report for <name> (<IP>)
```



Auf diese Weise können wir klar erkennen, auf welchen Host sich die folgenden Ergebnisse beziehen. Die allerletzte Zeile ist ebenfalls wichtig:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Wir wissen, dass Nmap in den gescannten Netzwerken 5 aktive Hosts entdeckt hat.



#### B. Unter der Haube: Netzwerkanalyse mit Wireshark



Wir werden uns nun genauer ansehen, was auf Netzwerkebene bei einer mit Nmap durchgeführten Netzwerkerkennung passiert.



Wie wir im vorigen Abschnitt gesehen haben, verwendet Nmap standardmäßig das ARP-Protokoll, um die Anwesenheit von Hosts im lokalen Netzwerk zu erkennen:



![nmap-image](assets/fr/27.webp)



aRP-Pakete, die beim Scannen eines lokalen Netzes mit Nmap und seinen Standardoptionen erfasst wurden



Auf diese Weise können praktisch alle Hosts im lokalen Netz erkannt werden, da die Antwort auf eine ARP-Anfrage in der Regel von allen im Netz aktiven Hosts stammt und in keiner Weise verdächtig erscheint.



Für entfernte Netzwerke verwendet Nmap eine Kombination von Techniken:



![nmap-image](assets/fr/28.webp)



iCMP- und TCP-Pakete, die beim Scannen eines entfernten Netzwerks mit Nmap und seinen Standardoptionen erfasst werden



Um genauer zu sein, verwendet Nmap ein ICMP-Echo-Paket (der klassische Fall von Ping) und ein ICMP-Timestamp-Paket, das normalerweise zur Berechnung der Paketlaufzeiten verwendet wird. Es hofft, eine Antwort von Hosts in entfernten Netzen zu erhalten.



Aber es steckt noch mehr dahinter. In der obigen Wireshark-Aufnahme können Sie sehen, dass **TCP SYN**-Pakete systematisch an TCP/443-Ports jedes potenziellen Hosts in den zu scannenden Netzwerken gesendet werden, ebenso wie **TCP ACK**-Pakete an TCP/80-Port.



**Warum TCP-Pakete an Ports als Teil der Netzwerkerkennung senden?



Durch das Senden eines SYN-Pakets an einen bestimmten Port kann Nmap **bestimmen, ob ein Dienst an diesem Port lauscht**. Wenn ein Host auf ein SYN-Paket mit einem SYN/ACK-Paket antwortet, zeigt dies an, dass er aktiv ist und dass ein Dienst an diesem Port lauscht. Nmap versucht also sein Glück bei diesem Dienst, **auch wenn keine Antwort auf den Ping erhalten wurde**.



Durch das Senden eines ACK-Pakets an einen bestimmten Port kann Nmap **bestimmen, ob eine Firewall auf diesem Host vorhanden ist**. Wenn ein Host auf ein ACK-Paket mit einem RST-Paket (Reset) antwortet, zeigt das an, dass auf diesem Host wahrscheinlich eine Firewall vorhanden ist und unerwünschten Verkehr blockiert. Der Host verrät damit seine Anwesenheit im Netz, auch wenn er auf andere Anfragen nicht geantwortet hat.



Es ist jedoch wichtig zu beachten, dass die Firewall-Erkennung mit dieser Technik nicht in allen Fällen absolut zuverlässig ist. Einige Hosts können generate RST-Antworten aus anderen Gründen als dem Vorhandensein einer Firewall verweigern, z. B. wegen bestimmter Dienste oder Betriebssystemkonfigurationen. Außerdem können moderne Firewalls so konfiguriert werden, dass sie auf Erkennungsversuche dieser Art nicht reagieren.



Wir haben nun einen weiten Weg zurückgelegt und können eine grundlegende Netzwerkerkennung durchführen. Jetzt werden wir uns ein paar weitere Optionen ansehen, die uns mehr Kontrolle über das Verhalten von Nmap geben.



### III. Netzwerkerkennung ohne Port-Scanning mit Nmap



Wie Sie vielleicht bemerkt haben, führt Nmap standardmäßig **einen Port-Scan durch, nachdem es einen aktiven Host entdeckt hat**, was zu einer riesigen Anzahl von Paketen und zum Warten auf Antworten auf unseren Scan führt. Wenn Sie 5 Hosts in Ihrem Netzwerk haben, wird Nmap versuchen, den Status von etwa 5.000 Ports zu überprüfen, was länger dauert.



Es ist jedoch möglich, die Optionen von Nmap zu nutzen, um **nur eine Erkennung aktiver Hosts** in einem Netzwerk durchzuführen, ohne deren Dienste zu erkennen.



Wenn wir nur wissen wollen, welche Hosts erreichbar sind, ohne Informationen über die Dienste und Ports, die sie bereitstellen, dann können wir die Option "-sn" verwenden, um **nur einen Scan mit ICMP Echo (ping) und ARP-Anfragen** durchzuführen. Mit anderen Worten, deaktivieren Sie das Port-Scanning vollständig:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Hier ist das Ergebnis einer Nmap-Netzwerkerkennung, die ohne Port-Scanning durchgeführt wurde:



![nmap-image](assets/fr/29.webp)



Ergebnis einer Netzwerkerkennung ohne Port-Scanning mit Nmap.



Wir haben bereits die möglichen Einschränkungen bei der alleinigen Verwendung von ICMP zur Host-Erkennung (für entfernte Netzwerke) erwähnt. Deshalb verwendet Nmap auch ein paar Tricks, die das Vorhandensein einer Firewall oder eines bestimmten Dienstes auf Hosts verraten können. Mit Hilfe von Optionen können wir diese Tricks wiederverwenden und sogar erweitern, ohne wieder mit einem kompletten Port-Scan jedes entdeckten Hosts beginnen zu müssen.



Dazu verwenden wir die Optionen "-PS" (TCP SYN) und "-PA" (TCP ACK), mit denen wir die Ports angeben können, denen wir bei der Host-Erkennung beitreten wollen, sowie die Option "-PP":



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Dieser Scan stellt bereits sicher, dass die Host-Erkennung ein wenig vollständiger ist als bei den Standardoptionen.



Wir fangen an, ziemlich umfassende Befehle zu bekommen, die mehrere Optionen verwenden. Das liegt daran, dass wir wissen, wie Nmap funktioniert und die Grenzen seiner "Standard"-Optionen kennen, die manchmal dazu führen können, dass wir Zeit verschwenden oder wichtige Elements übersehen. Genau darum geht es, wenn man sich die Zeit nimmt, es zu beherrschen!



Um die Optionen unserer letzten Bestellung zu erläutern:





- "`-sn`: Deaktiviert das Port-Scanning für jeden aktiven Host, der von Nmap entdeckt wurde.





- pP": aktiviert ICMP-Echo (Ping-Scan) zur Host-Erkennung.





- "`-PS <PORT>`": sendet ein TCP SYN-Paket an den angegebenen Port(s), um einen aktiven Dienst zu erkennen, der die Anwesenheit eines Hosts verrät, der nicht auf den Ping geantwortet hat.





- "`-PA <PORT>`": sendet ein TCP ACK-Paket auf dem/den angegebenen Port(s), um eine aktive Firewall zu erkennen, die die Anwesenheit eines Hosts verrät, der nicht auf den Ping geantwortet hat.




Im obigen Beispiel gebe ich für die Option "-PS" die Ports an, die meiner Meinung nach in meinen Nmap-Kontexten am häufigsten exponiert sind. Diese verschiedenen Ports werden dann auf jedem Host getestet, nicht um zu sehen, ob der Dienst, den sie hosten, wirklich aktiv ist, sondern um zu sehen, ob wir auf diese Weise einen Host entdecken können, der nicht auf unser ICMP-Echo geantwortet hat, obwohl er noch aktiv ist (durch eine Antwort des Dienstes oder der Firewall des Hosts).



Hier sehen Sie, was in einer Netzwerkaufzeichnung zu sehen ist, die zum Zeitpunkt eines solchen Scans gemacht wurde, in diesem Fall ein Extrakt auf einem einzelnen Zielhost:



![nmap-image](assets/fr/30.webp)



pakete, die von Nmap bei der erweiterten Netzwerkerkennung gesendet werden, ohne Port-Scanning



Wir finden unsere TCP SYN-Pakete, unsere TCP ACK auf Port TCP/80 und unser ICMP-Echo. Nmap führt all diese Tests für jeden Host durch, der von unserem Netzwerkerkennungsscan erfasst wird.



### IV. Verwendung einer Datei mit Assets als Ziel für Nmap



Die Angabe von Zielen kann sich in realen Informationssystemen, die manchmal aus Dutzenden oder Hunderten von Netzen, Subnetzen und VLANs bestehen, schnell als komplex erweisen. Deshalb ist es einfacher, eine Datei als Quelle für Nmap zu verwenden, als sie einzeln in der Kommandozeile anzugeben.



Erstellen Sie zunächst eine einfache Datei mit einem Eintrag pro Zeile:



![nmap-image](assets/fr/31.webp)



datei mit einem Ziel (Host oder Netzwerk) pro Zeile



Als nächstes können wir alle bisher gesehenen Nmap-Optionen verwenden und die Option "-iL <Pfad/Datei>" angeben:



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Nmap wird dann alle in unserer Datei enthaltenen Ziele in seinen Scan einbeziehen.



Wenn Sie sicher sein wollen, dass alle Ihre Ziele berücksichtigt werden, können Sie die Option "-sL -n" verwenden. Nmap interpretiert dann nur die CIDRs und Hosts in der Datei und zeigt sie Ihnen an, ohne irgendwelche Pakete über das Netzwerk zu senden:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Dadurch wird sichergestellt, dass die Liste der zu überprüfenden Hosts korrekt ist.



Ein letzter wichtiger Tipp, den ich mit Ihnen teilen möchte, betrifft den **Ausschluss von Hosts oder Netzwerken im Rahmen eines Scans**. Die Notwendigkeit, einen Host auszuschließen, kann in einer Reihe von Fällen notwendig sein, insbesondere wenn wir sicher sein wollen, dass **eine sensible Komponente des Informationssystems nicht durch unsere Scans gestört oder unterbrochen wird**.



Ein häufiges Beispiel für einen solchen Bedarf sind Unternehmen, die über industrielle (SPS) oder medizinische Geräte verfügen. Solche Geräte sind manchmal schlecht konzipiert und überhaupt nicht dafür gedacht, schlecht formatierte Pakete oder zu viele davon zu empfangen. Aus offensichtlichen Gründen der Verfügbarkeit oder des geschäftlichen/menschlichen Risikos ist es besser, sie von der Prüfung auszuschließen.



Um IP-Adressen oder Netzwerke von unserem Scan auszuschließen, können wir die Nmap-Option "--exclude" verwenden, zum Beispiel:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



In diesem Beispiel scanne ich das Netzwerk "192.168.1.0/24", schließe aber den dort befindlichen Host "192.168.1.140" aus. Nmap wird keine Pakete an diesen Host senden. Ein weiteres Beispiel mit Subnetz-Ausschluss:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



In ähnlicher Weise scanne ich das große Netzwerk "10.0.0.0/16", aber das Netzwerk "10.0.100.0/24" wird nicht gescannt. Auch hier empfehle ich, die Option "-sL -n" zu verwenden, um einen klaren Überblick darüber zu erhalten, welche Hosts gescannt werden und welche vom Scan ausgeschlossen werden, insbesondere wenn Sie in einem sensiblen Umfeld arbeiten.



### V. Netzwerkerkennung und Port-Scanning



Wir können nun das, was wir in diesem Abschnitt gelernt haben, mit dem kombinieren, was wir im vorherigen Abschnitt über Port-Scan-Optionen gelernt haben. Wir haben gesehen, dass Nmap standardmäßig die 1000 häufigsten Ports auf jedem aktiven Host scannt, den es entdeckt. Wir haben gesehen, wie wir dieses Verhalten verhindern können, wenn wir es nicht wollen, aber wir können es vollständig kontrollieren und sogar erweitern, wenn es unseren Bedürfnissen entspricht.



Der folgende Befehl prüft zum Beispiel, ob auf jedem gescannten Host ein Dienst auf Port TCP/22 lauscht:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap führt zunächst eine Netzwerkerkennung durch, um die aktiven Hosts aufzulisten, und prüft für jeden von ihnen, ob ein Dienst auf Port TCP/22 vorhanden ist.



Auf die gleiche Weise können wir einen vollständigen Scan aller TCP-Ports auf jedem Host durchführen, der im Netz "192.168.0.0/24" entdeckt wurde, mit Ausnahme des Hosts "192.168.0.4" zum Beispiel:



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Es steht Ihnen frei, alle bisher erlernten Möglichkeiten nach Ihren eigenen Bedürfnissen zu kombinieren.



### VI. Schlussfolgerung



In diesem Abschnitt haben wir gesehen, wie man Nmap benutzt, um das Netzwerk mit verschiedenen Optionen abzubilden. Wir haben jetzt ein fein abgestimmtes Verständnis der Ziele unserer Scans sowie des Port-Scan-Verhaltens und der Host-Erkennungsmethode von Nmap. Und am wichtigsten ist, dass wir wissen, wie Nmap sich standardmäßig verhält und wo seine Grenzen liegen und wie man seine Hauptoptionen nutzt, um weiterzukommen.



Im nächsten Abschnitt sehen wir uns die Mechanismen und Optionen an, um die Versionen der von Nmap gescannten Dienste und Betriebssysteme zu ermitteln.




## 6 - Erkennung von Dienst- und Betriebssystemversionen mit Nmap



### I. Präsentation



In diesem Abschnitt lernen wir, wie man Nmap benutzt, um die Versionen von Diensten und Betriebssystemen, die von gescannten Hosts benutzt werden, zu erkennen und genau zu bestimmen. Wir sehen uns im Detail an, wie Nmap diese Aufgabe erfüllt, und gehen auf die Einschränkungen des Tools ein, um seine Ergebnisse besser zu verstehen und zu interpretieren.



Wie wir in früheren Abschnitten dieses Tutorials gesehen haben, schaut Nmap standardmäßig nicht nach, welcher Dienst auf den Ports liegt, die es scannt und als offen betrachtet. Wenn Sie also einen Webdienst auf Port TCP/22 abhören, wird Nmap ihn weiterhin als offen melden, aber als `SSH'-Dienst. Das liegt daran, dass es eine [Datenbank](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) auf Ihrem System benutzt, um nach einer Beziehung zwischen einem Port/Protokoll und dem Namen eines Dienstes zu suchen (die Datei `/etc/services/`).



In den meisten Fällen liefert Ihnen [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) die richtigen Informationen, da solche Fälle in einer Produktionsumgebung nur selten vorkommen. Die verbleibenden Fälle sind jedoch Situationen, in denen ein klassischer Dienst ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP usw.) an einem nicht-klassischen Port (z.B. 2022 für einen SSH-Dienst) offengelegt wird; in diesem Fall wird Nmap in seiner lokalen Datenbank keine Übereinstimmung finden oder eine, die nicht der Realität entspricht, und Sie werden wichtige Informationen verpassen.



Glücklicherweise bietet Nmap sehr präzise Optionen und Mechanismen, um herauszufinden, welcher genaue Dienst sich hinter einem offenen Port verstecken könnte. Es hat sogar eine Datenbank mit Abfragen und Signaturen, um genaue Technologien und Versionen zu identifizieren. Zusätzlich zu den Diensten kann Nmap auch die verwendete Technologie und ihre Version identifizieren.



Damit werden wir uns in diesem Abschnitt befassen.



### II. Wie man eine Technologie oder Version erkennt



#### A. Erinnerung daran, wie man eine Technologie oder Version identifiziert



Die Identifizierung einer Technologie und einer Version umfasst die Abfrage des Namens des Dienstes, des CMS, der Anwendung oder der Software, die auf dem betreffenden Port überwacht wird. Eine Webseite wird zum Beispiel von einem CMS (WordPress) verwaltet, von einem Webdienst (Apache, IIS, Nginx) ausgeführt und von einem Server (Linux oder Windows) gehostet. Aber woher wissen Sie, welcher Webdienst läuft?



Die klassische Methode, um diese Informationen herauszufinden, ist das _Banner Grabbing_, das einfach darin besteht, die Stelle ausfindig zu machen, an der der betreffende Dienst diese Informationen anzeigt, und die Daten zu lesen. Sehr oft zeigen Dienste in ihrer Standardkonfiguration oder -verarbeitung ihren Namen und sogar ihre Version als erste Antwort nach einer Verbindung an.



![nmap-image](assets/fr/32.webp)



eine Version anzeigen, sobald eine TCP-Verbindung von einem FTP-Dienst aufgebaut wird



Hier sehen wir, dass eine einfache TCP-Verbindung zu diesem Dienst über `telnet` zu einem TCP-Paket führt, das seine Technologie und Version enthält.



Sobald Sie eine Vorstellung von der Art des Dienstes haben, mit dem Sie es zu tun haben, können Sie auch spezifische Befehle oder Anfragen an diesen Dienst senden, um Informationen von ihm zu erhalten. Diese Anfragen/Befehle können auch blind gesendet werden (ohne sicher zu sein, dass es sich um den richtigen Diensttyp handelt), in der Hoffnung, dass einer von ihnen eine Antwort des betreffenden Dienstes hervorruft.



In anderen, fortgeschritteneren Fällen ist es notwendig, bestimmte Pakete zu senden, um eine Reaktion auszulösen, z. B. einen Fehler, der detaillierte Informationen über die verwendete Version oder Technologie liefert.



Wie Sie sich vorstellen können, verwendet Nmap all diese Techniken, um die genaue Art des Dienstes zu identifizieren, der auf einem Port gehostet wird, sowie den Namen seiner Technologie und Version.



#### B. Nmap-Sonden und -Übereinstimmungen verstehen



Um all diese Prüfungen für jeden gescannten Port durchzuführen, verwendet Nmap eine lokale Datenbank, die häufig aktualisiert wird (genau wie das Binary oder seine Module). Es handelt sich um eine Textdatei mit mehreren tausend Zeilen: `/usr/share/nmap/nmap-service-probes`.



Diese Datei besteht aus zahlreichen Einträgen, die alle nach zwei Hauptleitlinien organisiert sind:





- Die `Probe`: Das ist die Definition des Pakets, das Nmap senden wird, um eine Reaktion des zu identifizierenden Dienstes zu provozieren. Betrachten Sie es als einen blinden Versuch wie _Hallo? Guten Tag? Hallo? Um... Buenos Dias vielleicht?_. Sobald der angepeilte Dienst eine Sonde empfängt, die er versteht (d.h. die das richtige Protokoll spricht), antwortet er Nmap, das dann die Bestätigung hat, um welche Art von Dienst es sich handelt.





- Match": Dies sind reguläre Ausdrücke, die Nmap auf die erhaltene Antwort anwendet. Wenn das Senden einer HTTP-GET-Anfrage eine Antwort des Dienstes hervorgerufen hat, wendet es Dutzende von regulären Ausdrücken auf diese Antwort an, um das Vorhandensein von z.B. dem Wort "Apache", "Nginx", "Microsoft IIS" usw. zu identifizieren.




Es gibt noch ein paar andere Direktiven für spezielle Fälle, aber die wichtigsten, um zu verstehen, wie Nmap funktioniert, und um seine Benutzung anzupassen, sind diese. Um diesen theoretischen Teil etwas konkreter zu machen, hier ein Beispiel:



![nmap-image](assets/fr/33.webp)



beispiel für eine Sonde in der Nmap-Datei `/usr/share/nmap/nmap-service-probes`



In der ersten Zeile dieses Beispiels sehen wir eine leicht verständliche Probe namens `GetRequest`. Es handelt sich um ein TCP-Paket, das eine leere HTTP-GET-Anfrage an das Webdienst-Root mit HTTP/1.0 enthält, gefolgt von einem Zeilenvorschub und einer Leerzeile.



Die Zeile "Ports" teilt Nmap mit, an welchen Port diese Sonde gesendet werden soll. So können Sie Tests priorisieren und Zeit sparen.



Schließlich haben wir noch zwei Beispiele für `match`. Das erste Beispiel kategorisiert den gescannten Webdienst als "ajp13", wenn der in dieser Zeile enthaltene reguläre Ausdruck mit der erhaltenen Dienstantwort übereinstimmt.



Damit Sie besser verstehen, wie Sonden aussehen können, finden Sie hier eine Liste einiger Sonden, die Sie in dieser Datei finden werden (zum Zeitpunkt der Erstellung dieses Tutorials gibt es insgesamt 188).



![nmap-image](assets/fr/34.webp)



beispiel für mehrere von Nmap verwendete Sonden, die in der Datei `/usr/share/nmap/nmap-service-probes`._ enthalten sind



Die ersten beiden (`NULL` und `GenericLines`) sind hier von besonderem Interesse, da sie einfach ein leeres TCP-Paket oder eines mit einem Zeilenumbruch senden. Serverdienste melden sich oft genau dann, wenn eine Verbindung eingegangen ist, ohne dass eine bestimmte Aktion, ein Befehl oder eine Anfrage vom Client vorliegt.



Hier ist der Fall eines etwas komplexeren _match_:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



Der genaue reguläre Ausdruck ist hier zwischen dem "m" und dem "|" enthalten, das jeden regulären Ausdruck in dieser Datei abgrenzt. Bitte nehmen Sie sich die Zeit, dieses Beispiel vollständig zu lesen. Sie werden eine Auswahl im regulären Ausdruck bemerken: `([\d.]+)`, die dazu dient, eine Version zu isolieren. Dieses Beispiel definiert auch andere Elements wie den Produktnamen `p/nginx/`, die abgerufene Version `v/$1/` und das CPE mit der Version `cpe:/a:igor_sysoev:nginx:$1/`.



Eine CPE (Common Platform Enumeration) ist ein standardisiertes Notationssystem zur Identifizierung und Beschreibung von Software und Hardware. Dieses Format ermöglicht eine effizientere Verwaltung von Schwachstellen und Sicherheitskonfigurationen und vor allem eine einheitliche Darstellung, unabhängig vom jeweiligen Produkt. Hier sind zwei Beispiele für CPE: "cpe:/o:microsoft:windows_8.1:r1" und "cpe:/a:apache:http_server:2.4.35"



Hier werden die Typen "o" für das Betriebssystem, "a" für die Anwendung, den Hersteller, das Produkt und die Versionen eindeutig identifiziert.



Bei einer _Übereinstimmung_ mit einem dieser regulären Ausdrücke erhalten wir also nicht nur den Namen des Dienstes, sondern auch seine Version und den genauen CPE, was es einfacher macht, CVEs zu finden, die diese Version betreffen. Diese Informationen finden Sie in der Standardausgabe von Nmap, und Sie werden sehen, dass sie für andere Zwecke, die wir in einigen Abschnitten behandeln werden, sehr nützlich sind.



Die genaue Syntax von _matches_ und, allgemeiner, der Direktiven in der Datei `/usr/share/nmap/nmap-service-probes` hört damit nicht auf und kann ziemlich komplex erscheinen, wenn Sie es nicht gewohnt sind, Nmap und seine Ergebnisse zu manipulieren. Sie sollten sich aber zumindest ihre Existenz und allgemeine Funktionsweise merken, was später sehr nützlich sein wird, wenn Sie ein Ergebnis verstehen oder debuggen, einen Scan anpassen oder sogar zur Nmap-Entwicklung beitragen wollen.



### III. Nmap zum Aufspüren von Versionen verwenden



Jetzt werden wir all diese komplexen _Probe_- und _Match_-Mechanismen über eine einfache Option verwenden: `-sV`. Sie sagt Nmap einfach: Versuche, genau herauszufinden, welche Dienste und Versionen von Ports du als offen angegeben hast.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



Hier ist ein vollständiges Beispiel für das Ergebnis eines solchen Befehls:



![nmap-image](assets/fr/35.webp)



ergebnisse der Nmap-Versionserkennung von Anwendungen, die im Netz ausgesetzt sind



Hier sehen wir, dass Nmap es geschafft hat, alle Versionen von Netzwerkdiensten zu identifizieren, die von diesem Ziel ausgesetzt sind, und diese Informationen in einer neuen Spalte `VERSION` anzeigt. Es ist möglich, ziemlich genaue Informationen zu sehen, sogar bis hin zum Betriebssystem, wenn diese Informationen Teil der wiederhergestellten Signatur sind.



Um im Detail zu verstehen, was während eines Schwachstellen-Scans passiert, können wir die Option `--version-trace` verwenden. Damit wird eine Ansicht im Debug-Modus bereitgestellt, die die _Probe_ anzeigt, die zur Erkennung geführt hat:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



Das Ergebnis ist, dass wir eine Menge an Informationen zu sortieren haben. Versuchen Sie, Zeilen zu finden, die mit "Service scan Hard match" beginnen. Sie werden dann Zeilen wie diese sehen:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Es ist deutlich zu erkennen, welche _Sonden_ zur Erkennung der Technologie und der Version verwendet wurden (in diesem Fall die _NULL_- und die _GetRequest_-Sonden), sowie die abgerufenen Informationen.



### IV. Beherrschung von Tests und Nachweisgenauigkeit



Wir kehren nun zu einer Direktive in der Datei `/usr/share/nmap/nmap-service-probes` zurück, die wir uns vorher nicht angeschaut haben:



![nmap-image](assets/fr/36.webp)



probes `rarity`-Direktive in der Datei `/usr/share/nmap/nmap-service-probes`._



Diese Direktive wird verwendet, um die Seltenheit (d.h. die Priorität/Wahrscheinlichkeit) einer _Probe_ anzugeben. Mit dieser Notation von 1 bis 9 können Sie die Vollständigkeit der von Nmap beim Senden von _Probes_ durchgeführten Analyse steuern. In Nmaps "Notationssystem" liefert eine Seltenheit von 1 in den allermeisten Fällen Informationen, während eine Seltenheit von 8 oder 9 einen sehr speziellen Fall darstellt, der sich auf eine Konfiguration oder einen Dienst bezieht, der nur selten vorkommt.



Zur Verdeutlichung: Im Standardfall sendet Nmap an jeden zu identifizierenden Dienst die _Sonden_, die eine Seltenheit von 1 bis 7 haben. Um Ihnen eine bessere Vorstellung von der Verteilung der _Sonden_ nach _Seltenheit_ zu geben, sehen Sie hier ihre Anzahl:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Es mag kontraintuitiv erscheinen, dass es mehr `Rarität` 8 und 9 gibt als den Rest. Das liegt genau daran, dass Probes der Seltenheit 1 allgemein sind und in den meisten Fällen funktionieren, unabhängig vom Dienst (denken Sie an die "NULL"-Sonde, die einfach ein leeres TCP-Paket sendet). Die komplexeren Sonden hingegen sind für jeden Dienst nahezu einzigartig.



Wenn wir die Sonden, die wir in unserem Versionsscan verwenden wollen, manuell verwalten wollen, können wir die Option `--version-intensity` verwenden. Hier sind zwei Beispiele:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Zum Abschluss dieses Themas hier ein Beispiel für _Probe_ 9 und 8:



![nmap-image](assets/fr/37.webp)



beispiele für Probe bei Seltenheit 8 und 9 in der Datei `/usr/share/nmap/nmap-service-probes`._



Diese beiden _Sonden_ erkennen Quake1 und Quake2 Server (das Videospiel). Interessant für die nostalgische Seite, aber unwahrscheinlich, dass sie im Alltag von großem Nutzen sind.



Je nachdem, ob Sie Präzision oder Schnelligkeit benötigen, sollten Sie bedenken, dass dieses "Seltenheits"-Prinzip existiert und das Ergebnis beeinflussen kann.



### V. Nmap zum Aufspüren von Betriebssystemen verwenden



Jetzt sehen wir uns an, wie Nmap uns helfen kann, die Betriebssysteme von Hosts zu erkennen, die in einem Netzwerk gescannt und entdeckt werden. Dazu benutzen wir die Nmap-Option `-O` (für `OS Scan`).



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



Hier ist ein Beispiel für die Ergebnisse. Hier sagt uns Nmap, dass es sich wahrscheinlich um ein Linux-Betriebssystem handelt, und bietet uns verschiedene Statistiken zu seiner genauen Version.



![nmap-image](assets/fr/38.webp)



ermittlung der Wahrscheinlichkeit der Identifizierung eines Betriebssystems durch Nmap



Um dies zu erreichen, verwendet Nmap eine Vielzahl von Techniken, die sehr ähnlich wie _Probes_ und _Matches_ zur Technologie- und Versionserkennung funktionieren. Der Hauptunterschied ist, dass Nmap ziemlich "einfache" Parameter von ICMP, TCP, UDP und anderen Protokollen verwendet. Hier sind zwei Testbeispiele für die Erkennung eines Microsoft Windows 11-Betriebssystems:



![nmap-image](assets/fr/39.webp)



beispiele für Tests, die Nmap zum Aufspüren eines Windows-11-Betriebssystems durchführt



Seien wir ehrlich, diese Tests sind sehr schwer zu interpretieren, und wir werden nicht versuchen, sie im Rahmen eines einführenden Nmap-Tutorials in der Tiefe zu verstehen. Wenn Sie tiefer in das Thema einsteigen wollen, finden Sie die Datei mit diesen Informationen unter `/usr/share/nmap/nmap-os-db`.



Sie müssen sich jedoch darüber im Klaren sein, dass die Erkennung des Betriebssystems eher eine von Nmap ermittelte Wahrscheinlichkeit als eine Gewissheit ist.



### VI. Schlussfolgerung



In diesem Abschnitt haben wir gelernt, wie man die Optionen von Nmap nutzt, um die Technologien, Versionen und Betriebssysteme von gescannten Hosts und Services zu erkennen. Wir haben jetzt ein gutes Verständnis davon, wie Nmap diese Informationen aus der Ferne beschafft. Wir haben auch die Optionen zur Verwaltung der Ausführlichkeit und der Testgenauigkeit sowie die Einschränkungen des Tools bei diesen Themen besprochen.



Im nächsten Abschnitt lernen wir, wie wir die NSE-Skripte von Nmap verwenden, um eine Sicherheitsanalyse unseres Informationssystems durchzuführen. Nehmen Sie sich die Zeit, die letzten Abschnitte noch einmal zu lesen, wenn es nötig ist, und zögern Sie nicht, selbst zu üben und in die Tiefen des Tools einzudringen, um das bisher Gelernte besser zu beherrschen.




## 7 - Sicherheitsanalyse: Aufdeckung von Schwachstellen



### I. Präsentation



In diesem Abschnitt lernen wir, wie man das Netzwerk-Scan-Tool Nmap verwendet, um Schwachstellen auf den Zielen unserer Scans zu erkennen und zu analysieren. Insbesondere werden wir uns die verschiedenen Optionen ansehen, die zur Erfüllung dieser Aufgabe zur Verfügung stehen, und die Grenzen der Fähigkeiten des Tools untersuchen, um seine Ergebnisse besser zu verstehen und zu interpretieren.



In diesem ersten Abschnitt werfen wir einen Blick auf den Schwachstellen-Scanner von Nmap und sehen, wie man die grundlegenden Optionen zur Erkennung von Schwachstellen benutzt. In den folgenden Abschnitten sehen wir uns genauer an, wie diese Funktion funktioniert und wie sie angepasst werden kann.



### II. Nmap zum Aufspüren von Schwachstellen verwenden



Wir wollen nun den Netzwerkscanner Nmap verwenden, um Schwachstellen in den Diensten und Systemen unseres Informationssystems aufzuspüren. Das bedeutet, dass Nmap nicht nur aktive Hosts entdeckt, exponierte Dienste auflistet und Versionen und Technologien erkennt, sondern auch nach Sicherheitslücken sucht.



Um dies zu erreichen, stützt sich Nmap auf NSE-Skripte (_Nmap Scripting Engine_), die als Module betrachtet werden können, die einen granularen Ansatz für Tests ermöglichen.



Mit den richtigen Optionen werden wir Nmap bitten, seine verschiedenen NSE-Skripte auf jeden entdeckten Dienst anzuwenden, so dass wir:





- Fehler in der Konfiguration ;





- Zusätzliche und erweiterte Version und OS Entdeckungen ;





- Bekannte Sicherheitslücken (CVEs) ;





- Schwache Identifikatoren ;





- Charakteristische Elements einer Malware-Infektion ;





- Denial-of-Service-Möglichkeiten ;





- Etc.




Wie Sie sehen, erweitern NSE-Skripte die Fähigkeiten von Nmap in Bezug auf die Netzwerkoperationen, die es durchführen kann, erheblich. Und das, um weitaus mehr fortgeschrittene Aufgaben als je zuvor durchzuführen. Die gute Nachricht ist, dass diese Funktionen wie üblich einfach über eine Option und in einem Standardkontext verwendet werden können. Das werden wir als nächstes sehen.



### III. Beispiel für eine Sicherheitsüberprüfung



NSE-Skripte können verwendet werden, wenn Nmap einen einzelnen Port auf einem Host, alle Dienste auf diesem Host oder alle in mehreren Netzwerken erkannten Dienste scannen soll. Wir können also die Optionen, die wir sehen werden, in allen Kontexten verwenden, die wir bisher untersucht haben.



Um das Scannen auf Sicherheitslücken über einen Nmap-Scan zu aktivieren, müssen wir die Option `-sC` verwenden:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Denken Sie daran, dass Nmap standardmäßig, wenn Sie nichts angeben, nur die 1000 gängigsten Ports scannt. Es wird keine Schwachstellen an den exotischeren Ports entdecken, die Ihre Ziele möglicherweise offenlegen.



Bevor Sie diese Funktionalität in einem produktiven Informationssystem einsetzen, sollten Sie das Tutorial weiter lesen. In den folgenden Abschnitten werden wir uns ansehen, wie man die Auswirkungen und die Arten von Tests, die durchgeführt werden, besser kontrollieren kann.



Durch die Wiederverwendung des zuvor Gelernten können wir beispielsweise umfassender vorgehen und alle TCP-Ports eines Ziels scannen:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Hier ist das Ergebnis eines Nmap-Scans mit NSE-Skripten:



![nmap-image](assets/fr/40.webp)



beispiel für die Ergebnisse eines Schwachstellen-Scans auf einem Host über Nmap._



Hier sehen wir die Anzeige zusätzlicher Informationen, die im Rahmen einer Schwachstellenanalyse von Interesse sind:





- Der FTP-Dienst kann anonym aufgerufen werden und ist nicht durch eine Authentifizierung geschützt. Das NSE-Skript, das für diese Überprüfung zuständig ist, teilt uns dies mit und zeigt sogar einen Teil der Baumstruktur des FTP-Dienstes an. Hier sehen wir, dass wir Zugriff auf das Verzeichnis `C` des Windows-Systems haben!





- Das NSE-Skript, das für die erweiterte Abfrage von Webdiensten zuständig ist, zeigt den Seitentitel an, so dass wir eine bessere Vorstellung davon bekommen, was der Webdienst bereitstellt.





- Wir haben auch eine Mini-Analyse der SMB-Dienstkonfiguration (Skripte `smb2-time`, `smb-security-mode` und `smb2-security-mode`). Die Informationen werden nach dem Ergebnis des Netzwerk-Scans etwas anders dargestellt, damit sie leichter zu lesen sind. Diese Informationen zeigen insbesondere das Fehlen von SMB-Exchange-Signaturen an. Diese Konfigurationsschwäche ermöglicht es, das Ziel für einen SMB-Relay-Angriff zu verwenden, eine bemerkenswerte Sicherheitslücke, die häufig in Tests für Eindringlinge/Cyberangriffe ausgenutzt wird.




Natürlich ist dies nur ein Beispiel. Nmap hat NSE-Skripte für viele Dienste, die auf eine breite Palette von Sicherheitslücken abzielen. Wir werden uns diese Möglichkeiten im nächsten Abschnitt genauer ansehen.



Zum Abschluss dieser Einführung in das Scannen von Sicherheitslücken finden Sie hier einen vollständigen Befehl für die Netzwerkerkennung, das Scannen von TCP-Ports sowie die Erkennung von Versionen und Sicherheitslücken:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



Hier ist ein Befehl, der langsam nach realistischeren Anwendungsfällen für Nmap aussieht!



### IV. Die Grenzen von Nmap beim Scannen von Sicherheitslücken verstehen



Um es klar zu sagen: Nmap ist nicht in der Lage, einen vollständigen Penetrationstest Ihres Informationssystems durchzuführen oder eine Red-Team-Operation zu simulieren. Es hat mehrere Einschränkungen, die Sie kennen müssen, wenn Sie sich nicht in falscher Sicherheit wiegen wollen:





- Begrenzte Abdeckung**: Obwohl die NSE-Skripte von Nmap leistungsstark sind, kann ihre Testabdeckung im Vergleich zu anderen spezialisierten Tools zur Erkennung von Schwachstellen begrenzt sein. Einige Schwachstellen werden von den verfügbaren NSE-Skripten möglicherweise nicht abgedeckt, z. B. Schwachstellen in Active Directory, die Offenlegung sensibler Daten oder fortgeschrittene Fälle von anfälligen Webanwendungen.





- Komplexität der Schwachstelle**: Bestimmte Arten von Schwachstellen können aufgrund ihrer Komplexität mit NSE-Skripten schwer aufzuspüren sein. Zum Beispiel können Sicherheitslücken, die eine komplexe Interaktion mit einem Remote-Dienst erfordern, von Nmap nicht effektiv erkannt werden (wie im Fall von übermäßigen Berechtigungen in einer Dateifreigabe oder einem Fehler in der Berechtigungskontrolle in einer Webanwendung).





- Passive Erkennung**: Nmap konzentriert sich beim Aufspüren von Schwachstellen hauptsächlich auf aktive Scans, was bedeutet, dass es potenzielle Schwachstellen möglicherweise nicht effektiv aufspürt, wenn keine aktive Verbindung zu den Zielhosts hergestellt wird. Schwachstellen, die sich bei einem aktiven Scan nicht zeigen, können daher übersehen werden (wie im Fall einer Code-Injektion in eine Web-Anwendung).





- Abhängigkeit von Updates**: Die [Datenbank](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) von Nmap mit NSE-Skripten wird ständig weiterentwickelt, aber es kann eine Verzögerung zwischen der Entdeckung einer neuen Sicherheitslücke und dem Hinzufügen eines entsprechenden Skripts zu Nmap geben. Daher ist Nmap möglicherweise nicht immer auf dem neuesten Stand, was die neuesten Sicherheitslücken angeht.





- Falsch-Positive und Falsch-Negative**: Wie bei jedem Sicherheitstool können die NSE-Skripte von Nmap falsch-positive Ergebnisse (falsche Warnungen vor Sicherheitslücken) oder falsch-negative Ergebnisse (echte Sicherheitslücken, die nicht entdeckt wurden) liefern. Das sollte man bei der Analyse der Nmap-Ergebnisse bedenken.




Es ist also wichtig zu verstehen, was Nmap tut und was nicht, und ebenso zu wissen, wie man seine Ergebnisse interpretiert. Vor allem haben wir in diesem Tutorial gesehen, dass Standardoptionen dazu führen können, dass wir wichtige Elements übersehen, die bei sorgfältiger Anwendung aufgedeckt werden können.



Ob Sie nun ein Netzwerksystemadministrator, ein Sicherheitsingenieur oder sogar ein CISO sind, mit Nmap erhalten Sie einen Überblick über den Sicherheitsstatus eines Informationssystems. Dies ist ein wichtiger erster Schritt zur Sicherung eines Systems, der regelmäßig vom IT-Team durchgeführt werden kann. Es sollte jedoch nicht das Eingreifen und den Rat von [Cybersicherheits-]Experten (https://www.it-connect.fr/cours-tutoriels/securite-informatique/) ersetzen, die in der Lage sind, Schwachstellen viel umfassender aufzudecken als Nmap.



### V. Schlussfolgerung



In diesem ersten Abschnitt von Modul 3 haben wir das Scannen von Sicherheitslücken mit Nmap vorgestellt. Wir wissen jetzt, wie man diese Aufgabe mit der Hauptoption ausführt, aber wir kennen auch die Grenzen der Übung. Im nächsten Abschnitt werden wir uns diese Funktionalität genauer ansehen und NSE-Skripte verwenden, um die Leistungsfähigkeit von Nmap um das Zehnfache zu erweitern.



## 8 - Verwendung der NSE-Skripte von Nmap



### I. Präsentation



In diesem Abschnitt werfen wir einen detaillierten Blick auf NSE (_Nmap Scripting Engine_) Skripte. Insbesondere werden wir uns ansehen, warum sie eine der großen Stärken dieses Tools sind, wie sie funktionieren und wie man die vielen vorhandenen Skripte durchsucht und verwendet.



Dieser Abschnitt knüpft an das vorherige Tutorial an, in dem wir gelernt haben, wie man die Funktionen von Nmap zum Scannen von Sicherheitslücken auf grundlegende Weise benutzt. Jetzt sehen wir uns genauer an, wie [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) in dieser Hinsicht arbeitet, so dass wir wieder präzisere und kontrollierte Scans durchführen können.



### II. Das Konzept der Nmap-NSE-Skripte



Mit den NSE-Skripten von Nmap können Sie seine Fähigkeiten auf sehr flexible Weise erweitern. Sie sind in LUA geschrieben, einer Skriptsprache, die einfacher zu handhaben und zugänglich ist als das von Nmap verwendete C oder C#. Der Vorteil der Verwendung eines LUA-Skripts mit Nmap gegenüber einem eigenständigen Tool besteht darin, dass wir so die Ausführungsgeschwindigkeit und die Standardfunktionen von Nmap (Host-, Port- und Versionserkennung usw.) nutzen können.



Diese Skripte sind nach Kategorien geordnet, wobei ein einzelnes Skript zu mehr als einer Kategorie gehören kann:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Technisch gesehen werden die Kategorien, zu denen ein Skript gehört, direkt in seinem Code angegeben.



![nmap-image](assets/fr/41.webp)



nSE-Skriptkategorien `ftp-anon`._



Dieses Beispiel zeigt einen Teil des Codes des NSE-Skripts `ftp-anon.nse`, dessen Ausführung wir im vorherigen Abschnitt gesehen haben.



### III. Liste bestehender NSE-Skripte



Standardmäßig befinden sich die NSE-Skripte von Nmap im Verzeichnis `/usr/share/nmap/scripts/`, das keine spezielle Baumstruktur oder Hierarchie hat. Hier ist ein Überblick über den Inhalt dieses Verzeichnisses:



![nmap-image](assets/fr/42.webp)



extrahiert den Inhalt des Verzeichnisses `/usr/share/nmap/scripts/` mit den NSE-Skripten._



Dieses Verzeichnis enthält über 5.000 NSE-Skripte. In den meisten Fällen enthält der erste Teil des Skriptnamens das Protokoll oder die Kategorie, zu der es gehört. So können wir die Liste sortieren, wenn wir zum Beispiel alle Skripte für den FTP-Dienst auflisten möchten:



![nmap-image](assets/fr/43.webp)



liste der NSE-Nmap-Skripte, deren Namen mit `ftp-` beginnen._



Nmap bietet nicht wirklich eine Option zum Durchsuchen und Auflisten seiner NSE-Skripte; Sie können den Befehl `--script-help` gefolgt vom Namen einer Kategorie oder einem Wort verwenden:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



Die Ausgabe besteht jedoch aus dem Namen des jeweiligen Skripts und seiner Beschreibung, was nicht optimal ist, wenn die Suche mehrere Dutzend Skripte ergibt:



![nmap-image](assets/fr/44.webp)



ergebnis der Verwendung des Nmap-Befehls "-script-help"



Meiner Meinung nach ist die effektivste Methode die Verwendung der klassischen Linux-Befehle im Verzeichnis `/usr/share/nmap/scripts/`:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Schauen Sie sich den Code der Module an, die Sie interessieren, um besser zu verstehen, wie ein NSE-Skript funktioniert.



### IV. Verwendung der NSE-Skripte von Nmap



Jetzt werden wir lernen, wie wir Schwachstellen-Scans durchführen können, indem wir die NSE-Skripte, die uns interessieren, sorgfältig auswählen.



#### A. Skripte nach Kategorie auswählen



Zunächst können wir uns dafür entscheiden, alle Skripte auszuführen, die zu einer bestimmten Kategorie gehören. Diese Kategorie(n) müssen wir Nmap mit dem Argument "Skript <Kategorie>" angeben:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Dieser erste Befehl ist das Äquivalent zum Befehl "nmap -sC". Standardmäßig wählt Nmap Skripte in der Kategorie `default` aus, aber das ist nur der Argumentation halber. Der nächste Befehl verwendet zum Beispiel alle Skripte in der Kategorie `Discovery`:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Wie wir gesehen haben, ermöglichen es uns einige Kategorien, schnell zu erkennen, was die entsprechenden NSE-Skripte tun (`Discovery`, `Vuln`, `Exploit`), während andere den Grad des Risikos, der Erkennung oder der Stabilität des durchgeführten Tests definieren. Wenn wir uns in einem sensiblen Kontext befinden und die verschiedenen Aktionen, die von unserer Skriptauswahl durchgeführt werden, nicht genau kennen, können wir die Auswahl kombinieren und nur die Skripte auswählen, die in die Kategorien "Entdeckung" und "sicher" fallen:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Wenn Sie unbedingt und ausdrücklich Skripte aus den Kategorien `dos` und `intrusive` ausschließen wollen, können Sie die folgende Notation verwenden:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Bitte beachten Sie, dass die Angabe der oben genannten Ausschlussbedingungen dazu führt, dass alle anderen Kategorien, die nicht ausdrücklich ausgeschlossen sind, verwendet werden. Um fairer zu sein, könnten wir z. B. angeben:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Hier sind einige Beispiele für den Umgang mit NSE-Skripten nach Kategorien, insbesondere bei der Verwendung von Nmap für die Schwachstellenanalyse in realen Kontexten.



#### B. Skripte als Einheit auswählen



Es ist auch möglich, während einer Analyse einen einzelnen spezifischen Test auszuführen, der einem NSE-Skript entspricht. Dazu muss der Name des Skripts mit dem Parameter "Skript <Name>" angegeben werden. Nehmen wir das Beispiel des Skripts "ftp-anon.nse":



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



Wir haben dann ein sehr präzises Ergebnis:



![nmap-image](assets/fr/45.webp)



ergebnis der Verwendung des NSE-Skripts `ftp-anon` auf einem FTP-Port über Nmap._



Wir sehen das Ergebnis der Ausführung des Skripts `ftp-anon` auf Port 21 und keinem anderen Port, weil wir die Option `-p 21` angegeben haben. Wir hätten auch einen einfachen Port-Scan durchführen können, bei dem das NSE-Skript `ftp-anon` nur auf den gefundenen FTP-Diensten ausgeführt worden wäre:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Nmap hätte diesen anonymen Verbindungstest also auch ausgeführt, wenn es einen FTP-Dienst auf einem anderen Port gefunden hätte.



Eine kurze Beschreibung der Funktionen eines NSE-Skripts finden Sie mit der oben erwähnten Option "-script-help":



![nmap-image](assets/fr/46.webp)



hilfe Ergebnisanzeige für NSE-Skript `sshv1`._



Kurzum, wir können alle bisher verwendeten Optionen, Dienste, Versionen und Technologien für die Netzwerkerkennung wiederverwenden!



#### C. Verwaltung von Skriptargumenten



Im Laufe der Arbeit mit Nmap werden Sie auf bestimmte NSE-Skripte stoßen, die Eingabeargumente benötigen, um korrekt zu funktionieren. Wir sehen uns jetzt an, wie man diesen Skripten über die Optionen von Nmap Argumente übergeben kann.



Nehmen wir als Beispiel das Skript `ssh-brute`, mit dem Sie einen Brute-Force-Angriff auf den SSH-Dienst durchführen können.



Ein klassischer Brute-Force-Angriff besteht darin, mehrere Passwörter (manchmal Millionen) zu testen, um sich bei einem bestimmten Konto zu authentifizieren. Indem er so viele Passwörter ausprobiert, setzt der Angreifer auf die Wahrscheinlichkeit, dass der Benutzer ein schwaches Passwort aus dem für den Angriff verwendeten Passwort-Wörterbuch verwendet hat.



Dieses Skript hat "Standard"-Optionen, die wir an unseren Kontext anpassen können. Im Zusammenhang mit diesem Angriff können wir Nmap zum Beispiel die Liste der Benutzer und das zu verwendende Passwort-Wörterbuch zur Verfügung stellen. Soweit ich weiß, ist es nicht möglich, die für ein Skript benötigten Argumente einfach aufzulisten, also ist der zuverlässigste Weg, die offizielle Nmap-Website zu besuchen. Einen direkten Link zur Dokumentation für ein NSE-Skript erhalten Sie als Antwort auf die Option `--script-help`:



![nmap-image](assets/fr/47.webp)



ergebnis der Anzeige der Hilfe für das NSE-Skript `ssh-brute` mit einem Link zu nmap.org._



Wenn Sie auf den angegebenen Link klicken, gelangen Sie auf diese Seite der Website [https://nmap.org](https://nmap.org/):



![nmap-image](assets/fr/48.webp)



liste der Argumente, die an das NSE-Skript `ssh-brute` von Nmap übergeben werden können



Hier haben wir einen klaren Überblick über die Argumente, die verwendet werden können, die wichtigsten in unserem Zusammenhang sind `passdb` (Datei mit einer Liste von Passwörtern) und `userdb` (Datei mit einer Liste von Benutzern). Die Dokumentation bezieht sich hier auf interne Nmap-Bibliotheken, da diese Brute-Force-Mechanismen und die zugehörigen Optionen für die einheitliche Verwendung in mehreren Skripten (`ssh-brute`, `mysql-brute`, `mssql-brute` usw.) gemeinsam genutzt werden und daher mehr oder weniger die gleichen Argumente haben:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Wie Sie in diesem letzten Befehl sehen können, können wir die notwendigen Argumente für ein Nmap-Skript mit der Option `--scripts-args key=value,key=value` angeben. Hier ist ein mögliches Ergebnis der Nmap-Ausgabe bei der Durchführung eines SSH-Brute-Force-Versuchs mit dem NSE-Skript `ssh-brute`:



![nmap-image](assets/fr/49.webp)



ergebnis der SSH-Bruteforce-Ausführung über Nmap._



Wie Sie sehen, wird den von NSE-Skripten erzeugten Informationen in der interaktiven Ausgabe (Terminalausgabe) das Präfix `NSE: [Skriptname]` vorangestellt, damit sie leichter zu finden sind. In der üblichen Anzeige der Nmap-Ergebnisse gibt es lediglich eine Zusammenfassung, die anzeigt, ob schwache Identifikatoren entdeckt wurden (einschließlich Passwörter, nicht vergessen).



Um noch einen Schritt weiter zu gehen und Sie daran zu erinnern, dass all dies zusätzlich zu den Optionen, die wir bereits betrachtet haben, verwendet werden kann, finden Sie hier einen Befehl, der das Netzwerk "10.10.10.0/24" ermittelt, die 2000 häufigsten TCP-Ports scannt und eine anonyme Zugriffssuche auf FTP-Dienste sowie eine Brute-Force-Kampagne auf SSH-Dienste durchführt:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Dies ist nur ein Beispiel für die vielen verfügbaren Skripte und ihre Optionen. Aber wir haben jetzt eine bessere Vorstellung davon, wie man mit NSE-Skripten zurechtkommt, ob sie Argumente benötigen und wie man diese Argumente an Nmap weitergibt.



### V. Schlussfolgerung



In diesem Abschnitt haben wir gelernt, wie man die NSE-Skripte von Nmap benutzt, um verschiedene Aufgaben durchzuführen. Ich lade Sie ein, sich die Zeit zu nehmen, die verschiedenen Kategorien von Skripts und die Skripts selbst zu entdecken, um zu sehen, wie viele Tests sie automatisieren können.



Seit mehreren Abschnitten haben wir nun mehr oder weniger fortgeschrittene Entdeckungs-, Scan- und Aufzählungsoptionen gesammelt. Inzwischen sollten Sie wissen, dass die Ausgabe und Ergebnisanzeige von Nmap ziemlich umfangreich wird, manchmal sogar zu ausführlich für unser Terminal. Im nächsten Abschnitt werden wir lernen, wie man diese Ausgabe in den Griff bekommt, vor allem durch Speicherung in Dateien in verschiedenen Formaten.






## 9 - Nmap-Ausgabedaten verwalten




### I. Präsentation



In diesem Abschnitt werfen wir einen Blick auf die von Nmap erzeugte Ausgabe und insbesondere auf die verschiedenen Optionen zur Formatierung dieser Ausgabe. Wir werden sehen, dass Nmap mehrere Ausgabeformate für unterschiedliche Bedürfnisse erzeugen kann, und dass auch das eine der großen Stärken dieses Tools ist.



Standardmäßig bietet Nmap eine detaillierte Übersicht über die Ergebnisse der von ihm durchgeführten Scans und Tests. Dazu gehören die gescannten Hosts und Dienste, die als zugänglich erkannt wurden, die Besonderheiten der offenen Ports, ihr Status und ihre Version. Darüber hinaus sind in der Terminalausgabe auch Details zu den NSE-Skripten verfügbar. Allerdings kann diese Ausgabe auch bei klarer Formatierung der Informationen schnell sehr umfangreich werden, so dass es schwierig sein kann, genaue Informationen in den Ergebnissen zu finden.



### II. Nmap-Ausgabeformate beherrschen



#### A. Speichern der Scanergebnisse in einer Textdatei



Um die Dinge zu vereinfachen, macht es [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) sehr einfach, seine Ausgabe in einer Textdatei zu speichern. Das kann nützlich sein für die Archivierung, den Vergleich mit anderen Tests, aber auch für das Durchsuchen dieser Ausgabe mit spezialisierten Textverarbeitungsprogrammen oder Skriptsprachen wie Sublime Text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed usw. Um die Standardausgabe von Nmap in einer Textdatei zu speichern, können wir die Option `-oN <Dateiname>` verwenden (das "N" in "normal"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Das ist keine Überraschung, denn Nmap zeigt seine übliche Standardausgabe in unserem Terminal an, aber auch in der angegebenen Datei.



#### B. generate Nmap-Ausgabe im komprimierten Format



Es gibt auch ein zweites Ausgabeformat im "Text"-Stil, das von einem Menschen leicht interpretiert werden kann: das "greppable"-Format.



Dieses Format wurde erstellt, um eine "komprimierte" Ansicht der Nmap-Ausgabe zu bieten, die so strukturiert ist, dass sie von Tools wie `grep` leichter verarbeitet werden kann. Schauen wir uns ein Beispiel für diese Art von Ausgabe an:



![nmap-image](assets/fr/50.webp)



nmap Netzwerk-Scan und Ausgabe im "greppable" Format._



Hier habe ich eine Netzwerkerkennung sowie einen Port-Scan und eine Analyse der Technologien und Versionen in einem /24-Netzwerk durchgeführt und die Ergebnisse in einer Datei im "greppable"-Format gespeichert. Am Ende habe ich eine Datei mit 2 Zeilen pro aktivem Host erhalten:





- Die erste Zeile sagt mir, dass dieser und jener Host _oben_ ist;





- In einer zweiten Zeile wird angegeben, welche Ports gescannt wurden, ihr Status und die Technologie- und Versionsinformationen, die in einem ganz bestimmten Format abgerufen wurden: <Port>/<Status/<Protokoll>//<Dienst>//<Version>/,`




Diese Formatierung mit einem festen Trennzeichen ermöglicht eine schnelle Verarbeitung durch Textverarbeitungsprogramme wie `grep` oder Skript- und Programmiersprachen. Der folgende Befehl ermöglicht es mir beispielsweise, Informationen über den Host "10.10.10.5" abzurufen, wenn Nmap einen umfangreichen Scan durchgeführt hat, dessen Ausgabe nur schwer zu durchsuchen wäre:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



Umgekehrt kann ich auch leicht alle Hosts auflisten, die Port 21 geöffnet haben, da Ports und IP in derselben Zeile stehen:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



Um generate solche Ausgaben zu machen, müssen wir die Option `-oG <Dateiname>.gnmap` verwenden (das "G" in "grep"). Aus Gewohnheit verwende ich hier die Endung `.gnmap` für eine solche Datei, aber es steht Ihnen frei, die von Ihnen gewünschte Endung zu verwenden:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Dieses Format kann für eine Vielzahl von Zwecken verwendet werden und ist besonders nützlich für eine schnelle Skripterstellung/Sortierung. Dennoch wird es tendenziell zugunsten des Formats aufgegeben, das wir uns als Nächstes ansehen werden.



hinweis: Das greppable-Format `-oG` ist seit Nmap 7.90 offiziell veraltet. Es kann aus Kompatibilitätsgründen noch verwendet werden. Es kann noch für Kompatibilitätszwecke verwendet werden, aber es wird empfohlen, das XML- oder normale Format für die Entwicklung oder das automatische Parsen zu verwenden



#### C. XML-Format für die Nmap-Ausgabe



Das letzte Format, das in diesem Lernprogramm erwähnt werden sollte, ist XML. Im Gegensatz zu den beiden vorangegangenen Formaten ist dieses nicht für das Lesen durch Menschen, sondern durch andere Tools oder Skripte gedacht.



XML (_eXtensible Markup Language_) ist eine Auszeichnungssprache, die zum Speichern und Transportieren von Daten verwendet wird und über benutzerdefinierte Tags eine hierarchische Struktur bietet.



Innerhalb von Nmap wird das XML-Format verwendet, um detaillierte Berichte über die durchgeführten Scans zu erstellen, einschließlich Informationen über Hosts, Ports und entdeckte Schwachstellen sowie zusätzliche Informationen, die nicht in der Standardausgabe von Nmap angezeigt werden.



Um generate eine Ausgabedatei im XML-Format zu geben, müssen wir die Option `-oX` ("O" von "XML") verwenden:



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



Das Ergebnis ist die Standardausgabe von Nmap in Ihrem Terminal sowie eine Datei im XML-Format in Ihrem aktuellen Verzeichnis.



Natürlich ist das XML-Format nicht dafür gedacht, von Menschen gelesen und interpretiert zu werden. Wenn Sie jedoch Skripte erstellen oder dieses Format der Nmap-Ausgabe automatisiert analysieren wollen, müssen Sie trotzdem eine Vorstellung von den verwendeten Tags und der Struktur haben. Hier ist zum Beispiel ein Teil des Inhalts der von Nmap erstellten XML-Datei, die die Scan-Ergebnisse für einen Host zeigt:



![nmap-image](assets/fr/51.webp)



beispiel für einen XML-Datensatz für 1 Host bei einem Nmap-Scan



Hier gibt es eine Menge Informationen, und wir sind besonders an den beiden offenen Ports interessiert:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Wir gehen davon aus, dass dieses Format die automatische Analyse der Ergebnisse erleichtert, da jede Information übersichtlich in einem speziellen, benannten Tag oder Attribut angeordnet ist. Insbesondere finden wir eine Information, auf die wir noch nicht gestoßen sind: den CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Wir haben das CPE in Abschnitt 2 von Modul 2 kurz erwähnt, und diese Information wird bei der Versionserkennung in Spielen ermittelt. Nmap verwendet seine Mechanismen zur Erkennung von Diensten, Technologien und Versionen, um das zugehörige CPE zu finden.



So können wir diese Informationen in den Datenbanken und Anwendungen, die sie verwenden, wiederverwenden. Ich denke dabei insbesondere an die NVD-Datenbank, die auf CVEs verweist. Für jedes CVE enthält sie die von der Sicherheitslücke betroffenen CPEs. Hier ist ein Beispiel für ein CVE zu `a:microsoft:internet_information_services:7.5` aus der NVD-Datenbank:



![nmap-image](assets/fr/52.webp)



vorhandensein eines CPE in den Angaben zu einem CVE in der NVD-Datenbank



Wir haben jetzt ein besseres Verständnis für die Vorteile dieses Formats, das eine sehr klare Informationsstruktur bietet und alle von Nmap erfassten oder verarbeiteten Daten enthält.



Aus Reflex speichere ich meine Nmap-Scans systematisch in allen drei Formaten auf einmal. Möglich wird dies durch die Option `-oA <Name>` ("A" für "All"), die eine Datei `<Name>.nmap`, eine Datei `<Name>.xml` und eine Datei `<Name>.gnmap` erzeugt. Auf diese Weise bin ich sicher, dass mir nichts ausgeht, wenn ich die Ergebnisse noch einmal durchgehen muss.



Mit diesen drei Formaten sollten Sie alles haben, was Sie brauchen, um Nmap-Ergebnisse zu speichern und schließlich automatisiert zu verarbeiten. Wir werden das XML-Format im nächsten Abschnitt wieder verwenden, wenn wir uns mit der Verwendung von Nmap mit anderen Sicherheitstools beschäftigen.



#### III. Erzeugen eines HTML-Berichts aus einem Nmap-Scan



Das XML-Format bietet viele Möglichkeiten, nicht zuletzt die, als Grundlage für die Erstellung eines Berichts im HTML-Format zu dienen, der optisch ansprechender ist.



Um eine Nmap-Datei im XML-Format in eine Webseite umzuwandeln, verwenden wir das Tool `xsltproc`, das wir zunächst installieren müssen:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Sobald dieses Tool installiert ist, geben Sie ihm einfach die zu konvertierende XML-Datei und den Namen des zu erstellenden HTML-Berichts:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Als Ergebnis haben wir unseren gesamten Scan schön strukturiert, mit sogar ein paar Farben und klickbaren Links im Inhaltsverzeichnis!



![nmap-image](assets/fr/53.webp)



auszug aus einem Nmap-Scanbericht im HTML-Format, der von xsltproc._ erstellt wurde



Im Großen und Ganzen enthält die von Nmap gespeicherte XML-Datei einen Verweis auf eine andere Datei im XSL-Format:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



Die Konvertierung in HTML ist daher eine Funktion, die von Nmap bereitgestellt und erleichtert wird, wobei `xsltproc` ein gängiges und anerkanntes Tool zur Durchführung dieser Aufgabe ist (das nicht aus der Nmap-Tool-Suite stammt).



XSLT (_Extensible Stylesheet Language Transformations_) ist eine Teilmenge von XSL, die es ermöglicht, XML-Daten auf einer Webseite darzustellen und parallel zu XSL-Styles in lesbare, formatierte Informationen im HTML-Format zu "transformieren".



quelle: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



Der Informationsgehalt des Reports entspricht dem des XML-Formats von Nmap und ist höher als der der Standard-Terminalausgabe (_interactive output_).



### IV. Verwaltung der Ausführlichkeitsstufe von Nmap



Wir sehen uns jetzt einige Optionen für Debugger Nmap oder für die Verfolgung seines Fortschritts an.



Die erste Option, die wir erwähnen sollten, ist die Option `-v`, die die Ausführlichkeit von Nmap erhöht. Hier ist ein Beispiel:



![nmap-image](assets/fr/54.webp)



die ausführliche Ausgabe von nmap mit der Option `-v`._



Bei einem Scan, der auf viele Hosts und Ports abzielt, wird die Terminalausgabe aufgrund der Menge der angezeigten Informationen schwer auswertbar. Aus diesem Grund sollte diese Option in Kombination mit den zuvor genannten Optionen verwendet werden, die es Ihnen ermöglichen, die Standardausgabe von Nmap in einer Datei zu speichern. Informationen, die sich auf die Verwendung von Verbosity beziehen, werden nicht in diese Ausgabedatei aufgenommen. Wie Sie an dem obigen Beispiel sehen können, erlaubt Ihnen diese Ausführlichkeit, die Aktionen und Entdeckungen von Nmap klar und direkt zu verfolgen. Bei längeren Scans, bei denen die Datenanzeige vielleicht nur langsam vorankommt, verhindert dies, dass man blind für die aktuellen Aktivitäten von Nmap ist und weiß, dass die Dinge voranschreiten und in welchem Tempo. Um die Ausführlichkeit um eine weitere Stufe zu erhöhen, können Sie die Option `-vv` verwenden.



Um die Aktivität von Nmap während seines Scans weiter zu verfolgen, können Sie die Option `--packet-trace` verwenden. Mit der Option `-v` erhalten wir ein Live-Protokoll aller offenen Ports, die von Nmap entdeckt wurden, während wir mit dieser Option eine Protokollzeile für jedes an einen Port gesendete Paket erhalten. Das erzeugt natürlich eine sehr ausführliche Ausgabe, erlaubt aber eine detaillierte Überwachung der Nmap-Aktivitäten, hier ein Beispiel:



![nmap-image](assets/fr/55.webp)



detaillierte Überwachung der Nmap-Aktivitäten über `--packet-trace`._



Auch diese Information wird nicht in der von Nmap erzeugten Ausgabedatei aufgezeichnet, wenn die Optionen `-oN`, `-oG`, `-oX` oder `-oA` verwendet werden.



Schließlich bietet Nmap auch zwei Debug-Optionen: `-d` und `-dd`. Diese Optionen verhalten sich ähnlich wie die Verbosity-Option `-v`, fügen aber zusätzliche technische Informationen hinzu, z.B. eine Zusammenfassung der technischen Parameter am Anfang des Scans:



![nmap-image](assets/fr/56.webp)



timing-Optionen werden in der Debug-Ansicht von Nmap angezeigt



In den nächsten Abschnitten werden wir uns ansehen, was die "Timing"-Optionen sind und warum es sich lohnt, sie zu kennen.



Wenn Sie schließlich nur einen grundlegenden, synthetischen Überblick über den Fortschritt des Nmap-Scans haben wollen, können Sie die Option `--stats-every 5s` verwenden. Die "5s" bedeuten hier 5 Sekunden und können Ihren Bedürfnissen entsprechend geändert werden. Dies ist die Häufigkeit, mit der wir von Nmap eine Rückmeldung über seinen Fortschritt erhalten:



![nmap-image](assets/fr/57.webp)



informationen, die mit der Nmap-Option `--stats-every` angezeigt werden



Insbesondere können wir einen Prozentsatz des Fortschritts sowie einen Hinweis auf die Phase, in der er sich befindet, erhalten: Erkennungsphase des Hosts über [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/), Erkennungsphase der exponierten TCP-Ports, usw. Diese Informationen sind auch in der Terminalausgabe zu finden, wenn Sie während eines Scans die Eingabetaste drücken.



Allerdings ist Nmap nicht sehr gut darin, abzuschätzen, wie lange eine Aufgabe dauern wird, nicht zuletzt, weil es nicht im Voraus weiß, wie viele Hosts und Dienste es scannen muss.



### V. Schlussfolgerung



In diesem Abschnitt haben wir uns eine Reihe von Möglichkeiten angesehen, Nmap-Scanergebnisse in verschiedenen Dateiformaten zu speichern. Das ist sehr nützlich, denn in realistischen Kontexten können Scan-Ergebnisse Hunderte oder sogar Tausende von Zeilen lang sein! Wir haben auch gesehen, wie man den Verbosity-Level von Nmap für Debugging-Zwecke erhöht oder um einen Scan-Fortschrittsbericht zu erhalten.



Das XML-Format wird vor allem im nächsten Abschnitt nützlich sein, in dem wir uns einige Tools ansehen, die mit Nmap-Ergebnissen arbeiten können.




## 10 - Nmap mit anderen Sicherheitstools verwenden



### I. Präsentation



In diesem Abschnitt werfen wir einen Blick auf einige der klassischen Anwendungen von Nmap mit anderen freien und Open-Source-Sicherheitstools. Insbesondere werden wir das, was wir in den vorhergehenden Abschnitten gelernt haben, nutzen, um die Leistung und Effizienz von Nmap weiter zu verbessern.



Die Möglichkeit, Nmap-Scanergebnisse in XML zu speichern, macht die Daten mit einer Vielzahl anderer Tools kompatibel. Da fast alle Programmier- und Skriptsprachen heute über Bibliotheken verfügen, die XML parsen können, ist es viel einfacher, diese Daten zu verarbeiten. Eine Reihe von Tools, insbesondere solche, die auf offensive Sicherheit ausgerichtet sind, verfügen über Funktionen zur Verarbeitung des von Nmap erzeugten XML-Formats. Schauen wir uns das mal genauer an.



Ich werde einige offensive Werkzeuge erwähnen, ohne wirklich detailliert darauf einzugehen, wie sie verwendet werden oder wie sie funktionieren. Ich gehe davon aus, dass der Leser mit ihrer grundlegenden Verwendung vertraut ist und dass sie bereits einsatzbereit sind. Dieser Abschnitt ist vor allem für [Cybersicherheits-]Fachleute (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), Personen in der Ausbildung oder solche, die sich mit dem Thema näher befassen wollen, von Interesse.



### II. Nmap-Ergebnisse in Metasploit importieren



Das erste Tool, das wir uns für die Wiederverwendung von Nmap-Daten bei der offensiven Sicherheits- und Schwachstellenforschung ansehen werden, ist Metasploit.



Metasploit ist ein Exploit- und Angriffs-Framework. Es ist eine kostenlose Lösung und ein anerkanntes Tool, das eine große Anzahl von in Ruby oder Python geschriebenen Modulen enthält. Diese ermöglichen es, Schwachstellen auszunutzen, Angriffe auszuführen, Hintertüren zu generieren, Rückrufe zu verwalten (C&C oder Kommunikations- und Kontrollfunktionen) und alles einheitlich zu nutzen.



Insbesondere kann dieses bekannte und weit verbreitete Betriebssystem mit einer postgreSQL [Datenbank] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) arbeiten, in der Hosts, Ports, Dienste, Authentifizierungsinformationen und mehr gespeichert werden.





- Offizielle Metasploit-Dokumentation: [https://docs.metasploit.com/](https://docs.metasploit.com/)




Hier kommen Nmap und sein Output ins Spiel, denn das XML-Format des Nmap-Outputs kann einfach in die Metasploit-Datenbank importiert werden, um die Datenbank mit Hosts und Services zu füllen, die dann schnell als Ziele für diesen oder jenen Angriff bestimmt werden können.



Sobald ich mich in meiner interaktiven Metasploit-Shell befinde, beginne ich damit, einen Arbeitsbereich zu erstellen, eine Art Raum, der speziell auf meine Tagesumgebung zugeschnitten ist:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Nachdem mein Arbeitsbereich erstellt wurde, müssen wir überprüfen, ob die Kommunikation mit der Datenbank funktioniert:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Schließlich können wir den Metasploit-Befehl `db_import` verwenden, um unseren Nmap-Scan im XML-Format zu importieren:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Hier ist das Ergebnis der Ausführung all dieser Befehle:



![nmap-image](assets/fr/58.webp)



einen Nmap-Scan im XML-Format in die Metasploit-Datenbank importieren



Hier können Sie sehen, dass jeder Host zusammen mit seinen Diensten importiert wird. Diese Daten können dann über den Befehl `services` oder `services -p <port>` für einen bestimmten Dienst angezeigt werden:



![nmap-image](assets/fr/59.webp)



liste der aus der XML-Datei in die Metasploit-Datenbank importierten Dienste



Schließlich können wir diese Daten schnell und einfach in einem Modul wiederverwenden, dank der Option `-R`, die die Liste der Dienste "umwandelt", die wir als Eingabe für die Direktive `RHOSTS` erhalten haben, die verwendet wird, um die Ziele des auszuführenden Angriffs festzulegen. Hier ein Beispiel mit dem Modul `ssh_login`, mit dem Sie einen Brute-Force-Angriff auf [SSH]-Dienste durchführen können (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



verwenden Sie die Option "Services -R", um die als Ziel des Angriffs angegebenen Dienste zu importieren



Dies ist nur ein kleines Beispiel dafür, was mit Nmap-Daten in Metasploit gemacht werden kann, aber es gibt Ihnen eine kleine Vorstellung davon, wie schnell und einfach diese Informationen als Teil eines Penetrationstests, eines Schwachstellenscans oder eines Cyberangriffs wiederverwendet werden können. Es ist auch erwähnenswert, dass Nmap direkt von Metasploit aus ausgeführt werden kann, um die Ergebnisse in die Datenbank zu importieren (Befehl `db_nmap`), ein weiteres interessantes Thema, das wir behandeln werden!



### III. Verwendung von Nmap mit dem Aquatone-Webscanner



Das zweite Tool, das ich in diesem Abschnitt über die Wiederverwendung von Nmap-Ergebnissen für offensive Sicherheits- und Schwachstellenanalysen vorstellen möchte, ist Aquatone.



Aquatone ist ein Web-Scanner zur effizienten Untersuchung von Webanwendungen in einem Netzwerk. Er bietet fortschrittliche Funktionen für die Erkennung von Webdiensten, die Identifizierung von Subdomänen, die Port-Analyse und das Fingerprinting von Webanwendungen. Alles wird klar und übersichtlich in HTML-, JSON- und Textberichten für eine einfache Web-Sicherheitsanalyse dargestellt.



Wie Metasploit kann auch Aquatone das XML-Format von Nmap direkt verarbeiten und als Ziel für Scans verwenden. Insbesondere kann es aus allen Daten, die ein Nmap-Bericht enthalten kann, nur die Hosts und Dienste von Interesse (Webdienste) extrahieren.





- Tool-Link: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




Um die XML-Ausgabe von Nmap mit Aquatone zu verwenden, senden Sie die XML-Datei einfach in eine Pipe, die von Aquatone verarbeitet wird. Hier ist ein Beispiel:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Während Aquatone normalerweise eine Port-Erkennung auf Hosts durchführt, um Webdienste zu finden, verlässt es sich in diesem Zusammenhang ausschließlich auf die Ergebnisse von Nmap, das diesen Vorgang bereits durchgeführt hat, was Zeit spart:



![nmap-image](assets/fr/61.webp)



verwendung von Nmap-Ergebnissen im XML-Format mit `aquatone`._



Zu Ihrer Information finden Sie hier einen Auszug aus dem von Aquatone erstellten Bericht:



![nmap-image](assets/fr/62.webp)



beispiel für einen "Aquatone"-Bericht



Ich persönlich verwende Aquatone häufig, um mir einen schnellen Überblick über die Arten von Websites im Netz zu verschaffen, insbesondere dank der Screenshot-Funktion.



Auch hier spart ein kompletter Nmap-Bericht im XML-Format Zeit und macht es einfach, ihn in einem anderen Tool wiederzuverwenden.



### IV. Schlussfolgerung



Diese beiden Beispiele zeigen deutlich, dass das XML-Format von Nmap es anderen Tools leicht macht, seine Ergebnisse zu verwenden, da es ein strukturiertes, einfach zu verwendendes Datenformat ist. Es gibt viele andere Tools, die diese Ergebnisse verarbeiten können, z.B. automatisierte Reporting-Tools, grafische Darstellungen oder komplexere, proprietäre Schwachstellen-Scanner.



Natürlich können Sie auch Ihre eigenen Skripte und Tools in Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) oder einer anderen Sprache mit einer XML-Parsing-Bibliothek entwickeln, um Nmap-Ergebnisdaten nach Belieben zu manipulieren und wiederzuverwenden.



Dieser Abschnitt bringt uns zum Ende des Tutorial-Moduls über die fortgeschrittene Nutzung von Nmap, insbesondere für das Scannen von Sicherheitslücken durch NSE-Skripte.



Der nächste Abschnitt des Tutorials konzentriert sich unter anderem auf einige zusätzliche, eher technische Best Practices und Tipps zu den spezifischen Scans, die Nmap durchführen kann. Wir werden auch einen Blick auf die Optionen zur Optimierung der Scan-Leistung werfen, die besonders beim Scannen großer Netzwerke nützlich sind.




## 11 - Verbesserung der Netzwerk-Scanleistung



### I. Präsentation



In diesem Kapitel lernen wir, wie man die Geschwindigkeit der mit Nmap durchgeführten Netzwerk-Scans mit Hilfe verschiedener spezifischer Optionen optimieren kann. Insbesondere erfahren wir mehr über das Innenleben von Nmap, von der _timeout_-Verwaltung bis zu den vorgespeicherten Konfigurationen des Tools.



Nachdem wir nun einen guten Blick auf die Funktionen von Nmap geworfen haben, wollen wir uns nun mit dem Biest und seiner Leistung befassen. Wenn Sie das Tool jemals in großen Netzwerken benutzt haben, ist Ihnen wahrscheinlich aufgefallen, dass manche Scans trotz der Leistungsfähigkeit des Tools sehr lange dauern können. Und das aus gutem Grund: Ein einfacher `nmap`-Befehl mit ein paar Optionen kann Millionen von Paketen mit Hunderttausenden von potenziellen Systemen und Diensten durchsuchen.



Darüber hinaus kann es vorkommen, dass manche Netzwerkkonfigurationen absichtlich eine niedrigere Rate (Anzahl der Pakete pro Sekunde) vorschreiben, auf die Gefahr hin, dass Ihre Pakete zurückgewiesen werden oder Ihre IP Address aus Sicherheitsgründen gesperrt wird.



Je nach Kontext kann es sich lohnen, all dies zu optimieren, wie wir in diesem Kapitel sehen werden.



Auf jeden Fall können Sie mit dem Nmap-Debug (Option `-d` aus einem früheren Kapitel) die Standardwerte der Parameter überprüfen, die wir uns ansehen werden, und auch, ob die Optionen, die Sie verwenden werden, korrekt berücksichtigt wurden:



![nmap-image](assets/fr/63.webp)



timing-Optionen über die Nmap-Option "d" anzeigen



### II. Steuerung der Geschwindigkeit von Nmap-Scans



#### A. Verwaltung der Parallelisierung



Standardmäßig nutzt Nmap die Parallelisierung bei seinen Scans, um sie zu optimieren, und alle Parameter, die es verwendet, können über verschiedene Optionen geändert werden. Die Fälle, in denen es tatsächlich notwendig ist, diese Parameter zu ändern, sind jedoch recht selten, so dass wir in diesem Tutorial nicht im Detail darauf eingehen werden:





- `--min-hostgroup/max-hostgroup <size>`: Größe der parallelen Host-Scan-Gruppen.





- `--min-parallelism/max-parallelism <numprobes>`: Parallelisierung von Sonden.





- `--scan-delay/--max-scan-delay <time>`: Stellt die Verzögerung zwischen den Sonden ein.




Sie müssen nur wissen, dass es sie gibt und dass sie genutzt werden können.



#### B. Verwaltung der Anzahl der Pakete pro Sekunde



Standardmäßig passt Nmap die Anzahl der Pakete pro Sekunde, die es sendet, selbst an die Netzwerkantwort an. Aber es ist möglich, diese Einstellung zu erzwingen, indem man den Höchst- und/oder Mindestwert für die Anzahl der Pakete pro Sekunde festlegt. Diese Einstellung wird mit den Optionen `--min-rate <number>` und `--max-rate <number>` vorgenommen, wobei `number` für eine Anzahl von Paketen pro Sekunde steht. Beispiel:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Mit diesen Optionen können Sie die Geschwindigkeit der Scans an Ihre speziellen Bedürfnisse anpassen, entweder um den Prozess zu beschleunigen oder um die verwendete Bandbreite zu begrenzen. Der letztere Fall (Begrenzung der Scan-Geschwindigkeit) ist derjenige, der Sie am ehesten zu diesen Optionen führt, vor allem, wenn Sie bei der Verwendung von Nmap mit Netzwerklatenz zu kämpfen haben (was ziemlich selten ist).



### III. Verwaltung von Verbindungsfehlern und Zeitüberschreitungen



Ein weiterer Parameter, mit dem wir spielen können, um die Geschwindigkeit von Nmap-Scans zu optimieren (oder eine höhere Genauigkeit zu garantieren), betrifft _timeout_ und _retry_.



Bei _timeouts_ ist dies die **Zeitüberschreitung für keine Antwort**, nach der Nmap aufhört, auf eine Antwort zu warten und den Dienst oder Host als unerreichbar betrachtet. Bei _retry_ ist dies die **Anzahl der aufeinanderfolgenden Versuche einer Operation**, die Nmap durchführt, bevor es weitergeht.



Wie bei der Parallelisierung können _timeout_ und _retry_ auf die Host- oder Service-Ermittlungsphasen angewendet werden:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: gibt die Umlaufzeit eines Exchange an. Auch dieser Parameter wird während des Scans berechnet und angepasst. Es ist unwahrscheinlich, dass Sie ihn benutzen müssen, da Nmap diese Zeit je nach Netzwerkreaktion selbst berechnet.





- `--max-retries <Anzahl>`: begrenzt die Anzahl der Wiederholungen eines Pakets beim Port-Scanning. Standardmäßig kann Nmap bis zu 10 Wiederholungen für einen einzelnen Dienst durchführen, insbesondere wenn es Latenzen oder Verluste auf Netzwerkebene feststellt, aber in den meisten Fällen wird nur eine durchgeführt.





- `--host-timeout <time>`: gibt die maximale Zeit an, die Nmap auf einem Host für alle seine Operationen verbringt, einschließlich Port-Scanning, Service-Erkennung und alle anderen Operationen im Zusammenhang mit diesem Host. Wenn dieses Zeitintervall überschritten wird, ohne dass eine Antwort oder ein **Abschluss der Operationen** erfolgt, gibt Nmap diesen Host auf, ohne irgendwelche Ergebnisse zu ihm anzuzeigen, und geht zum nächsten in seiner Liste über. Auf diese Weise können Sie die maximale Zeit, die Nmap auf einem bestimmten Host verbringt, kontrollieren, um zu vermeiden, dass es auf widerspenstigen Hosts stecken bleibt, und um die Gesamtscanzeit zu optimieren.




Bei meiner täglichen Arbeit verwende ich die Optionen `--max-retries` und `--host-timeout`, um meine Scans zu optimieren:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Diese Parameter bieten zusätzliche Flexibilität bei der Anpassung des Scanverhaltens an bestimmte Anforderungen und Netzwerkbedingungen. Sie müssen sich jedoch über die Auswirkungen auf die Belastung der gescannten Hosts und den möglichen Verlust an Genauigkeit im Klaren sein.



### IV. Verwendung der vorbereiteten Konfigurationen



Die verschiedenen Optionen, die wir in diesem Kapitel gesehen haben, können einzeln oder als Teil der vorgefertigten Konfigurationen, die Nmap anbietet, verwendet werden. Die Option, mit der diese _Vorlagen_ (Konfigurationsvorlagen) verwendet werden können, ist `-T <Nummer>` oder `-T <Name>`. Es gibt 5 verwendbare Ebenen von _Templates_:



```
-T<0-5>: Set timing template (higher is faster)
```



Standardmäßig verwendet Nmap _template_ 3 (_normal_), was im Allgemeinen ausreichend ist.



Ich für meinen Teil arbeite im Allgemeinen in Kontexten, in denen ich ziemlich schnell sein muss (und dabei so vollständig wie möglich bleiben muss), und ich verwende häufig die Option "T4".



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Die Debug-Informationen für diesen Scan zeigen Folgendes:



![nmap-image](assets/fr/64.webp)



verwendung der "T4"-Einstellung während eines Nmap-Scans



### V. Schlussfolgerung



In diesem Kapitel haben wir uns verschiedene Techniken und Optionen angesehen, mit denen Sie die Leistung, Aggressivität und Performance von Nmap steuern können. Diese Optionen sind besonders nützlich, wenn Sie große Netzwerke scannen, und seltener für Stealth-Zwecke.



Im nächsten Kapitel sehen wir uns einige Best Practices für die Verwendung von Nmap und die Gewährleistung seiner Sicherheit an.




## 12 - Datensicherheit und Vertraulichkeit bei der Verwendung von Nmap



### I. Präsentation



In diesem Kapitel sehen wir uns einige bewährte Verfahren an, die im Hinblick auf die Sicherheit und vor allem die Vertraulichkeit der von Nmap erzeugten, verarbeiteten und gespeicherten Daten anzuwenden sind.



Die Verwendung von Nmap innerhalb eines Informationssystems kann schnell als offensive Aktion eingestuft werden. Daher müssen eine Reihe von Vorkehrungen getroffen werden, um innerhalb eines rechtlichen Rahmens zu handeln und gleichzeitig die Sicherheit der beabsichtigten Ziele, der gesammelten Daten und des für den Scan verwendeten Systems zu gewährleisten.



### II. Einholung der entsprechenden Genehmigungen



Vergewissern Sie sich vor dem Scannen eines Netzes oder Systems, dass Sie die entsprechenden Berechtigungen erhalten haben. Das Scannen von Systemen auf Schwachstellen (NSE-Skripte) ohne Genehmigung kann illegal sein und rechtliche Konsequenzen nach sich ziehen, insbesondere wenn die Sicherheit von Informationssystemen nicht zu Ihrem offiziellen Aufgabenbereich gehört.





- Zur Erinnerung: [Strafgesetzbuch: Kapitel III: Angriffe auf automatisierte Datenverarbeitungssysteme](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Schutz sensibler Daten



Die von Nmap erzeugten Ergebnisse können als sensibel angesehen werden, insbesondere wenn sie Informationen über Schwachstellen im Informationssystem enthalten, die von einem Angreifer ausgenutzt werden könnten. Aber auch, wenn sie Systeme betreffen, die nicht für jedermann zugänglich sind (z. B. sensible, industrielle, medizinische oder [Backup-]Informationssysteme (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



Wir haben auch gesehen, dass die NSE-Scanergebnisse von [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) je nach den verwendeten NSE-Skripten auch Identifikatoren enthalten können.



Eine böswillige Person, der es gelingt, sich Zugang zu diesen Scan-Ergebnissen zu verschaffen, verfügt somit über eine Karte des Informationssystems und eine Fülle von technischen Informationen, ohne diese Aktionen selbst durchgeführt zu haben, und läuft Gefahr, entdeckt zu werden.



Es ist daher wichtig, bei der Verwendung von Nmap darauf zu achten, dass keine sensiblen Informationen unangemessen gesammelt oder gespeichert werden, einschließlich, aber nicht beschränkt auf, die folgenden:





- Verschlüsselung der Ausgabedaten: Wenn Sie die Ergebnisse Ihrer Nmap-Scans speichern oder übertragen müssen, sollten Sie sie verschlüsseln, um die Vertraulichkeit der Daten zu schützen. Dadurch wird verhindert, dass Unbefugte sensible Informationen abfangen. Idealerweise sollten die Daten verschlüsselt werden, sobald sie das System verlassen, auf dem der Scan durchgeführt wurde (ein mit einem starken Passwort verschlüsseltes ZIP-Archiv ist ein sehr guter Anfang).





- Richten Sie Zugangskontrollen ein: Stellen Sie sicher, dass nur autorisierte Personen Zugang zu den Ergebnissen Ihrer Nmap-Scans haben, wo sie gespeichert werden. Richten Sie geeignete Zugriffskontrollen ein, um sensible Informationen vor unberechtigtem Zugriff zu schützen.





- Wachsamkeit beim Umgang mit Daten: Achten Sie beim Übertragen, Kopieren oder Verarbeiten von Scandaten darauf, dass Sie die Datensicherheit streng kontrollieren. Das bedeutet: Lassen Sie sie nicht im Download-Verzeichnis eines mit dem Internet verbundenen Arbeitsplatzes herumliegen, lassen Sie sie nicht durch Ihre interne HTTP-Datei-Exchange-Anwendung laufen, lassen Sie Ihren Notepad nicht offen, ohne den Arbeitsplatz während der Mittagspause zu sperren, usw.




### IV. Umgang mit aggressiven Scans



Wie wir in diesem Lernprogramm gesehen haben, kann Nmap auf Netzwerkebene sehr ausführlich sein. Es kann auch Pakete senden, die nicht richtig formatiert sind und die die Protokollstruktur in den von ihm erzeugten Netzwerkrahmen und -paketen nicht strikt einhalten. All diese Aktionen können sich auf bestimmte Systeme und Dienste auswirken, manchmal bis zu dem Punkt, dass sie Fehlfunktionen oder eine Sättigung der System- und Netzwerkressourcen verursachen.



Um Zwischenfälle zu vermeiden, müssen Sie das Verhalten von Nmap beherrschen und wissen, wie Sie es mit Hilfe der verschiedenen Optionen, die in diesem Tutorial besprochen werden, an den Kontext anpassen können, in dem es benutzt wird. Wir werden Nmap in einem Informationssystem mit industrieller [Hardware] (https://www.it-connect.fr/actualites/actu-materiel/) nicht unbedingt auf dieselbe Weise einsetzen wie in einem Benutzernetz, das aus Windows-Systemen besteht, die durch eine lokale Firewall geschützt sind, oder in einem Netzwerkkern.



Hoffentlich haben Sie in den verschiedenen Lektionen dieses Tutorials gelernt, wie man das Verhalten von Nmap beherrscht und analysiert, aber am besten lernt man, indem man etwas tut. Stellen Sie also sicher, dass Sie mit den Nmap-Optionen vertraut sind, die Sie benutzen werden.



### V. Schutz des Scansystems



Im ersten Kapitel haben wir gesehen, dass Nmap in den meisten Fällen als `root` oder lokaler Administrator ausgeführt werden muss. Das liegt daran, dass es Netzwerkoperationen durchführt, manchmal auf einer ziemlich niedrigen Ebene, durch Netzwerkbibliotheken, die hohe und riskante Berechtigungen im Hinblick auf die Systemstabilität oder die Vertraulichkeit anderer Anwendungen erfordern.



Daher kann Nmap als eine sensible Komponente des Systems betrachtet werden, auf dem es installiert ist. Achten Sie darauf, dass Sie die neueste Version von Nmap verwenden, da ältere Versionen bekannte Sicherheitslücken enthalten können. Indem Sie eine aktuelle Version verwenden, können Sie die mit der Verwendung des Tools verbundenen Risiken minimieren.



Wenn Sie sich dafür entschieden haben, Nmap nicht über eine Sitzung als `root` zu benutzen, sondern indem Sie einem privilegierten Benutzer bestimmte Privilegien gewähren, so dass er alles hat, was er braucht, um Nmap zu benutzen (`sudo` oder _capabilities_), dann seien Sie sich bewusst, dass Nmap als Teil einer kompletten Erhöhung der Privilegien benutzt werden kann:



![nmap-image](assets/fr/65.webp)



erhöhung der Nmap-Privilegien über `sudo`._



Hier verwende ich den Nmap-Befehl über `sudo`, aber das erlaubt es mir, eine interaktive Shell als `root` auf dem System zu erhalten, was nicht das ursprüngliche Ziel war.



Es ist auch nicht ratsam, Nmap auf Systemen zu installieren, die nicht für die Durchführung von Netzwerk-Scans ausgelegt sind. Ich denke da vor allem an Server oder Workstations. Einerseits würde dies einen potenziellen Vektor für die Erhöhung von Privilegien hinzufügen, aber vor allem würde es dem Angreifer mühelos Zugang zu einem offensiven Tool verschaffen.



Schließlich muss die Sicherheit des für das Scannen verwendeten Systems umfassend gewährleistet sein, damit es nicht selbst zu einem Vektor für Eindringlinge oder Informationsverluste wird. Als Systemadministrator ist es besser, ein dediziertes System zu verwenden, das idealerweise eine begrenzte Lebensdauer hat, als Ihren eigenen Arbeitsplatz.



### VI. Schlussfolgerung



Stellen Sie also sicher, dass Sie Nmap richtig beherrschen, bevor Sie es unter realen oder produktiven Bedingungen einsetzen, und seien Sie bei der Verarbeitung und Verwaltung seiner Ergebnisse wachsam. Es wäre schade, wenn Sie Schaden anrichten, Daten preisgeben oder eine Kompromittierung erleichtern, wenn der ursprüngliche Ansatz darauf abzielt, die Sicherheit Ihres Unternehmens zu verbessern.



## 13 - Port-Scans über TCP: SYN, Connect und FIN



### I. Präsentation



In diesem und im nächsten Kapitel werden wir uns die verschiedenen Arten von TCP-Scans, die in Nmap verfügbar sind, genauer ansehen, angefangen mit den am häufigsten verwendeten: SYN-, Connect- und FIN-Scans.



Wie Sie vielleicht schon bemerkt haben, bietet Nmap mehrere Optionen für TCP-Scans:



![nmap-image](assets/fr/66.webp)



die in Nmap._ verfügbaren Scan-Techniken



Im Folgenden sollen einige dieser Methoden erläutert werden, damit Sie ihre Unterschiede, Vorteile und Grenzen besser verstehen. Sie werden sehen, dass es je nach dem Kontext oder dem, was Sie wissen wollen, besser ist, sich für die eine oder andere Option zu entscheiden.



### II. TCP SYN-Scan oder "Halboffener Scan



Die erste Art von TCP-Scan, die wir uns ansehen werden, ist der "TCP SYN Scan", auch bekannt als "Half Open Scan". Wenn Sie sich an die Netzwerk-Scans erinnern, die wir nach unseren ersten Port-Scans durchgeführt haben, ist dies die Art von Scan, die standardmäßig von [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) verwendet wird, wenn sie mit Root-Rechten ausgeführt wird.



Die Übersetzung wird Ihnen helfen zu verstehen, wie dieser Scan funktioniert. Bei einem TCP-SYN-Scan wird ein TCP-SYN-Paket an jeden Zielport gesendet. Dies ist das erste Paket, das ein Client (derjenige, der eine Verbindung herstellen möchte) als Teil des berühmten _Three way handshake_ TCP sendet. Wenn der Port auf dem Zielserver offen ist und ein Dienst dahinter läuft, sendet der Server normalerweise ein TCP SYN/ACK-Paket zurück, um das SYN des Clients zu bestätigen und die TCP-Verbindung zu initialisieren. Diese Antwort erfolgt in Form eines TCP-Pakets, bei dem die SYN- und ACK-Flags auf 1 gesetzt sind, so dass wir bestätigen können, dass der Port offen ist und zu einem Dienst führt.



Ist der Port hingegen geschlossen, sendet uns der Server ein `TCP`-Paket mit den Flags RST und ACK auf 1, um die Verbindungsanfrage zu beenden, so dass wir wissen, dass hinter diesem Port kein Dienst aktiv zu sein scheint:



![nmap-image](assets/fr/67.webp)



tCP SYN Scan Verhaltensdiagramm für offene und geschlossene Ports



Um einen konkreteren Einblick in den "TCP SYN Scan" zu bekommen, habe ich einen Scan des Ports TCP/80 auf einem Host durchgeführt, der einen aktiven Webserver auf diesem Port hatte. Ein Netzwerk-Scan mit Wireshark zeigt den folgenden Fluss (Scan-Quelle: 10.10.14.84):



![nmap-image](assets/fr/68.webp)



netzwerkaufzeichnung während eines TCP SYN-Scans für einen offenen Port



In der ersten Zeile sehen wir, dass die Scan-Quelle ein TCP-Paket an den Host "10.10.10.203" am Port TCP/80 sendet. In diesem TCP-Paket ist das SYN-Flag auf 1 gesetzt, um anzuzeigen, dass es sich um eine TCP-Verbindungsinitialisierungsanfrage handelt.



In der zweiten Zeile sehen wir, dass das Ziel mit einem `TCP SYN/ACK` antwortet, was bedeutet, dass es akzeptiert, eine Verbindung zu initialisieren und somit Streams auf Port TCP/80 zu empfangen. Daraus lässt sich ableiten, dass der Port TCP/80 offen ist und dass auf dem gescannten Server ein Webserver vorhanden ist.



Unser Host sendet dann ein RST-Paket zurück, um die Verbindung zu schließen, so dass der gescannte Host keine offene TCP-Verbindung aufrechterhalten muss, um auf eine Antwort zu warten. Im Falle eines Scans auf vielen Ports könnte das Nicht-Schließen von TCP-Verbindungen zu einer Dienstverweigerung (Denial of Service) führen, da die Anzahl der auf eine Antwort wartenden Verbindungen, die der Server aufrechterhalten kann, gesättigt ist (siehe [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



In Wireshark können Sie den Status der TCP-Flags für jeden Test, den wir durchführen, sehen. Dies zeigt, ob das Paket ein SYN-, SYN/ACK-, ACK-Paket usw. ist:



![nmap-image](assets/fr/69.webp)



die TCP-Flags eines Pakets in Wireshark anzeigen (hier TCP SYN)



Umgekehrt habe ich den gleichen Test zwischen den beiden Rechnern durchgeführt, aber dieses Mal einen TCP/81-Port gescannt, auf dem kein Dienst aktiv ist (Scan-Quelle: "10.10.14.84"):



![nmap-image](assets/fr/70.webp)



netzwerkerfassung während eines TCP SYN-Scans für einen geschlossenen Port



Der gescannte Host antwortet mit einem `TCP RST/ACK` auf mein `TCP SYN`, wenn der Port nicht offen ist.



Wie bereits erwähnt, ist der TCP-SYN-Scan der Standardmodus, wenn Nmap von einem privilegierten Terminal aus ausgeführt wird, und kann mit der Option `-sS` (`scan SYN`) erzwungen werden:



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




Der "TCP SYN Scan" ist aus Geschwindigkeitsgründen der am häufigsten verwendete Scan. Andererseits kann das Versäumnis eines Clients, den _Three Way Handshake_ abzuschließen (d.h. kein ACK nach dem SYN/ACK des Servers zu senden), verdächtig erscheinen, wenn es zu oft auf einem Server oder von der gleichen Quelle im Netz beobachtet wird. Das normale Verhalten eines Clients nach dem Empfang eines TCP SYN/ACK-Pakets als Antwort auf einen TCP SYN besteht darin, eine "Bestätigung" (ACK) zu senden und dann den Exchange zu starten.



Nichtsdestotrotz bietet er einen etwas schnelleren Scan, da er sich nicht die Mühe macht, für jede positive Antwort ein ACK zu senden. Der Vorteil des SYN-Scans liegt in der Geschwindigkeit, da nur ein Paket pro zu überprüfendem Anschluss gesendet wird, allerdings auf Kosten einer höheren Entdeckungswahrscheinlichkeit.



Darüber hinaus kann der TCP SYN-Scan erkennen, ob ein Port von einer Firewall gefiltert (geschützt) wird. Eine Firewall vor dem Zielhost kann nämlich daran erkannt werden, wie sie sich verhält, wenn sie ein TCP SYN-Paket an einem Port empfängt, den sie eigentlich schützen sollte. Sie antwortet einfach nicht. Wie wir jedoch gesehen haben, gibt es in beiden Fällen (offener oder geschlossener Port) eine Antwort des Hosts. Dieses dritte Verhalten zeigt das Vorhandensein einer Firewall zwischen dem gescannten Host und dem Rechner, der den Scan ausführt. Hier ist das Ergebnis, das Nmap zurückgeben kann, wenn ein gescannter Port von einer Firewall gefiltert wird:



![nmap-image](assets/fr/71.webp)



nmap-Anzeige beim Scannen eines gefilterten Ports



Wenn wir zum Zeitpunkt des Scans eine Netzwerkerfassung durchführen, können wir feststellen, dass keine Antwort erfolgt:



![nmap-image](assets/fr/72.webp)



netzwerkaufzeichnung während eines TCP SYN-Scans für einen von einer Firewall gefilterten Port



Der Unterschied zwischen einem geschlossenen und einem gefilterten Port ist folgender: Ein gefilterter Port ist ein Port, der durch eine Firewall geschützt ist, während ein geschlossener Port ein Port ist, auf dem kein Dienst läuft und der daher unsere TCP-Pakete nicht verarbeiten kann. Einige Arten von TCP-Scans, wie z. B. der TCP-SYN-Scan, sind in der Lage zu erkennen, ob ein Port gefiltert ist, während andere Arten von Scans dies nicht können.



### III. TCP Connect-Scan oder Full Open-Scan



Die zweite Art von TCP-Scan ist der "TCP-Connect-Scan", auch bekannt als "Full Open Scan". Er funktioniert auf die gleiche Weise wie der TCP SYN-Scan, aber dieses Mal wird nach einer positiven Antwort des Servers (einem SYN/ACK) ein `TCP ACK` zurückgegeben. Deshalb heißt er "Full Open", da die Verbindung vollständig geöffnet und auf jedem Port, der während des Scans geöffnet wird, initiiert wird, wodurch der TCP _Three Way Handshake_ respektiert wird:



![nmap-image](assets/fr/73.webp)



tCP Connect Scan Verhaltensdiagramm für offene und geschlossene Ports



Hier ist zu sehen, was während eines "TCP Connect"-Scans, der auf einen offenen Port abzielt, durch das Netzwerk übertragen wird:



![nmap-image](assets/fr/74.webp)



netzwerk-Sniffing während eines TCP Connect-Scans nach einem offenen Port



Wir können sehen, dass das erste gesendete TCP-Paket ein `TCP SYN` ist, das vom Client gesendet wird, und der Server antwortet dann mit einem `TCP SYN/ACK`, was anzeigt, dass der Port offen ist und einen aktiven Dienst hostet. Um einen legitimen Client zu simulieren, sendet Nmap dann ein `TCP ACK` zurück an den Server. Umgekehrt wird beim Scannen eines geschlossenen Ports:



![nmap-image](assets/fr/75.webp)



netzwerkerfassung während eines TCP Connect-Scans für einen geschlossenen Port



Beachten Sie, dass die Antwort des Servers auf unser `SYN`-Paket wieder ein `TCP RST/ACK`-Paket ist, woraus wir schließen können, dass der Port geschlossen ist und keine Dienste darauf laufen.



Bei der Verwendung von Nmap wird die Option `-sT` (`scan Connect`) verwendet, um einen TCP Connect Scan durchzuführen. Bitte beachten Sie, dass dies der Standard-TCP-Scan-Modus ist, wenn Nmap von einer unprivilegierten Sitzung aus benutzt wird:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



Der `TCP Connect Scan` simuliert eine legitimere Verbindungsanfrage, mit einem Verhalten, das dem eines Lambda-Clients am ähnlichsten ist, so dass es schwieriger ist, einen Scan auf einer reduzierten Anzahl von Ports zu erkennen. Er ist jedoch langsamer, da er jede TCP-Verbindung auf den offenen Ports des gescannten Rechners vollständig initialisiert.



Ein Nmap-Scan von 10.000 Ports kann immer noch leicht entdeckt werden, wenn Dienste zur Erkennung und zum Schutz von Eindringlingen in das Netzwerk (IDS, IPS, EDR) installiert sind. Wenn ein Angreifer sich unauffällig verhalten will, konzentriert er sich auf eine kleine Anzahl strategisch ausgewählter Ports wie 445 (SMB) oder 80 (HTTP), die auf Servern oft offen sind und häufig Schwachstellen aufweisen.



Da TCP Connect Scan in beiden Fällen eine Antwort erwartet, kann er auch das Vorhandensein einer Firewall erkennen, die möglicherweise Ports auf dem Zielhost filtert.



### IV. TCP FIN-Scan oder "Stealth Scan



Der `TCP FIN Scan`, auch bekannt als _Stealth Scan_, nutzt das Verhalten eines Clients, der eine TCP-Verbindung beendet, um einen offenen Port zu erkennen.



Bei TCP bedeutet Sitzungsende das Senden eines TCP-Pakets mit dem FIN-Flag auf 1. Bei einem normalen Exchange stellt der Server die Kommunikation mit dem Client ein (keine Antwort). Wenn der Server keine aktive TCP-Verbindung mit dem Client hat, sendet er ein "RST/ACK". Wir können also zwischen offenen und geschlossenen Ports unterscheiden, indem wir `TCP FIN`-Pakete an eine Reihe von Ports senden:



![nmap-image](assets/fr/76.webp)



tCP FIN-Scan-Verhaltensdiagramm für offene und geschlossene Ports



Ich habe das Netzwerk erneut während eines _Stealth-Scans_ aufgezeichnet, und das ist das, was Sie sehen, wenn der gescannte Port offen ist:



![nmap-image](assets/fr/77.webp)



netzwerkerfassung während eines TCP FIN-Scans nach einem offenen Port



Wir können sehen, dass der Client ein oder zwei Pakete sendet, um eine TCP-Verbindung zu beenden, und dass der Server nicht darauf reagiert. Er akzeptiert einfach das Ende der Verbindung und hört auf zu kommunizieren.



So sieht es jetzt aus, wenn wir einen geschlossenen Port scannen:



![nmap-image](assets/fr/78.webp)



netzwerkerfassung während eines TCP FIN-Scans für einen geschlossenen Port



Wir sehen, dass der Server ein `TCP RST/ACK'-Paket zurücksendet, es gibt also einen Unterschied im Verhalten zwischen einem offenen und einem geschlossenen Port, und wir können die offenen Ports auf einem Server auflisten, indem wir ein TCP FIN-Paket senden. Mit Nmap wird die Option `-sF` (`scan FIN`) verwendet, um einen TCP FIN Scan durchzuführen:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN Scan funktioniert nicht auf Windows-Hosts, da das Betriebssystem dazu neigt, TCP FIN-Pakete zu ignorieren, wenn sie an nicht offene Ports gesendet werden. Wenn Sie also einen TCP FIN Scan auf einem Windows-Host ausführen, erhalten Sie den Eindruck, dass alle Ports geschlossen sind.



Deshalb ist es wichtig, sich mit den verschiedenen Scanmethoden vertraut zu machen und die Unterschiede zwischen ihnen zu kennen.



Da der TCP FIN in beiden Fällen nicht auf eine Antwort wartet, kann er das Vorhandensein einer Firewall zwischen dem Zielhost und der Scan-Quelle nicht erkennen.



Hier ist ein Beispiel für das Ergebnis des TCP-FIN-Scans von Nmap:



![nmap-image](assets/fr/79.webp)



ergebnisse eines TCP FIN-Scans durch Nmap._



Wenn der Host auf einem bestimmten Port nicht antwortet, kann das bedeuten, dass der Port gefiltert wird, aber auch, dass er offen und aktiv ist.



Dieser Scan wird als "Stealth" bezeichnet, da er nicht viel generate-Verkehr erzeugt und im Allgemeinen keine Protokollierung in den Zielsystemen verursacht. Er kann verwendet werden, um diskret Ports in einem Netzwerk zu entdecken, ohne einen Alarm auszulösen. Wie bereits erwähnt, kann seine Wirksamkeit jedoch je nach Zielsystem variieren, ebenso wie seine Diskretion je nach Konfiguration der Sicherheitsausrüstung.



### V. Schlussfolgerung



So viel zum ersten von zwei Kapiteln über die verschiedenen TCP-Scan-Typen, die Nmap anbietet! Im nächsten Kapitel sehen wir uns die TCP-Scantypen XMAS, Null und ACK an, die auf unterschiedliche Weise funktionieren, um offene Ports auf einem Host zu erkennen.





## 14 - Port-Scans über TCP: XMAS, Null und ACK



### I. Präsentation



In diesem Abschnitt werden wir uns weiter mit den verschiedenen TCP-Scan-Methoden beschäftigen, die Nmap anbietet. Hier sehen wir uns die Methoden `XMAS`, `Null` und `ACK` an, die TCP-spezifische Eigenschaften nutzen, um Informationen über die Ports und Dienste zu erhalten, die auf einem bestimmten Ziel offen sind.



### II. TCP XMAS-Scan



Der XMAS Scan TCP ist insofern etwas ungewöhnlich, als er das normale Benutzer- oder Maschinenverhalten in einem Netzwerk überhaupt nicht simuliert. Tatsächlich sendet XMAS Scan TCP-Pakete mit den Flags `URG` (Urgent), `PSH` (Push) und `FIN` (Finish) auf 1 gesetzt, um bestimmte Firewalls oder Filtermechanismen zu umgehen.



Der Name XMAS kommt von der Tatsache, dass es ungewöhnlich ist, diese Flaggen eingeschaltet zu sehen. Wenn alle drei Flags gleichzeitig in einem TCP-Paket gesetzt sind, sieht es aus wie ein beleuchteter Weihnachtsbaum:



![nmap-image](assets/fr/80.webp)



tCP-Flags, die beim XMAS-Scan verwendet werden



Ohne hier im Detail auf die Rolle dieser Flags einzugehen, ist es wichtig zu wissen, dass ein aktiver Dienst hinter dem Zielport keine Pakete zurückschickt, wenn er ein Paket mit diesen drei Flags sendet. Wenn der Port hingegen geschlossen ist, erhalten wir ein TCP RST/ACK-Paket. Jetzt können wir bei der Auflistung der Ports eines Rechners zwischen dem Verhalten eines offenen und eines geschlossenen Ports unterscheiden:



![nmap-image](assets/fr/81.webp)



tCP XMAS Scan Verhaltensdiagramm für offene und geschlossene Ports



Nach der gleichen Logik zeigt ein Netzwerkscan auf Port TCP/80 eines Hosts mit aktivem Webserver folgendes Verhalten, wenn er einen offenen Port entdeckt (Scan-Quelle "10.10.14.84"):



![nmap-image](assets/fr/82.webp)



netzwerkaufzeichnung während eines TCP XMAS-Scans nach einem offenen Port



Wir können sehen, dass die Scan-Quelle zwei TCP XMAS-Pakete (mit den Flags `FIN`, `PSH` und `URG` auf 1 gesetzt) an den Host `10.10.10.203` sendet und dass es keine Antwort vom Ziel gibt, was anzeigt, dass der Port offen ist. Wird dagegen ein `TCP XMAS Scan` an einem geschlossenen Port durchgeführt, wird das folgende Ergebnis beobachtet:



![nmap-image](assets/fr/83.webp)



netzwerkaufzeichnung während eines TCP XMAS-Scans für einen geschlossenen Port



Die Antwort auf unser TCP-Paket ist dann ein `TCP RST/ACK`, das anzeigt, dass der Port geschlossen ist. Um diese Technik mit Nmap zu verwenden, können Sie mit der Option `-sX` (`scan XMAS`) einen TCP XMAS Scan durchführen:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



Es ist wichtig zu beachten, dass der TCP XMAS-Scan im Gegensatz zu anderen Scan-Typen wie TCP SYN oder Connect nicht in der Lage ist, Firewalls zu erkennen, die sich möglicherweise zwischen dem Ziel und dem Scan-Rechner befinden. Eine aktive Firewall zwischen den beiden Hosts stellt sicher, dass keine TCP-Rückmeldung erfolgt, wenn der Zielport gefiltert (d. h. durch die Firewall geschützt) ist. Im Falle einer ausbleibenden Antwort ist es daher unmöglich zu wissen, ob der Port durch die Firewall geschützt oder offen und aktiv ist. Sie sollten sich auch darüber im Klaren sein, dass, wie beim TCP FIN-Scan, bestimmte Anwendungen oder Betriebssysteme wie Windows die Ergebnisse dieser Art von Scan verfälschen können.



hinweis: Die Unterstützung für XMAS/FIN/NULL-Scans auf neueren Windows-Versionen ist nach wie vor begrenzt, und die Ergebnisse können bei dieser Art von Zielen inkonsistent sein. (Update 2025)_



### III. TCP-Nullsuche



Im Gegensatz zum TCP XMAS-Scan sendet der TCP Null-Scan TCP-Scan-Pakete, bei denen alle Flags auf 0 gesetzt sind. Auch dies ist ein Verhalten, das in einem normalen Exchange zwischen Rechnern nie vorkommt, da das Senden eines TCP-Pakets ohne Flag im RFC, der das TCP-Protokoll beschreibt, nicht spezifiziert ist. Aus diesem Grund kann es leichter entdeckt werden.



Wie der TCP XMAS-Scan kann auch dieser Scan bestimmte Firewalls oder Filtermodule stören, so dass Pakete durchgelassen werden:



![nmap-image](assets/fr/84.webp)



tCP Null Scan Verhaltensdiagramm für offene und geschlossene Ports



Hier sehen Sie, was im Netzwerk während eines TCP-Null-Scans an einem offenen Port zu sehen ist:



![nmap-image](assets/fr/85.webp)



netzwerkaufzeichnung während eines TCP-Null-Scans für einen offenen Port



Der Scan-Rechner sendet ein flaggenloses Paket (`[<None>]` in Wireshark), ohne dass eine Antwort vom Server kommt. Umgekehrt, wenn der Zielport geschlossen ist:



![nmap-image](assets/fr/86.webp)



netzwerkerfassung während eines TCP Null-Scans für einen geschlossenen Port



Um einen TCP-Null-Scan mit Nmap durchzuführen, verwenden Sie einfach die Option `-sN` (`scan Null`):



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Da die Reaktion bei offenem Port und bei aktiver Firewall (in beiden Fällen keine Rückmeldung des Servers) identisch ist, kann der TCP Null Scan das Vorhandensein einer Firewall nicht erkennen. Darüber hinaus kann die Firewall das Ergebnis sogar verfälschen, indem sie vorgibt, dass ein Port offen ist, da sie auf TCP-Pakete ohne Flags nicht antwortet, obwohl der Port gefiltert ist. Dies ist eine wichtige Information, die bei der Verwendung von Scans, die nicht zwischen einem offenen und einem gefilterten (durch eine Firewall geschützten) Port unterscheiden können, wie z. B. `TCP Null`, `XMAS` oder `FIN`, beachtet werden muss, damit die erhaltenen Ergebnisse richtig interpretiert werden können.



### IV. TCP ACK-Scan



Der TCP ACK-Scan wird verwendet, um das Vorhandensein einer Firewall auf dem Zielhost oder zwischen dem Ziel und der Scan-Quelle zu erkennen.



Im Gegensatz zu anderen Scans versucht der TCP ACK-Scan nicht festzustellen, welche Ports auf dem Host offen sind, sondern ob ein Filtersystem aktiv ist und antwortet für jeden Port mit "gefiltert" oder "ungefiltert". Einige TCP-Scans, wie z.B. `TCP SYN` oder `TCP Connect`, können beides gleichzeitig tun, während andere, wie z.B. `TCP FIN` oder `TCP XMAS`, das Vorhandensein einer Filterung überhaupt nicht feststellen können. Aus diesem Grund kann der TCP ACK-Scan nützlich sein:



![nmap-image](assets/fr/87.webp)



tCP ACK Scan Verhaltensdiagramm für gefilterte und ungefilterte Ports



Wir werden Nmaps Option `-sA` verwenden, um diese Art von Scan durchzuführen. Hier ist das Ergebnis eines TCP ACK-Scans, wenn der Port gefiltert ist, d.h. blockiert und durch eine Firewall geschützt:



![nmap-image](assets/fr/88.webp)



nmap-Anzeige während TCP ACK Scan._



Beispielergebnis für einen Host mit einer Firewall und einen ohne. Nmap liefert `gefiltert` auf den Ports TCP/80 und TCP/81 des Hosts `10.10.10.203`. Bei einer Netzwerkanalyse mit Wireshark sieht das Verhalten wie folgt aus:



![nmap-image](assets/fr/89.webp)



netzwerkerfassung während eines TCP ACK-Scans für einen nicht von einer Firewall gefilterten Port



Der Zielcomputer gibt nichts zurück, wenn eine Firewall vorhanden ist.



Um diesen Scan mit Nmap zu starten, verwenden Sie die Option `-sA` (`scan ACK`):



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Schlussfolgerung



Wir haben uns drei verschiedene Methoden des Scannens über TCP angesehen, die zu den bereits vorgestellten hinzukommen. Diese verschiedenen Methoden sind unter ganz bestimmten Bedingungen und in ganz bestimmten Kontexten zu verwenden, insbesondere im Rahmen von Penetrationstests oder Red-Team-Einsätzen, bei denen Diskretion gefragt ist.



## 15 - Nmap CheatSheet - Zusammenfassung der Befehle des Tutorials



### I. Präsentation



Hier ist eine kurze Zusammenfassung der vielen Befehle und Anwendungsfälle von Nmap, damit Sie sie im täglichen Gebrauch schnell finden und wiederverwenden können.



### II. Nmap: Spickzettel IT-Connect



Hier ist ein Cheatsheet mit den vorgestellten Befehlen. Diese Seite macht es einfach, die häufigsten Anwendungen von Nmap zu finden.





- Hafen-Scan




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Erkennung aktiver Hosts




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



hinweis: Die Option `-sP` ist seit einigen Jahren veraltet und sollte durch `-sn` ersetzt werden. (Update 2025)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Erkennung der Version




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- NSE-Skripte: Suche nach Schwachstellen




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Verwaltung der Nmap-Ausgabe




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Optimierung der Leistung




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- TCP-Scanarten




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Ich hoffe, Sie finden diese Befehle nützlich. Vergessen Sie nicht, das Ziel Ihrer Scans an Ihren Kontext anzupassen und die offizielle Dokumentation zu Rate zu ziehen, um die durchgeführten Tests vollständig zu beherrschen.



### III. Schlussfolgerung



Das Nmap-Tutorial ist nun abgeschlossen. Sie haben jetzt die Grundlagen, die Sie brauchen, um dieses umfassende und leistungsstarke Tool zu benutzen. Wir empfehlen Ihnen dringend, in kontrollierten Umgebungen (Hack The Box, VulnHub, virtuelle Maschinen) zu üben, bevor Sie es in der Produktion einsetzen.



Es gibt noch viel über das Innenleben des Tools und seine fortgeschrittenen Funktionen zu erforschen. Wenn Sie jedoch die hier vorgestellten Befehle und Konzepte beherrschen, können Sie Nmap mit Zuversicht und Relevanz nutzen.