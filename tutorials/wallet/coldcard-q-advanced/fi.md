---
name: COLDCARD Q - Edistyneet
description: COLDCARD Q:n lisäasetusten käyttäminen
---
![cover](assets/cover.webp)

Edellisessä opetusohjelmassa käsittelimme COLDCARD Q:n alkukonfigurointia ja sen perustoimintoja aloittelijoille. Jos olet juuri saanut COLDCARD Q:n etkä ole vielä määrittänyt sitä, suosittelen, että aloitat tuosta ohjeesta ennen kuin jatkat tästä:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
Tämä uusi opetusohjelma on omistettu COLDCARD Q:n kehittyneille ja vainoharhaisille käyttäjille tarkoitetuille lisäasetuksille. Itse asiassa COLDCARDit eroavat muista laitteistolompakoista monien kehittyneiden turvaominaisuuksiensa ansiosta. Sinun ei tietenkään tarvitse käyttää kaikkia näitä vaihtoehtoja. Valitse vain ne, jotka sopivat turvallisuusstrategiaasi.

**Varoitus**, joidenkin näiden lisäasetusten virheellinen käyttö voi johtaa bitcoinien menettämiseen tai laitteiston lompakon tuhoutumiseen. Siksi suosittelen vahvasti, että luet kunkin vaihtoehdon neuvot ja selitykset huolellisesti.

Ennen kuin aloitat, varmista, että sinulla on fyysinen varmuuskopio 12- tai 24-sanaisesta muistilausekkeestasi, ja tarkista sen oikeellisuus seuraavasta valikosta: `Advanced/Tools > Danger Zone > Seed Functions > View Seed Words`.

![CCQ](assets/fr/01.webp)

## BIP39-salasana

Jos et tiedä, mikä BIP39-salasana on, tai jos sinulle ei ole täysin selvää, miten se toimii, suosittelen lämpimästi, että tutustut etukäteen tähän opetusohjelmaan, joka kattaa teoreettiset perusteet, joita tarvitaan salasanan käyttöön liittyvien riskien ymmärtämiseen:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Muista, että kun olet määrittänyt salasanan lompakkoosi, pelkkä muistisääntösi ei riitä siihen, että pääset takaisin bitcoineihisi. Tarvitset sekä muistitikun että salasanan. Lisäksi sinun on syötettävä tunnuslause joka kerta, kun avaat COLDCARD Q:n lukituksen. Tämä parantaa turvallisuutta, sillä ilman tunnuslausetta COLDCARDin fyysinen käyttö ja PIN-koodin tunteminen eivät ole riittäviä.

COLDCARD-korttien kohdalla sinulla on kaksi vaihtoehtoa salasanan hallintaan:

1. **Klassinen syöttö:** Syötät salasanan manuaalisesti joka kerta, kun käytät laitteistolompakkoa, aivan kuten muidenkin laitteistolompakoiden kanssa. COLDCARD Q helpottaa tätä tehtävää täydellä näppäimistöllä.

2. **Voit salata salasanasi ja tallentaa sen microSD-kortille. Tässä tapauksessa sinun on asetettava microSD-kortti COLDCARD Q -laitteeseen joka kerta, kun käytät sitä. Huomaa, että tämä microSD-kortti toimii vain COLDCARD Q:ssa eikä se ole varmuuskopio. Siksi on erittäin tärkeää, että säilytät myös kopion salasanastasi fyysisellä välineellä, kuten paperilla tai metallilla.

Voit asettaa BIP39-salasanan valitsemalla "*Salasana*"-valikon.

![CCQ](assets/fr/02.webp)

Kirjoita salasana näppäimistöllä. Muista valita vahva salasana (pitkä ja satunnainen) ja ota fyysinen varmuuskopio.

![CCQ](assets/fr/03.webp)

