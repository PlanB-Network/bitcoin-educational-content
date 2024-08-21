---
term: P2MS
---

P2MS tähistab *Pay to Multisig*, mis tõlkes tähendab "maksa mitmele allkirjale". See on standardne skriptimudel, mida kasutatakse kulutamistingimuste seadmiseks UTXO-le. See võimaldab lukustada bitcoine mitme avaliku võtmega. Nende bitcoinide kulutamiseks on vajalik eelnevalt määratletud arvu seotud privaatvõtmetega allkiri. Näiteks `P2MS 2/3` hõlmab `3` avalikku võtit koos `3` seotud salajase privaatvõtmega. Selle P2MS skriptiga lukustatud bitcoinide kulutamiseks on vaja vähemalt `2` `3`st privaatvõtmest saadud allkirja. See on lävendturvalisuse süsteem.

Selle skripti leiutas 2011. aastal Gavin Andresen, kui ta võttis üle peamise Bitcoin klientrakenduse hoolduse. Tänapäeval kasutavad P2MS-i vaid mõned rakendused marginaalselt. Enamik kaasaegseid multisignatuure kasutab teisi skripte nagu P2SH või P2WSH. Võrreldes nendega on P2MS äärmiselt lihtne. Selles sisalduvad avalikud võtmed paljastatakse tehingu vastuvõtmisel. P2MS-i kasutamine on ka kallim kui teiste multisignatuuri skriptide puhul.

> ► *P2MS-i nimetatakse sageli "bare-multisig", mida võiks tõlkida kui "alasti multisignatuur" või "toores multisignatuur". 2023. aasta alguses olid P2MS skriptid Stamps protokolli väärkasutamise tõttu vaidluse keskmes. Nende mõju UTXO komplektile toodi eriti esile.*