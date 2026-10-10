---
name: Tails

description: Paigalda Tails USB võtmepulgale
---

![pilt](assets/cover.webp)

Kaasaskantav ja amneesiat tekitav operatsioonisüsteem, mis kaitseb sind jälgimise ja tsensuuri eest.

## Miks omada USB võtmepulka Tailsiga?

Tails (https://tails.net/) on kõige lihtsam viis alati omada turvalist arvutit, mis ei jäta jälgi arvutisse, millega seda kasutad.

Tailsi kasutamiseks lülita välja arvuti, millele sul on juurdepääs (vanemate juures, sõprade juures, internetikohvikus...) ja käivita see oma Tails USB võtmepulgaga Windowsi, macOSi või Linuxi asemel.

Pärast seda on sul töökeskkond ja suhtluskeskkond, mis on sõltumatu tavapärasest operatsioonisüsteemist ja ei kasuta kunagi kõvaketast.

Tails ei kirjuta kunagi kõvakettale ja kasutab ainult arvuti RAM-i toimimiseks. See mälu kustutatakse täielikult, kui Tails välja lülitatakse, eemaldades seeläbi kõik võimalikud jäljed.

## Mõned konkreetsed kasutusjuhtumid

Et anda sulle konkreetseid ideid Tailsiga USB võtmepulga alati kaasas kandmise eelistest, siin on väike mittetäielik nimekiri, mille on koostanud Agora256 meeskond:

- Ühendu Interneti ja Toriga tsenseerimata ja anonüümsel viisil, et sirvida veebisaite ilma jälgi jätmata;
- Ava PDF kahtlaselt veebilehelt;
- Testi oma Bitcoini privaatvõtme varukoopiat Electrumi rahakotiga;
- Kasuta kontoritarkvara (LibreOffice) ja tööta arvutis, mis ei kuulu sulle;
- Astu oma esimesed sammud Linuxi keskkonnas, et õppida lahkuma Microsofti ja Apple'i maailmast.

## Kuidas usaldada Tailsi?

Tarkvara kasutamisel on alati usalduse element, kuid see ei pea olema pime. Tööriist nagu Tails peab püüdma pakkuda oma kasutajatele vahendeid usaldusväärsuse tagamiseks. Tailsi jaoks tähendab see:

- Avalik lähtekood: https://gitlab.tails.boum.org/;
- Projekt põhineb mainekatel projektidel: Tor ja Debian;
- Kontrollitavad ja reprodutseeritavad allalaadimised;
- Erinevate isikute ja organisatsioonide soovitused.

## Paigaldus- ja kasutusjuhend

Selle paigaldusjuhendi eesmärk on juhendada sind läbi iga paigaldusetapi. Me ei kirjelda rohkem tegevusi kui ametlik juhend, kuid suuname sind õiges suunas, andes samal ajal näpunäiteid ja trikke.

Praktilise kogemuse tõttu keskenduvad need näpunäited macOSi ja Linuxi platvormidele.
🛠️
Enne selle protseduuri alustamist veendu, et sul on USB võtmepulk vähemalt 150 MB/s lugemiskiirusega ja vähemalt 8 GB mahuga, ideaalis USB 3.0.

Eeltingimused:

- 1 USB võtmepulk, ainult Tailsi jaoks, vähemalt 8 GB mahuga
- Internetiga ühendatud arvuti Linuxi, macOSi, (või Windowsiga)
- Umbes üks tund vaba aega, sõltuvalt sinu Internetiühenduse kiirusest, sealhulgas ½ tundi paigaldamiseks (1.3 GB faili allalaadimiseks)

## 1. samm: Laadi Tails alla oma arvutisse

![pilt](assets/1.webp)

> 🔗 Ametlik Tailsi jaotis: https://tails.net/install/linux/index.fr.html#download

Paigaldusfaili .img laiendiga allalaadimine võib võtta aega sõltuvalt sinu Interneti allalaadimiskiirusest, nii et planeeri ette. Kaasaegse ja tõhusa ühenduse korral võtab see vähem kui 5 minutit.

Salvesta fail tuntud kausta, näiteks Allalaadimised, kuna see on vajalik järgmiseks sammuks.

## 2. samm: Kontrolli oma allalaadimist

![pilt](assets/2.webp)
🔗 Ametlik Tailsi jaotis: https://tails.net/install/linux/index.fr.html#verify
Allalaadimise kontrollimine tagab, et see pärineb Tailsi arendajatelt ja ei ole allalaadimise käigus rikutud ega pealtkuulatud.

On võimalik käsitsi kontrollida, kas just allalaaditud fail on oodatud fail, kasutades PGP-d, kuid ilma põhjalike teadmisteta pakub see kontrollimine sama turvatase kui JavaScripti kontrollimine allalaadimislehel, olles samal ajal palju keerulisem ja vigadele altim.

Faili kontrollimiseks kasutage ametlikus jaotises pakutud "Vali oma allalaadimine..." nuppu!

## 3. samm: Installi Tails oma USB mälupulgale

![image](assets/3.webp)

> 🔗 Ametlik Tailsi jaotis:
>
> - Linux: https://tails.net/install/linux/index.fr.html#install
> - macOS: https://tails.net/install/mac/index.fr.html#etcher ja https://tails.net/install/mac/index.fr.html#install

See samm, Tailsi installimine oma USB mälupulgale, on kogu juhendi kõige keerulisem, eriti kui sa pole seda varem teinud. Kõige olulisem on valida oma operatsioonisüsteemi jaoks ametlikus jaotises õige protseduur: Linux või macOS.

Kui tööriistad on soovitatud viisil paigaldatud ja ette valmistatud, saab .img laiendiga faili kopeerida oma mälupulgale (kustutades kõik olemasolevad andmed), et muuta see iseseisvalt "käivitatavaks".

Edu! ja kohtumiseni 4. sammus.

## 4. samm: Taaskäivita oma Tailsi USB mälupulgal

![image](assets/4.webp)

> 🔗 Ametlik Tailsi jaotis: https://tails.net/install/linux/index.en.html#restart
> On aeg käivitada üks oma arvutitest kasutades sinu uut USB mälupulka. Sisesta see ühte oma USB porti ja taaskäivita!

> 💡 Enamik arvuteid ei käivitu automaatselt Tailsi USB mälupulgalt, kuid saad vajutada käivitusmenüü klahvi, et kuvada nimekiri võimalikest seadmetest, millelt käivitada.

Selleks, et teada saada, millist klahvi vajutada, et tagada käivitusmenüü, mis võimaldab valida USB mälupulga tavapärase kõvaketta asemel, siin on mittetäielik nimekiri tootjate kaupa:

| Tootja       | Klahv            |
| ------------ | ---------------- |
| Acer         | F12, F9, F2, Esc |
| Apple        | Option           |
| Asus         | Esc              |
| Clevo        | F7               |
| Dell         | F12              |
| Fujitsu      | F12, Esc         |
| HP           | F9               |
| Huawei       | F12              |
| Intel        | F10              |
| Lenovo       | F12              |
| MSI          | F11              |
| Samsung      | Esc, F12, F2     |
| Sony         | F11, Esc, F10    |
| Toshiba      | F12              |
| teised...    | F12, Esc         |

Kui USB mälupulk on valitud, peaksid nägema seda uut käivitusekraani, mis on väga hea märk, nii et lase arvutil jätkata käivitumist...

![image](assets/5.webp)

## 5. samm: Tere tulemast Tailsi!

![image](assets/6.webp)

> 🔗 Ametlik Tailsi jaotis: https://tails.net/install/linux/index.en.html#tails

Üks või kaks minutit pärast alglaadurit ja laadimisekraani ilmub tervitusekraan.

![image](assets/7.webp)

Tervitusekraanil vali oma keel ja klaviatuuri paigutus keele & piirkonna jaotises. Klõpsa alusta Tailsiga.

![image](assets/8.webp)
Kui teie arvuti ei ole teie võrguga juhtmega ühendatud, palun vaadake ametlikke Tails'i juhiseid, mis aitavad teil ühenduda oma võrguga ilma Wi-Fi'ta (jaotis "Testi oma Wi-Fi").
Kui olete ühendatud kohaliku võrguga, ilmub Tor Connection võlur, mis aitab teil ühenduda Tor võrguga.

![image](assets/9.webp)

Võite alustada anonüümset sirvimist, uurida Tailsis kaasas olevaid võimalusi ja tarkvara. Nautige, teil on palju ruumi vigadeks, kuna USB pulgal ei muudeta midagi... Teie järgmine taaskäivitus on unustanud kõik teie kogemused!

## Tulevases juhendis...

Kui olete natuke rohkem katsetanud oma Tails USB pulgaga, uurime teises artiklis muid edasijõudnumaid teemasid, nagu:

> Uuenda võtit Tailsi viimase versiooniga; Seadista ja kasuta püsimälu; Paigalda lisatarkvara.
> Seni, nagu alati, kui teil on küsimusi, jagage neid julgelt Agora256 kogukonnaga. Õpime koos olema homme paremad kui täna!