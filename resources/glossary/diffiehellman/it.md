---
term: DIFFIE-HELLMAN
---

Metodo crittografico che consente a due parti di generare un segreto condiviso attraverso un canale di comunicazione non sicuro. Questo segreto può poi essere utilizzato per cifrare la comunicazione tra le due parti. Diffie-Hellman utilizza l'aritmetica modulare in modo tale che, anche se un attaccante può osservare gli scambi, non può dedurre il segreto condiviso senza risolvere un difficile problema matematico: il logaritmo discreto. In Bitcoin, una variante di DH chiamata ECDH che utilizza una curva ellittica è talvolta usata, specialmente per protocolli di indirizzi statici come i Pagamenti Silenziosi o BIP47.