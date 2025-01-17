---
term: PERCORSO DI RECUPERO

---
In un software di portafoglio che utilizza Miniscript, come ad esempio Liana, i percorsi di recupero si riferiscono a set di chiavi che diventano operativi solo dopo un periodo definito di inattività nello script che blocca i bitcoin (timelock). I percorsi di recupero sono utilizzabili solo una volta scaduti i timelock, offrendo così un metodo per recuperare i fondi quando il percorso primario non è disponibile. Consideriamo l'esempio di uno script che incorpora 2 chiavi distinte: la chiave A, che autorizza la spesa immediata dei bitcoin, e la chiave B, che consente di spenderli dopo un ritardo definito da un timelock di 52.560 blocchi. In questo esempio, la chiave A proviene dal percorso primario, mentre la chiave B proviene dal percorso di recupero.