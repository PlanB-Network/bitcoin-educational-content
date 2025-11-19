---
name: Satochip x SeedSigner
description: Wie kann ich einen Satochip mit meinem SeedSigner verwenden?
---

![cover](assets/cover.webp)



*Vielen Dank an [Crypto Guide](https://www.youtube.com/@CryptoGuide/) für die fork der SeedSigner-Firmware für Smartcard-Unterstützung, die wir in diesem Tutorial verwenden werden



---

Der Satochip ist eine Hardware im wallet-Smartcard-Format mit einem EAL6+-zertifizierten Sicherheitselement, einem der höchsten Sicherheitsstandards. Er wird vom gleichnamigen belgischen Unternehmen entwickelt und hergestellt: Satochip.



Mit einem Preis von rund 25 € hebt sich der Satochip durch sein hervorragendes Preis-Leistungs-Verhältnis von der Konkurrenz ab. Dank seines sicheren Chips bietet er Widerstand gegen physische Angriffe. Darüber hinaus ist der Quellcode des Applets vollständig quelloffen und unter der *AGPLv3* lizenziert.



Andererseits bringt sein Format einige funktionelle Einschränkungen mit sich. Der größte Nachteil des Satochip ist das Fehlen eines integrierten Bildschirms: Die Benutzer müssen daher Transaktionen blind unterschreiben und sich ausschließlich auf das Display ihres Computers verlassen.



Um diese Schwäche zu überwinden, ist eine besonders interessante Konfiguration die Verwendung in Verbindung mit einem SeedSigner. In diesem Fall findet die Kommunikation nicht mehr direkt zwischen dem Computer und dem Satochip statt, sondern über den Austausch von QR-Codes zwischen dem Computer und dem SeedSigner. Der SeedSigner fungiert dann als Vertrauensbildschirm: Er zeigt die zu signierenden Informationen an, während die Signatur selbst vom Satochip durchgeführt wird. Anders als bei der herkömmlichen Verwendung des SeedSigners (oder sogar der Verwendung in Kombination mit Seedkeeper) wird der seed nie in den SeedSigner geladen. Der SeedSigner wird somit zum Bildschirm des Satochip, wodurch die mit dem blinden Signieren verbundenen Risiken eliminiert werden.



Wenn wir das Problem andersherum betrachten, schließt die Verwendung des SeedSigners mit einem Satochip eine große Lücke im SeedSigner: die Möglichkeit, den seed innerhalb eines secure element zu speichern und zu verwenden.



Meiner Meinung nach bietet diese Konfiguration mehrere Vorteile gegenüber herkömmlichen Hardware-Geldbörsen:




- Der Satochip kostet etwa 25 €, und da das Applet Open-Source ist, können Sie es selbst auf einer leeren Smartcard installieren. Hinzu kommen die Kosten für die SeedSigner-Komponenten und die Erweiterung zum Lesen von Smartcards: Je nachdem, wo Sie diese Hardware kaufen, dürfte der Gesamtbetrag zwischen 70 und 100 € liegen.
- Die gesamte Software, die an der Einrichtung beteiligt ist, ist Open-Source: die SeedSigner-Firmware und das Satochip-Applet.
- Sie profitieren von einem zertifizierten Sicherheitselement.
- Die Konfiguration kann vollständig selbst vorgenommen werden, ohne auf Hardware zurückzugreifen, die ausdrücklich für die Verwendung von Bitcoin vorgesehen ist, was eine Form der plausiblen Bestreitbarkeit und der Resistenz gegenüber bestimmten externen Bedrohungen (einschließlich, je nach Land, staatlichen Drucks) bieten kann. Dies ist auch eine interessante Lösung, wenn der Zugang zu kommerziellen Hardware-Geldbörsen in Ihrer Region eingeschränkt oder unmöglich ist.




## 1. Erforderliche Materialien



Für diese Einrichtung benötigen Sie die folgenden Gegenstände:




- Die übliche Ausrüstung, die ein klassischer SeedSigner benötigt:
 - ein Raspberry Pi Zero mit GPIO-Pins,
 - 1.3" Waveshare-Bildschirm,
 - eine kompatible Kamera,
 - eine microSD-Karte.



![Image](assets/fr/01.webp)





- Das SeedSigner-Erweiterungskit, erhältlich [im offiziellen Satochip-Store](https://satochip.io/product/seedsigner-extension-kit/), mit dem Sie eine Smartcard direkt von Ihrem SeedSigner lesen und beschreiben können. Eine andere Möglichkeit ist die Verwendung [eines externen Smartcard-Lesegeräts](https://satochip.io/product/chip-card-reader/), das per Kabel an einen Micro-USB-Port des Raspberry Pi angeschlossen werden kann. Ich habe diese Lösung jedoch nicht selbst getestet;
- [Ein Satochip](https://satochip.io/product/satochip/) oder alternativ eine [leere Smartcard](https://satochip.io/product/card-for-diy-project/), auf der das Satochip-Applet installiert wird (das von Satochip verkaufte Erweiterungsset enthält bereits eine leere Smartcard). Das Erweiterungskit von Satochip unterstützt auch das Format [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/). Sie können sich also für dieses Format entscheiden, wenn Sie es bevorzugen.



![Image](assets/fr/02.webp)



Weitere Einzelheiten zur Ausrüstung, die für den Zusammenbau eines SeedSigners erforderlich ist, finden Sie in Teil 1 dieses anderen Tutorials:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Firmware installieren



Um Ihren SeedSigner mit einem Satochip zu verwenden, müssen Sie eine alternative Firmware installieren, die sich von der des ursprünglichen SeedSigners unterscheidet, um das Lesen von Chipkarten zu unterstützen. Hierfür empfehle ich fork von "**3rdIteration**" (https://github.com/3rdIteration/seedsigner). Laden Sie [die neueste Version des Images](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) herunter, die dem von Ihnen verwendeten Raspberry Pi-Modell entspricht.



![Image](assets/fr/03.webp)



Wenn Sie es noch nicht haben, laden Sie die Software [Balena Etcher] herunter (https://etcher.balena.io/) und gehen Sie dann wie folgt vor:




- Legen Sie die microSD-Karte in Ihren Computer ein;
- Etcher starten ;
- Wählen Sie die soeben heruntergeladene `.zip`-Datei aus;
- Wählen Sie die microSD-Karte als Ziel aus;
- Klicken Sie auf `Flash!`.



![Image](assets/fr/04.webp)



Warten Sie, bis der Vorgang abgeschlossen ist: Ihre microSD-Karte ist nun einsatzbereit. Sie können nun mit dem Zusammenbau Ihres Geräts fortfahren.



Weitere Einzelheiten zur Installation der Firmware und zur Überprüfung der Software (ein Schritt, den ich Ihnen dringend empfehle) finden Sie in der folgenden Anleitung:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Zusammenbau des Chipkartenlesers



Installieren Sie zunächst die Kamera am Raspberry Pi Zero, indem Sie sie vorsichtig in den Kamerastift einführen und mit der schwarzen Lasche verriegeln. Legen Sie dann den Pi auf die Unterseite des Gehäuses und achten Sie darauf, dass die Anschlüsse auf die entsprechenden Öffnungen ausgerichtet sind.



![Image](assets/fr/05.webp)



Verbinden Sie dann den Chipkartenleser mit den GPIO-Pins des Raspberry Pi Zero.



![Image](assets/fr/06.webp)



Schieben Sie die Kunststoffabdeckung über den Chipkartenleser, bis sie richtig positioniert ist.



![Image](assets/fr/07.webp)



Fügen Sie dann den Bildschirm zu den GPIO-Pins der Erweiterung hinzu.



![Image](assets/fr/08.webp)



Zum Schluss stecken Sie die microSD-Karte mit der Firmware in den seitlichen Anschluss des Raspberry Pi Zero.



![Image](assets/fr/09.webp)



Sie können Ihren SeedSigner nun entweder über den Micro-USB-Anschluss des Raspberry Pi Zero oder über den USB-C-Anschluss der Erweiterung anschließen. Beide Optionen funktionieren. Warten Sie ein paar Sekunden für den Start, dann sollten Sie den Willkommensbildschirm sehen.



![Image](assets/fr/10.webp)



Für weitere Details zur Ersteinrichtung Ihres SeedSigners empfehle ich Ihnen, Teil 4 des folgenden Tutorials zu lesen:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Flashen einer Smartcard mit dem Satochip-Applet (optional)



Wenn Sie bereits einen Satochip besitzen, können Sie diesen Schritt überspringen und direkt zu Schritt 4 übergehen. In diesem Abschnitt sehen wir uns an, wie man das Satochip-Applet auf einer leeren Smartcard installiert (DIY-Methode). Das Applet ist einfach ein kleines Programm, das auf der Smartcard läuft und es uns ermöglicht, bestimmte Funktionen zu verwalten.



Um loszulegen, öffnen Sie das Menü "Tools > Smartcard Tools" auf Ihrem SeedSigner.



![Image](assets/fr/11.webp)



Wählen Sie dann `DIY Tools > Applet installieren`.



![Image](assets/fr/12.webp)



Stecken Sie Ihre Smartcard mit dem Chip nach unten in das SeedSigner-Lesegerät und wählen Sie das "Satochip"-Applet.



![Image](assets/fr/13.webp)



Bitte haben Sie während der Installation etwas Geduld: der Vorgang kann einige zehn Sekunden dauern.



![Image](assets/fr/14.webp)



Wenn das Applet erfolgreich installiert wurde, können Sie mit Schritt 4 fortfahren.



![Image](assets/fr/15.webp)




## 5. Erstellen und Speichern von seed



### 5.1. seed generieren



Nun, da Ihre Hard- und Software ordnungsgemäß funktioniert, können Sie mit der Erstellung Ihres Bitcoin-Portfolios fortfahren. Schließen Sie dazu Ihren SeedSigner an und erstellen Sie dann Ihren seed wie bei einem herkömmlichen SeedSigner, indem Sie entweder würfeln oder ein Foto machen:




- Gehen Sie in das Menü "Werkzeuge > Kamera / Würfelwürfe";
- Dann folgen Sie dem Prozess der Entropieerzeugung entsprechend der gewählten Methode;
- Erstellen Sie abschließend eine Sicherungskopie des seed auf einem physischen Datenträger und überprüfen Sie die Sicherungskopie sorgfältig.



![Image](assets/fr/16.webp)



Wenn Sie die Einzelheiten dieses Verfahrens sehen möchten, folgen Sie bitte Teil 5 dieses Tutorials:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Speichern des seed auf einem Seedkeeper



Sobald der seed erzeugt wurde, ist dies die einzige Zeit, in der er sich im RAM des SeedSigners befindet. In meinem Fall möchte ich ihn auf einem [Seedkeeper](https://satochip.io/product/seedkeeper/) speichern, einem anderen Satochip-Produkt, das für die Speicherung von Geheimnissen entwickelt wurde. Ich werde dieses Gerät als letzten Ausweg verwenden, falls ich meinen Satochip verlieren sollte.



Die hier gewählte Sicherungsstrategie hängt von Ihren Präferenzen ab, aber es ist unbedingt erforderlich, mindestens eine Kopie Ihrer mnemotechnischen Phrase zu haben, entweder auf physischen Medien (Papier oder Metall) oder, wie hier, in einem Seedkeeper. Sie können die Anzahl der Sicherungskopien bei Bedarf auch vervielfachen. Für weitere Informationen über Portfolio-Backup-Strategien empfehle ich Ihnen, dieses Tutorial zu lesen:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Um Ihren seed auf einem Seedkeeper zu sichern, gehen Sie direkt zum Menü "Backup Seed".



![Image](assets/fr/17.webp)



Stecken Sie dann Ihren Seedkeeper in das Smartcard-Lesegerät und wählen Sie "Zum SeedKeeper".



![Image](assets/fr/18.webp)



Geben Sie Ihre PIN ein, um sie zu entsperren.



![Image](assets/fr/19.webp)



Wählen Sie ein `Label`, um Ihre verschiedenen auf Seedkeeper gespeicherten Geheimnisse leicht zu identifizieren. Sie können z. B. einfach das wallet-Impressum beibehalten oder ausdrücklich "Seed" angeben. Die Wahl hängt von Ihrer Vorliebe und Ihrem Risiko ab.



![Image](assets/fr/20.webp)



Wenn sich Ihre Sicherungsstrategie ausschließlich auf diesen Seedkeeper stützt, empfehle ich Ihnen dringend, jetzt einen leeren Wiederherstellungstest durchzuführen und dann die Fingerabdrücke zu vergleichen, um zu prüfen, ob die Sicherung funktioniert.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Der Seedkeeper-PIN-Code sollte so lang und zufällig wie möglich sein, um Brute-Force-Versuche im Falle einer physischen Kompromittierung der Karte zu verhindern. Sie sollten auch eine Sicherungskopie dieses PIN-Codes aufbewahren, die an einem anderen Ort als Seedkeeper gespeichert ist. Ohne diesen PIN-Code können Sie nicht auf die in Seedkeeper gespeicherte Mnemonik zugreifen, und Ihre Bitcoins sind dauerhaft verloren.



### 5.3. Speichern Sie seed auf dem Satochip



Nachdem Ihr Portfolio nun erstellt, gespeichert und verifiziert wurde, übertragen wir es auf den Satochip. Stellen Sie dazu sicher, dass der seed in den RAM des SeedSigners geladen ist. Gehen Sie dann zu "Tools > Smartcard Tools > Satochip Functions".



![Image](assets/fr/21.webp)



Stecken Sie Ihren Satochip in den Chipkartenleser und wählen Sie dann "Initialisierung mit Seed".



![Image](assets/fr/22.webp)



Das Gerät fordert Sie auf, den Satochip-PIN-Code einzugeben; da die Karte neu und nicht initialisiert ist, existiert noch keine PIN. Geben Sie einen beliebigen Code ein, um diesen Schritt zu überspringen (es handelt sich nicht um einen Sperrcode).



![Image](assets/fr/23.webp)



Der SeedSigner stellt fest, dass Ihr Satochip noch nicht initialisiert wurde. Klicken Sie zur Bestätigung auf "Ich habe verstanden".



![Image](assets/fr/24.webp)



Sie können dann den Satochip-PIN-Code mit 4 bis 16 Zeichen einstellen. Um die Sicherheit Ihres wallet zu erhöhen, wählen Sie einen langen, zufälligen Code: Er ist der einzige Schutz gegen den physischen Zugriff auf Ihre Gedächtnisstütze.



Denken Sie daran, diese PIN zu speichern, sobald sie erstellt ist, entweder in einem sicheren Passwort-Manager oder auf einem physischen Medium, je nach Ihrer persönlichen Strategie. Im letzteren Fall sollten Sie den Datenträger mit der PIN niemals am selben Ort wie Ihren Satochip aufbewahren, da der Schutz sonst nutzlos wird. Es ist wichtig, eine Sicherungskopie zu haben: **Ohne diese PIN können Sie nicht auf Ihren seed zugreifen und Ihre Bitcoins sind für immer verloren**.



![Image](assets/fr/25.webp)



Der SeedSigner fragt Sie dann, welche seed in den Satochip importiert werden sollen. Wählen Sie denjenigen aus, dessen Fingerabdruck mit dem soeben erstellten Portfolio übereinstimmt.



![Image](assets/fr/26.webp)



Ihr seed wird nun in den Satochip importiert.



![Image](assets/fr/27.webp)



Sie können Ihren SeedSigner jetzt ausschalten.



Wenn Sie ein passphrase BIP39 verwenden möchten, um die Sicherheit Ihres wallet zu erhöhen, lesen Sie bitte Teil 6 dieses Tutorials:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. wallet in Sparrow importieren



Nachdem Ihr Portfolio nun eingerichtet ist, importieren wir seine öffentlichen Informationen (den "*Keystore*") in Sparrow Wallet oder eine andere Portfolioverwaltungssoftware. Diese Software wird zur Erstellung, Verteilung und Verfolgung Ihrer Transaktionen verwendet. Allerdings kann sie diese nicht signieren, da nur der Satochip (und etwaige Sicherungskopien) die für diesen Vorgang erforderlichen privaten Schlüssel enthält.



### 6.1 Vorbereiten des SeedSigners und des Satochip



Legen Sie die microSD-Karte mit dem Betriebssystem ein und schalten Sie dann Ihren SeedSigner ein. Im Moment kann er noch nichts tun, da er Ihren seed noch nicht kennt. Sie müssen zunächst den Satochip in den Chipkartenleser einführen, da sich auf diesem Ihr seed befindet.



Rufen Sie auf dem Startbildschirm das Menü "Tools > Smartcard Tools > Satochip Functions" auf.



![Image](assets/fr/28.webp)



Klicken Sie dann auf "Xpub exportieren".



![Image](assets/fr/29.webp)



Wählen Sie den Portfoliotyp. In unserem Fall handelt es sich um ein Einzelportfolio: Wählen Sie "Single Sig".



![Image](assets/fr/30.webp)



Als nächstes kommt die Wahl des Skripting-Standards. Wählen Sie den neuesten: "Native SegWit".



![Image](assets/fr/31.webp)



Wählen Sie schließlich den "Koordinator", d. h. die Portfolioverwaltungssoftware, die Sie verwenden möchten. In diesem Fall werden wir Sparrow Wallet verwenden.



![Image](assets/fr/32.webp)



Es erscheint eine Warnmeldung: Das ist völlig normal. Der erweiterte öffentliche Schlüssel (`xpub`) ermöglicht es Ihnen, alle von Ihrem seed (auf dem ersten Konto) abgeleiteten Adressen einzusehen. Er gewährt jedoch keinen Zugang zu Ihrem Guthaben: Seine Offenlegung würde Ihre Privatsphäre gefährden, aber nicht die Sicherheit Ihrer Bitcoins. Mit anderen Worten: Sie können Ihr Guthaben einsehen, aber nicht ausgeben.



Klicken Sie auf "Ich verstehe".



![Image](assets/fr/33.webp)



Geben Sie dann den PIN-Code Ihres Satochip ein, um ihn zu entsperren. Dies ist der Code, den Sie in Schritt 5 festgelegt und gespeichert haben.



![Image](assets/fr/34.webp)



Klicken Sie abschließend auf "Xpub exportieren", wenn Sie mit den angezeigten Informationen zufrieden sind.



![Image](assets/fr/35.webp)



Der SeedSigner erzeugt dann Ihr xpub in Form eines dynamischen QR-Codes, der alle Daten enthält, die Sie für die Verwaltung Ihres Portfolios in Sparrow Wallet benötigen. Sie können die Helligkeit des Bildschirms mit dem Joystick einstellen, um das Scannen des QR-Codes zu erleichtern.



### 6.2 Importieren eines neuen Portfolios in Sparrow Wallet



Stellen Sie sicher, dass die Software Sparrow Wallet auf Ihrem Computer installiert ist. Wenn Sie nicht wissen, wie Sie die Software herunterladen, ihre Echtheit überprüfen und sie richtig installieren, lesen Sie unsere vollständige Anleitung zu diesem Thema:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Öffnen Sie auf Ihrem Computer Sparrow Wallet, und klicken Sie dann in der Menüleiste auf "Datei → Wallet importieren".



![Image](assets/fr/36.webp)



Scrollen Sie nach unten zu "SeedSigner" und wählen Sie "Scannen...". Ihre Webcam wird aktiviert: Scannen Sie den dynamischen QR-Code, der auf dem Bildschirm Ihres SeedSigners angezeigt wird.



![Image](assets/fr/37.webp)



Vergeben Sie einen Namen für Ihr Portfolio und klicken Sie dann auf "Wallet erstellen". Sparrow fordert Sie dann auf, ein Passwort festzulegen, um den lokalen Zugang zu diesem wallet zu sperren. Wählen Sie ein starkes Passwort: Es schützt Ihre Daten in Sparrow (öffentliche Schlüssel, Adressen, Etiketten und Transaktionshistorie). Dieses Passwort ist jedoch nicht erforderlich, um den wallet in Zukunft wiederherzustellen: nur Ihre mnemonische Phrase (und möglicherweise Ihr passphrase) wird benötigt.



Ich empfehle Ihnen, dieses Passwort in einem Passwort-Manager zu speichern, um es nicht zu verlieren.



![Image](assets/fr/38.webp)



Ihr Keystore wurde erfolgreich importiert.



![Image](assets/fr/39.webp)



Prüfen Sie nun, ob der in Sparrow Wallet angezeigte "Master-Fingerabdruck" mit dem zuvor auf Ihrem SeedSigner gefundenen übereinstimmt.



Der SeedSigner fordert Sie dann auf, eine zufällige Empfangsadresse von Ihrem Sparrow wallet zu scannen, um die Gültigkeit des Imports zu bestätigen.



![Image](assets/fr/40.webp)



Ihr Satochip (über SeedSigner) und Ihr Sparrow Wallet sind nun sicher miteinander verbunden. Der Sparrow fungiert als vollständige Verwaltungsschnittstelle, während der Satochip das einzige Gerät bleibt, das Ihre Transaktionen signieren kann. Sie sind jetzt bereit, Bitcoins in einer völlig luftdichten Konfiguration zu empfangen und zu senden.



![Image](assets/fr/41.webp)



## 7. Empfangen und Senden von Bitcoins



Ihr Satochip und Ihr Sparrow Wallet sind jetzt so konfiguriert, dass sie zusammenarbeiten. In diesem Abschnitt erklären wir Ihnen Schritt für Schritt, wie Sie in diesem Modus Bitcoins empfangen und senden können.



### 7.1 Empfang von Bitcoins



#### 7.1.1 Generierung einer Empfangsadresse



Öffnen Sie auf Ihrem Computer Sparrow Wallet und entsperren Sie Ihren `Satochip-SeedSigner` wallet mit Ihrem Passwort. Stellen Sie sicher, dass die Software mit einem Server verbunden ist (Anzeige unten rechts). Klicken Sie dann in der Seitenleiste auf `Empfangen`.



![Image](assets/fr/42.webp)



Es erscheint eine neue Bitcoin-Adresse. Sie finden:




- Die Adresse im Textformat (beginnend mit `bc1q...`, wenn Sie P2WPKH verwenden, wie in diesem Beispiel) ;
- Der zugehörige QR-Code ;
- Ein Feld "Bezeichnung", das für die Rückverfolgung Ihrer Transaktionen nützlich ist.



Ich empfehle Ihnen dringend, jede Bitcoin-Quittung in Ihrem wallet mit einem Etikett zu versehen. Dies wird Ihnen helfen, die Herkunft jedes UTXO leicht zu identifizieren und Ihre Privatsphäre besser zu verwalten. Wenn Sie mehr über dieses wichtige Thema erfahren möchten, sehen Sie sich die spezielle Schulung auf der Plan ₿ Academy an:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Um ein Etikett hinzuzufügen, geben Sie einfach einen Namen in das Feld "Etikett" ein und bestätigen dann.



Zum Beispiel:



```txt
Label : Sale of the Raspberry Pi Zero
```



Ihre Adresse ist nun in allen Sparrow-Abschnitten mit diesem Label verknüpft.



![Image](assets/fr/43.webp)



#### 7.1.2 Address-Überprüfung auf dem SeedSigner



Bevor Sie dem Zahlungspflichtigen Ihre Empfangsadresse mitteilen, müssen Sie überprüfen, ob sie zu Ihrem seed gehört. Dieser Schritt stellt sicher, dass Ihr Satochip dann in der Lage ist, Transaktionen zu unterzeichnen, die mit dieser Adresse verbunden sind. Er verhindert auch potenzielle Angriffe, bei denen Sparrow eine betrügerische Adresse anzeigen würde. Bedenken Sie, dass Sparrow in einer unsicheren Umgebung (Ihrem Computer) läuft, deren Angriffsfläche viel größer ist als die Ihres Satochip, der völlig isoliert ist. Aus diesem Grund sollten Sie den in Sparrow angezeigten Adressen niemals blind vertrauen, bevor Sie sie nicht auf Ihrer wallet-Hardware überprüft haben.



Klicken Sie im Sparrow auf den QR-Code der Adresse, um ihn zu vergrößern: Er wird dann bildschirmfüllend angezeigt.



![Image](assets/fr/44.webp)



Stecken Sie den Satochip auf Ihrem SeedSigner in das Lesegerät und wählen Sie dann im Hauptmenü "Scannen". Scannen Sie den auf Ihrem Computer angezeigten QR-Code und wählen Sie dann "Satochip-Karte verwenden".



![Image](assets/fr/45.webp)



Bestätigen Sie dann den Typ des verwendeten Skripts (in diesem Fall "Native SegWit"), geben Sie den Satochip-PIN-Code ein, um es zu entsperren, und bestätigen Sie die "xpub"-Informationen.



![Image](assets/fr/46.webp)



Wenn die gescannte Adresse mit der von Ihrem seed übereinstimmt, zeigt der SeedSigner die Meldung an: gW-67 Verifiziert".



![Image](assets/fr/47.webp)



So können Sie sicher sein, dass die Adresse zu Ihrem Portfolio gehört.



#### 7.1.3 Erhalt der Mittel



Sie können diese Adresse nun in Textform oder über den QR-Code an die Person oder Abteilung übermitteln, die Ihnen Satss senden muss. Sobald die Transaktion im Netz übertragen wurde, erscheint sie auf der Registerkarte "Transaktionen" des Sparrow Wallet.



![Image](assets/fr/48.webp)



### 7.2 Bitcoins senden



Das Versenden von Bitcoins mit der Satochip-SeedSigner-Konfiguration umfasst 3 Schritte:




- Erstellung von Vorgängen in Sparrow ;
- Unterzeichnung dieser Transaktion auf dem Satochip über den SeedSigner ;
- Schließlich wird die Transaktion von Sparrow über das Netz übertragen.



Der gesamte Austausch zwischen den beiden Geräten findet ausschließlich über QR-Codes statt.



#### 7.2.1 Anlegen der Transaktion in Sparrow



In Sparrow Wallet können Sie eine Transaktion erstellen, indem Sie auf die Registerkarte "Senden" in der linken Seitenleiste klicken. Ich ziehe es jedoch vor, die Registerkarte "UTXOs" zu verwenden, mit der Sie die *Coin-Kontrolle* ausüben können. Diese Methode bietet eine genaue Kontrolle über die ausgegebenen UTXOs, um die Informationen zu begrenzen, die während Ihrer Transaktionen preisgegeben werden.



Wählen Sie auf der Registerkarte "UTXOs" die Münzen aus, die Sie ausgeben möchten, und klicken Sie dann auf "Ausgewählte senden".



![Image](assets/fr/49.webp)



Füllen Sie dann die Transaktionsfelder aus:




- Fügen Sie unter "Bezahlen an" die Adresse des Empfängers ein oder scannen Sie den QR-Code des Empfängers mit dem Kamerasymbol;
- Fügen Sie unter "Etikett" ein Etikett hinzu, um diese Ausgabe zu verfolgen;
- Geben Sie unter "Betrag" den zu überweisenden Betrag ein;
- Wählen Sie schließlich den Ladetarif entsprechend den aktuellen Netzbedingungen (Schätzungen finden Sie unter [mempool.space](https://mempool.space/)).



Wenn Sie alle Felder ausgefüllt haben, überprüfen Sie die Informationen sorgfältig und klicken Sie dann auf "Transaktion erstellen >>".



![Image](assets/fr/50.webp)



Überprüfen Sie die Transaktionsdetails ein letztes Mal auf ihre Richtigkeit und klicken Sie dann auf "Transaktion zur Unterzeichnung abschließen".



![Image](assets/fr/51.webp)



Die Transaktion ist nun fertig, wurde aber noch nicht unterzeichnet. Um den [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) als QR-Code anzuzeigen, klicken Sie auf "QR anzeigen".



![Image](assets/fr/52.webp)



#### 7.2.2 Unterzeichnung der Transaktion mit Satochip



Schalten Sie Ihren SeedSigner ein und setzen Sie Ihren Satochip wie gewohnt ein. Wählen Sie auf dem Startbildschirm "Scannen" und scannen Sie dann den auf dem Sparrow angezeigten QR-Code.



![Image](assets/fr/53.webp)



Wählen Sie die Option "Satochip-Karte verwenden".



![Image](assets/fr/54.webp)



Geben Sie Ihren PIN-Code ein, um die Smartcard zu entsperren.



![Image](assets/fr/55.webp)



Der SeedSigner erkennt, dass es sich um einen PSBT handelt und zeigt eine Zusammenfassung der Transaktion an:




   - Der gesendete Betrag,
   - Zieladressen,
   - Damit verbundene Transaktionskosten.



Klicken Sie auf "Details überprüfen" und überprüfen Sie alle Informationen direkt auf dem Bildschirm von SeedSigner. Die wichtigsten zu prüfenden Punkte sind die gesendeten Beträge, die Zieladressen und die Transaktionsgebühren.



![Image](assets/fr/56.webp)



Wenn alles in Ordnung ist, wählen Sie "PSBT genehmigen", um die Transaktion mit dem Satochip zu unterzeichnen.



![Image](assets/fr/57.webp)



Sobald die Signatur abgeschlossen ist, erzeugt der SeedSigner einen neuen QR-Code, der die signierte Transaktion enthält und vom Sparrow gescannt werden kann.



#### 7.2.3 Übermittlung der Transaktion vom Sparrow



Nun, da die Transaktion signiert und validiert ist, muss sie nur noch in das Bitcoin-Netzwerk übertragen werden, damit ein Miner sie in einen Block aufnehmen kann. In Sparrow klicken Sie auf "QR scannen".



![Image](assets/fr/58.webp)



Halten Sie den auf Ihrem SeedSigner angezeigten QR-Code (der die signierte Transaktion enthält) vor die Webcam. Sparrow zeigt dann alle Transaktionsdetails an. Überprüfen Sie, ob alle Informationen korrekt sind, und klicken Sie dann auf "Transaktion senden", um sie im Bitcoin-Netzwerk zu übertragen.



![Image](assets/fr/59.webp)



Ihre Transaktion wird nun an das Netzwerk übertragen. Sie können die Bestätigung auf der Registerkarte "Transaktionen" des Sparrow Wallet verfolgen.



![Image](assets/fr/60.webp)



## 8. Holen Sie sich Ihren wallet zurück



Wie wir in den vorangegangenen Abschnitten gesehen haben, gibt es je nach Ihrer Sicherheitsstrategie mehrere Möglichkeiten, Ihre Wiederherstellungsphrase zusätzlich zu Ihrem Satochip zu sichern:




- Verwendung eines klassischen *SeedQR* mit dem SeedSigner ;
- Durch Aufzeichnung der mnemotechnischen Phrase auf einem physischen Medium;
- Oder durch Speicherung auf einem Seedkeeper, wie in Abschnitt 5.2 erläutert.



In jedem Fall gibt es 2 Hauptsituationen, in denen Sie eingreifen müssen: Verlust des Satochips oder Verlust des SeedSigners. Schauen wir uns an, wie man in jedem dieser Szenarien reagieren sollte.



### 8.1. Rufen Sie Ihren wallet mit Satochip ab



Wenn Sie Ihren Satochip noch haben, Ihr SeedSigner aber kaputt oder verloren gegangen ist, ist die Situation relativ einfach zu handhaben, da Ihr wallet noch im Satochip ist.



Die beste Option ist, die notwendigen Komponenten zu empfehlen und einen neuen SeedSigner von Grund auf neu zu bauen. Da es sich um ein "zustandsloses" Gerät handelt, spielt es keine Rolle, ob Sie denselben oder einen anderen SeedSigner verwenden: Solange Sie Ihren Satochip einstecken können, wird alles normal funktionieren.



Wenn Sie keinen neuen bauen wollen, können Sie Ihren Satochip auch auf die klassische Weise verwenden, d.h. direkt von Ihrem Computer aus, ohne den SeedSigner zu benutzen. Diese Methode funktioniert einwandfrei, verringert aber die Sicherheit Ihres Bitcoin wallet beträchtlich: Sie verlieren die "*air-gapped*"-Isolierung und müssen nun blind unterschreiben, da der SeedSigner als vertrauenswürdiger Bildschirm fungierte. Im Notfall oder wenn Sie nicht in der Lage sind, einen SeedSigner neu zu bauen, kann dies jedoch eine vorübergehende Lösung sein.



Dazu benötigen Sie ein USB-Smartcard- oder NFC-Lesegerät. Öffnen Sie das wallet, das Sie wiederherstellen möchten, im Sparrow, gehen Sie dann auf die Registerkarte "Einstellungen" und klicken Sie auf "Ersetzen".



![Image](assets/fr/61.webp)



Stecken Sie Ihren Satochip in das an den Computer angeschlossene Chipkartenlesegerät und klicken Sie dann auf "Importieren" neben "Satochip".



![Image](assets/fr/62.webp)



Geben Sie schließlich Ihre Smartcard-PIN ein, um sie zu entsperren. Sie können dann auf Ihre wallet zugreifen, Transaktionen erstellen und sie direkt mit dem angeschlossenen Satochip unterschreiben.



### 8.2. Rufen Sie Ihr Portfolio mit SeedSigner ab



Das andere, heiklere Szenario ist, wenn Sie den Zugang zu Ihrem Satochip mit dem seed verlieren: sei es, dass er kaputt, verloren oder gestohlen wurde oder dass Sie seinen PIN-Code vergessen haben. Wenn Ihr Satochip gestohlen oder verlegt wurde, empfehlen wir Ihnen dringend, Ihre Bitcoins sofort auf einen brandneuen wallet zu übertragen, der mit einem anderen seed generiert wurde, sobald Sie wieder Zugriff auf Ihr Geld haben. Dadurch wird sichergestellt, dass ein potenzieller Angreifer niemals Zugang zu Ihrem Satochip erhalten kann.



Um wieder Zugriff auf Ihr Portfolio zu erhalten und Ihre Gelder zu verschieben, laden Sie einfach Ihren seed in SeedSigner. Je nachdem, welche Sicherungsmedien Sie verwendet haben, haben Sie mehrere Möglichkeiten:





- Geben Sie Ihre mnemonische Phrase manuell im Menü `Samen > 12-Wort seed eingeben` ein.



![Image](assets/fr/63.webp)





- Scannen Sie Ihren *SeedQR*, indem Sie auf die Schaltfläche "Scannen" auf der Startseite klicken.



![Image](assets/fr/64.webp)





- Oder laden Sie Ihren seed von einem Seedkeeper über das Menü "Seeds > From SeedKeeper" (dies ist die Methode, die ich in diesem Tutorial verwende). Sie müssen lediglich die Seedkeeper-PIN eingeben und das Geheimnis auswählen, das als seed auf dem SeedSigner verwendet werden soll.



![Image](assets/fr/65.webp)



Sobald der seed in den SeedSigner geladen wurde, können Sie unabhängig von der von Ihnen verwendeten Methode eine oder mehrere Scan-Transaktionen unterzeichnen, um Ihre Bitcoins auf einen neuen, nicht kompromittierten wallet zu übertragen. Um herauszufinden, wie das geht, lesen Sie Teil 7.2 des folgenden Tutorials:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Jetzt wissen Sie, wie Sie Satochip nutzen können, um Ihr Bitcoin-Portfolio in Kombination mit SeedSigner sicher zu verwalten.



Wenn Sie dieser Aufbau überzeugt hat, zögern Sie nicht, die Projekte zu unterstützen, die dies möglich machen:




- Indem Sie Ihr Gerät direkt [auf der Satochip-Website] kaufen (https://satochip.io/shop/);
- Durch [eine Spende an das SeedSigner-Projekt](https://seedsigner.com/donate/);
- Indem Sie den YouTube-Kanal von [Crypto Guide](https://www.youtube.com/@CryptoGuide/) abonnieren, der von der Person betrieben wird, die das GitHub-Repository verwaltet, in dem sich die modifizierte Firmware befindet, die wir in dieser Anleitung verwendet haben.