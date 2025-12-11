---
name: Ashigaru Terminal
description: Ashigaru auf dem Desktop verwenden, um Coinjoins zu erstellen
---

![cover](assets/cover.webp)



Ashigaru Terminal ist die Adaption von Sparrow Server durch das Ashigaru-Team, die das Whirlpool Coinjoin-Protokoll implementiert. Diese Software ist eine Fortsetzung der von Samourai Wallet begonnenen Arbeit, insbesondere an der Whirlpool-GUI, deren Grundprinzipien sie übernimmt: Selbstverwahrung und Wahrung der Vertraulichkeit.



Diese Software ist ein fork von Sparrow Server, modifiziert und optimiert für die vollständige Integration mit dem Whirlpool Ökosystem, dem ursprünglich von den Samourai Teams entwickelten ZeroLink Coinjoin Protokoll.



Ashigaru Terminal wird über eine minimalistische TUI-Schnittstelle bedient und kann auf einem PC oder einem dedizierten Server eingesetzt werden. Es ermöglicht Ihnen die direkte Interaktion mit Whirlpool, um "*Tx0*" zu initiieren, "*Deposit*", "*Premix*", "*Postmix*" und "*Badbank*" Konten zu verwalten und automatische Remixes durchzuführen, um die Vertraulichkeit Ihrer Teile zu verstärken.



Kurz gesagt, Ashigaru Terminal ist besonders nützlich, wenn Sie Coinjoins mit Whirlpool erstellen wollen.



In diesem ersten Tutorial werde ich Sie durch die Installation und den Betrieb von Ashigaru Terminal führen. Ein zweites, fortgeschritteneres Tutorial wird sich dann mit der eigentlichen Erstellung von Coinjoins befassen.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Ashigaru-Terminal installieren



