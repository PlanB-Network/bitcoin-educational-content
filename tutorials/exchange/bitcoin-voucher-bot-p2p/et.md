---
name: BitcoinVoucherBot P2P
description: Kuidas osta ja müüa Bitcoin P2P koos BitcoinVoucherBotiga
---

![image](assets/cover.webp)



Me kuuleme ikka veel BitcoinVoucherBotist, Telegram botist, mis on loodud Bitcoin ostmiseks ilma [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) SEPA pangaülekande kaudu. Kahjuks alates novembrist 2025 ei ole BitcoinVoucherBot oma tsentraliseeritud kujul enam KYC-ta teenusena saadaval.



Selles juhendis vaatame, kuidas töötab uus rakendus, mis võimaldab kasutajatel osta ja müüa Bitcoin otse uuel P2P (Peer-To-Peer) turul, seega ei ole KYC. Vastukaaluks uutele piirangutele, mis üha enam ohustavad digitaalset vabadust ja privaatsust, lõid arendajad selle laienduse, mis annab kasutajatele võimaluse osta ja müüa Bitcoin suure anonüümsusega P2P (Peer-To-Peer) kaudu. Vaatame koos, kuidas see uus vahetusmeetod töötab.



Teenuse kasutamiseks peate tegema ülekandeid Lightning Network kaudu. Seega veenduge, et teil on wallet, mis toetab seda protokolli ja võimaldab teil kasutada "LNURL" või "Lightning Address" raha vastuvõtmiseks ja saatmiseks.



Toetatud rahakottide hulgast leiame:





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Hooldus)
- [Wallet Of Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Hooldusasutus koos vahetusega mittehooldusasutusse)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



