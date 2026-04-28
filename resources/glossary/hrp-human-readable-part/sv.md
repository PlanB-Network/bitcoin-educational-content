---
term: Hrp (human readable part)
definition: Läsbar prefix för bech32-adresser som gör det möjligt att identifiera typen av Bitcoin-adress.
---

HRP, som står för "Human Readable Part", är en komponent i mottagningsadresserna bech32 och bech32m (SegWit v0 och SegWit v1). HRP hänvisar till den del av Address som är specifikt formaterad för att lätt kunna läsas och tolkas av människor. Ta till exempel en bech32 Bitcoin Address:


```text
bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwfqx5
```


I denna Address representerar det inledande `bc` HRP. Detta prefix gör att man snabbt kan identifiera att den teckensträng som presenteras är en Bitcoin Address och inte något annat.