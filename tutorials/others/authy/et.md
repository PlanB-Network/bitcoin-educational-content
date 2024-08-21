---
nimi: AUTHY 2FA
kirjeldus: Kuidas kasutada 2FA rakendust?
---
![kaas](assets/cover.webp)

Tänapäeval on kahefaktoriline autentimine (2FA) muutunud hädavajalikuks online-kontode turvalisuse tõstmiseks volitamata juurdepääsu eest. Küberrünnakute sagenemisega on mõnikord ainult parooli kasutamine kontode kaitsmiseks ebapiisav. 2FA tutvustab lisaturvalisuse kihti, nõudes paroolile lisaks teist autentimise vormi. See kinnitamine võib võtta mitmeid vorme, nagu kood, mis saadetakse SMS-i teel, dünaamiline kood, mida genereerib spetsiaalne rakendus, või füüsilise turvavõtme kasutamine. 2FA kasutamine vähendab oluliselt riski, et teie kontod kompromiteeritakse, isegi kui teie parool varastatakse.

## 2FA autentimisrakenduste kaudu

Teistes õpetustes uurime teisi lahendusi nagu füüsilised turvavõtmed, kuid selles tutvustan spetsiifiliselt 2FA rakendusi. Nende rakenduste tööpõhimõte on üsna lihtne: kui 2FA on kontol aktiveeritud, küsitakse iga sisselogimise korral lisaks tavapärasele paroolile ka 6-kohalist koodi. Selle koodi genereerib teie 2FA rakendus. Oluline omadus selle 6-kohalise koodi juures on see, et see ei ole staatiline; rakendus genereerib uue koodi iga 30 sekundi järel.
![AUTHY 2FA](assets/notext/01.webp)
Koodi uuendamine iga 30 sekundi järel muudab ründajale teie kontole juurdepääsu väga raskeks. See süsteem takistab ründajatel varastatud või pealtkuulatud koodi uuesti kasutamast, kuna see aegub kiiresti. Seega, isegi kui ründaja suudab koodi saada, saab ta seda kasutada ainult väga lühikese aja jooksul enne, kui on vaja uut koodi. Lisaks vähendab koodi sagedane muutmine oluliselt aega, mis on häkkeril koodi brute force meetodil ära arvamiseks.

Seega pakuvad autentimisrakendused lihtsat ja tasuta meetodit teie online-kontode turvalisuse oluliseks parandamiseks.

2FA seadistamiseks on palju rakendusi, millest Google Authenticator ja Microsoft Authenticator on kõige tuntumad. Kuid selles õpetuses soovin tutvustada teile teist, vähem tuntud lahendust nimega Authy. Kõik need rakendused kasutavad sama TOTP (*Time based One Time Password*) protokolli, muutes nende kasutamise üsna sarnaseks.
Authy pakub mitmeid eeliseid võrreldes teiste suurte tehnoloogiaettevõtete lahendustega. Esiteks võimaldab see sünkroniseerida teie 2FA tokeneid mitmel seadmel, mis võib olla kasulik telefoni kaotamise või vahetamise korral. Authy võimaldab teil ka genereerida krüpteeritud varukoopia ja salvestada selle veebi, tagades, et te ei kaota kunagi juurdepääsu oma tokenitele, isegi kui kaotate oma peamise seadme. Kasutajaliidese vaatenurgast leian ma isiklikult, et Authy pakub ka meeldivamat ja intuitiivsemat kogemust kui selle alternatiivid.

## Kuidas Authyt installida?

Oma nutitelefonis minge rakenduste poodi (Google Play Store või Apple Store) ja otsige "*Twilio Authy Authenticator*".

