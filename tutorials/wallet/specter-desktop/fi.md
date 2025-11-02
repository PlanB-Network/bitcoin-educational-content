---
name: Specter Desktop
description: Hallinnoi usean allekirjoituksen Bitcoin-salkkujasi täysin itsenäisesti omalla solmulla
---

![cover](assets/cover.webp)



Specter Desktop on avoimen lähdekoodin sovellus (MIT-lisenssi), jonka Cryptoadvance on kehittänyt vuodesta 2019 lähtien ja joka helpottaa Bitcoin-lompakoiden hallintaa laitteistosi lompakoiden (Ledger, Trezor, Coldcard, BitBox02, Passport jne.) ja oman Bitcoin-infrastruktuurisi (Bitcoin core-solmu tai Electrum Server) kanssa. Sovellus loistaa erityisesti usean allekirjoituksen konfiguraatioissa, jolloin voit turvata suuria summia jakamalla allekirjoitustehon usean riippumattoman laitteistolompakon kesken.



**Tässä opetusohjelmassa opit, miten:**




- Asenna ja määritä Specter Desktop tietokoneellesi (Windows, macOS tai Linux)
- Liitä Specter Electrum Server:een (tässä esimerkissä käytetään Umbrelia)
- Yksinkertaisen Wallet:n luominen Hardware Wallet:lla (Coldcard)
- Vastaanota ja lähetä bitcoineja täysin itsenäisesti
- 2-on-3-monisignatuurisen Wallet:n perustaminen useiden laitteistolompakoiden kanssa
- Asenna Specter Umbrel-palvelimelle (lisäbonus)



Kaikki maksutapahtumasi validoidaan paikallisesti oman infrastruktuurisi kautta ilman, että tietoja lähetetään ulkoisille palvelimille, mikä takaa luottamuksellisuutesi ja taloudellisen riippumattomuutesi. Tarkista tapahtumat aina Hardware Wallet-näytöltä ennen allekirjoittamista.



## Lataa ja asenna



Käy virallisella Specter Desktop -sivustolla lataamassa sovellus.



