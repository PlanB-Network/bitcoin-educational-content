---
term: ASSUME UTXO

---
En konfigurasjonsparameter i den ledende Bitcoin Core-klienten som gjør det mulig for en node som nettopp har blitt initialisert (men som ennå ikke har gjennomgått IBD) å utsette verifiseringen av transaksjoner og UTXO-settet til et gitt øyeblikksbilde. Konseptet baserer seg på bruk av et UTXO-sett (en liste over alle eksisterende UTXO-er på et gitt tidspunkt) som leveres av Core og antas å være nøyaktig, noe som gjør at noden svært raskt kan synkroniseres med kjeden med mest akkumulert arbeid. Siden noden hopper over det lange IBD-trinnet, blir den raskt operativ for brukeren. Anta at UTXO deler synkroniseringen (IBD) inn i to deler:


- Først utfører noden Header First Sync (kun verifisering av overskrifter) og anser UTXO-settet fra Core som gyldig;
- Når noden er i drift, vil den verifisere hele blokkhistorikken i bakgrunnen og oppdatere et nytt UTXO-sett som den selv har verifisert. Hvis dette nye UTXO-settet ikke stemmer overens med det som ble levert av Core, kommer det en feilmelding.

Anta derfor at UTXO fremskynder klargjøringen av en ny Bitcoin-node ved å utsette transaksjonsbekreftelsesprosessen og UTXO-settet gjennom et oppdatert øyeblikksbilde i Core.