---
name: Liquid Bootcamp Grundlagen
goal: Gewinnen Sie ein umfassendes Verständnis des Liquid Network- und des Elements-Projekts und lernen Sie, wie man fortschrittliche Lösungen für vertrauliche Transaktionen, Tokenisierung und dezentrale Netzwerkarchitekturen implementiert.
objectives: 

  - Verstehen der Grundlagen der Liquid-Architektur und ihrer Beziehung zu Bitcoin.
  - Lernen Sie, Liquid-Knoten mit der Elements-Software zu konfigurieren und zu betreiben.
  - Sondierung des Einsatzes vertraulicher Transaktionen und der Ausgabe von Vermögenswerten auf dem Liquid Network.
  - Verstehen der geschäftlichen und technischen Aspekte von Liquid für Anwendungen auf den Kapitalmärkten.

---

# Einführung in das Liquid-Netz


Begeben Sie sich auf eine Bildungsreise, die ein tiefes Verständnis des Liquid Network- und des Elements-Projekts vermitteln soll. Dieses Bootcamp kombiniert Theorie und Praxis, um Ihnen die technischen, architektonischen und geschäftlichen Grundlagen zu vermitteln, die zur Implementierung und Nutzung der Liquid-Funktionen erforderlich sind. Von vertraulichen Transaktionen bis hin zum Ökosystemdesign ist dieser Kurs ideal für diejenigen, die ihr Wissen über fortgeschrittene Tools innerhalb des Bitcoin-Ökosystems erweitern möchten.


Mit Präsentationen von Branchenexperten deckt der Kurs Themen wie die Liquid-Architektur, Tokenisierungsanwendungen, technische Konzepte von Elements und innovative Anwendungsfälle wie das Breez-SDK ab. Der Kurs ist so konzipiert, dass er für Anfänger und fortgeschrittene Benutzer zugänglich ist, bietet aber auch erfahrenen Entwicklern, die Liquid als Plattform zur Optimierung ihrer Projekte beherrschen möchten, einen Mehrwert.

+++

# Einführung


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Überblick über den Kurs


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Willkommen zum Liquid-Bootcamp, einer umfassenden Schulung, die Sie mit dem Wissen und den Fähigkeiten ausstatten soll, um das Liquid Network- und das Elements-Projekt effektiv zu nutzen. Dieser Kurs bietet eine umfassende Erkundung der besonderen Merkmale von Liquid, einschließlich Confidential Transactions, der Ausgabe von Vermögenswerten und seiner föderierten Netzwerkarchitektur, und führt gleichzeitig in die grundlegenden Konzepte von Elements ein, der Software, die Liquid unterstützt.


Während des Bootcamps werden Sie die praktischen Anwendungen des Liquid Network erkunden, von der Einrichtung und dem Betrieb von Knoten bis hin zum Verständnis seiner Verwendung in den Kapitalmärkten und der Tokenisierung des Bitcoin. Mit Präsentationen von Branchenexperten erhalten Sie auch Einblicke in fortgeschrittene Themen wie HTLCs, das Breez SDK und das Blockstream AMP-Projekt.


Dieses Bootcamp wurde ursprünglich als Präsenzveranstaltung durchgeführt und folgte einem strukturierten Zeitplan (wie in der Abbildung dargestellt), der für Live-Sitzungen konzipiert wurde. Für diese Kursanpassung wurde der Inhalt jedoch neu organisiert, damit er besser für ein Online-Format geeignet ist und die Teilnehmer ihn besser verstehen. Die neue Reihenfolge gewährleistet eine logische Abfolge von grundlegenden Konzepten zu fortgeschritteneren und technischen Themen und maximiert so den Lernerfolg.


Diese Reise ist so strukturiert, dass sie sich an Teilnehmer mit unterschiedlichem Wissensstand richtet und eine Mischung aus theoretischem Wissen und praktischer Erfahrung bietet. Am Ende dieses Bootcamps werden Sie ein solides Verständnis der Architektur von Liquid, seiner Integration mit Bitcoin und der Nutzung seiner innovativen Funktionen zur Erstellung und Optimierung von Finanzlösungen haben.


Tauchen Sie ein in die Welt der Liquid Sidechain und schöpfen Sie ihr volles Potenzial jetzt aus!

# Grundlagen


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Liquid Architektur


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Liquid Network Architektur und Konsensmodell


Liquid Network ist eine föderierte Sidechain, die auf der Codebasis von Elements aufbaut. Sie wurde entwickelt, um die Fähigkeiten von Bitcoin zu erweitern und sich dabei auf dessen grundlegende Sicherheit zu verlassen. Im Gegensatz zum Proof-of-Work von Bitcoin arbeitet Liquid mit einem föderierten Konsensmodell. Das Netz wird von einer weltweit verteilten Gruppe von Mitgliedern, darunter Börsen, Handelsschalter und Infrastrukturanbieter, unterhalten. Aus dieser Mitgliedschaft werden fünfzehn "Funktionäre" ausgewählt, die als Blocksignierer fungieren.


Diese Funktionäre produzieren Blöcke in einem deterministischen Rundlaufverfahren, wobei jede Minute ein neuer Block erzeugt wird. Dieser präzise Zeitplan steht im Gegensatz zu den probabilistischen Zehn-Minuten-Intervallen von Bitcoin. Damit ein Block gültig ist, muss er von mindestens 11 der 15 Funktionäre unterschrieben werden (eine Zwei-Drittel-plus-eins-Schwelle). Dieser Mechanismus verleiht Liquid eine "Zwei-Block-Finalität", was bedeutet, dass es nach zwei Bestätigungen einer Transaktion (ca. zwei Minuten) mathematisch unmöglich ist, die Kette zu reorganisieren. Diese Geschwindigkeit und Sicherheit sind entscheidend für Arbitrage, automatisierten Handel und eine schnelle Abrechnung zwischen den Börsen.


