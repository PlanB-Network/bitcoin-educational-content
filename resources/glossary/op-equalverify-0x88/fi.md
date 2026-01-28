---
term: OP_EQUALVERIFY (0X88)

definition: Yhdistää OP_EQUAL- ja OP_VERIFY-opcodet, mitätöiden siirron, jos arvot eroavat.
---
Yhdistää `OP_EQUAL`- ja `OP_VERIFY`-toiminnot. Se tarkistaa ensin pinossa olevien kahden ylimmän arvon yhdenvertaisuuden ja vaatii sitten, että tulos on nollasta poikkeava, muuten tapahtuma on virheellinen. `OP_EQUALVERIFY`:tä käytetään erityisesti osoitetarkistusskripteissä.