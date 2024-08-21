---
term: GAP LIMIT
---

Parameeter, mida kasutatakse Bitcoin'i rahakottide tarkvaras, et määrata maksimaalne järjestikuste kasutamata aadresside arv, mida genereerida enne lisatehingute otsimise peatamist. Selle parameetri kohandamine on sageli vajalik rahakoti taastamisel, et tagada kõikide tehingute leidmine. Ebapiisav Gap Limit võib põhjustada mõningate tehingute puudumise, kui aadresse jäeti tuletamisfaasides vahele. Gap Limit'i suurendamine võimaldab rahakotil otsida aadresside jadas kaugemale, et taastada kõik seotud tehingud.

Tõepoolest, üksik `xpub` võib teoreetiliselt tuletada rohkem kui 4 miljardit vastuvõtvaadressi (nii sisemisi kui ka välimisi aadresse). Siiski ei saa rahakottide tarkvara neid kõiki kasutuse osas tuletada ja kontrollida ilma tohutuid operatiivkulusid kandmata. Seetõttu järgivad nad indeksi järjekorda, kuna see on tavaliselt järjekord, milles kõik rahakottide tarkvarad aadresse genereerivad. Tarkvara registreerib iga kasutatud aadressi enne järgmise juurde liikumist ja peatab oma otsingu, kui see kohtab järjestikuste tühjade aadresside arvu. Seda arvu nimetatakse Gap Limit'iks.

Kui näiteks Gap Limit on määratud väärtusele `20` ja aadress `m/84'/0'/0'/0/15/` on tühi, siis rahakott tuletaks aadresse kuni `m/84'/0'/0'/0/34/`-ni. Kui see aadresside vahemik jääb kasutamata, peatub otsing seal. Seega ei tuvastataks selles näites tehingut, mis kasutab aadressi `m/84'/0'/0'/0/40/`.