---
name: Sperling Wallet
description: Installieren, Konfigurieren und Verwenden von Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet ist eine von Craig Raw entwickelte Bitcoin-Portfolioverwaltungssoftware zur Selbstverwahrung. Diese Open-Source-Software wird von Bitcoinern wegen ihrer vielen Funktionen und intuitiven Interface geschätzt.

Es gibt zwei Möglichkeiten, Sparrow zu verwenden:


- Wie ein Hot Wallet, bei dem Ihre privaten Schlüssel auf Ihrem PC gespeichert sind.
- Als Cold-Wallet-Manager, bei dem die privaten Schlüssel auf einem Hardware Wallet gespeichert sind. In diesem Modus manipuliert Sparrow nur öffentliche Wallet-Informationen, verfolgt Gelder, generiert Adressen und baut Transaktionen auf, aber die Hardware Wallet-Signatur ist erforderlich, um diese Transaktionen gültig zu machen. Es kann daher Anwendungen wie Ledger Live oder Trezor Suite ersetzen.

Sparrow unterstützt Geldbörsen mit einer und mehreren Unterschriften und ermöglicht eine flüssige Verwaltung mehrerer Geldbörsen. Sie können zum Beispiel gleichzeitig einen Wallet steuern, der mit einem Ledger verbunden ist, einen anderen mit einem Trezor, und auch einen Hot Wallet.

Die Software bietet auch fortschrittliche Münzkontrollfunktionen, mit denen Sie genau auswählen können, welche UTXOs in Ihren Transaktionen verwendet werden sollen, um Ihre Vertraulichkeit zu optimieren.

Was die Verbindung angeht, so können Sie mit Sparrow eine Verbindung zu Ihrem eigenen Bitcoin-Knoten herstellen, entweder aus der Ferne über einen Electrum-Server oder mit Bitcoin Core. Es ist auch möglich, einen öffentlichen Knoten zu verwenden, wenn Sie noch nicht Ihre eigene haben. Fernverbindungen werden über Tor hergestellt.

## Sperling Wallet einbauen

