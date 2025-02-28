---
name: Lipa
description: Lipa lightning mobiilse rahakoti seadistamine ja kasutamine
---
![cover](assets/cover.webp)

Bitcoin Lightning rahakott on mobiilirakendus, mis võimaldab koheseid ja odavaid tehinguid Bitcoini Lightning-võrgus. Erinevalt peamise plokiahelaga (on-chain) tehtavatest tehingutest on Lightning-maksed peaaegu kohesed ja nõuavad minimaalseid tasusid, mistõttu sobivad need eriti hästi väikesteks igapäevasteks makseteks.

Lightning rahakotte, nagu kõiki mobiilseid rahakotte, peetakse "kuumaks" rahakotiks, sest need on ühendatud internetti. Seetõttu on need eelkõige mõeldud väikeste rahasummade haldamiseks igapäevaste kulutuste tegemiseks. Suuremate summade jaoks on soovitav kasutada turvalisemat hoiustamislahendust, näiteks riistvaralist rahakotti.

Kui soovite rohkem teada saada Lightning-võrgustikust ja mõista, kuidas see tehniliselt toimib, siis soovitan teil läbida selle kursuse:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
Selles õpetuses vaatame **Lipa**, lihtsat ja tõhusat Lightning rahakotti, mis on välja töötatud Šveitsis.

## Tutvustame Lipa

Lipa on mittekasutatav Lightning rahakott, mida iseloomustab selle lihtne kasutamine ja lihtsa kasutajaliides. Šveitsi meeskonna poolt välja töötatud Lipa rõhutab konfidentsiaalsust ja kasutusmugavust algajatele.

Peamised omadused on järgmised:


- Intuitiivne kasutajaliides
- Autonoomne Lightning-kanali haldamine
- LNURL-protokolli tugi
- Võimalus osta bitcoine otse rakenduses

## Lipa paigaldamine ja konfigureerimine

Esimene samm on Lipa rakenduse allalaadimine. Hetkel on see saadaval ainult iOS-i jaoks:


