---
name: Olvid
description: Privaatsõnumid kõigile
---
![cover](assets/cover.webp)



Olvid on 2019. aastal käivitatud Prantsuse kiirsõnumirakendus, mis on loodud pakkuma kõrgetasemelist turvalisust, ilma privaatsust ohustamata. Erinevalt WhatsAppist või Signalist ei küsi Olvid registreerimisel mingeid isikuandmeid: ei telefoninumbrit, ei e-posti, mitte midagi. Kasutajate vaheline tuvastamine põhineb Exchange võtmetel, ilma kataloogiserveri või jagatud Address raamatuta.



Kõik sõnumid on lõpuni krüpteeritud, kasutades originaalset krüptograafilist protokolli, mis on loodud ka metaandmete kaitsmiseks: keegi ei tea, kellega ja millal sa räägid. Kliendikood on avatud lähtekoodiga, kuid keskne server, mida kasutatakse krüpteeritud sõnumite suunamiseks, on jätkuvalt kaitstud ja asub AWSis.

Olvidi turvamudel tugineb olulisele põhimõttele: digitaalsete identiteetide loomisel ei usaldata mitte ühtegi kolmandat osapoolt. Erinevalt enamikust krüpteeritud sõnumside rakendustest, mis tuginevad tsentraliseeritud kataloogile kasutajate identiteetide haldamiseks, ei sõltu Olvid ühestki keskserverist suhtluse tervikluse tagamisel. Selline arhitektuur välistab riskid, mis kaasnevad kataloogi võimaliku kahjustumisega.

Olvid kasutab siiski sõnumite edastamiseks keskserverit, mille roll on rangelt logistiline: krüpteeritud sõnumite asünkroonne edastamine. Server ei osale krüpteerimisprotsessis, ei tea kasutajate tegelikke identiteete ega sõnumite sisu või metaandmeid (v.a vastuvõtja avalik võti, mida kasutatakse suunamiseks). Seega võib seda serverit vaikimisi pidada vaenulikuks, ohustamata süsteemi turvalisust. Isegi kui see kompromiteeritaks, ei annaks see juurdepääsu suhtluse sisule. Olvid kasutab tsentraliseeritud sõnumiedastust (tõhususe ja teenuse kvaliteedi huvides), säilitades samas infrastruktuurist sõltumatu turvalisuse.


Olvid pakub tasuta versiooni ja tellimusversiooni hinnaga 4,99 eurot kuus. Tasuta versioon pakub täielikku funktsionaalsust, välja arvatud heli- ja videokõnede tegemine (kuigi neid on võimalik vastu võtta), ning ei võimalda konto sünkroniseerimist mitme seadme vahel. Seega, kui plaanite kasutada ainult oma nutitelefoni ja teil ei ole vaja helistada, on Olvid suurepärane lahendus.



Olvid on sertifitseeritud ANSSI (Prantsuse küberturvalisuse ametiasutus) poolt. See rakendus on suurepärane alternatiiv traditsioonilistele sõnumiteenustele (WhatsApp, Facebook Messenger, WeChat...) neile, kes otsivad privaatsust, säilitades samas kasutamise lihtsuse.


| Rakendus             | E2EE 1:1        | E2EE grupid     | Anonüümne registreerimine | Avatud lähtekoodiga kliendi litsents | Avatud lähtekoodiga serveri litsents | Detsentraliseeritud server | Loomise aasta |
| -------------------- | --------------- | --------------- | ------------------------- | ------------------------------------ | ------------------------------------ | -------------------------- | ------------- |
| WhatsApp             | ✅               | ✅               | ❌                         | ❌                                    | ❌                                    | ❌                          | 2009          |
| WeChat               | ❌               | ❌               | ❌                         | ❌                                    | ❌                                    | ❌                          | 2011          |
| Facebook Messenger   | ✅               | 🟡 (valikuline) | ❌                         | ❌                                    | ❌                                    | ❌                          | 2011          |
| Telegram             | 🟡 (valikuline) | ❌               | 🟡                        | ✅                                    | ❌                                    | ❌                          | 2013          |
| LINE                 | ✅               | ✅               | ❌                         | ❌                                    | ❌                                    | ❌                          | 2011          |
| Signal               | ✅               | ✅               | ❌                         | ✅                                    | ✅                                    | ❌                          | 2014          |
| Threema              | ✅               | ✅               | ✅                         | ✅                                    | ❌                                    | ❌                          | 2012          |
| Element (Matrix)     | ✅               | ✅               | ✅                         | ✅                                    | ✅                                    | 🟡 (födereeritud)          | 2016          |
| Delta Chat           | ✅               | ✅               | ✅                         | ✅                                    | N/A                                  | 🟡 (e-posti kaudu)         | 2017          |
| Conversations (XMPP) | ✅               | ✅               | ✅                         | ✅                                    | ✅                                    | 🟡 (födereeritud)          | 2014          |
| Session              | ✅               | ✅               | ✅                         | ✅                                    | ✅                                    | ✅                          | 2020          |
| SimpleX              | ✅               | ✅               | ✅                         | ✅                                    | ✅                                    | ✅                          | 2021          |
| **Olvid**            | **✅**           | **✅**           | **✅**                     | **✅**                                | **❌**                                | 🟡(kataloog puudub)        | **2019**      |
| Keet                 | ✅               | ✅               | ✅                         | ❌                                    | N/A                                  | ✅                          | 2022          |
| Jami                 | ✅               | ✅               | ✅                         | ✅                                    | N/A                                  | ✅                          | 2005          |
| Briar                | ✅               | ✅               | ✅                         | ✅                                    | N/A                                  | ✅                          | 2018          |
| Tox                  | ✅               | ✅               | ✅                         | ✅                                    | N/A                                  | ✅                          | 2013          |

