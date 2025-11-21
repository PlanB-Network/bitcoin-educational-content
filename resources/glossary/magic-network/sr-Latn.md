---
term: MAGIC NETWORK
---

Konstante korišćene u Bitcoin protokolu za identifikaciju specifične mreže (Mainnet, Testnet, regtest...) poruke razmenjene između čvorova. Ove vrednosti su upisane na početku svake poruke kako bi se olakšala njihova identifikacija u toku podataka. Magic Networks su dizajnirane da budu retko prisutne u običnim komunikacionim podacima. Zaista, ovi 4 bajta su retki u ASCII, nevažeći su u UTF-8, a generate je veoma veliki 32-bitni ceo broj, bez obzira na format skladištenja podataka. Magic Networks su (u little-endian formatu):


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


> ► *Ova 4 bajta se ponekad nazivaju i "Magic Number," "Magic Bytes," ili "Start String."*