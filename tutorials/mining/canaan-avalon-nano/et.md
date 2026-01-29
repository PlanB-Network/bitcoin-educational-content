---
name: Canaan Avalon Nano 3S
description: ASIC Avaloni konfigureerimine solomineerimiseks või Miner koondamiseks
---

![cover](assets/cover.webp)



Selles õpetuses vaatame, kuidas seadistada Canaan Avalon Nano 3S, et Miner kodus hõlpsasti kasutada.



Siiani olid ASIC (*rakendusspetsiifiline integraallülitus*) masinad, mis olid spetsiaalselt ette nähtud konkreetse ülesande täitmiseks - antud juhul Hash arvutamine (SHA-256) Bitcoin Miner jaoks - eriti sobimatud koduseks kasutamiseks. Häiriv müra, tekkiv soojus ja vajadus kohandada oma elektripaigaldist nende seadmete tohutu võimsuse toetamiseks takistasid enamikku meist osalemast.



Täna on Canaan, üks juhtivaid ASIC masinate tootjaid, otsustanud tegeleda eraisikute turuga, kes soovivad Miner kodus, pakkudes tootevalikut, mis on suhteliselt vaikne ja väga lihtne paigaldada (plug & play).



Neid seadmeid turustatakse kas **Avalon Nano 3S (140W)** puhul lisakütteseadmena või **Avalon Mini 3** puhul **800W** võimsusega miniradiaatorina.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Pange tähele, et hinnavahe traditsiooniliste samaväärse võimsusega kütteseadmetega ei võimalda teil enamasti rahalist kasumit teenida. Mining tegevusega genereeritud satoshid ei kompenseeri kunagi seda hinnavahe, kui teil ei ole juurdepääsu tasuta (ülejäävale) või väga odavale elektrile.



Minu arvates tuleks neid seadmeid vaadelda pigem kui lihtsat viisi Miner kodus kasutamiseks neile, kes seda isiklikel põhjustel soovivad: *saada mitte-KYC Satss / mängida "loterii" solominating / osaleda Hashrate detsentraliseerimine jne...*., samas kasu **boonusena** soojuse toodetud soojuse oma toa kütmiseks talvel. Aga mitte raha kokkuhoiu võimalusena vähemalt enamasti (lääneriikides).



## Avamine ja omadused



Kõigepealt vaatame, mis on Avalon Nano 3S karbi sees.



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



Kui olete karbi avanud, leiate pappümbruse, mis sisaldab WIFI-vastuvõtjat, mille, nagu hiljem näeme, peate ühendama seadme USB-porti, et see saaks ühenduda teie kohalikku võrku. Kaasas on ka kasutusjuhend ja metallnõel, millega saate seadme vajaduse korral tehaseseadistused taastada.