Der Zusammenschluss ist dynamisch. Durch das Dynamic Federation (Dynafed)-Protokoll kann das Netz Funktionsträger austauschen oder Parameter aktualisieren, ohne dass ein hartes fork erforderlich ist. Dadurch kann sich das System weiterentwickeln und Hardware oder Mitglieder nahtlos ersetzen, während der kontinuierliche Betrieb aufrechterhalten wird.


### Confidential Transactions und Vermögensverwaltung


Ein entscheidendes Merkmal von Liquid ist seine native Unterstützung für Confidential Transactions (CT) und mehrere Vermögenswerte. In der Bitcoin-Hauptkette sind alle Transaktionsdetails - Sender, Empfänger und Betrag - öffentlich. In Liquid verwendet CT kryptografische Zusagen, um die Art des Vermögenswerts und den Betrag vor dem öffentlichen Hauptbuch zu verbergen, während das Netzwerk dennoch überprüfen kann, ob die Transaktion gültig ist (d. h. keine Inflation stattgefunden hat). Nur die Teilnehmer, die im Besitz der Verblendungsschlüssel sind, können die spezifischen Werte einsehen, was einen Grad an kommerzieller Privatsphäre bietet, der für Institutionen, die große Positionen bewegen, unerlässlich ist.


Liquid behandelt alle Vermögenswerte als "native" Bürger der Blockchain. Dazu gehören Liquid Bitcoin (LBTC), Stablecoins wie USDT und Sicherheits-Token. Die Ausgabe eines Vermögenswerts erfordert keine komplexen Smart Contracts, sondern ist eine grundlegende Funktion des Protokolls.


#### Regulierte Vermögenswerte und AMP

Für Vermögenswerte, die die Einhaltung von Vorschriften erfordern, wie z. B. Sicherheits-Token, setzt Liquid die Blockstream Asset Management Platform (AMP) ein. Diese führt eine Genehmigungsschicht ein, bei der Transaktionen eine zweite Signatur von einem Autorisierungsserver benötigen. Dies ermöglicht es Emittenten, Regeln - wie Whitelisting oder KYC-Anforderungen - auf einer granularen Ebene durchzusetzen und so die Effizienz einer Blockchain mit den regulatorischen Kontrollen des traditionellen Finanzwesens zu kombinieren.


### Die Two-Way Peg- und Sicherheitsinfrastruktur


Die Verbindung zwischen Liquid und Bitcoin wird durch eine wechselseitige Kopplung aufrechterhalten. Zum "peg-in" sendet ein Benutzer Bitcoin an eine generierte Adresse auf mainchain. Diese Gelder werden für 102 Bestätigungen (ca. 17 Stunden) gesperrt, um das Risiko einer Umstrukturierung auszuschließen. Nach der Bestätigung wird ein gleichwertiger Betrag an LBTC auf der Liquid Sidechain gemünzt.


Das "peg-out"-Verfahren ermöglicht es den Nutzern, LBTC gegen Bitcoin einzutauschen. Dies erfordert das Verbrennen von LBTC und eine kryptografische Autorisierung durch die Föderation. Um Diebstahl zu verhindern, werden Peg-Outs durch Peg-Out Authorization Keys (PAKs), die von Verbandsmitgliedern gehalten werden, streng kontrolliert. Darüber hinaus können Gelder sofort über Drittanbieter wie SideSwap getauscht werden, wodurch die Abwicklungsverzögerung umgangen und die Liquidität beschleunigt wird.


#### Hardware-Sicherheitsmodule (HSMs)

Die Sicherheit wird strikt über die Hardware durchgesetzt. Die Funktionäre bewahren ihre privaten Schlüssel nicht auf Standardservern auf, sondern verwenden Hardware-Sicherheitsmodule (HSM). Diese Geräte sind von der Logik des Host-Servers abgekoppelt und werden nach strengen Regeln programmiert. So weigert sich ein HSM beispielsweise, einen Block zu signieren, wenn seine Höhe nicht größer ist als die des vorherigen Blocks, um ein Umschreiben der Geschichte zu verhindern. Dieses "gegnerische" Sicherheitsmodell geht davon aus, dass der Host-Server kompromittiert werden könnte, und gewährleistet, dass die Schlüssel auch dann sicher bleiben, wenn der physische Standort durchbrochen wird.


## Grundlagen von Elements


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: Die Gründung von Liquid


Elements ist eine Open-Source-Blockchain-Plattform, die von der Bitcoin Core-Codebasis abgeleitet ist. Sie erweitert die Funktionalität von Bitcoin, indem sie Sidechain-unabhängige Blockchains ermöglicht, die Vermögenswerte zu und von Bitcoin übertragen können. Während Bitcoin Core das Bitcoin-Netzwerk betreibt, ist Elements die Software-Engine hinter Liquid Network und anderen benutzerdefinierten Sidechains.


Die Beziehung ist einfach: Liquid ist eine spezifische "Instanz" einer Elements-Sidechain, die für den Produktionseinsatz mit einem föderierten Konsensmodell konfiguriert ist. Entwickler, die mit Bitcoin vertraut sind, werden Elements intuitiv finden, da es die gleiche RPC (Remote Procedure Call)-Schnittstelle und Befehlszeilenstruktur (`elements-cli`, `elements-d`, `elements-qt`) beibehält. Der Hauptunterschied liegt in der Konfiguration: Mit `chain=liquidv1` wird ein Knoten mit dem Liquid-Hauptnetz verbunden, während mit `chain=elementsregtest` eine lokale Regressionstestumgebung geschaffen wird, in der Entwickler generate-Blöcke sofort und ohne externe Abhängigkeiten testen können.


