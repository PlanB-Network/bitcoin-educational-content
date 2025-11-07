---
name: Plan ₿ Akademie - Birnen App
description: Wie installiert und verwendet man die Anwendung Plan ₿ Academy auf Pears?
---

![cover](assets/cover.webp)


Sie wissen wahrscheinlich schon, dass die Plan ₿ Academy die größte Bildungsdatenbank für Bitcoin ist, die Kurse, Tutorien und Tausende von Open-Source-Ressourcen zusammenführt. Ursprünglich war die Plan ₿ Academy eine Website. Aber was würde passieren, wenn man nicht mehr normal darauf zugreifen könnte, zum Beispiel im Falle einer Zensur?


In diesem Tutorial lernen wir, wie man die Plattform **Plan ₿ Academy** auf eine wirklich zensurresistente Art und Weise mit **Pears**, einer Peer-to-Peer (P2P) Technologie, die von **Holepunch** entwickelt und von **Tether** unterstützt wird, betreibt.


Pears ist die Software, die es uns ermöglicht, die Plan ₿ Academy-Plattform zu betreiben, ohne auf eine zentrale Website angewiesen zu sein. In diesem Tutorial werden wir Pears auf Ihrem Computer installieren, um auf die Plan ₿ Academy über Pears zugreifen zu können.


Das Ziel von Pears ist einfach: Es soll die Verbreitung und Nutzung von Webanwendungen ermöglichen, ohne von einer zentralisierten Infrastruktur abhängig zu sein (keine Server, keine Hosts, keine Vermittler). Mit anderen Worten: Selbst wenn ein Cloud-Anbieter seinen Betrieb einstellt oder ein Land eine Domain sperrt, bleibt die Anwendung unter den Peers des Netzwerks erhalten. Dieser Ansatz ermöglicht es unserer Bildungsplattform, der Plan ₿ Academy, weltweit zugänglich zu bleiben, ohne dass es einen einzigen Ausfallpunkt gibt.


---

**TL;DR:*



- Birnen installieren;



- Führen Sie den folgenden Befehl aus, um die Plan ₿ Academy App zu starten:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Was ist Birnen?


Pears ist gleichzeitig eine Laufzeitumgebung, ein Entwicklungswerkzeug und eine Bereitstellungsplattform für Peer-to-Peer-Anwendungen. Dieses Open-Source-Tool ermöglicht die Erstellung, gemeinsame Nutzung und Ausführung von Software ohne Server oder Infrastruktur, direkt zwischen Benutzern. In der Praxis bedeutet dies, dass eine Anwendung nicht auf einem zentralen Server gehostet wird, sondern jeder Benutzer ein Knoten im Netzwerk ist: Er teilt einen Teil der Anwendung und der Daten mit anderen Peers. Das gesamte System bildet ein verteiltes Netz, in dem jede Instanz zusammenarbeitet, um den Dienst zugänglich zu halten.


![Image](assets/fr/01.webp)


Dieser Ansatz basiert auf einer Reihe von modularen Softwarekomponenten, die von Holepunch entwickelt wurden:



- Hypercore**: ein verteiltes Protokoll, das Datenkonsistenz und Sicherheit ohne zentrale Datenbank gewährleistet.
- Hyperbee**: ein auf Hypercore aufbauender Index, mit dem Daten effizient organisiert und abgefragt werden können.
- Hyperdrive**: ein verteiltes Dateisystem, das zum Speichern und Synchronisieren von Anwendungsdateien zwischen Peers verwendet wird.
- Hyperswarm** und **HyperDHT**: Netzwerkschichten, die die Erkennung von Peers und weltweite Verbindungen ohne zentralen Server ermöglichen.
- Secretstream**: ein Ende-zu-Ende-Verschlüsselungsprotokoll, das die Kommunikation zwischen Peers sichert.


Durch die Kombination dieser Komponenten ermöglicht Pears die Erstellung von autonomen, verschlüsselten und verteilten Anwendungen, bei denen jeder Nutzer aktiv am Netzwerk teilnimmt. Diese dezentrale Architektur eliminiert Infrastrukturkosten, Zensurrisiken und SPOFs (*Single Points of Failure*).


