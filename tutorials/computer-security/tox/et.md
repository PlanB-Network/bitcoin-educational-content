---
name: Tox
description: Avage vestlused ilma vahendajateta detsentraliseeritud Tox-protokollis
---
![cover](assets/cover.webp)



Lõppkrüpteerimine on teenus, mida pakuvad paljud sõnumirakendused, näiteks WhatsApp ja Telegram. Krüpteerimine tähendab siin seda, et enne sõnumi saatja poolt saatmist on see kaitstud krüptograafilise lukuga, mille võti on ainult vastuvõtjal. Täna läheme avastama täiesti detsentraliseeritud, otsast lõpuni krüpteeritud sõnumirakendust, mis põhineb Blockchain-le sarnastel põhimõtetel, et pakkuda turvalist, otsast lõpuni krüpteeritud suhtlust ilma vahendajateta: Tox Chat.



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
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end krüpteerimine*



## Mis on Tox?



Tox on tasuta (avatud lähtekoodiga), detsentraliseeritud sideprotokoll, mis kasutab *Võrgustiku ja krüptograafia raamatukogu* (NaCl) tehnoloogiat ning krüpteerimisalgoritmide kombinatsioone, et tagada kasutajate turvalisus ja konfidentsiaalsus. Tox võimaldab teil Exchange tekstisõnumeid saata, teha heli- ja videokõnesid, jagada faile ja jagada oma ekraani sõpradega turvaliselt, detsentraliseeritult ja ilma vahendajateta.



Tehnoloogia, mida Tox-protokoll kasutab, sarnaneb peer-to-peer-võrkudega, nagu näiteks plokiahelad, mis soodustab protokolli infrastruktuuri detsentraliseerimist. Erinevalt suhtlusvõrgustikest ja läbivalt krüpteeritud sõnumirakendustest on Tox Chat'i rakendus üles ehitatud detsentraliseeritud protokollile, millel puudub keskne server. Kõik kasutajad suhtlevad vahendajatest vabas, tsensuurikindlas peer-to-peer-võrgus. Suhtlemiseks identifitseeritakse iga kasutaja tema avalikust võtmest tuletatud unikaalse ID (ToxID) abil, mis on salvestatud hajutatud Hash tabelis.



## Liitu Toxiga



