---
name: Minibits Wallet
description: Minibittien Wallet opas
---

![cover](assets/cover.webp)


Tässä oppaassa käyn läpi Minibits Wallet:n määrittämisen ecashin käyttöä varten. Tehokas yksityisyyteen keskittyvä maksuteknologia, joka toimii Bitcoin:n rinnalla. Minibits on ecash- ja Lightning Wallet, joka mahdollistaa välittömät, halvat ja yksityiset arvonsiirrot, joten se sopii erinomaisesti jokapäiväisiin maksutapahtumiin, joissa yksityisyydellä on merkitystä.


Ennen kuin perehdymme Minibitteihin, selvitetään ensin, mitä ecash on ja mitä se ei ole. Monet ihmiset sekoittavat ecashin Bitcoin- tai Blockchain-teknologiaan, mutta ne ovat pohjimmiltaan erilaisia käsitteitä.


Ecash EI ole Bitcoin. Se ei korvaa itsehallinnollista Bitcoin Wallet:ää, vaan pikemminkin täydentää sitä. Ecash EI ole Blockchain eikä se asu missään julkisessa Ledger:ssa. Mielenkiintoista on, että ecash EI ole uusi teknologia - se on itse asiassa vanhempi kuin maailmanlaajuinen verkko, sillä sen konseptit kehitettiin 1980- ja 1990-luvuilla.


Mitä ecash on: uskomattoman yksityinen (transaktiot eivät jätä jäljitettävää historiaa), vertaisvertainen (suorat siirrot ilman välikäsiä) ja toimii digitaalisena haltijavälineenä (jos omistat sen, hallitset sitä). Keskeinen etu on se, että ecashia VOI käyttää offline-tilassa - sekä lähettäjä että vastaanottaja voivat olla irrottautuneina internetistä transaktioiden aikana. Ecashia VOI lyödä yksittäinen osapuoli tai luotettavien tahojen liitto, ja se ON täydellinen täydentävä teknologia Bitcoin:n rinnalla, sillä se voi käsitellä pieniä, usein toistuvia transaktioita, kun Bitcoin toimii Layer:n selvitysjärjestelmänä.


Huomaa, että tämä Minibits-asetelma on `custodial-ratkaisu`, mikä tarkoittaa, että luotat rahapajaoperaattorin hallinnoimaan varojasi. Tämä tuo mukanaan erityisiä riskejä, jotka sinun on ymmärrettävä, ennen kuin jatkat.


Hankkeessa näkyy tämä tärkeä vastuuvapauslauseke:


- Tätä Wallet:ta tulisi käyttää ainoastaan tutkimustarkoituksiin.
- Wallet on beta-versio, jonka toiminnot ovat epätäydellisiä ja jossa on sekä tunnettuja että tuntemattomia virheitä.
- Älä käytä sitä suurilla summilla ecashia.
- Wallet:ään tallennetun ecashin liikkeeseenlaskijana toimii rahapaja
- luotat siihen, että rahapaja tukee sitä Bitcoin:llä, kunnes siirrät omistuksesi toiseen Bitcoin:n salaman Wallet:een.
- Wallet:n käyttämää Cashu-protokollaa ei ole vielä tarkasteltu tai testattu laajasti.


Kohtele Minibittejä kuin jokapäiväistä Wallet:aa, älä säästötiliä, äläkä koskaan säilytä niihin merkittävää arvoa.


## 1️⃣ Wallet:n asentaminen


