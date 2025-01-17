---
term: BIP49

---
BIP49 é um BIP informativo que introduz o método de derivação usado para gerar endereços SegWit aninhados numa carteira HD. O caminho de derivação proposto segue os padrões do BIP43 e BIP44, com o índice `49'` (derivação reforçada) na profundidade do objetivo. Por exemplo, o primeiro endereço de uma conta P2SH-P2WPKH seria derivado do caminho: `m/49'/0'/0'/0/0`. Os scripts SegWit aninhados foram inventados no lançamento do SegWit para facilitar a sua adoção. Eles permitem o uso deste novo padrão, mesmo em carteiras que ainda não são nativamente compatíveis com o SegWit.