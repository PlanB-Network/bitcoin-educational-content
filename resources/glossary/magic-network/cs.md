---
term: MAGIC NETWORK

---
Konstanty používané v protokolu Bitcoin k identifikaci konkrétní sítě (mainnet, testnet, regtest...) zprávy vyměňované mezi uzly. Tyto hodnoty jsou zapsány na začátku každé zprávy, aby se usnadnila jejich identifikace v datovém toku. Magické sítě jsou navrženy tak, aby se v běžných komunikačních datech vyskytovaly jen zřídka. Tyto 4 bajty se totiž v ASCII vyskytují zřídka, v UTF-8 jsou neplatné a generují velmi velké 32bitové celé číslo bez ohledu na formát uložení dat. Magické sítě jsou (ve formátu little-endian):


- Hlavní síť:

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

> ► *Těmto 4 bajtům se někdy říká také "magické číslo", "magické bajty" nebo "počáteční řetězec".*