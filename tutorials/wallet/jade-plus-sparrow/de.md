---
name: Jade Plus - Sparrow
description: Erweiterte Konfiguration von Jade Plus mit Sparrow Wallet
---
![cover](assets/cover.webp)

Jade Plus ist eine reine Bitcoin-Hardware-Wallet, die von Blockstream entwickelt wurde. Es ist der Nachfolger des klassischen Jade, mit Software-Verbesserungen, mehr Optionen und neu gestalteter Ergonomie für eine intuitivere Nutzung. Diese neue Version verfügt über einen großartigen 1,9-Zoll-LCD-Bildschirm mit einem größeren Farbumfang als sein Vorgänger. Auch die Tasten und die Menüführung wurden optimiert.

Der Jade Plus kann auf verschiedene Arten verwendet werden: über eine USB-C-Kabelverbindung, im "*Air-Gap*"-Modus mit einer Micro-SD-Karte (Adapter erforderlich), über Bluetooth oder sogar durch den Austausch von QR-Codes dank der integrierten Kamera. Diese Hardware-Wallet ist batteriebetrieben.

Sie ist ab 149,99 $ in der schwarzen Grundversion erhältlich, und der Preis kann um bis zu 20 $ für die Versionen "*Genesis Grey*" oder "*Lunar Silver*" steigen. Die Jade Plus ist daher eine interessante Wahl, mit fortschrittlichen Funktionen, die mit denen von High-End-Hardware-Geldbörsen wie Coldcard Q oder Passport V2 vergleichbar sind, aber zu einem ziemlich niedrigen Preis, nahe an Mittelklasse-Modellen.

![JADE-PLUS-SPARROW](assets/fr/01.webp)

Jade Plus ist mit den meisten Portfolioverwaltungsprogrammen kompatibel. Hier ist eine Übersicht über die Kompatibilität zum Zeitpunkt der Erstellung dieses Berichts (Januar 2025):

| Desktop | Mobile | USB | Bluetooth | QR | JadeLink | Verwaltungssoftware

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 |

| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 |

| Sperling | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 |

| Nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |

| Specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |

| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |

| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |

| Keeper | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

In diesem Tutorial richten wir eine erweiterte Konfiguration des Jade Plus mit der Desktop-Software Sparrow Wallet im QR-Code-Modus ein. Diese Konfiguration ist ideal für fortgeschrittene oder erfahrene Benutzer. Wenn Sie einen einfacheren Ansatz für Anfänger suchen, empfehle ich Ihnen einen Blick auf dieses Tutorial, in dem wir den Jade Plus mit Green Wallet über eine Bluetooth-Verbindung verwenden:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## Das Sicherheitsmodell Jade Plus

Der Jade Plus verwendet ein Sicherheitsmodell, das auf einem "virtuellen Sicherheitselement" basiert, das durch ein "blindes Orakel" realisiert wird. Konkret kombiniert dieser Mechanismus die vom Benutzer gewählte PIN, ein auf dem Jade-Gerät gehostetes Geheimnis und ein vom Orakel (einem von Blockstream unterhaltenen Server) gehaltenes Geheimnis, um einen auf zwei Entitäten verteilten AES-256-Schlüssel zu erstellen. Während der Initiierung sichert ein ECDH-Austausch die Kommunikation mit dem Orakel und verschlüsselt die Recovery-Phrase auf der Hardware-Wallet. Wenn Sie auf den Seed zugreifen wollen, um Transaktionen zu signieren, benötigen Sie Zugang zu :


- Das Jade Plus Gerät selbst;
- PIN zum Entsperren des Geräts ;
- Und zum Geheimnis des Orakels.

Der Hauptvorteil dieses Ansatzes ist das Fehlen einer einzigen Schwachstelle auf der Hardware-Ebene, denn wenn ein Angreifer jemals Zugang zu Ihrer Jade erhält, muss er, um die Schlüssel zu extrahieren, gleichzeitig die Jade und das Orakel kompromittieren. Dieses Modell bedeutet auch, dass Jade Plus vollständig quelloffen ist und die Einschränkungen vermeidet, die mit der Verwendung echter physischer Sicherheitselemente verbunden sind, wie sie z. B. bei Ledger verwendet werden.

