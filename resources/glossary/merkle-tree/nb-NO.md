---
term: MERKLE TREE

---
Et Merkle-tre er en kryptografisk akkumulator. Det er en metode for å bevise at et gitt stykke informasjon tilhører et større sett. Det er en datastruktur som gjør det enklere å verifisere informasjon i et kompakt format. I Bitcoin-systemet brukes Merkle Trees til å gruppere og kondensere transaksjonene i en blokk til en enkelt hash, kalt Merkle Root (eller "*Root Hash*"). Hver transaksjon hashes, og deretter hashes de tilstøtende hashene hierarkisk sammen til Merkle-roten er oppnådd.

![](../../dictionnaire/assets/1.webp)

Denne strukturen gjør det mulig å raskt verifisere om en bestemt transaksjon er inkludert i en gitt blokk uten å måtte analysere alle transaksjonene. Hvis jeg for eksempel bare har Merkle Root og ønsker å verifisere at `TX 7` faktisk er en del av treet, trenger jeg bare følgende bevis:


- "TX 7";
- `HASH 8`;
- `HASH 5-6`;
- `HASH 1-2-3-4`.

Med disse opplysningene kan jeg beregne de mellomliggende nodene opp til Merkle-roten.

![](../../dictionnaire/assets/2.webp)

Merkle Trees brukes særlig for lette noder (kjent som "SPV") som bare beholder blokkhodene, men ikke transaksjonene. Denne strukturen finnes også i UTREEXO-protokollen, en protokoll som gjør det mulig å kondensere UTXO-settet av noder, og i MAST Taproot.

> merkle-treet er oppkalt etter Ralph Merkle, en kryptograf som designet denne strukturen i 1979. Et Merkle-tre kan også kalles et "hash-tre". På fransk kalles det "Arbre de Merkle" eller "arbre de hachage"