---
term: BLOCK HEADER
---

Der Block Header ist eine Datenstruktur, die als Hauptkomponente beim Aufbau eines Bitcoin-Blocks dient. Jeder Block besteht aus einem Header und einer Liste von Transaktionen. Der Block Header enthält wichtige Informationen, die die Integrität und Gültigkeit eines Blocks innerhalb der Blockchain sicherstellen. Der Block Header umfasst 80 Bytes an Metadaten und setzt sich aus den folgenden Elementen zusammen:
* Die Blockversion;
* Der Hash des vorherigen Blocks;
* Der Merkle-Baum-Wurzel der Transaktionen;
* Der Zeitstempel des Blocks;
* Das Schwierigkeitsziel;
* Der Nonce.

Zum Beispiel, hier ist der Header des Blocks Nummer 785.530 im hexadezimalen Format, abgebaut von Foundry USA am 15. April 2023:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Wenn wir diesen Header aufschlüsseln, können wir erkennen:
* Die Version:

```text
00e0ff3f
```

* Der vorherige Hash:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```

* Die Merkle-Wurzel:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```

* Der Zeitstempel:

```text
bcb13a64
```

* Das Ziel:

```text
b2e00517
```

* Der Nonce:

```text
43f09a40
```

Damit ein Block gültig ist, muss er einen Header haben, der, einmal mit `SHA256d` gehasht, einen Hash erzeugt, der kleiner oder gleich dem Schwierigkeitsziel ist.

> ► *Auf Englisch wird es als "Block Header" bezeichnet.*