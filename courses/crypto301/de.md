---
name: Einführung in die Kryptographie
goal: Das Erstellen einer Bitcoin-Wallet aus kryptographischer Sicht verstehen
objectives:
  - Die Terminologie der mit Bitcoin verbundenen Kryptographie entmystifizieren.
  - Das Erstellen einer Bitcoin-Wallet beherrschen.
  - Die Struktur einer Bitcoin-Wallet verstehen.
  - Adressen und Ableitungspfade verstehen.
---

# Eine Reise ins Herz der Kryptographie

Sind Sie von Bitcoin fasziniert? Fragen Sie sich, wie eine Bitcoin-Wallet funktioniert? Machen Sie sich bereit für eine fesselnde Reise ins Herz der Kryptographie! Unser Experte Loïc wird Sie durch die Tiefen der Erstellung einer Bitcoin-Wallet führen und die Geheimnisse hinter einschüchternden technischen Begriffen wie Hashing, Schlüsselableitung und elliptischen Kurven enthüllen.

Dieses Training wird Ihnen nicht nur das Wissen vermitteln, um die Struktur einer Bitcoin-Wallet zu verstehen, sondern Sie auch darauf vorbereiten, tiefer in die faszinierende Welt der Kryptographie einzutauchen. Sind Sie bereit, diese Reise anzutreten? Schließen Sie sich uns an und verwandeln Sie Ihre Neugier in Kompetenz!

+++

# Einführung

## Einführung in die Kryptographie

### Ist dieses Training für Sie geeignet? JA!

Wir heißen Sie herzlich willkommen zu unserem neuen Training "Crypto 301: Einführung in die Kryptographie und HD-Wallets", geleitet von unserem Experten Loïc Morel. Dieser Kurs wird Sie in die faszinierende Welt der Kryptographie einführen, einer grundlegenden Disziplin der Mathematik, die die Verschlüsselung und Sicherheit Ihrer Daten gewährleistet.

In unserem täglichen Leben und insbesondere im Bereich der Bitcoins spielt Kryptographie eine entscheidende Rolle. Konzepte wie private und öffentliche Schlüssel, Adressen, Ableitungspfade, Seed und Entropie stehen im Mittelpunkt der Verwendung und Erstellung einer Bitcoin-Wallet. In diesem Kurs wird Ihnen Loïc ausführlich erklären, wie private Schlüssel erstellt werden und wie sie mit Adressen verknüpft sind. Loïc wird auch eine Stunde damit verbringen, Ihnen die mathematischen Details der elliptischen Kurve, dieser komplexen mathematischen Kurve, zu erklären. Darüber hinaus werden Sie verstehen, warum die Verwendung von HMAC SHA512 wichtig ist, um Ihre Wallet zu sichern, und was der Unterschied zwischen Seed und mnemonischer Phrase ist.
Das ultimative Ziel dieser Schulung ist es, Ihnen das technische Verständnis der Prozesse zur Erstellung einer HD-Wallet und der verwendeten kryptographischen Methoden zu ermöglichen. Im Laufe der Jahre haben sich Bitcoin-Wallets weiterentwickelt, um einfacher zu bedienen, sicherer und standardisierter zu sein, dank spezifischer BIPs. Loïc wird Ihnen helfen, diese BIPs zu verstehen, um die Entscheidungen der Bitcoin-Entwickler und Kryptographen zu verstehen. Wie alle Schulungen unserer Universität ist diese vollständig kostenlos und Open Source. Das bedeutet, dass Sie sie frei verwenden und nutzen können. Wir freuen uns darauf, Ihr Feedback am Ende dieses spannenden Kurses zu erhalten.

### Das Wort hat der Professor!

Hallo allerseits, ich bin Loïc Morel, Ihr Führer durch diese technische Erkundung der Kryptographie, die in Bitcoin-Wallets verwendet wird.

Unsere Reise beginnt mit einem Tauchgang in die Tiefen kryptographischer Hash-Funktionen. Gemeinsam werden wir die Mechanismen des unverzichtbaren SHA256 auseinandernehmen und verschiedene Algorithmen zur Ableitung erkunden.

Wir werden unser Abenteuer fortsetzen, indem wir die geheimnisvolle Welt der digitalen Signaturen entschlüsseln. Sie werden entdecken, wie die Magie elliptischer Kurven auf diese Signaturen angewendet wird, und wir werden erklären, wie der öffentliche Schlüssel aus dem privaten Schlüssel berechnet wird. Und natürlich werden wir uns mit dem Akt des Signierens mit dem privaten Schlüssel befassen.

Dann werden wir in die Vergangenheit zurückgehen, um die Entwicklung von Bitcoin-Wallets zu betrachten, und wir werden uns mit den Konzepten von Entropie und Zufallszahlen befassen. Wir werden die berühmte Mnemonik-Phrase überprüfen und dabei auch auf die Passphrase eingehen. Sie werden sogar die Möglichkeit haben, ein einzigartiges Erlebnis zu erleben, indem Sie einen Seed aus 128 Würfelwürfen erstellen!

Mit diesem soliden Fundament werden wir bereit sein für den entscheidenden Teil: die Erstellung einer Bitcoin-Wallet. Vom Erzeugen des Seeds und des Master-Schlüssels bis hin zur Untersuchung erweiterter Schlüssel werden wir jeden Schritt genau betrachten. Wir werden auch die Struktur der Wallets und die Ableitungspfade diskutieren.

Zum Abschluss werden wir unsere Reise beenden, indem wir uns Bitcoin-Adressen genauer ansehen. Wir werden erklären, wie sie erstellt werden und welche wichtige Rolle sie im Betrieb von Bitcoin-Wallets spielen.

Begleiten Sie mich auf dieser fesselnden Reise und machen Sie sich bereit, die Welt der Kryptographie wie nie zuvor zu erkunden. Lassen Sie Ihre Vorurteile hinter sich und öffnen Sie Ihren Geist für eine neue Art, Bitcoin und seine grundlegende Struktur zu verstehen.

# Hash-Funktionen

## Einführung in kryptographische Hash-Funktionen im Zusammenhang mit Bitcoin

Willkommen zu unserer heutigen Sitzung, die sich eingehend mit der kryptographischen Welt der Hash-Funktionen befasst, einem wesentlichen Baustein für die Sicherheit des Bitcoin-Protokolls. Stellen Sie sich eine Hash-Funktion als einen äußerst effizienten kryptographischen Entschlüsselungsroboter vor, der Informationen beliebiger Größe in einen eindeutigen und festen Fingerabdruck, genannt "Hash", umwandelt. Im Laufe unserer Erkundung werden wir das Profil kryptographischer Hash-Funktionen zeichnen, ihre Verwendung im Bitcoin-Protokoll hervorheben und die spezifischen Ziele definieren, die diese kryptographischen Funktionen erreichen müssen.

![image](assets/image/section1/0.JPG)

Das Zeichnen des Profils kryptographischer Hash-Funktionen erfordert das Verständnis zweier wesentlicher Eigenschaften: ihre Unumkehrbarkeit und ihre Fälschungssicherheit. Jede kryptographische Hash-Funktion ist wie ein einzigartiger Künstler, der für jede Eingabe einen eigenen "Hash" erzeugt. Selbst eine leicht abweichende Pinselstrich verändert das endgültige Bild erheblich, das heißt den Hash. Diese Funktionen wirken wie digitale Wächter, die die Integrität von heruntergeladener Software überprüfen. Eine weitere entscheidende Eigenschaft, die sie besitzen, ist ihre Kollisionsbeständigkeit. Kollisionen sind zwar im Bereich des Hashings unvermeidlich, aber eine ausgezeichnete kryptographische Hash-Funktion minimiert sie erheblich. Es ist, als ob jeder Hash ein Haus in einer riesigen Stadt wäre; trotz der enormen Anzahl von Häusern sorgt eine gute Hash-Funktion dafür, dass jedes Haus eine eindeutige Adresse hat.

![image](assets/image/section1/1.JPG)

Lassen Sie uns nun auf den stürmischen Gewässern veralteter Hash-Funktionen navigieren. SHA0, SHA1 und MD5 gelten heute als verrostete Schalen in der Welt des kryptographischen Hashings. Sie werden oft nicht empfohlen, da sie ihre Kollisionsbeständigkeit verloren haben. Das Schubladenprinzip erklärt, warum es trotz unserer besten Bemühungen unmöglich ist, Kollisionen zu vermeiden, aufgrund der Begrenzung der Ausgabegröße. Es ist auch wichtig zu beachten, dass die Beständigkeit gegenüber dem zweiten Bild nicht von der Kollisionsbeständigkeit abhängt. Um als wirklich sicher angesehen zu werden, muss eine Hash-Funktion Kollisionen, zweite Bilder und Ursprungsbilder widerstehen.
'Ein Schlüsselelement im Bitcoin-Protokoll ist die SHA-256-Hashfunktion, die Kapitän des Schiffs ist. Andere Funktionen wie SHA-512 werden für die Ableitung mit HMAC und PBKDF verwendet. Darüber hinaus wird RIPMD160 verwendet, um einen Hash auf 160 Bits zu reduzieren. Wenn wir von HASH256 und HASH160 sprechen, beziehen wir uns auf die Verwendung eines doppelten Hashes mit SHA-256 und RIPMD. Die Verwendung von HASH160 ist besonders vorteilhaft, da sie die Sicherheit von SHA-256 bietet und gleichzeitig die Größe des Hashes reduziert.

Zusammenfassend ist das ultimative Ziel einer kryptografischen Hashfunktion, Informationen beliebiger Größe in einen Hash fester Größe umzuwandeln. Um als sicher angesehen zu werden, muss sie mehrere Eigenschaften haben: Unumkehrbarkeit, Fälschungssicherheit, Kollisionsresistenz und Schutz vor zweitem Bild.

![image](assets/image/section1/2.JPG)

Nach dieser Erkundung haben wir kryptografische Hashfunktionen entmystifiziert, ihre Verwendung im Bitcoin-Protokoll aufgezeigt und ihre spezifischen Ziele untersucht. Wir haben gelernt, dass Hashfunktionen als sicher gelten müssen, wenn sie resistent gegen Pre-Image-Angriffe, zweite Bild-Angriffe, Kollisionen und Fälschungen sind. Wir haben auch die verschiedenen Hashfunktionen untersucht, die im Bitcoin-Protokoll verwendet werden. In unserer nächsten Sitzung werden wir uns in das Herzstück der SHA256-Hashfunktion vertiefen und die faszinierenden mathematischen Eigenschaften entdecken, die ihr ihre Einzigartigkeit verleihen.

## Die Mechanismen von SHA256

Willkommen zur Fortsetzung unserer faszinierenden Reise durch die kryptografischen Labyrinthe der Hashfunktion. Heute lüften wir das Geheimnis von SHA256, einem komplexen, aber genialen Prozess, den wir in unserer vorherigen Diskussion über Hashfunktionen eingeführt haben. Lassen Sie uns einen Schritt weiter in dieses Labyrinth gehen und mit der Vorverarbeitung von SHA256 beginnen. Stellen Sie sich die Vorverarbeitung wie die Zubereitung eines köstlichen Gerichts vor, bei dem wir "Füllbits" hinzufügen, um die Größe unserer Hauptzutat, der Eingabe, auf ein perfektes Vielfaches von 512 Bits zu bringen. All dies mit dem ultimativen Ziel, einen köstlichen 256-Bit-Hash aus einer Zutat unterschiedlicher Größe zu generieren.

