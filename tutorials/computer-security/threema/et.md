---
name: Threema
description: Turvaline, anonüümne kiirsõnumivahetus
---
![cover](assets/cover.webp)



2012. aastal Šveitsis asutatud Threema on kiirsõnumirakendus, mille eesmärk on tagada privaatsus ja turvalisus. Erinevalt WhatsAppist, Telegramist või Signalist ei nõua Threema konto loomiseks telefoninumbrit ega e-posti Address. Igal kasutajal on unikaalne identifikaator, mis võimaldab täiesti anonüümset registreerimist.



Tehnilisest küljest on side Threema kaudu lõpuni krüpteeritud. Mobiilirakenduse kood on alates 2020. aastast avatud lähtekoodiga, kuid serveriinfrastruktuur on endiselt patenteeritud ja tsentraliseeritud. Servereid majutatakse ainult Šveitsis (riik, mis on tuntud oma andmekaitse õigusraamistiku poolest).



![Image](assets/fr/01.webp)



Threemal on põhilised kliendid Androidile ja iOSile. Samuti on olemas veebirakendus, samuti on saadaval tarkvara Windowsile, Linuxile ja macOSile. Nende kasutamiseks tuleb aga kõigepealt registreeruda mobiilseadmes.



Threema rakendus ei ole tasuta. See töötab ühekordse ostu-mudeli alusel: 5,99 eurot, et kasutada rakendust kogu elu (või 4,99 eurot, kui ostate selle otse). Et Threema't tõesti anonüümselt kasutada, peab ka maksmine olema anonüümne. Seepärast saab Android-versiooni aktiveerimiseks osta aktiveerimisvõtme bitcoinides või sularahas "*Threema poest*". IOS-i puhul peab ostmine seevastu toimuma App Store'i kaudu, kuna Apple'il on piirangud rakenduste rahaks muutmisel.



On olemas ka spetsiaalne äriversioon nimega "*Threema Work*". Selles õpetuses keskendume koduversioonile.



| Rakendus             | E2EE 1:1       | E2EE grupid    | Anonüümne registreerimine | Avatud lähtekoodiga kliendi litsents | Avatud lähtekoodiga serveri litsents | Detsentraliseeritud server | Loomise aasta     |
| -------------------- | -------------- | -------------- | ------------------------- | ------------------------------------ | ------------------------------------ | -------------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                         | ❌                                    | ❌                                    | ❌                          | 2009              |
| WeChat               | ❌              | ❌              | ❌                         | ❌                                    | ❌                                    | ❌                          | 2011              |
| Facebook Messenger   | ✅              | 🟡 (valikuline) | ❌                         | ❌                                    | ❌                                    | ❌                          | 2011              |
| Telegram             | 🟡 (valikuline) | ❌              | 🟡                        | ✅                                    | ❌                                    | ❌                          | 2013              |
| LINE                 | ✅              | ✅              | ❌                         | ❌                                    | ❌                                    | ❌                          | 2011              |
| Signal               | ✅              | ✅              | ❌                         | ✅                                    | ✅                                    | ❌                          | 2014              |
| Threema              | ✅              | ✅              | ✅                         | ✅                                    | ❌                                    | ❌                          | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                         | ✅                                    | ✅                                    | 🟡 (födereeritud)         | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                         | ✅                                    | N/A                                  | 🟡 (e-posti kaudu)        | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                         | ✅                                    | ✅                                    | 🟡 (födereeritud)         | 2014              |
| Session              | ✅              | ✅              | ✅                         | ✅                                    | ✅                                    | ✅                          | 2020              |
| SimpleX              | ✅              | ✅              | ✅                         | ✅                                    | ✅                                    | ✅                          | 2021              |
| Olvid                | ✅              | ✅              | ✅                         | ✅                                    | ❌                                    | 🟡(kataloog puudub)       | 2019              |
| Keet                 | ✅              | ✅              | ✅                         | ❌                                    | N/A                                  | ✅                          | 2022              |
| Jami                 | ✅              | ✅              | ✅                         | ✅                                    | N/A                                  | ✅                          | 2005              |
| Briar                | ✅              | ✅              | ✅                         | ✅                                    | N/A                                  | ✅                          | 2018              |
| Tox                  | ✅              | ✅              | ✅                         | ✅                                    | N/A                                  | ✅                          | 2013              |

*E2EE = End-to-end krüpteerimine*



## Paigaldage Threema rakendus



Threema on saadaval kõigil platvormidel. Rakenduse saate alla laadida otse oma telefoni rakenduste poest:




- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold] (https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery] (https://appgallery.huawei.com/#/app/C103713829);
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



Androidis on võimalik ka [paigaldada APK kaudu](https://shop.threema.ch/en/download).



On olemas ka [arvutiversioonid](https://threema.ch/download) (MacOS, Linux ja Windows). See õpetus näitab, kuidas neid sünkroonida.



## Osta Threema litsents



Kui olete rakenduse paigaldanud, kui olete läinud otse rakenduste poe kaudu, olete juba litsentsi eest maksnud ja peaksite sellele kohe ligi pääsema. Kui läksite F-Droidi või APK kaudu, peate nüüd ostma litsentsi ametlikul veebisaidil.



[Mine "*Threema poodi*" (https://shop.threema.ch/) ja klõpsa nupule "*Ota Threema for Android*".



![Image](assets/fr/02.webp)



Valige litsentside arv, mida soovite osta (ainult üks, kui see on ainult teie jaoks), valige valuuta ja valige litsentside tarneviis. Võite valida, kas soovite litsentsi saada e-posti teel või otse saidil, kui soovite jääda anonüümseks. Seejärel klõpsake nupule "*Maksmise jätkamine*".



![Image](assets/fr/03.webp)



Valige oma makseviis. Minu puhul kavatsen maksta bitcoin'idega, mida soovitan ka teil teha, sest see võimaldab teil jääda anonüümseks (tingimusel, et kasutate Bitcoin asjakohaselt) ja on palju mugavam kui sularaha kaugmakse. Seejärel klõpsake nupule "*Järgmine*".



![Image](assets/fr/04.webp)



Kui te ei vaja Invoice, klõpsake uuesti "*Järgmine*", ilma et sisestaksite mingeid isikuandmeid.



Seejärel kinnitage oma ostu, klõpsates "*Kinnitage makse*".



![Image](assets/fr/05.webp)



Seejärel peate saatma näidatud summa Bitcoin Address-le (kahjuks ei toeta Lightning veel). Kui tehing on kinnitatud Blockchain-l, klõpsake Invoice kõrval nupule "*Close*".



Seejärel saate juurdepääsu oma litsentsivõtmele. Pange tähele: kui te ei ole sisestanud e-posti Address, kuvatakse see võti ainult siin. Ärge unustage salvestada lehe URL, et saaksite sellele vajadusel hiljem juurde pääseda.



![Image](assets/fr/06.webp)



## Loo konto Threema's



Nüüd, kui teil on litsentsivõti olemas, saate lõpuks rakenduse käivitada. Esimesel käivitamisel, kui te ei ole Threema't rakenduspoe kaudu ostnud, palutakse teil sisestada oma litsentsivõti, mis on ostetud saidilt.



![Image](assets/fr/07.webp)



Seejärel klõpsake nupule "*Set up now*".



![Image](assets/fr/08.webp)



Liigutage sõrmega üle ekraani, et generate oleks võimalik luua oma "*Threema ID*" entroopia allikas.



![Image](assets/fr/09.webp)



Seejärel kuvatakse teie "*Threema ID*". See võimaldab teil võtta ühendust teiste kasutajatega. Vajutage nupule "*Järgmine*".



![Image](assets/fr/10.webp)



Valige parool. See võimaldab teil vajaduse korral taastada juurdepääsu oma kontole. Tehke oma parool võimalikult pikaks ja juhuslikuks ning hoidke selle turvalist koopiat, näiteks paroolihalduris.



![Image](assets/fr/11.webp)



Seejärel valige kasutajanimi, mis võib olla kas teie pärisnimi või pseudonüüm.



![Image](assets/fr/12.webp)



Seejärel saate siduda oma Threema ID oma telefoninumbriga. See lihtsustab teie kontaktide otsimist, kuid kui te kasutate Threema't, siis ka selleks, et säilitada teie anonüümsus: seega on parem seda mitte siduda. Vajutage nupule "*Järgmine*".



![Image](assets/fr/13.webp)



Kui olete selle sammu lõpetanud, klõpsake nuppu "*Finish*".



![Image](assets/fr/14.webp)



Nüüd olete ühendatud Threema'ga ja saate alustada suhtlemist.



![Image](assets/fr/15.webp)



## Seadistage Threema



Kõigepealt pääsete seadistustesse, klõpsates kolmel väikesel punktil üleval paremas nurgas, seejärel valige "*Settings*".



![Image](assets/fr/16.webp)



Vahekaardil "*Privaatsus*" leiate mitu valikut, mida saate kohandada vastavalt oma vajadustele:




- Telefonis olevate kontaktide sünkroniseerimine ;
- Sõnumite vastuvõtmine tundmatutelt inimestelt;
- Andmete sisestamise ajal näituri kirjutamine ;
- Teade sõnumite kättesaamise kohta..



![Image](assets/fr/17.webp)



Soovitan vahekaardil "*Turvalisus*" aktiveerida valik "*Lukustusmehhanism*", et kaitsta ligipääsu rakendusele. Samuti on soovitatav aktiveerida passphrase, et kaitsta oma kohalikke varukoopiaid.



![Image](assets/fr/18.webp)



Tutvu vabalt ka muude sätete jaotistega, et kohandada rakendus oma eelistuste järgi.



![Image](assets/fr/19.webp)



## Threema konto varundamine



Enne sõnumite vahetamise alustamist on oluline kavandada viis, kuidas oma kontot taastada, eriti kui telefon on vahetatud või kaotatud. Selleks klõpsake Interface ülemises paremas servas kolmele punktile, seejärel avage menüü "*Backups*".



![Image](assets/fr/20.webp)



Siit leiate kaks võimalust oma andmete varundamiseks:




- "*Threema Safe*";
- "*Andmete varundamine*".



"Threema Safe* salvestab kogu teie kontoteabe, välja arvatud teie vestlused, Threema serverites. Need andmed on krüpteeritud teie poolt konto loomisel valitud parooliga, mis tagab, et Threema ei pääse neile ligi. Varukoopiaid tehakse automaatselt ja regulaarselt.



"*Threema Safe*" abil peate oma konto taastamiseks uues seadmes ainult sisestama oma "*Threema ID*" ja parooli. Kui kumbki neist kahest teabest puudub, on teie konto taastamine võimatu.



See valik võimaldab teil ainult oma ID-d, profiili, kontakte, rühmi ja teatavaid seadeid, kuid **ei vestlusajalugu**.



"*Threema Safe*" aktiveerimiseks tuleb lihtsalt märkida valik menüüs "*Backups*".



![Image](assets/fr/21.webp)



Kui soovite ka oma vestlusajalugu varundada ja taastada, peate kasutama valikut "*Data Backup*". See loob teie kontost täieliku varukoopia, mis salvestatakse lokaalselt teie telefoni. Peate selle varukoopia uude seadmesse üle kandma ja kasutama kogu konto taastamiseks oma parooli (ja võimaluse korral passphrase).



Kuna see varukoopia on ainult kohalik, tuleb seda regulaarselt kopeerida välisele andmekandjale. Vastasel juhul on seadme kadumisel taastamine võimatu. Seetõttu sobib see meetod kõige paremini kavandatud ülekandmiseks ühelt seadmelt teisele, mitte aga hädaolukorraks.



Pange tähele: "*Data Backup*" töötab ainult siis, kui kasutate sama operatsioonisüsteemi. Te ei saa seda kasutada näiteks Samsungilt iPhone'ile üleminekuks.



## Kohandage oma Threema profiili



Klõpsake Interface vasakus ülanurgas oma profiilipildil, seejärel valige "*Minu profiil*".



![Image](assets/fr/22.webp)



Siin saate kohandada oma profiili: lisada foto, valida, kes seda näha saavad, või vaadata oma Threema sisselogimist.



![Image](assets/fr/23.webp)



## PC tarkvara sünkroniseerimine



Kui soovite oma vestlustele juurdepääsu arvutis, saate oma Threema-konto sünkroonida spetsiaalse tarkvara abil. Laadige tarkvara oma operatsioonisüsteemi jaoks alla [ametlikust veebisaidist](https://threema.ch/en/download).



![Image](assets/fr/24.webp)



Klõpsake telefonis üleval paremal kolmel punktil, seejärel avage menüü "*Threema 2.0 for Desktop*".



![Image](assets/fr/25.webp)



Klõpsake nupule "*Lisata seade*", seejärel skannige oma telefoniga arvutis tarkvara poolt kuvatavat QR-koodi.



![Image](assets/fr/26.webp)



Sünkroniseerimise kinnitamiseks klõpsake tarkvaras kuvataval emotikonide grupil.



![Image](assets/fr/27.webp)



Logige oma arvutis sisse oma parooliga.



![Image](assets/fr/28.webp)



Lisaks mobiilirakendusele saate nüüd oma Threema-kontole ligi ka otse arvutist.



![Image](assets/fr/29.webp)



## Sõnumite saatmine Threema abil



Nüüd, kui kõik on õigesti seadistatud, võite alustada suhtlemist. Vajutage nupule "*Start chat*".



![Image](assets/fr/30.webp)



Valige "*Uus kontakt*".



![Image](assets/fr/31.webp)



Sisestage või skaneerige oma korrespondendi "*Threema ID*".



![Image](assets/fr/32.webp)



Klõpsake sõnumi ikoonil.



![Image](assets/fr/33.webp)



Saatke esimene sõnum oma korrespondendile.



![Image](assets/fr/34.webp)



Kui teie korrespondent vastab, luuakse ühendus ja te näete tema nime ja profiilifotot. Seejärel saate Exchange sõnumeid, multimeediafaile ja isegi helistada.



![Image](assets/fr/35.webp)



Palju õnne, sa oled nüüd kursis Threema sõnumite kasutamisega, mis on suurepärane alternatiiv WathsAppile! Kui leidsid selle õpetuse kasulikuks, oleksin väga tänulik, kui jätaksid allpool Green pöidla. Jagage seda õpetust julgelt oma sotsiaalvõrgustikes. Tänan teid väga!



Soovitan ka seda teist õpetust, kus ma tutvustan teile Proton Maili, mis on palju privaatsussõbralikum alternatiiv Gmailile :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2