---
term: SPV NODE (LYS NODE)

---
En SPV-node (*Simple Payment Verification*), også kalt en "light-node", er en lettvektsklient for en Bitcoin-node som lar brukerne validere transaksjoner uten å måtte lagre hele blokkjeden. I stedet lagrer en SPV-node bare blokkoverskriftene og innhenter informasjon om spesifikke transaksjoner ved å spørre fullstendige noder når det er nødvendig. Dette verifiseringsprinsippet muliggjøres av strukturen til transaksjonene i Bitcoin-blokker, som er organisert i en kryptografisk akkumulator (Merkle Tree).

Denne tilnærmingen er fordelaktig for enheter med begrensede ressurser, for eksempel mobiltelefoner. SPV-noder er imidlertid avhengige av fullstendige noder for å få tilgang til informasjon, noe som innebærer et ekstra tillitsnivå og følgelig mindre sikkerhet sammenlignet med fullstendige noder. SPV-noder kan ikke validere transaksjoner på egen hånd, men de kan verifisere om en transaksjon er inkludert i en blokk ved å konsultere Merkle-bevis.