![image](assets/image/section1/3.JPG)
![image](assets/image/section1/4.JPG)

Dans diesem kryptographischen Rezept spielen wir mit Bits, die eine anfängliche Nachrichtengröße haben, die wir M nennen. Ein Bit ist für den Trenner reserviert, während P Bits für die Polsterung verwendet werden. Darüber hinaus reservieren wir 64 Bits für die zweite Vorverarbeitungsphase. Das Ganze muss ein Vielfaches von 512 Bits sein. Ähnlich wie bei der Gewährleistung, dass alle Zutaten perfekt in unser Gericht passen.

![image](assets/image/section1/5.JPG)

Jetzt gehen wir zur zweiten Phase der Vorverarbeitung über, die das Hinzufügen der binären Darstellung der anfänglichen Nachrichtengröße in Bits beinhaltet. Dafür verwenden wir unsere 64 reservierten Bits aus dem vorherigen Schritt. Wir fügen Nullen hinzu, um unsere 64 Bits auf unsere ausgeglichene Eingabe abzurunden. Dann mischen wir die anfängliche Nachricht, die Bit-Polsterung und die Größenpolsterung wie Zutaten in einem Mixer, um unsere ausgeglichene Eingabe zu erhalten.

![image](assets/image/section1/6.JPG)

Jetzt bereiten wir uns auf die ersten Schritte der SHA-256-Funktion vor. Wie in jedem guten Rezept benötigen wir einige Grundzutaten, die wir Konstanten und Initialisierungsvektoren nennen. Die Initialisierungsvektoren von A bis H sind die ersten 32 Bits der Dezimalteile der Quadratwurzeln der ersten 8 Primzahlen. Die Konstanten K von 0 bis 63 repräsentieren die ersten 32 Bits der Dezimalteile der Kubikwurzeln der ersten 64 Primzahlen.

![image](assets/image/section1/7.JPG)

In der Kompressionsfunktion verwenden wir spezifische Operatoren wie XOR, AND und NOT. Wir verarbeiten die Bits einzeln nach ihrer Rangfolge, indem wir den XOR-Operator und eine Wahrheitstabelle verwenden. Der AND-Operator wird verwendet, um nur dann 1 zurückzugeben, wenn beide Operanden gleich 1 sind, und der NOT-Operator gibt den entgegengesetzten Wert eines Operanden zurück. Wir verwenden auch die SHR-Operation, um die Bits nach rechts um eine bestimmte Anzahl zu verschieben.

![image](assets/image/section1/8.JPG)
![image](assets/image/section1/9.JPG)

Schließlich, nachdem wir die ausgeglichene Eingabe in verschiedene 512-Bit-Nachrichtenblöcke aufgeteilt haben, führen wir 64 Berechnungsrunden in der Kompressionsfunktion durch. Ähnlich wie bei einem Radrennen verbessert jede Runde unsere Position. Wir addieren modulo 2^32 den Zwischenzustand zum anfänglichen Zustand der Kompressionsfunktion. Die Additionen in der Kompressionsfunktion sind Additionen modulo 2^32, um die Größe der Summen auf 32 Bits zu begrenzen.

![image](assets/image/section1/10.JPG)
![image](assets/image/section1/11.JPG)
![image](assets/image/section1/12.JPG)
![image](assets/image/section1/13.JPG)

Um es zusammenzufassen, möchten wir die entscheidende Rolle der Berechnungen in den Boxen CH, MAJ, σ0 und σ1 betonen. Diese Operationen sind unter anderem die Wächter, die die Robustheit der SHA256-Hashfunktion gegen Angriffe gewährleisten und sie zu einer bevorzugten Wahl für die Sicherung vieler digitaler Systeme machen, insbesondere im Bitcoin-Protokoll. Es ist daher offensichtlich, dass die Schönheit von SHA256, obwohl komplex, in ihrer Fähigkeit liegt, den Eingang aus dem Hash wiederherzustellen, während die Überprüfung des Hashes für eine gegebene Eingabe eine mechanisch einfache Aktion ist.

## Die für die Ableitung verwendeten Algorithmen

Die HMAC- und PBKDF2-Ableitungsalgorithmen sind Schlüsselkomponenten in der Sicherheitsmechanik des Bitcoin-Protokolls. Sie schützen vor verschiedenen potenziellen Angriffen und gewährleisten die Integrität von Bitcoin-Wallets.

HMAC und PBKDF2 sind kryptografische Werkzeuge, die in Bitcoin für verschiedene Aufgaben verwendet werden. HMAC wird hauptsächlich eingesetzt, um Längenerweiterungsangriffe bei der Ableitung von hierarchisch deterministischen (HD) Wallets zu verhindern, während PBKDF2 verwendet wird, um eine mnemonische Phrase in einen Seed umzuwandeln.

![image](assets/image/section1/14.JPG)

HMAC nimmt eine Nachricht und einen Schlüssel als Eingabe und generiert eine Ausgabe fester Größe. Um die Einheitlichkeit zu gewährleisten, wird der Schlüssel entsprechend der Blockgröße der Hashfunktion angepasst. Bei der Ableitung von HD-Wallets wird HMAC-SHA-512 verwendet. Letzteres arbeitet mit 1024-Bit-Blöcken (128 Bytes) und passt den Schlüssel entsprechend an. Es verwendet die Konstanten OPAD (0x5c) und IPAD (0x36), die so oft wiederholt werden, wie nötig, um die Sicherheit zu erhöhen.

Der HMAC-SHA-512-Prozess beinhaltet die Konkatenation des Ergebnisses von SHA-512, das auf den Schlüssel XOR OPAD und den Schlüssel XOR IPAD angewendet wird, mit der Nachricht. Bei Verwendung von 1024-Bit-Blöcken (128 Bytes) wird der Eingangsschlüssel bei Bedarf mit Nullen aufgefüllt und dann mit IPAD und OPAD XOR-verknüpft. Der modifizierte Schlüssel wird anschließend mit der Nachricht konkateniert.

![image](assets/image/section1/15.JPG)

Die Verwendung eines Salts in der Kettencodierung erhöht die Sicherheit der abgeleiteten Schlüssel. Ohne ihn könnte ein Angriff die gesamte Wallet kompromittieren und alle Bitcoins stehlen.
PBKDF2 wird verwendet, um eine mnemonische Phrase in einen Seed umzuwandeln. Dieser Algorithmus führt 2048 Durchläufe unter Verwendung von HMAC SHA512 durch. Durch diese Ableitungsalgorithmen können zwei verschiedene Eingaben zu einer eindeutigen und festen Ausgabe führen, was das Problem möglicher Angriffe auf die Längenerweiterung bei SHA-2-Funktionen behebt. Ein Angriff auf die Längenerweiterung nutzt eine spezifische Eigenschaft einiger kryptographischer Hashfunktionen aus. Bei einem solchen Angriff kann ein Angreifer, der bereits den Hash eines unbekannten Nachrichten besitzt, diesen verwenden, um den Hash einer längeren Nachricht zu berechnen, die eine Erweiterung der ursprünglichen Nachricht ist. Dies ist oft möglich, ohne den Inhalt der ursprünglichen Nachricht zu kennen, was zu erheblichen Sicherheitslücken führen kann, wenn eine solche Hashfunktion für Aufgaben wie die Integritätsprüfung verwendet wird.

![image](assets/image/section1/16.JPG)

Zusammenfassend spielen die HMAC- und PBKDF2-Algorithmen eine wesentliche Rolle bei der Sicherheit der Ableitung von HD-Wallets im Bitcoin-Protokoll. HMAC-SHA-512 wird verwendet, um Angriffe auf die Längenerweiterung zu verhindern, während PBKDF2 die Umwandlung der mnemonischen Phrase in einen Seed ermöglicht. Der Chain-Code fügt der Schlüsselableitung eine zusätzliche Entropiequelle hinzu und gewährleistet so die Robustheit des Systems.

# Digitale Signaturen

## Digitale Signaturen und elliptische Kurven

In der Welt der Kryptowährungen ist die Sicherheit von Transaktionen von größter Bedeutung. Im Herzen des Bitcoin-Protokolls findet man den Einsatz digitaler Signaturen, die als mathematischer Beweis für den Besitz eines privaten Schlüssels dienen, der mit einem bestimmten öffentlichen Schlüssel verbunden ist. Diese Methode zum Schutz von Daten basiert im Wesentlichen auf einem faszinierenden Bereich der Kryptographie, der als elliptische Kurvenkryptographie (ECC) bezeichnet wird.

![image](assets/image/section2/0.JPG)

Die elliptische Kurvenkryptographie ist das Rückgrat der Sicherheit von Bitcoin-Transaktionen. Diese elliptischen Kurven, die an mathematische Kurven erinnern, die wir in der Schule studiert haben, sind in einer Vielzahl kryptographischer Anwendungen nützlich, von Schlüsselaustausch bis hin zur asymmetrischen Verschlüsselung und Erstellung digitaler Signaturen. Ein interessantes Detail, das elliptische Kurven auszeichnet, ist ihre Symmetrie: Jede nicht-vertikale Linie, die zwei Punkte der Kurve schneidet, wird einen dritten Punkt schneiden.

Jetzt gehen wir etwas tiefer: Das Bitcoin-Protokoll verwendet eine spezielle elliptische Kurve namens SecP256K1 für seine kryptographischen Operationen. Diese Kurve, definiert über eine endliche Menge von positiven Ganzzahlen modulo einer 256-Bit-Primzahl, kann als Punktwolke anstelle einer traditionellen Kurve visualisiert werden. Diese einzigartige Gestaltung ermöglicht es Bitcoin, seine Transaktionen effektiv abzusichern.

![image](assets/image/section2/1.JPG)

Was die Wahl der Kurve secp256k1 für Bitcoin betrifft, ist es interessant zu beachten, dass sie der Kurve secp256r1 vorgezogen wurde. Diese Kurve wird durch die Parameter a=0 und b=7 definiert, und ihre Gleichung lautet y² = x³ + 7 modulo n, wobei n die Primzahl ist, die die Ordnung der Kurve bestimmt.

Wenn von den Konstanten im Bitcoin-System die Rede ist, bezieht man sich in der Regel auf die spezifischen Parameter des Elliptic Curve Digital Signature Algorithm (ECDSA) und des elliptischen Kurvensystems, das von Bitcoin verwendet wird, nämlich die Kurve secp256k1. Hier sind diese Parameter:

- Primfeld (p): Bitcoin verwendet eine Kurve über einem Primfeld, daher ist p die erste Zahl, die zur Definition dieses Feldes verwendet wird. Für die Kurve secp256k1 gilt p = `p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F` im Hexadezimalformat oder p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 -1 im Dezimalformat.
- Kurvenordnung (n): Dies ist die Anzahl der Punkte auf der Kurve, einschließlich des Punktes im Unendlichen. Für secp256k1 gilt n = `n = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141` im Hexadezimalformat oder n = 2^256 - 432420386565659656852420866394968145599 im Dezimalformat.
- Generierungspunkt (G): Der Basispunkt oder Generator ist der Punkt auf der Kurve, von dem aus alle anderen öffentlichen Schlüssel generiert werden. Er hat spezifische x- und y-Koordinaten, die normalerweise im Hexadezimalformat dargestellt werden. Für secp256k1 sind die Koordinaten von G im Hexadezimalformat:
  - `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
  - `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

