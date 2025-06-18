---
term: REPLAY-ANGREP
---

I Bitcoin-sammenheng oppstår et replay-angrep når en gyldig transaksjon på én Blockchain reproduseres på ondsinnet vis på en annen Blockchain som har samme transaksjonshistorikk. Med andre ord kan en transaksjon som sendes på én kanal, kopieres på en annen uten samtykke fra avsenderen av den første transaksjonen.


La oss ta et eksempel med en hypotetisk Hard Fork fra Bitcoin, kalt "*BitcoinBis*". Hvis du betaler i bitcoins for å kjøpe en baguette fra en baker på den virkelige Blockchain Bitcoin, kan den samme bakeren gjenta den legitime transaksjonen på *BitcoinBis* for å få det samme beløpet i kryptovaluta på denne Fork, uten noen handling fra din side.


Denne typen angrep kan bare forekomme ved Blockchain-forgrening med to uavhengige kjeder som vedvarer over tid. Vanligvis vil dette være tilfelle med Hard Fork. For at et replay-angrep skal være mulig, må de to blokkjedene ha en felles historikk, og den dupliserte transaksjonen må bruke UTXO-er som er opprettet fra tidligere transaksjoner som fant sted før de to kjedene ble splittet, eller fra tidligere transaksjoner som selv allerede har blitt replayet i et tidligere replay-angrep.


Generelt sett består et replay-angrep i databehandling av å snappe opp og gjenbruke gyldige data for å lure et system ved å gjenta den opprinnelige overføringen. Dette kan noen ganger føre til identitetstyveri i et nettverk.


> når det gjelder et replay-angrep på en Bitcoin-transaksjon, omtales dette noen ganger bare som en "replay-transaksjon". "*