---
name: BLOCKSTREAM Explorer
description: Tutustu Bitcoin:n ja Liquid Network:n tärkeimpään Layer:een
---

![cover](assets/cover.webp)



BLOCKSTREAM Explorer on projekti, joka helpottaa Bitcoin-protokollan transaktioiden ja Global State:n sekä BLOCKSTREAM-yhtiön kehittämän [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid:n tutkimista.



Adam Backin perustaman BLOCKSTREAM-yrityksen vuonna 2014 käynnistämä [BLOCKSTREAM.info](https://BLOCKSTREAM.info) explorer pyrkii tarjoamaan Bitcoin:lle vankan infrastruktuurin, joka takaa yhteentoimivuuden ja transaktioiden seurannan kerrosten (On-Chain ja Liquid) välillä ja parantaa samalla käyttäjien turvallisuutta ja yksityisyyttä.



Tässä oppaassa esitellään, mikä tekee siitä erilaisen, sen palvelut ja se, miten se tarjoaa saumatonta Bitcoin:n On-Chain- ja Liquid-kerrosten toiminnan ja tilan seurantaa.



## BLOCKSTREAM:n käytön aloittaminen



### Navigoi pääkanavalla



Kun siirryt BLOCKSTREAM.info-selaimeen, "**Dashboard**"-osassa on oletuksena valittu Bitcoin-protokollan pääkanava. Tästä Interface:sta sinulla on yleiskatsaus :





- Pääketjun koko: Äskettäin louhitut lohkot.



![blocks](assets/fr/01.webp)



Tässä osiossa on tietoja viime aikoina louhituista lohkoista, Timestamp:stä, kuhunkin BLOCK:een sisältyvien transaktioiden määrästä, koosta kilotavuina (kB) ja kunkin BLOCK:n mittauksesta painoyksikköinä (**WU** = *Weight Units*). Viimeksi mainittu mittaustapa on kiinnostava, koska sen avulla voidaan arvioida BLOCK:n optimointia, kun otetaan huomioon, että pääketjun kukin BLOCK on rajoitettu 4 000 000 WU:n eli 4 000 kWU:n suuruiseksi.





- Viimeaikaiset liiketoimet.



![transactions](assets/fr/02.webp)



Tapahtumaosio sisältää tiedot tapahtuman yksilöllisestä tunnisteesta, kyseessä olevasta Bitcoin-arvosta, koosta virtuaalitavuina (vB) - joka edustaa kaiken datan (tulo ja lähtö) summaa - ja siihen liittyvästä veloituksesta. Esimerkiksi transaktio, jonka koko on "153 vB" ja jonka hinta on "2 sat/vB", maksaa "306 satoshia".



### Nesteen etsintä



"**Blocks**"-valikosta voit jäljittää koko pääketjun historian viimeiseen louhittuun BLOCK:een asti.



![blocs](assets/fr/03.webp)



Klikkaamalla tiettyä BLOCK:tä saat lisätietoja siihen sisältyvistä tiedoista ja tapahtumista. Esimerkiksi BLOCK 919330: sinulla on BLOCK:n Hash. Voit myös siirtyä edelliseen BLOCK:een, sillä jokainen louhittu BLOCK (lukuun ottamatta Genesis:tä) on linkitetty edelliseen ja säilyttää edeltäjänsä Hash:n.



![metadata](assets/fr/04.webp)



Napsauttamalla **"Tiedot "** -painiketta saat lisätietoja tästä BLOCK:sta, kuten sen tilan, joka vahvistaa, että se on lisätty säilytettyyn ja levitettyyn pääketjuun. Sinulla on myös vaikeusaste, jolla tätä BLOCK:a louhitaan: tämä vaikeusaste edustaa laskentatehoa, joka tarvitaan Mining:n kryptografisen ongelman ratkaisemiseen, ja sitä mukautetaan joka 2016 lohko (noin 2 viikkoa).



![details](assets/fr/05.webp)



Tämän tiedot-osion alapuolella on kaikki tähän BLOCK:ään sisältyvät tapahtumat.



BLOCK:n ensimmäistä transaktiota kutsutaan **transaktioksi coinbase**. Sitä käytetään Miner:n Mining-palkkion jakamiseen (kaikki BLOCK:een sisältyviin transaktioihin liittyvät maksut ja BLOCK-avustus). Tällä transaktiolla luodut bitcoinit voidaan käyttää vasta, kun toiset 100 peräkkäistä lohkoa on louhittu. Toisin sanoen Miner:n on odotettava BLOCK:n **919430** tuottamista, jotta se voi käyttää niitä. Tämä tunnetaan nimellä [*"maturity period "*](https://planb.network/fr/resources/glossary/maturity-period).



Coinbase on erityinen tapahtuma: se on ainoa, jossa ei ole todellista panosta, sillä siinä ei käytetä yhtään bitcoinia edellisestä tapahtumasta.




![coinbase](assets/fr/06.webp)



Kaikki muut tapahtumat jaetaan kahteen osaan: panoksiin ja tuotoksiin.



Jotta bitcoineja voidaan käyttää uuden transaktion panoksena, transaktion aloittajan on todistettava hallussaan olevan bitcoinin olemassaolo antamalla tiettyä käsikirjoitusta vastaava allekirjoitus. Jokainen bitcoin (UTXO) sisältää käsikirjoituksen, joka vaatii yleensä tietyn allekirjoituksen, jonka vain haltijan yksityinen avain voi antaa. Nämä skriptit ovat ***scriptSig*** (ASM:ssä), jotka on kirjoitettu Bitcoin-skriptillä, ja ne voivat olla erityyppisiä. Tässä esimerkissä voidaan nähdä, että käytetyt UTXO:t olivat tyypiltään P2SH, ja niiden tuloste oli tyypiltään P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Voit jäljittää tietyn UTXO:n historian heuristiikan avulla. Kutsumme sinut tutustumaan erilaisiin Bitcoin-heuristiikkoihin ja siihen, miten voit vahvistaa Bitcoin-tapahtumien luottamuksellisuutta:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Otetaan esimerkki tämän tapahtuman lähtevistä kuluista. Klikkaamalla tapahtuman tunnusta meidät ohjataan tapahtuman tietosivun kohtaan **Tapahtumat**.



![transaction](assets/fr/08.webp)



Tältä sivulta voit selvittää, mihin BLOCK:een tapahtuma sisältyi. Käytetyn Address:n tyypistä riippuen transaktio voi optimoida tietonsa (*virtuaaliset tavut*) ja maksaa siten vähemmän transaktiomaksuja. Esimerkiksi tämä transaktio säästi 53 % maksuista käyttämällä natiivia SegWit BECH32 Address-muotoa, joka alkaa kirjaimella `bc1q`.



![trx_details](assets/fr/09.webp)



## Liquid-pinnoite



Liquid Network on [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) ja avoimen lähdekoodin tason 2 ratkaisu Bitcoin-protokollalle. Se mahdollistaa erityisesti nopeammat ja luottamuksellisemmat Bitcoin-tapahtumat.



Siirry Liquid Network:aan napsauttamalla BLOCKSTREAM.info-selaimen **"Liquid"** -painiketta.



![liquid](assets/fr/10.webp)



Klikkaamalla yhtä tapahtumaa, jota haluamme seurata, näemme, että Bitcoin-kappaleiden määrät on korvattu sanoilla "**luottamuksellinen**". Tässä verkossa transaktiot voivat olla luottamuksellisia, joten emme voi nähdä kunkin UTXO:n määriä, emme transaktion sisällä emmekä sen ulkopuolella.



![liquid_trx](assets/fr/11.webp)



Huomaamme kuitenkin, että Bitcoin-protokollan Layer:n tärkeimmän osan periaatteet ja mekanismit ovat samat: Bitcoin:n lukitusskriptit ja UTXO:n jäljitettävyys.



![liquid_details](assets/fr/12.webp)



Liquid Network tarjoaa myös muita kuin talletettavia digitaalisia varoja, joita organisaatiot voivat käyttää. Valikosta **"Assets "** löydät luettelon rekisteröidyistä asseteista, niiden kokonaismäärästä ja verkkotunnuksesta, johon ne liittyvät.



![assets](assets/fr/13.webp)



Kunkin omaisuuserän osalta voit jäljittää liikkeeseenlasku- ja polttotapahtumien historian (poistamalla liikkeessä olevan kokonaismäärän).



![assets_trxs](assets/fr/14.webp)




## Lisää vaihtoehtoja



BLOCKSTREAM.info explorer sisältää myös Testnet:n, Bitcoin:n, On-Chain:n ja Liquid Network:n liiketoimien visualisointia ja seurantaa.



![testnet](assets/fr/15.webp)



Testnet-verkossa et käytä oikeita bitcoineja, mutta sinulla on kaikki edellä kuvatut ominaisuudet.



![liquid_testnet](assets/fr/16.webp)



Tässä verkossa on eripituinen ketju, johon voit liittää ja testata Bitcoin- ja Liquid-mekanismien toimintaa.





- API-osio on tarkoitettu kaikille, jotka haluavat integroida tiettyjä Explorerin toimintoja omaan sovellukseensa. Tämän API:n kautta voit tutkia eri kerrosten (On-Chain ja Liquid) pääketjua, seurata transaktioita ja selvittää esimerkiksi BLOCK:n transaktioiden keskimääräiset maksut.



![api](assets/fr/17.webp)



Olet nyt valmis hyödyntämään BLOCKSTREAM Explorerin koko potentiaalia On-Chain- ja Liquid-kerrosten lohkoketjujen kyselyyn. Toivomme, että tämä opetusohjelma oli sinulle informatiivinen, ja suosittelemme opetustamme toisesta Bitcoin Explorerista:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f