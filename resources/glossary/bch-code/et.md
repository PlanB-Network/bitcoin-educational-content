---
term: BCH CODE
---

Veakorrektsioonikoodide klass, mida kasutatakse andmejada vigade avastamiseks ja parandamiseks. Teisisõnu kasutatakse BCH veakorrektsioonikoode juhuslike vigade leidmiseks ja parandamiseks edastatavas teabes, et tagada selle jõudmine sihtkohta tervena. Lühend "BCH" tähistab nende koodide leiutajate nimede algustähti: Bose, Ray-Chaudhuri ja Hocquenghem.


Seda vahendit kasutatakse paljudes arvutivaldkondades, sealhulgas SSD-d, DVD-d ja QR-koodid. Näiteks on tänu nendele veakorrigeerivatele koodidele isegi siis, kui QR-kood on osaliselt kaetud, võimalik selle kodeeritud teave ikkagi kätte saada.


Bitcoin osana kasutatakse BCH-koode Bech32 ja Bech32m (pärast SegWit) Address vormingus kontrollsummana. Need kujutavad endast paremat kompromissi kontrollsumma suuruse ja vigade tuvastamise võime vahel kui lihtsad Hash funktsioonid, mida varem kasutati Legacy-aadressidel. Bitcoin kontekstis kasutatakse BCH-koode ainult vigade tuvastamiseks, mitte veaparanduseks. Seega tuvastab Bitcoin portfelli tarkvara kõik vead vastuvõtvas Address-s ja teatab neist kasutajale, kuid ei muuda automaatselt vale Address-d. See valik on tingitud asjaolust, et veaparanduse integreerimine mõjutab paratamatult algoritmi veatuvastamisvõimet.