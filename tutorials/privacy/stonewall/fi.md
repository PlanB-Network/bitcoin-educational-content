---
name: Stonewall
description: Ymmärtäminen ja Stonewall-siirtojen käyttäminen
---
![cover stonewall](assets/cover.webp)

***VAROITUS:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta, Samourai Wallet -sovelluksen käyttö vaatii nyt yhteyden omaan Dojoon toimiakseen kunnolla. Tästä huolimatta Stonewall-siirrot eivät ole lainkaan vaikuttuneet ja niitä voidaan edelleen suorittaa ilman ongelmia. Itse asiassa nämä siirtotyypit suoritetaan autonomisesti, ilman tarvetta ulkopuoliseen yhteistyöhön tai yhteyteen Sorobanin kautta.*

_Seuraamme tiiviisti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voitte olla varmoja, että päivitämme tätä opasta uuden tiedon tultua saataville._

_Tämä opas on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme tue tai kannusta näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

---

> *"Murtakaa lohkoketjuanalyysin oletukset matemaattisesti todistettavalla epäilyllä lähettäjän ja vastaanottajan välillä transaktioissanne."*

## Mikä on Stonewall-siirto?
Stonewall on tietynlainen Bitcoin-siirto, jonka tavoitteena on lisätä käyttäjän yksityisyyttä siirron aikana jäljittelemällä coinjoinia kahden osapuolen välillä, olematta kuitenkaan sellainen. Itse asiassa tämä siirto ei ole yhteistyöllinen. Käyttäjä voi rakentaa sen yksin, käyttäen ainoastaan omia UTXO:itaan syötteinä. Siksi voit luoda Stonewall-siirron mihin tahansa tilanteeseen tarvitsematta koordinoida toisen käyttäjän kanssa.

Stonewall-siirron toiminta on seuraava: syötteenä lähettäjä käyttää 2 UTXO:ta, jotka kuuluvat hänelle. Tuloksena siirto tuottaa 4 tulostetta, mukaan lukien 2, jotka ovat täsmälleen samaa määrää. Muut 2 ovat vaihtorahaa. Kahdesta saman määrän tulosteesta vain toinen todellisuudessa menee maksun vastaanottajalle.

Stonewall-siirrossa on vain 2 roolia:
- Lähettäjä, joka suorittaa varsinaisen maksun;
- Vastaanottaja, joka saattaa olla tietämätön siirron erityisluonteesta ja yksinkertaisesti odottaa maksua lähettäjältä.

Otetaan esimerkki ymmärtääksemme tämän siirtorakenteen. Alice on leipomossa ostamassa patonkiaan, joka maksaa `4,000 satsia`. Hän haluaa maksaa bitcoineilla säilyttäen tietyn yksityisyyden tason maksussaan. Siksi hän päättää luoda Stonewall-siirron maksua varten.
![transaction stonewall bakery](assets/en/1.webp)
Analysoimalla tätä siirtoa voimme nähdä, että leipuri todellakin sai `4,000 satsia` maksuna patongista. Alice käytti 2 UTXO:ta syötteinä: yhden `10,000 satsia` ja toisen `15,000 satsia`. Tuloksena hän sai 3 UTXO:ta: yhden `4,000 satsia`, yhden `6,000 satsia` ja yhden `11,000 satsia`. Alicen netto saldo tässä siirrossa on `-4,000 satsia`, mikä vastaa patongin hintaa.

Tässä esimerkissä jätin tarkoituksella louhintamaksut pois ymmärryksen helpottamiseksi. Todellisuudessa siirtomaksut katetaan kokonaan lähettäjän toimesta.

## Mikä ero on Stonewall ja Stonewall x2 välillä?
Stonewall-tapahtuma toimii samalla tavalla kuin StonewallX2-tapahtuma, ainoana erona on, että jälkimmäinen vaatii yhteistyötä toisin kuin klassinen Stonewall-tapahtuma, siksi "x2" nimitys. Todellakin, Stonewall-tapahtuman voi suorittaa ilman ulkopuolista yhteistyötä: lähettäjä voi toteuttaa sen ilman toisen henkilön apua. Kuitenkin Stonewall x2 -tapahtumassa, lisäosallistuja, jota kutsutaan "yhteistyökumppaniksi", liittyy prosessiin. Yhteistyökumppani tuo omat bitcoinit sisääntulona, lähettäjän bitcoinien rinnalle, ja saa koko summan ulostulona (miinus louhintamaksut).

