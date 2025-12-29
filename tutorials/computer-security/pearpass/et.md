---
name: PearPass
description: Võta tagasi kontroll oma paroolide üle kohaliku, võrdõiguslikkusega ja pilvevaba paroolihalduriga
---

![cover](assets/cover.webp)



Ajal, mil iga inimene haldab kümneid, isegi sadu veebikontosid, on sisselogimise turvalisus muutunud IT-turbe keskseks küsimuseks. Sotsiaalvõrgustikud, sõnumsüsteemid, professionaalsed teenused, finantsplatvormid: iga selline juurdepääs tugineb saladusele, mille ohustamine võib teie elu suhtes tõsiseid tagajärgi kaasa tuua.



Vaatamata rünnakute arvu suurenemisele on halvad tavad elanikkonna seas endiselt laialt levinud: nõrgad paroolid, korduvkasutatavad paroolid, selge tekstina salvestatud paroolid või ligikaudu meeldejäetud paroolid. Nende probleemide lahendamiseks, ilma et elu igapäevaselt keerulisemaks muutuks, on lahenduseks paroolihalduri kasutamine.



Paroolihaldureid on juba olemas kümneid ja Plan ₿ Academy pakub enamiku neist õpetust. Kuid selles õpetuses tahaksin teile tutvustada ühte, mis oma tööpõhimõttelt selgelt eristub teistest: **PearPass**.



**PearPass on avatud lähtekoodiga, kohalik-pealt, peer-to-peer paroolihaldur, mis on loodud selleks, et anda kasutajatele täielik kontroll oma andmete üle



![Image](assets/fr/01.webp)



## Miks valida PearPass?



Paroolihaldur on tarkvara, mis genereerib, salvestab ja organiseerib kõik teie paroolid turvaliselt. Selle asemel, et paroole meelde jätta või uuesti kasutada, on teil ainult üks saladus, mida kaitsta: põhiparool, mis krüpteerib kogu teie seifi. Selline lähenemine võimaldab kasutada iga teenuse jaoks unikaalseid, pikki ja juhuslikke paroole, vähendades nii unustamise kui ka kompromissi ohtu, piirates samas võimaliku lekke mõju. Tänapäeval on see põhiline IT-vahend, mida igaüks peaks kasutama.



On olemas kaks peamist kategooriat paroolihaldurit. Ühest küljest on ainult kohalik tarkvara, mis on väga turvaline, kuna andmeid ei salvestata kunagi keskserverisse, kuid mitte väga praktiline, kuna ei võimalda lihtsalt sünkroniseerida oma andmeid mitme seadme vahel (arvuti, nutitelefon, tahvelarvuti...). Seevastu pilvepõhised paroolihaldurid salvestavad teie volitusi oma serverites ja sünkroonivad neid kõigis teie seadmetes. Nende peamiseks eeliseks on mugavus, kuid need sisaldavad kompromissi turvalisuse osas, kuna teie paroole hoitakse infrastruktuurides, mille üle teil puudub kontroll.



PearPass rikub teadlikult mõlema mudeliga. See paigutab end kohalike haldurite ja pilvelahenduste vahele: see võimaldab teie paroolide sünkroniseerimist, tagades samas, et neid ei salvestata kunagi kaugserveritesse. Selle tulemusena salvestatakse kõik teie volitused lokaalselt teie seadmetes ja sünkroonimine mitme masina vahel toimub eranditult peer-to-peer. Selline arhitektuur välistab tsentraliseeritud andmebaasidega seotud üksikud rikkekohad: ei ole servereid, mida ohustada, ega kolmanda osapoole infrastruktuuri, mis pääseks teie volitustele ligi. Teie seadmete vaheline side on otsast lõpuni krüpteeritud, mis tagab, et juurdepääs andmetele on võimalik ainult teie valduses olevate võtmete abil.



![Image](assets/fr/02.webp)



Nagu nimigi ütleb, tugineb PearPass selle võimaldamiseks **Pears**-le, mis on serverivabade rakenduste loomisele ja täitmisele pühendunud peer-to-peer-tehnoloogia ökosüsteem. Pears pakub täitmiskeskkonda, jaotamismehhanisme ja võrgukihte, mis on vajalikud täielikult detsentraliseeritud rakenduste käivitamiseks, mis on võimelised sünkroonima otse peeride vahel, ilma keskse infrastruktuurita. PearPassi puhul pakub Pears seadme tuvastamist, krüpteeritud ühenduse loomist ja paroolihoidla sünkroniseerimist teie masinate vahel. Selline lähenemisviis tagab, et PearPass jääb toimivaks, vastupidavaks ja sõltumatuks mis tahes välisest asutusest.



