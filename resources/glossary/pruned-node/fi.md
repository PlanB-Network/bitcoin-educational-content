---
termi: PRUNED NODE
---

Pruned node, suomeksi "Karsittu solmu", on täysi solmu, joka suorittaa lohkoketjun karsimisen. Tämä tarkoittaa vanhimpien lohkojen asteittaista poistamista niiden asianmukaisen tarkistamisen jälkeen, jättäen jäljelle vain uusimmat lohkot. Säilytysraja määritetään `bitcoin.conf`-tiedostossa `prune=n`-parametrin kautta, missä `n` on lohkojen maksimikoko megatavuina (MB). Jos tämän parametrin jälkeen on merkitty `0`, karsiminen on poistettu käytöstä, ja solmu säilyttää lohkoketjun kokonaisuudessaan.

Karsittuja solmuja pidetään joskus eri tyyppisinä solmuina verrattuna täysiin solmuihin. Karsitun solmun käyttö voi olla erityisen kiinnostavaa käyttäjille, jotka kohtaavat tallennuskapasiteetin rajoituksia. Tällä hetkellä täyden solmun on oltava lähes 600 GB vain lohkoketjun tallentamiseen. Karsittu solmu voi rajoittaa tarvittavan tallennustilan jopa 550 MB:iin. Vaikka se käyttää vähemmän levytilaa, karsittu solmu ylläpitää samanlaista varmennus- ja validointitasoa kuin täysi solmu. Karsitut solmut tarjoavat siis enemmän luottamusta käyttäjilleen verrattuna kevyisiin solmuihin (SPV).