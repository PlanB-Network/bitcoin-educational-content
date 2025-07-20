---
term: BIP0137
---

Proponuje znormalizowany format podpisywania wiadomości za pomocą kluczy prywatnych Bitcoin i powiązanych z nimi adresów, w celu udowodnienia Ownership Address. Ten BIP ma na celu rozwiązanie niejasności związanych z różnymi typami adresów Bitcoin (P2PKH, P2SH, P2WPKH...) podczas podpisywania wiadomości. Wprowadza on metodę wyraźnego rozróżniania tych formatów Address za pomocą podpisów. Podpisy te są przydatne w różnych zastosowaniach, takich jak dowód środków, audyt i inne zastosowania wymagające uwierzytelnienia Address za pomocą jego klucza prywatnego. Od tego czasu BIP322 wprowadził nowy format podpisu, który pozwala na rozszerzenie tego standardu i uogólnienie go dla dowolnego typu skryptu.