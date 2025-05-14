---
name: Misty Breez
description: Vibuta Lightning Wallet.
---

![misty-breez-cover](assets/cover.webp)



Misty Breez on Lightning isemajandav Wallet, mille Breez on välja töötanud oma tarkvara arenduskomplekti ja BlockStreami välja töötatud **Liquid** võrgu põhjal.


Sellega kaasneb täiesti uus lähenemisviis ilma välgumihkliksõlmedeta töötamisele: potentsiaalne **PELIMÄNGU** Bitcoin võrkudevahelistes ülekannetes.


Selles õpetuses kirjeldame, kuidas see portfell töötab, ja anname teile täieliku ülevaate.



## Kuidas Misty Breez töötab?



Misty Breez on rakendus ilma Lightning node'ita backendina. See on välja töötatud Breez SDK ja Liquid põhjal.



Liquid on Bitcoin võrguga paralleelne Layer, mis pakub märkimisväärset kiiruse ja tehingukulude parandamist. See Layer võimaldab Misty Breezil loobuda Lightning-sõlmest ja kasutada selle asemel kolmanda osapoole Exchange teenuseid, näiteks **Boltz**, et tagada Liquid Network ja Lightning Network koostalitlusvõime. Ärge kiirustage, me tuleme selle juurde tagasi.



Alustame oma seiklust Misty Breez Wallet-ga.



## Alustamine Misty Breeziga



Misty Breezi mobiilirakendus on saadaval ametlikel allalaadimisplatvormidel, nagu Google Play Store (Androidil) ja Apple Store (iOSil). Samuti saab õigesse rakendusse suunata ametlikul [Misty Breez] veebisaidil (https://breez.technology/misty/).



⚠️ Veenduge, et te ei aja Misty Breez'i ja Breez Wallet segamini.



⚠️ **OLULINE**: Teie bitcoinide turvalisuse tagamiseks on oluline laadida rakendus alla ametlikelt platvormidelt, et tagada selle autentsus.



![download-misty-breez](assets/fr/01.webp)



Selles õpetuses alustame Androidi seadmest. Sellegipoolest kehtivad kõik selles jaotises kirjeldatud sammud ja eriomadused ka iOS-i puhul.



Misty Breez annab teile pärast installimist võimaluse luua uus Wallet või taastada vana Lightning Wallet, mille taastamissõnad on teil olemas.


Selles õpetuses valime uue portfelli loomise.



⚠️Misty Breez on praegu arendusfaasis, seega soovitame alustada mõistlike kogustega.



![create-wallet](assets/fr/02.webp)


### Salvesta oma taastamise sõnad :


Üks esimesi asju, mida peaksite uue portfelli loomisel tegema, on varundada oma 12 taastussõna.


Siin on mõned näpunäited, kuidas varundada oma varunduslauset.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Oma lausete varundamiseks valige menüü **Eelistused > Turvalisus** ja seejärel valik **Kontrollige oma lausete varundamist**.



![backup](assets/fr/03.webp)


Lisaturvalisuse tagamiseks saate ka **luua PIN-koodi**, et autentida juurdepääsu oma Wallet-le.




Leia oma kohalik valuuta Misty Breez'i poolt aktsepteeritavate valuutade hulgast. Konfigureerige oma valuuta menüüst **Eelistused > Fiat Valuutad**, seejärel valige soovitud valuuta või valuutad.



![devises](assets/fr/04.webp)



### Esimeste tehingute tegemine


Kui te olete juba tuttav Breezi portfelliga, siis Misty Breezi intuitiivne Interface ei heiduta teid üldse.



Interface **Saldo** menüüs klõpsake valikut **Võta vastu**, et luua arveid oma bitcoinide vastuvõtmiseks Wallet-sse.



⚠️ Misty Breez palub teil aktiveerida rakenduse teavitused telefoni seadetes, et teil oleks õigus saada Lightning Address.



Misty Breeziga saate :




- Saate bitcoin'e Lightning Network-l alates **100 satoshist** kuni **25 000 000 satoshini**.
- Saada bitcoin'e Bitcoin põhivõrgus alates **25 000 satoshist**.



![transactions](assets/fr/05.webp)



Siit algab Misty Breez'i maagia.


Erinevalt Breez Wallet-st, mis annab teile välgussõlme ja palub teil ise katta maksekanalite avamise ja sulgemise kulud, ei palu Misty Breez teil midagi teha. Nagu varem mainitud, ei tööta Misty Breez isegi Lightning-sõlme alusel.



Vaatame lähemalt kulisside taha.



Tegelikkuses on teil Liquid portfell, mis on seotud teie Misty Breez'i portfelliga. Loogiliselt käsitlete L-BTC-d (Liquid Bitcoin) fikseeritud kursiga, mis on seotud kolmanda osapoole allveesatoshi konverteerimisteenustega, mis võimaldavad teil Lightning Network-ga koostööd teha.



Kui saate makse oma Misty Breez Wallet, saatja saadab teile satoshis, mis läheb läbi konverteerimisteenuse nagu Boltz (mida praegu kasutab Misty Breez), et konverteerida saadetud satoshis L-BTC-ks, mis saadetakse teie Misty Breez Wallet (seotud Liquid Wallet).


Siin on lihtsustatud skeem protsessi kulisside taga.



![lnswap-in](assets/fr/06.webp)



Klõpsake menüüs **Saldo** Interface, klõpsake välgumaksu Invoice maksmiseks valikut **Saatmine**.


Maksmiseks sisestage Lightning Invoice, teie saaja Lightning Address või skannige lihtsalt Invoice-l olev QR-kood.



![send-bitcoins](assets/fr/07.webp)



Kulisside taga lubate oma Misty Breez Wallet-ga seotud Liquid Wallet-l konverteerida L-BTC ekvivalendi satoshideks Boltzi kaudu, seejärel kannate need satoshid üle oma vastuvõtja Lightning Wallet-le (mis on olemas Lightning Network-l).



![send-bitcoin-bts](assets/fr/08.webp)



See Misty Breez'i infrastruktuuri funktsioon võimaldab kasutajatel teha tehinguid ka siis, kui Misty Breez on võrguühenduseta.



Kogenumate jaoks on olemas ka menüü **Preferences > Developers**, mis annab teile veidi rohkem üksikasju :




- Breez tarkvara arenduskomplekti versioon.
- Teie Misty Breez Wallet avalik võti.
- Laenuvõtja, esmane avalikust võtmest tuletatud unikaalne identifikaator.
- Teie portfelli saldo.
- Vihje Liquid, väikeste L-BTC summade saatmiseks.
- Bitcoin Tip, väikeste koguste Bitcoin saatmiseks.



Samuti saate teostada teatud toiminguid, näiteks sünkroonida Liquid Network-ga, varundada oma võtmeid, jagada oma tegevuslogi ja valida Liquid Network uuesti skaneerimise.



![dev-mode](assets/fr/09.webp)


Palju õnne! Nüüd on teil hea ülevaade Misty Breez'i portfellist ja selle panusest Bitcoin võrkudevahelistesse tehingutesse. Kui see õpetus oli teie jaoks kasulik, andke meile Green pöialt. Meil oleks hea meel kuulda sinust.



Et minna kaugemale, soovitan teil avastada ka meie õpetust Aqua Wallet kohta, mis töötab sarnaselt Misty Breeziga :



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125