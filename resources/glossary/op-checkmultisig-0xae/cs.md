---
term: OP_CHECKMULTISIG (0XAE)

---
Kontroluje více podpisů proti více veřejným klíčům. Jako vstup přijímá sérii `N` veřejných klíčů a `M` podpisů, kde `M` může být menší nebo rovno `N`. `OP_CHECKMULTISIG` ověří, zda alespoň `M` podpisů odpovídá `M` z `N` veřejných klíčů. Všimněte si, že kvůli historické chybě off-by-one odstraňuje `OP_CHECKMULTISIG` ze zásobníku další prvek. Tento prvek se nazývá "*dummy element*". Aby se předešlo chybě ve `scriptSig`, je proto zahrnut `OP_0`, což je zbytečný prvek, který vyhovuje odstranění a chybu obchází. Od BIP147 (zavedeného se SegWitem v roce 2017) musí být zbytečný prvek spotřebovaný kvůli chybě `OP_0`, aby byl skript platný, protože se jednalo o vektor malleability. Tento opkód byl v Tapscriptu odstraněn.