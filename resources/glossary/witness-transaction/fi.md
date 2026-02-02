---
term: Todistaja-siirto
definition: RGBssä Bitcoin-rahansiirto, joka sulkee Single-use Sealin vahvistaakseen sopimuksen tilan on-chain.
---

RGB-protokollassa Witness Transaction viittaa Bitcoin-transaktioon, joka sulkee Single-Use Seal:n Multi Protocol Commitment:n sisältävän sanoman ympärille (MPC). Tämä operaatio koostuu joko olemassa olevan UTXO:n käyttämisestä tai uuden UTXO:n luomisesta, jotta protokollaan kirjoitettu sopimus Commitment voidaan lukita. Witness Transaction on siis On-Chain todiste siitä, että RGB Contract:n tila on vahvistettu tiettynä ajankohtana.