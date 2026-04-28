---
term: UTXO kogum

definition: Kõigi antud ajahetkel olemasolevate UTXO-de kogum, mida iga sõlm peab tehingute kontrollimiseks.
---
Viitab kõigi olemasolevate UTXOde kogumile igal ajahetkel. Teisisõnu, see on suur nimekiri kõigist erinevatest bitcoinidest, mis ootavad kulutamist. Kui liita kokku kõigi UTXOde kogumis olevate UTXOde summad, saame sellest ringluses olevate bitcoinide rahalise kogumassi. Iga sõlme Bitcoini võrgus hoiab oma UTXO-kogumit reaalajas. Ta ajakohastab seda uute kehtivate plokkide kinnitamisel koos neis sisalduvate tehingutega, mis tarbivad mõned UTXO-d UTXO-de kogumist ja loovad vastutasuks uusi.

Seda UTXO-komplekti säilitab iga sõlmpunkt, et kiiresti kontrollida, kas tehingutes kasutatud UTXO-d on tõepoolest õiguspärased. See võimaldab neil tuvastada ja tagasi lükata topeltkulutuskatsed. UTXO-komplekt on sageli Bitcoini detsentraliseerimise murede keskmes, kuna selle suurus kasvab loomulikult väga kiiresti. Kuna osa sellest tuleb hoida RAM-is, et tehinguid mõistliku aja jooksul kontrollida, võib UTXO-kogum järk-järgult muuta täieliku sõlme käitamise liiga kulukaks. UTXO komplekt mõjutab oluliselt ka IBD-d (*Initial Block Download*). Mida rohkem UTXO-komplekti saab RAM-i paigutada, seda kiirem on IBD. Bitcoin Core'is salvestatakse UTXO-komplekt kausta nimega `/chainstate`.

