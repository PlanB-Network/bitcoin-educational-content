---
name: BitcoinVoucherBot P2P
description: Miten ostaa ja myydä Bitcoin P2P BitcoinVoucherBotilla?
---

![image](assets/cover.webp)



Kuulemme edelleen BitcoinVoucherBotista, Telegram-botista, joka on luotu ostamaan Bitcoin:ää ilman [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) SEPA-pankkisiirrolla. Valitettavasti marraskuusta 2025 lähtien BitcoinVoucherBot ei ole enää keskitetyssä muodossaan saatavilla palveluna ilman KYC:tä.



Tässä oppaassa tarkastelemme, miten uusi toteutus toimii, jonka avulla käyttäjät voivat ostaa ja myydä Bitcoin:tä suoraan uudella P2P (Peer-To-Peer) -markkinapaikalla, joten KYC:tä ei tarvita. Vastatakseen uusiin rajoituksiin, jotka uhkaavat yhä enemmän digitaalista vapautta ja yksityisyyttä, kehittäjät loivat tämän laajennuksen, joka antaa käyttäjille mahdollisuuden ostaa ja myydä Bitcoin:tä erittäin anonyymisti P2P:n (Peer-To-Peer) kautta. Katsotaan yhdessä, miten tämä uusi vaihtomenetelmä toimii.



Palvelun käyttäminen edellyttää, että siirrot tehdään Lightning Network:n kautta. Varmista siis, että sinulla on wallet, joka tukee tätä protokollaa ja jonka avulla voit käyttää "LNURL"- tai "Lightning Address" -protokollaa varojen vastaanottamiseen ja lähettämiseen.



Tuettujen lompakoiden joukosta löytyy:





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (säilytys) (Custodial)
- [Wallet Of Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Säilytys, jossa on swap-mahdollisuus muuhun kuin säilytysvelvollisuuteen)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



