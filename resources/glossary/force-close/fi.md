---
term: PAKOTTAMINEN SULJETTU
---

Ei-yhteistyöhön perustuva salamakanavan sulkemismekanismi. Kun kaksi käyttäjää avaa kanavan Multisig 2/2:lla, kumpikin voi yksipuolisesti sulkea kanavan lähettämällä viimeisen jo allekirjoitetun Commitment Transaction:n ja saada takaisin ketjussa olevat bitcoininsa. Tämä tunnetaan nimellä "force close".


Tätä menetelmää käytetään yleensä silloin, kun toinen osallistujista ei enää vastaa tai kun kanavan sulkeminen yhteistyössä on mahdotonta. Jos pakkosulkemista voidaan välttää, se on paras vaihtoehto, sillä ketjussa olevien varojen takaisin saaminen kestää kauemmin ja voi olla paljon kalliimpaa maksujen osalta.


Voimakkaassa sulkeutumisessa toinen käyttäjistä lähettää Commitment Transaction:n, joka kuvastaa salamakanavan viimeisintä tunnettua tilaa. Tämän jälkeen bitcoinit voidaan hakea ketjussa aikalukon jälkeen, jolloin toinen osapuoli voi tarkistaa, että transaktio vastaa kanavan viimeisintä tilaa. Jos käyttäjä yrittää huijata julkaisemalla vanhentuneen Commitment Transaction:n, toinen osapuoli voi käyttää peruutussalaisuutta rangaistakseen huijaria ja saadakseen takaisin kaikki kanavassa olevat varat.