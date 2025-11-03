---
name: COLDCARD Mk

description: Erstellung, Sicherung und Verwendung eines Bitcoin-Privatschlüssels mit einer Coldcard und Bitcoin Core
---

![cover](assets/cover.webp)

Erstellung, Sicherung und Verwendung eines Bitcoin-Privatschlüssels mit einer Coldcard und Bitcoin Core

## Vollständiger Leitfaden zur Generierung eines Privatschlüssels mit einer Coldcard und zur Verwendung über die Benutzeroberfläche Ihres Bitcoin Core-Knotens!

Der Grundgedanke hinter der Nutzung des Bitcoin-Netzwerks ist das Konzept der asymmetrischen Kryptographie: ein Schlüsselpaar - ein privater und ein öffentlicher Schlüssel - das zum Verschlüsseln und Entschlüsseln von Daten dient und die Vertraulichkeit einer Kommunikation gewährleistet.

Im Falle von Bitcoin generieren wir durch die Erzeugung eines solchen privaten und öffentlichen Schlüsselpaars die Möglichkeit, Bitcoins (UTXO oder Unspent Transaction Output) zu speichern und Transaktionen zu signieren, um diese auszugeben.

Heutzutage gibt es viele Tools, die die zufällige Generierung eines privaten Schlüssels und dessen Sicherung in Textform erleichtern, indem sie das BIP 39 verwenden - einen Standard, der festlegt, wie Wallets einer mnemonischen Phrase (Seed-Phrase) Schlüssel zuordnen. Die mnemonische Phrase besteht in der Regel aus 12 oder 24 Wörtern, die unbedingt sicher aufbewahrt werden müssen, um das Wallet und die Bitcoins wiederherstellen zu können.

In diesem Artikel werden wir lernen, wie man mit einer Coldcard Mk4 einen privaten Schlüssel generiert, einem der verbreitetsten und sichersten Geräte in der Bitcoin-Welt, indem wir die Methode des Würfelwurfs verwenden, um eine maximale Entropie zu gewährleisten, und wie man ihn mit Bitcoin Core luftdicht (air-gapped) verwendet!

> 🧰| Bitte bereiten Sie folgende Werkzeuge vor, um dem Leitfaden zu folgen:
>
> - Coldcard-Gerät (Mk3 oder Mk4)
> - MicroSD-Karte (4GB ausreichend)
> - Magnetisches USB-Kabel nur für Stromversorgung (Mini-USB für Mk3, USB-C für Mk4)
> - Ein oder mehrere hochwertige Würfel

## Generierung einer neuen mnemonischen Phrase mit einer Coldcard

Wir werden den Prozess der Erstellung eines privaten Schlüssels von Anfang an beginnen, wobei wir davon ausgehen, dass eine frisch ausgepackte Coldcard vorhanden ist, auf der bereits eine PIN konfiguriert wurde (folgen Sie den Schritten auf der Coldcard während der Geräteinitialisierung).

> 🚨 | Um den privaten Schlüssel einer bereits konfigurierten Coldcard zurückzusetzen, befolgen Sie diese Schritte:
> Advanced/Tools > Danger Zone > Seed Functions > Destroy Seed> ✓
>
> _Achtung_: Ihre Coldcard wird den privaten Schlüssel nach diesen Schritten vergessen. Stellen Sie sicher, dass Sie Ihre mnemonische Phrase gut gesichert haben, wenn Sie sie später wiederherstellen möchten.

## Schritte zum Folgen:

Verbindung zur Coldcard mit PIN > Neue Seed-Wörter > 24-Wort-Würfelwurf

Führen Sie 100 Würfelwürfe durch und notieren Sie das Ergebnis von 1 bis 6 auf der Coldcard nach jedem Wurf. Durch diese Methode erzeugen Sie 256 Bytes Entropie, was die Erzeugung eines vollständig zufälligen privaten Schlüssels ermöglicht. Coinkite stellt auch die erforderliche Dokumentation zur unabhängigen Überprüfung ihres Entropieerzeugungssystems zur Verfügung.

