---
name: Karte ₿ Akademie - Birnen App
description: Wie installiere und verwende ich die Anwendung Plan ₿ Academy auf Pears?
---

![cover](assets/cover.webp)



Wie Sie wahrscheinlich wissen, ist die Plan ₿ Academy die größte Bildungsdatenbank, die sich mit Bitcoin befasst und Kurse, Tutorien und Tausende von Ressourcen zusammenführt, die unter einer offenen Lizenz veröffentlicht werden. Ursprünglich war die Plan ₿ Academy eine Website. Aber was würde passieren, wenn man nicht mehr normal darauf zugreifen könnte, zum Beispiel im Falle einer Zensur?



In diesem Tutorial lernen wir, wie man die Plattform **Plan ₿ Academy** dank **Pears**, einer Peer-to-Peer (P2P)-Technologie, die von **Holepunch** entwickelt und von **Tether** unterstützt wird, auf eine wirklich unanfechtbare Weise betreibt.



Pears ist die Software, die es uns ermöglicht, die Plan ₿ Academy-Plattform zu betreiben, ohne auf eine zentrale Website angewiesen zu sein. In diesem Tutorial werden wir Pears auf Ihrem Computer installieren, um auf die Plan ₿ Academy über Pears zuzugreifen.



Das Ziel von Pears ist einfach: Es soll die Verbreitung und Nutzung von Webanwendungen ermöglichen, ohne auf eine zentralisierte Infrastruktur angewiesen zu sein (keine Server, keine Hosts, keine Vermittler). Mit anderen Worten: Selbst wenn ein Cloud-Anbieter seinen Betrieb einstellt oder ein Land eine Domain sperrt, lebt die Anwendung unter den Peers des Netzwerks weiter. Dieser Ansatz ermöglicht es unserer Bildungsplattform Plan ₿ Academy, überall auf der Welt zugänglich zu bleiben, ohne dass es einen einzigen Ausfallpunkt gibt.



---

**TL;DR :*





- Birnen installieren ;





- Führen Sie den folgenden Befehl aus, um die Anwendung Plan ₿ Academy zu starten:



