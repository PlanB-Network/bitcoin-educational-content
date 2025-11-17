---
name: Seedkeeper x SeedSigner
description: Wie verwende ich Seedkeeper mit meinem SeedSigner?
---

![cover](assets/cover.webp)



*Danke an das [Satochip](https://satochip.io/) Team für die Zustimmung zur Wiederverwendung [ihrer Videos](https://www.youtube.com/@satochip/videos) in diesem Tutorial. Dank auch an [Crypto Guide](https://www.youtube.com/@CryptoGuide/) für seine fork der SeedSigner-Firmware, die Unterstützung für Smartcards ermöglicht



---

Der SeedSigner ist eine wallet-Hardware, die Sie selbst aus Standardhardware zusammenbauen, in der Regel aus einem Raspberry Pi Zero. Dieser wallet wird als "*zustandslos*" bezeichnet: Im Gegensatz zu den meisten anderen Modellen auf dem Markt (Coldcard, Trezor, Ledger, usw.) speichert er keine Daten im permanenten Speicher und arbeitet nur live aus dem RAM. Folglich wird der seed Ihres Portfolios niemals auf dem SeedSigner gespeichert. Bei jedem Neustart müssen Sie ihn ausfüllen, damit das Gerät Ihre Transaktionen signieren kann. Die gebräuchlichste Methode ist es, Ihren seed als QR-Code zu speichern, den Sie dann jedes Mal scannen, wenn Sie ihn benutzen (*SeedQR*).



Dieser Ansatz birgt jedoch ein erhebliches Risiko: Der seed muss im Klartext zugänglich bleiben, damit er gescannt werden kann. Im Falle eines Diebstahls oder Eindringens könnte ein Angreifer ihn leicht in die Hände bekommen und Ihre Bitcoins stehlen.



Um diese Schwäche zu überwinden, kann SeedSigner mit [**Seedkeeper**] (https://satochip.io/product/seedkeeper/), einer von Satochip entwickelten Smartcard, kombiniert werden. Damit können mnemonische Phrasen (oder andere Geheimnisse) in einem secure element gespeichert werden, der durch einen PIN-Code geschützt ist. Das Seedkeeper-Applet ist quelloffen, und sein secure element ist EAL6+-zertifiziert. In Verbindung mit SeedSigner bietet es ein sehr interessantes Sicherheitsmerkmal: Ihre Schlüssel werden vollständig offline verwaltet, Sie signieren Ihre Transaktionen auf einem vertrauenswürdigen Bildschirm, und der seed ist physisch in einer Smartcard geschützt, die gegen physische Angriffe resistent ist.



Um die Installation abzuschließen, benötigen Sie lediglich die folgenden Komponenten:




- Die übliche Ausrüstung für einen klassischen SeedSigner: ein Raspberry Pi Zero, ein Waveshare 1,3"-Bildschirm, eine kompatible Kamera und eine microSD-Karte (weitere Details finden Sie im SeedSigner-Tutorial unten);
- Das SeedSigner-Erweiterungskit, erhältlich [im offiziellen Satochip-Store] (https://satochip.io/product/seedsigner-extension-kit/), mit dem Sie die Smartcard direkt von Ihrem SeedSigner lesen und beschreiben können. Eine andere Möglichkeit ist die Verwendung eines externen Smartcard-Lesegeräts, das per Kabel an einen Micro-USB-Port des Raspberry Pi angeschlossen werden kann. Ich habe diese Lösung jedoch nicht selbst getestet;
- Einen Seedkeeper oder alternativ eine leere Smartcard, auf der das Seedkeeper-Applet installiert werden kann (das von Satochip verkaufte Erweiterungspaket enthält bereits eine leere Smartcard).



![Image](assets/fr/01.webp)



Dieser Lehrgang behandelt zwei Szenarien:




- Wenn Sie bereits ein Bitcoin-Portfolio haben, das über Ihren SeedSigner verwaltet wird, installieren Sie einfach die neue Firmware. Sie können dann Ihr vorhandenes wallet weiter verwenden, diesmal aber mit Seedkeeper für zusätzliche Sicherheit.
- Wenn Sie noch keinen Bitcoin wallet mit Ihrem SeedSigner verbunden haben, müssen Sie die Schritte **5** und **6** des unten genannten Tutorials befolgen. In diesen Abschnitten wird erklärt, wie man einen generate mit dem SeedSigner verbindet, ihn über eine *SeedQR* speichert und dann diesen wallet mit Sparrow Wallet verbindet, um ihn zu verwalten. Ich werde hier nicht auf diese Prozeduren eingehen, und **ich gehe davon aus, dass Sie bereits ein funktionierendes Bitcoin wallet haben, das mit Sparrow und Ihrem SeedSigner konfiguriert ist**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Firmware installieren



Um Ihren SeedSigner mit einem Seedkeeper zu verwenden, müssen Sie eine alternative Firmware installieren, die sich von der des ursprünglichen SeedSigners unterscheidet, um das Lesen von Chipkarten zu unterstützen. Hierfür empfehle ich die fork von "*3rdIteration*" (https://github.com/3rdIteration/seedsigner). Laden Sie [die neueste Version des Images](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) herunter, die dem von Ihnen verwendeten Raspberry Pi-Modell entspricht.



![Image](assets/fr/02.webp)



Wenn Sie es noch nicht haben, laden Sie die Software [Balena Etcher] herunter (https://etcher.balena.io/) und gehen Sie dann wie folgt vor:




- Legen Sie die microSD-Karte in Ihren Computer ein;
- Etcher starten ;
- Wählen Sie die soeben heruntergeladene `.zip`-Datei aus;
- Wählen Sie die microSD-Karte als Ziel aus;
- Klicken Sie auf `Flash!`.



![Image](assets/fr/03.webp)



Warten Sie, bis der Vorgang abgeschlossen ist: Ihre microSD-Karte ist nun einsatzbereit. Sie können nun mit dem Zusammenbau Ihres Geräts fortfahren.



Weitere Einzelheiten zur Installation der Firmware und zur Überprüfung der Software (ein Schritt, den ich Ihnen dringend empfehle) finden Sie in der folgenden Anleitung:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Zusammenbau des Chipkartenlesers



![video](https://youtu.be/jqE8HDMCImA)



Installieren Sie zunächst die Kamera am Raspberry Pi Zero, indem Sie sie vorsichtig in den Kamerastift einführen und mit der schwarzen Lasche verriegeln. Legen Sie dann den Pi auf die Unterseite des Gehäuses und achten Sie darauf, dass die Anschlüsse auf die entsprechenden Öffnungen ausgerichtet sind.



![Image](assets/fr/04.webp)



Verbinden Sie dann den Chipkartenleser mit den GPIO-Pins des Raspberry Pi Zero.



![Image](assets/fr/05.webp)



Schieben Sie die Kunststoffabdeckung über den Chipkartenleser, bis sie richtig positioniert ist.



![Image](assets/fr/06.webp)



Fügen Sie dann den Bildschirm zu den GPIO-Pins der Erweiterung hinzu.



![Image](assets/fr/07.webp)



Zum Schluss stecken Sie die microSD-Karte mit der Firmware in den seitlichen Anschluss des Raspberry Pi Zero.



![Image](assets/fr/08.webp)



Sie können Ihren SeedSigner nun entweder über den Micro-USB-Anschluss des Raspberry Pi Zero oder über den USB-C-Anschluss der Erweiterung anschließen. Beide Optionen funktionieren. Warten Sie ein paar Sekunden für den Start, dann sollten Sie den Willkommensbildschirm sehen.



![Image](assets/fr/09.webp)



Für weitere Details zur Ersteinrichtung Ihres SeedSigners empfehle ich Ihnen das folgende Tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Flashen einer Smartcard mit dem Seedkeeper-Applet (optional)



![video](https://youtu.be/NF4HemyEcOY)



Wenn Sie bereits einen Seedkeeper besitzen, können Sie diesen Schritt überspringen und direkt zu Schritt 4 übergehen. In diesem Abschnitt sehen wir uns an, wie Sie das Seedkeeper-Applet auf einer leeren Smartcard installieren (DIY-Methode).



Um loszulegen, öffnen Sie das Menü "Tools > Smartcard Tools" auf Ihrem SeedSigner.



![Image](assets/fr/10.webp)



Wählen Sie dann `DIY Tools > Applet installieren`.



![Image](assets/fr/11.webp)



Stecken Sie Ihre Smartcard mit dem Chip nach unten in das SeedSigner-Lesegerät und wählen Sie dann das Applet "SeedKeeper".



![Image](assets/fr/12.webp)



Bitte haben Sie während der Installation etwas Geduld: der Vorgang kann einige zehn Sekunden dauern.



![Image](assets/fr/13.webp)



Wenn das Applet erfolgreich installiert wurde, können Sie mit Schritt 4 fortfahren.



![Image](assets/fr/14.webp)



## 4. Einen bestehenden SeedQR auf Seedkeeper speichern



![video](https://youtu.be/X-vmFHU9Ec8)



Jetzt, wo Ihr Seedkeeper betriebsbereit ist, können Sie Ihre Bitcoin wallet Mnemonik auf der Smartcard speichern. Um zu beginnen, schalten Sie Ihren SeedSigner wie gewohnt ein und scannen dann den *SeedQR* Ihres wallet, um ihn in das Gerät zu laden. Sobald der seed importiert wurde, wählen Sie einfach "Fertig".



![Image](assets/fr/15.webp)



Wenn der seed geladen ist, rufen Sie das Menü "Backup Seed" auf.



![Image](assets/fr/16.webp)



Legen Sie dann Ihren Seedkeeper in das SeedSigner-Laufwerk ein und wählen Sie die Option "Zum SeedKeeper".



![Image](assets/fr/17.webp)



Der SeedSigner wird Sie dann auffordern, einen PIN-Code für Ihren Seedkeeper einzugeben. Da es sich um eine leere Karte handelt, ist noch kein Code definiert worden. Geben Sie einen beliebigen Code ein, um diesen Schritt zu überspringen, und bestätigen Sie dann.



![Image](assets/fr/18.webp)



SeedSigner erkennt, dass Seedkeeper noch nicht initialisiert wurde (d. h. es wurde kein Passwort festgelegt). Klicken Sie auf "Ich habe verstanden", um fortzufahren.



![Image](assets/fr/19.webp)



Wählen Sie nun den neuen PIN-Code Ihres Seedkeepers, der zwischen 4 und 16 Zeichen lang ist. Für zusätzliche Sicherheit wählen Sie einen langen, zufälligen Code: Er ist die einzige Barriere, die den physischen Zugang zu Ihrer mnemonischen Phrase schützt.



Denken Sie daran, diese PIN zu speichern, sobald sie erstellt ist, entweder in einem zuverlässigen Passwortmanager oder auf einem separaten physischen Medium, je nach Ihrer Strategie. Im letzteren Fall sollten Sie das Medium mit der PIN niemals am selben Ort aufbewahren wie Ihren Seedkeeper, da der Schutz sonst unwirksam wird. Es ist wichtig, eine Sicherungskopie zu haben: **Ohne diese PIN können Sie nicht auf Ihren seed zugreifen und Ihre Bitcoins sind verloren**.



![Image](assets/fr/20.webp)



Sie können dann ein `Label` definieren, das mit Ihrer mnemonischen Phrase verbunden ist. Dieses Label ist nützlich, wenn Sie mehrere Geheimnisse auf Seedkeeper speichern, damit Sie sie leicht identifizieren können.



![Image](assets/fr/21.webp)



Ihr Merksatz ist nun auf der Smartcard gespeichert.



![Image](assets/fr/22.webp)



In Bezug auf die Sicherheitsstrategie sind mehrere Ansätze möglich, je nach Ihren Bedürfnissen und dem Grad der Risikoexposition. Ich persönlich empfehle, dass Sie mindestens 2 Kopien Ihrer seed aufbewahren:




- Dies ist eine Premiere für Smartcards, die Sie für alltägliche Vorgänge, wie die Überprüfung von Adressen oder die Unterzeichnung von Transaktionen, leicht zugänglich halten können. Diese Methode ist praktisch (wie wir in Teil 5 sehen werden) und bleibt dank des Schutzes durch den PIN-Code sicher, so dass Sie sie ohne großes Risiko zugänglich halten können;
- Eine zweite Kopie Ihrer unverschlüsselten mnemonischen Phrase, die als ultimative Sicherung Ihres Portfolios dient und nur bei Verlust oder Diebstahl des Seedkeepers zu verwenden ist. Da diese Version unverschlüsselt ist, muss sie an einem separaten, sichereren Ort aufbewahrt werden, um eine gleichzeitige Kompromittierung der beiden Backups zu verhindern.



Je nach Ihrer Schutzstrategie und Ihrem Risikoprofil können Sie die seed auch auf mehreren verschiedenen Seedkeepern duplizieren oder mehrere physische Kopien der Gedächtnisstütze erstellen. Wenn Sie mehr über diese Praktiken erfahren möchten, schauen Sie sich den folgenden Leitfaden an:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Laden eines seed von Seedkeeper



![video](https://youtu.be/ms0Iq_IyaoE)



Sie können nun Ihren Seedkeeper verwenden, um Ihre mnemonische Phrase beim Start in den SeedSigner zu laden und so Ihre Bitcoin Transaktionen zu signieren. Um zu beginnen, schalten Sie Ihren SeedSigner ein, indem Sie ihn einstecken und dann das Menü "Seeds" öffnen.



![Image](assets/fr/23.webp)



Wählen Sie dann die Option "Vom SeedKeeper".



![Image](assets/fr/24.webp)



Stecken Sie Ihren Seedkeeper in den Chipkartenleser und geben Sie dann Ihren PIN-Code ein, um ihn zu entsperren. Bestätigen Sie Ihre Eingabe durch Drücken der Bestätigungstaste unten rechts, "KEY3".



![Image](assets/fr/25.webp)



Da Seedkeeper mehrere Geheimnisse enthalten kann, fordert SeedSigner Sie auf, das zu ladende Geheimnis auszuwählen. Die angezeigte Bezeichnung entspricht dem Namen, den Sie in Schritt 4 festgelegt haben. Wenn Sie, wie in meinem Fall, nur einen seed registriert haben, wird nur eine Option verfügbar sein.



![Image](assets/fr/26.webp)



Ihr seed ist nun geladen. Überprüfen Sie, ob es sich um das richtige wallet handelt, indem Sie den auf dem Bildschirm angezeigten Fingerabdruck mit dem in Ihren Sparrow Wallet-Einstellungen angegebenen vergleichen. Dieser Fingerabdruck wurde auch bei der ersten Erstellung des wallet angegeben.



Wenn Sie einen passphrase verwenden, können Sie ihn in diesem Stadium anwenden (siehe Teil 6 dieses Tutorials). Ansonsten klicken Sie einfach auf "Fertig".



![Image](assets/fr/27.webp)



Sie können Ihren wallet dann wie gewohnt verwenden: Sie können Ihre Lieferadressen überprüfen und Transaktionen unterzeichnen, genau wie mit einem klassischen SeedSigner. Um mehr über die Verwendung zu erfahren, sehen Sie sich das entsprechende Tutorial an:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Verwendung von Seedkeeper mit einem passphrase BIP39



Verwenden Sie einen passphrase, um Ihr Bitcoin-Portfolio zu schützen? Sie können ihn auch in Ihrem Seedkeeper zusammen mit Ihrem seed registrieren. Diese Lösung ermöglicht es Ihnen, Ihr wallet schnell auf den SeedSigner zu laden, ohne dass Sie das passphrase jedes Mal manuell auf der kleinen Tastatur eingeben müssen.



Ich finde diese Methode besonders interessant, da sie es Ihnen ermöglicht, von den Sicherheitsvorteilen des passphrase zu profitieren und gleichzeitig die mit seiner alltäglichen Nutzung verbundenen Einschränkungen zu beseitigen. Hier ist ein Beispiel für eine Konfiguration, die ich empfehlen würde:




- Bewahren Sie Ihr seed und passphrase in einem Seedkeeper auf, der durch einen starken PIN-Code geschützt ist (dies ist wichtig). Mit dieser Sicherung können Sie Ihren wallet problemlos täglich benutzen. Wenn Sie möchten, können Sie diese Informationen auf einem zweiten Seedkeeper duplizieren;
- Bewahren Sie außerdem eine eindeutige Kopie Ihrer Mnemonik und passphrase auf, auf Papier oder Metall. Dies ist der letzte Ausweg, falls Sie Ihren Seedkeeper oder seine PIN verlieren. Bewahren Sie diese Kopien an verschiedenen Orten auf, damit sie nicht gleichzeitig gefährdet werden können.



Wenn in dieser Konfiguration jemand nur Ihre Klartext-Merkhilfe in die Hände bekommt, kann er nichts stehlen, ohne die passphrase zu kennen (vorausgesetzt natürlich, sie ist stark genug, um einem Brute-Force-Angriff standzuhalten). Umgekehrt gilt: Wenn jemand Ihren passphrase im Klartext entdeckt, bleibt er ohne die entsprechende mnemonische Phrase unbrauchbar.



Sollte es jemandem gelingen, sich physischen Zugang zu Ihrem Seedkeeper zu verschaffen, der den seed und den passphrase enthält, kann er ohne Kenntnis des PIN-Codes nichts herausnehmen. Im Gegensatz zum passphrase kann dieser Code nicht geknackt werden, da sich die Smartcard nach fünf ungültigen Versuchen automatisch sperrt.



Die Sicherheit dieser Konfiguration beruht also auf 2 wesentlichen Punkten:




- Ein **passphrase strong**: Er muss lang und zufällig sein und eine Vielzahl von Zeichen enthalten. Seine Komplexität stellt für Sie kein Problem dar, da Sie ihn nur einmal während der Initialisierung auf der Tastatur eingeben müssen; danach wird er von Seedkeeper übermittelt;
- Ein **starker PIN-Code** für Seedkeeper: ebenfalls zufällig und aus 16 Zeichen bestehend.



Um dieses Setup einzurichten, laden Sie zunächst Ihren passphrase auf die übliche Weise in den SeedSigner. Sie können das in diesem Tutorial beschriebene Verfahren befolgen:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Sobald Ihr Portfolio mit passphrase korrekt in den SeedSigner geladen wurde, öffnen Sie das Menü "Seeds" und wählen Sie den Footprint für dieses Portfolio. Beachten Sie, dass sich dieser Fußabdruck von dem des Portfolios ohne passphrase unterscheidet.



![Image](assets/fr/28.webp)



Klicken Sie dann auf "Backup Seed", legen Sie den Seedkeeper in das Laufwerk ein und wählen Sie "Zum SeedKeeper".



![Image](assets/fr/29.webp)



Geben Sie Ihre PIN ein, um Seedkeeper zu entsperren, und weisen Sie diesem Geheimnis dann eine Kennzeichnung zu. Sie können den Fingerabdruck als Kennzeichnung belassen, um eine Form der plausiblen Bestreitbarkeit aufrechtzuerhalten, oder Sie geben z. B. ausdrücklich "Passphrase Wallet" an.



![Image](assets/fr/30.webp)



Ihr passphrase-Portfolio ist jetzt bei Seedkeeper registriert.



![Image](assets/fr/31.webp)



Wenn Sie das nächste Mal starten, legen Sie einfach Ihren Seedkeeper in das Laufwerk ein und navigieren dann zu "Seeds > From SeedKeeper".



![Image](assets/fr/32.webp)



Geben Sie Ihre PIN ein, um die Smartcard zu entsperren, und wählen Sie dann den wallet aus, der Ihrem passphrase entspricht.



![Image](assets/fr/33.webp)



Überprüfen Sie den passphrase und Ihren wallet-Aufdruck und bestätigen Sie dann.



![Image](assets/fr/34.webp)



Sie können nun mit passphrase auf Ihr Portfolio zugreifen und Ihre Transaktionen wie bei einem SeedSigner unterschreiben.



## 7. Zusätzliche Optionen



Im Menü `Tools > Smartcard Tools` finden Sie verschiedene Optionen zur Verwaltung Ihres Seedkeepers:





- Im Menü `Gemeinsame Werkzeuge` können Sie :
 - Prüfen Sie die Echtheit der Karte;
 - PIN-Code ändern ;
 - Ändern Sie die mit Ihren Geheimnissen verbundenen Bezeichnungen;
 - Deaktivieren Sie die NFC-Funktion (empfohlen, wenn Sie nur ein Chip-Lesegerät verwenden);
 - Führen Sie einen Werksreset durch.





- Im Menü "SeedKeeper-Funktionen" können Sie :
 - Konsultieren Sie die Liste der registrierten Geheimnisse;
 - Speichern Sie ein neues Geheimnis;
 - Ein bestehendes Geheimnis löschen;
 - Speichern oder laden Sie Ihre Deskriptoren (nützliche Funktion für multi-sig-Portfolios).





- Im Menü `DIY Tools` können Sie :
 - Kompilieren des Seedkeeper-Applets ;
 - Installieren Sie das Applet auf einer leeren Karte;
 - Löschen Sie ein Seedkeeper-Applet, um es zurückzusetzen und es wieder leer zu machen.



Jetzt wissen Sie, wie Sie Seedkeeper verwenden können, um Ihr Portfolio in Kombination mit SeedSigner sicher zu sichern.



Wenn Sie dieser Aufbau überzeugt hat, zögern Sie nicht, die Projekte zu unterstützen, die dies möglich machen:




- Indem Sie Ihr Gerät direkt [auf der Satochip-Website] kaufen (https://satochip.io/shop/);
- Durch [eine Spende an das SeedSigner-Projekt](https://seedsigner.com/donate/);
- Indem Sie den YouTube-Kanal von [Crypto Guide] (https://www.youtube.com/@CryptoGuide/) abonnieren, der von der Person betrieben wird, die das GitHub-Repository mit der modifizierten Firmware verwaltet.