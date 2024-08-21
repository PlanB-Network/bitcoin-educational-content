---
term: MÜNTIDE VALIK
---

Protsess, mille käigus Bitcoin'i rahakoti tarkvara valib, milliseid UTXO-sid kasutada sisenditena, et rahuldada tehingu väljundeid. Mündivaliku meetod on oluline, kuna sellel on tagajärjed tehingu maksumusele ja kasutaja privaatsusele. See püüab sageli minimeerida kasutatavate sisendite arvu, et vähendada tehingu suurust ja sellega seotud tasusid, samal ajal püüdes säilitada privaatsust, vältides erinevatest allikatest pärit müntide ühendamist (CIOH). Mündivaliku jaoks on olemas mitu meetodit, nagu *Knapsack Solver* või *Branch-and-Bound*. Kui mündivalikut teostab kasutaja käsitsi, nimetatakse seda “*Mündikontrolliks*”.

> ► *Inglise keeles viidatakse sellele kui "Coin Selection".*