---
name: Trezor Safe 5
description: Hardware Wallet Safe 5:n määrittäminen ja käyttö
---
![cover](assets/cover.webp)



*Kuvan luotto: [Trezor.io](https://trezor.io/)*



Trezor Safe 5 on SatoshiLabsin suunnittelema viimeisimmän sukupolven Hardware Wallet, joka julkaistaan vuonna 2024. Se on sijoitettu Safe 3:n huippuluokan versioksi, jossa on keskitytty ergonomiaan ja kestävyyteen. Se hyötyy samoista turvallisuuteen liittyvistä edistysaskelista kuin edeltäjänsä Safe 3 verrattuna Model Oneen ja Model T:hen.



Safe 5:n hinta on 169 euroa, ja se sijoittuu huippuluokan Hardware Wallet-kategoriaan ja kilpailee Coldcardin, Ledger Nano X:n ja Flexin, Jade Plusin, Passportin ja Bitboxin kaltaisten mallien kanssa.



Safe 5:n erikoisuutena on sen 1,54-tuumainen värikosketusnäyttö, jota suojaa *Gorilla Glass 3*, joka kestää iskuja ja naarmuja. Se on myös varustettu *Trezor Touch* -haptisella moottorilla, joka lähettää pieniä värinöitä, kun sitä kosketetaan. Safe 3:n tapaan se sisältää Secure Elementin ja toimii USB-C-liitännän kautta, ja siihen on lisätty Micro SD -portti.



Safe 3:n ja Safe 5:n tärkein ero on turvallisuusnäkökohtien lisäksi laitteen laadussa. Se parantaa merkittävästi käyttökokemusta, sillä sen toiminta on sujuvampaa ja näyttö miellyttävämpi. Turvallisuuden kannalta se on vastaava.



![Image](assets/fr/01.webp)



Safe 5:ssä on kaikki olennaiset ominaisuudet, joita voit odottaa hyvältä Hardware Wallet:ltä, mukaan lukien erinomainen integrointi passphrase BIP39:n kanssa. Se ei kuitenkaan vielä tue Miniscriptiä.



Tämä malli sopii erityisesti aloittelijoille ja keskitason käyttäjille. Toisaalta se ei ehkä täytä kaikkia niiden edistyneiden käyttäjien odotuksia, jotka etsivät Coldcardin kaltaisten laitteiden erityisominaisuuksia. Jos et kuitenkaan tarvitse näitä kehittyneitä vaihtoehtoja, Trezor Safe 5 voi olla erinomainen valinta.



## Trezor Safe 5 -turvamalli



Trezor Safe 5 on Safe 3:n tavoin varustettu EAL6+-sertifioidulla **Secure Elementillä**, joka on merkittävä edistysaskel aiempiin malleihin, kuten Model Oneen ja Model T:hen verrattuna. Kyseessä on OPTIGA Trust M V3 -siru, joka ei tallenna seed:ta suoraan, vaan toimii kryptografisena komponenttina, joka turvaa pääsyn siihen. Secure Element säilyttää salaisuuden, johon pääsee käsiksi vasta, kun käyttäjä on syöttänyt PIN-koodin oikein. Tätä salaisuutta käytetään sitten seed:n salauksen purkamiseen, joka tallennetaan salattuna laitteen keskusmuistiin.



Tämä hybridi-turvajärjestelmä tarjoaa paremman fyysisen suojan, erityisesti louhintatekoja tai invasiivista analyysiä vastaan, jotka olivat Model One -mallissa ongelmallisia erityisesti PIN-koodien hallinnassa. Nämä haavoittuvuudet voidaan nyt kiertää Secure Elementin käytön ansiosta. Tässä mallissa säilytetään myös avoimen lähdekoodin ohjelmistoarkkitehtuuri: yksityisten avainten luomista ja käyttöä hallinnoiva koodi on täysin saatavilla ja todennettavissa. OPTIGA-siru hallinnoi vain PIN-koodia, joka on Bitcoin Wallet-avaimenhallinnan ulkopuolinen elementti. Se on rajoitettu vapauttamaan salaisuus, jota voidaan käyttää seed:n salauksen purkamiseen. Lisäksi OPTIGA Trust M V3 -sirulla on suhteellisen vapaa lisenssi, joka antaa SatoshiLabsille luvan julkaista vapaasti mahdolliset haavoittuvuudet (NDA-Free).



Tämä turvamalli on mielestäni yksi parhaista kompromisseista, joita markkinoilla on tällä hetkellä saatavilla. Siinä yhdistyvät Secure Elementin edut ja avoimen lähdekoodin ohjelmistojen hallinta. Aikaisemmin käyttäjien oli valittava sirun avulla parannetun fyysisen turvallisuuden ja avoimen lähdekoodin avulla saavutetun avoimuuden välillä; Trezor Safen avulla on mahdollista hyötyä molemmista.



Tässä oppaassa opit, miten Trezor Safe 5 -laite konfiguroidaan ja miten sitä käytetään turvallisesti.



## Trezor Safe 5:n purkaminen



Kun vastaanotat Safe 5 -laitteen, varmista, että laatikko ja Seal ovat ehjiä, jotta voit varmistaa, että pakettia ei ole avattu. Laitteen aitouden ja eheyden ohjelmistotarkastus suoritetaan myös, kun laite otetaan käyttöön myöhemmin.



Laatikon sisältö sisältää:




- Trezor Safe 5;
- Pussi, joka sisältää kartonkia Mnemonic-lauseen, tarroja ja ohjeet;
- USB-C-USB-C-kaapeli.



Kun Trezor Safe 5 -laite avataan, sen pitäisi olla suojamuovilla suojattu, ja USB-C-portti pitäisi olla suojattu hologrammilla Seal:lla. Varmista, että se on siellä.



![Image](assets/fr/02.webp)



Navigointi laitteessa on melko intuitiivista:




- Siirry eteenpäin koskettamalla näytön alaosaa;
- Liu'uta alaspäin palataksesi takaisin ;
- Vahvista toiminto painamalla ja pitämällä näyttöä painettuna.



## Edellytykset



Tässä opetusohjelmassa näytän, miten Trezor Safe 5:tä käytetään [Sparrow Wallet -salkunhallintaohjelmiston](https://sparrowwallet.com/download/) kanssa. Jos et ole vielä asentanut tätä ohjelmistoa, tee se nyt. Jos tarvitset apua, meillä on myös yksityiskohtainen ohje Sparrow Wallet:n konfiguroinnista :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Tarvitset myös Trezor Suite -ohjelmiston Safe 5:n konfigurointiin, sen aitouden tarkistamiseen ja laiteohjelmiston asentamiseen. Käytämme tätä ohjelmistoa vain tähän, ja sen jälkeen sitä tarvitaan vain laiteohjelmistopäivityksiin. Wallet:n päivittäiseen hallintaan käytämme yksinomaan Sparrow Wallet:tä, koska se on optimoitu Bitcoin:lle ja helppokäyttöinen myös aloittelijoille (Sparrow tukee vain Bitcoin:tä, ei altcoineja).



[Lataa Trezor Suite virallisilta sivuilta](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Suosittelen vahvasti, että tarkistat molempien ohjelmien aitouden (GnuPG:llä) ja eheyden (Hash:lla) ennen niiden asentamista koneellesi. Jos et tiedä, miten tämä tehdään, voit seurata tätä toista ohjetta :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Trezor Safe 5:n käynnistäminen



Liitä Safe 5 tietokoneeseen, johon Trezor Suite ja Sparrow Wallet on jo asennettu.



![Image](assets/fr/04.webp)



Avaa Trezor Suite ja napsauta sitten "*Set up my Trezor*".



![Image](assets/fr/05.webp)



Valitse "*Bitcoin-only firmware*" ja napsauta sitten "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



Trezor Suite asentaa sitten laiteohjelmiston Safe 5 -laitteeseesi. Odota asennuksen aikana.



![Image](assets/fr/07.webp)



Napsauta "*Jatka*".



![Image](assets/fr/08.webp)



Jatka sitten aitoustestiä varmistaaksesi, ettei Hardware Wallet ole väärennös tai vaarannettu.



![Image](assets/fr/09.webp)



Vahvista Safe 5 -laitteessa painamalla näyttöä.



![Image](assets/fr/10.webp)



Jos Trezor on aito, Trezor Suitessa näkyy vahvistusviesti.



![Image](assets/fr/11.webp)



Tämän jälkeen voit ohittaa ikkunat, joissa on peruskäyttöohjeet.



![Image](assets/fr/12.webp)



## Bitcoin-salkun luominen



Klikkaa Trezor Suiten "*Luo uusi Wallet*" -painiketta.



![Image](assets/fr/13.webp)



Luodaksesi tavallisen BIP39 Wallet -lauseen, valitse aluksi "*Legacy Wallet -varmistustyypit*" pudotusvalikosta ja valitse sitten 12- tai 24-sanainen Mnemonic-lause (tällä hetkellä suositellaan 12 sanaa). Näin voit luoda klassisen yhden tunnuksen salkun. Suosittelen valitsemaan BIP39-yhteensopivat parametrit, jotta haku olisi helpompaa ja jotta vältyttäisiin rajoituksilta tiettyyn ympäristöön. Viimeistele viimeistely klikkaamalla "*Luo Wallet*".



Jos haluat lisätietoja muista Trezorissa käytettävissä olevista varmuuskopiointivaihtoehdoista, mukaan lukien *Multi-share Backup*, suosittelen tutustumaan myös tähän oppaaseen :



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)



Hyväksy Hardware Wallet:n käyttöehdot.



![Image](assets/fr/15.webp)



Luo uusi salkku painamalla näyttöä pitkään.



![Image](assets/fr/16.webp)



Klikkaa Trezor Suitessa "*Jatka varmuuskopiointia*".



![Image](assets/fr/17.webp)



Ohjelmisto antaa ohjeet Mnemonic-lauseen hallintaan.



Tämä Mnemonic antaa sinulle täyden, rajoittamattoman pääsyn kaikkiin bitcoineihisi. Kuka tahansa, jolla on hallussaan tämä lauseke, voi varastaa varojasi, vaikka hänellä ei olisi fyysistä pääsyä Trezor Safe 5:een.



12-sanainen lause palauttaa pääsyn bitcoineihisi, jos Hardware Wallet häviää, varastetaan tai rikkoutuu. Siksi on erittäin tärkeää tallentaa se huolellisesti ja säilyttää se turvallisessa paikassa.



Voit kirjoittaa sen laatikossa olevaan pahviin, tai jos haluat lisätä turvallisuutta, suosittelen kaiverrusta ruostumattomasta teräksestä valmistettuun alustaan, joka suojaa sitä tulipalolta, tulvalta tai romahdukselta.



Vahvista ohjeet ja napsauta sitten "*Luo Wallet varmuuskopio*" -painiketta.



![Image](assets/fr/18.webp)



Safe 5 luo Mnemonic-lauseesi satunnaislukugeneraattorin avulla. Varmista, ettei sinua tarkkailla tämän toiminnon aikana. Kirjoita näytöllä näkyvät sanat haluamallesi fyysiselle välineelle. Turvallisuusstrategiastasi riippuen voit harkita useiden täydellisten fyysisten kopioiden tekemistä lauseesta (mutta ennen kaikkea älä jaa sitä). On tärkeää pitää sanat numeroituina ja juoksevassa järjestyksessä.



***Ei näitä sanoja saa tietenkään koskaan jakaa internetissä, kuten minä teen tässä ohjeessa. Tätä esimerkkiä Wallet käytetään vain Testnet:ssä, ja se poistetaan ohjeen lopussa



Jos haluat lisätietoja oikeasta tavasta tallentaa ja hallita Mnemonic-lauseesi, suosittelen lämpimästi seuraamaan tätä toista opetusohjelmaa, varsinkin jos olet aloittelija:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)



Voit siirtyä seuraaviin sanoihin napsauttamalla näytön alareunaa. Voit siirtyä taaksepäin liu'uttamalla alaspäin. Kun olet kirjoittanut kaikki sanat ylös, pidä sormi näytöllä siirtyäksesi seuraavaan vaiheeseen.



![Image](assets/fr/20.webp)



Valitse Mnemonic-lauseen sanat niiden järjestyksen mukaan varmistaaksesi, että olet kirjoittanut ne oikein.



![Image](assets/fr/21.webp)



Kun tämä vahvistusmenettely on valmis, jatka näyttöä napsauttamalla.



![Image](assets/fr/22.webp)



## PIN-koodin asettaminen



Seuraavaksi tulee PIN-koodin vaihe. PIN-koodi avaa Trezorisi lukituksen. Se suojaa siis luvattomalta fyysiseltä käytöltä. PIN-koodi ei osallistu Wallet:n salausavainten johtamiseen. Vaikka PIN-koodia ei olisikaan saatavilla, 12-sanaisen Mnemonic-lauseen hallussapito mahdollistaa bitcoinien takaisin saamisen.



Klikkaa Trezor Suitessa "*Jatka PIN-koodiin*" ja sitten "*Set PIN*" -painiketta.



![Image](assets/fr/23.webp)



Vahvista Safe 5:llä.



![Image](assets/fr/24.webp)



Suosittelemme valitsemaan mahdollisimman satunnaisen PIN-koodin. Muista tallentaa tämä koodi erilliseen paikkaan siitä, missä Trezor on tallennettu (esim. salasanahallintaohjelmaan). Voit määrittää 8-50-numeroisen PIN-koodin. Suosittelen, että valitset mahdollisimman pitkän PIN-koodin turvallisuuden parantamiseksi.



Syötä PIN-koodi kosketuslevyllä.



![Image](assets/fr/25.webp)



Kun olet valmis, napsauta oikeassa alareunassa olevaa Green-ruutua ja vahvista PIN-koodi toisen kerran.



![Image](assets/fr/26.webp)



PIN-koodisi on rekisteröity.



![Image](assets/fr/27.webp)



Klikkaa Trezor Suiten "*Complete setup*" -painiketta.



![Image](assets/fr/28.webp)



Safe 5:n konfigurointi on nyt valmis. Voit halutessasi muuttaa Hardware Wallet:n nimeä ja etusivua.



![Image](assets/fr/29.webp)



Trezor Suite -ohjelmistoa ei enää tarvita, paitsi Hardware Wallet:n säännöllisiä laiteohjelmistopäivityksiä varten tai jos haluat tehdä palautustestin. Käytämme nyt Sparrow'ta salkun hallintaan, sillä tämä ohjelmisto soveltuu täydellisesti vain Bitcoin:n käyttöön.



## Salkun määrittäminen Sparrow Wallet -järjestelmässä



Aloita lataamalla ja asentamalla Sparrow Wallet [virallisilta verkkosivuilta](https://sparrowwallet.com/) tietokoneellesi, jos et ole jo tehnyt sitä.



Kun olet avannut Sparrow Wallet:n, varmista, että ohjelmisto on yhdistetty Bitcoin-solmuun, mikä näkyy Interface:n oikeassa alakulmassa olevasta rastista. Jos sinulla on ongelmia Sparrow'n yhdistämisessä, suosittelen tutustumaan tämän ohjeen alkuun:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Napsauta välilehteä "*File*" ja sitten "*New Wallet*".



![Image](assets/fr/30.webp)



Nimeä salkkusi ja napsauta sitten "*Luo Wallet*".



![Image](assets/fr/31.webp)



Valitse avattavasta "*Script Type*"-valikosta skriptityyppi, jota käytetään bitcoinien suojaamiseen. Suosittelen "*Taproot*", tai jos se ei onnistu, "*Native SegWit*".



![Image](assets/fr/32.webp)



Napsauta "*Connected Hardware Wallet*" -painiketta. Safe 5:n on tietenkin oltava kytkettynä tietokoneeseen ja lukituksen on oltava avattu.



Kun liität Safe 5:n tietokoneeseen, jossa Sparrow Wallet on avoinna, sinua pyydetään syöttämään passphrase BIP39 Hardware Wallet-näytöllä. Tätä kehittynyttä vaihtoehtoa käsitellään tulevassa opetusohjelmassa. Toistaiseksi voit yksinkertaisesti napsauttaa oikeassa yläkulmassa olevaa Green-rastia vahvistaaksesi, että haluat käyttää tyhjää passphrase:tä (eli ilman passphrase:tä). Jos haluat estää Trezoria pyytämästä passphrase:n syöttämistä aina käynnistyksen yhteydessä, mene Trezor Suite -ohjelmaan, avaa asetukset ja vaihda "*Laite*" -kohdassa olevaa vaihtoehtoa > "*Wallet default*" muotoon "*Standard*" muotoon "*passphrase*".



![Image](assets/fr/33.webp)



Napsauta "*Scan*"-painiketta. Safe 5:n pitäisi ilmestyä näkyviin. Napsauta "*Import Keystore*".



![Image](assets/fr/34.webp)



Näet nyt Wallet:n tiedot, mukaan lukien ensimmäisen tilisi laajennettu julkinen avain. Napsauta "*Apply*"-painiketta viimeistelläksesi Wallet:n luomisen.



![Image](assets/fr/35.webp)



Valitse vahva salasana, jolla varmistat pääsyn Sparrow Wallet:een. Tämä salasana takaa turvallisen pääsyn Sparrow Wallet -tietoihin ja suojaa julkisia avaimia, osoitteita, tarroja ja tapahtumahistoriaa luvattomalta käytöltä.



Suosittelen, että tallennat tämän salasanan salasanahallintaan, jotta et unohda sitä.



![Image](assets/fr/36.webp)



Ja nyt portfoliosi on tuotu Sparrow Wallet:een!



![Image](assets/fr/37.webp)



Ennen kuin saat ensimmäiset bitcoinit Wallet:ään, **suositan vahvasti, että teet tyhjän palautustestin**. Kirjoita muistiin joitakin viitetietoja, kuten xpub-tietosi, ja nollaa sitten Trezor Safe 5 -laitteesi, kun Wallet on vielä tyhjä. Yritä sitten palauttaa Wallet Trezoriin paperivarmistusten avulla. Tarkista, että palautuksen jälkeen luotu xpub vastaa alun perin kirjoittamaasi xpubia. Jos se täsmää, voit olla varma, että paperiset varmuuskopiot ovat luotettavia.



Jos haluat lisätietoja palautustestin suorittamisesta, suosittelen, että tutustut tähän toiseen opetusohjelmaan:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Miten voin vastaanottaa bitcoineja Trezor Safe 5:llä?



Napsauta Sparrow'ssa välilehteä "*Vastaanottaa*".



![Image](assets/fr/38.webp)



Ennen kuin käytät Sparrow Wallet:n ehdottamaa Address:ää, tarkista se Trezorin näytöltä. Näin voit varmistaa, että Sparrow'n näyttämä Address ei ole vilpillinen ja että Hardware Wallet:lla todella on yksityinen avain, jota tarvitaan tällä Address:llä suojattujen bitcoinien käyttämiseen. Tämä auttaa sinua välttämään useita hyökkäystyyppejä.



Voit tehdä tämän tarkistuksen napsauttamalla painiketta "*näytä Address*".



![Image](assets/fr/39.webp)



Tarkista, että Trezorissasi näkyvä Address vastaa Sparrow Wallet:ssa olevaa Address:ta. Tämä tarkistus kannattaa tehdä juuri ennen Address:n lähettämistä lähettäjälle, jotta voit olla varma sen oikeellisuudesta. Voit vahvistaa sen painamalla näyttöä.



![Image](assets/fr/40.webp)



Voit sitten lisätä "*Label*" kuvaamaan tämän Address:n avulla suojattavien bitcoinien lähdettä. Tämä on hyvä käytäntö, jonka avulla voit paremmin hallita UTXO:tasi.



![Image](assets/fr/41.webp)



Tämän Address:n avulla voit sitten vastaanottaa bitcoineja.



![Image](assets/fr/42.webp)



## Miten lähetän bitcoineja Trezor Safe 5:llä?



Nyt kun olet saanut ensimmäiset Satssit Safe 5 -vakuudellisesta Wallet:sta, voit myös käyttää ne! Kytke Trezor tietokoneeseen, avaa sen lukitus PIN-koodilla, käynnistä Sparrow Wallet ja siirry sitten "*lähettää*"-välilehdelle rakentaaksesi uuden tapahtuman.



![Image](assets/fr/43.webp)



Jos haluat *kolikoiden hallintaa*, eli valita tarkkaan, mitä UTXO:ta haluat käyttää transaktiossa, siirry "*UTXO:t*"-välilehdelle. Valitse UTXO:t, jotka haluat käyttää, ja napsauta sitten "*Send Selected*". Sinut ohjataan samalle "*Lähettää*"-välilehdelle, mutta UTXOt on jo valittu tapahtumaa varten.



![Image](assets/fr/44.webp)



Syötä määränpää Address. Voit myös syöttää useita osoitteita napsauttamalla "*+ Lisää*"-painiketta.



![Image](assets/fr/45.webp)



Kirjoita "*Label*", jotta muistat tämän menon tarkoituksen.



![Image](assets/fr/46.webp)



Valitse tälle Address:lle lähetettävä summa.



![Image](assets/fr/47.webp)



Säädä maksutapahtuman maksuprosentti kulloisenkin markkinatilanteen mukaan. Voit esimerkiksi käyttää [Mempool.space](https://Mempool.space/) sopivan maksun valitsemiseen.



Varmista, että kaikki tapahtumaparametrit ovat oikein, ja napsauta sitten "*Luo tapahtuma*".



![Image](assets/fr/48.webp)



Jos olet tyytyväinen kaikkeen, napsauta "*Viimeistele tapahtuma allekirjoittamista varten*".



![Image](assets/fr/49.webp)



Napsauta "*Sign*".



![Image](assets/fr/50.webp)



Napsauta Trezor Safe 5:n vieressä olevaa "*Sign*"-painiketta.



![Image](assets/fr/51.webp)



Tarkista tapahtuman parametrit Hardware Wallet-näytöltä, mukaan lukien vastaanottajan vastaanottava Address, lähetetty summa ja maksu. Kun maksutapahtuma on tarkistettu Trezorissa, allekirjoita se painamalla ja pitämällä näyttöä painettuna.



![Image](assets/fr/52.webp)



Tapahtumasi on nyt allekirjoitettu. Tarkista vielä kerran, että kaikki on kunnossa, ja klikkaa sitten "*Broadcast Transaction*" lähettääksesi sen Bitcoin-verkkoon.



![Image](assets/fr/53.webp)



Löydät sen Sparrow Wallet:n "*Transaktiot*"-välilehdeltä.



![Image](assets/fr/54.webp)



Onneksi olkoon, olet nyt perillä Trezor Safe 5:n peruskäytöstä Sparrow Wallet:n kanssa! Jos haluat mennä askeleen pidemmälle, suosittelen tätä kattavaa opetusohjelmaa Trezor Hardware Wallet:n käytöstä passphrase BIP39:n kanssa turvallisuuden parantamiseksi:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Jos löysit tämän ohjeen hyödylliseksi, olisin kiitollinen, jos jättäisit Green peukalon alle. Voit vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissa. Kiitos paljon!