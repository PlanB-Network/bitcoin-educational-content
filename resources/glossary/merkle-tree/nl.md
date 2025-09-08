---
term: Merkle Tree
---

Een Merkle Tree is een cryptografische accumulator. Het is een methode om het lidmaatschap van een bepaald stuk informatie binnen een grotere set te bewijzen. Het is een datastructuur die de verificatie van informatie in een compact formaat vergemakkelijkt. In het Bitcoin systeem worden Merkle Trees gebruikt om de transacties van een blok te groeperen en samen te vatten in een enkele Hash, genaamd de Merkle Root (of "*Root Hash*"). Elke transactie wordt gehasht, daarna worden de aangrenzende hashes hiërarchisch samen gehasht totdat de Merkle Root is verkregen.


![](../../dictionnaire/assets/1.webp)


Deze structuur maakt het mogelijk om snel te verifiëren of een specifieke transactie in een bepaald blok zit, zonder alle transacties te hoeven analyseren. Als ik bijvoorbeeld alleen de Merkle Root heb en ik wil verifiëren dat `TX 7` inderdaad deel uitmaakt van de boom, dan heb ik alleen de volgende bewijzen nodig:


- tX 7`;
- gW-6 8`;
- gW-7 5-6`;
- `Hash 1-2-3-4`.

Met deze stukjes informatie kan ik de tussenliggende knooppunten berekenen tot aan de Merkle Root.


![](../../dictionnaire/assets/2.webp)


Merkle Trees worden met name gebruikt voor lichte knooppunten (bekend als "SPV") die alleen de blokkoppen bewaren, maar niet de transacties. Deze structuur wordt ook gevonden in het UTREEXO protocol, een protocol dat het mogelijk maakt om de UTXO set van knooppunten te condenseren, en in de MAST Taproot.


> ► *De Merkle Tree is vernoemd naar Ralph Merkle, een cryptograaf die deze structuur in 1979 ontwierp. Een Merkle Tree kan ook een "Hash boom" genoemd worden. In het Frans wordt het "Arbre de Merkle" of "arbre de hachage" genoemd.*