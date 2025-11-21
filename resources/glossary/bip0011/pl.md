---
term: BIP0011
---

BIP wprowadzony przez Gavina Andresena w marcu 2012 r., który proponuje standardową metodę tworzenia transakcji z wieloma podpisami na Bitcoin. Propozycja ta ma na celu zwiększenie bezpieczeństwa bitcoinów poprzez wymaganie wielu podpisów do walidacji transakcji. BIP11 wprowadza nowy typ skryptu, nazwany "M-of-N Multisig", gdzie `M` reprezentuje minimalną liczbę wymaganych podpisów spośród `N` potencjalnych kluczy publicznych. Standard ten wykorzystuje opcode `OP_CHECKMULTISIG`, istniejący już w Bitcoin, ale który nie był wcześniej zgodny z zasadami standaryzacji węzłów. Chociaż ten typ skryptu nie jest już powszechnie używany w rzeczywistych portfelach Multisig, preferując P2SH lub P2WSH, jego użycie pozostaje możliwe. Jest on w szczególności używany w meta-protokołach, takich jak Stamps. Węzły mogą jednak nie przekazywać tych transakcji P2MS z parametrem `permitbaremultisig=0`.


> obecnie standard ten znany jest jako "bare-Multisig" lub "P2MS"