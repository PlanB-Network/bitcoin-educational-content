---
term: HASH256
---

Função criptográfica usada para diversas aplicações no Bitcoin. Envolve a aplicação da função SHA256 duas vezes nos dados de entrada. A mensagem é passada por SHA256 uma vez, e o resultado desta operação é usado como entrada para uma segunda passagem por SHA256. O resultado desta função é, portanto, de 256 bits.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$