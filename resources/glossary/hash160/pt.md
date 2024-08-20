---
term: HASH160
---

Função criptográfica usada no Bitcoin, notavelmente para gerar endereços de recebimento Legacy e SegWit v0. Ela combina duas funções de hash que são executadas sucessivamente na entrada: primeiro SHA256, depois RIPEMD160. O resultado desta função é, portanto, de 160 bits.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$