---
term: REDEEMSCRIPT

---
Skript, mis määratleb konkreetsed tingimused, millele sisendid peavad vastama, et P2SH väljundiga seotud vahendid vabastataks. P2SH UTXOs sisaldab `scriptPubKey` `redeemScript`i hashi. Kui tehing soovib seda UTXOd sisendina kulutada, peab ta esitama selge `redeemScript`, mis vastab `scriptPubKey`s sisalduvale hashile. Seega on `redeemScript` esitatud sisendi `scriptSig`is koos muude skripti tingimuste täitmiseks vajalike elementidega, nagu allkirjad või avalikud võtmed. Selline kapseldatud struktuur tagab, et kulutamistingimuste üksikasjad jäävad varjatud, kuni bitcoinid tegelikult kulutatakse. Seda kasutatakse eelkõige Legacy P2SH multisignatuursete rahakottide puhul.