#### Ausgabe von Vermögenswerten

Ein herausragendes Merkmal von Elements ist die native Ausgabe von Vermögenswerten. Im Gegensatz zu Ethereum, wo Token komplexe Smart Contracts sind, sind Vermögenswerte in Elements erstklassige Bürger, die über einen einfachen RPC-Befehl (`issueasset`) erstellt werden.


- Eindeutige Bezeichner:** Jedes Asset erhält eine eindeutige 64-stellige hexadezimale ID.
- Reissuance-Token:** Emittenten können optional Reissuance-Token erstellen, die dem Inhaber das Recht einräumen, zu einem späteren Zeitpunkt mehr von dem Vermögenswert zu prägen (nützlich für Stablecoins oder Security-Token).
- Asset Registry:** Da Hex-IDs nicht für Menschen lesbar sind, ordnet das Blockstream Asset Registry diese IDs Namen und Tickern zu (z. B. "USDT"), ähnlich wie ein DNS für Assets.


### Datenschutz über Confidential Transactions


Elements behebt eine der wichtigsten Einschränkungen öffentlicher Blockchains: den Mangel an kommerzieller Privatsphäre. Auf Bitcoin ist jeder Transaktionsbetrag für die Welt sichtbar. Elements führt **Confidential Transactions (CT)** ein, das den Betrag und die Art des Vermögenswerts kryptografisch verbirgt und es dem Netzwerk dennoch ermöglicht, die Gültigkeit der Transaktion zu überprüfen.


Dies wird durch **Pedersen Commitments** und **Range Proofs** erreicht.


- Pedersen Commitments** ersetzen den sichtbaren Betrag durch eine kryptographische Verpflichtung. Aufgrund der homomorphen Verschlüsselung können Prüfer prüfen, ob *Eingangsverpflichtungen = Ausgangsverpflichtungen + Gebühren*, ohne die tatsächlichen Werte zu sehen.
- Bereichsnachweise** verhindern, dass ein Benutzer Geld aus dem Nichts erschafft (z. B. durch Verwendung negativer Zahlen), indem er mathematisch nachweist, dass der versteckte Wert eine positive ganze Zahl innerhalb eines gültigen Bereichs ist.


Für einen außenstehenden Beobachter zeigt eine vertrauliche Transaktion gültige Eingaben und Ausgaben, verschleiert aber, *was* und *wie viel* gesendet wird. Nur der Absender und der Empfänger (die im Besitz der Verblendungsschlüssel sind) können die Daten im Klartext sehen.


### Entwicklung und RPC Arbeitsablauf


Die Interaktion mit einem Elements-Knoten erfolgt hauptsächlich über seine JSON-RPC-Schnittstelle. Dadurch können Anwendungen, die in Python, JavaScript oder Go geschrieben wurden, mit der Blockchain kommunizieren.



- Einrichtung:** Ein Entwickler beginnt in der Regel im Modus "Regtest". Dies ermöglicht die sofortige Erzeugung von Blöcken (`generateblock`), um Transaktionen sofort zu bestätigen und die 1-minütige Blockzeit des Live-Netzwerks zu umgehen.
- Befehle:** Standard-Bitcoin-Befehle wie "getblockchaininfo" sind ebenso verfügbar wie Elements-spezifische Befehle wie "dumpblindingkey" (zur Prüfung von CTs) oder "pegin" (zum Verschieben von BTC in die Sidechain).
- Aliase:** Um mehrere Knoten zu verwalten (z.B. einen "Sender" und einen "Empfänger" zum Testen), verwenden Entwickler oft Shell-Aliase wie `e1-cli` und `e2-cli`, die auf verschiedene Datenverzeichnisse zeigen und so ein Peer-to-Peer-Netzwerk auf einem einzigen Rechner simulieren.


Diese Architektur ermöglicht es Entwicklern, anspruchsvolle Finanzanwendungen - wie z. B. Wertpapierplattformen oder private Zahlungs-Gateways - unter Verwendung der robusten und vertrauten Werkzeuge des Bitcoin-Ökosystems zu erstellen.


## Verbinden von Bitcoin Schichten


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Cross-Layer Infrastruktur und HTLCs


Das Bitcoin-Ökosystem hat sich zu einer mehrschichtigen Architektur entwickelt, bei der die Mainchain für die Abrechnung, Lightning für die Geschwindigkeit und Liquid für fortschrittliche Asset-Funktionen sorgen. Die Übertragung von Werten zwischen diesen Schichten ohne zentralisierte Vermittler erfordert ein vertrauensloses kryptografisches Primitiv: das Hash Time Locked Contract (HTLC).


Ein HTLC schafft einen bedingten Zahlungskanal, der unabhängige Systeme atomar verbindet. Er funktioniert über zwei primäre Beschränkungen: eine **Hash-Sperre** und eine **Zeitsperre**.


- Das Hash-Schloss:** Geldmittel können sofort ausgegeben werden, wenn der Empfänger ein geheimes "Vorabbild" preisgibt, das einem bestimmten kryptografischen Hash entspricht.
- Die Zeitsperre:** Wenn der Empfänger das Geheimnis nicht innerhalb einer bestimmten Zeitspanne (Blockhöhe) preisgibt, kann der ursprüngliche Absender das Geld zurückfordern.


