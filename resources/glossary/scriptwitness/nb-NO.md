---
term: SCRIPTWITNESS

---
Et element i SegWit-transaksjonsoppføringer som inneholder signaturene og de offentlige nøklene som er nødvendige for å låse opp bitcoinsene som sendes i transaksjonen. I likhet med `scriptSig` i Legacy-transaksjoner, er imidlertid ikke `scriptWitness` plassert på samme sted. Det er faktisk denne delen, som kalles "vitnet" (`*witness*` på engelsk), som flyttes til en separat database for å løse problemet med transaksjonens formbarhet. Hver SegWit-inngang har sitt eget `scriptWitness`, og alle `scriptWitness`-elementene utgjør til sammen transaksjonens `Witness`-felt.

> vær forsiktig så du ikke forveksler `scriptWitness` med `witnessScript`. Mens `scriptWitness` inneholder vitne-dataene for en SegWit-inngang, definerer `witnessScript` utgiftsbetingelsene for en P2WSH- eller P2SH-P2WSH UTXO og utgjør et skript i seg selv, på samme måte som `redeemScript` for en P2SH-utgang*