---
term: HTLC
---

Znači "*Hashed Timelock Contract*". Ovo je Smart contract mehanizam koji se uglavnom koristi na Lightning-u. Takođe se ponekad nalazi u atomskim zamjenama. U suštini, HTLC čini transfer novca uslovljen otkrivanjem tajne, a takođe uključuje vremenski uslov kako bi zaštitio novac pošiljaoca u slučaju neuspjele transakcije.


Na Lightning-u, HTLC vam omogućava da pošaljete bitkoine čvoru sa kojim nemate direktan kanal, prolazeći kroz nekoliko kanala, bez potrebe za poverenjem na tom putu. Plaćanje između svakog čvora je uslovljeno obezbeđivanjem pre-slike (tajne koja, kada se hešira, odgovara dogovorenoj vrednosti). Ako krajnji primalac obezbedi ovu pre-sliku, može da zahteva sredstva, i nužno omogućava svakom posrednom čvoru da zahteva sredstva u kaskadi.


Na primer, ako Alisa želi da pošalje 1 BTC Dejvidu, ali nema direktan kanal sa njim, mora proći kroz Boba i Karol, koji imaju platne kanale međusobno. Evo kako transakcija funkcioniše:




- David predstavlja Alisi Invoice Lightning. Ovo sadrži Hash $h$ tajne $s$ (pre-image) koju samo David zna. Dakle, imamo: $h = \text{Hash}(s)$ ;
- Alice kreira HTLC sa Bobom, koji nudi da joj pošalje 1 BTC pod uslovom da joj Bob obezbedi tajnu $s$ (pre-image) koja odgovara Hash $h$ ;
- Bob kreira HTLC sa Carol, koja nudi da mu pošalje 1 BTC pod uslovom da ona obezbedi istu tajnu $s$ ;
- Carol kreira HTLC sa Davidom, koji nudi još 1 BTC ako otkrije preimage $s$;
- David otkriva $s$ (koje je samo on znao) Carol kako bi dobio 1 BTC. Carol sada može koristiti $s$ da dobije BTC od Boba. A Bob, koji sada zna $s$, radi isto sa Alice.


Konačno, Alisa je poslala 1 BTC Davidu preko Boba i Karol (neutralna akcija za potonju), bez potrebe da iko ikome veruje, jer je sve osigurano u kaskadi uslovima HTLC-a.


HTLC-ovi na taj način omogućavaju takozvane "atomske" razmene: ili je transfer potpuno uspešan, ili ne uspeva, a sredstva se vraćaju. Ovo garantuje sigurnost transakcija, čak i između više učesnika bez potrebe za poverenjem.