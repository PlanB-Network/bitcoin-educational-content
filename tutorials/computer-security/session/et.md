---
name: Session
description: Saatke krüpteeritud sõnumeid, mitte metaandmeid
---
![cover](assets/cover.webp)



Session on 2020. aastal loodud krüpteeritud sõnumirakendus, mille eesmärk on pakkuda suuremat konfidentsiaalsust kui traditsiooniline sõnumivahetus. Selle töötas esmalt välja *Oxen Privacy Tech Foundation*, seejärel *Session Technology Foundation*.



Sessioonil on mõned huvitavad tehnilised omadused: sõnumite otsast lõpuni krüpteerimine, detsentraliseeritud võrk, mis on korraldatud kättesaadavuse ja koondamise tagamiseks, ning Torist inspireeritud sibulareiting. Erinevalt WathsAppist või Signalist, mis nõuavad registreerimiseks telefoninumbrit, ei nõuta Sessionis mingeid isikuandmeid (ei numbrit, ei e-posti aadressi, vaid ainult paar krüptograafilist võtit).



Sessioon võimaldab saata sõnumeid, faile, kõnesõnumeid, helikõnesid, samuti kuni 100-liikmelisi rühmi (ja kogukondi), vähendades samal ajal metaandmete lekkeid.



![Image](assets/fr/01.webp)



Sessioon on suunatud eelkõige kasutajatele, kes seavad konfidentsiaalsuse oma prioriteetide keskmesse. See sõnumiteenus kujutab endast tõsist alternatiivi WhatsAppile, mille ülesehitus on loodud vastu pidama kaasaegsetele jälgimismudelitele.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end krüpteerimine*



## Installige seansirakendus



Seanss on saadaval kõigil platvormidel. Rakenduse saate alla laadida otse oma telefoni rakenduste poest:




- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).