Kun olet asettanut salasanasi, COLDCARD Q näyttää sinulle salasanaan liittyvän uuden lompakon pääavaimen sormenjäljen. Muista tallentaa tämä sormenjälki. Kun syötät salasanasi uudelleen käyttäessäsi laitetta tulevaisuudessa, voit tarkistaa, että näytetty sormenjälki vastaa tallentamaasi sormenjälkeä. Tämä tarkistus varmistaa, ettet ole tehnyt virhettä syöttäessäsi salasanaa.

![CCQ](assets/fr/04.webp)

Voit nyt painaa "*ENTER*" soveltaaksesi tätä salasanaa muistilauseeseesi ja aktivoidaksesi uuden lompakon. Jos haluat tallentaa salasanan microSD-kortille, aseta kortti asianmukaiseen korttipaikkaan ja paina "*1*".

![CCQ](assets/fr/05.webp)

Salasana on nyt käytössä. Avainjälki näkyy aloitusnäytössä ja näytön yläreunassa.

![CCQ](assets/fr/06.webp)

Aina kun avaat COLDCARD Q:n lukituksen, sinun on mentävä "*Passphrase*"-valikkoon ja syötettävä salasanasi samalla tavalla kuin edellä, jotta voit soveltaa sitä laitteeseen tallennettuun muistiinpanoon ja päästä oikeaan Bitcoin-lompakkoon.

![CCQ](assets/fr/07.webp)

Jos olet tallentanut salasanan microSD-kortille, aseta se joka kerta, kun käytät sitä, COLDCARD-korttiin ja avaa "*Salasana*"-valikko. COLDCARD lataa salasanan suoraan microSD-kortilta, joten sinun ei tarvitse syöttää sitä manuaalisesti. Napsauta "*Restore Saved*".

![CCQ](assets/fr/08.webp)

Tarkista, että ladatun salasanan pituus ja ensimmäinen kirjain ovat oikein.

![CCQ](assets/fr/09.webp)

Vahvista, että näytetty sormenjälki vastaa lompakkosi sormenjälkeä ja napsauta "*Restore*".

![CCQ](assets/fr/10.webp)

Muista, että tunnuslauseen käyttäminen tarkoittaa, että sinun on tuotava lompakonhallintaohjelmistoon (kuten Sparrow Walletiin) uusi avainsarja, joka on johdettu muistilauseen ja tunnuslauseen yhdistelmästä. Voit tehdä tämän noudattamalla tämän toisen ohjeen kohtaa "*Konfiguroi uusi lompakko Sparrow'ssa*" :

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
## Vaihtoehtojen avaaminen

COLDCARD-kortit hyötyvät myös lukituksen avaamisprosessissa monista vaihtoehdoista. Tutustutaanpa tarkemmin näihin kehittyneisiin vaihtoehtoihin.

### Trick PIN-koodit

Trick-PIN-koodi on toissijainen PIN-koodi, joka eroaa laitteen alkuperäisen konfiguroinnin aikana määritetystä PIN-koodista. Tätä koodia käytetään käynnistämään tiettyjä ennalta määritettyjä toimintoja heti, kun se syötetään, kun COLDCARD kytketään päälle. Voit määrittää useita Trick PIN -koodeja, joista jokainen liittyy eri toimintoon. Näiden ominaisuuksien avulla voit räätälöidä COLDCARDin henkilökohtaisen turvallisuusstrategian mukaan. Ne ovat erityisen hyödyllisiä fyysisen pakkotilanteen aikana, kuten ryöstön aikana (jota Bitcoin-yhteisössä kutsutaan yleisesti "*5 dollarin jakoavainhyökkäykseksi*").

Jos haluat aktivoida Trick PIN -koodin ja liittää sen toimintoon, avaa valikko `Asetukset > Kirjautumisasetukset > Trick PIN -koodit`.

![CCQ](assets/fr/11.webp)

Valitse "*Lisää uusi temppu*".

![CCQ](assets/fr/12.webp)

Aseta toimintoon liitettävä PIN-koodi ja muista tallentaa se.

