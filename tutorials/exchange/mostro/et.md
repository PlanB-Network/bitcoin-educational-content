---
name: Mostro
description: KYC-vaba Bitcoin P2P vahetusplatvorm Lightning ja Nostr kaudu
---

![cover](assets/cover.webp)



Kuidas omandada või müüa bitcoin'e ilma oma finantssuveräänsust ohustamata? Tsentraliseeritud platvormid kehtestavad invasiivseid KYC-protseduure, mis paljastavad teie isikuandmed, mille puhul on võimalik meelevaldne konto külmutamine või riiklik jälgimine.



**Mostro P2P** pakub detsentraliseeritud alternatiivi, mis ühendab Lightning Network, Nostr-protokolli ja ootearveid. Selle peamine uuendus: automatiseeritud deposiidisüsteem, kus teie bitcoinid jäävad kogu vahetuse vältel teie kontrolli alla, välistades varguse, vahetuse pankroti või omavolilise konfiskeerimise riski.



## Mis on Mostro P2P?



Mostro P2P on avatud lähtekoodiga Bitcoin vahetusprotokoll, mille on loonud **grunch**, 2021. aastal käivitatud populaarse Telegram-boti **lnp2pbot** arendaja. Kuigi lnp2pbot võimaldas juba KYC-vaba P2P vahetust Lightning'i kaudu, esitas see suure haavatavuse: **Telegram kujutab endast tsentraliseeritud tõrkepunkti**, mis on vastuvõtlik valitsuste tsensuurile.



Mostro kujutab endast selle kontseptsiooni **detsentraliseeritud arengut**: asendades Telegrami **Nostr**-protokolliga (hajutatud releede mittemääratav võrgustik), kõrvaldab Mostro selle süsteemse riski. Protokoll ühendab Lightning Network koheseid tehinguid, Nostr tsensuurikindlat suhtlust ja **hoidmisarveid**, et luua tõeliselt mittekaitstav automatiseeritud eskroo.



### Tehniline arhitektuur



Mostro töötab kolme komponendi kaudu:




- Daemon Mostrod**: koordineerib kasutajate ja Lightning Network vahelist teabevahetust
- Lightning**-sõlm: loob ootearved (~24h krüptograafiline eskroov)
- Mostro** kliendid: kasutajaliidesed (CLI, mobiilne, veeb)



Tellimused avaldatakse Nostris avalike sündmustena (tüüp 38383), samas kui privaatseid tehinguid edastatakse otsast lõpuni krüpteeritud sõnumite (NIP-59, NIP-44) kaudu. Iga Mostro instants määratleb oma tasud (tavaliselt vahemikus 0,3% kuni 1%) ja tehingulimiidid (sõltuvalt instantsist vahemikus paarist tuhandest kuni mitusada tuhat sats).



### Otsustavad eelised



**Tsensuurikindel**: Ükski valitsus ei saa Mostrot sulgeda, kui Nostr-relaisid on kuskil maailmas olemas. Erinevalt haavatavast lnp2pbotist Telegrami kaudu võimaldab Mostro vahetusi, mis on **tsensuurikindlad**.



**Escrow mittekaitstav**: Lightning hold-arved lukustavad teie bitcoinid ilma neid jäädavalt üle kandmata. Teie raha jääb teie kontrolli alla ja tagastatakse teile automaatselt probleemide korral (~24h).



**Konfidentsiaalsus algselt**: Kaks režiimi, mis sobivad teie vajadustele. Maine režiim** seob teie maine teie Nostr-võtmega, et luua püsiv usaldus. Täielik privaatne režiim** eelistab absoluutset anonüümsust ühekordse kasutusega efemeeriliste võtmetega.



## Peamised omadused



**Detsentraliseeritud teabevahetus**: Kõik tellimused avaldatakse Nostris krüptograafiliselt allkirjastatud sündmuste kaudu. Privaatseid läbirääkimisi edastatakse otsast lõpuni krüpteeritud sõnumite kaudu, mis tagab absoluutse konfidentsiaalsuse.



**Reputatsioonisüsteem**: 5-tärni reiting iteratiivse arvutusega, mis on püsivalt salvestatud Nostrisse. Võimaldab teil järk-järgult luua usaldusväärse kaupleja maine.



**Detsentraliseeritud vahekohtumenetlus**: Vaidluse korral uurib erapooletu vahekohtunik tõendeid ja teeb otsuse läbipaistvate kriteeriumide alusel. Iga vaidlus tekitab jälgitavuse tagamiseks unikaalse token.



