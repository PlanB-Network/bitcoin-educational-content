---
term: ATOMIVAIHTOEHTO

---
Teknologia, joka mahdollistaa kryptovaluuttojen suoran vaihdon kahden osapuolen välillä ilman luottamusta ja ilman välittäjää. Näitä vaihtoja kutsutaan "atomisiksi", koska ne voivat johtaa vain kahteen lopputulokseen:


- Joko vaihto onnistuu, ja molemmat osallistujat ovat tosiasiallisesti vaihtaneet kryptovaluuttansa;
- Tai vaihto epäonnistuu, ja molemmat osallistujat lähtevät alkuperäiset kryptovaluuttansa mukanaan.

Atomic Swaps voidaan tehdä joko saman kryptovaluutan kanssa, jolloin sitä kutsutaan myös "*coinswapiksi*", tai eri kryptovaluuttojen välillä. Historiallisesti ne perustuivat "Hash Time-Locked Contracts" (HTLC) - aikalukitusjärjestelmään, joka takaa vaihdon loppuunsaattamisen tai täydellisen peruuttamisen ja säilyttää näin osapuolten varojen koskemattomuuden. Tämä menetelmä vaati protokollia, jotka pystyvät käsittelemään sekä skriptejä että aikalukkoja. Viime vuosina suuntaus on kuitenkin siirtynyt kohti *Adaptor-allekirjoitusten* käyttöä. Tämän jälkimmäisen lähestymistavan etuna on se, että skriptejä ei tarvita, mikä vähentää toimintakustannuksia. Sen toinen merkittävä etu on se, että se ei edellytä identtisen hashingin käyttöä tapahtuman molemmissa osissa, mikä auttaa välttämään niiden välisen yhteyden paljastumisen.