---
name: Inkivääri Wallet
description: Avoimen lähdekoodin, omavalvonnan Bitcoin Wallet -ohjelmisto, Fork Wasabi Wallet:sta, Coinjoinsin integrointi
---
![cover](assets/cover.webp)



Ginger Wallet on avoimen lähdekoodin Bitcoin-salkku, jossa ei ole huoltajuutta ja jossa keskitytään luottamuksellisuuteen ja yksityisyyteen. Se sai alkunsa Fork:n nimellä Wasabi Wallet:stä (version 2.0.7.2 jälkeen - MIT-lisenssi).



Ginger Wallet säilyttää Wasabin teknisen arkkitehtuurin, mutta lisää muutamia erityisominaisuuksia. [Ginger Wallet:n dokumentaation](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet) mukaan Wasabi korostaa **autonomiaa ja hallintaa**, kun taas Ginger keskittyy **käytön helppouteen, turvallisuuteen ja yksinkertaistettuun käyttökokemukseen**, mikä tekee siitä helpommin lähestyttävän niille, jotka eivät ole perehtyneet teknisiin seikkoihin.



Ginger Wallet on Wallet-ohjelmisto vain tietokoneille (ei mobiilisovellusta).



## Mikä on CoinJoin?



CoinJoin** on erityyppinen Bitcoin-tapahtumarakenne, joka kokoaa useita osallistujia yhteen yhteistapahtumaan. Tämä mekanismi sekoittaa eri käyttäjien kirjaukset yhteiseen transaktioon, mikä tekee varojen jäljittämisestä erittäin vaikeaa - ellei jopa usein mahdotonta, jos se tehdään oikein. Tämän seurauksena ulkopuolisen tarkkailijan on lähes mahdotonta tunnistaa varmuudella mukana olevien bitcoinien alkuperä ja määränpää, toisin kuin tavanomaisissa Bitcoin-tapahtumissa.



CoinJoin auttaa sinua, käyttäjää, säilyttämään luottamuksellisuutesi. Jos esimerkiksi saat 10 000 Sats:n lahjoituksen Bitcoin Address:lla, lähettäjä voi jäljittää nämä varat ja joissakin tapauksissa päätellä, että sinulla on hallussasi suurempi määrä bitcoineja, tai tarkkailla toimintaasi. Tekemällä CoinJoin tämän 10 000 Sats:n lahjoituksen jälkeen katkaiset jäljitettävyyden: lähettäjä ei voi enää johtaa mitään tietoja sinusta tästä maksusta.



Chaumian CoinJoin tarjoaa korkean turvallisuustason, sillä varat pysyvät koko ajan käyttäjän yksinomaisessa valvonnassa. Edes koordinoivien palvelimien ylläpitäjät eivät voi missään tapauksessa siirtää osallistujien bitcoineja. Käyttäjien ja koordinaattoreiden ei tarvitse luottaa toisiinsa: kumpikin pitää yksityiset avaimensa hallussaan ja on yksin oikeutettu vahvistamaan transaktioita. Kukaan kolmas osapuoli ei siis voi anastaa bitcoinejasi CoinJoin:n aikana eikä luoda suoraa yhteyttä syötteiden ja tulosteiden välille.



Jos haluat lisätietoja CoinJoin:stä, tutustu Plan ₿ Academyn BTC 204 -kurssille :



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Asenna inkivääri Wallet



