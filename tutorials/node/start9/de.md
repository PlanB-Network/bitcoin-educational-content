---
name: Start9

description: Anleitung zum Einrichten eines privaten Start9-Servers

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Hier ist ein Video-Tutorial von Southern Bitcoiner, ein Video-Guide, der Ihnen zeigt, wie man einen Start9 / StartOS Personal Server einrichtet und benutzt, und wie man einen Bitcoin-Node betreibt.*


## 1️⃣ Einleitung


### Was genau ist Start9?


Start9 ist ein 2020 gegründetes Unternehmen, das vor allem für die Entwicklung von [**StartOS**,](https://github.com/Start9Labs/start-os), einem Linux-basierten Betriebssystem für persönliche Server, bekannt ist. Es ermöglicht den Nutzern, eine breite Palette von Softwarediensten - wie Bitcoin und Lightning-Knoten, Messaging-Apps oder Passwort-Manager - einfach selbst zu hosten und dabei die volle Kontrolle über ihre Daten zu behalten und die Abhängigkeit von zentralisierten Tech-Plattformen zu beseitigen. StartOS bietet eine benutzerfreundliche, browserbasierte Oberfläche, einen kuratierten Marktplatz für die Installation von Diensten und integrierte Datenschutz-Tools wie die Integration von Tor und systemweite HTTPS-Verschlüsselung. Start9 bietet auch Hardwaregeräte an, auf denen das Betriebssystem vorinstalliert ist. Die Software kann jedoch auch auf kompatibler Hardware oder virtuellen Maschinen (VMs) installiert werden.


### Welche Möglichkeiten gibt es?


Start9 bietet sowohl vorgefertigte als auch DIY-Installationsoptionen an. Der [**Server One**] (https://store.start9.com/collections/servers/products/server-one) und der [**Server Pure**] (https://store.start9.com/collections/servers/products/server-pure) sind offizielle Hardware-Geräte mit Hochleistungskomponenten: Der Server One verwendet einen **AMD Ryzen 7 5825U**-Prozessor mit konfigurierbarem RAM (16GB-64GB) und Speicher (2TB-4TB NVMe SSD), während der Server Pure mit einem **Intel i7-10710U** ausgestattet ist und ebenfalls konfigurierbare RAM- und Speicheroptionen bietet. Beide beinhalten **lebenslangen technischen Support**, wenn sie direkt von Start9 erworben werden. Für Benutzer, die Flexibilität bevorzugen, kann StartOS kostenlos auf einer Vielzahl von vorhandener Hardware installiert werden, einschließlich Laptops, Desktops, Mini-PCs und Einplatinencomputern, oder innerhalb von VMs.


![image](assets/en/01.webp)


### Was sind die Unterschiede zu Umbrel?


StartOS und Umbrel vereinfachen beide die Installation von selbst gehosteten Diensten, unterscheiden sich aber in Architektur und Funktionen. Umbrel arbeitet als Anwendungsschicht auf Debian/Ubuntu-Systemen oder VMs, während Start9 ein dediziertes Betriebssystem ist, das eine direkte Hardware- oder VM-Installation erfordert. Umbrel bietet eine ausgefeilte, von macOS inspirierte Oberfläche, während Start9 ein funktionales, minimales Design bevorzugt. Umbrel bietet eine größere [Auswahl an Anwendungen](https://apps.umbrel.com/), während der [Start9 Marketplace](https://marketplace.start9.com/) dies durch erweiterte technische Möglichkeiten kompensiert. Start9 vereinfacht den Zugriff auf erweiterte Einstellungen durch validierte UI-Formulare, wodurch der Bedarf an Befehlszeileninteraktion reduziert wird. Es zeichnet sich auch bei der Backup-Verwaltung durch verschlüsselte System-Backups mit einem Klick aus, eine Funktion, die Umbrel von Haus aus fehlt. StartOS bietet integrierte Überwachungstools und erzwingt HTTPS-Verschlüsselung für den lokalen Netzwerkzugang, was die Sicherheit erhöht. Umbrel verwendet lokal unverschlüsseltes HTTP, obwohl beide Plattformen einen sicheren Fernzugriff über Tor unterstützen. Umbrel ist für Nutzer geeignet, die Wert auf ein reichhaltiges App-Ökosystem und eine ausgefeilte Benutzeroberfläche legen. Start9 ist eine gute Wahl für diejenigen, die Wert auf Sicherheit, Konfigurierbarkeit, Backup-Zuverlässigkeit und fortgeschrittene Service-Verwaltung legen, ohne Kommandozeilen-Kenntnisse zu benötigen. Um mehr über Umbrel und die Unterschiede zu Start9 zu erfahren, besuchen Sie bitte diesen Kurs:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ DIY-Voraussetzungen: Minimale und empfohlene Spezifikationen


Für die grundlegende Nutzung mit minimalen Diensten sind die **Mindestanforderungen** folgende: **1 vCPU-Kern (2,0 GHz+ Boost), 4 GB RAM, 64 GB Speicher** und ein Ethernet-Anschluss. Ich würde jedoch empfehlen, weit darüber hinauszugehen, insbesondere wenn Sie einen Bitcoin-Knoten betreiben. Ich persönlich habe mit 1 TB angefangen und hatte schnell keinen Platz mehr. Streben Sie lieber **mindestens 2 TB Speicherplatz** an, zusammen mit einer **Quad-Core-CPU (2,5 GHz+)** und **8 GB+ RAM**. Das macht einen großen Unterschied bei der Leistung und Langlebigkeit aus. Wenn Sie tiefer eintauchen wollen, finden Sie hier einen aktuellen Community-Thread über [Hardware, die für die Ausführung von StartOS geeignet ist] (https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ Herunterladen und Flashen der Firmware


Um mit der Einrichtung zu beginnen, besuchen Sie von einem anderen Computer aus die [Start9-Website] (https://start9.com/), und navigieren Sie zum Abschnitt "Dokumentation", indem Sie auf "DOCS" klicken. Rufen Sie von dort aus die "Flashing Guides" auf, um die passende Version von StartOS zu finden. Zwei Optionen sind verfügbar:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Dieses Tutorium behandelt die Option "x86/ARM".


Die neueste Betriebssystemversion kann von der [Github-Versionsseite](https://github.com/Start9Labs/start-os/releases/latest) heruntergeladen werden. für Benutzer, die neue Funktionen testen möchten, sind auch [Vorabversionen](https://github.com/Start9Labs/start-os/releases) verfügbar. Am Ende der Seite, unter `Assets`, können Sie die `x86_64` oder `x86_64-nonfree.iso` herunterladen.  Das `x86_64-nonfree.iso`-Image enthält unfreie (Closed-Source-)Software, die für den Server One und die meiste DIY-Hardware benötigt wird, insbesondere für die Unterstützung von Grafik- und Netzwerkgeräten.


Es wird empfohlen, die Integrität der Datei zu überprüfen, indem man ihren SHA256-Hash mit dem auf GitHub aufgeführten vergleicht. Für Linux kann der Befehl `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso` verwendet werden, andere Betriebssysteme werden in der Dokumentation behandelt.


Nach dem Herunterladen und Verifizieren des StartOS-Images muss dieses auf ein USB-Laufwerk geflasht werden. der "BalenaEtcher" ist eine empfohlene Software für diese Aufgabe. Es ist ein kostenloses Open-Source-Tool zum Schreiben von Betriebssystem-Image-Dateien auf USB-Laufwerke und SD-Karten, verfügbar für Windows, macOS und Linux. Laden Sie die entsprechende Version von der offiziellen [Balena Etcher Website](https://www.balena.io/etcher/) herunter und führen Sie das Installationsprogramm aus. Schließen Sie das Ziel-USB-Laufwerk oder die SD-Karte an, öffnen Sie Balena Etcher und klicken Sie auf `Flash from file`, um das heruntergeladene Betriebssystem-Image auszuwählen. Etcher erkennt automatisch die angeschlossenen Laufwerke; wählen Sie das richtige Ziel, wenn mehrere vorhanden sind. Klicken Sie auf "Flash!", um mit dem Schreiben des Images zu beginnen. Etcher validiert den Schreibvorgang automatisch nach Abschluss. Nach Abschluss des Vorgangs können Sie das Laufwerk sicher entfernen und zum Booten des Geräts verwenden.


![image](assets/en/19.webp)


## 4️⃣ Ersteinrichtung


Informationen zur Ersteinrichtung finden Sie auf der Seite Start9 [Dokumentation] (https://docs.start9.com/0.3.5.x/) unter "BENUTZERHANDBUCH", gefolgt von "Erste Schritte - Ersteinrichtung".  Dieses offizielle Handbuch sollte für die aktuellsten Informationen herangezogen werden.


Es werden zwei Optionen vorgestellt:



- Neu anfangen
- Wiederherstellungsoptionen


Für eine neue Serverinstallation wählen Sie "Neu starten". Schließen Sie den Server zunächst an die Stromversorgung und ein Ethernet-Kabel an. Vergewissern Sie sich, dass sich der für die Einrichtung verwendete Computer im selben lokalen Netzwerk befindet. Nehmen Sie das frisch geflashte USB-Laufwerk aus dem Computer und stecken Sie es in den Server.


Sie können den Server von einem beliebigen Computer im selben Netzwerk aus fernsteuern. Öffnen Sie einen Webbrowser und navigieren Sie zu `http://start.local`.


**Hinweis**: Wenn es bei dieser Adresse zu Verbindungsproblemen kommt, liegt das oft daran, dass die Heimnetzwerke die `.local'-Domänennamen nicht auflösen können. Das Problem kann behoben werden, indem Sie direkt über die IP-Adresse auf den Server zugreifen. Die IP-Adresse kann ermittelt werden, indem man sich in die Verwaltungsoberfläche des Routers einloggt (in der Regel unter "192.168.1.1" oder einer ähnlichen Adresse) und das Gerät in der Liste der DHCP-Clients oder der Netzwerkübersicht ausfindig macht. Geben Sie dann die vollständige IP-Adresse (z. B. "http://192.168.1.105") in den Browser ein. Dadurch wird die DNS-Auflösung umgangen. Wenn die Probleme weiterhin bestehen, konsultieren Sie die Seite [Allgemeine Probleme] (https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) oder [wenden Sie sich an den Support] (https://start9.com/contact/)


Der StartOS-Einrichtungsbildschirm sollte erscheinen. Klicken Sie auf "Neu starten", um die Einrichtung des neuen Servers zu beginnen.


![image](assets/en/03.webp)


Der nächste Schritt ist die Auswahl des Speicherlaufwerks, auf dem die StartOS-Daten gespeichert werden sollen.


![image](assets/en/04.webp)


Legen Sie ein sicheres "Passwort" für den Server fest. Notieren Sie es, wie von Start9 empfohlen, und klicken Sie dann auf "FINISH".


![image](assets/en/05.webp)


Ein Bildschirm zeigt an, dass StartOS initialisiert und den Server einrichtet. Der nächste Schritt ist das Herunterladen der Adressinformationen, da die Adresse "start.local" nur für die Einrichtung verwendet wird und danach nicht mehr funktioniert.


![image](assets/en/06.webp)


Die Konfigurationsdatei enthält zwei kritische Zugangsadressen: eine für das "lokale Netz (LAN)" und eine weitere für den sicheren Zugang über "Tor". Beide Adressen sollten in einem sicheren Passwort-Manager gespeichert werden. Der nächste Schritt ist `Vertrauen Sie Ihrer Root CA`. Öffnen Sie eine neue Browser-Registerkarte und folgen Sie den Anweisungen, um der Root-CA zu vertrauen und sich anzumelden. Das Root-CA-Zertifikat kann auch heruntergeladen werden, indem Sie in der heruntergeladenen Datei auf "Zertifikat herunterladen" klicken.


## 5️⃣ Vertrauen Sie Ihrer Root-CA


Nach dem Herunterladen des Zertifikats muss die "Root-CA" des Servers vom Betriebssystem als vertrauenswürdig eingestuft werden. Klicken Sie auf "Anweisungen anzeigen" und suchen Sie die Richtlinien für das jeweilige Betriebssystem.


![image](assets/en/07.webp)


Für ein Linux-System werden die folgenden Befehle verwendet. Öffnen Sie zunächst ein Terminal und installieren Sie die erforderlichen Pakete:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Navigieren Sie zu dem Verzeichnis, in dem das Zertifikat heruntergeladen wurde, normalerweise `~/Downloads`. Führen Sie diese Befehle aus, um das Zertifikat zum Vertrauensspeicher des Betriebssystems hinzuzufügen. Wechseln Sie mit "cd ~/Downloads" in den Ordner "Downloads". Erstellen Sie das erforderliche Verzeichnis mit `sudo mkdir -p /usr/share/ca-certificates/start9`. Kopieren Sie die Zertifikatsdatei, indem Sie `Ihr-Dateiname.crt` durch den tatsächlichen Dateinamen ersetzen, mit `sudo cp "Ihr-Dateiname.crt" /usr/share/ca-certificates/start9/`. Registrieren Sie das Zertifikat dauerhaft, indem Sie seinen Pfad mit `sudo bash -c "echo 'start9/ihr-dateiname.crt' >> /etc/ca-certificates.conf"` an die Systemkonfiguration anhängen. Abschließend erstellen Sie den Vertrauensspeicher mit `sudo update-ca-certificates` neu. Es ist wichtig, den tatsächlichen Dateinamen des Zertifikats zu verwenden und alle Pfade zu verifizieren, bevor Sie diese Befehle ausführen. Durch diesen Vorgang wird ein dauerhaftes Vertrauen für die HTTPS-Verbindungen des Start9-Servers hergestellt.


Eine erfolgreiche Installation wird durch die Ausgabe "1 hinzugefügt" angezeigt. Die meisten Anwendungen sind dann in der Lage, eine sichere Verbindung über `https` herzustellen. Wenn Sie Firefox verwenden, ist ein zusätzlicher [letzter Schritt](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff) erforderlich. Für Chrome oder Brave ist ein anderer [letzter Schritt](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome) erforderlich, um den Browser so zu konfigurieren, dass er die Root-CA respektiert. Testen Sie die Verbindung, indem Sie die Seite aktualisieren. Wenn das Problem weiterhin besteht, beenden Sie den Browser und öffnen Sie ihn erneut, bevor Sie die Seite erneut aufrufen.


![image](assets/en/08.webp)


## 6️⃣ Erste Schritte mit StartOS


Es sollte nun möglich sein, sich über eine sichere HTTPS-Verbindung anzumelden. Geben Sie das "Passwort" ein, um den "Willkommensbildschirm" aufzurufen.


![image](assets/en/09.webp)


Dieser Bildschirm bietet nützliche Abkürzungen für den Einstieg. Die linke Seitenleiste enthält die Hauptmenüpunkte für die Navigation.


## 7️⃣ System


Die Registerkarte "Systeme" in StartOS bietet Zugriff auf die wichtigsten Systemfunktionen zur Verwaltung des persönlichen Servers. Sie bietet Tools für die Systemwartung, Sicherheit, Diagnose und Konfiguration, ohne dass dafür Kommandozeilenkenntnisse erforderlich sind.


Der Abschnitt "Backups" ermöglicht die Erstellung vollständiger Systemsicherungen, einschließlich Diensten, Konfigurationen und Daten, die später wiederhergestellt werden können. Dies ist für die Notfallwiederherstellung oder die Migration auf neue Hardware unerlässlich. Die Backups können auf externen Laufwerken gespeichert werden und werden mit dem Master-Passwort verschlüsselt.


Der Abschnitt "Verwalten" auf der Registerkarte "Systeme" ermöglicht die Kontrolle über wichtige Systemfunktionen. Benutzer können manuell nach StartOS-Updates suchen und diese anwenden und so die Kontrolle über den Aktualisierungsprozess des Systems behalten. Es ist möglich, benutzerdefinierte Dienste oder Dienste von Drittanbietern, die nicht auf dem offiziellen Markt verfügbar sind, per Sideload zu installieren. Wenn der Server nicht über Ethernet angeschlossen ist, können die Wi-Fi-Einstellungen in diesem Bereich konfiguriert werden. Fortgeschrittene Benutzer können den SSH-Zugang für die Systemverwaltung auf Terminal-Ebene aktivieren.


![image](assets/en/10.webp)


Der Abschnitt "Einblicke" bietet eine Echtzeitüberwachung der Leistung und des Zustands des Servers und zeigt die CPU-, RAM- und Festplattennutzung in Diagrammen an. Außerdem wird die Systemtemperatur angezeigt, was für Geräte wie den Raspberry Pi nützlich ist, die keine aktive Kühlung haben. Metriken zur Betriebszeit und durchschnittlichen Auslastung helfen bei der Bewertung der Systemstabilität, und Live-Protokolle sind für die Fehlersuche bei Service- oder Systemproblemen verfügbar.


Der Bereich "Support" bietet Zugang zu den integrierten FAQs, der offiziellen Dokumentation und den Support-Kanälen der Community. Debug-Protokolle können von diesem Bereich heruntergeladen werden, um sie dem Start9-Support zur schnelleren Problemlösung zur Verfügung zu stellen.


![image](assets/en/11.webp)


## 8️⃣ Marktplatz


Der "Marktplatz" wird verwendet, um Dienste auf dem persönlichen Server zu entdecken, zu installieren und zu verwalten. Er bietet Zugang zu Software wie Bitcoin Core, BTCPay Server und electrs. StartOS unterstützt mehrere Marktplätze, darunter die offizielle Start9-Registry und von der Community betriebene Registrys. Diese können hinzugefügt werden, indem man auf `CHANGE` klickt und zur `Community Registry` wechselt, die Zugang zu einer breiteren Palette von Diensten bietet.


![image](assets/en/12.webp)


## 9️⃣ Installation eines vollständigen Bitcoin-Knotens


Die Installation eines Bitcoin full node auf StartOS bietet volle Souveränität über die Bitcoin-Erfahrung. Es ermöglicht die Validierung von Transaktionen und verbessert den Datenschutz und die Sicherheit, indem es die Abhängigkeit von externen Diensten, die Aktivitäten protokollieren können, beseitigt. Es ermöglicht die volle Kontrolle über Transaktionen, die direkt an das Netzwerk übertragen werden können. Die Standardoption ist `Bitcoin Core`, die sich nativ in StartOS integriert und die Verbindung mit Geldbörsen wie Specter, Sparrow oder Electrum für eine Selbstverwahrung ermöglicht. Eine Alternative, `Bitcoin Knots`, ist ebenfalls über die Community Registry verfügbar.


Um Bitcoin Core zu installieren, navigieren Sie zum Marketplace. Suchen Sie in der Standardregistrierung den Bitcoin Core-Dienst und installieren Sie ihn. Nach der Installation erscheint eine "Needs Config"-Eingabeaufforderung, die verlangt, dass die Einstellungen abgeschlossen werden, bevor der Dienst ausgeführt werden kann. Dies tritt in der Regel nach Updates oder Neuinstallationen auf und führt zu einer Überprüfung der RPC-Einstellungen. Fahren Sie mit der Standardkonfiguration fort und klicken Sie auf `Speichern`.


![image](assets/en/13.webp)


Sobald Ihr Knoten vollständig synchronisiert ist, kann er als privates Backend für Geldbörsen wie Sparrow dienen, was eine verbesserte Privatsphäre und Transaktionsvalidierung ermöglicht. Für Benutzer, die erhebliche Beträge speichern, ist es jedoch entscheidend, die Sicherheitsrisiken dieser direkten Verbindung zu verstehen. Wenn ein wallet eine direkte Verbindung zu Bitcoin Core herstellt, kann er sensible Daten preisgeben, da Bitcoin Core öffentliche Schlüssel (xpubs) und wallet-Salden unverschlüsselt auf dem Host-Rechner speichert. Ein kompromittiertes System könnte es einem Angreifer ermöglichen, Ihre Bestände zu entdecken und Sie ins Visier zu nehmen.


Um dieses Risiko zu mindern und ein robusteres Sicherheitsmodell zu erreichen, können Sie einen privaten Electrum Server einrichten. Dieser Server fungiert als Vermittler und indexiert die Blockchain, ohne wallet-spezifische Informationen zu speichern. Indem Sie Ihren wallet mit Ihrem eigenen Electrum-Server statt direkt mit Bitcoin Core verbinden, verhindern Sie, dass der wallet auf die sensiblen Daten des Knotens zugreift.


![image](assets/en/14.webp)


## 🔟 Wahlen einrichten


electrs (Electrum Rust Server) ist ein schneller, effizienter Indexer, der eine Verbindung zu Ihrem Bitcoin Core Node herstellt und Electrum-kompatiblen Wallets die Abfrage von Transaktionshistorie und Salden in Echtzeit ermöglicht. Wenn Sie electrs auf StartOS ausführen, sind Sie nicht mehr auf Electrum-Server von Drittanbietern angewiesen, was den Datenschutz und die Sicherheit erheblich verbessert - Ihre wallet-Abfragen gehen direkt an Ihren selbst gehosteten Knoten.


Zur Einrichtung installieren Sie zunächst den electrs-Dienst vom StartOS-Marktplatz. Das System erfordert eine vollständige Synchronisierung von Bitcoin Core, bevor Sie fortfahren können. Nach der Installation bestätigen Sie die "Needs Config"-Einstellungen mit den empfohlenen Standardwerten und electrs beginnt mit der Indizierung der Blockchain, was je nach Hardware bis zu einem Tag dauern kann.


![image](assets/en/15.webp)


Sobald dies abgeschlossen ist, können Sie Geldbörsen wie Sparrow oder Specter verbinden. Eine erfolgreiche Verbindung ermöglicht es Ihrem wallet, sich direkt mit Ihrem Node zu synchronisieren und bietet eine sichere, private und selbst gehostete Bitcoin-Erfahrung.


## 1️⃣1️⃣ Verbinden Sparrow Wallet


Um Sparrow Wallet mit Ihrem StartOS-Knoten unter Verwendung der electrs-Implementierung zu verbinden, stellen Sie zunächst sicher, dass Bitcoin Core vollständig synchronisiert ist und electrs installiert ist und läuft. Öffnen Sie Sparrow Wallet auf Ihrem Gerät und navigieren Sie zu `Datei` -> `Einstellungen` -> `Server`. Wählen Sie dann "Privater Electrum Server". Geben Sie in das URL-Feld den `Tor-Hostnamen` und den `Port` für electrs ein, den Sie in StartOS unter `Dienste` -> `electrs` -> `Eigenschaften` finden (endet normalerweise auf `.onion:50001`).


![image](assets/en/16.webp)


Als nächstes aktivierst du Tor, indem du "Proxy verwenden" anklickst und die Proxy-Adresse auf "127.0.0.1" und den Port auf "9050" setzt. Klicke auf "Verbindung testen" und warte ein paar Augenblicke. Bei einer erfolgreichen Verbindung wird eine Bestätigungsmeldung wie "Mit electrs verbunden" angezeigt. Sobald dies bestätigt ist, schließen Sie die Einstellungen und fahren Sie mit der Erstellung oder Wiederherstellung Ihres wallet fort. Dieses Setup stellt sicher, dass Ihr wallet Ihren eigenen Knotenpunkt über electrs abfragt, was eine vollständige Privatsphäre und einen vertrauenswürdigen Betrieb gewährleistet.


![image](assets/en/17.webp)


## 🎯 Schlussfolgerung


StartOS von Start9 ist eine benutzerfreundliche, datenschutzfreundliche Plattform, die für das Selbsthosten von wichtigen Diensten wie Bitcoin- und Lightning-Knoten, Wallets und persönlichen Anwendungen entwickelt wurde. Durch eine übersichtliche grafische Oberfläche, automatische Backups, Zustandsüberwachung und einen sicheren Tor-Zugang sind keine Kommandozeilen-Kenntnisse erforderlich, was sie ideal für technisch nicht versierte Nutzer macht. Seine modulare Architektur unterstützt die nahtlose Integration mit Tools wie electrs oder Sparrow und gibt dir die volle Kontrolle über deine finanzielle und digitale Souveränität. Mit einem starken Fokus auf Transparenz, lokaler Kontrolle und Erweiterbarkeit ermöglicht es StartOS seinen Nutzern, sich von zentralisierten Plattformen zu lösen und ihre eigene private, robuste Infrastruktur zu betreiben.