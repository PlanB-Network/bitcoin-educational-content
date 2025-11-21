---
term: SIGHASH_ALL (0X01)
---

Tip SigHash zastavice korišćen u Bitcoin potpisima transakcija da označi da se potpis odnosi na sve komponente transakcije. Korišćenjem `SIGHASH_ALL`, potpisnik pokriva sve ulaze i sve izlaze. To znači da ni ulazi ni izlazi ne mogu biti izmenjeni nakon potpisa bez njegovog poništavanja. Ovaj tip SigHash zastavice je najčešći u Bitcoin transakcijama, jer obezbeđuje potpunu konačnost i integritet transakcije.