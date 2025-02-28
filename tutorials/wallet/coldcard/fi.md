---
name: Cold Card

description: Bitcoinin yksityisen avaimen luominen, varmuuskopiointi ja käyttö Coldcard-laitteella ja Bitcoin Corella
---

![cover](assets/cover.webp)

Bitcoinin yksityisen avaimen luominen, varmuuskopiointi ja käyttö Coldcard-laitteella ja Bitcoin Corella

## Kattava opas yksityisen avaimen luomiseen Coldcardilla ja sen käyttämiseen Bitcoin Core -solmun käyttöliittymän kautta!

Bitcoin-verkon käytön ytimessä on asymmetrisen kryptografian käsite: avainpari - yksi yksityinen ja toinen julkinen - jotka salakoodaavat ja purkavat dataa, käsite, joka varmistaa viestinnän luottamuksellisuuden.

Bitcoinin tapauksessa tällaisen yksityisen ja julkisen avaimen parin luomalla pystymme säilyttämään bitcoineja (UTXO tai käyttämätön siirtotulo) ja allekirjoittamaan siirtoja niiden käyttämiseksi.

Nykyään on saatavilla useita työkaluja, jotka helpottavat yksityisen avaimen satunnaisen luomisen ja sen varmuuskopioinnin tekstimuodossa käyttäen BIP 39 -standardia, joka määrittää, miten lompakot yhdistävät muistisarjan (siemenlauseen) salausavaimiin. Useimmiten muistisarja koostuu 12 tai 24 sanasta, jotka on turvallisesti varmuuskopioitava, jotta lompakko ja sen bitcoinit voidaan palauttaa myöhemmin.

Tässä artikkelissa opimme, miten luoda yksityinen avain käyttäen Coldcard Mk4:ää, yhtä laajalti käytetyistä ja turvallisista laitteista Bitcoin-maailmassa, käyttäen nopanheitto-menetelmää maksimaalisen entropian varmistamiseksi, ja miten käyttää sitä Bitcoin Coren kanssa ilman suoraa yhteyttä!

> 🧰| Hanki seuraavat työkalut oppaan seuraamiseen:
>
> - Coldcard-laite (Mk3 tai Mk4)
> - MicroSD-kortti (4GB riittää)
> - Vain virtaa siirtävä magneettinen USB-kaapeli (mini-usb Mk3:lle, usb-c Mk4:lle)
> - Yksi tai useampi laadukas noppa

## Uuden muistisarjan luominen Coldcardilla

Aloitamme yksityisen avaimen luomisprosessin tyhjästä, olettaen juuri pakatusta Coldcardista, jolle PIN on jo asetettu (seuraa laitteen käynnistyksen aikana Coldcardin ohjeita).

> 🚨 | Jos haluat nollata jo määritetyn Coldcardin yksityisen avaimen, noudata näitä vaiheita:
> Advanced/Tools > Danger Zone > Seed Functions > Destroy Seed> ✓
> _Huomio_: Coldcard unohtaa yksityisen avaimen näiden vaiheiden jälkeen. Varmista, että olet asianmukaisesti varmuuskopioinut muistisarjasi, jos haluat pystyä palauttamaan sen myöhemmin.

## Seurattavat vaiheet:

Yhdistä Coldcardiin PIN-koodilla > New Seed Words > 24 Word Dice Roll

Suorita 100 noppaheittoa, kirjaa jokaisen heiton tulos 1:stä 6:een Coldcardiin jokaisen heiton jälkeen. Tätä menetelmää harjoittamalla luot 256 tavua entropiaa, mikä suosii täysin satunnaisen yksityisen avaimen luomista. Coinkite tarjoaa myös tarvittavan dokumentaation heidän entropian tuottamisjärjestelmänsä itsenäiseen tarkastamiseen.

![Visual Cold Card Screenshot](assets/guide-agora/1.webp)

Kun 100 noppaheittoa on suoritettu, paina ✓ ja kirjoita sitten saadut 24 sanaa järjestyksessä. Tarkista kahdesti ja paina ✓. Lopuksi jäljellä on vain suorittaa Coldcardilla 24 sanan varmistustesti, ja kas, uusi yksityinen avaimesi on luotu!