Diese Zwei-Pfad-Struktur gewährleistet Sicherheit. Bei einem schichtenübergreifenden Tausch wird in beiden Netzen das gleiche Hash-Schloss verwendet. Wenn der Empfänger das Geheimnis preisgibt, um Gelder auf einer Ebene (z. B. Liquid) einzufordern, wird dieses Geheimnis für den Sender sichtbar, der es dann verwenden kann, um die gegenseitigen Gelder auf der anderen Ebene (z. B. Lightning) einzufordern. Diese kryptografische Bindung garantiert, dass der Swap entweder für beide Parteien erfolgreich abgeschlossen wird oder für beide scheitert, wodurch das Risiko ausgeschlossen wird, dass eine Partei Gelder verliert, während die andere sie gewinnt.


### Das Taproot- und MuSig2-Upgrade


Ältere HTLCs (SegWit v0) funktionierten gut, hatten aber Nachteile in Bezug auf Datenschutz und Effizienz. Sie erforderten die Veröffentlichung der gesamten Skriptlogik on-chain, wodurch Swap-Transaktionen für Blockchain-Analysten leicht identifizierbar und aufgrund ihrer Datengröße teurer wurden. Die Einführung von Taproot (SegWit v1) und des MuSig2-Protokolls hat diese Architektur revolutioniert.


Taproot ermöglicht die **Schlüsselaggregation** über MuSig2. Anstatt ein komplexes Skript mit mehreren öffentlichen Schlüsseln zu offenbaren, können die Swap-Teilnehmer mit MuSig2 ihre Schlüssel zu einem einzigen aggregierten öffentlichen Schlüssel zusammenfassen.


- Kooperativer "Schlüsselweg":** Wenn beide Parteien dem Tausch zustimmen (der "glückliche Weg"), unterzeichnen sie die Transaktion gemeinsam. Für das Netzwerk sieht dies genauso aus wie eine normale Zahlung mit einer einzigen Unterschrift. Sie verbraucht nur minimalen Speicherplatz und gibt keinerlei Informationen über die Swap-Bedingungen preis.
- Skriptpfad des Gegners:** Wenn eine Partei nicht mehr reagiert oder böswillig ist, wird das zugrunde liegende Skript (das die Hash-/Zeitsperren enthält) erst dann offengelegt. Dieses ist in einem Merkle-Baum organisiert, der es der ehrlichen Partei ermöglicht, nur den spezifischen Zweig offenzulegen, der für die Rückgewinnung von Geldern erforderlich ist, während der Rest der Vertragslogik verborgen bleibt.


### Praktische Umsetzung: Liquid-Blitz-Austausch


In der Praxis ermöglichen diese Protokolle einen nahtlosen Austausch zwischen den Schichten von Bitcoin. Ein typischer Liquid-zu-Lightning-Swap beginnt damit, dass ein Kunde einen Swap bei einem Dienstanbieter anfordert. Der Kunde legt eine Lightning-Rechnung vor, und der Anbieter sperrt den entsprechenden Liquid-Bitcoin (L-BTC) in eine Taproot-fähige HTLC-Adresse.


Die Atomarität wird durchgesetzt, wenn die Zahlung abgewickelt wird. Um die L-BTC einfordern zu können, muss der Dienstleister über das Preimage verfügen. Er erhält dieses Preimage nur, wenn er die Lightning-Rechnung des Kunden erfolgreich bezahlt. In dem Moment, in dem die Lightning-Zahlung abgeschlossen ist, wird das Preimage offengelegt, sodass der Anbieter die Liquid-Gelder freischalten kann.


#### Wallet Abstraktion und UTXO Verwaltung

Für die Endnutzer ist diese Komplexität völlig abstrahiert. Moderne Wallets wie Aqua erledigen die Schlüsselgenerierung, die Rechnungserstellung und die Signierung im Hintergrund. Der Nutzer "bezahlt" eine Lightning-Rechnung einfach mit seinem Liquid-Guthaben. Hinter den Kulissen verwaltet der Dienst die UTXO-Konsolidierung, indem er in regelmäßigen Abständen kleine, nicht beanspruchte oder erstattete Ausgänge säubert, um die wallet-Effizienz aufrechtzuerhalten und die Auswirkungen auf die Gebühren in Zeiten hohen Verkehrsaufkommens zu minimieren.


## Liquid Network Überblick


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network Architektur und Konsens


Der Liquid Network arbeitet als föderierte Sidechain, die auf der **Elements**-Codebasis aufbaut. Während Elements - ein fork von Bitcoin Core - die Softwaregrundlage bildet, ist Liquid die Implementierung des Produktionsnetzwerks. Im Gegensatz zum Proof-of-Work von Bitcoin, der sich auf das konkurrierende mining stützt, verwendet Liquid ein **Föderiertes Konsensmodell**.


Das Netz wird von fünfzehn weltweit verteilten "Funktionären" gewartet Diese Einrichtungen betreiben spezialisierte Server, die zwei wichtige Aufgaben erfüllen:

1.  **Blockproduktion:** Die Funktionäre erstellen abwechselnd Blöcke in einem deterministischen Round-Robin-Zeitplan, wobei genau jede Minute ein neuer Block erzeugt wird.

2.  **Blocksignierung:** Damit ein Block gültig ist, muss er von mindestens 11 der 15 Funktionsträger signiert werden.


Diese 11-von-15-Schwelle stellt sicher, dass das Netz den Ausfall von bis zu vier Knoten tolerieren kann, ohne dass es zum Stillstand kommt. Der Hauptvorteil dieses Kompromisses ist die **deterministische Endgültigkeit**. Während Bitcoin mit Wahrscheinlichkeiten arbeitet, wird bei Liquid nach zwei Blöcken (ca. zwei Minuten) eine Abrechnungssicherheit erreicht. Sobald ein Block mit einer einzigen Bestätigung versehen ist, kann die Kette nicht mehr reorganisiert werden, was sie für Arbitrage und eine schnelle Abrechnung äußerst effektiv macht.


