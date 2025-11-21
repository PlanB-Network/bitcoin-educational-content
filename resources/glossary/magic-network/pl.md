---
term: SIEĆ MAGICZNA
---

Stałe używane w protokole Bitcoin do identyfikacji konkretnej sieci (Mainnet, Testnet, regtest...) wiadomości wymienianej między węzłami. Wartości te są wpisywane na początku każdej wiadomości, aby ułatwić ich identyfikację w strumieniu danych. Magic Networks są zaprojektowane tak, aby rzadko występowały w zwykłych danych komunikacyjnych. Rzeczywiście, te 4 bajty są rzadkie w ASCII, są nieprawidłowe w UTF-8, a generate jest bardzo dużą 32-bitową liczbą całkowitą, niezależnie od formatu przechowywania danych. Magic Networks to (w formacie little-endian):


- Mainnet:


```text
f9beb4d9
```



- Testnet:


```text
0b110907
```



- Regtest:


```text
fabfb5da
```


> te 4 bajty są czasami nazywane "Magic Number", "Magic Bytes" lub "Start String"