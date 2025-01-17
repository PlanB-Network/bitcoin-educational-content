---
term: EXKLUZIVNÍ NEBO

---
Základní funkce booleovské logiky. Funkce "Exclusive Or" neboli XOR ("*Exclusive or*") přijímá dva booleovské operandy, z nichž každý je pravda nebo nepravda, a dává pravdivý výstup pouze tehdy, když se oba operandy liší. Jinými slovy, výstup operace `XOR` je pravdivý, pokud je pravdivý přesně jeden (ale ne oba) z operandů. Například výsledkem operace `XOR` mezi operacemi `1` a `0` bude `1`. Poznamenáváme: $1 \oplus 0 = 1$. Podobně lze operaci `XOR` provádět i na delších posloupnostech bitů. Například: $10110 \oplus 01110 = 11000$. Každý bit posloupnosti se porovná se svým protějškem a provede se operace `XOR`. Zde je pravdivostní tabulka pro operaci `XOR`:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |

|:---:|:---:|:------------:|

| $0$ | $0$ | $0$ |

| $0$ | $1$ | $1$ |

| $1$ | $0$ | $1$ |

| $1$ | $1$ | $0$ |

</div>

Operace `XOR` se používá v mnoha oblastech informatiky, zejména v kryptografii, pro své zajímavé vlastnosti, jako jsou:


- Jeho komutativnost: pořadí operandů nemá vliv na výsledek. Pro dvě dané proměnné $D$ a $E$: $D \oplus E = E \oplus D$;
- Jeho asociativita: seskupení operandů nemá vliv na výsledek. Pro tři dané proměnné $A$, $B$ a $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Má neutrální prvek `0`: operand xorovaný s 0 se vždy rovná operandu. Pro danou proměnnou $A$: $A \oplus 0 = A$;
- Každý prvek je jeho vlastní inverzí. Pro danou proměnnou $A$: $A \oplus A = 0$.

V kontextu Bitcoinu se operace `XOR` samozřejmě používá na mnoha místech. Operace `XOR` je například masivně využívána ve funkci `SHA256`, která je hojně využívána v protokolu Bitcoin. Některé protokoly, jako například *SeedXOR* společnosti Coldcard, používají toto primitivum i pro další aplikace. Najdeme ho také v BIP47 pro šifrování opakovaně použitelného platebního kódu při jeho přenosu.

V širší oblasti kryptografie lze `XOR` použít jako symetrický šifrovací algoritmus. Tento algoritmus se nazývá "One-Time Pad" nebo "Vernamova šifra", pojmenovaná po svém vynálezci. Ačkoli je tento algoritmus nepraktický kvůli délce klíče, je jedním z mála šifrovacích algoritmů, které jsou uznávány jako bezpodmínečně bezpečné.