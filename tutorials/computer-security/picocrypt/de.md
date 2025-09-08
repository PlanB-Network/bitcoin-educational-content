---
name: Picocrypt
description: Ein Open-Source-Tool zum Verschlüsseln Ihrer Daten
---
![cover](assets/cover.webp)



___



*Dieses Tutorial basiert auf Originalinhalten von Florian BURNEL, veröffentlicht auf [IT-Connect](https://www.it-connect.fr/). Lizenz [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Es wurden Änderungen am Originalinhalt vorgenommen.*



___



## I. Präsentation



In diesem Tutorial werfen wir einen Blick auf Picocrypt, eine einfache, leichtgewichtige und effektive Verschlüsselungssoftware zum Verschlüsseln von Daten mit einem hohen Maß an Sicherheit.



Geeignet zum **Verschlüsseln von Dateien**, können Sie es zum Schutz von **Daten auf Ihrem Computer, auf einem USB-Stick**, aber auch von Daten in der Cloud verwenden. Zum Beispiel können Sie Daten verschlüsseln und auf **Microsoft OneDrive, Google Drive, iCloud oder Dropbox** speichern, obwohl ich für diesen Zweck eine andere Software bevorzuge, die in einem zukünftigen Artikel vorgestellt wird.



Sie können es auch verwenden, wenn Sie **Daten mit Dritten** teilen müssen: Dank Picocrypt und dem Entschlüsselungsschlüssel können diese die Daten auf ihrem Rechner entschlüsseln. Wenn also Ihr Konto oder Ihr Computer kompromittiert wird, sind Ihre Daten geschützt.



Um das Picocrypt-Projekt zu verfolgen, gibt es nur einen Address:





- [Picocrypt auf GitHub](https://github.com/Picocrypt/Picocrypt)



PicoCrypt ist völlig **kostenlos und quelloffen** und für **Windows**, **Linux** und **macOS** erhältlich. Unter Windows können Sie es auf Ihrem eigenen Rechner installieren oder die portable Version verwenden.



## II. Picocrypt, Open-Source-Verschlüsselungssoftware



Die Verschlüsselungssoftware Picocrypt** präsentiert sich als **Alternative** zu anderen bekannten Lösungen wie **VeraCrypt** und **Cryptomator** (*zur Verschlüsselung von Daten in Cloud-Umgebungen*), oder **AxCrypt**. Übrigens, auf dem offiziellen GitHub von Picocrypt finden Sie einen Vergleich mit einigen Konkurrenten:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Quelle: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt ist **sehr leichtgewichtig**, wiegt nur **3 MB** und muss nicht installiert werden: es ist eine **portable Anwendung** mit dem Vorteil, dass keine Administratorrechte erforderlich sind! Dennoch vernachlässigt es die Sicherheit nicht, da es sich auf **robuste und zuverlässige Algorithmen** stützt:





- XChaCha20** Verschlüsselungsalgorithmus
- Tastenumgehungsfunktion **Argon2**



Neben den bereits erwähnten Vorteilen ist es vor allem die **einfache Handhabung**, die überzeugt!



Es fehlt nur noch eine Sache: **ein Code-Audit**, aber das ist geplant, wie Sie in der Vergleichstabelle oben (letzte Zeile) sehen können. Aber da es Open Source ist, spricht nichts dagegen, einen Blick in den Quellcode zu werfen.



Auch wenn es in der obigen Tabelle mit BitLocker verglichen wird, **sind BitLocker und Picocrypt meiner Meinung nach für unterschiedliche Zwecke gedacht**: BitLocker für die Verschlüsselung eines kompletten Datenträgers (z. B. von Windows) und Picocrypt für die Verschlüsselung einer Baumstruktur oder eines "Drive"-Speicherplatzes.



## III. Verwendung von Picocrypt



Für diese Demonstration wird ein Windows 11 Rechner verwendet.



### A. Verschlüsselung von Daten mit Picocrypt



Zunächst müssen Sie Picocrypt.exe vom offiziellen GitHub herunterladen ([siehe diese Seite](https://github.com/Picocrypt/Picocrypt/releases)).



Öffnen Sie die Anwendung, um ihren minimalistischen Interface auf dem Bildschirm anzuzeigen. Um Daten zu verschlüsseln, sei es **eine Datei, mehrere Dateien oder ein Ordner**, ziehen Sie sie einfach **in den Interface von Picocrypt** und legen sie dort ab. Dadurch werden die zu verschlüsselnden Daten ausgewählt.



![Image](assets/fr/020.webp)



Für die Verschlüsselung der Daten stehen Ihnen mehrere Optionen zur Verfügung, darunter der Verschlüsselungscode. Dies kann **ein sicheres Passwort** oder **ein Verschlüsselungsschlüssel in Form einer Schlüsseldatei** oder **beides** sein. Nehmen wir das Beispiel eines Passworts: Sie haben die Wahl zwischen der Erstellung Ihres eigenen Passworts oder der Generierung eines Passworts mit Picocrypt.



Dieses Passwort muss stark sein, da es zur Entschlüsselung der Daten verwendet werden kann. Geben Sie es unter "**Passwort**" und "**Passwort bestätigen**" ein, und klicken Sie dann auf "**Verschlüsseln**", um die Daten zu verschlüsseln! Zuvor können Sie auf die Schaltfläche "**Ändern**" neben "**Ausgabe speichern unter**" klicken, um das Ausgabeverzeichnis anzugeben.



**Hinweis**: Um einen Schlüssel im Dateiformat zu verwenden, klicken Sie auf "**Erstellen**" rechts neben "**Schlüsseldateien**", um einen Schlüssel zu erstellen. Wählen Sie ihn dann aus, indem Sie auf "**Bearbeiten**" klicken und die Schlüsseldatei per Drag-and-Drop in den entsprechenden Bereich ziehen.



![Image](assets/fr/019.webp)



Die beiden ausgewählten Dateien werden **verschlüsselt und in der Datei "**Encrypted.zip.pcv**" zusammengefasst, da **PCV** die von Picocrypt verwendete Erweiterung ist. Diese ZIP-Datei ist dank der Verschlüsselung unlesbar. Um zu verhindern, dass ausgewählte Dateien in einer einzigen verschlüsselten ZIP-Datei zusammengefasst werden, müssen Sie die Option "**Rekursiv**" aktivieren, damit so viele Dateien verschlüsselt werden, wie es Dateien gibt, die verschlüsselt werden sollen.



Um auf unsere Daten zuzugreifen, müssen wir sie mit Picocrypt entschlüsseln.



![Image](assets/fr/023.webp)



Bevor wir über die Entschlüsselung von Daten sprechen, hier einige Informationen über einige der verfügbaren Optionen:





- Paranoid-Modus**: Verwenden Sie die höchste von Picocrypt angebotene Sicherheitsstufe. Das Tool verwendet mehrere kaskadierende Verschlüsselungsalgorithmen (XChaCha20 und Serpent) und HMAC-SHA3 anstelle von BLAKE2b zur Datenauthentifizierung.
- Reed-Solomon**: Implementierung von *Reed-Solomon*-Fehlerkorrekturcodes zur Erleichterung der Fehlerkorrektur bei beschädigten Daten. Damit können Sie einen Korruptionsgrad von etwa 3 % Ihrer Datei unterstützen.
- In Stücke aufteilen** oder **in mehrere Teile aufteilen**: Wenn Sie eine große Datei verschlüsseln, können Sie Picocrypt bitten, sie in mehrere Teile aufzuteilen. Dadurch lässt sich die Datei möglicherweise leichter übertragen.
- Dateien komprimieren** oder **Dateien komprimieren**: Komprimiert Dateien, um die Größe der verschlüsselten Dateien zu verringern.
- Gelöschte Dateien** oder **Fichiers supprimés**: Quelldateien löschen, um nur die verschlüsselte Version zu behalten



### B. Entschlüsseln von Daten mit Picocrypt



Wenn Sie die Daten entschlüsseln müssen, ist das nicht komplizierter als das Verschlüsseln. Öffnen Sie einfach Picocrypt und **Ziehen Sie die zu entschlüsselnde PCV-Datei per Drag & Drop**. Geben Sie dann das Passwort ein und/oder wählen Sie die Schlüsseldatei aus, bevor Sie auf "**Entschlüsseln**" klicken.



![Image](assets/fr/021.webp)



Mit der unverschlüsselten Version des ZIP-Archivs "Encrypted.zip" kann ich nun meine beiden Dateien im Klartext wiederherstellen!



![Image](assets/fr/022.webp)



## IV. Schlussfolgerung



**Sie sind gewarnt worden: Picocrypt ist sehr einfach zu bedienen, und es funktioniert! Obwohl der Interface minimalistisch ist, enthält er einige sehr nützliche Optionen zur Anpassung der Verschlüsselung! Und da es in einer tragbaren Version erhältlich ist, können Sie es überallhin mitnehmen, um Ihre Daten sicher entschlüsseln zu können**



Achten Sie darauf, starke Passwörter zu verwenden, um die Daten zu schützen, und wenn Sie eine Schlüsseldatei verwenden, müssen Sie daran denken, diese zu sichern, da Sie sonst nicht mehr in der Lage sind, den von Picocrypt erzeugten PCV-Container zu entschlüsseln. Schließlich sollten Sie wissen, dass es auch [eine CLI-Version](https://github.com/Picocrypt/CLI) (mit weniger Funktionen) gibt, mit der Sie Picocrypt von der Kommandozeile aus starten können: Auch hier eröffnet Picocrypt neue Möglichkeiten.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5