![CCQ](assets/fr/13.webp)

Valitse sitten toiminto, joka suoritetaan automaattisesti aina, kun syötät tämän Trick PIN -koodin. Tässä on luettelo PIN-koodille käytettävissä olevista toiminnoista:


- "*Kivi-itse*: Tämä toiminto tuhoaa molemmat COLDCARD Q -sirut, jos Trick PIN-koodi syötetään, jolloin laite on täysin käyttökelvoton. Sen jälkeen sitä on mahdotonta myydä, käyttää uudelleen tai edes palauttaa Coinkitelle. Laitteesta tulee peruuttamattomasti vanhentunut. Tätä ominaisuutta voidaan käyttää ryöstön yhteydessä vakuuttamaan hyökkääjä siitä, ettei hän koskaan pääse käsiksi bitcoineihisi. **Huomaa**: ilman fyysistä varmuuskopiota muistilauseestasi ja mahdollisesta salasanasta bitcoinisi menetetään pysyvästi.

![CCQ](assets/fr/14.webp)


- "*Pyyhi siemen*": Tämä valikko tarjoaa useita toimintoja siemenen poistamiseksi eli COLDCARDin nollaamiseksi sitä tuhoamatta. Toisin kuin "*Brick Self*" -vaihtoehdossa, laite on mahdollista konfiguroida uudelleen käyttämällä varmuuskopiota muistilauseesta. Ilman tätä varmuuskopiota bitcoinit kuitenkin menetetään. Tässä ovat käytettävissä olevat vaihtoehdot:
 - "*Pyyhi ja käynnistä uudelleen* : Poistaa siemenen ja käynnistää COLDCARDin uudelleen näyttämättä mitään tietoja näytöllä.
 - "*Silent Wipe*": Pyyhkii siemenen äänettömästi ja avaa COLDCARDin lukituksen satunnaisella väärennetyllä lompakolla ikään kuin mitään ei olisi tapahtunut.
 - "*Pyyhi -> Lompakko*": Poistaa siemenen huomaamattomasti ja avaa COLDCARDin lukituksen valmiiksi konfiguroidussa toissijaisessa lompakossa, joka on suunniteltu syötiksi. Tämä lompakko voi sisältää pienen osan bitcoin-säästöistäsi hyökkääjän tyydyttämiseksi.
 - "*Sano pyyhitty, lopeta*": Poistaa siemenen ja näyttää näytöllä viestin `Seed is wiped, Stop`.

![CCQ](assets/fr/15.webp)


- "*Duress-lompakko*": Tämän toiminnon avulla Trick PIN-koodi avaa BIP85:n avulla siemenestä johdetun lompakon. Tätä toissijaista lompakkoa voidaan käyttää syöttinä hyökkääjän tyydyttämiseksi. COLDCARD toimii ikään kuin se olisi oikea lompakko, mutta ilman pääkoodia (joka on eri kuin Trick-koodi) hyökkääjä ei koskaan pääse käsiksi oikeaan lompakkoon. Tämän strategian tarkoituksena on saada ihmiset uskomaan, että Trick PIN -koodiin yhdistetty lompakko on ainoa olemassa oleva lompakko.

![CCQ](assets/fr/16.webp)


