---
term: CISA
---

Forkortelse for "Cross-Input Signature Aggregation". Dette er et teknisk forslag som er utformet for å optimalisere størrelsen på Bitcoin-transaksjoner ved å redusere antallet signaturer som kreves for å validere dem.


I dag må hver input i en transaksjon på Bitcoin ha en individuell signatur før den kan konsumeres. Dette beviser at eieren av den aktuelle UTXO har autorisert transaksjonen. Med CISA er målet å kombinere signaturene til alle inndataene i en enkelt transaksjon til én enkelt signatur som dekker alle inndataene. Dette vil gjøre det mulig å redusere størrelsen på transaksjoner med mange inndata, og dermed også redusere kostnadene. Dette vil være spesielt nyttig for dem som utfører coinjoins eller konsolideringer, samtidig som det gjør det mulig å bekrefte flere transaksjoner på Bitcoin uten å endre blokkstørrelser eller intervaller. CISA er basert på Schnorr-protokollen, som muliggjør lineær aggregering av signaturer. Det betyr at en enkelt signatur kan bevise besittelsen av flere uavhengige nøkler.


Det er imidlertid svært komplisert å implementere CISA på Bitcoin, ettersom det krever dyptgripende endringer i måten skriptene fungerer på. For øyeblikket gjøres skriptverifisering på Bitcoin inngang for inngang. Å gå over til en modell der en hel transaksjon sjekkes på én gang, slik CISA foreslår, er langt fra en triviell endring.