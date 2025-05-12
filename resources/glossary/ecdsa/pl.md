---
term: ECDSA
---

Skrót od "Elliptic Curve Digital Signature Algorithm" Jest to algorytm podpisu cyfrowego oparty na kryptografii krzywej eliptycznej (ECC). Jest to wariant DSA (algorytmu podpisu cyfrowego). ECDSA wykorzystuje właściwości krzywych eliptycznych, aby zapewnić poziom bezpieczeństwa porównywalny z tradycyjnymi algorytmami klucza publicznego, takimi jak RSA, przy użyciu znacznie mniejszych rozmiarów kluczy. ECDSA umożliwia generowanie par kluczy (kluczy publicznych i prywatnych), a także tworzenie i weryfikację podpisów cyfrowych.


W kontekście Bitcoin ECDSA służy do wyprowadzania kluczy publicznych z kluczy prywatnych. Jest on również używany do podpisywania transakcji, aby spełnić wymagania skryptu do odblokowywania bitcoinów i ich wydawania. Krzywa eliptyczna używana w ECDSA Bitcoin to `secp256k1`, zdefiniowana równaniem $y^2 = x^3 + 7$. Algorytm ten był używany od momentu powstania Bitcoin w 2009 roku. Obecnie dzieli on swoje miejsce z protokołem Schnorra, innym algorytmem podpisu cyfrowego wprowadzonym wraz z Taproot w 2021 roku.