- "*Login Countdown*": Tämä valikko ryhmittelee toimintoja, joiden suorittamista edeltää lähtölaskenta. **Varoitus**, jotkut niistä voivat tuhota laitteesi tai johtaa bitcoinien menettämiseen. Tässä ovat käytettävissä olevat alatoiminnot:
 - "*Pyyhi ja laske* : Tyhjentää siemenen COLDCARDin muistista ja käynnistää sitten tunnin lähtölaskennan. Ilman muistisäännön tai tunnuslauseen tallentamista bitcoinit menetetään. Tämän vaihtoehdon tarkoituksena on huijata hyökkääjää luulemaan, että laite avaa lukituksen lähtölaskennan päätyttyä, vaikka se itse asiassa palautetaan tehdasasetuksiin.
 - "*Countdown & Brick*": Käynnistää tunnin lähtölaskennan, jonka päätyttyä COLDCARD tuhoaa kaksi suojattua siruaan, jolloin se on pysyvästi käyttökelvoton. Ilman varmuuskopiota bitcoinisi menetetään. Tämä toiminto on suunniteltu huijaamaan hyökkääjää, joka luulee odottavansa lukituksen avaamista, vaikka itse asiassa laite tuhoaa itsensä.
 - "*Just Countdown* : Käynnistää yksinkertaisen tunnin lähtölaskennan, jonka jälkeen COLDCARD käynnistyy uudelleen ilman lisätoimia. Siementä ei poisteta ja laite pysyy ehjänä. Varo sekoittamasta tätä toimintoa seuraavissa kappaleissa käsiteltävään "*Login Countdown*" -vaihtoehtoon, joka lisää lähtölaskennan pääkoodiin antaen samalla pääsyn todelliseen lompakkoon.

![CCQ](assets/fr/17.webp)


- "*Look Blank*": Tämä toiminto saa COLDCARDin näyttämään tyhjältä ja antaa vaikutelman, että siemen on poistettu. Todellisuudessa mitään ei tapahdu ja siemen säilyy ennallaan. Tämä simuloi käyttämätöntä tai nollattua COLDCARDia.

![CCQ](assets/fr/18.webp)


- "*Just Reboot* : Kun Trick PIN -koodia käytetään, COLDCARD yksinkertaisesti käynnistyy uudelleen. Mitään muita toimenpiteitä ei suoriteta.

![CCQ](assets/fr/19.webp)


- "*Delta Mode*": Tämä kokeneille käyttäjille varattu monimutkainen toiminto on suunniteltu torjumaan erittäin kehittyneitä pakkohyökkäyksiä, olivatpa ne sitten valtion tai etuoikeutettuja tietoja hallussaan pitävän sukulaisen tekemiä. Kun Delta Mode on aktivoitu, COLDCARD tarjoaa pääsyn oikeaan lompakkoon, jolloin hyökkääjä voi navigoida ja tarkistaa, että kyseessä on oikea lompakko. Tapahtumien allekirjoitukset on kuitenkin estetty, mikä estää bitcoin-siirrot. Lisäksi pääsy muistilausekkeeseen on estetty, ja kaikki yritykset hakea sitä johtavat sen poistamiseen. Uskottavuuden lisäämiseksi Delta Mode -tilan kanssa käytettävän Trick PIN -koodin on oltava sama etuliite kuin oikean PIN-koodin (jotta näkyvät samat anti-phishing-sanat), mutta loppuliitteen on oltava erilainen.

![CCQ](assets/fr/20.webp)

Kun olet valinnut toiminnon, vahvista valintasi.

![CCQ](assets/fr/21.webp)

Tämän jälkeen voit tarkastella kaikkia määritettyjä Trick PIN-koodeja omassa valikossa.

![CCQ](assets/fr/22.webp)

Valitsemalla olemassa olevan Trick PIN -koodin voit tarkistaa siihen liittyvän toiminnon. Voit myös piilottaa sen valitsemalla "*Hide Trick*", jolloin se ei näy Trick PIN -valikossa. Voit poistaa sen napsauttamalla "*Delete Trick*" tai muuttaa PIN-koodia ja säilyttää siihen liittyvän toiminnon "*Change PIN*" -painikkeella.

![CCQ](assets/fr/23.webp)

"*Lisää, jos väärin*" -vaihtoehto, joka on käytettävissä "*Temppu-PIN*"-valikossa, antaa sinulle mahdollisuuden määrittää tietyn toiminnon, joka käynnistyy automaattisesti tietyn määrän virheellisten pää-PIN-koodin syöttöyritysten jälkeen. Sallittujen yritysten määrä voidaan asettaa konfiguroinnin aikana.

