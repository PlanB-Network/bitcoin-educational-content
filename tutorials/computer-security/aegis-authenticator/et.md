---
name: Aegis Authenticator
description: Kuidas saate kasutada Aegis Authenticatorit oma kontode kaitsmiseks kahekordse autentimisega?
---

![cover](assets/cover.webp)



Tänapäeval on kahefaktoriline autentimine (2FA) veebikontode kaitsmiseks hädavajalik. Lisaks paroolile lisatakse teine tegur (sageli 6-kohaline kood), mis aegub 30 sekundi pärast, mis teeb selle häkkerite jaoks oluliselt keerulisemaks. Spetsiaalse TOTP-rakenduse (*Time-based One-Time Password*) kasutamine on turvalisem kui SMS, mida on võimalik kaaperdada SIM-kaardi vahetamise rünnakute abil.



Siiski ei ole kõik autentimisrakendused võrdsed. Paljude patenteeritud lahenduste (Google Authenticator, Authy jne) puhul on probleeme: need on patenteeritud ja suletud lähtekoodiga (nende turvalisust on võimatu kontrollida), mõnikord on neisse integreeritud reklaami jälgijad, nad ei paku teie koodide krüpteeritud varukoopiaid ja võivad isegi takistada teie kontode eksportimist, et lukustada teid nende ökosüsteemi.



Aegis Authenticator seevastu esitab end tasuta ja eetilise alternatiivina nendele rakendustele. Aegis on tasuta, turvaline ja avatud lähtekoodiga rakendus, millega saab hallata oma kaheastmelise verifitseerimise märgiseid Androidis. Selle arendus keskendub olulistele funktsioonidele, mida teised rakendused ei paku, sealhulgas kohalike andmete tugevale krüpteerimisele ja turvalise varukoopia tegemise võimalusele. Kokkuvõttes pakub Aegis lokaalset, kontrollitavat kahetasandilise autentimise lahendust, mis on ideaalne kõigile, kes soovivad säilitada täieliku kontrolli oma 2FA-koodide üle.



## Aegis Authenticator'i tutvustamine



Aegis Authenticator on avatud lähtekoodiga 2FA rakendus Androidile, mis on avaldatud GPL v3 litsentsi alusel. See paistab silma oma "Privacy by Design" filosoofia poolest: rakendus töötab täielikult võrguühenduseta ja ei vaja ühendust kaugteenusega. Selle tulemusel jäävad teie märgised teie seadmesse, turvalisse turvakappi, mille võti on ainult teil.



### Põhijooned



**Krüpteeritud hoidla:** kõik teie OTP-koodid on salvestatud AES-256 krüpteeritud hoidlasse (GCM-režiim), mis on kaitstud kasutaja määratud peaparooliga. Selle võlvkambri saab avada parooli või biomeetriliste andmete (sõrmejälg, näotuvastus) abil, mis lisab mugavust. Parooli puudumisel oleksid andmed krüpteerimata - seega soovitame tungivalt, et määraksite parooli.



**Täiustatud organiseerimine:** Aegis hoiab teie paljud 2FA-kontod hästi organiseeritud. Saate oma kirjeid sorteerida tähestikuliselt või enda valitud järjekorras, rühmitada neid kategooriate kaupa (nt Isiklik, Töö, Sotsiaalne), et neid oleks lihtne leida, ja määrata igale kirjele isikliku ikooni. Lisatud on otsinguriba, mille abil saate teenuse või konto nime järgi kohe üles leida.



**Krüpteeritud kohalikud varukoopiad:** Selleks, et te ei kaotaks kunagi juurdepääsu oma kontodele, pakub Aegis automaatseid varukoopiaid oma seifist. Need on krüpteeritud (parooliga) ja neid saab salvestada teie valitud kohta (sisemine salvestusruum, pilvekaust jne). Rakendus saab oma kontode andmebaasi eksportida ka käsitsi, vastavalt vajadusele krüpteeritud või krüpteerimata kujul. Kontode importimine teistest 2FA-rakendustest on sama lihtne (Aegis toetab importi Authy, Google Authenticator, FreeOTP, andOTP jne).



**Turvalisus ja privaatsus:** rakendus on vaikimisi täielikult võrguühenduseta. See ei nõua mingeid võrgulubasid - mis tähendab, et see ei edasta andmeid välismaailma ja ei sisalda reklaami jälgimisseadmeid ega käitumisanalüüsi mooduleid. Aegis ei näita reklaame ega nõua kasutajakontot: niipea kui see on paigaldatud, on see ilma registreerimiseta käivitatud. Kuna selle lähtekood on GitHubis avalik, saab kogukond seda vabalt auditeerida, mis tagab pahatahtlike või varjatud funktsioonide puudumise.