Rufen Sie [die offizielle Sparrow Wallet-Downloadseite] (https://sparrowwallet.com/download/) auf und wählen Sie die Softwareversion aus, die Ihrem Betriebssystem entspricht.

![Image](assets/fr/01.webp)

Es ist wichtig, die Integrität und Authentizität der Software zu überprüfen, bevor Sie sie installieren. Wenn Sie nicht wissen, wie man das macht, finden Sie hier eine vollständige Anleitung:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Sobald Sparrow installiert ist, können Sie die anfänglichen Erklärungsbildschirme überspringen und direkt zum Bildschirm für die Verbindungsverwaltung gehen.

![Image](assets/fr/02.webp)

## Verbindung mit dem Bitcoin-Netzwerk

Um mit dem Bitcoin-Netzwerk zu interagieren und Ihre Transaktionen zu übertragen, muss Sparrow mit einem Bitcoin-Knoten verbunden sein. Es gibt drei Hauptmöglichkeiten, diese Verbindung herzustellen:


- 🟡 Verwendung eines öffentlichen Knotens, d. h. Verbindung mit einem Knoten eines Drittanbieters, der solche Verbindungen zulässt. Wenn Sie keinen eigenen Bitcoin-Knoten haben, können Sie mit dieser Option schnell mit Sparrow beginnen. Allerdings sieht der Knoten, mit dem Sie sich verbinden, alle Ihre Transaktionen, was Ihre Vertraulichkeit gefährden könnte. Die Kontrolle über Ihre Schlüssel ist wichtig, aber ein eigener Knoten ist noch besser. Verwenden Sie diese Option also nur, wenn Sie gerade erst anfangen, und seien Sie sich der Risiken für Ihre Privatsphäre bewusst.
- 🟢 Verbindung mit einem Bitcoin Core-Knoten. Wenn Sie einen eigenen Bitcoin Core-Knoten haben, können Sie ihn mit Sparrow Wallet verbinden, entweder lokal, wenn Bitcoin Core auf demselben Computer installiert ist, oder per Fernzugriff.
- 🔵 Verbindung über einen Electrum-Server. Wenn Ihr Bitcoin-Knoten mit Electrs ausgestattet ist, wie es bei Node-in-a-Box-Lösungen wie Umbrel oder Start9 der Fall ist, können Sie sich von Sparrow aus mit ihm verbinden.

**Es ist vorzuziehen, eine Verbindung über Electrs oder Bitcoin Core auf Ihrem eigenen Knoten zu verwenden, um die Notwendigkeit, einem Dritten zu vertrauen, zu verringern und Ihre Vertraulichkeit zu optimieren**

### Verbindung zu einem öffentlichen Knoten 🟡

Die Verbindung zu einem öffentlichen Knoten ist sehr einfach. Klicken Sie auf die Registerkarte "*Public Server*".

![Image](assets/fr/03.webp)

Wählen Sie einen Knoten aus der Dropdown-Liste aus.

![Image](assets/fr/04.webp)

Klicken Sie dann auf "*Verbindung testen*".

![Image](assets/fr/05.webp)

Sobald die Verbindung hergestellt ist, zeigt Sparrow Wallet ein gelbes Häkchen in der unteren rechten Ecke von Interface an, um anzuzeigen, dass Sie mit einem öffentlichen Knoten verbunden sind.

![Image](assets/fr/06.webp)

### Anschließen an einen Bitcoin-Kern 🟢

Die zweite Methode zur Verbindung mit einem Bitcoin-Knoten besteht darin, Sparrow mit einem Bitcoin Core zu verbinden. Wenn Bitcoin Core auf demselben Rechner installiert ist, erfolgt die Authentifizierung über die Cookie-Datei. Wenn sich Bitcoin Core auf einem entfernten Rechner befindet, müssen Sie das in der Datei "Bitcoin.conf" definierte Passwort verwenden.

Bitte beachten Sie, dass Sie, wenn Sie einen beschnittenen Bitcoin-Kernknoten verwenden, nicht in der Lage sein werden, einen Wallet wiederherzustellen, der Transaktionen enthält, die vor den lokal gespeicherten Blöcken liegen. Für einen neuen Wallet, der auf Sparrow erstellt wurde, stellt dies jedoch kein Problem dar: Ihre neuen Transaktionen sind sichtbar, selbst bei einem beschnittenen Knoten.

Um einen Bitcoin Core-Knoten zu konfigurieren, können Sie je nach Betriebssystem eine der folgenden Anleitungen zu Rate ziehen:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Gehen Sie auf Sparrow auf die Registerkarte "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**Mit Bitcoin Core lokal:**

Wenn Bitcoin Core auf Ihrem Computer installiert ist, suchen Sie die Datei `Bitcoin.conf` unter den Softwaredateien. Wenn diese Datei nicht vorhanden ist, können Sie sie erstellen. Öffnen Sie sie mit einem Texteditor und fügen Sie die folgende Zeile ein:

```ini
server=1
```

Speichern Sie dann Ihre Änderungen.

Sie können dies auch über die Interface-Grafik von Bitcoin-QT tun, indem Sie zu "*Einstellungen*" navigieren > "*Optionen...*" und die Option "*RPC-Server aktivieren*" aktivieren.

Vergessen Sie nicht, die Software neu zu starten, nachdem Sie diese Änderungen vorgenommen haben.

![Image](assets/fr/08.webp)

Kehren Sie dann zu Sparrow Wallet zurück und geben Sie den Pfad zu Ihrer Cookie-Datei ein, die sich je nach Betriebssystem normalerweise im selben Ordner wie `Bitcoin.conf` befindet:

| **macOS** | ~/Library/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)

Lassen Sie die anderen Parameter wie vorgegeben, URL `127.0.0.1` und Port `8332`, und klicken Sie dann auf "*Verbindung testen*".

![Image](assets/fr/10.webp)

Die Verbindung ist hergestellt. In der unteren rechten Ecke erscheint ein Green-Häkchen, um anzuzeigen, dass Sie mit einem Bitcoin-Kernknoten verbunden sind.

![Image](assets/fr/11.webp)

**Mit Bitcoin Core-Fernbedienung:**

Wenn Bitcoin Core auf einem anderen Rechner installiert ist, der mit demselben Netzwerk verbunden ist, suchen Sie zunächst die Datei "Bitcoin.conf" unter den Softwaredateien. Wenn diese Datei noch nicht vorhanden ist, können Sie sie erstellen. Öffnen Sie diese Datei mit einem Texteditor und fügen Sie die folgende Zeile ein:

```ini
server=1
```

Nachdem Sie die Datei bearbeitet haben, speichern Sie sie im entsprechenden Ordner Ihres Betriebssystems:

| **macOS** | ~/Library/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

