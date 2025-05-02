---
term: OTKRIVANJE VRŠNJAKA
---

Proces pomoću kojeg se čvorovi u Bitcoin mreži povezuju sa drugim čvorovima kako bi dobili informacije. Kada se Bitcoin čvor prvi put pokrene, nema informacije o drugim čvorovima u mreži. Ipak, mora uspostaviti veze kako bi se sinhronizovao sa Blockchain koji ima najviše akumuliranog rada. Nekoliko mehanizama se koristi za otkrivanje ovih vršnjaka, po prioritetu:


- Čvor započinje konsultovanjem svoje lokalne datoteke `peers.dat`, koja čuva informacije o čvorovima sa kojima je prethodno komunicirao. Ako je čvor nov, ova datoteka će biti prazna i proces će preći na sledeći korak;
- U nedostatku informacija u datoteci `peers.dat` (što je normalno za novopokrenuti čvor), čvor obavlja DNS upite prema DNS izvorima. Ovi serveri pružaju listu IP adresa verovatno aktivnih čvorova za uspostavljanje veza. Adrese DNS izvora su hardkodirane u Bitcoin Core kodu. Ovaj korak je obično dovoljan za završetak otkrivanja vršnjaka;
- Ako DNS seed-ovi ne odgovore u roku od 60 sekundi, čvor može da se okrene ka seed čvorovima. Ovo su javni Bitcoin čvorovi navedeni u statičkoj listi od skoro hiljadu unosa integrisanih direktno u izvorni kod Bitcoin Core-a. Novi čvor će koristiti ovu listu da uspostavi prvu vezu sa mrežom i dobije IP adrese drugih čvorova;
- U veoma malo verovatnom slučaju da svi prethodni metodi ne uspeju, operater čvora uvek ima opciju da ručno doda IP adrese čvorova kako bi uspostavio prvu vezu.