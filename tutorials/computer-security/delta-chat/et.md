---
name: Delta vestlus
description: Praktiline juhend detsentraliseeritud sõnumivahendile
---

![image](assets/cover.webp)




## Sissejuhatus - Vestluskontroll ja privaatsus



Viimastel aastatel on üha enam räägitud Chat Control'ist, regulatiivsest ettepanekust, mille eesmärk on kehtestada suuremate kommunikatsiooniplatvormide privaatsõnumite automaatne skaneerimine. Eesmärgiks on võidelda ebaseadusliku sisuga, kuid probleem on selles, et see mehhanism tähendaks tegelikult massilist jälgimist, mis õõnestaks otsekohalduse krüpteerimist ja seega kõigi kasutajate, mitte ainult õigusrikkujate, eraelu puutumatust.



Tegelik oht on, et vestlused muutuvad kontrollitud keskkondadeks, kus iga sõnumit, pilti või manustust võidakse kontrollida enne, kui see jõuab vastuvõtjani. Siinkohal tulebki mängu üks võimalik lahendus: liikuda tsentraliseeritud platvormidelt detsentraliseeritud sõnumsüsteemide suunas, mis ei sõltu ühest teenusepakkujast ja mida ei saa hõlpsasti sellisele kontrollile allutada.



Üks selline lahendus esitatakse käesolevas õpiobjektis: Delta Chat. Väljakujunenud ja juba kasutatav vahend.




## Miks Delta Chat ja kuidas see toimib



Delta Chat on juba väga hea sõnumivahetuse lahendus igapäevaseks kasutamiseks: väga kasulik sõprade, pere ja teiste inimestega suhtlemiseks, justkui tõeline vaste WhatsAppile.



See on detsentraliseeritud sõnumsüsteem, mis põhineb täielikult e-kirjadel. Põhimõtteliselt kasutab see traditsioonilise e-posti infrastruktuuri, kuid ehitab selle peale kaasaegse kiirsõnumiliidese ja -kogemuse. Esmapilgul võib see tunduda veidi improviseeritud, kuid tegelikult töötab see väga hästi ja on üllatavalt töökindel. Saate kasutada spetsiaalseid e-posti servereid nimega ChatMail, kuid see võib ka sujuvalt töötada koos tavaliste e-posti serveritega. See tähendab, et saate soovi korral olemasoleva kontoga sisse logida, ilma et peaksite midagi uut looma.



Teine tipphetk on toetus WebXDC-dele, mis on väikesed veebirakendused, mida saab kasutada otse vestluste sees, sarnaselt Telegram minirakendustele. Oluline erinevus seisneb selles, et neil rakendustel ei ole Interneti-ühendust, seega ei saa nad kasutajat jälgida ega andmeid väljastpoolt saata.



Turvalisuse seisukohalt kasutab Delta Chat kontrollitud otsast lõpuni krüpteerimist, mis põhineb PGP-l, kuid millel on kaasaegsed laiendused, mis muudavad selle kaitsetaseme Signal-ga võrreldavaks. Ainus praegune puudus on Perfect Forward Secrecy, kuid see on arenev aspekt.



Kuna Delta Chat põhineb ainult e-kirjadel, välditakse seda täielikult:




- kohustuslikud telefoninumbrid
- Tsentraliseeritud ID-d
- ühe teenusega seotud registreeringud



Ja just see teebki selle tööriista väga vastupidavaks invasiivsetele regulatsioonidele, nagu näiteks Chat Control.




## Paigaldamine



