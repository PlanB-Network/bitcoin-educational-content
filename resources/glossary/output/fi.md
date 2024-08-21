---
termi: OUTPUT
---

Bitcoinin kontekstissa tapahtuman output viittaa UTXOihin (*Käyttämättömät Tapahtumaoutputit*), jotka luodaan maksun kohderahastoksi. Tarkemmin sanottuna se on mekanismi, jonka kautta tapahtuma jakaa varoja.

Tapahtuma ottaa UTXOja, eli bitcoineja, syötteiksi ja luo uusia UTXOja outputeiksi. Nämä outputit määrittävät tietyn määrän bitcoineja, usein tietylle osoitteelle osoitettuna, sekä ehdot, joiden mukaisesti näitä varoja voidaan myöhemmin käyttää. Bitcoin-tapahtuman rooli on siis kuluttaa UTXOja syötteinä ja luoda uusia UTXOja outputeina. Näiden kahden ero vastaa tapahtumamaksuja, jotka voittava louhija voi kerätä lohkosta. UTXO on perimmiltään edellisen tapahtuman output, jota ei ole vielä käytetty. Tapahtumaoutputit ovat siis uusien UTXOjen luomisia, jotka puolestaan mahdollisesti käytetään syötteinä tulevissa tapahtumissa.

Laajemmasta näkökulmasta tietotekniikassa termi "output" viittaa yleensä funktion, algoritmin tai järjestelmän tuottamaan dataan. Esimerkiksi kun dataa syötetään kryptografiseen hajautusfunktioon, tätä tietoa kutsutaan "syötteeksi", ja tulos nimetään "outputiksi".