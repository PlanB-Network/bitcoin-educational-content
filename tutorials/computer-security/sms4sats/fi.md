---
name: SMS4Sats
description: Vastaanota ja lähetä tekstiviestejä nimettömänä maksamalla Bitcoin Lightning -nimellä
---

![cover](assets/cover.webp)



Tekstiviestivarmennus on tullut välttämättömäksi monissa verkkopalveluissa. Verkkosivustot vaativat lähes järjestelmällisesti puhelinnumeron, olipa kyse tilin luomisesta alustalle, rekisteröinnin vahvistamisesta tai henkilöllisyyden vahvistamisesta. Tämä laajalle levinnyt käytäntö aiheuttaa suuren ongelman kaikille, jotka haluavat säilyttää yksityisyytensä: henkilökohtaisesta numerosta tulee pysyvä tunniste, joka yhdistää erilaiset digitaaliset toimintasi todelliseen henkilöllisyyteesi ja avaa oven ei-toivotuille kaupallisille pyynnöille.



**SMS4Sats** vastaa tähän ongelmaan tarjoamalla tilapäisiä puhelinnumeroita tekstiviestien vastaanottamista ja lähettämistä varten. Palvelu erottuu muista rekisteröimättömyydellään ja yksinoikeudella Bitcoin-maksulla Lightning Network:n kautta. Muutamaa satoshia vastaan saat kertakäyttönumeron, jonka avulla voit vahvistaa rekisteröinnin paljastamatta henkilökohtaista numeroasi.



Tämä opetusohjelma opastaa sinut kolmen SMS4Sats-ominaisuuden läpi: vastaanota vahvistustekstiviesti, lähetä nimetön tekstiviesti ja vuokraa väliaikainen numero useaksi tunniksi.



## Mikä on SMS4Sats?



