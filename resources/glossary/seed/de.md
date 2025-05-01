---
term: KORN
---

Im spezifischen Kontext eines hierarchischen, deterministischen Bitcoin-Portfolios ist ein seed eine 512-Bit-Information, die von einem Zufallsereignis abgeleitet ist. Es wird verwendet, um deterministisch und hierarchisch generate eine Reihe von privaten Schlüsseln und die entsprechenden öffentlichen Schlüssel für ein Bitcoin-Portfolio zu erstellen. Der seed wird oft mit der Recovery-Phrase selbst verwechselt. Aber es ist nicht dasselbe. Die seed wird durch Anwendung der Funktion "PBKDF2" auf die Mnemonic-Phrase und jede passphrase erhalten.


Der seed wurde mit BIP32 erfunden, das die Grundlagen des hierarchischen deterministischen Portfolios definierte. In diesem Standard maß der seed 128 Bit. Dadurch können alle Schlüssel eines Portfolios aus einer einzigen Information abgeleitet werden, im Gegensatz zu JBOK-Portfolios (*Just a Bunch of Keys*), die für jeden erzeugten Schlüssel neue Sicherungen erfordern. BIP39 schlug dann eine Kodierung dieses seed vor, um das Lesen durch Menschen zu vereinfachen. Diese Kodierung erfolgt in Form einer Phrase, die allgemein als Mnemonic-Phrase oder Wiederherstellungsphrase bezeichnet wird. Dieser Standard vermeidet Fehler beim Speichern der seed, insbesondere dank der Verwendung einer Prüfsumme.


Außerhalb des Bitcoin-Kontextes ist ein seed in der Kryptografie im Allgemeinen ein Anfangswert, der für generate kryptografische Schlüssel oder allgemeiner für jede Art von Daten verwendet wird, die von einem Pseudo-Zufallszahlengenerator erzeugt werden. Dieser Anfangswert muss zufällig und unvorhersehbar sein, um die Sicherheit des kryptografischen Systems zu gewährleisten. seed führt zwar Entropie in das System ein, aber der anschließende Generierungsprozess ist deterministisch.


> im allgemeinen Sprachgebrauch beziehen sich die meisten Bitcoiner auf die Mnemonic-Phrase, wenn sie von der "seed" sprechen, und nicht auf den Zwischenzustand der Ableitung, der zwischen der Mnemonic-Phrase und dem Hauptschlüssel liegt