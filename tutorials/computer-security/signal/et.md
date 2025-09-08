---
name: Signaal
description: Väljendage end vabalt
---
![cover](assets/cover.webp)



Signal on läbivalt krüpteeritud sõnumirakendus, mis on loodud vaikimisi hea konfidentsiaalsuse tagamiseks. Iga sõnum, kõne ja fail on kaitstud Signal-protokolliga, mida peetakse üheks kõige töökindlamaks sõnumivahetusprotokolliks. Seda kasutavad paljud teised rakendused, sealhulgas WathsApp, Facebook Messenger, Skype ja Google Messages RCS-suhtluseks.



Signal käivitati 2014. aastal Moxie Marlinspike'i (pseudonüüm) poolt ja seda arendab alates 2018. aastast Signal Foundation, mittetulundusühing, mis on loodud Brian Actoni (WhatsAppi kaasasutaja) toetusel.



![Image](assets/fr/01.webp)



Võrreldes WhatsAppiga paistab Signal silma läbipaistvuse poolest: rakenduse kood, nii kliendi- kui ka serveripoolne, on täielikult avatud lähtekoodiga. See võimaldab igaühel seda auditeerida ja eelkõige kontrollida, kas krüpteerimist rakendatakse vastavalt reklaamile.



Signal tugineb siiski telefoninumbri kasutamisele, mis on selle peamine nõrkus anonüümsuse osas võrreldes teiste lahendustega. Sellele vaatamata on see rakendus minu arvates üks kõige usaldusväärsemaid turvalisuse ja konfidentsiaalsuse poolest, tänu oma täiesti avatud arhitektuurile ja laialdaselt vastu võetud krüpteerimisprotokollile, ning seetõttu on seda testitud ja auditeeritud, erinevalt teistest marginaalsematest rakendustest.



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




## Paigaldage rakendus Signal



Signal on saadaval kõigil platvormidel. Rakenduse saate alla laadida otse oma telefoni rakenduste poest:




