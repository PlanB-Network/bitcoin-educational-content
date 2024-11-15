---
nimi: Teoreettinen johdatus Lightning-verkkoon
goal: Tutustu Lightning-verkkoon teknisestä näkökulmasta
objectives:
  - Ymmärrä verkon kanavien toiminta.
  - Tutustu termeihin HTLC, LNURL ja UTXO.
  - Omaksu likviditeetin hallinta ja LNN:n maksut.
  - Tunnista Lightning-verkko verkostona.
  - Ymmärrä Lightning-verkon teoreettiset käyttötarkoitukset.
---

# Matka Bitcoinin toiseen kerrokseen

Sukella Lightning-verkon ytimeen, joka on olennainen järjestelmä Bitcoin-siirtojen tulevaisuudelle. LNP201 on teoreettinen kurssi Lightningin teknisestä toiminnasta. Se paljastaa tämän toisen kerroksen verkon perustukset ja mekanismit, jotka on suunniteltu tekemään Bitcoin-maksuista nopeita, taloudellisia ja skaalautuvia.

Sen maksukanavien verkoston ansiosta Lightning mahdollistaa nopeat ja turvalliset siirrot tallentamatta jokaista vaihtoa Bitcoin-lohkoketjuun. Luvuissa opit, miten kanavien avaaminen, hallinta ja sulkeminen toimivat, miten maksut reititetään turvallisesti välityssolmujen kautta vähentäen luottamuksen tarvetta, ja miten likviditeettiä hallitaan. Löydät, mitä sitoumustapahtumat, HTLC:t, peruutusavaimet, rangaistusmekanismit, sipulireititys ja laskut ovat.

Olitpa Bitcoin-aloittelija tai kokeneempi käyttäjä, tämä kurssi tarjoaa arvokasta tietoa Lightning-verkon ymmärtämiseksi ja käyttämiseksi. Vaikka käsittelemmekin joitakin Bitcoinin toiminnan perusteita ensimmäisissä osissa, on olennaista hallita Satoshi Nakamoton keksinnön perusteet ennen sukeltamista LNP201:een.

Nauti löydöstäsi!

+++

# Perusteet

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Lightning-verkon ymmärtäminen

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

