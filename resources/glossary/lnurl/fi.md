---
term: LNURL
---

Viestintäprotokolla, joka määrittelee joukon ominaisuuksia, jotka on suunniteltu yksinkertaistamaan Lightning-solmujen ja asiakkaiden sekä kolmansien osapuolten sovellusten välistä vuorovaikutusta. Tämä protokolla perustuu HTTP:hen, ja sen avulla voidaan luoda linkkejä erilaisia toimintoja, kuten maksupyyntöä, nostopyyntöä tai muita käyttäjäkokemusta parantavia toimintoja varten. Jokainen LNURL on bech32-koodattu URL-osoite, jonka etuliite on `lnurl` ja joka skannattaessa käynnistää joukon automaattisia toimintoja Lightning Wallet:ssa.


Esimerkiksi LNURL-withdraw (LUD-03) mahdollistaa varojen nostamisen palvelusta skannaamalla QR-koodia ilman manuaalista generate ja Invoice -toimintoa. Tai LNURL-auth (LUD-04) antaa sinun muodostaa yhteyden verkkopalveluihin käyttämällä Salaman Wallet yksityistä avainta salasanan sijasta.