Tox-protokolli saab kasutada kiirsõnumikliendi kaudu, mille saab alla laadida [Tox Chat'i veebisaidilt](https://tox.chat).



![download](assets/fr/01.webp)



Sõltuvalt teie operatsioonisüsteemist saate alla laadida ja paigaldada Tox-kliendi, mis vastab:





- aTox: [aTox](https://github.com/evilcorpltd/aTox), Kotlini keeles kirjutatud Tox-klient, mis on saadaval ainult Androidis



![aTox](assets/fr/02.webp)





- qTox: Qt raamistikul (C++) põhinev [avatud lähtekoodiga](https://github.com/TokTok/qTox) Tox-klient, mis on saadaval Windowsis, Linuxis, MacOs.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic](https://github.com/JFreegman/toxic) on C keeles kirjutatud Toxi klient, mis töötab käsurea liidesega süsteemides.



![Toxic](assets/fr/04.webp)



Selles õpetuses kasutame suhtlemiseks qToxi kliente Windowsis ja aToxi.



## Alustamine qToxiga



Pärast allalaadimist installige oma Tox-klient ja looge oma profiil.



![qTox-acount](assets/fr/05.webp)



Palju õnne, te olete just liitunud Tox-protokolliga. QToxi tarkvaras leiate oma profiili andmed, kui klõpsate oma kasutajanimele.



![profil](assets/fr/06.webp)



Eelkõige leiad oma Tox ID, mille saad salvestada QR-koodina ja jagada inimestega, kes soovivad sinuga ühendust võtta.



Eksportige oma Tox-profiili fail, et teil oleks oma profiili ja kontaktandmete varukoopia, mida saate kasutada taastamiseks. Vajutage nupule **Eksport** ja valige seejärel oma varukoopia faili tee.



![export](assets/fr/07.webp)



Menüüs **More** saate lisada sõpru, importida kontakte ja hallata saadud sõbrakutseid.



![friends](assets/fr/08.webp)



Minuga saab ühendust näiteks selle Tox ID kaudu: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



Kui sõbrakutse on saadetud, peab saaja teie taotluse vastu võtma või tagasi lükkama, enne kui saate temaga ühendust võtta.



![request](assets/fr/09.webp)



Teie Tox-klient sisaldab kõiki kiirsõnumirakenduste pakutavaid võimalusi:





- Videokõned





- Häälkõned





- Failide jagamine





- emotikonid



![chat](assets/fr/10.webp)



### Vastastikused rühmad



Teie Tox-kliendid võimaldavad teil ka täiesti detsentraliseeritult suhelda rühma inimestega: neid nimetatakse konverentsideks. Looge menüüs **Rühmad** uus konverents või vaadake saadud konverentside kutsete nimekirja.



![conferences](assets/fr/11.webp)



Kui konverents on loodud, saate oma sõpru kutsuda konverentsiga liituma oma Tox-kliendis. Klõpsake oma sõprade nimekirjas paremklõpsuga selle sõbra kasutajanimel, keda soovite kutsuda. Klõpsake valikut **Kutsu konverentsile** ja valige seejärel loodud konverentsi nimi. Võite kutsuda sõbra ka kaudselt konverentsi loomisega, kasutades valikut **Loo uus konverents**.



⚠️ Toxi kliendid on veel arendamisel, seega võib tarkvara kasutamisel tekkida vigu. Konverentside ja videokõnede funktsioonid ei ole Tox Android-kliendis (aTox) veel saadaval.



![invite](assets/fr/12.webp)



### Failiülekanded



Menüüst **Failiülekanded** leiate ajaloo saadetud ja kontaktidelt saadud failidest.



![files](assets/fr/13.webp)



Samuti saate kohandada oma failijagamiskonfiguratsioone iga arutelu jaoks. Tehke paremklõps vastuvõtja kasutajanimel ja valige "Näita rohkem üksikasju".



![details](assets/fr/14.webp)



Interface üksikasjadest saate hallata volitusi, mida annate oma vastuvõtjale:





- Konverentsikutsete automaatne vastuvõtmine.





- Automaatne failide vastuvõtmine.





- Arutelu failide varukoopiate teekonnad.



![permissions](assets/fr/15.webp)



### Rohkem parameetreid



Menüüs **Settings** saate kohandada oma Tox-kliendi seadeid.





- Muuda jaotises **Üldine** oma Tox-kliendi põhikeelt, määra failide varundusteed ja maksimaalne automaatselt aktsepteeritav faili suurus.



![general](assets/fr/16.webp)





- Muuda **Interface kasutaja** sektsioonis oma sõnumite kirjatüüpe ja suurust. Samuti saate muuta oma Tox-kliendi teemat.



![ui](assets/fr/17.webp)





- Vahekaardil **Privaatsus** saate määrata efemeersed sõnumid, eemaldades märkeruudu "Säilitada vestlusajalugu". Samuti saate muuta oma Nospam-koodi, kui märkate, et teid rämpstakse sõbrapäringutega, klõpsates nupul "generate juhuslik NoSpam-kood".



![privacy](assets/fr/18.webp)



### Mis tagab Toxi konfidentsiaalsuse?



Tox-protokoll kasutab detsentraliseeritud Hash tabelit, et luua detsentraliseeritud sõlmedest koosnev võrk. Iga Toxi klient on osa DHT-võrgustikust ja salvestab teavet teiste sõlmede kohta. Toxi puhul salvestab DHT IP-aadressid Toxi avalike võtmetega seotud väärtustena (Tox ID). See muudab Tox-kliendi seadme otsimise lihtsaks, ilma et oleks vaja teha päringuid keskserverist.



Kujutage ette, et kirjutame meie kasutajale `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F`, keda nimetame **kasutaja B**. Teie Tox-klient leiab selle identifikaatori Hash jaotatud tabelist ja hangib sellega seotud IP Address. Kui IP Address on leitud, loob teie Tox-klient otsese, krüpteeritud sidekanali meie **kasutaja B** masinaga või kasutab teisi sõlmi vahendajatena, et jõuda **kasutaja B** juurde. Krüpteerimisalgoritmid tagavad, et olenemata sidekanalist saab teie sõnumi sisu lugeda ainult **Kasutaja B**.



Kui sulle meeldis Toxi avastamine ja saite aru, kuidas see on kasulik teie privaatsuse tugevdamiseks, siis anna sellele õpetusele julgelt pöidlaid üles. Soovitame ka meie õpetust Simple Login'ile, mis võimaldab teil anonüümselt e-kirju vastu võtta ja saata.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41