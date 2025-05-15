---
name: Mnemonic Phrase - Würfelwurf
description: Wie Sie Ihre eigene Wiederherstellungsphrase mit Würfeln generieren?
---

![cover](assets/cover.webp)

In diesem Tutorial lernen Sie, wie Sie manuell eine Wiederherstellungsphrase für eine Bitcoin-Wallet mithilfe von Würfelwürfen erstellen.

**WARNUNG:** Eine Mnemonic-Phrase auf sichere Weise zu generieren, erfordert, dass während ihrer Erstellung keine digitalen Spuren hinterlassen werden, was nahezu unmöglich ist. Andernfalls würde die Wallet eine viel zu große Angriffsfläche bieten, was das Risiko, dass Ihre Bitcoins gestohlen werden, erheblich erhöht. **Es wird daher dringend davon abgeraten, Mittel auf eine Wallet zu übertragen, die von einer Wiederherstellungsphrase abhängt, die Sie selbst generiert haben.** Selbst wenn Sie dieses Tutorial genau befolgen, besteht das Risiko, dass die Wiederherstellungsphrase kompromittiert werden könnte. **Daher sollte dieses Tutorial nicht für die Erstellung einer echten Wallet angewendet werden.** Die Verwendung einer Hardware-Wallet für diese Aufgabe ist viel weniger riskant, da sie die Phrase offline generiert und echte Kryptographen den Einsatz von qualitativen Entropiequellen berücksichtigt haben.

Dieses Tutorial kann nur zu experimentellen Zwecken für die Erstellung einer fiktiven Wallet verfolgt werden, ohne die Absicht, sie mit echten Bitcoins zu verwenden. Die Erfahrung bietet jedoch zwei Vorteile:

- Erstens ermöglicht es Ihnen, die Mechanismen an der Basis Ihrer Bitcoin-Wallet besser zu verstehen;
- Zweitens ermöglicht es Ihnen zu wissen, wie man es macht. Ich sage nicht, dass es eines Tages nützlich sein wird, aber es könnte sein!

## Was ist eine Mnemonic-Phrase?

Eine Wiederherstellungsphrase, auch manchmal "Mnemonic", "Seed-Phrase" oder "Geheimphrase" genannt, ist eine Sequenz, die üblicherweise aus 12 oder 24 Wörtern besteht und aus einer Entropiequelle auf pseudo-zufällige Weise generiert wird. Die pseudo-zufällige Sequenz wird immer mit einer Prüfsumme vervollständigt.

Die Mnemonic-Phrase, zusammen mit einer optionalen Passphrase, wird verwendet, um deterministisch alle Schlüssel abzuleiten, die mit einer HD (Hierarchical Deterministic) Wallet verbunden sind. Das bedeutet, dass aus dieser Phrase alle privaten und öffentlichen Schlüssel der Bitcoin-Wallet deterministisch generiert und rekreiert werden können und folglich Zugang zu den damit verbundenen Mitteln erhalten wird.
![mnemonic](assets/notext/1.webp)
Der Zweck dieser Phrase ist es, ein leicht zu verwendendes Mittel zur Sicherung und Wiederherstellung von Bitcoins bereitzustellen. Es ist zwingend notwendig, die Mnemonic-Phrase an einem sicheren Ort aufzubewahren, da jeder, der im Besitz dieser Phrase ist, Zugang zu den Mitteln der entsprechenden Wallet hätte. Wird sie im Kontext einer traditionellen Wallet verwendet und ohne eine optionale Passphrase, stellt sie oft einen SPOF (Single Point Of Failure) dar.
Üblicherweise wird Ihnen diese Phrase direkt bei der Erstellung Ihrer Wallet gegeben, durch die verwendete Software- oder Hardware-Wallet. Es ist jedoch auch möglich, diese Phrase selbst zu generieren und dann auf dem gewählten Träger einzugeben, um die Wallet-Schlüssel abzuleiten. Das werden wir in diesem Tutorial lernen.

## Vorbereitung der notwendigen Materialien

Für die Erstellung Ihrer Wiederherstellungsphrase von Hand benötigen Sie:

- Ein Blatt Papier;
- Einen Stift oder Bleistift, idealerweise in verschiedenen Farben, um die Organisation zu erleichtern;
- Mehrere Würfel, um das Risiko von Verzerrungen durch einen unausgewogenen Würfel zu minimieren;
- [Die Liste der 2048 BIP39-Wörter](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf) ausgedruckt.

