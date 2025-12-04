---
name: Dana Wallet
description: Minimalistinen salkku hiljaisia maksuja varten (BIP-352)
---

![cover](assets/cover.webp)



Bitcoin-osoitteiden uudelleenkäyttö on yksi välittömimmistä uhkista käyttäjien luottamuksellisuudelle. Kun vastaanottaja käyttää samaa osoitetta useiden maksujen vastaanottamiseen, kuka tahansa tarkkailija voi jäljittää kaikki siihen liittyvät maksutapahtumat ja rekonstruoida niiden taloushistorian. Tämä ongelma vaikuttaa erityisesti sisällöntuottajiin, hyväntekeväisyysjärjestöihin ja aktivisteihin, jotka haluavat julkisesti näyttää lahjoitusosoitteen vaarantamatta omaa tai lahjoittajiensa yksityisyyttä.



Dana Wallet vastaa tähän ongelmaan tyylikkäällä ratkaisulla: Hiljaiset maksut. Tämä minimalistinen, avoimen lähdekoodin wallet, joka lanseerataan vuonna 2024, luo uudelleenkäytettävän staattisen osoitteen ja takaa samalla, että jokainen vastaanotettu maksu päätyy erilliseen osoitteeseen lohkoketjussa. Lähettäjän ei tarvitse olla etukäteen vuorovaikutuksessa vastaanottajan kanssa, eikä yksikään ulkopuolinen tarkkailija voi yhdistää yksittäisiä maksutapahtumia toisiinsa. Lohkoketjussa nämä maksut näyttävät täysin tavallisilta Taproot-tapahtumilta.



Dana Wallet on saatavilla Mainnet:ssa ja Signetissä, mutta kehittäjät pitävät sitä edelleen kokeellisena ja suosittelevat, että et talleta varoja, joita et ole valmis menettämään. Tässä oppaassa käytämme Signet-versiota tutustuaksemme Silent Paymentsiin riskeeraamatta oikeita varoja.



## Mikä on Dana Wallet?



### Filosofia ja tavoitteet



Dana Wallet noudattaa "SP-first"-lähestymistapaa: wallet tuottaa ainoastaan hiljaisten maksujen osoitteita ja hyväksyy vain tämäntyyppisiä maksuja. Tällä sovelluksella ei voi luoda klassista Bitcoin-osoitetta (legacy-, SegWit- tai Taproot-standardi). Tämän tarkoituksellisen rajoituksen ansiosta voit keskittyä täysin BIP-352-protokollan oppimiseen ilman, että muut ominaisuudet häiritsevät sinua. Selkeä käyttöliittymä suosii tarkoituksellisesti helppokäyttöisyyttä vaihtoehtojen runsauden sijaan, joten työkalu on helppokäyttöinen myös on-chain-luottamuksellisuuden käsitteisiin vasta tutustuneille käyttäjille.



Hanke on täysin avoimen lähdekoodin hanke, jossa käytetään Flutteria mobiilikäyttöliittymää varten ja Rust:ta sisäistä salauslogiikkaa varten. Tässä arkkitehtuurissa yhdistyvät sujuva käyttäjäkokemus ja optimaalinen suorituskyky intensiivisiä skannaustoimintoja varten.



### Miten hiljaiset maksut toimivat?



Hiljaiset maksut (BIP-352) perustuvat kehittyneeseen salausmekanismiin, jossa käytetään Elliptic Curve Diffie-Hellman -avainta Exchange (ECDH). Vastaanottaja luo staattisen osoitteen (joka alkaa `sp1...` mainnet:ssa tai `tsp1...` Signetissä), joka koostuu kahdesta eri julkisesta avaimesta: skannausavain ($B_{scan}$) saapuvien maksujen havaitsemiseksi ja rahankäyttöavain ($B_{spend}$) saatujen varojen käyttämiseksi. Tämä erottelu mahdollistaa sen, että rahankäyttöavain voidaan pitää wallet-laitteistossa ja skannausavainta voidaan käyttää liitetyssä laitteessa.



