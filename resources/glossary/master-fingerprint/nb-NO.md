---
term: HOVEDFINGERAVTRYKK

---
Et fingeravtrykk på 4 byte (32 bits) av den private hovednøkkelen i en hierarkisk deterministisk (HD) lommebok. Det oppnås ved å beregne `SHA256`-hash av den private hovednøkkelen, etterfulgt av en `RIPEMD160`-hash, en prosess referert til som `HASH160` på Bitcoin. Masterfingeravtrykket brukes til å identifisere en HD-lommebok, uavhengig av avledningsveiene, men tar hensyn til tilstedeværelsen eller fraværet av en passordfrase. Det er kortfattet informasjon som gjør det mulig å referere til opprinnelsen til et sett med nøkler, uten å avsløre sensitiv informasjon om lommeboken.