Tai mikä tahansa wallet, jolla on "Lightning Address" ja joka luo Bolt11-laskun.Lompakoita, jotka generate luovat Bolt12-laskun, ei tällä hetkellä tueta. Lisätietoja on [Bolt](https://planb.academy/resources/glossary/bolt) -määritelmässä.



Tässä opetusohjelmassa käytämme Wallet of Satoshi:a, koska sitä on helppo käyttää välittömästi.



**Varoitus**: Käytä sitä vain tilapäisesti ja siirry välittömästi muuhun kuin säilytysjärjestelmään, jotta saat täyden määräysvallan. Lokakuusta 2025 alkaen se sisältää vakaan itsehallinnollisen tilan maailmanlaajuisesti iOS/Androidissa (päivitä sovellus), jossa on itsenäiset yksityiset avaimet, vaihtaminen tilojen välillä, mukautetut Lightning-osoitteet ja seed 12-sanaisen varmuuskopion. Se on kuitenkin edelleen väliaikainen ratkaisu konsolidointiin asti, mieluummin wallet:n ei-säilytystila on kypsä pitkän aikavälin hallintaan.



Oikein hyvä! Nyt voimme aloittaa matkamme, joka opastaa sinua askel askeleelta tilin luomisessa, osto- ja myyntitapahtumien hallinnassa ja rajoitetun alueen käytössä.



## Wallet ja ilmoittautuminen



Lataa ensin Wallet of Satoshi, jos sitä ei ole vielä asennettu älypuhelimeesi.





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Jos et ole koskaan käyttänyt Wallet of Satoshi:ta ja haluat ymmärtää, miten se toimii, suosittelen, että seuraat tätä ohjetta, jotta voit aktivoida sen oikein ja varmuuskopioida sen turvallisesti.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Nyt kun wallet on valmis, voit aloittaa pienen määrän sats:ää. Muista, että P2P (Peer-To-Peer) -alustan rekisteröinnin loppuunsaattamiseksi sinun on lähetettävä 1000 sats:ää valvontatoimenpiteenä: tämän tarkoituksena on luoda esto phantom match (huijaus) -tyyppisiä hyökkäyksiä vastaan, jotta kukaan ei voisi rekisteröityä ilman roskapostisuodatinta.



![image](assets/it/02.webp)



Voimme nyt avata P2P (Peer-To-Peer) -alustan ja jatkaa rekisteröintiä. Voit kirjautua sisään pöytätietokoneista tai älypuhelinten selaimista, Telegram BitcoinVoucherBotin kautta tai .onion-linkkien kautta, jotta yksityisyys olisi entistäkin parempi.



jos päätät käyttää Tor .onion -linkkiä, suosittelen myös "Tor Browser". Jos et vielä tunne sitä, voit oppia siitä lisää tästä linkistä:



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Valitse nyt, miten haluat päästä alustalle.





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Desktop / Selain Smartphone](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Sinut ohjataan pääsivulle.



paina "Get Starter" päästäksesi heti alkuun



![image](assets/it/03.webp)



Seuraavassa näytössä sinun on valittava salasana ja syötettävä se (ruutu A) ja toistettava se (ruutu B). Suosittelen, että tallennat tämän salasanan välittömästi varmuuskopioidulle tietovälineelle, joka voi olla turvallinen digitaalinen laite, kuten "Bitwarden":



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

tai tallenna salasanasi paperille (**varoitus**: tämä ei ole hyvä ratkaisu, mutta se on ihan hyvä, jos se on tarkoitettu väliaikaiseksi ratkaisuksi).



Merkitse rasti ruutuun, jossa ilmoitat, että et ole robotti (ruutu C). Huomaa Älä ota RSA-salausta käyttöön, ellet tiedä tarkalleen, mikä se on ja miten se toimii. Sinun ei tarvitse tehdä mitään tässä vaiheessa. Napsauta "Generate Avatar" ("Luo avatar") (ruutu D).



![image](assets/it/04.webp)



Nyt sinun on maksettava 1000 sats ilmoittautumisen loppuun saattamiseksi.



1. Aloita ylhäältä, katso ensin satunnaisesti luotu ja erittäin tärkeä "Avatar ID" Tallenna se huolellisesti, aivan kuten kehotin sinua tekemään salasanan kanssa.


2. Tämän jälkeen sinun on syötettävä "Lightning Address" alla olevaan kenttään. Näin voit vastaanottaa maksuja, jos ostat Bitcoin:n, tai saada palautuksia. Jos käytät Wallet:tä tai Satoshi:tä, voit kopioida Address:n napsauttamalla "vastaanottaa".


3. Rastita ruutu, jossa ilmoitat, ettet ole robotti.


4. Maksa 1000 sats saadaksesi pääsyn rajoitetulle alueelle. Jos et pysty kehystämään sitä, napsauta sitä hiirellä (tietokoneella) tai napauta sitä sormella (selaimella/Telegram älypuhelimilla) kopioidaksesi osoitteen, joka sinun on liimattava Wallet of Satoshi:een, ja suorittaaksesi laskun maksun.



![image](assets/it/05.webp)



Tämä on LNURL Address.



![image](assets/it/06.webp)



Onnittelut!!! Olet luonut Avatarisi pysyvästi ja voit tarkastella yhteenvetoa täällä. Jälleen kerran suosittelen, että tallennat huolellisesti sekä avatarisi että salasanasi, kuten olen ehdottanut aiemmin.



Napsauta `I've saved my credentials, continue` (käännettynä: "Olen tallentanut valtakirjani, jatka")



![image](assets/it/07.webp)



Olet nyt alustan sydämessä, jossa voit tarkastella kaikkia kauppasopimuksia ja niiden yksityiskohtia. Selkeämmän näkymän saamiseksi näet alla kuvia, jotka ovat luontaisia verkkosivuilla pöytätietokoneista.





- 'Tyyppi' ('Tyyppi') määrittelee, onko kyseessä 'Myynti' ('myy') vai 'Osto' ('osta')
- "Amount" ("Määrä"): osoittaa, kuinka monta sats:tä käyttäjä myy, jos ottelu on tyyppiä "Sell", tai kuinka monta Bitcoin:tä käyttäjä on valmis ostamaan, jos ottelu on tyyppiä "Buy".
- "BTC Price with Margin" ("BTC Price with Margin"): näyttää hinnan, jossa on otettu huomioon merkityn arvon yläpuolella sovellettava marginaali.
- "Marginaali" ("Margin") on prosenttiosuus, jota sovelletaan markkinahintaan, Miinusmerkin (-) avulla saat alennusta markkinahinnasta, plusmerkin (+) avulla markkinahintaan sovelletaan preemiota.
- "Tapa" ("Method") ilmaisee, millä motodolla käyttäjä haluaa, että hänelle maksetaan.
- "Luoja" on käyttäjän alustalla käyttämä ainutlaatuinen avatar.
- "Rep" (Maine) Käyttäjän maineen taso vaihtelee -5 epäluotettavasta +5 erittäin luotettavaan.
- "Status" ("Tila"): ilmaisee ottelun tilan. Esimerkin kuvakaappauksessa kaikki ottelut näyttävät olevan "Open" ("Avoin").
- "Expiration" ("Vanhentuminen"): näyttää, kuinka paljon aikaa on jäljellä ennen kuin ottelu päättyy ja peruuntuu, jos kukaan ei ole valinnut sitä.



![image](assets/it/08.webp)



Klikkaa oikeassa yläkulmassa Avatariasi päästäksesi profiiliisi.



![image](assets/it/09.webp)



Täällä näet avatarisi nimen, käyttäjätunnuksen, luontipäivämäärän ja maineen, joka vaikuttaa positiivisesti tai negatiivisesti käyttäytymiseesi neuvotteluissa.



![image](assets/it/10.webp)



Asetukset-osiossa voit tarkastella rekisteröinnin yhteydessä syöttämääsi "Lightning Address" -nimeä ja muuttaa sitä tarvittaessa. Sinulla on myös mahdollisuus luoda julkinen avain, joka, kuten mainittiin, tulisi luoda vain, jos sinulla on asianmukaiset taidot. Sitä käytetään niiden viestien salaamiseen, joita vaihdat vastapuolesi kanssa suoraan tietokoneeltasi.



Telegram-ilmoitusominaisuus on erittäin suositeltava. Aktivoimalla sen saat näkyviin QR-koodin, jonka voit kehystää Telegram-sovelluksella: näin saat reaaliaikaisia ilmoituksia kaikista otteluihisi liittyvistä toimista suoraan Telegram:n botin chatissa.



![image](assets/it/11.webp)



Lopuksi löydät suositteluosiosiosi, jossa on kutsumiesi käyttäjien tuottamat tulot. Täältä voit käyttää painiketta linkin tai QR-koodin jakamiseen, ja hieman alempana voit tarkastella luetteloa otteluista ja seurata mainettasi sekä vastaavaa pistemäärää.



![image](assets/it/12.webp)



## Luo tilaus ostaa Bitcoin



Siirry kauppapaikalle: napsauta päänavigointipalkista ostoskorin symbolia "Marketplace" ("Kauppapaikka") avataksesi tilauskirjan. aloita sitten uusi tilaus: paina "Uusi tilaus" -painiketta ("New Order") aloittaaksesi prosessin.



![image](assets/it/13.webp)





- Aseta tilauksen tiedot:
- Valitse vaihtoehto "Osta Bitcoin"("Buy Bitcoin").
- Kirjoita haluamasi sats:n määrä.
- Määritä hintamarginaali (-20 % ja +20 % välillä markkina-arvosta).
- Valitse maksutapa (Instant SEPA jne.).
- Ilmaisee ensisijaisen valuutan.
- Vahvista tilaus: klikkaa "Luo tilaus" ("Vahvista tilaus") siirtyäksesi arkistointivaiheeseen.



![image](assets/it/14.webp)



Talletus vaaditaan: tilauksen aktivoimiseksi vaaditaan talletus, joka on 10 % kokonaissummasta sekä palvelumaksu.




- Ennakkomaksu: Kun tilaus luodaan, järjestelmä luo automaattisesti Lightning-laskun. Talletus on vain väliaikainen ja se palautetaan, kun tilaus on valmis.
- Tärkeimmät ominaisuudet:
- Vakuusmaksu: 10 % tilauksen arvosta.
- Palvelumaksu: alustan käytöstä aiheutuvat kustannukset.
- Aikaraja: Sinulla on 5 minuuttia aikaa suorittaa maksu, muuten maksutapahtuma raukeaa.



![image](assets/it/15.webp)



Onnistuneen maksun jälkeen tilaus ilmestyy kirjaan ja näkyy kaikille käyttäjille, jotka voivat valita ja hyväksyä sen. Luodaksesi myyntitilauksen sinun tarvitsee vain klikata "Sell Bitcoin" ("Myydä Bitcoin"), syöttää määrä satoshi:a, jonka haluat myydä, asettaa marginaali, valita maksutapa ja valuutta ja jatkaa sitten 10 %:n talletus vakuustalletuksena. Kun se on valmis, ottelusi näkyy luettelossa.



![image](assets/it/16.webp)



## Tilauksen hyväksyminen



1. Myyjät näkevät luettelon kaikista kirjassa olevista tilauksista.


2. Tarkista yksityiskohdat: jokaisesta tilauksesta löytyvät seuraavat tiedot:




  - Bitcoin:n määrä,
  - Hintamarginaali,
  - Maksutapa,
  - Käyttäjän maine.



![image](assets/it/17.webp)



3. Napsauta tilausta avataksesi täydellisen lomakkeen, jossa on kaikki tiedot.


4. Hyväksy ehdotus painamalla "Myy Bitcoin"("Sell Bitcoin").



![image](assets/it/18.webp)



## Myyjän vaatima talletus



Kun tilaus on hyväksytty, järjestelmä luo laskun maksua varten. Talletus sisältää:



- Tilauksen kokonaissumma,



- palvelukomissio.



Talletusmaksu on suoritettava asetetussa määräajassa, muutoin kauppaa ei vahvisteta.



![image](assets/it/19.webp)



## Maksuohjeiden lähettäminen



Kun talletus on tehty, maksutapahtuma näkyy myyjän henkilökohtaisella kojelaudalla, ja myyjän on annettava tiedot ostajalle suorittaakseen maksun fiat-valuutassa.



1. Myyjä näyttää aktiivisen tapahtuman paneelissaan.


2. Napsauta "Lähetä maksuohjeet"


3. Anna kaikki tarvittavat tiedot fiat-maksua varten (IBAN, vastaanottaja, osoite, maksun syy jne.).


4. Klikkaa "Lähetä viesti"("Send Message") lähettääksesi tiedot ostajalle.



![image](assets/it/20.webp)



## Maksumenettely



Ostaja saa alustan chatissa viestin, jossa on kaikki tarvittavat tiedot maksun suorittamiseksi fiat-valuutassa:




- Pankkiyhteydet: IBAN sekä myyjän tilinomistajan nimi ja osoite.
- Tarkka summa: tarkka siirrettävä fiat-summa.
- Syy/kuvaus: tapahtumaan sisällytettävä teksti.
- Määräaika: määräaika, johon mennessä maksu on suoritettava.



Siirto tapahtuu P2P-järjestelmän ulkopuolella, ja se on tehtävä oman pankkilaitoksen kautta.



⚠️ **Tärkeä huomautus:** Vahvistus alustalla tulisi tehdä vasta sen jälkeen, kun olet todella järjestänyt siirron tai fiat-maksun pankkisi kautta.



![image](assets/it/21.webp)



## Maksun vahvistus fiat



Tämä vaihe on ostajan kannalta ratkaisevan tärkeä, ja se olisi suoritettava vasta sen jälkeen, kun on varmistettu, että maksu on todella lähetetty.



1. Vastaanottotiedot: Ostaja on saanut myyjältä maksuohjeet.


2. Maksun suorittaminen: fiat-siirto järjestetään pankkitililtä.


3. Tarkistus: Tarkista, että toiminto on käsitelty oikein.


4. Vahvista alustalla: klikkaa "Vahvista fiat-maksu" ("Confirm fiat payment") kaupan sivulla.


"Vahvista maksu fiat" -painike ilmestyy tapahtumaosioon, ja sitä tulisi käyttää vasta sen jälkeen, kun olet varmistanut, että maksu on todella lähetetty.



![image](assets/it/22.webp)



Prosessin viimeinen vaihe on, että myyjä vahvistaa fiat-maksun vastaanottamisen, minkä jälkeen satssit luovutetaan ostajalle.



![image](assets/it/23.webp)



## Päätelmä



Toivomme, että tämä opetusohjelma auttaa sinua käyttämään uutta menetelmää Bitcoineilla käytävään kauppaan tai jopa vain ostamaan niitä, joko omaksi arvovarastoksi tai päivittäisten maksujen elävöittämiseksi. Silti se on edelleen ovi, jota on tutkittava, jotta selviydytään siitä, mitä digitaalisessa maailmassamme on tapahtumassa.



Meitä valvovien elinten johtama silmukka kiristyy ja synnyttää yhä enemmän valvotun internetin. Ostamalla P2P:n pidät ostoksesi täysin anonyyminä, etkä jätä jälkiä etkä seuraa jälkiseuraamuksia kolmansilta osapuolilta.