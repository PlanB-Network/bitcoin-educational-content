---
term: OBJECTIVO

---
Nas carteiras determinísticas e hierárquicas (HD), o objetivo (ou _purpose_ em inglês), definido pela BIP43, representa um nível específico de derivação. Este índice, localizado na primeira profundidade da árvore de derivação (`m / purpose' /`), identifica o padrão de derivação adotado pela carteira, de forma a facilitar a compatibilidade entre diferentes softwares de gestão de carteiras. Por exemplo, no caso de endereços SegWit (BIP84), o objetivo é anotado como `/84'/`. Este método permite a organização eficiente de chaves entre diferentes tipos de endereços dentro da mesma carteira HD. Os índices padrão utilizados são:


- Para P2PKH: `44'`;
- Para P2WPKH-aninhado-em-P2SH: `49'`;
- Para P2WPKH: `84'`;
- Para P2TR: `86'`.

![](../../dictionnaire/assets/20.webp)