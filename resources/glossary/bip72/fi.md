---
term: BIP72

---
Täydentää BIP70:n ja BIP71:n määrittelemällä Bitcoin URI:n laajennuksen (BIP21) lisäparametrilla "r". Tämän parametrin avulla voidaan sisällyttää linkki suojattuun maksupyyntöön, joka on allekirjoitettu kauppiaan SSL-sertifikaatilla. Kun asiakas napsauttaa tätä laajennettua URI:tä, hänen lompakkonsa ottaa yhteyttä kauppiaan palvelimeen ja pyytää maksutietoja. Nämä tiedot täytetään automaattisesti lompakon tapahtumaliittymässä, ja asiakkaalle voidaan ilmoittaa, että hän maksaa allekirjoitusvarmenteen mukaista verkkotunnusta vastaavalle verkkotunnuksen omistajalle (esimerkiksi "pandul.fr"). Koska tämä parannus sisältyy BIP70:ään, sitä ei ole koskaan otettu laajasti käyttöön.