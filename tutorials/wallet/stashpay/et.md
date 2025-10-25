---
name: StashPay
description: Minimalistlik Bitcoin Wallet kõigile
---

![cover](assets/cover.webp)



Kasutajakogemus on Bitcoin lahenduste kasutuselevõtu võtmeteguriks kogu maailmas. Sujuva, lihtsa ja tehniliselt koormamata kasutajakogemuse pakkumine on paljude rahakottide ja Exchange platvormide prioriteet. Selles osas paistab StashPay silma oma minimalistliku lähenemise poolest, näidates samal ajal Lightning Network võimsust.



Selles õpetuses vaatame seda portfelli, et teada saada, kuidas see töötab ja kuidas see sobib ideaalselt väikeettevõtetele või füüsilisest isikust ettevõtjatele.



## StashPayga alustamine



StashPay on Lightning iseteeninduslik Wallet, mis on tunnustatud eelkõige oma minimalistliku, kasutajakeskse kasutajakogemuse poolest.  Selle Wallet abil ei ole teil vaja mingeid tehnilisi teadmisi, et saada ja saata oma esimesi satoshisid.



StashPay on avatud lähtekoodiga projekt, mis on välja töötatud React Native'is ja mille eesmärk on lahendada kõrgeid tehingutasusid isegi Bitcoin protokolli peamise ahela tehingute puhul. See on saadaval mobiilirakendusena Androidi ja iOSi platvormidel [veebisaidil](https://stashpay.me/) olevate allalaadimislinkide kaudu.



![introduce](assets/fr/01.webp)



Oluline on laadida Android-rakendus alla veebisaidilt, kuna see ei ole saadaval Google Play Store'is.


Kui allalaadimine on lõppenud, andke vajalikud õigused, et saaksite rakenduse oma Android-telefonile paigaldada.



Kui rakendus on paigaldatud, loob StashPay teile esimesel avamisel esialgse Bitcoin Wallet. Enne iga tehingu sooritamist soovitame teha sellest Wallet-st varukoopia. Allpool leiate kõik meie juhised, kuidas tagada, et teie taastamislaused oleksid korralikult varundatud.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Juurdepääs StashPay seadetele, klõpsates ikoonil "Seaded" ja seejärel valikul **Loo varukoopia**. Seejärel lubage taastamislausete kuvamine. Ärge kopeerige oma taastamislauseid telefoni lõikelauale, sest need võivad olla kättesaadavad teistele teie mobiiltelefoni paigaldatud petturirakendustele.



![backup](assets/fr/02.webp)



Te saate ka juba kasutatava Bitcoin Wallet taastada, klõpsates valikul **Recover Wallet** ja sisestades oma 12 või 24 taastamissõna.



### Saage oma esimesed satoshid StashPay'sse



Vajutage avakuval nupule **Võta** ja määrake summa, mis on suurem kui punasega märgitud summa. Meie puhul ei saa me StashPay Wallet abil saada vähem kui 0,11 USD.



![receive](assets/fr/03.webp)



Kui olete summa kindlaks määranud, saate klõpsata nupule **Loo Invoice**, seejärel skaneerige või kopeerige Invoice, et saata see oma satoshis saatjale.



![receive_sats](assets/fr/04.webp)



Saate oma tehinguajalugu vaadata, klõpsates avalehel ikoonil "kell".



![network_fee](assets/fr/05.webp)



Olete kindlasti märganud, et satoshide saamiseks peate maksma võrgutasu. Need tasud arvatakse maha satoshidest, mida te hakkate saama. See tuleneb sellest, et StashPay on Wallet, mis põhineb Breez Development Kit'il. Et saada satoshisid Lightning node-free Kit'i rakendusega, võtab Breez kliendilt (meie puhul StashPaylt) `0,25% + 40 satoshit`. Lisateavet leiate meie Misty Breezi õpetusest.



https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Bitcoinide saatmine StashPayga



Bitcoinide saatmine StashPayga on tänu minimalistlikule Interface-le üsna intuitiivne. Vajutage avakuval nupule **Sendama**. Skaneerige QR-kood või kleepige Address, kuhu soovite satoshisid saata. StashPay tuvastab automaatselt Bitcoin protokolliahela, kuhu soovite bitcoine saata.



![send](assets/fr/06.webp)



Kuna StashPay on Breez Development Kit'il põhinev Wallet, on sellel huvitav eelis: bitcoinide saatmine põhiahelas madala hinnaga. Breez kasutab Bitcoin protokolli erinevate ahelate vaheliste tehingute tegemiseks Boltz'i teenust, mis võimaldab klientidel, kes rakendavad arenduskomplekti, kasutada seda teenust otse oma rakenduses.



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Breez SDK kehtestab siiski minimaalse summa, mille puhul saab bitcoine saata Address-le peamise ahela kaudu.



![onchain](assets/fr/07.webp)



Võite saata bitcoin'e ka oma saaja Lightning Address abil. Vaadake oma tehingu üksikasjad üle ja kinnitage seejärel, klõpsates nupule **Sendama**.



![confirm](assets/fr/08.webp)



## Rohkem konfiguratsioone



StashPay seadetes saate kohandada konfiguratsioone, et kohandada Wallet kasutamist isikupäraselt.



StashPay võimaldab teil Exchange satoshis, mis põhineb teie valitud kohalikul vääringul. Klõpsake valikul **Vääringud**, seejärel otsige oma valuuta StashPay poolt pakutavate +113 valuuta nimekirjast.



![currencies](assets/fr/09.webp)



Menüüst **Võimalused** leiad kõik seaded bitcoinide vastuvõtmiseks StashPayga. Näiteks valides **Valida Lightning või Onchain**, lubate oma Wallet-le bitcoinide vastuvõtmist peamisest ahelast.



![receive-onchain](assets/fr/10.webp)



Valikuga **Scan OnChain addresses** saate värskendada oma Wallet saldot, kontrollides kõiki oma erinevate aadressidega seotud UTXOsid (bitcoinid, mida te pole veel kulutanud).



![rescan](assets/fr/11.webp)



Menüüs **Ekspordilogi** on loetletud kõik Breezi ja Boltzi infrastruktuuri toimingud, mis on seotud teie tehingute ja aatomivahetustega erinevate Bitcoin protokolliahelate vahel.



![export](assets/fr/12.webp)



Sa oled lihtsalt hakkama saanud StashPay minimalistliku Bitcoin Wallet-ga. Kui leidsid selle õpetuse kasulikuks, soovitame meie õpetust, kuidas Bitcoin-ga alustada ja teenida oma esimesed bitcoinid.



https://planb.network/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f