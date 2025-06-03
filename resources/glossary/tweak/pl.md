---
term: TWEAK
---

W kryptografii "tweakowanie" klucza publicznego polega na modyfikowaniu go przy użyciu wartości addytywnej zwanej "tweakiem", tak aby pozostał on użyteczny przy znajomości zarówno oryginalnego klucza prywatnego, jak i tweaku. Technicznie rzecz biorąc, tweak to wartość skalarna dodawana do oryginalnego klucza publicznego. Jeśli $P$ jest kluczem publicznym, a $t$ jest tweakiem, tweakowany klucz publiczny staje się :


$$
P' = P + tG
$$


Gdzie $G$ jest generatorem użytej krzywej eliptycznej. Ta operacja tworzy nowy klucz publiczny pochodzący z oryginału, zachowując pewne właściwości kryptograficzne, które pozwalają na jego użycie. Na przykład, metoda ta jest stosowana dla adresów Taproot (P2TR), aby umożliwić wydawanie albo poprzez przedstawienie podpisu Schnorra w tradycyjny sposób, albo poprzez spełnienie jednego z warunków określonych w Merkle Tree, znanym również jako "MAST".