Androidis on võimalik ka [paigaldada APK kaudu](https://github.com/session-foundation/session-android/releases).



Selles õpetuses keskendume mobiilsele versioonile, kuid pange tähele, et [arvutiversioonid on samuti saadaval](https://getsession.org/download) (MacOS, Linux ja Windows). Hiljem vaatame, kuidas sünkroonida kontot mitme seadme vahel.



## Looge konto Sessionil



Esimesel käivitamisel klõpsake "*Loo konto*".



![Image](assets/fr/02.webp)



Valige oma profiilile kuvamisnimi. See võib olla pseudonüüm või teie pärisnimi.



![Image](assets/fr/03.webp)



Seejärel peate valima kahe teate haldamise režiimi vahel:





- Kiire režiim (**Firebase Cloud Messaging/Apple Push Notification Service**): võimaldab teil saada teateid peaaegu reaalajas tänu Google'i või Apple'i (sõltuvalt teie süsteemist) pakutavatele teavitusteenustele. Selle toimimiseks edastatakse Google'ile või Apple'ile teie IP Address ja unikaalne teate ID ning STF-serveris (Tori kaudu) registreeritakse ka seansikonto ID. See režiim hõlmab metaandmete (küll minimaalset) paljastamist, kuid ei ohusta sõnumite sisu ega kontakte ning ei võimalda teie tegelikku tegevust jälgida. See režiim on seega reageerimisvõime poolest tõhusam, kuid tugineb tsentraliseeritud infrastruktuurile ja on konfidentsiaalsuse seisukohast veidi vähem tõhus.





- Aeglane režiim (**taustaküsitlus**): Seansirakendus jääb taustal aktiivseks, küsitledes perioodiliselt võrku uute sõnumite saamiseks. See lähenemisviis tagab suurema konfidentsiaalsuse kui esimene, kuna andmeid ei edastata kolmandatele serveritele; ei Google, Apple ega STF-i serverid ei saa mingit teavet. Teisest küljest on sellel režiimil kaks puudust: teated võivad hilineda (kuni mitu minutit) ja energiatarbimine on üldiselt suurem, kuna rakendus tegutseb taustal.



![Image](assets/fr/04.webp)



Nüüd olete ühendatud seansirakendusega ja saate alustada sõnumite vahetamist.



![Image](assets/fr/05.webp)



## Salvesta oma seansikonto



Esimene asi, mida enne Sessioni kasutamise alustamist teha, on oma konto salvestamine, et saaksite selle taastada, kui kaotate oma seadme. Selleks klõpsake nupule "*Jätka*" nupu "*Talleta oma taastamisparool*" kõrval.



![Image](assets/fr/06.webp)



Seanss kuvab seejärel Mnemonic fraasi. Kopeerige see hoolikalt ja hoidke seda turvalises kohas. See fraas annab täieliku juurdepääsu teie Sessioni kontole, seega on oluline seda mitte avaldada. Seda on vaja, et pääseda oma kontole ligi teises seadmes, eriti kui teie praegune telefon kaob või asendatakse.



![Image](assets/fr/07.webp)



See fraas toimib sarnaselt Mnemonic fraasidega, mida kasutatakse Bitcoin portfellis. Seetõttu soovitan teil tutvuda selle teise õpetusega, kus ma selgitan Mnemonic fraasi salvestamise parimaid tavasid:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Pöörake tähelepanu**: Erinevalt Bitcoin portfoolios kasutatavatest Mnemonic fraasidest, peate Sessioni puhul **tingimata salvestama iga sõna tervikuna**. Esimesed 4 tähte ei piisa!



## Seansirakenduse seadistamine



Rakenduse seadete avamiseks klõpsake Interface vasakus ülaservas oma profiilifotol. Siin saate lisada profiilifoto.



![Image](assets/fr/08.webp)



Menüüs "*Privaatsus*" saate lubada või keelata mitmesuguseid funktsioone (ettevaatust, mõned neist võivad teie IP Address avalikustada). Samuti soovitan aktiveerida valik "*Lock App*", mis nõuab rakendusele juurdepääsuks autentimist.



![Image](assets/fr/09.webp)



Menüüst "*Teavitus*" leiate valiku "*Kiire režiim*" ja "*Hiljem režiim*" vahel (vt õpetuse eelmised osad). Te saate ka teateid kohandada vastavalt oma eelistustele.



![Image](assets/fr/10.webp)



Lõpuks minge menüüsse "*Esitus*", et kohandada Interface oma maitse järgi. Menüü "*Recovery Password*" võimaldab teil taastada oma Mnemonic fraasi, kui soovite teha uue varukoopia.



![Image](assets/fr/11.webp)



## Sõnumite saatmine koos seansiga



Teiste inimestega kontakteerumiseks klõpsake avalehel nupule "*+*".



![Image](assets/fr/12.webp)



Saadaval on mitu võimalust. Kui soovite luua grupi või sellega liituda, valige "*Loo grupp*" või "*Ühendu kogukonnaga*".



![Image](assets/fr/13.webp)



Kui soovite, et keegi lisaks teid kontakti, saate lasta neil skannida oma seansi ID-d QR-koodina.



![Image](assets/fr/14.webp)



Oma sisselogimise saatmiseks eemalt, klõpsake "*Kutsu sõber*". Seejärel saate kopeerida oma seansi ID ja saata selle teise sidekanali kaudu. Te saate selle teabe kätte ka oma profiilifotole klõpsates avalehel.



![Image](assets/fr/15.webp)



Kui teil on teise isiku seansi ID ja soovite selle lisada, klõpsake "*Uus sõnum*".



![Image](assets/fr/16.webp)



Seejärel saate kleepida selle identifikaatori teksti või skaneerida seda otse, kui teil on see QR-kood.



![Image](assets/fr/17.webp)



Seejärel saatke sellele isikule esialgne sõnum.



![Image](assets/fr/18.webp)



Niipea, kui inimene nõustub teie taotlusega, näete tema kasutajanime ja saate temaga vabalt vestelda.



![Image](assets/fr/19.webp)



## Töölaua tarkvara sünkroniseerimine



Konto sünkroniseerimiseks arvutis peate installima tarkvara. [Laadige see alla ametlikust veebisaidist](https://getsession.org/download). Soovitan teil enne installimist kontrollida selle autentsust ja terviklikkust.



![Image](assets/fr/20.webp)



Esimesel käivitamisel klõpsake nupule "*Mulle on konto*".



![Image](assets/fr/21.webp)



Sisestage oma Mnemonic fraas, jättes iga sõna vahele tühiku.



![Image](assets/fr/22.webp)



Nüüd saate oma vestlustele juurdepääsu arvutist.



![Image](assets/fr/23.webp)



Palju õnne, sa oled nüüd saanud Session messingi kasutamise, mis on suurepärane alternatiiv WathsAppile!



Soovitan ka seda teist õpetust, kus ma tutvustan Threema't, mis on veel üks huvitav alternatiiv teie sõnumirakenduse jaoks:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74