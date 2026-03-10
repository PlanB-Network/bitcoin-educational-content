---
name: Programmierung Bitcoin
goal: Erstellen einer vollständigen Bitcoin-Bibliothek von Grund auf und Verstehen der kryptografischen Grundlagen von Bitcoin
objectives: 

 - Implementierung der Arithmetik endlicher Felder und elliptischer Kurven in Python
 - Bitcoin-Transaktionen programmatisch konstruieren und parsen
 - Erstellen von Testnetzadressen und Verteilen von Transaktionen über das Netz
 - Beherrschung der mathematischen Grundlagen des Bitcoin-Sicherheitsmodells

---
# Eine Reise durch die Skripte und Programme von Bitcoin


Dieser zweitägige Intensivkurs, der von Jimmy Song geleitet wird, führt Sie tief in die technischen Grundlagen von Bitcoin ein, indem er eine komplette Bitcoin-Bibliothek von Grund auf aufbaut. Beginnend mit der grundlegenden Mathematik der endlichen Felder und elliptischen Kurven, werden Sie durch Transaktionsparsing, Skriptausführung und Netzwerkkommunikation fortschreiten. Durch praktische Programmierübungen in Jupyter-Notizbüchern werden Sie Ihre eigene Testnetzadresse erstellen, Transaktionen manuell konstruieren und sie direkt an das Netzwerk senden - und dabei ein tiefes Verständnis der kryptografischen Prinzipien erlangen, die Bitcoin sicher und vertrauenswürdig machen.


Viel Spaß auf der Reise!

Hinweis: Die Videos zu diesem Kurs sind nur auf Englisch verfügbar.

+++

# Einführung


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Überblick über den Kurs


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Willkommen zum Kurs PRO 202 _**Programmierung von Bitcoin**_, einer intensiven Reise, die Sie von der Arithmetik mit endlichen Feldern bis hin zum Aufbau und der Übertragung echter Transaktionen auf Bitcoins Testnet führt.


In diesem Kurs werden Sie schrittweise eine Bitcoin-Bibliothek in Python aufbauen und sich gleichzeitig die kryptografischen, protokolltechnischen und softwaretechnischen Grundlagen aneignen, die notwendig sind, um die Sicherheit und das Innenleben von Bitcoin genau zu verstehen. Der Ansatz von PRO 202 ist durch und durch praxisorientiert: Jedes Konzept wird sofort in Jupyter-Notebooks implementiert, um sicherzustellen, dass sich Theorie und Code gegenseitig verstärken.


### Grundlegende mathematische Konzepte für Bitcoin


In diesem ersten Abschnitt werden die unverzichtbaren mathematischen Grundlagen geschaffen. Sie werden endliche Feldarithmetik und elliptische Kurvenoperationen (Gruppengesetz, Addition, Verdopplung, skalare Multiplikation...) implementieren - die Voraussetzungen für ECDSA. Das Ziel ist zweierlei: die algebraische Struktur zu verstehen, die kryptografische Signaturen möglich macht, und zuverlässige Python-Tools zu ihrer Handhabung zu entwickeln.


Anschließend werden Sie die Komponenten von ECDSA formalisieren: Schlüsselerzeugung, Punktformatierung, Hashing, Signaturerstellung und Verifizierung. Dieser Abschnitt stellt eine direkte Verbindung zwischen Theorie und Praxis her und betont die Details der Implementierung und die Robustheit des zugrunde liegenden Sicherheitsmodells.


### Bitcoin-Transaktion Innenleben


Im zweiten Abschnitt werden Sie die Struktur einer Bitcoin-Transaktion analysieren: UTXOs, Ein- und Ausgänge, Sequenzen, Skripte, Kodierungen und mehr. Sie werden Code schreiben, um Transaktionen zu konstruieren, zu signieren und zu verifizieren, und dabei ein genaues Verständnis dafür erlangen, was durch den Hash übertragen wird und warum.


Als nächstes werden Sie einen minimalen _Script_ Executor implementieren, wichtige Opcodes überprüfen und Ausgabenpfade validieren. Ziel ist es, Sie in die Lage zu versetzen, das Transaktionsverhalten zu überprüfen, Validierungsfehler zu diagnostizieren und Rückschlüsse auf die Sicherheit der Ausgabenpolitik zu ziehen.


### Bitcoin Netzwerk Innenleben


Im dritten Abschnitt werden Sie die Transaktionen in das allgemeine System einordnen: Blockstruktur, Kopfzeilen, Schwierigkeiten und der Proof-of-Work-Mechanismus. Sie werden Protokollnachrichten, Block-Header und Merkle-Bäume behandeln.


Schließlich werden Sie sich mit Peer-to-Peer-Knotenkommunikation, Nachrichtenoptimierung und der Einführung von SegWit beschäftigen.


Wie bei jedem Kurs über Plan ₿ Academy enthält der letzte Abschnitt eine Bewertung, die Ihr Verständnis festigen soll. Sind Sie bereit, das Innenleben von Bitcoin zu entdecken und den Code zu schreiben, der es antreibt? Fangen wir an!










# Grundlegende mathematische Konzepte für Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Mathematik für Bitcoin-Implementierung

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin Grundlagen der Programmierung: Mathematische Kernstrukturen