![image](assets/image/section2/2.JPG)

Beachten Sie, dass alle hexadezimalen Werte in der Regel in Basis 16 dargestellt werden, während dezimale Werte in Basis 10 sind. Darüber hinaus werden alle Operationen mit diesen Konstanten modulo p für die Koordinaten von Punkten auf der Kurve und modulo n für Schlüssel- und Signaturoperationen durchgeführt.
Also, wo werden diese berühmten Bitcoins gespeichert? Nicht in einer Bitcoin-Brieftasche, wie man denken könnte. Tatsächlich speichert eine Bitcoin-Brieftasche die privaten Schlüssel, die zum Nachweis des Besitzes der Bitcoins erforderlich sind. Die Bitcoins selbst werden in der Blockchain, einer dezentralen Datenbank, die alle Transaktionen archiviert, aufgezeichnet.

In dem Bitcoin-System ist die Recheneinheit der Bitcoin (beachten Sie das kleine "b"). Diese ist bis zu acht Dezimalstellen teilbar, wobei die kleinste Einheit der Satoshi ist. UTXO, oder "Unspent Transaction Output", repräsentieren die ungenutzten Transaktionsausgaben eines Benutzers. Um diese Bitcoins auszugeben, muss der Besitz des privaten Schlüssels nachgewiesen werden, der mit dem öffentlichen Schlüssel verbunden ist, der jedem UTXO zugeordnet ist.

Um die Sicherheit der Transaktionen zu gewährleisten, verwendet Bitcoin zwei digitale Signaturprotokolle: ECDSA (Elliptic Curve Digital Signature Algorithm) und Schnorr. ECDSA ist ein Signaturprotokoll, das seit dem Start von Bitcoin im Jahr 2009 integriert ist, während Schnorr-Signaturen erst kürzlich im November 2021 hinzugefügt wurden. Obwohl beide Protokolle auf elliptischer Kurvenkryptographie basieren und ähnliche mathematische Mechanismen verwenden, unterscheiden sie sich hauptsächlich in Bezug auf die Struktur der Signatur.

Bevor wir uns tiefer mit diesen Signaturmechanismen befassen, ist es wichtig, zu verstehen, was eine elliptische Kurve ist. Eine elliptische Kurve wird durch die Gleichung y² = x³ + ax + b definiert. Jeder Punkt auf dieser Kurve hat eine charakteristische Symmetrie, die der Schlüssel zu ihrer Verwendung in der Kryptographie ist.

Letztendlich werden verschiedene elliptische Kurven als sicher für kryptographische Zwecke anerkannt. Die bekannteste ist vielleicht die Kurve secp256r1. Für Bitcoin hat Satoshi Nakamoto jedoch eine andere Kurve gewählt: secp256k1.

Im nächsten Abschnitt dieses Kurses werden wir uns genauer mit dem öffentlichen Schlüssel und dem privaten Schlüssel befassen, um ein tiefes Verständnis für die Kryptographie auf elliptischen Kurven und den digitalen Signaturalgorithmus zu erlangen. Dies wird der Moment sein, um Ihr Wissen zu festigen und zu verstehen, wie all diese Informationen zusammenpassen, um die Sicherheit des Bitcoin-Protokolls zu gewährleisten.

## Berechnen des öffentlichen Schlüssels aus dem privaten Schlüssel

Dans diesem Kurs werden wir uns mit den Mechanismen der öffentlichen und privaten Schlüssel befassen, die zwei entscheidende Elemente des Bitcoin-Protokolls sind. Diese Schlüssel sind intrinsisch durch den Algorithmus Elliptic Curve Digital Signature Algorithm (ECDSA) verbunden. Ihr Verständnis wird uns einen tiefen Einblick in die Art und Weise geben, wie Bitcoin Transaktionen auf seiner Plattform sichert.

![image](assets/image/section2/3.JPG)
![image](assets/image/section2/4.JPG)

Um anzufangen, tauchen wir in die Welt des ECDSA-Algorithmus ein. Bitcoin nutzt diesen digitalen Signaturalgorithmus, um private und öffentliche Schlüssel zu verbinden. In diesem System ist der private Schlüssel eine zufällige oder pseudozufällige 256-Bit-Zahl. Die Gesamtzahl der Möglichkeiten für einen privaten Schlüssel beträgt theoretisch 2^256, aber in der Realität ist sie etwas geringer. Um genau zu sein, sind einige 256-Bit private Schlüssel für Bitcoin ungültig.

![image](assets/image/section2/5.JPG)

Um mit Bitcoin kompatibel zu sein, muss ein privater Schlüssel zwischen 1 und n-1 liegen, wobei n die Ordnung der elliptischen Kurve darstellt. Das bedeutet, dass die Gesamtzahl der Möglichkeiten für einen Bitcoin-Privatschlüssel fast gleich 1,158 x 10^77 ist. Um das in Perspektive zu setzen, ist das ungefähr die gleiche Anzahl von Atomen im beobachtbaren Universum. Der einzigartige private Schlüssel wird dann verwendet, um einen 512-Bit öffentlichen Schlüssel zu bestimmen.

![image](assets/image/section2/6.JPG)

Der öffentliche Schlüssel, als K bezeichnet, ist ein Punkt auf der elliptischen Kurve, der aus dem privaten Schlüssel unter Verwendung von Punktoperationen auf der Kurve abgeleitet wird. Es ist wichtig zu beachten, dass die ECDSA-Funktion nicht umkehrbar ist, dh es ist unmöglich, den privaten Schlüssel aus dem öffentlichen Schlüssel zurückzuerhalten. Diese Unumkehrbarkeit ist der Eckpfeiler der Sicherheit der Bitcoin-Wallet.

Der öffentliche Schlüssel besteht aus zwei 256-Bit-Punkten, insgesamt 512-Bit. Er kann jedoch auf eine 264-Bit-Zahl komprimiert werden. Der Punkt G ist der Ausgangspunkt für die Berechnung aller öffentlichen Schlüssel der Benutzer im System.

![image](assets/image/section2/7.JPG)

Eine bemerkenswerte Eigenschaft elliptischer Kurven ist, dass eine Gerade, die die Kurve an zwei Punkten schneidet, auch einen dritten Punkt schneiden wird, der als Punkt O bezeichnet wird. Diese Eigenschaft wird verwendet, um den Punkt U zu bestimmen, der das Gegenteil von Punkt O ist. Das Hinzufügen eines Punktes zu sich selbst erfolgt durch das Zeichnen einer Tangente an der Kurve an diesem Punkt, was einen neuen eindeutigen Punkt namens j ergibt. Das Skalarprodukt eines Punktes mit n bedeutet, diesen Punkt n-mal zu sich selbst hinzuzufügen.

![image](assets/image/section2/8.JPG)

Diese Operationen auf den Punkten einer elliptischen Kurve bilden die Grundlage für die Berechnung öffentlicher Schlüssel. Wenn der private Schlüssel bekannt ist, ist es einfach, den öffentlichen Schlüssel zu berechnen. Das Wissen über den öffentlichen Schlüssel ermöglicht jedoch nicht die Berechnung des privaten Schlüssels, was die Sicherheit des Bitcoin-Systems gewährleistet. Tatsächlich beruht die Sicherheit der öffentlichen und privaten Schlüssel auf dem Problem des diskreten Logarithmus, einer komplexen mathematischen Fragestellung.

![image](assets/image/section2/9.JPG)

In unserem nächsten Kurs werden wir erkunden, wie eine digitale Signatur mithilfe des ECDSA-Algorithmus mit einem privaten Schlüssel zum Entsperren von Bitcoins erstellt wird. Bleiben Sie gespannt auf diese aufregende Erkundung der Welt der Kryptowährungen und Kryptographie.

## Signieren mit dem privaten Schlüssel

Der Prozess der digitalen Signatur ist eine Schlüsselmethode, um zu beweisen, dass Sie im Besitz eines privaten Schlüssels sind, ohne ihn offenlegen zu müssen. Dies wird mithilfe des ECDSA-Algorithmus erreicht, der die Bestimmung einer eindeutigen Nonce, die Berechnung einer spezifischen Zahl V und die Erstellung einer digitalen Signatur aus zwei Teilen, S1 und S2, umfasst. Es ist entscheidend, immer eine eindeutige Nonce zu verwenden, um Sicherheitsangriffe zu vermeiden. Ein bekanntes Beispiel dafür, was passieren kann, wenn diese Regel nicht beachtet wird, ist der Fall des Hacks der PlayStation 3, der aufgrund der Wiederverwendung der Nonce kompromittiert wurde.

Um eine digitale Signatur mithilfe des ECDSA-Algorithmus (Elliptic Curve Digital Signature Algorithm) zu validieren, sind in der Regel die folgenden Schritte erforderlich:

1. Überprüfen Sie, ob die Werte der Signatur, S1 und S2, im Bereich [1, n-1] liegen. Ist dies nicht der Fall, ist die Signatur ungültig.
2. Berechnen Sie das Inverse von S2 mod n. Wir nennen dies u. Es wird oft wie folgt berechnet: u = (S2)^-1 mod n.
3. Berechnen Sie H, den Hash-Wert der signierten Nachricht.
4. Berechnen Sie u1 = H _ u mod n und u2 = S1 _ u mod n.
5. Berechnen Sie den Punkt P auf der elliptischen Kurve unter Verwendung von u1, u2 und dem öffentlichen Schlüssel K: P = u1*G + u2*K, wobei G der Generierungspunkt der Kurve ist.
6. Ist P der unendliche Punkt, ist die Signatur ungültig.
7. Berechnen Sie I = x-Koordinate von P mod n.
8. Die Signatur ist gültig, wenn I gleich S1 ist.

![image](assets/image/section2/10.JPG)
![image](assets/image/section2/11.JPG)

Es ist wichtig zu beachten, dass jede Software unterschiedliche Notationen verwenden kann und einige Schritte kombiniert oder umgestellt werden können, die Grundlogik ist jedoch dieselbe. Beachten Sie auch, dass alle arithmetischen Operationen in dem endlichen Körper ausgeführt werden, der durch die elliptische Kurve definiert ist (mod n, wobei n die Ordnung der Kurve ist). Zur Erinnerung: Die Kurve secp256k1 (die in Bitcoin verwendet wird) n = 2^256 - 432420386565659656852420866394968145599.
Bei der Generierung von öffentlichen und privaten Schlüsseln ist es entscheidend, sich mit der elliptischen Kurve und dem Generatorpunkt vertraut zu machen. Um einen öffentlichen Schlüssel zu erhalten, muss eine Zufallszahl als privater Schlüssel gewählt werden, die oft als `Anzeige` bezeichnet wird und in die Gleichung der elliptischen Kurve eingesetzt wird.

Die elliptische Kurve ist ein mächtiges Werkzeug, um sichere öffentliche und private Schlüssel zu erzeugen. Um beispielsweise den öffentlichen Schlüssel 3G zu erhalten, zeichnen Sie eine Tangente an den Punkt G, berechnen das Gegenteil von -G, um 2G zu erhalten, und addieren dann G und 2G. Um eine Transaktion durchzuführen, müssen Sie beweisen, dass Sie die Zahl 3 kennen, indem Sie die mit dem öffentlichen Schlüssel 3G verbundenen Bitcoins entsperren.

