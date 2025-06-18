---
term: EKSTRA-Nonce
---

Polje korišćeno u `scriptSig` bloka Coinbase Transaction, koje omogućava testiranje većeg broja mogućnosti kako bi se dobio Hash manji od ciljne težine, pored klasičnog Nonce, koji se nalazi direktno u zaglavlju svakog bloka.


Modifikovanje extra-Nonce u Coinbase Transaction menja identifikator ove transakcije, i stoga Merkle Root svih transakcija u bloku, što takođe menja zaglavlje bloka. Ovo omogućava Miner da nastavi sa pretragom heševa kada je opseg klasičnog Nonce već iscrpljen, bez promene strukture svog kandidata bloka.


U Mining bazenima, extra-Nonce je često podeljen na dva dela: jedan generisan od strane bazena za identifikaciju svakog helikoptera, i drugi modifikovan od strane helikoptera u potrazi za validnim delom. Ovo omogućava različitim helikopterima u bazenu da rade istovremeno na istom kandidatu bloka sa celim opsegom nonces, bez dupliranja istog posla na nivou bazena.