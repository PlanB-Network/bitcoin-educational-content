---
term: BIP113

---
Innført en endring i beregningen av alle tidslåsoperasjoner (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` og `OP_CHECKSEQUENCEVERIFY`). Den spesifiserer at for å evaluere gyldigheten av tidslåser må de nå sammenlignes med MTP (*Median Time Past*), som er medianen av tidsstemplene for de siste 11 blokkene. Tidligere ble bare tidsstempelet for den forrige blokken brukt. Denne metoden gjør systemet mer forutsigbart og forhindrer at utvinnere manipulerer tidsreferansen. BIP113 ble introdusert via en soft fork 4. juli 2016, sammen med BIP68 og BIP112, som for første gang ble aktivert ved hjelp av BIP9-metoden.