Anschließend wird die Verwendung eines Computers mit einem Terminal für die Berechnung der Prüfsumme notwendig. Genau aus diesem Grund rate ich von der manuellen Generierung der Mnemonic-Phrase ab. Meiner Meinung nach erhöht der Einsatz eines Computers, selbst unter den in diesem Tutorial genannten Vorsichtsmaßnahmen, die Verwundbarkeit einer Wallet erheblich.
Für einen experimentellen Ansatz bezüglich einer "fiktiven Geldbörse" ist es möglich, Ihren üblichen Computer und dessen Terminal zu verwenden. Für einen rigoroseren Ansatz, der darauf abzielt, die Risiken einer Kompromittierung Ihrer Phrase zu begrenzen, wäre es ideal, einen PC zu verwenden, der vom Internet getrennt ist (vorzugsweise ohne eine WLAN-Komponente oder RJ45-Kabelverbindung), ausgestattet mit dem Minimum an Peripheriegeräten (alle sollten per Kabel angeschlossen sein, um Bluetooth zu vermeiden), und vor allem, der auf einer amnesischen Linux-Distribution wie [Tails](https://tails.boum.org/index.fr.html) läuft, gestartet von einem entfernbaren Medium.
![mnemonic](assets/notext/2.webp)

In einem realen Kontext wäre es entscheidend, die Vertraulichkeit Ihres Arbeitsplatzes zu gewährleisten, indem Sie einen Ort fern von neugierigen Blicken wählen, ohne Personenverkehr und frei von Kameras (Webcams, Telefone...).
Es wird empfohlen, eine hohe Anzahl von Würfeln zu verwenden, um die Auswirkungen eines potenziell unausgeglichenen Würfels auf die Entropie zu mildern. Vor ihrer Verwendung wird empfohlen, die Würfel zu überprüfen: Dies kann erreicht werden, indem man sie in einer Schüssel mit gesättigtem Salzwasser testet, was den Würfeln erlaubt zu schwimmen. Dann fahren Sie fort, jeden Würfel etwa zwanzig Mal im Salzwasser zu werfen, wobei Sie die Ergebnisse beobachten. Wenn eine oder zwei Seiten unverhältnismäßig im Vergleich zu den anderen erscheinen, erweitern Sie den Test mit mehr Würfen. Gleichmäßig verteilte Ergebnisse deuten darauf hin, dass der Würfel zuverlässig ist. Wenn jedoch eine oder zwei Seiten regelmäßig dominieren, sollten diese Würfel beiseitegelegt werden, da sie die Entropie Ihrer mnemonischen Phrase und folglich die Sicherheit Ihrer Geldbörse gefährden könnten.
Unter realen Bedingungen wären Sie nach diesen Überprüfungen bereit, die notwendige Entropie zu erzeugen. Für eine experimentelle fiktive Geldbörse, die als Teil dieses Tutorials erstellt wurde, könnten Sie natürlich diese Vorbereitungen überspringen.

## Einige Erinnerungen an die Wiederherstellungsphrase

Zunächst werden wir die Grundlagen der Erstellung einer mnemonischen Phrase gemäß BIP39 überprüfen. Wie zuvor erklärt, wird die Phrase aus pseudo-zufälligen Informationen einer bestimmten Größe abgeleitet, zu denen eine Prüfsumme hinzugefügt wird, um deren Integrität zu gewährleisten.

Die Größe dieser anfänglichen Informationen, oft als "Entropie" bezeichnet, wird durch die Anzahl der Wörter bestimmt, die Sie in der Wiederherstellungsphrase erhalten möchten. Die gängigsten Formate sind Phrasen aus 12 und 24 Wörtern, die jeweils von einer Entropie von 128 Bits und 256 Bits abgeleitet werden. Hier ist eine Tabelle, die die verschiedenen Größen der Entropie gemäß BIP39 zeigt:

| Phrase (Wörter) | Entropie (Bits) | Prüfsumme (Bits) | Entropie + Prüfsumme (Bits) |
| --------------- | --------------- | ---------------- | --------------------------- |
| 12              | 128             | 4                | 132                         |
| 15              | 160             | 5                | 165                         |
| 18              | 192             | 6                | 198                         |
| 21              | 224             | 7                | 231                         |
| 24              | 256             | 8                | 264                         |

Entropie ist also eine Zufallszahl zwischen 128 und 256 Bits. In diesem Tutorial werden wir das Beispiel einer 12-Wort-Phrase nehmen, bei der die Entropie 128 Bits beträgt, was bedeutet, dass wir eine zufällige Sequenz von 128 `0`en oder `1`en generieren werden. Dies stellt eine Zahl dar, die aus 128 Ziffern in Basis 2 (binär) besteht.
Basierend auf dieser Entropie wird eine Prüfsumme generiert. Eine Prüfsumme ist ein Wert, der aus einer Datenmenge berechnet wird, um die Integrität und Gültigkeit dieser Daten während ihrer Übertragung oder Speicherung zu überprüfen. Prüfsummenalgorithmen sind darauf ausgelegt, zufällige Fehler oder Änderungen in den Daten zu erkennen.
Im Falle unserer mnemonischen Phrase besteht die Funktion der Prüfsumme darin, Eingabefehler beim Eingeben der Phrase in die Wallet-Software zu erkennen. Eine ungültige Prüfsumme signalisiert das Vorhandensein eines Fehlers in der Phrase. Umgekehrt deutet eine gültige Prüfsumme darauf hin, dass die Phrase höchstwahrscheinlich korrekt ist.
Um diese Prüfsumme zu erhalten, wird die Entropie durch die SHA256-Hashfunktion geleitet. Diese Operation produziert eine 256-Bit-Sequenz als Ausgabe, von der nur die ersten `N` Bits beibehalten werden, wobei `N` von der gewünschten Länge der Wiederherstellungsphrase abhängt (siehe die Tabelle oben). So werden für eine 12-Wort-Phrase die ersten 4 Bits des Hashs beibehalten.
![mnemonic](assets/de/3.webp)
Diese ersten 4 Bits, die die Prüfsumme bilden, werden dann zur ursprünglichen Entropie hinzugefügt. In diesem Stadium ist die Wiederherstellungsphrase praktisch konstituiert, aber sie ist noch in binärer Form. Um diese binäre Sequenz gemäß dem BIP39-Standard in Wörter umzuwandeln, werden wir die Sequenz zunächst in 11-Bit-Segmente unterteilen.
![mnemonic](assets/notext/4.webp)
Jedes dieser Pakete stellt eine Zahl in Binär dar, die dann in eine Dezimalzahl (Basis 10) umgewandelt wird. Wir werden zu jeder Zahl `1` hinzufügen, da in der Informatik das Zählen von `0` an beginnt, aber die BIP39-Liste ab `1` nummeriert ist.

![mnemonic](assets/notext/5.webp)

Schließlich teilt uns die Zahl in Dezimal die Position des entsprechenden Wortes in [der Liste der 2048 BIP39-Wörter](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf) mit. Es bleibt nur noch, diese Wörter auszuwählen, um die Wiederherstellungsphrase für unsere Wallet zu komponieren.

![mnemonic](assets/notext/6.webp)

Jetzt gehen wir zur Praxis über! Wir werden eine 12-Wort-Wiederherstellungsphrase generieren. Diese Operation bleibt jedoch im Falle einer 24-Wort-Phrase identisch, außer dass sie 256 Bits Entropie und eine 8-Bit-Prüfsumme erfordern würde, wie in der Äquivalenztabelle am Anfang dieses Abschnitts angegeben.

## Schritt 1: Generierung der Entropie

Bereiten Sie Ihr Blatt Papier, Ihren Stift und Ihre Würfel vor. Um zu beginnen, müssen wir zufällig 128 Bits generieren, das heißt, eine Sequenz von 128 `0`en und `1`en hintereinander. Dazu werden wir Würfel verwenden.
![mnemonic](assets/notext/7.webp)

Würfel haben 6 Seiten, alle mit einer identischen Wahrscheinlichkeit, geworfen zu werden. Unser Ziel ist es jedoch, ein binäres Ergebnis zu erzeugen, also zwei mögliche Ausgänge. Daher werden wir den Wert `0` jedem Wurf zuweisen, der auf eine gerade Zahl fällt, und `1` für jede ungerade Zahl. Als Ergebnis werden wir 128 Würfe durchführen, um unsere 128-Bit-Entropie zu erstellen. Zeigt der Würfel `2`, `4` oder `6`, werden wir `0` notieren; für `1`, `3` oder `5` wird es `1` sein. Jedes Ergebnis wird sequenziell notiert, von links nach rechts und von oben nach unten.

Um die folgenden Schritte zu erleichtern, werden wir die Bits in Pakete von vier und drei gruppieren, wie im Bild unten gezeigt. Jede Zeile muss 11 Bits haben: 2 Pakete von 4 Bits und ein Paket von 3 Bits.

![mnemonic](assets/notext/8.webp)
Wie Sie in meinem Beispiel sehen können, besteht das zwölfte Wort derzeit nur aus 7 Bits. Diese werden im nächsten Schritt durch die 4 Bits der Prüfsumme ergänzt, um die 11 Bits zu bilden.
![mnemonic](assets/notext/9.webp)

## Schritt 2: Berechnung der Prüfsumme

Dieser Schritt ist der kritischste bei der manuellen Erzeugung einer Mnemonik-Phrase, da er die Verwendung eines Computers erfordert. Wie bereits erwähnt, entspricht die Prüfsumme dem Anfang des SHA256-Hashs, der aus der Entropie generiert wird. Obwohl es theoretisch möglich ist, einen SHA256-Hash von Hand für eine Eingabe von 128 oder 256 Bits zu berechnen, könnte diese Aufgabe eine ganze Woche in Anspruch nehmen. Darüber hinaus würde jeder Fehler bei manuellen Berechnungen erst am Ende des Prozesses identifiziert werden, was Sie zwingt, von vorne zu beginnen. Daher ist es undenkbar, diesen Schritt nur mit einem Blatt Papier und einem Stift durchzuführen. Ein Computer ist fast obligatorisch. Wenn Sie dennoch lernen möchten, wie man einen SHA256 von Hand berechnet, erklären wir, wie das im [CRYPTO301-Kurs](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f) geht.

Aus diesem Grund rate ich dringend davon ab, eine manuelle Phrase für eine tatsächliche Wallet zu erstellen. Meiner Meinung nach erhöht die Verwendung eines Computers in dieser Phase, selbst mit allen notwendigen Vorsichtsmaßnahmen, unangemessen die Angriffsfläche der Wallet.
Um die Prüfsumme zu berechnen, während so wenig Spuren wie möglich hinterlassen werden, werden wir eine amnesische Linux-Distribution von einem entfernbaren Laufwerk namens **Tails** verwenden. Dieses Betriebssystem startet von einem USB-Stick und funktioniert vollständig im RAM des Computers, ohne mit der Festplatte zu interagieren. Theoretisch hinterlässt es daher keine Spuren auf dem Computer, nachdem er ausgeschaltet wurde. Bitte beachten Sie, dass Tails nur mit Prozessoren vom Typ x86_64 kompatibel ist und nicht mit Prozessoren vom Typ ARM.
Beginnen Sie damit, von Ihrem üblichen Computer aus das Tails-Image von seiner offiziellen Website [herunterzuladen](https://tails.net/install/index.fr.html). Stellen Sie die Authentizität Ihres Downloads sicher, indem Sie die Signatur des Entwicklers oder das vom Standort angebotene Verifizierungstool verwenden.
![mnemonic](assets/notext/10.webp)
Formatieren Sie zunächst Ihren USB-Stick und installieren Sie Tails mit einem Tool wie [Balena Etcher](https://etcher.balena.io/).
![mnemonic](assets/notext/11.webp)
Nachdem Sie bestätigt haben, dass das Flashen erfolgreich war, schalten Sie Ihren Computer aus. Gehen Sie dann dazu über, die Stromversorgung zu trennen und die Festplatte vom Motherboard Ihres PCs zu entfernen. Falls eine WiFi-Karte vorhanden ist, sollte diese getrennt werden. Entfernen Sie ebenso jedes RJ45-Ethernet-Kabel. Um das Risiko eines Datenlecks zu minimieren, wird empfohlen, Ihre Internetbox auszustecken und Ihr Mobiltelefon auszuschalten. Stellen Sie außerdem sicher, dass alle überflüssigen Peripheriegeräte von Ihrem Computer getrennt sind, wie das Mikrofon, die Webcam, Lautsprecher oder das Headset, und überprüfen Sie, dass andere Peripheriegeräte nur über Kabel verbunden sind. All diese Vorbereitungsschritte für den PC sind nicht unbedingt erforderlich, helfen aber, die Angriffsfläche so weit wie möglich in einem realen Kontext zu reduzieren.

Überprüfen Sie, ob Ihr BIOS so konfiguriert ist, dass es das Booten von einem externen Gerät zulässt. Wenn nicht, ändern Sie diese Einstellung und starten Sie Ihre Maschine neu. Sobald Sie die Computerumgebung gesichert haben, starten Sie den Computer vom USB-Stick mit Tails OS.

Auf dem Willkommensbildschirm von Tails wählen Sie die Sprache Ihrer Wahl und starten das System, indem Sie auf `Start Tails` klicken.

![mnemonic](assets/notext/12.webp)

Klicken Sie vom Desktop aus auf die Registerkarte `Anwendungen`.

![mnemonic](assets/notext/13.webp)

Navigieren Sie zum Menü `Dienstprogramme`.

![mnemonic](assets/notext/14.webp)
Und schließlich klicken Sie auf die `Terminal`-Anwendung.
![mnemonic](assets/notext/15.webp)

Sie gelangen zu einem neuen, leeren Befehlsterminal.

![mnemonic](assets/notext/16.webp)
Geben Sie den `echo`-Befehl ein, gefolgt von Ihrer zuvor generierten Entropie, und achten Sie darauf, ein Leerzeichen zwischen `echo` und Ihrer Binärziffernfolge einzufügen.
![mnemonic](assets/notext/17.webp)

Fügen Sie ein zusätzliches Leerzeichen hinzu, dann geben Sie den folgenden Befehl ein, indem Sie eine _Pipe_ (`|`) verwenden:

```plaintext
| shasum -a 256 -0
```

![mnemonic](assets/notext/18.webp)

Im Beispiel mit meiner Entropie lautet der gesamte Befehl wie folgt:

```plaintext
echo 11010111000110111011000011000010011000100111000001000000001001011011001010111111001010011111110001010100000101110010010011011010 | shasum -a 256 -0
```

In diesem Befehl:

- wird `echo` verwendet, um die Bitfolge zu senden;
- `|`, die _Pipe_, wird verwendet, um die Ausgabe des `echo`-Befehls an die Eingabe des nächsten Befehls zu leiten;
- `shasum` startet eine Hashing-Funktion, die zur SHA (_Secure Hash Algorithm_)-Familie gehört;
- `-a` gibt die Wahl eines spezifischen Hashing-Algorithmus an;
- `256` zeigt an, dass der SHA256-Algorithmus verwendet wird;
- `-0` ermöglicht es, die Eingabe als eine Binärzahl zu interpretieren.

Nachdem Sie sorgfältig überprüft haben, dass Ihre Binärsequenz keine Tippfehler enthält, drücken Sie die `Enter`-Taste, um den Befehl auszuführen. Das Terminal wird dann den SHA256-Hash Ihrer Entropie anzeigen.

![mnemonic](assets/notext/19.webp)

Vorerst wird der Hash im hexadezimalen Format (Basis 16) ausgedrückt. Zum Beispiel ist meiner:

```plaintext
a27abf1aff70311917a59a43ce86fa45a62723a00dd2f9d3d059aeac9b4b13d8
```

Um unsere mnemonische Phrase zu finalisieren, benötigen wir nur die ersten 4 Bits des Hashs, die die Prüfsumme bilden. Im hexadezimalen Format repräsentiert jedes Zeichen 4 Bits. Daher werden wir nur das erste Zeichen des Hashs beibehalten. Für eine 24-Wort-Phrase wäre es notwendig, die ersten zwei Zeichen zu berücksichtigen. In meinem Beispiel entspricht dies dem Buchstaben: `a`. Notieren Sie sich dieses Zeichen sorgfältig irgendwo auf Ihrem Blatt, dann schalten Sie Ihren Computer aus.

Der nächste Schritt ist die Umwandlung dieses hexadezimalen Zeichens (Basis 16) in einen binären Wert (Basis 2), da unsere Phrase in diesem Format konstruiert ist. Dazu können Sie die folgende Umrechnungstabelle verwenden:

| Dezimal (Basis 10) | Hexadezimal (Basis 16) | Binär (Basis 2) |
| ------------------ | ---------------------- | --------------- |
| 0                  | 0                      | 0000            |
| 1                  | 1                      | 0001            |
| 2                  | 2                      | 0010            |
| 3                  | 3                      | 0011            |
| 4                  | 4                      | 0100            |
| 5                  | 5                      | 0101            |
| 6                  | 6                      | 0110            |
| 7                  | 7                      | 0111            |
| 8                  | 8                      | 1000            |
| 9                  | 9                      | 1001            |
| 10                 | a                      | 1010            |
| 11                 | b                      | 1011            |
| 12                 | c                      | 1100            |
| 13                 | d                      | 1101            |
| 14                 | e                      | 1110            |
| 15                 | f                      | 1111            |

In meinem Beispiel entspricht der Buchstabe `a` der Binärzahl `1010`. Diese 4 Bits bilden die Prüfsumme unserer Wiederherstellungsphrase. Sie können sie nun der bereits auf Ihrem Blatt Papier notierten Entropie hinzufügen, indem Sie sie am Ende des letzten Wortes platzieren.

![mnemonic](assets/notext/20.webp)

Ihre mnemonische Phrase ist nun vollständig, aber sie liegt im Binärformat vor. Der nächste Schritt wird sein, sie in das Dezimalsystem umzuwandeln, damit Sie dann jede Zahl einer entsprechenden Wort in der BIP39-Liste zuordnen können.

## Schritt 3: Umwandlung von Wörtern in Dezimalzahlen

Um jede Binärzeile in eine Dezimalzahl umzuwandeln, werden wir eine Methode verwenden, die die manuelle Berechnung erleichtert. Derzeit haben Sie zwölf Zeilen auf Ihrem Papier, jede besteht aus 11 Binärziffern `0` oder `1`. Um mit einer Umwandlung in Dezimalzahlen fortzufahren, weisen Sie jedem ersten Ziffer den Wert `1024` zu, wenn es sich um `1` handelt, andernfalls `0`. Für die zweite Ziffer wird der Wert `512` zugewiesen, wenn es sich um `1` handelt, andernfalls `0`, und so weiter bis zur elften Ziffer. Die Entsprechungen sind wie folgt:

- 1. Bit: `1024`;
- 2. Bit: `512`;
- 3. Bit: `256`;
- 4. Bit: `128`;
- 5. Bit: `64`;
- 6. Bit: `32`;
- 7. Bit: `16`;
- 8. Bit: `8`;
- 9. Bit: `4`;
- 10. Bit: `2`;
- 11. Bit: `1`.

Für jede Zeile werden wir die Werte, die den Ziffern `1` entsprechen, addieren, um die Dezimalzahläquivalent der Binärzahl zu erhalten. Nehmen wir das Beispiel einer Binärzeile gleich:

```plaintext
1010 1101 101
```

Die Umwandlung wäre wie folgt:
![mnemonic](assets/notext/21.webp)
Das Ergebnis wäre dann:

```plaintext
1389
```

Für jedes Bit gleich `1`, notieren Sie die zugehörige Zahl darunter. Für jedes Bit gleich `0`, notieren Sie nichts.

![mnemonic](assets/notext/22.webp)
Dann addieren Sie einfach alle Zahlen, die durch `1`er bestätigt wurden, um die Dezimalzahl zu erhalten, die jede Binärzeile repräsentiert. Hier ist ein Beispiel, wie es für mein Blatt aussieht:
![mnemonic](assets/notext/23.webp)

## Schritt 4: Suche nach den Wörtern der mnemonischen Phrase

Mit den erhaltenen Dezimalzahlen können wir nun die entsprechenden Wörter in der Liste finden, um die mnemonische Phrase zu bilden. Die Nummerierung der 2048 Wörter in der BIP39-Liste reicht jedoch von `1` bis `2048`. Aber unsere berechneten Binärergebnisse reichen von `0` bis `2047`. Daher gibt es eine Verschiebung um eine Einheit, die korrigiert werden muss. Um diese Verschiebung zu korrigieren, fügen Sie einfach `1` zu den zwölf zuvor berechneten Dezimalzahlen hinzu.

![mnemonic](assets/notext/24.webp)
Nach dieser Anpassung haben Sie den Rang jedes Wortes innerhalb der Liste. Alles, was bleibt, ist, jedes Wort durch seine Nummer zu identifizieren. Offensichtlich, wie bei allen anderen Schritten, dürfen Sie Ihren Computer nicht verwenden, um diese Umwandlung durchzuführen. Stellen Sie daher sicher, dass Sie die Liste vorher ausgedruckt haben.
[**-> Drucken Sie die BIP39-Liste im A4-Format aus.**](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf)

Zum Beispiel, wenn die aus der ersten Zeile abgeleitete Nummer 1721 ist, wird das entsprechende Wort das 1721. auf der Liste sein:

```plaintext
1721. strike
```

![mnemonic](assets/notext/25.webp)
Auf diese Weise fahren wir sukzessive mit den 12 Wörtern fort, um unsere mnemonische Phrase zu konstruieren.

![mnemonic](assets/notext/26.webp)

## Schritt 5: Erstellen des Bitcoin-Wallets

An diesem Punkt bleibt nur noch, unsere mnemonische Phrase in eine Bitcoin-Wallet-Software zu importieren. Je nach unseren Vorlieben kann dies auf einer Desktop-Software geschehen, um ein Hot Wallet zu erhalten, oder auf einem Hardware-Wallet für ein Cold Wallet.

![mnemonic](assets/notext/27.webp)

Erst bei der Importierung können Sie die Gültigkeit Ihrer Prüfsumme verifizieren. Wenn die Software eine Nachricht wie `Invalid Checksum` anzeigt, bedeutet dies, dass ein Fehler in Ihren Erstellungsprozess eingeschlichen ist. Im Allgemeinen resultiert dieser Fehler entweder aus einem Rechenfehler während der manuellen Umwandlungen und Additionen oder aus einem Tippfehler bei der Eingabe Ihrer Entropie im Terminal auf Tails. Es wird notwendig sein, den Prozess von Anfang an neu zu starten, um diese Fehler zu korrigieren.

![mnemonic](assets/notext/28.webp)
Nachdem Sie Ihr Wallet erstellt haben, vergessen Sie nicht, Ihre Wiederherstellungsphrase auf einem physischen Medium wie Papier oder Metall zu sichern und die während der Generierung verwendete Tabelle zu zerstören, um jegliche Informationslecks zu verhindern.

## Spezifischer Fall der Würfelwurf-Option auf Coldcards

Die Hardware-Wallets aus der Coldcard-Familie bieten [eine Funktion namens _Dice Roll_](https://youtu.be/Rc29d9m92xg?si=OeFW2iCGRvxexhK7), um die Wiederherstellungsphrase Ihres Wallets mit Würfeln zu generieren. Diese Methode ist ausgezeichnet, da sie Ihnen direkte Kontrolle über die Erstellung der Entropie gibt, ohne die Verwendung eines externen Geräts zur Berechnung der Prüfsumme, wie in unserem Tutorial erforderlich.

Jedoch wurden kürzlich Bitcoin-Diebstähle gemeldet, die auf unsachgemäßen Gebrauch dieser Funktion zurückzuführen sind. Tatsächlich kann eine zu begrenzte Anzahl von Würfelwürfen zu unzureichender Entropie führen, was theoretisch das Brute-Force-Verfahren der mnemonischen Phrase und den Diebstahl der damit verbundenen Bitcoins ermöglicht. Um dieses Risiko zu vermeiden, wird empfohlen, auf der Coldcard mindestens 99 Würfelwürfe durchzuführen, was ausreichende Entropie sicherstellt.

Die Methode zur Interpretation der Ergebnisse, die von Coldcard vorgeschlagen wird, unterscheidet sich von der in diesem Tutorial vorgestellten. Während wir 128 Würfe empfehlen, um 128 Bit Sicherheit im Tutorial zu erreichen, schlägt Coldcard 99 Würfe vor, um 256 Bit Sicherheit zu erreichen. Tatsächlich sind in unserem Ansatz nur zwei Ergebnisse für jeden Würfelwurf möglich: gerade (`0`) oder ungerade (`1`). Daher ist die durch jeden Wurf generierte Entropie gleich `log2(2)`. Im Fall von Coldcard, das die sechs möglichen Seiten des Würfels (von `1` bis `6`) berücksichtigt, ist die Entropie pro Wurf gleich `log2(6)`. Deshalb müssen wir in unserem Tutorial mehr Würfe durchführen, um das gleiche Niveau an Entropie zu erreichen.

```plaintext
Entropie = Anzahl der Würfe * log2(Anzahl der möglichen Ergebnisse auf dem Würfel)
Coldcard:

Entropie = 99 * log2(6)
Entropie = 255,91

Unser Tutorial:

Entropie = 128 * log2(2)
Entropie = 128
```
