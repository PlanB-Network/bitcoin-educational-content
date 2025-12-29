---
name: Bitcoin Keeper
description: Bitcoin mobiili wallet turvallisuuden varmistamiseksi ja multi-sig
---

![cover](assets/cover.webp)



Bitcoinien turvallinen hallinnointi on suuri haaste kaikille haltijoille, jotka ovat tietoisia taloudelliseen suvereniteettiin liittyvistä panoksista. Mobiilin wallet:n yksinkertaisuuden ja multi-sig-ratkaisun kestävyyden välinen tekninen ero voi tuntua monista käyttäjistä pelottavalta. Bitcoin Keeper on sijoitettu juuri tähän risteyskohtaan, ja se tarjoaa progressiivisen lähestymistavan turvallisuuteen, joka seuraa käyttäjiä heidän kehittyessään.



Bitcoin Keeper on avoimen lähdekoodin mobiilisovellus, joka on omistettu yksinomaan Bitcoin:lle ja jonka on kehittänyt BitHyve-tiimi. Sen tavoitteena on tehdä edistyneestä salkunhoidosta helppokäyttöistä, erityisesti moni allekirjoituskokoonpanoista, säilyttäen samalla intuitiivinen käyttöliittymä aloittelijoille. Sovelluksen tunnuslause "Secure today, Plan for tomorrow" (turvaa tänään, suunnittele huomista varten) kuvastaa sen filosofiaa pitkäaikaisesta tuesta.



Toisin kuin yleistyyppiset lompakot, jotka hallinnoivat useita kryptovaluuttoja, Bitcoin Keeper keskittyy tiukasti Bitcoin:een. Tämä vain bitcoineihin keskittyvä lähestymistapa vähentää mahdollisia hyökkäyksiä ja yksinkertaistaa käyttäjäkokemusta huomattavasti. Sovellus erottuu myös yleisimpien laitteistolompakoiden natiivin integraationsa ja kehittyneiden UTXO-hallintaominaisuuksiensa ansiosta.



## Mikä on Bitcoin Keeper?



### Filosofia ja tavoitteet



Bitcoin Keeper suunniteltiin vastaamaan niiden bitcoin-käyttäjien erityistarpeisiin, jotka haluavat säilyttää yksityisten avaintensa täyden hallinnan. Hanke noudattaa täysin Bitcoin:n perusperiaatteita: avoin ja tarkastettavissa oleva lähdekoodi, yksityisyyden kunnioittaminen ja käyttäjien itsemääräämisoikeus. Sovelluksen käyttäminen ei vaadi rekisteröitymistä tai henkilökohtaisia tietoja, ja sitä voidaan käyttää jopa offline-tilassa allekirjoitustoimintoja varten.



Keskeisenä tavoitteena on tarjota joustava, tulevaisuudenkestävä väline BTC:n säilyttämiseen useiden vuosien ja jopa useiden sukupolvien ajan perintötoimintojen ansiosta. Sovelluksen avulla käyttäjät voivat aloittaa yksinkertaisesti mobiililla wallet:llä ja kehittyä sitten vähitellen kohti turvallisempia usean allekirjoituksen ratkaisuja.



### Sovellusarkkitehtuuri



Bitcoin Keeper järjestää rahastojen hallinnoinnin kahden eri käsitteen ympärille. **Hot Wallet** on yksinkertainen yhden näppäimen wallet, joka tallennetaan puhelimeen ja joka on suunniteltu päivittäisiin menoihin ja vaatimattomiin summiin. Holvit** ovat monen allekirjoituksen (Multi-Key) kassakaappeja, jotka vaativat useita avaimia menon hyväksymiseksi ja jotka on suunniteltu pitkäaikaiseen turvalliseen säilytykseen.



### Tärkeimmät ominaisuudet



Bitcoin Keeper tukee lähes kaikkia markkinoilla olevia laitteistolompakoita: Coldcard, Trezor, Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport ja Coinkiten Tapsigner. Integrointi tapahtuu eri menetelmillä laitteesta riippuen: QR-koodin skannaus, NFC-yhteys tai tiedoston tuonti.



Sovellus tarjoaa myös kehittynyttä UTXO-hallintaa, jossa on tapahtumamerkinnät, kolikonhallinta, jolla syötteet voidaan valita manuaalisesti lähetettäessä, ja PSBT-muodon tuki osittain allekirjoitetuille tapahtumille.



