---
term: HASH-FUNKTION
---

Eine mathematische Funktion, die eine Eingabe variabler Größe (genannt Nachricht) nimmt und eine Ausgabe fester Größe produziert (genannt Hash, Hashing, Digest oder Fingerabdruck). Hash-Funktionen sind weit verbreitete Primitive in der Kryptographie. Sie weisen spezifische Eigenschaften auf, die sie für den Einsatz in sicheren Kontexten geeignet machen:
* Preimage-Resistenz: Es muss sehr schwierig sein, eine Nachricht zu finden, die einen spezifischen Hash erzeugt, d.h., ein Preimage $m$ für einen Hash $h$ zu finden, so dass $h = H(m)$, wobei $H$ die Hash-Funktion ist;
* Second-Preimage-Resistenz: Gegeben sei eine Nachricht $m_1$, muss es sehr schwierig sein, eine andere Nachricht $m_2$ (unterschiedlich von $m_1$) zu finden, so dass $H(m_1) = H(m_2)$;
* Kollisionsresistenz: Es muss sehr schwierig sein, zwei verschiedene Nachrichten $m_1$ und $m_2$ zu finden, so dass $H(m_1) = H(m_2)$;
* Manipulationssicherheit: Kleine Änderungen in der Eingabe müssen signifikante und unvorhersehbare Änderungen in der Ausgabe verursachen.

Im Kontext von Bitcoin werden Hash-Funktionen für verschiedene Zwecke verwendet, einschließlich des Proof-of-Work-Mechanismus (*Proof-of-Work*), Transaktionsidentifikatoren, Adressgenerierung, Checksummenberechnungen und der Erstellung von Datenstrukturen wie Merkle-Bäumen. Auf der Protokollebene verwendet Bitcoin ausschließlich die Funktion `SHA256d`, auch `HASH256` genannt, die aus einem doppelten `SHA256`-Hash besteht. `HASH256` wird auch bei der Berechnung bestimmter Checksummen verwendet, insbesondere für erweiterte Schlüssel (`xpub`, `xprv`...). Auf der Wallet-Seite werden auch die folgenden verwendet:
* Einfaches `SHA256` für Checksummen von mnemonischen Phrasen;
* `SHA512` innerhalb der `HMAC`- und `PBKDF2`-Algorithmen, die im Prozess der Ableitung deterministischer und hierarchischer Wallets verwendet werden;
* `HASH160`, das eine aufeinanderfolgende Verwendung von `SHA256` und einem `RIPEMD160` beschreibt. `HASH160` wird im Prozess der Generierung von Empfangsadressen (außer P2PK und P2TR) und bei der Berechnung von Elternschlüssel-Fingerabdrücken für erweiterte Schlüssel verwendet.

> ► *Auf Englisch wird es als "hash function" bezeichnet.*