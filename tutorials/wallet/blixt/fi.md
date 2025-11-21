---
name: Blixt Wallet
description: Miten aloittaa tehokkaan LN-solmun käyttö matkapuhelimessa?
---
![cover](assets/cover.webp)


Tämä opas on omistettu kaikille niille uusille käyttäjille, jotka haluavat aloittaa Bitcoin Lightning Network:n (LN) käytön ILMAISENA AVOIMENA LÄHDEOHJELMANA, TÄYDELLISESTI EI-PAKOLLISESTI.


Käyttämällä [Blixt Wallet](https://blixtwallet.com/), täysi LN-solmu matkapuhelimessasi, missä ikinä oletkin.


Jos et ole koskaan käyttänyt Bitcoin Lightning Network:ää, ennen kuin aloitat, [lue tämä yksinkertainen selitysanalogia Lightning Network:stä (LN)](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## TÄRKEITÄ NÄKÖKOHTIA:



- Blixt on yksityinen solmu, EI reitityssolmu! Pidä tämä mielessä: Tämä tarkoittaa, että kaikki Blixtin LN-kanavat ovat LN-graafissa ilmoittamattomia (ns. yksityisiä kanavia). Tämä tarkoittaa, että tämä solmu ei reititä muita maksuja Blixt-solmun kautta. Tämä Blixt-solmu EI ole tarkoitettu reititykseen, toistan. Sen tarkoituksena on lähinnä hallita omia LN-kanavia ja suorittaa LN-maksut yksityisesti aina tarvittaessa. Tämän Blixt-solmun on oltava verkossa ja synkronoitu VAIN ENNEN kuin aiot tehdä maksutapahtumia. Siksi näet ylhäällä kuvakkeen, joka osoittaa synkronoinnin tilan. Se kestää vain muutaman hetken, riippuen siitä, kuinka kauan olet pitänyt sitä offline-tilassa.



- Blixt käyttää LND:tä (aezeed) Wallet:n taustajärjestelmänä, joten älä yritä tuoda siihen muunlaisia Bitcoin-lompakoita. [Tässä olet selittänyt Wallet Mnemonic siementen tyypit](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Ja tässä on [laajempi luettelo kaikentyyppisistä lompakoista](https://walletsrecovery.org/). Joten jos sinulla oli aiemmin LND-solmu, voit tuoda seed- ja varmuuskopio.kanavat Blixtiin, [kuten tässä oppaassa on selitetty](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- Tämän oppaan lopussa on erityinen osio, jossa on ["vinkkejä ja temppuja"](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Blixt tärkeät linkit - katso ne tämän oppaan lopussa, merkitse ne kirjanmerkkeihin.


---

## Blixt - Ensimmäinen kontakti


Joten... Darthin äiti päätti alkaa käyttää LN:aa Blixtin kanssa. Hard päätös, mutta viisas. Blixt on vain fiksuille ihmisille ja niille, jotka todella haluavat oppia lisää, syvällisesti LN:n käyttöä.


![blixt](assets/en/01.webp)


Darth varoittaa äitiään:


"* Äiti, jos alat käyttää Blixt LN Nodea, sinun on ensin tiedettävä, mikä on Lightning Network ja miten se toimii, ainakin perustasolla." "Äiti, jos alat käyttää Blixt LN Nodea, sinun on ensin tiedettävä, mikä on Lightning Network ja miten se toimii, ainakin perustasolla. [Tähän olen koonnut yksinkertaisen luettelon Lightning Network:tä koskevista resursseista](https://blixtwallet.github.io/faq#what-is-LN). Lue ne ensin.*"


Darthin äiti luki resurssit ja teki ensimmäisen askeleen: asensi Blixtin upouuteen Android-laitteeseensa. Blixt on saatavilla myös iOS:lle ja macOS:lle (työpöytä). Mutta ne eivät ole Darthin äidille... On kuitenkin suositeltavaa käyttää uudempaa Android-versiota, vähintään 9 tai 10, jotta yhteensopivuus ja kokemus olisivat paremmat. Täydellisen LN-solmun ajaminen mobiililaitteella ei ole helppo tehtävä ja se voi viedä jonkin verran tilaa (min 600MB) ja muistia.


Kun avaat Blixtin, "Tervetuloa"-näyttö antaa sinulle joitakin vaihtoehtoja:


![blixt](assets/en/02.webp)


Oikeassa yläkulmassa näet 3 pistettä, jotka aktivoivat valikon:



- "enable Tor" - käyttäjä voi aloittaa Tor-verkon, erityisesti jos haluaa palauttaa vanhan LND-solmun, joka toimi vain Tor-vertaisten kanssa.
- "Aseta Bitcoin-solmu" - jos käyttäjä haluaa muodostaa yhteyden suoraan omaan solmuunsa ja synkronoida lohkot Neutrinon kautta, hän voi tehdä sen heti tervetuliaisnäytöltä. Tämä vaihtoehto on hyvä myös siinä tapauksessa, että Internet-yhteytesi tai Tor-yhteytesi ei ole niin vakaa, että se voisi muodostaa yhteyden oletusarvoiselle Bitcoin-solmulle (node.blixtwallet.com).
- Pian sinne lisätään kieli, joten käyttäjä voi aloittaa suoraan kielellä, joka on hänelle mukava. Jos haluat osallistua tähän avoimen lähdekoodin projektiin käännöksillä muille kielille, [liity tähän](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### Vaihtoehto A - Luo uusi Wallet


Jos valitset "luo uusi Wallet", sinut ohjataan suoraan Blixt Wallet:n päänäyttöön.


Tämä on sinun "ohjaamosi" ja myös "Main LN Wallet", joten ole tietoinen siitä, että se näyttää sinulle vain LN Wallet:n tasapainon. Ketjussa oleva Wallet näytetään erikseen (ks. C).


![blixt](assets/en/03.webp)


A - Blixt-lohkojen synkronoinnin merkkikuvake. Tämä on LN-solmun tärkein asia: synkronointi verkon kanssa. Jos tämä kuvake on edelleen toiminnassa, se tarkoittaa, että solmusi EI OLE VALMIS! Joten ole kärsivällinen, erityisesti ensimmäisen synkronoinnin aikana. Se voi kestää jopa 6-8 minuuttia laitteestasi ja internetyhteydestäsi riippuen.


Voit napsauttaa sitä ja nähdä synkronoinnin tilan:


![blixt](assets/en/04.webp)


Voit myös napsauttaa "Näytä LND-loki" (A) -painiketta, jos haluat nähdä ja lukea lisää teknisiä yksityiskohtia LND-lokista reaaliajassa. Tämä on erittäin hyödyllistä LN:n virheenkorjauksessa ja LN:n toimintatapojen oppimisessa.


B - Täällä voit käyttää kaikkia Blixt Asetukset, ja ovat paljon! Blixt tarjoaa monia monipuolisia ominaisuuksia ja vaihtoehtoja, joilla voit hallita LN-solmua kuin ammattilainen. Kaikki nämä vaihtoehdot selitetään yksityiskohtaisesti kohdassa "[Blixt Features Page](https://blixtwallet.github.io/features#blixt-options) - Options Menu".


C - Tässä on "Magic Drawer" -valikko, [joka selitetään yksityiskohtaisesti myös täällä](https://blixtwallet.github.io/features#blixt-drawer). Tässä on "Onchain Wallet" (B), Lightning Channels (C), Contacts, Channels status icon (A), Keysend (D).


![blixt](assets/en/05.webp)


D - on ohjevalikko, jossa on linkit UKK/oppaat-sivulle, ota yhteyttä kehittäjään, Github-sivulle ja Telegram-tukiryhmään.


E - Ilmoita ensimmäinen BTC Address, johon voit tallettaa ensimmäisen testauksen Sats. TÄMÄ ON VAPAAEHTOISTA! Jos talletat suoraan tuohon Address:een, avataan LN-kanava kohti Blixt Nodea. Se tarkoittaa, että näet tallettamasi Sats:n, joka menee toiseen onchain-transaktioon (tx), tuon LN-kanavan avaamista varten. Voit tarkistaa sen Blixtin onchain Wallet:een (ks. kohta C) klikkaamalla oikean yläkulman TX-valikkoa.


![blixt](assets/en/06.webp)


Kuten näet Onchain Transaction Logista, vaiheet ovat hyvin yksityiskohtaisia ja osoittavat, minne Sats on menossa (talletus, avoin, suljettu kanava).


SUOSITUS:


Testattuamme useita tilanteita tulimme siihen tulokseen, että on paljon tehokkaampaa avata kanavia 1-5 M Sats:n välillä. Pienemmät kanavat tyhjenevät yleensä nopeasti ja maksavat suurempiin kanaviin verrattuna enemmän maksuja.


F - Ilmoita tärkein Lightning Wallet -saldosi. Tämä EI ole koko Blixt Wallet -saldosi, vaan ainoastaan se Sats, joka sinulla on Lightning-kanavissa lähetettävissä. Kuten aiemmin todettiin, Onchain Wallet on erillinen. Pidä tämä seikka mielessä. Onchain Wallet on erillinen tärkeästä syystä: sitä käytetään pääasiassa LN-kanavien avaamiseen/sulkemiseen.


Okei, nyt Darthin äiti on tallettanut Sats:tä siihen ketjussa olevaan Address:ään, joka näkyy päänäytöllä. On suositeltavaa, että kun teet tämän, pidät Blixt-sovelluksen verkossa ja aktiivisena jonkin aikaa, kunnes louhijat ottavat BTC-tx:n ensimmäiseen lohkoon.


Tämän jälkeen voi kestää jopa 20-30 minuuttia, kunnes kanava on täysin vahvistettu ja avattu, ja näet sen Magic Drawer - Lightning Channels -kohdassa aktiivisena. Myös pieni värillinen piste laatikon yläosassa, jos se on Green, osoittaa, että LN-kanavasi on verkossa ja valmis käytettäväksi Sats:n lähettämiseen LN:n kautta.


Address ja tervetuliaisviesti häviävät. Automaattikanavaa ei enää tarvitse avata. Voit myös poistaa vaihtoehdon käytöstä Asetukset-valikossa.


On aika siirtyä eteenpäin, testata muita ominaisuuksia ja vaihtoehtoja LN-kanavien avaamiseksi.


Avataan nyt toinen kanava toisen solmupisteen kanssa. Blixt-yhteisö on koonnut [luettelon hyvistä solmuista, joita kannattaa alkaa käyttää Blixtin kanssa](https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Menettely LN-kanavan avaamiseksi Blixtissä**


Tämä on hyvin yksinkertaista, vaatii vain muutamia vaiheita ja hieman kärsivällisyyttä:



- Pääsin [Blixt-yhteisön](https://github.com/hsjoberg/blixt-Wallet/issues/1033) vertaisluetteloon
- Valitse solmu ja napsauta sen nimen otsikkolinkkiä, jolloin sen Amboss-sivu avautuu
- Näytä solmun URI:n QR-koodi napsauttamalla sitä Address


![blixt](assets/en/07.webp)


Avaa Blixt ja siirry ylälaatikkoon - Salamakanavat ja napsauta "+" -painiketta


![blixt](assets/en/08.webp)


Nyt voit skannata QR-koodin Ambossin sivulta napsauttamalla kameraa (A), jolloin solmun tiedot täyttyvät. Lisää haluamasi kanavan Sats:n määrä ja valitse sitten tx:n maksuprosentti. Voit jättää sen automaattiseksi (B) nopeampaa vahvistusta varten tai säätää sitä manuaalisesti liu'uttamalla painiketta. Voit myös painaa numeroa pitkään ja muokata sitä haluamallasi tavalla.


Älä laita alle 1 sat/vbyte ! Yleensä on parempi katsoa [Mempool maksut](https://Mempool.space/) ennen kanavan avaamista ja valita sopiva maksu.


Valmis, nyt vain klikkaa painiketta "avaa kanava" ja odota 3 vahvistuksia, että yleensä kestää 30 min (1 lohko aprox jokainen 10min).


Kun se on vahvistettu, näet kanavan aktiivisena kohdassa "Salamakanavat".


---

## Blixt - Toinen kontakti


Nyt meillä on siis LN-kanava, jossa on vain OUTBOUND-likviditeetti. Se tarkoittaa, että voimme vain lähettää, mutta emme voi vastaanottaa Sats:ää LN:n kautta.


![blixt](assets/en/09.webp)


Miksi? Luitko alussa mainitut oppaat? Etkö? Palaa takaisin ja lue ne. On erittäin tärkeää ymmärtää, miten LN-kanavat toimivat.


![blixt](assets/en/10.webp)


Kuten voit nähdä tässä esimerkissä, kanavalla, joka on avattu ensimmäisellä talletuksella, ei ole liikaa INBOUND-likviditeettiä ("Voi vastaanottaa"), mutta sillä on paljon OUTBOUND-likviditeettiä ("Voi lähettää").


Mitä vaihtoehtoja sinulla on, jos haluat saada enemmän Sats:tä kuin LN:tä?



- Kuluta Sats olemassa olevasta kanavasta. Kyllä, LN on Bitcoin:n maksuverkko, jota käytetään pääasiassa Sats:n käyttämiseen nopeammin, halvemmalla, yksityisesti ja helposti. LN EI ole hodling-tapa, vaan sitä varten sinulla on ketjussa oleva Wallet.



- Vaihda Sats takaisin ketjussa olevaan Wallet:een käyttämällä sukellusveneen vaihtopalvelua. Tällä tavoin et tuhlaa Sats:ääsi, vaan annat sen takaisin omaan ketjussasi olevaan Wallet:een. Tässä näet yksityiskohtaisesti joitakin menetelmiä, [Blixt Guides Page](https://blixtwallet.github.io/guides).



- Avaa INBOUND-kanava mistä tahansa LSP-palveluntarjoajasta. Tässä on videodemo siitä, miten LNBig LSP:tä käytetään saapuvan kanavan avaamiseen. Tämä tarkoittaa, että maksat pienen maksun tyhjästä kanavasta (sinun puolellasi) ja voit vastaanottaa lisää Sats:ää kyseiseen kanavaan. Jos olet kauppias, joka vastaanottaa enemmän kuin käyttää, se on hyvä vaihtoehto. Myös jos ostat Sats:ää LN:n yli, käytät Robosatia tai mitä tahansa LN Exchange:aa.



- Avaa Dunder-kanava Blixt-solmulla tai muulla Dunder LSP-palveluntarjoajalla. Dunder-kanava on yksinkertainen tapa saada INBOUND-likviditeettiä, mutta samalla talletat Sats:a kyseiseen kanavaan. On myös hyvä, koska se avaa kanavan [UTXO](https://en.Bitcoin.it/wiki/UTXO), joka ei ole Blixtin Wallet:sta. Se lisää hieman yksityisyyttä. Se on hyvä myös siksi, että jos sinulla ei ole Sats:a onchain Wallet:ssa, jotta voit avata tavallisen LN-kanavan, mutta sinulla on niitä toisessa LN Wallet:ssa, voit vain maksaa tuosta toisesta Wallet:sta LN:n kautta tuon Dunder-kanavan avaamisen ja tallettamisen (omalta puoleltasi). [Lisätietoja siitä, miten Dunder toimii ja miten pyörität omaa palvelinta täällä](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Tässä ovat vaiheet Dunder-kanavan avaamisen aktivoimiseksi:



- Mene Asetuksiin, aktivoi kohdassa "Experiments" ruutu "Enable Dunder LSP".
- Kun olet tehnyt tämän, palaa takaisin "Lightning Network"-osioon ja näet, että näkyviin tuli vaihtoehto "Set Dunder LSP Server". Siellä on oletusarvoisesti asetettu "https://dunder.blixtwallet.com", mutta voit vaihtaa sen mihin tahansa muuhun Dunder LSP -palveluntarjoajaan Address. [Tässä on Blixt-yhteisöluettelo](https://github.com/hsjoberg/blixt-Wallet/issues/1033), jossa on solmuja, jotka voivat tarjota Dudner LSP -kanavia Blixtillesi.
- Nyt voit siirtyä päänäyttöön ja napsauttaa "Vastaanota" -painiketta. Seuraa sitten tätä menettelyä [selitetään tässä oppaassa](https://blixtwallet.github.io/guides#guide-lsp).


Kun Dunder-kanava on vahvistettu (kestää muutaman minuutin), sinulla on lopulta kaksi LN-kanavaa: toinen on avattu aluksi autopilotilla (kanava A) ja toinen, jossa on enemmän likviditeettiä ja joka on avattu Dunderilla (kanava B).


![blixt](assets/en/12.webp)


Hyvä, nyt olet valmis lähettämään ja vastaanottamaan riittävästi Sats:tä LN:n kautta !


ONNELLISTA Bitcoin SALAMOINTIA!


---

## Blixt - Kolmas kontakti


Muista, että luvussa yksi "Ensimmäinen kontakti" oli 2 vaihtoehtoa tervetuloruudussa:


- [Vaihtoehto A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Luo uusi Wallet
- Vaihtoehto B - Wallet:n palauttaminen


Keskustellaan nyt siitä, miten palauttaa Blixt Wallet:n tai minkä tahansa muun LND:n kaatuneen solmun. Tämä on hieman teknisempää, mutta ole hyvä ja kiinnitä huomiota. Ei ole, että Hard.


### Vaihtoehto B - Wallet:n palauttaminen


Aiemmin kirjoitin erillisen oppaan [miten palauttaa kaatunut Umbrel-solmu](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), jossa mainitsin myös menetelmän, jossa käytetään Blixtiä nopeana palautusprosessina, käyttäen seed + channel.backup-tiedostoa Umbrelista.


Kirjoitin myös oppaan siitä, miten palauttaa Blixt-solmusi tai siirtää Blixt toiselle laitteelle, [täällä](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Mutta selitetään tämä prosessi yksinkertaisin askelin. Kuten yllä olevasta kuvasta näkyy, sinun on tehtävä kaksi asiaa, jotta voit palauttaa edellisen Blixt/LND-solmun:



- ylimpään laatikkoon on täytettävä kaikki 24 sanaa seed:sta (vanha/kuollut solmu)
- alareunassa on kaksi painikevaihtoehtoa, joilla voit lisätä/ladata vanhasta Blixt/LND-solmusta aiemmin tallennetun channel.backup-tiedoston. Se voi olla paikallinen tiedosto (lataat sen laitteeseesi aiemmin) tai se voi olla Google drive / iCloud -etäsijainnista. Blixtillä on tämä mahdollisuus tallentaa kanaviesi varmuuskopio suoraan Google / iCloud-asemaan. Katso lisätietoja [Blixt Features Page](https://blixtwallet.github.io/features#blixt-options).


Mainittakoon kuitenkin, että jos sinulla ei aiemmin ollut yhtään avointa LN-kanavaa, sinun ei tarvitse ladata mitään channels.backup-tiedostoa. Aseta vain 24 sanaa seed ja paina palauta-painiketta.


Älä unohda aktivoida Toria 3 pisteen ylävalikosta, kuten selitimme kohdassa Vaihtoehto A. Tämä on tilanne silloin, kun sinulla oli VAIN Tor-vertaisverkkopalveluja, eikä sinuun voinut ottaa yhteyttä clearnetin kautta (verkkotunnus/IP). Muuten ei ole tarpeen.


Toinen hyödyllinen ominaisuus on tietyn Bitcoin-solmun asettaminen ylävalikosta. Oletusarvoisesti se synkronoi lohkot node.blixtwallet.com:sta (neutriinotila), mutta voit asettaa minkä tahansa muun Bitcoin-solmun, joka tarjoaa neutriinosynkronoinnin.


Kun olet täyttänyt nämä vaihtoehdot ja painanut palautuspainiketta, Blixt alkaa ensin synkronoida lohkoja Neutrinon kautta, kuten selitimme luvussa Ensimmäinen kontakti. Ole siis kärsivällinen ja seuraa palautusprosessia päänäytössä klikkaamalla synkronointikuvaketta.


![blixt](assets/en/14.webp)


Kuten tässä esimerkissä näkyy, Bitcoin-lohkot ovat 100-prosenttisesti synkronoitu (A) ja palautusprosessi on käynnissä (B). Tämä tarkoittaa, että LN-kanavat, jotka sinulla oli aiemmin, suljetaan ja varat palautetaan Blixt onchain Wallet:aan.


Tämä prosessi vie aikaa! Ole siis kärsivällinen ja yritä pitää Blixt aktiivisena ja verkossa. Alustava synkronointi voi kestää 6-8 minuuttia ja kanavien sulkeminen 10-15 minuuttia. Sinun on siis parasta pitää laite hyvin ladattuna.


Kun tämä prosessi on alkanut, voit tarkistaa Magic Drawer - Lightning Channels -osiosta jokaisen edellisen kanavasi tilan, jossa näkyy, että ne ovat "odottavat sulkemista" -tilassa. Kun kukin kanava on suljettu, voit nähdä sulkeutuvan tx:n onchain Wallet:ssa (katso Magic Drawer - Onchain) ja avata tx-valikon lokin.


![blixt](assets/en/15.webp)


On myös hyvä tarkistaa ja lisätä, jos niitä ei ole, vanhan LN-solmun aiemmat vertaisvertaisverkkosi. Mene siis Asetukset-valikkoon, alas kohtaan "Lightning Network" ja valitse vaihtoehto "Näytä salamavertailijat".


![blixt](assets/en/16.webp)


Osiossa näet vertaisvertaiset, joihin olet yhteydessä kyseisellä hetkellä, ja voit lisätä lisää, parempi lisätä ne, joilla oli kanavia aiemmin. Mene vain [Amboss-sivulle](https://amboss.space/), etsi vertaisverkkosolmusi alias tai nodeID ja skannaa niiden solmu-URI.


![blixt](assets/en/17.webp)


Kuten yllä olevassa kuvassa näkyy, on 3 näkökohtaa:


A - edustaa clearnet-solmun Address URI:tä (verkkotunnus/IP)


B - edustaa Tor-sipulisolmua Address URI (.onion)


C - on QR-koodi, joka skannataan Blixt-kameralla tai kopiointipainikkeella.


Tämä solmu Address URI sinun on lisättävä se vertaisluetteloon. Huomaa siis, että pelkkä solmun alias-nimi tai nodeID ei riitä.


Nyt voit siirtyä Magic Drawer (vasemmassa ylävalikossa) - Lightning Channels, ja näet, millä maturiteettilohkon korkeudella varat palautetaan onchain Address:een.


![blixt](assets/en/18.webp)


Lohkon numero 764272 on se hetki, jolloin varoja voidaan käyttää Bitcoin-ketjun Address-ketjussa. Ja se voi kestää jopa 144 lohkoa 1. vahvistuslohkosta, kunnes ne vapautetaan. [Tarkista se siis Mempool:stä] (https://Mempool.space/).


Ja siinä kaikki. Odota vain kärsivällisesti, kunnes kaikki kanavat on suljettu ja varat on palautettu ketjussa olevaan Wallet:een.


👉 **Salainen palautusmenetelmä :**


Blixt LND -solmun palauttamiseen on toinenkin menetelmä, jolla voit edes sulkea kanavia. Mutta se on piilotettu tavallisilta noob-käyttäjiltä, koska tämä menetelmä on AINOASTAAN niille, jotka tietävät, mitä ovat tekemässä.


Jos haluat siirtää nykyisen (toimivan) Blixt-solmun toiseen uuteen laitteeseen sulkematta nykyisiä LN-kanavia, sinun on suoritettava seuraavat vaiheet:



- Oletamme, että olet jo tallentanut Blixt Wallet seed (24 sanaa aezeed)
- Mene vanhassa laitteessa kohtaan "Asetukset" - debug-osio - "Compact LND database". Tämä vaihe on valinnainen, mutta sitä suositellaan, jos haluat pienemmän kokoisen channel.db-tiedoston. Yleensä se on melko suuri, riippuen solmun aktiivisuudesta. Tämä käynnistää Blixtin uudelleen ja pienentää db-tiedoston kokoa.
- Kun olet käynnistänyt järjestelmän uudelleen, siirry kohtaan "Asetukset" ja vaihda tavallinen peitenimesi muotoon "Hampus". Tämä aktivoi piilotetut asetukset, jotka ovat vain edistyneille käyttäjille.
- Mene alaspäin "Debug"-osioon ja näet uuden vaihtoehdon "Export channel.db file". VAROITUS! Kun teet tämän viennin, olemassa oleva Blixt LN -solmu poistetaan käytöstä tässä vanhassa laitteessa ja vie koko solmutietokannan (channel.db) valmiiksi tuotavaksi uuteen laitteeseen.
- Tämä db-tiedosto tallennetaan vanhan laitteesi tiettyyn kansioon (Documents tai Downloads), josta sinun on siirrettävä se sellaisenaan uuteen laitteeseesi. Voit käyttää esimerkiksi [LocalSend FOSS -sovellusta](https://github.com/localsend/localsend) siirtääksesi tiedoston suoraan laitteiden välillä.
- Tällä hetkellä vanhan Blixtin on pysyttävä suljettuna. ÄLÄ AVAA SITÄ UUDELLEEN!
- Kun olet siirtänyt channel.db-tiedoston uuteen laitteeseen, käynnistä Blixtin uusi asennus ja valitse ensimmäisessä näytössä "Restore Wallet".
- Paina painiketta, jossa lukee "Valitse SCB-tiedosto", pitkään (EI yksinkertaista napsautusta!) ja näet sitten mahdollisuuden valita channel.db-tiedoston, johon tallennat sen paikallisesti uudessa laitteessa. Jos vain yksinkertaisesti painat tuota painiketta, se käyttää oletusarvoisesti SCB-tiedostoa (sulkeutuvilla kanavilla), se ei toimi täydelle varmuuskopiolle live-kanavilla.
- Laita 24 sanaa seed ja napsauta sitten "Palauta"
- Näet, että Blixt alkaa synkronoida Neutrinon kanssa. Voit myös katsella synkronointilokeja.
- PITÄÄ MIELESSÄ! Yritä pitää Blixt auki koko ajan tässä vaiheessa! Älä anna sen mennä lepotilaan tai sulje sovelluksen näyttöä. Se voi häiritä alkuperäistä synkronointia ja sinun on tehtävä se uudelleen. Odota kärsivällisesti, ei kestä kuin muutaman minuutin.
- Kun alustava lohkojen synkronointi on valmis, se skannaa nopeasti aiemmat Wallet-osoitteesi, minkä jälkeen kanavasi ovat jälleen verkossa, elossa ja kunnossa.
- Valitettavasti aiempaa maksuhistoriaa ja yhteystietoja ei ole (vielä) mahdollista palauttaa. Mutta se ei ole kuitenkaan niin tärkeää.


Ja VALMIS! Nyt sinulla on täysin palautettu Blixt LN -solmu. Se voi toimia myös muiden LND varmuuskopioiden kanssa (Umbrel, Raspiblitz jne.), jos olet aiemmin tallentanut oikein channel.db-tiedoston. Blixt voi siis kirjaimellisesti pelastaa minkä tahansa kuolleen LND-solmun.


---

## Blixt - Neljäs kontakti


Tämä luku käsittelee räätälöintiä ja tietää paremmin Blixt Node. En aio kuvata kaikkia käytettävissä olevia ominaisuuksia, niitä on liian paljon ja ne on jo selitetty [Blixt Features Page](https://blixtwallet.github.io/features).


Mutta huomautan joitakin niistä, jotka ovat välttämättömiä, jotta voit käyttää Blixt-järjestelmääsi ja saada hyvän kokemuksen.


### A - Nimi (NameDesc)


![blixt](assets/en/19.webp)


[NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) on standardi "vastaanottajan nimen" ilmoittamiseksi BOLT11-laskuissa.


Tämä voi olla mikä tahansa nimi, ja sitä voidaan muuttaa milloin tahansa.


Tämä vaihtoehto on todella hyödyllinen useissa tapauksissa, kun haluat lähettää nimen yhdessä Invoice-kuvauksen kanssa, jotta vastaanottaja voi saada vihjeen siitä, kuka on vastaanottanut Sats:n. Tämä on täysin valinnainen, ja käyttäjän on myös maksunäytössä rastitettava ruutu, joka osoittaa, että alias-nimi halutaan lähettää.


Tässä on esimerkki siitä, miten se näkyy, kun käytät [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


Tämä on toinen esimerkki, jossa lähetetään toiseen Wallet-sovellukseen, joka tukee NameDesc-sovellusta:


![blixt](assets/en/21.webp)


### B - salamalaatikko


Alkaen uudesta versiosta v0.6.9-420 [äskettäin julkistettu](https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420), Blixt otti käyttöön uuden tehokkaan ominaisuuden Lightning Address:lle Blixtissä.


Tämä uusi ominaisuus on valinnainen opt-in, ei ole oletusarvoisesti päällä!


Tällä hetkellä oletusarvoinen LN-laatikko toimii Blixt-palvelimella ja tarjoaa @blixtwallet.com LN Address. Mutta KUKA tahansa, jolla on julkinen LND-solmu, voi käyttää Lightning Box -palvelinta ja tarjota LN Address:ää omalle verkkotunnukselleen, itsesäilytettäväksi.


Juuri nyt Blixt-palvelin välittää LN @blixtwallet.com -osoitteisiin lähetetyt maksut vain niille Blixt-käyttäjille, jotka ovat asettaneet LN Address -osoitteensa. Käyttäjien on asetettava Blixt-solmunsa Wallet "pysyvään tilaan", jotta he voivat vastaanottaa näitä maksuja @blixtwallet.com LN-osoitteisiinsa.


Katso julkaisutiedotteista videoesittely siitä, miten LN Address asennetaan Blixtissä.


Tämä LN Address on toteutettu Blixt Wallet -sovellukseen, se on kuin keskustelu LN:n kautta, välitön ja hauska, ja se tukee myös [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (peitenimen lisääminen maksuun). Voit lisätä yhteystietoluetteloon kaikki tavalliset LN-osoitteesi, joita käytät usein, ja pitää ne käsillä chattailua varten. Nyt Blixtiä voidaan pitää täydellisenä LN chat-sovelluksena 😂😂.


Toinen hyödyllinen ominaisuus on täysi tuki LUD-18:lle (jota myös [Stacker.News](https://stacker.news/r/DarthCoin) ja muut tukevat).


![blixt](assets/en/22.webp)


Kuten yllä olevasta kuvakaappauksesta näkyy, Stacker News -tililtä lähetettynä se näytti hienosti logon + LN Address + viestin. Sama tapa toimii myös Blixtistä lähetettäessä, voit liittää Blixtin LN Address:n tai yksinkertaisesti lisätä alias-nimen (joka on asetettu aiemmin Blixtin asetuksissa) tai jopa molemmat.


Tämä LUD-18:n vaihtoehto voisi olla hyödyllinen myös tilauspalveluissa, joissa käyttäjä voi lähettää tietyn peitenimen (joka EI ole solmun peitenimi tai oikea nimesi!), ja sen perusteella sinut voidaan rekisteröidä tai vastaanottaa tietty viesti tai mitä tahansa muuta. Alias-nimen ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ kommentin ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) liittämisellä LN-maksuun voi olla useita käyttötarkoituksia!


Tässä on [Lightning Boxin] (https://github.com/hsjoberg/lightning-box) koodi, jos käytät sitä itsellesi, perheellesi ja ystävillesi omalla solmullasi.


Täällä voit myös käyttää [LSP Dunder -palvelinta](https://github.com/hsjoberg/dunder-lsp) Blixtin mobiilisolmuille ja tarjota likviditeettiä Blixtin käyttäjille, jos sinulla on hyvä julkinen LN-solmu (toimii vain LND:n kanssa).


### C - LN-kanavien ja seed-sanojen varmuuskopiointi


Tämä on erittäin tärkeä ominaisuus !


LN-kanavan avaamisen tai sulkemisen jälkeen sinun on tehtävä varmuuskopiointi. Se voidaan tehdä manuaalisesti tallentamalla pieni tiedosto paikalliseen laitteeseen (yleensä latauskansioon) tai käyttämällä Google Drive- tai iCloud-tiliä.


![blixt](assets/en/23.webp)


Siirry kohtaan Blixt-asetukset - Wallet. Siellä voit tallentaa kaikki Blixt Wallet:n tärkeät tiedot:



- "Näytä Mnemonic" - näyttää 24 sanaa seed kirjoittaa ne ylös
- "Poista Mnemonic laitteesta" - tämä on valinnainen, ja käytä sitä vain, jos todella haluat poistaa seed-sanat laitteestasi. Tämä EI poista Wallet:tä, vain seed:n. Mutta ole tietoinen ! Niitä ei voi palauttaa, jos et ole ensin kirjoittanut niitä muistiin.
- "Vie kanavan varmuuskopio" - tämä vaihtoehto tallentaa pienen tiedoston paikalliseen laitteeseesi, yleensä "lataukset"-kansioon, josta voit ottaa sen ja siirtää sen laitteen ulkopuolelle turvalliseen säilytykseen.
- "Tarkista kanavan varmuuskopiointi" - tämä on hyvä vaihtoehto, jos käytät Google Drivea tai iCloudia etänä tehdyn varmuuskopion eheyden tarkistamiseen.
- " Google drive -kanavan varmuuskopiointi" - tallentaa varmuuskopiotiedoston henkilökohtaiseen Google-asemaan. Tiedosto on salattu ja se tallennetaan erilliseen arkistoon kuin tavalliset Google-tiedostosi. Joten ei ole huolta, että kuka tahansa voi lukea. Joka tapauksessa tämä tiedosto on täysin hyödytön ilman seed-sanoja, joten kukaan ei voi ottaa varoja vain tästä tiedostosta.


Suosittelen tähän jaksoon seuraavaa:



- käytä salasanahallintaohjelmaa seed:n ja varmuuskopiotiedoston turvalliseen säilyttämiseen. KeePass tai Bitwarden ovat erittäin hyviä tähän tarkoitukseen, ja niitä voidaan käyttää useilla alustoilla ja itse isännöitynä tai offline-tilassa.
- Tee varmuuskopiointi joka kerta, kun avaat tai suljet kanavan. Kyseinen tiedosto päivitetään kanavien tiedoilla. Sitä ei tarvitse tehdä jokaisen LN:llä tekemäsi tapahtuman jälkeen. Kanavan varmuuskopio ei tallenna näitä tietoja, vaan ainoastaan kanavan tilan.


![blixt](assets/en/24.webp)


---

## Blixt - Vinkkejä ja niksejä


### TAPAUS 1 - SYNKRONOINTIONGELMAT


"_My Blixt ei synkronoi... Blixtini ei näytä saldoa... Blixtini ei voi avata kanavia... Yritin palauttaa sen toiseen laitteeseen... jne_"


Kaikki nämä ongelmat alkavat siitä, että LAITTEESI EI SYNKRONOI OIKEASTI. Ymmärrä tämä tärkeä näkökohta: Blixt on mobiili LND-solmu, joka käyttää Neutrinoa lohkojen synkronointiin/lukemiseen.



- Tässä on vähemmän tekninen selitys [Bitcoin Magazine]sta (https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Tässä on lisää teknisiä resursseja [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/) osoitteesta
- Näin voit aktivoida Neutrinon omassa kotisolmussasi ja tarjota lohkosuodattimia mobiilisolmulle, [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


MUISTUTUS: IP-osoitteesi tai xpubisi ei vuoda. Luet vain lohkoja etäsolmusta neutriinon avulla. Siinä kaikki. Kaikki muu tapahtuu paikallisessa laitteessasi.


Sitä ei siis tarvitse käyttää Torin kanssa. Tor lisää synkronointiprosessiin valtavan viiveen ja tekee Blixtistäsi hyvin epävakaan. Jos todella haluat käyttää Torin kautta, varmista, mitä teet ja sinulla on hyvä yhteys ja kärsivällisyyttä. Sama koskee VPN:n käyttöä. Ole varovainen, mitä latenssia sinulle annetaan VPN:stä.


Voit testata neutriinopalvelimen viiveen yksinkertaisesti pingaamalla sitä tietokoneelta tai matkapuhelimesta.


![blixt](assets/en/25.webp)


Tämä on tavallinen pingaus neutrino-palvelimelle europe.blixtwallet.com, joka osoittaa, että yhteys on erittäin hyvä, vasteaika on keskimäärin 50 ms ja TTL 51. Vastausaika voi vaihdella, mutta ei liikaa. TTL:n on oltava vakaa.


Jos nämä arvot ovat yli 100-150ms, synkronointiprosessi pysähtyy tai vielä pahempaa, se voi aiheuttaa suljettuja kanavia vertaisverkoissa ! Älä jätä tätä näkökohtaa huomiotta.


Ilman kunnollista synkronointia et myöskään näe oikeaa tasapainoa tai LN-kanavat eivät pääse verkkoon ja toimintaan. Ei ole väliä kuinka monta giga ultra terra mbps sinulla on latausnopeus IT DOESN'T MATTER. Sillä on väliä aikavasteella ja TTL:llä (time to live).


Tämä on kuin yleinen tapaus LATAM-maiden käyttäjille. En tiedä, mitä siellä tapahtuu, mutta teillä on kauhea yhteys, jossa pingit ovat yli 200 ms, mikä voi häiritä synkronointia.


Mikä on siis ratkaisu näille epätoivoisille käyttäjille?



- lopeta Blixtin käyttö Torin kanssa. On täysin hyödytön
- voit käyttää VPN:ää, mutta valitse se viisaasti ja seuraa koko ajan pingiä. Käytä sellaista, joka on lähempänä maantieteellistä sijaintiasi. Muista, että etäisyys tarkoittaa enemmän ms:n vasteaikaa.
- valitse viisaasti neutriinopalvelimet, tässä on luettelo tunnetuista julkisista neutriinopalvelimista:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Toinen tapa on valita yksi solmujen luettelosta, jossa ilmoitetaan "kompaktit suodattimet" (BIP157 / neutriino) - [Bitnodes Page Neutrino filter](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Valitse yksi, joka on lähempänä maantieteellistä sijaintiasi.


Toinen tapa (paras tapa) on muodostaa yhteys paikalliseen yhteisön solmuun, jota ylläpitää ystäväsi tai ryhmä, jonka tunnet ja joka tarjoaa neutriinoyhteyttä. [Tässä on ohjeet, miten se tehdään.](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Heidän solmuunsa ei vaikuta mitenkään, he tarvitsevat vain vakaan ja julkisen yhteyden.


LATAM-alueella tarvitaan lisää neutriinopalvelimia, jotta synkronointi olisi parempaa ja nopeampaa. Järjestäytykää siis paikallisen Bitcoin-yhteisönne kanssa ja päättäkää, kuka ja missä Bitcoin Core + Neutrino -palvelin on käytössä omassa käytössänne. Pelkkä julkinen IP-osoite riittää. Jos sinulla ei ole pääsyä julkiseen IP:hen, voit käyttää VPS-IP:tä ja tehdä wireguard-tunnelin kotisolmuun. Näin ohjaat kaiken liikenteen paikalliseen VPS-IP:hen paljastamatta mitään yksityisiä tietoja kotisolmusta.


### TAPAUS 2 - SYNKRONOINTIA EI KOSKAAN LOPETETA


"_My Blixt on hyvä yhteys neutrino-palvelimeen, mutta synkronointi on jumissa._"


#### Aikapalvelin


Joskus ihmiset käyttävät erilaisia vanhoja laitteita tai eivät ole kunnolla yhteydessä aikapalvelimeen. Neutrino synkronoi ok, kunnes saavutetaan todelliset lohkot, jotka eivät vastaa todellista paikallista aikaa. Näet Blixt LND:n lokitiedoissa virheen, jossa sanotaan, että "lohkon aikaleima on kaukana tulevaisuudesta" tai jotain, joka liittyy "otsikko ei läpäise terveystarkastusta".


Pikakorjaus: aseta laitteesi oikea aika ja päivämäärä ja käynnistä Blixt uudelleen.


#### Vähän tilaa laitteessa


Joskus vanhaa laitetta käytettäessä, jossa on vähän tilaa, se voi saavuttaa kynnysarvon ja juuttua. Mitä enemmän käytät tätä LND-mobiilisolmua, sitä suuremmiksi kasvavat neutriinotiedostot ja myös channel.db-tiedosto.


Nopea korjaus: Valitse "pysäytä LND ja poista neutriinotiedostot". Se käynnistää sovelluksen uudelleen ja aloittaa uuden tuoreen synkronoinnin. Joskus tämä pikakorjaus voi korjata myös vioittuneet tiedot. Muista, että kestää jonkin aikaa, 1-3 minuuttia, ennen kuin synkronointi on täysin valmis. Se EI poista olemassa olevia rahastoja tai kanavia, mutta kyllä, uudelleensynkronoinnin jälkeen se voi käynnistää Bitcoin-osoitteiden uudelleen skannauksen, ja se voi viedä enemmän aikaa.


Seuraavaksi tarkistetaan, kuinka paljon tietoja on vielä varattu. Näet tämän Android-sovelluksen tiedot - data -kohdassa. Jos se on edelleen yli 400-500 Mt, voit tiivistää LND-tiedostot. Mene siis Blixt Options - Debug-osioon - Valitse "Compact DB LND". Käynnistä Blixt-sovellus uudelleen, jos se ei toimi automaattisesti. Tiivistäminen tapahtuu käynnistyksen yhteydessä ja vain kerran. Nyt näet, että Blixtin tiedot ovat vähemmän varattuja.


#### Pysyvä tila


Joskus ihmiset eivät avaa Blixtiä pitkään aikaan, joten synkronointi on aivan liian vanha. Mutta he odottavat, että synkronointi tapahtuu heti, kun he avaavat sen.


Ole kärsivällinen ja katso ylhäältä pyörivää pyörää. Valinnaisesti voit mennä Options - See Node Info -kohtaan ja katsoa, onko ketjuun synkronoitu ja kuvaajaan synkronoitu merkintä "true". Ilman tuota "true"-merkintää et voi käyttää kunnolla Blixtiä, et näe oikein saldoa, et näe LN-kanavia verkossa, et voi tehdä maksuja.


Nopea korjaus: Blixt-solmun "elossa pitämiseen" on tehokas vaihtoehto. Mene kohtaan Options - Experiments - Valitse "Activate Persistent Mode". Tämä käynnistää Blixtin uudelleen ja asettaa LND-palvelun pysyvään tilaan, eli se on aina aktiivinen ja pitää synkronoinnin verkossa, vaikka vaihtaisit toiseen sovellukseen tai yksinkertaisesti sulkisit Blixtin (ei pakotetusti sulkemalla tai tappamalla tehtävän). Voit pitää sitä näin koko päivän, jos sinulla on vakaa yhteys ja sinun on käytettävä Blixtiä useita kertoja. Se ei kuluta liikaa akkua.


### TAPAUS 3 - HALUAN SIIRTYÄ TOISEEN LAITTEESEEN


OK tästä skenaariosta kirjoitin laajan oppaan [FAQ-sivulle](https://blixtwallet.github.io/faq#blixt-restore): 2 vaihtoehtoa, nopea (kanavien yhteistoiminnallinen sulkeminen ennen siirtymistä) ja hidas (pakota kanavien sulkeminen, koska vanha laite on kuollut).


Haluan kuitenkin toistaa tässä joitakin tärkeitä näkökohtia ja lisätä uuden "salaisen" menettelyn.


MUISTUTUS:



- Tee aina varmuuskopio kanavien tilasta (SCB) aina kun avaat tai suljet kanavan. Se vie vain muutaman sekunnin.
- Älä säilytä vanhoja SCB-tiedostoja, jotta et mene sekaisin ja palauta niitä. Ovat täysin hyödyttömiä ja voivat käynnistää rangaistusmenettelyn, jos niitä käytetään. Käytä aina SCB-tiedoston viimeisintä versiota, jos jatkat palauttamista.
- Tallenna SCB-tiedosto (on salattu teksti, jonka tiedostotunnus on .bin) pois laitteestasi turvalliseen paikkaan. Voit käyttää [LocalSend] (https://github.com/localsend/localsend) tämän tiedoston siirtämiseen tietokoneeseen tai muuhun laitteeseen.
- Tallenna myös Blixt Wallet:n seed turvalliseen paikkaan, esimerkiksi offline-salasanahallintaan / salattuun USB-muistiin.


Salainen menetelmä: Miten siirtää Blixt-solmu sulkematta olemassa olevia kanavia. Tätä varten sinun on luettava huolellisesti tämän oppaan edellinen jakso "Kolmas yhteyshenkilö" aiheesta "Wallet:n palauttaminen".


Tämä menettely EI OLE NOOBSille, se on vain edistyneille käyttäjille! Siksi se ei ole laajalti avoinna ja suosittelen tekemään sen vain Blixtin kehittäjien tai tukeni avustuksella. Älä jätä tätä neuvoa huomiotta.


### TAPAUS 4 - MITÄ VERTAISVERTAISIA KÄYTETÄÄN KANAVIEN AVAAMISEEN?


Kuten kirjoitin [Blixtin oppaiden sivulla](https://blixtwallet.github.io/guides), on monia tapoja avata kanavia tällä LND-mobiilisolmulla. Mutta joitakin tärkeitä seikkoja haluaisin muistuttaa tässä:



- avoimet tunnettujen LSP-solmujen ja yhteisön varmennettujen vertaisverkkojen kanssa. [Katso tästä luettelo](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- älä avaa satunnaisia Tor only -solmuja. Ne ovat arvottomia, ja saat vain ongelmia, jotka liittyvät siihen, että et voi suorittaa maksuja. Ei ole väliä kuinka hyvä ystäväsi "node runner" on, jolla on surkea Tor-solmu viidakossa, se ei koskaan anna sinulle parhaita reittejä liikkuvalle yksityiselle solmulle. Et avaa kanavia jonkun kanssa, koska hän on ystäväsi. Tämä ei ole Facebook! Avaat kanavan: hyvien reittien, pienten maksujen ja saatavuuden vuoksi.
- ei tarvitse avata paska tonnia pieniä kanavia, 2-3 tai enintään 4, mutta hyvä määrä Sats. Älä avaa pieniä kanavia, ovat täysin hyödyttömiä. Pienemmät kuin 200k kännykälle ei ole paljon käyttöä.
- pitää mielessä LSP:t, jotka tarjoavat saapuvia kanavia ja JIT-kanavia (just in time). Ne ovat erittäin hyödyllisiä, koska sinun ei tarvitse käyttää mitään UTXO-varojasi, vaan voit maksaa avautuvan kanavan varoilla, joita sinulla on jo muissa LN-lompakoissa, pinota ja valmistella niitä suuremman kanavan avaamista varten. Sinun pitäisi käyttää näitä JIT-kanavia eduksesi. [Olen selittänyt tässä oppaassa] (https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) enemmän vaihtoehtoja vertaisvertaisille yksityisille solmuille, kuten Blixtille. Myös [tässä tässä SN:ssä julkaistussa oppaassa](https://stacker.news/items/679242/r/DarthCoin) selitin, miten hallita yksityisten mobiilisolmujen likviditeettiä.


---

## Päätelmä


OK, Blixt tarjoaa monia muita upeita ominaisuuksia, annan sinun tutustua niihin yksi kerrallaan ja pitää hauskaa.


Tämä sovellus on todella aliarvioitu, lähinnä siksi, että sen taustalla ei ole mitään riskipääomarahoitusta, vaan se on yhteisölähtöinen, ja se on rakennettu rakkaudella ja intohimolla Bitcoin:ää ja Lightning Network:aa kohtaan.


Tämä mobiili LN-solmu, Blixt, on erittäin tehokas työkalu monien käyttäjien käsissä, jos he osaavat käyttää sitä hyvin. Kuvittele, että kuljeskelet ympäri maailmaa LN-solmu omassa taskussasi, eikä kukaan tiedä sitä.


Puhumattakaan kaikista muista monipuolisista ominaisuuksista, joita muut Wallet-sovellukset eivät pysty tarjoamaan.


Sillä välin tässä ovat kaikki linkit tästä hämmästyttävästä Bitcoin Lightning Node:



- [Blixtin virallinen verkkosivusto](https://blixtwallet.com/)
- [Blixt Github-sivu](https://github.com/hsjoberg/blixt-Wallet/)
- [Blixtin ominaisuudet -sivu](https://blixtwallet.github.io/features) - selittää yksitellen jokaisen ominaisuuden ja toiminnon.
- [Blixt FAQ-sivu](https://blixtwallet.github.io/faq) - Luettelo Blixtin kysymyksistä ja ongelmanratkaisusta
- [Blixt Guides page](https://blixtwallet.github.io/guides) - demot, video-oppaat, lisäoppaat ja käyttötapaukset Blixtille
- Lataa: [Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [APK direct download](https://github.com/hsjoberg/blixt-Wallet/releases)
- [Telegram-ryhmä suoraa tukea varten](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [Geyserin joukkorahoitussivu](https://geyser.fund/project/blixt) - lahjoittaa Sats haluamallasi tavalla tukeaksesi projektia
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - anonyymi LN chat
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - mainosvideo (voit testata LN:n ensimmäistä käyttöä)
- [Tulostettava A4-esite Blixtin ensimmäisistä askeleista, eri kielillä](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt tarjoaa myös täysin toimivan demoversion](https://blixt-Wallet-git-master-hsjoberg.vercel.app/) suoraan verkkosivuillaan tai verkkoversiossa, jotta voit testata täydellisen kokemuksen, ennen kuin aloitat käytön todellisessa maailmassa.


---
**DISCLAIMER:**


*Tämän sovelluksen kehittäjät eivät maksa tai tue minua millään tavalla. Kirjoitin tämän oppaan, koska huomasin, että kiinnostus tätä Wallet-sovellusta kohtaan kasvaa, mutta uudet käyttäjät eivät vieläkään ymmärrä, miten sen käyttö aloitetaan. Myös auttaakseni Hampusta (pääkehittäjää) dokumentoinnissa tämän solmun käyttämisestä Wallet.*


*Minulla ei ole muita intressejä tämän LN-sovelluksen edistämisessä kuin edistää Bitcoin- ja LN-sovellusten käyttöönottoa. Tämä on ainoa keino!*


---