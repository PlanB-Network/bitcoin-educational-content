---
term: REKURSIV (PAKT)

---
En rekursiv pakt på Bitcoin er en type smartkontrakt som ikke bare stiller betingelser for den aktuelle transaksjonen, men også for fremtidige transaksjoner som bruker utdataene fra denne transaksjonen. Dette gjør det mulig å opprette transaksjonskjeder der hver transaksjon må følge visse regler som er definert av den første i kjeden. Rekursivitet skaper en sekvens av transaksjoner der hver transaksjon arver restriksjonene fra sin overordnede transaksjon. Dette muliggjør kompleks og langsiktig kontroll over hvordan bitcoins kan brukes, men det vil også medføre risiko med hensyn til bruksfrihet og fungibilitet.

For å oppsummere: En ikke-rekursiv pakt vil kun begrense seg til transaksjonen som følger umiddelbart etter den som etablerte reglene. En rekursiv pakt har derimot muligheten til å pålegge en bitcoin spesifikke betingelser på ubestemt tid. Transaksjoner kan følge etter hverandre, men den aktuelle bitcoinen vil alltid beholde de opprinnelige betingelsene som er knyttet til den. Teknisk sett oppstår etableringen av en ikke-rekursiv pakt når `scriptPubKey` av en UTXO definerer restriksjoner på `scriptPubKey` av utdataene til en transaksjon som bruker nevnte UTXO. En rekursiv pakt oppstår derimot når `scriptPubKey` til en UTXO definerer restriksjoner på `scriptPubKey` til utdataene til en transaksjon som bruker UTXO-en, og på alle `scriptPubKey`er som følger etter bruken av denne UTXO-en.

Mer generelt, innen databehandling, er det som kalles "rekursivitet" en funksjons evne til å kalle seg selv, noe som skaper en slags løkke.