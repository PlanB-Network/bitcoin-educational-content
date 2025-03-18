---
name: Abgesandter
description: Einrichten und Verwenden eines Reisepasses mit der Envoy-Anwendung
---
![cover](assets/cover.webp)

Envoy ist eine von Foundation entwickelte Anwendung zur Verwaltung von Bitcoin-Wallets. Sie ist speziell für die Verwendung mit der Passport-Hardware-Wallet konzipiert.

Der Passport "*Batch 2*", den wir in diesem Tutorial zusammen mit der Envoy-App vorstellen, ist der Nachfolger der "*Founder's Edition*". Er zeichnet sich durch ein hochwertiges Design, ein hochauflösendes Farbdisplay und eine ergonomische physische Tastatur aus. Er arbeitet im "*Air-Gap*"-Modus, wodurch die privaten Schlüssel Ihrer Wallet vollständig isoliert bleiben, mit Datenaustausch über eine MicroSD-Karte oder QR-Codes. Das Gerät ist mit einem herausnehmbaren, wiederaufladbaren Nokia BL-5C-Akku mit 1200 mAh ausgestattet. Diese handelsübliche Batterie kann leicht ersetzt werden, da das BL-5C-Modell weit verbreitet ist.

Was die Konnektivität betrifft, so ist das Passport mit einem MicroSD-Anschluss, einem USB-C-Anschluss zum Aufladen und einer Rückkamera zum Scannen von QR-Codes ausgestattet.

Was die Sicherheit betrifft, so verfügt der Passport über ein Sicherheitselement und der Quellcode des Geräts ist vollständig quelloffen. Es bietet alle Funktionen, die man von einer guten Bitcoin-Hardware-Wallet erwartet. Beachten Sie, dass der Passport noch nicht Miniscript unterstützt, aber diese Funktion ist für das zweite Quartal 2025 geplant.

Mit einem Preis von 199 US-Dollar ist der Passport als High-End-Hardware-Geldbörse positioniert und konkurriert mit der Coldcard Q, dem Jade Plus, dem Tezor Safe 5 und den Spitzenmodellen von Ledger.

![Image](assets/fr/01.webp)

Um Ihre sichere Geldbörse auf einem Passport zu verwalten, haben Sie mehrere Möglichkeiten. Diese Hardware-Wallet ist mit der Mehrzahl der auf dem Markt erhältlichen Wallet-Management-Software kompatibel, darunter Sparrow Wallet, Specter Desktop, Nunchuk, Keeper und andere.

In diesem Tutorial, das sich an Anfänger und Fortgeschrittene richtet, erfahren Sie, wie Sie die Envoy-Anwendung mit Ihrem Passport nutzen können. Es ist der einfachste Weg, das Beste aus Ihrer Hardware-Geldbörse herauszuholen.

Wenn Sie ein fortgeschrittener Benutzer sind und komplexere Funktionen erforschen möchten, empfehle ich Ihnen, sich dieses andere Tutorial anzusehen, in dem wir Passport mit Sparrow Wallet konfigurieren:

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

## Auspacken des Passes

Vergewissern Sie sich bei Erhalt Ihres Passport, dass die Verpackung und das Siegel auf dem Karton intakt sind, um sicherzustellen, dass das Paket nicht geöffnet wurde. Bei der Einrichtung des Geräts wird auch eine Softwareüberprüfung seiner Authentizität und Integrität durchgeführt.

![Image](assets/fr/02.webp)

Inhalt der Box: :


- Reisepass;
- Ein Stück Pappe, auf das Sie Ihre Gedächtnisstütze schreiben können;
- Ein USB-C-Kabel zum Aufladen ;
- MicroSD-Karte ;
- Zwei MicroSD-zu-Lightning- oder USB-C-Adapter ;
- Aufkleber.

Auf dem Gerät finden Sie :


- Eine Tastatur (1) ;
- USB-C-Anschluss (2);
- Eine Löschtaste (3);
- Eine Rücklauftaste (4) ;
- Eine Bestätigungstaste (5);
- Richtungsweisendes Pad (6);
- Taste Ein/Aus (7);
- Eine Statusanzeige (8);
- MicroSD-Anschluss (9) ;
- Eine Taste zum Wechseln des Modus aA1 (10) ;
- Eine Rückfahrkamera.

![Image](assets/fr/03.webp)

## Envoy-Anwendung herunterladen

Laden Sie Envoy in Ihrem App Store herunter:


