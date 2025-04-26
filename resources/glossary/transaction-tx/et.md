---
term: TEHING (TX)

---
Bitcoini kontekstis on tehing (lühend "TX") plokiahelas salvestatud operatsioon, mis kannab bitcoinide omandiõiguse üle ühelt või mitmelt sisendilt ühele või mitmele väljundile. Iga tehing tarbib sisenditena kasutamata tehingu väljundid (UTXO), mis on eelmiste tehingute väljundid, ja loob väljunditena uusi UTXOsid, mida saab kasutada sisenditena tulevastes tehingutes.

Iga sisend sisaldab viidet olemasolevale väljundile koos allkirja skriptiga (`scriptSig`), mis vastab kulutuste tingimustele (`scriptPubKey`), mis on kehtestatud väljundiga, millele ta viitab. See on see, mis võimaldab bitcoinide avamist. Väljundid määratlevad uued kulutamistingimused (`scriptPubKey`) ülekantud bitcoinide jaoks, sageli avaliku võtme või aadressi kujul, millega bitcoinid on nüüd seotud.