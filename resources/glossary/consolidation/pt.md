---
termo: CONSOLIDAÇÃO
---

Uma transação específica na qual múltiplos pequenos UTXOs são mesclados em uma entrada para formar um único UTXO maior como saída. Esta operação é uma transação feita para a própria carteira do usuário. O objetivo da consolidação é aproveitar períodos em que as taxas na rede Bitcoin estão baixas para mesclar vários pequenos UTXOs em um maior em valor. Assim, antecipa despesas obrigatórias em caso de aumento das taxas, permitindo economia em taxas de transação futuras.

De fato, transações com muitas entradas são mais pesadas e, consequentemente, mais caras. Além da economia alcançável em taxas de transação, a consolidação é também uma forma de planejamento a longo prazo. Se sua carteira contém UTXOs muito pequenos, estes podem se tornar inutilizáveis se a rede Bitcoin entrar em um período prolongado de taxas altas. Por exemplo, se você precisar gastar um UTXO de 10.000 sats mas as taxas mínimas de mineração somarem 15.000 sats, a despesa excederia o valor do próprio UTXO. Esses pequenos UTXOs então se tornam economicamente irracionais para usar e permanecem inutilizáveis enquanto as taxas não diminuírem. Esses UTXOs são comumente referidos como "poeira". Ao consolidar regularmente seus pequenos UTXOs, você reduz esse risco associado ao aumento das taxas.

No entanto, é importante notar que transações de consolidação são reconhecíveis durante uma análise de cadeia. Tal transação indica uma Heurística de Propriedade de Entrada Comum (CIOH, na sigla em inglês), significando que as entradas da transação de consolidação são de propriedade de uma única entidade. Isso pode ter implicações em termos de privacidade para o usuário.

![](../../dictionnaire/assets/7.png)