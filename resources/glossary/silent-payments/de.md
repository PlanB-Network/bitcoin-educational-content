---
term: STILLE ZAHLUNGEN

---
Methode zur Verwendung statischer Bitcoin-Adressen zum Empfang von Zahlungen ohne Adresswiederverwendung, ohne Interaktion und ohne sichtbare On-Chain-Verbindung zwischen den verschiedenen Zahlungen und der statischen Adresse. Diese Technik eliminiert die Notwendigkeit, neue, unbenutzte Empfangsadressen für jede Transaktion zu generieren und vermeidet somit die üblichen Interaktionen in Bitcoin, bei denen der Empfänger dem Zahler eine neue Adresse zur Verfügung stellen muss.

Bei Silent Payments verwendet der Zahler die öffentlichen Schlüssel des Empfängers (spend public key und scan public key) und die Summe seiner eigenen privaten Schlüssel als Eingabe, um für jede Zahlung eine neue Adresse zu generieren. Nur der Empfänger kann mit seinen privaten Schlüsseln den zu dieser Zahlungsadresse gehörenden privaten Schlüssel errechnen. ECDH (*Elliptic-Curve Diffie-Hellman*), ein kryptographischer Schlüsselaustauschalgorithmus, wird verwendet, um ein gemeinsames Geheimnis zu erstellen, das dann zur Ableitung der Empfängeradresse und des privaten Schlüssels (nur auf der Empfängerseite) verwendet wird. Um die für sie bestimmten Stillen Zahlungen zu identifizieren, müssen die Empfänger die Blockchain scannen und jede Transaktion prüfen, die den Kriterien des Protokolls entspricht. Im Gegensatz zu BIP47, das eine Benachrichtigungstransaktion zur Einrichtung des Zahlungskanals verwendet, entfällt dieser Schritt bei Silent Payments, wodurch eine Transaktion eingespart wird. Der Kompromiss besteht jedoch darin, dass der Empfänger alle potenziellen Transaktionen scannen muss, um durch Anwendung von ECDH festzustellen, ob sie für ihn bestimmt sind.

Bobs statische Adresse $B$ ist beispielsweise die Verkettung seines öffentlichen Schlüssels für den Scan und seines öffentlichen Schlüssels für den Spend:

$$ B = B_{\text{scan}} {{\text{ ‖ } B_{\text{spend}} $$

Diese Schlüssel werden einfach von dem folgenden Pfad abgeleitet:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Diese statische Adresse wird von Bob veröffentlicht. Alice ruft sie ab, um eine stille Zahlung an Bob zu leisten. Sie berechnet Bobs Zahlungsadresse $P_0$ auf diese Weise:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$

Wo:

$$ \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A) $$

Mit:


- $B_{\text{scan}}$: Bobs öffentlicher Scan-Schlüssel (statische Adresse);
- $B_{\text{spend}}$: Bobs öffentlicher Schlüssel für Ausgaben (statische Adresse);
- $A$: Die Summe der öffentlichen Schlüssel in der Eingabe (tweak);
- $a$: Der private Schlüssel des Tweaks, d.h. die Summe aller Schlüsselpaare, die im `scriptPubKey` der UTXOs verwendet werden, die als Eingaben in Alices Transaktion verwendet werden;
- $\text{outpoint}_L$: Der kleinste UTXO (lexikografisch), der als Eingabe in Alices Transaktion verwendet wird;
- $\text{ ‖ }$: Verkettung (die Operation, bei der Operanden Ende-zu-Ende verbunden werden);
- $G$: Der Generatorpunkt der elliptischen Kurve `secp256k1`;
- $\text{hash}$: Die SHA256-Hash-Funktion mit der Kennzeichnung "BIP0352/SharedSecret";
- $P_0$: Der erste öffentliche Schlüssel / die erste eindeutige Adresse für die Zahlung an Bob;
- $0$: Eine ganze Zahl, die verwendet wird, um mehrere eindeutige Zahlungsadressen zu erzeugen.

Bob scannt die Blockchain, um auf diese Weise seine Stille Zahlung zu finden:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Mit:


- $b_{\text{scan}}$: Bobs privater Scan-Schlüssel.

Wenn er $P_0$ als Adresse findet, die eine an ihn gerichtete Stille Zahlung enthält, berechnet er $p_0$, den privaten Schlüssel, der es ihm ermöglicht, die von Alice an $P_0$ gesendeten Mittel auszugeben:

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Mit:


- $b_{\text{spend}}$: Bobs privater Ausgabenschlüssel;
- $n$: die Ordnung der elliptischen Kurve "secp256k1".

Zusätzlich zu dieser Basisversion können Etiketten auch dazu verwendet werden, aus derselben statischen Basisadresse mehrere verschiedene statische Adressen zu generieren, um Mehrfachnutzungen zu trennen, ohne den Arbeitsaufwand beim Scannen unangemessen zu vervielfachen.