- [Apple](https://apps.apple.com/us/app/twilio-authy/id494168017)
- [Android](https://play.google.com/store/apps/details?id=com.authy.authy)
![AUTHY 2FA](assets/notext/02.webp)
Rakenduse esmakordsel käivitamisel peate looma konto. Valige oma riigi suunakood ja oma telefoninumber, seejärel klõpsake "*Submit*".
![AUTHY 2FA](assets/notext/03.webp)
Sisestage oma e-posti aadress koodi taastamiseks.
![AUTHY 2FA](assets/notext/04.webp)
Teie aadressi kinnitamiseks saadetakse teile e-kiri. Sisestage saadud 6-kohaline kood kinnitamiseks. ![AUTHY 2FA](assets/notext/05.webp)
Valige üks kahest saadaolevast meetodist oma telefoninumbri kinnitamiseks. Kui valite SMS-i saamise, sisestage sõnumiga saadud 6-kohaline kood oma numbri kinnitamiseks.
![AUTHY 2FA](assets/notext/06.webp)
Palju õnne, teie Authy konto on loodud!
![AUTHY 2FA](assets/notext/07.webp)
## Kuidas seadistada Authy?

Alustamiseks minge rakenduse seadetesse, klõpsates ekraani paremas ülanurgas asuvatel kolmel väikesel punktil.
![AUTHY 2FA](assets/notext/08.webp)
Seejärel klõpsake "*Settings*" peal.
![AUTHY 2FA](assets/notext/09.webp)
Vahekaardil "*My Account*" on teil võimalus oma kontot muuta. Soovitan lisada rakendusele PIN-koodi, valides "*App Protection*". See lisab teie rakendusele juurdepääsuks täiendava turvakihi.
![AUTHY 2FA](assets/notext/10.webp)
Vahekaardil "*Accounts*" saate seadistada oma tokenite varukoopia. See varukoopia võimaldab teie koode taastada probleemi korral. See on krüpteeritud parooliga, mille peate määrama. On oluline, et see parool oleks tugev ja hoitud turvalises kohas. Selle varukoopia seadistamine ei ole tingimata kohustuslik, kui teil on muid taastamismeetodeid, näiteks teine seade sama Authy kontoga, näiteks.
![AUTHY 2FA](assets/notext/11.webp)Vahekaardil "*Devices*" näete kõiki seadmeid, mis on sünkroniseeritud teie Authy kontoga. Teil on võimalus keelata mitme seadme kasutamine, mis piirab juurdepääsu teie kontole ainult sellele seadmele. Kui kasutate ainult ühte seadet, võib see suurendada teie konto turvalisust, kuid veenduge, et teil on teine varundamismeetod juhuks, kui kaotate selle seadme.

Kui eelistate lubada teiste seadmete lisamist, soovitan teil aktiveerida võimaluse, mis nõuab olemasolevatelt volitatud seadmetelt teie Authy kontol uue seadme lisamise kinnitamist.
![AUTHY 2FA](assets/notext/12.webp)
Uue seadme lisamiseks korrake lihtsalt eelmises osas esitatud installiprotsessi, kasutades samu volitusi. Seejärel palutakse teil kinnitada see uus juurdepääs oma peaseadmest.

## Kuidas seadistada 2FA kontol?

2FA autentimiskoodi seadistamiseks rakenduse, nagu Authy kaudu kontol, peab konto toetama seda funktsiooni. Tänapäeval pakuvad enamik veebiteenuseid seda 2FA võimalust, kuid see ei ole alati nii. Võtame näiteks Protoni meilikonto, mille tutvustasin teises õpetuses:

https://planb.network/tutorials/others/proton-mail
![AUTHY 2FA](assets/notext/13.webp)
Üldiselt leiate selle 2FA võimaluse oma konto seadetest, sageli "*Password*" või "*Security*" jaotise all.
![AUTHY 2FA](assets/notext/14.webp)
Kui aktiveerite selle võimaluse oma Protoni meilikontol, esitatakse teile QR-kood. Seejärel peate skaneerima selle QR-koodi oma Authy rakendusega.
![AUTHY 2FA](assets/notext/15.webp)
Authys klõpsake nuppu "*+*".
![AUTHY 2FA](assets/notext/16.webp)
Klõpsake "*Scan QR Code*". Seejärel skaneerige veebisaidil olev QR-kood.
![AUTHY 2FA](assets/notext/17.webp) Teil on võimalus vajadusel oma kasutajanime muuta. Pärast muudatuste tegemist klõpsake nuppu "*SALVESTA*".
![AUTHY 2FA](assets/notext/18.webp)
Seejärel kuvab Authy teie konkreetse 6-kohalise dünaamilise koodi sellele kontole, mis värskendub iga 30 sekundi järel.
![AUTHY 2FA](assets/notext/19.webp)
Sisestage see kood veebisaidil, et lõpetada 2FA seadistamine.
![AUTHY 2FA](assets/notext/20.webp)
Mõned saidid pakuvad pärast 2FA aktiveerimist ka taastekoodid. Need koodid võimaldavad teil juurdepääsu oma kontole, kui kaotate juurdepääsu oma Authy rakendusele. Soovitan need turvalises kohas hoida.
![AUTHY 2FA](assets/notext/21.webp) Teie konto on nüüd kahefaktorilise autentimisega Authy rakenduse kaudu kaitstud.
![AUTHY 2FA](assets/notext/22.webp)
Iga kord, kui logite kontole sisse, peate esitama Authy poolt genereeritud dünaamilise koodi. Nüüd saate kõik oma kontod selle 2FA meetodiga kaitsta. Uue konto lisamiseks Authys klõpsake rakenduse paremas ülanurgas kolmel väikesel punktil.
![AUTHY 2FA](assets/notext/23.webp)
Seejärel klõpsake "*Lisa konto*".
![AUTHY 2FA](assets/notext/24.webp)
Järgige samu samme nagu esimese konto puhul. Teie erinevad dünaamilised koodid on nähtavad Authy avalehel.