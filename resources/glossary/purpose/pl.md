---
term: CEL
---

W portfelach deterministycznych i hierarchicznych (HD) cel, zdefiniowany przez BIP43, reprezentuje określony poziom derywacji. Indeks ten, znajdujący się na pierwszej głębokości drzewa derywacji (`m / purpose' /`), identyfikuje standard derywacji przyjęty przez portfel, aby ułatwić kompatybilność między różnymi programami do zarządzania portfelem. Na przykład, w przypadku adresów SegWit (BIP84), cel jest oznaczony jako `/84'/`. Ta metoda umożliwia efektywne organizowanie kluczy między różnymi typami Address w ramach jednego portfela HD. Standardowe używane indeksy to :




- Dla P2PKH: `44'` ;
- Dla P2WPKH zagnieżdżonego w P2SH: `49'` ;
- Dla P2WPKH: `84'` ;
- Dla P2TR: `86'`.