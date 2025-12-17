---
name: BIP-39 Passphrase SeedSigner
description: Kuidas lisada passphrase oma SeedSigneri portfelli?
---

![cover](assets/cover.webp)



passphrase BIP39 on valikuline parool, mis koos mnemoonilise fraasiga annab deterministlike ja hierarhiliste Bitcoin rahakottide jaoks täiendava turvakihi. Selles õpetuses avastame üheskoos, kuidas luua passphrase oma Bitcoin wallet-l, mida kasutatakse koos SeedSigneriga.



![Image](assets/fr/01.webp)



## Eeltingimused enne salasõna lisamist



Enne selle õpetuse alustamist, kui te ei ole kursis passphrase kontseptsiooniga, selle tööpõhimõttega ja selle mõjudega teie Bitcoin wallet-le, soovitan tungivalt tutvuda selle teise teoreetilise artikliga, kus ma selgitan kõike (see on väga oluline, kuna passphrase kasutamine ilma täielikult mõistmata, kuidas see töötab, võib teie bitcoinid ohtu seada) :



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Enne selle õpetuse alustamist veenduge ka, et olete oma SeedSigneri juba initsialiseerinud ja genereerinud oma mnemoonilise fraasi. Kui te ei ole seda teinud ja teie SeedSigner on täiesti uus, järgige Plan ₿ Academy's olevat õpetust. Kui olete selle sammu lõpetanud, võite pöörduda tagasi selle õpetuse juurde:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Kuidas lisada passphrase SeedSignerile?



passphrase lisamine teie SeedSigneri kaudu hallatavasse portfelli loob täiesti uue portfelli, luues täiesti eraldi võtmekomplekti. Järelikult, kui teil on juba portfell, mis sisaldab satss, ei saa te sellele enam passphrase abil ligi, sest see loob täiesti erineva portfelli.



passphrase kohaldamiseks SeedSignerile lülitage seade sisse ja skannige SeedQR-i nagu tavaliselt. SeedSigner kuvab seejärel teie praeguse wallet sõrmejälje, mis vastab sellele, millel puudub passphrase**. wallet koos passphrase-ga omab teistsugust sõrmejälge.



Klõpsake nupul `BIP-39 salasõna`.



![Image](assets/fr/02.webp)



Seejärel sisestage ekraaniklaviatuuri abil etteantud väljale teie valitud passphrase. Tehke kindlasti üks või mitu füüsilist varukoopiat (paberil või metallist): selle passphrase kadumine toob kaasa püsiva juurdepääsu kaotuse teie bitcoinidele. ** wallet taastamiseks on hädavajalikud nii mnemoonika kui ka passphrase ** Kui kumbki neist kaob, blokeeritakse teie bitcoinid pöördumatult.



Kui olete oma sisestuse lõpetanud, kinnitage see, vajutades SeedSigner'i paremal allosas asuvat nuppu "KEY3".



![Image](assets/fr/03.webp)



*Selles näites kasutasin passphrase `pba`. Kuid teie puhul veenduge, et te valite robustse passphrase. Kuidas määrata optimaalne passphrase, leiate sellest teisest artiklist:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

SeedSigner kuvab seejärel teie passphrase wallet uue sõrmejälje. Tehke sellest sõrmejäljest mitu koopiat: see on oluline, kui kasutate wallet koos passphrase-ga, sest see võimaldab teil iga kord passphrase sisestamisel kontrollida, et te ei ole teinud trükivigu ja et te kasutate õiget wallet.



Näiteks, kui ma kirjutan SeedSigneri käivitamisel ekslikult passphrase `Pba` asemel `pba`, siis see lihtne muutus väiketähtedest suurtähtedeks toob kaasa täiesti erineva portfelli loomise kui see, millele ma tahan ligi pääseda.



See sõrmejälg ei ohusta teie wallet turvalisust ega konfidentsiaalsust. See ei avalda teie võtmete kohta mingit avalikku ega privaatset teavet. Seega võite erinevalt mnemoonilisest ja passphrase-st salvestada sõrmejälje digitaalsele andmekandjale. Soovitan hoida koopiat mitmes kohas: paberil, paroolihalduris jne.



Kui olete oma sõrmejälje salvestanud, klõpsake nuppu "Valmis".



![Image](assets/fr/04.webp)



Seejärel on teil juurdepääs kõikidele portfelli funktsioonidele, nagu klassikalise SeedSigneri puhul.



![Image](assets/fr/05.webp)



Nüüd saate importida võtmesalvestuse Sparrow Wallet ja kasutada oma wallet tavapäraselt. Iga kord, kui te taaskäivitate, peate nii oma SeedQR-i skaneerima kui ka passphrase klaviatuuri abil uuesti sisestama, nagu me siin tegime.



Enne wallet ja passphrase tegelikku kasutamist soovitan tungivalt teha täieliku tühja taastamise katse. See võimaldab teil kinnitada, et teie mälulause ja passphrase varukoopiad on kehtivad. Selle kontrolli teostamise kohta saate teavet järgmisest juhendmaterjalist:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895