- [Apple'ile](https://apps.apple.com/app/lipa-bitcoin-lightning/id1602180066)

Androidi versioon on praegu arendamisel ja on peagi saadaval.

![Installation de Lipa](assets/fr/01.webp)

Kui olete rakenduse käivitanud, jõuate avakuvale, mis pakub teile kaks võimalust:


- Uue portfelli loomine
- Olemasoleva portfelli taastamine varukoopiast

Kui olete valinud oma valiku, palub rakendus teil teateid lubada. See samm on oluline, sest teavitused on vajalikud :


- Saate teateid maksete laekumisest, isegi kui rakendus on suletud
- Olla kursis bitcoini ostmisega seotud sammudega nende integreeritud lahenduse kaudu

Seejärel tutvustab rakendus oma põhifunktsioone mitme sissejuhatava ekraani kaudu:


- Saamatu maksekviitung**: Kasutajad saavad Bitcoin-makseid vastu võtta isegi siis, kui rakendus on suletud, tagades usaldusväärsuse ja mugavuse.
- Mittehooldusõiguslikud välguaadressid**: Lipa toetab nüüd ka mittekaitstavaid Lightning-aadresse, mis suurendab privaatsust ja turvalisust, andes kasutajatele täieliku kontrolli oma bitcoinide üle.
- Kontroll analüütiliste andmete üle** : Kuna läbipaistvus ja konfidentsiaalsus on esmatähtsad, saavad kasutajad vaadata kogutud andmete tüüpe ja valida oma jagamise eelistusi.
- Saatke telefoninumbri** kaudu: Lihtsalt valige kontakt, sisestage summa ja saatke bitcoinid otse tema telefoninumbrile.

Rakendust täiustatakse pidevalt stabiilsuse, turvalisuse ja töökindluse osas, et tagada optimaalne kasutajakogemus.

## Rakenduse navigeerimine

Lipa kasutajaliides on korraldatud 4 peamise vahekaardi ümber, millele pääseb ligi ekraani allosas asuva navigatsiooniriba kaudu:

![Navigation principale](assets/fr/02.webp)


- Kodu**: Näitab teie jooksvat saldot ja tehinguajalugu
- Skanner**: Võimaldab maksete tegemiseks skaneerida QR-koode
- Kaart**: Kuvab interaktiivse kaardi Bitcoini aktsepteerivatest ettevõtetest teie piirkonnas
- Seaded**: Juurdepääs rakenduse seadetele, varundamisele ja eelistustele

Täiendavasse menüüsse pääseb, kui tõmmata avakuva alla:

![Menu supplémentaire](assets/fr/03.webp)

See žest paljastab lisafunktsioone, nagu :


- Bitcoinide ostmine
- On-chain bitcoini hoiustamine
- Lightning-arvete loomine bitcoinide saamiseks
- Välkarvete maksmine

## Salvestage oma portfell

Rahakoti varundamiseks minge vahekaardile "Seaded" ja valige "Recovery fraas". Lipa kasutab taastamislauset, mis tuleb kindlasti hoolikalt füüsilisele kandjale (paber, metall) üles kirjutada. See fraas on ainus viis oma raha taastamiseks, kui telefon on kadunud või varastatud. Varundamise kinnitamiseks palub rakendus teil kinnitada 3 juhuslikku sõna teie fraasist.

![Backup](assets/fr/04.webp)

Lisateavet selle kohta, kuidas korralikult varundada ja hallata oma taastamislauset, soovitan kindlasti jälgida seda teist õpetust, eriti kui olete algaja:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
## Bitcoinide vastuvõtmine

Bitcoinide saamiseks on teil kaks võimalust. Nendele valikutele juurdepääsuks minge tagasi avakuvale ja tõmmake ekraani allapoole. Seejärel saate kas :


- Valige "Transfer BTC", et saada bitcoine ahelas. Seejärel skaneerige lihtsalt QR-koodi oma teise rahakotiga ja viige tehing lõpule.
- Valige Lightning-võrgu kaudu saamiseks "Taotlus" ja sisestage summa, mida soovite saada.

Mõlemal juhul peate maksma tasu, mis on võrdne 0,4% summast või umbes 2500 sati, kui taotlus peab avama uue maksekanali (mis on paratamatult esimese makse puhul).

![Recevoir des bitcoins on chain](assets/fr/05.webp)

![Recevoir des bitcoins lightning](assets/fr/06.webp)

## Bitcoinide saatmine

Bitcoinide saatmiseks mine avakuvale, tõmba ekraan alla ja vali "Pay". Seejärel lihtsalt kas :


- sisestage välk LNURL aadress
- skannige makse tegemiseks välk QR-koodi.

Saate ka minna ekraani allosas olevale teisele vahekaardile, et skannida QR-koodi otse.

![Envoi de bitcoins](assets/fr/07.webp)

## Osta bitcoine

Lipa pakub võimalust osta bitcoine otse rakenduses 1,5%-lise tasu eest. Ostu sooritamiseks minge avakuvale ja tõmmake menüü kuvamiseks alla. Seejärel valige "Osta BTC". Kolm sissejuhatavat ekraani juhatavad teid ostuprotsessi läbi.

![Menu d'achat](assets/fr/08.webp)

Seejärel sisestage lihtsalt selle konto pangaandmed, mida kasutate ostu sooritamiseks. Valige oma valuuta ja sisestage oma e-posti aadress.

Pärast laadimisekraani leiate viitenumbri, mis tuleb lisada tehtava ülekande juurde, ning pangaandmed vahetuseks.

![Sélection du montant](assets/fr/09.webp)

Kõik, mida peate tegema, on soovitud summa ülekandmiseks kasutada oma panka, seadistada ülekanne, märkides eelnevalt välja otsitud RIB ja näidata tehingu ajal viide, et Lipa saaks seostada selle pangaliigutuse teie Lipa rahakotiga.

![Confirmation d'achat](assets/fr/10.webp)

## Eelised ja puudused

### Eelised


- Intuitiivne kasutajaliides
- Korrektsed teenustasud
- Mittekaitsenõukogu
- Integreeritud bitcoini ostulahendus
- BTCmap integratsioon
- NFC-tugi

### Puudused


- Bitcoine ei ole võimalik saata ahelas
- Keskmisest veidi pikem makse

Lipa on suurepärane valik Lightning Networkiga alustamiseks, mis sobib eriti hästi kasutajatele, kes otsivad lihtsat lahendust igapäevasteks makseteks. Tänu lihtsale kasutusmugavusele ja lihtsale kasutajaliidesele on see ideaalne rahakott algajatele, pakkudes samal ajal olulisi funktsioone igapäevaseks Lightningi kasutamiseks.

## Ressursid


- [Lipa ametlik kodulehekülg](https://lipa.swiss/)
- [Lipa toetus](https://getlipa.atlassian.net/servicedesk/customer/portal/1)