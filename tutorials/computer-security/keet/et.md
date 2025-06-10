---
name: Keet
description: Peer-to-peer vestlus
---
![cover](assets/cover.webp)



Keet on kiirsõnumirakendus, mis on loodud töötama ilma serveriteta. 2022. aastal Holepunchi (Tetheri ja Bitfinexi rahastatud ettevõte) poolt käivitatud rakendus põhineb täielikult peer-to-peer-võrgul ja pakub radikaalselt detsentraliseeritud lähenemist: sõnumeid, kõnesid ja faile vahetatakse kasutajate vahel otse, ilma vahendajateta.



Keet krüpteerib kogu side lõpuni ja ei küsi mingeid isikuandmeid. Registreerimine on anonüümne, ei nõuta telefoninumbrit ega e-posti aadressi. Lisaks tekstisõnumite vahetamisele pakub Keet väga kvaliteetseid videokõnesid ning piiramatut failide jagamist. Rakendust saab seega kasutada hübriidselt, nii isiklikuks kui ka tööalaseks kasutamiseks.



![Image](assets/fr/01.webp)



Hetkel (aprill 2025) ei ole Keet täielikult avatud lähtekoodiga. Osa lähtekoodist on kättesaadav [Holepunchi GitHubi repositooriumis](https://github.com/holepunchto), eelkõige krüptograafilised ja võrgukomponendid, kuid klient Interface veel mitte. Holepunch on siiski teatanud oma kavatsusest muuta kogu rakendus lõpuks avatud lähtekoodiga. Sõltuvalt sellest, millal te selle õpetuse avastate, võib see olla juba tehtud.




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



## Paigalda Keet



Keet on saadaval kõigil platvormidel. Rakenduse saate alla laadida otse oma telefoni rakenduste poest:




- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);