**Modern Interface:** Aegis võtab kasutusele korraliku materjalidisaini, mis toetab tumedat teemat (sealhulgas AMOLED-režiimi) ja isegi valikulist plaatide vaadet, et kuvada oma koodid ruudustikuna. Interface on lihtsakoeline, ilma igasuguste iludusteta ja takistab turvameetmena koodide pildistamist ekraanil.



## Paigaldamine



Kuna Aegis Authenticator on avatud lähtekoodiga, eelistavad selle arendajad privaatsussõbralikke levituskanaleid. Selle paigaldamiseks on kaks peamist võimalust:



### Via F-Droid (soovitatav)



Kõige turvalisem ja lihtsam viis on tasuta alternatiivse poe F-Droid kaudu. Kui F-Droid ei ole veel teie telefonile paigaldatud, alustage selle allalaadimisega ametlikust veebisaidist [F-Droid.org](https://f-droid.org). Seejärel :





- Avage F-Droid ja veenduge, et olete uuendanud oma repositooriume, et saada uusim nimekiri rakendustest
- Otsige F-Droidist "Aegis Authenticator". Ametlik rakendus peaks ilmuma (väljaandja: Beem Development)
- Alustage paigaldamist, vajutades nuppu Install. Kuna Aegis on üks F-Droidi poolt kontrollitud rakendustest, saate kasu usaldusväärsest ja turvalisest allalaadimisest



F-Droidi kaudu paigaldamise eeliseks on automaatsete rakendusuuenduste saamine kohe, kui need ilmuvad. Lisaks sellele tagab F-Droid, et rakendus ei sisalda soovimatuid patenteeritud komponente.



### Via GitHub (allkirjastatud APK)



Kui soovite rakenduse installida ilma poe kaudu minemata, saate ametliku APK otse projekti GitHubi lehelt alla laadida. Aegise repositooriumis ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)) minge jaotisse Releases, kus on avaldatud stabiilsed versioonid.





- Lae alla uusim APK versioon
- Enne APK installimist veenduge, et olete oma seadmes lubanud tundmatutest allikatest pärinevate rakenduste paigaldamise (Androidi seadetes)
- GitHubis esitatud APK on allkirjastatud arendaja poolt sama võtmega nagu F-Droidil



Pärast käsitsi paigaldamist toimib rakendus samamoodi. Pange tähele, et uuendused ei ole automaatsed: peate GitHubist regulaarselt uusi versioone otsima.



### Google Play Store vs F-Droid



Aegis Authenticator on saadaval nii Google Play poes kui ka F-Droidis, mis annab teile võimaluse valida paigaldusmeetod:



**Google Play Store:**




- ✅ Androidi süsteemi integreeritud automaatsed uuendused
- ✅ Lihtne, tuttavlik paigaldus
- ✅ Sama allkirjastatud APK nagu teistes kanalites



**F-Droid (soovitatav) :**




- ✅ Tasuta ja avatud lähtekoodiga kauplus
- ✅ Reprodutseeritav ja kontrollitav konstruktsioon
- ✅ Google'i teenust ei ole vaja
- ✅ Austus vaba tarkvara filosoofia vastu



Valik nende kahe võimaluse vahel sõltub teie eelistustest Google'i ökosüsteemi suhtes. Kui eelistate lihtsust, on Play Store ideaalne. Kui soovite privaatsussõbralikumat, Google'i teenustest sõltumatut lähenemist, on F-Droid parem valik.



## Esimene konfiguratsioon



Aegise esmakordsel käivitamisel tehakse ettepanek esialgse konfiguratsiooni protseduuriks, et tagada teie 2FA-koodi turvalisus:



![Configuration initiale Aegis](assets/fr/01.webp)



*Aegise algne konfigureerimisprotsess: tervitusekraan, turvavalikud, põhiparooli määramine ja lõpetamine*



### Määrake põhiparool



Aegis palub teil kõigepealt valida põhiparool. Seda salasõna kasutatakse kõigi teie võlvikusse salvestatud autentimistunnuste krüpteerimiseks. Soovitame tungivalt määrata tugeva ja ainulaadse parooli, mida ainult teie teate.