![Screenshot Visuel Cold Card](assets/guide-agora/1.webp)

Nach Abschluss der 100 Würfelwürfe drücken Sie ✓ und notieren die erhaltenen 24 Wörter in der richtigen Reihenfolge. Überprüfen Sie zweimal und drücken Sie ✓. Schließlich müssen Sie nur noch den 24-Wort-Überprüfungstest auf der Coldcard abschließen, und voilà, Ihr neuer privater Schlüssel ist erstellt!

Wählen Sie dann, ob Sie die NFC- (Mk4) und USB-Funktionen aktivieren möchten oder nicht, und folgen Sie den angezeigten Schritten. Sobald Sie sich im Hauptmenü befinden, ist es nun an der Zeit, die Firmware des Geräts zu aktualisieren. Gehen Sie zu Erweitert/Werkzeuge > Firmware aktualisieren > Version anzeigen und überprüfen Sie die offizielle Website, um die neueste verfügbare Version zu validieren und herunterzuladen. Es wird empfohlen, die Coldcard zu aktualisieren, um maximalen Schutz zu gewährleisten.

Bevor Sie fortfahren, wird empfohlen, den Master Key Fingerprint (XFP) mit dem privaten Schlüssel zu notieren. Diese Daten ermöglichen es Ihnen, schnell zu überprüfen, ob Sie sich im richtigen Wallet befinden, zum Beispiel bei einer Wiederherstellung. Gehen Sie zu Erweitert/Werkzeuge > Identität anzeigen > Master Key Fingerprint (XFP) und notieren Sie die erhaltenen acht alphanumerischen Zeichen. Der XFP kann an derselben Stelle wie die mnemonische Phrase notiert werden, es handelt sich nicht um sensible Daten.

> 💡 Es wird empfohlen, Ihre mnemonische Phrase in einer anderen Software zu überprüfen. Um dies sicher zu tun, lesen Sie unseren Artikel "Überprüfen Sie die Sicherung einer Bitcoin-Brieftasche mit Tails in weniger als 5 Minuten".

## Sicherheitsbonus: das "Geheime Passwort" (optional)

Eine geheime Passphrase ist ein großartiges Element, das zu einer Wallet-Konfiguration hinzugefügt werden kann, um eine zusätzliche Sicherheitsebene zum Schutz von Bitcoins hinzuzufügen. Die geheime Passphrase fungiert sozusagen als das 25. Wort der Mnemonik-Phrase. Sobald eine hinzugefügt wird, wird eine vollständig neue Wallet erstellt, zusammen mit einem privaten Schlüssel und der dazugehörigen Mnemonik-Phrase. Es ist nicht erforderlich, die neue Mnemonik-Phrase zu notieren, da auf diese Wallet zugegriffen werden kann, indem die ursprüngliche Mnemonik-Phrase mit der gewählten geheimen Passphrase kombiniert wird.

Das Ziel besteht darin, die geheime Passphrase separat von der Mnemonik-Phrase zu notieren, da ein Angreifer, der Zugriff auf beide Elemente hat, Zugriff auf die darin enthaltenen Mittel hat. Im Gegensatz dazu hat ein Angreifer, der nur auf eines dieser beiden Elemente zugreifen kann, keinen Zugriff auf die Mittel, und genau dieser Vorteil optimiert das Sicherheitsniveau der Wallet-Konfiguration.

![Hinzufügen einer geheimen Passphrase führt zu einer völlig anderen Wallet](assets/guide-agora/2.webp)

## Schritte zum Hinzufügen einer geheimen Passphrase mit der Coldcard:

Passphrase > Wörter hinzufügen (empfohlen) > Anwenden. Das Gerät zeigt die XFP der neu generierten Wallet durch die geheime Passphrase an, die aus den oben genannten Gründen zusammen mit der geheimen Passphrase notiert werden sollte.

