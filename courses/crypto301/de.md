---
name: Einführung in die Kryptographie
goal: Verständnis der Erstellung einer Bitcoin-Wallet aus kryptographischer Sicht
objectives:
  - Entmystifizierung der Kryptographie-Terminologie im Zusammenhang mit Bitcoin.
  - Beherrschung der Erstellung einer Bitcoin-Wallet.
  - Verständnis der Struktur einer Bitcoin-Wallet.
---

# Eine Reise ins Herz der Kryptographie

Sind Sie von Bitcoin fasziniert? Fragen Sie sich, wie eine Bitcoin-Wallet funktioniert? Machen Sie sich bereit für eine fesselnde Reise ins Herz der Kryptographie! Unser Experte Loïc wird Sie durch die Schaffung einer Bitcoin-Wallet führen und die Geheimnisse hinter einschüchternden technischen Begriffen wie Hashing, Schlüsselableitung und elliptischen Kurven enthüllen. Diese Schulung vermittelt Ihnen nicht nur das Wissen, um die Struktur einer Bitcoin-Wallet zu verstehen, sondern bereitet Sie auch darauf vor, tiefer in die faszinierende Welt der Kryptographie einzutauchen. Sind Sie bereit für diese Reise? Schließen Sie sich uns an und verwandeln Sie Ihre Neugier in Fähigkeiten!

+++

# Einführung in die Kryptographie

