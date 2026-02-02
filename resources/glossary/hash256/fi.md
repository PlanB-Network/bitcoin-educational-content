---
term: HASH256

definition: Funktio, joka käyttää SHA256-algoritmiä kahdesti peräkkäin, käytetään useissa Bitcoin-sovelluksissa.
---
Bitcoinin eri sovelluksissa käytetty salausfunktio. Siinä SHA256-funktiota sovelletaan kahdesti syöttötietoihin. Viesti läpäisee SHA256:n kerran, ja tämän toiminnon tulosta käytetään syötteenä SHA256:n toisessa läpikäynnissä. Tämän toiminnon tulos on siis 256 bittiä.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$$