Seuraavaksi voit valita, haluatko aktivoida NFC (Mk4) ja USB-toiminnot seuraamalla näytöllä näkyviä vaiheita. Päävalikossa on nyt aika päivittää laitteen firmware. Siirry kohtaan Advanced/Tools > Upgrade Firmware > Show Version, ja tarkista viralliselta verkkosivustolta viimeisin saatavilla oleva versio ja lataa se. On suositeltavaa päivittää Coldcard, jotta voit hyödyntää maksimaalista turvallisuutta.
Ennen jatkamista on suositeltavaa merkitä ylös yksityiseen avainpariin liitetty Master Key Fingerprint (XFP). Tämä tieto mahdollistaa nopean varmistuksen, jos olet oikeassa lompakossa esimerkiksi palautustilanteessa. Siirry kohtaan Advanced/Tools > View Identity > Master Key Fingerprint (XFP) ja kirjoita ylös saatu kahdeksan merkin alfanumeerinen sarja. XFP:n voi merkitä samaan paikkaan kuin mnemonic-lauseen, se ei ole arkaluonteista tietoa.
> 💡 On suositeltavaa testata mnemonic-lauseesi varmuuskopiota eri ohjelmistossa. Tehdäksesi tämän turvallisesti, katso artikkelimme Varmista Bitcoin-lompakkosi varmuuskopio Tailsilla alle viidessä minuutissa.

## Turvallisuusbonus: "Salainen lause" (valinnainen)

Salalause (secret phrase) on loistava lisä lompakon asetuksiin, jotta voit lisätä turvallisuustasoa suojellaksesi bitcoinejasi. Salalause toimii eräänlaisena 25. sanana mnemonic-lauseessa. Kun salalause lisätään, luodaan täysin uusi lompakko yhdessä yksityisen avaimen ja siihen liittyvän mnemonic-lauseen kanssa. Uutta mnemonic-lausetta ei tarvitse kirjoittaa ylös, sillä tähän lompakkoon pääsee käsiksi yhdistämällä alkuperäisen mnemonic-lauseen valittuun salalauseeseen.

Tavoitteena on merkitä salalause erilleen mnemonic-lauseesta, koska hyökkääjä, jolla on pääsy molempiin, pääsee käsiksi varoihin. Toisaalta hyökkääjä, jolla on pääsy vain toiseen näistä, ei pääse käsiksi varoihin, ja juuri tämä erityinen etu optimoi lompakon asetusten turvallisuustason.

![Salalauseen lisääminen johtaa täysin erilaiseen lompakkoon](assets/guide-agora/2.webp)

## Askeleet salalauseen lisäämiseen Coldcardilla:

Passphrase > Add Words (suositeltu) > Apply. Laite näyttää salalauseella luodun uuden lompakon XFP:n, joka tulisi merkitä ylös salalauseen kanssa aiemmin mainituista syistä.

> 💡 Lisäresursseja salalauseeseen liittyen:

    https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af
    https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/
    https://armantheparman.com/passphrase/

## Lompakon vieminen Bitcoin Coreen

Lompakko on nyt valmis viemiseen ohjelmistoon, jotta se voi olla vuorovaikutuksessa Bitcoin-verkon kanssa. Tässä oppaassa käytämme Bitcoin Corea (v24.1).

Katso asennus- ja konfigurointioppaamme Bitcoin Corelle:

> Oma solmu Bitcoin Coren kanssa - https://agora256.com/faire-tourner-son-propre-noeud-avec-bitcoin-core/
>
> Torin konfigurointi Bitcoin Core -solmulle - https://agora256.com/configuration-tor-bitcoin-core/

Aseta ensin mikro SD-kortti Coldcardiin, sitten vie lompakko Bitcoin Corelle seuraavien vaiheiden mukaisesti: Advanced/Tools > Export Wallet > Bitcoin Core. Kaksi tiedostoa kirjoitetaan mikro SD-kortille: bitcoin-core.sig & bitcoin-core.txt. Aseta mikro SD-kortti tietokoneeseen, jossa Bitcoin Core on asennettu, ja avaa .txt-tiedosto. Näet rivin "For wallet with master key fingerprint." Varmista, että kahdeksan merkin XFP vastaa sitä, jonka merkitsit ylös luodessasi yksityisen avaimen.
Ennen kuin noudatat tiedoston ohjeita, aloitetaan valmistelemalla lompakko Bitcoin Core -käyttöliittymässä seuraavien vaiheiden mukaisesti: siirry Tiedosto-välilehteen > Luo lompakko. Valitse lompakollesi nimi (vaihdettavissa termiin "porte-monnaie" Core:ssa) ja valitse vaihtoehdot Poista yksityiset avaimet käytöstä, Luo tyhjä lompakko ja Lompakon kuvaukset, kuten alla olevassa kuvassa näytetään. Paina sen jälkeen Luo-painiketta.
![luo lompakko](assets/guide-agora/3.webp)

Kun lompakko on luotu Bitcoin Core:ssa, siirry Ikkuna-välilehteen > Konsoli ja varmista, että sivun yläosassa valittuna oleva lompakko näyttää luomasi lompakon nimen.

Nyt, .txt-tiedostossa, jonka Coldcard aiemmin generoi, kopioi rivi, joka alkaa sanalla importdescriptors, ja liitä se Bitcoin Core -konsoliin. Vastauksen pitäisi sisältää rivi "success": true.

