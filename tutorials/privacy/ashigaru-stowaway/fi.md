---
name: Ashigaru - Salamatkustaja
description: Miten teen Payjoin-tilisiirron Ashigarussa?
---
![cover](assets/cover.webp)



> *Pakottaa lohkoketjuvakoilijat miettimään uudelleen kaikkea, mitä he luulevat tietävänsä.*

Payjoin on Bitcoin-tapahtumarakenne, joka on suunniteltu parantamaan käyttäjän luottamuksellisuutta tekemällä suoraa yhteistyötä maksun vastaanottajan kanssa. Useita toteutuksia on olemassa sen toteuttamisen helpottamiseksi ja prosessin automatisoimiseksi. Tunnetuin niistä on epäilemättä Stowaway, jonka alun perin kehitti Samurai Wallet -tiimi ja joka on nyt integroitu sen fork Ashigaruun.



## Miten Stowaway toimii?



Kuten aiemmin mainittiin, Ashigaru integroi PayJoin-työkalun nimeltä `Stowaway`. Tämä on saatavilla Androidin Ashigaru-sovelluksessa. Jotta Payjoin voidaan suorittaa, vastaanottajan (joka toimii myös yhteistyökumppanina) on käytettävä Stowawayn kanssa yhteensopivaa ohjelmistoa, eli tällä hetkellä vain Ashigarua.



Salamatkustaja perustuu liiketoimien luokkaan, jota Samurai kutsui nimellä "Cahoots". Cahoot on useiden käyttäjien välinen yhteistoiminnallinen transaktio, jossa vaihdetaan tietoja Bitcoin-lohkoketjun ulkopuolella. Ashigaru tarjoaa tällä hetkellä kaksi Cahoots-työkalua: Stowaway (Payjoins) ja StonewallX2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Cahoots-tapahtumat edellyttävät osittain allekirjoitettujen tapahtumien vaihtoa käyttäjien välillä. Tämä prosessi voi olla pitkä ja työläs, varsinkin jos se suoritetaan etänä. Se on kuitenkin mahdollista tehdä manuaalisesti, jos yhteistyökumppanit ovat samassa paikassa. Konkreettisesti tämä tarkoittaa viiden QR-koodin skannaamista peräkkäin, jotka vaihdetaan kahden osallistujan välillä.



Etäisyydellä tästä menetelmästä tulee liian monimutkainen. Tämän korjaamiseksi Samourai on kehittänyt Tor-pohjaisen salatun viestintäprotokollan nimeltä "*Soroban*". Sorobanin ansiosta Payjoinin edellyttämät vaihdot automatisoituvat ja tapahtuvat taustalla.



Nämä salatut viestit edellyttävät yhteyttä ja todennusta Cahootin osallistujien välillä. Siksi Soroban luottaa käyttäjien Paynymeihin. Jos et vielä tiedä, miten Paynyms toimii, tutustu tähän omaan opetusohjelmaan saadaksesi lisätietoja:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

Lyhyesti sanottuna Paynym on wallet:een liittyvä yksilöllinen tunniste, jonka avulla voit aktivoida erilaisia toimintoja, kuten salattuja vaihtoja. Se on muodoltaan tunniste, johon liittyy kuva. Tässä on esimerkiksi Testnet:ssä käyttämäni tunnus:



![Image](assets/fr/01.webp)



**Yhteenvetona:**





- payjoin" = Erityinen yhteistapahtumarakenne;





- `Stowaway` = Payjoin-toteutus saatavilla Ashigarussa;





- `Cahoots` = Samourain antama nimi kaikentyyppisille yhteistyötoiminnoille, erityisesti Payjoin `Stowaway`, joka on otettu käyttöön Ashigarussa;





- soroban = Toriin perustettu salattu viestintäprotokolla, joka mahdollistaa yhteistyön muiden käyttäjien kanssa `Cahoots`-tapahtumassa;





- paynym" = Yksilöllinen wallet-tunniste, jota käytetään yhteydenpitoon toisen Soroban-käyttäjän kanssa "Chahoots-tapahtuman" suorittamiseksi.



Jos haluat syvällisemmän katsauksen Payjoinsin toimintaan ja niiden hyödyllisyyteen onchain-yksityisyyden suojaamisessa, suosittelen tätä toista opetusohjelmaa:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Miten voin luoda yhteyden Paynymien välille?



Aloittaaksesi sinun täytyy tietenkin asentaa Ashigaru ja luoda :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Jos haluat suorittaa etäkäyttöön tarkoitetun Cahoots-tapahtuman, mukaan lukien PayJoin (*Stowaway*) Ashigarun kautta, sinun on ensin "seurattava" käyttäjää, jonka kanssa haluat tehdä yhteistyötä, käyttämällä hänen Paynym-käyttäjäänsä. Salamatkustajan tapauksessa tämä tarkoittaa sen henkilön seuraamista, jolle haluat lähettää bitcoineja. Jos et vielä tiedä, miten seurata toista Paynymiä, löydät yksityiskohtaisen menettelyn tästä opetusohjelmasta :



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Miten teen Payjoinin Ashigarussa?



Jos haluat suorittaa Stowaway-tapahtuman, napsauta näytön vasemmassa yläkulmassa olevaa Paynym-kuvasi kuvaa ja avaa sitten "Yhteistyö"-valikko. Tapahtumaan kanssasi osallistuvan henkilön on tehtävä samoin, ellette vaihda QR-koodeja henkilökohtaisesti.



![Image](assets/fr/02.webp)



Sinulla on kaksi vaihtoehtoa: valitse "Aloita", jos olet maksun lähettäjä, tai "Osallistu", jos olet tämän maksuliittymän maksunsaaja.



![Image](assets/fr/03.webp)



