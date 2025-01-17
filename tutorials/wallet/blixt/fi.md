---
name: Blixt

description: Mobiili LN Node Lompakko
---

![esittely](assets/blixt_intro_en.webp)

## Tehokas BTC/Lightning node taskussasi, missä ikinä oletkin

Haluaisin esitellä sinulle mielenkiintoisen ja tehokkaan uuden BTC/LN mobiilinoden ja lompakon – Blixt. Nimi tulee ruotsin kielestä ja tarkoittaa "salamaa".
Jos et ole koskaan käyttänyt Bitcoin Lightning Networkia, ennen kuin aloitat, lue [tämä yksinkertainen selitys vertaus Lightning Networkista (LN)](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport).

## TÄRKEITÄ NÄKÖKOHTIA:

### 1. Blixt on yksityinen node, EI reititysnode! Pidä tämä mielessä.

Tämä tarkoittaa, että kaikki LN-kanavat Blixtissä ovat ilmoittamattomia LN-graafissa (ns. yksityiset kanavat). Tämä tarkoittaa, ETTÄ TÄMÄ NODE EI TEE REITITYSTÄ muiden maksuille Blixt noden kautta. [Lue lisää yksityisistä ja julkisista kanavista täältä](https://voltage.cloud/blog/lightning-network-faq/what-are-the-differences-between-public-and-private-channels/).

Blixt mobiilinode EI ole reititykseen, toistan. Se on pääasiassa omien LN-kanaviesi hallintaan ja LN-maksujesi tekemiseen yksityisesti, aina kun tarvitset.

Blixt mobiilinoden on oltava verkossa ja synkronoituna VAIN ENNEN kuin aiot tehdä transaktiosi. Siksi näet yläosassa kuvakkeen, joka osoittaa synkronoinnin tilan. Se vie vain hetken, riippuen siitä, kuinka kauan pidit sen offline-tilassa ja synkronoit LN-graafin uudelleen.

### 2. Blixt käyttää LND (aezeed) -lompakon taustajärjestelmänä, joten älä yritä tuoda muita bitcoin-lompakkotyyppejä siihen.

[Tässä on selitetty lompakkotyypit](https://coldbit.com/what-types-of-mnemonic-seeds-are-used-in-bitcoin/). Joten jos sinulla oli aiemmin LND-node, voit tuoda siemenen ja backup.channels Blixtiin, [kuten tässä oppaassa selitetään](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario).

### 3. Tärkeitä Blixt-linkkejä (ole hyvä ja lisää kirjanmerkkeihin):

- [Blixt Github-repositorio](https://github.com/hsjoberg/blixt-wallet) | [Github Releases](https://github.com/hsjoberg/blixt-wallet/releases) (lataa apk-tiedosto suoraan)
- [Blixt Ominaisuudet -sivu](https://blixtwallet.github.io/features) - selittää yksitellen jokaisen ominaisuuden ja toiminnallisuuden.
- [Blixt FAQ -sivu](https://blixtwallet.github.io/faq) - Lista Q&A:sta ja Blixtin vianmäärityksestä
- [Blixt Oppaat -sivu](https://blixtwallet.github.io/guides) - demoja, video-oppaita, lisäoppaita ja käyttötapauksia Blixtille
- [Tulostettava A4-esite](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer) Blixtin ensiaskeleista, eri kielillä.
- Blixt tarjoaa myös täysin toimivan demon suoraan [verkkosivustollaan](https://blixtwallet.com) tai omistetussa [web-versiossa](https://blixt-wallet-git-master-hsjoberg.vercel.app/), jotta voit kokea täyden testauksen ennen Blixtin käyttöä todellisessa maailmassa.
- [Geyser joukkorahoitussivu](https://geyser.fund/project/blixt) - lahjoita satseja haluamallasi tavalla tukeaksesi projektia
- [Telegram-tukiryhmä](https://t.me/blixtwallet)
# Saatavilla olevat keskeiset ominaisuudet

## Neutrino Node

Blixt yhdistää oletuksena Blixtin palvelimeen synkronoidakseen lohkoja ja indeksoi Neutrinon avulla (SPV-tila yksinkertaistettua maksuvahvistusta varten), mutta käyttäjä voi myös yhdistää omaan solmuunsa. On yllättävää, että SPV-solmun synkronointi kestää alle 5 minuuttia, omassa tapauksessani Android 11:ssä, ollakseen valmis käyttämään täyttä solmukukkaroa (on-chain ja LN).

## Täysin omavalvottava solmu

Käyttäjä voi hallita omia kanaviaan helppokäyttöisen käyttöliittymän ja riittävän näytetyn tiedon avulla, jotta kokemus on hyvä. Vasemmassa yläkulmassa olevasta valikosta voit siirtyä Lightning-kanaviin aloittaaksesi niiden avaamisen muiden solmujen kanssa, kuten haluat. Älä unohda ottaa Toria käyttöön asetuksissa. Se on paljon parempi yksityisyyden kannalta ja myös siksi, että mobiilisolmuna, jos vaihdat internet-yhteyttä / clearnet-IP:tä usein, vertaisverkkosi saattavat häiriintyä. Tor-solmun URI:n avulla sinulla on aina sama yksityinen tunniste riippumatta sijainnistasi / IP:stäsi.

## Varmuuskopioi/palauta LND-solmu

Voimakas, helppohallintainen ja hyödyllinen ominaisuus on muiden kuolleiden LND-solmujen palauttaminen, vain 24 sanan siemenlistalla ja channels.backup-tiedostolla.

> [Tässä on opas kuolleiden Umbrel-solmujen palauttamiseen Blixtissä SHTF-tilanteessa.](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario)

Käyttäjällä on myös mahdollisuus tallentaa Blixt-kanavavarmuuskopio Google Driveen ja/tai paikalliseen tallennustilaan omalla mobiililaitteellaan (siirtääkseen sen myöhemmin turvalliseen paikkaan, pois puhelimestasi).

Palautusprosessi on melko yksinkertainen: syötä 24 sanan siemen, lisää varmuuskopiotiedosto (aiemmin kopioitu mobiilimuistiin) ja napsauta palauta. Synkronointiin ja kaikkien aiempien tapahtumiesi lohkojen skannaukseen kuluu jonkin verran aikaa. Kanavat suljetaan automaattisesti ja varat palautetaan on-chain-lompakkoosi (katso vasemman yläkulman valikko - on-chain).

> Jos sinulla oli aiemmin avoimia kanavia vanhan solmusi kanssa Torin takana, sinun on ensin otettava Tor-vaihtoehto käyttöön (ja käynnistettävä sovellus uudelleen) valikkoasetuksista. Näin sulkemismenettely ei epäonnistu ja/tai pakotettua sulkemisvaihtoehtoa ei käytetä.

Muista varmuuskopioida LN-kanavasi avaamisen ja/tai sulkemisen jälkeen. Turvallisuuden varmistaminen vie vain muutaman sekunnin. Myöhemmin voit siirtää varmuuskopiotiedoston turvalliseen paikkaan pois mobiililaitteestasi.
Testataksesi siementäsi palautusskenaariossa ennen varojen lisäämistä, käytä vain samaa 24 sanan siementä (aezeed) BlueWalletissa. Jos tuotettu BTC-osoite on sama Blixtissä, olet valmis jatkamaan. BlueWalletin käyttöä ei tarvita sen jälkeen, voit yksinkertaisesti poistaa testatun lompakon palautusta varten.

## Sisäänrakennettu Tor

Kun olet aktivoinut sen, sovellus käynnistyy uudelleen Tor-verkon kautta. Tästä hetkestä lähtien voit nähdä valikkoasetuksissasi solmuidentiteettisi sipuliosoitteella, jotta muut solmut voivat avata kanavia pienelle Blixt-mobiilisolmullesi. Tai sanotaan, että sinulla on oma solmusi kotona ja haluat avata pieniä kanavia Blixt-mobiilisolmullesi. Täydellinen yhdistelmä.

## Dunder LSP - Likviditeetin tarjoaja

Yksinkertainen ja fantastinen ominaisuus, joka tarjoaa uusille käyttäjille mahdollisuuden alkaa vastaanottaa BTC:tä Lightning Networkissa välittömästi, ilman tarvetta tallettaa varoja on-chain ja sitten avata LN-kanavia.
Uusille käyttäjille tämä on loistava uutinen, sillä heidän on tarkoitus pystyä aloittamaan alusta, suoraan LN-verkossa. Tämän tekemiseksi luo vain LN-lasku päävalikosta "vastaanota" -painikkeen kautta, syötä summa, kuvaus jne., ja maksa toisesta lompakosta. Blixt avaa kanavan jopa 400k satoshiin asti per vastaanotettu transaktio. Voit avata useita kanavia tarvittaessa.
Mielenkiintoinen ja hyödyllinen tapaus on seuraava: sanotaan, että ensimmäinen vastaanottamasi summa on 200k. Blixt avaa 400k satoshin kanavan, jossa on jo 200k (miinus avausmaksut) puolellasi, mutta koska sinulla on vielä 200k "tilaa" käytettävissä, voit vastaanottaa lisää. Joten seuraava maksu, sanotaan 100k, saapuu suoraan tämän kanavan kautta, ilman lisämaksuja, ja sinulla on edelleen 100k tilaa vastaanottaa lisää.

Mutta jos päätät vastaanottaa, sanotaan, 300k kolmannelle maksulle, se luo toisen uuden 400k kanavan ja siirtää nämä 300k puolellesi.

Jos pyyntöjä on liikaa, Blixt-solmu voi säätää kanavan kapasiteettia avauksen aikana.

## Automaattinen Kanavan Avaaminen

Asetuksissa käyttäjä voi aktivoida tämän vaihtoehdon ja saada automatisoidun palvelun, joka avaa kanavia parhaiden solmujen ja reittien kanssa käytettävissä olevan saldon perusteella Blixt-sovelluksen on-chain-lompakossa. Tämä on hyödyllinen ominaisuus uusille käyttäjille, jotka eivät ole varmoja, minkä solmun kanssa avata kanava ja/tai miten avata LN-kanava. Se on kuin autopilotti LN:lle.

> Muista: tämä vaihtoehto käytetään vain kerran, kun luot uuden Blixt-lompakkosi, ja se on oletusarvoisesti käytössä. Joten jos uusi käyttäjä skannaa on-chain QR-koodin päävalikosta ja tallettaa ensimmäiset satoshinsa siihen osoitteeseen, Blixt avaa automaattisesti kanavan näillä satosheilla, Blixtin julkisen solmun kanssa.

## Saapuvan Likviditeetin Palvelut

Ominaisuus on omistettu kauppiaille, jotka tarvitsevat enemmän SAAPUVAA likviditeettiä, helppokäyttöinen. Tätä varten valitse vain yksi likviditeetin tarjoajista listalta, maksa haluamasi summa kanavasta ja anna solmu-ID:si, ja siitä lähtien kanava avataan Blixt-solmullesi.

## Yhteystietolistat

Hyödyllinen ominaisuus, jos haluat kestävän listan vastaanottajista, joiden kanssa käyt kauppaa useimmiten. Tämä lista voi koostua LNURL-osoitteista, Lightning-osoitteista tai tulevaisuudessa staattisesta maksutiedosta/laskuista. Toistaiseksi tätä listaa ei voi tallentaa sovelluksen ulkopuolelle, mutta suunnitelmissa on mahdollisuus viedä se.

## LNURL ja Lightning-osoite

Täysi LNURL-tuki. Voit maksaa LNURL:lle, LN-authille, LN-chan pyynnölle LNURL:n kautta.
Voit lähettää mihin tahansa LN-osoitteeseen ja lisätä sen myös yhteystietoihisi.
Alkaen versiosta 0.6.9 on mahdollista vastaanottaa omaan LN-osoitteeseesi *@blixtwallet.com* tyyppi, [Blixt Lightning Box](https://github.com/hsjoberg/lightning-box) -ominaisuuden kautta.

## Keysend

Erittäin tehokas ominaisuus, joka on harvoilla mobiililompakoilla. Voit lähettää/varoja suoraan kanavan kautta tai osoittaa toiseen solmuun, tarvittaessa lisätä viestin. Se on kuin salainen chat LN:n yli. Tämä ominaisuus on erittäin hyödyllinen viestien näyttämiseen Amboss.space-mainostaululla ([tässä on opas tähän Amboss-mainostauluun](https://darthcoin.substack.com/p/amboss-billboard-amazing-tool)).

## Viestin Allekirjoitus
Erittäin hyödyllinen työkalu viestien allekirjoittamiseen Blixt-solmusi yksityisellä avaimella, autentikointiviesteihin ja niin edelleen. Hyvin harvoissa mobiililompakoissa on tämä ominaisuus, melkein ei missään.
## Monikanavamaksut - Monipolku Maksut (MPP)

Hyödyllinen ominaisuus LN-maksuille, joka mahdollistaa LN-maksun jakamisen useisiin osiin, useiden kanavien kautta. Se on hyvä tapa tasapainottaa likviditeettiä verkossa ja parantaa yksityisyyttä.

## Lightning-selain

Sarja kolmannen osapuolen palveluita LN:n kanssa, järjestetty yksinkertaisen, saavutettavan ja käyttäjäystävällisen selaimen sisällä. Se on myös hyvä tapa edistää yrityksiä, jotka hyväksyvät BTC:tä LN:ssä. Tämä on ominaisuus, jota kehitetään tulevaisuudessa lisää. Toistaiseksi se ei toimi Torin takana, joten näiden sovellusten selaaminen tapahtuu avoimesti (clearnetissä).

## Lokitutkijat

Tämä on tehokas työkalu LND-lokien tarkistamiseen ja solmusi tilan yleiseen tarkasteluun. On mahdollisuus tallentaa lokitiedosto. On erittäin hyödyllistä pitää nämä lokit käsillä, jos tarvitset kehittäjän apua tiettyjen ongelmien tunnistamisessa.

## Turvallisuus

Voit asettaa sovelluksen asetuksissa suuremman lompakkosi/solmusi turvallisuuden mahdollisuuden käynnistää sovellus PIN-koodilla ja/tai sormenjäljellä.

## Ketjussa toimiva lompakko

Tämä ominaisuus on hieman piilotettu, ylävasemmalla olevassa vetolaatikkovalikossa. Koska LN-käyttäjä ei usein käytä sitä, se ei ole näkyvissä pääruudulla. Mutta se on ok, voit pitää sen erillisessä lompakossa, jossa voit hallita osoitteita ja tarkastella tapahtumalokia, tuomalla siemenesi esimerkiksi Sparrow'ssa. Ehkä tulevaisuudessa Blixt-lompakko sisältää myös ominaisuuden UTxOjen hallintaan. Mutta toistaiseksi, KÄYTÄ tätä ketjussa toimivaa lompakkoa VAIN kanavien avaamiseen tai sulkemiseen LN:ssä.

## Erityisominaisuudet

- Versiossa 0.6.9 esiteltiin "pysyvä tila", joka mahdollistaa käyttäjän ajaa Blixtiä aina online LN-solmuna, pitäen LND-palvelut aktiivisina ja LN-lompakon valmiina vastaanottamaan/lähettämään milloin tahansa.
- Yksinkertaiset Taproot-kanavat - mahdollistavat Taproot-kanavien avaamisen lisäämään yksityisyyttä ja edistyneitä ominaisuuksia
- Nolla-vahvistuskanavat Blixt Dunder LSP:n kanssa
- Speedloader ("LN-kanavien synkronointi") - Tämä tarkoittaa, että kaikki kanavat synkronoidaan nopeasti käynnistyksen yhteydessä, paremman reitityksen vuoksi. Vaikka alun synkronointinäytön näkeminen on hieman ärsyttävää, se varmistaa, että lompakko tietää kaikista kanavista ja maksut ovat nopeampia ja luotettavampia.
- Käännetty 25+ kielelle!

## "Pääsiäismunat"

Kyllä, Blixt-sovelluksessa on joitakin piilotettuja ominaisuuksia, pieniä asioita, jotka tekevät sovelluksesta viehättävän, aktivoimalla hauskoja/mielenkiintoisia toimintoja ja vastauksia.
Vihje: kokeile klikata kahdesti Blixt-logoa vetolaatikossa 🙂 Annan sinun löytää loput.

# Blixtin Aloittaminen Askel Askeleelta -Opas

> Uutena LN-käyttäjänä, jos aloitat Blixt LN -solmun käytön, sinun on ensin tiedettävä, mikä on Lightning Network ja miten se toimii, ainakin perustasolla. [Tässä olemme koonneet yksinkertaisen luettelon resursseista Lightning Networkista](https://blixtwallet.github.io/faq#what-is-ln). Ole hyvä ja lue ne ensin.”

Täyden LN-solmun pyörittäminen mobiililaitteella ei ole helppo tehtävä ja se voi vaatia tilaa (min 600MB) ja muistia. Suosittelemme, että sinulla on hyvä mobiililaite, päivitetty ja käytössä vähintään Android 11 käyttöjärjestelmänä.

Kun avaat Blixtin, "Tervetuloa" -näyttö tarjoaa sinulle joitakin vaihtoehtoja:

![Demo Blixt 01](assets/blixt_t01.webp)
Oikeassa yläkulmassa näet kolme pistettä, jotka aktivoivat valikon, jossa on:
- "enable Tor" - käyttäjä voi aloittaa Tor-verkon käytön, erityisesti jos haluaa palauttaa vanhan LND-noden, joka toimi vain Tor-peereiden kanssa.

- "Set Bitcoin node" - jos käyttäjä haluaa yhdistää suoraan omaan nodeensa, synkronoidakseen lohkot Neutrinon kautta, voi tehdä sen suoraan tervetulonäytöltä. Tämä vaihtoehto on myös hyvä, jos internet-yhteytesi tai Tor ei ole niin vakaa yhdistääksesi oletus Bitcoin nodeen (node.blixtwallet.com).

## Ensimmäinen vaihe - Luo uusi lompakko

Jos valitset "luo uusi lompakko", sinut ohjataan suoraan Blixt Walletin päänäyttöön.

Tämä on "ohjaamosi" ja myös "Pää LN Lompakko", joten ole tietoinen, se näyttää vain LN-lompakkosi saldon. Onchain-lompakko näytetään erikseen (katso C).

![Demo Blixt 02](assets/blixt_t02.webp)

A - Blixtin lohkojen synkronointi-indikaattori. Tämä on tärkein asia LN-nodelle: olla synkronoitu verkon kanssa. Jos tuo kuvake on vielä siinä työskentelemässä, tarkoittaa, että nodesi EI OLE VALMIS! Joten ole kärsivällinen, erityisesti ensimmäisen alkusynkronoinnin aikana. Se voi kestää jopa 6-8 min, riippuen laitteestasi ja internet-yhteydestäsi.

Voit klikata sitä ja nähdä synkronoinnin tilan:

![Demo Blixt 03](assets/blixt_t03.webp)

Voit myös klikata "Show LND Log" (A) -painiketta, jos haluat nähdä ja lukea lisää teknisiä yksityiskohtia LND-lokista reaaliajassa. Se on hyödyllistä debuggauksessa ja oppiaksesi lisää siitä, miten LN toimii.

B - Täältä voit päästä kaikkiin Blixtin asetuksiin, ja niitä on paljon! Blixt tarjoaa monia rikkaita ominaisuuksia ja vaihtoehtoja hallita LN-nodeasi kuin ammattilainen. Kaikki nämä vaihtoehdot on selitetty yksityiskohtaisesti [“Blixt Features Page - Options Menu”](https://blixtwallet.github.io/features#blixt-options) -sivulla.

C - Täällä sinulla on "Magic Drawer" -valikko, joka on myös selitetty yksityiskohtaisesti täällä. Tässä on "Onchain Wallet" (B), Lightning Channels (C), Yhteystiedot, Kanavien tila -kuvake (A), Keysend (D).

![Demo Blixt 04](assets/blixt_t04.webp)

D - On apuvalikko, jossa on linkkejä FAQ / Oppaat -sivulle, yhteydenotto kehittäjään, Github-sivulle ja Telegram-tukiryhmään.

E - Näyttää ensimmäisen BTC-osoitteesi, johon voit tallettaa ensimmäiset testisatsisi. TÄMÄ ON VAPAAEHTOISTA! Jos talletat suoraan tuohon osoitteeseen, se avaa LN-kanavan Blixt Nodeen päin. Tämä tarkoittaa, että näet tallettamasi satsit siirtyvän toiseen onchain-siirtoon (tx), avatakseen tuon LN-kanavan. Voit tarkistaa sen Blixtin onchain-lompakosta (katso kohta C), klikkaamalla oikeassa yläkulmassa olevaa TX-valikkoa.

![Demo Blixt 05](assets/blixt_t05.webp)

Kuten voit nähdä Onchain Transaction Logissa, vaiheet on selitetty hyvin yksityiskohtaisesti osoittaen, minne satsit menevät (talletus, avaa, sulje kanava)

> SUOSITUS: Testattuamme useita tilanteita, tulimme siihen tulokseen, että on paljon tehokkaampaa avata kanavia 1 ja 5 M satsin välillä. Pienemmät kanavat tyhjenevät nopeasti ja maksavat suhteellisesti suuremman %:n palkkioita verrattuna suurempiin kanaviin.
F - Ilmoita pääasiallinen Lightning-lompakkosi saldo. Tämä EI ole koko Blixt-lompakkosi saldo, vaan se edustaa vain Lightning-kanavissa olevia satosheja, jotka ovat lähetettävissä. Kuten aiemmin mainittiin, Onchain-lompakko on erillinen. Pidä tämä seikka mielessä. Onchain-lompakko on erillinen tärkeästä syystä: sitä käytetään pääasiassa LN-kanavien avaamiseen/sulkemiseen.
No niin, nyt olet tallettanut joitakin satosheja siihen onchain-osoitteeseen, joka näkyy pääruudulla. On suositeltavaa, että tehdessäsi näin, pidät Blixt-sovelluksesi verkossa ja aktiivisena hetken aikaa, kunnes BTC-siirto otetaan louhijoiden toimesta ensimmäiseen lohkoon.

Tämän jälkeen voi kestää 20-30 minuuttia, kunnes se on täysin vahvistettu ja kanava on avoinna, ja näet sen Magic Drawer - Lightning Channels -osiossa aktiivisena. Myös laatikon yläosassa oleva pieni värillinen piste, jos se on vihreä, osoittaa, että LN-kanavasi on verkossa ja valmis lähettämään satosheja LN:n yli.

Osoite ja tervetuloviesti katoavat. Automaattisen kanavan avaaminen ei ole enää tarpeen. Voit myös poistaa tämän vaihtoehdon käytöstä Asetukset-valikosta.

On aika siirtyä eteenpäin, testata muita ominaisuuksia ja vaihtoehtoja LN-kanavien avaamiseen.

Nyt, avataan toinen kanava toisen solmupisteen kanssa. Blixt-yhteisö on koonnut [listan hyvistä solmupisteistä, joita käyttää Blixtin kanssa.](https://github.com/hsjoberg/blixt-wallet/issues/1033)

### Menettely tavallisen julkaisemattoman (yksityisen) LN-kanavan avaamiseen Blixt-mobiilisolmussasi

Tämä on hyvin yksinkertaista, vain muutama askel ja hieman kärsivällisyyttä:
- Mene [Blixt-yhteisön listaan](https://github.com/hsjoberg/blixt-wallet/issues/1033) hyvistä solmupisteistä
- Valitse solmupiste ja klikkaa sen nimen otsikkolinkkiä, se avaa sen Amboss-sivun
- Klikkaa näyttääksesi QR-koodin solmupisteen URI-osoitteelle

![Demo Blixt 06](assets/blixt_t06.webp)

Nyt, avaa Blixt ja mene ylälaatikkoon - Lightning Channels ja klikkaa “+” nappia

![Demo Blixt 07](assets/blixt_t07.webp)

Nyt, klikkaa (A) kameraa skannataksesi QR-koodin Amboss-sivulta ja solmupisteen tiedot täyttyvät. Lisää kanavalle haluamasi satoshien määrä ja valitse sitten siirtomaksun hinta. Voit jättää sen automaattiseksi (B) nopeampaa vahvistusta varten tai säätää sitä manuaalisesti liu'uttamalla nappia. Voit myös pitkään painaa numeroa ja muokata sitä mielesi mukaan.

Älä laita alle 1 sat/vbyte! Yleensä on parempi [konsultoida mempool-maksuja](https://mempool.space/) ennen kanavan avaamista ja valita sopiva maksu.

Valmista, nyt vain klikkaa nappia “avaa kanava” ja odota 3 vahvistusta, mikä yleensä kestää 30 min (noin 1 lohko joka 10min).

Kun se on vahvistettu, näet kanavan aktiivisena osiossasi “Lightning Channels”.

## Toinen vaihe - Hanki lisää sisääntulevaa likviditeettiä

Ok, nyt meillä on LN-kanava, jossa on vain ULOSPÄIN suuntautuvaa likviditeettiä. Se tarkoittaa, että voimme vain LÄHETTÄÄ, emme vielä voi VASTAANOTTAA satosheja LN:n yli. Miksi? Luitko alussa mainitut oppaat? Et? Palaa takaisin ja lue ne. On erittäin tärkeää ymmärtää, miten LN-kanavat toimivat.

![Demo Blixt 08](assets/blixt_t08.webp)
Kuten tässä esimerkissä näet, kanava avataan ensimmäisellä talletuksella, eikä sillä ole paljoa SISÄÄNTULEVAA likviditeettiä ("Voi vastaanottaa"), mutta ulospäin likviditeettiä ("Voi lähettää") on paljon.
Mitä vaihtoehtoja sinulla on, jos haluat vastaanottaa enemmän satosheja LN:n yli?
- Kuluta joitakin satosheja olemassa olevasta kanavasta. Kyllä, LN on Bitcoinin maksuverkko, jota käytetään pääasiassa satoshiesi kuluttamiseen nopeammin, halvemmin, yksityisemmin ja helpommin. LN EI ole hodlaamisen tapa, siihen sinulla on onchain-lompakko.
- Vaihda joitakin satosheja takaisin onchain-lompakkoosi käyttämällä sukellusvenevaihtopalvelua. Tällä tavalla et kuluta satoshejasi, vaan siirrät ne takaisin omaan onchain-lompakkoosi. Tässä voit nähdä yksityiskohtaisesti joitakin menetelmiä [Blixt Guides -sivulla](https://blixtwallet.github.io/guides).
- Avaa SISÄÄNTULEVA kanava mistä tahansa LSP-tarjoajalta. Tässä on videodemo siitä, [miten käyttää LNBig LSP:tä sisääntulevan kanavan avaamiseen](https://blixtwallet.github.io/assets/images/blixt-lnbig.mp4). Tämä tarkoittaa, että maksat pienen maksun TYHJÄSTÄ kanavasta (omalla puolellasi) ja pystyt vastaanottamaan enemmän satosheja kyseiseen kanavaan. Jos olet kauppias, joka vastaanottaa enemmän kuin kuluttaa, tämä on hyvä vaihtoehto. Samoin, jos ostat satosheja LN:n yli käyttäen Robosatseja tai jotain muuta LN-vaihtoa.
- Avaa Dunder-kanava, Blixt-solmun tai minkä tahansa muun Dunder LSP -tarjoajan kanssa. Dunder-kanava on yksinkertainen tapa saada jonkin verran SISÄÄNTULEVAA likviditeettiä, mutta samalla talletat joitakin satosheja kyseiseen kanavaan. Se on myös hyvä, koska se avaa kanavan [UTXO](https://en.bitcoin.it/wiki/UTXO):lla, joka ei ole peräisin Blixt-lompakostasi. Tämä lisää yksityisyyttä.
Se on myös hyvä, koska jos sinulla ei ole satosheja onchain-lompakossa normaalin LN-kanavan avaamiseksi, mutta sinulla on niitä toisessa LN-lompakossa, voit maksaa toisesta lompakosta LN:n kautta kyseisen Dunder-kanavan avaamisen ja talletuksen (omalla puolellasi). [Lisätietoja siitä, miten Dunder toimii ja miten voit pystyttää oman palvelimesi täällä.](https://github.com/hsjoberg/dunder-lsp)

![Demo Blixt 09](assets/blixt_t09.webp)

Tässä ovat vaiheet Dunder-kanavan avaamisen aktivoimiseksi:
- Siirry Asetuksiin, "Kokeilut"-osiossa aktivoi ruutu "Enable Dunder LSP".
- Kun olet tehnyt sen, palaa takaisin "Lightning Network" -osioon ja näet, että ilmestyi vaihtoehto "Set Dunder LSP Server". Oletuksena on asetettu "https://dunder.blixtwallet.com", mutta voit vaihtaa sen minkä tahansa muun Dunder LSP -tarjoajan osoitteeseen. [Tässä on Blixt-yhteisön lista](https://github.com/hsjoberg/blixt-wallet/issues/1033) solmuista, jotka voivat tarjota Dudner LSP -kanavia Blixtiisi.
- Nyt voit mennä päävalikkoon ja klikata "Vastaanota"-painiketta. Sitten seuraa tätä menettelyä, joka on selitetty [tässä oppaassa](https://blixtwallet.github.io/guides#guide-lsp).

OK, joten kun Dunder-kanava on vahvistettu (kestää muutaman minuutin), sinulla on lopulta 2 LN-kanavaa: yksi alun perin autopilotilla avattu (kanava A) ja toinen enemmän sisääntulevalla likviditeetillä, avattu Dunderin kautta (kanava B).
![Demo Blixt 10](assets/blixt_t10.webp)
Hyvä, nyt olet valmis lähettämään ja vastaanottamaan tarpeeksi satosheja LN:n yli!

## Kolmas vaihe - Solmun palautusprosessi

Keskustellaanpa nyt siitä, miten Blixt-lompakko tai mikä tahansa muu kaatunut LND-solmu palautetaan. Tämä on hieman teknisempi aihe, mutta kiinnitäthän huomiota. Se ei ole niin vaikeaa.

> MUISTUTUS: Aiemmin kirjoitin omistetun oppaan useilla vaihtoehdoilla [kuinka palauttaa kaatunut LND-solmu](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario), jossa mainitsin myös menetelmän käyttää Blixtiä nopeana palautusprosessina, käyttäen siementä + channel.backup-tiedostoa kuolleesta LND-solmustasi. Kirjoitin myös oppaan, kuinka palauttaa Blixt-solmusi tai siirtää Blixtisi toiselle laitteelle, [täällä](https://blixtwallet.github.io/faq#blixt-restore).

![Demo Blixt 11](assets/blixt_t11.webp)

Mutta selitetään tämä prosessi yksinkertaisin askelin. Kuten yllä olevasta kuvasta näet, on kaksi asiaa, jotka sinun tulee tehdä palauttaaksesi aiemman Blixt/LND-solmusi:
- ylälaatikko, johon sinun tulee täyttää kaikki 24 sanaa siemenestäsi (vanha / kuollut solmu)
- alhaalla on kaksi painikkeen vaihtoehtoa channel.backup-tiedoston lisäämiseen / lataamiseen, joka on aiemmin tallennettu vanhasta Blixt/LND-solmustasi. Se voi olla paikallisesta tiedostosta (olet ladannut sen laitteeseesi aiemmin) tai se voi olla Google Drive / iCloud etäpaikasta. Blixtillä on tämä vaihtoehto tallentaa kanaviesi varmuuskopio suoraan Google / iCloud-asemaan. Katso lisätietoja [Blixtin ominaisuussivulta](https://blixtwallet.github.io/features#blixt-options).

Mainittakoon, jos sinulla ei aiemmin ollut avoimia LN-kanavia, ei ole tarvetta ladata mitään channels.backup-tiedostoa. Syötä vain 24 sanan siemen ja paina palautuspainiketta.

Älä unohda aktivoida Toria ylävalikon kolmesta pisteestä, kuten selitimme oppaan "Ensimmäinen vaihe" -luvussa. Tämä on tapaus, kun sinulla oli VAIN Tor-peerejä eikä yhteyttä voitu ottaa clearnetin kautta (domain/IP). Muussa tapauksessa se ei ole tarpeen.

Toinen hyödyllinen ominaisuus on asettaa tietty Bitcoin-solmu ylävalikosta. Oletuksena se synkronoi lohkoja node.blixtwallet.comista (neutrino-tila), mutta voit asettaa minkä tahansa muun Bitcoin-solmun, joka tarjoaa neutrino-synkronoinnin.

Kun olet täyttänyt nuo vaihtoehdot ja painanut palautuspainiketta, Blixt alkaa ensin synkronoida lohkoja Neutrinon kautta, kuten selitimme oppaan "Ensimmäinen vaihe" -luvussa. Ole siis kärsivällinen ja seuraa palautusprosessia päänäytöllä napsauttamalla synkronointikuvaketta.

![Demo Blixt 12](assets/blixt_t12.webp)

Kuten tässä esimerkissä näet, se näyttää, että bitcoin-lohkot ovat 100% synkronoituja (A) ja palautusprosessi on käynnissä (B). Tämä tarkoittaa, että aiemmin omistamasi LN-kanavat suljetaan ja varat palautetaan Blixtin onchain-lompakkoosi.

Tämä prosessi vie aikaa! Ole siis kärsivällinen ja yritä pitää Blixtisi aktiivisena ja verkossa. Alkuperäinen synkronointi voi kestää jopa 6-8 minuuttia ja kanavien sulkeminen voi kestää jopa 10-15 minuuttia. Joten varmista, että laitteen akku on hyvin ladattu.
Kun tämä prosessi on käynnistetty, voit tarkistaa Magic Drawer - Lightning Channels -osiosta kunkin aiemman kanavasi tilan, joka näyttää olevan "odottaa sulkemista" -tilassa. Kun jokainen kanava on suljettu, voit nähdä sulkemistransaktion onchain-lompakossa (katso Magic Drawer - Onchain) ja avata tx-lokin.

![Demo Blixt 13](assets/blixt_t13.webp)

On myös hyvä tarkistaa ja lisätä, jos ne puuttuvat, aiemmat vertaisverkkosi, jotka sinulla oli vanhassa LN-nodessasi. Mene siis Asetukset-valikkoon, alaosaan "Lightning Network" ja valitse vaihtoehto "Näytä Lightning-vertaisverkot".

![Demo Blixt 14](assets/blixt_t14.webp)

Tässä osiossa näet sillä hetkellä yhdistetyt vertaisverkkosi ja voit lisätä lisää, on parempi lisätä ne, joilla oli kanavia aiemmin. Mene vain Amboss-sivulle, etsi vertaisnodojesi aliakset tai nodeID ja skannaa heidän noden URI-osoitteensa.

![Demo Blixt 15](assets/blixt_t15.webp)

Kuten yllä olevasta kuvasta näet, on kolme näkökohtaa:

A - edustaa clearnet-noden osoitteen URI:a (domain/IP)

B - edustaa Tor onion -noden osoitteen URI:a (.onion)

C - on QR-koodi, jonka voit skannata Blixt-kamerallasi tai kopionappi.

Tämän noden osoitteen URI:n sinun täytyy lisätä vertaisverkkoluetteloosi. Joten ole tietoinen siitä, että pelkkä noden aliaksnimi tai nodeID ei riitä.

Nyt voit mennä Magic Draweriin (ylävasen valikko) - Lightning Channels, ja näet, missä lohkokorkeudessa varat palautetaan onchain-osoitteeseesi.

![Demo Blixt 16](assets/blixt_t16.webp)

Tuo lohkonumero 764272 on, kun varat ovat käytettävissä bitcoin onchain -osoitteessasi. Ja vapautuminen voi kestää jopa 144 lohkoa ensimmäisestä vahvistuslohkosta. Joten tarkista se [mempoolista](https://mempool.space/).

Ja siinä kaikki. Odota kärsivällisesti, kunnes kaikki kanavat on suljettu ja varat palautettu onchain-lompakkoosi.

## Neljäs vaihe - Mukauttaminen

Tämä luku käsittelee mukauttamista ja Blixt-nodisi parempaa tuntemista. En kuvaile kaikkia saatavilla olevia ominaisuuksia, niitä on liian monta ja ne on jo selitetty [Blixtin ominaisuussivulla](https://blixtwallet.github.io/features).

Mutta osoitan joitakin niistä, jotka ovat tarpeellisia Blixtin käytön jatkamiseksi ja mahtavan kokemuksen saamiseksi.

### A - Nimi (NameDesc)

![Demo Blixt 17](assets/blixt_t17.webp)

[NameDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) on standardi "vastaanottajan nimen" välittämiseen BOLT11-laskuissa.

Tämä voi olla mikä tahansa nimi ja sitä voidaan muuttaa milloin tahansa.

Tämä vaihtoehto on todella hyödyllinen eri tapauksissa, kun haluat lähettää nimen yhdessä laskun kuvauksen kanssa, jotta vastaanottaja saisi vihjeen keneltä sai nuo satoshit. Tämä on täysin vapaaehtoinen ja myös maksunäytössä käyttäjän on rastitettava ruutu osoittaakseen, että haluaa lähettää aliaksnimen.

Tässä on esimerkki siitä, miltä näyttää, kun käytät [chat.blixtwallet.com](https://chat.blixtwallet.com/)

![Demo Blixt 18](assets/blixt_t18.webp)

Tässä on toinen esimerkki lähettäessä toiseen lompakko-sovellukseen, joka tukee NameDesciä:

![Demo Blixt 19](assets/blixt_t19.webp)

### B - Varmuuskopioi LN-kanavat ja siemen sanat

Tämä on erittäin tärkeä ominaisuus!
LN-kanavan avaamisen tai sulkemisen jälkeen sinun tulisi tehdä varmuuskopio. Sen voi tehdä manuaalisesti tallentamalla pienen tiedoston paikalliselle laitteelle (yleensä latauskansioon) tai käyttämällä Google Drivea tai iCloud-tiliä.
![Demo Blixt 20](assets/blixt_t20.webp)

Siirry Blixtin asetuksiin - Lompakko-osioon. Siellä sinulla on vaihtoehdot tallentaa kaikki tärkeät tiedot Blixt-lompakollesi:
- “Näytä mnemonic” - näyttää 24 sanan siemenen, jotta voit kirjoittaa ne ylös
- “Poista mnemonic laitteesta” - tämä on valinnainen ja käytä sitä vain, jos todella haluat poistaa siemensanat laitteestasi. Tämä EI poista lompakkoasi, vain siemenen. Mutta ole varovainen! Niitä ei voi palauttaa, jos et ole kirjoittanut niitä ensin ylös.
- “Vie kanavavarmuuskopio” - tämä vaihtoehto tallentaa pienen tiedoston paikalliselle laitteellesi, yleensä “lataukset”-kansioon, josta voit ottaa sen ja siirtää sen laitteesi ulkopuolelle turvaan.
- “Vahvista kanavavarmuuskopio” - tämä on hyvä vaihtoehto, jos käytät Google Drivea tai iCloudia varmuuskopion eheyden tarkistamiseen etänä.
- “Google Drive -kanavavarmuuskopio” - tallentaa varmuuskopiotiedoston henkilökohtaiseen Google Driveesi. Tiedosto on salattu ja se säilytetään erillisessä repositoriossa kuin tavalliset Google-tiedostosi. Joten ei ole huolta, että kukaan voisi lukea sitä. Joka tapauksessa kyseinen tiedosto on täysin hyödytön ilman siemensanoja, joten kukaan ei voi ottaa varojasi pelkästään sillä tiedostolla.

Tälle osiolle suosittelisin seuraavaa:
- käytä salasananhallintasovellusta siemenesi ja varmuuskopiotiedoston turvalliseen säilyttämiseen. [KeePass](https://keepass.info/) tai Bitwarden ovat erittäin hyviä tähän ja niitä voidaan käyttää monialustaisesti sekä itse isännöitynä tai offline-tilassa.
- TEE VARMUUSKOPIO JOKA KERTA, kun avaat tai suljet kanavan. Tiedosto päivittyy kanavien tiedoilla. Sinun ei tarvitse tehdä sitä jokaisen LN:ssä suorittamasi transaktion jälkeen. Kanavavarmuuskopio ei tallenna sitä tietoa, vaan ainoastaan kanavan tilan.

![Demo Blixt 21](assets/blixt_t21.webp)

## Yhteenveto

OK, Blixt tarjoaa monia muita uskomattomia ominaisuuksia, annan sinun löytää ne itse ja pitää hauskaa.

Tätä sovellusta aliarvioidaan todella paljon, pääasiassa siksi, että sitä ei tue mikään VC-rahoitus, se on yhteisövetoinen, rakennettu rakkaudella ja intohimolla Bitcoinia ja Lightning Networkia kohtaan.

Tämä mobiili LN-solmu, Blixt, on erittäin tehokas työkalu monien käyttäjien käsissä, jos he osaavat käyttää sitä hyvin. Kuvittele vain, että kävelet ympäri maailmaa LN-solmun kanssa omassa taskussasi eikä kukaan tiedä siitä.

Puhumattakaan kaikista muista rikkaista ominaisuuksista, joita mukana tulee, joita hyvin harvat tai ei yksikään muu lompakko-sovellus tarjoa.

Toivon, että nautit sen käytöstä. Henkilökohtaisesti rakastan sitä ja se on minulle erittäin hyödyllinen (katso tässä käyttötapaus, jossa tämä lompakko on loistava työkalu).

HYVÄÄ BITCOIN LIGHTNINGIA!

Olkoon ₿ITCOIN kanssasi!

> VASTUUVAPAUSLAUSEKE: En saa maksua tai tukea millään tavalla tämän sovelluksen kehittäjiltä. Kirjoitin tämän oppaan, koska huomasin, että kiinnostus tähän lompakko-sovellukseen on kasvussa ja uudet käyttäjät eivät vielä ymmärrä, miten aloittaa sen käytön. Myös auttaakseni Hampusta (pääkehittäjä) dokumentaation kanssa tämän solmulompakon käytöstä. Minulla ei ole mitään muuta intressiä edistää tätä LN-sovellusta, kuin edistää Bitcoinin ja LN:n omaksumista. Tämä on ainoa tapa!