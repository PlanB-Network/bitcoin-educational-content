---
term: Hashfunktion
definition: Matematisk funktion som producerar en utdata med fast storlek från en indata med variabel storlek.
---

En matematisk funktion som tar en variabel storlek på indata (ett meddelande) och producerar en fast storlek på utdata (Hash, hashing, digest eller fingeravtryck). Hash-funktioner är allmänt använda primitiver inom kryptografi. De uppvisar specifika egenskaper som gör dem lämpliga att använda i säkra sammanhang:


- Preimage-resistens: det måste vara mycket svårt att hitta ett meddelande som producerar en specifik Hash, dvs. att hitta en preimage $m$ för en Hash $h$ så att $h = H(m)$, där $H$ är Hash-funktionen;
- Andra preimage-resistens: givet ett meddelande $m_1$ måste det vara mycket svårt att hitta ett annat meddelande $m_2$ (som skiljer sig från $m_1$) så att $H(m_1) = H(m_2)$;
- Kollisionsmotstånd: Det måste vara mycket svårt att hitta två olika meddelanden $m_1$ och $m_2$ så att $H(m_1) = H(m_2)$;
- Sabotageskydd: små förändringar i indata måste orsaka betydande och oförutsägbara förändringar i utdata.


I samband med Bitcoin används Hash-funktioner för flera ändamål, bland annat Proof-of-Work-mekanismen (*Proof-of-Work*), transaktionsidentifierare, Address-generering, kontrollsummeberäkningar och skapande av datastrukturer som Merkle-träd. På protokollsidan använder Bitcoin uteslutande funktionen `SHA256d`, även kallad `HASH256`, som består av en dubbel `SHA256` Hash. `HASH256` används också vid beräkning av vissa kontrollsummor, särskilt för utökade nycklar (`xpub`, `xprv`...). På Wallet-sidan används också följande:


- Enkel `SHA256` för kontrollsummor av Mnemonic-fraser;
- `SHA512` inom algoritmerna `HMAC` och `PBKDF2` som används i processen för att härleda deterministiska och hierarkiska plånböcker;
- `HASH160`, som beskriver en successiv användning av en `SHA256` och en `RIPEMD160`. `HASH160` används vid generering av mottagningsadresser (utom P2PK och P2TR) och vid beräkning av fingeravtryck av huvudnycklar för utökade nycklar.