SMS4Sats on verkkopalvelu, joka on saatavilla osoitteessa [sms4sats.com](https://sms4sats.com) ja joka mahdollistaa nimettömien tekstiviestien hallinnan Bitcoin Lightning -maksun avulla. Palvelu tarjoaa kolme erillistä toimintoa: kertakäyttöisten vahvistuskoodien vastaanottaminen, tekstiviestien lähettäminen mihin tahansa numeroon ja tilapäisten numeroiden vuokraaminen useiksi tunneiksi.



### Filosofia ja toimintamalli



Hanke on suunniteltu siten, että varmistetaan mahdollisimman suuri luottamuksellisuus ja taloudellinen riippumattomuus. SMS4Sats ei vaadi tilin luomista ja hyväksyy vain Bitcoin Lightning -maksuja, joten henkilötietojen antaminen ei ole tarpeen. Ei sähköpostiosoitetta, ei luottokorttia, ei henkilökohtaisia tietoja ei tarvita. Vain Lightning-maksua tarvitaan palvelujen käyttämiseen.



Palvelu tukee yli 400 sivustoa ja sovellusta noin 120 maassa, ja se kattaa suurimman osan yleisimmistä todentamistarpeista. Tämä laaja maantieteellinen kattavuus mahdollistaa rekisteröintien validoinnin eri alustoilla sosiaalisista verkostoista viestipalveluihin.



### Ehdollinen maksumalli



SMS4Sats käyttää tekstiviestien vastaanottotoiminnoissaan ehdollisia salamalaskuja (hodl-laskuja). Tämä mekanismi varmistaa, että sinua veloitetaan vain, jos tekstiviesti todella vastaanotetaan. Jos yhtään viestiä ei saavu määrätyn ajan kuluessa (enintään 20 minuuttia), maksu peruuntuu automaattisesti ja satoshi palautetaan wallet:een. Tämä takuu ei koske lähetys- ja vuokraustoimintoja, joita ei palauteta.



## Kolmen SMS4Satin ominaisuudet



SMS4Sats-käyttöliittymä on järjestetty kolmen välilehden ympärille, jotka vastaavat kolmea eri käyttötarkoitusta: **RECEIVE** vahvistuskoodien vastaanottamiseksi, **SEND** nimettömien tekstiviestien lähettämiseksi ja **RENT** tilapäisen numeron vuokraamiseksi.



### Vastaanota tekstiviesti



Pääominaisuuden avulla voit saada väliaikaisen numeron, jolla saat ainutlaatuisen tarkistuskoodin. Kun koodi on saatu ja käytetty, numero poistetaan pysyvästi käytöstä.



### Lähetä tekstiviesti



Tämän ominaisuuden avulla voit lähettää tekstiviestin mihin tahansa puhelinnumeroon paljastamatta henkilöllisyyttäsi. Vastaanottaja saa viestin nimettömästä numerosta.



### Vuokraa esitys



Käyttäjille, jotka haluavat vastaanottaa useita tekstiviestejä yhteen numeroon, SMS4Sats tarjoaa tilapäisen vuokrausvaihtoehdon. Tämän vaihtoehdon avulla voit vastaanottaa ja lähettää useita viestejä vuokra-aikana.



**Hintoja koskeva huomautus** : Tässä oppaassa esitetyt hinnat ovat suuntaa-antavia. Ne vaihtelevat numeron sijaintimaan, kohdepalvelun ja nykyisen kysynnän mukaan. Esimerkiksi tekstiviesti Telegram Ranskaan voi maksaa 1 500-5 000 satoshia olosuhteista riippuen. Tarkista aina salamalaskun tarkka summa ennen maksamista.



## Vastaanota vahvistustekstiviesti



Katsotaanpa yksityiskohtaisesti, miten SMS4Satsin avulla saat vahvistuskoodin, ja havainnollistetaan tätä Telegram-tilin luomisella.



### Vaihe 1: Valitse maa ja palvelu



Mene osoitteeseen [sms4sats.com](https://sms4sats.com) ja pysy **RECEIVE**-välilehdellä. Valitse haluamasi numeron maa pudotusvalikosta. Jos tilauksesi kohdepalvelu on luettelossa, valitse se optimoidaksesi vastaanottomahdollisuudet.



![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)



Tässä esimerkissä valitaan maaksi Ranska ja kohdepalveluksi Telegram. Jatka seuraavaan vaiheeseen napsauttamalla **NEXT**.



### Vaihe 2: Maksa Lightning-lasku



Salamalasku näytetään QR-koodin muodossa. Summa vaihtelee valitun maan ja palvelun mukaan. Skannaa QR-koodi Lightning wallet -laitteella tai kopioi lasku maksaaksesi sen manuaalisesti.



![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)



Huomaa tärkeä viesti: "Ei tekstiviestikoodia = ei maksua". Jos et saa tekstiviestiä, maksusi peruuntuu automaattisesti ja palautetaan enintään 20 minuutin kuluessa.



### Vaihe 3: Hanki väliaikainen numero



Kun maksu on vahvistettu, tilapäinen puhelinnumero näytetään välittömästi. Laskuri näyttää tekstiviestin vastaanottamiseen jäljellä olevan ajan.



![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)



Kopioi tämä numero (tässä +33 7 74 70 09 66), jotta voit käyttää sitä palvelussa, johon haluat rekisteröityä.



### Vaihe 4: Käytä kohdepalvelun numeroa



Kirjoita tilapäinen numero sovellukseen tai verkkosivustolle, jossa luot tilisi. Esimerkissämme Telegram, anna numero, vahvista se ja odota vahvistuskoodia.



![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)



Prosessi on identtinen perinteisen rekisteröinnin kanssa: syötät numeron, Telegram lähettää vahvistuskoodin tekstiviestillä ja viimeistelet sitten tilin luomisen.



### Vaihe 5: Hae vahvistuskoodi



Palaa SMS4Sats-käyttöliittymään. Heti kun tekstiviesti on vastaanotettu, aktivointikoodi tulee automaattisesti näkyviin. Klikkaa **KOPIOI KOODI** kopioidaksesi sen helposti.



![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)



Syötä tämä koodi kohdepalveluun viimeistelläksesi rekisteröinnin. Tämän jälkeen väliaikainen numero poistetaan pysyvästi käytöstä.



## Lähetä anonyymi tekstiviesti



SMS4Satsin avulla voit myös lähettää tekstiviestejä mihin tahansa numeroon paljastamatta henkilöllisyyttäsi.



### Vaihe 1: Viestin kirjoittaminen



Napsauta **LÄHETÄ**-välilehteä. Kirjoita kohdepuhelinnumero ja sen kansainvälinen suuntanumero ja kirjoita viestisi (enintään 1600 merkkiä).



![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)



Jatka maksua napsauttamalla **NEXT**.



### Vaihe 2: Maksa ja lähetä



Maksa näytetty Lightning-lasku. Kun maksu on vahvistettu, tekstiviesti lähetetään välittömästi vastaanottajalle.



![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)



Näyttöön tulee vahvistuskoodi, joka vahvistaa, että viesti on lähetetty. Vastaanottaja saa tekstiviestin nimettömästä numerosta.



## Vuokraa väliaikainen numero



Jos tarvitset useita tekstiviestejä samaan numeroon, voit vuokrata numeron useaksi tunniksi RENT-toiminnon avulla.



### Vuokrakokoonpano



Napsauta välilehteä **VUOKRA**. Valitse maa ja kesto.



![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)



**Tärkeitä huomioitavia seikkoja:**




- Hinnat vaihtelevat maittain ja oleskelun keston mukaan
- Vuokrauksia ei voi palauttaa**, toisin kuin kertakäyttöisiä tekstiviestejä
- Vuokralle otetut numerot eivät yleensä toimi Telegram:n kanssa
- Tämä vaihtoehto soveltuu useiden palvelujen tilaamiseen peräkkäin



Kun olet napsauttanut **JATKA** ja maksanut Lightning-laskun, saat numeron, jota voit käyttää vuokra-ajan ajan tekstiviestien vastaanottamiseen ja lähettämiseen.



## Edut ja rajoitukset



### Kohokohdat



**Henkilötietoja ei tarvita**: Rekisteröimätön malli takaa, että henkilötietoja ei kerätä.



**Kolme lisätoimintoa**: Vastaanottaa, lähettää ja vuokrata kattaa useimmat tarpeet.



**Maksu vain Bitcoin** : Lightning Network mahdollistaa välittömät ja pseudonyymit transaktiot.



**Automaattinen korvaus**: Kun vastaanotat tekstiviestejä, hodl-laskujärjestelmä takaa, että maksat vain, jos tekstiviesti saapuu.



### Huomioon otettavat rajoitukset



**Relatiivinen tekstiviestikanavan turvallisuus**: Tekstiviestikoodit eivät ole vankka todentamismenetelmä, eikä niitä tulisi käyttää arkaluonteisiin tileihin.



**Muuttujien yhteensopivuus**: Monet sivustot havaitsevat ja estävät virtuaaliset numerot. Useita yrityksiä voi olla tarpeen.



**Ei uudelleenkäytettävät numerot**: Kertakäytön jälkeen numero kierrätetään, eikä sitä voida ottaa talteen.



**Vuokraa ei palauteta**: Toisin kuin kertaluonteisilla tekstiviesteillä, vuokrauksilla ei ole rahanpalautustakuuta.



## Parhaat käytännöt



### Käytä Toria saadaksesi enemmän yksityisyyttä



SMS4Satsiin pääsee [Torin] kautta (sms4sat6y7lkqq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion). Tämä konfiguraatio peittää IP-osoitteesi, kun käytät palvelua.



### Vältä kriittisiä tilejä



Älä koskaan käytä kertakäyttönumeroa tärkeillä tileilläsi (pankki, pääsähköposti). Jos nämä alustat vaativat sinua vahvistamaan numerosi uudelleen myöhemmin, menetät tilisi käyttöoikeuden.



### Erottele digitaaliset identiteettisi



Pseudonyymitilejä varten kannattaa tilapäinen numero yhdistää kertakäyttöiseen sähköpostiosoitteeseen ja selaimeen, joka on eristetty tavanomaisesta käytöstäsi.



### Valitse tukeva 2FA



Kun tilisi on luotu, aktivoi vahvemmat todennusratkaisut: TOTP-sovellus (Aegis, Ente Auth) tai FIDO2 fyysinen turvaavain.



## Päätelmä



SMS4Sats on täydellinen ratkaisu luottamuksellisten tekstiviestien hallintaan. Halusitpa sitten vastaanottaa vahvistuskoodin, lähettää nimettömän viestin tai vuokrata tilapäisen numeron, palvelu täyttää monenlaiset luottamuksellisuustarpeet Bitcoin Lightning -maksun ansiosta.



Muista kuitenkin sen rajoitukset: palvelu ei takaa ehdotonta anonymiteettiä, eikä se sovellu arkaluonteisille tai pitkäaikaisille tileille. Viisaasti käytettynä ja tietoisina sen rajoituksista SMS4Sats on käytännöllinen väline, jolla voit saada takaisin hallinnan puhelinliikenteeseesi.



## Resurssit





- [SMS4Satsin virallinen verkkosivusto](https://sms4sats.com)
- [Service FAQ](https://sms4sats.com/faq)
- [Tor-osoite](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)