---
term: REDE MÁGICA
---

Constantes usadas no protocolo Bitcoin para identificar a rede específica (mainnet, testnet, regtest...) de uma mensagem trocada entre nós. Esses valores são inscritos no início de cada mensagem para facilitar sua identificação no fluxo de dados. As Redes Mágicas são projetadas para serem raramente presentes em dados de comunicação ordinários. De fato, esses 4 bytes são infrequentes em ASCII, são inválidos em UTF-8 e geram um inteiro de 32 bits muito grande, independentemente do formato de armazenamento de dados. As Redes Mágicas são (no formato little-endian):
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

> ► *Esses 4 bytes são às vezes também chamados de "Número Mágico", "Bytes Mágicos" ou "String de Início".*