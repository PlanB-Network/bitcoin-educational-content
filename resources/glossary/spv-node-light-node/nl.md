---
term: SPV-node (light node)
definition: Light client die transacties valideert door alleen blokheaders op te slaan en Merkle-proofs te verifiëren.
---

Een SPV (*Simple Payment Verification*) node, soms een "light node" genoemd, is een lichtgewicht client van een Bitcoin node waarmee gebruikers transacties kunnen valideren zonder de hele Blockchain te hoeven opslaan. In plaats daarvan slaat een SPV node alleen de block headers op en verkrijgt informatie over specifieke transacties door indien nodig volledige nodes te bevragen. Dit verificatieprincipe wordt mogelijk gemaakt door de structuur van transacties in Bitcoin blokken, die georganiseerd zijn binnen een cryptografische accumulator (Merkle Tree).


Deze aanpak is voordelig voor apparaten met beperkte middelen, zoals mobiele telefoons. SPV nodes zijn echter afhankelijk van volledige nodes voor de beschikbaarheid van informatie, wat een extra niveau van vertrouwen met zich meebrengt en dus minder veilig is dan volledige nodes. SPV nodes kunnen transacties niet autonoom valideren, maar ze kunnen wel controleren of een transactie is opgenomen in een blok door Merkle bewijzen te raadplegen.