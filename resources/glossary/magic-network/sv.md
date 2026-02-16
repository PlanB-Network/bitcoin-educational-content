---
term: Magic network
definition: 4-byte konstanter som identifierar nätverket (mainnet, testnet, regtest) i meddelanden mellan noder.
---

Konstanter som används i Bitcoin-protokollet för att identifiera det specifika nätverket (Mainnet, Testnet, regtest...) för ett meddelande som utväxlas mellan noder. Dessa värden skrivs in i början av varje meddelande för att underlätta identifieringen av dem i dataströmmen. Magic Networks är utformade för att vara sällsynta i vanliga kommunikationsdata. Dessa 4 byte är sällsynta i ASCII, ogiltiga i UTF-8 och generate är ett mycket stort 32-bitars heltal, oavsett datalagringsformat. De magiska nätverken är (i little-endian-format):


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


> ► *Dessa 4 byte kallas ibland också "Magic Number", "Magic Bytes" eller "Start String"*