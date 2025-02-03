---
term: BIP43

---
Forslag til forbedring som introduserer bruk av et avledningsstienivå for å beskrive formålsfeltet i strukturen til HD-lommebøker, tidligere introdusert i BIP32. I henhold til BIP43 er det første avledningsnivået i en HD-lommebok, rett etter hovednøkkelen betegnet som `m/`, reservert for formålsnummeret som angir avledningsstandarden som brukes for resten av stien. Dette nummeret registreres som en herdet indeks. Hvis lommeboken for eksempel følger SegWit-standarden (BIP84), vil begynnelsen på avledningsstien være: `m/84'/`. BIP43 gjør det dermed mulig å avklare standardene som følges av hver lommebokprogramvare for å få bedre interoperabilitet mellom dem. Standardiseringen av resten av avledningsstien er beskrevet i BIP44.