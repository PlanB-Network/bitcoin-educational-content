---
term: CHIAVE PUBBLICA COMPRESSA

---
Una chiave pubblica viene utilizzata negli script (direttamente sotto forma di chiave pubblica o come indirizzo) per ricevere e proteggere i bitcoin. Una chiave pubblica grezza è rappresentata da un punto su una curva ellittica, costituito da due coordinate (`x, y`) di 256 bit ciascuna. In formato grezzo, una chiave pubblica misura quindi 512 bit, senza contare il byte aggiuntivo per identificare il formato. Una chiave pubblica compressa, invece, è una forma più compatta di rappresentazione della chiave pubblica. Utilizza solo la coordinata `x` e un prefisso (`02` o `03`) che indica la parità della coordinata `y` (pari o dispari).

Semplificando al campo dei numeri reali, dato che la curva ellittica è simmetrica rispetto all'asse x, per qualsiasi punto $P$ (`x, y`) sulla curva, esiste un punto $P'$ (`x, -y`) che si troverà anch'esso sulla stessa curva. Ciò significa che per ogni `x`, ci sono solo due possibili valori di `y`, positivo e negativo. Ad esempio, per una data ascissa `x`, ci saranno due punti $P1$ e $P2$ sulla curva ellittica, che condividono la stessa ascissa ma con ordinate opposte:

![](../../dictionnaire/assets/29.webp)

Per scegliere tra i due punti potenziali della curva, a `x` viene aggiunto un prefisso che specifica quale `y` scegliere. Questo metodo consente di ridurre le dimensioni di una chiave pubblica da 520 bit a soli 264 bit (8 bit di prefisso + 256 bit per `x`). Questa rappresentazione è nota come forma compressa della chiave pubblica.

Tuttavia, nel contesto della crittografia a curve ellittiche, non utilizziamo i numeri reali, ma un campo finito di ordine `p` (un numero primo). In questo contesto, il "segno" di `y` è determinato dalla sua parità, cioè se `y` è pari o dispari. Il prefisso `0x02` indica quindi un `y` pari, mentre `0x03` indica un `y` dispari.

Si consideri il seguente esempio di chiave pubblica grezza (un punto della curva ellittica) in esadecimale:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Possiamo isolare il prefisso, `x' e `y':

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Base 16 (esadecimale): f

Base 10 (decimale): 15

y è dispari

```
The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```