---
term: SWEEP TRANSACTION
---

Mustrit või tehingumudelit, mida kasutatakse ahelanalüüsis tehingu olemuse määramiseks. Seda mudelit iseloomustab ühe UTXO tarbimine sisendina ja ühe UTXO tootmine väljundina. Selle mudeli tõlgendus on, et tegemist on eneseülekandega. Kasutaja on kandnud oma bitcoine iseendale, teisele enda omanduses olevale aadressile. Kuna tehingus ei toimu muudatust, on väga ebatõenäoline, et tegemist on maksega. Tõepoolest, kui makse sooritatakse, on peaaegu võimatu, et maksjal oleks UTXO, mis täpselt vastab müüja nõutud summale, lisaks tehingutasudele. Üldiselt on maksja seetõttu sunnitud tootma muudatuse väljundi. Siis teame, et täheldatud kasutaja on tõenäoliselt endiselt selle UTXO omanik. Ahelanalüüsi kontekstis, kui me teame, et tehingus sisendina kasutatud UTXO kuulub Alicele, võime eeldada, et väljundis olev UTXO kuulub samuti temale.

![](../../dictionnaire/assets/6.png)

> ► *Prantsuse keeles võidakse "sweep transaction" tõlkida kui "transaction de balayage".*