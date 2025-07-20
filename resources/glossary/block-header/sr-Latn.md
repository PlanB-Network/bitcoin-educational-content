---
term: ZAGLAVLJE BLOKA
---

Zaglavlje bloka je struktura podataka koja služi kao glavni komponent u konstrukciji Bitcoin bloka. Svaki blok se sastoji od zaglavlja i liste transakcija. Zaglavlje bloka sadrži ključne informacije koje osiguravaju integritet i validnost bloka unutar Blockchain. Zaglavlje bloka sadrži 80 bajtova metapodataka i sastoji se od sledećih Elements:


- Verzija bloka;
- Hash iz prethodnog bloka;
- Merkle Tree koren transakcija;
- Blok Timestamp;
- Ciljna težina;
- Nonce.


Na primer, ovo je zaglavlje bloka broj 785,530 u heksadecimalnom formatu, koji je iskopao Foundry USA 15. aprila 2023:


```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```


Ako razložimo ovaj naslov, možemo prepoznati:


- Verzija:


```text
00e0ff3f
```



- Prethodni Hash:


```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```



- Merkle Root:


```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```



- Timestamp:


```text
bcb13a64
```



- Meta:


```text
b2e00517
```



- Nonce:


```text
43f09a40
```


Da bi bio važeći, blok mora imati zaglavlje koje, kada se hešira sa `SHA256d`, proizvodi Hash koji je manji ili jednak cilju težine.


> ► *Na engleskom se to naziva "Block Header".*