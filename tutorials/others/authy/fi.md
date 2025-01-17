---
name: Authy 2FA
description: Kuinka käyttää 2FA-sovellusta?
---
![cover](assets/cover.webp)

Nykyään kaksivaiheinen tunnistautuminen (2FA) on muodostunut olennaiseksi osaksi online-tilien turvallisuuden parantamista luvattomalta pääsyltä. Kyberhyökkäysten lisääntyessä pelkän salasanan varassa oleva tilien suojaus on joskus riittämätön. 2FA tuo mukanaan lisäkerroksen turvallisuutta vaatimalla toisen tunnistautumismuodon salasanan lisäksi. Tämä varmennus voi ottaa useita muotoja, kuten koodin lähettämisen SMS-viestillä, dynaamisen koodin generoinnin omistetulla sovelluksella tai fyysisen turva-avaimen käytön. 2FA:n käyttö vähentää merkittävästi tilisi joutumisen vaaraa kompromissoiduksi, jopa salasanasi varastamisen tapauksessa.

## 2FA tunnistautumissovellusten kautta

Tutkimme muita ratkaisuja, kuten fyysisiä turva-avaimia muissa oppaissa, mutta tässä yhdessä haluan erityisesti keskustella 2FA-sovelluksista. Näiden sovellusten toiminta on melko yksinkertaista: kun 2FA on aktivoitu tilillä, jokaisen kirjautumisen yhteydessä sinulta pyydetään paitsi tavallista salasanaasi myös 6-numeroinen koodi. Tämän koodin generoi 2FA-sovelluksesi. Tärkeä ominaisuus tässä 6-numeroisessa koodissa on, että se ei ole staattinen; sovellus generoi uuden koodin joka 30. sekunti.
![AUTHY 2FA](assets/notext/01.webp)
Koodin uusiutuminen joka 30. sekunti tekee hyökkääjän pääsyn tilillesi erittäin vaikeaksi. Tämä järjestelmä estää hyökkääjiä käyttämästä uudelleen varastettua tai kaapattua koodia, koska se vanhenee nopeasti. Näin ollen, vaikka hyökkääjä onnistuisi saamaan koodin, hänellä on käytössään vain hyvin lyhyt aikaikkuna ennen kuin uusi koodi vaaditaan. Lisäksi se, että koodi muuttuu niin usein, vähentää merkittävästi aikaa, joka hakkerilla on arvata koodi brute force -menetelmällä.

2FA tunnistautumissovellusten kautta edustaa siis helppokäyttöistä ja ilmaista menetelmää parantaa merkittävästi online-tiliesi turvallisuutta.

On olemassa lukuisia sovelluksia 2FA:n asettamiseen, joista Google Authenticator ja Microsoft Authenticator ovat tunnetuimpia. Tässä oppaassa haluan kuitenkin esitellä toisen, vähemmän tunnetun ratkaisun nimeltä Authy. Kaikki nämä sovellukset toimivat käyttäen samaa TOTP (*Time based One Time Password*) -protokollaa, mikä tekee niiden käytöstä melko samankaltaista.
Authy tarjoaa useita etuja muihin suurten teknologiayritysten ratkaisuihin verrattuna. Ensinnäkin se mahdollistaa 2FA-tokeneidesi synkronoinnin useiden laitteiden välillä, mikä voi olla hyödyllistä puhelimen katoamisen tai vaihdon yhteydessä. Authy mahdollistaa myös salatun varmuuskopion luomisen ja sen tallentamisen verkossa, varmistaen, että et koskaan menetä pääsyä tokeneihisi, vaikka menettäisit päälaiteesi. Käyttöliittymän näkökulmasta henkilökohtaisesti koen, että Authy tarjoaa myös miellyttävämmän ja intuitiivisemman kokemuksen kuin sen vaihtoehdot.

## Kuinka asentaa Authy?

Älypuhelimellasi, mene sovelluskauppaan (Google Play Store tai Apple Store) ja etsi "*Twilio Authy Authenticator*".

