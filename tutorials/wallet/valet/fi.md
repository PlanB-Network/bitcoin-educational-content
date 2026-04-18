---
name: Valet Bitcoin
description: Valet tuo ei-huoltajan Lightning-solmun taskuusi
---

![cover_valet](assets/cover.webp)



## Johdanto


Valet on kevyt, itseohjautuva Bitcoin- ja Lightning wallet -laite, joka tarjoaa helpon ja kätevän käyttöönottoprosessin aloittelijoille. Se on räätälöity erityisesti Bitcoin-yhteisöjä ja kiertotaloutta varten, erityisesti syrjäseuduilla.


Se on **Simple Bitcoin Wallet (SBW)**:n fork, jossa on kehittynyt Hosted Lightning -kanavaominaisuus nimeltä **Fiat Channels**, joka on suunniteltu niin, että kuka tahansa voi hyväksyä Lightning-maksuja ilman volatiliteettiriskejä.


Valet on tällä hetkellä saatavilla vain Android-laitteille, ja sen voi ladata ja asentaa useista avoimista sovelluskaupoista. Valet ei kuitenkaan ole **ei** Google Play Storessa** kehittäjien yksityisyyden suojaan ja KYC:hen liittyvien huolenaiheiden vuoksi.



## Lataa ja asenna Valet


