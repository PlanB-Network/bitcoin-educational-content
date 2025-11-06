---
name: Canaan Avalon Mini 3
description: ASIC Avaloni konfigureerimine solomineerimiseks või Miner koondamiseks
---

![cover](assets/cover.webp)



Selles õpetuses vaatame, kuidas Canaan Avalon Mini 3 seadistada, et Miner kodus hõlpsasti kasutada.



Siiani olid ASIC (*rakendusspetsiifiline integraallülitus*) masinad, mis olid spetsiaalselt ette nähtud konkreetse ülesande täitmiseks - antud juhul Hash arvutamine (SHA-256) Bitcoin Miner jaoks - eriti sobimatud koduseks kasutamiseks. Häiriv müra, tekkiv soojus ja vajadus kohandada oma elektripaigaldist nende seadmete tohutu võimsuse toetamiseks takistasid enamikku meist osalemast.



Täna on Canaan, üks juhtivaid ASIC masinate tootjaid, otsustanud tegeleda eraisikute turuga, kes soovivad Miner kodus, pakkudes tootevalikut, mis on suhteliselt vaikne ja väga lihtne paigaldada (plug & play).



Neid seadmeid turustatakse kas **Avalon Nano 3S (140W)** puhul lisakütteseadmena või **Avalon Mini 3** puhul **800W** võimsusega miniradiaatorina.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

Pange tähele, et hinnavahe traditsiooniliste samaväärse võimsusega kütteseadmetega ei võimalda teil enamasti rahalist kasumit teenida. Mining tegevusega genereeritud satšid ei kompenseeri kunagi seda hinnavahe, kui teil ei ole juurdepääsu tasuta (ülejäävale) või väga odavale elektrienergiale.



Minu arvates tuleks neid seadmeid vaadelda pigem kui lihtsat viisi Miner kodus kasutamiseks neile, kes seda isiklikel põhjustel soovivad: *saada mitte-KYC Satss / mängida "loterii" solominating / osaleda Hashrate detsentraliseerimine jne...*., samas kasu **boonusena** soojuse toodetud soojuse oma toa kütmiseks talvel. Aga mitte raha kokkuhoiu võimalusena vähemalt enamasti (lääneriikides).



## Avamine ja omadused



### Avalon Nano 3S



Kõigepealt vaatame, mis on Avalon Mini 3 karbis sees.



![image](assets/fr/24.webp)



Kui avate karbi, on kasutusjuhend otse teie ees, kuid mis veelgi tähtsam, WIFI-vastuvõtja moodul on peidetud kasutusjuhendist vasakul asuva valge ümmarguse kleebise alla. Seda vajate hiljem.



![image](assets/fr/25.webp)



Vahtploki all on seade, seejärel, kui see on karbist eemaldatud, võimsus Supply seade.



![image](assets/fr/26.webp)




![image](assets/fr/27.webp)



## Lokaalse võrgu sisselülitamine ja ühendamine kohaliku võrguga



Pärast lahtipakkimist asetage oma Avalon Mini 3 võimaluse korral suhteliselt avatud kohta, et soojus saaks korralikult ringelda. Seejärel alustage väikese WIFI-vastuvõtja mooduli sisestamisest seadme allosas asuvasse USB-porti, ühendage vooluvõrk Supply ja veenduge, et toitenupp on asendis "1".



![image](assets/fr/28.webp)



Kui need sammud on lõpetatud, süttib seadme LED-ekraan ja näitab sümbolit "Bluetooth", mis näitab, et seade on valmis ühendamiseks teie kohalikku võrku rakenduse Avalon Family kaudu.



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Selleks minge oma mobiilirakenduste poodi, otsige ja laadige alla rakendus **Avalon Family**.



![image](assets/fr/11.webp)


Pärast paigaldamist avage see, klõpsates üleval paremas nurgas nupul "Skip", seejärel nupul "Add" ja lõpuks nupul "Search". Veenduge, et teie nutitelefonis on Bluetooth sisse lülitatud, et seadme tuvastamine toimuks tõrgeteta.



![image](assets/fr/12.webp)


Kui rakendus on seadme tuvastanud, klõpsake sellel ja valige "Connect". Seejärel avaneb ekraan, kus saate sisestada oma WIFI-ühenduse andmed.


![image](assets/fr/13.webp)


Kui Mini 3 on ühendatud kohalikku võrku, kuvatakse ekraanil teave, nagu IP Address, kellaaeg, Hashrate ja elektriline võimsus.