**Maksmise paindlikkus**: Yadio.io vahetuskursi teenuse kaudu paljude fiat-valuutade toetus. Aktsepteerib SEPA ülekandeid, PayPali, Revoluti, sularaha ja kõiki osapoolte vahel kokkulepitud meetodeid.



## Mostro kliendid saadaval



Mostro pakub teie P2P vahetuste jaoks kaks peamist operatiivklienti.



### Mostro CLI - käsurea klient



**Mostro CLI** on kõige küpsem ja funktsionaalsem klient. See on kirjutatud Rust keeles ja pakub kõiki Mostro funktsioone käsurea kaudu. Ühildub macOSi, Linuxi ja Windowsiga.



** Peamised juhtimisseadmed** :




- "tellimuste nimekiri": Kuvada kõik olemasolevad tellimused
- `neworder` : Loo uus ostu- või müügikorraldus
- `takesell` / `takebuy`: Võtta ostu- või müügikorraldus
- `fiatsent`: Kinnitage fiat-makse saatmist
- "vabastamine": Vabastage eskroot ja lõpetage vahetus
- `getdm`: Otsesõnumite vaatamine
- `rate` : hinda oma vastaspoolt pärast vahetust



Ideaalne tehniliste kasutajate, automaatika ja maksimaalset ohutust nõudvate keskkondade jaoks.



### Mostro Mobile - nutitelefoni rakendus



**mobiilirakendus** alfa-versioonis võimaldab P2P kauplemist otse teie nutitelefonist. Intuitiivne graafiline Interface koos vahekaartidega navigeerimise, tellimuste vaatamise, täiustatud filtrite ja integreeritud chatiga, et suhelda oma vastaspooltega.



See on saadaval **Androidile** (GitHubi APK kaudu) ja on optimaalne valik kasutajatele, kes eelistavad lihtsust ja juhuslikku mobiilset kauplemist.



### Mostro-web - Interface web (arenduses)



Interface täiustatud JavaScript veebirakendus, mis on aktiivses arenduses. Mõeldud nii, et pakkuda täielikku kasutajakogemust koos ulatusliku kauplemis- ja portfellihaldusfunktsiooniga. Juurdepääs veebilehitseja kaudu ilma installimiseta.



## Paigaldamine ja konfigureerimine



See õpetus juhendab teid kahe peamise Mostro kliendi paigaldamise ja kasutamise kaudu: CLI ja mobiilirakendus.



### Olulised eeldused



Enne alustamist vajate :