### Scramble Keys

Scramble Keys -vaihtoehdon avulla voit sekoittaa näppäimistön painikkeissa näkyvät numerot, kun kirjoitat PIN-koodia. Tämä toiminto suojaa PIN-koodisi luottamuksellisuutta myös silloin, kun ihmisiä tai kameroita tarkkaillaan.

Voit aktivoida tämän vaihtoehdon valitsemalla valikosta `Asetukset > Kirjautumisasetukset > Sekoitusnäppäimet`.

![CCQ](assets/fr/24.webp)

Valitse vaihtoehto "*Scramble Keys*".

![CCQ](assets/fr/25.webp)

Tästä lähtien, kun avaat COLDCARD Q:n lukituksen, näppäimistön näppäimille annetaan uudet numerot satunnaisesti aina, kun käytät niitä.

![CCQ](assets/fr/26.webp)

### Sisäänkirjautumisen lähtölaskenta

Tämän vaihtoehdon avulla voit asettaa järjestelmällisen lähtölaskennan aina, kun yrität avata COLDCARD-kortin lukituksen. Se voidaan sisällyttää turvallisuusstrategiaasi viivyttämällä laitteen käyttöä varkaustapauksessa tai asettamalla viive ennen maksutapahtuman allekirjoittamista, esimerkiksi suojautuaksesi ryöstön varalta. Tämä lähtölaskenta koskee kuitenkin kaikkia käyttötapojasi, myös silloin, kun käytät COLDCARD-korttiasi laillisesti, mikä myös velvoittaa sinua olemaan kärsivällinen. Varo sekoittamasta tätä vaihtoehtoa "*Just Countdown*" -toimintoon, joka aktivoituu vain, kun käytetään tiettyä Trick PIN -koodia.

Voit määrittää tämän vaihtoehdon valitsemalla valikosta `Asetukset > Kirjautumisasetukset > Kirjautumisen lähtölaskenta`.

![CCQ](assets/fr/27.webp)

Valitse lähtölaskenta-aika. Jos valitset esimerkiksi 1 tunnin, sinun on odotettava 1 tunti jokaista COLDCARD Q:n lukituksen avausyritystä.

![CCQ](assets/fr/28.webp)

Aina kun avaat lukituksen, sinua pyydetään syöttämään PIN-koodisi.

![CCQ](assets/fr/29.webp)

Odota sitten lähtölaskennan asettamaa aikaa.

![CCQ](assets/fr/30.webp)

Lähtölaskennan päätyttyä sinun on annettava PIN-koodisi uudelleen, jotta pääset käyttämään laitetta.

![CCQ](assets/fr/31.webp)

### Laskin Kirjaudu sisään

Tämän vaihtoehdon avulla voit naamioida COLDCARD-korttisi laskimeksi lukituksen avaamisen yhteydessä. Voit aktivoida tämän ominaisuuden valitsemalla valikosta `Asetukset > Kirjautumisasetukset > Laskimen kirjautuminen`.

![CCQ](assets/fr/32.webp)

Aktivoi vaihtoehto valitsemalla se.

![CCQ](assets/fr/33.webp)

Tästä lähtien aina, kun laite kytketään päälle, näyttöön tulee toimiva laskin, jossa on peruskomentoja.

![CCQ](assets/fr/34.webp)

Voit esimerkiksi laskea SHA256-hash-määrityksen "*Suunnitelma B-verkko*".

![CCQ](assets/fr/35.webp)

Jos haluat avata COLDCARDin lukituksen laskentatilasta, aloita kirjoittamalla PIN-koodin etuliite, jota seuraa viiva. Jos PIN-koodisi on esimerkiksi `00-00` (tämä koodi on heikko ja vain esimerkki, joten valitse vahva PIN-koodi), kirjoita `00-`. Tämän jälkeen COLDCARD näyttää kaksi phishingin vastaista sanaa.