### Confidential Transactions und einheimische Vermögenswerte


Der Liquid zeichnet sich durch die standardmäßige Verwendung von **Confidential Transactions (CT)** aus. Bei Bitcoin und mainchain sind Absender, Empfänger und Betrag öffentlich. Liquid verbessert dies, indem es den Betrag und den Asset-Typ kryptografisch verbirgt, während die Absender- und Empfängeradressen zur Überprüfung sichtbar bleiben.


Um sicherzustellen, dass ein Benutzer kein Geld drucken kann (z. B. durch Senden negativer Beträge), verwendet Liquid **Pedersen Commitments** und **Range Proofs**. Diese kryptografischen Primitive ermöglichen es dem Netzwerk, zu überprüfen, dass *Eingaben = Ausgaben + Gebühren* und dass alle Werte positive ganze Zahlen sind, ohne dass die spezifischen Zahlen jemals dem öffentlichen Hauptbuch offengelegt werden. Nur die Teilnehmer, die im Besitz der Verblendungsschlüssel sind, können die entschlüsselten Daten einsehen.


#### Ausgabe von Vermögenswerten

Liquid behandelt alle Vermögenswerte als "nativ" Ob es sich um Liquid Bitcoin (L-BTC), einen Stablecoin wie USDT oder ein Wertpapier token handelt, sie alle haben dieselbe Architektur. Die Ausgabe eines Vermögenswerts erfordert keine intelligenten Verträge, sondern nur einen einfachen RPC-Aufruf.


- Unregulierte Vermögenswerte:** Können von jedermann ohne Genehmigung ausgegeben werden.
- Regulierte Vermögenswerte:** Mit der Blockstream Asset Management Plattform (AMP) können Emittenten Compliance-Regeln (wie KYC/AML) durchsetzen, indem sie eine zweite Signatur von einem Autorisierungsserver verlangen, bevor ein Vermögenswert bewegt werden kann.


### Der zweiseitige Pflock und die dynamische Föderation


Die Brücke zwischen Bitcoin und Liquid ist der **Two-Way Peg**. Sie ermöglicht es Nutzern, BTC auf die Sidechain (Peg-in) und zurück zum mainchain (Peg-out) zu verschieben.


**Der Peg-in-Prozess:**

Dies ist erlaubnisfrei. Ein Nutzer sendet BTC an eine von der Föderation kontrollierte Adresse. Zum Schutz vor Bitcoin-Blockchain-Umstrukturierungen müssen diese Gelder **102 Bestätigungen** (ca. 17 Stunden) abwarten, bevor der entsprechende L-BTC auf der Sidechain geprägt wird.


**Der Ausbootungsprozess:**

Um zu Bitcoin zurückzukehren, wird L-BTC verbrannt. Um jedoch den Diebstahl der zugrunde liegenden Bitcoin-Reserven zu verhindern, sind Peg-Outs nicht vollständig automatisiert. Sie erfordern die Genehmigung eines Mitglieds, das einen **Peg-Out Authorization Key (PAK)** besitzt. Die Bitcoin-Fonds selbst sind in einem wallet mit 11 von 15 Multisignaturen gesichert, wobei die Schlüssel in Hardware-Sicherheitsmodulen (HSMs) aufbewahrt werden, die von den Hauptservern der Funktionäre abgekoppelt sind.


**Dynamische Föderation (Dynafed):**

Um die Langlebigkeit zu gewährleisten, verwendet Liquid Dynafed, ein Protokoll, das es dem Netzwerk ermöglicht, Funktionäre auszutauschen oder Parameter zu aktualisieren, ohne dass ein hartes fork erforderlich ist. Wenn ein Funktionär ersetzt werden muss, sendet das Netzwerk eine Übergangstransaktion. Nach einer zweiwöchigen Überlappungszeit wird die neue Konfiguration übernommen, so dass sich der Verbund nahtlos weiterentwickeln kann, während die Betriebszeit kontinuierlich aufrechterhalten wird.


## Ökosystem und Kapitalmärkte


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Geschäftsstrategie und Ökosystem


Liquid ist mehr als eine technische Sidechain; es ist eine geschäftsorientierte Infrastrukturebene, die entwickelt wurde, um die komplexen Anforderungen der Kapitalmärkte zu erfüllen, die Bitcoin und mainchain nicht effizient unterstützen können. Während Lightning Network für Hochfrequenz-Zahlungen mit geringem Wert optimiert ist, zielt Liquid auf Überweisungen mit hohem Wert, die Emission von Vermögenswerten und die Abwicklung zwischen Börsen ab.


Das Ökosystem wird von der **Liquid Federation** vorangetrieben, einem Konsortium von etwa 73 Unternehmen, darunter Börsen, Handelsschalter und Infrastrukturanbieter. Dieses Kooperationsmodell ähnelt den traditionellen Finanzclearinghäusern, arbeitet jedoch mit größerer Transparenz und deutlich kürzeren Abwicklungszeiten (2 Minuten gegenüber T+2 Tagen).


### Die Tokenisierung von Real-World Assets (RWA)


Das Kerngeschäft von Liquid ist die "Tokenisierung" - die Darstellung von realen Werten (Aktien, Anleihen, mining-Verträge) als digitale Token auf der Blockchain. Dies bietet drei Hauptvorteile:

1.  **Globale Märkte rund um die Uhr:** Aufhebung von Banköffnungszeiten und geografischen Beschränkungen.

2.  **Betriebliche Effizienz:** Beseitigung von Abstimmungsfehlern durch ein gemeinsames, unveränderliches Hauptbuch.

3.  **Atomic Settlement:** Verringerung des Kontrahentenrisikos durch Sicherstellung, dass die Lieferung gleichzeitig mit der Zahlung erfolgt.


#### Regulierte Vermögenswerte und AMP

Die meisten institutionellen Vermögenswerte können aufgrund gesetzlicher Bestimmungen nicht erlaubnisfrei gehandelt werden. Die **Asset Management Platform (AMP)** ist der technische Standard, der diese Regeln durchsetzt.


- Whitelisting:** Emittenten können den Besitz und Handel auf KYC-geprüfte Adressen beschränken.
- Multisig-Kontrolle:** Compliance-Aktionen (wie das Einfrieren gestohlener Gelder oder die Neuausgabe verlorener Token) werden über eine Autorisierung mit mehreren Unterschriften verwaltet, so dass kein einzelner Mitarbeiter einseitig handeln kann.


Diese Infrastruktur ist heute in Betrieb. Plattformen wie **Stalker** bieten End-to-End-Tokenisierungsdienste in Europa an, während **Sideswap** als dezentraler Austausch und nicht-pfandrechtlicher wallet fungiert und den Peer-to-Peer-Handel von Vermögenswerten wie der **Blockstream Mining Note (BMN)** und tokenisierten MicroStrategy-Aktien (CMSTR) ermöglicht.


### Erfolg in der realen Welt: Die Mayfell-Fallstudie


Der überzeugendste Beweis für den Nutzen von Liquid kommt von **Mayfell** in Mexiko. In einem Markt, in dem die herkömmliche Finanzierung auf Schuldscheinen aus Papier beruht - die anfällig für Verlust, Betrug und langsame Bearbeitung sind - hat Mayfell die gesamte Infrastruktur auf Liquid umgestellt.



- Umfang:** Über 25.000 ausgestellte Schuldscheine im Wert von **1,5 Mrd. $+**.
- Datenschutz:** Mit dem Confidential Transactions des Liquid sind die Darlehensbeträge nur für den Darlehensgeber und den Darlehensnehmer sichtbar, so dass der Geschäftsgeheimnisschutz gewahrt bleibt, während Auditoren die Integrität des Hauptbuchs überprüfen können.
- Auswirkung:** Durch die Verbindung von Nicht-Bank-Kreditgebern mit globalen Kapitalmärkten über Blockchain hat Mayfell die Kosten gesenkt und den Zugang zu Krediten für mexikanische KMUs erweitert, was zeigt, dass das Wertangebot von Liquid weit über den spekulativen Handel hinausgeht.


### Strategische Positionierung im Vergleich zu anderen Ketten


Liquid konkurriert in einem überfüllten Markt von Tokenisierungsplattformen (Ethereum, Solana, etc.), hat aber deutliche strategische Vorteile:


- Regulatorische Klarheit:** Liquid verwendet Bitcoin (L-BTC) als sein natives Asset. Es gibt kein vorgeminiertes token oder einen ICO, wodurch die Risiken eines "nicht registrierten Wertpapiers" vermieden werden, die andere L1-Blockchains plagen.
- Stabilität:** Im Gegensatz zum Kontomodell von Ethereum, bei dem fehlgeschlagene Transaktionen immer noch Gasgebühren verschlingen, ist das UTXO-Modell deterministisch und zuverlässig für unternehmenskritische Finanzdaten.
- Datenschutz:** Die meisten Finanzinstitute verlangen standardmäßig Vertraulichkeit, eine Funktion, die Liquid von Haus aus bietet und die öffentliche Ketten nur mit Mühe und ohne komplexe Add-ons umsetzen können.


Für Entwickler bietet dieses Ökosystem eine klare Chance: die Entwicklung von Tools (Dashboards, Wallets, Compliance-Integrationen), die eine Brücke zwischen dem traditionellen Finanzwesen und der sicheren Abrechnungsebene von Bitcoin schlagen.


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Erlaubte Asset-Kontrolle auf Liquid


Blockstream AMP (Asset Management Platform) dient als kritische Infrastrukturebene auf dem Liquid Network, die speziell für Emittenten von regulierten digitalen Wertpapieren und Stablecoins entwickelt wurde. Während der Liquid eine genehmigungsfreie Basisschicht mit nativer Asset-Ausgabe bietet, benötigen regulierte Unternehmen oft strenge Aufsichts- und Compliance-Funktionen. AMP überbrückt diese Lücke, indem es eine genehmigungspflichtige Kontrollebene für bestimmte Vermögenswerte einführt, ohne die Datenschutzvorteile des Confidential Transactions des Liquid zu opfern.


Das zentrale Wertversprechen der Plattform beruht auf zwei Hauptfunktionen: umfassende Transparenz für den Emittenten und Transaktionsautorisierung. Im Gegensatz zu Standard-Liquid-Vermögenswerten, bei denen Beträge und Arten für alle außer den Teilnehmern blinded sind, ermöglichen AMP-Vermögenswerte dem Emittenten, einen vollständigen unblinded-Prüfpfad zu führen. Diese Transparenz ist für die aufsichtsrechtliche Berichterstattung und interne Audits unerlässlich. Darüber hinaus setzt AMP durch einen Mitzeichnungsmechanismus ein strenges Autorisierungsmodell durch. Jede Übertragung eines AMP-Vermögenswertes erfordert eine Signatur vom AMP-Server. Dies ermöglicht es Emittenten, komplexe Regeln off-chain durchzusetzen, wie z. B. das Einfrieren von Konten, die Aufnahme von zugelassenen Anlegern in die Whitelist oder die Auferlegung von Transferbeschränkungen, und somit als zentraler Gatekeeper in einem dezentralen Netzwerk zu fungieren.


