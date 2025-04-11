---
term: UTXO

---
Akronüüm *Unspent Transaction Output*. UTXO on tehingu väljund, mida ei ole veel kulutatud, st seda ei ole kasutatud uue tehingu sisendina. UTXOd kujutavad endast bitcoinide osa, mida kasutaja omab ja mida saab hetkel kulutada. Iga UTXO on seotud konkreetse väljundskriptiga (`scriptPubKey`), mis määratleb bitcoinide kulutamiseks vajalikud tingimused. Bitcoini tehingud tarbivad neid UTXOsid sisendina ja loovad uusi UTXOsid väljunditena. UTXO-mudel on Bitcoini jaoks väga oluline, sest see võimaldab hõlpsasti kontrollida, et tehingutega ei üritata kulutada bitcoin'e, mida ei ole olemas või mis on juba kulutatud.