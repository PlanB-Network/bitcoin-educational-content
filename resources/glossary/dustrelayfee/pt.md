---
term: DUSTRELAYFEE

---
Uma regra de normalização utilizada pelos nós da rede para determinar o que consideram o "limite de pó" Este parâmetro define uma taxa em sats por kilobyte virtual (sats/kvB) que serve de referência para calcular se o valor de um UTXO é inferior às taxas necessárias para o incluir numa transação. De facto, uma UTXO é considerada "pó" na Bitcoin se necessitar de mais taxas para ser transferida do que o valor que ela própria representa. O cálculo deste limite é o seguinte:

```text
limit = (input size + output size) * fee rate
```

Como a taxa necessária para que uma transação seja incluída em um bloco Bitcoin varia constantemente, o parâmetro `DustRelayFee` permite que cada nó defina a taxa utilizada neste cálculo. Por padrão, no Bitcoin Core, este valor é definido como 3.000 sats/kvB. Por exemplo, para calcular o limite de poeira para uma entrada e saída P2PKH, que medem 148 e 34 bytes respetivamente, o cálculo seria:

```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Isto significa que o nó em questão não retransmitirá transacções que incluam um UTXO protegido por P2PKH cujo valor seja inferior a 546 sats.