---
term: MAGISK NETTVERK

---
Konstanter som brukes i Bitcoin-protokollen for å identifisere det spesifikke nettverket (mainnet, testnet, regtest...) for en melding som utveksles mellom noder. Disse verdiene er innskrevet i begynnelsen av hver melding for å gjøre det lettere å identifisere dem i datastrømmen. Magic Networks er utformet slik at de sjelden forekommer i vanlige kommunikasjonsdata. Disse fire byte er sjeldne i ASCII, er ugyldige i UTF-8 og genererer et svært stort 32-bits heltall, uansett datalagringsformat. De magiske nettverkene er (i little-endian-format):


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

> disse fire byte kalles også "Magic Number", "Magic Bytes" eller "Start String"