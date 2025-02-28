---
term: BIP8

---
BIP8 ble utviklet etter debattene om SegWit, som brukte BIP9 til aktivering, og er en aktiveringsmetode for myk gaffel som inkluderer en automatisk UASF-mekanisme (*User-Activated Soft Fork*). I likhet med BIP9 bruker BIP8 miner-signalering, men legger til parameteren `LOT` (*Lock-in On Time out*). Hvis `LOT` er satt til `true`, utløses automatisk en UASF ved utløpet av signaleringsperioden uten å nå den nødvendige terskelen, noe som tvinger aktiveringen av soft fork. Denne tilnærmingen tvinger utvinnere til å samarbeide, ellers risikerer de en UASF pålagt av brukerne. I motsetning til BIP9 definerer BIP8 dessuten signaleringsperioden basert på blokkhøyde, noe som eliminerer potensiell manipulering gjennom hashraten fra utvinnernes side. BIP8 gjør det også mulig å sette en variabel terskel for stemmegivning og introduserer en parameter for minimum blokkhøyde for aktivering, noe som gir utvinnere tid til å forberede seg og signalisere sin enighet på forhånd uten nødvendigvis å være klare. Når en soft fork aktiveres via BIP8 med parameteren `LOT=true`, brukes en svært aggressiv metode mot utvinnere som umiddelbart blir satt under press av en potensiell UASF. Faktisk gir det dem bare to valg:


- Vær samarbeidsvillig, og legg dermed til rette for aktiveringsprosessen;
- Ikke være samarbeidsvillig, i så fall utfører brukerne automatisk en UASF for å innføre den myke gaffelen.