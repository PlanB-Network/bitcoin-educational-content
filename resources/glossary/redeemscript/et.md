---
term: REDEEMSCRIPT
---

Skript, mis määratleb konkreetsed tingimused, mida sisendid peavad rahuldama, et vabastada vahendid, mis on seotud P2SH väljundiga. P2SH UTXO puhul sisaldab `scriptPubKey` `redeemScript`i räsi. Kui tehing soovib seda UTXO-d sisendina kasutada, peab see esitama selge `redeemScript`i, mis vastab `scriptPubKey`s sisalduvale räsi. Seega antakse `redeemScript` sisendi `scriptSig`is koos teiste elementidega, mis on vajalikud skripti tingimuste rahuldamiseks, nagu allkirjad või avalikud võtmed. See kapseldatud struktuur tagab, et kulutamistingimuste üksikasjad püsivad peidetud kuni bitcoinide tegeliku kulutamiseni. Seda kasutatakse märkimisväärselt Legacy P2SH multisignatuuri rahakottide jaoks.