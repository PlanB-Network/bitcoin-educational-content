---
term: BLOK
---

Struktura podataka u sistemu Bitcoin. Blok sadrži skup validnih transakcija i metapodatke sadržane u njegovom zaglavlju. Svaki blok je povezan sa sledećim putem Hash svog zaglavlja, čime se formira Blockchain. Blockchain deluje kao server za vremensko označavanje koji omogućava svakom korisniku da zna sve prethodne transakcije, kako bi se verifikovalo nepostojanje transakcije i sprečilo dvostruko trošenje. Transakcije su organizovane u Merkle Tree. Ovaj kriptografski akumulator omogućava proizvodnju sažetka svih transakcija u bloku, nazvanog "Merkle Root." Zaglavlje bloka sadrži 6 Elements:


- Verzija bloka;
- Otisak prethodnog bloka;
- Korijen Merkle Tree transakcija;
- Timestamp bloka;
- Ciljna težina;
- Nonce.


Da bi blok bio važeći, mora imati zaglavlje koje, kada se hešira sa `SHA256d`, proizvodi sažetak koji je manji ili jednak cilju težine.