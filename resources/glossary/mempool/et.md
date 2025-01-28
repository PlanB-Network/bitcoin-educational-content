---
term: MEMPOOL

---
Mõistete "mälu" ja "bassein" lühend. See viitab virtuaalsele ruumile, kuhu on koondatud blokki lisamist ootavad Bitcoini tehingud. Kui tehing luuakse ja edastatakse Bitcoini võrgus, kontrollivad võrgu sõlmed seda kõigepealt. Kui seda peetakse kehtivaks, paigutatakse see seejärel iga sõlme Mempool'i, kus see jääb sinna, kuni kaevandaja valib selle plokki lisamiseks välja.

Oluline on märkida, et iga Bitcoini võrgu sõlme säilitab oma Mempool, mistõttu võib Mempooli sisu eri sõlmede vahel igal ajahetkel erineda. Nimelt võimaldab iga sõlme failis "bitcoin.conf" olev parameeter "maxmempool" operaatoritel kontrollida RAM-i (suvalise juurdepääsu mälu) hulka, mida nende sõlme kasutab Mempoolis olevate tehingute salvestamiseks. Mempool'i suuruse piiramisega saavad sõlme operaatorid vältida, et see tarbiks nende süsteemi liiga palju ressursse. See parameeter määratakse megabaitides (MB). Bitcoin Core'i vaikeväärtus on siiani 300 MB.

Mempoolis olevad tehingud on ajutised. Neid ei tohiks pidada muutumatuteks enne, kui need on lisatud plokki ja pärast teatud arvu kinnitusi. Neid saab sageli asendada või kustutada.