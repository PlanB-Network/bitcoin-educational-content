---
term: Avrundad betalning
definition: Kedjeanalys-heuristik som identifierar betalningen genom dess jämna belopp i en transaktion.
---

En intern heuristik för kedjeanalys på Bitcoin som möjliggör en hypotes om arten av utdata för en transaktion baserat på runda belopp. I allmänhet, när man står inför ett enkelt betalningsmönster (1 inmatning och 2 utmatningar), om en av utmatningarna spenderar ett runt belopp, så representerar den betalningen. Genom eliminering gäller att om en utgång representerar betalningen, så representerar den andra utgången förändringen. Det kan därför tolkas som att det är troligt att den användare som matar in transaktionen fortfarande har den utgång som identifierats som växeln.


Det bör noteras att denna heuristik inte alltid är tillämplig, eftersom majoriteten av betalningarna fortfarande görs i fiatvalutaenheter. När en handlare i Frankrike accepterar Bitcoin visar de i allmänhet inte stabila priser i Sats. De skulle hellre välja en konvertering mellan priset i euro och beloppet i bitcoins som ska betalas via deras POS (som BTCPay Server, till exempel). Därför bör det inte finnas ett runt tal i transaktionsutgången. Ändå kan en analytiker försöka göra denna konvertering genom att ta hänsyn till Exchange-kursen som gällde när transaktionen sändes i nätverket. Om Bitcoin en dag blir den föredragna beräkningsenheten i våra börser kan denna heuristik bli ännu mer användbar för analyser.