*E2EE = End-to-end krüpteerimine*



## Installige rakendus Olvid



Olvid on saadaval kõigil platvormidel. Rakenduse saate alla laadida otse oma telefoni rakenduste poest:




- [Google Play](https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store](https://apps.apple.com/app/olvid/id1414865219);



Androidis on võimalik ka [paigaldada APK kaudu](https://www.olvid.io/download/).



Selles õpetuses keskendume mobiilsele versioonile, kuid palun pange tähele, et [arvutiversioonid on samuti saadaval](https://www.olvid.io/download/) (MacOS, Linux ja Windows). Kui valite tasulise versiooni, saate sünkroonida oma kontot mitmel seadmel.



![Image](assets/fr/01.webp)



## Loo konto Olvid'is



Kui käivitate rakenduse esimest korda, klõpsake nupule "*Mina olen uus kasutaja*".



![Image](assets/fr/02.webp)



Valige hüüdnimi või sisestage oma ees- ja perekonnanimi.



![Image](assets/fr/03.webp)



Lisage profiilifoto.



![Image](assets/fr/04.webp)



Teie konto on nüüd loodud.



![Image](assets/fr/05.webp)



Et vältida juurdepääsu kaotamist teie Olvid-kontole, soovitame luua automaatsed varukoopiad. Selleks avage seaded, klõpsates Interface paremal ülaosas asuvatele kolmele punktile ja valige seejärel "*Settings*".

⚠️ **Tähelepanu**: alates Olvid versioonist 3.7 on teie profiilide ja kontaktide varundamise protseduur asendatud uuega. See õpetus esitab endiselt vana versiooni. Uue versiooni leiate nende KKK-st: [💾 Teie profiilide varundamine](https://www.olvid.io/faq/sauvegarder-vos-profils/)

![Image](assets/fr/06.webp)



Minge menüüsse "*Klahvide ja kontaktide salvestamine*".



![Image](assets/fr/07.webp)



Seejärel klõpsake nupule "*generate varukoopia võti*". See võti krüpteerib teie varukoopiad. Kui teil on vaja taastada oma konto mõnes teises seadmes ja teil ei ole sellele enam juurdepääsu, vajate selle dekrüpteerimiseks nii varukoopiat kui ka seda võtit.



![Image](assets/fr/08.webp)



Hoidke seda võtit turvalises kohas. Võite teha ka paberkoopia.



![Image](assets/fr/09.webp)



Seejärel saate valida, kas soovite luua kohaliku varukoopia või automaatse varukoopia pilveteenuses. See teine võimalus on väga soovitatav, et tagada juurdepääs teie Olvid-kontole igas olukorras, isegi kui te kaotate oma telefoni.



![Image](assets/fr/10.webp)



Veenduge, et valik "*Automaatse varundamise lubamine*" on märgitud.



![Image](assets/fr/11.webp)



Saate uurida ka muid olemasolevaid seadeid, et kohandada rakendus oma vajadustele vastavaks.



![Image](assets/fr/12.webp)



## Sõnumite saatmine Olvidiga



Sõnumite saatmiseks peate kõigepealt lisama kontaktid. Vajutage avalehel sinisele nupule "*+*".



![Image](assets/fr/13.webp)



Seejärel kuvab Olvid teie kasutajatunnuse. Seejärel saate selle edastada inimestele, kellega soovite suhelda, et nad saaksid teid kontaktina lisada.



Isiku lisamiseks skannige tema ID-kaamera abil või sisestage see käsitsi, klõpsates kolmel väikesel punktil üleval paremas nurgas.



![Image](assets/fr/14.webp)



Kui ID on skaneeritud, võite lasta kontaktil skaneerida kuvatavat QR-koodi või saata talle kaugühenduse taotluse, klõpsates "*kaugkontakt*".



![Image](assets/fr/15.webp)



Ühendus on nüüdseks loodud.



![Image](assets/fr/16.webp)



Nüüd saate alustada sõnumite ja muu sisu vahetamist oma korrespondendiga!



![Image](assets/fr/17.webp)



Kodulehelt leiate kõik oma vestlused.



![Image](assets/fr/18.webp)



Teine vahekaart sisaldab kõiki teie kontakte.



![Image](assets/fr/19.webp)



Saate luua ka grupiarutelusid.



![Image](assets/fr/20.webp)



Palju õnne, oled nüüd kursis Olvid sõnumside kasutamisega, mis on suurepärane alternatiiv WathsAppile! Kui leidsid selle õpetuse kasulikuks, oleksin väga tänulik, kui jätaksid allpool Green pöidla. Palun jagage seda õpetust julgelt oma sotsiaalsetes võrgustikes. Tänan teid väga!



Soovitan ka seda teist õpetust, kus ma tutvustan teile Proton Maili, mis on palju privaatsussõbralikum alternatiiv Gmailile :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2