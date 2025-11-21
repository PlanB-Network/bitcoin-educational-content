---
term: HRP (CZĘŚĆ CZYTELNA DLA CZŁOWIEKA)
---

HRP, skrót od "Human Readable Part", jest składnikiem adresów odbiorczych bech32 i bech32m (SegWit v0 i SegWit v1). HRP odnosi się do części Address, która jest specjalnie sformatowana tak, aby mogła być łatwo odczytana i zinterpretowana przez człowieka. Weźmy na przykład bech32 Bitcoin Address:


```text
bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwfqx5
```


W tym Address początkowe `bc` reprezentuje HRP. Ten prefiks pozwala szybko zidentyfikować, że przedstawiony ciąg znaków to Bitcoin Address, a nie coś innego.