- Im [Google Play Store] (https://play.google.com/store/apps/details?id=com.foundationdevices.envoy);
- Im [App Store] (https://apps.apple.com/us/app/envoy-by-foundation/id1584811818);
- Auf [F-Cold] (https://foundation.xyz/fdroid/).

![Image](assets/fr/50.webp)

Sie können die APK-Datei auch direkt [aus dem GitHub-Repository der Foundation] herunterladen (https://github.com/Foundation-Devices/envoy/releases).

![Image](assets/fr/51.webp)

Sobald die Anwendung geöffnet ist, wählen Sie "*Pass verwalten*".

![Image](assets/fr/52.webp)

Wählen Sie, ob Sie die Tor-Verbindung aktivieren möchten, um die Vertraulichkeit zu erhöhen, und drücken Sie dann auf "*Weiter*".

![Image](assets/fr/53.webp)

Wählen Sie "*Verbinden Sie einen vorhandenen Passport*", wenn Ihr Passport bereits konfiguriert ist, oder "*Einrichten eines neuen Passport*", wenn Sie Ihre Hardware-Geldbörse zum ersten Mal initialisieren.

![Image](assets/fr/54.webp)

Akzeptieren Sie die Nutzungsbedingungen.

![Image](assets/fr/55.webp)

Sie werden dann aufgefordert, die Echtheit des Passes zu überprüfen. Klicken Sie auf "*Weiter*".

![Image](assets/fr/56.webp)

## Reisepass starten

Drücken Sie die Ein/Aus-Taste an der Seite des Geräts, um es in Betrieb zu nehmen.

![Image](assets/fr/04.webp)

Drücken Sie die Bestätigungstaste, um das nächste Menü aufzurufen.

![Image](assets/fr/05.webp)

In diesem Tutorial werden wir Envoy verwenden, um die Passport-gesicherte Geldbörse zu verwalten. Wählen Sie "*Envoy App*".

![Image](assets/fr/57.webp)

Klicken Sie auf "*Fortsetzen auf Envoy*".

![Image](assets/fr/58.webp)

Der nächste Schritt ist die Überprüfung Ihres Geräts. Damit wird die Echtheit Ihres Passes bestätigt und sichergestellt, dass er während des Transports nicht manipuliert wurde. Sie werden aufgefordert, einen QR-Code zu scannen.

![Image](assets/fr/08.webp)

Scannen Sie die in der Anwendung angezeigten dynamischen QR-Codes mit Ihrem Reisepass. Wenn der Scanvorgang abgeschlossen ist, klicken Sie auf "*Weiter*".

![Image](assets/fr/59.webp)

Scannen Sie dann mit Ihrem Handy den QR-Code, der auf Ihrem Reisepass steht.

![Image](assets/fr/60.webp)

Wenn die Meldung "*Ihr Pass ist sicher*" erscheint, bestätigt dies, dass Ihre Hardware-Wallet echt ist. Sie können es nun verwenden, um eine Bitcoin-Wallet zu sichern.

![Image](assets/fr/61.webp)

Bestätigen Sie das Testergebnis in Ihrem Reisepass.

![Image](assets/fr/14.webp)

## Einstellen des PIN-Codes

Als Nächstes folgt der Schritt des PIN-Codes. Mit dem PIN-Code wird Ihr Pass entsperrt. Er bietet daher Schutz vor unbefugtem physischen Zugriff. Der PIN-Code ist nicht an der Ableitung der kryptografischen Schlüssel Ihrer Brieftasche beteiligt. Selbst wenn Sie keinen Zugang zum PIN-Code haben, können Sie mit Ihrer 12- oder 24-Wort-Mnemonik wieder Zugang zu Ihren Bitcoins erhalten.

![Image](assets/fr/15.webp)

Wir empfehlen, einen möglichst zufälligen PIN-Code zu wählen. Speichern Sie diesen Code an einem anderen Ort als den, an dem Ihr Pass gespeichert ist (z. B. in einem Passwortmanager).

Sie können einen PIN-Code zwischen 6 und 12 Ziffern wählen. Ich empfehle Ihnen, ihn so lang wie möglich zu machen.

Geben Sie Ihre PIN-Nummern über das Tastenfeld ein. Wenn Sie fertig sind, klicken Sie auf die Bestätigungstaste.

![Image](assets/fr/16.webp)

Bestätigen Sie Ihre PIN ein zweites Mal.

![Image](assets/fr/17.webp)

Ihr PIN-Code ist registriert worden.

![Image](assets/fr/18.webp)

## Passport-Firmware aktualisieren

Ihre Hardware-Brieftasche schlägt vor, dass Sie die Firmware aktualisieren. Ich empfehle Ihnen, sofort zu aktualisieren, um von den Verbesserungen und Korrekturen der neuesten Versionen zu profitieren. Um fortzufahren, klicken Sie auf die Bestätigungsschaltfläche auf der rechten Seite.

![Image](assets/fr/19.webp)

Ihr Passport ist nun bereit, die neue Firmware über eine MicroSD-Karte zu empfangen.

![Image](assets/fr/20.webp)

### Ohne Envoy-Anwendung

Verwenden Sie dazu die MicroSD-Karte, die in Ihrer Passport-Box enthalten ist (oder eine andere), und legen Sie sie in Ihren Computer ein. Laden Sie die neueste Firmware-Version von [der Dokumentations-Website der Foundation] (https://docs.foundation.xyz/firmware-updates/passport/) oder [ihrem GitHub-Repository] (https://github.com/Foundation-Devices/passport2/releases) herunter.

![Image](assets/fr/21.webp)

Wir raten Ihnen dringend, die Authentizität und Integrität der heruntergeladenen Firmware zu überprüfen, bevor Sie sie auf Ihrem Gerät installieren. Wenn Sie dabei Hilfe benötigen, lesen Sie dieses Tutorial:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### Mit der Envoy-Anwendung

Die andere, einfachere Möglichkeit besteht darin, die Envoy-Anwendung direkt zu verwenden. Klicken Sie auf "*Download Firmware*".

![Image](assets/fr/62.webp)

Verwenden Sie den mit Ihrem Passport gelieferten Adapter, um die MicroSD-Karte mit Ihrem Telefon zu verbinden.

![Image](assets/fr/63.webp)

Wählen Sie die MicroSD-Karte in Ihrem Datei-Explorer aus, um die Firmware zu speichern.

![Image](assets/fr/64.webp)

Die Firmware ist nun gespeichert. Entfernen Sie die MicroSD-Karte aus Ihrem Smartphone und legen Sie sie in den Passport ein.

![Image](assets/fr/65.webp)

Der Passport-Dateiexplorer wird geöffnet. Wählen Sie die Datei "vN.N.N-passport.bin".

![Image](assets/fr/22.webp)

Klicken Sie auf "*Auswählen*".

![Image](assets/fr/23.webp)

Bestätigen Sie dann die Installation der Firmware.

![Image](assets/fr/24.webp)

Bitte warten Sie, bis die Aktualisierung abgeschlossen ist.

![Image](assets/fr/25.webp)

Sobald die Aktualisierung abgeschlossen ist, geben Sie Ihren PIN-Code ein, um das Gerät zu entsperren und die Konfiguration fortzusetzen.

![Image](assets/fr/26.webp)

## Eine neue Bitcoin-Wallet erstellen

Nun ist es an der Zeit, eine neue Bitcoin-Brieftasche zu erstellen. Klicken Sie auf die Bestätigungsschaltfläche.

![Image](assets/fr/27.webp)

Um ein neues Portfolio zu erstellen, klicken Sie auf "*Neues Saatgut erstellen*".

![Image](assets/fr/28.webp)

Sie können zwischen einer Eselsbrücke mit 12 oder 24 Wörtern wählen. Die Sicherheit beider Optionen ist ähnlich, so dass Sie sich für diejenige entscheiden können, die am einfachsten zu speichern ist, d. h. für 12 Wörter.

![Image](assets/fr/29.webp)

Klicken Sie auf "*Fortfahren*".

![Image](assets/fr/30.webp)

Ihr Passport generiert nun Ihren "*Backup Code*". Dies ist eine Reihe von Zahlen, die verwendet werden können, um ein Backup Ihrer Wallet zu entschlüsseln, das auf einer MicroSD gespeichert ist. Dieses für Foundation-Geräte spezifische Backup-System stellt eine zusätzliche Sicherung Ihrer mnemonischen Phrase dar, ist aber nicht mit anderer Bitcoin-Software kompatibel.

Wenn Sie sich für diesen "*Backup Code*" entscheiden, sollten Sie ihn an einem anderen Ort aufbewahren als Ihre MicroSD-Karte, auf der sich die verschlüsselte Sicherungskopie Ihrer Geldbörse befindet. Sie können jedoch auch auf dieses System verzichten, wenn Sie der Meinung sind, dass ein gutes Backup Ihrer mnemonischen Phrase ausreichend ist.

![Image](assets/fr/31.webp)

Geben Sie Ihren "*Backup Code*" ein, um zu bestätigen, dass Sie ihn korrekt gespeichert haben.

![Image](assets/fr/32.webp)

Wenn eine MicroSD-Karte eingelegt wurde, ist die verschlüsselte Sicherung Ihres Portfolios dort gespeichert.

![Image](assets/fr/33.webp)

In Ihrem Passport wird Ihre 12-Wort-Merkhilfe angezeigt. Mit dieser Phrase haben Sie uneingeschränkten Zugriff auf alle Ihre Bitcoins. Jeder, der im Besitz dieser Phrase ist, kann Ihr Geld stehlen, auch ohne physischen Zugang zu Ihrem Pass.

Die 12-Wort-Phrase stellt den Zugang zu Ihren Bitcoins bei Verlust, Diebstahl oder Bruch Ihres Passes wieder her. Es ist daher sehr wichtig, dass Sie ihn sorgfältig aufbewahren und an einem sicheren Ort aufbewahren.

Sie können die Gravur auf dem mitgelieferten Karton anbringen. Für zusätzliche Sicherheit empfehle ich, die Gravur auf einem Edelstahlsockel anzubringen, um sie vor Feuer, Überschwemmung oder Einsturz zu schützen.

Klicken Sie auf die Bestätigungsschaltfläche, um Ihre mnemonische Phrase zu sehen.

![Image](assets/fr/34.webp)

Für weitere Informationen über die richtige Art und Weise, wie Sie Ihre mnemotechnische Phrase speichern und verwalten können, empfehle ich Ihnen diesen anderen Lehrgang, besonders wenn Sie Anfänger sind:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

natürlich dürfen Sie diese Worte niemals im Internet weitergeben, wie ich es in diesem Tutorium tue. Dieses Musterportfolio wird nur im Testnet verwendet und am Ende des Tutoriums gelöscht.**_

Machen Sie eine physische Sicherung dieses Satzes.

![Image](assets/fr/35.webp)

Ihr Passport wurde erfolgreich konfiguriert. Klicken Sie auf die Bestätigungsschaltfläche, um fortzufahren.

![Image](assets/fr/36.webp)

## Einrichten des Portfolios auf Envoy

In diesem Tutorial zeige ich Ihnen, wie Sie den Passport mit der Envoy-Anwendung verwenden. Diese Hardware-Geldbörse ist jedoch auch mit Sparrow Wallet, Keeper, BlueWallet, Nunchuk, Specter und vielen anderen kompatibel...

![Image](assets/fr/66.webp)

Verwenden Sie die Envoy-Anwendung, um den QR-Code auf Ihrem Pass zu scannen.

![Image](assets/fr/67.webp)

Ihre öffentlichen Schlüssel werden nun in die Anwendung importiert. Klicken Sie auf "*Empfangsadresse validieren*".

![Image](assets/fr/68.webp)

Scannen Sie die auf Envoy angezeigte Adresse mit Ihrem Reisepass.

![Image](assets/fr/69.webp)

Ihr Reisepass bestätigt, ob die auf Envoy importierte Brieftasche gültig ist. Bestätigen Sie dies in der Anwendung.

![Image](assets/fr/70.webp)

Sie können jetzt auf die öffentlichen Informationen Ihrer Geldbörse auf Envoy zugreifen, aber um Bitcoins auszugeben, müssen Sie Ihren Passport verwenden.

![Image](assets/fr/71.webp)

## Passport-Menüs entdecken

Die Passport-Oberfläche besteht aus drei Hauptmenüs:


- "*Konto*";
- "*Mehr*";
- "*Einstellungen*".

Um zwischen diesen Menüs zu navigieren, verwenden Sie die Links- und Rechtspfeile auf dem Steuerkreuz.

### *Menü "Konto*

Im Menü "*Konto*" finden Sie die wichtigsten Funktionen Ihrer Bitcoin-Brieftasche. Sie können eine Transaktion entweder über die Kamera oder über den MicroSD-Anschluss unterschreiben.

![Image](assets/fr/37.webp)

Das Untermenü "*Kontotools*" bietet Optionen wie die Überprüfung einer Adresse, das Signieren einer Nachricht oder die Abfrage der Adressen in Ihrem Portfolio.

![Image](assets/fr/38.webp)

Im Untermenü "*Konto verwalten*" können Sie Ihre Bitcoin-Wallet mit einer Wallet-Verwaltungssoftware verbinden (was wir in den nächsten Schritten dieses Tutorials behandeln werden) oder Ihr Konto einsehen und umbenennen.

![Image](assets/fr/39.webp)

### Menü "Mehr

Im Menü "*Mehr*" können Sie ein neues Konto in Ihrem Portfolio anlegen, das mit demselben Merksatz verknüpft ist.

![Image](assets/fr/40.webp)

Sie können auch eine BIP39-Passphrase eingeben oder einen temporären Seed verwenden.

![Image](assets/fr/41.webp)

### Menü "Einstellungen

Im Menü "*Einstellungen*" finden Sie alle Einstellungen für Ihre Geldbörse und Ihr Gerät.

![Image](assets/fr/42.webp)

Das Untermenü "*Gerät*" bietet Ihnen Optionen zum Anpassen der Bildschirmhelligkeit, zum Einstellen der Verzögerung vor der automatischen Sperre, zum Ändern des PIN-Codes oder zum Umbenennen des Geräts.

![Image](assets/fr/43.webp)

Über das Untermenü "*Backup*" können Sie Ihre verschlüsselte Portfoliosicherung exportieren, die Gültigkeit einer bestehenden Sicherung überprüfen oder Ihren "*Backup Code*" erneut nachschlagen.

![Image](assets/fr/44.webp)

Das Untermenü "*Firmware*" dient zum Aktualisieren der Firmware Ihres Passport. Wir empfehlen Ihnen, diese Updates regelmäßig durchzuführen, um von den neuesten Korrekturen und Funktionen zu profitieren.

![Image](assets/fr/45.webp)

Im Untermenü "*Bitcoin*" können Sie die angezeigte Einheit (BTC oder Satoshis) ändern, eine mögliche Multisig-Brieftasche verwalten oder in den Modus "*Testnet*" wechseln.

![Image](assets/fr/46.webp)

Unter "*Erweitert*" können Sie die Wörter Ihrer mnemotechnischen Phrase anzeigen, Aktionen auf der eingelegten MicroSD durchführen, Ihren Passport auf die Werkseinstellungen zurücksetzen oder eine Echtheitsprüfung durchführen, wie bereits zuvor durchgeführt.

![Image](assets/fr/47.webp)

Sie können "*Sicherheitswörter*" aktivieren, eine Funktion, die eine zusätzliche Sicherheitsebene schafft, indem sie beim Entsperren des Geräts nach Eingabe der ersten vier Ziffern des PIN-Codes zwei bestimmte Wörter anzeigt. Diese Wörter, die während der Konfiguration gespeichert werden, stellen sicher, dass der Passport nicht ausgetauscht oder manipuliert wurde. Sollte zu einem späteren Zeitpunkt eine Unstimmigkeit auftreten, raten wir Ihnen, das Gerät nicht zu benutzen. Ich empfehle Ihnen, diese Option zu aktivieren, um die meisten Risiken einer physischen Kompromittierung des Geräts zu vermeiden.

![Image](assets/fr/48.webp)

Im Untermenü "*Erweiterungen*" schließlich können Sie Funktionen aktivieren, die für bestimmte Verwendungszwecke des Geräts spezifisch sind, wie z. B. das Coinjoin-Protokoll von Whirlpool.

![Image](assets/fr/49.webp)

## Bitcoins erhalten

Nun, da Ihr Passport eingerichtet ist, können Sie Ihre ersten Sats auf Ihrer neuen Bitcoin-Brieftasche empfangen. Klicken Sie dazu auf Envoy auf Ihr "*Primary 0*"-Konto.

![Image](assets/fr/72.webp)

Klicken Sie auf die Schaltfläche "*Empfangen*".

![Image](assets/fr/73.webp)

Ihre Envoy-Anwendung zeigt die erste verfügbare leere Adresse in Ihrer Wallet an. Bevor wir sie verwenden, sollten wir die Adresse auf dem Passport-Bildschirm überprüfen, um sicherzustellen, dass sie wirklich zu unserer Bitcoin-Brieftasche gehört. Wählen Sie in Ihrem Passport-Menü "*Konto*" die Option "*Kontotools*".

![Image](assets/fr/74.webp)

Klicken Sie auf "*Adresse prüfen*" und scannen Sie dann den auf Envoy angezeigten QR-Code.

![Image](assets/fr/75.webp)

Vergewissern Sie sich, dass die auf dem Pass angezeigte Adresse genau mit der auf Sparrow angezeigten Adresse übereinstimmt und dass "*Verified*" angezeigt wird.

![Image](assets/fr/76.webp)

Sie können es jetzt verwenden, um Bitcoins zu empfangen. Wenn die Transaktion im Netzwerk übertragen wird, erscheint sie auf Envoy. Warten Sie, bis Sie genügend Bestätigungen erhalten haben, um die Transaktion als endgültig zu betrachten.

![Image](assets/fr/77.webp)

## Bitcoins senden

Jetzt, wo du ein paar Sats in deinem Portemonnaie hast, kannst du auch welche verschicken. Klicken Sie dazu auf die Schaltfläche "*Senden*".

![Image](assets/fr/78.webp)

Geben Sie die Adresse des Empfängers ein, indem Sie sie entweder direkt einfügen oder den QR-Code mit der Kamera Ihres Smartphones scannen.

![Image](assets/fr/79.webp)

Bestimmen Sie den Betrag, den Sie senden möchten, und klicken Sie dann auf "*Bestätigen*".

![Image](assets/fr/80.webp)

Wählen Sie die Transaktionsgebühr entsprechend der aktuellen Marktsituation aus und überprüfen Sie dann die Transaktionsinformationen. Wenn alles korrekt ist, klicken Sie auf "*Unterschreiben mit Pass*".

![Image](assets/fr/81.webp)

Versehen Sie Ihre Transaktion mit einem Etikett, um den Verwendungszweck eindeutig zu dokumentieren.

![Image](assets/fr/82.webp)

Envoy zeigt dann eine PSBT (*Partially Signed Bitcoin Transaction*) an. Die Anwendung hat die Transaktion erstellt, aber es fehlt noch die Signatur(en), um die in der Eingabe verwendeten Bitcoins zu entsperren. Diese Signaturen können nur vom Passport geleistet werden, der Ihren Seed hostet und Zugang zu den privaten Schlüsseln gibt, die zum Signieren der Transaktion benötigt werden.

![Image](assets/fr/83.webp)

Rufen Sie in Ihrem Passport das Menü "*Konto*" auf und klicken Sie auf "*Mit QR-Code unterschreiben*".

![Image](assets/fr/84.webp)

Scannen Sie die PSBT (*Partially Signed Bitcoin Transaction*), die auf Envoy angezeigt wird.

![Image](assets/fr/85.webp)

Vergewissern Sie sich, dass die Empfängeradresse und der gesendete Betrag korrekt sind, und drücken Sie dann die Bestätigungstaste.

![Image](assets/fr/86.webp)

Überprüfen Sie die Austauschadresse. In meinem Beispiel gibt es keine, da die Transaktion eine einzige Ausgabe enthält.

![Image](assets/fr/87.webp)

Vergewissern Sie sich, dass die Gebühr die von Ihnen gewählte ist.

![Image](assets/fr/88.webp)

Wenn alle Angaben korrekt sind, klicken Sie auf die Bestätigungsschaltfläche, um die Transaktion zu unterzeichnen.

![Image](assets/fr/89.webp)

Ihr Pass zeigt Ihnen Ihre signierte Transaktion in Form eines QR-Codes an.

![Image](assets/fr/90.webp)

Klicken Sie in der Envoy-Anwendung auf das QR-Code-Symbol und scannen Sie dann den PSBT, der auf dem Bildschirm Ihres Reisepasses angezeigt wird.

![Image](assets/fr/91.webp)

Überprüfen Sie ein letztes Mal Ihre Transaktionsdetails. Wenn alles korrekt ist, drücken Sie "*Transaktion senden*", um die Transaktion im Bitcoin-Netzwerk zu übertragen.

![Image](assets/fr/92.webp)

Ihre Transaktion wartet nun auf die Bestätigung. Sie können den Status der Transaktion direkt in Ihrem Konto verfolgen.

![Image](assets/fr/93.webp)

Herzlichen Glückwunsch, Sie wissen jetzt, wie Sie den Passport mit der Envoy-Anwendung einrichten und verwenden können. Wenn Sie diese Anleitung nützlich fanden, wäre ich Ihnen dankbar, wenn Sie unten einen grünen Daumen hinterlassen würden. Sie können diesen Artikel auch gerne in Ihren sozialen Netzwerken teilen. Vielen Dank fürs Teilen!

Weitere Informationen finden Sie in unserem Tutorium zur Liana-Software:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
