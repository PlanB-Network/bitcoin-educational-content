---
name: Liana
description: Lompakon perustaminen ja käyttö Liana-palvelussa
---
![cover](assets/cover.webp)

Tässä oppaassa selitämme vaihe vaiheelta, miten Liana-sovellusta käytetään tietokoneella. Opit muun muassa, miten voit perustaa automaattisen perintäsuunnitelman, vastaanottaa ja lähettää bitcoineja tavanomaisissa tilanteissa ja hakea varoja olemassa olevasta salkusta tietyn ajan kuluttua.

Tammikuussa 2025 Lianan kanssa yhteensopivat laitteistolompakot olivat: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Specter DIY.

Jos haluat palauttaa varoja olemassa olevasta Liana-lompakosta, lue alla oleva esittely ja siirry suoraan kohtaan "Bitcoinien palauttaminen".

## Liana-ohjelmiston esittely

Liana on avoimen lähdekoodin ohjelmistopaketti, joka on suunniteltu edistyneiden salkkujen luomiseen ja hallintaan, erityisesti osana automaattista perintöjärjestelmää tai vankkaa varmuuskopiointimekanismia. Hanketta on kehittänyt vuodesta 2022 lähtien Wizardsardine, joka on Kévin Loaecin ja Antoine Poinsot'n yhdessä perustama yritys. Virallisella verkkosivustolla Liana esitellään "yksinkertaisena portfoliona henkilökohtaiseen kuratointiin, jossa on palautus- ja perintätoiminnot". Ohjelmisto toimii tietokoneilla -- Linux, MacOS, Windows -- ja sen (avoin) lähdekoodi on saatavilla [GitHubissa](https://github.com/wizardsardine/liana).

Liana hyödyntää Bitcoinin ohjelmoitavuutta kehittyneen lompakon luomiseksi. Se hyödyntää erityisesti aikalukkoja (*timelocks*), jotka mahdollistavat varojen käytön vasta tietyn ajan kuluttua, ja jotka ovat mukana Bitcoineja palautettaessa. Liana-lompakko koostuu siis useista rahankäyttötavoista:


- Pääasiallinen menopolku, joka on aina käytettävissä;
- Vähintään yksi palautuspolku, joka on käytettävissä tietyn ajan kuluttua.

Alla oleva kaavio havainnollistaa sellaisen salkun toimintaa, jossa on kaksi menopolkua:

![Schéma explicatif](assets/fr/01.webp)

Tämän toiminnon avulla voit määrittää erilaisia kokoonpanoja, kuten :


