---
term: BIP156

---
Forslag, kjent som Dandelion, som tar sikte på å forbedre personvernet ved transaksjonsruting i Bitcoin-nettverket for å motvirke deanonymisering. I standarddriften av Bitcoin sendes transaksjoner umiddelbart til flere noder. Hvis en observatør kan se hver transaksjon som videresendes av hver node i nettverket, kan vedkommende anta at den første noden som sender en transaksjon, også er den opprinnelige noden for transaksjonen, og at den derfor kommer fra nodens operatør. Dette fenomenet kan potensielt gjøre det mulig for observatører å koble transaksjoner, som normalt er anonyme, med IP-adresser.

Målet med BIP156 er å løse dette problemet. For å gjøre dette innfører den en ekstra fase i kringkastingen for å bevare anonymiteten før offentlig spredning. Dandelion bruker derfor først en "stem"-fase der transaksjonen sendes gjennom en tilfeldig sti av noder, før den kringkastes til hele nettverket i "fluff"-fasen. Stilken og fluffen er referanser til hvordan transaksjonen forplanter seg gjennom nettverket, og ligner formen til en løvetann (*en dandelion* på engelsk).

Denne rutingsmetoden skjuler sporet som fører tilbake til kildenoden, noe som gjør det vanskelig å spore en transaksjon gjennom nettverket tilbake til dens opprinnelse. Dandelion forbedrer dermed personvernet ved å begrense motstandernes mulighet til å avanonymisere nettverket. Denne metoden er enda mer effektiv når transaksjonen i "stem"-fasen krysser en node som krypterer nettverkskommunikasjonen sin, for eksempel med Tor eller *P2P Transport V2*. BIP156 har ennå ikke blitt lagt til i Bitcoin Core.

![](../../dictionnaire/assets/36.webp)