**⚠️ Hoiatus:** ärge unustage seda parooli - kui kaotate selle, muutuvad teie krüpteeritud 2FA-koodid kättesaamatuks (tagauks puudub). Aegis palub teil parooli kinnitamiseks kaks korda sisestada.



### Biomeetrilise avamise lubamine (valikuline)



Kui teie Android-seade on varustatud sõrmejäljelugeja või muu biomeetrilise anduriga, palub Aegis teil aktiveerida biomeetriline avamine. See valik on valikuline, kuid väga praktiline: see võimaldab teil rakenduse kiiresti avada sõrmejälje või näo abil, selle asemel, et iga kord parooli sisestada.



Pange tähele, et biomeetria on lisamugavus: teie põhiparool on endiselt vajalik, kui biomeetriaid muudetakse või seade taaskäivitatakse.



### Avasta rakenduse seaded



Kui olete rakenduses sees (peamine Interface on esialgu tühi), tutvuge olemasolevate konfiguratsioonivõimalustega. Juurdepääs seadistustele toimub ekraani paremas ülaosas asuva rippmenüü kaudu (kolm vertikaalset punkti), seejärel valige "Settings" (Seaded).



![Interface principale et paramètres](assets/fr/02.webp)



*Interface peamine Aegis tühi käivitamisel, juurdepääs parameetrite menüüle ja ülevaade olemasolevatest valikutest*



Aegise seadete menüü koondab mitu olulist jaotist:





- **Välimus**: Kohandage teemat (hele, tume, AMOLED), keelt ja muid visuaalseid seadeid
- **Käitumine**: Konfigureerige rakenduse käitumist kirjete loeteluga suhtlemisel
- **Ikoonipaketid**: hallata ja importida ikoonipakette, et kohandada oma kontode välimust ja tunnetust
- **Turvalisus**: Krüpteerimise, biomeetrilise avamise, automaatse lukustuse ja muude turvaparameetrite seaded
- **Varukoopiad**: Konfigureerige automaatsed varukoopiad teie valitud asukohta
- **Import ja eksport**: Importida varukoopiaid teistest autentimisrakendustest ja eksportida käsitsi oma Aegis Vault
- **Auditilogi**: Üksikasjalik logi kõigi oluliste sündmuste kohta rakenduses



See selge korraldus võimaldab teil konfigureerida Aegis vastavalt oma eelistustele ja turvavajadustele.



## 2FA konto lisamine



Kui Aegis on konfigureeritud, liigume edasi oluliste küsimuste juurde: kahefaktoriliste kontode lisamine. Protsess on lihtne ja Aegis pakub mitmeid meetodeid autentimiskoodide integreerimiseks.



### Kolm olemasolevat lisamismeetodit



Vajutage Aegis Interface põhisüsteemis paremal allosas olevale nupule **+**, et pääseda juurde lisamisvalikutele. Teil on kolm võimalust:





- **Skaneeri QR-kood**: Skaneeri otse veebiteenuse poolt kuvatud QR-koodi
- **Skaneeri pilt**: Skaneerige QR-koodi seadmesse salvestatud pildilt
- **Sisestage käsitsi**: Sisestage 2FA konto andmed käsitsi



### Praktiline näide: Bitwardeni konfigureerimine



Võtame protsessi illustreerimiseks konkreetse näite 2FA aktiveerimisest Bitwardenis:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Näide 2FA aktiveerimisest Bitwardenis: Interface web koos autentimisvõimalustega ja Aegise soovitus*





- **Sisselogimine ja juurdepääs seadetele**: Logige sisse oma Bitwardeni kontole ja sisenege seadetele, vahekaardile "Turvalisus"
- **Teenuseosutajad**: Mine jaotisse "Providers" ja klõpsa "Manage" jaotises "Authenticator app"



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Täielik konto lisamise protsess: QR-kood, mida teenus kuvab, salajane võti nähtav ja kinnituskood sisestatud*





- **Skaneeri QR-kood**: Avaneb hüpikaken QR-koodi ja salajase võtmega
- **Aegis**: Kasutage "Skaneeri QR-koodi", et automaatselt teavet koguda
- **Kontrollimine**: Sisestage Aegise poolt genereeritud 6-kohaline kood väljale "Verifitseerimiskood"
- **Aktiveerimine**: Aktiveerimise lõpuleviimiseks klõpsake nuppu "Aktiveeri"



### Lisage andmed käsitsi



