---
term: Anonsets (anonymity sets)

definition: Indikaattorit, jotka mittaavat UTXOn yksityisyyden astetta laskemalla erottumattomien UTXOiden lukumäärää joukossa, tyypillisesti coinjoin-jälkeen.
---
Anonsetit toimivat indikaattoreina arvioitaessa tietyn UTXO:n yksityisyyden tasoa. Tarkemmin sanottuna ne mittaavat erottamattomien UTXO:iden määrää joukossa, joka sisältää tarkasteltavan kolikon. Koska tarvitaan ryhmä identtisiä UTXO:ita, anonsetit lasketaan yleensä coinjoin-kierroksen yhteydessä. Ne mahdollistavat tarvittaessa coinjoinien laadun arvioinnin. Suuri anonset tarkoittaa korkeampaa anonymiteetin tasoa, sillä yksittäisen UTXO:n erottaminen joukosta käy vaikeaksi.

Anonsetteja on kahta tyyppiä: forward anonset (forward-looking metrics); ja backward anonset (backward-looking metrics). Termiä "*score*" käytetään toisinaan myös anonsettien nimityksenä.

Ensimmäinen ilmaisee sen ryhmän koon, jonka sisällä tarkasteltu lähtö-UTXO piiloutuu, kun lähtö-UTXO tunnetaan. Tämä indikaattori mahdollistaa kolikon yksityisyyden kestävyyden mittaamisen menneisyydestä nykyhetkeen suuntautuvaa analyysiä vastaan (sisääntulosta ulostuloon). Toinen ilmaisee mahdollisten lähteiden määrän tietylle kolikolle, kun ulostulo-UTXO tunnetaan. Tämä indikaattori mahdollistaa kolikon yksityisyyden kestävyyden mittaamisen nykyhetkestä menneisyyteen suuntautuvaa analyysiä vastaan (ulostulosta sisääntuloon).










