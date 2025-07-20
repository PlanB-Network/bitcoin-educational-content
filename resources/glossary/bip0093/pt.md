---
term: BIP0093
---

BIP informativo que sugere uma norma para guardar e restaurar o seed de uma carteira determinística hierárquica (de acordo com o BIP32) utilizando a partilha de chaves secretas de Shamir. Este protocolo define o formato "codex32", que se inspira no formato bech32, introduzindo uma cadeia estruturada constituída por um prefixo, um parâmetro de limiar, um identificador, um índice de partilha, uma carga útil e uma soma de controlo (BCH). O método permite que o seed seja dividido em até 31 partilhas, das quais é necessário um limiar definido (entre 1 e 9) para a recuperação total do seed.