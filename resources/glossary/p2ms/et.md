---
term: P2MS

---
P2MS tähendab *Pay to Multisig*, mis tähendab "maksa mitme allkirja eest". See on standardne skripti mudel, mida kasutatakse UTXO kulutustingimuste kehtestamiseks. See võimaldab bitcoinide lukustamist mitme avaliku võtmega. Nende bitcoinide kulutamiseks on vaja allkirja, millel on eelnevalt kindlaks määratud arv seotud privaatvõtmeid. Näiteks `P2MS 2/3` hõlmab `3` avalikku võtit koos `3` seotud salajase privaatvõtmega. Selle P2MS-skriptiga lukustatud bitcoinide kulutamiseks on vaja allkirja, millel on vähemalt 2 privaatvõtit 3-st. See on lävendi turvasüsteem.

Selle skripti leiutas 2011. aastal Gavin Andresen, kui ta võttis üle Bitcoini põhikliendi hoolduse. Tänapäeval kasutavad P2MS-i vaid mõned rakendused marginaalselt. Valdav enamus kaasaegseid multisignatuurid kasutavad teisi skripte, nagu P2SH või P2WSH. Nendega võrreldes on P2MS äärmiselt triviaalne. Avalikud võtmed, millest see koosneb, paljastatakse tehingu vastuvõtmisel. P2MS-i kasutamine on ka kallim kui teiste mitme allkirja skriptide kasutamine.

> ► *P2MS-i nimetatakse sageli "paljaks multisignatuuriks", mida võib tõlkida kui "paljas multisignatuur" või "toores multisignatuur". 2023. aasta alguses olid P2MS-skriptid vastuolude keskmes nende väärkasutuse tõttu Stamps-protokollis. Eelkõige toodi välja nende mõju UTXO komplektile.*