Delta Chat](https://delta.chat/download) ametlikul veebisaidil saate minna allalaadimise sektsiooni. Linuxi puhul on see mugavalt kättesaadav Flathubi kaudu, kuid seal on olemas ka paketid Archile, NixOSile, Snap-le ja iseseisvatele versioonidele.



![image](assets/it/01.webp)



See on saadaval ka:




- [F-Droid](https://f-droid.org/app/com.b44t.messenger)
- [Play Store](https://play.google.com/store/apps/details?id=chat.delta)
- [iOS](https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS](https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch](https://open-store.io/app/deltatouch.lotharketterer)
- ja muud kauplused...



Kui otsite juhendit F-Droid paigaldamiseks, võib see õpetus olla teile abiks:



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

Üks väga oluline asi: töölauaversioonid ei nõua telefoni. Erinevalt WhatsAppist või SimpleX Chat-st ei pea te kõigepealt mobiililt registreeruma. Võite luua oma profiili otse arvutis või kanda selle üle mõnest teisest seadmest.




## Profiili loomine



Kui rakendus on avatud, küsib Delta Chat, kas luua uus profiil või kasutada olemasolevat.



![image](assets/it/02.webp)



Uue profiili loomisel saate sisestada:




- nimi
- pilt (valikuline)



Vaikimisi on pakutud ChatMaili server, kuid see on võimalik:




- valida teine ChatMail server
- kasutada klassikalist e-posti kontot
- iMAP ja SMTP käsitsi konfigureerimine
- registreeruda teise kasutaja kutsekoodi abil



Mõne sekundi pärast on profiil valmis ja saate hakata rakendust kasutama.



![image](assets/it/03.webp)




## Interface ja vestlus



Kasutajaliides on väga lihtne ja arusaadav:




- Seadmesõnumid, mis on kohalik side
- Salvestatud sõnumid, mis on sarnased Telegram-süsteemiga ja mida saab seadmete vahel sünkroonida



![image](assets/it/04.webp)



Kontakti lisamiseks lihtsalt:




- QR-koodi näitamine
- Skaneerige teise isiku
- Kutsuge lingi kaudu (jagage kutselinki).



![image](assets/it/05.webp)



Kui ühendus on loodud, konfigureeritakse automaatselt otsest krüpteerimist. Vestluse kasutajaliides on väga sarnane WhatsAppi kasutajaliidesele:




- tekstisõnumid ja kõnesõnumid
- fotod, videod ja failid
- vastused sõnumitele
- reaktsioonid
- pop-up sõnumid
- kohandatavad teavitused.



![image](assets/it/06.webp)



## WebXDC: rakendused vestlustes:



Delta Chat võimaldab kasutada WebXDC-d, st vestlustesse põimitud väikseid rakendusi. Siin on lühike loetelu kõige kasulikumatest tuvastatud rakendustest:




- uuringud
- joonistustahvlid
- ajutised privaatsed vestlused
- jagatud vestluse skooriga mängud



Samuti saab käivitada keerulisemaid mänge, mis näitab selle tööriista paindlikkust.



![image](assets/it/07.webp)



## Rühmad, kanalid ja täiustatud funktsioonid



Saate luua gruppe, kasutada kleebiseid (eriti lauaarvutitel) ja, kui aktiveerida eksperimentaalsed valikud, isegi kanaleid, mis on sarnased Telegram-le.



Täiustatud seadetes saate sisse lülitada:




- häälkõned (veel eksperimentaalne)
- täiustatud e-posti profiili haldamine
- täielikud varukoopiad.



![image](assets/it/08.webp)



## Mitme seadme ja varundamine



Delta Chat toetab täielikult mitut seadet:




- saate lisada teise seadme QR-koodi kaudu
- saate teha täieliku ülekande varundamise kaudu.



Sekunditega leiad oma vestlused, rühmad ja kogu ajaloo uuesti üles, ilma et sõltuksid keskserverist.



![image](assets/it/09.webp)




## Kokkuvõte



Ajal, mil üha enam räägitakse privaatse suhtluse kontrollimisest, on Delta Chat konkreetne vastus: detsentraliseeritud, krüpteeritud sõnumside, mida saab kasutada iga päev.



See on lahendus, mis kõigist minu poolt proovitud lahendustest on mind kõige enam veennud lihtsuse, privaatsuse ja vabaduse poolest. Kui soovite, võite minuga ühendust võtta ka Delta Chatis järgmise [kutselink](https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats) kaudu



Kui teile meeldis see juhend, saate mind toetada, tehes annetusi ja jättes pöidlaid üles. Ja pidage meeles: ainult Delta Chat'i kasutades ja uurides seda nii mobiiltelefoni kui ka töölaua pealt, avastate selle täieliku funktsionaalsuse.



Kuni järgmise korrani.