---
term: Entropianalys
definition: Indikator som mäter analytikers brist på kunskap om konfigurationen av en Bitcoin-transaktion.
---

När det gäller kedjeanalys är entropi också namnet på en indikator som härrör från Shannons entropi och som uppfanns av LaurentMT. Denna indikator gör det möjligt att mäta den brist på kunskap som analytiker har om den exakta konfigurationen av en Bitcoin-transaktion. Med andra ord, ju högre entropi en transaktion har, desto svårare blir det för analytiker att identifiera rörelserna av bitcoins mellan in- och utgångar.


I praktiken visar entropin om en transaktion, ur en extern observatörs perspektiv, ger flera möjliga tolkningar, enbart baserat på mängden in- och utdata, utan att ta hänsyn till andra externa eller interna mönster och heuristiker. Hög entropi är då synonymt med bättre sekretess för transaktionen.


Entropi definieras som den binära logaritmen av antalet möjliga kombinationer. Här är den formel som används där $E$ representerar transaktionens entropi och $C$ antalet möjliga tolkningar:


$$
E = \log_2(C)
$$


Med hänsyn till värdena för de UTXO:er som är involverade i transaktionen representerar antalet tolkningar $C$ antalet sätt på vilka ingångar kan associeras med utgångar. Med andra ord bestämmer det antalet tolkningar som en transaktion kan ge upphov till från en extern observatörs synvinkel som analyserar den.