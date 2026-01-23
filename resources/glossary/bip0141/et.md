---
term: BIP0141

definition: SegWiti (Segregated Witness) rakendamine, mis eraldab allkirjad ülejäänud tehingust, et lahendada muutlikkuse (malleability) probleem.
---
Tutvustas SegWit (Segregated Witness) kontseptsiooni, mis andis nime SegWit soft fork'ile. BIP141 kehtestab Bitcoini protokolli olulise muudatuse, mille eesmärk on lahendada tehingu võltsitavuse probleem. SegWit eraldab tunnistaja (allkirjaandmed) ülejäänud tehinguandmetest. See eraldamine saavutatakse tunnistajate lisamisega eraldi andmestruktuuri, mis on kinnitatud uues Merkle-puus, millele omakorda viidatakse plokis coinbase'i tehingu kaudu, mis muudab SegWit'i ühilduvaks protokolli vanemate versioonidega.