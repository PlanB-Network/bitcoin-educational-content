---
term: P2P TRANSPORT V2

---
Ny versjon av Bitcoins P2P-transportprotokoll med opportunistisk kryptering for å forbedre personvernet og sikkerheten i kommunikasjonen mellom noder. Denne forbedringen tar sikte på å løse flere problemer med grunnversjonen av P2P-protokollen, blant annet ved å gjøre utvekslede data umulig å skille fra hverandre for en passiv observatør (for eksempel en internettleverandør), noe som reduserer risikoen for sensur og angrep gjennom deteksjon av spesifikke mønstre i datapakker.

Den implementerte krypteringen inkluderer ikke autentisering for å unngå å øke kompleksiteten unødvendig og for ikke å kompromittere nettverkstilkoblingens tillatelsesløse natur. Denne nye P2P-transportprotokollen gir likevel bedre sikkerhet mot passive angrep og gjør aktive angrep betydelig mer kostbare og lettere å oppdage (særlig MITM-angrep). Innføringen av en pseudotilfeldig datastrøm gjør det vanskeligere for angripere som ønsker å sensurere eller manipulere kommunikasjonen.

P2P-transport V2 ble inkludert som et alternativ (deaktivert som standard) i versjon 26.0 av Bitcoin Core, som ble distribuert i desember 2023. Den kan aktiveres med alternativet `v2transport=1` i konfigurasjonsfilen.