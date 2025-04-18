---
name: Reisepass - Stiftung
description: Konfigurieren und Verwenden der Passport-Hardware-Geldbörse im manuellen Modus
---
![cover](assets/cover.webp)

Der Passport ist eine reine Bitcoin-Hardware-Wallet, entwickelt von Foundation Devices, einem amerikanischen Unternehmen, das im April 2020 in Boston gegründet wurde.

Der Passport "*Batch 2*", den wir in diesem Tutorial vorstellen, ist der Nachfolger der "*Founder's Edition*". Er zeichnet sich durch ein hochwertiges Design, ein hochauflösendes Farbdisplay und eine ergonomische physische Tastatur aus. Er arbeitet im "*Air-Gap*"-Modus, wodurch die privaten Schlüssel Ihrer Wallet vollständig isoliert bleiben, mit Datenaustausch über eine MicroSD-Karte oder QR-Codes. Das Gerät ist mit einem herausnehmbaren, wiederaufladbaren Nokia BL-5C-Akku mit 1200 mAh ausgestattet. Diese handelsübliche Batterie kann leicht ersetzt werden, da das BL-5C-Modell weit verbreitet ist.

Was die Konnektivität betrifft, so ist das Passport mit einem MicroSD-Anschluss, einem USB-C-Anschluss zum Aufladen und einer Rückkamera zum Scannen von QR-Codes ausgestattet.

Was die Sicherheit betrifft, so verfügt der Passport über ein Sicherheitselement und der Quellcode des Geräts ist vollständig quelloffen. Es bietet alle Funktionen, die man von einer guten Bitcoin-Hardware-Wallet erwartet. Beachten Sie, dass der Passport noch nicht Miniscript unterstützt, aber diese Funktion ist für das zweite Quartal 2025 geplant.

Mit einem Preis von 199 US-Dollar ist der Passport als High-End-Hardware-Geldbörse positioniert und konkurriert mit der Coldcard Q, dem Jade Plus, dem Tezor Safe 5 und den Spitzenmodellen von Ledger.

![Image](assets/fr/01.webp)

Um Ihre sichere Geldbörse auf einem Passport zu verwalten, haben Sie mehrere Möglichkeiten. Diese Hardware-Wallet ist mit der Mehrzahl der auf dem Markt erhältlichen Wallet-Management-Software kompatibel, darunter Sparrow Wallet, Specter Desktop, Nunchuk, Keeper und andere. In diesem Tutorial werden wir lernen, wie man sie mit Sparrow Wallet verwendet.

Für Anfänger ist es am einfachsten, den Passport mit der von Foundation entwickelten Anwendung Envoy zu verwenden. Um herauszufinden, wie Sie Envoy mit Ihrem Passport verwenden können, lesen Sie diese Anleitung:

https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb

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

## Reisepass starten

Drücken Sie die Ein/Aus-Taste an der Seite des Geräts, um es in Betrieb zu nehmen.

![Image](assets/fr/04.webp)

Drücken Sie die Bestätigungstaste, um das nächste Menü aufzurufen.

![Image](assets/fr/05.webp)

In diesem Tutorial werden wir Sparrow Wallet verwenden, um die passgesicherte Geldbörse zu verwalten. Wählen Sie "*Manuelle Einrichtung*".

![Image](assets/fr/06.webp)

Dann akzeptieren Sie die Nutzungsbedingungen.

![Image](assets/fr/07.webp)

Der nächste Schritt ist die Überprüfung Ihres Geräts. Damit wird die Echtheit Ihres Passes bestätigt und sichergestellt, dass er während des Transports nicht manipuliert wurde. Sie werden aufgefordert, einen QR-Code zu scannen.

![Image](assets/fr/08.webp)

