---
name: BIP-39 passphrase SeedSigner
description: Kuidas lisada passphrase oma SeedSigneri portfelli?
---

![cover](assets/cover.webp)



passphrase BIP39 on valikuline parool, mis koos Mnemonic fraasiga annab deterministlike ja hierarhiliste Bitcoin rahakottide jaoks täiendava Layer turvalisuse. Selles õpetuses avastame koos, kuidas luua passphrase oma Bitcoin Wallet, mida kasutatakse koos SeedSigneriga.



![Image](assets/fr/01.webp)



## Eeltingimused enne passphrase lisamist



Enne selle õpetuse alustamist, kui te ei ole kursis passphrase kontseptsiooniga, selle toimimisega ja selle mõjudega teie Bitcoin Wallet-le, soovitan tungivalt tutvuda selle teise teoreetilise artikliga, kus ma selgitan kõike (see on väga oluline, kuna passphrase kasutamine ilma täielikult mõistmata, kuidas see töötab, võib teie bitcoinid ohtu seada) :



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Enne selle õpetuse alustamist veenduge, et olete juba initsialiseerinud oma SeedSigneri ja genereerinud Mnemonic fraasi. Kui te ei ole seda teinud ja teie SeedSigner on täiesti uus, järgige Plan ₿ Academy's olevat õpetust. Kui olete selle sammu lõpetanud, võite pöörduda tagasi selle õpetuse juurde:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Kuidas lisada passphrase SeedSignerile?



passphrase lisamine teie SeedSigneri kaudu hallatavasse portfelli loob täiesti uue portfelli, luues täiesti eraldi võtmekomplekti. Järelikult, kui teil on juba portfell, mis sisaldab Satss, ei saa te sellele enam passphrase abil ligi, sest see loob täiesti erineva portfelli.



passphrase kohaldamiseks SeedSignerile lülitage seade sisse ja skannige SeedQR-i nagu tavaliselt. SeedSigner kuvab seejärel teie praeguse Wallet sõrmejälje, mis vastab sellele, millel puudub passphrase**. Wallet koos passphrase-ga omab teistsugust sõrmejälge.



Klõpsake nupule "BIP-39 passphrase".



![Image](assets/fr/02.webp)



Seejärel sisestage ekraaniklaviatuuri abil etteantud väljale teie valitud passphrase. Tehke kindlasti üks või mitu füüsilist varukoopiat (paber või metall): selle passphrase kadumine toob kaasa püsiva juurdepääsu kaotuse teie bitcoinidele. ** Wallet taastamiseks on hädavajalikud nii Mnemonic kui ka passphrase ** Kui kumbki neist kaob, blokeeritakse teie bitcoinid pöördumatult.



Kui olete oma sisestuse lõpetanud, kinnitage see, vajutades SeedSigner'i paremal allosas asuvat nuppu "KEY3".



![Image](assets/fr/03.webp)



*Selles näites kasutasin passphrase `pba`. Kuid teie puhul veenduge, et te valite robustse passphrase. Optimaalse passphrase määratlemise kohta saate teavet selles teises artiklis:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

SeedSigner kuvab seejärel teie passphrase Wallet uue sõrmejälje. Tehke sellest sõrmejäljest mitu koopiat: see on oluline, kui kasutate Wallet koos passphrase-ga, sest see võimaldab teil iga kord passphrase sisestamisel kontrollida, et te ei ole teinud trükivigu ja et pääsete ligi õigele Wallet-le.



Näiteks, kui ma kirjutan SeedSigneri käivitamisel passphrase `Pba` ekslikult üles `pba` asemel, siis see lihtne muutus väiketähtedest suurtähtedeks toob kaasa täiesti erineva portfelli loomise kui see, millele ma soovin ligi pääseda.



See sõrmejälg ei ohusta teie Wallet turvalisust ega konfidentsiaalsust. See ei avalda teie võtmete kohta mingit avalikku ega privaatset teavet. Erinevalt Mnemonic-st ja passphrase-st saate sõrmejälje salvestada digitaalsele andmekandjale. Soovitan hoida koopiat mitmes kohas: paberil, paroolihalduris jne.



Kui olete oma sõrmejälje salvestanud, klõpsake nuppu "Valmis".



![Image](assets/fr/04.webp)



Seejärel on teil juurdepääs kõikidele portfelli funktsioonidele, nagu klassikalise SeedSigneri puhul.



![Image](assets/fr/05.webp)



Nüüd saate importida võtmesalvestuse Sparrow wallet-i ja kasutada Wallet-i tavapäraselt. Iga kord, kui te taaskäivitate, peate nii oma SeedQR-i skaneerima kui ka passphrase uuesti sisestama, kasutades klaviatuuri, nagu me siin tegime.



Enne Wallet ja passphrase tegelikku kasutamist soovitan tungivalt teha täieliku tühja taastamise katse. See võimaldab teil kinnitada, et teie Mnemonic fraas ja passphrase varukoopiad on kehtivad. Selle kontrolli teostamise kohta saate teavet järgmisest juhendmaterjalist:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895