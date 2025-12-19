---
name: RGB-Programmierung
goal: Erwerbe die notwendigen Fähigkeiten, um RGB zu verstehen und zu verwenden
objectives:
- Verstehe die grundlegenden Konzepte des RGB-Protokolls
- Beherrsche die Grundsätze der client-side Validierung und der Bitcoin commitments
- Erfahre, wie du RGB-Verträge erstellen, verwalten und übertragen kannst
- Wie man eine RGB-kompatible Lightning-Node betreibt
---
# Entdecke das RGB-Protokoll
Tauche ein in die Welt von RGB, einem Protokoll zur Implementierung und Durchsetzung digitaler Rechte in Form von Verträgen und Vermögenswerten, basierend auf den Konsensregeln und Operationen der Bitcoin-[Blockchain](https://planb.academy/resources/glossary/blockchain). Dieser umfassende Schulungskurs führt dich durch die technischen und praktischen Grundlagen von RGB, von den Konzepten der [client-side Validation (client-side Validierung)](https://planb.academy/resources/glossary/client-side-validation) und [Single-use Seals](https://planb.academy/resources/glossary/single-use-seal) bis hin zur Implementierung von fortgeschrittenen [Smart Contracts](https://planb.academy/resources/glossary/smart-contract).

Durch ein strukturiertes, schrittweises Programm wirst du die Mechanismen der client-side Validierung, deterministische commitments auf Bitcoin und Interaktionsmuster zwischen Nutzern entdecken. Lerne, wie du RGB-Token auf Bitcoin oder dem [Lightning Network (Lightning Netzwerk)](https://planb.academy/resources/glossary/lightning-network) erstellen, verwalten und übertragen kannst.

Egal, ob du Entwickler, Bitcoin-Enthusiast oder einfach nur neugierig darauf bist, mehr über diese Technologie zu erfahren, dieser Kurs wird dir die Werkzeuge und das Wissen vermitteln, das du benötigst, um RGB zu beherrschen und innovative Lösungen auf Bitcoin zu entwickeln.

Der Kurs basiert auf einem von [Fulgur'Ventures](https://fulgur.ventures/) organisierten Live-Seminar, das von drei renommierten Lehrern und RGB-Experten geleitet wird.

+++
# Einführung

<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>

## Präsentation des Kurses

<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>

Hallo und herzlich willkommen zu diesem Schulungskurs über RGB, einem client-side validiertem Smart-Contract-System, das auf Bitcoin und dem Lightning Netzwerk läuft. Der Aufbau dieses Kurses ist so konzipiert, dass er eine eingehende Einarbeitung in dieses komplexe Thema ermöglicht. Der Kurs ist folgendermaßen aufgebaut:

**Abschnitt 1: Theorie**

Der erste Abschnitt ist den theoretischen Konzepten gewidmet, die notwendig sind, um die Grundlagen der client-side Validierung und von RGB zu verstehen. Wie du in diesem Kurs entdecken wirst, führt RGB eine Vielzahl von technischen Konzepten ein, die normalerweise nicht in Bitcoin vorkommen. In diesem Abschnitt findest du auch ein Glossar mit Definitionen für alle Begriffe, die das RGB-Protokoll betreffen.

**Abschnitt 2: Praxis**

Der zweite Abschnitt konzentriert sich auf die Anwendung der theoretischen Konzepte aus Abschnitt 1. Wir lernen, wie man RGB-Verträge erstellt und manipuliert. Wir werden auch sehen, wie man mit diesen Werkzeugen programmiert. Diese ersten beiden Abschnitte werden von Maxim Orlovsky präsentiert.

**Abschnitt 3: Anwendungen**

Der letzte Abschnitt wird von anderen Referenten geleitet, die konkrete RGB-basierte Anwendungen vorstellen, um reale Anwendungsfälle zu beleuchten.

---
Dieser Schulungskurs entstand ursprünglich aus einem zweiwöchigen Bootcamp für fortgeschrittene Entwickler in Viareggio, Toskana, organisiert von [Fulgur'Ventures](https://fulgur.ventures/). Die erste Woche, die sich auf Rust und SDKs konzentrierte, kann in diesem anderen Kurs nachgelesen werden:

https://planb.academy/courses/9fbd8b57-f278-4304-8d88-a2d384eaff58

In diesem Kurs konzentrieren wir uns auf die zweite Woche des Bootcamps, in der es um RGB geht.

**Woche 1 - LNP402:**

![RGB-Bitcoin](assets/en/001.webp)

**Woche 2 - CSV402 (dieses Training):**

![RGB-Bitcoin](assets/en/002.webp)

Vielen Dank an die Organisatoren dieser Live-Kurse und an die 3 Lehrer, die daran teilgenommen haben:


- Maxim Orlovsky: *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, KI, Robotik, Transhumanismus. Schöpfer von RGB, Prime, Radiant und lnp_bp, mycitadel_io & cyphernet_io*;
- Hunter Trujilo: *Entwickler, Rust, Bitcoin, Lightning, RGB* ;
- Federico Tenga: *Ich trage meinen Teil dazu bei, die Welt in eine Cypherpunk-Dystopie zu verwandeln. Derzeit arbeite ich an RGB bei Bitfinex*.

Die schriftliche Fassung dieses Schulungskurses wurde unter Verwendung von 2 Hauptquellen erstellt:


- Videos des Seminars von Maxim Orlovsky, Hunter Trujilo und Frederico Tenga beim Lightning Bootcamp;
- Die RGB-Dokumentation, deren Erstellung von [Bitfinex](https://www.bitfinex.com/) gesponsert wurde.

Bereit, in die komplexe und faszinierende Welt von RGB einzutauchen? Los geht's!

# RGB in der Theorie

<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## Einführung in Konzepte der verteilten Datenverarbeitung

<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

:::video id=f27338bc-4210-4a2e-9b27-30278ed3282c:::

RGB ist ein Protokoll zur Anwendung und Durchsetzung digitaler Rechte (in Form von Verträgen und Vermögenswerten) auf skalierbare und vertrauliche Weise, basierend auf den Konsensregeln und Operationen der Bitcoin-Blockchain. Ziel dieses ersten Kapitels ist es, die grundlegenden Konzepte und die Terminologie rund um das RGB-Protokoll vorzustellen, wobei insbesondere seine enge Verbindung zu grundlegenden Konzepten des [distributed](https://planb.academy/resources/glossary/distributed) Computings (verteilted Rechnen) wie z.B. der client-side Validierung und der Single-use Seals hervorgehoben wird.

In diesem Kapitel untersuchen wir die Grundlagen von **verteilten Konsenssystemen** und sehen, wie RGB in diese Familie von Technologien passt. Wir werden auch die Hauptprinzipien vorstellen, die uns helfen zu verstehen, warum RGB darauf abzielt, erweiterbar und unabhängig von Bitcoins eigenem Konsensmechanismus zu sein, während es sich bei Bedarf auf diesen stützt.

### Einführung

Distributed Computing, ein spezieller Zweig der Informatik, befasst sich mit den Protokollen, die für die Weitergabe und Verarbeitung von Informationen in einem Netz von Knotenpunkten verwendet werden. Diese Knoten und die Protokollregeln bilden zusammen ein so genanntes verteiltes System. Zu den wesentlichen Eigenschaften, die ein solches System kennzeichnen, gehören:


- Die **Fähigkeit zur unabhängigen Überprüfung und Validierung** bestimmter Daten durch jeden Knoten;
- Die Möglichkeit für die Knoten, (je nach Protokoll) eine vollständige oder teilweise Sicht auf die Informationen zu erstellen. Diese Ansichten sind die **Zustände** des verteilten Systems;
- Die **chronologische Reihenfolge** der Vorgänge, damit die Daten zuverlässig mit einem Zeitstempel versehen werden und ein Konsens über die Abfolge der Ereignisse (Abfolge der Zustände) besteht.

Der Begriff des **Konsenses** in einem verteilten System umfasst insbesondere zwei Aspekte:


- Erkennung der **Gültigkeit** von Zustandsänderungen (gemäß den Protokollregeln);
- Die **Übereinkunft über die Reihenfolge** dieser Zustandsänderungen, die es unmöglich macht, validierte Operationen im Nachhinein umzuschreiben oder rückgängig zu machen (dies ist in Bitcoin auch als "double-spend protection" (Schutz vor Doppelausgaben) bekannt).

Die erste funktionierende, erlaubnisfreie Implementierung eines verteilten Konsensmechanismus wurde von Satoshi Nakamoto mit Bitcoin eingeführt, dank der kombinierten Verwendung einer Blockchain-Datenstruktur und eines [Proof-of-Work](https://planb.academy/resources/glossary/proof-of-work)-Algorithmus (PoW). In diesem System hängt die Glaubwürdigkeit der Block-Historie von der Rechenleistung ab, die von den Knoten (Minern) aufgebracht wird. Bitcoin ist daher ein wichtiges und historisches Beispiel für ein verteiltes Konsenssystem, das allen offensteht (*erlaubnisfrei*).

In der Welt der Blockchain und des distributed Computings können wir zwei grundlegende Paradigmen unterscheiden: ***Blockchain*** im traditionellen Sinne und ***State Channels***, deren bestes Beispiel in der Praxis das Lightning Netzwerk ist. Die Blockchain ist definiert als ein Register chronologisch geordneter Ereignisse, das durch Konsens innerhalb eines offenen, erlaubnisfreien Netzwerks repliziert wird. State Channels hingegen sind Peer-to-Peer-Kanäle, die es zwei (oder mehr) Teilnehmern ermöglichen, einen aktualisierten Status außerhalb der Blockchain aufrechtzuerhalten, wobei die Blockchain nur beim Öffnen und Schließen dieser Kanäle verwendet wird.

Im Zusammenhang mit Bitcoin bist du zweifellos mit den Prinzipien des Mining, der Dezentralisierung und der Endgültigkeit von Transaktionen auf der Blockchain sowie der Funktionsweise von Zahlungskanälen vertraut. Mit RGB führen wir ein neues Paradigma namens **client-side Validierung** ein, das im Gegensatz zu Blockchain oder Lightning darin besteht, die Zustandsübergänge eines Smart Contracts lokal (client-side) zu speichern und zu validieren. Dies unterscheidet sich auch von anderen "DeFi"-Techniken (_rollups_, _plasma_, _ARK_, etc.), da sich die client-side Validierung auf die Blockchain stützt, um Doppelausgaben zu verhindern und ein Zeitstempelsystem zu haben, während das Register der Off-Chain-Zustände und -Übergänge nur bei den betroffenen Teilnehmern verbleibt.

![RGB-Bitcoin](assets/en/003.webp)

Später werden wir auch einen wichtigen Begriff einführen: den Begriff "**stash**", der sich auf die Menge der client-side Daten bezieht, die erforderlich sind, um den Zustand eines Vertrags aufrechtzuerhalten, da diese Daten nicht global über das Netzwerk repliziert werden. Schließlich werden wir uns die Beweggründe für RGB ansehen, ein Protokoll, das die Vorteile der client-side Validierung nutzt, und warum es die bestehenden Ansätze (Blockchain und State Channels) ergänzt.

### Trilemmas im distributed Computing

Um zu verstehen, wie client-side Validierung und RGB Probleme angehen, die von Blockchain und Lightning nicht gelöst werden, sollten wir uns die 3 wichtigsten "Trilemmas" im verteilten Computing anschauen:


- **Skalierbarkeit, Dezentralisierung, Datenschutz**;
- **CAP-Theorem** (Consistency (Konsistenz), Availability (Verfügbarkeit), Partition Tolerance (Partitionstoleranz));
- **CIA-Trilemma** (Confideniality (Vertraulichkeit), Integrity (Integrität), Availability (Verfügbarkeit)).

#### 1. Skalierbarkeit, Dezentralisierung und Vertraulichkeit


- **Blockchain (Bitcoin)**

Die Blockchain ist stark dezentralisiert, aber nicht sehr skalierbar. Außerdem ist die Vertraulichkeit begrenzt, da sich alles in einem globalen, öffentlichen Register befindet. Wir können versuchen, die Vertraulichkeit mit [Zero-Knowledge](https://planb.academy/resources/glossary/zkp-zeroknowledge-proof)-Technologien (vertrauliche Transaktionen, Mimblewimble-Verfahren usw.) zu verbessern, aber die öffentliche Blockchain kann den Transaktionsgraphen nicht verbergen.


- **Lightning/State channels**

State Channels (wie das Lightning Network) sind skalierbarer und privater als Blockchain, da die Transaktionen außerhalb der Kette stattfinden. Allerdings können die Verpflichtung zur öffentlichen Bekanntgabe bestimmter Elemente (funding Transaktion, Netzwerktopologie) und die Überwachung des Netzverkehrs die Vertraulichkeit teilweise beeinträchtigen. Auch die Dezentralisierung leidet: Routing ist geldintensiv, und große Knotenpunkte können zu Zentralisierungspunkten werden. Dies ist genau das Phänomen, das wir bei Lightning zu beobachten beginnen.


- Client-side Validierung **(RGB)**

Dieses neue Paradigma ist sogar noch skalierbarer und vertraulicher, denn wir können nicht nur Zero-Disclosure-Proof-of-Knowledge-Techniken integrieren, sondern es gibt auch keinen globalen Graphen der Transaktionen, da niemand das gesamte Register besitzt. Andererseits bedeutet dies auch einen gewissen Kompromiss in Bezug auf die Dezentralisierung: Der Emittent eines Smart Contracts kann eine zentrale Rolle einnehmen (wie ein "Contract Deployer" in Ethereum). Im Gegensatz zur Blockchain speichert und validiert bei der client-side Validierung jedoch jeder nur die Verträge, die für ihn selber von Interesse sind, was die Skalierbarkeit verbessert, da nicht alle bestehenden Zustände heruntergeladen und überprüft werden müssen.

![RGB-Bitcoin](assets/en/004.webp)

#### 2. CAP-Theorem (Konsistenz, Verfügbarkeit, Partitionstoleranz)

Das CAP-Theorem besagt, dass es für ein verteiltes System unmöglich ist, gleichzeitig Konsistenz (*Consistency*), Verfügbarkeit (*Availability*) und Partitionstoleranz (*Partition tolerance*) zu erfüllen.


- **Blockchain**

Die Blockchain begünstigt Konsistenz und Verfügbarkeit, kommt aber mit einer Partitionierung des Netzwerks nicht gut zurecht: Wenn man einen Block nicht sehen kann, kann man nicht handeln und dieselbe Sicht wie das gesamte Netzwerk haben.


- **Lightning**

Ein System von Zustandskanälen hat Verfügbarkeits- und Partitionierungstoleranz (da zwei Knoten miteinander verbunden bleiben können, auch wenn das Netzwerk fragmentiert ist), aber die Gesamtkonsistenz hängt vom Öffnen und Schließen der Kanäle auf der Blockchain ab.


- Client-side Validierung **(RGB)**

Ein System wie RGB bietet Konsistenz (jeder Teilnehmer validiert seine Daten lokal, ohne Mehrdeutigkeit) und Partitionierungstoleranz (du bewahrst deine Daten autonom auf), garantiert aber keine globale Verfügbarkeit (jeder muss sich vergewissern, dass er die relevanten Teile der Geschichte hat, und einige Teilnehmer veröffentlichen möglicherweise nichts oder stellen den Austausch bestimmter Informationen ein).

![RGB-Bitcoin](assets/en/005.webp)

#### 3. CIA-Trilemma (Vertraulichkeit, Integrität, Verfügbarkeit)

Dieses Trilemma erinnert uns daran, dass Vertraulichkeit, Integrität und Verfügbarkeit nicht alle gleichzeitig optimiert werden können. Blockchain, Lightning und client-side Validierung fallen unterschiedlich in dieses Gleichgewicht. Die Idee ist, dass kein einzelnes System alles bieten kann; es ist notwendig, mehrere Ansätze zu kombinieren (Blockchain-Zeitstempel, synchroner Ansatz von Lightning und lokale Validierung mit RGB), um ein kohärentes Paket zu erhalten, das gute Garantien in jeder Dimension bietet.

![RGB-Bitcoin](assets/en/006.webp)

### Die Rolle der Blockchain und das Konzept des Sharding

Die Blockchain (in diesem Fall Bitcoin) dient in erster Linie als _Zeitstempel-Mechanismus_ und als Schutz vor Doppelausgaben. Anstatt die kompletten Daten eines Smart Contracts oder eines dezentralen Systems einzufügen, fügen wir einfach **kryptografische Verpflichtungen** (_commitments_) in Transaktionen ein (im Sinne der client-side Validierung, die wir "Zustandsübergänge" nennen). Also:


- Wir ersparen der Blockchain eine große Menge an Daten und Logik;
- Jeder Benutzer speichert nur die für seinen eigenen Teil des Vertrags (seine "*Shard*" (Bruchstück/Scherbe)) erforderliche Historie, anstatt den globalen Zustand zu replizieren.

Sharding ist ein Konzept, das seinen Ursprung in verteilten Datenbanken hat (z.B. MySQL für soziale Netzwerke wie Facebook oder Twitter). Um das Problem des Datenvolumens und der Synchronisationslatenzen zu lösen, wird die Datenbank in _Shards_ (Bruchstücke/Scherben, z.B. USA, Europa, Asien usw.) unterteilt. Jedes Segment ist lokal konsistent und wird nur teilweise mit den anderen synchronisiert.

Bei RGB-Smart Contracts wird die Aufteilung anhand der Verträge selbst vorgenommen. Jeder Vertrag ist ein unabhängiger _Shard_. Wenn du zum Beispiel nur USDT-Token hältst, musst du nicht die gesamte Historie eines anderen Tokens wie z.B. USDC speichern oder validieren. Bei Bitcoin gibt es in der Blockchain kein _sharding_: es gibt einen globalen Satz von UTXOs. Bei der client-side Validierung behält jeder Teilnehmer nur die Vertragsdaten, die er besitzt oder verwendet.

Wir können uns das Ökosystem also wie folgt vorstellen:


- Die **Blockchain (Bitcoin)** als Grundlage, die eine vollständige Replikation eines minimalen Registers gewährleistet und als Zeitstempelschicht dient;
- Das **Lightning Netwerk** für schnelle, vertrauliche Transaktionen, die immer noch auf der Sicherheit und dem endgültigen Settlement der Bitcoin-Blockchain basieren;
- **RGB und client-side Validation**, um komplexere Smart-Contract-Logik hinzuzufügen, ohne die Blockchain zu überladen oder die Vertraulichkeit zu verlieren.

![RGB-Bitcoin](assets/en/007.webp)

Diese drei Elemente bilden eine dreifaltiges Ganzes anstelle eines linearen Stapels aus "Schicht 2", "Schicht 3" und so weiter. Lightning kann sich direkt mit Bitcoin verbinden oder mit Bitcoin-Transaktionen, die RGB-Daten enthalten, verknüpft werden. In ähnlicher Weise kann eine "BiFi"-Anwendung (Finanz-Anwendung auf Bitcoin) je nach Bedarf an Vertraulichkeit, Skalierbarkeit oder Vertragslogik mit der Blockchain, mit Lightning und mit RGB arbeiten.

![RGB-Bitcoin](assets/en/008.webp)

### Der Begriff der Zustandsübergänge

In jedem verteilten System besteht das Ziel des Validierungsmechanismus darin, die **Gültigkeit und zeitliche Abfolge von Zustandsänderungen** bestimmen zu können. Es soll überprüft werden, ob die Protokollregeln eingehalten wurden, und es soll nachgewiesen werden, dass diese Zustandsänderungen in einer definitiven, unanfechtbaren Reihenfolge aufeinander folgen.

Um zu verstehen, wie diese Validierung im Kontext von **Bitcoin** funktioniert und, allgemeiner, um die Philosophie hinter der client-side Validierung zu verstehen, lass uns zunächst einen Blick zurück auf die Mechanismen der Bitcoin-Blockchain werfen, bevor wir sehen, wie sich die client-side Validierung von ihnen unterscheidet und welche Optimierungen sie möglich macht.

![RGB-Bitcoin](assets/en/009.webp)

Im Fall der Bitcoin-Blockchain basiert die Validierung von Transaktionen auf einer einfachen Regel:


- Alle Netzwerkknoten laden jeden Block und jede Transaktion herunter;
- Sie validieren diese Transaktionen, um die korrekte Entwicklung des [UTXO-Sets](https://planb.academy/resources/glossary/utxo-set) (alle nicht ausgegebenen Outputs) zu überprüfen;
- Sie speichern diese Daten (in Form von Blöcken), so dass der Verlauf bei Bedarf wiedergegeben werden kann.

![RGB-Bitcoin](assets/en/010.webp)

Dieses Modell hat jedoch zwei große Nachteile:


- **Skalierbarkeit**: Da jeder Knoten alle Transaktionen verarbeiten, verifizieren und archivieren muss, gibt es eine offensichtliche Begrenzung der Transaktionskapazität, die insbesondere mit der maximalen Blockgröße zusammenhängt (bei Bitcoin im Durchschnitt 1 MB innerhalb von 10 Minuten, ohne Cookies);
- **Datenschutz**: Alles wird öffentlich übertragen und gespeichert (Beträge, Zieladressen usw.), wodurch die Vertraulichkeit des Austauschs eingeschränkt wird.

![RGB-Bitcoin](assets/en/012.webp)

In der Praxis funktioniert dieses Modell für Bitcoin als Basisschicht (Layer 1), kann aber für komplexere Anwendungen, die gleichzeitig einen hohen Transaktionsdurchsatz und ein gewisses Maß an Vertraulichkeit erfordern, unzureichend sein.

Die client-side Validierung basiert auf der entgegengesetzten Idee: Anstatt das gesamte Netzwerk zu verpflichten, alle Transaktionen zu validieren und zu speichern, validiert jeder Teilnehmer (Client) nur den Teil der Historie, der ihn betrifft:


- Wenn eine Person einen Vermögenswert (oder ein anderes digitales Gut) erhält, muss sie nur die Kette der Vorgänge (Zustandsübergänge) kennen und überprüfen, die zu diesem Vermögenswert führen, und deren Legitimität nachweisen;
- Diese Abfolge von Vorgängen, von der ***Genesis*** (Erstausgabe) bis zur jüngsten Transaktion, bildet einen [azyklischen gerichteten Graphen](https://planb.academy/resources/glossary/directed-acyclic-graph) (DAG) oder _Shard_, d.h. einen Teil der gesamten Historie.

![RGB-Bitcoin](assets/en/013.webp)

Damit der Rest des Netzwerks (oder genauer gesagt die darunter liegende Schicht, wie z. B. Bitcoin) den endgültigen Zustand festhalten kann, ohne die Details dieser Daten zu sehen, beruht die client-side Validierung auf dem Konzept des ***Commitments*** (Zusage/Verpflichtung).

Ein *Commitment* ist eine kryptographische Zusage/Verpflichtung, typischerweise ein [_Hash_](https://planb.academy/resources/glossary/hash-function) (z.B. SHA-256), die in eine Bitcoin-Transaktion eingefügt wird und die beweist, dass private Daten enthalten sind, ohne diese Daten zu offenbaren.

Dank dieser _Commitments_ können wir beweisen:


- Das Vorhandensein von Informationen (da sie gegen den veröffentlichten Hash prüfbar sind);
- Die zeitliche Vorrangigkeit dieser Informationen (da sie in der Blockchain verankert und mit einem Zeitstempel versehen sind, mit Datum und Blockreihenfolge).

Der genaue Inhalt wird jedoch nicht bekannt gegeben, so dass die Vertraulichkeit gewahrt bleibt.

Konkret funktioniert ein RGB-Zustandsübergang folgendermaßen:


- Man bereitet einen neuen Zustandsübergang vor (z. B. die Übertragung eines RGB-Tokens);
- Man erzeugt ein kryptografisches Commitment für diesen Übergang und fügt es in eine Bitcoin-Transaktion ein (diese Commitments werden im RGB-Protokoll "*Anker*" genannt);
- Die Gegenpartei (der Empfänger) ruft die mit diesem Vermögenswert verbundene client-side Historie ab und validiert die durchgängige Konsistenz, von der Entstehung des Smart Contracts bis zum Übergang, den man ihr übermittelt.

![RGB-Bitcoin](assets/en/014.webp)

Die client-side Validierung bietet zwei wesentliche Vorteile:


- **Skalierbarkeit:**

Die in der Blockchain enthaltenen *Commitments* sind klein (in der Größenordnung von einigen Dutzend Bytes). Dadurch wird sichergestellt, dass der Blocks-Space nicht überfüllt ist, da nur der Hash enthalten sein muss. Dies ermöglicht auch die Weiterentwicklung des Off-Chain-Protokolls, da jeder Nutzer nur sein eigenes History-Fragment (seinen _stash_) speichern muss.


- **Datenschutz:**

Die Transaktionen selbst (d.h. ihr detaillierter Inhalt) werden nicht auf der Blockchain veröffentlicht. Nur ihre Fingerabdrücke (*Hash*) werden veröffentlicht. Beträge, Adressen und Vertragslogik bleiben also privat, und der Empfänger kann die Gültigkeit seines *Shards* lokal überprüfen, indem er alle früheren Zustandsübergänge untersucht. Es gibt keinen Grund für den Empfänger, diese Daten zu veröffentlichen, außer im Falle eines Disputs oder wenn ein Beweis erforderlich ist.

In einem System wie RGB können mehrere Zustandsübergänge von verschiedenen Verträgen (oder verschiedenen Vermögenswerten) in einer einzigen Bitcoin-Transaktion über ein einziges _Commitment_ zusammengefasst werden. Dieser Mechanismus stellt eine deterministische, mit einem Zeitstempel versehene Verbindung zwischen der On-Chain-Transaktion und den Off-Chain-Daten (den client-side validierten Zustandsübergängen) her und ermöglicht die gleichzeitige Aktualisierung mehrerer Shards in einem einzigen Ankerpunkt, wodurch On-Chain-Kosten und -Footprint weiter reduziert werden.

In der Praxis wird mit der Validierung dieser Bitcoin-Transaktion der Zustand der zugrunde liegenden Verträge dauerhaft "verriegelt", da es unmöglich wird, den bereits in die Blockchain eingetragenen Hash zu ändern.

![RGB-Bitcoin](assets/en/015.webp)

### Das Stash-Konzept

Ein **Stash** ist die Menge an client-side Daten, die ein Teilnehmer unbedingt aufbewahren muss, um die Integrität und die Historie eines RGB-Smart Contracts aufrechtzuerhalten. Im Gegensatz zu einem Lightning-Kanal, bei dem bestimmte Zustände lokal aus gemeinsam genutzten Informationen rekonstruiert werden können, wird der Stash eines RGB-Kontrakts nirgendwo anders repliziert: Wenn du ihn verlierst, kann ihn niemand für dich wiederherstellen, da du für deinen Anteil an der Historie verantwortlich bist. Aus diesem Grund musst du in RGB ein System mit zuverlässigen Sicherungsverfahren verwenden.

![RGB-Bitcoin](assets/en/016.webp)

### Single-use Seals: Entstehung und Funktionsweise

Bei der Annahme eines Vermögenswerts wie einer Währung sind zwei Garantien unerlässlich:


- Die Echtheit des erhaltenen Artikels;
- Die Einzigartigkeit des erhaltenen Artikels, um doppelte Ausgaben zu vermeiden..

Bei physischen Vermögenswerten, wie z. B. einer Banknote, reicht die physische Präsenz aus, um zu beweisen, dass sie nicht dupliziert wurde. In der digitalen Welt, in der es sich um reine Informationswerte handelt, ist diese Überprüfung jedoch komplexer, da Informationen leicht vermehrt und dupliziert werden können.

Wie wir bereits gesehen haben, können wir durch die Offenlegung der Historie der Zustandsübergänge durch den Absender die Authentizität eines RGB-Tokens sicherstellen. Da wir Zugang zu allen Transaktionen seit der Ursprungstransaktion haben, können wir die Echtheit des Tokens bestätigen. Dieses Prinzip ähnelt dem von Bitcoin, wo die Historie der Münzen bis zur ursprünglichen Coinbase-Transaktion zurückverfolgt werden kann, um ihre Gültigkeit zu überprüfen. Im Gegensatz zu Bitcoin ist diese Historie der Zustandsübergänge bei RGB jedoch privat und wird auf der client-side aufbewahrt.

Um die doppelte Ausgabe von RGB-Tokens zu verhindern, verwenden wir einen Mechanismus namens "**Single-use Seals**" (einmalige Siegel). Dieses System stellt sicher, dass jeder Token, der einmal verwendet wurde, nicht in betrügerischer Absicht ein zweites Mal verwendet werden kann.

Single-use Seals sind kryptografische Primitive, die 2016 von Peter Todd vorgeschlagen wurden und dem Konzept physischer Siegel ähneln: Sobald ein Siegel auf einem Behälter angebracht wurde, ist es unmöglich, ihn zu öffnen oder zu verändern, ohne das Siegel unwiderruflich zu brechen.

![RGB-Bitcoin](assets/en/018.webp)

Mit diesem auf die digitale Welt übertragenen Ansatz lässt sich nachweisen, dass eine Abfolge von Ereignissen tatsächlich stattgefunden hat und dass sie im Nachhinein nicht mehr geändert werden kann. Single-use Seals gehen somit über die einfache Logik von "Hash + Zeitstempel" hinaus und fügen den Begriff eines Siegels hinzu, das **nur einmal** geschlossen werden kann.

![RGB-Bitcoin](assets/en/017.webp)

Damit Single-use Seals funktionieren, braucht man ein Medium, das die Existenz oder Abwesenheit einer Veröffentlichung nachweisen kann und das schwer (wenn nicht gar unmöglich) zu fälschen ist, sobald die Information verbreitet wurde. Eine **Blockchain** (wie Bitcoin) kann diese Aufgabe erfüllen, ebenso wie beispielsweise eine Papierzeitung mit öffentlicher Auflage. Die Idee ist die folgende:


- Wir wollen beweisen, dass ein bestimmtes Commitment `h(m)` zu einer Nachricht `m` an ein Publikum veröffentlicht wurde, ohne den Inhalt der Nachricht `m` preiszugeben;
- Wir wollen beweisen, dass kein anderes konkurrierende `h(m')` Nachrichten-Commitment anstelle von `h(m)` veröffentlicht worden ist;
- Wir wollen auch prüfen können, ob die Nachricht `m` vor einem bestimmten Datum existiert.

Eine Blockchain eignet sich ideal für diese Rolle: Sobald eine Transaktion in einen Block aufgenommen wird, verfügt das gesamte Netzwerk über denselben nicht falsifizierbaren Beweis für ihre Existenz und ihren Inhalt (zumindest teilweise, da das _Commitment_ die Details verbergen kann, während es die Authentizität der Nachricht beweist).

Ein Single-use Seal kann daher als formales Commitment gesehen werden, eine (zu diesem Zeitpunkt noch unbekannte) Nachricht einmal und nur einmal zu veröffentlichen, und zwar in einer Weise, die von allen interessierten Parteien überprüft werden kann.

Im Gegensatz zu einfachen _Commitments_ (Hash) oder Zeitstempeln, die ein Existenzdatum bescheinigen, bietet ein Single-use Seal die zusätzliche Garantie, dass **kein alternatives Commitment** koexistieren kann: Man kann dasselbe Siegel nicht zweimal schließen oder versuchen, die versiegelte Nachricht zu ersetzen.

Der folgende Vergleich hilft, dieses Prinzip zu verstehen:


- **Kryptografisches Commitment (Hash)**: Mit einer Hash-Funktion kann man sich auf ein Datenelement (eine Zahl) festlegen, indem man den Hash-Wert veröffentlicht. Die Daten bleiben geheim, bis man das Vorabbild offenlegt, aber man kann beweisen, dass man sie im Voraus kannt;
- **Zeitstempel (Blockchain)**: Indem man diesen Hash in die Blockchain einfügt, beweist man auch, dass man ihn zu einem bestimmten Zeitpunkt kannt (dem Zeitpunkt der Aufnahme in einen Block);
- **Single-use Seal**: Bei Single-use Seals geht man noch einen Schritt weiter, indem man die Zusage eindeutig macht. Mit einem einzigen Hash kann man mehrere widersprüchliche Zusagen parallel erstellen (das Problem des Arztes, der der Familie verkündet "*Es ist ein Junge*" und in seinem persönlichen Tagebuch "*Es ist ein Mädchen*"). Das Single-use Seal schließt diese Möglichkeit aus, indem es das Commitment mit einem Medium zum Nachweis der Veröffentlichung, wie der Bitcoin-Blockchain, verbindet, so dass das Ausgeben eines UTXO das Commitment endgültig besiegelt. Einmal ausgegebene UTXO können nicht erneut ausgegeben werden, um das Commitment zu ersetzen.

|                                                                                  | Einfaches Commitment (Digest/Hash) | Zeitstempel | Single-use Seal |
| -------------------------------------------------------------------------------- | ---------------------------------- | ----------- | ---------------- |
| Die Veröffentlichung des Commitments offenbart nicht die Nachricht               | Ja                                | Ja          | Ja              |
| Nachweis des Commitment-Datums / Existenz der Nachricht vor einem bestimmten Datum | Unmöglich                         | Möglich     | Möglich         |
| Nachweis, dass kein alternatives Commitment existieren kann                      | Unmöglich                         | Unmöglich   | Möglich         |

Siegel für den einmaligen Gebrauch funktionieren in drei Hauptphasen:

**Siegel Definition :**


- Alice legt im Voraus die Regeln für die Veröffentlichung des Siegels fest (wann, wo und wie die Nachricht veröffentlicht werden soll);
- Bob akzeptiert diese Bedingungen oder erkennt sie an.

![RGB-Bitcoin](assets/en/021.webp)

**Siegelverschluss:**


- Zur Laufzeit schließt Alice das Siegel, indem sie die eigentliche Nachricht veröffentlicht (normalerweise in Form eines _commitment_, z. B. eines Hash);
- Sie liefert auch einen **Zeugen** (kryptographischer Beweis), der beweist, dass das Siegel geschlossen und unwiderruflich ist.

![RGB-Bitcoin](assets/en/019.webp)

**Versiegelungsüberprüfung:**


- Sobald das Siegel verschlossen ist, kann Bob es nicht mehr öffnen: Er kann nur noch überprüfen, ob es verschlossen ist;
- Bob sammelt das Siegel, den **Zeugen** und die Nachricht (oder seine Zusage), um sicherzustellen, dass alles übereinstimmt und dass es keine konkurrierenden Siegel oder unterschiedliche Versionen gibt.

Der Prozess lässt sich wie folgt zusammenfassen:

```txt
# Definiert durch Alice, validiert oder akzeptiert von Bob
siegel <- Definiere()
# Siegel wird durch Alice mit einer Nachricht geschlossen
zeuge <- Schliesse(siegel, nachricht)
# Verifizierung durch Bob
bool <- Verifiziere(siegel, zeuge, nachricht)
```

Die client-side Validierung geht jedoch noch einen Schritt weiter: Wenn die Definition eines Siegels selbst außerhalb der Blockchain bleibt, ist es (theoretisch) möglich, dass jemand die Existenz oder Legitimität des fraglichen Siegels anzweifelt. Um dieses Problem zu überwinden, wird eine Kette von ineinandergreifenden Single-use Seals verwendet:


- Jedes geschlossene Siegel enthält die Definition des folgenden Siegels;+
- Wir registrieren diese Verschlüsse (mit ihren _commitments_) innerhalb der Blockchain (in einer Bitcoin-Transaktion);
- Jeder Versuch, ein früheres Siegel zu ändern, würde also der in Bitcoin eingebetteten Historie widersprechen.

Genau das tut das RGB-System:


- Veröffentlichte Nachrichten sind _Commitments_ zu client-side validierten Daten;
- Die Siegeldefinition ist mit einem Bitcoin UTXO verbunden;
- Das Siegel wird geschlossen, wenn dieser UTXO ausgegeben ist oder wenn ein neuer Output demselben Commitment gutgeschrieben wird;
- Die Transaktionskette, die diese UTXOs ausgibt, entspricht dem Veröffentlichungsnachweis: Jeder Zustandsübergang oder jede Zustandsänderung auf RGB ist somit in Bitcoin verankert.

Zusammengefasst:


- Die _Siegeldefinition_ ist der UTXO, mit dem man ein zukünftiges Commitment versiegeln will;
- Das _Schliessedn des Siegels_ findet statt, wenn man diesen UTXO ausgibt und eine Transaktion erstellt, die das Commitment enthält;
- Der _Zeuge_ ist die Transaktion selbst, die beweist, dass man das Siegel mit diesem Inhalt geschlossen hat;
- Man kann nicht beweisen, dass ein Siegel nicht geschlossen wurde (man kann nicht absolut sicher sein, dass ein UTXO nicht bereits ausgegeben wurde oder in einem Block ausgegeben wird, den man noch nicht gesehen hat), aber man kann beweisen, dass es tatsächlich geschlossen wurde.

Diese Einzigartigkeit ist wichtig für die client-side Validierung: Wenn man einen Zustandsübergang validiert, prüft man, ob er einem eindeutigen UTXO entspricht, der zuvor nicht in einer konkurrierenden Verpflichtung ausgegeben wurde. Dadurch wird sichergestellt, dass in off-chain Smart Contracts keine "double spends" getätigt werden.

### Multi-Commitments und Wurzeln

Ein RGB-Smart Contract muss möglicherweise mehrere Single-use Seals (mehrere UTXOs) gleichzeitig ausgeben. Darüber hinaus kann eine einzelne Bitcoin-Transaktion mehrere unterschiedliche Smart Contracts referenzieren, von denen jeder seinen eigenen Zustandsübergang versiegelt. Dies erfordert einen **Multi-Commitment**-Mechanismus, um deterministisch und eindeutig zu beweisen, dass keines der Commitments doppelt existiert. Hier kommt der Begriff **Anker** in RGB ins Spiel: eine spezielle Struktur, die eine Bitcoin-Transaktion und eine oder mehrere client-side Commitments (Zustandsübergänge) verbindet, von denen jedes potentiell zu einem anderen Vertrag gehört. Wir werden uns dieses Konzept im nächsten Kapitel genauer ansehen.

![RGB-Bitcoin](assets/en/023.webp)

Zwei der wichtigsten GitHub-Repositories des Projekts (unter der Organisation LNPBP) fassen die grundlegenden Implementierungen dieser im ersten Kapitel untersuchten Konzepte zusammen:


- **client_side_validation** : Enthält Rust-Primitive für die lokale Validierung;
- **single_use_seals**: Implementiert die Logik zur Definition und zum sicheren Schließen dieser Siegel.

![RGB-Bitcoin](assets/en/020.webp)

Beachte, dass diese Software-Bausteine Bitcoin-unabhängig sind; theoretisch könnten sie auf jedes andere Proof-of-Publication-Medium (ein anderes Register, eine Zeitschrift usw.) angewendet werden. In der Praxis verlässt sich RGB auf Bitcoin wegen seiner Robustheit und seines breiten Konsenses.

![RGB-Bitcoin](assets/en/021.webp)

### Fragen aus der Öffentlichkeit

#### Hin zu einer breiteren Verwendung von Single-use Seals

Peter Todd hat auch das _Open Timestamps_ Protokoll entwickelt, und das Konzept der Single-use Seals ist eine natürliche Erweiterung dieser Ideen. Neben RGB sind auch andere Anwendungsfälle denkbar, wie z.B. die Konstruktion von [_Sidechains_](https://planb.academy/resources/glossary/sidechain) ohne [_Merge Mining_](https://planb.academy/resources/glossary/merged-mining) oder [Drivechain](https://planb.academy/resources/glossary/drivechain)-bezogene Vorschläge wie BIP300. Jedes System, das ein einziges Commitment erfordert, kann im Prinzip dieses kryptografische Primitiv ausnutzen. Heute ist RGB die erste große Implementierung in vollem Umfang.

#### Probleme mit der Datenverfügbarkeit

Da bei der client-side Validierung jeder Nutzer seinen eigenen Teil der Historie speichert, ist die Verfügbarkeit der Daten nicht global garantiert. Wenn ein Emittent bestimmte Informationen zurückhält oder widerruft, weiß man möglicherweise nicht, wie sich das Angebot tatsächlich entwickelt hat. In einigen Fällen (z. B. bei Stablecoins) wird vom Emittenten erwartet, dass er öffentliche Daten vorhält, um den Umfang des Umlaufs nachzuweisen, aber es besteht keine technische Verpflichtung dazu. Es ist daher möglich, bewusst undurchsichtige Verträge mit unbegrenztem Angebot zu entwerfen, was Fragen des Vertrauens aufwirft.

#### Sharding und Vertragsisolierung

Jeder Vertrag (Smart Contract) stellt einen isolierten _Shard_ dar: USDT und USDC zum Beispiel müssen ihre Historie nicht teilen. Atomic Swaps sind nach wie vor möglich, aber dabei werden ihre Register nicht zusammengeführt. Alles geschieht durch ein kryptografisches Comittment, ohne dass jeder Teilnehmer den gesamten Verlaufsgraphen offenlegen muss.

### Schlussfolgerung

Wir haben gesehen, wie das Konzept der client-side Validierung in die Blockchain und die _State Channels_ passt, wie es die Trilemmata des distributed Computing beeinflusst und wie es die Bitcoin-Blockchain auf einzigartige Weise nutzt, um double spends zu vermeiden sowie *Zeitstempel* bereitzustellen. Die Idee basiert auf dem Konzept des **Single-use Seal**, das die Erstellung eindeutiger Commitments ermöglicht, die nicht beliebig erneut ausgegeben werden können. Auf diese Weise lädt jeder Teilnehmer nur den unbedingt notwendigen Verlauf hoch, was die Skalierbarkeit und Vertraulichkeit von Smart Contracts erhöht und gleichzeitig die Sicherheit von Bitcoin im Hintergrund beibehält.

Der nächste Schritt wird sein, genauer zu erklären, wie dieser Single-use Seal-Mechanismus in Bitcoin (über UTXOs) angewandt wird, wie Anker erstellt und validiert werden und wie dann komplette Smart Contracts in RGB aufgebaut werden. Insbesondere werden wir uns mit dem Problem der Multi-Commitments befassen, der technischen Herausforderung, zu beweisen, dass eine Bitcoin-Transaktion gleichzeitig mehrere Zustandsübergänge in verschiedenen Verträgen versiegelt, ohne Schwachstellen oder doppelte Verpflichtungen einzuführen.

Bevor du in die technischen Details des zweiten Kapitels eintauchst, solltest du dir die Schlüsseldefinitionen (Client-side Validierung, Single-use Seal, Anker, etc.) noch einmal durchlesen und dir die allgemeine Logik vor Augen halten: Wir versuchen, die Stärken der Bitcoin-Blockchain (Sicherheit, Dezentralisierung, Zeitstempel) mit denen von Off-Chain-Lösungen (Geschwindigkeit, Vertraulichkeit, Skalierbarkeit) in Einklang zu bringen, und genau das ist es, was RGB und client-side Validierung zu erreichen versuchen.

## Die Commitment-Ebene

<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

:::video id=73ddea2d-c243-479d-a3dc-12d7db8eef70:::

In diesem Kapitel werden wir uns die Implementierung von client-side Validierung und Single-use Seals innerhalb der Bitcoin-Blockchain ansehen. Wir werden die Hauptprinzipien von RGBs **Commitment Layer** (Layer 1) vorstellen, mit einem besonderen Fokus auf das **TxO2** Schema, welches RGB verwendet, um ein Siegel in einer Bitcoin Transaktion zu definieren und zu schließen. Als nächstes werden wir zwei wichtige Punkte besprechen, die bisher noch nicht im Detail behandelt wurden:


- Die _deterministischen Bitcoin-Commitments_;
- Multi-Protokoll-Commitments.

Es ist die Kombination dieser Konzepte, die es uns ermöglicht, mehrere Systeme oder Verträge über einen einzigen UTXO und damit eine einzige Blockchain zu legen.

Es sei daran erinnert, dass die beschriebenen kryptographischen Operationen absolut gesehen auch auf andere Blockchains oder Veröffentlichungsmedien angewendet werden können, aber die Eigenschaften von Bitcoin (in Bezug auf Dezentralisierung, Widerstand gegen Zensur und Offenheit für alle) machen es zur idealen Grundlage für die Entwicklung fortgeschrittener Programmierbarkeit, wie sie von **RGB** benötigt wird.

### Commitment-Schemata in Bitcoin und ihre Verwendung durch RGB

Wie wir im ersten Kapitel des Kurses gesehen haben, sind Single-use Seals ein allgemeines Konzept: wir geben ein Versprechen ab, eine Verpflichtung (_commitment_) an einer bestimmten Stelle in einer Transaktion aufzunehmen, und diese Stelle wirkt wie ein Siegel, das wir auf einer Nachricht schließen. Auf der Bitcoin-Blockchain gibt es jedoch mehrere Optionen für die Wahl des Ortes, an dem diese Verpflichtung (_commitment_) platziert werden kann.

Um die Logik zu verstehen, erinnern wir uns an das Grundprinzip: Um ein _Single-use Seal_ zu schließen, geben wir den versiegelten Bereich aus, indem wir das _Commitment_ für eine bestimmte Nachricht einfügen. In Bitcoin kann dies auf verschiedene Arten geschehen:


- Verwendung eines öffentlichen Schlüssels oder einer Adresse

Wir können entscheiden, dass ein bestimmter öffentlicher Schlüssel oder eine Adresse das _Single-use Seal_ ist. Sobald dieser Schlüssel oder diese Adresse in einer Transaktion auf der Blockchain erscheint, bedeutet dies, dass das Siegel mit einer bestimmten Nachricht geschlossen wird.


- Verwendung eines **Bitcoin-Transaktionsoutput**

Das bedeutet, dass ein _Single-use Seal_ als ein genauer [_Output_](https://planb.academy/resources/glossary/output) (ein Paar aus TXID und Ausgangsnummer) definiert ist. Sobald dieser _Output_ ausgegeben ist, wird das Siegel geschlossen.

Während der Arbeit an RGB haben wir mindestens 4 verschiedene Möglichkeiten gefunden, diese Siegel auf Bitcoin zu implementieren:


- Definieren des Siegels über einen öffentlichen Schlüssel, und Schließen in einem _Output_ ;
- Definieren des Siegels mit einem _Outpoint_ und Schließen mit einem _Output_;
- Definieren des Siegels über den Wert eines öffentlichen Schlüssels, und Schließen in einem _Input_ ;
- Definieren des Siegels über einen _Outpoint_ und Schließen mit einem _Input_.

| Name des Schemas | Definition des Siegels            | Siegel schließen       | Zusätzliche Anforderungen                             | Hauptanwendung                | Mögliche Commitment-Schemata  |
| ----------------- | ---------------------------      | ---------------------- | ----------------------------------------------------- | --------------------------    | ----------------------------- |
| PkO               | Wert des öffentlichen Schlüssels | Transaktions-Output    | P2(W)PKH                                              | Derzeit keine                 | Keytweak, taptweak, opret     |
| TxO2              | Transaktions-Output              | Transaktions-Output    | Erfordert deterministische Commitments auf Bitcoin    | RGBv1 (universell)            | Keytweak, tapret, opret       |
| PkI               | Wert des öffentlichen Schlüssels | Transaktions-Output    | Nur Taproot & nicht kompatibel mit Legacy-Wallets     | Bitcoin-basierte Identitäten  | Sigtweak, witweak             |
| TxO1              | Transaktions-Output              | Transaktions-Output    | Nur Taproot & nicht kompatibel mit Legacy-Wallets     | Derzeit keine                 | Sigtweak, witweak             |


Wir werden nicht im Detail auf jede dieser Konfigurationen eingehen, da wir uns in RGB dafür entschieden haben, **einen _Outpoint_ als Definition des Siegels** zu verwenden und das _commitment_ in dem Output der Transaktion zu platzieren, die diesen _Outpoint_ ausgibt. Wir können daher die folgenden Konzepte für die Fortsetzung einführen:


- "Siegeldefinition": Ein bestimmter _Outpoint_ (identifiziert durch TXID + Ausgangs-Nr.);
- **"Siegel Verschluss"**: Die Transaktion, die diesen _Outpoint_ ausgibt, in dem ein _Commitment_ zu einer Nachricht hinzugefügt wird.

Dieses Schema wurde wegen seiner Kompatibilität mit der RGB-Architektur gewählt, aber andere Konfigurationen könnten für verschiedene Zwecke nützlich sein.

Das "O2" in "TxO2" erinnert uns daran, dass sowohl die Definition als auch der Verschluss auf dem Ausgeben (oder Erstellen) eines Transaktions-Outputs beruhen.

### Beispiel für ein TxO2-Diagramm

Zur Erinnerung: Die Definition eines _Single-use Seals_ erfordert nicht unbedingt die Veröffentlichung einer On-Chain-Transaktion. Es reicht aus, wenn Alice zum Beispiel bereits einen unverbrauchten UTXO hat. Sie kann entscheiden: "Dieser _Outpoint_ (der bereits existiert) ist jetzt mein Siegel". Sie notiert dies lokal (_client-side_), und bis dieser UTXO ausgegeben ist, gilt das Siegel als offen.

![RGB-Bitcoin](assets/en/024.webp)

An dem Tag, an dem sie das Siegel schließen will (um ein Ereignis zu signalisieren oder eine bestimmte Nachricht zu verankern), gibt sie diese UTXO in einer neuen Transaktion aus (diese Transaktion wird oft "_Zeugentransaktion_" genannt (hat nichts mit _segwit_ zu tun, es ist nur der Begriff, den wir ihr geben). Diese neue Transaktion enthält das _commitment_ zu der Nachricht.

![RGB-Bitcoin](assets/en/025.webp)

Beachte, dass in diesem Beispiel :


- niemand außer Bob (oder den Personen, denen Alice den vollständigen Beweis offenbart) wissen wird, dass eine bestimmte Nachricht in dieser Transaktion versteckt ist;
- jeder sehen kann, dass der _Outpoint_ ausgegeben wurde, aber nur Bob hat den Beweis, dass die Nachricht tatsächlich in der Transaktion verankert ist.

Zur Veranschaulichung dieses TxO2-Schemas können wir ein _Single-Use Seal_ als Mechanismus für den Widerruf eines PGP-Schlüssels verwenden. Anstatt ein Widerrufszertifikat auf Servern zu veröffentlichen, kann Alice sagen: "Dieser Bitcoin-Output: wenn er ausgegeben wird, bedeutet dies, dass mein PGP-Schlüssel widerrufen wird".

Alice verfügt also über einen bestimmten UTXO, dem ein bestimmter Zustand oder bestimmte Daten (die nur ihr bekannt sind) lokal (auf der client-side) zugeordnet sind.

Alice teilt Bob mit, dass ein bestimmtes Ereignis als eingetreten gilt, wenn dieser UTXO ausgegeben wird. Von außen betrachtet ist alles, was wir sehen, eine Bitcoin-Transaktion, aber Bob weiß, dass diese Ausgabe eine versteckte Bedeutung hat.

![RGB-Bitcoin](assets/en/026.webp)

Wenn Alice diesen UTXO ausgibt, schließt sie das Siegel auf einer Nachricht, die ihren neuen Schlüssel oder einfach den Widerruf des alten Schlüssels angibt. Auf diese Weise kann jeder, der die Kette überwacht, sehen, dass der UTXO ausgegeben wurde, aber nur diejenigen, die den vollständigen Beweis haben, wissen, dass es sich um den Widerruf des PGP-Schlüssels handelt.

![RGB-Bitcoin](assets/en/027.webp)

Damit Bob oder ein anderer Beteiligter die versteckte Nachricht überprüfen kann, muss Alice ihm Informationen außerhalb der Kette zur Verfügung stellen.

![RGB-Bitcoin](assets/en/028.webp)

Alice muss Bob also:


- die Nachricht selbst (z.B. den neue PGP-Schlüssel);
- den kryptographischen Beweis, dass die Nachricht an der Transaktion beteiligt war (bekannt als _extra transaction proof_ oder _anchor_)

mitteilen.

![RGB-Bitcoin](assets/en/029.webp)

Dritte haben diese Informationen nicht. Sie sehen nur, dass ein UTXO ausgegeben wurde. Die Vertraulichkeit ist also gewährleistet.

Um die Struktur zu verdeutlichen, fassen wir den Prozess in zwei Transaktionen zusammen:


- **Transaktion 1**: Sie enthält die _Siegeldefinition_, d.h. den _Outpoint_, der als Siegel dienen wird.

![RGB-Bitcoin](assets/en/031.webp)


- **Transaktion 2**: Gibt diesen _Outpoint_ aus. Dies schließt das Siegel und fügt in derselben Transaktion das _Commitment_ zu der Nachricht ein.

![RGB-Bitcoin](assets/en/033.webp)

Wir bezeichnen daher die zweite Transaktion als "_Zeugentransaktion_".

Um dies aus einem anderen Blickwinkel zu veranschaulichen, können wir zwei Ebenen darstellen:


- Die oberste Schicht (Blockchain, öffentlich): Jeder sieht die Transaktion und weiß, dass ein _Outpoint_ ausgegeben wurde;
- Die untere Schicht (client-side, privat): Nur Alice (oder die betreffende Person) weiß über den kryptografischen Beweis und die von ihr lokal aufbewahrte Nachricht, dass diese Ausgabe einer gewissen anderen Nachricht entspricht.

![RGB-Bitcoin](assets/en/034.webp)

Beim Schließen des Siegels stellt sich jedoch die Frage, wo das _Commitment_ eingefügt werden soll.

Im vorherigen Abschnitt haben wir kurz erwähnt, wie das client-side Validierungsmodell auf RGB und andere Systeme angewendet werden kann. Hier befassen wir uns mit **deterministischen Bitcoin-Comittments** und wie man sie in eine Transaktion integriert. Die Idee ist, zu verstehen, warum wir versuchen, eine einzelne Zusage in die _Zeugentransaktion_ einzufügen, und vor allem, wie wir sicherstellen können, dass es keine anderen, nicht offengelegten konkurrierenden Commitments geben kann.

### Orte für Commitments in einer Transaktion

Wenn du jemandem beweist, dass eine bestimmte Nachricht in einer Transaktion eingebettet ist, musst du garantieren können, dass es keine andere Form des Commitments (eine zweite, versteckte Nachricht) in derselben Transaktion gibt, die deinem Gegenüber nicht offenbart wurde. Damit die client-side Validierung robust bleibt, braucht man einen **deterministischen** Mechanismus, um ein einzelnes _Commitment_ in die Transaktion einzufügen, das das _Single-use Seal_ schließt.

Die _Zeugentransaktion_ gibt den berühmten UTXO (oder _Siegeldefinition_) aus, und diese Ausgabe entspricht dem Schließen des Siegels. Technisch gesehen, wissen wir, dass jeder Outpoint nur einmal ausgegeben werden kann. Das ist genau das, was den Schutz von Bitcoin gegen Doppelausgaben untermauert. Aber die ausgebende Transaktion kann mehrere _Inputs_ und mehrere _Outputs_ haben oder auf komplexe Weise zusammengesetzt sein (Coinjoins, Lightning Channels usw.). Wir müssen daher eindeutig und einheitlich definieren, wo das _Commitment_ in dieser Struktur eingefügt werden soll.

Unabhängig von der Methode (PkO, TxO2, usw.) kann das _Commitment_ eingefügt werden:


- In einem **Input** über :
- **Sigtweak** (modifiziert die `r`-Komponente der ECDSA-Signatur, ähnlich dem "Sign-to-contract"-Prinzip) ;
- **Witweak** (die Daten des _segregated witness_ der Transaktion werden geändert).
- In einem **Output** über :
- **Keytweak** (der öffentliche Schlüssel des Empfängers wird mit der Nachricht "getweaked") ;
- **Opret** (die Nachricht wird in einem nicht ausgabefähigen Output `OP_RETURN` abgelegt) ;
- **Tapret** (oder _Taptweak_), das sich auf taproot stützt, um das Commitment in den Skriptteil eines taproot-Schlüssels einzufügen und so den öffentlichen Schlüssel deterministisch zu verändern.

![RGB-Bitcoin](assets/en/035.webp)

Im Folgenden findest du die Einzelheiten der einzelnen Methoden:

![RGB-Bitcoin](assets/en/038.webp)

***Sig tweak (sign-to-contract) :***

Ein früheres Verfahren bestand darin, den zufälligen Teil einer [Signatur](https://planb.academy/resources/glossary/digital-signature) ([ECDSA](https://planb.academy/resources/glossary/ecdsa) oder [Schnorr](https://planb.academy/resources/glossary/schnorr-protocol)) auszunutzen, um das _Commitment_ einzubetten: dies ist die Technik, die als "**sign-to-contract**" bekannt ist. Man ersetzt die zufällig erzeugte Nonce durch einen Hash, der die Daten enthält. Auf diese Weise gibt die Signatur implizit das Commitment preis, ohne dass zusätzlicher Platz in der Transaktion benötigt wird. Dieser Ansatz hat eine Reihe von Vorteilen:


- Keine On-Chain-Überlastung (man verwendet die gleiche Stelle wie die Basis-Nonce);
- Theoretisch kann dies recht diskret sein, da die Nonce zunächst ein zufälliges Datum ist.

Es haben sich jedoch 2 große Nachteile gezeigt:


- [Multisig](https://planb.academy/resources/glossary/multisig) vor Taproot: Wenn man mehrere Unterzeichner hat, müssen man entscheiden, welche Unterschrift das _Commitment_ tragen soll. Unterschriften können unterschiedlich angeordnet werden, und wenn ein Unterzeichner sich weigert, verliert man die Kontrolle über das Ergebnis des _Commitments_;
- MuSig und die gemeinsame Nonce: Bei Schnorr-Multisig (*MuSig*) ist die Nonce-Erzeugung ein Mehrparteien-Algorithmus, und es ist praktisch unmöglich, die Nonce individuell zu verändern.

In der Praxis ist **sig tweak** auch nicht sehr kompatibel mit bestehender Hardware (Hardware-Wallets) und Formaten (Lightning, etc.). Diese großartige Idee ist also schwer in die Praxis umzusetzen.

***Keytweak (pay-to-contract) :***

Der **Keytweak** greift das historische Konzept des _pay-to-contract_ auf. Wir nehmen den öffentlichen Schlüssel `X` und verändern ihn, indem wir den Wert `H(message)` hinzufügen. Genauer gesagt, wenn `X = x * G` und `h = H(message)`, dann ist der neue Schlüssel `X' = X + h * G`. Dieser veränderte Schlüssel verbirgt das Commitment an die `Nachricht`. Der Inhaber des ursprünglichen privaten Schlüssels kann durch Hinzufügen von `h` zu seinem privaten Schlüssel `x` beweisen, dass er den Schlüssel hat, um den Output auszugeben. Theoretisch ist das elegant, denn:


- Das _Commitment_ wird eingegeben, ohne dass zusätzliche Felder hinzugefügt werden;
- Man speichert keine zusätzlichen Daten on-chain.

In der Praxis stoßen wir jedoch auf die folgenden Schwierigkeiten:


- Wallets erkennen den öffentlichen Standardschlüssel nicht mehr, da er "getweaked" wurde, so dass sie den UTXO nicht ohne weiteres mit deinem üblichen Schlüssel in Verbindung bringen können;
- Hardware-Wallets sind nicht dafür ausgelegt, mit einem Schlüssel zu signieren, der nicht von ihrer Standardableitung abgeleitet ist;
- Man muss seine Skripte, Deskriptoren usw. anpassen.

Im Zusammenhang mit RGB war dieser Weg bis 2021 vorgesehen, aber es erwies sich als zu kompliziert, ihn mit derzeitigen Standards und Infrastruktur zu verwirklichen.

***Witweak :***

Eine andere Idee, die von bestimmten Protokollen wie _inscriptions ordinals_ in die Praxis umgesetzt wurde, besteht darin, die Daten direkt in den "Witness"-Abschnitt der Transaktion zu schreiben (daher der Ausdruck "witness tweak"). Aber, diese Methode :


- macht das Engagement sofort sichtbar (man fügt buchstäblich Rohdaten in den Witness-Abschnitt ein);
- kann der Zensur unterliegen (Miner oder Nodes können die Weiterleitung verweigern, wenn die Transaktion zu groß ist oder ein anderes willkürliches Merkmal aufweist);
- verbraucht Platz in den Blöcken, was den Zielen von RGB, nämlich Diskretion und Leichtigkeit, zuwiderläuft.

Außerdem ist der Witness-Abschnitt so konzipiert, dass er in bestimmten Kontexten gekürzt werden kann, was die Erstellung robuster Beweise komplizierter machen kann.

***Open-return (opret) :***

Ein sehr einfach zu nutzendes `OP_RETURN` erlaubt es einem, einen Hash oder eine Nachricht in einem speziellen Feld der Transaktion zu speichern. Aber es ist sofort erkennbar: jeder sieht, dass es ein _Commitment_ in der Transaktion gibt, und es kann zensiert oder verworfen werden, oder zusätzliche Outputs hinzugefügt werden. Da dies die Transparenz und die Blockgröße erhöht, wird es vom Standpunkt einer client-side Validierungslösung als weniger zufriedenstellend angesehen.

```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|
1-byte       1-byte         32 bytes
```

### Tapret

Die letzte Option ist die Verwendung von [**Taproot**](https://planb.academy/resources/glossary/taproot) (eingeführt mit BIP341) mit dem *Tapret*-Schema. *Tapret* ist eine komplexere Form eines deterministischen Commitments, die Verbesserungen in Bezug auf den Fußabdruck auf der Blockchain und die Vertraulichkeit für Vertragsoperationen bringt. Die Hauptidee besteht darin, das Comittment im `Script Path Spend`-Teil einer [Taproot-Transaktion](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) zu verstecken.

![RGB-Bitcoin](assets/en/036.webp)

Bevor wir beschreiben, wie das Commitment in eine Taproot-Transaktion eingefügt wird, schauen wir uns die **exakte Form** des Commitments an, die **zwingenderweise** einer 64-Byte-Zeichenkette entsprechen muss, die wie folgt [aufgebaut](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) ist:

```txt
64-byte_Tapret_Commitment =

OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|
TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```


- Die 29 Bytes `OP_RESERVED`, gefolgt von `OP_RETURN`, dann `OP_PUSHBYTE_33`, bilden den 31 Byte langen _Präfixteil_;
- Als Nächstes kommt ein 32-Byte-_Commitment_ (normalerweise die [Merkle-Root](https://planb.academy/resources/glossary/merkle-root) von **MPC**), zu der wir 1 Byte **Nonce** hinzufügen (insgesamt 33 Byte für diesen zweiten Teil).

Die 64-Byte `Tapret`-Methode sieht also aus wie ein `Opret`, dem wir 29 Bytes `OP_RESERVED` vorangestellt und ein zusätzliches Byte als Nonce hinzugefügt haben.

Um die Flexibilität in Bezug auf Implementierung, Vertraulichkeit und Skalierung zu erhalten, berücksichtigt das Tapret-Schema verschiedene Anwendungsfälle, je nach Anforderungen:


- Eindeutige Einbindung eines Tapret-Commitments in eine Taproot-Transaktion ohne eine bereits bestehende Script Path-Struktur;
- Integration eines Tapret-Commitments in eine Taproot-Transaktion, die bereits mit einem Script Path ausgestattet ist.

Schauen wir uns diese beiden Szenarien einmal genauer an.

#### Tapret-Einbindung ohne bestehenden Script Path

In diesem ersten Fall gehen wir von einem Taproot-Ausgabeschlüssel (*Taproot-Output-Key*) `Q` aus, der nur den internen öffentlichen Schlüssel `P` (*Interner Schlüssel*) und keinen zugehörigen Skriptpfad (*Skriptpfad*) enthält:

![RGB-Bitcoin](assets/en/047.webp)


- `P`: der interne öffentliche Schlüssel für den _Key Path Spend_.
- `G`: der Erzeugungspunkt der elliptischen Kurve [secp256k1](https://en.bitcoin.it/wiki/Secp256k1).
- `t = tH_TWEAK(P)` ist der Tweak-Faktor, der über einen _getaggten Hash_ (z.B. `SHA-256(SHA-256(TapTweak) || P)`) gemäß [BIP86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki#address-derivation) berechnet wird. Dies beweist, dass es kein verstecktes Skript gibt.

Um ein **Tapret**-Commitment einzubeziehen, fügt man einen **Script Path Spend** mit einem **eindeutigen Skript** wie folgt hinzu:

![RGB-Bitcoin](assets/en/048.webp)


- `t = tH_TWEAK(P || Script_root)` wird dann zum neuen Tweak-Faktor, einschließlich der **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` stellt die Wurzel dieses **Skripts** dar, die einfach ein Hash des Typs `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)` ist.

Der Nachweis des Einbeziehens und der Einzigartigkeit im taproot tree läuft hier auf den einzigen internen öffentlichen Schlüssel `P` hinaus.

#### Tapret-Integration in einen bereits bestehenden Skript Path

Das zweite Szenario betrifft einen komplexeren `Q` **taproot**-Output, der bereits mehrere Skripte enthält. Wir haben zum Beispiel einen Baum mit 3 Skripten:

![RGB-Bitcoin](assets/en/049.webp)


- `tH_LEAF(x)` bezeichnet die normalisierte getaggte Hash-Funktion eines Blattskripts.
- `A, B, C` stehen für Skripte, die bereits in der taproot Struktur enthalten sind.

Um das Tapret-Commitment hinzuzufügen, müssen wir ein *unausgebbares Skript* auf der ersten Ebene des Baums einfügen und die vorhandenen Skripte um eine Ebene nach unten verschieben. Grafisch wird der Baum zu :

![RGB-Bitcoin](assets/en/050.webp)


- `tHABC` steht für den getaggten Hash der Gruppe `A, B, C` auf der obersten Ebene.
- `tHT` steht für den Hash des Skripts, der dem 64-Byte-`Tapret` entspricht.

Laut den Taproot Regeln muss jeder Zweig/Blatt nach einer lexikographischen Hash-Reihenfolge kombiniert werden. Es gibt zwei mögliche Fälle:


- **`tHT` > `tHABC`**: Das Tapret-Commitment bewegt sich nach rechts im Baum. Der Einzigartigkeitsbeweis benötigt nur `tHABC` und `P`;
- **`tHT` < `tHABC`**: Das Tapret-Commitment ist links platziert. Um zu beweisen, dass es kein anderes Tapret-Commitement auf der rechten Seite gibt, müssen `tHAB` und `tHC` aufgedeckt werden, um zu zeigen, dass es kein anderes derartiges Script gibt.

Anschauliches Beispiel für den ersten Fall (`tHABC < tHT`):

![RGB-Bitcoin](assets/en/051.webp)

Beispiel für den zweiten Fall (`tHABC > tHT`):

![RGB-Bitcoin](assets/en/052.webp)

#### Optimierung mit der Nonce

Um die Vertraulichkeit zu verbessern, können wir den Wert von `<Nonce>` (das letzte Byte des 64-Byte-`Tapret`) "minen" (ein besserer Begriff wäre "bruteforcing"), um einen Hashwert `tHT` zu erhalten, für den `tHABC < tHT` ist. In diesem Fall wird das Commitment auf der rechten Seite platziert, so dass der Benutzer nicht den gesamten Inhalt bestehender Skripte preisgeben muss, um die Einzigartigkeit des Tapret zu beweisen.

Zusammenfassend lässt sich sagen, dass `Tapret` eine diskrete und deterministische Möglichkeit bietet, ein Commitment in eine Taproot-Transaktion einzubinden und gleichzeitig die Anforderungen an Eindeutigkeit und Einzigartigkeit zu erfüllen, die für die client-side Validierung und die Single-use Seal Logik von RGB wesentlich sind.

#### Gültige Ausgänge

Für RGB-Commitment-Transaktionen ist die Hauptvoraussetzung für ein gültiges Bitcoin-Commitment-Schema die folgende: Die Transaktion (*Zeugentransaktion*) muss nachweislich ein einziges Commitment enthalten. Diese Anforderung macht es unmöglich, eine alternative Historie für client-side validierte Daten innerhalb derselben Transaktion zu konstruieren. Das bedeutet, dass die Nachricht, um die sich das _Single-use Seal_ schließt, einzigartig ist.

Um diesem Prinzip gerecht zu werden und unabhängig von der Anzahl der Ausgaben in einer Transaktion, verlangen wir, dass **ein und nur ein Output** eine Verpflichtung (*Commitment*) enthalten kann. Für jedes der verwendeten Schemata (*Opret* oder *Tapret*) sind die einzigen gültigen Outputs, die ein RGB-_Commitment_ enthalten können:


- Der erste `OP_RETURN`-Output (falls vorhanden) für das *Opret*-Schema;
- Der erste Taproot-Output (falls vorhanden) für das *Tapret*-Schema.

Es ist durchaus möglich, dass eine Transaktion ein einziges `Opret`-Commitment und ein einziges `Tapret`-Commitment in zwei getrennten Outputs enthält. Dank des deterministischen Charakters der Siegeldefinition entsprechen diese beiden Commitments dann zwei verschiedenen Daten, die auf der client-side validiert werden.

### Analyse und konkrete Design-Entscheidungen in RGB

Als wir mit RGB begannen, prüften wir all diese Methoden, um zu bestimmen, wo und wie wir ein _Commitment_ in einer Transaktion auf deterministische Weise platzieren können. Wir haben einige Kriterien definiert:


- Kompatibilität mit verschiedenen Szenarien (z.B. Multisig, Lightning, Hardware-Wallets, etc.);
- Auswirkungen auf den Platz in der Blockchain;
- Schwierigkeit der Umsetzung und Wartung;
- Vertraulichkeit und Zensurresistenz.

| Methode                                            | On-chain Fußabdruck | Größe auf client-side | Wallet-Integration | Hardware-Kompatibilität | Lightning-Kompatibilität | Taproot-Kompatibilität |
| -------------------------------------------------- | ---------------------- | --------------------- | ----------------------------- | ---------------------- | ---------------------- | --------------------- |
| Keytweak (deterministisches P2C)                   | 🟢                     | 🟡                   | 🔴                            | 🟠                     | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🟢 MuSig  |
| Sigtweak (deterministisches S2C)                   | 🟢                     | 🟢                   | 🟠                            | 🔴                     | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🔴 MuSig  |
| Opret (OP_RETURN)                                  | 🔴                     | 🟢                   | 🟢                            | 🟠                     | 🔴 BOLT, 🟠 Bifrost     | -                     |
| Tapret-Algorithmus: oberster linker Knoten        | 🟠                     | 🔴                   | 🟠                            | 🟢                     | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Tapret-Algorithmus #4: beliebiger Knoten + Beweis | 🟢                     | 🟠                   | 🟠                            | 🟢                     | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |

| Deterministisches Commitment-Schema                        | Standard       | On-Chain-Kosten                                                                                                         | Nachweisgröße client-side                                                                               |
| ------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Keytweak (deterministisches P2C)                              | LNPBP-1, 2     | 0 Bytes                                                                                                                | 33 Bytes (nicht getweakter Schlüssel)                                                                          |
| Sigtweak (deterministisches S2C)                              | WIP (LNPBP-39) | 0 Bytes                                                                                                                | 0 Bytes                                                                                                        |
| Opret (OP_RETURN)                                             | -              | 36 (v)Bytes (zusätzlicher TxOut)                                                                                       | 0 Bytes                                                                                                        |
| Tapret-Algorithmus: oberster linker Knoten                    | LNPBP-6        | 32 Bytes im Witness (8 vBytes) für jedes n-aus-m MultiSig und Ausgabe über Script-Path                                 | 0 Bytes für scriptless scripts taproot ~270 Bytes bei einem einzigen Script, ~128 Bytes, falls mehrere Scripts |
| Tapret-Algorithmus #4: beliebiger Knoten + Einzigkeitsnachweis | LNPBP-6        | 32 Bytes im Witness (8 vBytes) für Fälle mit einzelnem Script, 0 Bytes im Witness in den meisten anderen Fällen      | 0 Bytes für scriptless scripts taproot, 65 Bytes, bis der Taptree ein Dutzend Skripte enthält                   |

| Layer                          | On-Chain-Kosten (Bytes/vbytes) | On-Chain-Kosten (Bytes/vbytes) | On-Chain-Kosten (Bytes/vbytes) | On-Chain-Kosten (Bytes/vbytes) | On-Chain-Kosten (Bytes/vbytes) | Client-Kosten (Bytes) | Client-Kosten (Bytes) | Client-Kosten (Bytes) | Client-Kosten (Bytes) | Client-Kosten (Bytes) |
| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | --------------------- | --------------------- | --------------------- | --------------------- | --------------------- |
| **Typ**                        | **Tapret**                   | **Tapret #4**                | **Keytweak**                 | **Sigtweak**                 | **Opret**                    | **Tapret**           | **Tapret #4**        | **Keytweak**         | **Sigtweak**         | **Opret**            |
| SingleSig                     | 0                            | 0                            | 0                            | 0                            | 32                           | 0                     | 0                     | 32                    | 0?                    | 0                     |
| MuSig (n-aus-n)                 | 0                            | 0                            | 0                            | 0                            | 32                           | 0                     | 0                     | 32                    | ? > 0                 | 0                     |
| MultiSig 2-aus-3               | 32/8                         | 32/8 oder 0                  | 0                            | n/a                          | 32                           | ~270                  | 65                    | 32                    | n/a                   | 0                     |
| MultiSig 3-aus-5               | 32/8                         | 32/8 oder 0                  | 0                            | n/a                          | 32                           | ~340                  | 65                    | 32                    | n/a                   | 0                     |
| MultiSig 2-aus-3 mit Timeouts  | 32/8                         | 0                            | 0                            | n/a                          | 32                           | 64                     | 65                    | 32                    | n/a                   | 0                     |


| Layer                            | On-Chain-Kosten (vbytes) | On-Chain-Kosten (vbytes) | On-Chain-Kosten (vbytes) | Client-Kosten (bytes) | Client-Kosten (bytes) |
| -------------------------------- | ------------------------ | ------------------------ | ------------------------ | --------------------- | --------------------- |
| **Typ**                          | **Basis**                | **Tapret #2**            | **Tapret #4**            | **Tapret #2**         | **Tapret #4**         |
| MuSig (n-aus-n)                  | 16.5                     | 0                        | 0                        | 0                     | 0                     |
| FROST (n-aus-m)                  | ?                        | 0                        | 0                        | 0                     | 0                     |
| Multi_a (n-aus-m)                | 1+16n+8m                 | 8                        | 8                        | 33 * m                | 65                    |
| Branch MuSig / Multi_a (n-aus-m) | 1+16n+8n+8xlog(n)        | 8                        | 0                        | 64                    | 65                    |
| Mit Timeouts (n-aus-m)           | 1+16n+8n+8xlog(n)        | 8                        | 0                        | 64                    | 65                    |

| Methode                                    | Datenschutz und Skalierbarkeit | Interoperabilität | Kompatibilität | Portabilität | Komplexität |
| ------------------------------------------ | ------------------------------ | ----------------- | -------------- | ------------ | ----------- |
| Keytweak (deterministisches P2C)           | 🟢                             | 🔴                | 🔴            | 🟡           | 🟡          |
| Sigtweak (deterministisches S2C)           | 🟢                             | 🔴                | 🔴            | 🟢           | 🔴          |
| Opret (OP_RETURN)                          | 🔴                             | 🟠                | 🔴            | 🟢           | 🟢          |
| Algo Tapret: oberster linker Knoten        | 🟠                             | 🟢                | 🟢            | 🔴           | 🟠          |
| Algo Tapret #4: beliebiger Knoten + Beweis | 🟢                             | 🟢                | 🟢            | 🟠           | 🔴          |






Im Laufe der Untersuchung wurde deutlich, dass keines der Commitment-Schemata vollständig mit dem aktuellen Lightning-Standard kompatibel ist (der weder Taproot, _muSig2_ noch zusätzliche _Commitment_-Unterstützung bietet). Es wird daran gearbeitet, die Kanalkonstruktion von Lightning (*BiFrost*) so zu ändern, dass das Einfügen+ von RGB-Commitments möglich wird. Dies ist ein weiterer Bereich, in dem wir die Transaktionsstruktur, die Schlüssel und die Art und Weise, in der Kanalaktualisierungen signiert werden, überprüfen müssen.

Die Analyse hat gezeigt, dass andere Methoden (Key Tweak, Sig Tweak, Witness Tweak usw.) andere Formen von Komplikationen aufweisen:


- Entweder haben wir ein großes On-Chain-Volumen;
- Oder es gibt eine radikale Inkompatibilität mit dem bestehenden Code der Wallets;
- Oder die Lösung ist bei nicht-kooperativem MultiSig nicht durchführbar.

Für RGB sind zwei Methoden besonders hervorzuheben: ***Opret*** und ***Tapret***, die beide als "Transaction Output" bezeichnet werden und mit dem vom Protokoll verwendeten TxO2-Modus kompatibel sind.

### Multi-Protokoll-Commitments - MPC

In diesem Abschnitt sehen wir uns an, wie **RGB** die Aggregation von mehreren Verträgen (oder, genauer gesagt, deren _transition bundles_) innerhalb einer einzigen Verpflichtung (*Commitment*), die in einer Bitcoin-Transaktion aufgezeichnet wird, über ein deterministisches Schema (gemäß `Opret` oder `Tapret`) handhabt. Um dies zu erreichen, wird die Reihenfolge der Merkelisierung der verschiedenen Verträge in einer Struktur namens **MPC Tree** (_Multi Protocol Commitment Tree_) festgelegt. In diesem Abschnitt werden wir uns die Konstruktion dieses MPC-Trees ansehen, wie man seine Wurzel erhält und wie mehrere Verträge dieselbe Transaktion vertraulich und eindeutig teilen können.

Multi Protocol Commitment (MPC) wurde entwickelt, um zwei Anforderungen zu erfüllen:


- Die Konstruktion des `mpc::Commitment`-Hashes: Dieser wird in die Bitcoin-Blockchain nach einem `Opret`- oder `Tapret`-Schema aufgenommen und muss alle zu überprüfenden Zustandsänderungen wiedergeben;
- Gleichzeitige Speicherung von mehreren Verträgen in einem einzigen _Commitment_, so dass separate Aktualisierungen für mehrere Vermögenswerte oder RGB-Verträge in einer einzigen Bitcoin-Transaktion verwaltet werden können.

Konkret: Jedes _transition bundle_ gehört zu einem bestimmten Vertrag. Alle diese Informationen werden in einen **MPC-Tree** eingefügt, dessen Wurzel (`mpc::Root`) dann erneut gehasht wird, um das `mpc::Commitment` zu erhalten. Dieser letzte Hash wird in die Bitcoin-Transaktion (_Zeugentransaktion_) eingefügt, je nach der gewählten deterministischen Methode.

![RGB-Bitcoin](assets/en/042.webp)

#### MPC-Root-Hash

Der tatsächlich auf die Kette geschriebene Wert (in `Opret` oder `Tapret`) wird `mpc::Commitment` genannt. Dieser wird in Form von [BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) nach der Formel berechnet:

```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```

wobei :


- `mpc_tag` ist ein Tag: `urn:ubideco:mpc:commitment#2024-01-31`, gewählt nach den [RGB tagging conventions](https://github.com/RGB-WG/rgb-core/blob/master/doc/Commitments.md);
- `depth` (1 Byte) gibt die Tiefe des *MPC Tree* an;
- `cofactor` (16 Bits, in Little Endian) ist ein Parameter, der dazu dient, die Eindeutigkeit der den einzelnen Verträgen zugewiesenen Positionen im Baum zu fördern;
- `mpc::Root` ist die Wurzel des *MPC Tree*, die nach dem im nächsten Abschnitt beschriebenen Verfahren berechnet wird.

![RGB-Bitcoin](assets/en/044.webp)

#### MPC Tree-Konstruktion

Um diesen MPC-Tree zu erstellen, müssen wir sicherstellen, dass jeder Vertrag einer eindeutigen Blattposition entspricht. Nehmen wir an, wir haben :


- `c` einzubeziehende Verträge, indiziert durch `i` aus `i` = {0,1,...,C-1};
- Für jeden Vertrag `c_i` gibt es eine Kennung `ContractId(i) = c_i`.

Dann konstruieren wir einen Baum der Breite `w` und der Tiefe `d`, so dass `2^d = w`, mit `w > C`, so dass jeder Vertrag in einem eigenen _Blatt_ untergebracht werden kann. Die Position `pos(c_i)` jedes Vertrags im Baum wird bestimmt durch :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

wobei "Faktor" eine ganze Zahl ist, die die Wahrscheinlichkeit erhöht, für jeden Vertrag unterschiedliche Positionen zu erhalten. In der Praxis erfolgt die Konstruktion in einem iterativen Prozess:


- Wir beginnen mit einer Mindesttiefe (`d=3`, um die genaue Anzahl der Verträge zu verbergen);
- Wir probieren verschiedene `cofactors` aus (bis zu `w/2`, oder maximal 500 aus Performancegründen);
- Gelingt es uns nicht, alle Verträge kollisionsfrei zu positionieren, erhöhen wir `d` und beginnen erneut.

Ziel ist es, zu hohe Bäume zu vermeiden und gleichzeitig das Kollisionsrisiko so gering wie möglich zu halten. Beachte, dass das Phänomen der Kollision einer zufälligen Verteilungslogik folgt, die mit dem [Geburtstagsparadoxon](https://en.wikipedia.org/wiki/Birthday_problem) zusammenhängt.

#### Genutzte Blätter

Sobald `C` verschiedene Positionen `pos(c_i)` für Verträge `i = {0,1,...,C-1}` ermittelt wurden, wird jedes Blatt mit einer Hash-Funktion (*tagged hash*) gefüllt:

```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```

wobei:


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, wird immer nach den Merkle-Konventionen von RGB gewählt;
- `0x10` kennzeichnet ein _contract leaf_ ;
- `c_i` ist die 32-Byte-Kennung des Vertrags (abgeleitet vom Genesis-Hash);
- `bundleId(c_i)` ist ein 32-Byte-Hash, der die Menge der `Zustandsübergänge` in Bezug auf `c_i` beschreibt (zusammengefasst in einem *transition bundle*).

#### Ungenutzte Blätter

Die verbleibenden Blätter, die keinem Vertrag zugeordnet sind (d.h. `w - C` Blätter), werden mit einem "Dummy"-Wert (_entropy leaf_) gefüllt:

```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```

wobei:


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, wird immer nach den Merkle-Konventionen von RGB gewählt;
- `0x11` kennzeichnet ein _entropy leaf_ ;
- `entropie` ist ein Zufallswert von 64 Bytes Länge, der von der Person, die den Baum erstellt, ausgewählt wird;
- `j` ist die Position (in 32 Bit Little Endian) dieses Blattes in der Baumstruktur.

#### MPC-Knoten

Nach der Generierung der `w`-Blätter (genutzt oder nicht) wird die Merkelisierung durchgeführt. Alle internen Knoten werden wie folgt gehasht:

```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```

wobei:


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, wird immer nach den Merkle-Konventionen von RGB gewählt;
- `b` ist der _branching factor_ (8 Bits). Meistens ist `b=0x02`, weil der Baum binär und vollständig ist;
- `d` ist die Tiefe des Knotens in der Baumstruktur;
- `w` ist die Baumbreite (in 256-Bit Little Endian Binary);
- `tH1` und `tH2` sind die Hashes der Kindknoten (oder Blätter), die bereits wie oben gezeigt berechnet wurden.

Wenn wir auf diese Weise vorgehen, erhalten wir die Wurzel `mpc::Root`. Wir können dann `mpc::Commitment` berechnen (wie oben erklärt) und es in die Blockchain einfügen.

Um dies zu veranschaulichen, stellen wir uns ein Beispiel vor, bei dem `C=3` (drei Verträge) ist. Ihre Positionen werden als `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2` angenommen. Die anderen Blätter (Positionen 0, 1, 3, 5, 6) sind _entropy leafs_. Das folgende Diagramm zeigt die Abfolge der Hashes zur Wurzel mit:


- `BUNDLE_i`, das für `BundleId(c_i)` steht;
- `tH_MPC_LEAF(A)` und so weiter, welche Blätter darstellen (einige für Verträge, andere für Entropie);
- Jeder Zweig `tH_MPC_BRANCH(...)` kombiniert die Hashes seiner beiden Kinder.

Das Endergebnis ist die **mpc::Root**, dann das `mpc::Commitment`.

![RGB-Bitcoin](assets/en/053.webp)

#### MPC Überprüfung

Wenn ein Überprüfer sicherstellen möchte, dass ein `c_i`-Vertrag (und seine `BundleId`) in der endgültigen `mpc::Commitment` enthalten ist, erhält er einfach einen Merkle-Beweis. Dieser Beweis gibt die Knoten an, die benötigt werden, um die Blätter (in diesem Fall das _contract leaf_ von `c_i`) zurück zur Wurzel zu verfolgen. Es besteht keine Notwendigkeit, den gesamten *MPC-Tree* offenzulegen: Dies schützt die Vertraulichkeit anderer Verträge.

Im Beispiel benötigt ein `c_2` Verifier nur einen Zwischenhash (`tH_MPC_LEAF(D)`), zwei `tH_MPC_BRANCH(...)`, den `pos(c_2)` Positionsbeweis und den `cofactor` Wert. Er kann dann lokal die Wurzel rekonstruieren, dann das `mpc::Commitment` neu berechnen und es mit dem in der Bitcoin-Transaktion (innerhalb von `Opret` oder `Tapret`) geschriebenen vergleichen.

![RGB-Bitcoin](assets/en/054.webp)

Dieser Mechanismus gewährleistet, dass:


- Der Status in Bezug auf `c_2` in der Tat in den Gesamtinformationsblock (auf der Client-Seite) aufgenommen wird;
- Niemand eine alternative Historie mit derselben Transaktion erstellen kann, da das On-Chain-_Commitment_ auf eine einzige MPC-Root verweist.

#### Zusammenfassung der MPC-Struktur

Multi Protocol Commitment (MPC) ist das Prinzip, das es RGB ermöglicht, mehrere Verträge in einer einzigen Bitcoin-Transaktion zusammenzufassen, wobei die Einzigartigkeit der Commitments und die Vertraulichkeit gegenüber anderen Teilnehmern gewahrt bleiben. Dank der deterministischen Konstruktion des Baums wird jedem Vertrag eine eindeutige Position zugewiesen, und das Vorhandensein von "Dummy"-Blättern (*Entropy Leaves*) verschleiert teilweise die Gesamtzahl der an der Transaktion beteiligten Verträge.

Der gesamte Merkle-Baum wird niemals auf dem Client gespeichert. Wir erzeugen lediglich einen _Merkle-Pfad_ für jeden betroffenen Vertrag, der an den Empfänger übermittelt wird (der dann die Commitments validieren kann). In einigen Fällen kann man mehrere Vermögenswerte haben, die denselben UTXO durchlaufen haben. In diesem Fall kann man mehrere _Merkle-Pfade_ zu einem so genannten _multi-protocol commitment block_ zusammenfassen, um eine Duplizierung der Daten zu vermeiden.

Jeder _Merkle-Beweis_ ist daher leichtgewichtig, zumal die Baumtiefe in RGB 32 nicht überschreitet. Es gibt auch den Begriff des "Merkle-Blocks", der mehr Informationen enthält (Querschnitt, Entropie usw.), die zum Kombinieren oder Trennen mehrerer branches nützlich sind.

Deshalb hat es auch so lange gedauert, RGB fertigzustellen. Wir hatten die allgemeine Vision von 2019: alles auf die client-side zu verlagern, Token außerhalb der Kette in Umlauf zu bringen. Aber Details wie das Sharding für mehrere Verträge, die Struktur des Merkle-Baums, der Umgang mit Kollisionen und Merge-Beweise... all das erforderte Iterationen.

### Anchor: eine globale Versammlung

Im Anschluss an die Konstruktion unserer Commitments (`Opret` oder `Tapret`) und unseres MPC (*Multi Protocol Commitment*) müssen wir uns mit dem Begriff **Anchor** (Anker) im RGB-Protokoll befassen. Ein Anchor ist eine client-side validierte Struktur, die die Elemente zusammenfasst, die erforderlich sind, um zu überprüfen, ob ein Bitcoin-Commitment tatsächlich spezifische vertragliche Informationen enthält. Mit anderen Worten, ein Anchor fasst alle Daten zusammen, die benötigt werden, um die oben beschriebenen _Commitments_ zu validieren.

Ein Anker besteht aus drei geordneten Feldern:


- `Txid`
- `MPC-Proof`
- Extra-Transaktionsnachweis - ETP

Jedes dieser Felder spielt eine Rolle im Validierungsprozess, egal ob es darum geht, die zugrunde liegende Bitcoin-Transaktion zu rekonstruieren oder das Vorhandensein eines versteckten Commitments nachzuweisen (insbesondere im Fall von `Tapret`).

#### TxId

Das `Txid`-Feld entspricht dem 32-Byte-Identifikator der Bitcoin-Transaktion, die das `Opret`- oder `Tapret`-Commitment enthält.

Theoretisch wäre es möglich, diese `Txid` zu finden, indem man die Kette der Zustandsübergänge zurückverfolgt, die ihrerseits auf jede Zeugentransaktion verweisen, entsprechend der Logik von Single-use Seals. Um jedoch die Überprüfung zu erleichtern und zu beschleunigen, wird diese `Txid` einfach in den Anchor aufgenommen, so dass der Prüfer nicht die gesamte Off-Chain-Historie zurückverfolgen muss.

#### MPC-Proof

Das zweite Feld, `MPC-Proof`, bezieht sich auf den Nachweis, dass dieser bestimmte Vertrag (z.B. `c_i`) in dem _Multi Protocol Commitment_ enthalten ist. Es ist eine Kombination aus:


- `pos_i`, die Position dieses Vertrags in der MPC-Struktur;
- `cofaktor`, der zur Auflösung von Positionskollisionen definierte Wert;
- dem `Merkle-Beweis`, d.h. die Menge der Knoten und Hashes, die verwendet werden, um die MPC-Root zu rekonstruieren und zu überprüfen, ob die Vertragskennung (`Txid`) und ihr `transition bundle` an diese Wurzel gebunden sind.

Dieser Mechanismus wurde im vorherigen Abschnitt über den Aufbau des *MPC-Tree* beschrieben, bei dem jeder Vertrag wegen:

```txt
pos(c_i) = c_i mod (w - cofactor)
```
einem eindeutigen Blatt zugeordnet wird.

Dann wird ein deterministisches Merkelisierungs-Schema verwendet, um alle Blätter zu aggregieren (Verträge + Entropie). Am Ende ermöglicht der `MPC-Proof` die lokale Rekonstruktion der Wurzel und den Vergleich mit dem in der Blockchain enthaltenen `MPC::Commitment`.

#### Extra-Transaktionsnachweis - ETP

Das dritte Feld, das **ETP**, hängt von der Art des verwendeten Commitments ab. Wenn das Commitment vom Typ `Opret` ist, ist kein zusätzlicher Nachweis erforderlich. Der Prüfer prüft den ersten `OP_RETURN`-Output der Transaktion und findet dort direkt das `mpc::Commitment`.

**Wenn das Commitment vom Typ `Tapret`** ist, muss ein zusätzlicher Nachweis, der *Extra Transaction Proof - ETP*, erbracht werden. Er enthält:


- Den internen öffentlichen Schlüssel (`P`) des taproot-Output, in den das *Commitment* eingebettet ist;
- Die Partnerknoten des `Script Path Spend` (wenn das Tapret *Commitment* in ein Script eingefügt wird), um die genaue Position dieses Scripts im Tapret-Baum nachzuweisen:
- Falls sich das `Tapret`-*Commitment* auf dem rechten Zweig befindet, wird der linke Knoten aufgedeckt (z. B. `tHABC`),
- Falls sich das `Tapret`-*Commitment* auf der linken Seite steht, muss man 2 Knoten (z.B. `tHAB` und `tHC`) offenlegen, um zu beweisen, dass kein anderes *Commitment* auf der rechten Seite vorhanden ist.
- Die `Nonce` kann verwendet werden, um die beste Konfiguration zu "minen", so dass das *Commitment* auf der rechten Seite des Baumes platziert werden kann (Optimierung des Beweises).

Dieser zusätzliche Nachweis ist unerlässlich, da im Gegensatz zu `Opret` die `Tapret`-Verpflichtung in die Struktur eines Taproot-Scripts integriert ist, was die Offenlegung eines Teils des Taproot-Baums erfordert, um den Ort des *Commitments* korrekt zu validieren.

![RGB-Bitcoin](assets/en/045.webp)

Die **Anchor** kapseln daher alle Informationen, die für die Validierung eine Bitcoin-Commitments im Kontext von RGB erforderlich sind. Sie geben sowohl die relevante Transaktion (`Txid`) als auch den Nachweis der Vertragspositionierung (`MPC-Proof`) an, während sie den zusätzlichen Nachweis (`ETP`) im Falle von `Tapret` verwalten. Auf diese Weise schützt ein Anchor die Integrität und Einzigartigkeit des Off-Chain-Status, indem er sicherstellt, dass dieselbe Transaktion nicht für andere Vertragsdaten umgedeutet werden kann.

### Schlussfolgerung

In diesem Kapitel behandelten wir:


- Wie man das Konzept der Single-use Seals in Bitcoin anwendet (insbesondere über einen _Outpoint_);
- Die verschiedenen Methoden zum deterministischen Einfügen eines _Commitment_ in eine Transaktion (Sig tweak, Key tweak, witness tweak, op_return, Taproot/Tapret) ;
- Die Gründe, warum RGB sich auf Tapret-Commitments konzentriert;
- Verwaltung mehrerer Verträge über _multi-protocol commitments_, die unerlässlich sind, wenn man nicht den gesamten Zustand oder andere Verträge offenlegen will, wenn man einen bestimmten Punkt beweisen will;
- Wir haben auch die Rolle von _Anchor_ gesehen, die alles in einem einzigen Paket zusammenfassen (Transaktions-TXID, Merkle-Baum-Beweis und Taproot-Beweis).

In der Praxis ist die technische Umsetzung auf mehrere dedizierte Rust _crates_ verteilt (in _client_side_validation_, _commit-verify_, _bp_core_, etc.). Die grundlegenden Begriffe sind vorhanden:

![RGB-Bitcoin](assets/en/046.webp)

Im nächsten Kapitel werden wir uns mit der reinen Off-Chain-Komponente von RGB beschäftigen, nämlich der Vertragslogik. Wir werden sehen, wie RGB-Verträge, die als teilweise replizierte _finite state machines_ organisiert sind, eine viel höhere Ausdruckskraft als Bitcoin-Skripte erreichen, während sie die Vertraulichkeit ihrer Daten bewahren.

## Einführung in Smart Contracts und ihre Zustände

<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

:::video id=db4ee09f-1352-4ad1-9f7a-c962df7ea9fa:::

In diesem und dem nächsten Kapitel werden wir uns mit dem Begriff des **Smart Contracts** (Intelligenter Vertrag) im der RGB-Kontext befassen und die verschiedenen Möglichkeiten untersuchen, wie diese Verträge ihren *Zustand* definieren und weiterentwickeln können. Wir werden sehen, warum die RGB-Architektur unter Verwendung der geordneten Abfolge von Single-use Seals die Ausführung verschiedener Arten von ***Vertragsoperationen*** auf skalierbare Weise und ohne den Umweg über eine zentralisierte Registrierung ermöglicht. Wir werden auch die grundlegende Rolle der ***Business Logic*** bei der Entwicklung des Vertragsstatus betrachten.

### Smart Contracts und digitale Inhaberrechte

Das Ziel von RGB ist es, eine Infrastruktur für die Implementierung von Smart Contracts auf Bitcoin bereitzustellen. Mit "Smart Contract" meinen wir eine Vereinbarung zwischen mehreren Parteien, die automatisch und rechnerisch durchgesetzt wird, ohne dass ein Mensch eingreift, um die Klauseln durchzusetzen. Mit anderen Worten, das Recht des Vertrages wird von Software durchgesetzt, nicht von einer vertrauenswürdigen dritten Partei.

Diese Automatisierung wirft die Frage der Dezentralisierung auf: Wie können wir uns von einem zentralen Register (z.B. einer zentralen Plattform oder Datenbank) befreien, um Eigentum und Vertragserfüllung zu verwalten? Die ursprüngliche Idee, die von RGB aufgegriffen wurde, besteht darin, zu einer Eigentumsform zurückzukehren, die als "Inhaberpapiere" bekannt ist. In der Vergangenheit wurden bestimmte Wertpapiere (Anleihen, Aktien usw.) als Inhaberpapiere ausgegeben, so dass jeder, der das Dokument physisch besaß, seine Rechte geltend machen konnte.

![RGB-Bitcoin](assets/en/055.webp)

RGB wendet dieses Konzept auf die digitale Welt an: Rechte (und Pflichten) werden in Daten gekapselt, die off-chain bearbeitet werden, und der Status dieser Daten wird von den Teilnehmern selbst validiert. Dies ermöglicht von vornherein ein viel höheres Maß an Vertraulichkeit und Unabhängigkeit als bei anderen Ansätzen, die auf öffentlichen Registern basieren.

### Einführung in den Smart Contract RGB-Status

Ein Smart Contract in RGB kann als ein Zustandsautomat betrachtet werden, der definiert ist durch:


- Einen **Zustand**, d.h. den Satz von Informationen, der die aktuelle Konfiguration des Vertrags widerspiegelt;
- Eine **Business Logic** (eine Reihe von Regeln), die beschreibt, unter welchen Bedingungen und von wem der Zustand geändert werden kann.

![RGB-Bitcoin](assets/en/056.webp)

Es ist wichtig zu verstehen, dass diese Verträge nicht auf die einfache Übertragung von Token beschränkt sind. Sie können eine Vielzahl von Anwendungen umfassen: von traditionellen Vermögenswerten (Token, Aktien, Anleihen) bis hin zu komplexeren Mechanismen (Nutzungsrechte, Handelsbedingungen usw.). Im Gegensatz zu anderen Blockchains, bei denen der Vertragscode für alle zugänglich und ausführbar ist, ist der Zugang und das Wissen über den Vertrag beim RGB-Ansatz auf die Teilnehmer ("***Vertragsteilnehmer***") beschränkt. Es gibt mehrere Rollen:


- Der **Emittent** oder Ersteller des Kontrakts, der die Genesis des Vertrags und seine Anfangsvariablen definiert;
- *Parteien mit Rechten** (*Eigentum*) oder anderen Durchsetzungsmöglichkeiten;
- **Beobachter**, die möglicherweise nur bestimmte Informationen sehen können, aber keine Änderungen vornehmen können.

Diese Rollentrennung trägt zur Zensurresistenz bei, da sie sicherstellt, dass nur autorisierte Personen mit dem Vertrags-Zustand interagieren können. Sie gibt RGB auch die Möglichkeit, horizontal zu skalieren: Die meisten Validierungen finden außerhalb der Blockchain statt, und nur die kryptografischen Anker (die *Commitments*) sind in Bitcoin festgeschrieben.

### Status und Business Logic in RGB

Praktisch gesehen besteht die **Business Logic** des Vertrags aus Regeln und Skripten, die in einem, wie RGB es nennt, **Schema** definiert sind. Das Schema kodiert:


- Zustandsstruktur (welche Felder sind öffentlich? Welche Felder sind im Besitz von welchen Parteien?)
- Gültigkeitsbedingungen (was muss geprüft werden, bevor eine Zustandsaktualisierung genehmigt wird?);
- Befugnisse (wer kann einen Zustandsübergang (*State Transition*) einleiten? Wer kann nur beobachten?).

Zugleich zerfällt der **Vertragszustand** häufig in zwei Komponenten:


- Ein **Global State**: öffentlicher Teil, der potenziell von allen beobachtet werden kann (je nach Konfiguration);
- **Owned States**: private Teile, die über UTXOs, auf die in der Business Logic verwiesen wird, speziell den Eigentümern zugewiesen werden.

Wie wir in den folgenden Kapiteln sehen werden, muss jeder Zustandsübergang (*Vertragsoperation*) an ein Bitcoin _commitment_ andocken (via `Opret` oder `Tapret`) und den *Business Logic* Skripten entsprechen, um als gültig zu gelten.

### Vertragsoperationen: Erzeugung und Entwicklung des Zustands

Im RGB-Universum ist eine ***Vertragsoperation*** jedes Ereignis, das den Vertrag von einem **alten Zustand** in einen **neuen Zustand** versetzt. Diese Operationen folgen der folgenden Logik:


- Wir nehmen den aktuellen Zustand des Vertrages zur Kenntnis;
- Wir wenden die Regel oder Operation an (einen ***Zustandsübergang***, eine ***Genesis***, wenn es sich um den allerersten Zustand handelt, oder eine ***Zustandserweiterung*** (State Extension), wenn es eine öffentliche *Valenz* zum erneuten Auslösen (re-trigger) gibt);
- Wir verankern die Änderung durch ein neues _Commitment_ auf der Blockchain, schließen ein _Single-use Seal_ und erstellen ein weiteres;
- Die betroffenen Rechteinhaber validieren lokal (*client-side*), dass der Übergang dem *Schema* entspricht und dass die zugehörige Bitcoin-Transaktion auf der Kette registriert ist.

![RGB-Bitcoin](assets/en/057.webp)

Das Endergebnis ist ein aktualisierter Vertrag, der nun einen anderen Zustand hat. Dieser Übergang erfordert nicht, dass sich das gesamte Bitcoin-Netzwerk mit den Details befasst, da nur ein kleiner kryptographischer Fingerabdruck (das _Commitment_) in der Blockchain aufgezeichnet wird. Die Abfolge von Single-Use-Seals verhindert eine doppelte Ausgabe oder eine doppelte Verwendung des Zustands.

### Operationskette: von der Genesis bis zum Endzustand

Um dies zu verdeutlichen, beginnt ein RGB-Smart Contract mit einer **Genesis**, dem allerersten Zustand. Danach folgen verschiedene Vertragsoperationen aufeinander und bilden einen [DAG](https://planb.academy/resources/glossary/directed-acyclic-graph) (*Directed Acyclic Graph*) aus Operationen:


- Jeder Übergang basiert auf einem vorhergehenden Zustand (oder mehreren, im Falle von konvergenten Übergängen);
- Die chronologische Reihenfolge wird durch die Aufnahme jedes Übergangs in einen Bitcoin-Anker garantiert, der mit einem Zeitstempel versehen und dank des Konsens durch Proof-of-Work unveränderlich ist;
- Wenn keine Operationen mehr laufen, wird ein **Endzustand** erreicht: der letzte und vollständige Zustand des Vertrags.

![RGB-Bitcoin](assets/en/012.webp)

Diese DAG-Topologie (anstelle einer einfachen linearen Kette) spiegelt die Möglichkeit wider, dass sich verschiedene Teile des Vertrags parallel entwickeln können, solange sie sich nicht gegenseitig widersprechen. RGB sorgt dann für die Vermeidung von Inkonsistenzen durch *client-side* Überprüfung jedes beteiligten Teilnehmers.

### Zusammenfassung

Smart Contracts in RGB führen ein Modell von digitalen Inhaberinstrumenten ein, die dezentralisiert, aber in Bitcoin verankert sind, um die Zeitstempel und die Reihenfolge der Transaktionen zu garantieren. Die automatisierte Ausführung dieser Verträge basiert auf:


- Einem **Vertragszustand**, der die aktuelle Konfiguration des Vertrags (Rechte, Salden, Variablen usw.) angibt;
- Eine **Business Logic** (*Schema*), die festlegt, welche Übergänge zulässig sind und wie sie validiert werden müssen;
- **Vertragsoperationen**, die diesen Zustand dank der in Bitcoin-Transaktionen verankerten Verpflichtungen Schritt für Schritt aktualisieren.

Im nächsten Kapitel werden wir auf die konkrete Darstellung dieser ***Zustände*** und ***Zustandsübergänge*** auf der Off-Chain-Ebene eingehen und wie sie mit den in Bitcoin eingebetteten UTXOs und Single-use Seals zusammenhängen. Dies wird eine Gelegenheit sein, zu sehen, wie die internen Mechanismen von RGB, die auf client-side Validierung basieren, die Konsistenz von Smart Contracts aufrechterhalten und gleichzeitig die Vertraulichkeit der Daten bewahren.

## RGB-Vertragsoperationen

<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

:::video id=1caec34d-f214-425b-a1a4-0a40ae7d3e0e:::

In diesem Kapitel werden wir uns ansehen, wie Operationen in Smart Contracts und Zustandsübergänge funktionieren, wiederum innerhalb des RGB-Protokolls. Ziel ist es auch zu verstehen, wie mehrere Teilnehmer zusammenarbeiten, um das Eigentum an einem Vermögenswert zu übertragen.

### Zustandsübergänge und ihre Mechanik

Das allgemeine Prinzip ist immer noch das der client-side Validierung, bei der die Zustandsdaten vom Eigentümer gehalten und vom Empfänger validiert werden. Die Besonderheit bei RGB liegt jedoch darin, dass Bob als Empfänger Alice bittet, bestimmte Informationen in die Vertragsdaten aufzunehmen, um über einen versteckten Verweis auf einen seiner UTXOs die tatsächliche Kontrolle über den erhaltenen Vermögenswert zu haben.

Zur Veranschaulichung des Prozesses eines *Zustandsübergangs* (der eine der grundlegenden ***Vertragsoperationen*** in RGB ist), untersuchen wir ein Beispiel einer Vermögensübertragung zwischen Alice und Bob Schritt-für-Schritt:

**Ausgangssituation:**

Alice hat einen ***stash RGB*** mit lokal validierten Daten (*client-side*). Dieser Stash bezieht sich auf eineng ihrer UTXOs auf Bitcoin. Das bedeutet, dass eine _Siegeldefinition_ in diesen Daten auf einen UTXO verweist, der Alice gehört. Sie soll in die Lage versetzt werden, bestimmte digitale Rechte in Verbindung mit einem Vermögenswert (z.B. RGB-Token) an Bob zu übertragen.

![RGB-Bitcoin](assets/en/058.webp)

**Bob hat auch UTXOs:**

Bob hingegen verfügt über mindestens einen eigenen UTXO, der nicht direkt mit dem von Alice verbunden ist. Falls Bob keinen UTXO hat, ist es immer noch möglich, die Übertragung an ihn mit Hilfe der *Zeugentransaktion* selbst vorzunehmen: Der Output dieser Transaktion enthält dann die Verpflichtung (_Commitment_) und ordnet das Eigentum an dem neuen Vertrag implizit Bob zu.

![RGB-Bitcoin](assets/en/059.webp)

**Erstellen der neuen Eigentumsverhältnisse (*Neuer Zustand*):**

Bob sendet Alice Informationen in Form einer ***Rechnung*** (auf den Aufbau von Rechnungen werden wir in späteren Kapiteln näher eingehen) und bittet sie, einen neuen Zustand zu erzeugen, der den Regeln des Vertrags entspricht. Dieser Zustand wird eine neue *Siegeldefinition* enthalten, die auf einen von Bobs UTXOs verweist. Auf diese Weise erhält Bob das Eigentum an den in diesem neuen Zustand definierten Vermögenswerten, z.B. eine bestimmte Menge an RGB-Tokens.

![RGB-Bitcoin](assets/en/060.webp)

**Vorbereitung der Beispiel-Transaktion:**

Alice erstellt dann eine Bitcoin-Transaktion, die den UTXO ausgibt, auf den im vorherigen Siegel verwiesen wurde (das sie als Inhaberin legitimiert hat). Im Output dieser Transaktion wird ein *Commitment* (via `Opret` oder `Tapret`) eingefügt, um den neuen RGB-Zustand zu verankern. Die `Opret`- oder `Tapret`-Commitments werden von einem *MPC-Tree* abgeleitet (wie in den vorangegangenen Kapiteln beschrieben), der mehrere Übergänge aus verschiedenen Verträgen zusammenfassen kann.

**Übermittlung des *Consignment* an Bob:**

Vor der Veröffentlichung der Transaktion sendet Alice an Bob ein ***Consignment***, das alle erforderlichen Daten auf der *client-side* (seinen *Stash*) und die neuen Zustandsinformationen zu Bobs Gunsten enthält. Zu diesem Zeitpunkt wendet Bob die RGB-Konsensregeln an:


- Es überprüft alle in dem *Consignment* enthaltenen RGB-Daten, einschließlich des neuen Zustands, der ihm das Eigentum an dem Vermögenswert verleiht;
- Anhand der *Anchor*, die in dem *Consignment* enthalten sind, überprüft es die Chronologie der Zeugentransaktionen (von der Genesis bis zum jüngsten Übergang) und validiert die entsprechenden Commitments in der Blockchain.

**Abschluss des Zustandsübergangs:**

Wenn Bob zufrieden ist, kann er seine Zustimmung geben (z. B. durch Unterzeichnung des *Consignment*). Alice kann dann die vorbereitete Beispielransaktion veröffentlichen. Sobald sie bestätigt ist, wird das Siegel, das zuvor von Alice gehalten wurde, geschlossen und das Eigentum von Bob formalisiert. Die Sicherheit gegen Doppelausgaben basiert dann auf demselben Mechanismus wie bei Bitcoin: Der UTXO wird ausgegeben, was beweist, dass Alice ihn nicht mehr wiederverwenden kann.

![RGB-Bitcoin](assets/en/061.webp)

Der neue Zustand verweist nun auf Bobs UTXO, wodurch Bob das Eigentum erhält, das zuvor bei Alice lag. Der Bitcoin-Output, in dem die RGB-Daten verankert sind, wird zum unwiderruflichen Beweis für den Eigentumsübergang.

Ein Beispiel für einen minimalen DAG (*Directed Acyclic Graph*), der zwei Vertragsoperationen umfasst (eine **Genesis** und einen ***State Transition***), kann veranschaulichen, wie der RGB-Zustand (*client-side* Schicht, in rot) mit der Bitcoin-Blockchain (*Commitment* Schicht, in orange) verbunden ist.

![RGB-Bitcoin](assets/en/062.webp)

Es zeigt, dass eine Genesis ein Siegel definiert (*Siegeldefinition*), dann schließt ein *Zustandsübergang* dieses Siegel, um ein neues in einem anderen UTXO zu schaffen.

In diesem Zusammenhang einige Hinweise zur Terminologie:


- Eine ***Zuweisung*** kombiniert:
    - Eine ***Siegeldefinition*** (die auf einen UTXO verweist);
    - **Owned States**, d. h. Daten, die mit dem Besitz verbunden sind (z.B. die Menge der übertragenen Token).
- Ein **Global State** fasst die allgemeinen Eigenschaften des Vertrags zusammen, die für alle sichtbar sind und die globale Konsistenz der Entwicklungen gewährleisten.

**Zustandsübergänge**, die im vorigen Kapitel beschrieben wurden, sind die Hauptform der Vertragsoperationen. Sie beziehen sich auf einen oder mehrere frühere Zustände (aus Genesis oder einem anderen Zustandsübergang) und aktualisieren sie zu einem neuen Zustand.

![RGB-Bitcoin](assets/en/063.webp)

Dieses Diagramm zeigt, wie in einem *State Transition Bundle* mehrere Siegel in einer einzigen Beispieltransaktion geschlossen werden können, während gleichzeitig neue Siegel geöffnet werden. Ein interessantes Merkmal des RGB-Protokolls ist seine Skalierbarkeit: Mehrere Zustandsübergänge können zu einem State Transition Bundle zusammengefasst werden, wobei jede Zusammenfassung mit einem bestimmten Blatt des *MPC-Tree* (einem eindeutigen Bundle Identifier) verbunden ist. Dank des *Deterministic Bitcoin Commitment* (DBC)-Mechanismus wird die gesamte Nachricht in eine `Tapret`- oder `Opret`-Ausgabe eingefügt, wobei vorherige Siegel geschlossen und möglicherweise neue definiert werden. Der `Anchor` dient als direkte Verbindung zwischen dem in der Blockchain gespeicherten Commitment und der client-side Validierungsstruktur (*client-side*).

In den folgenden Kapiteln werden wir uns alle Komponenten und Prozesse ansehen, die an der Erstellung und Validierung eines Zustandsübergangs beteiligt sind. Die meisten dieser Elemente sind Teil des RGB-Konsenses, der in der **RGB Core Library** implementiert ist.

### Transition Bundle

Bei RGB ist es möglich, verschiedene Zustandsübergänge zu bündeln, die zum selben Vertrag gehören (d.h. dieselbe **ContractId** haben, abgeleitet von der Genesis **OpId**). Im einfachsten Fall, wie zwischen Alice und Bob im obigen Beispiel, enthält ein **Transition Bundle** nur einen Übergang. Die Unterstützung von Multi-Payer-Operationen (wie z.B. [Coinjoins](https://planb.academy/resources/glossary/coinjoin), Lightning-Channel-Öffnungen, etc.) bedeutet jedoch, dass mehrere Nutzer ihre Zustandsübergänge in einem einzigen Bundle zusammenfassen können.

Einmal gesammelt, werden diese Übergänge (durch den MPC + DBC-Mechanismus) in einer einzigen Bitcoin-Transaktion verankert:


- Jeder Zustandsübergang wird gehasht und in einem Transition Bundle gruppiert;
- Das Transition Bundle selbst wird gehasht und in das diesem Vertrag entsprechende MPC-Blatt (eine BundleId) eingefügt;
- Der MPC-Tree wird schließlich über `Opret` oder `Tapret` in die Zeugentransaktion eingebunden, die damit die verbrauchten Siegel schließt und die neuen Siegel definiert.

Technisch gesehen wird die **BundleId**, die in das MPC-Blatt eingefügt wird, aus einem getaggten Hash gewonnen, der auf die strenge Serialisierung des Feldes *InputMap* des Bundles angewendet wird:

```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```

In dem zum Beispiel `bundle_tag = urn:lnp-bp:rgb:bundle#2024-02-03`.

Die *InputMap* ist eine Datenstruktur, die für jeden Eingang `i` der Beispieltransaktion den Verweis auf die *OpId* des entsprechenden Zustandsübergangs auflistet. Zum Beispiel:

```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
                       |_________________________| |_________________________|  ...  |___________________________|
                                MapElement1                MapElement2                       MapElementN
```


- `N` ist die Gesamtzahl der Einträge in der Transaktion, die sich auf eine `OpId` beziehen;
- `opId(input_j)` ist die Vorgangskennung eines der im Bündel vorhandenen Zustandsübergänge.

Indem wir jeden Eintrag nur einmal und in geordneter Weise referenzieren, verhindern wir, dass dasselbe Siegel zweimal in zwei gleichzeitigen Zustandsübergängen ausgegeben wird.

### Zustandserzeugung und aktiver Zustand

Zustandsübergänge können daher verwendet werden, um das Eigentum an einem Vermögenswert von einer Person auf eine andere zu übertragen. Sie sind jedoch nicht die einzigen möglichen Operationen im RGB-Protokoll. Das Protokoll definiert drei **Vertragsoperationen**:


- **Zustandsübergang**;
- **Genesis**;
- **Zustandserweiterung**.

Unter diesen werden **Genesis** und **Zustandserweiterung** manchmal als "*State Generation operations*" bezeichnet, weil sie neue Zustände erzeugen, ohne sofort einen zu schließen. Dies ist ein sehr wichtiger Punkt: **Genesis** und **Zustandserweiterung** beinhalten nicht das Schließen eines Siegels. Vielmehr definieren sie ein neues Siegel, das dann durch eine nachfolgende **State Transition** ausgegeben werden muss, um in der Blockchain-Historie wirklich validiert zu werden.

![RGB-Bitcoin](assets/en/064.webp)

Der **Aktive Zustand** eines Vertrages wird oft als die Menge der letzten Zustände definiert, die sich aus der Historie (der DAG) der Transaktionen ergeben, beginnend mit der Genesis und danach allen Ankern in der Bitcoin-Blockchain. Alle alten Zustände, die bereits veraltet (d.h. an verbrauchten UTXOs angehängt) sind, werden nicht mehr als aktiv betrachtet, bleiben aber für die Überprüfung der Konsistenz der Historie wichtig.

### Genesis

Die Genesis ist der Ausgangspunkt eines jeden RGB-Vertrags. Sie wird vom Emittenten des Vertrags erstellt und definiert die Anfangsparameter in Übereinstimmung mit dem **Schema**. Im Falle eines RGB-Tokens kann die Genesis z. B. angeben:


- Die Anzahl der ursprünglich erstellten Token und deren Besitzer;
- Mögliche Emissionsobergrenze insgesamt;
- Alle Regeln für die Neuausgabe und welche Teilnehmer in Frage kommen.

Da es sich um die erste Transaktion im Vertrag handelt, verweist die Genesis weder auf einen früheren Zustand noch schließt sie ein Siegel. Um jedoch in der Historie zu erscheinen und validiert zu werden, muss die Genesis durch einen ersten Zustandsübergang **verbraucht** (geschlossen) werden (oft eine Scan-/Auto-Spend-Transaktion an den Emittenten selbst oder die Erstverteilung an die Nutzer).

### Zustandserweiterung

**Zustandserweiterungen** bieten eine neuartige Funktion für Smart Contracts. Sie ermöglichen es, bestimmte in der Vertragsdefinition vorgesehene digitale Rechte (*Valenzen*) einzulösen, ohne das Siegel sofort zu schließen. Am häufigsten betrifft dies:


- Verteilte Tokenausgaben;
- Mechanismen zum Tausch von Vermögenswerten;
- Bedingte Neuausstellungen (die die Zerstörung anderer Vermögenswerte usw. beinhalten können).

Technisch gesehen verweist eine Zustandserweiterung auf ein *Redeem* (eine bestimmte Art von RGB-Input), das einer *Valency* entspricht, die zuvor definiert wurde (zum Beispiel in Genesis oder einem anderen Zustandsübergang). Sie definiert ein neues Siegel, das der Person oder dem Zustand zur Verfügung steht, dem es zugute kommt. Damit dieses Siegel wirksam wird, muss es durch einen nachfolgenden Zustandsübergang ausgegeben werden.

![RGB-Bitcoin](assets/en/065.webp)

Ein Beispiel: Die Genesis schafft ein Recht auf Ausgabe (*Valency*). Dieses kann von einem autorisierten Akteur ausgeübt werden, der dann eine Zustandserweiterung errichtet:


- Sie bezieht sich auf die Valenz (redeem);
- Es wird eine neue *Zuweisung* (neue *Owned State* Daten) erstellt, die auf einen UTXO zeigt;
- Ein zukünftiger Zustandsübergang, ausgestellt vom Besitzer dieses neuen UTXO, wird die neu ausgegebenen Token tatsächlich übertragen oder verteilen.

### Komponenten einer Vertragsoperation

Ich möchte nun einen detaillierten Blick auf die einzelnen Bestandteile einer **Vertragsoperation** in RGB werfen. Eine Vertragsoperation ist eine Aktion, die den Zustand eines Vertrags ändert und die auf der client-side auf deterministische Weise vom rechtmäßigen Empfänger validiert wird. Wir werden insbesondere sehen, wie die Vertragsoperation einerseits den **alten Zustand** (*Old State*) des Vertrags und andererseits die Definition eines **neuen Zustands** (*New State*) berücksichtigt.

```txt
               +---------------------------------------------------------------------------------------------------------------------+
               |  Contract Operation                                                                                                 |
               |                                                                                                                     |
               |  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
               |  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
               |  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
               |                                                                                                                     |
               |  +-----------------------------------------------+  +------------------------------------------------------------+  |
               |  | Metadata                                      |  | Global State                                               |  |
               |  |                                               |  | +----------------------------------+                       |  |
               |  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
               |  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
               |  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
               |  |                                               |  | +----------------------------------+                       |  |
               |  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
               |                                                                                                                     +---------> OpId |
               |  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
               |  | Inputs                                        |  | Assignments                                                |  |
               |  |                                               |  |                                                            |  |
               |  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
               |  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
               |  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
               |  |                                               |  |                                                            |  |
               |  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
               |  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
               |  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
               |  |                                               |  |                                                            |  |
               |  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
               |  |                                               |  |                                                            |  |
               |  +-----------------------------------------------+  +------------------------------------------------------------+  |
               |                                                                                                                     |
               |  +-----------------------------------------------+  +------------------------------------------------------------+  |
               |  | Redeems                                       |  | Valencies                                                  |  |
               |  |                                               |  |                                                            |  |
               |  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
               |  | +------------------------------+              |  |                                                            |  |
               |  |                                               |  |                                                            |  |
               |  +-----------------------------------------------+  +------------------------------------------------------------+  |
               |                                                                                                                     |
               +---------------------------------------------------------------------------------------------------------------------+
```

Aus dem obigen Diagramm geht hervor, dass eine Vertragsoperation Elemente enthält, die sich auf den **Neuen Zustand** beziehen, und andere, die sich auf den aktualisierten **Alten Zustand** beziehen.

Die Elemente des **Neuen Zustands** sind :


- **Zuweisungen**, in denen definiert sind:
 - Die **Siegeldefinition**;
 - Der **Owned State**.
- Der **Global State**, der verändert oder angereichert werden kann;
- **Valenzen**, möglicherweise definiert in einem Zustandsübergang oder einer Genesis.

Der **Alte Zustand** wird referenziert über:


- **Inputs**, die auf *Zuweisungen* früherer Zustandsübergänge verweisen (in Genesis nicht vorhanden);
- **Redeems**, die sich auf zuvor definierte Valenzen beziehen (nur in State Extensions).

Darüber hinaus enthält eine Vertragsoperation allgemeinere, für den Vorgang spezifische Felder:


- `ffv` (*Fast-Forward-Version*): 2-Byte-Ganzzahl zur Angabe der Vertragsversion;
- `transitionType` oder `ExtensionType`: 16-Bit-Ganzzahl zur Angabe des Übergangs- oder Erweiterungstyps, je nach Business Logic;
- `ContractId`: 32-Byte-Zahl, die sich auf die *OpId* der Vertrags-Genesis bezieht. Enthalten in Transitions und Extensions, aber nicht in Genesis;
- schemaId: nur in Genesis vorhanden; dies ist der 32-Byte-Hash, der die Struktur (*Schema*) des Vertrags darstellt;
- `testnet`: Boolescher Wert, der angibt, ob Sie sich im Testnet- oder Mainnet-Netzwerk befinden. Nur Genesis;
- `altlayers1`: Variable zur Identifizierung der alternativen Schicht (Sidechain oder andere), die zur Verankerung von Daten zusätzlich zu Bitcoin verwendet wird. Nur in Genesis vorhanden;
- `metadata`: Feld, in dem temporäre Informationen gespeichert werden können, die für die Validierung eines komplexen Vertrags nützlich sind, aber nicht in den endgültigen Zustandsverlauf aufgenommen werden dürfen.

Schließlich werden alle diese Felder durch ein individuelles Hashing-Verfahren verdichtet, um einen eindeutigen Fingerabdruck, die `OpId`, zu erzeugen. Diese `OpId` wird dann in das Transition Bundle integriert, damit es innerhalb des Protokolls authentifiziert und validiert werden kann.

Jeder *Vertragsoperation* wird daher durch einen 32-Byte-Hash mit der Bezeichnung `OpId` identifiziert. Dieser Hash wird durch einen SHA256-Hash aller Elemente, aus denen der Vorgang besteht, berechnet. Mit anderen Worten: Jede *Vertragsoperation* hat ih eigenes kryptografisches Comittment, das alle Daten enthält, die zur Überprüfung der Authentizität und Konsistenz der Operation erforderlich sind.

Ein RGB-Vertrag wird dann durch eine `ContractId` identifiziert, die von der Genesis `OpId` abgeleitet ist (da es keine Operation vor Genesis gibt). Konkret nehmen wir die Genesis-`OpId`, kehren die Byte-Reihenfolge um und wenden eine Base58-Kodierung an. Diese Kodierung macht die `ContractId` einfacher zu handhaben und zu erkennen.

### Methoden und Regeln für die Zustandsaktualisierung

Der **Vertrag-Zustand** stellt die Menge der Informationen dar, die das RGB-Protokoll für einen bestimmten Vertrag verfolgen muss. Er besteht aus :


- **Einem einzigen Global State**: Dies ist der öffentliche, globale Teil des Vertrags, der für alle sichtbar ist;
- **Ein oder mehrere Owned States**: Jeder Owned State ist mit einem einzigartigen Siegel (und damit einem UTXO auf Bitcoin) verbunden. Es wird unterschieden zwischen:
    - Den **öffentlichen** Owned States,
    - Den **privaten** Owned States.

![RGB-Bitcoin](assets/en/066.webp)

Der *Global State* ist direkt in der *Vertragsoperation* als einzelner Block enthalten. Die *Owned States* werden in jeder *Zuweisung* definiert, zusammen mit der *Siegeldefinition*.

Ein wichtiges Merkmal von RGB ist die Art und Weise, wie der Global State und die Owned States geändert werden. Im Allgemeinen gibt es zwei Arten von Verhalten:


- **Veränderlich**: Wenn ein Zustandselement als veränderlich beschrieben wird, ersetzt jede neue Operation den vorherigen Zustand durch einen neuen Zustand. Die alten Daten werden dann als veraltet betrachtet;
- **Akkumulierend**: Wenn ein Zustandselement als akkumulierend definiert ist, fügt jede neue Operation neue Informationen zum vorherigen Zustand hinzu, ohne diesen zu überschreiben. Das Ergebnis ist eine Art akkumulierte Geschichte.

Wenn ein Zustandselement im Vertrag nicht als veränderbar oder kumulativ definiert ist, bleibt dieses Element bei nachfolgenden Operationen leer (mit anderen Worten, es gibt keine neuen Versionen für dieses Feld). Es ist das Vertragsschema (d.h. die kodierte Business Logic), das bestimmt, ob ein Zustand (Global oder Owned) veränderbar, kumulativ oder fix ist. Nach der Definition der Genesis können diese Eigenschaften nur dann geändert werden, wenn der Vertrag selbst dies zulässt, z.B. über eine spezifische State Extension.

Die nachstehende Tabelle veranschaulicht, wie die einzelnen Arten von Vertragsoperationen den Global State und den Owned State manipulieren können (oder auch nicht):

|                                 | Genesis | Zustandserweiterung | Zustandsübergang |
| ------------------------------- | :-----: | :-----------------: | :--------------: |
| **Hinzufügen von Global State** |    +    |         -           |        +         |
| **Änderung von Global State**   |   n/a   |         -           |        +         |
| **Hinzufügen von Owned State**  |    +    |         -           |        +         |
| **Änderung von Owned State**    |   n/a   |        Nein         |        +         |
| **Hinzufügen von Valenzen**     |    +    |         +           |        +         |


**`+`** : Aktion möglich, wenn das Schema des Vertrags dies zulässt.

**`-`**: Der Vorgang muss durch einen nachfolgenden Zustandsübergang bestätigt werden (die Zustandserweiterung allein schließt das Single-use Seal nicht).

Darüber hinaus lassen sich der zeitliche Umfang und die Aktualisierungsrechte der einzelnen Datentypen in der folgenden Tabelle unterscheiden:

|                                 | Metadaten                                | Global State                            | Owned State                                                                                             |
| ------------------------------- | ---------------------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Geltungsbereich**             | Definiert für eine einzelne Vertragsoperation | Global für den Vertrag definiert           | Definiert für jedes Siegel (*Zuweisung*)                                                               |
| **Wer kann es aktualisieren?**  | Nicht aktualisierbar (flüchtige Daten)   | Operation von Akteuren ausgeführt (Emittent usw.) | Abhängig vom rechtmäßigen Inhaber des Siegels (derjenige, der es in der nächsten Transaktion ausgeben kann) |
| **Zeitlicher Rahmen**           | Nur für die aktuelle Operation           | Der Zustand wird nach der Operation festgelegt | Der Zustand wird vor der Operation definiert (durch die *Siegeldefinition* der vorherigen Operation)      |


### Global State

Der Global State wird oft als "niemand besitzt, jeder weiß es" beschrieben. Er enthält allgemeine Informationen über den Vertrag, die öffentlich sichtbar sind. Bei einem Vertrag, der Token ausgibt, enthält er zum Beispiel möglicherweise:


- Der Ticker (symbolische Abkürzung des Tokens): `ticker`;
- Der vollständige Name des Tokens: `name`;
- Genauigkeit (Anzahl der Dezimalstellen): `precision`;
- Initiales Angebot (und/oder maximale Token-Grenze): `issuedSupply`;
- Ausstellungsdatum: `created`;
- Rechtliche Daten oder andere öffentliche Informationen: `data`.

Dieser Global State kann auf öffentlichen Ressourcen (Websites, IPFS, Nostr, Torrent usw.) abgelegt und an die Community verteilt werden. Auch der wirtschaftliche Anreiz (die Notwendigkeit, diese Token zu halten und zu übertragen usw.) treibt die Vertragsnutzer natürlich dazu, diese Daten selbst zu pflegen und zu verbreiten.

### Zuweisungen

Die *Zuweisung* ist die Grundstruktur für die Definition von:


- Dem Siegel (*Siegeldefinition*), das auf einen bestimmten UTXO verweist;
- Dem *Owned State*, d.h. die mit diesem Siegel verbundenen Eigenschaften oder Daten.

Eine *Zuweisung* kann als Analogon eines Bitcoin-Transaktions-Outputs gesehen werden, jedoch mit mehr Flexibilität. Hierin liegt die Logik der Eigentumsübertragung: die *Zuweisung* verbindet eine bestimmte Art von Vermögenswert oder Recht (`AssignmentType`) mit einem Siegel. Wer den privaten Schlüssel des mit diesem Siegel verbundenen UTXO besitzt (oder wer diesen UTXO ausgeben kann), wird als Eigentümer dieses *Owned State* betrachtet.

Eine der großen Stärken von RGB ist die Möglichkeit, die Felder *Siegeldefinition* und *Owned State* nach Belieben *offenzulegen* oder zu *verstecken* (auszublenden). Dies bietet eine leistungsstarke Kombination aus Vertraulichkeit und Selektivität. So kann man beispielsweise beweisen, dass ein Übergang gültig ist, ohne alle Daten offenzulegen, indem man der Person, die ihn validieren muss, die offengelegte Version zur Verfügung stellt, während Dritte nur die verborgene Version (einen Hash) sehen. In der Praxis wird die `OpId` eines Übergangs immer aus den *versteckten* Daten berechnet.

![RGB-Bitcoin](assets/en/067.webp)

#### Siegeldefinition

Die *Siegeldefinition* hat in ihrer offenkundigen Form vier grundlegende Felder: `txptr`, `vout`, `blinding` und `method` :


- **txptr**: Dies ist ein Verweis auf einen UTXO auf Bitcoin:
    - Im Falle eines **Genesis-Siegels** verweist er direkt auf einen bestehenden UTXO (der mit der Genesis verbundene);
    - Im Falle eines **Graphen-Siegels** kann er:
        - Ein einfaches `txid` sein, wenn er auf einen bestimmten UTXO verweist,
        - Oder ein `WitnessTx` sein, das eine Selbstreferenz darstellt: Das Siegel verweist auf die Transaktion selbst. Dies ist besonders nützlich, wenn kein externer UTXO verfügbar ist, z.B. bei Transaktionen zur Eröffnung von Lightning-Kanälen, oder wenn der Empfänger keinen UTXO hat.
- **vout** : die Output-Nummer der durch `txptr` angegebenen Transaktion. Nur bei einem Standard-Graph-Siegel vorhanden (nicht bei `WitnessTx`);
- **blinding**: eine Zufallszahl von 8 Bytes, um die Vertraulichkeit zu erhöhen und Brute-Force-Versuche zur Identifizierung des UTXO zu verhindern;
- **method**: gibt die verwendete Verankerungsmethode an (`Tapret` oder `Opret`).

Die *versteckte* Form der Siegeldefinition ist ein SHA256-Hash (getaggt) der Verkettung dieser 4 Felder, mit einem RGB-spezifischen Tag.

![RGB-Bitcoin](assets/en/068.webp)

#### Owned States

Die zweite Komponente von *Zuweisungen* ist der Owned State. Anders als der Global State kann er in öffentlicher oder privater Form existieren:


- **Öffentlicher Owned State**: Jeder kennt die mit dem Siegel verbundenen Daten. Zum Beispiel, ein öffentliches Bild;
- **Privater Owned State**: Die Daten sind verborgen und nur dem Eigentümer (und ggf. dem Validierer) bekannt. Zum Beispiel die Anzahl der gehaltenen Token.

RGB definiert vier mögliche Zustandstypen (*StateTypes*) für einen Owned State:


- **Deklarativ**: enthält keine numerischen Daten, sondern nur ein deklaratives Recht (z. B. ein Wahlrecht). Die verborgene und die offene Form sind identisch;
- **Fungibel**: steht für eine fungible Menge (wie Token). In offener Form haben wir `amount` (Betrag) und `blinding` (Verblendung). In versteckter Form haben wir ein einziges *Pedersen Commitment*, das den Betrag und die Verblendung verbirgt;
- **Structured**: speichert strukturierte Daten (bis zu 64 kB). In offener Form ist es der Datenblob. In versteckter Form ist es ein getaggter Hash-Wert dieses Blob:

```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```

Zum Beispiel mit :

```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```


- **Attachments**: Verknüpft eine Datei (Audio, Bild, Binärdatei usw.) mit dem Owned State und speichert den Datei-Hash `file_hash`, den MIME-Typ `media type` und ein kryptografisches Salt `salt`. Die Datei selbst wird an anderer Stelle gehostet. In versteckter Form ist sie ein Hash, der mit den drei vorangegangenen Datenelementen verknüpft ist:

```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```

Zum Beispiel mit:

```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```

Zusammengefasst sind dies die 4 möglichen Zustandsarten in öffentlicher und verborgener Form:

```txt
State                      Concealed form                              Revealed form
+---------------------------------------------------------------------------------------------------------

                   +--------------------------------------------------------------------------------+
                   |                                                                                |
Declarative        |                              < void >                                          |
                   |                                                                                |
                   +--------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------------

                   +--------------------------+             +---------------------------------------+
                   | +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
                   | +----------------------+ |             |         +--------+ +----------+       |
                   +--------------------------+             +---------------------------------------+

+---------------------------------------------------------------------------------------------------------

                   +--------------------------+             +---------------------------------------+
                   | +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
                   | +----------------------+ |             |         +--------------------+        |
                   +--------------------------+             +---------------------------------------+

+---------------------------------------------------------------------------------------------------------

                   +--------------------------+             +---------------------------------------+
                   | +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
                   | +----------------------+ |             | +-----------+ +------------+ +------+ |
                   +--------------------------+             +---------------------------------------+
```

| **Element**              | **Deklarativ**     | **Fungibel**                               | **Strukturiert**              | **Anhänge**                   |
| ------------------------ | ------------------ | ------------------------------------------ | ----------------------------- | ----------------------------- |
| **Daten**                | Keine              | Signierte oder unsignierte 64-Bit-Ganzzahl | Streng definierte Datentypen  | Jede Datei                    |
| **Informationstyp**      | Keine              | Signiert oder unsigniert                   | Strenge Typen                 | MIME-Typ                      |
| **Privatsphäre**         | Nicht erforderlich | Pedersen Commitment                        | Hash mit Blinding             | Gehashte Datei-ID             |
| **Größenbeschränkungen** | N/A                | 256 Bytes                                  | Bis zu 64 KB                  | Bis zu ~500 GB                |


### Inputs

Die Inputs einer *Vertragsoperation* beziehen sich auf die *Zuweisungen*, die in diesem neuen Vorgang ausgegeben werden. Ein Input zeigt an:


- `prevOpId` : der Identifier (`OpId`) der vorherigen Operation, in der sich die *Zuweisung* befand;
- `assignmentType` : die Art der *Zuweisung* (zum Beispiel `assetOwner` für ein Token);
- `index`: der Index der *Zuweisung* in der Liste, die mit der vorherigen `OpId` verbunden ist, ermittelt nach einer lexikografischen Sortierung der verborgenen Siegel.

Inputs erscheinen nie in Genesis, da es keine früheren Zuweisungen gibt. Sie erscheinen auch nicht in Zustandserweiterungen (weil Zustandserweiterungen keine Siegel schließen, sondern neue Siegel auf der Grundlage von Valenzen neu definieren).

Bei Owned States vom Typ `Fungible` prüft die Validierungslogik (über das im Schema enthaltene AluVM-Skript) die Konsistenz der Summen: die Summe der eingehenden Token (*Inputs*) muss gleich der Summe der ausgehenden Token (in den neuen *Zuweisungen*) sein.

### Metadaten

Das Feld **Metadaten** kann bis zu 64 KiB groß sein und wird verwendet, um temporäre Daten aufzunehmen, die für die Validierung nützlich sind, aber nicht in den permanenten Zustand des Vertrags integriert werden. Zum Beispiel können hier Zwischenberechnungsvariablen für komplexe Skripte gespeichert werden. Dieser Speicherplatz ist nicht dafür vorgesehen, in der globalen Historie gespeichert zu werden, weshalb er nicht in den Anwendungsbereich von Owned States oder Global State fällt.

### Valenzen

**Valenzen** sind ein neuartiger Mechanismus des RGB-Protokolls. Sie können in Genesis, State Transitions oder Zustandserweiterungen vorkommen. Sie stellen numerische Rechte dar, die durch eine Zustandserweiterung (über *Redeems*) aktiviert und dann durch eine nachfolgende Transition abgeschlossen werden können. Jede Valenz wird durch einen "Valenztyp" (16 Bit) identifiziert. Ihre Semantik (Wiederausgaberecht, Token-Swap, Vernichtungsrecht usw.) ist im Schema definiert.

Konkret könnte man sich eine Genesis vorstellen, die eine "Recht auf Neuausgabe"-Valenz definiert. Eine Zustandserweiterung verbraucht sie (*Rückgabe*), wenn bestimmte Bedingungen erfüllt sind, um eine neue Menge von Token einzuführen. Dann kann ein Zustandsübergang, der vom Inhaber des so geschaffenen Siegels ausgeht, diese neuen Token übertragen.

### Redeems

Redeems sind das Valenz-Äquivalent von Inputs für Zuweisungen. Sie erscheinen nur in Zustandserweiterungen, da hier eine zuvor definierte Valenz aktiviert wird. Ein Redeem besteht aus zwei Feldern:


- `prevOpId`: die `OpId` der Operation, bei der die Valenz angegeben wurde;
- `ValencyType`: die Art der Valenz, die man aktivieren möchte (jeder Valenztyp kann von der Zustandserweiterung nur einmal verwendet werden).

Beispiel: Ein Redeem kann einer CoinSwap-Ausführung entsprechen, je nachdem, was in der Valenz kodiert wurde.

### RGB-Zustandsmerkmale

Wir werden uns nun einige grundlegende Zustandsmerkmale von RGB ansehen. Insbesondere beschäftigen wir uns mit:

- Dem **Strict Type System**, das eine präzise und typisierte Organisation von Daten vorschreibt;
- Der Bedeutung der Trennung von **Validierung** und **Eigentum** ;
- Dem System der **Konsens-Evolution** in RGB, das die Begriffe *fast-forward* und *push-back* umfasst.

Wie immer ist zu beachten, dass alles, was mit dem Vertragszustand zu tun hat, auf der client-side. nach den im Protokoll festgelegten Konsensregeln validiert wird, deren ultimative kryptografische Referenz in Bitcoin-Transaktionen verankert ist.

#### Strict Type System

RGB verwendet ein *Strict Type System* und einen deterministischen Serialisierungsmodus (*Strict Encoding*). Dies soll perfekte Reproduzierbarkeit und Präzision bei der Definition, Handhabung und Validierung von Vertragsdaten gewährleisten.

In vielen Programmierumgebungen (JSON, YAML...) kann die Datenstruktur flexibel sein, sogar zu locker. In RGB hingegen werden die Struktur und die Typen der einzelnen Felder mit ausdrücklichen Einschränkungen definiert. Zum Beispiel:


- Jede Variable hat einen bestimmten Typ (z. B. eine 8-Bit-Ganzzahl ohne Vorzeichen `u8` oder eine 16-Bit-Ganzzahl mit Vorzeichen usw.);
- Typen können zusammengesetzt werden (verschachtelte Typen). Das bedeutet, dass Sie einen Typ definieren können, der auf anderen Typen basiert (z.B. ein Aggregattyp, der ein `u8`-Feld, ein `bool`-Feld usw. enthält);
- Es können auch Sammlungen angegeben werden: Listen (*list*), Mengen (*set*) oder Dictionaries (*map*), mit einer deterministischen Reihenfolge der Abfolge;
- Jedes Feld ist begrenzt (*untere Grenze* / *obere Grenze*). Auch die Anzahl der Elemente in Sammlungen wird begrenzt (Containment);
- Die Daten sind byte-ausgerichtet und die Serialisierung ist streng definiert und eindeutig.

Dank dieses strengen Kodierungsprotokolls :


- Ist die Reihenfolge der Felder immer die gleiche, unabhängig von der Implementierung oder der verwendeten Programmiersprache;
- Sind die mit demselben Datensatz berechneten Hashes daher reproduzierbar und identisch (streng deterministische *Commitments*);
- Verhindern Grenzen ein unkontrolliertes Anwachsen der Datengröße (z.B. zu viele Felder);
- Erleichtert diese Form der Verschlüsselung die kryptografische Überprüfung, da jeder Teilnehmer genau weiß, wie die Daten zu serialisieren und zu hashen sind.

In der Praxis werden die Struktur (*Schema*) und der resultierende Code (*Schnittstelle* und zugehörige Logik) kompiliert. Eine Beschreibungssprache wird verwendet, um den Vertrag (Typen, Felder, Regeln) zu definieren und ein strenges Binärformat zu erzeugen. Nach der Kompilierung ist das Ergebnis:


- Ein *Memory Layout* für jedes Feld;
- Semantische Bezeichner (die angeben, ob die Änderung eines Variablennamens Auswirkungen auf die Logik hat, auch wenn die Speicherstruktur gleich bleibt).

Das Strict Type System ermöglicht auch eine genaue Überwachung von Änderungen: Jede Änderung der Struktur (selbst eine Änderung des Feldnamens) ist erkennbar und kann zu einer Änderung des gesamten Footprints führen.

Schließlich erzeugt jede Kompilierung einen Fingerabdruck, einen kryptografischen Identifikator, der die genaue Version des Codes (Daten, Regeln, Validierung) bescheinigt. Zum Beispiel ein Identifikator in der Form :

```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```

Dies ermöglicht die Verwaltung von Konsens- oder Implementierungsupdates und gewährleistet gleichzeitig eine detaillierte Rückverfolgbarkeit der im Netzwerk verwendeten Versionen.

Um zu verhindern, dass der Zustand eines RGB-Vertrages zu aufwendig wird, um ihn auf der client-side zu validieren, schreibt eine Konsensregel eine maximale Größe von 2^16 Bytes (64 KiB) für alle Daten vor, die in Validierungsberechnungen einbezogen werden. Dies gilt für jede Variable oder Struktur: nicht mehr als 65536 Bytes oder das Äquivalent in Zahlen (32768 16-Bit-Ganzzahlen usw.). Dies gilt auch für Sammlungen (Listen, Sets, Maps), die nicht mehr als 2^16 Elemente enthalten dürfen.

Dieser Grenzwert garantiert :


- eine maximale Größe der Daten, die während eines Zustandsübergangs manipuliert werden;
- Kompatibilität mit der virtuellen Maschine (*AluVM*), die zur Ausführung der Validierungsskripte verwendet wird.

#### Das Paradigma: Validierung != Eigentum

Eine der wichtigsten Innovationen von RGB ist die strikte Trennung zwischen zwei Konzepten:


- **Validierung**: Überprüfung, ob ein Zustandsübergang die Regeln des Vertrags einhält (Business Logic, Historie usw.);
- Der **Besitz** (Eigentum oder Kontrolle): die Tatsache, den Bitcoin UTXO zu besitzen, der es ermöglicht, das Single-use Seal auszugeben (oder zu schließen) und somit den Zustandsübergang zu vollziehen.

Die **Validierung** findet auf der Ebene des RGB-Software-Stacks statt (Bibliotheken, *Commitments*-Protokoll, usw.). Ihre Aufgabe ist es, sicherzustellen, dass die internen Regeln des Vertrags (Beträge, Berechtigungen usw.) beachtet werden. Auch Beobachter oder andere Teilnehmer können die Datenhistorie validieren.

Der **Besitz** hingegen beruht vollständig auf der Sicherheit von Bitcoin. Der Besitz des privaten Schlüssels eines UTXO bedeutet die Kontrolle über die Fähigkeit, einen neuen Übergang zu starten (Schließen des Single-use Seals). Selbst wenn also jemand die Daten sehen oder validieren kann, kann er den Zustand nicht ändern, wenn er den betreffenden UTXO nicht besitzt.

![RGB-Bitcoin](assets/en/069.webp)

Dieser Ansatz begrenzt die klassischen Schwachstellen, die bei komplexeren Blockchains auftreten (wo der gesamte Code eines Smart Contract öffentlich ist und jedermann damit interagieren kann, was manchmal zu Hacks geführt hat). Bei RGB kann ein Angreifer nicht einfach mit dem on-chain Zustand interagieren, da das Recht, auf den Zustand einzuwirken (*Eigentum*), durch die Bitcoin-Schicht geschützt ist.

Darüber hinaus ermöglicht diese Entkopplung eine natürliche Integration von RGB in das Lightning-Netzwerk. Lightning-Kanäle können verwendet werden, um RGB-Assets zu aktivieren und zu verschieben, ohne dass jedes Mal On-Chain-*Commitments* erforderlich sind. Wir werden uns diese Integration von RGB in Lightning in späteren Kapiteln des Kurses genauer ansehen.

#### Konsensentwicklungen bei RGB

Zusätzlich zur semantischen Codeversionierung umfasst RGB ein System zur Weiterentwicklung oder Aktualisierung der Konsensregeln eines Vertrags im Laufe der Zeit. Es gibt zwei Hauptformen der Evolution:


- **Fast-forward**
- **Push-back**

Ein fast-forward tritt ein, wenn eine zuvor ungültige Regel gültig wird. Wenn sich der Vertrag beispielsweise dahingehend entwickelt, dass ein neuer Typ von "Zuweisungstyp" oder ein neues Feld zugelassen wird:


- Dies ist nicht mit einem klassischen Blockchain-Hardfork zu vergleichen, da RGB in der client-side Validierung arbeitet und die Gesamtkompatibilität der Blockchain nicht beeinträchtigt;
- In der Praxis wird diese Art der Änderung durch das Feld `Ffv` (*fast-forward version*) in der Vertragsoperation angezeigt;
- Die derzeitigen Inhaber werden nicht benachteiligt: Ihr Status bleibt gültig;
- Neue Begünstigte (oder neue Nutzer) hingegen müssen ihre Software (ihre Wallet) aktualisieren, um die neuen Regeln anzuwenden.

Ein Push-back bedeutet, dass eine zuvor gültige Regel ungültig wird. Es handelt sich also um eine "Härtung" der Regeln, aber nicht um eine Softfork im eigentlichen Sinne:


- Bestehende Inhaber können davon betroffen sein (sie könnten sich mit Vermögenswerten konfrontiert sehen, die in der neuen Version veraltet oder ungültig sind);
- Wir können davon ausgehen, dass wir tatsächlich ein neues Protokoll erstellen: Wer die neue Regel annimmt, weicht von der alten ab;
- Der Emittent kann beschließen, Vermögenswerte in diesem neuen Protokoll neu auszugeben, so dass die Nutzer gezwungen sind, zwei getrennte Wallets zu führen (eine für das alte Protokoll, die andere für das neue), wenn sie beide Versionen verwalten wollen.

In diesem Kapitel über RGB-Vertragsoperationen haben wir uns mit den grundlegenden Prinzipien dieses Protokolls beschäftigt. Wie du sicher bemerkt hast, erfordert die dem RGB-Protokoll innewohnende Komplexität die Verwendung vieler Fachbegriffe. Daher werde ich dir im nächsten Kapitel ein Glossar zur Verfügung stellen, das alle in diesem ersten theoretischen Teil behandelten Konzepte zusammenfasst und Definitionen aller Fachbegriffe im Zusammenhang mit RGB enthält. Im nächsten Abschnitt werden wir dann einen praktischen Blick auf die Definition und Implementierung von RGB-Verträgen werfen.

## RGB-Glossar

<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>

Wenn Sie auf dieses kurze Glossar mit wichtigen Fachbegriffen aus der RGB-Welt (in alphabetischer Reihenfolge) zurückgreifen müssen, werden Sie es nützlich finden. Dieses Kapitel ist nicht unbedingt notwendig, wenn Sie bereits alles verstanden haben, was wir im ersten Abschnitt behandelt haben.

#### AluVM

Die Abkürzung AluVM steht für "_Algorithmic logic unit Virtual Machine_", eine registerbasierte virtuelle Maschine, die für die Validierung von Smart Contracts und distributed Computing entwickelt wurde. Sie wird für die Validierung von RGB-Verträgen verwendet (ist aber nicht ausschließlich dafür reserviert). Skripte oder Operationen, die in einem RGB-Vertrag enthalten sind, können somit in der AluVM-Umgebung ausgeführt werden.

Für weitere Informationen: [AluVM offizielle Website](https://www.aluvm.org/)

#### Anchor

Ein Anchor stellt einen Satz von client-side Daten dar, der zum Nachweis der Einbeziehung eines eindeutigen _Commitment_ in eine Transaktion verwendet werden. Im RGB-Protokoll besteht ein Anchor aus den folgenden Elementen:


- Dem Bitcoin-Transaktionskennung (TXID) der **Zeugentransaktion** ;
- Dem **Multi Protocol Commitment (MPC)** ;
- Dem **Deterministischen Bitcoin Commitment (DBC)**;
- Dem **Extra Transaction Proof (ETP)**, wenn der **Tapret** Commitment-Mechanismus verwendet wird (siehe den diesem Modell gewidmeten Abschnitt).

Ein Anchor dient also dazu, eine überprüfbare Verbindung zwischen einer bestimmten Bitcoin-Transaktion und privaten Daten herzustellen, die durch das RGB-Protokoll validiert wurden. Er garantiert, dass diese Daten tatsächlich in der Blockchain enthalten sind, ohne dass ihr genauer Inhalt öffentlich zugänglich ist.


#### Business Logic

Die Business Logic fasst alle Regeln und internen Vorgänge eines Vertrags zusammen, die durch sein **Schema** (d.h. die Struktur des Vertrags selbst) beschrieben werden. Sie legt fest, wie sich der Zustand des Vertrags entwickeln kann und unter welchen Bedingungen.

#### client-side Validierung

Die client-side Validierung bezieht sich auf den Prozess, bei dem jede Partei (Client) eine Reihe von Daten, die privat ausgetauscht werden, gemäß den Regeln eines Protokolls überprüft. Im Fall von RGB werden diese ausgetauschten Daten in so genannten **consignments** zusammengefasst. Im Gegensatz zum Bitcoin-Protokoll, das verlangt, dass alle Transaktionen auf der Blockchain veröffentlicht werden, erlaubt RGB, dass nur _Commitments_ (in Bitcoin verankert) öffentlich gespeichert werden, während die wesentlichen Vertragsinformationen (Zustandsübergänge, Bescheinigungen, Beweise) off-chain bleiben und nur zwischen den betroffenen Nutzern ausgetauscht werden.

#### Commitment

Ein Commitment (im kryptographischen Sinne) ist ein mathematisches Objekt, bezeichnet mit `C`, das sich deterministisch aus einer Operation an strukturierten Daten `m` (der Nachricht) und einem Zufallswert `r` ergibt. Wir schreiben :

$$
C = \text{commit}(m, r)
$$

Dieser Mechanismus umfasst zwei Hauptvorgänge:


- **Commit**: Eine kryptographische Funktion wird auf eine Nachricht `m` und eine Zufallszahl `r` angewendet, um `C` zu erzeugen;
- **Verify**: Wir benutzen `C`, die `m` Nachricht und den `r` Wert, um zu überprüfen, ob dieses Commitment korrekt ist. Die Funktion gibt `True` oder `False` zurück.

Ein Commitment muss zwei Eigenschaften erfüllen:


- **Bindung**: Es muss unmöglich sein, zwei verschiedene Nachrichten zu finden, die das gleiche `C` ergeben:

$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$

Zum Beispiel:

$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$


- **Verstecken**: Die Kenntnis von `C` darf den Inhalt von `m` nicht preisgeben.

Im RGB-Protokoll wird eine Zusage in eine Bitcoin-Transaktion aufgenommen, um die Existenz einer bestimmten Information zu einem bestimmten Zeitpunkt zu beweisen, ohne die Information selbst preiszugeben.

#### Consignment

Ein **Consignment** fasst die zwischen den Parteien ausgetauschten Daten zusammen und unterliegt der client-side Validierung in RGB. Es gibt zwei Hauptkategorien von consignments:


- **Contract consignment**: wird vom *Emittenten* (Vertragsaussteller) bereitgestellt und enthält Initialisierungsinformationen wie Schema, Genesis, Schnittstelle und Schnittstellenimplementierung.
- **Transfer consignment**: wird von der zahlenden Partei (*Zahler*) bereitgestellt. Sie enthält die gesamte Historie der Zustandsübergänge, die zur letzten Consignment (d.h. dem vom Zahler empfangenen Endzustand) führen.

Diese consignments werden nicht öffentlich in der Blockchain erfasst, sondern direkt zwischen den beteiligten Parteien über den Kommunikationskanal ihrer Wahl ausgetauscht.

#### Deterministisches Bitcoin-Commitment - DBC

Deterministisches Bitcoin Commitment (DBC) ist der Satz von Regeln, die verwendet werden, um nachweislich und eindeutig ein _Commitment_ in einer Bitcoin-Transaktion zu speichern. Im RGB-Protokoll gibt es zwei Hauptformen von DBC:


- **Opret**
- **Tapret**

Diese Mechanismen definieren genau, wie das _Commitment_ in dem Output oder der Struktur einer Bitcoin-Transaktion kodiert wird, um sicherzustellen, dass dieses Commitment deterministisch nachvollziehbar und verifizierbar ist.

#### Eigentümerschaft

Eigentümerschaft bezieht sich auf die Fähigkeit, einen UTXO, auf den eine Siegeldefinition verweist, zu kontrollieren und auszugeben. Wenn ein Owned State mit einem UTXO verknüpft ist, hat der Eigentümer dieses UTXO das Recht, den zugehörigen State nach den Regeln des Vertrags zu übertragen oder weiterzuentwickeln.

#### Extra-Transaktionsnachweis - ETP

Der ETP (*Extra Transaction Proof*) ist der Teil des Anchor, der die zusätzlichen Daten enthält, die zur Validierung eines **Tapret** *Commitment* (im Kontext von _taproot_) erforderlich sind. Er enthält unter anderem den internen öffentlichen Schlüssel des Taproot-Skripts (_internal PubKey_) und Informationen, die für den _Script Path Spend_ spezifisch sind.

#### Genesis

Genesis bezieht sich auf den Satz von Daten, der durch ein Schema geregelt wird und den Ausgangszustand eines jeden Vertrags in RGB bildet. Es kann mit dem Konzept des _Genesis Block_ von Bitcoin oder dem Transaktionskonzept von Coinbase verglichen werden, hier jedoch auf der Ebene der _client-side_ und des RGB-Tokens.

#### Gerichteter azyklischer Graph - DAG

Ein DAG (Gerichteter azyklischer Graph, *Directed Acyclic Graph* oder *Acyclic Guided Graph*) ist ein zyklusfreier Graph, der eine topologische Planung ermöglicht. Blockchains, genauso wie die _Shards_ von RGB-Verträgen, können durch DAGs dargestellt werden.

Für weitere Informationen: [Gerichteter azyklischer Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)

#### Global State

Der Global State ist die Menge der öffentlichen Eigenschaften, die im Vertragszustand enthalten sind. Er wird in der Genesis definiert und kann je nach den Vertragsregeln durch autorisierte Übergänge aktualisiert werden. Im Gegensatz zu Owned States gehört der Global State nicht zu einer bestimmten Entität; er ist eher ein öffentliches Register innerhalb des Vertrags.


#### Gravur

Bei der Gravur handelt es sich um einen optionalen Datenstring, den aufeinanderfolgende Eigentümer eines Vertrags in die Vertragshistorie eingeben können. Diese Funktion ist z.B. in der Schnittstelle **RGB21** vorhanden und ermöglicht es, der Vertragshistorie Erinnerungsdaten oder beschreibende Informationen hinzuzufügen.


#### Implementierung der Schnittstelle

Die Schnittstellenimplementierung ist der Satz von Deklarationen, die eine **Schnittstelle** mit einem **Schema** verbinden. Sie ermöglicht die semantische Übersetzung, die von der Schnittstelle selbst vorgenommen wird, so dass die Rohdaten eines Vertrags vom Benutzer oder der beteiligten Software (den Wallets) verstanden werden können.


#### Letztes Consignment - Consignment-Endpoint

Das letzte Consignment (oder _Consignment-Endpoint_) ist ein *Transfer Consignment*, welches den endgültigen Zustand des Vertrags enthält, einschließlich des Zustandsübergangs, der aus der Rechnung des Empfängers (*Zahlungsempfänger*) erstellt wurde. Es handelt sich also um den Endpunkt einer Übertragung mit den erforderlichen Daten zum Nachweis des Eigentumsübergangs oder des Zustands.

#### Lightning-Netzwerk

Das Lightning-Netzwerk ist ein dezentrales Netzwerk von Zahlungskanälen (oder _State Channels_) auf Bitcoin, das aus 2/2 Multi-Signatur-Wallets besteht. Es ermöglicht schnelle, kostengünstige _off-chain_ Transaktionen, während es sich auf Bitcoins Layer 1 für die Schlichtung (oder Schließung) verlässt, wenn nötig.

Wenn Sie mehr über die Funktionsweise von Lightning erfahren möchten, empfehle ich Ihnen, diesen anderen Kurs zu besuchen:

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

#### Multi-Protokoll-Commitment - MPC

Multi-Protokoll Commitment (MPC) bezieht sich auf die Merkle-Baumstruktur, die in RGB verwendet wird, um innerhalb einer einzigen Bitcoin-Transaktion mehrere **transition bundles** aus verschiedenen Verträgen einzubeziehen. Die Idee ist, mehrere Commitments (die möglicherweise verschiedenen Verträgen oder verschiedenen Vermögenswerten entsprechen) in einem einzigen Anchor zusammenzufassen, um die Belegung des Blockspaces zu optimieren.

#### Owned State

Ein Owned State ist der Teil eines Vertragszustands, der in einer Zuweisung eingeschlossen und mit einem bestimmten Inhaber verbunden ist (über ein Single-use Seal, das auf einen UTXO zeigt). Dabei handelt es sich zum Beispiel um einen digitalen Vermögenswert oder ein bestimmtes vertragliches Recht, das dieser Person zugewiesen wurde.

#### Pedersen-Commitment

Eine Pedersen-Commitment ist eine Art von kryptografischem Commitment mit der Eigenschaft, **homomorph** in Bezug auf die Additionsoperation zu sein. Dies bedeutet, dass es möglich ist, die Summe von zwei Zusagen zu validieren, ohne die einzelnen Werte zu offenbaren.

Formal gesehen, wenn :

$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$

dann:

$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$

Diese Eigenschaft ist z.B. nützlich, um die Beträge der ausgetauschten Token zu verbergen, während die Gesamtsummen doch überprüft werden können.

Weitere Informationen: [Pedersen-Commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)


#### Rechnung

Eine Rechnung (invoice) hat die Form einer in [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58) kodierten URL, in der die für die Erstellung eines **Zustandsübergangs** (durch den Zahler) erforderlichen Daten eingebettet sind. Mit anderen Worten, es handelt sich um eine Rechnung, die es der Gegenpartei (*Zahler*) ermöglicht, den entsprechenden Übergang zu erstellen, um den Vermögenswert zu übertragen oder den Zustand des Vertrags zu aktualisieren.

#### Redeem

In einer Zustandserweiterung bezieht sich ein Redeem auf die Rückforderung (oder Ausnutzung) einer zuvor erklärten **Valenz**. Da es sich bei einer Valenz um ein öffentliches Recht handelt, kann ein autorisierter Teilnehmer durch Redeem eine bestimmte Vertragserweiterung in Anspruch nehmen.

#### Schema

Ein Schema in RGB ist ein deklarativer Codeabschnitt, der den Satz von Variablen, Regeln und Business Logic (*Business Logic*) beschreibt, die die Funktionsweise eines Vertrags bestimmen. Das Schema definiert die Zustandsstruktur, die Arten der zulässigen Übergänge und die Validierungsbedingungen.


#### Schnittstelle

Die Schnittstelle ist der Satz von Anweisungen, mit denen die in einem Schema oder in Vertragsoperationen zusammengestellten Binärdaten und ihre Zustände dekodiert werden, um sie für den Benutzer oder seine Wallet lesbar zu machen. Sie fungiert als Interpretationsschicht.


#### Shard

Ein Shard stellt einen Zweig im DAG der Zustandsübergangs-Historie eines RGB-Vertrags dar. Mit anderen Worten, es handelt sich um eine kohärente Teilmenge der Gesamtgeschichte des Vertrags, die z.B. der Abfolge der Übergänge entspricht, die erforderlich sind, um die Gültigkeit eines bestimmten Vermögenswerts seit der _Genesis_ nachzuweisen.

#### Siegeldefinition

Die Siegeldefinition ist der Teil einer Zuweisung, der das _Commitment_ mit einem UTXO im Besitz des neuen Inhabers verbindet. Mit anderen Worten, sie gibt an, wo sich die Bedingung befindet (in welchem UTXO), und begründet das Eigentum an einem Vermögenswert oder Recht.

#### Single-use Seal

Ein Single-use Seal (Einweg-Siegel) ist ein kryptografisches Versprechen eines Commitments zu einer noch unbekannten Nachricht, die nur einmal in der Zukunft offenbart wird und allen Mitgliedern eines bestimmten Publikums bekannt sein muss. Damit soll verhindert werden, dass für ein und dasselbe Siegel mehrere konkurrierende Zusagen gemacht werden.

#### Stash

Der Stash ist die Menge der client-side Daten, die ein Benutzer für einen oder mehrere RGB-Verträge zum Zweck der Validierung speichert (*client-side Validierung*). Dazu gehören die Übergangshistorie, Sendungen, Gültigkeitsnachweise usw. Jeder Inhaber behält nur die Teile der Historie, die er benötigt (*Shards*).

#### Taproot

Bezieht sich auf das Bitcoin-Transaktionsformat Segwit v1, das durch [BIP341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) und [BIP342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki) eingeführt wurde. Taproot verbessert die Vertraulichkeit und Flexibilität von Skripten, insbesondere indem es Transaktionen kompakter und schwieriger voneinander zu unterscheiden macht.

#### Teilweise signierte Bitcoin-Transaktion - PSBT

Eine PSBT (_Partially Signed Bitcoin Transaction_) ist eine Bitcoin-Transaktion, die noch nicht vollständig signiert ist. Sie kann zwischen mehreren Entitäten geteilt werden, von denen jede bestimmte Elemente (Signaturen, Skripte...) hinzufügen oder verifizieren kann, bis die Transaktion als bereit für die Veröffentlichung auf der Blockchain angesehen wird.

Für weitere Informationen: [BIP-0174](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki)

#### Transition Bundle

Ein Transition Bundle ist ein Satz von RGB-Zustandsübergängen (die zum selben Vertrag gehören), die alle an derselben ***Zeugentransaktion*** Bitcoin beteiligt sind. Dies macht es möglich, mehrere Updates oder Transfers in einem einzigen On-Chain-Anchor zu bündeln.

#### UTXO

Ein Bitcoin UTXO (*Unspent Transaction Output*) ist definiert durch den Hash einer Transaktion und den Output-Index (*vout*). Er wird manchmal auch als _Outpoint_ bezeichnet. Im RGB-Protokoll ermöglicht der Verweis auf einen UTXO (über eine **Siegeldefinition**) den Standort des **Owned State**, d.h. der in der Blockchain gehaltenen Eigenschaft.

#### Valenz

Eine Valenz ist ein öffentliches Recht, das als solches keine Zustandssicherung erfordert, sondern durch eine **Zustandserweiterung** eingelöst werden kann. Es handelt sich also um eine in der Vertragslogik deklarierte Möglichkeit, die allen (oder bestimmten) Akteuren offensteht, um zu einem späteren Zeitpunkt eine bestimmte Erweiterung vorzunehmen.

#### Vertrag

Ein Vertrag ist eine Reihe von Rechten, die auf digitalem Wege zwischen mehreren Akteuren über das RGB-Protokoll ausgeführt werden. Er hat einen aktiven Zustand und eine Business Logic, die durch ein Schema definiert ist, das angibt, welche Operationen zulässig sind (Übertragungen, Erweiterungen usw.). Der Zustand eines Vertrags sowie seine Gültigkeitsregeln werden im Schema ausgedrückt. Zu einem bestimmten Zeitpunkt entwickelt sich der Vertrag nur in Übereinstimmung mit dem, was das Schema und die Validierungsskripte (die z.B. in AluVM ausgeführt werden) zulassen.

#### Vertragliche Rechte

Vertragliche Rechte beziehen sich auf die verschiedenen Rechte, die von den an einem RGB-Vertrag Beteiligten ausgeübt werden können. Sie lassen sich in mehrere Kategorien einteilen:


- **Eigentumsrechte**, die mit dem Eigentum an einem bestimmten UTXO verbunden sind (über eine _Sigeldefinition_);
- **Ausführungsrechte**, d.h. die Fähigkeit, eine oder mehrere Transitionen (Zustandsübergänge) gemäß dem Schema zu erstellen;
- **Öffentliche Rechte**, wenn das Schema bestimmte öffentliche Verwendungen zulässt, z.B. die Schaffung einer Zustandserweiterung durch das Einlösen (redeem) einer Valenz.

#### Vertragsoperation

Eine Vertragsoperation ist eine Aktualisierung des Vertragszustands, die gemäß den Schemaregeln durchgeführt wird. Die folgenden Operationen gibt es in RGB:


- **State transition**;
- **Genesis**;
- **Zustandserweiterung**.

Jede Operation verändert den Zustand durch Hinzufügen oder Ersetzen bestimmter Daten (Global State, Owned State...).

#### Vertragsteilnehmer

Ein Vertragsteilnehmer ist ein Akteur, der an Vorgängen im Zusammenhang mit dem Vertrag teilnimmt. Im RGB wird unterschieden zwischen:


- Der Emittent des Vertrags, der die Genesis erstellt (der Ursprung des Vertrags);
- Die Vertragsparteien, d.h. die Inhaber der Rechte am Vertragszustand;
- Öffentliche Stellen, die Zustandserweiterungen vornehmen können, wenn der Vertrag öffentlich zugängliche Valenzen vorsieht.

#### Vertragszustand

Der Vertragsstatus entspricht dem aktuellen Zustand eines Vertrags zu einem bestimmten Zeitpunkt. Er kann sowohl aus öffentlichen als auch aus privaten Daten bestehen, die den Zustand des Vertrages widerspiegeln. RGB unterscheidet zwischen :


- Der **Globalstatus**, der die öffentlichen Eigenschaften des Vertrags enthält (in Genesis eingerichtet oder durch autorisierte Updates hinzugefügt);
- **Eigene Staaten**, die bestimmten Eigentümern gehören, die durch ihre UTXOs identifiziert werden.

#### Zeugentransaktion

Die Zeugentransaktion (Witness-Transaktion) ist die Bitcoin-Transaktion, die das Single-use Seal um eine Nachricht schließt, die ein Multi-Protokoll-Commitment (MPC) enthält. Diese Transaktion gibt einen UTXO aus oder erstellt einen, um das mit dem RGB-Protokoll verbundene Commitment zu versiegeln. Sie dient als On-Chain-Beweis dafür, dass der Zustand zu einem bestimmten Zeitpunkt festgelegt wurde.

#### Zustandserweiterung

Eine Zustandserweiterung ist eine Vertragsoperation, die dazu dient, Zustandsaktualisierungen erneut auszulösen, indem zuvor erklärte **Valenzen** eingelöst werden. Um wirksam zu sein, muss eine Zustandserweiterung anschließend durch einen Zustandsübergang abgeschlossen werden (der den Endzustand des Vertrags aktualisiert).

#### Zustandsübergang

Zustandsübergang (state transition) ist die Operation, die den Zustand eines RGB-Vertrags in einen neuen Zustand ändert. Sie kann Global State und/oder Owned State verändern. In der Praxis wird jeder Übergang durch Schema-Regeln verifiziert und in der Bitcoin-Blockchain durch ein _Commitment_ verankert.

#### Zuweisung

In der Logik von RGB ist eine Zuweisung das Äquivalent eines Transaktions-Outputs, die bestimmte Eigenschaften im Zustand eines Vertrags ändert, aktualisiert oder erzeugt. Eine Zuweisung besteht aus zwei Elementen:


- Einer **Siegeldefinition** (Verweis auf einen bestimmten UTXO) ;
- Ein **Owned State** (Daten, die den mit diesem neuen Eigentümer verbundenen Zustand beschreiben).

Eine Zuweisung zeigt daher an, dass ein Teil des Zustands (z.B. ein Vermögenswert) nun einem bestimmten Inhaber zugewiesen ist, der durch ein mit einem UTXO verknüpftes Single-use Seal identifiziert wird.

# Programmierung auf RGB

<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>

## Umsetzung von RGB-Verträgen

<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>

:::video id=97d81b85-5a82-40a5-b111-7d96be5afd0f:::

In diesem Kapitel werden wir einen genaueren Blick darauf werfen, wie ein RGB-Vertrag definiert und implementiert wird. Wir werden sehen, was die Komponenten eines RGB-Vertrags sind, welche Rolle sie spielen und wie sie aufgebaut sind.

### Die Bestandteile eines RGB-Vertrags

Bisher haben wir bereits die **Genesis** besprochen, die den Ausgangspunkt eines Vertrags darstellt, und wir haben gesehen, wie sie sich in die Logik einer *Vertragsoperation* und den Zustand des Protokolls einfügt. Die vollständige Definition eines RGB-Vertrages beschränkt sich jedoch nicht nur auf die Genesis: Sie umfasst drei ergänzende Komponenten, die zusammen das Herzstück der Implementierung bilden.

Die erste Komponente ist das **Schema**. Dabei handelt es sich um eine Datei, die die grundlegende Struktur und Business Logic (*Business Logic*) des Vertrags beschreibt. Sie spezifiziert die verwendeten Datentypen, die Validierungsregeln, die zulässigen Operationen (z. B. anfängliche Token-Ausgabe, Übertragungen, besondere Bedingungen usw.) - kurz gesagt, den allgemeinen Rahmen, der vorgibt, wie der Vertrag funktioniert.

Die zweite Komponente ist die **Schnittstelle**. Sie legt den Schwerpunkt darauf, wie die Nutzer (und damit auch die Portfoliosoftware) mit diesem Vertrag interagieren werden. Sie beschreibt die Semantik, d.h. die lesbare Darstellung der verschiedenen Felder und Aktionen. Während also das Schema definiert, wie der Vertrag technisch funktioniert, legt die Schnittstelle fest, wie diese Funktionalitäten dargestellt und zugänglich gemacht werden: Methodennamen, Datenanzeige usw.

Die dritte Komponente ist die **Schnittstellenimplementierung**, die die beiden vorherigen Komponenten ergänzt, indem sie als eine Art Brücke zwischen dem Schema und der Schnittstelle fungiert. Mit anderen Worten, sie verbindet die durch die Schnittstelle ausgedrückte Semantik mit den im Schema definierten zugrunde liegenden Regeln. Diese Implementierung sorgt beispielsweise für die Konvertierung zwischen einem in der Wallet eingegebenen Parameter und der vom Protokoll vorgegebenen binären Struktur oder für die Kompilierung der Validierungsregeln in Maschinensprache.

Diese Modularität ist ein interessantes Merkmal von RGB, da sie es verschiedenen Gruppen von Entwicklern ermöglicht, getrennt an diesen Aspekten (*Schema*, *Schnittstelle*, *Implementierung*) zu arbeiten, solange sie die Konsensregeln des Protokolls befolgen.

Zusammengefasst besteht jeder Vertrag aus :


- **Genesis**, die den Anfangszustand des Vertrags darstellt (und mit einer speziellen Transaktion verglichen werden kann, die das erste Eigentum an einem Vermögenswert, einem Recht oder anderen parametrisierbaren Daten definiert);
- **Schema**, das die Business Logic des Vertrags beschreibt (Datentypen, Validierungsregeln usw.);
- **Schnittstelle**, die sowohl für Wallets als auch für menschliche Nutzer eine semantische Ebene bietet, die das Lesen und Ausführen von Transaktionen verdeutlicht;
- **Implementation-Schnittstelle**, die die Kluft zwischen Business Logic und Darstellung überbrückt, um sicherzustellen, dass die Vertragsdefinition mit der Benutzererfahrung übereinstimmt.

![RGB-Bitcoin](assets/en/070.webp)

Es ist wichtig zu beachten, dass eine Wallet, die ein RGB-Asset (sei es ein fungibles Token oder ein Recht jeglicher Art) verwalten soll, alle diese Elemente zusammenhalten muss: *Schema*, *Schnittstelle*, *Schnittstellenimplementierung* und *Genesis*. Dies wird über ein ***contract consignment*** übermittelt, d.h. ein Datenpaket, das alles enthält, was zur Validierung des client-side Vertrags erforderlich ist.

Um diese Begriffe zu verdeutlichen, finden Sie hier eine zusammenfassende Tabelle, in der die Komponenten eines RGB-Vertrags mit Konzepten verglichen werden, die entweder in der objektorientierten Programmierung (OOP) oder im Ethereum-Ökosystem bereits bekannt sind:

| RGB Vertragskomponente       | Bedeutung                             | OOP-Äquivalent                                      | Ethereum-Äquivalent                |
| ---------------------------- | ------------------------------------- | --------------------------------------------------- | ---------------------------------- |
| **Genesis**                  | Anfangszustand des Vertrags           | Klassenkonstruktor                                  | Vertragskonstruktor                |
| **Schema**                   | Business Logic des Vertrags           | Klasse                                              | Vertrag                            |
| **Interface**                | Semantik des Vertrags                 | Interface (Java) / Trait (Rust) / Protokoll (Swift) | ERC-Standard                       |
| **Interface Implementation** | Zuordnung von Semantik und Logik      | Impl (Rust) / Implements (Java)                     | Application Binary Interface (ABI) |


Die linke Spalte zeigt die für das RGB-Protokoll spezifischen Elemente. Die mittlere Spalte zeigt die konkrete Funktion der einzelnen Komponenten. In der Spalte "OOP-Äquivalent" finden wir dann den entsprechenden Begriff in der objektorientierten Programmierung:


- Die **Genesis** spielt eine ähnliche Rolle wie ein *Klassenkonstruktor*: Hier wird der Zustand des Vertrags initialisiert;
- Das **Schema** ist die Beschreibung einer Klasse, d.h. die Definition ihrer Eigenschaften, Methoden und der zugrunde liegenden Logik;
- Die **Schnittstelle** entspricht *Schnittstellen* (Java), *Traits* (Rust) oder *Protokollen* (Swift): dies sind die öffentlichen Definitionen von Funktionen, Ereignissen, Feldern... ;
- Die **Schnittstellenimplementierung** entspricht *Impl* in Rust oder *Implements* in Java, wo wir angeben, wie der Code die in der Schnittstelle angekündigten Methoden tatsächlich ausführen wird.

Im Ethereum-Kontext ist die Genesis näher am *Vertragskonstruktor*, das Schema an der Vertragsdefinition, die Schnittstelle an einem Standard wie ERC-20 oder ERC-721 und die Schnittstellenimplementierung an der ABI (*Application Binary Interface*), die das Format der Interaktionen mit dem Vertrag festlegt.

Der Vorteil der Modularität von RGB liegt auch darin, dass verschiedene Beteiligte z.B. ihre eigene Schnittstellenimplementierung schreiben können, solange sie die Logik des *Schemas* und die Semantik der *Schnittstelle* beachten. So könnte ein Emittent ein neues, benutzerfreundlicheres Front-End (Schnittstelle) entwickeln, ohne die Logik des Vertrags zu ändern, oder umgekehrt könnte man das Schema erweitern, um neue Funktionen hinzuzufügen, und eine neue Version der angepassten Schnittstellenimplementierung bereitstellen, während die alten Implementierungen für die Grundfunktionen gültig bleiben.

Wenn wir einen neuen Vertrag erstellen, generieren wir eine Genesis (der erste Schritt bei der Ausgabe oder Verteilung des Vermögenswerts) sowie die zugehörigen Komponenten (Schema, Schnittstelle, Schnittstellenimplementierung). Danach ist der Vertrag voll funktionsfähig und kann an Wallets und Nutzer weitergegeben werden. Diese Methode, bei der Genesis mit diesen drei Komponenten kombiniert wird, garantiert ein hohes Maß an Individualisierung (jeder Vertrag kann seine eigene Logik haben), Dezentralisierung (jeder kann zu einer bestimmten Komponente beitragen) und Sicherheit (die Validierung bleibt streng durch das Protokoll definiert, ohne von willkürlichem On-Chain-Code abhängig zu sein, wie es bei anderen Blockchains oft der Fall ist).

Ich möchte nun einen genaueren Blick auf jede dieser Komponenten werfen: das **Schema**, die **Schnittstelle** und die **Schnittstellenimplementierung**.

### Schema

Im vorangegangenen Abschnitt haben wir gesehen, dass sich ein Vertrag im RGB-Ökosystem aus mehreren Elementen zusammensetzt: der Genesis, die den Ausgangszustand festlegt, und mehreren anderen ergänzenden Komponenten. Der Zweck des Schemas ist die deklarative Beschreibung der gesamten Business Logic des Vertrags, d.h. der Datenstruktur, der verwendeten Typen, der zulässigen Operationen und ihrer Bedingungen. Es ist daher ein sehr wichtiges Element, um einen Vertrag auf der Client-Seite funktionsfähig zu machen, da jeder Teilnehmer (z.B. eine Wallet) prüfen muss, ob die Zustandsübergänge, die er empfämgt, mit der im Schema definierten Logik übereinstimmen.

Ein Schema kann mit einer "Klasse" in der objektorientierten Programmierung (OOP) verglichen werden. Im Allgemeinen dient es als Modell, das die Komponenten eines Vertrags definiert, wie z.B.:


- Die verschiedenen Arten von Owned States und Zuweisungen;
- Valenzen, d.h. besondere Rechte, die bei bestimmten Vorgängen ausgelöst (*redeemed*) werden können;
- Globale Statess, die globale, öffentliche und gemeinsame Eigenschaften des Vertrags beschreiben;
- Die Genesis-Struktur (die allererste Operation, die den Vertrag aktiviert);
- Die zulässigen Formen von Zustandsübergängen und -erweiterungen und wie diese Operationen die Metadaten verändern können;
- Metadaten, die mit jedem Vorgang verbunden sind, um vorübergehende oder zusätzliche Informationen zu speichern;
- Regeln, die festlegen, wie sich interne Vertragsdaten entwickeln können (z.B. ob ein Feld veränderbar oder kumulativ ist);
- Abfolgen von Operationen, die als gültig angesehen werden: z.B. eine Reihenfolge von Übergängen, die eingehalten werden müssen, oder eine Reihe von logischen Bedingungen, die erfüllt werden müssen.

![RGB-Bitcoin](assets/en/071.webp)

Wenn der *Emittent* eines Vermögenswertes auf RGB einen Vertrag veröffentlicht, stellt er die Genesis und das damit verbundene Schema zur Verfügung. Benutzer oder Wallets, die mit dem Vermögenswert interagieren möchten, rufen dieses Schema ab, um die Logik hinter dem Vertrag zu verstehen und um später überprüfen zu können, ob die Übergänge, an denen sie teilnehmen werden, legitim sind.

Der erste Schritt für jeden, der Informationen über einen RGB-Vermögenswert erhält (z.B. eine Token-Übertragung), besteht darin, diese Informationen anhand des Schemas zu validieren. Dazu wird die Schema-Kompilierung verwendet, um:


- zu prüfen, ob Owned States, Zuweisungen und andere Elemente korrekt definiert sind und ob sie die vorgeschriebenen Typen einhalten (das sogenannte *strict Type System*);
- zu überprüfen, ob die Übergangsregeln (Validierungsskripte) erfüllt sind. Diese Skripte können über AluVM ausgeführt werden, das auf der client-side vorhanden ist und für die Validierung der Konsistenz der Business Logic zuständig ist (Überweisungsbetrag, besondere Bedingungen usw.).

In der Praxis ist das Schema kein ausführbarer Code, wie man bei Blockchains sehen kann, die On-Chain-Code speichern (EVM auf Ethereum). Im Gegenteil, RGB trennt die Business Logic (deklarativ) vom ausführbaren Code auf der Blockchain (der auf kryptografische Anchor beschränkt ist). Das Schema legt also die Regeln fest, aber die Anwendung dieser Regeln findet außerhalb der Blockchain statt, bei jedem Teilnehmer, nach dem Prinzip der client-side Validierung.

Ein Schema muss kompiliert werden, bevor es von RGB-Anwendungen verwendet werden kann. Diese Kompilierung erzeugt eine Binärdatei (z.B. `.rgb`) oder eine verschlüsselte Binärdatei (`.rgba`). Wenn die Wallet diese Datei importiert, weiß sie:


- Wie jeder Datentyp (Ganzzahlen, Strukturen, Arrays...) dank des strengen Typensystems aussieht;
- Wie Genesis strukturiert sein sollte (zum Verständnis der Asset-Initialisierung);
- Die verschiedenen Arten von Operationen (Zustandsübergänge, Zustandserweiterungen) und wie sie den Zustand verändern können;
- Die (im Schema eingeführten) Skripting-Regeln, die die AluVM-Engine anwendet, um die Gültigkeit der Operationen zu prüfen.

Wie in den vorangegangenen Kapiteln erläutert, bietet uns das *strict Type System* ein stabiles, deterministisches Kodierungsformat: alle Variablen, ob Owned States, Global States oder Valenzen, werden genau beschrieben (Größe, untere und obere Schranken, falls erforderlich, Typ mit oder ohne Vorzeichen usw.). Es ist auch möglich, verschachtelte Strukturen zu definieren, um z.B. komplexe Anwendungsfälle zu unterstützen.

Optional kann das Schema auf eine Root-`SchemaId` verweisen, was die Wiederverwendung einer bestehenden Grundstruktur (einer Vorlage/ein Template) erleichtert. Auf diese Weise können Sie einen Vertrag weiterentwickeln oder Variationen (z.B. eine neue Art von Token) aus einer bereits bewährten Vorlage erstellen. Diese Modularität vermeidet die Notwendigkeit, ganze Verträge neu zu erstellen, und fördert die Standardisierung bewährter Verfahren.

Ein weiterer wichtiger Punkt ist, dass die Logik der Zustandsentwicklung (Übertragungen, Aktualisierungen usw.) im Schema in Form von Skripten, Regeln und Bedingungen beschrieben wird. Wenn der Vertragsgestalter also eine Neuausgabe genehmigen oder einen Burn-Mmechanismus (Zerstörung von Token) vorschreiben möchte, kann er die entsprechenden Skripte für AluVM im Validierungsteil des Schemas angeben.

#### Unterschied zu programmierbaren On-Chain-Blockchains

Im Gegensatz zu Systemen wie Ethereum, bei denen der Smart-Contract-Code (ausführbar) in die Blockchain selbst geschrieben wird, speichert RGB den Vertrag (seine Logik) außerhalb der Blockchain, in Form eines kompilierten deklarativen Dokuments. Dies bedeutet:


- Es gibt keine Turing-komplette VM, die in jedem Knoten des Bitcoin-Netzwerks läuft. Die Regeln eines RGB-Vertrages werden nicht auf der Blockchain ausgeführt, sondern in jedem Nutzer, der einen Zustand validieren möchte;
- Vertragsdaten verschmutzen die Blockchain nicht: nur kryptographische Beweise (*Commitments*) werden in Bitcoin-Transaktionen eingebettet (über `Tapret` oder `Opret`);
- Das Schema kann aktualisiert oder abgelehnt werden (*fast-forward*, *push-back*, etc.), ohne dass ein Fork auf der Bitcoin-Blockchain erforderlich ist. Wallets müssen lediglich das neue Schema importieren und sich an die Konsensänderungen anpassen.

#### Nutzung durch den Emittenten und die Nutzer

Wenn ein *Emittent* einen Vermögenswert schafft (z. B. ein nicht-inflationäres fungibles Token), bereitet er folgendes vor:


- Ein Schema, das die Regeln für Emission, Übertragung usw. beschreibt;
- Eine an dieses Schema angepasste Genesis (mit der Gesamtzahl der ausgegebenen Token, der Identität des ursprünglichen Besitzers, speziellen Valenzen für die Neuausgabe usw.).

Anschließend wird das kompilierte Schema (eine `.rgb`-Datei) den Nutzern zur Verfügung gestellt, so dass jeder, der eine Übertragung dieses Tokens erhält, die Konsistenz des Vorgangs lokal überprüfen kann. Ohne dieses Schema wäre ein Benutzer nicht in der Lage, die Statusdaten zu interpretieren oder zu überprüfen, ob sie den Vertragsregeln entsprechen.

Wenn also eine neue Wallet einen Vermögenswert unterstützen möchte, muss sie lediglich das entsprechende Schema integrieren. Dieser Mechanismus macht es möglich, die Kompatibilität mit neuen RGB-Asset-Typen hinzuzufügen, ohne die Software-Basis der Wallet invasiv zu verändern: Es ist lediglich erforderlich, das Schema-Binary zu importieren und seine Struktur zu verstehen.

Das Schema definiert die Business Logic in RGB. Es enthält die Evolutionsregeln eines Vertrags, die Struktur seiner Daten (Owned States, Global State, Valenzen) und die zugehörigen Validierungsskripte (ausführbar durch AluVM). Dank dieses deklarativen Dokuments ist die Definition eines Vertrags (kompilierte Datei) klar von der tatsächlichen Ausführung der Regeln (client-side) getrennt. Diese Entkopplung verleiht RGB eine große Flexibilität und ermöglicht eine breite Palette von Anwendungsfällen (fungible Token, NFT, anspruchsvollere Verträge), wobei die Komplexität und die Fehler vermieden werden, die für programmierbare On-Chain-Blockchains typisch sind.

#### Beispiel-Schema

Werfen wir einen Blick auf ein konkretes Beispiel für ein Schema für einen RGB-Vertrag. Dies ist ein Auszug in Rust aus der Datei `nia.rs` (Initialen für "*Non-Inflatable Assets*"), die ein Modell für fungible Token definiert, die nicht über ihren ursprünglichen Bestand hinaus neu ausgegeben werden können (ein nicht-inflationärer Vermögenswert). Diese Art von Token kann im RGB-Universum als Äquivalent zum ERC20 auf Ethereum angesehen werden, d.h. als fungible Token, die bestimmte Grundregeln einhalten (z.B. für Übertragungen, die Initialisierung des Bestands usw.).

Bevor wir in den Code eintauchen, sollten wir uns die allgemeine Struktur eines RGB-Schemas in Erinnerung rufen. Es besteht aus einer Reihe von Deklarationen, die folgenden Rahmen festlegen:


- Eine mögliche `SchemaId`, die die Verwendung eines anderen Basisschemas als Vorlage angibt;
- Die **Global States** und **Owned State** (mit ihren strengen Typen);
- **Valenzen** (falls vorhanden);
- Die **Operationen** (Genesis, Zustandsübergänge, Zustandserweiterungen), die sich auf diese Zustände und Wertigkeiten beziehen können;
- Das **Strict Type System**, das zur Beschreibung und Validierung von Daten verwendet wird;
- **Validierungsskripte** (über AluVM ausgeführt).

![RGB-Bitcoin](assets/en/072.webp)

Der folgende Code zeigt die vollständige Definition des Rust-Schemas. Wir werden ihn Teil für Teil kommentieren, indem wir die Anmerkungen (1) bis (9) unten befolgen:

```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
    
    // definitions of libraries and variables

    // ===== PART 2: General Properties (ffv, subset_of, type_system) =====
    Schema {
        ffv: zero!(),
        subset_of: None,
        type_system: types.type_system(),

        // ===== PART 3: Global States =====
        global_types: tiny_bmap! {
            GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
            GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
            GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
            GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
        },

        // ===== PART 4: Owned Types =====
        owned_types: tiny_bmap! {
            OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
        },

        // ===== PART 5: Valencies =====
        valency_types: none!(),

        // ===== PART 6: Genesis: Initial Operations =====
        genesis: GenesisSchema {
            metadata: Ty::<SemId>::UNIT.id(None),
            globals: tiny_bmap! {
                GS_NOMINAL => Occurrences::Once,
                GS_DATA => Occurrences::Once,
                GS_TIMESTAMP => Occurrences::Once,
                GS_ISSUED_SUPPLY => Occurrences::Once,
            },
            assignments: tiny_bmap! {
                OS_ASSET => Occurrences::OnceOrMore,
            },
            valencies: none!(),
        },

        // ===== PART 7: Extensions =====
        extensions: none!(),

        // ===== PART 8: Transitions: TS_TRANSFER =====
        transitions: tiny_bmap! {
            TS_TRANSFER => TransitionSchema {
                metadata: Ty::<SemId>::UNIT.id(None),
                globals: none!(),
                inputs: tiny_bmap! {
                    OS_ASSET => Occurrences::OnceOrMore,
                },
                assignments: tiny_bmap! {
                    OS_ASSET => Occurrences::OnceOrMore,
                },
                valencies: none!(),
            }
        },

        // ===== PART 9: Script AluVM and Entry Points =====
        script: Script::AluVM(AluScript {
            libs: confined_bmap! { alu_id => alu_lib },
            entry_points: confined_bmap! {
                EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
                EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
            },
        }),
    }
}
```


- (1) - **Funktionsheader und Subschema**

Die Funktion `nia_schema()` gibt ein `SubSchema` zurück, was bedeutet, dass dieses Schema teilweise von einem allgemeineren Schema erben kann. Im RGB-Ökosystem ermöglicht diese Flexibilität die Wiederverwendung bestimmter Standardelemente eines Hauptschemas und die Festlegung spezifischer Regeln für den betreffenden Vertrag. In diesem Fall haben wir uns entschieden, die Vererbung nicht zu aktivieren, da `subset_of` `None` sein wird.


- (2) - Allgemeine Eigenschaften: ffv, subset_of, **type_system**

Die Eigenschaft `ffv` entspricht der *fast-forward* Version des Vertrags. Ein Wert von `zero!()` zeigt an, dass wir uns in der Version 0 oder der Anfangsversion dieses Schemas befinden. Wenn man zu einem späteren Zeitpunkt neue Funktionalitäten hinzufügen möchten (neue Art von Operationen usw.), kann man diese Version erhöhen, um eine Konsensänderung anzuzeigen.

Die `subset_of: None`-Eigenschaft bestätigt die Abwesenheit von Vererbung. Das Feld `type_system` verweist auf das strenge Typsystem, das bereits in der Bibliothek `types` definiert ist. Diese Zeile zeigt an, dass alle vom Vertrag verwendeten Daten die strenge Serialisierungsimplementierung verwenden, die von der betreffenden Bibliothek bereitgestellt wird.


- (3) - Global States

Im Block `global_types` deklarieren wir vier Elemente. Wir verwenden die Schlüssel, z.B. `GS_NOMINAL` oder `GS_ISSUED_SUPPLY`, um später auf sie zu verweisen:


- `GS_NOMINAL` bezieht sich auf einen `DivisibleAssetSpec`-Typ, der verschiedene Felder des erstellten Tokens beschreibt (vollständiger Name, Ticker, Genauigkeit...);
- `GS_DATA` steht für allgemeine Daten, wie z. B. einen Haftungsausschluss, Metadaten oder anderen Text;
- `GS_TIMESTAMP` bezieht sich auf ein Ausstellungsdatum;
- mit `GS_ISSUED_SUPPLY` wird die Gesamtmenge festgelegt, d.h. die maximale Anzahl der Token, die erzeugt werden können.

Das Schlüsselwort `once(...)` bedeutet, dass jedes dieser Felder nur einmal vorkommen kann.


- (4) - Owned States

In `owned_types` deklarieren wir `OS_ASSET`, das einen fungiblen Zustand beschreibt. Wir verwenden `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, was bedeutet, dass die Menge der Vermögenswerte (Token) als vorzeichenlose 64-Bit-Ganzzahl gespeichert wird. Somit wird bei jeder Transaktion eine bestimmte Anzahl von Einheiten dieses Tokens gesendet, die gemäß dieser streng typisierten numerischen Struktur validiert wird.


- (5) - **Valenzen**

Wir geben `valency_types: none!()` an, was bedeutet, dass es in diesem Schema keine Valenzen gibt, d.h. keine besonderen oder zusätzlichen Rechte (wie z.B. Wiederveröffentlichung, bedingtes Burnen, usw.). Wenn ein Schema welche enthielte, würden sie in diesem Abschnitt deklariert werden.


- (6) - Genesis: Erste Operationen

Hier kommen wir zu dem Teil, der die Vertragsoperationen erklärt. Die Genesis wird beschrieben durch:


- Das Fehlen von `metadata` (Feld `Metadaten: Ty::<SemId>::UNIT.id(None)`) ;
- Global States, die jeweils einmal vorhanden sein müssen (`Once`);
- Eine Zuweisungsliste, in der `OS_ASSET` einmal oder mehrmals (`OnceOrMore`) vorkommen muss. Das bedeutet, dass Genesis mindestens eine `OS_ASSET`-Zuweisung (einen ersten Inhaber) benötigt;
- Keine Valenz: `Valenzen: none!()`.

Auf diese Weise schränken wir die Definition der anfänglichen Token-Ausgabe ein: Wir müssen das ausgegebene Angebot (`GS_ISSUED_SUPPLY`) sowie mindestens einen Inhaber (einen Owned State vom Typ `OS_ASSET`) angeben.


- (7) - Erweiterungen

Das Feld `Extensions: none!()` zeigt an, dass in diesem Vertrag keine Zustandserweiterung vorgesehen ist. Dies bedeutet, dass es keine Operation zur Einlösung eines digitalen Rechts (Valenz) oder zur Durchführung einer Zustandserweiterung vor einem Zustandsübergang gibt. Alles wird über Genesis oder State Transitions abgewickelt.


- (8) - Übergänge: TS_TRANSFER

In `transitions` definieren wir den Operationstyp `TS_TRANSFER`. Wir erklären (zgl. einer Transition), dass:


- Sie keine Metadaten enthält;
- Der Global State (der bereits in Genesis definiert ist) dadurch nicht verändert wird;
- Sie einen oder mehrere `OS_ASSETs` als Input nimmt. Das bedeutet, dass sie vorhandene Owned States ausgeben muss;
- Sie mindestens ein neues "OS_ASSET" erstellt (mit anderen Worten: der oder die Empfänger erhalten Token);
- Sie keine neue Valenz erzeugt.

Dies modelliert das Verhalten eines Basis-Transfers, der Token auf einem UTXO verbraucht, dann neue Owned States zugunsten der Empfänger schafft und somit die Gleichheit des Gesamtbetrags zwischen Inputs und Outputs bewahrt.


- (9) - **AluVM-Skript und Entry Points**

Schließlich deklarieren wir ein AluVM-Skript (`Script::AluVM(AluScript { ... })`). Dieses Skript enthält:


- Eine oder mehrere externe Bibliotheken (`libs`), die während der Validierung verwendet werden sollen;
- Einstiegspunkte (Entry Points), die auf Funktionsoffsets im AluVM-Code zeigen, die der Validierung der Genesis (`ValidateGenesis`) und jeder deklarierten Transition (`ValidateTransition(TS_TRANSFER)`) entsprechen.

Dieser Validierungscode ist für die Anwendung der Business Logic verantwortlich. Er prüft zum Beispiel:


- Dass der Wert `GS_ISSUED_SUPPLY` während der Genesis nicht überschritten wird;
- Dass die Summe der `inputs` (gesendete Token) gleich der Summe der `Zuweisungen` (empfangene Token) für `TS_TRANSFER` ist.

Werden diese Regeln nicht beachtet, wird der Übergang als ungültig betrachtet.

Dieses Beispiel eines "*Non Inflatable Fungible Asset*"-Schemas vermittelt uns ein besseres Verständnis für die Struktur eines einfachen RGB Fungible-Token-Vertrags. Man erkennt deutlich die Trennung zwischen der Beschreibung der Daten (Global und Owned States), der Deklaration der Operationen (Genesis, Transitions, Extensions) und der Implementierung der Validierung (AluVM-Skripte). Dank dieses Modells verhält sich ein Token wie ein klassischer fungibler Token, bleibt aber auf der client-side validiert und ist nicht von der On-Chain-Infrastruktur abhängig, um seinen Code auszuführen. Nur die kryptographischen Commitments sind in der Bitcoin-Blockchain verankert.

### Schnittstelle

Die Schnittstelle ist die Ebene, die einen Vertrag lesbar und manipulierbar machen soll, sowohl für die Nutzer (menschliche Leser) als auch für die Portfolios (lesende Software). Die Schnittstelle spielt daher eine Rolle, die mit der einer Schnittstelle in einer objektorientierten Programmiersprache (Java, Rust Trait usw.) vergleichbar ist, da sie die funktionale Struktur eines Vertrags offenlegt und verdeutlicht, ohne notwendigerweise die internen Details der Business Logic offenzulegen.

Im Gegensatz zum Schema, das rein deklarativ ist und in eine binäre Datei kompiliert wird, die nur schwer zu verwenden ist, bietet die Schnittstelle die Schlüsselinformationen, die nötig sind für:


- Nennen und beschreiben der im Vertrag enthaltenen Global States und Owned States;
- Zugriff auf die Namen und Werte der einzelnen Felder, so dass sie angezeigt werden können (z.B. für einen Token, um dessen Ticker, maximale Menge usw. zu ermitteln);
- Interpretieren und konstruieren von Vertragsoperationen (Genesis, Zustandsübergang oder Zustandserweiterung), indem Sie Daten mit verständlichen Namen verknüpft (z.B. durchführen einer Überweisung, indem man eindeutig "Betrag" und nicht einen binären Bezeichner angibt).

![RGB-Bitcoin](assets/en/073.webp)

Dank der Schnittstelle kann man beispielsweise Wallet-Code schreiben, der anstelle von Feldern direkt Bezeichnungen wie "Anzahl der Token", "Asset-Name" usw. manipuliert. Auf diese Weise wird die Verwaltung eines Vertrags intuitiver.

#### Allgemeiner Betrieb

Diese Methode hat viele Vorteile:


- **Normierung:**

Dieselbe Art von Vertrag kann durch eine Standardschnittstelle unterstützt werden, die von mehreren Wallet-Implementierungen gemeinsam genutzt wird. Dies erleichtert die Kompatibilität und die Wiederverwendung von Code.


- Klare Trennung zwischen Schema und Schnittstelle:

Beim RGB-Design sind das Schema (Business Logic) und die Schnittstelle (Darstellung und Manipulation) zwei unabhängige Einheiten. Die Entwickler, die die Vertragslogik schreiben, können sich auf das Schema konzentrieren, ohne sich über Ergonomie oder Datendarstellung Gedanken zu machen, während ein anderes Team (oder dasselbe Team, aber mit einem anderen Zeitplan) die Schnittstelle entwickeln kann.


- **Flexible Entwicklung:**

Die Schnittstelle kann nach der Ausgabe des Vermögenswerts geändert oder ergänzt werden, ohne dass der Vertrag selbst geändert werden muss. Dies ist ein wesentlicher Unterschied zu einigen On-Chain-Smart-Contract-Systemen, bei denen die Schnittstelle (oft zusammen mit dem Ausführungscode) in der Blockchain eingefroren ist.


- Multi-Interface-Fähigkeit

Ein und derselbe Vertrag könnte über verschiedene Schnittstellen zugänglich gemacht werden, die an unterschiedliche Bedürfnisse angepasst sind: eine einfache Schnittstelle für den Endnutzer, eine andere, fortgeschrittenere für den Emittenten, der komplexe Konfigurationsvorgänge verwalten muss. Die Wallet kann dann je nach Verwendungszweck wählen, welche Schnittstelle sie importiert.

![RGB-Bitcoin](assets/en/074.webp)

In der Praxis importiert die Wallet, wenn sie einen RGB-Vertrag abruft (über eine `.rgb`- oder `.rgba`-Datei), auch die zugehörige Schnittstelle, die ebenfalls kompiliert wird. Zur Laufzeit kann die Wallet zum Beispiel:


- Die Liste der States durchsuchen und deren Namen lesen um Ticker, Anfangsbetrag, Ausgabedatum usw. auf der Benutzeroberfläche anzuzeigen, anstatt eine unleserliche numerische Kennung zu verwenden;
- Eine Operation (z.B. eine Überweisung) unter Verwendung expliziter Parameternamen erstellen: anstatt "Zuweisungen { OS_ASSET => 1 }" zu schreiben, kann sie dem Benutzer ein Feld "Betrag" in einem Formular anbieten und diese Information in die vom Vertrag erwarteten streng typisierten Felder übersetzen.

#### Unterschied zu Ethereum und anderen Systemen

Bei Ethereum wird die Schnittstelle (beschrieben durch das ABI, *Application Binary Interface*) in der Regel aus dem auf der Blockchain gespeicherten Code (dem Smart Contract) abgeleitet. Es kann kostspielig oder kompliziert sein, einen bestimmten Teil der Schnittstelle zu ändern, ohne den Vertrag selbst zu berühren. RGB basiert jedoch auf einer Logik, die vollständig außerhalb der Bitcoin-Blockchain liegt, wobei die Daten in *Commitments* auf Bitcoin verankert sind. Dieses Design macht es möglich, die Schnittstelle (oder ihre Implementierung) zu ändern, ohne die grundlegende Sicherheit des Vertrages zu beeinträchtigen, da die Validierung der Regeln im Schema und im referenzierten AluVM-Code verbleibt.

#### Zusammenstellung der Schnittstelle

Wie beim Schema wird die Schnittstelle im Quellcode (oft in Rust) definiert und in eine `.rgb`- oder `.rgba`-Datei kompiliert. Diese Binärdatei enthält alle Informationen, die die Wallet benötigt, um:


- Felder anhand ihres Namens identifizieren;
- Jedes Feld (und seinen Wert) mit dem im Vertrag definierten strengen Systemtyp zu verknüpfen;
- Die verschiedenen zulässigen Operationen zu kennen und zu wissen, wie sie zu erstellen sind.

Sobald die Schnittstelle importiert wurde, kann die Wallet den Vertrag korrekt anzeigen und dem Nutzer Interaktionen vorschlagen.

### Von der LNP/BP Association standardisierte Schnittstellen

Im RGB-Ökosystem wird eine Schnittstelle verwendet, um den Daten und Operationen eines Vertrags eine lesbare und manipulierbare Bedeutung zu geben. Die Schnittstelle ergänzt somit das Schema, das die Business Logic intern beschreibt (strict Types, Validierungsskripte usw.). In diesem Abschnitt werfen wir einen Blick auf die Standardschnittstellen, die von der LNP/BP Association für gängige Vertragstypen (fungible Token, NFT usw.) entwickelt wurden.

Zur Erinnerung: Die Idee ist, dass jede Schnittstelle beschreibt, wie ein Vertrag auf der Seite der Wallet angezeigt und bearbeitet werden kann, wobei die Felder klar benannt werden (z.B. `spec`, `ticker`, `issuedSupply`...) und die möglichen Operationen definiert werden (z.B. `Transfer`, `Burn`, `Rename`...). Mehrere Schnittstellen sind bereits in Betrieb, aber es werden in Zukunft immer mehr hinzukommen.

#### Einige vorgefertigte Schnittstellen

**RGB20** ist die Schnittstelle für fungible Vermögenswerte, die mit dem ERC20-Standard von Ethereum verglichen werden kann. Sie geht jedoch einen Schritt weiter und bietet umfangreichere Funktionen:


- Zum Beispiel die Möglichkeit, den Vermögenswert umzubenennen (Änderung des *Tickers* oder des vollständigen Namens), nachdem er ausgegeben wurde, oder seine Genauigkeit anzupassen (*Aktiensplit*);
- Sie kann auch Mechanismen für eine (begrenzte oder unbegrenzte) Sekundäremmision sowie für einen Burn und anschließende Ersetzung beschreiben, um den Emittenten zu ermächtigen, Vermögenswerte unter bestimmten Bedingungen zu vernichten und anschließend wiederherzustellen;

Die RGB20-Schnittstelle kann beispielsweise mit dem **Non-Inflatable-Asset (NIA)-Schema** verbunden werden, das eine nicht aufblasbare Erstversorgung vorschreibt, oder mit anderen fortschrittlicheren Schemata, je nach Bedarf.

**RGB21** beschreibt NFT-artige Verträge oder im weiteren Sinne alle einzigartigen digitalen Inhalte, wie die Darstellung digitaler Medien (Bilder, Musik usw.). Es beschreibt nicht nur die Ausgabe und Übertragung eines einzelnen Assets, sondern umfasst auch Merkmale wie:


- Integrierte Unterstützung für die direkte Aufnahme einer Datei (bis zu 16 MB) in den Vertrag (für den Abruf auf der client-side);
- Die Möglichkeit für den Eigentümer, eine "*Gravur*" in die Historie einzutragen, um den früheren Besitz eines NFT zu beweisen.

**RGB25** ist ein hybrider Standard, der fungible und nicht-fungible Aspekte kombiniert. Er ist für teilweise fungible Vermögenswerte konzipiert, wie z.B. die Tokenisierung von Immobilien, bei der eine Immobilie aufgeteilt werden soll, während die Verbindung zu einem einzigen Stammvermögen beibehalten wird (mit anderen Worten: Sie haben fungible Teile eines Hauses, die mit einem nicht fungiblen Haus verbunden sind). Technisch gesehen kann diese Schnittstelle mit dem Schema **Collectible Fungible Asset (CFA)** verknüpft werden, das den Begriff der Aufteilung bei gleichzeitiger Rückverfolgung des ursprünglichen Vermögenswertes berücksichtigt.

#### Schnittstellen in der Entwicklung

Weitere Schnittstellen sind für speziellere Anwendungen geplant, aber noch nicht verfügbar:


- **RGB22**, das sich mit digitalen Identitäten befasst, um Identifier und On-Chain-Profile im RGB-Ökosystem zu verwalten;
- **RGB23**, für fortgeschrittene Zeitstempel, die einige der Ideen von *Opentimestamps* verwenden, aber mit Rückverfolgungsfunktionen;
- **RGB24**, das das Äquivalent eines dezentralen Domain Name Systems (DNS) ähnlich dem *Ethereum Name Service* anstrebt;
- **RGB26**, entwickelt für die Verwaltung von DAOs (*Dezentralisierte Autonome Organisation*) in einem komplexeren Format (Verwaltung, Abstimmung usw.);
- **RGB30**, sehr ähnlich wie RGB20, jedoch mit der Besonderheit, dass die dezentrale Erstausgabe berücksichtigt wird und Zustandserweiterungen verwendet werden. Dies würde für Vermögenswerte verwendet, deren Neuausgabe von mehreren Stellen verwaltet wird oder feineren Bedingungen unterliegt.

Je nach dem Datum, an dem Sie diesen Kurs besuchen, können diese Schnittstellen natürlich bereits in Betrieb und zugänglich sein.

#### Beispiel für eine Schnittstelle

Dieses Rust Code Snippet zeigt eine [RGB20](https://github.com/RGB-WG/rgb-std/blob/master/src/interface/rgb20.rs) Schnittstelle (fungibles Asset). Dieser Code stammt aus der Datei `rgb20.rs` in der Standard-RGB-Bibliothek. Werfen wir einen Blick darauf, um die Struktur einer Schnittstelle zu verstehen und zu sehen, wie sie eine Brücke zwischen der (im Schema definierten) Business Logic einerseits und den Funktionalitäten für Geldbörsen und Benutzer andererseits bildet.

```rust
// ...
fn rgb20() -> Iface {
    let types = StandardTypes::with(rgb20_stl());

    Iface {
        version: VerNo::V1,
        name: tn!("RGB20"),
        global_state: tiny_bmap! {
            fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
            fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
            fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
            fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
            fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
            fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
        },
        assignments: tiny_bmap! {
            fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
            fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
            fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
            fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
            fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
        },
        valencies: none!(),
        genesis: GenesisIface {
            metadata: Some(types.get("RGBContract.IssueMeta")),
            global: tiny_bmap! {
                fname!("spec") => ArgSpec::required(),
                fname!("data") => ArgSpec::required(),
                fname!("created") => ArgSpec::required(),
                fname!("issuedSupply") => ArgSpec::required(),
            },
            assignments: tiny_bmap! {
                fname!("assetOwner") => ArgSpec::many(),
                fname!("inflationAllowance") => ArgSpec::many(),
                fname!("updateRight") => ArgSpec::optional(),
                fname!("burnEpoch") => ArgSpec::optional(),
            },
            valencies: none!(),
            errors: tiny_bset! {
                SUPPLY_MISMATCH,
                INVALID_PROOF,
                INSUFFICIENT_RESERVES
            },
        },
        transitions: tiny_bmap! {
            tn!("Transfer") => TransitionIface {
                optional: false,
                metadata: None,
                globals: none!(),
                inputs: tiny_bmap! {
                    fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
                },
                assignments: tiny_bmap! {
                    fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
                },
                valencies: none!(),
                errors: tiny_bset! {
                    NON_EQUAL_AMOUNTS
                },
                default_assignment: Some(fname!("beneficiary")),
            },
            tn!("Issue") => TransitionIface {
                optional: true,
                metadata: Some(types.get("RGBContract.IssueMeta")),
                globals: tiny_bmap! {
                    fname!("issuedSupply") => ArgSpec::required(),
                },
                inputs: tiny_bmap! {
                    fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
                },
                assignments: tiny_bmap! {
                    fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
                    fname!("future") => ArgSpec::from_many("inflationAllowance"),
                },
                valencies: none!(),
                errors: tiny_bset! {
                    SUPPLY_MISMATCH,
                    INVALID_PROOF,
                    ISSUE_EXCEEDS_ALLOWANCE,
                    INSUFFICIENT_RESERVES
                },
                default_assignment: Some(fname!("beneficiary")),
            },
            tn!("OpenEpoch") => TransitionIface {
                optional: true,
                metadata: None,
                globals: none!(),
                inputs: tiny_bmap! {
                    fname!("used") => ArgSpec::from_required("burnEpoch"),
                },
                assignments: tiny_bmap! {
                    fname!("next") => ArgSpec::from_optional("burnEpoch"),
                    fname!("burnRight") => ArgSpec::required()
                },
                valencies: none!(),
                errors: none!(),
                default_assignment: Some(fname!("burnRight")),
            },
            tn!("Burn") => TransitionIface {
                optional: true,
                metadata: Some(types.get("RGBContract.BurnMeta")),
                globals: tiny_bmap! {
                    fname!("burnedSupply") => ArgSpec::required(),
                },
                inputs: tiny_bmap! {
                    fname!("used") => ArgSpec::from_required("burnRight"),
                },
                assignments: tiny_bmap! {
                    fname!("future") => ArgSpec::from_optional("burnRight"),
                },
                valencies: none!(),
                errors: tiny_bset! {
                    SUPPLY_MISMATCH,
                    INVALID_PROOF,
                    INSUFFICIENT_COVERAGE
                },
                default_assignment: None,
            },
            tn!("Replace") => TransitionIface {
                optional: true,
                metadata: Some(types.get("RGBContract.BurnMeta")),
                globals: tiny_bmap! {
                    fname!("replacedSupply") => ArgSpec::required(),
                },
                inputs: tiny_bmap! {
                    fname!("used") => ArgSpec::from_required("burnRight"),
                },
                assignments: tiny_bmap! {
                    fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
                    fname!("future") => ArgSpec::from_optional("burnRight"),
                },
                valencies: none!(),
                errors: tiny_bset! {
                    NON_EQUAL_AMOUNTS,
                    SUPPLY_MISMATCH,
                    INVALID_PROOF,
                    INSUFFICIENT_COVERAGE
                },
                default_assignment: Some(fname!("beneficiary")),
            },
            tn!("Rename") => TransitionIface {
                optional: true,
                metadata: None,
                globals: tiny_bmap! {
                    fname!("new") => ArgSpec::from_required("spec"),
                },
                inputs: tiny_bmap! {
                    fname!("used") => ArgSpec::from_required("updateRight"),
                },
                assignments: tiny_bmap! {
                    fname!("future") => ArgSpec::from_optional("updateRight"),
                },
                valencies: none!(),
                errors: none!(),
                default_assignment: Some(fname!("future")),
            },
        },
        extensions: none!(),
        error_type: types.get("RGB20.Error"),
        default_operation: Some(tn!("Transfer")),
        type_system: types.type_system(),
    }
}
```

In dieser Schnittstelle sind Ähnlichkeiten mit der Schema-Struktur zu erkennen: Wir finden eine Deklaration von Global State, Owned States, Vertragsoperationen (Genesis und Transitions) sowie eine Fehlerbehandlung. Die Schnittstelle konzentriert sich jedoch auf die Darstellung und Manipulation dieser Elemente für eine Wallet oder eine andere Anwendung.

Der Unterschied zu Schema liegt in der Art der Typen. Schema verwendet strenge Typen (wie `FungibleType::Unsigned64Bit`) und eher technische Bezeichner. Die Schnittstelle verwendet Feldnamen, Makros (`fname!()`, `tn!()`) und Verweise auf Argumentklassen (`ArgSpec`, `OwnedIface::Rights`...). Das Ziel ist es, das funktionale Verständnis und die Organisation der Elemente für die Wallet zu erleichtern.

Darüber hinaus kann die Schnittstelle zusätzliche Funktionalitäten in das Basisschema einführen (z.B. die Verwaltung eines `burnEpoch`-Rechts), solange dies mit der endgültigen validierten client-side Logik konsistent bleibt. Der Abschnitt "script" von AluVM im Schema gewährleistet die kryptographische Gültigkeit, während die Schnittstelle beschreibt, wie der Benutzer (oder die Wallet) mit diesen Zuständen und Übergängen interagiert.

#### Globaler Zustand und Zuweisungen

Im Abschnitt `global_state` finden wir Felder wie `spec` (Vermögenswertbeschreibung), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Dies sind Felder, die die Wallet lesen und darstellen kann. Zum Beispiel:


- `spec` zeigt die Token-Konfiguration an;
- mit `issuedSupply` oder `burnedSupply` erhalten wir die Gesamtzahl der ausgegebenen oder verbrannten Token, usw.

Im Abschnitt `assignments` (Zuweisungen) werden verschiedene Rollen oder Rechte definiert. Zum Beispiel:


- `assetOwner` entspricht dem Besitz von Token (es ist der fungible *Owned State*);
- `burnRight` entspricht der Fähigkeit, Token zu burnen (vernichten);
- `updateRight` entspricht dem Recht, das Asset umzubenennen.

Das Schlüsselwort `public` oder `private` (z.B. `AssignIface::public(...)`) gibt an, ob diese Zustände sichtbar (`public`) oder vertraulich (`private`) sind. Die Schlüsselwörter `Req::NoneOrMore` und `Req::Optional` geben das erwartete Vorkommen an.

#### Genesis und Transitions

Der Teil `genesis` beschreibt, wie das Asset initialisiert wird:


- Die Felder `spec`, `data`, `created` und `issuedSupply` sind obligatorisch (`ArgSpec::required()`);
- Zuweisungen wie `assetOwner` können in mehreren Kopien vorhanden sein (`ArgSpec::many()`), so dass Token an mehrere Erstbesitzer verteilt werden können;
- Felder wie `inflationAllowance` oder `burnEpoch` können (müssen aber nicht) in Genesis enthalten sein.

Dann definiert die Schnittstelle für jede Transition (`Transfer`, `Issue`, `Burn`...), welche Felder die Operation als Eingabe erwartet, welche Felder die Operation als Ausgabe produziert und welche Fehler auftreten können. Zum Beispiel:

**Transition:**


- Inputs : `previous` → muss ein `assetOwner` sein;
- Zuweisungen : `beneficiary` (Begünstigter)  → wird ein neuer `assetOwner` sein;
- Fehler: `NON_EQUAL_AMOUNTS` (die Wallet kann also Fälle behandeln, in denen die Eingabesumme nicht der Ausgabesumme entspricht).

**Transition `Issue` :**


- Optional (`optional: true`), da die zsätzliche Emission nicht unbedingt aktiviert wird;
- Inputs: `used` → eine `inflationAllowance`, d.h. die Erlaubnis, weitere Token hinzuzufügen;
- Zuweisungen: `beneficiary` (erhält neue Token) und `future` (verbleibende `inflationAllowance`);
- Mögliche Fehler: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE`, etc.

**Burn-übergang :**


- Inputs : `used` → ein `burnRight`;
- Globals : `burnedSupply` erforderlich;
- Zuweisungen: `future` → eine mögliche Fortsetzung des `burnRight`, wenn wir nicht alles geburned (vernichtet) haben;
- Fehler: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.

Jeder Vorgang wird daher so beschrieben, dass er für eine Wallet lesbar ist. Dies ermöglicht es, eine grafische Schnittstelle anzuzeigen, auf der der Benutzer deutlich sehen kann: "Sie haben das Recht zu burnen. Möchten Sie einen bestimmten Betrag burnen? Der Code weiß, dass er ein Feld `burnedSupply` ausfüllen und prüfen muss, ob das `burnRight` gültig ist.

Zusammenfassend ist es wichtig zu bedenken, dass eine Schnittstelle, auch wenn sie noch so vollständig ist, für sich genommen nicht die interne Logik des Vertrags definiert. Der Kern der Arbeit wird vom **Schema** erledigt, das strikte Typen, die Genesis-Struktur, Übergänge usw. enthält. Die Schnittstelle stellt diese Elemente einfach in einer intuitiveren und benannten Weise für die Verwendung in einer Anwendung zur Verfügung.

Dank der Modularität von RGB kann die Schnittstelle aktualisiert werden (z.B. durch Hinzufügen eines `Rename`-Übergangs, Korrektur der Anzeige eines Feldes usw.), ohne dass der gesamte Vertrag neu geschrieben werden muss. Die Benutzer dieser Schnittstelle können dann sofort von diesen Verbesserungen profitieren, sobald sie die `.rgb` oder `.rgba` Datei aktualisieren.

Sobald Sie jedoch eine Schnittstelle deklariert haben, müssen Sie sie mit dem entsprechenden Schema verknüpfen. Dies geschieht über die ***Schnittstellenimplementierung***, die angibt, wie jedes benannte Feld (z. B. `fname!("assetOwner")`) auf die im Schema definierte strikte ID (z.B. `OS_ASSET`) abgebildet werden soll. Dadurch wird beispielsweise sichergestellt, dass, wenn eine Wallet ein Feld `burnRight` manipuliert, dies der Zustand ist, der im Schema die Fähigkeit zum Burnen von Token beschreibt.

### Schnittstellenimplementierung

In der RGB-Architektur haben wir gesehen, dass jede Komponente (Schema, Schnittstelle usw.) unabhängig entwickelt und kompiliert werden kann. Es gibt jedoch noch ein unverzichtbares Element, das diese verschiedenen Bausteine miteinander verbindet: die ***Schnittstellenimplementierung***. Diese bildet die im Schema (auf der Seite der Business Logic) definierten Bezeichner oder Felder explizit auf die in der Schnittstelle (auf der Seite der Präsentation und Benutzerinteraktion) deklarierten Namen ab. Wenn also eine Brieftasche einen Vertrag lädt, kann sie genau verstehen, welches Feld was bedeutet und wie eine in der Schnittstelle genannte Operation mit der Logik des Schemas zusammenhängt.

Ein wichtiger Punkt ist, dass die Interface-Implementierung nicht notwendigerweise alle Funktionen des Schemas und auch nicht alle Interface-Felder offenlegen soll: Sie kann auf eine Teilmenge beschränkt werden. In der Praxis ist es dadurch möglich, bestimmte Aspekte des Schemas einzuschränken oder zu filtern. Zum Beispiel könnte ein Schema vier Operationstypen haben, aber eine Implementierungsschnittstelle, die nur zwei von ihnen in einem bestimmten Kontext abbildet. Umgekehrt können wir, wenn eine Schnittstelle zusätzliche Endpunkte vorschlägt, beschließen, diese hier nicht zu implementieren.

Hier ist ein klassisches Beispiel für die Schnittstellenimplementierung, bei der wir ein *Non-Inflatable Asset* (NIA)-Schema mit der RGB20-Schnittstelle verknüpfen:

```rust
fn nia_rgb20() -> IfaceImpl {
    let schema = nia_schema();
    let iface = Rgb20::iface();

    IfaceImpl {
        version: VerNo::V1,
        schema_id: schema.schema_id(),
        iface_id: iface.iface_id(),
        script: none!(),
        global_state: tiny_bset! {
            NamedField::with(GS_NOMINAL, fname!("spec")),
            NamedField::with(GS_DATA, fname!("data")),
            NamedField::with(GS_TIMESTAMP, fname!("created")),
            NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
        },
        assignments: tiny_bset! {
            NamedField::with(OS_ASSET, fname!("assetOwner")),
        },
        valencies: none!(),
        transitions: tiny_bset! {
            NamedType::with(TS_TRANSFER, tn!("Transfer")),
        },
        extensions: none!(),
    }
}
```

In dieser Implementierungsschnittstelle :


- Referenzieren wir explizit das Schema über `nia_schema()` und die Schnittstelle über `Rgb20::iface()`. Die Aufrufe `schema.schema_id()` und `iface.iface_id()` werden verwendet, um die Schnittstellenimplementierung auf der Kompilierungsseite zu verankern (dies assoziiert die kryptographischen Bezeichner dieser beiden Komponenten);
- Wird ein Mapping zwischen Schema-Elementen und Interface-Elementen erstellt. Zum Beispiel wird das Feld `GS_NOMINAL` im Schema mit der Zeichenkette `"spec"` auf der Schnittstellenseite verknüpft (`NamedField::with(GS_NOMINAL, fname!("spec"))`). Dasselbe tun wir für Operationen wie `TS_TRANSFER`, die wir mit `"Transfer"` in der Schnittstelle verknüpfen...;
- Wir können sehen, dass es keine Valenzen (`valencies: none!()`) oder Erweiterungen (`extensions: none!()`) gibt, was die Tatsache widerspiegelt, dass dieser NIA-Vertrag diese Merkmale nicht verwendet.

Das Ergebnis nach der Kompilierung ist eine separate `.rgb`- oder `.rgba`-Datei, die zusätzlich zum Schema und zur Schnittstelle in die Wallet importiert wird. Somit weiß die Software, wie sie diesen NIA-Vertrag (dessen Logik durch das Schema beschrieben wird) konkret mit der "RGB20"-Schnittstelle (die menschliche Namen und einen Interaktionsmodus für fungible Token bereitstellt) verbinden kann, indem sie diese Schnittstellenimplementierung als Gateway zwischen den beiden verwendet.

#### Warum eine separate Schnittstellenimplementierung?

Die Trennung erhöht die Flexibilität. Ein einziges Schema kann mehrere verschiedene Schnittstellenimplementierungen haben, die jeweils einen anderen Satz von Funktionalitäten abbilden. Darüber hinaus kann die Schnittstellenimplementierung selbst weiterentwickelt oder umgeschrieben werden, ohne dass eine Änderung des Schemas oder der Schnittstelle erforderlich ist. Damit wird das RGB-Prinzip der Modularität beibehalten: Jede Komponente (Schema, Schnittstelle, Schnittstellenimplementierung) kann unabhängig voneinander versioniert und aktualisiert werden, solange die vom Protokoll auferlegten Kompatibilitätsregeln beachtet werden (gleiche Bezeichner, Konsistenz der Typen usw.).

Im konkreten Fall muss die Wallet, wenn sie einen Vertrag laden will:


- Das kompilierte **Schema** laden (um die Struktur der Business Logic zu kennen);
- Die kompilierte **Schnittstelle** laden (um Namen und benutzerseitige Operationen zu verstehen);
- Die kompilierte **Schnittstellenimplementierung** laden (zur Verknüpfung von Schema-Logik mit Schnittstellennamen, Operation für Operation, Feld für Feld).

Diese modulare Architektur ermöglicht Einsatzszenarien wie:


- Bestimmte Vorgänge für bestimmte Benutzer einschränken: eine partielle Implementierungsschnittstelle anbieten, die nur den Zugang zu den grundlegenden Übertragungen ermöglicht, ohne z.B. Burn- oder Aktualisierungsfunktionen anzubieten;
- Änderungsdarstellung: Entwurf einer Schnittstellenimplementierung, die ein Feld in der Schnittstelle umbenennt oder anders zuordnet, ohne die Grundlage des Vertrags zu ändern;
- Unterstützung mehrerer Schemata: Eine Wallet kann mehrere Schnittstellenimplementierungen für denselben Schnittstellentyp laden, um verschiedene Schemata (verschiedene Token-Logiken) zu handhaben, sofern ihre Struktur kompatibel ist.

Im nächsten Kapitel werden wir uns ansehen, wie eine Vertragsübertragung funktioniert und wie RGB-Invoices (Rechnungen) erstellt werden.

## Vertragsüberweisungen

<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>

:::video id=75eb5a8d-1910-4155-b5e3-81204c9a8901:::

In diesem Kapitel werden wir den Prozess einer Vertragsüberweisung im RGB-Ökosystem analysieren. Zur Veranschaulichung betrachten wir Alice und Bob, unsere üblichen Protagonisten, die einen RGB-Vermögenswert tauschen möchten. Außerdem zeigen wir einige Auszüge aus dem Kommandozeilentool `rgb`, um zu sehen, wie es in der Praxis funktioniert.

### Verstehen der RGB-Vertragsüberweisung

Nehmen wir ein Beispiel für eine Überweisung zwischen Alice und Bob. In diesem Beispiel nehmen wir an, dass Bob gerade erst anfängt, RGB zu nutzen, während Alice bereits RGB-Vermögenswerte in ihrer Wallet hat. Wir werden sehen, wie Bob seine Umgebung einrichtet, den entsprechenden Vertrag importiert, dann eine Überweisung von Alice anfordert und schließlich wie Alice die eigentliche Transaktion auf der Bitcoin-Blockchain durchführt.

#### 1) Installieren der RGB-Wallet

Zunächst muss Bob eine RGB-Wallet installieren, d.h. eine Software, die mit dem Protokoll kompatibel ist. Diese enthält zu Beginn keine Verträge. Bob benötigt außerdem:


- Eine Bitcoin-Wallet zur Verwaltung seiner UTXOs;
- Eine Verbindung zu einem Bitcoin-Knoten (oder zu einem Electrum-Server), damit er seine UTXOs identifizieren und seine Transaktionen im Netzwerk verbreiten kann.

Zur Erinnerung: **Owned States** in RGB beziehen sich auf Bitcoin UTXOs. Wir müssen daher immer in der Lage sein, UTXOs in einer Bitcoin-Transaktion zu verwalten und auszugeben, die kryptographische Commitments (`Tapret` oder `Opret`) enthalten, die auf RGB-Daten verweisen.

#### 2) Beschaffung der Vertragsinformationen

Bob muss dann die Vertragsdaten abrufen, an denen er interessiert ist. Diese Daten können über jeden beliebigen Kanal zirkulieren: Website, E-Mail, Messaging-Anwendung... In der Praxis werden sie in einem ***consignment*** zusammengefasst, d.h. in einem kleinen Datenpaket, das folgendes enthält:


- Die **Genesis**, die den Ausgangszustand des Vertrags definiert;
- Das **Schema**, das die Business Logic beschreibt (struic types, Validierungsskripte usw.);
- Die **Schnittstelle**, die die Darstellungsschicht definiert (Feldnamen, zugängliche Operationen);
- Die **Schnittstellenimplementierung**, die das Schema konkret mit der Schnittstelle verbindet.

![RGB-Bitcoin](assets/en/075.webp)

Die Gesamtgröße liegt oft in der Größenordnung von einigen Kilobytes, da jede Komponente im Allgemeinen weniger als 200 Bytes groß ist. Es kann auch möglich sein, dieses consignemnt in Base58, über zensurresistente Kanäle (wie z.B. Nostr oder über das Lightning Network) oder als QR-Code zu versenden.

#### 3) Vertragsimport und -validierung

Sobald Bob das consignemnt erhalten hat, importiert er es in seine RGB-Wallet. Diese wird dann:


- Prüfen, ob die Genesis und das Schema gültig sind;
- Schnittstelle und Schnittstellenimplementierung laden;
- Den client-side Stash aktualisieren.

Bob kann nun den Vermögenswert in seiner Wallet sehen (auch wenn er ihn noch nicht besitzt) und verstehen, welche Felder verfügbar sind, welche Operationen möglich sind... Dann muss er sich mit einer Person in Verbindung setzen, die den zu übertragenden Vermögenswert tatsächlich besitzt. In unserem Beispiel ist dies Alice.

Der Prozess, um herauszufinden, wer einen bestimmten RGB-Vermögesnwert besitzt, ähnelt der Suche nach einem Bitcoin-Halter. Die Details dieser Verbindung hängen von der Nutzung ab (Marktplätze, private Chat-Kanäle, Rechnungsstellung, Verkauf von Waren und Dienstleistungen, Gehalt...).

#### 4) Rechnungsausstellung

Um die Überweisung eines RGB-Vermögenswertes einzuleiten, muss Bob zunächst eine Rechnung (invoice) ausstellen. Diese Rechnung wird verwendet, um:


- Alice die Art der Operation, die durchgeführt werden soll mitzuteilen (z. B. ein `transfer` einer RGB20-Schnittstelle);
- Alice die *Siegeldefinition* von Bob bereitzustellen (d.h. den UTXO, an dem er den Vermögenswert erhalten möchte);
- Die gewünschte Menge des Vermögenswertes anzugeben (z.B. 100 Einheiten).

Bob verwendet das Programm `rgb` auf der Kommandozeile. Angenommen, er will 100 Einheiten eines Tokens, dessen `ContractId` bekannt ist, will sich auf `Tapret` verlassen und gibt dessen UTXO an (`456e3..dfe1:0`):

```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```

Am Ende dieses Kapitels werden wir uns die Struktur von RGB-Rechnungen genauer ansehen.

#### 5) Rechnungsübermittlung

Die generierte Rechnung (z.B. als URL: `rgb:2WBcas9.../RGB20/100+utxob:...`) enthält alle Informationen, die Alice zur Vorbereitung der Überweisung benötigt. Wie das consignemnt kann sie kompakt kodiert (Base58 oder ein anderes Format) und über einen Messenger, E-Mail, Nostr... versandt werden.

![RGB-Bitcoin](assets/en/076.webp)

#### 6) Transaktionsvorbereitung seitens Alice

Alice erhält die Rechnung von Bob. In ihrer RGB-Wallet hat sie einen Stash, der den zu übertragenden Vermögenswert enthält. Um den UTXO mit dem Vermögenswert auszugeben, muss sie zunächst eine PSBT (*Partially Signed Bitcoin Transaction*), d.h. eine unvollständige Bitcoin-Transaktion, unter Verwendung des UTXO, den sie hat, erzeugen:

```bash
alice$ wallet construct tx.psbt
```

Diese (vorerst unsignierte) Basistransaktion wird zur Verankerung des kryptografischen Commitments der Überweisung an Bob verwendet. Der UTXO von Alice wird also ausgegeben, und in dem Output wird das `Tapret` oder `Opret` Commitment für Bob platziert.

#### 7) Erstellung eines Überweisungs-Consignments

Als nächstes erstellt Alice das ***letzte Consignment*** (manchmal auch "Transfer-Consignment" genannt) mit dem Befehl:

```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```

Diese neue Datei `consignment.rgb` enthält:


- Die vollständige Historie der für die Validierung des Vermögenswerts erforderlichen Zustandsübergänge (state transitions) bis zum jetzugen Zeitpunkt (seit Genesis);
- Den neuen Zustandsübergang, der Vermögenswerte von Alice an Bob überträgt, entsprechend der von Bob ausgestellten Rechnung;
- Die unvollständige Bitcoin-Transaktion (*Zeugentransaktion*) (`tx.psbt`), die Alices Single-use Seal ausgibt, modifiziert, um das kryptografische Commitment gegenüber Bob einzuschließen.

In diesem Stadium wird die Transaktion noch nicht an das Bitcoin-Netzwerk übertragen/veröffentlicht. Das Consignments ist größer als ein einfaches Consignment, da es die gesamte Historie (*proof chain*) enthält, um die Legitimität des Vermögenswertes zu beweisen.

#### 8) Bob prüft und akzeptiert das Consignment

Alice sendet dieses **letzte Consignment** an Bob. Bob wird dann:


- Die Gültigkeit des Zustandsübergangs prüfen (sicherstellen, dass die Historie konsistent ist, dass die Vertragsregeln eingehalten werden usw.);
- Es zu seinem lokalen Stash hinzufügen;
- Eventuell eine Unterschrift (`sig:...`) auf der Sendung erzeugen, um zu beweisen, dass er sie geprüft und genehmigt hat (manchmal auch "*Zahlungsschein*" (payslip) genannt).

```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```

![RGB-Bitcoin](assets/en/077.webp)

#### 9) Option: Bob schickt eine Bestätigung an Alice zurück (*Zahlungsschein*)

Wenn Bob möchte, kann er diese Signatur an Alice zurücksenden. Dies zeigt an:


- Dass er den Übergang als gültig anerkennt;
- Dass er mit dem Veröffentlichen der Bitcoin-Transaktion einverstanden ist.

Dies ist nicht obligatorisch, kann Alice aber die Sicherheit geben, dass es keine späteren Streitigkeiten über die Übertragung des Vermögenswertes gibt.

#### 10) Alice unterzeichnet und veröffentlicht die Transaktion

Alice kann dann :


- Bobs Unterschrift prüfen (`rgb check <sig>`) ;
- Die *Zeugentransaktion* unterschreiben, die immer noch eine PSBT ist (`Wallet sign`);
- Die Zeugentransaktion im Bitcoin-Netzwerk veröffentlicnen (`-publish`).

```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```

![RGB-Bitcoin](assets/en/078.webp)

Mit der Bestätigung dieser Transaktion ist die Überweisung abgeschlossen. Bob wird neuer Eigentümer des Vermögenswerts: Er verfügt nun über einen "Owned State", der auf den von ihm kontrollierten UTXO verweist, was durch das Vorhandensein des Comittments in der Transaktion belegt wird.

Zusammenfassend lässt sich der gesamte Überweisungsprozess wie folgt beschreiben:

![RGB-Bitcoin](assets/en/079.webp)

### Vorteile der RGB-Überweisung


- **Vertraulichkeit**:

Nur Alice und Bob haben Zugang zu allen Zustandsübergangsdaten. Sie tauschen diese Informationen außerhalb der Blockchain über consignments aus. Die kryptografischen Commitments in der Bitcoin-Transaktion verraten weder die Art des Vermögenswerts noch den Betrag, was eine weitaus größere Vertraulichkeit garantiert als andere On-Chain-Token-Systeme.


- **client-side Validierung**:

Bob kann die Konsistenz der Überweisung überprüfen, indem er das *Consignment* mit den *Anchors* in der Bitcoin-Blockchain vergleicht. Er braucht keine Validierung durch Dritte. Alice muss nicht den gesamten Verlauf in der Blockchain veröffentlichen, was die Belastung des Basisprotokolls verringert und die Vertraulichkeit verbessert.


- **Vereinfachte Atomizität**:

Komplexe Tauschvorgänge (z.B. atomare Tauschvorgänge (atomic swaps) zwischen BTC und einem RGB-Vermögenswert) können innerhalb einer einzigen Transaktion durchgeführt werden, so dass keine HTLC- oder PTLC-Skripte erforderlich sind. Wenn die Vereinbarung nicht veröffentlicht wird, kann jeder seine UTXOs auf andere Weise wiederverwenden.

### Übersichtsdiagramm der Überweisung

Bevor wir uns die Rechnungen genauer ansehen, hier eine Übersicht über den Gesamtablauf einer RGB-Überweisung:


- Bob installiert eine RGB-Wallet und erhält das erste Vertragsconsignment;
- Bob stellt eine Rechnung aus, in der er den UTXO angibt, der den Vermögenswert erhalten soll;
- Alice erhält die Rechnung, erstellt die PSBT und erzeugt das letzte Consignment;
- Bob nimmt es an, prüft es, fügt die Daten seinem Stash hinzu und unterschreibt (*Zahlschein*), falls erforderlich;
- Alice veröffentlicht die Transaktion im Bitcoin-Netzwerk;
- Mit der Bestätigung der Transaktion wird die Überweisung offiziell.

![RGB-Bitcoin](assets/en/080.webp)

Die Überweisung veranschaulicht die ganze Stärke und Flexibilität des RGB-Protokolls: ein privater Austausch, der auf der client-side validiert wird, minimal und diskret in der Bitcoin-Blockchain verankert ist und die besten Sicherheitsmerkmale des Protokolls beibehält (kein Risiko von Doppelausgaben). Dies macht RGB zu einem vielversprechenden Ökosystem für Werttransfers, die vertraulicher und skalierbarer sind als programmierbare On-Chain-Blockchains.

### RGB-Rechnungen

In diesem Abschnitt erläutern wir im Detail, wie **Rechnungen** (invoices) im RGB-Ökosystem funktionieren und wie sie die Durchführung von Operationen (insbesondere Überweisungen) mit einem Vertrag ermöglichen. Zunächst werden wir uns die verwendeten Bezeichner (identifier) ansehen, dann ihre Kodierung und schließlich die Struktur einer Rechnung, die als URL ausgedrückt wird (ein Format, das für die Verwendung in Wallets praktikabel genug ist).

#### Bezeichner und Kodierung

Für jedes der folgenden Elemente wird ein eindeutiger Bezeichner (identifier) festgelegt:


- Ein RGB-Vertrag;
- Sein Schema (Business Logic);
- Seine Schnittstelle und Schnittstellenimplementierung;
- Seine Vermögenswerte (Token, NFT, etc.).

Diese Eindeutigkeit ist sehr wichtig, da jede Komponente des Systems unterscheidbar sein muss. So darf beispielsweise ein Vertrag X nicht mit einem anderen Vertrag Y verwechselt werden, und zwei verschiedene Schnittstellen (z.B. RGB20 vs. RGB21) müssen eindeutige Bezeichner haben.

Um diese Bezeichner sowohl effizient (geringe Größe) als auch lesbar zu machen, verwenden wir:


- Base58-Kodierung, die die Verwendung verwirrender Zeichen (z.B. `0` und der Buchstabe `O`) vermeidet und relativ kurze Zeichenketten liefert;
- Ein Präfix, das die Art des Identifikators angibt, normalerweise in Form von `rgb:` oder einer ähnlichen URN.

Zum Beispiel könnte eine `ContractId` durch so etwas dargestellt werden:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Das Präfix `rgb:` bestätigt, dass es sich um einen RGB-Bezeichner und nicht um einen HTTP-Link oder ein anderes Protokoll handelt. Dank dieses Präfixes sind Wallets in der Lage, die Zeichenfolge korrekt zu interpretieren.

#### Bezeichnersegmentierung

RGB-Bezeichner sind oft recht lang, da die zugrunde liegende (kryptografische) Sicherheit Felder von 256 Bit oder mehr erfordern kann. Um das Lesen und Überprüfen durch Menschen zu erleichtern, *teilen* wir diese Zeichenfolgen in mehrere Blöcke, die durch einen Bindestrich (`-`) getrennt sind. Anstelle einer langen, ununterbrochenen Zeichenkette wird sie also in kürzere Blöcke unterteilt. Diese Praxis ist bei Kreditkarten- oder Telefonnummern üblich und gilt auch hier, um die Überprüfung zu erleichtern. So kann zum Beispiel einem Nutzer oder Partner gesagt werden: "*Bitte prüfen Sie, ob der dritte Block `9GEgnyMj7`* ist", anstatt alles auf einmal vergleichen zu müssen. Der letzte Block wird oft als **Prüfsumme** verwendet, um ein System zur Erkennung von Fehlern oder Tippfehlern zu haben.

Ein Beispiel: Eine `ContractId` in base58 kodiert und segmentiert könnte lauten:

```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Jeder der Bindestriche unterteilt die Zeichenfolge in Abschnitte. Dies hat keinen Einfluss auf die Semantik des Codes, sondern nur auf seine Darstellung.

#### Verwendung von URLs für Rechnungen

Eine RGB-Rechnung wird als URL dargestellt. Das bedeutet, dass sie angeklickt oder gescannt werden kann (wie ein QR-Code), und eine Wallet kann sie direkt interpretieren, um eine Transaktion durchzuführen. Diese Einfachheit der Interaktion unterscheidet sich von einigen anderen Systemen, bei denen man verschiedene Daten in verschiedene Felder der Software kopieren und einfügen muss.

Eine Rechnung für einen fungiblen Token (z.B. einen RGB20-Token) könnte wie folgt aussehen:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Analysieren wir diese URL:


- **`rgb:`** (Präfix): zeigt an, dass es sich um einen Link, der das RGB-Protokoll aufruft (analog zu `http:` oder `bitcoin:` in anderen Zusammenhängen) handelt;
- **`2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`**: steht für die `ContractId` des Tokens, die man manipulieren möchte;
- **`rGB20/100`**: zeigt an, dass die `RGB20`-Schnittstelle verwendet wird und dass 100 Einheiten des Vermögenswertes angefordert werden. Die Syntax lautet: `Interface/amount` (Schnittstelle/Menge);
- **`+utxob:`**: gibt an, dass Informationen über den Empfänger-UTXO (genauer gesagt, die Definition des Single-use Seals) hinzugefügt werden;**
- **`egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`**: dies ist der *blinded* (verblendete) UTXO (oder Siegeldefinition). Mit anderen Worten: Bob hat seine genaue UTXO maskiert, so dass der Absender (Alice) nicht weiß, wie die genaue Adresse lautet. Sie weiß nur, dass es ein gültiges Siegel gibt, das sich auf einen von Bob kontrollierten UTXO bezieht.

Die Tatsache, dass alles unter einer einzigen URL zu finden ist, macht dem Nutzer das Leben leichter: ein einfacher Klick oder ein Scan in der Wallet, und der Vorgang kann ausgeführt werden.

Man könnte sich Systeme vorstellen, bei denen anstelle der `ContractId` eine einfache Kennung (z. B. `USDT`) verwendet wird. Dies würde jedoch große Vertrauens- und Sicherheitsprobleme aufwerfen: eine Kennung ist keine eindeutige Referenz (mehrere Verträge könnten behaupten, `USDT` zu heißen). Mit RGB wollen wir einen eindeutigen, kryptografischen Bezeichner. Daher die 256-Bit-Zeichenkette, kodiert in base58 und segmentiert. Der Nutzer weiß, dass er genau den Vertrag manipuliert, dessen ID "2WBcas9-yjz..." lautet, und keinen anderen.

#### Zusätzliche URL-Parameter

Man kann der URL auch zusätzliche Parameter hinzufügen, genau wie bei HTTP, z.B. :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```


- `?sig=...`: steht beispielsweise für eine Signatur, die mit der Rechnung verbunden ist und die von einigen Wallets überprüft werden kann;
- Wenn eine Wallet diese Signatur nicht verwaltet, ignoriert sie diesen Parameter einfach.

Nehmen wir den Fall eines NFT über die RGB21-Schnittstelle. Wir könnten dieses Beispiel haben:

```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Hier sehen wir:


- **`rgb:`**: URL-Präfix;
- **`7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: Vertrags-ID (NFT);
- **`rGB21`**: Schnittstelle für nicht fungible Vermögenswerte (NFT);
- **`dbwzvSu-4BZU81jEp-...`**: ein expliziter Verweis auf den eindeutigen Teil des NFT, z.B. ein Hash des Datenblob (Medien, Metadaten...) ;
- **`+utxob:egXsFnw-...`**: die Siegeldefinition.

Die Idee ist dieselbe: Übermittlung eines eindeutigen Links, den die Wallet interpretieren kann und der den zu übertragenden Vermögenswert eindeutig identifiziert.

#### Andere Operationen über URL

RGB-URLs werden nicht nur verwendet, um eine Überweisung anzufordern. Sie können auch fortgeschrittenere Vorgänge kodieren, wie die Ausgabe neuer Token (*issuance*). Zum Beispiel:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Hier finden wir:


- `rgb:` : Protokoll;
- `2WBcas9-...`: Vertrags-ID ;
- `rGB20/issue/100000`: zeigt an, dass Sie den Übergang "*Issue*" aufrufen möchten, um weitere 100.000 Token zu erstellen;
- `+utxob:`: die Siegeldefinition.

Die Wallet könnte zum Beispiel verstehen: "Ich wurde gebeten, über die Schnittstelle `RGB20` eine `Ausgabe` für diesen oder jenen Vertrag über 100.000 Einheiten zugunsten dieses oder jenen Single-use seals durchzuführen."

Nachdem wir uns nun die wichtigsten Elemente der RGB-Programmierung angesehen haben, werde ich dir im nächsten Kapitel erklären, wie du einen RGB-Vertrag erstellst.

## Entwerfen von Smart Contracts

<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>

:::video id=a3ad6dcd-90b8-4272-9dfc-76c85c859167:::

In diesem Kapitel gehen wir Schritt für Schritt durch, wie man einen Vertrag mit Hilfe des Kommandozeilen-Tools `rgb` erstellt. Das Ziel ist es, zu zeigen, wie man das CLI (Command Line Interface, Kommandozeilen-Schnittstelle) installiert und bedient, ein **Schema** kompiliert, die **Schnittstelle** und die **Schnittstellenimplementierung** importiert und dann ein Asset ausgibt (*issue*). Wir werden uns auch die zugrundeliegende Logik ansehen, einschließlich Kompilierung und Zustandsüberprüfung. Am Ende dieses Kapitels solltest du in der Lage sein, den Prozess zu reproduzieren und deine eigenen RGB-Verträge zu erstellen.

Zur Erinnerung: Die interne Logik von RGB basiert auf Rust-Bibliotheken, die du als Entwickler in deine Projekte importieren kannst, um den client-side Validierungsteil zu verwalten. Darüber hinaus arbeitet das Team der LNP/BP Association an bindings für andere Sprachen, was aber noch nicht abgeschlossen ist. Darüber hinaus entwickeln andere Unternehmen wie Bitfinex ihre eigenen Integrationsstacks (wir werden in den letzten beiden Kapiteln des Kurses darüber sprechen). Für den Moment ist daher das `rgb` CLI die offizielle Referenz, auch wenn sie noch relativ unausgereift ist.

### Installation und Präsentation des rgb-Tools

Der Hauptbefehl heißt einfach `rgb`. Das Tool ist so konzipiert, dass es an `git` erinnert, mit einer Reihe von Unterbefehlen für die Bearbeitung von Verträgen, deren Aufruf, die Ausgabe von Vermögenswerten und so weiter. Bitcoin Wallet ist derzeit noch nicht integriert, wird aber in einer der nächsten Versionen (0.11) integriert sein. Diese nächste Version wird es Nutzern ermöglichen, ihre Wallets (über Deskriptoren) direkt von `rgb` aus zu erstellen und zu verwalten, einschließlich PSBT-Generierung, Kompatibilität mit externer Hardware (z.B. einer Hardware-Wallet) zum Signieren und Interoperabilität mit Software wie Sparrow. Dies wird das gesamte Szenario der Ausgabe und Übertragung von Vermögenswerten vereinfachen.

#### Installation über Cargo

Wir installieren das Tool in Rust mit:

```bash
cargo install rgb-contracts --all-features
```

(Hinweis: Die crate heißt `rgb-contracts`, und der installierte Befehl wird `rgb` heißen. Wenn eine Kiste mit dem Namen `rgb` bereits existiert, könnte es eine Kollision gegeben haben, daher der Name)

Die Installation kompiliert eine große Anzahl von dependencies (Abhängigkeiten) (z.B. Befehls-Parsing, Electrum-Integration, Verwaltung von Zero-Knowledge-Proofs usw.).

Sobald die Installation abgeschlossen ist, haben wir diesen Befehl zur Verfügung:

```bash
rgb
```

Wenn du `rgb` (ohne Argumente) ausführst, wird eine Liste der verfügbaren Unterbefehle angezeigt, z. B. `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer` usw. Du kannst das lokale Speicherverzeichnis (ein stash, der alle Protokolle, Schemata und Implementierungen enthält) ändern, das Netzwerk (Testnet, Mainnet) wählen oder deinen Electrum-Server konfigurieren.

![RGB-Bitcoin](assets/en/081.webp)

#### Erster Überblick über die Befehle

Wenn du den folgenden Befehl ausführst, siehst du, dass eine "RGB20"-Schnittstelle bereits standardmäßig integriert ist:

```bash
rgb interfaces
```

Wenn diese Schnittstelle nicht integriert ist, klone das Schnittstellen repository:

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Kompiliere es:

```bash
cargo run
```

Importiere dann die Schnittstelle deiner Wahl:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-Bitcoin](assets/en/082.webp)

Andererseits wird uns gesagt, dass noch kein Schema in die Software importiert wurde. Es gibt auch noch keinen Vertrag im Stash. Um dies zu sehen, führe diesen Befehl aus:

```bash
rgb schemata
```

Du kannst dann das Repository klonen, um bestimmte Schemata abzurufen:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-Bitcoin](assets/en/083.webp)

Dieses Repository enthält in seinem Verzeichnis `src/` mehrere Rust-Dateien (z.B. `nia.rs`), die Schemata definieren (NIA für "*Non Inflatable Asset*", UDA für "*Unique Digital Asset*", usw.). Um zu kompilieren, verwendest du den Befehl :

```bash
cd rgb-schemata
cargo run
```

Dies erzeugt mehrere `.rgb` und `.rgba` Dateien, die den kompilierten Schemata entsprechen. Zum Beispiel findest du `NonInflatableAsset.rgb`.

#### Schema und Schnittstellenimplementierung importieren

Du kannst nun das Schema in `rgb` importieren:

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-Bitcoin](assets/en/084.webp)

Dadurch wird es dem lokalen Stash hinzugefügt. Wenn wir den folgenden Befehl ausführen, sehen wir, dass das Schema jetzt erscheint:

```bash
rgb schemata
```

### Vertragserstellung (Vermögenswertausgabe)

Es gibt zwei Möglichkeiten, einen neuen Vermögenswert zu erstellen:


- Entweder verwenden wir ein Skript oder Code in Rust, der einen Vertrag erstellt, indem er Schemafelder ausfüllt (Global States, Owned States usw.) und eine `.rgb`- oder `.rgba`-Datei erzeugt;
- Oder wir verwenden direkt den Unterbefehl `issue` mit einer YAML- (oder TOML-)Datei, die die Eigenschaften des Tokens beschreibt.

Im Ordner `examples` findest du Beispiele in Rust, die veranschaulichen, wie du einen `ContractBuilder` erstellst, den `Global State` (Asset-Name, Ticker, Ausgabemenge, Datum usw.) ausfüllst, den Owned State definierst (welchem UTXO er zugewiesen ist) und dann all dies zu einem *contract consignment* zusammenstellst, das du exportieren, validieren und in einen Stash importieren kannst.

Die andere Möglichkeit besteht darin, eine YAML-Datei manuell zu bearbeiten, um den `ticker`, den `namen`, den `supply` usw. anzupassen. Nehmen wir an, die Datei heißt `RGB20-demo.yaml`. Du kannst angeben:


- `spec`: Ticker, Name, Genauigkeit;
- `terms`: ein Feld für rechtliche Hinweise;
- `issuedSupply`: die Menge der ausgegebenen Token;
- `assignments`: gibt das Single-use Seal (*Siegeldefinition*) und die freigeschaltete Menge an.

Hier ist ein Beispiel für eine YAML-Datei:

```yaml
interface: RGB20Fixed

globals:
  spec:
    ticker: Plan ₿ Academy
    name: Plan ₿ Academy
    details: "Pay attention: the asset has no value"
    precision: 2
  terms:
    text: >
      SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
    media: ~
  issuedSupply: 100000000

assignments:
  assetOwner:
    seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
    amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-Bitcoin](assets/en/085.webp)

Führe dann einfach den folgenden Befehl aus:

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-Bitcoin](assets/en/086.webp)

In meinem Fall lautet der eindeutige Schema-Bezeichner (der in einfache Anführungszeichen gesetzt werden muss) `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` und ich habe keinen Emittenten angegeben. Mein Befehl lautet also:

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Wenn du die Schema-ID nicht kennst, führe diesen Befehl aus:

```bash
rgb schemata
```

Das CLI meldet zurück, dass ein neuer Vertrag ausgestellt und dem Stash hinzugefügt wurde. Wenn wir den folgenden Befehl eingeben, sehen wir, dass es jetzt einen zusätzlichen Vertrag gibt, der dem soeben erteilten Vertrag entspricht:

```bash
rgb contracts
```

![RGB-Bitcoin](assets/en/087.webp)

Dann zeigt der nächste Befehl die Global States (Name, Ticker, Ausgabemenge...) und die Liste der Owned States, d.h. der Zuweisungen (z.B. 1 Million `Plan ₿ Academy` Token, definiert in UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`) an.

```bash
rgb state '<ContractId>'
```

![RGB-Bitcoin](assets/en/088.webp)

### Export, Import und Validierung

Um diesen Vertrag mit anderen Nutzern zu teilen, kann er aus dem Stash in eine Datei exportiert werden:

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-Bitcoin](assets/en/089.webp)

Die Datei `myContractPBN.rgb` kann an einen anderen Benutzer weitergegeben werden, der sie mit dem folgenden Befehl zu seinem Stash hinzufügen kann:

```bash
rgb import myContractPBN.rgb
```

Wenn es sich beim Import um ein einfaches *contract consignment* handelt, erhalten wir die Meldung "`Importing consignment rgb`". Handelt es sich um eine größere *state transition consignment*, muss der Befehl anders lauten (`rgb accept`).

Um die Gültigkeit sicherzustellen, kannst du auch die lokale Validierungsfunktion verwenden. Du kannst zum Beispiel diese Funktion aufrufen:

```bash
rgb validate myContract.rgb
```

#### Den Stash verwenden, überprüfen und anzeigen

Zur Erinnerung: Der Stash ist ein lokaler Bestand an Schemata, Schnittstellen, Implementierungen und Verträgen (Genesis + Transitionen). Jedes Mal, wenn du "import" ausführst, fügst du dem Stash ein Element hinzu. Dieser Bestand kann im Detail mit dem Befehl:

```bash
rgb dump
```

angezeigt werden.

![RGB-Bitcoin](assets/en/090.webp)

Dadurch wird ein Ordner mit Details über den gesamten Stash erstellt.

### Überweisungen und PSBT

Um eine Überweisung durchzuführen, musst du eine lokale Bitcoin-Wallet bedienen, um die `Tapret`- oder `Opret`-Commitments zu verwalten.

#### Eine Rechnung erstellen

In den meisten Fällen erfolgt die Interaktion zwischen den Teilnehmern eines Vertrags (z.B. Alice und Bob) über die Erstellung einer Rechnung (invoice). Wenn Alice möchte, dass Bob etwas ausführt (eine Token-Überweisung, eine Neuausgabe, eine Aktion in einer DAO usw.), erstellt Alice eine Rechnung, in der sie ihre Anweisungen an Bob detailliert beschreibt. Wir haben also:


- **Alice** (die Ausstellerin der Rechnung);
- **Bob** (der die Rechnung erhält und ausführt).

Im Gegensatz zu anderen Ökosystemen ist eine RGB-Invoice nicht auf Zahlungsvorgänge beschränkt. Sie kann jede mit dem Vertrag verbundene Anfrage enthalten: Widerruf eines Schlüssels, Abstimmung, Erstellung einer Gravur (*Gravur*) auf einem NFT usw. Der entsprechende Vorgang kann in der Vertragsschnittstelle beschrieben werden.

Der folgende Befehl erzeugt eine RGB-Invoice (Rechnung):

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Mit:


- `$CONTRACT`: Vertragskennung (*ContractId*) ;
- `$INTERFACE`: die zu verwendende Schnittstelle (z.B. `RGB20`);
- `$ACTION`: der Name der in der Schnittstelle angegebenen Operation (für eine einfache NFT-Übertragung könnte dies "Transfer" sein). Wenn die Schnittstelle bereits eine Standardaktion vorsieht, brauchen Sie diese hier nicht erneut einzugeben;
- `$STATE`: die zu übertragenden Zustandsdaten (z.B. eine Anzahl von Token, wenn ein fungibles Token übertragen wird);
- `$SEAL`: das Single-use Seal des Begünstigten (Alice), d.h. ein ausdrücklicher Verweis auf einen UTXO. Bob verwendet diese Information, um die Zeugen-Transaktion zu erstellen, und der entsprechende Output gehört dann Alice (in *verblendetem UTXO* oder unverschlüsselter Form).

Zum Beispiel mit den folgenden Befehlen

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

erzeugt das CLI eine Rechnung wie:

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Sie kann über einen beliebigen Kanal (Text, QR-Code usw.) an Bob übermittelt werden.

#### Eine Überweisung vornehmen

Um eine Überweisung gemäß dieser Rechnung vorzunehmen passiert folgendes:


- Bob (der die Token in seinem Stash hält) verfügt über eine Bitcoin-Wallet. Er muss eine Bitcoin-Transaktion vorbereiten (in Form eines PSBT, z. B. `tx.psbt`), die die UTXOs ausgibt, in denen sich die erforderlichen RGB-Token befinden, sowie einen zusätzlichen UTXO für das Wechselgeld (change);
- Bob führt den folgenden Befehl aus:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Dies erzeugt eine Datei `consignment.rgb`, die folgendes enthält:
 - Die Zustandsübergangshistorie, welche Alice beweist, dass die Token echt sind;
 - Den neuen Zustandsübergang, der Token auf Alices Single-use Seal überträgt;
 - Eine Zeugen-Transaktion (ohne Unterschriften/Signaturen).
- Bob sendet diese Datei `consignment.rgb` an Alice (per E-Mail, über einen Freigabeserver oder ein RGB-RPC-Protokoll, Storm usw.);
- Alice erhält die Datei `consignment.rgb` und nimmt sie in ihren eigenen Stash auf:

```bash
alice$ rgb accept consignment.rgb
```


- Das CLI prüft die Gültigkeit des Zustandsübergangs und fügt ihn zu Alices Stash hinzu. Ist sie ungültig, schlägt der Befehl mit detaillierten Fehlermeldungen fehl. Andernfalls ist er erfolgreich und meldet, dass die Beispieltransaktion noch nicht im Bitcoin-Netzwerk veröffentlicht wurde (Bob wartet auf Alices grünes Licht);
- Zur Bestätigung liefert der Befehl "accept" eine Unterschrift (*payslip*), die Alice an Bob senden kann, um ihm zu zeigen, dass sie das *consignment* bestätigt hat;
- Bob kann dann seine Bitcoin-Transaktion signieren und veröffentlichen (`--publish`):

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Sobald diese Transaktion auf der Blockchain bestätigt wird, gilt das Eigentum an dem Vermögenswert als auf Alice übertragen. Die Wallet von Alice, die das Mining der Transaktion überwacht, sieht den neuen Owned State in ihrem Stash erscheinen.

Im nächsten Kapitel werden wir einen genaueren Blick auf die Integration von RGB in das Lightning Network werfen.

## RGB im Lightning-Netzwerk

<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>

:::video id=be25a165-6e23-488c-91d8-3dcfccc6eca1:::

In diesem Kapitel möchte ich untersuchen, wie RGB innerhalb des Lightning-Netzwerks genutzt werden kann, um RGB-Assets (Token, NFTs, etc.) über Off-Chain-Zahlungskanäle zu integrieren und zu bewegen.

Die Grundidee ist, dass der RGB-Zustandsübergang (*State Transition*) in eine Bitcoin-Transaktion übertragen werden kann, die wiederum außerhalb der Kette bleiben kann, bis der Lightning-Kanal geschlossen wird. Jedes Mal, wenn der Kanal aktualisiert wird, kann also ein neuer RGB-Zustandsübergang in die neue Transaktion mit einem Commitment aufgenommen werden, die dann den alten Übergang ungültig macht. Auf diese Weise können Lightning-Kanäle für die Übertragung von RGB-Vermögenswerten verwendet und auf dieselbe Weise wie herkömmliche Lightning-Zahlungen geleitet werden.

### Einrichtung und Finanzierung von Kanälen

Um einen Lightning-Kanal zu erstellen, der RGB-Assets enthält, benötigen wir zwei Elemente:


- Bitcoin-Finanzierung, um das 2/2-MultiSig des Kanals zu erstellen (der grundlegende UTXO für den Kanal);
- RGB-Finanzierung, die Vermögenswerte an dieselbe MultiSig sendet.

In Bitcoin-Begriffen muss die Finanzierungstransaktion existieren, um den Referenz-UTXO zu definieren, auch wenn sie nur eine kleine Menge an Sats enthält (es geht nur darum, dass jeder Output in zukünftigen Transaktionen mit Commitments trotzdem über der [Staub](https://planb.academy/resources/glossary/dust)grenze bleibt). Zum Beispiel könnte Alice beschließen, 10k Sats und 500 USDT (als RGB-Asset ausgegeben) bereitzustellen. In die Finanzierungstransaktion fügen wir ein Commitment (`Opret` oder `Tapret`) ein, das den RGB-Zustandsübergang verankert.

![RGB-Bitcoin](assets/en/091.webp)

Sobald die Finanzierungstransaktion vorbereitet (aber noch nicht gesendet) wurde, werden Commitment-Transaktionen erstellt, so dass jede Partei den Kanal jederzeit einseitig schließen kann. Diese Transaktionen ähneln den klassischen Commitment-Transaktionen von Lightning, mit dem Unterschied, dass wir einen zusätzlichen Output hinzufügen, der den RGB-Anchor (OP_RETURN oder Taproot) enthält, der mit dem neuen Zustandsübergang verbunden ist.

Der RGB-Zustandsübergang verschiebt dann die Vermögenswerte von der 2/2-MultiSig (Finanzierung) zu den Outputs der Commitment-Transaktion. Der Vorteil dieses Prozesses ist, dass die Sicherheit des RGB-Zustands genau der Strafmechanik von Lightning entspricht: Wenn Bob einen alten Kanalzustand sendet, kann Alice ihn bestrafen und den Output ausgeben, um sowohl die Sats als auch die RGB-Token zurückzuerhalten. Der Anreiz ist also noch größer als bei einem Lightning-Kanal ohne RGB-Vermögenswerte, da ein Angreifer nicht nur die Sats, sondern auch die RGB-Vermögenswerte des Kanals verlieren kann.

Eine von Alice unterzeichnete und an Bob gesendete Commitment-Transaktion würde also wie folgt aussehen:

![RGB-Bitcoin](assets/en/092.webp)

Die dazugehörige Commitment-Transaktion, die von Bob unterzeichnet und an Alice gesendet wird, sieht folgendermaßen aus:

![RGB-Bitcoin](assets/en/093.webp)

### Kanal-Update

Wenn eine Zahlung zwischen zwei Kanalteilnehmern erfolgt (oder sie die Asset-Zuordnung ändern wollen), erstellen sie ein neues Paar von Commitment-Transaktionen. Der Betrag in Sats an jedem Ausgang kann je nach Implementierung unverändert bleiben oder nicht, da seine Hauptaufgabe darin besteht, die Erstellung gültiger UTXOs zu ermöglichen. Andererseits muss der OP_RETURN (oder Taproot) Output geändert werden, um den neuen RGB-Anchor zu enthalten, der die neue Verteilung der Vermögenswerte im Kanal darstellt.

Wenn Alice beispielsweise 30 USDT an Bob im Kanal überweist, wird der neue Zustandsübergang einen Saldo von 400 USDT für Alice und 100 USDT für Bob widerspiegeln. Die Commit-Transaktion wird zum OP_RETURN/Taproot-Anchor hinzugefügt (oder von diesem geändert), um diesen Übergang zu berücksichtigen. Beachte, dass aus der Sicht von RGB der Input für den Übergang die anfängliche MultiSig bleibt (in der die Vermögenswerte auf der Kette tatsächlich zugewiesen werden, bis der Kanal geschlossen wird). Nur die RGB-Outputs (Zuweisungen) ändern sich, je nach der beschlossenen Umverteilung.

Die von Alice unterzeichnete Commitment-Transaktion, die von Bob verteilt werden kann:

![RGB-Bitcoin](assets/en/094.webp)

Die von Bob unterzeichnete Commitment-Transaktion, die von Alice verteilt werden kann:

![RGB-Bitcoin](assets/en/095.webp)

### HTLC-Verwaltung

In Wirklichkeit ermöglicht das Lightning Network die Weiterleitung von Zahlungen über mehrere Kanäle unter Verwendung von [HTLCs](https://planb.academy/resources/glossary/htlc) (*Hashed Time-Locked Contracts*). Mit RGB ist es dasselbe: Für jede Zahlung, die den Kanal durchläuft, wird ein HTLC-Output zur Commitment-Transaktion hinzugefügt und eine RGB-Zuweisung mit diesem HTLC verknüpft. Wer also den HTLC-Output ausgibt (dank des Geheimnisses oder nach Ablauf der Zeitsperre), erhält sowohl die Sats als auch die zugehörigen RGB-Guthaben zurück. Andererseits muss man natürlich über genügend Liquidität in Form von Sats und RGB-Vermögenswerten verfügen.

![RGB-Bitcoin](assets/en/096.webp)

Der Betrieb von RGB auf Lightning muss daher parallel zu dem des Lightning-Netzwerks selbst betrachtet werden. Wenn du tiefer in dieses Thema einsteigen möchtest, empfehle ich dir, einen Blick auf diesen anderen umfassenden Schulungskurs zu werfen:

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### RGB Code-Übersicht

Bevor ich zum nächsten Abschnitt übergehe, möchte ich dir noch einen Überblick über den in RGB verwendeten Code geben. Das Protokoll basiert auf einer Reihe von Rust-Bibliotheken und Open-Source-Spezifikationen. Hier ist ein Überblick über die wichtigsten Repositories und Crates:

![RGB-Bitcoin](assets/en/097.webp)

#### client-side Validierung


- **Repository**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- **Crates**: [client_side_validation](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)

Verwaltung der Off-Chain-Validierung und der Logik für Single-use Seals.

#### Deterministische Bitcoin-Zusagen (DBC)


- **Repository**: [bp-core](https://github.com/BP-WG/bp-core)
- **Crate**: [bp-dbc](https://crates.io/crates/bp-dbc)

Verwaltung der deterministischen Anchor in Bitcoin-Transaktionen (Tapret, OP_RETURN, etc.).

#### Multi Protocol Commitment (MPC)


- **Repository**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- **Crate**: [commit_verify](https://crates.io/crates/commit_verify)

MPCs und Integration mit verschiedenen Protokollen.

#### Stricy Types und strenge Kodierung


- **Spezifikation**: [Website strict-types.org](https://www.strict-types.org/)
- **Repositories**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- **Crates**: [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)

Das Strict Typing System und die deterministische Serialisierung, die für die client-side Validierung verwendet werden.

#### RGB Core


- **Repository**: [rgb-core](https://github.com/RGB-WG/rgb-core)
- **Crate**: [rgb-core](https://crates.io/crates/rgb-core)

Der Kern des Protokolls, der die Hauptlogik der RGB-Validierung umfasst.

#### RGB Standardbibliothek & Wallet


- **Repository**: [rgb-std](https://github.com/RGB-WG/rgb-std)
- **Crate**: [rgb-std](https://crates.io/crates/rgb-std)

Standard Implementierungen, Stash- und Walletverwaltung.

#### RGB CLI


- **Repository**: [rgb](https://github.com/RGB-WG/rgb)
- **Crates**: [rgb-cli](https://crates.io/crates/rgb-cli), [rgb-wallet](https://crates.io/crates/rgb-wallet)

Die `rgb` CLI und crate Wallet, für die Bearbeitung von Verträgen per Kommandozeile.

#### RGB Schema


- **Repository**: [rgb-schemata](https://github.com/RGB-WG/rgb-schemata/)

Enthält Beispiele für Schemata (NIA, UDA, usw.) und ihre Implementierungen.

#### ALuVM


- **Info**: [aluvm.org](https://www.aluvm.org/)
- **Repositories**: [aluvm-spec](https://github.com/AluVM/aluvm-spec), [alure](https://github.com/AluVM/alure)
- **Crates**: [aluvm](https://crates.io/crates/aluvm), [aluasm](https://crates.io/crates/aluasm)

Registry-basierte virtuelle Maschine zur Ausführung von Validierungsskripten.

#### Bitcoin-Protokoll - BP


- **Repositories**: [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-wallet](https://github.com/BP-WG/bp-wallet)

Add-ons zur Unterstützung des Bitcoin-Protokolls (Transaktionen,  usw.).

#### Ubiquitäres deterministisches Rechnen - UBIDECO


- **Repository**: [UBIDECO](https://github.com/UBIDECO)

Ökosystem in Verbindung mit deterministischen Open-Source-Entwicklungen.

# Building on RGB

<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>

## DIBA und das Bitmask-Projekt

<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>

:::video id=2ec9a181-a8b0-4da2-b7b5-9dfaaaeb10ba:::

Dieser letzte Abschnitt des Kurses basiert auf den Präsentationen verschiedener Redner des RGB-Bootcamps. Er enthält Erfahrungsberichte und Überlegungen zu RGB und seinem Ökosystem sowie Präsentationen von Tools und Projekten, die auf dem Protokoll basieren. Dieses erste Kapitel wird von Hunter Beast moderiert, die nächsten beiden von Frederico Tenga.

### Von JavaScript zu Rust und hinein in das Bitcoin-Ökosystem

Zunächst arbeitete Hunter Beast hauptsächlich in JavaScript. Dann entdeckte er **Rust**, dessen Syntax anfangs unattraktiv und frustrierend erschien. Er lernte jedoch die Leistungsfähigkeit der Sprache, die Kontrolle über den Speicher (*Heap* und *Stack*) sowie die damit verbundene Sicherheit und Leistung zu schätzen. Er betont, dass Rust ein ausgezeichnetes Übungsfeld für ein tiefgreifendes Verständnis der Funktionsweise eines Computers ist.

Hunter Beast berichtet über seinen Hintergrund in verschiedenen Projekten im *Altcoin*-Ökosystem, wie Ethereum (mit Solidity, TypeScript usw.) und später Filecoin. Er erklärt, dass er anfangs von einigen der Protokolle beeindruckt war, aber schließlich von den meisten von ihnen desillusioniert war, nicht zuletzt wegen ihrer Tokenomik. Er prangert die zweifelhaften finanziellen Anreize, die inflationäre Schaffung von Token, die die Investoren verwässern, und den potenziell ausbeuterischen Aspekt dieser Projekte an. So hat er schließlich eine **Bitcoin maximalistische** Haltung eingenommen, nicht zuletzt, weil ihm einige Leute die Augen für die solideren wirtschaftlichen Mechanismen von Bitcoin und die Robustheit dieses Systems geöffnet haben.

### Die Attraktivität von RGB und der Aufbau in Ebenen

Was ihn endgültig von der Relevanz von Bitcoin überzeugt hat, war seiner Meinung nach die Entdeckung von RGB und des Konzepts der Schichten. Er glaubt, dass bestehende Funktionalitäten anderer Blockchains auf höheren Schichten über Bitcoin reproduziert werden könnten, ohne das grundlegende Protokoll zu verändern.

Im Februar 2022 trat er **DIBA** bei, um speziell an RGB und insbesondere an der **Bitmask**-Wallet zu arbeiten. Zu dieser Zeit war Bitmask noch in der Version 0.01 und verwendete RGB in der Version 0.4, nur für die Verwaltung einzelner Token. Er merkt an, dass dies weniger selbstverwahrungssorientiert als heute war, da die Logik teilweise serverbasiert war. Seitdem hat sich die Architektur in Richtung dieses Modells (Selbstverwahrung) entwickelt, was von Bitcoinern sehr geschätzt wird.

### Die Grundlagen des RGB-Protokolls

Das **RGB**-Protokoll ist die jüngste und am weitesten fortgeschrittene Ausprägung des Konzepts der _colored coins_, das bereits 2012-2013 erforscht wurde. Zu dieser Zeit versuchten mehrere Teams, UTXOs verschiedene Bitcoin-Werte zuzuordnen, was zu mehreren verstreuten Implementierungen führte. Dieser Mangel an Standardisierung und die geringe Nachfrage zu dieser Zeit verhinderten, dass diese Lösungen dauerhaft Fuß fassen konnten.

Heute zeichnet sich RGB durch konzeptionelle Robustheit und einheitliche Spezifikationen über die LNP/BP-Association aus. Das Prinzip basiert auf einer client-side Validierung. Die Bitcoin-Blockchain speichert nur kryptografische Verpflichtungen (_commitments_, über Taproot oder OP_RETURN), während der Großteil der Daten (Vertragsdefinitionen, Überweisungshistorien usw.) von den betroffenen Nutzern gespeichert wird. Auf diese Weise wird die Speicherlast verteilt und die Vertraulichkeit des Austauschs verstärkt, ohne die Blockchain zu belasten. Dieser Ansatz ermöglicht die Schaffung fungibler Vermögenswerte (**RGB20**-Standard) oder einzigartiger Vermögenswerte (**RGB21**-Standard) innerhalb eines modularen und skalierbaren Rahmens.

### Die Token-Funktion (RGB20) und eindeutige Vermögenswerte (RGB21)

Mit **RGB20** definieren wir einen fungiblen Token auf Bitcoin. Der Emittent wählt ein _Angebot_, eine _Präzision_, und erstellt einen _Vertrag_, in dem er dann Überweisungen tätigen kann. Jeder Transfer wird auf einen Bitcoin UTXO referenziert, der als *Single-use Seal* fungiert. Diese Logik stellt sicher, dass der Nutzer nicht in der Lage ist, denselben Vermögenswert zweimal auszugeben, da nur die Person, die in der Lage ist, den UTXO auszugeben, auch den Schlüssel besitzt, um den Zustand des client-side Vertrags zu aktualisieren.

**RGB21** zielt auf einzigartige Vermögenswerte (oder "NFTs"). Der Vermögenswert hat einen Wert von 1 und kann mit Metadaten (Bilddatei, Audio usw.) verknüpft werden, die über ein bestimmtes Feld beschrieben werden. Im Gegensatz zu NFTs auf öffentlichen Blockchains können Daten und ihre MIME-Kennungen privat bleiben und nach dem Ermessen des Eigentümers peer-to-peer verteilt werden.

### Die Bitmask-Lösung: eine Wallet für RGB

Um die Möglichkeiten von RGB in der Praxis zu nutzen, hat das **DIBA**-Projekt eine Wallet namens [Bitmask](https://bitmask.app/) entwickelt. Die Idee besteht darin, ein non-custodial, auf Taproot basierendes Tool bereitzustellen, das als Webanwendung oder Browsererweiterung zugänglich ist. Bitmask verwaltet sowohl RGB20- als auch RGB21-Assets und integriert verschiedene Sicherheitsmechanismen:


- Der Kerncode wird in Rust geschrieben und dann in WebAssembly kompiliert, um in einer JavaScript-Umgebung (React) zu laufen;
- Die Schlüssel werden lokal generiert und dann verschlüsselt lokal gespeichert;
- Die Zustandsdaten (Stash) werden im Speicher gehalten, serialisiert und mit Hilfe der **Carbonado**-Bibliothek verschlüsselt, die Kompression, Fehlerkorrektur, Verschlüsselung und Stream-Verifizierung mit Blake3 durchführt.

Dank dieser Architektur finden alle Vermögenstransaktionen auf der client-side statt. Von außen betrachtet ist die Bitcoin-Transaktion nichts anderes als eine klassische Taproot-Transaktion, bei der niemand vermuten würde, dass sie auch eine Übertragung von fungiblen Token oder NFTs beinhaltet. Das Fehlen einer On-Chain-Überlastung (keine öffentlich gespeicherten Metadaten) garantiert ein gewisses Maß an Diskretion und macht es einfacher, möglichen Zensurversuchen zu widerstehen.

### Sicherheit und verteilte Architektur

Da das RGB-Protokoll verlangt, dass jeder Teilnehmer seinen Transaktionsverlauf aufbewahrt (um die Gültigkeit der empfangenen Überweisungen zu beweisen), stellt sich die Frage der Speicherung. Bitmask schlägt vor, diesen Stash lokal zu serialisieren und dann an mehrere Server oder Clouds (optional) zu senden. Die Daten bleiben vom Nutzer über **Carbonado** verschlüsselt, so dass ein Server sie nicht lesen kann. Im Falle einer teilweisen Beschädigung kann die Fehlerkorrekturschicht den Inhalt wiederherstellen.

Durch die Verwendung von CRDT (_Conflict-free replicated data type_) können verschiedene Versionen des Stash zusammengeführt werden, falls sie voneinander abweichen. Jedem steht es frei, diese Daten zu hosten, wo immer er möchte, da kein einzelner vollständiger Knoten alle mit dem Vermögenswert verbundenen Informationen enthält. Dies entspricht genau der Philosophie der *client-side Validation*, bei der jeder Eigentümer dafür verantwortlich ist, Beweise für die Gültigkeit seines RGB-Assets zu speichern.

### Auf dem Weg zu einem breiteren Ökosystem: Marktplatz, Interoperabilität und neue Funktionen

Das Unternehmen, das hinter Bitmask steht, beschränkt sich nicht auf die einfache Entwicklung einer Wallet. DIBA beabsichtigt die Entwicklung von:


- Einem **Marktplatz** für den Tausch von Token, insbesondere in **RGB21**-Form;
- Kompatibilität mit anderen Wallets (z.B. *Iris Wallet*);
- **Transfer batching**-Möglichkeiten, d.h. die Möglichkeit, mehrere aufeinander folgende RGB-Überweisungen in eine einzige Transaktion einzubeziehen.

Gleichzeitig arbeiten wir an **WebBTC** oder **WebLN** (Standards, die es Webseiten ermöglichen, die Wallet aufzufordern, Bitcoin- oder Lightning-Transaktionen zu signieren), sowie an der Möglichkeit, Ordinals-Einträge zu "teleburnen" (falls wir Ordinals in ein diskreteres und flexibleres RGB-Format zurückführen wollen).

### Schlussfolgerung

Der gesamte Prozess zeigt, wie das RGB-Ökosystem durch robuste technische Lösungen implementiert und für Endnutzer zugänglich gemacht werden kann. Der Übergang von einer Altcoin-Perspektive zu einer eher Bitcoin-zentrierten Vision, gekoppelt mit der Entdeckung der *client-side Validation*, veranschaulicht einen ziemlich logischen Weg: Wir verstehen, dass es möglich ist, verschiedene Funktionalitäten (fungible Token, NFT, Smart Contracts...) zu implementieren, ohne die Blockchain zu forken, indem man einfach die Vorteile kryptographischer Commitments auf Taproot-Transaktionen oder OP_RETURNs nutzt.

Die **Bitmask**-Wallet ist Teil dieses Ansatzes: Auf der Blockchain-Seite sieht man nur eine gewöhnliche Bitcoin-Transaktion; auf der Benutzerseite manipuliert man eine Webschnittstelle, auf der man alle Arten von Off-Chain-Assets erstellen, austauschen und speichern kann. Dieses Modell trennt die monetäre Infrastruktur (Bitcoin) eindeutig von der Ausgabe- und Übertragungslogik (RGB) und gewährleistet gleichzeitig ein hohes Maß an Vertraulichkeit und eine bessere Skalierbarkeit.

## Die Arbeit von Bitfinex an RGB

<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>

:::video id=04555813-516f-4eea-9767-7082c2ea6f01:::

In diesem Kapitel, das auf einer Präsentation von Frederico Tenga basiert, sehen wir uns eine Reihe von Tools und Projekten an, die vom Bitfinex-Team für RGB entwickelt wurden, um die Entstehung eines reichhaltigen und vielfältigen Ökosystems rund um dieses Protokoll zu fördern. Das ursprüngliche Ziel des Teams ist es nicht, ein spezifisches kommerzielles Produkt zu veröffentlichen, sondern vielmehr Software-Bausteine bereitzustellen, einen Beitrag zum RGB-Protokoll selbst zu leisten und konkrete Implementierungsreferenzen wie eine mobile Wallet (*Iris Wallet*) oder einen RGB-kompatiblen Lightning-Knoten vorzuschlagen.

### Hintergrund und Ziele

Seit etwa 2022 konzentriert sich das Bitfinex RGB-Team auf die Entwicklung des Technologie-Stacks, der eine effiziente Nutzung und Prüfung von RGB ermöglicht. Es wurden bereits mehrere Beiträge geleistet:


- Mitwirkung an Quellcode und Protokollspezifikationen, einschließlich des Verfassens von Verbesserungsvorschlägen, der Behebung von Fehlern usw;
- Werkzeuge für Entwickler zur Vereinfachung der Integration von RGB in ihre Anwendungen;
- Entwicklung einer mobilen Wallet mit dem Namen [Iris](https://iriswallet.com/) zur Erprobung und Veranschaulichung bewährter Verfahren für die Verwendung von RGB;
- Erstellung eines angepassten Lightning-Knotens, der Kanäle mit RGB-Assets verwalten kann;
- Unterstützung anderer Teams, die Lösungen auf RGB aufbauen, um Vielfalt und ein starkes Ökosystem zu fördern.

Dieser Ansatz zielt darauf ab, die gesamte Bedarfskette abzudecken: von der Low-Level-Bibliothek (*[RGBlib](https://github.com/RGB-Tools/rgb-lib)*), die die Implementierung einer Wallet ermöglicht, bis hin zum Produktionsaspekt (ein Lightning-Knoten, eine Wallet für Android usw.).

### Die RGBlib-Bibliothek: Vereinfachung der Entwicklung von RGB-Anwendungen

Ein wichtiger Punkt bei der Demokratisierung der Erstellung von RGB-Wallets und -Anwendungen ist es, eine Abstraktion zur Verfügung zu stellen, die einfach genug ist, damit Entwickler nicht alles über die interne Logik des Protokolls lernen müssen. Genau das ist das Ziel von **RGBlib**, geschrieben in Rust.

RGBlib fungiert als Brücke zwischen den hochflexiblen (aber manchmal komplexen) Anforderungen von RGB, die wir in den vorangegangenen Kapiteln untersuchen konnten, und den konkreten Bedürfnissen eines Anwendungsentwicklers. Mit anderen Worten: Eine Wallet (oder ein Dienst), der Token-Transfers, die Ausgabe von Vermögenswerten, die Verifizierung usw. verwalten möchte, kann sich auf RGBlib verlassen, ohne jedes kryptografische Detail oder jeden anpassbaren RGB-Parameter zu kennen.

Diese Lösung bietet:


- Schlüsselfertige Funktionen für die Ausgabe (_issuance_) von Vermögenswerten (fungibel oder nicht);
- Die Fähigkeit, Vermögenswerte zu übertragen (senden/empfangen), indem einfache Objekte (Adressen, Beträge, UTXOs usw.) manipuliert werden;
- Einen Mechanismus zum Speichern und Laden der für die client-side Validierung erforderlichen Statusinformationen (*Zuordnungen*).

RGBlib stützt sich daher auf komplexe, RGB-spezifische Konzepte (client-side Validierung, Tapret/Opret-Anchor), kapselt diese jedoch, so dass die endgültige Anwendung nicht alles neu programmieren oder riskante Entscheidungen treffen muss. Darüber hinaus ist RGBlib bereits in mehrere Sprachen (Kotlin und Python) eingebunden, was die Tür zu Anwendungen jenseits des einfachen Rust-Universums öffnet.

### Iris Wallet: ein Beispiel für eine RGB-Wallet auf Android

Um die Effektivität von RGBlib zu beweisen, hat das Bitfinex-Team **Iris Wallet** entwickelt, derzeit ausschließlich für Android. Es handelt sich dabei um eine mobile Wallet, die ein ähnliches Benutzererlebnis wie eine gewöhnliche Bitcoin-Wallet bietet: Man kann ein Asset ausgeben, es senden, empfangen und seine Historie einsehen, wobei man beim Prinzip der Eigenverwahrung bleibt.

Iris hat eine Reihe interessanter Merkmale:

**Verwendung eines Electrum-Servers:**

Wie jede Wallet muss auch Iris über Transaktionsbestätigungen auf der Blockchain Bescheid wissen. Anstatt einen kompletten Knoten einzubetten, verwendet Iris standardmäßig einen Electrum-Server, der vom Bitfinex-Team gewartet wird. Benutzer können jedoch ihren eigenen Server oder einen anderen Drittanbieterdienst konfigurieren. Auf diese Weise können Bitcoin-Transaktionen auf modulare Weise validiert und Informationen abgerufen werden (Indexierung).

**Der RGB-Proxy-Server:**

Anders als Bitcoin erfordert RGB den Austausch von Off-Chain-Metadaten (*Consignments*) zwischen Sender und Empfänger. Um diesen Prozess zu vereinfachen, bietet Iris eine Lösung an, bei der die Kommunikation über einen Proxy-Server stattfindet. Die empfangende Wallet generiert eine *Rechnung*, die angibt, wohin der Absender die *client-side* Daten senden soll. Standardmäßig verweist die URL auf einen Proxy, der vom Bitfinex-Team gehostet wird, aber du kannst diesen Proxy ändern (oder deinen eigenen hosten). Die Idee ist, zu einer gewohnten Benutzererfahrung zurückzukehren, bei der der Empfänger einen QR-Code anzeigt und der Absender diesen Code für die Transaktion scannt, ohne komplexe zusätzliche Interaktionen.

**Kontinuierliche Sicherung:**

In einem reinen Bitcoin-Kontext reicht es im Allgemeinen aus, den Seed zu sichern (obwohl wir heutzutage empfehlen, stattdessen den Seed und die Deskriptoren zu sichern). Bei RGB reicht das nicht aus: Du musst auch die lokale Historie (die *Consignments*) aufbewahren, die beweist, dass du wirklich ein RGB-Asset besitzt. Jedes Mal, wenn du eine Quittung erhältst, speichert das Gerät neue Daten, die für spätere Ausgaben unerlässlich sind. Iris verwaltet automatisch ein verschlüsseltes Backup im Google Drive des Nutzers. Dies erfordert kein besonderes Vertrauen in Google, da das Backup verschlüsselt ist, und für die Zukunft sind robustere Optionen (wie ein persönlicher Server) geplant, um jegliches Risiko einer Zensur oder Löschung durch einen Drittanbieter zu vermeiden.

**Weitere Merkmale:**


- Es ist leicht möglich ein Faucet (Wasserhahn) zu erstellen, um Token für Experimente oder Werbeaktionen schnell zu testen oder zu verteilen;
- Ein (derzeit zentralisiertes) Zertifizierungssystem zur Unterscheidung zwischen einem legitimen Token und einem gefälschten Token, das einen berühmten Ticker kopiert. In Zukunft könnte diese Zertifizierung dezentraler werden (über DNS oder andere Mechanismen).

Alles in allem bietet Iris ein Benutzererlebnis, das dem einer klassischen Bitcoin-Wallet nahe kommt, wobei die zusätzliche Komplexität (Stash-Management, *Consignment*-Historie usw.) dank der RGBlib und der Verwendung eines Proxy-Servers verborgen bleibt.

### Proxyserver und Nutzererfahrung

Der oben vorgestellte Proxyserver verdient es, näher erläutert zu werden, da er der Schlüssel zu einem reibungslosen Benutzererlebnis ist. Anstatt dass der Absender die *Sendungen* manuell an den Empfänger übermitteln muss, erfolgt die RGB-Transaktion im Hintergrund über eine Reihe von Abfragen:


- Der Empfänger erstellt eine *Invoice* (die u.a. die Adresse des Bevollmächtigten enthält);
- Der Absender sendet (über eine HTTP-Anfrage) ein Übergangsprojekt (das *Consignment*) an den Proxy;
- Der Empfänger ruft dieses Projekt ab und führt die *client-side* Validierung lokal durch;
- Der Empfänger veröffentlicht dann über den Proxy die Annahme (oder gegebenenfalls Ablehnung) des Zustandsübergangs;
- Der Absender kann den Validierungsstatus einsehen und, wenn er ihn akzeptiert, die Bitcoin-Transaktion zum Abschluss der Überweisung veröffentlichen.

Auf diese Weise verhält sich die Wallet fast wie eine normale Wallet. Der Nutzer bekommt von allen Zwischenschritten nichts mit. Zugegeben, der aktuelle Proxy ist weder verschlüsselt noch authentifiziert (was Bedenken hinsichtlich Vertraulichkeit und Integrität aufkommen lässt), aber diese Verbesserungen sind in späteren Versionen möglich. Das Proxy-Konzept ist nach wie vor äußerst nützlich, um das Erlebnis "Ich sende einen QR-Code, du scannst ihn, um zu bezahlen" nachzubilden.

### RGB-Integration in das Lightning-Netzwerk

Ein weiterer Schwerpunkt der Arbeit des Bitfinex-Teams ist es, das Lightning-Netzwerk mit RGB-Assets kompatibel zu machen. Das Ziel ist es, Lightning-Kanäle in USDT (oder jedem anderen Token) zu ermöglichen und von den gleichen Vorteilen wie Bitcoin auf Lightning zu profitieren (nahezu sofortige Transaktionen, Routing usw.). Konkret geht es darum, einen modifizierten Lightning-Knoten zu bauen, der:


- einen Kanal öffnen kann, indem nicht nur Satoshis, sondern auch ein oder mehrere RGB-Assets in der Finanzierungs-MultiSig-UTXO platziert sind;
- Lightning-Commitment-Transaktionen (Bitcoin-Seite) erstellen kann, die von entsprechenden RGB-Zustandsübergängen begleitet werden. Jedes Mal, wenn der Kanal aktualisiert wird, definiert ein RGB-Übergang die Vermögensverteilung in den Lightning-Outputs neu;
- ein einseitiges Schließen ermöglicht, bei der der Vermögenswert in einem exklusiven UTXO unter Einhaltung der Regeln des Lightning-Netzwerks (HTLC, Timelock, Strafe usw.) abgerufen wird.

Diese Lösung mit dem Namen "**RGB Lightning Node**" verwendet LDK (*Lightning Dev Kit*) als Basis und fügt die Mechanismen hinzu, die erforderlich sind, um RGB-Token in die Kanäle zu injizieren. Lightning Commitments behalten die klassische Struktur (bestrafbare Outputs, Timelock...), und verankern zusätzlich einen RGB-Zustandsübergang (via `Opret` oder `Tapret`). Für den Nutzer eröffnet dies den Weg zu Lightning-Kanälen in Stablecoins oder in jedem anderen Vermögenswert, der über RGB ausgegeben wird.

### DEX-Potenzial und Auswirkungen auf Bitcoin

Sobald mehrere Vermögenswerte über Lightning verwaltet werden, ist es möglich, sich einen **atomaren Austausch** auf einem einzigen Lightning-Routing-Pfad vorzustellen, der dieselbe Logik von Geheimnissen und Timelocks verwendet. Beispiel: Nutzer A hält Bitcoin in einem Lightning-Kanal und Nutzer B hält USDT RGB in einem anderen Lightning-Kanal. Sie können einen Pfad erstellen, der ihre beiden Kanäle miteinander verbindet, und gleichzeitig BTC gegen USDT tauschen, ohne dass Vertrauen erforderlich ist. Dies ist nichts anderes als ein **atomarer Tausch**, der über mehrere Hops stattfindet, so dass die außenstehenden Teilnehmer kaum bemerken, dass sie einen Handel und nicht nur eine Weiterleitung vornehmen. Dieser Ansatz bietet:


- Sehr niedrige Latenzzeit, da alles auf Lightning und somit off-chain bleibt.
- Eine überlegene **Privatssphäre**: niemand weiß, dass es sich um einen Handel und nicht um eine normale Weiterleitung handelt;
- Vermeidung von Frontrunning, ein immer wiederkehrendes Problem bei On-Chain DEXes;
- Geringere Kosten (man zahlt keinen Blockspace, sondern nur Lightning-Routing-Gebühren).

Wir können uns dann ein Ökosystem vorstellen, in dem Lightning-Knoten Tauschpreise anbieten (indem sie Liquidität bereitstellen). Jeder Knoten kann, wenn er möchte, die Rolle eines _Market Makers_ spielen, der verschiedene Vermögenswerte auf Lightning kauft und verkauft. Diese Aussicht auf eines DEX in Schicht 2 unterstreicht die Idee, dass es nicht notwendig ist, Blockchains von Drittanbietern zu nutzen oder Bitcoin zu forken, um dezentralisierte Börsen für Vermögenswerte zu erhalten.

Die Auswirkungen auf Bitcoin könnten positiv sein: Die Infrastruktur von Lightning (Knoten, Kanäle und Dienste) würde dank des von diesen *stablecoins*, Derivaten und anderen Token generierten Volumen besser ausgelastet werden. Händler, die an USDT-Zahlungen auf Lightning interessiert sind, würden mechanisch BTC-Zahlungen auf Lightning entdecken (da sie vom gleichen Stack verwaltet werden). Die Wartung und Finanzierung der Infrastruktur des Lightning-Netzwerks könnte ebenfalls von der Vervielfachung dieser Nicht-BTC-Ströme profitieren, was indirekt den Bitcoin-Nutzern zugute käme.

### Schlussfolgerung und Ressourcen

Das Bitfinex-Team, das sich mit RGB beschäftigt, veranschaulicht durch seine Arbeit die Vielfalt dessen, was auf dem Protokoll aufgebaut werden kann. Auf der einen Seite gibt es RGBlib, eine Bibliothek, die das Design von Wallets und Anwendungen erleichtert. Auf der anderen Seite haben wir Iris Wallet, einen praktischen Demonstrator einer sauberen Endbenutzerschnittstelle auf Android. Schließlich zeigt die Integration von RGB mit Lightning, dass Stablecoin-Kanäle möglich sind, und öffnet den Weg zu einem möglichen dezentralen DEX auf Lightning.

Dieser Ansatz bleibt weitgehend experimentell und entwickelt sich weiter: Die RGBlib-Bibliothek wird nach und nach verfeinert, Iris Wallet wird regelmäßig verbessert, und der dedizierte Lightning-Knoten ist noch kein Mainstream-Lightning-Client.

Für diejenigen, die mehr erfahren oder einen Beitrag leisten möchten, stehen mehrere Ressourcen zur Verfügung, darunter:


- [GitHub RGB Tools Repositories](https://github.com/RGB-Tools);
- [Eine Informationsseite zu Iris Wallet](https://iriswallet.com/), um die Wallet auf Android zu testen.

Im nächsten Kapitel werden wir uns genauer ansehen, wie man einen RGB-Lightning-Knoten (Node) startet.

## RLN: RGB-Lightning-Knoten

<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>

:::video id=d1e9753e-6093-4a47-bcdc-da1aebaefffc:::

In diesem letzten Kapitel führt Frederico Tenga dich Schritt für Schritt durch die Einrichtung eines Lightning-RGB-Knotens (RLN) in einer [Regtest](https://planb.academy/resources/glossary/regtest)-Umgebung und zeigt dir, wie du darauf RGB-Token erstellen kannst. Indem du zwei separate Nodes aufsetzt, erfährst du auch, wie du einen Lightning-Kanal zwischen ihnen öffnen und RGB-Assets austauschen kannst.

Dieses Video dient als Tutorial, ähnlich dem, was wir in einem früheren Kapitel behandelt haben, aber dieses Mal speziell auf Lightning konzentriert!

Die Hauptquelle für dieses Video ist das Github-Repository [RGB Lightning Node](https://github.com/RGB-Tools/rgb-lightning-node), das es dir leicht macht, diese Konfiguration in Regtest zu starten.

### Einrichten eines RGB-kompatiblen Lightning-Knotens

Der Prozess greift alle in den vorangegangenen Kapiteln behandelten Konzepte auf und setzt sie in die Praxis um:


- Die Idee, dass ein in einem 2/2 MultiSig eines Lightning-Kanals gesicherter **UTXO**, nicht nur Bitcoins erhalten, sondern auch ein Single-use Seal von RGB-Assets (fungibel oder nicht) sein kann;
- Das Hinzufügung eines Outputs (`Tapret` oder `Opret`) bei jeder Lightning-Transaktion zur Verankerung des RGB-Zustandsübergangs;
- Die zugehörige Infrastruktur (bitcoind/indexer/proxy) zur Validierung von Bitcoin-Transaktionen und zum Austausch von *client-side* Daten.

### Einführung von rgb-lightning-node

Das Projekt **`rgb-lightning-node`** ist ein Rust-Daemon, der auf einem `rust-lightning` (LDK) Fork basiert und so modifiziert wurde, dass er das Vorhandensein von RGB-Assets in einem Kanal berücksichtigt. Wenn ein Kanal geöffnet wird, kann das Vorhandensein von Assets angegeben werden, und jedes Mal, wenn der Kanalstatus aktualisiert wird, wird ein RGB-Übergang erstellt, der die Verteilung des Assets in den Lightning-Ausgängen widerspiegelt. Dies ermöglicht:


- Das Öffnen von Lightning-Kanäle in USDT, zum Beispiel;
- Das Routen dieser Token durch das Netzwerk, vorausgesetzt, die Routing-Pfade sind ausreichend liquide;
- Das Nutzen der Bestrafungs- und Timelock-Logik von Lightning ohne weitere Anpassungen: der RGB-Übergang wird einfach in einem zusätzlichen Ausgang der Commitment-Transaktion verankert.

Der Code befindet sich noch im Alpha-Stadium: Wir empfehlen, ihn nur in **regtest** oder im **testnet** zu verwenden.

### Installation des Knotens

Um die Binärdatei `rgb-lightning-node` zu kompilieren und zu installieren, beginnen wir mit dem Klonen des Repositories und seiner Untermodule, danach starten wir den Kompiliervorgang:

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RGB-Bitcoin](assets/en/098.webp)


- Die Option `--recurse-submodules` klont auch die notwendigen Subdevices (einschließlich der modifizierten Version von `rust-lightning`);
- Die Option `--shallow-submodules` schränkt die Tiefe des Klons ein, um das Herunterladen zu beschleunigen, während der Zugang zu den wesentlichen commits erhalten bleibt.

Führe im Stammverzeichnis des Projekts den folgenden Befehl aus, um die Binärdatei zu kompilieren und zu installieren:

```bash
cargo install --locked --debug --path .
```

![RGB-Bitcoin](assets/en/099.webp)


- `--locked` stellt sicher, dass die Version der Abhängigkeiten (dependencies) strikt eingehalten wird;
- `--debug` ist nicht obligatorisch, kann aber helfen (du kannst `--release` verwenden, wenn du es vorziehst);
- `--path .` weist `cargo install` an, aus dem aktuellen Verzeichnis zu installieren.

Nach Ausführung dieses Befehls wird eine ausführbare Datei `rgb-lightning-node` in deinem `$CARGO_HOME/bin/` verfügbar sein. Stelle sicher, dass dieser Pfad in deinem `$PATH` ist, damit du den Befehl von jedem Verzeichnis aus aufrufen kannst.

### Leistungsanforderungen

Um zu funktionieren, benötigt der `rgb-lightning-node`-Daemon das Vorhandensein und die Konfiguration von:


- Einem **bitcoind**-Knoten

Jede RLN-Instanz muss mit `bitcoind` kommunizieren, um deine On-Chain-Transaktionen zu übertragen und zu überwachen. Die Authentifizierung (Login/Passwort) und die URL (Host/Port) müssen dem Daemon mitgeteilt werden.


- Einem **Indexer** (Electrum oder Esplora)

Der Daemon muss in der Lage sein, On-Chain-Transaktionen aufzulisten und zu untersuchen, insbesondere um den UTXO zu finden, auf dem ein Vermögenswert verankert wurde. Du musst die URL Deines Electrum-Servers oder Esplora angeben.


- Einem **RGB-Proxy**

Wie in den vorangegangenen Kapiteln beschrieben, ist der **Proxy-Server** eine Komponente (optional, aber sehr empfehlenswert), die den Austausch von *consignments* zwischen Lightning-Teilnehmern vereinfacht. Auch hier muss eine URL angegeben werden.

IDs und URLs werden eingegeben, wenn der Daemon über die API _freigegeben_ wird. Mehr dazu später.

### Regtest-Start

Für den einfachen Gebrauch gibt es ein `regtest.sh`-Skript, das über Docker automatisch eine Reihe von Diensten startet: `bitcoind`, `electrs` (Indexer), `rgb-proxy-server`.

![RGB-Bitcoin](assets/en/100.webp)

Damit kannst du eine lokale, isolierte, vorkonfigurierte Umgebung starten. Bei jedem Neustart werden Container und Datenverzeichnisse erstellt und vernichtet. Wir beginnen mit dem Start:

```bash
./regtest.sh start
```

Dieses Skript wird:


- ein `docker/` Verzeichnis zum Speichern erstellen;
- `bitcoind` in regtest ausführen, ebenso wie den Indexer `electrs` und den `rgb-proxy-server`;
- Warten, bis alles gebrauchsfertig ist.

![RGB-Bitcoin](assets/en/101.webp)

Als nächstes werden wir mehrere RLN starten. Führe Sie in separaten Shells aus, z.B. (um 3 RLN-Knoten zu starten):

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RGB-Bitcoin](assets/en/102.webp)


- Der Parameter `--network regtest` zeigt die Verwendung der regtest-Konfiguration an;
- die Option `-daemon-listening-port` gibt an, an welchem REST-Port der Lightning-Knoten auf API-Aufrufe (JSON) warten soll;
- der Parameter `--ldk-peer-listening-port` gibt an, auf welchem Lightning p2p-Port gelauscht werden soll;
- `dataldk0/`, `dataldk1/` sind die Pfade zu den Speicherverzeichnissen (jeder Knoten speichert seine Daten separat).

du kannst auch von deinem Browser aus Befehle auf deinem RL-Knoten ausführen:

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Damit ein Knoten einen Kanal öffnen kann, muss er zunächst Bitcoins auf einer Adresse haben, die mit dem folgenden Befehl erzeugt wurde (zum Beispiel für Knoten Nr. 1):

```bash
curl -X POST http://localhost:3001/address
```

In der Antwort wird dir eine Adresse mitgeteilt.

![RGB-Bitcoin](assets/en/103.webp)

Mit dem `bitcoind` Regtest werden wir ein paar Bitcoins schürfen. Gib ein:

```bash
./regtest.sh mine 101
```

![RGB-Bitcoin](assets/en/104.webp)

Sende das Geld an die oben angegebene Adresse des Knotens:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RGB-Bitcoin](assets/en/105.webp)

Dann mine einen Block, um die Transaktion zu bestätigen:

```bash
./regtest.sh mine 1
```

![RGB-Bitcoin](assets/en/106.webp)

### Testnet-Start (ohne Docker)

Wenn du ein realistischeres Szenario testen willst, kannst du 3 RLN im Testnetz statt im Regtest starten, die auf öffentliche Dienste verweisen:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Wenn keine Konfiguration gefunden wird, versucht der Daemon standardmäßig, diese Services:


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- `indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Mit diesen Anmeldedaten:


- `bitcoind_rpc_username`: `Benutzer`
- `bitcoind_rpc_username`: `passwort`

Du kannst diese Elemente auch über die API `init`/`unlock` anpassen.

### Ausgabe eines RGB-Tokens

Um einen Token auszugeben, beginnen wir mit der Erstellung "färbbarer" UTXOs:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
        "up_to": false,
        "num": 4,
        "size": 2000000,
        "fee_rate": 4.2,
        "skip_sync": false
      }' \
  http://localhost:3001/createutxos
```

![RGB-Bitcoin](assets/en/107.webp)

Du kannst de Befehle natürlich anpassen. Um die Transaktion zu bestätigen, minen wir einen Block:

```bash
./regtest.sh mine 1
```

Wir können nun ein RGB-Asset erstellen. Der Befehl hängt von der Art des Assets, das du erstellen möchtest, und seinen Parametern ab. Hier erstelle ich ein NIA-Token (*Non Inflatable Asset*) mit dem Namen "Plan ₿ Academy" und einer Menge von 1000 Einheiten. Mit der `Präzision` kannst du die Teilbarkeit der Einheiten festlegen.

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
        "amounts": [
          1000
        ],
        "ticker": "Plan ₿ Academy",
        "name": "Plan ₿ Academy",
        "precision": 0
      }' \
  http://localhost:3001/issueassetnia
```

![RGB-Bitcoin](assets/en/108.webp)

Die Antwort enthält die ID des neu erstellten Assets. Vergesse nicht, dir diese Kennung zu merken. In meinem Fall lautet sie:

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RGB-Bitcoin](assets/en/109.webp)

Du kannst es dann auf die Blockchain übertragen oder in einem Lightning-Kanal zuweisen. Genau das werden wir im nächsten Abschnitt tun.

### Öffnen eines Kanals und Übertragen eines RGB-Assets

Du musst deine Node zunächst mit einem Peer im Lightning-Netzwerk verbinden, indem du den Befehl `/connectpeer` verwendest. In meinem Beispiel kontrolliere ich beide Nodes. Ich rufe also den öffentlichen Schlüssel meines zweiten Lightning-Knotens mit diesem Befehl ab:

```bash
curl -X 'GET' \
  'http://localhost:3002/nodeinfo' \
  -H 'accept: application/json'
```

Der Befehl gibt den öffentlichen Schlüssel meines Knotens Nr. 2 zurück:

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RGB-Bitcoin](assets/en/110.webp)

Als Nächstes öffnen wir den Kanal, indem wir das entsprechende Asset (`Plan ₿ Academy`) angeben. Mit dem Befehl `/openchannel` kannst du die Größe des Kanals in Satoshis festlegen und entscheiden, ob das RGB-Asset einbezogen werden soll. Es hängt davon ab, was du erstellen willst, aber in meinem Fall lautet der Befehl:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
        "peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
        "capacity_sat": 1000000,
        "push_msat": 10000000,
        "asset_amount": 500,
        "asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
        "public": true,
        "with_anchors": true,
        "fee_base_msat": 1000,
        "fee_proportional_millionths": 0,
        "temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
      }' \
  http://localhost:3001/openchannel
```

Weitere Informationen findest du hier:


- `peer_pubkey_and_opt_addr`: Identifiert des Peers, mit dem wir eine Verbindung herstellen wollen (der öffentliche Schlüssel, den wir zuvor gefunden haben);
- `capacity_sat`: Gesamtkapazität des Kanals in Satoshis;
- `push_msat`: Menge in Millisatoshis, die zunächst an den Peer übertragen wird, wenn der Kanal geöffnet wird (hier übertrage ich sofort 10.000 Sats, damit er später eine RGB-Übertragung vornehmen kann);
- `asset_amount`: Menge der RGB-Assets, die dem Kanal zugewiesen werden sollen;
- `asset_id`: Eindeutige ID des RGB-Assets, das in den Kanal eingebunden ist;
- `public`: Gibt an, ob der Kanal für die Weiterleitung im Netz öffentlich gemacht werden soll.

![RGB-Bitcoin](assets/en/111.webp)

Um die Transaktion zu bestätigen, werden 6 Blöcke gemined:

```bash
./regtest.sh mine 6
```

![RGB-Bitcoin](assets/en/112.webp)

Der Lightning-Kanal ist nun offen und enthält auch 500 Plan ₿ Academy-Token auf der Seite des Knotens Nr. 1. Wenn Knoten Nr. 2 "Plan ₿ Academy"-Token erhalten möchte, muss er eine Rechnung erstellen. So geht's:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
        "amt_msat": 3000000,
        "expiry_sec": 420,
        "asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
        "asset_amount": 100
      }' \
  http://localhost:3002/lninvoice
```

Mit:


- `amt_msat`: Rechnungsbetrag in Millisatoshis (mindestens 3000 sats);
- `expiry_sec` : Verfallszeit der Rechnung in Sekunden;
- `asset_id`: ID des RGB-Vermögenswertes, der der Rechnung zugeordnet ist;
- `asset_amount`: Menge der mit dieser Rechnung zu übertragenden RGB-Assets.

Als Antwort erhalten wir eine RGB-Rechnung (wie in den vorherigen Kapiteln beschrieben):

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RGB-Bitcoin](assets/en/113.webp)

Wir werden diese Rechnung nun vom ersten Knoten bezahlen, der den nötigen Bestand an "Plan ₿ Academy"-Token besitzt:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
        "invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
      }' \
  http://localhost:3001/sendpayment
```

![RGB-Bitcoin](assets/en/114.webp)

Die Zahlung ist erfolgt. Dies kann durch Ausführen des Befehls überprüft werden:

```bash
curl -X 'GET' \
  'http://localhost:3001/listpayments' \
  -H 'accept: application/json'
```

![RGB-Bitcoin](assets/en/115.webp)

Hier erfährst du, wie du einen Lightning-Knoten einrichtest, der für den Transport von RGB-Assets modifiziert wurde. Diese Demonstration basiert auf:


- Einer regtest-Umgebung (über `./regtest.sh`) oder testnet;
- Einem Lightning-Knoten (`rgb-lightning-node`) basierend auf einem `bitcoind`, einem Indexer und einem `rgb-proxy-server`;
- Einer Reihe von JSON REST APIs für das Öffnen/Schließen von Kanälen, die Ausgabe von Token, die Übertragung von Vermögenswerten über Lightning, usw.

Dank dieses Prozesses:


- Beinhalten Lightning Engagement Transaktionen einen zusätzlichen Output (OP_RETURN oder Taproot) mit dem Anchor eines RGB-Zustandsübergangs;
- Werden Überweisungen genauso durchgeführt wie herkömmliche Lightning-Zahlungen, allerdings mit dem Zusatz eines RGB-Tokens;
- Können mehrere RLN-Knoten miteinander verbunden werden, um Zahlungen über mehrere Knoten zu routen und mit ihnen zu experimentieren, vorausgesetzt, es ist ausreichend Liquidität sowohl in Bitcoins als auch im RGB-Asset auf dem Pfad vorhanden.

Das Projekt befindet sich noch in der Alphaphase. Es wird daher dringend empfohlen, sich auf Testumgebungen (regtest, testnet) zu beschränken.

Die Möglichkeiten, die sich durch diese LN-RGB-Kompatibilität eröffnen, sind beträchtlich: Stablecoins auf Lightning, Layer-2 DEXes, Übertragung von fungiblen Token oder NFTs zu sehr niedrigen Kosten... In den vorangegangenen Kapiteln wurden die konzeptionelle Architektur und die Validierungslogik skizziert. Jetzt hast du einen praktischen Überblick darüber, wie du einen solchen Knoten für deine zukünftigen Entwicklungen oder Tests zum Laufen bringen kannst.

# Letzter Abschnitt

<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>

## Rezensionen und Bewertungen

<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>

<isCourseReview>true</isCourseReview>

## Schlussfolgerung

<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>

<isCourseConclusion>true</isCourseConclusion>
