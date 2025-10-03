---
name: Cryptomator
description: Verschlüsseln Sie Ihre Dateien in der Cloud
---
![cover](assets/cover.webp)



___



*Dieses Tutorial basiert auf Originalinhalten von Florian BURNEL, veröffentlicht auf [IT-Connect](https://www.it-connect.fr/). Lizenz [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Am Originaltext können Änderungen vorgenommen worden sein.*



___



## I. Präsentation



In diesem Tutorial werden wir die Cryptomator-Anwendung verwenden, um Daten zu verschlüsseln, die in der Cloud gespeichert sind, sei es auf Microsoft OneDrive, Google Drive, Dropbox, Box oder sogar iCloud.



Die Verschlüsselung der Daten, die Sie auf Online-Speicherlösungen wie Drive speichern, ist der beste Weg, um Ihre Dateien und Ihre Privatsphäre zu schützen. Dank der Verschlüsselung sind Sie der Einzige, der Ihre Daten entschlüsseln und lesen kann, auch wenn sie auf einem Server in den USA oder einem anderen Land auf der ganzen Welt gespeichert sind.



In dieser Demonstration wird ein Windows 11 22H2-Rechner mit OneDrive verwendet, aber das Verfahren ist für andere Windows-Versionen und andere Speicherdienste identisch. Alles, was Sie tun müssen, ist, den Synchronisations-Client zu installieren und Ihr Konto hinzuzufügen. Dadurch wird Cryptomator in die Lage versetzt, seine Daten im Tresor zu speichern.



![Image](assets/fr/020.webp)



Cryptomator ist eine Alternative zu anderen Anwendungen, insbesondere zu dem in einem anderen Artikel vorgestellten Picocrypt, das zwar anders aussieht, aber ebenso einfach zu bedienen ist. Cryptomator ist außerdem **Open Source**, RGPD-konform und verschlüsselt **Daten mit dem AES-256-Bit-Verschlüsselungsalgorithmus**. Im Gegensatz dazu setzt Picocrypt auf den schnelleren XChaCha20-Algorithmus (ebenfalls 256-Bit).



https://planb.network/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

Die Cryptomator-Anwendung ist verfügbar für **Windows** (exe / msi), **Linux**, **macOS,** aber auch **Android** und **iOS**. Übrigens sind alle Anwendungen kostenlos, außer der Android-Anwendung, für die Sie bezahlen müssen (14,99 Euro).



Auf Ihrem Rechner erstellt **Cryptomator einen Ordner, in dem es einen Tresor** erstellt. Innerhalb des Tresors, der auf Ihrem OneDrive, Google Drive oder ähnlichem gespeichert sein kann, werden Ihre Daten verschlüsselt. Wenn Sie also alle Ihre Daten in dem Tresor auf Ihrem Drive-Speicherplatz speichern, sind sie geschützt (weil sie verschlüsselt sind).



**Anmerkung**: In diesem Artikel werden Online-Speicherdienste als Beispiel verwendet, aber Cryptomator kann zur Verschlüsselung von Daten auf einer lokalen Festplatte, einer externen Festplatte oder sogar einem NAS verwendet werden. Es gibt eigentlich keine Einschränkungen.



## II. Installation von Cryptomator



Um loszulegen, müssen Sie **Cryptomator** **herunterladen** und **installieren**. Sobald der Download abgeschlossen ist, genügen ein paar Klicks, um die Installation abzuschließen. Wie [Rclone] (https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/), verlässt sich Cryptomator auf WinFsp, um **ein virtuelles Laufwerk auf Ihrem Windows-Rechner** einzurichten.





- [Cryptomator von der offiziellen Website herunterladen](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III. Verwendung von Cryptomator unter Windows



### A. Erstellen Sie einen neuen Safe



Um einen neuen Safe zu erstellen, klicken Sie auf die Schaltfläche "**Hinzufügen**" und wählen Sie "**Neuer Safe...**". Ihre bestehenden und bekannten Tresore auf diesem Rechner werden dann in Interface auf der linken Seite angezeigt. **Ein auf Rechner A erstellter Tresor kann auf Rechner B** geöffnet und verändert werden, sofern dieser mit Cryptomator ausgestattet ist (und der Verschlüsselungsschlüssel bekannt ist).



![Image](assets/fr/015.webp)



Geben Sie dem Tresor zunächst einen Namen, z. B. "**IT-Connect**". Dadurch wird in meinem OneDrive ein Verzeichnis mit dem Namen "**IT-Connect**" erstellt.



![Image](assets/fr/011.webp)



Im nächsten Schritt wird Cryptomator wahrscheinlich **das auf Ihrem Rechner vorhandene "Laufwerk "** erkennen: Google Drive, OneDrive, Dropbox, etc.... Damit Sie den Anbieter direkt auswählen können. Ich habe dies auf zwei verschiedenen Windows 11-Rechnern mit verschiedenen Laufwerken ausprobiert, und es wurde nicht erkannt. Das ist kein Problem, definieren Sie einfach einen "**Benutzerdefinierten Speicherort**" und wählen Sie das Stammverzeichnis Ihres Speicherplatzes. Zum Beispiel: **C:\Users\<Benutzername>\OneDrive**.



![Image](assets/fr/018.webp)



Als nächstes können Sie eine Option in den Experteneinstellungen anpassen.



![Image](assets/fr/021.webp)



Als nächstes müssen Sie ein **Passwort für den Verschlüsselungscode** festlegen. Mit diesem Passwort können Sie Ihren Cryptomator-Tresor **entriegeln** und auf seine Daten zugreifen. **Wenn Sie es verlieren, verlieren Sie den Zugang zu Ihren Daten**. Schließlich haben Sie noch die Möglichkeit, einen **Backup-Schlüssel** zu erstellen, indem Sie die Option **Ja, sicher ist sicher**" ankreuzen, ganz im Sinne des [BitLocker]-Wiederherstellungsschlüssels (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). Dies ist ratsam, aber speichern Sie diesen Sicherungsschlüssel nicht im Stammverzeichnis Ihres OneDrive!



Klicken Sie auf "**Safe erstellen**".



![Image](assets/fr/019.webp)



Kopieren Sie den Wiederherstellungsschlüssel und speichern Sie ihn in Ihrem bevorzugten Passwortmanager. Klicken Sie auf "**Weiter**".



![Image](assets/fr/013.webp)



Das war's, Ihr neuer Kofferraum ist erstellt und einsatzbereit!



![Image](assets/fr/014.webp)



### B. Zugangszahlen



Um auf einen Safe und seine Daten zuzugreifen, entweder um **vorhandene Daten zu lesen oder neue Daten hinzuzufügen**, müssen Sie ihn **entsperren**. Cryptomator listet die bekannten Tresore auf: der IT-Connect-Tresor erscheint, wählen Sie ihn einfach aus und klicken Sie auf "**Entsperren**".



![Image](assets/fr/016.webp)



Sie müssen Ihr Passwort eingeben, um den Safe zu entsperren. Klicken Sie dann auf "**Laufwerk freigeben**".



![Image](assets/fr/022.webp)



**Ihr Safe wird auf dem Windows-Rechner als virtuelles Laufwerk gemountet.** Über dieses Laufwerk, das hier den Buchstaben E trägt, haben Sie Zugriff auf Ihre Daten (im Klartext, da der Safe entsperrt ist).



![Image](assets/fr/017.webp)



Auf der OneDrive-Seite können wir den Cryptomator-Datenspeicher nicht direkt durchsuchen. Wir können die Daten nicht sehen (weder die Dateinamen noch den Inhalt). Das bedeutet, dass Sie Ihre Daten nicht über die übliche OneDrive-Verknüpfung zu Ihrem Cryptomator-Tresor hinzufügen müssen. **Sie müssen Ihre Daten über das virtuelle Laufwerk von Cryptomator hinzufügen.**



![Image](assets/fr/012.webp)



### C. Trunk-Optionen



Die Einstellungen des Tresors werden über die Schaltfläche "**Optionen für verschlüsselte Datenträger**" (im gesperrten Zustand) aufgerufen und ermöglichen das automatische Sperren bei Inaktivität, genau wie bei Ihrem Passwort-Safe. Die Option "**Verschlüsseltes Volume beim Start entsperren**" hebt, wie der Name schon sagt, die Sperre des Laufwerks ohne Ihr Zutun auf und bindet das virtuelle Laufwerk ein. Aus Sicherheitsgründen ist es am besten, diese Option nicht zu aktivieren.



Über die Registerkarte "**Mounting**" können Sie auch entscheiden, ob Sie die Datei schreibgeschützt mounten oder einen bestimmten Buchstaben zuweisen möchten.



![Image](assets/fr/024.webp)



Außerdem können Sie in den Cryptomator-Einstellungen **den automatischen Start der Anwendung aktivieren**.



## IV. Schlussfolgerung



Mit **Cryptomator** können Sie **in wenigen Minuten einen verschlüsselten Safe** erstellen, um die Daten zu schützen, die Sie auf OneDrive und Konsorten speichern möchten. Es ist sehr einfach zu bedienen, wenn es darum geht, es mit einem Laufwerk zu "koppeln": zu diesem Zweck hat es meine Präferenz gegenüber Picocrypt.