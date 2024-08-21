---
term: P2SH
---

P2SH tähistab *Maksa Skripti Räsi* (Pay to Script Hash). See on standardne skriptimudel, mida kasutatakse kulutamistingimuste kehtestamiseks UTXO-s. Erinevalt P2PK ja P2PKH skriptidest, kus kulutamistingimused on eelnevalt määratletud, võimaldab P2SH integreerida suvalisi kulutamistingimusi ja lisafunktsioone tehinguskripti.

Tehniliselt, P2SH tehingus, `scriptPubKey` sisaldab `redeemScript` krüptograafilist räsi, mitte eksplitsiitseid kulutamistingimusi. See räsi saadakse kasutades `SHA256` räsi. Bitcoine saates P2SH aadressile, ei paljastata aluseks olevat `redeemScript`i. Tehingusse lisatakse ainult selle räsi. P2SH aadressid kodeeritakse `Base58Check` formaadis ja algavad numbriga `3`. Kui saaja soovib vastuvõetud bitcoine kulutada, peab ta esitama `redeemScript`i, mis vastab `scriptPubKey`s olevale räsile, koos vajalike andmetega selle `redeemScript`i tingimuste täitmiseks. Näiteks P2SH multisignatuuri skripti puhul võib skript nõuda allkirju mitmelt privaatvõtmelt.

P2SH kasutamine pakub rohkem paindlikkust, kuna see võimaldab luua suvalisi skripte ilma, et saatja teaks detaile. P2SH tutvustati 2012. aastal BIP16-ga.