---
term: OP_HASH160 (0XA9)

definition: Opcode, der das oberste Element erst mit SHA256 und dann mit RIPEMD160 hasht.
---
Nimmt das oberste Element vom Stapel und ersetzt es durch seinen Hash, wobei die Funktionen `SHA256` und `RIPEMD160` gleichzeitig verwendet werden. Dieser zweistufige Prozess erzeugt einen 160-Bit-Fingerabdruck.