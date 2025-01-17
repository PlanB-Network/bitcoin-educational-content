---
term: VANSKELIGHET

---
En justerbar parameter som bestemmer kompleksiteten i beviset på arbeidet som kreves for å legge til en ny blokk i blokkjeden og oppnå den tilhørende belønningen. Denne vanskelighetsgraden representeres av vanskelighetsmålet, en 256-biters verdi som angir den øvre grensen som blokkoverskriftens hash må oppfylle for å anses som gyldig. Målet er at hashen, som oppnås gjennom en dobbel kjøring av SHA256 (SHA256d), skal være mindre enn eller lik dette målet. For å oppnå denne hashen manipulerer utvinnerne `nonce` i blokkhodet. Vanskelighetsgraden justeres hver 2016. blokk, eller omtrent annenhver uke, for å holde den gjennomsnittlige tiden det tar å opprette en blokk på rundt 10 minutter.