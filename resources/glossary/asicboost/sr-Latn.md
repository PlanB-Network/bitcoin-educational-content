---
term: ASICBOOST
---

ASICBOOST je algoritamska metoda optimizacije izumljena 2016. godine, dizajnirana da poveća efikasnost Bitcoin Mining za oko 20% smanjenjem broja potrebnih proračuna za svaki Hash pokušaj zaglavlja. Ova tehnika koristi karakteristiku SHA256 Hash funkcije, koja se koristi za Mining, a koja deli podatke na blokove pre nego što ih obradi. ASICBOOST zadržava jedan od ovih blokova nepromenjenim kroz više pokušaja heširanja, omogućavajući Miner da uradi samo deo posla za ovaj blok tokom nekoliko pokušaja. Ovo deljenje podataka omogućava ponovno korišćenje rezultata iz prethodnih proračuna, čime se smanjuje ukupan broj proračuna potrebnih za pronalaženje validnog Hash.


ASICBOOST se može koristiti u dva oblika: Overt ASICBOOST i Covert ASICBOOST. Overt ASICBOOST oblik je vidljiv svima, jer uključuje korišćenje polja `nVersion` bloka kao Nonce, i ne menja pravi `Nonce`. Covert oblik nastoji da sakrije ove modifikacije korišćenjem Merkle stabala. Međutim, ova druga metoda je postala manje efikasna od uvođenja SegWit zbog drugog Merkle Tree, koji povećava broj potrebnih proračuna za njegovo korišćenje.


Ukratko, ASICBOOST omogućava rudarima da ne moraju da izvrše potpuno SHA256 heširanje za sve pokušaje, jer deo rezultata ostaje nepromenjen, što ubrzava rad rudara.