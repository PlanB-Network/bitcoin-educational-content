---
term: PÜHKIMISTEHING

---
Ahelanalüüsis kasutatav muster või tehingumudel tehingu olemuse kindlaksmääramiseks. Seda mudelit iseloomustab ühe UTXO tarbimine sisendina ja ühe UTXO tootmine väljundina. Selle mudeli tõlgendus seisneb selles, et tegemist on enesevahetusega. Kasutaja on oma bitcoinid üle kandnud iseendale, teisele talle kuuluvale aadressile. Kuna tehingus ei toimu mingeid muutusi, on väga ebatõenäoline, et tegemist on maksega. Tõepoolest, kui makse tehakse, on peaaegu võimatu, et maksja UTXO oleks täpselt sama suur kui müüja poolt nõutav summa, lisaks tehingutasudele. Üldiselt on maksja seetõttu sunnitud tekitama muutuste väljundi. Siis teame, et vaadeldav kasutaja on tõenäoliselt ikka veel selle UTXO valduses. Kui me teame ahelanalüüsi kontekstis, et tehingus sisendina kasutatud UTXO kuulub Alice'ile, võime eeldada, et ka väljundis olev UTXO kuulub talle.

![](../../dictionnaire/assets/6.webp)

> ► *Fransi keeles võiks "pühkimistehingut" tõlkida kui "transaction de balayage"