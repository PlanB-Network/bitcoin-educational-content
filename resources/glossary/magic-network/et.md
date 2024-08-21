---
term: MAGIC NETWORK
---

Konstandid, mida kasutatakse Bitcoin'i protokollis, et tuvastada sõnumite vahetatavate sõlmede konkreetset võrku (mainnet, testnet, regtest...). Neid väärtusi kirjutatakse iga sõnumi algusesse, et hõlbustada nende tuvastamist andmevoos. Magic Network'id on kavandatud harva esinema tavalises suhtlusandmetes. Tõepoolest, need 4 baiti on ASCII-s haruldased, UTF-8-s kehtetud ja genereerivad väga suure 32-bitise täisarvu, olenemata andmete salvestusvormingust. Magic Network'id on (little-endian formaadis):
* Mainnet:

```text
f9beb4d9
```

* Testnet:

```text
0b110907
```

* Regtest:

```text
fabfb5da
```

> ► *Neid 4 baiti nimetatakse mõnikord ka "Magic Number", "Magic Bytes" või "Start String".*