---
name: Specter DIY
description: Einrichtungsanleitung für Specter DIY
---

![cover](assets/cover.webp)


## Specter-DIY


> Cypherpunks schreiben Code. Wir wissen, dass jemand Software schreiben muss, um die Privatsphäre zu schützen, und da wir die Privatsphäre nur erhalten können, wenn wir alle sie schützen, werden wir sie schreiben.

*Das Manifest eines Cypherpunk - Eric Hughes - 9. März 1993*


Die Idee des Projekts ist es, einen Hardware-wallet aus handelsüblichen Komponenten zu bauen.

Auch wenn wir eine Erweiterungsplatine haben, die alles in einen schönen Formfaktor bringt und Ihnen hilft, jegliches Löten zu vermeiden, werden wir weiterhin die Kompatibilität mit Standardkomponenten unterstützen und aufrechterhalten.


![image](assets/fr/01.webp)


Wir wollen das Projekt auch so flexibel halten, dass es mit minimalen Änderungen auf jedem anderen Komponentensatz funktionieren kann. Vielleicht möchten Sie einen Hardware-wallet auf einer anderen Architektur (RISC-V?) mit einem Audiomodem als Kommunikationskanal entwickeln - Sie sollten dazu in der Lage sein. Es sollte einfach sein, Funktionen von Specter hinzuzufügen oder zu ändern, und wir versuchen, logische Module so weit wie möglich zu abstrahieren.


QR-Codes sind eine Standardmethode für Specter zur Kommunikation mit dem Host. QR-Codes sind sehr praktisch und ermöglichen dem Benutzer die Kontrolle über die Datenübertragung - jeder QR-Code hat eine sehr begrenzte Kapazität und die Kommunikation erfolgt unidirektional. Und es ist airgapped - Sie müssen das wallet zu keiner Zeit mit dem Computer verbinden.


Für die Speicherung von Geheimnissen unterstützen wir den agnostischen Modus (wallet vergisst alle Geheimnisse, wenn es ausgeschaltet wird), den rücksichtslosen Modus (speichert Geheimnisse im Flash des Anwendungsmikrocontrollers) und die Integration von secure element ist in Kürze geplant.