#### Operative Abwägungen

Diese Architektur ist mit besonderen Kompromissen verbunden. Das System ist von der Verfügbarkeit des AMP-Servers abhängig; wenn der Server als Mitunterzeichner fungiert und offline geht, wird die Liquidität der Vermögenswerte unterbrochen. Während die Privatsphäre der einzelnen Nutzer gewahrt bleibt, müssen die Anleger außerdem akzeptieren, dass der Emittent vollen Einblick in ihre Bestände hat. Dieses Modell ist ideal für konforme Sicherheits-Token, aber ungeeignet für zensurresistente Kryptowährungen.


### Architekturentwicklung und Integrationspfade


Das AMP-Ökosystem wird derzeit von seiner ersten Iteration auf eine flexiblere, interoperable "Version 2"-Architektur umgestellt. Das Altsystem verlangte von den Emittenten, vollständig synchronisierte Elements-Knoten zu unterhalten, und zwang die Entwickler, sich stark auf das monolithische Green-SDK zu verlassen. Dies war zwar funktional, schuf aber hohe technische Zugangsbarrieren und begrenzte wallet-Auswahlmöglichkeiten.


Die Architektur der nächsten Generation vereinfacht diese Anforderungen grundlegend, indem sie die Komplexität auf den Server verlagert. In diesem neuen Modell übernimmt der AMP-Server die schwere Arbeit der Transaktionskonstruktion, der UTXO-Auswahl und der Gebührenberechnung. Er präsentiert dem Emittenten eine teilweise signierte Elements-Transaktion (PSET), die lediglich eine Signatur erfordert. Dieser "Smart Server, Dumb wallet"-Ansatz macht es für Emittenten überflüssig, vollständige Knoten zu betreiben, und ermöglicht die Verwendung von Hardware-Wallets und Standard-Multisignatur-Setups für das Treasury-Management.


Für Entwickler bedeutet diese Entwicklung eine Abkehr von proprietären SDKs hin zu Standarddeskriptoren und PSET-Workflows. Geldbörsen können nun Multisignatur-Deskriptoren beim AMP-Server registrieren, um Autorisierungsrechte festzulegen. Dadurch wird die AMP-Entwicklung an die breiteren Bitcoin-wallet-Standards angeglichen, so dass die Integration für jede Anwendung möglich ist, die PSBT/PSET-Formate verarbeiten kann. Entwickler, die heute entwickeln, werden ermutigt, Tools wie das Liquid Wallet Kit (LWK) zu verwenden, das diese modernen, deskriptorbasierten Architekturen unterstützt und sicherstellt, dass ihre Anwendungen zukunftssicher für die neuen AMP-Standards sind.


### Das Liquid Wallet-Ökosystem und die Vertraulichkeit


Die Entwicklung von Anwendungen auf Liquid erfordert einen komplexeren Stack als die Standard-Bitcoin-Entwicklung aufgrund von Funktionen wie nativen Assets und Confidential Transactions. Das Ökosystem wird durch eine mehrschichtige Architektur unterstützt: Low-Level-Bibliotheken wie "secp256k1-zkp" behandeln kryptografische Primitive, während Toolkits auf höherer Ebene die wallet-Logik verwalten.


In der Vergangenheit bot das Green Development Kit (GDK) eine umfassende, aber starre Lösung. Die moderne Alternative ist das Liquid Wallet Kit (LWK), das einen modularen Ansatz bietet. Das LWK trennt die Belange in verschiedene Kisten auf, die Deskriptoren, Signierung und Hardwarekommunikation unabhängig voneinander handhaben, was den Entwicklern die Flexibilität gibt, kundenspezifische Lösungen ohne den Overhead einer monolithischen Bibliothek zu erstellen.


#### Handhabung Confidential Transactions

Die größte Herausforderung in diesem Ökosystem ist die Verwaltung des Verblendungslebenszyklus. In Liquid werden die Transaktionsausgaben mit dem Elliptic Curve Diffie-Hellman (ECDH) Schlüsselaustausch verschlüsselt. Ein Sender verwendet den öffentlichen Schlüssel des Empfängers, um die Beträge und Arten von Vermögenswerten zu verschlüsseln und einen Reichweitennachweis zu erstellen, der die Gültigkeit der Transaktion verifiziert, ohne Werte preiszugeben.


Damit ein wallet funktionieren kann, muss er diesen Prozess erfolgreich umkehren. Wenn ein wallet eine eingehende Transaktion erkennt, versucht er, die Ausgabe mit seinem privaten Verschlüsselungsschlüssel zu entschlüsseln. Wenn das gemeinsam genutzte Geheimnis übereinstimmt, kann der wallet den Wert entschlüsseln und zum Guthaben des Benutzers hinzufügen. Dieser Prozess ist rechenintensiv und erfordert eine präzise Verwaltung der Verblendungsfaktoren, um sicherzustellen, dass die Transaktionen mathematisch ausgeglichen sind - eine Komplexität, die Tools wie LWK dem Entwickler abnehmen wollen.


# Technisch


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - Knotenlos


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Einführung in Breez Liquid SDK


Das Breez Liquid SDK ist ein selbstverwaltetes Open-Source-Toolkit, das die Lücke zwischen dem Liquid Network und dem breiteren Bitcoin-Ökosystem schließen soll. Seine Hauptaufgabe besteht darin, die Komplexität der Lightning Network-Knotenverwaltung und des Atomtauschs zu abstrahieren, um Entwicklern die Erstellung reibungsloser Finanzanwendungen zu ermöglichen.