Jos olet vastaanottaja, menettely on hyvin yksinkertainen. Jos haluat tehdä etäyhteistyötä Soroban-verkon kautta, klikkaa `Osallistu`, valitse tili, jota haluat käyttää, ja paina sitten `LISTEN FOR CAHOOTS REQUESTS` odottaaksesi maksajan lähettämää pyyntöä.



![Image](assets/fr/04.webp)



Jos taas haluat tehdä henkilökohtaista yhteistyötä QR-koodin skannauksen avulla, siirry wallet:n etusivulle, paina näytön yläreunassa olevaa QR-koodi-kuvaketta ja skannaa sitten maksutapahtuman aloittavan maksajan antama QR-koodi.



![Image](assets/fr/05.webp)



Jos olet maksajan roolissa, eli olet se, joka aloittaa tapahtuman, siirry "Yhteistyö"-valikkoon ja valitse sitten "Aloita".



![Image](assets/fr/06.webp)



Koska haluamme tehdä Payjoin Stowaway -maksun, valitse tapahtumatyypiksi tämä vaihtoehto.



![Image](assets/fr/07.webp)



Tämän jälkeen voit valita joko online-yhteistyön (*Cahoots* *Sorobanin* kautta) tai kasvokkain tapahtuvan yhteistyön QR-koodien vaihdon avulla.



![Image](assets/fr/08.webp)



### Cahoots verkossa



Jos olet valinnut "Online"-vaihtoehdon, valitse vastaanottaja seuraamistasi Paynymeistä.



![Image](assets/fr/09.webp)



Napsauta `Set up transaction` ja valitse sitten tili, jolta haluat tehdä menon.



![Image](assets/fr/10.webp)



Kirjoita seuraavalla sivulla tapahtuman tiedot: vastaanottajalle lähetettävä summa ja veloitusmaksu. Vastaanottajan osoitetta ei tarvitse syöttää, sillä vastaanottaja lähettää sen itse PSBT-vaihdon aikana.



Napsauta sitten `Review transaction setup`.



![Image](assets/fr/11.webp)



Tarkista tiedot huolellisesti, varmista, että yhteistyökumppanisi kuuntelee *Cahoots*-pyyntöjä, ja napsauta sitten vihreää `BEGIN TRANSACTION` -painiketta aloittaaksesi PSBT:iden vaihdon Sorobanin kautta.



![Image](assets/fr/12.webp)



Odota, kunnes molemmat osallistujat ovat allekirjoittaneet tapahtuman, ja lähetä se sitten Bitcoin-verkkoon.



![Image](assets/fr/13.webp)



### Henkilökohtaiset keskustelut



Jos haluat suorittaa vaihdon henkilökohtaisesti, valitse tapahtumatyyppi "STONEWALL X2" ja valitse sitten vaihtoehto "Henkilökohtaisesti / Manuaalisesti".



![Image](assets/fr/14.webp)



Napsauta `Set up transaction` ja valitse sitten tili, jolta haluat tehdä menon.



![Image](assets/fr/15.webp)



Kirjoita seuraavalla sivulla tapahtuman tiedot: vastaanottajalle lähetettävä summa ja veloitusmaksu. Vastaanottajan osoitetta ei tarvitse syöttää, sillä vastaanottaja lähettää sen itse PSBT-vaihdon aikana.



Napsauta sitten `Review transaction setup`.



![Image](assets/fr/16.webp)



Tarkista tiedot ja paina sitten vihreää `BEGIN TRANSACTION` -painiketta aloittaaksesi PSBT:iden vaihtamisen QR-koodin skannauksen avulla.



![Image](assets/fr/17.webp)



Vaihto tapahtuu skannaamalla vuorotellen yhteistyökumppanin kanssa: napsauta `NÄYTÄ QR-KOODI` näyttääksesi QR-koodisi yhteistyökumppanillesi, joka skannaa sen. Tämän jälkeen hän napsauttaa `NÄYTÄ QR-KOODI` näyttääksesi omansa, ja sinä skannaat sen `LAUNCH QR Scanner` -ohjelmalla. Toista tätä prosessia, kunnes kaikki viisi vaihtovaihetta on suoritettu.



![Image](assets/fr/18.webp)



Kun kaikki vaihdot on suoritettu, tarkista tapahtuman tiedot ja vapauta se vetämällä näytön alareunassa olevaa vihreää nuolta.



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). Sen rakenne on seuraava:



![Image](assets/fr/20.webp)



*Luotto: [mempool.space](https://mempool.space/)*



Jos analysoimme tätä tapahtumaa, näemme tulopuolella tuloni UTXO, joka on 164 211 sats, sekä UTXO, joka on 190 002 sats ja joka kuuluu maksun varsinaiselle vastaanottajalle. Lähtöpuolella minä saan vaihdossa UTXO:n, joka on 63 995 sats, kun taas vastaanottaja saa UTXO:n, joka on 290 002 sats. Verrattaessa panoksia ja tuotoksia voidaan todeta, että vastaanottaja on todellakin ansainnut 100 000 sats`, mikä vastaa todellisen maksuni määrää, ja että minä olen menettänyt 100 000 sats`, johon olen lisännyt mining-kustannukset.



Voin luonnollisesti kuvata tämän rakenteen, koska olen rakentanut tapahtuman itse. Ulkopuolisen tarkkailijan on kuitenkin yleensä mahdotonta määrittää, mitkä UTXO:t kuuluvat millekin osallistujalle joko tuloissa tai lähdöissä.



Jos haluat syventää tietämystäsi Bitcoin:n onchain-yksityisyyden hallinnasta, suosittelen, että osallistut BTC 204 -koulutukseeni Plan ₿ Academyssa:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c