Der Nachteil dieses Systems ist, dass die Nutzung von Jade Plus von dem von Blockstream unterhaltenen Orakel abhängt. Wenn dieses Orakel unzugänglich wird, ist es nicht mehr möglich, die Hardware-Wallet direkt mit der PIN zu verwenden. Dies bedeutet jedoch nicht, dass Ihre Bitcoins verloren sind, da sie immer noch mit Hilfe Ihrer Wiederherstellungsphrase, die Sie in Jade Plus im Modus "*stateless*" eingeben können, wiederhergestellt werden können. Um diese Abhängigkeit zu umgehen, können Sie auch Ihren eigenen Orakel-Server konfigurieren und verwalten.

Eine weitere Möglichkeit, Ihr Saatgut zu verwalten, besteht darin, es einfach nicht auf dem Jade Plus zu registrieren. In diesem Fall wird der Jade zu einem reinen Signaturgerät. Während der Initialisierung speichern Sie die Wiederherstellungsphrase nicht nur wie üblich als Wörter, sondern auch als handgenerierten QR-Code. Auf diese Weise können Sie jedes Mal, wenn Sie Ihre Brieftasche verwenden, den Seed mit der Kamera Ihres Jade importieren. Dies kann eine interessante Option für fortgeschrittene Benutzer sein, abhängig von Ihrer Sicherheitsstrategie, aber Sie müssen darauf achten, Ihren Seed zu speichern und ihn zu schützen, denn selbst als QR-Code würde er es jedem ermöglichen, Ihr Geld zu stehlen. Wir werden uns diese Option in diesem Tutorial ansehen, aber sie ist nicht obligatorisch.

## Auspacken des Jade Plus

Wenn Sie Ihr Jade Plus erhalten, überprüfen Sie, ob die Verpackung und das Siegel in gutem Zustand sind, um sicherzustellen, dass das Paket nicht geöffnet wurde.

![JADE-PLUS-SPARROW](assets/fr/02.webp)

In der Box finden Sie :


- Le Jade Plus;
- USB-C-Kabel;
- Karten, um Ihre mnemonische Phrase als Wörter oder als "*CompactSeedQR*" zu speichern;
- Einige Hinweise zur Verwendung ;
- Eine Schnur;
- Einige Aufkleber.

![JADE-PLUS-SPARROW](assets/fr/03.webp)

Das Gerät verfügt über 4 Navigationstasten:


- Die Taste unten rechts schaltet die Jade ein;
- Die große Taste auf der Vorderseite des Geräts wird zur Auswahl eines Elements verwendet;
- Mit den beiden kleinen Schaltflächen am oberen Rand können Sie nach links und rechts navigieren;
- Sie können ein Element auch auswählen, indem Sie gleichzeitig auf die beiden Schaltflächen am oberen Rand des Geräts klicken.

![JADE-PLUS-SPARROW](assets/fr/04.webp)

## Einrichten einer neuen Bitcoin-Brieftasche

Klicken Sie auf die Schaltfläche Start.

![JADE-PLUS-SPARROW](assets/fr/05.webp)

Klicken Sie auf "*Setup Jade*".

![JADE-PLUS-SPARROW](assets/fr/06.webp)

Wählen Sie "Erweiterte Einstellungen".

![Image](assets/fr/07.webp)

Klicken Sie dann auf "*Neue Geldbörse erstellen*", um einen neuen Seed zu erzeugen. Sie können zwischen einer 12- oder 24-Wort-Mnemonik wählen. Die Sicherheit Ihres Wallets bleibt bei beiden Optionen gleich, daher kann es bequemer sein, die einfachste Option zum Speichern zu wählen, d. h. 12 Wörter.

![Image](assets/fr/08.webp)

Klicken Sie auf die Schaltfläche "*Fortfahren*", um Ihre neue Wiederherstellungsphrase anzuzeigen.

![Image](assets/fr/09.webp)

