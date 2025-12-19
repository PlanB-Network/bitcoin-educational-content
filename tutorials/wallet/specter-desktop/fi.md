---
name: Specter Desktop
description: Hallinnoi usean allekirjoituksen Bitcoin-salkkujasi täysin itsenäisesti omalla solmulla
---

![cover](assets/cover.webp)



Specter Desktop on CryptoAdvancen vuodesta 2019 lähtien kehittämä avoimen lähdekoodin sovellus (MIT-lisenssi), joka helpottaa Bitcoin-lompakoiden hallintaa laitteistosi lompakoiden (Ledger, Trezor, Coldcard, BitBox02, Passport jne.) ja oman Bitcoin-infrastruktuurisi (Bitcoin Core-solmu tai Electrum-palvelin) kanssa. Sovellus loistaa erityisesti usean allekirjoituksen konfiguraatioissa, joiden avulla voit turvata suuria summia jakamalla allekirjoitustehon usean riippumattoman laitteistolompakon kesken.



**Tässä opetusohjelmassa opit, miten:**




- Asenna ja määritä Specter Desktop tietokoneellesi (Windows, macOS tai Linux)
- Yhdistä Specter Electrum-palvelimeen (tässä esimerkissä käytetään Umbrelia)
- Yksinkertaisen wallet:n luominen wallet-laitteistolla (Coldcard)
- Vastaanota ja lähetä bitcoineja täysin itsenäisesti
- 2-on-3-monisignatuurisen wallet:n perustaminen useiden laitteistolompakoiden kanssa
- Asenna Specter Umbrel-palvelimelle (lisäbonus)



Kaikki maksutapahtumasi validoidaan paikallisesti oman infrastruktuurisi kautta ilman, että tietoja lähetetään ulkoisille palvelimille, mikä takaa luottamuksellisuutesi ja taloudellisen riippumattomuutesi. Tarkista tapahtumat aina wallet-laitteiston näytöltä ennen allekirjoittamista.



## Lataa ja asenna



Käy virallisella Specter Desktop -sivustolla lataamassa sovellus.



