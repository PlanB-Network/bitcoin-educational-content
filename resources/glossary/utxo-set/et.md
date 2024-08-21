---
term: UTXO KOMPLEKT
---

Viitab kõikide olemasolevate UTXO-de kogumile igal antud hetkel. Teisisõnu, see on suur nimekiri kõikidest erinevatest bitcoinide tükkidest, mis ootavad kulutamist. Kui liidate kõikide UTXO-de summad UTXO komplektis, annab see meile ringluses olevate bitcoinide kogumonetaarse massi. Iga sõlm Bitcoin'i võrgus hoiab oma UTXO komplekti reaalajas. See uuendab seda, kui uued kehtivad plokid kinnitatakse, koos nende sisaldavate tehingutega, mis tarbivad mõningaid UTXO-sid UTXO komplektist ja loovad vastutasuks uusi.

Iga sõlm hoiab seda UTXO komplekti, et kiiresti kontrollida, kas tehingutes kulutatud UTXO-d on tõepoolest legitiimsed. See võimaldab neil tuvastada ja tagasi lükata topeltkulutamise katseid. UTXO komplekt on sageli Bitcoin'i detsentraliseerituse murede keskmes, kuna selle suurus loomulikult suureneb väga kiiresti. Kuna osa sellest tuleb hoida RAM-is, et tehinguid mõistliku aja jooksul kontrollida, võib UTXO komplekt järk-järgult muuta täissõlme käitamise liiga kulukaks. UTXO komplektil on oluline mõju ka IBD-le (*Initial Block Download*). Mida rohkem UTXO komplektist saab paigutada RAM-i, seda kiirem on IBD. Bitcoin Core'is hoitakse UTXO komplekti kaustas nimega `/chainstate`.

> ► *Inglise keeles "UTXO set" võiks tõlkida kui "UTXO komplekt".*