---
termi: BIP72
---

Täydentää BIP70:n ja BIP71:n määrittelemällä Bitcoin URI:n (BIP21) laajennuksen lisäparametrilla `r`. Tämä parametri mahdollistaa linkin sisällyttämisen turvalliseen maksupyyntöön, jonka on allekirjoittanut kauppiaan SSL-sertifikaatti. Kun asiakas klikkaa tätä laajennettua URI:a, heidän lompakkonsa ottaa yhteyttä kauppiaan palvelimeen pyytääkseen maksutietoja. Nämä tiedot täytetään automaattisesti lompakon maksuliittymään, ja asiakas voidaan informoida, että he maksavat domainin omistajalle, joka vastaa allekirjoittavaa sertifikaattia (esimerkiksi "pandul.fr"). Koska tämä parannus on niputettu BIP70:n kanssa, sitä ei ole koskaan laajasti omaksuttu.