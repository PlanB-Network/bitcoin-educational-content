---
name: Peach
description: Täydellinen opas Peach:n käyttöön ja bitcoinien kaupankäyntiin P2P:ssa
---

![cover](assets/cover.webp)





## Johdanto



KYC-vapaat vertaisverkkopörssit (P2P) ovat välttämättömiä käyttäjien luottamuksellisuuden ja taloudellisen riippumattomuuden säilyttämiseksi. Ne mahdollistavat suorat transaktiot yksityishenkilöiden välillä ilman henkilöllisyyden todentamista, mikä on ratkaisevan tärkeää yksityisyyttä arvostaville. Jos haluat syvällisemmän käsityksen teoreettisista käsitteistä, katso BTC204-kurssi:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. Mikä on Peach?



Peach on P2P-vaihtofoorumi, jonka avulla käyttäjät voivat ostaa ja myydä bitcoineja ilman KYC:tä. Se tarjoaa intuitiivisen käyttöliittymän ja kehittyneet turvaominaisuudet. Verrattuna muihin ratkaisuihin, kuten Bisq, HodlHodl ja Robosat, Peach erottuu edukseen helppokäyttöisyytensä ansiosta.


multisignature escrow -järjestelmä (2-2) takaa varojen turvallisuuden liiketoimien aikana. Peach tukee erilaisia maksutapoja, ja siinä on mainejärjestelmä, joka ohjaa kauppiaiden toimintaa. Kuten tavallista P2P-alustoilla, on siis tärkeää ylläpitää hyvää mainetta, jotta uskottavuus muiden kauppiaiden keskuudessa säilyy.



### 2. Yksityisyys ja kerätyt tiedot



**Mitä tietoja Peach kerää?



Peach pyrkii tallentamaan mahdollisimman vähän tietoja käyttäjistään. Seuraavassa on yleiskatsaus palvelimillemme tallennetuista tiedoista:





- hash yksilöllisen sovellustunnuksesi (AdID)
- hash maksutiedoistasi
- Salatut keskustelut
- Transaktiotiedot sen varmistamiseksi, että anonyymit käyttäjät eivät ylitä kaupankäyntilimiittiä (käytetyt maksutavat, osto- ja myyntimäärät)
- Addresses, jota käytetään escrow-tilin lähettämiseen ja vastaanottamiseen
- Käyttötiedot (Firebase & Google Analytics), vain suostumuksellasi



Muistutuksena mainittakoon, että hash on tietoa, joka on tehty tunnistamattomaksi, samoin kuin salaus. Sama data tuottaa aina saman hash:n, joten kaksoiskappaleet voidaan havaita tuntematta alkuperäistä dataa.



*Jos haluat yksityiskohtaisemman selityksen hashingistä, käy tämä kurssi:*



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Kuka näkee maksutietoni?





- Vain vastapuolesi näkee maksutietosi
- Tiedot siirretään Peach-palvelimien kautta, mutta ne ovat täysin salattuja päästä päähän
- Riitatilanteessa Peach-sovittelija näkee maksutietosi ja keskusteluhistoriasi



## Asennus ja konfigurointi



### 1. Asenna Peach-sovellus



![Installation de Peach](assets/fr/01.webp)





