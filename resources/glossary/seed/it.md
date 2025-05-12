---
term: GRANO
---

Nel contesto specifico di un portafoglio deterministico gerarchico Bitcoin, un seed è un'informazione a 512 bit derivata da un evento casuale. Viene utilizzato per determinare in modo deterministico e gerarchico generate un insieme di chiavi private, e le corrispondenti chiavi pubbliche, per un portafoglio Bitcoin. Il seed viene spesso confuso con la frase di recupero stessa. Ma non è la stessa cosa. Il seed si ottiene applicando la funzione `PBKDF2` alla frase Mnemonic e a qualsiasi passphrase.


Il seed è stato inventato con il BIP32, che ha definito le basi del portafoglio deterministico gerarchico. In questo standard, il seed misurava 128 bit. Ciò consente di ricavare tutte le chiavi di un portafoglio da un'unica informazione, a differenza dei portafogli JBOK (*Just a Bunch Of Keys*), che richiedono nuovi backup per ogni chiave generata. Il BIP39 ha poi proposto una codifica di questo seed, per semplificarne la lettura da parte dell'uomo. Questa codifica assume la forma di una frase, generalmente indicata come frase Mnemonic o frase di recupero. Questo standard evita gli errori durante il salvataggio del seed, in particolare grazie all'uso di un checksum.


Al di fuori del contesto del Bitcoin, in crittografia in generale, un seed è un valore iniziale utilizzato per le chiavi crittografiche generate o, più in generale, per qualsiasi tipo di dato prodotto da un generatore di numeri pseudocasuali. Questo valore iniziale deve essere casuale e imprevedibile per garantire la sicurezza del sistema crittografico. Infatti, il seed introduce entropia nel sistema, ma il processo di generazione che segue è deterministico.


> *Nel linguaggio comune, la maggior parte dei bitcoiners si riferisce alla frase Mnemonic quando parla di "seed", e non allo stato di derivazione intermedio che si trova tra la frase Mnemonic e la chiave master