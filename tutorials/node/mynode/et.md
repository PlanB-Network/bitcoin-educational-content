---
nimi: Minu Node
kirjeldus: Seadista oma bitcoin MyNode
---

![pilt](assets/0.webp)

https://mynodebtc.com/

Lihtsaim, võimsaim viis Bitcoin ja Lightning node'i käitamiseks! Me ühendame parima avatud lähtekoodiga tarkvara meie liidesega, halduse ja toega, et saaksite Bitcoin'i ja Lightning'it kasutada lihtsalt, privaatselt ja turvaliselt.

## Node'i seadistuste tüübid

Node'i seadistusi on mitmesuguseid. MyNode on suurepärane. Sellega kaasneb palju rakendusi ja veelgi enam, kui maksate premium versiooni eest. Muidu on kõigi nende rakenduste ise allalaadimine väga tüütu. MyNode muudab selle üsna lihtsaks, nagu näete.

Alternatiivne ja sarnane võimalus on RaspiBlitz. GUI pole nii kena ja rakendused kattuvad palju MyNode'iga kaasnevate rakendustega, kuid Raspiblitz on tasuta avatud lähtekoodiga tarkvara (FOSS) ja MyNode mitte päris. Teine erinevus on see, et MyNode töötab Dockeri konteineris. Docker tundub mulle hirmutav ja raskesti lahendatav. See on probleem ainult siis, kui ilmnevad vead või tõrked. Arendaja pakub abi premium kasutajatele ja on olemas ka Telegrami vestlusrühm.

RaspiBlitz on lihtsalt mitu programmi, mis on installitud Linuxile, ilma Dockerita. Välist kõvaketast saab hõlpsasti ühendada teise Linuxi masinaga, kus töötab Bitcoin Core, ja nii edasi, kui vaja.

Teine võimalus on lihtsalt installida Bitcoin Core ja Electrum Serveri erinevaid variante (neid on mitu) operatsioonisüsteemile. Mul on juhendid Linuxile (Raspberry Pi), Macile ja Windowsile.

## Ostunimekiri

- Raspberry Pi 4, 4Gb mälu või 8Gb (4Gb on piisav)

- Ametlik Raspberry Pi toide (Väga oluline! Ärge ostke üldist, tõsiselt)

- Korpus Pi'le. FLIRC korpus on suurepärane. Kogu korpus on jahutusradiaator ja te ei vaja ventilaatorit, mis võib olla lärmakas

- 16 Gb microSD kaart (teil on seda vaja, kuid mõned on käepärased)

- Mälukaardilugeja (enamikul arvutitel pole microSD kaardi jaoks pesa).

- Väline SSD 1Tb kõvaketas.  
  Märkus: SSD on oluline. ärge kasutage kaasaskantavat välist kõvaketast, isegi kui see on odavam

- Etherneti kaabel (ühendamiseks koduse ruuteriga)

- Te ei vaja monitori

## Laadi alla MyNode Image

Navigeeri MyNode veebilehele Link

![pilt](assets/1.webp)

Klõpsa <Download Now>

Laadi alla Raspberry Pi 4 versioon:

![pilt](assets/2.webp)

See on suur fail:

![pilt](assets/3.webp)

Laadi alla SHA 256 räsiväärtused

![pilt](assets/4.webp)

Ava terminal Macis või Linuxis või käsurida Windowsis. Tüüp:

```bash
shasum -a 256 ALLALAADITUDFAILINIMI # <--- Mac/Linux
certUtil -hashfile ALLALAADITUDFAILINIMI SHA256 # <--- Windows
```

Arvuti mõtleb umbes 20 sekundit. Seejärel kontrollige, kas väljundräsi vastab veebisaidilt eelmises etapis allalaaditud räsile. Kui see on identne, võite jätkata.
Välgu SD-kaart

## Laadi alla ja installi Balena Etcher. Link

Ma ei suutnud selle digitaalset allkirja leida. Kui teate, kuidas, andke mulle teada ja ma uuendan seda artiklit.

Etcher on kasutamisel iseenesestmõistetav. Sisestage oma micro SD kaart ja välgu Raspberry Pi tarkvara (.img fail) SD-kaardile.

![pilt](assets/5.webp)
![pilt](assets/6.webp)
Kui olete valmis, ei ole draiv enam loetav. Võite saada operatsioonisüsteemilt veateate ja draiv peaks töölaualt kaduma. Tõmmake kaart välja.

## Seadista Pi ja sisesta SD-kaart

Osad (korpust ei ole näidatud):

![image](assets/12.webp)
![image](assets/13.webp)

Ühendage etherneti kaabel ja kõvaketta USB-ühendus (veel mitte toide). Vältige ühendamist siniste USB-portidega keskel. Need on USB 3. MyNode soovitab kasutada USB 2 porti, isegi kui draiv võib olla USB 3 võimeline.

![image](assets/14.webp)

Siia läheb mikro SD-kaart:

![image](assets/15.webp)

Lõpuks ühendage toide:

![image](assets/16.webp)

## Leia Pi IP-aadress

MyNode'iga ei vaja te kunagi monitori. Teil on siiski vaja teist arvutit koduvõrgus. Kui teie Pi ei ole ühendatud etherneti kaudu ja soovite kasutada WiFi-ühendust, nõuab IP-aadressi leidmine kõrgetasemelisi arvutioskusi. Kahjuks ei saa aidata, vabandust. Teil on vaja etherneti ühendust. (Probleem tuleneb vajadusest pääseda ligi monitorile ja operatsioonisüsteemile, et ühenduda WiFi-ga ja sisestada parool).

Kontrollige oma ruuterit, et näha kõigi ühendatud seadmete IP-aadresse.