https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Lisaks uuenduslikule arhitektuurile on PearPass täielikult avatud lähtekoodiga ja kõik selle funktsioonid on tasuta. Tarkvara on sõltumatult auditeerinud ka Secfault Security. Lisaks oma erilisele arhitektuurile pakub PearPass muidugi kõiki klassikalisi funktsioone, mida ühelt healt paroolihaldurilt oodatakse ja mida me selle õpetuse käigus avastame.



Lühidalt öeldes, kui traditsioonilised paroolihaldurid paluvad teil usaldada ettevõtet ja selle servereid, siis PearPass kasutab suveräänsuse loogikat: ei mingit pilve, tsentraliseeritud kontosid ega vahendajaid. Teil säilib ainukontroll oma volituste üle, samas saate kasu oma seadmete vahelisest sünkroniseerimisest.



## Kuidas paigaldada PearPass?



PearPass on saadaval kõigil platvormidel: Windows, Linux, macOS, Android, iOS ja veebilehitseja laiendused. Pears ei ole vaja oma masinasse paigaldada: PearPass töötab iseseisvalt.



### Paigaldamine Windowsis



Windowsis on PearPass tarnitud klassikalise paigaldusprogrammina. Mine [ametlikule allalaadimislehele](https://pass.pears.com/download), seejärel klõpsa nupule `Download Windows installer`.



Kui fail on alla laaditud, avage paigaldusprogramm ja järgige nõustaja poolt näidatud samme. Seejärel pääseb rakendusele ligi menüüst "Start Menu" või töölaua otsetee kaudu.



![Image](assets/fr/03.webp)



### Paigaldamine macOS-i



MacOS-i puhul levitatakse PearPassi plaadikujutisena (`.dmg`). Mine [ametlikule allalaadimislehele](https://pass.pears.com/download) ja vali oma Maci arhitektuurile (Intel või Apple Silicon) vastav versioon. Pärast allalaadimist avage `.dmg` fail ja käivitage rakendus kaustast `Applications`.



Esimesel käivitamisel kuvab macOS turvateate, mis näitab, et rakendus on tulnud internetist: jätkamiseks tuleb lihtsalt kinnitada.



### Paigaldamine Linuxile



Linuxis on PearPass saadaval `.AppImage` formaadis, mis tagab laiaulatusliku ühilduvuse enamiku distributsioonidega ilma spetsiifiliste sõltuvusteta. Laadige `.AppImage` fail alla [ametlikult allalaadimislehelt](https://pass.pears.com/download), seejärel käivitage see otse topeltklõpsuga.



Sõltuvalt teie keskkonnast võib olla vaja teha fail käivitatavaks faili omaduste kaudu (paremklõps) või käsuga `chmod +x`. Pärast autoriseerimist käivitub PearPass iseseisva rakendusena.



### Brauseri laienduse paigaldamine



PearPass pakub veebilehitseja laiendust automaatseks sisselogimiseks ja kiireks juurdepääsuks oma seifile veebi sirvimise ajal. Laiendus on praegu saadaval Google Chrome'ile ja sellega ühilduvatele brauseritele. Selle installimiseks minge [ametlikule allalaadimislehele](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/04.webp)



Kui see on lisatud, saate selle kiireks juurdepääsuks tööriistaribale kinnitada. Laienduse aktiveerimiseks on seejärel vaja linki PearPassi rakendusega, mis on teie arvutisse lokaalselt paigaldatud (selle juurde tuleme hiljem õpetuses tagasi).



### Paigaldamine iOS-i ja Androidile



IPhone'i ja Androidi puhul laadige rakendus lihtsalt alla oma rakenduste poest:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store](https://apps.apple.com/us/app/pearpass/id6752954830).



![Image](assets/fr/05.webp)



Lisaks nendele klassikalistele paigaldusmeetoditele on võimalik tarkvara alla laadida ka otse GitHubi repositooriumidest, iga :




- [Desktop](https://github.com/tetherto/pearpass-app-desktop);
- [Mobile](https://github.com/tetherto/pearpass-app-mobile);
- [brauseripikendus](https://github.com/tetherto/pearpass-app-browser-extension).



Kui PearPass on paigaldatud ühele või mitmele platvormile, saate edasi minna esialgse konfiguratsiooni juurde. Selles õpetuses alustame tarkvara konfigureerimisega töölaual, seejärel sünkroniseerime selle brauseripikenduse ja mobiilirakendusega.



## Kuidas luua PearPassi seif?



Kui käivitate PearPassi arvutis esimest korda, juhendab rakendus teid kahe sammu kaudu: põhiparooli määramine ja seejärel esimese seifi loomine.



### Peaparooli määramine



Kui rakendus käivitatakse töölaual esimest korda, klõpsake nupule "Siirdu" ja seejärel nupule "Jätka", et läbida sissejuhatusekraan ja jõuda peaparooli konfigureerimise etapini.



![Image](assets/fr/06.webp)



Järgmisena tuleb oluline samm, milleks on põhiparooli valimine. Nagu nägime sissejuhatuses, on see parool väga oluline, sest see annab teile juurdepääsu kõigile teie teistele haldurisse salvestatud paroolidele. Tehniliselt kasutatakse seda teie andmete krüpteerimiseks kasutatavate krüptograafiliste võtmete tuletamiseks.



Peaparooliga kaasneb kaks peamist ohtu: kaotus ja kompromiss. Kui kaotate juurdepääsu sellele paroolile, ei pääse te enam oma sisselogimisandmetele ligi. PearPass ei säilita kunagi teie põhiparooli: **Kui see kaotatakse, on teie sisselogimisandmed jäädavalt kadunud**. Taastamismehhanismi ei ole. Seevastu, kui see parool on ohus ja ründaja saab juurdepääsu ühele teie seadmetele, saab ta ligipääsu kõikidele teie kontodele.



Kaotuse riski piiramiseks võite teha oma põhiparoolist füüsilise varukoopia, näiteks paberil, ja hoida seda turvalises kohas. Ideaaljuhul sulgege see varukoopia ümbrikusse, et saaksite regulaarselt kontrollida, et sellele ei ole ligi pääsenud. Teisest küljest ärge kunagi tehke sellest paroolist digitaalset varukoopiat.



Selleks, et vähendada kompromissi ohtu, peab teie põhiparool olema tugev. See peaks olema võimalikult pikk, sisaldama mitmesuguseid sümboleid ja olema valitud tõeliselt juhuslikult. 2025. aasta soovitused nõuavad vähemalt 13 tähemärki, sealhulgas suur- ja väiketähti, numbreid ja sümboleid, tingimusel, et parool on juhuslik. Ma soovitaksin siiski vähemalt 20 tähemärki, kui mitte rohkem, sisaldades igat liiki sümboleid, et tagada püsivam turvalisuse tase.



Sisestage oma põhiparool ettenähtud väljale, kinnitage see teist korda ja vajutage seejärel nupule "Jätka".



![Image](assets/fr/07.webp)



Seejärel suunatakse teid ümber sisselogimisekraanile: sisestage oma põhiparool, et kontrollida, kas kõik toimib õigesti.



![Image](assets/fr/08.webp)



### Loo oma esimene seif



Kui olete sisse loginud, palub PearPass teil luua oma esimene seif. Seif on krüpteeritud konteiner, milles hoitakse teie paroole, ID-d, turvalisi märkmeid ja muud teavet. Iga seif on isoleeritud ja seda saab identifitseerida erineva nimega, mis võimaldab teil oma andmeid vastavalt kasutusalale (isiklik, tööalane, konkreetsed projektid...) korraldada.



Klõpsake nupul `Loo uus hoidla`.



![Image](assets/fr/09.webp)



Valige sellele hoidlale nimi ja klõpsake loomise lõpetamiseks uuesti nuppu `Loo uus hoidla`.



![Image](assets/fr/10.webp)



Teie seif on kohe kasutusvalmis. Saate kohe alustada paroolide, sisselogimise või turvaliste märkmete lisamist.



![Image](assets/fr/11.webp)



## Kuidas lisada PearPassile sisselogimine?



Kui olete oma seifi loonud, võite hakata oma esemeid sinna salvestama. PearPass toetab paljude esemetüüpide registreerimist:




- sisselogimine saidile või teenusele ;
- identiteet: teie isikuandmed vormide kiireks täitmiseks, aga ka isikut tõendavate dokumentide salvestamiseks otse PearPassis ;
- krediitkaart: teie krediitkaardi numbrid kiiremaks maksmiseks veebiostude tegemisel;
- Wi-Fi: Wi-Fi võrkude paroolid ;
- PassPhrase: mitmest sõnast koosnev salajane fraas (hoiatus: soovitan tungivalt mitte kasutada seda wallet Bitcoin mnemofraaside puhul);
- märkus: turvaliste märkuste loomine ;
- custom: see funktsioon võimaldab teil luua kohandatud elemenditüübi, mis on kohandatud teie erivajadustele.



Alustage PearPassi avamisega ja logige sisse oma põhiparooliga.



![Image](assets/fr/12.webp)



Valige seif, kuhu soovite selle tunnuse salvestada.



![Image](assets/fr/13.webp)



Vajutage avalehel nupule, et lisada uus kirje, sõltuvalt sellest, millist teavet soovite salvestada. Minu puhul tahan lisada oma konto sisselogimise Plan ₿ Academy veebisaidil: seega klõpsan nupule `Create a Login` (loo sisselogimine).



![Image](assets/fr/14.webp)



Kui olete valinud elemendi tüübi, mida soovite lisada, ilmub vorm, mis võimaldab teil sisestada kõnealuse teenusega seotud teavet. Sõltuvalt teie vajadustest saate sisestada teenuse nime, sisselogimise, salasõna ja vajaduse korral veebisaidi aadressi ning lisamärkusi.



PearPassil on ka parooligeneraator, mis võimaldab teil luua tugeva parooli otse vormilt. Selle kasutamiseks klõpsake kolme väikest punkti kujutaval ikoonil väljal `Password`, valige soovitud pikkus ja seejärel klõpsake `Insert password`.



Kui kõik väljad on täidetud, klõpsake nupule "Salvesta", et salvestada identifikaator seifis.



![Image](assets/fr/15.webp)



Identifikaator on nüüd salvestatud. See ilmub valitud seifi esemete loendisse ja seda saab vaadata, kui klõpsata sellel.



![Image](assets/fr/16.webp)



Elementi saab hõlpsasti muuta, klõpsates sellel ja seejärel nupul "Muuda". Samuti saate selle kustutada, klõpsates kolmele väikesele punktile kasutajaliidese paremas ülaosas ja seejärel nupule "Kustuta element".



![Image](assets/fr/22.webp)



Mobiilis jääb loogika samaks, kuigi kasutajaliides on kohandatud. Pärast sisselogimist valige soovitud seif, koputage nupule "+", valige loodava eseme tüüp ja täitke seejärel vajalikud andmed.



![Image](assets/fr/17.webp)



## Kuidas korraldada PearPassi?



Nagu me nägime eelmistes punktides, võimaldab PearPass teil luua mitu erinevat võlvkonda. See võimaldab eraldada erinevaid kasutusalasid ja kujutab endast teie paroolihalduri esimest organiseerimistasandit. Avalehelt saate hõlpsasti ühelt võlvilt teisele üle minna, klõpsates liidese vasakus ülaservas oleval noolega.



![Image](assets/fr/18.webp)



Teine võimalus oma paroole korraldada, isegi varakambri sees, on luua kaustu. Selleks klõpsake kasutajaliidese vasakpoolses veerus "Kõik kaustad" kõrval olevale sümbolile "+" ja sisestage seejärel kausta nimi, mida soovite luua.



![Image](assets/fr/19.webp)



Seejärel saate salvestada oma valitud identifikaatorid kas otse objekti loomisel või hiljem, klõpsates nupule "Muuda". Teil tuleb vaid valida vormi vasakus ülanurgas soovitud kaust.



![Image](assets/fr/20.webp)



Pärast elemendi, näiteks sisselogimise avamist saate klõpsata kasutajaliidese paremas ülaosas oleval tärni ikoonil, et lisada see oma lemmikute hulka. Lemmikud saab kiiresti leida lisaks oma põhikaustale ka spetsiaalsest kaustast.



![Image](assets/fr/21.webp)



Lõpuks on kasutajaliidese ülaosas otsinguriba, nii et saate kiiresti leida otsitava objekti, isegi kui teie võlv sisaldab palju identifikaatoreid.



## Kuidas ma sünkroonin PearPassi oma mobiilis?



Nüüd, kui teil on arvutisse salvestatud elementidega töötav võlv, soovite tõenäoliselt oma paroolidele ligi pääseda ka nutitelefonist või muust seadmest. PearPass võimaldab teil sünkroonida oma haldurit mitmel masinal turvaliselt, kasutades Pears. Uurime, kuidas.



Alustuseks logige lähtemasinas (näiteks teie arvutis) oma peaparooliga oma võlvkambrisse sisse. Kui olete avalehel, klõpsake nupule `Add a Device`, mis asub kasutajaliidese paremas allosas.



![Image](assets/fr/23.webp)



PearPass genereerib seejärel kutselinki, mis on saadaval ka QR-koodina, et sünkroonida valitud hoidla teie valitud seadmes.



![Image](assets/fr/24.webp)



Kui soovite sünkroonida oma mobiilseadmes, installige esmalt rakendus ja käivitage see seejärel. Teil palutakse luua mobiilihalduri põhiparool. Saate valida, kas kasutada sama parooli, mis arvutis, või teistsugust parooli. Igal juhul järgige samu soovitusi: tugev, juhuslik parool, mis on salvestatud füüsilisele andmekandjale.



![Image](assets/fr/25.webp)



Seejärel saate soovi korral aktiveerida biomeetrilise autentimise, et vältida peaparooli käsitsi sisestamist iga kord, kui avate oma mobiiltelefoni lukustuse.



![Image](assets/fr/26.webp)



Sisestage uuesti oma põhiparool, seejärel klõpsake nupule "Jätka".



![Image](assets/fr/27.webp)



Valige valik `Load a vault`, seejärel klõpsake `Scan QR Code` ja skaneerige kutse QR-kood, mida PearPass kuvab teie lähtemasinas (arvutis).



![Image](assets/fr/28.webp)



Teie arvutis ja mobiilis olevad võlvid on nüüd sünkroonitud. Iga ühes seadmes lisatud ID salvestatakse ja kordub turvaliselt teises seadmes.



![Image](assets/fr/29.webp)



Mobiiltelefonide puhul saate aktiveerida ka automaatse väljade täitmise. Selleks valige "Seaded > Täiendatud", seejärel klõpsake jaotises "Automaatne täitmine" nupule "Seadistada vaikimisi".



![Image](assets/fr/30.webp)



## Kuidas sünkroonida PearPassi ja brauseripikendust?



Arvuti ja nutitelefoni vahel sünkroniseeritud paroolihaldur on juba väga praktiline, kuid selle integreerimine otse brauserisse on veelgi praktilisem. Selleks alustage [ametliku PearPassi laienduse lisamisest brauserisse](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/31.webp)



Mine oma kohalikule masinale paigaldatud PearPassi tarkvarast menüüsse `Settings > Advanced`, seejärel aktiveeri valik `Activate browser extension` (Aktiveeri brauser laiendus).



![Image](assets/fr/32.webp)



PearPass genereerib token paaritusfaili. Kopeerige see.



![Image](assets/fr/33.webp)



Seejärel avage oma brauseris PearPassi laiendus, sisestage token paaritus ja vajutage nupule "Kontrollida", millele järgneb "Lõpeta".



![Image](assets/fr/34.webp)



Teie paroolihaldur on nüüd sünkroonitud brauseripikendusega.



![Image](assets/fr/35.webp)



Nüüd saate seda kasutada, et hõlpsasti oma erinevate veebikontodega ühendust luua.



![Image](assets/fr/36.webp)



Nüüd teate, kuidas kasutada PearPass paroolihaldurit. Lisaks sellele tööriistale sõltub igapäevane digitaalne turvalisus asjakohaste lahenduste õigest kasutamisest. Kui soovite õppida, kuidas luua turvaline, stabiilne ja tõhus isiklik digitaalne keskkond, kutsun teid üles avastama meie sellele teemale pühendatud koolituskursust:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1