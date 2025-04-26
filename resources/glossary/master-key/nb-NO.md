---
term: MASTERNØKKEL

---
I forbindelse med HD-lommebøker (Hierarchical Deterministic) er den private hovednøkkelen en unik privat nøkkel som er avledet fra lommebokens seed. For å få tak i hovednøkkelen brukes `HMAC-SHA512`-funksjonen på seed, med ordene "*Bitcoin seed*" bokstavelig talt som nøkkel. Resultatet av denne operasjonen gir en 512-biters utgang, der de første 256 bitene utgjør hovednøkkelen, og de resterende 256 bitene danner hovedkjedekoden. Hovednøkkelen og hovedkjedekoden fungerer som utgangspunkt for å utlede alle underordnede private og offentlige nøkler i HD-lommebokens trestruktur. Derfor er den private hovednøkkelen på avledningsdybde 0.

![](../../dictionnaire/assets/19.webp)