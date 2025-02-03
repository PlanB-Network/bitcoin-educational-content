---
term: REKURSIIVNE (LEPING)

---
Bitcoini rekursiivne leping on teatud tüüpi arukas leping, mis seab tingimused mitte ainult praegusele tehingule, vaid ka tulevastele tehingutele, mis kulutavad selle tehingu väljundid. See võimaldab luua tehinguahelaid, kus iga tehing peab järgima teatavaid reegleid, mis on määratletud ahela esimese tehingu poolt. Rekursiivsus loob tehingute jada, kus iga tehing pärib piirangud oma vanemtehingult. See võimaldaks keerulist ja pikaajalist kontrolli selle üle, kuidas bitcoine saab kulutada, kuid see tooks kaasa ka riske seoses kulutamisvabaduse ja asendatavusega.

Kokkuvõtvalt võib öelda, et mitterekursiivne kokkulepe piirduks ainult selle tehinguga, mis järgneb vahetult sellele, millega eeskirjad kehtestati. Seevastu rekursiivne leping on võimeline kehtestama bitcoin'ile konkreetseid tingimusi lõpmatult. Tehingud võivad üksteisele järgneda, kuid kõnealusele bitcoinile jäävad alati algsed tingimused. Tehniliselt toimub mitterekursiivse lepingu kehtestamine siis, kui UTXO `scriptPubKey` määratleb piirangud UTXOd kulutava tehingu väljundite `scriptPubKey` jaoks. Teisalt, rekursiivse lepingu kehtestamine toimub siis, kui UTXO "scriptPubKey" määratleb piirangud selle UTXO kulutava tehingu väljundite "scriptPubKey" ja kõigi UTXO kulutamisele järgnevate "scriptPubKey`de" suhtes.

Üldisemalt on arvutuses nn "rekursiivsus" funktsiooni võime kutsuda iseennast, luues omamoodi tsükli.