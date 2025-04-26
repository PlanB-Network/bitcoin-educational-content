---
term: XOR

---
Akronym for operasjonen "eksklusivt eller", på fransk "Ou exclusif" Det er en grunnleggende funksjon i boolsk logikk. Denne operasjonen tar to boolske operander, som hver er $sann$ eller $falsk$, og produserer en $sann$ utgang bare når de to operandene er forskjellige. Med andre ord er resultatet av XOR-operasjonen $sant$ hvis nøyaktig én (men ikke begge) av operandene er $sant$. For eksempel vil XOR-operasjonen mellom $1$ og $0$ resultere i $1$. Vi legger merke til dette:

$$
1 \oplus 0 = 1
$$

På samme måte kan XOR-operasjonen utføres på lengre bitsekvenser. For eksempel

$$
10110 \oplus 01110 = 11000
$$

Hver bit i sekvensen sammenlignes med sin motpart, og XOR-operasjonen brukes. Her er sannhetstabellen for XOR-operasjonen:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |

|:---:|:---:|:------------:|

| $0$ | $0$ | $0$ |

| $0$ | $1$ | $1$ |

| $1$ | $0$ | $1$ |

| $1$ | $1$ | $0$ |

</div> </div>

XOR-operasjonen brukes på mange områder innen informatikk, særlig innen kryptografi, på grunn av sine interessante egenskaper, som f.eks:


- Kommutativitet: rekkefølgen på operandene påvirker ikke resultatet. For to gitte variabler $D$ og $E$: $D \oplus E = E \oplus D$;
- Assosiativitet: Grupperingen av operander påvirker ikke resultatet. For tre gitte variabler $A$, $B$ og $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Den har et nøytralt element $0$: en operand xored med $0$ vil alltid være lik operanden. For en gitt variabel $A$: $A \oplus 0 = A$;
- Hvert element er sin egen inverse. For en gitt variabel $A$: $A \oplus A = 0$.

I forbindelse med Bitcoin brukes XOR-operasjonen åpenbart mange steder. XOR er for eksempel mye brukt i SHA256-funksjonen, som er mye brukt i Bitcoin-protokollen. Noen protokoller som Coldcards *SeedXOR* bruker også denne primitive funksjonen til andre applikasjoner. Den finnes også i BIP47 for å kryptere den gjenbrukbare betalingskoden under overføringen.

Innenfor kryptografi kan XOR brukes som en symmetrisk krypteringsalgoritme. Denne algoritmen kalles "One-Time Pad" eller "Vernam Cipher", oppkalt etter oppfinneren. Selv om denne algoritmen er upraktisk på grunn av nøkkellengden, er den en av de eneste krypteringsalgoritmene som er anerkjent som ubetinget sikker.