Kun lähettäjä haluaa suorittaa maksun, hänen wallet:nsa yhdistää syötteidensä yksityisten avainten summan ja vastaanottajan julkisen skannausavaimen jaetun ECDH-salaisuuden laskemiseksi. Tämä salaisuus tuottaa kryptografisen "virityksen", joka lisättynä vastaanottajan maksuavaimeen luo ainutlaatuisen Taproot-osoitteen kyseistä maksutapahtumaa varten.



Vastaanottaja voi toistaa tämän laskennan käyttämällä yksityistä skannausavainta ja transaktiossa näkyviä julkisia avaimia (Diffie-Hellmanin matemaattinen ominaisuus). Näin hän voi havaita ja käyttää varat ilman edeltävää vuorovaikutusta lähettäjän kanssa.



Tämä lähestymistapa tarjoaa useita etuja:




- Vastaanottajan luottamuksellisuus**: jokainen maksu päätyy eri osoitteeseen
- Lähettäjän luottamuksellisuus**: maksuja ei yhdistetä pysyvällä tunnisteella
- Ei kolmannen osapuolen palvelinta**: protokolla toimii itsenäisesti
- Erottamattomat liiketoimet**: Hiljaiset maksut näyttävät tavallisilta Taproot-tapahtumilta



Suurin haittapuoli on skannauksen kustannukset: vastaanottajan on analysoitava jokainen uusi Taproot-tapahtuma havaitakseen hänelle tarkoitetut tapahtumat.



Jos haluat lisätietoja Hiljaisten maksujen teknisestä toiminnasta, suosittelemme Bitcoin:n luottamuksellisuutta käsittelevää BTC204-kurssia, jossa on luku, joka koskee Hiljaisia maksuja:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Tuetut alustat



Dana Wallet on saatavilla Android-sovelluksena. APK:n voi ladata kehittäjien tarjoamasta F-Droid-arkistosta, Obtainiumin kautta tai suoraan GitHubista. Linux-käyttäjille on teknisesti mahdollista kääntää Flutter-sovellus työpöydälle.



Sovellus ei ole saatavilla iOS:ssä eikä virallisissa kaupoissa (Google Play, App Store), mikä kuvastaa sen kokeellista asemaa ja keskittymistä tekniseen yleisöön.



## Asennus



### Olennaiset edellytykset



Jotta voit asentaa Dana Wallet:n Androidiin, tarvitset Android-laitteen, jonka tietoturva-asetuksissa on otettu käyttöön "Tuntemattomat lähteet" -vaihtoehto. Tiliä tai rekisteröintiä ei tarvita.



### Lisää F-Cold talletus



Suositeltava tapa on lisätä Dana Wallet:n oma F-Droid-tietovarasto. Mene osoitteeseen `fdroid.silentpayments.dev`, josta löydät arkiston linkin ja QR-koodin skannattavaksi. Arkisto tarjoaa tällä hetkellä 3 sovellusta: Mainnet-versio, Development ja Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Asennus F-Droidin kautta



Avaa F-Droid-sovellus Android-laitteessasi ja siirry sitten Asetuksiin oikeassa alakulmassa olevan kuvakkeen kautta. Valitse "Repositories", jos haluat hallita sovellusten lähteitä. Lisää uusi arkisto painamalla "+"-painiketta ja skannaa QR-koodi tai liitä linkki "https://fdroid.silentpayments.dev/fdroid/repo". Kun arkisto on lisätty, näet Dana Wallet:n kolme saatavilla olevaa versiota. Valitse "Dana Wallet - kirjanmerkki" ja paina "Asenna".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Alkuperäinen konfigurointi



### Portfolion luominen



