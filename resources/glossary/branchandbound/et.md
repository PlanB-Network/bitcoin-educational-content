---
term: BRANCH-AND-BOUND

---
Meetod, mida kasutatakse sisendite valimiseks Bitcoin Core'i rahakotis alates versioonist 0.17 ja mille leiutas Murch. Branch-and-Bound (BnB) on otsing, et leida UTXOde kogum, mis vastab täpselt tehingus täidetavate väljundite hulgale, et minimeerida muutusi ja nendega seotud tasusid. Selle eesmärk on vähendada raiskamise kriteeriumi, mis võtab arvesse nii koheseid kulusid kui ka muutusega eeldatavaid tulevasi kulusid. See meetod on tasude osas täpsem võrreldes varasemate heuristikatega, nagu *Knapsack Solver*. *Branch-and-Bound* on inspireeritud samanimelisest probleemilahenduse meetodist, mille leiutasid 1960. aastal Ailsa Land ja Alison Harcourt.

> ► *Seda meetodit nimetatakse mõnikord ka "Murchi algoritmiks", viidates selle leiutajale