- [Apple](https://apps.apple.com/us/app/twilio-authy/id494168017)
- [Android](https://play.google.com/store/apps/details?id=com.authy.authy)
![AUTHY 2FA](assets/notext/02.webp)
Sovelluksen ensimmäisellä käynnistyksellä sinun tulee luoda tili. Valitse maasi suuntanumero sekä puhelinnumerosi, sitten klikkaa "*Submit*".
![AUTHY 2FA](assets/notext/03.webp)
Syötä sähköpostiosoitteesi koodin palautusta varten.
![AUTHY 2FA](assets/notext/04.webp)Sähköposti lähetetään sinulle osoitteesi vahvistamiseksi. Syötä saamasi 6 numeroa vahvistaaksesi.
![AUTHY 2FA](assets/notext/05.webp)
Valitse kaksi saatavilla olevaa menetelmää puhelinnumerosi vahvistamiseksi. Jos valitset SMS-viestin vastaanottamisen, syötä viestillä saamasi 6-numeroinen koodi vahvistaaksesi numerosi.
![AUTHY 2FA](assets/notext/06.webp)
Onneksi olkoon, Authy-tilisi on luotu!
![AUTHY 2FA](assets/notext/07.webp)
## Kuinka Authy konfiguroidaan?

Aloittaaksesi, mene sovelluksen asetuksiin klikkaamalla kolmea pientä pistettä näytön oikeassa yläkulmassa.
![AUTHY 2FA](assets/notext/08.webp)
Klikkaa sitten "*Asetukset*".
![AUTHY 2FA](assets/notext/09.webp)
"*Oma tili*" -välilehdessä sinulla on mahdollisuus muokata tiliäsi. Suosittelen lisäämään PIN-koodin sovellukseen valitsemalla "*Sovelluksen suojaus*". Tämä lisää ylimääräisen turvakerroksen sovelluksesi käyttöön.
![AUTHY 2FA](assets/notext/10.webp)
"*Tilit*" -välilehdessä voit asettaa varmuuskopion tokeneillesi. Tämä varmuuskopio mahdollistaa koodiesi palauttamisen ongelmatilanteessa. Se salataan käyttämällä salasanaa, jonka sinun täytyy määritellä. On tärkeää, että tämä salasana on vahva ja säilytetään turvallisessa paikassa. Tämän varmuuskopion asettaminen ei välttämättä ole pakollista, jos sinulla on muita palautusmenetelmiä, kuten toinen laite samalla Authy-tilillä, esimerkiksi.
![AUTHY 2FA](assets/notext/11.webp)"*Laitteet*" -välilehdessä voit nähdä kaikki Authy-tiliisi synkronoidut laitteet. Sinulla on mahdollisuus poistaa käytöstä usean laitteen käyttö, mikä rajoittaa pääsyn tilillesi vain kyseiselle laitteelle. Jos käytät vain yhtä laitetta, tämä voi lisätä tilisi turvallisuutta, mutta varmista, että sinulla on toinen varmuuskopio menetelmä, jos menetät kyseisen laitteen.

Jos haluat sallia muiden laitteiden lisäämisen, suosittelen aktivoimaan vaihtoehdon, joka vaatii vahvistuksen tällä hetkellä valtuutetuilta laitteilta Authy-tililläsi ennen uuden laitteen lisäämistä.
![AUTHY 2FA](assets/notext/12.webp)
Uuden laitteen lisäämiseksi toista vain aiemmin esitetty asennusprosessi käyttäen samoja tunnistetietoja. Sinua pyydetään sitten vahvistamaan tämä uusi pääsy päälaitteeltasi.

## Kuinka ottaa käyttöön 2FA tunnistus tilillä?

Jotta voit ottaa käyttöön 2FA-tunnistuskoodin sovelluksen, kuten Authyn kautta tilillä, tilin on tuettava tätä ominaisuutta. Nykyään suurin osa online-palveluista tarjoaa tämän 2FA-vaihtoehdon, mutta näin ei aina ole. Otetaan esimerkiksi Proton mail -tili, jonka esittelin toisessa oppaassa:

https://planb.network/tutorials/others/general/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
![AUTHY 2FA](assets/notext/13.webp)
Yleensä löydät tämän 2FA-vaihtoehdon tilisi asetuksista, usein "*Salasana*" tai "*Turvallisuus*" -osion alla.
![AUTHY 2FA](assets/notext/14.webp)
Kun aktivoit tämän vaihtoehdon Proton mail -tililläsi, sinulle esitetään QR-koodi. Sinun täytyy sitten skannata tämä QR-koodi Authy-sovelluksellasi.
![AUTHY 2FA](assets/notext/15.webp)
Authyssa, klikkaa "*+*" -painiketta.
![AUTHY 2FA](assets/notext/16.webp)
Napsauta "*Skannaa QR-koodi*". Skannaa sitten QR-koodi verkkosivustolta. ![AUTHY 2FA](assets/notext/17.webp)
Sinulla on myös mahdollisuus säätää käyttäjänimeäsi tarvittaessa. Muutosten jälkeen napsauta "*TALLENNA*" -painiketta.
![AUTHY 2FA](assets/notext/18.webp)
Authy näyttää tämän jälkeen dynaamisen 6-numeroisen koodisi, joka on tietyn tilin erityinen ja uusiutuu joka 30. sekunti.
![AUTHY 2FA](assets/notext/19.webp)
Syötä tämä koodi verkkosivustolle viimeistelläksesi 2FA-asetuksen.
![AUTHY 2FA](assets/notext/20.webp)
Jotkut sivustot tarjoavat myös palautuskoodit 2FA:n aktivoimisen jälkeen. Nämä koodit mahdollistavat tilillesi pääsyn, jos menetät pääsyn Authy-sovellukseesi. Suosittelen säilyttämään ne turvallisessa paikassa.
![AUTHY 2FA](assets/notext/21.webp)Tilisi on nyt suojattu kaksivaiheisella todennuksella Authy-sovelluksen kautta.
![AUTHY 2FA](assets/notext/22.webp)
Joka kerta kun kirjaudut tilille, sinun on annettava Authyn generoima dynaaminen koodi. Voit nyt suojata kaikki tämän 2FA-menetelmän kanssa yhteensopivat tilisi. Lisätäksesi uuden tilin Authyyn, napsauta sovelluksen oikeassa yläkulmassa olevia kolmea pientä pistettä.
![AUTHY 2FA](assets/notext/23.webp)
Napsauta sitten "*Lisää tili*".
![AUTHY 2FA](assets/notext/24.webp)
Noudata samoja vaiheita kuin ensimmäisen tilin kohdalla. Eri dynaamiset koodisi näkyvät Authyn kotisivulla.