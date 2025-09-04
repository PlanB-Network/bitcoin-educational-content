---
name: Whonix
description: Ihre Privatsphäre und Vertraulichkeit zu wahren.
---

![cover](assets/cover.webp)



**Whonix** ist eine Linux-Distribution, die auf **Debian** basiert und entwickelt wurde, um eine Umgebung zu schaffen, die **Sicherheit**, **Anonymität** und **Privatsphäre** kombiniert. Sie ist leicht zu erlernen und mit verschiedenen Schnittstellen kompatibel (virtuelle Maschinen, Qubes OS, Live-Modus). Sie beinhaltet standardmäßig die Weiterleitung des Netzwerkverkehrs über **Tor**, eine **doppelte Firewall** (eine Firewall auf dem Gateway und eine weitere auf der Workstation), einen **vollständigen Schutz gegen IP/DNS-Lecks** und Werkzeuge, um Ihre Aktivitäten effektiv vor Netzwerkbeobachtern, einschließlich Ihres ISP, zu verbergen. Mehr als nur ein anonymes System, **Whonix** ist eine komplett sichere Entwicklungsumgebung.



## Warum Whonix wählen?





- Frei**: Wie die meisten Linux-Distributionen ist Whonix ein Open-Source-System, das völlig kostenlos lizenziert ist. Es wird als Open-Source-System entwickelt, mit einer aktiven und transparenten Gemeinschaft.
- Privatsphäre, Sicherheit und Anonymität**: Das Hauptziel von Whonix ist es, eine ultra-sichere Umgebung zu bieten, in der alle deine Daten geschützt sind und deine Kommunikation über das Tor-Netzwerk verschlüsselt wird.
- Einfach zu bedienen**: Whonix bietet eine intuitive, vorkonfigurierte grafische Interface, die auch für unerfahrene Benutzer geeignet ist. Man muss kein Experte sein, um von dem erweiterten Schutz zu profitieren.
- Ideale Umgebung für sichere Entwicklung**: Mit Whonix können Sie Programme entwickeln, testen, prüfen oder ausführen, ohne jemals Ihre echte IP Address preiszugeben oder Ihre Surf- oder Kommunikationsgewohnheiten im Netz preiszugeben.
- Wegwerf-Sitzungen und Live-Modus**: Whonix kann im Live-Modus oder über Einwegrechner (z. B. über **Qubes OS**) gestartet werden, so dass kritische Aufgaben ausgeführt werden können, ohne nach Beendigung der Sitzung dauerhafte Spuren zu hinterlassen.
- Relativ einfache Installation**: Für die schnelle Installation in virtuellen Maschinen (VirtualBox, KVM, Qubes) werden gebrauchsfertige Images geliefert. Das System ist dokumentiert und wird regelmäßig aktualisiert.



## Installation und Konfiguration



Bevor wir zur Installation von Whonix kommen, ist es wichtig zu wissen, dass diese Distribution **noch nicht offiziell als Hauptsystem** verfügbar ist, das direkt auf der Hard-Platte (im Bare-Metal-Modus) installiert werden kann. Mit anderen Worten, Sie **können Whonix noch nicht als klassisches Host-Betriebssystem**, wie Ubuntu oder Standard-Debian, installieren.



Es stehen jedoch mehrere Editionen zur Verfügung, mit denen Whonix **flüchtig** (Live-Modus, temporäre Sitzungen) oder **persistent** (über virtuelle Maschinen oder Integration in Qubes OS) genutzt werden kann.



Für eine langfristige, stabile Nutzung ist **Virtualisierung derzeit die einzige offiziell empfohlene Methode**. Sie können Whonix mit **VirtualBox** (Whonix-Gateway und Whonix-Workstation) betreiben oder es in ein System wie **Qubes OS** integrieren. In diesem Tutorial konzentrieren wir uns auf eine VirtualBox-Installation.



### Voraussetzungen



Bevor Sie Whonix im virtuellen Modus installieren können, müssen Sie sicherstellen, dass Ihr Computer die technischen Mindestanforderungen erfüllt. Die Virtualisierung erfordert bestimmte Ressourcen, die nicht alle Computer bieten können. Es ist daher wichtig, dass Ihr Prozessor die Virtualisierungstechnologie (Intel VT-x oder AMD-V) unterstützt und dass diese Option im BIOS/UEFI aktiviert ist.



Hier sind die empfohlenen Spezifikationen für eine reibungslose und stabile Erfahrung mit Whonix:





- Arbeitsspeicher mit wahlfreiem Zugriff (RAM)**: Ein Minimum von **8 GB** wird dringend empfohlen. Je mehr RAM Sie haben, desto mehr Ressourcen können Sie den virtuellen Maschinen (Gateway und Workstation) zuweisen, was die Leistung verbessert.
- Verfügbarer Festplattenspeicher**: Bitte planen Sie mindestens 30 GB freien Festplattenspeicher** ein. Dies umfasst den für die beiden virtuellen Maschinen, die Systemdateien und alle Daten oder Snapshots benötigten Speicherplatz.
- Prozessor**: Ein Prozessor mit mindestens **4 physischen Kernen** (8 logischen Threads) wird empfohlen, insbesondere wenn Sie andere Dienste oder Tools parallel ausführen möchten.



### Whonix herunterladen



