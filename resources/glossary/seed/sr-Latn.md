---
term: GRAIN
---

U specifičnom kontekstu hijerarhijski determinističkog portfolija Bitcoin, seed je 512-bitni deo informacija izveden iz slučajnog događaja. Koristi se za determinističko i hijerarhijsko generate skupa privatnih ključeva i njihovih odgovarajućih javnih ključeva za Bitcoin portfolio. seed se često meša sa samom frazom za oporavak. Ali to nije ista stvar. seed se dobija primenom funkcije `PBKDF2` na Mnemonic frazu i bilo koji passphrase.


seed je izumljen sa BIP32, koji je definisao osnove hijerarhijskog determinističkog portfolija. U ovom standardu, seed je merio 128 bita. Ovo omogućava da se svi ključevi u portfoliju izvedu iz jednog komada informacija, za razliku od JBOK (*Just a Bunch Of Keys*) portfolija, koji zahtevaju nove rezervne kopije za svaki generisani ključ. BIP39 je zatim predložio kodiranje ovog seed, kako bi se pojednostavilo njegovo čitanje od strane ljudi. Ovo kodiranje ima oblik fraze, koja se obično naziva Mnemonic fraza ili fraza za oporavak. Ovaj standard izbegava greške prilikom čuvanja seed, zahvaljujući posebno korišćenju kontrolne sume.


Izvan konteksta Bitcoin, u kriptografiji generalno, seed je početna vrednost koja se koristi za generate kriptografskih ključeva, ili šire, bilo koje vrste podataka proizvedenih od strane pseudo-slučajnog generatora brojeva. Ova početna vrednost mora biti nasumična i nepredvidiva kako bi se garantovala sigurnost kriptografskog sistema. Naime, seed unosi entropiju u sistem, ali proces generisanja koji sledi je deterministički.


> ► *U uobičajenom govoru, većina bitkoinera se poziva na Mnemonic frazu kada govore o "seed", a ne na međuprostorno stanje derivacije koje leži između Mnemonic fraze i glavnog ključa.*