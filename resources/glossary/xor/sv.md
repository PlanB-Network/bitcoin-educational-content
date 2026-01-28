---
term: XOR
definition: Grundläggande boolesk logisk operation inom kryptografi som ger sant endast när de två operanderna skiljer sig åt.
---

Akronym för operationen "Exklusivt eller", på franska "Ou exclusif" Det är en grundläggande funktion i boolesk logik. Denna operation tar två booleska operander, var och en är $sann$ eller $falsk$, och producerar en $sann$ utdata endast när de två operanderna skiljer sig åt. Med andra ord är resultatet av XOR-operationen $sant$ om exakt en (men inte båda) av operanderna är $sant$. Till exempel kommer XOR-operationen mellan $1$ och $0$ att resultera i $1$. Vi noterar:


$$
1 \oplus 0 = 1
$$


På samma sätt kan XOR-operationen utföras på längre sekvenser av bitar. Till exempel


$$
10110 \oplus 01110 = 11000
$$


Varje bit i sekvensen jämförs med sin motsvarighet och XOR-operationen tillämpas. Här är sanningstabellen för XOR-operationen:


<div align="center">


| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>


XOR-operationen används inom många områden av datavetenskap, särskilt inom kryptografi, för sina intressanta egenskaper som t.ex:


- Dess kommutativitet: ordningen på operanderna påverkar inte resultatet. För två givna variabler $D$ och $E$: $D \oplus E = E \oplus D$;
- Dess associativitet: Grupperingen av operander påverkar inte resultatet. För tre givna variabler $A$, $B$ och $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Den har ett neutralt element $0$: en operand som är xored med $0$ kommer alltid att vara lika med operanden. För en given variabel $A$: $A \oplus 0 = A$;
- Varje element är sin egen invers. För en given variabel $A$: $A \oplus A = 0$.


I samband med Bitcoin används XOR-operationen uppenbarligen på många ställen. Till exempel används XOR massivt i SHA256-funktionen, som används i stor utsträckning i Bitcoin-protokollet. Vissa protokoll som Coldcards *SeedXOR* använder också denna primitiva för andra applikationer. Den finns också i BIP47 för att kryptera den återanvändbara betalkoden under överföringen.

Inom det bredare området kryptografi kan XOR användas som en symmetrisk krypteringsalgoritm. Denna algoritm kallas "One-Time Pad" eller "Vernam Cipher", uppkallad efter dess uppfinnare. Även om den är opraktisk på grund av nyckelns längd är denna algoritm en av de enda krypteringsalgoritmer som erkänts som ovillkorligt säker.