Um eine digitale Signatur zu erstellen und zu beweisen, dass Sie den privaten Schlüssel kennen, der mit dem öffentlichen Schlüssel 3G verknüpft ist, berechnen Sie zunächst eine Nonce und dann den Punkt V, der mit dieser Nonce verknüpft ist (im gegebenen Beispiel ist es 4G). Dann berechnen Sie den T-Punkt, indem Sie den öffentlichen Schlüssel 3G und den V-Punkt addieren, was 7G ergibt.

![image](assets/image/section2/12.JPG)

Die Überprüfung einer digitalen Signatur ist ein entscheidender Schritt bei der Verwendung des ECDSA-Algorithmus, mit dem die Echtheit einer signierten Nachricht bestätigt werden kann, ohne dass der private Schlüssel des Absenders benötigt wird. Im Einzelnen läuft dies folgendermaßen ab:

In unserem Beispiel haben wir zwei wichtige Werte: T und V. T ist ein numerischer Wert (in diesem Beispiel 7), und V ist ein Punkt auf der elliptischen Kurve (hier durch 4G dargestellt). Diese Werte werden bei der Erstellung der digitalen Signatur erzeugt und dann mit der Nachricht gesendet, um die Überprüfung zu ermöglichen.

Wenn der Verifizierer die Nachricht erhält, wird er auch diese beiden Werte, T und V, erhalten.

Hier sind die Schritte, die der Überprüfer durchführen wird, um die Signatur zu validieren:

1. Er wird zunächst den Hash der Nachricht berechnen, den wir H nennen werden.
2. Danach wird er u1 und u2 berechnen. Dazu wird er die folgenden Formeln verwenden:
   - u1 = H /\* (S2)^-1 mod n
   - u2 = T /\* (S2)^-1 mod n'.
     'Dabei ist S2 der zweite Teil der digitalen Signatur, n ist die Ordnung der elliptischen Kurve und (S2)^-1 ist der Kehrwert von S2 mod n.3. Der Prüfer berechnet dann einen Punkt P' auf der elliptischen Kurve mithilfe der Formel: P' = u1 _ G + u2 _ K.
   - G ist der Punkt, an dem die Kurve erzeugt wurde.
   - K ist der öffentliche Schlüssel des Absenders.
3. Der Prüfer berechnet dann I', was einfach die x-Koordinate des Punktes P' modulo n ist.
4. Schließlich bestätigt der Verifizierer, dass I' gleich T ist. Wenn dies der Fall ist, wird die Signatur als gültig betrachtet. Ist dies nicht der Fall, ist die Signatur ungültig.

Dieses Verfahren stellt sicher, dass nur der Absender, der den entsprechenden privaten Schlüssel besitzt, eine Signatur erzeugt haben könnte, die diesen Überprüfungsprozess durchläuft.

Zusammenfassend lässt sich sagen, dass die Überprüfung einer digitalen ECDSA-Signatur ein wesentliches Verfahren bei Bitcoin-Transaktionen ist. Sie stellt sicher, dass die signierte Nachricht während der Übertragung nicht manipuliert wurde und dass der Absender der Inhaber des privaten Schlüssels ist. Diese digitale Authentifizierungstechnik beruht auf komplexen mathematischen Prinzipien, insbesondere der Ellipsenkurvenarithmetik, und wahrt gleichzeitig die Vertraulichkeit des privaten Schlüssels. Sie bietet eine solide Sicherheitsgrundlage für kryptografische Transaktionen.

Davon abgesehen ist die Verwaltung dieser Schlüssel sowie ihre Erzeugung ein weiteres zentrales Thema in Bitcoin. Wie generiert man ein neues Schlüsselpaar? Wie kann man eine Vielzahl von Schlüsseln sicher und effizient organisieren? Wie können sie bei Bedarf abgerufen werden?

Um diese Fragen zu beantworten und Ihr Verständnis für die Sicherheit von Kryptographie zu vertiefen, wird sich unsere nächste Unterrichtsstunde auf das Konzept der Hierarchischen Deterministischen Brieftasche (HD wallets) und die Verwendung von mnemonischen Phrasen konzentrieren. Diese Mechanismen bieten elegante Möglichkeiten, Ihre Kryptowährungsschlüssel effizient zu verwalten und gleichzeitig die Sicherheit und Wiederherstellbarkeit zu erhöhen.

# Der mnemonische Satz

## Entwicklung der Bitcoin-Wallets

Der Hierarchische Deterministische Wallet, oder auch HD Wallet genannt, spielt eine wichtige Rolle im Kryptowährungs-Ökosystem. Der Begriff "Wallet" kann für Neulinge in diesem Bereich irreführend sein, da er nicht das Halten von Geld oder Währungen impliziert. Stattdessen bezieht er sich auf eine Sammlung von kryptographischen privaten Schlüsseln, die aus einem einzigen Mutter-Schlüssel abgeleitet werden, mithilfe eines cleveren algorithmischen arithmetischen Verfahrens. Diese privaten Schlüssel, die eine feste Länge von 256 Bits haben, sind das Wesentliche für den Besitz von Kryptowährungen und werden manchmal etwas grob als "Just a Bunch Of Keys" (JBOC) bezeichnet.

![image](assets/image/section3/0.JPG)

Die Komplexität der Verwaltung dieser Schlüssel wird jedoch durch eine Reihe von Protokollen, namens Bitcoin Improvement Proposals (BIP), ausgeglichen. Diese Upgrade-Vorschläge sind das Herzstück der Funktionalität und Sicherheit von HD Wallets. Zum Beispiel hat das [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), das 2012 eingeführt wurde, die Art und Weise, wie diese Schlüssel generiert und gespeichert werden, revolutioniert, indem es das Konzept der deterministischen und hierarchischen Schlüsselableitung eingeführt hat. Dadurch wird der Sicherungsprozess dieser Schlüssel erheblich vereinfacht, während ihr Sicherheitsniveau erhalten bleibt.

![image](assets/image/section3/1.JPG)

Anschließend hat das [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) eine bemerkenswerte Innovation eingeführt: die 24-Wort-Mnemonic-Phrase. Dieses System hat es ermöglicht, eine komplexe und schwer zu merkende Zahlenfolge in eine Reihe gewöhnlicher Wörter umzuwandeln, die viel einfacher zu merken und zu speichern sind. Darüber hinaus hat das [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) vorgeschlagen, eine zusätzliche Passphrase hinzuzufügen, um die Sicherheit der einzelnen Schlüssel zu erhöhen. Diese aufeinanderfolgenden Verbesserungen haben zu den Standards BIP43 und BIP44 geführt, die die Struktur und Hierarchie von HD Wallets standardisiert haben und diese Wallets für die breite Öffentlichkeit zugänglicher und benutzerfreundlicher gemacht haben.

In den folgenden Abschnitten werden wir tiefer in die Funktionsweise von HD Wallets eintauchen. Wir werden die Prinzipien der Schlüsselableitung behandeln und die grundlegenden Konzepte von Entropie und Zufallszahlengenerierung untersuchen, die für die Sicherheit Ihres HD Wallets unerlässlich sind.
Um es zusammenzufassen, ist es wichtig, die zentrale Rolle von BIP32 und BIP39 bei der Gestaltung und Sicherung von HD-Wallets hervorzuheben. Diese Protokolle ermöglichen die Generierung einer Vielzahl von Schlüsseln aus einem einzigen Seed, der als zufällige oder pseudozufällige Zahl betrachtet wird. Heutzutage werden diese Standards von den meisten Kryptowährungs-Wallets übernommen, egal ob sie für eine einzelne Kryptowährung oder für mehrere Währungstypen geeignet sind.

Ich hoffe, diese Einführung hat Ihnen geholfen, die Grundlagen des HD-Wallets und seine verschiedenen Eigenschaften besser zu verstehen. Unser Ziel ist es, Ihnen zu helfen, diese wesentlichen Konzepte zu beherrschen und effizienter in der komplexen Welt der Kryptowährungen zu navigieren. Also bleiben Sie bei uns, während wir in den kommenden Lektionen die Feinheiten und Nuancen dieser faszinierenden Welt weiter erkunden.

## Entropie und Zufallszahl

Die Bedeutung der Sicherheit privater Schlüssel im Bitcoin-Ökosystem ist unbestreitbar. Sie sind tatsächlich der Grundstein für die Sicherheit von Bitcoin-Transaktionen. Um jegliche Vorhersagbarkeit zu vermeiden, müssen diese Schlüssel wirklich zufällig generiert werden, was für den Benutzer schnell zu einer mühsamen Aufgabe werden kann. Eine Lösung für dieses Rätsel ist das Hierarchische Deterministische Wallet oder HD-Wallet. Diese Methode ermöglicht die deterministische und hierarchische Generierung von Kinderschlüsselpaaren aus einer einzigen Information am Anfang des Wallets. Hier kommt die Zufälligkeit ins Spiel, um die Sicherheit der abgeleiteten Schlüssel zu gewährleisten.

![image](assets/image/section3/2.JPG)

Die Generierung von Zufallszahlen ist tatsächlich ein entscheidendes Element in der Kryptographie, um die Integrität privater Schlüssel zu gewährleisten. Um jegliche Vorhersagbarkeit zu vermeiden, muss ein privater Schlüssel zufällig erzeugt werden. Die Verwendung eines neuen Schlüsselpaars für jede Transaktion erhöht die Sicherheit weiter, obwohl dies die Sicherung erschwert und die Vertraulichkeit nur teilweise gewährleistet. Zusammenfassend ist die Sicherheit privater Schlüssel eine absolute Priorität, die eine sorgfältige und zufällige Generierung erfordert. HD-Wallets bieten eine Lösung, um die Generierung und Verwaltung von Schlüsseln zu erleichtern und gleichzeitig ein hohes Sicherheitsniveau zu gewährleisten.

Jedoch stellt die Generierung von Zufallszahlen auf Computern eine große Herausforderung dar, da die erzielten Ergebnisse nicht wirklich zufällig sind. Deshalb ist es wichtig, einen Zufallszahlengenerator (RNG) zu verwenden. Die Arten von RNG variieren von Pseudo-Zufallszahlengeneratoren (PRNG) über echte Zufallszahlengeneratoren (TRNG) bis hin zu PRNGs, die eine Entropiequelle integrieren.

![image](assets/image/section3/3.JPG)

Im Fall von Bitcoin werden die privaten Schlüssel aus einer einzigen Information generiert, die der Basis der Brieftasche zugrunde liegt. Diese Information ermöglicht eine deterministische und hierarchische Ableitung von Kinderschlüsselpaaren. Die Entropie ist das Fundament jeder HD-Brieftasche, obwohl es keinen Standard für die Generierung dieser Zufallszahl gibt. Daher ist die Generierung von Zufallszahlen ein wichtiges Anliegen zur Sicherung von Bitcoin-Transaktionen.

Die Überprüfungsphase der Schlüsselgenerierung ist entscheidend, um die Sicherheit und Authentizität der Zufallszahlengenerierung zu gewährleisten, ein grundlegender Schritt, um jegliche Vorhersagbarkeit zu verhindern. Es wird daher dringend empfohlen, Open-Source-Brieftaschen zu verwenden, um diese Überprüfung zu ermöglichen.

Es ist jedoch wichtig zu beachten, dass einige Hardware-Brieftaschen "Closed Source" sein können, was die Überprüfung der Zufallszahlengenerierung unmöglich macht. Eine mögliche Umgehung wäre die Generierung einer mnemonischen Phrase mit Würfeln, obwohl dieser Ansatz gewisse Risiken mit sich bringen kann.

