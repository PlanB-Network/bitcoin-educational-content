---
name: SeedSigner
description: Selbstgebaute, zustandslose, erschwingliche und vollständig mit der Luft gekapselte wallet-Hardware
---

![cover](assets/cover.webp)



Der SeedSigner ist eine quelloffene wallet-Bitcoin-Hardware, die jeder mit preiswerten elektronischen Bauteilen für den allgemeinen Gebrauch selbst bauen kann. Im Gegensatz zu kommerziellen Produkten wie dem Ledger, der Coldcard oder dem Trezor handelt es sich nicht um ein fertiges Gerät, das von einem Unternehmen hergestellt wird: Es ist ein Gemeinschaftsprojekt, das es jedem ermöglicht, sein eigenes Gerät zu erstellen und jeden Schritt zu kontrollieren.



Der SeedSigner ist so konzipiert, dass er zu 100% ***air-gapped*** ist: er verbindet sich nie mit dem Internet, hat kein Wi-Fi oder Bluetooth (im Falle des Raspberry Pi Zero v1.3) und ist nie mit einem Computer verbunden, um Daten auszutauschen. Die Kommunikation erfolgt ausschließlich über ein QR-Code-Austauschsystem. Konkret zeigt Ihre Portfolioverwaltungssoftware (z. B. Sparrow Wallet) die zu signierende Transaktion in Form von QR-Codes an; Sie scannen sie mit der Kamera des SeedSigners, dann signiert das Gerät die Transaktion mit Ihren privaten Schlüsseln, die vorübergehend in seinem RAM gespeichert sind. Schließlich erzeugt es QR-Codes mit der signierten Transaktion, die Sie mit Ihrer Software scannen, um sie an das Bitcoin-Netzwerk zu senden.



![Image](assets/fr/001.webp)



SeedSigner ist außerdem ***stateless***. Mit anderen Worten, er speichert Ihre seed oder Ihre privaten Schlüssel nicht dauerhaft, im Gegensatz zu anderen Hardware-Wallets. Bei jedem Neustart ist der Speicher komplett leer, es sei denn, Sie konfigurieren das Gerät so, dass es Ihre Einstellungen auf einer microSD-Karte speichert. Sie müssen daher Ihren seed jedes Mal neu eingeben, wobei die praktischste Methode darin besteht, ihn in Form eines QR-Codes zu speichern, der beim Start mit der Kamera des SeedSigners gescannt wird. Diese Funktionsweise reduziert die Angriffsfläche erheblich: Selbst wenn ein Dieb Ihr Gerät stiehlt, wird er keine Informationen darauf finden, da es standardmäßig immer leer ist.



Eine weitere Möglichkeit, Ihr seed zu speichern und es mit dem SeedSigner zu verwenden, ist die Verwendung einer *SeedKeeper* Smartcard in Verbindung mit einem kompatiblen Lesegerät. Damit erhalten Sie ein sehr robustes *Secure Element* zum Speichern Ihres seed, während Sie den SeedSigner-Bildschirm zum Signieren von Transaktionen verwenden. Aber diese spezielle Konfiguration ist Gegenstand eines anderen speziellen Tutorials. Hier konzentrieren wir uns auf die grundlegende Verwendung des SeedSigners:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

Das SeedSigner-Projekt nimmt einen wichtigen Platz im Bitcoin-Ökosystem ein, da es jedem, überall auf der Welt, die Möglichkeit bietet, von fortschrittlicher Sicherheit zum Schutz seiner Bitcoins zu profitieren. Sein Hauptvorteil liegt in seiner Zugänglichkeit: Die benötigte Hardware kann für weniger als 50 Dollar erworben werden. Darüber hinaus können Menschen, die in Ländern mit eingeschränktem Zugang leben, ihre eigene wallet-Hardware aus Standard-Computerkomponenten bauen, die leicht zu finden sind und weniger behördlichen Beschränkungen unterliegen.



Aber auch außerhalb dieser speziellen Kontexte kann SeedSigner eine interessante Option für Sie sein: Es ist Open-Source, arbeitet zustandslos und airgapped und reduziert die Angriffsvektoren, die mit der Lieferkette Ihrer wallet-Hardware verbunden sind.



## 1. Erforderliche Ausrüstung



Um Ihren SeedSigner zu bauen, benötigen Sie die folgenden Komponenten:





