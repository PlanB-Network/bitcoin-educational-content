---
term: BIP0386

definition: Funções tr() para descrever as saídas Taproot nos descriptors.
---
Introduz funções descritoras para o Taproot. Ele define as funções `tr(KEY)` e `tr(KEY, TREE)` para encontrar saídas Taproot, onde `KEY` é a chave interna e `TREE` é uma árvore opcional de caminhos de script. BIP386 foi implementado no Bitcoin Core versão 22.0.