![Lightning-verkon ymmärtäminen](https://youtu.be/PszWk046x-I)

Tervetuloa LNP201-kurssille, jonka tavoitteena on selittää Lightning-verkon tekninen toiminta.

Lightning-verkko on maksukanavien verkosto, joka on rakennettu Bitcoin-protokollan päälle ja jonka tavoitteena on mahdollistaa nopeat ja edulliset siirrot. Se mahdollistaa maksukanavien luomisen osallistujien välille, joiden sisällä siirrot voidaan tehdä lähes välittömästi ja minimaalisin kustannuksin tallentamatta jokaista siirtoa erikseen lohkoketjuun. Näin ollen Lightning-verkko pyrkii parantamaan Bitcoinin skaalautuvuutta ja tekemään siitä käyttökelpoisen pienarvoisiin maksuihin.

Ennen "verkon" aspektin tutkimista on tärkeää ymmärtää Lightningissa maksukanavan käsite, sen toiminta ja erityispiirteet. Tämä on tämän ensimmäisen luvun aihe.

### Maksukanavan käsite

Maksukanava mahdollistaa kahden osapuolen, tässä **Alicen** ja **Bobin**, varojen vaihdon Lightning-verkon kautta. Kullakin protagonistilla on solmu, joka on symbolisoitu ympyrällä, ja heidän välillään oleva kanava on esitetty viivasegmenttinä.

![LNP201](assets/en/01.webp)

Esimerkissämme Alicella on 100 000 satoshia hänen puolellaan kanavaa, ja Bobilla on 30 000, yhteensä 130 000 satoshia, mikä muodostaa **kanavan kapasiteetin**.

**Mutta mikä on satoshi?**

**Satoshi** (tai "sat") on yksikkö Bitcoinissa. Euroon verrattuna sentin tavoin satoshi on yksinkertaisesti Bitcoinin murto-osa. Yksi satoshi on yhtä kuin **0.00000001 Bitcoin**, eli yksi sadasosamiljoonasosa Bitcoinista. Bitcoinin arvon noustessa satoshin käyttö muuttuu yhä käytännöllisemmäksi.

### Varojen jakautuminen kanavassa
Palataan maksukanavaan. Keskeinen käsite tässä on "**kanavan puoli**". Kullakin osallistujalla on varoja omalla puolellaan kanavassa: Alicella 100 000 satoshia ja Bobilla 30 000. Kuten olemme nähneet, näiden varojen summa edustaa kanavan kokonaiskapasiteettia, luku, joka asetetaan kun se avataan.

![LNP201](assets/en/02.webp)

Otetaan esimerkki Lightning-siirrosta. Jos Alice haluaa lähettää 40 000 satoshia Bobille, tämä on mahdollista, koska hänellä on tarpeeksi varoja (100 000 satoshia). Tämän siirron jälkeen Alicella on 60 000 satoshia omalla puolellaan ja Bobilla 70 000.

![LNP201](assets/en/03.webp)

**Kanavan kapasiteetti**, 130 000 satoshissa, pysyy vakiona. Mikä muuttuu, on varojen jakautuminen. Tämä järjestelmä ei salli lähettää enemmän varoja kuin mitä omistaa. Esimerkiksi, jos Bob haluaisi lähettää takaisin 80 000 satoshia Alicelle, hän ei voisi, koska hänellä on vain 70 000.

Toinen tapa kuvitella varojen jakautumista on ajatella **liukusäädintä**, joka osoittaa, missä varat ovat kanavassa. Aluksi, kun Alicella on 100 000 satoshia ja Bobilla 30 000, liukusäädin on loogisesti Alicen puolella. 40 000 satoshin siirron jälkeen liukusäädin siirtyy hieman Bobin puolelle, jolla nyt on 70 000 satoshia.

![LNP201](assets/en/04.webp)

Tämä esitystapa voi olla hyödyllinen kuviteltaessa varojen tasapainoa kanavassa.

### Maksukanavan perussäännöt

Ensimmäinen muistettava seikka on, että **kanavan kapasiteetti** on kiinteä. Se on hieman kuin putken halkaisija: se määrittää maksimimäärän varoja, jotka voidaan lähettää kanavan kautta kerralla.
Otetaan esimerkki: jos Alicella on 130 000 satoshia omalla puolellaan, hän voi lähettää enintään 130 000 satoshia Bobille yhdessä siirrossa. Bob voi kuitenkin sen jälkeen lähettää nämä varat takaisin Alicelle, joko osittain tai kokonaan.

Tärkeää on ymmärtää, että kanavan kiinteä kapasiteetti rajoittaa yksittäisen siirron maksimimäärää, mutta ei mahdollisten siirtojen kokonaismäärää, eikä kanavan sisällä vaihdettujen varojen kokonaismäärää.

**Mitä sinun tulisi ottaa mukaasi tästä luvusta?**

- Kanavan kapasiteetti on kiinteä ja määrittää maksimimäärän, joka voidaan lähettää yhdessä siirrossa.
- Kanavan varat on jaettu kahden osallistujan kesken, ja kumpikin voi lähettää toiselle vain ne varat, jotka he omistavat omalla puolellaan.
- Lightning-verkko mahdollistaa siten varojen nopean ja tehokkaan vaihdon, samalla kunnioittaen kanavien kapasiteetin asettamia rajoituksia.

Tämä on tämän ensimmäisen luvun loppu, jossa olemme luoneet perustan Lightning-verkolle. Tulevissa luvuissa näemme, miten avata kanava ja syvennymme tässä käsiteltyihin konsepteihin.

## Bitcoin, osoitteet, UTXO ja siirrot

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

![bitcoin, osoitteet, utxo ja siirrot](https://youtu.be/cadCJ2V7zTg)
Tämä luku on hieman erityinen, sillä se ei suoraan keskity Lightning-verkkoon, vaan Bitcoiniin. Todellakin, Lightning-verkko on kerros Bitcoinin päällä. On siis olennaista ymmärtää tietyt Bitcoinin peruskäsitteet, jotta voimme kunnolla käsittää Lightningin toiminnan seuraavissa luvuissa. Tässä luvussa käymme läpi Bitcoinin vastaanotto-osoitteiden, UTXO:iden sekä Bitcoin-siirtojen toiminnan perusteet.
### Bitcoin-osoitteet, yksityiset avaimet ja julkiset avaimet

Bitcoin-osoite on merkkijono, joka johdetaan **julkisesta avaimesta**, joka puolestaan lasketaan **yksityisestä avaimesta**. Kuten varmasti tiedät, sitä käytetään bitcoinien lukitsemiseen, mikä vastaa niiden vastaanottamista lompakkoosi.

Yksityinen avain on salainen elementti, jota **ei koskaan tulisi jakaa**, kun taas julkinen avain ja osoite voidaan jakaa ilman turvallisuusriskiä (niiden paljastaminen edustaa vain riskiä yksityisyydellesi). Tässä on yleinen esitystapa, jota noudatamme koko tämän koulutuksen ajan:

- **Yksityiset avaimet** esitetään **pystysuunnassa**.
- **Julkiset avaimet** esitetään **vaakasuunnassa**.
- Niiden väri osoittaa, kuka niitä hallitsee (Alice oranssina ja Bob mustana...).

### Bitcoin-siirrot: Varojen lähettäminen ja skriptit

Bitcoinissa siirto tarkoittaa varojen lähettämistä yhdestä osoitteesta toiseen. Otetaan esimerkki, jossa Alice lähettää 0.002 Bitcoinia Bobille. Alice käyttää osoitteeseensa liitettyä yksityistä avainta **allekirjoittaakseen** siirron, todistaen näin, että hän todella pystyy käyttämään näitä varoja. Mutta mitä tarkalleen ottaen tapahtuu tämän siirron takana? Bitcoin-osoitteessa olevat varat on lukittu **skriptillä**, eräänlaisella miniohjelmalla, joka asettaa tiettyjä ehtoja varojen käyttämiseksi.

Yleisin skripti vaatii allekirjoituksen osoitteeseen liitetyllä yksityisellä avaimella. Kun Alice allekirjoittaa siirron yksityisellä avaimellaan, hän **avaa skriptin**, joka estää varojen siirtämisen, ja ne voidaan sitten siirtää. Varojen siirtoon liittyy uuden skriptin lisääminen näihin varoihin, joka määrää, että niiden käyttämiseen tällä kertaa tarvitaan **Bobin** yksityisen avaimen allekirjoitus.

![LNP201](assets/en/05.webp)

### UTXO:t: Käyttämättömät siirtojen tulosteet

Bitcoinissa vaihdamme itse asiassa suoraan bitcoineja, vaan **UTXO:ita** (_Unspent Transaction Outputs_), tarkoittaen "käyttämättömiä siirtojen tulosteita".

UTXO on bitcoinin pala, joka voi olla minkä tahansa arvoinen, esimerkiksi **2,000 bitcoina**, **8 bitcoinia** tai jopa **8,000 satsia**. Jokainen UTXO on lukittu skriptillä, ja sen käyttämiseen täytyy täyttää skriptin ehdot, usein allekirjoitus annetun vastaanotto-osoitteen yksityisellä avaimella.

UTXO:ita ei voi jakaa. Joka kerta, kun niitä käytetään edustamansa bitcoin-määrän kuluttamiseen, se on tehtävä kokonaisuudessaan. Se on hieman kuin setelin kanssa: jos sinulla on 10 euron seteli ja sinun täytyy maksaa leipurille 5 euroa, et voi vain leikata seteliä puoliksi. Sinun täytyy antaa hänelle 10 euron seteli, ja hän antaa sinulle 5 euroa vaihtorahaa. Tämä on täsmälleen sama periaate UTXO:iden kanssa Bitcoinissa! Esimerkiksi, kun Alice avaa skriptin yksityisellä avaimellaan, hän avaa koko UTXO:n. Jos hän haluaa lähettää vain osan UTXO:n edustamista varoista Bobille, hän voi "pilkkoa" sen useampaan pienempään osaan. Hän lähettää sitten 0.0015 BTC Bobille ja lähettää loput, 0.0005 BTC, **vaihto-osoitteeseen**.

Tässä on esimerkki siirrosta, jossa on 2 tulostetta:
- UTXO, joka on 0,0015 BTC Bobille, lukittu skriptillä, joka vaatii Bobin yksityisen avaimen allekirjoituksen.
- UTXO, joka on 0,0005 BTC Alicelle, lukittu skriptillä, joka vaatii hänen oman allekirjoituksensa.

![LNP201](assets/en/06.webp)

### Moniallekirjoitusosoitteet

Yksinkertaisten osoitteiden, jotka on luotu yhdestä julkisesta avaimesta, lisäksi on mahdollista luoda **moniallekirjoitusosoitteita** useista julkisista avaimista. Erityisen kiinnostava tapaus Lightning-verkolle on **2/2 moniallekirjoitusosoite**, joka on luotu kahdesta julkisesta avaimesta:

![LNP201](assets/en/07.webp)

Jotta varat, jotka on lukittu tällä 2/2 moniallekirjoitusosoitteella, voidaan käyttää, on tarpeen allekirjoittaa kahdella yksityisellä avaimella, jotka liittyvät julkisiin avaimiin.

![LNP201](assets/en/08.webp)

Tämä osoitetyyppi on nimenomaan Bitcoin-lohkoketjun esitys Lightning-verkon maksukanavista.

**Mitä sinun tulisi oppia tästä luvusta?**

- **Bitcoin-osoite** johdetaan julkisesta avaimesta, joka puolestaan on johdettu yksityisestä avaimesta.
- Bitcoinissa varat lukitaan **skripteillä**, ja näiden varojen käyttämiseksi on täytettävä skriptin vaatimukset, mikä yleensä tarkoittaa vastaavan yksityisen avaimen allekirjoituksen antamista.
- **UTXO:t** ovat bitcoineja, jotka on lukittu skripteillä, ja jokainen Bitcoin-siirto koostuu UTXO:n lukituksen avaamisesta ja sitten yhden tai useamman uuden luomisesta vastineeksi.
- **2/2 moniallekirjoitusosoitteet** vaativat kahden yksityisen avaimen allekirjoituksen varojen käyttämiseksi. Nämä erityiset osoitteet ovat käytössä Lightning-verkossa maksukanavien luomiseksi.

Tämä luku Bitcoinista on antanut meille mahdollisuuden kerrata joitakin olennaisia käsitteitä tulevaa varten. Seuraavassa luvussa tutustumme erityisesti siihen, miten kanavien avaaminen Lightning-verkossa toimii.

# Kanavien Avaaminen ja Sulkeminen

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Kanavan Avaaminen

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

![avaa kanava](https://youtu.be/B2caBC0Rxko)

Tässä luvussa tarkastelemme tarkemmin, miten maksukanava avataan Lightning-verkossa ja ymmärrämme yhteyden tämän toimenpiteen ja taustalla olevan Bitcoin-järjestelmän välillä.

### Lightning-kanavat

Kuten ensimmäisessä luvussa näimme, Lightning-verkon **maksukanavaa** voidaan verrata "putkeen", jossa varoja vaihdetaan kahden osallistujan (**Alicen** ja **Bobin** esimerkeissämme) välillä. Tämän kanavan kapasiteetti vastaa kummankin puolen saatavilla olevien varojen summaa. Esimerkissämme Alicella on **100 000 satoshia** ja Bobilla **30 000 satoshia**, mikä antaa **kokonaiskapasiteetiksi 130 000 satoshia**.

![LNP201](assets/en/09.webp)

### Tiedonvaihdon Tasot

On tärkeää selvästi erottaa Lightning-verkon eri tiedonvaihtotasot:

- **Vertaisverkkoviestintä (Lightning-protokolla)**: Nämä ovat viestejä, joita Lightning-solmut lähettävät toisilleen kommunikoidakseen. Esitämme nämä viestit katkoviivoilla diagrammeissamme.
- **Maksukanavat (Lightning-protokolla)**: Nämä ovat polkuja varojen vaihtoon Lightning-verkossa, jotka esitämme yhtenäisinä mustina viivoina.
- **Bitcoin-siirrot (Bitcoin-protokolla)**: Nämä ovat onchain-tapahtumia, jotka esitämme oransseilla viivoilla.

![LNP201](assets/en/10.webp)
On huomionarvoista, että Lightning-solmu voi kommunikoida P2P-protokollan kautta avaamatta kanavaa, mutta varojen vaihtamiseksi kanava on välttämätön.
### Vaiheet Lightning-kanavan avaamiseksi

1. **Viestien vaihto**: Alice haluaa avata kanavan Bobin kanssa. Hän lähettää Bobille viestin, joka sisältää summan, jonka hän haluaa tallettaa kanavalle (130 000 satsia) ja hänen julkisen avaimensa. Bob vastaa jakamalla oman julkisen avaimensa.

![LNP201](assets/en/11.webp)

2. **Moniallekirjoitusosoitteen luominen**: Näillä kahdella julkisella avaimella Alice luo **2/2 moniallekirjoitusosoitteen**, mikä tarkoittaa, että myöhemmin tähän osoitteeseen talletetut varat vaativat molempien allekirjoitukset (Alicen ja Bobin) käytettäväksi.

![LNP201](assets/en/12.webp)

3. **Talletustransaktio**: Alice valmistelee Bitcoin-transaktion tallettaakseen varoja tähän moniallekirjoitusosoitteeseen. Esimerkiksi hän voi päättää lähettää **130 000 satoshia** tähän moniallekirjoitusosoitteeseen. Tämä transaktio on **muodostettu, mutta ei vielä julkaistu** lohkoketjussa.

![LNP201](assets/en/13.webp)

4. **Nostotransaktio**: Ennen talletustransaktion julkaisemista Alice muodostaa nostotransaktion, jotta hän voi palauttaa varansa ongelmatilanteessa Bobin kanssa. Todellakin, kun Alice julkaisee talletustransaktion, hänen satsinsa lukitaan 2/2 moniallekirjoitusosoitteeseen, joka vaatii sekä hänen että Bobin allekirjoituksen vapautettavaksi. Alice suojautuu tämän tappioriskin varalta muodostamalla nostotransaktion, joka mahdollistaa hänen varojensa palauttamisen.

![LNP201](assets/en/14.webp)

5. **Bobin allekirjoitus**: Alice lähettää talletustransaktion Bobille todisteena ja pyytää häntä allekirjoittamaan nostotransaktion. Kun Bobin allekirjoitus on saatu nostotransaktioon, Alice on varmistunut siitä, että hän voi palauttaa varansa milloin tahansa, koska nyt tarvitaan vain hänen oma allekirjoituksensa moniallekirjoitusosoitteen vapauttamiseen.

![LNP201](assets/en/15.webp)

6. **Talletustransaktion julkaiseminen**: Kun Bobin allekirjoitus on saatu, Alice voi julkaista talletustransaktion Bitcoin-lohkoketjussa, virallisesti avaten Lightning-kanavan kahden käyttäjän välille.

![LNP201](assets/en/16.webp)

### Milloin kanava on avoin?

Kanava katsotaan avatuksi, kun talletustransaktio on sisällytetty Bitcoin-lohkoon ja se on saavuttanut tietyn syvyyden vahvistuksissa (seuraavien lohkojen määrä).

**Mitä sinun tulisi muistaa tästä luvusta?**

- Kanavan avaaminen alkaa **viestien vaihdolla** kahden osapuolen välillä (summan ja julkisten avainten vaihto).
- Kanava muodostetaan luomalla **2/2 moniallekirjoitusosoite** ja tallettamalla varoja siihen Bitcoin-transaktion kautta.
- Kanavan avaava henkilö varmistaa, että hän voi **palauttaa varansa** nostotransaktion kautta, joka on allekirjoitettu toisen osapuolen toimesta ennen talletustransaktion julkaisemista.

Seuraavassa luvussa tutustumme Lightning-transaktion tekniseen toimintaan kanavalla.

## Sitoutumistransaktio

<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

![Lightning transaction & commitment transaction](https://youtu.be/aPqI34tpypM)

Tässä luvussa tutustumme Lightning-verkon kanavalla tapahtuvan transaktion tekniseen toimintaan, eli kun varoja siirretään kanavan toiselta puolelta toiselle.

### Muistutus kanavan elinkaaresta
Kuten aiemmin nähtiin, Lightning-kanava alkaa **avaamalla** Bitcoin-siirrolla. Kanava voidaan **sulkea** milloin tahansa, myös Bitcoin-siirrolla. Näiden kahden hetken välillä kanavassa voidaan suorittaa lähes rajaton määrä siirtoja ilman, että tarvitsee käyttää Bitcoinin lohkoketjua. Katsotaan, mitä tapahtuu kanavassa suoritetun siirron aikana.

![LNP201](assets/en/17.webp)

### Kanavan alkutila

Kanavan avaamisen hetkellä Alice talletti **130 000 satoshia** kanavan multisignatuuri-osoitteeseen. Näin ollen alkutilassa kaikki varat ovat Alicen puolella. Ennen kanavan avaamista Alice sai myös Bobin allekirjoittamaan **nostotapahtuman**, joka mahdollistaisi hänelle varojen takaisin saamisen, jos hän haluaisi sulkea kanavan.

![LNP201](assets/en/18.webp)

### Julkaisemattomat Siirrot: Sitoumustapahtumat

Kun Alice tekee kanavassa siirron lähettääkseen varoja Bobille, luodaan uusi Bitcoin-siirto, joka heijastaa tämän muutoksen varojen jakautumisessa. Tätä siirtoa, jota kutsutaan **sitoumustapahtumaksi**, ei julkaista lohkoketjussa, mutta se edustaa kanavan uutta tilaa Lightning-siirron jälkeen.

Otetaan esimerkki, jossa Alice lähettää 30 000 satoshia Bobille:

- **Aluksi**: Alicella on 130 000 satoshia.
- **Siirron jälkeen**: Alicella on 100 000 satoshia ja Bobilla 30 000 satoshia.
  Tämän siirron vahvistamiseksi Alice ja Bob luovat uuden **julkaisemattoman Bitcoin-siirron**, joka lähettäisi **100 000 satoshia Alicelle** ja **30 000 satoshia Bobille** multisignatuuri-osoitteesta. Molemmat osapuolet rakentavat tämän siirron itsenäisesti, mutta samoilla tiedoilla (määrät ja osoitteet). Kun siirto on rakennettu, kumpikin allekirjoittaa siirron ja vaihtaa allekirjoituksensa toisen osapuolen kanssa. Tämä mahdollistaa kummankin osapuolen julkaista siirron milloin tahansa tarvittaessa palauttaakseen osuutensa kanavasta päässä Bitcoin-lohkoketjussa.
  ![LNP201](assets/en/19.webp)

### Siirtoprosessi: Lasku

Kun Bob haluaa vastaanottaa varoja, hän lähettää Alicelle **_laskun_** 30 000 satoshista. Alice jatkaa tämän laskun maksamista aloittamalla siirron kanavassa. Kuten olemme nähneet, tämä prosessi perustuu uuden **sitoumustapahtuman** luomiseen ja allekirjoittamiseen.

Jokainen sitoumustapahtuma edustaa kanavan varojen uutta jakautumista siirron jälkeen. Tässä esimerkissä siirron jälkeen Bobilla on 30 000 satoshia ja Alicella 100 000 satoshia. Jos jompikumpi kahdesta osallistujasta päättäisi julkaista tämän sitoumustapahtuman lohkoketjussa, se johtaisi kanavan sulkemiseen ja varojen jakautumiseen tämän viimeisen jakautumisen mukaisesti.

![LNP201](assets/en/20.webp)

### Uusi tila toisen siirron jälkeen

Otetaan toinen esimerkki: ensimmäisen siirron jälkeen, jossa Alice lähetti 30 000 satoshia Bobille, Bob päättää lähettää **10 000 satoshia takaisin Alicelle**. Tämä luo kanavan uuden tilan. Uusi **sitoumustapahtuma** edustaa tätä päivitettyä jakautumista:

- **Alice**lla on nyt **110 000 satoshia**.
- **Bob**illa on **20 000 satoshia**.

![LNP201](assets/en/21.webp)

Jälleen, tätä siirtoa ei julkaista lohkoketjussa, mutta se voidaan julkaista milloin tahansa, jos kanava suljetaan.

Yhteenvetona, kun varoja siirretään Lightning-kanavassa:
- Alice ja Bob luovat uuden **sitoumustapahtuman**, joka heijastaa varojen uutta jakautumista. - Tämä Bitcoin-tapahtuma **allekirjoitetaan** molempien osapuolten toimesta, mutta sitä **ei julkaista** Bitcoin-lohkoketjussa niin kauan kuin kanava pysyy avoimena.
- Sitoumustapahtumat varmistavat, että kumpikin osapuoli voi milloin tahansa palauttaa varansa Bitcoin-lohkoketjussa julkaisemalla viimeksi allekirjoitetun tapahtuman.

Tässä järjestelmässä on kuitenkin potentiaalinen puute, johon puutumme seuraavassa luvussa. Näemme, miten kumpikin osapuoli voi suojautua toisen osapuolen huijausyritykseltä.

## Revocation Key

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>
![transactions part 2](https://youtu.be/RRvoVTLRJ84)
Tässä luvussa syvennymme siihen, miten tapahtumat toimivat Lightning-verkossa keskustelemalla mekanismeista, jotka suojaavat huijauksilta, varmistaen, että kumpikin osapuoli noudattaa kanavan sääntöjä.

### Muistutus: Sitoumustapahtumat

Kuten aiemmin näimme, Lightning-tapahtumat perustuvat julkaisemattomiin **sitoumustapahtumiin**. Nämä tapahtumat heijastavat kanavan varojen nykyistä jakautumista. Kun uusi Lightning-tapahtuma tehdään, luodaan ja allekirjoitetaan uusi sitoumustapahtuma molempien osapuolten toimesta heijastamaan kanavan uutta tilaa.

Otetaan yksinkertainen esimerkki:

- **Alkutila**: Alicella on **100 000 satoshia**, Bobilla **30 000 satoshia**.
- Tapahtuman jälkeen, jossa Alice lähettää **40 000 satoshia** Bobille, uusi sitoumustapahtuma jakaa varat seuraavasti:
  - Alice: **60 000 satoshia**
  - Bob: **70 000 satoshia**

![LNP201](assets/en/22.webp)

Milloin tahansa molemmat osapuolet voivat julkaista **viimeisimmän sitoumustapahtuman** allekirjoitettuna sulkeakseen kanavan ja palauttaakseen varansa.

### Puute: Huijaaminen julkaisemalla vanha tapahtuma

Potentiaalinen ongelma ilmenee, jos jompikumpi osapuoli päättää **huijata** julkaisemalla vanhan sitoumustapahtuman. Esimerkiksi Alice voisi julkaista vanhemman sitoumustapahtuman, jossa hänellä oli **100 000 satoshia**, vaikka todellisuudessa hänellä on nyt vain **60 000**. Tämä mahdollistaisi hänelle **40 000 satoshin** varastamisen Bobilta.

![LNP201](assets/en/23.webp)

Vielä pahempaa, Alice voisi julkaista kaikkein ensimmäisen nostotapahtuman, sen ennen kuin kanava avattiin, jossa hänellä oli **130 000 satoshia**, ja siten varastaa koko kanavan varat.

![LNP201](assets/en/24.webp)

### Ratkaisu: Revocation Key ja Timelock

Estääkseen tällaisen huijauksen Alicen toimesta, Lightning-verkossa sitoumustapahtumiin lisätään **turvamekanismeja**:

1. **Timelock**: Jokainen sitoumustapahtuma sisältää aikalukon Alicen varoille. Aikalukko on älykäs sopimusprimitiivi, joka asettaa aikaehtoja, jotka on täytettävä, jotta tapahtuma voidaan lisätä lohkoon. Tämä tarkoittaa, että Alice ei voi palauttaa varojaan ennen kuin tietty määrä lohkoja on kulunut, jos hän julkaisee jonkin sitoumustapahtumista. Tämä aikalukko alkaa soveltua sitoumustapahtuman vahvistamisesta. Sen kesto on yleensä suhteessa kanavan kokoon, mutta sen voi myös määrittää manuaalisesti.
2. **Revocation Key**: Alicen varat voidaan myös välittömästi käyttää Bobin toimesta, jos hänellä on **revocation key**. Tämä avain koostuu salaisuudesta, joka on Alicen hallussa, ja salaisuudesta, joka on Bobin hallussa. Huomaa, että tämä salaisuus on erilainen jokaiselle sitoumustapahtumalle.
Näiden kahden yhdistetyn mekanismin ansiosta Bobilla on aikaa havaita Alicen yritys huijata, ja rangaista häntä palauttamalla hänen tulonsa peruutusavaimella, mikä Bobille tarkoittaa kanavan kaikkien varojen takaisin saamista. Uusi sitoumustapahtumamme näyttää nyt tältä:
![LNP201](assets/en/25.webp)

Käydään yhdessä läpi tämän mekanismin toiminta.

### Tapahtuman Päivitysprosessi

Kun Alice ja Bob päivittävät kanavan tilan uudella Lightning-tapahtumalla, he vaihtavat etukäteen omat **salaisuutensa** edelliseen sitoumustapahtumaan (se, joka tulee vanhentuneeksi ja voisi mahdollistaa toisen huijaamisen). Tämä tarkoittaa, että kanavan uudessa tilassa:

- Alicella ja Bobilla on uusi sitoumustapahtuma, joka edustaa varojen nykyistä jakautumista Lightning-tapahtuman jälkeen.
- Kummallakin on toisen salaisuus edellisestä tapahtumasta, mikä mahdollistaa peruutusavaimen käytön vain, jos toinen yrittää huijata julkaisemalla vanhan tilan tapahtuman Bitcoin-verkon mempooleissa. Todellakin, toisen osapuolen rankaisemiseksi on välttämätöntä hallita molempia salaisuuksia ja toisen sitoumustapahtumaa, joka sisältää allekirjoitetun syötteen. Ilman tätä tapahtumaa peruutusavain yksinään on hyödytön. Ainoa tapa saada tämä tapahtuma on hakea se mempooleista (vahvistusta odottavissa tapahtumissa) tai vahvistetuissa tapahtumissa lohkoketjussa aikaviiveen aikana, mikä todistaa, että toinen osapuoli yrittää huijata, tahallisesti tai ei.

Otetaan esimerkki ymmärtääksemme tämän prosessin hyvin:

1. **Alkutila**: Alicella on **100 000 satoshia**, Bobilla **30 000 satoshia**.

![LNP201](assets/en/26.webp)

2. Bob haluaa saada 40 000 satoshia Alicelta heidän Lightning-kanavansa kautta. Tehdäkseen niin:
   - Hän lähettää hänelle laskun yhdessä salaisuutensa kanssa peruutusavaimen edellisen sitoumustapahtuman osalta.
   - Vastauksena Alice antaa allekirjoituksensa Bobin uudelle sitoumustapahtumalle sekä oman salaisuutensa edellisen tapahtuman peruutusavaimelle.
   - Lopuksi Bob lähettää allekirjoituksensa Alicen uudelle sitoumustapahtumalle.
   - Nämä vaihdot mahdollistavat Alicen lähettämään **40 000 satoshia** Bobille Lightningin kautta heidän kanavassaan, ja uudet sitoumustapahtumat nyt heijastavat tätä uutta varojen jakautumista.

![LNP201](assets/en/27.webp)

3. Jos Alice yrittää julkaista vanhan sitoumustapahtuman, jossa hänellä oli edelleen **100 000 satoshia**, Bob, saatuaan peruutusavaimen, voi välittömästi palauttaa varat käyttämällä tätä avainta, kun taas Alice on estetty aikaviiveen vuoksi.

![LNP201](assets/en/28.webp)

Vaikka tässä tapauksessa Bobilla ei ole taloudellista etua yrittää huijata, jos hän kuitenkin tekee niin, Alice hyötyy myös symmetrisestä suojasta, joka tarjoaa hänelle samat takeet.

**Mitä sinun tulisi ottaa mukaasi tästä luvusta?**

Lightning-verkon **sitoumustapahtumat** sisältävät turvamekanismeja, jotka vähentävät sekä huijaamisen riskiä että siihen kannustimia. Ennen uuden sitoumustapahtuman allekirjoittamista Alice ja Bob vaihtavat keskenään omat **salaisuutensa** edellisistä sitoumustapahtumista. Jos Alice yrittää julkaista vanhan sitoumustapahtuman, Bob voi käyttää **peruutusavainta** palauttaakseen kaikki varat ennen kuin Alice voi (koska hän on estetty aikaviiveen vuoksi), mikä rankaisee häntä huijaamisen yrityksestä.

Tämä turvajärjestelmä varmistaa, että osallistujat noudattavat Lightning-verkon sääntöjä, eivätkä he voi hyötyä vanhojen sitoumustapahtumien julkaisemisesta.
Tässä koulutuksen vaiheessa tiedät nyt, miten Lightning-kanavat avataan ja miten transaktiot näissä kanavissa toimivat. Seuraavassa luvussa tulemme tutustumaan eri tapoihin sulkea kanava ja palauttaa bitcoinsi päälohkoketjuun.

## Kanavan sulkeminen

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

![sulje kanava](https://youtu.be/FVmQvNpVW8Y)

Tässä luvussa keskustelemme **kanavan sulkemisesta** Lightning-verkossa, joka tehdään Bitcoin-transaktiolla, aivan kuten kanavan avaaminen. Nähtyämme, miten transaktiot kanavassa toimivat, on nyt aika nähdä, miten sulkea kanava ja palauttaa varat Bitcoin-lohkoketjuun.

### Muistutus kanavan elinkaaresta

**Kanavan elinkaari** alkaa sen **avaamisesta**, Bitcoin-transaktion kautta, sitten Lightning-transaktioita tehdään sen sisällä, ja lopulta, kun osapuolet haluavat palauttaa varansa, kanava **suljetaan** toisen Bitcoin-transaktion kautta. Välilliset transaktiot Lightningissa esitetään julkaisemattomina **sitoumustransaktioina**.

![LNP201](assets/en/29.webp)

### Kolme kanavan sulkemistapaa

On kolme pääasiallista tapaa sulkea tämä kanava, joita voidaan kutsua **hyväksi, pahaksi ja rumaksi** (inspiroituneena Andreas Antonopoulosin teoksesta _Mastering the Lightning Network_):

1. **Hyvä**: **yhteistyöllinen sulkeminen**, jossa Alice ja Bob sopivat kanavan sulkemisesta.
2. **Paha**: **pakotettu sulkeminen**, jossa yksi osapuolista päättää sulkea kanavan rehellisesti, mutta ilman toisen suostumusta.
3. **Ruma**: **huijaamisella tapahtuva sulkeminen**, jossa yksi osapuolista yrittää varastaa varoja julkaisemalla vanhan sitoumustransaktion (mikä tahansa paitsi viimeisin, joka heijastaa todellista ja reilua varojen jakautumista).

Otetaan esimerkki:

- Alicella on **100 000 satoshia** ja Bobilla **30 000 satoshia**.
- Tämä jakautuminen heijastuu **kahdessa sitoumustransaktiossa** (yksi per käyttäjä), jotka eivät ole julkaistuja, mutta voisivat olla kanavan sulkemisen yhteydessä.

![LNP201](assets/en/30.webp)

### Hyvä: yhteistyöllinen sulkeminen

**Yhteistyöllisessä sulkemisessa** Alice ja Bob sopivat kanavan sulkemisesta. Näin se tapahtuu:

1. Alice lähettää Bobille viestin Lightning-viestintäprotokollan kautta ehdottaakseen kanavan sulkemista.
2. Bob suostuu, ja kaksi osapuolta eivät tee enää transaktioita kanavassa.

![LNP201](assets/en/31.webp)

3. Alice ja Bob neuvottelevat yhdessä **sulkemistransaktion** kulut. Nämä kulut lasketaan yleensä Bitcoinin kulupörssin perusteella sulkemishetkellä. On tärkeää huomata, että **se henkilö, joka avasi kanavan** (esimerkissämme Alice) maksaa sulkemiskulut.
4. He rakentavat uuden **sulkemistransaktion**. Tämä transaktio muistuttaa sitoumustransaktiota, mutta ilman aikalukkoja tai peruutusmekanismeja, koska molemmat osapuolet tekevät yhteistyötä eikä huijaamisen riskiä ole. Tämä yhteistyöllinen sulkemistransaktio on siis erilainen kuin sitoumustransaktiot.
Esimerkiksi, jos Alice omistaa **100 000 satoshia** ja Bob **30 000 satoshia**, lopetustransaktio lähettää **100 000 satoshia** Alicen osoitteeseen ja **30 000 satoshia** Bobin osoitteeseen ilman aikalukkorajoituksia. Kun molemmat osapuolet ovat allekirjoittaneet tämän transaktion, Alice julkaisee sen. Kun transaktio on vahvistettu Bitcoin-lohkoketjussa, Lightning-kanava suljetaan virallisesti.
![LNP201](assets/en/32.webp)

**Yhteistyöllinen sulkeminen** on suosittu sulkemistapa, koska se on nopea (ei aikalukkoa) ja transaktiomaksut mukautuvat nykyisten Bitcoin-markkinaolosuhteiden mukaan. Tämä välttää liian pienten maksujen maksamisen, mikä voisi riskeerata transaktion jumiutumisen mempooleihin, tai tarpeettoman yli maksamisen, mikä johtaa tarpeettomiin taloudellisiin tappioihin osallistujille.

### Huono: pakotettu sulkeminen

Kun Alicen solmu lähettää Bobille viestin pyytäen yhteistyöllistä sulkemista, ja jos hän ei vastaa (esimerkiksi internet-katkoksen tai teknisen ongelman vuoksi), Alice voi edetä **pakotettuun sulkemiseen** julkaisemalla **viimeisen allekirjoitetun sitoumustapahtuman**.
Tässä tapauksessa Alice yksinkertaisesti julkaisee viimeisen sitoumustapahtuman, joka heijastaa kanavan tilaa viimeisen Lightning-transaktion tapahtumahetkellä oikealla varojen jaolla.

![LNP201](assets/en/33.webp)

Tässä transaktiossa on **aikalukko** Alicen varoille, mikä tekee sulkemisesta hitaamman.

![LNP201](assets/en/34.webp)

Lisäksi sitoumustapahtuman maksut voivat olla sopimattomia sulkemishetkellä, koska ne asetettiin, kun transaktio luotiin, joskus useita kuukausia aiemmin. Yleensä Lightning-asiakkaat yliarvioivat maksuja välttääkseen tulevaisuuden ongelmia, mutta tämä voi johtaa liiallisiin maksuihin tai päinvastoin liian alhaisiin.

Yhteenvetona, **pakotettu sulkeminen** on viimeinen vaihtoehto, kun vertaisosapuoli ei enää vastaa. Se on hitaampi ja vähemmän taloudellinen kuin yhteistyöllinen sulkeminen. Siksi sitä tulisi välttää mahdollisuuksien mukaan.

### Huijaus: pettäminen

Lopuksi, sulkeminen **pettämisen** kautta tapahtuu, kun jompikumpi osapuoli yrittää julkaista vanhan sitoumustapahtuman, usein sellaisen, jossa heillä oli enemmän varoja kuin heillä pitäisi olla. Esimerkiksi Alice saattaisi julkaista vanhan transaktion, jossa hän omisti **120 000 satoshia**, vaikka hänellä on todellisuudessa nyt vain **100 000**.

![LNP201](assets/en/35.webp)

Bob, estääkseen tämän petoksen, valvoo Bitcoin-lohkoketjua ja sen mempoolia varmistaakseen, ettei Alice julkaise vanhaa transaktiota. Jos Bob havaitsee petosyrityksen, hän voi käyttää **kumoamisavainta** palauttaakseen Alicen varat ja rangaistakseen häntä ottamalla koko kanavan varat. Koska Alicen lähtö on estetty aikalukolla, Bobilla on aikaa käyttää sitä ilman aikalukkoa omalla puolellaan palauttaakseen koko summan osoitteeseen, joka hän omistaa.

![LNP201](assets/en/36.webp)

Ilmeisesti petos voi potentiaalisesti onnistua, jos Bob ei toimi aikalukon Alicen lähdössä asettamassa ajassa. Tässä tapauksessa Alicen lähtö avautuu, mahdollistaen hänelle sen kuluttamisen luodakseen uuden lähdön osoitteeseen, jonka hän hallitsee.

**Mitä sinun tulisi ottaa tästä luvusta mukaasi?**

Kanavan sulkemiseen on kolme tapaa:

1. **Yhteistyöllinen sulkeminen**: Nopea ja vähemmän kallis, missä molemmat osapuolet suostuvat sulkemaan kanavan ja julkaisemaan räätälöidyn sulkemistransaktion.
2. **Pakotettu sulkeminen**: Vähemmän toivottava, koska se perustuu sitoumustapahtuman julkaisemiseen, mahdollisesti sopimattomilla maksuilla ja aikalukolla, mikä hidastaa sulkemista.
3. **Huijaaminen**: Jos jompikumpi osapuolista yrittää varastaa varoja julkaisemalla vanhan transaktion, toinen voi käyttää peruutusavainta rangaistakseen tästä huijauksesta.
Tulevissa luvuissa tutkimme Lightning-verkkoa laajemmasta näkökulmasta, keskittyen siihen, miten sen verkosto toimii.

# Likviditeettiverkosto

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Lightning-verkko

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

![lightning network](https://youtu.be/RAZAa3v41DM)

Tässä luvussa tutkimme, miten maksut Lightning-verkossa voivat saavuttaa vastaanottajan, vaikka he eivät olisikaan suoraan yhdistettyjä maksukanavalla. Lightning on todellakin **maksukanavien verkosto**, joka mahdollistaa varojen lähettämisen kaukaiselle solmulle muiden osallistujien kanavien kautta. Tulemme löytämään, miten maksut reititetään verkoston läpi, miten likviditeetti liikkuu kanavien välillä, ja miten transaktiomaksut lasketaan.

### Maksukanavien verkosto

Lightning-verkossa transaktio vastaa varojen siirtoa kahden solmun välillä. Kuten aiemmissa luvuissa on nähty, Lightning-transaktioiden suorittamiseksi on tarpeen avata kanava jonkun kanssa. Tämä kanava mahdollistaa lähes rajattoman määrän off-chain-transaktioita ennen sen sulkemista on-chain-saldon takaisin saamiseksi. Tällä menetelmällä on kuitenkin haittana, että toisen henkilön kanssa tarvitaan suora kanava varojen vastaanottamiseksi tai lähettämiseksi, mikä tarkoittaa avaamistransaktiota ja sulkemistransaktiota jokaiselle kanavalle. Jos aion tehdä suuren määrän maksuja tämän henkilön kanssa, kanavan avaaminen ja sulkeminen muuttuu kustannustehokkaaksi. Päinvastoin, jos tarvitsen suorittaa vain muutaman Lightning-transaktion, suoran kanavan avaaminen ei ole edullista, koska se maksaisi minulle 2 on-chain-transaktiota rajalliselle määrälle off-chain-transaktioita. Tämä tilanne saattaisi ilmetä esimerkiksi silloin, kun haluaa maksaa Lightningilla kauppiaalle ilman aikomusta palata.

Tämän ongelman ratkaisemiseksi Lightning-verkko mahdollistaa maksun reitittämisen useiden kanavien ja välisolmujen kautta, mahdollistaen siten transaktion ilman suoraa kanavaa toisen henkilön kanssa.

Kuvitellaan esimerkiksi, että:

- **Alice** (oranssissa) on kanavassa **Suzien** (harmaassa) kanssa, jolla on **100 000 satoshia** hänen puolellaan ja **30 000 satoshia** Suzien puolella.
- **Suzie** on kanavassa **Bobin** kanssa, jossa hänellä on **250 000 satoshia** ja Bobilla ei ole satosheja.

![LNP201](assets/en/37.webp)

Jos Alice haluaa lähettää varoja Bobille avaamatta suoraa kanavaa hänen kanssaan, hänen on mentävä Suzien kautta, ja jokaisen kanavan on säädettävä likviditeettiä kummallakin puolella. **Lähetetyt satoshit pysyvät omassa kanavassaan**; ne eivät todellisuudessa "yli" kanavia, mutta siirto tehdään säätämällä sisäistä likviditeettiä kussakin kanavassa.

Oletetaan, että Alice haluaa lähettää **50 000 satoshia** Bobille:

1. **Alice** lähettää 50 000 satoshia **Suzielle** heidän yhteisessä kanavassaan.
2. **Suzie** toistaa tämän siirron lähettämällä 50 000 satoshia **Bobille** heidän kanavassaan.

![LNP201](assets/en/38.webp)
Näin ollen maksu ohjataan Bobille liikuttamalla likviditeettiä kussakin kanavassa. Toimenpiteen lopussa Alicella on 50 000 satsia. Hän on todellakin siirtänyt 50 000 satsia, koska alun perin hänellä oli 100 000. Bob puolestaan päätyy 50 000 satsin lisäyksellä. Suzielle (välisolmulle) tämä toimenpide on neutraali: alun perin hänellä oli 30 000 satsia kanavassaan Alicen kanssa ja 250 000 satsia kanavassaan Bobin kanssa, yhteensä 280 000 satsia. Toimenpiteen jälkeen hänellä on 80 000 satsia kanavassaan Alicen kanssa ja 200 000 satsia kanavassaan Bobin kanssa, mikä on sama summa kuin alussa.
Tämä siirto on siis rajoitettu **käytettävissä olevan likviditeetin** mukaan siirron suunnassa.

### Reitin ja Likviditeetin Rajojen Laskeminen

Otetaan teoreettinen esimerkki toisesta verkosta, jossa on:

- **130 000 satoshia** Alicen puolella (oranssilla) hänen kanavassaan **Suzien** kanssa (harmaalla).
- **90 000 satoshia** **Suzien** puolella ja **200 000 satoshia** **Carolin** puolella (pinkillä).
- **150 000 satoshia** **Carolin** puolella ja **100 000 satoshia** **Bobin** puolella.

![LNP201](assets/en/39.webp)

Suurin summa, jonka Alice voi lähettää Bobille tässä konfiguraatiossa, on **90 000 satoshia**, koska hän on rajoitettu pienimmän likviditeetin mukaan kanavassa **Suzielta Carolille**. Vastakkaiseen suuntaan (Bobilta Alicelle) maksu ei ole mahdollinen, koska **Suzien** puolella kanavassa **Alicen** kanssa ei ole satosheja. Siksi **ei ole reittiä** käytettävissä siirrolle tässä suunnassa.
Alice lähettää **40 000 satoshia** Bobille kanavien kautta:

1. Alice siirtää 40 000 satoshia kanavaansa Suzien kanssa.
2. Suzie siirtää 40 000 satoshia Carolille heidän yhteisessä kanavassaan.
3. Carol lopulta siirtää 40 000 satoshia Bobille.

![LNP201](assets/en/40.webp)

**Lähetetyt satoshit** pysyvät kussakin kanavassa, joten Carolin Bobille lähettämät satoshit eivät ole samoja kuin Alicen Suzielle lähettämät. Siirto tehdään vain säätämällä likviditeettiä kussakin kanavassa. Lisäksi kanavien kokonaiskapasiteetti pysyy muuttumattomana.

![LNP201](assets/en/41.webp)

Kuten edellisessä esimerkissä, transaktion jälkeen lähtösolmu (Alice) on 40 000 satoshia vähemmän. Välisolmut (Suzie ja Carol) säilyttävät saman kokonaismäärän, mikä tekee toimenpiteestä neutraalin heille. Lopulta kohdesolmu (Bob) saa lisää 40 000 satoshia.

Välisolmujen rooli on siis erittäin tärkeä Lightning Networkin toiminnassa. Ne helpottavat siirtoja tarjoamalla useita polkuja maksuille. Kannustaakseen näitä solmuja tarjoamaan likviditeettiään ja osallistumaan maksujen reititykseen, **reitityspalkkiot** maksetaan heille.

### Reitityspalkkiot

Välisolmut soveltavat palkkioita salliakseen maksujen kulkemisen kanaviensa kautta. Nämä palkkiot asettaa **jokainen solmu kullekin kanavalleen**. Palkkiot koostuvat kahdesta osasta:

1. "**Peruspalkkio**": kiinteä määrä per kanava, usein oletuksena **1 sat**, mutta muokattavissa.
2. "**Muuttuva maksu**": siirretyn summan prosenttiosuus, laskettuna **miljoonasosina (ppm)**. Oletusarvoisesti se on **1 ppm** (1 sat miljoonaa siirrettyä satoshia kohden), mutta sitä voidaan myös säätää.
Maksut vaihtelevat myös siirron suunnan mukaan. Esimerkiksi siirrossa Alicelta Suzielle sovelletaan Alicen maksuja. Päinvastaisesti Suzielta Alicelle siirrettäessä käytetään Suzien maksuja.

Esimerkiksi kanavalla Alicen ja Suzien välillä meillä voisi olla:

- **Alice**: perusmaksu 1 sat ja 1 ppm muuttuvista maksuista.
- **Suzie**: perusmaksu 0.5 sat ja 10 ppm muuttuvista maksuista.

![LNP201](assets/en/42.webp)

Ymmärtääksemme paremmin, miten maksut toimivat, tutkitaan samaa Lightning Networkia kuin aiemmin, mutta nyt seuraavilla reititysmaksuilla:

- Kanava **Alice - Suzie**: perusmaksu 1 satoshi ja 1 ppm Alicelle.
- Kanava **Suzie - Carol**: perusmaksu 0 satoshia ja 200 ppm Suzielle.
- **Carol - Bob** Kanava: perusmaksu 1 satoshi ja 1 ppm Suzielle 2.
  ![LNP201](assets/en/43.webp)

Samasta **40,000 satoshin** maksusta Bobille, Alicen on lähetettävä hieman enemmän, koska jokainen välisolmu vähentää omat maksunsa:

- **Carol** vähentää 1.04 satoshia kanavalla Bobin kanssa:
  $$ f*{\text{Carol-Bob}} = \text{perusmaksu} + \left(\frac{\text{ppm} \times \text{määrä}}{10^6}\right) $$
  $$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ sats} $$

- **Suzie** vähentää 8 satoshia maksuina kanavalla Carolin kanssa:
  $$ f*{\text{Suzie-Carol}} = \text{perusmaksu} + \left(\frac{\text{ppm} \times \text{määrä}}{10^6}\right) $$
  $$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ sats} $$

Tämän maksun kokonaismaksut tällä reitillä ovat siis **9.04 satoshia**. Näin ollen Alicen on lähetettävä **40,009.04 satoshia**, jotta Bob saa tarkalleen **40,000 satoshia**.

![LNP201](assets/en/44.webp)

Nesteytys päivittyy siis:

![LNP201](assets/en/45.webp)

### Sipulireititys

Maksun reitittämiseksi lähettäjältä vastaanottajalle Lightning Network käyttää menetelmää, jota kutsutaan "**sipulireititykseksi**". Toisin kuin klassisen datan reitityksessä, jossa jokainen reititin päättää datan suunnan perustuen niiden määränpäähän, sipulireititys toimii eri tavalla:

- **Lähettävä solmu laskee koko reitin**: Alice esimerkiksi määrittää, että hänen maksunsa on kuljettava Suzien ja Carolin kautta ennen kuin se saavuttaa Bobin.
- **Jokainen välisolmu tuntee vain välittömän naapurinsa**: Suzie tietää vain, että hän sai varoja Alicelta ja että hänen täytyy siirtää ne Carolille. Suzie ei kuitenkaan tiedä, onko Alice lähdesolmu vai välisolmu, eikä hän myöskään tiedä, onko Carol vastaanottajasolmu vai vain toinen välisolmu. Tämä periaate pätee myös Caroliin ja kaikkiin muihin polun solmuihin. Sipulireititys näin ollen säilyttää tapahtumien luottamuksellisuuden peittämällä lähettäjän ja lopullisen vastaanottajan identiteetin. Jotta lähettävä solmu voi laskea täydellisen reitin vastaanottajalle sipulireitityksessä, sen on ylläpidettävä **verkkograafia** tietääkseen sen topologian ja määrittääkseen mahdolliset reitit.
  **Mitä sinun tulisi oppia tästä luvusta?**

1. Lightning-verkossa maksut voidaan reitittää solmujen välillä epäsuorasti välisolmukanavien kautta. Jokainen näistä välisolmuista helpottaa likviditeetin välitystä.
2. Välisolmut saavat palvelustaan komission, joka koostuu kiinteistä ja muuttuvista maksuista.
3. Sipulireititys mahdollistaa lähettävän solmun laskea täydellisen reitin ilman, että välisolmut tietävät lähteen tai lopullisen määränpään.

Tässä luvussa tutkimme maksujen reititystä Lightning-verkossa. Mutta herää kysymys: mikä estää välisolmuja hyväksymästä tulevaa maksua ilman, että se välittää sen seuraavaan määränpäähän, tavoitteenaan kaapata transaktio? Tämä on juuri HTLC:iden rooli, joita tutkimme seuraavassa luvussa.

## HTLC – Hashed Time Locked Contract

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

![HTLC](https://youtu.be/-JC4mkq7H48)

Tässä luvussa tutustumme siihen, miten Lightning mahdollistaa maksujen siirtymisen välisolmujen kautta ilman, että niitä tarvitsee luottaa, kiitos **HTLC** (_Hashed Time-Locked Contracts_) -älykkäiden sopimusten. Nämä älykkäät sopimukset varmistavat, että jokainen välisolmu saa varat kanavastaan vain, jos se välittää maksun lopulliselle vastaanottajalle, muuten maksua ei vahvisteta.

Maksujen reitityksessä esiin nouseva ongelma on siis tarvittava luottamus välisolmuihin ja välisolmujen keskinäinen luottamus. Havainnollistaaksemme tätä, palatkaamme yksinkertaistettuun Lightning-verkon esimerkkiimme, jossa on 3 solmua ja 2 kanavaa:

- Alicella on kanava Suzien kanssa.
- Suziella on kanava Bobin kanssa.

Alice haluaa lähettää 40 000 satsia Bobille, mutta hänellä ei ole suoraa kanavaa hänen kanssaan eikä hän halua avata sellaista. Hän etsii reittiä ja päättää mennä Suzien solmun kautta.

![LNP201](assets/en/46.webp)

Jos Alice naiivisti lähettää 40 000 satoshia Suzielle toivoen, että Suzie siirtäisi tämän summan Bobille, Suzie voisi pitää varat itsellään eikä siirtää mitään Bobille.

![LNP201](assets/en/47.webp)
Välttääkseen tämän tilanteen Lightning-verkossa käytämme HTLC:itä (Hashed Time-Locked Contracts), jotka tekevät maksun välisolmulle ehdolliseksi, mikä tarkoittaa, että Suzien on täytettävä tietyt ehdot päästäkseen käsiksi Alicen varoihin ja siirtääkseen ne Bobille.

### Miten HTLC:t Toimivat

HTLC on erityinen sopimus, joka perustuu kahteen periaatteeseen:

- **Pääsyn ehto**: Vastaanottajan on paljastettava salaisuus avatakseen heille kuuluvan maksun.
- **Vanhentuminen**: Jos maksua ei suoriteta kokonaan määritellyssä ajassa, se peruutetaan, ja varat palautuvat lähettäjälle.

Tässä on, miten tämä prosessi toimii esimerkissämme Alicen, Suzien ja Bobin kanssa:

![LNP201](assets/en/48.webp)
**Salaisuuden luominen**: Bob luo satunnaisen salaisuuden, jota merkitään _s_ (esikuva), ja laskee sen hajautusarvon, jota merkitään _r_, käyttäen hajautusfunktiota, jota merkitään _h_. Meillä on:
$$
r = h(s)
$$

Hajautusfunktion käyttö tekee mahdottomaksi löytää _s_ pelkästään _h(s)_ avulla, mutta jos _s_ annetaan, on helppo varmistaa, että se vastaa _h(s)_.

![LNP201](assets/en/49.webp)

**Maksupyynnön lähettäminen**: Bob lähettää **laskun** Alicelle pyytäen maksua. Tämä lasku sisältää erityisesti hajautusarvon _r_.

![LNP201](assets/en/50.webp)

**Ehdollisen maksun lähettäminen**: Alice lähettää HTLC:n, joka on 40 000 satoshia, Suzielle. Ehto Suzien saada nämä varat on, että hän toimittaa Alicelle salaisuuden _s'_, joka täyttää seuraavan yhtälön:

$$
h(s') = r
$$

![LNP201](assets/en/51.webp)

**HTLC:n siirtäminen lopulliselle vastaanottajalle**: Suzien, saadakseen 40 000 satoshia Alicelta, täytyy siirtää vastaava HTLC, joka on 40 000 satoshia, Bobille, jolla on sama ehto, nimittäin että hänen täytyy toimittaa Suzielle salaisuus _s'_, joka täyttää yhtälön:

$$
h(s') = r
$$

![LNP201](assets/en/52.webp)

**Vahvistus salaisuudella _s_**: Bob toimittaa _s_:n Suzielle saadakseen luvatut 40 000 satoshia HTLC:ssä. Tällä salaisuudella Suzie voi sitten avata Alicen HTLC:n ja saada 40 000 satoshia Alicelta. Maksu on sitten oikein ohjattu Bobille.

![LNP201](assets/en/53.webp)
Tämä prosessi estää Suzieta pitämästä Alicen varoja suorittamatta siirtoa Bobille, koska hänen täytyy lähettää maksu Bobille saadakseen salaisuuden _s_ ja siten avata Alicen HTLC. Toiminta pysyy samana, vaikka reitti sisältäisi useita välityssolmuja: kyse on vain Suzien toimien toistamisesta kullekin välityssolmulle. Jokainen solmu on suojattu HTLC:iden ehdoilla, koska viimeisen HTLC:n avaaminen vastaanottajan toimesta automaattisesti laukaisee kaikkien muiden HTLC:iden avaamisen kaskadina.

### HTLC:ien vanhentuminen ja hallinta ongelmatilanteissa

Jos maksuprosessin aikana jokin välityssolmuista tai vastaanottajasolmu lopettaa vastaamisen, erityisesti internet- tai sähkökatkoksen yhteydessä, maksua ei voida suorittaa loppuun, koska tarvittavaa salaisuutta HTLC:ien avaamiseen ei välitetä. Ottaen esimerkkimme Alicen, Suzien ja Bobin kanssa, tämä ongelma ilmenee esimerkiksi, jos Bob ei välitä salaisuutta _s_ Suzielle. Tässä tapauksessa kaikki reitin yläpuolella olevat HTLC:t ovat jumissa, ja myös niiden turvaamat varat.

![LNP201](assets/en/54.webp)

Välttääkseen tämän, Lightningin HTLC:illä on vanhentumisaika, joka mahdollistaa HTLC:n poistamisen, jos sitä ei ole suoritettu loppuun tietyn ajan kuluttua. Vanhentumisen järjestys on tietty, koska se alkaa ensin HTLC:stä, joka on lähimpänä vastaanottajaa, ja siirtyy sitten asteittain takaisin tapahtuman lähettäjälle. Esimerkissämme, jos Bob ei koskaan anna salaisuutta _s_ Suzielle, tämä aiheuttaisi ensin Suzien HTLC:n Bobille vanhentumaan.

![LNP201](assets/en/55.webp)

Sitten HTLC Alicelta Suzielle.
Jos erääntymisjärjestys olisi käännetty, Alice voisi palauttaa maksunsa ennen kuin Suzie ehtisi suojautua mahdolliselta huijaukselta. Todellakin, jos Bob palaa vaatimaan HTLC:tään samalla kun Alice on jo poistanut omansa, Suzie olisi epäedullisessa asemassa. Tämä HTLC:iden kaskadoituva erääntymisjärjestys varmistaa siis, että yksikään välittäjäsolmu ei kärsi epäreiluista tappioista.

### HTLC:iden esitys sitoumustapahtumissa

Sitoumustapahtumat esittävät HTLC:t tavalla, joka mahdollistaa niiden asettamien ehtojen siirtämisen Bitcoinille pakotetun kanavan sulkemisen yhteydessä HTLC:n elinaikana. Muistutuksena, sitoumustapahtumat edustavat kanavan nykyistä tilaa kahden käyttäjän välillä ja mahdollistavat yksipuolisen pakotetun sulkemisen ongelmatilanteissa. Jokaisen kanavan uuden tilan myötä luodaan 2 sitoumustapahtumaa: yksi kummallekin osapuolelle. Palatkaamme esimerkkiimme Alicen, Suzien ja Bobin kanssa, mutta tarkastellaan tarkemmin, mitä tapahtuu kanavatasolla Alicen ja Suzien välillä, kun HTLC luodaan.

Ennen 40 000 satoshin maksun aloittamista Alicen ja Bobin välillä, Alicella on 100 000 satoshia kanavassaan Suzien kanssa, kun taas Suziella on 30 000. Heidän sitoumustapahtumansa ovat seuraavat:

Alice on juuri saanut Bobin laskun, joka sisältää merkittävästi _r_:n, salaisuuden hashin. Hän voi siis rakentaa 40 000 satoshin HTLC:n Suzien kanssa. Tämä HTLC esitetään viimeisimmissä sitoumustapahtumissa lähtökohtana nimeltä "**_HTLC Out_**" Alicen puolella, koska varat ovat lähteviä, ja "**_HTLC In_**" Suzien puolella, koska varat ovat saapuvia.

Nämä HTLC:hen liittyvät lähdöt jakavat täsmälleen samat ehdot, nimittäin:

- Jos Suzie pystyy tarjoamaan salaisuuden _s_, hän voi avata tämän lähdön välittömästi ja siirtää sen hallitsemaansa osoitteeseen.
- Jos Suzie ei omista salaisuutta _s_, hän ei voi avata tätä lähtöä, ja Alice pystyy avaamaan sen ajastimen jälkeen lähettääkseen sen hallitsemaansa osoitteeseen. Ajastin antaa siis Suzielle aikaa reagoida, jos hän saa _s_:n.

Nämä ehdot pätevät vain, jos kanava suljetaan (eli sitoumustapahtuma julkaistaan ketjussa) samalla kun HTLC on edelleen aktiivinen Lightningissa, mikä tarkoittaa, että maksu Alicen ja Bobin välillä ei ole vielä valmistunut, ja HTLC:t eivät ole vielä vanhentuneet. Kiitos näiden ehtojen, Suzie voi palauttaa 40 000 satoshia HTLC:stä, joka hänelle kuuluu tarjoamalla _s_. Muussa tapauksessa Alice saa varat takaisin ajastimen vanhentumisen jälkeen, koska jos Suzie ei tiedä _s_:ää, se tarkoittaa, että hän ei ole siirtänyt 40 000 satoshia Bobille, ja siksi Alicen varat eivät ole hänelle velkaa.

Lisäksi, jos kanava suljetaan samalla kun useita HTLC:itä on odottamassa, luodaan yhtä monta lisälähtöä kuin käynnissä olevia HTLC:itä on.
Jos kanavaa ei suljeta, niin Lightning-maksun vanhentumisen tai onnistumisen jälkeen luodaan uudet sitoumustapahtumat heijastamaan kanavan uutta, nyt vakaata tilaa, eli ilman odottavia HTLC:itä. HTLC:iin liittyvät lähdöt voidaan siis poistaa sitoumustapahtumista.
Lopulta, jos yhteistyössä tapahtuvan kanavan sulkemisen aikana HTLC on aktiivinen, Alice ja Suzie lopettavat uusien maksujen hyväksymisen ja odottavat meneillään olevien HTLC:iden ratkaisua tai vanhentumista. Tämä mahdollistaa heidän julkaista kevyemmän sulkemistransaktion, ilman HTLC:iin liittyviä ulostuloja, vähentäen näin maksuja ja välttäen mahdollisen aikalukon odottamisen.
**Mitä sinun tulisi oppia tästä luvusta?**

HTLC:t mahdollistavat Lightning-maksujen reitittämisen useiden solmujen kautta ilman, että niitä tarvitsee luottaa. Tässä ovat keskeiset muistettavat asiat:

1. HTLC:t takaavat maksujen turvallisuuden salaisuuden (preimage) ja vanhentumisajan kautta.
2. HTLC:iden ratkaisu tai vanhentuminen noudattaa tiettyä järjestystä: sitten määränpäästä lähteeseen, jotta jokainen solmu suojataan.
3. Niin kauan kuin HTLC:tä ei ole ratkaistu eikä se ole vanhentunut, se säilytetään ulostulona viimeisimmissä sitoumustapahtumissa.

Seuraavassa luvussa tutustumme siihen, miten solmu, joka lähettää Lightning-transaktion, löytää ja valitsee reitit maksunsa toimittamiseksi vastaanottavalle solmulle.

## Löytämäsi Tie

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

![finding your way](https://youtu.be/wnUGJjOxd9Q)

Edellisissä luvuissa näimme, miten käyttää muiden solmujen kanavia maksujen reitittämiseen ja tavoittamaan solmun ilman, että on suoraan yhdistetty siihen kanavan kautta. Keskustelimme myös siitä, miten varmistetaan siirron turvallisuus luottamatta välittäjiin. Tässä luvussa keskitymme parhaan mahdollisen reitin löytämiseen kohdesolmuun.

### Reititysongelma Lightning-verkossa

Kuten olemme nähneet, Lightning-verkossa maksua lähettävän solmun on laskettava koko reitti vastaanottajalle, koska käytämme sipulireititysjärjestelmää. Välisolmut eivät tiedä lähtöpistettä tai lopullista määränpäätä. Ne tietävät vain, mistä maksu tulee ja mihin solmuun ne siirtävät sen seuraavaksi. Tämä tarkoittaa, että lähettävän solmun on ylläpidettävä dynaamista paikallista topologiaa verkosta, olemassa olevista Lightning-solmuista ja niiden välisistä kanavista, ottaen huomioon avaukset, sulkemiset ja tilapäivitykset.

![LNP201](assets/en/61.webp)
Vaikka meillä on tämä Lightning-verkon topologia, reitityksen kannalta olennaista tietoa jää lähettävälle solmulle saavuttamattomiin, mikä on kanavien tarkka likviditeetin jakautuminen missä tahansa hetkessä. Itse asiassa, jokainen kanava näyttää vain **kokonaiskapasiteettinsa**, mutta rahojen sisäinen jakautuminen on vain kahden osallistuvan solmun tiedossa. Tämä aiheuttaa haasteita tehokkaalle reititykselle, sillä maksun onnistuminen riippuu erityisesti siitä, onko sen summa pienempi kuin valitun reitin pienin likviditeetti. Kuitenkaan likviditeetit eivät ole kaikki lähettävän solmun nähtävillä.
![LNP201](assets/en/62.webp)

### Verkkokartan Päivitys

Pitääkseen verkkokarttansa ajan tasalla, solmut vaihtavat säännöllisesti viestejä algoritmin kautta, jota kutsutaan "**_juoruiluksi_**". Tämä on hajautettu algoritmi, jota käytetään tiedon leviämiseen epidemian tavoin kaikkiin verkon solmuihin, mikä mahdollistaa kanavien globaalin tilan vaihdon ja synkronoinnin muutamassa viestintäsyklissä. Jokainen solmu välittää tietoa yhdelle tai useammalle satunnaisesti tai ei satunnaisesti valitulle naapurille, jotka puolestaan välittävät tiedon muille naapureille ja niin edelleen, kunnes globaalisti synkronoitu tila saavutetaan.

Kaksi pääviestiä, joita Lightning-solmut vaihtavat, ovat seuraavat:

- "**Kanavailmoitukset**": viestit, jotka ilmoittavat uuden kanavan avaamisesta.
- "**Kanavapäivitykset**": päivitysviestejä kanavan tilasta, erityisesti maksujen kehityksestä (mutta ei likviditeetin jakautumisesta).
Lightning-solmut myös seuraavat Bitcoin-lohkoketjua havaitakseen kanavan sulkemistransaktiot. Suljettu kanava poistetaan sitten kartasta, koska sitä ei enää voida käyttää maksujemme reitittämiseen.

### Maksun Reititys

Otetaan esimerkki pienestä Lightning Networkista, jossa on 7 solmua: Alice, Bob, 1, 2, 3, 4 ja 5. Kuvitellaan, että Alice haluaa lähettää maksun Bobille, mutta sen on kuljettava välisolmujen kautta.

![LNP201](assets/en/63.webp)

Tässä on varojen todellinen jakautuminen näissä kanavissa:

- **Kanava Alicen ja 1 välillä**: 250 000 satsia Alicen puolella, 80 000 1:n puolella (kokonaiskapasiteetti 330 000 satsia).
- **Kanava 1:n ja 2:n välillä**: 300 000 satsia 1:n puolella, 200 000 2:n puolella (kokonaiskapasiteetti 500 000 satsia).
- **Kanava 2:n ja 3:n välillä**: 50 000 satsia 2:n puolella, 60 000 3:n puolella (kokonaiskapasiteetti 110 000 satsia).
- **Kanava 2:n ja 5:n välillä**: 90 000 satsia 2:n puolella, 160 000 5:n puolella (kokonaiskapasiteetti 250 000 satsia).
- **Kanava 2:n ja 4:n välillä**: 180 000 satsia 2:n puolella, 110 000 4:n puolella (kokonaiskapasiteetti 290 000 satsia).
- **Kanava 4:n ja 5:n välillä**: 200 000 satsia 4:n puolella, 10 000 5:n puolella (kokonaiskapasiteetti 210 000 satsia).
- **Kanava 3:n ja Bobin välillä**: 50 000 satsia 3:n puolella, 250 000 Bobin puolella (kokonaiskapasiteetti 300 000 satsia).
- **Kanava 5:n ja Bobin välillä**: 260 000 satsia 5:n puolella, 100 000 Bobin puolella (kokonaiskapasiteetti 360 000 satsia).

![LNP201](assets/en/64.webp)

Jotta Alice voisi tehdä 100 000 satsin maksun Bobille, reititysvaihtoehdot ovat rajoitettuja kunkin kanavan käytettävissä olevan likviditeetin mukaan. Alicen kannalta optimaalinen reitti, tunnetun likviditeetin jakautumisen perusteella, voisi olla järjestys `Alice → 1 → 2 → 4 → 5 → Bob`:

![LNP201](assets/en/65.webp)

Koska Alice ei kuitenkaan tiedä tarkkaa varojen jakautumista kussakin kanavassa, hänen on arvioitava optimaalinen reitti todennäköisyyden perusteella ottaen huomioon seuraavat kriteerit:

- **Onnistumisen todennäköisyys**: kanavalla, jolla on suurempi kokonaiskapasiteetti, on todennäköisemmin riittävästi likviditeettiä. Esimerkiksi solmun 2 ja solmun 3 välisellä kanavalla on kokonaiskapasiteetti 110 000 satsia, joten on epätodennäköistä löytää 100 000 satsia tai enemmän solmun 2 puolelta, vaikka se onkin mahdollista.
- **Siirtomaksut**: parasta reittiä valitessaan lähettävä solmu ottaa myös huomioon kunkin välisolmun soveltamat maksut ja pyrkii minimoimaan kokonaisreitityskustannukset.
- **HTLC:ien vanheneminen**: estääkseen maksujen jumiutumisen, myös HTLC:ien vanhenemisaika on huomioitava parametri.
- **Välisolmujen määrä**: lopulta, laajemmin ottaen, lähetysolmu pyrkii löytämään reitin, jossa on mahdollisimman vähän solmuja, vähentääkseen vikojen riskiä ja rajoittaakseen Lightning-siirtomaksuja.
Näitä kriteereitä analysoimalla lähetysolmu voi testata todennäköisimpiä reittejä ja yrittää optimoida niitä. Esimerkissämme Alice voisi arvottaa parhaat reitit seuraavasti:

1. `Alice → 1 → 2 → 5 → Bob`, koska se on lyhin reitti suurimmalla kapasiteetilla.
2. `Alice → 1 → 2 → 4 → 5 → Bob`, koska tämä reitti tarjoaa hyvät kapasiteetit, vaikkakin se on pidempi kuin ensimmäinen.
3. `Alice → 1 → 2 → 3 → Bob`, koska tämä reitti sisältää kanavan `2 → 3`, jolla on hyvin rajoitettu kapasiteetti, mutta on silti mahdollisesti käyttökelpoinen.

### Maksun suoritus

Alice päättää testata ensimmäistä reittiään (`Alice → 1 → 2 → 5 → Bob`). Hän siis lähettää 100 000 satoshin HTLC:n solmulle 1. Tämä solmu tarkistaa, että sillä on riittävästi likviditeettiä solmun 2 kanssa, ja jatkaa siirtoa. Solmu 2 sitten vastaanottaa HTLC:n solmulta 1, mutta huomaa, ettei sillä ole tarpeeksi likviditeettiä kanavassaan solmun 5 kanssa siirtääkseen 100 000 satoshin maksun. Se lähettää virheviestin takaisin solmulle 1, joka välittää sen Alicelle. Tämä reitti epäonnistui.

![LNP201](assets/en/66.webp)

Alice yrittää sitten reitittää maksunsa käyttäen toista reittiään (`Alice → 1 → 2 → 4 → 5 → Bob`). Hän lähettää 100 000 satoshin HTLC:n solmulle 1, joka välittää sen solmulle 2, sitten solmulle 4, solmulle 5 ja lopulta Bobille. Tällä kertaa likviditeetti on riittävä, ja reitti toimii. Jokainen solmu avaa HTLC:nsä kaskadina käyttäen Bobin antamaa esikuvaa (salaisuus _s_), mikä mahdollistaa Alicen maksun Bobille onnistuneesti.

![LNP201](assets/en/67.webp)

Reitin etsintä tapahtuu seuraavasti: lähetysolmu aloittaa tunnistamalla parhaat mahdolliset reitit, sitten yrittää maksuja peräkkäin, kunnes toimiva reitti löytyy.

On huomionarvoista, että Bob voi antaa Alicelle tietoja **laskussa** helpottaakseen reititystä. Esimerkiksi hän voi ilmoittaa lähellä olevista kanavista, joilla on riittävästi likviditeettiä tai paljastaa yksityisten kanavien olemassaolon. Nämä vihjeet auttavat Alicea välttämään reittejä, joilla on vähän onnistumisen mahdollisuuksia, ja ensin yrittämään Bobin suosittelemia polkuja.

**Mitä sinun tulisi ottaa tästä luvusta mukaasi?**

1. Solmut ylläpitävät karttaa verkon topologiasta ilmoitusten kautta ja seuraamalla kanavien sulkemisia Bitcoin-lohkoketjussa.
2. Optimaalisen reitin etsintä maksulle on todennäköisyyspohjaista ja riippuu monista kriteereistä.
3. Bob voi antaa vihjeitä **laskussa** ohjatakseen Alicen reititystä ja säästääkseen häntä testaamasta epätodennäköisiä reittejä.

Seuraavassa luvussa tutkimme erityisesti laskujen toimintaa, lisäksi joitakin muita Lightning-verkon käyttämiä työkaluja.

# Lightning-verkon työkalut

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Lasku, LNURL ja Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>
![lasku, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)
Tässä luvussa tarkastelemme tarkemmin Lightning **laskujen** toimintaa, eli maksupyyntöjä, jotka vastaanottava solmu lähettää lähettävälle solmulle. Tavoitteena on ymmärtää, miten maksuja suoritetaan ja vastaanotetaan Lightning-verkossa. Keskustelemme myös kahdesta klassisten laskujen vaihtoehdosta: LNURL ja Keysend.
![LNP201](assets/en/68.webp)

### Lightning-laskujen rakenne

Kuten HTLC-luvussa selitettiin, jokainen maksu alkaa **laskun** luomisella vastaanottajan toimesta. Tämä lasku välitetään sitten maksajalle (QR-koodin tai kopioimalla ja liittämällä) maksun aloittamiseksi. Lasku koostuu kahdesta pääosasta:

1. **Ihmislukukelpoinen osa**: tämä osio sisältää selvästi näkyvää metadataa käyttökokemuksen parantamiseksi.
2. **Tietosisältö**: tämä osio sisältää koneiden käsiteltäväksi tarkoitettua tietoa maksun suorittamiseksi.

Tyypillisen laskun rakenne alkaa tunnisteella `ln` "Lightning" varten, jonka jälkeen tulee `bc` Bitcoinille, sitten laskun summa. Erotin `1` erottaa ihmislukukelpoisen osan tietosisällöstä (payload).

Otetaan esimerkiksi seuraava lasku:

```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Voimme jo jakaa sen kahteen osaan. Ensin on ihmislukukelpoinen osa:

```invoice
lnbc100u
```

Sitten tietosisältöä varten tarkoitettu osa:

```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```
Kaksi osaa on erotettu toisistaan `1`:llä. Tämä erotin valittiin erikoismerkin sijaan, jotta koko laskun kopioiminen kaksoisklikkaamalla olisi helppoa.
Ensimmäisessä osassa voimme nähdä, että:

- `ln` osoittaa, että kyseessä on Lightning-siirto.
- `bc` osoittaa, että Lightning-verkko on Bitcoin-lohkoketjussa (eikä testnetissä tai Litecoinissa).
- `100u` osoittaa laskun määrän, joka ilmaistaan **mikrosatosheina** (`u` tarkoittaa "mikro"), mikä tässä tapauksessa vastaa 10 000 satia.

Maksun määrä ilmaistaan bitcoinin alayksiköissä. Tässä käytetyt yksiköt:

- **Millibitcoin (merkitty `m`):** Edustaa yhtä tuhannesosaa bitcoinista.

  $$
  1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satosheja}
  $$

- **Mikrobitcoin (merkitty `u`):** Joskus kutsutaan myös "bitiksi", edustaa yhtä miljoonasosaa bitcoinista.

  $$
  1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satosheja}
  $$

- **Nanobitcoin (merkitty `n`):** Edustaa yhtä miljardisosaa bitcoinista.

  $$
  1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satosheja}
  $$

- **Pikobitcoin (merkitty `p`):** Edustaa yhtä biljoonasosaa bitcoinista.
  $$
  1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satosheja}
  $$

### Laskun Sisältö

Laskun sisältö käsittää useita maksun käsittelyyn tarvittavia tietoja:

- **Aikaleima:** Laskun luomishetki, ilmaistuna Unix-aikaleimana (sekuntien määrä, joka on kulunut tammikuun 1. päivästä 1970).
- **Salaisuuden Hahmontaminen**: Kuten HTLC-osiossa näimme, vastaanottavan solmun on annettava lähettävälle solmulle esikuvan hahmo. Tätä käytetään HTLC:ssä siirron turvaamiseen. Viittasimme siihen "_r_"-koodilla.
- **Maksusalaisuus**: Vastaanottaja luo toisen salaisuuden, mutta tällä kertaa se lähetetään lähettävälle solmulle. Sitä käytetään sipulireitityksessä estämään välisolmuja arvaamasta, onko seuraava solmu lopullinen vastaanottaja vai ei. Tämä ylläpitää vastaanottajan luottamuksellisuutta viimeisen välisolmun suhteen reitillä.
- **Vastaanottajan Julkinen Avain**: Ilmoittaa maksajalle maksettavan henkilön tunnisteen.
- **Vanhentumisaika**: Maksimiaika laskun maksamiselle (oletuksena 1 tunti).
- **Reititysvihjeet**: Vastaanottajan antama lisätieto, joka auttaa lähettäjää optimoimaan maksureitin.
- **Allekirjoitus**: Takaa laskun eheyden vahvistamalla kaikki tiedot.

Laskut koodataan sitten **bech32**-muotoon, samaan tapaan kuin Bitcoin SegWit -osoitteet (muoto alkaa `bc1`).

### LNURL Kotiutus
Perinteisessä transaktiossa, kuten kaupassa tehtävässä ostoksessa, lasku luodaan maksettavaksi tulevalle kokonaissummalle. Kun lasku esitetään (QR-koodin tai merkkijonon muodossa), asiakas voi skannata sen ja viimeistellä transaktion. Maksu noudattaa sitten perinteistä prosessia, jota tutkimme edellisessä osiossa. Tämä prosessi voi kuitenkin joskus olla hyvin hankala käyttäjäkokemuksen kannalta, koska se vaatii vastaanottajalta tiedon lähettämistä lähettäjälle laskun kautta.

Tietyissä tilanteissa, kuten bitcoineja nostettaessa online-palvelusta, perinteinen prosessi on liian hankala. Tällaisissa tapauksissa **LNURL**-nostoratkaisu yksinkertaistaa tätä prosessia näyttämällä QR-koodin, jonka vastaanottajan lompakko skannaa automaattisesti luodakseen laskun. Palvelu maksaa sitten laskun, ja käyttäjä näkee vain välittömän noston.

![LNP201](assets/en/69.webp)

LNURL on viestintäprotokolla, joka määrittelee joukon toiminnallisuuksia, jotka on suunniteltu yksinkertaistamaan vuorovaikutusta Lightning-nodien ja asiakkaiden sekä kolmansien osapuolten sovellusten välillä. LNURL-nosto, kuten juuri näimme, on siis vain yksi esimerkki muiden toiminnallisuuksien joukossa.
Tämä protokolla perustuu HTTP:hen ja mahdollistaa linkkien luomisen erilaisiin toimintoihin, kuten maksupyynnön, nostopyynnön tai muiden toiminnallisuuksien, jotka parantavat käyttäjäkokemusta. Jokainen LNURL on bech32-koodattu URL, jossa on lnurl-etuliite, joka skannattaessa laukaisee sarjan automaattisia toimintoja Lightning-lompakossa.
Esimerkiksi LNURL-withdraw (LUD-03) -ominaisuus mahdollistaa varojen nostamisen palvelusta skannaamalla QR-koodin, ilman että laskua tarvitsee luoda manuaalisesti. Samoin LNURL-auth (LUD-04) mahdollistaa online-palveluihin kirjautumisen käyttämällä yksityistä avainta Lightning-lompakossa salasanan sijaan.

### Lightning-maksun lähettäminen ilman laskua: Keysend

Toinen mielenkiintoinen tapaus on varojen siirto ilman etukäteen saatuja laskuja, tunnetaan nimellä "**Keysend**". Tämä protokolla mahdollistaa varojen lähettämisen lisäämällä esikuvan salattuun maksutietoon, joka on vain vastaanottajan saatavilla. Tämä esikuva mahdollistaa vastaanottajan HTLC:n avaamisen, jolloin hän voi hakea varat ilman, että laskua on etukäteen luotu.

Yksinkertaistaen, tässä protokollassa lähettäjä luo salaisuuden, jota käytetään HTLC:ssä, eikä vastaanottaja. Käytännössä tämä mahdollistaa lähettäjän suorittaa maksun ilman, että on tarvinnut olla yhteydessä vastaanottajaan etukäteen.

![LNP201](assets/en/70.webp)

**Mitä sinun tulisi ottaa mukaasi tästä luvusta?**

1. **Lightning-lasku** on maksupyyntö, joka koostuu ihmisen luettavasta osasta ja koneen datan osasta.
2. Lasku on koodattu **bech32**:lla, jossa on `1` erotin kopioinnin helpottamiseksi ja datan osa, joka sisältää kaikki maksun käsittelyyn tarvittavat tiedot.
3. Lightningissa on olemassa muita maksuprosesseja, erityisesti **LNURL-Withdraw** nostojen helpottamiseksi, ja **Keysend** suorille siirroille ilman laskua.

Seuraavassa luvussa näemme, kuinka solmuoperaattori voi hallita likviditeettiä kanavissaan, jotta ei koskaan jää jumiin ja voi aina lähettää ja vastaanottaa maksuja Lightning-verkossa.

## Likviditeettisi Hallinta

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

![likviditeettisi hallinta](https://youtu.be/YuPrbhEJXbg)

Tässä luvussa tutkimme strategioita tehokkaaseen likviditeetin hallintaan Lightning-verkossa. Likviditeetin hallinta vaihtelee käyttäjätyypin ja kontekstin mukaan. Käymme läpi pääperiaatteet ja olemassa olevat tekniikat ymmärtääksemme paremmin, kuinka optimoida tämä hallinta.

### Likviditeettitarpeet
Lightning-verkossa on kolme pääkäyttäjäprofiilia, joilla kullakin on erityiset likviditeettitarpeet:
1. **Maksaja**: Tämä on henkilö, joka suorittaa maksuja. He tarvitsevat lähtevää likviditeettiä voidakseen siirtää varoja muille käyttäjille. Esimerkiksi tämä voisi olla kuluttaja.
2. **Myyjä (tai Saaja)**: Tämä on henkilö, joka vastaanottaa maksuja. He tarvitsevat saapuvaa likviditeettiä voidakseen hyväksyä maksuja omaan solmuunsa. Esimerkiksi tämä voisi olla yritys tai verkkokauppa.
3. **Reititin**: Välisolmu, joka on usein erikoistunut maksujen reitittämiseen, ja jonka on optimoitava likviditeettinsä kussakin kanavassa voidakseen reitittää mahdollisimman monta maksua ja ansaita palkkioita.

Nämä profiilit eivät tietenkään ole kiinteitä; käyttäjä voi vaihtaa maksajan ja saajan roolien välillä riippuen transaktioista. Esimerkiksi Bob voisi vastaanottaa palkkansa Lightning-verkossa työnantajaltaan, mikä asettaisi hänet "myyjän" asemaan tarviten saapuvaa likviditeettiä. Myöhemmin, jos hän haluaa käyttää palkkaansa ruoan ostamiseen, hänestä tulee "maksaja" ja hänen on silloin oltava lähtevää likviditeettiä.

Ymmärtääksemme paremmin, otetaan esimerkki yksinkertaisesta verkosta, joka koostuu kolmesta solmusta: ostaja (Alice), reititin (Suzie) ja myyjä (Bob).

![LNP201](assets/en/71.webp)

Kuvittele, että ostaja haluaa lähettää 30 000 satoshia myyjälle ja että maksu kulkee reitittimen solmun kautta. Jokaisella osapuolella on silloin oltava vähimmäismäärä likviditeettiä maksun suuntaan:

- Maksajan on oltava vähintään 30 000 satoshia heidän puolellaan kanavassa reitittimen kanssa.
- Myyjällä on oltava kanava, jossa 30 000 satoshia on vastakkaisella puolella voidakseen vastaanottaa ne.
- Reitittimellä on oltava 30 000 satoshia maksajan puolella heidän kanavassaan, ja myös 30 000 satoshia heidän puolellaan kanavassa myyjän kanssa, jotta se voi reitittää maksun.

![LNP201](assets/en/72.webp)

### Likviditeetinhallintastrategiat

Maksajien on varmistettava riittävä likviditeetti kanaviensa puolella taatakseen lähtevän likviditeetin. Tämä osoittautuu suhteellisen yksinkertaiseksi, sillä uusien Lightning-kanavien avaaminen riittää tähän likviditeettiin. Itse asiassa alussa multisig-sopimuksessa lukitut varat ovat kokonaan maksajan puolella Lightning-kanavassa. Maksukyky on siis taattu niin kauan kuin kanavia avataan tarpeeksi varoilla. Kun lähtevä likviditeetti on käytetty, riittää uusien kanavien avaaminen.
Toisaalta myyjälle tehtävä on monimutkaisempi. Jotta he voivat vastaanottaa maksuja, heidän on oltava likviditeettiä kanaviensa vastakkaisella puolella. Siksi pelkkä kanavan avaaminen ei riitä: heidän on myös suoritettava maksu tässä kanavassa siirtääkseen likviditeetin toiselle puolelle ennen kuin he voivat itse vastaanottaa maksuja. Tietyille Lightning-käyttäjäprofiileille, kuten kauppiaille, on selvä epäsuhta sen välillä, mitä heidän solmunsa lähettää ja mitä se vastaanottaa, koska liiketoiminnan tavoitteena on pääasiassa kerätä enemmän kuin se kuluttaa, jotta se voi tuottaa voittoa. Onneksi näille käyttäjille, joilla on erityisiä saapuvan likviditeetin tarpeita, on olemassa useita ratkaisuja:

- **Kanavien houkuttelu**: Kauppias hyötyy edusta johtuen odotetusta saapuvien maksujen määrästä heidän solmussaan. Ottaen tämän huomioon, he voivat yrittää houkutella reitityssolmuja, jotka etsivät tuloja transaktiomaksuista ja jotka saattavat avata kanavia heitä kohti toivoen voivansa reitittää heidän maksunsa ja kerätä niihin liittyvät palkkiot.
- **Likviditeetin liikuttaminen**: Myyjä voi myös avata kanavan ja siirtää osan varoista vastakkaiselle puolelle tekemällä kuvitteellisia maksuja toiselle solmulle, joka palauttaa rahat toisella tavalla. Näemme seuraavassa osassa, miten tämä toimenpide suoritetaan.
- **Kolmikulmainen avaaminen**: Alustoja on olemassa solmuille, jotka haluavat avata kanavia yhteistyössä, mahdollistaen jokaiselle välittömän tulevan ja lähtevän likviditeetin hyödyn. Esimerkiksi [LightningNetwork+](https://lightningnetwork.plus/) tarjoaa tämän palvelun. Jos Alice, Bob ja Suzie haluavat avata kanavan 100 000 satoshilla, he voivat sopia tästä alustalla niin, että Alice avaa kanavan Bobille, Bob Suzielle ja Suzie Alicelle. Näin jokaisella on 100 000 satoshin lähtevä likviditeetti ja 100 000 satoshin tuleva likviditeetti, samalla kun on lukittu vain 100 000 satoshia.

![LNP201](assets/en/73.webp)

- **Kanavien ostaminen**: Palveluita Lightning-kanavien vuokraamiseen on myös olemassa tulevan likviditeetin saamiseksi, kuten [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) tai [Lightning Labs Pool](https://lightning.engineering/pool/). Esimerkiksi Alice voi ostaa kanavan yhden miljoonan satoshin arvoisesti solmulleen voidakseen vastaanottaa maksuja.

![LNP201](assets/en/74.webp)

Lopuksi reitittimille, joiden tavoitteena on maksimoida käsiteltyjen maksujen määrä ja kerätyt palkkiot, niiden on:

- Avattava hyvin rahoitettuja kanavia strategisten solmujen kanssa.
- Säännöllisesti säädettävä varojen jakautumista kanavissa verkon tarpeiden mukaisesti.

### Loop Out -palvelu

[Loop Out](https://lightning.engineering/loop/) -palvelu, jonka Lightning Labs tarjoaa, mahdollistaa likviditeetin siirtämisen kanavan vastakkaiselle puolelle samalla kun varat lunastetaan takaisin Bitcoin-lohkoketjuun. Esimerkiksi Alice lähettää 1 miljoona satoshia Lightningin kautta loop-solmulle, joka palauttaa nämä varat hänelle on-chain bitcoineina. Tämä tasapainottaa hänen kanavansa 1 miljoonalla satoshilla kummallakin puolella, optimoiden hänen kykynsä vastaanottaa maksuja.

![LNP201](assets/en/75.webp)

Näin ollen tämä palvelu mahdollistaa tulevan likviditeetin samalla kun lunastetaan omat bitcoinit on-chain, mikä auttaa rajoittamaan käteisen immobilisointia, jota tarvitaan maksujen vastaanottamiseen Lightningin kautta.

**Mitä sinun tulisi ottaa tästä luvusta mukaasi?**

- Maksujen lähettämiseksi Lightningissa sinulla on oltava tarpeeksi likviditeettiä kanavissasi omalla puolellasi. Lähettämiskyvyn lisäämiseksi avaa yksinkertaisesti uusia kanavia.
- Maksujen vastaanottamiseksi tarvitset likviditeettiä kanaviesi vastakkaisella puolella. Tämän vastaanottokyvyn lisääminen on monimutkaisempaa, koska se vaatii muiden avaavan kanavia sinua kohti tai tekemään (kuvitteellisia tai todellisia) maksuja siirtääkseen likviditeetin toiselle puolelle.
- Likviditeetin ylläpitäminen halutussa paikassa voi olla vielä haastavampaa kanavien käytöstä riippuen. Siksi olemassa on työkaluja ja palveluita, jotka auttavat tasapainottamaan kanavia toivotulla tavalla.

Seuraavassa luvussa ehdotan tärkeimpien käsitteiden kertausta tästä koulutuksesta.

# Mene pidemmälle

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Koulutuksen päätelmä

<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

![päätelmä](https://youtu.be/MaWpD0rbkVo)
Tässä viimeisessä luvussa, joka merkitsee LNP201-koulutuksen päätöstä, ehdotan, että kertaamme yhdessä käsittelemämme tärkeät konseptit.
Tämän koulutuksen tavoitteena oli tarjota sinulle kattava ja tekninen ymmärrys Lightning-verkosta. Havaitsimme, miten Lightning-verkko nojaa Bitcoinin lohkoketjuun suorittaakseen off-chain-transaktioita, säilyttäen samalla Bitcoinin perusominaisuudet, erityisesti tarpeettomuuden luottaa muihin solmuihin.

### Maksukanavat

Alkuluvuissa tutkimme, miten kaksi osapuolta voi suorittaa transaktioita Bitcoinin lohkoketjun ulkopuolella avaamalla maksukanavan. Tässä ovat käsitellyt vaiheet:

1. **Kanavan Avaaminen**: Kanavan luominen tapahtuu Bitcoin-transaktiolla, joka lukitsee varat 2/2 moniallekirjoitusosoitteeseen. Tämä talletus edustaa Lightning-kanavaa lohkoketjussa.

![LNP201](assets/en/76.webp) 2. **Transaktiot Kanavassa**: Tässä kanavassa on sitten mahdollista suorittaa lukuisia transaktioita julkaisematta niitä lohkoketjussa. Jokainen Lightning-transaktio luo kanavan uuden tilan, joka heijastuu sitoutumistransaktiossa.
![LNP201](assets/en/77.webp)

3. **Turvaaminen ja Sulkeminen**: Osallistujat sitoutuvat kanavan uuteen tilaan vaihtamalla peruutusavaimia varojen turvaamiseksi ja huijaamisen estämiseksi. Molemmat osapuolet voivat sulkea kanavan yhteistyössä tekemällä uuden transaktion Bitcoinin lohkoketjussa, tai viimeisenä keinona pakotetun sulkemisen kautta. Tämä jälkimmäinen vaihtoehto, vaikka se on vähemmän tehokas koska se on pidempi ja joskus huonosti arvioitu maksujen suhteen, sallii silti varojen palauttamisen. Huijauksen tapauksessa uhri voi rangaista huijaria palauttamalla kaikki kanavan varat lohkoketjussa.

![LNP201](assets/en/78.webp)

### Kanavien Verkosto

Tutkittuamme erillisiä kanavia, laajensimme analyysiamme kanavien verkostoon:

- **Reititys**: Kun kaksi osapuolta ei ole suoraan yhdistetty kanavalla, verkosto mahdollistaa reitityksen välisolmujen kautta. Maksut kulkevat sitten solmulta toiselle.

![LNP201](assets/en/79.webp)

- **HTLC:t**: Välisolmujen kautta kulkevat maksut turvataan "_Hash Time-Locked Contracts_" (HTLC) avulla, jotka mahdollistavat varojen lukitsemisen, kunnes maksu on suoritettu alusta loppuun.

![LNP201](assets/en/80.webp)

- **Onion Reititys**: Maksun luottamuksellisuuden varmistamiseksi onion reititys peittää lopullisen määränpään välisolmuilta. Lähettävän solmun on siis laskettava koko reitti, mutta kanavien likviditeetin täydellisen tiedon puuttuessa se etenee peräkkäisin kokeiluin reitin maksun reitittämiseksi.

![LNP201](assets/en/81.webp)

### Likviditeetin Hallinta

Olemme nähneet, että likviditeetin hallinta on haaste Lightning-verkossa maksujen sujuvan kulun varmistamiseksi. Maksujen lähettäminen on suhteellisen yksinkertaista: se vaatii vain kanavan avaamisen. Kuitenkin maksujen vastaanottaminen edellyttää likviditeetin olemassaoloa omien kanavien vastakkaisella puolella. Tässä joitakin käsiteltyjä strategioita:

- **Kanavien Houkutteleminen**: Kannustamalla muita solmuja avaamaan kanavia itselleen, käyttäjä saa tulevaa likviditeettiä.

- **Likviditeetin Siirtäminen**: Lähettämällä maksuja muille kanaville, likviditeetti siirtyy vastakkaiselle puolelle.

![LNP201](assets/en/82.webp)

- **Palveluiden, kuten Loop ja Pool, Käyttäminen**: Nämä palvelut mahdollistavat uudelleentasapainottamisen tai kanavien ostamisen likviditeetillä vastakkaisella puolella.
  ![LNP201](assets/en/83.webp)
- **Yhteistyössä Tehdyt Avaamiset**: On myös alustoja saatavilla yhdistämään suorittamaan kolmikantaisia avaamisia ja saamaan tulevaa likviditeettiä.

![LNP201](assets/en/84.webp)

### Kiitokset
Haluaisin kiittää jokaista teistä kiinnostuksestanne, tuestanne ja kysymyksistänne tämän sarjan aikana. Alun perin ideani oli luoda ranskankielistä sisältöä Lightningin teknisistä näkökohdista, ottaen huomioon saatavilla olevien resurssien puutteen. Se oli henkilökohtainen haaste, jonka halusin ottaa vastaan yhdistämällä teknisen tarkkuuden saavutettavuuteen. Jos pidit tästä ilmaisesta kurssista, ole hyvä ja arvostele se "_Arvostele tämä kurssi_" -osiossa ja jaa se rakkaimpiesi ja sosiaalisten verkostojesi kanssa.
Kiitos, nähdään pian!

### Bonus: Haastattelu Faniksen kanssa

![Haastattelu Faniksen kanssa](https://youtu.be/VeJ4oJIXo9k)

## Arvostele tämä kurssi

<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>
<isCourseReview>true</isCourseReview>

## Loppukoe

<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>
<isCourseExam>true</isCourseExam>

## Yhteenveto

<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>

**Onnittelut kurssin suorittamisesta!**

Huomaa, että tämä luku on parhaillaan työn alla ja paranneltu versio saapuu pian. Sillä välin, jos olet innokas jatkamaan Bitcoin-matkaasi, kutsumme sinut tutustumaan muihin alustallamme saatavilla oleviin kursseihin ja opetusohjelmiin. Jatka hyvää työtä ja iloista oppimista!