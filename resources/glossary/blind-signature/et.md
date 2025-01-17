---
term: PIME ALLKIRI

---
Chaumi pimedad allkirjad on digitaalallkirja vorm, mille puhul allkirja andja ei tea allkirjastatava sõnumi sisu. Allkirja saab aga hiljem kontrollida originaalsõnumiga. Selle tehnika töötas 1983. aastal välja krüptograaf David Chaum.

Võtame näiteks ettevõtte, kes soovib autentida konfidentsiaalset dokumenti, näiteks lepingut, paljastamata selle sisu. Ettevõte rakendab maskeerimisprotsessi, mis muudab originaaldokumenti krüptograafiliselt ja pöördvõrreldes. See muudetud dokument saadetakse sertifitseerimisasutusele, kes annab pimesi allkirja, teadmata selle sisu. Pärast maskeeritud allkirjastatud dokumendi kättesaamist tühistab ettevõte allkirja maskeeringu. Tulemuseks on originaaldokument, mis on autenditud asutuse allkirjaga, ilma et asutus oleks kunagi näinud algset sisu.

Seega võimaldavad Chaumi pimedad allkirjad dokumendi autentsuse tõendamist ilma selle sisu tundmata, tagades nii kasutaja andmete konfidentsiaalsuse kui ka allkirjastatud dokumendi terviklikkuse.

Bitcoinis kasutatakse seda protokolli Chaumian pankade süsteemides ülekandena (Cashu, Fedimint jne), kuid eriti Chaumian coinjoin-protokollides, et tagada, et koordinaator ei saa sisendit väljundiga siduda.