---
term: Assignment
---

I logikken til RGB-protokollen tilsvarer en Assignment en transaksjonsutgang som endrer, oppdaterer eller oppretter visse egenskaper i tilstanden til en Contract. En Assignment består av to Elements:




- En Seal Definition (referanse til en spesifikk UTXO);
- En Owned State (data som beskriver tilstanden som er knyttet til denne nye innehaveren).


En Assignment indikerer derfor at en del av staten (for eksempel en eiendel) nå er allokert til en bestemt innehaver, identifisert via en Single-Use Seal knyttet til en UTXO.