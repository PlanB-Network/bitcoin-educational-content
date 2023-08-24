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

**Anmerkung: Dieser Kurs wurde vollständig von IA übersetzt und das Korrekturlesen wurde noch nicht durchgeführt. Wenn Sie dies tun möchten, tragen Sie bitte zum [github](https://github.com/DecouvreBitcoin/sovereign-university-data/tree/main/courses/crypto301) bei.**

Sind Sie fasziniert von Bitcoin? Fragen Sie sich, wie eine Bitcoin-Wallet funktioniert? Machen Sie sich bereit für eine fesselnde Reise ins Herz der Kryptographie! Unser Experte Loïc wird Sie durch die Tiefen der Erstellung einer Bitcoin-Wallet führen und die Geheimnisse hinter einschüchternden technischen Begriffen wie Hashing, Schlüsselableitung und elliptischen Kurven enthüllen.

Dieses Training wird Ihnen nicht nur das Wissen vermitteln, um die Struktur einer Bitcoin-Wallet zu verstehen, sondern Sie auch darauf vorbereiten, tiefer in die faszinierende Welt der Kryptographie einzutauchen. Sind Sie bereit, diese Reise anzutreten? Schließen Sie sich uns an und verwandeln Sie Ihre Neugier in Kompetenz!

+++

# Einführung in die Kryptographie

![Einführung von Rogzy](https://youtu.be/ul8zU5QWIXg)

Wir freuen uns, Sie zu unserem neuen Kurs "Crypto 301: Einführung in die Kryptographie und HD-Wallets" begrüßen zu dürfen, geleitet von unserem Experten Loïc Morel. Dieser Kurs wird Sie in die faszinierende Welt der Kryptographie einführen, einer grundlegenden Disziplin der Mathematik, die die Verschlüsselung und Sicherheit Ihrer Daten gewährleistet.

In unserem täglichen Leben und insbesondere im Bereich der Bitcoins spielt Kryptographie eine entscheidende Rolle. Konzepte wie private und öffentliche Schlüssel, Adressen, Ableitungspfade, Seed und Entropie stehen im Mittelpunkt der Verwendung und Erstellung einer Bitcoin-Wallet. In diesem Kurs wird Ihnen Loïc ausführlich erklären, wie private Schlüssel erstellt werden und wie sie mit Adressen verknüpft sind. Loïc wird auch eine Stunde damit verbringen, Ihnen die mathematischen Details der elliptischen Kurve zu erklären. Darüber hinaus werden Sie verstehen, warum die Verwendung von HMAC SHA512 wichtig ist, um Ihre Wallet zu sichern, und was der Unterschied zwischen Seed und mnemonischer Phrase ist.
Das ultimative Ziel dieser Schulung ist es, Ihnen das technische Verständnis der Prozesse zur Erstellung einer HD-Wallet und der verwendeten kryptographischen Methoden zu ermöglichen. Im Laufe der Jahre haben sich Bitcoin-Wallets weiterentwickelt, um einfacher zu bedienen, sicherer und standardisierter zu sein, dank spezifischer BIPs. Loïc wird Ihnen helfen, diese BIPs zu verstehen, um die Entscheidungen der Bitcoin-Entwickler und Kryptographen zu verstehen. Wie alle Schulungen unserer Universität ist diese vollständig kostenlos und Open Source. Das bedeutet, dass Sie sie frei verwenden und nutzen können. Wir freuen uns darauf, Ihr Feedback am Ende dieses spannenden Kurses zu erhalten.
![Einführung von Loïc](https://youtu.be/mwuxXLk4Kws)

Hallo allerseits, ich bin Loïc Morel, Ihr Führer durch diese technische Erkundung der Kryptographie, die in Bitcoin-Wallets verwendet wird.

Unsere Reise beginnt mit einem Tauchgang in die Tiefen kryptographischer Hash-Funktionen. Gemeinsam werden wir die Mechanismen des unverzichtbaren SHA256 auseinandernehmen und verschiedene Algorithmen zur Ableitung erkunden.

Wir werden unser Abenteuer fortsetzen, indem wir die geheimnisvolle Welt der digitalen Signaturen entschlüsseln. Sie werden entdecken, wie die Magie elliptischer Kurven auf diese Signaturen angewendet wird, und wir werden erklären, wie der öffentliche Schlüssel aus dem privaten Schlüssel berechnet wird. Und natürlich werden wir den Prozess der digitalen Signatur behandeln.

Dann werden wir in die Vergangenheit zurückgehen, um die Entwicklung von Bitcoin-Wallets zu betrachten, und wir werden uns mit Entropie und Zufallszahlen befassen. Wir werden uns die berühmte Mnemonik-Phrase ansehen und auch auf die Passphrase eingehen. Sie werden sogar die Möglichkeit haben, ein einzigartiges Erlebnis zu machen, indem Sie einen Seed aus 128 Würfelwürfen erstellen!

Mit diesem soliden Grundlagenwissen werden wir bereit sein für den entscheidenden Teil: die Erstellung einer Bitcoin-Wallet. Vom Erzeugen des Seeds und des Master-Schlüssels bis hin zur Untersuchung erweiterter Schlüssel werden wir jeden Schritt genau betrachten. Wir werden auch die Struktur der Wallets und die Ableitungspfade diskutieren.

Zum Abschluss werden wir unsere Reise beenden, indem wir uns Bitcoin-Adressen genauer ansehen. Wir werden erklären, wie sie erstellt werden und welche wichtige Rolle sie im Betrieb von Bitcoin-Wallets spielen.

Begleiten Sie mich auf dieser fesselnden Reise und machen Sie sich bereit, die Welt der Kryptographie wie nie zuvor zu erkunden. Lassen Sie Ihre Vorurteile hinter sich und öffnen Sie Ihren Geist für ein neues Verständnis von Bitcoin und seiner grundlegenden Struktur.

# Hash-Funktionen

## Einführung in kryptographische Hash-Funktionen im Zusammenhang mit Bitcoin

![2.1 - die Funktionen kryptographischer Hashes](https://youtu.be/dvnGArYvVr8)
Willkommen zu unserer heutigen Sitzung, die sich eingehend mit der kryptographischen Welt der Hash-Funktionen beschäftigt, einem wesentlichen Baustein für die Sicherheit des Bitcoin-Protokolls. Stellen Sie sich eine Hash-Funktion als einen äußerst effizienten kryptografischen Entschlüsselungsroboter vor, der Informationen beliebiger Größe in einen eindeutigen und festen Fingerabdruck, genannt "Hash", "Abdruck" oder "Digest", umwandelt.
Zusammenfassend nimmt eine Hash-Funktion eine Eingabe beliebiger Größe entgegen und wandelt sie in eine feste Ausgabe um.

Das Profil kryptographischer Hash-Funktionen zu beschreiben erfordert das Verständnis von zwei wesentlichen Eigenschaften: ihre Unumkehrbarkeit und ihre Fälschungssicherheit.

Die Unumkehrbarkeit oder Widerstandsfähigkeit gegenüber dem Urbild bedeutet, dass die Berechnung der Ausgabe bei Kenntnis der Eingabe einfach durchgeführt werden kann, aber die Berechnung der Eingabe aus der Ausgabe nicht möglich ist.
Es handelt sich um eine Einwegfunktion.

![image](assets/image/section1/0.JPG)

Die Fälschungssicherheit ergibt sich daraus, dass bereits die geringste Änderung der Eingabe zu einer stark unterschiedlichen Ausgabe führt.
Diese Funktionen ermöglichen die Überprüfung der Integrität von heruntergeladener Software.

![image](assets/image/section1/1.JPG)

Eine weitere entscheidende Eigenschaft ist ihre Widerstandsfähigkeit gegenüber Kollisionen und zweitem Urbild. Eine Kollision tritt auf, wenn zwei unterschiedliche Eingaben die gleiche Ausgabe erzeugen.
Zwar sind Kollisionen im Bereich der Hash-Funktionen unvermeidlich, aber eine ausgezeichnete kryptographische Hash-Funktion minimiert sie erheblich. Das Risiko sollte so gering sein, dass es als vernachlässigbar betrachtet werden kann. Es ist, als ob jeder Hash ein Haus in einer riesigen Stadt wäre; trotz der enormen Anzahl von Häusern stellt eine gute Hash-Funktion sicher, dass jedes Haus eine eindeutige Adresse hat.
Der Widerstand gegenüber dem zweiten Urbild hängt von der Widerstandsfähigkeit gegenüber Kollisionen ab; wenn es Widerstand gegen Kollisionen gibt, gibt es auch Widerstand gegen das zweite Urbild.
Gegeben eine vorgegebene Eingabe müssen wir eine zweite Eingabe finden, die sich von der ersten unterscheidet und zu einer Kollision in der Ausgabe der Funktion führt. Der Widerstand gegen das zweite Urbild ist ähnlich wie der Widerstand gegen Kollisionen, mit der Ausnahme, dass die Eingabe vorgegeben ist.
Navigieren wir nun durch die stürmischen Fluten veralteter Hashfunktionen. SHA0, SHA1 und MD5 gelten heute als rostige Rümpfe im Meer der kryptografischen Hashfunktionen. Von ihnen wird oft abgeraten, da sie ihre Kollisionsresistenz verloren haben. Das Schubladenprinzip erklärt, warum trotz unserer besten Bemühungen eine Kollisionsvermeidung aufgrund der begrenzten Größe der Ausgabe nicht möglich ist. Um wirklich als sicher zu gelten, muss eine Hashfunktion gegen Kollisionen, Second Preimage und Preimage resistent sein.

Als Schlüsselelement im Bitcoin-Protokoll ist die Hashfunktion SHA-256 der Kapitän des Schiffes. Andere Funktionen, wie SHA-512, werden für die Ableitung mit HMAC und PBKDF verwendet. Außerdem wird RIPMD160 verwendet, um einen Fingerabdruck auf 160 Bit zu reduzieren. Wenn wir von HASH256 und HASH160 sprechen, beziehen wir uns auf die Verwendung eines doppelten Hashes mit SHA-256 und RIPMD.

Bei HASH256 handelt es sich um einen doppelten Hash der Nachricht mit der Funktion SHA256.

$$
SHA256(SHA256(Nachricht))
$$

Bei HASH160 handelt es sich um ein doppeltes Hashing der Nachricht, wobei zuerst die Funktion SHA256 und dann RIPMD160 verwendet wird.

$$
RIPMD160(SHA256(Nachricht))
$$

Die Verwendung von HASH160 ist besonders vorteilhaft, da sie die Sicherheit von SHA-256 nutzt und gleichzeitig die Größe des Fingerabdrucks verringert.

Zusammenfassend lässt sich sagen, dass das ultimative Ziel einer kryptografischen Hashfunktion darin besteht, eine Information beliebiger Größe in einen Fingerabdruck fester Größe zu überführen. Um als sicher anerkannt zu werden, muss sie mehrere Fäden in der Hand halten: Irreversibilität, Fälschungssicherheit, Kollisionssicherheit und Resistenz gegen zweite Pre-Images.

![image](assets/image/section1/2.JPG)

Am Ende dieser Erkundung haben wir die kryptografischen Hash-Funktionen entmystifiziert, ihre Verwendung im Bitcoin-Protokoll aufgezeigt und ihre spezifischen Ziele aufgeschlüsselt. Wir haben gelernt, dass Hashfunktionen, um als sicher zu gelten, resistent gegen Preimage, Second Preimage, Kollisionen und Fälschung sein müssen. Außerdem haben wir die Bandbreite der verschiedenen Hashfunktionen durchlaufen, die im Bitcoin-Protokoll verwendet werden. In unserer nächsten Sitzung tauchen wir in das Herz der Hashfunktion SHA256 ein und entdecken die faszinierende Mathematik, die ihr ihre einzigartigen Eigenschaften verleiht.

## Die Zahnräder von SHA256

![Das Räderwerk von SHA256](https://youtu.be/74SWg_ZbUj4)

Willkommen zur Fortsetzung unserer faszinierenden Reise durch die kryptographischen Labyrinthe der Hashfunktion. Heute lüften wir den Schleier über den Geheimnissen von SHA256, einem komplexen, aber genialen Verfahren, das wir zuvor eingeführt haben.
Zur Erinnerung, das Ziel der SHA256-Hashfunktion besteht darin, eine Eingabebotschaft beliebiger Größe zu nehmen und eine 256-Bit-Hash-Ausgabe zu generieren.

### Vorverarbeitung

Lassen Sie uns einen Schritt weiter in dieses Labyrinth gehen und mit der Vorverarbeitung von SHA256 beginnen.

#### Padding-Bits

Das Ziel dieses ersten Schrittes ist es, eine Nachricht auf ein Vielfaches von 512 Bits auszugleichen. Dazu fügen wir Padding-Bits zur Nachricht hinzu.

Sei M die Größe der ursprünglichen Nachricht.
Sei 1 ein Bit für den Trenner reserviert.
Sei P die Anzahl der Bits für das Padding und 64 die Anzahl der Bits, die für die zweite Vorverarbeitungsphase beiseite gelegt werden.
Die Gesamtzahl muss ein Vielfaches von 512 Bits sein, das ist n.

![image](assets/image/section1/3.JPG)

Beispiel mit einer Eingabebotschaft von 950 Bits:

```
Schritt 1: Größe bestimmen; die endgültige ideale Anzahl von Bits.
Das erste Vielfache von 512 > (M + 64 + 1) (mit M = 950) ist 1024.
1024 = 2 * 512
Also n = 2.

Schritt 2: P bestimmen, die Anzahl der erforderlichen Padding-Bits, um die endgültige ideale Anzahl von Bits zu erreichen.
-> M + 1 + P + 64 = n * 512
-> M + 1 + P + 64 = 2 * 512
-> 940 + 1 + P + 64 = 1024
-> P = 1024 - 1 - 64 - 950
-> P = 9

Es müssen also 9 Padding-Bits hinzugefügt werden, um eine Nachricht auf ein Vielfaches von 512 auszugleichen.
```

Und jetzt?
Direkt nach der ursprünglichen Nachricht muss der Trenner 1 gefolgt von P hinzugefügt werden, das in unserem Beispiel neun 0 ist.

```
Nachricht + 1 000 000 000
```

#### Größenpadding

Wir gehen nun zur zweiten Phase der Vorverarbeitung über, bei der die binäre Darstellung der Größe der ursprünglichen Nachricht in Bits hinzugefügt wird.

Nehmen wir das Beispiel mit einer Eingabe von 950 Bits:

```
Die binäre Darstellung der Zahl 950 ist: 11 1011 0110

Wir verwenden unsere 64 reservierten Bits aus dem vorherigen Schritt. Wir fügen Nullen hinzu, um unsere 64 Bits auf unsere ausgeglichene Eingabe abzurunden. Dann kombinieren wir die ursprüngliche Nachricht, das Padding der Bits und das Größenpadding, um unsere ausgeglichene Eingabe zu erhalten.
```

Hier ist das Ergebnis:

![image](assets/image/section1/4.JPG)

### Die Verarbeitung

#### Verständnisvoraussetzungen

##### Die Initialisierungskonstanten und -vektoren

Jetzt bereiten wir uns auf die ersten Schritte bei der Verarbeitung der SHA-256-Funktion vor. Wie bei jedem guten Rezept benötigen wir einige Grundzutaten, die wir als Konstanten und Initialisierungsvektoren bezeichnen.
Die Initialisierungsvektoren, von A bis H, sind die ersten 32 Bit der Dezimalteile der Quadratwurzeln der ersten acht Primzahlen. Sie werden uns in den ersten Verarbeitungsschritten als Basiswerte dienen. Ihre Werte sind im Hexadezimalformat.

Die Konstanten K, von 0 bis 63, repräsentieren ihrerseits die ersten 32 Bits der dezimalen Teile der Kubikwurzeln der ersten 64 Primzahlen. Sie werden bei jeder Umdrehung der Komprimierungsfunktion verwendet. Ihre Werte sind ebenfalls im Hexadezimalformat.

![image](assets/image/section1/5.JPG)

##### Die verwendeten Operationen.

Innerhalb der Komprimierungsfunktion verwenden wir spezielle Operatoren wie XOR, AND und NOT. Wir verarbeiten die Bits eines nach dem anderen entsprechend ihrem Rang, indem wir den XOR-Operator und eine Wahrheitstabelle verwenden. Der AND-Operator wird verwendet, um nur dann 1 zurückzugeben, wenn beide Operanden gleich 1 sind, und der NOT-Operator, um den entgegengesetzten Wert eines Operanden zurückzugeben. Außerdem verwenden wir die Operation SHR, um die Bits entsprechend einer gewählten Zahl nach rechts zu verschieben.

Die Wahrheitstabelle :

![image](assets/image/section1/6.JPG)

Die Operationen zum Verschieben von Bits :

![image](assets/image/section1/7.JPG)

#### Die Komprimierungsfunktion

Bevor wir die Komprimierungsfunktion anwenden, teilen wir den Input in 512-Bit-Blöcke auf. Jeder Block wird unabhängig von den anderen verarbeitet.

Jeder 512-Bit-Block wird dann wieder in 32-Bit-Stücke W unterteilt. Auf diese Weise repräsentiert W(0) die ersten 32 Bits des 512-Bit-Blocks. W(1) steht für die nächsten 32 Bits und so weiter, bis die 512 Bits des Blocks erreicht sind.

Sobald alle Konstanten K und die Stücke W definiert sind, können wir für jedes Stück W die folgenden Berechnungen für jede Runde bearbeiten.

Wir führen in der Komprimierungsfunktion 64 Berechnungsrunden durch. In der letzten Runde werden wir bei "Funktionsausgabe" einen Zwischenzustand haben, der zum Anfangszustand der Komprimierungsfunktion addiert wird.

Danach wiederholen wir alle diese Schritte der Komprimierungsfunktion auf dem nächsten 512-Bit-Block, bis zum letzten Block.

Alle Additionen in der Komprimierungsfunktion sind Modulo-2^32-Additionen, um immer eine 32-Bit-Summe zu erhalten.

![image](assets/image/section1/9.JPG)

![image](assets/image/section1/8.JPG)

##### Ein Rundgang durch die Komprimierungsfunktion

![image](assets/image/section1/11.JPG)

![image](assets/image/section1/10.JPG)

Der Komprimierungsfunktion wird 64 Mal durchlaufen. Als Eingabe erhalten wir unsere Blöcke W und unsere zuvor definierten Konstanten K.
Die roten Quadrate/Kreuze entsprechen einer Addition modulo 2^32 Bits.

Die Eingaben A, B, C, D, E, F, G, H werden jeweils mit einem 32-Bit-Wert assoziiert, um insgesamt 32 \* 8 = 256 Bits zu erzeugen.
Als Ausgabe erhalten wir eine neue Sequenz A, B, C, D, E, F, G, H. Diese Ausgabe wird dann als Eingabe für den nächsten Durchlauf verwendet und so weiter bis zum Ende des 64. Durchlaufs.

Die Werte der Eingabesequenz im ersten Durchlauf der Komprimierungsfunktion entsprechen den zuvor definierten Initialisierungsvektoren.
Zur Erinnerung, die Initialisierungsvektoren repräsentieren die ersten 32 Bits der Dezimalstellen der Quadratwurzeln der ersten 8 Primzahlen.

Hier ist ein Beispiel für einen Durchlauf:

![image](assets/image/section1/12.1.png)

##### Zwischenzustand

Zur Erinnerung, die Nachricht wird in Blöcke von 512 Bits aufgeteilt, die dann in 32-Bit-Stücke unterteilt werden. Für jeden 512-Bit-Block wenden wir die 64 Durchläufe der Komprimierungsfunktion an.
Der Zwischenzustand entspricht dem Ende der 64 Durchläufe eines Blocks. Die Werte der Ausgabesequenz nach diesem 64. Durchlauf werden als Anfangswerte für den ersten Durchlauf des nächsten Blocks verwendet.

![image](assets/image/section1/12.2.png)

#### Gesamtüberblick über die Hash-Funktion

![image](assets/image/section1/13.JPG)

Wir stellen fest, dass die Ausgabe des ersten 512-Bit-Nachrichtenstücks unseren Initialisierungsvektoren entspricht, die als Eingabe für das zweite 512-Bit-Nachrichtenstück verwendet werden, und so weiter.

Die Ausgabe des letzten Durchlaufs, des letzten Stücks, entspricht dem endgültigen Ergebnis der SHA256-Funktion.

Abschließend möchten wir die entscheidende Rolle der Berechnungen in den CH-, MAJ-, σ0- und σ1-Boxen hervorheben. Diese Operationen sind unter anderem die Wächter, die die Robustheit der SHA256-Hash-Funktion gegen Angriffe gewährleisten und sie zu einer bevorzugten Wahl für die Sicherung vieler digitaler Systeme machen, insbesondere im Bitcoin-Protokoll. Es ist offensichtlich, dass die Schönheit von SHA256 trotz ihrer Komplexität darin besteht, dass sie in der Lage ist, den Eingang aus dem Hash wiederherzustellen, während die Überprüfung des Hashes für eine gegebene Eingabe eine mechanisch einfache Aktion ist.

## Die für die Ableitung verwendeten Algorithmen

![Die für die Ableitung verwendeten Algorithmen](https://youtu.be/ZF1_BMsOJXc)

Die Ableitungsalgorithmen HMAC und PBKDF2 sind Schlüsselkomponenten in der Sicherheitsmechanik des Bitcoin-Protokolls. Sie schützen vor verschiedenen potenziellen Angriffen und gewährleisten die Integrität von Bitcoin-Wallets.
HMAC und PBKDF2 sind kryptographische Werkzeuge, die für verschiedene Aufgaben in Bitcoin verwendet werden. HMAC wird hauptsächlich verwendet, um Längenerweiterungsangriffe bei der Ableitung von hierarchisch deterministischen (HD) Wallets zu verhindern, während PBKDF2 verwendet wird, um eine mnemonische Phrase in einen Seed umzuwandeln.

#### HMAC-SHA512

Das HMAC-SHA512-Paar hat zwei Eingaben: eine Nachricht m (Eingabe 1) und einen vom Benutzer willkürlich gewählten Schlüssel K (Eingabe 2).
Es hat auch eine feste Ausgabe von 512 Bits.

```
Beachten Sie:
- m: vom Benutzer gewählte Nachricht beliebiger Länge (Eingabe 1)
- K: vom Benutzer gewählter beliebiger Schlüssel (Eingabe 2)
- K': der angepasste Schlüssel K. Er wurde auf die Blockgröße B angepasst.
- ||: Verkettungsoperation.
- opad: Konstante definiert durch das Byte 0x5c, wiederholt B Mal.
- ipad: Konstante definiert durch das Byte 0x36, wiederholt B Mal.
- B: Die Blockgröße der verwendeten Hash-Funktion.
```

![image](assets/image/section1/14.JPG)

HMAC-SHA512, das eine Nachricht und einen Schlüssel als Eingabe nimmt, generiert eine Ausgabe fester Größe. Um die Einheitlichkeit zu gewährleisten, wird der Schlüssel entsprechend der Blockgröße, die in der Hash-Funktion verwendet wird, angepasst. Im Rahmen der HD-Wallet-Derivation wird HMAC-SHA-512 verwendet. Letzteres funktioniert mit 1024-Bit-Blöcken (128 Bytes) und passt den Schlüssel entsprechend an. Es verwendet die Konstanten OPAD (0x5c) und IPAD (0x36), die so oft wiederholt werden, wie nötig, um die Sicherheit zu verstärken.

Der HMAC-SHA-512-Prozess beinhaltet die Verkettung des Ergebnisses von SHA-512, das auf den Schlüssel XOR OPAD und den Schlüssel XOR IPAD angewendet wird, mit der Nachricht. Wenn es mit 1024-Bit-Blöcken (128 Bytes) verwendet wird, wird der Eingangsschlüssel bei Bedarf mit Nullen aufgefüllt und dann mit IPAD und OPAD XORiert. Der modifizierte Schlüssel wird dann mit der Nachricht verkettet.

![image](assets/image/section1/15.JPG)

Die Verwendung einer zusätzlichen Entropiequelle im Zeichenstring erhöht die Sicherheit der abgeleiteten Schlüssel. Ohne sie könnte ein Angriff die gesamte Wallet kompromittieren und alle Bitcoins stehlen.

#### PBKDF2

PBKDF2 wird verwendet, um eine mnemonische Phrase in einen Seed umzuwandeln. In diesem Fall finden wir in Eingabe 1 die mnemonische Phrase und in Eingabe 2 die Passphrase.
Dieser Algorithmus führt 2048 Durchläufe unter Verwendung von HMAC SHA512 durch. Durch diese Ableitungsalgorithmen können zwei verschiedene Eingaben zu einer eindeutigen und festen Ausgabe führen, was das Problem möglicher Angriffe auf die Längenerweiterung bei SHA-2-Funktionen behebt. Ein Angriff auf die Längenerweiterung nutzt eine spezifische Eigenschaft bestimmter kryptografischer Hashfunktionen aus. Bei einem solchen Angriff kann ein Angreifer, der bereits den Hash eines unbekannten Nachrichten besitzt, diesen verwenden, um den Hash einer längeren Nachricht zu berechnen, die eine Erweiterung der ursprünglichen Nachricht ist. Dies ist oft möglich, ohne den Inhalt der ursprünglichen Nachricht zu kennen, was zu erheblichen Sicherheitslücken führen kann, wenn eine solche Hashfunktion für Aufgaben wie die Integritätsprüfung verwendet wird.

![image](assets/image/section1/16.JPG)

Zusammenfassend spielen die HMAC- und PBKDF2-Algorithmen eine wesentliche Rolle bei der Sicherheit der Ableitung von HD-Wallets im Bitcoin-Protokoll. HMAC-SHA-512 wird verwendet, um Angriffe auf die Längenerweiterung zu verhindern, während PBKDF2 die Umwandlung des mnemonischen Satzes in einen Seed ermöglicht. Der Chain-Code fügt der Schlüsselableitung eine zusätzliche Entropiequelle hinzu und gewährleistet so die Robustheit des Systems.

# Digitale Signaturen

## Digitale Signaturen und elliptische Kurven

![Digitale Signaturen und elliptische Kurven](https://youtu.be/gOjYiPkx4z8)

Wo werden diese berühmten Bitcoins gespeichert? Nicht in einer Bitcoin-Brieftasche, wie man vielleicht denken könnte. Tatsächlich speichert eine Bitcoin-Brieftasche die privaten Schlüssel, die zum Nachweis des Besitzes der Bitcoins erforderlich sind. Die Bitcoins selbst werden in der Blockchain, einer dezentralen Datenbank, die alle Transaktionen archiviert, aufgezeichnet.

In dem Bitcoin-System ist die Recheneinheit der Bitcoin (beachten Sie das kleine "b"). Diese ist bis zu acht Dezimalstellen teilbar, wobei die kleinste Einheit der Satoshi ist. UTXO, oder "Unspent Transaction Output", repräsentiert nicht ausgegebene Transaktionsausgaben, die einer öffentlichen Schlüssel zugeordnet sind, der mathematisch mit einem privaten Schlüssel verknüpft ist. Um diese Bitcoins auszugeben, muss die Ausgabebedingung der Transaktion erfüllt werden. Eine typische Ausgabebedingung besteht darin, dem Rest des Netzwerks nachzuweisen, dass der Benutzer der rechtmäßige Eigentümer des mit UTXO verbundenen öffentlichen Schlüssels ist. Dazu muss er nachweisen, dass er im Besitz des privaten Schlüssels ist, der dem öffentlichen Schlüssel jedes UTXO entspricht, ohne jedoch den privaten Schlüssel preiszugeben.
Das ermöglicht die digitale Signatur. Sie dient als mathematischer Beweis für den Besitz eines privaten Schlüssels, der mit einem bestimmten öffentlichen Schlüssel verbunden ist. Diese Technik zum Schutz von Daten basiert im Wesentlichen auf einem faszinierenden Bereich der Kryptographie, der als elliptische Kurvenkryptographie (ECC) bezeichnet wird.

Die Signatur kann mathematisch von anderen Parteien im Bitcoin-Netzwerk überprüft werden.

![image](assets/image/section2/0.JPG)

Um die Sicherheit von Transaktionen zu gewährleisten, verwendet Bitcoin zwei Protokolle für digitale Signaturen: ECDSA (Elliptic Curve Digital Signature Algorithm) und Schnorr. ECDSA ist ein Signaturprotokoll, das seit dem Start von Bitcoin im Jahr 2009 integriert ist, während Schnorr-Signaturen erst kürzlich im November 2021 hinzugefügt wurden. Obwohl beide Protokolle auf elliptischer Kurvenkryptographie basieren und ähnliche mathematische Mechanismen verwenden, unterscheiden sie sich hauptsächlich in Bezug auf die Struktur der Signatur.

In diesem Kurs werden wir den ECDSA-Algorithmus vorstellen.

### Was ist eine elliptische Kurve?

Elliptische Kurvenkryptographie ist eine Sammlung von Algorithmen, die eine elliptische Kurve aufgrund ihrer verschiedenen geometrischen und mathematischen Eigenschaften für kryptographische Zwecke verwenden und deren Sicherheit auf der Schwierigkeit der Berechnung des diskreten Logarithmus beruht.

Elliptische Kurven sind in einer Vielzahl von kryptographischen Anwendungen im Bitcoin-Protokoll nützlich, von Schlüsselaustausch bis hin zur asymmetrischen Verschlüsselung und digitalen Signaturen.

Elliptische Kurven haben interessante Eigenschaften:

- Symmetrie: Jede nicht-vertikale Linie, die zwei Punkte auf der elliptischen Kurve schneidet, schneidet die Kurve in einem dritten Punkt.
- Jede nicht-vertikale Linie, die die Kurve in einem Punkt berührt, schneidet die Kurve immer in einem zweiten eindeutigen Punkt.

Das Bitcoin-Protokoll verwendet eine spezielle elliptische Kurve namens Secp256k1 für seine kryptographischen Operationen.

Bevor wir tiefer in diese Signaturmechanismen eintauchen, ist es wichtig, zu verstehen, was eine elliptische Kurve ist. Eine elliptische Kurve wird durch die Gleichung y² = x³ + ax + b definiert. Jeder Punkt auf dieser Kurve hat eine charakteristische Symmetrie, die der Schlüssel zu ihrer Nützlichkeit in der Kryptographie ist.

![image](assets/image/section2/1.JPG)

Letztendlich werden verschiedene elliptische Kurven als sicher für kryptographische Zwecke anerkannt. Die bekannteste ist vielleicht die Kurve secp256r1. Für Bitcoin hat sich jedoch Satoshi Nakamoto für eine andere Kurve entschieden: secp256k1.

Diese Kurve wird durch die Parameter a=0 und b=7 definiert, und ihre Gleichung lautet y² = x³ + 7 modulo n, wobei n die Primzahl ist, die die Ordnung der Kurve bestimmt.

![image](assets/image/section2/2.JPG)
Die erste Abbildung zeigt die secp256k1-Kurve über dem Körper der reellen Zahlen und ihre Gleichung. Das zweite Bild ist eine Darstellung der secp256k1-Kurve über dem Körper ZP, dem Körper der natürlichen positiven Zahlen, modulo p, wobei p eine Primzahl ist. Es ähnelt einer Punktwolke. Wir verwenden diesen Körper der natürlichen positiven Zahlen, um Approximationen zu vermeiden.
p ist eine Primzahl und stellt die Ordnung der verwendeten Kurve dar.
Schließlich lautet die Gleichung, die im Bitcoin-Protokoll verwendet wird:

$$
y^2 = (x^3 + 7) mod(p)
$$

Die Gleichung der elliptischen Kurve in Bitcoin entspricht der letzten Gleichung im vorherigen Bild.

In dem nächsten Abschnitt dieses Kurses werden wir Kurven verwenden, die über dem Körper der reellen Zahlen liegen, um das Verständnis zu erleichtern.

### Berechnung des öffentlichen Schlüssels aus dem privaten Schlüssel

![Berechnung des öffentlichen Schlüssels aus dem privaten Schlüssel](https://youtu.be/NJENwFU889Y)

Um anzufangen, tauchen wir in die Welt des Elliptic Curve Digital Signature Algorithm (ECDSA) ein. Bitcoin nutzt diesen Algorithmus für digitale Signaturen, um private und öffentliche Schlüssel zu verknüpfen. In diesem System ist der private Schlüssel eine zufällige oder pseudozufällige 256-Bit-Zahl. Die Gesamtzahl der Möglichkeiten für einen privaten Schlüssel beträgt theoretisch 2^256, aber in der Realität ist sie etwas geringer. Um genau zu sein, sind einige 256-Bit private Schlüssel für Bitcoin ungültig.

Um mit Bitcoin kompatibel zu sein, muss ein privater Schlüssel zwischen 1 und n-1 liegen, wobei n die Ordnung der elliptischen Kurve darstellt. Das bedeutet, dass die Gesamtzahl der Möglichkeiten für einen Bitcoin-privaten Schlüssel fast 1,158 x 10^77 beträgt. Um das in Perspektive zu setzen, entspricht dies etwa der Anzahl der Atome im beobachtbaren Universum.

![image](assets/image/section2/3.JPG)

Der eindeutige private Schlüssel, gekennzeichnet als k, wird dann verwendet, um einen öffentlichen Schlüssel zu bestimmen.

Der öffentliche Schlüssel, gekennzeichnet als K, ist ein Punkt auf der elliptischen Kurve, der aus dem privaten Schlüssel mithilfe von irreversiblen Algorithmen wie ECDSA abgeleitet wird. Wenn wir den privaten Schlüssel kennen, ist es sehr einfach, den öffentlichen Schlüssel zu finden. Wenn wir jedoch nur den öffentlichen Schlüssel haben, ist es unmöglich, den privaten Schlüssel zurückzufinden. Diese Unumkehrbarkeit ist der Grundpfeiler der Sicherheit der Bitcoin-Wallet.

Der öffentliche Schlüssel hat eine Länge von 512 Bits, da er einem Punkt auf der Kurve mit einer x-Koordinate von 256 Bits und einer y-Koordinate von 256 Bits entspricht. Er kann jedoch auf eine 264-Bit-Zahl komprimiert werden.

![image](assets/image/section2/4.JPG)
Der generative Punkt (G) ist der Punkt auf der Kurve, von dem aus alle öffentlichen Schlüssel im Bitcoin-Protokoll generiert werden. Er hat spezifische x- und y-Koordinaten, die normalerweise in hexadezimaler Form dargestellt werden. Für secp256k1 sind die Koordinaten von G in hexadezimaler Form:

- `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
- `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

Dieser Punkt ist nützlich, um alle öffentlichen Schlüssel abzuleiten. Um den öffentlichen Schlüssel K zu berechnen, multipliziert man einfach den Punkt G mit dem privaten Schlüssel k, wie folgt: K = k.G

Nun werden wir untersuchen, wie man Punkte auf elliptischen Kurven addiert und multipliziert.

#### Addition und Verdopplung von Punkten auf elliptischen Kurven

##### Addition von zwei Punkten M + L

Eine bemerkenswerte Eigenschaft elliptischer Kurven ist, dass eine nicht-vertikale Linie, die die Kurve an zwei Punkten schneidet, sie auch an einem dritten Punkt schneidet, der in unserem Beispiel als Punkt O bezeichnet wird. Diese Eigenschaft wird verwendet, um den Punkt U zu bestimmen, der das Gegenteil von Punkt O ist.

M + L = U

![image](assets/image/section2/5.JPG)

##### Addition eines Punktes zu sich selbst = Verdopplung des Punktes

Die Addition eines Punktes G zu sich selbst erfolgt durch das Zeichnen einer Tangente an der Kurve an diesem Punkt. Diese Tangente schneidet die Kurve gemäß den Eigenschaften elliptischer Kurven zwangsläufig an einem zweiten eindeutigen Punkt -J. Das Gegenteil dieses Punktes, J, ist das Ergebnis der Addition des Punktes G zu sich selbst.
G + G = J

Übrigens ist der Punkt G der Ausgangspunkt für die Berechnung aller öffentlichen Schlüssel der Benutzer des Bitcoin-Systems.

![image](assets/image/section2/6.JPG)

#### Skalare Multiplikation auf elliptischen Kurven

Die skalare Multiplikation eines Punktes mit n besteht darin, diesen Punkt n-mal zu sich selbst zu addieren.

Ähnlich wie bei der Verdopplung eines Punktes erfolgt die skalare Multiplikation des Punktes G mit einem Punkt n durch das Zeichnen einer Tangente an der Kurve am Punkt G. Diese Tangente schneidet die Kurve gemäß den Eigenschaften elliptischer Kurven zwangsläufig an einem zweiten eindeutigen Punkt -2G. Das Gegenteil dieses Punktes, 2G, ist das Ergebnis der Addition des Punktes G zu sich selbst.

Wenn n = 4 ist, wiederholt man den Vorgang, bis man zu 4G gelangt.

![image](assets/image/section2/7.JPG)

Hier ist ein Beispiel für die Berechnung von 3G:

![image](assets/image/section2/8.JPG)
Diese Operationen auf den Punkten einer elliptischen Kurve bilden die Grundlage für die Berechnung öffentlicher Schlüssel. Die Ableitung eines öffentlichen Schlüssels aus dem Wissen über den privaten Schlüssel ist sehr einfach. Ein öffentlicher Schlüssel ist ein Punkt auf der elliptischen Kurve, das Ergebnis unserer Addition und Verdoppelung des Punktes G k Mal. Mit k = privater Schlüssel.

In diesem Beispiel:

- Der private Schlüssel k = 4
- Der öffentliche Schlüssel K = kG = 4G

![image](assets/image/section2/9.JPG)

Wenn der private Schlüssel k bekannt ist, ist es einfach, den öffentlichen Schlüssel K zu berechnen. Es ist jedoch unmöglich, den privaten Schlüssel aus dem öffentlichen Schlüssel zurückzufinden. Ist dies das Ergebnis einer Punktaddition oder -verdoppelung?

In unserem nächsten Kurs werden wir untersuchen, wie eine digitale Signatur mit dem ECDSA-Algorithmus und einem privaten Schlüssel zum Ausgeben von Bitcoins erstellt wird.

## Mit dem privaten Schlüssel signieren

![Mit dem privaten Schlüssel signieren](https://youtu.be/h2hIyGgPqkM)

Der Prozess der digitalen Signatur ist eine Schlüsselmethode, um zu beweisen, dass Sie der Inhaber eines privaten Schlüssels sind, ohne ihn offenlegen zu müssen. Dies wird durch Verwendung des ECDSA-Algorithmus erreicht, der die Bestimmung einer eindeutigen Nonce, die Berechnung einer spezifischen Zahl V und die Erstellung einer digitalen Signatur aus zwei Teilen, S1 und S2, umfasst.
Es ist entscheidend, immer eine eindeutige Nonce zu verwenden, um Sicherheitsangriffe zu vermeiden. Ein bekanntes Beispiel dafür, was passieren kann, wenn diese Regel nicht eingehalten wird, ist der Fall des Hacks der PlayStation 3, der aufgrund der Wiederverwendung der Nonce kompromittiert wurde.

![](assets/image/section2/10.JPG)

Schritte:

- Bestimmen Sie eine Nonce v, das heißt, eine eindeutige zufällige Zahl.
  Nonce = Number Only Used Once.
  Es wird von der Person bestimmt, die die Signatur erstellt.
- Berechnen Sie durch Addition und Verdoppelung des Punktes auf der elliptischen Kurve vom Punkt G aus die Position von V auf der elliptischen Kurve.
  So dass V = v.G
  x und y sind die Koordinaten von V in der Ebene.
- Berechnen Sie S1.
  S1 = x mod n mit n = die Ordnung der Kurve und x eine Koordinate von V in der Ebene.
  Hinweis: Die Anzahl der möglichen öffentlichen Schlüssel ist größer als die Anzahl der Punkte auf der elliptischen Kurve im endlichen Körper der positiven ganzen Zahlen, der in Bitcoin verwendet wird.
  Die Ordnung der Kurve entspricht nur den Möglichkeiten, die der öffentliche Schlüssel auf der Kurve annehmen kann.
- Berechnen Sie S2.
  H(Tx) = Hash der Transaktion
  k = der private Schlüssel
- Berechnen Sie die Signatur: die Konkatenation von S1 + S2.
- Berechnen Sie P, die Überprüfung der Signatur.
  K = der öffentliche Schlüssel
  Par exemple, um den öffentlichen Schlüssel 3G zu erhalten, zeichnen Sie eine Tangente am Punkt G, berechnen Sie das Gegenteil von -G, um 2G zu erhalten, und addieren Sie dann G und 2G. Um eine Transaktion durchzuführen, müssen Sie beweisen, dass Sie die Zahl 3 kennen, indem Sie die mit dem öffentlichen Schlüssel 3G verbundenen Bitcoins freischalten.

Um eine digitale Signatur zu erstellen und zu beweisen, dass Sie den privaten Schlüssel kennen, der mit dem öffentlichen Schlüssel 3G verbunden ist, berechnen Sie zuerst eine Zufallszahl (Nonce) und dann den Punkt V, der mit dieser Zufallszahl verbunden ist (im gegebenen Beispiel ist dies 4G). Anschließend berechnen Sie den Punkt T, indem Sie den öffentlichen Schlüssel 3G und den Punkt V addieren, was 7G ergibt.

![image](assets/image/section2/11.JPG)

Lassen Sie uns den Prozess der digitalen Signatur vereinfachen.
Auf dem vorherigen Bild ist der private Schlüssel k = 3.
Wir können leicht den öffentlichen Schlüssel K berechnen, der mit diesem privaten Schlüssel verbunden ist: K = 3G.
Dann generieren wir pseudozufällig eine Zufallszahl (Nonce): v = 4.
Aus dieser Zufallszahl können wir V berechnen, sodass V = v.G = 4G.

Aus diesem Punkt V berechnen wir den Punkt T wie folgt:
T = t.G = 7G (mit t = 7).

Es ist Zeit, die digitale Signatur zu überprüfen.

Die Überprüfung einer digitalen Signatur ist ein entscheidender Schritt bei der Verwendung des ECDSA-Algorithmus, der die Echtheit einer signierten Nachricht bestätigt, ohne den privaten Schlüssel des Absenders zu benötigen. Hier ist, wie dies im Detail abläuft:

In unserem Beispiel haben wir zwei wichtige Werte: t und V.
t ist ein numerischer Wert (in diesem Beispiel 7), und V ist ein Punkt auf der elliptischen Kurve (hier durch 4G dargestellt). Diese Werte werden bei der Erstellung der digitalen Signatur erzeugt und anschließend mit der Nachricht gesendet, um die Überprüfung zu ermöglichen.

Wenn der Verifizierer die Nachricht erhält, erhält er auch diese beiden Werte, t und V.

Hier sind die Schritte, die der Verifizierer zur Validierung der Signatur durchführt:

1. Er berechnet zuerst den Hash-Wert der Nachricht, den wir H nennen.
2. Anschließend berechnet er u1 und u2. Dazu verwendet er die folgenden Formeln:
   - u1 = H /\* (S2)^-1 mod n
   - u2 = T /\* (S2)^-1 mod n
     Dabei ist S2 der zweite Teil der digitalen Signatur, n ist die Ordnung der elliptischen Kurve und (S2)^-1 ist das Inverse von S2 mod n.
3. Der Verifizierer berechnet dann einen Punkt P' auf der elliptischen Kurve mit der Formel: P' = u1 _ G + u2 _ K
   - G ist der Generierungspunkt der Kurve
   - K ist der öffentliche Schlüssel des Absenders
4. Der Verifikator berechnet dann I, was einfach die x-Koordinate des Punktes P' modulo n ist. 5. Schließlich bestätigt der Verifikator, dass I' gleich t ist. Wenn dies der Fall ist, wird die Signatur als gültig betrachtet. Wenn dies nicht der Fall ist, ist die Signatur ungültig.

Dieses Verfahren stellt sicher, dass nur der Absender, der den entsprechenden privaten Schlüssel besitzt, eine Signatur erzeugen konnte, die diesen Überprüfungsprozess besteht.

![image](assets/image/section2/12.JPG)

Vereinfacht ausgedrückt: Derjenige, der die Signatur erstellt, liefert demjenigen, der die Überprüfung durchführt, die Zahl t (in unserem Beispiel t = 7) und den Punkt V.

Es ist unmöglich, den öffentlichen oder privaten Schlüssel aus der Zahl 7 und der Zahl V zu bestimmen.

Die Schritte zur Überprüfung der digitalen Signatur sind wie folgt:

- Auf der Kurve addiert er den Punkt des öffentlichen Schlüssels mit dem Punkt V, um den Punkt T' zu erhalten.
- Er berechnet die Zahl t.G
- Er überprüft, ob das Ergebnis von t.G gleich der Zahl T' ist.

Zusammenfassend ist die Überprüfung einer digitalen Signatur ein wesentlicher Vorgang bei Bitcoin-Transaktionen. Sie gewährleistet, dass die signierte Nachricht während der Übertragung nicht verändert wurde und dass der Absender tatsächlich im Besitz des privaten Schlüssels ist. Diese Methode der digitalen Authentifizierung basiert auf komplexen mathematischen Prinzipien, insbesondere der elliptischen Kurvenarithmetik, und gewährleistet gleichzeitig die Vertraulichkeit des privaten Schlüssels. Sie bietet eine solide Sicherheitsgrundlage für kryptografische Transaktionen.

Die Verwaltung dieser Schlüssel und deren Erstellung ist jedoch eine weitere wesentliche Frage bei Bitcoin. Wie generiert man ein neues Schlüsselpaar? Wie organisiert man eine Vielzahl von Schlüsseln sicher und effizient? Wie stellt man sie bei Bedarf wieder her?

Um diese Fragen zu beantworten und Ihr Verständnis für die Sicherheit der Kryptographie zu vertiefen, wird sich unser nächster Kurs auf das Konzept der Hierarchischen Deterministischen Wallets (HD Wallets) und die Verwendung von mnemonischen Phrasen konzentrieren. Diese Mechanismen bieten elegante Möglichkeiten, Ihre Kryptowährungsschlüssel effizient zu verwalten und die Sicherheit zu stärken.

# Die mnemonische Phrase

## Entwicklung von Bitcoin-Wallets

![Entwicklung von Bitcoin-Wallets](https://youtu.be/6tmu1R9cXyk)

Die Hierarchische Deterministische Wallet, oder auch HD Wallet genannt, spielt eine wichtige Rolle im Kryptowährungsökosystem. Der Begriff "Wallet" mag für Neulinge in diesem Bereich irreführend sein, da er nicht den Besitz von Geld oder Währungen impliziert. Stattdessen bezieht er sich auf eine Sammlung von privaten kryptographischen Schlüsseln.
Die ersten Wallets waren Software, die pseudozufällig generierte private Schlüssel enthielten, die keine Verbindung zueinander hatten. Diese Wallets werden "Just a Bunch Of Keys" (JBOK) genannt.
Da die Schlüssel keine Verbindung zueinander haben, muss der Benutzer für jedes neu generierte Schlüsselpaar eine neue Sicherung erstellen.
Entweder verwendet der Benutzer immer dasselbe Schlüsselpaar und verliert an Vertraulichkeit, oder er generiert neue Schlüsselpaare zufällig und muss daher eine neue Sicherung dieser Schlüssel erstellen.

![image](assets/image/section3/0.JPG)

Die Komplexität der Verwaltung dieser Schlüssel wird jedoch durch eine Reihe von Protokollen, sogenannten Bitcoin Improvement Proposals (BIP), ausgeglichen. Diese Upgrade-Vorschläge sind der Kern der Funktionalität und Sicherheit von HD-Wallets. Zum Beispiel hat das [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), das 2012 eingeführt wurde, die Art und Weise, wie diese Schlüssel generiert und gespeichert werden, revolutioniert, indem es das Konzept der deterministischen und hierarchischen Schlüsselableitung eingeführt hat. Die Idee besteht darin, alle Schlüssel deterministisch und hierarchisch aus einer einzigen Information abzuleiten: dem Seed. Auf diese Weise wird der Prozess der Sicherung dieser Schlüssel erheblich vereinfacht, während ihr Sicherheitsniveau erhalten bleibt.

![image](assets/image/section3/1.JPG)

Später führte das [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) eine bedeutende Innovation ein: die 24-Wort-Mnemonic-Phrase. Dieses System verwandelt eine komplexe und schwer zu merkende Zahlenfolge in eine Reihe gewöhnlicher Wörter, die viel einfacher zu merken und zu speichern sind. Darüber hinaus schlug das [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) vor, eine zusätzliche Passphrase hinzuzufügen, um die Sicherheit der einzelnen Schlüssel zu erhöhen. Diese aufeinanderfolgenden Verbesserungen führten zu den Standards BIP43 und BIP44, die die Struktur und Hierarchie von HD-Wallets standardisierten und diese Wallets für die breite Öffentlichkeit zugänglicher und einfacher zu bedienen machten.

In den folgenden Abschnitten werden wir tiefer in die Funktionsweise von HD-Wallets eintauchen. Wir werden die Prinzipien der Schlüsselableitung behandeln und die grundlegenden Konzepte von Entropie und Zufallszahlengenerierung untersuchen, die für die Sicherheit Ihrer HD-Wallets unerlässlich sind.

## Zusammenfassung

Es ist wichtig, die zentrale Rolle von BIP32 und BIP39 bei der Gestaltung und Sicherung von HD-Wallets hervorzuheben. Diese Protokolle ermöglichen die Generierung einer Vielzahl von Schlüsseln aus einem einzigen Seed, der als zufällige oder pseudo-zufällige Zahl betrachtet wird. Heutzutage werden diese Standards von den meisten Kryptowährungs-Wallets übernommen, egal ob sie für eine einzelne Kryptowährung oder für mehrere Währungstypen geeignet sind.

## Entropie und Zufallszahl

![Entropie und Zufallszahl](https://youtu.be/k18yH18w2TE)

Die Sicherheit der privaten Schlüssel im Bitcoin-Ökosystem ist von entscheidender Bedeutung. Sie sind das Fundament, das die Sicherheit von Bitcoin-Transaktionen gewährleistet. Um Schwachstellen aufgrund von Vorhersagbarkeit zu vermeiden, müssen diese Schlüssel wirklich zufällig generiert werden, was sich schnell als mühsame Aufgabe erweisen kann. Das Problem ist, dass es in der Informatik unmöglich ist, eine wirklich zufällige Zahl zu generieren, da sie zwangsläufig aus einem deterministischen Prozess stammt - einem Code.
Daher ist es wichtig, sich über verschiedene Zufallszahlengeneratoren (RNG) zu informieren. Die Arten von RNG variieren von Pseudo-Zufallszahlengeneratoren (PRNG) über echte Zufallszahlengeneratoren (TRNG) bis hin zu PRNGs, die eine Entropiequelle integrieren.

Entropie bezieht sich auf den "Unordnungszustand" eines Systems. Mit Hilfe einer externen Entropie, also einer externen Informationsquelle, kann ein Zufallszahlengenerator verwendet werden, um eine Zufallszahl zu erhalten.

![image](assets/image/section3/2.JPG)

Lassen Sie uns gemeinsam die Funktionsweise eines Pseudo-Zufallszahlengenerators (PRNG) betrachten.

Er nimmt einen Seed als Eingabe, der dem internen Zustand 0 entspricht.
Auf diesem internen Zustand wird eine Transformationsfunktion angewendet und das Ergebnis, eine pseudo-zufällige Zahl, entspricht dem internen Zustand 1.
Auf diesem internen Zustand 1 wird erneut eine Transformationsfunktion angewendet, die zu einer neuen Zufallszahl = interner Zustand 2 führt.
Und so weiter.

Der Hauptnachteil ist, dass jeder identische Seed immer das gleiche Ergebnis liefert. Und auch wenn wir das Ergebnis der Anfangstransformationsfunktionen kennen, können wir die Zufallszahl am Ende des Prozesses wiederherstellen.

Ein Beispiel für eine Transformationsfunktion ist die PBKDF2-Funktion.

**Zusammenfassend muss ein kryptographisch sicherer PRNG:**

- statistisch zufällig sein
- unvorhersagbar sein
- widerstandsfähig sein, auch wenn die Ergebnisse bekannt sind
- eine ausreichend lange Periode haben

![image](assets/image/section3/3.JPG)
Im Fall von Bitcoin werden private Schlüssel aus einer einzigen Information generiert, die am Anfang der Brieftasche steht. Diese Information ermöglicht eine deterministische und hierarchische Ableitung von Kinderschlüsselpaaren. Die Entropie ist das Fundament jeder HD-Brieftasche, obwohl es keinen Standard für die Generierung dieser Zufallszahl gibt. Daher ist die Generierung von Zufallszahlen ein wichtiges Anliegen zur Sicherung von Bitcoin-Transaktionen.
![image](assets/image/section3/4.JPG)

Die Überprüfungsphase der Schlüsselgenerierung ist entscheidend, um die Sicherheit und Authentizität der Zufallszahlengenerierung zu gewährleisten, ein grundlegender Schritt, um jegliche mit der Vorhersagbarkeit verbundene Schwachstelle zu verhindern. Es wird daher dringend empfohlen, Open-Source-Brieftaschen zu verwenden, um diese Überprüfung zu ermöglichen.

Es ist jedoch wichtig zu beachten, dass einige Hardware-Brieftaschen "Closed Source" sein können, was die Überprüfung der Zufallszahlengenerierung unmöglich macht. Eine mögliche Umgehung wäre die Generierung einer mnemonischen Phrase mit Würfeln, obwohl dieser Ansatz gewisse Risiken mit sich bringen kann.

Die Verwendung einer zufällig generierten Passphrase kann dazu beitragen, diese Risiken zu mildern.

Letztendlich spielt Zufall eine zentrale Rolle in der Kryptographie und Informatik, und die Fähigkeit, Zufall auf sichere Weise zu generieren, ist entscheidend, um die Sicherheit privater Schlüssel und Bitcoin-Transaktionen zu gewährleisten. Die Entropie, die im Herzen der Bitcoin HD-Brieftasche steht, ist für ihre Sicherheit unerlässlich. In unserer nächsten Lektion werden wir dieses Thema weiter erkunden und genauer darauf eingehen, wie die Entropie zur Sicherheit von HD-Brieftaschen beiträgt.

## Die mnemonische Phrase

![Die mnemonische Phrase](https://youtu.be/uJERqH9Xp7I)

Die Sicherheit einer Bitcoin-Brieftasche ist eine Hauptanliegen für alle Benutzer. Eine wesentliche Methode zur Sicherung der Brieftasche besteht darin, eine mnemonische Phrase basierend auf Entropie und Prüfsumme zu generieren.

![image](assets/image/section3/5.JPG)

Um von Entropie zu einer mnemonischen Phrase zu gelangen, berechnet man einfach die Prüfsumme der Entropie und fügt Entropie und Prüfsumme zusammen.

Sobald die Entropie generiert ist, wird die SHA256-Funktion auf die Entropie angewendet, um einen Hash zu erstellen. Die ersten 8 Bits des Hashes werden als Prüfsumme verwendet.
Die mnemonische Phrase ist das Ergebnis der Entropie, die mit der Prüfsumme addiert wird.

Die Prüfsumme gewährleistet die Überprüfung der Genauigkeit der Wiederherstellungsphrase. Ohne diese Prüfsumme könnte ein Fehler in der Phrase zur Erstellung einer anderen Brieftasche führen und somit zum Verlust der Gelder führen. Die Prüfsumme wird erhalten, indem die Entropie durch die SHA256-Funktion geleitet wird und die ersten 8 Bits des Hashes extrahiert werden.
![image](assets/image/section3/6.JPG)
Es gibt verschiedene Standards für die mnemonische Phrase, abhängig von der Entropiegröße. Der am häufigsten verwendete Standard für eine Wiederherstellungsphrase mit 24 Wörtern hat eine Entropie von 256 Bits. Die Größe der Prüfsumme wird durch Teilen der Entropiegröße durch 32 bestimmt.

Zum Beispiel erzeugt eine Entropie von 256 Bits eine Prüfsumme von 8 Bits. Die Konkatenation von Entropie und Prüfsumme führt dann zu den jeweiligen Größen von 128 Bits, 160 Bits usw. Abhängig von der Entropiegröße enthält die Wiederherstellungsphrase 12 Wörter für 128 Bits, 15 Wörter für 160 Bits und 24 Wörter für 256 Bits.

**Codierung der mnemonischen Phrase:**

![image](assets/image/section3/7.JPG)

Die letzten 8 Bits entsprechen der Prüfsumme.
Jedes 11-Bit-Segment wird in Dezimalzahlen umgewandelt.
Jede Dezimalzahl entspricht einem Wort aus einer Liste von 2048 Wörtern im BIP39. Es ist wichtig zu beachten, dass kein Wort die ersten vier Buchstaben in derselben Reihenfolge enthält.

Es ist entscheidend, die 24-Wort-Wiederherstellungsphrase zur Sicherung der Integrität der Bitcoin-Brieftasche zu speichern. Die beiden am häufigsten verwendeten Standards basieren auf einer Entropie von 128 oder 256 Bits und einer Konkatenation von 12 oder 24 Wörtern. Das Hinzufügen einer Passphrase ist eine zusätzliche Option, um die Sicherheit der Brieftasche zu stärken.

Zusammenfassend ist die Generierung einer mnemonischen Phrase zur Sicherung einer Bitcoin-Brieftasche ein entscheidender Prozess. Es ist wichtig, die Standards der mnemonischen Phrase entsprechend der Entropiegröße einzuhalten. Das Speichern der 24-Wort-Wiederherstellungsphrase ist entscheidend, um einen Verlust von Mitteln zu verhindern.

## Die Passphrase

![Die Passphrase](https://youtu.be/dZkOYO7MXwc)

Die Passphrase ist ein zusätzliches Kennwort, das in eine Bitcoin-Brieftasche integriert werden kann, um ihre Sicherheit zu erhöhen. Ihre Verwendung ist optional und liegt im Ermessen des Benutzers. Durch Hinzufügen beliebiger Informationen, die zusammen mit der mnemonischen Phrase verwendet werden, um den Wallet-Samen zu berechnen, stärkt die Passphrase die Sicherheit der Brieftasche.

![image](assets/image/section3/8.JPG)

Die Passphrase ist ein optionaler kryptografischer Salt mit einer vom Benutzer gewählten Größe. Sie verbessert die Sicherheit einer HD-Brieftasche, indem sie beliebige Informationen hinzufügt, die, wenn sie mit der mnemonischen Phrase kombiniert werden, den Seed berechnen.
Wenn es bei der Erstellung einer Brieftasche festgelegt wird, ist es erforderlich, um alle Schlüssel der Brieftasche abzuleiten. Die Funktion pbkdf2 wird verwendet, um den Seed aus der Passphrase zu generieren. Dieser Seed ermöglicht die Ableitung aller Kinderschlüsselpaare der Brieftasche. Wenn die Passphrase geändert wird, wird die Bitcoin-Brieftasche vollständig unterschiedlich.

Die Passphrase ist ein wesentliches Werkzeug zur Stärkung der Sicherheit von Bitcoin-Brieftaschen. Sie kann die Anwendung verschiedener Sicherheitsstrategien ermöglichen. Zum Beispiel kann sie verwendet werden, um Duplikate zu erstellen und das Sichern der mnemonischen Phrase zu erleichtern. Sie kann auch die Sicherheit der Brieftasche verbessern, indem sie die mit der zufälligen Generierung der mnemonischen Phrase verbundenen Risiken verringert.

Eine effektive Passphrase sollte lang (20 bis 40 Zeichen) und vielfältig sein (Großbuchstaben, Kleinbuchstaben, Zahlen und Symbole verwenden). Sie sollte nicht direkt mit dem Benutzer oder seiner Umgebung verbunden sein. Es ist sicherer, eine zufällige Zeichenfolge anstelle eines einfachen Wortes als Passphrase zu verwenden.

![image](assets/image/section3/9.JPG)

Eine Passphrase ist sicherer als ein einfaches Passwort. Die ideale Passphrase ist lang, vielfältig und zufällig. Sie kann die Sicherheit einer Brieftasche oder einer Hot Wallet stärken. Sie kann auch zur Erstellung redundanter und sicherer Backups verwendet werden.

Es ist wichtig, die Passphrase-Backups sorgfältig aufzubewahren, um den Zugriff auf die Brieftasche nicht zu verlieren. Eine Passphrase ist eine Option für eine HD-Brieftasche. Sie kann zufällig mit Würfeln oder einem anderen Pseudozufallszahlengenerator generiert werden.

# Erstellung einer Bitcoin-Brieftasche

## Erstellung des Seeds und des Master-Schlüssels

![Erstellung des Seeds und des Master-Schlüssels](https://youtu.be/56yAt_JDWhY)

In diesem Teil des Kurses werden wir die Schritte zur Ableitung einer HD-Brieftasche (Hierarchical Deterministic Wallet) erkunden, die die hierarchische und deterministische Erstellung und Verwaltung von privaten und öffentlichen Schlüsseln ermöglicht.

![image](assets/image/section4/0.JPG)

Das Fundament der HD-Brieftasche basiert auf zwei wesentlichen Elementen: der mnemonischen Phrase und der Passphrase (optionales zusätzliches Passwort). Zusammen bilden sie den Seed, eine alphanumerische Sequenz von 512 Bits, die als Grundlage für die Ableitung der Brieftaschenschlüssel dient. Aus diesem Seed können alle Kinderschlüsselpaare der Bitcoin-Brieftasche abgeleitet werden. Der Seed ist der Schlüssel, um auf alle mit der Brieftasche verbundenen Bitcoins zuzugreifen, unabhängig davon, ob Sie eine Passphrase verwenden oder nicht.

![image](assets/image/section4/1.JPG)
Um den Seed zu erhalten, verwenden wir die Funktion pbkdf2 (Password-Based Key Derivation Function 2) mit dem mnemonischen Satz und dem Passwort. Die Ausgabe von pbkdf2 ist ein 512-Bit Seed.
Ausgehend vom Seed ist es möglich, den Master-Private-Key und den Chain-Code mithilfe des HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512) Algorithmus zu bestimmen. Dieser Algorithmus erfordert eine Nachricht und einen Schlüssel als Eingabe, um ein Ergebnis zu generieren. Der Master-Private-Key wird aus dem Seed und dem Satz "Bitcoin SEED" berechnet. Dieser Satz ist für alle Ableitungen aller HD-Wallets identisch und gewährleistet somit eine Konsistenz zwischen den Wallets.

Ursprünglich war die SHA-512 Funktion nicht im Bitcoin-Protokoll implementiert, daher verwenden wir HMAC SHA-512. Die Verwendung von HMAC SHA-512 mit dem Satz "Bitcoin SEED" zwingt den Benutzer zur Generierung einer spezifischen Bitcoin-Wallet. Das Ergebnis von HMAC SHA-512 ist eine 512-Bit-Zahl, die in zwei Teile aufgeteilt ist: die linken 256 Bits repräsentieren den Master-Private-Key, während die rechten 256 Bits den Master-Chain-Code repräsentieren.

![image](assets/image/section4/2.JPG)

Der Master-Private-Key ist der übergeordnete Schlüssel für alle zukünftigen Schlüssel des Wallets, während der Master-Chain-Code bei der Ableitung der Kinderschlüssel eine Rolle spielt. Es ist wichtig zu beachten, dass es unmöglich ist, ein Paar von Kinderschlüsseln abzuleiten, ohne den entsprechenden Chain-Code des übergeordneten Paares zu kennen.

Ein Schlüsselpaar in der Wallet besteht aus einem Private-Key, einem Public-Key und einem Chain-Code. Der Chain-Code ermöglicht es, eine Zufallsquelle in der Ableitung der Kinderschlüssel einzuführen und jedes Schlüsselpaar zu isolieren, um Informationslecks zu vermeiden.

Es ist wichtig zu betonen, dass der Master-Private-Key der erste aus dem Seed abgeleitete Private-Key ist und keine Verbindung zu den erweiterten Schlüsseln der Wallet hat.

Im nächsten Kurs werden wir uns ausführlich mit den erweiterten Schlüsseln wie xPub, xPRV, zPub befassen und verstehen, warum sie verwendet werden und wie sie aufgebaut sind.

## Erweiterte Schlüssel

![Erweiterte Schlüssel](https://youtu.be/TRz760E_zUY)

In diesem Teil des Kurses werden wir uns mit den erweiterten Schlüsseln (xPub, zPub, yPub) und ihren Präfixen befassen, die eine wichtige Rolle bei der Ableitung von Kinderschlüsseln in einer HD-Wallet (Hierarchical Deterministic Wallet) spielen.

![image](assets/image/section4/3.JPG)
Erweiterte Schlüssel unterscheiden sich von Masterschlüsseln. Eine HD-Wallet erzeugt eine mnemonische Phrase und einen Seed, um den Masterschlüssel und den Masterkettencode zu erhalten. Erweiterte Schlüssel werden zur Ableitung von Kindschlüsseln verwendet und benötigen sowohl den übergeordneten Schlüssel als auch den zugehörigen Kettencode. Ein erweiterter Schlüssel kombiniert diese beiden Informationen, um den Ableitungsprozess zu vereinfachen.
![image](assets/image/section4/4.JPG)

Erweiterte öffentliche Schlüssel können nur normale öffentliche Kindschlüssel ableiten, während erweiterte private Schlüssel sowohl öffentliche als auch private Kindschlüssel ableiten können, und zwar sowohl über eine normale als auch über eine gehärtete Ableitung.
Die gehärtete Ableitung ist die Ableitung vom privaten Elternschlüssel. Die normale Ableitung entspricht der Ableitung vom öffentlichen Elternschlüssel.

Die Verwendung von erweiterten Schlüsseln mit dem Präfix XPUB ermöglicht die Ableitung neuer Adressen, ohne auf die entsprechenden privaten Schlüssel zurückgreifen zu müssen, und bietet somit eine höhere Sicherheit. Die mit erweiterten Schlüsseln verknüpften Metadaten liefern wichtige Informationen über ihre Rolle und ihre Position in der Schlüsselhierarchie.

Erweiterte Schlüssel werden durch spezifische Präfixe (XPRV, XPUB, YPUB, ZPUB) identifiziert, die angeben, ob es sich um einen privaten oder öffentlichen erweiterten Schlüssel handelt, sowie seinen spezifischen Zweck. Zu den Metadaten, die mit einem erweiterten Schlüssel verknüpft sind, gehören die Version (Präfix), die Tiefe, der Fingerabdruck des öffentlichen Schlüssels, der Index und die Nutzlast (Kettencode und übergeordneter Schlüssel).

![image](assets/image/section4/5.JPG)

Die Version entspricht dem Schlüsseltyp: xpub, xprv, ...

Die Tiefe entspricht der Anzahl der Ableitungen zwischen Eltern und Kind, die es seit dem Masterschlüssel gegeben hat.

Der übergeordnete Fingerabdruck sind die ersten 4 Bytes des Hashes 160 des übergeordneten Schlüssels.

Der Index ist die Nummer des Paares, das zur Erzeugung des erweiterten Schlüssels unter seinen Schwestern verwendet wird. (Schwestern = Schlüssel mit der gleichen Tiefe)
Beispiel: Wenn wir den xpub unseres dritten Kontos ableiten wollen, ist sein Index 2 (da Index bei 0 beginnt).

Die Nutzlast besteht aus dem Stringcode (32 Byte) und dem übergeordneten Schlüssel (33 Byte).

Komprimierte öffentliche Schlüssel haben eine Größe von 33 Byte, während rohe öffentliche Schlüssel 512 Bit lang sind. Komprimierte öffentliche Schlüssel behalten die gleichen Informationen wie die Rohschlüssel, sind aber kleiner. Erweiterte Schlüssel haben eine Größe von 82 Byte und ihr Präfix wird durch eine Hexadezimalumwandlung zur Basis 58 dargestellt. Die Prüfsumme wird mithilfe der Hashfunktion HASH256 berechnet.

![image](assets/image/section4/6.JPG)
Die verstärkten Ableitungen beginnen bei den Indizes, die Potenzen von 2 (2^31) sind. Es ist interessant zu beachten, dass die am häufigsten verwendeten Präfixe xpub und zpub sind, die jeweils den Legacy-Standard und SegWit v1 und SegWit v0 entsprechen.

In unserem nächsten Kurs werden wir uns mit der Ableitung von Kinderschlüsselpaaren unter Verwendung des erworbenen Wissens über erweiterte Schlüssel und den Master-Schlüssel des Wallets befassen.

## Ableitung von Kinderschlüsselpaaren

![Ableitung von Kinderschlüsselpaaren](https://youtu.be/FXhI-GmE9Aw)

Zur Erinnerung haben wir die Berechnung des Seeds und des Master-Schlüssels behandelt, die die ersten wesentlichen Elemente für die Hierarchisierung und Ableitung des HD-Wallets (Hierarchical Deterministic Wallet) darstellen. Der Seed, der eine Länge von 128 bis 256 Bits hat, wird zufällig generiert oder aus einem geheimen Satz abgeleitet. Er spielt eine deterministische Rolle bei der Ableitung aller anderen Schlüssel. Der Master-Schlüssel ist der erste Schlüssel, der aus dem Seed abgeleitet wird, und er ermöglicht die Ableitung aller anderen Kinderschlüsselpaare.

Der Master-Chain-Code spielt eine wichtige Rolle bei der Wiederherstellung des Wallets aus dem Seed. Es ist zu beachten, dass alle aus demselben Seed abgeleiteten Schlüssel denselben Master-Chain-Code haben werden.

![Bild](assets/image/section4/7.JPG)

Die Hierarchisierung und Ableitung des HD-Wallets ermöglichen eine effizientere Verwaltung von Schlüsseln und Wallet-Strukturen. Erweiterte Schlüssel ermöglichen die Ableitung eines Kinderschlüsselpaars aus einem Elternschlüsselpaar unter Verwendung spezifischer mathematischer Berechnungen und Algorithmen.

Es gibt verschiedene Arten von Kinderschlüsselpaaren, darunter verstärkte Schlüssel und normale Schlüssel. Der erweiterte öffentliche Schlüssel ermöglicht nur die Ableitung normaler öffentlicher Kinderschlüssel, während der erweiterte private Schlüssel die Ableitung aller Kinderschlüssel ermöglicht, sowohl öffentlicher als auch privater, ob im normalen oder verstärkten Modus. Jedes Schlüsselpaar hat einen Index, der sie voneinander unterscheidet.

![Bild](assets/image/section4/8.JPG)

Die Ableitung von Kinderschlüsseln verwendet die HMAC-SHA512-Funktion unter Verwendung des Elternschlüssels, der mit dem Index und dem mit dem Schlüsselpaar verbundenen Chain-Code konkateniert wird. Normale Kinderschlüssel haben einen Index von 0 bis 2 hoch 31 minus 1, während verstärkte Kinderschlüssel einen Index von 2 hoch 31 bis 2 hoch 32 minus 1 haben.

![Bild](assets/image/section4/9.JPG)

![Bild](assets/image/section4/10.JPG)

Es gibt zwei Arten von Kinderschlüsselpaaren: verstärkte Paare und normale Paare. Der Prozess zur Ableitung von Kinderschlüsseln verwendet die öffentlichen Schlüssel, um die Ausgabebedingungen zu generieren, während die privaten Schlüssel zur Signatur verwendet werden. Der erweiterte öffentliche Schlüssel ermöglicht nur die Ableitung von normalen öffentlichen Kinderschlüsseln, während der erweiterte private Schlüssel die Ableitung aller Kinderschlüssel ermöglicht, sowohl öffentlicher als auch privater, im normalen oder verstärkten Modus.

![image](assets/image/section4/11.JPG)
![image](assets/image/section4/12.JPG)

Die verstärkte Ableitung verwendet den übergeordneten privaten Schlüssel, während die normale Ableitung den übergeordneten öffentlichen Schlüssel verwendet. Die HMAC-SHA512-Funktion wird für die verstärkte Ableitung verwendet, während die normale Ableitung einen 512-Bit-Hash verwendet. Der Kinderschlüssel wird erhalten, indem der Kindesprivatschlüssel mit dem Generator der elliptischen Kurve multipliziert wird.

![image](assets/image/section4/13.JPG)
![image](assets/image/section4/14.JPG)

Die Hierarchisierung und die deterministische Ableitung vieler Schlüsselpaare ermöglichen die Erstellung eines Baumschemas für die hierarchische Ableitung. Im nächsten Kurs dieses Trainings werden wir uns die Struktur der HD-Brieftasche sowie die Ableitungspfade genauer ansehen und insbesondere auf die Notation der Ableitungspfade eingehen.

## Struktur der Brieftasche und Ableitungspfade

![Struktur der Brieftasche und Ableitungspfade](https://youtu.be/etO9UxwyE2I)

In diesem Kapitel werden wir uns die Struktur des Ableitungsbaums in einer HD-Brieftasche (Hierarchical Deterministic Wallet) genauer ansehen. Wir haben bereits die Berechnung des Seeds, des Master-Schlüssels und die Ableitung der Kinderschlüsselpaare untersucht. Jetzt werden wir uns auf die Organisation der Schlüssel innerhalb der Brieftasche konzentrieren.

Die HD-Brieftasche verwendet Tiefenebenen, um die Schlüssel zu organisieren. Jede Ableitung von einem Elternpaar zu einem Kindpaar entspricht einer Tiefenebene.

![image](assets/image/section4/15.JPG)

- Tiefenebene 0 entspricht dem Master-Schlüssel und dem Master-Kettencode.

- Tiefenebene 1 wird verwendet, um Kinderschlüssel gemäß einem bestimmten Ziel abzuleiten, das durch den Index bestimmt wird. Die Ziele entsprechen den Standards BIP 84 und Segwit v0/v1.

- Tiefenebene 2 ermöglicht die Unterscheidung von Konten für verschiedene Kryptowährungen oder Netzwerke. Dadurch kann die Brieftasche entsprechend den verschiedenen Geldquellen organisiert werden. Für Bitcoin ist der Index 0.

- Tiefenebene 3 wird verwendet, um die Brieftasche in verschiedene Konten zu organisieren und so eine klarere und organisierte Struktur zu bieten.
- Die Tiefe 4 entspricht den internen und externen Ketten, die für Adressen verwendet werden, die öffentlich kommuniziert werden sollen. Index 0 ist mit der externen Kette verbunden, während Index 1 mit der internen Kette verbunden ist. Jedes Konto hat zwei Ketten: die externe Kette (0) und die interne Kette (1). Die Tiefe 4 wird auch zur Verwaltung von Skripttypen bei Multi-Signatur-Wallets verwendet.
- Die Tiefe 5 wird für Empfangsadressen in einer herkömmlichen Wallet verwendet. Im nächsten Abschnitt werden wir die Ableitung von Kinderschlüsselpaaren genauer betrachten.

![Bild](assets/image/section4/16.JPG)

Für jede Tiefe verwenden wir Indizes, um die Kinderschlüsselpaare zu unterscheiden.

Der Index ohne Apostroph entspricht dem tatsächlich verwendeten Index, während der Index mit Apostroph dem tatsächlichen Index + 2^31 entspricht. Verstärkte Ableitungen verwenden Indizes von 2^31 bis 2^32-1. Zum Beispiel entspricht der Index 44' dem tatsächlichen Index 2^31 + 44.

Um eine bestimmte Empfangsadresse zu generieren, leiten wir ein Kinderschlüsselpaar aus dem Master-Schlüssel und dem Master-Kettencode ab. Anschließend verwenden wir den Index, um die verschiedenen Kinderschlüsselpaare derselben Tiefe zu unterscheiden.

Erweiterte Schlüssel wie XPUB ermöglichen das Teilen Ihrer Wallet mit mehreren Personen. Die Ableitungskette wird verwendet, um die externe Kette (Adressen, die kommuniziert werden sollen) von der internen Kette (Wechseladressen) zu unterscheiden.

Im nächsten Kapitel werden wir uns Empfangsadressen genauer ansehen, ihre Vorteile und den Prozess zu ihrer Erstellung.

# Was ist eine Bitcoin-Adresse?

## Bitcoin-Adressen

![Bitcoin-Adressen](https://youtu.be/nqGBMjPtFNI)

![Bild](assets/image/section5/0.JPG)

In diesem Kapitel werden wir uns Empfangsadressen genauer ansehen, die eine entscheidende Rolle im Bitcoin-System spielen. Sie ermöglichen den Empfang von Geldern und werden aus privaten und öffentlichen Schlüsselpaaren generiert. Obwohl es einen Skripttyp namens Pay2PublicKey gibt, mit dem Bitcoins an einen öffentlichen Schlüssel gebunden werden können, verwenden Benutzer in der Regel lieber Empfangsadressen anstelle dieses Skripts.

Wenn ein Empfänger Bitcoins erhalten möchte, gibt er dem Sender anstelle seines öffentlichen Schlüssels eine Empfangsadresse an. Eine Adresse ist tatsächlich ein Hash eines öffentlichen Schlüssels mit einem spezifischen Format.

![Bild](assets/image/section5/1.JPG)

Es ist wichtig zu beachten, dass es nicht möglich ist, von der Adresse auf den öffentlichen Schlüssel oder vom öffentlichen Schlüssel auf den privaten Schlüssel zurückzuschließen. Die Verwendung einer Adresse reduziert die Größe der Informationen des öffentlichen Schlüssels, der ursprünglich 512 Bits beträgt.
Bitcoin-Adressen wurden zur Vereinfachung ihrer Verwendung verkleinert. Sie besitzen eine Prüfsumme, die Tippfehler erkennt und das Risiko des Verlusts von Bitcoins verringert. Öffentliche Schlüssel haben jedoch keine Prüfsumme, was bedeutet, dass Tippfehler zum Verlust der entsprechenden Mittel führen können.

Adressen bieten auch eine zweite Sicherheitsebene zwischen öffentlichen und privaten Informationen, was es schwieriger macht, den privaten Schlüssel zu übernehmen.

Es ist wichtig zu betonen, dass jede Adresse nur einmal verwendet werden sollte. Die Wiederverwendung derselben Adresse birgt Datenschutzprobleme und sollte vermieden werden.

Für Bitcoin-Adressen werden verschiedene Präfixe verwendet. Zum Beispiel entspricht BC1Q einer Segwit V0-Adresse, BC1P einer Taproot/Segwit V1-Adresse und die Präfixe 1 und 3 sind mit Pay2PublicKeyH/Pay2ScriptH-Adressen (legacy) verbunden. Im nächsten Kurs werden wir Schritt für Schritt die Ableitung einer Adresse aus einem öffentlichen Schlüssel erklären.

## Wie erstellt man eine Bitcoin-Adresse?

![Wie erstellt man eine Bitcoin-Adresse?](https://youtu.be/ewMGTN8dKjI)

In diesem Kapitel werden wir die Erstellung einer Empfangsadresse für Bitcoin-Transaktionen behandeln. Eine Empfangsadresse ist eine alphanumerische Darstellung eines komprimierten öffentlichen Schlüssels. Die Umwandlung eines öffentlichen Schlüssels in eine Empfangsadresse erfolgt in mehreren Schritten.

### Schritt 1: Komprimierung des öffentlichen Schlüssels

![Bild](assets/image/section5/14.png)

Eine Adresse wird aus einem untergeordneten öffentlichen Schlüssel abgeleitet.

Ein öffentlicher Schlüssel ist ein Punkt auf der elliptischen Kurve. Dank der Symmetrie der elliptischen Kurve hat ein Punkt auf der elliptischen Kurve eine x-Koordinate, die nur mit zwei möglichen Werten für y verbunden ist: positiv oder negativ.
Auf dem Bitcoin-Protokoll arbeiten wir jedoch mit endlichen positiven Ganzzahlen anstelle von reellen Zahlen. Um zwischen den beiden möglichen Werten von y zu unterscheiden, reicht es aus anzugeben, ob y gerade oder ungerade ist.

Die Komprimierung eines öffentlichen Schlüssels reduziert seine Größe von 520 Bits auf 264 Bits.

Wir verwenden das Präfix 0x02 für ein gerades y und 0x03 für ein ungerades y. Dies ist die komprimierte Form des öffentlichen Schlüssels.

### Schritt 2: Hashing des komprimierten öffentlichen Schlüssels

![Bild](assets/image/section5/3.JPG)

Der Hash des komprimierten öffentlichen Schlüssels wird mit der Funktion SHA256 durchgeführt. Anschließend wird die Funktion RIPEMD160 auf das Kondensat angewendet.

### Schritt 3: Die Payload = Nutzlast der Adresse.

![image](assets/image/section5/4.JPG)

Mit dem binären Kondensat von RIPEMD160(SHA256(K)) werden 5-Bit-Gruppen gebildet. Jede Gruppe wird in die Basis16 (Hexadezimal) und/oder die Basis10 umgewandelt.

### Schritt 4: Fügen Sie die Metadaten für die Berechnung der Prüfsumme mit dem Programm BCH hinzu.

![image](assets/image/section5/5.JPG)

Bei Legacy-Adressen verwenden wir den doppelten Hashwert SHA256, um die Prüfsumme der Adresse zu erzeugen. Bei Segwit V0- und V1-Adressen greifen wir jedoch auf die BCH-Checksum-Technologie zurück, um die Fehlererkennung zu gewährleisten. Das BCH-Programm ist in der Lage, Fehler mit einer äußerst geringen Fehlerwahrscheinlichkeit vorzuschlagen und zu korrigieren. Derzeit wird das BCH-Programm verwendet, um Änderungen zu erkennen und vorzuschlagen, es führt diese jedoch nicht automatisch anstelle des Nutzers durch.

Das BCH-Programm benötigt mehrere Eingabeinformationen, darunter das HRP (Human Readable Part), das erweitert werden muss. Die Erweiterung des HRP besteht darin, jeden Buchstaben in der Basis 2 gemäß seinem ASCII-Code zu kodieren. Dann, indem Sie die ersten 3 Bits des Ergebnisses für jeden Buchstaben in die Basis 10 umwandeln (im Bild blau). Fügen Sie ein Trennzeichen 0 ein. Dann verknüpfen Sie die letzten 5 Bits für jeden Buchstaben, die zuvor in die Basis 10 umgewandelt wurden (im Bild gelb).

Die Erweiterung des HRP auf die Basis 10 ermöglicht es, die letzten fünf Bits jedes Buchstabens zu isolieren, wodurch die Prüfsumme verstärkt wird.

Die Segwit V0-Version wird durch den Code 00 dargestellt und die "Payload" ist schwarz, auf der Basis 10. Darauf folgen sechs Zeichen, die für die Prüfsumme reserviert sind.

### Schritt 5: Berechnen Sie die Prüfsumme mit dem BCH-Programm.

![image](assets/image/section5/6.JPG)

Der Eintrag mit den Metadaten wird dann dem BCH-Programm vorgelegt, um die Prüfsumme in der Basis 10 zu erhalten.

Hier haben wir die Prüfsumme.

### Schritt 6: Aufbau der Adresse und Umwandlung in Bech32.

![image](assets/image/section5/7.JPG)

Durch die Verkettung von Version, Payload und Checksum wird die Adresse aufgebaut. Die Zeichen mit der Basis 10 werden dann mithilfe einer Zuordnungstabelle in bech32-Zeichen umgewandelt. Das bech32-Alphabet umfasst alle alphanumerischen Zeichen mit Ausnahme von 1, b, i und o, um Verwechslungen zu vermeiden.

### Schritt 7: Fügen Sie das HRP und das Trennzeichen hinzu.

![image](assets/image/section5/8.JPG)

In rosa die Prüfsumme.
In Schwarz die Payload = der Hash des öffentlichen Schlüssels.
In Blau die Version.
Der gesamte Betrag wird in Bech32 umgewandelt und dann wird 'bc' für Bitcoin hinzugefügt und '1' als Trennzeichen, und hier ist die Adresse.
Auf diese Weise haben wir den Prozess zum Erstellen einer Empfangsadresse durchlaufen, die Verwendung der BCH-Checksummen-Technologie sowie das Erstellen einer Adresse, die mit bc1q oder bc1p beginnt, unter Verwendung der BCH32-Variante der Bitcoin-spezifischen Base32.

## Zusammenfassung der Kryptographie für Bitcoin-Wallets

![Zusammenfassung des Trainings](https://youtu.be/NkAYoVUMvOs)

Die innerhalb des Bitcoin-Protokolls verwendeten Hash-Funktionen haben Eigenschaften, die für die Sicherheit des Protokolls erforderlich sind. Sie müssen irreversibel sein (= widerstandsfähig gegen Vorabbilder), fälschungssicher, kollisionsresistent und widerstandsfähig gegen Zweitbilder.

![Bild](assets/image/section5/11.JPG)

Eine weitere weit verbreitete kryptographische Methode im Bitcoin-Protokoll ist die Methode der digitalen Signaturen.

![Bild](assets/image/section5/12.JPG)

Im Laufe dieses Trainings haben wir uns ausführlich mit der hierarchisch deterministischen (HD) Brieftasche mit BIP32 beschäftigt. Die Entropie spielt bei dieser Art von Brieftasche eine zentrale Rolle, da sie verwendet wird, um aus einer Zufallszahl eine mnemonische Phrase zu generieren.

Diese Zufallszahl wird dann mit Hilfe der SHA256-Hash-Funktion in ein 256-Bit-Format gebracht. Die Prüfsumme entspricht den ersten 8 Bits dieses Ergebnisses. Die mnemonische Phrase ist die Konkatenation der Zufallszahl mit der Prüfsumme. Mit Hilfe der im BIP39 bereitgestellten Liste von 2048 Wörtern kann diese mnemonische Phrase in eine Reihe leicht zu merkender Wörter codiert werden. Die mnemonische Phrase sowie eine optionale Passphrase sind erforderlich, um den Wallet Seed zu generieren. Die Passphrase fungiert als kryptographisches Salz, das dem Wallet eine zusätzliche Schutzschicht hinzufügt.

Die Funktion pbkdf2 wird verwendet, um den Seed aus der mnemonischen Phrase und der Passphrase zu generieren, wobei ein HMAC-SHA512 und 2048 Iterationen verwendet werden. Aus diesem Seed werden dann der Master Key und der Master Chain Code abgeleitet, indem erneut die HMAC-SHA512-Funktion mit dem Text "bitcoin seed" verwendet wird. Der Master Private Key und der Master Chain Code sind die obersten Elemente in der Hierarchie der HD-Brieftasche.

Die Derivation eines Child Keys hängt von mehreren Faktoren ab, einschließlich des Parent Keys und des entsprechenden Chain Codes. Ein Extended Key wird durch Konkatenation eines Parent Keys mit seinem Chain Code erhalten, während ein Master Key ein separater Key ist.
Um eine Adresse abzuleiten, wird zuerst der komprimierte öffentliche Schlüssel mit SHA256 und RIPMD160 gehasht und dann eine Prüfsumme berechnet. Der doppelte SHA256-Hash wird verwendet, um die Prüfsumme im Falle eines Legacy-Standards zu berechnen, während das BCH-Programm (Bose-Chaudhuri-Hocquenghem) verwendet wird, um die Prüfsumme im Falle eines SegWit-Standards zu berechnen. Anschließend wird eine Darstellung im Base58-Format für einen Legacy-Standard verwendet, während das Bech32-Format für einen SegWit-Standard verwendet wird, um die HD-Wallet-Adresse zu erhalten.
![image](assets/image/section5/13.JPG)

Zusammenfassend haben wir uns ausführlich mit Hash-Funktionen und ihren Eigenschaften sowie mit digitalen Signaturen und elliptischen Kurven beschäftigt. Anschließend sind wir in die Welt der deterministischen hierarchischen (HD) Wallets mit BIP32 eingetaucht, wobei wir Entropie und Passphrase verwendet haben, um den Wallet-Schlüssel zu generieren. Wir haben auch gelernt, wie man Kindschlüssel ableitet und die HD-Wallet-Adresse erhält. Ich hoffe, diese Informationen waren hilfreich für Sie, und ich ermutige Sie nun, mit der Bewertung fortzufahren, um Ihr während des Crypto 301-Kurses erworbenes Wissen zu testen. Vielen Dank für Ihre Aufmerksamkeit.
