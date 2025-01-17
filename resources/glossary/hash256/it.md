---
term: HASH256

---
Funzione crittografica utilizzata per varie applicazioni su Bitcoin. Comporta l'applicazione della funzione SHA256 due volte sui dati in ingresso. Il messaggio viene passato una volta attraverso SHA256 e il risultato di questa operazione viene utilizzato come input per un secondo passaggio attraverso SHA256. Il risultato di questa funzione è quindi di 256 bit.

$${testo{HASH256}(x) = ´testo{SHA256}(´testo{SHA256}(x))$$