---
term: OVERT ASICBOOST

---
Den åpne og transparente versjonen av AsicBoost. AsicBoost er en algoritmisk optimaliseringsteknikk som brukes i Bitcoin-gruvedrift. Utvinnere som bruker Overt-versjonen, manipulerer `nVersion`-feltet i kandidatblokken og bruker denne modifikasjonen som en ekstra nonce. Denne metoden lar det faktiske `Nonce`-feltet i blokken være uendret under hvert hashing-forsøk, og reduserer dermed beregningene som trengs for hver SHA256, ved å holde noen data de samme mellom forsøkene. Denne versjonen kan oppdages offentlig og skjuler ikke endringene for resten av nettverket, i motsetning til den skjulte versjonen av AsicBoost.