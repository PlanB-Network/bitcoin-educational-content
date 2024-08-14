---
nimi: RaspiBlitz
kirjeldus: Juhend oma RaspiBlitzi seadistamiseks
---

![pilt](assets/0.webp)

RaspiBlitz on tee-ise Lightning Node (LND ja/või Core Lightning), mis töötab koos Bitcoin-Fullnode'iga RaspberryPi peal (1TB SSD) ja ilusa ekraaniga lihtsaks seadistamiseks & jälgimiseks.

RaspiBlitzi peamine sihtgrupp on õppida, kuidas oma sõlme kodus detsentraliseeritult käitada - sest: Kui pole sinu Sõlm, pole sinu Reeglid. Avasta & arenda Lightning Networki kasvavat ökosüsteemi, saades selle täieõiguslikuks osaks. Ehita see osana töötoast või kui nädalavahetuse projekt ise.

![video](https://youtu.be/DTHlSPMz3ns)
RASPIBLITZ - Kuidas käitada Lightning ja Bitcoin Full Node'i BTC sessiooni poolt

# Parmani Raspiblitzi seadistamise juhend

Raspiblitz on suurepärane süsteem Bitcoin Node'i ja sellega seotud rakenduste käitamiseks. Soovitan seda ja My Node node'i enamikule kasutajatele (ideaalis omage kahte sõlme redundantsuse jaoks.) Üks suur eelis on see, et Raspiblitzi sõlm on "Tasuta Avatud Lähtekoodiga Tarkvara", erinevalt MyNode'ist või Umbrel'ist. Miks see on oluline? Vlad Costa selgitab. Samuti võid RaspbiBlitzi käitada WiFi ühendusega, mitte etherneti kaudu – siin on selleks täiendav juhend. (MyNode'iga seda teha ei ole ma leidnud.)

Võid osta valmis sõlme koos külge kinnitatud mini ekraaniga, või võid selle ise ehitada (ekraani pole vaja).

Githubi lehel olev juhend on suurepärane, kuid võib-olla liiga detailne mõõdukalt kogenud kasutajale. Minu juhised on lühemad ja loodetavasti lihtsamini järgitavad.

Põhimõtteliselt on protsess väga sarnane MyNode node'i seadistamisega Raspberry Pi 4-ga. Raspiblitzi juhend soovitab osta monitori, kuid tegelikult pole seda vaja ja ma ei soovitaks seda. Sul pole isegi vaja lisaklaviatuuri või hiirt. Lihtsalt pääse seadme terminali menüüsse juurde arvuti kaudu samas koduvõrgus ja kasuta ssh käsku terminalis. See on võimalik Linux/Mac'iga (lihtne) ja natuke raskem Windowsiga.

## 1. samm: Osta varustus.

Vajad täpselt sama varustust, mida vajad MyNode node'i käitamiseks. Võid proovida ühte või teist, ainus erinevus on mikro SD kaardil olevad andmed.

- Raspberry Pi 4, 4Gb mälu või 8Gb (4Gb on piisav)
- Ametlik Raspberry Pi toide (Väga oluline! Ära osta mitteametlikku, tõsiselt)
- Karp Pi jaoks. (FLIRC karp on suurepärane. Kogu karp on jahutusradiaator ja sa ei vaja ventilaatorit, mis võib olla lärmakas)
- 32 Gb mikroSD kaart (vajad ühte, kuid mõned on käepärased.)
- Mälukaardi lugeja (enamikul arvutitel pole mikroSD kaardi pesa).
- Väline SSD 1Tb kõvaketas.
- Ethernet kaabel (ühendamiseks kodurouteriga).

Monitori (või klaviatuuri või hiirt) pole vaja

Märkus: See on vale kõvaketas: See on kaasaskantav väline kõvaketas. See ei ole SSD. SSD on hädavajalik. Seepärast on see odav (hind AUDis)

![pilt](assets/1.webp)

See on õige tüüp, mida saada:

![pilt](assets/2.webp)

See on kiirem, kuid tarbetult kallis:

![pilt](assets/3.webp)

## 2. samm: Laadi alla Raspiblitzi Image
Navigeerige Raspiblitz GitHubi veebilehele ja leidke "download image" link:
![image](assets/4.webp)

Allalaaditud faili sha-256 räsi on veebilehel saadaval. See muutub iga uuendusega. Kui te ei saa aru, mis see on, siis peaksite seda tegema, seega kirjutasin juhendi, mida saate siin lugeda.

![image](assets/5.webp)

## 3. samm: Kontrollige pilti

Enne jätkamist, kui te ei tunne end käsureal failisüsteemis liikudes kindlalt, on see lihtne õppida ja te peaksite seda tegema.

Siin on kasulik video Linuxile, kuid see kehtib ka Maci kohta.

Windowsi jaoks on siin lihtne õpetus.
Mac/Linux

Oodake, kuni fail on lõpetanud allalaadimise (tähtis!), ja seejärel avage terminal, navigeerige sinna, kuhu faili alla laadisite, ja tippige järgmine käsk...

```bash
shasum -a 256 xxxxxxxxxxxxxx
```

kus xxxxxxxxxxxxxx on just allalaaditud faili nimi. Kui te ei ole selles kataloogis, kus fail asub, peate sisestama täieliku tee.

Arvuti mõtleb umbes 20 sekundit või nii. Kontrollige, et väljundräsi vastab veebilehelt eelmises etapis allalaaditud räsile. Kui see on identne, võite jätkata.
Windows

Avage käsurida ja navigeerige sinna, kuhu fail on allalaaditud, ning tippige see käsk:

```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```

kus xxxxxxxxxxxxxx on just allalaaditud faili nimi. Kui te ei ole selles kataloogis, kus fail asub, peate sisestama täieliku tee.

Arvuti mõtleb umbes 20 sekundit või nii. Kontrollige, et väljundräsi vastab veebilehelt eelmises etapis allalaaditud räsile. Kui see on identne, võite jätkata.

## 4. samm: Kirjutage SD-kaart

Selleks võite kasutada Balena Etcherit. Laadige see siit alla.

Etcher on iseõpetav kasutamiseks. Sisestage oma mikro-SD kaart ja kirjutage Raspiblitz tarkvara (.img fail) SD-kaardile.

![image](assets/6.webp)

![image](assets/7.webp)

![image](assets/8.webp)

![image](assets/9.webp)

Kui see on tehtud, ei ole draiv enam loetav. Operatsioonisüsteem võib anda veateate ja draiv peaks töölaualt kaduma. Tõmmake kaart välja.

## 5. samm: Seadistage Pi ja sisestage SD-kaart

Osad (korpust ei ole näidatud):

![image](assets/10.webp)

![image](assets/11.webp)

Ühendage Etherneti kaabel ja kõvaketta USB-ühendus (veel mitte toide). Vältige ühendamist keskel asuvate siniste USB-portidega. Need on USB 3. Kasutage USB 2 porti, isegi kui draiv võib olla USB 3 võimeline (usaldusväärsem).

![image](assets/12.webp)

Mikro-SD kaart läheb siia:

![image](assets/13.webp)

Lõpuks ühendage toide:

![image](assets/14.webp)

## 6. samm: Leidke Pi IP-aadress

Raspiblitziga ei ole kunagi vaja monitori. Teil on siiski vaja teist arvutit koduvõrgus. Kui teie Pi ei ole Etherneti kaudu ühendatud ja soovite WiFi-le toetuda, nõuab IP leidmine mõningaid arvutioskusi. Kahjuks ei saa aidata. Teil on vaja Etherneti ühendust. (Probleem tuleneb vajadusest pääseda ligi monitorile ja operatsioonisüsteemile, et ühendada WiFi ja sisestada parool.)

Kontrollige oma ruuterit, et näha kõigi ühendatud seadmete IP-aadresse.
Sisestasin brauserisse 192.168.0.1 (juhised, mis tulid minu ruuteriga), logisin sisse ja nägin oma seadet IP-aadressiga 192.168.0.191. Pane tähele, et neid IP-aadresse ei ole internetis avalikult nähtavad (nad läbivad esmalt ruuteri), need on lihtsalt identifikaatorid seadmetele sinu koduvõrgus.
IP leidmine on hädavajalik.

> UUENDUS: Maci või Linuxi masinas saad kasutada terminali, et leida kõikide Ethernetiga ühendatud seadmete IP-aadressid koduvõrgus, kasutades käsku „arp -a“. Väljund ei ole nii ilus kui ruuteri oma, kuid kogu vajalik info on olemas. Kui pole ilmne, milline on Pi, tee katse-eksituse meetodil.

## 7. samm: SSH ühendus Pi'ga

Enne Pi sisselülitamist pane sinna SD-kaart. Oota mõni minut ja seejärel ava teisel Linuxi/Maci masinal terminal.

Maci/Linuxi jaoks, terminalis tüüpige:

```bash
ssh admin@sinu_Pi_IP_aadress
```

Windowsi puhul pead installima putty, et ssh'ga Pi'le ühenduda. Tüüpige sama käsk nagu eespool.

Esimesel korral, kui seda teed, või kui muudad Pi OS-i, vahetades SD-kaarti, võid saada selle vea...

![image](assets/15.webp)

Selle parandamiseks navigeeri sinna, kus asub „known_hosts“ fail (veateates öeldakse), ja kustuta see. Käsk on "rm known_hosts"

Seejärel korda ssh käsku, et sisse logida. See juhtub...

![image](assets/16.webp)

Tüüpige yes (täis sõna), et jätkata.

Kui õnnestub, küsitakse sinult parooli. See ei ole sinu arvuti jaoks, vaid raspiblitzi jaoks. Üldine parool on „raspiblitz“, ja sa muudad selle hiljem. Terminaliaken muutub siniseks ja sulle kuvatakse menüüvalikud nagu vanades DOS menüüdes. Navigeeri nooleklahvide või hiirega.

![image](assets/17.webp)

Järgi juhiseid, sea oma paroolid ja seejärel tuvastatakse sinu kõvaketas ning sulle antakse võimalus see vajadusel formaatida.

Seejärel küsitakse, kas soovid blockchaini andmed kopeerida teisest allikast või need uuesti alla laadida. Kopeerimine on õppeprotsess ja juhised on üsna head ning hea on neid käepärast hoida...

![image](assets/18.webp)

Lihtsam, kuid aeglasem viis on laadida kogu kett algusest peale alla...

![image](assets/19.webp)

Terminaliaknas vilksatab palju teksti. Võid seda ekslikult pidada blockchaini allalaadimise protsessiks, kuid minu arvates genereeritakse sel hetkel suhtluse jaoks privaatvõtit.

Seejärel ilmuvad välkvaliku võimalused.

![image](assets/20.webp)

Loo uus parool oma välklompaka lukustamiseks, seejärel luuakse uus rahakott ja sulle antakse üles kirjutada 24 sõna...

![image](assets/21.webp)

Veendu kindlasti, et kirjutad need üles ja hoiad turvaliselt. Ma kuulsin ühest inimesest, kes seda ei teinud, kuna ta ei plaaninud välku kasutada, kuid aasta hiljem otsustas seda kasutada ja avas kanaleid. Siis mõistis ta, et tema sõnu ei olnud varundatud ja kuna seadmest ei olnud võimalik sõnu uuesti ekstraheerida, pidi ta kõik oma kanalid sulgema ja alustama otsast peale. Tema pääses sellega, kuid teised ei pruugi nii õnnelikud olla.

Sellele järgneb mõni minut teksti kerimist terminaliaknas. Siis...

![image](assets/22.webp)
Teid logitakse ssh seansist välja. Logige uuesti sisse, seekord oma uue parooliga, parool A. Sees olles palutakse teil sisestada parool C, et avada oma lightning rahakott.
Nüüd me ootame. Näeme kahe nädala pärast. Võite terminali sulgeda, see ei mõjuta Pi'd, see on lihtsalt suhtlusaken.

![image](assets/23.webp)

Kui mingil põhjusel soovite Pi välja lülitada enne, kui plokiahel on lõpetanud allalaadimise, on see korras, kuni teete seda õigesti. Plokiahel jätkab allalaadimist sealt, kus see pooleli jäi, kui te uuesti ühendate.

Vajutage CTRL+c, et sinisest ekraanist väljuda. Te jõuate Pi Linuxi terminali. Siin saate trükkida "menu", mis laadib järgmise ekraani, ja sealt saate Pi välja lülitada.

![image](assets/24.webp)

JUHENDI LÕPP

Niisiis, nüüdsest on teie sõlm valmis kasutamiseks. Kui vajate veel abi rohkemate valikute navigeerimisel, vaadake lisajuhendite ja õpetuste jaoks githubi lehte https://github.com/raspiblitz/raspiblitz#feature-documentation