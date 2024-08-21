---
termi: KNAPSACK SOLVER
---

Vanha menetelmä, jota käytettiin kolikoiden valintaan Bitcoin Core -lompakossa ennen versiota 0.17. Knapsack Solver yrittää ratkaista kolikoiden valintaongelman iteratiivisesti ja satunnaisesti valitsemalla UTXO:ja ja lisäämällä ne osajoukoiksi, tavoitteenaan minimoida siirtomaksut ja siirron koko. Tämä menetelmä on sittemmin korvattu *Branch-and-Bound* -menetelmällä.