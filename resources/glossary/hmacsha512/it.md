---
term: HMAC-SHA512

---
hMAC-SHA512" sta per "Hash-based Message Authentication Code - Secure Hash Algorithm 512". È un algoritmo crittografico utilizzato per verificare l'integrità e l'autenticità dei messaggi scambiati tra due parti. Combina la funzione crittografica di hash `SHA512` con una chiave segreta condivisa per generare un codice di autenticazione del messaggio (MAC) unico per ogni messaggio.

Nel contesto di Bitcoin, l'uso naturale di `HMAC-SHA512` è leggermente derivato. Questo algoritmo è utilizzato nel processo di derivazione deterministica e gerarchica dell'albero delle chiavi crittografiche di un portafoglio. l'algoritmo `HMAC-SHA512` viene utilizzato in particolare per passare dal seme alla chiave master, e poi per ogni derivazione da una coppia di genitori a coppie di figli. Questo algoritmo si trova anche all'interno di un altro algoritmo di derivazione chiamato `PBKDF2`, utilizzato per passare dalla frase di recupero e dalla passphrase al seme.