> 💡 Zusätzliche Ressourcen zur geheimen Passphrase:

    https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af
    https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/
    https://armantheparman.com/passphrase/

## Exportieren der Wallet in Bitcoin Core

Die Wallet ist nun bereit, auf einer Software exportiert zu werden, um mit dem Bitcoin-Netzwerk zu interagieren. In diesem Leitfaden verwenden wir Bitcoin Core (v24.1).

Beziehen Sie sich auf unsere Installations- und Konfigurationsanleitungen für Bitcoin Core:

> Führen Sie Ihren eigenen Bitcoin Core-Knoten aus - https://agora256.com/faire-tourner-son-propre-noeud-avec-bitcoin-core/
>
> Konfiguration von Tor für einen Bitcoin Core-Knoten - https://agora256.com/configuration-tor-bitcoin-core/

Legen Sie zuerst eine microSD-Karte in die Coldcard ein und exportieren Sie die Wallet für Bitcoin Core, indem Sie diesen Schritten folgen: Advanced/Tools > Wallet exportieren > Bitcoin Core. Zwei Dateien werden auf der microSD-Karte gespeichert: bitcoin-core.sig & bitcoin-core.txt. Legen Sie die microSD-Karte in den Computer ein, auf dem Bitcoin Core installiert ist, und öffnen Sie die .txt-Datei. Sie sehen die Zeile Für Wallet mit Fingerabdruck des Master-Schlüssels. Überprüfen Sie, ob der achstellige XFP mit dem übereinstimmt, den Sie beim Erstellen Ihres privaten Schlüssels notiert haben.
Bevor wir den Anweisungen in der Datei folgen, bereiten wir das Wallet in der Bitcoin Core-Schnittstelle vor, indem wir die folgenden Schritte ausführen: Gehen Sie zum Tab "Datei" > "Wallet erstellen". Wählen Sie einen Namen für Ihr Wallet (ein austauschbarer Begriff für Wallet in Core) und aktivieren Sie die Optionen "Private Keys deaktivieren", "Leeres Wallet erstellen" und "Wallet mit Descriptoren", wie im untenstehenden Bild gezeigt. Drücken Sie dann auf die Schaltfläche "Erstellen".

![Wallet erstellen](assets/guide-agora/3.webp)

Nachdem das Wallet in Bitcoin Core erstellt wurde, gehen Sie zum Tab "Fenster" > "Konsole" und stellen Sie sicher, dass das ausgewählte Wallet oben auf der Seite den Namen des von Ihnen erstellten Wallets anzeigt.

Nun kopieren Sie in die Bitcoin Core-Konsole die Zeile aus der zuvor von der Coldcard generierten .txt-Datei, die mit "importdescriptors" beginnt. Eine Antwort mit der Zeile "success": true sollte zurückgegeben werden.

![Knotenfenster](assets/guide-agora/4.webp)

Wenn die Antwort "message": "Ranged descriptors should not have a label" enthält, löschen Sie den Eintrag "label": "Coldcard xxxx0000" in der kopierten Zeile aus der .txt-Datei und fügen Sie dann die vollständige Zeile erneut in die Bitcoin Core-Konsole ein.

Hilfe: [https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md](https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md)

## Überprüfung des Wallet-Imports in Bitcoin Core

Um sicherzustellen, dass der Import erfolgreich war, müssen Sie überprüfen, ob das gewünschte Wallet tatsächlich in Bitcoin Core importiert wurde. Eine einfache Methode, dies zu bestätigen, besteht darin, zu überprüfen, ob die in der Coldcard generierten Adressen mit den in Bitcoin Core generierten Adressen übereinstimmen.

Bitcoin Core: "Empfangen" > "Neue Empfangsadresse erstellen"
Coldcard: "Address Explorer" > Wählen Sie die Adresse, die mit "bc1q" beginnt. Die Coldcard-Adresse "bc1q" sollte mit der in Bitcoin Core angezeigten Adresse übereinstimmen.
Empfangen und Senden von Transaktionen im "air-gapped"-Modus

