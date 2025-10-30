---
name: StashPay
description: Minimalistinen Bitcoin Wallet kaikille
---

![cover](assets/cover.webp)



Käyttäjäkokemus on keskeinen tekijä Bitcoin-ratkaisujen käyttöönotossa kaikkialla maailmassa. Sujuvan, yksinkertaisen ja teknisesti vaivattoman käyttökokemuksen tarjoaminen on monien lompakoiden ja Exchange-alustojen ensisijainen tavoite. Tässä suhteessa StashPay erottuu edukseen minimalistisen lähestymistapansa ansiosta ja osoittaa samalla Lightning Network:n voiman.



Tässä oppaassa tutustumme tähän portfolioon ja selvitämme, miten se toimii ja miten se sopii pienille yrityksille tai yksinyrittäjille.



## Aloittaminen StashPayn kanssa



StashPay on Lightning-omahuoltaja Wallet, joka tunnetaan ensisijaisesti minimalistisesta, käyttäjäkeskeisestä käyttökokemuksestaan.  Tämän Wallet:n avulla et tarvitse teknistä osaamista vastaanottaaksesi ja lähettäksesi ensimmäiset satoshisi.



StashPay on avoimen lähdekoodin hanke, joka on kehitetty React Native -ohjelmalla, ja sen tavoitteena on ratkaista ongelma korkeista transaktiomaksuista jopa Bitcoin-protokollan pääketjussa tapahtuvissa transaktioissa. Se on saatavilla mobiilisovelluksena Android- ja iOS-alustoille [verkkosivustolla](https://stashpay.me/) olevien latauslinkkien kautta.



![introduce](assets/fr/01.webp)



On tärkeää ladata Android-sovellus verkkosivustolta, sillä se ei ole saatavilla Google Play Storesta.


Kun lataus on valmis, anna tarvittavat oikeudet, jotta voit asentaa sovelluksen Android-puhelimeesi.



Kun sovellus on asennettu, StashPay luo sinulle alustavan Bitcoin Wallet:n, kun avaat sen ensimmäistä kertaa. Suosittelemme, että teet varmuuskopion tästä Wallet:sta ennen kaikkia tapahtumia. Alta löydät kaikki ohjeemme, joilla varmistat, että palautuslausekkeistasi on tehty asianmukainen varmuuskopio.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Pääset StashPayn asetuksiin napsauttamalla "Asetukset"-kuvaketta ja napsauttamalla sitten **Luo varmuuskopio** -vaihtoehtoa. Hyväksy sitten palautuslauseiden näyttäminen. Älä kopioi palautuslauseita puhelimesi leikepöydälle, sillä ne voivat olla muiden matkapuhelimeesi asennettujen petollisten sovellusten käytettävissä.



![backup](assets/fr/02.webp)



Voit myös palauttaa jo käyttämäsi Bitcoin Wallet:n napsauttamalla **Palauta Wallet** -vaihtoehtoa ja lisäämällä 12 tai 24 palautussanaa.



### Vastaanota ensimmäiset satoshisi StashPayn kautta



Napsauta aloitusnäytössä **Vastaanottaa**-painiketta ja aseta punaisella merkittyä määrää suurempi summa. Meidän tapauksessamme emme voi vastaanottaa vähemmän kuin 0,11 USD StashPay Wallet:llä.



![receive](assets/fr/03.webp)



Kun olet määrittänyt summan, voit napsauttaa **Luo Invoice**-painiketta, skannata tai kopioida Invoice:n ja lähettää sen satoshis-lähettäjälle.



![receive_sats](assets/fr/04.webp)



Voit tarkastella tapahtumahistoriaasi napsauttamalla etusivun "kello"-kuvaketta.



![network_fee](assets/fr/05.webp)



Olet varmaan huomannut, että saadaksesi satosheja sinun on maksettava verkkomaksu. Nämä maksut vähennetään saamistasi satoshista. Tämä johtuu siitä, että StashPay on Breez Development Kitiin perustuva Wallet. Jos haluat vastaanottaa satosheja Kitin Lightning node-free -toteutuksella, Breez veloittaa asiakkaalta (meidän tapauksessamme StashPaylta) `0,25 % + 40 satoshea`. Lue lisää Misty Breez -oppaastamme.



https://planb.academy/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Lähetä bitcoineja StashPayn avulla



Bitcoinien lähettäminen StashPayn avulla on melko intuitiivista minimalistisen Interface:n ansiosta. Napsauta aloitusnäytössä **lähettää**-painiketta. Skannaa QR-koodi tai liitä Address, johon haluat lähettää satoshia. StashPay tunnistaa automaattisesti Bitcoin-protokollaketjun, johon haluat lähettää bitcoineja.



![send](assets/fr/06.webp)



Koska StashPay on Breez Development Kitiin perustuva Wallet, sillä on mielenkiintoinen etu: bitcoinien lähettäminen pääketjussa edullisesti. Breez käyttää Boltz-palvelua transaktioiden suorittamiseen Bitcoin-protokollan eri ketjujen välillä, joten Development Kitin käyttöön ottavat asiakkaat voivat hyödyntää tätä palvelua suoraan sovelluksessaan.



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Breez SDK asettaa kuitenkin vähimmäissumman, jolla voit lähettää bitcoineja pääketjun Address:lle.



![onchain](assets/fr/07.webp)



Voit lähettää bitcoineja myös vastaanottajan Lightning Address -palvelun avulla. Tarkista tapahtuman tiedot ja vahvista sitten klikkaamalla **lähettää**-painiketta.



![confirm](assets/fr/08.webp)



## Lisää kokoonpanoja



StashPayn asetuksissa voit mukauttaa asetuksia Wallet:n käytön mukauttamiseksi.



StashPayn avulla voit maksaa Exchange satoshia valitsemallasi paikallisella valuutalla. Napsauta **Valuutat**-vaihtoehtoa ja etsi sitten valuutta StashPayn tarjoamasta +113 valuutan luettelosta.



![currencies](assets/fr/09.webp)



**Vastaanottovaihtoehdot** -valikosta löydät kaikki asetukset bitcoinien vastaanottamiseksi StashPayn avulla. Valitsemalla esimerkiksi **Valitse Lightning tai Onchain** voit ottaa Wallet:n käyttöön vastaanottamaan bitcoineja pääketjusta.



![receive-onchain](assets/fr/10.webp)



**Tarkista OnChain-osoitteet** -vaihtoehdon avulla voit päivittää Wallet:n saldon tarkistamalla kaikki UTXO:t (bitcoinit, joita et ole vielä käyttänyt), jotka on liitetty eri osoitteisiisi.



![rescan](assets/fr/11.webp)



Valikossa **Tuontiloki** luetellaan kaikki Breez- ja Boltz-infrastruktuurin toimet, jotka koskevat transaktioitasi ja eri Bitcoin-protokollaketjujen välisiä atomien vaihtoja.



![export](assets/fr/12.webp)



StashPayn minimalistisen Bitcoin Wallet:n kanssa on juuri tullut toimeen. Jos löysit tämän ohjeen hyödylliseksi, suosittelemme ohjettamme siitä, miten pääset alkuun Bitcoin:lla ja ansaitset ensimmäiset bitcoinisi.



https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f