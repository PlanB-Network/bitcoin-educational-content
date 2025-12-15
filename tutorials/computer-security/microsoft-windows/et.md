---
name: Windows 11
description: Microsoft Windows 11 automaatne paigaldamine konfiguratsioonifaili kaudu
---
![cover](assets/cover.webp)


Selles õpetuses õpime, kuidas paigaldada Windows 11 automaatselt, kasutades teistsugust meetodit kui Windowsi standardne paigaldusprotsess.


## Lae alla!


Esimene asi, mida vajate, on paigaldusfail. Kõige ohutum ja usaldusväärsem koht selle allalaadimiseks on otse Microsofti ametlikust veebisaidist.


Lihtsalt külastage allpool toodud linki ja järgige juhiseid [Windows 11 ISO-faili](https://www.microsoft.com/en-us/software-download/windows11) allalaadimiseks


![Image](assets/en/02.webp)


Kui olete allalaadimislehele jõudnud, kerige alla ISO-faili allalaadimise sektsiooni.


![Image](assets/en/01.webp)


َ Ja valige sobiv versioon.


![Image](assets/en/03.webp)


Pärast Windows 11 valimist klõpsake nupule Kinnita.


Selles etapis võib taotluse töötlemine võtta paar sekundit ja seejärel kuvatakse järgmine lehekülg:


![Image](assets/en/04.webp)


Pärast taotluse kinnitamist peate valima oma eelistatud keele.


![Image](assets/en/05.webp)


Pärast keele valimist ja kinnitamise nupule klõpsamist töödeldakse taotlust. See etapp võib võtta paar sekundit.


Kui taotlus on edukalt töödeldud, ilmub lehekülg .iso faili allalaadimislingiga. Vajutage 64-bitise allalaadimise nupule, et alustada allalaadimist.


Faili suurus on umbes 5,5 GB ja loodud link kehtib 24 tundi.


## Automatiseerimine!


Selles etapis peame tegema muudatusi Windowsi standardpaigalduses. Selles etapis, kasutades Unattended install'i, määrame, millised elemendid paigaldatakse, ilma et kasutaja tagantjärele sekkuks. Tegelikult kasutatakse selle meetodi puhul XML-faili, et konfigureerida Windowsi installeerimise sammud ja installeeritavad teenused. Teisisõnu, Unattended.xml faili kasutamine loob paigaldamise ajal automatiseerimisprotsessi, vältides vajadust valida mitmeid valikuid ja vältides tüütuid samme, mida tavaliselt paigaldamise ajal nõutakse. See meetod on ebatavaline, kuid standardne meetod, mille Microsoft on kasutusele võtnud. Lisateave on saadaval [Microsofti ametlikul veebilehel](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11).


Internetis on saadaval mitmesuguseid vahendeid järelevalveta failide genereerimiseks. Mõned neist on veebipõhised, teised aga võrguvälised. Üks veebipõhine vahend selle faili loomiseks on [see veebisait](https://schneegans.de/windows/unattend-generator). Pärast selle avamist kuvatakse meile järgmine lehekülg:


![Image](assets/en/06.webp)


Nagu lehe ülaosas mainitud, saab seda meetodit kasutada Windows 10 ja 11 installimiseks. Esimeses etapis valime Windowsi keele. Kui meil on vaja lisada Windows'i kuvamis- ja klaviatuurikeelte loetellu teine või isegi kolmas keel, siis võime kasutada allolevat kasti:


![Image](assets/en/07.webp)


Järgmises etapis valime soovitud asukoha.


![Image](assets/en/08.webp)


Selles etapis saame määrata ka arvuti protsessorarhitektuuri. Selles etapis saame:

1. Otsustage, kas ignoreerida Windowsi turvaelemente, nagu TPM ja Secure Boot. Secure Boot funktsioon tagab, et kui Windowsi tuumikfaile muudetakse bootimise ajal, avastatakse see probleem ja nende täitmine takistatakse. See funktsioon aitab ka kaitsta süsteemi Windowsi pahatahtlike värskenduste paigaldamise eest. Nende funktsioonide ümbersõidu võimaluse sisselülitamine on mõnikord teatavate arvutite puhul, eriti vanemate mudelite puhul, vältimatu. Üldiselt on siiski soovitatav sellised funktsioonid nagu Secure Boot sisse lülitatud hoida.

2. Ignoreerige internetiühenduse nõuet protsessi lõpuleviimiseks. See on kasulik olukordades, kus traadiga LAN-ühendus ei ole kättesaadav, sest enamasti ei tuvastata Windows'i paigaldamise ajal veel traadita kaarti ja vajalik on internetiühendus kaabli kaudu. Selle valiku aktiveerimine lahendab selle sammuga seotud probleemid.


Järgmise sammuna saame valida arvutile nime.


![Image](assets/en/09.webp)


Samuti võime lubada Windowsil valida süsteemile nime. Selles etapis saame valida Windowsi tüübi, kas pakitud või pakkimata, või lasta Windowsil määrata sobiv versioon arvuti spetsifikatsioonide põhjal. Selles etapis saab määrata ka ajavööndi.


Järgmine samm hõlmab partitsiooni seadistusi:


![Image](assets/en/10.webp)


Selles etapis saame määrata Windows'i paigaldamiseks vajaliku partitsiooni tüübi ning Windows Recovery Environment'i paigaldamiseks vajalikud seaded. Valides esimese võimaluse, lükatakse partitsiooni valik ja partitsioneerimine edasi Windows'i paigaldamise ajaks ja seadistamise ajal küsitakse neid küsimusi nagu tavalise paigaldusmeetodi puhul.


Selles etapis valime Windowsi versiooni, mida paigaldada:


![Image](assets/en/11.webp)


Kui tootevõti on olemas, saab selle samuti selles etapis sisestada.


Järgmine samm hõlmab Windowsi sisselogimiskonto konfigureerimist:


![Image](assets/en/12.webp)


## Kontoseisukohad


Selles etapis:


1. Saame määrata admin-konto nime ja parooli. Samuti on võimalik luua mitu kasutaja- või administraatorikontot.

2. Siin määrame, millisele kontole tuleb pärast Windowsi paigaldamist esimest korda sisse logida. Selle jaotise erinevad valikud on näidatud pildil.

3. Kui te ei soovi, et ühtegi kontot ei loodaks, puhastage kõik kontod ja valige see valik. Sellisel juhul logid Sa pärast Windowsi installeerimist automaatselt Windowsi administraatori kontole.


Järgmise sammuna tuleb konfigureerida parooli ja hostifaili seaded:


![Image](assets/en/13.webp)


Selles etapis määratakse kindlaks, kas paroolidel peaks olema kehtivusaeg. Lisaks sisaldab see lõik ebaõnnestunud sisselogimiskatsetega seotud turvasätteid, mida saab vastavalt vajadusele lubada või keelata.


Selle jaotise allosas on failide kuvamise seaded. Ükski neist valikutest ei ole Windowsi standardse installeerimise ajal saadaval ja need tuleb konfigureerida pärast installeerimist. Seevastu järelevalveta paigaldamise meetodi puhul on need seaded kergesti kättesaadavad.


Järgmine samm hõlmab Windowsi turvasätete konfigureerimist:


![Image](assets/en/14.webp)


## Turvasätted


Selles etapis:


1. Windows Defenderi saab sisse või välja lülitada. See funktsioon toimib nagu Windowsi turvatarkvara ja aitab vältida pahatahtlike failide täitmist, teatud võrgurünnakuid ja muud.

2. Windowsi automaatsed uuendused saab välja lülitada. See on üks levinud probleem, millega Windowsi kasutajad silmitsi seisavad!

3. See jaotis võimaldab UAC (User Account Control) sisse- või väljalülitamist. See funktsioon takistab kahtlaste rakenduste käivitamist kõrgendatud lugemis- ja kirjutamisõigustega.

4. Seda funktsiooni kasutab Windows potentsiaalselt kahjuliku tarkvara tuvastamiseks.

5. Lubage või keelake Windows'i rakenduste, näiteks PowerShelli ja teiste rakenduste pikkade teekondade tugi või lülitage see välja.

6. Lubage või keelake kaugtöölaua kasutamine süsteemile eemalt juurdepääsuks.


Sõltuvalt kasutatavast Windowsi versioonist võivad mõned neist funktsioonidest olla toetatud või mitte.


Järgmine samm hõlmab ikoonide konfigureerimist:


![Image](assets/en/15.webp)


Selles jaotises:


1. Loetletud on töölaua ikoonid, mida saab vastavalt vajadusele lisada või eemaldada.

2. Loetletud on stardimenüü ikoonid, mida saab vastavalt vajadusele lisada või eemaldada.

3. See jaotis võimaldab konfigureerida, kas virtualiseerimisega seotud tööriistad on paigaldatud või mitte. See valik on spetsiifiline Windows 11 jaoks ja ei kehti Windows 10 puhul.


Järgmine samm hõlmab Wi-Fi seadete konfigureerimist:


![Image](assets/en/16.webp)


Selles jaotises saab konfigureerida Wi-Fi-võrgu seadeid. Nagu eespool mainitud, ei tuvastata enamasti Windowsi installimise ajal Wi-Fi kaarti, nii et ühendamine seadistamise ajal ei ole tavaliselt võimalik. Selle sektsiooni konfigureerimisel saab süsteem aga traadita kaardi tuvastamise korral internetti ühenduda.


Järgmine samm hõlmab olulist seadistust:


![Image](assets/en/17.webp)


Selles jaotises täpsustame, kas süsteemiprobleemide teave tuleb Microsoftile saata või mitte.


Järgmine samm hõlmab vaikimisi rakenduste konfigureerimist:


![Image](assets/en/18.webp)


## Tarkvara vaikimisi lubamine/väljalülitamine


Selles jaotises saame valida kõik rakendused, mida me ei soovi vaikimisi paigaldada. Näiteks saame valida, et Cortana või Copilot ei paigaldataks.


Järgmine samm hõlmab rakenduse täitmisega seotud turvasätteid:


![Image](assets/en/19.webp)


WDAC-sätete kohaldamisega saab teatavate rakenduste käivitamist takistada.


Lõpuks, pärast soovitud seadete rakendamist, saab loodud XML-faili alla laadida:


![Image](assets/en/20.webp)


Vajutades nupule Download XML File, laaditakse alla fail autounattend.xml. Selle faili kasutamiseks lihtsalt ühendage alla laetud ISO USB-kettale, paigutage autounattend.xml fail juurkataloogi ja jätkake seejärel Windowsi installimist.


Üks käivitatava USB-ketta loomiseks saadaval olevatest tööriistadest on Rufus. Rufus saab teha käivitatava Windowsi installeerimise mälupulga, kasutades antud Windowsi installeerimise ISO-faili. See on kiire ja lihtne, selle saab alla laadida [siit](https://rufus.ie/en/#download)


![Image](assets/en/21.webp)


Selles tarkvaras vajutame pärast soovitud USB-ketta ja sobiva ISO-faili valimist nupule Start.


![Image](assets/en/22.webp)


Selles etapis lülitame kõik valikud välja, kuna nende sisselülitamine võib tekitada konflikte genereeritud Unattend-faili kasutamisel. Pärast failide kopeerimist USB-kettale paigutame faili autounattend.xml juurkataloogi:


![Image](assets/en/23.webp)


Siinkohal on USB-ketas valmis Windows'i automaatseks paigaldamiseks ja paigaldamist saab alustada selle ketta abil.


## ISO redigeerimine


Kui teil on vaja installida Windows virtuaalmasinasse, saate kasutada tarkvara ISO-failide loomiseks ja muutmiseks. Üks selline tarkvara on AnyBurn. Pärast Microsofti veebilehelt alla laaditud ISO-faili sisu ekstraheerimist asetage fail autounattend.xml juurkataloogi. Seejärel looge AnyBurni abil uus ISO-faili uuendatud sisuga.


AnyBurn on multifunktsionaalne tarkvara ISO-failidega töötamiseks. See pakub erinevaid funktsioone ISO-failide töötlemiseks, millest üks on käivitatavate ISO-kujutiste loomine; [siin](https://www.anyburn.com/download.php) on originaalveebisait.


Valige tarkvara pealehel "Create Image from File/Folder" (Pildi loomine failist/kaustast):


![Image](assets/en/24.webp)


Järgmisel lehel valige kõik ISO-st ekstraheeritud failid koos autounattend.xml-failiga.


![Image](assets/en/25.webp)


Selles etapis konfigureerime seaded, et ISO-faili saaks käivitada:


![Image](assets/en/26.webp)


Selles etapis tuleb määrata tee faili bootfix.bin juurde, et ISO oleks käivitatav. See fail asub ISO faili juurest, bootkausta sees. Samuti on soovitatav lubada nii ISO9660 kui ka UDF valikud Properties sektsioonis.


![Image](assets/en/27.webp)


Pärast seda sammu, klõpsates nupule Next, luuakse ISO-fail. Seda faili saab kasutada virtualiseerimistarkvaras, näiteks Oracle VirtualBox. Allpool leiate VirtualBox kohta õpetuse:


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65