Um Ashigaru Terminal zu installieren, benötigst du den Tor-Browser, da die Binärdateien nur über das Tor-Netzwerk verbreitet werden. Wenn du das noch nicht getan hast, [installiere ihn auf deinem Rechner](https://www.torproject.org/download/).



### 1.1. Ashigaru Terminal herunterladen



Gehe im Tor-Browser auf [die Veröffentlichungsseite des Git-Repositorys] (http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/), um die neueste Version von Ashigaru Terminal für dein Betriebssystem herunterzuladen.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Laden Sie die folgenden 2 Dateien für Ihr Betriebssystem herunter:




- Die Binärdatei (`ashigaru_terminal_v1.0.0_amd64.deb` für Debian/Ubuntu, `.dmg` für macOS oder `.zip` für Windows) ;
- Die signierte Hashes-Datei: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Ashigaru Terminal überprüfen



Bevor Sie die Software auf Ihrem Gerät ausführen, müssen Sie ihre Authentizität und Integrität überprüfen. Dies ist ein wichtiger Schritt, da er Sie davor bewahrt, eine betrügerische Version zu installieren, die Ihre Bitcoins gefährden oder Ihren Computer infizieren könnte.



Öffnen Sie eine neue Browser-Registerkarte und gehen Sie zu [Keybase-Verifizierungstool] (https://keybase.io/verify). Fügen Sie den Inhalt der soeben heruntergeladenen "txt"-Datei in das dafür vorgesehene Feld ein und klicken Sie dann auf die Schaltfläche "Überprüfen".



![Image](assets/fr/02.webp)



Um Ihre Überprüfungsquellen zu diversifizieren, können Sie die Nachricht auch mit der auf der Website clearnet [ashigaru.rs] (https://ashigaru.rs/download/) im Bereich "Downloads" verfügbaren Nachricht vergleichen.



![Image](assets/fr/03.webp)



Wenn die Signatur gültig ist, zeigt Keybase eine Meldung an, die bestätigt, dass die Datei von den Entwicklern von Ashigaru signiert wurde.



![Image](assets/fr/04.webp)



Sie können auch auf das von Keybase angezeigte Profil `ashigarudev` klicken und überprüfen, ob der Fingerabdruck des Schlüssels genau mit dem folgenden übereinstimmt: `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Wenn an dieser Stelle ein Fehler erscheint, ist die Signatur ungültig. In diesem Fall **installieren Sie die heruntergeladene Software nicht**. Beginnen Sie noch einmal von vorne, oder bitten Sie die Community um Hilfe, bevor Sie fortfahren.



Keybase hat Ihnen den authentifizierten Hash der Anwendung zur Verfügung gestellt. Nun überprüfen wir, ob der Hash der heruntergeladenen `.deb`-, `.zip`- oder `.dmg`-Datei mit dem auf Keybase validierten Hash übereinstimmt. Gehen Sie dazu auf [HASH DATEI ONLINE](https://hash-file.online/).



Klicken Sie auf die Schaltfläche `BROWSE...` und wählen Sie die in Schritt 1.1 heruntergeladene `.deb`, `.zip` oder `.dmg` Datei. Wählen Sie dann die Hash-Funktion `SHA-256` und klicken Sie auf `CALCULATE HASH`, um den Hash-Wert für Ihre Datei zu berechnen.



![Image](assets/fr/06.webp)



Auf der Website wird dann der Software-Hash angezeigt. Vergleichen Sie ihn mit dem Hash, den Sie auf Keybase.io überprüft haben. Wenn die beiden perfekt übereinstimmen, war die Authentizitäts- und Integritätsprüfung erfolgreich. Sie können die Software dann verwenden.



![Image](assets/fr/07.webp)



### 1.3 Start Ashigaru Terminal





- Debian / Ubuntu



Um die Software zu installieren, führen Sie den Befehl :



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Ändern Sie die Reihenfolge entsprechend der heruntergeladenen Version.



Überprüfen Sie dann die Installation:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Starten Sie dann die Software:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Fenster**



Klicken Sie mit der rechten Maustaste auf die heruntergeladene und geprüfte `.zip`-Datei und wählen Sie dann `Alles entpacken...`, um den Inhalt zu entpacken.



Sobald die Extraktion abgeschlossen ist, doppelklicken Sie auf die Datei `Ashigaru-terminal.exe`, um die Software zu starten.



![Image](assets/fr/08.webp)



## 2. Erste Schritte mit Ashigaru Terminal



Ashigaru Terminal ist ein TUI (*Text-based User Interface*) Programm, d.h. eine minimalistische Oberfläche, die direkt im Terminal läuft. Sie interagieren mit ihm über Menüs und Tastenkombinationen, aber ohne eine echte klassische grafische Umgebung.



![Image](assets/fr/09.webp)



Es ist einfach zu bedienen: Verwenden Sie die Pfeiltasten Ihrer Tastatur, um durch die Menüs zu navigieren, und drücken Sie die "Enter"-Taste, um eine Aktion zu bestätigen oder eine Auswahl zu treffen.



## 3. Verbinden Ihres Knotens mit dem Ashigaru-Terminal



Standardmäßig stellt Ashigaru Terminal eine Verbindung zu einem öffentlichen Electrum-Server her. Dies birgt natürlich Risiken in Bezug auf Vertraulichkeit und Souveränität. Deshalb werden wir es so konfigurieren, dass es sich direkt mit Ihrem eigenen Electrum Server verbindet.



Öffnen Sie dazu das Menü "Einstellungen > Server".



![Image](assets/fr/10.webp)



Klicken Sie auf die Schaltfläche `< Bearbeiten >`.



![Image](assets/fr/11.webp)



Wählen Sie "Private Electrum Server" und klicken Sie dann auf "<Fortfahren>".



![Image](assets/fr/12.webp)



Gib die URL und den Port deines Servers ein. Du kannst eine Tor-Adresse in `.onion` angeben. Klicke dann auf `< Test >`, um die Verbindung zu überprüfen.



![Image](assets/fr/13.webp)



Wenn die Verbindung erfolgreich ist, erscheint die Meldung `Erfolg` zusammen mit den Angaben zu Ihrem Server.



![Image](assets/fr/14.webp)



Wenn Sie noch keinen Bitcoin-Knoten haben, empfehle ich Ihnen, diesen Kurs zu besuchen:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*In meinem Fall werde ich für dieses Lernprogramm die Verbindung zu meinem Electrs-Server trennen, da ich im Testnetz arbeite. Der Betrieb auf mainnet ist jedoch völlig identisch



## 4. Erstellen Sie ein Portfolio auf Ashigaru Terminal



Nachdem die Software nun korrekt konfiguriert ist, können wir ein Bitcoin-Portfolio hinzufügen.



Sie haben zwei Möglichkeiten:




- Sie können ein neues wallet von Grund auf neu erstellen und es ausschließlich mit Ashigaru Terminal verwenden. In diesem Fall müssen Sie diese Software jedes Mal öffnen, wenn Sie mit Ihrem wallet interagieren möchten;
- Alternativ können Sie Ihr bestehendes Ashigaru wallet auch direkt von Ihrem Telefon in Ashigaru Terminal importieren. Der Nachteil dieser Methode ist, dass sie die Sicherheit Ihrer Einrichtung etwas verringert, da Ihr wallet dann zwei risikoreichen Umgebungen statt einer ausgesetzt ist. Auf der anderen Seite bietet sie den Vorteil, dass Sie Ashigaru Terminal ständig laufen lassen können, um Ihre Münzen zu mischen, während Sie sie aus der Ferne über die Ashigaru Mobile App ausgeben können.



In diesem Lernprogramm werden wir uns für die zweite Methode entscheiden. Wenn Sie es jedoch vorziehen, ein völlig neues Portfolio zu erstellen, bleibt das Verfahren dasselbe: Der einzige Unterschied besteht darin, dass Sie während der Erstellung Ihre neue mnemonische Phrase und Ihre neue passphrase speichern müssen.



Beachten Sie auch, dass Ashigaru Terminal es nicht ermöglicht, Ihre Bitcoins direkt auszugeben. Sie können entweder dasselbe Wallet auf Ashigaru Terminal und in der Ashigaru-App synchronisieren (was ich in diesem Tutorial tun werde) oder im Sparrow Wallet.



Wenn Sie noch keinen wallet für die Ashigaru-Anwendung haben, können Sie dem entsprechenden Tutorial folgen:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Gehen Sie zum Menü "Brieftaschen".



![Image](assets/fr/15.webp)



Wählen Sie dann `wallet erstellen / wiederherstellen...`. Mit der Option "Wallet öffnen..." können Sie zu einem späteren Zeitpunkt auf ein bereits in Ashigaru Terminal gespeichertes Portfolio zugreifen.



![Image](assets/fr/16.webp)



Geben Sie Ihrem Portfolio einen Namen.



![Image](assets/fr/17.webp)



Wählen Sie dann den Portfoliotyp "Hot Wallet".






![Image](assets/fr/18.webp)



In dieser Phase unterscheidet sich das Verfahren je nach Ihrer ursprünglichen Wahl:




- Wenn Sie eine neue Mappe von Grund auf neu erstellen möchten, klicken Sie auf `<Neues Wallet erzeugen>`, legen Sie ein passphrase BIP39 fest und speichern Sie dann sorgfältig Ihre mnemonische Phrase und Ihr passphrase auf einem physischen Medium;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Wenn Sie denselben wallet wie Ihre Ashigaru-Anwendung verwenden möchten, geben Sie die 12 Wörter Ihrer mnemonischen Phrase und Ihren passphrase BIP39 direkt in die entsprechenden Felder ein. Schreiben Sie die Wörter in Kleinbuchstaben, ganz, in der Reihenfolge, getrennt durch ein Leerzeichen, ohne Zahlen oder zusätzliche Zeichen.



Sobald dieser Schritt abgeschlossen ist, klicken Sie auf `< Weiter >`.



*Hinweis*: Wenn Sie diese Schaltfläche nicht anklicken können, ist Ihre Gedächtnisstütze ungültig. Prüfen Sie sorgfältig, dass keines der Wörter falsch ist oder falsch geschrieben wird.



![Image](assets/fr/19.webp)



Anschließend müssen Sie ein Passwort festlegen. Dieses wird verwendet, um Ihr Ashigaru-Terminal wallet zu entsperren und gegen unbefugten physischen Zugriff zu schützen. Es ist nicht an der kryptografischen Ableitung Ihrer Schlüssel beteiligt: Mit anderen Worten, auch ohne dieses Passwort kann jeder, der über Ihre mnemonische Phrase und passphrase verfügt, Ihren wallet wiederherstellen und auf Ihre Bitcoins zugreifen.



Wählen Sie ein langes, komplexes, zufälliges Passwort. Bewahren Sie eine Kopie an einem sicheren Ort auf: idealerweise auf einem physischen Medium oder in einem sicheren Passwortmanager.



Klicken Sie auf "< OK >", wenn Sie fertig sind.



![Image](assets/fr/20.webp)



## 5. Verwendung des Portfolios



Sie können dann wählen, auf welches Konto Sie zugreifen möchten. Im Moment haben wir noch keine Mischungen initiiert, also greifen wir auf das Konto "Einzahlung" zu.



![Image](assets/fr/21.webp)



Die Bedienung ist dann identisch mit der von Sparrow, da Ashigaru Terminal ein fork von Sparrow Server ist. Sie finden die gleichen Menüs vor:



![Image](assets/fr/22.webp)





- transaktionen": Hier können Sie die Historie der mit diesem Konto verbundenen Transaktionen einsehen. In meinem Fall erscheinen bereits einige davon, da ich einige mit der Ashigaru-Anwendung auf derselben wallet getätigt hatte.



![Image](assets/fr/23.webp)





- receive`: erzeugt eine neue, leere Empfangsadresse für die Einzahlung von Satss auf das Einzahlungskonto.



![Image](assets/fr/24.webp)





- adressen": zeigt eine Liste aller Ihrer Adressen an, unabhängig davon, ob sie zur internen oder externen Kette Ihres Kontos gehören.



![Image](assets/fr/25.webp)





- uTXOs": listet alle verfügbaren UTXOs auf.



![Image](assets/fr/26.webp)





- einstellungen": ermöglicht den Zugriff auf Ihren Portfolio-"Deskriptor". Sie können auch Ihre seed einsehen, das *Gap Limit* anpassen oder das Erstellungsdatum Ihres Portfolios ändern.



![Image](assets/fr/27.webp)



Sie wissen nun, wie man Ashigaru Terminal installiert und verwendet. Im nächsten Tutorial sehen wir uns an, wie man mit dieser Software Coinjoins durchführt und wie man Gelder im "*Postmix*" verwaltet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
