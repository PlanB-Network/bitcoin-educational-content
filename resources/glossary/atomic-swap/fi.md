---
termi: ATOMIC SWAP
---

Teknologia, joka mahdollistaa suorat kryptovaluuttojen vaihdot kahden osapuolen välillä ilman luottamuksen tarvetta ja ilman välittäjää. Näitä vaihtoja kutsutaan "atomisiksi", koska ne voivat päättyä vain kahteen tulokseen:
* Joko vaihto onnistuu, ja molemmat osapuolet ovat tehokkaasti vaihtaneet kryptovaluuttojaan;
* Tai vaihto epäonnistuu, ja molemmat osapuolet poistuvat alkuperäisine kryptovaluuttoineen.

Atomic Swapit voidaan suorittaa joko samalla kryptovaluutalla, jolloin sitä kutsutaan myös "*coinswapiksi*," tai eri kryptovaluuttojen välillä. Historiallisesti ne ovat perustuneet "Hash Time-Locked Contracts" (HTLC) -sopimuksiin, aikalukitusjärjestelmään, joka takaa vaihdon täydellisen suorittamisen tai täydellisen peruuntumisen, näin ollen säilyttäen osapuolten varojen eheyden. Tämä menetelmä vaati protokollia, jotka kykenivät käsittelemään sekä skriptejä että aikalukkoja. Viime vuosina suuntaus on kuitenkin siirtynyt *Adaptor Signatures* -menetelmän käyttöön. Tämän toisen lähestymistavan etuna on skriptien tarpeen poistaminen, mikä vähentää operatiivisia kustannuksia. Sen toinen merkittävä etu on, että se ei vaadi identtisen hashaamisen käyttöä molemmissa siirron osissa, mikä auttaa välttämään linkin paljastumisen niiden välillä.