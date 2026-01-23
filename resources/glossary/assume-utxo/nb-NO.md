---
term: Assume utxo

definition: En Bitcoin Core-parameter som tillater rask synkronisering av en ny node ved å bruke et øyeblikksbilde av UTXO-settet antatt gyldig, før historieverifisering i bakgrunnen.
---
Konfigurasjonsparameter i majoritetsklienten Bitcoin Core som lar en node som nettopp har blitt initialisert (men som ennå ikke har utført IBD) utsette verifiseringen av transaksjoner og UTXO-settet før et gitt snapshot. Konseptet er basert på bruken av et UTXO-sett (liste over alle eksisterende UTXO-er på et gitt tidspunkt) levert av Core og antatt å være nøyaktig, noe som gjør at noden kan synkroniseres veldig raskt på kjeden med mest akkumulert arbeid. Siden noden hopper over det lange IBD-trinnet, blir den veldig raskt funksjonell for brukeren.

Assume UTXO deler synkroniseringen (IBD) inn i to deler: Først utfører noden Header First Sync (kun verifisering av hoder) og anser UTXO-settet levert av Core som gyldig; Deretter, når den er funksjonell, vil noden verifisere den fullstendige blokkhistorikken i bakgrunnen, og oppdatere et nytt UTXO-sett som den har verifisert selv. Hvis sistnevnte ikke samsvarer med UTXO-settet levert av Core, vil den gi en feilmelding.

Assume UTXO gjør det derfor mulig å fremskynde klargjøringen av en ny Bitcoin-node ved å utsette verifiseringsprosessen for transaksjoner og UTXO-settet takket være et oppdatert snapshot levert i Core.





