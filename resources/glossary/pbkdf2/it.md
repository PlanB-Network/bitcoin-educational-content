---
term: PBKDF2

---
`PBKDF2` sta per *Password-Based Key Derivation Function 2*. È un metodo per creare chiavi crittografiche da una password utilizzando una funzione di derivazione. Prende in input una password, un sale crittografico e applica iterativamente una funzione predeterminata (spesso una funzione hash come `SHA256` o una `HMAC`) a questi dati. Questo processo viene ripetuto molte volte per generare una chiave crittografica.

Nel contesto di Bitcoin, `PBKDF2` viene utilizzato insieme alla funzione `HMAC-SHA512` per creare il seme di un portafoglio deterministico e gerarchico (seed) da una frase di recupero di 12 o 24 parole. Il sale crittografico utilizzato in questo caso è la passphrase BIP39 e il numero di iterazioni è `2048`.