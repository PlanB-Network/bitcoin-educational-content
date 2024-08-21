---
term: PIME ALLKIRI
---

Chaumi pimedad allkirjad on digitaalallkirja vorm, kus allkirja andja ei tea sõnumi sisu, millele ta allkirja annab. Siiski saab hiljem allkirja koos algse sõnumiga kontrollida. Selle tehnika töötas välja krüptograaf David Chaum 1983. aastal.

Võtame näiteks ettevõtte, kes soovib autentida konfidentsiaalset dokumenti, nagu leping, ilma selle sisu avaldamata. Ettevõte rakendab maskeerimisprotsessi, mis krüptograafiliselt muudab algdokumendi pöörduval viisil. See muudetud dokument saadetakse sertifitseerimisasutusele, kes rakendab pimeallkirja, teadmata aluseks olevat sisu. Pärast maskeeritud allkirjastatud dokumendi kättesaamist eemaldab ettevõte allkirja maskeeringu. Tulemuseks on algdokument, mille on autentinud asutuse allkiri, ilma et asutus oleks kunagi näinud algset sisu.

Seega võimaldavad Chaumi pimeallkirjad dokumendi autentsuse tõendamist ilma selle sisu teadmata, tagades nii kasutaja andmete konfidentsiaalsuse kui ka allkirjastatud dokumendi terviklikkuse.

Bitcoini puhul kasutatakse seda protokolli Chaumi pankade süsteemides kui pealiskihti (Cashu, Fedimint jne), kuid eriti Chaumi coinjoin protokollides, et tagada, et koordinaator ei suuda seostada sisendit väljundiga.