## Asennus ja alustava konfigurointi



Bitcoin Keeper on saatavilla ilmaiseksi Androidille Google Play Storesta ja iOS:lle App Storesta. Julkaisija on BitHyve. Varmista ennen asentamista, että laitteesi on haittaohjelmaton, ajan tasalla eikä sitä ole rootattu tai jailbreakattu.



Ensimmäisellä käynnistyskerralla sovellus pyytää sinua luomaan PIN-turvakoodin. Tämä koodi suojaa pääsyn wallet:aan ja salaa arkaluonteiset tiedot paikallisesti. Valitse vahva koodi ja paina se mieleesi. Tämän jälkeen voit aktivoida biometrisen todennuksen (sormenjälki tai Face ID) lukituksen nopeampaa avaamista varten.



![Installation et configuration du PIN](assets/fr/01.webp)



Tämän jälkeen sovellus esittää useita esittelynäyttöjä, joissa selitetään sen kolme pilaria: wallet:n luominen bitcoinien lähettämistä ja vastaanottamista varten, avainten hallinta wallet-laitteiston yhteensopivuuden avulla ja perintösuunnittelu bitcoinien siirtämistä varten. Paina "Get Started" ja valitse sitten "Start New" luodaksesi uuden kokoonpanon.



![Écrans d'introduction](assets/fr/02.webp)



## Rajapinnan löytäminen



Bitcoin Keeper:n käyttöliittymä on järjestetty neljän päävälilehden ympärille, jotka löytyvät alareunan navigointipalkista:



![Les quatre onglets de l'application](assets/fr/03.webp)



**Lompakot**-välilehdellä näytetään lompakot ja niiden saldot. Täältä pääset lompakkoihisi lähettämään ja vastaanottamaan bitcoineja. Tunnisteiden "Hot Wallet" ja "Single-Key" tai "Multi-Key" avulla voit nopeasti tunnistaa kunkin wallet:n tyypin.



**Keys**-välilehdellä keskitetään allekirjoitusavaimien hallinta. Täältä löydät sovelluksen tuottaman mobiiliavaimen sekä kaikki laitteistolompakoista tuodut avaimet. Täällä voit myös lisätä uusia allekirjoituslaitteita.



**Vahtimestari**-välilehti tarjoaa tukipalveluja: voit lähettää kysymyksiä tukitiimille ja ottaa yhteyttä Bitcoin:n neuvonantajiin henkilökohtaista apua varten.



**More** (Lisää asetuksia) -välilehdellä pääsee käsiksi asetuksiin, kuten henkilökohtainen palvelinyhteys, avainten varmuuskopiointi, perintöasiakirjat, näyttöasetukset ja wallet:n hallinta.



## Yhteys omaan palvelimeen



Luottamuksellisuuden vahvistamiseksi Bitcoin Keeper:n avulla voit liittää sovelluksen omaan Electrum-palvelimeesi sen sijaan, että käyttäisit julkisia oletuspalvelimia.



![Configuration du serveur Electrum](assets/fr/04.webp)



Selaa Lisää-välilehdeltä alaspäin ja etsi palvelimen asetukset. Määritä uusi yhteys painamalla "Lisää palvelin". Voit valita "Julkinen palvelin" (valmiiksi määritetyt julkiset palvelimet) ja "Yksityinen Electrum" (oma palvelimesi).



Jos kyseessä on yksityinen palvelin, anna URL-osoite (esim. umbrel.local Umbrel-solmulle) ja porttinumero (yleensä 50001). Aktivoi SSL, jos palvelimesi tukee sitä. Voit myös skannata kokoonpanon QR-koodin. Kun olet syöttänyt parametrit, paina "Yhdistä palvelimeen".



Jos sinulla ei vielä ole omaa Bitcoin-solmua, tutustu Umbrel-solmun ohjeeseen, joka on yksinkertainen ja edullinen tapa kehrätä oma solmusi:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Vastaanottaa bitcoineja



Valitse Lompakot-välilehdeltä wallet, josta haluat vastaanottaa varoja, painamalla sitä. wallet:n näytöllä näkyy saldo ja kolme toimintopainiketta: Lähetä Bitcoin, Vastaanota Bitcoin ja Näytä kaikki kolikot.



![Réception de bitcoins](assets/fr/05.webp)



Paina "Vastaanota Bitcoin". Bitcoin Keeper luo uuden Bech32-muotoisen vastaanotto-osoitteen (alkaen bc1...) ja sen QR-koodin. Voit lisätä tähän osoitteeseen tarran, jolla voit tunnistaa varojen lähteen. Jaa osoite lähettäjän kanssa näyttämällä QR-koodi tai kopioimalla tekstiosoite.



Sovellus luo automaattisesti uuden osoitteen jokaista vastaanottoa varten, jolloin yksityisyytesi säilyy. Käytä "Get New Address" -toimintoa saadaksesi tarvittaessa tyhjän osoitteen.



## UTXO hallinta



Bitcoin Keeper tarjoaa täydellisen näkyvyyden saldon muodostaviin UTXO:een (käyttämättömät tapahtumatulosteet). Paina wallet-näytöltä "View All Coins" (Näytä kaikki kolikot) päästäksesi kulmanhallintaan.



![Gestion des UTXO](assets/fr/06.webp)



"Kolikoiden hallinta" -näytössä luetellaan jokainen UTXO erikseen määrineen ja merkintöineen. Tämän näkymän avulla voit jäljittää kolikoidesi alkuperän ja järjestää ne. Voit valita tietyt UTXO:t "Select to Send" -valinnalla lähetettäväksi kolikoiden hallinnan kanssa, jolloin vältät eri alkuperää olevien kolikoiden sekoittumisen.



## Lähetä bitcoineja



Valitse lähdesalkku ja paina "Send Bitcoin". Syötä kohdeosoite (liimataan tai skannataan QR-koodilla) ja lisää valinnaisesti etiketti vastaanottajan tunnistamiseksi.



![Envoi de bitcoins](assets/fr/07.webp)



Seuraavassa näytössä voit syöttää lähetettävän summan. Käyttöliittymä näyttää käytettävissä olevan saldosi ja fiat-valuutan muuntamisen. Valitse veloituksen prioriteetti: Matala (säästö, ~60 minuuttia), Keskisuuri tai Korkea (prioriteetti). Arvioidut maksut (sats/vbyte) näytetään reaaliajassa. Jatka painamalla "Lähetä".



![Confirmation et envoi](assets/fr/08.webp)



Yhteenvetonäytössä näkyvät kaikki tiedot: wallet-lähde, kohdeosoite, tapahtuman prioriteetti, verkkomaksut, lähetetty määrä ja loppusumma. Tarkista nämä tiedot huolellisesti, sillä Bitcoin-tapahtumat ovat peruuttamattomia. Lähetä tapahtuma painamalla "Vahvista ja lähetä".



Näyttöön tulee "Lähetä onnistui" -vahvistus, jossa on täydellinen yhteenveto. Tapahtuma näkyy "Viimeaikaiset tapahtumat" -historiassa merkinnällä varustettuna.



## Tallenna avaimet



Elvytysavaimen varmuuskopioiminen on kriittinen vaihe. Siirry Lisää-välilehdeltä kohtaan "Varmuuskopiointi ja palautus" ja napsauta "Palautusavain".



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



Näytössä näkyy varmuuskopioiden tila. Varmistaaksesi varmuuskopiointisi sovellus pyytää sinua vahvistamaan tietyn sanan lauseessasi (esim. 7. sana). Tällä varmistuksella varmistetaan, että olet kirjoittanut palautuslauseesi oikein.



"Recovery Key Settings" -kohdasta voit tarkastella koko lauseketta "View Recovery Key" -kohdasta ja nähdä avaimen allekirjoittajan sormenjäljen. Säilytä 12-sanainen lauseesi paperilla turvallisessa paikassa, kosteudelta ja tulelta suojattuna. Älä koskaan säilytä sitä liitetyssä laitteessa.



## Ulkoisen avaimen lisääminen (wallet-laitteisto)



Yksi Bitcoin Keeper:n tärkeimmistä eduista on laitteistolompakoiden integrointi. Paina Avaimet-välilehdellä "Lisää avain" lisätäksesi uuden allekirjoituslaitteen.



![Ajout d'une clé hardware](assets/fr/10.webp)



Valitse "Lisää avain laitteistosta" liittääksesi laitteiston wallet. Sovellus tukee monenlaisia laitteita: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner ja Specter Solutions.



### Tapsigner-konfiguraatio



Tapsigner on Coinkiten NFC-kortti, joka soveltuu erityisesti mobiilikäyttöön. Jos haluat lisätietoja, meillä on oma opetusohjelma :



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

Jos haluat lisätä Tapsigner:n, valitse se laitteistolompakoiden luettelosta.



![Configuration du Tapsigner](assets/fr/11.webp)



Syötä ensin kortin kääntöpuolelle painettu 6-32-numeroinen PIN-koodi (oletusarvo uusissa korteissa) tai PIN-koodisi, jos se on jo määritetty. Paina "Jatka" ja tuo Tapsigner-kortti lähelle puhelimen takaosaa, kun näyttöön tulee "Valmis skannaukseen". NFC-viestintä tuo automaattisesti julkisen avaimen. Voit sitten lisätä kuvauksen (esim. "Métro Card") tämän avaimen tunnistamiseksi.



## Luo multisig-salkku



Kun olet määrittänyt avaimet, voit luoda wallet:n, jossa on useita allekirjoituksia ja jossa yhdistetään useita laitteita. Napsauta Lompakot-välilehdeltä "Lisää Wallet".



![Création d'un nouveau wallet](assets/fr/12.webp)



Sinulla on kolme vaihtoehtoa: "Luo Wallet" uutta salkkua varten, "Tuo Wallet" olemassa olevan wallet:n palauttamiseksi tai "Yhteinen Wallet" jaettua holvia varten. Valitse "Luo Wallet" ja sitten "Bitcoin Wallet".



![Sélection du type de wallet](assets/fr/13.webp)



Seuraavassa näytössä on erilaisia asetuksia: "Single-key", "2 of 3 multi-key" tai "3 of 5 multi-key". Jos haluat mukautetun multi-sig:n, paina "Select custom setup" (Valitse mukautettu asetus). Valitse esimerkiksi "1 of 2": kahdesta mahdollisesta näppäimestä vaaditaan yksi allekirjoitus.



Valitse sitten avaimet, jotka muodostavat Holvin. Esimerkissämme yhdistämme "Mobile Key" -avaimen (puhelinohjelmiston avain) ja "TAPSIGNER" -avaimen (Metro Card). Tämä kokoonpano tarjoaa redundanssia: jos toinen avaimista ei ole käytettävissä, voit aina käyttää rahasi toisella avaimella.



![Finalisation du wallet multisig](assets/fr/14.webp)



Anna wallet:lle nimi (esim. "Test PlanB"), lisää valinnainen kuvaus ja tarkista valitut avaimet. Paina "Create Your Wallet". Näyttöön tulee vahvistusviesti "Wallet Created Successfully" (Wallet luotu onnistuneesti), joka muistuttaa wallet:n palautustiedoston tallentamisesta.



Uusi multisig wallet näkyy nyt Lompakot-välilehdellä tunnisteella "Multi-key" ja merkinnällä "1 of 2".



### Tallenna asetustiedosto



** Toisin kuin yksinkertaisessa wallet:ssä, jossa palautuslauseke riittää pääsyn palauttamiseen, wallet multisig vaatii myös konfigurointitiedoston, jossa kuvataan kassakaapin rakenne (mitkä avaimet osallistuvat, kuinka monta allekirjoitusta tarvitaan). Ilman tätä tiedostoa et voi rakentaa wallet:ää uudelleen, vaikka sinulla olisi kaikki palautuslausekkeet.



![Export du fichier de configuration](assets/fr/15.webp)



Voit viedä tämän tiedoston valitsemalla wallet multisigin lompakot-välilehdeltä ja painamalla sitten oikeassa yläkulmassa olevaa Asetukset-kuvaketta (hammasratas). Napsauta "Wallet Settings" -kohdassa "Wallet configuration file". Käytettävissä on useita vientivaihtoehtoja:





- Export PDF**: luo PDF-dokumentin, joka sisältää kaikki wallet:n tiedot
- Näytä QR**: näyttää skannattavan QR-koodin, jonka avulla kokoonpano voidaan tuoda toiseen laitteeseen
- Airdrop / Tiedoston vienti**: vie tiedoston puhelimen jakamisvaihtoehtojen kautta
- NFC**: jakaminen NFC:n kautta yhteensopivan laitteen kanssa



Pidä tämä asetustiedosto erillään palautuslausekkeista, mieluiten salatulla tai tulostetulla välineellä. Jos kadotat puhelimesi, tämän tiedoston ja kunkin osallistuvan avaimen palautuslausekkeiden avulla voit rakentaa wallet-multisignaalin uudelleen Bitcoin Keeper:llä tai muulla yhteensopivalla ohjelmistolla.



## Parhaat käytännöt



### Rahaston organisaatio



Strukturoi bitcoinisi niiden käyttötarkoituksen mukaan: kuuma wallet Single-Key juokseviin menoihin rajoitetuilla summilla ja yksi tai useampi Vaults Multi-Key pitkän aikavälin säästöihin. Järjestelmällinen UTXO-merkintä auttaa sinua seuraamaan, mistä varasi ovat peräisin, mikä on erityisen hyödyllistä luottamuksellisuuden hallinnassa ja eri alkuperää olevien kolikoiden sekoittamisen välttämisessä.



Pidä puhelimesi turvassa: aktivoi biometrinen lukitus, tee järjestelmäpäivityksiä säännöllisesti ja ole valppaana asennettujen sovellusten suhteen. Pidä Bitcoin Keeper:n tietoturvakorjaukset ajan tasalla.



### Varmuuskopioinnin turvallisuus



Säilytä vähintään kaksi kopiota jokaisesta palautuslausekkeesta paperilla maantieteellisesti erillisissä paikoissa. Suuria summia varten harkitse kaiverrettua, katastrofinkestävää metallia. Älä koskaan säilytä näitä lauseita laitteessa, joka on yhteydessä Internetiin, äläkä koskaan valokuvaa niitä.



Tallenna multi-sig-holvien osalta myös konfigurointitiedosto (Wallet Recovery File), joka sisältää osallistuvat julkiset avaimet ja holvin rakenteen. Tämän tiedoston ja avainten palautuslausekkeiden avulla wallet voidaan rakentaa uudelleen millä tahansa yhteensopivalla ohjelmistolla, kuten Sparrow:llä tai Specterillä.



## Edut ja rajoitukset



### Kohokohdat





- Vain Bitcoin-sovellus vähentää monimutkaisuutta ja riskejä
- Multisig-holvien integrointi natiivisti ja vaiheittainen opastus
- Laajennettu laitteistotuki wallet (Tapsigner, Coldcard, Ledger, Jade jne.)
- UTXO:n ja kolikonvalvonnan edistynyt hallinta
- Voidaan liittää henkilökohtaiseen Electrum-palvelimeen
- Avoin, tarkastettavissa oleva lähdekoodi



### Huomioon otettavat rajoitukset





- Interface pääasiassa englanniksi
- Jotkin premium-ominaisuudet (Cloud Backup, Assisted Server) vaativat päivityksen
- Multisig-konfiguraatio vaatii peruskoulutusta



## Päätelmä



Bitcoin Keeper erottuu edukseen skaalautuvana ratkaisuna bitcoinien hallintaan. Sen asteittainen lähestymistapa yksinkertaisesta kuumasta wallet:stä usean allekirjoituksen holveihin tarkoittaa, että turvallisuutta voidaan päivittää tarpeiden muuttuessa. Kyky integroida Tapsigner:n kaltaisia laitteistolompakoita helposti tasoittaa tietä vankoille kokoonpanoille ilman liiallista monimutkaisuutta.



Vain bitcoineja käyttävä suuntautuminen, avoin lähdekoodi ja yksityisyyden kunnioittaminen tekevät siitä valinnan, joka on linjassa Bitcoin-ekosysteemin ydinarvojen kanssa.



Tämä opetusohjelma kattaa Bitcoin Keeper:n keskeiset ominaisuudet sen ilmaisversiossa. Sovellus tarjoaa myös premium-ominaisuuksia (pilvivarmistus, avustettu palvelimen varmuuskopiointi, Canary-lompakot), joita käsitellään erillisessä opetusohjelmassa. Tulevassa oppaassa tutustumme myös perintösuunnitteluominaisuuteen, jonka avulla voit valmistella bitcoinien siirtämistä läheisillesi sovellukseen integroitujen Enhanced Vaults -holvien ja niihin liittyvien asiakirjojen ansiosta.



## Resurssit





- Virallinen verkkosivusto: [bitcoinkeeper.app](https://bitcoinkeeper.app)
- Ohjekeskus: [help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- Lähdekoodi: [github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)