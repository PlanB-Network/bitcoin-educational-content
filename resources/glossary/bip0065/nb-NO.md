---
term: BIP0065

definition: Introduksjon av opkoden OP_CHECKLOCKTIMEVERIFY som gjør det mulig å låse bitcoins frem til en bestemt dato eller blokkhøyde.
---
Innførte en ny opcode kalt `OP_CHECKLOCKTIMEVERIFY` som gjør det mulig å gjøre en UTXO ubrukelig frem til et spesifisert fremtidig tidspunkt. Implementeringen av denne BIP-en krevde en soft fork, som fant sted 14. desember 2015. Den introduserte også versjon 4 av blokkene.