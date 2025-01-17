---
term: OP_HASH256 (0XAA)

---
Nimmt das oberste Element vom Stapel und ersetzt es durch seinen Hash, indem die Funktion `SHA256` zweimal verwendet wird. Die Eingabe wird einmal mit `SHA256` gehasht, und dann wird der Digest ein zweites Mal mit `SHA256` gehasht. Dieser zweistufige Prozess erzeugt einen 256-Bit-Fingerabdruck.