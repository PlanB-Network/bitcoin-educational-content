---
term: UTXO
---

Akronüüm *Unspent Transaction Output* jaoks. UTXO on tehingu väljund, mida ei ole veel kulutatud, tähendades, et seda ei ole kasutatud uue tehingu sisendina. UTXOd esindavad bitcoini kasutaja omandis olevat ja hetkel kulutamiseks saadaolevat bitcoini osa. Iga UTXO on seotud spetsiifilise väljundi skriptiga (`scriptPubKey`), mis määratleb vajalikud tingimused bitcoinide kulutamiseks. Bitcoinis tarbivad tehingud neid UTXOsid sisenditena ja loovad uusi UTXOd väljunditena. UTXO mudel on Bitcoinile fundamentaalne, kuna see võimaldab lihtsalt kontrollida, et tehingud ei ürita kulutada bitcoine, mida ei eksisteeri või on juba kulutatud.