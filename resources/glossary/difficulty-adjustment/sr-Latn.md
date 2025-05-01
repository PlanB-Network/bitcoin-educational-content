---
term: PRILAGOĐAVANJE TEŽINE
---

Podešavanje težine je periodični proces koji redefiniše cilj težine za mehanizam Proof of Work (Mining) na Bitcoin. Ovaj događaj se dešava svakih 2016 blokova (otprilike svake dve nedelje). Služi za povećanje ili smanjenje faktora težine (takođe nazvanog ciljem težine), u zavisnosti od toga koliko brzo su pronađena poslednja 2016 bloka. Podešavanje ima za cilj održavanje stabilne i predvidljive stope proizvodnje blokova, sa frekvencijom od jednog bloka svakih 10 minuta, uprkos varijacijama u računarskoj snazi koju koriste rudari. Promena težine tokom podešavanja je ograničena na faktor 4. Formula koju izvršavaju čvorovi za izračunavanje novog cilja je sledeća:

$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$


Gde:


- $N$: Nova meta;
- $A$: Stara meta poslednjih 2016 blokova;
- $T$: Ukupno stvarno vreme poslednjih 2016 blokova u sekundama;
- $1,209,600$: Ciljano vreme u sekundama za proizvodnju 2016 blokova sa intervalom od 10 minuta između svakog.


> ► *U francuskom, termin "reciblage" se ponekad koristi i za označavanje prilagođavanja. Na engleskom, to se naziva "Difficulty Adjustment".*