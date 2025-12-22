---
name: Cake Wallet
description: Tutorial über Cake Wallet und Stille Zahlungen
---

![cover](assets/cover.webp)


Dieser Leitfaden befasst sich mit [**Cake Wallet**](https://cakewallet.com/): ein quelloffenes, nicht-kustodiales, datenschutzorientiertes wallet mit mehreren Währungen, das für Android, iOS, macOS, Linux und Windows verfügbar ist. Wir werden in die Bitcoin-spezifischen Datenschutzfunktionen eintauchen, das Senden/Empfangen von Bitcoin über **Silent Payments** (ein verbessertes on-chain-Datenschutzprotokoll) durchgehen und einen Blick auf die Implementierung von PayJoin v2 für asynchrone Transaktionen werfen.


## 🎉 Hauptmerkmale



- [**Silent Payments (BIP-352)**](https://bips.dev/352/) verbessert die bisherigen [BIP 47 Zahlungscodes](https://silentpayments.xyz/docs/comparing-proposals/bip47/), auch "PayNyms" genannt, mit wiederverwendbaren Tarnadressen. Wenn ein Absender Ihre Silent-Payment-Adresse verwendet, leitet sein wallet eine einmalige Adresse mit verschiedenen Schlüsseln ab, die zu einer einmaligen Taproot-Adresse kombiniert werden. Die Blockchain-Aufzeichnungen zeigen nicht zusammenhängende Transaktionen, was eine Verknüpfung eingehender Zahlungen verhindert. Silent Payments bieten eine Reihe von Vorteilen, darunter:
    - Wiederverwendbare Adressen: Es ist nicht erforderlich, für jede Transaktion eine neue generate-Adresse zu verwenden, was die Benutzerfreundlichkeit erhöht und den Datenschutz verbessert
    - Kein Kostenanstieg: Silent Payments erhöhen weder den Umfang noch die Kosten der Transaktionen.
    - Erhöhte Anonymität: Außenstehende Beobachter können Transaktionen nicht mit einer Silent-Payment-Adresse in Verbindung bringen.
    - Keine Sender-Empfänger-Interaktion erforderlich: Transaktionen können ohne jegliche Kommunikation zwischen den Parteien durchgeführt werden.
    - Eindeutige Adressen für jede Zahlung: Das Risiko der versehentlichen Wiederverwendung von Adressen wird eliminiert.
    - Kein Server erforderlich: Silent Payments können ohne einen eigenen Server durchgeführt werden.
- PayJoin v2** entschärft die Analyse von Transaktionsgraphen, indem es die Eingaben von Sendern und Empfängern zu einer einzigen Transaktion zusammenfasst. Cake Wallet implementiert zwei entscheidende Fortschritte:
    - Asynchrone Transaktionen**: Sender und Empfänger müssen nicht mehr gleichzeitig online sein, um eine private Transaktion abzuschließen.
    - Serverlose Kommunikation**: Keine der beiden Parteien muss einen Payjoin-Server betreiben, was eine große technische Hürde darstellt.
- Die Coin-Kontrolle** ermöglicht die manuelle UTXO-Auswahl bei Transaktionen. Dies verhindert eine versehentliche Verknüpfung von Adressen, wenn mehrere UTXOs mit unterschiedlicher Herkunft ausgegeben werden.
- TOR**-Unterstützung, die es Nutzern ermöglicht, ihren Netzwerkverkehr durch das Tor-Netzwerk zu leiten
- Mit RBF** (Replace-By.Fee) können Sie die Gebühr nach dem Senden einer Transaktion anpassen.


## 1️⃣ Aufstellen des Wallet


Cake Wallet bietet eine breite Palette an Plattformunterstützung. Sie können zwischen `Android`, `iOS / macOS`, `Linux` und `Windows` wählen.  Um zu beginnen, besuchen Sie https://docs.cakewallet.com/get-started/ und wählen Sie Ihr Betriebssystem.


![image](assets/en/01.webp)


Nach der Installation legen Sie eine PIN fest (4- oder 6-stellig). Sie werden dann sehen:


1. neues Wallet erstellen" (für neue Benutzer)

2. gW-19 wiederherstellen" (für bestehende Geldbörsen)


![image](assets/en/02.webp)


Auf dem nächsten Bildschirm können Sie aus einer breiten Palette von Kryptowährungen wählen. Wählen Sie "Bitcoin" und tippen Sie auf "Weiter" und geben Sie einen "Wallet-Namen" ein, um den wallet zu identifizieren. Wenn Sie auf "Erweiterte Einstellungen" tippen, erscheint eine Reihe von "Datenschutzeinstellungen". Nehmen Sie diese Änderungen vor:



- Fiat API:** wähle "Nur Tor" (leitet Preisanfragen durch Tor)
- Swap:** Wählen Sie "Nur Tor" (anonymisiert den Austauschverkehr)


Standardmäßig wird der Typ BIP-39 seed erzeugt, mit der Option, zu Electrum seed zu wechseln. Die Ableitungspfade sind die folgenden:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Wenn Sie eine zusätzliche Sicherheitsebene einrichten wollen, können Sie einen "passphrase" einrichten.  Der Hauptzweck eines passphrase besteht darin, zusätzlichen Schutz gegen physische Angriffe zu bieten. Selbst wenn ein Angreifer den seed-Satz findet, kann er ohne den richtigen passphrase nicht auf Ihren wallet zugreifen. Mit anderen Worten, der seed-Satz allein stellt einen wallet dar, während der seed-Satz plus passphrase einen völlig anderen wallet ohne Verbindung zum Original erzeugt. Diese Funktion ermöglicht auch "geheime Geldbörsen", die durch den passphrase geschützt sind, und gibt Ihnen eine plausible Bestreitbarkeit. In einer Zwangssituation könnten Sie den seed-Satz preisgeben, während größere Vermögenswerte im passphrase-geschützten wallet sicher aufbewahrt werden.


Wenn Sie bereits Ihren eigenen Knoten betreiben, klicken Sie auf "Add New Custom Node" und geben Sie Ihren "Node Address" an, um Transaktionen und Blöcke innerhalb Ihrer eigenen Infrastruktur zu validieren. Sobald Sie fertig sind, tippen Sie auf "Continue" und "Next", um Ihren wallet zu erstellen.


![image](assets/en/03.webp)


Auf dem nächsten Bildschirm erhalten Sie einen Haftungsausschluss:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Um zu erfahren, wie Sie Ihre Eselsbrücke am besten speichern, lesen Sie bitte diesen Leitfaden:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Tippen Sie auf "Ich verstehe. Zeigen Sie mir mein seed" und speichern Sie diese Worte an einem sicheren Ort! Tippen Sie dann auf "seed überprüfen" und nach der Überprüfung auf "Wallet öffnen".


## 2️⃣ Einstellungen


Bevor wir tiefer eintauchen, werfen wir einen Blick auf den "Startbildschirm" und die "Einstellungen".


Auf dem Startbildschirm werden verschiedene Elemente angezeigt:



- das "Hamburger-Menü" bringt uns zu den "Einstellungen"
- Verfügbarer Saldo
- Silent-Payments-Karte, um mit dem Scannen nach Transaktionen zu beginnen, die an Ihre Silent-Payment-Adresse gesendet werden
- Payjoin-Karte zum "Freischalten" von Payjoin als datenschutzfreundliches und gebührenschonendes Feature
- unten befinden sich Verknüpfungen zu "Wallet Übersicht", "Empfangen", "Tauschen" zwischen Bitcoin und anderen Währungen, "Senden" und "Kaufen"


![image](assets/en/11.webp)


Durch Tippen auf das Symbol "Hamburger-Menü" wird das Einstellungsmenü geöffnet. Schauen wir uns die Optionen an.


![image](assets/en/05.webp)


### A - Verbindung und Synchronisation 🔗


Hier können wir den wallet wieder anschließen, Knoten verwalten und eine Verbindung zu unserem eigenen Knoten herstellen (empfohlen). Mit dem "Silent Payments Scanning" können wir das Scannen anpassen, indem wir entweder "Scannen nach Blockhöhe" oder "Scannen nach Datum" angeben.


![image](assets/en/06.webp)


Als "Alpha"-Funktion gibt es auch die Möglichkeit, "eingebautes Tor" zu aktivieren, um den Datenverkehr durch das Tor-Netzwerk zu leiten.


### B - Einstellungen für stille Zahlungen 🔈


Wir können die Karte "Stille Zahlungen" auf dem Startbildschirm einschalten, um diese Funktion anzuzeigen. Wenn Sie "Immer scannen" aktivieren, kann die wallet die Blockchain kontinuierlich auf eingehende stille Zahlungen überwachen. Wir können Scan-Parameter festlegen, um den Scan-Prozess an unsere Bedürfnisse anzupassen, wie oben beschrieben.


![image](assets/en/07.webp)


### C - Sicherheit & Backup 🗝️


Um unser wallet zu sichern, können wir eine Sicherungskopie erstellen, indem wir den Anweisungen in der App folgen. Dadurch wird sichergestellt, dass wir eine sichere Kopie unserer privaten Schlüssel haben, so dass wir unser wallet wiederfinden können, wenn es verloren geht oder gestohlen wird. Außerdem können wir unsere seed-Phrase und unsere privaten Schlüssel anzeigen, unsere PIN ändern, die biometrische Authentifizierung aktivieren, Sign / Verify und 2FA für eine zusätzliche Schutzebene einrichten.


![image](assets/en/08.webp)


**Anmerkung**: Ab September 2025 muss die biometrische Authentifizierung per Fingerabdruck auf Android-Geräten mindestens mit einer biometrischen Implementierung der Klasse 2 funktionieren; weitere Einzelheiten finden Sie [hier](https://source.android.com/docs/security/features/biometric/measure#biometric-classes). Diese Anforderung kann sich jedoch in Zukunft ändern.


### D - Datenschutzeinstellungen 🔒


Wir können auch die Sicherheit unseres wallet erhöhen, indem wir Tor verwenden, um unsere Internetverbindung zu verschlüsseln und unsere Privatsphäre zu schützen, wenn wir auf externe Quellen zugreifen. Außerdem können wir Screenshots verhindern, um unsere wallet-Informationen vertraulich zu halten, automatisch generierte Adressen aktivieren, um neue Adressen für jede Transaktion zu erstellen, und Kauf-/Verkaufsaktionen deaktivieren, um nicht autorisierte Transaktionen zu verhindern. Außerdem können wir "PayJoin aktivieren", eine weitere Datenschutzfunktion, die wir später noch genauer betrachten werden.


![image](assets/en/09.webp)


### E - Sonstige Einstellungen 🔧


Andere Einstellungen ermöglichen es uns, die Gebührenpriorität zu verwalten und die Standardgebührenhöhe für unsere Transaktionen festzulegen. Auf diese Weise können wir die mit unseren Stillen Zahlungen verbundenen Transaktionsgebühren unter Berücksichtigung der aktuellen Netzauslastung steuern.


![image](assets/en/10.webp)


## 3️⃣ ₿itcoin-Empfang mit stillen Zahlungen


Für den Empfang von Bitcoin stehen mehrere Optionen und Adresstypen zur Verfügung. segwit (P2WPKH)" *(beginnend mit bc1q....)* ist die Standardoption.  In diesem Beispiel wählen wir "Stille Zahlungen".


Um eine Stille Zahlung zu erhalten, tippen Sie zunächst auf das Symbol "Empfangen" in Cake Wallet. Geben Sie dann den Betrag ein, den Sie erwarten zu erhalten. Um den Adresstyp festzulegen, tippen Sie erneut auf "Empfangen" am oberen Bildschirmrand und wählen Sie dann "Stille Zahlungen" aus den Optionen.


Auf dem Hauptbildschirm werden Ihr wiederverwendbarer Silent Payment QR-Code und Ihre Adresse angezeigt. Wie erwartet, ist die Adresse recht lang:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Verwenden Sie nun ein BIP-352-kompatibles wallet (z. B. Blue Wallet), um diesen QR-Code zu scannen und die Zahlung zu senden. Sie werden sehen, dass das wallet eine eindeutige Zieladresse aus Ihrer stummen Adresse ableitet.


![image](assets/en/13.webp)


## 4️⃣ Senden von ₿itcoin mit Silent Payments


Da der Blue Wallet nur "stille Zahlungen" senden kann, verwenden wir einen anderen BIP 352 kompatiblen wallet als Empfänger. Dieser Vorgang ist identisch mit dem einer regulären Bitcoin-Transaktion.



- Tippen Sie auf "Senden" auf dem Startbildschirm
- entweder durch Einfügen unserer wiederverwendbaren `sp1qq...`-Adresse oder durch Scannen des QR-Codes direkt in der App.
- Wählen Sie, wie viel Sie von Ihrem verfügbaren Guthaben ausgeben möchten
- Tippen Sie auf "Senden" am unteren Rand des Bildschirms, um die Transaktion zu bestätigen


Sobald wir die Adresse "sp1qq..." eingegeben haben, leitet der wallet im Hintergrund automatisch eine entsprechende "bc1p..."-Adresse des Taproot (P2TR) ab, die für die stille Zahlung verwendet wird.


Wir können optional eine interne Notiz für jede Transaktion schreiben, die Gebühreneinstellungen anpassen oder bestimmte UTXOs für die Transaktion mit der Funktion `Coin Control` auswählen.


![image](assets/en/14.webp)


wischen" Sie nach rechts, um die Transaktion zu bestätigen.


Sobald Sie die Transaktion abgeschickt haben, werden Sie gefragt, ob Sie diesen Kontakt zu Ihrem Adressbuch hinzufügen möchten.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


Schauen wir uns an, worum es bei PayJoin geht (https://docs.cakewallet.com/cryptos/bitcoin/#payjoin):


payjoin v2 ist eine datenschutzfreundliche und gebührenschonende Funktion in Bitcoin, die es dem Sender und dem Empfänger einer Transaktion ermöglicht, zusammenzuarbeiten, um eine einzige Transaktion zu erstellen. Diese Transaktion hat Eingaben von *beiden* Absendern und Empfängern, was die gängigsten Überwachungstechniken gegen Bitcoin bricht und unter bestimmten Umständen auch eine bessere Skalierung und Gebühreneinsparungen ermöglicht._


Um mehr über PayJoin zu erfahren, können Sie auch den folgenden Lehrgang besuchen.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

Um PayJoin zu verwenden, benötigen beide Parteien ein PayJoin-kompatibles wallet, und der Empfänger muss mindestens eine Münze oder einen Ausgang in seinem wallet haben. Um zu beginnen, folgen Sie bitte diesen Schritten:


1. Tippen Sie auf das "Hamburger-Menü" und dann auf die Schaltfläche "Datenschutz"

2. Schalten Sie die Option "Payjoin verwenden" ein

3.  Tippen Sie auf der Startseite auf "Empfangen", und Sie erhalten einen PayJoin-QR-Code und eine Kopierschaltfläche (bei Auswahl von Segwit)


![image](assets/en/16.webp)


## 6️⃣ Sonstige Merkmale


Es gibt verschiedene andere Funktionen wie "Swaps" in mehreren Währungen, "Kauf- und Verkaufsoptionen" mit Verbindungen zu verschiedenen Anbietern und Cake-spezifische Programme wie "Cake Pay", mit dem Sie Prepaid-Karten oder Geschenkkarten kaufen können.


![image](assets/en/17.webp)


## 🎯 Schlussfolgerung


Dies ist unser Test des Cake Wallet, der dank Funktionen wie Silent Payments (BIP-352) und Payjoin v2 einen praktischen Bitcoin Datenschutz bietet.


Stille Zahlungen ersetzen Einwegadressen durch wiederverwendbare Tarnadressen, um die on-chain-Verknüpfung eingehender Transaktionen zu verhindern. Obwohl sich die Synchronisierungsprobleme früherer Versionen deutlich verbessert haben, sind die Rechenanforderungen für die Überprüfung und Erkennung von Silent Payments gestiegen, was mehr Ressourcen und Bandbreite erfordert.


Payjoin v2 unterbricht die Kettenanalyse, indem es die Eingaben von Sender und Empfänger zu einer einzigen Transaktion zusammenfasst, ohne zusätzliche Gebühren oder zentrale Koordination. Dies bricht die übliche Heuristik der Input-Eigentümerschaft auf, was ein großer Vorteil ist, da man nicht davon ausgehen kann, dass alle Inputs dem Sender gehören.


Für Nutzer, die Wert auf finanzielle Anonymität legen, ist der Cake Wallet eine praktikable Option. Es integriert Datenschutzprotokolle direkt in seine Kernfunktionalität und macht sie ohne technische Komplexität zugänglich. Da die Überwachung auf öffentlichen Blockchains zunimmt, helfen Tools wie dieses dabei, die Privatsphäre bei Transaktionen dort zu wahren, wo sie am wichtigsten ist. Eine breitere Implementierung dieser Standards innerhalb der wallet-Landschaft wäre eine willkommene Entwicklung.


## 📚 Ressourcen


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/