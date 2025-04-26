---
term: ELTOO

---
Yleinen protokolla Bitcoinin toisille kerroksille, jossa määritellään, miten UTXO:n omistusta hallitaan yhdessä. Eltoon suunnittelivat Christian Decker, Rusty Russell ja Olaoluwa Osuntokun erityisesti ratkaisemaan Lightning-kanavien tilojen neuvottelumekanismeihin eli avaamisen ja sulkemisen välisiin neuvotteluihin liittyviä ongelmia. Eltoo-arkkitehtuuri yksinkertaistaa neuvotteluprosessia ottamalla käyttöön lineaarisen tilanhallintajärjestelmän, joka korvaa vakiintuneen rangaistuksiin perustuvan lähestymistavan joustavammalla ja vähemmän rankaisevalla päivitysmenetelmällä. Tämä protokolla edellyttää uudenlaisen SigHash-tyypin käyttöä, joka mahdollistaa kaikkien syötteiden huomiotta jättämisen tapahtuman allekirjoituksessa. Tämän SigHashin nimi oli aluksi `SIGHASH_NOINPUT`, sitten `SIGHASH_ANYPREVOUT` (*Any Previous Output*). Sen toteutus on suunniteltu BIP118:ssa.

> ► *Eltoon viitataan joskus myös nimellä "LN-symmetria".*