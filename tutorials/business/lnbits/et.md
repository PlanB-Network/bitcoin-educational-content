---
name: LNbits
description: Kaupmehe raamatupidamisplatvorm
---
![presentation](assets/lnbits-intro.webp)

# Raamatupidamissüsteem

LNbits on pakitud paljude vahenditega, et kontrollida ja suunata oma sissetulevaid ja väljaminevaid vahendeid, ühendada oma veebipood või isegi seadmed nagu riistvaraline rahakott või ATM, mille olete ise ehitanud. Kasutajatüüpide hulka kuuluvad:


- Rahakoti omanikud, kes soovivad kasutada LNbits'i oma vahendite haldamise ja selle lisafunktsioonide liidesena.
- Online- ja offline-kaupmehed või teenusepakkujad, kes soovivad aktsepteerida Bitcoini onchain- ja Lightning Network-makseid.
- Arendajad, kes soovivad luua Lightning Networki rakendusi.
- Sõlmeoperaatorid, kes soovivad integreerida oma sõlme LNbits-süsteemiga raamatupidamise eesmärgil.
- Kõigil neil on erinevad vajadused. Me ehitame LNbits'i modulaarselt, et iga kasutaja saaks meie funktsioone kasutada just endale sobival viisil.

# Rahakoti haldur

LNbits on vaba ja avatud lähtekoodiga raamatupidamissüsteem - mitte sõlmede haldur. Kanalihaldus on Lightning-sõlme valdkond, mis on ühendatud LNbitsiga kui rahastamisallikaga nagu LND või c-lightning. LNbits'i süsteemi superkasutajad või administraatorid vastutavad raamatupidamisfunktsioonide ja sisemiste laienduste üldise kättesaadavuse ja konfigureerimise eest.

LNbits toimib liidesena kasutaja ja Lightning-sõlme vahel, pakkudes lihtsat ja kasutajasõbralikku viisi maksevõrgu haldamiseks ja sellega suhtlemiseks.

Mõelge LNbitsist kui "wordpressi moodulraamistikust" teie sõlme jaoks. Lihtsalt hallatav platvorm, mis põhineb laiendustel, mida saate kombineerida paljude kasutusjuhtumite jaoks.

Mõelge LNbitsist kui oma panga finantsjuhtimise tarkvarast. Teie sõlmpunkt pakub kanaleid, mille kaudu maksta, ja LNbits laiendab teie sõlmpunkti, et saaksite kasutada rohkem kui ühte välgukassat, millega teie sõlmpunkt kaasas on. Need rahakotid ei pea tingimata kuuluma teile. Oletame, et teil kui LN-sõlme halduril on juba piisavalt kanali likviidsust ja vahendeid ning nüüd soovite pakkuda mõningaid bitcoin-pangateenuseid oma sõpradele, perele, oma poele või teistele tavakaupmeestele.

Pakute neile lihtsat võimalust avada "pangakonto" oma sõlmes, ilma et neil oleks juurdepääs teistele rahakottidele teie sõlmes ja kogu teie sõlme likviidsusele, kuid ainult nende osale. Teie sõlmpunkt (pank) toimib ainult transporditeenuse pakkujana nende maksete (sisse/välja) jaoks.

MÄRKUS: kõik rahalised vahendid, mida teie "kliendid" hoiavad oma LNbits pangakontodele teie sõlmes, lähevad otse teie sõlme LN kanalitesse. See tähendab, et SINA oled tegelikult nende vahendite tegelik omanik. Teil on suur vastutus nende vahendite eest. Ärge olge kurjad ja ärge põgenege rahaliste vahenditega, ärge olge kurjad ja ärge võtke kõrgeid tasusid. Me tahame fuck fiat banksters, mitte fuck üksteist (bitcoin kasutajad).

# Demo platvorm

