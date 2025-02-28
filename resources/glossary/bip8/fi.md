---
term: BIP8

---
BIP8 on pehmeän haarautumisen aktivointimenetelmä, joka on kehitetty SegWitistä käytyjen keskustelujen jälkeen, ja BIP8 on automaattinen UASF-mekanismi (*User-Activated Soft Fork*). BIP9:n tavoin BIP8 käyttää louhijoiden signalointia, mutta lisää siihen `LOT` (*Lock-in On Time out*) -parametrin. Jos "LOT"-parametrin arvoksi on asetettu "true", kun signalointijakso päättyy saavuttamatta vaadittua kynnysarvoa, UASF käynnistyy automaattisesti, mikä pakottaa soft forkin aktivoitumaan. Tämä lähestymistapa pakottaa louhijat yhteistyöhön tai vaarantaa käyttäjien määräämän UASF:n. Lisäksi toisin kuin BIP9:ssä, BIP8:ssa signaalijakso määritellään lohkon korkeuden perusteella, jolloin kaivostyöläiset eivät voi manipuloida hash-astetta. BIP8 mahdollistaa myös muuttuvan äänestyskynnyksen asettamisen ja ottaa käyttöön parametrin, joka määrittää aktivoinnin minimilohkokorkeuden, mikä antaa louhijoille aikaa valmistautua ja ilmoittaa suostumuksestaan etukäteen ilman, että he ovat välttämättä valmiita. Kun pehmeä haarautuminen aktivoidaan BIP8:n kautta parametrilla `LOT=true`, tämä käyttää hyvin aggressiivista menetelmää louhijoita vastaan, jotka joutuvat välittömästi mahdollisen UASF:n paineen alle. Se jättää heille vain kaksi vaihtoehtoa:


- Ole yhteistyökykyinen ja helpota siten aktivointiprosessia;
- Olla yhteistyöhaluton, jolloin käyttäjät suorittavat automaattisesti UASF:n pehmeän haarautumisen määräämiseksi.