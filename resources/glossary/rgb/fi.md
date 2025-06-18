---
term: RGB
---

Hajautettu, luottamuksellinen Smart contract-järjestelmä, joka on suunniteltu toimimaan yhdessä Bitcoin:n ja Lightning Network:n kanssa. RGB toimii Client-side Validation-mallilla ja erottaa Contract State:n tallennuksen Blockchain:stä niin, että siinä säilytetään vain kryptografisia sitoumuksia. Näin koko tilahistoria säilytetään ketjun ulkopuolella, mikä mahdollistaa paremman skaalautuvuuden ja luottamuksellisuuden. RGB mahdollistaa siten monimutkaisten sopimusten luomisen tokenien, NFT:iden, hajautettujen identiteettien tai DeFi-ratkaisujen tallentamiseksi suoraan Bitcoin:n päälle.


RGB:ssa Double-spending:n vastustuskyky varmistetaan käyttämällä Single-Use Seal:ää, joka on salausmekanismi, jossa hyödynnetään sitä, että Bitcoin:n UTXO:ta voidaan käyttää vain kerran. Merkkien aitouden takaa asiakkaan puolelta tehtävä tilahistorian todentaminen Contract:n luomisesta sen viimeisimpään tilaan.