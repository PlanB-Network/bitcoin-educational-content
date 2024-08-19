---
term: BIP137
---

Propone un formato standardizzato per la firma di messaggi con chiavi private Bitcoin e i relativi indirizzi, al fine di dimostrare la proprietà di un indirizzo. Questo BIP mira a risolvere l'ambiguità relativa ai diversi tipi di indirizzi Bitcoin (P2PKH, P2SH, P2WPKH...) quando si firma un messaggio. Introduce un metodo per distinguere esplicitamente questi formati di indirizzo attraverso le firme. Queste firme sono utili per varie applicazioni come la prova di fondi, l'audit e altri usi che richiedono l'autenticazione di un indirizzo tramite la sua chiave privata. BIP322 ha successivamente introdotto un nuovo formato di firma che consente di estendere questo standard e generalizzarlo per qualsiasi tipo di script.