Demo on leitav aadressil [https://legend.lnbits.com](https://legend.lnbits.com). See on täielikult toimiv ja seda saab kasutada Lightning Networki ning LNbits'i ja LNURLi funktsioonide tundmaõppimiseks üldiselt. Kuigi me ei saa seda takistada, palume teil seda mitte kasutada oma tootmisseadistuses. Me mitte ainult ei tööta sageli serverite kallal, et testida uusi funktsioone, vaid soovime ka julgustada teid oma sõlme ja LNbits'i suveräänselt käivitama. Kui te arvate, et oma sõlme käitamine on hetkel liiga palju küsitud, võite ühendada LNbits'i pilves asuva custodian funding sservice'iga nagu Opennode, Luna või Votage või Lightning Tipbot'iga Telegramis, et nimetada vaid mõned.

# LNbits flaier

Tahate anda mõne põhiinfo kaupmehele või ehitussõbrale üle ? Meil on väga hea meel teatada oma esimesest flaierist, mida igaüks saab kasutada. Suurus on ülemaailmselt tüüpiline flaierformaat 6 leheküljega (2 korda) ja laius 3508 ja kõrgus 2480px.

LNbits kaupmeeste jaoks: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)

LNbits ehitajatele: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)

# Mõned põhitõed

LNbits töötab LNURL-protokolli alusel, mis tähendab, et päringud kehtivad kahes vormis: kas https:// clearnet link (isesigneeritud sertifikaadid ei ole lubatud) või http:// v2/v3 onion link. Selleks, et pakkuda LNbits'i teenuseid, nagu LNURLp/w QR-koodid või NFC-kaardid, mida saab kasutada looduses, tuleb LNbits avada clearnetile (https).

Enne LNbits'i paigaldamist veenduge, et olete lugenud ja mõistnud järgmisi üldisi juhiseid selle kohta, mis on LNbits ja milliseid võimalusi see teile avab.


