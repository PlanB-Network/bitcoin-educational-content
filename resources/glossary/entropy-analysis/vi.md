---
term: ENTROPY (ANALYSIS)

---
In the specific context of chain analysis, entropy is also the name of an indicator, derived from Shannon entropy, invented by LaurentMT. This indicator allows measuring the lack of knowledge analysts have about the exact configuration of a Bitcoin transaction. In other words, the higher the entropy of a transaction, the more difficult it becomes for analysts to identify the movements of bitcoins between inputs and outputs.

In practice, entropy reveals whether, from the perspective of an external observer, a transaction presents multiple possible interpretations, based solely on the amounts of inputs and outputs, without considering other external or internal patterns and heuristics. High entropy is then synonymous with better confidentiality for the transaction.

Entropy is defined as the binary logarithm of the number of possible combinations. Here is the formula used with $E$ representing the entropy of the transaction and $C$ the number of possible interpretations:

$$
E = \log_2(C)
$$

Taking into account the values of the UTXOs involved in the transaction, the number of interpretations $C$ represents the number of ways in which inputs can be associated with outputs. In other words, it determines the number of interpretations a transaction can elicit from the viewpoint of an external observer analyzing it.