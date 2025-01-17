---
term: PSBT

---
Lyhenne sanoista "Partially Signed Bitcoin Transaction". Se on BIP174:n myötä käyttöön otettu määrittely, jonka tarkoituksena on standardoida tapa, jolla keskeneräiset transaktiot muodostetaan Bitcoiniin liittyvissä ohjelmistoissa, kuten lompakko-ohjelmistoissa. PSBT kiteyttää transaktion, jonka syötteet eivät välttämättä ole täysin allekirjoitettuja. Se sisältää kaikki tarvittavat tiedot, jotta osallistuja voi allekirjoittaa transaktion ilman lisätietoja. Näin ollen PSBT voi olla kolmessa eri muodossa:


- Täysin valmis liiketoimi, jota ei ole vielä allekirjoitettu;
- Osittain allekirjoitettu tapahtuma, jossa osa syötteistä on allekirjoitettu, mutta osa ei ole vielä allekirjoitettu;
- Tai täysin allekirjoitettu Bitcoin-tapahtuma, joka voidaan muuntaa valmiiksi lähetettäväksi verkossa.

PSBT-muoto helpottaa eri lompakko-ohjelmistojen ja allekirjoituslaitteiden (laitteistolompakot) välistä yhteentoimivuutta. Tällä hetkellä käytetään PSBT:n versiota 0, joka on määritelty BIP174:ssä, mutta versiota 2 ehdotetaan BIP370:ssä.

> ► * PSBT:n versiota 1 ei ole olemassa. Koska versio 0 oli ensimmäinen versio, toista versiota kutsuttiin epävirallisesti versioksi 2. Ava Chow, joka laati BIP370:n, päätti antaa tälle uudelle versiolle numeron 2 sekaannusten välttämiseksi.* *