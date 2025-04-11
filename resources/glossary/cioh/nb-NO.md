---
term: CIOH

---
Forkortelse for "*Common Input Ownership Heuristic*". Det er en heuristikk som brukes innen analyse av Bitcoin-kjeder, og som antar at alle input i en transaksjon tilhører samme enhet eller bruker. Når man observerer de offentlige dataene til en Bitcoin-transaksjon og oppdager flere inndata, kan man, hvis det ikke finnes noen mønstre eller annen informasjon som motbeviser dette, anta at alle inndataene til denne transaksjonen tilhørte én enkelt person (eller enhet).

Denne analyseheuristikken ble oppdaget av Satoshi Nakamoto selv, som diskuterer den i del 10 av White Paper:

> "Men forbindelsen er uunngåelig med transaksjoner med flere inndata, som nødvendigvis avslører at inndataene deres var eid av samme eier. Risikoen er at hvis eieren av en nøkkel blir avslørt, kan forbindelsene avsløre andre transaksjoner som tilhørte samme eier." - Nakamoto, S. (2008). "Bitcoin: Et elektronisk peer-to-peer-kontantsystem". Konsultert på https://bitcoin.org/bitcoin.pdf.
Selv i dag er CIOH fortsatt den viktigste heuristikken som brukes av selskaper som driver med kjedeanalyse, sammen med gjenbruk av adresser.

![](../../dictionnaire/assets/13.webp)

> på engelsk kan "CIOH" oversettes med "Common Input Ownership Heuristic"