Ensimmäisen käynnistyksen yhteydessä Dana Wallet näyttää tervetuloruudun, jossa esitellään sen tehtävä: "Lähetä ja vastaanota lahjoituksia ilman välikäsiä". Jatka painamalla "Begin". Seuraavassa näytössä esitellään sovelluksen kolme keskeistä etua:




- Vaivaton lahjoittaminen**: aloita lahjoitusten vastaanottaminen muutamassa sekunnissa
- Yksityisyys oletusarvoisesti**: ei tarvetta palvelimille tai monimutkaiselle infrastruktuurille
- Sähköpostin kaltainen kokemus**: lähetä ja vastaanota bitcoineja yhtä yksinkertaisesti kuin sähköpostilla



Voit valita joko "Palauta", jos haluat palauttaa olemassa olevan salkun, tai "Luo uusi wallet", jos haluat luoda uuden salkun. Paina "Luo uusi wallet".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



Tämän jälkeen sovellus luo palautuslausekkeen, joka sinun on kirjattava huolellisesti muistiin fyysiselle tietovälineelle. Ota käyttöön hyvät varmuuskopiointikäytännöt myös sellaisten testivarojen osalta, joilla ei ole todellista arvoa.



### Interface ja parametrit



Kun salkku on luotu, pääset pääkäyttöliittymään, joka on jaettu kahteen välilehteen: "Transact" ja "Settings".



**Transaktio**-välilehdellä näytetään bitcoin-saldosi (ja sen muuntaminen dollareiksi), luettelo viimeisimmistä transaktioista ja kaksi toimintopainiketta: "Maksa" varojen lähettämistä varten ja vastaanottopainike (latauskuvake).



**Asetukset**-välilehdellä on neljä vaihtoehtoa:




- Näytä seed-lause**: näyttää palautuslauseesi säilytettäväksi
- Vaihda fiat-valuutta**: vaihda näyttövaluutta (oletusarvoisesti USD)
- Set backend url**: määritä Blindbit-palvelimen URL-osoite (katso seuraava kohta)
- Wipe wallet**: pyyhkii wallet:n kokonaan laitteesta



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Blindbit-palvelin



Dana Wallet käyttää indeksointipalvelinta nimeltä **Blindbit** havaitakseen hiljaiset maksut. Sen toiminnan ymmärtäminen on tärkeää sovelluksen luottamusmallin arvioimiseksi.



**Mihin tarvitsemme palvelimen?



Hiljaisen maksun havaitsemiseksi wallet:n on teoriassa skannattava kaikki Taproot-transaktiot kussakin lohkossa ja suoritettava salauslaskenta (ECDH) jokaiselle. Matkapuhelimessa tämä operaatio olisi liian laskenta- ja kaistanleveysintensiivinen.



Blindbit-palvelin ratkaisee tämän ongelman laskemalla etukäteen välitiedot (joita kutsutaan "tweaksiksi") kaikkia Taproot-tapahtumia varten. Sen jälkeen wallet lataa nämä tweakit (33 tavua per tapahtuma) ja suorittaa lopullisen laskennan **lokaalisti** tarkistaakseen, kuuluuko maksu sinulle.



**Säilytetään luottamuksellisuus**



Toisin kuin tavallisella Electrum-palvelimella, jossa paljastat osoitteesi, Blindbit-palvelin ei tiedä, mitkä maksut kuuluvat sinulle. Se antaa samat tiedot kaikille käyttäjille, ja puhelimesi suorittaa lopullisen tarkistuksen. Näin ollen luottamuksellisuutesi säilyy palvelimeen nähden.



**Esimerkkipalvelin



Dana Wallet käyttää julkista palvelinta `silentpayments.dev/blindbit/signet` (Signet) tai `silentpayments.dev/blindbit/mainnet` (Mainnet). Voit muuttaa tätä URL-osoitetta asetuksissa, jos isännöit omaa palvelinta.



**Hosta oma Blindbit-palvelimesi**



Käyttäjät, jotka haluavat olla täysin riippumattomia, voivat isännöidä omaa Blindbit Oracle -palvelinta. Tämä vaatii :




