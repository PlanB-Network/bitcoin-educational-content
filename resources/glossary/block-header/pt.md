---
term: BLOCK HEADER
---

O cabeçalho do bloco é uma estrutura de dados que serve como o principal componente na construção de um bloco Bitcoin. Cada bloco consiste em um cabeçalho e uma lista de transações. O cabeçalho do bloco contém informações cruciais que garantem a integridade e validade de um bloco dentro da blockchain. O cabeçalho do bloco contém 80 bytes de metadados e é composto pelos seguintes elementos:
* A versão do bloco;
* O hash do bloco anterior;
* A raiz da árvore de Merkle das transações;
* O carimbo de tempo do bloco;
* O alvo de dificuldade;
* O nonce.

Por exemplo, aqui está o cabeçalho do bloco número 785.530 em formato hexadecimal, minerado pela Foundry USA em 15 de abril de 2023:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Se desmembrarmos este cabeçalho, podemos reconhecer:
* A versão:

```text
00e0ff3f
```

* O hash anterior:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```

* A raiz de Merkle:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```

* O carimbo de tempo:

```text
bcb13a64
```

* O alvo:

```text
b2e00517
```

* O nonce:

```text
43f09a40
```

Para ser válido, um bloco deve ter um cabeçalho que, uma vez hasheado com `SHA256d`, produza um hash que seja menor ou igual ao alvo de dificuldade.

> ► *Em inglês, é referido como "Block Header".*