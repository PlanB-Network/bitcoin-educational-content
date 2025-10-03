---
name: StashPay
description: Minimalistički Bitcoin Wallet za svakoga
---

![cover](assets/cover.webp)



Korisničko iskustvo je ključni faktor u usvajanju Bitcoin rešenja širom sveta. Pružanje glatkog, jednostavnog i tehnički neopterećenog iskustva je prioritet za mnoge novčanike i Exchange platforme. U tom pogledu, StashPay se ističe svojim minimalističkim pristupom, dok istovremeno demonstrira moć Lightning Network.



U ovom vodiču ćemo pogledati ovaj portfolio da bismo saznali kako funkcioniše i zašto je idealan za mala preduzeća ili solopreduzetnike.



## Početak sa StashPay



StashPay je Lightning samostalni Wallet prepoznat prvenstveno po minimalističkom, korisnički orijentisanom korisničkom iskustvu. Sa ovim Wallet, ne trebate nikakvo tehničko znanje da biste primili i poslali svoje prve satoshije.



StashPay je projekt otvorenog koda razvijen u React Native-u i ima za cilj da reši problem visokih naknada za transakcije čak i sa transakcijama na glavnom lancu Bitcoin protokola. Dostupan je kao mobilna aplikacija na Android i iOS platformama putem linkova za preuzimanje prisutnih na [veb-sajtu](https://stashpay.me/).



![introduce](assets/fr/01.webp)



Važno je preuzeti Android aplikaciju sa vebsajta, jer nije dostupna na Google Play Store.


Kada se preuzimanje završi, molimo vas da odobrite potrebne dozvole kako biste mogli instalirati aplikaciju na vaš Android telefon.



Jednom kada je aplikacija instalirana, StashPay će kreirati početni Bitcoin Wallet za vas prvi put kada je otvorite. Pre bilo koje transakcije, preporučujemo da napravite rezervnu kopiju ovog Wallet. Ispod ćete pronaći sve naše smernice za osiguravanje da su vaše fraze za oporavak pravilno sačuvane.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Pristupite StashPay podešavanjima klikom na ikonu "Settings", zatim kliknite na opciju **Create backup**. Zatim autorizujte prikaz fraza za oporavak. Nemojte kopirati svoje fraze za oporavak u clipboard telefona, jer mogu biti dostupne drugim prevarantskim aplikacijama instaliranim na vašem mobilnom uređaju.



![backup](assets/fr/02.webp)



Takođe možete povratiti Bitcoin Wallet koji već koristite klikom na opciju **Recover Wallet** i unosom vaših 12 ili 24 reči za oporavak.



### Primite svoje prve satoshije na StashPay



Na početnom ekranu, kliknite na dugme **Primi** i postavite iznos veći od iznosa navedenog crvenom bojom. U našem slučaju, ne možemo primiti manje od 0.11 USD sa StashPay Wallet.



![receive](assets/fr/03.webp)



Kada definišete iznos, možete kliknuti na dugme **Create Invoice**, zatim skenirati ili kopirati Invoice da biste ga poslali pošiljaocu vaših satoshija.



![receive_sats](assets/fr/04.webp)



Istoriju transakcija možete pogledati klikom na ikonu "sat" na početnoj stranici.



![network_fee](assets/fr/05.webp)



Primetićete da ćete morati platiti mrežnu naknadu da biste primili satoshije. Ove naknade će biti oduzete od satoshija koje ćete primiti. To je zato što je StashPay Wallet zasnovan na Breez Development Kit-u. Da biste primili satoshije sa Lightning node-free implementacijom Kita, Breez će naplatiti korisniku (u našem slučaju StashPay) `0.25% + 40 satoshija`. Saznajte više u našem Misty Breez vodiču.



https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Pošalji bitkoine sa StashPay



Slanje bitcoina putem StashPay-a je prilično intuitivno zahvaljujući minimalističkom Interface. Na početnom ekranu, kliknite na dugme **Send**. Skenirajte QR kod ili nalepite Address na koji želite poslati satoshije. StashPay će automatski detektovati Bitcoin protokol lanac na koji želite poslati bitcoine.



![send](assets/fr/06.webp)



Kako je StashPay Wallet zasnovan na Breez Development Kit-u, ima zanimljivu prednost: slanje bitcoina na glavnom lancu po niskoj ceni. Breez koristi Boltz uslugu za obavljanje transakcija između različitih lanaca Bitcoin protokola, omogućavajući korisnicima koji implementiraju Development Kit da koriste ovu uslugu direktno u svojoj aplikaciji.



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Međutim, Breez SDK nameće minimalni iznos pri kojem možete poslati bitkoine na Address na glavnom lancu.



![onchain](assets/fr/07.webp)



Bitkoine možete poslati i koristeći Lightning Address vašeg primaoca. Pregledajte detalje transakcije, a zatim potvrdite klikom na dugme **Send**.



![confirm](assets/fr/08.webp)



## Više konfiguracija



U postavkama StashPay-a, možete prilagoditi konfiguracije kako biste personalizovali korišćenje Wallet.



StashPay vam omogućava da Exchange satoshija na osnovu lokalne valute po vašem izboru. Kliknite na opciju **Valute**, zatim potražite vašu valutu na listi od +113 valuta koje nudi StashPay.



![currencies](assets/fr/09.webp)



U meniju **Receive options** pronaći ćete sva podešavanja za primanje bitkoina sa StashPay. Na primer, izborom opcije **Choose Lightning or Onchain**, omogućite vašem Wallet da prima bitkoine sa glavnog lanca.



![receive-onchain](assets/fr/10.webp)



Opcija **Scan OnChain addresses** omogućava vam da osvežite stanje vašeg Wallet proverom svih UTXO-a (bitcoina koje još niste potrošili) povezanih sa vašim različitim adresama.



![rescan](assets/fr/11.webp)



Meni **Export log** navodi sve radnje infrastrukture Breez i Boltz koje se tiču vaših transakcija i atomskih razmena između različitih Bitcoin protokol lanaca.



![export](assets/fr/12.webp)



Upravo ste se upoznali sa minimalističkim Bitcoin Wallet od StashPay-a. Ako vam je ovaj vodič bio koristan, preporučujemo naš vodič o tome kako započeti sa Bitcoin i zaraditi svoje prve bitkoine.



https://planb.network/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f