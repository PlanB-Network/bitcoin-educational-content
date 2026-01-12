---
name: Alby

description: Bitcoin ja Lightning Network brauseripikendus
---

![cover](assets/cover.webp)




Bitcoiniga maksete tegemine üha lihtsamaks on paljude sektori ettevõtete ees seisev väljakutse. Alby paistab silma oma Alby wallet laiendusega brauserite jaoks. Selle laienduse eesmärk on luua sujuv raamistik, mis tuvastab automaatselt aadressid ja võimaldab teha hõõrdumisvabasid bitcoin-makseid. Selles õpetuses avastame Alby laiendust ja testime, kuidas see hõlbustab makseid brauserist.




![video](https://youtu.be/nd5fX2vHuDw)




## Alby laiendus



Alby laiendus on vahend, mis võimaldab teie veebibrauseril hõlpsasti ja turvaliselt suhelda Bitcoin võrgu ja selle Lightning Network kihiga. Seda iseloomustavad kolm aspekti:




- Lightning Network wallet: ühendage oma Alby sõlme või konto, et saata ja vastu võtta bitcoine kiiresti ja odavalt Lightning Network kihi kaudu.
- Sujuvad maksed veebi kaudu: See kaotab vajaduse skannida QR-koode või vahetada bitcoin-maksete jaoks rakendusi veebisaitidel, mis toetavad Lightningut. See võimaldab sujuvaid tehinguid ühe klõpsuga või ilma kinnituseta, kui olete määranud eelarve.
- Nostr juht: Laiendus haldab teie Nostr võtmeid, muutes lihtsaks ühenduse ja suhtlemise Nostr rakendustega, mis tegutsevad turvalise allakirjutajana, ilma et teie privaatne võti oleks avatud igale platvormile.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Ühendage laiendus



Selles õpetuses kasutame Alby laiendust Firefox brauseris Ubuntu operatsioonisüsteemis. Siiski on see saadaval ka Windowsis ja selliste brauserite nagu Chrome puhul.



Alby laienduse saate lisada oma brauserisse, külastades [Firefox] laienduste poodi (https://addons.mozilla.org/fr/firefox/addon/alby/) või [Chrome] laienduste poodi (https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ Oluline on kontrollida, et laienduse autor on tõepoolest ametlik Alby konto, et vältida igasugust piraatlust või teie bitcoinide vargust.



Lisage laiendus oma brauserisse, klõpsates paremal oleval nupul.


Andke vajalikud õigused laienduse paigaldamiseks ja kasutamiseks, seejärel kinnitage laiendus tööriistaribale, et seda oleks lihtne kasutada.



![pin](assets/fr/03.webp)



Samuti peaksite määrama avamiskoodi (väga oluline), mis tagab turvalise juurdepääsu teie Lightning wallet-le teie brauserist. Soovitame määrata tugeva tähtnumbrilise salasõna.



ℹ️ Salvesta see parool turvalisse kohta, et saaksid sellele ligi, kui unustad selle, sest seda saab muuta, kuid ei saa taastada.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby näitab oma kohanemisvõimet, pakkudes teile kahte valikut:




- Jätkake Alby kontoga, kui soovite nautida rakendusi, säilitades samal ajal kontrolli oma bitcoinide üle.
- Ühendage oma wallet või Lightning-sõlm, kui teil on juba olemas laiendusega toetatav sõlmpunkt.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


Selles õpetuses otsustame jätkata Alby kontoga, et kasutada ära Alby ökosüsteemi funktsioone.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Logige sisse oma Alby kontole või looge see, kui teil ei ole veel kontot.



![signup](assets/fr/05.webp)



## Esimeste maksete tegemine



Kui olete sisse loginud, saate tööriistaribal klõpsata Alby laiendil, et pääseda oma portfelli juurde.



![buzzin](assets/fr/06.webp)



Kui olete loonud oma Alby konto, peate selle ühendama wallet-ga, et kulutada satoshisid. Bitcoini wallet ühendamiseks Alby kontoga soovitame kasutada Alby Hub sõlme, mille saate kas oma arvutis sisse seada või tellida Alby pakutava paketi.



![hubplan](assets/fr/13.webp)




Selles õpetuses toetab meie Alby kontot meie masina kohalik paigaldus.


Oma Alby sõlme ehitamiseks soovitame meie Alby Hub õpetust.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

See sõlme võimaldab teil luua isehaldatavaid Lightning-portfelle ja hallata tõhusalt oma Lightning-kanaleid, et saata ja vastu võtta satosid.



![channels](assets/fr/14.webp)



Avatud vastuvõtukanalid, mis määravad kindlaks vastuvõetavate satelliitside koguarvu.



![receivechanal](assets/fr/15.webp)



Avatud saatekanalid, blokeerides satoshid bitcoini onchaini aadressil. Blokeeritud satoshid määravad kogu satoshide summa, mida te saate kulutada.



![spend](assets/fr/16.webp)



Nüüd saate saata ja vastu võtta satoshisid Alby laienduse kaudu.



![exchange](assets/fr/08.webp)



Alates sellest hetkest suudab Alby laiendus tuvastada külastatavatel veebilehtedel saadaval olevad Lightning-aadressid ja -arved ning teeb ettepaneku maksta need bitcoinis või Lightningis otse teie laiendusest.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Taastamisvõtmete kaitsmine koos üldvõtmega



Alby laienduse pakutav peavõti toimib kaitsva kattekihina, mis võimaldab teil turvaliselt suhelda peamise Bitcoin võrgukihiga (Onchain), Nostr süsteemiga ja aktiveerida Lightning-ühenduse Nostr rakendustega.



![masterKey](assets/fr/11.webp)



See põhivõti koosneb 12 sõnast, mis on sarnased teie taastumisfraasiga. Seetõttu soovitame seda turvaliste meetodite abil säilitada, et tagada selle kättesaadavus igal ajal.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Alby laiendusega saate nüüd kogeda bitcoini ja Lightning-makseid ilma hõõrdumisteta. Kui teile meeldis see õpetus, siis soovitame meie Alby Hub õpetust, et luua oma Alby sõlme ja kontrollida kõiki Alby rahakoti aspekte sujuva ja võimsa kasutajaliidese kaudu.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a