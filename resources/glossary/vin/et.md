---
term: VIN
---

Bitcoin tehingu konkreetne element, mis määratleb vahendite allika, mida kasutatakse väljundite rahuldamiseks. Iga `vin` viitab eelmisest tehingust pärit kulutamata väljundile (UTXO). Tehing võib sisaldada mitut sisendit, millest igaüht tuvastatakse kombinatsiooniga `txid` (algse tehingu identifikaator) ja `vout` (väljundi indeks selles tehingus).

Iga `vin` sisaldab järgmist teavet:
* `txid`: eelmise tehingu identifikaator, mis sisaldab siin sisendina kasutatavat väljundit;
* `vout`: väljundi indeks eelmises tehingus;
* `scriptSig` või `scriptWitness`: avamisskript, mis pakub vajalikke andmeid eelmise tehingu `scriptPubKey` poolt esitatud tingimuste rahuldamiseks, tavaliselt pakkudes krüptograafilist allkirja;
* `nSequence`: konkreetne väli, mida kasutatakse selle sisendi ajalise lukustuse näitamiseks, samuti muude valikute nagu RBF näitamiseks.