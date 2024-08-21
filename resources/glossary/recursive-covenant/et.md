---
term: REKURSIIVNE (KOVENANT)
---

Bitcoinis rekursiivne kovenant on tüüpi nutileping, mis seab tingimused mitte ainult praegusele tehingule, vaid ka tulevastele tehingutele, mis kulutavad selle tehingu väljundeid. See võimaldab luua tehingute ahelaid, kus igaüks peab järgima teatud reegleid, mille on määratlenud ahela esimene tehing. Rekursiivsus loob tehingute jada, kus igaüks pärib piirangud oma vanemtehingult. See võimaldaks keerukat ja pikaajalist kontrolli selle üle, kuidas bitcoine saab kulutada, kuid see tooks kaasa ka riske seoses kulutamisvabaduse ja fungibiliteediga.

Kokkuvõttes piiraks mitterekursiivne kovenant ennast ainult vahetult järgneva tehinguga, mis on reeglite kehtestamise tehing. Seevastu rekursiivne kovenant omab võimet kehtestada kindlad tingimused bitcoinile lõputult. Tehingud võivad üksteisele järgneda, kuid küsimuse all olev bitcoin säilitab alati sellele alguses lisatud tingimused. Tehniliselt toimub mitterekursiivse kovenandi loomine, kui UTXO `scriptPubKey` määratleb piirangud tehingu `scriptPubKey` väljunditele, mis kulutab nimetatud UTXO. Teisest küljest toimub rekursiivse kovenandi loomine, kui UTXO `scriptPubKey` määratleb piirangud tehingu `scriptPubKey` väljunditele, mis kulutab nimetatud UTXO, ja kõikidele `scriptPubKey`dele, mis järgnevad selle UTXO kulutamisele.

Üldisemalt arvutiteaduses nimetatakse "rekursiivsuseks" funktsiooni võimet kutsuda iseennast, luues omamoodi tsükli.