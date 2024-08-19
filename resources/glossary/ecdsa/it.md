---
term: ECDSA
---

Acronimo di "Elliptic Curve Digital Signature Algorithm" (Algoritmo di Firma Digitale basato su Curve Ellittiche). Si tratta di un algoritmo di firma digitale basato sulla crittografia a curve ellittiche (ECC). È una variante del DSA (Digital Signature Algorithm). ECDSA utilizza le proprietà delle curve ellittiche per fornire livelli di sicurezza paragonabili a quelli degli algoritmi tradizionali di chiave pubblica, come RSA, pur utilizzando dimensioni di chiave significativamente inferiori. ECDSA consente la generazione di coppie di chiavi (chiavi pubbliche e private) così come la creazione e la verifica di firme digitali.

Nel contesto di Bitcoin, ECDSA è utilizzato per derivare le chiavi pubbliche dalle chiavi private. È inoltre usato per firmare le transazioni, al fine di soddisfare uno script per sbloccare i bitcoin e spenderli. La curva ellittica utilizzata nell'ECDSA di Bitcoin è `secp256k1`, definita dall'equazione $y^2 = x^3 + 7$. Questo algoritmo è stato utilizzato sin dalla nascita di Bitcoin nel 2009. Oggi, condivide il suo posto con il protocollo Schnorr, un altro algoritmo di firma digitale introdotto con Taproot nel 2021.