![Page d'accueil Specter](assets/fr/01.webp)



Valitse lataussivulla käyttöjärjestelmääsi vastaava versio: macOS, Windows tai Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Kun olet ladannut sovelluksen, asenna se käyttöjärjestelmäsi tavanomaisten ohjeiden mukaisesti. Jos kyseessä on macOS, vedä kuvake Applications-ohjelmaan. Windowsissa suorita asennusohjelma. Linuxissa noudata paketin ohjeita.



## Alkuperäinen konfigurointi



Ensimmäisellä käynnistyskerralla Specter Desktop pyytää sinua valitsemaan yhteystyypin. Voit muodostaa yhteyden Electrum Server:een tai omaan Bitcoin core-solmuun.



![Choix du type de connexion](assets/fr/03.webp)



Tässä esimerkissä käytämme yhteyttä Umbrelilla toimivaan Electrum Server:een.



Lisätietoja saat Umbrel-oppaasta:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Tämä vaihtoehto tarjoaa nopeamman synkronoinnin kuin Bitcoin core. Jos haluat, voit valita "Bitcoin core" ja määrittää yhteyden paikalliseen solmuun. Seuraavat vaiheet pysyvät samoina valinnasta riippumatta.



Valitse "Electrum Connection" ja valitse sitten "Enter my own" määrittääksesi oman Electrum Server:n.



![Configuration Electrum](assets/fr/04.webp)



Syötä Electrum Server:n Address. Umbrelin tapauksessa Address on `umbrel.local` ja portti `50001`. Napsauta "Connect" yhteyden muodostamiseksi.



Kun yhteys on muodostettu, näyttöön tulee tervetuliaisnäyttö, jossa on tarkistuslista, jonka avulla pääset alkuun. Nyt sinun on lisättävä laitteistosi lompakot.



![Écran d'accueil](assets/fr/05.webp)



## Hardware Wallet:n lisääminen



Valitse vasemmanpuoleisessa valikossa "Lisää laite" lisätäksesi Hardware Wallet:n.



Specter Desktop tukee lukuisia laitteistolompakoita: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault ja monet muut.



Jos haluat oppia lisää, katso Hardware Wallet-oppaamme.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Valitse Hardware Wallet. Tässä esimerkissä käytämme Coldcard MK4:ää.



Ohjeemme tästä Hardware Wallet:sta on alla:



https://planb.network/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Coldcardia varten sinun on vietävä julkiset avaimet Hardware Wallet:stä joko USB-yhteyden tai microSD-kortin kautta.



![Import des clés du Coldcard](assets/fr/07.webp)



Noudata näytettyjä ohjeita viedäksesi avaimet Coldcardista. Anna Hardware Wallet:lle nimi (tässä "MK4 Tuto"). Kun avaimet on tuotu, voit luoda Wallet:n yhdellä avaimella tai lisätä muita laitteistolompakoita, jotta Wallet:sta tulisi moniääninen.



![Dispositif ajouté](assets/fr/08.webp)



## Portfolion luominen



Kun olet lisännyt Hardware Wallet:n, napsauta "Create single key Wallet" (Luo yksittäinen avain Wallet) luodaksesi yhden allekirjoituksen Wallet:n.



Anna portfoliollesi nimi (esim. "Wallet for tuto") ja valitse Address-tyyppi. Valitse "SegWit" käyttääksesi natiiveja BECH32-osoitteita, jotka optimoivat transaktiokustannukset.



![Configuration du portefeuille](assets/fr/09.webp)



Kun salkku on luotu, Specter tarjoaa varmuuskopioidun PDF-tiedoston tallentamista, joka sisältää kaikki salkun palauttamiseen tarvittavat julkiset tiedot (kuvaajat, laajennetut julkiset avaimet). Tämä tiedosto ei sisällä yksityisiä avaimiasi.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Vastaanottaa bitcoineja



Jos haluat vastaanottaa bitcoineja, valitse Wallet vasemmanpuoleisesta valikosta ja napsauta sitten "Vastaanota" -välilehteä.



Specter luo automaattisesti uuden vastaanoton Address QR-koodilla.



![Génération d'une adresse de réception](assets/fr/11.webp)



Voit kopioida Address:n tai skannata QR-koodin. Tarkista Address aina Hardware Wallet:n näytöltä, ennen kuin annat sen kenellekään.



## Näytä historia ja osoitteet



Kun olet saanut bitcoineja, voit tarkastella tapahtumia "Tapahtumat"-välilehdellä.



![Historique des transactions](assets/fr/12.webp)



Osoitteet-välilehdellä voit tarkastella kaikkia salkun tuottamia osoitteita, niiden käyttötilaa ja niihin liittyviä summia.



![Liste des adresses](assets/fr/13.webp)



## Lähetä bitcoineja



Voit lähettää bitcoineja napsauttamalla "Lähetä"-välilehteä. Anna vastaanottajan Address, lähetettävä summa ja tarkista lisäasetukset, jos haluat valita UTXO:t manuaalisesti (Coin:n ohjaus).



![Création d'une transaction](assets/fr/14.webp)



Napsauta "Create Unsigned Transaction" (Luo allekirjoittamaton tapahtuma) rakentaaksesi tapahtuman. Tämän jälkeen Specter pyytää sinua allekirjoittamaan tapahtuman Hardware Wallet:lläsi.



![Signature de la transaction](assets/fr/15.webp)



Jos käytät Coldcard-korttia, voit valita, allekirjoitatko USB:n kautta vai käytätkö microSD-korttia (ilman liitäntää). Vahvista tapahtuma Hardware Wallet-näytöllä ja tarkista huolellisesti kohde Address ja summa.



Kun tapahtuma on allekirjoitettu, voit lähettää sen Bitcoin-verkossa.



![Options de diffusion](assets/fr/16.webp)



Lähetä tapahtuma napsauttamalla "Lähetä tapahtuma". Specter vahvistaa, että tapahtuma on lähetetty, ja voit seurata sen tilaa Tapahtumat-välilehdellä.



![Diffusion de la transaction](assets/fr/17.webp)



## Usean allekirjoituksen salkun luominen ja käyttö



Yksi Specter Desktopin suurimmista eduista on sen kyky yksinkertaistaa usean allekirjoituksen salkkujen hallintaa. Multisig Wallet vaatii useita allekirjoituksia tapahtuman hyväksymiseksi, jolloin yksittäinen vikapiste poistuu. Esimerkiksi 2-on-3-konfiguraatio vaatii kaksi allekirjoitusta kolmesta erillisestä laitteistolompakosta minkä tahansa menon vahvistamiseksi.



Jos haluat luoda Multisig Wallet:n, aloita lisäämällä kaikki allekirjoittajina olevat laitteistolompakot "Lisää laite" -painikkeella. Tässä esimerkissä käytämme kolmea eri laitteistolompakkoa: Coldcard MK4 (lisätty jo aiemmin), Passport ja Ledger. Tämä valmistajien monipuolistaminen vahvistaa turvallisuutta välttämällä riippuvuutta yhdestä Supply-ketjusta tai laiteohjelmistosta.



Tässä ovat linkit Ledger- ja Passport-oppaaseen:



https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Lisää Passport nimeämällä Hardware Wallet (esim. "Passport multi") ja tuomalla sen avaimet microSD-kortilla tai QR-koodilla. Jatka sitten napsauttamalla "Jatka".



![Ajout du Passport](assets/fr/23.webp)



Lisää sitten Ledger liittämällä se USB:n kautta ja avaamalla Bitcoin-sovellus Hardware Wallet:ssä. Anna sille nimi (esim. "Ledger multi") ja napsauta "Get via USB" ja sitten "Continue" tuodaksesi sen julkiset avaimet.



![Ajout du Ledger](assets/fr/24.webp)



Kun olet rekisteröinyt kolme laitteistolompakkoasi Specteriin, napsauta "Lisää Wallet" ja valitse "Multiple Signature" -vaihtoehto luodaksesi Wallet:n, jolla on useita allekirjoituksia.



![Choix du type de wallet](assets/fr/25.webp)



Valitse kolme laitteistolompakkoa, jotka haluat sisällyttää moniäänilompakkokorumiin: MK4 Tuto, Passport multi ja Ledger multi. Jatka seuraavaan vaiheeseen napsauttamalla "Jatka".



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Valitse usean allekirjoituksen kokoonpano. Valitse "SegWit" Address-tyypiksi, jotta voit hyötyä optimoiduista maksuista. Parametri "Tarvittavat allekirjoitukset tapahtumien valtuuttamiseksi (m of 3)" antaa sinulle mahdollisuuden määrittää kynnysarvon: 2-on-3 -konfiguraatiossa tarvitaan 2 allekirjoitusta. Kukin Hardware Wallet näyttää vastaavan Multisig-avaimen. Viimeistele luominen napsauttamalla "Create Wallet".



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



"Multi tuto" -monisignatuurisalkkusi on nyt luotu. Specter suosittelee välittömästi, että tallennat portfolion sisältävän varmuuskopio PDF-tiedoston Descriptor. Lataa tämä kriittinen tiedosto napsauttamalla "Save Backup PDF".



![Wallet multisig créé](assets/fr/28.webp)



Specterin avulla voit myös viedä Wallet-tiedot kuhunkin laitteistosi lompakkoon QR-koodin tai tiedoston avulla. Näin tietyt laitteistolompakot (kuten Coldcard tai Passport) voivat tallentaa Multisig-konfiguraation suoraan muistiinsa.



Passi: Avaa laitteesi lukitus ja siirry sitten kohtaan "Tilin hallinta" > "Yhdistä Wallet" > "Specter" > "Multisig" > "QR-koodi" ja skannaa sitten Specterin luoma QR-koodi. Passport pyytää sinua sitten skannaamaan Wallet:n vastaanottaneen Address:n Multisig:n konfiguraation vahvistamiseksi.



MK4:n osalta kytke se tietokoneeseen ja avaa lukitus. Napsauta sitten "Save MK4 Tuto file" ja tallenna tiedosto MK4:ään. Kun seuraavan kerran allekirjoitat Hardware Wallet:n, MK4 käyttää tätä tiedostoa Multisig:n konfiguroinnin viimeistelyyn.



![Export vers les hardware wallets](assets/fr/29.webp)



Tiedoksi, että voit käyttää varmuuskopioita milloin tahansa portfoliosi "Asetukset"-välilehdeltä ja sitten "Vie":



![Accès au backup PDF](assets/fr/30.webp)



Päivittäinen käyttö on samanlaista kuin yksinkertaisella Wallet:llä: generate vastaanottaa osoitteita normaalisti. Jos haluat lähettää bitcoineja, siirry "Lähetä"-välilehdelle, syötä vastaanottajan Address ja summa ja napsauta sitten "Luo allekirjoittamaton transaktio".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter rakentaa PSBT:n (Partially Signed Bitcoin Transaction) ja näyttää "Acquired 0 of 2 signatures". Sinun on nyt allekirjoitettava vähintään kahdella kolmesta laitteistolompakostasi. Napsauta ensimmäistä Hardware Wallet:a (esim. "MK4 Tuto") allekirjoittaaksesi Coldcardilla ja sitten toista (esim. "Passport multi") saadaksesi toisen vaaditun allekirjoituksen.



![Signature de la transaction](assets/fr/32.webp)



Kun olet saanut 2 vaadittua allekirjoitusta (Interface näyttää "Acquired 2 of 2 signatures" ja "Transaction is ready to send"), napsauta "Send Transaction" lähettääksesi transaktion Bitcoin-verkkoon.



![Transaction prête à être diffusée](assets/fr/33.webp)



Tämä usean allekirjoituksen lähestymistapa soveltuu erityisen hyvin yrityksille (useiden johtajien on hyväksyttävä menot), perheille (usean sukupolven perinnön suojaaminen) tai suuria summia hallinnoiville yksityishenkilöille (laitteistolompakoiden maantieteellinen jakautuminen paikallisten katastrofien varalta).



### Usean allekirjoituksen varmuuskopioiden ratkaiseva merkitys



**Huomaa**: usean allekirjoituksen salkun varmuuskopiointi eroaa olennaisesti yhden salkun varmuuskopioinnista. Pelkät palautuslausekkeet (seed-lauseet) eivät riitä Multisig-salkun palauttamiseen. Sinun on varmuuskopioitava myös **output descriptor** (output descriptor), joka sisältää monialkakirjoitussalkun konfigurointitiedot.



output descriptor sisältää olennaiset tiedot: kunkin allekirjoittajan laajennetut julkiset avaimet (xpubs), allekirjoituskynnys (esimerkissämme 2:3), käytetyn skriptityypin (SegWit natiivi, sisäkkäinen tai legacy) ja kunkin Hardware Wallet:n johdannaispolut. Ilman tätä Descriptor:ta et voi rakentaa Wallet:tta uudelleen tai päästä käsiksi bitcoineihisi, vaikka sinulla olisi kaksi kolmesta palautuslauseestasi. Descriptor:n avulla ohjelmistosi tietää, miten yhdistää julkiset avaimet generate:een Bitcoin-osoitteisiin, jotka vastaavat varojasi.



Specter Desktop luo automaattisesti varmuuskopioidun PDF-tiedoston, kun luot Multisig-salkun. Tämä PDF-tiedosto sisältää koko Descriptor:n, kunkin Hardware Wallet:n sormenjäljet ja kaikki palautusta varten tarvittavat julkiset tiedot. **Tämä tiedosto ei sisällä yksityisiä avaimiasi**, joten et voi käyttää bitcoinejasi, mutta sen avulla kuka tahansa, joka käyttää tiedostoa, voi nähdä koko tapahtumahistoriasi ja saldosi.



Jos haluat varmuuskopioida moni allekirjoituskokoonpanosi oikein, toimi seuraavasti: kun olet luonut portfoliosi, napsauta "Asetukset"-välilehteä, sitten "Vie" ja valitse "Tallenna varmuuskopio PDF". Luo tästä PDF-tiedostosta useita kopioita: tulosta vähintään kaksi kopiota paperille ja säilytä myös salattu digitaalinen kopio. Säilytä yksi kopio PDF-tiedostosta jokaisen palautuslausekkeen kanssa maantieteellisesti erillisissä paikoissa.



Polta talteenottolauseet tulenkestäville ja vedenpitäville metallilevyille niiden pitkäikäisyyden takaamiseksi. Älä koskaan aliarvioi näiden varmuuskopioiden merkitystä: jos menetät tietokoneesi `~/.specter`-kansion JA menetät yhden laitteistosi lompakoista ilman Descriptor-varmuuskopiota, kaikki varasi menetetään peruuttamattomasti, vaikka käytössäsi olisi 2-on-3-kokoonpano. Usean allekirjoituksen redundanssi suojaa Hardware Wallet:n menettämiseltä, mutta vain jos olet varmuuskopioinut Wallet:n Descriptor:n oikein.



## Specter Desktopin edut ja rajoitukset



**Hyötyjä**: Optimaalinen luottamuksellisuus täydellisellä paikallisella validoinnilla ilman kolmannen osapuolen palvelimia. Monen allekirjoituksen joustavuus edistyneissä kokoonpanoissa (yritys, perhe, yksityishenkilö). Laaja Hardware Wallet-tuki ja täysi yhteentoimivuus (USB- ja ilmakytkentä).



**Rajoitukset**: Bitcoin:n kehittyneiden käsitteiden (UTXO:t, kuvaajat, johdannaispolut) oppiminen on huomattavaa.



## Parhaat käytännöt



Tarkista aina osoitteet ja summat Hardware Wallet-näytöltä ennen vahvistamista suojautuaksesi haittaohjelmilta.



Pidä PDF-varmistuskopiot erillään siemenistäsi. Nämä julkiset kuvaajat voidaan säilyttää pankkiholvissa tai salatussa pilvipalvelussa, mikä helpottaa palautusta paljastamatta yksityisiä avaimia.



Testaa takaisinperintää token-määrillä ennen kuin käytät salkkujasi suurilla varoilla. Luo, testaa, poista ja palauta menettelyjen validoimiseksi.



Pidä Specter ja laiteohjelmisto ajan tasalla. Hajauta usean allekirjoituksen allekirjoittajat maantieteellisesti (koti/toimisto/läheinen paikka), jotta kestät paikalliset katastrofit. Käytä kuvaavia tarroja kirjanpidon ja veroilmoitusten helpottamiseksi.



## Bonus: Asennus Bitcoin-palvelimelle (Umbrel, RaspiBlitz, Start9)



Jos sinulla on jo Bitcoin-palvelin, kuten Umbrel, RaspiBlitz, MyNode tai Start9, voit asentaa Specter Desktopin suoraan niiden sovelluskaupasta. Tämä lähestymistapa tarjoaa useita merkittäviä etuja: sovellus konfiguroituu automaattisesti paikalliseen Bitcoin core-solmuun, se on käytettävissä 24/7 Interface-verkon kautta mistä tahansa laitteesta verkossa, ja voit jopa käyttää sitä turvallisesti etänä Torin kautta. Koko Bitcoin-infrastruktuurisi on keskitetty yhdelle erilliselle palvelimelle, mikä yksinkertaistaa hallintaa ja vahvistaa riippumattomuuttasi.



### Asennus Umbrel App Storesta



Mene Umbrel Interface:stä App Storeen ja etsi Specter Desktop. Käynnistä asennus napsauttamalla "Install".



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Kun asennus on valmis, avaa Specter Desktop Umbrelissa. Tervetuloruudussa sinua pyydetään valitsemaan yhteystyyppisi. Jos käytät Specteriä Umbrelissa, napsauta "Päivitä asetukset" määrittääksesi yhteyden.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Valitse "Remote Specter USB connection", jotta voit käyttää paikalliseen tietokoneeseen liitettyjä USB-laitteistokukkaroita, kun käytät Specteriä Umbrel-palvelimen etäpalvelimella.



![Configuration Remote Specter USB](assets/fr/20.webp)



Seuraa näytön ohjeita HWI-sillan määrittämiseksi. Sinun on päästävä laitteen silta-asetuksiin ja lisättävä toimialue `http://umbrel.local:25441` valkoiseen listaan. Tallenna asetukset napsauttamalla "Päivitä".



![HWI Bridge Settings](assets/fr/21.webp)



Jos haluat käyttää USB-laitelompakoitasi myös paikalliselta tietokoneeltasi, lataa Specter Desktop -sovellus koneellesi ja aseta sen asetukseksi "Kyllä, käytän Specteria etänä". Klikkaa "Tallenna" viimeistelläksesi asetukset.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Päätelmä



Specter Desktop demokratisoi Bitcoin:n edistyneet konfiguraatiot ja tekee moniäänisistä allekirjoituksista helppokäyttöisiä ilman, että suvereniteetti tai luottamuksellisuus kärsii. Merkittäviä rahamääriä hallinnoiville käyttäjille se muuttaa institutionaaliset käytännöt ratkaisuiksi, joita yksityishenkilöt voivat käyttää.



Vaikka sovellus vaatii alkuinvestointeja infrastruktuuriin ja oppimiseen, se tarjoaa täydellisen riippumattomuuden: validointi-infrastruktuurin hallinnan, avainten fyysisen Ownership:n ja tapahtumat ilman kolmannen osapuolen valvontaa. Olitpa sitten yksityishenkilö, joka turvaa säästöjään, perhe, joka luo usean sukupolven tallelokeron, tai yritys, joka hallinnoi kassavirtaa, Specter Desktop on referenssityökalu maksimaalisen turvallisuuden ja ehdottoman suvereenisuuden yhteensovittamiseen.



## Resurssit



### Viralliset asiakirjat




- [Specter Desktopin virallinen verkkosivusto](https://specter.solutions/desktop/)
- [GitHub-lähdekoodi](https://github.com/cryptoadvance/specter-desktop)
- [Täydellinen dokumentaatio](https://docs.specter.solutions/)



### Yhteisö ja tuki




- [Telegram Specter Community Group](https://t.me/spectersupport)
- [Reddit-keskustelufoorumi](https://reddit.com/r/specterdesktop/)
- [GitHubin vikailmoitukset](https://github.com/cryptoadvance/specter-desktop/issues)