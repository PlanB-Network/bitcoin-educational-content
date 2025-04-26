---
term: BLOCKKOPF

---
Der Block-Header ist eine Datenstruktur, die als Hauptkomponente bei der Konstruktion eines Bitcoin-Blocks dient. Jeder Block besteht aus einem Header und einer Liste von Transaktionen. Der Block-Header enthält wichtige Informationen, die die Integrität und Gültigkeit eines Blocks innerhalb der Blockchain sicherstellen. Der Block-Header enthält 80 Bytes an Metadaten und setzt sich aus den folgenden Elementen zusammen:


- Die Blockversion;
- Der Hash-Wert des vorherigen Blocks;
- Die Merkle-Baumwurzel der Transaktionen;
- Der Zeitstempel des Blocks;
- Das Schwierigkeitsziel;
- Die Nonce.

Hier ist zum Beispiel die Kopfzeile des Blocks Nummer 785.530 im Hexadezimalformat, der von Foundry USA am 15. April 2023 abgebaut wurde:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Wenn wir diese Überschrift aufschlüsseln, können wir erkennen:


- Die Version:

```text
00e0ff3f
```


- Die vorherige Raute:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```


- Die Merkle-Wurzel:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```


- Der Zeitstempel:

```text
bcb13a64
```


- Das Ziel:

```text
b2e00517
```


- Die Nonce:

```text
43f09a40
```

Um gültig zu sein, muss ein Block einen Header haben, der nach dem Hashing mit `SHA256d` einen Hash ergibt, der kleiner oder gleich dem Schwierigkeitsziel ist.

> ► *Im Englischen wird er als "Block Header" bezeichnet