Dieser Vorgang kann auch über das grafische Bitcoin-QT Interface durchgeführt werden. Gehen Sie in das Menü "*Einstellungen*", dann "*Optionen...*", und aktivieren Sie die Option "*RPC-Server aktivieren*", indem Sie das entsprechende Kontrollkästchen aktivieren. Wenn die Datei `Bitcoin.conf` nicht existiert, können Sie sie direkt von diesem Interface aus erstellen, indem Sie auf "*Open Configuration File*" klicken.

![Image](assets/fr/12.webp)

Finden Sie die IP Address des Rechners, der Bitcoin Core in Ihrem lokalen Netzwerk hostet. Dazu können Sie ein Tool wie [Angry IP Scanner](https://angryip.org/) verwenden. Nehmen wir an, dass die IP Address Ihres Knotens "192.168.1.18" lautet.

Fügen Sie in der Datei "Bitcoin.conf" die folgenden Zeilen hinzu und setzen Sie "rpcbind=192.168.1.18" auf die IP Address Ihres Knotens.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/13.webp)

Fügen Sie in der Datei `Bitcoin.conf` einen Benutzernamen und ein Passwort für Fernverbindungen hinzu. Ersetzen Sie `loic` durch Ihren Benutzernamen und `my_password` durch ein sicheres Passwort:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/14.webp)

Starten Sie die Bitcoin-QT-Software nach dem Ändern und Speichern der Datei neu.

Sie können nun zu Sparrow Wallet zurückkehren. Gehen Sie auf die Registerkarte "*Benutzer/Passwort*". Geben Sie den Benutzernamen und das Passwort ein, die Sie in der Datei `Bitcoin.conf` konfiguriert haben. Belassen Sie die anderen Parameter als Standard, d.h. URL `127.0.0.1` und Port `8332`. Klicken Sie dann auf "*Verbindung testen*".

![Image](assets/fr/15.webp)

Die Verbindung wird hergestellt. In der unteren rechten Ecke erscheint ein Green-Häkchen, um anzuzeigen, dass Sie mit einem Bitcoin-Kernknoten verbunden sind.

![Image](assets/fr/16.webp)

### Verbinden mit einem Electrum-Server 🔵

Die letzte Option für die Verbindung ist die Verwendung eines entfernten Electrum-Servers. Mit dieser Methode können Sie sich von einem anderen Gerät aus über Tor mit Ihrem Knoten verbinden und einen Indexer nutzen, um Ihre Portfolios auf Sparrow schneller zu durchsuchen. Sie ist besonders geeignet, wenn du eine Node-in-a-Box-Lösung wie Umbrel oder Start9 hast, die es dir ermöglichen, Electrum mit einem einzigen Klick zu installieren.