Unser Hauptaugenmerk liegt auf dem Multisignatur-Setup mit anderen Hardware-Wallets, aber wallet kann auch als Einzelsignierer arbeiten. Wir versuchen, es mit Bitcoin Core kompatibel zu machen, wo wir können - PSBT für unsignierte Transaktionen, wallet Deskriptoren zum Importieren/Exportieren von Multisig-Wallets. Um die Kommunikation mit Bitcoin Core zu vereinfachen, arbeiten wir auch an [Specter Desktop app](https://github.com/cryptoadvance/specter-desktop) - ein kleiner Python-Flask-Server, der mit Ihrem Bitcoin Core-Knoten kommuniziert.


Der größte Teil der Firmware ist in MicroPython geschrieben, wodurch der Code leicht zu prüfen und zu ändern ist. Wir verwenden die Bibliothek [secp256k1](https://github.com/bitcoin-core/secp256k1) von Bitcoin Core für elliptische Kurvenberechnungen und die Bibliothek [LittlevGL](https://lvgl.io/) für die grafische Benutzeroberfläche.


## Haftungsausschluss


Das Projekt ist inzwischen so weit ausgereift, dass das Sicherheitsniveau von Specter-DIY mit dem kommerzieller Hardware-Geldbörsen auf dem Markt vergleichbar ist. Wir haben einen sicheren Bootloader implementiert, der Firmware-Upgrades verifiziert, sodass Sie sicher sein können, dass nach der Ersteinrichtung nur signierte Firmware auf das Gerät hochgeladen werden kann. Anders als bei kommerziellen signierten Geräten muss der Bootloader jedoch vom Benutzer manuell installiert werden und wird nicht vom Gerätehersteller werkseitig eingestellt. Seien Sie daher bei der Erstinstallation der Firmware besonders aufmerksam und stellen Sie sicher, dass Sie die PGP-Signaturen verifiziert haben und die Firmware von einem sicheren Computer aus flashen.


Wenn etwas nicht funktioniert, öffnen Sie hier ein Problem oder stellen Sie eine Frage in unserer [Telegram-Gruppe](https://t.me/+VEinVSYkW5TUl5Ai).


## Einkaufsliste für Specter-DIY


Hier beschreiben wir, was zu kaufen ist, und im nächsten Teil erklären wir, wie man es zusammenbaut, und geben ein paar Hinweise zur Platine - Stromversorgungs-Jumper, USB-Anschlüsse usw.


### Entdeckungstafel


Hauptbestandteil des Geräts ist die Entwicklerplatine:



- STM32F469I-DISCO-Entwicklerplatine (z. B. von [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) oder [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Mini**USB-Kabel
- Standard-MicroUSB-Kabel für die Kommunikation über USB


Optional, aber empfohlen:


- [Waveshare QR-Code-Scanner](https://www.waveshare.com/barcode-scanner-module.htm) mit langen Stiftleisten wie [diese](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) oder [diese](https://www.amazon.com/gp/product/B015KA0RRU/), um den Scanner mit der Platine zu verbinden (4 Stiftleisten erforderlich).


Wir arbeiten derzeit an einer Erweiterungsplatine, die einen Smartcard-Slot, einen QR-Code-Scanner, eine Batterie und ein 3D-gedrucktes Gehäuse enthält, aber nicht das Hauptteil - die Entdeckungsplatine, die Sie separat bestellen müssen. Auf diese Weise ist ein Angriff auf die Lieferkette immer noch kein Thema, da die sicherheitskritischen Komponenten in einem beliebigen Elektronikgeschäft gekauft werden.


Sie können Specter auch ohne zusätzliche Komponenten verwenden, aber Sie können mit ihm über USB oder den eingebauten SD-Kartenslot kommunizieren. Die Verwendung von Specter über USB bedeutet, dass es nicht mit der Luft verbunden ist, so dass Sie eine wichtige Sicherheitseigenschaft verlieren.


### QR-Scanner


Für den QR-Code-Scanner haben Sie mehrere Möglichkeiten.


**Option 1. Empfehlenswert ** Angenehm guter Scanner von Waveshare (40$)


[Waveshare-Scanner](https://www.waveshare.com/barcode-scanner-module.htm) - Sie müssen eine Möglichkeit finden, ihn gut zu befestigen, vielleicht mit einer Art Arduino-Prototyp-Schild und etwas Klebeband.


Löten ist nicht erforderlich, aber wenn du über Lötkenntnisse verfügst, kannst du den wallet viel schöner machen ;)


**Option 2.** Sehr schöner Scanner von Mikroe, aber ziemlich teuer (150$):


[Barcode-Klick](https://www.mikroe.com/barcode-click) + [Adapter](https://www.mikroe.com/arduino-uno-click-shield)


**Option 3.** Jeder andere QR-Scanner


Sie können einige billige Scanner in China finden. Ihre Qualität ist oft nicht so toll, aber man kann es ja mal versuchen. Vielleicht würde sogar ESPcamera die Aufgabe erfüllen. Sie müssen nur Strom, UART (Pins D0 und D1) und Trigger an D5 anschließen.


**Option 4.** Kein Scanner.


Dann können Sie Specter nur mit USB/SD-Karte verwenden.


Es sei denn, Sie bauen Ihr eigenes Kommunikationsmodul, das statt QR-Codes etwas anderes verwendet - Audiomodem, Bluetooth oder was auch immer. Sobald es ausgelöst werden kann und die Daten über die serielle Schnittstelle sendet, können Sie tun, was Sie wollen.


### Optionale Komponenten


Wenn Sie eine winzige Powerbank oder ein Akku- und Stromladegerät/Booster hinzufügen, wird Ihr wallet völlig autark ;)



## Montage von Specter-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### Waveshare Barcode-Scanner anschließen


Die wallet-Firmware konfiguriert den Scanner beim ersten Durchlauf für Sie, so dass keine manuelle Vorkonfiguration erforderlich ist.


Hier sehen Sie, wie Sie den Scanner an die Platine anschließen:


![image](assets/fr/02.webp)


Der Einfachheit halber können Sie ein Arduino Protype Schild kaufen und alles darauf löten und montieren (z.B. [dieses](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Energieverwaltung


Auf der Oberseite der Platine befindet sich ein Jumper, der festlegt, wo das Gerät mit Strom versorgt werden soll. Sie können die Position des Jumpers ändern und als Stromquelle einen der USB-Anschlüsse oder den VIN-Pin auswählen und dort eine externe Batterie anschließen (sollte 5 V betragen).


### Gehäuse für DIY


Sehen Sie sich den Ordner [enclosures](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures) an.


### Seien Sie kreativ!


Bauen Sie Ihr eigenes Specter-DIY zusammen und schicken Sie uns die Bilder (stellen Sie einen Pull Request oder kontaktieren Sie uns).


Seht euch die [Galerie](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) mit den von der Community zusammengestellten Gespenstern an!




## Installieren des kompilierten Codes


Mit dem sicheren Bootloader ist die Erstinstallation der Firmware etwas anders. Upgrades sind einfacher und erfordern nicht den Anschluss der Hardware wallet an den Computer.


![video](https://youtu.be/eF4cgK_L6T4)


### Flashen der ursprünglichen Firmware


**Hinweis** Wenn Sie keine Binärdateien aus den Veröffentlichungen verwenden wollen, lesen Sie die [Bootloader-Dokumentation](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md), in der erklärt wird, wie Sie den Bootloader kompilieren und so konfigurieren, dass er Ihre öffentlichen Schlüssel anstelle unserer verwendet.



- Wenn Sie von Versionen unter `1.4.0` upgraden oder die Firmware zum ersten Mal hochladen, verwenden Sie die `initial_firmware_<version>.bin` von der [releases](https://github.com/cryptoadvance/specter-diy/releases) Seite.
 - Überprüfe die Signatur der Datei "sha256.signed.txt" mit [Stepans PGP-Schlüssel](https://stepansnigirev.com/ss-specter-release.asc)
 - Überprüfen Sie den Hash der Datei `initial_firmware_<version>.bin` mit dem in der Datei `sha256.signed.txt` gespeicherten Hash
- Wenn Sie ein Upgrade von einem leeren Bootloader durchführen oder die Fehlermeldung des Bootloaders erscheint, dass die Firmware nicht gültig ist, lesen Sie den nächsten Abschnitt - Flashen signierter Specter-Firmware.
- Vergewissern Sie sich, dass der Power-Jumper Ihres Discovery-Boards auf der Position STLK steht
- Verbinden Sie das Discovery Board über das **miniUSB**-Kabel an der Oberseite des Boards mit Ihrem Computer.
    - Die Karte sollte als Wechseldatenträger mit dem Namen `DIS_F469NI` erscheinen.
- Kopieren Sie die Datei `initial_firmware_<version>.bin` in das Stammverzeichnis des `DIS_F469NI`-Dateisystems.
- Wenn das Board mit dem Flashen der Firmware fertig ist, setzt es sich selbst zurück und bootet neu in den Bootloader. Der Bootloader prüft die Firmware und bootet in die Hauptfirmware. Wenn eine Fehlermeldung angezeigt wird, dass keine Firmware gefunden wurde, folgen Sie den Update-Anweisungen und laden Sie die Firmware über die SD-Karte hoch.
- Jetzt können Sie den Power-Jumper umstecken und das Board über die Powerbank oder die Batterie mit Strom versorgen.


Das Flashen der anfänglichen Firmware durch Kopieren und Einfügen der `.bin`-Datei schlägt manchmal fehl - oft wegen des Kabels, oder wenn Sie das Gerät über einen USB-Hub anschließen. In diesem Fall können Sie es noch ein paar Mal versuchen (normalerweise funktioniert es nach 2-3 Versuchen).


Wenn es immer wieder fehlschlägt, können Sie das Open-Source-Tool [stlink](https://github.com/stlink-org/stlink/releases/latest) verwenden. Installieren Sie es und geben Sie in Ihrem Terminal ein: `st-flash write <Pfad/zu/initial_firmare.bin> 0x8000000`. Das funktioniert normalerweise viel zuverlässiger.


### Aktualisieren der Firmware



- Laden Sie die Datei `specter_upgrade_<version>.bin` aus dem [releases](https://github.com/cryptoadvance/specter-diy/releases) herunter.
- Kopieren Sie diese Binärdatei in das Stammverzeichnis der SD-Karte (FAT-formatiert, maximal 32 GB)
 - Vergewissern Sie sich, dass sich nur eine `specter_upgrade***.bin`-Datei im Stammverzeichnis befindet
- Stecken Sie die SD-Karte in den SD-Slot des Discovery-Boards und schalten Sie das Board ein
- Der Bootloader wird die Firmware flashen und Sie benachrichtigen, wenn dies geschehen ist.
- Starten Sie die Karte neu - Sie sehen nun die Specter-DIY-Schnittstelle, die Ihnen vorschlägt, Ihren PIN-Code auszuwählen


Wann immer eine neue Version herauskommt, laden Sie einfach die Datei `specter_upgrade_<version>.bin` aus den Veröffentlichungen herunter, legen Sie sie auf der SD-Karte ab und aktualisieren Sie das Gerät genau wie im vorherigen Schritt. Der Bootloader stellt sicher, dass nur signierte Firmware auf das Board geladen werden kann.


### Wie man die Firmware-Version herausfindet


Gehen Sie in das Menü "Geräteeinstellungen" - dort wird die Versionsnummer unter dem Titel des Bildschirms angezeigt.


## Verwendung von Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Sicherheit von Specter-DIY


### Hardware


Das Display wird von der MCU der Anwendung gesteuert.


Die Integration des sicheren Elements ist noch nicht abgeschlossen - im Moment werden die Geheimnisse auch auf der Haupt-MCU gespeichert. Sie können das wallet aber auch ohne Speicherung des Geheimnisses verwenden - Sie müssen nur jedes Mal Ihre Wiederherstellungsphrase eingeben. Warum sollte man sich einen langen passphrase merken, wenn man sich die ganze Eselsbrücke merken kann?


Das Gerät verwendet externen Flash zum Speichern einiger Dateien (QSPI), aber alle Benutzerdateien werden vom wallet signiert und beim Laden geprüft.


Die QR-Scanfunktion befindet sich auf einem separaten Mikrocontroller, sodass die gesamte Bildverarbeitung außerhalb der sicherheitskritischen MCU stattfindet. Derzeit werden USB und SD-Karte noch von der Haupt-MCU verwaltet. Verwenden Sie also keine SD-Karte und USB, wenn Sie die Angriffsfläche verringern möchten.


### PIN-Schutz (Benutzerauthentifizierung)


Während des ersten Starts wird auf der Haupt-MCU ein einzigartiges Geheimnis generiert. Anhand dieses Geheimnisses können Sie überprüfen, dass das Gerät nicht durch ein bösartiges Gerät ersetzt wurde - wenn Sie den PIN-Code eingeben, sehen Sie eine Liste von Wörtern, die gleich bleiben, solange das Geheimnis besteht.


Ihr PIN-Code wird zusammen mit diesem einmaligen Geheimnis verwendet, um generate einen Entschlüsselungsschlüssel für Ihre Bitcoin-Schlüssel zu erstellen (falls Sie diese speichern). Wenn der Angreifer also in der Lage wäre, den PIN-Bildschirm zu umgehen, wird die Entschlüsselung trotzdem fehlschlagen.


Wenn Sie die Firmware gesperrt haben (TODO: fügen Sie hier den Link zur Anleitung ein), wird auch das Geheimnis effektiv gesperrt, so dass, wenn der Angreifer eine andere Firmware auf das Board flasht, das Geheimnis gelöscht wird und Sie in der Lage sein werden, es zu erkennen, wenn Sie beginnen, den PIN-Code einzugeben - die Wortfolge wird anders sein.


### Generierung der Wiederherstellungsphrase


Dies ist einer der wichtigsten Teile des wallet - zu generate der Schlüssel sicher. Um dies gut zu tun, verwenden wir mehrere Quellen von Entropie:



- TRNG des Mikrocontrollers. Proprietär, zertifiziert und wahrscheinlich gut, aber wir trauen ihm nicht
- Touchscreen. Jedes Mal, wenn Sie den Bildschirm berühren, messen wir die Position und den Moment, in dem diese Berührung stattfand (in Mikrocontroller-Ticks bei 180 MHz).
- Eingebaute Mikrofone - noch nicht. Das Board hat zwei Mikrofone, so dass die Hardware wallet Ihnen zuhören und diese Daten in den Entropie-Pool mischen kann.


All diese Entropie wird zusammengehasht und in Ihre Wiederherstellungsphrase umgewandelt. Die resultierende Entropie ist immer besser als jede der einzelnen Quellen.


### Hochwertige Logik - Geldbörsen


Specter arbeitet als Schlüsselspeicher. Er enthält private HD-Schlüssel, die in Wallets eingebunden werden können. Wallets werden durch ihre Deskriptoren definiert. Wir unterstützen auch Miniscript.


Jeder wallet gehört zu einem bestimmten Netz. Das bedeutet, wenn Sie einen wallet in `testnet` importiert haben, wird er nicht in `mainnet` oder `regtest` verfügbar sein - Sie müssen zu diesem Netz wechseln und den wallet separat importieren.


### Überprüfung von Transaktionen


Die folgenden Regeln gelten für Transaktionen, die wallet unterzeichnen wird:



- wenn gemischte Eingaben von verschiedenen Geldbörsen gefunden werden, wird der Benutzer gewarnt ([Angriff](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- änderungsausgaben zeigen den Namen des wallet, an den sie gesendet werden
- um ein Multisig- oder Miniscript zu verwenden, müssen Sie zunächst den wallet importieren, indem Sie den wallet-Deskriptor hinzufügen (über QR, USB oder SD-Karte)


## Deskriptoren unterstützen


Alle normalen Bitcoin-Deskriptoren funktionieren. Darüber hinaus haben wir ein paar Erweiterungen:


### Mehrere Verzweigungen in Deskriptoren


Um etwas Platz in den QR-Codes zu sparen, erlauben wir das Hinzufügen von Deskriptoren mit mehreren Zweigen in einem Durchgang. Wenn Sie `wpkh(xpub/0/*)` für Empfangsadressen und `wpkh(xpub/1/*)` für Änderungsadressen verwenden möchten, können Sie diese in einem einzigen Deskriptor kombinieren: `wpkh(xpub/{0,1}/*)` - der wallet wird den ersten Index des `{}`-Satzteils als den Zweig für Empfangsadressen und den zweiten als Änderungsadressen behandeln.


Sie können auch mehr als zwei Verzweigungen angeben, und die Verzweigungsindizes können für verschiedene Mitunterzeichner unterschiedlich sein, so dass dieser Deskriptor zwar sehr seltsam, aber absolut gültig ist:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Hier verwendet der wallet für den Empfang der Adresse Nummer 17 das Skript von "wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3)").


Die einzige Voraussetzung ist, dass die Anzahl der Indizes in allen Gruppen gleich ist (3 im obigen Fall).


### Standardableitungen


Enthält der Deskriptor öffentliche Hauptschlüssel, aber keine Platzhalterableitungen, wird die Standardableitung `/{0,1}/*` zu allen erweiterten Schlüsseln im Deskriptor hinzugefügt. Wenn mindestens eine der xpubs eine Wildcard-Ableitung enthält, wird der Deskriptor nicht geändert.


Der Deskriptor `wpkh(xpub)` wird in `wpkh(xpub/{0,1}/*)` umgewandelt.


### Miniscript


Specter unterstützt Miniskripte, aber nicht die Kompilierung von Richtlinien zu Miniskripten (weil es viel zu teuer ist). Wir führen einige Überprüfungen des Miniskripts durch, so dass nur `B`-Skripte auf der obersten Ebene erlaubt sind und alle Argumente in Sub-Miniskripten die Eigenschaften gemäß [spec](http://bitcoin.sipa.be/miniscript/) haben müssen.


Sie können [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) verwenden, um einen Deskriptor aus einer Richtlinie zu generate und ihn dann in den wallet zu importieren.


Zum Beispiel kann eine Police "Ich kann jetzt ausgeben, oder in 100 Tagen kann meine Frau ausgeben" wie folgt in die wallet umgewandelt werden:


Richtlinie: `oder(9@pk(xpubA),and(older(14400),pk(B)))` (mein Schlüssel ist 9-mal wahrscheinlicher)


Miniscript: "or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`


Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))`


Da wir hier keine Wildcard-Ableitungen haben, werden die Standardableitungen von `/{0,1}/*` an die xpubs angehängt.



---

MIT-Lizenz


Copyright (c) 2019 cryptoadvance


---