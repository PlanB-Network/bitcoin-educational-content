---
term: HASH FUNCTION

---
Eine mathematische Funktion, die eine Eingabe variabler Größe (Nachricht genannt) annimmt und eine Ausgabe fester Größe (Hash, Hashing, Digest oder Fingerprint genannt) erzeugt. Hash-Funktionen sind weit verbreitete Primitive in der Kryptographie. Sie weisen spezifische Eigenschaften auf, die sie für den Einsatz in sicheren Kontexten geeignet machen:


- Preimage-Resistenz: Es muss sehr schwierig sein, eine Nachricht zu finden, die einen bestimmten Hash erzeugt, d. h. ein Preimage $m$ für einen Hash $h$ zu finden, so dass $h = H(m)$, wobei $H$ die Hash-Funktion ist;
- Zweiter Vorbildwiderstand: Bei einer Nachricht $m_1$ muss es sehr schwierig sein, eine andere Nachricht $m_2$ (verschieden von $m_1$) zu finden, so dass $H(m_1) = H(m_2)$;
- Kollisionssicherheit: Es muss sehr schwierig sein, zwei verschiedene Nachrichten $m_1$ und $m_2$ zu finden, bei denen $H(m_1) = H(m_2)$ ist;
- Manipulationssicherheit: Kleine Änderungen am Eingang müssen zu signifikanten und unvorhersehbaren Änderungen am Ausgang führen.

Im Zusammenhang mit Bitcoin werden Hash-Funktionen für verschiedene Zwecke verwendet, darunter der Proof-of-Work-Mechanismus (*Proof-of-Work*), Transaktionskennungen, Adressgenerierung, Prüfsummenberechnungen und die Erstellung von Datenstrukturen wie Merkle-Bäumen. Auf der Protokollseite verwendet Bitcoin ausschließlich die Funktion `SHA256d`, auch `HASH256` genannt, die aus einem doppelten `SHA256`-Hash besteht. die Funktion `HASH256` wird auch zur Berechnung bestimmter Prüfsummen verwendet, insbesondere für erweiterte Schlüssel (`xpub`, `xprv`...). Auf der Seite der Brieftasche werden auch die folgenden Verfahren verwendet:


- Einfaches `SHA256` für Prüfsummen von mnemonischen Phrasen;
- sHA512" in den Algorithmen "Hmac" und "PBKDF2", die bei der Ableitung deterministischer und hierarchischer Wallets verwendet werden;
- hASH160", das die aufeinanderfolgende Verwendung von "SHA256" und "RIPEMD160" beschreibt. hASH160" wird bei der Erzeugung von Empfangsadressen (außer P2PK und P2TR) und bei der Berechnung von Fingerabdrücken von Elternschlüsseln für erweiterte Schlüssel verwendet.

> ► *Im Englischen wird sie als "Hash-Funktion" bezeichnet