Das Empfangen einer Transaktion ist äußerst einfach: Drücken Sie auf "Empfangen", geben Sie der Transaktion eine Bezeichnung (optional, aber empfohlen) und erstellen Sie eine neue Empfangsadresse. Dann müssen Sie die Adresse nur noch dem Absender mitteilen.

Der Schlüsselaspekt dieser Coldcard + Bitcoin Core-Konfiguration besteht darin, Transaktionen zu senden, ohne dass die Coldcard und ihr privater Schlüssel mit dem Internet verbunden sind. Dies erfolgt über eine Methode namens "air-gapped", die die TBSP-Funktion (PSBT - Partially Signed Bitcoin Transactions) von Bitcoin verwendet.
Grundsätzlich verwenden wir die Bitcoin Core-Schnittstelle, um eine Transaktion zu erstellen, die wir dann über die Micro-SD-Karte auf die Coldcard exportieren, um sie zu signieren. Anschließend übertragen wir die signierte Transaktionsdatei zurück auf Bitcoin Core und verbreiten die Transaktion im Netzwerk. Wir müssen dies tun, da der auf Bitcoin Core importierte Geldbeutel keine privaten Schlüssel enthält, sondern nur den öffentlichen Schlüssel (mit dem wir unsere Empfangsadressen generieren können). Daher ist es uns unmöglich, eine Transaktion direkt in der Software zu signieren, um unsere Bitcoins auszugeben.

Bevor Sie fortfahren, stellen Sie sicher, dass die folgenden Optionen in den Einstellungen > Geldbörse aktiviert sind:

> - Münzkontrollfunktionen aktivieren
> - Nicht bestätigte Münzen ausgeben (optional)
> - TBPS-Überprüfungen aktivieren

![Option](assets/guide-agora/5.webp)

### Schritte zum Senden im air-gapped-Modus:

Senden > Eingänge > gewünschte UTXO auswählen, dann die Empfängeradresse in "An" eingeben. Transaktionsgebühr: Auswählen... > Benutzerdefiniert > Transaktionsgebühr eingeben (Bitcoin Core berechnet in sats/kilobyte anstelle von sat/byte wie die meisten alternativen Geldbörsenlösungen. Daher entspricht 4000 sats/kilobyte 4 sats/byte). Nicht signierte Transaktion erstellen > Datei auf Ihrer Micro-SD-Karte speichern und diese in die Coldcard einlegen.

Auf der Coldcard auf "Bereit zum Signieren" drücken, die Transaktionsdetails überprüfen und dann auf ✓ drücken. Nachdem die signierten Dateien generiert wurden, legen Sie die Micro-SD-Karte wieder in den Computer ein.

Gehen Sie zurück zu Bitcoin Core, wählen Sie die Registerkarte "Datei" > "TBSP aus Datei laden" und geben Sie die signierte Transaktionsdatei .psbt ein. Das PSBT-Operationsfeld wird angezeigt und bestätigt, dass die Transaktion vollständig signiert und bereit zur Verbreitung ist. Drücken Sie einfach auf "Transaktion verbreiten".

![PSBT-Operationen](assets/guide-agora/6.webp)

### Fazit

Die Kombination aus der Coldcard und Bitcoin Core, auf dem Sie Ihren eigenen Knoten betreiben, ist leistungsstark. Fügen Sie dazu einen privaten Schlüssel hinzu, der mit 100 Würfen generiert wurde, sowie einen geheimen Satz, und Ihre Geldbörsenkonfiguration wird zu einer anspruchsvollen und robusten Festung.

Zögern Sie nicht, uns zu kontaktieren, um uns Ihre Kommentare und Fragen mitzuteilen! Unser Ziel ist es, unser Wissen zu teilen und jeden Tag dazuzulernen.
