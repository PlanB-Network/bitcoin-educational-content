---
term: XOR
---

Akronym pro operaci "Exkluzivní nebo," ve francouzštině "Ou exclusif." Jedná se o základní funkci Booleovské logiky. Tato operace bere dva Booleovské operandy, každý může být $true$ nebo $false$, a produkuje výstup $true$ pouze tehdy, když se dva operandy liší. Jinými slovy, výstup operace XOR je $true$, pokud přesně jeden (ale ne oba) z operandů je $true$. Například operace XOR mezi $1$ a $0$ bude mít výsledek $1$. Poznamenáváme:

$$
1 \oplus 0 = 1
$$

Podobně lze operaci XOR provádět na delších sekvencích bitů. Například:

$$
10110 \oplus 01110 = 11000
$$

Každý bit v sekvenci je porovnán se svým protějškem a je na něj aplikována operace XOR. Zde je pravdivostní tabulka pro operaci XOR:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>

Operace XOR se používá v mnoha oblastech informatiky, zejména v kryptografii, pro její zajímavé vlastnosti, jako jsou:
* Její komutativita: pořadí operandů neovlivňuje výsledek. Pro dvě dané proměnné $D$ a $E$: $D \oplus E = E \oplus D$;
* Její asociativita: seskupení operandů neovlivňuje výsledek. Pro tři dané proměnné $A$, $B$ a $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
* Má neutrální prvek $0$: operand xorovaný s $0$ bude vždy roven operandu. Pro danou proměnnou $A$: $A \oplus 0 = A$;
* Každý prvek je svým vlastním inverzem. Pro danou proměnnou $A$: $A \oplus A = 0$.

V kontextu Bitcoinu je operace XOR samozřejmě používána na mnoha místech. Například XOR je masivně používán ve funkci SHA256, která je široce používána v protokolu Bitcoinu. Některé protokoly, jako je *SeedXOR* od Coldcard, také používají tuto primitivu pro jiné aplikace. Najdeme ji také v BIP47 pro šifrování opakovaně použitelného platebního kódu během jeho přenosu.
V širším oboru kryptografie lze XOR použít jako symetrický šifrovací algoritmus. Tento algoritmus se nazývá "One-Time Pad" nebo "Vernamova šifra" po svém vynálezci. Ačkoliv je kvůli délce klíče nepraktický, tento algoritmus je jedním z mála šifrovacích algoritmů, které jsou uznávány jako bezpodmínečně bezpečné.