Käy aluksi [Minibitsin verkkosivustolla](https://www.minibits.cash/), josta löydät latausvaihtoehdot kaikille tärkeimmille alustoille. iOS-käyttäjät voivat ladata [App Storesta](https://testflight.apple.com/join/defJQgTD), kun taas EU:n iOS-käyttäjät voivat lisäksi asentaa [Freedom Storesta](https://freedomstore.io/). Android-käyttäjät voivat hankkia sovelluksen [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) tai ladata APK-tiedoston suoraan [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases) -sivulta.


Kun asennat Minibitsin, näyttöön ilmestyy peruskäsitteitä selittäviä esittelynäyttöjä - voit lukea ne läpi tai ohittaa ne, jos tekniikka on sinulle jo tuttu. Kun olet suorittanut nämä alkuvaiheet, sinua pyydetään valitsemaan seuraavista vaihtoehdoista:


- `Got it, take me to the Wallet` uusille käyttäjille tai
- "Palauta menetetty Wallet", jos palautat varmuuskopiosta.


![image](assets/en/01.webp)

Kun olet suorittanut alkuasetukset, pääset aloitusnäyttöön, jossa on useita tärkeitä Elements huomioitavia asioita. ① Yläkulmassa oleva profiilikuvake vie sinut profiilisivullesi, jossa voit käyttää Minibits Wallet Address -ominaisuuksiasi ja valita `erän vastaanotto` -vaihtoehdot. ② Näytön keskellä näet käyttämäsi minttuset, joista oletuksena on valittu Minibitsin minttu. ③ Alla olevalla toimintorivillä on vaihtoehtoja ecash- tai salamamaksujen lähettämiseen, QR-koodin skannaamiseen ja maksujen vastaanottamiseen. ④ Lopuksi alin navigointirivi sisältää pikavalinnat aloitusnäyttöön, tapahtumahistoriaan, yhteystietoihin ja asetuksiin.


![image](assets/en/02.webp)


## 2️⃣ Minttujen hallinta


Minibits Minttu on oletusarvoisesti käytössä, kun käynnistät sovelluksen. Yksi ecashin vahvuuksista on kuitenkin mahdollisuus käyttää useita rahapajoja hajauttamisen ja turvallisuuden lisäämiseksi. Jos haluat lisätä toisen minttupisteen, siirry kohtaan `Asetukset`, valitse `Minttupisteiden hallinta` ja napauta lopuksi `Lisää minttupiste`.


[Bitcoinmints.com](Bitcoinmints.com) tarjoaa kattavan luettelon saatavilla olevista rahapajoista ja käyttäjien luokituksista, jotka auttavat sinua valitsemaan hyvämaineisia vaihtoehtoja. Useiden rahapajojen käyttäminen vähentää riskiäsi. Jos yhdessä rahapajassa ilmenee ongelmia, muiden rahapajojen varat pysyvät saatavilla.


![image](assets/en/04.webp)


## 3️⃣ Varmuuskopion luominen


Varmuuskopiointi on luultavasti koko asennusprosessin kriittisin vaihe. Pääset varmuuskopiointivaihtoehtoihin siirtymällä kohtaan `Asetukset`-> `Varmuuskopiointi` Täältä löydät kaksi tärkeää vaihtoehtoa:

1. "seed-lauseesi", joka sisältää "12 sanaa", joiden avulla voit palauttaa ecash-saldosi, jos laite katoaa. Tämä seed-lause on pääavaimesi kaikkeen ecashiin kaikissa lisäämässäsi rahapajoissa. Kirjoita se fyysiselle välineelle (paperille tai metallille) ja säilytä se turvallisesti useissa eri paikoissa. Älä koskaan säilytä seed-lausetta digitaalisesti, missä se voi vaarantua. Tutustu tähän [opetusohjelmaan](https://planb.network/en/tutorials/Wallet/backup/backup-Mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270), josta löydät parhaat käytännöt Wallet:n suojaamiseen.

2. `Wallet backup`, joka sisältää pitkän varmuuskopiojonon.


**Huomio**: Tarvitset edelleen seed-lauseesi, kun käytät tätä varmuuskopiota Wallet:n palauttamiseen.


![image](assets/en/05.webp)


## 4️⃣ Luo minibittejä Wallet Address


Siirry seuraavaksi alareunassa olevaan kohtaan `Yhteystiedot` ja muokkaa oma `Minibits Wallet Address` napauttamalla `Muuta` -> `Muuta Wallet Address`. Anna haluamasi Address ja tarkista saatavuus.


![image](assets/en/07.webp)


Kun olet asettanut Address:n, sinua pyydetään tekemään pieni "lahjoitus" projektin tukemiseksi. Vaikka tämä on vapaaehtoista, suosittelen vahvasti harkitsemaan sitä, jos aiot käyttää palvelua säännöllisesti. Minibitsin kaltaiset avoimen lähdekoodin projektit ovat riippuvaisia yhteisön tuesta kehityksen ja ylläpidon jatkamiseksi. Pienikin lahjoitus auttaa varmistamaan projektin pitkäikäisyyden.


![image](assets/en/08.webp)


## 5️⃣ Nostr Setup


Jos haluat antaa vinkkejä henkilöille, joita seuraat Nostrissa, voit `Add your npub key` valitsemalla `Contacts` ja sitten `Public`. Tämä yhdistää Minibits Wallet:n Nostrin sosiaaliseen verkostoon, mikä mahdollistaa saumattoman juomarahan antamisen.


Sinulla on myös mahdollisuus käyttää omaa profiiliasi menemällä "Asetukset" ja sitten "Yksityisyys" ja tuoda oma Nostr Address ja avain. Huomaa kuitenkin, että tämä estää Wallet:si kommunikoinnin minibits.cash Nostr- ja LNURL Address -palvelimien kanssa, mikä poistaa Address:n salamaominaisuudet zapien ja maksujen vastaanottamiseksi.


![image](assets/en/09.webp)


## 6️⃣ Varojen vastaanottaminen


Jos haluat aluksi saada varoja, sinun on ladattava Wallet-järjestelmääsi Invoice-salamalla. Prosessi on suoraviivainen: napauta `Topup`, syötä haluamasi summa, lisää valinnaisesti `Memo` ja napauta sitten `Create Invoice`. Sinun on sitten maksettava tämä Invoice käyttämällä toista Lightning Wallet:tä, mikä muuntaa Bitcoin Lightning-maksut ecash-tokeneiksi Minibits Wallet:ssäsi.


![image](assets/en/10.webp)


## 7️⃣ Lähetä varoja


Nyt kun olet rahoittanut Wallet:n, voit lähettää varoja kahdella eri tavalla.


### Lähetä ecash


Ensimmäinen vaihtoehto on lähettää ecash suoraan. Napauta `Lähettää`, valitse sitten `Lähettää ecash`, syötä `Määrä` ja napauta `Luo token.` Tämä luo generate QR-koodin, jonka voit jakaa vastaanottajan kanssa tai antaa hänen skannata sen suoraan laitteellaan. Vastaanottaja näkee kuponkien ilmestyvän hänen Wallet tililleen lähes välittömästi ilman Blockchain maksuja tai vahvistusviiveitä.


![image](assets/en/11.webp)


### Maksa Lightningilla


Toinen vaihtoehto on maksaa Lightningin kautta. Napauta `Lähettää` ja valitse sitten `Maksa Lightningilla`. Voit valita Nostrin `yhteystiedoista` (jos olet yhdistänyt npubin) tai syöttää/liittää Lightning Address-, Invoice- tai LNURL-maksukoodin käyttämällä `Täytä` tai `skannaa`-vaihtoehtoa. Kun olet `Vahvistanut` vastaanottajan, sinua pyydetään syöttämään `Maksettava summa`, lisäämään muistio ja napauta sitten `Vahvista` ja sen jälkeen `Maksa nyt` viimeistelläksesi Lightning-tapahtuman.


![image](assets/en/12.webp)


## 8️⃣ Luo NWC-yhteys


Toinen Minibitsin tehokas ominaisuus on mahdollisuus luoda NWC-yhteyksiä (Nostr Wallet Connect), joiden avulla muut sovellukset voivat pyytää maksuja Wallet:ltäsi paljastamatta yksityisiä avaimiasi.


Määritä tämä valitsemalla "Asetukset", valitsemalla "Nostr Wallet Connect" ja napauttamalla "Lisää yhteys". Anna yhteydelle jokin kuvaava nimi, jolla voit tunnistaa sekä sovelluksen että siihen liittyvän käyttäjätilin. Aseta kohtuullinen päivittäinen enimmäisraja, jotta voit valvoa, kuinka paljon rahaa voi käyttää tämän yhteyden kautta, ja viimeistele asetukset napauttamalla sitten `Save` (Tallenna).


Tämä ominaisuus on erityisen hyödyllinen Nostr Clientsin kaltaisissa palveluissa, joissa haluat ottaa käyttöön automaattisen juomarahan ilman jokaisen tapahtuman manuaalista hyväksyntää.


![image](assets/en/12.webp)


## 🎯 Päätelmät


Minibits tarjoaa helposti lähestyttävän sisäänpääsyn ecash-maailmaan ja tarjoaa yksityisyyteen keskittyviä maksuja, jotka täydentävät Bitcoin-omistuksiasi. Muista aina ylläpitää asianmukaisia varmuuskopioita, harkitse useiden minibittien käyttöä redundanssin varmistamiseksi ja säilytä vain sopivia määriä tässä säilytysratkaisussa.


Lisäresursseja löydät Minibitsin GitHub-arkistosta, viralliselta verkkosivustolta ja Telegram-kanavalta, jossa yhteisö keskustelee aktiivisesti kehityksestä ja ongelmien ratkaisemisesta


- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Verkkosivusto](https://www.minibits.cash/)
- [Telegram](https://t.me/MinibitsWallet)


Ecash-ekosysteemi on vasta kehittymässä, mutta Minibitsin kaltaiset työkalut tekevät tästä tehokkaasta yksityisyyden suojaa koskevasta teknologiasta yhä helpommin tavallisten käyttäjien ulottuvilla.