Um dies zu tun, musst du die Tor `.onion' Address deines Electrum-Servers erhalten. Bei Umbrel z.B. findest du sie in der Electrs-Anwendung.

![Image](assets/fr/17.webp)

Rufen Sie auf dem Sparrow Wallet die Registerkarte "*Private Electrum*" auf.

![Image](assets/fr/18.webp)

Gib deine Tor Address in das dafür vorgesehene Feld ein. Die anderen Einstellungen können voreingestellt bleiben. Klicke dann auf "*Verbindung testen*".

![Image](assets/fr/19.webp)

Die Verbindung wird bestätigt. Wenn Sie dieses Fenster schließen, erscheint ein blaues Häkchen in der rechten unteren Ecke, das anzeigt, dass Sie mit einem Electrum-Server verbunden sind.

![Image](assets/fr/20.webp)

## Erstellen Sie ein warmes Portfolio

Nachdem der Sparrow Wallet für die Kommunikation mit dem Bitcoin-Netzwerk konfiguriert wurde, können Sie nun Ihren ersten Wallet erstellen. Dieser Abschnitt führt Sie durch die Erstellung eines Hot Wallet, d. h. eines Wallet, dessen private Schlüssel auf Ihrem Computer gespeichert sind. Da Ihr Computer eine komplexe Maschine ist, die mit dem Internet verbunden ist, stellt er eine sehr große Angriffsfläche dar. Daher sollte ein Hot Wallet nur für begrenzte Mengen an Bitcoins verwendet werden. Um größere Beträge zu speichern, sollten Sie sich für einen sicheren Wallet mit einem Hardware Wallet entscheiden. Wenn Sie genau das suchen, können Sie zum nächsten Abschnitt übergehen.

Um einen Hot Wallet zu erstellen, klicken Sie auf dem Sparrow Wallet-Startbildschirm auf die Registerkarte "*Datei*" und dann auf "*Neuer Wallet*".

![Image](assets/fr/21.webp)

Geben Sie einen Namen für Ihr Portfolio ein und klicken Sie auf "*Wallet* erstellen".

![Image](assets/fr/22.webp)

Oben auf dem Interface können Sie wählen, ob Sie ein "*Einzelsignatur*"- oder ein "*Multisignatur*"-Portfolio erstellen möchten. Direkt darunter wählen Sie die Art des Skripts, mit dem Sie Ihre UTXOs sperren. Ich empfehle Ihnen, den neuesten Standard zu verwenden: "*Taproot (P2TR)*".

![Image](assets/fr/23.webp)

Klicken Sie dann auf "*Neue oder importierte Software Wallet*".

![Image](assets/fr/24.webp)

Wählen Sie den BIP39-Standard, da er von praktisch allen Bitcoin-Portfolio-Softwareprogrammen unterstützt wird. Als Nächstes wählen Sie die Länge Ihrer Wiederherstellungsphrase. Derzeit ist eine 12-Wort-Phrase ausreichend, da beide ähnliche Sicherheit bieten, aber die 12-Wort-Phrase ist einfacher zu speichern.

![Image](assets/fr/25.webp)

Klicken Sie auf die Schaltfläche "*generate Neu*", um die generate Phrase Ihres Wallet zu ändern. Diese Phrase gibt Ihnen vollen, uneingeschränkten Zugriff auf alle Ihre Bitcoins. Jeder, der im Besitz dieser Phrase ist, kann Ihre Gelder stehlen, auch ohne physischen Zugang zu Ihrem Computer.

Die 12-Wort-Phrase stellt den Zugang zu Ihren Bitcoins im Falle von Verlust, Diebstahl oder Bruch Ihres Computers wieder her. Es ist daher sehr wichtig, sie sorgfältig zu speichern und an einem sicheren Ort aufzubewahren.

Sie können ihn auf Papier beschriften oder, für zusätzliche Sicherheit, auf Edelstahl gravieren, um ihn vor Feuer, Überschwemmung oder Einsturz zu schützen. Die Wahl des Mediums für Ihr Mnemonic hängt von Ihrer Sicherheitsstrategie ab, aber wenn Sie Sparrow als warmes Wallet mit moderaten Mengen verwenden, sollte Papier ausreichend sein.

Für weitere Informationen über die richtige Art und Weise, Ihren Mnemonic-Satz zu speichern und zu verwalten, empfehle ich Ihnen dringend, diese andere Anleitung zu befolgen, besonders wenn Sie ein Anfänger sind:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)

**Natürlich dürfen Sie diese Wörter niemals im Internet weitergeben, wie ich es in diesem Tutorial tue. Dieses Beispiel Wallet wird nur auf dem Testnet verwendet und wird am Ende des Tutorials gelöscht.**

Sie können auch ein passphrase BIP39 hinzufügen, indem Sie auf das Feld "*passphrase verwenden*" klicken. Warnung: Die Verwendung eines passphrase kann sehr nützlich sein, aber wenn Sie nicht verstehen, wie es funktioniert, kann es sehr riskant sein. Deshalb empfehle ich Ihnen dringend, diesen kurzen theoretischen Artikel zu diesem Thema zu lesen:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Wenn Sie Ihren Mnemonic und jeden passphrase auf einem physischen Medium gespeichert haben, klicken Sie auf "*Bestätigung der Sicherung*".

![Image](assets/fr/27.webp)

Geben Sie Ihre 12 Wörter erneut ein, um zu bestätigen, dass sie korrekt gespeichert wurden, und klicken Sie dann auf "*Schlüsselspeicher erstellen*".

![Image](assets/fr/28.webp)

Klicken Sie dann auf "*Import Keystore*", um generate Ihre Portfolio-Schlüssel aus dem Mnemonic-Satz zu übertragen.

![Image](assets/fr/29.webp)

Klicken Sie auf "*Anwenden*", um die Erstellung des Portfolios abzuschließen.

![Image](assets/fr/30.webp)

Legen Sie ein sicheres Passwort fest, um den Zugang zu Ihrem Sparrow-Portfolio zu schützen. Es ist eine gute Idee, dieses Passwort in einem Passwort-Manager zu speichern, damit Sie es nicht vergessen. Beachten Sie, dass dieses Passwort keine Rolle bei der Ableitung Ihrer Schlüssel spielt. Es wird nur für den Zugriff auf Ihren Wallet über Sparrow Wallet verwendet. Auch ohne dieses Kennwort reicht Ihre Mnemonic-Phrase also aus, um von jeder BIP39-kompatiblen Anwendung aus auf Ihre Bitcoins zuzugreifen.

![Image](assets/fr/31.webp)

Ihr Hot Wallet ist nun erstellt. Sie können den Abschnitt *Empfang von Bitcoins* in dieser Anleitung überspringen, wenn Sie nicht vorhaben, ein Hardware Wallet mit Sparrow zu verwenden.

## Verwaltung eines Cold-Portfolios

Die zweite Möglichkeit, Sparrow Wallet zu verwenden, besteht darin, ihn als Portfoliomanager mit einem Hardware Wallet einzurichten. In dieser Konfiguration verbleiben die privaten Schlüssel Ihres Bitcoin Wallet ausschließlich auf dem Hardware Wallet, während Sparrow nur auf die öffentlichen Informationen zugreift. Dieser Ansatz bietet ein höheres Maß an Sicherheit als die oben besprochenen Hot-Geldbörsen, da die privaten Schlüssel auf einem speziellen Gerät aufbewahrt werden, oft mit einem sicheren Chip, der nicht mit dem Internet verbunden ist und daher eine viel kleinere Angriffsfläche bietet als ein herkömmlicher Computer.

Es gibt zwei Möglichkeiten, Ihr Hardware Wallet mit Sparrow zu verbinden:


- Per Kabel, das üblicherweise mit Einsteigermodellen wie dem Trezor Safe 3 oder dem Ledger Nano S Plus verwendet wird;
- Im Air-Gap-Modus, d.h. ohne direkte kabelgebundene Verbindung, über eine MicroSD-Karte oder den QR-Code Exchange.

Sparrow unterstützt alle diese Kommunikationsmethoden und ist mit den meisten Hardware-Wallets auf dem Markt kompatibel.

In diesem Tutorial verwende ich ein Ledger Nano S mit einem Kabel, aber das Verfahren ist im Air-Gap-Modus ähnlich. Einzelheiten zu Ihrem Hardware Wallet finden Sie in der entsprechenden Anleitung zum Plan ₿ Network.

Bevor Sie beginnen, vergewissern Sie sich, dass das Wallet bereits auf Ihrem Hardware Wallet konfiguriert ist. Wenn Sie eine kabelgebundene Verbindung verwenden, schließen Sie es über das Kabel an Ihren Computer an.

Um den sogenannten "*Keystore*" (die öffentlichen Informationen, die zur Verwaltung des Portfolios benötigt werden) in Sparrow Wallet zu importieren, klicken Sie auf die Registerkarte "*Datei*" und dann auf "*Neues Wallet*".

![Image](assets/fr/32.webp)

Benennen Sie Ihr Portfolio und klicken Sie auf "*Wallet* erstellen". Ich empfehle Ihnen, den Namen Ihres Hardware Wallet einzugeben, um ihn später leicht identifizieren zu können.

![Image](assets/fr/33.webp)

Wählen Sie oben auf dem Interface zwischen einem "*Einzelsignatur*"- oder "*Multisignatur*"-Portfolio. Für unser Beispiel konfigurieren wir ein Portfolio mit einer Unterschrift.

Wählen Sie unten die Art des Skripts zum Sperren Ihrer UTXOs. Wenn Ihr Hardware Wallet dies unterstützt, schlage ich vor, dass Sie "*Taproot (P2TR)*" wählen.

![Image](assets/fr/34.webp)

Das weitere Vorgehen hängt von Ihrer Verbindungsmethode ab. Wenn Sie eine Air-Gap-Methode verwenden, wählen Sie "*Airgapped Hardware Wallet*". Befolgen Sie dann die für Ihr Gerät spezifischen Anweisungen.

![Image](assets/fr/35.webp)

Wenn Sie, wie in meinem Fall, eine Kabelverbindung verwenden, wählen Sie "*Verbundenes Hardware Wallet*".

![Image](assets/fr/36.webp)

Klicken Sie auf "*Scan*", damit Sparrow Ihr Gerät erkennt. Stellen Sie sicher, dass es eingesteckt und entsperrt ist. Bei einigen Modellen, z. B. dem Ledger, müssen Sie die Anwendung "*Bitcoin*" öffnen, um die Erkennung zu aktivieren.

![Image](assets/fr/37.webp)

Wählen Sie "*Schlüsselspeicher importieren*".

![Image](assets/fr/38.webp)

Klicken Sie auf "*Anwenden*", um die Erstellung des Portfolios abzuschließen.

![Image](assets/fr/39.webp)

Legen Sie ein sicheres Passwort fest, um den Zugang zu Ihrem Sparrow Wallet zu schützen. Dieses Passwort schützt Ihre öffentlichen Schlüssel, Adressen und den Transaktionsverlauf. Wir empfehlen, dass Sie es in einem Passwort-Manager speichern. Beachten Sie, dass dieses Passwort keine Rolle bei der Ableitung Ihrer Schlüssel spielt. Auch ohne es können Sie mit Ihrem Mnemonic über jede BIP39-kompatible Software wieder Zugang zu Ihren Bitcoins erhalten.

![Image](assets/fr/40.webp)

Ihr Verwaltungsportfolio ist nun auf Sparrow konfiguriert.

![Image](assets/fr/41.webp)

## Bitcoins erhalten

Jetzt, wo Ihr Wallet auf Sparrow eingerichtet ist, können Sie Bitcoins empfangen. Rufen Sie einfach das Menü "*Empfangen*" auf.

![Image](assets/fr/42.webp)

Sparrow zeigt das erste unbenutzte Address in Ihrem Wallet an. Sie können diesem Address ein "*Label*" hinzufügen, um sich in Zukunft an die Herkunft dieser Satoshis zu erinnern.

![Image](assets/fr/43.webp)

Wenn Sie ein Hot Wallet verwenden, kann das angezeigte Address sofort verwendet werden, entweder durch Kopieren oder durch Scannen des zugehörigen QR-Codes.

Wenn Sie ein Hardware Wallet verwenden, ist es sehr wichtig, dass Sie das Address auf dem Gerätebildschirm überprüfen, bevor Sie es verwenden. Bei kabelgebundenen Geräten schließen Sie Ihr Hardware Wallet an und entsperren es, dann klicken Sie in Sparrow auf "*Address anzeigen*". Vergewissern Sie sich, dass das auf Ihrem Hardware Wallet angezeigte Address mit dem in Sparrow angezeigten übereinstimmt.

![Image](assets/fr/44.webp)

Für Hardware Wallet Air-Gap-Benutzer variiert die Address-Verifizierung je nach Gerätemodell. Genaue Anweisungen finden Sie in der speziellen Plan ₿ Network-Anleitung.

Sobald die Transaktion vom Zahlungspflichtigen übermittelt wurde, wird sie auf der Registerkarte "*Transaktionen*" angezeigt. Sie können darauf klicken, um weitere Details zu erfahren, z. B. den txid.

![Image](assets/fr/45.webp)

Auf der Registerkarte "*Adressen*" finden Sie eine Liste mit allen Adressen Ihres Posteingangs. Sie können sehen, ob sie bereits verwendet wurden und ob ein Etikett hinzugefügt wurde. *Empfangen*"-Adressen sind diejenigen, die Sparrow anzeigt, wenn Sie auf "*Empfangen*" klicken, und sind für eingehende Zahlungen bestimmt. Die "*Ändern*"-Adressen werden für Exchange in Ihren Transaktionen verwendet, d.h. um den ungenutzten Teil Ihrer UTXOs in den Eingängen zurückzuholen.

![Image](assets/fr/46.webp)

Die Registerkarte "*UTXOs*" zeigt Ihnen alle Ihre UTXOs, d. h. die Bitcoin-Fragmente, die Sie besitzen. Sie können die Menge jedes UTXO und die zugehörige Bezeichnung sehen.

![Image](assets/fr/47.webp)

## Bitcoins senden

Jetzt, wo Sie ein paar Satoshis in Ihrem Wallet haben, haben Sie auch die Möglichkeit, welche zu versenden. Obwohl es mehrere Möglichkeiten gibt, dies zu tun, empfehle ich Ihnen, das Menü "*UTXOs*" zu verwenden, um eine genauere Kontrolle über die ausgegebenen Münzen zu haben (*Münzkontrolle*), anstatt direkt zum Menü "*Senden*" zu gehen (obwohl letzteres für Anfänger vielleicht ausreicht).

![Image](assets/fr/48.webp)

Wählen Sie die UTXOs aus, die Sie als Input für diese Transaktion verwenden möchten, und klicken Sie dann auf "*Ausgewählte senden*". Auf diese Weise können Sie die am besten geeigneten Quellen unter Ihren UTXOs auswählen, je nach Ihren Ausgaben und den Etiketten, die bei ihrem Eingang verwendet werden, um die Vertraulichkeit Ihrer Zahlungen zu optimieren. Achten Sie darauf, dass die Summe der ausgewählten UTXOs größer ist als der Betrag, den Sie senden möchten.

![Image](assets/fr/49.webp)

Geben Sie den Address des Empfängers in das Feld "*Zahlung an*" ein. Sie können den Address auch mit Ihrer Webcam scannen, indem Sie auf das Kamerasymbol klicken. Mit der Schaltfläche "*+Hinzufügen*" können Sie mehrere Adressen in einer einzigen Transaktion bezahlen.

![Image](assets/fr/50.webp)

Fügen Sie Ihrer Transaktion ein Etikett hinzu, das Sie an den Zweck der Transaktion erinnert. Dieses Etikett wird auch mit Ihrem eventuellen Exchange verbunden sein.

![Image](assets/fr/51.webp)

Geben Sie den Betrag ein, der an diese Address zu übermitteln ist.

![Image](assets/fr/52.webp)

Passen Sie den Gebührensatz an die aktuellen Marktbedingungen an. Sie können dies tun, indem Sie einen absoluten Gebührenwert eingeben oder den Gebührensatz mit dem Schieberegler anpassen.

![Image](assets/fr/53.webp)

Am unteren Rand des Interface können Sie zwischen "*Effizienz*" und "*Datenschutz*" wählen. In meinem Fall ist die Option "*Privatsphäre*" nicht verfügbar, da ich nur einen UTXO in diesem Portfolio habe. "*Effizienz*" entspricht einer klassischen Transaktion, während "*Privatsphäre*" eine Transaktion vom Typ Stonewall ist, eine Transaktionsstruktur, die Ihre Vertraulichkeit verstärkt, indem sie einen Mini-CoinJoin simuliert, was die Kettenanalyse komplexer macht.

![Image](assets/fr/54.webp)

Sparrow zeigt ein zusammenfassendes Diagramm an, das Ihre Eingaben, Ausgaben und Transaktionsgebühren zeigt (beachten Sie, dass Gebühren nicht wirklich eine Ausgabe sind, im Gegensatz zu dem, was dieses Diagramm vermuten lässt). Wenn Sie mit allem zufrieden sind, klicken Sie auf "*Transaktion erstellen*".

![Image](assets/fr/55.webp)

Dadurch gelangen Sie auf eine Seite, auf der der Elements Ihrer Transaktion angezeigt wird. Überprüfen Sie, ob alle Informationen korrekt sind, und klicken Sie dann auf "*Transaktion zur Unterzeichnung abschließen*".

![Image](assets/fr/56.webp)

Es ist wichtig, die Standardeinstellungen von Sighash beizubehalten. Um zu verstehen, warum, schauen Sie sich diesen Schulungskurs an, in dem ich alles erkläre, was Sie über Sighash wissen müssen:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

Auf dem nächsten Bildschirm variieren die Optionen je nach Typ des Wallet, den Sie verwenden:


- Für einen Hardware Wallet Air-Gap klicken Sie auf "*QR anzeigen*", um einen PSBT anzuzeigen, den Sie mit Ihrem Gerät signieren können, und laden dann den signierten PSBT mit "*QR scannen*" in Sparrow. Die Option "*Transaktion speichern*" funktioniert auf ähnliche Weise, aber mit Austauschvorgängen auf einer microSD ;
- Bei einem Hot Wallet klicken Sie einfach auf "*Unterschreiben*" und geben das Wallet-Passwort ein, um zu unterschreiben;
- Bei einem kabelgebundenen Hardware Wallet klicken Sie auch auf "*Signieren*", um die unsignierte Transaktion an Ihr Gerät zu senden.

![Image](assets/fr/57.webp)

Überprüfen Sie auf Ihrem Hardware Wallet den Address des Empfängers, den gesendeten Betrag und die Gebühren. Wenn alles korrekt ist, fahren Sie mit der Unterschrift fort.

Sobald die Transaktion signiert wurde, erscheint sie wieder in Sparrow und ist bereit, im Bitcoin-Netzwerk gesendet zu werden, um anschließend in einen Block aufgenommen zu werden. Wenn alles korrekt ist, klicken Sie auf "*Broadcast Transaction*".

![Image](assets/fr/58.webp)

Ihre Transaktion wird nun übertragen und wartet auf Bestätigung.

![Image](assets/fr/59.webp)

## Verwalten und Konfigurieren von Portfolios auf Sparrow

Auf der Registerkarte "*Einstellungen*" finden Sie detaillierte Informationen zu Ihrem Portfolio, wie z. B. :


- Portfoliotyp (Einzelunterschrift oder multi-sig) ;
- Art der verwendeten Schrift ;
- Der Name, den Sie dem Portfolio zugewiesen haben;
- Aufdruck Hauptschlüssel;
- Der Bypass-Pfad ;
- Der erweiterte öffentliche Schlüssel des Kontos.

![Image](assets/fr/60.webp)

Mit der Schaltfläche "*Export*" können Sie Ihre Portfoliodaten exportieren, so dass Sie sie in anderer Software verwenden können, während die in Sparrow eingerichteten Informationen erhalten bleiben.

Mit der Schaltfläche "*Konto hinzufügen*" können Sie ein zusätzliches Konto zu Ihrem Portfolio hinzufügen. Ein Konto entspricht einem separaten Satz von Posteingangsadressen. Diese Funktion kann zum Beispiel nützlich sein, wenn Sie ein privates und ein geschäftliches Konto mit einem einzigen Mnemonic-Satz trennen möchten.

Die Schaltfläche "*Erweitert*" ermöglicht den Zugriff auf erweiterte Einstellungen, wie z. B. die Anpassung der Address-Suche von Sparrow und die Änderung des Portfolio-Passworts.

![Image](assets/fr/61.webp)

Wenn Sie Sparrow Wallet schließen, wird Ihr Wallet automatisch gesperrt. Wenn Sie die Software das nächste Mal öffnen, werden Sie in einem Fenster aufgefordert, Ihr Wallet mit seinem Passwort zu entsperren.

![Image](assets/fr/62.webp)

Wenn sich dieses Fenster nicht öffnet oder wenn Sie ein anderes Portfolio auf Sparrow öffnen möchten, klicken Sie auf die Registerkarte "*Datei*" und wählen Sie "*Wallet* öffnen".

![Image](assets/fr/63.webp)

Dadurch wird Ihr Dateimanager zu dem Ordner geöffnet, in dem Sparrow Ihre Geldbörsen speichert. Wählen Sie einfach den Wallet aus, den Sie öffnen möchten, und geben Sie das Passwort ein, um ihn zu entsperren.

![Image](assets/fr/64.webp)

Im Menü "*Datei*" unter "*Einstellungen*" finden Sie die bereits in den vorangegangenen Abschnitten erläuterten Parameter für die Bitcoin-Netzwerkverbindung. Außerdem können Sie verschiedene Parameter wie die verwendete Einheit, die Fiat-Währung für die Umrechnung und die Informationsquellen einstellen.

![Image](assets/fr/65.webp)

Die Registerkarte "*Ansicht*" bietet Anpassungsoptionen und Zugang zu einigen nützlichen Befehlen, wie z. B. "*Wallet* aktualisieren", mit dem die Transaktionssuche für Ihr Portfolio aktualisiert wird.

![Image](assets/fr/66.webp)

Auf der Registerkarte "*Tools*" sind mehrere fortgeschrittene Tools zusammengefasst, darunter :


- mit "*Sign/Verify Message*" können Sie den Besitz eines empfangenen Address nachweisen oder eine Signatur überprüfen.
- "*Senden an viele*" bietet ein vereinfachtes Interface für die Durchführung von Transaktionen an mehrere Empfängeradressen gleichzeitig, was für Stapelausgaben praktisch ist.
- mit "*Sweep Private Key*" können Sie Bitcoins abrufen, die durch einen einfachen privaten Schlüssel gesichert sind, und sie auf Ihren Sparrow Wallet übertragen. Dies kann besonders für diejenigen nützlich sein, die Bitcoins aus den frühen 2010er Jahren besitzen, also vor der Ära der HD-Wallets.
- "Download überprüfen" prüft die Integrität und Authentizität der heruntergeladenen Software, bevor sie auf Ihrem Gerät installiert wird.
- mit "*Restart In*" können Sie zu Ihren Geldbörsen auf Testnet oder Signet-Netzwerken wechseln. Dies kann nützlich sein, wenn Sie auf Testnetzwerke mit Münzen ohne echten Wert zugreifen möchten.

![Image](assets/fr/67.webp)

Sie wissen jetzt alles über die Sparrow Wallet Software, ein hervorragendes Werkzeug für die tägliche Verwaltung Ihrer Bitcoin Portfolios.

Wenn Sie dieses Tutorial nützlich fanden, wäre ich Ihnen sehr dankbar, wenn Sie unten einen Green-Daumen hinterlassen würden. Sie können es auch gerne in Ihren sozialen Netzwerken teilen. Ich danke Ihnen sehr!

Ich empfehle auch dieses andere Tutorial, in dem ich erkläre, wie man die Hardware Wallet COLDCARD Q mit Sparrow Wallet konfiguriert:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3