---
term: Lukitus (.lock)

definition: Tiedosto, joka estää useita Bitcoin Core -instansseja käyttämästä samaa hakemistoa samanaikaisesti.
---
Tiedosto, jota käytetään Bitcoin Coressa datahakemiston lukitsemiseen. Se luodaan, kun bitcoind tai Bitcoin-qt käynnistyy, jotta useat ohjelmiston instanssit eivät voi käyttää samaa datahakemistoa samanaikaisesti. Tavoitteena on estää ristiriidat ja tietojen korruptoituminen. Jos ohjelmisto pysähtyy odottamatta, .lock-tiedosto voi jäädä jäljelle, ja se on poistettava manuaalisesti ennen Bitcoin Coren uudelleenkäynnistämistä.