Või mis tahes wallet, millel on "Lightning Address" ja mis genereerib Bolt11 arve. rahakotid, mis generate Bolt12 arve, ei ole praegu toetatud. Lisateavet leiate [Bolt](https://planb.academy/resources/glossary/bolt) määratlusest.



Selles õpetuses kasutame Wallet of Satoshi, arvestades selle lihtsat ja vahetut kasutust.



**Ohutus**: Kasutage seda ainult ajutiselt ja kandke see kohe üle mittekaitstavale süsteemile, et saavutada täielik suveräänsus. Alates 2025. aasta oktoobrist sisaldab see iOS/Androidis (uuendage rakendust) stabiilset isevalitseja režiimi kogu maailmas, millel on autonoomsed privaatvõtmed, režiimide vahel vahetamine, kohandatud Lightning-aadressid ja seed 12-sõnaline varundamine. Siiski jääb see ajutiseks lahenduseks kuni konsolideerimiseni, eelistades wallet mittekaitstavat küpset pikaajalise haldamise jaoks.



Väga hea! Nüüd saame alustada oma teekonda, mis juhatab teid samm-sammult konto loomisel, ostu- ja müügimängude haldamisel ning piiratud ala kasutamisel.



## Wallet ja registreerimine



Esiteks, kui sul ei ole seda veel nutitelefonile paigaldatud, lae alla Wallet of Satoshi.





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Kui te ei ole kunagi kasutanud Wallet of Satoshi ja soovite mõista, kuidas see töötab, siis soovitan teil jälgida seda õpetust, et te saaksite selle korralikult aktiveerida ja turvaliselt varundada.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Nüüd, kui teie wallet on valmis, võite alustada väikese koguse sats saatmist. Pidage meeles, et P2P (Peer-To-Peer) platvormi registreerimise lõpuleviimiseks peate kontrollimeetmena saatma 1000 sats: see on selleks, et luua tõkke mis tahes phantom match (kelmuse) tüüpi rünnakute vastu, takistades kellelgi registreerumist ilma rämpspostifiltrita.



![image](assets/it/02.webp)



Nüüd saame avada P2P (Peer-To-Peer) platvormi, et jätkata registreerimist. Saate sisse logida lauaarvutitest või nutitelefonide brauseritest, Telegram BitcoinVoucherBot'i kaudu või .onion linkide kaudu, et tagada veelgi suurem privaatsus.



kui otsustate kasutada Tor .onion linki, siis soovitan ka "Tor Browser". Kui te seda veel ei tea, siis saate selle kohta rohkem teada sellel lingil:



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Nüüd valige, kuidas soovite platvormile jõuda.





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Desktop / Brauser Smartphone](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Teid suunatakse ümber pealehele.



vajutage "Get Starter", et kohe alustada



![image](assets/it/03.webp)



Järgmisel ekraanil tuleb valida parool ja sisestada see (lahter A) ning seejärel korrata seda (lahter B). Soovitan selle salasõna kohe varunduskandjale salvestada, mis võib olla turvalisel digitaalsel seadmel, näiteks "Bitwarden":



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

või salvestage oma parool paberkandjal (**hoiatus**: see ei ole hea lahendus, kuid kui see on mõeldud ajutiseks lahenduseks, siis on see okei).



Märkige kontrollruut, kus te kinnitate, et te ei ole robot (lahter C). Märkus Ärge lubage RSA-krüpteerimist, kui te ei tea täpselt, mis see on ja kuidas see töötab. Selles etapis ei pea te midagi tegema. Klõpsake nupule "Generate Avatar" ("Loo Avatar") (lahter D).



![image](assets/it/04.webp)



Nüüd peate registreerimise lõpetamiseks maksma 1000 sats.



1. Alustades ülevalt, näete kõigepealt oma juhuslikult genereeritud ja äärmiselt olulist "Avatari ID" Salvestage see hoolikalt, nagu ma soovitasin teil teha parooliga.


2. Seejärel peate sisestama oma "Lightning Address" allolevasse lahtrisse. See võimaldab teil saada makseid, kui te ostate Bitcoin või saate tagasimakseid. Kui te kasutate Wallet Of Satoshi, siis saate kopeerida oma Address, klõpsates nupule receive.


3. Märkige kinnituskast, kus te kinnitate, et te ei ole robot.


4. Tasu 1000 sats, et saada juurdepääs oma piiratud alale. Kui te ei saa seda raamida, klõpsake sellel hiirega (arvutis) või koputage seda sõrmega (brauseris/Telegram nutitelefonides), et kopeerida aadress, mille peate kleepima Wallet of Satoshi-i ja viima lõpule arve maksmise.



![image](assets/it/05.webp)



See on teie LNURL Address.



![image](assets/it/06.webp)



Palju õnne!!! Sa oled loonud oma Avatari jäädavalt ja saad kokkuvõtet vaadata siin. Soovitan veelkord hoolikalt salvestada nii oma Avatari kui ka salasõna, nagu ma juba varem soovitasin.



Klõpsake "Olen salvestanud oma volitused, jätka" (tõlge: "Olen salvestanud oma volitused, jätka")



![image](assets/it/07.webp)



Nüüd olete platvormi südames, kus saate vaadata kõiki kaubandustulemusi koos nende üksikasjadega. Selgema ülevaate saamiseks näete allpool veebilehele omaseid pilte lauaarvutitest.





- "Tüüp" ("Type") määrab, kas tegemist on müügi ("Sell") või ostu ("Buy") müügiga
- "Amount" ("Summa"): näitab, kui palju sats kasutaja müüb, kui vaste on tüüpi "Sell", või kui palju Bitcoin kasutaja on valmis ostma, kui vaste on tüüpi "Buy".
- "BTC Price with Margin" ("BTC hind koos marginaaliga"): näitab hinda, mis võtab arvesse marginaali, mis on kohaldatud üle märgitud väärtuse.
- "Marginaal" ("Margin") on protsent, mida rakendatakse turuhinnale, Miinusmärkiga (-) saate turuhinnast allahindlust, plussmärgiga (+) rakendatakse turuhinnale preemiat.
- "Meetod" ("Method") näitab, millise motodo järgi kasutaja eelistab maksta.
- "Looja" on unikaalne avatar, mida kasutaja kasutab platvormil.
- "Rep" (maine) Kasutaja maine tase on vahemikus -5 ebausaldusväärne kuni +5 äärmiselt usaldusväärne.
- "Status" ("Staatus"): näitab mängu staatust. Näidise ekraanipildil on kõik vasted "Open" ("Avatud").
- "Expiration" ("Aegumine"): näitab, kui palju aega on jäänud enne mängu lõppemist ja tühistamist, kui seda ei ole keegi valinud.



![image](assets/it/08.webp)



Oma profiili avamiseks klõpsake üleval paremal oma Avataril.



![image](assets/it/09.webp)



Siin näed oma Avatari nime, kasutaja ID-d, loomise kuupäeva ja mainet, mis kajastab positiivselt või negatiivselt sinu käitumist läbirääkimistel.



![image](assets/it/10.webp)



Seadete sektsioonis saate vaadata oma "Lightning Address", mis on sisestatud registreerimise ajal, ja seda vajaduse korral muuta. Teil on ka võimalus luua avalik võti, mida, nagu mainitud, tuleks luua ainult siis, kui teil on vastavad oskused. Seda kasutatakse sõnumite krüpteerimiseks, mida vahetate oma vastaspoolega otse oma arvutist.



Telegram teavitamisfunktsioon on väga soovitatav. Selle aktiveerimisel ilmub QR-kood, mida saate Telegram rakendusega raamida: nii saate reaalajas teateid kõigi teie mängudega seotud toimingute kohta otse Telegram bot'i vestluses.



![image](assets/it/11.webp)



Lõpuks leiate oma soovituste sektsiooni, kus on teie poolt kutsutud kasutajate poolt teenitud tulu. Siit saate kasutada nuppu, et jagada oma linki või QR-koodi, ning veidi allapoole saate vaadata vastete nimekirja, et jälgida oma mainet koos vastava skooriga.



![image](assets/it/12.webp)



## Looge tellimus, et osta Bitcoin



Turuplatsile sisenemine: klõpsake põhinavigatsiooniribalt ostukorvisümbolile "Marketplace" ("Turuplats"), et avada tellimusraamat. seejärel alustage uut tellimust: vajutage protsessi alustamiseks nupule "New Order" ("Uus tellimus").



![image](assets/it/13.webp)





- Seadke tellimuse üksikasjad:
- Valige valik "Osta Bitcoin" ("Buy Bitcoin").
- Sisestage soovitud sats kogus.
- Määrake hinnamarginaal (vahemikus -20% kuni +20% turuväärtusest).
- Valige makseviis (Instant SEPA jne).
- Näitab eelistatud valuutat.
- Tellimuse kinnitamine: klõpsake "Tellimuse loomine" ("Tellimuse kinnitamine"), et minna edasi esitamise etappi.



![image](assets/it/14.webp)



Nõutav tagatisraha: tellimuse aktiveerimiseks on nõutav tagatisraha, mis moodustab 10% kogusummast, millele lisandub teenustasu.




- Ettemaks: kui tellimus luuakse, genereerib süsteem automaatselt Lightning-arve. Tagatisraha on ainult ajutine ja see makstakse tagasi, kui tellimus on lõpetatud.
- Peamised omadused:
- Tagatisraha: 10% tellimuse väärtusest.
- Teenustasu: platvormi kasutamise maksumus.
- Tähtaeg: Teil on makse tegemiseks aega 5 minutit, vastasel juhul lõpeb tehing.



![image](assets/it/15.webp)



Pärast edukat maksmist ilmub tellimus raamatusse ja on nähtav kõigile kasutajatele, kes saavad selle valida ja vastu võtta. Müügitellimuse loomiseks tuleb vaid klõpsata "Sell Bitcoin" ("Müü Bitcoin"), sisestada satoshi kogus, mida soovite müüa, määrata marginaal, valida makseviis ja valuuta, seejärel jätkata 10% tagatisraha kui tagatisraha. Kui see on lõpetatud, on teie vaste loetelus nähtav.



![image](assets/it/16.webp)



## Kuidas tellimust vastu võtta



1. Müüjad näevad raamatus kõigi olemasolevate tellimuste nimekirja.


2. Kontrollige üksikasju: iga tellimuse kohta on esitatud järgmised andmed:




  - Bitcoin kogus,
  - Hinna marginaal,
  - Makseviis,
  - Kasutaja maine.



![image](assets/it/17.webp)



3. Klõpsake tellimusel, et avada kogu teavet sisaldav leht.


4. Ettepaneku vastuvõtmiseks vajutage "Müü Bitcoin" ("Sell Bitcoin").



![image](assets/it/18.webp)



## Müüja nõutav tagatisraha



Kui tellimus on vastu võetud, koostab süsteem arve maksmiseks. Tagatisraha sisaldab:



- Tellimuse kogusumma,



- teeninduskomisjon.



Tagatisraha tuleb tasuda ettenähtud tähtaja jooksul, vastasel juhul tehingut ei kinnitata.



![image](assets/it/19.webp)



## Maksejuhiste saatmine



Pärast sissemakse tegemist ilmub tehing müüja isiklikule armatuurlauale, kes peab edastama andmed ostjale, et sooritada makse fiat-valuutas.



1. Müüja kuvab aktiivse tehingu oma paneelis.


2. Klõpsake nupule "Maksejuhiste esitamine"


3. Sisestage kõik vajalikud andmed fiat-makse kohta (IBAN, saaja, aadress, makse põhjus jne).


4. Klõpsake "Send Message" ("Sõnumi saatmine"), et edastada andmed ostjale.



![image](assets/it/20.webp)



## Maksekorraldus



Ostja saab platvormi vestluses sõnumi kõigi vajalike andmetega, et teha makse fiat-valuutas:




- Pangaandmed: IBAN koos müüja kontoomaniku nime ja aadressiga.
- Täpne summa: täpne ülekantav fiat-summa.
- Põhjus/kirjeldus: tehingus sisalduv tekst.
- Tähtaeg: tähtaeg, mille jooksul tuleb makse sooritada.



Ülekanne toimub väljaspool P2P süsteemi ja seda tuleb teha oma pangandusasutuse kaudu.



⚠️ **Tähtis märkus:** Kinnitus platvormil tuleks teha alles pärast seda, kui olete tegelikult korraldanud ülekande või fiat-makse oma panga kaudu.



![image](assets/it/21.webp)



## Makse kinnitamine fiat



See samm on ostja jaoks ülioluline ja seda tuleks teha alles pärast seda, kui on kontrollitud, et makse on tegelikult saadetud.



1. Andmete saamine: ostja on saanud müüjalt maksejuhised.


2. Makse teostamine: fiat-ülekanne korraldatakse oma pangakontolt.


3. Kontrollimine: kontrollige, et toiming on õigesti töödeldud.


4. Kinnitage platvormil: klõpsake kaubavahetuse lehel "Kinnita fiat-makse" ("Confirm fiat payment").


Nupp "Kinnita makse fiat" ilmub tehingu sektsioonis ja seda tuleks kasutada alles pärast seda, kui olete veendunud, et makse on tõepoolest saadetud.



![image](assets/it/22.webp)



Protsessi viimane samm on, et müüja kinnitab fiat-makse kättesaamist, misjärel satss vabastatakse ostjale.



![image](assets/it/23.webp)



## Kokkuvõte



Loodan, et see õpetus aitab teil kasutada uut meetodit Bitcoinsiga kauplemiseks või isegi lihtsalt nende ostmiseks, kas oma väärtuse hoidmiseks või igapäevaste maksete ellu viimiseks. Ikka jääb uks, mida uurida, et tulla toime sellega, mis meie digitaalses maailmas peagi juhtub.



Meid kontrollivate organite poolt juhitud silmus tõmbub üha tihedamalt kokku, et sünnitada üha enam kontrollitav internet. Ostes P2P, hoiad oma ostud täiesti anonüümselt, ei jäta mingeid jälgi ega mingeid järelkajasid kolmandate isikute poolt.