![image](assets/image/section3/4.JPG)

Die Verwendung einer zufällig generierten Passphrase kann dazu beitragen, diese Risiken zu mindern.

Ein Beispiel für die Anwendung dieser Methode ist die "Dice Roll" Option von CoinKit zur Generierung von mnemonischen Phrasen. Eine andere Möglichkeit wäre die Verwendung einer sehr großen anfänglichen Information und deren Reduzierung auf 256 Bits mit der SHA-256 Hash-Funktion, die in der Lage ist, eine gute Zufallszahl zu generieren. Es ist wichtig zu erwähnen, dass die SHA-256 Hash-Funktion kollisionsresistent, fälschungssicher und resistent gegen Pre-Image- und Second-Pre-Image-Angriffe ist.

Letztendlich spielt Zufall eine zentrale Rolle in der Kryptographie und Informatik, und die Fähigkeit, Zufall auf sichere Weise zu generieren, ist entscheidend für die Sicherheit von privaten Schlüsseln und Bitcoin-Transaktionen. Die Entropie, die das Herzstück der Bitcoin HD-Brieftasche ist, ist für ihre Sicherheit unerlässlich. In unserer nächsten Lektion werden wir dieses Thema weiter erkunden und genauer darauf eingehen, wie die Entropie zur Sicherheit von HD-Brieftaschen beiträgt.

## Die mnemonische Phrase

Die Sicherheit einer Bitcoin-Wallet ist eine Hauptanliegen für alle Benutzer. Eine wesentliche Methode zur Sicherung der Wallet besteht darin, eine mnemonische Phrase basierend auf Entropie und Prüfsumme zu generieren.

![image](assets/image/section3/5.JPG)

Die Entropie ist das Fundament der Sicherheit einer HD-Wallet. Es gibt verschiedene Methoden, um diese Entropie zu generieren, einschließlich der Verwendung von Pseudozufallszahlengeneratoren (PRNG), echten Zufallszahlengeneratoren (TRNG) oder manueller Eingabe. Es ist entscheidend, dass diese Entropie zufällig oder pseudozufällig ist, um die Sicherheit der Wallet zu gewährleisten.

![image](assets/image/section3/6.JPG)

Die Prüfsumme dient zur Überprüfung der Richtigkeit der Wiederherstellungsphrase. Ohne diese Prüfsumme könnte ein Fehler in der Phrase zur Erstellung einer anderen Wallet führen und somit zum Verlust der Gelder. Die Prüfsumme wird erreicht, indem die Entropie durch die SHA256-Funktion geleitet wird und die ersten 8 Bits des Hashes extrahiert werden.

Es gibt verschiedene Standards für die mnemonische Phrase, abhängig von der Größe der Entropie. Der am häufigsten verwendete Standard für eine 24-Wort-Wiederherstellungsphrase ist eine Entropie von 256 Bits. Die Größe der Prüfsumme wird durch die Teilung der Entropiegröße durch 32 bestimmt.

Zum Beispiel erzeugt eine Entropie von 256 Bits eine Prüfsumme von 8 Bits. Die Konkatenation von Entropie und Prüfsumme führt dann zu den jeweiligen Größen von 128 Bits, 160 Bits usw. Abhängig von der Entropiegröße besteht die Wiederherstellungsphrase aus 12 Wörtern für 128 Bits, 15 Wörtern für 160 Bits und 24 Wörtern für 256 Bits.

![image](assets/image/section3/7.JPG)

Um die Bits in Wörter umzuwandeln, wird jedem Segment ein Wort aus einer Liste von 2048 Wörtern zugeordnet. Es ist wichtig zu beachten, dass kein Wort die ersten vier Buchstaben in derselben Reihenfolge enthält.

Es ist entscheidend, die 24-Wort-Wiederherstellungsphrase zur Sicherung der Bitcoin-Wallet zu speichern. Die beiden am häufigsten verwendeten Standards basieren auf einer Entropie von 128 oder 256 Bits und einer Konkatenation von 12 oder 24 Wörtern. Das Hinzufügen einer Passphrase ist eine zusätzliche Option, um die Sicherheit der Wallet zu stärken.

Zusammenfassend ist die Generierung einer mnemonischen Phrase zur Sicherung einer Bitcoin-Wallet ein entscheidender Prozess. Es ist wichtig, die Standards der mnemonischen Phrase entsprechend der Entropiegröße einzuhalten. Die Sicherung der 24-Wort-Wiederherstellungsphrase ist entscheidend, um einen Verlust von Geldern zu verhindern. Vielen Dank für Ihre Aufmerksamkeit und wir freuen uns auf unseren nächsten Kurs über Kryptowährungen.

## Die Passphrase

Die Passphrase ist ein zusätzliches Kennwort, das in eine Bitcoin-Wallet integriert werden kann, um die Sicherheit zu erhöhen. Die Verwendung ist optional und liegt im Ermessen des Benutzers. Durch Hinzufügen beliebiger Informationen, die zusammen mit der mnemonischen Phrase verwendet werden, um den Wallet-Samen zu berechnen, erhöht die Passphrase die Sicherheit des Wallets.

![image](assets/image/section3/8.JPG)

Um die Schlüssel einer HD-Wallet abzuleiten, sind sowohl die mnemonische Phrase als auch die Passphrase erforderlich. Die Passphrase ist frei wählbar und kann nahezu unendlich lang sein. Sie ist nicht in der mnemonischen Phrase enthalten, die standardisiert ist und bestimmten Größen-, Prüfsummen- und Codierungsbeschränkungen unterliegen muss. Ein Angreifer kann nicht auf die Bitcoins eines Benutzers zugreifen, ohne die Passphrase zu kennen. Diese spielt eine Rolle bei der Konstruktion und Berechnung aller Wallet-Schlüssel.

Die Funktion pbkdf2 wird verwendet, um den Seed aus der Passphrase zu generieren. Dieser Seed ermöglicht die Ableitung aller Kinderschlüsselpaare der Wallet. Wenn die Passphrase geändert wird, wird die Bitcoin-Wallet vollständig verändert.

Die Passphrase ist ein wesentliches Werkzeug zur Stärkung der Sicherheit von Bitcoin-Wallets. Sie ermöglicht die Anwendung verschiedener Sicherheitsstrategien. Zum Beispiel kann sie verwendet werden, um Duplikate zu erstellen und das Backup der mnemonischen Phrase zu erleichtern. Sie kann auch die Sicherheit der Wallet verbessern, indem sie die mit der zufälligen Generierung der mnemonischen Phrase verbundenen Risiken verringert.

Eine effektive Passphrase sollte lang (20 bis 40 Zeichen) und vielfältig sein (Großbuchstaben, Kleinbuchstaben, Zahlen und Symbole verwenden). Sie sollte nicht direkt mit dem Benutzer oder seiner Umgebung verbunden sein. Es ist sicherer, eine zufällige Zeichenfolge anstelle eines einfachen Wortes als Passphrase zu verwenden.

![image](assets/image/section3/9.JPG)

Eine Passphrase ist sicherer als ein einfaches Kennwort. Die ideale Passphrase ist lang, vielfältig und zufällig. Sie kann die Sicherheit einer Wallet oder einer Hot-Software stärken. Sie kann auch zur Erstellung redundanter und sicherer Backups verwendet werden.

Es ist entscheidend, die Backups der Passphrase sorgfältig aufzubewahren, um den Zugriff auf die Wallet nicht zu verlieren. Eine Passphrase ist eine Option für eine HD-Wallet. Sie kann zufällig mit Würfeln oder einem anderen Pseudozufallszahlengenerator generiert werden. Es wird nicht empfohlen, eine Passphrase oder mnemonische Phrase auswendig zu lernen.

In unserem nächsten Kurs werden wir uns ausführlich mit der Funktionsweise des Seeds und dem ersten generierten Schlüsselpaar befassen. Zögern Sie nicht, diesen Kurs fortzusetzen, um Ihr Wissen zu vertiefen. Wir freuen uns darauf, Sie bald wiederzusehen.

# Erstellung von Bitcoin-Wallets

## Erstellung des Seeds und des Master-Schlüssels

In diesem Teil des Kurses werden wir die Schritte zur Ableitung einer HD-Brieftasche (Hierarchical Deterministic Wallet) erkunden, die es ermöglicht, private und öffentliche Schlüssel hierarchisch zu erstellen und zu verwalten.

![image](assets/image/section4/0.JPG)

Das Fundament der HD-Brieftasche basiert auf zwei wesentlichen Elementen: dem mnemonischen Satz und der Passphrase (optionales zusätzliches Kennwort). Zusammen bilden sie den Seed, eine alphanumerische Sequenz von 512 Bits, die als Grundlage für die Ableitung der Brieftaschenschlüssel dient. Aus diesem Seed können alle Kinderschlüsselpaare der Bitcoin-Brieftasche abgeleitet werden. Der Seed ist der Schlüssel, um auf alle mit der Brieftasche verbundenen Bitcoins zuzugreifen, unabhängig davon, ob Sie eine Passphrase verwenden oder nicht.

Um den Seed zu erhalten, wird die Funktion pbkdf2 (Password-Based Key Derivation Function 2) mit dem mnemonischen Satz und der Passphrase verwendet. Die Ausgabe von pbkdf2 ist ein 512-Bit-Seed. Der Master-Private-Key und der Master-Chain-Code werden unter Verwendung des HMAC SHA-512-Algorithmus (Hash-based Message Authentication Code Secure Hash Algorithm 512) bestimmt. Dieser Algorithmus erfordert eine Nachricht und einen Schlüssel, um ein Ergebnis zu generieren. Der Master-Private-Key wird aus dem Seed und dem Satz "Bitcoin SEED" berechnet. Dieser Satz ist für alle Ableitungen von HD-Brieftaschen identisch und gewährleistet so eine Konsistenz zwischen den Brieftaschen.

![image](assets/image/section4/1.JPG)

Ursprünglich war die SHA-512-Funktion nicht im Bitcoin-Protokoll implementiert, daher wird HMAC SHA-512 verwendet. Die Verwendung von HMAC SHA-512 mit dem Satz "Bitcoin SEED" zwingt den Benutzer, eine spezifische Bitcoin-Brieftasche zu generieren. Das Ergebnis von HMAC SHA-512 ist eine 512-Bit-Zahl, die in zwei Teile aufgeteilt ist: die linken 256 Bits repräsentieren den Master-Private-Key, während die rechten 256 Bits den Master-Chain-Code repräsentieren.

Der Master-Private-Key ist der übergeordnete Schlüssel für alle zukünftigen Schlüssel der Brieftasche, während der Master-Chain-Code bei der Ableitung der Kinderschlüssel eine Rolle spielt. Es ist wichtig zu beachten, dass es unmöglich ist, ein Kinderschlüsselpaar abzuleiten, ohne den entsprechenden Chain-Code des übergeordneten Paares zu kennen. Der Chain-Code fügt dem Ableitungsprozess eine Entropiequelle hinzu.

Ein Schlüsselpaar in der Brieftasche besteht aus einem privaten Schlüssel, einem öffentlichen Schlüssel und einem Chain-Code. Der Chain-Code ermöglicht es, eine Zufallsquelle in die Ableitung der Kinderschlüssel einzuführen und jedes Schlüsselpaar zu isolieren, um Informationslecks zu vermeiden.

