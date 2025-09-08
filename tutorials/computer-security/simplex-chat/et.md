---
name: SimpleX vestlus
description: Esimene postkast ilma kasutajatunnuseta
---
![cover](assets/cover.webp)



2021. aastal käivitatud SimpleX on tasuta kiirsõnumirakendus, millel on radikaalselt erinev lähenemine privaatsusele. Erinevalt WhatsAppist, Signalist ja teistest tsentraliseeritud sõnumiteenustest eristub SimpleX oma kasutajahalduse poolest: ei ole kasutajatunnuseid, pseudonüüme, numbreid ega nähtavaid avalikke võtmeid. Selline identifikaatorite täielik puudumine muudab kasutajate omavahelise seostamise praktiliselt võimatuks, tagades kõrge privaatsuse taseme.



Erinevalt enamikust rakendustest, mis nõuavad kontot või telefoninumbrit, võimaldab SimpleX algatada vestlusi lingi või efektse QR-koodi jagamise teel. Iga link loob ainulaadse krüpteeritud kanali ning kontaktid ei saa saatjat leida ega temaga uuesti ühendust võtta ilma selgesõnalise Exchange-ta. Sõnumid on krüpteeritud otsast lõpuni ja läbivad releeserverid, mis kustutavad need pärast saatmist ning ei näe ei saatjat ega vastuvõtjat ega nende võtmeid.



![Image](assets/fr/01.webp)



Võrgustiku arhitektuur on täielikult detsentraliseeritud ja föderatsioonita: serverid ei tunne üksteist, nad ei hoia globaalset kataloogi ja nad ei halda ühtegi kasutaja profiili. Veelgi parem on see, et iga kasutaja saab kasutada oma releeserverit, jäädes samal ajal koostalitlusvõimeliseks avaliku võrgu serveritega.



SimpleX on täielikult avatud lähtekoodiga (kliendid, protokollid ja serverid), mis on saadaval Androidil, iOSil, Linuxil, Windowsil ja macOSil. Selle kohalik salvestusruum on krüpteeritud ja kaasaskantav, nii et saate profiili ühest seadmest teise üle kanda ilma tsentraliseeritud serverile toetumata.



SimpleX integreerib kõik sõnumirakenduste klassikalised funktsioonid. Selle ergonoomika jääb siiski vähem sujuvaks kui WhatsAppil või Signalil. Samuti võib selle kasutamine olla piiravam, eriti kontaktide lisamisel. Seega on see minu arvates asjakohane alternatiiv WhatsAppile või Signalile kasutajatele, kes seavad konfidentsiaalsuse oma prioriteetide keskmesse ja on seetõttu valmis tegema mõningaid järeleandmisi igapäevase kasutusmugavuse osas.



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



## Paigaldage SimpleXi vestlusrakendus



SimpleX Chat on saadaval kõigil platvormidel. Rakenduse saate alla laadida otse oma telefoni rakenduste poest:




