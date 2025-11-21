---
name: Sats.mobi

description: Telegrammiga juurdepääsetav eestkostetav Wallet
---

![cover](assets/cover.webp)


_Selle õpetuse on kirjutanud_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobi on Wallet, mis tegutseb Telegramis, millel on kõik Lightning Network (eestkostetava) Wallet funktsioonid ja lisaks rida väga meelelahutuslikke funktsioone. See sai alguse nüüdseks lõpetatud LightningTipBoti Fork-st, pärides kõik selle funktsioonid, lisades samal ajal uuemaid funktsioone, muutes selle seega kaasaegsemaks. Nagu LNTipBot, on ka Sats.Mobi avatud lähtekoodiga filosoofia. Wallet saab konfigureerida ja hallata iseseisvalt, kloonides seda sellest [repositooriumist](https://github.com/massmux/SatsMobiBot).


Kui soovite seda lihtsalt kasutada, siis Telegramis vestluse alustamine näitab, et tegemist on botiga.


## Seaded

Otsige Telegrami otsinguribalt "satsmobi" ja [bot](@SatsMobiBot) link ilmub.


**Hoiatus**: Kui te ei ole kindel, et otsite Telegrami kaudu, pääsete botile turvaliselt ligi, kasutades järgmist [linki](https://t.me/SatsMobiBot)


![image](assets/it/01.webp)


Alustamiseks tuleb vaid vajutada _START_


![image](assets/it/02.webp)


Wallet uurimiseks võite valida vasakult allosas _Menu_.


![image](assets/it/03.webp)


Nüüd valige peamiste käskude hulgast _/help_.


![image](assets/it/04.webp)


Sats.Mobi tervitab meid sõnumiga, milles on loetletud kõik peamised funktsioonid. Käivitamisel loob bott ka LN Address, mis on seotud valitud käepidemega Telegramis (mis on vaikimisi unikaalne). Selle Wallet-ga Sats saatmise ja vastuvõtmise käsud on nähtavad, samuti muud funktsioonid, mida näeme hiljem. Huvitav on heita pilk ka _/täiendatud_ menüüsse


![image](assets/it/05.webp)


Märkimisväärne on, et Sats.Mobi lõi ka anonüümse LN Address, mida kasutatakse privaatsuse saavutamiseks. Bot töötab käskudega: klõpsake lihtsalt vastaval sõnal või kirjutage sõnumiribale kaldkriips "/", millele järgneb käsk, mida soovite täita. Isegi kui Wallet on äsja loodud, valige näiteks _/transactions_


![image](assets/it/06.webp)


See käsk näitab viimaste tehingute nimekirja, mis antud juhul on võrdne nulliga.


![image](assets/it/07.webp)


## Sats vastuvõtmine

Invoice loomise ja Sats vastuvõtmise käsk on _/arve_. Sats.Mobi töötab ainult Satoshi-s, mis on Bitcoin väikseim ühik; seega tuleb Invoice loomiseks kirjutada sõnumiribale summa Sats-s ja seejärel saata see boti vestluses.

![image](assets/it/08.webp)


Järgnevas näites valiti 210 Sats suuruse summa saamiseks.


![cover](assets/it/09.webp)


Pärast mõne hetke ootamist, kuni Invoice on valmis, on see saadaval tekstina ja QR-koodina. Tasudes Invoice, näitab Wallet saldot. Kui mingil põhjusel ei ole kogusumma uuendatud, kirjutage _/saldo_ ja vajutage klahvi "enter".


![image](assets/it/10.webp)


## Sats saatmine


Kuigi Sats on äärmiselt väärtuslik vara, millest ei tohiks kergekäeliselt osa saada, teeb Sats.Mobi selle osa ahvatlevaks, mõne lühikese testi (st paar proovitehingut) tegemine ei ole probleemiks.


### Invoice maksmine


Lihtsaim viis Invoice-i maksmiseks on kopeerida sõnumi string `lnbc1xxxxx` ja kleepida see pärast käsu _/pay_ sisestamist sõnumiribale. **Korrektne süntaks** nõuab, et käsu järele jääks tühik.


![image](assets/it/11.webp)


Wallet saadab sõnumi, milles palub kinnitust. Vajutades nupule _Pay_, tasub Invoice.


![image](assets/it/12.webp)


Sats.Mobi võib tugineda tõhusale ja hästi ühendatud Lightning-sõlmele, harva ebaõnnestuvad maksed, sest see suudab alati leida õige marsruutimise.


### Maksmine mugavalt mobiiltelefoni kaudu


Telegrami sirvimine, Sats.Mobi on saadaval ka mobiilis. Kõige mugavam funktsioon mobiiliga maksmiseks on QR-koodi skaneerimine, kuid sellel Wallet-l puudub see juba oma olemuselt, sest tegemist ei ole iseseisva rakendusega, vaid see sisaldub sotsiaalvõrgustikus. Sats.Mobi on seetõttu programmeeritud nii, et see lihtsustaks mobiilikogemust nii palju kui võimalik: see suudab tõepoolest dekodeerida pilti, näiteks fotot, mis on tehtud selle Invoice QR-koodist, mille eest soovite maksta.


Oletame näiteks, et soovite maksta Invoice 50 Sats.


![image](assets/it/20.webp)


Kui seda meile näidatakse, saame teha foto seotud QR-koodist.


![image](assets/it/21.webp)


Seejärel avame mobiilis Telegrami ja lisame Sats.Mobiga peetavasse vestlusesse QR-koodist äsja tehtud foto


![cover](assets/it/22.webp)


Kui see on valitud, saadame selle botile:


![image](assets/it/23.webp)

Sats.Mobi dekodeerib foto ja **esitab kohe maksetaotluse** koos õige kirjeldusega. Vestluskeskkonnas küsitakse kinnitust, jätkamiseks tuleb vajutada _/maksa_

![image](assets/it/24.webp)


Palun oodake hetk, et makse oleks võimalik töödelda.


![image](assets/it/25.webp)


Invoice 50 Sats eest on makstud, tulemus, mis on saavutatud ilma kaamera ja selle integreeritud skaneerimisfunktsiooni kasutamiseta.


### Sats.Mobi Telegrammi gruppides


![image](assets/it/27.webp)


LNTipBoti kuulsaks teinud ja Sats.Mobi poolt Telegrami toodud funktsioonide hulgas on see, mis muudab grupi liikmete jaoks kogemuse lõbusaks ja interaktiivseks.

Omanikud saavad boti kutsuda grupivestlusega liituma ja seejärel nimetada Sats.Mobi administraatoriks. Sellest hetkest alates algab lõbu, sest liikmed saavad hakata teisi kasutajaid premeerima nende panuse eest gruppi.


- _/tip_ lisab vihje, vastates sõnumile;
- _/send_ saadab raha, määrates saajaks LN Address või Telegram-käepi;
- _/faucet_ (menüüs _/advanced_) võimaldab luua vihjeid, mida rühma kiiremad liikmed saavad koguda, klõpsates nupule _/collect_;
- _/tipjar_ (menüüs _/täiendatud_) loob teise tüüpi jaotuse, mida saab saata grupi kasutajatele.


Igal käsul on oma süntaks, mis on selgitatud käskude peamenüüs.


Ja kui me ei ole grupi omanik? Pole probleemi: paluge lihtsalt asutajal kutsuda Sats.Mobi, lisage see grupi administraatoriks ja kõik on valmis!


## Müügipunkt (POS)


Kui Sats.Mobi käivitatakse esimest korda, loob bott kasutajale ka teise funktsiooni: **POS**. "Seadme" aktiveerib kasutaja käsuga _/pos_ või klõpsates sellega seotud nuppu konsoolist paremal allosas. Tegelikult on POS veebirakendus, mis avaneb hüpikakna Telegrami vestluses


![image](assets/it/14.webp)


Interface kuvab kasutaja isiklikku Telegram-käepi vasakus ülaosas ja seda kasutatakse lihtsalt nii, nagu kõiki kassasid kasutatakse: sisestades summa klaviatuurile. Oletame nüüd, et soovime koguda 21 eurosenti teenuse eest. Teades, et Sats.Mobi haldab natiivselt ainult Sats, ei ole lihtne ümberarvestust peas teha. Vastupidi, kassas kuvatakse arvestusühikuna eurot, näidates samal ajal vaste Satoshi-s.


![image](assets/it/15.webp)

Vajutades nupule _/OK_ kuvatakse Invoice, mida saab näidata kliendile QR-koodi kaudu või mida saab saata stringina kiirsõnumite kaudu, et selle eest saaks tasuda.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


Loomulikult on kassasüsteem kättesaadav ka mobiiltelefonidel, millele pääseb ligi samamoodi nagu eelnevalt näidatud.


![image](assets/it/18.webp)


See on ka mobiiltelefoni ekraanil hästi kuvatud:


![image](assets/it/19.webp)


## Täiendavad omadused


Sats.Mobi Wallet pakub ka muid funktsioone, mis, nagu me nägime, laiendavad Wallet kontseptsiooni kaugemale maksete vastuvõtmise ja saatmise toimingutest:


- _/nostr_: Wallet ühendamiseks oma Nostr-kasutajaga, et saada zap'e;
- _/cashback_: näitab koodi, mida saab esitada kaupmehele, et saada ostu eest raha tagasi;
- _/buy_: käivitab boti sees juhendatud protseduuri, mis võimaldab osta Sats euro eest;
- _/activatecard_: NFC deebetkaardi aktiveerimise taotlemiseks, mida saab laadida Sats.Mobi Wallet kaudu ja mille jaoks saab aktiveerida teateid;
- _/link_: loob lingi teie enda Zeus või Blue Wallet jaoks, mida saab kasutada selle Wallet kaugjuhtimispuldina.


## Kokkuvõte

Sats.Mobi on meeldiv ja lõbus Wallet kasutada, mis toob tagasi LNTipBotiga saadud kogemused, kasutades LNBits'i täiustatud funktsioone. Siiski on oluline meeles pidada, et **see on hooldusteenus**. Seetõttu tuleks seda kasutada väga väheste Sats hoidmiseks, see ei ole peamine Wallet teie Lightning Network vahendite jaoks. Samuti on olemas sisemine mahupiirang, mis on võrdne 500 000 Sats-ga ja mida ei soovitata ületada.


Kui otsite Lightning Network rahakotte, mis ei ole mõeldud kasutamiseks, on kindlasti soovitav vaadata teisi tooteid.


---
### Dokumentatsioon


- [Github](https://github.com/massmux/SatsMobiBot)
- Playlist [videos](https://www.youtube.com/results?search_query=Sats.mobi) demo