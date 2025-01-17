---
term: HASH160

---
Função criptográfica utilizada na Bitcoin, nomeadamente para gerar endereços de receção Legacy e SegWit v0. Combina duas funções de hash que são executadas sucessivamente na entrada: primeiro SHA256, depois RIPEMD160. A saída desta função é, portanto, de 160 bits.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$