Valet voidaan ladata APK-tiedostona Standard Sats:n GitHub-sivulta. [Standard Sats](https://standardsats.github.io/) on Valetin kehittänyt yritys.


👉 Jos haluat ladata Valetin, käy Standard Sats [GitHub-sivulla](https://github.com/standardsats/valet/releases) ja etsi **uusin** julkaisu (tämä on usein päällimmäinen).


👉 Mene kohtaan **Assets** ja napsauta tiedostoa, jolla on vain **.apk**-pääte. Lataus käynnistyy automaattisesti.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


👉 Kun lataus on valmis, siirry laitteesi **Tiedostonhallinta** > **Lataukset** ja valitse Valet apk-tiedosto.


![Select_valet_apk](assets/en/002.webp)


👉 Asenna se, ja muutaman sekunnin kuluttua sovellus on valmis ja ilmestyy aloitusnäyttöön.


![valet_icon_on_homescreen](assets/en/003.webp)


Vaihtoehtoisesti voit myös ladata Valetin **F-Droid**-sovelluskaupasta. Jos sinulla ei ole F-Droid-sovellusta laitteessasi, voit ladata ja asentaa sen [täältä](https://f-droid.org/en/).


👉 Avaa aloitusnäytöltä F-Droid ja etsi **Valet**. Valitse ensimmäinen vaihtoehto, jossa on **violetti ja valkoinen kuvake**, kahdesta esiin tulevasta vaihtoehdosta ja napsauta **Lataus**.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


👉 Kun olet ladannut ohjelman, napsauta **Asenna** ja noudata näytön ohjeita. Kun asennus on valmis, voit käynnistää Valetin F-Droid:stä napsauttamalla **Avaa** tai käynnistää sen laitteen aloitusnäytöstä.



## Bitcoin Wallet:n luominen


Voit määrittää Bitcoin wallet:n Valetissa kahdessa yksinkertaisessa vaiheessa.


👉 Käynnistä Valet laitteen aloitusnäytöstä tai F-Droid-sovelluksesta. Näyttöön tulee wallet:n asetusnäyttö, jossa on kaksi vaihtoehtoa: **Luo uusi Wallet** ja **Palauta olemassa oleva Wallet**.


👉 Valitse **Luo uusi Wallet**, ja heti luodaan uusi wallet, ja sinut ohjataan etusivulle.


![set_up_a\_new_wallet](assets/en/006.webp)



## Varmuuskopioi siemenlauseesi


👉 Napsauta wallet:n etusivulla **Green-korttia**, jossa on merkintä **"Napauta tallentaaksesi wallet:n palautuslauseen siltä varalta, että kadotat tai vaihdat laitteen".**


![seed_phrase_green_card](assets/en/007.webp)


👉 Näyttöön tulee 12 englanninkielistä sanaa. Kirjoita ne paperille järjestyksessä 1-12 ja säilytä niitä.


![the_seed_phrase](assets/en/008.webp)


### Kiinnitä huomiota ⚠️:


Kiinnitä huomiota seuraaviin tekijöihin:


- Kuten jo tiedät, Valet on wallet:n itsesäilyttävä, joten seed-lauseesi on ainoa keino saada Wallet takaisin.
- Jos menetät seed-lauseesi, et **saa** koskaan wallet-lauseesi käyttöön.
- Jos joku saa seed-lauseesi, hän voi peruuttamattomasti varastaa kaikki Bitcoin-laitteesi.


Sinun on siis kirjoitettava ylös 12 sanan seed-lauseesi ja säilytettävä se turvallisessa paikassa. Älä koskaan ota kuvakaappausta, tallenna sitä luonnoksena sähköpostiin tai tallenna sitä mihinkään elektroniseen laitteeseen, joka on koskaan ollut yhteydessä internetiin.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Bitcoin:n vastaanottaminen ja lähettäminen Valetissa


Valet on itsesäilyttävä wallet, jossa on sekä on-chain- että Lightning Bitcoin -ominaisuudet. Tämä tarkoittaa sitä, että voit vastaanottaa ja lähettää Bitcoin:n Valetista joko **On-chain**- tai **Lightning Network**-ketjun kautta.


Jotta voit kuitenkin vastaanottaa tai lähettää Bitcoin:ta Lightningin kautta, sinun on perustettava Lightning-kanava, jossa on-chain Bitcoin:t toimivat Liquiditynä. Tai voit ostaa Lightning-kanavan likviditeetin myyjiltä.



## Ketjussa olevan Bitcoin Address:n luominen


Jos haluat vastaanottaa Bitcoin:n on-chain:n kautta, sinun on luotava Bitcoin-osoite.


👉 wallet:n etusivulla näet **oranssin** ja **violetin kortin**, jotka on merkitty vastaavasti nimillä **Bitcoin** ja **Valo**.


👉 Napsauta oranssia korttia, jossa on merkintä **Bitcoin**. Sinut ohjataan näytölle, jossa näkyy Bitcoin-osoite.


![click_on_Bitcoin_card](assets/en/009.webp)


👉 Voit **kopioida** osoitteen ja lähettää sen henkilölle, joka lähettää sinulle Bitcoin-lähetyksiä, tai napsauttaa **Jaa**-painiketta lähettääksesi QR-koodin henkilölle sosiaalisen median tai muiden viestintäkanavien kautta.


👉 Voit myös napsauttaa **Muokkaa**-painiketta asettaaksesi kyseiseen osoitteeseen lähetettävien Bitcoin:ien määrän.


**Huomio:** Muokkaustoiminto on laskun tapaan kätevä tilanteissa, joissa haluat saada tietyn määrän Bitcoin:ää tiettyyn osoitteeseen tietyssä vaiheessa; tämä ei kuitenkaan tarkoita, että osoite ei voisi saada suurempia tai pienempiä määriä.


👉Klikkaa **Lisää tuoreita osoitteita**, luodaksesi uusia satunnaisia osoitteita.


![generating_a\_bitcoin_add](assets/en/010.webp)


👉 Voit myös luoda on-chain Bitcoin -osoitteen napsauttamalla wallet:n etusivun alareunassa olevaa **Vastaanota**-painiketta. Valitse sitten **Vastaanottaa bitcoin-osoitteeseen** ja jatka samaa edellä mainittua prosessia.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Bitcoin:n lähettäminen ketjussa


Bitcoin:n lähettäminen Valet wallet:stä on-chain:n kautta on yksinkertainen tehtävä.


👉 Napsauta wallet:n kotisivun alareunassa **lähettää**-painiketta, syötä Bitcoin:n osoite tai napsauta **skannaa** skannataksesi osoitteen QR-koodin ja napsauta sitten **Ok**.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


👉 Kirjoita lähetettävä Bitcoin-määrä. Voit syöttää summan manuaalisesti Sats:nä tai Fiat-valuuttana tai voit klikata **Max** käyttääksesi koko on-chain-saldosi.


👉 Voit myös säätää maksuja, jotka haluat maksaa tapahtumasta, napsauttamalla pientä vihreää laatikkoa, jossa lukee **maksu**, ja liu'uttamalla valkoista pistettä oikealle tai vasemmalle voit lisätä tai vähentää maksuja. Lähetä tapahtuma napsauttamalla **Ok**.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Lightning Network-kanavan määrittäminen


Kuten edellä mainittiin, Valet on itseohjautuva Bitcoin ja Lightning wallet; jotta voit lähettää ja vastaanottaa Bitcoin:tä Lightning-verkon kautta, sinun on ensin perustettava Lightning-kanava seuraavien ohjeiden mukaisesti:


👉 Napsauta aloitusnäytössä **violettia korttia**, jossa on merkintä **Salama**. Pääset sivulle, jossa on seuraavat vaihtoehdot:



- Skannaa solmu QR
- Osta osoitteesta LNBIG.COM
- Osta osoitteesta BITREFILL.COM
- Pyyntö LN-graafin uudelleensynkronoinnista.


Kun valitset **Ostaa lnbig.comista** tai **Ostaa bitrefill.comista**, sinut ohjataan näiden yritysten verkkosivustoille, joilla voit ostaa usean kapasiteetin saapuvan likviditeetin. Jätä toistaiseksi huomiotta viimeinen vaihtoehto **Pyydä LN-kuvaajan uudelleensynkronointia**.


Joten meidän valintamme on **Skannaa solmun QR**. Tässä vaiheessa sinun on päätettävä ja saatava sen solmun **QR-koodi**, johon haluat avata kanavan. Voit avata kanavia mihin tahansa valitsemaasi julkiseen solmuun. Tarkista [1ML](https://1ml.com/) tai [Amboss](https://amboss.space/), valitse mikä tahansa valitsemasi julkinen solmu ja skannaa valitsemasi solmun QR-koodi.


![channel_opening_options](assets/en/016.webp)


👉 Sinut ohjataan automaattisesti seuraavalle sivulle, jossa sinun on nyt rahoitettava kanavasi. Jälleen kerran omavalvontakäyttöinen Salama-verkon käyttö edellyttää, että käytät Bitcoin:tä kanavan rahoittamiseen. Tämä tarkoittaa sitä, että sinulla on oltava Bitcoin:t on-chain wallet:ssä, joilla voit rahoittaa Lightning-kanavan. Lue lisää Lightning-verkosta tästä [Hacken](https://hacken.io/discover/lightning-network/) artikkelista.


![fund_channel](assets/en/017.webp)


👉 Kirjoita **määrä** Bitcoin:ta, jolla haluat rahoittaa kanavan, tai napsauta **Max**, jos haluat käyttää koko on-chain Bitcoin-saldosi. Voit säätää **maksua** tai jättää oletusmaksuasetuksen ja napsauttaa **Ok**.


**Huomio:** Määrä, jolla rahoitat kanavaa, on uuden kanavasi kapasiteetti (eli Sats:n kokonaisvolyymi, joka voidaan siirtää kanavalle ja kanavalta)


On myös tärkeää, että käytät kanavaa avatessasi rahoitussummana yli **100 000 Sats**. Tämä johtuu siitä, että monet Lightning-solmut vaativat vähintään 100 000 Sats:n kapasiteetin avatakseen kanavan niihin. Jotta vältät kokeilun ja erehdyksen, käytä yksinkertaisesti tätä suurempia summia.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


👉 Kun tarkastat wallet-kotisivusi, näet, että rahoitussummasi on nyt siirretty **Bitcoin-kortilta** **Lightning-kortille**. Tapahtumahistoriassasi näet, että rahoitustapahtumaa käsitellään.


![channel_funding_processing](assets/en/020.webp)


👉 Jos napsautat Lightning-korttia, näet tietoja, jotka osoittavat, että Lightning-kanava on avautumassa. Näet myös **kanavan rahoitustapahtuman** tapahtumaluettelossasi. Odota, että rahoitustapahtuma vahvistetaan blockchain:ssä, ja Lightning-kanavasi on valmis.


![channel_opening](assets/en/021.webp)


👉 Heti kun rahoitustapahtuma on vahvistettu, napsauta etusivulla olevaa **Valokorttia**, jolloin näet seuraavat tiedot Valokuvakanavastasi:



- HARJOITELMA NUMEROITA, jotka on erotettu pisteillä:** Nämä ovat solmujen IP-osoitteita. (IPV4 ja IPV6)
- KAPASITEETTI:** Tämä on Sats:n kokonaismäärä, joka voidaan lähettää ja vastaanottaa tämän kanavan kautta
- VOI LÄHETÄ:** Tämä on Sats:n määrä, jonka voit lähettää tässä vaiheessa. Huomaat, että se on lähes sama kuin **Kapasiteetti**. Tämä johtuu siitä, että et ole lähettänyt yhtään maksua kanavan kautta.
- VOI VASTAANOTTAA:** Tämä on niiden Sats:ien määrä, joita voit vastaanottaa tällä kanavalla tällä hetkellä. (Se on tässä vaiheessa vähän tai ei mitään, koska voidaksesi vastaanottaa sinun on ensin lähetettävä Sats:tä luodaksesi saapuvan Liquidityn)
- PALAUTETTAVA:** Tämä näyttää summan, joka maksetaan takaisin on-chain-osoitteeseesi, kun suljet kanavasi. Tätä kutsutaan myös **kanavasi paikalliseksi saldoksi**. Huomaa, että se on vain hieman pienempi kuin kanavan kapasiteetti, ja tämä johtuu siitä, että kun suljet kanavan, sinun on maksettava maksu sulkemistapahtuman julkaisemisesta blockchain:ssa, aivan kuten teit kanavaa rahoittaessasi. Järjestelmä on siis vähentänyt likimääräisesti pienimmän maksamasi summan)
- VALUE IN FLIGHT:** Kun joku lähettää sats:n kanavallesi tai kun yrität lähettää sats:n jollekin ja jostain syystä tapahtuma viivästyy, se näkyy usein tässä kentässä.


![channel_info](assets/en/022.webp)


## Sats:n lähettäminen kanavasi kautta


Sats:n lähettäminen Lightning Network:n kautta on yksinkertainen tehtävä.


👉 Napsauta etusivun alareunassa **lähettää** ja **liitä** Lightning-lasku (sinun on kopioitava se) sille varattuun kenttään tai napsauta **skannaa** skannataksesi Lightning-laskun QR-koodin.


![click_send_or_scan](assets/en/023.webp)


Useimmissa Lightning-laskuissa on valmiiksi syötetty maksettava summa. Joissakin tapauksissa kyseessä voi kuitenkin olla avoin lasku, johon sinun on täytettävä summa.


👉 Syötä summa **Dollareina** tai **Sats** tai napsauta **Max**, jos haluat käyttää koko salamakanavan saldon, ja napsauta sitten **Ok**. Heti kun hyvä polku on löytynyt, maksusi lähetetään ja suoritetaan loppuun muutamassa sekunnissa. Tarkkaile etusivulla, onko maksu suoritettu. Se saa vihreän valintamerkin, kun se on suoritettu.


![enter_the_amount](assets/en/024.webp)


## Sats:n vastaanottaminen kanavasi kautta


Maksujen vastaanottaminen Lightning-kanavallasi riippuu pitkälti siitä, onko sinulla saapuva Liquidity vai ei. Kun olet avannut kanavan, et voi vastaanottaa maksuja, ennen kuin olet lähettänyt ainakin jonkin Sats:n **luodaksesi saapuvan likviditeetin** kanavayhteyden toiseen päähän. Jos haluat varmistaa, voitko vastaanottaa Sats:tä ja kuinka paljon Sats:tä voit vastaanottaa, tarkista kanavatietojesi **Voi vastaanottaa** -kenttä. Tämä näyttää, kuinka monta Sats:tä voit vastaanottaa kullakin hetkellä.


Oletetaan, että olet lähettänyt Sats:n kanavaltasi, sinulla on nyt saapuvaa likviditeettiä ja voit vastaanottaa Sats:n.


Jotta voit vastaanottaa Lightning-kanavalla, sinun on luotava lasku. Toisin kuin Bitcoin on-chain, joka käyttää osoitteita, Lightning-verkko käyttää laskuja. Valetissa on kaksi reittiä laskun luomiseen.


#### VAIHTOEHTO 1


👉 Klikkaa etusivun alareunassa **Vastaanotto** ja valitse **Vastaanottaa salamalaskulle**. Täytä laskuun vastaanotettava summa ja napsauta **Ok**. Kopioi lasku tai jaa QR-koodi maksajan kanssa.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### VAIHTOEHTO 2


👉 Napsauta violettia Lightning-korttia wallet:n etusivulla. Napauta mitä tahansa kohtaa kanavallasi, jolloin esiin avautuu luettelo vaihtoehdoista. Valitse **Vastaanottaa kanavalle** ja syötä vastaanottamasi summa (joko Sats:na tai dollareina). Näet myös, kuinka monta Sats:ta voit vastaanottaa (saapuva kapasiteetti), kun täytät laskua. Napsauta **Ok** ja kopioi lasku tai jaa QR-koodi maksajan kanssa.


![receive_to_channel](assets/en/028.webp)


**Huomio:** Ensimmäinen vaihtoehto on yleisvalinta, mikä tarkoittaa, että jos sinulla on useampi kuin yksi aktiivinen kanava ja käytät ensimmäistä vaihtoehtoa, järjestelmä valitsee automaattisesti yhden kanavistasi Sats:n vastaanottoa varten.


Tässä skenaariossa toista vaihtoehtoa kannattaa käyttää, jos haluat vastaanottaa Sats:n tietylle kanavalle.


### Kanavasi ponnahdusikkunavaihtoehdot selitetty


Kun napautat kanavaa, seuraavat valintakentät tulevat näkyviin:


![channel_pop_ups](assets/en/029.webp)


**JAKAA LIGHTNING-KANAVAN TIEDOT:** Tämän avulla voit jakaa kanavasi tiedot, kuten etävertaisverkon ID, paikallisen kanavan ID, Rahoitustapahtuma, luontipäivämäärä jne.


**KANAVAN SULKEMINEN PYÖRÄTALLE:** Voit sulkea salamakanavasi milloin haluat. Sulkeaksesi kanavasi järjestelmä tarkistaa Bitcoin-saldon, joka sinulla on omalla puolellasi kanavaa (muista **"Can Send "**-kenttä, joka tunnetaan myös nimellä paikallinen saldosi), ja lähettää sen takaisin sinulle. Valetissa voit valita, minne haluat Bitcoin:n lähetettävän, kun kanava suljetaan. Joten **Sulje kanava wallet:een** on yksi kahdesta vaihtoehdosta.


👉 Napsauta tätä vaihtoehtoa ja valitse **Bitcoin**. Kanavan sulkeminen alkaa, ja kanavasi Bitcoin:n saldo lähetetään takaisin wallet:n on-chain-osoitteeseen.


![close_channel_to_wallet](assets/en/030.webp)


**CLOSE CHANNEL TO ADDRESS:** Tämä on toinen vaihtoehto kanavan sulkemiseksi. Kun valitset tämän vaihtoehdon, sinua pyydetään antamaan wallet-osoite, johon kanavasi Bitcoin-saldo lähetetään. Huomaa, että tässä vaihtoehdossa voit skannata vain sen Bitcoin-osoitteen QR-koodin, johon haluat sulkea kanavan. Tällä hetkellä ei ole mahdollisuutta liittää osoitetta manuaalisesti.


👉 Napsauta tätä vaihtoehtoa, skannaa Bitcoin-osoite ja napsauta **Ok**. Kanavan sulkeminen alkaa, ja Lightning Bitcoin -saldosi lähetetään skannaamaasi osoitteeseen.


![scan_address_and_Ok](assets/en/031.webp)


**VASTAANOTTO KANAVALLE:** Tämä on sama asia kuin laskun luominen, mutta joissakin tapauksissa sinulla voi olla useampi kuin yksi kanava, mukaan lukien Fiat-kanavat (ainutlaatuinen Lightning-kanava, joka on saatavissa Valet wallet:sta). Jos sinulla on siis useita kanavia auki, tämä vaihtoehto varmistaa, että voit vastaanottaa maksun tiettyyn kanavaan.


**TÄYTTÖ MUISTA KANAVISTA:** Tämä vaihtoehto on ominaisuus, jonka avulla voit täyttää yhden kanavan muista olemassa olevista kanavista. Jos sinulla on esimerkiksi kaksi eri Lightning-kanavaa (A ja B) ja kanavan A Bitcoin saldo on tyhjentynyt, voit tämän vaihtoehdon avulla helposti ja automaattisesti täydentää kanavan A saldoa kanavalta B. Tämä vaihtoehto on myös käytettävissäsi.


**Ei yksityisvastaanottoa:** Tämä on myös mahdollisuus luoda lasku maksun vastaanottamista varten, mutta kun käytät tätä vaihtoehtoa, lähettäjä maksaa suoraan sinulle. Tämä tarkoittaa, että maksu ei hyppää eri solmujen läpi ennen kuin se saapuu sinulle, kuten normaali Lightning-maksu. Lähettäjä tietää siis pohjimmiltaan, että hän on maksanut sinulle, tietää kanavatunnuksesi jne. Tätä vaihtoehtoa voidaan usein käyttää, kun saat maksun lähteeltä, johon luotat, eikä sinun tarvitse säilyttää yksityisyyttäsi.


## Isännöidyt ja Fiat-kanavat


Kuten monet muutkin Bitcoin wallet:t, Valet on yksinkertainen, kevyt Bitcoin ja Lightning wallet. Siinä on kuitenkin ainutlaatuinen Lightning-ominaisuus, joka erottaa sen useimmista muista Bitcoin wallet-laitteista. Tämä ominaisuus on nimeltään **Hosted and Fiat Channels**.


Fiat-kanavat ovat eräänlainen Lightning-toteutus, joka mahdollistaa Lightning-verkon helpon käyttöönoton ja käytön. Se on säilytysratkaisu, joka mahdollistaa täyden anonymiteetin, aivan kuten tavallinen Lightning-kanava. Fiat-kanavateknologia mahdollistaa myös Bitcoin-johdannaisten luomisen Lightning-verkossa. Fiat-kanavien avulla kauppiaat voivat esimerkiksi hyväksyä arvoltaan vakaita Bitcoin-maksuja ilman huolta Bitcoin:n volatiliteetista.


Fiat-kanavien nykyinen toteutus Valetissa mahdollistaa vakaiden synteettisten Fiat-valuuttojen luomisen Sats:n tukemana. Se käyttää isäntä-asiakas-suhdetta, jossa isäntä on mikä tahansa Lightning-solmu, joka tarjoaa tätä palvelua, ja asiakas on Valetin käyttäjä. Kyseessä on säilytysratkaisu, koska kaikki Sats on isännän puolella; laskun luominen, tor-reititys ja esikuvan luominen tapahtuvat kuitenkin edelleen asiakkaan puolella, kuten tavallisessa Lightning-kanavassa.


Fiat-kanavan avaaminen tapahtuu samalla tavalla kuin Lightning-kanavan avaaminen. Ainoa merkittävä ero on, että tässä tapauksessa asiakkaan (Valet-käyttäjän) ei tarvitse sitoa likviditeettiä on-chain kanavakapasiteetin luomiseen. Isäntä asettaa kanavakapasiteetin ja reitittää kaikki maksut asiakkaan puolesta.


👉 Voit avata Fiat-kanavan napsauttamalla wallet-kotisivulla olevaa violettia **Valokorttia**. Valitse **Scan Node QR** (Tässä vaiheessa sinun on tunnistettava isäntä, johon haluat avata kanavan, ja saatava solmun QR-koodi. Esimerkki isäntäsolmusta, johon voit avata Fiat-kanavan, on Standard Sats:n SATM-solmu)


**Huomio:** On tärkeää huomata, että kuka tahansa voi olla isäntä. Tarvitset vain Lightning-solmun, jossa on **Fiat-kanavaliitin** ja **Hedging-palvelu**. Fiat-kanavat on *Standard Sats*:n avoimen lähdekoodin projekti. Lue siitä lisää [täällä](https://github.com/standardsats/fiat-channels-rfc) ja [täällä](https://standardsats.github.io/).


SATM-solmu QR alla:


![SATM_node_QR](assets/en/032.webp)


👉 Kun olet skannannut solmun QR-koodin, napsauta **Pyydä USD-fiat-kanavaa** tai **Pyydä EUR-fiat-kanavia** (Tämä on fiat-arvo, jolla Fiat-saldosi noteerataan). Valitse nyt USD ja napsauta **OK**. Kanava avataan automaattisesti, ja voit aloittaa Sats:n vastaanottamisen heti. Näet, se on niin yksinkertaista!!!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉 Mene wallet:n kotisivulle, näet **valonvihreän** kortin, jossa lukee **USD**, se on **Fiat-kanava**.


![fiat_channel_card](assets/en/035.webp)


**Varoitus:** Kun vastaanotat Sats:n Fiat-kanavalla, vastaanottamasi Sats:n fiat-arvo lukitaan vakaana saldona, kun taas Sats:n määrä kelluu Bitcoin:n hinnan mukana. Tämä ratkaisu on suunniteltu lähinnä kauppiaille, jotka haluavat hyväksyä Sats:n maksuvälineeksi, mutta eivät halua kohdata Bitcoin:n volatiliteettihaasteita. Tämä auttaa heitä säilyttämään vakaan arvon koko ajan, mutta voivat silti tehdä liiketoimia Lightning-verkossa ja nauttia Bitcoin:n maailmanlaajuisesta ulottuvuudesta ja nopeasta selvityksestä Lightning Network:n vaihdon välineenä.


Kun Fiat-kanavasi luodaan, näet seuraavat arvokentät ja niiden merkityksen:


![fiat_channel_info](assets/en/036.webp)



- HARJOITELMA NUMEROITA, jotka on erotettu pisteillä:** Nämä ovat solmujen IP-osoitteita. (IPV4 ja IPV6)
- PALVELINHINTA:** Tämä on Bitcoin-markkinahinta, jolla isäntä tarjoaa palveluja sinulle. Tämä poikkeaa usein hieman vallitsevasta markkinahinnasta, koska isäntä voi lisätä pienen lisähinnan. Tämä hinta on täysin isännän päätettävissä, joten se vaihtelee myös isäntäkohtaisesti.
- FIAT SALDO:** Tämä on jokaisen tällä kanavalla vastaanottamasi satelliitin lukittu vakaa fiat-arvo. Muista, kuten aiemmin selitettiin, että aina kun vastaanotat Sats:n Fiat-kanavallasi, Sats:n fiat-arvo vastaanottohetkellä lukitaan välittömästi synteettisenä vakaana fiat-arvona tähän kenttään. **Fiat-saldosi** arvo ei vaihtele Bitcoin:n markkinahinnan mukaan. Aina kun haluat suorittaa maksuja tästä kanavasta, voit lähettää vain tämän Fiat-saldon Sats-arvon. Ajattele tätä siis digitaalisena fiat-valuuttana, jonka takana on Sats.
- KAPASITEETTI:** Tämä on Sats:n kokonaismäärä, joka voidaan lähettää ja vastaanottaa tämän kanavan kautta. (Myös tämä asetetaan isännän toimesta. Ja toisin kuin normaali Lightning-kanava, isäntä voi tarvittaessa säätää tätä kapasiteettia)
- VOI LÄHETÄ:** Tämä on Sats-määrä, jonka voit lähettää kussakin pisteessä fiat-saldosi perusteella. Tämä on täysin erilainen kuin tavallisessa Lightning-kanavassa, koska tämä arvo vaihtelee Bitcoin:n hinnan mukaan. Näin ollen tässä näet fiat-saldosi Sats-arvon joka hetki **Serverkurssin** perusteella.
- VOI VASTAANOTTAA:** Tämä on niiden Sats:ien määrä, joita voit vastaanottaa tällä kanavalla tällä hetkellä. Kun olet luonut kanavan, tämän arvon pitäisi olla sama kuin kanavan kapasiteetti.
- VALUE IN FLIGHT:** Kun joku lähettää sats:n kanavallesi tai kun yrität lähettää sats:n jollekulle, ja jostain syystä tapahtuma viivästyy, se näkyy usein tässä kentässä.


Seuraavassa on tärkeitä asioita, jotka on syytä huomioida Fiat-kanavista:



- Toisin kuin tavallisella Lightning-kanavalla, kun avaat fiat-kanavan, voit heti aloittaa Sats:n vastaanottamisen, mutta et voi lähettää. Voit lähettää Sats:n vasta, kun olet vastaanottanut Sats:n.
- Koko ajan Sats on kohde, johon lähetetään ja josta lähetetään, ja Sats on Sats. *Fiat-saldo* on vain synteettinen IOU-edustus Bitcoin:n arvosta, joka on vastaanotettu minä tahansa ajankohtana. Se ei siis ole token-luomus tai uusi kryptovaluutta.
- Fiat-kanava on hyödyllinen lähinnä kauppiaille/yrityksille, jotka suhtautuvat epäilevästi Bitcoin-maksujen hyväksymiseen volatiliteettiin liittyvien huolien vuoksi. Se voi olla hyödyllinen myös yrityksille, jotka haluavat maksaa työntekijöidensä palkat Bitcoin:ssä kantamatta Bitcoin:n volatiliteetin seurauksia, jotka voivat tehdä palkkapääomasta epävakaan. Se voi olla hyödyllinen myös yksityishenkilöille, jotka asuvat alueella, jossa Bitcoin:tä käytetään yleisesti, mutta joilla on kiinteät elinkustannukset.
- Huomaa, että kentässä ei ole merkintää **RAHOITTAVA**. Tämä johtuu siitä, että teknisesti Fiat-kanavaa ei voi sulkea. Voit lopettaa Fiat-kanavan käytön vain tyhjentämällä sen saldon normaaliin Lightning-kanavaan.


### Fiat-kanavan ponnahdusikkunan vaihtoehdot selitettyinä


Kun napautat Fiat Lightning -kanavaa, seuraavat kentät tulevat näkyviin:


![fiat_channel_pop_up](assets/en/037.webp)


**JAKA HOSTED CHANNEL DETAILS:** Tämän avulla voit jakaa Fiat-kanavasi tiedot, kuten etäverkon ID, paikallisen kanavan ID, luontipäivämäärä jne.


**KANAVAN TILAN VIENTI:** Tämän avulla voit viedä kanavan tilan missä tahansa vaiheessa. Tästä on yleensä hyötyä kanavavirheiden korjaamisessa, ja isäntä voi pyytää sinua jakamaan tämän, jos sille on tarvetta.


**KANAVAN TASAPAINO:** Kuten aiemmin mainittiin, et voi teknisesti sulkea Fiat-kanavaa, mutta voit tyhjentää kanavasi saldon olemassa olevaan normaaliin Lightning-kanavaan. Tämä siirtää automaattisesti Fiat-saldosi Sat-saldon normaaliin Lightning-kanavaan.


**VASTAANOTTO KANAVALLE:** Tämä on sama asia kuin laskun luominen, mutta joissakin tapauksissa käyttäjällä voi olla useampi kuin yksi Fiat-kanava eri isännillä, mukaan lukien normaalit Lightning-kanavat. Jos käyttäjällä on siis useita kanavia auki, tämä vaihtoehto varmistaa, että hän voi vastaanottaa maksun tiettyyn kanavaan.


**TÄYTTÖ MUISTA KANAVISTA:** Tämä vaihtoehto on ominaisuus, jonka avulla käyttäjä voi täyttää yhden kanavan muista olemassa olevista kanavista. Tämän vaihtoehdon avulla voit siis täyttää Fiat-kanavasi uudelleen normaalista kanavasta tai muista Fiat-kanavista, jotka sinulla on, aivan samalla tavalla kuin voit tyhjentää kanavan.


**Ei yksityisvastaanottoa:** Tämä on myös mahdollisuus luoda lasku maksun vastaanottamista varten, mutta kun käytät tätä vaihtoehtoa, lähettäjä maksaa suoraan sinulle. Tämä tarkoittaa, että maksu ei hyppää eri solmujen kautta ennen kuin se saapuu sinulle. Lähettäjä tietää siis pohjimmiltaan, että se olet sinä, jolle se on maksanut, tietää kanavatunnuksesi jne. Tätä vaihtoehtoa voidaan usein käyttää, kun saat maksun lähteeltä, johon luotat, eikä sinun tarvitse säilyttää yksityisyyttäsi.


## Valet-asetukset:


Kuten kaikissa muissakin sovelluksissa, Valetissa on sovelluksen asetukset, joita voit säätää oman makusi mukaan. Pääset asetussivulle aloitusnäytöstä.


👉 Pääset asetuksiin napsauttamalla aloitusnäytössä näytön oikeassa yläkulmassa olevaa **Gear**-kuvaketta. Alla on lueteltu asetukset-osion osat.


![settings_icon](assets/en/038.webp)


**LOCAL CHANNEL BACKUP IS ENABLED:** Jos tämä on muuten **Disabled,** sinun pitäisi ottaa se käyttöön, koska tämä on ainoa tapa palauttaa normaalit Lightning-kanavat, jos poistat ja asennat Valetin uudelleen. Selitämme tämän myöhemmin. Napsauta tätä ja anna Valetille oikeudet **mediatallennustilaan**, koska varmuuskopiotiedosto on tallennettu sinne.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**MIKSI TALLENNETAAN PAIKALLINEN VARMUUSKOPIO:** Kun olet antanut Valetille oikeuden tallennustilaan, tämä kenttä asetetaan automaattisesti tallentamaan paikalliset varmuuskopiot **Lataukset**-kansioon. Voit kuitenkin muuttaa sitä napsauttamalla tätä ja valitsemalla minkä tahansa haluamasi kansion.


**HALLITSE KETJUVAATTEITA** Tämä on hieman teknistä, eikä sinun tarvitse välittää tästä, ellet ole tarpeeksi kokenut. Oletusasetus tässä on aivan hyvä.


**ADD HARDWARE WALLET:** Sinun ei myöskään kannata huolehtia tästä, ellei sinulla ole laitteistoa wallet, jonka haluat liittää ja valvoa. Tällä asetuksella voit skannata ja liittää laitteistosi wallet:n, kuten Trezor- tai Cold-kortin, ja seurata sen toimintaa. Tämä on vain tarkkailutoiminto, mikä tarkoittaa, että et voi suorittaa tapahtumia laitteiston wallet:lla tästä. Voit vain tarkkailla ja seurata wallet:n toimintoja, saldoja jne.


**SET CUSTOM ELECTRUM NODE:** Tämäkin on tekninen asia, ja jos et ole tarpeeksi asiantunteva, sinun ei kannata vaivautua tämän kanssa. Oletusasetus riittää.


**BITCOIN UNITS:** Näin haluat Bitcoin-saldosi näkyvän. Ensimmäinen vaihtoehto näyttää saldosi Satoshi:nä, esim. 1,000,000 Sats, kun taas toinen vaihtoehto näyttää sen BTC:n desimaalipisteinä, esim. 0.01BTC


**KÄYTÄ PIN-TUNNISTUSTA** Jos ruksaat tämän valintaruudun, sinun on määritettävä PIN-koodi tai sormenjälki, jolla sinun on kirjauduttava sisään wallet-laitteeseen ja todennettava tapahtumat.


**KÄYTÄ TOR-YHTEYTTÄ:** Jos valitset tämän ruudun, tapahtumasi ohjataan Tor-verkon kautta. Se lisää yksityisyyden suojaa, mutta saattaa viivästyttää maksujen läpimenoa, erityisesti Lightning-maksujen osalta.


**VIEW BIP39 RECOVERY PHRASE:** Täältä voit käyttää 12-sanaista seed-lausetta varmuuskopiointia varten. Joten jos et ole kirjoittanut sitä aiemmin tai et löydä, mihin kirjoitit sen, voit kopioida sen täältä, kunhan sinulla on vielä pääsy Wallet-lauseeseesi.


**KÄYTTÖTILASTOT:** Tämä näyttää yhteenvedon kaikista tapahtumista ja toiminnoista wallet:n luomisen jälkeen


![usage_stats](assets/en/041.webp)


## Wallet Talteenotto


Valet ei ole wallet:n säilytysjärjestelmä, joten jos kadotat laitteesi tai poistat wallet-sovelluksen, sinun on suoritettava wallet:n palautus saadaksesi Bitcoin- ja Lightning-kanavasi takaisin. Tämän ohjeen alussa mainitsimme, että on tärkeää kirjoittaa ylös **12-sanainen seed-lauseesi**, koska se on avain wallet:n palauttamiseen. Asiakaspalvelun edustajat eivät voi auttaa sinua pääsemään takaisin wallet:een.


Valet wallet -laitteen palauttamiseen tarvitaan kaksi tärkeää työkalua riippuen siitä, oliko Lightning-kanava aktiivinen vai ei. Käyttäjä, jolla ei ollut aktiivista normaalia Lightning-kanavaa, tarvitsee vain **12-sanaisen seed-lauseen** ja noudattaa alla olevia yksinkertaisia ohjeita:


👉 Asenna uusi Valet-sovellus ja käynnistä sovellus.


👉 Valitse **Varmistaa olemassa oleva Wallet**


![restore_existing_wallet](assets/en/042.webp)


👉 Valitse **vain palautuslause**.


![select_recovery_phrase](assets/en/043.webp)


👉 Syötä 12-sanainen palautuslauseesi ja napsauta **OK**.


![input_12_words](assets/en/044.webp)


wallet:nne saadaan takaisin. Tässä tapauksessa vain on-chain Bitcoin-saldosi palautetaan.


Jos sinulla oli kuitenkin aktiivinen normaali salamakanava ja palautat wallet:n pelkällä palautuslauseella, salamakanava suljetaan väkisin, ja kaikki Bitcoin-saldosi siirretään automaattisesti on-chain-saldoosi.


Toinen tapa palauttaa Valet wallet, varsinkin jos sinulla oli normaali Lightning-kanava auki ennen Valetin poistamista, on **käyttää laitteeseen tallennettua paikallista varmuuskopiotiedostoa ja 12-sanaista seed-lauseesi**. Jos käytät näitä kahta, Lightning-kanavasi tila palautuu, joten Lightning-kanavaasi ei suljeta väkisin.


Tässä ovat vaiheet:


👉 Asenna uusi Valet-sovellus ja käynnistä sovellus.


👉 Valitse **Varmistaa olemassa oleva Wallet**.


👉 Valitse **Backup + Recovery -lause**.


![select_backup_and_recovery_seed](assets/en/045.webp)


👉 Valitse varmuuskopiotiedosto puhelimen tiedostonhallinnasta. (Se on aina oletusarvoisesti tallennettu **Lataukset**-kansioon)


![local_backup_file_in_download_folder](assets/en/046.webp)


Kun oikea varmuuskopiotiedosto on valittu, näyttöön tulee kehote, jossa vahvistetaan, että **"Varmuuskopiotiedosto on olemassa "**, ja sen jälkeen sinua pyydetään syöttämään 12-sanainen seed-lause.


![enter_12_words](assets/en/047.webp)


👉 Kirjoita 12-sanainen palautuslauseke ja napsauta **OK**. Sinut siirretään wallet:n kotisivulle.


👉 Odota, että Bitcoin-verkon synkronointi (**SYNC**) ja Lightning-solmun synkronointi (**LN Sync**) on valmis, ja wallet palautuu täysin, Lightning-kanavat mukaan lukien.


![LN_sync](assets/en/048.webp)


## Päätelmä


Valet on jännittävä wallet-ratkaisu, jonka ominaisuudet tekevät siitä sopivan uusien käyttäjien perehdyttämiseen. Siinä on myös Fiat-kanava, joka ei ole aivan uusi tekniikka, jolla varmistetaan fiat-yritysten integrointi Bitcoin-standardiin.


Lataa Valet jo tänään ja kokeile sitä!!!! 🧡