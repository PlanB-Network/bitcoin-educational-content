---
term: BIP0384
---

Wprowadza funkcję `combo(KEY)` dla deskryptorów. Funkcja ta opisuje zestaw możliwych skryptów wyjściowych dla danego klucza publicznego. W ten sposób obejmuje wiele typów skryptów jednocześnie, w tym P2PK, P2PKH, P2WPKH i P2SH-P2WPKH. Jeśli dany klucz jest skompresowany, testowane są wszystkie 4 typy skryptów, a jeśli nie jest, testowane są tylko 2 typy skryptów Legacy. Celem jest uproszczenie reprezentacji kluczy w deskryptorach poprzez zapewnienie jednej metody generate dla różnych wariantów skryptów wyjściowych opartych na tym samym kluczu publicznym. BIP384 został zaimplementowany wraz ze wszystkimi innymi BIP-ami związanymi z deskryptorami (z wyjątkiem BIP386) w wersji 0.17 Bitcoin Core.