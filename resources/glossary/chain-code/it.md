---
termine: CHAIN CODE
---

Nel contesto della derivazione deterministica gerarchica (HD) dei portafogli Bitcoin, il chain code è un valore di sale crittografico a 256 bit utilizzato per generare chiavi figlie da una chiave genitore, secondo lo standard BIP32. Il chain code è usato in combinazione con la chiave genitore e l'indice del figlio per generare deterministicamente una nuova coppia di chiavi (chiave privata e chiave pubblica) senza rivelare la chiave genitore o altre chiavi figlie derivate.

Pertanto, esiste un unico chain code per ogni coppia di chiavi. Il chain code è ottenuto o tramite l'hashing del seed del portafoglio e prendendo la metà destra dei bit. In questo caso, è definito come un master chain code, associato alla master private key. Alternativamente, può essere ottenuto facendo l'hashing di una chiave genitore con il suo parent chain code e un indice, poi mantenendo i bit di destra. Questo è quindi definito come un child chain code.

È impossibile derivare le chiavi senza conoscere il chain code associato a ogni coppia genitore. Introduce dati pseudo-casuali nel processo di derivazione per assicurare che la generazione di chiavi crittografiche rimanga imprevedibile per gli attaccanti pur essendo deterministica per il detentore del portafoglio.

> ► *In inglese, un "code de chaîne" è chiamato "chain code", e un "code de chaîne maître" è chiamato "master chain code".*