---
term: DIFFIE-HELLMAN

---
Kryptografisk metode som gjør det mulig for to parter å generere en delt hemmelighet over en usikret kommunikasjonskanal. Denne hemmeligheten kan deretter brukes til å kryptere kommunikasjonen mellom de to partene. Diffie-Hellman bruker modulær aritmetikk, slik at selv om en angriper kan observere utvekslingene, kan de ikke utlede den delte hemmeligheten uten å løse et vanskelig matematisk problem: den diskrete logaritmen. I Bitcoin brukes noen ganger en variant av DH kalt ECDH som bruker en elliptisk kurve, spesielt for statiske adresseprotokoller som Silent Payments eller BIP47.