Ihr Jade Plus zeigt Ihre 12-Wort-Merkhilfe an. **Mit diesem Merksatz haben Sie uneingeschränkten Zugriff auf alle Ihre Bitcoins. Jeder, der im Besitz dieser Phrase ist, kann Ihr Geld stehlen, auch ohne physischen Zugang zu Ihrem Jade Plus. Die 12-Wort-Phrase stellt den Zugang zu Ihren Bitcoins im Falle von Verlust, Diebstahl oder Bruch Ihrer Jade wieder her. Es ist daher sehr wichtig, dass Sie sie sorgfältig aufbewahren und an einem sicheren Ort aufbewahren.**

Sie können die Gravur auf dem mitgelieferten Karton anbringen. Für zusätzliche Sicherheit empfehle ich, die Gravur auf einem Edelstahlsockel anzubringen, um sie vor Feuer, Überschwemmung oder Einsturz zu schützen.

![Image](assets/fr/10.webp)

Für weitere Informationen über die richtige Art und Weise, wie Sie Ihre mnemotechnische Phrase speichern und verwalten können, empfehle ich Ihnen, diese andere Anleitung zu lesen, insbesondere wenn Sie Anfänger sind:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

natürlich dürfen Sie diese Worte niemals im Internet weitergeben, wie ich es in diesem Tutorium tue. Dieses Musterportfolio wird nur im Testnet verwendet und am Ende des Tutoriums gelöscht.

Klicken Sie auf den Pfeil auf der rechten Seite des Bildschirms, um die folgenden Wörter anzuzeigen.

![Image](assets/fr/11.webp)

Sobald Sie Ihren Satz gespeichert haben, fordert Jade Plus Sie auf, ihn zu bestätigen. Wählen Sie das richtige Wort entsprechend der Reihenfolge mit den Tasten oben auf dem Gerät aus und klicken Sie auf die mittlere Taste, um zum nächsten Wort zu gelangen.

![Image](assets/fr/12.webp)

Sie haben dann 2 Möglichkeiten. Wie in der Einleitung erläutert, können Sie Ihren Seed direkt auf dem Gerät speichern und das "*Virtual Secure Element*"-Schutzsystem von Blockstream verwenden, um auf Ihre Wallet zuzugreifen (Option 1), oder Sie können Ihren Seed als QR-Code speichern und ihn bei jeder Verwendung scannen (Option 2).

Wählen Sie für Option 1 "*Nein*" und für Option 2 "*Ja*".

![Image](assets/fr/13.webp)

### Option 1: QR-PIN-Entsperrung

Wenn Sie die Option 1 (CompactSeedQR: "*No*") gewählt haben, werden Sie direkt zur Auswahl der Verbindungsmethode weitergeleitet. In diesem Tutorial wollen wir das Gerät im Air-Gap-Modus über QR-Code-Austausch verwenden, also wählen Sie "*QR*".

![Image](assets/fr/27.webp)

Klicken Sie auf "*Fortfahren*".

![Image](assets/fr/28.webp)

Der PIN-Code wird verwendet, um Ihre Jade zu entsperren und bietet Schutz vor unbefugtem physischen Zugriff. Dieser PIN-Code ist nicht an der Ableitung der kryptografischen Schlüssel Ihrer Geldbörse beteiligt. Selbst wenn Sie keinen Zugang zu diesem PIN-Code haben, können Sie mit der 12-Wort-Mnemonik wieder Zugang zu Ihren Bitcoins erhalten. Wir empfehlen, einen möglichst zufälligen PIN-Code zu wählen. Stellen Sie außerdem sicher, dass Sie diesen Code an einem anderen Ort speichern als Ihre Jade, z. B. in einem Passwort-Manager.

Wählen Sie einen 6-stelligen PIN-Code auf Ihrer Jade, indem Sie mit der linken und rechten Taste durch die Ziffern blättern und mit der mittleren Taste jede Ziffer bestätigen.

![Image](assets/fr/29.webp)

Bestätigen Sie Ihre PIN ein zweites Mal.

