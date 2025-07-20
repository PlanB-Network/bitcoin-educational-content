---
name: Trezor Safe 3
description: Hardware Wallet Safe 3:n määrittäminen ja käyttö
---
![cover](assets/cover.webp)



*Kuvan luotto: [Trezor.io](https://trezor.io/)*



Trezor Safe 3 on SatoshiLabsin suunnittelema Hardware Wallet, joka on luotu vuonna 2023. Se on erittäin kompakti ja kevyt malli (14 grammaa), joka on suunniteltu sekä aloittelijoille että keskitason käyttäjille. Se on kuuluisan Model One -mallin seuraaja, johon on tehty merkittäviä lisäyksiä, säilyttäen samalla tuotemerkin avoimen lähdekoodin lähestymistavan, joka erottaa sen tärkeimmästä kilpailijastaan Ledger:sta. Safe 3:n hinta on 79 euroa. Se sijoittuu siis Hardware Wallet:n keskiluokkaan ja kilpailee suoraan Ledger Nano S Plus -mallin kanssa.



Safe 3:ssa ei ole akkua, ja se toimii yksinomaan USB-C-liitännän kautta, jota käytetään sekä virransyöttöön että viestintään. Siinä on pieni 0,96 tuuman yksivärinen OLED-näyttö ja kaksi fyysistä painiketta.



![Image](assets/fr/01.webp)



Safe 3 tarjoaa kaikki olennaiset ominaisuudet, joita hyvältä Hardware Wallet:lta odotetaan, mukaan lukien passphrase BIP39:n erinomainen integrointi. Se ei kuitenkaan vielä tue Miniscriptiä.



Tämä malli soveltuu erityisen hyvin aloittelijoille, ja saattaisin jopa suositella Hardware Wallet:tä uudelle käyttäjälle. Se sopii hyvin myös keskitason käyttäjille. Toisaalta se ei ehkä täytä kaikkia Coldcardin kaltaisissa laitteissa saatavilla olevia erityisominaisuuksia etsivien edistyneiden käyttäjien odotuksia. Jos et kuitenkaan tarvitse näitä kehittyneitä vaihtoehtoja, Trezor Safe 3 voi olla erinomainen valinta.



## Trezor Safe 3 -turvamalli



Trezor Safe 3 on nyt varustettu EAL6+-sertifioidulla **Secure Elementillä**, mikä on merkittävä edistysaskel aiempiin malleihin, kuten Model Oneen ja Model T:hen, verrattuna. Kyseessä on OPTIGA Trust M V3 -siru, joka ei tallenna suoraan seed:ta, vaan toimii kryptografisena komponenttina, joka turvaa pääsyn siihen. Secure Element säilyttää salaisuuden, johon pääsee käsiksi vasta, kun käyttäjä on syöttänyt PIN-koodin oikein. Tätä salaisuutta käytetään sitten seed:n salauksen purkamiseen, joka tallennetaan salattuna laitteen keskusmuistiin.



Tämä hybridi-turvajärjestelmä tarjoaa paremman fyysisen suojan, erityisesti louhintatekoja tai invasiivista analyysiä vastaan, jotka olivat Model One -mallissa ongelmallisia erityisesti PIN-koodien hallinnassa. Nämä haavoittuvuudet voidaan nyt kiertää Secure Elementin käytön ansiosta. Tässä mallissa säilytetään myös avoimen lähdekoodin ohjelmistoarkkitehtuuri: yksityisten avainten luomista ja käyttöä hallinnoiva koodi on täysin saatavilla ja todennettavissa. OPTIGA-siru hallinnoi vain PIN-koodia, joka on Bitcoin Wallet-avaimenhallinnan ulkopuolinen elementti. Se julkaisee ainoastaan salaisuuden, jota voidaan käyttää seed:n salauksen purkamiseen. Lisäksi OPTIGA Trust M V3 -sirulla on suhteellisen vapaa lisenssi, joka antaa SatoshiLabsille luvan julkaista vapaasti mahdolliset haavoittuvuudet.



Tämä turvamalli on mielestäni yksi parhaista kompromisseista, joita markkinoilla on tällä hetkellä saatavilla. Siinä yhdistyvät Secure Elementin edut ja avoimen lähdekoodin ohjelmistojen hallinta. Aikaisemmin käyttäjien oli valittava sirun avulla parannetun fyysisen turvallisuuden ja avoimen lähdekoodin avulla saavutetun avoimuuden välillä; Trezor Safe 3:n avulla on mahdollista hyötyä molemmista.



Tässä ohjeessa näytämme, miten Trezor Safe 3 -laite asetetaan ja sitä käytetään turvallisesti.



## Trezor Safe 3:n purkaminen



Kun vastaanotat Safe 3 -laitteen, varmista, että laatikko ja Seal ovat ehjiä, jotta voit varmistaa, että pakettia ei ole avattu. Laitteen aitouden ja eheyden ohjelmistovarmennus suoritetaan myös, kun laite otetaan käyttöön myöhemmin.



Laatikon sisältö sisältää:




- Trezor Safe 3;
- Pussi, joka sisältää kartonkia Mnemonic-lauseen, tarroja ja ohjeet;
- USB-C-USB-C-kaapeli.



![Image](assets/fr/02.webp)



Kun Trezor Safe 3 -laite avataan, sen pitäisi olla suojamuovilla suojattu ja USB-C-portin pitäisi olla suojattu hologrammilla Seal. Varmista, että se on siellä.



![Image](assets/fr/03.webp)



Navigointi laitteessa on suoraviivaista: käytä oikeaa painiketta selataksesi oikealle ja vasenta painiketta selataksesi vasemmalle. Vahvista toiminto painamalla molempia painikkeita samanaikaisesti.



![Image](assets/fr/04.webp)



## Edellytykset



Tässä opetusohjelmassa näytän, miten Trezor Safe 3:a käytetään [Sparrow Wallet -salkunhallintaohjelmiston](https://sparrowwallet.com/download/) kanssa. Jos et ole vielä asentanut tätä ohjelmistoa, tee se nyt. Jos tarvitset apua, meillä on myös yksityiskohtainen ohje Sparrow Wallet:n konfiguroinnista :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Tarvitset myös Trezor Suite -ohjelmiston Safe 3:n konfigurointiin, sen aitouden tarkistamiseen ja laiteohjelmiston asentamiseen. Käytämme tätä ohjelmistoa vain tähän, ja sen jälkeen sitä tarvitaan vain laiteohjelmistopäivityksiin. Wallet:n päivittäiseen hallintaan käytämme yksinomaan Sparrow Wallet:tä, koska se on optimoitu Bitcoin:lle ja helppokäyttöinen myös aloittelijoille (Sparrow tukee vain Bitcoin:tä, ei altcoineja).



[Lataa Trezor Suite virallisilta sivuilta](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



Suosittelen vahvasti, että tarkistat molempien ohjelmien aitouden (GnuPG:llä) ja eheyden (Hash:lla) ennen niiden asentamista koneellesi. Jos et tiedä, miten tämä tehdään, voit seurata tätä toista ohjetta :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Trezor Safe 3:n käynnistäminen



Liitä Safe 3 tietokoneeseen, johon Trezor Suite ja Sparrow Wallet on jo asennettu.



![Image](assets/fr/06.webp)



Avaa Trezor Suite ja napsauta sitten "*Set up my Trezor*".



![Image](assets/fr/07.webp)



Valitse "*Bitcoin-only firmware*" ja napsauta sitten "*Install Bitcoin-only*".



![Image](assets/fr/08.webp)



Trezor Suite asentaa sitten laiteohjelmiston Safe 3 -laitteeseesi. Odota asennuksen aikana.



![Image](assets/fr/09.webp)



Napsauta "*Jatka*".



![Image](assets/fr/10.webp)



Jatka sitten aitoustestiä varmistaaksesi, ettei Hardware Wallet ole väärennös tai vaarannettu.



![Image](assets/fr/11.webp)



Vahvista Safe 3 -laitteessa painamalla oikeaa painiketta.



![Image](assets/fr/12.webp)



Jos Trezor on aito, Trezor Suitessa näkyy vahvistusviesti.



![Image](assets/fr/13.webp)



Tämän jälkeen voit ohittaa ikkunat, joissa on peruskäyttöohjeet.



![Image](assets/fr/14.webp)



## Bitcoin-salkun luominen



Klikkaa Trezor Suiten "*Luo uusi Wallet*" -painiketta.



![Image](assets/fr/15.webp)



Vakiosalkun osalta voit valita oletusvarmuuskopiotyypin. Tämä luo klassisen yhden tunnuksen salkun, jossa on 12-sanainen Mnemonic-lause. Napsauta "*Luo Wallet*".



Jos haluat lisätietoja muista Trezorissa käytettävissä olevista varmuuskopiointivaihtoehdoista, mukaan lukien *Multi-share Backup*, suosittelen tutustumaan myös tähän oppaaseen :



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



Hyväksy Hardware Wallet:n käyttöehdot.



![Image](assets/fr/17.webp)



Luo uusi salkku painamalla uudelleen oikeaa painiketta.



![Image](assets/fr/18.webp)



Klikkaa Trezor Suitessa "*Jatka varmuuskopiointia*".



![Image](assets/fr/19.webp)



Ohjelmisto antaa ohjeet Mnemonic-lauseen hallintaan.



Tämä Mnemonic antaa sinulle täyden, rajoittamattoman pääsyn kaikkiin bitcoineihisi. Kuka tahansa, jolla on hallussaan tämä lauseke, voi varastaa varojasi, vaikka hänellä ei olisi fyysistä pääsyä Trezor Safe 3:een.



12-sanainen lause palauttaa pääsyn bitcoineihisi, jos Hardware Wallet häviää, varastetaan tai rikkoutuu. Siksi on erittäin tärkeää tallentaa se huolellisesti ja säilyttää se turvallisessa paikassa.



Voit kirjoittaa sen laatikossa olevaan pahviin, tai jos haluat lisätä turvallisuutta, suosittelen kaiverrusta ruostumattomasta teräksestä valmistettuun alustaan, joka suojaa sitä tulipalolta, tulvalta tai romahdukselta.



Vahvista ohjeet ja napsauta sitten "*Luo Wallet varmuuskopio*" -painiketta.



![Image](assets/fr/20.webp)



Safe 3 luo Mnemonic-lauseesi satunnaislukugeneraattorin avulla. Varmista, ettei sinua tarkkailla tämän toiminnon aikana. Kirjoita näytöllä annetut sanat haluamallesi fyysiselle välineelle. Turvallisuusstrategiastasi riippuen voit harkita useiden täydellisten fyysisten kopioiden tekemistä lauseesta (mutta ennen kaikkea älä jaa sitä). On tärkeää pitää sanat numeroituina ja juoksevassa järjestyksessä.



***Ei näitä sanoja saa tietenkään koskaan jakaa internetissä, kuten minä teen tässä ohjeessa. Tätä esimerkkiä Wallet käytetään vain Testnet:ssä, ja se poistetaan ohjeen lopussa



Jos haluat lisätietoja oikeasta tavasta tallentaa ja hallita Mnemonic-lauseesi, suosittelen lämpimästi seuraamaan tätä toista opetusohjelmaa, varsinkin jos olet aloittelija:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



Siirry seuraaviin sanoihin napsauttamalla hiiren kakkospainiketta. Voit siirtyä taaksepäin napsauttamalla vasenta painiketta. Kun olet kirjoittanut kaikki sanat ylös, siirry seuraavaan vaiheeseen pitämällä oikeaa painiketta painettuna.



![Image](assets/fr/22.webp)



Valitse Mnemonic-lauseen sanat niiden järjestyksen mukaan varmistaaksesi, että olet kirjoittanut ne oikein. Käytä vasenta ja oikeaa painiketta siirtyäksesi ehdotusten välillä ja valitse sitten oikea sana napsauttamalla kahta painiketta samanaikaisesti.



![Image](assets/fr/23.webp)



Kun tämä vahvistusmenettely on valmis, napsauta oikealla olevaa painiketta.



![Image](assets/fr/24.webp)



## PIN-koodin asettaminen



Seuraavaksi tulee PIN-koodin vaihe. PIN-koodi avaa Trezorisi lukituksen. Se suojaa siis luvattomalta fyysiseltä käytöltä. PIN-koodi ei osallistu Wallet:n salausavainten johtamiseen. Vaikka PIN-koodia ei olisikaan saatavilla, 12-sanaisen Mnemonic-lauseen hallussapito mahdollistaa bitcoinien takaisin saamisen.



Klikkaa Trezor Suitessa "*Jatka PIN-koodiin*" ja sitten "*Set PIN*" -painiketta.



![Image](assets/fr/25.webp)



Vahvista Safe 3:lla.



![Image](assets/fr/26.webp)



Suosittelemme valitsemaan mahdollisimman satunnaisen PIN-koodin. Muista tallentaa tämä koodi erilliseen paikkaan siitä, missä Trezor on tallennettu (esim. salasanahallintaohjelmaan). Voit määrittää 8-50-numeroisen PIN-koodin. Suosittelen, että valitset mahdollisimman pitkän PIN-koodin turvallisuuden parantamiseksi.



Valitse kukin numero vasemmalla ja oikealla painikkeella. Vahvista valinta ja siirry seuraavaan numeroon painamalla molempia painikkeita samanaikaisesti.



![Image](assets/fr/27.webp)



Kun olet valmis, napsauta numeroiden alussa olevaa "*ENTER*"-valintamerkkiä ja vahvista PIN-koodi toisen kerran.



![Image](assets/fr/28.webp)



PIN-koodisi on rekisteröity.



![Image](assets/fr/29.webp)



Klikkaa Trezor Suiten "*Complete setup*" -painiketta.



![Image](assets/fr/30.webp)



Safe 3:n konfigurointi on nyt valmis. Voit halutessasi muuttaa Hardware Wallet:n nimeä ja etusivua.



![Image](assets/fr/31.webp)



Trezor Suite -ohjelmistoa ei enää tarvita, paitsi Hardware Wallet:n säännöllisiä laiteohjelmistopäivityksiä varten tai jos haluat tehdä palautustestin. Käytämme nyt Sparrow'ta salkun hallintaan, sillä tämä ohjelmisto soveltuu täydellisesti vain Bitcoin:n käyttöön.



## Salkun määrittäminen Sparrow Wallet:ssä



Aloita lataamalla ja asentamalla Sparrow Wallet [virallisilta verkkosivuilta](https://sparrowwallet.com/) tietokoneellesi, jos et ole jo tehnyt sitä.



Kun olet avannut Sparrow Wallet:n, varmista, että ohjelmisto on yhdistetty Bitcoin-solmuun, mikä näkyy Interface:n oikeassa alakulmassa olevasta rastista. Jos sinulla on ongelmia Sparrow'n yhdistämisessä, suosittelen, että luet tämän ohjeen alun:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Napsauta välilehteä "*File*" ja sitten "*New Wallet*".



![Image](assets/fr/32.webp)



Nimeä salkkusi ja napsauta sitten "*Luo Wallet*".



![Image](assets/fr/33.webp)



Valitse avattavasta "*Script Type*"-valikosta skriptityyppi, jota käytetään bitcoinien suojaamiseen. Suosittelen "*Taproot*", tai jos se ei onnistu, "*Native SegWit*".



![Image](assets/fr/34.webp)



Napsauta "*Connected Hardware Wallet*" -painiketta. Safe 3:n on tietenkin oltava kytkettynä tietokoneeseen ja lukituksen on oltava avattu.



![Image](assets/fr/35.webp)



Napsauta "*Scan*"-painiketta. Safe 3:n pitäisi tulla näkyviin. Napsauta "*Import Keystore*".



![Image](assets/fr/36.webp)



Näet nyt Wallet:n tiedot, mukaan lukien ensimmäisen tilisi laajennettu julkinen avain. Napsauta "*Apply*"-painiketta viimeistelläksesi Wallet:n luomisen.



![Image](assets/fr/37.webp)



Valitse vahva salasana, jolla varmistat pääsyn Sparrow Wallet:een. Tämä salasana takaa turvallisen pääsyn Sparrow Wallet -tietoihin ja suojaa julkisia avaimia, osoitteita, tarroja ja tapahtumahistoriaa luvattomalta käytöltä.



Suosittelen, että tallennat tämän salasanan salasanahallintaan, jotta et unohda sitä.



![Image](assets/fr/38.webp)



Ja nyt salkkusi on tuotu Sparrow Wallet:een!



![Image](assets/fr/39.webp)



Ennen kuin saat ensimmäiset bitcoinit Wallet:een, **suositan vahvasti, että teet tyhjän palautustestin**. Kirjoita muistiin joitakin viitetietoja, kuten xpub, ja nollaa sitten Trezor Safe 3, kun Wallet on vielä tyhjä. Yritä sitten palauttaa Wallet Trezorilla paperisten varmuuskopioiden avulla. Tarkista, että palautuksen jälkeen luotu xpub vastaa alun perin kirjoittamaasi xpubia. Jos se täsmää, voit olla varma, että paperiset varmuuskopiot ovat luotettavia.



Jos haluat lisätietoja palautustestin suorittamisesta, suosittelen, että tutustut tähän toiseen opetusohjelmaan:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Miten voin vastaanottaa bitcoineja Trezor Safe 3:lla?



Napsauta Sparrow'ssa välilehteä "*Vastaanottaa*".



![Image](assets/fr/40.webp)



Ennen kuin käytät Sparrow Wallet:n ehdottamaa Address:ää, tarkista se Trezorin näytöltä. Näin voit varmistaa, että Sparrow'n näyttämä Address ei ole vilpillinen ja että Hardware Wallet:ssa on todellakin yksityinen avain, jota tarvitaan Address:llä suojattujen bitcoinien käyttämiseen. Näin voit välttää useita hyökkäystyyppejä.



Voit tehdä tämän tarkistuksen napsauttamalla painiketta "*Display Address*".



![Image](assets/fr/41.webp)



Tarkista, että Trezorissasi näkyvä Address vastaa Sparrow Wallet:ssa olevaa Address:ää. Tämä tarkistus kannattaa tehdä myös juuri ennen Address:n lähettämistä lähettäjälle, jotta voit olla varma sen oikeellisuudesta. Voit käyttää painikkeita vahvistamiseen.



![Image](assets/fr/42.webp)



Voit sitten lisätä "*Label*" kuvaamaan tämän Address:n avulla suojattavien bitcoinien lähdettä. Tämä on hyvä käytäntö, jonka avulla voit paremmin hallita UTXO:tasi.



![Image](assets/fr/43.webp)



Tämän Address:n avulla voit sitten vastaanottaa bitcoineja.



![Image](assets/fr/44.webp)



## Miten lähetän bitcoineja Trezor Safe 3:lla?



Nyt kun olet saanut ensimmäiset Satssit Safe 3 -vakuudellisesta Wallet:stäsi, voit myös käyttää ne! Kytke Trezor tietokoneeseen, avaa sen lukitus PIN-koodilla, käynnistä Sparrow Wallet ja siirry sitten "*lähettää*"-välilehdelle rakentaaksesi uuden tapahtuman.



![Image](assets/fr/45.webp)



Jos haluat *kolikoiden hallintaa*, eli valita tarkkaan, mitä UTXO:ta haluat käyttää transaktiossa, siirry "*UTXO:t*"-välilehdelle. Valitse UTXO:t, jotka haluat käyttää, ja napsauta sitten "*Send Selected*". Sinut ohjataan samalle "*Lähettää*"-välilehdelle, mutta UTXOt on jo valittu tapahtumaa varten.



![Image](assets/fr/46.webp)



Syötä määränpää Address. Voit myös syöttää useita osoitteita napsauttamalla "*+ Lisää*"-painiketta.



![Image](assets/fr/47.webp)



Kirjoita "*Label*", jotta muistat tämän menon tarkoituksen.



![Image](assets/fr/48.webp)



Valitse tähän Address:een lähetettävä summa.



![Image](assets/fr/49.webp)



Säädä maksutapahtuman maksuprosentti kulloisenkin markkinatilanteen mukaan. Voit esimerkiksi käyttää [Mempool.space](https://Mempool.space/) valitaksesi sopivan maksuprosentin.



Varmista, että kaikki tapahtumaparametrit ovat oikein, ja napsauta sitten "*Luo tapahtuma*".



![Image](assets/fr/50.webp)



Jos olet tyytyväinen kaikkeen, napsauta "*Viimeistele tapahtuma allekirjoittamista varten*".



![Image](assets/fr/51.webp)



Napsauta "*Sign*".



![Image](assets/fr/52.webp)



Napsauta Trezor Safe 3:n vieressä olevaa "*Sign*"-painiketta.



![Image](assets/fr/53.webp)



Tarkista tapahtuman parametrit Hardware Wallet-näytöltä, mukaan lukien vastaanottajan vastaanottava Address, lähetetty summa ja maksu. Kun maksutapahtuma on tarkistettu Trezorissa, allekirjoita se napsauttamalla molempia painikkeita samanaikaisesti.



![Image](assets/fr/54.webp)



Tapahtumasi on nyt allekirjoitettu. Tarkista vielä kerran, että kaikki on kunnossa, ja klikkaa sitten "*Broadcast Transaction*" lähettääksesi sen Bitcoin-verkkoon.



![Image](assets/fr/55.webp)



Löydät sen Sparrow Wallet:n "*Transaktiot*"-välilehdeltä.



![Image](assets/fr/56.webp)



Onneksi olkoon, olet nyt perillä Trezor Safe 3:n peruskäytöstä Sparrow Wallet:n kanssa! Jos haluat mennä askeleen pidemmälle, suosittelen tätä kattavaa opetusohjelmaa Hardware Wallet Trezorin ja passphrase BIP39:n käytöstä passphrase BIP39:n kanssa turvallisuuden parantamiseksi:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Jos löysit tämän ohjeen hyödylliseksi, olisin kiitollinen, jos jättäisit Green-peukalon alle. Voit vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissa. Kiitos paljon!