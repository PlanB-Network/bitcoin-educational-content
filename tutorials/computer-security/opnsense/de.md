---
name: OPNsense
description: Wie kann ich eine OPNsense Firewall installieren und konfigurieren?
---
![cover](assets/cover.webp)



___



*Dieses Tutorial basiert auf Originalinhalten von Florian BURNEL, veröffentlicht auf [IT-Connect](https://www.it-connect.fr/). Lizenz [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Am Originaltext können Änderungen vorgenommen worden sein.*



___



## I. Präsentation



In diesem Tutorial werfen wir einen Blick auf die Open-Source-Firewall OPNsense. Wir werden uns die wichtigsten Funktionen, die Voraussetzungen und die Installation dieser FreeBSD-basierten Lösung ansehen.



Bevor Sie beginnen, sollten Sie wissen, dass **OPNsense und pfSense beides Open-Source-Firewalls** sind, die auf FreeBSD basieren. Man kann sagen, dass pfSense gewissermaßen der große Bruder von OPNsense ist, da letztere eine Fork ist, die 2015 entwickelt wurde. Schließlich ist es wichtig, darauf hinzuweisen, dass **OPNsense seit 2017 auf HardenedBSD anstelle von FreeBSD** umgestellt hat. HardenedBSD ist eine verbesserte Version von FreeBSD mit erweiterten Sicherheitsfunktionen



OPNsense zeichnet sich durch eine modernere Benutzer-Interface und eine **häufigere Update-Kadenz** aus. Der Aktualisierungsplan von OPNsense sieht in der Tat zwei Hauptversionen pro Jahr vor, die etwa alle zwei Wochen aktualisiert werden (was zu kleineren Versionen führt). Diese Folge ist im Vergleich zu pfSense sehr interessant, wenn wir uns die Community-Versionen dieser Lösungen ansehen.



![Image](assets/fr/050.webp)



## II. OPNsense Merkmale



OPNsense ist ein Betriebssystem, das als Firewall und Router fungiert, obwohl seine Funktionen zahlreich sind und durch die Installation von Zusatzpaketen erweitert werden können. Es eignet sich für den produktiven Einsatz und wird hauptsächlich für die Netzwerksicherheit und das Flussmanagement verwendet.



### A. Wichtigste Merkmale



Hier sind einige der wichtigsten Funktionen von OPNsense:





- Firewall und NAT**: OPNsense bietet fortschrittliche Stateful-Firewall-Funktionalität mit Stateful-Filterung sowie Network-Address-Translation (NAT)-Funktionen.





- DNS/DHCP**: OPNsense kann für die Verwaltung von DNS- und DHCP-Diensten im Netzwerk konfiguriert werden. Es kann als DHCP-Server fungieren, aber auch als DNS-Auflöser für Maschinen im lokalen Netzwerk verwendet werden. Dnsmasq ist ebenfalls standardmäßig integriert.





- VPN**: OPNsense unterstützt mehrere VPN-Protokolle, darunter IPsec, OpenVPN und WireGuard, und ermöglicht so sichere Verbindungen für den Fernzugriff auf mobile Workstations oder die Standortvernetzung.





- Web-Proxy**: OPNsense enthält einen Web-Proxy, um den Internetzugang zu kontrollieren und zu filtern. Er kann auch verwendet werden, um Inhalte zu filtern und den Netzwerkzugang zu verwalten.





- Bandbreitenverwaltung (QoS)**: OPNsense bietet Quality of Service (QoS) Management Funktionen, um den Netzwerkverkehr zu priorisieren und die Netzwerkbandbreite besser zu verwalten.





- Captive Portal**: Mit dieser Funktion können Sie den Benutzerzugang zum Netzwerk über eine Authentifizierungsseite (lokale Basis, Voucher usw.) verwalten. Diese Funktion wird häufig für öffentliche Wi-Fi-Netzwerke eingesetzt.





- IDS/IPS**: OPNsense integriert Suricata, um Intrusion Detection und Prevention (IDS/IPS) Funktionen zum Schutz des Netzwerks vor Angriffen anzubieten.





- Hohe Verfügbarkeit (CARP)**: OPNsense unterstützt CARP (*Common Address Redundancy Protocol*) für Hochverfügbarkeit zwischen mehreren OPNsense Firewalls und stellt sicher, dass der Dienst auch bei einem Hardwareausfall aktiv bleibt.





- Berichterstattung und Überwachung**: OPNsense bietet Echtzeit-Berichts- und Überwachungswerkzeuge, um die Netzwerkleistung (mit NetFlow) zu verfolgen und dank der Erstellung von Protokollen potenzielle Probleme zu erkennen. Dies schließt Grafiken ein. Das Monit-Tool ist in OPNsense integriert und ermöglicht die Überwachung der Firewall selbst.



### B. Zusätzliche Pakete



Dies ist nur ein Überblick über die von OPNsense angebotenen Funktionen. Darüber hinaus können Sie mit dem **Paketkatalog**, der über die OPNsense-Administration Interface zugänglich ist, die Firewall mit zusätzlichen Funktionalitäten **anreichern**. Dazu gehören ein ACME-Client, ein Wazuh-Agent, der NTP Chrony-Dienst und Caddy als Reverse-Proxy.



![Image](assets/fr/051.webp)



## III. OPNsense-Voraussetzungen



Als erstes müssen Sie entscheiden, wo Sie OPNsense installieren wollen. Es gibt mehrere mögliche Lösungen, einschließlich der Installation auf:





- Ein Hypervisor als virtuelle Maschine, sei es Hyper-V, Proxmox, VMware ESXi, etc.
- Eine Maschine als *Bare-Metal*-System. Dies könnte ein Mini-PC sein, der als Firewall fungiert.



Sie können auch **eine rack-montierbare OPNsense-Appliance** über unseren Online-Shop erwerben.



Sie müssen die für den Betrieb von OPNsense erforderlichen Hardware-Ressourcen berücksichtigen. Dies wird auf [dieser Dokumentationsseite] (https://docs.opnsense.org/manual/hardware.html) ausführlich beschrieben.



**Mindestausstattung und empfohlene Ressourcen für die Produktion:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Schließlich hängt der **Ressourcenbedarf vor allem von der Anzahl der zu verwaltenden Verbindungen** und damit vom **Bandbreitenbedarf** ab. Darüber hinaus müssen Sie **die Dienste berücksichtigen, die aktiviert und verwendet werden** (Proxy, Intrusion Detection usw.), da diese CPU- und/oder RAM-hungrig sein können.



Sie benötigen außerdem das OPNsense-Installations-ISO-Image, das Sie von [der offiziellen Website](https://opnsense.org/download/) herunterladen können. Für die Installation auf einer VM wählen Sie "**dvd**" als Image-Typ, um ein ISO-Image zu erhalten (und machen Sie damit, was Sie wollen...). Für die Installation über einen bootfähigen USB-Stick wählen Sie die Option "**vga**", um eine "**.img**"-Datei zu erhalten.



![Image](assets/fr/048.webp)



Außerdem benötigen Sie einen Computer für die Verwaltung und den Test von OPNsense.



## IV. Zielkonfiguration



Unser Ziel ist es





- Erstellen Sie ein internes virtuelles Netzwerk (192.168.10.0/24 - LAN)**, das über die OPNsense Firewall auf das Internet zugreifen kann. Für den Produktionseinsatz könnte dies Ihr lokales Netzwerk, Kabel und/oder Wi-Fi sein.
- Aktivieren und konfigurieren Sie NAT**, damit VMs im internen virtuellen Netzwerk auf das Internet zugreifen können
- Aktivieren und konfigurieren Sie den DHCP-Server auf OPNsense**, um eine IP-Konfiguration an zukünftige Maschinen zu verteilen, die mit dem internen virtuellen Netzwerk verbunden sind
- Konfigurieren Sie die Firewall** so, dass nur ausgehende LAN-zu-WAN-Flüsse in HTTP (80) und HTTPS (443) zugelassen werden.
- Konfigurieren Sie die Firewall** so, dass das virtuelle LAN OPNsense als DNS-Auflöser verwenden kann (53).



Wenn Sie die Hyper-V-Plattform verwenden, erhalten Sie die folgende Darstellung:



![Image](assets/fr/033.webp)



## V. Installation der OPNsense-Firewall



### A. Vorbereiten des bootfähigen USB-Sticks



Der erste Schritt ist die Vorbereitung des Installationsmediums: **den bootfähigen USB-Stick mit OPNsense**. Dies ist natürlich optional, wenn Sie in einer virtuellen Umgebung arbeiten, aber in jedem Fall müssen Sie das OPNsense-Installations-ISO-Image herunterladen.



Nach dem Herunterladen erhalten Sie **ein Archiv, das ein Abbild im Format ".img "** enthält. Sie können **mit verschiedenen Anwendungen einen bootfähigen USB-Stick** erstellen, darunter **balenaEtcher**: ultra-einfach zu bedienen. Darüber hinaus erkennt die Anwendung das Image im Archiv, so dass Sie es nicht vorher dekomprimieren müssen.





- [Download balenaEtcher](https://etcher.balena.io/)



Sobald die Anwendung installiert ist, wählen Sie Ihr Bild und Ihren USB-Stick aus und klicken Sie dann auf "Flash! Warten Sie einen Moment.



![Image](assets/fr/049.webp)



Jetzt sind Sie bereit für die Installation.



### B. Installieren des OPNsense Systems



Starten Sie den Rechner, auf dem OPNsense läuft. Sie sollten eine Begrüßungsseite ähnlich der untenstehenden sehen. Für ein paar Sekunden wird der gezeigte Bildschirm im Fenster zu sehen sein. Lassen Sie den Prozess seinen Lauf nehmen...



![Image](assets/fr/019.webp)



Das OPNsense-Image wird auf die Maschine geladen, so dass auf das System im "**Live**"-Modus zugegriffen werden kann, d.h. es wird vorübergehend im Speicher abgelegt.



![Image](assets/fr/025.webp)



Sie gelangen dann zu einer Interface-Seite, die der folgenden ähnelt. Melden Sie sich mit dem Login "**installer**" und dem Passwort "**opnsense**" an. Bitte beachten Sie, dass die Tastatur im Moment **QWERTY** ist. An diesem Punkt **starten wir den OPNsense-Installationsprozess**.



![Image](assets/fr/026.webp)



Ein neuer Assistent erscheint auf dem Bildschirm. Der erste Schritt besteht darin, das Tastaturlayout auszuwählen, das Ihrer Konfiguration entspricht. Wählen Sie für eine AZERTY-Tastatur die Option "**Französisch (Akzenttasten)**" aus der Liste und doppelklicken Sie dann auf**.



![Image](assets/fr/027.webp)



Der zweite Schritt besteht darin, die auszuführende Aufgabe auszuwählen. Hier werden wir eine Installation mit dem **ZFS-Dateisystem** durchführen. Stellen Sie sich auf die Zeile "**Install (ZFS)**" und bestätigen Sie mit **Eingabe**.



![Image](assets/fr/028.webp)



Im dritten Schritt wählen Sie "**Streifen**", da unser Rechner mit **nur einer Festplatte** ausgestattet ist: Es ist keine Redundanz möglich, um den Firewall-Speicher und seine Daten zu sichern. Dies ist besonders wichtig bei der Installation auf einem physischen Rechner, um sich gegen den Ausfall einer Festplatte durch das RAID-Prinzip zu schützen.



![Image](assets/fr/029.webp)



Im vierten Schritt drücken Sie einfach **Enter** zur Bestätigung.



![Image](assets/fr/030.webp)



Bestätigen Sie abschließend, indem Sie "**Ja**" auswählen und dann die Taste **Eingabe** drücken.



![Image](assets/fr/031.webp)



Jetzt müssen Sie warten, bis OPNsense installiert ist... Dieser Vorgang dauert etwa 5 Minuten.



![Image](assets/fr/032.webp)



Sobald die Installation abgeschlossen ist, können Sie das "**root**"-Passwort vor dem Neustart ändern. Wählen Sie "**Root-Passwort**", drücken Sie **Eingabe** und geben Sie das Passwort "**root**" zweimal ein.



![Image](assets/fr/020.webp)



Wählen Sie schließlich "**Installation abschließen**" und drücken Sie **Eingabe**. Werfen Sie bei dieser Gelegenheit **die Diskette aus dem DVD-Laufwerk der VM aus**. In den VM-Einstellungen können Sie auch den ersten Bootvorgang auf Festplatte festlegen.



![Image](assets/fr/021.webp)



Die virtuelle Maschine wird neu starten und das OPNsense-System von der Festplatte laden, da wir es gerade installiert haben. Melden Sie sich mit dem "root"-Konto in der Konsole und Ihrem neuen Passwort an (das Standardpasswort ist "**opnsense**").



### D. Verknüpfung von Netzwerkschnittstellen



Der unten gezeigte Bildschirm wird angezeigt. Wählen Sie "**1**" und drücken Sie **Enter**, um die Netzwerkkarten des Geräts mit den OPNsense-Schnittstellen zu verbinden.



![Image](assets/fr/022.webp)



Zunächst werden Sie vom Assistenten aufgefordert, Link Aggregation und VLANs zu konfigurieren. Geben Sie "**n**" an, um dies abzulehnen, und bestätigen Sie Ihre Antwort jedes Mal mit **Enter**. Als nächstes müssen Sie die beiden Schnittstellen "**hn0**" und "**hn1**" dem **WAN** und **LAN** zuweisen. Im Prinzip entspricht "**hn0**" dem WAN und die andere Interface dem LAN.



Und so funktioniert es:



![Image](assets/fr/023.webp)



Wir haben jetzt:





- Das Interface **LAN**, das mit der Netzwerkkarte "**hn1**" und mit der OPNsense-Standard-IP Address, d. h. **192.168.1.1/24**, verbunden ist.
- Der Interface **WAN**, der mit der Netzwerkkarte "**hn0**" verbunden ist, und mit einer IP Address, die über **DHCP** im lokalen Netzwerk abgerufen wird (dank unseres externen virtuellen Switches).



Standardmäßig ist der OPNsense-Administrations-Interface aus offensichtlichen Sicherheitsgründen nur über den LAN-Interface zugänglich. Sie müssen sich daher mit dem LAN Interface der Firewall verbinden, um die Administration durchzuführen. Wenn dies nicht möglich ist, können Sie OPNsense vorübergehend über das WAN administrieren. Dazu müssen Sie die Firewall-Funktion deaktivieren.



Wechseln Sie dazu mit der Option "**8**" in den Shell-Modus und führen Sie den folgenden Befehl aus:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Zugang zum OPNsense Interface Managementsystem



Auf die OPNsense Administration Interface kann über HTTPS zugegriffen werden, wobei die IP Address des LAN** Interface (oder des WAN) verwendet wird. Ihr Browser führt Sie zu einer Anmeldeseite. Melden Sie sich mit dem "root"-Konto und dem Passwort an, das Sie zuvor ausgewählt haben.



![Image](assets/fr/034.webp)



Warten Sie ein paar Sekunden... Sie werden aufgefordert, einem Assistenten zu folgen, um die Grundkonfiguration durchzuführen. Klicken Sie auf "**Weiter**", um fortzufahren.



![Image](assets/fr/036.webp)



Der erste Schritt besteht darin, den Hostnamen und den Domänennamen zu definieren, die Sprache zu wählen und den/die DNS-Server festzulegen, die für die Namensauflösung verwendet werden sollen. Wenn Sie die Option "**Auflöser** aktivieren" beibehalten, kann die Firewall als DNS-Auflöser verwendet werden, was für die Maschinen in unserem virtuellen LAN nützlich ist.



![Image](assets/fr/037.webp)



Fahren Sie mit dem nächsten Schritt fort. Der Assistent bietet Ihnen die Möglichkeit, **einen NTP-Server für die Datums- und Zeitsynchronisation** zu definieren, obwohl standardmäßig bereits Server konfiguriert sind. Außerdem müssen Sie unbedingt die Zeitzone auswählen, die Ihrem geografischen Standort entspricht (es sei denn, Sie haben besondere Anforderungen).



![Image](assets/fr/038.webp)



Dann kommt ein wichtiger Schritt: **Konfiguration des Interface WAN**. Derzeit ist es mit DHCP konfiguriert und wird in diesem Konfigurationsmodus bleiben, es sei denn, Sie möchten eine statische IP Address einstellen.



![Image](assets/fr/039.webp)



Auf der Interface-WAN-Konfigurationsseite müssen Sie die Option "**Zugang zu privaten Netzwerken über WAN** blockieren" deaktivieren, wenn das Netzwerk auf der WAN-Seite eine private Adressierung verwendet. Dies wird wahrscheinlich der Fall sein, wenn Sie ein Labor betreiben, und kann Sie daran hindern, auf das Internet zuzugreifen.



![Image](assets/fr/040.webp)



Als Nächstes können Sie ein **Passwort für "root "** festlegen, aber das ist optional, da wir das bereits getan haben.



![Image](assets/fr/041.webp)



Fahren Sie bis zum Ende fort, um das Neuladen der Konfiguration einzuleiten. Wenn Sie die Steuerung über das WAN fortsetzen müssen, starten Sie den obigen Befehl erneut, sobald dieser Vorgang abgeschlossen ist.



![Image](assets/fr/042.webp)



Das ist alles, was es zu sagen gibt!



![Image](assets/fr/035.webp)



### E. DHCP-Konfiguration



Unser Ziel ist es, den OPNsense DHCP-Server für die Verteilung von IP-Adressen im virtuellen LAN zu verwenden. Zu diesem Zweck müssen wir auf diesen Menüpunkt zugreifen:



```
Services > ISC DHCPv4 > [LAN]
```



**Wie Sie sehen können, ist DHCP bereits standardmäßig im LAN aktiviert ** Wenn Sie an diesem Dienst nicht interessiert sind, sollten Sie ihn deaktivieren. Auch wenn er bereits aktiviert ist und wir ihn nutzen wollen, ist es wichtig, seine Konfiguration zu überprüfen.



Falls erforderlich, können Sie den Bereich der zu verteilenden IP-Adressen ändern: **192.168.10.10** bis **192.168.10.245**, je nach den aktuellen Einstellungen.



![Image](assets/fr/046.webp)



Wir können auch sehen, dass die Felder "**DNS-Server**", "**Gateway**", "**Domänenname**" usw. standardmäßig leer sind. Tatsächlich gibt es eine automatische Vererbung bestimmter Optionen und Standardwerte für diese verschiedenen Felder. Zum Beispiel wird für den DNS-Server die IP Address des Interface LAN verteilt, so dass die OPNsense-Firewall als DNS-Auflöser verwendet werden kann.



Speichern Sie die Konfiguration, nachdem Sie Änderungen vorgenommen haben, falls erforderlich.



![Image](assets/fr/047.webp)



Um den DHCP-Server zu testen, müssen Sie einen Rechner mit dem LAN-Netzwerk Ihrer Firewall verbinden.



Dieser Rechner muss eine IP Address vom OPNsense DHCP-Server erhalten, und unser Rechner muss Zugang zum Netzwerk haben. Der Internetzugang muss funktionieren. Bitte beachten Sie, dass, wenn Sie die Firewall-Funktion für den Zugriff auf OPNsense vom WAN aus deaktiviert haben, dies NAT deaktiviert und den Zugriff auf das Web verhindert.



**Hinweis**: Die aktuell ausgegebenen DHCP-Leases sind in der OPNsense Administration Interface sichtbar. Gehen Sie dazu zu folgendem Ort: **Dienste > ISC DHCPv4 > Leases**.



![Image](assets/fr/045.webp)



### F. NAT und Firewall-Regeln konfigurieren



Die gute Nachricht ist, dass wir nun vom LAN aus auf die OPNsense-Administration Interface zugreifen können.



```
https://192.168.1.10
```



Nachdem Sie sich bei OPNsense angemeldet haben, lassen Sie uns die NAT-Konfiguration ermitteln. Gehen Sie zu diesem Ort: **Firewall > NAT > Ausgehend**. Hier können Sie zwischen automatischer (Standard) und manueller Erstellung von NAT-Regeln für ausgehende Verbindungen wählen.



Wählen Sie den automatischen Modus über die Option "**Automatische Generierung von ausgehenden NAT-Regeln**" und klicken Sie auf "**Speichern**" (im Prinzip ist diese Konfiguration bereits die aktive). Im automatischen Modus erstellt OPNsense selbst eine NAT-Regel für jedes Ihrer Netzwerke.



![Image](assets/fr/043.webp)



Vorerst können alle Computer, die mit dem virtuellen LAN "**192.168.10.0/24**" verbunden sind, ohne Einschränkung auf das Internet zugreifen. Unser Ziel ist es jedoch, den Zugang zum WAN auf HTTP- und HTTPS-Protokolle sowie DNS im Interface-LAN der Firewall zu beschränken.



Wir müssen also Firewall-Regeln erstellen... Navigieren Sie wie folgt durch das Menü: **Firewall > Regeln > LAN**.



**Standardmäßig gibt es zwei Regeln, um den gesamten ausgehenden LAN-Verkehr in IPv4 und IPv6 zuzulassen**. Deaktivieren Sie diese beiden Regeln, indem Sie auf den Pfeil Green ganz links, am Anfang jeder Zeile, klicken.



Erstellen Sie dann drei neue Regeln, um das **LAN-Netz** (d.h. "**LAN net**") zu autorisieren,:





- zugang zu allen Zielen über **HTTP**.
- zugang zu allen Zielen mit **HTTPS**.
- **OPNsense** auf seinem **Interface LAN** (d.h. "**LAN Address**") über das **DNS-Protokoll** anfordern (dies impliziert die Verwendung der Firewall als DNS), ansonsten Ihren DNS-Resolver über seine IP Address autorisieren.



Daraus ergibt sich das folgende Ergebnis:



![Image](assets/fr/044.webp)



Nun müssen Sie nur noch auf "**Änderungen übernehmen**" klicken, um die neuen Firewall-Regeln in die Produktion zu übernehmen. **Bitte beachten Sie, dass alle Ströme, die nicht ausdrücklich autorisiert sind, standardmäßig blockiert werden



Der LAN-Rechner kann über HTTP und HTTPS auf das Internet zugreifen. Alle anderen Protokolle werden blockiert.



![Image](assets/fr/018.webp)



## IV. Schlussfolgerung



Wenn Sie diese Anleitung befolgen, können Sie OPNsense installieren und sofort loslegen. OPNsense bietet eine Vielzahl von Funktionen, um Ihren Netzwerkverkehr effizient zu sichern und zu verwalten und ist für den Einsatz in professionellen Umgebungen geeignet.



Diese Installation ist nur der Anfang: erkunden Sie die Menüs und konfigurieren Sie weitere Funktionen, um OPNsense an Ihre Bedürfnisse anzupassen.