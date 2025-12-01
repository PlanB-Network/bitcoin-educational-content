---
name: Mostro
description: KYC-vapaa Bitcoin P2P vaihtofoorumi Lightningin ja Nostrin kautta
---

![cover](assets/cover.webp)



Miten voit hankkia tai myydä bitcoineja vaarantamatta taloudellista riippumattomuuttasi? Keskitetyt alustat edellyttävät invasiivisia KYC-menettelyjä, jotka paljastavat henkilötietosi, ja tili voidaan jäädyttää mielivaltaisesti tai sitä voidaan valvoa valtion toimesta.



**Mostro P2P** tarjoaa hajautetun vaihtoehdon, jossa yhdistyvät Lightning Network, Nostr-protokolla ja holding-laskut. Sen tärkein innovaatio: automatisoitu escrow-järjestelmä, jossa bitcoinisi pysyvät hallinnassasi koko vaihdon ajan, mikä poistaa varkauden, pörssin konkurssin tai mielivaltaisen takavarikon riskin.



## Mikä on Mostro P2P?



Mostro P2P on avoimen lähdekoodin Bitcoin-vaihtoprotokolla, jonka on luonut **grunch**, vuonna 2021 lanseeratun suositun Telegram-botin **lnp2pbot** kehittäjä. Vaikka lnp2pbot mahdollisti jo KYC-vapaat P2P-vaihdot Lightningin kautta, se esitti merkittävän haavoittuvuuden: **Telegram muodostaa keskitetyn vikapisteen**, joka on altis hallitusten harjoittamalle sensuurille.



Mostro edustaa tämän konseptin **hajautettua kehitystä**: korvaamalla Telegramin **Nostr**-protokollalla (hajautettujen releiden mitattavissa oleva verkko) Mostro eliminoi tämän järjestelmäriskin. Protokolla yhdistää Lightning Network:n välittömiin transaktioihin, Nostrin sensuurin kestävään viestintään ja **pidätyslaskuihin** luodakseen aidosti vapaamuotoisen automatisoidun escrow-järjestelmän.



### Tekninen arkkitehtuuri



Mostro toimii kolmen osatekijän avulla:




- Daemon Mostrod**: koordinoi käyttäjien ja Lightning Network:n välistä tiedonvaihtoa
- Lightning**-solmu: luo holding-laskuja (~24h kryptografinen escrow)
- Mostro**-asiakkaat: käyttöliittymät (CLI, Mobile, Web)



Toimeksiannot julkaistaan Nostrissa julkisina tapahtumina (tyyppi 38383), kun taas yksityiset kaupat välitetään päästä päähän salattujen viestien avulla (NIP-59, NIP-44). Kukin Mostro-instanssi määrittelee omat maksunsa (yleensä 0,3-1 %) ja transaktiorajansa (muutamasta tuhannesta useisiin satoihin tuhansiin sats, riippuen instanssista).



### Ratkaisevat edut



**Sensuurin kestävä**: Mikään hallitus ei voi sulkea Mostroa niin kauan kuin Nostr-releet ovat olemassa jossain päin maailmaa. Toisin kuin haavoittuva lnp2pbot Telegramin kautta, Mostro mahdollistaa vaihdot, jotka ovat **sensuurin kestäviä**.



**Pelastaminen ilman huoltajuutta**: Lightning hold -laskut lukitsevat bitcoinisi siirtämättä niitä pysyvästi. Varasi pysyvät hallinnassasi ja palautetaan sinulle automaattisesti ongelmatilanteessa (~24h).



**Suojattu luottamuksellisuus**: Kaksi tilaa käytettävissä tarpeidesi mukaan. Maine-tila** yhdistää maineesi Nostr-avaimeesi ja rakentaa näin pysyvää luottamusta. Täysin yksityinen tila** suosii ehdotonta anonymiteettiä kertakäyttöisillä, hetkellisillä avaimilla.



## Tärkeimmät ominaisuudet



**Depentralisoitu viestintä**: Kaikki tilaukset julkaistaan Nostrissa kryptografisesti allekirjoitettujen tapahtumien kautta. Yksityiset neuvottelut välitetään päästä päähän salattujen viestien avulla, mikä takaa ehdottoman luottamuksellisuuden.