Kui te eelistate või ei saa QR-koodi skaneerida, kasutage valikut "Sisesta käsitsi". Vorm võimaldab sisestada :



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Uue 2FA-konto lisamise protsess: tühi Interface, valikute lisamine, käsitsi sisestamise vorm ja konto edukalt lisatud*





- **Nimi**: Teenuse nimi (nt Bitwarden, GitHub...)
- **Emitent**: Emitent (sageli identne nimega)
- **Rühm**: Valikuline, et korraldada oma kontosid kategooriate kaupa
- **Märkus**: Isiklikud märkused selle konto kohta
- **Saladus**: Teenuse esitatud salajane võti (vaikimisi maskeeritud)
- **Edasijõudnud**: Täiustatud parameetrid (algoritm, periood, numbrite arv)



Kui konto on lisatud, kuvatakse see teie nimekirjas koos praeguse koodiga ja ajaindikaatoriga, mis näitab uuendamiseni jäänud aega.



### Universaalne ühilduvus



Aegis ühildub kõigi TOTP- ja HOTP-standardeid kasutavate teenustega, sealhulgas praktiliselt kõigi 2FA-d pakkuvate saitidega: sotsiaalvõrgustikud, pangad, paroolihaldurid, krüptoplatvormid jne.



### Sissepääsu korraldus



Kui olete lisanud mitu kontot, hakkate hindama Aegise organiseerimisvahendeid:





- **Kohandatud sorteerimine:** Vaikimisi on kontod loetletud tähestikulises järjekorras, kuid te saate järjekorda käsitsi muuta
- **Rühmad ja kategooriad:** Looge rühmad, et eristada oma isiklikke kontosid ärikontodest, või grupeerige neid teenuse tüübi järgi (pangandus, e-post, suhtlusvõrgustikud jne)
- **Kohandatud ikoonid:** Aegis püüab automaatselt määrata sobiva ikooni, kui see on saadaval, vastasel juhul saate valida paljude üldiste ikoonide vahel või importida pildi
- **Kiirotsing:** Otsinguriba ülaosas võimaldab teil sisestada paar tähte, et filtreerida koheselt sobivad kirjed välja



Kui puudutate sisestust, kuvatakse OTP-kood täissuuruses (kui see oli peidetud) ja saate selle pika vajutusega lõikelauale kopeerida - see on mugav, kui soovite seda ühendatavasse rakendusse kleepida.



## Turvalisus ja varukoopiad



Kuna turvalisus on Aegise keskmes, on oluline mõista, kuidas teie 2FA-koodid on kaitstud ja kuidas tagada nende püsimine probleemide korral.



### Turvalisuse arhitektuur



**Robust krüpteerimine**: Kõik teie koodid salvestatakse krüpteeritud seifis, kasutades **AES-256 algoritmi GCM-režiimis**, kombineerituna teie põhiparooliga. Võtme tuletamine põhineb **scryptil**, mis pakub täiustatud kaitset brute-force rünnakute vastu.



**Turvaline avamine** : Andmete dekrüpteerimiseks on vaja peaparooli. Biomeetria (valikuline) kasutab krüpteerimisvõtme kaitsmiseks **Android Secure Keystore** ja TEE (Trusted Execution Environment).



**Miinimumload**: Aegis töötab vaikimisi võrguühenduseta, nõudes juurdepääsu ainult kaamerale (QR-skaneerimine), biomeetriale ja vibraatorile. Andmeid ei koguta ega jagata.



### Varundamise võimalused



Aegis pakub mitmeid varundusstrateegiaid, mis vastavad erinevatele turva- ja mugavusvajadustele:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface koos lisatud konto, varundushoiatuse, automaatsete varundusseadete ja varundusstrateegiatega*



**1. Automaatne kohalik varundamine**




- Konfigureerige valitud sihtkaust
- Kohandatav sagedus (pärast iga muudatust, iga päev jne)
- Salasõnaga kaitstud krüpteeritud failid (.aesvault)
- Ühildub sünkroonitud kaustadega (Nextcloud, Dropbox jne)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Varukoopia kausta valimise protsess: failiotsinguprogramm, sihtkaust ja juurdepääsuluba*



**2. Androidi** pilve varukoopiad




- Vabatahtlik integratsioon Android varundussüsteemiga
- Saadaval ainult krüpteeritud seifide puhul (turvalisus säilinud)
- Läbipaistev varundamine koos teiste Androidi andmetega
- Automaatne taastamine seadme vahetamisel



**3. Käsitsi** eksport