- [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms);
- [App Store](https://apps.apple.com/us/app/signal-private-messenger/id874139669);



Androidis on võimalik ka [paigaldada APK kaudu](https://github.com/signalapp/Signal-Android/releases).



Selles õpetuses keskendume mobiilsele versioonile, kuid pange tähele, et [ka töölauaversioonid on saadaval](https://signal.org/fr/download/) (MacOS, Linux ja Windows). Enne kui saate oma konto sünkroniseerida töölauaversiooniga, peate siiski kõigepealt seadistama mobiilirakenduse.



## Loo konto Signal'is



Kui käivitate rakenduse esimest korda, klõpsake nupule "*Jätka*".



![Image](assets/fr/02.webp)



Sisestage oma telefoninumber, seejärel klõpsake nuppu "*Järgmine*".



![Image](assets/fr/03.webp)



Kinnituskood saadetakse teile SMS-i teel. Sisestage see kood Signal-rakenduses.



![Image](assets/fr/04.webp)



Valige PIN-kood oma Signaali konto kaitsmiseks. See kood krüpteerib teie andmed ja seda saab kasutada teie kontole juurdepääsu taastamiseks, kui teie seade on kadunud. Seega on oluline valida kindel PIN-kood, mis on võimalikult pikk ja juhuslik, ning hoida selle kohta usaldusväärset arvestust.



![Image](assets/fr/05.webp)



Kinnitage see PIN-kood teist korda.



![Image](assets/fr/06.webp)



Nüüd saate oma kasutajaprofiili isikupärastada. Valige foto, sisestage oma nimi või hüüdnimi. Selles etapis saate määrata ka selle, kes saab teid Signalis teie numbri kaudu üles leida. Valige "*Kõik*", kui soovite olla nähtav, või "*Kellegi*", kui soovite jääda telefoninumbri kaudu jälitamatuks (teid saab siis lisada ainult teie "*Kasutajanime*" abil). Kui olete oma valiku teinud, klõpsake "*Järgmine*".



![Image](assets/fr/07.webp)



Nüüd olete Signaliga ühendatud ja valmis Exchange sõnumeid saatma.



![Image](assets/fr/08.webp)



## Signaali konto seadistamine



Rakenduse seadete avamiseks klõpsake vasakus ülanurgas oma profiilifotol.



![Image](assets/fr/09.webp)



Menüü "*Konto*" võimaldab teil hallata oma profiili seadeid. Soovitan teil säilitada vaikimisi seaded. Samuti saate aktiveerida valiku "*Registreerimislukk*", mis kaitseb teie kontot teatud tüüpi rünnakute eest. See menüü sisaldab ka valikuid, mida vajate oma konto üleviimiseks uude seadmesse.



![Image](assets/fr/10.webp)



Kui klõpsate seadetes uuesti oma profiilipildil, avanevad teie profiili isikupärastamise võimalused. Soovitan määrata "*Kasutajanimi*": see võimaldab teil teiste inimestega ühendust võtta ilma oma telefoninumbrit avaldamata.



![Image](assets/fr/11.webp)



Valides "*QR-kood või link*", saate teabe, mida peate jagama kellegagi, kes soovib teid Signalisse lisada.



![Image](assets/fr/12.webp)



Eriti oluline on menüü "*Privaatsus*". Siit leiate valikud oma numbri nähtavuse kontrollimiseks, sõnumite haldamiseks oma kontaktidega, samuti mitmesugused rakenduses antud volitused.



![Image](assets/fr/13.webp)



Ja uurige julgelt menüüd "*Esildumine*", "*Kõnelused*" ja "*Teavitused*", et kohandada Interface ja rakenduse toimimist vastavalt oma isiklikele vajadustele.



## Ühendage töölauarakendus



Töölauarakenduse ühendamiseks alustage tarkvara installimisega arvutisse (vt selle õpetuse esimest osa). Seejärel minge oma telefonis seadistustesse ja avage jaotis "*Liidetud seadmed*".



![Image](assets/fr/14.webp)



Vajutage nupule "*Uue seadme linkimine*".



![Image](assets/fr/15.webp)



Käivitage arvutis tarkvara, seejärel skannige telefoniga ekraanil kuvatavat QR-koodi. Kui soovite oma vestlusi importida, valige valik "*Sõnumiajaloo ülekandmine*".



![Image](assets/fr/16.webp)



Teie seadmed on nüüd täielikult sünkroonitud.



![Image](assets/fr/17.webp)



## Sõnumite saatmine signaaliga



Selleks, et kellegagi Signalis suhelda, peate esmalt lisama ta kontaktiks. Selleks on mitu võimalust: võite lisada nad nende telefoninumbri kaudu (kui isik on aktiveerinud võimaluse, et teda saaks sel viisil leida) või kasutada nende Signal ID-d.



Klõpsake Interface alumises paremas nurgas oleval pliiatsi ikoonil.



![Image](assets/fr/18.webp)



Minu puhul tahan lisada isiku kasutajanime järgi. Seega klõpsan "*Find by username*".



![Image](assets/fr/19.webp)



Seejärel saate kas kleepida selle sisselogimise või skannida selle QR-koodi.



![Image](assets/fr/20.webp)



Saatke talle sõnum, et luua kontakt.



![Image](assets/fr/21.webp)



Seejärel ilmub vestlus avalehele. Kui isik nõustub teie kontaktitaotlusega, näete tema nime ja profiilifotot.



![Image](assets/fr/22.webp)



Palju õnne, oled nüüd kursis Signal-sõnumite kasutamisega, mis on suurepärane alternatiiv WathsAppile! Kui leidsid selle õpetuse kasulikuks, oleksin väga tänulik, kui jätaksid allpool Green pöidla. Jagage seda õpetust julgelt oma sotsiaalvõrgustikes. Tänan teid väga!



Soovitan ka seda teist õpetust, kus ma tutvustan teile Proton Maili, mis on palju privaatsussõbralikum alternatiiv Gmailile:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2