- Täydellinen Bitcoin-ydinsolmu **ei-korvattu** (ei-pruned)
- Blindbit Oraclen asentaminen (saatavilla GitHubissa: `setavenger/blindbit-oracle`)
- Noin 10 GB lisää levytilaa
- Tekniset taidot (Go-käännöstyö, palvelinkonfigurointi)



Umbrelille tai Start9:lle ei ole vielä saatavilla pakattua sovellusta. Asennus on toistaiseksi manuaalinen. Tämä ala on aktiivisessa kehityksessä, ja tulevaisuudessa saattaa tulla esiin helpommin lähestyttäviä ratkaisuja.



## Päivittäinen käyttö



### Varojen vastaanottaminen



Jos haluat vastaanottaa bitcoineja, paina vastaanota-painiketta (latauskuvake) päänäytöltä. Dana Wallet näyttää sitten täydellisen Silent Payment -osoitteesi muodossa `tsp1q...` kirjanmerkin kohdalla. Käyttöliittymä tarjoaa useita vaihtoehtoja:




- Näytä QR-koodi**: näyttää osoitteesi QR-koodin helppoa skannausta varten
- Jaa**: jaa osoite puhelimesi sovellusten kautta
- Kopioi**: kopioi osoitteen leikepöydälle



Kuten näytössä näkyy, voit jakaa tämän osoitteen julkisesti sosiaalisissa verkostoissa vaarantamatta yksityisyyttäsi.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Jos haluat saada ensimmäiset testivarasi Signetistä, käytä erityistä Silent Payments -hanaasi, joka on saatavilla osoitteessa `silentpayments.dev/faucet/signet`. Kopioi osoitteesi `tsp1...`, liitä se hanan kenttään ja vahvista pyyntö. Odota, että lohko louhitaan (noin 10 minuuttia Signetissä).



### Lähetä maksu



Jos haluat lähettää varoja, paina "Maksa"-painiketta päänäytössä. Näyttöön tulee "Valitse vastaanottaja(t)" -näyttö, jossa on kolme vaihtoehtoa vastaanottajan määrittämiseksi:




- Syötä maksutiedot manuaalisesti
- Liitä leikepöydältä**: liittää osoitteen leikepöydältä
- Skannaa QR-koodi**: skannaa osoitteen sisältävä QR-koodi



Kun vastaanottajan osoite on vahvistettu, voit syöttää lähetettävän summan satosheina "Syötä summa" -näytölle. Käytettävissä oleva saldosi näytetään viitteeksi. Jatka painamalla "Siirry maksun valintaan".



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



Seuraavalla näytöllä näkyy kolme maksutasoa, jotka riippuvat kiireellisyydestä:




- Nopea** (10-30 minuuttia): nopeasta vahvistuksesta peritään korkeammat maksut
- Normaali** (30-60 minuuttia): kohtuulliset kustannukset
- Hidas** (1+ tunti): vähimmäismaksu ei-kiireellisistä maksutapahtumista



Kun olet valinnut maksutason, "Valmis lähettämään?" -vahvistusnäytössä on yhteenveto kaikista yksityiskohdista: kohdeosoite, summa, arvioitu aika ja transaktiomaksu. Tarkista nämä tiedot huolellisesti ja lähetä tapahtuma painamalla "Lähetä".



Lähetyksen jälkeen tapahtuma näkyy historiassasi tilassa "Vahvistamaton", kunnes se sisällytetään estoon. Saldosi päivittyy vastaavasti.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Edut ja rajoitukset



### Kohokohdat





- Pedagoginen**: yksinkertaistettu käyttöliittymä, jossa keskitytään oppimiseen Hiljaiset maksut
- Kaksisuuntainen**: tukee sekä lähettämistä että vastaanottamista, toisin kuin muut portfoliot
- Avoin lähdekoodi**: täysin tarkastettavissa oleva koodi GitHubissa
- Erityinen Faucet**: helpottaa testausrahoituksen saamista
- Ilman tiliä**: rekisteröintiä tai henkilötietoja ei tarvita