![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



Kui kõik on karbist välja võetud, siis on siin, mis on käepärast: masin ise muidugi, kasutusjuhend, WIFI-vastuvõtja, eelmainitud metallist ots ja seadme Supply toide. Kaasasolev krediitkaart ei ole meie arvates mainimist väärt.



![image](assets/fr/05.webp)



Allpool on esitatud tabel, mis võtab kokku Nano 3S üldised tehnilised näitajad:




| Omadus                                      | Väärtus                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Hashi määr                                      | 6 Th/s +- 5%                                            |
| Elektritarbimine                               | 140 W                                                   |
| Müra                                                | 30 - 40 dB                                              |
| Väljundõhu temperatuuri vahemik                 | 60-70°C (ümbritseva temperatuuri juures 25°C)                |
| Kasutamise ümbritseva temperatuuri nõuded | -5 kuni 30°C                                            |
| Seadme sisendpinge vahemik                         | 28V 5A pidev                                          |
| Adapteri sisendpinge vahemik                       | 110-240V AC 50/60Hz                                     |
| Seadme suurus                                 | Pikkus: 205 mm / Laius: 115 mm / Kõrgus: 58.5 mm |
| Seadme mass                                  | 0.86 kg                                                 |

## Lokaalse võrgu sisselülitamine ja ühendamine kohaliku võrguga



Pärast lahtipakkimist asetage oma Avalon Nano 3 S võimaluse korral suhteliselt avatud kohta, et soojus saaks ringelda. Seejärel alustage väikese WIFI-vastuvõtja mooduli paigaldamisega, nagu allpool näidatud:



![image](assets/fr/06.webp)


Seejärel ühendage Supply USB-C pistik seadme USB-C porti, et seda toiteallikaga varustada.



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



Seade käivitub ja ekraanile ilmub Avalon Nano logo, millele järgneb "mobiiltelefoni" logo koos sõnadega "Palun konfigureerige võrk Avalon Family Appiga".



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



Selleks minge oma mobiilirakenduste poodi, otsige ja laadige alla rakendus **Avalon Family**.



![image](assets/fr/11.webp)


Pärast paigaldamist avage see, klõpsates üleval paremas nurgas nupul "Skip", seejärel nupul "Add" ja lõpuks nupul "Search". Veenduge, et teie nutitelefonis on Bluetooth sisse lülitatud, et seadme tuvastamine toimuks tõrgeteta.



![image](assets/fr/12.webp)


Kui rakendus on seadme tuvastanud, klõpsake sellel ja valige "Connect". Seejärel avaneb ekraan, kus saate sisestada oma WIFI-ühenduse andmed.


![image](assets/fr/13.webp)


Kui seade on ühendatud kohalikku võrku, näeb ekraan nüüd välja selline:



![image](assets/fr/14.webp)



See näitab "fiktiivset" Hashrate, kuna ühtegi basseinit ei ole veel konfigureeritud, ning seadme kellaaega, kuupäeva, võimsust ja IP Address - väga kasulik, kui soovite juurdepääsu seadme Interface-le arvuti ja brauseri kaudu (sellest lähemalt hiljem).



![image](assets/fr/15.webp)




## Ühendamine Mining pool-ga



**See osa on ühine Nano 3s ja Mini 3 jaoks, kuna protsessid on rangelt identsed**.



Sõltumata sellest, kas me tahame "solominate" või Miner "koondada", peame ühendama Mining pool-ga. Tegelikult ei ole meie seade midagi muud kui Hash tegija, kes ei ole teadlik Bitcoin võrgust. Selle ühendamine basseiniga annab talle juurdepääsu Bitcoin võrgule ja võimaldab tal saada plokkide malle töötamiseks.



### Rakenduse kasutamine Mining pool-ga ühenduse loomiseks



Valige Avalon Family'i rakenduses seade, nagu allpool näidatud. Seejärel palutakse teil automaatselt muuta seadme administraatori parooli. Kui soovite seda teha, klõpsake nupule "OK" või tühistage, kui soovite jätta vaikimisi juurdepääsuparooli "admin".


![image](assets/fr/16.webp)


Seejärel valige "Settings", seejärel "Pool Config" ja sisestage 3 soovitud basseinide parameetrid.


Poolid nr 2 ja nr 3 toimivad varukoopiana, kui üks neist peaks välja kukkuma, nii et teie Miner ei tööta asjata. Vaikimisi on Hashrate suunatud basseinile nr 1



Meie puhul valime:




- 1 - avalik bassein,
- 2 - CkPool,
- 3 - ookean.



![image](assets/fr/17.webp)



Lisateavet Mining pool-ga ühendamise kohta leiate nendest juhendmaterjalidest :



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

Kokkuvõttes on meil vaja





- koond Address, tavaliselt **stratum+tcp://xxxxxxxxxx:port**.





- "töötaja" nimi, mis koosneb *selle Bitcoin Address* ja *pseudo*, mille te oma seadme jaoks valite, kusjuures need 2 on eraldatud *punkti*ga, näiteks:**bc1qxxxxxxxxxxxxxxxxxxxxxxx.MonAvalonNano3S**





- parool, mis on tavaliselt alati "**x**"



Kui basseini andmed on sisestatud, klõpsake nuppu "Salvesta".



![image](assets/fr/18.webp)


Käivitage seade uuesti vastavalt juhistele ja oodake paar minutit, kuni teie Hashrate on suunatud eelistatud basseinile (#1).



### Brauseri kasutamine Mining pool-ga ühenduse loomiseks



Samuti saate luua ühenduse Mining pool-ga ja üldisemalt pääseda oma seadme Interface juhtimissüsteemile oma lemmikbrauseri kaudu.



Selleks sisestage brauseri otsinguribale allpool näidatud seadme IP Address, meie näites **192.168.144.6**



![image](assets/fr/15.webp)



Ilmub järgmine lehekülg, kus palutakse avada Avalon Family'i rakendus ja skaneerida rakendusega koos kuvatav QR-kood.



![image](assets/fr/20.webp)



Avage rakendus ja klõpsake 3 kriipsu üleval paremal, seejärel klõpsake skaneerimist. Skaneerige brauseri QR-kood, seejärel sisestage rakenduse administraatori parool ja klõpsake OK.



![image](assets/fr/21.webp)



Siin olete veebilehel, mis võimaldab teil oma Avaloniga suhelda. See on pigem armatuurlaud, mis näitab masina parameetreid, kui vahend masina seadistamiseks.



Kuid basseinide seaded on endiselt kättesaadavad ka sel viisil, klõpsates **"Pool Config "** all paremas nurgas.



![image](assets/fr/22.webp)



Samamoodi nagu mobiilirakenduse puhul, saate siin sisestada oma basseiniparameetrid.



![image](assets/fr/23.webp)



## Juhtige oma seadet Avalon Family rakenduse kaudu



Oleme nüüd ühendanud oma koduse Miner meie kohalikku võrku ja suunanud meie Hashrate kaevanduste basseinidesse. Nüüd avastame meie masina põhifunktsioone Avalon Family rakenduse kaudu.



Klõpsake Avaloni perekonna rakenduses Avalon Nano 3S-le vastaval ikoonil.


seejärel kuvatakse 3 menüüd: "Töörežiim", "Valguse juhtimine" ja "Seaded". Esmalt klõpsake nuppu "Töörežiim". Seejärel pakutakse teile 3 töörežiimi.



**Low**: toob teile umbes 3 Th/s Hashrate 70W energiatarbimise juures


**Keskmine**: 100 W energiatarbimise korral annab Hashrate umbes 4,5 Th/s


**Kõrge**: annab teile umbes 6 Th/s Hashrate maksimaalse tarbimise juures 140W



![image](assets/fr/31.webp)


Astume sammu tagasi ja uurime menüüd "Light Control". See on puhtalt kosmeetiline. Saadaval on terve hulk valikuid värvi, intensiivsuse, soojuse muutmiseks, seadme LED-ide väljalülitamiseks öösel jne... Seda on lihtne ise välja selgitada.



![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



Lõpuks on viimane meile kättesaadav menüü "Seaded", mida me juba nägime meie Mining basseinidega ühendamiseks. Siin saate hallata oma basseine, muuta seadme administraatori parooli ja jälgida erinevaid näitajaid, nagu garantii aegumise kuupäev, filtri puhtus või kuidas võtta rikke korral ühendust klienditoega.



![image](assets/fr/35.webp)


Hoolduseks ja filtri võimalikult puhtana hoidmiseks soovitame kasutada tolmuimejat ja regulaarselt tolmuimeerida õhu sisselaske- ja väljalaskeavad, et vältida nende ummistumist.



Oleme jõudnud selle õpetuse lõpuni, mis on õpetanud meile, kuidas ühendada meie Avalon Nano 3 S kohalikku võrku, kuidas suunata meie Hashrate Mining basseinidele ning kuidas navigeerida valikute ja seadete vahel, kasutades Avalon Family'i rakendust.



Kui soovite rohkem teada saada, vaadake meie õpetust Avaloni paremast versioonist: Mini 3.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7