---
term: MAAGILINE VÕRK

---
Konstandid, mida kasutatakse Bitcoini protokollis konkreetse võrgu (mainnet, testnet, regtest...) tuvastamiseks, mille kaudu sõlmede vahel vahetatud sõnumid on pärit. Need väärtused kirjutatakse iga sõnumi algusesse, et hõlbustada nende tuvastamist andmevoos. Magic Networks on loodud nii, et need esinevad harva tavalistes sideandmetes. Tõepoolest, need 4 baiti on ASCII-keeles harva esinevad, UTF-8-keeles kehtetud ja tekitavad väga suure 32-bitise täisarvu, olenemata andmete salvestamise formaadist. Magic Networks on (little-endian formaadis):


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

> ► *Neid 4 baiti nimetatakse mõnikord ka "Magic Number", "Magic Bytes" või "Start String" *