```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



---

## 1. Birnen einbauen



### 1.1 Was ist Birnen?



Pears ist eine Laufzeitumgebung, ein Entwicklungswerkzeug und eine Einsatzplattform für Peer-to-Peer-Anwendungen. Dieses Open-Source-Tool ermöglicht die Erstellung, gemeinsame Nutzung und Ausführung von Software ohne Server oder Infrastruktur, direkt zwischen Nutzern. Konkret bedeutet das: Statt eine Anwendung auf einem zentralen Server zu hosten, wird jeder Nutzer zu einem Netzwerkknoten, der Teile der Anwendung und Daten mit anderen Peers teilt. Das gesamte System bildet ein verteiltes Netz, in dem jede Instanz kooperiert, um den Dienst zugänglich zu halten.



![Image](assets/fr/01.webp)



Dieser Ansatz basiert auf einer Reihe von modularen Softwarebausteinen, die von Holepunch entwickelt wurden:




- Hypercore**: ein verteiltes Protokoll, das Datenkonsistenz und -sicherheit ohne zentrale Datenbank gewährleistet.
- Hyperbee**: ein Indexer, der auf Hypercore aufbaut, um Daten effizient zu organisieren und zu durchsuchen.
- Hyperdrive**: ein verteiltes Dateisystem, das zum Speichern und Synchronisieren von Anwendungsdateien zwischen Peers verwendet wird.
- Hyperswarm** und **HyperDHT**: Netzwerkschichten, die die Erkennung und Verbindung zwischen Peers weltweit ermöglichen, ohne dass ein zentraler Server benötigt wird.
- Secretstream**: ein E2E-Verschlüsselungsprotokoll zur Sicherung des Austauschs zwischen zwei Peers.



Durch die Kombination dieser Komponenten ermöglicht Pears die Erstellung autonomer, verschlüsselter und verteilter Anwendungen, bei denen jeder Nutzer aktiv am Netz teilnimmt. Diese dezentrale Architektur eliminiert Infrastrukturkosten, Zensurrisiken und SPOFs (*Single Point of Failure*).



Pears wird von Holepunch entwickelt, einem von Mathias Buus und Paolo Ardoino (CEO von Tether und CTO von Bitfinex) gegründeten Unternehmen, das sich zum Ziel gesetzt hat, die Peer-to-Peer-Logik über Bitcoin hinaus zu erweitern. Ihr Ziel ist es, das "Peer-to-Peer-Internet" aufzubauen, in dem jede Anwendung ohne Autorisierung, ohne Server und ohne Vermittler laufen kann. Holepunch steht bereits hinter **Keet**, einer vollständig P2P-fähigen Anwendung für Videokonferenzen und Nachrichtenaustausch.



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Diese Pears-Installationsanleitung ist in mehrere Abschnitte unterteilt, die von Ihrem Betriebssystem abhängen. Gehen Sie direkt zu dem Abschnitt, der Ihrer Umgebung entspricht, um die entsprechenden Anweisungen zu befolgen :*




- Linux (Debian)** → Teil **1.2.**
- Windows** → Teil **1.3.**
- macOS** → Teil **1.4.**




### 1.2 - Wie kann ich Pears unter Linux (Debian) installieren?



Die Installation von Pears auf einem Debian-System ist relativ einfach, erfordert aber ein paar Voraussetzungen, die wir in diesem Abschnitt im Detail erklären.



#### 1.2.1. Aktualisierung des Systems



Zuallererst ist es wichtig, dass Ihr System auf dem neuesten Stand ist.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



#### 1.2.2 Installieren von Abhängigkeiten



Pears stützt sich auf eine Reihe von Systembibliotheken, einschließlich `libatomic1`, die von der Bare JavaScript-Laufzeit verwendet wird. Installieren Sie sie mit dem folgenden Befehl:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



#### 1.2.3 Installation von Node.js und npm über NVM



Pears wird über *npm*, den *Node.js*-Paketmanager, verteilt. Obwohl Pears nicht direkt von *Node.js* abhängt, um zu funktionieren, ist es für die Installation notwendig. Die empfohlene Methode zur Installation von *Node.js* unter Linux ist *NVM* (*Node Version Manager*), mit dem Sie mehrere Versionen von Node parallel verwalten können.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Laden Sie dann Ihr Terminal neu, um *NVM* zu aktivieren:



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Prüfen Sie, ob *NVM* installiert ist:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Dann installieren Sie eine stabile Version von *Node.js* (z.B. die aktuelle LTS):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Überprüfen Sie *Node.js* und *npm* Installationen:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



#### 1.2.4 Installation von Pears mit npm



Sobald *npm* verfügbar ist, können Sie Pears CLI global auf Ihrem System installieren. Dadurch können Sie den Befehl `pear` von jedem Verzeichnis aus ausführen.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



#### 1.2.5. Birnen initialisieren



Nach der Installation führen Sie einfach den folgenden Befehl in Ihrem Terminal aus:



```bash
pear
```



Beim ersten Start verbindet sich Pears mit dem Peer-to-Peer-Netz, um die erforderlichen Komponenten herunterzuladen. Dieser Prozess erfordert keinen zentralen Server: Die Dateien werden direkt von anderen Peers bezogen.



![Image](assets/fr/10.webp)



Sobald der Download abgeschlossen ist, führen Sie den Befehl erneut aus, um zu überprüfen, ob alles funktioniert:



```bash
pear
```



![Image](assets/fr/11.webp)



Wenn alles korrekt installiert ist, wird die Pears-Hilfe mit einer Liste der verfügbaren Befehle angezeigt.



#### 1.2.6. Prüfung von Birnen mit Keet



Um zu überprüfen, ob Pears voll funktionsfähig ist, können Sie eine P2P-Anwendung starten, die bereits im Netz verfügbar ist, z. B. Keet, die Open-Source-Nachrichten- und Videokonferenzsoftware von Holepunch.



```bash
pear run pear://keet
```



Mit diesem Befehl wird die Keet-Anwendung direkt aus dem Pears-Netzwerk geladen, ohne einen zentralen Server zu durchlaufen. Wenn Keet korrekt gestartet wird, ist Ihre Pears-Installation voll funktionsfähig.



![Image](assets/fr/12.webp)



Ihr Linux-System ist nun bereit, Peer-to-Peer-Anwendungen mit Pears auszuführen und zu hosten.



### 1.3 - Wie kann ich Pears unter Windows installieren?



Die Installation von Pears unter Windows ist genauso einfach wie unter Linux, erfordert aber ein paar spezielle Tools.



*Wenn Sie Linux verwenden und Pears bereits installiert haben, können Sie direkt mit Schritt 2 fortfahren



#### 1.3.1. Öffnen Sie PowerShell im Administratormodus



Führen Sie zunächst PowerShell mit Administratorrechten aus:




- Klicken Sie auf das Menü Start;
- Geben Sie PowerShell ein;
- Klicken Sie mit der rechten Maustaste auf "*Windows PowerShell*" ;
- Wählen Sie "*Ausführen als Administrator*".



![Image](assets/fr/15.webp)



#### 1.3.2. NVS herunterladen



Pears wird über *npm*, den *Node.js* Paketmanager, installiert. Unter Windows ist die von Holepunch empfohlene Methode die Verwendung von *NVS* (*Node Version Switcher*), die auf diesem System stabiler ist als *NVM*.



Führen Sie in PowerShell den folgenden Befehl aus, um die neueste Version von *NVS* zu installieren:



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



#### 1.3.3. Node.js installieren



Starten Sie PowerShell nach der Installation neu und geben Sie den folgenden Befehl ein:



```powershell
nvs
```



Sie sollten eine Liste der verfügbaren *Node.js*-Versionen sehen. Wählen Sie die erste aus, indem Sie die Taste "a" auf Ihrer Tastatur drücken.



![Image](assets/fr/17.webp)



*Node.js* ist installiert.



![Image](assets/fr/18.webp)



#### 1.3.4. Installationen prüfen



Stellen Sie sicher, dass *Node.js* und *npm* zugänglich sind:



```powershell
node -v
npm -v
```



Beide Befehle müssen eine Versionsnummer zurückgeben.



![Image](assets/fr/19.webp)



#### 1.3.5. Installation von Pears mit npm



Sobald *Node.js* und *npm* verfügbar sind, installieren Sie **Pears CLI** global auf Ihrem System:



```powershell
npm install -g pear
```



Dadurch wird die `pear`-Binärdatei in Ihrem globalen *npm*-Verzeichnis installiert.



![Image](assets/fr/20.webp)



#### 1.3.6. Prüfen und Initialisieren von Pears



Sobald die Installation abgeschlossen ist, führen Sie :



```powershell
pear
```



Beim ersten Start lädt Pears automatisch die erforderlichen Komponenten aus dem Peer-to-Peer-Netzwerk herunter. Dieser Vorgang kann einige Augenblicke dauern.



![Image](assets/fr/21.webp)



Wenn alles gut gegangen ist, sollten Sie den Hilfebildschirm von CLI Pears mit einer Liste der verfügbaren Unterbefehle (run, seed, info...) sehen.



#### 1.3.7. Prüfung von Birnen mit Keet



Um zu überprüfen, ob Pears voll funktionsfähig ist, können Sie eine P2P-Anwendung starten, die bereits im Netz verfügbar ist, z. B. Keet, die Open-Source-Nachrichten- und Videokonferenzsoftware von Holepunch.



```bash
pear run pear://keet
```



Mit diesem Befehl wird die Keet-Anwendung direkt aus dem Pears-Netzwerk geladen, ohne einen zentralen Server zu durchlaufen. Wenn Keet korrekt gestartet wird, ist Ihre Pears-Installation voll funktionsfähig.



![Image](assets/fr/22.webp)



Ihr Windows-System ist nun bereit, Peer-to-Peer-Anwendungen mit Pears auszuführen und zu hosten.



### 1.4. Wie installiert man Pears auf macOS?



Die Installation von Pears unter macOS ähnelt der Installation unter Linux, erfordert aber einige Anpassungen, die speziell für die Apple-Umgebung gelten. Lassen Sie uns diese Schritte gemeinsam entdecken.



*Wenn Sie Linux oder Windows verwenden und Pears bereits installiert haben, können Sie direkt mit Schritt 2 fortfahren



#### 1.4.1. Systemanforderungen prüfen



Bitte stellen Sie vor der Installation sicher, dass *Xcode Command Line Tools* auf Ihrem System vorhanden ist. Dieses Paket bietet die notwendigen Kompilierungswerkzeuge für _Node.js_ und seine Abhängigkeiten.



Öffnen Sie dazu ein Terminal mit der Tastenkombination `Cmd + Leertaste`, geben Sie `Terminal` ein und drücken Sie die Taste `Enter`. Sie können dann diesen Befehl in das Terminal eingeben, um die Installation zu starten:



```bash
xcode-select --install
```



Wenn die Tools bereits auf Ihrem System installiert sind, informiert macOS Sie darüber.



#### 1.4.2. Installieren von NVM



Pears wird über *npm*, den *Node.js*-Paketmanager, verteilt. Obwohl Pears nicht direkt von *Node.js* abhängt, um zu funktionieren, ist es für die Installation notwendig. Die empfohlene Methode zur Installation von *Node.js* auf macOS ist *NVM* (*Node Version Manager*), mit dem Sie mehrere Versionen von Node parallel verwalten können.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Laden Sie dann Ihr Terminal neu, um *NVM* zu aktivieren:



```bash
source ~/.zshrc
```



Wenn Sie *bash* und nicht *zsh* verwenden, führen Sie :



```bash
source ~/.bashrc
```



Prüfen Sie dann, ob *NVM* installiert ist:



```bash
nvm --version
```



Das Terminal sollte die auf Ihrem System installierte Version von *NVM* anzeigen.



#### 1.4.3 Installation von Node.js und npm



Dann installieren Sie eine stabile Version von *Node.js* (z.B. die aktuelle LTS):



```bash
nvm install --lts
```



Überprüfen Sie nach Abschluss der Installation die installierten Versionen:



```bash
node -v
npm -v
```



Beide Befehle müssen eine Versionsnummer zurückgeben.



#### 1.4.4 Installation von Pears mit npm



Sobald *npm* verfügbar ist, können Sie Pears CLI global auf Ihrem System installieren. Dadurch können Sie den Befehl `pear` von jedem Verzeichnis aus ausführen.



```bash
npm install -g pear
```



#### 1.4.5. Birnen initialisieren



Nach der Installation führen Sie einfach den folgenden Befehl in Ihrem Terminal aus:



```bash
pear
```



Beim ersten Start verbindet sich Pears mit dem Peer-to-Peer-Netz, um die erforderlichen Komponenten herunterzuladen. Dieser Prozess erfordert keinen zentralen Server: Die Dateien werden direkt von anderen Peers bezogen.



Sobald der Download abgeschlossen ist, führen Sie den Befehl erneut aus, um zu überprüfen, ob alles funktioniert:



```bash
pear
```



Wenn alles korrekt installiert ist, wird die Pears-Hilfe mit einer Liste der verfügbaren Befehle angezeigt.



#### 1.4.6. Prüfung von Birnen mit Keet



Um zu überprüfen, ob Pears voll funktionsfähig ist, können Sie eine P2P-Anwendung starten, die bereits im Netz verfügbar ist, z. B. Keet, die Open-Source-Nachrichten- und Videokonferenzsoftware von Holepunch.



```bash
pear run pear://keet
```



Mit diesem Befehl wird die Keet-Anwendung direkt aus dem Pears-Netzwerk geladen, ohne einen zentralen Server zu durchlaufen. Wenn Keet korrekt gestartet wird, ist Ihre Pears-Installation voll funktionsfähig.



Ihr macOS-System ist nun bereit, Peer-to-Peer-Anwendungen mit Pears auszuführen und zu hosten.



## 2. Wie verwende ich Plan ₿ Academy bei Birnen?



Sobald Pears installiert ist und läuft, können Sie die Plattform **Plan ₿ Academy** direkt über das P2P-Netzwerk ausführen. Führen Sie einfach den folgenden Befehl in Ihrem Terminal aus (es ist derselbe Befehl für Linux, Windows und macOS):



```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



![Image](assets/fr/13.webp)



Nach dem Hochladen wird Plan ₿ Academy in Ihrer Pears-Umgebung geöffnet und kann wie die ursprüngliche Website verwendet werden, jedoch ohne Abhängigkeit von einem zentralen Server.



![Image](assets/fr/14.webp)