---
term: DANDELION

---
Et forslag som tar sikte på å forbedre personvernet ved transaksjonsruting i Bitcoin-nettverket for å motvirke deanonymisering. I standarddriften av Bitcoin sendes transaksjoner umiddelbart til flere noder. Dette fenomenet kan potensielt gjøre det mulig for observatører å koble transaksjoner, som normalt er anonyme, med IP-adresser. Målet med BIP156 er å løse dette problemet. For å gjøre dette innfører den en ekstra fase i kringkastingsprosessen for å bevare anonymiteten før offentlig spredning. Dandelion bruker derfor først en "stem"-fase der transaksjonen sendes gjennom en tilfeldig sti av noder, før den kringkastes til hele nettverket i en "fluff"-fase. Stilken og fluffen er referanser til hvordan transaksjonen forplanter seg gjennom nettverket, og ligner på formen til en løvetann. Denne rutingsmetoden tilslører sporet som fører tilbake til kildenoden, noe som gjør det vanskelig å spore en transaksjon gjennom nettverket tilbake til dens opprinnelse.

![](../../dictionnaire/assets/36.webp)