![Page d'accueil Specter](assets/fr/01.webp)



Valitse lataussivulla käyttöjärjestelmääsi vastaava versio: macOS, Windows tai Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Kun olet ladannut sovelluksen, asenna se käyttöjärjestelmäsi tavanomaisten ohjeiden mukaisesti. Jos kyseessä on macOS, vedä kuvake Applications-ohjelmaan. Windowsissa suorita asennusohjelma. Linuxissa noudata paketin ohjeita.



## Alkuperäinen konfigurointi



Ensimmäisellä käynnistyskerralla Specter Desktop pyytää sinua valitsemaan yhteystyypin. Voit muodostaa yhteyden Electrum-palvelimeen tai omaan Bitcoin Core -solmuun.



![Choix du type de connexion](assets/fr/03.webp)



Tässä esimerkissä käytämme yhteyttä Umbrelissa toimivaan Electrum-palvelimeen.



Lisätietoja saat Umbrel-oppaasta:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Tämä vaihtoehto tarjoaa nopeamman synkronoinnin kuin Bitcoin Core. Voit halutessasi valita "Bitcoin Core" ja määrittää yhteyden paikalliseen solmuun. Seuraavat vaiheet pysyvät samoina valinnasta riippumatta.



Valitse "Electrum Connection" ja valitse sitten "Enter my own" määrittääksesi oman Electrum-palvelimesi.



![Configuration Electrum](assets/fr/04.webp)



Kirjoita Electrum-palvelimen osoite. Meidän tapauksessamme Umbrelin osoite on `umbrel.local` ja portti `50001`. Napsauta "Connect" yhteyden muodostamiseksi.



Kun yhteys on muodostettu, näyttöön tulee tervetuliaisnäyttö, jossa on tarkistuslista, jonka avulla pääset alkuun. Nyt sinun on lisättävä laitteistosi lompakot.



![Écran d'accueil](assets/fr/05.webp)



## wallet-laitteiston lisääminen



Napsauta vasemmanpuoleisessa valikossa "Lisää laite" lisätäksesi wallet-laitteiston.



Specter Desktop tukee lukuisia laitteistolompakoita: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault ja monet muut.



Jos haluat lisätietoja, katso laitteiston wallet-oppaat.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Valitse wallet-laitteisto. Tässä esimerkissä käytämme Coldcard MK4:ää.



Alta löydät tämän wallet-laitteiston ohjeen:



https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Coldcardia varten sinun on vietävä julkiset avaimet wallet-laitteistosta joko USB-yhteyden tai microSD-kortin kautta.



![Import des clés du Coldcard](assets/fr/07.webp)



Noudata näytettyjä ohjeita viedäksesi avaimet Coldcardista. Anna wallet-laitteistolle nimi (tässä "MK4 Tuto"). Kun avaimet on tuotu, voit luoda wallet:n yhdellä avaimella tai lisätä muita laitteistolompakoita, jos haluat käyttää usean allekirjoituksen wallet:tä.



![Dispositif ajouté](assets/fr/08.webp)



## Portfolion luominen



Kun olet lisännyt wallet-laitteiston, napsauta "Luo yhden avaimen wallet" luodaksesi yhden allekirjoituksen wallet:n.



Anna portfoliollesi nimi (esim. "Wallet for tuto") ja valitse osoitetyyppi. Valitse "Segwit" käyttääksesi natiiveja bech32-osoitteita, jotka optimoivat transaktiokustannukset.



![Configuration du portefeuille](assets/fr/09.webp)



Kun salkku on luotu, Specter tarjoaa varmuuskopioidun PDF-tiedoston tallentamista, joka sisältää kaikki salkun palauttamiseen tarvittavat julkiset tiedot (kuvaajat, laajennetut julkiset avaimet). Tämä tiedosto ei sisällä yksityisiä avaimiasi.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Vastaanottaa bitcoineja



Jos haluat vastaanottaa bitcoineja, valitse wallet vasemmanpuoleisesta valikosta ja napsauta sitten "Vastaanota" -välilehteä.



Specter luo automaattisesti uuden vastaanotto-osoitteen QR-koodilla.



![Génération d'une adresse de réception](assets/fr/11.webp)



Voit kopioida osoitteen tai skannata QR-koodin. Tarkista osoite aina wallet-laitteiston näytöltä, ennen kuin annat sen kenellekään.



## Näytä historia ja osoitteet



Kun olet saanut bitcoineja, voit tarkastella tapahtumia "Tapahtumat"-välilehdellä.



![Historique des transactions](assets/fr/12.webp)



Osoitteet-välilehdellä voit tarkastella kaikkia salkun tuottamia osoitteita, niiden käyttötilaa ja niihin liittyviä summia.



![Liste des adresses](assets/fr/13.webp)



## Lähetä bitcoineja



Voit lähettää bitcoineja napsauttamalla "Lähetä"-välilehteä. Kirjoita vastaanottajan osoite, lähetettävä summa ja tarkista lisäasetukset, jos haluat valita UTXO:t (kolikon ohjaus) manuaalisesti.



![Création d'une transaction](assets/fr/14.webp)



Napsauta "Create Unsigned Transaction" (Luo allekirjoittamaton tapahtuma) rakentaaksesi tapahtuman. Tämän jälkeen Specter pyytää sinua allekirjoittamaan tapahtuman wallet-laitteistollasi.



![Signature de la transaction](assets/fr/15.webp)



Jos käytät Coldcard-korttia, voit valita, allekirjoitatko USB:n kautta vai microSD-kortin avulla (ilman liitäntää). Vahvista tapahtuma wallet-laitteiston näytöllä ja tarkista kohdeosoite ja summa huolellisesti.



Kun tapahtuma on allekirjoitettu, voit lähettää sen Bitcoin-verkossa.



![Options de diffusion](assets/fr/16.webp)



Lähetä tapahtuma napsauttamalla "Lähetä tapahtuma". Specter vahvistaa, että tapahtuma on lähetetty, ja voit seurata sen tilaa Tapahtumat-välilehdellä.



![Diffusion de la transaction](assets/fr/17.webp)



## Usean allekirjoituksen salkun luominen ja käyttö



Yksi Specter Desktopin suurimmista eduista on sen kyky yksinkertaistaa usean allekirjoituksen salkkujen hallintaa. Multisig wallet edellyttää useita allekirjoituksia tapahtuman valtuuttamiseksi, jolloin yksittäinen vikapiste poistuu. Esimerkiksi 2-on-3-konfiguraatio vaatii kaksi allekirjoitusta kolmesta erillisestä laitteistolompakosta minkä tahansa menon vahvistamiseksi.



Jos haluat luoda multisig wallet:n, aloita lisäämällä kaikki allekirjoittavat laitteistolompakot "Lisää laite" -painikkeella. Tässä esimerkissä käytämme kolmea eri laitteistolompakkoa: Coldcard MK4 (lisätty jo aiemmin), Passport ja Ledger. Tämä valmistajien monipuolistaminen vahvistaa turvallisuutta välttämällä riippuvuutta yhdestä toimitusketjusta tai laiteohjelmistosta.



Tässä ovat linkit Ledger- ja Passport-oppaaseen:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Lisää Passport nimeämällä wallet-laitteisto (esim. "Passport multi") ja tuomalla sen avaimet microSD-kortilla tai QR-koodilla. Jatka sitten napsauttamalla "Jatka".



![Ajout du Passport](assets/fr/23.webp)



Lisää sitten Ledger liittämällä se USB:n kautta ja avaamalla Bitcoin-sovellus wallet-laitteistoon. Anna sille nimi (esim. "ledger multi") ja napsauta "Get via USB" ja sitten "Continue" tuodaksesi sen julkiset avaimet.



![Ajout du Ledger](assets/fr/24.webp)



Kun olet rekisteröinyt kolme laitteistolompakkoa Specteriin, napsauta "Lisää wallet" ja valitse "Multiple Signature" -vaihtoehto luodaksesi wallet:n, jolla on useita allekirjoituksia.



![Choix du type de wallet](assets/fr/25.webp)



Valitse kolme laitteistolompakkoa, jotka haluat sisällyttää moniäänilompakkokorumiin: MK4 Tuto, Passport multi ja Ledger multi. Jatka seuraavaan vaiheeseen napsauttamalla "Jatka".



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Valitse usean allekirjoituksen kokoonpano. Valitse osoitetyypiksi "Segwit", jos haluat hyötyä optimoiduista maksuista. "Tarvittavat allekirjoitukset tapahtumien hyväksymiseksi (m of 3)" -parametrin avulla voit määritellä kynnysarvon: 2-on-3 -konfiguraatiossa vaaditaan 2 allekirjoitusta. Kukin wallet-laitteisto näyttää vastaavan multisig-avaimen. Viimeistele luominen napsauttamalla "Create wallet".



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



"Multi tuto" -monisignatuurisalkkusi on nyt luotu. Specter suosittelee heti, että tallennat varmuuskopioidun PDF-tiedoston, joka sisältää portfolion kuvauksen. Lataa tämä kriittinen tiedosto napsauttamalla "Save Backup PDF".



![Wallet multisig créé](assets/fr/28.webp)



Specterin avulla voit myös viedä wallet-tiedot kuhunkin laitteistolompakkoon QR-koodin tai tiedoston avulla. Näin tietyt laitteistolompakot (kuten Coldcard tai Passport) voivat tallentaa multisig-konfiguraation suoraan muistiinsa.



Jos haluat Passportin, avaa laitteen lukitus ja siirry sitten kohtaan "Tilin hallinta" > "Yhdistä Wallet" > "Specter" > "Multisig" > "QR-koodi" ja skannaa sitten Specterin luoma QR-koodi. Passport pyytää sinua tämän jälkeen skannaamaan wallet:n vastaanottoosoitteen multisig-konfiguraation vahvistamiseksi.



MK4:n osalta kytke se tietokoneeseen ja avaa lukitus. Napsauta sitten "Save MK4 Tuto file" ja tallenna tiedosto MK4:ään. Kun seuraavan kerran allekirjoitat wallet-laitteistosi, MK4 käyttää tätä tiedostoa viimeistelläkseen multisig-konfiguroinnin.



![Export vers les hardware wallets](assets/fr/29.webp)



Tiedoksi, että voit käyttää varmuuskopioita milloin tahansa portfoliosi "Asetukset"-välilehdeltä ja sitten "Vie":



![Accès au backup PDF](assets/fr/30.webp)



Päivittäinen käyttö on samanlaista kuin yksinkertaisella wallet:llä: generate vastaanottaa osoitteita normaalisti. Jos haluat lähettää bitcoineja, siirry "Lähetä"-välilehdelle, syötä vastaanottajan osoite ja summa ja napsauta sitten "Luo allekirjoittamaton transaktio".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter rakentaa PSBT:n (Partially Signed Bitcoin Transaction) ja näyttää "Acquired 0 of 2 signatures". Sinun on nyt allekirjoitettava vähintään kahdella kolmesta laitteistolompakostasi. Napsauta ensimmäistä wallet-laitteistoa (esim. "MK4 Tuto") allekirjoittaaksesi Coldcardilla ja sitten toista (esim. "Passport multi") saadaksesi toisen vaaditun allekirjoituksen.



![Signature de la transaction](assets/fr/32.webp)



Kun olet saanut 2 vaadittua allekirjoitusta (käyttöliittymässä näkyy "Acquired 2 of 2 signatures" ja "Transaction is ready to send"), klikkaa "Send Transaction" lähettääksesi transaktion Bitcoin-verkkoon.



![Transaction prête à être diffusée](assets/fr/33.webp)



Tämä usean allekirjoituksen lähestymistapa soveltuu erityisen hyvin yrityksille (useiden johtajien on hyväksyttävä menot), perheille (usean sukupolven perinnön suojaaminen) tai suuria summia hallinnoiville yksityishenkilöille (laitteistolompakoiden maantieteellinen jakautuminen paikallisten katastrofien varalta).



### Usean allekirjoituksen varmuuskopioiden ratkaiseva merkitys



**Huomaa**: monisignaalisen salkun varmuuskopiointi eroaa olennaisesti yksittäisen salkun varmuuskopioinnista. Pelkät palautuslausekkeet (seed-lausekkeet) eivät riitä monisignaalisalkun palauttamiseen. Sinun on varmuuskopioitava myös **output descriptor** (output descriptor), joka sisältää multisig-salkun asetustiedot.



output descriptor sisältää olennaiset tiedot: kunkin allekirjoittajan laajennetut julkiset avaimet (xpubs), allekirjoituksen kynnysarvo (esimerkissämme 2:3), käytetyn skriptin tyyppi (natiivi, sisäkkäinen tai perinteinen Segwit) ja kunkin wallet-laitteiston ohitusreitit. Ilman tätä kuvaajaa et voi rakentaa wallet:tä uudelleen tai päästä käsiksi bitcoineihisi, vaikka sinulla olisi kaksi kolmesta palautuslauseestasi. Kuvaajan avulla ohjelmistosi tietää, miten yhdistää julkiset avaimet generate:een ja Bitcoin:n osoitteisiin, jotka vastaavat varojasi.



Specter Desktop luo automaattisesti varmuuskopioidun PDF-tiedoston, kun luot multisig-salkkusi. Tämä PDF-tiedosto sisältää täydellisen kuvauksen, kunkin wallet-laitteiston sormenjäljet ja kaikki palauttamiseen tarvittavat julkiset tiedot. **Tämä tiedosto ei sisällä yksityisiä avaimiasi**, joten et voi käyttää bitcoinejasi, mutta sen avulla kuka tahansa, joka käyttää sitä, voi nähdä koko tapahtumahistoriasi ja saldosi.



Jos haluat varmuuskopioida moni allekirjoituskokoonpanosi oikein, toimi seuraavasti: kun olet luonut portfoliosi, napsauta "Asetukset"-välilehteä, sitten "Vie" ja valitse "Tallenna varmuuskopio PDF". Luo tästä PDF-tiedostosta useita kopioita: tulosta vähintään kaksi kopiota paperille ja säilytä myös salattu digitaalinen kopio. Säilytä yksi kopio PDF-tiedostosta jokaisen palautuslausekkeen kanssa maantieteellisesti erillisissä paikoissa.



Kaiverruta palautuslauseesi paloturvallisiin ja vedenkestäviin metallilevyihin niiden pitkäikäisyyden takaamiseksi. Älä koskaan aliarvioi näiden varmuuskopioiden tärkeyttä: jos menetät `~/.specter`-kansion tietokoneeltasi JA menetät yhden laitteistosi lompakoista ilman varmuuskopiota kuvaajista, kaikki varasi menetetään peruuttamattomasti, vaikka käytössä olisi 2:3-kokoonpano. Usean allekirjoituksen redundanssi suojaa wallet-laitteiston katoamiselta, mutta vain jos olet varmuuskopioinut wallet:n kuvaajan oikein.



## Specter Desktopin edut ja rajoitukset



**Hyötyjä**: Optimaalinen luottamuksellisuus täydellisellä paikallisella validoinnilla ilman kolmannen osapuolen palvelimia. Monen allekirjoituksen joustavuus edistyneissä kokoonpanoissa (yritys, perhe, yksityishenkilö). Laaja laitteistotuki wallet:lle ja täysi yhteentoimivuus (USB- ja ilmakytkentä).



**Rajoitukset**: Bitcoin:n kehittyneiden käsitteiden (UTXO:t, kuvaajat, johdannaispolut) oppiminen on huomattavaa.



## Parhaat käytännöt



Tarkista aina osoitteet ja summat laitteistosi wallet-näytöltä ennen vahvistamista suojautuaksesi haittaohjelmilta.



Pidä PDF-varmistuskopiot erillään siemenistäsi. Nämä julkiset kuvaajat voidaan säilyttää pankkiholvissa tai salatussa pilvipalvelussa, mikä helpottaa palautusta paljastamatta yksityisiä avaimia.



Testaa talteenotto token-määrillä ennen kuin käytät salkkujasi suurilla varoilla. Luo, testaa, poista ja palauta validoidaksesi menettelyt.



Pidä Specter ja laiteohjelmisto ajan tasalla. Hajauta usean allekirjoituksen allekirjoittajat maantieteellisesti (koti/toimisto/läheinen paikka), jotta kestät paikalliset katastrofit. Käytä kuvaavia tarroja kirjanpidon ja veroilmoitusten helpottamiseksi.



## Bonus: Asennus Bitcoin-palvelimelle (Umbrel, RaspiBlitz, Start9)



Jos sinulla on jo Bitcoin-palvelin, kuten Umbrel, RaspiBlitz, MyNode tai Start9, voit asentaa Specter Desktopin suoraan niiden sovelluskaupasta. Tämä lähestymistapa tarjoaa useita merkittäviä etuja: sovellus konfiguroituu automaattisesti paikalliseen Bitcoin Core -solmuun, se on käytettävissä 24/7 web-käyttöliittymän kautta mistä tahansa verkon laitteesta, ja voit jopa käyttää sitä turvallisesti etänä Torin kautta. Koko Bitcoin-infrastruktuurisi on keskitetty yhdelle erilliselle palvelimelle, mikä yksinkertaistaa hallintaa ja vahvistaa riippumattomuuttasi.



### Asennus Umbrel App Storesta



Mene Umbrelin käyttöliittymästä App Storeen ja etsi Specter Desktop. Käynnistä asennus napsauttamalla "Asenna".



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Kun asennus on valmis, avaa Specter Desktop Umbrelissa. Tervetuloruudussa sinua pyydetään valitsemaan yhteystyyppisi. Jos käytät Specteriä Umbrelissa, napsauta "Päivitä asetukset" määrittääksesi yhteyden.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Valitse "Remote Specter USB connection", jotta voit käyttää paikalliseen tietokoneeseen liitettyjä USB-laitteistokukkaroita, kun käytät Specteriä Umbrel-palvelimen etäpalvelimella.



![Configuration Remote Specter USB](assets/fr/20.webp)



Seuraa näytön ohjeita HWI-sillan määrittämiseksi. Sinun on päästävä laitteen silta-asetuksiin ja lisättävä toimialue `http://umbrel.local:25441` valkoiselle listalle. Tallenna asetukset napsauttamalla "Päivitä".



![HWI Bridge Settings](assets/fr/21.webp)



Jos haluat käyttää USB-laitelompakoitasi myös paikalliselta tietokoneeltasi, lataa Specter Desktop -sovellus koneellesi ja aseta sen asetukseksi "Kyllä, käytän Specteria etänä". Klikkaa "Tallenna" viimeistelläksesi asetukset.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Päätelmä



Specter Desktop demokratisoi Bitcoin:n edistyneet konfiguraatiot ja tekee moniäänisistä allekirjoituksista helppokäyttöisiä uhraamatta riippumattomuutta tai luottamuksellisuutta. Merkittäviä rahamääriä hallinnoiville käyttäjille se muuttaa institutionaaliset käytännöt ratkaisuiksi, joita yksityishenkilöt voivat ottaa käyttöön.



Vaikka sovellus vaatii alkuinvestointeja infrastruktuuriin ja oppimiseen, se tarjoaa täydellisen riippumattomuuden: validointi-infrastruktuurin hallinnan, avainten fyysisen omistuksen ja liiketoimet ilman kolmannen osapuolen valvontaa. Olitpa sitten yksityishenkilö, joka turvaa säästöjään, perhe, joka luo usean sukupolven tallelokeron, tai yritys, joka hallinnoi kassavirtaa, Specter Desktop on referenssityökalu maksimaalisen turvallisuuden ja ehdottoman suvereenisuuden yhteensovittamiseen.



## Resurssit



### Viralliset asiakirjat




- [Specter Desktopin virallinen verkkosivusto](https://specter.solutions/desktop/)
- [GitHub-lähdekoodi](https://github.com/cryptoadvance/specter-desktop)
- [Täydellinen dokumentaatio](https://docs.specter.solutions/)



### Yhteisö ja tuki




- [Telegram Specter Community Group](https://t.me/spectersupport)
- [Reddit-keskustelufoorumi](https://reddit.com/r/specterdesktop/)
- [GitHubin vikailmoitukset](https://github.com/cryptoadvance/specter-desktop/issues)