Gehen Sie auf [die offizielle Verifizierungsseite] (https://validate.foundationdevices.com/) und wählen Sie "*Passport*".

![Image](assets/fr/09.webp)

Benutzen Sie die Kamera Ihres Passes, um den auf der Website angezeigten QR-Code zu scannen.

![Image](assets/fr/10.webp)

Ihr Gerät zeigt dann 4 Wörter an.

![Image](assets/fr/11.webp)

Geben Sie diese Worte auf der Website ein, um die Echtheit Ihres Passes zu bestätigen, und klicken Sie auf "*Validieren*".

![Image](assets/fr/12.webp)

Wenn die Meldung "*Passed*" erscheint, ist Ihre Hardware-Wallet echt. Sie können sie nun verwenden, um eine Bitcoin-Wallet zu sichern.

![Image](assets/fr/13.webp)

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

Verwenden Sie dazu die MicroSD-Karte, die in Ihrer Passport-Box enthalten ist (oder eine andere), und legen Sie sie in Ihren Computer ein. Laden Sie die neueste Firmware-Version von [der Dokumentations-Website der Foundation] (https://docs.foundation.xyz/firmware-updates/passport/) oder [ihrem GitHub-Repository] (https://github.com/Foundation-Devices/passport2/releases) herunter.

![Image](assets/fr/21.webp)

Wir raten Ihnen dringend, die Authentizität und Integrität der heruntergeladenen Firmware zu überprüfen, bevor Sie sie auf Ihrem Gerät installieren. Wenn Sie dabei Hilfe benötigen, lesen Sie dieses Tutorial:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Nachdem Sie die "bin"-Datei überprüft haben, legen Sie sie auf Ihrer MicroSD-Karte ab und stecken sie in den Passport. Der Passport-Dateiexplorer wird geöffnet. Wählen Sie die Datei "vN.N.N-passport.bin".

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

Ihr Passport generiert nun Ihren "*Backup Code*". Dies ist eine Reihe von Zahlen, die verwendet werden können, um ein Backup Ihrer Wallet zu entschlüsseln, das auf einer MicroSD-Karte gespeichert ist. Dieses für Foundation-Geräte spezifische Backup-System stellt eine zusätzliche Sicherung Ihrer mnemonischen Phrase dar, ist aber nicht mit anderer Bitcoin-Software kompatibel.

Wenn Sie sich für diesen "*Backup Code*" entscheiden, sollten Sie ihn an einem anderen Ort aufbewahren als Ihre MicroSD-Karte, auf der sich die verschlüsselte Sicherungskopie Ihrer Geldbörse befindet. Sie können jedoch auch auf dieses System verzichten, wenn Sie der Meinung sind, dass ein gutes Backup Ihrer mnemonischen Phrase ausreichend ist.

![Image](assets/fr/31.webp)

Geben Sie Ihren "*Backup Code*" ein, um zu bestätigen, dass Sie ihn korrekt gespeichert haben.

![Image](assets/fr/32.webp)

Wenn eine MicroSD-Karte eingelegt wurde, ist die verschlüsselte Sicherung Ihres Portfolios dort gespeichert.

![Image](assets/fr/33.webp)

In Ihrem Pass wird Ihre 12-Wort-Mnemonik angezeigt. Mit diesem Merksatz haben Sie uneingeschränkten Zugriff auf alle Ihre Bitcoins. Jeder, der im Besitz dieser Phrase ist, kann Ihr Geld stehlen, auch ohne physischen Zugang zu Ihrem Pass.

Die 12-Wort-Phrase stellt den Zugang zu Ihren Bitcoins bei Verlust, Diebstahl oder Bruch Ihres Passes wieder her. Es ist daher sehr wichtig, dass Sie ihn sorgfältig aufbewahren und an einem sicheren Ort aufbewahren.

Sie können die Gravur auf dem mitgelieferten Karton anbringen. Für zusätzliche Sicherheit empfehle ich, die Gravur auf einem Edelstahlsockel anzubringen, um sie vor Feuer, Überschwemmung oder Einsturz zu schützen.

Klicken Sie auf die Bestätigungsschaltfläche, um Ihre mnemonische Phrase zu sehen.

![Image](assets/fr/34.webp)

Für weitere Informationen über die richtige Art und Weise, wie Sie Ihre mnemotechnische Phrase speichern und verwalten können, empfehle ich Ihnen, diese andere Anleitung zu lesen, insbesondere wenn Sie Anfänger sind:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

natürlich dürfen Sie diese Worte niemals im Internet weitergeben, wie ich es in diesem Tutorium tue. Dieses Musterportfolio wird nur im Testnet verwendet und am Ende des Tutoriums gelöscht.**_

Machen Sie eine physische Sicherung dieses Satzes.

![Image](assets/fr/35.webp)

Ihr Passport wurde erfolgreich konfiguriert. Klicken Sie auf die Bestätigungsschaltfläche, um fortzufahren.

![Image](assets/fr/36.webp)

## Entdeckung des Menüs

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

Sie können auch eine BIP39-Passphrase eingeben (siehe nächster Abschnitt) oder einen temporären Seed verwenden.

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

## Hinzufügen einer BIP39-Passphrase

Bevor Sie fortfahren, können Sie, wenn Sie möchten, eine BIP39-Passphrase hinzufügen. Eine BIP39-Passphrase ist ein optionales Passwort, das Sie frei wählen können und das zu Ihrer mnemonischen Phrase hinzugefügt wird, um die Sicherheit Ihrer Wallet zu erhöhen. Wenn diese Funktion aktiviert ist, ist für den Zugriff auf Ihre Bitcoin-Wallet sowohl die Eselsbrücke als auch die Passphrase erforderlich. Ohne beides wäre es unmöglich, die Wallet wiederherzustellen.

Bevor Sie diese Option auf Ihrem Passport konfigurieren, empfehlen wir Ihnen dringend, diesen Artikel zu lesen, um die theoretische Funktionsweise der Passphrase vollständig zu verstehen und Fehler zu vermeiden, die zum Verlust Ihrer Bitcoins führen könnten:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Um sie zu aktivieren, gehen Sie zum Menü "*Mehr*" und klicken Sie auf "*Passphrase eingeben*".

![Image](assets/fr/50.webp)

Geben Sie Ihre Passphrase über die aA1-Tastatur ein und speichern Sie sie ein oder mehrere Male auf einem physischen Medium (Papier oder Metall). Für das Beispiel habe ich eine sehr schwache Passphrase verwendet, aber Sie sollten eine starke, zufällige Passphrase wählen, die alle Zeichentypen enthält und ausreichend lang ist (wie ein starkes Passwort).

![Image](assets/fr/51.webp)

Bitte beachten Sie, dass bei BIP39-Passphrasen zwischen Groß- und Kleinschreibung unterschieden wird. Wenn Sie eine Passphrase eingeben, die sich geringfügig von der ursprünglich konfigurierten unterscheidet, meldet Passport keinen Fehler, sondern leitet einen anderen Satz kryptografischer Schlüssel ab, der sich von dem in Ihrer ursprünglichen Brieftasche unterscheidet.

Daher ist es wichtig, dass Sie sich bei der Konfiguration irgendwo den Hauptschlüssel-Fingerabdruck notieren, den Sie im nächsten Schritt erhalten werden. Bei meiner Passphrase "Plan B Network" lautet mein Hauptschlüssel-Fingerabdruck zum Beispiel "745D526B".

![Image](assets/fr/52.webp)

Jedes Mal, wenn Sie Ihren Passport entsperren, müssen Sie zu diesem Menü zurückkehren, um Ihre Passphrase einzugeben und sie auf Ihre Brieftasche anzuwenden. Der Passport speichert die Passphrase nicht.

Überprüfen Sie bei jeder Entsperrung nach Eingabe der Passphrase auf diesem Bestätigungsbildschirm, ob der angegebene Fingerabdruck mit dem übereinstimmt, den Sie bei der Konfiguration eingegeben haben. Wenn dies der Fall ist, ist Ihre Passphrase korrekt und Sie haben Zugriff auf die richtige Bitcoin-Wallet. Ist dies nicht der Fall, sind Sie auf der falschen Wallet und müssen es noch einmal versuchen, wobei Sie darauf achten sollten, keine Eingabefehler zu machen.

Bevor Sie Ihre ersten Bitcoins auf Ihrer Wallet erhalten, **empfehle ich Ihnen dringend, einen Test zur Wiederherstellung der leeren Wallet durchzuführen**. Notieren Sie sich einige Referenzinformationen, z. B. Ihre xpub- oder erste Empfangsadresse, und löschen Sie dann Ihre Geldbörse auf dem Passport, solange sie noch leer ist (Einstellungen -> Erweitert -> Passport löschen). Versuchen Sie dann, Ihre Brieftasche mit Hilfe Ihrer Sicherungskopien der mnemonischen Phrase und einer eventuellen Passphrase wiederherzustellen. Überprüfen Sie, ob die Cookie-Informationen, die nach der Wiederherstellung generiert werden, mit denen übereinstimmen, die Sie ursprünglich aufgeschrieben haben. Wenn dies der Fall ist, können Sie sicher sein, dass Ihre Sicherungskopien zuverlässig sind. Weitere Informationen über die Durchführung einer Testwiederherstellung finden Sie in diesem anderen Tutorial:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

![Image](assets/fr/53.webp)

## Konfigurieren der Brieftasche auf Sparrow Wallet

In diesem Tutorial zeige ich Ihnen eine fortgeschrittene Verwendung von Passport mit Sparrow Wallet. Diese Hardware-Geldbörse ist jedoch auch mit Envoy (der Foundation-Anwendung), Keeper, BlueWallet, Nunchuk, Specter und vielen anderen kompatibel...

Beginnen Sie mit dem Herunterladen und Installieren von Sparrow Wallet [von der offiziellen Website] (https://sparrowwallet.com/) auf Ihrem Computer, falls Sie dies noch nicht getan haben.

![Image](assets/fr/54.webp)

Stellen Sie sicher, dass Sie die Echtheit und Integrität der Software vor der Installation überprüfen. Wenn Sie nicht wissen, wie man das macht, lesen Sie bitte diese Anleitung:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Sobald Sparrow Wallet geöffnet ist, klicken Sie auf die Registerkarte "*Datei*" und dann auf "*New Wallet*".

![Image](assets/fr/55.webp)

Geben Sie Ihrer Geldbörse einen Namen und klicken Sie dann auf "*Geldbörse erstellen*".

![Image](assets/fr/56.webp)

Wählen Sie "*Airgapped Hardware Wallet*".

![Image](assets/fr/57.webp)

Klicken Sie auf "*Scannen...*" neben der Option "*Pass*". Dadurch wird Ihre Webcam geöffnet.

![Image](assets/fr/58.webp)

Gehen Sie auf Ihrer Hardware-Wallet zum Menü "*Konto*", wählen Sie das Untermenü "*Konto verwalten*" und klicken Sie auf "*Wallet verbinden*".

![Image](assets/fr/59.webp)

Wählen Sie in der erscheinenden Dropdown-Liste "*Sparrow*".

![Image](assets/fr/60.webp)

Wählen Sie dann "*Einzel-Sig*" für eine normale Konfiguration, ohne Multisig.

![Image](assets/fr/61.webp)

Wählen Sie die Option "*QR-Code*".

![Image](assets/fr/62.webp)

Ihr Passport generiert dann dynamische QR-Codes. Verwenden Sie die Webcam Ihres Computers, um diese in die Sparrow-Software zu scannen.

![Image](assets/fr/63.webp)

Sie sollten nun Ihren xpub und Ihren Hauptschlüssel-Fingerabdruck sehen, der mit dem auf Ihrem Passport angezeigten Fingerabdruck übereinstimmen sollte, wenn Sie Ihre Passphrase eingeben. Klicken Sie auf die Schaltfläche "*Apply*".

![Image](assets/fr/64.webp)

Legen Sie ein sicheres Passwort fest, um den Zugang zu Ihrer Sparrow-Geldbörse zu schützen. Dieses Passwort schützt Ihre öffentlichen Schlüssel, Adressen, Labels und den Transaktionsverlauf vor unbefugtem Zugriff. Es ist eine gute Idee, dieses Passwort in einem Passwort-Manager zu speichern, damit Sie es nicht vergessen.

![Image](assets/fr/65.webp)

Ihr Passport fordert Sie dann auf, die erste Empfangsadresse zu scannen, um zu bestätigen, dass der Import erfolgreich war.

![Image](assets/fr/66.webp)

Gehen Sie in Sparrow auf die Registerkarte "*Empfangen*" und scannen Sie den QR-Code der ersten Adresse.

![Image](assets/fr/67.webp)

Wenn der Vorgang erfolgreich war, wird in Ihrem Pass "*Verified*" angezeigt.

![Image](assets/fr/68.webp)

Dies bestätigt, dass der Import erfolgreich war.

![Image](assets/fr/69.webp)

## Bitcoins erhalten

Jetzt, da Ihr Passport eingerichtet ist, können Sie Ihre ersten Sats auf Ihrer neuen Bitcoin-Brieftasche empfangen. Klicken Sie dazu auf Sparrow auf das Menü "*Empfangen*".

![Image](assets/fr/70.webp)

Sparrow zeigt die erste leere Empfangsadresse in Ihrem Portfolio an. Sie können ein Etikett hinzufügen.

![Image](assets/fr/71.webp)

Bevor wir es verwenden, überprüfen wir die Adresse auf dem Passport-Bildschirm, um sicherzustellen, dass sie zu unserer Bitcoin-Wallet gehört. Auf Sparrow können Sie den QR-Code der Adresse vergrößern, indem Sie ihn anklicken, falls nötig. Wählen Sie in Ihrem Passport im Menü "*Konto*" die Option "*Kontotools*".

![Image](assets/fr/72.webp)

Klicken Sie auf "*Adresse prüfen*" und scannen Sie dann den QR-Code, der auf Sparrow Wallet angezeigt wird.

![Image](assets/fr/73.webp)

Vergewissern Sie sich, dass die auf dem Pass angezeigte Adresse genau mit der auf Sparrow angezeigten Adresse übereinstimmt und dass "*Verified*" angezeigt wird.

![Image](assets/fr/74.webp)

Sie können es jetzt verwenden, um Bitcoins zu empfangen. Wenn die Transaktion im Netzwerk übertragen wird, erscheint sie auf Sparrow. Warten Sie, bis Sie genügend Bestätigungen erhalten haben, um die Transaktion als endgültig zu betrachten.

![Image](assets/fr/75.webp)

## Bitcoins senden

Jetzt, wo Sie ein paar Sats in Ihrem Portemonnaie haben, können Sie auch welche verschicken. Klicken Sie dazu auf das Menü "*UTXOs*".

![Image](assets/fr/76.webp)

Wählen Sie die UTXOs aus, die Sie als Eingaben für diese Transaktion verwenden möchten, und klicken Sie dann auf "*Ausgewählte senden*".

![Image](assets/fr/77.webp)

Geben Sie die Adresse des Empfängers, ein Etikett, das Sie an den Zweck der Transaktion erinnert, und den Betrag ein, den Sie an diese Adresse senden möchten.

![Image](assets/fr/78.webp)

Passen Sie den Gebührensatz an die aktuellen Marktbedingungen an und klicken Sie dann auf "*Transaktion erstellen*".

![Image](assets/fr/79.webp)

Überprüfen Sie, ob alle Transaktionsparameter korrekt sind, und klicken Sie dann auf "*Transaktion zur Unterzeichnung abschließen*".

![Image](assets/fr/80.webp)

Klicken Sie auf "*QR anzeigen*", um die PSBT (*Partially Signed Bitcoin Transaction*) anzuzeigen. Sparrow hat die Transaktion erstellt, aber es fehlen noch die Signaturen, um die in der Eingabe verwendeten Bitcoins zu entsperren. Diese Signaturen können nur vom Passport durchgeführt werden, der Ihren Seed hostet und Zugang zu den privaten Schlüsseln gibt, die zum Signieren der Transaktion benötigt werden.

![Image](assets/fr/81.webp)

Rufen Sie in Ihrem Passport das Menü "*Konto*" auf und klicken Sie auf "*Mit QR-Code unterschreiben*".

![Image](assets/fr/82.webp)

Scannen Sie die PSBT (*Partially Signed Bitcoin Transaction*), die auf Sparrow Wallet angezeigt wird.

![Image](assets/fr/83.webp)

Vergewissern Sie sich, dass die Empfängeradresse und der gesendete Betrag korrekt sind, und drücken Sie dann die Bestätigungstaste.

![Image](assets/fr/84.webp)

Überprüfen Sie die Austauschadresse. In meinem Beispiel gibt es keine, da die Transaktion eine einzige Ausgabe enthält.

![Image](assets/fr/85.webp)

Vergewissern Sie sich, dass die Gebühr die von Ihnen gewählte ist.

![Image](assets/fr/86.webp)

Wenn alle Angaben korrekt sind, klicken Sie auf die Bestätigungsschaltfläche, um die Transaktion zu unterzeichnen.

![Image](assets/fr/87.webp)

Klicken Sie in Sparrow Wallet auf "*Scan QR*" und scannen Sie den QR-Code, der auf Ihrem Reisepass angezeigt wird.

![Image](assets/fr/88.webp)

Ihre signierte Transaktion ist nun bereit, in das Bitcoin-Netzwerk übertragen und von einem Miner in einen Block aufgenommen zu werden. Wenn alles korrekt ist, klicken Sie auf "*Broadcast Transaction*".

![Image](assets/fr/89.webp)

Ihre Transaktion wurde übertragen und wartet auf Bestätigung.

![Image](assets/fr/90.webp)

Herzlichen Glückwunsch, Sie wissen jetzt, wie Sie Passport konfigurieren und verwenden können. Wenn Sie diese Anleitung nützlich fanden, wäre ich Ihnen dankbar, wenn Sie unten einen grünen Daumen hinterlassen würden. Sie können diesen Artikel auch gerne in Ihren sozialen Netzwerken teilen. Vielen Dank fürs Teilen!

Weitere Informationen finden Sie in unserem Tutorium zur Liana-Software:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
