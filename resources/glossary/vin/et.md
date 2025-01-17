---
term: VIN

---
Bitcoini tehingu konkreetne element, mis määrab kindlaks väljundite rahuldamiseks kasutatud rahaliste vahendite allika. Iga `vin` viitab eelmise tehingu kasutamata väljundile (UTXO). Tehing võib sisaldada mitut sisendit, millest igaüks on identifitseeritud kombinatsiooniga `txid` (algse tehingu identifikaator) ja `vout` (selle tehingu väljundi indeks).

Iga `vin` sisaldab järgmist teavet:


- `txid`: eelmise tehingu identifikaator, mis sisaldab siin sisendina kasutatavat väljundit;
- `vout`: eelmise tehingu väljundi indeks;
- `scriptSig` või `scriptWitness`: lukustamisskript, mis esitab vajalikud andmed, et täita eelmise tehingu, mille raha kulutatakse, `scriptPubKey` poolt esitatud tingimusi, tavaliselt krüptograafilise allkirja andmisega;
- `nSequence`: konkreetne väli, mida kasutatakse, et näidata, kuidas see sisend on ajaliselt lukustatud, samuti muud valikud nagu RBF.