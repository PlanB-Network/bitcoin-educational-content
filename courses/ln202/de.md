---
name: Einrichtung eines Bitcoin & Lightning Knotens
goal: Einrichten eines Bitcoin- und Lightning-Knotens über Umbrel
objectives:
  - Installation eines Bitcoin-Knotens
  - Verwaltung eines Bitcoin-Knotens
  - Verwendung eines Lightning-Netzwerksknotens
---

# Eine Reise in die technische Seite von Bitcoin

Dieses Training ist technischer und wird umso vorteilhafter sein, wenn Sie Grundkenntnisse über Bitcoin haben, insbesondere das Verständnis von Bitcoin-Wallets und dem Prinzip von Transaktionen, Mining und Blockchain. Sie müssen nicht programmieren können, Ihre Neugierde und Lernbereitschaft sind die einzigen erforderlichen Fähigkeiten. Denken Sie daran, jeder Experte war einmal ein Anfänger. Also atmen Sie tief durch und tauchen Sie ein in die aufregende Welt von Bitcoin. Sie stehen kurz vor einer aufregenden und bereichernden Reise. Viel Glück!

+++

# Ein souveräner Bitcoiner werden

![Start des Trainings](https://youtu.be/NF3SHhE1PFw?list=PLinTFKehfR4zoKvBcncHPr-ZTh1enuEhr)

Um vollständig an der Philosophie von Bitcoin teilzunehmen und das Motto "Don't Trust, Verify" zu verkörpern, streben wir danach, souveräne Benutzer von Bitcoin-Knoten zu werden. In diesem Prozess werden wir uns auf die Umbrel-Schnittstelle stützen, um unseren eigenen Knoten einzurichten. Die für diese Aufgabe erforderlichen Werkzeuge umfassen einen Raspberry Pi, eine externe Festplatte, eine SD-Karte, einen Lüfter und eine Box, für eine geschätzte Gesamtinvestition von etwa 200 €.

Indem wir Umbrel als unsere Betriebsbasis übernehmen, werden wir in der Lage sein, das Lightning-Netzwerk zu integrieren, den Mempool zu erkunden und Multisig-Lösungen zu entdecken. Am Ende dieser Reise werden wir uns nicht nur als souveräne Bitcoiner etabliert haben, sondern auch die Zufriedenheit haben, aktiv zum Bitcoin-Netzwerk beigetragen zu haben.

# Was ist ein Bitcoin-Knoten?

![Was ist ein Knoten?](https://youtu.be/19YgL9vkHh4)

Ein Bitcoin-Knoten ist einfach ein Gerät, auf dem die Bitcoin-Software läuft, der Eckpfeiler des Netzwerks für Existenz und Kommunikation. Diese Knoten bilden das Fundament der Dezentralisierung von Bitcoin, indem sie verschiedene Formen annehmen und verschiedene Verantwortlichkeiten übernehmen. Dazu gehören der Empfang und die Übertragung von Transaktionen, die Anzeige ausgehender Transaktionen und die Herstellung von Verbindungen zu anderen Knoten.
Drei Hauptrollen sind diesen Knoten zugewiesen: die Etablierung des Bitcoin-Konsenses, die Validierung von Transaktionen und die Interaktion mit dem Netzwerk. Dank dieser Dezentralisierung profitiert Bitcoin von einer erhöhten Widerstandsfähigkeit, mit einer durch die Tatsache, nicht von einem Drittanbieter-Server abhängig zu sein, gestärkten Privatsphäre. Laut [Bitnodes](https://bitnodes.io/nodes/all/) bilden etwa 43.000 Knoten weltweit das Bitcoin-Netzwerk.

Lassen Sie uns nun die spezifischen Funktionen dieser Knoten im Bitcoin-Netzwerk erkunden. Ein Knoten ist nicht nur eine Software; er ist auch ein Gateway zum Konsens des Bitcoin-Netzwerks und zum Zugang zur Blockchain-Historie. Zum Beispiel nutzen Händler ihren eigenen Knoten, um eingehende und ausgehende Transaktionen zu validieren.

Der Vorteil, einen eigenen Knoten zu betreiben, liegt in der Verbesserung der Privatsphäre und der Erreichung finanzieller Souveränität. Tatsächlich stärkt das Ausführen eines eigenen Knotens Ihren Beitrag zum Netzwerk und macht Sie zu Ihrer eigenen Bank. Dies ermöglicht es Ihnen, Transaktionen in Echtzeit zu überprüfen und bietet Ihnen eine bessere Entscheidungsgrundlage für Ihre Finanzen.

Zusammenfassend bietet das Betreiben eines eigenen Knotens im Bitcoin-Netzwerk viele Vorteile. Es trägt nicht nur zur Dezentralisierung des Netzwerks bei und stärkt damit die Widerstandsfähigkeit des Systems, sondern gewährleistet auch eine größere Vertraulichkeit und finanzielle Autonomie. Durch die Durchführung dieses Schrittes können Sie Transaktionen in Echtzeit authentifizieren, fundierte finanzielle Entscheidungen treffen und die Abhängigkeit von einem Drittanbieter-Server vermeiden, um Ihre Privatsphäre zu gewährleisten. Darüber hinaus ist das Ausführen eines eigenen Knotens ein konkreter Beitrag zum Bitcoin-Ökosystem und verkörpert wirklich die Rolle Ihrer eigenen Bank.

# Bitcoin-Knoten-Tutorial über Umbrel

![Umbrel-Tutorial](https://youtu.be/mr4iTzdTczI)

In diesem Kapitel werden wir einen Bitcoin-Knoten selbst bereitstellen, Lightning-Kanäle öffnen und einen Multi-Signatur-Wallet ausprobieren. Dies hat für einige Personen einen erheblichen materiellen Aufwand. Beachten Sie jedoch, dass die gesamte Schulung OHNE Hardware durchgeführt werden kann. Sie werden nicht verloren sein, wenn Sie keinen eigenen Knoten haben.
Wenn Sie bereit sind, hier sind die Produkte (Affiliate-Link):

- 16GB SD-Karte - https://amzn.to/3Qi2Opm
- Raspberry Pi 4 - https://amzn.to/3qoSUYl
- 1TB SSD - https://amzn.to/3jSvjLC
- Externes Gehäuse für Festplatte - https://amzn.to/3x5R02S
- RASPBERRY Stromversorgung - https://amzn.to/3D36zvM
- Raspberry Pi FLIRC-Gehäuse - https://amzn.to/3TNllgi
  Wenn Sie über Affiliate-Links gekommen sind, vielen Dank für Ihre Unterstützung! Sie ermöglichen es diesem Projekt, zu überleben und immer mehr Schulungen und Bildungsinhalte anzubieten.

Was braucht man, um seinen Bitcoin-Knoten zu betreiben?

- Die Blockchain ist etwa 500 GB groß, daher sollte Platz eingeplant werden.
- Die Internetverbindung muss konstant sein und etwa 5 GB Bandbreite pro Monat haben.
- Es wird RAM benötigt, um BTC Core auszuführen.
- Wenn man Umbrel und einen LN-Knoten ausführt, wird mehr RAM benötigt (mindestens 4 GB).

Sie können Ihren Bitcoin-Knoten direkt auf Ihrem Computer ausführen oder ein System wie in dem Video mit einem Raspberry Pi verwenden.

Es gibt bereits andere [fertige Lösungen](https://thebitcoinmanual.com/behind-btc/nodes/buy-node/)!

Folgen Sie diesen Schritten, um einen Full Node mit einem Raspberry Pi und Umbrel zu erstellen. Beachten Sie, dass Sie etwa 200 Euro für das benötigte Material benötigen, obwohl die Software kostenlos ist.

1. **Vorbereitung der Werkzeuge**: Gehen Sie zu [Umbrel](https://umbrel.com/), einer Open-Source-Lösung, die für ihre ausgezeichnete Benutzeroberfläche und ihren guten Service bekannt ist, um die benötigte Software herunterzuladen. Außerdem benötigen Sie Benella Itcher, um die SD-Karte zu flashen.
2. **Montage des Raspberry Pi**: Bauen Sie Ihren Raspberry Pi zusammen. Stellen Sie sicher, dass Sie den Lüfter und die kleinen Kühlkomponenten im Kit installieren.
3. **Flashen der SD-Karte**: Verwenden Sie das im Kit enthaltene Gerät, um die SD-Karte zu flashen. Wenn Sie Schwierigkeiten haben, versuchen Sie, die Karte neu zu formatieren oder das Gerät aus- und wieder einzustecken.
4. **Anschließen der Hardware**: Sobald die SD-Karte geflasht ist, schließen Sie die SSD über einen 3.0-Port an den Raspberry Pi an. Schließen Sie dann den Raspberry Pi an Ihren Router und eine Stromquelle an.
5. **Konfiguration von Umbrel**: Nach etwa 5 Minuten können Sie auf die Umbrel-Oberfläche auf Ihrem Computer zugreifen. Es wird empfohlen, einen Passwort-Manager zu verwenden, um ein sicheres Passwort für den Zugriff auf Ihren Umbrel-Knoten zu erstellen und zu speichern.
6. **Sicherung Ihrer Seed-Phrase**: Ihre Seed-Phrase ist der private Schlüssel, der Ihnen Zugang zu Ihren Bitcoins gibt. Bewahren Sie sie also sicher auf. Vermeiden Sie es, Fotos oder Screenshots Ihrer Seed-Phrase zu machen. Es wird auch empfohlen, den TOR-Link in Ihrem Passwort-Manager für einen späteren einfachen Zugriff zu speichern.
7. **Erkunden des Umbrel-Dashboards**: Umbrel verfügt über ein klares Dashboard und einen innovativen App Store zum Herunterladen weiterer Anwendungen. Das Umbrel-Tutorial ist für alle zugänglich, Sie müssen nur das Material kaufen und den Schritten folgen.
8. **Bewusstsein für die Bedeutung von Knotenpunkten**: Knotenpunkte sind entscheidend, um das Bankensystem zu transformieren und Zentralbanken zu ersetzen. Mit Ihrem eigenen Knotenpunkt tragen Sie zur Überprüfung von Bitcoin-Transaktionen und zur Einhaltung der Protokollregeln bei. Durch das Betreiben Ihres eigenen Knotenpunkts müssen Sie keinem Dritten mehr vertrauen und können Transaktionen selbst überprüfen. Knotenpunkte sind ein wesentlicher Pfeiler Ihrer finanziellen Souveränität.

Durch das Befolgen dieser Schritte können Sie zur Dezentralisierung des Bitcoin-Netzwerks beitragen, Ihre finanzielle Privatsphäre und Autonomie erhöhen und aktiv an der Entwicklung des traditionellen Bankensystems teilnehmen. Zögern Sie also nicht, sich zu engagieren und ein echter souveräner Bitcoiner zu werden.

# Überblick über Umbrel

![Umbrel-Überblick](https://youtu.be/cwEa61BgemM)

Wir werden uns nun ausführlich mit dieser Benutzeroberfläche befassen, die die Verwaltung Ihrer Bitcoin- und Lightning-Netzwerk-Wallet erleichtert.

Zunächst werden wir uns mit einem sicheren Passwort und einem dedizierten Passwort-Manager anmelden und dann die Benutzeroberfläche gründlich erkunden, wobei wir uns mit den einzigartigen Merkmalen der Bitcoin-Wallet und des Lightning-Netzwerks vertraut machen.

Der Knotenpunkt wird zufällig und unter einem Pseudonym mit anderen Knotenpunkten im Bitcoin-Peer-to-Peer-Netzwerk kommunizieren. Diese wesentliche Funktion ermöglicht es, die gesamte Blockchain (auch Timechain genannt) herunterzuladen, ohne von einer zentralen Entität abhängig zu sein. Es ist jedoch zu beachten, dass der anfängliche Download der Timechain mehrere Tage dauern kann, da er ein Volumen von über 500 GB hat.

Anschließend werden wir Transaktionen innerhalb der Bitcoin-Wallet durchführen, einschließlich eines Testtransfers zu einer Multisig-Wallet. Danach werden wir Kanäle im Lightning-Netzwerk öffnen und aktive Verbindungen in der Lightning-Wallet nutzen. Das Öffnen von Kanälen erfordert eine gewisse visuelle Erkundung.

Nachdem diese Operationen durchgeführt wurden, wird Bitcoin Core betriebsbereit sein. Sie können dann einige Ihrer Wallets mit Ihrem Knotenpunkt verbinden, um den Status Ihrer Konten zu überprüfen.

Es ist möglich, Ihre Bitcoin-Wallets wie [Green Wallet](https://blockstream.com/green/), [Samouraï](https://samouraiwallet.com/), [Spectre](https://specter.solutions/), [Sparrow](https://sparrowwallet.com/) über eine dedizierte Schnittstelle mit Ihrem Bitcoin-Knotenpunkt zu verbinden. Durch die Verbindung Ihrer Wallet mit Ihrem eigenen Knotenpunkt können Sie den Empfang von Geldern bestätigen, ohne einem externen Server vertrauen zu müssen, was insbesondere für Händler empfohlen wird.
Umbrel bietet auch einen App Store mit Explorern, vielen anderen Bitcoin-, Lightning- oder Datenhosting-Diensten. Neue Anwendungen werden regelmäßig zu ihrem [Appstore](https://apps.umbrel.com/) hinzugefügt. Um weitere Informationen und Unterstützung zu erhalten, besuchen Sie ihre Website, den Telegram-Chat, Discord, Github und Reddit. Zusammenfassend bietet Umbrel die Möglichkeit, dank Bitcoin die Kontrolle über Ihre finanzielle Souveränität zurückzugewinnen und Ihre eigene Bank zu werden, während Sie zum Netzwerk beitragen. Wir ermutigen Sie dringend, diese Technologie zu vertiefen und zu lernen, um sie in Ihren Laden, E-Commerce, Ihr persönliches Leben oder einfach aus Neugier zu integrieren.

# Analyse des MemPools

![mempool](https://youtu.be/0xS859IoMh8)

Der MemPool fungiert intrinsisch als Transitbereich für Bitcoin-Transaktionen, die darauf warten, in der Blockchain validiert zu werden. Um den MemPool effektiv zu untersuchen, ist Umbrel das Werkzeug der Wahl. Die Anwendung [Mempool.space](https://mempool.space/), die über die Umbrel-Schnittstelle zugänglich ist, bietet eine klare Darstellung der ausstehenden Transaktionen, der damit verbundenen Kosten und verschiedener anderer relevanter Funktionen.

Die Bitcoin-Blockchain ist im Wesentlichen eine Datenbank, die in regelmäßigen Abständen von etwa 10 Minuten Transaktionsblöcke enthält. Nach jeder Serie von 2016 Blöcken passt sich die Mining-Schwierigkeit an, um dieses durchschnittliche Intervall aufrechtzuerhalten. Wenn die Miner beschließen, ihre Energie aus dem Bitcoin-Netzwerk abzuziehen, steigt die durchschnittliche Zeit, die benötigt wird, um neue Blöcke zu finden, was zu einer Senkung der Mining-Schwierigkeit führt und anderen Minern ermöglicht, wieder wettbewerbsfähig zu werden.

Neben der Mining-Schwierigkeit ist auch die aktuelle Kosten für eine Bitcoin-Transaktion auf dem Dashboard sichtbar, sowie die Blockchain mit ihrer Blockkette. Die Gebühren für eine Bitcoin-Transaktion betragen derzeit 40 Sats/vByte. Die Transaktionsgebühren auf Bitcoin basieren auf der Komplexität der Transaktion, die als proportional zum virtuellen Gewicht (vByte) der Transaktion betrachtet wird. VBytes oder virtuelle Bytes sind eine Maßeinheit, die in Bitcoin verwendet wird, um die Größe einer Transaktion unter Berücksichtigung der SegWit-Technologie zu bewerten. Die Verwendung von vBytes ermöglicht daher eine genauere Messung der Effizienz des Platzes in einem Block.

Jeder Benutzer ist frei, die mit seiner Transaktion verbundenen Gebühren zu bestimmen, die tendenziell die Dringlichkeit der Validierung der Transaktion widerspiegeln: Je schneller der Benutzer möchte, dass seine Transaktion validiert wird, desto höher sind die Gebühren. Wenn also die Nachfrage steigt und das Blockvolumen auf 4 MB begrenzt ist (obwohl die durchschnittliche Blockgröße etwa 1,5 MB beträgt), können die Gebühren, um die Wahrscheinlichkeit zu erhöhen, dass unsere Transaktion im nächsten Block enthalten ist, signifikant steigen.

# Block Explorer & Analyse Stats

![block explorer et analyse stat](https://youtu.be/Qe9VaUhUS0E)

Wir werden eine Erkundungsreise durch die Bitcoin-Blockchain unternehmen, indem wir leistungsstarke Tools wie Block-Explorer und die BTC Explorer-App auf dem Umbrel-Knoten verwenden. Block-Explorer geben uns die Fähigkeit, die Bitcoin-Blockchain im Detail zu analysieren. Mit BTC Explorer, einer Anwendung auf Umbrel, können Sie alle Informationen über die Bitcoin-Blockchain auf Ihrer Festplatte überprüfen, sodass Sie nicht mehr von einem Dritten abhängig sind.

Wir beziehen uns auf eine bestimmte Transaktion, dieselbe wie im vorherigen Kurs untersucht, um die Funktionen und die Bedeutung dieser Tools zu demonstrieren. Wir werden auch die neuesten abgebauten Blöcke illustrieren und Informationen zu ihrem Inhalt detaillieren. Dann werden wir einen tiefen Vergleich zwischen zwei verschiedenen Blöcken anstellen, indem wir ihren Inhalt und die Zeit, die für das Mining benötigt wurde, analysieren.

Der Block Explorer ermöglicht es uns, Details eines abgebauten Blocks wie Hash, Zusammenfassung, Outputs, Gebühren, Zeit und Transaktionen zu visualisieren. Bitcoin Explorer bietet fortgeschrittenere Tools zur Analyse der Blockchain. Das erste Tool ermöglicht beispielsweise eine detaillierte Untersuchung Ihres Knotens (Synchronisation, Index, Größe der Blockchain, akzeptierte BIPs).

Bitcoin Improvement Proposals (BIP) sind Vorschläge zur Verbesserung des Bitcoin-Protokolls. Wir können die Aktivierung von Segwit und die Anzahl der Netzwerkverbindungen beobachten. Darüber hinaus bieten Blockstats detaillierte Statistiken zu Gebühren, Transaktionen, Inputs und Outputs.
Die Analyse von Segwit-Daten bietet einen Überblick über die Entwicklung von Bitcoin im Laufe der Jahre. Statistiken zu Transaktionen, Volumen, Blöcken, UTXO und Zeitstempeln sind kostenlos verfügbar. Die Interpretation dieser Daten ist entscheidend für die Finanzforschung und die Überprüfung der Bitcoin-Adoption.

Es ist wichtig, die finanzielle Souveränität in die eigene Hand zu nehmen und die Daten selbst zu recherchieren. Die Blockanalyse ermöglicht die Untersuchung von Daten eines bestimmten Blocks, wie z.B. des ersten von Satoshi im Jahr 2009 abgebauten Blocks, in dem er seine ersten 50 Bitcoins absichtlich zerstört hat, um einen ehrlichen Start zu gewährleisten.

Die Daten von Bitcoin-Transaktionen sind transparent und für alle einsehbar, einschließlich Analysten und Branchenprofis. Diese Informationen sind entscheidend, da sie wertvolle Hinweise auf die Aktivität des Bitcoin-Netzwerks, die Marktdynamik und laufende Trends liefern, was für eine fundierte Entscheidungsfindung und die Umsetzung solider Finanzstrategien unerlässlich ist. Darüber hinaus werden diese Daten zur Überwachung von Transaktionen verwendet, um die Rückverfolgbarkeit und Transparenz des Bitcoin-Netzwerks zu gewährleisten.

Eine sogenannte "schwere" Bitcoin-Transaktion, wie z.B. eine mit 673 Inputs und 1 Output, verdeutlicht den Kompromiss zwischen der Anzahl der UTXO (Unspent Transaction Outputs) und der Menge an Bitcoin in einer Adresse. UTXO repräsentieren die nicht ausgegebenen Mittel einer früheren Transaktion, die zu den Inputs zukünftiger Transaktionen werden. Eine Erhöhung der Anzahl von UTXO in einer Transaktion macht sie komplexer und teurer. Daher ist es entscheidend, UTXO zu gruppieren, um Transaktionsgebühren zu minimieren und die Nutzung des Platzes in einem Bitcoin-Blockchain-Block zu optimieren.

Das Mining, der zentrale Dreh- und Angelpunkt des Bitcoin-Protokolls, spielt eine grundlegende Rolle bei der Sicherung von Transaktionen. Der Prozess wird durch eine Anpassung der Schwierigkeit alle 2016 Blöcke reguliert, um einen durchschnittlichen Abstand von 10 Minuten zwischen den Blöcken zu halten. Gleichzeitig steigt die Hash-Rate, die die Rechenleistung des Netzwerks widerspiegelt, stetig an.

Innerhalb des Netzwerks schließen sich Miner in Mining-Pools zusammen. Diese Einheiten haben nicht die Macht, das gesamte Netzwerk zu kontrollieren, da die Miner das Privileg haben, zwischen den Pools nach Belieben zu wechseln. Innovative Technologien wie Stratum V2 geben den Minern innerhalb der Mining-Pools mehr Macht. Darüber hinaus stellen technische Lösungen wie MimbleWimble und Dandelion vielversprechende Verbesserungen für Transaktionen dar.
Par ailleurs, die historische Bedeutung der Blockchain liegt darin, dass sie alle Transaktionen von der Genesis-Block bis zu den neuesten Transaktionen archiviert. Sie umfasst die erste Bitcoin-Transaktion von Satoshi an Hal Finney im Block 170 und die berühmte Transaktion von 10.000 Bitcoins gegen zwei Pizzen im Block 57043, die das jährliche "Pizza Day" am 22. Mai ins Leben gerufen hat.

Um Ihre finanzielle Souveränität zu stärken und die Abhängigkeit von Dritten bei der Empfang und dem Versand Ihrer Bitcoins zu vermeiden, ist es entscheidend, Ihre Wallets mit Ihrem eigenen Bitcoin-Knotenpunkt zu verbinden. Die Transaktionen werden zuerst von den Knotenpunkten im Netzwerk bei ihrer Verbreitung validiert und dann ein zweites Mal, wenn sie in einen Block aufgenommen werden.

Abschließend ist es lobenswert, Bitcoin mit anderen zu teilen und sie einzuführen. Durch die Nutzung Ihres eigenen Knotenpunkts und die Beitrag zum Netzwerk können Sie Ihre eigene Bank werden. Das ultimative Ziel ist es, vollständig autonom zu werden.

# Verbindung Ihrer Wallets mit Ihrem Knotenpunkt

![Verbindung Ihrer Wallets mit Ihrem Knotenpunkt](https://youtu.be/HOV3bVcram4)

Im heutigen digitalen Zeitalter ist es von entscheidender Bedeutung, Ihre Kryptowährungen und Ihre Privatsphäre zu schützen. In diesem Zusammenhang werde ich Sie durch den Prozess führen, um Ihre mobilen und Desktop-Wallets mit unserem Bitcoin-Knotenpunkt zu verbinden. Dieser Prozess erhöht Ihre Sicherheit erheblich und gibt Ihnen mehr Kontrolle über Ihre Vermögenswerte.

Es gibt eine Vielzahl von Wallets zur Verfügung: Bitbox App, Blue Wallet, Blockstream Green, Samouraï, Phoenix, Sparrow, Wasabi, Electrum und viele andere. Jeder hat seine eigenen Spezifikationen, Stärken und Schwächen. Heute werden wir uns auf Sparrow konzentrieren, eine interessante Alternative zu Ledger Live, die für ihre einfache Verwaltung und Erstellung von Wallets bekannt ist.

In Bezug auf Sicherheit und Privatsphäre kann ein zusätzlicher Schritt unternommen werden: die Verwendung eines privaten Servers anstelle eines öffentlichen Servers. Dieser Schritt, obwohl komplexer, bietet ein höheres Maß an Kontrolle und Schutz. Die Informationen zur Verbindung mit einem privaten Server finden Sie auf Umbrel.

Denken Sie daran, dass das Aktualisieren Ihrer Wallets ein wesentlicher Schritt ist. Updates beheben Fehler, bekämpfen Schwachstellen, verbessern das Produkt und fügen manchmal nützliche neue Funktionen hinzu. Insbesondere sorgt Umbrel automatisch für die Aktualisierung aller Anwendungen. Es ist also ratsam, Ihr Umbrel auf dem neuesten Stand zu halten.
Um abschließend zu sagen, dass das direkte Verbinden Ihrer Wallets mit unserem Bitcoin-Knotenpunkt ein Schritt in Richtung finanzieller Unabhängigkeit ist. Dies gibt Ihnen ein höheres Maß an Privatsphäre und Sicherheit und ermöglicht es Ihnen, die volle Kontrolle über Ihre digitalen Vermögenswerte zu behalten. Finanzielle Souveränität bedeutet, dass man das volle Eigentum und die Kontrolle über sein Geld ohne Vermittler hat. Durch die Diversifizierung Ihrer Wallets und deren Aktualisierung machen Sie einen weiteren Schritt in Richtung Autonomie.

# Multi-Sig-Wallets über Specter

![Multi-Sig-Wallets](https://youtu.be/mV1KS-Uwjew)

Wir bieten Ihnen die Möglichkeit, einen weiteren Schritt in Richtung finanzieller Autonomie zu gehen. Unser Ziel ist es, ein Multi-Sig-Wallet mit der Anwendung Specter, die in Umbrel integriert ist, einzurichten. Wir werden die Desktop-Anwendung mit unserem Knotenpunkt verbinden, um diesen Leitfaden für alle zugänglich zu machen.

Das Konzept von Multi-Sig ist einfach: Es gewährleistet ein außergewöhnliches Maß an Sicherheit für größere Beträge. Dazu werden wir drei private Schlüssel verwenden, um unsere neue Bitcoin-Wallet zu sichern. Es gibt mehrere Sicherheitsstufen: mobile Wallets, physische Wallets, Passphrasen, Multi-Sig 2 von 3, Multi-Sig 3 von 5 oder sogar eine Kombination aus all diesen Elementen mit Open Dimes. Sie müssen kein Technologieexperte sein, um diesem Leitfaden zu folgen, aber Sie sollten mit dem System der privaten und öffentlichen Schlüssel vertraut sein.

Bereiten Sie sich vor, denn dieser Leitfaden geht schnell. Da die Geräte bereits initialisiert wurden, sollte es uns etwa 15 Minuten dauern. Um diesem Leitfaden zu folgen, benötigen Sie drei initialisierte Geräte, einen Knotenpunkt, um die Specter-Anwendung zu verbinden, sowie einen USB-Stick und einen Drucker. Wir werden die Specter-Anwendung für unsere Multi-Sig-Lösung verwenden. Sie können sie über Umbrel oder direkt von der Website von Specter Solutions herunterladen. Vergessen Sie nicht, die Signatur vor dem Download zu überprüfen. Sie können auch Ihre Multi-Sig mit Sparrow oder Electrum durchführen. Zögern Sie nicht, Ihre Recherchen anzustellen und sich mit diesen Tools vertraut zu machen, bevor Sie sie zur Verwaltung großer Beträge verwenden.

Lassen Sie uns nun zur Praxis übergehen. Hier haben wir ein 2-auf-3-System mit einem Ledger und 2 Trezor (weiß und schwarz) und Specter Desktop, das die Wallet-Schnittstelle ist, mit der wir mit unseren Wallets interagieren können und das über Umbrel mit Bitcoin Core verbunden ist.
Wir werden zuerst eine einfache Brieftasche erstellen, um mit Ledger ohne Ledger Live zu interagieren. Dadurch können wir neue Adressen generieren und Bitcoins senden. Anschließend fügen wir weitere Geräte (Tresore) hinzu, um das Multisig zu erstellen. Beginnen wir damit, das zweite Gerät (den weißen Tresor) auszuwählen, das wir über USB anschließen werden. Nachdem wir die PIN verwendet haben, um es zu aktivieren, extrahieren wir die öffentlichen Schlüssel und erstellen eine zweite Brieftasche. Dann fügen wir ein drittes Gerät (den schwarzen Trezor) hinzu und verwenden es, um eine Multisig-Brieftasche zu erstellen. Wir erstellen eine Multisig-Brieftasche, indem wir die drei Geräte auswählen, Signet zum Testen verwenden und keine Mittel verlieren, falls etwas schief geht (obwohl der Prozess für das Mainnet derselbe ist).

Dann erstellen wir die Brieftasche, indem wir die öffentlichen Schlüssel kombinieren. Die Sicherung einer Multisig-Brieftasche enthält mehrere Elemente. Um die Brieftasche wiederherzustellen, benötigen wir die drei öffentlichen Schlüssel und zwei private Schlüssel, um das Geld auszugeben. Es ist daher entscheidend, die öffentlichen Schlüssel zusammen mit der Sicherung jeder der privaten Schlüssel an einem sicheren Ort zu speichern.

Es wird empfohlen, die mnemonischen Phrasen (Liste von 24 Wörtern) der 3 privaten Schlüssel auf Papier oder Metall in mehreren Exemplaren (mindestens 2) zu notieren. Außerdem ist es ratsam, präzise und detaillierte Informationen zu schreiben, die es ermöglichen, Ihr Geld im Falle eines Problems oder für einen Erbschaftsplan wiederherzustellen. Diese Anweisungen müssen ebenfalls an einem sicheren Ort aufbewahrt werden.

Auf diese Weise haben Sie einen weiteren Schritt auf dem Weg zur Bitcoin-Souveränität getan. Indem Sie Ihre Sicherheit beherrschen und Tools wie Multisig verwenden, stärken Sie Ihre finanzielle Autonomie und schützen Ihre Vermögenswerte optimal. Denken Sie daran, dass Vorsicht und kontinuierliches Lernen der Schlüssel zum Erfolg in der Welt von Bitcoin sind.
Wenn Sie mit Testnet-Bitcoins üben möchten, können Sie diese über diesen [Faucet](https://bitcoinfaucet.uo1.net/) erhalten.

# Öffnen von Lightning-Kanälen

![Öffnen von Lightning-Kanälen](https://youtu.be/bAZJn0AH1yU)

Lassen Sie uns nun zum Lightning-Teil des Umbrel-Knotens übergehen. Wir werden ThunderHub verwenden, eine Anwendung unter mehreren, die als Lightning-Knoten-Manager dienen, wie Lightning Terminal und RideTheLightning (RTL). Diese Anwendungen geben uns einen genauen Überblick über den Zustand unserer Kanäle und dienen als Schnittstelle zwischen uns und unseren Lightning Network (LN)-Kanälen.
Zu diesem Zeitpunkt ist unser Hauptziel die Eröffnung eines neuen Kanals. Wenn Sie ThunderHub herunterladen, wird ein Standardpasswort bereitgestellt, das Sie direkt im Appstore finden können. Es ist unerlässlich, dieses Passwort zu ändern und sorgfältig in einem dedizierten Passwort-Manager aufzubewahren.

Wenn Sie erwägen, einen Kanal mit einem anderen Lightning-Knoten im Netzwerk zu öffnen, stellen sich einige Fragen. Zum Beispiel, wie viel Liquidität möchten Sie einem Kanal zuweisen? Mit welchen Parteien möchten Sie einen Kanal öffnen? Die Antworten auf diese Fragen sind entscheidend, um Ihre Transaktionen zu optimieren und potenzielle Probleme zu vermeiden.

Lassen Sie uns über die Größe der Kanäle sprechen. Es wäre nicht klug, mit einer geringen Menge wie 20k, 50k oder 100k Sats Kanäle zu öffnen. Dies wäre unzureichend und die Öffnungs- und Schließungsgebühren des Kanals würden nicht gedeckt. Ein Kanal mit geringem Betrag wäre für Sie und das Netzwerk eher schädlich als nützlich. Wenn Sie zum Beispiel einen Kanal mit meinem Knoten von 20k öffnen, würde dies kaum die Öffnungs- und Schließungsgebühren (+ Reserve) decken. Es bliebe nur Krümel zum Ausgeben übrig.

Deshalb wird empfohlen, Kanäle mit mindestens 500k-1M Sats zu öffnen. Dies würde eine bessere Routing-Option bieten, die für Sie und alle anderen, die Transaktionen durch Ihren Knoten routen, vorteilhaft ist. Es ist wichtig zu beachten, dass die Idee "je größer, desto besser" hier nicht gilt. Es wäre besser, 5-6 ausgehende Kanäle zu haben, von denen jeder zwischen 500k und 1M Sats enthält, und je nach Bedarf 4-5 eingehende Kanäle mit ähnlicher Kapazität zu haben.

Jetzt, da Sie mit der Größe der Kanäle vertraut sind, kommen wir zur Verwaltung. Was die ausgehende Liquidität (auf Ihrer Seite) betrifft, ermöglicht Ihnen Ihr LN-Knoten, LN-Zahlungen zu leisten, Dinge zu kaufen, Geld an Freunde zu senden, Dienstleistungen zu bezahlen usw. Versuchen Sie, LN-Kanäle mit Händlern zu öffnen, mit denen Sie handeln möchten. Was die eingehende Liquidität (auf der Seite Ihrer Peers) betrifft, finden Sie Peers, die bereit sind, Kanäle zu Ihrem Knoten zu öffnen. Diese eingehende Liquidität ist erforderlich, um Zahlungen auf dem LN zu erhalten.
Die Frage, mit wem man Kanäle öffnen sollte, ist von entscheidender Bedeutung. Erstens können Sie bei Händlern, mit denen Sie Transaktionen durchführen möchten, von einer direkten Routing-Option profitieren und Gebühren vermeiden. Zweitens sollten Sie an Freunde und erfahrene LN-Benutzer denken, die einen Knotenring (Ring of Fire) mit einer bestimmten Anzahl von Sats für diese Kanäle erstellen können. Dies ist perfekt, um die Liquidität auszugleichen und die Gebühren zwischen den Knoten im Ring zu reduzieren. Drittens kann Ihr Knotenring "externe" Verbindungen oder Kanäle zu anderen guten Knoten haben, was das Routing zu jedem Empfänger erleichtert und beschleunigt.

Um diese Verbindungen herzustellen, müssen Sie die öffentlichen Adressen der anderen Parteien abrufen. Sie können dies direkt bei ihnen oder über Websites wie [1ML](https://1ml.com/) oder [Amboss](https://amboss.space/) tun. Die Eröffnung eines Kanals beinhaltet Transaktionsgebühren in der Blockchain, daher sollten Sie die Momente nutzen, in denen die Mempool leer ist, um Kanäle zu öffnen. Sobald ein Kanal geöffnet ist, ist die Liquidität auf einer Seite des Kanals blockiert. Um sie auf die andere Seite zu verschieben, müssen Transaktionen für Zahlungen durchgeführt oder ein sogenannter "Submarine Swap" durchgeführt werden (dies werden wir im nächsten Teil besprechen). Es ist zu beachten, dass im Lightning Network Routinggebühren anfallen. Wenn ein Kanal aufgrund des Routings zu schnell leer wird, können Sie diese Gebühren erhöhen.

Bevor wir abschließen, ist es wichtig zu beachten, dass es eine weitere wichtige Entscheidung gibt, die bei der Eröffnung von Lightning-Kanälen getroffen werden muss: die Wahl zwischen einem öffentlichen oder einem privaten Kanal. Jeder hat seine Vor- und Nachteile, je nach Ihren Bedürfnissen und Vorlieben.

Ein öffentlicher Kanal wird dem gesamten Lightning-Netzwerk angekündigt und kann für die Zahlungsrouting verwendet werden. Dies ist eine ausgezeichnete Option, wenn Sie aktiv am Netzwerk teilnehmen und die Transaktionen anderer Benutzer erleichtern möchten. Dies kann auch (sehr geringe) Einnahmen durch die Routinggebühren generieren, die Sie erhalten können. Beachten Sie jedoch, dass ein öffentlicher Kanal für diejenigen, die ein hohes Maß an Privatsphäre wahren möchten, nicht geeignet ist, da er für alle sichtbar ist.

Auf der anderen Seite wird ein privater Kanal nicht im Netzwerk angekündigt und wird nicht für die Zahlungsrouting verwendet. Dies ist eine gute Option, wenn Sie die Privatsphäre bevorzugen und den Kanal hauptsächlich für Ihre eigenen Transaktionen verwenden möchten. Es ist zu beachten, dass ein privater Kanal zwar nicht die gleichen Möglichkeiten für Routinggebühren wie ein öffentlicher Kanal bietet, jedoch eine erhöhte Sicherheit und Privatsphäre bieten kann.
Letztendlich hängt die Wahl zwischen einem öffentlichen und einem privaten Kanal von Ihrer eigenen Situation und Prioritäten ab. Bewerten Sie sorgfältig Ihre Bedürfnisse und Ziele, bevor Sie eine Entscheidung treffen.

Zusammenfassend ist das Öffnen von Kanälen im Lightning Network ein wesentlicher technischer Schritt zur Optimierung Ihrer Transaktionen. Die Wahl der Kanalgröße, die Wahl zwischen einem öffentlichen oder privaten Kanal und die sorgfältige Auswahl der Parteien, mit denen Kanäle geöffnet werden sollen, sind entscheidende Faktoren für eine effektive und wirtschaftliche Routenführung. In unserem nächsten Teil werden wir uns mit der effektiven Verwaltung dieser Kanäle befassen. Gehen Sie also zur nächsten Sektion für weitere Details zu diesem wichtigen Aspekt des Lightning Network.

# Verwaltung von LN-Kanälen

![Verwaltung von LN-Kanälen](https://youtu.be/CgBnGQLar4o)

Nachdem wir die Öffnung von Kanälen im Lightning Network behandelt haben, richten wir unsere Aufmerksamkeit auf deren Verwaltung. Eine effektive Kanalverwaltung kann einen großen Unterschied bei der Optimierung Ihrer Lightning Network-Erfahrung ausmachen.

Das erste wesentliche Element der Kanalverwaltung ist die Balance. Die Kanäle im Lightning Network haben eine sogenannte "Liquidität", die zwischen den beiden Parteien des Kanals aufgeteilt ist. Das Ausgleichen dieser Liquidität ist entscheidend, um sicherzustellen, dass Transaktionen effizient von Ihrem Knoten geroutet werden können. Zu viel Liquidität auf einer Seite oder der anderen kann den Kanal weniger nützlich für das Routing machen. Glücklicherweise gibt es mehrere Strategien, um Kanäle auszugleichen, einschließlich der Verwendung von Diensten wie Lightning Loop von Lightning Labs, die es ermöglichen, Liquidität in und aus dem Bitcoin-Netzwerk zu bewegen.

Das zweite Element, das berücksichtigt werden muss, ist die Überwachung Ihrer Kanäle. Es ist wichtig, den Zustand Ihrer Kanäle regelmäßig zu überprüfen und die Leistung Ihres Knotens zu überwachen. Tools wie ThunderHub und RTL bieten großartige Funktionen, um Ihren Knoten zu überwachen und Ihre Kanäle zu verwalten. Sie bieten Informationen über den Zustand Ihrer Kanäle, einschließlich ihrer Liquidität, Gebühren und Kapazität. Darüber hinaus bieten sie Funktionen zum Schließen von Kanälen, Öffnen neuer Kanäle und Ausgleichen der Liquidität zwischen Kanälen.

Drittens muss die Schließung von Kanälen berücksichtigt werden. Manchmal kann es vorkommen, dass Sie einen Kanal haben, der nicht mehr nützlich oder leistungsfähig ist. In diesem Fall möchten Sie den Kanal schließen. Es ist jedoch wichtig zu beachten, dass das Schließen eines Kanals eine Transaktion auf der Bitcoin-Blockchain auslöst, die Gebühren verursachen kann. Daher ist es ratsam, Kanäle während Zeiten geringer Blockchain-Überlastung zu schließen, um die Gebühren zu minimieren.
Zusammenfassend ist das Management der Kanäle im Lightning Network ein wichtiger Faktor, um einen leistungsstarken und wirtschaftlichen Lightning-Knoten zu erhalten. Mit einer guten Ausgleichsstrategie, regelmäßiger Überwachung und intelligentem Management der Öffnung und Schließung von Kanälen können Sie Ihre Erfahrung mit dem Lightning Network optimieren. Im nächsten Abschnitt werden wir einen weiteren wichtigen Aspekt des Lightning Network behandeln: die Sicherheit.

# Umbenennen des LN-Knotens

![Umbenennen des LN-Knotens](https://youtu.be/HnK1_TDYXsY)

Die Anpassung des Alias Ihres Lightning Network-Knotens ist eine großartige Möglichkeit, sich im Netzwerk zu unterscheiden. Es ist nicht nur praktisch, sondern auch eine Möglichkeit, Ihre Erfahrung zu personalisieren. Um den Alias Ihres Knotens zu ändern, verwenden wir die Befehlszeilenschnittstelle. Wenn Sie mit dieser Schnittstelle nicht vertraut sind, keine Sorge, dieser Leitfaden wird Sie Schritt für Schritt durch den Prozess führen.

Zunächst müssen Sie das Terminal Ihres Systems öffnen. Das Terminal ist eine Befehlsschnittstelle, mit der Sie direkt mit Ihrem Betriebssystem interagieren können. Sobald das Terminal geöffnet ist, geben Sie den Befehl `ssh -t umbrel@umbrel.local` ein und drücken Sie die Eingabetaste. Dieser Befehl wird eine sichere Verbindung zu Ihrem Umbrel herstellen.

Als nächstes werden Sie aufgefordert, das Passwort Ihres Umbrel einzugeben. Beachten Sie, dass aus Sicherheitsgründen das Passwort beim Tippen nicht auf dem Bildschirm angezeigt wird. Nachdem Sie Ihr Passwort eingegeben haben, gelangen Sie zur Oberfläche Ihres Umbrel.

Sobald Sie verbunden sind, geben Sie den Befehl `sudo nano umbrel/lnd/lnd.conf` in das Terminal ein und drücken Sie die Eingabetaste. Dadurch gelangen Sie zu einem Texteditor namens Nano, in dem Sie die Konfigurationsdatei Ihres Lightning-Knotens bearbeiten können.

Erneut müssen Sie Ihr Passwort eingeben. Navigieren Sie dann in der Datei zur Sektion "Anwendungsoptionen". Fügen Sie in dieser Sektion die Zeile `alias=SOMENAME` hinzu, wobei "SOMENAME" durch den Alias ersetzt wird, den Sie für Ihren Knoten wünschen. Beachten Sie, dass die Verwendung der Maus in dieser Schnittstelle unnötig ist, verwenden Sie stattdessen die Pfeile zum Navigieren.

Um die Änderungen zu speichern, drücken Sie `Strg-X`, dann `Y` und schließlich `Eingabetaste`. Dadurch wird der Editor geschlossen und Ihre Änderungen gespeichert. Um diese Änderungen wirksam zu machen, müssen Sie Ihr Umbrel neu starten. Gehen Sie dazu zum Einstellungsmenü der Umbrel-Oberfläche und wählen Sie die Neustart-Option.

Und voilà, Sie haben den Alias Ihres Lightning Network-Knotens erfolgreich geändert! Sie können jetzt Ihren Knoten auf Websites wie 1ML oder Amboss beanspruchen. Im nächsten Abschnitt werden wir weitere Methoden diskutieren, um Ihren Lightning Network-Knoten anzupassen und zu optimieren.

### Unterstütze uns

Dieser Kurs sowie der gesamte Inhalt dieser Universität wurden Ihnen kostenlos von unserer Gemeinschaft zur Verfügung gestellt. Um uns zu unterstützen, können Sie ihn teilen, Mitglied der Universität werden und sogar über GitHub zu ihrer Entwicklung beitragen. Im Namen des gesamten Teams vielen Dank!

### Bewertung des Kurses

Ein Bewertungssystem für den Kurs wird bald in diese neue E-Learning-Plattform integriert! In der Zwischenzeit vielen Dank für die Teilnahme am Kurs und wenn Sie ihn genossen haben, denken Sie daran, ihn zu teilen.

# Spaß mit LN

![Verwendung von LN](https://youtu.be/6yekAvH13E0)

Jetzt, da Sie Ihren Knoten konfiguriert haben, ist es Zeit, ihn zu nutzen. Für diese erste Nutzung werden wir uns auf [Satoshi's Place](https://satoshis.place/) konzentrieren, einen faszinierenden Service, der es Ihnen ermöglicht, Satoshis, die kleinste Einheit von Bitcoin, auszugeben, um Pixelkunst auf einem öffentlichen Platz online zu erstellen. Jeder Pixel ändert seine Farbe für einen Satoshi. Lassen Sie Ihrer Kreativität freien Lauf, ich habe zum Beispiel eine Pokeball für 166 Satoshis erstellt! Die Zahlungen erfolgen über "Rechnungen" oder "Invoices" im Lightning-Netzwerk. Diese Rechnungen können als QR-Code dargestellt werden, was die Zahlung einfach und sofortig macht.

Wenn eine Transaktion mehrere Knoten durchläuft, fallen in der Regel Routinggebühren an. Es ist daher entscheidend, gut mit dem Zentrum des Netzwerks verbunden zu sein, um diese Kosten zu reduzieren. Eine Alternative wäre, direkt mit dem Händler einen Kanal zu öffnen. Dies hat mehrere Vorteile, wie zum Beispiel niedrigere Transaktionsgebühren und schnellere Transaktionsgeschwindigkeiten.

Als Beispiel werden wir einen Kanal mit Satoshi's Place für zukünftige Zahlungen erstellen. Nach der Kanalerstellung ist eine Wartezeit von etwa 30 Minuten erforderlich, damit der Kanal betriebsbereit wird. Sobald der Kanal erstellt wurde, können Sie direkte Zahlungen vornehmen. Sie können zum Beispiel einen Satoshi kostenlos über das Lightning-Netzwerk ohne Vertrauensintermediär senden.

Das Lightning-Netzwerk bietet mehrere Vorteile, wie niedrige Kosten und die Möglichkeit, regelmäßige Zahlungen zu leisten. Zum Einstieg wird empfohlen, Wallets wie Wallet of Satoshi oder Alby zu verwenden. Diese Wallets ermöglichen das Bezahlen von Rechnungen über das Lightning-Netzwerk. Um mehr zu erfahren, können Sie diesen [Artikel](https://asi0.substack.com/p/comparatif-des-portefeuilles-ln) von Darthcoin lesen.

Zusammenfassend beweist das Lightning-Netzwerk die Fähigkeit von Bitcoin, sich weiterzuentwickeln. Es ermöglicht nicht nur kostengünstige Transaktionen, sondern bietet auch eine Lösung für die Skalierungsprobleme, die Bitcoin in der Vergangenheit hatte.

# Bitcoin mit BTCpay-Server akzeptieren

![Bitcoin in Ihrem Geschäft akzeptieren](https://youtu.be/zpCMlLfiRgg)
Im Laufe dieses letzten Kapitels werden wir die verschiedenen Möglichkeiten untersuchen, Bitcoin für Ihr Unternehmen zu akzeptieren. Wir werden drei Hauptoptionen überprüfen, nämlich BTCPay Server über Ihren Umbrel-Knoten, BTCPay über einen externen Luna-Knoten und schließlich über OpenNode. Es ist wichtig zu beachten, dass jede Option ihre Nuancen hat und es entscheidend ist, diejenige auszuwählen, die am besten zu Ihren spezifischen Bedürfnissen passt.

Stellen Sie sich vor, Sie besitzen ein Restaurant und haben einen Umbrel-Knoten in Ihrem Unternehmen. In diesem Fall können Sie BTCpay direkt unter Tor verwenden. Dies ist eine ideale Lösung für physische Operationen, bei denen Kunden persönlich bezahlen.

Für den E-Commerce ist die Verwendung von BTCPay unter Tor von Ihrem Umbrel-Knoten aus jedoch nicht realisierbar. In diesem Fall ist die Verwendung eines externen Knotens im Clearnet, wie Luna Node, bevorzugt. Dies bietet mehr Flexibilität und ermöglicht eine nahtlose Integration mit Ihrer Online-Handelsplattform.

Für diejenigen, die eine All-in-One-Lösung suchen, die einfach zu verwalten ist, ist OpenNode eine ausgezeichnete Option. Die Konfiguration und Verwendung können jedoch ziemlich komplex sein. Aus diesem Grund planen wir, diese Lösung in einem dedizierten Schulungskurs ausführlicher zu behandeln.

Unten finden Sie Links zu den verschiedenen genannten Diensten:

- [OpenNode] (https://www.opennode.com/)
- [BTCPay Server] (https://btcpayserver.org/)
- [Luna Node] (https://www.lunanode.com/) und der Leitfaden zu [BTCPay Server mit Luna Node] (https://docs.btcpayserver.org/Deployment/LunaNode/)

Außerdem hatte ich die Gelegenheit, Nicolas Dorier, den Schöpfer von BTCPay Server, zu interviewen. Wenn Sie daran interessiert sind, schauen Sie sich gerne unser Gespräch an, indem Sie [hier] (https://www.youtube.com/watch?v=XR6qB76hCL0&pp=ygUoaW50ZXJ2aWV3IG5pY29sYSBkb3JpZXIgZGVjb3V2cmUgYml0Y29pbg%3D%3D) klicken. Sie werden viele interessante Informationen und wertvolle Tipps zur Optimierung der Verwendung von BTCPay Server in Ihrem Unternehmen entdecken.

Insgesamt kann die Akzeptanz von Bitcoin Ihrem Unternehmen eine Vielzahl von Vorteilen bieten. Ob Sie ein lokales Restaurant oder ein globales E-Commerce-Unternehmen sind, es gibt eine Lösung, die Ihren Bedürfnissen entspricht. Nehmen Sie sich Zeit, um die verschiedenen Optionen zu prüfen, und zögern Sie nicht, sich auf dieses neue Bitcoin-Abenteuer einzulassen.

# Zusammenfassung der Schulung

![Schlussfolgerung] (https://youtu.be/QrKbagtUE1s)
Wir sind nun am Ende unserer umfassenden Erkundung des Lightning-Netzwerks von Bitcoin angekommen. Wir haben einen komplexen Weg zurückgelegt, der von technologischen Innovationen und neuen Perspektiven auf die Art und Weise geprägt war, wie wir mit unserem digitalen Geld interagieren. Vom ersten Erkunden von Umbrel bis hin zur Eröffnung und Verwaltung von Lightning-Kanälen war jeder Schritt ein Fortschritt hin zu einem besseren Verständnis und einer größeren Beherrschung dieser revolutionären Technologie.

Wir begannen mit einer Einführung in Umbrel, um uns mit der Benutzeroberfläche und den wichtigsten Funktionen vertraut zu machen. Anschließend tauchten wir in den Mempool ein und lernten, wie man ausstehende Transaktionen analysiert, um einen tieferen Einblick in das Bitcoin-Netzwerk zu erhalten. Danach erkundeten wir Block-Explorer und Netzwerkstatistiken, unverzichtbare Werkzeuge zur Überwachung des Netzwerkstatus.

Als nächstes widmeten wir uns dem persönlichsten Aspekt des Bitcoin-Netzwerks: der Wallet. Wir lernten, wie man unsere Wallet mit unserem Knoten verbindet und entdeckten die Bedeutung und Sicherheit von Multisig-Wallets mit Specter.

Dann tauchten wir in die Welt des Lightning-Netzwerks ein. Wir erkundeten die Eröffnung und Verwaltung von Lightning-Kanälen, zwei entscheidende Aspekte für eine optimale Funktionsweise unseres Knotens. Wir lernten auch, wie man unseren Knoten umbenennt, um seine Identifizierung im Netzwerk zu erleichtern.

Wir erhielten auch einen spielerischen Einblick in die Verwendung des Lightning-Netzwerks durch Satoshi's Place, ein konkretes Beispiel dafür, wie LN für kostengünstige Mikrotransaktionen genutzt werden kann.

Schließlich widmeten wir uns dem geschäftlichen Aspekt von Bitcoin. Wir erkundeten, wie man Bitcoin in seinem Geschäft über BTCpay Server akzeptiert und dabei verschiedene Konfigurationen je nach Bedarf berücksichtigt.

Das Beherrschen des Lightning-Netzwerks ist jedoch keine Aufgabe, die an einem Tag erledigt werden kann. Es handelt sich um eine sich ständig weiterentwickelnde, komplexe und nuancierte Technologie. Es erfordert Zeit, Übung und den Willen zu lernen, um dieses Werkzeug wirklich zu beherrschen. Wie Bitcoin selbst ist das Lightning-Netzwerk ein Abenteuer, eine Erkundung dessen, was im Bereich der digitalen Finanzen möglich ist. Aber mit Geduld, Ausdauer und dem Willen zu lernen, werden Sie bald in der Lage sein, sich im Lightning-Netzwerk mühelos und selbstbewusst zu bewegen.

Insgesamt war die Reise, die wir gemeinsam durch das Lightning-Netzwerk unternommen haben, erst der Anfang. Die Beherrschung dieser Technologie bietet viele Möglichkeiten und Vorteile. Also fahren Sie fort zu erkunden, zu lernen und mit dem Lightning-Netzwerk zu experimentieren. Die Zukunft der Finanzen liegt in greifbarer Nähe.
Zum Abschluss ist es wichtig zu betonen, dass diese Schulung, genauso wie die anderen, die wir anbieten, vollständig kostenlos ist. Wir glauben fest an die Bedeutung des Wissensaustauschs und daran, den Zugang zu Informationen so frei und offen wie möglich zu gestalten. In diesem Geist haben wir beschlossen, alles, was wir über das Lightning-Netzwerk gelernt haben, mit Ihnen zu teilen.

Wenn Sie jedoch Wert in dieser Schulung gefunden haben und uns unterstützen möchten, laden wir Sie ein, unsere E-Commerce-Website unter folgender Adresse zu besuchen: https://thebitcoinrabbithole.myshopify.com/. Durch Einkäufe auf unserer Website tragen Sie nicht nur dazu bei, unsere Arbeit zu unterstützen, sondern helfen uns auch weiterhin, kostenlose und qualitativ hochwertige Schulungen anzubieten.

Vielen Dank, dass Sie sich die Zeit genommen haben, diese Schulung zu absolvieren. Ihre Unterstützung und Ihr Interesse an unserer Arbeit bedeuten uns viel.

# Dank und weiterhin den Kaninchenbau erkunden

Herzlichen Glückwunsch zum Abschluss dieser LN 202-Schulung! Ich hoffe von ganzem Herzen, dass sie Ihnen gefallen und Türen geöffnet hat. Ihre Entdeckung von Bitcoin steht erst am Anfang und ich lade Sie ein, alle anderen verfügbaren Schulungen an der Universität zu entdecken.

- ECON 201 behandelt die österreichische Wirtschaft
- SECU 101 ermöglicht es Ihnen, Ihre Sicherheit zu aktualisieren
- MINAGE 201 für mehr Informationen zum Mining
- (und viele mehr)

Küsse und bis bald!