![Einführung von Rogzy](https://youtu.be/ul8zU5QWIXg)

Wir heißen Sie herzlich willkommen zu unserem neuen Kurs "Crypto 301: Einführung in die Kryptographie und HD-Wallets", geleitet von unserem Experten Loïc Morel. Dieser Kurs führt Sie in die faszinierende Welt der Kryptographie ein, einer grundlegenden Disziplin der Mathematik, die die Verschlüsselung und Sicherheit Ihrer Daten gewährleistet. In unserem täglichen Leben und insbesondere im Bereich von Bitcoin spielt Kryptographie eine wichtige Rolle. Konzepte wie private und öffentliche Schlüssel, Adressen, Ableitungspfade, Samen und Entropie sind der Kern der Verwendung und Erstellung einer Bitcoin-Wallet. In diesem Kurs wird Loïc Ihnen ausführlich erklären, wie private Schlüssel erstellt werden und wie sie mit Adressen verbunden sind. Loïc wird auch eine Stunde damit verbringen, Ihnen die mathematischen Details der elliptischen Kurve, dieser komplexen mathematischen Kurve, zu erklären. Darüber hinaus werden Sie verstehen, warum die Verwendung von HMAC SHA512 wichtig ist, um Ihre Wallet zu sichern, und was der Unterschied zwischen einem Samen und einem mnemonischen Satz ist.
Das ultimative Ziel dieser Schulung ist es, Ihnen technisch die Prozesse zur Erstellung einer HD-Wallet und die verwendeten kryptographischen Methoden zu vermitteln. Im Laufe der Jahre haben sich Bitcoin-Wallets weiterentwickelt, um durch spezifische BIPs einfacher zu bedienen, sicherer und standardisierter zu werden. Loïc wird Ihnen helfen, diese BIPs zu verstehen, um die Entscheidungen der Bitcoin-Entwickler und Kryptographen zu verstehen. Wie alle Schulungen unserer Universität ist auch diese vollständig kostenlos und Open Source. Das bedeutet, dass Sie sie frei übernehmen und nach Belieben verwenden können. Wir freuen uns auf Ihr Feedback am Ende dieses spannenden Kurses.

![intro par loïc](https://youtu.be/mwuxXLk4Kws)

Guten Tag allerseits, ich bin Loïc Morel, Ihr Führer durch diese technische Erkundung der Kryptographie, die in Bitcoin-Wallets verwendet wird.

Unsere Reise beginnt mit einem Tauchgang in die Tiefen der kryptographischen Hash-Funktionen. Gemeinsam werden wir die Mechanismen des unverzichtbaren SHA256 demontieren und verschiedene Algorithmen zur Ableitung erkunden.

Wir werden unser Abenteuer fortsetzen, indem wir die mysteriöse Welt der digitalen Signaturen entschlüsseln. Sie werden entdecken, wie die Magie der elliptischen Kurven auf diese Signaturen angewendet wird, und wir werden erklären, wie der öffentliche Schlüssel aus dem privaten Schlüssel berechnet wird. Und natürlich werden wir uns mit dem Akt des Signierens mit dem privaten Schlüssel befassen.

Dann werden wir in die Vergangenheit zurückkehren, um die Entwicklung von Bitcoin-Wallets zu sehen, und uns mit den Konzepten von Entropie und Zufallszahlen befassen. Wir werden die berühmte Mnemonik-Phrase überprüfen und dabei auch auf die Passphrase eingehen. Sie werden sogar die Möglichkeit haben, ein einzigartiges Erlebnis zu erleben, indem Sie einen Seed aus 128 Würfelwürfen erstellen!

Mit diesem soliden Fundament werden wir bereit sein für den entscheidenden Teil: die Erstellung einer Bitcoin-Wallet. Vom Entstehen des Seeds und des Master-Schlüssels über die Untersuchung der erweiterten Schlüssel bis hin zur Ableitung von Kinderschlüsselpaaren wird jeder Schritt genau untersucht. Wir werden auch die Struktur der Wallet und die Ableitungspfade diskutieren.

Zum Abschluss werden wir unseren Weg fortsetzen und uns mit Bitcoin-Adressen befassen. Wir werden erklären, wie sie erstellt werden und welche wichtige Rolle sie im Betrieb von Bitcoin-Wallets spielen.

Begleiten Sie mich auf dieser faszinierenden Reise und bereiten Sie sich darauf vor, das Universum der Kryptographie wie nie zuvor zu erkunden. Lassen Sie Ihre Vorurteile hinter sich und öffnen Sie Ihren Geist für eine neue Art, Bitcoin und seine grundlegende Struktur zu verstehen.

# Hash-Funktionen

## Einführung in kryptographische Hash-Funktionen im Zusammenhang mit Bitcoin

![die Funktionen kryptographischer Hashes](https://youtu.be/dvnGArYvVr8)

Willkommen zu unserer heutigen Sitzung, die sich der tiefen Eintauchung in die kryptographische Welt der Hash-Funktionen widmet, einem wesentlichen Eckpfeiler der Sicherheit des Bitcoin-Protokolls. Stellen Sie sich eine Hash-Funktion als einen äußerst effizienten kryptographischen Entschlüsselungsroboter vor, der Informationen jeder Größe in einen einzigartigen und festen digitalen Fingerabdruck, genannt "Hash", umwandelt. Im Laufe unserer Erkundung werden wir das Profil kryptographischer Hash-Funktionen skizzieren, ihre Verwendung im Bitcoin-Protokoll hervorheben und die spezifischen Ziele definieren, die diese kryptographischen Funktionen erreichen müssen.

Das Skizzieren des Profils kryptographischer Hash-Funktionen erfordert das Verständnis zweier wesentlicher Eigenschaften: ihrer Unumkehrbarkeit und ihrer Fälschungssicherheit. Jede kryptographische Hash-Funktion ist wie ein einzigartiger Künstler, der für jede Eingabe einen eigenen "Hash" produziert. Selbst eine leicht abweichende Bürste verändert das endgültige Bild erheblich, d.h. den Hash. Diese Funktionen wirken wie digitale Wächter, die die Integrität von heruntergeladenen Software überprüfen. Eine weitere entscheidende Eigenschaft, die sie besitzen, ist ihre Kollisionssicherheit. Sicherlich sind Kollisionen im Hash-Universum unvermeidlich, aber eine ausgezeichnete kryptographische Hash-Funktion minimiert sie erheblich. Es ist, als ob jeder Hash ein Haus in einer riesigen Stadt wäre; trotz der enormen Anzahl von Häusern sorgt eine gute Hash-Funktion dafür, dass jedes Haus eine eindeutige Adresse hat.

Lassen Sie uns nun auf den stürmischen Gewässern veralteter Hash-Funktionen navigieren. SHA0, SHA1 und MD5 gelten heute als verrostete Schalen im Ozean der kryptographischen Hashes. Sie werden oft nicht empfohlen, da sie ihre Kollisionssicherheit verloren haben. Das Schubladenprinzip erklärt, warum es trotz unserer besten Bemühungen unmöglich ist, Kollisionen aufgrund der Begrenzung der Ausgabegröße zu vermeiden. Es ist auch wichtig zu beachten, dass die Widerstandsfähigkeit gegen die zweite Bildung von Bildern von der Widerstandsfähigkeit gegen Kollisionen abhängt. Um wirklich als sicher zu gelten, muss eine Hash-Funktion Kollisionen, zweite Bildung von Bildern und Bildung von Bildern widerstehen.
Schlüsselelement im Bitcoin-Protokoll ist die SHA-256-Hashfunktion, die das Schiff steuert. Andere Funktionen wie SHA-512 werden für die Ableitung mit HMAC und PBKDF verwendet. Darüber hinaus wird RIPMD160 verwendet, um einen Abdruck auf 160 Bits zu reduzieren. Wenn wir von HASH256 und HASH160 sprechen, beziehen wir uns auf die Verwendung eines doppelten Hashs mit SHA-256 und RIPMD. Die Verwendung von HASH160 ist besonders vorteilhaft, da sie die Sicherheit von SHA-256 nutzt und gleichzeitig die Größe des Abdrucks reduziert.

Zusammenfassend ist das ultimative Ziel einer kryptografischen Hashfunktion, eine Information beliebiger Größe in einen Abdruck fester Größe zu transmutieren. Um als sicher anerkannt zu werden, muss sie mehrere Aspekte haben: Unumkehrbarkeit, Fälschungssicherheit, Kollisionsresistenz und Zweitbildresistenz.

Nach dieser Erkundung haben wir die kryptografischen Hashfunktionen entmystifiziert, ihre Verwendung im Bitcoin-Protokoll aufgezeigt und ihre spezifischen Ziele untersucht. Wir haben gelernt, dass Hashfunktionen als sicher gelten müssen, wenn sie resistent gegen Preimage, Zweitbild, Kollisionen und Fälschungen sind. Wir haben auch das Spektrum der verschiedenen Hashfunktionen untersucht, die im Bitcoin-Protokoll verwendet werden. In unserer nächsten Sitzung werden wir uns in das Herzstück der SHA256-Hashfunktion vertiefen und die faszinierenden Mathematik entdecken, die ihr ihre einzigartigen Eigenschaften verleiht.

## Die Mechanik von SHA256

![Die Mechanik von SHA256](https://youtu.be/74SWg_ZbUj4)

Willkommen zur Fortsetzung unserer faszinierenden Reise durch die kryptografischen Labyrinthe der Hashfunktion. Heute lüften wir das Geheimnis von SHA256, einem komplexen, aber genialen Prozess, den wir in unserer vorherigen Diskussion über Hashfunktionen eingeführt haben. Wir machen einen Schritt weiter in diesem Labyrinth, indem wir mit der Vorverarbeitung von SHA256 beginnen. Stellen Sie sich die Vorverarbeitung wie die Zubereitung eines köstlichen Gerichts vor, bei dem wir "Füllbits" hinzufügen, um sicherzustellen, dass die Größe unserer Hauptzutat, der Eingabe, ein perfektes Vielfaches von 512 Bits erreicht. All dies mit dem ultimativen Ziel, einen köstlichen 256-Bit-Hash aus einer Zutat variabler Größe zu generieren.

In diesem kryptografischen Rezept spielen wir mit Bits, die eine anfängliche Nachrichtengröße haben, die wir M nennen werden. Ein Bit ist für den Trenner reserviert, während P Bits für die Polsterung verwendet werden. Darüber hinaus legen wir 64 Bits für die zweite Vorverarbeitungsphase beiseite. Das Gesamtergebnis muss ein Vielfaches von 512 Bits sein. Ein bisschen wie sicherstellen, dass alle Zutaten perfekt in unser Gericht passen.
Wir gehen nun zur zweiten Phase der Vorverarbeitung über, die das Hinzufügen der binären Darstellung der Größe der ursprünglichen Nachricht in Bits beinhaltet. Dazu verwenden wir unsere 64 reservierten Bits aus dem vorherigen Schritt. Wir fügen Nullen hinzu, um unsere 64 Bits auf unsere ausgeglichene Eingabe abzurunden. Anschließend mischen wir die ursprüngliche Nachricht, die Bit-Füllung und die Größen-Füllung wie Zutaten in einem Mixer, um unsere ausgeglichene Eingabe zu erhalten.

Jetzt bereiten wir uns auf die ersten Schritte der SHA-256-Funktionsverarbeitung vor. Wie bei jedem guten Rezept benötigen wir einige Grundzutaten, die wir Konstanten und Initialisierungsvektoren nennen. Die Initialisierungsvektoren von A bis H sind die ersten 32 Bits der Dezimalteile der Quadratwurzeln der ersten 8 Primzahlen. Die Konstanten K von 0 bis 63 repräsentieren die ersten 32 Bits der Dezimalteile der Kubikwurzeln der ersten 64 Primzahlen.

Innerhalb der Kompressionsfunktion verwenden wir spezielle Operatoren wie XOR, AND und NOT. Wir verarbeiten die Bits einzeln nach ihrer Rangfolge, indem wir den XOR-Operator und eine Wahrheitstabelle verwenden. Der AND-Operator wird verwendet, um nur dann 1 zurückzugeben, wenn beide Operanden gleich 1 sind, und der NOT-Operator, um den entgegengesetzten Wert eines Operanden zurückzugeben. Wir verwenden auch die SHR-Operation, um die Bits nach rechts um eine bestimmte Anzahl zu verschieben.

Schließlich, nachdem wir die ausgeglichene Eingabe in verschiedene 512-Bit-Nachrichtenblöcke aufgeteilt haben, führen wir 64 Berechnungsrunden in der Kompressionsfunktion durch. Wie bei einem Radrennen verbessert jede Runde unsere Position. Wir addieren modulo 2^32 den Zwischenzustand zum Anfangszustand der Kompressionsfunktion. Die Additionen in der Kompressionsfunktion sind Additionen modulo 2^32, um die Größe der Summen auf 32 Bits zu begrenzen.

Abschließend möchten wir die entscheidende Rolle der Berechnungen in den CH-, MAJ-, σ0- und σ1-Boxen hervorheben. Diese Operationen sind unter anderem die Wächter, die die Robustheit der SHA256-Hashfunktion gegen Angriffe gewährleisten und sie zu einer bevorzugten Wahl zur Sicherung vieler digitaler Systeme machen, insbesondere im Bitcoin-Protokoll. Es ist offensichtlich, dass die Schönheit von SHA256 trotz ihrer Komplexität in ihrer Robustheit liegt, die Eingabe aus dem Hash wiederherzustellen, während die Überprüfung des Hashes für eine gegebene Eingabe eine mechanisch einfache Aktion ist.

## Die verwendeten Algorithmen zur Ableitung

![Die verwendeten Algorithmen zur Ableitung](https://youtu.be/ZF1_BMsOJXc)
Die HMAC- und PBKDF2-Ableitungs-Algorithmen sind Schlüsselkomponenten in der Sicherheitsmechanik des Bitcoin-Protokolls. Sie verhindern eine Vielzahl potenzieller Angriffe und gewährleisten die Integrität von Bitcoin-Wallets.

HMAC und PBKDF2 sind kryptographische Werkzeuge, die für verschiedene Aufgaben in Bitcoin verwendet werden. HMAC wird hauptsächlich eingesetzt, um Angriffe durch Längenerweiterung bei der Ableitung von hierarchisch deterministischen Wallets (HD) zu verhindern, während PBKDF2 verwendet wird, um eine mnemonische Phrase in einen Seed umzuwandeln.

HMAC, das eine Nachricht und einen Schlüssel als Eingabe erhält, generiert eine Ausgabe fester Größe. Um die Einheitlichkeit zu gewährleisten, wird der Schlüssel entsprechend der Blockgröße in der Hash-Funktion angepasst. Im Rahmen der HD-Wallet-Derivation wird HMAC-SHA-512 verwendet. Letzteres arbeitet mit 1024-Bit-Blöcken (128 Bytes) und passt den Schlüssel entsprechend an. Es verwendet die Konstanten OPAD (0x5c) und IPAD (0x36), die so oft wiederholt werden, wie nötig, um die Sicherheit zu erhöhen.

Der HMAC-SHA-512-Prozess beinhaltet die Konkatenation des Ergebnisses von SHA-512, das auf den Schlüssel XOR OPAD und den Schlüssel XOR IPAD angewendet wird, mit der Nachricht. Wenn es mit 1024-Bit-Blöcken (128 Bytes) verwendet wird, wird der Eingangsschlüssel bei Bedarf mit Nullen aufgefüllt und dann mit IPAD und OPAD XORiert. Der modifizierte Schlüssel wird dann mit der Nachricht konkateniert.

Die Chain-Code-Integration einer zusätzlichen Entropiequelle erhöht die Sicherheit der abgeleiteten Schlüssel. Ohne sie könnte ein Angriff das gesamte Wallet kompromittieren und alle Bitcoins stehlen.

PBKDF2 wird verwendet, um eine mnemonische Phrase in einen Seed umzuwandeln. Dieser Algorithmus führt 2048 Durchläufe mit HMAC SHA512 durch. Dank dieser Ableitungs-Algorithmen können zwei verschiedene Eingaben eine eindeutige und feste Ausgabe erzeugen, was das Problem möglicher Angriffe durch Längenerweiterung auf Funktionen der SHA-2-Familie löst.

Ein Angriff durch Längenerweiterung nutzt eine spezifische Eigenschaft einiger kryptographischer Hash-Funktionen aus. Bei einem solchen Angriff kann ein Angreifer, der bereits den Hash einer unbekannten Nachricht besitzt, diesen verwenden, um den Hash einer längeren Nachricht zu berechnen, die eine Erweiterung der ursprünglichen Nachricht darstellt. Dies ist oft möglich, ohne den Inhalt der ursprünglichen Nachricht zu kennen, was zu erheblichen Sicherheitslücken führen kann, wenn eine solche Hash-Funktion für Aufgaben wie die Integritätsprüfung verwendet wird.
Zusammenfassend spielen die HMAC- und PBKDF2-Algorithmen eine wesentliche Rolle bei der Sicherheit der Ableitung von HD-Wallets im Bitcoin-Protokoll. HMAC-SHA-512 wird verwendet, um sich gegen Angriffe durch Längenerweiterung zu schützen, während PBKDF2 die Umwandlung des mnemonischen Satzes in einen Seed ermöglicht. Der Chain-Code fügt eine zusätzliche Entropiequelle in die Schlüsselableitung ein und gewährleistet so die Robustheit des Systems.

# Digitale Signaturen

## Digitale Signaturen und elliptische Kurven

![Digitale Signaturen und elliptische Kurven](https://youtu.be/gOjYiPkx4z8)

In der Welt der Kryptowährungen ist die Sicherheit von Transaktionen von größter Bedeutung. Im Herzen des Bitcoin-Protokolls findet man die Verwendung von digitalen Signaturen, die als mathematischer Beweis dienen, dass man im Besitz eines privaten Schlüssels ist, der mit einem bestimmten öffentlichen Schlüssel verbunden ist. Diese Methode zum Schutz von Daten basiert im Wesentlichen auf einem faszinierenden Bereich der Kryptographie namens elliptische Kurvenkryptographie (ECC).

Die elliptische Kurvenkryptographie ist das Rückgrat der Sicherheit von Bitcoin-Transaktionen. Diese elliptischen Kurven, die an mathematische Kurven erinnern, die man in der Schule studiert hat, sind in einer Vielzahl von kryptographischen Anwendungen nützlich, von Schlüsselaustausch bis hin zur asymmetrischen Verschlüsselung und der Erstellung digitaler Signaturen. Ein interessantes Detail, das elliptische Kurven auszeichnet, ist ihre Symmetrie: Jede nicht vertikale Linie, die zwei Punkte der Kurve schneidet, wird einen dritten Punkt schneiden.

Nun gehen wir etwas tiefer: Das Bitcoin-Protokoll verwendet eine spezielle elliptische Kurve namens SecP256K1 für seine kryptographischen Operationen. Diese Kurve, definiert auf einer endlichen Menge von positiven ganzen Zahlen modulo einer Primzahl von 256 Bits, kann als Punktewolke anstelle einer traditionellen Kurve visualisiert werden. Diese einzigartige Konstruktion ermöglicht es Bitcoin, seine Transaktionen effektiv zu sichern.

Was die Wahl der secp256k1-Kurve für Bitcoin betrifft, ist es interessant zu bemerken, dass sie der secp256r1-Kurve vorgezogen wurde. Diese Kurve wird durch die Parameter a=0 und b=7 definiert und ihre Gleichung lautet y² = x³ + 7 modulo n, wobei n die Primzahl ist, die die Ordnung der Kurve bestimmt.

Wenn man über die Konstanten spricht, die im Bitcoin-System verwendet werden, bezieht man sich in der Regel auf die spezifischen Parameter des Elliptic Curve Digital Signature Algorithm (ECDSA) und des elliptischen Kurvensystems, das von Bitcoin verwendet wird, nämlich die secp256k1-Kurve. Hier sind diese Parameter:

- Primzahlfeld (p): Bitcoin verwendet eine Kurve auf einem Primzahlfeld, wobei p die erste Zahl ist, die dieses Feld definiert. Für die secp256k1-Kurve ist p gleich `p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F` in Hexadezimal oder p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 -1 in Dezimal.
- Kurvenordnung (n): Dies ist die Anzahl der Punkte auf der Kurve, einschließlich des Punktes im Unendlichen. Für secp256k1 ist n gleich `n = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141` in Hexadezimal oder n = 2^256 - 432420386565659656852420866394968145599 in Dezimal.
- Generierungspunkt (G): Der Basispunkt oder Generator ist der Punkt auf der Kurve, von dem aus alle anderen öffentlichen Schlüssel generiert werden. Er hat spezifische x- und y-Koordinaten, die normalerweise in Hexadezimal dargestellt werden. Für secp256k1 sind die Koordinaten von G in Hexadezimal:
  - `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
  - `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

Beachten Sie, dass alle hexadezimalen Werte normalerweise in Basis 16 dargestellt werden, während Dezimalwerte in Basis 10 dargestellt werden. Darüber hinaus werden alle Operationen mit diesen Konstanten modulo p für die Koordinaten von Punkten auf der Kurve und modulo n für Schlüssel- und Signaturoperationen durchgeführt.

Also, wo werden diese berühmten Bitcoins gespeichert? Nicht in einer Bitcoin-Brieftasche, wie man denken könnte. Tatsächlich speichert eine Bitcoin-Brieftasche die privaten Schlüssel, die zum Nachweis des Besitzes der Bitcoins erforderlich sind. Die Bitcoins selbst werden auf der Blockchain gespeichert, einer dezentralisierten Datenbank, die alle Transaktionen archiviert.

Im Bitcoin-System ist die Recheneinheit der Bitcoin (beachten Sie das kleine "b"). Diese ist bis zu acht Dezimalstellen teilbar, wobei die kleinste Einheit der Satoshi ist. UTXOs oder "Unspent Transaction Outputs" repräsentieren die ungenutzten Transaktionsausgänge, die einem Benutzer gehören. Um diese Bitcoins auszugeben, muss der Besitz des privaten Schlüssels nachgewiesen werden, der dem öffentlichen Schlüssel jedes UTXO zugeordnet ist.
Um die Sicherheit von Transaktionen zu gewährleisten, verwendet Bitcoin zwei Protokolle für digitale Signaturen: ECDSA (Elliptic Curve Digital Signature Algorithm) und Schnorr. ECDSA ist ein Signaturprotokoll, das seit seiner Einführung im Jahr 2009 in Bitcoin integriert ist, während Schnorr-Signaturen erst kürzlich im November 2021 hinzugefügt wurden. Obwohl beide Protokolle auf elliptischen Kurvenkryptographie und ähnlichen mathematischen Mechanismen basieren, unterscheiden sie sich hauptsächlich in Bezug auf die Signaturstruktur.

Bevor wir uns tiefer mit diesen Signaturmechanismen beschäftigen, ist es wichtig, zu verstehen, was eine elliptische Kurve ist. Eine elliptische Kurve wird durch die Gleichung y² = x³ + ax + b definiert. Jeder Punkt auf dieser Kurve hat eine charakteristische Symmetrie, die der Schlüssel zu ihrer Nützlichkeit in der Kryptographie ist.

Letztendlich werden verschiedene elliptische Kurven als sicher für die kryptographische Verwendung anerkannt. Die bekannteste ist vielleicht die secp256r1-Kurve. Für Bitcoin hat Satoshi Nakamoto jedoch eine andere Kurve gewählt: die secp256k1.

In der nächsten Sektion dieses Kurses werden wir uns genauer mit dem öffentlichen und privaten Schlüssel befassen, um ein tiefes Verständnis für die Kryptographie auf elliptischen Kurven und das digitale Signaturverfahren zu erlangen. Dies wird der Moment sein, um Ihr Wissen zu festigen und zu verstehen, wie all diese Informationen zusammenwirken, um die Sicherheit des Bitcoin-Protokolls zu gewährleisten.

## Berechnung des öffentlichen Schlüssels aus dem privaten Schlüssel

![Berechnung des öffentlichen Schlüssels aus dem privaten Schlüssel](https://youtu.be/NJENwFU889Y)

In den folgenden Abschnitten dieses Kurses werden wir uns mit den Mechanismen der öffentlichen und privaten Schlüssel befassen, zwei entscheidenden Elementen des Bitcoin-Protokolls. Diese Schlüssel sind durch das Elliptic Curve Digital Signature Algorithm (ECDSA) intrinsisch miteinander verbunden. Ihr Verständnis wird uns einen tiefen Einblick in die Art und Weise geben, wie Bitcoin Transaktionen auf seiner Plattform sichert.

Um zu beginnen, tauchen wir in die Welt des ECDSA-Algorithmus ein. Bitcoin nutzt diesen digitalen Signaturalgorithmus, um private und öffentliche Schlüssel zu verknüpfen. In diesem System ist der private Schlüssel eine zufällige oder pseudozufällige 256-Bit-Zahl. Die Gesamtzahl der Möglichkeiten für einen privaten Schlüssel beträgt theoretisch 2^256, ist aber in der Realität etwas geringer. Um genau zu sein, sind einige 256-Bit-Private Keys für Bitcoin ungültig.
Um mit Bitcoin kompatibel zu sein, muss ein privater Schlüssel zwischen 1 und n-1 liegen, wobei n die Ordnung der elliptischen Kurve darstellt. Dies bedeutet, dass die Gesamtzahl der Möglichkeiten für einen Bitcoin-Privatschlüssel fast gleich 1,158 x 10^77 ist. Um dies in Perspektive zu setzen, ist dies ungefähr die gleiche Anzahl von Atomen im beobachtbaren Universum. Der einzigartige private Schlüssel wird dann verwendet, um einen öffentlichen Schlüssel von 512 Bits zu bestimmen.

Der öffentliche Schlüssel, bezeichnet als K, ist ein Punkt auf der elliptischen Kurve, der aus dem privaten Schlüssel unter Verwendung von Punktoperationen auf der Kurve abgeleitet wird. Es ist wichtig zu beachten, dass die ECDSA-Funktion irreversibel ist, dh es ist unmöglich, den privaten Schlüssel aus dem öffentlichen Schlüssel zurückzugewinnen. Diese Unumkehrbarkeit ist der Eckpfeiler der Sicherheit der Bitcoin-Brieftasche.

Der öffentliche Schlüssel besteht aus zwei 256-Bit-Punkten, die insgesamt 512 Bits ergeben. Es kann jedoch auf eine Anzahl von 264 Bits komprimiert werden. Der Punkt G ist der Ausgangspunkt für die Berechnung aller öffentlichen Schlüssel der Benutzer des Systems.

Eine bemerkenswerte Eigenschaft von elliptischen Kurven ist, dass eine Linie, die die Kurve an zwei Punkten schneidet, auch einen dritten Punkt schneiden wird, der als Punkt O bezeichnet wird. Diese Eigenschaft wird verwendet, um den Punkt U zu bestimmen, der das Gegenteil des Punktes O ist. Das Hinzufügen eines Punktes zu sich selbst erfolgt durch Zeichnen einer Tangente an der Kurve an diesem Punkt, was einen neuen eindeutigen Punkt namens j ergibt. Das Skalarprodukt eines Punktes mit n bedeutet, dass dieser Punkt n-mal zu sich selbst hinzugefügt wird.

Diese Operationen an den Punkten einer elliptischen Kurve bilden die Grundlage für die Berechnung öffentlicher Schlüssel. Wenn der private Schlüssel bekannt ist, ist es einfach, den öffentlichen Schlüssel zu berechnen. Das Wissen des öffentlichen Schlüssels ermöglicht jedoch nicht die Berechnung des privaten Schlüssels, was die Sicherheit des Bitcoin-Systems gewährleistet. Tatsächlich beruht die Sicherheit von öffentlichen und privaten Schlüsseln auf dem Problem des diskreten Logarithmus, einer komplexen mathematischen Frage.

In unserem nächsten Kurs werden wir untersuchen, wie eine digitale Signatur mit dem ECDSA-Algorithmus unter Verwendung eines privaten Schlüssels zum Entsperren von Bitcoins erstellt wird. Bleiben Sie dran für diese aufregende Erkundung der Welt der Kryptowährungen und der Kryptographie.

## Mit dem privaten Schlüssel unterschreiben

![Mit dem privaten Schlüssel unterschreiben](https://youtu.be/h2hIyGgPqkM)
Der Prozess der digitalen Signatur ist eine wichtige Methode, um zu beweisen, dass Sie der Inhaber eines privaten Schlüssels sind, ohne diesen offenlegen zu müssen. Dies wird durch die Verwendung des ECDSA-Algorithmus erreicht, der die Bestimmung eines eindeutigen Nonce, die Berechnung einer spezifischen Zahl V und die Erstellung einer digitalen Signatur aus zwei Teilen, S1 und S2, umfasst. Es ist entscheidend, immer einen eindeutigen Nonce zu verwenden, um Sicherheitsangriffe zu vermeiden. Ein bekanntes Beispiel dafür, was passieren kann, wenn diese Regel nicht befolgt wird, ist der Fall des PlayStation 3-Hacks, der aufgrund der Wiederverwendung des Nonce kompromittiert wurde.

Um eine digitale Signatur mithilfe des ECDSA-Algorithmus (Elliptic Curve Digital Signature Algorithm) zu validieren, sind in der Regel die folgenden Schritte erforderlich:

1. Überprüfen Sie, ob die Werte der Signatur, S1 und S2, im Bereich [1, n-1] liegen. Wenn dies nicht der Fall ist, ist die Signatur ungültig.
2. Berechnen Sie das Inverse von S2 mod n. Wir nennen dies u. Es wird oft wie folgt berechnet: u = (S2)^-1 mod n.
3. Berechnen Sie H, den Hashwert der signierten Nachricht.
4. Berechnen Sie u1 = H _ u mod n und u2 = S1 _ u mod n.
5. Berechnen Sie den Punkt P auf der elliptischen Kurve unter Verwendung von u1, u2 und dem öffentlichen Schlüssel K: P = u1*G + u2*K, wobei G der Generierungspunkt der Kurve ist.
6. Wenn P der unendliche Punkt ist, ist die Signatur ungültig.
7. Berechnen Sie I = x-Koordinate von P mod n.
8. Die Signatur ist gültig, wenn I gleich S1 ist.

Es ist wichtig zu beachten, dass jede Software unterschiedliche Notationen verwenden kann und einige Schritte kombiniert oder neu angeordnet werden können, aber die Grundlogik bleibt gleich. Beachten Sie auch, dass alle arithmetischen Operationen im endlichen Körper durchgeführt werden, der durch die elliptische Kurve definiert ist (mod n, wobei n die Ordnung der Kurve ist). Zur Erinnerung, die secp256k1-Kurve (verwendet in Bitcoin) hat n = 2^256 - 432420386565659656852420866394968145599.

Was die Generierung von öffentlichen und privaten Schlüsseln betrifft, ist es wichtig, sich mit der elliptischen Kurve und dem Generierungspunkt vertraut zu machen. Um einen öffentlichen Schlüssel zu erhalten, muss eine zufällige Zahl als privater Schlüssel, oft als `Nonce` bezeichnet, ausgewählt und in die Gleichung der elliptischen Kurve eingesetzt werden.
Die elliptische Kurve ist ein leistungsstarkes Werkzeug zur Erzeugung sicherer öffentlicher und privater Schlüssel. Um beispielsweise den öffentlichen Schlüssel 3G zu erhalten, zeichnen Sie eine Tangente am Punkt G, berechnen das Gegenteil von -G, um 2G zu erhalten, und addieren G und 2G. Um eine Transaktion durchzuführen, müssen Sie beweisen, dass Sie die Zahl 3 kennen, indem Sie die mit dem öffentlichen Schlüssel 3G verbundenen Bitcoins entsperren.

Um eine digitale Signatur zu erstellen und zu beweisen, dass Sie den privaten Schlüssel kennen, der mit dem öffentlichen Schlüssel 3G verbunden ist, berechnen Sie zuerst eine Nonce und dann den Punkt V, der mit dieser Nonce verbunden ist (im gegebenen Beispiel ist dies 4G). Anschließend berechnen Sie den Punkt T, indem Sie den öffentlichen Schlüssel 3G und den Punkt V addieren, was 7G ergibt.

Die Überprüfung einer digitalen Signatur ist ein entscheidender Schritt bei der Verwendung des ECDSA-Algorithmus, der die Echtheit einer signierten Nachricht bestätigt, ohne den privaten Schlüssel des Absenders zu benötigen. Hier ist, wie es im Detail funktioniert:

In unserem Beispiel haben wir zwei wichtige Werte: T und V. T ist ein numerischer Wert (in diesem Beispiel 7), und V ist ein Punkt auf der elliptischen Kurve (hier als 4G dargestellt). Diese Werte werden bei der Erstellung der digitalen Signatur erzeugt und dann mit der Nachricht gesendet, um die Überprüfung zu ermöglichen.

Wenn der Verifier die Nachricht erhält, erhält er auch diese beiden Werte, T und V.

Hier sind die Schritte, die der Verifier ausführen wird, um die Signatur zu validieren:

1. Zuerst berechnet er den Hash der Nachricht, den wir H nennen werden.
2. Dann berechnet er u1 und u2. Dazu verwendet er die folgenden Formeln:
   - u1 = H \* (S2)^-1 mod n
   - u2 = T \* (S2)^-1 mod n
     Wobei S2 der zweite Teil der digitalen Signatur ist, n die Ordnung der elliptischen Kurve und (S2)^-1 das Inverse von S2 mod n ist.
3. Der Verifier berechnet dann einen Punkt P' auf der elliptischen Kurve mit der Formel: P' = u1 _ G + u2 _ K
   - G ist der Generierungspunkt der Kurve
   - K ist der öffentliche Schlüssel des Absenders
4. Der Verifier berechnet dann I', was einfach die x-Koordinate des Punktes P' modulo n ist.
5. Schließlich bestätigt der Verifier, dass I' gleich T ist. Wenn dies der Fall ist, wird die Signatur als gültig betrachtet. Wenn dies nicht der Fall ist, ist die Signatur ungültig.

Dieses Verfahren stellt sicher, dass nur der Absender, der den entsprechenden privaten Schlüssel besitzt, eine Signatur produzieren konnte, die diesen Überprüfungsprozess besteht.
Zusammenfassend ist die Überprüfung einer ECDSA-Digital-Signatur ein wesentlicher Schritt bei Bitcoin-Transaktionen. Sie gewährleistet, dass die signierte Nachricht während der Übertragung nicht verändert wurde und dass der Absender tatsächlich im Besitz des privaten Schlüssels ist. Diese Methode der digitalen Authentifizierung basiert auf komplexen mathematischen Prinzipien, insbesondere der elliptischen Kurvenarithmetik, während die Vertraulichkeit des privaten Schlüssels gewahrt bleibt. Sie bietet eine solide Sicherheitsgrundlage für kryptografische Transaktionen.

Die Verwaltung dieser Schlüssel und ihre Erstellung sind jedoch weitere wesentliche Fragen bei Bitcoin. Wie generiert man ein neues Schlüsselpaar? Wie organisiert man eine Vielzahl von Schlüsseln sicher und effektiv? Wie kann man sie im Bedarfsfall wiederherstellen?

Um diese Fragen zu beantworten und Ihr Verständnis für die Sicherheit der Kryptografie zu vertiefen, wird sich unser nächster Kurs auf das Konzept des Hierarchischen Deterministischen Wallets (HD Wallets) und die Verwendung von Mnemonik-Phrasen konzentrieren. Diese Mechanismen bieten elegante Möglichkeiten, Ihre Kryptowährungsschlüssel effektiv zu verwalten und gleichzeitig Sicherheit und Wiederherstellbarkeit zu erhöhen.

# Mnemonik-Phrasen

## Entwicklung von Bitcoin-Wallets

![Entwicklung von Bitcoin-Wallets](https://youtu.be/6tmu1R9cXyk)

Das Hierarchische Deterministische Wallet, oder kurz HD Wallet, spielt eine wichtige Rolle im Kryptowährungs-Ökosystem. Der Begriff "Wallet" mag für Neulinge in diesem Bereich irreführend sein, da er nicht die Aufbewahrung von Geld oder Währungen impliziert. Vielmehr bezieht er sich auf eine Sammlung von privaten kryptografischen Schlüsseln, die von einem einzigen Mutter-Schlüssel abgeleitet werden, dank eines cleveren algorithmischen arithmetischen Verfahrens. Diese privaten Schlüssel, die eine feste Länge von 256 Bits haben, sind das Wesen des Besitzes von Kryptowährungen und werden manchmal etwas grob als "Just a Bunch Of Keys" (JBOC) bezeichnet.

Die Komplexität der Verwaltung dieser Schlüssel wird jedoch durch eine Reihe von Protokollen ausgeglichen, die als Bitcoin Improvement Proposals (BIP) bezeichnet werden. Diese Upgrade-Vorschläge sind der Kern der Funktionalität und Sicherheit von HD Wallets. Zum Beispiel hat das [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), das 2012 gestartet wurde, die Art und Weise revolutioniert, wie diese Schlüssel generiert und gespeichert werden, indem es das Konzept der deterministischen und hierarchischen Schlüsselableitung eingeführt hat. Auf diese Weise wird der Prozess der Sicherung dieser Schlüssel erheblich vereinfacht, während ihr Sicherheitsniveau erhalten bleibt.
Später führte [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) eine bedeutende Innovation ein: die 24-Wort-Mnemonic-Phrase. Dieses System verwandelt eine komplexe und schwer zu merkende Zahlenfolge in eine Reihe gewöhnlicher Wörter, die viel einfacher zu merken und zu speichern sind. Darüber hinaus schlug [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) vor, ein zusätzliches Passwort hinzuzufügen, um die Sicherheit der einzelnen Schlüssel zu erhöhen. Diese aufeinanderfolgenden Verbesserungen führten zu den Standards BIP43 und BIP44, die die Struktur und Hierarchie von HD-Wallets standardisierten und diese Wallets für die breite Öffentlichkeit zugänglicher und einfacher zu bedienen machten.

In den folgenden Abschnitten werden wir tiefer in die Funktionsweise von HD-Wallets eintauchen. Wir werden die Prinzipien der Schlüsselableitung behandeln und die grundlegenden Konzepte von Entropie und Zufallszahlengenerierung untersuchen, die für die Sicherheit Ihres HD-Wallets unerlässlich sind.

Zusammenfassend ist es wichtig zu betonen, dass BIP32 und BIP39 eine zentrale Rolle bei der Gestaltung und Sicherung von HD-Wallets spielen. Diese Protokolle ermöglichen die Generierung einer Vielzahl von Schlüsseln aus einem einzigen Samen, der als zufällige oder pseudozufällige Zahl angesehen wird. Heute werden diese Standards von der Mehrheit der Kryptowährungs-Wallets übernommen, ob sie nun für eine einzige Kryptowährung oder für mehrere Währungstypen ausgelegt sind.

Ich hoffe, dass diese Einführung Ihnen geholfen hat, die Grundlagen von HD-Wallets und ihren verschiedenen Merkmalen besser zu verstehen. Unser Ziel ist es, Ihnen zu helfen, diese wesentlichen Konzepte zu beherrschen und effektiver durch die komplexe Welt der Kryptowährungen zu navigieren. Bleiben Sie also bei uns, während wir in den nächsten Lektionen die Feinheiten und Nuancen dieser faszinierenden Welt weiter erforschen.

## Entropie und Zufallszahlengenerierung

![Entropie und Zufallszahlengenerierung](https://youtu.be/k18yH18w2TE)

Die Bedeutung der Sicherheit von privaten Schlüsseln im Bitcoin-Ökosystem ist unbestreitbar. Sie sind die Eckpfeiler, die die Sicherheit von Bitcoin-Transaktionen gewährleisten. Um jegliche Schwachstellen aufgrund von Vorhersehbarkeit zu vermeiden, müssen diese Schlüssel wirklich zufällig generiert werden, was für den Benutzer schnell zu einer mühsamen Aufgabe werden kann. Eine Lösung für dieses Rätsel ist das Hierarchische Deterministische Wallet oder HD-Wallet. Diese Methode ermöglicht die deterministische und hierarchische Generierung von Kinderschlüsselpaaren aus einer einzigen Information am Basispunkt des Wallets. Hierbei ist Zufälligkeit unverzichtbar, um die Sicherheit der abgeleiteten Schlüssel zu gewährleisten.

Die Generierung von Zufallszahlen ist ein entscheidendes Element in der Kryptographie, um die Integrität von privaten Schlüsseln zu gewährleisten. Um jegliche Schwachstellen aufgrund von Vorhersehbarkeit zu vermeiden, muss ein privater Schlüssel zufällig generiert werden. Die Verwendung eines neuen Schlüsselpaars für jede Transaktion erhöht die Sicherheit weiter, obwohl dies die Sicherung komplizierter macht und die Vertraulichkeit nur teilweise gewährleistet. Zusammenfassend ist die Sicherheit von privaten Schlüsseln eine absolute Priorität, die eine strenge und zufällige Generierung erfordert. HD-Wallets bieten eine Lösung, um die Generierung und Verwaltung von Schlüsseln zu erleichtern und gleichzeitig ein hohes Sicherheitsniveau zu gewährleisten.

Die Generierung von Zufallszahlen auf Computern stellt jedoch eine große Herausforderung dar, da die Ergebnisse nicht wirklich zufällig sind. Daher ist es unerlässlich, einen Random Number Generator (RNG) zu verwenden. Die Arten von RNGs variieren von Pseudo-Random Number Generators (PRNG) bis hin zu True Random Number Generators (TRNG) sowie PRNGs, die eine Entropiequelle integrieren.

Im Falle von Bitcoin werden private Schlüssel aus einer einzigen Information am Basispunkt des Wallets generiert. Diese Information ermöglicht eine deterministische und hierarchische Ableitung von Kinderschlüsselpaaren. Entropie ist das Fundament jedes HD-Wallets, obwohl es keinen Standard für die Generierung dieser Zufallszahl gibt. Daher ist die Generierung von Zufallszahlen ein wichtiger Faktor, um Bitcoin-Transaktionen zu sichern.

Die Überprüfungsphase der Schlüsselgenerierung ist entscheidend, um die Sicherheit und Authentizität der Zufallszahlengenerierung zu gewährleisten, eine grundlegende Maßnahme, um jegliche Schwachstellen aufgrund von Vorhersehbarkeit zu vermeiden. Es wird daher dringend empfohlen, Open-Source-Wallets zu verwenden, um diese Überprüfung zu ermöglichen.
Cependant, es ist wichtig zu beachten, dass einige Hardware-Wallets "closed source" sein können, was die Überprüfung der Generierung der Zufallszahl unmöglich macht. Eine mögliche Umgehung wäre, die Mnemonik-Phrase selbst mit Würfeln zu generieren, obwohl dieser Ansatz einige Risiken birgt. Die Verwendung einer zufällig generierten Passphrase kann dazu beitragen, diese Risiken zu mildern.

Ein Beispiel für die Anwendung dieser Methode ist die "Dice Roll"-Option von CoinKit zur Generierung von Mnemonik-Phrasen. Eine andere Möglichkeit wäre, eine sehr breite Anfangsinformation zu verwenden und diese Information auf 256 Bits mit der SHA-256-Hash-Funktion zu reduzieren, die in der Lage ist, eine gute Zufallszahl zu generieren. Es ist wichtig zu erwähnen, dass die SHA-256-Hash-Funktion kollisionsresistent, fälschungssicher und gegen Pre-Image- und Second-Pre-Image-Angriffe beständig ist.

Letztendlich spielt Zufall eine zentrale Rolle in der Kryptographie und Informatik, und die Fähigkeit, sicher Zufall zu generieren, ist entscheidend für die Sicherheit von privaten Schlüsseln und Bitcoin-Transaktionen. Die Entropie, die im Herzen der Bitcoin-HD-Wallets steht, ist für ihre Sicherheit unerlässlich. In unserer nächsten Lektion werden wir dieses Thema weiter erforschen und genauer darauf eingehen, wie Entropie zur Sicherheit von HD-Wallets beiträgt.

### Unterstütze uns

Dieser Kurs sowie der gesamte Inhalt dieser Universität wurden kostenlos von unserer Community zur Verfügung gestellt. Um uns zu unterstützen, können Sie ihn teilen, Mitglied der Universität werden und sogar über GitHub zu ihrer Entwicklung beitragen. Im Namen des gesamten Teams vielen Dank!

### Kursbewertung

Ein Bewertungssystem für den Kurs wird bald in diese neue E-Learning-Plattform integriert! In der Zwischenzeit vielen Dank für die Teilnahme am Kurs und wenn Sie ihn genossen haben, denken Sie daran, ihn zu teilen.

## Die Mnemonik-Phrase

![Die Mnemonik-Phrase](https://youtu.be/uJERqH9Xp7I)

Die Sicherheit einer Bitcoin-Wallet ist eine wichtige Sorge für alle ihre Benutzer. Eine wesentliche Möglichkeit, die Sicherheit der Wallet zu gewährleisten, besteht darin, eine Mnemonik-Phrase auf der Grundlage von Entropie und Checksumme zu generieren.

Entropie ist das Fundament der Sicherheit von HD-Wallets. Es gibt mehrere Methoden zur Generierung dieser Entropie, einschließlich Pseudozufallszahlengeneratoren (PRNG), echter Zufallszahlengeneratoren (TRNG) oder manueller Generierung. Es ist entscheidend, dass diese Entropie zufällig oder pseudozufällig ist, um die Sicherheit der Wallet zu gewährleisten.
Auf der anderen Seite gewährleistet die Prüfsumme die Überprüfung der Genauigkeit des Wiederherstellungssatzes. Ohne diese Prüfsumme könnte ein Fehler im Satz zur Erstellung einer anderen Brieftasche führen und somit zum Verlust der Mittel führen. Die Prüfsumme wird erhalten, indem die Entropie durch die SHA256-Funktion geleitet und die ersten 8 Bits des Hashes abgerufen werden.

Je nach Größe der Entropie gibt es verschiedene Standards für den mnemonischen Satz. Der am häufigsten verwendete Standard für einen Wiederherstellungssatz mit 24 Wörtern ist eine Entropie von 256 Bits. Die Größe der Prüfsumme wird durch die Teilung der Größe der Entropie durch 32 bestimmt.

Zum Beispiel erzeugt eine Entropie von 256 Bits eine Prüfsumme von 8 Bits. Die Konkatenation von Entropie und Prüfsumme führt zu Größen von jeweils 128 Bits, 160 Bits usw. Abhängig von der Größe der Entropie wird der Wiederherstellungssatz 12 Wörter für 128 Bits, 15 Wörter für 160 Bits und 24 Wörter für 256 Bits enthalten.

Um Bits in Sätze umzuwandeln, wird jeder Abschnitt einem Wort aus einer Liste von 2048 Wörtern zugeordnet. Es ist wichtig zu beachten, dass kein Wort die ersten vier Buchstaben in derselben Reihenfolge aufweist.

Es ist unerlässlich, den 24-Wort-Wiederherstellungssatz zur Aufrechterhaltung der Integrität der Bitcoin-Brieftasche zu sichern. Die beiden am häufigsten verwendeten Standards basieren auf einer Entropie von 128 oder 256 Bits und einer Konkatenation von 12 oder 24 Wörtern. Das Hinzufügen einer Passphrase ist eine zusätzliche Option zur Stärkung der Brieftaschensicherheit.

Zusammenfassend ist die Generierung eines mnemonischen Satzes zur Sicherung einer Bitcoin-Brieftasche ein entscheidender Prozess. Es ist wichtig, die Standards des mnemonischen Satzes je nach Größe der Entropie einzuhalten. Die Sicherung des 24-Wort-Wiederherstellungssatzes ist unerlässlich, um einen Verlust von Mitteln zu vermeiden. Wir danken Ihnen für Ihre Aufmerksamkeit und freuen uns auf unseren nächsten Kurs über Kryptowährungen.

## Die Passphrase

![Die Passphrase](https://youtu.be/dZkOYO7MXwc)

Die Passphrase ist ein zusätzliches Passwort, das in eine Bitcoin-Brieftasche integriert werden kann, um ihre Sicherheit zu erhöhen. Die Verwendung ist optional und liegt im Ermessen des Benutzers. Durch Hinzufügen willkürlicher Informationen, die zusammen mit dem mnemonischen Satz verwendet werden können, um den Seed der Brieftasche zu berechnen, erhöht die Passphrase die Sicherheit dieser.
Um die Schlüssel einer HD-Wallet abzuleiten, sind sowohl die Mnemonik-Phrase als auch die Passphrase erforderlich. Die Passphrase ist frei wählbar und kann nahezu unendlich lang sein. Sie ist nicht in der standardisierten Mnemonik-Phrase enthalten, die bestimmten Größen-, Prüfsummen- und Codierungsbeschränkungen unterliegt. Ein Angreifer kann nicht auf die Bitcoins eines Benutzers zugreifen, ohne die Passphrase zu kennen. Letztere spielt eine Rolle bei der Konstruktion und Berechnung aller Wallet-Schlüssel.

Die Funktion PBKDF2 wird verwendet, um den Seed aus der Passphrase zu generieren. Dieser Seed ermöglicht die Ableitung aller Kinderschlüsselpaare der Wallet. Wenn die Passphrase geändert wird, wird die Bitcoin-Wallet vollständig verändert.

Die Passphrase ist ein wesentliches Instrument zur Stärkung der Sicherheit von Bitcoin-Wallets. Sie kann verschiedene Sicherheitsstrategien ermöglichen. Zum Beispiel kann sie verwendet werden, um Duplikate zu erstellen und das Backup der Mnemonik-Phrase zu erleichtern. Sie kann auch die Sicherheit der Wallet verbessern, indem sie die Risiken der zufälligen Generierung der Mnemonik-Phrase verringert.

Eine effektive Passphrase sollte lang (20 bis 40 Zeichen) und vielfältig sein (mit Groß- und Kleinbuchstaben, Zahlen und Symbolen). Sie sollte nicht direkt mit dem Benutzer oder seiner Umgebung verbunden sein. Es ist sicherer, eine zufällige Zeichenfolge anstelle eines einfachen Wortes als Passphrase zu verwenden.

Eine Passphrase ist sicherer als ein einfaches Passwort. Die ideale Passphrase ist lang, vielfältig und zufällig. Sie kann die Sicherheit einer Wallet oder einer Hot-Software erhöhen. Sie kann auch zur Erstellung redundanter und sicherer Backups verwendet werden.

Es ist entscheidend, sich um die Passphrase-Backups zu kümmern, um den Zugriff auf die Wallet zu vermeiden. Eine Passphrase ist eine Option für eine HD-Wallet. Sie kann zufällig mit Würfeln oder einem anderen Pseudozufallszahlengenerator generiert werden. Es wird nicht empfohlen, sich an eine Passphrase oder Mnemonik-Phrase zu erinnern.

In unserem nächsten Kurs werden wir uns ausführlich mit der Funktionsweise des Seeds und dem ersten aus ihm generierten Schlüsselpaar befassen. Zögern Sie nicht, diesen Kurs zu verfolgen, um Ihr Lernen fortzusetzen. Wir freuen uns darauf, Sie bald wiederzusehen.

## Erstellung eines Seeds aus 128 Würfelwürfen!

![Erstellung eines Seeds aus 128 Würfelwürfen!](https://youtu.be/lUw-1kk75Ok)

Die Erstellung eines mnemonischen Satzes ist ein entscheidender Schritt zur Sicherung Ihrer Kryptowährungs-Portfolio. Es gibt mehrere Methoden zur Generierung eines mnemonischen Satzes, aber wir werden uns auf die manuelle Methode konzentrieren, die Würfel verwendet. Es ist wichtig zu betonen, dass diese Methode nicht für ein Portfolio mit hohem Wert geeignet ist. Es wird empfohlen, eine Open-Source-Software oder eine Hardware-Brieftasche zu verwenden, um den mnemonischen Satz zu generieren. Um einen mnemonischen Satz zu erstellen, werden wir Würfel verwenden, um binäre Informationen zu generieren. Das Ziel ist es, den Prozess der Erstellung des mnemonischen Satzes zu verstehen.

**Schritt 1 - Vorbereitung:**
Stellen Sie sicher, dass Sie eine amnestische Linux-Distribution wie Tails OS auf einem USB-Stick installiert haben, um die Sicherheit zu erhöhen. Beachten Sie, dass dieses Tutorial nicht zur Erstellung eines Hauptportfolios verwendet werden sollte.

**Schritt 2 - Generierung einer zufälligen binären Zahl:**
Wir werden Würfel verwenden, um binäre Informationen zu generieren. Werfen Sie 128 Mal einen Würfel und notieren Sie jedes Ergebnis (1 für ungerade, 0 für gerade).

**Schritt 3 - Organisation der binären Zahlen:**
Ordnen Sie die erhaltenen binären Zahlen in Reihen von 11 Ziffern an, um spätere Berechnungen zu erleichtern. Die zwölfte Zeile sollte nur 7 Ziffern enthalten.

**Schritt 4 - Berechnung der Prüfsumme:**

Die letzten 4 Ziffern für die zwölfte Zeile entsprechen der Prüfsumme. Um diese Prüfsumme zu berechnen, benötigen wir ein Terminal einer Linux-Distribution. Es wird empfohlen, [TailOs](https://tails.boum.org/index.fr.html) zu verwenden, das eine bootfähige amnestische Distribution von einem USB-Stick aus ist. Geben Sie im Terminal den Befehl `echo <binäre Nummer> | shasum -a 254 -0` ein. Ersetzen Sie `<binäre Nummer>` durch Ihre Liste von 128 Nullen und Einsen. Die Ausgabe ist ein hexadezimaler Hash. Notieren Sie das erste Zeichen dieses Hashs und konvertieren Sie es in binär. Sie können diese [Tabelle](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) verwenden, um zu helfen. Fügen Sie die Prüfsumme in binärer Form (4 Ziffern) zur zwölften Zeile Ihres Blattes hinzu.

**Schritt 5 - Konvertierung in Dezimal:**
Um die Wörter, die jeder Ihrer Zeilen zugeordnet sind, zu finden, müssen Sie zunächst jede 11-Bit-Serie in Dezimalzahlen umwandeln. Hier können Sie keinen Online-Konverter verwenden, da diese Bits Ihre Mnemonik darstellen. Sie müssen also mit einem Taschenrechner und einem Trick konvertieren: Jedes Bit ist mit einer Potenz von 2 verbunden, so dass wir von links nach rechts 11 Ränge haben, die jeweils 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1 entsprechen. Um Ihre 11-Bit-Serie in Dezimalzahlen umzuwandeln, müssen Sie nur die Ränge addieren, die eine 1 enthalten. Zum Beispiel entspricht die Serie 00110111011 der folgenden Addition: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Sie können nun jede Zeile in Dezimalzahlen umwandeln. Bevor Sie jedoch mit der Codierung in Wörter beginnen, müssen Sie zu jeder Zeile +1 hinzufügen, da der Index der BIP39-Wortliste ab 1 und nicht ab 0 beginnt.

**Schritt 8 - Generierung der Mnemonik-Phrase:**
Beginnen Sie damit, die [Liste der 2048 Wörter](https://seedxor.com/files/wordlist.pdf) auszudrucken, um die Konvertierung zwischen Ihren Dezimalzahlen und den BIP39-Wörtern durchzuführen. Das Besondere an dieser Liste ist, dass kein Wort die ersten 4 Buchstaben mit allen anderen Wörtern in diesem Wörterbuch gemeinsam hat. Suchen Sie dann für jede Ihrer Zeilen das Wort, das der Dezimalzahl zugeordnet ist.

**Schritt 9 - Test der Mnemonik-Phrase:**
Testen Sie Ihre Mnemonik-Phrase sofort auf Sparrow Wallet, indem Sie eine Wallet daraus erstellen. Wenn Sie einen ungültigen Prüfsummenfehler erhalten, haben Sie wahrscheinlich einen Rechenfehler gemacht. Korrigieren Sie diesen Fehler, indem Sie zum Schritt 4 zurückkehren und testen Sie erneut auf Sparrow Wallet. Voilà! Sie haben gerade eine neue Bitcoin-Wallet aus 128 Würfelwürfen erstellt.

Die Generierung einer Mnemonik-Phrase ist ein wichtiger Prozess zur Sicherung Ihrer Kryptowährungs-Wallet. Es wird empfohlen, sicherere Methoden wie die Verwendung von Open-Source-Software oder Hardware-Wallets zu verwenden, um die Mnemonik-Phrase zu generieren. Durch die Durchführung dieses Workshops können Sie jedoch besser verstehen, wie wir aus einer zufälligen Zahl eine Bitcoin-Wallet erstellen können.

# Erstellung einer Bitcoin-Wallet

## Erstellung des Seeds und des Master-Schlüssels

![Erstellung des Seeds und des Master-Schlüssels](https://youtu.be/56yAt_JDWhY)

In diesem Teil des Kurses werden wir die Schritte zur Ableitung einer HD-Wallet (Hierarchical Deterministic Wallet) untersuchen, die die hierarchische Erstellung und Verwaltung von privaten und öffentlichen Schlüsseln ermöglicht.
Die Grundlage der HD-Wallet beruht auf zwei wesentlichen Elementen: der Mnemonik-Phrase und der Passphrase (optionales zusätzliches Passwort). Zusammen bilden sie den Seed, eine alphanumerische Sequenz von 512 Bits, die als Basis für die Ableitung der Wallet-Schlüssel dient. Aus diesem Seed können alle Bitcoin-Wallet-Schlüsselpaare abgeleitet werden. Der Seed ist der Schlüssel, um auf alle mit der Wallet verbundenen Bitcoins zuzugreifen, unabhängig davon, ob eine Passphrase verwendet wird oder nicht.

Um den Seed zu erhalten, wird die Funktion PBKDF2 (Password-Based Key Derivation Function 2) mit der Mnemonik-Phrase und der Passphrase verwendet. Die Ausgabe von PBKDF2 ist ein Seed von 512 Bits. Der Master-Private-Key und der Master-Chain-Code werden unter Verwendung des HMAC SHA-512-Algorithmus (Hash-based Message Authentication Code Secure Hash Algorithm 512) bestimmt. Dieser Algorithmus erfordert eine Nachricht und einen Schlüssel, um ein Ergebnis zu generieren. Der Master-Private-Key wird aus dem Seed und der Phrase "Bitcoin SEED" berechnet. Diese Phrase ist für alle HD-Wallet Ableitungen identisch, um eine Konsistenz zwischen den Wallets zu gewährleisten.

Ursprünglich war die SHA-512-Funktion nicht im Bitcoin-Protokoll implementiert, daher wird HMAC SHA-512 verwendet. Die Verwendung von HMAC SHA-512 mit der Phrase "Bitcoin SEED" zwingt den Benutzer, eine spezifische Bitcoin-Wallet zu generieren. Das Ergebnis von HMAC SHA-512 ist eine 512-Bit-Nummer, die in zwei Teile aufgeteilt ist: die linken 256 Bits repräsentieren den Master-Private-Key, während die rechten 256 Bits den Master-Chain-Code repräsentieren.

Der Master-Private-Key ist der Elternschlüssel aller zukünftigen Wallet-Schlüssel, während der Master-Chain-Code bei der Ableitung von Kinderschlüsseln eine Rolle spielt. Es ist wichtig zu beachten, dass es unmöglich ist, ein Schlüsselpaar abzuleiten, ohne den entsprechenden Chain-Code des Elternpaares zu kennen. Der Chain-Code fügt eine Entropiequelle in den Ableitungsprozess ein.

Ein Schlüsselpaar in der Wallet besteht aus einem privaten Schlüssel, einem öffentlichen Schlüssel und einem Chain-Code. Der Chain-Code ermöglicht es, eine zufällige Quelle in der Ableitung von Kinderschlüsseln einzuführen und jedes Schlüsselpaar zu isolieren, um Informationslecks zu vermeiden.

Es ist wichtig zu betonen, dass der Master-Private-Key der erste aus dem Seed abgeleitete private Schlüssel ist und keine Verbindung zu den erweiterten Wallet-Schlüsseln hat. Der Seed ist daher das grundlegende Element zur Ableitung aller Wallet-Schlüssel. Er unterscheidet sich von der Mnemonik-Phrase und der Passphrase, die zur Erstellung des Seeds verwendet werden.
Im nächsten Kurs werden wir uns ausführlich mit erweiterten Schlüsseln wie xPub, xPRV, zPub befassen und verstehen, warum sie verwendet werden und wie sie aufgebaut sind.

## Erweiterte Schlüssel

![Erweiterte Schlüssel](https://youtu.be/TRz760E_zUY)

In diesem Teil des Kurses werden wir uns mit erweiterten Schlüsseln (xPub, zPub, yPub) und ihren Präfixen befassen, die eine wichtige Rolle bei der Ableitung von Kinderschlüsseln in einer HD-Brieftasche (Hierarchical Deterministic Wallet) spielen.

Erweiterte Schlüssel unterscheiden sich von Master-Schlüsseln. Eine HD-Brieftasche generiert eine mnemonische Phrase und einen Seed, um den Master-Schlüssel und den Master-Chain-Code zu erhalten. Erweiterte Schlüssel werden verwendet, um Kinderschlüssel abzuleiten und erfordern sowohl den übergeordneten Schlüssel als auch den entsprechenden Chain-Code. Ein erweiterter Schlüssel kombiniert diese beiden Informationen, um den Ableitungsprozess zu vereinfachen.

Erweiterte Schlüssel werden durch spezifische Präfixe (XPRV, XPUB, YPUB, ZPUB) identifiziert, die anzeigen, ob es sich um einen erweiterten privaten oder öffentlichen Schlüssel handelt, sowie seinen spezifischen Zweck. Die Metadaten, die einem erweiterten Schlüssel zugeordnet sind, umfassen die Version (Präfix), die Tiefe, den öffentlichen Schlüsselabdruck, den Index und die Payload (Chain-Code und übergeordneter Schlüssel).

Die Payload besteht aus dem Chain-Code (32 Bytes) und dem übergeordneten Schlüssel (33 Bytes). Diese Elemente sind wesentlich für die Ableitung von Kinderschlüsseln. Ein privater Schlüssel wird aus einer zufälligen oder pseudozufälligen Zahl generiert, während ein öffentlicher Schlüssel mithilfe des ECDSA-Algorithmus (Elliptic Curve Digital Signature Algorithm) generiert wird.

Jedes Paar erweiterter Schlüssel ist mit einem eindeutigen Chain-Code verbunden, der spezifische Ableitungen ermöglicht. Durch Verknüpfung des übergeordneten Schlüssels mit dem Chain-Code wird ein erweiterter privater oder öffentlicher Schlüssel erhalten.

Erweiterte öffentliche Schlüssel können nur normale öffentliche Kinderschlüssel ableiten, während erweiterte private Schlüssel sowohl öffentliche als auch private Kinderschlüssel ableiten können, sowohl auf normaler als auch auf gehärteter Ableitung. Die Verwendung von erweiterten Schlüsseln mit dem Präfix XPUB ermöglicht die Ableitung neuer Adressen, ohne auf die entsprechenden privaten Schlüssel zurückgreifen zu müssen, was eine bessere Sicherheit bietet. Die Metadaten, die erweiterten Schlüsseln zugeordnet sind, liefern wichtige Informationen über ihre Rolle und Position in der Schlüsselhierarchie.
Die komprimierten öffentlichen Schlüssel haben eine Größe von 33 Bytes, während rohe öffentliche Schlüssel 512 Bits haben. Die komprimierten öffentlichen Schlüssel behalten die gleichen Informationen wie die rohen Schlüssel bei, jedoch mit reduzierter Größe. Die erweiterten Schlüssel haben eine Größe von 82 Bytes und ihr Präfix wird durch eine Umwandlung in Hexadezimalzahl in Base 58 dargestellt. Die Prüfsumme wird mithilfe der HASH256-Hashfunktion berechnet.

Verstärkte Ableitungen beginnen bei Indizes, die Potenzen von 2 (2^31) sind. Erweiterte öffentliche Schlüssel ermöglichen nur die Ableitung normaler Kinderschlüssel, während erweiterte private Schlüssel die Ableitung beliebiger Kinderschlüssel ermöglichen. Es ist interessant zu bemerken, dass die am häufigsten verwendeten Präfixe xpub und zpub sind, die den Legacy- und SegWit-v1- und SegWit-v0-Standards entsprechen.

In unserem nächsten Kurs werden wir uns mit der Ableitung von Kinderschlüsselpaaren unter Verwendung des Wissens über erweiterte Schlüssel und des Master-Schlüssels des Wallets befassen.

Zusammenfassend spielen erweiterte Schlüssel eine wesentliche Rolle in der Kryptographie und dem Betrieb von HD-Wallets. Das Verständnis ihrer Verwendung und Berechnung ist entscheidend für die Sicherheit von Transaktionen und den Schutz digitaler Vermögenswerte. Die mit erweiterten Schlüsseln verbundenen Präfixe und Metadaten ermöglichen eine effektive Verwendung und präzise Ableitung der erforderlichen Kinderschlüssel.

## Ableitung von Kinderschlüsselpaaren

![Ableitung von Kinderschlüsselpaaren](https://youtu.be/FXhI-GmE9Aw)

Als nächstes werden wir uns mit der Berechnung des Seeds und des Master-Schlüssels befassen, die die ersten wesentlichen Elemente für die Hierarchisierung und Ableitung des HD-Wallets (Hierarchical Deterministic Wallet) darstellen. Der Seed, der eine Länge von 128 bis 256 Bits hat, wird zufällig oder aus einem geheimen Satz generiert. Er spielt eine deterministische Rolle bei der Ableitung aller anderen Schlüssel. Der Master-Schlüssel ist der erste Schlüssel, der aus dem Seed abgeleitet wird, und er ermöglicht die Ableitung aller anderen Kinderschlüsselpaare.

Der Master-Chain-Code spielt eine wichtige Rolle bei der Wiederherstellung des Wallets aus dem Seed. Es ist zu beachten, dass alle aus demselben Seed abgeleiteten Schlüssel denselben Master-Chain-Code haben werden.

Die Hierarchisierung und Ableitung des HD-Wallets bieten eine effizientere Verwaltung von Schlüsseln und Wallet-Strukturen. Erweiterte Schlüssel ermöglichen die Ableitung eines Kinderschlüsselpaars aus einem Elternschlüsselpaar unter Verwendung spezifischer mathematischer Berechnungen und Algorithmen.
Es gibt verschiedene Arten von Kinderschlüsselpaaren, einschließlich verstärkter und normaler Schlüssel. Der erweiterte öffentliche Schlüssel ermöglicht nur die Ableitung normaler öffentlicher Kinderschlüssel, während der erweiterte private Schlüssel die Ableitung aller Kinderschlüssel ermöglicht, sowohl öffentlicher als auch privater, ob sie normal oder verstärkt sind. Jedes Schlüsselpaar hat einen Index, der sie voneinander unterscheidet.

Die Ableitung von Kinderschlüsseln verwendet die HMAC-SHA512-Funktion unter Verwendung des übergeordneten Schlüssels, der mit dem Index und dem Kettencode der Schlüsselpaarung konkateniert wird. Normale Kinderschlüssel haben einen Index zwischen 0 und 2 hoch 31 minus 1, während verstärkte Kinderschlüssel einen Index zwischen 2 hoch 31 und 2 hoch 32 minus 1 haben.

Es gibt zwei Arten von Kinderschlüsselpaaren: verstärkte und normale Paare. Der Prozess der Ableitung von Kinderschlüsseln verwendet öffentliche Schlüssel, um Ausgabenbedingungen zu generieren, während private Schlüssel zur Signatur verwendet werden. Der erweiterte öffentliche Schlüssel ermöglicht nur die Ableitung normaler öffentlicher Kinderschlüssel, während der erweiterte private Schlüssel die Ableitung aller Kinderschlüssel ermöglicht, sowohl öffentlicher als auch privater, ob sie normal oder verstärkt sind.

Die verstärkte Ableitung verwendet den übergeordneten privaten Schlüssel, während die normale Ableitung den übergeordneten öffentlichen Schlüssel verwendet. Die HMAC-SHA512-Funktion wird für die verstärkte Ableitung verwendet, während die normale Ableitung einen 512-Bit-Hash verwendet. Der öffentliche Kinderschlüssel wird erhalten, indem der private Kinderschlüssel mit dem Generator der elliptischen Kurve multipliziert wird.

Die Hierarchisierung und Ableitung vieler Schlüsselpaare auf deterministische Weise ermöglicht die Erstellung eines Stammbaumschemas für die hierarchische Ableitung. Im nächsten Kurs dieser Schulung werden wir uns die Struktur der HD-Brieftasche sowie die Ableitungspfade genauer ansehen und uns insbesondere auf die Notation der Ableitungspfade konzentrieren.

## Struktur der Brieftasche und Ableitungspfade

![Struktur der Brieftasche und Ableitungspfade](https://youtu.be/etO9UxwyE2I)

In diesem Kapitel werden wir uns die Struktur des Ableitungsbaums in einer HD-Brieftasche (Hierarchical Deterministic Wallet) ansehen. Wir haben bereits die Berechnung des Seeds, des Master-Schlüssels und die Ableitung von Kinderschlüsselpaaren untersucht. Jetzt werden wir uns auf die Organisation der Schlüssel innerhalb der Brieftasche konzentrieren.
Der HD-Wallet verwendet Tiefenschichten, um Schlüssel zu organisieren. Jede Ableitung von einem Elternpaar zu einem Kindpaar entspricht einer Tiefenschicht. Tiefenschicht 0 entspricht dem Master-Schlüssel und dem Master-Chain-Code.
Tiefenschicht 1 wird verwendet, um Kinderschlüssel gemäß einem bestimmten Ziel abzuleiten, das durch den Index bestimmt wird. Die Ziele entsprechen den Standards BIP 84 und Segwit v0/v1.

Tiefenschicht 2 ermöglicht die Unterscheidung von Konten verschiedener Kryptowährungen oder Netzwerke. Dies ermöglicht die Organisation des Wallets entsprechend den verschiedenen Quellen von Mitteln.

Tiefenschicht 3 wird verwendet, um das Wallet in verschiedene Konten zu organisieren und bietet so eine klarere und organisierte Struktur.

Tiefenschicht 4 entspricht den internen und externen Ketten, die für Adressen verwendet werden, die öffentlich kommuniziert werden sollen. Index 0 ist mit der externen Kette verbunden, während Index 1 mit der internen Kette verbunden ist. Jedes Konto hat zwei Ketten: die externe Kette (0) und die interne Kette (1). Tiefenschicht 4 wird auch verwendet, um Skripttypen bei Multi-Signatur-Wallets zu verwalten.

Tiefenschicht 5 wird für Empfangsadressen in einem klassischen Wallet verwendet. Im nächsten Abschnitt werden wir die Ableitung von Kinderschlüsselpaaren genauer untersuchen.

Für jede Tiefenschicht verwenden wir Indizes, um Kinderschlüsselpaare zu unterscheiden. Verstärkte Indizes werden für einige Ableitungen mit einem Apostroph verwendet. Der öffentliche Schlüssel pro Jahr wird als Eingabe für die HMAC-Funktion verwendet. Der Index in einem Ableitungspfad gibt den Wert an, der in der HMAC-Funktion verwendet wird.

Der Index ohne Apostroph entspricht dem tatsächlich verwendeten Index, während der Index mit Apostroph dem tatsächlichen Index + 2^31 entspricht. Verstärkte Ableitungen verwenden Indizes von 2^31 bis 2^32-1. Zum Beispiel entspricht der Index 44' dem tatsächlichen Index 2^31 + 44.

Um eine bestimmte Empfangsadresse zu generieren, leiten wir ein Kinderschlüsselpaar aus dem Master-Schlüssel und dem Master-Chain-Code ab. Dann verwenden wir den Index, um die verschiedenen Kinderschlüsselpaare derselben Tiefenschicht zu unterscheiden.

Erweiterte Schlüssel wie XPUB ermöglichen es, Ihr Wallet mit mehreren Personen zu teilen. Der Ableitungspfad wird verwendet, um die externe Kette (Adressen, die kommuniziert werden sollen) und die interne Kette (Wechseladressen) zu unterscheiden.
Es ist wichtig zu beachten, dass in einem HD-Portfolio verschiedene Tiefen je nach verschiedenen Standards verwendet werden. Die Ableitung von Elternschlüsseln zu Kinderschlüsseln ermöglicht den Übergang von einer Tiefe zur anderen. Die Verwendung verschiedener Zweige im HD-Portfolio ermöglicht die Angabe der verschiedenen Standards, die befolgt werden.

Im nächsten Kapitel werden wir uns mit Empfangsadressen, ihren Verwendungsvorteilen und den Schritten zu ihrer Konstruktion befassen.

# Was ist eine Bitcoin-Adresse?

## Bitcoin-Adressen

![Bitcoin-Adressen](https://youtu.be/nqGBMjPtFNI)

In diesem Kapitel werden wir die Empfangsadressen untersuchen, die eine entscheidende Rolle im Bitcoin-System spielen. Sie ermöglichen den Empfang von Geldern auf einer Münze und werden aus Paaren von privaten und öffentlichen Schlüsseln generiert. Obwohl es einen Skripttyp namens Pay2PublicKey gibt, der Bitcoins auf einem öffentlichen Schlüssel sperrt, bevorzugen Benutzer in der Regel die Verwendung von Empfangsadressen anstelle dieses Skripts.

Wenn ein Empfänger Bitcoins erhalten möchte, gibt er dem Sender eine Empfangsadresse anstelle seines öffentlichen Schlüssels. Eine Adresse ist tatsächlich ein Hash eines öffentlichen Schlüssels mit einem spezifischen Format. Der öffentliche Schlüssel wird aus dem Kind-Privatschlüssel abgeleitet, indem mathematische Operationen wie Addition und Verdopplung von Punkten auf elliptischen Kurven verwendet werden.

Es ist wichtig zu beachten, dass es nicht möglich ist, von der Adresse zum öffentlichen Schlüssel oder vom öffentlichen Schlüssel zum privaten Schlüssel zurückzukehren. Die Verwendung einer Adresse reduziert die Größe der öffentlichen Schlüsselinformation, die ursprünglich 512 Bits beträgt. Es ist möglich, einen öffentlichen Schlüssel zu komprimieren, indem nur der x-Wert beibehalten und ein Präfix hinzugefügt wird, aber diese Technik war zur Zeit der Entstehung von Bitcoin nicht bekannt. Die Verwendung einer Adresse ermöglicht daher keine Platzersparnis in den Blöcken.

Bitcoin-Adressen wurden in der Größe reduziert, um ihre Verwendung zu erleichtern. Sie haben eine Prüfsumme, die Tippfehler erkennt und das Risiko des Verlusts von Bitcoins reduziert. Öffentliche Schlüssel haben jedoch keine Prüfsumme, was bedeutet, dass Tippfehler zum Verlust der entsprechenden Mittel führen können.

Adressen bieten auch eine zweite Sicherheitsebene zwischen öffentlicher und privater Information, die es schwieriger macht, den privaten Schlüssel zu übernehmen. Die verwendeten Hash-Funktionen machen es den Schlüsselpaaren widerstandsfähig gegen mögliche Angriffe von Quantencomputern. Diese Computer können ECDSA (Elliptic Curve Digital Signature Algorithm) potenziell brechen, aber sie können keine Hash-Funktion brechen.
Es ist wichtig zu betonen, dass jede Adresse nur einmal verwendet werden kann, was zur Sicherheit und Vertraulichkeit beiträgt. Die Wiederverwendung derselben Adresse stellt ein ernsthaftes Vertraulichkeitsproblem dar und sollte vermieden werden. Darüber hinaus ist jede Adresse ein Hash eines öffentlichen Schlüssels, begleitet von einer Prüfsumme, um das Risiko des Verlusts von Bitcoins zu reduzieren.

Verschiedene Präfixe werden für Bitcoin-Adressen verwendet. Zum Beispiel entspricht BC1Q einer Segwit V0-Adresse, BC1P einer Taproot/Segwit V1-Adresse und die Präfixe 1 und 3 sind mit Pay2PublicKeyH/Pay2ScriptH-Adressen (legacy) verbunden. Im nächsten Kurs werden wir Schritt für Schritt die Ableitung einer Adresse aus einem öffentlichen Schlüssel erklären.

Zusammenfassend sind Empfangsadressen ein wesentlicher Bestandteil des Bitcoin-Systems. Sie werden aus Paaren von privaten und öffentlichen Schlüsseln generiert und dienen zum Empfangen von Geldern auf einer Münze. Adressen enthalten eine Prüfsumme, um das Risiko des Verlusts von Bitcoins zu reduzieren, und sind so konzipiert, dass sie einmalig verwendet werden, um Sicherheit und Vertraulichkeit zu gewährleisten. Verschiedene Arten von Adressen werden im Bitcoin-System verwendet, die eine erhöhte Vertraulichkeit und Sicherheit bieten.

## Wie man eine Bitcoin-Adresse erstellt

![Wie man eine Bitcoin-Adresse erstellt](https://youtu.be/ewMGTN8dKjI)

In diesem Kapitel werden wir die Erstellung einer Empfangsadresse für Bitcoin-Transaktionen behandeln. Eine Empfangsadresse ist eine alphanumerische Darstellung eines komprimierten öffentlichen Schlüssels. Die Umwandlung eines öffentlichen Schlüssels in eine Empfangsadresse erfolgt in mehreren Schritten.

Eine vorteilhafte Eigenschaft von Empfangsadressen ist das Vorhandensein einer Prüfsumme, die Fehlererkennung ermöglicht. Hierfür verwenden wir die BCH-Prüfsummentechnologie (Bose-Chaudhuri-Hocquenghem), die eine präzise Fehlererkennung gewährleistet. Diese Technologie trägt auch zur Reduzierung der Anzahl der erforderlichen Zeichen zur Darstellung einer Adresse bei, was ihre Verwendung erleichtert.

Um mit dem Bau einer Adresse zu beginnen, müssen wir den entsprechenden öffentlichen Schlüssel komprimieren. Ein roher öffentlicher Schlüssel benötigt 520 Bits, aber dank der Symmetrie der verwendeten elliptischen Kurve kann eine elliptische Kurve eine x-Abszisse haben, die mit zwei möglichen Werten für y verbunden ist: positiv oder negativ. Im Bitcoin-Netzwerk arbeiten wir mit einem Körper endlicher positiver ganzer Zahlen anstelle des Körpers der reellen Zahlen. Um einen öffentlichen Schlüssel aus x darzustellen, fügen wir einen Präfix hinzu, der den Wert von y angibt (gerade oder ungerade). Die Komprimierung eines öffentlichen Schlüssels reduziert seine Größe von 520 auf 264 Bits. Die Parität von y in einem Körper endlicher positiver ganzer Zahlen entspricht der Parität von y im Körper der reellen Zahlen.
Wir nehmen das Beispiel des öffentlichen Schlüssels von Satoshi Nakamoto mit einem Präfix von 0,3, was auf einen ungeraden Wert von y hinweist. Wir können dann zum zweiten Schritt des Aufbaus einer Adresse aus komprimierten öffentlichen Schlüsseln übergehen. Es ist möglich, zwei Adressen für jeden öffentlichen Schlüssel zu berechnen. Dazu verwenden wir die SHA256-Funktion, um den Hash des öffentlichen Schlüssels zu erhalten. Anschließend wenden wir die ripemd160-Funktion auf das Ergebnis von SHA256 an, um eine Zeichenfolge zu erhalten. Diese Zeichenfolge wird dann in Gruppen von 5 Bits kodiert, zu denen Metadaten hinzugefügt werden, um die Prüfsumme mit dem BCH-Programm zu berechnen.

Im Falle von Legacy-Adressen verwenden wir den doppelten SHA256-Hash, um die Prüfsumme der Adresse zu generieren. Für Segwit V0- und V1-Adressen verwenden wir jedoch die BCH-Checksum-Technologie, um Fehler zu erkennen. Das BCH-Programm ist in der Lage, Fehler mit einer extrem geringen Fehlerwahrscheinlichkeit vorzuschlagen und zu korrigieren. Derzeit wird das BCH-Programm verwendet, um Fehler zu erkennen und Änderungen vorzuschlagen, aber es führt sie nicht automatisch für den Benutzer durch. Die Berechnung der Prüfsumme mit dem BCH-Code basiert auf der Chien-Chauffage-Polynomarithmetik.

Das BCH-Programm erfordert mehrere Eingabeinformationen, einschließlich des HRP (Human Readable Part), der erweitert werden muss. Die Erweiterung des HRP besteht darin, jeden Buchstaben in Basis 2 zu kodieren, wobei die ersten drei Bits jedes Zeichens genommen werden, ein Trennzeichen 0 eingefügt wird und die letzten fünf Bits jedes Zeichens zusammengefügt werden. Die blauen Zeichen, die in Basis 10 konvertiert wurden, entsprechen 3 und 3 im Dezimalsystem, während die anderen fünf orangefarbenen Zeichen 2 und 3 in Basis 10 entsprechen. Die Erweiterung des HRP in Basis 10 isoliert die letzten fünf Bits jedes Zeichens und verstärkt somit die Prüfsumme.

Die Segwit V0-Version wird durch den Code 00 dargestellt und das "Payload" ist in Schwarz in Basis 10 angegeben. Dies wird von sechs Zeichen für die Prüfsumme begleitet. Die Eingabe mit den Metadaten wird dann dem BCH-Programm übergeben, um die Prüfsumme in Basis 10 zu erhalten. Die Verkettung der Version, des Payloads und der Prüfsumme ermöglicht den Aufbau der Adresse. Die Basis-10-Zeichen werden dann mithilfe einer Korrespondenztabelle in Bech32-Zeichen konvertiert. Das Bech32-Alphabet umfasst alle alphanumerischen Zeichen mit Ausnahme von 1, b, i und o, um Verwechslungen zu vermeiden.
Um eine Adresse zu erstellen, die mit bc1q beginnt, müssen wir eine Hash-Funktion (H160) auf einem komprimierten öffentlichen Schlüssel anwenden, dann die Prüfsumme, die Version (q), die HRP (bc) und den Trennzeichen (1) hinzufügen. Taproot-Adressen beginnen mit bc1p, da ihre Version (Segwit V1) 0+1=1 entspricht, daher wird der Buchstabe p verwendet. Alle diese Elemente werden dann in BCH32 konvertiert, einer Variante von Base 32, die spezifisch für Bitcoin ist.

So haben wir die Schritte zum Erstellen einer Empfangsadresse, die Verwendung der BCH-Prüfsummentechnologie sowie zum Erstellen einer Adresse, die mit bc1q oder bc1p beginnt, unter Verwendung der BCH32-Variante von Base 32 spezifisch für Bitcoin durchlaufen.

## Zusammenfassung der Kryptographie für Bitcoin-Wallets

![Zusammenfassung der Schulung](https://youtu.be/NkAYoVUMvOs)

Im Laufe dieser Schulung haben wir das hierarchische deterministische Wallet (HD) mit BIP32 eingehend untersucht. Die Entropie spielt bei dieser Art von Wallet eine zentrale Rolle, da sie verwendet wird, um aus einer zufälligen Zahl eine mnemonische Phrase zu generieren. Mit der Liste von 2048 Wörtern, die im BIP39 bereitgestellt wird, kann diese mnemonische Phrase in eine Reihe von leicht zu merkenden Wörtern codiert werden. Die mnemonische Phrase sowie eine mögliche Passphrase sind erforderlich, um den Wallet-Samen zu generieren. Die Passphrase fungiert als kryptographisches Salz, das eine zusätzliche Schutzschicht für das Wallet hinzufügt.

Die Funktion pbkdf2 wird verwendet, um den Seed aus der mnemonischen Phrase und der Passphrase zu generieren, wobei ein hmacha512 und 2048 Iterationen verwendet werden. Der Master Key und der Master Chain Code werden dann aus diesem Seed abgeleitet, indem die Funktion hmacha512 erneut mit dem Satz "bitcoin seed" verwendet wird. Der Master Private Key und der Master Chain Code sind die höchsten Elemente in der Hierarchie des HD-Wallets.
Die Ableitung eines Kindschlüssels hängt von mehreren Faktoren ab, einschließlich des Elternschlüssels und des entsprechenden Chaincodes. Ein erweiterter Schlüssel wird durch Verketten eines Elternschlüssels mit seinem Chaincode erhalten, während ein Master-Schlüssel ein separater Schlüssel ist. Um eine Adresse abzuleiten, wird zuerst der komprimierte öffentliche Schlüssel mit SHA256 und RIPMD160 gehasht und dann eine Prüfsumme berechnet. Für einen Standard-Legacy wird der doppelte SHA256-Hash verwendet, um die Prüfsumme zu berechnen, während das BCH-Programm (Bose-Chaudhuri-Hocquenghem) verwendet wird, um die Prüfsumme für einen SegWit-Standard zu berechnen. Anschließend wird eine Base-58-Darstellung für einen Legacy-Standard und das Bech32-Format für einen SegWit-Standard verwendet, um die HD-Wallet-Adresse zu erhalten.

Zusammenfassend haben wir die Hash-Funktionen und ihre Eigenschaften sowie digitale Signaturen und elliptische Kurven im Detail untersucht. Wir sind dann in die Welt der deterministischen hierarchischen Wallets (HD) mit BIP32 eingetaucht, wobei Entropie und Passphrase verwendet wurden, um den Wallet-Samen zu generieren. Wir haben auch gelernt, wie man Kinderschlüssel ableitet und die HD-Wallet-Adresse erhält. Ich hoffe, diese Informationen waren nützlich für Sie, und ich ermutige Sie jetzt, zur Bewertung zu gehen, um Ihr Wissen aus dem Crypto 301-Kurs zu testen. Vielen Dank für Ihre Aufmerksamkeit.

# Dankeschön und weiterhin den Kaninchenbau erkunden

Wir möchten uns herzlich bei Ihnen für die Teilnahme am Crypto 301-Kurs bedanken. Wir hoffen, dass diese Erfahrung für Sie bereichernd und lehrreich war. Wir haben viele spannende Themen behandelt, von Mathematik über Kryptographie bis hin zur Funktionsweise des Bitcoin-Protokolls.

Wenn Sie das Thema weiter vertiefen möchten, haben wir eine zusätzliche Ressource für Sie. Wir haben ein exklusives Interview mit Théo Pantamis und Loïc Morel, zwei renommierten Experten auf dem Gebiet der Kryptographie, durchgeführt. In diesem Interview werden verschiedene Aspekte des Themas vertieft und interessante Perspektiven geboten.

Schauen Sie sich das Interview an, um weiterhin den faszinierenden Bereich der Kryptographie zu erkunden. Wir hoffen, dass dies für Sie nützlich und inspirierend in Ihrem Weg sein wird. Nochmals vielen Dank für Ihre Teilnahme und Ihr Engagement während des Kurses.

## Interview mit Théo Pantamis

![Interview mit Théo Pantamis](https://youtu.be/c9MvtGJsEvY)

Hier ist eine Zusammenfassung des Interviews:

In diesem Interview teilt Théo Pantamys, der sich auf Mathematik spezialisiert hat und leidenschaftlich an Bitcoin, Lightning Network und Protokollen interessiert ist, seinen Werdegang und seine Gedanken zu verschiedenen Themen.
Théo entdeckte Bitcoin im Jahr 2009, aber sein Interesse entwickelte sich 2015-2016 dank wissenschaftlicher Vermittler auf YouTube weiter. Er konzentrierte sich auf die Mathematik und Kryptographie von Bitcoin sowie auf den Vergleich mit anderen Protokollen.

Er betont die Bedeutung der Dezentralisierung in Bitcoin und wie dies im Gegensatz zur Autorität des Staates steht, indem es eine Öffnung des Registers bietet. Bitcoin löst auch das Problem der Regulierung effektiv.

Théo spricht auch über das Thema Privatsphäre in Bitcoin. Er erklärt die Bedeutung von CoinJoin, um die Privatsphäre der Benutzer zu schützen und die Offenlegung persönlicher Informationen zu vermeiden. Er empfiehlt die Verwendung von Wasabi und Whirlpool, um die Anonymität von Transaktionen zu verbessern.

Dann diskutiert Théo RGB, ein komplexes Protokoll, das die technischen Probleme von Bitcoin löst. Er erklärt, wie RGB diskrete Verträge verwendet, um Tokens und Finanzprodukte zu erstellen, während der Zustand des Vertrags auf der Bitcoin-Blockchain validiert wird.

Die Diskussion setzt sich über die Bedrohung durch die Quanteninformatik für Bitcoin fort. Théo erwähnt, dass es etwa hundert Qubits braucht, um die meisten Algorithmen zu brechen, und dass Quantencomputer bisher noch nicht dieses Leistungsniveau erreicht haben.

Was die Prüfsumme der Bitcoin-Adressen betrifft, erklärt Théo, wie BCH-Codes verwendet werden, um Tippfehler zu erkennen und potenziell zu korrigieren. Er betont die Bedeutung der Prüfsumme, um den Verlust von Bitcoins zu vermeiden und die Größe der Adressen zu optimieren.

Abschließend teilt Théo Ressourcen, um das Verständnis von Bitcoin zu vertiefen, einschließlich YouTube-Kanälen für mathematische Vermittlung, empfohlenen Büchern und Twitter-Räumen, in denen Entwickler ihre Arbeit diskutieren.
