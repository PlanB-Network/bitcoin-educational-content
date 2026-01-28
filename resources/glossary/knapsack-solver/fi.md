---
term: Knapsack solver

definition: Vanha kolikonvalintamenetelmä Bitcoin Coressa, korvattu Branch-and-Bound-menetelmällä.
---
Vanha menetelmä, jota käytettiin kolikoiden valintaan Bitcoin Core -lompakossa ennen versiota 0.17. Knapsack Solver yrittää ratkaista kolikonvalintaongelman valitsemalla iteratiivisesti ja satunnaisesti UTXO:t ja laskemalla ne yhteen osajoukoittain tavoitteena minimoida maksut ja transaktion koko. Tämä menetelmä on sittemmin korvattu *Branch-and-Bound*-menetelmällä.