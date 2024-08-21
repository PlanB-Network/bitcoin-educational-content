---
term: TEHING (TX)
---

Bitcoin'i kontekstis on tehing (lühendatult "TX") operatsioon, mis on salvestatud plokiahelasse ja mis kannab bitcoine ühelt või mitmelt sisendilt ühele või mitmele väljundile. Iga tehing tarbib kasutamata Tehingu Väljundeid (UTXOsid) sisenditena, mis on eelnevate tehingute väljundid, ja loob uued UTXOsid väljunditena, mida saab kasutada sisenditena tulevastes tehingutes.

Iga sisend sisaldab viidet olemasolevale väljundile koos allkirjastamise skriptiga (`scriptSig`), mis täidab väljundi poolt kehtestatud kulutamistingimused (`scriptPubKey`). See võimaldab bitcoinide vabastamist. Väljundid määratlevad üle kantud bitcoinidele uued kulutamistingimused (`scriptPubKey`), sageli avaliku võtme või aadressi kujul, millega bitcoinid nüüd seostatakse.