- Eksportige soovi korral **Settings > Import & Export** kaudu
- Valida krüpteeritud (soovitatav) või selge vorming
- Kasulik migratsioonide või aeg-ajalt tehtavate varukoopiate jaoks



### Head ohutustavad





- Hoidke mitu varukoopiat, et vältida kahjustusi
- Testige regulaarselt **oma varukoopiaid**, tehes taastamiskatseid
- Säilitage oma teenuse osutamise koodid **eraldi**
- Teie **põhiparool** on endiselt vajalik ka pilvekaardistamise puhul
- **Turvaline põhiparool**: kasutage unikaalset, tugevat parooli, mis on salvestatud paroolihaldurisse
- Hoidke oma rakendus **ajakohasena** koos viimaste turvaparandustega
- Aktiveerige seadetes **automaatne lukustus**, et tagada juurdepääs rakendusele
- Lülita **ekraanipildid** välja (vaikimisi valik), et sinu koode ei saaks pealtkuulata
- **Kasutage biomeetriaid säästlikult**: eelistage paroole kriitiliste juurdepääsude puhul



## Võrdlus teiste rakendustega



Kuidas on Aegis võrreldav teiste populaarsete autentimisrakendustega?



### Aegis vs Google Authenticator



**Aegis :**




- ✅ Avatud lähtekoodiga ja auditeeritav
- ✅ Kohalik krüpteeritud varundamine
- ✅ Täiustatud korraldus (rühmad, ikoonid, otsing)
- ✅ Andmete kogumine puudub
- ❌ Ainult Android



**Google Authenticator :**




- ✅ Saadaval Androidis ja iOSis
- ✅ Pilves sünkroniseerimine (alates 2023. aastast)
- ❌ Suletud lähtekood
- ❌ Piiratud funktsionaalsus
- ❌ Potentsiaalne Google'i andmete kogumine



### Aegis vs Authy



**Aegis :**




- ✅ Avatud lähtekood
- ✅ Kontot ei ole vaja
- ✅ Võimalik koodieksport
- ✅ Andmete kontrollimine kokku
- ❌ Mitme seadme sünkroonimine puudub



**Authy :**




- ✅ Mitme seadme sünkroniseerimine
- ✅ Saadaval Androidis ja iOSis
- ❌ Suletud lähtekood
- ❌ Nõuab telefoninumbrit
- ❌ Koodide eksportimine ei ole võimalik
- ❌ Töölauarakendused eemaldatakse märtsis 2024



Aegis sobib suurepäraselt Androidi kasutajatele, kes hindavad läbipaistvust, kohalikku turvalisust ja täielikku kontrolli oma andmete üle. Alternatiivid, nagu Authy, sobivad paremini, kui teil on tingimata vaja automaatset mitme seadme sünkroniseerimist.




## Kokkuvõte



Aegis Authenticator on suurepärane lahendus neile, kes otsivad privaatsussõbralikku, turvalist ja läbipaistvat 2FA rakendust. Selle avatud lähtekoodiga lähenemisviis koos tugeva krüpteerimise ja korraliku Interface-ga teeb sellest esmaklassilise valiku teie võrgukontode kaitsmiseks.



Kuigi Aegis on piiratud Androidiga ja tal puudub natiivne pilvesünkroniseerimine, kompenseerib ta need piirangud oma "Privacy by Design" filosoofia ja täieliku andmekontrolli abil. Kasutajatele, kes on mures oma digitaalse privaatsuse pärast, pakub Aegis usaldusväärset ja võimsat alternatiivi turul valitsevatele patenteeritud lahendustele.



Teie võrgukontode turvalisus ei pea sõltuma kaubandusettevõtete heast tahtest. Aegise abil saate oma autentimiskoodid hoida kontrolli all digitaalses seifis, mille võti on ainult teie käes.



## Ressursid



### Ametlikud veebisaidid




- **Ametlik veebileht**: [getaegis.app](https://getaegis.app/) - Taotluse esitlus ja allalaadimine
- **Allikakood**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Ametlik GitHub repository
- **F-Droid**: [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Installeerimine tasuta poe kaudu



### Tehniline dokumentatsioon




- **Vault dokumentatsioon**: [Vault design](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Krüpteerimise ja turvalise arhitektuuri tehniline kirjeldus
- **Ametlik KKK**: [getaegis.app/#faq](https://getaegis.app/#faq) - Vastused korduma kippuvatele küsimustele
- **Projekti wiki**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Täielik kasutajate dokumentatsioon