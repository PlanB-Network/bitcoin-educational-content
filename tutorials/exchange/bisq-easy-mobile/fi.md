---
name: Bisq Easy Mobile
description: Vertaisvertaiskaupankäyntiprotokolla uusille bitcoin-käyttäjille - ei välikäsiä, ei KYC:tä.
---
![cover](assets/cover.webp)


## Johdanto


[Bisq Easy](https://bisq.network/bisq-easy/) -kauppaprotokolla on suunniteltu [Bisq 2](https://github.com/bisq-network/bisq2) -kauppaprotokollalle, joka on [Bisq v1](https://github.com/bisq-network/bisq) -kauppaprotokollan seuraaja. Bisq 2 tukee useita kauppaprotokollia, yksityisyysverkkoja ja identiteettejä. Se helpottaa Bitcoin:n ostamista ilman kaupankäyntimaksuja ja ilman vakuusvaatimusta. Se on tarkoitettu uusille Bitcoin:n ostajille, jotka etsivät vaihtoehtoa, jossa ei ole KYC-vaihtoehtoa, ja jotka haluavat, että kokeneet ja asiantuntevat myyjät, jotka tuntevat Bisq-alustan, ottavat heidät tehokkaasti käyttöön.


Bisq Easy on tällä hetkellä Bisq 2:n ainoa kauppamenettely. Tulevaisuudessa on suunnitteilla lisää kauppaprotokollia. Lue lisää Bisq 2:stä tästä opetusohjelmasta:


https://planb.academy/tutorials/exchange/peer-to-peer/bisq-v2-c1c6a702-6c16-4101-8b90-62c424017b80

Tämä lyhyt opas täydentää yllä olevaa ohjetta Bitcoin:n ostamisesta [Bisq Easy Mobile] (https://github.com/bisq-network/bisq-mobile) -sovelluksen ja Lightningin avulla.


## 1️⃣ Aloittaminen


Aloita lataamalla Bisq Easy Mobile [lataussivulta](https://bisq.network/downloads/). On suositeltavaa tarkistaa lataus. Varmennusohjeet löytyvät myös [lataussivulta](https://bisq.network/downloads/). Asennuksen jälkeen sinun on hyväksyttävä `Käyttäjäsopimus`. Luo seuraavaksi julkinen profiili, joka koostuu `nickname`-nimestä ja avatarista (jota edustaa `bot-kuvake`). Bisq Easy -ohjelmalla voit myös luoda useita käyttäjäprofiileja samaan asiakkaaseen. Lyhyen alustuksen jälkeen pääset `Kotinäyttöön`. Sovellus korostaa opetusmateriaalia suoraan pääsivulla. Napauta `Open Trade Guide` tutustuaksesi uusimpiin tietoihin.


![image](assets/en/01.webp)


Kauppaoppaassa selitetään kaikki olennainen helpoissa vaiheissa:



- Miten käydä kauppaa Bisq Easy -palvelussa
- Miten kaupantekoprosessi toimii
- Mitä minun on tiedettävä kauppasäännöistä.


Toinen tärkeä osio on **"Kuinka turvallista on käydä kauppaa Bisq Easyllä? "**


![image](assets/en/08.webp)


Merkitse rasti ruutuun "Olen lukenut ja ymmärtänyt" ja napauta "Viimeistele".


![image](assets/en/02.webp)


## 2️⃣ Varmuuskopioi tietosi


Ennen kuin aloitamme, hoidetaan muutama siivoustehtävä ja luodaan varmuuskopio tallennustiedostostasi. Siirry kohtaan `Lisää` > `Backup & Restore` tallentaaksesi profiilisi ja kauppahistoriasi. Jos menetät laitteesi ilman varmuuskopiota, maineesi ja käynnissä olevat kaupat eivät ole palautettavissa. Anna `Salasana` salataksesi varmuuskopiosi.


![image](assets/en/11.webp)


## 3️⃣ Tarjoukset


"Aloitusnäytöltä" voit siirtyä tarjouksiin kahdella tavalla. Napauta näytön keskellä olevaa kohtaa "Tutustu tarjouksiin" tai napauta alavalikossa olevaa kohtaa "Tarjoukset". Valitse sieltä valuutta, jolla haluat käydä kauppaa.


![image](assets/en/03.webp)


Toisin kuin [Bisq 1] (https://planb.academy/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04), joka edellyttää vakuutta, Bisq Easy luottaa vakuudeksi ainoastaan myyjän maineeseen. Vaikka tämä lähestymistapa antaa ostajille mahdollisuuden ostaa Bitcoin:ta ensimmäistä kertaa ilman aiempaa omistusta, se asettaa suuren luottamuksen myyjän kykyyn toimittaa Bitcoin sen jälkeen, kun hän on saanut fiat-maksut. Sen vuoksi Bisq Easy -turvamalli on optimoitu vain pienille kauppasummille, ja kaupat on rajoitettu 600 Yhdysvaltain dollarin vasta-arvoon transaktiota kohti riskin minimoimiseksi. Valitse `Offerbook`-osiossa suodattimet maksutapoja ja selvitystä varten Lightning tai Bitcoin (on-chain).


![image](assets/en/04.webp)


Kun olet soveltanut "suodattimia", valitse sopiva tarjous hyvämaineiselta kauppakumppanilta. Myyjän ennalta valitsema maksutapa ja maksutapa (`Lightning` tai `on-chain`) näytetään. Varmista, että nämä vastaavat mieltymyksiäsi, ennen kuin jatkat. Valitsemme tässä Lightning ⚡ -vaihtoehdon.


![image](assets/en/05.webp)


Tarkista ja vahvista kaupan yksityiskohdat napauttamalla `Vahvista tarjous`. Tämän jälkeen ponnahdusikkuna vahvistaa, että olet ottanut tarjouksen onnistuneesti. Napauta Näytä kauppa kohdassa `Open Trades`. Liitä Open Trades (Avoimet kaupat) -osiossa `Lightning-laskusi` ja napauta `Lähetä myyjälle` jakaaksesi sen. Odota nyt myyjän maksutilitietoja. Myyjiltä voi kestää jonkin aikaa vastata. Tarkista säännöllisesti päivitykset chat-ikkunasta.


![image](assets/en/06.webp)


Lähetä lyhyt tervehdys chatissa. Myyjä jakaa maksutiedot, kun hän tulee verkkoon


![image](assets/en/09.webp)


Kun olet saanut tarvittavat maksutiedot myyjältä, jatka maksun suorittamista. Napauta sen jälkeen `Vahvista, että olet suorittanut maksun`-painiketta ja odota kärsivällisesti vastaanottovahvistusta. ️ ⌛️


Kun myyjä vahvistaa maksun vastaanottamisen, myös sinun on vahvistettava Bitcoin:n vastaanottaminen. Näin osto Bisq:lla Easy Mode -tilassa on valmis. Onnittelut! Voit nyt napauttaa `Sulje kauppa`-painiketta.


![image](assets/en/10.webp)


## 4️⃣ Riitojenratkaisu Bisq:ssä helppoa


Jos kaupassa menee jokin pieleen, sekä ostajat että myyjät voivat pyytää sovittelutukea.


**Mitä sovittelijat voivat tehdä:**

- Auttaa helpottamaan kaupan onnistunutta loppuunsaattamista

- Varmista fiat-, altcoin- ja Bitcoin-maksut

- Peruuta kaupat tarvittaessa

- Ilmoita vakavista sääntörikkomuksista moderaattoreille mahdollisia käyttökieltoja varten


**Rangaistukset vilpillisille myyjille:**

Riippuen niiden maineen tyypistä:



- BSQ Bondin maine**: DAO voi takavarikoida joukkovelkakirjalainan BSQ:n
- Sipuli Address Maine**: Heidän Bisq 1 sipuliosoitteensa voidaan kieltää


**Tärkeä huomautus:** Koska kaikki maine on sidottu käyttäjäprofiiliisi, bannaus poistaa maineesi kokonaan.


## 5️⃣ Luo oma tarjous


Sen sijaan, että ottaisit vastaan olemassa olevia tarjouksia, voit luoda oman ostotarjouksen ja antaa myyjien tulla luoksesi. Tämä on oikea vaihtoehto, jos et löydä oikean preemion tai maksutavan mukaisia tarjouksia markkinoilla, joilla haluat käydä kauppaa, mutta sinun on kuitenkin odotettava, että myyjä hyväksyy tarjouksen.


Napauta "Tarjoukset"-näytössä oikeassa alakulmassa olevaa vihreää "+"-kuvaketta. Valitse sitten `Osta Bitcoin` ja valitse fiat-valuutta.


Aseta kaupankäynnin parametrit:



- Kiinteä määrä tai vaihteluväli**: Valitse, kuinka paljon haluat käyttää.
- Maksutapa**: Valitse käytettävissä olevista vaihtoehdoista
- Selvitys**: Valitse Salama ⚡ tai ₿ on-chain


Tarkista tietosi ja napauta `Luo tarjous`. Tarjouksesi näkyy nyt tarjouskirjassa.


![image](assets/en/07.webp)


*Huomautus: Bisq Easy -palvelun ostajana et tarvitse mainetta - tämä on tärkein etu. Myyjät kantavat maineen vaatimuksen ja riskin, minkä vuoksi he veloittavat palkkioita. Tarjouksesi on vain hinnoiteltava tarpeeksi houkuttelevasti, jotta hyvämaineiset myyjät ottavat sen huomioon.*


Kun se on julkaistu, odota "tarjouskirja"-osiossa. Kun myyjä hyväksyy tarjouksesi, saat ilmoituksen. Avaa kauppa kohdassa `Open Trades`, jossa myyjä ja sinä voitte vaihtaa maksutiedot. Lähetä Bitcoin-osoitteesi tai Lightning-lasku myyjälle. Kun olet lähettänyt fiatin, vahvista maksu. Kun myyjä on vahvistanut maksun vastaanottamisen, hän vapauttaa Bitcoin:t kaupan loppuun saattamiseksi.


## 🎯 Päätelmät


Bisq Easy mahdollistaa Bitcoin-ostot ilman vakuuksia, mikä ratkaisee uusien ostajien klassisen kanan ja munan ongelman. Vaihtoehto on selvä: luotat myyjän maineeseen lukittujen varojen sijaan. Tämä luottamukseen perustuva lähestymistapa selittää tyypillisen 5-15 prosentin preemion, joka korvaa hyvämaineisten myyjien investoinnit luottamuksen rakentamiseen ja tuen tarjoamiseen. Vaikka järjestelmä rajoittaa kaupat pieniin summiin mahdollisten tappioiden hillitsemiseksi, pidä aina kiinni myyjistä, joilla on hyvä maine. Uusille tulokkaille, jotka ovat valmiita hyväksymään nämä ehdot, Bisq Easy tarjoaa helpon pääsyn Bitcoin:een.


## 📚 Bisq Helppo mobiiliresurssit


[Github](https://github.com/bisq-network/bisq-mobile) | [Verkkosivusto ](https://bisq.network/bisq-easy/)| [Wiki](https://bisq.wiki/Bisq_Easy)