- Raspberry Pi Zero
    - Empfohlen wird die Version 1.3, die weder über Wi-Fi noch über Bluetooth verfügt und somit eine vollständige Isolierung gewährleistet.
 - Die Versionen W und v2 sind ebenfalls kompatibel, enthalten aber einen Wi-Fi/Bluetooth-Chip. Es ist daher ratsam, ihn physisch zu deaktivieren, indem man das Funkmodul aus der Karte entfernt. Der Vorgang ist relativ einfach, erfordert aber Präzision (bei der Zero W genügt eine feine Zange, während man bei der v2 einen heißen Stift benötigt, um die Metallplatte zu entfernen, die das Modul verbirgt). Ich werde in dieser Anleitung nicht ins Detail gehen, aber Sie finden alle Anweisungen in diesem Dokument: *[Deaktivieren von WiFi/Bluetooth per Hardware](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Bitte beachten Sie: Einige Raspberry Pi Zero-Modelle werden ohne vorgelötete GPIO-Pins verkauft. Sie können entweder eine Version mit integrierten Pins direkt kaufen (einfachste Lösung), oder die Pins separat kaufen und sie selbst anlöten (komplexere Lösung).
 - Vergessen Sie nicht, ein Micro-USB-Netzteil beizulegen.



![Image](assets/fr/002.webp)





- Waveshare 1,3" Bildschirm (240×240 px)** (auf Französisch)
    - Es ist wichtig, dass Sie sich für dieses Modell entscheiden: Es gibt andere ähnliche Bildschirme, aber mit einer anderen Auflösung. Ohne eine Auflösung von 240×240 px ist der Bildschirm unbrauchbar.
    - Der Bildschirm verfügt über drei Tasten und einen Mini-Joystick für die Benutzeroberfläche.



![Image](assets/fr/003.webp)





- Raspberry Pi Zero**-kompatible Kamera
    - Option 1: die Standardkamera mit einer breiten Goldmatte (prüfen Sie die Kompatibilität mit Ihrem Gehäuse).
    - Option 2: die kompaktere "*Zero*"-Kamera, die speziell für den Pi Zero entwickelt wurde.



![Image](assets/fr/004.webp)





- MicroSD**-Karte
    - Empfohlene Kapazität: zwischen 4 und 32 GB.





- Gehäuse (optional, aber empfohlen)** (optional, aber empfohlen)** (optional, aber empfohlen)** (optional, aber empfohlen)**)
    - Schützt das Gerät und macht es einfach zu bedienen.
    - Das beliebteste Modell ist das "*Orange Pill Case*", für das [Open-Source STL-Dateien für den 3D-Druck verfügbar sind] (https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Die Boxen sind auch bei [unabhängigen, mit dem Projekt verbundenen Wiederverkäufern] erhältlich (https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Sie können diese Komponenten einzeln kaufen oder sich der Einfachheit halber für fertige Pakete entscheiden, die die gesamte erforderliche Hardware enthalten. Ich persönlich habe mein Paket [auf dieser französischen Website](https://bitcoinbazar.fr/) bestellt, aber Sie finden auch eine Liste von Anbietern für jede Region der Welt auf [der Hardware-Seite des SeedSigner-Projekts](https://seedsigner.com/hardware/). Wenn Sie die Komponenten lieber einzeln kaufen möchten, sind sie auf den großen E-Commerce-Plattformen oder in Fachgeschäften erhältlich.



## 2. Vorbereiten der Software



Sobald Sie Ihre Hardware zusammen haben, müssen Sie die microSD-Karte vorbereiten, indem Sie das SeedSigner-System auf ihr installieren. Gehen Sie dazu zu Ihrem normalen Computer und stecken Sie Ihre microSD-Karte für SeedSigner ein.



### 2.1. Herunterladen



Gehen Sie zu [dem offiziellen GitHub-Repository des Projekts](https://github.com/SeedSigner/seedsigner/releases). Laden Sie die neueste Version der Software herunter:




- Das `.img`-Image, das Ihrem Pi-Modell entspricht.
- Die Datei `.sha256.txt`.
- Die Datei `.sha256.txt.sig`.



![Image](assets/fr/006.webp)



Bevor wir mit der Installation beginnen, sollten wir die Software überprüfen.



### 2.2 Verifizierung unter Linux und macOS



Importieren Sie zunächst den offiziellen öffentlichen Schlüssel des SeedSigner-Projekts direkt von Keybase :



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Das Terminal sollte Ihnen mitteilen, dass ein Schlüssel importiert oder aktualisiert wurde. Als nächstes führen Sie den Verifizierungsbefehl für die Signaturdatei aus (denken Sie daran, den Befehl entsprechend Ihrer Version zu ändern, hier `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Wenn alles korrekt ist, sollte die Ausgabe `Gute Signatur` lauten. Das bedeutet, dass die Datei `.sha256.txt` mit dem Schlüssel, den Sie gerade importiert haben, signiert wurde und dass die Signatur gültig ist. Ignorieren Sie die Warnmeldung `WARNUNG: Dieser Schlüssel ist nicht mit einer vertrauenswürdigen Signatur zertifiziert`: Dies ist normal, da es nun an Ihnen liegt, zu überprüfen, ob der verwendete Schlüssel zum SeedSigner-Projekt gehört.



Vergleichen Sie dazu die letzten 16 Zeichen des angezeigten Fingerabdrucks mit denen, die auf [Keybase.io/SeedSigner](https://keybase.io/seedsigner), auf dem [offiziellen Twitter](https://twitter.com/SeedSigner/status/1530555252373704707) oder in der auf [SeedSigner.com](https://seedsigner.com/keybase.txt) veröffentlichten Datei verfügbar sind. Wenn diese Identifikatoren genau übereinstimmen, können Sie sicher sein, dass der Schlüssel tatsächlich der des Projekts ist. Im Zweifelsfall sollten Sie sofort aufhören und die SeedSigner-Community (Telegram, X, GitHub...) um Hilfe bitten.



Wenn der Schlüssel validiert wurde, können Sie überprüfen, ob das heruntergeladene Bild nicht verändert wurde (denken Sie daran, den Befehl entsprechend Ihrer Version zu ändern, hier `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- Unter Linux ist dieser Befehl eingebaut.
- Warnung: macOS-Versionen vor `Big Sur (11)` erkennen die Option `--ignore-missing` nicht. In diesem Fall entfernen Sie sie und ignorieren Sie Warnungen über fehlende Dateien.



Das erwartete Ergebnis ist ein `OK` neben der `.img` Datei. Dies bestätigt, dass das hochgeladene Bild mit dem vom Projekt veröffentlichten Bild identisch ist und nicht verändert wurde.



### 2.3 Überprüfung der Fenster



Unter Windows ist das Verfahren ähnlich, aber die Befehle sind anders. Beginnen Sie mit der Installation von [Gpg4win] (https://www.gpg4win.org/) und öffnen Sie die Anwendung *Kleopatra*. Importieren Sie den öffentlichen Schlüssel des SeedSigner-Projekts von der URL Keybase :



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Öffnen Sie als Nächstes die PowerShell in dem Ordner, in dem sich die heruntergeladenen Dateien befinden (Umschalttaste + rechte Maustaste > "PowerShell hier öffnen"). Führen Sie den folgenden Befehl aus, um die Manifest-Signatur zu überprüfen (denken Sie daran, den Befehl entsprechend Ihrer Version zu ändern, hier `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Wenn alles korrekt ist, sollte die Ausgabe `Gute Signatur` lauten. Das bedeutet, dass die Datei `.sha256.txt` mit dem Schlüssel, den Sie gerade importiert haben, signiert wurde und dass die Signatur gültig ist. Ignorieren Sie die Warnmeldung `WARNUNG: Dieser Schlüssel ist nicht mit einer vertrauenswürdigen Signatur zertifiziert`: Dies ist normal, da es nun an Ihnen liegt, zu überprüfen, ob der verwendete Schlüssel zum SeedSigner-Projekt gehört.



Vergleichen Sie dazu die letzten 16 Zeichen des angezeigten Fingerabdrucks mit denen, die auf [Keybase.io/SeedSigner](https://keybase.io/seedsigner), auf dem [offiziellen Twitter](https://twitter.com/SeedSigner/status/1530555252373704707) oder in der auf [SeedSigner.com](https://seedsigner.com/keybase.txt) veröffentlichten Datei verfügbar sind. Wenn diese Identifikatoren genau übereinstimmen, können Sie sicher sein, dass der Schlüssel tatsächlich der des Projekts ist. Im Zweifelsfall sollten Sie sofort aufhören und die SeedSigner-Community (Telegram, X, GitHub...) um Hilfe bitten.



Nachdem der Schlüssel validiert wurde, müssen Sie überprüfen, ob die Imagedatei nicht beschädigt worden ist. Verwenden Sie dazu den folgenden Befehl in PowerShell :



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Beispiel für einen Raspberry Pi Zero 2 (denken Sie daran, den Befehl entsprechend Ihrer Version zu ändern, hier `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



PowerShell berechnet dann den SHA256-Hash Ihrer Bilddatei. Vergleichen Sie diesen Hash mit dem entsprechenden Wert in `seedsigner.0.8.6.sha256.txt`.




- Wenn die beiden Werte absolut identisch sind, ist die Prüfung erfolgreich und Sie können fortfahren.
- Wenn sie nicht übereinstimmen, ist die Datei beschädigt oder fehlerhaft. Verwenden Sie sie nicht und starten Sie den Download erneut.



![Image](assets/fr/013.webp)



Eine erfolgreiche Überprüfung garantiert, dass Ihre `.img`-Datei sowohl authentisch (vom SeedSigner signiert) als auch unverändert (unmodifiziert) ist. Sie können dann gefahrlos mit dem nächsten Schritt fortfahren.



### 2.4. Flashen Sie das Bild



Wenn Sie es noch nicht haben, laden Sie die Software [Balena Etcher] herunter (https://etcher.balena.io/), dann :




- Legen Sie die microSD-Karte in Ihren Computer ein.
- Etcher starten.
- Wählen Sie die heruntergeladene und verifizierte `.img`-Datei.
- Wählen Sie die microSD-Karte als Ziel.
- Klicken Sie auf `Flash!`.



![Image](assets/fr/014.webp)



Warten Sie, bis der Vorgang abgeschlossen ist: Ihre microSD-Karte ist einsatzbereit. Jetzt ist es Zeit für den Zusammenbau!



## 3. SeedSigner-Baugruppe



Sobald Ihre microSD-Karte vorbereitet und mit der SeedSigner-Software geflasht wurde, können Sie mit der Endmontage fortfahren. Nehmen Sie sich Zeit, da einige Teile zerbrechlich sind (vor allem die Tischdecke, die Kamera und die GPIO-Pins).



### 3.1 Vorbereiten des Gehäuses



Öffnen Sie zunächst Ihr Gehäuse. Vergewissern Sie sich, dass es sauber ist und dass keine Kunststoffreste aus dem 3D-Druck den inneren Verschlüssen im Weg sind. Achten Sie auf :




- Position der Kamera (kleines rundes Loch an der Vorderseite).
- Die Öffnung für den Bildschirm.
- Die Aussparungen für die micro-USB-Anschlüsse und den microSD-Steckplatz des Raspberry Pi Zero.



### 3.2 Installation der Kamera



Suchen Sie den Flachbandanschluss der Kamera am Raspberry Pi Zero: Es handelt sich um einen dünnen schwarzen Streifen an der Seite der Platine, der zum Öffnen leicht angehoben werden kann. Heben Sie ihn vorsichtig an, ohne ihn zu forcieren: Er sollte sich einfach ein paar Millimeter neigen.



![Image](assets/fr/015.webp)



Setzen Sie die Kameraabdeckung ein. Der braune/kupferne Teil sollte nach unten zeigen. Vergewissern Sie sich, dass sie fest im Anschluss sitzt, ohne sich zu verdrehen.



![Image](assets/fr/016.webp)



Schließen Sie die schwarze Leiste, um die Tischdecke zu verriegeln (Sie werden ein leichtes Klicken spüren). Prüfen Sie vorsichtig, ob sie an ihrem Platz bleibt und sich nicht bewegt.



![Image](assets/fr/017.webp)



Setzen Sie dann das Kameramodul in die entsprechende Öffnung im Gehäuse ein. Je nach Modell kann es direkt einrasten oder mit einem kleinen Klebestreifen fixiert werden. Das Objektiv muss perfekt ausgerichtet sein und nach außen zeigen.



### 3.3 Installieren des Raspberry Pi Zero



Wenn Sie ein Gehäuse verwenden, setzen Sie die Raspberry Pi Zero-Platine darin ein. Richten Sie die Anschlüsse sorgfältig an den vorgesehenen Öffnungen aus.



Positionieren Sie dann das Waveshare-Display auf dem Raspberry Pi Zero. Die GPIO-Pins des Pi sollten perfekt mit der Buchse des Displays übereinstimmen. Drücken Sie das Display langsam auf die Pins und üben Sie dabei gleichmäßigen Druck auf jede Seite aus, um ein Verbiegen der Pins zu vermeiden.



![Image](assets/fr/018.webp)



Wenn Sie ein Gehäuse haben, vervollständigen Sie die Montage, indem Sie die Frontplatte und den Joystick hinzufügen.



Zum Schluss stecken Sie die microSD-Karte mit der geflashten Software in den Steckplatz am Rand des Raspberry Pi Zero. Vergewissern Sie sich, dass sie einrastet.



### 3.4 Erste Inbetriebnahme



Schließen Sie ein Micro-USB-Netzkabel an den entsprechenden Anschluss an. Warten Sie etwa eine Minute. Das SeedSigner-Logo sollte erscheinen, gefolgt vom Startbildschirm.



![Image](assets/fr/019.webp)



Überprüfen Sie zunächst, ob die verschiedenen Komponenten ordnungsgemäß funktionieren, indem Sie das Menü "Einstellungen > E/A-Test" aufrufen.



![Image](assets/fr/020.webp)



Testen Sie alle Tasten und stellen Sie sicher, dass sie richtig reagieren. Klicken Sie dann auf die Taste `KEY1`, um zu prüfen, ob die Kamera wie erwartet funktioniert. Dadurch wird ein Bild aufgenommen.



![Image](assets/fr/021.webp)



### 3.5 Kameraeinstellung



Je nachdem, wie Sie Ihren SeedSigner montiert haben, kann die Kamera ein invertiertes Bild anzeigen. Um dies zu korrigieren, gehen Sie zu "Einstellungen > Erweitert > Kameradrehung" und wählen Sie ggf. eine 180°-Drehung.



![Image](assets/fr/022.webp)



Wenn Sie die Kameraausrichtung geändert haben oder andere Einstellungen (wie die Sprache der Benutzeroberfläche) zu einem späteren Zeitpunkt ändern möchten, müssen Sie die Persistenz der Einstellungen auf der microSD-Karte aktivieren. Andernfalls werden Ihre Einstellungen bei jedem Neustart auf die Standardeinstellungen zurückgesetzt, da der Raspberry Pi Zero keinen dauerhaften Speicher hat.



Öffnen Sie dazu das Menü "Einstellungen > Dauerhafte Einstellungen" und wählen Sie dann "Aktiviert".



![Image](assets/fr/023.webp)



Wenn alles funktioniert, ist Ihr SeedSigner jetzt einsatzbereit!



## 4. SeedSigner-Einstellungen



Bevor Sie Ihren Bitcoin wallet erstellen, sollten Sie den SeedSigner konfigurieren. Da er auf einem Raspberry Pi Zero ohne persistenten Speicher läuft, werden seine Einstellungen nicht automatisch gespeichert, es sei denn, Sie speichern sie auf der microSD-Karte. Stellen Sie also sicher, dass Sie diese Option aktiviert haben, sonst gehen diese Einstellungen beim Neustart verloren (siehe Schritt 3.5).



### 4.1 Zugang zum Parametermenü



Starten Sie Ihren SeedSigner und warten Sie, bis der Startbildschirm erscheint. Navigieren Sie mit dem Joystick zur Option "Einstellungen" und bestätigen Sie diese durch Drücken der mittleren Taste. Sie gelangen nun in das Hauptmenü der Einstellungen.



![Image](assets/fr/024.webp)



### 4.2 Auswahl der Software für die Portfolioverwaltung



Rufen Sie dann das Menü `Koordinator-Software` auf.



![Image](assets/fr/025.webp)



Der "Koordinator" bezieht sich auf die Portfolioverwaltungssoftware, mit der Ihr SeedSigner über QR-Codes kommunizieren wird. Diese Software wird entweder auf Ihrem Computer oder auf Ihrem Smartphone installiert. Sie ermöglicht es Ihnen, Ihre Bitcoins zu verwalten, ohne jedoch jemals Zugang zu Ihren privaten Schlüsseln zu haben. Der SeedSigner bleibt das einzige Gerät, das Ihre Transaktionen signieren kann.



Die aktuelle Firmware-Version unterstützt mehrere Programme: Sparrow, Specter, BlueWallet, Nunchuk und Keeper. In meinem Fall verwende ich **Sparrow Wallet**, die ich besonders für seine Einfachheit und reiche Funktionalität empfehlen.



Wenn Sie nicht wissen, wie man es installiert, können Sie diese Anleitung befolgen:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Wählen Sie einfach die Software Ihrer Wahl aus dem Menü aus.



![Image](assets/fr/026.webp)



### 4.3 Einheiten und Betragsanzeige



Im Menü "Nennwertanzeige" können Sie die Einheit wählen, in der die Beträge angezeigt werden:




- bTC
- mBTC" (Milli-Bitcoin, oder 0,001 BTC)
- gW-15 (Satoshis, oder 1/100.000.000 BTC)



Das Gerät **sats** ist im Allgemeinen für kleine Mengen am praktischsten.



![Image](assets/fr/027.webp)



### 4.4 Erweiterte Einstellungen



Gehen Sie nun in das Menü "Erweitert". Hier finden Sie mehrere nützliche Optionen:




- gW-17 network": muss nur geändert werden, wenn Sie den SeedSigner auf dem Testnet verwenden möchten.
- qR-Code-Dichte": Passt die Menge der in jedem QR-Code enthaltenen Informationen an. Sie können den Standardwert beibehalten, es sei denn, Sie finden ihn beim Scannen schwierig zu lesen.
- xpub-Export": Aktiviert oder deaktiviert den Export Ihres erweiterten öffentlichen Schlüssels (Xpub, Hypub, Zpub) an eine Portfoliomanagement-Software per QR-Code (eine Funktion, die wir später verwenden werden, also lassen Sie sie vorerst aktiviert).
- skripttypen": definiert die Skripttypen, die zum Sperren Ihrer Bitcoins zugelassen sind. Sie brauchen diesen Parameter nicht zu ändern, da der Skripttyp direkt auf Sparrow gesetzt wird. Hier sind nur Skripte betroffen, die der SeedSigner manipulieren darf.



### 4.5 Sprachauswahl



Schließlich können Sie im Menü "Sprache" die Sprache der Benutzeroberfläche nach Ihren Wünschen ändern.



![Image](assets/fr/028.webp)



## 5. seed erstellen und speichern



Das seed (oder die mnemonische Phrase) bildet die Grundlage für Ihr Bitcoin-Portfolio. Sie wird verwendet, um Ihre privaten Schlüssel und Adressen abzuleiten, und ermöglicht den Zugang zu Ihren Fonds. SeedSigner bietet mehrere Methoden zur Erstellung an, die wir uns in diesem Abschnitt ansehen werden.



Bevor wir beginnen, noch ein paar wichtige Hinweise:




- Diese Phrase gibt Ihnen vollen, uneingeschränkten Zugang zu all Ihren Bitcoins.** Jeder, der im Besitz dieser Phrase ist, kann Ihr Geld stehlen, auch ohne physischen Zugang zu Ihrem SeedSigner ;
- Normalerweise wird eine 12-Wort-Phrase verwendet, um einen wallet im Falle eines Verlusts oder Diebstahls der wallet-Hardware wiederherzustellen. Da der SeedSigner aber ein *zustandsloses* Gerät ist, registriert er Ihren seed nie. Ihre physischen Backups sind also nicht einfach Sicherungskopien, sondern **die einzige Möglichkeit, Ihren wallet zu benutzen**. Wenn Sie diese Sicherungskopien verlieren, sind Ihre Bitcoins für immer verloren. Sichern Sie sie also sorgfältig, auf mehreren Medien und an sicheren Orten;
- Wenn Sie gerade erst anfangen, empfehle ich Ihnen dringend, dieses Tutorial zu lesen, um ein detailliertes Verständnis der Risiken zu erhalten, die mit der Verwaltung einer mnemonischen Phrase verbunden sind:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Zugriff auf das seed-Erstellungstool



Gehen Sie auf dem SeedSigner-Startbildschirm auf das Menü "Tools".



![Image](assets/fr/029.webp)



Sie werden nun generate Ihr seed. Ein seed ist einfach eine große Zufallszahl. Je zufälliger sie generiert wird, desto sicherer ist sie. SeedSigner bietet zwei Möglichkeiten, dies zu tun:




- kamera": seed wird aus dem visuellen Rauschen eines Fotos erzeugt. Man nimmt ein Bild einer zufälligen Umgebung auf (Objekt, Landschaft, Gesicht usw.), dessen Pixelvariationen zur generate-Entropie verwendet werden. Es ist eine schnelle Methode, aber nicht reproduzierbar.
- würfelwürfe": Sie würfeln, um die notwendige Entropie zu erzeugen. Das ist zeitaufwändiger, aber reproduzierbar und damit überprüfbar. Wenn Sie sich für diese Methode entscheiden, befolgen Sie die Ratschläge in diesem Tutorial (die Prüfsumme muss hier nicht berechnet werden, das übernimmt der SeedSigner):



https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Erstellen des seed mit dem Foto



Wenn Sie sich für die Fotomethode entscheiden, klicken Sie auf "Neue seed" (mit dem Kamerasymbol), machen Sie ein Foto und bestätigen Sie es. Wählen Sie dann die Länge Ihres Satzes (12 oder 24 Wörter), der zum Speichern auf dem Bildschirm erscheint. Die folgenden Schritte sind identisch mit Teil 5.3.



### 5.3 seed mit Würfeln erstellen



In diesem Tutorial verwenden wir die Methode **Würfelwürfe**. Klicken Sie auf "Neue seed" (mit dem Würfelsymbol).



![Image](assets/fr/030.webp)



Wählen Sie dann die Länge Ihrer mnemonischen Phrase. 12 Wörter bieten bereits ein ausreichendes Maß an Sicherheit, so dass ich diese Wahl empfehle.



![Image](assets/fr/031.webp)



Würfeln Sie und geben Sie die resultierenden Zahlen mit dem Cursor ein. Drücken Sie die mittlere Taste, um jede Eingabe zu bestätigen. Wenn Sie einen Fehler machen, können Sie zurückgehen. Verwenden Sie mehrere verschiedene Würfel, um den Einfluss von unausgewogenen Würfeln zu verringern. Vergewissern Sie sich, dass Sie während dieses Vorgangs nicht beobachtet werden.



![Image](assets/fr/032.webp)



Sobald Sie Ihre 50 Würfe eingegeben haben, generiert der SeedSigner Ihren Satz. **Befolgen Sie die Anweisungen in diesem Lernprogramm sorgfältig, wenn Sie gerade erst anfangen:**



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Anzeigen und Speichern des seed



Schreiben Sie die Wörter Ihres Merksatzes sorgfältig auf einen geeigneten Träger (Papier oder Metall).



![Image](assets/fr/033.webp)



### 5.5 Überprüfung der Sicherung



Um Fehler beim Backup zu vermeiden, bittet SeedSigner Sie, Ihr Backup zu verifizieren. Klicken Sie auf "Verifizieren".



![Image](assets/fr/034.webp)



Geben Sie dann das gewünschte Wort in der Reihenfolge ein, in der es im Satz vorkommt. Hier muss ich zum Beispiel das dritte Wort in meinem Satz wählen.



![Image](assets/fr/035.webp)



Wenn Sie einen Fehler machen, wird der SeedSigner Sie darauf hinweisen, und Sie müssen noch einmal von vorne anfangen. Dieser Überprüfungsschritt stellt sicher, dass Ihre Sicherung korrekt und vollständig ist. Nach der Überprüfung erscheint auf dem Bildschirm die Meldung `Backup Verified`.



![Image](assets/fr/036.webp)



Für einen umfassenderen Wiederherstellungstest folgen Sie bitte dieser Anleitung:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Das Konzept des "zustandslosen Geräts" verstehen



Der SeedSigner ist ein Gerät ohne permanenten Speicher. Das bedeutet, dass Ihr seed niemals im Gerät gespeichert wird (im Gegensatz zu einem Ledger, Trezor oder einer Coldcard zum Beispiel). Sobald Sie das Gerät ausschalten, verschwindet der seed vollständig aus seinem RAM. Wenn Sie den SeedSigner neu starten, kehrt er in einen leeren Zustand zurück: Sie müssen ihm dann Ihr seed erneut geben, damit er Ihre Transaktionen signieren kann.



Dies bietet einen wesentlichen Schutz. Im Gegensatz zu anderen Hardware-Wallets basiert SeedSigner auf einem Raspberry Pi Zero, der keinen physischen Schutz bietet, einschließlich *Secure Element*. Da jedoch keine sensiblen Daten gespeichert werden, würde selbst ein physisch kompromittiertes Gerät einem Angreifer nicht erlauben, Ihre privaten Schlüssel zu extrahieren oder Ihre Bitcoins auszugeben.



Andererseits bringt diese Architektur eine zusätzliche Verantwortung mit sich: Ohne ein Backup sind Ihre Gelder definitiv verloren. Deshalb empfehle ich ein **doppeltes Backup**. Sie haben bereits Ihre Wiederherstellungsphrase: dies ist Ihre langfristige Hauptsicherung, die Sie an einem sicheren Ort aufbewahren. Jetzt werden wir eine Kopie dieses Satzes in Form eines **QR-Codes** erstellen.



Jedes Mal, wenn Sie den SeedSigner verwenden, scannen Sie diesen QR-Code mit der Kamera des Geräts, damit es Ihren seed vorübergehend in seinen Speicher lädt, während Sie Ihre Transaktionen unterschreiben. Diese zweite Sicherung, die für den täglichen Gebrauch gedacht ist, muss ebenfalls mit größter Sorgfalt aufbewahrt werden: Jeder, der im Besitz dieses QR-Codes ist, hat vollen Zugriff auf Ihre Bitcoins.


Ich empfehle Ihnen auch, Ihren QR-Code und Ihren Merksatz an zwei verschiedenen Orten zu speichern, damit Sie im Schadensfall nicht alles verlieren.



Eine fortgeschrittene und sichere Alternative ist die Verwendung des SeedSigners mit einem **SeedKeeper**, der den seed in einem secure element speichert. Um mehr darüber zu erfahren, schauen Sie sich dieses Tutorial an:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Hauptschlüssel-Fingerabdruck schreiben



Sobald die Verifizierung abgeschlossen ist, zeigt SeedSigner den Fingerabdruck des Hauptschlüssels Ihres wallet an. Dieser Fingerabdruck identifiziert Ihr wallet und stellt sicher, dass Sie in Zukunft die richtige Wiederherstellungsphrase verwenden. Er gibt keine Informationen über Ihre privaten Schlüssel preis, so dass Sie ihn sicher auf einem digitalen Medium speichern können. Stellen Sie nur sicher, dass Sie eine zugängliche Kopie aufbewahren und diese niemals verlieren.



![Image](assets/fr/037.webp)



In diesem Stadium können Sie auch ein **passphrase BIP39** hinzufügen, um die Sicherheit Ihres wallet zu verstärken. Je nach Ihrer Backup-Strategie kann sich diese Option lohnen, aber sie birgt auch Risiken: Wenn Sie das passphrase verlieren, ist der Zugang zu Ihren Bitcoins dauerhaft verloren.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Wenn Sie mit dem passphrase-Konzept noch nicht vertraut sind, lade ich Sie ein, diese umfassende Anleitung zu diesem Thema zu lesen:



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 Speichern des seed im QR-Format (*SeedQR*)



Mit SeedSigner können Sie Ihren seed in einen Papier-QR-Code umwandeln, der *SeedQR* genannt wird. Diese Methode vereinfacht das Nachladen Ihres wallet, da Sie nicht jedes Wort manuell neu eingeben müssen.



Dazu benötigen Sie einen leeren Papier- oder Metall-QR-Code, der der Länge Ihrer mnemonischen Phrase entspricht. Wenn Sie ein komplettes Paket für Ihren SeedSigner gekauft haben, sind die Vorlagen normalerweise enthalten. Wenn nicht, können Sie sie hier herunterladen und ausdrucken (oder von Hand reproduzieren):




- [12-Wort-Format](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [24-Wort-Format](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Kompaktformat 12 Wörter](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Kompaktformat 24 Wörter](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Wählen Sie auf Ihrem seed-Bildschirm "Backup Seed".



![Image](assets/fr/039.webp)



Wählen Sie dann "Als SeedQR exportieren".



![Image](assets/fr/040.webp)



Wählen Sie dann das gewünschte Format (normal oder kompakt) entsprechend der verfügbaren Papiervorlage.



![Image](assets/fr/041.webp)



Klicken Sie auf "Begin", um mit der Erstellung des *SeedQR* zu beginnen. Der SeedSigner zeigt dann eine Reihe von Gittern (A1, A2, B1 usw.) an, die jeweils einem Teil des Codes entsprechen.



![Image](assets/fr/042.webp)



Reproduzieren Sie sorgfältig jeden schwarzen Punkt auf Ihrem Speicherblatt und benutzen Sie dann den Joystick, um zum nächsten Block zu gelangen. Nehmen Sie sich Zeit: Eine einfache Fehlausrichtung kann den QR-Code unbrauchbar machen.



Ein paar Tipps:




- Beginnen Sie mit einem Bleistift, damit Sie eventuelle Fehler korrigieren können, und wechseln Sie anschließend wieder zu einem feinen schwarzen Stift;
- Ein gut zentrierter Punkt in der Mitte des Quadrats ist alles, was Sie brauchen, es muss nicht vollständig ausgefüllt werden.



![Image](assets/fr/043.webp)



Klicken Sie dann auf "SeedQR bestätigen", und scannen Sie Ihren QR-Code, um zu überprüfen, ob er korrekt funktioniert.



![Image](assets/fr/044.webp)



Wenn die Meldung `Success` angezeigt wird, ist Ihr *SeedQR* gültig: Sie können mit dem nächsten Schritt fortfahren.



![Image](assets/fr/045.webp)



**Bewahren Sie dieses Blatt so strikt auf wie Ihre Wiederherstellungsphrase. Jeder, der im Besitz dieses QR-Codes ist, kann Ihre privaten Schlüssel rekonstruieren und Ihre Bitcoins stehlen.**



Herzlichen Glückwunsch, Ihr Bitcoin-Portfolio ist jetzt betriebsbereit! Wir werden nun seine öffentlichen Komponenten in **Sparrow Wallet** importieren, um es einfach zu verwalten.



## 6. wallet in Sparrow importieren



Sobald Ihr SeedSigner eingerichtet und Ihr seed korrekt erstellt und gespeichert wurde, besteht der nächste Schritt darin, dieses Portfolio mit einer Verwaltungssoftware wie Sparrow Wallet zu verknüpfen. Ihr seed wird immer offline bleiben, da nur der öffentliche Teil Ihres Portfolios an Sparrow übermittelt wird. Dadurch kann die Software Ihre Adressen und Transaktionen anzeigen und neue Transaktionen erstellen, ohne dass Sie jemals Ihre Bitcoins ausgeben können. Um Ihre Bitcoins auszugeben, muss Ihr SeedSigner immer die von Sparrow vorbereitete Transaktion unterschreiben.



### 6.1 Vorbereiten des SeedSigners



Legen Sie die microSD-Karte mit dem Betriebssystem ein, schalten Sie Ihren SeedSigner ein und laden Sie dann den seed, den Sie gerade aus Ihrem Backup-QR-Code erstellt haben. Wählen Sie auf dem Startbildschirm "Scannen" und scannen Sie dann Ihren SeedQR mit dem SeedSigner.



![Image](assets/fr/046.webp)



Überprüfen Sie, ob der Fingerabdruck auf Ihrem Hauptschlüssel mit dem Fingerabdruck auf Ihrem wallet übereinstimmt. Wenn Sie ein passphrase verwenden, geben Sie es an dieser Stelle ein.



![Image](assets/fr/047.webp)



Dies führt Sie zum Menü für Ihr Portfolio, in meinem Fall mit dem Namen `d4149b27`. Wenn Sie sich wieder auf dem Startbildschirm befinden, wählen Sie "Seeds" und dann den Druck, der Ihrem Portfolio entspricht. Klicken Sie dann auf "Xpub exportieren".



![Image](assets/fr/048.webp)



Wählen Sie den Portfoliotyp. In unserem Fall handelt es sich um ein Einzelportfolio: Wählen Sie "Single Sig".



![Image](assets/fr/049.webp)



Als nächstes kommt die Wahl des Skripting-Standards. Der neueste und hinsichtlich der Transaktionskosten günstigste ist Taproot. Ich rate Ihnen daher, diesen Standard zu wählen.



![Image](assets/fr/050.webp)



Es wird eine Warnmeldung angezeigt. Das ist normal: Mit diesem erweiterten öffentlichen Schlüssel (`xpub`) können Sie alle von Ihrem seed (auf dem ersten Konto) abgeleiteten Adressen einsehen. Er erlaubt es Ihnen nicht, Ihr Geld auszugeben, aber er zeigt die Struktur Ihres Portfolios. Sollte er jemals durchsickern, ist das ein Problem für Ihre Privatsphäre, aber nicht für die Sicherheit Ihrer Bitcoins: Sie können sie sehen, aber nicht ausgeben.



Klicken Sie auf "Ich verstehe" und dann auf "Xpub exportieren", wenn Sie mit den angezeigten Informationen zufrieden sind.



Der SeedSigner erzeugt dann Ihr xpub in Form eines dynamischen QR-Codes, der alle Daten enthält, die Sie für die Verwaltung Ihres Portfolios in Sparrow Wallet benötigen.



![Image](assets/fr/051.webp)



Mit dem Joystick können Sie die Bildschirmhelligkeit einstellen, um das Scannen von QR-Codes zu erleichtern.



### 6.2 Importieren eines neuen Portfolios in Sparrow Wallet



Vergewissern Sie sich, dass Sie die Software Sparrow Wallet auf Ihrem Computer installiert haben. Wenn Sie nicht wissen, wie Sie die Software herunterladen, überprüfen und richtig installieren, lesen Sie unsere vollständige Anleitung zu diesem Thema:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Öffnen Sie auf Ihrem Computer Sparrow Wallet, und klicken Sie dann in der Menüleiste auf "Datei → Wallet importieren".



![Image](assets/fr/052.webp)



Scrollen Sie nach unten zu "SeedSigner" und wählen Sie "Scannen...". Ihre Webcam wird geöffnet: Scannen Sie den dynamischen QR-Code, der auf dem Bildschirm Ihres SeedSigners angezeigt wird.



![Image](assets/fr/053.webp)



Vergeben Sie einen Namen für Ihr Portfolio und klicken Sie dann auf "Wallet erstellen". Sparrow fordert Sie dann auf, ein Passwort festzulegen, um den lokalen Zugang zu diesem wallet zu sperren. Wählen Sie ein sicheres Passwort: Es schützt den Zugriff auf Ihre Portfoliodaten in Sparrow (öffentliche Schlüssel, Adressen, Labels und Transaktionshistorie). Dieses Kennwort wird nicht benötigt, um das Portfolio zu einem späteren Zeitpunkt wiederherzustellen: Zu diesem Zweck wird nur Ihre mnemonische Phrase (und möglicherweise Ihr passphrase) benötigt.



Ich empfehle Ihnen, dieses Passwort in einem Passwort-Manager zu speichern, damit Sie es nicht verlieren.



![Image](assets/fr/054.webp)



Ihr Keystore wurde nun erfolgreich importiert.



![Image](assets/fr/055.webp)



Überprüfen Sie dann, ob der in Sparrow angezeigte "Master-Fingerabdruck" mit dem zuvor in Ihrem SeedSigner notierten Fingerabdruck übereinstimmt.



Ihr SeedSigner und Sparrow Wallet sind jetzt sicher miteinander verbunden. Das Sparrow fungiert als vollständige Verwaltungsschnittstelle, während der SeedSigner das einzige Gerät bleibt, das Ihre Transaktionen signieren kann. Sie sind nun bereit, Bitcoins in einer vollständig abgekapselten Konfiguration zu empfangen und zu senden.



## 7. Empfangen und Senden von Bitcoins



Ihr SeedSigner und Ihr Sparrow Wallet sind nun so konfiguriert, dass sie zusammenarbeiten. In diesem letzten Abschnitt sehen wir uns an, wie Sie mit dieser Konfiguration Bitcoins empfangen und senden können.



### 7.1 Empfang von Bitcoins



#### 7.1.1 Generierung einer Empfangsadresse



Öffnen Sie auf Ihrem Computer Sparrow Wallet und entsperren Sie Ihren SeedSigner wallet mit Ihrem Passwort. Stellen Sie sicher, dass die Software mit einem Server verbunden ist (Kerbe unten rechts). Klicken Sie in der Seitenleiste auf `Empfangen`.



![Image](assets/fr/056.webp)



Es wird eine neue Bitcoin-Adresse angezeigt. Sie werden sehen:




- Die Textadresse (beginnend mit `bc1p...`, wenn Sie wie ich P2TR verwenden),
- Der entsprechende QR-Code,
- Ein Feld "Bezeichnung" zur Verfolgung Ihrer Transaktionen.



Ich empfehle Ihnen dringend, jede Bitcoin-Quittung auf Ihrem wallet mit einem Etikett zu versehen. Dadurch können Sie die Herkunft jedes UTXO leicht identifizieren und Ihr Datenschutzmanagement verbessern. Um dieses wichtige Thema zu vertiefen, können Sie sich die spezielle Schulung auf der Plan ₿ Academy ansehen:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Um ein Etikett hinzuzufügen, geben Sie einfach einen Namen in das Feld "Etikett" ein und bestätigen dann.



Zum Beispiel:



```txt
Label : Sale of the Raspberry Pi Zero
```



Ihre Adresse ist nun in allen Sparrow-Abschnitten mit diesem Label verknüpft.



![Image](assets/fr/057.webp)



#### 7.1.2 Address-Überprüfung auf dem SeedSigner



Bevor Sie Ihre Empfangsadresse freigeben, ist es sehr wichtig zu überprüfen, ob sie zu Ihrem seed gehört. Dieser Schritt stellt sicher, dass Ihr SeedSigner in der Lage ist, mit dieser Adresse verbundene Transaktionen zu signieren. Er schützt auch vor möglichen Angriffen, bei denen Sparrow eine betrügerische Adresse anzeigt. Denken Sie daran, dass Sparrow in einer unsicheren Umgebung (Ihrem Computer) läuft, die eine viel größere Angriffsfläche bietet als Ihr SeedSigner, der völlig isoliert ist. Deshalb sollten Sie den vom Sparrow angezeigten Empfangsadressen niemals blindlings glauben, bevor Sie sie nicht mit Ihrer wallet-Hardware überprüft haben.



Klicken Sie auf dem Sparrow auf den QR-Code der Adresse, um ihn zu vergrößern: Er wird dann als Vollbild angezeigt.



![Image](assets/fr/058.webp)



Wählen Sie auf Ihrem SeedSigner im Hauptmenü "Scannen". Scannen Sie den auf Ihrem Computerbildschirm angezeigten QR-Code und wählen Sie dann den seed, der Ihrem wallet entspricht (in meinem Fall den Fingerabdruck "d4149b27").



![Image](assets/fr/059.webp)



Wenn die gescannte Adresse mit der von Ihrem seed übereinstimmt, erscheint auf dem SeedSigner-Bildschirm die Meldung: gW-92 verifiziert".



![Image](assets/fr/060.webp)



Dies bestätigt, dass die Adresse zu Ihrer wallet gehört und dass Sie vertrauensvoll Bitcoins von ihr erhalten können.



#### 7.1.3 Erhalt der Mittel



Sie können nun diese Adresse (in Form eines Textes oder QR-Codes) an die Person oder Abteilung weitergeben, die Ihnen die Daten schicken muss. Sobald die Transaktion im Netz übertragen wurde, erscheint sie auf der Registerkarte "Transaktionen" von Sparrow Wallet.



![Image](assets/fr/061.webp)



### 7.2 Bitcoins senden



Das Versenden von Bitcoins mit einem SeedSigner ist ein 3-stufiger Prozess:




- Erstellung von Vorgängen in Sparrow ;
- Unterzeichnung der Transaktion durch den SeedSigner ;
- Endgültige Verteilung der Transaktion über Sparrow.



Der gesamte Austausch zwischen den beiden Geräten erfolgt ausschließlich über QR-Codes.



#### 7.2.1 Anlegen der Transaktion in Sparrow



In Sparrow Wallet können Sie auf die Registerkarte "Senden" in der linken Seitenleiste klicken. Ich ziehe es jedoch vor, die Registerkarte "UTXOs" zu verwenden, die es Ihnen ermöglicht, "*Coin Control*" zu praktizieren. Mit dieser Methode haben Sie eine genaue Kontrolle über die verwendeten UTXOs, so dass Sie die Informationen kontrollieren können, die Sie während der Transaktion preisgeben.



Wählen Sie auf der Registerkarte "UTXOs" die Münzen aus, die Sie ausgeben möchten, und klicken Sie dann auf "Ausgewählte senden".



![Image](assets/fr/062.webp)



Füllen Sie dann die Transaktionsfelder aus:




- Fügen Sie unter "Bezahlen an" die Adresse des Empfängers ein oder klicken Sie auf das Kamerasymbol, um den QR-Code zu scannen;
- Fügen Sie unter "Bezeichnung" eine Bezeichnung hinzu, um diese Ausgabe zu verfolgen;
- Geben Sie unter "Betrag" den zu überweisenden Betrag ein;
- Wählen Sie schließlich den Gebührensatz auf der Grundlage der aktuellen Marktbedingungen (Schätzungen finden Sie unter [mempool.space](https://mempool.space/)).



Wenn Sie die Felder ausgefüllt haben, überprüfen Sie die Angaben sorgfältig und klicken Sie dann auf "Transaktion erstellen >>".



![Image](assets/fr/063.webp)



Überprüfen Sie die Details der Transaktion, um sicherzustellen, dass alles korrekt ist, und klicken Sie dann auf "Transaktion zur Unterzeichnung abschließen".



![Image](assets/fr/064.webp)



Die Transaktion ist nun fertig, aber noch nicht unterzeichnet. Um den [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) als QR-Code anzuzeigen, klicken Sie auf "QR anzeigen".



![Image](assets/fr/065.webp)



#### 7.2.2 Unterzeichnung der Transaktion mit dem SeedSigner



Schalten Sie Ihren SeedSigner ein und scannen Sie Ihren SeedQR, um wie gewohnt auf Ihr Portfolio zuzugreifen. Wählen Sie auf dem Startbildschirm "Scannen" und scannen Sie dann den auf dem Sparrow angezeigten QR-Code.



![Image](assets/fr/066.webp)



Dann wählen Sie den seed, der zu Ihrem Portfolio passt.



![Image](assets/fr/067.webp)



Der SeedSigner erkennt automatisch, dass es sich um eine PSBT handelt und zeigt eine Zusammenfassung der Transaktion an:




   - Der gesendete Betrag,
   - Ausgangsadressen,
   - Damit verbundene Transaktionskosten.



Klicken Sie auf "Details überprüfen" und überprüfen Sie sorgfältig alle Informationen direkt auf dem Bildschirm des SeedSigners. Die wichtigsten zu prüfenden Punkte sind der gesendete Betrag, die Adresse des Empfängers und die Höhe der angefallenen Gebühren.



![Image](assets/fr/068.webp)



Wenn alles korrekt ist, wählen Sie "PSBT genehmigen", um die Transaktion mit dem/den entsprechenden privaten Schlüssel(n) zu signieren.



![Image](assets/fr/069.webp)



Nach der Unterzeichnung generiert der SeedSigner einen neuen QR-Code, der die unterzeichnete Transaktion enthält und von Sparrow gescannt werden kann.



![Image](assets/fr/070.webp)



#### 7.2.3 Übermittlung der Transaktion von Sparrow



Da die Transaktion nun gültig ist, muss sie im Bitcoin-Netzwerk verbreitet werden, damit sie einen Miner erreicht, der sie zu einem Block hinzufügt.



Klicken Sie auf dem Sparrow auf "QR Scan".



![Image](assets/fr/071.webp)



Halten Sie den von Ihrem SeedSigner angezeigten QR-Code (den der signierten Transaktion) vor die Webcam. Sparrow entschlüsselt die Signatur und zeigt die vollständigen Transaktionsdetails an. Überprüfen Sie abschließend, ob alle Informationen korrekt sind, und klicken Sie dann auf Transaktion senden, um sie im Bitcoin-Netzwerk zu übertragen.



![Image](assets/fr/072.webp)



Ihre Transaktion wurde nun an das Bitcoin-Netz gesendet. Sie können den Fortschritt der Transaktion auf der Registerkarte "Transaktionen" von Sparrow Wallet verfolgen.



![Image](assets/fr/073.webp)



Sie haben nun die Grundlagen der Verwendung von SeedSigner erlernt. Um Ihr Wissen zu vertiefen und fortgeschrittene Anwendungen zu erkunden, lade ich Sie ein, das folgende Tutorial zu lesen:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Sie können die Entwicklung des Open-Source-Projekts SeedSigner auch durch eine Spende in Bitcoins unterstützen!](https://seedsigner.com/donate/)**



*Hinweis: Einige der Bilder in diesem Tutorial stammen von der [offiziellen SeedSigner-Projekt-Website] (https://seedsigner.com/) und dem [GitHub-Repository] (https://github.com/SeedSigner/seedsigner)