Allpool on esitatud kokkuvõtlik tabel Mini 3 üldiste tehniliste näitajate kohta:



| Caractéristique                                      | Valeur                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Consommation électrique                              | 800 W                                                     |
| Bruit                                                | 35-55 dB                                                  |
| Température de l'air en sortie                       | 60-70°C (sous température ambiante 25°C)                  |
| Exigences de température ambiante pour l'utilisation | -5° C - 40°C                                              |
| Plage d'entrée de l'appareil                         | 110V-240V AC 50/60Hz                                      |
| Taille de la machine                                 | Longueur: 760 mm / Profondeur: 104 mm / Hauteur: 214.5 mm |
| Poids de la machine                                  |  8.35 kg                                                  |

## Ühendamine Mining pool-ga



**See osa on ühine Nano 3s ja Mini 3 seadmetele, kuna protsessid on rangelt identsed **



Olenemata sellest, kas me tahame "solominate" või Miner "koondada", peame ühendama Mining pool-ga. Tegelikult ei ole meie seade midagi muud kui Hash tegija, kes ei ole teadlik Bitcoin võrgust. Ühendamine pooliga annab talle juurdepääsu Bitcoin võrgule ja võimaldab tal saada töötamiseks plokkide malle.



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



Klõpsake rakenduse Avalon family peamenüüs Avalon Mini 3 ikoonile vastaval ikoonil. Saate otse töörežiimide haldamise menüüsse.



saadaval on 3 võimalust: "Kütte", "Mining" või "Öö" režiim.





- Režiimis "Heater" on 2 võimsustaset "Eco" või "Super".


Öko-tase vastab 500 W küttevõimsusele Hashrate juures, mis on umbes 25 Th/s, ja 40 dB helitasemele.


"Super" tase vastab 650 W väljundvõimsusele umbes 30Th/s ja 45 dB juures. See režiim võimaldab määrata maksimaalse ümbritseva keskkonna temperatuuri, millest kõrgemal seade lõpetab töö.



![image](assets/fr/36.webp)




- Režiimis "Mining" töötab seade maksimaalsel kiirusel, ilma et oleks võimalik määrata sihttemperatuuri (peale sisseehitatud ülekuumenemise piirväärtuse muidugi). Eesmärgiks on kasutada Miner jõudlust maksimaalselt ära. Siin läheneb väljundvõimsus 800 W umbes 37,5 Th/s ja müratase 50-55 dB.



![image](assets/fr/37.webp)


Lõpuks, režiimis "Öö" töötab teie Mini 3 madalaimal võimalikul kiirusel ja minimaalse müraga. 400 W, 20 Th/s ja umbes 33 dB.



Ka siin saate määrata sihttemperatuuri, mille ületamisel seade läheb inaktiivsesse režiimi ja peatab Miner. Kui temperatuur langeb, käivitub seade uuesti ja jätkab kütmist ja Miner. Selles režiimis on näidiku LED-id vaikimisi välja lülitatud, kuid vajaduse korral saate need sisse lülitada, et valgustada ruumi pimedal ajal nagu öösel (vt allpool olevat fotot).



![image](assets/fr/38.webp)



![image](assets/fr/39.webp)



Lõpuks saate mängida oma Avaloni valgusdioodidega menüüst "Display". Saate valida, kas kerida läbi asjakohast tööinfot, valida aja kuvamise või isegi kohandatud (pikslilise) pildi kuvamise.



![image](assets/fr/40.webp)



![image](assets/fr/41.webp)



Nagu ka Avalon Nano 3S puhul, saate menüüst "Seaded" muuta administraatori parooli, basseiniseadistusi, kontrollida filtri ummistumist (asub seadme alumisel küljel), võtta ühendust klienditoega või vaadata seadme logisid.



![image](assets/fr/42.webp)



Seadme põhjas asuvat filtrit saab puhastada tolmuimejaga, mida regulaarsemalt, seda parem.



Oleme jõudnud selle õpetuse lõpuni, mis on õpetanud meile, kuidas ühendada meie Avalon Mini 3 kohalikku võrku, kuidas suunata meie Hashrate Mining basseinidele ning kuidas navigeerida valikute ja seadete vahel, kasutades Avalon Family'i rakendust.



Kui soovite rohkem teada saada, vaadake meie õpetust Avaloni väiksema versiooni kohta: Nano 3S.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6