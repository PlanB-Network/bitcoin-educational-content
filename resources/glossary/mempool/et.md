---
term: MEMPOOL
---

Terminite "memory" (mälu) ja "pool" (bassein) kokkutõmbamine. See viitab virtuaalsele ruumile, kus Bitcoin'i tehingud, mis ootavad blokki lisamist, on koondatud. Kui tehing luuakse ja levitatakse Bitcoin'i võrgus, kontrollivad seda esmalt võrgu sõlmed. Kui tehing peetakse kehtivaks, paigutatakse see iga sõlme Mempool'i, kus see püsib, kuni kaevur valib selle blokki lisamiseks.

On oluline märkida, et iga sõlm Bitcoin'i võrgus hoiab oma Mempool'i, ja seetõttu võib Mempool'i sisu erinevates sõlmedes igal ajahetkel erineda. Eriti tähtis on `maxmempool` parameeter iga sõlme `bitcoin.conf` failis, mis võimaldab operaatoritel kontrollida, kui palju RAM'i (juhusliku juurdepääsuga mälu) nende sõlm kasutab ootel olevate tehingute Mempool'is hoidmiseks. Mempool'i suuruse piiramine võimaldab sõlme operaatoritel vältida liigsete ressursside tarbimist nende süsteemis. See parameeter on määratud megabaitides (MB). Bitcoin Core'i vaikimisi väärtus on praeguse seisuga 300 MB.

Mempool'is olevad tehingud on ajutised. Neid ei tohiks pidada muutumatuks enne, kui need on lisatud blokki ja pärast teatud arvu kinnituste saamist. Neid võib sageli asendada või eemaldada.