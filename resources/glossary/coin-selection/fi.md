---
term: COIN SELECTION

---
Prosessi, jonka avulla Bitcoin-lompakko-ohjelmisto valitsee, mitä UTXO:ita käytetään syötteinä transaktion tuotosten täyttämiseksi. Kolikon valintamenetelmä on tärkeä, koska se vaikuttaa transaktion kustannuksiin ja käyttäjän yksityisyyteen. Usein pyritään minimoimaan käytettyjen syötteiden määrä, jotta transaktion kokoa ja siihen liittyviä maksuja voidaan pienentää, ja samalla pyritään säilyttämään yksityisyys välttämällä eri lähteistä peräisin olevien kolikoiden yhdistämistä (CIOH). Kolikoiden valintaan on olemassa useita menetelmiä, kuten *Knapsack Solver* tai *Branch-and-Bound*. Kun käyttäjä valitsee kolikon manuaalisesti, sitä kutsutaan *Kolikonvalvonnaksi*.

> ► *Englanniksi sitä kutsutaan nimellä "Coin Selection".*