![CCQ](assets/fr/36.webp)

Kirjoita sitten koko PIN-koodisi välilyönnillä tai katkoviivalla erotettuna, esimerkiksi: "00 00".

![CCQ](assets/fr/37.webp)

Tämän jälkeen COLDCARD poistuu laskentatilasta ja avaa lukituksen normaalisti.

## COLDCARD-kortin puhdas tuhoaminen

Jos aiot hävittää COLDCARD Q:n esimerkiksi siksi, että käytät nyt toista laitteistolompakkoa, on tärkeää tuhota laite oikein. Näin varmistetaan, että kolmas osapuoli ei voi palauttaa lompakkoasi koskevia tietoja.

Tietojen hävittämisessä on kolme eri tasoa, jotka riippuvat tarpeistasi. Ennen kuin aloitat, varmista, että lompakkosi on tuotu toiseen laitteistolompakkoon, että pääset käsiksi kaikkiin varoihisi ja ennen kaikkea, että sinulla on muistilauseesi ja mahdollinen salasanasi, jotka molemmat ovat toimivia. Ilman lompakon varmuuskopiota COLDCARDin tuhoutuminen johtaa bitcoinien menettämiseen.

Ensimmäisellä tuhoutumistasolla poistetaan vain siemen. Tämä vaihtoehto poistaa muistilausekkeen COLDCARDin muistista, mutta jättää laitteen toiminnalliseksi. Se on ihanteellinen, jos haluat käyttää COLDCARD Q:ta uudelleen myöhemmin. Jos haluat poistaa siemenen muistista, siirry valikkoon `Advanced/Tools > Danger Zone > Seed Functions > Destroy Seed`.

![CCQ](assets/fr/38.webp)

Toisella tuhoutumistasolla COLDCARD-kortin kaksi turvallista sirua poistetaan pysyvästi käytöstä ohjelmiston avulla. Tämä tekee laitteesta täysin käyttökelvottoman. Sitä ei voi myydä, käyttää uudelleen tai palauttaa Coinkitelle: se tuhoutuu pysyvästi. Noudata edellisessä kohdassa kuvattuja vaiheita, jotka koskevat "*Brick Me*"-laitetta PIN-koodia ja anna sitten tarkoituksella tämä PIN-koodi COLDCARDin lukituksen avaamisen yhteydessä.

Kolmannella tasolla COLDCARD Q:n suojatut komponentit tuhotaan fyysisesti. Kuten aiemmin, tämä tekee laitteesta peruuttamattomasti käyttökelvottoman. Tee porakoneella reikä laitteen oikeassa yläkulmassa oleviin kahteen siruun (kun laite on käännetty ylösalaisin), lähelle "*SHOOT HERE*"-merkintää.

**Tärkeitä varotoimenpiteitä** :


- Sähköiskun vaaran välttämiseksi poista paristot laitteesta ja irrota se verkkovirrasta ennen laitteen käsittelyä.
- Odota muutama minuutti laitteen sammuttamisen jälkeen ennen porauksen aloittamista.
- Käytä eristettyjä käsineitä ja suojalaseja turvallisuutesi varmistamiseksi.

![CCQ](assets/fr/39.webp)

Kun sirut on lyöty, älä yritä kytkeä COLDCARD Q:ta uudelleen.

Onneksi olkoon, olet nyt perehtynyt COLDCARD Q:n lisäasetuksiin!

Jos löysit tämän ohjeen hyödylliseksi, olisin hyvin kiitollinen, jos jättäisit vihreän peukalon alle. Voit myös vapaasti jakaa tätä opetusohjelmaa sosiaalisissa verkostoissa. Kiitos paljon!

Suosittelen myös tätä toista opetusohjelmaa, jossa keskustelemme CCQ:n suoran kilpailijan, Ledger Flexin, käytöstä:

https://planb.network/fr/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a