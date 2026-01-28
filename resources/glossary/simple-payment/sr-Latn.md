---
term: Jednostavno plaćanje
definition: Model transakcije sa 2 izlaza, obično plaćanje i kusur.
---

Obrazac transakcije (ili model) korišćen u analizi lanca karakteriše se potrošnjom jednog ili više UTXO-a u ulazima i proizvodnjom 2 UTXO-a u izlazima. Ovaj model će stoga izgledati ovako:





Ovaj jednostavan model plaćanja ukazuje na to da smo verovatno u prisustvu transakcije slanja ili plaćanja. Korisnik je potrošio svoj sopstveni UTXO u ulazima kako bi zadovoljio u izlazima plaćanje UTXO i kusur UTXO (kusur vraćen istom korisniku). Stoga znamo da posmatrani korisnik verovatno više nije u posedu jednog od dva UTXO-a u izlazima (onog za plaćanje), ali je i dalje u posedu drugog UTXO (onog za kusur).