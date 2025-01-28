---
term: FORENKLET BETALINGSBEKREFTELSE

---
Metode som gjør det mulig for lette klienter å verifisere Bitcoin-transaksjoner uten å laste ned hele blokkjeden. En node som bruker SPV, laster bare ned blokkoverskriftene, som er mye lettere enn de komplette blokkene. Når den trenger å verifisere en transaksjon, ber SPV-noden om et Merkle-bevis fra fullstendige noder for å bekrefte at transaksjonen er inkludert i en bestemt blokk. Denne tilnærmingen er effektiv for enheter med begrensede ressurser, for eksempel smarttelefoner, men den innebærer en avhengighet av fullstendige noder, noe som kan redusere sikkerheten og øke den nødvendige tilliten.

> forkortelsen "SPV" brukes ofte om denne metoden