Pears wird von Holepunch entwickelt, einem von Mathias Buus und Paolo Ardoino (CEO von Tether und CTO von Bitfinex) gegründeten Unternehmen, das sich zum Ziel gesetzt hat, die Peer-to-Peer-Logik über Bitcoin hinaus zu erweitern. Ihr Ziel ist es, das "*Internet der Peers*" aufzubauen, in dem jede Anwendung ohne Genehmigung, ohne Server und ohne Vermittler arbeiten kann. Holepunch steht bereits hinter **Keet**, einer vollständig P2P-fähigen Videokonferenz- und Messaging-App.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Diese Pears-Installationsanleitung ist in mehrere Abschnitte unterteilt, die von Ihrem Betriebssystem abhängen. Gehen Sie direkt zu dem Abschnitt, der Ihrer Umgebung entspricht, um die entsprechenden Anweisungen zu befolgen:*



- Linux (Debian)** → Abschnitt **2**
- Fenster** → Abschnitt **3**
- macOS** → Abschnitt **4**


## 2. Wie installiert man Pears unter Linux (Debian)?


Die Installation von Pears unter Debian ist relativ einfach, erfordert aber ein paar Voraussetzungen, die wir in diesem Abschnitt näher erläutern werden.


### 2.1. Aktualisieren Sie das System


Vor allem muss sichergestellt werden, dass Ihr System auf dem neuesten Stand ist.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Abhängigkeiten installieren


Pears stützt sich auf einige Systembibliotheken, darunter `libatomic1`, die von der Bare JavaScript-Laufzeit-Engine verwendet werden. Installieren Sie sie mit dem folgenden Befehl:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Node.js und npm über NVM installieren


Pears wird über *npm*, den *Node.js*-Paketmanager, verteilt. Obwohl Pears nicht direkt von *Node.js* abhängt, um zu laufen, wird es für die Installation benötigt. Der empfohlene Weg, *Node.js* unter Linux zu installieren, ist über *NVM* (*Node Version Manager*), der es Ihnen ermöglicht, mehrere Versionen von Node nebeneinander zu verwalten.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Laden Sie dann Ihr Terminal neu, um *NVM* zu aktivieren:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Prüfen Sie, ob *NVM* richtig installiert ist:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Installieren Sie als nächstes eine stabile Version von *Node.js* (zum Beispiel die aktuelle LTS-Version):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Überprüfen Sie, ob *Node.js* und *npm* richtig installiert sind:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Pears mit npm installieren


Sobald *npm* verfügbar ist, können Sie den Pears CLI global auf Ihrem System installieren. Dadurch können Sie den Befehl "Pears" von jedem Verzeichnis aus ausführen.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Birnen initialisieren


Nach der Installation führen Sie einfach den folgenden Befehl in Ihrem Terminal aus:


```bash
pear
```


Beim ersten Start verbindet sich Pears mit dem Peer-to-Peer-Netzwerk, um die erforderlichen Komponenten herunterzuladen. Dieser Prozess ist nicht auf einen zentralen Server angewiesen - die Dateien werden direkt von anderen Peers abgerufen.


![Image](assets/fr/10.webp)


Sobald der Download abgeschlossen ist, führen Sie den Befehl erneut aus, um sicherzustellen, dass alles funktioniert:


```bash
pear
```


![Image](assets/fr/11.webp)


Wenn alles korrekt installiert ist, wird das Pears-Hilfemenü mit einer Liste der verfügbaren Befehle angezeigt.


### 2.6. Testbirnen mit Keet


Um zu überprüfen, ob Pears voll funktionsfähig ist, können Sie eine vorhandene P2P-Anwendung im Netzwerk starten, z. B. Keet, die von Holepunch entwickelte Open-Source-Software für Messaging und Videokonferenzen.


```bash
pear run pear://keet
```


Dieser Befehl lädt die Keet-Anwendung direkt aus dem Pears-Netzwerk, ohne einen zentralen Server zu verwenden. Wenn Keet korrekt gestartet wird, bedeutet dies, dass Ihre Pears-Installation voll funktionsfähig ist.


![Image](assets/fr/12.webp)


Ihr Linux-System ist nun bereit, Peer-to-Peer-Anwendungen mit Pears auszuführen und zu hosten.


## 3. Wie installiert man Pears unter Windows?


Die Installation von Pears unter Windows ist genauso einfach wie unter Linux, erfordert aber ein paar spezielle Tools.


*Wenn Sie Linux verwenden und Pears bereits installiert haben, können Sie direkt zu **Schritt 5** übergehen


### 3.1. Öffnen Sie PowerShell als Administrator


Starten Sie zunächst PowerShell mit Administratorrechten:



- Klicken Sie auf das Menü Start;
- Geben Sie "PowerShell" ein;
- Klicken Sie mit der rechten Maustaste auf "*Windows PowerShell*";
- Wählen Sie "*Ausführen als Administrator*".


![Image](assets/fr/15.webp)


### 3.2. NVS herunterladen


