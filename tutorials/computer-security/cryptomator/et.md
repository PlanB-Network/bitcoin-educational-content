---
name: Cryptomator
description: Krüpteerige oma faile pilves
---
![cover](assets/cover.webp)



___



*See õpetus põhineb Florian BURNELi originaalsel sisul, mis on avaldatud [IT-Connect](https://www.it-connect.fr/). Litsents [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Originaaltekstis võib olla tehtud muudatusi.*



___



## I. Esitlus



Selles õpetuses kasutame rakendust Cryptomator, et krüpteerida pilves salvestatud andmeid, olgu need siis Microsoft OneDrive'is, Google Drive'is, Dropboxis, Boxis või isegi iCloudis.



Andmete krüpteerimine, mida salvestate veebipõhistes salvestuslahendustes, nagu Drive, on parim viis oma failide ja privaatsuse kaitsmiseks. Tänu krüpteerimisele saate oma andmeid dekrüpteerida ja lugeda ainult teie, isegi kui need on salvestatud USAs või mõnes teises maailma riigis asuvas serveris.



Selles demonstratsioonis kasutatakse Windows 11 22H2 masinat koos OneDrive'iga, kuid protseduur on identne ka teiste Windowsi versioonide ja muude salvestusteenuste puhul. Kõik, mida te peate tegema, on sünkroonimiskliendi paigaldamine ja konto lisamine. See võimaldab Cryptomatoril salvestada oma andmeid hoidlasse.



![Image](assets/fr/020.webp)



Cryptomator on alternatiiv teistele rakendustele, eelkõige teises artiklis tutvustatud Picocryptile, mis näeb küll teistsugune välja, kuid on sama lihtne kasutada. Cryptomator on samuti **avatud lähtekoodiga**, RGPD-konformne ja **krüpteerib andmeid AES-256-bitise krüpteerimisalgoritmiga**. Seevastu Picocrypt tugineb kiiremale XChaCha20 algoritmile (samuti 256-bitine).



https://planb.academy/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

Cryptomatori rakendus on saadaval **Windows** (exe / msi), **Linux**, **macOS,** aga ka **Android** ja **iOS**. Muide, kõik rakendused on tasuta, välja arvatud Androidi rakendus, mille eest tuleb maksta (14,99 eurot).



Teie masinas loob **Cryptomator kausta, kuhu ta loob seifi**. Truubis, mida võib hoida OneDrive'is, Google Drive'is vms, krüpteeritakse teie andmed. Seega, kui te salvestate kõik oma andmed oma Drive'i salvestusruumis asuvasse seifi, on need kaitstud (sest need on krüpteeritud).



** Märkus**: selles artiklis kasutatakse näitena veebipõhiseid salvestusteenuseid, kuid Cryptomatorit saab kasutada andmete krüpteerimiseks kohalikul kettal, välisel kettal või isegi NAS-il. Tegelikult ei ole mingeid piiranguid.



## II. Cryptomatori paigaldamine



Alustamiseks peate **laadima** ja **installima** **Cryptomatori**. Kui allalaadimine on lõpetatud, piisab paarist klõpsust, et paigaldus lõpule viia. Nagu [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/), kasutab ka Cryptomator WinFsp'i, et **määrida virtuaalne ketas Windowsi masinasse**.





- [Lae Cryptomator alla ametlikust veebisaidist](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III. Cryptomatori kasutamine Windowsis



### A. Uue seifi loomine



Uue seifi loomiseks klõpsake nupule "**Lisata**" ja valige "**Uue seif...**". Teie olemasolevad ja teadaolevad seifid sellel masinal ilmuvad seejärel vasakule Interface. **A masinal A loodud seifi saab avada ja muuta masinal B**, kui see on varustatud Cryptomatoriga (ja krüpteerimisvõti on teada).



![Image](assets/fr/015.webp)



Alustage, andes hoidlale nime, nt "**IT-Connect**". Sellega luuakse OneDrive'is kataloog nimega "**IT-Connect**".



![Image](assets/fr/011.webp)



Järgmises etapis tuvastab Cryptomator tõenäoliselt **tuvastab teie masinas oleva "Drive "**: Google Drive, OneDrive, Dropbox jne..... Selleks, et te saaksite teenusepakkuja otse valida. Ma proovisin seda kahes erinevas Windows 11 masinas, kus oli mitu Drive'i ja seda ei tuvastatud. See ei ole probleem, määrake lihtsalt "**Custom location**" ja valige oma salvestusruumi juurest. Näiteks: **C:\Users\<Username>\OneDrive**.



![Image](assets/fr/018.webp)



Järgnevalt saate reguleerida valikut ekspertide seadete all.



![Image](assets/fr/021.webp)



Järgmisena tuleb määrata **krüpteerimisvõtmele vastav parool**. See parool võimaldab teil **avada Cryptomatori seifi** ja pääseda ligi selle andmetele. **Kui te selle kaotate, kaotate juurdepääsu oma andmetele**. Lõpuks on teil veel võimalus **luua varukoopia võti**, märgistades valiku "**Ja, parem kindel kui kahju**", mis on sarnane [BitLockeri] taastamisvõtmega (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). See on soovitatav, kuid ärge salvestage seda varukoopia võtit oma OneDrive'i juurest!



Klõpsake nuppu "**Loo seif**".



![Image](assets/fr/019.webp)



Kopeerige taastamisvõti ja salvestage see oma lemmik paroolihaldurisse. Klõpsake nuppu "**Järgmine**".



![Image](assets/fr/013.webp)



See ongi kõik, teie uus pagasiruumi on loodud ja valmis kasutamiseks!



![Image](assets/fr/014.webp)



### B. Juurdepääsunäitajad



Selleks, et pääseda ligi seifile ja selle andmetele, kas **lugeda olemasolevaid andmeid või lisada uusi andmeid**, tuleb see **avada**. Cryptomator loetleb teadaolevad seifid: IT-Connecti seif ilmub, seega valige see lihtsalt välja ja klõpsake "**Unlock**".



![Image](assets/fr/016.webp)



Seifi avamiseks peate sisestama oma salasõna. Seejärel klõpsake nuppu "**Vabastage ketas**".



![Image](assets/fr/022.webp)



**Sinu seif on Windowsi masinasse paigaldatud virtuaalse kettana.** See ketas, mis siinkohal pärib E-tähte, annab sulle ligipääsu oma andmetele (lihtsas tekstis, sest seif on lukustamata).



![Image](assets/fr/017.webp)



OneDrive'i poolel ei saa me Cryptomatori võlvkappi otse sirvida. Me ei näe andmeid (ei failide nimesid ega sisu). See tähendab, et te ei pea Cryptomatori võlvile andmeid lisama tavapärase OneDrive'i otsetee kaudu. **Te peate oma andmed lisama, kasutades Cryptomatori virtuaalset draivi.**



![Image](assets/fr/012.webp)



### C. Trunki valikud



Seifi seaded on kättesaadavad nupu "**Krüpteeritud mahu valikud**" kaudu (kui see on lukustatud) ja võimaldab automaatset lukustamist tegevusetuse korral, nagu te saate teha oma parooliga seifi puhul. Valik "**Unlock encrypted volume on startup**", nagu nimigi ütleb, avab ketta lukustuse ilma teiepoolse sekkumiseta ja monteerib virtuaalse draivi. Turvalisuse huvides on parem vältida selle valiku aktiveerimist.



Vahekaardil "**Mounting**" saate ka otsustada, kas see monteeritakse ainult lugemiseks või määrata konkreetne kiri.



![Image](assets/fr/024.webp)



Lisaks saate Cryptomatori seadetes **lülitada rakenduse automaatse käivitamise**.



## IV. Kokkuvõte



**Cryptomatoriga** saate **luua mõne minutiga krüpteeritud seifi**, et kaitsta andmeid, mida soovite salvestada OneDrive'is ja konsoolides. Seda on väga lihtne kasutada, kui tegemist on selle "sidumisega" Drive'iga: sel eesmärgil on see minu eelistus Picocrypt'ile.