---
term: State Transition
---

RGB-protokollassa State Transition on toiminto, jota käytetään Contract:n tilan muuttamiseen uuteen kokoonpanoon. Se voi muuttaa sekä Global State:n että Owned States -tietoja. Jokainen siirtymä tarkistetaan tarkasti Contract:n Schema:ssa määriteltyjen sääntöjen mukaisesti, mikä takaa, että muutokset ovat Genesis:ssä asetettujen rajoitusten mukaisia. Tämä toiminto on ankkuroitu Blockchain Bitcoin:een Commitment:n kautta.