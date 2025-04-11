---
term: MAGIC NETWORK

---
Constants used in the Bitcoin protocol to identify the specific network (mainnet, testnet, regtest...) of a message exchanged between nodes. These values are inscribed at the beginning of each message to facilitate their identification in the data stream. Magic Networks are designed to be rarely present in ordinary communication data. Indeed, these 4 bytes are infrequent in ASCII, are invalid in UTF-8, and generate a very large 32-bit integer, regardless of the data storage format. The Magic Networks are (in little-endian format):


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

> ► *These 4 bytes are sometimes also called "Magic Number," "Magic Bytes," or "Start String."*