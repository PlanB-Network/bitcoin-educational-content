---
term: ASICBOOST

---
ASICBOOST er en algoritmisk optimaliseringsmetode som ble oppfunnet i 2016, og som er utviklet for å øke effektiviteten i Bitcoin-gruvedrift med ca. 20 % ved å redusere mengden beregninger som trengs for hvert hash-forsøk av headeren. Denne teknikken utnytter en funksjon i SHA256-hashfunksjonen, som brukes til utvinning, og som deler dataene inn i blokker før de behandles. ASICBOOST beholder en av disse blokkene uendret over flere hashforsøk, slik at utvinneren bare trenger å gjøre en del av arbeidet for denne blokken over flere forsøk. Denne datadelingen gjør det mulig å gjenbruke resultater fra tidligere beregninger, noe som reduserer det totale antallet beregninger som trengs for å finne en gyldig hash.

ASICBOOST kan brukes i to former: Overt ASICBOOST og Covert ASICBOOST. Overt ASICBOOST-formen er synlig for alle, ettersom den innebærer å bruke `nVersion`-feltet i blokken som en nonce, og ikke endre den virkelige `Nonce`. Covert-formen forsøker å skjule disse endringene ved å bruke Merkle-trær. Denne andre metoden har imidlertid blitt mindre effektiv etter innføringen av SegWit på grunn av det andre Merkle-treet, som øker antallet beregninger som trengs for å bruke det.

ASICBOOST gjør at utvinnere ikke trenger å utføre en fullstendig SHA256 for alle hashingsforsøk, ettersom en del av resultatet forblir uendret, noe som gjør arbeidet til utvinnerne raskere.