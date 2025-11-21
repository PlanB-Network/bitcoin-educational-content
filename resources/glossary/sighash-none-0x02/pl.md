---
term: SIGHASH_NONE (0X02)
---

Typ flagi SigHash używanej w podpisach transakcji Bitcoin do wskazania, że podpis dotyczy wszystkich wejść transakcji, ale żadnego z jej wyjść. Użycie `SIGHASH_NONE` oznacza, że podpisujący zobowiązuje się tylko do danych wejściowych, pozwalając, aby dane wyjściowe pozostały nieokreślone lub modyfikowalne po podpisaniu. Ten rodzaj podpisu jest przydatny w przypadkach, gdy podpisujący chce upoważnić inne strony do decydowania o sposobie dystrybucji bitcoinów w transakcji.