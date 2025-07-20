---
term: XOR
---

Akronim operacji "Wyłącz lub", po francusku "Ou exclusif" Jest to podstawowa funkcja logiki boolowskiej. Operacja ta przyjmuje dwa operandy boolowskie, z których każdy jest $prawdą$ lub $fałszem$, i daje wynik $prawdziwy$ tylko wtedy, gdy oba operandy się różnią. Innymi słowy, wynikiem operacji XOR jest $true$, jeśli dokładnie jeden (ale nie oba) z operandów jest $true$. Na przykład, operacja XOR pomiędzy $1$ i $0$ da w wyniku $1$. Zauważamy:


$$
1 \oplus 0 = 1
$$


Podobnie, operacja XOR może być wykonywana na dłuższych sekwencjach bitów. Na przykład:


$$
10110 \oplus 01110 = 11000
$$


Każdy bit w sekwencji jest porównywany ze swoim odpowiednikiem i wykonywana jest operacja XOR. Oto tabela prawdy dla operacji XOR:


<div align="center">


| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>


Operacja XOR jest wykorzystywana w wielu dziedzinach informatyki, zwłaszcza w kryptografii, ze względu na jej interesujące cechy, takie jak:


- Jego przemienność: kolejność operandów nie wpływa na wynik. Dla dwóch zmiennych $D$ i $E$: $D \oplus E = E \oplus D$;
- Jego asocjatywność: grupowanie operandów nie wpływa na wynik. Dla trzech zmiennych $A$, $B$ i $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Ma neutralny element $0$: operand xored z $0$ zawsze będzie równy operandowi. Dla danej zmiennej $A$: $A \oplus 0 = A$;
- Każdy element jest swoją własną odwrotnością. Dla danej zmiennej $A$: $A \oplus A = 0$.


W kontekście Bitcoin operacja XOR jest oczywiście używana w wielu miejscach. Na przykład XOR jest masowo wykorzystywany w funkcji SHA256, która jest szeroko stosowana w protokole Bitcoin. Niektóre protokoły, takie jak *SeedXOR* firmy Coldcard, również używają tego prymitywu do innych zastosowań. Występuje również w BIP47 do szyfrowania kodu płatności wielokrotnego użytku podczas jego transmisji.

W szerszej dziedzinie kryptografii, XOR może być używany jako symetryczny algorytm szyfrowania. Algorytm ten nazywany jest "One-Time Pad" lub "szyfrem Vernama", od nazwiska jego wynalazcy. Choć niepraktyczny ze względu na długość klucza, algorytm ten jest jednym z niewielu algorytmów szyfrowania uznawanych za bezwarunkowo bezpieczne.