![Image](assets/fr/30.webp)

Wie in der Einleitung erläutert, wird Ihr Seed verschlüsselt auf dem Jade Plus gespeichert. Um ihn zu entschlüsseln, müssen Sie :


- Der gültige PIN-Code (den wir gerade eingerichtet haben) ;
- Das Geheimnis des von Blockstream verwalteten Orakels.

In diesem Tutorial für Fortgeschrittene werden wir Sparrow Wallet verwenden, um unsere Bitcoin-Wallet zu verwalten. Im Gegensatz zur Green-Wallet-Software von Blockstream hat Sparrow jedoch keinen Zugriff auf das Orakel auf den Servern von Blockstream. Wir werden daher die Website von Blockstream nutzen, um das Orakelgeheimnis jedes Mal abzurufen, wenn wir Jade Plus entsperren.

Besuchen Sie https://jadefw.blockstream.com/pinqr/index.html

Klicken Sie auf "*Start QR Unlock*".

![Image](assets/fr/31.webp)

Klicken Sie auf "*Erledigt*", da Sie Ihre PIN bereits auf dem Jade Plus gewählt haben.

![Image](assets/fr/32.webp)

Verwenden Sie die Kamera Ihres Computers, um die auf dem Bildschirm Ihres Jade angezeigten QR-Codes zu scannen.

![Image](assets/fr/33.webp)

Bestätigen Sie auf Ihrer Jade, um auf den nächsten Bildschirm zu gelangen.

![Image](assets/fr/34.webp)

Scannen Sie den QR-Code, der jetzt auf der Website sichtbar ist, um das Geheimnis des Orakels zu erfahren.

![Image](assets/fr/35.webp)

Da Ihr Portfolio nun erstellt wurde, können Sie mit den nächsten Schritten fortfahren und den Unterabschnitt "*Option 2: CompactSeedQR*" überspringen.

![Image](assets/fr/36.webp)

Klicken Sie bei jedem Neustart auf "*QR-Modus*".

![Image](assets/fr/37.webp)

Wählen Sie "*QR PIN Unlock*".

![Image](assets/fr/38.webp)

Geben Sie Ihren PIN-Code ein.

![Image](assets/fr/39.webp)