- [LND Guide](https://docs.lightning.engineering/) | LND paigaldamine
- [LND Config Example](https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | LND seaded
- [CLN Guide](https://docs.corelightning.org/docs/installation) | CLN-i paigaldamine
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Juhi vahitorn](https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower) | Väga oluline!

Üksikasjalikumad juhendid LNbits'i kasutamiseks konkreetsetes kasutusjuhendites siin:


- [Getting Started with LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Substack guide
- [ToDos teie ohutuse tagamiseks koos LNbitsiga](https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Erapangad Lightning Network'is](https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning) | Substack guide
- [Käivita oma sõpradele ja pereliikmetele rahakotid](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Substack guide
- [LNbits väikese restorani/hotelli jaoks](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Substack guide
- [LNbits Streamer copiloti kasutamine](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Substack guide
- [Alusta oma NOSTR turgu LNbitsiga](https://darthcoin.substack.com/p/lnbits-nostr-market) | Substack guide
- [LNbits'i kasutamine koolide projektides või festivalidel](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Substack juhend

# Paigaldage LNbits

## Põhiline paigaldusjuhend

LNbits'i saab paigaldada mis tahes Linux OS masinale. See ei nõua võimsat masinat või serverit, vaid lihtsalt piisavalt RAM-mälu ja veidi kettaruumi andmebaasi jaoks. Seda saab käivitada eraldi BTC/LN-sõlmest (kohalik arvuti või kaug-VPS) või koos sõlme või juba paigaldatud komplektsesse sõlme tarkvaraga masinasse.

Saate valida kõige levinumate paketihaldurite, nagu poetry ja nix, vahel. Vaikimisi kasutab LNbits andmebaasina SQLite'i. Võite kasutada ka PostgreSQL-i, mida soovitatakse suure koormusega rakenduste puhul. [Siin on juhend põhiinstallatsiooni jaoks, kasutades poetry või nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).

Kõigile, kes on uued, leiate üksikasjalikumaid samm-sammult juhiseid LNbits'i käivitamiseks konkreetsetes keskkondades:


- [LNbits on clearnet](https://ereignishorizont.xyz/lnbits-server/en/) poolt Axel
- [LNbits on VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes
- [LNbits on cloudflare](https://www.nodeacademy.org/lnbits) poolt Leo

Samuti leiate video [dockerised Setup on a VPS koos PostgreSQ, LightningTipBot kui rahastamisallikas kasutades nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).

[Rohkem paigaldusstsenaariume siin](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).

Komplektide tarkvarasõlmede puhul vaadake nende spetsiifilist dokumentatsiooni LNbits'i kohta: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)

## LNbits SaaS

Kui te ei ole huvitatud tehnilistest asjadest ega soovi ise oma rahastamisallikat ega lnbits'i hallata, siis on olemas [LNbits SaaS versioon](https://saas.lnbits.com) (Software-as-a-service), mida saate kasutada. See on põhimõtteliselt nagu LNbits pilves, kuid te saate ise määrata rahastamisallika (nt oma Node, LNbits'i rahakott, LNtipbot, fakewallet jne) ja keskkonnamuutujad - mida teiste pilvelahenduste puhul enamasti ei ole.

[Siin on üksikasjalik juhend, kuidas kasutada LNbits SaaSi konkreetsete kasutusjuhtumite puhul](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).

## Rahastamisallikad

LNbits ei ole sõlme haldustarkvara, vaid LN-keskne raamatupidamissüsteem LND või CLN rahastamisallika peal. Pärast esimest paigaldamist saate oma LNbits'i külastada aadressil http://localhost:5000/.

Rahastamisallika muutmiseks minge oma super-user-URL-i ja valige rahastamisallikas "Manage Server" kaudu või redigeerige .env-faili, muutes `LNBITS_BACKEND_WALLET_CLASS` oma vajalikuks allikaks, kui olete `.env'is seadnud `adminUI=TRUE`.

Sa leiad .env faili oma lnbits/ või lnbits/apps/data kaustast, laiendades käsku oma kataloogis olevate failide loetlemiseks käsuga `ls -a`.

Samuti võib olla vaja paigaldada lisapakette või teha täiendavaid seadistamisetappe, valides soovitud rahastamisallikas. Pärast taaskäivitamist on teie uus seadistus aktiivne.

Milliseid rahastamisallikaid saan kasutada LNbits'i jaoks?

LNbits võib töötada paljude välkkiirte võrgu rahastamisallikate peal. Praegu on olemas tugi CoreLightningile, LND-le, LNbitsile, LNPayle, OpenNode'ile ja regulaarselt lisandub veel rohkem.

Oluline on valida allikas, millel on hea likviidsus ja head kolleegid, kes on ühendatud. Kui kasutate LNbits avalike teenuste jaoks, saavad teie kasutajate maksed ainult siis voolata õnnelikult mõlemas suunas.

Backend rahakoti (rahastamisallikas) saab konfigureerida, kasutades järgmisi LNbits keskkonnamuutujaid failis `.env` või oma peakasutajakontol jaotises Manage-Server.

Kui soovite kasutada .env-versiooni, leiate parameetrid siit:

### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/path/lightning-rpc
- Säde (c-pilv)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - `SPARK_TOKEN`: secret_access_key

### Lightning Network Daemon


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - "LND_REST_CERT": /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon või Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_aadress
  - `LND_GRPC_PORT`: port
  - "LND_GRPC_CERT": /file/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon või Bech64/Hex

Selle asemel võite kasutada ka AES-krüpteeritud makrooni (rohkem infot), kasutades selleks


  - "LND_GRPC_MACAROON_ENCRYPTED": eNcRyPtEdMaCaRoOn

Makaronide krüpteerimiseks käivitage `./venv/bin/python lnbits/wallets/macaroon/macaroon/macaroon.py`.

### LNbits (teine LNbits'i instants)


- LNbits'i instants, mis asub pilveserveris või teie enda koduserveris
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Server (!! Ärge kasutage seda mitte tootmises / ärilistel eesmärkidel, vaid ainult testimiseks !!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### Välk TipBot

Selleks, et ühendada oma [Lightning Tipbot](https://t.me/LightningTipBot) Telegramist, peate seadistama järgmise parameetri:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://ln.tips
  - `LNBITS_KEY`: Võtme saamiseks peate kord käivitama /api privaatses vestluses LightningTipbotiga Telegramis.

Vaata ka seda õpetust, kuidas paigaldada [LNbits koos LightningTipBotiga vps kaudu](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)

### IBEX HUB

Registreeru [siin](https://ibexpay.ibexmercado.com/onboard) ja saad sealt oma võtmed/tokumendid, lõpp-punkt on https://ibexpay-api.ibexmercado.com.

Rohkem infot vt [IBEX API-dokumentatsioon](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).

### LNPay

Selleks, et arve kuulaja töötaks, on teil LNbitsis avalikult ligipääsetav URL ja te peate looma [LNPay webhook](https://dashboard.lnpay.co/webhook/), mis osutab `<oma LNbits host>/wallet/webhook` sündmusega "Wallet Receive" ja ilma saladuseta. Seadistus `https://mylnbits/wallet/webhook` on lõpp-punkti url, mida teavitatakse igast maksest.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey

### OpenNode

Selleks, et arve toimiks, peab teie LNbitsis olema avalikult ligipääsetav URL-aadress. Veebikonksu seadistus on vabatahtlik.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey

### Alby

Alby on brauseripikendus, millel on LN rahakoti funktsioonid ja LNDHUBi konto, mida saab kasutada LNbitside rahastamisallikana. [Täpsemalt siin](https://getalby.com/).

Selleks, et arve toimiks, peab teil olema avalikult ligipääsetav URL-aadress LNbitsis. Käsitsi veebikonksu seadistamine ei ole vajalik. Alby juurdepääsutunnuse saate genereerida siin: https://getalby.com/developer/access_tokens/new


- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken

## Täiendavad / tõrkeotsingu juhendid

Siin on mõned täiendavad juhised juhuks, kui teil on neid vaja. Klõpsake noolele, et laiendada kirjeldust.

### The Killswitch 🚨

Viimasel ajal on olnud nii palju ohtlikke vigu mitte ainult kogu kosmoses, vaid ka LNbitsis, et otsustasime midagi ette võtta. Nüüd saate valida hoiatuste ja/või otseste meetmete võtmise, kui haavatavus või viga, mis võib viia raha kaotamiseni, uuesti esineb.

![killswitchn](assets/lnbits-killswitch.webp)

Kui lülitatakse void-walletile, näevad kõik kasutajatüübid instantsil kollase bänneri, kus tavaliselt on "LNbits on beeta" teade teema/keele ala kõrval paremal - ja see on kõige ilmsem vihje, et midagi on juhtunud. Vaadake oma uut serverilehte, mis on akna vasakpoolses osas roheliselt esile tõstetud.

Kuidas see toimib ? Kui killswitch on sisse lülitatud, kontrollitakse X-minutilise intervalliga (mida saab määrata) salajast githubi repositooriumi, mis on kättesaadav ainult LNbits'i tuumikmeeskonnale. Kui selles repositooriumis avaldatakse haavatav viga, on see signaaliks, mis käivitab killswitch'i kõikides installatsioonides, mis on selle tellinud, ja muudab teie lnbits'i instantsi tühja rahakoti kasutamiseks. Kui pilved on puhastatud ja te olete paigaldanud turvavärskenduse, saate oma rahastamisallikaks määrata oma sõlme, rahakoti või mida iganes te kasutate, uuesti ka jaotise Manage Server kaudu. Selles wikis on jaotis rahastamisallikate vahetamise kohta, kui te ei tea, mida seadistada.

### Erinevus administraatori ja superkasutaja vahel

LNbits Admin UI võimaldab teil muuta LNbits'i seadeid LNbits'i kasutajaliidese kaudu. See on vaikimisi välja lülitatud ja kui te esimest korda seadistate failis `.env` muutuja `LNBITS_ADMIN_UI=true`, siis seaded initsialiseeritakse ja neid hakatakse kasutama. Edaspidi kasutatakse andmebaasi vastavaid seadistusi .env faili asemel.

### Super kasutaja

Koos Admin UI me kasutusele super kasutaja, mis on juurdepääs server nii saab muuta seadeid, mis võib krahhi server või teha seda reageerimata kaudu frontend ja api, nagu nt muutes rahastamise allikas. Superkasutaja on salvestatud ainult andmebaasi seadete tabelis. Pärast seadete "lähtestamist" ja taaskäivitamist luuakse uus superkasutaja. Samuti lisasime API marsruutidele dekoraatori, et kontrollida superkasutajate olemasolu. Selle ID-d ei saadeta kunagi üle api ja frontend ja saab ainult bool (jah/ei), kas olete super kasutaja või mitte.

Ainult superkasutajal on lubatud brrrr satoshis erinevatele rahakottidele "Top Up" sektsiooni kaudu.

Samuti saate veebikonksu kaudu postitada superkasutajat teise teenusesse, kui see on loodud. Rohkem infot siin https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`

Frontendist leiate ka võimaluse muuta poe pilti, mis kuvatakse "loo rahakott" lehel, avades jaotise Manage Server ja valides Theme -> Custom Logo.

### Administraatori kasutajad

Keskkonna muutuja: lNBITS_ADMIN_USERS, komadega eraldatud kasutajatunnuste nimekiri: `LNBITS_ADMIN_USERS`. Administraatorikasutajad saavad muuta seadistusi admin ui's - välja arvatud rahastamisallikate seaded, sest see nõuaks serveri taaskäivitamist ja võib muuta serveri ligipääsmatuks. Samuti on neil juurdepääs kõikidele neile määratud laiendustele, mis on kirjas `LNBITS_ADMIN_EXTENSIONS`.

### Lubatud kasutajad

Keskkonna muutuja: lNBITS_ALLOWED_USERS, komadega eraldatud kasutajate ID-de nimekiri. Nende kasutajate määratlemisel ei ole LNbits enam avalikult kasutatav. Ainult määratletud kasutajad ja administraatorid saavad seejärel LNbits'i frontendile ligi.

#### LNbits'i ajakohastamine

LNbits'i kohaliku instantsi tavaline uuendamine toimub lihtsalt järgmiste CLI käskude kopeerimise ja kleepimise teel:

```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```

Kui te kasutate Raspiblitz'i või MyNode'i, siis võib teil olla lisaks vaja ka

```
sudo systemctl restart lnbits
```

lõpus, sest LNbits töötab teenusena.

Umbrel/Citadellis on käsud järgmised

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```

#### SQLite'i migratsioon PostgreSQL-i

Kui LNbits on juba paigaldatud ja töötab SQLite'i andmebaasis, soovitame tungivalt üle minna postgres'ile, kui kavatsete LNbits'i kasutada mastaapselt.

Seal on lisatud skript, millega saab migratsiooni hõlpsasti teha. Sul peab olema Postgres juba installeeritud ja seal peaks olema kasutaja parool (vt Postgres'i paigaldamise juhendit eespool). Lisaks peab teie LNbits'i instants kord käivituma Postgres'ile, et rakendada andmebaasi skeemi, enne kui migratsioon saab toimida:

```
# STOP LNbits
# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit
# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Loodetavasti töötab nüüd kõik ja saab migreeritud... Käivitage LNbits uuesti ja kontrollige, kas kõik töötab korralikult.

#### Andmebaasi varundamine ja taastamine

Palun lugege [seda väga üksikasjalikku juhendit varundamise ja taastamise protsessi kohta](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).

#### Minu LNbits'i rahakoti rahastamine minu sõlme kaudu ei toimi

Kui soovite saata sati samast sõlmest, mis on teie LNbiti rahastamisallikaks, peate muutma faili lnd.conf.

Lisatavad parameetrid on järgmised: `allow-circular-route=1`

Palun tehke seda oma lnd.conf-i jaotises Application options. Mõnes kimbu sõlmes võib LND käivitamine muidu ebaõnnestuda.

MÄRKUS: LNbits'i kontole raha lisamiseks on soovitatav kasutada uut adminUI laiendust koos valikuga "TopUp".

#### Viga 426

Ma sain vea: "lnurl tuleb edastada üle avalikult ligipääsetava https-domeeni või tor. 426 upgrade required"</summary>

See viga tuleneb tavaliselt sellest, et teie LNbits ngnix-tunneli taga ei edasta LNURL-aadressi õigesti. Peatage oma LNbits ja redige .env faili, lisades selle rea:

`FORWARDED_ALLOW_IPS=*`

Samuti kui kasutate ngnixi seadistust, veenduge, et teil on need päised ngnixi konfiguratsioonis:

```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```

#### Võrgu viga

Ma sain "https error", võrguviga" või muud, kui ma skaneerin QR</summary>

Halb uudis, see on marsruutimisviga, millel võib olla üsna palju põhjusi. Kõigepealt kontrollige QR´i LNURL-i [Lightning Decoder](https://lightningdecoder.com/) abil, kas leiate sealt midagi imelikku. Proovime mõned kõige võimalikud probleemid ja nende lahendused.

LNbits töötab ainult Tori kaudu, sa ei saa seda avada avalikus domeenis nagu lnbits.yourdomain.com


- Arvestades, et soovite, et teie seadistus jääks selliseks, avage oma LNbits'i rahakott, kasutades .onion URI-d ja looge see uuesti. Sel moel luuakse QR, mis on kättesaadav selle .onion URI kaudu, seega ainult tor'i kaudu. Ärge genereerige seda QR-i .local URI-st, sest see ei ole Interneti kaudu kättesaadav - ainult oma koduse LANi kaudu.
- Avage oma LN rahakoti rakendus, mida kasutasite selle QR-koodi skannimiseks, ja kasutage seekord tor'i (vt rahakoti rakenduse seaded). Kui rakendus ei paku tor'i, võite selle asemel kasutada Orbot (Android). Vaata paigaldamise jaotises üksikasjalikke juhiseid, kuidas avada oma LNbits clearnet/https jaoks.

#### Vältida teiste rahakottide genereerimist minu LNbitsidel

Kui te käivitate oma LNbits clearnetis põhimõtteliselt igaüks saab luua rahakoti selle kohta. Kuna teie sõlme rahalised vahendid on seotud nende rahakottidega, siis võiksite seda vältida. Selleks on kaks võimalust:

Konfigureeri lubatud kasutajad ja laiendused failis `.env` ([vaata env näide siit](https://github.com/lnbits/lnbits/blob/main/.env.example)). See toimib ainult siis, kui kasutate .env failis seadistust `adminUI=FALSE`, muidu peate seda tegema jaotises Manage Server -> Users -> Allowed Users. Kõiki teisi ei lubata pärast seda.

#### Kohandada arve aegumise aega

Nüüd saate koostada kohandatud kehtivusajaga arveid. Ühildub backendidega: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet siiani: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet!

Saate määrata `LIGHTNING_INVOICE_EXPIRY` oma .env failis või kasutada AdminUI-d, et muuta kõigi arvete vaikeväärtust. Samuti on uus väli /api/v1/payments lõpp-punktis, kus saate määrata JSON-andmetes aegumistähtaega.

## Wallet-URL välja jäetud

### Rahakott demo serveril legend.lnbits

Salvesta alati oma rahakoti-URL-i, Export2phone-QR-i või LNDhub-i koopia oma rahakoti jaoks turvalisse kohta. LNbits EI AITA teid nende kaotamise korral taastada.

### Rahakott oma rahastamisallikas/sõlm

Salvesta alati oma rahakoti-URL-i, Export2phone-QR-i või LNDhub-i koopia oma rahakoti jaoks turvalisse kohta. Kõik LNbits'i kasutajad ja rahakoti-IDd leiad LNbits'i kasutajahalduri laiendusest või sqlite'i andmebaasist. LNbits'i andmebaasi muutmiseks või lugemiseks minge LNbits'i /data kausta ja otsige fail nimega sqlite.db. Saate seda avada ja redigeerida Exceliga või spetsiaalse SQL-redaktoriga nagu [SQLite browser](https://sqlitebrowser.org/).

Samuti saate klipi kaudu rahakotid välja lasta ja vaadata iga rahakotti oma andmebaasis.

```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```

Väljund näeb välja umbes nii

```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

ja sa tahad need väärtused panna url-i, näiteks niimoodi

```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```

Seejuures asendate f8a43fc363ea428db5c53b3559935f1f nime ees oleva väärtusega (meie näites f8a43fc363ea428db5c53b3559935f1f) ja 1280ff5910a9c485a782a2376f338b6c on teie kasutaja ja peaks saama nime järel olevaks väärtuseks. Sqlite3 lõpetamiseks sisestage

```
.quit
```

#### LNURL jaoks välk-aadressi vastupidi

Proovi seda [kodeerijat](https://lnurl-codec.netlify.app/) fiatjafilt või [seda](https://lightningdecoder.com/). LNURLp maksmiseks või kontrollimiseks võite samuti kasutada [LNurlpay](https://wwww.lnurlpay.com/). Seal peaks olema märgitud HTTPS EI HTTP.

#### Konfigureeri kommentaar, mida inimesed näevad, kui nad maksavad minu LNURLp QR-le

LNURL-p loomisel ei täideta vaikimisi kommentaari kasti. See tähendab, et kommentaaride lisamine maksetele ei ole lubatud.

Kommentaaride lubamiseks lisage kasti tähemärkide pikkus 1 kuni 250. Kui panete sinna numbri, kuvatakse kommentaarikast maksmise käigus. Võite ka muuta juba loodud LNURL-p ja lisada selle numbri.

![lnbits comments](assets/lnbits-comments.webp)

#### Deponeeri onchain BTC LNbits'ile

On kaks võimalust vahetada satsid onchain BTC-st LN BTC-ks (või LNbitsiks).

##### Välise vahetusteenuse kaudu.

Teised kasutajad, kellel ei ole juurdepääsu teie LNb-le, saavad kasutada vahetusteenust nagu [Boltz](https://boltz.exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) või [ZigZag](https://zigzag.io/). See on kasulik, kui te esitate oma LNbits'i instantsist ainult LNURL/LN-arveid, kuid maksjal on ainult onchain-satid, nii et ta peab need satsid kõigepealt omalt poolt vahetama. Protseduur on lihtne: kasutaja saadab swapteenusele onchain btc ja annab swapi sihtkohaks LNURL/LN arve LNbitsilt.

##### Kasutades Onchaini ja Boltzi LNbiti laiendust.

Pidage meeles, et see on eraldi rahakott, mitte LN btc, mida LNbits esindab kui "teie rahakotti" teie LN rahastamisallikas. Seda onchain rahakotti saab kasutada ka LN btc vahetamiseks (nt teie hardwarewallet), kasutades LNbits Boltz või Deezy laiendust. Kui teil on veebipood, mis on seotud teie LNbitsiga LN maksete jaoks, on väga mugav regulaarselt tühjendada kõik satsid LN-ist onchaini. See toob kaasa rohkem ruumi teie LN-kanalites, et saaksite uusi värskeid sats'e vastu võtta.

Menetlus neile, kellel puudub bitcoini riistvaraline rahakott:


- Kasutage Electrumi või Sparrow rahakotti, et luua uus onchain rahakott ja salvestada varukoopia seemne turvalisse kohta.
- Mine rahakoti infolehele ja kopeeri xpub.
- Mine LNbits - Onchaini laiendusse ja loo uus ainult kellale mõeldud rahakott koos selle xpubiga.
- Mine LNbits - Tipjar laiendus ja loo uus Tipjar. Valige lisaks LN rahakotile ka valik onchain.
- Valikuline - Mine LNbits - SatsPay laiendusele ja loo uus tasu onchain btc jaoks. Saate valida onchain ja LN või mõlemad. Seejärel loob see arve, mida saab jagada.
- Valikuline - Kui kasutate oma LNbits'i, mis on seotud Wordpress + Woocommerce lehega, siis kui loote/linkite ainult kellale mõeldud rahakoti oma LN btc poe rahakotiga, on kliendil mõlemad maksevõimalused samal ekraanil.

Kui saate LNbitsis makse, kuvatakse tehingulogis ainult tehingu jätkuv tüüp.

![lnbits payment details](assets/lnbits-payment-details.webp)

Teie tehinguülevaates näete väikest rohelist noolt saadud ja punast noolt saadetud raha kohta.

Kui klõpsate nendel nooltel, kuvatakse lisatud sõnumeid ja saatja nime (kui see on olemas).

Määrata nimi, et see ilmuks maksete sees, LNbitsis ei ole seda praegu võimalik teha - kuid saada. See on võimalik ainult siis, kui saatja LN rahakott toetab [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) nagu [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).

Seejärel näete oma LNbits-tehingute üksikasjade sektsioonis (klõpsake nooltele) varjunime/pseudonüümi. Pange tähele, et võite anda seal mis tahes nime ja see ei pruugi olla seotud tegeliku saatja nimega, kui te saate sellise nime.

![lnbits namedesc](assets/lnbits-namedesc.webp)

Selleks, et importida oma LNbits-konto rahakoti rakendusse, avage oma LNbits koos konto / rahakotiga, mida soovite kasutada, minge "manage extensions" ja aktiveerige LNDHUB laiendus. Avage LNDHUBi laiendus, valige rahakott, mida soovite kasutada, ja skaneerige kas "admin" või "ainult arve" QR, olenevalt sellest, millist turvataset soovite selle rahakoti jaoks.

Võite kasutada [Zeus](https://zeusln.app/) või [Bluewallet](https://bluewallet.io/) kui rahakoti rakendusi lndhubi konto jaoks, kusjuures BW toetab rohkem kui ühte sellist rahakotti.

Seda tehes soovitame määrata LN-võrgu URI ka teie enda sõlme URI-ks. Kui teie LNbits'i instants on ainult Tor, peate kasutama ka neid rakendusi, mille Tor on aktiveeritud. Ka sel juhul peate LNbits'i lehe avama oma Tor .onion-aadressi kaudu.

Kui teil ilmneb viga "toetamata hash-tüüp", kui kasutate ypubi On-chain laienduses, kontrollige, kas teie LNbits kasutab python 3.10, see võib olla mõjutatud [sellest probleemist](https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python). Muuda openssl.cnf nagu kirjeldatud stackoverflow'i vastuses ja käivita oma LNbits uuesti.

## Tööriistade valmistamine ja ehitamine LNbitsiga

LNbitsil on igasuguseid [avatud APIsid](https://legend.lnbits.com/docs) ja vahendeid, et programmeerida ja ühendada palju erinevaid seadmeid, mis on mõeldud tuhandete eri kasutusviiside jaoks.

Kui te olete uus ehitamine alustada selle [MakerBits esitlused](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) Ben Arc umbes hoone vidinaid põhineb LNbits.

### TÄHELEPANU:


- LNbits töötab LNURL-protokolli alusel, mille taotlused kehtivad kahel kujul: kas https:// clearnet link (isesigneeritud sertifikaadid ei ole lubatud) või http:// v2/v3 sibulalink. Selleks et pakkuda LNbits'i teenuseid, nagu LNURLp/w QR-koodid või NFC-kaardid, mida saab kasutada looduses, tuleb LNbits avada clearnetile (https).
- Kasutage esp32 toiteks ainult DATA-kaableid. Mitte kõik kaablid ei toeta lisaks esp-i toitele ka andmeid. Te ei oleks esimene, kui esp-ga kaasasolev kaabel on ainult toiteallikaks
- Veenduge, et te ei kasuta USB-keskust, millele on ühendatud teisi seadmeid. See võib põhjustada kummalisi efekte, mida on raske kõrvaldada (nt ei käivitu või ei peatu).
- Esp-projektide realiseerimiseks MacOSiga on vaja UART Bridge Driver'i. Kui sul on probleeme draiveriga Mac või Linux süsteemides, leiad need siit või, kui tegemist on TTGO ekraaniga, siis siit. Kui olete windowsis ja teil on probleeme ühendamisega, siis laadige kindlasti alla VANA versioon 11.1.0, sest uuem versioon ei tööta! Samuti leiate siit jadaterminali, et kontrollida oma ühendust - seadistage baudrate 115200.
- Kuigi Platform.io kasutamine on palju mugavam (nt sõltuvused paigaldatakse automaatselt), soovitame kõigile, kes alles alustavad ehitamist, kasutada Arduinot.
- TT-Go Display S3: Ekraanikaitsekile vahekaardi värvus näitab, millise kontrolleri (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..) abil on see täpselt valmistatud. Hoidke seda, et oleks võimalik siluda, kui te ise programmeerite ja ekraan ei näita graafikat õigesti, nt värvid valesti, peegelpildid või eksivad pikslid servades. Kui teil on kunagi vaja seda teha, on olemas eepiline juhend erinevate ekraanide jaoks kohandamise kohta
- Kasutage alati väikseid tähti lnurl239xx asemel LNURLl239xx
- Lightning:lnurl1234xyz lisamine loob QR-i, mis taotleb skannimisel kasutaja rahakoti avamist selle arve jaoks (iOS-is viimati installitud välk rakendust, Androidis seadistus)
- Kui te vilgub esp32 kaudu veebi töötab ainult nende brauserite (TL:DR Chrome, Edge & Opera).
- Palun võtke arvesse seda PIN-OUT viide esp
- Kui kasutate FOSSoftware või FOSGuides pls alati linkida autor. Kõigile meeldib vaadata, kuidas nende laps kasvab ja see algatab ka ehitamise ahela, mida on üsna vinge vaadata :)

Tule [Makerbits Telegram Groupi](https://t.me/makerbits), kui vajad abi mõne projektiga - me aitame sind!

![lnbits hackathlon](assets/lnbits-hackathlon.webp)

Siin on mõned projektikategooriad, mida saate LNbitsiga ehitada:


- [Nostr Signing Device](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lamp](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Riistvara rahakott](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-switch)
- [müügiautomaat](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora ja võrkude võrgustik](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)
- [ABIMEHED JA RESSURSID](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Rohkem näiteid "Powered by LNbits" projektide kohta siin](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [LNbits'i kasutusjuhtumid](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)