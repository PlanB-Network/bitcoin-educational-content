---
term: OP_CHECKMULTISIG (0XAE)
---

Proverava više potpisa u odnosu na više javnih ključeva. Kao ulaz uzima niz od `N` javnih ključeva i `M` potpisa, gde `M` može biti manje ili jednako `N`. `OP_CHECKMULTISIG` proverava da li se najmanje `M` potpisa poklapa sa `M` od `N` javnih ključeva. Imajte na umu da zbog istorijske greške za jedan, `OP_CHECKMULTISIG` uklanja dodatni element sa steka. Ovaj element se naziva "*dummy element*". Da bi se izbegla greška u `scriptSig`, `OP_0`, koji je beskoristan element, je stoga uključen da zadovolji uklanjanje i zaobiđe grešku. Od BIP147 (uveden sa SegWit 2017. godine), beskorisni element koji se troši zbog greške mora biti `OP_0` da bi skripta bila validna, jer je to bila vektorska malleabilnost. Ovaj opcode je uklonjen u Tapscript.