![image](assets/image/section4/2.JPG)

Es ist wichtig zu betonen, dass der Master-Private-Key der erste aus dem Seed abgeleitete Private Key ist und keine Verbindung zu den erweiterten Wallet-Keys hat. Der Seed ist daher das grundlegende Element zur Ableitung aller Wallet-Keys. Er unterscheidet sich von der mnemonischen Phrase und der Passphrase, die zur Erstellung des Seeds verwendet werden.

Im nächsten Kurs werden wir im Detail erweiterte Keys wie xPub, xPRV, zPub erkunden und verstehen, warum sie verwendet werden und wie sie aufgebaut sind.

## Erweiterte Keys

In diesem Teil des Kurses werden wir erweiterte Keys (xPub, zPub, yPub) und ihre Präfixe untersuchen, die eine wichtige Rolle bei der Ableitung von Child-Keys in einer HD-Wallet (Hierarchical Deterministic Wallet) spielen.

![image](assets/image/section4/3.JPG)

Erweiterte Keys unterscheiden sich von Master-Keys. Eine HD-Wallet generiert eine mnemonische Phrase und einen Seed, um den Master-Private-Key und den Master-Chain-Code zu erhalten. Erweiterte Keys werden verwendet, um Child-Keys abzuleiten und erfordern sowohl den Parent-Key als auch den entsprechenden Chain-Code. Ein erweiterter Key kombiniert diese beiden Informationen, um den Ableitungsprozess zu vereinfachen.

Erweiterte Keys werden durch spezifische Präfixe (XPRV, XPUB, YPUB, ZPUB) identifiziert, die anzeigen, ob es sich um einen erweiterten privaten oder öffentlichen Key handelt, sowie seinen spezifischen Zweck. Die Metadaten, die mit einem erweiterten Key verbunden sind, umfassen die Version (Präfix), die Tiefe, den öffentlichen Schlüsselabdruck, den Index und die Payload (Chain-Code und Parent-Key).

![image](assets/image/section4/4.JPG)

Die Payload besteht aus dem Chain-Code (32 Bytes) und dem Parent-Key (33 Bytes). Diese Elemente sind entscheidend für die Ableitung von Child-Keys. Ein privater Key wird aus einer zufälligen oder pseudo-zufälligen Zahl generiert, während ein öffentlicher Key mit dem ECDSA-Algorithmus (Elliptic Curve Digital Signature Algorithm) generiert wird.

Jedes Paar erweiterter Keys ist mit einem eindeutigen Chain-Code verbunden, der spezifische Ableitungen ermöglicht. Durch Verknüpfung des Parent-Keys mit dem Chain-Code erhält man einen erweiterten privaten oder öffentlichen Key.

![image](assets/image/section4/5.JPG)

Die erweiterten öffentlichen Schlüssel können nur von normalen öffentlichen Kinderschlüsseln abgeleitet werden, während erweiterte private Schlüssel von sowohl öffentlichen als auch privaten Kinderschlüsseln abgeleitet werden können, sei es in einer normalen oder gehärteten Ableitung. Die Verwendung von erweiterten Schlüsseln mit dem Präfix XPUB ermöglicht die Ableitung neuer Adressen, ohne auf die entsprechenden privaten Schlüssel zurückgreifen zu müssen, was eine bessere Sicherheit bietet. Die Metadaten, die mit den erweiterten Schlüsseln verbunden sind, liefern wichtige Informationen über ihre Rolle und Position in der Schlüsselhierarchie.
Komprimierte öffentliche Schlüssel haben eine Größe von 33 Bytes, während rohe öffentliche Schlüssel 512 Bits haben. Komprimierte öffentliche Schlüssel enthalten die gleichen Informationen wie rohe Schlüssel, jedoch in einer kleineren Größe. Erweiterte Schlüssel haben eine Größe von 82 Bytes und ihr Präfix wird in Base58 dargestellt, indem es in Hexadezimal umgewandelt wird. Die Prüfsumme wird mit der HASH256-Hashfunktion berechnet.

![image](assets/image/section4/6.JPG)

Die gehärteten Ableitungen beginnen bei Indizes, die Potenzen von 2 (2^31) sind. Erweiterte öffentliche Schlüssel können nur von normalen öffentlichen Kinderschlüsseln abgeleitet werden, während erweiterte private Schlüssel beliebige Kinderschlüssel ableiten können. Es ist interessant festzustellen, dass die am häufigsten verwendeten Präfixe xpub und zpub sind, die den Legacy-Standard und SegWit v1 bzw. SegWit v0 entsprechen.

In unserem nächsten Kurs werden wir uns mit der Ableitung von Kinderschlüsselpaaren unter Verwendung des erworbenen Wissens über erweiterte Schlüssel und den Master-Schlüssel des Wallets befassen.

Zusammenfassend spielen erweiterte Schlüssel eine wesentliche Rolle in der Kryptographie und im Betrieb von HD-Wallets. Das Verständnis ihrer Verwendung und Berechnung ist entscheidend, um die Sicherheit von Transaktionen und den Schutz digitaler Vermögenswerte zu gewährleisten. Die mit erweiterten Schlüsseln verbundenen Präfixe und Metadaten ermöglichen eine effiziente Nutzung und genaue Ableitung der erforderlichen Kinderschlüssel.

## Ableitung von Kinderschlüsselpaaren

Nun werden wir uns mit der Berechnung des Seeds und des Master-Schlüssels befassen, die die ersten wesentlichen Elemente für die Hierarchisierung und Ableitung des HD-Wallets (Hierarchical Deterministic Wallet) darstellen. Der Seed, der eine Länge von 128 bis 256 Bits hat, wird entweder zufällig generiert oder aus einem geheimen Satz abgeleitet. Er spielt eine deterministische Rolle bei der Ableitung aller anderen Schlüssel. Der Master-Schlüssel ist der erste Schlüssel, der aus dem Seed abgeleitet wird, und er ermöglicht die Ableitung aller anderen Kinderschlüsselpaare.

Der Master-Chain-Code spielt eine wichtige Rolle bei der Wiederherstellung der Wallet aus dem Seed. Es ist zu beachten, dass alle aus demselben Seed abgeleiteten Schlüssel denselben Master-Chain-Code haben.

![image](assets/image/section4/7.JPG)

Die Hierarchisierung und Ableitung der HD-Wallet bieten eine effizientere Verwaltung von Schlüsseln und Wallet-Strukturen. Erweiterte Schlüssel ermöglichen die Ableitung eines Kindschlüsselpaars aus einem Elternschlüsselpaar unter Verwendung mathematischer Berechnungen und spezifischer Algorithmen.

Es gibt verschiedene Arten von Kindschlüsselpaaren, einschließlich verstärkter Schlüssel und normaler Schlüssel. Der erweiterte öffentliche Schlüssel ermöglicht nur die Ableitung normaler Kinderschlüssel, während der erweiterte private Schlüssel die Ableitung aller Kinderschlüssel ermöglicht, sowohl öffentlicher als auch privater, ob im normalen oder verstärkten Modus. Jedes Schlüsselpaar hat einen Index, der sie voneinander unterscheidet.

![image](assets/image/section4/8.JPG)

Die Ableitung der Kinderschlüssel verwendet die HMAC-SHA512-Funktion unter Verwendung des Elternschlüssels, der mit dem Index und dem Chain-Code des Schlüsselpaars verknüpft ist. Normale Kinderschlüssel haben einen Index von 0 bis 2 hoch 31 minus 1, während verstärkte Kinderschlüssel einen Index von 2 hoch 31 bis 2 hoch 32 minus 1 haben.

![image](assets/image/section4/9.JPG)
![image](assets/image/section4/10.JPG)

Es gibt zwei Arten von Kinderschlüsselpaaren: verstärkte Paare und normale Paare. Der Prozess der Ableitung der Kinderschlüssel verwendet die öffentlichen Schlüssel, um die Ausgabekonditionen zu generieren, während die privaten Schlüssel zur Signatur verwendet werden. Der erweiterte öffentliche Schlüssel ermöglicht nur die Ableitung normaler Kinderschlüssel, während der erweiterte private Schlüssel die Ableitung aller Kinderschlüssel ermöglicht, sowohl öffentlicher als auch privater, im normalen oder verstärkten Modus.

![image](assets/image/section4/11.JPG)
![image](assets/image/section4/12.JPG)

Die verstärkte Ableitung verwendet den Eltern-privaten Schlüssel, während die normale Ableitung den Eltern-öffentlichen Schlüssel verwendet. Die HMAC-SHA512-Funktion wird für die verstärkte Ableitung verwendet, während die normale Ableitung einen 512-Bit-Hash verwendet. Der Kind-öffentliche Schlüssel wird erhalten, indem der Kind-private Schlüssel mit dem Generator der elliptischen Kurve multipliziert wird.

![image](assets/image/section4/13.JPG)
![image](assets/image/section4/14.JPG)

## Struktur der Wallet und Ableitungspfade

In diesem Kapitel werden wir uns die Struktur des Ableitungsbaums in einer HD-Wallet (Hierarchical Deterministic Wallet) ansehen. Wir haben bereits die Berechnung des Seeds, des Master Keys und die Ableitung der Kinderschlüsselpaare untersucht. Jetzt werden wir uns auf die Organisation der Schlüssel innerhalb der Wallet konzentrieren.

Die HD-Wallet verwendet Tiefenebenen, um die Schlüssel zu organisieren. Jede Ableitung von einem Elternpaar zu einem Kindpaar entspricht einer Tiefenebene. Die Tiefenebene 0 entspricht dem Master Key und dem Master Chain Code.

![image](assets/image/section4/15.JPG)

- Tiefenebene 1 wird verwendet, um Kinderschlüssel gemäß einem bestimmten Ziel abzuleiten, das durch den Index bestimmt wird. Die Ziele entsprechen den Standards BIP 84 und Segwit v0/v1.

- Tiefenebene 2 ermöglicht die Unterscheidung von Konten für verschiedene Kryptowährungen oder Netzwerke. Dadurch kann die Wallet entsprechend den verschiedenen Geldquellen organisiert werden.

- Tiefenebene 3 wird verwendet, um die Wallet in verschiedene Konten zu organisieren und so eine klarere und organisierte Struktur zu bieten.

- Tiefenebene 4 entspricht den internen und externen Chains, die für Adressen verwendet werden, die öffentlich kommuniziert werden sollen. Index 0 ist mit der externen Chain verbunden, während Index 1 mit der internen Chain verbunden ist. Jedes Konto hat zwei Chains: die externe Chain (0) und die interne Chain (1). Tiefenebene 4 wird auch verwendet, um Skripttypen in Fällen von Multi-Signature-Wallets zu verwalten.

- Tiefenebene 5 wird für Empfangsadressen in einer herkömmlichen Wallet verwendet. Im nächsten Abschnitt werden wir die Ableitung der Kinderschlüsselpaare genauer betrachten.

![image](assets/image/section4/16.JPG)

Für jede Tiefenebene verwenden wir Indizes, um die Kinderschlüsselpaare zu unterscheiden. Verstärkte Indizes werden für bestimmte Ableitungen mit einem Apostroph verwendet. Der öffentliche Schlüssel pro Jahr wird als Eingabe für die HMAC-Funktion verwendet. Der Index in einem Ableitungspfad gibt den Wert an, der in der HMAC-Funktion verwendet wird.

