---
term: REDE MÁGICA

---
Constantes utilizadas no protocolo Bitcoin para identificar a rede específica (mainnet, testnet, regtest...) de uma mensagem trocada entre nós. Estes valores são inscritos no início de cada mensagem para facilitar a sua identificação no fluxo de dados. As redes mágicas são concebidas para estarem raramente presentes nos dados de comunicação normais. De facto, estes 4 bytes são pouco frequentes em ASCII, são inválidos em UTF-8 e geram um número inteiro de 32 bits muito grande, independentemente do formato de armazenamento dos dados. As Redes Mágicas são (em formato little-endian):


- Rede principal:

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

> ► *Estes 4 bytes são por vezes também designados por "Magic Number", "Magic Bytes" ou "Start String"