Pears wird über *npm*, den *Node.js* Paketmanager, installiert. Unter Windows ist die von Holepunch empfohlene Methode die Verwendung von *NVS* (*Node Version Switcher*), die auf diesem System stabiler ist als *NVM*.


Führen Sie in PowerShell den folgenden Befehl aus, um die neueste Version von *NVS* zu installieren:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Node.js installieren


Starten Sie PowerShell nach der Installation neu, und geben Sie dann den folgenden Befehl ein:


```powershell
nvs
```


Sie sollten eine Liste der verfügbaren *Node.js*-Versionen sehen. Wählen Sie die erste aus, indem Sie die Taste "a" auf Ihrer Tastatur drücken.


![Image](assets/fr/17.webp)


*Node.js* ist jetzt installiert.


![Image](assets/fr/18.webp)


### 3.4. Überprüfung der Installationen


Stellen Sie sicher, dass *Node.js* und *npm* zugänglich sind:


```powershell
node -v
npm -v
```


Beide Befehle sollten eine Versionsnummer zurückgeben.


![Image](assets/fr/19.webp)


### 3.5. Pears mit npm installieren


Sobald *Node.js* und *npm* verfügbar sind, installieren Sie **Pears CLI** global auf Ihrem System:


```powershell
npm install -g pear
```


Dies installiert die `pear`-Binärdatei in Ihrem globalen *npm*-Verzeichnis.


![Image](assets/fr/20.webp)


### 3.6. Überprüfen und Initialisieren von Pears


Sobald die Installation abgeschlossen ist, führen Sie sie aus:


```powershell
pear
```


Beim ersten Start lädt Pears automatisch die erforderlichen Komponenten aus dem Peer-to-Peer-Netzwerk herunter. Dieser Vorgang kann einige Augenblicke dauern.


![Image](assets/fr/21.webp)


Wenn alles gut gegangen ist, sollten Sie das Pears CLI-Hilfemenü mit der Liste der verfügbaren Unterbefehle (run, seed, info...) sehen.


### 3.7. Testbirnen mit Keet


Um zu überprüfen, ob Pears voll funktionsfähig ist, können Sie eine bestehende P2P-Anwendung im Netz starten, z. B. Keet - die von Holepunch entwickelte Open-Source-Software für Nachrichtenübermittlung und Videokonferenzen.


```bash
pear run pear://keet
```


Dieser Befehl lädt die Keet-Anwendung direkt aus dem Pears-Netzwerk, ohne einen zentralen Server zu verwenden. Wenn Keet erfolgreich gestartet wird, bedeutet dies, dass Ihre Pears-Installation voll funktionsfähig ist.


![Image](assets/fr/22.webp)


Ihr Windows-System ist nun bereit, Peer-to-Peer-Anwendungen mit Pears auszuführen und zu hosten.


## 4. So installieren Sie Pears unter macOS


Die Installation von Pears unter macOS ist ähnlich wie unter Linux, erfordert aber einige Anpassungen, die speziell für die Apple-Umgebung gelten. Lassen Sie uns diese Schritte gemeinsam durchgehen.


*Wenn Sie Linux oder Windows verwenden und Pears bereits installiert haben, können Sie direkt zu **Schritt 5** übergehen


### 4.1. Systemvoraussetzungen prüfen


Stellen Sie vor der Installation sicher, dass *Xcode Command Line Tools* auf Ihrem System installiert ist. Dieses Paket enthält die erforderlichen Build-Tools für *Node.js* und seine Abhängigkeiten.


Öffnen Sie dazu ein Terminal mit der Tastenkombination "Befehl + Leertaste", geben Sie "Terminal" ein und drücken Sie die "Eingabetaste". Führen Sie dann den folgenden Befehl in dem Terminal aus, um es zu installieren:


```bash
xcode-select --install
```


Wenn die Tools bereits auf Ihrem System installiert sind, werden Sie von macOS benachrichtigt.


### 4.2. NVM installieren


Pears wird über *npm*, den *Node.js* Paketmanager, verteilt. Obwohl Pears nicht direkt von *Node.js* abhängt, um zu funktionieren, ist es für die Installation erforderlich. Die empfohlene Methode zur Installation von *Node.js* auf macOS ist *NVM* (*Node Version Manager*), mit dem Sie mehrere Node-Versionen gleichzeitig verwalten können.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Laden Sie dann Ihr Terminal neu, um *NVM* zu aktivieren:


```bash
source ~/.zshrc
```


Wenn Sie *bash* anstelle von *zsh* verwenden, führen Sie aus:


```bash
source ~/.bashrc
```


Prüfen Sie dann, ob *NVM* korrekt installiert ist:


```bash
nvm --version
```


Ihr Terminal sollte die installierte *NVM*-Version anzeigen.


### 4.3. Node.js und npm installieren


Installieren Sie als nächstes eine stabile Version von *Node.js* (z. B. die aktuelle LTS-Version):


```bash
nvm install --lts
```


Wenn die Installation abgeschlossen ist, überprüfen Sie die installierten Versionen:


```bash
node -v
npm -v
```


Beide Befehle sollten eine Versionsnummer zurückgeben.


### 4.4. Pears mit npm installieren


Sobald *npm* verfügbar ist, können Sie den Pears CLI global auf Ihrem System installieren. Dadurch können Sie den Befehl `pear` von jedem Verzeichnis aus ausführen.


```bash
npm install -g pear
```


### 4.5. Birnen initialisieren


Nach der Installation führen Sie einfach den folgenden Befehl in Ihrem Terminal aus:


```bash
pear
```


Beim ersten Start verbindet sich Pears mit dem Peer-to-Peer-Netzwerk, um die erforderlichen Komponenten herunterzuladen. Dieser Prozess erfordert keinen zentralen Server - die Dateien werden direkt von anderen Peers abgerufen.


Sobald der Download abgeschlossen ist, führen Sie den Befehl erneut aus, um zu überprüfen, ob alles funktioniert:


```bash
pear
```


Wenn alles korrekt installiert ist, erscheint das Pears-Hilfemenü mit einer Liste der verfügbaren Befehle.


### 4.6. Testbirnen mit Keet


Um zu überprüfen, ob Pears voll funktionsfähig ist, können Sie eine bereits im Netzwerk verfügbare P2P-Anwendung starten, z. B. Keet, die Open-Source-Software für Messaging und Videokonferenzen von Holepunch.


```bash
pear run pear://keet
```


Dieser Befehl lädt die Keet-App direkt aus dem Pears-Netzwerk, ohne einen zentralen Server zu verwenden. Wenn Keet erfolgreich gestartet wird, bedeutet dies, dass Ihre Pears-Installation voll funktionsfähig ist.


Ihr macOS-System ist nun bereit, Peer-to-Peer-Anwendungen mit Pears auszuführen und zu hosten.


## 5. Verwendung von Plan ₿ Academy bei Birnen


Sobald Pears installiert ist und läuft, können Sie die Plattform **Plan ₿ Academy** direkt über das P2P-Netzwerk starten. Führen Sie einfach den folgenden Befehl in Ihrem Terminal aus (der gleiche Befehl funktioniert unter Linux, Windows und macOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Sobald der Ladevorgang abgeschlossen ist, öffnet sich die Plan ₿ Academy in Ihrer Pears-Umgebung und kann wie die ursprüngliche Website genutzt werden - jedoch ohne Abhängigkeit von einem zentralen Server.


![Image](assets/fr/14.webp)


## 6. Aussaatplan ₿ Akademie für Birnen


Im Pears-Netzwerk bedeutet *seed* eine Anwendung von Ihrem eigenen Rechner aus an andere Peers weiterzugeben. In der Praxis wird Ihr Computer, wenn Sie seed Plan ₿ Academy verwenden, zu einer Datenquelle, die es anderen Nutzern ermöglicht, die Anwendung herunterzuladen, ohne auf einen zentralen Server angewiesen zu sein.


Dieser Mechanismus stärkt die Widerstandsfähigkeit und Zensurresistenz unserer Anwendung im Pears-Netzwerk. Je mehr Peers seed eine Anwendung haben, desto verfügbarer und dezentraler wird sie, selbst wenn einige ursprüngliche Knoten offline gehen.


Um die Verteilung von Plan ₿ Academy zu unterstützen, führen Sie einfach den folgenden Befehl aus:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Solange dieser Befehl aktiv ist, nimmt Ihr Gerät an der Verteilung der Dateien der Anwendung teil. Wenn Sie das Terminal schließen, wird der Freigabeprozess beendet.


Um das Seeding nach einem Neustart fortzusetzen, können Sie den Befehl im Hintergrund ausführen oder einen Systemdienst erstellen - zum Beispiel einen systemd-Dienst unter Linux, einen LaunchAgent unter macOS oder eine geplante Aufgabe unter Windows. Diese Methoden stellen sicher, dass die Plan ₿ Academy-Anwendung das Seeding beim Systemstart automatisch fortsetzt.


Vielen Dank, dass Sie zur dezentralen Verbreitung der Plan ₿ Academy on Pears beitragen und helfen, Bitcoin Bildung wirklich zensurresistent zu machen!