Androidis on võimalik ka [paigaldada APK kaudu](https://github.com/holepunchto/keet-mobile-releases/releases).



Selles õpetuses keskendume mobiilsele versioonile, kuid palun pange tähele, et [arvutiversioonid on samuti saadaval](https://keet.io/) (MacOS, Linux ja Windows). Samuti on võimalik sünkroonida oma kontot mitmes seadmes.



## Loo konto Keet'is



Esmakordsel käivitamisel võite esitlusekraanidest mööda vaadata.



![Image](assets/fr/02.webp)



Vajutage nupule "*Mina olen uus kasutaja*".



![Image](assets/fr/03.webp)



Nõustuge kasutustingimustega, seejärel klõpsake nupule "*Pikainstallatsioon*".



![Image](assets/fr/04.webp)



Valige nimi või hüüdnimi, seejärel klõpsake nupule "*Seadistuse lõpetamine*".



![Image](assets/fr/05.webp)



Teie profiil on nüüd loodud. Lõplikuks vormistamiseks klõpsake uuesti nuppu "*Finish setup*".



![Image](assets/fr/06.webp)



Saate oma profiili igal ajal kohandada vahekaardil "*Profiil*".



## Salvesta oma Keet konto



Esimene asi, mida oma uue Keet-kontoga teha, on salvestada oma taastumisfraas. See on 24 sõnast koosnev jada, mis võimaldab teil taastada juurdepääsu oma kontole seadme kaotamise või vahetamise korral. See fraas annab täieliku juurdepääsu teie kontole kõigile, kes seda teavad, seega on oluline teha usaldusväärne varukoopia ja seda mitte kunagi avaldada.



Selleks klõpsake Interface paremal allosas oleval vahekaardil "*Profiil*".



![Image](assets/fr/07.webp)



Seejärel avage menüü "*Settings*".



![Image](assets/fr/08.webp)



Valige "*Privaatsus ja turvalisus*".



![Image](assets/fr/09.webp)



Seejärel klõpsake nupule "*Recovery fraas*".



![Image](assets/fr/10.webp)



Vajutage nuppu "*View phrase*", et kuvada oma taastamislauset. Kopeerige see hoolikalt ja hoidke seda turvalises kohas.



![Image](assets/fr/11.webp)



## Sõnumite saatmine Keetiga



Keetis suhtlemiseks peate looma "*Roomid*". Selleks klõpsake Interface paremal ülaosas olevale pliiatsi ikoonile.



![Image](assets/fr/12.webp)



Valige "*Uus grupivestlus*".



![Image](assets/fr/13.webp)



Valige oma "*Ruumile*" nimi ja kirjeldus, seejärel klõpsake "*Loo grupivestlus*".



![Image](assets/fr/14.webp)



Teie "*Ruum*" on nüüd loodud. Osalejate kutsumiseks klõpsake paremal üleval oleval ikoonil "*+*".



![Image](assets/fr/15.webp)



Määrake õigused, mida annate uutele liikmetele kutselinkide kaudu, samuti lingi kehtivuse kestus. Seejärel klõpsake nuppu "*generate kutse*".



![Image](assets/fr/16.webp)



Keet generate lingi, et liituda teie "*Ruumiga*". Saate selle kas kopeerida ja jagada või lasta selle QR-koodi skaneerida inimestel, keda soovite kutsuda.



![Image](assets/fr/17.webp)



Nüüd saate alustada sõnumite ja multimeediafailide vahetamist. Kõne käivitamiseks klõpsake paremas ülemises nurgas oleval telefoni ikoonil.



![Image](assets/fr/18.webp)



Sellest grupist saate saata ka privaatsõnumeid konkreetsele liikmele. Klõpsake grupi profiilipildil ja valige seejärel soovitud liige jaotises "*liikmed*".



![Image](assets/fr/19.webp)



Klõpsake nupule "*Saatke DM-päring*" ja sisestage oma sõnum.



![Image](assets/fr/20.webp)



Kui DM-päring on vastu võetud, leiate selle kontakti kodulehelt, kus saate temaga privaatselt rääkida.



![Image](assets/fr/21.webp)



## Sünkroonige oma kontot mitmes seadmes



Nüüd, kui te teate, kuidas Keeti kasutada ja teil on konto, saate seda sünkroonida ka mõnes teises seadmes, näiteks arvutis. Selleks avage rakendus oma mobiilis, seejärel klõpsake "*Profiil*" ja sisenege "*Settings*".



![Image](assets/fr/22.webp)



Seejärel minge menüüsse "*Minu seadmed*".



![Image](assets/fr/23.webp)



Klõpsake nuppu "*Lisata seade*". Keet generate linki uue seadme sünkroniseerimiseks. Kopeerige see link.



![Image](assets/fr/24.webp)



Paigaldage oma teise seadmesse Keet. Valige avakuval valik "*Mina olen praegune kasutaja*".



![Image](assets/fr/25.webp)



Seejärel klõpsake nupule "*Linki seade*".



![Image](assets/fr/26.webp)



Sisestage esimese seadme poolt antud link, seejärel klõpsake "*Sünkroonimise alustamine*".



![Image](assets/fr/27.webp)



Esimeses seadmes klõpsake ühenduse lubamiseks nuppu "*Kinnitage lingi seadmed*".



![Image](assets/fr/28.webp)



Teises seadmes lõpetage protsess, klõpsates nupule "*Liideseadmete ühendamine*".



![Image](assets/fr/29.webp)



Nüüd saate sellest uuest seadmest juurdepääsu kõigile oma "*Ruumile*" ja vestlustele.



![Image](assets/fr/30.webp)



Palju õnne, oled nüüd kursis Keet-sõnumite kasutamisega, mis on suurepärane alternatiiv WathsAppile! Kui leidsid selle õpetuse kasulikuks, oleksin väga tänulik, kui jätaksid allpool Green pöialt. Jagage seda õpetust julgelt oma sotsiaalvõrgustikes. Tänan teid väga!



Soovitan ka seda teist õpetust, kus ma tutvustan teile Proton Maili, mis on palju privaatsussõbralikum alternatiiv Gmailile :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2