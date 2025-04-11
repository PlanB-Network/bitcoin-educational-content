---
term: CONSOLIDAÇÃO

---
Uma transação específica na qual vários pequenos UTXOs são fundidos numa entrada para formar um único e maior UTXO como saída. Esta operação é uma transação feita para a própria carteira. O objetivo da consolidação é aproveitar os períodos em que as taxas na rede Bitcoin são baixas para fundir vários pequenos UTXOs num único de maior valor. Desta forma, antecipa as despesas obrigatórias em caso de aumento das taxas, permitindo poupar nas taxas de transação futuras.

De facto, as transacções com muitos inputs são mais pesadas e, consequentemente, mais caras. Para além das poupanças que se podem obter nas taxas de transação, a consolidação é também uma forma de planeamento a longo prazo. Se a sua carteira contém UTXOs muito pequenos, estes podem tornar-se inutilizáveis se a rede Bitcoin entrar num período prolongado de taxas elevadas. Por exemplo, se precisar de gastar um UTXO de 10.000 sats, mas as taxas mínimas de mineração ascendem a 15.000 sats, a despesa excederia o valor do próprio UTXO. Estes pequenos UTXOs tornam-se então economicamente irracionais para usar e permanecem inutilizáveis enquanto as taxas não diminuírem. Estes UTXOs são vulgarmente designados por "pó" Ao consolidar regularmente os seus pequenos UTXOs, reduz este risco associado ao aumento das comissões.

No entanto, é importante notar que as transacções de consolidação são reconhecíveis durante uma análise em cadeia. Uma transação deste tipo indica uma Heurística de Propriedade de Entrada Comum (CIOH), o que significa que as entradas da transação de consolidação são propriedade de uma única entidade. Isto pode ter implicações em termos de privacidade para o utilizador.

![](../../dictionnaire/assets/7.webp)