---
term: CPFP (Child Pays For Parent)
definition: Methode waarmee de ontvanger een vastgelopen transactie kan versnellen door een child-transactie met hoge kosten aan te maken.
---

Een transactiemechanisme gericht op het versnellen van de bevestiging van een Bitcoin transactie, vergelijkbaar met wat Replace-by-fee (RBF) doet, maar dan van de kant van de ontvanger. Wanneer een transactie met vergoedingen die te laag zijn in vergelijking met de markt, vast blijft zitten in de mempools van nodes en niet snel genoeg bevestigd wordt, kan de ontvanger een nieuwe transactie doen, waarbij de bitcoins die in de geblokkeerde transactie zijn ontvangen, worden uitgegeven, ook al is deze nog niet bevestigd. Deze tweede transactie vereist noodzakelijkerwijs dat de eerste wordt gemined om te worden bevestigd. Miners worden dus gedwongen om beide transacties samen op te nemen. De tweede transactie zal veel meer transactiekosten opleveren dan de eerste, op zo'n manier dat de gemiddelde kosten mijnwerkers aanmoedigen om beide transacties op te nemen. De kindtransactie (de tweede) betaalt voor de oudertransactie die vastzit (de eerste). Daarom wordt het een "CPFP" genoemd


CPFP zorgt er dus voor dat de ontvanger sneller over zijn geld kan beschikken ondanks de lage initiële kosten voor de verzender, in tegenstelling tot RBF (*Replace-by-fee*), waarbij de verzender het initiatief kan nemen om zijn eigen transactie te versnellen door de kosten te verhogen.