---
termi: ELTOO
---

Yleinen protokolla Bitcoinin toisen kerroksen ratkaisuille, joka määrittelee, miten UTXO:n omistajuutta hallinnoidaan yhdessä. Eltoo on suunniteltu Christian Deckerin, Rusty Russellin ja Olaoluwa Osuntokunin toimesta erityisesti ratkaisemaan ongelmia, jotka liittyvät Lightning-kanavien tilojen neuvottelumekanismeihin, eli avauksen ja sulkemisen välillä. Eltoo-arkkitehtuuri yksinkertaistaa neuvotteluprosessia esittelemällä lineaarisen tilanhallintajärjestelmän, korvaten vakiintuneen rangaistuspohjaisen lähestymistavan joustavammalla ja vähemmän rankaisevalla päivitysmenetelmällä. Tämä protokolla vaatii uudentyyppisen SigHashin käyttöä, joka sallii kaikkien syötteiden ohittamisen transaktion allekirjoituksessa. Tätä SigHashia kutsuttiin alun perin nimellä `SIGHASH_NOINPUT`, sitten `SIGHASH_ANYPREVOUT` (*Mikä Tahansa Edellinen Lähtö*). Sen toteutus on suunniteltu BIP118:ssa.

> ► *Eltoo viitataan joskus myös nimellä "LN-Symmetry".*