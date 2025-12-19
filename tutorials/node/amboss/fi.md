---
name: Amboss
description: Tutki ja analysoi Lightning Network
---

![cover](assets/cover.webp)



Lightning Network on Bitcoin-protokollan Layer, joka kehitettiin ensisijaisesti edistämään Bitcoin-maksujen käyttöönottoa päivittäisessä käytössä lisäämällä kunkin maksutapahtuman käsittelynopeutta. Hajauttamisperiaatteeseen perustuva Lightning Network koostuu solmuista (Lightning-toteutusta käyttävistä tietokoneista), jotka kommunikoivat vertaisverkkona ja välittävät tietoja (maksuja ja maksujen tarkistuksia) toisilleen.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Aivan kuten pääketjussa, on tullut olennaisen tärkeäksi antaa käyttäjille mahdollisuus saada tietoa verkon tiedoista ja tilasta, jotta voidaan helpottaa solmujen välisiä yhteyksiä ja minimoida verkossa yleensä esiintyvä likviditeettiongelma. Lightning Network:ssä suositellaankin suhteellisen pienempien summien mikromaksuja kuin Bitcoin:n pääketjun transaktioissa.



On tärkeää huomata, että kaikki Lightning-solmut eivät ole saatavilla Amboss-alustalla.



Kuten [Mempool Space](https://Mempool.space), joka tarjoaa hyödyllistä tietoa Bitcoin-protokollan pääketjusta, vuodesta 2022 lähtien [Amboss](https://amboss.space) tarjoaa tietoa :





- Lightning Network:n solmut
- Maksukanavat ja niiden maksukyky
- Lightning Network:n kehitys ajan myötä
- Tilastotiedot maksujen välityssolmujen maksuista.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Tässä opetusohjelmassa tutustumme tähän alustaan, joka on tärkeä resurssi Lightning Network-käyttäjille, niille, jotka haluavat liittää solmunsa laajentaakseen verkkoa jne.




## Etsi parit



Yksi Amboss-alustan tavoitteista on mahdollistaa verkon eri solmukohtien yhdistäminen ja tiedonsiirto toistensa kanssa. Alustan etusivulla voit etsiä suoraan jo tuntemasi solmun nimeä tai löytää solmuja käyttämistäsi suosituimmista Lightning-salkuista.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Kotisivulta löydät myös solmuja, jotka on luokiteltu :




- Kapasiteetin kehitys: solmun julkiseen avaimeen liittyvä Bitcoin-määrä ja sen kaikissa kanavissa käytettävissä oleva kokonaismäärä.
- Kanavien kehitys: uusien yhteyksien määrä verkon muihin solmuihin.
- Solmun suosio: kuinka usein solmua käytetään.



![nodes](assets/fr/03.webp)



Oikean solmun valitseminen edellyttää siis seuraavien kriteerien tarkistamista:





- Varmista, että solmussa on riittävä määrä bitcoineja; mitä suurempi solmun kapasiteetti on, sitä suuremman määrän bitcoineja voit maksaa.





- Varmista, että solmulla on suuri määrä yhteyksiä ja avoimia kanavia verkon muihin solmuihin.





- Varmista, että solmu on aktiivinen ja että sen vertaiset arvostavat sitä edelleen, tarkistamalla uusien kanavien määrä; mitä enemmän uusia kanavia solmulla on avoinna, sitä enemmän muut verkon solmut arvostavat sitä.



Kun olet löytänyt oikean solmun, napsauta sen nimeä, jolloin sinut ohjataan solmun tietosivulle.



Tarkistamalla Interface:n ja hiljattain luodun kanavan Timestamp:n saat vihjeen solmun aktiivisuudesta. Löydät myös tietoa tämän solmun kanavien kapasiteetista: tämä tieto on elintärkeä, jos haluat käyttää tätä solmua aktiivisesti maksujen suorittamiseen.




![node_info](assets/fr/04.webp)



Vasemmanpuoleisessa osiossa on lisätietoja solmun sijainnista. Voit esimerkiksi tarkastella :




- Julkinen avain: tunniste heti solmun nimen alapuolella.
- Tämän solmun maantieteellinen sijainti.




![channels](assets/fr/05.webp)



Tämä Interface kertoo tämän solmun Address-yhteyden: se on muotoa `pubkey@ip:port`. Esimerkissämme haluamme muodostaa yhteyden solmuun, jonka :




- julkinen avain `pubkey` on: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- Satama: `9735`



![geoinfo](assets/fr/06.webp)



**Kanavat**-osiossa näet luettelon avoimista kanavista ja solmun yhteydet verkon muihin solmuihin. Tässä Interface:ssä useat tiedot ovat elintärkeitä sen varmistamiseksi, että solmu vastaa tarpeitamme tai on luotettava:





- Saapuva suhdeluku**: Määrä, jonka solmu veloittaa sinua jokaisesta vastaanottamastaan miljoonasta Satoshi:sta valitusta kanavasta riippuen.
- Suhdeluku (miljoonasosaa)** : joka kuvaa Satoshi:n määrää miljoonaa yksikköä kohti, jonka solmu veloittaa sinulta, kun päätät suorittaa maksun jonkin sen kanavan kautta. Oletetaan, että päätät maksaa `10_000 Sats`:n suuruisen maksun kanavan kautta, jonka ppm-suhde on `500 Sats`, sinun on maksettava solmulle `10_000 * 500 / 1_000_000` satosheja, mikä vastaa `5 Sats`.
- [HTLC] (https://planb.academy/resources/glossary/htlc) enimmäismäärä** : Enimmäismäärä, jonka tämä solmu sallii sinun kulkea jonkin kanavan kautta.



Tämän Interface:n taulukosta löydät kaikki nämä tiedot myös solmusta, johon se on sovitettu.



![channels_info](assets/fr/07.webp)



**Kanavakartat** -osiossa näet solmun eri kanavien jakautumisen ja kapasiteetin. Voit muuttaa näytettäviä jakeluperusteita valitsemalla jonkin vaihtoehdon oikealla olevasta avattavasta luettelosta.



![cha_maps](assets/fr/08.webp)



Osio **Suljetut kanavat** ryhmittelee kaikki solmun entiset kanavat suljetun tyypin mukaan:




- Molemminpuolinen sulkeminen**: edustaa molempien osapuolten suostumusta, jotka allekirjoittavat yksityisellä avaimellaan tapahtuman, joka merkitsee kanavan sulkemista ja saldojen jakamista sen sisällä
- **Pakkosulkeminen**: tarkoittaa kanavan yhden osan äkillistä, yksipuolista sulkemista. Tällaista sulkemista ei suositella, koska Lightning Network on rangaistukseen perustuva protokolla: kun yrität huijata kanavan saldoa, vaarana on, että menetät koko käytettävissä olevan saldosi kyseisessä kanavassa.



![closed](assets/fr/09.webp)



Hanki tietoa kauttakulkumaksuista, joita peritään maksujen reitittämisestä käyttämäsi solmun kanavan kautta



![fees](assets/fr/10.webp)



## Verkkotiedot



Amboss ei keskity ainoastaan verkon jäsenten tietoihin vaan myös itse verkon tilaan.



Vasemmanpuoleisen "Simuloinnit"-valikon **Tilastot** -osiossa on kaavio, joka näyttää onnistuneen maksun todennäköisyyden maksusumman funktiona.



Itse asiassa huomaat, että käyrä laskee, koska maksun määrän kasvaessa sinulla on vähemmän mahdollisuuksia saada maksu maksuun. Tämä kuvastaa Lightning Network:n todellista likviditeettiongelmaa. Esimerkiksi "10_000" satoshin maksulla on "79 %" mahdollisuus toteutua. Toisaalta 3 000 000 satoshin maksun onnistumisen mahdollisuus on alle 13 %.



![network](assets/fr/11.webp)



**Verkkotilastot**-valikossa voit näyttää graafisesti tilastoja :




- Maksukanavat
- Solmut
- Kapasiteetti
- Maksut
- Kanavien kehitys.



![network_stat](assets/fr/12.webp)



**Markkinatilastot** -valikossa voit tarkastella Lightning Network:n likviditeetin kysyntää **Tilauksen tiedot** -vaihtoehdon avulla. Tämä kuvaaja voi myös osoittaa, mitkä kanavat ovat kysytyimpiä ja/tai mitkä ovat huomattavan kapasiteetin omaavia.



![markets](assets/fr/13.webp)




## Työkalut



Amboss tarjoaa useita työkaluja, joiden avulla voit optimoida hakuja ja toimia.



### Lightning Network dekooderi



Tämä työkalu on pääasiassa vastuussa Lightning Invoice-, Lightning Address- tai Lightning URL -osoitteen rakenteen yksityiskohtien antamisesta.



Lähetä etusivun **Tools**-osiossa esimerkiksi Lightning Address.



![decoder](assets/fr/14.webp)



Tästä dekooderista saat esimerkiksi seuraavia tietoja:




- lightning Address:een liittyvä solmun julkinen avain;
- Invoice:n voimassaoloaika Address:stä;
- Vähimmäis- ja enimmäisarvo, jonka voit lähettää;
- Address:een liittyvä Nostr-solmu, jos Nostr on käytössä tässä solmussa.



![decode](assets/fr/15.webp)



### Magma IA



Tutustu Ambossin uusimpaan työkaluun, jolla voit hallita tehokkaasti yhteyksiäsi Lightning Network-solmuihin. Magma AI käyttää erityistä tekoälyä keskittyäkseen tärkeään ongelmaan: solmujen hyvään valintaan, joihin voidaan muodostaa yhteyksiä.



![magma](assets/fr/16.webp)



### Satoshi laskin



Selvitä Bitcoin nykyinen hinta paikallisena valuuttana (EUR / USD). Käytä kotisivulla olevaa satoshislaskuria selvittääksesi nykyisen markkinahinnan.



![calculator](assets/fr/17.webp)




Olet nyt tutustunut alustan ominaisuuksiin ja analyysityökaluihin. Alla on artikkeli Bitcoin **Mempool.space** -etsintäohjelmasta.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f