Voit asentaa Ginger Wallet:n verkkosivustolla [Ginger Wallet] (https://gingerwallet.io).



Paina **Lataus** ladataksesi oikean version tietokoneellesi (Windows / MacOs / Linux).



![screen](assets/fr/03.webp)



Toinen vaihtoehto on ladata projekti [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases).



![screen](assets/fr/04.webp)



Käynnistä sitten asennusohjelma.



![screen](assets/fr/05.webp)




## Parametriasetukset



### Alustavat kokoonpanot



Avaa Ginger Wallet ja valitse haluamasi kieli.



![screen](assets/fr/06.webp)



Ginger muistuttaa heti alussa CoinJoin-prosessiin liittyvistä kustannuksista.



![screen](assets/fr/07.webp)



Paina sitten **Start** ja sitten **New** luodaksesi uuden portfolion.



![screen](assets/fr/08.webp)



Tallenna ja vahvista sitten seedphrase.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Ginger Wallet antaa mahdollisuuden lisätä passphrase:n lisäturvaksi.



![screen](assets/fr/11.webp)



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Kun tämä passphrase on lisätty, sitä pyydetään joka kerta, kun yrität käyttää salkkuasi.



![screen](assets/fr/12.webp)



Ginger aktivoi automaattisesti oletusarvon **CoinJoin**, kun luot salkun. Sinulle ilmoitetaan tästä ja voit sitten muokata asetusta tarpeisiisi sopivaksi.



![screen](assets/fr/13.webp)




### Yleiset asetukset



Kun olet luonut ensimmäisen portfoliosi, sinut viedään Gingerin Interface Wallet:een.



![screen](assets/fr/14.webp)



Aktivoi **Discreet-tila**, jos haluat piilottaa lompakoiden saldot.



![screen](assets/fr/15.webp)



Voit luoda useita salkkuja Ginger Wallet:ssä. Klikkaa yksinkertaisesti **Lisää salkku**.



![screen](assets/fr/16.webp)



Ginger tukee laitteistoportfolioiden käyttöä Bitcoin core-standardin Interface kautta, vaikka suora integrointi laitteistoportfoliosta tai laitteistoportfolioon ei ole vielä käytettävissä.



Yhteensopiviin laitteistosalkkuihin kuuluvat (mutta eivät rajoitu) :




- BLOCKSTREAM Jade
- Kylmäkortti MK4
- Kylmäkortti Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor malli T
- Trezor Safe 3
- jne.



Napsauta nyt **Asetukset**.



![screen](assets/fr/17.webp)



Nämä asetukset ovat sovelluksen yleisiä asetuksia, ja siellä tekemäsi määritykset koskevat kaikkia salkkuja.



**Asetukset** -kohdassa on välilehdet :





- Yleistä**



![screen](assets/fr/18.webp)





- Ulkonäkö



Tällä välilehdellä voit vaihtaa muun muassa kielen, valuutan ja maksun näyttöyksikön (BTC/Satoshi).



![screen](assets/fr/19.webp)





- Bitcoin**



Tällä välilehdellä voit ottaa Bitcoin Knots:n käyttöön sovelluksen käynnistyessä, valita verkon (Main/RegTest) ja lataustariffin tarjoajan (Mempool Space/BLOCKSTREAM info/Full node) jne.



![screen](assets/fr/20.webp)





- Turvallisuusominaisuudet**



Turvallisuus-välilehdellä voit ottaa käyttöön kaksitekijätodennuksen, aktivoida tai poistaa Torin käytöstä ja jopa poistaa sen käytöstä, kun Ginger-sovellus suljetaan.



![screen](assets/fr/21.webp)



**NB** :




- Varmista kaksitekijätodennusta varten, että todennussovelluksesi tukee SHA256-protokollaa ja 8-numeroisia koodeja. Ginger Wallet vaatii 8-numeroisen 2FA-koodin tehostettua turvallisuutta varten. Tämän pidemmän muodon ansiosta koodia on paljon vaikeampi arvata tai vaarantaa, mikä tarjoaa paremman suojan luvatonta käyttöä vastaan.
- Oletusarvoisesti kaikki Gingerin verkkoliikenne kulkee Torin kautta, jolloin manuaalista määritystä ei tarvita. Jos Tor on jo aktiivinen järjestelmässäsi, Ginger antaa sille automaattisesti etusijan.



Kun poistat Torin käytöstä asetuksista, yksityisyytesi säilyy yleensä, paitsi kahdessa tilanteessa:




- gW-42:n aikana koordinaattori voi yhdistää tulot ja lähdöt IP Address:een;
- kun lähetät transaktiota, haitallinen solmu, johon olet yhteydessä, voi yhdistää transaktiosi IP-osoitteeseesi.



Muista joka kerta painaa **Tehdään** (oikeassa alakulmassa Coin) tallentaaksesi asetukset. Jotkin asetukset edellyttävät Ginger Wallet:n uudelleenkäynnistämistä, jotta ne tulevat voimaan.



Lisäksi portfolioiden yläosassa olevan hakupalkin avulla voit etsiä ja käyttää mitä tahansa parametria jne...



![screen](assets/fr/22.webp)




### Salkun kokoonpano



Sovelluksessa voidaan luoda useita salkkuja, joten jokainen salkku voidaan konfiguroida tarpeidesi mukaan. Napsauta salkun nimen edessä olevaa **kolmea pistettä** ja sitten **Salkun asetukset**.



![screen](assets/fr/23.webp)



Kuten näet, Wallet-parametrin lisäksi näet UTXO:t (luettelo omistamistasi tokeneista), tilastot ja Wallet-tiedot (esimerkiksi laajennettu julkinen avain).



Palataksesi salkun määritykseen, kun napsautat salkun parametreja, pääset seuraaville välilehdille:




- Yleistä** (jossa voit vaihtaa salkun nimen) ;



![screen](assets/fr/24.webp)





- CoinJoin** (jossa voit muokata tämän salkun CoinJoin-asetuksia) ;



![screen](assets/fr/25.webp)





- Työkalut** (jossa voit tarkistaa seedphrase:n, synkronoida salkkusi uudelleen tai poistaa sen).



![screen](assets/fr/26.webp)




## Vastaanottaa bitcoineja



Jos haluat vastaanottaa bitcoineja Wallet:ään Ginger Wallet:ssä :




- paina **Vastaanottaa** ;



![screen](assets/fr/27.webp)





- Kirjoita sen lähteen nimi, johon haluat liittää Address:n. Tämä on merkintä, jonka avulla voit seurata maksuja. Tällä ei ole On-Chain:n vaikutuksia; se on vain paikallisesti sovellukseesi tallennettua jäljitettävyystietoa;



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- valitse Address-muoto (**SegWit** /**Taproot**) napsauttamalla **generate** vasemmalla puolella olevaa pientä nuolta ja napsauta sitten **generate** generate:n ja Address:n sekä QR-koodin valitsemiseksi.



![screen](assets/fr/29.webp)



Lähettäjäsi käyttää tätä Address- tai QR-koodia lähettääkseen sinulle bitcoineja.



![screen](assets/fr/30.webp)




## Lähetä bitcoineja



Ohjevideo siitä, miten Ginger Wallet:n kautta lähetetään.



![Vidéo](https://youtu.be/2nf5aAimfhg)



Tätä varten :




- Paina **Lähetä**-painiketta;
- kirjoita vastaanottajan Address, lähetettävä summa ja etiketti;
- tarkista tapahtuman yleiskatsaus ja vahvista lähetys.



![screen](assets/fr/31.webp)




## Käytä bitcoineja



Bitcoin on helppo ostaa ja myydä Ginger Wallet:n kanssa. Vain muutamassa vaiheessa voit käyttää bitcoinisi.



### Osta bitcoineja



Ginger Wallet:n käyttäjät voivat ostaa bitcoineja.





- Paina **Osta**-painiketta. Tämä painike pysyy näkyvissä, vaikka Wallet olisi tyhjä.



![screen](assets/fr/32.webp)





- Valitse maasi tai jopa osavaltiosi (joillakin alueilla, kuten Kanadassa), ennen kuin jatkat Bitcoin:n ostamista. Itse asiassa, kun napsautat **Osta**-toimintoa ensimmäistä kertaa, sinun on myös määritettävä alueesi.



![screen](assets/fr/33.webp)



Paina **Jatka** edetäksesi ostoprosessin läpi.





- Kirjoita sitten haluamasi bitcoinien määrä sille varattuun kenttään. Voit myös valita transaktiovaluutan.



![screen](assets/fr/34.webp)



Kullakin valuutalla on vähimmäis- ja enimmäisostoraja. Esimerkiksi Yhdysvaltain dollareissa enimmäisraja on 30 000 dollaria.



Jos olet jo tehnyt ostoksen, voit tarkastella tapahtumahistoriaasi napsauttamalla **Edelliset tilaukset**-painiketta. Näyttöön tulee luettelo aiemmista maksutapahtumista ja niiden tilasta.





- Valitse sinulle sopiva tarjous.



Tässä vaiheessa näet luettelon kaikista saatavilla olevista tarjouksista. Jokaisen tarjouksen kohdalla sinulla on :




 - toimittajan nimi (1) ;
 - aiemmin syötettyä summaa vastaava määrä bitcoineja, maksutapa ja ostomaksu (2) ;
 - **Hyväksyntä**-painiketta (3).



![screen](assets/fr/35.webp)



Tarjouksessa ilmoitetut maksut eivät ole lisäkustannuksia. Ne sisältyvät jo tarjouksen kokonaissummaan.



Näytön oikeassa yläkulmassa Coin, jossa on merkintä **kaikki**, voit suodattaa tarjouksia maksutavan mukaan. Valitsemasi maksutapa asetetaan oletusarvoisesti, mutta sitä voi muuttaa milloin tahansa.



![screen](assets/fr/36.webp)



Jos löydät sopivan tarjouksen, jatka ostamista napsauttamalla **Hyväksyn**-painiketta. Tämän jälkeen sinut ohjataan myyjän sivulle, jossa voit viimeistellä kaupan.



### Bitcoinien myynti



Inkivääri Wallet:n käyttäjät voivat myydä Bitcoin:tä. **Myydä**-painike on näkyvissä vain silloin, kun salkussa on varoja käytettävissä.





- Klikkaa **Myydä**.



![screen](assets/fr/37.webp)





- Kuten **Osta**-vaihtoehdon kohdalla, kun käytät myyntitoimintoa ensimmäistä kertaa, sinun on valittava maasi ennen Bitcoin-myynnin aloittamista.





- Seuraavaksi sinun on syötettävä myytävien Bitcoins-määrä. Voit antaa tämän summan BTC:nä tai fiat-valuuttana, kuten Yhdysvaltain dollarina (USD).





- Kun olet tehnyt tämän, näet luettelon saatavilla olevista tarjouksista. Valitse itsellesi sopiva myyntitarjous ja jatka sitten napsauttamalla **Hyväksyä**.





- Nyt sinun on viimeisteltävä kauppa:
 - Kun olet hyväksynyt tarjouksen, sinut ohjataan toimittajan sivulle;
 - Seuraa toimittajan sivulla olevia ohjeita ;
 - Jossain vaiheessa saat vastaanottajan Address ja tarkan lähetettävän summan;
 - Palaa sitten takaisin inkivääri Wallet:ään jatkaaksesi prosessia;
 - Kun olet taas Ginger Wallet:ssä, näyttöön tulee valintaikkuna, jossa voit jatkaa klikkaamalla **lähettää**.



Tämä avaa **lähettää** -näytön, jossa vastaanottajan Address ja summa on esitäytetty. Voit myös käyttää aloitusnäytön **lähettää**-painiketta. Vaikka voit lähettää tapahtuman manuaalisesti, suosittelemme, että suoritat sen valintaikkunan kautta, jotta prosessi olisi optimaalinen.



## Tee CoinJoin Ginger Wallet:sta Ginger Wallet:sta



![Vidéo](https://youtu.be/AJe67RDfB1A)



Suojaa bitcoinien luottamuksellisuus **CoinJoin**:llä, joka on integroitu suoraan Ginger Wallet:een. Wallet käyttää **WABISABI**:tä, Chaumian CoinJoin-protokollaa, joka on suunniteltu helpottamaan helpommin saavutettavia ja tehokkaampia kolikkoliitoksia.



Voit valita itsellesi parhaiten sopivan CoinJoin-strategian (automaattinen tai manuaalinen).



Ginger CoinJoin on käyttövalmis heti, kun olet ladannut sen (mitään muita vaiheita ei tarvita). Ginger CoinJoin toimii automaattisesti taustalla suojatakseen yksityisyytesi jokaisen tapahtuman yhteydessä. Käytännössä CoinJoin-lukija tulee näkyviin aina, kun sinulla on saldo, joka voidaan anonymisoida.



CoinJoin:n manuaalinen käynnistys onnistuu yhdellä napsautuksella. Käynnistä kierros ja odota, että CoinJoin-tapahtuma muodostetaan ja vahvistetaan. Näet anonymisointipisteet Interface:ssä.



Useita sekoituksia voidaan tehdä, kunnes saavutetaan haluttu anonymiteetin taso. Voit myös jättää tietyt osat pois miksauksesta.



Ginger käyttää oletusarvoisesti omaa koordinaattoriaan, jolla on kaikki valmiiksi määritetyt parametrit ja taatut maksut. Yli 0,03 BTC:n arvoisten kuponkien kolikkoliitoksista veloitetaan Mining-maksun lisäksi 0,3 prosentin koordinaattorimaksu. Enintään 0,03 BTC:n arvoiset merkinnät sekä remixit ovat vapautettuja koordinaattorimaksusta, jopa yhden transaktion jälkeen. Näin ollen CoinJoin-varoilla suoritettu maksu antaa sekä lähettäjälle että vastaanottajalle mahdollisuuden remixata kolikkonsa ilman koordinaattorimaksuja.



Ginger suosii useamman osallistujan yhteisturnauksia pienempien ja nopeampien kierrosten sijaan. Suuremmat coinjoinit tarjoavat enemmän anonymiteettiä, pienemmät kustannukset ja BLOCK-tilan tehokkaamman käytön.




## Turvallisuus ja parhaat käytännöt



Hajauttamispyrkimys ja yksityisyyden suojan säilyttäminen edellyttävät useiden parhaiden käytäntöjen omaksumista:




- Säilytä seedphrase aina turvallisessa paikassa offline-tilassa;
- Jos kadotat tietokoneesi tai epäilet, että siihen on luvaton pääsy, luo välittömästi uusi Wallet. Siirrä varasi tähän uuteen salkkuun ja poista vanha salkku;
- Käytä eri Address:ta jokaista vastaanottoa varten, jotta vältät osoitteiden uudelleenkäytön;
- Lataa portfoliosovellukset aina yksinomaan viralliselta GitHub-tililtä tai viralliselta verkkosivustolta.



Nyt tunnet Ginger Wallet -sovelluksen käyttämisen bitcoinien lähettämiseen, vastaanottamiseen ja käyttämiseen.



Jos löysit tämän opetusohjelman hyödylliseksi, jätä minulle Green peukku alla. Voit vapaasti jakaa tämän artikkelin sosiaalisen median alustoilla. Kiitos paljon!



Suosittelen myös tutustumaan tähän oppaaseen, jossa kerrotaan, miten Liana-tietokonesovellusta käytetään bitcoinien lähettämiseen ja vastaanottamiseen sekä automatisoidun kiinteistösuunnitelman toteuttamiseen.



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04