- [Google Play](https://play.google.com/store/apps/details?id=chat.simplex.app);
- [App Store](https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084);
- [F-Droid](https://simplex.chat/fdroid/).



Androidis on võimalik ka [paigaldada APK kaudu](https://github.com/simplex-chat/simplex-chat/releases).



Selles õpetuses keskendume mobiilsele versioonile, kuid pange tähele, et [ka töölauaversioonid on saadaval](https://simplex.chat/downloads/) (MacOS, Linux ja Windows). Lauaversiooni on võimalik siduda olemasoleva mobiilikasutaja profiiliga, kuid selle sünkroniseerimise toimimiseks peavad mõlemad seadmed olema ühendatud samasse kohalikku võrku.



![Image](assets/fr/02.webp)



## Loo konto SimpleX Chatis



Kui käivitate rakenduse esimest korda, klõpsake nupule "*Loo oma profiil*".



![Image](assets/fr/03.webp)



Valige kasutajanimi, mis võib olla teie pärisnimi või pseudonüüm, ja seejärel klõpsake "*Loo*".



![Image](assets/fr/04.webp)



Seejärel määrake sagedus, millega rakendus hakkab uusi sõnumeid kontrollima. Kui teie telefoni aku kestus ei ole probleemiks, valige "*Instant*", et saada sõnumeid reaalajas. Kui soovite akut säästa ja vältida rakenduse taustal töötamist, valige "*Kui rakendus töötab*": saate siis teateid ainult siis, kui rakendus on avatud. Võimalik kompromiss on valida perioodiline kontroll iga 10 minuti järel.



Kui olete oma valiku teinud, klõpsake "*Kasutage vestlust*".



![Image](assets/fr/05.webp)



Nüüd olete ühendatud SimpleX Chatiga ja valmis alustama vestlust.



![Image](assets/fr/06.webp)



## SimpleX Chat'i seadistamine



Kõigepealt pääsete seadistustesse, klõpsates oma profiilifotol all paremas nurgas ja seejärel "*Sätted*".



![Image](assets/fr/07.webp)



Vaikimisi seaded sobivad üldiselt enamikule kasutajatele. Soovitan siiski minna menüüsse "*Database passphrase & export*". Seal saate oma SimpleX-konto andmebaasi varundamise eesmärgil eksportida.



Samuti saate muuta andmebaasi krüpteerimiseks kasutatavat passphrase. Vaikimisi on see juhuslikult genereeritud ja salvestatud lokaalselt teie seadmesse. Kui soovite, võite määrata oma passphrase ja kustutada lokaalse passphrase varukoopia: siis peate selle käsitsi sisestama iga kord, kui avate rakenduse, samuti siis, kui liigute teisele seadmele.



**Pöörake tähelepanu**: kui valite selle võimaluse, siis passphrase kadumine toob kaasa kõigi teie SimpleX-profiilide ja sõnumite püsiva kadumise.



![Image](assets/fr/08.webp)



Samuti soovitan teil minna menüüsse "*Privaatsus ja turvalisus*", kus saate aktiveerida valiku "*SimpleX Lock*". See kaitseb juurdepääsu rakendusele lukustuskoodiga.



![Image](assets/fr/09.webp)



Lõpuks võimaldavad menüüd "*Teavitused*" ja "*Esitus*" kohandada SimpleXi vestlust vastavalt oma eelistustele.



![Image](assets/fr/10.webp)



## Sõnumite saatmine SimpleX Chatiga



SimpleXi kaudu teise inimesega ühenduse loomiseks on teil kaks võimalust:




- Kasutage ühekordselt kasutatavat linki;
- Kasutage korduvkasutatavat staatilist Address.



Staatiline Address võimaldab kõigil, kes seda teavad, teiega SimpleXi kaudu ühendust võtta. See on püsiv Address, mida saab kasutada mitu korda, erinevate inimeste poolt, ilma ajalise piiranguta. Just see püsivus muudab selle rämpsposti suhtes haavatavamaks. Kuid erinevalt teistest sõnumirakendustest piisab SimpleX Address kustutamisest, et peatada kogu rämpspost, ilma et see mõjutaks olemasolevaid vestlusi. Tegelikult kasutatakse seda Address ainult esialgse ühenduse loomiseks ja seda ei ole enam vaja, kui Exchange on alanud.



Ühekordseid linke saab seevastu iga kasutaja kasutada ainult üks kord. Kui kontakt kasutab seda, muutub link kehtetuks. Iga uue ühenduse jaoks peate generate uue looma.



### Staatilise Address puhul



Kui soovite kasutada Address, klõpsake oma profiilipildil Interface vasakul allosas, seejärel valige "*Loo SimpleX Address*". Seejärel klõpsake uuesti "*Create SimpleX Address*".



![Image](assets/fr/11.webp)



Teie korduvkasutatav Address on nüüd loodud. Saate seda jagada inimestega, kes soovivad teiega ühendust võtta, näidates neile QR-koodi või saates neile lingi.



![Image](assets/fr/12.webp)



Vajutage nupule "*Address seaded*". Siin saate konfigureerida oma Address-ga seotud õigusi. Valik "*Jagamine kontaktidega*" muudab teie Address nähtavaks teie SimpleX-profiilis. Seejärel saavad teie kontaktid sellega tutvuda ja edastada selle teistele inimestele, kes soovivad teiega ühendust võtta.



Valik "*Auto-aktsepteerimine*" võtab automaatselt vastu teie Address kaudu sissetulevaid ühendusi. See tähendab, et igaüks, kellel on teie Address, saab näha teie profiili ja saata teile sõnumi, kui te ei aktiveeri valikut "*Accept incognito*". See peidab teie nime ja profiilifoto, kui uus ühendus luuakse, asendades need juhusliku pseudonüümiga, mis on iga vestluspartneri jaoks erinev.



![Image](assets/fr/13.webp)



### Korduvkasutatava lingiga



Teine viis inimesega ühenduse loomiseks on luua ühekordne link. Selleks klõpsake Interface all paremas nurgas oleval pliiatsi ikoonil ja valige seejärel "*Loo ühekordne link*".



Kui teie kontakt on saatnud teile lingi, klõpsake selle skannimiseks või kleepimiseks nupule "*Skaneeri / kleebi link*".



![Image](assets/fr/14.webp)



SimpleX genereerib seejärel ühekordselt kasutatava lingi. Seda saate edastada oma kontaktisikule mis tahes viisil: füüsiline Exchange, muud sõnumid jne.



![Image](assets/fr/15.webp)



Samuti saate valida, millist profiili selle kutselinkiga seostada. Selleks klõpsake oma profiilil kohe QR-koodi all. Seejärel saate:




- valige üks oma olemasolevatest profiilidest (järgmises jaotises näeme, kuidas luua mitu profiili);
- või valida režiim "*Incognito*", mis peidab teie nime ja profiilifoto koos teie korrespondendi juhuslikult genereeritud pseudonüümiga.



Siinkohal valin režiimi "*Incognito*".



![Image](assets/fr/16.webp)



Minu kontakt kasutas linki. Tema omalt poolt ei aktiveerinud režiimi "*Incognito*", mistõttu näen tema profiili nime "*Bob*". Teisalt ei näe Bob minu tegelikku nime "*Loïc Morel*", vaid juhuslikku pseudonüümi, antud juhul "*RealSynergy*".



![Image](assets/fr/17.webp)



Ma võiksin kohe vestlust alustada, kuid kõigepealt tahaksin kontrollida, et ma räägin Bobiga, mitte mõne pahatahtliku isikuga, kes võib olla linki pealtkuulanud või MITM-rünnaku läbi viinud.



Selleks kontrollime meie turvalinki **väljaspool rakendust**. See on oluline, sest MITM-rünnaku korral oleks sisemine kontroll ohus. Seega kasutage mõnda muud turvalist sõnumsüsteemi või veel parem, kontrollige koode isiklikult.



Klõpsake vestluses Bobi fotol ja seejärel "*Kontrollige turvakoodi*". Bob peab sama tegema oma poolel.



![Image](assets/fr/18.webp)



Kui te töötate eemalt, võrrelge koode teises turvalises sõnumsüsteemis (need peavad olema identsed). Või veelgi parem, kui saate kohtuda silmast silma, skaneerige oma kontakti QR-koodi, klõpsates "*Skaneeri kood*".



![Image](assets/fr/19.webp)



Kui kontrollimine on edukas, ilmub teie kontakti nime kõrvale märkega kilbi ikoon. See on teie kinnitus, et te vahetate Bobiga. Kui kontrollimine ei õnnestu, ilmub teade "*Vale turvakood!*".



![Image](assets/fr/20.webp)



Nüüd saate vabalt Exchange sõnumeid, kõnesid ja faile koos Bobiga, sõltuvalt sellest, millised õigused olete selle vestluse jaoks määranud.



## Kohandage oma SimpleXi vestlusprofiile



Üks SimpleXi kõige võimsamaid funktsioone on võimalus hallata mitut täiesti eraldi kasutaja profiili, mis on kõik kättesaadavad samast kohalikust kontost. See võimaldab teil oma erinevaid identiteete kenasti eraldada, ilma et sõnumite haldamine muutuks keerulisemaks.



Näiteks võiksite luua:




- Profiili oma tegeliku nime ja tõelise fotoga oma professionaalsete vahetuste jaoks;
- Profiil oma tegeliku nimega ja naljakas foto oma perekonna vahetamiseks;
- Profiil võltsitud foto ja pseudonüümiga oma isiklike vestluste jaoks;
- Veel üks pseudonüümne profiil võõrastega vestlemiseks.



See on see, mida me siin teeme. Alustan oma põhiprofiili, mis on seotud minu tegeliku identiteediga, seadistamisest. Selleks klõpsan oma profiilifotol paremas alumises nurgas ja seejärel oma kasutajanimel.



![Image](assets/fr/21.webp)



Seejärel klõpsan oma profiilifotol, et seda muuta ja lisada uus foto.



![Image](assets/fr/22.webp)



Teiste profiilide lisamiseks klõpsake menüüs "*Teie vestlusprofiilid*".



![Image](assets/fr/23.webp)



Siin näete kõiki oma profiile. Uue profiili loomiseks klõpsake nupule "*Add profile*".



![Image](assets/fr/24.webp)



Seejärel valige oma uue profiili andmed: nimi, foto jne. Siinkohal kasutan ma pseudonüümi ja teistsugust pilti, et varjata oma tegelikku identiteeti teatavates vahetustes.



![Image](assets/fr/25.webp)



Hoides sõrme profiili allapoole, saate selle varjata. See muudab selle ja kõik sellega seotud vestlused rakenduses nähtamatuks. Te võite ka valida "*Mute*", et lõpetada teavituste saamine.



![Image](assets/fr/26.webp)



Kui olete oma profiilid loonud, saate neid iseseisvalt hallata. Valige avalehelt lihtsalt aktiivne profiil, mida soovite kuvada.



![Image](assets/fr/27.webp)



Kutselinki või staatilise Address loomisel saate nüüd valida, milline profiil sellega seostatakse. Näiteks kui ma valin generate lingi jaoks profiili "*Satoshi Nakamoto*" ja saadan selle Alice'ile, näeb ta ainult minu pseudonüümset identiteeti "*Satoshi Nakamoto*", teadmata kunagi minu tegelikku identiteeti "*Loïc Morel*". Seevastu, kui ma annan talle lingi oma tegelikust profiilist, ei saa ta kuidagi minu pseudonüümsetele profiilidele viidata.



![Image](assets/fr/28.webp)



Palju õnne, nüüd oled kursis SimpleXi sõnumite edastamisega, mis on suurepärane alternatiiv WathsAppile!



Soovitan ka seda teist õpetust, kus ma tutvustan Threema't, mis on veel üks huvitav alternatiiv teie sõnumirakenduse jaoks:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74