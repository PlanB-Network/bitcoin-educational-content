---
termo: BIP49
---

BIP49 é um BIP informativo que introduz o método de derivação usado para gerar endereços Nested SegWit em uma carteira HD. O caminho de derivação proposto segue os padrões do BIP43 e BIP44, com o índice `49'` (derivação reforçada) na profundidade do objetivo. Por exemplo, o primeiro endereço de uma conta P2SH-P2WPKH seria derivado do caminho: `m/49'/0'/0'/0/0`. Scripts Nested SegWit foram inventados no lançamento do SegWit para facilitar sua adoção. Eles permitem o uso deste novo padrão, mesmo em carteiras que ainda não são nativamente compatíveis com SegWit.