Gehen Sie dann auf [die Blockstream-Website] (https://jadefw.blockstream.com/pinqr/qrpin.html), um QR-Codes mit dem Orakel auszutauschen.

![Image](assets/fr/40.webp)

Deine Jade ist jetzt freigeschaltet.

![Image](assets/fr/41.webp)

### Möglichkeit 2: CompactSeedQR

Wenn Sie Option 2 (CompactSeedQR: "*Ja*") gewählt haben, klicken Sie erneut auf "*Ja*".

![Image](assets/fr/14.webp)

Klicken Sie auf "*Start*".

![Image](assets/fr/15.webp)

Sie können die QR-Code-Basis verwenden, die in der Jade Plus Box enthalten ist. Wählen Sie das entsprechende Feld aus, je nachdem, ob Sie sich für einen Satz mit 12 oder 24 Wörtern entschieden haben. Sie können auch [die Vorlage von der Blockstream-Website drucken] (https://help.blockstream.com/hc/article_attachments/41928319071769).

Ihr Jade Plus zeigt jeden Bereich Ihres QR-Codes an.

![Image](assets/fr/16.webp)

Verwenden Sie einen Stift, um die Quadrate auszumalen und Ihr Saatgut als QR-Code abzubilden. Seien Sie präzise, damit die Jade Plus Kamera ihn später scannen kann. Verwenden Sie den Pfeil, um zum nächsten Bereich zu gelangen.

![Image](assets/fr/17.webp)

Wenn Sie fertig sind, klicken Sie auf "*Erledigt*".

![Image](assets/fr/18.webp)

Scannen Sie Ihren handgefertigten QR-Code mit dem Jade Plus, um seine Gültigkeit zu überprüfen.

![Image](assets/fr/19.webp)

Wenn die Sicherung Ihres Papiers korrekt ist, klicken Sie auf "*Fortfahren*".

![Image](assets/fr/20.webp)

In diesem Tutorial werden wir einen Verbindungsmodus verwenden, der ausschließlich auf dem Scannen von QR-Codes basiert, also wählen Sie "*QR*".

![Image](assets/fr/21.webp)

Sie können auch wählen, ob Sie zusätzlich zu Ihrem CompactSeedQR-Backup eine PIN hinzufügen möchten, wie in Option 1. Dies bietet zwei Möglichkeiten für den Zugriff auf Ihre Geldbörse: entweder über die PIN und das "Virtual Secure Element"-System von Blockstream oder über den CompactSeedQR.

Wenn Sie sich für die Option der doppelten PIN entscheiden, wählen Sie "*PIN*" und folgen Sie denselben Schritten wie bei Option 1, um Ihren PIN-Code festzulegen.

Wenn Sie nur mit CompactSeedQR fortfahren möchten, wählen Sie "*SeedQR*".

![Image](assets/fr/22.webp)

Nachdem Sie nun Ihr Portfolio erstellt haben, können Sie zu den nächsten Schritten übergehen.

![Image](assets/fr/23.webp)

Klicken Sie bei jedem Start auf die Schaltfläche "*QR-Modus*" und dann auf "*Scan SeedQR*".

![Image](assets/fr/24.webp)

Verwenden Sie die Kamera des Geräts, um Ihr gespeichertes Saatgut als QR-Code zu scannen.

![Image](assets/fr/25.webp)

Deine Jade ist jetzt freigeschaltet.

![Image](assets/fr/26.webp)

## Hinzufügen einer BIP39-Passphrase

Eine BIP39-Passphrase ist ein optionales Passwort, das Sie frei wählen können und das zu Ihrer mnemonischen Phrase hinzugefügt wird, um die Sicherheit Ihrer Wallet zu erhöhen. Wenn diese Funktion aktiviert ist, erfordert der Zugriff auf Ihre Bitcoin-Wallet sowohl die Eselsbrücke als auch die Passphrase. Ohne beides wäre es unmöglich, die Wallet wiederherzustellen.

Bevor Sie diese Option auf Ihrem Jade Plus konfigurieren, empfehlen wir Ihnen dringend, diesen Artikel zu lesen, um die theoretische Funktionsweise der Passphrase vollständig zu verstehen und Fehler zu vermeiden, die zum Verlust Ihrer Bitcoins führen könnten:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Rufen Sie bei noch gesperrtem Jade (die Passphrase kann nur eingegeben werden, wenn das Gerät nicht entsperrt ist) das Menü "*Optionen*" auf.

![Image](assets/fr/42.webp)

Wählen Sie "*BIP39 Passphrase*".

![Image](assets/fr/43.webp)

In der Option "*Häufigkeit*" können Sie wählen, ob Jade Plus Sie bei jedem Start zur Eingabe Ihrer Passphrase auffordern soll:


- mit "*Deaktiviert*" wird die Verwendung einer Passphrase deaktiviert;
- mit der Option "*Nur bei nächster Anmeldung*" müssen Sie zu diesem Menü zurückkehren, um die Abfrage Ihrer Passphrase beim nächsten Start zu aktivieren. Mit dieser Option können Sie die Verwendung der Passphrase nicht preisgeben;
- "Die Option *Immer fragen* veranlasst Jade, Sie bei jedem Start systematisch nach Ihrer Passphrase zu fragen und so zu zeigen, dass Ihre Brieftasche durch eine Passphrase geschützt ist.

Wählen Sie die Option entsprechend Ihrer Sicherheitsstrategie. Ich persönlich wähle für das Beispiel "*Immer fragen*".

![Image](assets/fr/44.webp)

Sie können dann zwischen zwei Methoden zur Eingabe Ihrer Passphrase wählen:


- "*Manuell*: Über eine virtuelle Tastatur können Sie Buchstaben (Groß- und Kleinschreibung), Zahlen und Symbole Zeichen für Zeichen eingeben. Dies ist die Standardmethode für alle Hardware-Geldbörsen;
- "*WordList*": Spezifische, von Blockstream für Jade entwickelte Methode, die die Eingabe der Passphrase beschleunigt und ihre Entropie erhöht. Während der Eingabe schlägt das System Wörter aus der BIP39-Liste vor, was die Entsperrung erleichtert. Diese Methode generiert automatisch einen Satz, indem die gewählten Wörter durch Leerzeichen getrennt aneinandergereiht werden (Beispiel: `abandon ability able`).

Ich persönlich empfehle Ihnen, die erste Methode zu verwenden, da sie der Standard ist, den Sie auf allen anderen Portfolioträgern finden werden.

![Image](assets/fr/45.webp)

Sie können dann zum Startbildschirm zurückkehren und Ihr Portemonnaie wie gewohnt entsperren, entweder mit Ihrem PIN-Code oder Ihrem CompactSeedQR (wie oben zu sehen). Sie werden dann aufgefordert, Ihre Passphrase einzugeben.

![Image](assets/fr/46.webp)

Geben Sie es auf der Jade-Tastatur ein, und machen Sie auf jeden Fall eine oder mehrere Sicherungskopien auf physischen Medien (Papier oder Metall). Für das Beispiel habe ich eine sehr schwache Passphrase verwendet, aber Sie müssen eine starke, zufällige Passphrase wählen, die alle Arten von Zeichen enthält und lang genug ist (wie ein starkes Passwort).

![Image](assets/fr/47.webp)

Wenn Ihre Passphrase gültig ist, bestätigen Sie.

![Image](assets/fr/48.webp)

Bitte beachten Sie, dass bei BIP39-Passphrasen zwischen Groß- und Kleinschreibung unterschieden wird. Wenn Sie eine Passphrase eingeben, die sich geringfügig von der ursprünglich konfigurierten unterscheidet, meldet Jade keinen Fehler, sondern leitet einen anderen Satz kryptografischer Schlüssel ab, der sich von dem in Ihrem ursprünglichen Portfolio unterscheidet.

Daher ist es wichtig, dass Sie sich bei der Konfiguration den Fingerabdruck Ihres Hauptschlüssels notieren, den Sie in der unteren rechten Ecke des Bildschirms finden. Bei meiner Passphrase `PBN` lautet mein Hauptschlüssel-Fingerabdruck zum Beispiel `3AD1AE65`.

![Image](assets/fr/49.webp)

Jedes Mal, wenn Sie Ihre Jade mit Ihrer Passphrase entsperren, überprüfen Sie, ob der Fingerabdruck mit dem übereinstimmt, den Sie bei der Konfiguration eingegeben haben. Wenn dies der Fall ist, ist Ihre Passphrase korrekt und Sie greifen auf die richtige Bitcoin-Wallet zu. Ist dies nicht der Fall, sind Sie auf der falschen Wallet und müssen es erneut versuchen, wobei Sie darauf achten sollten, keine Eingabefehler zu machen.

Bevor Sie Ihre ersten Bitcoins in Ihrem Wallet erhalten, **empfehle ich Ihnen dringend, einen leeren Recovery-Test** durchzuführen. Notieren Sie sich einige Referenzinformationen, z. B. Ihre xpub- oder erste Empfangsadresse, und löschen Sie dann Ihre Geldbörse auf dem Jade Plus, solange sie noch leer ist (Optionen -> Gerät -> Werksreset). Versuchen Sie dann, Ihre Brieftasche mit Hilfe Ihrer Sicherungskopien der mnemonischen Phrase und einer Passphrase wiederherzustellen. Überprüfen Sie, ob die Cookie-Informationen, die nach der Wiederherstellung generiert werden, mit denen übereinstimmen, die Sie ursprünglich aufgeschrieben haben. Wenn dies der Fall ist, können Sie sicher sein, dass Ihre Sicherungskopien zuverlässig sind. Wenn Sie mehr darüber erfahren möchten, wie Sie eine Testwiederherstellung durchführen, sehen Sie sich diesen anderen Lehrgang an:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Konfigurieren der Brieftasche auf Sparrow Wallet

In diesem Tutorial stelle ich eine fortgeschrittene Verwendung von Jade Plus mit Sparrow Wallet vor. Diese Hardware-Geldbörse ist jedoch mit vielen anderen Programmen kompatibel, wie Liana, Nunchuk, Specter, Green und Keeper. Diese Kompatibilitäten variieren in Bezug auf die Verbindungen: USB, Bluetooth oder QR-Code (siehe Tabelle in der Einleitung für Details).

Beginnen Sie mit dem Herunterladen und Installieren von Sparrow Wallet [von der offiziellen Website] (https://sparrowwallet.com/) auf Ihrem Computer, falls Sie dies noch nicht getan haben.

![Image](assets/fr/50.webp)

Stellen Sie sicher, dass Sie die Echtheit und Integrität der Software vor der Installation überprüfen. Wenn Sie nicht wissen, wie man das macht, lesen Sie bitte diese Anleitung:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Sobald Sparrow Wallet geöffnet ist, klicken Sie auf die Registerkarte "*Datei*" und dann auf "*New Wallet*".

![Image](assets/fr/51.webp)

Geben Sie Ihrer Geldbörse einen Namen und klicken Sie dann auf "*Geldbörse erstellen*".

![Image](assets/fr/52.webp)

Wählen Sie "*Airgapped Hardware Wallet*".

![Image](assets/fr/53.webp)

Klicken Sie auf "*Scan...*" neben der Option "*Jade*".

![Image](assets/fr/54.webp)

Entsperren Sie Ihr Jade Plus und geben Sie, falls Sie eines verwenden, Ihre Passphrase ein. Gehen Sie dann zum Menü "*Optionen*", wählen Sie "*Wallet*" und klicken Sie auf "*Export Xpub*".

![Image](assets/fr/55.webp)

Ihr Jade zeigt Ihren Keystore über mehrere QR-Codes an. Scannen Sie diese auf Ihrem Gerät mit Sparrow.

![Image](assets/fr/56.webp)

Sie sollten nun Ihren xpub und Ihren Hauptschlüssel-Fingerabdruck sehen, der mit dem auf Ihrem Jade Plus übereinstimmen sollte. Klicken Sie auf "*Anwenden*".

![Image](assets/fr/57.webp)

Legen Sie ein sicheres Passwort fest, um den Zugang zu Ihrer Sparrow-Geldbörse zu schützen. Dieses Passwort schützt Ihre öffentlichen Schlüssel, Adressen, Labels und den Transaktionsverlauf vor unbefugtem Zugriff. Es ist eine gute Idee, dieses Passwort in einem Passwort-Manager zu speichern, damit Sie es nicht vergessen.

![Image](assets/fr/58.webp)

Ihr Portfolio ist nun korrekt auf Sparrow konfiguriert.

![Image](assets/fr/59.webp)

## Bitcoins erhalten

Nun, da Ihr Jade Plus konfiguriert ist, können Sie Ihre ersten Sats auf Ihrer neuen Bitcoin-Brieftasche empfangen. Klicken Sie dazu auf Sparrow auf das Menü "*Empfangen*".

![Image](assets/fr/60.webp)

Sparrow wird die erste leere Empfangsadresse in Ihrem Portfolio anzeigen.

![Image](assets/fr/61.webp)

Bevor wir sie verwenden, sollten wir sie auf dem Jade Plus-Bildschirm überprüfen, um sicherzustellen, dass sie zu unserer Bitcoin-Brieftasche gehört. Klicken Sie auf der Jade auf "*Scan QR*" und scannen Sie dann den QR-Code der auf Sparrow angezeigten Adresse.

![Image](assets/fr/62.webp)

Überprüfen Sie, ob die auf dem Bildschirm Ihres Jade angezeigte Adresse mit der auf Sparrow Wallet angezeigten Adresse übereinstimmt. Wenn dies der Fall ist, klicken Sie auf das Häkchen, um fortzufahren.

![Image](assets/fr/63.webp)

Ihre Hardware-Brieftasche bestätigt dann, dass diese Adresse zu Ihrer Brieftasche gehört und dass sie den zugehörigen privaten Schlüssel enthält.

![Image](assets/fr/64.webp)

Wenn die Adresse von Ihrer Jade validiert wurde, können Sie sie nun verwenden, um Bitcoins zu erhalten. Wenn die Transaktion im Netzwerk übertragen wird, erscheint sie auf Sparrow. Warten Sie, bis Sie genügend Bestätigungen erhalten haben, um die Transaktion als endgültig zu betrachten.

![Image](assets/fr/65.webp)

## Bitcoins senden

Jetzt, wo Sie ein paar Sats in Ihrer Brieftasche haben, können Sie auch welche verschicken. Klicken Sie dazu auf das Menü "*UTXOs*".

![Image](assets/fr/66.webp)

Wählen Sie die UTXOs aus, die Sie als Eingaben für diese Transaktion verwenden möchten, und klicken Sie dann auf "*Ausgewählte senden*".

![Image](assets/fr/67.webp)

Geben Sie die Adresse des Empfängers, ein Etikett, das Sie an den Zweck der Transaktion erinnert, und den Betrag ein, den Sie an diese Adresse senden möchten.

![Image](assets/fr/68.webp)

Passen Sie den Gebührensatz an die aktuellen Marktbedingungen an und klicken Sie dann auf "*Transaktion erstellen*".

![Image](assets/fr/69.webp)

Überprüfen Sie, ob alle Transaktionsparameter korrekt sind, und klicken Sie dann auf "*Transaktion zur Unterzeichnung abschließen*".

![Image](assets/fr/70.webp)

Klicken Sie auf "*QR anzeigen*", um die PSBT (*Partially Signed Bitcoin Transaction*) anzuzeigen. Sparrow hat die Transaktion erstellt, aber es fehlen noch die Signaturen, um die in der Eingabe verwendeten Bitcoins zu entsperren. Diese Signaturen können nur von Jade Plus durchgeführt werden, das Ihren Seed hostet und Zugang zu den privaten Schlüsseln gibt, die zum Signieren der Transaktion benötigt werden.

![Image](assets/fr/71.webp)

Klicken Sie auf Ihrem Jade Plus auf "*Scan QR*", um den auf Sparrow angezeigten PSBT zu scannen.

![Image](assets/fr/72.webp)

Vergewissern Sie sich, dass die Lieferadresse und der gesendete Betrag korrekt sind, und klicken Sie dann auf den Pfeil, um zu bestätigen.

![Image](assets/fr/73.webp)

Vergewissern Sie sich, dass der Gebührenbetrag mit dem von Ihnen gewählten Betrag übereinstimmt, und klicken Sie dann auf das Häkchensymbol in der oberen linken Ecke der Schnittstelle, um die Transaktion zu unterzeichnen.

![Image](assets/fr/74.webp)

Klicken Sie in Sparrow Wallet auf "*Scan QR*" und scannen Sie den QR-Code, der auf Ihrer Jade angezeigt wird.

![Image](assets/fr/75.webp)

Ihre signierte Transaktion ist nun bereit, in das Bitcoin-Netzwerk übertragen und von einem Miner in einen Block aufgenommen zu werden. Wenn alles korrekt ist, klicken Sie auf "*Broadcast Transaction*".

![Image](assets/fr/76.webp)

Ihre Transaktion wurde übertragen und wartet auf Bestätigung.

![Image](assets/fr/77.webp)

Herzlichen Glückwunsch, Sie wissen jetzt, wie Sie den Jade Plus im QR-Modus einrichten und verwenden können. Wenn Sie diese Anleitung nützlich fanden, wäre ich Ihnen dankbar, wenn Sie unten einen grünen Daumen hinterlassen würden. Sie können diesen Artikel auch gerne in Ihren sozialen Netzwerken teilen. Vielen Dank fürs Teilen!

Um weiter zu gehen, empfehle ich dieses andere Tutorial über den Jade Plus, wo wir ihn über Bluetooth mit der Green Mobile App konfigurieren:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0