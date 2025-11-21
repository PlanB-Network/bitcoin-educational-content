---
term: PUT OPORAVKA
---

U softveru Wallet koji koristi Miniscript, kao što je na primer Liana, putanje oporavka odnose se na skupove ključeva koji postaju operativni tek nakon definisanog perioda neaktivnosti u skripti koja zaključava bitkoine (timelock). Putanje oporavka su upotrebljive samo kada timelock istekne, čime se nudi metoda za oporavak sredstava kada primarna putanja nije dostupna. Razmotrite primer skripte koja uključuje 2 različita ključa: ključ A, koji omogućava trenutno trošenje bitkoina, i ključ B, koji omogućava njihovo trošenje nakon kašnjenja definisanog timelock-om od 52,560 blokova. U ovom primeru, ključ A dolazi iz primarne putanje, dok ključ B dolazi iz putanje oporavka.