'Der Index ohne Apostroph entspricht dem verwendeten tatsächlichen Index, während der Index mit Apostroph dem tatsächlichen Index + 2^31 entspricht. Bei verstärkten Ableitungen werden Indizes von 2^31 bis 2^32-1 verwendet. Beispielsweise entspricht der Index 44' dem tatsächlichen Index 2^31 + 44.

Um eine bestimmte Empfangsadresse zu generieren, leiten wir ein Kinderschlüsselpaar aus dem Masterschlüssel und dem Masterkettencode ab. Anschließend verwenden wir den Index, um zwischen verschiedenen Paaren von Kindschlüsseln mit derselben Tiefe zu unterscheiden.

Mit erweiterten Schlüsseln wie XPUB können Sie Ihre Brieftasche mit mehreren Personen teilen. Der Ableitungsstring wird verwendet, um zwischen dem externen String (Adressen, die weitergegeben werden sollen) und dem internen String (Wechseladressen) zu unterscheiden.

Es ist wichtig zu beachten, dass in einer HD-Wallet aufgrund verschiedener Standards unterschiedliche Tiefen verwendet werden. Durch die Ableitung von Elternschlüsseln zu Kindschlüsseln kann von einer Tiefe in eine andere gewechselt werden. Durch die Verwendung unterschiedlicher Zweige in der HD-Wallet können die verschiedenen verfolgten Standards angezeigt werden.

Im nächsten Kapitel werden wir uns mit Empfangsadressen, den Vorteilen ihrer Verwendung und den Schritten ihres Aufbaus befassen.

# Was ist eine Bitcoin-Adresse?

## Die Bitcoin-Adressen.

In diesem Kapitel werden wir Empfangsadressen erforschen, die im Bitcoin-System eine entscheidende Rolle spielen. Sie ermöglichen den Empfang von Geld auf einer Münze und werden aus privaten und öffentlichen Schlüsselpaaren generiert. Zwar gibt es eine Art Skript namens Pay2PublicKey, mit dem man Bitcoins auf einem öffentlichen Schlüssel sperren kann, aber die Nutzer ziehen es in der Regel vor, Empfangsadressen statt dieses Skripts zu verwenden.

![image](assets/image/section5/0.JPG)

Wenn ein Empfänger Bitcoins erhalten möchte, stellt er dem Sender statt seines öffentlichen Schlüssels eine Empfangsadresse zur Verfügung. Eine Adresse ist in Wirklichkeit ein Hash eines öffentlichen Schlüssels mit einem bestimmten Format. Der öffentliche Schlüssel wird vom privaten Kind-Schlüssel abgeleitet, indem mathematische Operationen wie das Addieren und Verdoppeln von Punkten auf elliptischen Kurven verwendet werden.

![image](assets/image/section5/1.JPG)

Es ist wichtig zu beachten, dass es nicht möglich ist, von der Adresse auf den öffentlichen Schlüssel oder vom öffentlichen Schlüssel auf den privaten Schlüssel zurückzugehen. Durch die Verwendung einer Adresse kann die Informationsgröße des öffentlichen Schlüssels, der ursprünglich 512 Bit lang ist, reduziert werden. Es ist möglich, einen öffentlichen Schlüssel zu komprimieren, indem man nur den Wert von x beibehält und ein Präfix hinzufügt, aber diese Technik war zur Zeit der Entstehung von Bitcoin noch nicht bekannt. Durch die Verwendung einer Adresse kann also kein Platz in den Blöcken gewonnen werden'.

Die Bitcoin-Adressen wurden zur Vereinfachung ihrer Verwendung verkleinert. Sie haben eine Prüfsumme, die Tippfehler erkennt und das Risiko des Verlusts von Bitcoins verringert. Im Gegensatz dazu haben öffentliche Schlüssel keine Prüfsumme, was bedeutet, dass Tippfehler zum Verlust der entsprechenden Mittel führen können.

Adressen bieten auch eine zweite Sicherheitsebene zwischen öffentlichen und privaten Informationen, was es schwieriger macht, den privaten Schlüssel zu übernehmen. Die verwendeten Hash-Funktionen ermöglichen es den Schlüsselpaaren, gegen mögliche Angriffe von Quantencomputern resistent zu sein. Tatsächlich können diese Computer möglicherweise ECDSA (Elliptic Curve Digital Signature Algorithm) brechen, aber sie können keine Hash-Funktion brechen.

Es ist wichtig zu betonen, dass jede Adresse nur einmal verwendet wird, was zur Sicherheit und Vertraulichkeit beiträgt. Die Wiederverwendung derselben Adresse birgt ernsthafte Datenschutzprobleme und sollte vermieden werden. Darüber hinaus ist jede Adresse ein Hash eines öffentlichen Schlüssels, begleitet von einer Prüfsumme, um das Risiko des Verlusts von Bitcoins zu verringern.

Für Bitcoin-Adressen werden verschiedene Präfixe verwendet. Zum Beispiel steht BC1Q für eine Segwit V0-Adresse, BC1P für eine Taproot/Segwit V1-Adresse und die Präfixe 1 und 3 sind mit Pay2PublicKeyH/Pay2ScriptH-Adressen (legacy) verbunden. Im nächsten Kurs werden wir Schritt für Schritt die Ableitung einer Adresse aus einem öffentlichen Schlüssel erklären.

Zusammenfassend sind Empfangsadressen ein wesentlicher Bestandteil des Bitcoin-Systems. Sie werden aus privaten und öffentlichen Schlüsselpaaren generiert und dienen zum Empfangen von Mitteln auf einer Münze. Die Adressen enthalten eine Prüfsumme, um das Risiko des Verlusts von Bitcoins zu verringern, und sind so konzipiert, dass sie einmalig verwendet werden, um Sicherheit und Vertraulichkeit zu gewährleisten. Im Bitcoin-System werden verschiedene Arten von Adressen verwendet, die eine erhöhte Vertraulichkeit und Sicherheit bieten.

## Wie erstellt man eine Bitcoin-Adresse?

In diesem Kapitel werden wir die Erstellung einer Empfangsadresse für Bitcoin-Transaktionen behandeln. Eine Empfangsadresse ist eine alphanumerische Darstellung eines komprimierten öffentlichen Schlüssels. Die Umwandlung eines öffentlichen Schlüssels in eine Empfangsadresse erfolgt in mehreren Schritten.

![Bild](assets/image/section5/3.JPG)

Eine der vorteilhaften Eigenschaften von Empfangsadressen ist das Vorhandensein einer Prüfsumme, die Fehler erkennt. Dafür verwenden wir die BCH (Bose-Chaudhuri-Hocquenghem) Prüfsummentechnologie, die eine genaue Fehlererkennung gewährleistet. Diese Technologie trägt auch zur Reduzierung der Anzahl der erforderlichen Zeichen zur Darstellung einer Adresse bei und erleichtert somit deren Verwendung.

Um mit dem Aufbau einer Adresse zu beginnen, müssen wir den entsprechenden öffentlichen Schlüssel komprimieren. Ein roher öffentlicher Schlüssel besteht aus 520 Bits, aber dank der Symmetrie der verwendeten elliptischen Kurve kann eine elliptische Kurve mit einer x-Koordinate mit zwei möglichen Werten für y existieren: positiv oder negativ. Im Bitcoin-Netzwerk arbeiten wir mit einem endlichen Körper positiver ganzer Zahlen anstelle des Körpers der reellen Zahlen. Um einen öffentlichen Schlüssel aus x darzustellen, fügen wir einen Präfix hinzu, der den Wert von y (gerade oder ungerade) angibt. Durch die Komprimierung eines öffentlichen Schlüssels kann seine Größe von 520 auf 264 Bits reduziert werden. Die Parität von y in einem endlichen Körper positiver ganzer Zahlen entspricht der Parität von y im Körper der reellen Zahlen.

![image](assets/image/section5/4.JPG)
![image](assets/image/section5/5.JPG)

Nehmen wir das Beispiel des öffentlichen Schlüssels von Satoshi Nakamoto mit einem Präfix 0,3, der auf einen ungeraden Wert von y hinweist. Dann können wir zum zweiten Schritt des Aufbaus einer Adresse aus komprimierten öffentlichen Schlüsseln übergehen. Es ist möglich, zwei Adressen für jeden öffentlichen Schlüssel zu berechnen. Dazu verwenden wir die SHA256-Funktion, um den Hash des öffentlichen Schlüssels zu erhalten. Anschließend wenden wir die ripemd160-Funktion auf das Ergebnis von SHA256 an, um eine Zeichenfolge zu erhalten. Diese Zeichenfolge wird dann in binärem Format in Gruppen von 5 Bits codiert, zu denen Metadaten hinzugefügt werden, um die Prüfsumme mithilfe des BCH-Programms zu berechnen.

![image](assets/image/section5/6.JPG)

Bei Legacy-Adressen verwenden wir den doppelten SHA256-Hash, um die Prüfsumme der Adresse zu generieren. Für Segwit V0 und V1-Adressen verwenden wir jedoch die BCH-Prüfsummentechnologie, um Fehler zu erkennen. Das BCH-Programm ist in der Lage, Fehler mit einer äußerst geringen Fehlerwahrscheinlichkeit vorzuschlagen und zu korrigieren. Derzeit wird das BCH-Programm verwendet, um Fehler zu erkennen und Änderungsvorschläge zu machen, aber es führt sie nicht automatisch für den Benutzer aus. Die Berechnung der Prüfsumme mit dem BCH-Code basiert auf der Chien-Chauffage-Polynomarithmetik.

![image](assets/image/section5/7.JPG)

Das BCH-Programm erfordert mehrere Eingabeinformationen, einschließlich des HRP (Human Readable Part), das erweitert werden muss. Die Erweiterung des HRP besteht darin, jeden Buchstaben in Basis 2 zu codieren, wobei die ersten drei Bits jedes Zeichens verwendet werden, indem man einen Trenner 0 einfügt und die letzten fünf Bits jedes Zeichens verknüpft. Die blauen Zeichen, die in Dezimalzahlen umgewandelt wurden, entsprechen 3 und 3 in Dezimalzahlen, während die anderen fünf orangefarbenen Zeichen 2 und 3 in Dezimalzahlen entsprechen. Die Erweiterung des HRP in Dezimalzahlen ermöglicht es, die letzten fünf Bits jedes Zeichens zu isolieren und somit die Prüfsumme zu verstärken.

![image](assets/image/section5/8.JPG)

Die Segwit V0-Version wird durch den Code 00 dargestellt und die "Payload" ist in Dezimalzahlen in Schwarz. Dies wird von sechs reservierten Zeichen für die Prüfsumme gefolgt. Die Eingabe mit den Metadaten wird dann dem BCH-Programm übergeben, um die Prüfsumme in Dezimalzahlen zu erhalten. Die Verknüpfung von Version, Payload und Prüfsumme ermöglicht den Aufbau der Adresse. Die Dezimalzeichen werden dann mithilfe einer Zuordnungstabelle in bech32-Zeichen umgewandelt. Das bech32-Alphabet umfasst alle alphanumerischen Zeichen außer 1, b, i und o, um Verwechslungen zu vermeiden.

![image](assets/image/section5/9.JPG)
![image](assets/image/section5/10.JPG)