Die mit einer "Mobile-first"-Philosophie entwickelte Kernlogik ist aus Leistungs- und Sicherheitsgründen in Rust geschrieben, nutzt aber UniFFI (Unified Foreign Function Interface), um native Bindungen für Kotlin, Swift, Python, C#, Dart und Flutter bereitzustellen. Dadurch wird sichergestellt, dass Entwickler Bitcoin-Funktionen in ihre bevorzugte Umgebung integrieren können, ohne kryptografische Operationen auf niedriger Ebene verwalten zu müssen.


**Unterstützte Transaktionsarten:**

Das SDK arbeitet mit Liquid als "Heimatbasis" Es zeichnet sich durch drei spezifische Operationen aus:

1.  **Liquid-zu-Liquid:** Direkte on-chain-Transfers.

2.  **Liquid-to-Lightning:** Bezahlen von Lightning-Rechnungen mit Liquid-Mitteln.

3.  **Liquid-zu-Bitcoin:** Direktübertragung von Mitteln auf den Bitcoin mainchain.


*Hinweis: Das SDK unterstützt keine direkten Lightning-zu-Lightning- oder Bitcoin-zu-Bitcoin-Transaktionen. Es ist ein rein Liquid-zentriertes Tool


### Zahlungsarchitekturen: Submarine Swaps


Um die Interoperabilität zwischen Liquid, Lightning und Bitcoin ohne zentralisierte Verwahrstellen zu erreichen, stützt sich Breez auf **Submarine Swaps**. Dabei handelt es sich um atomare Operationen, bei denen eine Transaktion entweder in beiden Netzen erfolgreich abgeschlossen wird oder in beiden Netzen fehlschlägt, wodurch sichergestellt wird, dass Gelder während der Übertragung nicht verloren gehen.


#### Lightning Send (U-Boot-Swap)

Wenn ein Nutzer eine Lightning-Rechnung bezahlt, sendet das SDK eine "Lock-up"-Transaktion an das Liquid Network. Dadurch werden die Gelder effektiv auf ein Treuhandkonto gelegt. Der Swap-Anbieter (Boltz) erkennt dies, bezahlt die Lightning-Rechnung und verwendet dann das Zahlungsvorbild (die kryptografische Quittung), um die gesperrten Liquid-Mittel einzufordern.


#### Blitzempfang (Reverse Submarine Swap)

Der Empfang von Lightning ist der umgekehrte Prozess. Der Benutzer erstellt eine Rechnung, und der Swap-Anbieter sperrt Mittel auf dem Lightning Network. Das SDK überwacht diesen Prozess über WebSockets. Sobald die Sperre bestätigt ist, führt das SDK automatisch eine Forderungstransaktion aus, um die entsprechenden Mittel in das Liquid des Benutzers zu übertragen.


#### Kreuz-Kette Bitcoin

Für Liquid-zu-Bitcoin-Übertragungen verwendet die Architektur einen "Dual-Swap"-Mechanismus. Lock-up-Transaktionen finden auf beiden Ketten gleichzeitig statt. Der Absender fordert Gelder auf Bitcoin an, während der Empfänger Gelder auf Liquid anfordert. Dies ermöglicht eine vertrauenswürdige Überbrückung ohne federated peg-Ausgänge oder zentralisierte Austauschvorgänge.


### Entwickler Interface und automatisierte Verwaltung


Das Breez SDK vereinfacht die Arbeit der Entwickler, indem es komplexe Finanzströme in einem standardisierten Drei-Schritte-Prozess zusammenfasst: **Verbinden, Vorbereiten und Ausführen**.


1.  **Connect:** Initialisiert den wallet, synchronisiert sich mit der Blockchain über das Liquid Wallet Kit (LWK) und baut WebSocket-Verbindungen für die Echtzeitüberwachung auf.

2.  **Vorbereiten:** Vor der Mittelbindung werden in diesem Schritt alle damit verbundenen Netzwerkgebühren und Swap-Kosten berechnet und zurückgegeben, so dass die Benutzeroberfläche dem Benutzer eine klare Gesamtsumme präsentiert.

3.  **Ausführen:** In diesem Schritt wird die Transaktion erstellt, übertragen und der Swap eingeleitet.


#### Automatisierte Sicherheitsmechanismen

Eine der wichtigsten Funktionen des SDK ist das **Automatische Erstattungsmanagement**. Im Falle eines Netzwerkausfalls oder einer nicht kooperativen Gegenpartei könnten Gelder theoretisch in einem zeitlich gesperrten Vertrag stecken bleiben. Das SDK abstrahiert die Rückzahlungslogik vollständig. Es überwacht den Status jedes Swaps; wenn ein Swap fehlschlägt oder eine Zeitüberschreitung eintritt, erstellt das SDK automatisch die Rückzahlungstransaktion und sendet sie an das wallet des Nutzers.


Außerdem übernimmt das SDK die **Metadatenauflösung**. Es führt off-chain-Swap-Daten (die vom Boltz-Swapper bereitgestellt werden) mit dem on-chain-Transaktionsverlauf zusammen. Dadurch wird sichergestellt, dass der Transaktionsverlauf des Benutzers für den Menschen lesbar ist und Rechnungsdetails und den Zahlungskontext anzeigt und nicht nur rohe hexadezimale Transaktionshashes.


# Letzter Abschnitt


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Rezensionen und Bewertungen


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Abschlussprüfung


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Schlussfolgerung


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>