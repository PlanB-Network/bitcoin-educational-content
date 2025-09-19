---
term: SCRIPTWITNESS
---

Een element in SegWit transactieboekingen dat de handtekeningen en publieke sleutels bevat die nodig zijn om de bitcoins te ontgrendelen die in de transactie zijn verzonden. Vergelijkbaar met de `scriptSig` van Legacy transacties, wordt de `scriptWitness` echter niet op dezelfde plaats geplaatst. Het is dit deel, waarnaar verwezen wordt als de "getuige" (`*witness*` in het Engels), dat verplaatst wordt naar een aparte database om het probleem van de vervormbaarheid van de transactie op te lossen. Elke SegWit invoer heeft zijn eigen `scriptWitness`, en alle `scriptWitness` Elements samen vormen het `Witness` veld van de transactie.


> verwar `scriptWitness` niet met `witnessScript`. Terwijl het `scriptWitness` de getuigegegevens bevat voor elke SegWit invoer, definieert het `witnessScript` de bestedingsvoorwaarden van een P2WSH of P2SH-P2WSH UTXO en vormt het een script op zichzelf, vergelijkbaar met de `redeemscript` voor een P2SH uitvoer.