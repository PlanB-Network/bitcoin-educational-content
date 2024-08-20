---
term: DUSTRELAYFEE
---

Uma regra de padronização usada pelos nós da rede para determinar o que eles consideram o "limite de poeira" (dust limit). Esse parâmetro estabelece uma taxa de fee em sats por kilobyte virtual (sats/kvB) que serve como referência para calcular se o valor de um UTXO é menor do que as taxas necessárias para incluí-lo em uma transação. De fato, um UTXO é considerado "poeira" no Bitcoin se ele requer mais em taxas para ser transferido do que o valor que ele representa. O cálculo deste limite é o seguinte:

```text
limite = (tamanho da entrada + tamanho da saída) * taxa de fee
```

Como a taxa de fee necessária para que uma transação seja incluída em um bloco do Bitcoin varia constantemente, o parâmetro `DustRelayFee` permite que cada nó defina a taxa de fee usada neste cálculo. Por padrão, no Bitcoin Core, esse valor é definido como 3.000 sats/kvB. Por exemplo, para calcular o limite de poeira para uma entrada e saída P2PKH, que medem 148 e 34 bytes respectivamente, o cálculo seria:

```text
limite (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Isso significa que o nó em questão não irá retransmitir transações que incluam um UTXO protegido por P2PKH cujo valor seja menor que 546 sats.