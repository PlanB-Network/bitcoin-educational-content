---
term: Anchor
---

RGB protokollis kujutab Anchor kliendipoolset andmekogumit, mida kasutatakse ühe Commitment tehingusse kaasamise tõendamiseks. RGB protokollis koosneb Anchor järgmistest Elements:




- transaction ID Bitcoin (txid) alates Witness Transaction ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Täiendav tehingu tõendamine (ETP), kui kasutatakse Tapret Commitment mehhanismi.


Anchor teenib seega kontrollitava seose loomist konkreetse Bitcoin tehingu ja RGB protokolliga valideeritud privaatsete andmete vahel. See tagab, et need andmed on tõepoolest Blockchain-s sisalduvad, ilma et nende täpset sisu avalikustataks.