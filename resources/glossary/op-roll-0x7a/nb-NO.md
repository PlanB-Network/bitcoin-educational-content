---
term: OP_ROLL (0X7A)

---
Flytter et element fra stakken til toppen av stakken, basert på dybden som er spesifisert av verdien på toppen av stakken før operasjonen. Hvis for eksempel verdien øverst i bunken er `4`, vil `OP_ROLL` velge det fjerde elementet fra toppen av bunken, og flytte denne verdien til toppen. `OP_ROLL` har samme funksjon som `OP_PICK`, bortsett fra at den fjerner elementet fra sin opprinnelige posisjon.