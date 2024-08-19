---
termine: CHIAVE PUBBLICA COMPRESSA
---

Una chiave pubblica viene utilizzata negli script (direttamente sotto forma di chiave pubblica o come indirizzo) per ricevere e proteggere bitcoin. Una chiave pubblica grezza è rappresentata da un punto su una curva ellittica, consistente di due coordinate (`x, y`) ciascuna di 256 bit. In formato grezzo, una chiave pubblica misura quindi 512 bit, senza contare il byte aggiuntivo per identificare il formato. Una chiave pubblica compressa, d'altra parte, è una forma più compatta di rappresentazione della chiave pubblica. Utilizza solo la coordinata `x` e un prefisso (`02` o `03`) che indica la parità della coordinata `y` (pari o dispari).

Se semplifichiamo questo al campo dei numeri reali, dato che la curva ellittica è simmetrica rispetto all'asse x, per ogni punto $P$ (`x, y`) sulla curva, esiste un punto $P'$ (`x, -y`) che sarà anch'esso su questa stessa curva. Ciò significa che per ogni `x`, ci sono solo due possibili valori di `y`, positivo e negativo. Ad esempio, per una data ascissa `x`, ci sarebbero due punti $P1$ e $P2$ sulla curva ellittica, condividendo la stessa ascissa ma con ordinate opposte:

![](../../dictionnaire/assets/29.png)
Per scegliere tra i due potenziali punti sulla curva, viene aggiunto a `x` un prefisso che specifica quale `y` scegliere. Questo metodo permette di ridurre la dimensione di una chiave pubblica da 520 bit a soli 264 bit (8 bit di prefisso + 256 bit per `x`). Questa rappresentazione è nota come la forma compressa della chiave pubblica.

Tuttavia, nel contesto della crittografia a curva ellittica, non usiamo i numeri reali, ma un campo finito di ordine `p` (un numero primo). In questo contesto, il "segno" di `y` è determinato dalla sua parità, cioè se `y` è pari o dispari. Il prefisso `0x02` indica quindi un `y` pari, mentre `0x03` indica un `y` dispari.

Consideriamo il seguente esempio di una chiave pubblica grezza (un punto sulla curva ellittica) in esadecimale:
```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Possiamo isolare il prefisso, `x`, e `y`:
```plaintext
Prefisso = 04
Per determinare la parità di `y`, esaminiamo l'ultimo carattere esadecimale di `y`:
```plaintext
Base 16 (esadecimale): f
Base 10 (decimale): 15
y è dispari
```

Il prefisso per la chiave pubblica compressa sarà `03`. La chiave pubblica compressa in esadecimale diventa:
```plaintext
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```