Whonix ist in verschiedenen Editionen erhältlich, je nach der Art der Umgebung, in der Sie es verwenden möchten. Für die meisten Benutzer (Windows, Linux oder MacOs) ist die VirtualBox-Edition am einfachsten einzurichten. Sie können das Image direkt von [der offiziellen Website](https://www.whonix.org/wiki/VirtualBox) herunterladen.



⚠️ Whonix **ist nicht kompatibel** mit MacBooks mit Apple Silicon Prozessoren (ARM-Architektur).



## Installation von VirtualBox



Um Whonix auszuführen, benötigen Sie einen **Hypervisor** wie VirtualBox, Qubes oder KVM.



Sobald Sie die Datei heruntergeladen haben, installieren Sie sie wie jede andere Software. Akzeptieren Sie die Standardoptionen, sofern Sie keine besonderen Anforderungen haben. Sie wissen nicht weiter? Schauen Sie sich unseren Leitfaden zur Verwendung von VirtualBox an.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Whonix importieren



Nach der Installation von VirtualBox können Sie die Whonix-.ova-Dateien importieren, die Sie zuvor heruntergeladen haben (`Whonix-Gateway-Xfce.ova` und `Whonix-Workstation-Xfce.ova`).



Öffnen Sie VirtualBox und klicken Sie dann auf **Datei → Appliance importieren**.


Wählen Sie die entsprechende `.ova'-Datei aus (beginnen Sie mit dem Gateway).



![0_03](assets/fr/03.webp)



Wählen Sie den Ort, an dem die Dateien der virtuellen Whonix-Maschine gespeichert werden sollen.



![0_04](assets/fr/04.webp)



Akzeptieren Sie die Nutzungsbedingungen, starten Sie dann den Import und warten Sie, bis der Vorgang abgeschlossen ist.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Whonix-Konfiguration



Bevor Sie Whonix starten, sollten Sie einige **Systemeinstellungen** vornehmen, um eine bessere Leistung zu gewährleisten:



Wählen Sie die virtuelle Maschine **Whonix-Workstation-Xfce** aus und klicken Sie dann auf **Konfiguration**.



![0_06](assets/fr/07.webp)



Gehen Sie auf die Registerkarte **System**, wo die Standard-RAM-Zuweisung 2048 MB beträgt. Wir empfehlen, dass du **den Arbeitsspeicher auf 4096 MB (4 GB)** erhöhst, um eine flüssigere Arbeitsweise zu erreichen, besonders wenn du mehrere Anwendungen öffnen oder in langen Sitzungen arbeiten willst. Das Gateway kann bei 2048 MB bleiben, es sei denn, du verwendest viele Tor-Verbindungen parallel.



![0_08](assets/fr/08.webp)



### Erste Schritte mit Whonix



Damit Whonix ordnungsgemäß und sicher funktioniert, **müssen Sie diese Startsequenz** einhalten:



Starten Sie zunächst den **Whonix-Gateway-Xfce** Rechner. Dieser Rechner ist dafür verantwortlich, den gesamten Verkehr durch das **Tor**-Netzwerk zu leiten. Wenn das Gateway nicht läuft, wird kein Verkehr über Tor geleitet und du verlierst die Anonymität.



![0_09](assets/fr/09.webp)



Sobald das Gateway vollständig gestartet ist (du wirst sehen, dass Tor verbunden ist), kannst du **Whonix-Workstation-Xfce** starten, das sich automatisch über das Gateway verbindet.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Aktualisierung des Systems



Geben Sie im Terminal den folgenden Befehl ein, um die Liste der Pakete zu aktualisieren:



```shell
sudo apt update
```



Führen Sie dann den folgenden Befehl aus, um die verfügbaren Updates zu installieren:



```shell
sudo apt full-upgrade
```



## Whonix entdecken



**Whonix** ist ein System, das eine **sichere**, **anonyme** und **vertrauliche** Computerumgebung bietet, ideal zum Surfen im Internet, ohne Ihre Identität oder Ihre Daten zu gefährden. Um dies zu erreichen, wird es mit einer Reihe von nützlichen, alltäglichen Anwendungen geliefert, die Ihre digitale Sicherheit von Anfang an verstärken.


### KeepassXC



**KeePassXC** ist der integrierte Passwortmanager von Whonix. Mit ihm können Sie Ihre Passwörter **erstellen, speichern und sicher verwalten**, ohne sie sich alle manuell merken zu müssen. Die Passwörter werden in einer **verschlüsselten Datenbank** gespeichert und durch ein Master-Passwort geschützt.



### Tor-Browser



*der *Tor Browser** ist der Standard-Webbrowser von Whonix. Er stützt sich auf das **Tor**-Netzwerk, das Ihren Datenverkehr über mehrere Relais auf der ganzen Welt umleitet, so dass es praktisch unmöglich ist, Ihre tatsächliche IP Address zu ermitteln.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Elektrum Bitcoin Wallet



**Electrum** ist ein leichter und schneller Bitcoin Wallet, der auf Whonix vorinstalliert ist, damit Sie **Kryptowährungstransaktionen** anonym verwalten können. Es lädt nicht den gesamten Blockchain herunter, sondern nutzt entfernte Server, um die notwendigen Informationen zu erhalten, was es viel leichter macht als einen vollständigen Wallet.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix ist mehr als nur ein Betriebssystem: Es ist eine echte **sichere Umgebung**, die entwickelt wurde, um deine Anonymität, deine Privatsphäre und deine sensiblen Aktivitäten zu schützen. Dank seiner Tor-basierten Architektur, der intelligenten Partitionierung zwischen Gateway und Workstation und den vorinstallierten Tools wie Tor Browser, KeePassXC und Electrum bietet es eine schlüsselfertige Lösung für jeden, der **anonym surfen**, **sicher arbeiten** oder **vertrauliche Daten** verwalten möchte.



Um die Sicherheit Ihres Unix-Systems zu erhöhen, schauen Sie sich unsere Anleitung zur Überprüfung Ihres Rechners an: Suchen Sie nach Sicherheitslücken in Ihrem Betriebssystem und stellen Sie sicher, dass Ihre Daten nicht gefährdet sind.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af