---
name: BIP-39 Passphrase Trezor
description: Kuidas lisada passphrase oma Trezori portfelli?
---
![cover](assets/cover.webp)



passphrase BIP39 on valikuline parool, mis koos Mnemonic fraasiga annab täiendava Layer turvalisuse deterministlike ja hierarhiliste Bitcoin portfellide jaoks. Selles õpetuses avastame koos, kuidas luua passphrase oma turvalise Bitcoin Wallet Trezoril (Safe 3, Safe 5 ja Model One).



![Image](assets/fr/01.webp)



Enne selle õpetuse alustamist, kui te ei ole kursis passphrase kontseptsiooniga, kuidas see töötab ja selle mõju teie Bitcoin Wallet-le, soovitan tungivalt tutvuda selle teise teoreetilise artikliga, kus ma selgitan kõike (see on väga oluline, kuna passphrase kasutamine ilma täielikult mõistmata, kuidas see töötab, võib teie bitcoinid ohtu seada) :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase on Trezoril käsitletud klassikaliselt, kui olete seadistamise ajal valinud BIP39 standardi (mida ma soovitan, kui te ei vaja *Multi-share Backup*). Trezori eripära on see, et passphrase saab sisestada kas otse Hardware Wallet või arvuti klaviatuuri kaudu, kasutades Trezor Suite'i tarkvara. See teine võimalus on tunduvalt vähem turvaline, kuna arvutil on tohutult suurem ründepind kui Hardware Wallet-l. Siiski võib keerulise passphrase sisestamine olla tavaklaviatuuril kiirem kui Hardware Wallet-l, mis võib soodustada tugevate salasõnade kasutamist. Seega on alati parem kasutada passphrase, isegi kui seda tuleb tippida, kui üldse mitte kasutada. Oluline on siiski olla teadlik sellest, et sellega kaasneb suurenenud numbriliste rünnakute oht.



Need valikud ei ole saadaval kõigis Trezoriga ühilduvates portfellihaldustarkvarades. Näiteks Model One'i puhul saab passphrase sisestada Sparrow Wallet klaviatuuri kaudu. Model T, Safe 3 ja Safe 5 mudelite puhul tuleb kas kasutada Trezor Suite'i või sisestada passphrase otse Hardware Wallet-s, kuna HWI lülitas Sparrow kaudu sisestamise võimaluse mõned aastad tagasi välja.



![Image](assets/fr/02.webp)



Trezor Suite'is on teil kaks erinevat võimalust passphrase nõudluse haldamiseks. Saate aktiveerida vahekaardil "*Gevus*" valiku "*passphrase*". Kui see on aktiveeritud, küsivad Trezor Suite ja kõik teised portfellihaldustarkvarad teil süstemaatiliselt iga kord käivitamisel passphrase sisestamist. Kui eelistate passphrase kasutamisel diskreetsemat lähenemist, võite jätta seadistuse "*Standard*". Sellisel juhul peate käsitsi sisenema oma Hardware Wallet menüüsse vasakus ülanurgas ja klõpsama iga kord käivitamisel nupule "*+ passphrase*".



Enne selle õpetuse alustamist veenduge, et olete oma Trezori juba initsialiseerinud ja Mnemonic fraasi genereerinud. Kui te ei ole seda teinud ja teie Trezor on uus, järgige Plan ₿ Network kohta kättesaadavat mudelispetsiifilist õpetust. Kui olete selle sammu lõpetanud, võite selle õpetuse juurde tagasi pöörduda.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## passphrase lisamine Safe 3-le või Safe 5-le



Kui olete loonud oma Wallet, salvestanud Mnemonic ja määranud PIN-koodi, jõuate Trezor Suite'i avalehele. Vasakusse ülemisse nurka peaks ilmuma aken, mis kutsub teid üles passphrase BIP39 aktiveerima.



![Image](assets/fr/03.webp)



Kui see aken ei ilmu, tuleb teil käsitsi aktiveerida valik "*passphrase*" vahekaardil "*Seade*" seaded.



![Image](assets/fr/04.webp)



Selles aknas palutakse teil sisestada oma passphrase. Valige tugev passphrase ja tehke kohe füüsiline varukoopia, näiteks paberile või metallile. Selles näites valisin passphrase: `fH3&kL@9mP#2sD5qR!82`. See on näide; soovitan siiski valida veidi pikema passphrase. Ideaalne oleks 30-40 tähemärki (nagu hea parool).



loomulikult ei tohiks te kunagi oma passphrase internetis jagada, nagu ma seda käesolevas õpetuses teen. Seda näidis Wallet kasutatakse ainult Testnet peal ja see kustutatakse õpetuse lõpus.



