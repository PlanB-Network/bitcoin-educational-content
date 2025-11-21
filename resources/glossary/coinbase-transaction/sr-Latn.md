---
term: COINBASE (TRANSAKCIJA)
---

Coinbase Transaction je posebna i jedinstvena transakcija uključena u svaki blok Bitcoin Blockchain. Predstavlja prvu transakciju bloka i kreira je Miner koji je uspešno pronašao zaglavlje koje validira Proof of Work (*Proof-of-Work*), odnosno, manje ili jednako cilju.


Coinbase Transaction prvenstveno služi dvema svrhama: da dodeli Block reward do Miner i da doda nove jedinice bitkoina u cirkulišući novac Supply. Block reward, koji je ekonomski podsticaj za rudare da se uključe u Proof of Work, uključuje akumulirane naknade za transakcije uključene u blok i određenu količinu novostvorenih bitkoina ex-nihilo (subvencija bloka). Ova količina, koja je prvobitno postavljena na 50 bitkoina po bloku 2009. godine, prepolovljava se svakih 210.000 blokova (približno svake 4 godine) tokom događaja nazvanog "Halving."


Coinbase Transaction se razlikuje od regularnih transakcija na nekoliko načina. Prvo, nema ulaz, što znači da nijedan postojeći izlaz transakcije (UTXO) nije potrošen njime. Zatim, skripta potpisa (`scriptSig`) za Coinbase Transaction obično sadrži proizvoljno polje koje omogućava uključivanje dodatnih podataka, kao što su prilagođene poruke ili informacije o verziji softvera Mining. Na kraju, bitkoini generisani od strane Coinbase Transaction podležu periodu sazrevanja od 100 blokova (101 potvrda) pre nego što mogu biti potrošeni, kako bi se sprečila potencijalna potrošnja nepostojećih bitkoina u slučaju reorganizacije lanca.


> ► *Ne postoji prevod za "Coinbase" na francuski. Stoga je prihvaćeno koristiti ovaj termin direktno.*