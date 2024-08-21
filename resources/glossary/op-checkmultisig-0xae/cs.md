---
term: OP_CHECKMULTISIG (0XAE)
---

Prověřuje více podpisů proti více veřejným klíčům. Jako vstup bere sérii `N` veřejných klíčů a `M` podpisů, kde `M` může být menší nebo rovno `N`. `OP_CHECKMULTISIG` ověřuje, zda alespoň `M` podpisů odpovídá `M` z `N` veřejných klíčů. Poznamenejme, že kvůli historické chybě off-by-one je `OP_CHECKMULTISIG` odstraněn zásobníkem další prvek. Tento prvek se nazývá "*dummy element*" (falešný prvek). Aby se předešlo chybě ve `scriptSig`, je proto zahrnut `OP_0`, který je zbytečným prvkem, aby se uspokojilo odstranění a obešlo chybu. Od BIP147 (zavedeného s SegWit v roce 2017) musí být zbytečný prvek spotřebovaný kvůli chybě `OP_0`, aby byl skript platný, jelikož to byl vektor mutability. Tento operační kód byl odstraněn v Tapscript.