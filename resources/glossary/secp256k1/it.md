---
term: SECP256K1

---
Nome dato a una specifica curva ellittica utilizzata nel protocollo Bitcoin per l'implementazione degli algoritmi di firma digitale ECDSA (*Elliptic Curve Digital Signature Algorithm*) e Schnorr. La curva `secp256k1` è stata scelta dall'inventore di Bitcoin, Satoshi Nakamoto. Ha alcune proprietà interessanti, in particolare vantaggi in termini di prestazioni.

L'uso di `secp256k1` in Bitcoin significa che ogni chiave privata (un numero casuale a 256 bit) è mappata su una corrispondente chiave pubblica attraverso l'addizione e il raddoppio del punto della chiave privata con il punto del generatore della curva `secp256k1`. Questa operazione è facile da eseguire in una direzione ma praticamente impossibile da invertire, il che costituisce la base della sicurezza delle firme digitali su Bitcoin.

La curva `secp256k1` è specificata dall'equazione della curva ellittica $y^2 = x^3 + 7$, cioè ha coefficienti $a$ pari a $0$ e $b$ pari a $7$ nella forma generale dell'equazione di una curva ellittica $y^2 = x^3 + ax + b$. `secp256k1` è definita su un campo finito il cui ordine è un numero primo molto grande, in particolare $p = 2^{256} - 2^{32} - 977$. La curva ha anche un ordine di gruppo, che è il numero di punti distinti sulla curva, un punto generatore predefinito (o punto $G$), che viene utilizzato nelle operazioni crittografiche per generare coppie di chiavi, e un cofattore pari a $1$.

> *"SEC" sta per "Standards for Efficient Cryptography". "P256" indica che la curva è definita su un campo $\mathbb{Z}_p$ dove $p$ è un numero primo a 256 bit. "K" si riferisce al nome del suo inventore, Neal Koblitz. Infine, "1" indica che questa è la prima versione di questa curva.*