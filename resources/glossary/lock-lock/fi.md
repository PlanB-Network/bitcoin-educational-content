---
termi: LOCK (.LOCK)
---

Tiedosto, jota käytetään Bitcoin Core:ssa datadirektorion lukitsemiseen. Se luodaan, kun bitcoind tai Bitcoin-qt käynnistetään estämään useiden ohjelmistoinstanssien samanaikainen pääsy samaan datadirektorioon. Tavoitteena on estää ristiriidat ja datan korruptoituminen. Jos ohjelmisto pysähtyy odottamatta, .lock-tiedosto voi jäädä jäljelle ja se on poistettava manuaalisesti ennen Bitcoin Core:n uudelleenkäynnistystä.