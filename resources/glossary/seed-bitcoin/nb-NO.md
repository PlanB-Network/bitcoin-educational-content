---
term: SEED (BITCOIN)

---
I forbindelse med Bitcoin er et seed en 512-biters verdi som brukes til å utlede alle de private og offentlige nøklene som er knyttet til en HD-lommebok (Hierarchical Deterministic). Teknisk sett er seed en annen verdi enn gjenopprettingsfrasen (eller mnemonikken). Frasen, som vanligvis består av 12 eller 24 ord, genereres på en pseudotilfeldig måte fra en entropikilde og kompletteres med en kontrollsum. Denne frasen gjør det enklere for mennesker å ta sikkerhetskopi ved å gi en tekstlig representasjon av verdien i bunnen av lommeboken.

For å finne det faktiske frøet behandles gjenopprettingsfrasen, eventuelt sammen med en valgfri passordfrase, gjennom PBKDF2-algoritmen (*Password-Based Key Derivation Function 2*). Resultatet av denne beregningen er et 512-biters seed. Det er dette frøet som brukes til å generere hovednøkkelen på en deterministisk måte, og deretter hele settet med nøkler for HD-lommeboken, i samsvar med BIP32.

![](../../dictionnaire/assets/31.webp)

> i vanlig språkbruk refererer imidlertid de fleste bitcoinere til den mnemoniske frasen når de snakker om "frøet", og ikke til den mellomliggende avledningstilstanden som ligger mellom den mnemoniske frasen og hovednøkkelen