- Perintösuunnitelma, jonka avulla perilliset voivat periä varat takaisin käyttäjän kuollessa. Jos haluat lisätietoja tästä aiheesta, suosittelemme BTC102-kurssin [osa 4](https://planb.network/courses/btc102/233c88d3-2e8e-5eba-ac06-efe67a209038) lukemista.
- Vahvistettu varmuuskopio, jossa on palautumisaika, jolloin käyttäjä voi käyttää lompakkoaan ilman, että hänen tarvitsee säilyttää vastaavaa salaista lausetta ja ottaa riskin, että se varastetaan esimerkiksi murtovarkauden aikana.
- Turvaverkko ihmisille, jotka aloittavat Bitcoinin käytön: he hallinnoivat omaa lompakkoaan, ja heidän "holhoojansa" (esimerkiksi sukulainen) pidättää itselleen oikeuden periä heidän varansa takaisin tietyn ajan kuluttua.
- Monen osapuolen allekirjoitusjärjestelmä (*multisig*), jonka vaatimuksia vähennetään ajan myötä, jotta voidaan selviytyä yhden tai useamman osallistujan, esimerkiksi yrityksen yhteistyökumppanien, katoamisesta.

Lianan suuri vahvuus on se, että siinä otetaan käyttöön standardoitu tapa taata varojen takaisinperintä, jos juokseviin menoihin käytettävä pääavain menetetään. Tämä on valtava innovaatio varojen puhtaaseen säilyttämiseen, joka on täynnä riskejä, varsinkin jos et ole hyvin perillä aiheesta. Liana voisi näin ollen kannustaa jopa kaikkein riskialttiimpia käyttäjiä lopettamaan varojensa säilyttämisen säilytysyhteisön (kuten vaihtopalvelun) käyttämisen ja saamaan rahansa takaisin omistukseensa Bitcoinin salakirjoituksen eetoksen mukaisesti.

Lianalla on tietysti haittansa. Ensimmäinen on se, että sinun on päivitettävä lompakkosi säännöllisesti tekemällä transaktio Bitcoinin lohkoketjuun. Tämä voi olla vaivalloista (riippuen siitä, kuinka usein käytät ohjelmistoa) ja kallista (riippuen kulloinkin voimassa olevien maksujen tasosta), mutta se on hinta, jonka maksat lisäturvasta.

Toinen kielteinen seikka voi olla luottamuksellisuus. Kun otat toisen henkilön mukaan konfigurointiin, hän saa tietoonsa kaikki osoitteesi ja voi näin ollen seurata toimintaasi. Tämä ei kuitenkaan ole ongelma, jos valitset vahvistetun varmuuskopion tai perintäsuunnitelman, jossa perijälläsi ei ole välitöntä tietoa salkun tiedoista.

## Valmistelu

Tässä oppaassa laadimme seuraajasuunnitelman. Käytämme :


- Ledger Nano S Plus, jokapäiväisiä menoja varten;

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

- Blockstream Jade, jota käytetään varojen takaisinperintään;

https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3

- Kaksi tallennusvälinettä (USB-muistitikkuja) salkun kuvaajan tallentamista varten;
- Perintäkirje, jossa on ohjeet varojen takaisinperinnästä;
- Numeroitu sinetöity pussi, jolla varmistetaan, että talteenottolaitetta (Jade) ei ole käytetty.

## Asennus ja konfigurointi

Käy virallisella Wizardsardine-sivustolla ja lataa Liana osoitteessa https://wizardsardine.com/liana/. Voit myös ladata uusimman version [GitHub-arkistosta](https://github.com/wizardsardine/liana/releases), josta voit tarkistaa ohjelmiston aitouden. Tässä opetusohjelmassa käytetty versio on 0.9.

![Télécharger Liana](assets/fr/02.webp)

Jos haluat tietää, miten ohjelmiston aitous ja eheys voidaan tarkistaa manuaalisesti ennen asennusta, suosittelemme tutustumaan tähän ohjeeseen :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Asenna ohjelmisto koneellesi ja käynnistä se. Valitse "*Luo uusi Liana-lompakko*" -vaihtoehto määrittääksesi lompakkosi.

![Accueil Liana](assets/fr/03.webp)

Valitse salkkutyyppi. Jos haluat määrittää tehostetun varmuuskopion, jossa on palautumisaika, voit valita vaihtoehdon "*Rakenna oma*" ja valita oletusjärjestelmän. Tämä toimii pitkälti samalla tavalla, paitsi että sinun ei tarvitse säilyttää laitteiston lompakon palautuslausetta.

Tässä yhteydessä ei oteta huomioon *Laajentuva monisigma*-tapausta, joka muodostaa monimutkaisemman kokoonpanon.

Tässä ohjeessa käytämme yksinkertaista periytymistä.

![Choisir type de portefeuille](assets/fr/04.webp)

Seuraavassa on lyhyt selitys.

![Rapide explication](assets/fr/05.webp)

Kun olet lukenut selityksen, voit määrittää Liana-lompakkosi avaimet. Tämä on tärkeä vaihe, sillä se määrittää tilisi käyttöominaisuudet.

![Configurer clés](assets/fr/06.webp)

Ensiksi voit "Lisäasetukset"-valikossa päättää "kuvaustyypin" eli tavan, jolla sopimus kirjoitetaan ketjuun. Voit valita kahden tyypin välillä: P2WSH (SegWit) tai Taproot. Molemmissa tapauksissa menoehtojen semantiikka on sama. Vaikka P2WSH tekee sopimuksesta helpommin ymmärrettävän, Taproot on parempi siinä mielessä, että se piilottaa käyttämättömät ehdot ja säästää kustannuksia haun aikana.

Tämä valinta on valinnainen: jos olet epävarma, jätä oletusvaihtoehto (P2WSH versiossa 0.9, mutta se voi muuttua).

![Choisir le type de descripteur](assets/fr/07.webp)

Määritä seuraavaksi ensisijainen avain (*primääriavain*). Tätä avainta (tai pikemminkin tätä avainten joukkoa) käytetään varojen nykyiseen käyttöön, johon ei sovelleta mitään ajoitusehtoja. Klikkaamalla "*Set*" voit valita vastaavan *signointilaitteen*. Meidän tapauksessamme olemme valinneet Ledger Nano S Plus -laitelompakon.

Laajennetun julkisen avaimen jakamisen salliminen laitteesta. Anna tälle avaimelle mielekäs nimi (tässä tapauksessa "Nano S+"). Huomaa, että kaikki laitteeseen asennetut sovellukset toimivat edelleen normaalisti.

![Configurer clé principale](assets/fr/08.webp)

Seuraavaksi asetetaan takaisinmaksuviive eli aika, jonka jälkeen varat voidaan käyttää *perintöavaimella*. Tämä viive määritellään lohkoina, ja kunkin lohkon väliin jää keskimäärin 10 minuuttia. Se voi vaihdella 10 minuutista (1 lohko) noin 15 kuukauteen (65 535 lohkoa). Tämä yläraja on Bitcoin-protokollan rajoitus, koska lukitusaika on koodattu 16 bitillä.

Ellei erityisiä olosuhteita ole, valitse pisin toimitusaika: 15 kuukautta tai 65 535 lohkoa. Näin säästät kustannuksia. Suosittelemme kuitenkin, että suoritat päivitysmenettelyn (kuvattu kohdassa "Salkun päivittäminen") kerran vuodessa ja aina samaan aikaan vuodesta, jotta tämä käytäntö "ritualisoituu" ja vältät unohtamisen.

Tässä asetamme tunnin (6 lohkoa) palautumisajan testien suorittamista varten.

![Configurer temps de verrouillage](assets/fr/09.webp)

Määritä lopuksi kiinteistöavain. Tätä avainta (tai pikemminkin avainsarjaa) käytetään varojen palauttamiseen, jos katoat. Napsauta "*Set*", valitse allekirjoituslaite ja vahvista laajennetun julkisen avaimen jakaminen sillä.

Tähän opetusohjelmaan valitsimme Jaden. Anna avaimelle mieleenpainuva nimi (tässä "Jade"). Kuten ensimmäisen laitteen kohdalla, tavanomaiset tilit toimivat edelleen.

![Configurer clé de succession](assets/fr/10.webp)

Kun kaikki nämä toimet on suoritettu, tarkista, että kaikki on kunnossa, ja vahvista valintasi napsauttamalla "*Jatka*".

![Confirmer clés](assets/fr/11.webp)

Seuraavaksi tallennat salkun kuvaajan. Tämä on tieto, jota tarvitset löytääksesi tililläsi olevat varat. Toisin kuin muistisanassa, kuvaajan avulla et voi käyttää varoja, joten sen paljastaminen aiheuttaa vain luottamuksellisuusongelman (henkilö tietää kaikki tapahtumasi).

Tallenna kaksi kopiota kuvaajasta sähköisille välineille, kuten USB-tikuille. Muista tulostaa kaksi kopiota myös paperille, jotta saat ne käyttöösi, jos sähköinen tallennusväline vahingoittuu. Kukin varmuuskopio on liitettävä allekirjoituslaitteeseen.

![Sauvegarder descripteur](assets/fr/12.webp)

Kuvaajamme (jota analysoidaan opetusohjelman lopussa) on seuraava:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

Alkuperäisen salkun kokoonpanon viimeinen vaihe on allekirjoituslaitteina toimivien laitteistosalkkujen kuvaajien tarkistaminen.

![Enregistrer descripteur](assets/fr/13.webp)

Tee sama jokaiselle allekirjoittavalle laitteelle. Sinun on tarkistettava ja vahvistettava, että kuvaaja on lisätty kuhunkin laitteistosalkkuun.

![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)

Lompakkosi tiedot on nyt rekisteröity, ja jäljellä on enää sen määrittäminen, miten haluat muodostaa yhteyden Bitcoin-verkkoon. Voit valita oman solmusi (paikallisen tai etäyhteyden) tai käyttää WizardSardinen infrastruktuuria. Jälkimmäisessä tapauksessa sinun on yhdistettävä lompakkoosi sähköpostiosoite, jonka avulla voit hakea kuvaajan. WizardSardine pääsee käsiksi kaikkiin transaktioihisi. Ensimmäistä vaihtoehtoa suositellaan siksi.

![Sélectionner connexion réseau](assets/fr/15.webp)

Olemme päättäneet käyttää omaa solmua. Voit käyttää olemassa olevaa solmua tai asentaa *karsitun solmun* koneellesi. Jos sinulla ei ole pääsyä mihinkään muuhun solmuun, asenna oma solmusi koneellesi, mikä vie jonkin aikaa (useita päiviä).

![Choisir type de nœud](assets/fr/16.webp)

Tässä ohjeessa käytämme olemassa olevaa (julkista) Electrum-palvelinta. Mutta ole varovainen! Sillä oli pääsy kaikkeen toimintaamme Liana-lompakolla. Käytä siis omaa solmua, jos haluat suojata yksityisyytesi.

![Connexion serveur Electrum public](assets/fr/17.webp)

Kun solmun konfigurointi on valmis, avautuu päänäyttö, jossa näkyy juuri luotu Liana-lompakkosi.

Käytä tilaisuutta hyväksenne ja säilytä talteenottoyksikkö turvallisessa paikassa. Se olisi säilytettävä strategisesti tärkeässä paikassa, jotta perillisesi voivat löytää sen kuolemasi yhteydessä.

Lisäturvallisuuden lisäämiseksi voit laittaa palautukseen käytettävät komponentit suljettuun pussiin (*tuhoamissuojattu pussi*) ja kirjoittaa sen sarjanumeron jonnekin. Näin varmistat, ettei kukaan ole päässyt käsiksi siihen ja että laitteesi pysyy voimassa.

Esimerkissämme olemme koonneet seuraavat elementit:


- Blockstream Jade kuolinpesän allekirjoituslaitteena;
- USB-kaapeli laitteen liittämistä ja lataamista varten;
- Lauseen varmuuskopio paperilla, jos laitteessa on toimintahäiriö tai se vahingoittuu (huomaa, että tallennusväline voi olla myös metallinen ja siten suojattu säältä, kuten esimerkiksi Cryptosteel-kapselit);
- Salkun kuvaajan sisältävä USB-levyke ;
- Paperikopio kuvaajasta, jos USB-muistitikku ei toimi tai vahingoittuu (tätä kopiota ei ole kuvattu tässä);
- Perintäkirje, jossa kuvataan toimenpiteet, joihin on ryhdyttävä varojen takaisinperimiseksi.

![Éléments de récupération](assets/fr/18.webp)

Ja me panemme nämä tavarat sinetöityyn!

![Sachet scellé récupération](assets/fr/19.webp)

## Varojen vastaanottaminen

Lianan päänäytöllä näytetään saldosi ja salkkuusi liittyvät tapahtumat (aiemmat ja nykyiset). Meidän tapauksessamme saldo on nolla, mikä on normaalia.

![Écran principal](assets/fr/20.webp)

Jos haluat vastaanottaa varoja, siirry "*Vastaanottaa*"-välilehdelle ja napsauta "*Luo osoite*". Uuden osoitteen pitäisi ilmestyä näytöllesi. Se on pidempi kuin perinteisissä salkuissa: se on osoite, joka on linkitetty erilliseen sopimukseen (P2WSH tai Taproot).

![Générer nouvelle adresse](assets/fr/21.webp)

Sinun on tarkistettava tämä osoite laitteistosalkussasi napsauttamalla "*Varmista laitteistolaitteessa*".

![Vérifier adresse portefeuille matériel](assets/fr/22.webp)

Kun varat on lähetetty, maksutapahtuma näkyy päänäytöllä (ensin vahvistamattomana ja sitten vahvistettuna). Tässä testissä olemme lähettäneet 50 000 satoshia (hieman yli 50 dollaria siirtohetkellä). On sanomattakin selvää, että sinun tapauksessasi siirretyn summan on oltava tätä arvoa kertaluokkaa suurempi, koska siitä peritään siirtomaksut.

![Vérifier solde](assets/fr/23.webp)

Voit tarkistaa varojesi vanhentumistilan siirtymällä "*Coins*"-välilehdelle. Tämä välilehti näyttää lompakossasi olevat eri kolikot (UTXO). Tässä näemme, että tapahtumallamme luodun 50 000 satoshis-kolikon voimassaolo päättyy samana päivänä (tunnin kuluttua).

![Obtenir informations pièce](assets/fr/24.webp)

Jos haluat ymmärtää paremmin Bitcoinissa käytettyä UTXO-edustusmallia, voit tutustua Loïc Morelin kirjoittaman Bitcoinin luottamuksellisuutta käsittelevän kurssin ensimmäiseen osaan:

https://planb.network/courses/btc204
## Juoksevat menot

Nykyiset menot ovat normaali tilanne Lianan käytössä. Bitcoinien lähettäminen pääavaimella toimii kuten kaikissa klassisissa Bitcoin-lompakoissa, kuten Electrumissa tai Sparrowissa.

Jos haluat tehdä maksun, siirry "*Lähettää*"-välilehdelle ja syötä olennaiset tiedot: vastaanottajan BTC-osoite, lähetettävä summa ja haluamasi veloitusprosentti. Voit myös lisätä kuvauksen (paikallisesti tallennettuna) henkilökohtaista mukavuutta varten. Esimerkissämme lähetimme 10 000 satoshia tietylle Bobille, ja veloituskurssi oli 4 sat/ov eli 0,67 dollaria tapahtumahetkellä.

Liana tarjoaa myös "kolikonhallinnan": voit ilmoittaa, minkä kolikon (UTXO) haluat käyttää. Tässä olemme valinneet aiemmin luodun 50 000 satoshin kolikon.

![Envoyer fonds clé principale](assets/fr/25.webp)

Allekirjoita sitten tapahtuma pääavaimeen liitetyllä allekirjoituslaitteellasi napsauttamalla "*Sign*". Sinun on tarkistettava ja vahvistettava transaktio laitteistolompakossasi. Tässä olemme käyttäneet Nano S Plus -lompakkoa tapahtuman allekirjoittamiseen.

![Signer transaction clé principale](assets/fr/26.webp)

Lopuksi lähetä tapahtuma verkon kautta napsauttamalla "*Lähetys*". Huomaa, että varojen lähettäminen nollaa käytettyjen kolikoiden palautumisajan.

![Diffuser transaction clé principale](assets/fr/27.webp)

Tapahtuma näkyy päänäytöllä ja saldosi päivittyy.

![Solde après dépense](assets/fr/28.webp)

## Salkun päivitys

Kuten edellä on selitetty, Liana-lompakko vaatii sinua päivittämään varojasi säännöllisesti suorittamalla transaktion lohkoketjussa. Jos et tee näin, perijäsi (tai toinen laitteesi, jos kyseessä on tehostettu varmuuskopiointi) voi palauttaa varasi. Tilanne ei ole äärimmäisen vaarallinen, mutta se kumoaa tämän mekanismin perustamisen tarkoituksen: voit pitää bitcoinisi hallinnassa ilman luotettavaa kolmatta osapuolta ja hyötyä samalla turvaverkosta.

Varoitus tulee näkyviin ennen kuin varat (tai osa niistä) vanhentuvat ja ne voidaan käyttää palautusavaimella. Se ilmoittaa, että "palautuspolkusi" (*palautuspolku*) on pian käytettävissä. Koska palautumisaikamme on lyhyt (yksi tunti), tämä viesti näytetään suoraan meidän tapauksessamme.

![Avertissement chemin récupération](assets/fr/29.webp)

Kun määräaika lähestyy, näyttöön ilmestyy painike, joka kehottaa sinua päivittämään kyseiset varat.

![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)

Voit päivittää kolikkojasi siirtymällä "*Kolikot*"-välilehdelle ja napsauttamalla "*Uudista kolikko*" vastaavassa kolikkokentässä. Jos sinulla on useita kolikoita, ne on syytä päivittää yksi kerrallaan ja suhteellisen lyhyin väliajoin luottamuksellisuussyistä. Kustannusten vähentämiseksi voit yhdistää varojasi lähettämällä koko salkun uuteen vastaanottavaan osoitteeseen, mutta tämä vaikuttaa luottamuksellisuuteen.

![Actualiser pièce](assets/fr/31.webp)

Ilmoita maksutapahtuman haluttu maksuprosentti. Koska kyseessä on siirto itsellesi, voit asettaa melko alhaisen maksuprosentin, varsinkin jos teet sen useita päiviä ennen voimassaolon päättymistä.

![Transfert à soi-même](assets/fr/32.webp)

Tapahtuma (merkinnällä "*itsesiirto*") näkyy vain "*Tapahtumat*"-välilehdellä.

![Transactions après auto-transfert](assets/fr/33.webp)

Kun se on vahvistettu, kolikkosi on turvassa! Voit levätä rauhassa seuraavaan voimassaolon päättymispäivään asti.

## Bitcoinin elpyminen

Kun perit varoja takaisin Liana-salkusta, saatat joutua jompaankumpaan seuraavista tilanteista. Sinulla voi olla pääsy tietokoneeseen, johon ohjelmisto on asennettu, jolloin sinun tarvitsee vain avata se (mikä tapahtuu tehostetun varmuuskopiointimallin tapauksessa). Sinulla ei kuitenkaan välttämättä ole pääsyä tähän tietokoneeseen, joten aloitamme tässä tapauksessa tyhjästä. Huomaa, että palautusmenettely on sama molemmissa tapauksissa.

Voit aloittaa lataamalla Lianan [Wizardsardinen viralliselta verkkosivustolta](https://wizardsardine.com/liana/) tai [GitHub-arkistosta](https://github.com/wizardsardine/liana/releases), josta voit tarkistaa ohjelmiston aitouden. Asenna ohjelmisto ja suorita se. Tapauksessamme käytetty versio on 0.9, joten visuaalinen ilme on saattanut muuttua. Valitse tervetuliaisnäytössä vaihtoehto "Add an existing Liana wallet".

![Ajouter portefeuille existant](assets/fr/34.webp)

Määritä, miten haluat muodostaa yhteyden verkkoon. Voit käyttää omaa solmua (paikallista tai etäyhteyttä) tai WizardSardinen infrastruktuuria. Jälkimmäisessä tapauksessa tarvitset salkun luojan käyttämän sähköpostiosoitteen, jotta varat voidaan paikantaa automaattisesti. Jos sinulla ei ole tätä tietoa, valitse ensimmäinen vaihtoehto.

![Sélectionner connexion réseau](assets/fr/35.webp)

Jos käytät omaa solmua, tuo portfolion kuvaaja. Tämä on tilin tekninen kuvaus, jonka avulla voit hakea tilillä olevat varat. Meidän tapauksessamme se on seuraavat tiedot:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

![Importer descripteur](assets/fr/36.webp)

Liana pyytää sinua sitten syöttämään muistisäännön. Jos sinulla on toimiva allekirjoituslaite (laitteistolompakko), jätä tämä kohta väliin. Jos laite puuttuu tai on vahingoittunut, mutta sinulla on vastaavat 12 tai 24 sanaa, voit silti käyttää tätä vaihtoehtoa. Varmuuden vuoksi (jos palautettava määrä on suuri) suosittelemme silti, että hankit uuden laitteistolompakon ja käytät muistisanaa sen avainten palauttamiseen.

Meidän tapauksessamme käytämme Blockstream Jade -laitelompakkoa palautuslaitteena ja valitsemme tämän vaiheen ohittamisen ("*Skip*").

![Passer phrase mnémotechnique](assets/fr/37.webp)

Tarkista ja tallenna kuvaaja allekirjoituslaitteeseen valitsemalla se näytöltä. Jos laitteiston lompakko ei näy, tarkista, että se on liitetty ja lukitus on avattu. Tarkista ja vahvista, että nämä tiedot on lisätty laitteeseesi.

![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)

Konfiguroi solmusi. Voit käyttää olemassa olevaa solmua tai asentaa *karsitun solmun* koneellesi. Meidän tapauksessamme käytimme olemassa olevaa solmua.

![Choisir type de nœud](assets/fr/39.webp)

Tässä ohjeessa käytimme julkista Electrum-palvelinta. Sillä oli kuitenkin pääsy kaikkeen toimintaamme Liana-lompakolla. Jos haluat suojata yksityisyytesi, sinun on parempi käyttää omaa solmua.

![Connexion serveur Electrum public](assets/fr/17.webp)

Kun olet määrittänyt solmun, pääset lompakon päänäyttöön, jossa voit tarkastella saldoa ja tiliin liittyviä aiempia tapahtumia. Näet myös, voiko varoja hakea. Tässä näkyy, että kolikon voi hakea.

![Accueil Liana récupération](assets/fr/40.webp)

Jos haluat palauttaa salkussa olevat varat, siirry vasemmalla alhaalla olevaan kohtaan Asetukset ("*Asetukset*") ja napsauta kohtaa "*Palautus*".

![Récupération dans paramètres](assets/fr/41.webp)

Käytä lompakossa oleva kolikko rastittamalla asianmukainen ruutu. Ilmoita BTC-osoite, johon haluat lähettää varat, sekä transaktiomaksu. Napsauta sitten "*Seuraava*".

![Récupération des pièces](assets/fr/42.webp)

Allekirjoita transaktio napsauttamalla "*Sign*" ja vahvistamalla transaktio laitteistosi lompakossa.

![Signer transaction clé de récupération](assets/fr/43.webp)

Lähetä se sitten verkon kautta napsauttamalla "*Lähetys*".

![Diffuser transaction clé de récupération](assets/fr/44.webp)

Tapahtuman pitäisi näkyä päänäytöllä. Kun se on vahvistettu, palautus on valmis!

![Écran principal après récupération](assets/fr/45.webp)

## Videot

Jos haluat tietää enemmän Lanasta, voit tutustua videosisältöön, jonka avulla saat selkeämmän käsityksen sen toiminnasta. Tässä on videoesittely Lianasta, jossa ovat mukana Kévin Loaec ja Antoine Poinsot :

![Vidéo de présentation avec Kévin Loaec et Antoine Poinsot](https://youtu.be/siuLmQo1lM8)

Ja tässä on Antoine Poinsot'n opetusohjelma Lianan käytöstä:

![Vidéo-tutoriel avec Antoine Poinsot](https://youtu.be/JrG4WMVPZDQ)

Jälkimmäisessä esitetyt manipulaatiot ovat samanlaisia kuin tässä opetusohjelmassa esitetyt.

## Bonus: kuvaaja-analyysi

Kuvaaja on ihmisen luettavissa oleva merkkijono, joka kuvaa tyhjentävästi joukon osoitteita. Siinä yhdistyvät useat olennaiset tiedot, joita tarvitaan kehittyneen salkun osien (UTXO) hakemiseen. Kuvaajan kirjoitustapa perustuu Andrew Poelstran, Pieter Wuillen ja Sanket Kanjalkarin vuonna 2019 kehittämään skriptikieleen [Miniscript syntax] (https://bitbox.swiss/blog/understanding-bitcoin-miniscript-part-2/).

Jotta ymmärtäisimme paremmin, miksi tämä merkkijono on tärkeä, analysoidaan esimerkkimme kuvaajaa, joka on :

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

Tästä kuvaajasta voidaan poimia seuraavat tiedot:


- `wsh` (lyhenne sanoista *todistuskäsikirjoituksen hash*): Tämä on luodun transaktiotulosteen tyyppi. Jos olisimme päättäneet käyttää Taprootia, tunniste olisi ollut `tr`.
- `or_d`: Tämä on looginen operaattori, joka osoittaa, että *jommankumman seuraavista kahdesta* ehdosta on täytyttävä, jotta kustannus voidaan hyväksyä (`_d` tarkoittaa tiettyä syntaksia).
- "pk" (lyhenne sanoista *julkinen avain*): Tämä operaattori vertaa annettua allekirjoitusta seuraavaan julkiseen avaimeen ja antaa vastauksen boolen muodossa (TRUE tai FALSE).
- `[3689a8e7/48'/0'/0'/2']`: Tämä elementti sisältää päälaitteiston lompakon (tässä tapauksessa Nano S Plus) pääavaimen *sormenjäljen* ja linkitetyn laajennetun yksityisen avaimen (josta kaikki muut yksityiset avaimet johdetaan) johdannaispolun.
- `xpub6FKY ... WQa`: Tämä on laajennettu julkinen avain, joka liittyy päälaitteistoon (tässä Nano S Plus)
- `/<0;1>/*`: `0` vastaanottoon, `1` sisäisiin operaatioihin (*muutos*), ja "jokerimerkki" (`*`), joka mahdollistaa useiden osoitteiden peräkkäisen johtamisen konfiguroitavalla tavalla, joka on samanlainen kuin klassisten salkku-ohjelmistojen "aukkorajojen" hallinta.
- and_v`: Tämä on looginen operaattori, joka osoittaa, että *kahdessa* seuraavassa esitetyn ehdon on täytyttävä, jotta kustannus voidaan hyväksyä (`_v` tarkoittaa tiettyä syntaksia).
- `v:pkh` (lyhenne sanoista *verify: public key hash*): Tämä operaattori verifioi annetun allekirjoituksen ja julkisen avaimen seuraavan julkisen avaimen hashiin (*hash*). Tämä on periaatteessa sama tarkistus kuin P2PKH- ja P2WPKH-skripteissä.
- `[42e629dd/48'/0'/0'/2']`: Tämä on sama elementti kuin edellä (joka koostuu jäljityksestä ja johdannaispolusta), paitsi että laitteiston palautussalkun pääavaimen (tässä tapauksessa Jade) jäljitys ilmoitetaan.
- `xpub6DpQ ... WQd`: Tämä on laajennettu julkinen avain, joka on liitetty laitteiston palautuslompakkoon (tässä Jade).
- `older(6)` : Tällä operaattorilla tarkistetaan, että luodun transaktiotulosteen iän on oltava ehdottomasti suurempi kuin 6 lohkoa, jotta se voidaan käyttää.

Viimeinen tietoerä (`8alrve5h`) on kuvaajan tarkistussumma, ja se vastaa salkun tunnusta.

Tämän salkun luomat skriptit ovat seuraavanlaisia:

```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```

Koska Bitcoin-lompakkosi turvallisuus riippuu myös siitä, ymmärrätkö, miten se toimii, suosittelen, että opiskelet determinististen ja hierarkkisten lompakoiden mekanismeja syvällisesti osallistumalla tälle ilmaiselle koulutuskurssille Plan ₿ Network :

https://planb.network/courses/cyp201