Konkreetsemaid soovitusi passphrase valimiseks palun veel kord tutvuda selle teise artikliga:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Kui soovite sisestada oma passphrase arvuti klaviatuuri kaudu, sisestage see ettenähtud väljale ja klõpsake seejärel "*Access passphrase Wallet*".



![Image](assets/fr/05.webp)



Seejärel kuvab teie Hardware Wallet teie passphrase. Veenduge, et see vastab teie füüsilisele varukoopiale (paber või metall), enne kui klõpsate ekraanil jätkamiseks.



![Image](assets/fr/06.webp)



See annab teile juurdepääsu teie passphrase-ga kaitstud portfellile.



![Image](assets/fr/07.webp)



Kui eelistate suurendada turvalisust, sisestades passphrase ainult Trezorile, klõpsake küsimisel "*Enter passphrase on Trezor*".



![Image](assets/fr/08.webp)



Trezorile ilmub T9-klaviatuur, mis võimaldab teil sisestada passphrase. Kui olete oma sisestuse lõpetanud, klõpsake Green märkele, et rakendada passphrase teie Wallet-le.



![Image](assets/fr/09.webp)



Seejärel on teil juurdepääs oma passphrase turvalisele Wallet-le.



![Image](assets/fr/10.webp)



Sparrow Wallet kasutamiseks on protseduur sarnane, kuid mudelite T, Safe 3 ja Safe 5 puhul tuleb passphrase sisestada Hardware Wallet, mitte arvuti klaviatuuri kaudu.



Kui Sparrow Wallet nõuab juurdepääsu teie Trezorile ja passphrase ei ole pärast viimast käivitamist veel rakendatud, peate selle sisestama T9-klaviatuuri abil.



![Image](assets/fr/11.webp)



## passphrase lisamine Model One'ile



Model One'i puhul on passphrase BIP39 kasutamine peaaegu hädavajalik. Kuna see seade ei sisalda turvalist elementi, on tundliku teabe väljavõtmine suhteliselt lihtne. Seetõttu ei ole see füüsilise rünnaku suhtes vastupidav. Kuna aga passphrase ei jää pärast seadme väljalülitamist seadmesse, võib tugeva (mitte-bruteeritava) passphrase kasutamine kaitsta teid selle mudeli puhul enamiku teadaolevate füüsiliste rünnakute eest.



Model One'i puhul ei ole võimalik sisestada passphrase otse Hardware Wallet-i. Te peate selle sisestama arvuti klaviatuuri kaudu.



Kui olete loonud oma Wallet, salvestanud Mnemonic ja määranud PIN-koodi, jõuate Trezor Suite'i avalehele. Vasakusse ülemisse nurka peaks ilmuma aken, mis kutsub teid üles passphrase BIP39 aktiveerima.



![Image](assets/fr/12.webp)



Kui see aken ei ilmu, peate seadete vahekaardil "*Seade*" aktiveerima valiku "*passphrase*".



![Image](assets/fr/13.webp)



Selles aknas palutakse teil sisestada oma passphrase. Valige tugev passphrase ja tehke kohe füüsiline varukoopia, näiteks paberile või metallile. Selles näites valisin passphrase: `fH3&kL@9mP#2sD5qR!82`. See on vaid näide; soovitan siiski valida veidi pikema passphrase. Ideaalne oleks 30-40 tähemärki (nagu hea parool).



Konkreetsemaid soovitusi passphrase valimiseks palun veel kord tutvuda selle teise artikliga:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Sisestage oma passphrase ettenähtud väljale, seejärel klõpsake nupule "*Access passphrase Wallet*".



![Image](assets/fr/14.webp)



Teie Hardware Wallet kuvab teie passphrase. Veenduge, et see vastab teie füüsilisele varukoopiale (paber või metall), seejärel klõpsake jätkamiseks paremal nupul.



![Image](assets/fr/15.webp)



See viib teid passphrase-ga kaitstud portfelli.



![Image](assets/fr/16.webp)



Sparrow Wallet kasutamiseks jääb protseduur samaks. Iga kord, kui Sparrow vajab juurdepääsu teie Hardware Wallet-le ja passphrase ei ole pärast seadme viimast käivitamist sisestatud, peate selle sisestama.



![Image](assets/fr/17.webp)



Palju õnne, te olete nüüd kursis passphrase BIP39 kasutamisega Trezori riistvara rahakottidel. Kui soovid Wallet turvalisust veelgi edasi viia, vaata seda Trezori *Multi-share* varundussüsteemide (*Shamir's Secret Sharing Scheme*) õpetust:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Kui leidsite selle õpetuse kasulikuks, oleksin tänulik, kui jätaksite allpool Green pöidla. Jagage seda artiklit julgelt oma suhtlusvõrgustikes. Tänan teid väga!