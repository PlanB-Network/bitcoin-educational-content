---
name: Blockstream Explorer
description: Tutki Bitcoin:n ja Liquid Network:n pääkerrosta
---

![cover](assets/cover.webp)



Blockstream Explorer on projekti, joka helpottaa Bitcoin-protokollan sekä Blockstream-yhtiön kehittämän [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid:n transaktioiden ja globaalin tilan tutkimista.



Adam Backin perustaman Blockstream-yrityksen vuonna 2014 käynnistämän [blockstream.info](https://blockstream.info) explorerin tavoitteena on tarjota Bitcoin:lle vankka infrastruktuuri, joka takaa yhteentoimivuuden ja transaktioiden seurannan kerrosten (on-chain ja Liquid) välillä ja parantaa samalla käyttäjien turvallisuutta ja yksityisyyttä.



Tässä oppaassa tarkastelemme, mikä erottaa sen muista, sen palveluja ja sitä, miten se tarjoaa saumatonta Bitcoin:n on-chain- ja Liquid-kerrosten toiminnan ja tilan seurantaa.



## Blockstream explorerin käytön aloittaminen



### Navigoi pääkanavalla



Kun siirryt Blockstream.info-selaimeen, "**Dashboard**" -osiossa on oletusarvoisesti valittu Bitcoin-protokollan pääketju. Tästä käyttöliittymästä saat yleiskuvan :





- Pääketjun koko: Äskettäin louhitut lohkot.



![blocks](assets/fr/01.webp)



Tässä osiossa on tietoja äskettäin louhituista lohkoista, aikaleima, kuhunkin lohkoon sisältyvien transaktioiden määrä, koko kilotavuina (kB) ja kunkin lohkon mitta painoyksikköinä (**WU** = *Weight Units*). Viimeksi mainittu mittaustapa on kiinnostava, koska sen avulla voidaan arvioida lohkon optimointia, kun otetaan huomioon, että pääketjun jokainen lohko on rajoitettu 4 000 000 WU:n eli 4 000 kWU:n suuruiseksi.





- Viimeaikaiset liiketoimet.



![transactions](assets/fr/02.webp)



Transaktio-osio sisältää tiedot transaktion yksilöllisestä tunnisteesta, transaktion sisältämästä bitcoin-arvosta, koosta virtuaalitavuina (vB) - joka edustaa kaiken datan (tulo ja lähtö) summaa - ja siihen liittyvästä maksun määrästä. Esimerkiksi transaktio, jonka koko on "153 vB" ja jonka hinta on "2 sat/vB", maksaa "306 satoshia".



### Nesteen etsintä



"**Lohkot**"-valikosta voit seurata koko pääketjun historiaa viimeiseen louhittuun lohkoon asti.



![blocs](assets/fr/03.webp)



Klikkaamalla tiettyä lohkoa saat lisätietoja lohkoon sisältyvistä tiedoista ja tapahtumista. Esimerkiksi lohkon 919330 kohdalla: näet lohkon hashin. Voit myös siirtyä edelliseen lohkoon, sillä jokainen louhittu lohko (Genesis:tä lukuun ottamatta) on linkitetty edelliseen lohkoon ja säilyttää edeltäjänsä hashin.



![metadata](assets/fr/04.webp)



Napsauttamalla **"Tiedot "** -painiketta saat lisätietoja tästä lohkosta, kuten sen tilan, joka vahvistaa, että se on lisätty säilytettyyn ja levitettyyn pääketjuun. Sinulla on myös vaikeusaste, jolla tätä lohkoa louhitaan: tämä vaikeusaste edustaa laskentatehoa, joka tarvitaan mining:n kryptografisen ongelman ratkaisemiseen, ja sitä mukautetaan joka 2016 lohko (noin 2 viikkoa).



![details](assets/fr/05.webp)



Tämän yksityiskohtia koskevan osion alapuolella on kaikki tähän lohkoon sisältyvät tapahtumat.



Lohkon ensimmäistä transaktiota kutsutaan **transaktioksi coinbase**. Sitä käytetään louhijan mining-palkkion jakamiseen (kaikki lohkoon sisältyviin transaktioihin liittyvät maksut ja lohkoavustus). Tällä transaktiolla luodut bitcoinit voidaan käyttää vasta, kun toiset 100 peräkkäistä lohkoa on louhittu. Toisin sanoen voidakseen käyttää niitä louhijan on odotettava lohkon **919430** tuottamista. Tämä tunnetaan nimellä [*"maturity period "*](https://planb.academy/fr/resources/glossary/maturity-period).



Coinbase on erityinen tapahtuma: se on ainoa, jossa ei ole todellista panosta, sillä siinä ei käytetä yhtään bitcoinia edellisestä tapahtumasta.




![coinbase](assets/fr/06.webp)



Kaikki muut tapahtumat jaetaan kahteen osaan: panoksiin ja tuotoksiin.



Jotta bitcoineja voidaan käyttää uuden transaktion panoksena, transaktion aloittajan on todistettava hallussaan olevan bitcoinin olemassaolo antamalla tiettyä käsikirjoitusta vastaava allekirjoitus. Jokainen bitcoin (UTXO) sisältää käsikirjoituksen, joka vaatii yleensä tietyn allekirjoituksen, jonka vain haltijan yksityinen avain voi antaa. Nämä skriptit ovat ***scriptSig*** (ASM:ssä), jotka on kirjoitettu Bitcoin-skriptillä, ja ne voivat olla erityyppisiä. Tässä esimerkissä voidaan nähdä, että käytetyt UTXO:t olivat tyypiltään P2SH, ja niiden tuloste oli tyypiltään P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Voit jäljittää tietyn UTXO:n historiaa heuristiikan avulla. Kutsumme sinut tutustumaan erilaisiin Bitcoin-heuristiikkoihin ja tapoihin vahvistaa Bitcoin-tapahtumien luottamuksellisuutta:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Otetaan esimerkki tämän tapahtuman lähtevistä kuluista. Klikkaamalla tapahtuman tunnusta meidät ohjataan tapahtuman tietosivun kohtaan **Tapahtumat**.



![transaction](assets/fr/08.webp)



Tällä sivulla voit selvittää, mihin lohkoon tapahtuma sisältyi. Käytetystä osoitetyypistä riippuen transaktio voi optimoida datansa (*virtuaaliset tavut*) ja maksaa siten vähemmän transaktiomaksuja. Esimerkiksi tämä transaktio säästi 53 % maksuista käyttämällä natiivia SegWit Bech32-osoiteformaattia, joka alkaa kirjaimella `bc1q`.



![trx_details](assets/fr/09.webp)



## Liquid-kerros



Liquid Network on [*sivuketju*](https://planb.academy/en/resources/glossary/sidechain) ja avoimen lähdekoodin tason 2 ratkaisu Bitcoin-protokollalle. Se mahdollistaa erityisesti nopeammat ja luottamuksellisemmat Bitcoin-tapahtumat.



Napsauta Blockstream.info-selaimessa **"Liquid"**-painiketta siirtyäksesi Liquid-verkkoon.



![liquid](assets/fr/10.webp)



Klikkaamalla yhtä tapahtumista, joita haluamme seurata, näemme, että bitcoin-kappaleiden määrät on korvattu sanoilla "**luottamuksellinen**". Tässä verkossa transaktiot voivat olla luottamuksellisia, joten emme näe kunkin UTXO:n määriä, emme transaktion sisällä emmekä sen ulkopuolella.



![liquid_trx](assets/fr/11.webp)



Huomaamme kuitenkin, että Bitcoin-protokollan pääkerroksessa olevat periaatteet ja mekanismit ovat samat: Bitcoin-lukitusskriptit ja UTXO:n jäljitettävyys.



![liquid_details](assets/fr/12.webp)



Liquid Network tarjoaa myös muita kuin talletettavia digitaalisia varoja, joita organisaatiot voivat käyttää. Valikosta **"Assets "** löydät luettelon rekisteröidyistä asseteista, niiden kokonaismäärästä ja verkkotunnuksesta, johon ne liittyvät.



![assets](assets/fr/13.webp)



Kunkin omaisuuserän osalta voit jäljittää liikkeeseenlasku- ja polttotapahtumien historian (poistamalla liikkeessä olevan kokonaismäärän).



![assets_trxs](assets/fr/14.webp)




## Lisää vaihtoehtoja



Blockstream.info-selain sisältää myös visualisointeja ja Testnet-, Bitcoin-, on-chain- ja Liquid Network-tapahtumien seurantaa.



![testnet](assets/fr/15.webp)



Kun siirryt Testnet-verkkoon, et käytä oikeita bitcoineja, mutta sinulla on kaikki edellä kuvatut ominaisuudet.



![liquid_testnet](assets/fr/16.webp)



Tässä verkossa on eripituinen ketju, johon voit liittää ja testata Bitcoin- ja Liquid-mekanismien toimintaa.





- API-osio on tarkoitettu kaikille, jotka haluavat integroida tiettyjä Explorerin toimintoja omaan sovellukseensa. Tämän API:n kautta voit tutkia eri kerrosten (on-chain ja Liquid) pääketjua, seurata transaktioita ja selvittää esimerkiksi lohkon transaktioiden keskimääräiset maksut.



![api](assets/fr/17.webp)



Olet nyt valmis hyödyntämään Blockstream Explorerin kaikkia mahdollisuuksia lohkoketjujen kyselyyn on-chain- ja Liquid-kerroksilla. Toivomme, että tämä opetusohjelma oli sinulle informatiivinen, ja suosittelemme opetusohjelmaamme toisesta Bitcoin Explorerista:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f