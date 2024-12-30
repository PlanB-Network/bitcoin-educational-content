---
name: RoninDojo v2
description: Oma RoninDojo v2 Bitcoin node'i paigaldamine Raspberry Pi'le
---
![kaanepilt RoninDojo v2](assets/cover.webp)

***HOIATUS:** Pärast Samourai Walleti asutajate vahistamist ja nende serverite konfiskeerimist 24. aprillil on mõned RoninDojo funktsioonid, nagu Whirlpool, enam mitte töökorras. Siiski on võimalik, et need tööriistad võidakse järgnevatel nädalatel taastada või uuesti käivitada erineval kujul. Kuna RoninDojo kood oli majutatud Samourai GitLabis, mis samuti konfiskeeriti, ei ole hetkel võimalik koodi kaugelt alla laadida. RoninDojo meeskonnad töötavad tõenäoliselt koodi uuesti avaldamise nimel.*

_Jälgime selle juhtumi arenguid ning seotud tööriistade arenguid tähelepanelikult. Võite olla kindlad, et uuendame seda õpetust, kui uut teavet saadaval on._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---

> "*Kasuta Bitcoini privaatselt.*"

[Varasemas õpetuses](https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0) olime juba selgitanud protseduuri RoninDojo v1 paigaldamiseks ja kasutamiseks. Siiski, viimase aasta jooksul on RoninDojo meeskonnad käivitanud nende rakenduse versiooni 2, mis tähistas olulist pöördepunkti tarkvara arhitektuuris. Tõepoolest, nad liikusid Linux Manjaro distributsioonist Debiani kasuks. Seetõttu ei paku nad enam eelkonfigureeritud pilti Raspberry Pi'le automaatseks paigaldamiseks. Kuid on siiski olemas meetod käsitsi paigaldamiseks. Seda meetodit kasutasin omaenda node'i jaoks ja sellest ajast alates on RoninDojo v2 suurepäraselt töötanud minu Raspberry Pi 4-l. Seega pakun uut õpetust, kuidas käsitsi paigaldada RoninDojo v2 Raspberry Pi'le.

## Sisukord:
- Mis on RoninDojo?
- Millist riistvara valida RoninDojo v2 paigaldamiseks?
- Kuidas kokku panna Raspberry Pi 4?
- Kuidas paigaldada RoninDojo v2 Raspberry Pi 4-le?
- Kuidas kasutada oma RoninDojo v2 node'i?

## Mis on RoninDojo?
Dojo on algselt täielik Bitcoin node'i rakendus, mis põhineb Bitcoin Core'il ja on välja töötatud Samourai Walleti meeskondade poolt. Seda lahendust saab paigaldada igale seadmele. Erinevalt teistest Core'i rakendustest on Dojo spetsiaalselt optimeeritud integreerimiseks Samourai Walleti Androidi rakenduskeskkonnaga. RoninDojo on aga tööriist, mis on mõeldud Dojo paigaldamise ja haldamise hõlbustamiseks, samuti mitmesuguste muude täiendavate tööriistade jaoks. Lühidalt, RoninDojo rikastab Dojo baasrakendust, integreerides hulgaliselt lisatööriistu, samal ajal lihtsustades selle paigaldamist ja haldamist.