- Lataa sovellus osoitteesta [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/). IOS:ssä sinun on ensin asennettava [testflight](https://apps.apple.com/us/app/testflight/id899247664) -sovellus.
- Seuraa laitteesi asennusohjeita.
- Asennuksen aikana sinua pyydetään valitsemaan, haluatko jakaa tiettyjä tietoja Peach-sovelluksen parantamiseksi. (Kuva 1)
- Seuraavassa näytössä (kuva 2) on kaksi vaihtoehtoa:
 - Jos olet uusi käyttäjä, klikkaa "Uusi käyttäjä" luodaksesi uuden profiilin
 - Jos sinulla on jo tili, voit palauttaa nykyisen profiilisi käyttämällä "Palauta"
- Jos sinulla on suosittelukoodi, voit syöttää sen tähän.
- Jos haluat palauttaa olemassa olevan tilin (kuva 3), tarvitset :
 - Varmuuskopiotiedostosi
 - Salasana tiedoston salauksen purkamiseen



### 2. Yleiskatsaus päänäytöihin



Peach-sovellus koostuu neljästä päänäytöstä, joihin pääsee alareunan navigointipalkista:



![Navigation dans l'application](assets/fr/02.webp)





- Koti (4)** : Päänäyttö, josta voit valita osto- tai myyntitapahtuman, luoda uusia tapahtumia ja tutustua saatavilla oleviin tarjouksiin:
 - luo tarjouksia kahdella alla olevalla painikkeella (luo osta / luo myy)
 - hyödyntää muiden käyttäjien luomia tarjouksia käyttämällä kahta alla olevaa painiketta ("Osta"/"Myy").





- Wallet (5)** : Integroitu Bitcoin wallet, jonka avulla voit :
 - Tarkista saldosi
 - Vastaanottaa bitcoineja
 - Envoyer bitcoinit (kolikoiden hallinnalla)
 - Tarkastele tapahtumahistoriaasi
 - Myynnin rahoittaminen





- Kaupat (6)**: nykyiset ja aiemmat sopimuksesi kolmella välilehdellä:
 - Keskeneräiset ostot
 - Käynnissä oleva myynti
 - Vaihtojen historia





- Asetukset (7)** : Konfigurointikeskus
 - Tarkastele profiiliasi (maine, merkit, rajoitukset jne.)
 - Tietoturvan hallinta (varmuuskopiointi, pin)
 - Hallitse maksutapojasi
 - Ota yhteyttä tukeen
 - Vaihda kieltä
 - jne.



### 3. Määritä maksutavat



![Accès aux paramètres de paiement](assets/fr/03.webp)



Voit hallita maksutapojasi asetuksissa (kuva 8)



Peach tarjoaa verkkomaksuja ja henkilökohtaisia maksuja (vain rekisteröidyissä tapaamisissa).



**Online-maksut



**Tärkeää:**


käyttäjien suojelemiseksi Peach edellyttää, että varojen lähde vastaa mainostettua lähdettä. Kauppiaiden tehtävänä on varmistaa, että näin on, omaksi suojakseen.



![Configuration des paiements en ligne](assets/fr/04.webp)



Menetelmän lisääminen :




- Klikkaa "online"-välilehdellä "Lisää valuutta/menetelmä"
- Valitse valuutta
- Valitse haluamasi maksutapa



*Käytettävissä olevat maksutavat:*



***Pankkisiirtoja varten: ***




- SEPA (vakio- tai pikakortti)
- Täytä SEPA-pankkitietosi.



***Online wallet hyväksytään :***




- Käytettävissä on useita vaihtoehtoja maasta riippuen (Revolut, Paypal, Wise, Strike jne.)
- Seuraa ohjeita lisätäksesi kirjautumistietosi



*lahjakortti käyttökelpoinen:*** lahjakortti käyttökelpoinen:*** lahjakortti käyttökelpoinen:*** lahjakortti käyttökelpoinen:*** lahjakortti käyttökelpoinen:*** lahjakortti käyttökelpoinen:***




- Amazon, Steam jne.
- Syötä kortin myöntäjämaa ja muut tarvittavat tiedot



***Kansalliset maksuvaihtoehdot:***


Maakohtaiset maksujärjestelmät :




- Satispay (Italia)
- MB Way (Portugali)
- Bizum (Espanja)
- Nopeammat maksut (Yhdistynyt kuningaskunta)
- jne.



***Kohtaisesti suoritettaviin maksuihin: ***



![Configuration des paiements en personne](assets/fr/05.webp)





- Valitse "Meetup" (kuva 12)
- Valitse sitten tapaamisesi luettelosta (kuva 13)



### Käyttöohjeet





- Voit lisätä useita maksutapoja
- Mitä enemmän menetelmiä lisäät, sitä laajempi valikoima tarjouksia on käytettävissäsi
- Tarkista tietojesi oikeellisuus ennen rekisteröitymistä
- Voit muuttaa tai poistaa maksutapojasi milloin tahansa



**Turvahuomautus**: Paitsi riitatilanteessa, jolloin myös Peach-sovittelija pääsee käsiksi tietoihin.



### 4. Kuinka turvata salkkusi



** Peach-tilisi ymmärtäminen



Peach-tilillä ei ole käyttäjätunnusta eikä salasanaa. Se on tiedosto, joka on tallennettu paikallisesti puhelimeesi, mikä tarkoittaa, että Peach:n ei tarvitse tallentaa tietojasi tai tietää henkilöllisyyttäsi: sinä hallitset tilannetta. Tämä tiedosto sisältää kaikki tietosi: mukaan lukien 12 bitcoin-palautussanaa, PGP-avaimet, maksutiedot ja niin edelleen. On siis erittäin tärkeää tallentaa tämä tiedosto ja suojata se __robust__-salasanalla.



Tämä lähestymistapa takaa tietynasteisen luottamuksellisuuden ja jättää vastuun tietojen ja varmuuskopioiden hallinnasta käyttäjälle. Puhelimen menettäminen ilman varmuuskopiota tarkoittaa, että menetät pääsyn Peach-tiliisi ja varoihisi.



**Luo varmuuskopiot**






- Pääset asetuksiin aloitusnäytön oikeassa alareunassa olevasta välilehdestä
- Valitse asetusvalikosta vaihtoehto "varmuuskopiot"



![Processus de sauvegarde](assets/fr/06.webp)



Käytettävissä on kahdenlaisia varmuuskopioita:



**Tallenna tilitiedosto (kuva 14)**




- Napsauta "Luo uusi varmuuskopio"
- Luo **vahva** salasana varmuuskopiointitiedoston salaamiseksi
- Lähetä tämä tiedosto paikkaan, jossa se on käytettävissä, jos puhelin katoaa.



Tiedoston varmuuskopiointi palauttaa koko Peach-tilisi, mukaan lukien :




- Salkkusi
- Maksutapasi
- Maksutiedot
- Transaktiohistoria, jossa on yksityiskohtaiset tiedot vastapuolista ja niiden kanssa käydyistä keskusteluista



**Palautuslauseen tallentaminen (kuva 15)**




- Seuraa ohjeita näyttääksesi palautuslauseesi
- Kirjoita sanat huolellisesti oikeaan järjestykseen
- Säilytä tämä varmuuskopio turvallisessa paikassa, mieluiten eri paikassa kuin tilitiedosto



Elvytyslauseen avulla voit palauttaa :




- Maineesi, kauppasi
- Bitcoin-varasi



Mutta **Ei** seuraavia:




- Nykyiset ja aiemmat keskustelut
- Maksutiedot
- Vastapuolen tiedot tapahtumahistoriassa




## Bitcoinien ostaminen ja myyminen



### 1.a Miten ostaa bitcoineja: Ota tarjous myydä



Ostajan ensimmäisenä refleksinä pitäisi olla tarkistaa myytävät tarjoukset, jotka on jo rahoitettu bitcoineilla.



![Vue des offres de vente et filtres](assets/fr/07.webp)





- Napsauta aloitusnäytössä "Osta"-painiketta (kuva 16)
- Tämän jälkeen voit selata luetteloa bitcoineista, jotka on sijoitettu escrow-järjestelmään ja jotka ovat valmiina myytäväksi (kuva 17). Näet määrän, hinnan (prosentteina suhteessa KYC-markkinoihin), maksutavat ja hyväksytyt valuutat.
- Käytä suodattimia tarjousten lajitteluun ja järjestämiseen (kuva 18).
- Huomaa: Suodattimet-sivun alareunassa olevan painikkeen avulla voit saada ilmoituksen, kun suodattimiasi vastaava tarjous on julkaistu, ja "nollaa"-painikkeen avulla voit yksinkertaisesti tyhjentää kaikki suodattimet (kuva 18).



![Sélection et confirmation d'achat](assets/fr/08.webp)





- Tarkastele sinulle sopivaa tarjousta ja lähetä vaihtopyyntö (kuva 19)
- Voit tehdä useita vaihtopyyntöjä, ja ensimmäinen myönteinen tarjous peruuttaa muut pyynnöt.
- Suorita maksu sovitulla tavalla.


**Muistutus:** Varojen lähteen on vastattava sitä, jonka määrittelit maksutapaa lisätessäsi.




- Vahvista maksusi hakemuksessa heti, kun se on tehty**.
- Odota, että myyjä vastaanottaa maksun, ja ilmoita se sellaiseksi (kuva 20)
- Lopuksi arvioi kokemuksesi myyjän kanssa (kuva 21)



![Réception des bitcoins](assets/fr/09.webp)





- Seuraa tapahtuman tilaa
- Tarkista vahvistus bitcoinien vastaanottamisesta
- Varat ovat käytettävissä Peach-salkussasi (kuvat 22 ja 23)



### 1.b Miten ostaa bitcoineja: Luo tarjous



Jos et löydä sopivaa myyntitarjousta, voit tehdä ostotarjouksen. Koska tämä ei tässä vaiheessa sido yhtään bitcoinia, sinulla on pienemmät mahdollisuudet löytää vaihtokumppani, varsinkin jos saavutuksesi ja maineesi ovat huonot tai olemattomat. Tämän korjaamiseksi on tärkeää, että tarjousta luodessasi *tehdä korkeapalkkainen tarjous*, jotta myyjät motivoituvat valitsemaan tarjouksesi. Jatketaan:



![Creation d'ordre d'achat](assets/fr/10.webp)





- Napsauta aloitusnäytössä "Luo ostotarjous" -painiketta (kuva 24)
- Lisää maksutapa, jos et ole vielä tehnyt sitä, ja anna asetukset (määrä, palkkio jne.) (kuva 25).


"Välitön" -vaihtoehdon avulla voit hyväksyä kaupantekopyynnön automaattisesti.




 - Jatka klikkaamalla uudelleen "Luo tarjous"
- Kun se on luotu, on myyjien vuoro tulla luoksesi vaihtopyynnön kanssa. Voit sulkea sovelluksen ja poistua siitä huoletta.
- Voit muuttaa palkkion, jos et saa yhtään pyyntöä. Muista: korkeampi palkkio motivoi myyjiä tulemaan etsimään tarjoustasi (kuva 26).
- Löydät tarjouksesi "Osta"-välilehdeltä, joka puolestaan on "Exchange"-ikkunassa (kuva 27)



![Reception d'une demande de vente, messagerie](assets/fr/11.webp)





- Kun saat ostopyynnön (kuva 28) (ja jos et ole poistanut pikakauppaa käytöstä kuvassa 25), hyväksy kauppa tarkistettuasi myyjän maineen. Jos pikakauppa on käytössä, hyppää suoraan kuvaan 29.
- Myyjän on sitten sijoitettava bitcoinit escrow-järjestelmään ("rahasto kassakaappiin"). (kuva 29)
- Maksa sitten myyjälle kuvassa 30 esitetyssä kohteessa henkilökohtaisen pankkijärjestelmäsi kautta. Älä vedä "Olen suorittanut maksun" -kursoria, ennen kuin olet tehnyt sen!
- Voit kommunikoida myyjän kanssa viestijärjestelmän kautta (P2P-salattu). Ongelmatilanteessa voit avata riidan klikkaamalla oikeassa yläkulmassa olevaa kuvaketta (kuva 31). Peach-sovittelija osallistuu tällöin keskusteluun.



![Offre de vente completée](assets/fr/12.webp)





- Kun myyjä on saanut rahat, hän ilmoittaa siitä, ja escrow-järjestelmä vapauttaa bitcoinit, jotka ovat matkalla wallet:ään (oletusarvoisesti GroupHugin, Peach:n transaktioiden ryhmittelyjärjestelmän kautta, joka toimii kerran päivässä),
- Arvioi kokemuksesi myyjästä



Juuri noin!



**Huomautus uusille ostajille:** Myyjät perustavat kaupat ostajien maineeseen ja välttävät tarjouksia ostajilta, joilla ei ole tehtyjä kauppoja. On helpompaa aluksi rakentaa mainetta ottamalla vastaan olemassa olevia myyntitarjouksia.




### 2.a Kuinka myydä bitcoineja: Luo myynti



Nopein ja helpoin tapa myydä Peach:ssa on **luoda myyntitarjous**.



![Création d'un ordre de vente](assets/fr/13.webp)





- Klikkaa etusivulta "Luo myyntitarjous" (kuva 32)
- Määritä tarjouksesi, varmista, että lisäät maksutavan ja oikeat parametrit


voit myös :




  - luoda useita identtisiä tarjouksia
  - aktivoi "välitön vaihto", jotta ensimmäinen ostaja voi ottaa sopimuksen vastaan (ilman sinun vahvistustasi) ja jatkaa maksua.
  - valitse palautusosoite
  - rahoittaa wallet Peach:n runkoa
- Rahoita transaktio lähettämällä bitcoinit annettuun osoitteeseen (kuva 34)
- Odota vahvistusta tapahtumasta. Kun se on tehty, tarjouksesi näkyy markkinoilla.



![Attente du paiement](assets/fr/14.webp)





- Odota, että ostaja tarttuu tarjoukseesi. Harkitse palkkion (%) korottamista, jos haluat nopeuttaa asioita (kuva 36)
- Kun olet saanut vaihtopyynnön, tarkista ostajan maine. Arvioi itse, sopiiko profiili sinulle, ja napsauta "hyväksy", jos sopii. (37)
- Nyt on ostajan vuoro suorittaa maksu hänen pankistaan sinun pankkiisi. Sitten hän välittää maksun sinulle. Älä epäröi ottaa yhteyttä ostajaan chatissa.
- kun olet tarkistanut, että pankkisi* on vastaanottanut varat, vapauta varat napsauttamalla "olen vastaanottanut maksun" -painiketta (kuva 38). Älä koskaan vahvista maksun vastaanottamista ennen kuin olet tarkistanut, että maksu on saapunut tilillesi.
- Arvioi liiketoimi
- Bitcoin:t luovutetaan automaattisesti ostajalle,



Noin sitä pitää!



**Turvahuomautus ja vinkkejä onnistuneeseen kauppaan:**




 - Tarkkaile ostajan tietoja ja tarkista, että varojen alkuperä vastaa Peach:ssä kuvattua alkuperää Jos varojen alkuperä ei vastaa ilmoitettua alkuperää, mene Chatiin ja avaa riita (kuva 39) ja lähetä varat takaisin niiden alkuperään.
 - Noudata keltaisen kissan ohjeita.
 - Vastapuolen viesteihin vastaaminen nopeasti
 - ole varovainen ostajan asenteen suhteen, varsinkin jos olet tekemisissä profiilin kanssa, jolla on vain vähän kokemusta
 - Älä epäröi käyttää sovittelupalvelua, jos sinulla on ongelmia



### 2.b Kuinka myydä bitcoineja: tee tarjous



On myös mahdollista tarkastella ja valita ostotarjouksia. Sinun on oltava erityisen varovainen, sillä täällä on eniten huijareita.



![Prendre une offre d'achat](assets/fr/15.webp)





- Klikkaa etusivulta "Myynti" (kuva 40)
- Käytä suodattimia nähdäksesi ja valitaksesi houkuttelevimmat tarjoukset (kuva 41)



![vérification de la réputation](assets/fr/16.webp)





- ennen kuin pyydät kauppaa, suosittelemme, että arvioit ostajan profiilin sopivuuden. Voit klikata tarjousta ja sitten käyttäjän tunnusta nähdäksesi hänen profiilinsa. Esimerkiksi kuvan 42 tarjousta voitaisiin pitää "riskialttiina" (uusi käyttäjä, suhteellisen suuri summa). "Riski", jonka otat tämän tarjouksen vastaan, on vain ajan tuhlaaminen, kunhan et tee sitä virhettä, että vapautat bitcoineja saamatta rahaa. Voit silti tallettaa bitcoinit kassakaappiin.


Kuvassa 43 oleva arvopaperi sen sijaan on peräisin kokeneelta kauppiaalta (kuva 44), jonka historiassa ei ole riitoja. Se on siis vähemmän riskialtis tarjous.



![Match avec vendeur](assets/fr/17.webp)





- Kun tarjous on pyydetty, ja jos ostaja hyväksyy pyyntösi, sovellus vie sinut kuvaan 34, jossa voit jatkaa kauppaa jäljempänä kuvatulla tavalla.




## Edut ja haitat



### Peach:n edut





- KYC:tä ei tarvita**: Säilyttää käyttäjän luottamuksellisuuden.
- Ei pääsyä pankkitietoihin**: Peach:llä ei ole pääsyä pankkitietoihisi tai henkilöllisyytesi.
- Interface intuitiivinen**: Helppokäyttöinen keskitason käyttäjille.
- Avoin lähdekoodi** : Lähdekoodi on julkinen ja yhteisön tarkistettavissa.



### Peach:n haitat





- Rajoitettu Liquidity**: Vähemmän kaupankäynnin volyymia kuin vakiintuneemmilla alustoilla.
- Sääntelyriski** : Sovellusta hallinnoi sveitsiläinen yritys. Siksi siihen sovelletaan sveitsiläisiä säädöksiä, jotka voivat kehittyä ja mahdollisesti sensuroida sovelluksen.



## Hyödyllisiä resursseja





- Ranskankielinen selittävä video: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Pikaopas: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
- [Support telegram](t.me/peachtopeach) (varo huijareita, ylläpitäjät eivät koskaan kirjoita sinulle ensin yksityisviestillä)