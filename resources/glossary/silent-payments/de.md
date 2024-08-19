---
term: STILLE ZAHLUNGEN
---

Methode zur Verwendung von statischen Bitcoin-Adressen, um Zahlungen zu empfangen, ohne Adresswiederverwendung, ohne Interaktion und ohne eine sichtbare On-Chain-Verbindung zwischen den verschiedenen Zahlungen und der statischen Adresse. Diese Technik eliminiert die Notwendigkeit, für jede Transaktion neue, unbenutzte Empfangsadressen zu generieren, und vermeidet somit die üblichen Interaktionen in Bitcoin, bei denen der Empfänger dem Zahler eine neue Adresse bereitstellen muss.

Bei Stillen Zahlungen verwendet der Zahler die öffentlichen Schlüssel des Empfängers (Ausgaben-öffentlicher Schlüssel und Scan-öffentlicher Schlüssel) und die Summe seiner eigenen privaten Schlüssel als Eingabe, um eine frische Adresse für jede Zahlung zu generieren. Nur der Empfänger, mit seinen privaten Schlüsseln, kann den privaten Schlüssel berechnen, der dieser Zahlungsadresse entspricht. ECDH (*Elliptic-Curve Diffie-Hellman*), ein kryptografischer Schlüsselaustauschalgorithmus, wird verwendet, um ein gemeinsames Geheimnis zu etablieren, das dann verwendet wird, um die Empfangsadresse und den privaten Schlüssel (nur auf der Seite des Empfängers) abzuleiten. Um die Stillen Zahlungen zu identifizieren, die für sie bestimmt sind, müssen Empfänger die Blockchain scannen und jede Transaktion untersuchen, die den Kriterien des Protokolls entspricht. Im Gegensatz zu BIP47, das eine Benachrichtigungstransaktion verwendet, um den Zahlungskanal zu etablieren, eliminieren Stille Zahlungen diesen Schritt und sparen eine Transaktion. Der Kompromiss besteht jedoch darin, dass der Empfänger alle potenziellen Transaktionen scannen muss, um durch Anwendung von ECDH zu bestimmen, ob sie an ihn gerichtet sind.

Zum Beispiel repräsentiert Bobs statische Adresse $B$ die Verkettung seines Scan-öffentlichen Schlüssels und seines Ausgaben-öffentlichen Schlüssels:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

Diese Schlüssel werden einfach von folgendem Pfad abgeleitet:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Diese statische Adresse wird von Bob veröffentlicht. Alice ruft sie ab, um eine Stille Zahlung an Bob zu tätigen. Sie berechnet Bobs Zahlungsadresse $P_0$ auf diese Weise:

$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Wobei:

$$  \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A)  $$

Mit:
* $B_{\text{scan}}$: Bobs Scan-öffentlicher Schlüssel (statische Adresse);
* $B_{\text{spend}}$: Bobs Ausgaben-öffentlicher Schlüssel (statische Adresse);
* $A$: Die Summe der öffentlichen Schlüssel in Eingabe (Tweak);
* $a$: Der private Schlüssel des Tweak, das heißt, die Summe aller Schlüsselpaare, die im `scriptPubKey` der UTXOs verwendet werden, die als Eingaben in Alices Transaktion verbraucht werden;
* $\text{outpoint}_L$: Das kleinste UTXO (lexikografisch), das als Eingabe in Alices Transaktion verwendet wird;
* $\text{ ‖ }$: Verkettung (die Operation des End-zu-End-Verbindens von Operanden);
* $G$: Der Generatorpunkt der elliptischen Kurve `secp256k1`;
* $\text{hash}$: Die SHA256-Hash-Funktion, getaggt mit `BIP0352/SharedSecret`;
* $P_0$: Der erste öffentliche Schlüssel / eindeutige Adresse für die Zahlung an Bob;
* $0$: Eine ganze Zahl, die verwendet wird, um mehrere einzigartige Zahlungsadressen zu generieren.

Bob scannt die Blockchain auf diese Weise, um seine Stille Zahlung zu finden:
$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$
Mit:
* $b_{\text{scan}}$: Bobs privater Scan-Schlüssel.

Wenn er $P_0$ als eine Adresse findet, die eine stille Zahlung an ihn enthält, berechnet er $p_0$, den privaten Schlüssel, der es ihm erlaubt, die von Alice an $P_0$ gesendeten Gelder auszugeben:

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Mit:
* $b_{\text{spend}}$: Bobs privater Ausgabe-Schlüssel;
* $n$: die Ordnung der elliptischen Kurve `secp256k1`.

Zusätzlich zu dieser Basisversion können auch Labels verwendet werden, um mehrere verschiedene statische Adressen aus derselben Basisadresse zu generieren, mit dem Ziel, mehrere Verwendungen zu trennen, ohne die bei der Überprüfung erforderliche Arbeit unangemessen zu vervielfachen.