Ronin pakub ka [node-in-box lahendust, mida nimetatakse "*Tanto*"](https://ronindojo.io/en/products), seadet, millele on RoninDojo juba paigaldatud ja mille on kokku pannud nende meeskond. Tanto on tasuline valik, mis võib olla huvitav neile, kes soovivad vältida tehnilisi komplikatsioone. Kuid kuna RoninDojo lähtekood on avatud, on võimalik seda ka oma riistvarale paigaldada. See alternatiiv, mis on majanduslikult soodsam, nõuab siiski mõningaid lisamanipulatsioone, mida me selles õpetuses käsitleme.
RoninDojo on Dojo, mis võimaldab Whirlpool CLI lihtsat integreerimist teie Bitcoin'i sõlme, et pakkuda parimat võimalikku coinjoin kogemust. Whirlpool CLI abil muutub võimalikuks teie bitcoinide pidev remiximine 24 tundi päevas, 7 päeva nädalas, ilma et teie isiklik arvuti peaks jääma sisse lülitatuks.
Peale Whirlpool CLI sisaldab RoninDojo mitmesuguseid tööriistu, et täiustada teie Dojo funktsionaalsusi. Nende hulgas Boltzmanni kalkulaator analüüsib teie tehingute privaatsuse taset, Electrumi server võimaldab teie Bitcoin'i rahakottide ühendamist teie sõlmega ja Mempooli server võimaldab teil kohalikult vaadata oma tehinguid, ilma et lekitaksite informatsiooni.

Võrreldes teiste sõlmlahendustega nagu Umbrel, on RoninDojo selgelt keskendunud on-chain lahendustele ja privaatsustööriistadele. Erinevalt Umbrelist ei toeta RoninDojo Lightning'i sõlme seadistamist ega üldisemate serverirakenduste integreerimist. Kuigi RoninDojo pakub vähem mitmekülgseid tööriistu kui Umbrel, on sellel kõik olulised funktsionaalsused teie on-chain tegevuse haldamiseks.

Kui te ei vaja üldisi funktsionaalsusi ega neid, mis on seotud Lightning Networkiga, nagu pakub Umbrel, ja otsite lihtsat, stabiilset sõlme oluliste tööriistadega nagu Whirlpool või Mempool, võib RoninDojo olla ideaalne lahendus. Kuigi Umbrel kipub muutuma mini multitasking serveriks, mis on orienteeritud Lightning Networkile ja mitmekülgsusele, keskendub RoninDojo, kooskõlas Samourai Walleti filosoofiaga, kasutaja privaatsuse põhitööriistadele.

Nüüd, kui oleme RoninDojo üle vaadanud, vaatame koos, kuidas seda sõlme seadistada.

## Millist riistvara valida RoninDojo v2 paigaldamiseks?
RoninDojo pakub oma tarkvara automaatseks paigaldamiseks pilti [RockPro64](https://ronindojo.io/en/download) jaoks. Siiski keskendub meie õpetus käsitsi paigaldamise protseduurile Raspberry Pi 4 peal. Kuigi Raspberry Pi 5 on hiljuti turule lastud ja teoreetiliselt peaks see õpetus olema ühilduv selle uue mudeliga, ei ole mul veel olnud võimalust seda isiklikult testida ja ma pole kogukonnalt tagasisidet leidnud. Niipea kui soetan Pi 5 ja ühilduvad komponendid, uuendan seda õpetust, et teid kursis hoida. Seniks soovitan eelistada Pi 4, kuna see töötab minu sõlme jaoks suurepäraselt.
Minu osa, ma jooksen RoninDojo Raspberry Pi'l, mis on varustatud 8 GB RAM'iga. Kuigi mõned kogukonna liikmed on suutnud selle tööle saada seadmetel, mis on varustatud ainult 4 GB RAM'iga, ei ole ma seda konfiguratsiooni ise testinud. Väikese hinnavahe tõttu tundub mõistlik valida 8 GB RAM'i versioon. See võib osutuda kasulikuks ka siis, kui plaanite oma Raspberry Pi tulevikus muuks otstarbeks ümber kasutada.
On oluline märkida, et RoninDojo meeskonnad on teatanud sagedastest probleemidest, mis on seotud korpuse ja SSD adapteriga. Olen ise nende probleemidega silmitsi seisnud. **Seetõttu on tungivalt soovitatav vältida oma sõlme SSD jaoks USB-kaabliga varustatud korpusi.** Eelistage selle asemel spetsiaalselt teie Raspberry Pi jaoks mõeldud salvestuslaienduskaarti:

![salvestuslaienduskaart RPI4](assets/notext/1.webp)
Bitcoin'i plokiahela salvestamiseks vajate SSD-d, mis ühildub teie valitud laienduskaardiga. Praegu (veebruar 2024) oleme üleminekufaasis. Oodatakse, et mõne kuu pärast ei ole 1 TB kettad enam piisavad kasvava plokiahela suuruse mahutamiseks, eriti arvestades erinevaid rakendusi, mida plaanite oma sõlme integreerida. Seetõttu soovitavad mõned investeerida pikemaajalise rahu tagamiseks 2 TB SSD-sse. Siiski, arvestades SSD hindade aastast aastasse langustrendi, soovitavad teised piirduda 1 TB kõvakettaga, mis peaks olema piisav üheks või kaheks aastaks, väites, et selleks ajaks, kui see muutub vananenuks, on 2 TB mudelite hind tõenäoliselt langenud. Valik sõltub seega teie isiklikest eelistustest. Kui plaanite oma RoninDojo't pikka aega hoida ja soovite vältida lähiaastatel tehnilist sekkumist, tundub 2 TB SSD valik kõige ettenägelikum, kuna see pakub teile mugavat varu tulevikuks.
Lisaks vajate mitmesuguseid väikseid komponente:
- Korpus koos ventilaatoriga, et majutada teie Raspberry Pi-d ja teie laienduskaarti. Komplektid, mis sisaldavad nii SSD laienduskaarti kui ka ühilduvat korpust, on saadaval internetis;
- Toitekaabel teie Raspberry Pi jaoks;
- Vähemalt 16 GB mikro SD-kaart (kuigi tehniliselt võiks piisata ka 8 GB-st, on 8 ja 16 GB kaartide hinnavahe tihti tühine);
- RJ45 Ethernet kaabel võrguühenduse jaoks.

![node material](assets/notext/2.webp)

## Kuidas kokku panna Raspberry Pi 4?
Teie sõlme kokkupanek varieerub sõltuvalt valitud riistvarast, eriti korpuse tüübist. Siiski, üldine sammude järgimise skeem jääb kokkupanekul üldjoontes sarnaseks.
Alustage oma SSD paigaldamisega laienduskaardile, veendudes, et tagaküljel olevad kaks lukustuskruvi on kindlalt kinnitatud.

![assembly1](assets/notext/3.webp)

Seejärel kinnitage oma Raspberry Pi laienduskaardile.

![assembly2](assets/notext/4.webp)

Samuti kinnitage ventilaator Raspberry Pi külge.

![assembly3](assets/notext/5.webp)

Ühendage erinevad komponendid, pöörates tähelepanu õigetele pistikutele, viidates oma korpuse juhendile. Korpusetootjad pakuvad sageli videoõpetusi, mis aitavad teil kokkupanekul.
Minu puhul on mul lisaks laienduskaart, millel on sisse/välja lüliti. See ei ole Bitcoin'i sõlme tegemiseks hädavajalik. Ma kasutan seda peamiselt toitenupu olemasoluks.

Kui teil, nagu minul, on laienduskaart sisse/välja lülitiga, ärge unustage paigaldada väikest "Auto Power On" hüppajat. See võimaldab teie sõlmel automaatselt sisse lülituda niipea, kui see on toitega ühendatud. See funktsioon on eriti kasulik elektrikatkestuse korral, kuna see võimaldab teie sõlmel ise taaskäivituda, ilma et peaksite ise sekkuma.

![assembly4](assets/notext/6.webp)

Enne kõigi riistvarakomponentide korpusesse paigutamist on oluline kontrollida teie Raspberry Pi, laienduskaardi ja ventilaatori nõuetekohast toimimist, lülitades need sisse.

![assembly5](assets/notext/7.webp)
Lõpuks paigaldage oma Raspberry Pi selle korpusesse. Olge teadlikud, et hilisemas etapis on vajalik mikro-SD kaardi lisamine vastavasse porti Raspberry Pi-s. Kui teie korpusel on avaus, mis võimaldab SD-kaarti sisestada ilma seda avamata (nagu on minu puhul foto näitel), võite nüüd korpuse sulgeda. Kui aga teie korpuse juures pole otsest ligipääsu mikro-SD pordile, peate ootama, kuni olete mikro-SD kaardi ette valmistanud, et see enne koostamise lõpetamist sisestada.
![assembly6](assets/notext/8.webp)

## Kuidas paigaldada RoninDojo v2 Raspberry Pi 4 peale?

### 1. samm: Valmistage ette käivitatav mikro-SD
Pärast riistvara kokkupanekut on järgmine samm RoninDojo paigaldamine. Selleks valmistame teie arvutist käivitatava mikro-SD kaardi, kirjutades sellele sobiva kettapildi.
Teil on vaja kasutada _**Raspberry Pi Imager**_ tarkvara, mis on loodud operatsioonisüsteemide allalaadimise, seadistamise ja kirjutamise hõlbustamiseks mikro-SD kaardile, mida kasutatakse Raspberry Pi-ga. Alustage selle tarkvara paigaldamist oma isiklikule arvutile:
- Ubuntu/Debiani jaoks: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- Windowsi jaoks: https://downloads.raspberrypi.org/imager/imager_latest.exe
- Maci jaoks: https://downloads.raspberrypi.org/imager/imager_latest.dmg

Kui tarkvara on paigaldatud, avage see ja sisestage oma mikro-SD kaart isiklikku arvutisse. Raspberry Pi Imageri liidesest valige `CHOOSE OS`:

![choose OS](assets/notext/9.webp)

Seejärel minge menüüsse `Raspberry Pi OS (other)`:

![choose OS others](assets/notext/10.webp)

Valige operatsioonisüsteem nimega `Raspberry Pi OS (Legacy, 64-bit) Lite`, mille suurus on `0.3 GB`:

![choose OS Legacy Lite](assets/notext/11.webp)

Pärast operatsioonisüsteemi valimist suunatakse teid tagasi Raspberry Pi Imageri põhimenüüsse. Klõpsake `CHOOSE STORAGE`:

![choose storage](assets/notext/12.webp)

Valige oma mikro-SD kaart:

![choose micro sd](assets/notext/13.webp)

Pärast operatsioonisüsteemi ja mikro-SD kaardi valimist klõpsake `NEXT`:

![choose next](assets/notext/14.webp)

Ilmub uus aken. Valige `EDIT CONFIGURATION`:

![edit settings](assets/notext/15.webp)

Selles aknas minge vahekaardile `GENERAL` ja tehke järgmised seadistused (mis on selle toimimiseks väga olulised):
- Luba valik ja määrake `RoninDojo` kui hostinimi;
- Luba `Set username and password`, sisestage kasutajanimeks `pi`, valige parool ja pange see info kirja, kuna seda läheb hiljem vaja. Need volitused kustutatakse hiljem;
- Keela `Configure Wi-Fi`;
- Luba `Set locale settings` ja valige oma ajavöönd ning klaviatuuri tüüp, mis vastab teie arvutile;

![general settings](assets/notext/16.webp)

SERVICES vahekaardil klõpsake `Enable SSH` ruudul ja valige `Use a password for authentication`:

![services settings](assets/notext/17.webp)

Veenduge ka, et `OPTIONS` vahekaardil on telemetria keelatud:

![options settings](assets/notext/18.webp)

Klõpsake `SAVE`:
![settings save](assets/notext/19.webp)Kinnitage klõpsates `YES`, et alustada käivitusvalmis micro SD kaardi loomist:
![settings yes](assets/notext/20.webp)

Teile kuvatakse teade, et kõik andmed micro SD kaardil kustutatakse. Kinnitage protsessi alustamiseks klõpsates `YES`:

![overwrite micro SD](assets/notext/21.webp)

Oodake, kuni tarkvara lõpetab teie micro SD kaardi ettevalmistamise:

![writing micro SD](assets/notext/22.webp)

Kui ilmub teade protsessi lõppemisest, võite micro SD kaardi arvutist eemaldada:

![writing micro SD completed](assets/notext/23.webp)

### 2. samm: Sõlme kokkupaneku lõpetamine
Nüüd saate sisestada micro SD kaardi oma Raspberry Pi vastavasse porti.

![micro SD](assets/notext/24.webp)

Seejärel ühendage oma Raspberry Pi ruuteriga Etherneti kaabli abil. Lõpuks lülitage oma sõlm sisse, ühendades toitekaabli ja vajutades toitenuppu (kui teie seadistus seda sisaldab).

### 3. samm: SSH-ühenduse loomine sõlmega
Esmalt on vajalik leida teie sõlme IP-aadress. Selleks võite kasutada tööriista nagu _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ või _[Angry IP Scanner](https://angryip.org/)_ või kontrollida oma ruuteri haldusliidest. IP-aadress peaks olema kujul `192.168.1.??`. **Kõigi järgnevate käskude puhul asendage `[IP]` tegeliku sõlme IP-aadressiga**, (eemaldades sulud).

Käivitage terminal.

Võimaliku juba IP-aadressiga seostatud võtme eemaldamiseks täitke käsk: 
`ssh-keygen -R [IP]`. 

Selle käsu järgne viga ei ole tõsine; see lihtsalt tähendab, et võti ei eksisteeri teie tuntud hostide nimekirjas (mis on üsna tõenäoline). Näiteks, kui teie sõlme IP on `192.168.1.40`, muutub käsk: `ssh-keygen -R 192.168.1.40`.

Seejärel looge oma sõlmega SSH-ühendus, täites käsu: 
`ssh pi@[IP]`.
Ilmub teade hosti autentsuse kohta: `The authenticity of host '[IP]' can't be established.` See näitab, et seadme, millega üritate ühendust luua, autentsust ei saa kinnitada, kuna puudub tuntud avalik võti. SSH kaudu esmakordselt uue hostiga ühenduse loomisel ilmub see teade alati. Peate vastama `yes`, et lisada selle avalik võti oma kohalikku kataloogi, mis hoiab seda hoiatusteate ilmumast tulevikus, luues SSH-ühendusi selle sõlmega. Seega tippige `yes` ja vajutage `enter`, et kinnitada.
Seejärel palutakse teil sisestada oma parool, mille seadsite ajutiselt 1. sammus. Kinnitage vajutades `enter`. Nüüd olete oma sõlmega SSH kaudu ühendatud.

Kokkuvõttes, siin on käsklused, mida täita:
- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `yes`
- Sisestage ajutine parool ja kinnitage.

### 4. samm: Uuendamine ja ettevalmistus
Nüüd olete oma sõlmega SSH-seansi kaudu ühendatud. Teie terminalis peaks käsurea viip olema: `pi@RoninDojo:~ $`. Alustuseks uuendage saadaolevate pakettide nimekirja ja installige olemasolevatele pakettidele uuendused järgmise käsu abil:
`sudo apt update && sudo apt upgrade -y`
Pärast uuenduste lõpetamist jätkake *Git* ja *Dialog* installimist käsu abil: `sudo apt install git dialog -y`

Järgmisena kloonige _RoninOS_ Git repositooriumi `master` haru, käivitades:
`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`

Käivitage skript `customize-image.sh` käsu abil:
`cd /opt/RoninOS/ && sudo ./customize-image.sh`

**On oluline lasta skriptil katkestusteta töötada ja kannatlikult selle protsessi lõppu oodata**, mis võtab umbes 10 minutit. Kui ilmub teade `Setup is complete`, võite liikuda järgmise sammu juurde.

### 5. samm: RoninOS käivitamine
Käivitage RoninOS käsu abil:
`sudo systemctl start ronin-setup`

Kuvage logifaili read käsu abil:
`tail -f /home/ronindojo/.logs/setup.logs`

Sel etapil on **oluline lasta RoninOSil käivituda ja oodata**, kuni see on lõpetanud töötamise. See võtab umbes 40 minutit. Kui ilmub `All RoninDojo feature installations complete!`, võite liikuda 6. sammu juurde.

### 6. samm: RoninUI-le juurdepääsu saamine ja volituste muutmine
Pärast installimise lõpetamist, et ühenduda oma sõlmega brauseri kaudu, veenduge, et teie isiklik arvuti on ühendatud sama kohaliku võrguga kui teie sõlm. Kui kasutate oma masinas VPN-i, keelake see ajutiselt. Sõlme liidesele brauseris juurdepääsemiseks sisestage URL-i ribale:
- Otseselt teie sõlme IP-aadress, näiteks `192.168.1.??`;
- Või tippige `ronindojo.local`.

RoninUI avalehele jõudes palutakse teil seadistamist alustada. Selleks klõpsake nupul `Let's start`.

![lets start](assets/notext/25.webp)

Sel etapil esitleb RoninUI teile teie `root` parooli. On oluline see turvaliselt hoida. Võite valida füüsilise varukoopia, paberil, või salvestada selle [paroolihalduris](https://planb.network/courses/secu101/4/2).

![root password](assets/notext/26.webp)

Pärast `root` parooli salvestamist märkige ruut `I have backed up Root user credentials` ja klõpsake jätkamiseks nupul `Continue`.

![confirm root password](assets/notext/27.webp)

Järgmine samm hõlmab kasutajaparooli loomist, mida kasutatakse nii RoninUI veebiliidesele juurdepääsuks kui ka SSH seansside loomiseks teie sõlmega. Valige tugev parool ja veenduge, et salvestate selle turvaliselt. Peate sisestama selle parooli kaks korda enne `Finish` nupule klõpsamist, et kinnitada. Kasutajanime osas on soovitatav jääda vaikimisi valiku juurde, `ronindojo`. Kui otsustate seda muuta, pidage meeles järgmistes sammudes käskude kohandamist.

![user credentials](assets/notext/28.webp)

Pärast neid toiminguid oodake, kuni teie sõlm initsialiseerub. Seejärel pääsete juurde RoninUI veebiliidesele. Olete peaaegu protsessi lõpus, jäänud on vaid mõned väikesed sammud!
![Ronin UI](assets/notext/29.webp)

### 7. samm: Ajutiste volituste eemaldamine
Avage oma isiklikus arvutis uus terminal ja looge oma sõlmega SSH-ühendus järgmise käsu abil:
`SSH ronindojo@[IP]`
Kui näiteks teie sõlme IP-aadress on `192.168.1.40`, siis sobiv käsk oleks: `SSH ronindojo@192.168.1.40`

Kui te muutsite eelmises etapis oma kasutajanime, asendades vaikimisi kasutajanime (`ronindojo`) mõne teisega, veenduge, et kasutate seda uut nime käskluses. Näiteks, kui valisite kasutajanimeks `planb` ja IP-aadress on `192.168.1.40`, siis sisestatav käsk oleks:
`SSH planb@192.168.1.40`
Teilt küsitakse kasutaja parooli. Sisestage see ja vajutage `enter`, et kinnitada. Seejärel pääsete ligi RoninCLI liidesele. Kasutage klaviatuuri nooleklahve, et liikuda valikuni `Exit RoninDojo` ja vajutage `enter`, et seda valida.
![RoninCLI](assets/notext/30.webp)

Sel hetkel olete oma sõlme terminalis, käsureaga sarnane: `ronindojo@RoninDojo:~ $`. Ajutise kasutaja eemaldamiseks, kes loodi käivitatava mikro SD-kaardi seadistamise ajal, sisestage järgmine käsk ja vajutage `enter`:
`sudo deluser --remove-home pi`

Teilt küsitakse kinnituseks teie kasutaja parooli. Sisestage see ja kinnitage vajutades `enter`. Oodake, kuni toiming on lõpule viidud, seejärel kasutage terminalist väljumiseks käsku `exit`.

Palju õnne! Teie RoninDojo v2 sõlm on nüüd seadistatud ja kasutusvalmis. See alustab oma IBD-d (*Initial Block Download*), alustades Bitcoin'i plokiahela allalaadimist ja kontrollimist Genesis plokist. See samm hõlmab kõikide alates 3. jaanuarist 2009 tehtud Bitcoin'i tehingute hankimist ja võtab aega. Kui plokiahel on täielikult alla laaditud, jätkab indekseerija andmebaasi tihendamist. IBD kestus võib oluliselt varieeruda. Teie RoninDojo sõlm on täielikult töökorras, kui see protsess on lõpule viidud.

**Kui te migreerite vanast RoninDojo v1 sõlmest** uude versiooni selle õpetuse abil, säilitades sama SSD, peaks teie sõlm automaatselt tuvastama ja taaskasutama kettal olemasolevaid andmeid, säästes teid IBD uuesti tegemise vajadusest. Sel juhul peate lihtsalt ootama, kuni teie sõlm sünkroniseerub viimaste plokkidega.

### 8. samm: "veth* parandus"
Kui kohtate oma RoninDojo v2 sõlmega Raspberry Pi peal viga, kus pärast probleemideta paigaldust muutub teie sõlm äkki SSH kaudu kättesaamatuks, kuid taastub pärast lihtsat taaskäivitust, siis peate järgima seda 8. sammu. See levinud viga saab kergesti lahendatud kogukonna välja töötatud lahendusega: "_veth parandus_". See väike parandus kõrvaldab järsud katkestused püsivalt. Siin on, kuidas seda rakendada.

Avage oma isiklikul arvutil uus terminal ja looge oma sõlmega SSH-ühendus järgmise käsu abil:
`SSH ronindojo@[IP]`

Kui näiteks teie sõlme IP-aadress on `192.168.1.40`, siis sobiv käsk oleks:
`SSH ronindojo@192.168.1.40`

Teilt küsitakse kasutaja parooli. Sisestage see ja vajutage `enter`, et kinnitada. Seejärel pääsete ligi RoninCLI liidesele. Kasutage klaviatuuri nooleklahve, et liikuda valikuni `Exit RoninDojo` ja vajutage `enter`, et seda valida.
Sel hetkel viibite oma sõlme terminalis, kus käsukutse näeb välja sarnane: `ronindojo@RoninDojo:~ $`. Veth* paranduse rakendamiseks tippige järgmine käsk ja vajutage `enter`: `sudo nano /etc/dhcpcd.conf`

Kinnitage oma parool uuesti ja vajutage `enter`.

Jõuate `dhcpcd.conf` failini. Peate kopeerima järgmise teksti, veendudes, et ka asterisk on kaasatud, ja lisama selle faili lõppu:
`denyinterfaces veth*`

Selleks liikuge faili lõppu, kasutades klaviatuuril allanoolt, seejärel kasutage teksti sõltumatu reana kleepimiseks hiire paremat nuppu.

Pärast teksti lisamist vajutage `ctrl X`, et alustada väljumist, järgnevalt `ctrl Y`, et kinnitada muudatuste salvestamist, ja vajutage `enter`, et lõpetada ja naasta käsukutsesse. Veendumaks, et muudatus on õigesti rakendatud, avage `dhcpcd.conf` fail uuesti, kasutades sobivat käsku.

Paranduse rakendamise lõpetamiseks taaskäivitage oma sõlm, käivitades:
`sudo reboot now`

Sel hetkel võite oma terminali sulgeda. Andke oma RoninDojole vajalik aeg taaskäivitamiseks, pärast mida peaksite saama ühenduda oma brauseri graafilise liidese kaudu. See protsess peaks parandama kohatud vea.

## Kuidas kasutada oma RoninDojo v2 sõlme?

### Ühendades oma rahakott-tarkvara Electrs'iga
Teie värskelt paigaldatud ja sünkroniseeritud sõlme esimene kasutus on teie tehingute edastamine Bitcoin'i võrku. Tõenäoliselt soovite ühendada oma erinevad rahakotid oma sõlmega, et edastada oma tehinguid konfidentsiaalselt. Seda saate teha läbi Electrum Rust Serveri (electrs). See rakendus on tavaliselt eelinstalleeritud teie RoninDojo sõlmes. Kui mitte, võite selle käsitsi paigaldada RoninCLI liidese kaudu `Applications > Manage Applications > Install Electrum Server`.

Oma Electrum Serveri Tor aadressi saamiseks, RoninUI veebiliidesest, minge:
`Pairing > Electrum server > Pair now`
![Pairing](assets/notext/31.webp)
![Electrs](assets/notext/32.webp)
Seejärel peate sisestama oma rahakott-tarkvaras `Hostname` aadressi, mis lõppeb `.onion`-iga, koos pordiga `50001`. ![hostname](assets/notext/33.webp)
Näiteks Sparrow Wallet'is lihtsalt minge vahekaardile:
`File > Preferences > Server > Private Electrum`

![Sparrow](assets/notext/34.webp)

### Ühendades oma rahakott-tarkvara Samourai Dojoga
Alternatiivina Electrs'i kasutamisele võimaldab Dojo ühendada oma ühilduva tarkvara rahakoti otse oma RoninDojo sõlmega. Rahakotid nagu Samourai Wallet ja Sentinel pakuvad seda funktsionaalsust.

Ühenduse loomiseks peate lihtsalt skaneerima oma Dojo QR-koodi. Selle QR-koodi juurde pääsemiseks RoninUI kaudu, navigeerige:
`Pairing > Samourai Dojo > Pair now`
![Samourai Dojo](assets/notext/35.webp)
Oma Samourai Wallet'i oma Dojoga ühendamiseks skaneerige lihtsalt see QR-kood rakenduse paigaldamise ajal:

![Samourai Wallet connection](assets/notext/36.webp)
Kui teil oli juba enne oma Ronin Dojo seadistamist Samourai Wallet, on vajalik teha oma rahakotist varukoopia, desinstallida ja seejärel uuesti installida Samourai Walleti rakendus, enne kui taastate oma rahakoti. Taasinstalleeritud rakenduse käivitamisel on teil võimalus ühenduda uue Dojoga. **Olge ettevaatlik, see protsess kannab endas bitcoine kaotamise riski, kui seda ei teostata korrektselt!** Veenduge, et teil on oma Samourai rahakoti varukoopia failides ja kontrollige oma paroolilause kehtivust `Settings > Troubleshoot > Passphrase` kaudu. On samuti oluline omada loetavat varukoopiat oma taastefraasist ja paroolilausest. Selle toimingu täpsemaks teostamiseks on soovitatav järgida seda detailset õpetust: [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).
### Oma Mempool.space plokkide uurija kasutamine
Plokkide uurija muudab Bitcoin'i plokiahela toorandmed struktureeritud ja kergesti loetavaks formaadiks. Tööriistadega nagu *Mempool.space* on võimalik analüüsida tehinguid, otsida konkreetseid aadresse või isegi konsulteerida võrgu mempoolide keskmisi tasumäärasid reaalajas.

Siiski, veebipõhiste plokkide uurijate kasutamine kujutab endast riske teie privaatsusele ja hõlmab usaldust kolmandate osapoolte pakutava andmeid. Tõepoolest, nende teenuste kasutamine ilma oma sõlme kaudu võib tahtmatult avalikustada teavet teie tehingute kohta ja peate lootma saidi omaniku esitatud teabe täpsusele.
Nende riskide maandamiseks on soovitatav kasutada oma *Mempool.space* instantsi Tor võrgu kaudu, otse oma sõlmel hostituna. See lahendus tagab teie privaatsuse säilimise ja andmete autonoomia.
Selleks alustage *Mempool Space Visualizer* installimisest RoninUI kaudu. Veebiliideses minge vahekaardile `Dashboard` ja klõpsake `Manage` all `Mempool Space`:
`Dashboard > Mempool Space > Manage`
![Manage mempool](assets/notext/37.webp)
Seejärel klõpsake nupul `Install Mempool visualizer`:
![install mempool](assets/notext/38.webp)
Kinnitage oma kasutajaparool:
![password mempool](assets/notext/39.webp)
Oodake installimise lõpuleviimist, seejärel klõpsake uuesti nupul `Manage`:
![Mempool Manage](assets/notext/40.webp)
Te saate `.onion` lingi, et pääseda juurde oma *Mempool.space* instantsile Tor võrgu kaudu.
![Mempool link](assets/notext/41.webp)
Soovitan teil salvestada see link oma Tor brauseri lemmikutesse või lisada see Tor Browseri rakendusse oma nutitelefonis, et tagada lihtne ja turvaline juurdepääs igalt poolt. Kui teil ei ole veel Tor brauserit, saate selle alla laadida siit: [https://www.torproject.org/download/](https://www.torproject.org/download/)
![Mempool Tor](assets/notext/42.webp)

### Whirlpooli kasutamine oma bitcoinide segamiseks
Teie RoninDojo sõlm integreerib ka _WhirlpoolCLI_, käsurealiidese, mis võimaldab Whirlpooli coinjoinide automatiseerimist, ja _WhirlpoolGUI_, graafilise liidese, mis on mõeldud suhtlemiseks _WhirlpoolCLI_-ga.
Whirlpooli kasutamiseks mündiühendamiseks peab kasutatav rakendus olema aktiivne, et teostada ümbersegamisi. See tingimus võib olla piirav neile, kes soovivad saavutada kõrge anonüümsuse tasemeid. Tõepoolest, seade, kuhu on integreeritud Whirlpooli rakendus, peab pidevalt töötama. See tähendab, et osalemiseks ümbersegamistes ööpäevaringselt, peab teie arvuti või nutitelefon olema pidevalt sisse lülitatud koos Samourai või Sparrow'ga avatuna. Selle piirangu lahenduseks on kasutada _WhirlpoolCLI_-d masinal, mis on alati sees, nagu näiteks Bitcoin node, võimaldades teie müntidel seguneda katkematult, ilma vajaduseta hoida teist seadet sisse lülitatuna.
Üksikasjalik õpetus on ettevalmistamisel, et juhendada teid samm-sammult läbi protsessi, kuidas teha mündiühendamist Samourai Walleti ja RoninDojo v2 abil, A-st Z-ni.

Sügavamaks mõistmiseks mündiühendamisest ja selle kasutamisest Bitcoinil, kutsun teid samuti konsulteerima selle teise artikliga: [Mündiühendamise mõistmine ja kasutamine Bitcoinil](https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2), kus ma detailideni selgitan kõike, mida peate selle tehnika kohta teadma.
### Whirlpool Stat Tool (WST) kasutamine

Pärast mündiühendamiste tegemist Whirlpooliga on kasulik täpselt hinnata saavutatud privaatsuse taset teie segatud UTXO-de jaoks. Selleks võite kasutada Pythoni tööriista *Whirlpool Stat Tool*. See tööriist võimaldab teil mõõta nii teie UTXO-de tuleviku- kui ka tagasivaatelisi hindeid, analüüsides samal ajal nende leviku määra basseinis.

Oma anonüümsete komplektide arvutusmehhanismide mõistmise süvendamiseks soovitan lugeda artiklit: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa), mis kirjeldab nende indeksite toimimist.

WST tööriista kasutamiseks minge RoninCLI juurde. Selleks avage oma isiklikul arvutil terminal ja looge SSH ühendus oma noodiga, kasutades järgmist käsku:
`SSH ronindojo@[IP]`

Näiteks, kui teie noodil on IP aadress `192.168.1.40`, oleks sobiv käsk:
`SSH ronindojo@192.168.1.40`

Kui te muutsite 6. sammu ajal oma kasutajanime, asendades vaikimisi kasutajanime (`ronindojo`) mõne teisega, veenduge, et kasutate seda uut nime käskluses. Näiteks, kui valisite oma kasutajanimeks `planb` ja IP aadress on `192.168.1.40`, tuleks sisestada käsk:
`SSH planb@192.168.1.40`

Teilt palutakse sisestada kasutaja parool. Sisestage see ja vajutage `enter`, et kinnitada. Seejärel pääsete ligi RoninCLI liidesele. Kasutage oma klaviatuuri nooleklahve, et navigeerida menüüsse `Samourai Toolkit` ja vajutage `enter`, et seda valida:

![Samourai Toolkit](assets/notext/43.webp)

Seejärel valige `Whirlpool Stat Tool`:

![WST](assets/notext/44.webp)

WST käivitamisel jätkub tööriista automaatne installimine. Oodake selle sammu ajal. Kasutusjuhised kerivad läbi. Kui installimine on lõpetatud, vajutage mis tahes klahvi, et pääseda WST terminali:

![WST commands](assets/notext/45.webp)

Kuvatakse järgmine käsurea viip:
`wst#/tmp>`

Kui soovite sellest liidesest väljuda ja naasta RoninCLI menüüsse, sisestage lihtsalt:
`quit`

Esmalt on vajalik konfigureerida proxy Tori kasutamiseks, et tagada konfidentsiaalsus andmete väljavõtmisel OXT-st. Sisestage käsk:
`socks5 127.0.0.1:9050`
Seejärel jätkake oma tehingu sisaldava basseiniinfo allalaadimisega:
`download 0001`
Asendage `0001` basseini koodiga, mis teid huvitab. Basseini koodid on WST järgi järgmised:
- Bassein 0.5 bitcoini: `05`
- Bassein 0.05 bitcoini: `005`
- Bassein 0.01 bitcoini: `001`
- Bassein 0.001 bitcoini: `0001`

Pärast allalaadimist laadige andmed, asendades `0001` oma basseini koodiga selles käskluses: `load 0001`

![WST laadimine](assets/notext/46.webp)

Oodake, kuni laadimine on lõppenud, mis võib võtta mõned minutid. Kui andmed on laetud, et teada saada oma mündi anonüümsuse skoore, täitke käsklus `score` järgnevalt oma TXID-ga (ilma sulgudeta):
`score [TXID]`

![WST skoor](assets/notext/47.webp)

WST kuvab seejärel tagasivaatava skoori (_Tagasivaatavad mõõdikud_), millele järgneb tulevikku vaatav skoor (_Tulevikku vaatavad mõõdikud_). Lisaks anonüümsuse skooridele näitab WST ka teie tehingu difusioonimäära basseinis, võrreldes selle anonüümsusega.

**On oluline märkida, et teie mündi tulevikku vaatav skoor tuleks arvutada TXID-st, mis pärineb teie esialgsest segamisest, mitte teie kõige hiljutisemast segamisest. Vastupidiselt arvutatakse UTXO tagasivaatav skoor viimase tsükli TXID-st.**

### Boltzmanni kalkulaatori kasutamine
Boltzmanni kalkulaator on tööriist Bitcoin'i tehingu analüüsimiseks, pakkudes võimalust mõõta selle entroopia taset teiste edasijõudnute mõõdikute hulgas. Need andmed pakuvad kvantifitseeritud hinnangut tehingu privaatsusele ja aitavad tuvastada potentsiaalseid puudusi. See tööriist on juba integreeritud teie RoninDojo sõlme, muutes selle kergesti kättesaadavaks ja kasutatavaks.

Enne Boltzmanni kalkulaatori kasutamise protseduuri üksikasjalikku kirjeldamist on oluline mõista nende näitajate tähendust, nende arvutamise meetodit ja nende kasulikkust. Kuigi need näitajad kehtivad mis tahes Bitcoin'i tehingu kohta, on need eriti kasulikud coinjoin tehingu kvaliteedi hindamiseks.

**Esimene näitaja**, mida tarkvara arvutab, on võimalike kombinatsioonide koguarv, mida näidatakse tööriistas `nb combinations` all. UTXO-de väärtuste põhjal kvantifitseerib see näitaja sisendite ja väljundite seostamise võimalike viiside arvu. Teisisõnu, see määrab, mitu usutavat tõlgendust tehing genereerida võib. Näiteks Whirlpool 5x5 mudeli järgi struktureeritud coinjoin esitab `1496` võimalikku kombinatsiooni:
![kombinatsioonid](assets/notext/50.webp)
Autor: KYCP

**Teine arvutatav näitaja** on tehingu entroopia, mida tähistatakse `Entropy`ga. Kui tehingul on suur hulk võimalikke kombinatsioone, on sageli asjakohasem viidata selle entroopiale. See on määratletud kui võimalike kombinatsioonide arvu binaarlogaritm. Siin on kasutatav valem:
- $E$: tehingu entroopia;
- $C$: tehingu võimalike kombinatsioonide arv.
$$E = \log_2(C)$$
Matemaatikas vastab binaarlogaritm (alus 2 logaritm) kahe astmesse tõstmise pöördoperatsioonile. Teisisõnu, $x$ binaarlogaritm on eksponent, milleni 2 tuleb tõsta, et saada $x$. Seega väljendatakse seda näitajat bittides. Võtame näiteks entroopia arvutamise mündiühenduse tehingu jaoks, mis on struktureeritud vastavalt Whirlpool 5x5 mudelile, mis, nagu varem mainitud, pakub `1496` võimalikku kombinatsiooni:$$ C = 1496 $$
$$ E = \log_2(1496) $$
$$ E \approx 10.5469 \text{ bitti}$$

Seega näitab see mündiühenduse tehing 10.5469 biti suurust entroopiat, mis peetakse väga rahuldavaks. Mida kõrgem see väärtus on, seda rohkem erinevaid tõlgendusi tehing lubab, suurendades seeläbi selle privaatsuse taset.

Võtame veel ühe näite tavapärasema tehinguga, mis sisaldab ühte sisendit ja kahte väljundit: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)
Selle tehingu puhul on ainus võimalik tõlgendus: `(inp 0) > (Outp 0 ; Outp 1)`. Seega on selle entroopia määratud `0` juures:
$$ C = 1 $$
$$ E = \log_2(1) $$
$$ E \approx 0 \text{ bitti}$$
**Kolmas näitaja**, mida Boltzmanni kalkulaator pakub, on nimetatud `Rahakoti Efektiivsuseks`. See näitaja hindab tehingu efektiivsust, võrreldes seda optimaalse tehinguga identsetes tingimustes. See viib meid arutlema maksimaalse entroopia kontseptsiooni üle, mis vastab kõrgeimale entroopiale, mida konkreetne tehingustruktuur teoreetiliselt saavutada võib. Seega, Whirlpool 5x5 mündiühenduse struktuuri puhul on maksimaalne entroopia määratud `10.5469` juures. Tehingu efektiivsus arvutatakse seejärel, võrreldes seda maksimaalset entroopiat analüüsitava tehingu tegeliku entroopiaga. Kasutatav valem on järgmine:
- $ER$: tehingu tegelik entroopia, väljendatuna bittides;
- $EM$: antud tehingustruktuuri maksimaalne võimalik entroopia, samuti bittides;
- $Ef$: tehingu efektiivsus, bittides.
$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$
$$Ef = 0 \text{ bitti}$$

See näitaja väljendatakse ka protsendina, selle valem on siis:
- $CR$: tegelike võimalike kombinatsioonide arv;
- $CM$: sama struktuuriga võimalike maksimaalsete kombinatsioonide arv;
- $Ef$: efektiivsus väljendatuna protsendina.
$$Ef = \frac{CR}{CM}$$
$$Ef = \frac{1496}{1496}$$
$$Ef = 100\%$$

Seega näitab `100%` efektiivsus, et tehing maksimeerib oma privaatsuse potentsiaali lähtuvalt oma struktuurist.
**Neljas näitaja**, entroopia tihedus ehk `Entropy Density`, pakub vaatenurka entroopia suhtele iga tehingu sisendi või väljundi kohta. See näitaja osutub kasulikuks erineva suurusega tehingute efektiivsuse hindamisel ja võrdlemisel. Selle arvutamiseks jagage lihtsalt tehingu koguentroopia sisendite ja väljundite koguarvuga. Võttes näiteks Whirlpool 5x5 coinjoini:
- $ED$: entroopia tihedus, väljendatuna bittides;
- $E$: tehingu entroopia, väljendatuna bittides;
- $T$: tehingus osalevate sisendite ja väljundite koguarv.
$$T = 5 + 5 = 10$$
$$ED = \frac{E}{T}$$
$$ED = \frac{10.5469}{10}$$
$$ED = 1.054 \text{ bitti}$$
**Viiendaks teabeks**, mida Boltzmanni kalkulaator pakub, on sisendite ja väljundite vaheliste vastavusvõimaluste tabel. See tabel näitab `Boltzmanni skoori` kaudu tõenäosust, et kindel sisend on ühendatud teatud väljundiga. Võttes näiteks Whirlpooli coinjoini, tõstaks tõenäosuste tabel esile iga sisendi ja väljundi vahelise seose võimalused, pakkudes kvantitatiivset mõõtu tehingu seoste ebamäärasusele või ennustatavusele:

| %       | Väljund 0 | Väljund 1 | Väljund 2 | Väljund 3 | Väljund 4 |
|---------|-----------|-----------|-----------|-----------|-----------|
| Sisend 0| 34%       | 34%       | 34%       | 34%       | 34%       |
| Sisend 1| 34%       | 34%       | 34%       | 34%       | 34%       |
| Sisend 2| 34%       | 34%       | 34%       | 34%       | 34%       |
| Sisend 3| 34%       | 34%       | 34%       | 34%       | 34%       |
| Sisend 4| 34%       | 34%       | 34%       | 34%       | 34%       |

Siin on selge, et igal sisendil on võrdne võimalus olla seotud mis tahes väljundiga, mis tugevdab tehingu ebamäärasust ja konfidentsiaalsust. Kuid lihtsa tehingu puhul, millel on üks sisend ja kaks väljundit, on olukord erinev:

| %       | Väljund 0 | Väljund 1 |
|---------|-----------|-----------|
| Sisend 0| 100%      | 100%      |

Siin näeme, et iga väljundi tulemise tõenäosus sisendist 0 on 100%. Madalam tõenäosus tähendab seega suuremat konfidentsiaalsust, lahjendades otseseid seoseid sisendite ja väljundite vahel.

**Kuuendaks teabeks**, mida pakutakse, on deterministlike linkide arv, mida täiendab nende linkide suhe. See näitaja paljastab, mitu sisendite ja väljundite vahelist ühendust analüüsitud tehingus on vaieldamatud, 100% tõenäosusega. Suhe omakorda pakub vaatenurka nende deterministlike linkide kaalule tehingu kogulinkide seas.

Näiteks Whirlpooli-tüüpi coinjoin tehing ei esita ühtegi deterministlikku linki ja seetõttu kuvatakse näitaja ja suhe 0%. Teisest küljest, meie teises vaadeldud tehingus (ühe sisendi ja kahe väljundiga) on näitaja määratud 2-le ja suhe jõuab 100%-ni. Seega nullnäitaja signaliseerib suurepärast konfidentsiaalsust tänu otsese ja vaieldamatute linkide puudumisele sisendite ja väljundite vahel.
**Kuidas pääseda ligi Boltzmanni kalkulaatorile RoninDojo's?** Boltzmanni kalkulaatori tööriista kasutamiseks minge RoninCLI juurde. Selleks avage oma isiklikus arvutis terminal ja looge oma sõlmega SSH-ühendus, kasutades järgmist käsku: `SSH ronindojo@[IP]`

Näiteks, kui teie sõlme IP-aadress on `192.168.1.40`, siis sobiv käsk oleks:
`SSH ronindojo@192.168.1.40`

Kui te muutsite 6. sammu käigus oma kasutajanime, asendades vaikimisi kasutajanime (`ronindojo`) mõne teisega, veenduge, et kasutate seda uut nime käskluses. Näiteks, kui valisite kasutajanimeks `planb` ja IP-aadress on `192.168.1.40`, siis sisestatav käsk oleks:
`SSH planb@192.168.1.40`

Teilt küsitakse kasutaja parooli. Sisestage see ja vajutage `enter` kinnitamiseks. Seejärel pääsete ligi RoninCLI liidesele. Kasutage klaviatuuril nooli, et liikuda `Samourai Toolkit` menüüsse ja vajutage `enter`, et seda valida:

![Samourai Toolkit](assets/notext/43.webp)

Seejärel valige `Boltzmann Calculator`:

![boltzmann](assets/notext/49.webp)

Jõuate tarkvara avalehele:

![boltzmann home](assets/notext/51.webp)

Sisestage uuritava tehingu TXID ja vajutage `enter` klahvi:

![boltzmann txid](assets/notext/52.webp)

Kalkulaator annab teile kõik varem arutatud näitajad:

![boltzmann result](assets/notext/53.webp)

### Teised teie RoninDojo v2 funktsioonid
Teie RoninDojo sõlm integreerib mitmesuguseid muid funktsioone. Eelkõige on teil võimalus skannida konkreetset teavet, et seda arvesse võtta. Näiteks mõnikord ei pruugi teie Samourai rahakott, mis on ühendatud RoninDojoga, kuvada teie tegelikke bitcoine. Kui saldo näitab 0, samal ajal kui olete kindel, et selles rahakotis on bitcoine, võib selle olukorra selgitada mitmel põhjusel, nagu tuletusteede viga. Kuid üks põhjuseid võib olla ka see, et teie sõlm ei jälgi korralikult teie aadresse. Selle probleemi lahendamiseks võite veenduda, et teie sõlm tõepoolest jälgib teie `xpub` kasutades _xpub tööriista_. Selle tööriista kasutamiseks RoninUI kaudu järgige teed:
`Maintenance > XPUB Tool`

Sisestage probleemi põhjustav `xpub` ja klõpsake `Check` nupul, et seda teavet kontrollida:
![xpub tool](assets/notext/54.webp)
Veenduge, et kõik tehingud on korrektselt loetletud. On oluline ka kontrollida, et kasutatud tuletustüüp vastab teie rahakoti omale. Kui see nii ei ole, klõpsake `Retype`, seejärel valige `BIP44`, `BIP49` või `BIP84` vastavalt teie vajadustele.
RoninUI `Maintenance` vahekaardil on veel palju muid kasulikke funktsioone:
- *Transaction Tool*: Võimaldab uurida konkreetse tehingu detaile;
- *Address Tool*: Võimaldab kinnitada, et teie Dojo jälgib konkreetset aadressi;
- *Rescan Blocks*: Sunnib teie sõlme uuesti skannima määratud plokkide vahemikku.

`Push Tx` vahekaart on veel üks huvitav RoninUI funktsioon, mis võimaldab edastada allkirjastatud tehingu Bitcoin võrgus. Tehing tuleb sisestada heksadesimaalses vormis.
Teie RoninUI armatuurlaua teiste vahelehtede kohta:

- `Apps`: Majutab Whirlpool rakendust ja tulevikus kasutatakse kindlasti uute rakenduste integreerimiseks;
- `Logs`: Pakub reaalajas juurdepääsu teie tarkvara sündmuslogidele;
- `System Info`: Annab üldist teavet teie sõlme kohta, nagu CPU temperatuur, salvestusruumi kasutus või RAM andmed. Leiate ka `Reboot` ja `Shut down` valikud sõlme taaskäivitamiseks või väljalülitamiseks;
- `Settings`: Võimaldab muuta teie kasutaja parooli.

Siin see on! Täname, et järgisite seda õpetust lõpuni. Kui see meeldis, julgustan teid seda jagama sotsiaalmeedias. Lisaks, kui teil on võimalus, kaaluge arendajate toetamist annetusega, kes teevad need vabad ja avatud lähtekoodiga tarkvarad meie kogukonnale kättesaadavaks: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). RoninDojo ja lisavõimaluste avastamiseks soovitan tungivalt tutvuda allpool mainitud väliste ressursside linkidega.

**Välised ressursid:**
- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/boltzmanni-tutvustus-85930984a159](https://medium.com/@laurentmt/boltzmanni-tutvustus-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)