- Töötav Lightning Network** wallet piisava likviidsusega (või Lightning-ühilduv)
 - Soovitatav: Phoenix, Breez, Wallet ja Satoshi...
 - Vähemalt 1000 satoshi likviidsust testimiseks



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Nostr** privaatne võti (formaat `nsec1...`)
 - Looge spetsiaalne kauplemisvõti [nostrkeygen.com](https://nostrkeygen.com/)
 - Oluline**: Ärge kunagi kasutage oma peamist isiklikku Nostr võtit
 - Hoidke oma isiklikku võtit turvalises kohas (paroolihaldur)





- Vabatahtlik, kuid soovitatav**: VPN- või Tor-ühendus IP-aadressi maskeerimiseks



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Mostro CLI paigaldus



#### MacOSis



**Samm 1: Rust kontroll**



Kontrollige, kas Rust on paigaldatud (nõutav versioon 1.64+):



```bash
rustc --version
```



Kui Rust ei ole paigaldatud :



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Samm 2: hoidla kloonimine**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Samm 3: Konfiguratsioon**



Kopeeri ja redigeeri :



```bash
cp .env-sample .env
```



Avage `.env` ja seadistage oma seaded:



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



**Vajalik CLI/Mobile** sünkroniseerimiseks: CLI ja mobiilirakenduses samadele tellimustele juurdepääsuks peate kasutama **sama Mostro Pubkey** ja **sama Nostr relee** mõlemas kliendis. Kontrollige neid seadeid mobiilirakenduse seadetes.



![Configuration .env](assets/fr/02.webp)



**Samm 4: Paigaldamine**



Koosta ja paigalda CLI :



```bash
cargo install --path .
```



Koostamine võtab 1-2 minutit. Käivitatav programm `mostro-cli` paigaldatakse faili `~/.cargo/bin/`.



![Installation du CLI](assets/fr/03.webp)



**Samm 5: Kontrollimine**



Kontrollige, et kõik töötaks:



```bash
mostro-cli --help
```



Te peaksite nägema tellimuste täielikku nimekirja.



![Vérification avec --help](assets/fr/04.webp)



#### Linuxis (Ubuntu/Debian)



Paigaldamine on identne macOSiga, millele on lisatud :



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Seejärel järgige samme 3 ja 4 jaotises macOS.



#### Windowsis



Installige esmalt Rust [rustup.rs](https://rustup.rs/) kaudu, seejärel kasutage PowerShelli :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Identne konfiguratsioon: kopeeri `.env-sample` faili `.env` ja täida oma parameetrid.



### Mostro Mobile paigaldamine



#### Androidis



**Samm 1**: Mine [GitHub release'i lehele](https://github.com/MostroP2P/mobile/releases) ja lae alla **app-release.apk** fail (umbes 65 MB).



![Page GitHub Releases](assets/fr/10.webp)



**Samm 2: Pärast allalaadimist avage APK-faili oma allalaadimistest. Android palub teil lubada paigaldamist sellest allikast.



![Téléchargement et installation APK](assets/fr/11.webp)



**Samm 3**: Jälgige sissejuhatusekraane, kus esitatakse funktsioonid:




- Bitcoin vabalt kaubelda - KYC puudub** : Kauplemine ilma isikutuvastamiseta tänu Nostr'ile
- Privaatsus vaikimisi**: Valige maine režiimi ja täieliku privaatsuse režiimi vahel
- Turvalisus igal sammul**: Kaitse mittekaitsvate kinnipidamisarvete abil



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Samm 4**: Jätkake sisseelamist, et avastada :




- Täielikult krüpteeritud vestlus**: Lõpust lõpuni krüpteeritud suhtlus
- Võtke pakkumine**: Sirvige tellimusraamatut ja valige pakkumine
- Ei leia seda, mida vajad?** : Looge oma kohandatud tellimus



![Suite onboarding](assets/fr/13.webp)



**Samm 5: Kui sisseelamine on lõpule viidud, genereerib rakendus automaatselt Nostr-võtmepaari. Minge menüüsse (☰) ja seejärel **Konto**, et salvestada oma **Saladussõnad** (taastumisfraas). Sellel ekraanil on teil ka võimalus muuta eelnevalt mainitud privaatsusrežiimi.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Tähtis**: Kirjutage oma taastamisfraas turvalisse kohta (paroolihaldur, paberkast).



### Esialgne turvakonfiguratsioon



Ükskõik, millist platvormi te kasutate :





- Spetsiaalne võti**: Kasutage kauplemiseks eraldi Nostr identiteeti
- Väikesed kogused**: Alustage vähem kui 10 000 sats, et alustada
- Mitu releed**: Konfigureerige 3-5 geograafiliselt erinevat releed
- Võrgukaitse**: Aktiveerige VPN või Tor, et varjata oma IP-aadressi
- Wallet turvaline**: Aktiveerige oma wallet välklambi automaatne lukustamine



## Kasutage koos CLI-ga



Selles jaotises näidatakse bitcoinide ostmist Mostro CLI kaudu vastavalt tegelikule kasutusjuhtumile.



### 1. samm: loetlege olemasolevad tellimused



Käsk `listorders` näitab kõiki aktiivseid tellimusi:



```bash
mostro-cli listorders
```



Näete tabelit iga tellimuse üksikasjadega: ID, tüüp (osta/müüa), summa, valuuta, makseviis.



![Liste des ordres disponibles](assets/fr/05.webp)



Selles näites on nähtav korraldus müüa 5 eurot Revoluti kaudu (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### 2. samm: tellimuse võtmine



Nende bitcoinide ostmiseks võtke tellimus `takesell` :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro palub teil esitada **Lightning arve**, et saada BTC. Täpne summa satoshides on märgitud (siin: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### 3. samm: esitage oma Lightning-arve



Looge oma wallet (Phoenix, Breez jne.) välkarvega arve täpse summa kohta ja saatke see :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



Süsteem kinnitab saadetise ja ütleb teile, et ootaksite, kuni müüja maksab kinnipidamisarve, enne kui aktiveerite eskroo.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### 4. samm: Võtke ühendust müüjaga



Kui eskroov on aktiveeritud, kasutage `dmtouser`, et küsida müüjalt makse üksikasju:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### 5. samm: Vastuse leidmine



Müüja vastuse nägemiseks kontrollige otsesõnumeid:



```bash
mostro-cli getdm
```



Müüja annab teile oma maksetunnuse (siin tema Revtag: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### 6. samm: Fiat-makse tegemine



Saatke makse kokkulepitud meetodi (antud näites Revolut) kaudu esitatud kontaktandmetele. **Hoidke kõik tõendavad dokumendid** (ekraanipildid, tehingu viited).



### Samm 7: Kinnitage makse saatmine



Kui makse on tehtud, teavitab Mostro :



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### 8. samm: bitcoinide kättesaamine



Niipea kui müüja kinnitab fiatraha kättesaamist ja vabastab käsuga `release` eskrovi, saate oma bitcoinid koheselt kätte teie esitatud Lightning-arvele.



### 9. samm: hindamine



Hinda müüjat, et aidata kaasa detsentraliseeritud mainele:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Kasulikud käsud



**Tellimuse tühistamine** (enne selle vastuvõtmist) :


```bash
mostro-cli cancel -o <order-id>
```



**Loo uus müügitellimus** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Avatakse vaidlus** :


```bash
mostro-cli dispute -o <order-id>
```



## Kasutamine koos mobiilirakendusega



Selles jaotises näidatakse bitcoinide müüki Mostro Mobile'i kaudu, järgides reaalset kasutusjuhtumit.



### Interface peamine



Rakendusel on 3 peamist vahekaarti:





- Tellimusraamat**: Sirvi olemasolevaid ostu- (BUY BTC) ja müügitellimusi (SELL BTC)
- Minu ametid**: Vaadake oma aktiivseid ja ajaloolisi tellimusi
- Vestlus**: Suhtle oma vastaspooltega arvude abil



![Interface principale](assets/fr/14.webp)



### Soovitatav konfiguratsioon



Enne kauplemist seadistage mõned seaded menüü kaudu (☰) > **Settings** :





- Välk Address** (valikuline): Makseid otse vastu võtta
- Releed**: Lisada mitu Nostr releed vastupidavuse tagamiseks (nt `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Kontrollige kasutatava Mostro instantsi avalikku võtit



![Paramètres de l'application](assets/fr/16.webp)



**Vajalik CLI/Mobile sünkroniseerimiseks**: Kui kasutate nii CLI kui ka mobiilirakendust, konfigureerige **täpselt samad Nostr-releed ja Mostro Pubkey** mõlemas kliendis. Ilma selle identse konfiguratsioonita ei näe te samu tellimusi, mis on saadaval mõlemas liideses. Seadetes (ülaltoodud ekraanipilt) nähtavad releed ja Mostro Pubkey peavad vastama teie CLI `.env' failis olevatele releedele ja Mostro Pubkey'le.



### Samm 1: Loo müügikorraldus



Vajutage rohelist **"+"** nuppu all paremal, seejärel valige **MÜÜDA** (punane nupp).



![Boutons de création d'ordre](assets/fr/17.webp)



Täitke loomevorm :



1. **Valuuta**: Valige valuuta, mida soovite saada (EUR, USD jne)


2. **Summa** : Sisestage summa fiat'is (nt 1 kuni 3 eurot)


3. **Makseviisid** : Valige meetod (nt "Revolut")


4. **Hinna tüüp**: Valige "Turuhind"


5. **Premium**: Reguleeri preemiat (liugur -10% kuni +10%, soovitatav: 0% kiireks müügiks)



Tellimuse avaldamiseks vajutage **Submit**.



### 2. samm: avaldamise kinnitamine



Teie tellimus on nüüd avaldatud! See on saadaval 24 tundi. Saate selle igal ajal tühistada, enne kui ostja selle vastu võtab, sooritades käsu `cancel`.



![Ordre publié](assets/fr/18.webp)



Tellimus ilmub vahekaardil **My Trades** staatusega "Pending" ja märgiga "Created by you".



### 3. samm: Ostja võtab teie tellimuse vastu



Kui ostja võtab teie tellimuse vastu, saate teate. Vaata üksikasju **Minu tehingud**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Tähtis juhis**: Te peate nüüd **maksma näidatud arve**, et lukustada oma bitcoinid (siin 4674 sats 1-5 EUR eest) deponeerimisele. Teil on aega **15 minutit maksimaalselt**, vastasel juhul tühistatakse vahetus.



Kopeerige kinnipidamisarve ja tasuge see oma wallet Lightning (Phoenix, Breez jne).



### 4. samm: Suhtle ostjaga



Kui eskroov on aktiveeritud, vajutage **CONTACT**, et avada ostjaga krüpteeritud vestlus.



Ostja (siin "anonymous-gloriaZhao") võtab teiega ühendust, et küsida teie makseandmeid. Palun vastake oma andmed (Revtag, IBAN jne).



![Chat avec l'acheteur](assets/fr/20.webp)



### 5. samm: Fiat-makse laekumine



Oodake, kuni saate fiat-makse oma Revolut-kontole (või muul kokkulepitud viisil). **Kontrollige hoolikalt**:




- Täpne summa
- Saatja
- Viide, kui seda taotletakse



Ostja teavitab teid vestluse kaudu, et ta on makse saatnud. Mostro kuvab ka sõnumi, mis kinnitab, et fiat on teile saadetud.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### 6. samm: vabastage eskroot



Kui olete **kinnitanud** fiat-makse laekumist oma kontole, vajutage rohelist **VÄLJENDAMINE** nuppu ja kinnitage, et saata satss ostjale.



![Libération de l'escrow](assets/fr/20.webp)



Bitcoins kantakse ostjale koheselt üle tema Lightning-arve kaudu.



### 7. samm: Hinda kaalutlust



Pärast vabastamist vajutage ostja hindamiseks **HINNANG**. Valige 1 kuni 5 tärni (siin 5/5) ja vajutage **Submit Rating**.



![Évaluation de la contrepartie](assets/fr/21.webp)



Vahetus on lõppenud!



### Osta bitcoine mobiilirakendusega



Bitcoinide **ostmise** protsess on sarnane, kuid vastupidine:



1. Müügitellimuste vaatamiseks sirvige **Tellimusraamat** > **OTSI BTC** vahekaart


2. Klõpsake huvitaval tellimusel, et vaadata üksikasju


3. Vajutage **Võta tellimus**


4. Esitage oma Lightning-arve (genereeritud teie wallet-st)


5. Oodake, kuni müüja aktiveerib eskroo


6. Võtke müüjaga ühendust **CONTACT** kaudu makse üksikasjade saamiseks


7. Saatke fiat-makse (hoidke tõend)


8. Müüja vabastab eskroo pärast kontrollimist


9. Saage bitcoinid kohe oma Lightning-arvele


10. Hinda müüjat (1-5 tärni)



### Probleemide haldamine



**Tellimuse tühistamine**: Vajutage **My Trades** oma tellimusele ja seejärel nupule **CANCEL** (saadaval ainult enne selle võtmist).



**Avatakse vaidlus**: Kui tekib erimeelsus, vajutage tellimuse üksikasjades **DISPUTE**. Lisage kõik tõendid (chat'i ekraanipildid, pangatehingu viited).



## Eelised ja piirangud



### Eelised



**Finantssuveräänsus**: Tänu arve hoidmise mehhanismile ei kao teie bitcoinid kunagi teie otsese kontrolli alt, mis välistab valuutavahetuse pankroti või piraatluse ohu.



**Tsensuurikindel**: Ükski asutus ei saa võrku sulgeda ega teie tellimusi tsenseerida. Süsteem töötab nii kaua, kuni Nostri releed toimivad.



**Vaikimisi anonüümsus**: Ainult pseudonüümne Nostr-võti tuvastab teid, ilma KYC- või isikuandmeteta. Lõpp-otsast lõpuni krüpteeritud side.



**Maksmise paindlikkus**: (ülekanded, mobiilirakendused, sularaha, barter).



### Piirangud



**Vaimne areng**: Vajalikud elementaarsed liidesed ja tehniline õppimine.



**Piiratud likviidsus**: Piiratud arv tellimusi, eriti suurte summade või haruldaste valuutade puhul.



**Tehnilised nõuded**: Nõutav on Lightning ja Nostr põhiteadmised.



**Isiklik vastutus**: Probleemide korral puudub tsentraliseeritud tugi, ettevaatust nõutakse.



## Kokkuvõte



Mostro P2P on paljulubav alternatiiv tsentraliseeritud börsidele, ühendades Lightning Network, Nostr ja automaatse deponeerimise tõeliselt detsentraliseeritud kauplemiseks. Hoolimata oma varajasest arengust ja piiratud likviidsusest pakub platvorm juba praegu finantssuveräänsust, tsensuurikindlus ja vaikimisi anonüümsust.



Bitcoini kasutajate jaoks, kes eelistavad autonoomiat ja konfidentsiaalsust, on Mostro elujõuline võimalus, mis väärib järkjärgulist uurimist. Selle detsentraliseeritud arhitektuur tagab pigem kogukonna kui ärilise arengu, sillutades teed tõeliselt vabade Bitcoin vahetuste tulevikule.



## Ressursid



### Ametlikud dokumendid




- [Mostro ametlik kodulehekülg](https://mostro.network)
- [Tehniline dokumentatsioon](https://mostro.network/docs-english/index.html)
- [Mostro Foundation](https://mostro.foundation)



### Lähtekood ja arendus




- [peamine GitHubi repositoorium](https://github.com/MostroP2P/mostro)
- [Veebiklient](https://github.com/MostroP2P/mostro-web)
- [Klient CLI](https://github.com/MostroP2P/mostro-cli)



### Ühendus




- [Nostr protokoll](https://nostr.com)
- [Lightning Network juhendid](https://lightning.network)