---
term: SECP256K1
---

Nazwa nadana konkretnej krzywej eliptycznej używanej w protokole Bitcoin do implementacji algorytmów podpisu cyfrowego ECDSA (*Elliptic Curve Digital Signature Algorithm*) i Schnorr. Krzywa `secp256k1` została wybrana przez twórcę Bitcoin, Satoshi Nakamoto. Ma ona kilka interesujących właściwości, w szczególności korzyści w zakresie wydajności.


Użycie `secp256k1` w Bitcoin oznacza, że każdy klucz prywatny (losowa 256-bitowa liczba) jest mapowany na odpowiadający mu klucz publiczny poprzez dodanie i podwojenie punktu klucza prywatnego przez punkt generatora krzywej `secp256k1`. Ta operacja jest łatwa do wykonania w jednym kierunku, ale praktycznie niemożliwa do odwrócenia, co stanowi podstawę bezpieczeństwa podpisów cyfrowych na Bitcoin.


Krzywa `secp256k1` jest określona przez równanie krzywej eliptycznej $y^2 = x^3 + 7$, co oznacza, że ma współczynniki $a$ równe $0$ i $b$ równe $7$ w ogólnej postaci równania krzywej eliptycznej $y^2 = x^3 + ax + b$. `secp256k1` jest zdefiniowana na skończonym polu, którego rząd jest bardzo dużą liczbą pierwszą, konkretnie $p = 2^{256} - 2^{32} - 977$. Krzywa ma również porządek grupy, który jest liczbą odrębnych punktów na krzywej, predefiniowany punkt generatora (lub punkt $G$), który jest używany w operacjach kryptograficznych do par kluczy generate, oraz kofaktor równy $1$.


> *"SEC" oznacza "Standards for Efficient Cryptography". "P256" oznacza, że krzywa jest zdefiniowana na polu $\mathbb{Z}_p$, gdzie $p$ jest 256-bitową liczbą pierwszą. "K" odnosi się do nazwiska jej wynalazcy, Neala Koblitza. Wreszcie, "1" oznacza, że jest to pierwsza wersja tej krzywej