**Mainintajärjestelmä**: 5 tähden luokitus iteratiivisella laskennalla, joka tallennetaan pysyvästi Nostriin. Mahdollistaa sinun rakentaa vähitellen mainetta luotettavana kauppiaana.



**Depentralisoitu välimiesmenettely**: Riitatilanteessa puolueeton välimies tutkii todisteet ja tekee päätöksen avoimin perustein. Jokaisesta riidasta syntyy yksilöllinen token jäljitettävyyden varmistamiseksi.



**Maksamisen joustavuus**: Yadio.io:n valuuttakurssipalvelun kautta. Hyväksyy SEPA-siirrot, PayPalin, Revolutin, käteisen ja minkä tahansa osapuolten välillä sovitun menetelmän.



## Mostro-asiakkaat saatavilla



Mostro tarjoaa kaksi pääasiakasohjelmaa P2P-vaihtoa varten.



### Mostro CLI - Komentoriviasiakas



**Mostro CLI** on kehittynein ja toimivin asiakasohjelma. Se on kirjoitettu Rust-kielellä ja tarjoaa kaikki Mostro-ominaisuudet komentorivikäyttöliittymän kautta. Yhteensopiva macOS:n, Linuxin ja Windowsin kanssa.



**Pääsäätimet** :




- "Listatilaukset": Näytä kaikki saatavilla olevat tilaukset
- `neworder` : Luo uusi osto- tai myyntitoimeksianto
- `takesell` / `takebuy`: Ota osto- tai myyntitoimeksianto
- `fiatsent`: Vahvista fiat-maksun lähettäminen
- `release`: Vapauta escrow ja viimeistele vaihto
- `getdm`: Näytä suorat viestit
- `rate` : Arvioi vastapuolesi vaihdon jälkeen



Ihanteellinen teknisille käyttäjille, automaatioon ja ympäristöihin, joissa vaaditaan maksimaalista turvallisuutta.



### Mostro Mobile - Älypuhelinsovellus



Alpha-version **mobiilisovellus** mahdollistaa P2P-kaupankäynnin suoraan älypuhelimesta. Intuitiivinen graafinen Interface, jossa on välilehtinavigointi, toimeksiantojen katselu, kehittyneet suodattimet ja integroitu chat, jolla voit kommunikoida vastapuoliesi kanssa.



Se on saatavilla **Androidille** (GitHubin APK:n kautta), ja se on optimaalinen valinta käyttäjille, jotka suosivat yksinkertaisuutta ja satunnaista mobiilikauppaa.



### Mostro-web - Interface web (kehitteillä)



Interface edistynyt JavaScript-verkkosovellus, jota kehitetään aktiivisesti. Suunniteltu tarjoamaan kattava käyttäjäkokemus ja laajat kaupankäynti- ja salkunhallintatoiminnot. Pääsy selaimen kautta ilman asennusta.



## Asennus ja konfigurointi



Tämä opetusohjelma opastaa sinut kahden tärkeimmän Mostro-asiakasohjelman asennuksessa ja käytössä: CLI ja mobiilisovellus.



### Olennaiset edellytykset



Ennen kuin aloitat, tarvitset :





