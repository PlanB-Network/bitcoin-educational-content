---
term: CHAIN CODE
---

U kontekstu hijerarhijske determinističke (HD) derivacije Bitcoin novčanika, lančani kod je 256-bitna kriptografska vrednost soli koja se koristi za generate ključeve deteta iz roditeljskog ključa, prema BIP32 standardu. Lančani kod se koristi u kombinaciji sa roditeljskim ključem i indeksom deteta da bi se deterministički generate novi par ključeva (privatni ključ i javni ključ) bez otkrivanja roditeljskog ključa ili drugih izvedenih ključeva deteta.


Stoga, postoji jedinstveni lančani kod za svaki par ključeva. Lančani kod se dobija ili heširanjem Wallet-ovog seed i uzimanjem desne polovine bitova. U ovom slučaju, naziva se glavnim lančanim kodom, povezanim sa glavnim privatnim ključem. Alternativno, može se dobiti heširanjem roditeljskog ključa sa njegovim roditeljskim lančanim kodom i indeksom, zatim zadržavanjem desnih bitova. Ovo se tada naziva dečijim lančanim kodom.


Nemoguće je izvesti ključeve bez poznavanja lanca koda povezanog sa svakim roditeljskim parom. On uvodi pseudo-slučajne podatke u proces izvođenja kako bi osigurao da generisanje kriptografskih ključeva ostane nepredvidivo za napadače, dok je deterministično za vlasnika Wallet.


> ► *Na engleskom, "code de chaîne" se zove "chain code", a "code de chaîne maître" se zove "master chain code".*