![solmujen ikkuna](assets/guide-agora/4.webp)

Jos vastaus sisältää "message": "Ranged descriptors should not have a label", poista kopioitavasta rivistä .txt-tiedostosta merkintä "label": "Coldcard xxxx0000" ja liitä koko rivi takaisin Bitcoin Core -konsoliin.

Apua: [https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md](https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md)

## Lompakon tuonnin validointi Bitcoin Core:ssa

Jotta voidaan varmistaa, että toimenpide onnistui, on tarpeen validoida, että haluttu lompakko on tuotu Bitcoin Coreen. Yksinkertainen menetelmä tämän vahvistamiseen on tarkistaa, että Coldcardissa generoidut osoitteet vastaavat Bitcoin Core:ssa generoituja osoitteita.

Bitcoin Core: Vastaanota > Luo uusi vastaanotto-osoite
Coldcard: Osoite Explorer > Valitse osoite, joka alkaa bc1q:lla. Coldcardin osoitteen 'bc1q' tulisi vastata Bitcoin Core:ssa näytettyä osoitetta.
Vastaanottaminen ja lähettäminen 'air-gapped' -tilassa

Vastaanottaminen on erittäin yksinkertaista; paina vain Vastaanota, nimeä transaktio (valinnainen, mutta suositeltava) ja Luo uusi vastaanotto-osoite. Sen jälkeen jäljellä on vain jakaa osoite lähettäjän kanssa.

Nyt, tämän Coldcard + Bitcoin Core -asetelman avainelementti on transaktioiden lähettäminen ilman, että Coldcard ja sen yksityinen avain ovat yhteydessä internetiin, menetelmällä, jota kutsutaan air-gappediksi, joka käyttää TBSP (PSBT - Partially Signed Bitcoin Transactions) -toimintoa Bitcoinissa.
Periaatteessa käytämme Bitcoin Core -käyttöliittymää transaktion rakentamiseen, jonka sitten vietämme mikro SD-kortin kautta Coldcardiin allekirjoitettavaksi, ja palautamme sitten allekirjoitetun transaktiotiedoston Bitcoin Coreen ja lähetämme transaktion verkkoon. Meidän on toimittava näin, koska Bitcoin Coreen tuotuun lompakkoon ei ole yksityistä avainta, vain julkinen avain (joka mahdollistaa vastaanotto-osoitteidemme generoinnin), joten emme voi suoraan ohjelmistossa allekirjoittaa transaktiota käyttääksemme bitcoinejamme.

Ennen kuin jatkat, varmista, että seuraavat vaihtoehdot ovat käytössä Asetukset > Lompakko:

> - Ota käyttöön kolikoiden hallintatoiminnot
> - Käytä vahvistamattomia kolikoita (Valinnainen)
> - Ota TBPS-tarkistukset käyttöön

![vaihtoehto](assets/guide-agora/5.webp)

### Vaiheet lähettämiseen air-gapped -tilassa:
Lähetä > Syötteet > valitse haluttu utxo, syötä sen jälkeen vastaanottajan osoite kohtaan Maksuun. Siirtomaksu: Valitse... > Mukautettu > Anna siirtomaksu (Bitcoin Core laskee satsit/kilobitti eikä satsi/bitti kuten useimmat muut lompakko-ratkaisut. Joten 4000 satsia/kilobitti = 4 satsia/bittiä). Luo allekirjoittamaton siirto > tallenna tiedosto micro SD -kortillesi ja aseta se Coldcardiin.
Coldcardissa paina Valmis allekirjoitettavaksi, tarkista siirtotiedot, paina sitten ✓ ja aseta micro SD -kortti takaisin tietokoneeseen, kun allekirjoitetut tiedostot on luotu.

Takaisin Bitcoin Core:ssa, mene Tiedosto-välilehteen > Lataa TBSP tiedostosta ja syötä allekirjoitettu siirtotiedosto .psbt. PSBT Toiminnot -laatikko ilmestyy näytölle, vahvistaen, että siirto on täysin allekirjoitettu ja valmis lähetettäväksi. Kaikki mikä jää tehtäväksi, on painaa Lähetä siirto.

![PSBT toiminnot](assets/guide-agora/6.webp)

### Yhteenveto

Yhdistelmä Coldcard-laitteesta ja Bitcoin Coresta, jossa ajat omaa noodiasi, on tehokas. Lisää tähän yksityinen avain, joka on luotu 100 nopanheitolla ja salasanalla, ja lompakkokokoonpanosi muuttuu kehittyneeksi ja lujaksi linnoitukseksi.

Ota meihin vapaasti yhteyttä jakamaan kommenttisi ja kysymyksesi! Tavoitteenamme on jakaa tietoa ja lisätä ymmärrystämme päivä päivältä.