---
term: HASH256

---
Função criptográfica usada para várias aplicações no Bitcoin. Envolve a aplicação da função SHA256 duas vezes nos dados de entrada. A mensagem é passada uma vez pelo SHA256 e o resultado desta operação é utilizado como entrada para uma segunda passagem pelo SHA256. O resultado desta função é, portanto, 256 bits.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$