Käydään uudelleen läpi esimerkkimme Alicesta leipomossa. Jos hän olisi halunnut tehdä Stonewall x2 -tapahtuman, Alicen olisi täytynyt tehdä yhteistyötä Bobin (kolmas osapuoli) kanssa tapahtuman luomisessa. He olisivat kumpikin tarjonneet sisääntulon UTXO:n. Bob olisi sitten saanut koko hänen sisääntulonsa summan ulostulona. Leipuri olisi saanut maksun hänen patongistaan samalla tavalla kuin Stonewall-tapahtumassa, kun taas Alice olisi saanut alkuperäisen saldonsa takaisin, miinus patongin hinta.
![transaction stonewall x2](assets/en/2.webp)

Ulkopuolisesta näkökulmasta tapahtuman kuvio olisi pysynyt täsmälleen samana.
![Stonewall vai Stonewall x2 ?](assets/en/3.webp)

Yhteenvetona, Stonewall ja Stonewall x2 -tapahtumat jakavat saman rakenteen. Erotus niiden välillä on niiden yhteistyöllisessä luonteessa. Stonewall-tapahtuma kehitetään yksilöllisesti, ilman yhteistyön tarvetta. Sen sijaan, Stonewall x2 -tapahtuma nojaa kahden henkilön väliseen yhteistyöhön sen toteuttamiseksi.

[**-> Lue lisää Stonewall x2 -tapahtumista**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)

## Mikä on Stonewall-tapahtuman tarkoitus?
Stonewall-rakenne lisää merkittävän määrän entropiaa tapahtumaan ja hämärtää ketjuanalyysiä. Ulkopuolisesta näkökulmasta tällainen tapahtuma voidaan tulkita pienenä coinjoinina kahden ihmisen välillä. Mutta todellisuudessa, aivan kuten Stonewall x2 -tapahtuma, se on maksu. Tämä menetelmä luo siis epävarmuuksia ketjuanalyysiin, ja saattaa jopa johtaa vääriin johtopäätöksiin.

Käydään uudelleen läpi Alicen esimerkki leipomossa. Tapahtuma lohkoketjussa näyttäisi seuraavalta:
![Stonewall vai Stonewall x2 ?](assets/en/4.webp)
Ulkopuolinen tarkkailija, joka nojaa yleisiin ketjuanalyysin heuristiikkoihin, saattaisi virheellisesti päätellä, että "*kaksi ihmistä on suorittanut pienen coinjoinin, kummallakin yksi UTXO sisääntulona ja kaksi UTXO:a kummallakin ulostulona*".
![Stonewall vai Stonewall x2 ?](assets/en/5.webp)
Tämä tulkinta on väärä, koska, kuten tiedät, UTXO lähetettiin leipurille, 2 UTXO:a sisääntulossa ovat Alicen, ja hän sai 3 vaihtorahaa ulostulona.

![transaction stonewall baker](assets/en/1.webp)
Vaikka ulkopuolinen tarkkailija onnistuisikin tunnistamaan Stonewall-siirron kaavan, hänellä ei ole kaikkea tietoa. Hän ei pysty määrittämään, kumpi kahdesta samansuuruisesta UTXO:sta vastaa maksua. Lisäksi hän ei kykene määrittämään, tulevatko kaksi syötteen UTXO:ta kahdelta eri henkilöltä vai kuuluvatko ne yhdelle henkilölle, joka on yhdistänyt ne. Tämä viimeinen kohta johtuu siitä, että yllä mainitut Stonewall x2 -siirrot noudattavat täsmälleen samaa kaavaa kuin Stonewall-siirrot. Ulkopuolelta ja ilman lisätietoja kontekstista on mahdotonta erottaa Stonewall-siirtoa Stonewall x2 -siirrosta. Kuitenkin edelliset eivät ole yhteistyössä tehtyjä siirtoja, kun taas jälkimmäiset ovat. Tämä lisää entisestään epävarmuutta tästä menosta.
![Stonewall vai Stonewall x2 ?](assets/en/3.webp)
## Kuinka tehdä Stonewall-siirto Samourai Walletissa?
Toisin kuin Stowaway- tai Stonewall x2 (cahoots) -siirrot, Stonewall-siirto ei vaadi Paynymien käyttöä. Se voidaan tehdä suoraan, ilman mitään valmisteluvaiheita. Tee tämä seuraamalla videomme ohjeita Samourai Walletissa:
![Stonewall-opas - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)

## Kuinka tehdä Stonewall-siirto Sparrow Walletissa?
Toisin kuin Stowaway- tai Stonewall x2 (cahoots) -siirrot, Stonewall-siirto ei vaadi Paynymien käyttöä. Se voidaan tehdä suoraan, ilman mitään valmisteluvaiheita. Tee tämä seuraamalla videomme ohjeita Sparrow Walletissa:
![Stonewall-opas - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)

**Ulkoiset Resurssit:**
- https://docs.samourai.io/en/spend-tools#stonewall.