Ma tippisin brauserisse 192.168.0.1 (juhised, mis tulid minu ruuteriga), logisin sisse ja nägin seadet "MyNode" IP-aadressiga 192.168.0.18. Pange tähele, et need IP-aadressid ei ole internetis avalikult nähtavad (need läbivad esmalt ruuteri), need on lihtsalt identifikaatorid teie koduvõrgu seadmetele.

IP-aadressi leidmine on kriitilise tähtsusega.

> UUENDUS: Maci või Linuxi masinas saate kasutada terminali, et leida kõikide koduvõrgus Etherneti kaudu ühendatud seadmete IP-aadressid käsu „arp -a“ abil. Väljund ei ole nii ilus kui see, mida ruuter kuvab, kuid kõik vajalik info on olemas. Kui ei ole ilmne, milline on Pi, tehke katse-eksituse meetodil.

## SSH ühendus Pi-ga

Teil on võimalus sisse logida seadmesse kaugelt SSH käsu abil, kuid see ei ole nõutav (see on nõutav, kui kasutate RaspiBlitz Node'i). Ma näitan teile siiski, kuidas seda teha, kuna see on väga käepärane.

Avage Maci või Linuxi arvuti (Windowsi puhul laadige alla putty, SSH tööriist) ja tippige:

```bash
ssh admin@192.168.0.18
```

Kasutage oma IP-aadressi. MyNode seadme kasutajanimi on vaikimisi „admin“. Parool on vaikimisi „bolt“.

Kui olete oma Pi-d varem kasutanud ja mikro SD-kaarti vahetanud, saate selle veateate:

![image](assets/17.webp)

Teil on vaja navigeerida sinna, kus asub „known_hosts“ fail ja see kustutada. See on ohutu. Veateade näitab teile teed. Minu jaoks oli see /Users/MinuKasutajanimi/.ssh/

Ärge unustage enne ssh-d „.“, see näitab, et tegemist on peidetud kataloogiga.

Seejärel proovige SSH käsku uuesti.

Sel korral näete seda väljundit:

![image](assets/18.webp)

Kustutatud fail on kustutatud ja lisate uue sõrmejälje. Tippige yes ja vajutage <enter>.

Teilt palutakse sisestada parool. See on „bolt“.
Teil on nüüd terminali juurdepääs MyNode Pi'le, ilma monitorita, ja saate kinnitada, et kõik on sujuvalt laadinud.
![image](assets/19.webp)

## Juurdepääs veebibrauseri kaudu

Avage brauser. See peab olema arvuti teie koduvõrgus, väljastpoolt seda teha ei saa. On küll viis, kuid see on keeruline. Ma pole seda testinud.

Sisestage IP-aadress brauseri aadressiaknasse. Seejärel juhtub järgnev:

![image](assets/20.webp)

Sisestage parool “bolt” – muutke see hiljem ära.

Seejärel juhtub järgnev:

![image](assets/21.webp)

Valige Format Drive (Vorminda draiv)

![image](assets/22.webp)

Nüüd ootame.

Mingil hetkel küsitakse teilt, kas soovite sisestada oma tootevõtme või kasutada tasuta “community edition” versiooni — ma näitan Premium versiooni. Soovitan maksta Premium versiooni eest, kui teil on võimalik, see on väga seda väärt.

![image](assets/23.webp)

Seejärel näete allalaaditavate plokkide edenemist. See võtab päevi:

![image](assets/24.webp)

Masina väljalülitamine allalaadimise ajal on ohutu, kui teil on vaja. Minge seadetesse ja leidke nupp masina väljalülitamiseks. Ärge lihtsalt tõmmake juhet välja, see võib rikkuda installimise või kõvaketta.

Veenduge varakult, et lähete "Settings" (Seaded) juurde ja keelate quicksynci. See algatab esialgse plokkide allalaadimise algusest.

![image](assets/25.webp)

Tahtsin jätkata juhendi loomisega, seega siin on teine MyNode, mille ma varem ette valmistasin. See on lehekülg, kui plokiahel on sünkroniseeritud ja mitu "rakendust" on lubatud ja sünkroniseeritud:

![image](assets/26.webp)

Pange tähele, et Electrum Server peab samuti sünkroniseerima, nii et niipea, kui Bitcoin Blockchain on sünkroniseeritud, klõpsake nuppu, et alustada seda protsessi – võtab päeva või kaks. Kõik muu on lubatud mõne minuti jooksul, kui valite selle lubamise. Võite klõpsata asjadel ja uurida. Te ei riku midagi. Kui midagi siiski katki läheb (see juhtus minuga, kuid ma arvan, et kuna mul olid odavad osad), peate uuesti välklambi tegema ja allalaadimist alustama. Probleem, mis mul MyNode'iga on, on see, et kui on vaja "uuesti välklampi" teha, peate alustama plokiahela sünkroniseerimist otsast peale. On tehnilisi viise sellest mööda minna, kuid see pole lihtne.

Kui soovite proovida ka mõnda muud sõlme, näiteks RaspiBlitz, vajate lisaks SSD välist kõvaketast ja teist mikro-SD-kaarti välklambi jaoks. Muidu on varustus sama, te lihtsalt ei saa MyNode'i ja RaspiBlitz'i samaaegselt käitada, ilmselgelt. Kui soovite seda teha, on aeg osta teine Raspberry Pi.

Nüüd, kui teil on sõlm töös, kasutage seda, ärge laske sellel lihtsalt seal istuda, tehes teie jaoks mitte midagi. Järgige minu artiklit (ja videot) selle kohta, kuidas ühendada oma Electrum Desktop Wallet Electrum Serveri ja Bitcoin Core'iga siin.