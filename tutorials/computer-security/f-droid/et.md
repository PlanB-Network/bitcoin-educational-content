---
name: F-Cold
description: Vaba ja avatud lähtekoodiga rakenduste kataloog.
---

![cover](assets/cover.webp)



Digitaalajastul töötavad suured korporatsioonid ja institutsioonid selle nimel, et muuta internet tsentraliseeritumaks, andes selle kontrolli enda kätte ja takistades seeläbi kõigi kasutajate eraelu puutumatust ja vabadust. See ei ole utoopia, see toimub juba praegu. Bitcoinerina on detsentraliseerimine, eraelu puutumatuse ja individuaalsete vabaduste austamine põhimõtted, mida te kalliks peate, eriti tööriistade puhul, mida te igapäevaselt kasutate. Erinevalt iOSist on Android juba aastaid lubanud oma ökosüsteemis eksisteerida mitu rakenduste poodi, andes teile vabaduse leida ja installida rakendusi oma lemmikallikatest.



Selles õpetuses tutvume F-droidiga, rakenduste kataloogiga, mis on alternatiiviks sellistele rakenduste poodidele nagu Google Play Store ja Microsoft Store.



## F-Droidiga alustamine



F-Droid on rakenduste ja tööriistade pood, mis võimaldab paigaldada tasuta avatud lähtekoodiga rakendusi Androidi platvormile. F-droid ise on avatud lähtekoodiga projekt, mille käivitasid 2010. aastal Ciaran Gultnieks ja mitmed teised toetajad. Projekti peamine eesmärk on teha avatud lähtekoodiga rakendused kättesaadavaks ja võimaldada avatud lähtekoodiga projektide algatajatel leida platvorm, kus nad saavad oma vahendeid avaldada, ilma et nad peaksid viitama Google Play Store'ile.



Kahjuks ei ole F-Droid iOS-i jaoks kättesaadav rakendus ja see sisaldab paljusid Android-süsteemide jaoks mõeldud tööriistu.



Saate F-droidi alla laadida [ametlikust veebisaidist](https://f-droid.org/) APK-formaadis ja paigaldada selle käsitsi oma Android-telefonile.



![download](assets/fr/02.webp)



Androidi puhul veenduge, et te annate paigaldusõigused brauserile, kust te F-Droid alla laadisite.



Kui paigaldamine on lõpetatud, käivitab F-Droid avatud lähtekoodiga rakenduste kataloogide uuendamise, et rikastada rakendusi poes.



![repositories](assets/fr/03.webp)



Nüüd saate oma telefoni rakendusi installida ilma Google Play poe kaudu.



## F-Droid raamatupood



Rakenduste poest leiad mitu kategooriat rakendusi, mis sobivad sinu vajadustele. Vahekaardilt **Kategooriad** leiate üle 20 tüüpi rakenduse, alates brauseritest kuni vabade tekstiredaktoriteni, mis kõik nõuavad teilt võimalikult vähe teavet.



Kas soovite paigaldada konkreetse rakenduse? Klõpsake nupul **Search** ja sisestage seejärel otsitava rakenduse nimi.



![search](assets/fr/04.webp)



F-Droid pakub põhjalikku teavet iga rakenduse kohta, mida soovite paigaldada.



Kui klõpsate taotlusel, leiate muu hulgas:




- Viimases versioonis lisatud funktsioonid ja muudatused
- Rakenduse üksikasjalik kirjeldus, selle funktsioonid, kasutamise põhjused ja projekti taga olev avatud lähtekoodiga kogukond.



![features](assets/fr/05.webp)





- Projektis kasutatav litsents, lingid lähtekoodile ja rakenduse kasutamisel ilmnenud probleemidele
- Rakenduses nõutavad load



![permissions](assets/fr/06.webp)



Lisateavet leiate meie Thunderbirdi õpetusest:



https://planb.network/tutorials/computer-security/communication/thunderbird-91d02325-0361-4641-b152-8975890284a8

F-Droid annab teile kogu vajaliku teabe, et otsustada, kas rakenduse kasutamine kaitseb teie andmeid ja suurendab teie privaatsust. Skaneerige kõik rakendused, mida soovite kasutada, seejärel klõpsake rakenduse allalaadimiseks ja installimiseks nupule **Install**.


Andke F-Droidile paigaldusõigused, lubades selle võimaluse oma seadetes.



![settings](assets/fr/07.webp)



## Exchange teie rakendused



F-Droid julgustab avatud lähtekoodiga ja kogukonna panust, eelkõige oma **Near By** Exchange valiku kaudu. Ühendage end ümbritsevate kasutajatega läbi:




- Bluetoothi tuvastamine;
- Sama Wi-Fi-võrk;
- QR-koodi või IP:PORT Address sisestamiseks teie veebilehitsejas.



Selle võimaluse abil saate oma Android-telefonile paigaldatud rakendusi sõprade ja pereliikmetega paari sammuga jagada ja vastu võtta.



![swap](assets/fr/08.webp)



## Uuendused



Vaadake vahekaardil **Update** kättesaadavate värskenduste loetelu ja lugege kindlasti ka teavet iga rakenduse uute versioonide kohta, et saada teada teie kasutatava versiooni olulistest muudatustest.



![updates](assets/fr/09.webp)



Saate olemasolevate rakenduste nimekirja uuendada ka lehte värskendades (kerige alla).



## Lisage oma rakendused



F-Droid on avatud lähtekoodiga projekt, mis julgustab panustama rakendustesse, mis seavad kasutajate privaatsuse prioriteediks. F-Droid GitLab'i lähtekoodi panustamise kaudu saate lisada oma Androidi mobiilirakenduse poodi.



Teie rakendus peab olema avatud lähtekoodiga, mille lähtekood on avalikult kättesaadav näiteks GitHubis või GitLabis.


Seejärel peate koostama YAML-faili (metaandmed), mis kirjeldab teie rakendust, sealhulgas kogu teavet ja selle kasutamiseks vajalikke õigusi, järgides F-Droidi pakutud [metaandmete malli](https://f-droid.org/docs/Build_Metadata_Reference/).



[Dokumentatsiooni] (https://f-droid.org/en/docs/) jaotises **Developers** leiate kõik ressursid, mida vajate oma rakenduste avaldamiseks ja hooldamiseks F-Droidis.



### Terviklikkus ja ohutus



Avatud lähtekoodiga rakenduste kasutuselevõtt on sageli sünonüümiks suuremale turvalisusele, kuid ka märkimisväärsele riskile. Kuidas saab tagada, et F-Droidil kättesaadava rakenduse lähtekoodis ei ole pahatahtlikke muudatusi?



F-Droid kompileerib rakendusi oma serverites, tuginedes ametlikule lähtekoodile ja kompileerimisjuhistele. Iga avaldatud rakendus koostatakse uuesti ja kontrollitakse, et tagada, et seda ei ole kahjustatud. See tagab, et pakutav APK vastab arendajate avaldatud lähtekoodile. Veelgi enam, iga F-Droid'i kaudu paigaldatud rakendus allkirjastatakse digitaalselt ja seejärel võrreldakse allkirja sõrmejälge rakenduse arendajate poolt ametlikul veebisaidil või Git-hoidlas avaldatud sõrmejäljega.



Kui sulle meeldis see õpetus, siis uuri lähemalt meie IT-turbe ja andmehalduse kursuse kohta:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1