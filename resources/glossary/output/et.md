---
term: OUTPUT

---
Bitcoini kontekstis viitab tehingu väljund UTXOdele (*Unspent Transaction Outputs*), mis on loodud makse sihtrahana. Täpsemalt öeldes on see mehhanism, mille abil tehing jaotab vahendeid.

Tehing võtab sisendina UTXOsid, st bitcoinide tükke, ja loob väljundina uusi UTXOsid. Need väljundid määravad kindlaks teatud hulga bitcoine, mis on sageli määratud konkreetsele aadressile, ning tingimused, mille alusel neid vahendeid saab hiljem kulutada. Bitcoini tehingu roll on seega tarbida UTXOsid kui sisendeid ja luua uusi UTXOsid kui väljundeid. Nende kahe erinevus vastab tehingutasudele, mida ploki võitnud kaevandaja saab sisse nõuda. UTXO on sisuliselt eelmise tehingu väljund, mida ei ole veel kulutatud. Tehingu väljundid on seega uute UTXOde loomine, mida omakorda saab potentsiaalselt kasutada tulevaste tehingute sisenditena.

Laiemalt vaadatuna viitab termin "väljund" andmetöötluses üldiselt funktsioonist, algoritmist või süsteemist tulenevatele andmetele. Näiteks kui andmed läbivad krüptograafilise hash-funktsiooni, nimetatakse seda teavet "sisendiks" ja tulemust "väljundiks"