### Huomioon otettavat rajoitukset





- Kokeellinen**: auditoimaton ohjelmisto, Mainnet:ssä on noudatettava varovaisuutta
- Rajoitettu käyttöjärjestelmä**: pääasiassa Android, ei iOS-versiota
- Vähennetyt toiminnot**: ei kolikonhallintaa, ei alatilejä, ei Lightningia
- Intensiivinen skannaus**: maksujen havaitseminen kuluttaa merkittävästi resursseja



## Parhaat käytännöt



### seed turvallisuus



Jopa Signet-testeissä, joilla on arvoton tausta, suhtaudu toipumislausekkeeseen vakavasti. Käytä asetuksissa olevaa "Näytä seed-lause" -vaihtoehtoa kirjoittaaksesi sen huolellisesti muistiin. Pidä hyvänä käytäntönä yllä täysin erillisiä lompakoita Signetille ja Mainnet:lle: älä koskaan käytä testausta varten luotua seed:ää wallet:ssa, joka on tarkoitettu oikeiden varojen vastaanottamiseen.



### Varoitus kokeellisesta tilasta



Dana Wallet:n kehittäjät pitävät sitä edelleen kokeellisena. Kuten he selvästi toteavat: "Älä käytä varoja, joita et ole valmis menettämään". Valitse oppimistarkoituksiin Signet-versio. Jos käytät Mainnet-versiota, rajoitu token-määriin.



### Varmuuskopiointi ja palauttaminen



Hiljaisten maksujen varojen takaisinperintä edellyttää wallet:ää, joka on yhteensopiva BIP-352-protokollan kanssa. Tavallinen wallet ei voi skannata lohkoketjua UTXO Silent Payments -rahaston palauttamiseksi. Pidä Dana Wallet asennettuna tai käytä "Restore"-vaihtoehtoa ensimmäisellä käynnistyksellä olemassa olevan wallet:n palauttamiseksi.



## Vertailu BIP-47:ään ja PayJoin:een



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Hiljaiset maksut poistavat BIP-47-ilmoitustapahtuman, mutta maksavat kalliimman skannauksen. PayJoin ratkaisee toisenlaisen ongelman (tulojen korrelaatio), ja se voidaan yhdistää hiljaisiin maksuihin.



## Päätelmä



Dana Wallet on arvokas koulutusväline, jonka avulla voit oppia hiljaisista maksuista riskittömässä ympäristössä. Sen minimalistinen lähestymistapa antaa sinulle mahdollisuuden ymmärtää BIP-352-protokollan perusmekanismit ilman, että toissijaiset ominaisuudet häiritsevät sinua. Kokeilemalla Signetillä saat käytännön käsityksen tästä lupaavasta teknologiasta Bitcoin-tapahtumien luottamuksellisuuden takaamiseksi.



Hiljaiset maksut ovat merkittävä edistysaskel helppokäyttöisyyden ja yksityisyyden suojan yhteensovittamisessa. Yhteisön innostus ja ensimmäiset integraatiot eri lompakoihin (Cake Wallet, BitBox02, BlueWallet lähettämistä varten) viittaavat tulevaisuuteen, jossa lahjoitusosoitteen julkaiseminen ei enää vaaranna omistajan taloudellista yksityisyyttä.



## Resurssit



### Viralliset asiakirjat




- Dana Wallet GitHub-tietovarasto: https://github.com/cygnet3/danawallet
- F-Cold talletus: https://fdroid.silentpayments.dev
- Hiljaiset maksut -yhteisön sivusto: https://silentpayments.xyz
- Eritelmä BIP-352: https://bips.dev/352



### Signet-testityökalut




- Faucet Hiljaiset maksut: https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet



### Blindbit-palvelin (itse isännöity)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle