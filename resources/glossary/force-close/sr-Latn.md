---
term: PRISILNO ZATVARANJE
---

Nekooperativni mehanizam zatvaranja Lightning kanala. Kada dva korisnika otvore kanal sa Multisig 2/2, svaki može jednostrano zatvoriti kanal emitovanjem poslednjeg Commitment Transaction koji je već potpisan, kako bi povratili svoje bitkoine na lancu. Ovo je poznato kao "prisilno zatvaranje".


Ova metoda se obično koristi ako jedan od učesnika više ne odgovara, ili ako je kooperativno zatvaranje kanala nemoguće. Ako se može izbeći prisilno zatvaranje, to je najbolje, jer je potrebno više vremena za povratak sredstava na lancu i može biti mnogo skuplje u smislu naknada.


U slučaju prisilnog zatvaranja, jedan od dva korisnika emituje Commitment Transaction, koji odražava poslednje poznato stanje Lightning kanala. Zatim postoji vremenska blokada pre nego što se bitkoini mogu povući na lancu, što daje drugoj strani vreme da proveri da li transakcija odgovara najnovijem stanju kanala. Ako korisnik pokuša da prevari objavljivanjem zastarelog Commitment Transaction, druga strana može koristiti tajnu opoziva da kazni prevaranta i povrati sva sredstva u kanalu.