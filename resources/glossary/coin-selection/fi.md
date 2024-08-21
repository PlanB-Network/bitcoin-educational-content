---
termi: KOLIKONVALINTA
---

Prosessi, jonka avulla Bitcoin-lompakon ohjelmisto valitsee, mitkä UTXO:t käytetään syötteinä tyydyttämään transaktion tulosteet. Kolikonvalinnan menetelmä on tärkeä, koska sillä on seurauksia transaktion kustannuksiin ja käyttäjän yksityisyyteen. Se pyrkii usein minimoimaan käytettyjen syötteiden määrän, jotta transaktion koko ja siihen liittyvät maksut pienenevät, samalla yrittäen säilyttää yksityisyyden välttämällä eri lähteistä peräisin olevien kolikoiden yhdistämistä (CIOH). Kolikonvalintaan on olemassa useita menetelmiä, kuten *Knapsack Solver* tai *Branch-and-Bound*. Kun kolikonvalinta suoritetaan manuaalisesti käyttäjän toimesta, sitä kutsutaan “*Kolikon Hallinta*”.

> ► *Englanniksi sitä kutsutaan "Coin Selection".*