Um eine Adresse zu erstellen, die mit bc1q beginnt, müssen wir eine Hash-Funktion (H160) auf einen komprimierten öffentlichen Schlüssel anwenden und dann die Prüfsumme, die Version (q), den HRP (bc) und den Trenner (1) hinzufügen. Taproot-Adressen hingegen beginnen mit bc1p, da ihre Version (Segwit V1) 0+1=1 entspricht, daher die Verwendung des Zeichens p. Alle diese Elemente werden dann in BCH32 umgewandelt, eine Bitcoin-spezifische Variante von Base32.

Auf diese Weise haben wir die Schritte zum Erstellen einer Empfangsadresse, die Verwendung der BCH-Prüfsummentechnologie sowie den Aufbau einer Adresse, die mit bc1q oder bc1p beginnt, unter Verwendung der BCH32-Variante von Base32 durchlaufen.

## Zusammenfassung der Kryptographie für Bitcoin-Wallets

Im Laufe dieser Schulung haben wir uns ausführlich mit der hierarchisch deterministischen (HD) Wallet mit BIP32 beschäftigt. Die Entropie spielt bei dieser Art von Wallet eine zentrale Rolle, da sie verwendet wird, um aus einer Zufallszahl eine mnemonische Phrase zu generieren. Mit der Liste von 2048 Wörtern im BIP39 kann diese mnemonische Phrase in eine Reihe leicht zu merkender Wörter codiert werden. Die mnemonische Phrase sowie eine optionale Passphrase sind erforderlich, um den Wallet-Schlüssel zu generieren. Die Passphrase fungiert als kryptografisches Salz, das dem Wallet eine zusätzliche Schutzschicht hinzufügt.

![image](assets/image/section5/11.JPG)

Die Funktion pbkdf2 wird verwendet, um den Seed aus der mnemonischen Phrase und der Passphrase zu generieren, unter Verwendung von hmacha512 und 2048 Iterationen. Der Master Key und der Master Chain Code werden dann aus diesem Seed abgeleitet, erneut unter Verwendung der Funktion hmacha512 mit der Phrase "bitcoin seed". Der Master Private Key und der Master Chain Code sind die obersten Elemente in der Hierarchie der HD Wallets.

![image](assets/image/section5/12.JPG)

Die Ableitung eines Child Keys hängt von mehreren Faktoren ab, einschließlich des Parent Keys und des entsprechenden Chain Codes. Ein Extended Key wird erhalten, indem ein Parent Key mit seinem Chain Code konkateniert wird, während ein Master Key ein separater Key ist. Um eine Adresse abzuleiten, wird zuerst der komprimierte öffentliche Schlüssel mit SHA256 und RIPMD160 gehasht und dann eine Checksumme berechnet. Der doppelte SHA256-Hash wird verwendet, um die Checksumme im Fall eines Legacy-Standards zu berechnen, während das BCH-Programm (Bose-Chaudhuri-Hocquenghem) verwendet wird, um die Checksumme im Fall eines SegWit-Standards zu berechnen. Anschließend wird eine Base58-Darstellung für einen Legacy-Standard verwendet, während das Bech32-Format für einen SegWit-Standard verwendet wird, um die HD Wallet-Adresse zu erhalten.

![image](assets/image/section5/13.JPG)

Zusammenfassend haben wir uns ausführlich mit Hash-Funktionen und ihren Eigenschaften, sowie mit digitalen Signaturen und elliptischen Kurven beschäftigt. Anschließend sind wir in die Welt der deterministischen hierarchischen (HD) Wallets mit BIP32 eingetaucht, wobei wir Entropie und Passphrase verwendet haben, um den Wallet Seed zu generieren. Wir haben auch gelernt, wie man Child Keys ableitet und die HD Wallet-Adresse erhält. Ich hoffe, diese Informationen waren hilfreich für Sie, und ich ermutige Sie nun, mit der Bewertung fortzufahren, um Ihr während des Crypto 301-Kurses erworbenes Wissen zu testen. Vielen Dank für Ihre Aufmerksamkeit.

# Gehen Sie weiter

## Erzeugung eines Seeds aus 128 Würfelwürfen!

Die Erstellung eines mnemonischen Satzes ist ein entscheidender Schritt zur Sicherung Ihrer Kryptowährungs-Brieftasche. Es gibt mehrere Methoden zur Generierung eines mnemonischen Satzes, aber wir werden uns auf die manuelle Methode konzentrieren, bei der Würfel verwendet werden. Es ist wichtig zu beachten, dass diese Methode nicht für eine Brieftasche mit hohem Wert geeignet ist. Es wird empfohlen, eine Open-Source-Software oder eine Hardware-Brieftasche zur Generierung des mnemonischen Satzes zu verwenden. Um einen mnemonischen Satz zu erstellen, verwenden wir Würfel, um binäre Informationen zu generieren. Das Ziel ist es, den Prozess der Erstellung des mnemonischen Satzes zu verstehen.

**Schritt 1 - Vorbereitung:**

Stellen Sie sicher, dass Sie eine amnesische Linux-Distribution wie Tails OS auf einem USB-Stick installiert haben, um die Sicherheit zu erhöhen. Beachten Sie, dass dieses Tutorial nicht zur Erstellung einer Hauptbrieftasche verwendet werden sollte.

**Schritt 2 - Generierung einer zufälligen binären Zahl:**

Wir werden Würfel verwenden, um binäre Informationen zu generieren. Werfen Sie den Würfel 128 Mal und notieren Sie jedes Ergebnis (1 für ungerade, 0 für gerade).

**Schritt 3 - Organisation der binären Zahlen:**

Ordnen Sie die erhaltenen binären Zahlen in Reihen mit 11 Ziffern an, um spätere Berechnungen zu erleichtern. Die zwölfte Zeile sollte nur 7 Ziffern enthalten.

**Schritt 4 - Berechnung der Prüfsumme:**

Die letzten 4 Ziffern für die zwölfte Zeile entsprechen der Prüfsumme. Um diese Prüfsumme zu berechnen, müssen wir ein Terminal einer Linux-Distribution verwenden. Es wird empfohlen, [TailOs](https://tails.boum.org/index.fr.html) zu verwenden, das eine bootfähige amnesische Distribution von einem USB-Stick ist. Sobald Sie sich in Ihrem Terminal befinden, geben Sie den Befehl `echo <binäre Zahl> | shasum -a 254 -0` ein. Ersetzen Sie `<binäre Zahl>` durch Ihre Liste von 128 Nullen und Einsen. Die Ausgabe ist ein hexadezimaler Hash. Notieren Sie das erste Zeichen dieses Hashs und konvertieren Sie es in binär. Sie können diese [Tabelle](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) zur Hilfe nehmen. Fügen Sie die Prüfsumme in binärer Form (4 Ziffern) zur zwölften Zeile Ihres Blattes hinzu.

**Schritt 5 - Konvertierung in Dezimalzahl:**

Um die Wörter, die zu jeder Ihrer Zeilen gehören, zu finden, müssen Sie zuerst jede 11-Bit-Serie in eine Dezimalzahl umwandeln. Hier können Sie keinen Online-Konverter verwenden, da diese Bits Ihren mnemonischen Satz darstellen. Sie müssen also mit einem Taschenrechner und einem Trick umwandeln: Jedes Bit ist mit einer Potenz von 2 verbunden, und von links nach rechts haben wir 11 Positionen, die jeweils 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1 entsprechen. Um Ihre 11-Bit-Serie in eine Dezimalzahl umzuwandeln, müssen Sie nur die Positionen addieren, die eine 1 enthalten. Zum Beispiel entspricht die Serie 00110111011 der folgenden Addition: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Sie können nun jede Zeile in eine Dezimalzahl umwandeln. Und bevor Sie zur Codierung in Wörter übergehen, müssen Sie zu allen Zeilen +1 hinzufügen, da der Index der BIP39-Wortliste ab 1 und nicht ab 0 beginnt.

**Schritt 8 - Generierung des mnemonischen Satzes:**

Beginnen Sie damit, die [Liste der 2048 Wörter](https://seedxor.com/files/wordlist.pdf) auszudrucken, um die Umwandlung zwischen Ihren Dezimalzahlen und den BIP39-Wörtern durchzuführen. Das Besondere an dieser Liste ist, dass kein Wort die ersten 4 Buchstaben mit allen anderen Wörtern in diesem Wörterbuch gemeinsam hat. Suchen Sie dann für jede Ihrer Zeilen das Wort, das der Dezimalzahl zugeordnet ist.

**Schritt 9 - Test des mnemonischen Satzes:**

Testen Sie sofort Ihren mnemonischen Satz in der Sparrow Wallet, indem Sie eine Brieftasche daraus erstellen. Wenn Sie einen ungültigen Prüfsummenfehler erhalten, haben Sie wahrscheinlich einen Rechenfehler gemacht. Korrigieren Sie diesen Fehler, indem Sie wieder bei Schritt 4 beginnen, und testen Sie erneut in der Sparrow Wallet. Voilà! Sie haben gerade eine neue Bitcoin-Brieftasche aus 128 Würfelwürfen erstellt.

Das Generieren eines mnemonischen Satzes ist ein wichtiger Prozess zur Sicherung Ihrer Kryptowährungs-Brieftasche. Es wird empfohlen, sicherere Methoden wie die Verwendung von Open-Source-Software oder Hardware-Wallets zu verwenden, um den mnemonischen Satz zu generieren. Dennoch hilft Ihnen diese Übung dabei, besser zu verstehen, wie wir aus einer Zufallszahl eine Bitcoin-Brieftasche erstellen können.

## Fazit und Ende

### Dank und weiterhin viel Erfolg bei der Erforschung des Kaninchenbaus.

Wir möchten uns herzlich bei Ihnen für die Teilnahme am Crypto 301-Kurs bedanken. Wir hoffen, dass diese Erfahrung für Sie bereichernd und lehrreich war. Wir haben viele spannende Themen behandelt, von Mathematik über Kryptographie bis hin zum Funktionsprinzip des Bitcoin-Protokolls.

Wenn Sie das Thema weiter vertiefen möchten, haben wir eine zusätzliche Ressource für Sie. Wir haben ein exklusives Interview mit Théo Pantamis und Loïc Morel, zwei renommierten Experten auf dem Gebiet der Kryptographie, durchgeführt. Dieses Interview beleuchtet verschiedene Aspekte des Themas im Detail und bietet interessante Perspektiven.

Zögern Sie nicht, sich dieses Interview anzusehen, um weiterhin in die faszinierende Welt der Kryptographie einzutauchen. Wir hoffen, dass es Ihnen nützlich und inspirierend für Ihren weiteren Werdegang ist. Nochmals vielen Dank für Ihre Teilnahme und Ihr Engagement während des gesamten Kurses.

### Unterstütze uns

Dieser Kurs sowie der gesamte Inhalt dieser Universität wurden Ihnen kostenlos von unserer Community zur Verfügung gestellt. Um uns zu unterstützen, können Sie ihn in Ihrem Umfeld teilen, Mitglied der Universität werden und sogar über GitHub zu ihrer Entwicklung beitragen. Im Namen des gesamten Teams, vielen Dank!

### Bewerte den Kurs

Ein Bewertungssystem für den Kurs wird bald in diese neue E-Learning-Plattform integriert! In der Zwischenzeit vielen Dank für die Teilnahme am Kurs und wenn Ihnen dieser gefallen hat, denken Sie bitte daran, ihn in Ihrem Umfeld zu teilen.
