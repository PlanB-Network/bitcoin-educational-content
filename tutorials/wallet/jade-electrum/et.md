---
name: Jade - Electrum
description: Kuidas kasutada oma Jade'i või Jade Plus'i koos Electrum-ga (lauaarvuti)
---

![cover](assets/cover.webp)



_See juhend on võetud [Bitcoin töötubade õppetunnist](https://officinebitcoin.it/lezioni/jadeele/index.html)_



Õpetus on tehtud Jade Classiciga, kuid toimingud kehtivad ka neile, kellel on Jade Plus.



Pärast Jade'i initsialiseerimist saate seda kasutama hakata ja - selleks - valida wallet ekraani.



Jade on seade, mida saab kasutada koos mitme wallet või kaaslase rakendusega, nagu Blockstream neid oma veebisaidil nimetab.



Selles õpetuses näete, kuidas kasutada Electrum Wallet USB-kaabli kaudu.



## Avaliku võtme üleandmine



Võtke ja lülitage oma initsialiseeritud Jade sisse. Niipea, kui te selle sisse lülitate, näeb see välja selline:




![img](assets/en/32.webp)



Kui valid _Unlock Jade_, avaneb menüü, kus tuleb valida, kuidas ühendada seade kaaslase rakendusega.



Electrum-ga saab Jade'i ühendada ainult USB kaudu, seega valige see meetod.



Käivitage Electrum, mis avab ettepaneku avada vaikimisi valikuna viimati kasutatud wallet.



Kui ühendate Jade'i esimest korda Electrum-ga, valige _Create New Wallet_ ja seejärel _Finish_.



![img](assets/en/34.webp)



Nimi wallet.



![img](assets/en/35.webp)



Valige standard Wallet.



![img](assets/en/36.webp)



Võtmesalvestuse valimisel on oluline valida _Kasutage riistvaraseadet_.



![img](assets/en/37.webp)



Electrum alustab riistvaraseadme otsimist.



![img](assets/en/38.webp)



Ühendades USB-ühenduse arvutiga (Jade'ile juba USB C-poolt ühendatud), ilmub wallet riistvara teile lukustusrežiimis. Jade avab lukustuse, sisestades seadistamise käigus määratud kuuekohalise PIN-koodi.




![img](assets/en/39.webp)



Lukustamata riistvara seade, Electrum tuvastab Jade. Jätka, klõpsates nuppu _Next_.



![img](assets/en/40.webp)



Siinkohal palub Electrum teil määrata poliitikaskript: valige _Native Segwit_.



![img](assets/en/41.webp)



Algab wallet avaliku võtme üleandmise etapp Jade'i Electrum ekraanile.



Kui avaliku võtme eksport on lõpetatud, on protsess lõppenud.



Kell on valmis ja Electrum annab järgmise ekraaniga teateid valmimisest.



![img](assets/en/42.webp)



wallet on tegelikult loodud ja te võite hakata seda uurima: te näete _aadressid_, _valuutakoti andmed_ ja - mis kõige tähtsam - te näete paremas alumises nurgas märget, et tegemist on Blockstream'i seadmega. Roheline punkt Blockstream'i logo kõrval näitab, et seade on sisse lülitatud ja korralikult ühendatud kohalikku võrku.



![img](assets/en/43.webp)



## Tehingute vastuvõtmine ja kulutamine



Electrum menüüst _Receive_, generate "scriptPubKey" (aadress), et saada raha. Alustage alati väikese summaga ja tehke vastuvõtu+kulu test.



![img](assets/en/44.webp)



Kui olete saanud satss-i, saate nende saabumist kontrollida menüüs _History_.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



Kui tehing on kinnitatud, saate kulutada selle UTXO ja lõpetada testi.



Kulud hõlmavad Jade'i allkirja kasutamist.



Mine Electrum menüüsse _Send_, kleebi scriptPubKey ja kontrolli seda hästi.



![img](assets/en/47.webp)



Kui olete lõpetanud, vajutage nuppu _Maksma_.



Avaneb tehinguaken, kus on oluline määrata õiged tehingutasud. Kui olete kõik seadistused lõpetanud, klõpsake paremas alumises nurgas nupule _Preview_.



![img](assets/en/48.webp)



Tehingu aknas kuvatakse mõned olulised andmed, eelkõige staatus: "Allkirjastamata".



Selles etapis näete ka käsku _Sign_, millele tuleb klõpsata, et kinnitada allkiri Jade'iga.



![img](assets/en/49.webp)



Nüüd algab sidefaas ekraani wallet ja riistvaraseadme vahel, milles Electrum hoiatab teid, et järgiksite riistvaraseadme juhiseid, mis on sisse lülitatud ja valmis allkirjastamiseks.



![img](assets/en/50.webp)



**Ettevahetuseks peaksite siiski kõigepealt kontrollima, mida allkirjastate: kõik äsja loodud tehingu parameetrid ilmuvad ka Jade**-s ja te saate neid kõiki kontrollida.



![img](assets/en/51.webp)



Jätkamiseks veenduge, et te asetate kursori alati noolele "→", mis viib järgmiste sammude juurde, ja mitte kunagi noolele "X", välja arvatud juhul, kui soovite operatsiooni lõpetada ilma seda lõpetamata.



Kontrollimisosa lõpeb tasu kuvamisega. Sel hetkel on kinnitus samaväärne allkirja panemisega.



![img](assets/en/52.webp)



Jade töötleb lühikest aega toimingut, kui see on lõpetatud, naaseb ta algmenüüsse.



![img](assets/en/53.webp)



Electrum-s näete tehingu staatust, mis on muutunud `Unsigned`-st `Signed`-ks ja nüüd on teil võimalik seda levitada, klõpsates _Broadcast_.



![img](assets/en/54.webp)



wallet, mida on sel viisil katsetatud, võib kasutada UTXO vastuvõtmiseks, mis on ette nähtud ohutuks ladustamiseks.



![img](assets/en/55.webp)



See juhend on näide selle kohta, kuidas kasutada oma Jade'i, mis on ühendatud USB kaudu, ainult wallet kellaga. Electrum on klassikaline näide, kuid te võite eelistada muud wallet tarkvara. Jade ekspordib avaliku võtme paljudesse teistesse rahakottidesse: leiate sarnaseid funktsioone, mida loete sellest juhendist, et juhendada teid ja leida, kuidas kasutada seda oma lemmik companio rakendust.