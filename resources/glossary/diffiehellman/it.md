---
term: DIFFIE-HELLMAN

---
Metodo crittografico che consente a due parti di generare un segreto condiviso su un canale di comunicazione non protetto. Questo segreto può essere utilizzato per crittografare le comunicazioni tra le due parti. Diffie-Hellman utilizza l'aritmetica modulare in modo che, anche se un attaccante può osservare gli scambi, non può dedurre il segreto condiviso senza risolvere un difficile problema matematico: il logaritmo discreto. In Bitcoin viene talvolta utilizzata una variante di DH chiamata ECDH che utilizza una curva ellittica, soprattutto per i protocolli a indirizzo statico come Silent Payments o BIP47.