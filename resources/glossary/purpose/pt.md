---
term: OBJECTIVO
---

Nas carteiras determinísticas e hierárquicas (HD), o objetivo, definido pela BIP43, representa um nível de derivação específico. Este índice, localizado na primeira profundidade da árvore de derivação (`m / purpose' /`), identifica o padrão de derivação adotado pela carteira, para facilitar a compatibilidade entre diferentes softwares de gestão de carteiras. Por exemplo, no caso dos endereços SegWit (BIP84), a finalidade é anotada como `/84'/`. Este método permite que as chaves sejam organizadas de forma eficiente entre diferentes tipos de Address dentro de uma única carteira HD. Os índices padrão utilizados são :




- Para P2PKH: `44'` ;
- Para P2WPKH aninhado em P2SH: `49'` ;
- Para P2WPKH: `84'` ;
- Para P2TR: `86'`.