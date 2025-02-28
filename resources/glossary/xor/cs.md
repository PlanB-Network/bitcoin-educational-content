---
term: XOR

---
Zkratka pro operaci "Exclusive or", francouzsky "Ou exclusif" Jedná se o základní funkci booleovské logiky. Tato operace přijímá dva booleovské operandy, z nichž každý je $pravdivý$ nebo $nepravdivý$, a dává výstup $pravdivý$ pouze tehdy, když se oba operandy liší. Jinými slovy, výstup operace XOR je $pravdivý$, pokud je přesně jeden (ale ne oba) z operandů $pravdivý$. Například výsledkem operace XOR mezi $1$ a $0$ bude $1$. Poznamenáváme:

$$
1 \oplus 0 = 1
$$

Podobně lze operaci XOR provádět i na delších posloupnostech bitů. Například:

$$
10110 \oplus 01110 = 11000
$$

Každý bit v posloupnosti se porovná se svým protějškem a provede se operace XOR. Zde je pravdivostní tabulka pro operaci XOR:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |

|:---:|:---:|:------------:|

| $0$ | $0$ | $0$ |

| $0$ | $1$ | $1$ |

| $1$ | $0$ | $1$ |

| $1$ | $1$ | $0$ |

</div>

Operace XOR se používá v mnoha oblastech informatiky, zejména v kryptografii, pro své zajímavé vlastnosti, jako jsou:


- Jeho komutativnost: pořadí operandů nemá vliv na výsledek. Pro dvě dané proměnné $D$ a $E$: $D \oplus E = E \oplus D$;
- Jeho asociativita: seskupení operandů nemá vliv na výsledek. Pro tři dané proměnné $A$, $B$ a $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Má neutrální prvek $0$: operand xorovaný s $0$ bude vždy roven operandu. Pro danou proměnnou $A$: $A \oplus 0 = A$;
- Každý prvek je jeho vlastní inverzí. Pro danou proměnnou $A$: $A \oplus A = 0$.

V kontextu Bitcoinu se operace XOR samozřejmě používá na mnoha místech. Operace XOR se například masivně používá ve funkci SHA256, která je hojně využívána v protokolu Bitcoin. Některé protokoly, jako například *SeedXOR* společnosti Coldcard, používají toto primitivum i pro další aplikace. Vyskytuje se také v BIP47 k šifrování opakovaně použitelného platebního kódu během jeho přenosu.

V širší oblasti kryptografie lze XOR použít jako symetrický šifrovací algoritmus. Tento algoritmus se nazývá "One-Time Pad" nebo "Vernamova šifra", pojmenovaná po svém vynálezci. Ačkoli je tento algoritmus nepraktický kvůli délce klíče, je jedním z mála šifrovacích algoritmů uznávaných jako bezpodmínečně bezpečné.