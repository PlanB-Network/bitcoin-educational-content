---
term: Komprimerad publik nyckel
definition: Kompakt form av en offentlig nyckel som endast använder x-koordinaten och ett paritetsprefix (02 eller 03).
---

En publik nyckel används i skript (antingen direkt i form av en publik nyckel eller som en Address) för att ta emot och säkra bitcoins. En rå publik nyckel representeras av en punkt på en elliptisk kurva som består av två koordinater (`x, y`) på vardera 256 bitar. I råformat mäter en offentlig nyckel därför 512 bitar, utan att räkna den extra byte som identifierar formatet. En komprimerad publik nyckel är å andra sidan en mer kompakt form av representation av publika nycklar. Den använder endast koordinaten `x` och ett prefix (`02` eller `03`) som anger pariteten för koordinaten `y` (jämn eller udda).


Om vi förenklar detta till området för reella tal, givet att den elliptiska kurvan är symmetrisk med avseende på x-axeln, finns det för varje punkt $P$ (`x, y`) på kurvan en punkt $P'$ (`x, -y`) som också kommer att ligga på samma kurva. Detta innebär att för varje `x` finns det bara två möjliga värden på `y`, positiva och negativa. Till exempel, för en given abscissa `x`, skulle det finnas två punkter $P1$ och $P2$ på den elliptiska kurvan, som delar samma abscissa men med motsatta ordinater:




För att välja mellan de två potentiella punkterna på kurvan läggs ett prefix som anger vilken `y` som ska väljas till `x`. Med den här metoden kan storleken på en publik nyckel minskas från 520 bitar till endast 264 bitar (8 bitar för prefixet + 256 bitar för `x`). Denna representation kallas för den komprimerade formen av den publika nyckeln.


I samband med elliptisk kurvkryptografi använder vi dock inte de reella talen, utan ett ändligt fält av ordning `p` (ett primtal). I detta sammanhang bestäms "tecknet" för `y` av dess paritet, det vill säga om `y` är jämnt eller udda. Prefixet `0x02` anger då ett jämnt `y`, medan `0x03` anger ett udda `y`.


Ta följande exempel på en rå publik nyckel (en punkt på den elliptiska kurvan) i hexadecimal:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```


Vi kan isolera prefixet, "x" och "y":

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Bas 16 (hexadecimal): f

Bas 10 (decimal): 15

y är udda

```

The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```