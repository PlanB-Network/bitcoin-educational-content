---
term: XOR
---

Acroniem voor de bewerking "Exclusive or," in het Frans "Ou exclusif." Het is een fundamentele functie van Booleaanse logica. Deze bewerking neemt twee Booleaanse operanden, die elk $waar$ of $onwaar$ zijn, en produceert alleen een $waar$ uitvoer als de twee operanden verschillen. Met andere woorden, de uitvoer van de XOR-bewerking is $waar$ als precies één (maar niet beide) van de operanden $waar$ is. Bijvoorbeeld, de XOR-bewerking tussen $1$ en $0$ resulteert in $1$. We merken op:


$$
1 \oplus 0 = 1
$$


Op dezelfde manier kan de XOR-bewerking worden uitgevoerd op langere reeksen bits. Bijvoorbeeld:


$$
10110 \oplus 01110 = 11000
$$


Elk bit in de reeks wordt vergeleken met zijn tegenhanger en de XOR-bewerking wordt toegepast. Hier is de waarheidstabel voor de XOR-bewerking:


<div align="center">


| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>


De XOR-bewerking wordt gebruikt in veel gebieden van de computerwetenschap, met name in de cryptografie, vanwege de interessante eigenschappen zoals:


- De commutativiteit: de volgorde van de operanden heeft geen invloed op het resultaat. Voor twee gegeven variabelen $D$ en $E$ geldt: $D \oplus E = E \oplus D$;
- De associativiteit: de groepering van operanden heeft geen invloed op het resultaat. Voor drie gegeven variabelen $A$, $B$ en $C$ geldt: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Het heeft een neutraal element $0$: een operand xored met $0$ zal altijd gelijk zijn aan de operand. Voor een gegeven variabele $A$ geldt: $A \oplus 0 = A$;
- Elk element is zijn eigen inverse. Voor een gegeven variabele $A$ geldt: $A ƒoplus A = 0$.


In de context van Bitcoin wordt de XOR operatie duidelijk op veel plaatsen gebruikt. XOR wordt bijvoorbeeld massaal gebruikt in de SHA256 functie, die veel gebruikt wordt in het Bitcoin protocol. Sommige protocollen zoals Coldcard's *SeedXOR* gebruiken deze primitieve ook voor andere toepassingen. Het komt ook voor in BIP47 om de herbruikbare betaalcode te versleutelen tijdens de overdracht.

Op het bredere gebied van cryptografie kan XOR worden gebruikt als symmetrisch versleutelingsalgoritme. Dit algoritme heet de "One-Time Pad" of het "Vernam Cipher", genoemd naar de uitvinder. Hoewel dit algoritme onpraktisch is vanwege de lengte van de sleutel, is het een van de enige versleutelingsalgoritmen die erkend zijn als onvoorwaardelijk veilig.