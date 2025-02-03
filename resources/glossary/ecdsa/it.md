---
term: ECDSA

---
Acronimo di "Elliptic Curve Digital Signature Algorithm" È un algoritmo di firma digitale basato sulla crittografia a curva ellittica (ECC). È una variante del DSA (Digital Signature Algorithm). ECDSA utilizza le proprietà delle curve ellittiche per fornire livelli di sicurezza paragonabili a quelli dei tradizionali algoritmi a chiave pubblica, come RSA, pur utilizzando chiavi di dimensioni notevolmente inferiori. L'ECDSA consente di generare coppie di chiavi (pubbliche e private) e di creare e verificare firme digitali.

Nel contesto di Bitcoin, ECDSA viene utilizzato per ricavare chiavi pubbliche da chiavi private. Viene anche utilizzato per firmare le transazioni, al fine di soddisfare uno script per sbloccare i bitcoin e spenderli. La curva ellittica utilizzata nell'ECDSA di Bitcoin è `secp256k1`, definita dall'equazione $y^2 = x^3 + 7$. Questo algoritmo è stato utilizzato fin dalla nascita di Bitcoin nel 2009. Oggi condivide il suo posto con il protocollo Schnorr, un altro algoritmo di firma digitale introdotto con Taproot nel 2021.