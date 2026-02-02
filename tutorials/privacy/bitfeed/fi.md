---
name: Bitfeed
description: Tutustu Bitcoin:n tärkeimpään protokollaketjuun.
---

![cover](assets/cover.webp)



Bitfeed on alusta Bitcoin-protokollan onchain-kerroksen visualisointiin. Sen aloitti yksi Mempool.space-projektin osallistujista, ja se erottuu edukseen lähinnä minimalistisen ulkonäkönsä ja helppokäyttöisyytensä ansiosta.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Tässä oppaassa tutustumme tähän työkaluun, jonka avulla voit tutkia kaikkia verkon transaktioita ja lohkoja.



## Bitfeedin käytön aloittaminen



Bitfeed on alusta, joka keskittyy kolmeen pääkohtaan:





- Blockchain kuuleminen**,
- Tapahtumahaku**,
- Mempoolin visualisointi**.



### Lohkoketjun konsultointi



Bitfeedin etusivulta löydät pääasiassa :





- Hakupalkki: Tämä osio on lohkoketjukyselyjen aloituspiste. Täältä voit hakea tiettyä lohkoa sen numeron tai hashin perusteella. Voit myös hakea tiettyjä transaktioita ja Bitcoin-osoitteita tarkistaaksesi tiettyjä transaktiotietoja verkossa.



![searchBar](assets/fr/01.webp)



Vasemmassa yläkulmassa näet bitcoinin senhetkisen hinnan Yhdysvaltain dollareina (USD).



![price](assets/fr/02.webp)



Oikeanpuoleisessa sivupalkissa on alustavalikko. Tästä valikosta voit muokata alustan käyttöliittymää mieleiseksesi, lisätä tai poistaa kohteita ja mukauttaa katselusuodattimia. Voit esimerkiksi tarkastella kunkin lohkon kokoa arvon tai painon mukaan virtuaalitavuina (vBytes).



![menu](assets/fr/03.webp)



Sivun keskellä on viimeisin louhittu lohko ja näkymä kaikista kyseiseen lohkoon sisältyvistä transaktioista. Tässä osiossa on tietoja aikaleimasta, lohkoon osallistuneiden bitcoinien kokonaismäärästä, lohkon koosta tavuina, transaktioiden määrästä ja keskimääräisestä transaktiokustannussuhteesta lohkon virtuaalista tavua kohti.



![block](assets/fr/04.webp)



Voit palata kanavan historiaan etsimällä tietyn lohkon hakupalkista ja tarkastella sitä haluamiesi kriteerien mukaisesti.



Haluamme esimerkiksi tarkastella lohkon "879488" tapahtumia.



![bloc](assets/fr/05.webp)



Tämän lohkon ensimmäinen transaktio edustaa **coinbase**-transaktiota, jonka avulla lohkon louhija voi ansaita mining-palkkion, joka voidaan käyttää vasta, kun 100 lohkoa on louhittu, ja joka koostuu mukana olevista transaktiomaksuista ja lohkon avustuksesta. Tämä transaktio mahdollistaa uusien bitcoinien liikkeeseenlaskun järjestelmässä.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f

Oletusarvoisesti lohkon tapahtumat esitetään kahden kriteerin mukaan:




- Koko, joka voi vaihdella arvon ja painon välillä (vBytes) ;
- Väri voi vaihdella iän ja virtuaalista tavua kohti laskettujen transaktiomaksujen suhteen mukaan.



![options](assets/fr/07.webp)



Näin ollen voidaan päätellä, että kaikilla samaan lohkoon sisältyvillä transaktioilla on sama määrä vahvistuksia lohkoketjussa. Suurimmat kuutiot edustavat transaktioita, jotka sisältävät eniten bitcoineja.



Tämä tulkinta vahvistetaan edelleen **"Info "** -valikkovaihtoehdolla, joka ilmoittaa meille lohkon transaktioiden värin ja koon käännöksen.



![infos](assets/fr/08.webp)



Voit myös tarkastella lohkon transaktioita virtuaalisten tavujen ja maksusuhteen mukaan. Tämä näkymä voi poiketa edellisestä, sillä transaktion sisältämä bitcoin-arvo ei määrittele sen kokoa.



![visualisation](assets/fr/09.webp)



### Tapahtumien tarkastelu



Voit hakea tapahtumaa sen tunnisteen avulla hakupalkin kautta. Voit myös napsauttaa kuutiota nähdäksesi kyseiseen tapahtumaan liittyvät tiedot.



Meidän tapauksessamme otetaan transaktio, joka vie suurimman tilan lohkosta `879488`.



![biggest](assets/fr/10.webp)



Näet, että tässä transaktiossa on "42,989", joka on viimeisimmän louhitun lohkon ja valitsemamme lohkon välinen erotus. Nämä vahvistukset auttavat vahvistamaan Bitcoin-verkon turvallisuutta, sillä tämän transaktion muuttaminen ilkivaltaisesti edellyttää, että hyökkääjillä on vastaava laskentateho koko päälohkoketjun uudelleenkirjoittamiseen.



Tämän tapahtuman koko on "57 088 vBytes", mikä johtuu pääasiassa sen rakentamisessa käytettyjen UTXO:iden suuresta määrästä (842 merkintää). Yllättävää kyllä, sovellettu maksusuhde on suhteellisen alhainen (vain 4 sats/vByte) verrattuna lohkon kokonaiskeskiarvoon, joka on 5,82 sats/vByte.



Eniten tilaa vievä transaktio ei siis välttämättä ole transaktio, jonka transaktiokustannussuhde on korkein.



![transaction](assets/fr/11.webp)



Jos seuraat **Info**-valikossa olevaa asteikkoa, transaktio, jonka transaktiokustannussuhde on korkein, on violetti. Tämä on transaktio [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35), jonka transaktiokustannussuhde on `147.49 sats/vBytes`.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Mempool visualisointi



Mempool on virtuaalinen paikka, jossa lohkoon sisällytettäväksi odottavat Bitcoin-tapahtumat on ryhmitelty yhteen. Bitfeed mahdollistaa useiden Bitcoin-kaivostyöläisten [mempool](https://planb.academy/resources/glossary/mempool) konsultoinnin, mikä tarjoaa laajan valikoiman transaktioiden seurantaa.



![mempool](assets/fr/13.webp)



Tässä osiossa voit seurata kaikkia voimassa olevia ja vielä vahvistamattomia transaktioita Bitcoin-verkon pääketjussa.



![unconfirmed](assets/fr/14.webp)



Sinulla on nyt opas Bitfeed-alustan käyttämiseen lohkojen ja transaktioiden analysoimiseksi, jotta voit visualisoida Bitcoin-verkon pääketjussa saatavilla olevat tiedot ja samalla hyötyä minimalistisesta ja helppokäyttöisestä käyttöliittymästä. Jos pidit tästä oppaasta, suosittelemme, että otat seuraavan askeleen: tutustu Lightning Network:een Amboss-projektin kautta.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017