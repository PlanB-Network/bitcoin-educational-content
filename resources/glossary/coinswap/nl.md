---
term: COINSWAP
---

Protocol voor geheime overdracht van Ownership tussen gebruikers. Deze methode heeft als doel om het bezit van bitcoins over te dragen van de ene persoon naar de andere, en vice versa, zonder dat deze Exchange expliciet zichtbaar is op de Blockchain. Coinwap gebruikt smart contracts om de overdracht uit te voeren zonder dat er vertrouwen tussen de partijen nodig is.


Laten we ons een naïef voorbeeld voorstellen (dat niet werkt) met Alice en Bob. Alice bezit 1 BTC beveiligd met privésleutel $A$, en Bob bezit ook 1 BTC beveiligd met privésleutel $B$. Theoretisch zouden ze hun privésleutels via een extern communicatiekanaal kunnen Exchange-en om een geheime overdracht uit te voeren. Deze naïeve methode brengt echter een groot vertrouwensrisico met zich mee. Niets weerhoudt Alice ervan om een kopie van de $A$ privésleutel te bewaren na de Exchange en deze later te gebruiken om de bitcoins te stelen, zodra de sleutel in Bob's handen is. Bovendien is er geen garantie dat Alice niet Bob's privésleutel $B$ ontvangt en nooit haar privésleutel $A$ in Exchange doorgeeft. Deze Exchange berust dus op overmatig vertrouwen tussen de partijen en is niet effectief om een veilige, geheime overdracht van Ownership te garanderen.


Om deze problemen op te lossen en coinswap mogelijk te maken tussen partijen die elkaar niet vertrouwen, gaan we Smart contract systemen gebruiken die de Exchange "atomair" maken. Dit kunnen HTLC (*Hash Time-Locked Contracts*) of PTLC (*Point Time-Locked Contracts*) zijn. Deze twee protocollen werken op dezelfde manier, met een tijdvergrendelingssysteem dat ervoor zorgt dat de Exchange met succes wordt voltooid of volledig wordt geannuleerd, waardoor de integriteit van de fondsen van beide partijen wordt beschermd. Het belangrijkste verschil tussen HTLC en PTLC is dat HTLC hashes en preimages gebruikt om de transactie te beveiligen, terwijl PTLC Adaptor Signatures gebruikt.


In een coinswap-scenario met een HTLC of PTLC tussen Alice en Bob, vindt de Exchange op een veilige manier plaats: of het slaagt en ieder ontvangt de BTC van de ander, of het mislukt en ieder behoudt zijn eigen BTC. Dit maakt het onmogelijk voor een van de partijen om vals te spelen of de BTC van de ander te stelen.


Het gebruik van Adaptor Signatures is in deze context bijzonder interessant, omdat het het mogelijk maakt om af te zien van traditionele scripts (een mechanisme dat soms "scriptloze scripts_" wordt genoemd). Dit verlaagt de kosten van de Exchange. Een ander groot voordeel van Adaptor Handtekeningen is dat ze niet het gebruik van een gemeenschappelijke Hash voor beide partijen bij de transactie vereisen, waardoor het niet nodig is om een directe link tussen hen te onthullen in bepaalde typen Exchange.