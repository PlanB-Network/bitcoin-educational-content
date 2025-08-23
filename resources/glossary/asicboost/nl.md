---
term: ASICBOOST
---

ASICBOOST is een algoritmische optimalisatiemethode uitgevonden in 2016, ontworpen om de efficiëntie van Bitcoin Mining met ongeveer 20% te verhogen door het aantal berekeningen te verminderen dat nodig is voor elke Hash poging van de header. Deze techniek maakt gebruik van een functie van de SHA256 Hash functie, gebruikt voor Mining, die de gegevens in blokken verdeelt voordat ze worden verwerkt. ASICBOOST houdt één van deze blokken ongewijzigd over meerdere hashing-pogingen, waardoor de Miner slechts een deel van het werk voor dit blok hoeft te doen over meerdere pogingen. Dit delen van gegevens maakt het hergebruik van resultaten van eerdere berekeningen mogelijk, waardoor het totale aantal berekeningen dat nodig is om een geldige Hash te vinden wordt verminderd.


ASICBOOST kan in twee vormen worden gebruikt: Overt ASICBOOST en Covert ASICBOOST. De Overt ASICBOOST vorm is voor iedereen zichtbaar, omdat het het `nVersion` veld van het blok als Nonce gebruikt en de echte `Nonce` niet wijzigt. De Covert vorm probeert deze wijzigingen te verbergen door Merkle trees te gebruiken. Deze tweede methode is echter minder effectief geworden sinds de introductie van SegWit, vanwege de tweede Merkle Tree, die het aantal berekeningen verhoogt dat nodig is om het te gebruiken.


Samengevat zorgt ASICBOOST ervoor dat miners niet een echte volledige SHA256 hoeven uit te voeren voor alle hashingpogingen, aangezien een deel van het resultaat onveranderd blijft, wat het werk van miners versnelt.