- Toimiva Lightning Network** wallet, jolla on riittävästi likviditeettiä (tai Lightning-yhteensopiva)
 - Suositellaan: Phoenix, Breez, Wallet tai Satoshi...
 - Vähintään 1000 satoshin likviditeetti testattavaksi



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Yksityinen Nostr**-avain (muoto `nsec1...`)
 - Luo oma kaupankäyntiavain [nostrkeygen.com](https://nostrkeygen.com/)
 - Tärkeää**: Älä koskaan käytä henkilökohtaista Nostr-avainta
 - Säilytä yksityinen avain turvallisessa paikassa (salasanahallinta)





- Valinnainen mutta suositeltava**: VPN- tai Tor-yhteys IP-osoitteen peittämiseksi



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Mostro CLI asennus



#### MacOS:ssä



**Vaihe 1: Rust-tarkistus** *Vaihe 1: Rust-tarkistus**



Tarkista, että Rust on asennettu (vaaditaan versio 1.64+):



```bash
rustc --version
```



Jos Rust ei ole asennettu :



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Vaihe 2: Arkiston kloonaus**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Vaihe 3: Konfigurointi**



Kopioi ja muokkaa :



```bash
cp .env-sample .env
```



Avaa tiedosto `.env` ja määritä asetukset:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**Tärkeää CLI/Mobile**-synkronoinnin kannalta: Jos haluat käyttää samoja tilauksia CLI:ssä ja mobiilisovelluksessa, sinun on käytettävä **samaa Mostro Pubkey -avainta** ja **samaa Nostr-releetä** molemmissa asiakkaissa. Tarkista nämä asetukset mobiilisovelluksen Asetuksissa.



![Configuration .env](assets/fr/02.webp)



**Vaihe 4: Asennus**



Käännä ja asenna CLI :



```bash
cargo install --path .
```



Kokoaminen kestää 1-2 minuuttia. Suoritettava `mostro-cli`-tiedosto asennetaan paikkaan `~/.cargo/bin/`.



![Installation du CLI](assets/fr/03.webp)



**Vaihe 5: Tarkista**



Tarkista, että kaikki toimii:



```bash
mostro-cli --help
```



Sinun pitäisi nähdä täydellinen luettelo tilauksista.



![Vérification avec --help](assets/fr/04.webp)



#### Linuxissa (Ubuntu/Debian)



Asennus identtinen macOS:n kanssa, mutta lisäksi :



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Noudata sitten macOS-osion vaiheita 3 ja 4.



#### Windowsissa



Asenna ensin Rust [rustup.rs](https://rustup.rs/) kautta ja käytä sitten PowerShelliä :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Identtinen konfiguraatio: kopioi `.env-sample` tiedostoon `.env` ja täytä parametrit.



### Mostro Mobilen asentaminen



#### Androidissa



**Vaihe 1**: Siirry [GitHubin julkaisusivulle](https://github.com/MostroP2P/mobile/releases) ja lataa **app-release.apk**-tiedosto (noin 65 MB).



![Page GitHub Releases](assets/fr/10.webp)



**Vaihe 2: Kun olet ladannut APK-tiedoston, avaa se latauksista. Android pyytää sinua hyväksymään asennuksen tästä lähteestä.



![Téléchargement et installation APK](assets/fr/11.webp)



**Vaihe 3**: Seuraa käyttöönottonäyttöjä, joissa esitellään toiminnot:




- Kauppa Bitcoin vapaasti - ei KYC** : Kaupankäynti ilman henkilöllisyyden todentamista Nostrin ansiosta
- Yksityisyys oletusarvoisesti**: Valitse maine-tilan ja täyden yksityisyyden tilan välillä
- Turvallisuutta joka askeleella**: Suojaus ei-hallinnollisilla pidätyslaskuilla



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Vaihe 4**: Jatka sisäänpääsyä löytääksesi :




- Täysin salattu keskustelu**: Päästä-päähän-salattu viestintä
- Tee tarjous**: Selaa tilauskirjaa ja valitse tarjous
- Etkö löydä tarvitsemaasi?** : Luo oma räätälöity tilaus



![Suite onboarding](assets/fr/13.webp)



**Vaihe 5: Kun sisäänkirjautuminen on valmis, sovellus luo automaattisesti Nostr-avainparin. Siirry valikkoon (☰) ja sitten **Tili** tallentaaksesi **Salaiset sanat** (palautuslauseke). Tässä näytössä sinulla on myös mahdollisuus vaihtaa aiemmin mainittu yksityisyydensuojatila.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Tärkeää**: Kirjoita palautuslauseke turvalliseen paikkaan (salasanahallintaohjelma, paperikaappi).



### Alkuperäinen turvallisuusmääritys



Mitä tahansa alustaa käytätkin :





- Oma avain**: Käytä erillistä Nostr-tunnusta kaupankäyntiä varten
- Pienet määrät**: Aloita alle sats 10 000:lla päästäksesi alkuun
- Useita releitä**: Määritä 3-5 maantieteellisesti erilaista relettä
- Verkon suojaus**: Aktivoi VPN tai Tor IP-osoitteesi piilottamiseksi
- Wallet turvallinen**: Aktivoi wallet Lightningin automaattinen lukitus



## Käyttö CLI:n kanssa



Tässä osassa esitellään bitcoinien ostaminen Mostro CLI:n kautta todellisen käyttötapauksen mukaisesti.



### Vaihe 1: Listaa käytettävissä olevat tilaukset



Komento `listorders` näyttää kaikki aktiiviset tilaukset:



```bash
mostro-cli listorders
```



Näet taulukon, jossa on kunkin tilauksen tiedot: Tunnus, tyyppi (osto/myynti), määrä, valuutta, maksutapa.



![Liste des ordres disponibles](assets/fr/05.webp)



Tässä esimerkissä on näkyvissä toimeksianto, joka koskee 5 euron myyntiä Revolutin kautta (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Vaihe 2: Tilauksen vastaanottaminen



Jos haluat ostaa näitä bitcoineja, ota tilaus `takesell` :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro pyytää sinua toimittamaan **Lightning-laskun** saadaksesi BTC:n. Tarkka määrä satosheina ilmoitetaan (tässä: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Vaihe 3: Toimita Lightning-laskusi



Luo wallet:stä (Phoenix:stä, Breezistä jne.) salamalasku, jossa on tarkka summa, ja lähetä se sitten :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



Järjestelmä vahvistaa lähetyksen ja kehottaa sinua odottamaan, että myyjä maksaa pidätyslaskun, ennen kuin voit aktivoida escrow-talletuksen.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Vaihe 4: Ota yhteyttä myyjään



Kun escrow on aktivoitu, pyydä myyjältä maksutiedot `dmtouser` -toiminnolla:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Vaihe 5: Hae vastaus



Tarkista suorat viestit nähdäksesi myyjän vastauksen:



```bash
mostro-cli getdm
```



Myyjä antaa sinulle maksutunnuksensa (tässä hänen Revtag-tunnuksensa: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Vaihe 6: Fiat-maksun suorittaminen



Lähetä maksu sovitulla menetelmällä (tässä esimerkissä Revolut) annettuihin yhteystietoihin. **Säilytä kaikki tositteet** (kuvakaappaukset, tapahtumaviitteet).



### Vaihe 7: Vahvista maksun lähetys



Kun maksu on suoritettu, ilmoita siitä Mostrolle :



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Vaihe 8: Bitcoinien vastaanottaminen



Heti kun myyjä vahvistaa fiatin vastaanottamisen ja vapauttaa escrow-komennon `release`-komennolla, saat bitcoinit välittömästi antamallasi Lightning-laskulla.



### Vaihe 9: Arviointi



Arvioi myyjä ja osallistu hajautetun maineen luomiseen:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Hyödyllisiä komentoja



**Tilauksen peruuttaminen** (ennen kuin se otetaan vastaan) :


```bash
mostro-cli cancel -o <order-id>
```



**Luo uusi myyntitilaus** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Avaa riita** :


```bash
mostro-cli dispute -o <order-id>
```



## Käyttö mobiilisovelluksen kanssa



Tässä osassa esitellään bitcoinien myynti Mostro Mobilen kautta todellisen käyttötapauksen avulla.



### Interface pääkone



Sovelluksessa on 3 päävälilehteä:





- Tilauskirja**: Selaa saatavilla olevia osto- (BUY BTC) ja myyntitoimeksiantoja (SELL BTC)
- Minun kaupat**: Näytä aktiiviset ja historialliset tilauksesi
- Chat**: Kommunikoi vastapuoliesi kanssa lukujen avulla



![Interface principale](assets/fr/14.webp)



### Suositeltava kokoonpano



Ennen kaupankäyntiä määritä muutama asetus valikosta (☰) > **Asetukset** :





- Salama Address** (valinnainen): Maksujen vastaanottaminen suoraan
- Releet**: (esim. `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Tarkista käyttämäsi Mostro-instanssin julkinen avain



![Paramètres de l'application](assets/fr/16.webp)



**Tärkeää CLI:n/Mobiilin synkronoinnin kannalta**: Jos käytät sekä CLI:tä että mobiilisovellusta, määritä **täsmälleen samat Nostr-releet ja Mostro Pubkey** molemmissa asiakkaissa. Ilman tätä identtistä konfiguraatiota et näe samoja tilauksia saatavilla molemmissa käyttöliittymissä. Asetuksissa näkyvien releiden ja Mostro Pubkey -avaimen (kuvakaappaus yllä) on vastattava CLI:n `.env'-tiedostossa olevia.



### Vaihe 1: Luo myyntitoimeksianto



Paina oikeassa alakulmassa olevaa vihreää **"+"**-painiketta ja valitse sitten **MYYNTI** (punainen painike).



![Boutons de création d'ordre](assets/fr/17.webp)



Täytä luomislomake :



1. **Valuutta**: Valitse haluamasi valuutta (EUR, USD jne.)


2. **Määrä** : Syötä summa fiat-määräisenä (esim. 1-3 euroa)


3. **Maksutavat** : Valitse maksutapa (esim. "Revolut")


4. **Hintatyyppi**: Valitse "Markkinahinta"


5. **Premium**: Säädä palkkio (liukusäädin -10% ja +10% välillä, suositus: 0% nopean myynnin vuoksi)



Julkaise tilauksesi painamalla **Submit**.



### Vaihe 2: Julkaisun vahvistaminen



Tilauksesi on nyt julkaistu! Se on saatavilla 24 tunnin ajan. Voit peruuttaa sen milloin tahansa ennen kuin ostaja ottaa sen vastaan suorittamalla `cancel`-komennon.



![Ordre publié](assets/fr/18.webp)



Toimeksianto näkyy **Minut kaupat** -välilehdellä tilassa "Vireillä" ja merkillä "Created by you".



### Vaihe 3: Ostaja ottaa tilauksesi vastaan



Kun ostaja ottaa tilauksesi vastaan, saat ilmoituksen. Katso yksityiskohdat kohdasta **Minut kaupat**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Tärkeä ohje**: Sinun täytyy nyt **maksaa näytetty pidätyslasku** lukitaksesi bitcoinisi (tässä 4674 sats 1-5 EUR:lle) escrowiin. Sinulla on **15 minuuttia aikaa**, muuten vaihto peruutetaan.



Kopioi pidätyslasku ja maksa se wallet Lightningista (Phoenix, Breez jne.).



### Vaihe 4: Kommunikoi ostajan kanssa



Kun escrow on aktivoitu, avaa salattu keskustelu ostajan kanssa painamalla **CONTACT**.



Ostaja (tässä "anonymous-gloriaZhao") ottaa sinuun yhteyttä ja pyytää maksutietojasi. Pyydämme sinua vastaamaan ja ilmoittamaan tietosi (Revtag, IBAN jne.).



![Chat avec l'acheteur](assets/fr/20.webp)



### Vaihe 5: Fiat-maksun vastaanottaminen



Odota, kunnes saat fiat-maksun Revolut-tilillesi (tai muulla sovitulla tavalla). **Tarkista huolellisesti**:




- Tarkka määrä
- Lähettäjä
- Viite, jos sitä pyydetään



Ostaja ilmoittaa sinulle chatissa, että hän on lähettänyt maksun. Mostro näyttää myös viestin, jossa vahvistetaan, että fiat on lähetetty sinulle.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Vaihe 6: Vapauta escrow



Kun olet **vahvistanut** fiat-maksun saapumisen tilillesi, paina vihreää **VAPAUTTAA**-painiketta ja vahvista lähettääksesi satssin ostajalle.



![Libération de l'escrow](assets/fr/20.webp)



Bitcoinit siirretään välittömästi ostajalle hänen Lightning-laskunsa kautta.



### Vaihe 7: Arvioi harkinta



Paina vapauttamisen jälkeen **RATE** arvioidaksesi ostajaa. Valitse 1 - 5 tähteä (tässä 5/5) ja paina **lähetä arvio**.



![Évaluation de la contrepartie](assets/fr/21.webp)



Vaihto on päättynyt!



### Osta bitcoineja mobiilisovelluksella



Bitcoinien **ostaminen** on samanlainen prosessi, mutta päinvastoin:



1. Selaa **Tilauskirja** > **OTA BTC** -välilehteä nähdäksesi myyntitilaukset


2. Klikkaa kiinnostavaa tilausta nähdäksesi yksityiskohdat


3. Paina **Toimita tilaus**


4. Toimita Lightning-lasku (joka on luotu wallet:stä)


5. Odota, että myyjä aktivoi escrow-järjestelmän


6. Ota yhteyttä myyjään **CONTACT** kautta maksutietoja varten


7. Lähetä fiat-maksu (säilytä todiste)


8. Myyjä vapauttaa escrow tarkistuksen jälkeen


9. Vastaanota bitcoineja välittömästi Lightning-laskuusi


10. Arvioi myyjää (1-5 tähteä)



### Ongelmien hallinta



**Tilauksen peruuttaminen**: Paina **My Trades** -kohdassa tilaustasi ja sitten **CANCEL**-painiketta (käytettävissä vain ennen kuin tilaus on otettu).



**Avaa riita**: Jos syntyy erimielisyys, paina **DISPUTE** tilauksen tiedoissa. Liitä mukaan kaikki todisteet (chatin kuvakaappaukset, pankkitapahtumaviitteet).



## Edut ja rajoitukset



### Edut



**Rahoituksellinen suvereniteetti**: Tämä poistaa valuutanvaihdon konkurssin tai piratismin riskin.



**Sensuurin kestävä**: Mikään viranomainen ei voi sulkea verkkoa tai sensuroida tilauksiasi. Järjestelmä toimii niin kauan kuin Nostrin releet ovat toiminnassa.



**Varusteellinen anonymiteetti**: Vain pseudonyymi Nostr-avain tunnistaa sinut ilman KYC- tai henkilötietoja. Päästä-päähän-salattu viestintä.



**Maksamisen joustavuus**: Kaikki yhteisesti hyväksytyt maksutavat ovat mahdollisia (tilisiirrot, mobiilisovellukset, käteinen, vaihtokauppa).



### Rajoitukset



**Varhainen kehitys**: Alkeelliset käyttöliittymät ja tekninen oppimiskäyrä vaaditaan.



**Rajoitettu likviditeetti**: Rajoitettu määrä toimeksiantoja, erityisesti suurten määrien tai harvinaisten valuuttojen osalta.



**Tekniset vaatimukset**: Lightning- ja Nostr-järjestelmien peruskäsitys.



**Kohtainen vastuu**: Ei keskitettyä tukea ongelmatilanteissa, varovaisuus tarpeen.



## Päätelmä



Mostro P2P on lupaava vaihtoehto keskitetyille pörsseille, sillä se yhdistää Lightning Network:n, Nostrin ja automaattisen escrow-talletuksen aidosti hajautettuun kaupankäyntiin. Huolimatta varhaisesta kehitysvaiheesta ja rajoitetusta likviditeetistä alusta tarjoaa jo nyt taloudellista suvereniteettia, sensuurin vastustuskykyä ja oletusarvoista anonymiteettiä.



Itsenäisyyttä ja luottamuksellisuutta arvostaville bitcoin-käyttäjille Mostro on varteenotettava vaihtoehto, jota kannattaa tutkia asteittain. Sen hajautettu arkkitehtuuri takaa pikemminkin yhteisöllisen kuin kaupallisen kehityksen, mikä tasoittaa tietä todella vapaiden Bitcoin-pörssien tulevaisuudelle.



## Resurssit



### Viralliset asiakirjat




- [Mostron virallinen verkkosivusto](https://mostro.network)
- [Tekninen dokumentaatio](https://mostro.network/docs-english/index.html)
- [Mostro-säätiö](https://mostro.foundation)



### Lähdekoodi ja kehitys




- [Pääasiallinen GitHub-arkisto](https://github.com/MostroP2P/mostro)
- [Web client](https://github.com/MostroP2P/mostro-web)
- [Asiakas CLI](https://github.com/MostroP2P/mostro-cli)



### Yhteisö




- [Nostr Protocol](https://nostr.com)
- [Lightning Network oppaat](https://lightning.network)