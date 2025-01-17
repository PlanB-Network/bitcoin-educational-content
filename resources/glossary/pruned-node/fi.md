---
term: PRUNED NODE

---
Karsittu solmu, englanniksi "Pruned Node", on täysi solmu, joka suorittaa lohkoketjun karsinnan. Tämä tarkoittaa vanhimpien lohkojen asteittaista poistamista sen jälkeen, kun ne on asianmukaisesti todennettu, jotta vain uusimmat lohkot säilyvät. Säilytysraja määritetään `bitcoin.conf`-tiedostossa parametrilla `prune=n`, jossa `n` on lohkojen enimmäiskoko megatavuina (MB). Jos tämän parametrin perään merkitään `0`, karsinta poistetaan käytöstä ja solmu säilyttää lohkoketjun kokonaisuudessaan.

Karsittuja solmuja pidetään joskus erityyppisinä solmuina kuin kokonaisia solmuja. Karsittujen solmujen käyttö voi olla erityisen kiinnostavaa käyttäjille, joilla on rajoituksia tallennuskapasiteetissa. Tällä hetkellä täydellä solmulla on oltava lähes 600 gigatavua pelkästään lohkoketjun tallentamista varten. Karsittu solmu voi rajoittaa tarvittavan tallennustilan jopa 550 megatavuun. Vaikka karsittu solmu käyttää vähemmän levytilaa, se säilyttää samantasoisen verifioinnin ja validoinnin kuin täysi solmu. Näin ollen karsitut solmut tarjoavat käyttäjilleen enemmän luottamusta kevyisiin solmuihin (SPV) verrattuna.