---
term: Speedy trial

definition: Metodo per l'attivazione rapida di un soft fork con ritardo ridotto, utilizzato per Taproot.
---
Metodo di attivazione di un soft fork inizialmente concepito per Taproot all'inizio del 2021 da David A. Harding sulla base di un'idea di Russell O'Connor. Il principio è quello di utilizzare il metodo BIP8 con un parametro `LOT` impostato su `false`, riducendo il periodo di attivazione a soli 3 mesi. Questo periodo di voto ridotto consente una rapida verifica dell'approvazione dei minatori. Se la soglia di approvazione richiesta viene raggiunta durante uno dei periodi, il soft fork viene bloccato. Verrà attivata diversi mesi dopo, dando così ai minatori il tempo necessario per aggiornare il proprio software.

Il successo di questo metodo per Taproot, che ha goduto di un ampio consenso all'interno della comunità Bitcoin, non garantisce tuttavia la sua efficacia per tutti gli aggiornamenti. Sebbene il metodo Speedy Trial consenta un'attivazione più rapida, alcuni sviluppatori esprimono preoccupazioni sul suo utilizzo futuro. Temono che possa portare a una successione troppo rapida di soft fork, che potrebbero minacciare la stabilità e la sicurezza del protocollo Bitcoin. Rispetto al BIP8 con il parametro `LOT=true`, il metodo Speedy Trial è molto meno minaccioso per i minatori. Non è previsto alcun UASF automatico. Questo metodo di attivazione non è ancora stato formalizzato in un BIP.

