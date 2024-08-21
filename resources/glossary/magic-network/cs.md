---
term: MAGIC NETWORK
---

Konstanty používané v protokolu Bitcoinu pro identifikaci konkrétní sítě (mainnet, testnet, regtest...) zprávy vyměňované mezi uzly. Tyto hodnoty jsou zapsány na začátku každé zprávy, aby usnadnily jejich identifikaci v datovém toku. Magic Networks jsou navrženy tak, aby se v běžných komunikačních datech vyskytovaly jen zřídka. Skutečně, tyto 4 bajty jsou neobvyklé v ASCII, jsou neplatné v UTF-8 a generují velmi velké 32bitové číslo, bez ohledu na formát ukládání dat. Magic Networks jsou (ve formátu little-endian):
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

> ► *Tyto 4 bajty jsou někdy také nazývány "Magic Number," "Magic Bytes," nebo "Start String."*