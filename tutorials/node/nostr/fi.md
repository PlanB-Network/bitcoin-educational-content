---
name: NOSTR

description: Tutustu ja aloita NOSTR:n käyttö
---


![Uusi haastaja on saapunut](assets/1.webp)

*Tämän oppaan lopussa ymmärrät, mitä Nostr on, olet luonut tilin ja pystyt käyttämään sitä.*

## Mikä on Nostr?

Nostr on protokolla, jolla on voima korvata Twitter, Telegram ja muut sosiaalisen median alustat. Se on yksinkertainen avoin protokolla, joka kykenee luomaan maailmanlaajuisesti vastustuskykyisen sosiaalisen verkoston kerralla ja kaikille.

## Miten se toimii?

Nostr perustuu kolmeen komponenttiin: avainpareihin, asiakasohjelmiin ja välityspalvelimiin.

Jokaisella käyttäjällä on yksi tai useampi identiteetti, ja jokainen identiteetti määräytyy kryptografisen avainparin perusteella.

Verkkoon päästäksesi sinun on käytettävä asiakasohjelmistoa ja yhdistettävä välityspalvelimiin sisällön vastaanottamiseksi ja lähettämiseksi.

![Avainjärjestelmä](assets/2.webp)

## 1. Kryptografiset avaimet

Toisin kuin Facebookissa tai Twitterissä, missä käyttäjien on annettava sähköpostiosoite ja paljon tietoja yksityiselle yritykselle, Nostr toimii ilman keskitettyä auktoriteettia. Käyttäjät tuottavat kryptografisen avainparin, salaisen avaimen (tunnetaan myös nimellä yksityinen avain) ja julkisen avaimen.

Salainen avain, nsec, joka on vain käyttäjän tiedossa, käytetään todentamiseen ja sisällön julkaisemiseen.

Julkinen avain, npub, on ainutlaatuinen tunniste, johon kaikki käyttäjän julkaisema sisältö liitetään. Julkinen avain on kuin käyttäjänimi, joka mahdollistaa muiden käyttäjien löytää sinut ja tilata Nostr-syötteesi.

## 2. Asiakasohjelmat

Asiakasohjelmat ovat ohjelmistoja, jotka mahdollistavat vuorovaikutuksen Nostrin kanssa. Pääasiakasohjelmat ovat:

- iOS: damus
- Android: amethyst
- Web: iris.to; snort.social; astral.ninja

Asiakasohjelmat mahdollistavat käyttäjille uuden avainparin luomisen (vastaa tilin luomista) tai olemassa olevan avainparin avulla todentautumisen.

## 3. Välityspalvelimet

Välityspalvelimet ovat yksinkertaisia palvelimia, jotka voit hylätä milloin tahansa, jos et pidä niiden sinulle toimittamasta sisällöstä. Voit myös ajaa oman välityspalvelimesi, jos haluat.

> 💡 Pro vinkki: Maksulliset välityspalvelimet ovat yleensä tehokkaampia suodattamaan roskapostia ja ei-toivottua sisältöä.

## Opas

Nyt tiedät tarpeeksi Nostrista aloittaaksesi ja luodaksesi ensimmäisen identiteettisi tällä protokollalla.

Tämän oppaan tarkoituksessa käytämme iris.to (https://iris.to/) sivustoa, koska tämä web-asiakasohjelma toimii millä tahansa alustalla.

## Vaihe 1: Avainten luominen

Iris luo sinulle avainparin tekemättä muuta kuin syöttämällä nimen (oikea tai kuvitteellinen) profiilillesi. Klikkaa sitten GO ja olet valmis!

![Päävalikko](assets/3.webp)

> ⚠️ Huomio! Sinun on pidettävä avaimistasi huolta, jos haluat pystyä pääsemään profiiliisi uudelleen istunnon sulkeuduttua. Näytän, miten tämä tehdään oppaan lopussa.

## Vaihe 2: Sisällön julkaiseminen

Sisällön julkaiseminen on yhtä yksinkertaista ja intuitiivista kuin muutaman sanan kirjoittaminen julkaisukenttään.

![Julkaisu](assets/4.webp)

Siinä se! Olet julkaissut ensimmäisen muistiinpanosi Nostrissa.

![Postaus](assets/5.webp)

## Vaihe 3: Löydä ystävä

Löydä minut Nostrista, niin et ole enää koskaan yksin. Tilaa takaisin kaikille, jotka tilaavat syötteeni. Tee tämä yksinkertaisesti syöttämällä julkinen avaimeni

npub1hartx53w6t3q5wv9xdqdwrk7h6r5866t8u775q0304zedpn5zgssasp7d3 hakukenttään.
![Oma profiili](assets/6.webp)
Klikkaa "seuraa", ja muutaman päivän sisällä, tulen myös tilaamaan sinun syötteesi. Meistä tulee ystäviä. Olen myös iloinen, jos haluat kirjoittaa minulle viestin.

Lopuksi, muista myös tilata Agora256:n syöte, jotta saat ilmoituksen aina kun julkaisemme jotain uutta: npub1ag0rawstycy7nanuc6sz4v287rneen2yapcq3fd06972f8ncrhzqx

## Vaihe 4: Mukauta profiiliasi

Sinulla on vielä hieman työtä tehtävänä profiilisi mukauttamiseksi. Tee tämä klikkaamalla avataria, jonka iris on automaattisesti luonut sinulle näytön oikeassa yläkulmassa, ja sitten klikkaa "muokkaa profiilia".

![Profiili](assets/7.webp)

Sinun tarvitsee nyt vain kertoa irisille, mistä löytää kuvasi ja profiilisi banneri internetistä. Suosittelen oman sisällön isännöintiä: suojaa omaisuutesi.

![Toinen vaihtoehto](assets/8.webp)

Jos haluat, voit myös ladata kuvia, jotka iris säilyttää puolestasi nostr.build-palvelussa, ilmaisessa visuaalisen sisällön isännöintipalvelussa Nostrille.

Kuten näet, voit myös määrittää asiakasohjelmasi niin, että voit vastaanottaa ja lähettää satseja. Näin voit palkita sisällön tekijöitä, joista pidit tai vielä parempaa, kerryttää satseja loistavasta sisällöstä, jonka tulet julkaisemaan.

## Vaihe 5: Varmuuskopioi avainpari

Tämä vaihe on ratkaisevan tärkeä, jos haluat säilyttää pääsyn profiiliisi sen jälkeen, kun olet kirjautunut ulos asiakasohjelmasta tai istuntosi on vanhentunut.
Ensiksi, klikkaa "asetukset"-kuvaketta, jota edustaa hammasratas
![Asetus](assets/9.webp)

Kopioi ja liitä sitten yksitellen npub, npub hex, nsec ja nsec hex teksti-tiedostoon, jonka pidät turvallisesti. Suosittelen tämän tiedoston salaamista, jos tiedät miten se tehdään.

![Avain](assets/10.webp)

> ⚠️ Huomioi varoitus, jonka iris antaa sinulle. Vaikka voit jakaa julkisen avaimen pelkäämättä, yksityisen avaimen kanssa tarina on toinen. Kuka tahansa, jolla on se, pystyy pääsemään käsiksi tilillesi.

## Yhteenveto

Siinä se nyt on, pikku strutsi, olet ottanut ensiaskeleesi Nostrilla. Nyt sinun täytyy oppia juoksemaan salaman nopeudella. Julkaisemme pian oppaita, jotka näyttävät sinulle, miten hallita avaimiasi ja miten integroida salama Nostr-kokemukseesi käyttäen getalby.