Dieser Kurs fasst die grundlegende Mathematik hinter den kryptografischen Systemen von Bitcoin in einem äußerst praktischen Arbeitsablauf zusammen. Die Konzepte werden erklärt, anhand von Beispielen demonstriert und dann in Jupyter Notebook implementiert. Der Leitgedanke ist einfach: Man versteht ein kryptographisches Primitiv nur dann wirklich, wenn man es programmiert. Während des zweitägigen Kurses werden die Teilnehmer generate-Testnetzadressen erstellen, [Transaktionen](https://planb.academy/resources/glossary/transaction-tx) durchführen und übertragen und schließlich ohne Blockexplorer mit dem Netzwerk interagieren. All dies erfordert eine solide Grundlage in endlichen Feldern und elliptischen Kurven.


### Endliche Felder: Der arithmetische Motor der Kryptographie


Ein endliches Feld F(p) ist ein arithmetisches System, das durch eine Primzahl p definiert ist und die Elemente 0 bis p-1 enthält. Primzahlfelder gewährleisten, dass jedes Element, das nicht Null ist, eine Inverse hat und alle Operationen innerhalb des Feldes bleiben. In der Arithmetik wird modulo p für Addition, Subtraktion und Multiplikation verwendet. Pythons `pow(base, exp, mod)` ermöglicht eine effiziente modulare Potenzierung, die für große Exponenten in echten kryptographischen Operationen entscheidend ist.


#### Multiplikatives Verhalten

Multipliziert man ein beliebiges Element k, das nicht Null ist, mit allen Elementen eines Primfeldes, so erhält man eine Permutation des Feldes. Diese Eigenschaft garantiert Einheitlichkeit und verhindert strukturelle Schwächen, wodurch sich Primzahlfelder ideal für die sichere Schlüsselerzeugung und [digitale Signaturen](https://planb.academy/resources/glossary/digital-signature) eignen.


#### Division und der kleine Satz von Fermat

Die Division erfolgt über multiplikative Inverse. Der kleine Satz von Fermat besagt, dass

n^(p-1) ≡ 1 (mod p),

also ist die Inverse n^(p-2). Python unterstützt dies direkt mit `pow(n, -1, p)`. Diese Operationen tauchen ständig in den [ECDSA](https://planb.academy/resources/glossary/ecdsa) und Bitcoin zugrunde liegenden kryptographischen Routinen auf.


### Elliptische Kurven: Nichtlineare Strukturen für Public-Key-Sicherheit


Elliptische Kurven folgen der Gleichung y² = x³ + ax + b. Bitcoin verwendet secp256k1, definiert als y² = x³ + 7 über einem endlichen Feld. Punkte auf einer elliptischen Kurve bilden eine mathematische Gruppe unter Punktaddition. Eine durch zwei Punkte P und Q gezogene Linie schneidet die Kurve in einem dritten Punkt R; die Spiegelung von R an der x-Achse ergibt P + Q. Dieses System ist assoziativ und enthält ein Identitätselement: den Punkt im Unendlichen.


Bei der Verdoppelung eines Punktes wird eine Tangente anstelle einer Sekante verwendet, wobei die Steigung aus der Ableitung der Kurve abgeleitet wird. Obwohl diese Formeln Kalkulationen über reellen Zahlen beinhalten, werden sie vollständig diskret und exakt, wenn die Kurve über einem endlichen Feld definiert ist - ein Kontext, der in Bitcoin verwendet wird.


### Von der Mathematik zur Bitcoin-Kryptographie


Endliche Felder bieten eine deterministische, invertierbare Arithmetik; elliptische Kurven bieten eine nichtlineare Struktur, bei der die Berechnung von k-P einfach ist, die Umkehrung jedoch rechnerisch nicht machbar ist. Die Kombination beider ergibt die Grundlage für die öffentlichen/privaten Schlüssel von Bitcoin, ECDSA-Signaturen und Transaktionssicherheit. Das Verständnis dieser Grundlagen bereitet die Studierenden darauf vor, Schlüssel, Transaktionen und Signaturen direkt zu implementieren - ohne Abstraktionen oder externe Tools.


## Elliptische Kurven Kryptographie

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Dieses Kapitel führt in elliptische Kurven ein, die über endlichen Feldern definiert sind, und erklärt, warum sie das mathematische Rückgrat der Bitcoin-[Kryptographie](https://planb.academy/resources/glossary/cryptography) bilden. Während elliptische Kurven über reellen Zahlen glatt und kontinuierlich erscheinen, erzeugt die Anwendung der gleichen Gleichungen über einem endlichen Feld eine diskrete, verstreute Menge von Punkten. Trotz des visuellen Unterschieds verhalten sich alle Punktadditionsformeln, Steigungen und algebraischen Regeln genau gleich - nur die Arithmetik ändert sich zu modularer Arithmetik. Bitcoin verwendet die Kurve y² = x³ + 7 (secp256k1), die Symmetrie und nichtlineares Verhalten bewahrt, die für die kryptografische Sicherheit wichtig sind.


### Überprüfung der Punkte und Implementierung des endlichen Feldes


Ein Punkt liegt auf einer elliptischen Kurve mit endlichem Feld, wenn seine Koordinaten die Kurvengleichung modulo p erfüllen. Die Überprüfung eines Punktes wie (73,128) auf F₁₃₇ erfordert die Überprüfung, dass y² mod p gleich x³ + 7 mod p ist. Das Überladen von Operatoren stellt sicher, dass alle arithmetischen Operationen - Addition, Multiplikation, Potenzierung, Division - automatisch modulo p durchgeführt werden. Sobald diese Abstraktionen existieren, werden fortgeschrittene kryptografische Operationen einfach zu schreiben und zu verstehen sein.


#### Gruppeneigenschaften und Punktaddition

Die Punkte der elliptischen Kurve bilden eine mathematische Gruppe, die sich addieren lässt. Die Gruppe erfüllt Schließung, Assoziativität, Identität (der Punkt im Unendlichen) und Inversen (Spiegelung an der x-Achse). Geometrische Konstruktionen bestätigen diese Eigenschaften und machen die skalare Multiplikation (P wird wiederholt zu sich selbst addiert) wohldefiniert. Diese Gruppenregeln ermöglichen die Kryptographie mit elliptischen Kurven und gewährleisten ein konsistentes, vorhersehbares Verhalten bei wiederholten Punktoperationen.


### Zyklische Gruppen und das Problem des diskreten Logarithmus


Die Wahl eines Generatorpunktes G auf einer Kurve ermöglicht es uns, eine zyklische Gruppe generate zu bilden: G, 2G, 3G, ..., nG = 0. Die Punkte erscheinen nichtlinear und unvorhersehbar, selbst wenn sie nacheinander erzeugt werden. Diese Unvorhersehbarkeit bildet die Grundlage für das Problem des diskreten Logarithmus: Die Berechnung von P = sG ist einfach, aber die Bestimmung von s aus P ist für große Gruppen rechnerisch undurchführbar. Diese Einwegfunktion macht die Kryptographie mit öffentlichen Schlüsseln sicher. Skalare ([private Schlüssel](https://planb.academy/resources/glossary/private-key)) werden in Kleinbuchstaben geschrieben, Punkte ([öffentliche Schlüssel](https://planb.academy/resources/glossary/public-key)) in Großbuchstaben.


#### Effiziente Skalarmultiplikation

Um sG effizient zu berechnen, verwenden Implementierungen den Double-and-Add-Algorithmus: Sie scannen die Binärdarstellung des Skalars, verdoppeln den Punkt bei jedem Schritt und addieren G nur, wenn das Bit 1 ist. Dadurch wird die Berechnung von O(n) Additionen auf O(log n) reduziert, was praktische kryptografische Operationen sogar mit 256-Bit-Skalaren ermöglicht.


#### Die secp256k1-Kurve in Bitcoin


Bitcoin verwendet die Kurve secp256k1, definiert durch y² = x³ + 7 über einem Primzahlfeld mit p = 2²⁵⁶ - 2³² - 977. Der Generatorpunkt G hat feste Koordinaten, die mit einem deterministischen NUMS-Verfahren ("nothing up my sleeve") gewählt werden. Die Gruppenordnung n ist eine große Primzahl in der Nähe von 2²⁵⁶, wodurch sichergestellt wird, dass jeder Punkt, der nicht Null ist, dieselbe Gruppe erzeugt. Die Größe von 2²⁵⁶ (~10⁷⁷) ist astronomisch groß, so dass die Erzwingung privater Schlüssel physisch unmöglich ist. Selbst eine Billion Supercomputer, die eine Billion Jahre lang laufen, würden den Schlüsselraum nicht nennenswert verkleinern.


### Öffentliche Schlüssel, private Schlüssel und SEC-Serialisierung


Ein privater Schlüssel ist ein zufälliger Skalar s; der öffentliche Schlüssel ist P = sG. Da die Lösung des diskreten Log-Problems undurchführbar ist, kann P weitergegeben werden, ohne s preiszugeben. Öffentliche Schlüssel müssen für die Übertragung im SEC-Format serialisiert werden. Das unkomprimierte SEC-Format verwendet 65 Bytes: Präfix 0x04 + x-Koordinate + y-Koordinate. Das komprimierte Format verwendet nur 33 Bytes: Präfix 0x02 oder 0x03 (je nach Parität von y) + x-Koordinate. Bitcoin hat ursprünglich unkomprimierte Schlüssel verwendet, bevorzugt jetzt aber aus Effizienzgründen komprimierte Schlüssel.


#### Bitcoin Address Erstellung


Bitcoin-Adressen sind Hashes von öffentlichen Schlüsseln, nicht die Rohschlüssel selbst. Um eine generate-Adresse zu erhalten, wird der öffentliche Schlüssel im SEC-Format serialisiert, ein Hash160 ([SHA-256](https://planb.academy/resources/glossary/sha256) und dann RIPEMD-160) berechnet, das Netzwerkpräfix vorangestellt (0x00 für mainnet, 0x6F für testnet), eine Prüfsumme unter Verwendung des doppelten SHA-256 berechnet, die ersten vier Prüfsummenbytes angehängt und das Ergebnis mit Base58 kodiert. Bei dieser Kodierung werden mehrdeutige Zeichen entfernt und die Prüfsumme hinzugefügt, um Transkriptionsfehler zu vermeiden. Die mehrstufige Pipeline verbirgt den öffentlichen Schlüssel, bis eine Ausgabe erfolgt, fügt eine Netzwerkidentifikation hinzu und gewährleistet menschenlesbare, fehlerresistente Adressen.


# Bitcoin-Transaktion Innenleben

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Transaktionsparsing und ECDSA-Signaturen

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### ECDSA verstehen: Bitcoin's Digital Signature Foundation


Bitcoin basiert auf ECDSA, einem auf elliptischen Kurven basierenden Signaturverfahren, das hohe Sicherheit bei weitaus kleineren Schlüsselgrößen als RSA bietet. Seine Sicherheit ergibt sich aus dem Problem des diskreten Logarithmus der elliptischen Kurve: Bei P = eG ist die Berechnung von P einfach, aber die Ableitung von e aus P ist rechnerisch nicht machbar. Diese Asymmetrie ermöglicht die Kryptographie mit öffentlichen Schlüsseln, während die privaten Schlüssel sicher bleiben.


#### DER-Kodierung von ECDSA-Signaturen


Bitcoin kodiert ECDSA-Signaturen unter Verwendung des DER-Formats:


- 0x30 (Sequenzmarkierung)
- längenbyte
- 0x02 + Länge + R Bytes
- 0x02 + Länge + S Bytes


Dadurch entsteht ein zusätzlicher Overhead, der eine 64-Byte-Signatur auf ~71-72 Byte erweitert. [Taproot](https://planb.academy/resources/glossary/taproot) beseitigt diese Ineffizienz durch die Einführung von [Schnorr](https://planb.academy/resources/glossary/schnorr-protocol)-Signaturen fester Größe.


### Unterschriftsverpflichtungen und der Unterschriftsprozess


ECDSA-Signaturen beruhen auf einer Verpflichtungsgleichung: UG + VP = KG. Der Unterzeichner wählt von Null verschiedene U- und V-Werte und eine zufällige [Nonce](https://planb.academy/resources/glossary/nonce) K, die die Kenntnis des privaten Schlüssels beweist, ohne ihn preiszugeben. Die Nachricht wird in Z gehasht, ein zufälliges K wird generiert, R ist die x-Koordinate von KG, und S = (Z + RE)/K. Die Signatur ist das Paar (R, S). Die Sicherheit hängt entscheidend von der Verwendung eines eindeutigen, unvorhersehbaren K ab - wird K wiederverwendet oder weitergegeben, ist der private Schlüssel gefährdet. Moderne Implementierungen verwenden eine deterministische K-Generierung (RFC 6979), um RNG-Ausfälle zu vermeiden.


#### Überprüfung der Unterschrift

Bei Z, (R, S) und dem öffentlichen Schlüssel P berechnet der Prüfer U = Z/S und V = R/S und prüft dann, ob die x-Koordinate von UG + VP gleich R ist. Dies funktioniert, weil die Verifikationsalgebra KG rekonstruiert, ohne den privaten Schlüssel zu benötigen. Um Signaturen zu fälschen, müsste das diskrete Log-Problem gelöst oder die Hash-Funktion gebrochen werden.


#### Schnorr-Signaturen und historischer Kontext


Schnorr-Signaturen sind mathematisch sauberer und unterstützen Aggregationsfunktionen, waren aber bei der Einführung von Bitcoin patentiert. ECDSA bot eine kostenlose Alternative, allerdings mit mehr Komplexität und größeren Signaturen. Nachdem die Patente ausgelaufen waren, fügte Bitcoin über Taproot Schnorr-Signaturen hinzu, die feste 64-Byte-Signaturen und einen verbesserten Datenschutz bieten. ECDSA wird aus Kompatibilitätsgründen weiterhin unterstützt.



### Transaktionsstruktur und Eingaben/Ausgaben


Eine Bitcoin-Transaktion besteht aus:


- version (4 Bytes, Little-Endian)
- eingabeliste
- ausgabeliste
- sperrzeit (4 Bytes)


Die Eingaben referenzieren frühere [UTXOs](https://planb.academy/resources/glossary/utxo) durch ihren Transaktionshash und ihren Ausgabeindex und enthalten ein Entsperrungsskript (scriptSig) und eine Sequenznummer, die für Timelocks oder RBF verwendet wird. Die Ausgaben geben den Betrag (8 Byte) und das Sperrskript (scriptPubKey) an und definieren die Ausgabebedingungen. Bitcoin-Adressen sind Darstellungen dieser [Skripte](https://planb.academy/resources/glossary/script).


#### Das Modell UTXO

Bitcoin verfolgt nicht ausgegebene Ausgaben und nicht Kontosalden. UTXOs müssen vollständig ausgegeben werden - eine teilweise Ausgabe ist nicht möglich. Um 1 BTC von einem 100 BTC UTXO auszugeben, muss eine Transaktion eine Wechselgeldausgabe enthalten. Wird die Wechselgeldausgabe vergessen, wird der Restbetrag zu einer [Mining](https://planb.academy/resources/glossary/mining)-Gebühr.


#### Serialisierung und Parsing von Transaktionen


Transaktionen verwenden ein kompaktes Binärformat. Nach dem Versionsfeld kodiert ein varint die Anzahl der Eingaben. Eingaben umfassen:


- vorheriger Sende-Hash (32 Bytes)
- ausgangsindex (4 Bytes)
- scriptSig (varstr)
- sequenz (4 Bytes)


Die Ausgaben umfassen einen 8-Byte-Betrag und scriptPubKey (varstr). Die Sperrzeit steuert, wann die Transaktion gültig wird. Die Serialisierung verwendet für die meisten Ganzzahlen die Little-Endian-Reihenfolge. Parser verbrauchen Bytes sequentiell und delegieren an spezialisierte Klassen für Eingaben, Ausgaben und Skripte.


### Gebühren, Veränderung und Anpassungsfähigkeit


Die Gebühren sind implizit:

gebühr = Summe(Eingabewerte) - Summe(Ausgabewerte).

Jeder nicht zugewiesene Wert wird zur Gebühr, was eine korrekte Konstruktion der Änderungsausgabe unerlässlich macht. Vor [SegWit](https://planb.academy/resources/glossary/segwit) erlaubten Signaturen eine Verfälschung - eine Änderung von S zu N-S führte zu einer neuen gültigen Transaktion mit einer anderen ID. Bitcoin erzwingt nun eine Low-S-Regel, und SegWit isoliert Signaturen von der txid-Berechnung, was IDs stabil macht und Protokolle der zweiten Schicht wie [Lightning](https://planb.academy/resources/glossary/lightning-network) ermöglicht.


## Bitcoin Skript- und Transaktionsvalidierung

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script ist eine kleine, stapelbasierte Smart-Contract-Sprache, die definiert, wie Coins ausgegeben werden können. Jede Ausgabe trägt einen scriptPubKey (Sperr-Skript) und jede Eingabe trägt ein scriptSig (Entsperr-Skript). Zusammen bilden sie ein Programm, das auf "wahr" ausgewertet werden muss, damit die Ausgabe gültig ist. Das Skript ist absichtlich nicht Turing-komplett, damit alle Ausführungspfade vorhersehbar und im Netzwerk leicht zu validieren sind.


### Skriptoperationen und Ausführungsmodell


Ein Skript ist eine Folge von Datenelementen und Opcodes. Daten-Pushes (Signaturen, öffentliche Schlüssel, Hashes) werden auf dem Stack abgelegt, während Opcodes, die mit `OP_` beginnen, den Stack umwandeln. Nach der Ausführung muss das oberste Stackelement ungleich Null sein, um erfolgreich zu sein. Beispiele: `OP_DUP` dupliziert das oberste Element, `OP_HASH160` wendet SHA256 und dann RIPEMD160 an, und `OP_CHECKSIG` verifiziert eine Signatur gegen den Sighash der Transaktion und einen öffentlichen Schlüssel, wobei 1 für gültig, 0 für ungültig gesetzt wird. Die Parsing-Regeln unterscheiden zwischen Rohdaten (mit Längenpräfix) und Opcodes (nach Byte-Wert), und eine kleine virtuelle Maschine führt sie deterministisch auf jedem [Knoten](https://planb.academy/resources/glossary/node) aus.


### P2PK und P2PKH: Grundlegende Zahlungsmustern


Das erste Muster, Pay-to-Public-Key (P2PK), hat Münzen direkt an einen vollständigen öffentlichen Schlüssel gebunden: der scriptPubKey ist `<pubkey> OP_CHECKSIG`, und der scriptSig ist nur eine Signatur. Es ist einfach, aber platzsparend und legt den öffentlichen Schlüssel offen, bevor die Münzen ausgegeben werden.


#### P2PKH und Adressen

Pay-to-Public-Key-Hash (P2PKH) verbessert dies, indem es auf einen 20-Byte-Hash des öffentlichen Schlüssels verweist. Das SkriptPubKey ist `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, und das SkriptSig liefert `<Signatur> <pubkey>`. Bei der Ausführung wird geprüft, ob der angegebene öffentliche Schlüssel mit dem übergebenen Wert übereinstimmt, und dann wird die Signatur überprüft. Dies verbirgt den öffentlichen Schlüssel bis zur Ausgabezeit, reduziert die Größe und entspricht dem bekannten "1..." mainnet-Adressformat.


### Transaktionsvalidierung und Signatur-Hashing


Ein Knoten, der eine Transaktion validiert, muss sicherstellen:

1) Jede Eingabe verweist auf eine vorhandene, nicht verbrauchte Ausgabe.

2) Gesamtinputwert ≥ Gesamtoutputwert (die Differenz ist die Gebühr).

3) Jedes scriptSig schaltet seinen referenzierten scriptPubKey korrekt frei.


Die Überprüfung einer Signatur erfordert die Konstruktion der exakten Nachricht, die signiert wurde, genannt sighash. Bei altem ECDSA leert die Validierung alle scriptSigs, ersetzt das scriptSig der aktuellen Eingabe durch den entsprechenden scriptPubKey, fügt einen 4-Byte-Hashtyp (normalerweise `SIGHASH_ALL`) hinzu und verdoppelt den Hashwert des Ergebnisses. Dieser 256-Bit-Wert ist das, was `OP_CHECKSIG` verwendet. Alternative Hash-Typen (z.B. `SINGLE`, `NONE`, mit oder ohne `ANYONECANPAY`) ändern, welche Teile der Transaktion bestätigt werden, und ermöglichen so Nischenanwendungen wie kollaborative Finanzierung oder teilweise spezifizierte Transaktionen, aber sie werden in der Praxis selten verwendet.


#### Quadratisches Hashing und SegWit

Da jede Eingabe in einer Legacy-Transaktion eine eigene Sighash-Berechnung über eine Struktur erfordert, die alle Eingaben umfasst, kann die Validierungszeit quadratisch mit der Anzahl der Eingaben wachsen. Große Transaktionen mit mehreren Eingängen führten früher zu spürbaren Verzögerungen bei der Validierung. SegWit hat die Sighash-Berechnung so umgestaltet, dass gemeinsam genutzte Teile zwischengespeichert werden und die Komplexität auf lineare Zeit reduziert wird, wodurch die Skalierbarkeit verbessert und Denial-of-Service-Angriffe erschwert werden.


### Skript-Rätsel und Sicherheitslektionen


Ein Skript kann weit mehr ausdrücken als nur "eine Unterschrift schaltet diese Münzen frei" Script-Rätsel demonstrieren dies, indem sie beliebige Bedingungen kodieren - mathematische Probleme, Hash-Preimage-Herausforderungen oder sogar Kollisionsprämien - bei denen jeder, der die richtigen Daten liefert, die Münzen ausgeben kann. Ausgaben, die sich nur auf öffentliche Daten (keine Signaturen) stützen, sind jedoch anfällig für [Miner](https://planb.academy/resources/glossary/miner)-Frontrunning: Sobald eine gültige Lösung im [Mempool](https://planb.academy/resources/glossary/mempool) auftaucht, kann jeder Miner sie kopieren und die Auszahlung an sich selbst umleiten.


Die praktische Lehre daraus ist, dass Verträge in der realen Welt fast immer Unterschriftenprüfungen enthalten, selbst wenn sie eine komplexere Logik wie Multisig, Timelocks oder Hashlocks enthalten. Unterschriften binden die Lösung an eine bestimmte Partei, wodurch Anreize erhalten bleiben und andere daran gehindert werden, die Auszahlung zu stehlen. Das Verständnis des Skript-Stack-Modells, der Standardmuster und der subtilen Fallstricke ist für die Entwicklung sicherer Bitcoin-Smart Contracts und für Überlegungen darüber, wie Transaktionen im Netzwerk tatsächlich validiert werden, unerlässlich.


## Transaktionsaufbau und Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Gebäude Bitcoin-Transaktionen und P2SH


Die Bitcoin-Transaktionskonstruktion verbindet theoretisches Protokollwissen mit praktischer Umsetzung. Eine Transaktion wählt UTXOs aus, die ausgegeben werden sollen, erstellt Ausgaben mit Sperrskripten, erstellt Signaturen für jede Eingabe und serialisiert alles in genau dem Format, das die Knoten erwarten. Der Prozess erfordert ein Verständnis der Sighash-Erzeugung, des Skriptverhaltens und der korrekten Handhabung von Gebühren und Änderungen.


### Konstruktion der Grundtransaktion


Jeder Transaktionsinput verweist auf einen vorherigen Output durch txid und Index. Die Ausgaben geben Beträge in Satoshis und Sperrscripts an. Die Differenz zwischen den gesamten Eingaben und den gesamten Ausgaben ist die Gebühr. Um eine Eingabe zu signieren, wird eine modifizierte Version der Transaktion serialisiert, ihr Sighash berechnet und mit dem privaten Schlüssel signiert. Die resultierende Signatur und der öffentliche Schlüssel bilden das ScriptSig. Sobald jede Eingabe signiert ist, kann die Rohtransaktion an das Netz gesendet werden.


### Multisignatur-Transaktionen


Bare multisig verwendet `OP_CHECKMULTISIG`, um m-of-n-Signaturen zu verlangen. Aufgrund eines frühen "off-by-one"-Fehlers verbraucht OP_CHECKMULTISIG ein zusätzliches Stackelement und erfordert ein anfängliches "OP_0" in der ScriptSig. Bare Multisig ist funktional, aber ineffizient: Alle öffentlichen Schlüssel erscheinen als on-chain, wodurch die ScriptPubKeys groß, teuer und schwer als Adressen zu kodieren sind. Diese Einschränkungen waren der Grund für die Einführung von Pay-to-Script-Hash.


#### P2SH Architektur

P2SH verbirgt komplexe Skripte hinter einem 20-Byte-HASH160. Der scriptPubKey ist festgelegt: `OP_HASH160 <20-Byte-HASH> OP_EQUAL`. Das zugrundeliegende Erlösungsskript, das Multisig, Timelocks oder andere Bedingungen enthält, wird nur bei der Ausgabe offengelegt und ausgeführt. Der Absender sieht nur den Hash, während der Empfänger das Einlöseskript privat verwaltet. Dieses Design reduziert die on-chain-Größe, verbessert den Datenschutz und ermöglicht komplexe Verträge, ohne die Absender zu belasten.


### P2SH Ausgaben und Durchführung


Um eine P2SH-Ausgabe auszugeben, muss das ScriptSig die erforderlichen Freischaltdaten *und* das Freischaltskript selbst enthalten. Die Validierung erfolgt in zwei Schritten:

1) HASH160(redeem_script) muss mit dem ScriptPubKey-Hash übereinstimmen.

2) Nach der Überprüfung wird das Redem-Skript mit den angegebenen Daten ausgeführt.


Bei der Erzeugung von Signaturen für eine P2SH-Eingabe verwendet der Sighash-Prozess das Redeem-Skript anstelle des scriptPubKey. Jeder Unterzeichner muss über das vollständige redeem-Skript verfügen, um generate gültige Signaturen zu erstellen. P2SH-Adressen verwenden das Versionsbyte 0x05 bei mainnet ("3..."-Adressen) und 0xC4 bei testnet ("2..."-Adressen).


#### Praktische Sicherheitsüberlegungen


Der Verlust eines Einlöseskripts bedeutet den Verlust von Geldern: Zum Ausgeben werden sowohl die privaten Schlüssel als auch das Einlöseskript selbst benötigt. Multisig-Teilnehmer müssen überprüfen, ob ihre öffentlichen Schlüssel korrekt eingebunden sind, bevor sie Einzahlungen akzeptieren. P2SH unterstützt fortgeschrittene Konstruktionen wie Multisig, Timelocks und Hashlocks, aber Fehler in der Skriptlogik können Gelder dauerhaft sperren, so dass Tests im Testnet unerlässlich sind.


P2SH verbessert die Privatsphäre, indem es die Ausgabenbedingungen bis zur ersten Ausgabe verbirgt, aber sobald das Einlöseskript on-chain erscheint, wird es dauerhaft sichtbar. Trotzdem wurde P2SH durch die Vorteile der geringeren Größe, der Abwärtskompatibilität und der flexiblen Vertragsunterstützung zu einem wichtigen Meilenstein, der spätere Upgrades wie SegWit und Taproot beeinflusst hat.


# Bitcoin Netzwerk Innenleben

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin-Blöcke und Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Bitcoin-Blöcke fassen Transaktionen zusammen und sichern sie mit [proof of work](https://planb.academy/resources/glossary/proof-of-work). Jeder [Block](https://planb.academy/resources/glossary/block) enthält einen 80-Byte-[Header](https://planb.academy/resources/glossary/block-header) sowie eine Liste der Transaktionen. Trotz der hohen Energiekosten für die Erzeugung eines gültigen Blocks ist die Verifizierung eines Blocks billig: Für die Speicherung aller 900k Header werden nur 72 MB benötigt, so dass selbst kleine Geräte die proof of work der Kette effizient verifizieren können.


### Coinbase-Transaktionen und Block Rewards


Jeder Block beginnt mit genau einer [Coinbase-Transaktion](https://planb.academy/resources/glossary/coinbase-transaction) - der einzigen Möglichkeit, neue Bitcoin in Umlauf zu bringen. Er hat einen nullten prev-tx-Hash und einen Index von 0xffffffff, der ihn eindeutig identifiziert. Die Subvention begann bei 50 BTC und halbiert sich alle 210.000 Blöcke (50, 25, 12,5, 6,25, 3,125, ...). Die Miner berechnen auch Transaktionsgebühren. Da die 4-Byte-Nonce für moderne ASICs zu klein ist, ändern die Miner die Daten in der Coinbase-Transaktion, um die [Merkle](https://planb.academy/resources/glossary/merkle-tree)-Wurzel zu ändern und zusätzlichen Suchraum zu schaffen. [BIP34](https://planb.academy/resources/glossary/bip) erfordert die Einbettung der Blockhöhe in das Coinbase scriptSig, um sicherzustellen, dass jeder Coinbase txid einzigartig ist.


### Block-Kopffelder und Soft Fork-Signalisierung


Der 80-Byte-Header enthält:


- version (4 Bytes)
- vorheriger Blockhash (32 Bytes)
- Merkle-Wurzel (32 Bytes)
- zeitstempel (4 Bytes)
- bits (Schwierigkeitsziel, 4 Bytes)
- nonce (4 Bytes)


Die Versionsnummern haben sich über BIP9 zu einem Bitfeld-Signalsystem entwickelt, mit dem Bergleute die [Soft-fork](https://planb.academy/resources/glossary/soft-fork)-Bereitschaft koordinieren können. Der Zeitstempel ist ein 32-Bit-Unix-Zeitwert und muss um das Jahr 2106 herum aktualisiert werden.


#### Bits Feld und Ziele

Das Bit-Feld kodiert das Ziel in kompakter Form: Ziel = Koeffizient × 256^(Exponent-3). Gültige Block-Hashes müssen numerisch unter diesem Zielwert liegen. Da Hashes als Little-Endian-Ganzzahlen interpretiert werden, erscheinen gültige Hashes bei der Anzeige in Hexadezimalzahlen oft mit vielen Nullen am Ende.


### Schwierigkeit, Validierung und Anpassungen


Der [Schwierigkeitsgrad](https://planb.academy/resources/glossary/difficulty) ist definiert als lowest_target / current_target und drückt aus, wie viel schwieriger mining heute im Vergleich zum einfachsten möglichen Schwierigkeitsgrad ist. Für die Validierung muss nur der Hash des Headers mit dem Ziel verglichen werden - extrem billig im Vergleich zu mining.


Alle 2016er-Blöcke passt Bitcoin die Schwierigkeit an, um ~10-Minuten-Blockintervalle zu erreichen. Bei der Anpassung wird die tatsächliche Zeit für die vorherigen 2016er Blöcke mit den erwarteten zwei Wochen verglichen. Die Grenzen beschränken die Anpassungen auf einen Faktor von vier. Große reale Ereignisse - wie das mining-Verbot in China - haben die Widerstandsfähigkeit dieses Mechanismus bewiesen, als die Hash-Rate stark einbrach und die Schwierigkeit nach unten angepasst wurde, um dies auszugleichen.


### Blockzuschuss und Gesamt Supply


Die Subvention in Höhe h wird wie folgt berechnet: Subvention = 5_000_000_000 >> (h // 210_000). Daraus ergibt sich der Halbierungsplan, der zu einem Gesamtangebot von ~21 Millionen BTC konvergiert. Die Summierung der geometrischen Reihe (50 + 25 + 12,5 + ...) × 210.000 erklärt die Obergrenze. Miner können weniger als die erlaubte Subvention beanspruchen, aber nie mehr, sonst wird der Block ungültig. Da die Subventionen über aufeinanderfolgende Halbjahre hinweg schrumpfen, werden die Transaktionsgebühren zu einem immer wichtigeren Bestandteil der Einnahmen der Miner und der langfristigen Netzwerksicherheit.


## Netzwerkkommunikation und Merkle-Bäume

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Bitcoin Netzwerkarchitektur


Das [Peer-to-Peer](https://planb.academy/resources/glossary/peertopeer-p2p)-Netzwerk von Bitcoin funktioniert als dezentrales Klatschsystem, bei dem die Knoten Transaktionen und Blöcke weiterleiten, ohne sich gegenseitig zu vertrauen. Neue Knoten booten, indem sie sich an fest kodierte DNS-Seeds wenden, die von den Kernentwicklern gepflegt werden. Diese DNS-Seeds geben die IPs aktiver Peers zurück und ermöglichen es den Knoten, das Netzwerk zu entdecken und dann über getaddr weitere Peers anzufordern. Die Vernetzung ist absichtlich nicht konsenskritisch, so dass sich die Implementierungen unterscheiden können, solange die [Konsensregeln](https://planb.academy/resources/glossary/consensus) unverändert bleiben.


### Nachrichtenstruktur und Handshake


Alle Bitcoin-P2P-Nachrichten verwenden einen festen Umschlag: einen 4-Byte-Magic-Value (F9BEB4D9 für mainnet), einen 12-Byte-ASCII-Befehl, eine 4-Byte-Nutzdatenlänge im Little-Endian-Format, eine 4-Byte-Prüfsumme (die ersten 4 Bytes von [hash](https://planb.academy/resources/glossary/hash-function)256) und die Nutzdaten. Übliche Befehle sind version, verack, inv, getdata, tx, block, getheaders, headers, ping und pong.


Der Handshake beginnt, wenn ein Verbindungsknoten eine Versionsnachricht sendet. Der Empfänger antwortet mit verack und seiner eigenen Version. Sobald beide Seiten diese beiden Nachrichten austauschen, ist die Verbindung aktiv und die Knoten können mit der Weitergabe von Beständen und Daten beginnen.


### Merkle-Bäume und Merkle-Wurzeln


Bitcoin speichert in jedem Blockkopf eine einzelne 32-Byte-Merkle-Wurzel als Verpflichtung für alle Transaktionen im Block. Die Transaktionen werden gehasht (hash256), gepaart, verkettet und wiederholt gehasht, bis ein Hash übrig bleibt. Wenn eine Ebene eine ungerade Anzahl hat, wird der letzte Hash dupliziert. Intern sind die Hashes Big-Endian, während die serialisierten Blockdaten Little-Endian sind, was Umkehrungen vor und nach der Baumkonstruktion erfordert.


#### Merkle-Beweise und SPV

Mit Merkle-Beweisen lässt sich überprüfen, ob eine Transaktion in einem Block enthalten ist, ohne dass der gesamte Block heruntergeladen werden muss. Der Beweis besteht aus Hashes von Geschwistern entlang des Pfades zur Wurzel. Leichtgewichtige SPV-Clients speichern nur Blockheader und fordern diese Beweise von [vollständigen Knoten](https://planb.academy/resources/glossary/full-node) an. Da ein Merkle-Baum logarithmisch wächst, erfordert der Nachweis der Aufnahme in einen Block mit Tausenden von Transaktionen nur einige hundert Bytes.


Taproot erweitert dieses Konzept, indem es die Ausgabenbedingungen an einen Merklized Script Tree (MAST) bindet und nur den ausgeführten Zweig zusammen mit einem Merkle-Beweis preisgibt. Dies verbessert sowohl die Effizienz als auch die Privatsphäre.


### Netzbetrieb und Blocksynchronisation


Die Knoten verwenden getdata, um Transaktionen oder Blöcke anzufordern, wobei sie eine Typ-ID (1=tx, 2=Block, 3=gefilterter Block, 4=kompakter Block) sowie einen 32-Byte-Bezeichner angeben. Für die Kettensynchronisation senden die Knoten getheaders mit einem Startblock-Hash und erhalten bis zu 2000 Header als Antwort. Jeder zurückgesendete Header besteht aus 80 Byte, gefolgt von einer Dummy-Transaktionszahl von Null.


Die vollständige Überprüfung der empfangenen Blöcke erfordert zwei Kontrollen:

1. Der Blockhash muss unter dem im Bitfeld kodierten Zielwert liegen.

2. Die aus allen Transaktionen berechnete Merkle-Wurzel (bei ordnungsgemäßer Handhabung der Endianness) muss mit der Wurzel des Headers übereinstimmen.


Nur wenn beide Bedingungen erfüllt sind, akzeptiert ein Knoten den Block, was dem Bitcoin-Prinzip "Don't trust, verify" entspricht.


## Erweiterte Knotenkommunikation und getrennter Zeuge

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Diese Sitzung vereint fortgeschrittene P2P-Netzwerke mit Segregated Witness und zeigt, wie moderne Bitcoin-Software direkt mit Knoten interagiert, während sie SegWit-taugliche Transaktionsstrukturen verwendet. Entwickler lernen, Blöcke abzurufen, nach relevanten Transaktionen zu suchen und Transaktionen zu konstruieren, indem sie nur rohe Netzwerkkommunikation verwenden - keine Blockexplorer erforderlich.


### Blockbasierter Transaktionsabruf und Datenschutz


[Wallets](https://planb.academy/resources/glossary/wallet) müssen eingehende Zahlungen erkennen, indem sie Blöcke nach Ausgaben durchsuchen, die ihrem scriptPubKey entsprechen. Der Abruf ganzer Blöcke schützt die Privatsphäre besser als die Abfrage einzelner Transaktionen, die starke Signale über die Benutzeraktivität aussenden. Selbst Blockanfragen können bei Ketten mit geringem Volumen Informationen preisgeben, weshalb kompakte Blockfilter (BIP158) für datenschutzfreundliche Light Clients unerlässlich sind. Filter können falsch-positive, aber niemals falsch-negative Ergebnisse liefern, so dass Clients nur potenziell relevante Blöcke herunterladen können, ohne bestimmte Adressen preiszugeben.


### Trustless Netzwerk-Interaktion


Der Arbeitsablauf "get_block" demonstriert die ordnungsgemäße Nutzung des Netzes: Senden von getdata, Empfangen eines Blocks, dann unabhängige Überprüfung der Merkle-Root und proof of work. Ein Block wird nur dann akzeptiert, wenn der empfangene Header-Hash mit dem angeforderten Hash übereinstimmt und seine berechnete Merkle-Root mit dem Header übereinstimmt. Dies verkörpert das Prinzip "Don't trust, verify" und stellt sicher, dass selbst böswillige Peers die Knoten nicht dazu bringen können, veränderte Daten zu akzeptieren.


#### Abrufen von Transaktionen aus Blöcken

Die Transaktionen eines Blocks können durch einfache Iteration nach übereinstimmenden scriptPubKeys durchsucht werden. Produktions-Wallets führen dies kontinuierlich durch, wenn neue Blöcke eintreffen, und weisen die Eigentümerschaft von Ausgaben ausschließlich durch kryptografische Validierung nach, anstatt sich auf APIs von Drittanbietern zu verlassen.


### SegWit Ziele und Aufbau


Segregierter Zeuge (SegWit) behebt die Transaktionsfälschung, indem Unterschriftsdaten aus der txid-Berechnung entfernt werden. Dies ermöglichte zuverlässige vorsignierte Transaktionsketten und machte den Lightning Network praktikabel. SegWit erhöhte auch die Blockkapazität durch die Verwendung von "Blockgewicht": alte Knoten sehen immer noch Blöcke von ≤1 MB, während aktualisierte Knoten bis zu 4 MB einschließlich der Zeugendaten validieren. Versionierte Zeugenprogramme (bisher v0-v1) schaffen einen strukturierten Upgrade-Pfad für künftige Skripttypen.


#### P2WPKH (gebürtig SegWit)


P2WPKH ersetzt die alte P2PKH-Struktur durch ein 22-Byte-Skript: OP_0 + push20 + hash160(pubkey). Durch die Ausgabe werden die Signatur und der Pubkey in ein separates Zeugenfeld verschoben.


- Vor-SegWit-Knoten: siehe "anyone-can-spend", behandeln Sie es als gültig.
- Post-SegWit-Knoten: Erkennen von OP_0 + 20-Byte-Hash und Validierung anhand von Zeugendaten.


Diese Trennung behebt die Fehleranfälligkeit und reduziert die Gebühren. Der Zeuge verwendet eine varint-Zahl, gefolgt von der Signatur und dem Pubkey.


#### P2SH-P2WPKH (Rückwärtskompatibel SegWit)


Damit alte Geldbörsen an SegWit-Adressen senden können, können P2WPKH-Skripte in P2SH verpackt werden.


- scriptPubKey: Standard P2SH hash160(redeemScript)
- scriptSig: das RedeemScript (das P2WPKH-Programm)
- zeuge: Unterschrift + Pubkey


Validierungsebenen:

1. Vor-BIP16-Knoten akzeptieren das redeemScript als gültig.

2. Post-BIP16-Knoten werten ihn aus und lassen OP_0 + Hash auf dem Stapel liegen.

3. SegWit-Knoten führen eine vollständige Zeugenvalidierung durch.


#### P2WSH für komplexe Skripte


P2WSH verallgemeinert SegWit für Multisig und fortgeschrittene Skripte, indem es SHA256(Skript) anstelle von hash160 einsetzt. Ein typischer 2-von-3-Multisig-Zeugenstapel:


- leeres Element (CHECKMULTISIG-Fehler)
- sig1
- sig2
- zeugenschrift (die Multisig-Schrift)


SegWit-Knoten überprüfen, ob SHA256(witnessScript) mit dem scriptPubKey-Hash übereinstimmt und führen ihn dann aus. Die Verwendung von SHA256 und einem 32-Byte-Hash ermöglicht die Unterscheidung von P2WSH und P2WPKH und erhöht die Sicherheit.


#### P2SH-P2WSH (Maximale Kompatibilität)


Komplexe SegWit-Skripte können auch in P2SH verpackt werden:


- scriptSig: redeemScript (OP_0 + 32-Byte-Hash)
- zeuge: Unterschriften + witnessScript


Die Validierung durchläuft drei Generationen von Regeln, genau wie bei P2SH-P2WPKH. Dieser Wrapper war für frühe Lightning-Einsätze, die Multisig ohne Malleability benötigten, unerlässlich. Obwohl heute natives P2WSH bevorzugt wird, gewährleistet die umhüllte Form die Kompatibilität mit älteren wallet-Systemen.


### Die Auswirkungen von SegWit


SegWit bereitgestellt:


- stabile Transaktions-IDs
- niedrigere Gebühren durch ermäßigte Zeugendaten
- höherer Blockdurchsatz durch Blockgewicht
- kompatibilität für alte Knotenpunkte
- ein sauberer Upgrade-Pfad für Taproot und zukünftige Erweiterungen


Zusammen mit der vertrauenslosen Interaktion im Netz bilden diese Werkzeuge das Rückgrat der modernen Bitcoin-Entwicklung.



# Letzter Abschnitt


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Rezensionen und Bewertungen


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Abschlussprüfung


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Schlussfolgerung



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>